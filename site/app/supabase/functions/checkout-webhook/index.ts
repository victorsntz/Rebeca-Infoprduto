// Webhook do checkout → libera ou bloqueia o acesso na tabela `members`.
// Deploy: supabase functions deploy checkout-webhook --no-verify-jwt
// Segredos: supabase secrets set WEBHOOK_TOKEN=... SUPABASE_SERVICE_ROLE_KEY=... SUPABASE_URL=...
//
// Configure na plataforma de pagamento (Hotmart, Kiwify, Eduzz...) a URL:
//   https://<projeto>.supabase.co/functions/v1/checkout-webhook?token=<WEBHOOK_TOKEN>
//
// Cada plataforma manda um JSON diferente. A função normaliza os campos mais comuns
// e trata: compra aprovada → ativa; reembolso, chargeback, cancelamento, assinatura atrasada → desativa.

import { createClient } from "npm:@supabase/supabase-js@2";

const ATIVA = ["approved", "purchase_approved", "paid", "order.paid", "subscription_renewed", "completed", "compra_aprovada"];
const DESATIVA = ["refunded", "purchase_refunded", "chargeback", "purchase_chargeback", "canceled", "cancelled", "subscription_canceled", "subscription_cancellation", "purchase_canceled", "expired", "subscription_expired", "overdue", "purchase_delayed", "reembolso", "cancelamento"];

function pick(obj: any, paths: string[]): string | undefined {
  for (const p of paths) {
    const v = p.split(".").reduce((o, k) => (o == null ? undefined : o[k]), obj);
    if (v != null && String(v).trim() !== "") return String(v);
  }
  return undefined;
}

Deno.serve(async (req) => {
  const url = new URL(req.url);
  if (url.searchParams.get("token") !== Deno.env.get("WEBHOOK_TOKEN")) {
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

  const ativa = ATIVA.some((s) => status.includes(s));
  const desativa = DESATIVA.some((s) => status.includes(s));
  if (!ativa && !desativa) return new Response("ignored: " + status, { status: 200 });

  const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { error } = await sb.from("members").upsert(
    { email, active: ativa, plan: "travessia", provider, provider_ref: ref },
    { onConflict: "email" },
  );
  if (error) return new Response(error.message, { status: 500 });
  return new Response(JSON.stringify({ ok: true, email, active: ativa }), { headers: { "content-type": "application/json" } });
});
