-- Safe to run more than once. Supabase: SQL Editor > New query > paste the CONTENTS of this file > Run.
--
-- Access model: no self-service. A student has one or two login emails (any provider), same password for both.
-- (Earlier note: no emails are sent.) An admin adds each student with an assigned password.
-- Sign-up only succeeds when the password typed matches the one on the class list (checked in the
-- database against the hash), so only the student who was given the password can create the login.

create extension if not exists pgcrypto with schema extensions;

create table if not exists public.admins (
  email            text primary key check (email = lower(email)),
  name             text not null,
  initial_password text            -- set by hand in SQL, never committed to the repo
);
alter table public.admins add column if not exists initial_password text;
-- Admin rows live in supabase/admin_seed.sql (git-ignored; this repo is public).

-- Co-teachers: can open every subject, but have no admin access and see no student data.
create table if not exists public.teachers (
  email    text primary key check (email = lower(email)),
  name     text not null,
  password text not null
);
alter table public.teachers enable row level security;

-- Schools (v8): a school licence covers some subjects at one tier, for a number of student seats, until an end date.
-- Its teachers add and remove their own students (up to the seat limit) and see only their own school's progress.
create table if not exists public.schools (
  id         text primary key check (id ~ '^[a-z0-9-]+$'),
  name       text not null,
  products   text[] not null default '{}',   -- any of: ig-econ, ig-cs, a-econ, a-cs
  tier       text not null default 'full' check (tier in ('free', 'basic', 'full', 'vip')),
  seats      int not null default 30 check (seats >= 0),
  expires_at timestamptz,                    -- null = no end date
  note       text,
  created_at timestamptz not null default now()
);
alter table public.schools enable row level security;
create table if not exists public.school_teachers (
  email     text primary key check (email = lower(email)),
  school_id text not null references public.schools (id) on delete cascade,
  name      text not null,
  password  text not null
);
alter table public.school_teachers enable row level security;

create table if not exists public.profiles (
  email        text primary key check (email = lower(email)),
  name         text not null,
  subjects     text[] not null default '{}',   -- any of: ig-econ, ig-cs, a-econ, a-cs
  password     text not null default '',       -- assigned password, visible to admins only
  created_at   timestamptz not null default now(),
  signed_up_at timestamptz,
  last_seen    timestamptz
);
-- v3: any email address allowed, plus an optional second login email.
alter table public.profiles drop constraint if exists profiles_email_check;
alter table public.profiles drop constraint if exists profiles_email_lower;
alter table public.profiles add constraint profiles_email_lower check (email = lower(email));
alter table public.profiles add column if not exists email2 text;
alter table public.profiles drop constraint if exists profiles_email2_check;
alter table public.profiles add constraint profiles_email2_check check (email2 is null or (email2 = lower(email2) and email2 <> email));
create unique index if not exists profiles_email2_key on public.profiles (email2) where email2 is not null;
alter table public.profiles add column if not exists password text not null default '';
alter table public.profiles add column if not exists classes text[] not null default '{}';    -- ig1-cs, ig2-cs, a-cs, ig2-econ, a-econ
alter table public.profiles add column if not exists requested text[] not null default '{}';  -- subjects awaiting approval
alter table public.profiles add column if not exists school_id text references public.schools (id) on delete set null;  -- v8: seat on a school licence

create table if not exists public.progress (
  email   text not null check (email = lower(email)),
  slug    text not null,
  done_at timestamptz not null default now(),
  primary key (email, slug)
);

alter table public.admins   enable row level security;   -- no policies: clients never read it directly
alter table public.profiles enable row level security;
alter table public.progress enable row level security;

create or replace function public.is_admin() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from admins where email = lower(auth.jwt() ->> 'email'))
$$;

-- The profile key (primary email) behind whichever login email is signed in.
create or replace function public.my_key() returns text
language sql stable security definer set search_path = public as $$
  select coalesce((select email from profiles
                    where email = lower(auth.jwt() ->> 'email') or email2 = lower(auth.jwt() ->> 'email') limit 1),
                  lower(auth.jwt() ->> 'email'))
$$;

create or replace function public.is_member() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from admins   where email = lower(auth.jwt() ->> 'email'))
      or exists (select 1 from teachers where email = lower(auth.jwt() ->> 'email'))
      or exists (select 1 from school_teachers where email = lower(auth.jwt() ->> 'email'))
      or exists (select 1 from profiles where email = lower(auth.jwt() ->> 'email') or email2 = lower(auth.jwt() ->> 'email'))
$$;

drop policy if exists profiles_admin_all on public.profiles;
create policy profiles_admin_all on public.profiles
  for all using (is_admin()) with check (is_admin());

drop policy if exists teachers_admin_all on public.teachers;
create policy teachers_admin_all on public.teachers
  for all using (is_admin()) with check (is_admin());

drop policy if exists schools_admin_all on public.schools;
create policy schools_admin_all on public.schools for all using (is_admin()) with check (is_admin());
drop policy if exists school_teachers_admin_all on public.school_teachers;
create policy school_teachers_admin_all on public.school_teachers for all using (is_admin()) with check (is_admin());

-- The school of the signed-in school teacher (null for anyone else).
create or replace function public.my_school() returns text
language sql stable security definer set search_path = public as $$
  select school_id from school_teachers where email = lower(auth.jwt() ->> 'email')
$$;

-- Subjects and tier a student holds through their school's licence, while it is running.
create or replace function public.school_access(_email text) returns table (product text, tier text, expires_at timestamptz)
language sql stable security definer set search_path = public as $$
  select u, s.tier, s.expires_at from profiles p join schools s on s.id = p.school_id, unnest(s.products) u
   where p.email = _email and (s.expires_at is null or s.expires_at > now())
$$;

-- A school can't hold more students than it has seats (checked whenever someone joins one).
create or replace function public.check_school_seats() returns trigger
language plpgsql security definer set search_path = public as $$
declare cap int; n int;
begin
  if new.school_id is null or (tg_op = 'UPDATE' and new.school_id is not distinct from old.school_id) then return new; end if;
  select seats into cap from schools where id = new.school_id;
  select count(*) into n from profiles where school_id = new.school_id and email <> new.email;
  if n >= cap then raise exception 'All % seats on this school licence are in use', cap; end if;
  return new;
end $$;
drop trigger if exists check_school_seats on public.profiles;
create trigger check_school_seats before insert or update of school_id on public.profiles
  for each row execute function public.check_school_seats();

drop policy if exists progress_select on public.progress;
create policy progress_select on public.progress
  for select using (email = my_key() or is_admin());
drop policy if exists progress_insert on public.progress;
create policy progress_insert on public.progress
  for insert with check (email = my_key() and is_member());
drop policy if exists progress_delete on public.progress;
create policy progress_delete on public.progress
  for delete using (email = my_key());

-- No address may appear twice across primary/second emails, or collide with an admin.
create or replace function public.check_profile_emails() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if exists (select 1 from profiles where email <> new.email and (email = new.email or email2 = new.email))
     or exists (select 1 from admins where email = new.email)
     or exists (select 1 from teachers where email = new.email)
     or exists (select 1 from school_teachers where email = new.email) then
    raise exception 'Email % is already in use', new.email;
  end if;
  if new.email2 is not null and (
       exists (select 1 from profiles where email <> new.email and (email = new.email2 or email2 = new.email2))
       or exists (select 1 from profiles where email = new.email2)
       or exists (select 1 from admins where email = new.email2)
       or exists (select 1 from teachers where email = new.email2)
       or exists (select 1 from school_teachers where email = new.email2)) then
    raise exception 'Email % is already in use', new.email2;
  end if;
  return new;
end $$;
drop trigger if exists check_profile_emails on public.profiles;
create trigger check_profile_emails before insert or update of email, email2 on public.profiles
  for each row execute function public.check_profile_emails();

-- Sign-up gate: the password supplied must match the assigned one (admins: admins.initial_password).
create or replace function public.gate_signup() returns trigger
language plpgsql security definer set search_path = public, extensions as $$
declare a admins; p profiles;
begin
  select * into a from admins where email = lower(new.email);
  if found and a.initial_password is not null and a.initial_password <> ''
     and new.encrypted_password = crypt(a.initial_password, new.encrypted_password) then
    return new;
  end if;
  if exists (select 1 from teachers t where t.email = lower(new.email) and t.password <> ''
             and new.encrypted_password = crypt(t.password, new.encrypted_password)) then
    return new;
  end if;
  if exists (select 1 from school_teachers t where t.email = lower(new.email) and t.password <> ''
             and new.encrypted_password = crypt(t.password, new.encrypted_password)) then
    return new;
  end if;
  select * into p from profiles where email = lower(new.email) or email2 = lower(new.email);
  if found and p.password <> '' and new.encrypted_password = crypt(p.password, new.encrypted_password) then
    update profiles set signed_up_at = coalesce(signed_up_at, now()) where email = p.email;
    return new;
  end if;
  raise exception 'Sign-up refused';
end $$;

drop trigger if exists gate_signup on auth.users;
create trigger gate_signup before insert on auth.users
  for each row execute function public.gate_signup();

-- Nobody can change their login email (stops a student re-pointing their account at an admin address).
create or replace function public.lock_email() returns trigger
language plpgsql as $$
begin
  if new.email is distinct from old.email then raise exception 'Email cannot be changed'; end if;
  return new;
end $$;

drop trigger if exists lock_email on auth.users;
create trigger lock_email before update of email on auth.users
  for each row execute function public.lock_email();

-- Who am I? Returns null if the signed-in user is not on the roster.
create or replace function public.whoami() returns json
language plpgsql security definer set search_path = public as $$
declare e text := lower(auth.jwt() ->> 'email'); a admins; p profiles; st school_teachers; sc schools; live boolean;
begin
  if e is null then return null; end if;
  select * into a from admins where email = e;
  if found then
    return json_build_object('email', e, 'name', a.name, 'is_admin', true,
                             'subjects', array['ig-econ','ig-cs','a-econ','a-cs'], 'requested', array[]::text[]);
  end if;
  if exists (select 1 from teachers where email = e) then
    return json_build_object('email', e, 'name', (select name from teachers where email = e), 'is_admin', false, 'is_teacher', true,
                             'subjects', array['ig-econ','ig-cs','a-econ','a-cs'], 'requested', array[]::text[]);
  end if;
  -- School teachers count as teachers (they preview assessments, don't submit them) but only for their licence's subjects and tier.
  select * into st from school_teachers where email = e;
  if found then
    select * into sc from schools where id = st.school_id;
    live := sc.expires_at is null or sc.expires_at > now();
    return json_build_object('email', e, 'name', st.name, 'is_admin', false, 'is_teacher', true, 'is_school_teacher', true,
                             'school', json_build_object('id', sc.id, 'name', sc.name, 'products', sc.products, 'tier', sc.tier,
                                                         'seats', sc.seats, 'expires_at', sc.expires_at, 'active', live),
                             'subjects', case when live then sc.products else '{}'::text[] end, 'requested', array[]::text[],
                             'entitlements', coalesce((select json_agg(json_build_object('product', u, 'plan', 'school', 'tier', sc.tier, 'expires_at', sc.expires_at))
                                                         from unnest(case when live then sc.products else '{}'::text[] end) u), '[]'::json));
  end if;
  update profiles set last_seen = now() where email = e or email2 = e returning * into p;
  if not found then return null; end if;
  return json_build_object('email', p.email, 'email2', p.email2, 'login', e, 'name', p.name, 'is_admin', false,
                           'subjects', effective_subjects(p.email), 'requested', p.requested, 'paywall', paywall_on(),
                           'school', (select name from schools where id = p.school_id),
                           'entitlements', coalesce((select json_agg(x) from (
                               select json_build_object('product', product, 'plan', plan, 'tier', tier, 'expires_at', expires_at) x
                                 from entitlements where email = p.email and is_active(starts_at, expires_at)
                               union all
                               select json_build_object('product', product, 'plan', 'school', 'tier', tier, 'expires_at', expires_at)
                                 from school_access(p.email)) q), '[]'::json));
end $$;

-- Admin: every progress row in one JSON value (avoids the 1000-row API cap).
create or replace function public.admin_progress() returns json
language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  return coalesce((select json_agg(json_build_object('email', email, 'slug', slug, 'done_at', done_at)) from progress), '[]'::json);
end $$;

-- Creates a ready-to-use, already-confirmed login directly (no sign-up, no email, no Confirm-email setting).
-- Internal: not callable from the website. Used by the admin functions below and by the bootstrap line at the end.
create or replace function public._create_login(_email text, _password text) returns void
language plpgsql security definer set search_path = public, extensions, auth as $$
declare uid uuid := gen_random_uuid(); e text := lower(_email);
begin
  if exists (select 1 from auth.users where email = e) then return; end if;
  insert into auth.users (instance_id, id, aud, role, email, encrypted_password, email_confirmed_at,
      raw_app_meta_data, raw_user_meta_data, created_at, updated_at,
      confirmation_token, recovery_token, email_change_token_new, email_change,
      email_change_token_current, phone_change, phone_change_token, reauthentication_token)
  values ('00000000-0000-0000-0000-000000000000', uid, 'authenticated', 'authenticated', e,
      crypt(_password, gen_salt('bf')), now(),
      '{"provider":"email","providers":["email"]}', '{}', now(), now(), '', '', '', '', '', '', '', '');
  insert into auth.identities (id, user_id, provider_id, identity_data, provider, last_sign_in_at, created_at, updated_at)
  values (gen_random_uuid(), uid, uid::text,
      jsonb_build_object('sub', uid::text, 'email', e, 'email_verified', true, 'phone_verified', false),
      'email', now(), now(), now());
  update profiles set signed_up_at = coalesce(signed_up_at, now()) where email = e or email2 = e;
end $$;
revoke all on function public._create_login(text, text) from public, anon, authenticated;

-- Admin: create the login for a student already on the list, using the password on the list.
create or replace function public.admin_create_login(target text) returns void
language plpgsql security definer set search_path = public as $$
declare pw text;
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  select password into pw from profiles where email = lower(target) or email2 = lower(target);
  if pw is null or pw = '' then raise exception 'No password set for %', target; end if;
  perform _create_login(target, pw);
end $$;

-- Admin: recreate a student's login(s) with the password currently on the list (keeps their progress).
create or replace function public.admin_reset_login(target text) returns void
language plpgsql security definer set search_path = public, auth as $$
declare p profiles;
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  target := lower(target);
  if exists (select 1 from admins where email = target) then raise exception 'Cannot reset an admin'; end if;
  select * into p from profiles where email = target;
  if not found or p.password = '' then raise exception 'No password set for %', target; end if;
  delete from auth.users where email = p.email or email = p.email2;
  perform _create_login(p.email, p.password);
  if p.email2 is not null then perform _create_login(p.email2, p.password); end if;
end $$;

-- Admin: set, change or remove a student's second login email.
create or replace function public.admin_set_email2(target text, new_email2 text) returns void
language plpgsql security definer set search_path = public, auth as $$
declare p profiles; n text := nullif(lower(trim(coalesce(new_email2, ''))), '');
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  select * into p from profiles where email = lower(target);
  if not found then raise exception 'No such student'; end if;
  if p.email2 is not null then delete from auth.users where email = p.email2; end if;
  update profiles set email2 = n where email = p.email;
  if n is not null then
    if p.password = '' then raise exception 'No password set for %', target; end if;
    perform _create_login(n, p.password);
  end if;
end $$;

-- Student: change password. Applies to both of their login emails so they stay in step.
create or replace function public.set_my_password(new_password text) returns void
language plpgsql security definer set search_path = public, extensions, auth as $$
declare e text := lower(auth.jwt() ->> 'email'); k text; e2 text;
begin
  if e is null then raise exception 'Not signed in'; end if;
  if length(new_password) < 8 then raise exception 'Password must be at least 8 characters'; end if;
  k := my_key();
  select email2 into e2 from profiles where email = k;
  update auth.users set encrypted_password = crypt(new_password, gen_salt('bf')), updated_at = now()
   where email = e or email = k or (e2 is not null and email = e2);
end $$;

-- Admin: add a co-teacher with their own login (generated password is passed in from the admin panel).
create or replace function public.admin_add_teacher(t_name text, t_email text, t_password text) returns void
language plpgsql security definer set search_path = public as $$
declare e text := lower(trim(t_email));
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  if length(t_password) < 8 then raise exception 'Password too short'; end if;
  if exists (select 1 from admins where email = e) or exists (select 1 from teachers where email = e)
     or exists (select 1 from school_teachers where email = e)
     or exists (select 1 from profiles where email = e or email2 = e) then
    raise exception 'Email % is already in use', e;
  end if;
  insert into teachers (email, name, password) values (e, trim(t_name), t_password);
  perform _create_login(e, t_password);
end $$;

create or replace function public.admin_remove_teacher(t_email text) returns void
language plpgsql security definer set search_path = public, auth as $$
declare e text := lower(t_email);
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  delete from progress where email = e;
  delete from auth.users where email = e;
  delete from teachers where email = e;
end $$;

-- Student asks to join a subject; an admin approves or declines from the admin panel.
create or replace function public.request_subject(subject text) returns void
language plpgsql security definer set search_path = public as $$
declare e text := my_key();
begin
  if subject <> all (array['ig-econ','ig-cs','a-econ','a-cs']) then raise exception 'Unknown subject'; end if;
  update profiles set requested = array_append(requested, subject)
   where email = e and not (subject = any (subjects)) and not (subject = any (requested));
end $$;

create or replace function public.cancel_request(subject text) returns void
language plpgsql security definer set search_path = public as $$
begin
  update profiles set requested = array_remove(requested, subject) where email = my_key();
end $$;

-- ===================== Assessments (v4) =====================
-- Answer keys live in a table no client can read. Marking happens inside submit_assessment().
create table if not exists public.assessments (
  slug       text primary key,
  title      text not null,
  pass_pct   int  not null default 80,
  questions  jsonb not null,          -- full questions incl. answer keys, feedback
  updated_at timestamptz not null default now()
);
alter table public.assessments enable row level security;   -- no policies: unreadable from the website

create table if not exists public.assessment_attempts (
  id           bigint generated always as identity primary key,
  email        text not null,
  slug         text not null,
  answers      jsonb not null,
  score        int not null,
  max_score    int not null,
  pct          int not null,
  result       jsonb not null,
  submitted_at timestamptz not null default now(),
  reset_at     timestamptz            -- set when the teacher allows a retake; row stays as history
);
alter table public.assessment_attempts add column if not exists retake_requested_at timestamptz;
create unique index if not exists attempts_one_live on public.assessment_attempts (email, slug) where reset_at is null;
alter table public.assessment_attempts enable row level security;   -- reads only through the functions below

create or replace function public.has_assessment(_slug text) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from assessments where slug = _slug)
$$;

-- Lessons with an assessment are completed by passing it (or by the teacher), not by self-marking.
drop policy if exists progress_insert on public.progress;
create policy progress_insert on public.progress
  for insert with check (email = my_key() and is_member() and not has_assessment(slug));
drop policy if exists progress_delete on public.progress;
create policy progress_delete on public.progress
  for delete using (email = my_key() and not has_assessment(slug));

-- Lowercase, strip punctuation, collapse spaces.
create or replace function public._norm(t text) returns text
language sql immutable as $$
  select trim(regexp_replace(regexp_replace(regexp_replace(lower(replace(coalesce(t, ''), chr(8722), '-')), '[^a-z0-9.% -]+', ' ', 'g'), '\.( |$)', ' ', 'g'), '\s+', ' ', 'g'))
$$;

-- Does the typed answer contain the phrase? A trailing * allows any word ending (opportunit* matches opportunity/opportunities).
create or replace function public._hit(typed text, alt text) returns boolean
language plpgsql immutable as $$
declare a text := public._norm(replace(alt, '*', '')); pat text;
begin
  if a = '' then return false; end if;
  pat := '(^| )' || regexp_replace(a, '([.%-])', '\\\1', 'g') || case when right(alt, 1) = '*' then '' else '( |$)' end;
  return public._norm(typed) ~ pat;
end $$;

create or replace function public._first_number(t text) returns numeric
language sql immutable as $$
  select (regexp_match(replace(replace(coalesce(t, ''), ',', ''), chr(8722), '-'), '-?\d+(?:\.\d+)?'))[1]::numeric
$$;

-- Mark one question. Returns marks gained.
create or replace function public._mark(q jsonb, typed text) returns int
language plpgsql immutable as $$
declare t text := q ->> 'type'; got int := 0; g jsonb; alt jsonb; n numeric;
begin
  if typed is null or btrim(typed) = '' then return 0; end if;
  if t = 'mcq' then
    return case when btrim(typed) = (q ->> 'ans') then coalesce((q ->> 'marks')::int, 1) else 0 end;
  elsif t = 'num' then
    n := public._first_number(typed);
    if n is not null and q ->> 'abs' = 'true' then n := abs(n); end if;
    if n is not null and abs(n - (q ->> 'ans')::numeric) <= coalesce((q ->> 'tol')::numeric, 0) then
      return coalesce((q ->> 'marks')::int, 1);
    end if;
    return 0;
  else
    for g in select * from jsonb_array_elements(q -> 'groups') loop
      for alt in select * from jsonb_array_elements(g) loop
        if public._hit(typed, alt #>> '{}') then got := got + 1; exit; end if;
      end loop;
    end loop;
    return least(got, coalesce((q ->> 'marks')::int, jsonb_array_length(q -> 'groups')));
  end if;
end $$;

-- Questions without keys or feedback, plus this student's live attempt (with feedback) if they have one.
create or replace function public.get_assessment(_slug text) returns json
language plpgsql security definer set search_path = public as $$
declare a assessments; att assessment_attempts; e text := my_key();
begin
  if not is_member() then raise exception 'Sign in first'; end if;
  select * into a from assessments where slug = _slug;
  if not found then return null; end if;
  select * into att from assessment_attempts where email = e and slug = _slug and reset_at is null;
  return json_build_object(
    'slug', a.slug, 'title', a.title, 'pass', a.pass_pct,
    'questions', (select json_agg(jsonb_build_object('id', q ->> 'id', 'type', q ->> 'type', 'q', q ->> 'q',
                    'opts', q -> 'opts', 'code', q ->> 'code', 'marks', coalesce((q ->> 'marks')::int, 1), 'topic', q ->> 'topic', 'hint', q ->> 'hint'))
                  from jsonb_array_elements(a.questions) q),
    'attempt', case when att.id is null then null else json_build_object('answers', att.answers, 'score', att.score, 'max', att.max_score,
                    'pct', att.pct, 'result', att.result, 'at', att.submitted_at, 'requested', att.retake_requested_at) end);
end $$;

-- One attempt only. Marks, stores, auto-completes the lesson at/above the pass mark, returns the full feedback.
create or replace function public.submit_assessment(_slug text, _answers jsonb) returns json
language plpgsql security definer set search_path = public as $$
declare a assessments; e text := my_key(); q jsonb; typed text; got int; tot int := 0; sc int := 0;
        items jsonb := '[]'::jsonb; p int; weak text[] := '{}'; res jsonb;
begin
  if not is_member() then raise exception 'Sign in first'; end if;
  if exists (select 1 from admins where email = lower(auth.jwt() ->> 'email'))
     or exists (select 1 from teachers where email = lower(auth.jwt() ->> 'email'))
     or exists (select 1 from school_teachers where email = lower(auth.jwt() ->> 'email')) then
    raise exception 'Teacher accounts preview the assessment but do not submit it';
  end if;
  select * into a from assessments where slug = _slug;
  if not found then raise exception 'No assessment for this lesson'; end if;
  if exists (select 1 from assessment_attempts where email = e and slug = _slug and reset_at is null) then
    raise exception 'Already submitted. Ask your teacher to reset it for a retake.';
  end if;
  for q in select * from jsonb_array_elements(a.questions) loop
    typed := _answers ->> (q ->> 'id');
    got := _mark(q, typed);
    tot := tot + coalesce((q ->> 'marks')::int, case when q ->> 'type' = 'text' then jsonb_array_length(q -> 'groups') else 1 end);
    sc := sc + got;
    items := items || jsonb_build_array(jsonb_build_object('id', q ->> 'id', 'got', got,
        'max', coalesce((q ->> 'marks')::int, case when q ->> 'type' = 'text' then jsonb_array_length(q -> 'groups') else 1 end),
        'q', q ->> 'q', 'code', q ->> 'code', 'typed', case when q ->> 'type' = 'mcq' and typed ~ '^[0-9]+$' then q -> 'opts' ->> typed::int else typed end, 'model', q ->> 'model', 'feedback', case when got >= coalesce((q ->> 'marks')::int, 1) then q ->> 'ok'
                         when got > 0 and q ? 'fb_part' then q ->> 'fb_part' else q ->> 'fb' end,
        'topic', q ->> 'topic'));
  end loop;
  p := case when tot = 0 then 0 else round(100.0 * sc / tot) end;
  res := jsonb_build_object('items', items);
  insert into assessment_attempts (email, slug, answers, score, max_score, pct, result) values (e, _slug, _answers, sc, tot, p, res);
  if p >= a.pass_pct then
    insert into progress (email, slug) values (e, _slug) on conflict do nothing;
  end if;
  return json_build_object('score', sc, 'max', tot, 'pct', p, 'pass', a.pass_pct, 'result', res);
end $$;

-- Student: my own scores (slug, pct, when).
create or replace function public.my_attempts() returns json
language sql stable security definer set search_path = public as $$
  select coalesce(json_agg(json_build_object('slug', slug, 'pct', pct, 'score', score, 'max', max_score, 'at', submitted_at) order by submitted_at desc), '[]'::json)
  from assessment_attempts where email = my_key() and reset_at is null
$$;

-- Student: after passing, start a fresh attempt for practice. The pass stays recorded (lesson stays complete); the old attempt is kept as history.
create or replace function public.retake_assessment(_slug text) returns void
language plpgsql security definer set search_path = public as $$
declare e text := my_key(); pass int;
begin
  select pass_pct into pass from assessments where slug = _slug;
  update assessment_attempts set reset_at = now()
   where email = e and slug = _slug and reset_at is null and pct >= coalesce(pass, 80);
  if not found then raise exception 'You can retake an assessment once you have passed it. Otherwise ask your teacher.'; end if;
end $$;

-- Student: ask the teacher for a retake after not passing.
create or replace function public.request_retake(_slug text) returns void
language plpgsql security definer set search_path = public as $$
declare e text := my_key(); pass int;
begin
  select pass_pct into pass from assessments where slug = _slug;
  update assessment_attempts set retake_requested_at = now()
   where email = e and slug = _slug and reset_at is null and pct < coalesce(pass, 80) and retake_requested_at is null;
  if not found then raise exception 'No retake request is needed or one is already waiting.'; end if;
end $$;

create or replace function public.admin_decline_retake(_id bigint) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  update assessment_attempts set retake_requested_at = null where id = _id;
end $$;

-- Admin: counts for the navbar bell.
create or replace function public.admin_notifications() returns json
language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then return json_build_object('approvals', 0, 'retakes', 0); end if;
  return json_build_object(
    'approvals', (select coalesce(sum(cardinality(requested)), 0) from profiles),
    'retakes', (select count(*) from assessment_attempts where retake_requested_at is not null and reset_at is null));
end $$;

-- Admin: every attempt (history included) with its feedback.
create or replace function public.admin_attempts() returns json
language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  return coalesce((select json_agg(json_build_object('id', id, 'email', email, 'slug', slug, 'score', score, 'max', max_score, 'pct', pct,
            'result', result, 'at', submitted_at, 'reset_at', reset_at, 'requested_at', retake_requested_at) order by submitted_at desc) from assessment_attempts), '[]'::json);
end $$;

-- Admin: allow a retake (the old attempt stays as history).
create or replace function public.admin_reset_attempt(_id bigint) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  update assessment_attempts set reset_at = now() where id = _id and reset_at is null;
end $$;

-- Admin: mark a lesson done / not done for a student, whatever their score.
create or replace function public.admin_set_done(_email text, _slug text, _done boolean) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  if _done then insert into progress (email, slug) values (lower(_email), _slug) on conflict do nothing;
  else delete from progress where email = lower(_email) and slug = _slug; end if;
end $$;

create or replace function public.admin_delete_student(target text) returns void
language plpgsql security definer set search_path = public, auth as $$
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  target := lower(target);
  delete from progress where email = target;
  delete from assessment_attempts where email = target;
  delete from entitlements where email = target;
  delete from auth.users where email = target or email = (select email2 from profiles where email = target);
  delete from profiles where email = target;
end $$;

-- Chapter review vs additional resource (or hidden = deleted), set by an admin from the site. Overrides the default in site_data.py.
create table if not exists public.artifact_roles (
  slug       text primary key,
  role       text not null check (role in ('review', 'resource')),
  updated_at timestamptz not null default now()
);
alter table public.artifact_roles drop constraint if exists artifact_roles_role_check;
alter table public.artifact_roles add constraint artifact_roles_role_check check (role in ('review', 'resource', 'hidden'));
alter table public.artifact_roles enable row level security;
drop policy if exists artifact_roles_read on public.artifact_roles;
create policy artifact_roles_read on public.artifact_roles for select using (true);
drop policy if exists artifact_roles_admin on public.artifact_roles;
create policy artifact_roles_admin on public.artifact_roles
  for all using (is_admin()) with check (is_admin());

-- Landing page sign-up list: anyone can add themselves; only admins can read or change it.
create table if not exists public.waitlist (
  id         bigserial primary key,
  email      text not null check (email ~* '^[^@\s]+@[^@\s]+\.[^@\s]+$' and length(email) <= 254),
  name       text check (length(name) <= 120),
  role       text check (role in ('student', 'parent', 'teacher')),
  subjects   text[] not null default '{}',
  created_at timestamptz not null default now()
);
create unique index if not exists waitlist_email_key on public.waitlist (lower(email));
alter table public.waitlist enable row level security;
drop policy if exists waitlist_insert on public.waitlist;
create policy waitlist_insert on public.waitlist for insert to anon, authenticated with check (true);
drop policy if exists waitlist_admin on public.waitlist;
create policy waitlist_admin on public.waitlist
  for all using (is_admin()) with check (is_admin());

-- ===================== Entitlements (v5) =====================
-- Who may open which course. The site reads whoami().subjects, so the front end never changes:
--   paywall off (today): subjects = the list an admin sets on the profile, plus any active entitlements.
--   paywall on (later):  subjects = active entitlements only. Subjects set on a profile are mirrored into
--                        entitlements (source 'manual') by a trigger, so flipping the switch locks nobody out.
-- 'school-all' unlocks all four subjects (school licence). Seasonal or annual passes are entitlements with an expires_at.
create table if not exists public.settings (
  key   text primary key,
  value text not null
);
alter table public.settings enable row level security;   -- no policies: read through paywall_on(), changed through admin_set_paywall()
insert into public.settings (key, value) values ('paywall_enabled', 'false') on conflict (key) do nothing;

create table if not exists public.products (
  id          text primary key,                 -- ig-econ, ig-cs, a-econ, a-cs, school-all
  title       text not null,
  level       text,
  subject     text,
  price_cents integer,                          -- set when pricing is decided; null for now
  currency    text not null default 'USD',
  active      boolean not null default true
);
insert into public.products (id, title, level, subject) values
  ('ig-econ', 'IGCSE Economics (0455)', 'IGCSE', 'Economics'),
  ('ig-cs', 'IGCSE Computer Science (0478)', 'IGCSE', 'Computer Science'),
  ('a-econ', 'A-Level Economics (9708)', 'A-Level', 'Economics'),
  ('a-cs', 'A-Level Computer Science (9618)', 'A-Level', 'Computer Science'),
  ('school-all', 'School licence: all four syllabuses', null, null)
on conflict (id) do nothing;
alter table public.products enable row level security;
drop policy if exists products_read on public.products;
create policy products_read on public.products for select using (true);
drop policy if exists products_admin on public.products;
create policy products_admin on public.products for all using (is_admin()) with check (is_admin());

create table if not exists public.entitlements (
  email      text not null check (email = lower(email)),
  product    text not null references public.products (id),
  source     text not null default 'manual' check (source in ('manual', 'payment', 'school')),
  plan       text not null default 'free' check (plan in ('free', 'annual', 'seasonal', 'school')),
  tier       text not null default 'full' check (tier in ('free', 'basic', 'full', 'vip')),  -- depth of access; 'full' is the historical default
  org        text,                              -- school name for school licences
  starts_at  timestamptz not null default now(),
  expires_at timestamptz,                       -- null = no expiry
  note       text,
  created_at timestamptz not null default now(),
  primary key (email, product)
);
alter table public.entitlements enable row level security;
alter table public.entitlements add column if not exists tier text not null default 'full';  -- for tables created before v7
alter table public.entitlements drop constraint if exists entitlements_tier_check;
alter table public.entitlements add constraint entitlements_tier_check check (tier in ('free', 'basic', 'full', 'vip'));
drop policy if exists entitlements_select on public.entitlements;
create policy entitlements_select on public.entitlements for select using (email = my_key() or is_admin());
drop policy if exists entitlements_admin on public.entitlements;
create policy entitlements_admin on public.entitlements for all using (is_admin()) with check (is_admin());

create or replace function public.is_active(_starts timestamptz, _expires timestamptz) returns boolean
language sql stable as $$ select _starts <= now() and (_expires is null or _expires > now()) $$;

-- Access tiers are an ordered ladder: free < basic < full < vip. A lesson names the lowest tier that opens it
-- (artifact_courses.min_tier); a student clears it when they hold that subject at an equal or higher tier.
create or replace function public.tier_rank(_tier text) returns int
language sql immutable as $$
  select case _tier when 'free' then 0 when 'basic' then 1 when 'full' then 2 when 'vip' then 3 else -1 end
$$;

create or replace function public.paywall_on() returns boolean
language sql stable security definer set search_path = public as $$
  select coalesce((select value = 'true' from settings where key = 'paywall_enabled'), false)
$$;

create or replace function public.effective_subjects(_email text) returns text[]
language sql stable security definer set search_path = public as $$
  select coalesce(array_agg(distinct s order by s), '{}') from (
    select unnest(case when p.product = 'school-all' then array['ig-econ','ig-cs','a-econ','a-cs'] else array[p.product] end) as s
      from entitlements p where p.email = _email and is_active(p.starts_at, p.expires_at)
    union
    select unnest(subjects) from profiles where email = _email and not paywall_on()
    union
    select product from school_access(_email)
  ) x
$$;

-- Keep entitlements in step with the subjects an admin sets on a profile.
create or replace function public.sync_subject_entitlements() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  insert into entitlements (email, product, source, plan)
    select new.email, s, 'manual', 'free' from unnest(new.subjects) s
     where s in (select id from products) on conflict (email, product) do nothing;
  delete from entitlements
   where email = new.email and source = 'manual' and product = any (array['ig-econ','ig-cs','a-econ','a-cs'])
     and product <> all (new.subjects);
  return new;
end $$;
drop trigger if exists sync_subject_entitlements on public.profiles;
create trigger sync_subject_entitlements after insert or update of subjects on public.profiles
  for each row execute function public.sync_subject_entitlements();

-- One-off backfill for students who already have subjects.
insert into public.entitlements (email, product, source, plan)
  select p.email, s, 'manual', 'free' from public.profiles p, unnest(p.subjects) s
   where s in (select id from public.products) on conflict (email, product) do nothing;

-- Admin: switch the paywall. Refuses to turn it on while any student with subjects has no active entitlement for one of them.
create or replace function public.admin_set_paywall(on_ boolean) returns void
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  if on_ then
    select count(*) into n from profiles p, unnest(p.subjects) s
     where not exists (select 1 from entitlements e where e.email = p.email and is_active(e.starts_at, e.expires_at)
                         and (e.product = s or e.product = 'school-all'));
    if n > 0 then raise exception '% subject allocation(s) have no active entitlement; see admin_paywall_check()', n; end if;
  end if;
  insert into settings (key, value) values ('paywall_enabled', on_::text)
    on conflict (key) do update set value = excluded.value;
end $$;

-- Admin: who would lose a subject if the paywall were switched on now?
create or replace function public.admin_paywall_check() returns json
language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  return json_build_object('paywall', paywall_on(), 'would_lose', coalesce((
    select json_agg(json_build_object('email', p.email, 'subject', s)) from profiles p, unnest(p.subjects) s
     where not exists (select 1 from entitlements e where e.email = p.email and is_active(e.starts_at, e.expires_at)
                         and (e.product = s or e.product = 'school-all'))), '[]'::json));
end $$;

-- Admin: give someone a product (annual or seasonal pass, school licence). Replaces any existing row for that product.
create or replace function public.admin_grant(target text, _product text, _plan text default 'annual',
                                              _expires timestamptz default null, _org text default null, _note text default null,
                                              _tier text default 'full')
returns void language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  if not exists (select 1 from profiles where email = lower(target)) then raise exception 'No such student'; end if;
  insert into entitlements (email, product, source, plan, tier, org, expires_at, note)
    values (lower(target), _product, case when _plan = 'school' then 'school' else 'payment' end, _plan, _tier, _org, _expires, _note)
    on conflict (email, product) do update
      set source = excluded.source, plan = excluded.plan, tier = excluded.tier, org = excluded.org, starts_at = now(), expires_at = excluded.expires_at, note = excluded.note;
end $$;

create or replace function public.admin_revoke(target text, _product text) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  delete from entitlements where email = lower(target) and product = _product;
end $$;

-- ===================== Locked lessons (v6) =====================
-- Lesson files are published encrypted. The key for a lesson is derived from a master secret held only in
-- settings ('gate_master', set by running supabase/gate_secret.sql once) and is handed out only to admins,
-- co-teachers and members whose subjects (see effective_subjects) include one of the lesson's courses.
-- supabase/artifact_access_seed.sql, written by build.py, lists each locked lesson and its courses.
create table if not exists public.artifact_courses (
  slug     text primary key,
  courses  text[] not null,
  min_tier text not null default 'full'   -- lowest tier that opens this lesson; 'full' is the historical default
);
alter table public.artifact_courses enable row level security;   -- no policies: read only inside artifact_key()
alter table public.artifact_courses add column if not exists min_tier text not null default 'full';  -- for tables created before v7
alter table public.artifact_courses drop constraint if exists artifact_courses_min_tier_check;
alter table public.artifact_courses add constraint artifact_courses_min_tier_check check (min_tier in ('free', 'basic', 'full', 'vip'));

create or replace function public.artifact_key(_slug text) returns text
language plpgsql stable security definer set search_path = public, extensions as $$
declare e text := lower(auth.jwt() ->> 'email'); c text[]; m text; mt text; trank int; staff boolean;
begin
  if e is null then return null; end if;
  select value into m from settings where key = 'gate_master';
  if m is null then return null; end if;
  -- Admins and co-teachers can open any lesson, even one not yet listed in artifact_courses.
  staff := exists (select 1 from admins where email = e) or exists (select 1 from teachers where email = e);
  if not staff then
    select courses, min_tier into c, mt from artifact_courses where slug = _slug;
    if c is null then return null; end if;
    -- School teachers open their licence's subjects at their licence's tier while it runs.
    if exists (select 1 from school_teachers where email = e) then
      if not exists (select 1 from school_teachers t join schools s on s.id = t.school_id
                      where t.email = e and s.products && c and tier_rank(s.tier) >= tier_rank(mt)
                        and (s.expires_at is null or s.expires_at > now())) then
        return null;
      end if;
      return encode(hmac(convert_to('artifact:' || _slug, 'utf8'), convert_to(m, 'utf8'), 'sha256'), 'base64');
    end if;
    -- Subject gate (unchanged): the student must hold one of the lesson's subjects.
    if not exists (select 1 from profiles p where (p.email = e or p.email2 = e) and effective_subjects(p.email) && c) then
      return null;
    end if;
    -- Tier gate: the highest tier they hold on one of this lesson's products (school-all and school licences count) must reach min_tier.
    -- A student with the subject but no matching entitlement row (legacy / paywall-off) is treated as 'full', so nobody loses access.
    select coalesce(max(r), tier_rank('full')) into trank from (
      select tier_rank(ent.tier) r
        from profiles p
        join entitlements ent on ent.email = p.email and is_active(ent.starts_at, ent.expires_at)
                             and (ent.product = any (c) or ent.product = 'school-all')
       where (p.email = e or p.email2 = e)
      union all
      select tier_rank(sa.tier) from profiles p, school_access(p.email) sa
       where (p.email = e or p.email2 = e) and sa.product = any (c)) z;
    if trank < tier_rank(mt) then return null; end if;
  end if;
  return encode(hmac(convert_to('artifact:' || _slug, 'utf8'), convert_to(m, 'utf8'), 'sha256'), 'base64');
end $$;

-- ===================== Schools (v8) =====================
-- Admins edit schools directly (RLS). Teacher logins and anything a school teacher does go through these functions.
create or replace function public.admin_add_school_teacher(_school text, t_name text, t_email text, t_password text) returns void
language plpgsql security definer set search_path = public as $$
declare e text := lower(trim(t_email));
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  if length(t_password) < 8 then raise exception 'Password too short'; end if;
  if exists (select 1 from admins where email = e) or exists (select 1 from teachers where email = e)
     or exists (select 1 from school_teachers where email = e)
     or exists (select 1 from profiles where email = e or email2 = e) then
    raise exception 'Email % is already in use', e;
  end if;
  insert into school_teachers (email, school_id, name, password) values (e, _school, trim(t_name), t_password);
  perform _create_login(e, t_password);
end $$;

create or replace function public.admin_remove_school_teacher(t_email text) returns void
language plpgsql security definer set search_path = public, auth as $$
declare e text := lower(t_email);
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  delete from auth.users where email = e;
  delete from school_teachers where email = e;
end $$;

-- Admin: delete a school and its teacher logins. Its students stay on the site, with no school.
create or replace function public.admin_delete_school(_school text) returns void
language plpgsql security definer set search_path = public, auth as $$
begin
  if not is_admin() then raise exception 'Admins only'; end if;
  delete from auth.users where email in (select email from school_teachers where school_id = _school);
  delete from schools where id = _school;
end $$;

-- School teacher: their students, progress and live assessment scores.
create or replace function public.school_dashboard() returns json
language plpgsql security definer set search_path = public as $$
declare sid text := my_school();
begin
  if sid is null then raise exception 'School teachers only'; end if;
  return json_build_object(
    'students', coalesce((select json_agg(json_build_object('email', email, 'email2', email2, 'name', name, 'password', password,
                            'signed_up_at', signed_up_at, 'last_seen', last_seen) order by name) from profiles where school_id = sid), '[]'::json),
    'progress', coalesce((select json_agg(json_build_object('email', g.email, 'slug', g.slug, 'done_at', g.done_at))
                            from progress g join profiles p on p.email = g.email where p.school_id = sid), '[]'::json),
    'attempts', coalesce((select json_agg(json_build_object('email', a.email, 'slug', a.slug, 'pct', a.pct, 'score', a.score, 'max', a.max_score, 'at', a.submitted_at)
                            order by a.submitted_at desc)
                            from assessment_attempts a join profiles p on p.email = a.email where p.school_id = sid and a.reset_at is null), '[]'::json));
end $$;

-- School teacher: add a student to their school (seat limit is checked by check_school_seats).
-- A student who left a school keeps their login and progress and can be added back.
create or replace function public.school_add_student(_name text, _email text, _email2 text, _password text) returns void
language plpgsql security definer set search_path = public as $$
declare sid text := my_school(); e text := lower(trim(_email)); e2 text := nullif(lower(trim(coalesce(_email2, ''))), ''); p profiles;
begin
  if sid is null then raise exception 'School teachers only'; end if;
  if length(_password) < 8 then raise exception 'Password too short'; end if;
  if (select expires_at from schools where id = sid) <= now() then raise exception 'This school licence has ended'; end if;
  select * into p from profiles where email = e;
  if found then
    if p.school_id = sid then return; end if;
    if p.school_id is not null or cardinality(p.subjects) > 0 then raise exception 'Email % is already in use', e; end if;
    update profiles set school_id = sid, name = trim(_name) where email = e;
    return;
  end if;
  insert into profiles (email, email2, name, password, school_id) values (e, e2, trim(_name), _password, sid);
  perform _create_login(e, _password);
  if e2 is not null then perform _create_login(e2, _password); end if;
end $$;

-- School teacher: take a student off the licence (frees the seat; their login and progress are kept).
create or replace function public.school_remove_student(_email text) returns void
language plpgsql security definer set search_path = public as $$
declare sid text := my_school();
begin
  if sid is null then raise exception 'School teachers only'; end if;
  update profiles set school_id = null where email = lower(_email) and school_id = sid;
end $$;

-- School teacher: recreate a student's login(s) with the listed password.
create or replace function public.school_reset_login(_email text) returns void
language plpgsql security definer set search_path = public, auth as $$
declare sid text := my_school(); p profiles;
begin
  if sid is null then raise exception 'School teachers only'; end if;
  select * into p from profiles where email = lower(_email) and school_id = sid;
  if not found or p.password = '' then raise exception 'No such student'; end if;
  delete from auth.users where email = p.email or email = p.email2;
  perform _create_login(p.email, p.password);
  if p.email2 is not null then perform _create_login(p.email2, p.password); end if;
end $$;

-- Bootstrap: create the admin logins from admins.initial_password.
select public._create_login(email, initial_password) from public.admins where initial_password is not null and initial_password <> '';

select a.email, (a.initial_password is not null) as has_password, exists (select 1 from auth.users u where u.email = a.email) as login_exists
from public.admins a;
