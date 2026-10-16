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

  async function decrypt(keyB64) {
    const buf = new Uint8Array(await (await fetch("payload.bin", { cache: "no-cache" })).arrayBuffer());
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

  async function open(keyB64) {
    const html = assemble(await decrypt(keyB64));
    document.open();
    document.write(html);
    document.close();
  }
  window.Gate = { open, decrypt, assemble };

  async function run() {
    if (!S || !S.configured) return deny("Lessons are not available", "The account service is not connected.", "Go to Profile");
    const me = await S.whoami();
    if (!me) {
      try { sessionStorage.setItem("site.next", location.href); } catch (e) {}
      return deny("Sign in to open this lesson", "Lessons are for registered students. Sign in with the account your teacher set up.", "Sign in");
    }
    const { data, error } = await S.sb.rpc("artifact_key", { _slug: slug });
    if (error) return deny("Could not open this lesson", "Please check your connection and try again.", "Go to Profile");
    if (!data) return deny("You are not registered for this subject", "Ask for it from your profile page. Your teacher will approve it.", "Go to Profile");
    if (msg) msg.textContent = "Opening lesson…";
    await open(data);
  }
  if (!el.hasAttribute("data-manual")) run().catch(() => deny("Could not open this lesson", "Please try again.", "Go to Profile"));
})();
