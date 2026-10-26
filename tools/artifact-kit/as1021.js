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
  const vals = [7, 12, 3, 18, 9]; const draw = (s) => { const k = Math.round(s.i); let mx = vals[0]; for (let i = 1; i <= Math.min(k, 4); i++) if (vals[i] > mx) mx = vals[i]; let o = ""; vals.forEach((v, i) => o += SV.rect(20 + i * 76, 20, 68, 34, i === k ? "f3" : i < k ? "f1" : "cell", { rx: 5 }) + SV.text(54 + i * 76, 43, v, "lbl bd", { "text-anchor": "middle" }) + SV.text(54 + i * 76, 68, "[" + (i + 1) + "]", "sm", { "text-anchor": "middle" }));
    o += SV.text(20, 108, "Max = " + mx, "lbl bd t3"); return o; };
  Lib.stepper($("#stA"), { w: 420, h: 125, label: "Largest", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["Max starts as the first element: 7.", "12 > 7: Max = 12.", "3 is not greater: Max stays 12.", "18 > 12: Max = 18.", "9 is not greater. Output 18."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const g = ["AAB", "BAA", "ABA"]; let o = SV.text(20, 14, "Version1[floor, room]", "sm"); g.forEach((r, f) => r.split("").forEach((c, m) => o += SV.rect(60 + m * 60, 22 + f * 34, 54, 28, c === "A" ? "f1" : "f2", { rx: 4 }) + SV.text(87 + m * 60, 41 + f * 34, c, "lbl bd", { "text-anchor": "middle" }))); for (let f = 0; f < 3; f++) o += SV.text(20, 41 + f * 34, "floor " + f, "sm"); for (let m = 0; m < 3; m++) o += SV.text(87 + m * 60, 130, "room " + (m + 1), "sm", { "text-anchor": "middle" });
    if (k >= 1) o += SV.rect(56, 18, 190, 36, "ax", { rx: 4, style: "fill:none;stroke:var(--accent);stroke-width:2" }); o += SV.text(280, 50, ["", "Version1[0, 3] is the 3rd room on floor 0", "loop through the rooms of one floor"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 560, h: 145, label: "2D array", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Each cell holds A (available) or B (booked): three floors by rooms.", "The first index is the floor, the second the room.", "To list a floor, loop through its rooms."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const a = [10, 20, 15, 40, 41, 42]; const draw = (s) => { const k = Math.round(s.i); let o = ""; a.forEach((v, i) => o += SV.rect(20 + i * 70, 20, 62, 30, Math.floor(i / 3) === k - 1 ? "f1" : "cell", { rx: 4 }) + SV.text(51 + i * 70, 40, v, "lbl bd", { "text-anchor": "middle" })); const avg = k >= 1 ? Math.floor((a[0] + a[1] + a[2]) / 3) : null, avg2 = k >= 2 ? Math.floor((a[3] + a[4] + a[5]) / 3) : null;
    if (avg !== null) o += SV.rect(20, 80, 100, 30, "f3", { rx: 4 }) + SV.text(70, 100, "Array2[1] = " + avg, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); if (avg2 !== null) o += SV.rect(140, 80, 110, 30, "f3", { rx: 4 }) + SV.text(195, 100, "Array2[2] = " + avg2, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); return o; };
  Lib.stepper($("#stC"), { w: 460, h: 130, label: "Averages", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Six sensor samples in Array1.", "(10 + 20 + 15) / 3 = 15 stored in Array2[1].", "(40 + 41 + 42) / 3 = 41 stored in Array2[2]. IxA moves on by 3."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let vals, k; const reset = () => { k = 0; paint(); }; const shuf = () => { vals = Array.from({ length: 10 }, () => 1 + Math.floor(Math.random() * 99)); k = 0; paint(); };
  const paint = () => { let mx = vals[0], mi = 1, mn = vals[0], ni = 1; for (let i = 1; i <= k; i++) { if (vals[i] > mx) { mx = vals[i]; mi = i + 1; } if (vals[i] < mn) { mn = vals[i]; ni = i + 1; } }
    let h = '<div class="tw"><table class="t mono"><tr><th>index</th>' + vals.map((_, i) => `<th>${i + 1}</th>`).join("") + "</tr><tr><td>Data</td>" + vals.map((v, i) => `<td style="${i === k ? "background:var(--accent-soft);font-weight:700" : i < k ? "opacity:.6" : ""}">${v}</td>`).join("") + "</tr></table></div>"; $("#mxV").innerHTML = h + `<div class="verdict">After checking element ${k + 1}: Max = <b>${mx}</b> (index ${mi}), Min = <b>${mn}</b> (index ${ni}).</div>`; };
  vals = [34, 78, 12, 90, 45, 23, 67, 5, 88, 51]; $("#mx_step").onclick = () => { if (k < vals.length - 1) { k++; paint(); } }; $("#mx_shuf").onclick = shuf; $("#mx_reset").onclick = reset; reset();
})();
(function () {
  const g = [["A", "B", "A", "A", "B"], ["B", "A", "A", "B", "A"], ["A", "A", "B", "A", "A"]]; let fl = 0; const bar = $("#hF");
  const paint = () => { let h = '<div class="tw"><table class="t mono"><tr><th>floor ↓ room →</th>' + [1, 2, 3, 4, 5].map((r) => `<th>${r}</th>`).join("") + "</tr>"; g.forEach((r, f) => h += `<tr style="${f === fl ? "background:var(--accent-soft);font-weight:700" : ""}"><td>${f}</td>` + r.map((c) => `<td>${c}</td>`).join("") + "</tr>"); $("#hG").innerHTML = h + "</table></div>"; const av = []; g[fl].forEach((c, i) => { if (c === "A") av.push(i + 1); }); $("#hV").innerHTML = `Floor <b>${fl}</b>: available rooms ${av.join(", ")}. The loop <span class="mono">FOR RoomNumber ← 1 TO 5</span> tests <span class="mono">Version1[${fl}, RoomNumber] = 'A'</span> and counts <b>${av.length}</b>.`; };
  [0, 1, 2].forEach((f) => { const b = document.createElement("button"); b.textContent = "Floor " + f; b.onclick = () => { fl = f; bar.querySelectorAll("button").forEach((x) => x.className = x === b ? "on" : ""); paint(); }; if (f === 0) b.className = "on"; bar.appendChild(b); }); paint();
})();
btnTable("aB", "aO", [
  ["Add all the marks", "Total ← 0; Total ← Total + Marks[Index]", "Total"],
  ["How many marks are 50 or more", "Count ← 0; IF Marks[Index] >= 50 THEN Count ← Count + 1", "Count"],
  ["The highest mark", "Max ← Marks[1]; IF Marks[Index] > Max THEN Max ← Marks[Index]", "Largest"],
  ["Where the lowest mark is", "Min ← Marks[1]; MinIndex ← 1; update both when smaller", "Index of smallest"]
], ["Need", "Pseudocode", "Algorithm"]);
Lib.classify($("#cl1"), { prompt: "Which array algorithm does it describe?", buckets: [{"label": "Total"}, {"label": "Count in a range"}, {"label": "Largest value"}, {"label": "Index of smallest"}], items: [{"text": "Add each element to a running sum", "b": 0}, {"text": "Add 1 when an element is between 66 and 173", "b": 1}, {"text": "Keep the biggest value seen so far", "b": 2}, {"text": "Store the position of the minimum", "b": 3}, {"text": "Total ← Total + Data[Index]", "b": 0}, {"text": "IF Data[Index] > Max THEN Max ← Data[Index]", "b": 2}], done: "Match the loop body." });
Lib.classify($("#cl2"), { prompt: "Should this be set before the loop or inside the loop?", buckets: [{"label": "Before the loop"}, {"label": "Inside the loop"}], items: [{"text": "Count ← 0", "b": 0}, {"text": "Reading the element Data[Index]", "b": 1}, {"text": "Total ← 0", "b": 0}, {"text": "Adding Data[Index] to Total", "b": 1}, {"text": "Max ← Data[1]", "b": 0}, {"text": "Comparing the element with Max", "b": 1}], done: "Set starting values first." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Array", "Many values of the same type under one identifier"], ["Index", "The position of an element"], ["Bounds", "The lowest and highest index"], ["2D array", "Two indexes, for example floor and room"], ["Element", "One value in an array"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for the largest value in order.", items: ["Set Max to the first element", "Loop through the remaining elements", "Compare each element with Max", "If it is greater, replace Max", "Output Max after the loop"], done: "Start, loop, compare, replace, output." });
Lib.calc($("#c1"), { qs: [
  {"q": "DECLARE Data : ARRAY [1:120] OF REAL. How many elements?", "a": 120, "unit": "", "tol": 0.01, "hint": "120 − 1 + 1.", "sol": "<b>120</b>."},
  {"q": "DECLARE Version1 : ARRAY [0:2, 1:15] OF CHAR. How many elements?", "a": 45, "unit": "", "tol": 0.01, "hint": "3 × 15.", "sol": "<b>45</b>."},
  {"q": "Values: 4, 9, 2, 7. What is the total?", "a": 22, "unit": "", "tol": 0.01, "hint": "4 + 9 + 2 + 7.", "sol": "<b>22</b>."},
  {"q": "In the same values, what is the index (from 1) of the smallest?", "a": 3, "unit": "", "tol": 0.01, "hint": "The value 2.", "sol": "<b>3</b>."},
  {"q": "Array1 has 600 elements; averages of three consecutive values go in Array2. How many elements are used in Array2?", "a": 200, "unit": "", "tol": 0.01, "hint": "600 ÷ 3.", "sol": "<b>200</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An array holds:", opts: ["Values of the same type", "Mixed types", "One value", "Only text"], a: 0, why: "Same type." },
  { q: "ARRAY [0:99] has:", opts: ["100 elements", "99 elements", "101 elements", "1 element"], a: 0, why: "0 to 99." },
  { q: "To total an array you:", opts: ["Initialise Total before the loop", "Set Total inside the loop", "Never initialise", "Loop twice"], a: 0, why: "Before the loop." },
  { q: "A 2D array needs:", opts: ["Two indexes", "Two types", "No loop", "A record"], a: 0, why: "Two indexes." },
  { q: "An array beats separate variables because:", opts: ["A loop can go through the values", "It uses less memory always", "It is faster always", "It needs no type"], a: 0, why: "Iterate with a loop." },
  { q: "INT(RAND(200)) + 1 gives:", opts: ["1 to 200", "0 to 199", "1 to 199", "0 to 200"], a: 0, why: "1 to 200." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Array", "Same type, one name, index."],
  ["Declare", "ARRAY [lower:upper] OF type."],
  ["2D array", "[0:2, 1:15]"],
  ["Total", "Initialise, add in a loop."],
  ["Largest", "Start with the first; replace."],
  ["Count", "Initialise; add 1 on a match."],
  ["Loop counter", "Used as the index."],
  ["Benefit", "Simpler, loop, one identifier."],
] });
