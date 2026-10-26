const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

const bin = (n, w = 8) => n.toString(2).padStart(w, "0");
const hx = (n, w = 2) => n.toString(16).toUpperCase().padStart(w, "0");
const grp4 = (s) => s.replace(/(.{4})(?=.)/g, "$1 ");
const clamp01 = (v) => Math.max(0, Math.min(1, v));
/* row of boxes: items [{t, c, v}] t text, c fill class, v opacity */
function boxRow(items, x0, y, w = 64, h = 52, gap = 10, o = {}) {
  let s = "";
  items.forEach((it, i) => {
    const x = x0 + i * (w + gap), v = it.v === undefined ? 1 : it.v;
    if (v <= 0) return;
    s += SV.rect(x, y, w, h, it.c || "f3", { rx: 8, ...op(v * (it.c ? 0.55 : 0.18)) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) });
    s += SV.text(x + w / 2, y + h / 2 + 8, it.t, "lbl bd", { "text-anchor": "middle", style: "font-size:" + (o.fs || 22) + "px;font-family:var(--mono)", ...op(v) });
    if (it.top !== undefined) s += SV.text(x + w / 2, y - 8, it.top, "sm", { "text-anchor": "middle", ...op(v) });
    if (it.bot !== undefined) s += SV.text(x + w / 2, y + h + 18, it.bot, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return s;
}

/* memory cell: address on the left, value in the box */
function memCell(x, y, addr, val, cls = "f3", v = 1, w = 150, h = 40) {
  return SV.rect(x, y, w, h, cls, { rx: 6, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 6, fill: "none", ...op(v) }) +
    SV.text(x + 10, y + h / 2 + 6, String(addr), "sm", { style: "font-family:var(--mono)", ...op(v) }) +
    SV.text(x + w - 12, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono);font-size:17px", ...op(v) });
}
function regBox(x, y, name, val, cls = "f2", v = 1, w = 120, h = 46) {
  return SV.rect(x, y, w, h, cls, { rx: 8, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) }) +
    SV.text(x + 10, y - 7, name, "sm", op(v)) + SV.text(x + w / 2, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:19px", ...op(v) });
}
/* a list of code lines; hl is the highlighted index (or -1) */
function codeList(x, y, lines, hl, v = 1, lh = 30, w = 230) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 4, i === hl ? "cell-warn" : "cell", { rx: 4, ...op(v) }) + SV.text(x + 10, y + i * lh + 18, l, "lbl", { style: "font-family:var(--mono);font-size:14px;white-space:pre", ...op(v) })).join("");
}

(function () {
  const pk = [["port 80 (web)", 1], ["port 4444 (unknown)", 0], ["port 443 (secure web)", 1]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "Internet", "lbl bd") + SV.rect(210, 30, 40, 120, "f3", { rx: 6 }) + SV.text(230, 95, "firewall", "sm", { "text-anchor": "middle", style: "transform-origin:230px 95px;transform:rotate(-90deg)" }) + SV.text(380, 20, "Computer", "lbl bd");
    pk.forEach(([n, ok], i) => { if (i <= k) o += SV.rect(30, 40 + i * 36, 160, 28, ok ? "f1" : "f2", { rx: 4 }) + SV.text(40, 59 + i * 36, n, "lbl", { style: "font-size:12px" }); if (i < k || (i === k && false)) {} }); pk.forEach(([n, ok], i) => { if (ok && i <= k) o += SV.rect(290, 40 + i * 36, 160, 28, "f1", { rx: 4 }) + SV.text(300, 59 + i * 36, n, "lbl", { style: "font-size:12px" }) + SV.path(`M250,${54 + i * 36} H290`, "ax"); if (!ok && i <= k) o += SV.text(260, 59 + i * 36, "✗", "lbl bd", { style: "fill:var(--bad)" }); });
    o += SV.text(20, 170, ["", "web traffic matches the allow rule: it passes", "an unknown port is not allowed: blocked", "secure web traffic matches the rules: it passes"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 480, h: 190, label: "Firewall", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["The firewall monitors incoming and outgoing packets.", "Port 80 matches the rules: <b>allowed</b>.", "Port 4444 is not allowed: <b>blocked</b>.", "Port 443 matches the rules: <b>allowed</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 120, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 60, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(10, "plain text", true) + B(160, "encrypt (key)", k >= 1) + B(310, "cipher text", k >= 2) + B(460, "decrypt (key)", k >= 3) + SV.path("M130,62 H160", "ax") + SV.path("M280,62 H310", "ax") + SV.path("M430,62 H460", "ax");
    o += SV.text(300, 125, ["HELLO", "", "KHOOR (interceptor sees this)", "HELLO again, only with the key"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 150, label: "Encryption", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["The message is plain text.", "It is encrypted using a key.", "Cipher text is sent: if intercepted it cannot be understood.", "The receiver decrypts it with the key."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, w, t, on) => SV.rect(x, y, w, 36, on ? "f3" : "cell", { rx: 6 }) + SV.text(x + w / 2, y + 23, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); let o = B(10, 20, 100, "message", true) + B(150, 20, 100, "hash → digest", k >= 1) + B(290, 20, 150, "encrypt: private key", k >= 2) + B(10, 90, 150, "decrypt: public key", k >= 3) + B(200, 90, 150, "hash message again", k >= 4) + B(390, 90, 100, "same digest?", k >= 5);
    if (k >= 1) o += SV.path("M110,38 H150", "ax"); if (k >= 2) o += SV.path("M250,38 H290", "ax"); if (k >= 4) o += SV.path("M160,108 H200", "ax"); if (k >= 5) o += SV.path("M350,108 H390", "ax"); o += SV.text(20, 160, k >= 5 ? "If the digests match, the message is authentic and unchanged" : "", "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 175, label: "Digital signature", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["The sender has a message.", "It is hashed to produce a <b>digest</b>.", "The digest is encrypted with the sender's <b>private key</b> (the signature).", "The receiver decrypts the signature with the sender's <b>public key</b>.", "The receiver hashes the received message.", "The two digests are <b>compared</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let len = 8, set = 62; const sets = { 10: "digits only", 26: "lower-case letters", 52: "upper and lower case", 62: "upper, lower and digits", 94: "all keyboard characters" };
  const paint = () => { const n = Math.pow(set, len); const f = (x) => x >= 1e15 ? (x / 1e15).toFixed(1) + " quadrillion" : x >= 1e12 ? (x / 1e12).toFixed(1) + " trillion" : x >= 1e9 ? (x / 1e9).toFixed(1) + " billion" : x >= 1e6 ? (x / 1e6).toFixed(1) + " million" : x.toLocaleString(); $("#pV").innerHTML = `A <b>${len}</b>-character password from a set of <b>${set}</b> characters (${sets[set]}) has <b>${f(n)}</b> possible combinations. Longer passwords and a bigger set of characters make guessing far harder.`; };
  Lib.slider($("#pS1"), { id: "p1", label: "Length ", min: 4, max: 16, value: len, fmt: (x) => x, onInput: (v) => { len = v; paint(); } });
  const sl = $("#pS2"); [10, 26, 52, 62, 94].forEach((k) => { const b = document.createElement("button"); b.textContent = k + " chars"; b.onclick = () => { set = k; sl.querySelectorAll("button").forEach((x) => x.className = x === b ? "on" : ""); paint(); }; if (k === set) b.className = "on"; sl.appendChild(b); }); paint();
})();
(function () {
  let shift = 3; const msg = "SECURITY"; const paint = () => { const enc = msg.split("").map((c) => String.fromCharCode(((c.charCodeAt(0) - 65 + shift) % 26) + 65)).join(""); $("#eV").innerHTML = `Plain text <b>${msg}</b>, key (shift) <b>${shift}</b> → cipher text <b>${enc}</b>. Without the key the cipher text is hard to understand; with it, shifting back gives <b>${msg}</b>. (A Caesar cipher is easy to break: real encryption uses very long keys.)`; };
  Lib.slider($("#eS"), { id: "e1", label: "Key (shift) ", min: 1, max: 25, value: shift, fmt: (x) => x, onInput: (v) => { shift = v; paint(); } }); paint();
})();
btnTable("mB", "mO", [
  ["Firewall", "Data security", "Blocks packets that fail the rules"],
  ["Password", "Data security", "Proves identity"],
  ["Double entry", "Data integrity", "Checks data is the same as the original"],
  ["Presence check", "Data integrity", "Validation"],
  ["Access rights", "Data security", "Limits what each user can do"],
  ["Back-up", "Data security", "Recovery of lost data"]
], ["Measure", "Protects", "Why"]);
Lib.classify($("#cl1"), { prompt: "Security, privacy or integrity?", buckets: [{"label": "Security"}, {"label": "Privacy"}, {"label": "Integrity"}], items: [{"text": "Protecting data from loss or corruption", "b": 0}, {"text": "Only authorised people can see the data", "b": 1}, {"text": "The data is accurate and consistent", "b": 2}, {"text": "Making sure data can be recovered", "b": 0}, {"text": "Preventing disclosure to unauthorised people", "b": 1}, {"text": "The data is up to date and complete", "b": 2}], done: "Security: loss. Privacy: access. Integrity: accuracy." });
Lib.classify($("#cl2"), { prompt: "Is it a security measure or an integrity measure?", buckets: [{"label": "Data security"}, {"label": "Data integrity"}], items: [{"text": "Firewall", "b": 0}, {"text": "Double entry", "b": 1}, {"text": "Access rights", "b": 0}, {"text": "Presence check", "b": 1}, {"text": "Password", "b": 0}, {"text": "Visual check", "b": 1}], done: "Firewall, access rights and passwords protect security; checks protect integrity." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Firewall", "Checks packets against rules and blocks those that fail"], ["Encryption", "Scrambles data with a key so it cannot be understood if intercepted"], ["Anti-malware", "Scans files against a database of known malware"], ["Access rights", "Limits which files each user can open or change"], ["Back-up", "Regular copies so lost data can be recovered"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the digital signature steps in order.", items: ["The sender hashes the message to produce a digest", "The digest is encrypted with the sender's private key", "The message and signature are sent", "The receiver decrypts the signature with the sender's public key", "The receiver hashes the message and compares the digests"], done: "Hash, encrypt, send, decrypt, compare." });
Lib.calc($("#c1"), { qs: [
  {"q": "A password uses 26 lower-case letters and is 4 characters long. How many possible passwords?", "a": 456976, "unit": "", "tol": 0.5, "hint": "26^4.", "sol": "<b>456976</b>."},
  {"q": "Using 62 characters (upper, lower, digits) and 6 characters, how many millions of passwords (nearest million)?", "a": 56800, "unit": "million", "tol": 100, "hint": "62^6 ÷ 10^6 ≈ 56 800.", "sol": "about <b>56 800</b> million."},
  {"q": "A Caesar cipher shifts each letter by 3. What does D become? (Give its number: A=1, B=2 ...)", "a": 7, "unit": "", "tol": 0.01, "hint": "D is 4; 4 + 3.", "sol": "<b>7</b> (G)."},
  {"q": "A firewall allows 3 ports and blocks the other 65 533. How many ports in total?", "a": 65536, "unit": "", "tol": 0.5, "hint": "3 + 65 533.", "sol": "<b>65536</b>."},
  {"q": "A back-up is taken every night. The data is lost at 3 pm on Thursday; the last back-up was Wednesday night. How many hours of work could be lost if work started at 9 am?", "a": 6, "unit": "h", "tol": 0.01, "hint": "9 am to 3 pm.", "sol": "<b>6</b> hours."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Data privacy means:", opts: ["Only authorised people can access it", "It is accurate", "It is backed up", "It is compressed"], a: 0, why: "Authorised access." },
  { q: "Data integrity is:", opts: ["Accuracy and consistency", "Encryption", "A firewall", "Copying"], a: 0, why: "Accuracy." },
  { q: "Encryption produces:", opts: ["Cipher text", "A digest only", "A password", "A virus"], a: 0, why: "Cipher text." },
  { q: "A digital signature uses the sender's:", opts: ["Private key", "Public key to sign", "Password", "IP address"], a: 0, why: "Private key encrypts the digest." },
  { q: "A firewall:", opts: ["Checks packets against rules", "Creates back-ups", "Fixes typing errors", "Compresses files"], a: 0, why: "Rules." },
  { q: "Which protects integrity?", opts: ["Validation", "Firewall", "Password", "Encryption"], a: 0, why: "Validation." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Security", "Protect from loss, corruption, unauthorised access."],
  ["Privacy", "Only authorised people can see the data."],
  ["Integrity", "Accurate, complete, consistent, up to date."],
  ["Firewall", "Rules on packets; blocks those that fail."],
  ["Anti-malware", "Scans against known malware."],
  ["Encryption", "Cipher text; needs the key."],
  ["Digital signature", "Hash, encrypt digest with private key."],
  ["Back-up", "Recover lost data."],
] });
