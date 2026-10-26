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
  if (x === 0) return { m: "0".repeat(mb), e: "0".repeat(eb), exact: true, ev: 0 };
  const mag = Math.abs(x); let e = 0, m = mag;
  while (m >= 1) { m /= 2; e++; } while (m < 0.5) { m *= 2; e--; }
  const scaled = m * 2 ** (mb - 1), pos = Math.floor(scaled), exact = scaled === pos, mi = x > 0 ? pos : 2 ** mb - pos;
  const tw = (n, b) => (n < 0 ? n + 2 ** b : n).toString(2).padStart(b, "0");
  return { m: tw(mi, mb), e: tw(e, eb), exact, ev: e };
}
const tw2 = (n, b) => (n < 0 ? n + 2 ** b : n).toString(2).padStart(b, "0");

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); const sh = [0, 1, 3, 6][k], m = ("0000000111" + "000000").slice(sh, sh + 10), e = tw2(val2("100111") - sh, 6);
    let o = SV.text(30, 22, "Mantissa", "sm") + SV.text(430, 22, "Exponent", "sm");
    m.split("").forEach((c, i) => (o += SV.rect(30 + i * 34, 30, 30, 36, i < 2 ? (m[0] !== m[1] ? "cell-ok" : "cell-no") : "f3", { rx: 4 }) + SV.text(45 + i * 34, 55, c, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px" })));
    e.split("").forEach((c, i) => (o += SV.rect(430 + i * 34, 30, 30, 36, "f2", { rx: 4 }) + SV.text(445 + i * 34, 55, c, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px" })));
    o += SV.text(30, 100, m[0] !== m[1] ? "starts " + m[0] + m[1] + ": NORMALISED" : "starts " + m[0] + m[1] + ": not normalised", "lbl bd " + (m[0] !== m[1] ? "t3" : "t2"), { style: "font-size:16px" });
    o += SV.text(430, 100, "exponent = " + val2(e), "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    if (sh) o += SV.text(30, 140, sh + " shift" + (sh > 1 ? "s" : "") + " left, so the exponent drops by " + sh + " (from −25)", "lbl", { style: "font-size:15px" });
    if (k === 3) o += SV.text(30, 178, "value unchanged: 0.0000000111 × 2^-25 = 0.111 × 2^-31", "lbl bd t3", { style: "font-family:var(--mono);font-size:15px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 205, label: "Shifting a mantissa until it is normalised", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "Mantissa <code>0000000111</code>, exponent <code>100111</code> (−25). The mantissa starts 00, so the leading zeros are wasted: it is <b>not normalised</b>.", s: { i: 0 } },
    { cap: "Shift the mantissa <b>1 place left</b>. Each shift doubles the mantissa, so the exponent is reduced by 1 to keep the value the same.", s: { i: 1 } },
    { cap: "After 3 shifts it still starts 00. The exponent is −28.", s: { i: 2 } },
    { cap: "After <b>6</b> shifts the mantissa starts <b>01</b>: normalised. The exponent is −25 − 6 = −31 (<code>100001</code>).", s: { i: 3 } }] });
})();

(function () {
  const al = [[12, 4], [10, 6], [8, 8]];
  const draw = (s) => {
    const k = Math.round(s.i), [mb, eb] = al[k], E = 2 ** (eb - 1); let o = "";
    for (let i = 0; i < 16; i++) o += SV.rect(30 + i * 28, 30, 24, 34, i < mb ? "f3" : "f2", { rx: 4 }) + SV.text(42 + i * 28, 52, i < mb ? "M" : "E", "lbl bd", { "text-anchor": "middle", style: "font-size:13px" });
    o += SV.text(30, 90, mb + " bits mantissa (precision)", "lbl bd", { style: "font-size:14px" }) + SV.text(430, 90, eb + " bits exponent (range)", "lbl bd", { style: "font-size:14px" });
    o += SV.rect(30, 110, mb * 30, 20, "f3", { rx: 4, ...op(0.8) }) + SV.text(30, 150, "precision", "sm");
    o += SV.rect(30, 164, eb * 38, 20, "f2", { rx: 4, ...op(0.8) }) + SV.text(30, 204, "range", "sm");
    o += SV.text(430, 130, "largest ≈ 2^" + (E - 1), "lbl", { style: "font-family:var(--mono);font-size:15px" }) + SV.text(430, 160, "smallest ≈ 2^-" + (E + 1), "lbl", { style: "font-family:var(--mono);font-size:15px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 215, label: "Sharing 16 bits", base: { i: 0 }, draw, tween: 300, dwell: 3200, steps: [
    { cap: "<b>12 + 4</b>: lots of precision, but the 4-bit exponent only reaches 2<sup>7</sup> = 128: a small range.", s: { i: 0 } },
    { cap: "<b>10 + 6</b>: two bits move from the mantissa to the exponent. The range becomes huge (up to 2<sup>31</sup>) but each number has fewer digits of precision.", s: { i: 1 } },
    { cap: "<b>8 + 8</b>: the exponent reaches 2<sup>127</sup>, but with only 7 digits after the sign bit the numbers are rough approximations. Precision and range trade off.", s: { i: 2 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.line(40, 100, 720, 100, "ax");
    o += SV.rect(240, 70, 280, 60, "f3", { rx: 6, ...op(0.55) }) + SV.text(380, 124, "range that can be stored", "lbl bd", { "text-anchor": "middle" });
    o += SV.text(240, 150, "-largest", "sm", { "text-anchor": "middle" }) + SV.text(520, 150, "+largest", "sm", { "text-anchor": "middle" }) + SV.text(380, 150, "0", "sm", { "text-anchor": "middle" });
    if (k >= 1) o += SV.circle(640, 100, 12, "dot2") + SV.text(640, 70, "214.75", "lbl bd t2", { "text-anchor": "middle" }) + SV.text(640, 175, "OVERFLOW: beyond +127.9375", "lbl bd t2", { "text-anchor": "middle" });
    if (k >= 2) o += SV.circle(380, 100, 5, "dot1") + SV.text(380, 55, "1.0 × 10^-12 → 0", "lbl bd t2", { "text-anchor": "middle" }) + SV.text(380, 200, "UNDERFLOW: closer to 0 than the smallest number", "lbl bd t2", { "text-anchor": "middle" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 215, label: "Overflow and underflow", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "A system can only store numbers within a range. In 12 + 4 bits the largest is 127.9375.", s: { i: 0 } },
    { cap: "<b>Overflow</b>: 91.5 + 123.25 = 214.75 is too large. It needs an exponent of 8, which does not fit. The most significant bits are lost.", s: { i: 1 } },
    { cap: "<b>Underflow</b>: a result very close to zero, smaller than the smallest storable number, is stored as zero.", s: { i: 2 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 28, "0.1 in binary", "lbl bd", { style: "font-size:16px" });
    o += SV.text(30, 64, "0.000110011001100110011...  (recurring)", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 1) o += SV.text(30, 100, "normalised: 0.110011001100... × 2^-3", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 2) o += SV.text(30, 136, "12-bit mantissa keeps:   011001100110   (the rest is cut off)", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 3) o += SV.text(30, 172, "stored value = 0.0999755859", "lbl bd t2", { style: "font-family:var(--mono);font-size:16px" }) + SV.text(30, 200, "not 0.1: a rounding error of about −0.0000244", "sm");
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 215, label: "A rounding error", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "0.1 is easy in denary but in <b>binary</b> it recurs: 0.0001100110011... It cannot be written as a finite sum of ½, ¼, ⅛...", s: { i: 0 } },
    { cap: "Normalised, the mantissa digits are 1100110011... with exponent −3.", s: { i: 1 } },
    { cap: "A 12-bit mantissa can only keep the first digits: the rest is <b>truncated</b>.", s: { i: 2 } },
    { cap: "The stored value is a little less than 0.1. A <b>rounding error</b> appears, and it can build up over many calculations.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  const pre = [["0000000111", "100111"], ["00011110", "00011000"], ["11110000", "000100"], ["00000001", "000011"]]; let cur = 0, m, e, n;
  const reset = () => { m = pre[cur][0]; e = pre[cur][1]; n = 0; paint(); };
  const paint = () => {
    $$("#nB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const norm = m[0] !== m[1];
    $("#nS").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Mantissa</th><th>Exponent</th><th>Value</th><th>Normalised?</th></tr><tr><td>' + m + "</td><td>" + e + " (" + val2(e) + ")</td><td>" + +decodeFp(m, e).toPrecision(12) + "</td><td>" + (norm ? "yes: starts " + m[0] + m[1] : "no: starts " + m[0] + m[1]) + "</td></tr></table></div>";
    $("#nV").textContent = norm ? "Normalised after " + n + " shift" + (n === 1 ? "" : "s") + ". The value is unchanged." : "Shift left; the exponent will drop by 1 each time. Shifts so far: " + n + ".";
  };
  $("#nB").innerHTML = pre.map((p, i) => `<button class="b" data-i="${i}">${p[0]} | ${p[1]}</button>`).join("");
  $$("#nB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; reset(); }));
  $("#nL").onclick = () => { if (m[0] !== m[1]) return; if (parseInt(m, 2) === 0 || /^(0+|1+)$/.test(m)) { $("#nV").textContent = "A mantissa of all 0s or all 1s cannot be normalised."; return; } m = m.slice(1) + "0"; e = tw2(val2(e) - 1, e.length); n++; paint(); };
  $("#nR").onclick = reset; reset();
})();

/* Lab 2 */
(function () {
  let mb = 10;
  const paint = () => {
    const eb = 16 - mb, E = 2 ** (eb - 1), big = (1 - 2 ** -(mb - 1)) * 2 ** (E - 1), small = 2 ** -(E + 1);
    $("#s1").textContent = big.toExponential(3) + "  (2^" + (E - 1) + ")"; $("#s2").textContent = small.toExponential(3) + "  (2^-" + (E + 1) + ")"; $("#s3").textContent = (2 ** -(mb - 1)).toExponential(2) + " (spacing 2^-" + (mb - 1) + ")";
    $("#sV").textContent = mb + " bits for the mantissa and " + eb + " for the exponent. " + (mb >= 11 ? "High precision, small range." : mb <= 8 ? "Large range, low precision." : "A balance of range and precision.");
  };
  Lib.slider($("#sS"), { id: "sss", label: "Bits for the mantissa (the rest go to the exponent) ", min: 6, max: 13, value: mb, fmt: (x) => x + " + " + (16 - x), onInput: (v) => { mb = v; paint(); } });
  paint();
})();

/* Lab 3 */
(function () {
  const al = [[12, 4], [10, 6], [8, 8]]; let cur = 0;
  const run = () => {
    $$("#rB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const x = parseFloat($("#rN").value); if (isNaN(x)) { $("#rO").innerHTML = ""; $("#rV").textContent = "Enter a number."; return; }
    const [mb, eb] = al[cur], r = encodeFp(x, mb, eb), v = decodeFp(r.m, r.e), maxE = 2 ** (eb - 1);
    const outOfRange = r.ev > maxE - 1 || r.ev < -maxE;
    $("#rO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Mantissa</th><th>Exponent</th><th>Stored value</th><th>Error</th></tr><tr><td>' + r.m + "</td><td>" + r.e + "</td><td>" + +v.toPrecision(14) + "</td><td>" + +(v - x).toPrecision(4) + "</td></tr></table></div>";
    $("#rV").textContent = outOfRange ? "The exponent needed (" + r.ev + ") does not fit in " + eb + " bits: overflow or underflow." : r.exact ? "Stored exactly: the number is a sum of powers of 2 that fits in the mantissa." : "Not stored exactly: the stored value is the nearest the mantissa can hold, so there is a rounding error.";
  };
  $("#rB").innerHTML = al.map((a) => `<button class="b">${a[0]} + ${a[1]} bits</button>`).join("");
  $$("#rB button").forEach((b, i) => (b.onclick = () => { cur = i; run(); }));
  $("#rE").innerHTML = ["0.1", "0.25", "0.3", "65.2", "1000000"].map((v) => `<button class="b">${v}</button>`).join("");
  $$("#rE button").forEach((b) => (b.onclick = () => { $("#rN").value = b.textContent; run(); }));
  $("#rR").onclick = run; $("#rN").addEventListener("keydown", (ev) => { if (ev.key === "Enter") run(); });
  run();
})();
Lib.classify($("#cl1"), { prompt: "Is each mantissa normalised?", buckets: [{"label": "Normalised"}, {"label": "Not normalised"}], items: [{"text": "0110100000", "b": 0}, {"text": "1001100000", "b": 0}, {"text": "0011010000", "b": 1}, {"text": "1101100000", "b": 1}, {"text": "01000000", "b": 0}, {"text": "00000011", "b": 1}, {"text": "10000000", "b": 0}, {"text": "11100000", "b": 1}], done: "Normalised: the first two bits differ (01 or 10)." });
Lib.classify($("#cl2"), { prompt: "Which change gives this effect?", buckets: [{"label": "More mantissa bits"}, {"label": "More exponent bits"}], items: [{"text": "Greater precision", "b": 0}, {"text": "A larger range of numbers", "b": 1}, {"text": "More significant digits stored", "b": 0}, {"text": "A larger largest number", "b": 1}, {"text": "Smaller rounding errors", "b": 0}, {"text": "A smaller smallest positive number", "b": 1}], done: "Mantissa: precision. Exponent: range." });
Lib.order($("#o1"), { prompt: "Put the steps for normalising a mantissa in order.", items: ["Check the first two bits of the mantissa", "If they are the same, shift the mantissa left one place", "Reduce the exponent by 1", "Repeat until the first two bits differ", "Write the new mantissa and exponent"], done: "Check, shift, lower the exponent, repeat, write." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Normalised", "Mantissa starts 01 or 10"], ["Overflow", "A result too large to be stored"], ["Underflow", "A result closer to zero than the smallest storable number"], ["Rounding error", "The difference between a number and its stored approximation"], ["Truncated", "Least significant bits that do not fit are lost"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Mantissa 00011000 is shifted left until it is normalised. How many shifts are needed?", "a": 2, "unit": "", "tol": 0.01, "hint": "00011000 → 00110000 → 01100000.", "sol": "<b>2</b> shifts."},
  {"q": "The exponent is 5 before 3 shifts left are made to normalise. What is it after?", "a": 2, "unit": "", "tol": 0.01, "hint": "5 − 3.", "sol": "<b>2</b>."},
  {"q": "The exponent is −25 and the mantissa needs 6 shifts. What is the new exponent?", "a": -31, "unit": "", "tol": 0.01, "hint": "−25 − 6.", "sol": "<b>−31</b>."},
  {"q": "What is the largest positive value with a 12-bit mantissa and a 4-bit exponent? (1 − 2^-11) × 2^7, to 4 decimal places.", "a": 127.9375, "unit": "", "tol": 0.001, "hint": "128 − 0.0625.", "sol": "<b>127.9375</b>."},
  {"q": "The largest value is 127.9375. Does 91.5 + 123.25 (= 214.75) overflow? Enter 1 for yes, 0 for no.", "a": 1, "unit": "", "tol": 0.01, "hint": "214.75 > 127.9375.", "sol": "<b>1</b>: yes."},
  {"q": "How many bits does a 10-bit mantissa system with a 6-bit exponent use in total?", "a": 16, "unit": "bits", "tol": 0.01, "hint": "10 + 6.", "sol": "<b>16</b> bits."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A normalised positive mantissa starts...", opts: ["00", "01", "10", "11"], a: 1, why: "01: 0.1..." },
  { q: "Increasing the bits for the exponent...", opts: ["increases precision", "increases range", "decreases range", "does nothing"], a: 1, why: "More exponent bits means a larger range (and, with a fixed total, less precision)." },
  { q: "What is overflow?", opts: ["A result too small to store", "A result too large to store", "A file that is too big", "Memory running out"], a: 1, why: "The most significant bits are lost." },
  { q: "Why is 0.1 only an approximation in binary?", opts: ["It is negative", "It is a recurring binary fraction cut off by the mantissa", "It is too large", "It is an integer"], a: 1, why: "A finite mantissa cannot hold a recurring fraction." },
  { q: "Why are numbers normalised?", opts: ["To make them negative", "To maximise precision and give one representation", "To save the file", "To add a sign bit"], a: 1, why: "No wasted leading bits." },
  { q: "What happens to the exponent when the mantissa is shifted left once?", opts: ["It increases by 1", "It decreases by 1", "It is unchanged", "It doubles"], a: 1, why: "To keep the value the same." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Normalised", "Mantissa starts 01 or 10: no wasted leading bits."],
  ["Normalising", "Shift mantissa left until first two bits differ; subtract the shifts from the exponent."],
  ["More mantissa bits", "More precision, smaller range."],
  ["More exponent bits", "Larger range, less precision."],
  ["Overflow", "Result too large to store."],
  ["Underflow", "Result too small: stored as zero."],
  ["Rounding error", "Stored value differs from the real number: binary cannot hold it exactly."],
  ["Fix", "Compare with a tolerance; store money as integers."],
] });
