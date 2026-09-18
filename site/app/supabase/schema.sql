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

-- Segurança: cada mulher só vê o que é dela.
alter table public.members enable row level security;
alter table public.profiles enable row level security;
alter table public.entries enable row level security;
alter table public.prep enable row level security;

create policy "member reads own row" on public.members for select
  using (email = auth.jwt() ->> 'email');

create policy "profile own" on public.profiles for all
  using (user_id = auth.uid()) with check (user_id = auth.uid());

create policy "entries own" on public.entries for all
  using (user_id = auth.uid()) with check (user_id = auth.uid());

create policy "prep own" on public.prep for all
  using (user_id = auth.uid()) with check (user_id = auth.uid());

-- updated_at automático
create or replace function public.touch_updated_at() returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end $$;
drop trigger if exists t_members on public.members;
create trigger t_members before update on public.members for each row execute function public.touch_updated_at();
drop trigger if exists t_profiles on public.profiles;
create trigger t_profiles before update on public.profiles for each row execute function public.touch_updated_at();
drop trigger if exists t_entries on public.entries;
create trigger t_entries before update on public.entries for each row execute function public.touch_updated_at();
drop trigger if exists t_prep on public.prep;
create trigger t_prep before update on public.prep for each row execute function public.touch_updated_at();

-- Pra testar sem checkout: libere um e-mail na mão.
-- insert into public.members (email, active, plan, provider) values ('teste@exemplo.com', true, 'travessia', 'manual');
