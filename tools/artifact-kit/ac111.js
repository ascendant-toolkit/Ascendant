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

function bitsSteps(el, n, label) {
  const pv = [128, 64, 32, 16, 8, 4, 2, 1]; let rem = n; const rows = pv.map((p) => { const b = rem >= p ? 1 : 0, before = rem; rem -= b * p; return { p, b, before, after: rem }; });
  const draw = (s) => {
    let o = SV.text(380, 28, n + " in denary", "lbl bd", { "text-anchor": "middle", style: "font-size:18px" });
    rows.forEach((r, i) => {
      const x = 60 + i * 80, v = clamp01(s.k - i);
      o += SV.text(x + 34, 66, r.p, "sm", { "text-anchor": "middle" });
      if (v > 0) {
        o += boxRow([{ t: r.b, c: r.b ? "f2" : "f3", v }], x, 76, 68, 52, 0);
        o += SV.text(x + 34, 152, r.b ? "fits" : "no", "sm", { "text-anchor": "middle", ...op(v) }) + SV.text(x + 34, 172, "left " + r.after, "sm", { "text-anchor": "middle", ...op(v) });
      } else o += boxRow([{ t: "", v: 1 }], x, 76, 68, 52, 0);
    });
    const done = clamp01(s.k - 7.5);
    if (done > 0) o += SV.text(380, 214, bin(n), "lbl bd t3", { "text-anchor": "middle", style: "font-size:26px;font-family:var(--mono)", ...op(done) }) + SV.text(380, 240, "= " + n + " in binary", "sm", { "text-anchor": "middle", ...op(done) });
    return o;
  };
  const steps = [{ cap: "Write the column values 128, 64, 32 ... 1 above eight empty bits. Work from the left. For each column ask: does this value fit into what is left of " + n + "?", s: { k: 0 } }];
  rows.forEach((r, i) => steps.push({ cap: `<b>${r.p}:</b> ${r.b ? `${r.before} is at least ${r.p}, so write <b>1</b> and subtract. ${r.after} left.` : `${r.before} is less than ${r.p}, so write <b>0</b>. Still ${r.after} left.`}`, s: { k: i + 1 } }));
  steps.push({ cap: `Read the bits: <b>${bin(n)}</b>. Check by adding the columns with a 1: ${rows.filter((r) => r.b).map((r) => r.p).join(" + ")} = ${n}.`, s: { k: 8 } });
  Lib.stepper($(el), { w: 760, h: 256, label, base: { k: 0 }, draw, tween: 600, dwell: 3600, steps });
}
bitsSteps("#stA", 241, "Converting 241 to binary one column at a time");

(function () {
  const v = "11110010", hi = "1111", lo = "0010";
  const draw = (s) => {
    const items = v.split("").map((t, i) => ({ t, c: i < 4 ? "f1" : "f2", top: [128, 64, 32, 16, 8, 4, 2, 1][i] }));
    let o = boxRow(items, 60 + 0, 50, 64, 52, 16);
    const g = clamp01(s.g);
    o += SV.line(60, 124, 60 + 4 * 80 - 16, 124, "c1", { "stroke-width": 3, ...op(g) }) + SV.line(60 + 4 * 80, 124, 60 + 8 * 80 - 16, 124, "c2", { "stroke-width": 3, ...op(g) });
    o += SV.text(60 + 2 * 80 - 8, 146, "1111", "lbl bd t1", { "text-anchor": "middle", style: "font-family:var(--mono)", ...op(g) }) + SV.text(60 + 6 * 80 - 8, 146, "0010", "lbl bd t2", { "text-anchor": "middle", style: "font-family:var(--mono)", ...op(g) });
    o += SV.text(60 + 2 * 80 - 8, 176, "8+4+2+1 = 15", "sm", { "text-anchor": "middle", ...op(clamp01(s.h)) }) + SV.text(60 + 6 * 80 - 8, 176, "2", "sm", { "text-anchor": "middle", ...op(clamp01(s.h)) });
    o += boxRow([{ t: "F", c: "f1", v: clamp01(s.f1) }], 60 + 2 * 80 - 40, 190, 64, 52, 0, { fs: 26 }) + boxRow([{ t: "2", c: "f2", v: clamp01(s.f2) }], 60 + 6 * 80 - 40, 190, 64, 52, 0, { fs: 26 });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 262, label: "Converting 11110010 to hexadecimal", base: { g: 0, h: 0, f1: 0, f2: 0 }, draw, tween: 600, dwell: 4200, steps: [
    { cap: "Start with the 8-bit value <b>11110010</b>. One hex digit stands for exactly four bits, so two hex digits will do.", s: {} },
    { cap: "Split into groups of four bits from the right: <b>1111</b> and <b>0010</b>. If the length is not a multiple of four, add leading zeros on the left.", s: { g: 1 } },
    { cap: "Work out each group. 1111 is 8 + 4 + 2 + 1 = <b>15</b>, which is the hex digit <b>F</b>. 0010 is <b>2</b>.", s: { g: 1, h: 1, f1: 1, f2: 1 } },
    { cap: "Write the digits in order: <b>F2</b>. To go back, write each hex digit as four bits again.", s: { g: 1, h: 1, f1: 1, f2: 1 } }] });
})();

(function () {
  const digs = [9, 6, 4];
  const draw = (s) => {
    let o = "";
    digs.forEach((d, i) => {
      const x = 90 + i * 200, a = clamp01(s.k - i * 1);
      o += boxRow([{ t: d, c: "f1", v: clamp01(s.d) }], x + 51, 36, 70, 52, 0, { fs: 28 });
      if (a > 0) {
        o += SV.line(x + 86, 94, x + 86, 120, "dash", op(a));
        o += boxRow(bin(d, 4).split("").map((t) => ({ t, c: "f2", v: a })), x, 126, 40, 46, 4, { fs: 20 });
      }
    });
    const f = clamp01(s.f);
    if (f > 0) o += SV.text(380, 226, "1001 0110 0100", "lbl bd t3", { "text-anchor": "middle", style: "font-size:26px;font-family:var(--mono)", ...op(f) });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 250, label: "Converting 964 into BCD", base: { d: 0, k: 0, f: 0 }, draw, tween: 600, dwell: 4200, steps: [
    { cap: "BCD treats each denary digit separately. 964 has three digits: <b>9</b>, <b>6</b> and <b>4</b>.", s: { d: 1 } },
    { cap: "Convert the first digit, 9, into four bits: 8 + 1 = <b>1001</b>.", s: { d: 1, k: 1 } },
    { cap: "Next digit, 6: 4 + 2 = <b>0110</b>. Always use all four bits, with leading zeros.", s: { d: 1, k: 2 } },
    { cap: "Last digit, 4: <b>0100</b>.", s: { d: 1, k: 3 } },
    { cap: "Join the groups in order: <b>1001 0110 0100</b>. Plain binary for 964 is 1111000100, so BCD needs 12 bits against 10 and the groups are different.", s: { d: 1, k: 3, f: 1 } }] });
})();

/* Lab 1 */
(function () {
  const rows = [["kilo and kibi", 1, "kB", "KiB"], ["mega and mebi", 2, "MB", "MiB"], ["giga and gibi", 3, "GB", "GiB"], ["tera and tebi", 4, "TB", "TiB"]];
  const show = (i) => {
    const r = rows[i], dec = 10 ** (3 * r[1]), b = 2 ** (10 * r[1]), gap = (b / dec - 1) * 100;
    $$("#pB button").forEach((x, k) => x.classList.toggle("pri", k === i));
    $("#p1").textContent = dec.toLocaleString("en-GB"); $("#p2").textContent = b.toLocaleString("en-GB"); $("#p3").textContent = Lib.fmtN(gap, 1) + "%";
    $("#pv").textContent = r[1] === 4 ? "A drive sold as 1 TB holds 10^12 bytes, which is only " + Lib.fmtN(dec / b, 3) + " TiB, about " + Lib.fmtN(dec / 2 ** 30, 0) + " GiB." : "1 " + r[3] + " = " + b.toLocaleString("en-GB") + " bytes, 1 " + r[2] + " = " + dec.toLocaleString("en-GB") + " bytes.";
    const w = 320, wb = w * (b / dec) / 1.11;
    $("#pS").innerHTML = SV.text(30, 40, "1 " + r[2] + " (decimal)", "lbl bd") + SV.rect(30, 50, w / 1.11, 28, "f3", { rx: 6, ...op(0.7) }) + SV.text(30, 112, "1 " + r[3] + " (binary)", "lbl bd") + SV.rect(30, 122, wb, 28, "f1", { rx: 6, ...op(0.7) }) + SV.text(30, 178, "Binary is " + Lib.fmtN(gap, 1) + "% larger", "sm");
  };
  $("#pB").innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  $$("#pB button").forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
})();

/* Lab 2 */
(function () {
  let bits = [1, 1, 1, 1, 0, 0, 1, 0];
  const pv = [128, 64, 32, 16, 8, 4, 2, 1];
  const paint = () => {
    const n = bits.reduce((a, b, i) => a + b * pv[i], 0), s = bits.join("");
    $("#t1").textContent = n; $("#t2").textContent = hx(n);
    const hi = parseInt(s.slice(0, 4), 2), lo = parseInt(s.slice(4), 2), ok = hi <= 9 && lo <= 9;
    $("#t3").textContent = ok ? "" + hi + lo : "not BCD";
    $("#tv").textContent = ok ? `As BCD the nibbles ${s.slice(0, 4)} and ${s.slice(4)} are the digits ${hi} and ${lo}, so BCD gives ${hi}${lo} but unsigned binary gives ${n}.` : `A nibble above 1001 (${hi > 9 ? s.slice(0, 4) : s.slice(4)}) is not a valid BCD digit, so this pattern cannot be BCD.`;
    $$("#tg button").forEach((b, i) => { b.textContent = bits[i]; b.classList.toggle("pri", !!bits[i]); });
    $("#tS").innerHTML = boxRow(bits.map((t, i) => ({ t, c: t ? "f2" : "f3", top: pv[i] })), 60, 24, 64, 48, 16) + SV.text(60 + 2 * 80 - 8, 108, hx(hi, 1), "lbl bd t1", { "text-anchor": "middle", style: "font-size:20px" }) + SV.text(60 + 6 * 80 - 8, 108, hx(lo, 1), "lbl bd t2", { "text-anchor": "middle", style: "font-size:20px" });
  };
  $("#tg").innerHTML = bits.map((b, i) => `<button class="b" data-i="${i}" aria-label="Bit ${pv[i]}"></button>`).join("");
  $$("#tg button").forEach((b) => (b.onclick = () => { bits[+b.dataset.i] ^= 1; paint(); })); paint();
})();

/* Lab 3 */
(function () {
  const v = { r: 252, g: 35, b: 138 };
  const paint = () => {
    $("#k1").textContent = "#" + hx(v.r) + hx(v.g) + hx(v.b); $("#k2").textContent = `${v.r}, ${v.g}, ${v.b}`;
    $("#kS").innerHTML = SV.rect(30, 20, 360, 110, "f3", { rx: 12, style: `fill:rgb(${v.r},${v.g},${v.b});opacity:1` }) + SV.text(210, 160, "R " + hx(v.r) + " = " + bin(v.r), "sm", { "text-anchor": "middle" }) + SV.text(210, 180, "G " + hx(v.g) + " = " + bin(v.g) + "   B " + hx(v.b) + " = " + bin(v.b), "sm", { "text-anchor": "middle" });
  };
  [["cr", "Red", "r"], ["cg", "Green", "g"], ["cb", "Blue", "b"]].forEach(([id, l, k]) => Lib.slider($("#" + id), { id: "s" + id, label: l + " ", min: 0, max: 255, value: v[k], fmt: (x) => x + " (" + hx(x) + ")", onInput: (x) => { v[k] = x; paint(); } }));
  paint();
})();

/* Lab 4 */
(function () {
  Lib.slider($("#bs"), { id: "bsl", label: "Denary number ", min: 0, max: 9999, value: 964, fmt: (x) => x, onInput: (n) => {
    const d = String(n).split(""), bcd = d.map((x) => bin(+x, 4)).join(" "), bb = Math.max(1, n.toString(2).length), cb = d.length * 4;
    $("#b1").textContent = bcd; $("#b2").textContent = cb; $("#b3").textContent = bb;
    $("#bv").textContent = cb > bb ? `BCD needs ${cb - bb} more bit${cb - bb === 1 ? "" : "s"} than plain binary here, but each digit stays separate.` : "Same number of bits here.";
    const mx = 40;
    $("#bS").innerHTML = SV.text(30, 40, "BCD: " + cb + " bits", "lbl bd") + SV.rect(30, 50, cb / mx * 360, 26, "f1", { rx: 6, ...op(0.7) }) + SV.text(30, 112, "Plain binary: " + bb + " bits", "lbl bd") + SV.rect(30, 122, bb / mx * 360, 26, "f2", { rx: 6, ...op(0.7) });
  } });
})();
Lib.classify($("#cl1"), { prompt: "Is each prefix binary or decimal?", buckets: [{"label": "Binary prefix"}, {"label": "Decimal prefix"}], items: [{"text": "kibi", "b": 0}, {"text": "kilo", "b": 1}, {"text": "mebi", "b": 0}, {"text": "mega", "b": 1}, {"text": "gibi", "b": 0}, {"text": "giga", "b": 1}, {"text": "tebi", "b": 0}, {"text": "tera", "b": 1}], done: "Kibi, mebi, gibi and tebi are the binary prefixes; they are written with an 'i'." });
Lib.classify($("#cl2"), { prompt: "Which representation suits each use?", buckets: [{"label": "BCD"}, {"label": "Hexadecimal"}], items: [{"text": "A bank adds up pence", "b": 0}, {"text": "A web page colour code", "b": 1}, {"text": "A calculator shows digits", "b": 0}, {"text": "A MAC address", "b": 1}, {"text": "Date and time held in the BIOS clock", "b": 0}, {"text": "A memory address in a debugger", "b": 1}, {"text": "A digital clock display", "b": 0}, {"text": "An error code on a screen", "b": 1}], done: "BCD keeps each denary digit separate. Hexadecimal is a compact way of showing binary for people." });
Lib.order($("#o1"), { prompt: "Put the steps for converting denary 558 into hexadecimal in order.", items: ["Write 558 as binary using the column values", "Pad the binary to 12 bits: 0010 0010 1110", "Split into groups of four bits from the right", "Convert each group to a hex digit", "Write the digits in order: 22E"], done: "Binary first, group in fours, then convert each nibble." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Nibble", "Four bits"], ["Kibibyte", "1024 bytes"], ["Kilobyte", "1000 bytes"], ["BCD", "Each denary digit stored in its own four bits"], ["Hexadecimal", "Base 16, digits 0 to 9 and A to F"], ["Binary", "Base 2, digits 0 and 1"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Convert the binary number 11010110 into denary.", "a": 214, "unit": "", "tol": 0.01, "hint": "128 + 64 + 16 + 4 + 2.", "sol": "<b>214</b>."},
  {"q": "Convert the hexadecimal value 3F into denary.", "a": 63, "unit": "", "tol": 0.01, "hint": "3 × 16 + 15.", "sol": "<b>63</b>."},
  {"q": "How many bytes are there in 6 kibibytes?", "a": 6144, "unit": "bytes", "tol": 0.01, "hint": "6 × 1024.", "sol": "<b>6144</b> bytes."},
  {"q": "A drive is sold as 2 terabytes. How many gigabytes is that in decimal units?", "a": 2000, "unit": "GB", "tol": 0.01, "hint": "Terabyte is a decimal prefix: 1 TB = 1000 GB.", "sol": "<b>2000</b> GB."},
  {"q": "Convert denary 200 into hexadecimal.", "t": ["C8"], "unit": "", "hint": "200 = 12 × 16 + 8, and 12 is C.", "sol": "<b>C8</b>."},
  {"q": "How many bits are in 3 kibibytes?", "a": 24576, "unit": "bits", "tol": 0.01, "hint": "3 × 1024 × 8.", "sol": "<b>24576</b> bits."},
  {"q": "Write denary 48 in BCD (eight bits, no spaces).", "t": ["01001000"], "unit": "", "hint": "4 = 0100, 8 = 1000.", "sol": "<b>0100 1000</b>."},
  {"q": "The BCD value 0110 0010 is stored. What denary number is it?", "a": 62, "unit": "", "tol": 0.01, "hint": "0110 = 6 and 0010 = 2.", "sol": "<b>62</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which of these is a binary prefix?", opts: ["kilo", "mebi", "giga", "tera"], a: 1, why: "Mebi is the binary prefix paired with mega." },
  { q: "How many bytes are in one kibibyte?", opts: ["1000", "1024", "1 000 000", "1 048 576"], a: 1, why: "A kibibyte is 2^10 = 1024 bytes." },
  { q: "What is denary 59 in BCD?", opts: ["0011 1011", "0101 1001", "1001 0101", "0101 1010"], a: 1, why: "Digits 5 and 9: 0101 and 1001." },
  { q: "Why do people use hexadecimal to show binary values?", opts: ["The computer can only process hex", "It uses less memory in the computer", "One hex digit stands for four bits, so values are shorter and easier to read", "It runs programs faster"], a: 2, why: "Hex is a human-friendly shorthand; the computer still stores binary." },
  { q: "Which use best suits BCD?", opts: ["A colour code on a web page", "A memory address in a debugger", "Financial calculations", "A MAC address"], a: 2, why: "BCD stores decimal digits exactly, so there are no rounding errors in money." },
  { q: "Which 4-bit pattern cannot be a BCD digit?", opts: ["1001", "0111", "1010", "0000"], a: 2, why: "BCD digits run from 0000 (0) to 1001 (9)." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Kibibyte", "1024 bytes. Binary prefix."],
  ["Kilobyte", "1000 bytes. Decimal prefix."],
  ["Pairs", "Kibi/kilo, mebi/mega, gibi/giga, tebi/tera."],
  ["Nibble", "Four bits. One hex digit."],
  ["Hexadecimal", "Base 16. Digits 0-9 and A-F. A = 10, F = 15."],
  ["BCD", "Each denary digit in its own four bits."],
  ["Valid BCD digits", "0000 to 1001 only."],
  ["BCD use", "Money, calculators, clocks, BIOS time, barcodes."],
] });
