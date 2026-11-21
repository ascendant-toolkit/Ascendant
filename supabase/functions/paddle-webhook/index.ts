// Paddle Billing webhook: turns a paid transaction into an entitlement, and a full refund into a revoke.
// Secrets (supabase secrets set ...): PADDLE_WEBHOOK_SECRET, PADDLE_API_KEY, PADDLE_ENV (sandbox|live), SITE_URL.
// SUPABASE_URL, SUPABASE_ANON_KEY and SUPABASE_SERVICE_ROLE_KEY are provided by the platform.
// Deploy with verify_jwt off: Paddle cannot send a Supabase JWT, the signature check below is the authentication.
import { createClient } from "npm:@supabase/supabase-js@2";

const GRACE_MS = 3 * 24 * 3600 * 1000; // covers renewal webhooks arriving a little after the period ends
const RANK: Record<string, number> = { free: 0, basic: 1, full: 2, vip: 3 };

const db = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, {
  auth: { persistSession: false },
});
const anon = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_ANON_KEY")!, {
  auth: { persistSession: false },
});

async function verify(raw: string, header: string | null): Promise<boolean> {
  const secret = Deno.env.get("PADDLE_WEBHOOK_SECRET");
  if (!secret || !header) return false;
  const parts = Object.fromEntries(header.split(";").map((p) => p.split("=") as [string, string]));
  const ts = parts.ts, h1 = parts.h1;
  if (!ts || !h1 || Math.abs(Date.now() / 1000 - Number(ts)) > 300) return false;
  const key = await crypto.subtle.importKey("raw", new TextEncoder().encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const sig = new Uint8Array(await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(`${ts}:${raw}`)));
  const want = Array.from(sig, (b) => b.toString(16).padStart(2, "0")).join("");
  if (want.length !== h1.length) return false;
  let diff = 0; // constant-time compare
  for (let i = 0; i < want.length; i++) diff |= want.charCodeAt(i) ^ h1.charCodeAt(i);
  return diff === 0;
}

async function paddleCustomer(id: string): Promise<{ email: string; name: string | null }> {
  const base = Deno.env.get("PADDLE_ENV") === "live" ? "https://api.paddle.com" : "https://sandbox-api.paddle.com";
  const r = await fetch(`${base}/customers/${id}`, { headers: { Authorization: `Bearer ${Deno.env.get("PADDLE_API_KEY")}` } });
  if (!r.ok) throw new Error(`Paddle customer lookup failed: ${r.status}`);
  const { data } = await r.json();
  return { email: String(data.email).trim().toLowerCase(), name: data.name ?? null };
}

// Returns the roster email to attach the entitlement to; creates the login + profile for a brand-new buyer.
async function ensureAccount(email: string, name: string | null): Promise<string> {
  const { data: p } = await db.from("profiles").select("email").or(`email.eq.${email},email2.eq.${email}`).limit(1).maybeSingle();
  if (p) return p.email;
  // The database's gate_signup trigger only lets a login be created when its password matches a roster profile, so the
  // profile goes in first with a throwaway password, the login is created with it, then the password is cleared.
  const tmp = crypto.randomUUID() + crypto.randomUUID();
  const { error: pe } = await db.from("profiles").insert({ email, name: name || email.split("@")[0], subjects: [], password: tmp });
  if (pe) throw pe;
  const { error: ce } = await db.auth.admin.createUser({ email, password: tmp, email_confirm: true });
  if (ce && !/already|registered|exists/i.test(ce.message)) {
    await db.from("profiles").delete().eq("email", email); // roll back so a retry starts clean
    throw ce;
  }
  await db.from("profiles").update({ password: "" }).eq("email", email);
  // New buyers set their own password through the normal reset flow.
  const site = Deno.env.get("SITE_URL") ?? "https://ascendant.academy";
  await anon.auth.resetPasswordForEmail(email, { redirectTo: `${site}/profile/` });
  return email;
}

async function fulfil(txn: any) {
  const items: any[] = txn.items ?? [];
  const ids = items.map((i) => i.price?.id ?? i.price_id).filter(Boolean);
  // Independent lookups run together: Paddle gives up on a delivery after about 5 seconds.
  const [{ data: prices }, cust, { data: prior }] = await Promise.all([
    db.from("paddle_prices").select("*").in("price_id", ids),
    paddleCustomer(txn.customer_id),
    db.from("payments").select("status").eq("txn_id", txn.id).maybeSingle(),
  ]);
  console.log("customer ok");
  const amount = txn.details?.totals?.total, currency = txn.currency_code;
  const base = { txn_id: txn.id, customer_id: txn.customer_id, amount, currency };

  const known = (prices ?? []).filter((p) => p.kind === "student" && p.product);
  const hasTeacher = (prices ?? []).some((p) => p.kind === "teacher");
  if (!known.length || hasTeacher || known.length < ids.length) {
    // Teacher plan or a price we do not recognise: record it for hand fulfilment rather than guess.
    await db.from("payments").upsert({ ...base, email: cust.email, price_id: ids.join(","), status: "needs_setup",
      note: hasTeacher ? "Teacher plan: create the school-of-one in the admin Schools tab" : "Unrecognised price id" }, { onConflict: "txn_id", ignoreDuplicates: true });
    if (!known.length) return;
  }

  if (prior?.status === "refunded") return; // a late retry must not undo a refund

  const email = await ensureAccount(cust.email, cust.name);
  console.log("account ok");
  const ends = txn.billing_period?.ends_at ? new Date(txn.billing_period.ends_at).getTime() : Date.now() + 31 * 24 * 3600 * 1000;
  const expires = new Date(ends + GRACE_MS).toISOString();

  for (const p of known) {
    const { data: cur } = await db.from("entitlements").select("*").eq("email", email).eq("product", p.product).maybeSingle();
    const active = cur && (!cur.expires_at || new Date(cur.expires_at) > new Date());
    // Never downgrade a manual or school grant of the same or higher tier.
    if (active && cur.source !== "payment" && RANK[cur.tier] >= RANK[p.tier]) continue;
    const [{ error }, { error: perr }] = await Promise.all([
      db.from("entitlements").upsert({
        email, product: p.product, source: "payment", plan: p.period === "y" ? "annual" : "monthly",
        tier: p.tier, starts_at: cur?.source === "payment" && active ? cur.starts_at : new Date().toISOString(),
        expires_at: expires, note: `Paddle ${txn.id}`,
      }, { onConflict: "email,product" }),
      db.from("payments").upsert({ ...base, email, price_id: p.price_id, product: p.product, tier: p.tier, status: "granted" },
        { onConflict: "txn_id" }),
    ]);
    if (error) throw error;
    if (perr) throw perr;
  }
}

async function refund(adj: any) {
  if (adj.action !== "refund" || adj.status !== "approved") return;
  // Paddle can label a refund of the whole amount "partial" at adjustment level when it was raised per item, so also
  // accept an adjustment whose items are all full.
  const items: any[] = adj.items ?? [];
  if (adj.type !== "full" && !(items.length && items.every((i) => i.type === "full"))) return;
  const { data: pay } = await db.from("payments").select("*").eq("txn_id", adj.transaction_id).maybeSingle();
  if (!pay) return;
  await db.from("payments").update({ status: "refunded" }).eq("txn_id", pay.txn_id);
  if (pay.product) {
    await db.from("entitlements").update({ expires_at: new Date().toISOString() })
      .eq("email", pay.email).eq("product", pay.product).eq("source", "payment");
  }
}

Deno.serve(async (req) => {
  if (req.method !== "POST") return new Response("Method not allowed", { status: 405 });
  const raw = await req.text();
  if (!(await verify(raw, req.headers.get("paddle-signature")))) return new Response("Bad signature", { status: 401 });
  const t0 = Date.now();
  try {
    const ev = JSON.parse(raw);
    console.log("webhook", ev.event_type, ev.data?.id);
    if (ev.event_type === "transaction.completed") await fulfil(ev.data);
    else if (ev.event_type === "adjustment.updated") await refund(ev.data);
    console.log("done", ev.event_type, `${Date.now() - t0}ms`);
    return new Response("ok");
  } catch (e) {
    console.error(e);
    return new Response("error", { status: 500 }); // Paddle retries on non-2xx
  }
});
