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
  const L = ["Number = int(input(\"Enter a number: \"))", "Result = 100 / Number", "print(Result)", "print(\"Finished\")"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = codeList(20, 20, L, k === 0 ? -1 : k === 1 ? 0 : k >= 2 ? 1 : -1, 1, 36, 410);
    o += SV.text(450, 40, "Input: 0", "lbl bd", { style: "font-family:var(--mono);font-size:16px" });
    if (k >= 2) o += SV.rect(450, 70, 290, 80, "cell-no", { rx: 8 }) + SV.text(464, 98, "ZeroDivisionError", "lbl bd t2", { style: "font-family:var(--mono);font-size:15px" }) + SV.text(464, 124, "program halts here", "lbl");
    if (k >= 3) o += SV.text(20, 190, "print(Result) and print(\"Finished\") never run", "lbl bd t2");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 215, label: "A program with no exception handling", base: { i: 0 }, draw, tween: 300, dwell: 2800, steps: [
    { cap: "A short program that divides 100 by a number the user types. The user types <b>0</b>.", s: { i: 0 } },
    { cap: "Line 1 works: Number = 0.", s: { i: 1 } },
    { cap: "Line 2 divides 100 by 0. That is impossible, so Python raises a <b>ZeroDivisionError</b> exception. With nothing to respond to it, the program <b>halts</b>.", s: { i: 2 } },
    { cap: "The remaining lines never run, and the user sees a system error. That is the unexpected halt that exception handling prevents.", s: { i: 3 } }] });
})();

(function () {
  const L = ["try:", "    Number = int(input(\"Enter a number: \"))", "    print(100 / Number)", "except ZeroDivisionError:", "    print(\"Cannot divide by zero\")", "print(\"Finished\")"];
  const draw = (s) => {
    const k = Math.round(s.i); const hl = [-1, 1, 2, 3, 4, 5][k]; let o = codeList(20, 10, L, hl, 1, 34, 420);
    o += SV.text(470, 36, "Input: 0", "lbl bd", { style: "font-family:var(--mono);font-size:16px" });
    if (k >= 2) o += SV.rect(470, 56, 270, 64, "cell-no", { rx: 8 }) + SV.text(484, 84, "ZeroDivisionError", "lbl bd t2", { style: "font-family:var(--mono);font-size:14px" }) + SV.text(484, 106, "jump to the matching except", "sm");
    if (k >= 4) o += SV.rect(470, 130, 270, 40, "cell-ok", { rx: 8 }) + SV.text(484, 156, "Cannot divide by zero", "lbl bd t3", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 5) o += SV.rect(470, 178, 270, 36, "cell-ok", { rx: 8 }) + SV.text(484, 202, "Finished", "lbl bd t3", { style: "font-family:var(--mono);font-size:14px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 235, label: "The same program with try and except", base: { i: 0 }, draw, tween: 300, dwell: 2800, steps: [
    { cap: "The risky lines are placed in a <code>try</code> block, followed by an <code>except</code> block that says what to do.", s: { i: 0 } },
    { cap: "The try block starts: the user types 0 and <code>Number</code> is 0.", s: { i: 1 } },
    { cap: "<code>100 / Number</code> raises <b>ZeroDivisionError</b>. The rest of the try block is skipped.", s: { i: 2 } },
    { cap: "Python looks for an <code>except</code> that matches and finds <code>except ZeroDivisionError</code>.", s: { i: 3 } },
    { cap: "The handler runs and the user sees a meaningful message, not a system error.", s: { i: 4 } },
    { cap: "The program <b>carries on</b> after the try statement and prints Finished. It did not halt unexpectedly.", s: { i: 5 } }] });
})();

(function () {
  const cases = [["abc", "ValueError", "int(\"abc\") fails: the text is not a number", "Please enter a whole number"], ["0", "ZeroDivisionError", "100 / 0 is impossible", "Cannot divide by zero"], ["4", "(none)", "everything works: 100 / 4", "25.0"]];
  const draw = (s) => {
    const k = Math.round(s.i); const c = cases[Math.max(0, k - 1)]; let o = SV.text(20, 26, "try:  Number = int(input(...));  print(100 / Number)", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    o += SV.rect(20, 50, 400, 44, k === 1 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(34, 78, "except ValueError:  \"Please enter a whole number\"", "lbl", { style: "font-family:var(--mono);font-size:12px" });
    o += SV.rect(20, 104, 400, 44, k === 2 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(34, 132, "except ZeroDivisionError:  \"Cannot divide by zero\"", "lbl", { style: "font-family:var(--mono);font-size:12px" });
    if (k >= 1) o += SV.text(440, 70, "User types: " + c[0], "lbl bd", { style: "font-family:var(--mono);font-size:15px" }) + SV.text(440, 100, "Exception: " + c[1], "lbl bd " + (k === 3 ? "t3" : "t2"), { style: "font-family:var(--mono);font-size:14px" }) + SV.text(440, 128, c[2], "sm", { style: "font-size:11px" }) + SV.text(440, 160, "Output: " + c[3], "lbl bd t3", { style: "font-family:var(--mono);font-size:13px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 190, label: "Several except blocks", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "Different problems can have different responses: one <code>except</code> for each exception type.", s: { i: 0 } },
    { cap: "The user types <b>abc</b>. <code>int()</code> raises a <b>ValueError</b>, so that handler runs.", s: { i: 1 } },
    { cap: "The user types <b>0</b>. The division raises <b>ZeroDivisionError</b>, so the other handler runs.", s: { i: 2 } },
    { cap: "The user types <b>4</b>. No exception happens, so no except block runs and the answer is printed.", s: { i: 3 } }] });
})();

(function () {
  const L = ["try:", "    File = open(\"Data.txt\")", "    Line = File.readline()", "except IOError:", "    print(\"Problem with the file\")", "finally:", "    print(\"Done\")"];
  const draw = (s) => {
    const k = Math.round(s.i); const hl = [-1, 1, 3, 4, 5, 6][k]; let o = codeList(20, 10, L, hl, 1, 34, 360);
    if (k >= 2) o += SV.rect(420, 40, 310, 40, "cell-no", { rx: 8 }) + SV.text(434, 66, "IOError: file not found", "lbl bd t2", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 3) o += SV.rect(420, 92, 310, 40, "cell-ok", { rx: 8 }) + SV.text(434, 118, "Problem with the file", "lbl bd t3", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 5) o += SV.rect(420, 144, 310, 40, "cell-ok", { rx: 8 }) + SV.text(434, 170, "Done  (always runs)", "lbl bd t3", { style: "font-family:var(--mono);font-size:14px" });
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 255, label: "The finally block", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "A <code>finally</code> block runs <b>whether or not</b> an exception happened. It is used for clean-up, such as closing a file.", s: { i: 0 } },
    { cap: "The file cannot be opened.", s: { i: 1 } },
    { cap: "An IOError is raised, so the try block stops and the matching except runs.", s: { i: 2 } },
    { cap: "The except block outputs its message.", s: { i: 3 } },
    { cap: "Then the <code>finally</code> block.", s: { i: 4 } },
    { cap: "It would also have run if the file had opened without error. The mark scheme does not require <code>finally</code>, but it is a correct use.", s: { i: 5 } }] });
})();

/* Lab 1 */
(function () {
  let sit = 0, on = false;
  const sits = [["File exists, first line 5", "5"], ["File exists, first line is the word five", "five"], ["File exists, first line 0", "0"], ["File does not exist", ""]];
  const run = () => {
    const s = sits[sit], out = []; let halted = null;
    try {
      if (sit === 3) throw ["FileNotFoundError", "Could not find the file"];
      const v = s[1]; if (isNaN(parseInt(v, 10)) || !/^-?\d+$/.test(v)) throw ["ValueError", "The file does not hold a number"];
      if (+v === 0) throw ["ZeroDivisionError", "Cannot divide by zero"];
      out.push("100 / " + v + " = " + 100 / +v);
    } catch (e) { if (on) out.push(e[1]); else { halted = e[0]; } }
    return { out, halted };
  };
  const paint = () => {
    $$("#sB button").forEach((b, i) => b.classList.toggle("pri", i === sit)); $("#sT").textContent = "Exception handling: " + (on ? "on" : "off"); $("#sT").classList.toggle("pri", on);
    const r = run(), code = ['File = open("Data.txt")', "Number = int(File.readline())", "print(100 / Number)"];
    const lines = on ? ["try:", ...code.map((c) => "    " + c), "except:", '    print("An error occurred")'] : code;
    $("#sC").innerHTML = '<div class="code"><pre class="cp">' + lines.map((l) => `<span class="ln">${l.replace(/&/g, "&amp;").replace(/</g, "&lt;")}</span>`).join("") + "</pre></div>";
    $("#sV").innerHTML = r.halted ? "<b>Output:</b> the program <b>halts</b> with " + r.halted + ". Nothing after the error runs." : "<b>Output:</b> " + r.out.join("<br>") + (on && !/^100/.test(r.out[0] || "") ? "<br>The program carries on after the try statement." : "");
  };
  $("#sB").innerHTML = sits.map((s, i) => `<button class="b" data-i="${i}">${s[0]}</button>`).join("");
  $$("#sB button").forEach((b) => (b.onclick = () => { sit = +b.dataset.i; paint(); })); $("#sT").onclick = () => { on = !on; paint(); };
  paint();
})();

btnTable("eB", "eO", [
  ["User types text for a number", "ValueError", "User error", "except ValueError: print(\"Please enter a whole number\")"],
  ["Divide by a zero entered by the user", "ZeroDivisionError", "User error shown as a programming error", "except ZeroDivisionError: print(\"Cannot divide by zero\")"],
  ["Open a file that does not exist", "FileNotFoundError (an IOError)", "User error (wrong name) or system error", "except IOError: print(\"File not found\")"],
  ["Read element 10 of a list of 5", "IndexError", "Programming error", "Check the index with IF, or except IndexError"],
  ["Disk full while saving", "OSError", "Hardware / system failure", "except OSError: print(\"Cannot save\")"],
  ["Add a string to an integer", "TypeError", "Programming error", "Fix the code: convert with str() or int()"]
], ["Situation", "Exception", "Type of cause", "Handler"]);

(function () {
  const rows = [
    ["try with no except", "try:\n    File = open(\"Data.txt\")", "A SyntaxError: a try needs at least one except (or finally)", "Add except IOError: with a message"],
    ["Empty except", "except:\n    pass", "The error is hidden, nothing is shown to the user, and no mark for a message", "print(\"File not found\")"],
    ["Open outside the try", "File = open(\"Data.txt\")\ntry:\n    ...", "The most likely failure is not protected, so the program can still halt", "Put the open inside the try"],
    ["Using try for a range check", "try:\n    Age = int(Age)\nexcept:\n    print(\"Too old\")", "A value that is too large is not an exception: it needs IF", "IF Age > 120 THEN"],
    ["Closing the file only in the try", "try:\n    File = open(...)\n    ...\n    File.close()", "If an error happens, the file is not closed; use finally or close it as well", "finally: File.close()"]
  ];
  const paint = (i) => { $$("#mB button").forEach((b, k) => b.classList.toggle("pri", k === i)); const r = rows[i]; $("#mO").innerHTML = '<div class="tw"><table class="t"><tr><th>Mistake</th><th>What goes wrong</th><th>Fix</th></tr><tr><td><b>' + r[0] + "</b><pre class=\"plain\">" + r[1].replace(/&/g, "&amp;").replace(/</g, "&lt;") + "</pre></td><td>" + r[2] + "</td><td>" + r[3] + "</td></tr></table></div>"; };
  $("#mB").innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  $$("#mB button").forEach((b) => (b.onclick = () => paint(+b.dataset.i))); paint(0);
})();
Lib.classify($("#cl1"), { prompt: "What type of cause is each situation?", buckets: [{"label": "Programming error"}, {"label": "User error"}, {"label": "Hardware failure"}], items: [{"text": "Dividing by a variable that holds zero", "b": 0}, {"text": "Typing a file name that does not exist", "b": 1}, {"text": "A hard disk crashes", "b": 2}, {"text": "Reading element 12 of a 10-element array", "b": 0}, {"text": "Entering letters where a number is expected", "b": 1}, {"text": "A printer is disconnected during printing", "b": 2}, {"text": "Adding a string to an integer in code", "b": 0}, {"text": "The network cable is pulled out", "b": 2}], done: "Programming errors are mistakes the program makes; user errors are bad input; hardware failure is a device problem." });
Lib.classify($("#cl2"), { prompt: "Exception handling or an ordinary IF check?", buckets: [{"label": "Exception handling"}, {"label": "IF check"}], items: [{"text": "Opening a file that might not exist", "b": 0}, {"text": "Making sure a mark is between 0 and 100", "b": 1}, {"text": "Converting text typed by the user to an integer", "b": 0}, {"text": "Checking a menu choice is 1, 2 or 3", "b": 1}, {"text": "Reading from a network that might disconnect", "b": 0}, {"text": "Checking an index is less than the length of the list", "b": 1}, {"text": "Writing to a disk that might be full", "b": 0}, {"text": "Making sure a name is not empty", "b": 1}], done: "Use exception handling for events outside the program's control. Use IF to check values you can test." });
Lib.order($("#o1"), { prompt: "Put the steps of a try and except in order.", items: ["The statements in the try block start to run", "One of them causes an exception", "The rest of the try block is skipped", "The matching except block runs", "The program carries on after the try statement"], done: "Try, exception, skip, handle, carry on." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Exception", "An unexpected event that disrupts a running program"], ["Exception handling", "Responding to the event so the program does not halt unexpectedly"], ["try", "The block of statements that might cause the exception"], ["except", "The block that responds to the exception"], ["finally", "Runs whether or not an exception happened"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A try block has 4 statements. The 2nd causes an exception. How many statements of the try block run completely?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the 1st finishes; the 2nd fails.", "sol": "<b>1</b>."},
  {"q": "A loop reads 10 lines in a try block. The 6th line is not a number, which raises ValueError. How many lines were converted successfully?", "a": 5, "unit": "", "tol": 0.01, "hint": "Lines 1 to 5.", "sol": "<b>5</b>."},
  {"q": "A program prints Done after a try/except. How many times is Done printed if an exception occurs and is handled?", "a": 1, "unit": "", "tol": 0.01, "hint": "The program carries on after the try statement.", "sol": "<b>1</b>."},
  {"q": "The user enters 5, then 0, then abc into a program with a handler for ValueError and a handler for ZeroDivisionError. How many handler blocks run in total?", "a": 2, "unit": "", "tol": 0.01, "hint": "5 causes no exception; 0 and abc each cause one.", "sol": "<b>2</b>."},
  {"q": "A file has 30 lines. A loop reads each line inside a try, with the file closed afterwards. If the file does not exist, how many lines are read?", "a": 0, "unit": "", "tol": 0.01, "hint": "The open fails.", "sol": "<b>0</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is an exception?", opts: ["A programming language", "An unexpected event during execution that disrupts the program", "A type of loop", "An error in the design"], a: 1, why: "It happens at run time." },
  { q: "Which is the best definition of exception handling?", opts: ["Preventing all errors", "Responding to unexpected events so the program does not halt unexpectedly", "Printing a program's errors", "Ignoring errors"], a: 1, why: "The program responds and carries on." },
  { q: "Which is a hardware cause of an exception?", opts: ["Dividing by zero", "Typing a wrong file name", "A disk crash", "A missing bracket"], a: 2, why: "Disk crash or a lost device connection." },
  { q: "Where should the file opening go?", opts: ["Outside the try", "Inside the try", "In the except", "After the program"], a: 1, why: "It is the statement that might fail." },
  { q: "What does the except block do?", opts: ["Runs the risky code", "Responds to the exception, e.g. with a message", "Closes the program", "Creates a file"], a: 1, why: "It is the response." },
  { q: "Which should use an IF check rather than exception handling?", opts: ["Opening a file", "Converting user input", "Checking that a score is between 0 and 100", "Reading a network connection"], a: 2, why: "A range can be tested directly." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Exception", "An unexpected event during execution that disrupts the program."],
  ["Exception handling", "Responding to it so the program does not halt unexpectedly."],
  ["try", "Statements that might cause an exception."],
  ["except", "Statements that respond to the exception."],
  ["Causes", "Programming errors, user errors, hardware failure."],
  ["finally", "Runs whether or not an exception happened."],
  ["Always add", "An output message in the except block."],
  ["Use for", "Files, input, devices: things outside the program's control."],
] });
