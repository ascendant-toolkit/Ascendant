// Mints a Paddle customer portal session for the signed-in user and returns its URL.
// The customer id is resolved server-side from the user's own payments, never taken from the request.
// Secrets: PADDLE_API_KEY (needs Customers read, Customer portal sessions write, Subscriptions read), PADDLE_ENV.
// Deploy with verify_jwt on: the site sends the signed-in user's JWT.
import { createClient } from "npm:@supabase/supabase-js@2";

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (body: unknown, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { ...cors, "Content-Type": "application/json" } });

const db = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, { auth: { persistSession: false } });
const anon = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_ANON_KEY")!, { auth: { persistSession: false } });

const base = () => (Deno.env.get("PADDLE_ENV") === "live" ? "https://api.paddle.com" : "https://sandbox-api.paddle.com");
const keyShape = () => {
  const k = Deno.env.get("PADDLE_API_KEY") ?? "";
  return `len=${k.length} prefix_ok=${k.startsWith("pdl_live_apikey_")} ws=${/\s/.test(k)} quote=${/['"]/.test(k)} env=${Deno.env.get("PADDLE_ENV")}`;
};
const paddle = (path: string, init: RequestInit = {}) =>
  fetch(`${base()}${path}`, {
    ...init,
    headers: { Authorization: `Bearer ${Deno.env.get("PADDLE_API_KEY")}`, "Content-Type": "application/json" },
  });

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return json({ error: "method" }, 405);

  const token = (req.headers.get("Authorization") ?? "").replace(/^Bearer\s+/i, "");
  const { data: { user } } = await anon.auth.getUser(token);
  if (!user?.email) return json({ error: "auth" }, 401);
  const email = user.email.trim().toLowerCase();

  const { data: prof } = await db.from("profiles").select("email,email2").or(`email.eq.${email},email2.eq.${email}`).limit(1).maybeSingle();
  const emails = [...new Set([email, prof?.email, prof?.email2].filter(Boolean))] as string[];
  const { data: pay } = await db.from("payments").select("customer_id").in("email", emails)
    .not("customer_id", "is", null).order("created_at", { ascending: false }).limit(1).maybeSingle();
  if (!pay?.customer_id) return json({ error: "no_billing" }, 404);

  try {
    // Subscription ids unlock the cancel and update deep links; the general overview works without them.
    let ids: string[] = [];
    const sr = await paddle(`/subscriptions?customer_id=${pay.customer_id}&status=active,trialing,past_due,paused`);
    if (sr.ok) ids = ((await sr.json()).data ?? []).map((s: any) => s.id);
    else console.log("subscription list skipped", sr.status, keyShape(), (await sr.text()).slice(0, 300));

    const r = await paddle(`/customers/${pay.customer_id}/portal-sessions`, {
      method: "POST",
      body: JSON.stringify(ids.length ? { subscription_ids: ids } : {}),
    });
    if (!r.ok) throw new Error(`portal session failed: ${r.status} ${(await r.text()).slice(0, 300)}`);
    const { data } = await r.json();
    return json({ url: data.urls.general.overview });
  } catch (e) {
    console.error(e);
    return json({ error: "portal" }, 502);
  }
});
