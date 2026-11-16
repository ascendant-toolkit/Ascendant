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
(function () { const C = {"ps": ["TRY", "   INPUT Age", "   OUTPUT \"Next year you will be \", Age + 1", "EXCEPT", "   OUTPUT \"Please enter a whole number\"", "ENDTRY", "OUTPUT \"Finished\""], "py": ["try:", "    Age = int(input(\"Enter your age: \"))", "    print(\"Next year you will be\", Age + 1)", "except ValueError:", "    print(\"Please enter a whole number\")", "print(\"Finished\")"], "lh": 24, "vw": 150}, ST = [{"c": "The risky statements are inside a <b>try</b> block. The user is going to type <b>ten</b>.", "p": 0, "y": 0, "v": [["Age", ""]], "f": []}, {"c": "The input is read and Python tries to convert <code>ten</code> to a whole number.", "p": 1, "y": 1, "v": [["Age", ""]], "f": [], "t": [[330, 10, "ValueError raised", "lbl bd t2"]]}, {"c": "The conversion fails, so an exception is raised. The rest of the try block is <b>skipped</b>: the next-year line does not run.", "p": 2, "y": 2, "v": [["Age", ""]], "f": [], "t": [[330, 10, "ValueError raised", "lbl bd t2"], [330, 34, "line skipped", "sm"]]}, {"c": "The <b>except</b> block matches the exception and takes over.", "p": 3, "y": 3, "v": [["Age", ""]], "f": [], "t": [[330, 10, "ValueError handled", "lbl bd t2"]]}, {"c": "The user sees a meaningful message, not a system error.", "p": 4, "y": 4, "v": [["Age", ""]], "f": [], "t": [[330, 10, "Please enter a whole number", "lbl bd t3"]]}, {"c": "The program <b>carries on</b> after the try statement. It did not halt unexpectedly.", "p": 6, "y": 5, "v": [["Age", ""]], "f": [], "t": [[330, 10, "Please enter a whole number", "lbl bd t3"], [330, 34, "Finished", "lbl bd t3"]]}];
  Lib.stepper($("#stA"), { w: 760, h: 356, label: "try and except with a bad input", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3200, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "A program checks that <code>Data.txt</code> exists before it opens it.", "f": [{"x": 20, "y": 20, "t": "Folder", "r": ["Data.txt", "Notes.txt"], "w": 200, "hl": 0}], "t": [[300, 40, "IF file exists THEN ...", "lbl bd"]]}, {"c": "The check passes: the file is there.", "f": [{"x": 20, "y": 20, "t": "Folder", "r": ["Data.txt", "Notes.txt"], "w": 200, "ok": [0]}], "t": [[300, 40, "IF file exists  ->  TRUE", "lbl bd t3"]]}, {"c": "Before the program reaches <code>open</code>, the file is deleted by the user or another program.", "f": [{"x": 20, "y": 20, "t": "Folder", "r": ["Notes.txt"], "w": 200}], "t": [[300, 40, "Data.txt has been deleted", "lbl bd t2"]]}, {"c": "<code>open(\"Data.txt\")</code> fails and the program halts, even though the check passed.", "f": [{"x": 20, "y": 20, "t": "Folder", "r": ["Notes.txt"], "w": 200}], "t": [[300, 40, "FileNotFoundError: halted", "lbl bd t2"]]}, {"c": "A <b>try</b> block round the open responds whenever it happens, whatever happened before. The program reports the problem and carries on.", "f": [{"x": 20, "y": 20, "t": "Folder", "r": ["Notes.txt"], "w": 200}], "t": [[300, 40, "except: \"File not found\"", "lbl bd t3"], [300, 66, "the program carries on", "sm"]]}];
  Lib.stepper($("#stB"), { w: 760, h: 108, label: "Why an IF check can fail", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3400, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();
(function () { const C = {"ps": null, "py": null, "lh": 22, "vw": 150}, ST = [{"c": "<b>Age must be between 0 and 120</b>: use an <b>if check</b>. A range check on a value the program already has.", "f": [{"x": 20, "y": 20, "t": "Situation", "r": ["Age must be between 0 and 120"], "w": 360}, {"x": 20, "y": 70, "t": "Use", "r": ["IF check"], "w": 360, "ok": [0]}]}, {"c": "<b>Open the file the user names</b>: use an <b>exception handling</b>. The file may not exist: outside the program's control.", "f": [{"x": 20, "y": 20, "t": "Situation", "r": ["Open the file the user names"], "w": 360}, {"x": 20, "y": 70, "t": "Use", "r": ["Exception handling"], "w": 360, "ok": [0]}]}, {"c": "<b>Convert typed text to a number</b>: use an <b>exception handling</b>. The user may type anything.", "f": [{"x": 20, "y": 20, "t": "Situation", "r": ["Convert typed text to a number"], "w": 360}, {"x": 20, "y": 70, "t": "Use", "r": ["Exception handling"], "w": 360, "ok": [0]}]}, {"c": "<b>Menu choice must be 1, 2 or 3</b>: use an <b>if check</b>. A known set of values you can test directly.", "f": [{"x": 20, "y": 20, "t": "Situation", "r": ["Menu choice must be 1, 2 or 3"], "w": 360}, {"x": 20, "y": 70, "t": "Use", "r": ["IF check"], "w": 360, "ok": [0]}]}, {"c": "<b>Disk fills up while saving</b>: use an <b>exception handling</b>. Hardware: the program cannot rule it out.", "f": [{"x": 20, "y": 20, "t": "Situation", "r": ["Disk fills up while saving"], "w": 360}, {"x": 20, "y": 70, "t": "Use", "r": ["Exception handling"], "w": 360, "ok": [0]}]}];
  Lib.stepper($("#stC"), { w: 760, h: 133, label: "Choosing the right tool", base: { i: 0 }, draw: (s) => stepDraw(C, ST[Math.round(s.i)]), tween: 300, dwell: 3200, steps: ST.map((t, i) => ({ cap: t.c, s: { i } })) }); })();

btnTable("dB", "dO", [
  ["Age 0 to 120", "IF check", "The value is known and can be tested against a range."],
  ["Open a named file", "Exception handling", "The file may not exist or may fail to read."],
  ["Convert typed text", "Exception handling", "The user may type text that is not a number."],
  ["Menu choice 1 to 3", "IF check", "The valid values are known, so test them directly."],
  ["Printer disconnected", "Exception handling", "Hardware failure outside the program's control."],
  ["Total is wrong", "Neither: fix the code", "A logic error runs without stopping, so nothing is raised to catch."]
], ["Situation", "Use", "Why"]);

(function () {
  const inputs = ["25", "ten", "-5"]; let cur = 0, on = false;
  const paint = () => {
    $$("#rB button").forEach((b, i) => b.classList.toggle("pri", i === cur)); $("#rT").textContent = "Exception handling: " + (on ? "on" : "off");
    const t = inputs[cur], n = parseInt(t, 10), bad = isNaN(n); let L = ["Enter your age: " + t];
    if (!bad) { L.push("Next year you will be " + (n + 1)); L.push("Finished"); $("#rV").textContent = n < 0 ? "No exception was raised, but the output is nonsense. A negative age needs an IF check as well." : "The input is valid, so handling makes no difference."; }
    else if (on) { L.push("Please enter a whole number"); L.push("Finished"); $("#rV").textContent = "ValueError raised and handled: the program carries on."; }
    else { L.push("Traceback ... ValueError: invalid literal for int()"); L.push("(program halted: Finished never printed)"); $("#rV").textContent = "ValueError raised and not handled: the program halts."; }
    $("#rO").innerHTML = lineHTML(L);
  };
  $("#rB").innerHTML = inputs.map((x, i) => `<button class="b" data-i="${i}">Type ${x}</button>`).join("");
  $$("#rB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); })); $("#rT").onclick = () => { on = !on; paint(); }; paint();
})();
Lib.classify($("#cl1"), { prompt: "Exception handling or an ordinary IF check?", buckets: [{"label": "Exception handling"}, {"label": "IF check"}], items: [{"text": "Opening a file the user names", "b": 0}, {"text": "Making sure Age is between 0 and 120", "b": 1}, {"text": "Converting typed text with int()", "b": 0}, {"text": "Testing a menu choice is 1, 2 or 3", "b": 1}, {"text": "Reading a file that might be damaged", "b": 0}, {"text": "Checking a list index is less than the length", "b": 1}, {"text": "A printer that might be unplugged", "b": 0}, {"text": "Making sure a score is not negative", "b": 1}], done: "Exception handling: things outside the program's control. IF: values you can test directly." });
Lib.order($("#o1"), { prompt: "Put the steps in order when a bad input meets try and except.", items: ["The program enters the try block", "A statement cannot be carried out", "An exception is raised", "The rest of the try block is skipped", "The matching except block runs", "The program carries on after the try statement"], done: "Try, failure, raise, skip, except, carry on." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Trap a runtime error", "Catch the error at the moment it happens"], ["Prevent halting", "The program carries on after the problem"], ["Meaningful message", "The user is told what went wrong in plain words"], ["Validation", "An IF check that a value is sensible"], ["Exception handling", "A response to an unexpected event while the program runs"], ["try block", "Holds the statements that might raise the exception"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "try: print(\"A\"); print(1 / 0); print(\"B\")  except: print(\"C\"). How many lines are printed?", "a": 2, "unit": "", "tol": 0.01, "hint": "A is printed, then the exception, then C.", "sol": "<b>2</b> (A and C)."},
  {"q": "A try block has 5 statements. The second one raises an exception. How many statements of the try block are skipped?", "a": 3, "unit": "", "tol": 0.01, "hint": "Statements 3, 4 and 5.", "sol": "<b>3</b>."},
  {"q": "A loop asks for a number until it is valid. The user types ten, 4x, then 7. How many times does the except block run?", "a": 2, "unit": "", "tol": 0.01, "hint": "ten and 4x both fail.", "sol": "<b>2</b>."},
  {"q": "Of these four: age range, open a file, convert text to a number, menu choice 1 to 3, how many are best handled with exception handling?", "a": 2, "unit": "", "tol": 0.01, "hint": "Opening a file and converting text.", "sol": "<b>2</b>."},
  {"q": "How many reasons for using exception handling does this page give?", "a": 3, "unit": "", "tol": 0.01, "hint": "Trap, prevent halting, meaningful message.", "sol": "<b>3</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a reason for using exception handling?", opts: ["To make code run faster", "To prevent the program halting unexpectedly", "To remove logic errors", "To skip validation"], a: 1, why: "It stops an unexpected halt." },
  { q: "Which is best handled by an IF check?", opts: ["Opening a file", "A value that must be between 1 and 10", "A lost network connection", "Converting text to a number"], a: 1, why: "A range is known and can be tested." },
  { q: "What does the except block normally contain?", opts: ["The risky statements", "The response to the exception", "The input", "The loop"], a: 1, why: "It says what to do." },
  { q: "Why is checking a file exists first not always enough?", opts: ["IF is slow", "It may be deleted or fail after the check", "IF cannot test files", "Files cannot be opened"], a: 1, why: "Things change between the check and the open." },
  { q: "What happens to the statements after the failing one in a try block?", opts: ["They run", "They are skipped", "They run twice", "They run first"], a: 1, why: "Control jumps to except." },
  { q: "A negative age is typed and int() accepts it. Which tool catches this?", opts: ["try and except", "An IF range check", "Neither", "finally"], a: 1, why: "No exception is raised; it is a validation matter." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Exception handling", "Responds to an unexpected event so the program does not halt."],
  ["Reason 1", "Trap runtime errors."],
  ["Reason 2", "Stop the program halting unexpectedly."],
  ["Reason 3", "Give a meaningful message or recover."],
  ["Use it for", "Files, typed conversions, hardware and network problems."],
  ["Use IF for", "Ranges, menus and known values."],
  ["Validation", "An IF check that data is sensible."],
  ["Not a bug fix", "A logic error is fixed in the code."],
] });
