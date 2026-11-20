// Opens a locked lesson. The lesson is shipped as an encrypted file (payload.bin); the key is only handed
// out by the database to a signed-in member whose subjects include this lesson's course (artifact_key()).
(function () {
  const el = document.currentScript;
  const slug = el.dataset.slug;
  const S = window.Site;
  const msg = document.getElementById("gate-msg");

  function deny(title, text, linkText, href) {
    document.body.innerHTML = `<div style="max-width:460px;margin:12vh auto;padding:24px;font:16px/1.5 -apple-system,Segoe UI,sans-serif;color:#16202a;background:#fff;border:1px solid #ddd8cc;border-radius:12px">
      <h2 style="margin:0 0 8px;font-family:Georgia,serif">${title}</h2><p>${text}</p>
      <p><a href="${href || (S && S.profileUrl) || "../../profile/"}" style="color:#2b5d7c;font-weight:700">${linkText}</a></p></div>`;
    document.body.style.cssText = "background:#f6f4ef";
  }

  const b64 = (s) => Uint8Array.from(atob(s), (c) => c.charCodeAt(0));

  async function decrypt(keyB64, file) {
    const res = await fetch(file || "payload.bin", { cache: "no-cache" });
    if (!res.ok) throw new Error("missing " + file);
    const buf = new Uint8Array(await res.arrayBuffer());
    const key = await crypto.subtle.importKey("raw", b64(keyB64), "AES-GCM", false, ["decrypt"]);
    const gz = await crypto.subtle.decrypt({ name: "AES-GCM", iv: buf.slice(0, 12) }, key, buf.slice(12));
    const text = await new Response(new Blob([gz]).stream().pipeThrough(new DecompressionStream("gzip"))).text();
    return JSON.parse(text);
  }

  // Bundled sibling files (iframe pages, linked pages, css) become blob URLs or inline styles.
  function assemble(p) {
    const root = new URL("../../", location.href).href, shell = location.origin + location.pathname;
    const files = p.files || {}, names = Object.keys(files).sort((a, b) => b.length - a.length);
    const swap = (t, from, to) => t.split('"' + from + '"').join('"' + to + '"').split("'" + from + "'").join("'" + to + "'");
    const css = (t) => names.filter((n) => n.endsWith(".css")).reduce((acc, n) =>
      acc.replace(new RegExp('<link[^>]*href=["\']' + n.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + '["\'][^>]*>', "g"), "<style>" + files[n] + "</style>"), t);
    const fix = (t) => css(swap(t.split('"../../').join('"' + root).split("'../../").join("'" + root), "index.html", shell));
    const urls = {};
    names.filter((n) => !n.endsWith(".css")).forEach((n) => {
      urls[n] = URL.createObjectURL(new Blob([fix(files[n])], { type: "text/html" }));
    });
    let html = css(p.index);
    Object.keys(urls).forEach((n) => { html = swap(html, n, urls[n]); });
    return html;
  }

  // Practise, Exam questions and Tips & keywords ship in a second payload under a Full-only key (artifact_key(slug + ":full")).
  // Full accounts get the panels and the script lines that fill them spliced back in; everyone else gets an upgrade card.
  const lockCard = (root) => `<div class="card" style="text-align:center;padding:28px 20px"><h2 style="margin:0 0 8px">Part of the Full plan</h2>
    <p style="margin:0 0 14px">Practise, Exam questions and Tips &amp; keywords are included with Full. Multiple choice is marked instantly and written answers are self-marked against the mark scheme.</p>
    <p style="margin:0"><a href="${root}pricing/" style="font-weight:700">See the plans</a></p></div>`;
  async function withFull(p) {
    let full = null;
    try {
      const { data } = await S.sb.rpc("artifact_key", { _slug: slug + ":full" });
      if (data) full = await decrypt(data, "payload.full.bin");
    } catch (e) { full = null; }
    const root = new URL("../../", location.href).href, swap = (s, a, b) => s.split(a).join(b);
    const names = full ? Object.keys(full.panels) : (p.index.match(/data-lock="[^"]+"/g) || []).map((s) => s.slice(11, -1));
    names.forEach((n) => { p.index = swap(p.index, `<div class="fulllock" data-lock="${n}"></div>`, full ? full.panels[n] : lockCard(root)); });
    p.index = swap(p.index, "/*@@FULL@@*/", full ? full.js : "");
    if (!full) p.index = p.index.replace(new RegExp('(data-p="(?:' + names.join("|") + ')"[^>]*>)([^<]*)', "g"), '$1$2 <span style="font-size:.7em;opacity:.7;margin-left:.3em">Full</span>');
    return p;
  }

  async function open(keyB64) {
    let p = await decrypt(keyB64);
    if (el.dataset.split) p = await withFull(p);
    const html = assemble(p);
    document.open();
    document.write(html);
    document.close();
  }
  window.Gate = { open, decrypt, assemble };

  // artifact_key() only says yes or no, so work out the reason here from whoami(), mirroring its subject and tier checks.
  const TIERS = ["free", "basic", "full", "vip"], NAMES = { free: "Free", basic: "Basic", full: "Full", vip: "VIP" };
  function explain(me) {
    const courses = (el.dataset.courses || "").split(",").filter(Boolean), need = el.dataset.tier || "full";
    if (!courses.some((c) => (me.subjects || []).includes(c)))
      return deny("You are not registered for this subject", "Ask your teacher to add it, or see the plans.", "Go to Profile");
    const ents = (me.entitlements || []).filter((e) => e.product === "school-all" || courses.includes(e.product));
    // No matching entitlement counts as full, as in artifact_key().
    const held = ents.length ? Math.max(...ents.map((e) => TIERS.indexOf(e.tier))) : TIERS.indexOf("full");
    if (held < TIERS.indexOf(need))
      return deny(`Upgrade to ${NAMES[need]} to open this lesson`,
        `This lesson is part of the ${NAMES[need]} plan. Your access to this subject is ${NAMES[TIERS[held]] || "limited"}.`, "See your plan");
    deny("This lesson is not ready yet", "It was added recently and is still being set up. Please try again later.", "Go to Profile");
  }

  async function run() {
    if (!S || !S.configured) return deny("Lessons are not available", "The account service is not connected.", "Go to Profile");
    const me = await S.whoami();
    if (!me) {
      try { sessionStorage.setItem("site.next", location.href); } catch (e) {}
      return deny("Sign in to open this lesson", "Lessons are for registered students. Sign in with the account your teacher set up.", "Sign in");
    }
    const { data, error } = await S.sb.rpc("artifact_key", { _slug: slug });
    if (error) return deny("Could not open this lesson", "Please check your connection and try again.", "Go to Profile");
    if (!data) return explain(me);
    if (msg) msg.textContent = "Opening lesson…";
    await open(data);
  }
  if (!el.hasAttribute("data-manual")) run().catch(() => deny("Could not open this lesson", "Please try again.", "Go to Profile"));
})();
