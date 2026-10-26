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

function lcg(seed) { let s = seed; return () => ((s = (s * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff); }
(function () {
  const rnd = lcg(7), bits = Array.from({ length: 8 }, () => (rnd() < 0.5 ? 0 : 1)), flips = [0, 0, 1, 0, 0, 1, 0, 0].map(Number);
  const make = (el, eve) => { const recv = bits.map((b, i) => (eve ? b ^ flips[i] : b));
    const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "Sender", "lbl bd") + SV.text(20, 112, "Receiver", "lbl bd"); if (eve) o += SV.text(300, 22, "Eavesdropper measures each photon", "sm");
      bits.forEach((b, i) => { const x = 130 + i * 56, sent = i < k + 1 && k >= 0; o += SV.rect(x, 30, 46, 40, "f1", { rx: 6 }) + SV.text(x + 23, 57, String(b), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:18px" }); if (i < k) { const bad = recv[i] !== b; o += SV.rect(x, 96, 46, 40, bad ? "cell-no" : "cell-ok", { rx: 6 }) + SV.text(x + 23, 123, String(recv[i]), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:18px" }); } });
      if (k >= 8) { const err = recv.filter((r, i) => r !== bits[i]).length; o += SV.text(20, 168, eve ? "Compare: " + err + " bits differ, so an eavesdropper is detected. The key is discarded." : "Compare: all bits match. The key can be used.", "lbl bd " + (eve ? "t2" : "t3"), { style: "font-size:13.5px" }); } return o; };
    Lib.stepper(el, { w: 620, h: 186, label: eve ? "With eavesdropper" : "No eavesdropper", base: { i: 0 }, draw, tween: 100, dwell: 1500, steps: [0, 1, 2, 3, 4, 5, 6, 7, 8].map((i) => ({ cap: i === 0 ? (eve ? "The sender sends eight photons; an eavesdropper tries to measure them on the way." : "The sender sends eight photons down the fibre; the receiver measures each one.") : i === 8 ? (eve ? "Measuring photons disturbs them, so some arrive wrong. The two sides compare bits and find the differences." : "Every bit matches: nobody has disturbed the photons.") : "Photon " + i + " arrives" + (eve && recv[i - 1] !== bits[i - 1] ? " but its state was changed by the eavesdropper: <b>wrong bit</b>." : "."), s: { i } })) }); };
  make($("#stA"), false); make($("#stB"), true);
})();
(function () {
  let eve = false, n = 40; const b = $("#eB");
  const paint = () => { const rnd = lcg(11), sent = [], recv = []; for (let i = 0; i < n; i++) { const s = rnd() < 0.5 ? 0 : 1; sent.push(s); const wrong = eve && rnd() < 0.25; recv.push(wrong ? 1 - s : s); }
    const diff = sent.filter((s, i) => s !== recv[i]).length; $("#eT").innerHTML = '<div class="tw"><table class="t mono"><tr><td>sent</td><td>' + sent.join("") + "</td></tr><tr><td>received</td><td>" + recv.map((r, i) => (r !== sent[i] ? '<b style="color:var(--bad)">' + r + "</b>" : r)).join("") + "</td></tr></table></div>";
    $("#eV").innerHTML = eve ? `With an eavesdropper about a quarter of the bits are disturbed: <b>${diff}</b> of ${n} differ. The sides see the mismatch, <b>detect the eavesdropper</b>, discard the key and request another.` : `<b>${diff}</b> bits differ: nobody has measured the photons, so the key can be used.`; b.querySelectorAll("button").forEach((x) => (x.className = (x.dataset.k === "on") === eve ? "on" : "")); };
  [["off", "No eavesdropper"], ["on", "Eavesdropper listening"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { eve = k === "on"; paint(); }; b.appendChild(x); });
  Lib.slider($("#eS"), { id: "es", label: "Photons sent ", min: 8, max: 80, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();
btnTable("bB", "bO", [
  ["Eavesdropping can be detected", "Benefit", "Measuring a photon changes it, so errors appear"],
  ["Needs dedicated fibre and specialist hardware", "Drawback", "Expensive to buy and maintain"],
  ["Based on the laws of physics", "Benefit", "Not reliant on a mathematical problem"],
  ["Works only over short distances", "Drawback", "A current limit of the technology"],
  ["Polarisation may be altered in the fibre", "Drawback", "Causes errors in the key"],
  ["Keys cannot be copied", "Benefit", "No-cloning theorem"]
], ["Point", "Benefit or drawback", "Reason"]);
Lib.classify($("#cl1"), { prompt: "Is it a benefit or a drawback?", buckets: [{"label": "Benefit"}, {"label": "Drawback"}], items: [{"text": "Eavesdropping can be detected", "b": 0}, {"text": "Needs a dedicated fibre-optic line", "b": 1}, {"text": "Virtually unhackable", "b": 0}, {"text": "Currently works over short distances only", "b": 1}, {"text": "Longer keys can be exchanged", "b": 0}, {"text": "Equipment is very expensive", "b": 1}, {"text": "Criminals can hide their communications", "b": 1}], done: "Benefits: detection, security, longer keys. Drawbacks: cost, range, hardware." });
Lib.classify($("#cl2"), { prompt: "Which type of cryptography?", buckets: [{"label": "Symmetric"}, {"label": "Asymmetric"}, {"label": "Quantum"}], items: [{"text": "Uses photons", "b": 2}, {"text": "One shared key", "b": 0}, {"text": "A public and a private key", "b": 1}, {"text": "Detects eavesdropping by the change in a state", "b": 2}, {"text": "Has the key distribution problem", "b": 0}, {"text": "Can verify the sender with a key pair", "b": 1}], done: "Quantum uses the properties of photons." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Quantum cryptography", "Uses laws of quantum physics to exchange keys securely"], ["Photon", "A particle of light carrying a bit"], ["Eavesdropping", "Listening to a communication without permission"], ["No-cloning", "A quantum state cannot be copied"], ["Fibre-optic cable", "The medium the photons travel through"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of a quantum key exchange in order.", items: ["The sender sends photons carrying the key bits", "The receiver measures them", "The two sides compare a sample of the bits", "If the bits match, no eavesdropper is present and the key is used", "The message is encrypted with the key and sent"], done: "Send, measure, compare, accept, encrypt." });
Lib.calc($("#c1"), { qs: [
  {"q": "A key exchange sends 40 photons. An eavesdropper disturbs about a quarter of them. About how many bits are wrong?", "a": 10, "unit": "", "tol": 0.5, "hint": "40 × 0.25.", "sol": "<b>10</b>."},
  {"q": "In the comparison, 0 of 20 sample bits differ. How many eavesdroppers are suggested?", "a": 0, "unit": "", "tol": 0.01, "hint": "No errors, no eavesdropper.", "sol": "<b>0</b>."},
  {"q": "How many benefits does a Paper 3 question usually ask for, and how many drawbacks? Add the numbers.", "a": 4, "unit": "", "tol": 0.01, "hint": "Two and two.", "sol": "<b>4</b>."},
  {"q": "What kind of cable carries the photons? Enter 1 for copper, 2 for fibre-optic.", "a": 2, "unit": "", "tol": 0.01, "hint": "Light needs fibre.", "sol": "<b>2</b>."},
  {"q": "A key has 256 bits and a quarter are discarded after comparing. How many bits remain?", "a": 192, "unit": "", "tol": 0.5, "hint": "256 × 3/4.", "sol": "<b>192</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Quantum cryptography uses:", opts: ["Prime numbers", "Photons", "Passwords", "Paper keys"], a: 1, why: "Photons." },
  { q: "How is an eavesdropper detected?", opts: ["By a loud noise", "Errors appear because measuring photons changes them", "By a certificate", "They cannot be detected"], a: 1, why: "Disturbed states." },
  { q: "A drawback is:", opts: ["It detects eavesdropping", "It needs a dedicated fibre line and specialist hardware", "It uses physics", "It uses long keys"], a: 1, why: "Cost and hardware." },
  { q: "Quantum cryptography is used mainly for:", opts: ["Exchanging keys securely", "Printing", "Compressing files", "Browsing"], a: 0, why: "Secure key exchange." },
  { q: "Which is a benefit?", opts: ["Short range", "Virtually unhackable", "High cost", "Needs dedicated line"], a: 1, why: "Virtually unhackable." },
  { q: "The no-cloning theorem means:", opts: ["Keys can be copied", "A quantum state cannot be copied", "Photons are free", "Fibre is cheap"], a: 1, why: "Cannot be copied." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Purpose", "Virtually unbreakable key exchange using quantum physics."],
  ["Detects eavesdropping", "Photon states change when measured."],
  ["Benefit", "Security from physics; longer keys; no-cloning."],
  ["Drawback", "Cost, dedicated fibre, short range, polarisation altered."],
  ["Photon", "Particle of light that carries a bit."],
  ["Fibre-optic", "The cable photons travel in."],
  ["Key exchange", "Keys first, then the message."],
  ["Third type", "Not symmetric or asymmetric."],
] });
