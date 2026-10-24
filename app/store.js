/* Camada de dados da área de membros.
 * Dois modos, mesma interface:
 *  - local: tudo em localStorage (demonstração, sem servidor)
 *  - supabase: login por e-mail e senha, progresso salvo na nuvem, acesso liberado pela tabela `members`
 */
(function () {
  const cfg = window.DTV_CONFIG || {};
  const useSupabase = !!(cfg.SUPABASE_URL && cfg.SUPABASE_ANON_KEY && window.supabase);
  // Servidor configurado mas a biblioteca não carregou (bloqueador, sem internet): não cai no modo demonstração em silêncio.
  if (cfg.SUPABASE_URL && cfg.SUPABASE_ANON_KEY && !window.supabase) {
    document.addEventListener("DOMContentLoaded", () => { const a = document.getElementById("app"); if (a) a.innerHTML = '<div class="inactive"><div class="card"><h2>Não conseguimos carregar o app</h2><p>Confere a internet, desliga bloqueador de anúncios nesta página e recarrega.</p><button class="btn gold" onclick="location.reload()">Recarregar</button></div></div>'; });
  }

  // ---------- LOCAL ----------
  const LS = {
    key: (k) => "dtv:" + k,
    get(k, d) { try { const v = localStorage.getItem(this.key(k)); return v == null ? d : JSON.parse(v); } catch { return d; } },
    set(k, v) { try { localStorage.setItem(this.key(k), JSON.stringify(v)); } catch {} },
    del(k) { try { localStorage.removeItem(this.key(k)); } catch {} },
  };

  const local = {
    mode: "local",
    async session() { return LS.get("session", null); },
    async signUp(email, password, name) {
      const users = LS.get("users", {});
      if (users[email]) throw new Error("Esse e-mail já tem cadastro. Entre com a senha.");
      users[email] = { email, password, name, created: Date.now() };
      LS.set("users", users);
      const s = { email, name }; LS.set("session", s); return s;
    },
    async signIn(email, password) {
      const users = LS.get("users", {});
      const u = users[email];
      if (!u || u.password !== password) throw new Error("E-mail ou senha não conferem.");
      const s = { email, name: u.name }; LS.set("session", s); return s;
    },
    async signOut() { LS.del("session"); },
    async resetPassword() { throw new Error("No modo demonstração não há recuperação de senha."); },
    async updatePassword() { return true; },
    async membership(email) { return { active: true, plan: "demo", email }; },
    async getProfile(email) { return LS.get("profile:" + email, { start_date: null, name: null }); },
    async setProfile(email, data) { const p = await this.getProfile(email); LS.set("profile:" + email, { ...p, ...data }); },
    async getEntries(email) { return LS.get("entries:" + email, {}); },
    async setEntry(email, day, data, full) { const all = await this.getEntries(email); all[day] = { ...(all[day] || {}), ...(full || data), updated: Date.now() }; LS.set("entries:" + email, all); },
    async getPrep(email) { return LS.get("prep:" + email, {}); },
    async setPrep(email, key, data, full) { const all = await this.getPrep(email); all[key] = { ...(all[key] || {}), ...(full || data) }; LS.set("prep:" + email, all); },
    async wipe(email) { LS.del("entries:" + email); LS.del("prep:" + email); LS.del("profile:" + email); },
    // Presentes (demonstração): toda conta ganha um código de exemplo pra testar o fluxo.
    async getGifts(email) {
      const all = LS.get("gifts", {});
      const mine = Object.values(all).filter((g) => g.buyer_email === email);
      if (mine.length) return mine;
      const code = "AMIGA" + String(Math.floor(Math.random() * 900) + 100);
      all[code] = { code, buyer_email: email, buyer_name: (LS.get("users", {})[email] || {}).name || "", to_name: "", message: "", active: true, claimed_email: null, claimed_at: null, created_at: Date.now() };
      LS.set("gifts", all); return [all[code]];
    },
    async updateGift(code, patch) { const all = LS.get("gifts", {}); if (all[code]) { all[code] = { ...all[code], ...patch }; LS.set("gifts", all); } },
    async claimGift(email, code) {
      const all = LS.get("gifts", {}); const g = all[String(code || "").toUpperCase().trim()];
      if (!g) return { ok: false, error: "Código não encontrado. Confere com quem te presenteou." };
      if (g.buyer_email === email) return { ok: false, error: "Esse código é pra sua amiga, não pra você." };
      if (g.claimed_email && g.claimed_email !== email) return { ok: false, error: "Este código já foi usado por outra pessoa." };
      g.claimed_email = email; g.claimed_at = g.claimed_at || Date.now(); LS.set("gifts", all);
      return { ok: true, from: g.buyer_name || g.buyer_email };
    },
    async giftReceived(email) { const all = LS.get("gifts", {}); return Object.values(all).find((g) => g.claimed_email === email) || null; },
  };

  // ---------- SUPABASE ----------
  function sb() { return window.__sb || (window.__sb = window.supabase.createClient(cfg.SUPABASE_URL, cfg.SUPABASE_ANON_KEY)); }
  const remote = {
    mode: "supabase",
    async session() {
      const { data } = await sb().auth.getSession();
      const u = data.session && data.session.user;
      return u ? { email: u.email, id: u.id, name: (u.user_metadata && u.user_metadata.name) || "" } : null;
    },
    async signUp(email, password, name) {
      const { data, error } = await sb().auth.signUp({ email, password, options: { data: { name } } });
      if (error) throw new Error(traduz(error.message));
      if (!data.session) throw new Error("Cadastro feito. Confirme o e-mail que enviamos e depois entre.");
      return this.session();
    },
    async signIn(email, password) {
      const { error } = await sb().auth.signInWithPassword({ email, password });
      if (error) throw new Error(traduz(error.message));
      return this.session();
    },
    async signOut() { await sb().auth.signOut(); },
    async resetPassword(email) {
      const { error } = await sb().auth.resetPasswordForEmail(email, { redirectTo: location.href.split("#")[0] });
      if (error) throw new Error(traduz(error.message));
    },
    async updatePassword(password) {
      const { error } = await sb().auth.updateUser({ password });
      if (error) throw new Error(traduz(error.message));
      return true;
    },
    async membership(email) {
      const { data } = await sb().from("members").select("active, plan, expires_at, provider").eq("email", email).maybeSingle();
      if (!data) return { active: false, email, found: false };
      const expired = data.expires_at && new Date(data.expires_at) < new Date();
      return { active: !!data.active && !expired, plan: data.plan, provider: data.provider, email, found: true };
    },
    async getProfile() {
      const { data } = await sb().from("profiles").select("start_date, name").maybeSingle();
      return data || { start_date: null, name: null };
    },
    async setProfile(email, patch) {
      const s = await this.session();
      const { error } = await sb().from("profiles").upsert({ user_id: s.id, ...patch }, { onConflict: "user_id" });
      if (error) throw new Error(traduz(error.message));
    },
    async getEntries() {
      const { data } = await sb().from("entries").select("day, data");
      const out = {}; (data || []).forEach((r) => { out[r.day] = r.data; }); return out;
    },
    async setEntry(email, day, patch, full) {
      // Grava o objeto inteiro que o app já tem na memória: duas gravações seguidas não se atropelam.
      const s = await this.session();
      let merged = full;
      if (!merged) { const all = await this.getEntries(); merged = { ...(all[day] || {}), ...patch }; }
      const { error } = await sb().from("entries").upsert({ user_id: s.id, day, data: { ...merged, updated: Date.now() } }, { onConflict: "user_id,day" });
      if (error) throw new Error(traduz(error.message));
    },
    async getPrep() {
      const { data } = await sb().from("prep").select("key, data");
      const out = {}; (data || []).forEach((r) => { out[r.key] = r.data; }); return out;
    },
    async setPrep(email, key, patch, full) {
      const s = await this.session();
      let merged = full;
      if (!merged) { const all = await this.getPrep(); merged = { ...(all[key] || {}), ...patch }; }
      const { error } = await sb().from("prep").upsert({ user_id: s.id, key, data: merged }, { onConflict: "user_id,key" });
      if (error) throw new Error(traduz(error.message));
    },
    async wipe() { const s = await this.session(); await sb().from("entries").delete().eq("user_id", s.id); await sb().from("prep").delete().eq("user_id", s.id); },
    async getGifts(email) { const { data } = await sb().from("gifts").select("*").eq("buyer_email", email).order("created_at"); return data || []; },
    async updateGift(code, patch) { const { error } = await sb().from("gifts").update(patch).eq("code", code); if (error) throw new Error(traduz(error.message)); },
    async claimGift(email, code) {
      const { data, error } = await sb().rpc("claim_gift", { p_code: String(code || "").toUpperCase().trim() });
      if (error) return { ok: false, error: traduz(error.message) };
      return data || { ok: false, error: "Não deu pra resgatar agora. Tente de novo." };
    },
    async giftReceived(email) { const { data } = await sb().from("gifts").select("code, buyer_name, buyer_email, to_name, message, claimed_at, active").eq("claimed_email", email).maybeSingle(); return data || null; },
  };

  function traduz(m) {
    m = String(m || "");
    if (/Invalid login credentials/i.test(m)) return "E-mail ou senha não conferem.";
    if (/already registered/i.test(m)) return "Esse e-mail já tem cadastro. Entre com a senha.";
    if (/Password should be/i.test(m)) return "A senha precisa ter pelo menos 6 caracteres.";
    if (/Email not confirmed/i.test(m)) return "Confirme o e-mail que enviamos antes de entrar.";
    if (/JWT expired|session_not_found|refresh_token/i.test(m)) return "Sua sessão venceu. Entra de novo.";
    if (/Failed to fetch|NetworkError|Load failed/i.test(m)) return "Sem conexão agora. Tenta de novo em instantes.";
    return m;
  }

  window.DTV_STORE = useSupabase ? remote : local;
})();
