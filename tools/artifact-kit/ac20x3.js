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
(function () { const C = {"ps": ["TRY", "   INPUT Number", "   Result <- 100 / Number", "   OUTPUT Result", "EXCEPT", "   OUTPUT \"Cannot divide by zero\"", "FINALLY", "   OUTPUT \"Done\"", "ENDTRY"], "py": ["try:", "    Number = int(input(\"Enter a number: \"))", "    Result = 100 / Number", "    print(Result)", "except ZeroDivisionError:", "    print(\"Cannot divide by zero\")", "finally:", "    print(\"Done\")"], "lh": 22, "vw": 150}, ST = [{"c": "The try block starts. The user types <b>0</b>.", "p": 0, "y": 0, "v": [["Number", ""], ["Result", ""]], "f": []}, {"c": "The input is read: <code>Number</code> is 0.", "p": 1, "y": 1, "v": [["Number", "0"], ["Result", ""]], "f": []}, {"c": "<code>100 / Number</code> raises <b>ZeroDivisionError</b>. The rest of the try block is skipped: <code>Result</code> is never set and the print is not run.", "p": 2, "y": 2, "v": [["Number", "0"], ["Result", ""]], "f": [], "t": [[330, 10, "ZeroDivisionError", "lbl bd t2"]]}, {"c": "Python looks for an except that matches and finds <code>except ZeroDivisionError</code>.", "p": 4, "y": 4, "v": [["Number", "0"], ["Result", ""]], "f": [], "t": [[330, 10, "ZeroDivisionError", "lbl bd t2"]]}, {"c": "The response runs.", "p": 5, "y": 5, "v": [["Number", "0"], ["Result", ""]], "f": [], "t": [[330, 10, "Cannot divide by zero", "lbl bd t3"]]}, {"c": "<b>finally</b> runs next, as it always does.", "p": 6, "y": 6, "v": [["Number", "0"], ["Result", ""]], "f": [], "t": [[330, 10, "Cannot divide by zero", "lbl bd t3"]]}, {"c": "<code>Done</code> is output. The program then carries on after the structure.", "p": 7, "y": 7, "v": [["Number", "0"], ["Result", ""]], "f": [], "t": [[330, 10, "Cannot divide by zero", "lbl bd t3"], [330, 34, "Done", "lbl bd t3"]]}];
  Lib.stepper($("#stA"), { w: 760, h: 386, label: "try, except and finally with input 0", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3000, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": ["TRY", "   INPUT Number", "   Result <- 100 / Number", "   OUTPUT Result", "EXCEPT", "   OUTPUT \"Cannot divide by zero\"", "FINALLY", "   OUTPUT \"Done\"", "ENDTRY"], "py": ["try:", "    Number = int(input(\"Enter a number: \"))", "    Result = 100 / Number", "    print(Result)", "except ZeroDivisionError:", "    print(\"Cannot divide by zero\")", "finally:", "    print(\"Done\")"], "lh": 22, "vw": 150}, ST = [{"c": "The try block starts. This time the user types <b>4</b>.", "p": 0, "y": 0, "v": [["Number", ""], ["Result", ""]], "f": []}, {"c": "<code>Number</code> is 4.", "p": 1, "y": 1, "v": [["Number", "4"], ["Result", ""]], "f": []}, {"c": "<code>100 / 4</code> works: <code>Result</code> is 25.0.", "p": 2, "y": 2, "v": [["Number", "4"], ["Result", "25.0"]], "f": []}, {"c": "The result is output.", "p": 3, "y": 3, "v": [["Number", "4"], ["Result", "25.0"]], "f": [], "t": [[330, 10, "25.0", "lbl bd t3"]]}, {"c": "No exception was raised, so the <b>except block is skipped</b>.", "p": 4, "y": 4, "v": [["Number", "4"], ["Result", "25.0"]], "f": [], "t": [[330, 10, "25.0", "lbl bd t3"], [330, 34, "except skipped", "sm"]]}, {"c": "<b>finally</b> still runs.", "p": 6, "y": 6, "v": [["Number", "4"], ["Result", "25.0"]], "f": [], "t": [[330, 10, "25.0", "lbl bd t3"], [330, 34, "except skipped", "sm"]]}, {"c": "<code>Done</code> is output. <code>finally</code> runs with or without an exception.", "p": 7, "y": 7, "v": [["Number", "4"], ["Result", "25.0"]], "f": [], "t": [[330, 10, "25.0", "lbl bd t3"], [330, 34, "Done", "lbl bd t3"]]}];
  Lib.stepper($("#stB"), { w: 760, h: 386, label: "try, except and finally with input 4", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3000, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": ["TRY", "   INPUT Number", "   Result <- 100 / Number", "EXCEPT", "   OUTPUT \"Problem with the number\"", "ENDTRY", "// one EXCEPT covers every exception", "// named exceptions and else are Python"], "py": ["try:", "    Number = int(input(\"Enter a number: \"))", "    Result = 100 / Number", "except ValueError:", "    print(\"Not a whole number\")", "except ZeroDivisionError:", "    print(\"Cannot divide by zero\")", "else:", "    print(\"Result is\", Result)"], "lh": 22, "vw": 150}, ST = [{"c": "Two different exceptions can be raised in the try block, so there are two except blocks, and an else block for when nothing goes wrong.", "p": -1, "y": -1, "v": [["Number", ""], ["Result", ""]], "f": []}, {"c": "The user types <b>abc</b>. <code>int(\"abc\")</code> raises <b>ValueError</b>. The rest of the try block is skipped.", "p": 1, "y": 1, "v": [["Number", "abc"], ["Result", ""]], "f": [], "t": [[330, 10, "ValueError", "lbl bd t2"]]}, {"c": "<code>except ValueError</code> matches, so it runs. The other except and the else are skipped.", "p": 4, "y": 4, "v": [["Number", "abc"], ["Result", ""]], "f": [], "t": [[330, 10, "Not a whole number", "lbl bd t3"]]}, {"c": "Now the user types <b>0</b>. <code>int(\"0\")</code> works, then <code>100 / 0</code> raises <b>ZeroDivisionError</b>.", "p": 2, "y": 2, "v": [["Number", "0"], ["Result", ""]], "f": [], "t": [[330, 10, "ZeroDivisionError", "lbl bd t2"]]}, {"c": "Python checks the blocks in order. <code>except ValueError</code> does not match; <code>except ZeroDivisionError</code> does.", "p": 3, "y": 5, "v": [["Number", "0"], ["Result", ""]], "f": [], "t": [[330, 10, "ZeroDivisionError", "lbl bd t2"]]}, {"c": "The matching response runs.", "p": 4, "y": 6, "v": [["Number", "0"], ["Result", ""]], "f": [], "t": [[330, 10, "Cannot divide by zero", "lbl bd t3"]]}, {"c": "Finally the user types <b>4</b>. Both statements work: <code>Result</code> is 25.0.", "p": 2, "y": 2, "v": [["Number", "4"], ["Result", "25.0"]], "f": [], "t": [[330, 10, "no exception", "sm"]]}, {"c": "No exception, so no except block runs. The <b>else</b> block runs instead.", "p": -1, "y": 8, "v": [["Number", "4"], ["Result", "25.0"]], "f": [], "t": [[330, 10, "Result is 25.0", "lbl bd t3"]]}];
  Lib.stepper($("#stC"), { w: 760, h: 386, label: "Which except block runs?", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3200, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();

(function () {
  const ins = ["4", "0", "abc"];
  const code = ["try:", "    Number = int(input(...))", "    Result = 100 / Number", "except ValueError:", "    print(\"Not a whole number\")", "except ZeroDivisionError:", "    print(\"Cannot divide by zero\")", "else:", "    print(\"Result is\", Result)", "finally:", "    print(\"Done\")"];
  const run = (t) => {
    const n = parseInt(t, 10), rows = [["try", "runs"]], out = [];
    if (isNaN(n)) { rows[0][1] = "stops at int(): ValueError raised"; rows.push(["except ValueError", "RUNS"], ["except ZeroDivisionError", "skipped"], ["else", "skipped"]); out.push("Not a whole number"); }
    else if (n === 0) { rows[0][1] = "stops at 100 / Number: ZeroDivisionError raised"; rows.push(["except ValueError", "skipped (no match)"], ["except ZeroDivisionError", "RUNS"], ["else", "skipped"]); out.push("Cannot divide by zero"); }
    else { rows[0][1] = "finishes normally"; rows.push(["except ValueError", "skipped"], ["except ZeroDivisionError", "skipped"], ["else", "RUNS"]); out.push("Result is " + (Number.isInteger(100 / n) ? (100 / n).toFixed(1) : 100 / n)); }
    rows.push(["finally", "RUNS (always)"]); out.push("Done"); return { rows, out };
  };
  const paint = (i) => {
    $$("#wB button").forEach((b, k) => b.classList.toggle("pri", k === i)); const r = run(ins[i]);
    $("#wO").innerHTML = '<div class="grid2"><div>' + lineHTML(code) + '</div><div><div class="tw"><table class="t"><tr><th>Block</th><th>What happens</th></tr>' + r.rows.map((x) => `<tr><td><code>${x[0]}</code></td><td>${x[1]}</td></tr>`).join("") + "</table></div></div></div>";
    $("#wV").textContent = "Output: " + r.out.join(", then ");
  };
  $("#wB").innerHTML = ins.map((x) => `<button class="b">Type ${x}</button>`).join("");
  $$("#wB button").forEach((b, i) => (b.onclick = () => paint(i))); paint(1);
})();
btnTable("mB", "mO", [
  ["try with no except", "try:\n    X = int(input())", "A try must be followed by except or finally: this is a syntax error", "Add except ValueError: with a response"],
  ["Empty except", "except ValueError:\n    pass", "The user is told nothing, and the exam mark needs a message or action", "print(\"Please enter a whole number\")"],
  ["Risky line outside try", "X = int(input())\ntry:\n    print(100 / X)", "The int() can still fail and halt the program", "Put int(input()) inside the try"],
  ["Wrong exception", "try: X = int(\"abc\")\nexcept IOError: ...", "IOError does not match a ValueError, so the program halts", "except ValueError: (or a bare except:)"],
  ["else instead of finally", "else:\n    File.close()", "else only runs when nothing went wrong, so the file stays open after an exception", "Use finally: for tidying up"],
  ["Missing colon or indent", "except ValueError\nprint(\"Oops\")", "Each except needs a colon and an indented block", "except ValueError:\n    print(\"Oops\")"]
], ["Mistake", "Code", "What goes wrong", "Fix"]);
Lib.classify($("#cl1"), { prompt: "Which block does each statement describe?", buckets: [{"label": "try"}, {"label": "except"}, {"label": "else"}, {"label": "finally"}], items: [{"text": "Holds the statements that might raise the exception", "b": 0}, {"text": "Runs only if an exception was raised and it matches", "b": 1}, {"text": "Runs only if there was no exception", "b": 2}, {"text": "Runs whether or not an exception happened", "b": 3}, {"text": "The place to tidy up, such as closing a file", "b": 3}, {"text": "Contains the message shown to the user", "b": 1}, {"text": "Skipped if the try block raises an exception", "b": 2}, {"text": "Is left part-way when an exception is raised", "b": 0}], done: "try: risky. except: response. else: no exception. finally: always." });
Lib.order($("#o1"), { prompt: "Put the steps in order for a try block that raises an exception which is caught, with a finally block.", items: ["The try block starts", "A statement in the try block raises an exception", "The rest of the try block is skipped", "The matching except block runs", "The finally block runs", "The program carries on after the structure"], done: "Try, raise, skip, except, finally, carry on." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["try", "The block of statements that might cause an exception"], ["except", "The block that responds to the exception"], ["else", "Runs only if no exception was raised"], ["finally", "Runs whether or not an exception was raised"], ["ValueError", "Raised when int(\"abc\") cannot convert the text"], ["ZeroDivisionError", "Raised when a number is divided by zero"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "The program on this page is run with input 4 (result 25.0, with finally). How many lines are printed?", "a": 2, "unit": "", "tol": 0.01, "hint": "The result and Done.", "sol": "<b>2</b>."},
  {"q": "Same program, input 0. How many lines are printed?", "a": 2, "unit": "", "tol": 0.01, "hint": "The message and Done.", "sol": "<b>2</b>."},
  {"q": "Program: try: print(\"A\"); print(int(\"x\")); print(\"B\") except ValueError: print(\"C\") finally: print(\"D\"). How many lines are printed?", "a": 3, "unit": "", "tol": 0.01, "hint": "A, C and D. B is skipped.", "sol": "<b>3</b> (A, C, D)."},
  {"q": "The try block raises a ValueError but the only except is for ZeroDivisionError. A finally block prints one line. How many lines does the program print before the error message?", "a": 1, "unit": "", "tol": 0.01, "hint": "finally still runs, then the program halts.", "sol": "<b>1</b> (the finally line)."},
  {"q": "A try has three except blocks, and an exception matches the second. How many except blocks run?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the first match runs.", "sol": "<b>1</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What happens to the rest of a try block after an exception is raised?", opts: ["It runs", "It is skipped", "It runs twice", "It moves to finally"], a: 1, why: "Control jumps to the matching except." },
  { q: "Which block runs only if no exception happens?", opts: ["except", "finally", "else", "try"], a: 2, why: "else is the no-exception block." },
  { q: "Which block always runs?", opts: ["except", "finally", "else", "none of them"], a: 1, why: "finally runs whether or not there was an exception." },
  { q: "What does a bare except: catch?", opts: ["Only ValueError", "Only file errors", "Any exception", "No exceptions"], a: 2, why: "A bare except catches everything." },
  { q: "try with no except or finally is...", opts: ["Fine", "A syntax error", "A logic error", "Only a warning"], a: 1, why: "A try needs a handler." },
  { q: "In exam pseudocode, which keyword ends the structure?", opts: ["END", "ENDTRY", "ENDEXCEPT", "STOP"], a: 1, why: "TRY ... EXCEPT ... FINALLY ... ENDTRY." },
] });
Lib.cards($("#fc1"), { cards: [
  ["try", "The statements that might raise an exception."],
  ["except", "The response. Naming the exception is best."],
  ["else", "Runs only when there was no exception. Python only."],
  ["finally", "Always runs. For tidying up."],
  ["Bare except", "Catches every exception. Accepted in the exam."],
  ["except ... as E", "E holds the reason Python gave."],
  ["Order", "First matching except runs; the rest are skipped."],
  ["ENDTRY", "Ends the exam pseudocode structure."],
] });
