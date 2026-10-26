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
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(30, 20, 200, 32, "cell", { rx: 6 }) + SV.text(40, 42, "entry 1: Smith", "lbl") + (k >= 1 ? SV.rect(30, 62, 200, 32, "cell", { rx: 6 }) + SV.text(40, 84, k >= 2 ? "entry 2: Smyth" : "entry 2: Smith", "lbl") : "") + (k >= 2 ? SV.rect(280, 40, 240, 36, "f2", { rx: 6 }) + SV.text(290, 63, "different: error, re-enter", "lbl bd") : "") + (k === 1 ? SV.rect(280, 40, 240, 36, "f1", { rx: 6 }) + SV.text(290, 63, "same: accepted", "lbl bd") : ""); return o; };
  Lib.stepper($("#stA"), { w: 540, h: 120, label: "Double entry", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["The name is entered once.", "It is entered a second time and the computer compares them: the same, so accepted.", "If the second entry differs the computer reports an error."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const bits = "0101110"; const draw = (s) => { const k = Math.round(s.i); let o = ""; for (let i = 0; i < 7; i++) o += SV.rect(30 + i * 50, 30, 44, 36, bits[i] === "1" ? "f1" : "cell", { rx: 6 }) + SV.text(52 + i * 50, 54, bits[i], "lbl bd", { "text-anchor": "middle" }); o += SV.rect(380, 30, 44, 36, k >= 2 ? "f3" : "cell", { rx: 6 }) + SV.text(402, 54, k >= 2 ? "0" : "?", "lbl bd", { "text-anchor": "middle" }) + SV.text(380, 90, "parity bit", "sm");
    o += SV.text(30, 120, ["7 data bits: 0101110", "count the 1s: four", "four is even, so the parity bit is 0", "byte sent: 01011100; receiver counts: still even, accepted"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 460, h: 140, label: "Parity", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Seven data bits are to be sent with <b>even parity</b>.", "The sender counts the 1s.", "Four is already even, so the parity bit is 0.", "The receiver recounts: an odd count would mean an error."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const rows = ["10110111", "01110000", "00011011", "01110100"], pb = "10100000";
  const draw = (s) => { const k = Math.round(s.i); let o = ""; rows.forEach((r, i) => { for (let j = 0; j < 8; j++) { const hot = (k >= 1 && i === 1) || (k >= 2 && j === 4); o += SV.rect(20 + j * 40, 14 + i * 28, 36, 24, k >= 3 && i === 1 && j === 4 ? "f2" : hot ? "f3" : "cell", { rx: 4 }) + SV.text(38 + j * 40, 31 + i * 28, r[j], "lbl", { "text-anchor": "middle" }); } }); for (let j = 0; j < 8; j++) o += SV.rect(20 + j * 40, 130, 36, 24, k >= 2 && j === 4 ? "f3" : "f1", { rx: 4 }) + SV.text(38 + j * 40, 147, pb[j], "lbl bd", { "text-anchor": "middle" });
    o += SV.text(350, 14, "", "sm"); return o; };
  Lib.stepper($("#stC"), { w: 360, h: 170, label: "Parity block", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Four bytes arrive with a parity byte (even parity, last column is each byte's parity bit).", "Row 2 has an odd number of 1s (three): the error is in this byte.", "Column 5 has the wrong parity: the error is in this bit position.", "The wrong bit is where row 2 and column 5 cross: a 0 that should be a 1."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let even = true; const bitsA = [0, 1, 0, 1, 1, 1, 0]; const bar = $("#pB");
  const paint = () => { bar.querySelectorAll("button").forEach((b, i) => { b.textContent = bitsA[i]; b.className = bitsA[i] ? "on" : ""; }); const ones = bitsA.reduce((a, b) => a + b, 0); const p = even ? ones % 2 : 1 - (ones % 2);
    $("#pO").innerHTML = `<div class="mono">${bitsA.join("")} <b>${p}</b></div><div class="verdict">${ones} ones in the data. For <b>${even ? "even" : "odd"}</b> parity the parity bit is <b>${p}</b>, so the whole byte ${bitsA.join("") + p} has ${ones + p} ones (${(ones + p) % 2 ? "odd" : "even"}).</div>`; };
  for (let i = 0; i < 7; i++) { const b = document.createElement("button"); b.onclick = () => { bitsA[i] ^= 1; paint(); }; bar.appendChild(b); }
  $("#pEv").onclick = () => { even = true; $("#pEv").className = "on"; $("#pOd").className = ""; paint(); }; $("#pOd").onclick = () => { even = false; $("#pOd").className = "on"; $("#pEv").className = ""; paint(); }; paint();
})();
(function () {
  const orig = ["1011011", "0111000", "0001101", "0111010"].map((r) => r.split("").map(Number)); const rowsP = orig.map((r) => r.reduce((a, b) => a + b, 0) % 2); const colsP = orig[0].map((_, j) => orig.reduce((a, r) => a + r[j], 0) % 2);
  let cur = orig.map((r) => r.slice());
  const paint = () => { let h = '<div class="tw"><table class="t mono"><tr><th></th>' + orig[0].map((_, j) => `<th>${j + 1}</th>`).join("") + "<th>parity</th></tr>"; const rbad = [], cbad = [];
    cur.forEach((r, i) => { if ((r.reduce((a, b) => a + b, 0) + rowsP[i]) % 2) rbad.push(i); }); orig[0].forEach((_, j) => { if ((cur.reduce((a, r) => a + r[j], 0) + colsP[j]) % 2) cbad.push(j); });
    cur.forEach((r, i) => { h += `<tr><td>byte ${i + 1}</td>` + r.map((c, j) => `<td><button data-r="${i}" data-c="${j}" style="min-width:34px;${rbad.includes(i) && cbad.includes(j) ? "background:var(--bad);color:#fff" : ""}">${c}</button></td>`).join("") + `<td>${rowsP[i]}</td></tr>`; });
    h += "<tr><td>parity byte</td>" + colsP.map((c) => `<td>${c}</td>`).join("") + "<td></td></tr></table></div>"; $("#bG").innerHTML = h;
    $("#bG").querySelectorAll("button").forEach((b) => b.onclick = () => { cur[+b.dataset.r][+b.dataset.c] ^= 1; paint(); });
    $("#bV").innerHTML = rbad.length === 0 && cbad.length === 0 ? "No error: every row and column has the agreed (even) parity. Click a bit to damage it." : rbad.length === 1 && cbad.length === 1 ? `Error located: byte <b>${rbad[0] + 1}</b>, bit <b>${cbad[0] + 1}</b> is wrong. It can be corrected by flipping it.` : "More than one bit is wrong: the errors are detected but cannot be located reliably."; };
  paint();
})();
btnTable("mB", "mO", [
  ["Reading the screen against the paper form", "Visual check", "Data entry"],
  ["Typing a new password twice", "Double entry", "Data entry"],
  ["An extra bit on each byte", "Parity byte check", "Data transfer"],
  ["Row and column parity to find a wrong bit", "Parity block check", "Data transfer"],
  ["A value calculated from the whole file", "Checksum", "Data transfer"]
], ["Description", "Method", "Used during"]);
Lib.classify($("#cl1"), { prompt: "Used during data entry or data transfer?", buckets: [{"label": "Data entry"}, {"label": "Data transfer"}], items: [{"text": "Visual check", "b": 0}, {"text": "Parity byte check", "b": 1}, {"text": "Double entry", "b": 0}, {"text": "Checksum", "b": 1}, {"text": "Comparing the screen with the paper form", "b": 0}, {"text": "Parity block check", "b": 1}], done: "Entry: visual, double entry. Transfer: parity, checksum." });
Lib.classify($("#cl2"), { prompt: "Verification or validation?", buckets: [{"label": "Verification"}, {"label": "Validation"}], items: [{"text": "Double entry", "b": 0}, {"text": "Range check", "b": 1}, {"text": "Visual check", "b": 0}, {"text": "Presence check", "b": 1}, {"text": "Checksum", "b": 0}, {"text": "Format check", "b": 1}], done: "Verification: the same as the original." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Visual check", "A person compares the entered data with the original"], ["Double entry", "The data is entered twice and compared by the computer"], ["Parity byte check", "A bit is added so each byte has an agreed number of 1s"], ["Parity block check", "Row and column parity locate a wrong bit"], ["Checksum", "A value calculated from the data and sent with it"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the checksum steps in order.", items: ["A value is calculated from the data before transmission", "The value is transmitted with the data", "The receiver recalculates the value from the data received", "The two values are compared", "A difference means an error has occurred"], done: "Calculate, send, recalculate, compare, difference." });
Lib.calc($("#c1"), { qs: [
  {"q": "Even parity: the 7 data bits 1011001 have four 1s. What is the parity bit?", "a": 0, "unit": "", "tol": 0.01, "hint": "Four is already even.", "sol": "<b>0</b>."},
  {"q": "Odd parity: the 7 data bits 1011001. What is the parity bit?", "a": 1, "unit": "", "tol": 0.01, "hint": "Four 1s; add a 1 to make five.", "sol": "<b>1</b>."},
  {"q": "A byte with even parity arrives as 01101110 (five 1s). How many 1s should it have (even)?", "a": 4, "unit": "", "tol": 0.01, "hint": "Even number: 4 or 6; the error is one bit wrong. Answer 4 or 6: give the lower.", "sol": "<b>4</b> (or 6): it has 5, so there is an error."},
  {"q": "A parity block has 4 data bytes and a parity byte. How many bits are sent in total (8 bits each)?", "a": 40, "unit": "", "tol": 0.01, "hint": "5 × 8.", "sol": "<b>40</b>."},
  {"q": "A checksum is the sum of the bytes mod 256. The bytes are 100, 200 and 50. What is the checksum?", "a": 94, "unit": "", "tol": 0.01, "hint": "350 mod 256.", "sol": "<b>94</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Double entry:", opts: ["Data entered twice and compared", "Typed once", "A range check", "Compression"], a: 0, why: "Twice." },
  { q: "A parity bit makes the number of 1s:", opts: ["Odd or even as agreed", "Always zero", "Always one", "Prime"], a: 0, why: "Odd or even." },
  { q: "Parity block can:", opts: ["Locate a single wrong bit", "Correct all errors", "Encrypt", "Compress"], a: 0, why: "Locate." },
  { q: "A checksum is compared:", opts: ["After transmission", "Never", "Before typing", "Only by hand"], a: 0, why: "After." },
  { q: "Verification checks data is:", opts: ["The same as the original", "Sensible", "Encrypted", "Short"], a: 0, why: "Same as the original." },
  { q: "Visual check is used during:", opts: ["Data entry", "Data transfer", "Encryption", "Back-up"], a: 0, why: "Entry." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Verification", "Same as the original."],
  ["Visual check", "Person compares with the original."],
  ["Double entry", "Two entries compared by the computer."],
  ["Parity bit", "Makes the 1s odd or even."],
  ["Parity block", "Rows and columns find the bit."],
  ["Checksum", "Calculated, sent, recalculated, compared."],
  ["Entry", "Visual, double entry."],
  ["Transfer", "Parity, checksum."],
] });
