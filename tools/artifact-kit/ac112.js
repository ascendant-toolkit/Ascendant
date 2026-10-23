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

/* column adder: rows a, b, result with carries; k columns done */
function addSteps(el, a, b, label, sub) {
  const n = a.length, res = [], car = Array(n + 1).fill(0), why = [];
  let c = 0;
  for (let j = n - 1; j >= 0; j--) { const s = +a[j] + +b[j] + c, w = s % 2, co = s >> 1; res[j] = w; car[j] = co; why[n - 1 - j] = `Column ${n - j}: ${a[j]} + ${b[j]}${c ? " + carry 1" : ""} = ${s.toString(2)}. Write <b>${w}</b>${co ? ", carry <b>1</b> to the next column" : ", no carry"}.`; c = co; }
  const out = c, total = parseInt(a, 2) + parseInt(b, 2);
  const draw = (s) => {
    const X0 = 60, W = 64, G = 16; let o = "";
    o += SV.text(24, 134, "+", "lbl bd", { "text-anchor": "middle", style: "font-size:26px" }) + SV.line(40, 160, 730, 160, "ax");
    o += boxRow(a.split("").map((t) => ({ t, c: "f1" })), X0, 62, W, 44, G, { fs: 20 });
    o += boxRow(b.split("").map((t) => ({ t, c: "f1" })), X0, 112, W, 44, G, { fs: 20 });
    for (let j = 0; j < n; j++) {
      const k = n - 1 - j, v = clamp01(s.k - k), x = X0 + j * (W + G);
      if (v > 0) o += boxRow([{ t: res[j], c: "f2", v }], x, 168, W, 44, 0, { fs: 20 });
      if (v > 0 && car[j] && j > 0) o += SV.text(X0 + (j - 1) * (W + G) + W / 2, 52, "1", "lbl bd t3", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:16px", ...op(v) });
    }
    if (s.k > 0 && s.k < n + 0.5) { const j = n - Math.max(1, Math.min(n, Math.ceil(s.k))), x = X0 + j * (W + G); o += SV.rect(x - 6, 56, W + 12, 160, "f3", { rx: 10, style: "fill:none;stroke:var(--accent);stroke-width:2.5px" }); }
    if (s.k >= n && out) o += SV.text(X0 - 30, 196, "1", "lbl bd t3", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:22px" }) + SV.text(X0 - 30, 218, "lost", "sm", { "text-anchor": "middle" });
    o += SV.text(40, 40, "carries", "sm");
    return o;
  };
  const steps = [{ cap: `Write the two numbers in columns, one above the other. Start at the <b>right-most</b> column and write any carry above the next column. ${sub || ""}`, s: { k: 0 } }];
  for (let k = 0; k < n; k++) steps.push({ cap: why[k], s: { k: k + 1 } });
  steps.push({ cap: out ? `The result is <b>${res.join("")}</b> after dropping the ninth bit. The true total is ${total}, which is more than ${2 ** n - 1}, so <b>overflow</b> has occurred.` : `Result: <b>${res.join("")}</b> = ${total}. No carry out of the left-most column, so no overflow.`, s: { k: n + 1 } });
  Lib.stepper($(el), { w: 760, h: 236, label, base: { k: 0 }, draw, tween: 500, dwell: 3400, steps });
}
addSteps("#stA", "10110000", "00011011", "Adding 10110000 and 00011011 column by column", "Here 176 + 27 = 203.");
addSteps("#stC", "01101011", "11100010", "Adding 01101011 and the two's complement of 30", "This is 107 − 30, done by adding −30 (1110 0010).");
addSteps("#stD", "11000000", "01000000", "Overflow when adding 11000000 and 01000000", "192 + 64 = 256.");

(function () {
  const n = 30, p = bin(n), f = p.split("").map((x) => (x === "1" ? "0" : "1")).join(""), r = bin((~n + 1) & 255);
  const draw = (s) => {
    const row = (str, y, c, v, lab) => (v > 0 ? SV.text(20, y + 28, lab, "sm", op(v)) + boxRow(str.split("").map((t) => ({ t, c, v })), 80, y, 64, 44, 16, { fs: 20 }) : "");
    let o = row(p, 20, "f1", 1, "30");
    o += row(f, 86, "f3", clamp01(s.a), "flip");
    o += row(r, 152, "f2", clamp01(s.b), "+ 1");
    if (s.c > 0) o += SV.text(380, 226, "= −30 in 8-bit two's complement", "lbl bd t3", { "text-anchor": "middle", ...op(clamp01(s.c)) });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 244, label: "Making -30 in two's complement", base: { a: 0, b: 0, c: 0 }, draw, tween: 600, dwell: 4200, steps: [
    { cap: "Write the positive number in the full width: 30 = <b>" + p + "</b>.", s: {} },
    { cap: "Flip every bit (1 becomes 0, 0 becomes 1): <b>" + f + "</b>. This is the one's complement.", s: { a: 1 } },
    { cap: "Add 1: " + f + " + 1 = <b>" + r + "</b>.", s: { a: 1, b: 1 } },
    { cap: "Check by adding the column values with −128: −128 + 64 + 32 + 2 = −30.", s: { a: 1, b: 1, c: 1 } }] });
})();

/* Lab 1 */
Lib.slider($("#nb"), { id: "nbs", label: "Number of bits ", min: 2, max: 16, value: 8, fmt: (x) => x, onInput: (n) => {
  const u = 2 ** n - 1, t = 2 ** (n - 1);
  $("#n1").textContent = "0 to " + u.toLocaleString("en-GB"); $("#n2").textContent = -(t - 1) + " to " + (t - 1); $("#n3").textContent = -t + " to " + (t - 1);
  $("#nv").textContent = `${n} bits give ${(2 ** n).toLocaleString("en-GB")} different patterns. Two's complement splits them: ${t.toLocaleString("en-GB")} negative, zero, and ${(t - 1).toLocaleString("en-GB")} positive.`;
  $("#nS").innerHTML = SV.text(30, 36, "unsigned", "sm") + SV.rect(30, 44, 360, 24, "f1", { rx: 6, ...op(0.6) }) + SV.text(30, 88, "0", "sm") + SV.text(390, 88, u.toLocaleString("en-GB"), "sm", { "text-anchor": "end" })
    + SV.text(30, 124, "two's complement", "sm") + SV.rect(30, 132, 360, 24, "f2", { rx: 6, ...op(0.6) }) + SV.line(210, 128, 210, 162, "ax") + SV.text(30, 176, -t, "sm") + SV.text(210, 176, "0", "sm", { "text-anchor": "middle" }) + SV.text(390, 176, t - 1, "sm", { "text-anchor": "end" });
} });

/* Lab 2 */
Lib.slider($("#tcs"), { id: "tcv", label: "Denary value ", min: -128, max: 127, value: -30, fmt: (x) => x, onInput: (v) => {
  const s = bin(v & 255), pv = [-128, 64, 32, 16, 8, 4, 2, 1];
  $("#tc1").textContent = grp4(s); $("#tc2").textContent = pv.map((p, i) => (s[i] === "1" ? p : 0)).filter((x) => x).join(" + ").replace(/\+ -/g, "- ") || "0";
  $("#tcS").innerHTML = boxRow(s.split("").map((t, i) => ({ t, c: t === "1" ? (i === 0 ? "f3" : "f2") : "f1", top: pv[i] })), 60, 40, 64, 52, 16) + SV.text(380, 130, "= " + v, "lbl bd t3", { "text-anchor": "middle", style: "font-size:20px" });
} });

/* Lab 3 */
(function () {
  let A = 200, B = 100;
  const paint = () => {
    const sA = bin(A), sB = bin(B), t = A + B, r = bin(t & 255), sa = A > 127 ? A - 256 : A, sb = B > 127 ? B - 256 : B, rs = (t & 255) > 127 ? (t & 255) - 256 : t & 255;
    $("#a1").textContent = grp4(sA); $("#a2").textContent = grp4(sB); $("#a3").textContent = grp4(r); $("#a4").textContent = t;
    $("#av").textContent = t > 255 ? `Unsigned: ${A} + ${B} = ${t}, which is more than 255, so there is a carry out and an overflow. The stored result is ${t & 255}.` : `Unsigned: ${A} + ${B} = ${t}, which fits in 8 bits. No overflow.`;
    const ov = sa + sb !== rs;
    $("#av2").textContent = `Two's complement: ${sa} + ${sb} = ${sa + sb}. ${ov ? "That is outside −128 to 127, so it overflows and the 8 bits read as " + rs + "." : "That is inside −128 to 127, so the 8 bits read correctly as " + rs + "."}`;
  };
  Lib.slider($("#aA"), { id: "asA", label: "A ", min: 0, max: 255, value: A, fmt: (x) => x, onInput: (v) => { A = v; paint(); } });
  Lib.slider($("#aB"), { id: "asB", label: "B ", min: 0, max: 255, value: B, fmt: (x) => x, onInput: (v) => { B = v; paint(); } });
})();

/* Lab 4 */
(function () {
  let A = 107, B = 30;
  const paint = () => {
    const nb = (-B) & 255, t = A + nb, r = t & 255, rs = r > 127 ? r - 256 : r;
    $("#s1").textContent = grp4(bin(A)); $("#s2").textContent = grp4(bin(B)); $("#s3").textContent = grp4(bin(nb)); $("#s4").textContent = grp4(bin(r));
    $("#sv").textContent = `${A} − ${B} = ${A - B}. The 8-bit sum is ${bin(t >= 256 ? t - 256 : t)} with ${t >= 256 ? "a carry that is dropped" : "no carry"}, which reads as ${rs}${A < B ? " (negative because B is larger)" : ""}.`;
  };
  Lib.slider($("#sA"), { id: "ssA", label: "A ", min: 0, max: 127, value: A, fmt: (x) => x, onInput: (v) => { A = v; paint(); } });
  Lib.slider($("#sB"), { id: "ssB", label: "B ", min: 0, max: 127, value: B, fmt: (x) => x, onInput: (v) => { B = v; paint(); } });
})();
Lib.classify($("#cl1"), { prompt: "Does the unsigned 8-bit addition overflow?", buckets: [{"label": "No overflow"}, {"label": "Overflow"}], items: [{"text": "1010 1010 + 0101 0101 (170 + 85)", "b": 0}, {"text": "1100 0000 + 0100 0000 (192 + 64)", "b": 1}, {"text": "0111 1111 + 0000 0001 (127 + 1)", "b": 0}, {"text": "1111 0000 + 0001 1111 (240 + 31)", "b": 1}, {"text": "0011 0011 + 0101 0101 (51 + 85)", "b": 0}, {"text": "1000 0000 + 1000 0000 (128 + 128)", "b": 1}], done: "Overflow when the total is more than 255, which needs a ninth bit." });
Lib.classify($("#cl2"), { prompt: "Read each 8-bit two's complement pattern. Is it positive or negative?", buckets: [{"label": "Positive or zero"}, {"label": "Negative"}], items: [{"text": "0000 0000", "b": 0}, {"text": "0111 1111", "b": 0}, {"text": "1000 0000", "b": 1}, {"text": "1111 1111", "b": 1}, {"text": "0100 1101", "b": 0}, {"text": "1110 0010", "b": 1}, {"text": "1011 0100", "b": 1}, {"text": "0001 1110", "b": 0}], done: "In two's complement the left-most bit tells you the sign: 1 means negative." });
Lib.order($("#o1"), { prompt: "Put the steps for 0110 1011 − 0001 1110 using two's complement in order.", items: ["Write the number to subtract in full: 0001 1110", "Flip every bit: 1110 0001", "Add 1 to make −30: 1110 0010", "Add 0110 1011 + 1110 0010", "Ignore the carry out and write 0100 1101"], done: "Negate the second number, add, then drop the carry." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["One's complement", "Flip every bit"], ["Two's complement", "Flip every bit, then add 1"], ["Overflow", "Result too large for the bits available"], ["Left-most bit (two's complement)", "Worth −128 in an 8-bit number"], ["Carry out", "A ninth bit produced when the sum is more than 255"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Convert the 8-bit two's complement number 1111 0001 into denary.", "a": -15, "unit": "", "tol": 0.01, "hint": "−128 + 64 + 32 + 16 + 1.", "sol": "<b>−15</b>."},
  {"q": "What is the largest number a 6-bit two's complement integer can hold?", "a": 31, "unit": "", "tol": 0.01, "hint": "2^5 − 1.", "sol": "<b>31</b>."},
  {"q": "What is the smallest number a 6-bit two's complement integer can hold?", "a": -32, "unit": "", "tol": 0.01, "hint": "−2^5.", "sol": "<b>−32</b>."},
  {"q": "Write denary −5 as an 8-bit two's complement integer (no spaces).", "t": ["11111011"], "unit": "", "hint": "5 = 00000101, flip 11111010, add 1.", "sol": "<b>1111 1011</b>."},
  {"q": "Add 0011 0110 and 0100 1001 in binary. Give the 8-bit answer (no spaces).", "t": ["01111111"], "unit": "", "hint": "54 + 73 = 127.", "sol": "<b>0111 1111</b>."},
  {"q": "How many different values can 12 bits represent?", "a": 4096, "unit": "", "tol": 0.01, "hint": "2^12.", "sol": "<b>4096</b>."},
  {"q": "A counter stores unsigned 8-bit values. It holds 250 and 10 is added. What does it hold afterwards?", "a": 4, "unit": "", "tol": 0.01, "hint": "260 − 256.", "sol": "<b>4</b>, and overflow has occurred."},
  {"q": "The one's complement of 0010 1101 is 1101 0010. What is the two's complement, as a denary value?", "a": -45, "unit": "", "tol": 0.01, "hint": "0010 1101 is 45, so its two's complement is −45.", "sol": "<b>−45</b> (1101 0011)."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "How is the two's complement of a binary number found?", opts: ["Flip every bit", "Add 1 to the number", "Flip every bit and add 1", "Move every bit one place left"], a: 2, why: "Flip, then add 1." },
  { q: "What is the range of an 8-bit two's complement integer?", opts: ["0 to 255", "−127 to +127", "−128 to +127", "−256 to +255"], a: 2, why: "The left-most column is −128 and the rest add to 127." },
  { q: "What is the 8-bit two's complement pattern for −1?", opts: ["1000 0001", "1111 1110", "1111 1111", "0000 0001"], a: 2, why: "1 = 0000 0001, flip 1111 1110, add 1 = 1111 1111." },
  { q: "1111 1111 + 0000 0001 is calculated using 8 bits. What happens?", opts: ["The answer is 256", "A carry out is lost and the result is 0000 0000", "The answer is 1111 1111", "No error occurs and the result is 1 0000 0000"], a: 1, why: "The ninth bit does not fit, so the stored value is 0000 0000." },
  { q: "Why do computers use two's complement for negative numbers?", opts: ["It uses fewer bits than other methods", "The same adder circuit can add and subtract", "It avoids all overflow", "It makes negative numbers look like denary"], a: 1, why: "Subtraction becomes addition of the negative." },
  { q: "When subtracting by adding the two's complement, what do you do with the carry out of the left-most column?", opts: ["Add it back at the right", "Ignore it", "Write it as the sign bit", "Subtract it"], a: 1, why: "The carry is discarded; the remaining bits are the answer." },
] });
Lib.cards($("#fc1"), { cards: [
  ["One's complement", "Flip every bit. Two zeros. 8-bit range −127 to +127."],
  ["Two's complement", "Flip every bit, then add 1. One zero. 8-bit range −128 to +127."],
  ["Sign bit", "Left-most bit. 1 means negative in two's complement."],
  ["Overflow", "Result too large for the bits available."],
  ["Carry out", "Ninth bit from adding two bytes. Lost in an 8-bit store."],
  ["Subtract", "Add the two's complement of the second number. Ignore the carry out."],
  ["Smallest 8-bit", "1000 0000 = −128."],
  ["Largest 8-bit", "0111 1111 = +127."],
] });
