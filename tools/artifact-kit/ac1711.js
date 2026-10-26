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

function msgDraw(o) { // o: {left, right, mid, midNote, keyL, keyR, keyNote}
  let s = SV.rect(20, 40, 140, 70, "cell", { rx: 10 }) + SV.text(90, 66, o.left[0], "lbl bd", { "text-anchor": "middle" }) + SV.text(90, 92, o.left[1], "lbl", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:13px" });
  s += SV.rect(480, 40, 140, 70, "cell", { rx: 10 }) + SV.text(550, 66, o.right[0], "lbl bd", { "text-anchor": "middle" }) + SV.text(550, 92, o.right[1], "lbl", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:13px" });
  s += SV.path("M160,75 H480", "ax", { style: "stroke-dasharray:6 5" }); if (o.mid) s += SV.rect(250, 55, 140, 40, "f2", { rx: 6 }) + SV.text(320, 80, o.mid, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:14px" });
  if (o.keyL) s += SV.text(10, 140, o.keyL, "sm", { "text-anchor": "start", style: "fill:var(--accent);font-size:12px" }); if (o.keyR) s += SV.text(630, 140, o.keyR, "sm", { "text-anchor": "end", style: "fill:var(--accent);font-size:12px" }); if (o.note) s += SV.text(320, 170, o.note, "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return s; }
(function () {
  const S = [{ left: ["Sender", "HELLO"], right: ["Receiver", ""], note: "" }, { left: ["Sender", "HELLO"], right: ["Receiver", ""], keyL: "key: shift 3", keyR: "key: shift 3", note: "both hold the same secret key (shared first)" }, { left: ["Sender", "HELLO"], right: ["Receiver", ""], mid: "KHOOR", keyL: "encrypt with the key", keyR: "", note: "cipher text travels; an eavesdropper sees only KHOOR" }, { left: ["Sender", ""], right: ["Receiver", "HELLO"], mid: "", keyL: "", keyR: "decrypt with the same key", note: "the same key reverses it" }];
  Lib.stepper($("#stA"), { w: 640, h: 190, label: "Symmetric", base: { i: 0 }, draw: (s) => msgDraw(S[Math.round(s.i)]), tween: 120, dwell: 2800, steps: [{ cap: "The sender wants to send HELLO privately.", s: { i: 0 } }, { cap: "<b>Symmetric</b>: both sides need the <b>same key</b>. Getting it to the receiver safely is the key distribution problem.", s: { i: 1 } }, { cap: "The sender encrypts the plain text with the key: the cipher text <b>KHOOR</b> is sent.", s: { i: 2 } }, { cap: "The receiver decrypts with the same key and gets HELLO.", s: { i: 3 } }] });
})();
(function () {
  const S = [{ left: ["Sender", "HELLO"], right: ["Receiver", ""], note: "" }, { left: ["Sender", "HELLO"], right: ["Receiver", ""], keyR: "makes a key pair: public + private", note: "" }, { left: ["Sender", "HELLO"], right: ["Receiver", ""], keyL: "has the receiver's PUBLIC key", keyR: "keeps the PRIVATE key secret", note: "the public key can be sent to anyone" }, { left: ["Sender", ""], right: ["Receiver", ""], mid: "x9#Qk2", keyL: "encrypt with receiver's PUBLIC key", keyR: "", note: "" }, { left: ["Sender", ""], right: ["Receiver", "HELLO"], mid: "", keyL: "", keyR: "decrypt with own PRIVATE key", note: "only the private key can decrypt it" }];
  Lib.stepper($("#stB"), { w: 640, h: 190, label: "Private message", base: { i: 0 }, draw: (s) => msgDraw(S[Math.round(s.i)]), tween: 120, dwell: 2800, steps: [{ cap: "The sender wants to send a <b>private message</b> to the receiver.", s: { i: 0 } }, { cap: "The receiver generates a <b>matched pair of keys</b>.", s: { i: 1 } }, { cap: "The receiver makes the <b>public key</b> available. The <b>private key</b> is never sent.", s: { i: 2 } }, { cap: "The sender encrypts with the <b>receiver's public key</b> and sends the cipher text.", s: { i: 3 } }, { cap: "The receiver decrypts with the <b>private key</b>. Nobody else can.", s: { i: 4 } }] });
})();
(function () {
  const S = [{ left: ["Organisation", "NOTICE"], right: ["Anyone", ""], note: "" }, { left: ["Organisation", "NOTICE"], right: ["Anyone", ""], keyL: "key pair; public key published", keyR: "has the organisation's PUBLIC key", note: "" }, { left: ["Organisation", ""], right: ["Anyone", ""], mid: "q4%Rz8", keyL: "encrypt with its PRIVATE key", keyR: "", note: "" }, { left: ["Organisation", ""], right: ["Anyone", "NOTICE"], mid: "", keyL: "", keyR: "decrypt with the PUBLIC key", note: "it must have come from the organisation: verified" }];
  Lib.stepper($("#stC"), { w: 640, h: 190, label: "Verified message", base: { i: 0 }, draw: (s) => msgDraw(S[Math.round(s.i)]), tween: 120, dwell: 2800, steps: [{ cap: "An organisation wants to send a <b>verified</b> message to the public.", s: { i: 0 } }, { cap: "It generates a key pair and makes its <b>public key</b> available, for example on its website.", s: { i: 1 } }, { cap: "It encrypts the message with its <b>private key</b> and sends it to everyone.", s: { i: 2 } }, { cap: "Anyone can decrypt with the <b>public key</b>. Only the owner of the private key could have made it, so the sender is verified.", s: { i: 3 } }] });
})();

(function () {
  const inp = $("#cI"); let k = 3;
  const enc = (s, k) => [...s.toUpperCase()].map((c) => (/[A-Z]/.test(c) ? String.fromCharCode(((c.charCodeAt(0) - 65 + k + 26) % 26) + 65) : c)).join("");
  const paint = () => { const c = enc(inp.value, k); $("#cV").innerHTML = `Plain text <b class="bx">${inp.value.toUpperCase()}</b> → cipher text <b class="bx">${c}</b> (key: shift ${k}). Decrypting <b class="bx">${c}</b> with the same key gives <b class="bx">${enc(c, -k)}</b>. Anyone who learns the key can read every message.`; };
  Lib.slider($("#cS"), { id: "cs", label: "Shared key (shift) ", min: 1, max: 25, value: k, fmt: (x) => x, onInput: (v) => { k = v; paint(); } }); inp.oninput = paint; paint();
})();
(function () {
  const N = 3233, E = 17, D = 2753; let m = 65;
  const pw = (b, e) => { let r = 1n, x = BigInt(b) % BigInt(N), p = BigInt(e); while (p > 0n) { if (p & 1n) r = (r * x) % BigInt(N); x = (x * x) % BigInt(N); p >>= 1n; } return Number(r); };
  const paint = () => { const c = pw(m, E), back = pw(c, D), sig = pw(m, D), ver = pw(sig, E);
    $("#rO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Step</th><th>Calculation</th><th>Result</th></tr>' + `<tr><td>Message (plain text)</td><td></td><td>${m}</td></tr><tr><td>Encrypt with the <b>public</b> key</td><td>${m}^${E} mod ${N}</td><td><b>${c}</b></td></tr><tr><td>Decrypt with the <b>private</b> key</td><td>${c}^${D} mod ${N}</td><td><b>${back}</b></td></tr></table></div>` + `<div class="verdict">Private message: only the holder of d = ${D} can turn ${c} back into ${back}. Verified message: encrypting ${m} with the <b>private</b> key gives ${sig}; anyone can use the public key to get ${ver} back, which proves it came from the key's owner.</div>`; };
  Lib.slider($("#rS"), { id: "rs", label: "Message number ", min: 2, max: 3000, value: m, fmt: (x) => x, onInput: (v) => { m = v; paint(); } }); paint();
})();
btnTable("kB", "kO", [
  ["Send a private message to Ben", "Ben's public key", "Ben's private key", "Only Ben can read it"],
  ["Send a verified message to the public", "Your private key", "Your public key (anyone)", "Proves it came from you; anyone can read it"],
  ["Symmetric encryption", "The shared secret key", "The same shared secret key", "Both sides need the key first"],
  ["Receive a private message", "(the sender uses your public key)", "Your private key", "Never share the private key"]
], ["Situation", "Encrypt with", "Decrypt with", "Result"]);
Lib.classify($("#cl1"), { prompt: "Symmetric or asymmetric?", buckets: [{"label": "Symmetric"}, {"label": "Asymmetric"}], items: [{"text": "One key encrypts and decrypts", "b": 0}, {"text": "A matched pair of keys", "b": 1}, {"text": "Has the key distribution problem", "b": 0}, {"text": "Slower and needs longer keys", "b": 1}, {"text": "Allows the sender to be verified", "b": 1}, {"text": "Quick and simple", "b": 0}], done: "Symmetric: one shared key. Asymmetric: public and private pair." });
Lib.classify($("#cl2"), { prompt: "Which key is used?", buckets: [{"label": "Receiver's public key"}, {"label": "Receiver's private key"}, {"label": "Sender's private key"}], items: [{"text": "Encrypting a private message to the receiver", "b": 0}, {"text": "The receiver decrypting a private message", "b": 1}, {"text": "Encrypting a verified message", "b": 2}, {"text": "Keeping the message secret from everyone else", "b": 0}, {"text": "Never sent to anyone", "b": 1}, {"text": "Proving who sent the message", "b": 2}], done: "Private message: receiver's public key in, receiver's private key out." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Plain text", "The original readable data"], ["Cipher text", "The result of encrypting plain text"], ["Public key", "A key anyone can have"], ["Private key", "A key kept secret by its owner"], ["Key distribution problem", "A symmetric key has to be shared safely"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of sending a private message in order.", items: ["The receiver generates a matched pair of keys", "The receiver makes the public key available to the sender", "The sender encrypts the message with the public key", "The sender sends the cipher text", "The receiver decrypts it with the private key"], done: "Generate, publish, encrypt, send, decrypt." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many keys are used in symmetric encryption between two people?", "a": 1, "unit": "", "tol": 0.01, "hint": "One shared key.", "sol": "<b>1</b>."},
  {"q": "How many keys does one user have in asymmetric encryption?", "a": 2, "unit": "", "tol": 0.01, "hint": "Public and private.", "sol": "<b>2</b>."},
  {"q": "A Caesar cipher with shift 3 encrypts the letter A. Which position in the alphabet (A = 1) is the cipher letter?", "a": 4, "unit": "", "tol": 0.01, "hint": "A to D.", "sol": "<b>4</b> (D)."},
  {"q": "Toy keys n = 3233, e = 17: what is 2790 decrypted with d = 2753? (use the lab)", "a": 65, "unit": "", "tol": 0.01, "hint": "Message 65 encrypts to 2790.", "sol": "<b>65</b>."},
  {"q": "A symmetric key is 128 bits and an asymmetric key is 2048 bits. How many times longer is the asymmetric key?", "a": 16, "unit": "", "tol": 0.01, "hint": "2048 ÷ 128.", "sol": "<b>16</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which key encrypts a private message to Sam?", opts: ["Sam's private key", "Sam's public key", "Your private key", "Your public key"], a: 1, why: "The receiver's public key." },
  { q: "The private key is:", opts: ["Sent with the message", "Kept secret by its owner", "Published on a website", "Shared with everyone"], a: 1, why: "Never transmitted." },
  { q: "Which is a drawback of symmetric encryption?", opts: ["Slow", "The key has to be shared safely", "Two keys", "Long keys"], a: 1, why: "The key distribution problem." },
  { q: "A verified message is encrypted with:", opts: ["The receiver's public key", "The sender's private key", "The receiver's private key", "No key"], a: 1, why: "The sender's private key." },
  { q: "Cipher text is:", opts: ["Readable data", "Encrypted data", "A key", "A certificate"], a: 1, why: "Encrypted data." },
  { q: "Asymmetric encryption can:", opts: ["Verify the sender", "Only be used by banks", "Not use keys", "Only decrypt"], a: 0, why: "It allows verification." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Plain text", "Original readable data."],
  ["Cipher text", "Encrypted data."],
  ["Symmetric", "One shared key; fast; key distribution problem."],
  ["Asymmetric", "Public and private pair; slower; longer keys."],
  ["Private message", "Encrypt with the receiver's public key."],
  ["Verified message", "Encrypt with your private key."],
  ["Private key", "Secret; never transmitted."],
  ["Public key", "Available to anyone."],
] });
