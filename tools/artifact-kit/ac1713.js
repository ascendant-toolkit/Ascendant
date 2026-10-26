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
  const M = [["Client", "ClientHello: I want a secure connection"], ["Server", "Sends its digital certificate"], ["Client", "Verifies the certificate; gets the server's public key"], ["Client + Server", "Agree the encryption algorithms"], ["Client + Server", "Generate shared symmetric session keys"], ["Both", "Secure session established"]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 14, 150, 40, "cell", { rx: 8 }) + SV.text(95, 40, "Client", "lbl bd", { "text-anchor": "middle" }) + SV.rect(450, 14, 150, 40, "cell", { rx: 8 }) + SV.text(525, 40, "Server", "lbl bd", { "text-anchor": "middle" }) + SV.path("M95,54 V320", "ax", { style: "stroke-dasharray:4 5;opacity:.5" }) + SV.path("M525,54 V320", "ax", { style: "stroke-dasharray:4 5;opacity:.5" });
    M.slice(0, k).forEach(([who, t], i) => { const y = 84 + i * 48, cur = i === k - 1; const toServer = i === 0, toClient = i === 1; o += (toServer ? SV.path("M95," + y + " H450", "ax", {}) + SV.arrowHead(450, y, "r", "arr") : toClient ? SV.path("M525," + y + " H100", "ax", {}) + SV.arrowHead(95, y, "l", "arr") : "") + SV.text(310, y - 8, t, "lbl" + (cur ? " bd" : ""), { "text-anchor": "middle", style: "font-size:12.5px" }); });
    return o; };
  Lib.stepper($("#stA"), { w: 620, h: 340, label: "TLS handshake", base: { i: 0 }, draw, tween: 120, dwell: 2800, steps: [{ cap: "Before any data is sent, the client and server carry out a <b>handshake</b>.", s: { i: 0 } }, { cap: "The client (the application that starts the connection) asks for a secure session.", s: { i: 1 } }, { cap: "The server sends its <b>digital certificate</b>.", s: { i: 2 } }, { cap: "The client <b>verifies the certificate</b> and takes the server's <b>public key</b> from it.", s: { i: 3 } }, { cap: "The two sides <b>agree the encryption algorithms</b>.", s: { i: 4 } }, { cap: "<b>Symmetric session keys</b> are generated, with the public key making it safe to share them.", s: { i: 5 } }, { cap: "A <b>secure session</b> is established.", s: { i: 6 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 30, 130, 50, "cell", { rx: 8 }) + SV.text(85, 60, "Client", "lbl bd", { "text-anchor": "middle" }) + SV.rect(470, 30, 130, 50, "cell", { rx: 8 }) + SV.text(535, 60, "Server", "lbl bd", { "text-anchor": "middle" });
    o += SV.rect(150, 40, 320, 30, "f3", { rx: 15, ...op(0.35) }) + SV.text(310, 28, "secure tunnel (session key)", "sm", { "text-anchor": "middle" });
    if (k >= 1) o += SV.text(85, 110, "card=4242...", "lbl", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:12px" });
    if (k >= 2) o += SV.rect(250, 44, 120, 22, "f2", { rx: 4 }) + SV.text(310, 60, "x7#Qa9!kP2", "lbl", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:12px" });
    if (k >= 3) o += SV.text(535, 110, "card=4242...", "lbl", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:12px" }) + SV.text(310, 140, "an eavesdropper sees only x7#Qa9!kP2", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 620, h: 160, label: "Record protocol", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: [{ cap: "The handshake is complete. The client wants to send a card number.", s: { i: 0 } }, { cap: "The <b>record protocol</b> takes the data...", s: { i: 1 } }, { cap: "...encrypts and authenticates it with the session key, so it is protected as it travels.", s: { i: 2 } }, { cap: "The server decrypts it. Anyone who intercepts the data sees only cipher text, and any change would be noticed.", s: { i: 3 } }] });
})();

(function () {
  let tls = false; const inp = $("#vI"), b = $("#vB");
  const enc = (s) => { let h = 7; return [...s].map((c, i) => { h = (h * 31 + c.charCodeAt(0) + i * 17) % 4093; return h.toString(16).padStart(3, "0"); }).join(""); };
  const paint = () => { $("#vO").innerHTML = `<div class="tw"><table class="t mono"><tr><th>What the eavesdropper sees</th></tr><tr><td style="word-break:break-all">${tls ? enc(inp.value) : inp.value.replace(/</g, "&lt;")}</td></tr></table></div><div class="verdict">${tls ? "With SSL/TLS the data is <b>encrypted</b>: it is meaningless without the session key, and the server was authenticated first." : "Without SSL/TLS the data is sent as <b>plain text</b>: anyone on the route can read it, or change it."}</div>`; b.querySelectorAll("button").forEach((x) => (x.className = (x.dataset.k === "t") === tls ? "on" : "")); };
  [["p", "Without SSL/TLS"], ["t", "With SSL/TLS"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { tls = k === "t"; paint(); }; b.appendChild(x); });
  inp.oninput = paint; paint();
})();
btnTable("sB", "sO", [
  ["Sending a password to log in", "Yes", "Authentication data must be protected"],
  ["Entering card details to pay", "Yes", "Non-public data that must not be read or changed"],
  ["Sending a session cookie", "Yes", "It proves who you are; stealing it would let someone pretend to be you"],
  ["Reading a public news headline page", "Not essential", "Public data; nothing secret is sent (but TLS is still common)"],
  ["Sending results from a server to a user's input", "Yes", "Must be protected from modification on the way"],
  ["Filling in a private medical form", "Yes", "Non-public personal data"]
], ["Situation", "Use SSL/TLS?", "Reason"]);
Lib.classify($("#cl1"), { prompt: "Which protocol of TLS?", buckets: [{"label": "Handshake protocol"}, {"label": "Record protocol"}], items: [{"text": "Client and server authenticate each other", "b": 0}, {"text": "Encrypts the data sent after the session starts", "b": 1}, {"text": "Agrees the encryption algorithms", "b": 0}, {"text": "Protects the integrity of the data in transit", "b": 1}, {"text": "Establishes a secure connection between two devices", "b": 0}, {"text": "Deals with the format of data transmission", "b": 1}], done: "Handshake sets up; record protects the data." });
Lib.classify($("#cl2"), { prompt: "Is SSL/TLS appropriate?", buckets: [{"label": "Yes"}, {"label": "Not needed"}], items: [{"text": "Sending a password", "b": 0}, {"text": "Reading a public page with nothing to protect", "b": 1}, {"text": "Online payment", "b": 0}, {"text": "Sending a session cookie", "b": 0}, {"text": "Posting non-public health data", "b": 0}, {"text": "Looking at a public weather map", "b": 1}], done: "Use it for authentication data and non-public or must-not-be-changed data." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Handshake", "The start of a session: certificate checked, keys agreed"], ["Digital certificate", "Sent by the server to prove its identity and give its public key"], ["Session key", "A symmetric key used for one secure session"], ["Record protocol", "Encrypts and authenticates the data in the session"], ["Client", "The application that starts the connection"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the handshake steps in order.", items: ["The client starts the connection", "The server sends its digital certificate", "The client verifies the certificate and obtains the public key", "The encryption algorithms are agreed and session keys generated", "A secure session is established"], done: "Start, certificate, verify, agree, secure." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many main protocols make up TLS?", "a": 2, "unit": "", "tol": 0.01, "hint": "Handshake and record.", "sol": "<b>2</b>."},
  {"q": "How many functions of SSL/TLS were listed in the purpose (encryption, authentication, confidentiality, integrity)?", "a": 4, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>4</b>."},
  {"q": "A page uses https. Does the data travel as plain text? Enter 0 for no, 1 for yes.", "a": 0, "unit": "", "tol": 0.01, "hint": "It is encrypted.", "sol": "<b>0</b>."},
  {"q": "How many keys does the server hold in the handshake that the client needs from its certificate (the public key)?", "a": 1, "unit": "", "tol": 0.01, "hint": "The public key.", "sol": "<b>1</b>."},
  {"q": "The session keys are symmetric. How many keys does each side use for the session?", "a": 1, "unit": "", "tol": 0.01, "hint": "One shared key.", "sol": "<b>1</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "SSL/TLS provides:", opts: ["Only speed", "Encryption and authentication", "Only storage", "Printing"], a: 1, why: "Encryption and authentication." },
  { q: "The client:", opts: ["Starts the connection", "Is always the server", "Issues certificates", "Has no keys"], a: 0, why: "It initiates it." },
  { q: "The handshake includes:", opts: ["The server sending its certificate", "Deleting the data", "A virus scan", "Compression only"], a: 0, why: "Certificate." },
  { q: "The session keys are:", opts: ["Asymmetric", "Symmetric", "Quantum", "None"], a: 1, why: "Symmetric." },
  { q: "Which would use SSL/TLS?", opts: ["Sending a password", "Reading public information only", "Nothing", "Turning off the screen"], a: 0, why: "Passwords." },
  { q: "The record protocol:", opts: ["Sets the session up", "Encrypts and authenticates the data", "Issues certificates", "Compresses files"], a: 1, why: "Protects the data." },
] });
Lib.cards($("#fc1"), { cards: [
  ["SSL/TLS", "Secure, authenticated, encrypted client-server communication."],
  ["Handshake", "Certificate, verify, algorithms, session keys."],
  ["Record protocol", "Encrypts and authenticates the session data."],
  ["Session key", "Symmetric key for one session."],
  ["Client", "Starts the connection."],
  ["Server", "Receives it; sends its certificate."],
  ["Use when", "Passwords, cookies, non-public data."],
  ["Provides", "Encryption, authentication, confidentiality, integrity."],
] });
