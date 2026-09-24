-- De Tola a Virtuosa · esquema do banco (Supabase / Postgres)
-- Rode no SQL Editor do projeto. Depois cole a URL e a chave anon em site/app/config.js.

-- Assinaturas: quem pode entrar. Preenchida pelo webhook do checkout (ver functions/checkout-webhook).
create table if not exists public.members (
  email text primary key,
  active boolean not null default true,
  plan text default 'travessia',
  provider text,                 -- hotmart, kiwify, eduzz...
  provider_ref text,             -- id da transação/assinatura na plataforma
  expires_at timestamptz,        -- null = sem vencimento
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- Perfil: nome e data do dia 1.
create table if not exists public.profiles (
  user_id uuid primary key references auth.users(id) on delete cascade,
  name text,
  start_date date,
  updated_at timestamptz default now()
);

-- Um registro por dia (1 a 40): checklist, chips, textos, energia, feito.
create table if not exists public.entries (
  user_id uuid references auth.users(id) on delete cascade,
  day int not null check (day between 1 and 40),
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz default now(),
  primary key (user_id, day)
);

-- Preparação e revisões: compromisso, tola, identidade, proposito, regras, carta, retrato1, retrato40, prova1..prova4.
create table if not exists public.prep (
  user_id uuid references auth.users(id) on delete cascade,
  key text not null,
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz default now(),
  primary key (user_id, key)
);

-- Presentes: quem comprou o "presentear uma amiga" ganha um código. A amiga resgata e vira membro.
create table if not exists public.gifts (
  code text primary key,
  buyer_email text not null,
  buyer_name text,
  to_name text,
  message text,
  active boolean not null default true,
  claimed_email text,
  claimed_at timestamptz,
  provider text,
  provider_ref text,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- Segurança: cada mulher só vê o que é dela.
alter table public.members enable row level security;
alter table public.profiles enable row level security;
alter table public.entries enable row level security;
alter table public.prep enable row level security;

create policy "member reads own row" on public.members for select
  using (email = lower(auth.jwt() ->> 'email'));

create policy "profile own" on public.profiles for all
  using (user_id = auth.uid()) with check (user_id = auth.uid());

create policy "entries own" on public.entries for all
  using (user_id = auth.uid()) with check (user_id = auth.uid());

create policy "prep own" on public.prep for all
  using (user_id = auth.uid()) with check (user_id = auth.uid());

alter table public.gifts enable row level security;
create policy "gift buyer reads" on public.gifts for select
  using (buyer_email = lower(auth.jwt() ->> 'email'));
create policy "gift buyer edits card" on public.gifts for update
  using (buyer_email = lower(auth.jwt() ->> 'email')) with check (buyer_email = lower(auth.jwt() ->> 'email'));
-- A compradora só pode mudar o nome da amiga e o recado. Código, validade e quem resgatou ficam fora do alcance dela.
revoke update on public.gifts from authenticated, anon;
grant update (to_name, message) on public.gifts to authenticated;
-- Sem login ninguém escreve nada nas tabelas (RLS já barra, isto é só cinto e suspensório).
revoke all on public.members, public.gifts, public.entries, public.prep, public.profiles from anon;

-- Resgate: a amiga chama esta função com o código. Roda com privilégio pra criar o membro dela.
create or replace function public.claim_gift(p_code text)
returns json language plpgsql security definer set search_path = public as $$
declare g public.gifts%rowtype; v_email text;
begin
  v_email := lower(auth.jwt() ->> 'email');
  if v_email is null then return json_build_object('ok', false, 'error', 'Entre na sua conta antes de resgatar.'); end if;
  select * into g from public.gifts where code = upper(trim(p_code)) for update;
  if not found then return json_build_object('ok', false, 'error', 'Código não encontrado. Confere com quem te presenteou.'); end if;
  if not g.active then return json_build_object('ok', false, 'error', 'Este presente foi cancelado.'); end if;
  if g.claimed_email is not null and g.claimed_email <> v_email then return json_build_object('ok', false, 'error', 'Este código já foi usado por outra pessoa.'); end if;
  if g.buyer_email = v_email then return json_build_object('ok', false, 'error', 'Esse código é pra sua amiga, não pra você. Você já tem acesso.'); end if;
  -- Quem já comprou não gasta o código de uma amiga por engano (e não vira "presente" de alguém que pode pedir reembolso).
  if exists (select 1 from public.members where email = v_email and active and provider is distinct from 'gift') then
    return json_build_object('ok', false, 'error', 'Você já tem acesso por conta própria. Guarda esse código pra outra amiga.');
  end if;
  update public.gifts set claimed_email = v_email, claimed_at = coalesce(claimed_at, now()) where code = g.code;
  insert into public.members (email, active, plan, provider, provider_ref)
    values (v_email, true, 'presente', 'gift', g.code)
    on conflict (email) do update set active = true, plan = 'presente', provider = 'gift', provider_ref = g.code;
  return json_build_object('ok', true, 'from', coalesce(g.buyer_name, g.buyer_email));
end $$;
grant execute on function public.claim_gift(text) to authenticated;

-- Quem resgatou pode ver de quem veio o presente (só a própria linha).
create policy "gift claimed reads" on public.gifts for select
  using (claimed_email = lower(auth.jwt() ->> 'email'));

-- updated_at automático
create or replace function public.touch_updated_at() returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end $$;
drop trigger if exists t_members on public.members;
create trigger t_members before update on public.members for each row execute function public.touch_updated_at();
drop trigger if exists t_profiles on public.profiles;
create trigger t_profiles before update on public.profiles for each row execute function public.touch_updated_at();
drop trigger if exists t_entries on public.entries;
create trigger t_entries before update on public.entries for each row execute function public.touch_updated_at();
drop trigger if exists t_gifts on public.gifts;
create trigger t_gifts before update on public.gifts for each row execute function public.touch_updated_at();
drop trigger if exists t_prep on public.prep;
create trigger t_prep before update on public.prep for each row execute function public.touch_updated_at();

-- Pra testar sem checkout: libere um e-mail na mão.
-- insert into public.members (email, active, plan, provider) values ('teste@exemplo.com', true, 'travessia', 'manual');
-- Pra testar o presente sem checkout:
-- insert into public.gifts (code, buyer_email, buyer_name) values ('AMIGA123', 'teste@exemplo.com', 'Rebeca');
