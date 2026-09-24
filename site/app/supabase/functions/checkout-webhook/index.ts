// Webhook do checkout → libera ou bloqueia o acesso na tabela `members`.
// Deploy: supabase functions deploy checkout-webhook --no-verify-jwt
// Segredos: supabase secrets set WEBHOOK_TOKEN=... SUPABASE_SERVICE_ROLE_KEY=... SUPABASE_URL=...
//           supabase secrets set GIFT_OFFER_IDS=<ids das ofertas/bumps "presentear uma amiga">   (vários: separe por vírgula)
//
// Quando a compra é da oferta com presente, além de liberar a compradora a função cria um código
// na tabela `gifts`. Ela vê o código na área de membros e manda pra amiga, que resgata ao criar a conta.
// O mesmo produto de presente comprado sozinho (link próprio, depois da compra) só gera o código:
// um por compra, quantas vezes ela quiser presentear.
//
// Configure na plataforma de pagamento (Hotmart, Kiwify, Eduzz...) a URL:
//   https://<projeto>.supabase.co/functions/v1/checkout-webhook?token=<WEBHOOK_TOKEN>
//
// Cada plataforma manda um JSON diferente. A função normaliza os campos mais comuns
// e trata: compra aprovada → ativa; reembolso, chargeback, cancelamento, assinatura atrasada → desativa.

import { createClient } from "npm:@supabase/supabase-js@2";

const ATIVA = ["approved", "purchase_approved", "paid", "order.paid", "subscription_renewed", "completed", "compra_aprovada"];
const DESATIVA = ["refunded", "purchase_refunded", "chargeback", "chargedback", "purchase_chargeback", "canceled", "cancelled", "subscription_canceled", "subscription_cancellation", "purchase_canceled", "expired", "subscription_expired", "overdue", "purchase_delayed", "reembolso", "cancelamento"];

// Código curto e legível, sem letras que confundem (0/O, 1/I).
function codigo(): string {
  const alf = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
  const buf = new Uint8Array(8); crypto.getRandomValues(buf);
  return Array.from(buf, (b) => alf[b % alf.length]).join("");
}

function pick(obj: any, paths: string[]): string | undefined {
  for (const p of paths) {
    const v = p.split(".").reduce((o, k) => (o == null ? undefined : o[k]), obj);
    if (v != null && String(v).trim() !== "") return String(v);
  }
  return undefined;
}

Deno.serve(async (req) => {
  const url = new URL(req.url);
  const token = Deno.env.get("WEBHOOK_TOKEN");
  if (!token || url.searchParams.get("token") !== token) {
    return new Response("unauthorized", { status: 401 });
  }
  let body: any = {};
  try { body = await req.json(); } catch { return new Response("bad json", { status: 400 }); }

  // Campos normalizados (Hotmart, Kiwify, Eduzz e genéricos)
  const email = pick(body, ["data.buyer.email", "Customer.email", "buyer.email", "customer.email", "email", "data.customer.email"])?.toLowerCase();
  const status = (pick(body, ["event", "webhook_event_type", "order_status", "status", "data.purchase.status", "type"]) || "").toLowerCase();
  const provider = pick(body, ["provider"]) || (body.data?.product ? "hotmart" : body.order_id ? "kiwify" : "generic");
  const ref = pick(body, ["data.purchase.transaction", "order_id", "id", "data.subscription.subscriber.code", "transaction"]);

  if (!email) return new Response("no email", { status: 400 });

  const name = pick(body, ["data.buyer.name", "Customer.full_name", "Customer.first_name", "buyer.name", "customer.name", "name"]);
  const offer = (pick(body, ["data.purchase.offer.code", "data.product.id", "product_id", "Product.product_id", "offer_id", "data.offer.id", "product.id"]) || "").toLowerCase();
  // Ofertas e order bumps: junta o id principal com os ids de itens extras que a plataforma mandar.
  const extras: string[] = [];
  for (const arr of [body.data?.purchase?.order_bump?.offers, body.order_bumps, body.data?.order_bumps, body.items, body.data?.items, body.Product?.order_bumps]) {
    if (Array.isArray(arr)) for (const it of arr) { const id = pick(it, ["code", "offer_code", "product_id", "id", "offer.code"]); if (id) extras.push(id.toLowerCase()); }
  }
  const ids = [offer, ...extras].filter(Boolean);
  const lista = (k: string) => (Deno.env.get(k) || "").toLowerCase().split(",").map((x) => x.trim()).filter(Boolean);
  const giftOffers = lista("GIFT_OFFER_IDS");
  const comPresente = giftOffers.some((g) => ids.includes(g));
  // Compra só do presente (produto principal do pedido é o "presentear uma amiga"): a compradora já é
  // membro. Não mexe na conta dela, só cria (ou cancela) o convite. Assim ela pode comprar quantos quiser.
  const soPresente = comPresente && giftOffers.includes(offer);

  const ativa = ATIVA.some((s) => status.includes(s));
  const desativa = DESATIVA.some((s) => status.includes(s));
  if (!ativa && !desativa) return new Response("ignored: " + status, { status: 200 });

  const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  if (!soPresente) {
    const { error } = await sb.from("members").upsert(
      { email, active: ativa, plan: "travessia" + (comPresente ? "+amiga" : ""), provider, provider_ref: ref },
      { onConflict: "email" },
    );
    if (error) return new Response(error.message, { status: 500 });
  }

  let gift: string | undefined;
  if (comPresente && ativa) {
    // Um código por transação: se o webhook repetir, não duplica.
    const { data: existing } = ref ? await sb.from("gifts").select("code").eq("provider_ref", ref).maybeSingle() : { data: null };
    if (existing) gift = existing.code;
    else {
      gift = codigo();
      const { error: ge } = await sb.from("gifts").insert({ code: gift, buyer_email: email, buyer_name: name, provider, provider_ref: ref });
      if (ge) return new Response(ge.message, { status: 500 });
    }
  }
  if (desativa && ref) {
    // Reembolso da compradora cancela o presente e bloqueia a amiga, se ela já tiver resgatado.
    const { data: g } = await sb.from("gifts").update({ active: false }).eq("provider_ref", ref).select("claimed_email").maybeSingle();
    if (g?.claimed_email) await sb.from("members").update({ active: false }).eq("email", g.claimed_email).eq("provider", "gift");
  }
  return new Response(JSON.stringify({ ok: true, email, active: ativa, gift }), { headers: { "content-type": "application/json" } });
});
