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
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, w, t, kind, on) => (kind === "dec" ? SV.path(`M${x},${y - 22} L${x + w / 2},${y} L${x},${y + 22} L${x - w / 2},${y} Z`, on ? "f3" : "cell") : SV.rect(x - w / 2, y - 14, w, 28, on ? "f3" : "cell", { rx: kind === "term" ? 14 : 3 })) + SV.text(x, y + 4, t, "lbl", { "text-anchor": "middle", style: "font-size:10px" });
    let o = B(100, 20, 90, "START", "term", k >= 0) + (k >= 1 ? B(100, 65, 150, "Total ← 0", "proc", true) : "") + (k >= 2 ? B(100, 110, 150, "INPUT Number", "proc", true) : "") + (k >= 3 ? B(100, 160, 150, "Number = 0 ?", "dec", true) : "") + (k >= 4 ? B(300, 160, 150, "Total ← Total + Number", "proc", true) : "") + (k >= 5 ? B(100, 215, 130, "OUTPUT Total", "proc", true) : "");
    if (k >= 4) o += SV.path("M175,160 H225", "ax") + SV.path("M300,146 V110 H175", "ax"); return o; };
  Lib.stepper($("#stA"), { w: 440, h: 240, label: "Flowchart", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["START.", "Initialise Total before the loop.", "Input a number (in the loop).", "A decision: is it 0?", "NO: add to Total and loop back to the input.", "YES: output Total."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const ins = [5, 2, -3, 0]; const draw = (s) => { const k = Math.round(s.i); let pos = 0, cp = 0, neg = 0, cn = 0; for (let i = 0; i < Math.min(k, 3); i++) { if (ins[i] > 0) { pos += ins[i]; cp++; } else { neg += ins[i]; cn++; } }
    let o = SV.text(20, 22, "inputs: " + ins.slice(0, Math.min(k + 1, 4)).join(", "), "lbl bd", { style: "font-size:13px" }); [["PosSum", pos], ["PosCount", cp], ["NegSum", neg], ["NegCount", cn]].forEach(([n, v], i) => o += SV.rect(20 + i * 110, 40, 100, 44, "cell", { rx: 6 }) + SV.text(70 + i * 110, 58, n, "sm", { "text-anchor": "middle" }) + SV.text(70 + i * 110, 76, v, "lbl bd", { "text-anchor": "middle" }));
    o += SV.text(20, 112, k < 3 ? "input " + ins[k] + (ins[k] > 0 ? ": positive, add to PosSum" : ": negative, add to NegSum") : "input 0: leave the loop and output the four values", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 460, h: 130, label: "Trace", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["First input 5.", "Next input 2.", "Next input −3.", "Input 0 ends the loop."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const L = ["Total ← 0", "FOR i ← 1 TO 3", "IF Total > 5 THEN", "OUTPUT Total"]; const kinds = ["assignment", "iteration", "selection", "input/output"]; const draw = (s) => { const k = Math.round(s.i); let o = ""; L.forEach((l, i) => { o += SV.rect(20, 14 + i * 34, 220, 28, i === k ? "f3" : "cell", { rx: 5 }) + SV.text(30, 33 + i * 34, l, "lbl", { style: "font-size:12px" }) + (i === k ? SV.text(260, 33 + i * 34, "← " + kinds[i], "lbl bd t3", { style: "font-size:12px" }) : ""); }); return o; };
  Lib.stepper($("#stC"), { w: 440, h: 160, label: "Constructs", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: kinds.map((c, i) => ({ cap: "This line is <b>" + c + "</b>.", s: { i } })) });
})();

(function () {
  let pos = 0, cp = 0, neg = 0, cn = 0, done = false, log = [];
  const paint = () => { $("#flV").innerHTML = `PosSum = <b>${pos}</b>, PosCount = <b>${cp}</b>, NegSum = <b>${neg}</b>, NegCount = <b>${cn}</b>.` + (log.length ? "<br>Inputs: " + log.join(", ") : "") + (done ? "<br><b>0 entered: the loop ends and the four values are output.</b>" : ""); };
  const add = (v) => { if (done) return; log.push(v); if (v === 0) done = true; else if (v > 0) { pos += v; cp++; } else { neg += v; cn++; } paint(); };
  $("#fl_p5").onclick = () => add(5); $("#fl_p2").onclick = () => add(2); $("#fl_m3").onclick = () => add(-3); $("#fl_m7").onclick = () => add(-7); $("#fl_0").onclick = () => add(0); $("#fl_r").onclick = () => { pos = cp = neg = cn = 0; done = false; log = []; paint(); }; paint();
})();
btnTable("cB", "cO", [
  ["Total ← Total + 1", "Assignment", "Stores a value"],
  ["IF Mark > 74 THEN", "Selection", "Chooses"],
  ["WHILE Index < 7", "Iteration", "Repeats while true"],
  ["CASE OF Option", "Selection", "Chooses between cases"],
  ["REPEAT INPUT Value UNTIL ...", "Iteration (and input)", "Repeats; one line, two constructs"]
], ["Line", "Construct", "Why"]);
btnTable("sB", "sO", [
  ["START / END", "Terminator (rounded)", "Begins and ends"],
  ["INPUT / OUTPUT", "Parallelogram", "Data in or out"],
  ["Total ← 0", "Rectangle", "A process (assignment)"],
  ["Number = 0 ?", "Diamond", "A decision with YES and NO"],
  ["CALL Update(...)", "Rectangle with double sides", "A subroutine call"]
], ["Step", "Symbol", "Meaning"]);
Lib.classify($("#cl1"), { prompt: "Which construct does the pseudocode use?", buckets: [{"label": "Assignment"}, {"label": "Selection"}, {"label": "Iteration"}], items: [{"text": "Total ← Total + 1", "b": 0}, {"text": "IF Mark > 74 THEN", "b": 1}, {"text": "FOR Index ← 1 TO 10", "b": 2}, {"text": "CASE OF Option", "b": 1}, {"text": "WHILE IsClosed", "b": 2}, {"text": "Discount ← TRUE", "b": 0}], done: "Store, choose, repeat." });
Lib.classify($("#cl2"), { prompt: "Which flowchart symbol is used?", buckets: [{"label": "Terminator"}, {"label": "Parallelogram"}, {"label": "Rectangle"}, {"label": "Diamond"}], items: [{"text": "START", "b": 0}, {"text": "INPUT Number", "b": 1}, {"text": "Count ← Count + 1", "b": 2}, {"text": "Number = 0 ?", "b": 3}, {"text": "END", "b": 0}, {"text": "OUTPUT Total", "b": 1}], done: "Input/output: parallelogram. Decision: diamond." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Algorithm", "A sequence of steps that solves a problem"], ["Identifier table", "Variables with name, type, purpose and example"], ["Assignment", "Storing a value in a variable"], ["Selection", "Choosing which statements to run"], ["Iteration", "Repeating statements"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the algorithm for 'sum the numbers until 0' in order.", items: ["Set Total to 0", "Input a number", "If it is 0, stop and output Total", "Add the number to Total", "Go back and input the next number"], done: "Initialise, input, test, add, repeat." });
Lib.calc($("#c1"), { qs: [
  {"q": "The algorithm sums inputs 5, 2, −3, −7, 0. What is the sum of the positive values?", "a": 7, "unit": "", "tol": 0.01, "hint": "5 + 2.", "sol": "<b>7</b>."},
  {"q": "For the same inputs what is the count of negative values?", "a": 2, "unit": "", "tol": 0.01, "hint": "−3 and −7.", "sol": "<b>2</b>."},
  {"q": "The loop in the algorithm runs once for each non-zero input. How many times for 5, 2, −3, −7, 0?", "a": 4, "unit": "", "tol": 0.01, "hint": "The 0 ends it.", "sol": "<b>4</b> (the 0 is input but not processed)."},
  {"q": "A FOR loop is FOR Index ← 4 TO 6. How many times does the body run?", "a": 3, "unit": "", "tol": 0.01, "hint": "4, 5, 6.", "sol": "<b>3</b>."},
  {"q": "A flowchart has 2 diamonds and each has YES and NO exits. How many labelled exits?", "a": 4, "unit": "", "tol": 0.01, "hint": "2 × 2.", "sol": "<b>4</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A decision is drawn as a:", opts: ["Diamond", "Rectangle", "Oval", "Parallelogram"], a: 0, why: "Diamond." },
  { q: "A WHILE loop tests:", opts: ["Before the body", "After the body", "Never", "Once"], a: 0, why: "First." },
  { q: "A REPEAT loop tests:", opts: ["After the body", "Before the body", "Never", "Twice"], a: 0, why: "Last." },
  { q: "An identifier table has:", opts: ["Variable names and data types", "Only passwords", "Only loops", "Files"], a: 0, why: "Names and types." },
  { q: "INPUT is drawn as a:", opts: ["Parallelogram", "Diamond", "Oval", "Triangle"], a: 0, why: "Parallelogram." },
  { q: "A good variable name:", opts: ["Says what it holds", "Is a single letter", "Is Temp", "Is X"], a: 0, why: "Meaningful." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Algorithm", "Steps that solve a problem."],
  ["Identifier table", "Name, type, purpose, example."],
  ["Terminator", "START and END."],
  ["Parallelogram", "Input and output."],
  ["Rectangle", "Process (assignment)."],
  ["Diamond", "Decision: YES and NO."],
  ["WHILE", "Test first."],
  ["REPEAT ... UNTIL", "Test last."],
] });
