/* ---------- Watch ---------- */
watch([
  { h: "1 · The compiler", spec: { label: "A compiler translates the whole program", nodes: [
    { id: "s", x: 20, y: 80, w: 170, h: 80, t: "Source code", s: "high-level program" },
    { id: "c", x: 260, y: 80, w: 150, h: 80, t: "Compiler", s: "whole program", c: "var(--warn)" },
    { id: "o", x: 500, y: 20, w: 230, h: 70, t: "Object code", s: "executable file", c: "var(--good)", from: 2 },
    { id: "e", x: 500, y: 150, w: 230, h: 70, t: "Error report", s: "no program produced", c: "var(--bad)", from: 3 },
  ], edges: [["s", "c"], ["c", "o"], ["c", "e"]], steps: [
    { cap: "The programmer writes the program in a high-level language: the <b>source code</b>.", on: ["s"] },
    { cap: "The compiler reads the <b>whole program</b> and translates it in one go.", on: ["s", "c"], e: [0] },
    { cap: "No errors found: it produces <b>object code</b>, an executable file of machine code. It can be run again and again <b>without the compiler</b>.", on: ["c", "o"], e: [1] },
    { cap: "Errors found: it produces an <b>error report</b> instead of a compiled program. Nothing can be run until the errors are fixed.", on: ["c", "e"], e: [2] },
  ] } },
  { h: "2 · The interpreter", spec: { label: "An interpreter translates and runs one line at a time", nodes: [
    { id: "l1", x: 20, y: 10, w: 200, h: 44, t: "Line 1", mono: 1, s: "" }, { id: "l2", x: 20, y: 70, w: 200, h: 44, t: "Line 2" },
    { id: "l3", x: 20, y: 130, w: 200, h: 44, t: "Line 3 (has an error)", c: "var(--bad)" }, { id: "l4", x: 20, y: 190, w: 200, h: 44, t: "Line 4" },
    { id: "i", x: 310, y: 80, w: 170, h: 80, t: "Interpreter", s: "one statement at a time", c: "var(--warn)" },
    { id: "r", x: 560, y: 80, w: 170, h: 80, t: "Computer", s: "executes", c: "var(--good)" },
  ], edges: [["l1", "i"], ["l2", "i"], ["l3", "i"], ["i", "r"]], steps: [
    { cap: "The interpreter takes the program <b>one statement at a time</b>.", on: ["i"] },
    { cap: "Line 1 is translated and <b>executed</b> straight away.", on: ["l1", "i", "r"], e: [0, 3], set: { r: { s: "done: line 1" } } },
    { cap: "Then line 2 is translated and executed.", on: ["l2", "i", "r"], e: [1, 3], set: { r: { s: "done: lines 1-2" } } },
    { cap: "Line 3 has an error. <b>Execution stops</b> and an error message appears. Line 4 never runs.", on: ["l3", "i"], e: [2], set: { r: { s: "stopped at line 3", t: "Computer" } } },
    { cap: "No executable file is made. Next time the program runs, the <b>interpreter is needed again</b>.", on: ["i"] },
  ] } },
]);

/* ---------- Lab 1: compile vs interpret ---------- */
(() => {
  const L = (fix) => ['OUTPUT "Hello"', "total ← 5 * 2", fix ? 'OUTPUT "Total is " + total' : 'OUTPUT "Total is " total', 'OUTPUT "Goodbye"'];
  const draw = (cur) => { const fix = $("#trFix").checked; $("#trC").innerHTML = L(fix).map((t, i) => `<span class="ln ${i === 2 && !fix ? "err" : ""} ${cur === i ? "on" : ""}"><span class="cm">${i + 1}  </span>${t}</span>`).join(""); };
  const out = (h) => ($("#trO").innerHTML = h.map((x) => `<div>${x}</div>`).join(""));
  $("#trFix").onchange = () => { draw(); out(["Choose a translator."]); };
  $("#trCo").onclick = () => { const fix = $("#trFix").checked; draw();
    if (!fix) out(['<span class="hi">Compiler: reads the whole program first.</span>', '<span class="bd">Error report: line 3, missing "+"</span>', "No executable file is produced, so <b>nothing runs</b>, not even lines 1 and 2."]);
    else out(['<span class="hi">Compiler: translates the whole program.</span>', '<span class="gd">Executable file produced.</span>', "Running it...", "Hello", "Total is 10", "Goodbye", "It can be run again <b>without the compiler</b>."]); };
  $("#trIn").onclick = async () => { const fix = $("#trFix").checked, lines = []; 
    const lg = [['Hello'], [], fix ? ["Total is 10"] : null, ["Goodbye"]];
    for (let i = 0; i < 4; i++) { draw(i); if (lg[i] === null) { lines.push(`<span class="bd">Error on line 3: missing "+". Execution stops.</span>`); lines.push("Line 4 never runs. No executable file exists."); break; } lines.push(`Line ${i + 1} translated and run.` + (lg[i].length ? " Output: " + lg[i][0] : "")); }
    if (fix) lines.push("Finished. Interpreting is needed again next time."); out(["<span class=\"hi\">Interpreter: one statement at a time.</span>"].concat(lines)); };
  draw();
})();

/* ---------- Lab 2: repeated runs ---------- */
(() => {
  Lib.slider($("#rnS"), { id: "rn", label: "Number of times the program is run", min: 1, max: 20, value: 5, onInput: (n) => {
    $("#rnC").textContent = 1; $("#rnI").textContent = n;
    $("#rnV").innerHTML = `A compiled program is translated <b>once</b>. The executable can then be run ${n} time${n > 1 ? "s" : ""}, even on a computer without the compiler. An interpreted program is translated <b>every time it runs</b>, so it needs the interpreter ${n} time${n > 1 ? "s" : ""}, and may run more slowly.`;
  } });
})();

/* ---------- Lab 3: which translator ---------- */
(() => {
  const O = ["Compiler", "Interpreter", "Assembler"];
  const Q = [
    ["A program is written in assembly language.", 2, "An assembler translates assembly language into machine code."],
    ["A programmer is testing code and wants an error reported at the exact statement where it happens.", 1, "An interpreter stops at the statement with the error and reports it."],
    ["A company wants to hand customers an executable file that does not need any translator.", 0, "A compiler produces an executable file of machine code."],
    ["The translator usually converts one statement into exactly one machine code instruction.", 2, "Assembly statements usually translate one-to-one."],
    ["A high-level program must be translated again every time it is run.", 1, "No executable file is produced, so it has to be interpreted again."],
  ];
  const el = $("#whC"); let i = 0, score = 0;
  const draw = () => { if (i >= Q.length) { el.innerHTML = `<p><b>Done. Score ${score} / ${Q.length}.</b></p><button class="b" id="whr">Try again</button>`; $("#whr").onclick = () => { i = score = 0; draw(); }; return; }
    el.innerHTML = `<p><b>${i + 1}.</b> ${Q[i][0]}</p><div class="ch">${O.map((o, k) => `<button data-a="${k}">${o}</button>`).join("")}</div><div class="verdict" id="whv" hidden></div>`;
    $$(".ch button", el).forEach((b) => (b.onclick = () => { const ok = +b.dataset.a === Q[i][1]; $$(".ch button", el).forEach((x) => (x.disabled = true)); b.classList.add(ok ? "ok" : "no"); if (ok) score++; const v = $("#whv"); v.hidden = false; v.innerHTML = (ok ? "✓ " : "✗ ") + Q[i][2] + `<br><button class="b" id="whn" style="margin-top:8px">Next</button>`; $("#whn").onclick = () => { i++; draw(); }; })); };
  draw();
})();

/* ---------- Practise ---------- */
practise([
  { h: "1 · Compiler, interpreter or assembler?", type: "classify", prompt: "Drag each statement to the translator it describes.", buckets: [{ label: "Compiler" }, { label: "Interpreter" }, { label: "Assembler" }], items: [
    { text: "Translates the whole high-level program in one go", b: 0 }, { text: "Produces an executable file; no translator needed to run it", b: 0 }, { text: "Gives an error report instead of a program", b: 0 },
    { text: "Translates and runs one statement at a time", b: 1 }, { text: "Stops at the first error", b: 1 }, { text: "No executable file is produced", b: 1 },
    { text: "Translates assembly language", b: 2 }, { text: "One statement usually becomes one instruction", b: 2 },
  ], done: "Whole program, one statement, or assembly." },
  { h: "2 · Match the term", type: "match", prompt: "Match each term to its meaning.", pairs: [
    ["Source code", "The program as written by the programmer"], ["Object code", "The machine code produced after compiling"], ["Translator", "A program that converts a program into machine code"],
    ["Executable file", "A file of machine code that can be run on its own"], ["Error report", "What a compiler produces when it finds errors"],
  ] },
  { h: "3 · Compiling a program", type: "order", prompt: "Put these steps for a compiled program in order.", items: [
    "The programmer writes the source code", "The compiler reads the whole program", "An executable file of machine code is produced", "The program is run, again and again, without the compiler",
  ], done: "Write, compile, produce executable, run." },
  { h: "4 · Multiple choice", type: "quiz", qs: [
    { q: "What does a compiler produce if it finds errors?", opts: ["An error report", "An executable file", "Source code", "A blank screen"], a: 0, why: "It produces an error report instead of a compiled program." },
    { q: "What happens when an interpreter finds an error?", opts: ["Execution stops and an error message is shown", "The error is ignored", "The program is compiled instead", "The computer shuts down"], a: 0, why: "It stops at that statement." },
    { q: "Which translator needs to be present every time the program runs?", opts: ["Interpreter", "Compiler", "Assembler", "None of them"], a: 0, why: "No executable is produced, so the interpreter must be available." },
    { q: "What is object code?", opts: ["The machine code produced by a compiler", "The program written by a person", "A kind of error", "The name of a language"], a: 0, why: "Source code goes in, object code comes out." },
  ] },
]);

real([
  ["Apps you download", "The program you install on a phone or laptop is usually already compiled into machine code. It runs without the developer's compiler.", "A compiled program is distributed for general use and run without the compiler."],
  ["Testing in a school IDE", "When you press Run in a program such as Python's editor, the interpreter reads your code line by line and stops with a message at the first mistake.", "Interpreters are often used while a program is being developed."],
  ["A script that needs an interpreter", "Web page scripts are run by the interpreter in your browser. If the interpreter is missing, the script does not work.", "Interpreted programs cannot run without the interpreter."],
  ["A big game studio", "Studios compile the final game so players get fast, ready-to-run files. While writing, they test in smaller steps.", "Compile for release, interpret (or quickly test) during development."],
  ["Error messages that give a line number", "Both a compiler and an interpreter report errors, often with a line number. A compiler reports them before anything runs.", "Difference in when the errors are reported."],
]);

exam([
  { cmd: "State", m: 2, q: "Name the three types of translator.", tip: "Three words.", ans: [["k", "Compiler, interpreter"], ["k", "Assembler"]], warn: "Naming programming languages." },
  { cmd: "Describe", m: 3, q: "Describe how a compiler translates a high-level program.", tip: "Whole program, machine code, executable.", ans: [["k", "It translates the whole program in one go."], ["k", "Into machine code (object code) in an executable file."], ["k", "If there are errors, it produces an error report instead."]], warn: "Saying it runs the program line by line." },
  { cmd: "Describe", m: 3, q: "Describe how an interpreter translates a high-level program.", tip: "One at a time, executes, stops.", ans: [["k", "It reads one statement at a time, translates it and executes it."], ["k", "Then moves on to the next statement."], ["k", "If there is an error, execution stops and an error message is output."]], warn: "Saying it creates an executable file." },
  { cmd: "State", m: 2, q: "State two differences between a compiler and an interpreter.", tip: "Whole vs one at a time; executable.", ans: [["k", "A compiler translates the whole program at once, but an interpreter translates and runs one statement at a time."], ["k", "A compiler produces an executable file, but an interpreter does not."]], warn: "Naming two things about only one translator." },
  { cmd: "State", m: 2, q: "State the job of an assembler.", tip: "Assembly to machine code.", ans: [["k", "It translates a program written in assembly language"], ["k", "into machine code."]], warn: "Saying it translates a high-level language." },
  { cmd: "Explain", m: 2, q: "Explain why a compiled program can be run on a computer that does not have the compiler.", tip: "Executable file.", ans: [["k", "The compiler has already produced an executable file of machine code,"], ["k", "so no translation is needed when it runs."]], warn: "Saying the computer \"has no need for code\"." },
  { cmd: "Explain", m: 2, q: "A program is run 50 times. Explain how many times it would be translated if (a) compiled and (b) interpreted.", tip: "Once, or every run.", ans: [["k", "(a) Once, because the executable file is reused."], ["k", "(b) 50 times, because it is interpreted again each time it is run."]], warn: "Saying both are translated once." },
]);

tips([
  "<b>Compiler = whole program, interpreter = one statement at a time.</b> Start every comparison there.",
  "<b>Compiled output:</b> an executable file of object code. <b>Interpreter:</b> no executable file.",
  "<b>Errors:</b> a compiler gives an error report and nothing runs. An interpreter stops at the error.",
  "<b>Assembler is for assembly language,</b> not for high-level code.",
  "<b>Source code goes in. Object code comes out.</b> Use both terms.",
  "<b>Compiled programs run without the compiler.</b> Interpreted ones need the interpreter every time.",
  "<b>One-to-one:</b> assembler statements usually map to one instruction each. High-level statements map to several.",
  "<b>Use \"in one go\" and \"one at a time\"</b> so the examiner sees you know the difference.",
], [
  ["Translator", "A program that converts a program into machine code."], ["Compiler", "A translator that translates a whole high-level program into machine code in one go."],
  ["Interpreter", "A translator that translates and executes a high-level program one statement at a time."], ["Assembler", "A translator that converts assembly language into machine code."],
  ["Source code", "The original program, before translation."], ["Object code", "The machine code produced after compiling."],
  ["Executable file", "A file of machine code that can be run without a translator."], ["Error report", "The list of errors a compiler produces instead of a compiled program."],
]);
