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
  const draw = (s) => { const k = Math.round(s.i); const lv = [["copy the file into an array"], ["open the file", "set the index", "loop until end of file", "close the file"], ["open the file", "set the index to 1", "loop until end of file:", "   read a line", "   store it at the index", "   add 1 to the index", "close the file"]][Math.min(k, 2)]; let o = ""; lv.forEach((l, i) => o += SV.rect(20, 10 + i * 24, 300, 20, k === 0 ? "f3" : k === 1 ? "f1" : "cell", { rx: 4 }) + SV.text(28, 24 + i * 24, l, "lbl", { style: "font-size:11px" })); o += SV.text(340, 40, ["one step", "refined once", "each step can now be coded"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 190, label: "Refinement", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["The problem as one step.", "<b>Refine</b> it into main steps.", "Refine again until each step can be <b>directly coded</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const file = ["red", "green", "blue", "pink"]; const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 16, "file", "sm") + SV.text(250, 16, "array", "sm"); file.forEach((l, i) => o += SV.rect(20, 22 + i * 28, 150, 24, i < k ? "f1" : "cell", { rx: 4 }) + SV.text(28, 39 + i * 28, l, "lbl", { style: "font-size:12px" })); for (let i = 0; i < 6; i++) o += SV.rect(250, 22 + i * 28, 150, 24, "cell", { rx: 4 }) + SV.text(258, 39 + i * 28, (i + 1) + (i < k ? "  " + file[i] : ""), "lbl", { style: "font-size:12px" }); o += SV.text(420, 60, "index = " + (k + 1), "lbl bd t3"); return o; };
  Lib.stepper($("#stB"), { w: 540, h: 195, label: "File into array", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["Open the file; index is 1.", "Read line 1, store it at index 1, index becomes 2.", "Read line 2, store it, index becomes 3.", "Read line 3, store it, index becomes 4.", "Read line 4, store it, index becomes 5. End of file: stop and close."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const L = ["Count ← 1", "Flag ← FALSE", "WHILE Flag = FALSE AND Count <= 5", "   CALL ReBoot()", "   Count ← Count + 1", "   Flag ← Check()", "ENDWHILE", "IF Flag = FALSE THEN CALL Alert(27)"]; const at = [[0, 1], [2, 5], [7, 7]][Math.min(k, 2)]; let o = ""; L.forEach((l, i) => o += SV.rect(20, 8 + i * 22, 340, 20, i >= at[0] && i <= at[1] ? "f3" : "cell", { rx: 3 }) + SV.text(28, 22 + i * 22, l, "lbl", { style: "font-size:11px" })); o += SV.text(380, 40, ["before the loop: initialise", "loop-back decision: WHILE", "final decision: IF"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:11px" }); return o; };
  Lib.stepper($("#stC"), { w: 620, h: 190, label: "Flowchart to code", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Initialisation boxes become assignments.", "The loop-back decision becomes a <b>WHILE</b> loop.", "The final decision becomes an <b>IF</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const file = ["red", "green", "blue", "pink"]; let st;
  const reset = () => { st = { phase: 0, idx: 1, arr: [], pos: 0, log: ["Ready."] }; paint(); };
  const step = () => { const s = st; if (s.phase === 0) { s.log.push("Open the file for reading; index = 1"); s.phase = 1; } else if (s.phase === 1) { if (s.pos >= file.length) { s.log.push("End of file reached: leave the loop"); s.phase = 2; } else { const l = file[s.pos++]; s.arr[s.idx - 1] = l; s.log.push(`Read "${l}", store it in array[${s.idx}], index becomes ${s.idx + 1}`); s.idx++; } } else if (s.phase === 2) { s.log.push("Close the file. Done."); s.phase = 3; } paint(); };
  const paint = () => { const s = st; let h = '<div class="tw"><table class="t mono"><tr><th>index</th>' + [1, 2, 3, 4, 5, 6].map((i) => `<th>${i}</th>`).join("") + "</tr><tr><td>array</td>" + [0, 1, 2, 3, 4, 5].map((i) => `<td>${s.arr[i] || ""}</td>`).join("") + "</tr></table></div>"; $("#faV").innerHTML = h + '<div class="verdict">' + s.log.slice(-3).join("<br>") + "</div>"; };
  $("#fa_step").onclick = step; $("#fa_reset").onclick = reset; reset();
})();
btnTable("oB", "oO", [
  ["Copy a file into an array", "Open, index = 1, loop until end of file (read, store, add 1), close", "Iteration with an end-of-file test"],
  ["Write non-blank array items to a file", "Open in append mode, index = 1, loop 65 times (if not blank write; add 1), close", "Selection inside iteration"],
  ["Sum positives and negatives until 0", "Set sums to 0, input, add to the right sum, repeat until 0, output both", "Selection inside iteration"]
], ["Task", "Steps", "Constructs"]);
btnTable("mB", "mO", [
  ["Read the names in a file", "Read mode", "Nothing is changed"],
  ["Start a new file or replace all its contents", "Write mode", "Overwrites existing data"],
  ["Add names to a file that already has data", "Append mode", "Existing data is kept"]
], ["Task", "Mode", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which construct is being used?", buckets: [{"label": "Sequence"}, {"label": "Selection"}, {"label": "Iteration"}], items: [{"text": "Steps carried out one after another in order", "b": 0}, {"text": "Test whether an element is blank", "b": 1}, {"text": "Repeat until the end of the file", "b": 2}, {"text": "Open the file, then read a line", "b": 0}, {"text": "Check the value returned by EOF", "b": 1}, {"text": "Repeat for 35 students", "b": 2}], done: "Order, choice, repeat." });
Lib.classify($("#cl2"), { prompt: "Is the step correct for an algorithm that appends the names of students with a mark under 20 to an existing file?", buckets: [{"label": "Correct"}, {"label": "Wrong"}], items: [{"text": "Open the file in append mode", "b": 0}, {"text": "Open the file in write mode", "b": 1}, {"text": "Write the name if the mark is less than 20", "b": 0}, {"text": "Write the mark as well as the name", "b": 1}, {"text": "Repeat for each student", "b": 0}, {"text": "Close the file before the first student", "b": 1}], done: "Append keeps the old data." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Stepwise refinement", "Adding detail until each step can be coded"], ["Structured English", "Numbered steps in words, no pseudocode"], ["Sequence", "Steps in order"], ["Iteration", "Repeating steps"], ["Append mode", "Adds to a file without overwriting it"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the algorithm for copying a file into an array in order.", items: ["Open the file for reading", "Set the index to 1", "Repeat until the end of the file is reached", "Read a line, store it in the array at the index, add 1 to the index", "Close the file"], done: "Open, index, loop, body, close." });
Lib.calc($("#c1"), { qs: [
  {"q": "A file has 4 lines copied into an array starting at index 1. What is the index after the last line is stored and incremented?", "a": 5, "unit": "", "tol": 0.01, "hint": "4 lines, then +1.", "sol": "<b>5</b>."},
  {"q": "An array has 65 elements and the algorithm checks each once. How many loop passes?", "a": 65, "unit": "", "tol": 0.01, "hint": "One per element.", "sol": "<b>65</b>."},
  {"q": "Of 65 elements, 40 are blank. How many lines are written to the file?", "a": 25, "unit": "", "tol": 0.01, "hint": "65 − 40.", "sol": "<b>25</b>."},
  {"q": "A student list has 35 students and the mark under 20 for 6 of them. How many names are appended?", "a": 6, "unit": "", "tol": 0.01, "hint": "Only those under 20.", "sol": "<b>6</b>."},
  {"q": "A string is to be built by repeating a character 5 times. How many times is the loop body run if the counter counts down from 5 to 0 (loop while counter > 0)?", "a": 5, "unit": "", "tol": 0.01, "hint": "5, 4, 3, 2, 1.", "sol": "<b>5</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Stepwise refinement:", opts: ["Adds detail until steps can be coded", "Compiles the code", "Removes steps", "Draws the screen"], a: 0, why: "Adds detail." },
  { q: "To keep existing data in a file, open it in:", opts: ["Append mode", "Write mode", "Read mode only", "Delete mode"], a: 0, why: "Append." },
  { q: "A loop that repeats until the end of a file is:", opts: ["Iteration", "Selection", "Sequence", "Declaration"], a: 0, why: "Iteration." },
  { q: "Structured English contains:", opts: ["No pseudocode statements", "Only code", "Only flowcharts", "Compiler errors"], a: 0, why: "No pseudocode." },
  { q: "Before a counting loop you should:", opts: ["Initialise the variable", "Close the file", "Output the result", "Nothing"], a: 0, why: "Initialise." },
  { q: "A decision with a loop back is usually a:", opts: ["WHILE loop", "FUNCTION", "DECLARE", "CASE"], a: 0, why: "WHILE." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Stepwise refinement", "More detail until directly codeable."],
  ["Structured English", "Numbered words; no pseudocode."],
  ["Sequence", "Steps in order."],
  ["Selection", "A test and a choice."],
  ["Iteration", "A loop with an end condition."],
  ["Append", "Add to the end of a file."],
  ["Initialise", "Set before the loop."],
  ["Increment", "Add 1 each pass."],
] });
