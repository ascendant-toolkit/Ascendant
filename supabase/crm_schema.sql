-- Customer database (CRM). Safe to rerun. Supabase: SQL Editor > New query > paste this file > Run.
-- Needs schema.sql first (uses is_admin(), products). Admin-only: no policy lets anyone else read or write.
-- A payment webhook (Lemon Squeezy) can later fill orders/order_items/events using external_id to stay idempotent.

create table if not exists public.customers (
  id          bigserial primary key,
  email       text not null check (email = lower(email) and email ~* '^[^@\s]+@[^@\s]+\.[^@\s]+$'),
  name        text not null default '' check (length(name) <= 160),
  kind        text not null default 'student' check (kind in ('student', 'parent', 'teacher', 'school', 'tutor', 'other')),
  org         text check (length(org) <= 160),
  country     text check (length(country) <= 80),
  phone       text check (length(phone) <= 40),
  source      text not null default 'manual' check (source in ('manual', 'waitlist', 'contact', 'checkout', 'school', 'referral', 'import')),
  status      text not null default 'lead' check (status in ('lead', 'active', 'lapsed', 'churned')),
  marketing_ok boolean not null default false,
  tags        text[] not null default '{}',
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);
create unique index if not exists customers_email_key on public.customers (email);

create table if not exists public.orders (
  id           bigserial primary key,
  number       text unique,                         -- human reference, e.g. from the payment provider
  provider     text not null default 'manual' check (provider in ('manual', 'lemonsqueezy', 'invoice', 'other')),
  external_id  text,                                -- provider order/subscription id; unique per provider
  status       text not null default 'paid' check (status in ('pending', 'paid', 'refunded', 'cancelled', 'failed')),
  currency     text not null default 'USD',
  total_cents  integer not null default 0 check (total_cents >= 0),
  refunded_cents integer not null default 0 check (refunded_cents >= 0),
  plan         text check (plan in ('monthly', 'annual', 'seasonal', 'school', 'one-off')),
  placed_at    timestamptz not null default now(),
  note         text,
  created_at   timestamptz not null default now()
);
create unique index if not exists orders_provider_ext_key on public.orders (provider, external_id) where external_id is not null;

create table if not exists public.order_items (
  id          bigserial primary key,
  order_id    bigint not null references public.orders (id) on delete cascade,
  product     text references public.products (id),
  tier        text check (tier in ('free', 'basic', 'full', 'vip')),
  description text,
  qty         integer not null default 1 check (qty > 0),
  unit_cents  integer not null default 0 check (unit_cents >= 0)
);
create index if not exists order_items_order_idx on public.order_items (order_id);

-- Who is tied to an order: the payer, and whoever the access is for (a parent pays, the student learns).
create table if not exists public.customer_orders (
  customer_id bigint not null references public.customers (id) on delete cascade,
  order_id    bigint not null references public.orders (id) on delete cascade,
  role        text not null default 'buyer' check (role in ('buyer', 'recipient')),
  primary key (customer_id, order_id, role)
);
create index if not exists customer_orders_order_idx on public.customer_orders (order_id);

-- Timeline: sign-ups, purchases, access grants, emails, support contacts, anything worth remembering.
create table if not exists public.events (
  id          bigserial primary key,
  customer_id bigint references public.customers (id) on delete cascade,
  order_id    bigint references public.orders (id) on delete set null,
  type        text not null check (type in ('signup', 'order', 'refund', 'grant', 'revoke', 'renewal', 'cancel', 'email', 'contact', 'call', 'note', 'other')),
  summary     text not null check (length(summary) <= 500),
  meta        jsonb not null default '{}',
  occurred_at timestamptz not null default now(),
  created_at  timestamptz not null default now()
);
create index if not exists events_customer_idx on public.events (customer_id, occurred_at desc);

create table if not exists public.customer_notes (
  id          bigserial primary key,
  customer_id bigint not null references public.customers (id) on delete cascade,
  body        text not null check (length(body) between 1 and 4000),
  created_at  timestamptz not null default now()
);
create index if not exists customer_notes_customer_idx on public.customer_notes (customer_id, created_at desc);

create or replace function public.crm_touch() returns trigger language plpgsql as $$
begin new.updated_at := now(); return new; end $$;
drop trigger if exists customers_touch on public.customers;
create trigger customers_touch before update on public.customers for each row execute function public.crm_touch();

-- One row per customer with the numbers the admin list needs.
create or replace view public.customer_summary with (security_invoker = true) as
select c.*,
  coalesce(s.orders, 0) as order_count,
  coalesce(s.spent_cents, 0) as spent_cents,
  s.last_order_at,
  (select max(occurred_at) from public.events e where e.customer_id = c.id) as last_event_at
from public.customers c
left join (
  select co.customer_id, count(*) as orders, sum(o.total_cents - o.refunded_cents) as spent_cents, max(o.placed_at) as last_order_at
  from public.customer_orders co
  join public.orders o on o.id = co.order_id and o.status in ('paid', 'refunded')
  where co.role = 'buyer'
  group by co.customer_id
) s on s.customer_id = c.id;

-- Pull in everyone already on the site: students/parents from profiles, the waitlist, and contact-form senders.
create or replace function public.admin_crm_import() returns integer
language plpgsql security definer set search_path = public as $$
declare n integer := 0; k integer;
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  insert into customers (email, name, kind, source, status)
    select lower(p.email), coalesce(p.name, ''), 'student', 'import', 'active' from profiles p
    on conflict (email) do nothing;
  get diagnostics k = row_count; n := n + k;
  insert into customers (email, name, kind, source, status, marketing_ok)
    select lower(w.email), coalesce(w.name, ''), coalesce(w.role, 'other'), 'waitlist', 'lead', true from waitlist w
    on conflict (email) do nothing;
  get diagnostics k = row_count; n := n + k;
  insert into customers (email, name, kind, source, status)
    select distinct on (lower(m.email)) lower(m.email), m.name, coalesce(m.role, 'other'), 'contact', 'lead' from contact_messages m
    order by lower(m.email), m.created_at
    on conflict (email) do nothing;
  get diagnostics k = row_count; n := n + k;
  return n;
end $$;

do $$ declare t text; begin
  foreach t in array array['customers', 'orders', 'order_items', 'customer_orders', 'events', 'customer_notes'] loop
    execute format('alter table public.%I enable row level security', t);
    execute format('drop policy if exists %I on public.%I', t || '_admin', t);
    execute format('create policy %I on public.%I for all using (is_admin()) with check (is_admin())', t || '_admin', t);
  end loop;
end $$;
