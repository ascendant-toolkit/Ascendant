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
const MYD = [2, 8, 9, 12, 13, 15, 18, 19, 20, 23, 25, 26, 39, 38, 40];
(function () {
  const draw = (s) => { const k = Math.round(s.i); const steps = [[1, 15, 8], [1, 7, 4], [5, 7, 6]]; const st = steps[Math.min(k, 2)]; let o = ""; MYD.forEach((v, i) => { const idx = i + 1, inr = idx >= st[0] && idx <= st[1]; o += SV.rect(10 + i * 38, 20, 34, 30, idx === st[2] ? "f3" : inr ? "f1" : "cell", { rx: 4, ...(inr ? {} : op(0.3)) }) + SV.text(27 + i * 38, 40, v, "lbl", { "text-anchor": "middle", style: "font-size:11px" }) + SV.text(27 + i * 38, 66, idx, "sm", { "text-anchor": "middle" }); });
    o += SV.text(10, 100, ["", "Mid = 8: 19 > 15 so Right = 7", "Mid = 4: 12 < 15 so Left = 5", "Mid = 6: 15 = target: Found 6"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 590, h: 115, label: "Binary search", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Search for 15 in sorted data, indexes 1 to 15; Mid = 8.", "19 is greater than 15: keep the left half.", "Mid = 4 holds 12: keep the right half of that.", "Mid = 6 holds 15: found."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const start = [5, 2, 4, 1]; const draw = (s) => { const k = Math.round(s.i); const a = start.slice(); const log = []; for (let i = 0; i < Math.min(k, 3); i++) if (a[i] > a[i + 1]) { [a[i], a[i + 1]] = [a[i + 1], a[i]]; } let o = ""; a.forEach((v, i) => o += SV.rect(20 + i * 70, 20, 62, 34, k < 4 && (i === k || i === k + 1) ? "f3" : "cell", { rx: 5 }) + SV.text(51 + i * 70, 43, v, "lbl bd", { "text-anchor": "middle" })); o += SV.text(20, 88, k === 0 ? "pass starts: compare 5 and 2" : k < 4 ? "compare neighbours; swap if the left is larger" : "end of pass: the largest (5) is in place", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 340, h: 110, label: "Bubble sort pass", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["5, 2, 4, 1: compare the first pair.", "5 > 2: swap: 2, 5, 4, 1; compare 5 and 4.", "5 > 4: swap: 2, 4, 5, 1; compare 5 and 1.", "5 > 1: swap: 2, 4, 1, 5.", "The largest value 5 is in place after one pass."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const rows = [["D", "T", "H", "R"], ["D", "T", "H", "R"], ["D", "H", "T", "R"], ["D", "H", "R", "T"]][Math.min(k, 3)]; let o = ""; rows.forEach((v, i) => o += SV.rect(20 + i * 70, 20, 62, 34, k === 1 && i === 2 ? "f3" : "cell", { rx: 5 }) + SV.text(51 + i * 70, 43, v, "lbl bd", { "text-anchor": "middle" })); o += SV.text(20, 88, ["D, T, H, R: D is already sorted", "key = H: T > H so T shifts right...", "...H is inserted before T: D H T R", "key = R: T shifts, R inserted: D H R T"][Math.min(k, 3)], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 360, h: 110, label: "Insertion sort", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Start.", "Key H: shift T right.", "Insert H.", "Key R: shift T, insert R. Sorted."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let target = 15, L, R, rows, done; const reset = () => { L = 1; R = MYD.length; rows = []; done = false; paint(); };
  const step = () => { if (done || L > R) return; const M = Math.floor((L + R) / 2); rows.push([L, R, M, MYD[M - 1]]); if (MYD[M - 1] === target) done = M; else if (target > MYD[M - 1]) L = M + 1; else R = M - 1; paint(); };
  const paint = () => { $("#bsV").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Left</th><th>Right</th><th>Mid</th><th>MyData[Mid]</th></tr>' + rows.map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td></tr>`).join("") + "</table></div>" + `<div class="verdict">${done ? `Found ${target} at index <b>${done}</b> after ${rows.length} comparison(s).` : L > R ? `<b>Not found</b> after ${rows.length} comparison(s).` : "Press Step to compare with the middle element."}</div>`; };
  Lib.slider($("#bT"), { id: "bt", label: "Target ", min: 1, max: 45, value: target, fmt: (x) => x, onInput: (v) => { target = v; reset(); } }); $("#bs_step").onclick = step; $("#bs_reset").onclick = reset; reset();
})();
(function () {
  let a, i, swaps, passes; const reset = () => { a = [9, 4, 7, 2, 8]; i = 0; swaps = 0; passes = 0; paint("Press the button to compare the first pair."); };
  const cmp = () => { if (i >= a.length - 1) { i = 0; passes++; paint("End of the pass: the largest remaining value is in place."); return; } let m = ""; if (a[i] > a[i + 1]) { [a[i], a[i + 1]] = [a[i + 1], a[i]]; swaps++; m = "swapped"; } else m = "no swap"; i++; paint(m); };
  const paint = (m) => { $("#buV").innerHTML = '<div class="tw"><table class="t mono"><tr>' + a.map((v, k) => `<td style="${k === i || k === i + 1 ? "background:var(--accent-soft);font-weight:700" : ""}">${v}</td>`).join("") + `</tr></table></div><div class="verdict">${m}. Swaps so far: <b>${swaps}</b>, passes: <b>${passes}</b>.</div>`; };
  $("#bu_step").onclick = cmp; $("#bu_pass").onclick = () => { for (let k = 0; k < a.length; k++) { if (i >= a.length - 1) break; cmp(); } }; $("#bu_reset").onclick = reset; reset();
})();
btnTable("wB", "wO", [
  ["Find a name in an unsorted list", "Linear search", "No order needed"],
  ["Find a name in a sorted list of a million", "Binary search", "Halve the range each step"],
  ["Compare neighbours and swap", "Bubble sort", "Largest value moves to the end"],
  ["Slide each item into place among the sorted ones", "Insertion sort", "Shift larger values right"],
  ["Swap two array elements in a procedure", "BYREF parameters", "Change the original"]
], ["Need", "Method", "Why"]);
Lib.classify($("#cl1"), { prompt: "Is it a search or a sort?", buckets: [{"label": "Search"}, {"label": "Sort"}], items: [{"text": "Binary search", "b": 0}, {"text": "Bubble sort", "b": 1}, {"text": "Linear search", "b": 0}, {"text": "Insertion sort", "b": 1}, {"text": "Needs the data to be in order first", "b": 0}, {"text": "Puts the data in order", "b": 1}], done: "Search finds; sort orders." });
Lib.classify($("#cl2"), { prompt: "Bubble sort or insertion sort?", buckets: [{"label": "Bubble sort"}, {"label": "Insertion sort"}], items: [{"text": "Swaps neighbouring elements that are out of order", "b": 0}, {"text": "Takes a key and shifts larger elements right", "b": 1}, {"text": "Stops early when a pass makes no swaps", "b": 0}, {"text": "Inserts the key into the sorted part", "b": 1}, {"text": "Uses a Temp variable to swap", "b": 0}, {"text": "Final list D H R T from D T H R by shifting", "b": 1}], done: "Neighbour swaps against shifting." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Binary search", "Compare with the middle and discard half"], ["Linear search", "Check each element in turn"], ["Bubble sort", "Swap neighbouring elements that are out of order"], ["Dry run", "Executing an algorithm by hand with a trace table"], ["BYREF", "Parameter passed so the procedure changes the original"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the binary search steps in order.", items: ["Set Left to 1 and Right to the last index", "Work out Mid ← (Left + Right) DIV 2", "If the middle element is the target, stop", "If the target is bigger, set Left to Mid + 1", "Otherwise set Right to Mid − 1 and repeat"], done: "Set, mid, found, right half, left half." });
Lib.calc($("#c1"), { qs: [
  {"q": "Left = 1, Right = 15. What is Mid ((Left + Right) DIV 2)?", "a": 8, "unit": "", "tol": 0.01, "hint": "16 DIV 2.", "sol": "<b>8</b>."},
  {"q": "Left = 1, Right = 7. What is Mid?", "a": 4, "unit": "", "tol": 0.01, "hint": "8 DIV 2.", "sol": "<b>4</b>."},
  {"q": "A bubble sort of 10 values needs at most how many comparisons in one pass?", "a": 9, "unit": "", "tol": 0.01, "hint": "Neighbouring pairs.", "sol": "<b>9</b>."},
  {"q": "A binary search on 1000 sorted values needs at most about how many comparisons (log2 1000 rounded up)?", "a": 10, "unit": "", "tol": 0.01, "hint": "2^10 = 1024.", "sol": "<b>10</b>."},
  {"q": "Process(3) with Count reaching 5 and Index 2 sets Mix[4] ← Count × Index. What is Mix[4]?", "a": 10, "unit": "", "tol": 0.01, "hint": "5 × 2.", "sol": "<b>10</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A binary search needs data that is:", opts: ["Sorted", "Random", "Text only", "Empty"], a: 0, why: "Sorted." },
  { q: "Mid is:", opts: ["(Left + Right) DIV 2", "Left × Right", "Right − Left", "Left"], a: 0, why: "Average, integer." },
  { q: "BYREF means:", opts: ["The original is changed", "A copy is changed", "Nothing happens", "The value is deleted"], a: 0, why: "Original changed." },
  { q: "A more efficient bubble sort stops when:", opts: ["A pass has no swaps", "The array is empty", "Index = 1", "Never"], a: 0, why: "No swaps." },
  { q: "A trace table records:", opts: ["Variable values as the algorithm runs", "Only the output", "The compiler", "Only arrays"], a: 0, why: "Values." },
  { q: "Linear search works on:", opts: ["Any array", "Only sorted arrays", "Only numbers", "Only 2D arrays"], a: 0, why: "Any." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Binary search", "Sorted data; Mid; discard half."],
  ["Linear search", "Each element in turn."],
  ["Bubble sort", "Compare neighbours; swap."],
  ["Insertion sort", "Shift larger; insert the key."],
  ["Efficient bubble", "Boundary − 1; stop if NoSwaps."],
  ["BYREF", "Swap needs reference parameters."],
  ["Dry run", "One row per pass."],
  ["Trace table", "Variables after each statement."],
] });
