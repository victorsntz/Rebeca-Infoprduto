/* Área de membros · De Tola a Virtuosa
 * App de página única, sem build. Conteúdo vem de content.json (o mesmo do caderno impresso).
 */
(async function () {
  const S = window.DTV_STORE;
  const CFG = window.DTV_CONFIG || {};
  const app = document.getElementById("app");
  const toastEl = document.getElementById("toast");
  const C = window.DTV_CONTENT || (await fetch("content.json").then((r) => r.json()));
  const TOTAL = 40;

  const st = { session: null, member: null, profile: null, entries: {}, prep: {} };

  // ------------------------------------------------------------------ utils
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const bloco = (d) => C.blocos.find((b) => d >= b.inicio && d <= b.fim);
  const pad = (n) => String(n).padStart(2, "0");
  const isoToday = () => { const d = new Date(); return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`; };
  const parseISO = (s) => { const [y, m, d] = s.split("-").map(Number); return new Date(y, m - 1, d); };
  const fmt = (iso) => { if (!iso) return ""; const d = parseISO(iso); return d.toLocaleDateString("pt-BR", { day: "2-digit", month: "long" }); };
  function todayIdx() {
    if (!st.profile || !st.profile.start_date) return 0;
    const diff = Math.floor((parseISO(isoToday()) - parseISO(st.profile.start_date)) / 86400000) + 1;
    return Math.max(0, Math.min(TOTAL, diff));
  }
  const dayDate = (d) => { if (!st.profile || !st.profile.start_date) return ""; const dt = parseISO(st.profile.start_date); dt.setDate(dt.getDate() + d - 1); return dt.toLocaleDateString("pt-BR", { weekday: "long", day: "2-digit", month: "long" }); };
  const entry = (d) => st.entries[d] || {};
  const isDone = (d) => !!entry(d).done;
  const doneCount = () => Object.keys(st.entries).filter((d) => st.entries[d].done).length;
  const streak = () => { let s = 0; for (let d = todayIdx(); d >= 1; d--) { if (isDone(d)) s++; else if (d !== todayIdx()) break; } return s; };
  const firstName = () => ((st.profile && st.profile.name) || (st.session && st.session.name) || "").split(" ")[0];

  let toastT;
  function isoShift(days) { const d = new Date(); d.setDate(d.getDate() + days); return d.toISOString().slice(0, 10); }
  function toast(msg, err) { toastEl.textContent = msg; toastEl.hidden = false; toastEl.className = "toast" + (err ? " err" : ""); clearTimeout(toastT); toastT = setTimeout(() => (toastEl.hidden = true), 2200); }
  const debounce = (fn, ms) => { let t; return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); }; };

  const ICO = {
    inicio: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="m3 11 9-8 9 8v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg>',
    hoje: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/></svg>',
    travessia: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 20c3-6 6-9 9-9s6 3 9 9"/><path d="M12 3v8"/><path d="m8 7 4-4 4 4"/></svg>',
    prep: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 3h9l5 5v13H6z"/><path d="M14 3v6h6M9 13h6M9 17h6"/></svg>',
    aulas: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="14" height="14" rx="2"/><path d="m17 10 4-2v8l-4-2z"/></svg>',
    imprimir: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M6 14h12v7H6z"/></svg>',
    conta: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
    play: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>',
    left: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18"><path d="m15 5-7 7 7 7"/></svg>',
    right: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18"><path d="m9 5 7 7-7 7"/></svg>',
  };
  const LOGO = `<img src="../assets/logo.svg" alt="">`;
  const verse = (t, r, cls = "") => `<p class="verse ${cls}">“${esc(t)}”<span class="verse-ref">${esc(r)}</span></p>`;
  const chips = (items, group, selected, cls = "", single = false) =>
    `<div class="chips">${items.map((i) => `<button type="button" class="chip ${cls} ${(single ? selected === i : (selected || []).includes(i)) ? "on" : ""}" data-chip="${esc(group)}" data-val="${esc(i)}" data-single="${single ? 1 : 0}">${esc(i)}</button>`).join("")}</div>`;

  // ------------------------------------------------------------------ boot
  // Código de presente vindo do link (#/resgatar/CODIGO) fica guardado até a amiga entrar.
  function pendingGift() { const m = location.hash.match(/^#\/?resgatar\/([A-Za-z0-9]+)/); if (m) { try { localStorage.setItem("dtv:gift", m[1].toUpperCase()); } catch {} } try { return localStorage.getItem("dtv:gift"); } catch { return null; } }
  async function tryClaim() {
    const code = pendingGift(); if (!code) return;
    const r = await S.claimGift(st.session.email, code);
    try { localStorage.removeItem("dtv:gift"); } catch {}
    if (r.ok) { toast(`Presente de ${r.from} resgatado. Bem-vinda à travessia.`); st.member = await S.membership(st.session.email); }
    else toast(r.error, true);
    if (/resgatar/.test(location.hash)) location.hash = "";
  }
  async function boot() {
    st.session = await S.session();
    if (!st.session) return renderAuth(pendingGift() ? "criar" : "entrar");
    await tryClaim();
    st.member = await S.membership(st.session.email);
    if (!st.member.active) return renderInactive();
    [st.profile, st.entries, st.prep] = await Promise.all([S.getProfile(st.session.email), S.getEntries(st.session.email), S.getPrep(st.session.email)]);
    if (!st.profile || !st.profile.name) return renderOnboarding();
    route();
  }
  window.addEventListener("hashchange", () => { if (st.session && st.profile && st.profile.name) route(); });

  // ------------------------------------------------------------------ auth
  function renderAuth(tab = "entrar", err = "") {
    document.body.classList.add("no-shell");
    app.innerHTML = `
    <div class="auth">
      <div class="side"><div class="frame"></div>
        <a class="logo" href="../"><img src="../assets/logo.svg" alt=""><span>De Tola a Virtuosa<small>Rebeca Fortunato</small></span></a>
        <div>
          <span class="eyebrow" style="color:var(--dourado-vivo)">Área de membros · 40 dias no deserto</span>
          <h1>A imatura espera ter vontade.<br>A <em class="gold">sábia</em> começa.</h1>
          <div class="mockstack" aria-hidden="true">
            <img src="../assets/img/mural.png" alt="">
            <img src="../assets/img/prova.png" alt="">
            <img src="../assets/img/travessia.png" alt="">
            <img src="../assets/img/dia.png" alt="">
          </div>
          <p class="mockcap">Página do dia, mapa dos 40 dias, abertura de prova e mural: tudo do caderno impresso, aqui no celular.</p>
        </div>
        ${verse(C.versiculo_capa.texto, C.versiculo_capa.ref)}
      </div>
      <div class="form"><div>
        ${S.mode === "local" ? `<div class="demo"><b>Modo demonstração.</b> Sem servidor conectado, tudo fica salvo só neste navegador. Crie qualquer e-mail e senha pra testar.</div>` : ""}
        ${pendingGift() ? `<div class="gift-note"><b>Você ganhou um presente.</b> Alguém te chamou pra fazer os 40 dias. Crie sua conta (ou entre) e o código <code>${esc(pendingGift())}</code> libera o seu acesso na hora.</div>` : ""}
        <div class="tabs"><button data-act="tab" data-tab="entrar" class="${tab === "entrar" ? "on" : ""}">Entrar</button><button data-act="tab" data-tab="criar" class="${tab === "criar" ? "on" : ""}">Criar conta</button></div>
        <form id="authform" data-tab="${tab}">
          ${tab === "criar" ? `<div class="field"><label class="label" for="f-name">Seu nome</label><input id="f-name" type="text" name="name" required autocomplete="name" placeholder="Como você quer ser chamada"></div>` : ""}
          <div class="field"><label class="label" for="f-email">E-mail</label><input id="f-email" type="email" name="email" required autocomplete="email" placeholder="o mesmo da compra"></div>
          <div class="field"><label class="label" for="f-pass">Senha</label><input id="f-pass" type="password" name="password" required minlength="6" autocomplete="${tab === "criar" ? "new-password" : "current-password"}" placeholder="mínimo 6 caracteres"></div>
          ${err ? `<p class="err">${esc(err)}</p>` : ""}
          <button class="btn block" type="submit" style="margin-top:0.6rem">${tab === "criar" ? "Criar minha conta" : "Entrar na travessia"}</button>
          ${tab === "entrar" ? `<p class="muted" style="font-size:0.85rem;margin-top:1rem;text-align:center"><button type="button" class="linklike" data-act="reset">Esqueci a senha</button></p>` : ""}
        </form>
      </div></div>
    </div>`;
    startFan();
  }

  // Leque de páginas na tela de entrada: a de trás vem pra frente a cada poucos segundos.
  let fanTimer = null;
  function startFan() {
    clearInterval(fanTimer);
    const stack = app.querySelector(".mockstack");
    if (!stack || (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches)) return;
    fanTimer = setInterval(() => {
      const s = app.querySelector(".mockstack");
      if (!s) { clearInterval(fanTimer); return; }
      const first = s.firstElementChild;
      first.classList.add("out");
      setTimeout(() => { s.appendChild(first); first.classList.remove("out"); }, 500);
    }, 3200);
  }

  function renderInactive() {
    app.innerHTML = `<div class="inactive"><div class="card">
      ${LOGO.replace("<img", '<img style="width:48px;margin:0 auto 1rem"')}
      <h2>Seu acesso não está ativo</h2>
      <p>A conta <b>${esc(st.session.email)}</b> existe, mas não encontramos uma assinatura ativa. Se você acabou de comprar, aguarde alguns minutos. Se cancelou ou pediu reembolso, o acesso foi encerrado.</p>
      ${CFG.CHECKOUT_URL ? `<a class="btn gold block" href="${esc(CFG.CHECKOUT_URL)}">Quero ativar meu acesso</a>` : ""}
      <form id="claimform" class="claim"><label class="label" for="c-code" style="color:rgba(249,245,238,0.8)">Ganhou de presente? Digite o código</label><div class="row-inline"><input id="c-code" type="text" name="code" placeholder="AMIGA123" autocomplete="off" required><button class="btn gold sm" type="submit">Resgatar</button></div></form>
      <p style="margin-top:1rem;font-size:0.85rem">Precisa de ajuda? <a href="mailto:${esc(CFG.SUPORTE_EMAIL || "")}">${esc(CFG.SUPORTE_EMAIL || "fale com o suporte")}</a></p>
      <button class="btn ghost sm" data-act="logout" style="margin-top:0.8rem;color:var(--creme)">Sair</button>
    </div></div>`;
  }

  function renderOnboarding() {
    app.innerHTML = `
    <div class="auth"><div class="side"><div class="frame"></div>
      <a class="logo" href="../"><img src="../assets/logo.svg" alt=""><span>De Tola a Virtuosa<small>Rebeca Fortunato</small></span></a>
      <div><span class="eyebrow" style="color:var(--dourado-vivo)">Antes de tudo</span><h1>Bem-vinda,<br><em class="gold">${esc(firstName() || "mulher")}</em>.</h1>
      <p style="color:rgba(249,245,238,0.85);max-width:44ch">Quatro provas de dez dias. Um minuto por dia pra marcar. Primeiro as páginas de preparação, depois o dia 1. Igual ao caderno impresso.</p></div>
      ${verse("Ensina-nos a contar os nossos dias, de tal maneira que alcancemos corações sábios.", "Salmo 90:12")}
    </div>
    <div class="form"><div>
      <form id="onboard">
        <div class="field"><label class="label" for="o-name">Como você quer ser chamada</label><input id="o-name" type="text" name="name" value="${esc(st.session.name || "")}" required></div>
        
        <div class="field"><span class="label">Onde eu estou hoje</span>${chips(["Solteira", "Namorando", "Noiva", "Casada", "Mãe"], "fase", [], "", false)}</div>

        <button class="btn block" type="submit">Começar a travessia</button>
      </form>
    </div></div></div>`;
  }

  // ------------------------------------------------------------------ shell
  const NAV = [["inicio", "Início", ICO.inicio], ["prep", "Preparação", ICO.prep], ["dia", "Hoje", ICO.hoje], ["travessia", "Travessia", ICO.travessia], ["aulas", "Aulas", ICO.aulas], ["imprimir", "Imprimir", ICO.imprimir], ["conta", "Conta", ICO.conta]];
  const LOCK = '<svg class="lock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>';
  function navLink(k, l, i, current, t) {
    const locked = !prepDone() && (k === "dia" || k === "travessia");
    const href = locked ? "#/prep" : "#/" + (k === "dia" ? "dia/" + Math.max(1, t) : k);
    return `<a href="${href}" class="${current === k ? "on" : ""} ${locked ? "locked" : ""}" ${locked ? 'title="Abre depois da preparação"' : ""}>${i}<span>${l}</span>${locked ? LOCK : ""}</a>`;
  }
  function shell(view, current, accent = "rubi") {
    const t = todayIdx();
    const nav = (cls) => NAV.map(([k, l, i]) => navLink(k, l, i, current, t)).join("");
    app.innerHTML = `<div class="shell c-${accent}">
      <aside class="side-nav">
        <a class="logo" href="#/inicio">${LOGO}<span>De Tola a Virtuosa<small>Rebeca Fortunato</small></span></a>
        <nav>${nav()}</nav>
        <div class="dayline">${!st.profile.start_date ? "Preparação em andamento" : t === 0 ? "Sua travessia começa em " + fmt(st.profile.start_date) : `<b>Dia ${t}</b>de 40 · ${doneCount()} marcados`}<div class="progress"><i style="width:${(doneCount() / TOTAL) * 100}%"></i></div></div>
      </aside>
      <div>
        <header class="topbar"><a class="logo" href="#/inicio">${LOGO}<span>De Tola a Virtuosa<small>Rebeca Fortunato</small></span></a><span class="daypill">${t === 0 ? "Começa " + fmt(st.profile.start_date) : "Dia " + t + " de 40"}</span></header>
        <main class="content">${view}</main>
      </div>
      <nav class="bottom-nav">${NAV.slice(0, 5).map(([k, l, i]) => navLink(k, l, i, current, t)).join("")}</nav>
    </div>`;
    window.scrollTo(0, 0);
  }

  function route() {
    const h = location.hash.replace(/^#\/?/, "") || "inicio";
    const [name, arg] = h.split("/");
    const t = todayIdx();
    if (name === "dia") return viewDia(Math.min(TOTAL, Math.max(1, parseInt(arg || t || 1, 10))));
    if (name === "prova") return viewProva(parseInt(arg, 10) || 1);
    const views = { inicio: viewInicio, travessia: viewTravessia, prep: viewPrep, aulas: viewAulas, imprimir: viewImprimir, conta: viewConta, presente: viewPresente, resgatar: viewInicio };
    (views[name] || viewInicio)();
  }

  // ------------------------------------------------------------------ início
  function prepStatus() {
    const p = st.prep;
    const has = (k, f) => p[k] && p[k][f] && String(p[k][f]).trim().length > 0;
    return [
      ["compromisso", "Compromisso", has("compromisso", "assinatura")],
      ["tola", "Tola ou virtuosa", has("tola", "linha")],
      ["identidade", "Identidade", has("identidade", "hoje") && has("identidade", "deus")],
      ["proposito", "Propósito e limites", has("proposito", "frase")],
      ["regras", "Regras e quadro dos sonhos", p.regras && ((p.regras.marcadas || []).length > 0 || has("regras", "minhas"))],
      ["carta", "Carta pro dia 40", has("carta", "texto")],
      ["retrato1", "Retrato do dia 1", p.retrato1 && p.retrato1.notas && Object.keys(p.retrato1.notas).length >= 5],
    ];
  }
  function viewInicio() {
    S.getGifts(st.session.email).then((gs) => {
      const g = (gs || []).find((x) => !x.claimed_email);
      const slot = document.getElementById("gift-slot");
      if (!slot) return;
      if (g) slot.innerHTML = `<a class="card gift-cta" href="#/presente"><div><span class="eyebrow">Fazer junto</span><b>Você tem um presente pra dar</b><span class="muted">Mande o código ${esc(g.code)} pra sua amiga e façam os 40 dias juntas.</span></div><span class="btn ghost sm">Mandar</span></a>`;
      else slot.innerHTML = `<a class="card gift-cta" href="#/presente"><div><span class="eyebrow">Fazer junto</span><b>Presenteie uma amiga</b><span class="muted">Chame alguém pra atravessar o deserto com você. Um acesso completo por ${esc(CFG.GIFT_PRICE || "R$ 27")}.</span></div><span class="btn ghost sm">Ver</span></a>`;
    }).catch(() => {});
    const t = todayIdx();
    const b = bloco(Math.max(1, t));
    const ps = prepStatus();
    const pending = ps.filter((x) => !x[2]);
    const todayEntry = entry(t);
    const html = `
      <div id="gift-slot"></div>
      <div class="hero-card">
        <div>
          <span class="eyebrow">${!st.profile.start_date ? "Antes do dia 1" : t === 0 ? "Sua travessia começa " + fmt(st.profile.start_date) : `Prova ${b.num} · ${esc(b.lugar)} · ${esc(b.virtude)}`}</span>
          <h2>${!prepDone() ? `Antes do dia 1, ${esc(firstName())}.` : !st.profile.start_date ? `Preparação pronta, ${esc(firstName())}. Quando começa?` : t === 0 ? `Preparada, ${esc(firstName())}?` : todayEntry.done ? `Dia ${t} marcado, ${esc(firstName())}.` : `Dia ${t}, ${esc(firstName())}.`}</h2>
          <p>${!prepDone() ? "Igual ao caderno: primeiro as páginas de preparação, depois o dia 1. Compromisso, identidade, propósito, regras, quadro dos sonhos, carta e retrato. Uma tarde resolve." : !st.profile.start_date ? "As sete páginas estão preenchidas. Escolha se o dia 1 é hoje ou amanhã, e o caderno se organiza a partir daí. Dá pra ajustar em Conta se errar." : t === 0 ? "Use estes dias pra preencher a preparação. É a parte que a maioria pula e que decide tudo." : todayEntry.done ? "Fidelidade é isso: o dia " + t + " com a mesma seriedade do dia 1." : esc(C.desafios[t - 1])}</p>
          ${!prepDone() ? `<a class="btn gold" href="#/prep">Continuar a preparação (${prepPending()} ${prepPending() === 1 ? "página" : "páginas"})</a>` : !st.profile.start_date ? `<div class="btns"><button class="btn gold" data-act="start" data-when="0">Meu dia 1 é hoje</button><button class="btn ghost" data-act="start" data-when="1" style="color:var(--creme)">Começo amanhã</button></div>` : t > 0 ? `<a class="btn gold" href="#/dia/${t}">${todayEntry.done ? "Rever o dia de hoje" : "Marcar o dia de hoje"}</a>` : `<a class="btn gold" href="#/prep">Rever a preparação</a>`}
        </div>
        <div class="ring" style="--p:${(doneCount() / TOTAL) * 100}"><div><b>${doneCount()}</b><small>de 40</small></div></div>
      </div>
      <div class="stats" style="margin:1.2rem 0">
        <div class="card"><b>${streak()}</b><span>dias seguidos</span></div>
        <div class="card"><b>${t}</b><span>dia de hoje</span></div>
        <div class="card"><b>${Math.max(0, TOTAL - t)}</b><span>dias pela frente</span></div>
      </div>
      <div class="two">
        <div class="stack">
          <a class="prova-mini c-${b.cor}" href="#/prova/${b.num}" style="text-decoration:none">
            <span class="eyebrow">Prova ${b.num} de 4 · dias ${b.inicio} a ${b.fim}</span>
            <h3>${esc(b.lugar)}</h3><div class="v">${esc(b.virtude)} · ${esc(b.sub)}</div>
            <p>${esc(b.chamada)}. Com ${esc(b.mulher)}.</p>
          </a>
          <div class="card">${verse(b.versiculo, b.ref)}</div>
        </div>
        <div class="card">
          <span class="eyebrow">Preparação${pending.length ? ` · ${pending.length} pendente${pending.length > 1 ? "s" : ""}` : " · completa"}</span>
          ${ps.map(([k, l, ok]) => `<a class="todo ${ok ? "ok" : ""}" href="#/prep"><span class="dot"></span><span>${esc(l)}</span><small>${ok ? "feito" : "fazer"}</small></a>`).join("")}
        </div>
      </div>`;
    shell(html, "inicio", b.cor);
  }

  // ------------------------------------------------------------------ dia
  function viewDia(d) {
    if (!prepDone()) { toast("Antes do dia 1, preencha a preparação. Faltam " + prepPending() + ".", true); location.hash = "#/prep"; return viewPrep(); }
    const t = todayIdx();
    const b = bloco(d);
    const nav = `<div class="daynav">${d > 1 ? `<a href="#/dia/${d - 1}" aria-label="Dia anterior">${ICO.left}</a>` : `<span>${ICO.left}</span>`}${d < TOTAL && d < t ? `<a href="#/dia/${d + 1}" aria-label="Próximo dia">${ICO.right}</a>` : `<span>${ICO.right}</span>`}</div>`;
    const head = `<div class="day-head">
      <div><div class="num"><small>Dia</small>${pad(d)}<small>de 40</small></div><div class="muted" style="font-size:0.85rem;margin-top:0.4rem">${esc(dayDate(d))}</div></div>
      <div style="display:flex;gap:1rem;align-items:flex-end"><div class="meta"><b>${esc(b.virtude)} · ${esc(b.lugar)}</b><span>Prova ${b.num} · ${esc(b.chamada)}</span></div>${nav}</div>
    </div>`;
    if (d > t) {
      shell(head + `<div class="day-locked"><div class="big">${pad(d)}</div><h2>Ainda não.</h2><p class="muted">Este dia abre ${esc(dayDate(d))}. Uma página por dia, sem adiantar. A prova é de fidelidade, não de velocidade.</p><a class="btn" href="#/dia/${Math.max(1, t)}">Voltar pro dia de hoje</a></div>`, "dia", b.cor);
      return;
    }
    const en = entry(d);
    const cl = en.checklist || {};
    const pil = Object.entries(C.checklist).map(([k, items]) => `<div class="p-${k}"><span class="eyebrow">${k === "espirito" ? "Espírito" : k[0].toUpperCase() + k.slice(1)}</span>${items.map((it, i) => `<label class="check ${cl[k] && cl[k][i] ? "on" : ""}" data-check="${k}:${i}"><span class="box"></span><span>${esc(it)}</span></label>`).join("")}</div>`).join("");
    const html = head + `
      <div class="two">
        <div>
          <div class="box reading"><span class="eyebrow">Leitura de hoje</span><div class="txt">${esc(C.leituras[d - 1])}</div><div class="tema">${esc((C.leituras_tema || [])[d - 1] || "")}</div></div>
          <div class="box ch"><span class="eyebrow">Desafio do dia</span><div class="txt">${esc(C.desafios[d - 1])}</div>
            <label class="check ${en.desafio ? "on" : ""}" data-check="desafio" style="margin-top:0.6rem"><span class="box"></span><span>Fiz o desafio</span></label></div>
          <div class="pillars">${pil}</div>
          ${verse(b.versiculo, b.ref, "lverse")}
        </div>
        <div>
          <div class="row"><span class="label">Hoje eu me senti <span class="hint">toque pra marcar</span></span>${chips(C.senti, "senti", en.senti)}</div>
          <div class="row"><span class="label">O que pesou hoje</span>${chips(C.pesou, "pesou", en.pesou, "soft")}</div>
          <div class="row"><span class="label">${esc(b.virtude)} hoje</span>${chips(C.virtude_opcoes, "virtude", en.virtude, "acc", true)}</div>
          <div class="row"><label class="label" for="e-grat">Sou grata por</label><textarea id="e-grat" class="lined" data-entry="gratidao" rows="2">${esc(en.gratidao)}</textarea></div>
          <div class="row"><label class="label" for="e-dif">Minha maior dificuldade hoje <span class="hint">e o que ela me mostrou</span></label><textarea id="e-dif" class="lined" data-entry="dificuldade" rows="3">${esc(en.dificuldade)}</textarea></div>
          <div class="row"><label class="label" for="e-am">Amanhã eu vou <span class="hint">uma coisa só</span></label><input id="e-am" type="text" class="lined" data-entry="amanha" value="${esc(en.amanha)}"></div>
          <div class="row" style="display:flex;gap:1.5rem;flex-wrap:wrap;align-items:center">
            <div><span class="label">Energia</span><div class="energy">${[1, 2, 3, 4, 5].map((n) => `<button type="button" class="${en.energia === n ? "on" : ""}" data-energy="${n}">${n}</button>`).join("")}</div></div>
            <label class="check ${en.pulei ? "on" : ""}" data-check="pulei" style="margin-top:1rem"><span class="box"></span><span>Pulei hoje</span></label>
          </div>
        </div>
      </div>
      <div class="savebar"><span id="savestate">${en.done ? "Dia marcado" : "Salvando sozinho enquanto você preenche"}</span><button class="btn ${en.done ? "ghost" : ""} sm" data-act="done" data-day="${d}">${en.done ? "Desmarcar o dia" : "Marcar o dia como feito"}</button></div>`;
    shell(html, "dia", b.cor);
    app.dataset.day = d;
  }

  const saveEntryDebounced = debounce(async (d, patch) => { await S.setEntry(st.session.email, d, patch); flashSaved(); }, 500);
  function flashSaved() { const el = document.getElementById("savestate"); if (el && !entry(+app.dataset.day).done) { el.textContent = "Salvo"; setTimeout(() => { if (el.textContent === "Salvo") el.textContent = "Salvando sozinho enquanto você preenche"; }, 1500); } }
  function patchEntry(d, patch, immediate) {
    st.entries[d] = { ...(st.entries[d] || {}), ...patch };
    if (immediate) return S.setEntry(st.session.email, d, patch).then(flashSaved);
    saveEntryDebounced(d, patch);
  }

  // ------------------------------------------------------------------ travessia
  function provaProgress(b) { let n = 0; for (let d = b.inicio; d <= b.fim; d++) if (isDone(d)) n++; return n; }
  function gatePrep() { if (prepDone()) return false; toast("Primeiro a preparação, depois a travessia. Faltam " + prepPending() + " páginas.", true); location.hash = "#/prep"; viewPrep(); return true; }
  function viewTravessia() {
    if (gatePrep()) return;
    const t = todayIdx();
    const cards = C.blocos.map((b) => { const n = provaProgress(b); const state = t > b.fim ? "concluída" : t >= b.inicio ? "em andamento" : "em breve"; return `<a class="prova-card c-${b.cor}" href="#/prova/${b.num}"><span class="n">${pad(b.num)}</span><span class="eyebrow">Prova ${b.num} · dias ${b.inicio} a ${b.fim} · ${state}</span><h3>${esc(b.lugar)}</h3><div class="v">${esc(b.virtude)} · ${esc(b.sub)}</div><small>${esc(b.chamada)}. Com ${esc(b.mulher)}.</small><div class="progress"><i style="width:${n * 10}%"></i></div><small>${n} de 10 dias marcados</small></a>`; }).join("");
    const grid = Array.from({ length: TOTAL }, (_, i) => i + 1).map((d) => { const e = entry(d); const cls = [e.done ? "done" : "", e.pulei && !e.done ? "skip" : "", d === t ? "today" : "", d > t ? "locked" : ""].join(" "); return `<a href="#/dia/${d}" class="${cls} c-${bloco(d).cor}">${d}</a>`; }).join("");
    shell(`<div class="page-head"><div><span class="eyebrow">Visão geral</span><h1>A travessia</h1></div><p class="muted" style="max-width:48ch">${esc(C.mapa.intro)}</p></div>
      <div class="prova-list">${cards}</div>
      <div class="card" style="margin-top:1.4rem"><span class="eyebrow">Os 40 dias</span><div class="days-grid">${grid}</div><p class="muted" style="font-size:0.82rem;margin:0.8rem 0 0">Cheio: dia marcado. Claro: pulado. Contorno: hoje.</p></div>`, "travessia");
  }

  const HAB = [["Água", "corpo", 0], ["Movimento", "corpo", 1], ["Comida", "corpo", 2], ["Sono", "corpo", 3], ["Leitura", "mente", 0], ["Sem tela 1ª h", "mente", 1], ["Palavra", "espirito", 1], ["Oração", "espirito", 0], ["Desafio", "desafio", null]];
  function viewProva(n) {
    if (gatePrep()) return;
    const b = C.blocos.find((x) => x.num === n) || C.blocos[0];
    const t = todayIdx();
    const futura = t < b.inicio;
    const pk = "prova" + n;
    const p = st.prep[pk] || {};
    const days = Array.from({ length: 10 }, (_, i) => b.inicio + i);
    const trk = `<div class="scroll-x"><table class="tracker"><thead><tr><th class="h">Hábito / dia</th>${days.map((d) => `<th>${d}</th>`).join("")}</tr></thead><tbody>${HAB.map(([l, k, i]) => `<tr><th class="h">${esc(l)}</th>${days.map((d) => { const e = entry(d); const on = k === "desafio" ? !!e.desafio : !!(e.checklist && e.checklist[k] && e.checklist[k][i]); return `<td class="${d > t ? "na" : on ? "on" : ""}"></td>`; }).join("")}</tr>`).join("")}</tbody></table></div>`;
    const metas = Object.entries(b.metas).map(([k, v]) => `<div class="p-${k}"><span class="eyebrow">${k === "espirito" ? "Espírito" : k[0].toUpperCase() + k.slice(1)}</span>${esc(v)}</div>`).join("");
    const rv = C.revisao;
    const html = `
      <div class="prova-hero c-${b.cor}"><span class="n">${pad(n)}</span>
        <span class="eyebrow">Prova ${n} de 4 · dias ${b.inicio} a ${b.fim} · ${esc(b.chamada)}</span>
        <h1>${esc(b.lugar)}</h1><div class="v">${esc(b.virtude)} · ${esc(b.sub)}</div>
        ${verse(b.versiculo_lugar, b.ref_lugar)}
        <div class="woman"><b>${esc(b.mulher)}</b>${esc(b.mulher_desc)}<br><small style="opacity:0.75;letter-spacing:0.1em;text-transform:uppercase;font-size:0.68rem">${esc(b.mulher_ref)}</small></div>
      </div>
      <div class="two" style="margin-top:1.4rem">
        <div class="stack">
          <div class="card"><p>${esc(b.resumo)}</p><p>${esc(b.definicao)}</p>${verse(b.versiculo, b.ref)}
            <div class="tv"><div class="t"><span class="who">A tola</span>${esc(b.tola)}</div><div class="v"><span class="who">A virtuosa</span>${esc(b.virtuosa)}</div></div>
            <span class="eyebrow">Metas destes 10 dias</span><div class="metas">${metas}</div></div>
          ${futura ? `<div class="card soft"><span class="eyebrow">Ainda não</span><h3 style="font-size:1.2rem;margin:0.2rem 0 0.4rem">Esta prova abre no dia ${b.inicio}, ${esc(dayDate(b.inicio))}.</h3><p class="muted" style="margin:0">Igual ao caderno: leia a abertura, as metas e a mulher desta prova antes dos 10 dias. A meta pessoal, a oração e o quadro de hábitos você preenche quando ela começar.</p></div>` : `<div class="card"><span class="eyebrow">O que é meu nesta prova</span>
            <div class="field"><label class="label" for="pm">Minha meta pessoal <span class="hint">uma só, mensurável</span></label><input id="pm" type="text" data-prep="${pk}.meta" value="${esc(p.meta)}"></div>
            <div class="field"><label class="label" for="pp">Por quem vou orar nesta prova <span class="hint">uma pessoa ou uma família, os 10 dias</span></label><textarea id="pp" data-prep="${pk}.pessoa" rows="2">${esc(p.pessoa)}</textarea></div>
            <div class="field"><label class="label" for="pn">Notas da prova <span class="hint">o que eu percebi no caminho</span></label><textarea id="pn" data-prep="${pk}.notas" rows="3">${esc(p.notas)}</textarea></div></div>`}
        </div>
        <div class="stack">
          ${futura ? "" : `<div class="card"><span class="eyebrow">Quadro de hábitos · preenchido pelas caixinhas de cada dia</span>${trk}<p class="muted" style="font-size:0.82rem;margin:0.6rem 0 0">${provaProgress(b)} de 10 dias marcados. Dez dias de uma vez mostram o padrão que o dia a dia esconde.</p></div>
          <div class="card"><span class="eyebrow">${esc(rv.titulo)} ${n}${t <= b.fim ? " · abre no fim da prova, mas pode começar" : ""}</span>
            <div class="field"><span class="label">Cumpri a meta pessoal?</span>${chips(["Sim", "Em parte", "Não"], pk + ".meta_ok", p.meta_ok, "", true)}</div>
            <div class="field"><span class="label">Nota de 1 a 5</span><div class="two" style="gap:0.6rem">${rv.notas.map((nm) => `<div><small class="muted">${esc(nm)}</small><div class="energy" style="margin-top:0.2rem">${[1, 2, 3, 4, 5].map((v) => `<button type="button" class="${(p.notas_n || {})[nm] === v ? "on" : ""}" data-nota="${pk}:${esc(nm)}:${v}">${v}</button>`).join("")}</div></div>`).join("")}</div></div>
            ${rv.perguntas.map(([q], i) => `<div class="field"><label class="label" for="rq${i}">${esc(q)}</label><textarea id="rq${i}" class="lined" data-prep="${pk}.r${i}" rows="2">${esc(p["r" + i])}</textarea></div>`).join("")}
          </div>`}
        </div>
      </div>`;
    shell(html, "travessia", b.cor);
  }

  // ------------------------------------------------------------------ preparação
  const PREP_ORDER = ["compromisso", "tola", "identidade", "proposito", "regras", "carta", "retrato1"];
  function prepDone() { return prepStatus().every((x) => x[2]); }
  function prepPending() { return prepStatus().filter((x) => !x[2]).length; }
  function viewPrep() {
    const p = st.prep, t = todayIdx();
    const ps = Object.fromEntries(prepStatus().map(([k, l, ok]) => [k, ok]));
    const first = PREP_ORDER.find((k) => !ps[k]);
    const stepBtn = (k) => { const i = PREP_ORDER.indexOf(k); const nx = PREP_ORDER[i + 1];
      return `<div class="stepbar">${nx ? `<button type="button" class="btn sm" data-act="prep-next" data-next="${nx}">Salvar e ir pro próximo</button><span class="muted">${i + 1} de ${PREP_ORDER.length}</span>` : `<button type="button" class="btn gold sm" data-act="start" data-when="0">Terminei. Meu dia 1 é hoje</button><button type="button" class="btn ghost sm" data-act="start" data-when="1">Começo amanhã</button><span class="muted">${i + 1} de ${PREP_ORDER.length}</span>`}</div>`; };
    const g = (k, f) => esc((p[k] || {})[f]);
    const acc = (k, title, sub, body, open) => `<details class="acc" id="acc-${k}" ${(first ? k === first : false) ? "open" : ""}><summary class="${ps[k] ? "ok" : ""}"><span class="st"></span><b>${esc(title)}</b><small>${esc(sub)}</small></summary><div class="body">${body}</div></details>`;
    const cae = C.corpo_alma_espirito, idn = C.identidade, pl = C.proposito_limites, rs = C.regras_sonhos, rt = C.retrato, tv = C.tola_virtuosa, cf = C.carta_futuro;
    const retratoRows = (k) => rt.areas.map((a) => `<div class="retrato-row"><span>${esc(a)}</span><div class="scale">${Array.from({ length: 11 }, (_, i) => i).map((v) => `<button type="button" class="${((p[k] || {}).notas || {})[a] === v ? "on" : ""}" data-nota="${k}:${esc(a)}:${v}">${v}</button>`).join("")}</div></div>`).join("");
    const html = `
      <div class="page-head"><div><span class="eyebrow">Antes do dia 1 · ${PREP_ORDER.length - prepPending()} de ${PREP_ORDER.length} prontas</span><h1>Preparação</h1></div><p class="muted" style="max-width:48ch">As páginas que a maioria pula e que decidem tudo. Reserve uma tarde. Tudo salva sozinho.</p></div>
      <div class="steps-strip">${PREP_ORDER.map((k, i) => { const it = prepStatus().find((x) => x[0] === k); return `<a href="#acc-${k}" class="step ${it[2] ? "ok" : ""} ${k === first ? "cur" : ""}" data-act="prep-goto" data-next="${k}"><i>${it[2] ? "✓" : i + 1}</i><span>${esc(it[1])}</span></a>`; }).join("")}</div>
      ${prepDone() ? `<div class="card gift-cta"><div><span class="eyebrow">Tudo pronto</span><b>A preparação está completa</b><span class="muted">${st.profile.start_date ? "Agora é uma página por dia." : "Falta só dizer quando começa."}</span></div>${st.profile.start_date ? `<a class="btn gold sm" href="#/inicio">Ir pro início</a>` : `<span class="btns"><button type="button" class="btn gold sm" data-act="start" data-when="0">Meu dia 1 é hoje</button><button type="button" class="btn ghost sm" data-act="start" data-when="1">Começo amanhã</button></span>`}</div>` : ""}
      ${acc("compromisso", "Meu compromisso", "assinatura e porquê", `
        <p>Eu, <b>${esc(st.profile.name || "")}</b>, decido atravessar estes 40 dias com honestidade, sem perfeição e sem desistir. Quando falhar, viro a página. Quando acertar, agradeço a Deus.</p>
        <div class="field"><label class="label" for="c-ass">Assinatura <span class="hint">digite seu nome completo</span></label><input id="c-ass" type="text" data-prep="compromisso.assinatura" value="${g("compromisso", "assinatura")}" style="font-family:var(--serif);font-size:1.4rem;font-style:italic"></div>
        <div class="field"><label class="label" for="c-luta">O que eu mais luto contra hoje</label><textarea id="c-luta" class="lined" data-prep="compromisso.luta" rows="2">${g("compromisso", "luta")}</textarea></div>
        <div class="field"><label class="label" for="c-why">Por que eu quero ser uma mulher melhor</label><textarea id="c-why" class="lined" data-prep="compromisso.porque" rows="3">${g("compromisso", "porque")}</textarea></div>
        <span class="label">Antes de virar a página, lembre</span>
        <div class="postits">
          <div class="pi a">“Ela é mais preciosa do que rubis, e tudo o que mais possas desejar não se pode comparar a ela.”<small>Provérbios 3:15</small></div>
          <div class="pi b">“A força e a dignidade são os seus vestidos, e ri-se do dia futuro.”<small>Provérbios 31:25</small></div>
          <div class="pi c">“Enganosa é a graça e vã a formosura, mas a mulher que teme ao Senhor, essa sim será louvada.”<small>Provérbios 31:30</small></div>
          <div class="pi d">“Se alguém quer vir após mim, negue-se a si mesmo, e tome cada dia a sua cruz, e siga-me.”<small>Lucas 9:23</small></div>
        </div>
        <div class="field"><span class="label">Onde eu estou hoje</span>${chips(["Solteira", "Namorando", "Noiva", "Casada", "Mãe"], "compromisso.fase", (p.compromisso || {}).fase)}</div>${stepBtn("compromisso")}`, !ps.compromisso)}
      ${acc("tola", tv.titulo, "diagnóstico", `
        ${verse(tv.versiculo, tv.ref)}<p style="margin-top:0.8rem">${esc(tv.intro)}</p>
        <table class="contrast">${tv.contrastes.map(([a, b], i) => `<tr><td><button type="button" class="chip ${(p.tola || {}).linha == i ? "on" : ""}" data-chip="tola.linha" data-val="${i}" data-single="1" style="width:30px;height:30px;padding:0;justify-content:center">${i + 1}</button></td><td class="t"><i>A tola</i> ${esc(a)}</td><td class="v"><i style="color:var(--rubi)">A virtuosa</i> ${esc(b)}</td></tr>`).join("")}</table>
        <div class="field" style="margin-top:0.8rem"><label class="label" for="tl">${esc(tv.pergunta)} <span class="hint">marque o número acima e escreva por quê</span></label><textarea id="tl" class="lined" data-prep="tola.porque" rows="2">${g("tola", "porque")}</textarea></div>${stepBtn("tola")}`)}
      ${acc("identidade", idn.titulo, "quem Deus diz", `
        <p>${esc(idn.intro)}</p>
        <div class="two" style="gap:0.6rem;margin-bottom:1rem">${idn.versiculos.map(([t2, v, r]) => `<div style="border-left:3px solid var(--rubi);padding-left:0.7rem"><span class="label" style="color:var(--rubi);margin:0">${esc(t2)}</span><i class="serif" style="font-size:1.05rem">“${esc(v)}”</i><br><small class="muted" style="letter-spacing:0.1em;text-transform:uppercase;font-size:0.65rem">${esc(r)}</small></div>`).join("")}</div>
        <div class="field"><label class="label" for="id1">${esc(idn.pergunta1)}</label><textarea id="id1" class="lined" data-prep="identidade.hoje" rows="3">${g("identidade", "hoje")}</textarea></div>
        <div class="field"><label class="label" for="id2">${esc(idn.pergunta2)}</label><textarea id="id2" class="lined" data-prep="identidade.deus" rows="3">${g("identidade", "deus")}</textarea></div>${stepBtn("identidade")}`)}
      ${acc("proposito", pl.titulo, "direção e limites", `
        <div class="two"><div><h4 class="serif" style="font-size:1.3rem">Propósito</h4><p class="muted" style="font-size:0.92rem">${esc(pl.prop_intro)}</p>
          ${pl.prop_perguntas.map((q, i) => `<div class="field"><label class="label" for="pq${i}">${esc(q)}</label><textarea id="pq${i}" class="lined" data-prep="proposito.q${i}" rows="2">${g("proposito", "q" + i)}</textarea></div>`).join("")}
          <div class="field" style="background:var(--dourado-claro);padding:0.8rem;border-radius:10px"><label class="label" for="pf">${esc(pl.prop_frase)}</label><textarea id="pf" data-prep="proposito.frase" rows="2" style="background:transparent">${g("proposito", "frase")}</textarea></div></div>
        <div><h4 class="serif" style="font-size:1.3rem">Limites</h4><p class="muted" style="font-size:0.92rem">${esc(pl.lim_intro)} <i>“${esc(pl.lim_versiculo)}”</i> ${esc(pl.lim_ref)}</p>
          ${pl.lim_areas.map((a, i) => `<span class="label">${esc(a)}</span><div class="two" style="gap:0.6rem;margin-bottom:0.8rem">${pl.lim_cols.map((c, j) => `<div><small class="muted">${esc(c)}</small><textarea class="lined" data-prep="proposito.l${i}${j}" rows="2">${g("proposito", "l" + i + j)}</textarea></div>`).join("")}</div>`).join("")}</div></div>${stepBtn("proposito")}`)}
      ${acc("regras", rs.titulo, "inegociáveis e visão", `
        <div class="two"><div><p class="muted" style="font-size:0.92rem">${esc(rs.regras_intro)}</p>${rs.regras.map((r) => `<label class="check ${((p.regras || {}).marcadas || []).includes(r) ? "on" : ""}" data-multi="regras.marcadas" data-val="${esc(r)}"><span class="box"></span><span>${esc(r)}</span></label>`).join("")}
          <div class="field" style="margin-top:0.8rem"><label class="label" for="rm">Minhas regras <span class="hint">as que eu não negocio por 40 dias</span></label><textarea id="rm" class="lined" data-prep="regras.minhas" rows="3">${g("regras", "minhas")}</textarea></div></div>
        <div><p class="muted" style="font-size:0.92rem">${esc(rs.sonhos_intro)} <i>“${esc(rs.sonhos_versiculo)}”</i> ${esc(rs.sonhos_ref)}</p>
          <div class="dreams">${rs.areas.map(([a, cor], i) => `<div class="c-${cor}"><h4>${esc(a)}</h4><label class="label" for="dm${i}">Meta que dá pra medir</label><input id="dm${i}" type="text" data-prep="regras.meta${i}" value="${g("regras", "meta" + i)}"><label class="label" for="dc${i}" style="margin-top:0.5rem">Como vou saber que cheguei</label><input id="dc${i}" type="text" data-prep="regras.como${i}" value="${g("regras", "como" + i)}"></div>`).join("")}</div></div></div>${stepBtn("regras")}`)}
      ${acc("carta", cf.titulo, "só abre no dia 40", (p.carta || {}).texto && t < TOTAL && (p.carta || {}).lacrada
        ? `<div class="sealed"><div class="big">Lacrada.</div><p class="muted">Escrita em ${esc((p.carta || {}).data || "")}. Abre no dia 40, ${esc(dayDate(TOTAL))}.</p><button class="btn ghost sm" data-act="unseal">Preciso editar</button></div>${stepBtn("carta")}`
        : `<p class="muted">${esc(cf.intro)}</p><p class="serif" style="font-size:1.2rem;font-style:italic">${esc(cf.cabecalho)}</p>
           <div class="field"><textarea class="lined" data-prep="carta.texto" rows="8" placeholder="Hoje eu estou…">${g("carta", "texto")}</textarea></div>
           ${t >= TOTAL ? "" : `<button class="btn sm" data-act="seal">Lacrar até o dia 40</button>`}${stepBtn("carta")}`)}
      ${acc("retrato1", rt.titulo_1, "foto honesta", `
        <p class="muted" style="font-size:0.92rem">${esc(rt.intro_1)}</p><span class="label">De 0 a 10, como está cada área hoje</span>${retratoRows("retrato1")}
        <div class="two" style="margin-top:1rem"><div class="field"><label class="label" for="r1a">${esc(rt.palavras_1)}</label><input id="r1a" type="text" data-prep="retrato1.palavras" value="${g("retrato1", "palavras")}"></div><div class="field"><label class="label" for="r1b">${esc(rt.incomodo_1)}</label><input id="r1b" type="text" data-prep="retrato1.incomodo" value="${g("retrato1", "incomodo")}"></div></div>
        <div class="field"><label class="label" for="r1c">Oração de partida <span class="hint">o que eu quero pedir a Deus antes do dia 1</span></label><textarea id="r1c" class="lined" data-prep="retrato1.oracao" rows="3">${g("retrato1", "oracao")}</textarea></div>${stepBtn("retrato1")}`)}
      ${t >= TOTAL ? acc("retrato40", rt.titulo_40, "dia 40", `
        <p class="muted" style="font-size:0.92rem">${esc(rt.intro_40)}</p>${retratoRows("retrato40")}
        <div class="two" style="margin-top:1rem"><div class="field"><label class="label" for="r4a">${esc(rt.mudou_40)}</label><textarea id="r4a" class="lined" data-prep="retrato40.mudou" rows="3">${g("retrato40", "mudou")}</textarea></div><div class="field"><label class="label" for="r4b">${esc(rt.deus_40)}</label><textarea id="r4b" class="lined" data-prep="retrato40.deus" rows="3">${g("retrato40", "deus")}</textarea></div></div>
        <div class="card soft" style="margin-top:1rem"><span class="eyebrow">Sua carta do dia 1</span><p class="serif" style="font-size:1.15rem;white-space:pre-wrap">${g("carta", "texto") || "Você não escreveu a carta."}</p></div>
        ${verse(C.fechamento.versiculo, C.fechamento.ref)}${C.fechamento.paragrafos.map((x) => `<p style="margin-top:0.8rem">${esc(x)}</p>`).join("")}
        ${C.fechamento.proximos.map((q, i) => `<div class="field"><label class="label" for="fx${i}">${esc(q)}</label><textarea id="fx${i}" class="lined" data-prep="retrato40.p${i}" rows="2">${g("retrato40", "p" + i)}</textarea></div>`).join("")}`, true) : ""}
      <div class="card" style="margin-top:1rem">${verse(cae.versiculo, cae.ref)}<p style="margin-top:0.8rem">${esc(cae.intro)}</p><div class="metas">${cae.pilares.map(([n, cor, fr, it]) => `<div style="--pc:var(--${cor})"><span class="eyebrow">${esc(n)}</span><b class="serif" style="font-size:1.05rem">${esc(fr)}</b><br><small class="muted">${esc(it)}</small></div>`).join("")}</div></div>`;
    shell(html, "prep");
  }

  // ------------------------------------------------------------------ aulas / imprimir / conta
  const video = (url, title, desc) => `<div class="card"><div class="video">${url ? `<iframe src="${esc(url)}" title="${esc(title)}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>` : `<div>${ICO.play}<b style="display:block;color:var(--creme);font-family:var(--serif);font-size:1.3rem">${esc(title)}</b><small>Vídeo em breve. Cole a URL em config.js.</small></div>`}</div><h3 style="margin-top:1rem">${esc(title)}</h3><p class="muted" style="margin:0.3rem 0 0">${esc(desc)}</p></div>`;
  function viewAulas() {
    const V = CFG.VIDEOS || {};
    shell(`<div class="page-head"><div><span class="eyebrow">Com a Rebeca</span><h1>Aulas</h1></div></div>
      <div class="stack">
        ${video(V.aula_inaugural, "Aula inaugural: o propósito da travessia", "Por que 40 dias, por que quatro provas, o que esperar de cada uma e como a Rebeca usa o caderno no dia a dia.")}
        <div class="two">${video(V.como_imprimir, "Como imprimir e encadernar", "Papel, gramatura, espiral e o que pedir na gráfica.")}${video(V.como_usar_site, "Como usar a versão pelo celular", "O passo a passo desta área de membros pelo celular.")}</div>
      </div>`, "aulas");
  }
  function viewImprimir() {
    shell(`<div class="page-head"><div><span class="eyebrow">Versão impressa</span><h1>Imprimir o caderno</h1></div></div>
      <div class="two">
        <div class="stack">
          <div class="card"><img src="../assets/img/capa.png" alt="" style="border-radius:8px;box-shadow:var(--shadow-sm)"><a class="btn block" style="margin-top:1rem" href="${esc(CFG.PDF_URL || "#")}" download>Baixar o PDF (A4, 72 páginas)</a><p class="muted" style="font-size:0.85rem;margin:0.8rem 0 0">Só frente. Quer menor? Imprima em A5, é a mesma proporção.</p></div>
        </div>
        <div class="card"><span class="eyebrow">Como pedir na gráfica</span><ul class="tips">
          <li>Tamanho A4 deitado (29,7 x 21 cm), impressão colorida, só frente.</li>
          <li>Miolo em sulfite 120g ou 150g, que segura canetinha sem enrugar.</li>
          <li>Capa e contracapa em papel 250g ou 300g, laminação fosca.</li>
          <li>Encadernação em espiral wire-o (preto ou dourado) na borda de cima.</li>
          <li>Em casa: imprima em A4 deitado, uma página por folha, e leve pra encadernar.</li>
          <li>Deixe na mesa de cabeceira, não numa gaveta.</li>
        </ul></div>
      </div>`, "imprimir");
  }
  function giftLink(code) { const base = location.href.split("#")[0]; return base + "#/resgatar/" + code; }
  // Checkout do presente com o e-mail da compradora já preenchido (o webhook liga o convite a esse e-mail).
  function giftBuyUrl() {
    if (!CFG.GIFT_CHECKOUT_URL) return "";
    const u = CFG.GIFT_CHECKOUT_URL + (CFG.GIFT_CHECKOUT_URL.includes("?") ? "&" : "?") + "email=" + encodeURIComponent(st.session.email);
    return u;
  }
  function giftBuyCard(temAlgum) {
    const url = giftBuyUrl();
    return `<div class="card gift buy"><span class="eyebrow">${temAlgum ? "Mais uma amiga" : "Presente pra uma amiga"}</span><h3>Ninguém atravessa sozinha</h3>
      <p>Imagina sua amiga fazendo esses 40 dias junto com você: as duas na mesma prova, trocando mensagem sobre o desafio do dia, orando uma pela outra. Você pode ser o canal dessa bênção na vida dela.</p>
      <p class="muted">Cada presente é um acesso completo, com caderno, app e aulas, por <b>${esc(CFG.GIFT_PRICE || "R$ 27")}</b>. Pode presentear quantas quiser: cada compra vira um convite novo aqui nesta página.</p>
      ${url ? `<div class="btns"><a class="btn gold" href="${esc(url)}" target="_blank" rel="noopener">Presentear ${temAlgum ? "mais " : ""}uma amiga · ${esc(CFG.GIFT_PRICE || "R$ 27")}</a><button class="btn ghost" type="button" data-act="reload">Já paguei, atualizar</button></div>
      <p class="muted" style="font-size:0.82rem;margin:0.8rem 0 0">Use o mesmo e-mail desta conta na hora de pagar. O convite aparece aqui em até alguns minutos depois da confirmação.</p>` : `<p class="muted" style="font-size:0.82rem">O link de compra do presente ainda não foi configurado. Fale com o suporte${CFG.SUPORTE_EMAIL ? ": " + esc(CFG.SUPORTE_EMAIL) : ""}.</p>`}
    </div>`;
  }
  function giftMsg(g) {
    const nome = g.to_name ? g.to_name + ", " : "";
    const de = st.profile.name || st.session.name || "uma amiga";
    const msg = g.message ? g.message + "\n\n" : "";
    return `${nome}te dei um presente: 40 dias do caderno De Tola a Virtuosa pra gente fazer juntas.\n\n${msg}Seu código é ${g.code}. É só entrar em ${giftLink(g.code)} e criar sua conta.\n\nCom carinho, ${de}.`;
  }
  async function viewPresente() {
    const gifts = await S.getGifts(st.session.email);
    const recebido = await S.giftReceived(st.session.email);
    const cards = gifts.map((g) => {
      const claimed = !!g.claimed_email;
      return `<div class="card gift ${claimed ? "done" : ""}">
        <div class="gift-head"><span class="eyebrow">${claimed ? "Presente resgatado" : "Presente pra uma amiga"}</span><span class="code">${esc(g.code)}</span></div>
        ${claimed ? `<p>Resgatado por <b>${esc(g.claimed_email)}</b>${g.claimed_at ? " em " + new Date(g.claimed_at).toLocaleDateString("pt-BR") : ""}. Vocês estão na mesma travessia.</p>` : `
        <div class="field"><label class="label" for="g-to-${esc(g.code)}">Nome dela</label><input id="g-to-${esc(g.code)}" type="text" data-gift="${esc(g.code)}.to_name" value="${esc(g.to_name || "")}" placeholder="Como você chama sua amiga"></div>
        <div class="field"><label class="label" for="g-msg-${esc(g.code)}">Um recado seu <span class="hint">vai junto com o código</span></label><textarea id="g-msg-${esc(g.code)}" class="lined" rows="3" data-gift="${esc(g.code)}.message" placeholder="Por que você pensou nela pra fazer isso junto">${esc(g.message || "")}</textarea></div>
        <div class="btns">
          <a class="btn" href="https://wa.me/?text=${encodeURIComponent(giftMsg(g))}" target="_blank" rel="noopener">Mandar pelo WhatsApp</a>
          <button class="btn ghost" type="button" data-act="copy" data-text="${esc(giftLink(g.code))}">Copiar link do presente</button>
          <button class="btn ghost" type="button" data-act="cartao" data-code="${esc(g.code)}">Cartão pra imprimir</button>
        </div>
        <p class="muted" style="font-size:0.82rem;margin:0.8rem 0 0">Ela abre o link, cria a conta com o e-mail dela e o acesso libera na hora. O código vale uma vez.</p>`}
      </div>`;
    }).join("");
    shell(`<div class="page-head"><div><span class="eyebrow">Fazer junto</span><h1>Presente</h1></div></div>
      <div class="stack">
        ${recebido ? `<div class="card gift received"><span class="eyebrow">Você ganhou</span><p>Sua travessia foi um presente de <b>${esc(recebido.buyer_name || recebido.buyer_email)}</b>.${recebido.message ? ` Ela deixou um recado: <em>“${esc(recebido.message)}”</em>` : ""} Quando terminar os 40 dias, conta pra ela o que mudou.</p></div>` : ""}
        ${cards}
        ${giftBuyCard(gifts.length > 0)}
      </div>`, "conta");
  }
  function cartaoPresente(g) {
    const de = st.profile.name || st.session.name || "";
    const w = window.open("", "_blank");
    if (!w) return toast("Libere as janelas pop-up pra abrir o cartão.", true);
    w.document.write(`<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Cartão de presente</title>
      <link rel="stylesheet" href="${location.href.split("#")[0].replace(/app\/?$/, "")}assets/brand.css">
      <style>@page{size:148mm 105mm;margin:0}body{margin:0;background:#fff}.c{width:148mm;height:105mm;box-sizing:border-box;padding:12mm 14mm;background:var(--rubi-profundo);color:var(--creme);display:flex;flex-direction:column;justify-content:space-between;position:relative}.c .frame{position:absolute;inset:5mm;border:0.3mm solid rgba(232,194,122,.5)}.c .eyebrow{color:var(--dourado-vivo)}.c h1{font-family:var(--display);font-size:22pt;line-height:1.05;margin:2mm 0 3mm}.c p{font-family:var(--serif);font-style:italic;font-size:10.5pt;line-height:1.4;margin:0;color:rgba(249,245,238,.9)}.c .code{font-family:var(--serif);font-size:16pt;letter-spacing:.2em;color:var(--dourado-vivo);margin-top:2mm}.c .foot{font-size:7pt;letter-spacing:.14em;text-transform:uppercase;color:rgba(249,245,238,.6)}.c .de{font-family:var(--display);font-size:13pt;color:var(--creme)}@media screen{body{padding:20px;background:#eee}.c{box-shadow:0 10px 30px rgba(0,0,0,.2)}}</style></head>
      <body><div class="c"><div class="frame"></div>
        <div><span class="eyebrow">Um presente pra você${g.to_name ? ", " + esc(g.to_name) : ""}</span><h1>40 dias no deserto,<br>nós duas.</h1><p>${g.message ? esc(g.message) : "Pensei em você pra fazer esse caminho comigo. Um caderno, quarenta dias, uma virtude de cada vez."}</p></div>
        <div><div class="foot">Seu código de acesso</div><div class="code">${esc(g.code)}</div><div class="foot" style="margin-top:1.5mm">${esc(location.href.split("#")[0])}</div></div>
        <div style="display:flex;justify-content:space-between;align-items:flex-end"><span class="de">${esc(de)}</span><span class="foot">De Tola a Virtuosa · Rebeca Fortunato</span></div>
      </div><script>setTimeout(function(){window.print()},400)<\/script></body></html>`);
    w.document.close();
  }
  function viewConta() {
    shell(`<div class="page-head"><div><span class="eyebrow">Sua conta</span><h1>Conta</h1></div></div>
      <div class="card gift-cta"><div><span class="eyebrow">Fazer junto</span><b>Presente pra uma amiga</b><span class="muted">Mande o código, imprima o cartão ou veja quem já resgatou.</span></div><a class="btn ghost sm" href="#/presente">Abrir</a></div>
      <div class="two">
        <div class="card">
          <div class="field"><label class="label" for="a-name">Nome</label><input id="a-name" type="text" data-profile="name" value="${esc(st.profile.name || "")}"></div>
          <div class="field"><label class="label">E-mail</label><input type="text" value="${esc(st.session.email)}" disabled></div>
          <div class="field"><label class="label" for="a-date">Data do meu dia 1 <span class="hint">só mude se errou</span></label><input id="a-date" type="date" data-profile="start_date" value="${esc(st.profile.start_date || "")}"><p class="muted" style="font-size:0.82rem;margin:0.4rem 0 0">Mudar a data desloca todos os dias. Os registros ficam pelo número do dia.</p></div>
          <p class="muted" style="font-size:0.85rem">Acesso: <b>${st.member.plan === "demo" ? "modo demonstração" : "ativo"}</b> · ${S.mode === "local" ? "salvo neste navegador" : "salvo na nuvem"}</p>
          <button class="btn ghost sm" data-act="logout">Sair</button>
        </div>
        <div class="card"><span class="eyebrow">Zona de cuidado</span><p class="muted" style="font-size:0.92rem">Apagar o progresso remove os 40 dias e a preparação. Não tem volta.</p><button class="btn ghost sm danger" data-act="wipe">Apagar meu progresso</button></div>
      </div>`, "conta");
  }

  // ------------------------------------------------------------------ eventos
  const savePrepDebounced = debounce(async (k, f, v) => { await S.setPrep(st.session.email, k, { [f]: v }); }, 500);
  function setPrep(k, f, v, now) { st.prep[k] = { ...(st.prep[k] || {}), [f]: v }; if (now) return S.setPrep(st.session.email, k, { [f]: v }); savePrepDebounced(k, f, v); }

  const saveGiftDebounced = debounce(async (code, f, v) => { await S.updateGift(code, { [f]: v }); }, 500);
  app.addEventListener("input", (ev) => {
    const el = ev.target;
    if (el.dataset.gift) { const [code, f] = el.dataset.gift.split("."); return saveGiftDebounced(code, f, el.value); }
    if (el.dataset.entry) return patchEntry(+app.dataset.day, { [el.dataset.entry]: el.value });
    if (el.dataset.prep) { const [k, f] = el.dataset.prep.split("."); return setPrep(k, f, el.value); }
  });
  app.addEventListener("change", async (ev) => {
    const el = ev.target;
    if (el.dataset.profile) { st.profile[el.dataset.profile] = el.value; await S.setProfile(st.session.email, { [el.dataset.profile]: el.value }); toast("Salvo"); if (el.dataset.profile === "start_date") route(); }
  });
  app.addEventListener("click", async (ev) => {
    const chip = ev.target.closest("[data-chip]");
    if (chip) {
      const group = chip.dataset.chip, val = chip.dataset.val, single = chip.dataset.single === "1";
      const day = +app.dataset.day;
      if (group.includes(".")) {
        const [k, f] = group.split(".");
        const cur = (st.prep[k] || {})[f];
        let next;
        if (single) next = String(cur) === val ? null : (isNaN(+val) ? val : +val);
        else { const arr = Array.isArray(cur) ? [...cur] : []; const i = arr.indexOf(val); i >= 0 ? arr.splice(i, 1) : arr.push(val); next = arr; }
        await setPrep(k, f, next, true);
        if (single) chip.parentElement.querySelectorAll(".chip").forEach((c) => c.classList.toggle("on", c === chip && next != null)); else chip.classList.toggle("on");
        return;
      }
      if (group === "fase") { chip.classList.toggle("on"); return; }
      const cur = entry(day)[group];
      let next;
      if (single) next = cur === val ? null : val;
      else { const arr = Array.isArray(cur) ? [...cur] : []; const i = arr.indexOf(val); i >= 0 ? arr.splice(i, 1) : arr.push(val); next = arr; }
      patchEntry(day, { [group]: next }, true);
      if (single) chip.parentElement.querySelectorAll(".chip").forEach((c) => c.classList.toggle("on", c === chip && next != null)); else chip.classList.toggle("on");
      return;
    }
    const chk = ev.target.closest("[data-check]");
    if (chk) {
      ev.preventDefault();
      const day = +app.dataset.day, key = chk.dataset.check;
      const on = !chk.classList.contains("on"); chk.classList.toggle("on", on);
      if (key.includes(":")) { const [k, i] = key.split(":"); const cl = JSON.parse(JSON.stringify(entry(day).checklist || {})); cl[k] = cl[k] || []; cl[k][+i] = on; patchEntry(day, { checklist: cl }, true); }
      else patchEntry(day, { [key]: on }, true);
      return;
    }
    const multi = ev.target.closest("[data-multi]");
    if (multi) { ev.preventDefault(); const [k, f] = multi.dataset.multi.split("."); const arr = [...(((st.prep[k] || {})[f]) || [])]; const v = multi.dataset.val; const i = arr.indexOf(v); i >= 0 ? arr.splice(i, 1) : arr.push(v); multi.classList.toggle("on", i < 0); await setPrep(k, f, arr, true); return; }
    const en = ev.target.closest("[data-energy]");
    if (en) { const day = +app.dataset.day; const v = +en.dataset.energy; const cur = entry(day).energia; const next = cur === v ? null : v; patchEntry(day, { energia: next }, true); en.parentElement.querySelectorAll("button").forEach((b) => b.classList.toggle("on", +b.dataset.energy === next)); return; }
    const nota = ev.target.closest("[data-nota]");
    if (nota) { const [k, nm, v] = nota.dataset.nota.split(":"); const field = k.startsWith("prova") ? "notas_n" : "notas"; const cur = { ...(((st.prep[k] || {})[field]) || {}) }; cur[nm] = cur[nm] === +v ? undefined : +v; if (cur[nm] === undefined) delete cur[nm]; await setPrep(k, field, cur, true); nota.parentElement.querySelectorAll("button").forEach((b) => b.classList.toggle("on", b.dataset.nota === nota.dataset.nota && cur[nm] != null)); return; }
    const act = ev.target.closest("[data-act]");
    if (!act) return;
    const a = act.dataset.act;
    if (a === "tab") return renderAuth(act.dataset.tab);
    if (a === "logout") { await S.signOut(); location.hash = ""; return boot(); }
    if (a === "start") { if (!prepDone()) return toast("Termine a preparação primeiro.", true); const d = isoShift(+act.dataset.when || 0); st.profile.start_date = d; await S.setProfile(st.session.email, { start_date: d }); toast(+act.dataset.when ? "Combinado. Amanhã é o dia 1." : "Hoje é o dia 1. Vamos."); location.hash = "#/inicio"; return route(); }
    if (a === "prep-next" || a === "prep-goto") { ev.preventDefault(); const k = act.dataset.next; app.querySelectorAll("details.acc").forEach((d) => { d.open = d.id === "acc-" + k; }); const el = document.getElementById("acc-" + k); if (el) el.scrollIntoView({ behavior: "smooth", block: "start" }); if (a === "prep-next") toast("Salvo. Próxima página."); return; }
    if (a === "reload") { toast("Atualizando..."); route(); return; }
    if (a === "copy") { try { await navigator.clipboard.writeText(act.dataset.text); toast("Link copiado."); } catch { prompt("Copie o link:", act.dataset.text); } return; }
    if (a === "cartao") { const gs = await S.getGifts(st.session.email); const g = gs.find((x) => x.code === act.dataset.code); if (g) cartaoPresente(g); return; }
    if (a === "reset") { const email = document.getElementById("f-email").value; if (!email) return toast("Digite o e-mail primeiro.", true); try { await S.resetPassword(email); toast("Enviamos um link pro seu e-mail."); } catch (e) { toast(e.message, true); } return; }
    if (a === "done") { const d = +act.dataset.day; const next = !entry(d).done; await patchEntry(d, { done: next, date: isoToday() }, true); toast(next ? `Dia ${d} marcado. Fidelidade.` : "Dia desmarcado."); return viewDia(d); }
    if (a === "seal") { await setPrep("carta", "lacrada", true, true); await setPrep("carta", "data", new Date().toLocaleDateString("pt-BR"), true); toast("Carta lacrada até o dia 40."); return viewPrep(); }
    if (a === "unseal") { await setPrep("carta", "lacrada", false, true); return viewPrep(); }
    if (a === "wipe") { if (!confirm("Apagar todo o progresso? Não tem volta.")) return; await S.wipe(st.session.email); st.entries = {}; st.prep = {}; toast("Progresso apagado."); return route(); }
  });
  app.addEventListener("submit", async (ev) => {
    const f = ev.target;
    ev.preventDefault();
    if (f.id === "authform") {
      const fd = new FormData(f); const tab = f.dataset.tab;
      const btn = f.querySelector("button[type=submit]"); btn.disabled = true;
      try { st.session = tab === "criar" ? await S.signUp(fd.get("email").trim().toLowerCase(), fd.get("password"), fd.get("name").trim()) : await S.signIn(fd.get("email").trim().toLowerCase(), fd.get("password")); await boot(); }
      catch (e) { renderAuth(tab, e.message); }
      return;
    }
    if (f.id === "claimform") {
      const code = new FormData(f).get("code");
      const r = await S.claimGift(st.session.email, code);
      if (!r.ok) return toast(r.error, true);
      toast(`Presente de ${r.from} resgatado. Bem-vinda.`);
      return boot();
    }
    if (f.id === "onboard") {
      const fd = new FormData(f);
      const fases = [...f.querySelectorAll(".chip.on")].map((c) => c.dataset.val);
      await S.setProfile(st.session.email, { name: fd.get("name").trim() });
      await S.setPrep(st.session.email, "compromisso", { fase: fases });
      st.profile = await S.getProfile(st.session.email); st.prep = await S.getPrep(st.session.email);
      location.hash = "#/prep"; route();
    }
  });

  boot();
})();
