// Emails the admin whenever a row is inserted into contact_messages (called by a Supabase database webhook).
// Secrets (supabase secrets set ...): RESEND_API_KEY, NOTIFY_TO (one or more addresses, comma-separated), WEBHOOK_SECRET, optional NOTIFY_FROM.
// Deploy with verify_jwt off: the webhook sends WEBHOOK_SECRET in the x-webhook-secret header instead.
const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

Deno.serve(async (req) => {
  const secret = Deno.env.get("WEBHOOK_SECRET");
  if (!secret || req.headers.get("x-webhook-secret") !== secret) return new Response("forbidden", { status: 403 });
  const { record: m } = await req.json();
  if (!m) return new Response("no record", { status: 400 });

  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${Deno.env.get("RESEND_API_KEY")}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from: Deno.env.get("NOTIFY_FROM") ?? "Ascendant <onboarding@resend.dev>",
      to: (Deno.env.get("NOTIFY_TO") ?? "").split(",").map((s) => s.trim()).filter(Boolean), // comma-separated list
      reply_to: m.email, // hitting reply goes straight to the sender
      subject: `Contact: ${m.topic ?? "other"} from ${m.name}`,
      html: `<p><b>${esc(m.name)}</b> (${esc(m.email)}) · ${esc(m.role ?? "-")}${m.org ? " · " + esc(m.org) : ""} · ${esc(m.topic ?? "-")}</p><p style="white-space:pre-wrap">${esc(m.message)}</p>`,
    }),
  });
  if (!res.ok) return new Response(await res.text(), { status: 502 });
  return new Response("ok");
});
