-- Emails the admin on each new contact message via the contact-notify edge function.
-- Replace __WEBHOOK_SECRET__ with the function's WEBHOOK_SECRET before running; never commit the real value.
create extension if not exists pg_net with schema extensions;

create or replace function public.notify_contact() returns trigger
language plpgsql security definer set search_path = public, extensions as $$
begin
  perform net.http_post(
    url := 'https://ejywlpscqvchwifnlevx.supabase.co/functions/v1/contact-notify',
    headers := jsonb_build_object('Content-Type', 'application/json', 'x-webhook-secret', '__WEBHOOK_SECRET__'),
    body := jsonb_build_object('record', to_jsonb(new))
  );
  return new;
end $$;

drop trigger if exists contact_notify on public.contact_messages;
create trigger contact_notify after insert on public.contact_messages
  for each row execute function public.notify_contact();
