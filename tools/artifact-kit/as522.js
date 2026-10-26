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
  const lines = ["total ← 0", "FOR n ← 1 TO 3", "  total ← total + n", "NEXT n", "OUTPUT total"]; const draw = (s) => { const k = Math.round(s.i); const st = [[0, "-"], [1, "n=1"], [2, "total=1"], [1, "n=2"], [2, "total=3"]][k]; let o = ""; lines.forEach((l, i) => { o += SV.rect(20, 14 + i * 28, 260, 24, i === st[0] ? "f3" : "cell", { rx: 4 }) + SV.text(30, 31 + i * 28, (i + 1) + "  " + l, "lbl"); });
    o += SV.rect(320, 14, 200, 80, "cell", { rx: 6 }) + SV.text(330, 34, "watch window", "sm") + SV.text(330, 58, "total = " + [0, 0, 1, 1, 3][k], "lbl bd") + SV.text(330, 80, "n = " + ["?", 1, 1, 2, 2][k], "lbl bd"); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 165, label: "Single stepping", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["Single stepping: line 1 runs, total = 0.", "Line 2: n becomes 1.", "Line 3: total = 0 + 1 = 1.", "Back to the loop: n = 2.", "Line 3 again: total = 1 + 2 = 3."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const lines = ["a ← 5", "b ← 0", "FOR i ← 1 TO 4", "  b ← b + a", "NEXT i", "OUTPUT b"]; const draw = (s) => { const k = Math.round(s.i); let o = ""; lines.forEach((l, i) => { o += SV.circle(26, 26 + i * 28, 7, i === 3 ? "f2" : "cell") + SV.rect(44, 14 + i * 28, 240, 24, k >= 1 && i === 3 ? "f3" : "cell", { rx: 4 }) + SV.text(54, 31 + i * 28, (i + 1) + "  " + l, "lbl"); });
    o += SV.text(310, 40, ["breakpoint set on line 4", "lines 1-3 run normally", "it stops: check b and i"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 560, h: 180, label: "Breakpoint", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Set a <b>breakpoint</b> on line 4.", "Run: lines 1 to 3 execute normally.", "The program <b>stops at the breakpoint</b>; the programmer checks the variables."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 20, 330, 30, k === 3 ? "f1" : "cell", { rx: 4 }) + SV.text(30, 40, ["IF a > 5 THEN", "IF a > 5 THE", "pri", "print("][k], "lbl") + (k === 1 ? SV.path("M30,44 H110", "ax", { style: "stroke:var(--bad);stroke-width:3" }) + SV.text(370, 40, "syntax error underlined", "lbl bd t3", { style: "font-size:12px" }) : "") + (k === 2 ? SV.rect(30, 52, 180, 56, "f3", { rx: 4 }) + SV.text(40, 72, "print", "lbl") + SV.text(40, 92, "printf", "lbl") + SV.text(40, 108, "", "sm") : "");
    o += SV.text(20, 135, ["", "Dynamic syntax check: the error is highlighted as you type", "Context-sensitive prompt: options are shown", "Auto-complete finishes the statement"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 150, label: "Typing", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["A statement is typed.", "A <b>dynamic syntax check</b> underlines the mistake straight away.", "A <b>context-sensitive prompt</b> predicts what is being entered.", "<b>Auto-complete</b> finishes it."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const lines = ["total ← 0", "FOR n ← 1 TO 3", "  total ← total + n", "NEXT n", "OUTPUT total"];
  // pre-computed execution: [line index, total, n, output]
  const run = [[0, 0, "?", ""], [1, 0, 1, ""], [2, 1, 1, ""], [3, 1, 1, ""], [1, 1, 2, ""], [2, 3, 2, ""], [3, 3, 2, ""], [1, 3, 3, ""], [2, 6, 3, ""], [3, 6, 3, ""], [4, 6, 3, "6"]]; let k = -1, bp = new Set();
  const paint = () => { const cur = k >= 0 ? run[k] : null;
    $("#dbP").innerHTML = '<div class="tw"><table class="t mono">' + lines.map((l, i) => `<tr style="${cur && cur[0] === i ? "background:var(--accent-soft);font-weight:700" : ""}"><td><button data-ln="${i}" style="min-width:34px">${bp.has(i) ? "●" : (i + 1)}</button></td><td>${l}</td></tr>`).join("") + "</table></div>";
    $("#dbP").querySelectorAll("button").forEach((b) => b.onclick = () => { const i = +b.dataset.ln; bp.has(i) ? bp.delete(i) : bp.add(i); paint(); });
    $("#dbW").innerHTML = '<div class="tw"><table class="t mono"><tr><th>total</th><th>n</th><th>output</th></tr><tr>' + (cur ? `<td>${cur[1]}</td><td>${cur[2]}</td><td>${cur[3]}</td>` : "<td>·</td><td>·</td><td>·</td>") + "</tr></table></div>";
    $("#dbV").innerHTML = k < 0 ? "Press Step or Run to breakpoint." : k >= run.length - 1 ? "The program has finished and printed 6." : `Stopped on line ${cur[0] + 1}. The report window shows total = ${cur[1]} and n = ${cur[2]}.`; };
  $("#db_step").onclick = () => { if (k < run.length - 1) { k++; paint(); } };
  $("#db_run").onclick = () => { do { k++; } while (k < run.length - 1 && !bp.has(run[k][0])); if (k >= run.length) k = run.length - 1; paint(); };
  $("#db_reset").onclick = () => { k = -1; paint(); }; bp.add(2); paint();
})();
btnTable("fB", "fO", [
  ["Run the program one line at a time", "Single stepping", "Debugging"],
  ["Stop at line 40 to look at a variable", "Breakpoint", "Debugging"],
  ["Show the values of variables as they change", "Report (watch) window", "Debugging"],
  ["Underline a mistake as you type", "Dynamic syntax check", "Presentation / writing"],
  ["Suggest the rest of a statement", "Context-sensitive prompt", "Presentation / writing"],
  ["Hide the body of a long function", "Collapse code block", "Presentation"]
], ["Need", "Feature", "Type"]);
btnTable("pB", "pO", [
  ["Prettyprint", "Presentation", "Formats the code"],
  ["Breakpoint", "Debugging", "Stops at a set line"],
  ["Colour coding", "Presentation", "Shows keywords and structure"],
  ["Single stepping", "Debugging", "One line at a time"],
  ["Auto-indentation", "Presentation", "Shows the structure"],
  ["Variable watch window", "Debugging", "Shows values change"]
], ["Feature", "Type", "Why"]);
Lib.classify($("#cl1"), { prompt: "Presentation feature or debugging feature?", buckets: [{"label": "Presentation"}, {"label": "Debugging"}], items: [{"text": "Prettyprint", "b": 0}, {"text": "Single stepping", "b": 1}, {"text": "Expand and collapse code blocks", "b": 0}, {"text": "Breakpoints", "b": 1}, {"text": "Auto-indentation", "b": 0}, {"text": "Report (variable watch) window", "b": 1}], done: "Presentation: how the code looks. Debugging: finding errors." });
Lib.classify($("#cl2"), { prompt: "Single stepping or breakpoint?", buckets: [{"label": "Single stepping"}, {"label": "Breakpoint"}], items: [{"text": "Executes one line and then stops", "b": 0}, {"text": "Stops the code at a set line", "b": 1}, {"text": "Used to check a value at a particular statement", "b": 1}, {"text": "Used to see the effect of every statement", "b": 0}, {"text": "The technical term for the position at which the program stops", "b": 1}, {"text": "The program waits for the next click after each line", "b": 0}], done: "Stepping: one line. Breakpoint: a chosen line." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Context-sensitive prompt", "Displays predictions of the code being entered"], ["Dynamic syntax check", "Underlines or highlights statements that break the rules of the language"], ["Breakpoint", "Stops the code executing at a set line"], ["Single stepping", "Executes one line of the program and then stops"], ["Report window", "Outputs the contents of variables and data structures"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the debugging steps in order.", items: ["Set a breakpoint at the line before the suspected error", "Run the program: it stops at the breakpoint", "Check the variables in the report window", "Single step through the next lines", "Spot where a variable first holds a wrong value"], done: "Breakpoint, run, check, step, spot." });
Lib.calc($("#c1"), { qs: [
  {"q": "A program has 120 lines and a breakpoint on line 80. How many lines run before it stops (lines 1 to 79)?", "a": 79, "unit": "", "tol": 0.01, "hint": "Up to the line before.", "sol": "<b>79</b>."},
  {"q": "A loop runs 8 times with 3 lines in the body. How many single steps to run the loop body completely?", "a": 24, "unit": "", "tol": 0.01, "hint": "8 × 3.", "sol": "<b>24</b>."},
  {"q": "total starts at 0 and adds 4 each loop. What is total after 5 loops?", "a": 20, "unit": "", "tol": 0.01, "hint": "5 × 4.", "sol": "<b>20</b>."},
  {"q": "How many presentation features are in the Learn tab table (colour coding, prettyprint, auto-indentation, expand/collapse, auto-complete, auto-correct, dynamic syntax checks)?", "a": 7, "unit": "", "tol": 0.01, "hint": "Count the rows.", "sol": "<b>7</b>."},
  {"q": "A student sets 2 breakpoints. The program stops at both in turn. How many times must they press Run to reach the end of the program (after the last breakpoint)?", "a": 3, "unit": "", "tol": 0.01, "hint": "To the 1st, the 2nd, then the end.", "sol": "<b>3</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A breakpoint:", opts: ["Stops the program at a set line", "Runs one line", "Formats code", "Compiles"], a: 0, why: "Stops at a set line." },
  { q: "Single stepping:", opts: ["Runs one line then stops", "Runs to the end", "Highlights errors", "Indents code"], a: 0, why: "One line." },
  { q: "Prettyprint is a:", opts: ["Presentation feature", "Debugging feature", "Translator", "Utility"], a: 0, why: "Presentation." },
  { q: "The report window shows:", opts: ["The contents of variables", "The source code colours", "The compiler output only", "The file size"], a: 0, why: "Variables." },
  { q: "Dynamic syntax checking:", opts: ["Highlights errors as you type", "Runs the program", "Compresses code", "Creates a back-up"], a: 0, why: "As you type." },
  { q: "An IDE is:", opts: ["An application with tools to write and test programs", "A type of RAM", "An assembler only", "A file format"], a: 0, why: "Tools together." },
] });
Lib.cards($("#fc1"), { cards: [
  ["IDE", "Tools to write, translate, test and debug."],
  ["Presentation", "Colour, prettyprint, indentation, collapse."],
  ["Context-sensitive prompt", "Shows predictions as you type."],
  ["Dynamic syntax check", "Underlines errors as you type."],
  ["Single stepping", "One line then stop."],
  ["Breakpoint", "Stops at a set line."],
  ["Report window", "Shows variable values."],
  ["Debugging", "Finding and fixing errors."],
] });
