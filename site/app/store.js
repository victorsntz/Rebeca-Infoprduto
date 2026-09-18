/* Camada de dados da área de membros.
 * Dois modos, mesma interface:
 *  - local: tudo em localStorage (demonstração, sem servidor)
 *  - supabase: login por e-mail e senha, progresso salvo na nuvem, acesso liberado pela tabela `members`
 */
(function () {
  const cfg = window.DTV_CONFIG || {};
  const useSupabase = !!(cfg.SUPABASE_URL && cfg.SUPABASE_ANON_KEY && window.supabase);

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
    async membership(email) { return { active: true, plan: "demo", email }; },
    async getProfile(email) { return LS.get("profile:" + email, { start_date: null, name: null }); },
    async setProfile(email, data) { const p = await this.getProfile(email); LS.set("profile:" + email, { ...p, ...data }); },
    async getEntries(email) { return LS.get("entries:" + email, {}); },
    async setEntry(email, day, data) { const all = await this.getEntries(email); all[day] = { ...(all[day] || {}), ...data, updated: Date.now() }; LS.set("entries:" + email, all); },
    async getPrep(email) { return LS.get("prep:" + email, {}); },
    async setPrep(email, key, data) { const all = await this.getPrep(email); all[key] = { ...(all[key] || {}), ...data }; LS.set("prep:" + email, all); },
    async wipe(email) { LS.del("entries:" + email); LS.del("prep:" + email); LS.del("profile:" + email); },
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
      const { error } = await sb().auth.resetPasswordForEmail(email, { redirectTo: location.href });
      if (error) throw new Error(traduz(error.message));
    },
    async membership(email) {
      const { data } = await sb().from("members").select("active, plan, expires_at").eq("email", email).maybeSingle();
      if (!data) return { active: false, email };
      const expired = data.expires_at && new Date(data.expires_at) < new Date();
      return { active: !!data.active && !expired, plan: data.plan, email };
    },
    async getProfile() {
      const { data } = await sb().from("profiles").select("start_date, name").maybeSingle();
      return data || { start_date: null, name: null };
    },
    async setProfile(email, patch) {
      const s = await this.session();
      await sb().from("profiles").upsert({ user_id: s.id, ...patch }, { onConflict: "user_id" });
    },
    async getEntries() {
      const { data } = await sb().from("entries").select("day, data");
      const out = {}; (data || []).forEach((r) => { out[r.day] = r.data; }); return out;
    },
    async setEntry(email, day, patch) {
      const s = await this.session();
      const all = await this.getEntries();
      const merged = { ...(all[day] || {}), ...patch, updated: Date.now() };
      await sb().from("entries").upsert({ user_id: s.id, day, data: merged }, { onConflict: "user_id,day" });
    },
    async getPrep() {
      const { data } = await sb().from("prep").select("key, data");
      const out = {}; (data || []).forEach((r) => { out[r.key] = r.data; }); return out;
    },
    async setPrep(email, key, patch) {
      const s = await this.session();
      const all = await this.getPrep();
      await sb().from("prep").upsert({ user_id: s.id, key, data: { ...(all[key] || {}), ...patch } }, { onConflict: "user_id,key" });
    },
    async wipe() { const s = await this.session(); await sb().from("entries").delete().eq("user_id", s.id); await sb().from("prep").delete().eq("user_id", s.id); },
  };

  function traduz(m) {
    m = String(m || "");
    if (/Invalid login credentials/i.test(m)) return "E-mail ou senha não conferem.";
    if (/already registered/i.test(m)) return "Esse e-mail já tem cadastro. Entre com a senha.";
    if (/Password should be/i.test(m)) return "A senha precisa ter pelo menos 6 caracteres.";
    if (/Email not confirmed/i.test(m)) return "Confirme o e-mail que enviamos antes de entrar.";
    return m;
  }

  window.DTV_STORE = useSupabase ? remote : local;
})();
