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

const MONO = "font-family:var(--mono);font-size:13px";
function codeLines(x, y, lines, hl, w, lh) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 3, i === hl ? "cell-warn" : "cell", { rx: 4 }) + SV.text(x + 8, y + i * lh + lh / 2 + 3, l, "lbl", { style: "font-family:var(--mono);font-size:11px;white-space:pre" })).join("");
}
function vbox(x, y, name, val, cls, w) {
  return SV.text(x, y - 7, name, "sm") + SV.rect(x, y, w, 34, cls || "f2", { rx: 6, ...op(0.6) }) + SV.rect(x, y, w, 34, "ax", { rx: 6, fill: "none" }) + SV.text(x + w / 2, y + 22, String(val), "lbl bd", { "text-anchor": "middle", style: MONO });
}
/* a column of file rows. o: x,y,t,r + optional w, lh, hl (warn row), ok[], no[], nw (new row), ptr (pointer row), ptrLabel, addr (show row numbers), eof */
function fcol(o) {
  const w = o.w || 210, lh = o.lh || 28, rows = o.r || [];
  let s = SV.text(o.x, o.y - 8, o.t, "sm");
  if (!rows.length) s += SV.rect(o.x, o.y, w, lh - 4, "cell", { rx: 5, ...op(0.5) }) + SV.text(o.x + 10, o.y + lh / 2 + 3, "(empty)", "sm");
  rows.forEach((r, i) => {
    let c = "cell";
    if (o.ok && o.ok.includes(i)) c = "cell-ok";
    if (o.no && o.no.includes(i)) c = "cell-no";
    if (o.nw === i) c = "f3";
    if (o.hl === i) c = "cell-warn";
    s += SV.rect(o.x, o.y + i * lh, w, lh - 4, c, { rx: 5 });
    if (o.addr) s += SV.text(o.x + 10, o.y + i * lh + lh / 2 + 3, String(i), "sm", { style: MONO }) + SV.text(o.x + 36, o.y + i * lh + lh / 2 + 3, r, "lbl", { style: MONO });
    else s += SV.text(o.x + 10, o.y + i * lh + lh / 2 + 3, r, "lbl", { style: MONO });
  });
  if (o.ptr !== undefined && o.ptr !== null && o.ptr >= 0) s += SV.text(o.x + w + 8, o.y + o.ptr * lh + lh / 2 + 3, "◀ " + (o.ptrLabel || "pointer"), "sm");
  if (o.eof) s += SV.text(o.x, o.y + rows.length * lh + 12, "end of file", "sm");
  return s;
}
function stepDraw(C, t) {
  let o = "", y = 8;
  if (C.ps) {
    o += SV.text(8, 14, "Pseudocode", "sm");
    const wa = Math.max(...C.ps.map((l) => l.length)) * 6.6 + 18, wb = Math.max(...C.py.map((l) => l.length)) * 6.6 + 18, ex = Math.max(0, (744 - wa - wb - 14) / 2), xb = 8 + wa + ex + 14;
    o += SV.text(xb, 14, "Python", "sm") + codeLines(8, 22, C.ps, t.p, wa + ex, C.lh) + codeLines(xb, 22, C.py, t.y, wb + ex, C.lh);
    y = 22 + Math.max(C.ps.length, C.py.length) * C.lh + 14;
  }
  if (t.v && t.v.length) { t.v.forEach((v, j) => { o += vbox(8 + j * C.vw, y + 16, v[0], v[1], v[2], C.vw - 12); }); y += 82; }
  (t.f || []).forEach((f) => { o += fcol({ ...f, y: y + f.y }); });
  (t.t || []).forEach((q) => { o += SV.text(q[0], y + q[1], q[2], q[3] || "sm"); });
  return o;
}
const lineHTML = (L) => '<div class="code"><pre class="cp">' + L.map((l) => `<span class="ln">${esc(l) || " "}</span>`).join("") + "</pre></div>";
(function () { const C = {"ps": ["INPUT Number", "Result <- 100 / Number", "OUTPUT Result", "OUTPUT \"Finished\""], "py": ["Number = int(input(\"Enter a number: \"))", "Result = 100 / Number", "print(Result)", "print(\"Finished\")"], "lh": 24, "vw": 150}, ST = [{"c": "A short program divides 100 by a number the user types. The user is going to type <b>0</b>.", "p": -1, "y": -1, "v": [["Number", ""], ["Result", ""]], "f": []}, {"c": "The first line reads the input. <code>Number</code> is 0.", "p": 0, "y": 0, "v": [["Number", "0"], ["Result", ""]], "f": []}, {"c": "<code>100 / Number</code> cannot be worked out. An exception is <b>raised</b>: ZeroDivisionError.", "p": 1, "y": 1, "v": [["Number", "0"], ["Result", ""]], "f": [], "t": [[330, 0, "ZeroDivisionError: division by zero", "lbl bd t2"]]}, {"c": "Nothing responds to it, so the program <b>halts</b>. The last two lines never run and the user sees a system error message.", "p": -1, "y": -1, "v": [["Number", "0"], ["Result", ""]], "f": [], "t": [[330, 0, "Program halted at line 2", "lbl bd t2"], [330, 30, "OUTPUT Result and OUTPUT \"Finished\" never run", "sm"]]}];
  Lib.stepper($("#stA"), { w: 760, h: 274, label: "A program with no exception handling", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3200, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "A program can run perfectly for years and still meet an exception. The cause is one of three kinds. First, <b>programming errors</b>: something the code asks for that cannot be done.", "f": [{"x": 20, "y": 20, "t": "Programming error", "r": ["divide by zero", "index out of range", "wrong data type"], "w": 220}]}, {"c": "Second, <b>user errors</b>: the user gives the program something it cannot use.", "f": [{"x": 20, "y": 20, "t": "Programming error", "r": ["divide by zero", "index out of range", "wrong data type"], "w": 220}, {"x": 260, "y": 20, "t": "User error", "r": ["text for a number", "wrong file name", "empty input"], "w": 220}]}, {"c": "Third, <b>hardware or system failure</b>: something outside the program stops working.", "f": [{"x": 20, "y": 20, "t": "Programming error", "r": ["divide by zero", "index out of range", "wrong data type"], "w": 220}, {"x": 260, "y": 20, "t": "User error", "r": ["text for a number", "wrong file name", "empty input"], "w": 220}, {"x": 500, "y": 20, "t": "Hardware failure", "r": ["disk crash", "disk full", "printer or network lost"], "w": 220}]}, {"c": "In every case the program is stopped by an <b>unexpected event while it is running</b>. That is what makes it an exception, rather than a syntax error found before the program starts.", "f": [{"x": 20, "y": 20, "t": "Programming error", "r": ["divide by zero", "index out of range", "wrong data type"], "w": 220}, {"x": 260, "y": 20, "t": "User error", "r": ["text for a number", "wrong file name", "empty input"], "w": 220}, {"x": 500, "y": 20, "t": "Hardware failure", "r": ["disk crash", "disk full", "printer or network lost"], "w": 220}]}];
  Lib.stepper($("#stB"), { w: 760, h: 133, label: "The three causes of an exception", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3600, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "When an exception is not handled, Python prints a message like this and stops.", "f": [{"x": 20, "y": 20, "t": "What Python prints", "r": ["Traceback (most recent call last):", "  File \"prog.py\", line 2, in <module>", "    Result = 100 / Number", "ZeroDivisionError: division by zero"], "w": 520, "hl": null}]}, {"c": "The second line gives the <b>line number</b> in the program where it happened: line 2.", "f": [{"x": 20, "y": 20, "t": "What Python prints", "r": ["Traceback (most recent call last):", "  File \"prog.py\", line 2, in <module>", "    Result = 100 / Number", "ZeroDivisionError: division by zero"], "w": 520, "hl": 1}]}, {"c": "The third line is the <b>statement</b> that raised the exception.", "f": [{"x": 20, "y": 20, "t": "What Python prints", "r": ["Traceback (most recent call last):", "  File \"prog.py\", line 2, in <module>", "    Result = 100 / Number", "ZeroDivisionError: division by zero"], "w": 520, "hl": 2}]}, {"c": "The last line is the <b>name of the exception</b> and the reason: ZeroDivisionError, because the program divided by zero.", "f": [{"x": 20, "y": 20, "t": "What Python prints", "r": ["Traceback (most recent call last):", "  File \"prog.py\", line 2, in <module>", "    Result = 100 / Number", "ZeroDivisionError: division by zero"], "w": 520, "hl": 3}]}];
  Lib.stepper($("#stC"), { w: 760, h: 143, label: "Reading a Python error message", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3400, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();

btnTable("eB", "eO", [
  ["100 / 0", "print(100 / 0)", "A number cannot be divided by zero", "ZeroDivisionError", "Programming error"],
  ["List index", "Numbers = [4, 8, 15]; print(Numbers[5])", "The list has 3 items, so index 5 does not exist", "IndexError", "Programming error"],
  ["Text to number", "Age = int(\"abc\")", "\"abc\" cannot be turned into a whole number", "ValueError", "User error (typed input)"],
  ["Missing file", "open(\"missing.txt\", \"r\")", "No file with that name exists to open", "FileNotFoundError", "User error (wrong file name)"],
  ["Adding types", "print(\"5\" + 3)", "A string and a number cannot be added", "TypeError", "Programming error"],
  ["Disk full", "File.write(Line)  # no space left", "The device cannot store any more data", "OSError", "Hardware or system failure"]
], ["Statement", "Code", "What goes wrong", "Exception", "Cause"]);
btnTable("kB", "kO", [
  ["print(\"Hi\"", "print(\"Hi\"", "The bracket is never closed, so Python cannot read the line", "Syntax error", "Found before the program runs"],
  ["Average", "Average = Total * Count", "It runs, but should be Total / Count, so the answer is wrong", "Logic error", "The program does not stop"],
  ["int(\"abc\")", "Age = int(\"abc\")", "The program stops at this line while it is running", "Exception", "ValueError"],
  ["Wrong test", "IF Score > 50 THEN  (should be < 50)", "Runs to the end with the wrong result", "Logic error", "The program does not stop"],
  ["No file", "open(\"missing.txt\")", "The file is missing when the program tries to open it", "Exception", "FileNotFoundError"]
], ["Example", "Code", "What happens", "Kind", "Detail"]);
Lib.classify($("#cl1"), { prompt: "Which cause is this?", buckets: [{"label": "Programming error"}, {"label": "User error"}, {"label": "Hardware failure"}], items: [{"text": "Dividing by a variable that is 0", "b": 0}, {"text": "Using index 10 in a list of 5 items", "b": 0}, {"text": "Typing a name where a number is asked for", "b": 1}, {"text": "Giving the name of a file that does not exist", "b": 1}, {"text": "A disk crash while saving", "b": 2}, {"text": "The connection to a printer is lost", "b": 2}, {"text": "Adding a string to an integer", "b": 0}, {"text": "Leaving a required input empty", "b": 1}], done: "Programming: the code asks for something impossible. User: bad input from the user. Hardware: something outside the program fails." });
Lib.order($("#o1"), { prompt: "Put these events in order when an exception is not handled.", items: ["The program is running normally", "A statement cannot be carried out", "An exception is raised", "The rest of the program is skipped", "The program halts and an error message is shown"], done: "Running, impossible statement, exception raised, rest skipped, halt and message." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Exception", "An unexpected event during execution that disrupts the normal flow"], ["Syntax error", "A mistake in the code found before the program runs"], ["Logic error", "The program runs but gives wrong results"], ["ZeroDivisionError", "Raised when a number is divided by zero"], ["IndexError", "Raised when an index does not exist in a list"], ["ValueError", "Raised when a value has the right type but cannot be used, such as int(\"abc\")"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A program runs print(\"A\"), then print(5 / 0), then print(\"B\") with no handling. How many lines of output does it produce before it halts?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the first print completes.", "sol": "<b>1</b> (A)."},
  {"q": "A list has 5 items numbered from 0. What is the highest index that does NOT raise an IndexError?", "a": 4, "unit": "", "tol": 0.01, "hint": "0, 1, 2, 3, 4.", "sol": "<b>4</b>."},
  {"q": "A loop converts 10 lines of a file with int() and has no handling. The fourth line is abc. How many numbers have been stored when the program halts?", "a": 3, "unit": "", "tol": 0.01, "hint": "Lines 1, 2 and 3 were fine.", "sol": "<b>3</b>."},
  {"q": "Of these four, how many are hardware or system failures: disk crash, wrong file name, divide by zero, printer disconnected?", "a": 2, "unit": "", "tol": 0.01, "hint": "Disk crash and printer disconnected.", "sol": "<b>2</b>."},
  {"q": "How many different causes of exceptions does the syllabus list (programming errors, user errors, ...)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Programming, user, hardware.", "sol": "<b>3</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What happens to the rest of a program when an unhandled exception is raised?", opts: ["It carries on", "It is skipped and the program halts", "It runs twice", "It is deleted"], a: 1, why: "The program halts at that line." },
  { q: "Which is an exception rather than a syntax error?", opts: ["A missing bracket", "Dividing by a variable that is 0 at run time", "A misspelt keyword", "A missing colon"], a: 1, why: "Exceptions happen while the program runs." },
  { q: "What does int(\"abc\") raise?", opts: ["IndexError", "ZeroDivisionError", "ValueError", "OSError"], a: 2, why: "The text cannot be converted to a number." },
  { q: "A user types a file name that does not exist. This is mainly a...", opts: ["Hardware failure", "User error", "Syntax error", "Logic error"], a: 1, why: "The user gave bad input." },
  { q: "A program runs to the end but the average is wrong. This is a...", opts: ["Syntax error", "Logic error", "Exception", "Hardware failure"], a: 1, why: "The program does not stop; the result is wrong." },
  { q: "Which line of a Python error message names the exception?", opts: ["The first", "The last", "The one with the line number", "There is no such line"], a: 1, why: "The last line gives the name and reason." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Exception", "An unexpected event during execution that disrupts normal flow."],
  ["Halt", "What an unhandled exception does to the program."],
  ["Programming error", "Divide by zero, index out of range."],
  ["User error", "Wrong input or wrong file name."],
  ["Hardware failure", "Disk crash, printer or network lost."],
  ["Syntax error", "Found before the program runs."],
  ["Logic error", "Runs, but gives wrong output."],
  ["Traceback", "Python's message: line number, statement, exception name."],
] });
