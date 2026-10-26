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

const val2 = (s) => { const n = parseInt(s, 2); return s[0] === "1" ? n - 2 ** s.length : n; };
const decodeFp = (m, e) => (val2(m) / 2 ** (m.length - 1)) * 2 ** val2(e);
function encodeFp(x, mb, eb) {
  if (x === 0) return { m: "0".repeat(mb), e: "0".repeat(eb), exact: true };
  const mag = Math.abs(x); let e = 0, m = mag;
  while (m >= 1) { m /= 2; e++; } while (m < 0.5) { m *= 2; e--; }
  const scaled = m * 2 ** (mb - 1), pos = Math.floor(scaled), exact = scaled === pos;
  let mi = x > 0 ? pos : 2 ** mb - pos;
  const tw = (n, b) => (n < 0 ? n + 2 ** b : n).toString(2).padStart(b, "0");
  return { m: tw(mi, mb), e: tw(e, eb), exact, ev: e, mag };
}

(function () {
  const M = "1011000111", E = "000111";
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const boxes = (str, x0, cls) => str.split("").map((c, i) => SV.rect(x0 + i * 34, 30, 30, 36, cls, { rx: 4 }) + SV.text(x0 + i * 34 + 15, 55, c, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px" })).join("");
    o += SV.text(30, 22, "Mantissa", "sm") + SV.text(430, 22, "Exponent", "sm") + boxes(M, 30, "f3") + boxes(E, 430, "f2");
    if (k >= 1) o += SV.text(430, 96, "exponent 000111 = 7", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 2) o += SV.text(30, 96, "mantissa 1.011000111   (point after the first bit)", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 3) o += SV.text(30, 132, "move the point 7 places right:   10110001.11", "lbl bd t3", { style: "font-family:var(--mono);font-size:16px" });
    if (k >= 4) o += SV.text(30, 168, "−128 + 32 + 16 + 1 + 0.5 + 0.25", "lbl", { style: "font-family:var(--mono);font-size:16px" });
    if (k >= 5) o += SV.text(30, 204, "value = −78.25", "lbl bd t3", { style: "font-family:var(--mono);font-size:22px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 225, label: "Converting floating-point to denary", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "The 16 bits are a 10-bit <b>mantissa</b> and a 6-bit <b>exponent</b>, both in two's complement.", s: { i: 0 } },
    { cap: "Convert the exponent: <code>000111</code> is <b>7</b>.", s: { i: 1 } },
    { cap: "The mantissa has its point after the first bit: <code>1.011000111</code>. It starts with 1, so the number is negative.", s: { i: 2 } },
    { cap: "Multiply by 2<sup>7</sup>: move the point <b>7 places right</b>. <code>1.011000111</code> becomes <code>10110001.11</code>.", s: { i: 3 } },
    { cap: "Add the place values. The first bit is a <b>negative</b> place value: −128 + 32 + 16 + 1 + 0.5 + 0.25.", s: { i: 4 } },
    { cap: "The value is <b>−78.25</b>.", s: { i: 5 } }] });
})();

(function () {
  const rows = [["7.25 in binary", "111.01"], ["Normalise: move the point 3 places left", "0.11101 × 2^3,  exponent = 3"], ["Positive mantissa (10 bits)", "0111010000"], ["Negative: invert the bits", "1000101111"], ["Add 1", "1000110000"], ["Exponent 3 in 6 bits", "000011"], ["Answer", "1000110000   000011"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "Convert −7.25: 10-bit mantissa, 6-bit exponent", "lbl bd");
    rows.forEach((r, i) => { const v = i < k ? 1 : 0; if (!v) return; o += SV.rect(30, 38 + i * 34, 700, 30, i === rows.length - 1 ? "cell-ok" : "cell", { rx: 6 }) + SV.text(44, 59 + i * 34, r[0], "lbl", { style: "font-size:14px" }) + SV.text(330, 59 + i * 34, r[1], "lbl bd", { style: "font-family:var(--mono);font-size:15px" }); });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 285, label: "Denary to floating-point", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "Convert <b>−7.25</b> to floating-point. First ignore the sign.", s: { i: 0 } },
    { cap: "7.25 in binary: 7 is 111 and 0.25 is .01, so <b>111.01</b>.", s: { i: 1 } },
    { cap: "Normalise to 0.1...: move the point 3 places left. That is <b>× 2³</b>, so the exponent is 3.", s: { i: 2 } },
    { cap: "The positive mantissa has a 0 sign bit and the digits, padded with zeros to 10 bits.", s: { i: 3 } },
    { cap: "The number is negative, so take the <b>two's complement</b> of the mantissa. Invert every bit...", s: { i: 4 } },
    { cap: "...then add 1. The mantissa is now 1000110000. It starts with <b>10</b>, as a normalised negative mantissa does.", s: { i: 5 } },
    { cap: "The exponent does not change: 3 in 6-bit two's complement is 000011.", s: { i: 6 } },
    { cap: "The answer, mantissa then exponent: <b>1000110000 000011</b>.", s: { i: 7 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); const vals = ["0.1011", "1.011", "10.11", "101.1", "1011."], dec = ["0.6875", "1.375", "2.75", "5.5", "11"];
    let o = SV.text(30, 26, "mantissa 0.1011 (0.6875)", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    o += SV.text(30, 76, "× 2^" + k, "lbl bd", { style: "font-family:var(--mono);font-size:22px" });
    o += SV.text(30, 130, "move the point " + k + " place" + (k === 1 ? "" : "s") + " right", "lbl", { style: "font-size:15px" });
    o += SV.text(30, 180, vals[k] + "  =  " + dec[k], "lbl bd t3", { style: "font-family:var(--mono);font-size:26px" });
    for (let i = 0; i <= 4; i++) o += SV.rect(430 + i * 62, 40, 54, 50, i === k ? "cell-ok" : "cell", { rx: 6 }) + SV.text(457 + i * 62, 70, "2^" + i, "lbl", { "text-anchor": "middle", style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 215, label: "The exponent as a shift of the binary point", base: { i: 0 }, draw, tween: 200, dwell: 2200, steps: [0, 1, 2, 3, 4].map((i) => ({ cap: i === 0 ? "A mantissa of 0.1011 is 0.5 + 0.125 + 0.0625 = <b>0.6875</b>. With exponent 0 the value is unchanged." : `Exponent ${i}: multiply by 2<sup>${i}</sup>, which moves the binary point <b>${i}</b> place${i > 1 ? "s" : ""} to the right. The value is ${["", "1.375", "2.75", "5.5", "11"][i]}. Each increase of 1 in the exponent doubles the value.`, s: { i } })) });
})();

/* Lab 1 */
(function () {
  const alloc = [[10, 6], [12, 4], [8, 8]]; let cur = 0, m = "1011000111", e = "000111";
  const paint = () => {
    $$("#fB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const bits = (str, id, w) => { $("#" + id).innerHTML = '<span style="align-self:center;margin-right:6px">' + (id === "fM" ? "Mantissa" : "Exponent") + "</span>" + str.split("").map((c, i) => `<button class="b${c === "1" ? " pri" : ""}" data-i="${i}" style="min-width:2.2em;font-family:var(--mono)">${c}</button>`).join(""); $$("#" + id + " button").forEach((b) => (b.onclick = () => { const i = +b.dataset.i, arr = (id === "fM" ? m : e).split(""); arr[i] = arr[i] === "1" ? "0" : "1"; if (id === "fM") m = arr.join(""); else e = arr.join(""); paint(); })); };
    bits(m, "fM"); bits(e, "fE");
    const ev = val2(e), v = decodeFp(m, e), pt = 1 + ev;
    $("#f1").textContent = ev; $("#f2").textContent = m[0] + "." + m.slice(1); $("#f3").textContent = String(+v.toPrecision(12));
    let ipb, fpb; if (pt >= m.length) { ipb = m + "0".repeat(pt - m.length); fpb = ""; } else if (pt <= 0) { ipb = "0"; fpb = "0".repeat(-pt) + m; } else { ipb = m.slice(0, pt); fpb = m.slice(pt); }
    $("#fW").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Step</th><th>Working</th></tr><tr><td>Exponent</td><td>' + e + " = " + ev + "</td></tr><tr><td>Mantissa</td><td>" + m[0] + "." + m.slice(1) + (m[0] === "1" ? " (negative)" : " (positive)") + "</td></tr><tr><td>Move the point " + Math.abs(ev) + (ev >= 0 ? " places right" : " places left") + "</td><td>" + ipb + (fpb ? "." + fpb : "") + "</td></tr><tr><td>Normalised?</td><td>" + (m[0] !== m[1] ? "yes (starts " + m[0] + m[1] + ")" : "no: the mantissa starts " + m[0] + m[1]) + "</td></tr></table></div>";
  };
  $("#fB").innerHTML = alloc.map((a) => `<button class="b">${a[0]} + ${a[1]} bits</button>`).join("");
  $$("#fB button").forEach((b, i) => (b.onclick = () => { cur = i; m = ["1011000111", "010111000110", "01110001"][i]; e = ["000111", "0111", "00000111"][i]; paint(); })); paint();
})();

/* Lab 2 */
(function () {
  const alloc = [[10, 6], [12, 4], [8, 8]]; let cur = 0;
  const run = () => {
    $$("#gB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const x = parseFloat($("#gN").value), [mb, eb] = alloc[cur];
    if (isNaN(x)) { $("#gW").innerHTML = ""; $("#gV").textContent = "Enter a number."; return; }
    const r = encodeFp(x, mb, eb), back = decodeFp(r.m, r.e), mag = Math.abs(x);
    const maxE = 2 ** (eb - 1) - 1, over = r.ev !== undefined && (r.ev > maxE || r.ev < -(maxE + 1));
    const bin = (() => { let ip = Math.floor(mag), fr = mag - ip, s = ip.toString(2), f = ""; for (let i = 0; i < 20 && fr > 0; i++) { fr *= 2; f += fr >= 1 ? "1" : "0"; fr -= Math.floor(fr); } return s + (f ? "." + f : ""); })();
    $("#gW").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Step</th><th>Working</th></tr><tr><td>Binary of ' + mag + "</td><td>" + bin + "</td></tr><tr><td>Exponent</td><td>" + (r.ev === undefined ? "0" : r.ev) + " → " + r.e + "</td></tr><tr><td>Mantissa</td><td>" + r.m + (x < 0 ? " (two's complement of the positive mantissa)" : "") + "</td></tr><tr><td>Answer</td><td><b>" + r.m + "  " + r.e + "</b></td></tr><tr><td>Converted back</td><td>" + +back.toPrecision(12) + "</td></tr></table></div>";
    $("#gV").textContent = over ? "The exponent does not fit in " + eb + " bits: this number is outside the range of this system (overflow or underflow)." : r.exact ? "Stored exactly." : "The number needs more bits than the " + mb + "-bit mantissa has, so the last bits are lost: the stored value is " + +back.toPrecision(12) + ", an approximation.";
  };
  $("#gB").innerHTML = alloc.map((a) => `<button class="b">${a[0]} + ${a[1]} bits</button>`).join("");
  $$("#gB button").forEach((b, i) => (b.onclick = () => { cur = i; run(); })); $("#gR").onclick = run; $("#gN").addEventListener("keydown", (e) => { if (e.key === "Enter") run(); });
  run();
})();

btnTable("eB", "eO", [
  ["Mantissa", "A two's complement fraction with the binary point after the first bit; holds the digits of the number", "Normalised: starts 01 (positive) or 10 (negative)", "More mantissa bits: more precision"],
  ["Exponent", "A two's complement integer: the power of 2 the mantissa is multiplied by", "Positive moves the point right; negative moves it left", "More exponent bits: larger range"],
  ["Value", "mantissa × 2^exponent", "Example: 0.1011 × 2^3 = 5.5", "Check by converting back"]
], ["Part", "What it is", "Detail", "Effect of more bits"]);
Lib.classify($("#cl1"), { prompt: "Does each statement describe the mantissa or the exponent?", buckets: [{"label": "Mantissa"}, {"label": "Exponent"}], items: [{"text": "Holds the digits of the number", "b": 0}, {"text": "Says how many places to move the binary point", "b": 1}, {"text": "Has the binary point after its first bit", "b": 0}, {"text": "A two's complement integer", "b": 1}, {"text": "More bits here increase precision", "b": 0}, {"text": "More bits here increase the range", "b": 1}], done: "Mantissa: the digits and precision. Exponent: the scale and range." });
Lib.classify($("#cl2"), { prompt: "Which way does the binary point move (and what is the exponent's sign)?", buckets: [{"label": "Right (positive exponent)"}, {"label": "Left (negative exponent)"}], items: [{"text": "Converting 0.101 × 2^4 to denary", "b": 0}, {"text": "Normalising 0.000111 (a small number)", "b": 0}, {"text": "Converting 0.101 × 2^(-2) to denary", "b": 1}, {"text": "Writing 111.01 as 0.11101 × 2^3: the point moves left, exponent +3", "b": 0}, {"text": "A very small number: the normalised exponent", "b": 1}, {"text": "A large number such as 202 when normalised", "b": 0}], done: "Evaluating with a positive exponent moves the point right. A very small number needs a negative exponent." });
Lib.order($("#o1"), { prompt: "Put the steps for converting −7.25 to floating-point in order.", items: ["Convert 7.25 to binary: 111.01", "Normalise: 0.11101 × 2^3, so the exponent is 3", "Write the positive mantissa: 0111010000", "Invert the bits and add 1: 1000110000", "Write the exponent 3 in two's complement: 000011"], done: "Binary, normalise, mantissa, negate, exponent." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Mantissa", "The digits of the number, a two's complement fraction"], ["Exponent", "The power of 2 that scales the mantissa"], ["Floating point", "A real number stored as a mantissa and an exponent"], ["Two's complement", "Representation where the first bit has a negative place value"], ["Normalised", "The mantissa starts 01 or 10"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Exponent 000111 in 6-bit two's complement. What is its denary value?", "a": 7, "unit": "", "tol": 0.01, "hint": "4 + 2 + 1.", "sol": "<b>7</b>."},
  {"q": "Exponent 111110 in 6-bit two's complement. What is its denary value?", "a": -2, "unit": "", "tol": 0.01, "hint": "−32 + 16 + 8 + 4 + 2.", "sol": "<b>−2</b>."},
  {"q": "Mantissa 0.1 (binary) with exponent 3. What is the value?", "a": 4, "unit": "", "tol": 0.01, "hint": "0.5 × 8.", "sol": "<b>4</b>."},
  {"q": "Mantissa 0.11 (binary) with exponent 2. What is the value?", "a": 3, "unit": "", "tol": 0.01, "hint": "0.75 × 4.", "sol": "<b>3</b>."},
  {"q": "Mantissa 0100111100 with exponent 001001. What is the denary value?", "a": 316, "unit": "", "tol": 0.01, "hint": "Move the point 9 places: 100111100.", "sol": "<b>316</b>."},
  {"q": "Mantissa 1011000111 with exponent 000111. What is the denary value?", "a": -78.25, "unit": "", "tol": 0.01, "hint": "10110001.11 = −128 + 32 + 16 + 1 + 0.5 + 0.25.", "sol": "<b>−78.25</b>."},
  {"q": "In 8-bit two's complement, what is the denary value of 10011011?", "a": -101, "unit": "", "tol": 0.01, "hint": "−128 + 16 + 8 + 2 + 1.", "sol": "<b>−101</b>."},
  {"q": "A floating-point system has 12 bits for the mantissa and 4 for the exponent. How many bytes does one number use?", "a": 2, "unit": "bytes", "tol": 0.01, "hint": "16 bits.", "sol": "<b>2</b> bytes."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Where is the binary point in a floating-point mantissa?", opts: ["At the far right", "After the first bit", "In the middle of the exponent", "It has no point"], a: 1, why: "The mantissa is a fraction with the point after the first bit." },
  { q: "A mantissa starting with 1 is...", opts: ["positive", "negative", "zero", "not normalised"], a: 1, why: "In two's complement a leading 1 means negative." },
  { q: "To negate a mantissa you...", opts: ["add 1 to the exponent", "invert the bits and add 1", "remove the first bit", "double it"], a: 1, why: "Two's complement." },
  { q: "What does a positive exponent do?", opts: ["Moves the point right", "Moves the point left", "Makes the number negative", "Nothing"], a: 0, why: "It multiplies by a power of 2." },
  { q: "How is a negative number converted to floating point?", opts: ["Negate the mantissa and the exponent", "Convert the positive number, then take the two's complement of the mantissa only", "Subtract from 1", "Use a sign bit in the exponent"], a: 1, why: "The exponent is the same as for the positive number." },
  { q: "0.11101 × 2³ equals...", opts: ["7.25", "3.625", "7", "14.5"], a: 0, why: "111.01 = 7.25." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Floating point", "Mantissa × 2^exponent, both in two's complement."],
  ["Mantissa", "Fraction with the point after the first bit; holds the digits."],
  ["Exponent", "Integer power of 2. Positive moves the point right."],
  ["Denary to float", "Binary, normalise, mantissa, negate if negative, exponent."],
  ["Float to denary", "Exponent, move the point, add place values."],
  ["Negative mantissa", "Invert bits, add 1. Exponent unchanged."],
  ["Normalised", "Mantissa starts 01 or 10."],
  ["Truncation", "Bits that do not fit are lost: precision reduced."],
] });
