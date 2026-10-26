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

function boxes(items, ox, y) { let o = ""; items.forEach(([t, cls, w], i) => { o += SV.rect(ox, y + i * 54, w || 190, 42, cls || "cell", { rx: 8 }) + SV.text(ox + (w || 190) / 2, y + i * 54 + 27, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); }); return o; }
(function () {
  const st = [["Message: PAY 50", "cell-ok"], ["Hash algorithm", "f4"], ["Message digest: 1158", "cell-ok"], ["Encrypt digest with sender's PRIVATE key", "f2"], ["Digital signature", "cell-ok"]];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; st.slice(0, k + 1).forEach(([t, c], i) => { o += SV.rect(30, 14 + i * 52, 300, 42, i === k ? "cell-warn" : c, { rx: 8 }) + SV.text(180, 41 + i * 52, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); if (i) o += SV.path("M180," + (14 + i * 52) + " V" + (6 + i * 52 + 8), "ax"); });
    if (k >= 4) o += SV.text(360, 250, "message + signature are sent", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 600, h: 280, label: "Producing a signature", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: [{ cap: "The sender has a message to sign.", s: { i: 0 } }, { cap: "The message is put through the agreed <b>hashing algorithm</b>...", s: { i: 1 } }, { cap: "...which produces a short <b>message digest</b>. Changing the message would change the digest.", s: { i: 2 } }, { cap: "The digest is <b>encrypted with the sender's private key</b>.", s: { i: 3 } }, { cap: "The result is the <b>digital signature</b>. It is sent with the message.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(30, 20, "received", "sm") + SV.rect(30, 28, 150, 40, "cell", { rx: 8 }) + SV.text(105, 54, "message", "lbl bd", { "text-anchor": "middle" }) + SV.rect(230, 28, 170, 40, "cell", { rx: 8 }) + SV.text(315, 54, "digital signature", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.path("M315,68 V92", "ax") + SV.rect(215, 92, 200, 40, "f2", { rx: 8 }) + SV.text(315, 118, "decrypt with sender's PUBLIC key", "lbl", { "text-anchor": "middle", style: "font-size:12px" }) + SV.path("M315,132 V150", "ax") + SV.rect(240, 150, 150, 36, "cell-ok", { rx: 8 }) + SV.text(315, 173, "digest A", "lbl bd", { "text-anchor": "middle" });
    if (k >= 2) o += SV.path("M105,68 V92", "ax") + SV.rect(30, 92, 150, 40, "f4", { rx: 8 }) + SV.text(105, 118, "hash it", "lbl", { "text-anchor": "middle" }) + SV.path("M105,132 V150", "ax") + SV.rect(30, 150, 150, 36, "cell-ok", { rx: 8 }) + SV.text(105, 173, "digest B", "lbl bd", { "text-anchor": "middle" });
    if (k >= 3) o += SV.text(210, 224, "compare digest A and digest B", "lbl bd", { "text-anchor": "middle" }); if (k >= 4) o += SV.text(210, 252, "same: not altered, from the sender  |  different: altered", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 440, h: 270, label: "Checking a signature", base: { i: 0 }, draw, tween: 120, dwell: 2800, steps: [{ cap: "The receiver has the message and the digital signature.", s: { i: 0 } }, { cap: "The signature is decrypted with the sender's <b>public key</b> (from the certificate) to recover digest A.", s: { i: 1 } }, { cap: "The receiver hashes the message they received to make digest B.", s: { i: 2 } }, { cap: "The two digests are <b>compared</b>.", s: { i: 3 } }, { cap: "If they match the message has not been altered and the sender is verified; if not, it has been altered.", s: { i: 4 } }] });
})();
(function () {
  const L = ["Organisation generates a public and private key pair", "Organisation requests a certificate from a CA", "Organisation sends proof of identity and its public key", "CA verifies the organisation's identity", "CA issues the certificate (with the public key)"];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; L.forEach((t, i) => (o += SV.rect(20, 12 + i * 46, 420, 38, i === k ? "cell-warn" : i < k ? "cell-ok" : "cell", { rx: 8 }) + SV.text(34, 36 + i * 46, t, "lbl", { style: "font-size:13px" }))); return o; };
  Lib.stepper($("#stC"), { w: 460, h: 250, label: "Acquiring a certificate", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: L.map((t, i) => ({ cap: ["The organisation first makes its own key pair.", "It asks a trusted <b>Certificate Authority</b> for a certificate.", "It sends the information the CA needs to prove who it is, with its public key.", "The CA <b>checks</b> that the organisation is who it says it is.", "The CA <b>issues the certificate</b>, signed by the CA so others can trust it."][i], s: { i } })) });
})();

(function () {
  const N = 3233, E = 17, D = 2753; const h = (s) => [...s].reduce((a, c, i) => a + c.charCodeAt(0) * (i + 1), 0) % 3000;
  const pw = (b, e) => { let r = 1n, x = BigInt(b) % BigInt(N), p = BigInt(e); while (p > 0n) { if (p & 1n) r = (r * x) % BigInt(N); x = (x * x) % BigInt(N); p >>= 1n; } return Number(r); };
  const SIGNED = "PAY 50", sig = pw(h(SIGNED), D), inp = $("#gI");
  const paint = () => { const m = inp.value, d = pw(sig, E), hh = h(m), ok = d === hh;
    $("#gO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Step</th><th>Value</th></tr>' + `<tr><td>Signature sent with the message (digest ${h(SIGNED)} encrypted with the private key)</td><td>${sig}</td></tr><tr><td>Receiver decrypts it with the public key: digest A</td><td>${d}</td></tr><tr><td>Receiver hashes the message "${m.replace(/</g, "&lt;")}": digest B</td><td>${hh}</td></tr></table></div><div class="verdict">${ok ? "<b style=\"color:var(--good)\">Digests match</b>: the message is unaltered and was signed with the matching private key." : "<b style=\"color:var(--bad)\">Digests differ</b>: the message has been altered (or was not signed by this key)."}</div>`; };
  inp.oninput = paint; paint();
})();
btnTable("cB", "cO", [
  ["Subject (holder's name)", "The person, website or organisation the certificate is for", "Identifies who it belongs to"],
  ["Public key", "The holder's public key", "Used to encrypt messages to the holder or check their signature"],
  ["Issuer", "The Certificate Authority that issued it", "Who vouches for the holder"],
  ["Validity dates", "Start and expiry dates", "A certificate is only trusted while valid"],
  ["Serial and version number", "Unique number and format version", "Identify this certificate"],
  ["CA's digital signature", "Signature of the CA on the certificate", "Proves the certificate is genuine and unchanged"]
], ["Item", "What it is", "Why it matters"]);
Lib.classify($("#cl1"), { prompt: "Is it about a certificate or a signature?", buckets: [{"label": "Digital certificate"}, {"label": "Digital signature"}], items: [{"text": "Issued by a Certificate Authority", "b": 0}, {"text": "An encrypted message digest", "b": 1}, {"text": "Contains the holder's public key", "b": 0}, {"text": "Shows a message has not been altered", "b": 1}, {"text": "Has an expiry date", "b": 0}, {"text": "Made with the sender's private key", "b": 1}], done: "Certificate: identity and public key. Signature: encrypted digest." });
Lib.classify($("#cl2"), { prompt: "Which key is used?", buckets: [{"label": "Sender's private key"}, {"label": "Sender's public key"}, {"label": "Receiver's private key"}], items: [{"text": "Encrypting the message digest to make the signature", "b": 0}, {"text": "Decrypting the signature to recover the digest", "b": 1}, {"text": "Decrypting a message that was encrypted for the receiver", "b": 2}, {"text": "Provided to the receiver by the certificate", "b": 1}, {"text": "Never sent to anybody", "b": 0}, {"text": "Used to check who signed", "b": 1}], done: "Sign with the private key; check with the public key." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Digital certificate", "Electronic document proving identity and holding a public key"], ["Certificate Authority", "Trusted organisation that issues certificates"], ["Message digest", "Fixed-size result of hashing a message"], ["Digital signature", "The message digest encrypted with the sender's private key"], ["Non-repudiation", "The sender cannot deny sending the message"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of checking a digital signature in order.", items: ["Decrypt the signature with the sender's public key to get digest A", "Hash the received message to get digest B", "Compare digest A and digest B", "Decide: same means unaltered, different means altered"], done: "Decrypt, hash, compare, decide." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many digests are compared when a signature is checked?", "a": 2, "unit": "", "tol": 0.01, "hint": "A and B.", "sol": "<b>2</b>."},
  {"q": "The two digests are the same. Has the message been altered? Enter 0 for no, 1 for yes.", "a": 0, "unit": "", "tol": 0.01, "hint": "Same digests: not altered.", "sol": "<b>0</b>."},
  {"q": "How many items commonly in a certificate did the mark scheme list in the Learn tab (name, public key, serial number, version number, dates, issuer, CA signature)?", "a": 7, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>7</b>."},
  {"q": "How many keys does the signer use to make the signature?", "a": 1, "unit": "", "tol": 0.01, "hint": "Their private key.", "sol": "<b>1</b>."},
  {"q": "A signature is made from a message digest. How many keys does the receiver need to check it (the sender's public key)?", "a": 1, "unit": "", "tol": 0.01, "hint": "One key.", "sol": "<b>1</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A digital certificate is issued by:", opts: ["The receiver", "A Certificate Authority", "The sender", "A printer"], a: 1, why: "A CA." },
  { q: "What is encrypted to make a digital signature?", opts: ["The whole message", "The message digest", "The certificate", "The public key"], a: 1, why: "The digest." },
  { q: "The signature is checked with the:", opts: ["Sender's public key", "Sender's private key", "Receiver's public key", "Nothing"], a: 0, why: "Sender's public key." },
  { q: "Different digests mean:", opts: ["The message is unaltered", "The message has been altered", "The key is long", "Nothing"], a: 1, why: "Altered." },
  { q: "A certificate proves:", opts: ["Identity", "Speed", "Colour", "Size"], a: 0, why: "Identity." },
  { q: "A hash function produces:", opts: ["A key pair", "A fixed-size digest", "A certificate", "A network"], a: 1, why: "A digest." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Digital certificate", "Document from a CA proving identity; holds the public key."],
  ["CA", "Verifies identity and issues certificates."],
  ["Message digest", "Hash of the message."],
  ["Digital signature", "Digest encrypted with the sender's private key."],
  ["Checking", "Decrypt with public key, hash, compare digests."],
  ["Why a certificate", "Provides and validates the public key; non-repudiation."],
  ["Acquire", "Request, details and public key, CA verifies, issues."],
  ["Contents", "Name, public key, serial, dates, issuer, CA signature."],
] });
