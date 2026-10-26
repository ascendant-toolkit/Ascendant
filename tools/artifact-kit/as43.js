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

const BM = { AND: (a, m) => a & m, OR: (a, m) => a | m, XOR: (a, m) => a ^ m, LSL: (a, n) => (a << n) & 255, LSR: (a, n) => a >> n, CSL: (a, n) => ((a << n) | (a >> (8 - n))) & 255, CSR: (a, n) => ((a >> n) | (a << (8 - n))) & 255 };
const b8 = (n) => ("00000000" + (n & 255).toString(2)).slice(-8), g4 = (s) => s.slice(0, 4) + " " + s.slice(4);
(function () {
  const draw = (s) => { const k = Math.round(s.i); const a = "00011110"; const r = [a, "00111100", "01111000", "01111000"]; let o = ""; for (let i = 0; i < 8; i++) { const bit = r[Math.min(k, 2)][i]; o += SV.rect(30 + i * 40, 30, 34, 34, bit === "1" ? "f1" : "cell", { rx: 6 }) + SV.text(47 + i * 40, 53, bit, "lbl bd", { "text-anchor": "middle" }); }
    o += SV.text(30, 100, ["ACC = 0001 1110", "LSL #1: every bit moves one place left", "LSL #2: two places left; zeros enter on the right", "0001 1110 LSL #2 = 0111 1000 (30 × 4 = 120)"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 380, h: 120, label: "Shift left", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "The ACC holds 0001 1110 (30).", s: { i: 0 } }, { cap: "<b>LSL #1</b>: each bit moves one place left, a 0 enters on the right.", s: { i: 1 } }, { cap: "<b>LSL #2</b>: two places.", s: { i: 2 } }, { cap: "The result is 0111 1000 = 120, which is 30 × 2<sup>2</sup>.", s: { i: 3 } }] });
})();
(function () {
  const A = "10011010", M = "00011110", R = "00011010";
  const draw = (s) => { const k = Math.round(s.i); let o = ""; const row = (y, t, str, on) => { o += SV.text(10, y + 22, t, "sm"); for (let i = 0; i < 8; i++) o += SV.rect(80 + i * 40, y, 34, 30, str[i] === "1" ? (on ? "f1" : "f3") : "cell", { rx: 5 }) + SV.text(97 + i * 40, y + 21, str[i], "lbl bd", { "text-anchor": "middle" }); };
    row(10, "ACC", A, false); row(50, "mask", M, false); if (k >= 1) row(90, "AND", k >= 3 ? R : R.slice(0, k * 3) + "?".repeat(8 - k * 3), true); return o; };
  Lib.stepper($("#stB"), { w: 420, h: 135, label: "AND", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "ACC = 1001 1010 and the mask is 0001 1110 (#30).", s: { i: 0 } }, { cap: "AND is 1 only when both bits are 1. A 0 in the mask <b>clears</b> that bit.", s: { i: 1 } }, { cap: "The top bits of the mask are 0, so they are cleared.", s: { i: 2 } }, { cap: "Result: 0001 1010.", s: { i: 3 } }] });
})();
(function () {
  const A = "01100101", M = "11111111", R = "10011010";
  const draw = (s) => { const k = Math.round(s.i); let o = ""; const row = (y, t, str) => { o += SV.text(10, y + 22, t, "sm"); for (let i = 0; i < 8; i++) o += SV.rect(80 + i * 40, y, 34, 30, str[i] === "1" ? "f1" : "cell", { rx: 5 }) + SV.text(97 + i * 40, y + 21, str[i], "lbl bd", { "text-anchor": "middle" }); };
    row(10, "ACC", A); row(50, "mask", M); if (k >= 1) row(90, "XOR", k >= 2 ? R : "????????"); o += SV.text(80, 140, ["", "XOR is 1 when the bits differ", "A mask of all 1s flips every bit: XOR #255", ""][Math.min(k, 3)], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 420, h: 150, label: "XOR", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "ACC = 0110 0101 and the mask is 1111 1111.", s: { i: 0 } }, { cap: "XOR gives 1 when the bits <b>differ</b>.", s: { i: 1 } }, { cap: "With a mask of all 1s every bit is <b>flipped</b>: 1001 1010.", s: { i: 2 } }] });
})();

(function () {
  let acc = 0b01100101, op = "AND", opd = 0b00001111;
  const bits = $("#bA"), ops = $("#bI");
  const paint = () => { bits.querySelectorAll("button").forEach((b, i) => { const v = (acc >> (7 - i)) & 1; b.textContent = v; b.className = v ? "on" : ""; });
    const sh = ["LSL", "LSR", "CSL", "CSR"].includes(op); const n = opd & 7; const res = BM[op](acc, sh ? n : opd);
    $("#bS").innerHTML = `<div class="mono">ACC &nbsp;&nbsp;${g4(b8(acc))}<br>${op} ${sh ? "#" + n : "B" + g4(b8(opd))}<br><b>result ${g4(b8(res))}</b> (denary ${res})</div>`;
    $("#bV").innerHTML = op === "AND" ? "AND keeps a bit only where the mask has a 1: it <b>clears</b> the others." : op === "OR" ? "OR sets a bit wherever the mask has a 1." : op === "XOR" ? "XOR flips the bits where the mask has a 1." : op === "LSL" ? "Logical shift left: zeros enter on the right; bits shifted off the left are lost." : op === "LSR" ? "Logical shift right: zeros enter on the left." : "Cyclic shift: bits pushed off one end come back on the other."; };
  for (let i = 0; i < 8; i++) { const b = document.createElement("button"); b.onclick = () => { acc ^= 1 << (7 - i); paint(); }; bits.appendChild(b); }
  ["AND", "OR", "XOR", "LSL", "LSR", "CSL", "CSR"].forEach((o) => { const b = document.createElement("button"); b.textContent = o; b.onclick = () => { op = o; ops.querySelectorAll("button").forEach((x) => x.className = x === b ? "on" : ""); paint(); }; if (o === op) b.className = "on"; ops.appendChild(b); });
  Lib.slider($("#bS").parentNode.insertBefore(document.createElement("div"), $("#bS")), { id: "bo", label: "Operand (0 to 255; for shifts the low 3 bits) ", min: 0, max: 255, value: opd, fmt: (x) => x, onInput: (v) => { opd = v; paint(); } }); paint();
})();
btnTable("wB", "wO", [
  ["Set the least significant bit and leave the rest", "OR #1", "OR sets bits"],
  ["Clear the register", "AND B00000000", "AND with 0 clears"],
  ["Flip every bit", "XOR #255", "XOR with 1 flips"],
  ["Test whether a number is odd", "AND #1 then compare with 1", "Isolate the LSB"],
  ["Multiply by 8", "LSL #3", "2^3"],
  ["Divide by 4", "LSR #2", "2^2"]
], ["Task", "Instruction", "Why"]);
(function () {
  let n = 12, k = 2; const paint = () => { $("#sV").innerHTML = `LSL #${k}: ${n} × 2<sup>${k}</sup> = <b>${n << k}</b>` + (((n << k) > 255) ? " (too big for 8 bits: the top bits are lost, so the 8-bit result is <b>" + ((n << k) & 255) + "</b>)" : "") + `.<br>LSR #${k}: ${n} ÷ 2<sup>${k}</sup> = <b>${n >> k}</b> (the remainder is discarded).`; };
  Lib.slider($("#sS").appendChild(document.createElement("div")), { id: "s1", label: "Number ", min: 0, max: 255, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } });
  Lib.slider($("#sS").appendChild(document.createElement("div")), { id: "s2", label: "Shift places ", min: 0, max: 7, value: k, fmt: (x) => x, onInput: (v) => { k = v; paint(); } }); paint();
})();
Lib.classify($("#cl1"), { prompt: "Which instruction does the task need?", buckets: [{"label": "AND"}, {"label": "OR"}, {"label": "XOR"}], items: [{"text": "Clear some bits to 0", "b": 0}, {"text": "Set some bits to 1", "b": 1}, {"text": "Flip some bits", "b": 2}, {"text": "Test whether the last bit is 1", "b": 0}, {"text": "Set the least significant bit and leave the rest", "b": 1}, {"text": "Invert every bit with mask 11111111", "b": 2}], done: "AND clears and tests, OR sets, XOR flips." });
Lib.classify($("#cl2"), { prompt: "Left shift or right shift?", buckets: [{"label": "LSL"}, {"label": "LSR"}], items: [{"text": "Multiplies an unsigned number by 2^n", "b": 0}, {"text": "Divides an unsigned number by 2^n", "b": 1}, {"text": "Zeros enter on the right", "b": 0}, {"text": "Zeros enter on the left", "b": 1}, {"text": "Bits can be lost from the left end", "b": 0}, {"text": "Bits can be lost from the right end", "b": 1}], done: "LSL multiplies; LSR divides." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["AND B00000000", "Clears the ACC to zero"], ["OR #1", "Sets the least significant bit"], ["XOR #255", "Flips every bit"], ["AND #1", "Isolates the least significant bit"], ["LSL #1", "Doubles an unsigned number"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the odd-number test in order.", items: ["Take the number in the ACC", "Mask it with AND #1", "The result is 1 if the least significant bit is 1", "Compare the ACC with 1", "If equal, the number is odd"], done: "Number, mask, bit, compare, odd." });
Lib.calc($("#c1"), { qs: [
  {"q": "ACC = 0001 0111 (23). What denary value after LSL #2?", "a": 92, "unit": "", "tol": 0.01, "hint": "23 × 4.", "sol": "<b>92</b>."},
  {"q": "ACC = 0010 1000 (40). What denary value after LSR #3?", "a": 5, "unit": "", "tol": 0.01, "hint": "40 ÷ 8.", "sol": "<b>5</b>."},
  {"q": "How many bits are lost when 0110 1101 is shifted left by 4?", "a": 4, "unit": "", "tol": 0.01, "hint": "The leading four.", "sol": "<b>4</b>."},
  {"q": "ACC = 1001 1010 after AND #30 (0001 1110): what denary value?", "a": 26, "unit": "", "tol": 0.01, "hint": "0001 1010.", "sol": "<b>26</b>."},
  {"q": "What is &F1 in denary?", "a": 241, "unit": "", "tol": 0.01, "hint": "15 × 16 + 1.", "sol": "<b>241</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which instruction clears bits?", opts: ["AND", "OR", "XOR", "LSL"], a: 0, why: "AND with 0." },
  { q: "Which sets bits?", opts: ["OR", "AND", "LSR", "CMP"], a: 0, why: "OR with 1." },
  { q: "LSL #1 on an unsigned number:", opts: ["Doubles it", "Halves it", "Adds 1", "Clears it"], a: 0, why: "×2." },
  { q: "XOR with 1 does what to a bit?", opts: ["Flips it", "Clears it", "Sets it", "Keeps it"], a: 0, why: "Flips." },
  { q: "AND #1 isolates:", opts: ["The least significant bit", "The most significant bit", "The whole byte", "The carry"], a: 0, why: "LSB." },
  { q: "The operand &12 is:", opts: ["Hexadecimal", "Binary", "Denary", "An address"], a: 0, why: "& = hex." },
] });
Lib.cards($("#fc1"), { cards: [
  ["LSL / LSR", "Logical shifts; zeros enter."],
  ["AND", "Clear or test bits."],
  ["OR", "Set bits."],
  ["XOR", "Flip bits."],
  ["#n / Bn / &n", "Denary / binary / hex operand."],
  ["Clear a register", "AND B00000000."],
  ["Odd test", "AND #1, compare with 1."],
  ["8 bits", "Always write all eight."],
] });
