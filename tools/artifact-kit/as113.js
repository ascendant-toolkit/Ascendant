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
  const draw = (s) => { const k = Math.round(s.i); const L = ["IF IsAdult(17) THEN", "Age ← 17  (argument 17 into parameter Age)", "17 >= 18 is FALSE", "RETURN FALSE", "IF FALSE THEN"]; let o = ""; L.forEach((t, i) => o += SV.rect(10, 8 + i * 26, 320, 22, i === k ? "f3" : "cell", { rx: 4 }) + SV.text(18, 24 + i * 26, t, "lbl bd", { style: "font-size:12px;font-family:monospace" })); return o; };
  Lib.stepper($("#stA"), { w: 340, h: 145, label: "Function call", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["The function is called inside the IF.", "The argument 17 is passed to the parameter.", "The body runs.", "A value is returned.", "The call is replaced by the returned value."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(10, 10, 120, 34, "cell", { rx: 6 }) + SV.text(20, 32, "X = " + (k >= 3 ? "10" : "5"), "lbl bd", { style: "font-size:14px;font-family:monospace" }); if (k >= 1) o += SV.rect(190, 10, 120, 34, "f3", { rx: 6 }) + SV.text(200, 32, "N = " + (k >= 2 ? "10" : "5"), "lbl bd", { style: "font-size:14px;font-family:monospace" }); o += SV.text(10, 74, ["Before the call", "BYREF: N is X itself (BYVAL: a copy)", "N ← N * 2 inside the procedure", "X is now 10 (BYVAL: still 5)"][k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 330, h: 92, label: "BYREF", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["X holds 5.", "CALL Double(X) with BYREF.", "The procedure doubles N.", "The change is seen by the caller."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(10, 6, 320, 28, k === 0 ? "f3" : "cell", { rx: 5 }) + SV.text(18, 24, "GLOBAL  Volume = 7   (visible everywhere)", "lbl bd", { style: "font-size:12px" }); o += SV.rect(10, 44, 150, 62, k === 1 ? "f3" : "cell", { rx: 5 }) + SV.text(18, 62, "PROCEDURE A", "lbl bd", { style: "font-size:12px" }) + SV.text(18, 80, "local Temp = 1", "lbl", { style: "font-size:12px;font-family:monospace" }) + SV.text(18, 96, "can use Volume", "lbl", { style: "font-size:11px" }); o += SV.rect(180, 44, 150, 62, k === 2 ? "f3" : "cell", { rx: 5 }) + SV.text(188, 62, "PROCEDURE B", "lbl bd", { style: "font-size:12px" }) + SV.text(188, 80, "local Temp = 99", "lbl", { style: "font-size:12px;font-family:monospace" }) + SV.text(188, 96, "its own Temp", "lbl", { style: "font-size:11px" }); return o; };
  Lib.stepper($("#stC"), { w: 340, h: 118, label: "Scope", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["A global variable can be used by every subroutine.", "A's local Temp exists only inside A.", "B has a separate Temp: no clash, and B cannot see A's."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const inp = $("#pm_x"); const go = (ref) => { const x = Math.round(+inp.value || 0); const n = x * 2; $("#pmV").innerHTML = `<div class="tw"><table class="t mono"><tr><th>Passing</th><th>X before</th><th>N after Double</th><th>X after</th></tr><tr><td>${ref ? "BYREF" : "BYVAL"}</td><td>${x}</td><td>${n}</td><td><b>${ref ? n : x}</b></td></tr></table></div><div class="verdict">${ref ? "BYREF: N is the caller's variable, so X changed." : "BYVAL: N is a copy, so X is unchanged."}</div>`; };
  $("#pm_val").onclick = () => go(false); $("#pm_ref").onclick = () => go(true); go(false);
})();
btnTable("scB", "scO", [
  ["A variable declared inside PROCEDURE A", "Only in A", "local: exists while A runs"],
  ["A variable declared before all procedures", "Anywhere", "global"],
  ["A parameter in a header", "Only in that subroutine", "it behaves like a local variable"],
  ["Two procedures each declare Temp", "Each has its own Temp", "locals do not clash"]
], ["Variable", "Where it can be used", "Why"]);
btnTable("pfB", "pfO", [
  ["IsPrime(N) returns TRUE or FALSE", "Function", "returns a value"],
  ["ShowMenu() prints options", "Procedure", "an action, no value"],
  ["Average(A, B, C) gives the mean", "Function", "returns a value"],
  ["SaveScores() writes the scores to a file", "Procedure", "an action"],
  ["CheckFiles(NameRoot) returns the number found", "Function", "RETURNS INTEGER"]
], ["Subroutine", "Type", "Why"]);
Lib.classify($("#cl1"), { prompt: "Is this a procedure or a function?", buckets: [{"label": "Procedure"}, {"label": "Function"}], items: [{"text": "Returns TRUE if a number is prime", "b": 1}, {"text": "Outputs a report to the screen", "b": 0}, {"text": "Returns the average of three marks", "b": 1}, {"text": "Writes a new line to a file", "b": 0}, {"text": "FUNCTION ... RETURNS INTEGER", "b": 1}, {"text": "Called with CALL", "b": 0}], done: "A function returns a value." });
Lib.classify($("#cl2"), { prompt: "Local or global?", buckets: [{"label": "Local"}, {"label": "Global"}], items: [{"text": "Exists only while the subroutine runs", "b": 0}, {"text": "Can be changed from any subroutine", "b": 1}, {"text": "Declared outside any subroutine", "b": 1}, {"text": "Its name can be reused in another subroutine", "b": 0}, {"text": "A fault in it may be anywhere in the program", "b": 1}, {"text": "The better choice for most variables", "b": 0}], done: "Local is safe; global is shared." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Parameter", "A name and type in the subroutine header"], ["Argument", "The value supplied when it is called"], ["BYREF", "Changes the caller's variable"], ["BYVAL", "Works on a copy"], ["RETURN", "Sends a value back from a function"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of a function call IsAdult(17) in order.", items: ["The program reaches IsAdult(17) in an expression", "The value 17 is passed to the parameter Age", "The function body runs: 17 >= 18 is false", "RETURN FALSE sends a value back", "The call is replaced by FALSE in the expression"], done: "Call, pass, run, return, replace." });
Lib.calc($("#c1"), { qs: [
  {"q": "MID(InString, Counter, 1) is called with how many parameters?", "a": 3, "unit": "", "tol": 0.01, "hint": "String, start, length.", "sol": "<b>3</b>."},
  {"q": "A procedure has the header PROCEDURE P(A : INTEGER, BYREF B : REAL, C : STRING). How many parameters does it take?", "a": 3, "unit": "", "tol": 0.01, "hint": "Count A, B, C.", "sol": "<b>3</b>."},
  {"q": "A procedure doubles BYVAL N. X = 5 before the call. What is X after?", "a": 5, "unit": "", "tol": 0.01, "hint": "A copy was changed.", "sol": "<b>5</b>."},
  {"q": "The same procedure with BYREF N. What is X after?", "a": 10, "unit": "", "tol": 0.01, "hint": "The original is changed.", "sol": "<b>10</b>."},
  {"q": "A program has 4 subroutines. Two are functions. How many are procedures?", "a": 2, "unit": "", "tol": 0.01, "hint": "4 − 2.", "sol": "<b>2</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A function differs from a procedure because it:", opts: ["Returns a value", "Has no parameters", "Cannot be called", "Has no header"], a: 0, why: "Returns." },
  { q: "In PROCEDURE MyProc(Count : INTEGER), Count is a:", opts: ["Parameter", "Argument", "Constant", "Library"], a: 0, why: "In the header." },
  { q: "BYREF means the subroutine:", opts: ["Changes the caller's variable", "Works on a copy", "Cannot use the value", "Returns a string"], a: 0, why: "Reference." },
  { q: "A local variable:", opts: ["Exists only in its subroutine", "Exists everywhere", "Cannot be changed", "Is a constant"], a: 0, why: "Local." },
  { q: "A benefit of a library routine:", opts: ["It is tried and tested", "It is always slower", "It cannot be reused", "It has no parameters"], a: 0, why: "Tested." },
  { q: "A feature of readable code:", opts: ["Meaningful identifiers and indentation", "Single-letter names only", "No blank lines", "No comments"], a: 0, why: "Readability." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Procedure", "Does a task; no value returned."],
  ["Function", "Returns a value."],
  ["Parameter", "In the header."],
  ["Argument", "In the call."],
  ["BYVAL", "A copy."],
  ["BYREF", "The original."],
  ["Local", "Only inside the subroutine."],
  ["Global", "Anywhere in the program."],
] });
