/* ---------- Watch ---------- */
watch([
  { h: "1 · Editing and testing while developing", spec: { label: "Interpreter against compiler during development", nodes: [
    { id: "e", x: 20, y: 95, w: 130, h: 64, t: "Edit a line", c: "var(--accent)" },
    { id: "i", x: 260, y: 20, w: 190, h: 64, t: "Interpreter", s: "runs it straight away", c: "var(--good)" },
    { id: "c", x: 260, y: 170, w: 190, h: 64, t: "Compiler", s: "translate the whole program", c: "var(--warn)" },
    { id: "r", x: 560, y: 95, w: 170, h: 64, t: "See the result", s: "" },
  ], edges: [["e", "i"], ["e", "c"], ["i", "r"], ["c", "r"]], steps: [
    { cap: "The programmer changes a line and wants to see if it works. This happens again and again during development.", on: ["e"] },
    { cap: "<b>Interpreter:</b> the code is translated and run straight away, and it stops at the line with the error. Quick to test and debug.", on: ["e", "i", "r"], e: [0, 2], set: { r: { s: "seconds" } } },
    { cap: "<b>Compiler:</b> the whole program must be compiled again before it can run, so each test takes longer.", on: ["e", "c", "r"], e: [1, 3], set: { r: { s: "wait for the compile" } } },
    { cap: "So for <b>developing, debugging and editing</b>, the interpreter is the better choice.", on: ["i"] },
  ] } },
  { h: "2 · Releasing the finished program", spec: { label: "Compile once and distribute the executable", nodes: [
    { id: "s", x: 20, y: 80, w: 160, h: 70, t: "Finished source code" },
    { id: "c", x: 260, y: 80, w: 150, h: 70, t: "Compiler", s: "once", c: "var(--warn)" },
    { id: "x", x: 490, y: 80, w: 150, h: 70, t: "Executable", s: "ready to use", c: "var(--good)" },
    { id: "u", x: 490, y: 190, w: 150, h: 60, t: "User's computer", s: "no compiler needed" },
  ], edges: [["s", "c"], ["c", "x"], ["x", "u"]], steps: [
    { cap: "The program has been tested and is finished.", on: ["s"] },
    { cap: "It is compiled <b>once</b>.", on: ["s", "c"], e: [0] },
    { cap: "The compiled program is <b>stored ready for use</b>.", on: ["c", "x"], e: [1] },
    { cap: "Users run it <b>without the compiler</b>, in a <b>shorter time</b> and using <b>less memory</b>.", on: ["x", "u"], e: [2] },
  ] } },
]);

/* ---------- Lab 1: cost model ---------- */
(() => {
  let sz, ts, rn;
  const upd = () => {
    if (!sz || !ts || !rn) return;
    const n = sz.get(), t = ts.get(), r = rn.get();
    const dc = t * (n * 0.05 + n * 0.01), di = t * (n * 0.015), uc = r * n * 0.01, ui = r * n * 0.03;
    const f = (x) => Math.round(x).toLocaleString("en-GB");
    $("#cmDC").textContent = f(dc); $("#cmDI").textContent = f(di); $("#cmUC").textContent = f(uc); $("#cmUI").textContent = f(ui);
    const mx = Math.max(dc, di, uc, ui), H = (v) => (v / mx) * 140, B = [[dc, "var(--warn)", "Dev: comp."], [di, "var(--good)", "Dev: interp."], [uc, "var(--warn)", "Users: comp."], [ui, "var(--good)", "Users: interp."]];
    $("#cmC").innerHTML = B.map((b, i) => `<rect x="${20 + i * 80}" y="${165 - H(b[0])}" width="56" height="${H(b[0])}" rx="4" style="fill:${b[1]}"/><text x="${48 + i * 80}" y="185" text-anchor="middle" class="sm">${b[2]}</text>`).join("");
    $("#cmV").innerHTML = `During <b>development</b> the interpreter wins by ${f(dc - di)} units, because every test avoids a full compile. Once the program is <b>released</b> and run ${r} times, the compiled version wins by ${f(ui - uc)} units, because it runs faster and needs no translating each time.`;
  };
  sz = Lib.slider($("#cmS"), { id: "cms", label: "Program size (statements)", min: 50, max: 2000, step: 50, value: 500, onInput: upd });
  ts = Lib.slider($("#cmT"), { id: "cmt", label: "Edit-and-test cycles while developing", min: 1, max: 100, value: 30, onInput: upd });
  rn = Lib.slider($("#cmR"), { id: "cmr", label: "Times the finished program is run", min: 1, max: 1000, value: 100, onInput: upd });
  upd();
})();

/* ---------- Lab 2: sharing ---------- */
(() => {
  const D = [["Compiled version", "✓ Your friend can run it. The executable file contains machine code, so it can be run <b>without the compiler</b>."], ["Interpreted version (source code)", "✗ Your friend cannot run it yet. An interpreted program <b>cannot be run without the interpreter</b>, so they would need to install one first."]];
  stateBtns($("#shB"), D.map((d) => d[0]), (i) => ($("#shV").innerHTML = D[i][1])); $("#shB button").click();
})();

/* ---------- Lab 3: choose ---------- */
choose($("#cqC"), ["Compiler", "Interpreter"], [
  ["A student is writing and debugging a new program and edits it every few minutes.", 1, "Interpreter: easier and quicker to debug, test and edit during development."],
  ["A company is releasing a finished program to thousands of customers who do not have a translator.", 0, "Compiler: the executable can be run without the compiler."],
  ["A program must run in as short a time as possible once it is finished.", 0, "Compiled programs are executed in a shorter time."],
  ["A programmer wants an error to stop the program at the exact line so it can be fixed.", 1, "An interpreter stops execution at the statement with the error."],
  ["A programmer wants the translated program stored ready for use, to run again and again.", 0, "A compiled program can be stored ready for use."],
]);

/* ---------- Practise ---------- */
practise([
  { h: "1 · Advantage or disadvantage?", type: "classify", prompt: "Drag each point to the translator it belongs to.", buckets: [{ label: "Interpreter: advantage" }, { label: "Interpreter: disadvantage" }, { label: "Compiler: advantage" }, { label: "Compiler: disadvantage" }], items: [
    { text: "Quicker to debug and test during development", b: 0 }, { text: "Easier to edit during development", b: 0 },
    { text: "Cannot be run without the interpreter", b: 1 }, { text: "Programs can take longer to execute", b: 1 },
    { text: "Can be stored ready for use", b: 2 }, { text: "Runs without the compiler", b: 2 }, { text: "Executed in a shorter time", b: 2 }, { text: "Uses less memory when executed", b: 2 },
    { text: "Takes longer to write, test and debug", b: 3 },
  ], done: "Interpret to develop, compile to release." },
  { h: "2 · Development to release", type: "order", prompt: "Put the life of a program in order.", items: [
    "The programmer writes the code", "The code is tested and edited using an interpreter", "Errors are found and fixed quickly", "The finished program is compiled", "Users run the executable without a translator",
  ], done: "Interpret while developing, compile to release." },
  { h: "3 · Calculations", type: "calc", qs: [
    { q: "A program is tested 40 times. Each compile takes 30 seconds. How many minutes is spent compiling?", a: 20, sol: "40 × 30 = 1200 seconds = 20 minutes." },
    { q: "An interpreted program takes 8 seconds to run and the compiled version takes 2. If it is run 90 times, how many seconds does the compiled version save?", a: 540, sol: "(8 − 2) × 90 = 540 seconds." },
  ] },
  { h: "4 · Multiple choice", type: "quiz", qs: [
    { q: "Why is an interpreter useful during development?", opts: ["It is quicker to debug, test and edit", "It makes the program smaller", "It creates an executable", "It works without any code"], a: 0, why: "It runs code immediately and stops at the error." },
    { q: "Which is a disadvantage of an interpreter?", opts: ["The program cannot be run without the interpreter", "It cannot find errors", "It translates assembly", "It is expensive"], a: 0, why: "No executable is produced." },
    { q: "Which is an advantage of a compiler?", opts: ["The program is executed in a shorter time", "It stops at the first line", "Easier to edit", "Needs no source code"], a: 0, why: "Compiled programs are executed faster." },
    { q: "Which translator would you give to customers?", opts: ["A compiled program", "The interpreter and the source code only", "The assembler", "The error report"], a: 0, why: "It can run without a translator." },
  ] },
]);

real([
  ["Why a Python script runs where the interpreter is installed", "A Python program is run by the Python interpreter. If you send the script to a friend without Python, it cannot run.", "Interpreted programs cannot run without the interpreter."],
  ["Apps from an app store", "The apps are already translated into machine code before they reach you. They start quickly and need no extra software.", "Compiled programs are executed in a shorter time and can be run without the compiler."],
  ["Trying a quick change in the shell", "Many programmers test a tiny idea by typing it into an interpreter and seeing the result at once.", "Interpreters make development, editing and debugging quick."],
  ["Waiting for a big project to build", "Large programs can take minutes to compile, which slows the developer down when they change one line.", "A compiler takes longer to write, test and debug with during development."],
  ["Games that must feel smooth", "Fast-moving games need to run quickly, so the final game is compiled to machine code.", "Compiled programs execute in a shorter time."],
]);

exam([
  { cmd: "State", m: 2, q: "Give two advantages of using an interpreter while a program is being developed.", tip: "Debug, test, edit.", ans: [["k", "It is easier and quicker to debug and test the program."], ["k", "It is easier to edit the program during development."]], warn: "Saying the program runs faster." },
  { cmd: "State", m: 2, q: "Give two disadvantages of an interpreter.", tip: "Needs interpreter, slower.", ans: [["k", "The program cannot be run without the interpreter."], ["k", "The program can take longer to execute."]], warn: "Saying it does not find errors." },
  { cmd: "State", m: 3, q: "Give three advantages of a compiler.", tip: "Stored, no compiler, speed, memory.", ans: [["k", "A compiled program can be stored ready for use and executed without the compiler."], ["k", "It is executed in a shorter time."], ["k", "It takes up less space in memory when it is executed."]], warn: "Repeating one advantage in different words." },
  { cmd: "State", m: 1, q: "Give one disadvantage of a compiler during development.", tip: "Time.", ans: [["k", "It takes a longer time to write, test and debug programs."]], warn: "Saying the finished program is slow." },
  { cmd: "Explain", m: 4, q: "A programmer uses an interpreter while writing a program, but a compiler to produce the final version. Explain why.", tip: "Development reasons, then release reasons.", ans: [["k", "An interpreter makes it quicker and easier to debug, test and edit while writing."], ["k", "It stops at the statement with the error so it can be corrected."], ["k", "The compiler produces an executable that can be run without the compiler,"], ["k", "and it can be executed in a shorter time."]], warn: "Giving only one half of the answer." },
  { cmd: "Explain", m: 2, q: "Explain why a customer can run a compiled program but could not run an interpreted program without extra software.", tip: "Executable, interpreter.", ans: [["k", "A compiled program is already in machine code (an executable file)."], ["k", "An interpreted program needs the interpreter every time it runs."]], warn: "Saying the customer \"needs the internet\"." },
]);

tips([
  "<b>Link each translator to a stage:</b> interpreter for developing, compiler for the finished product.",
  "<b>Learn the table.</b> Two interpreter advantages, two disadvantages. Four compiler advantages, one disadvantage.",
  "<b>\"Cannot run without the interpreter\"</b> is the standard disadvantage to quote.",
  "<b>Compiled programs are stored ready for use.</b> That is why they suit distribution.",
  "<b>Do not mix up speed:</b> interpreters are quicker for <i>testing</i>, compiled programs are quicker to <i>run</i>.",
  "<b>Explain, do not list.</b> For a 4-mark \"explain\", give reason plus effect for each half.",
  "<b>Use \"during development\" and \"when released\"</b> to show you are thinking about both stages.",
  "<b>Many IDEs offer both,</b> so your answer can say the programmer uses each for a different stage.",
], [
  ["Debug", "To find and fix errors in a program."], ["Development", "The stage when a program is being written, tested and edited."],
  ["Compiler advantage", "Runs without the compiler, in a shorter time, using less memory."], ["Interpreter advantage", "Easier and quicker to debug, test and edit during development."],
  ["Interpreter disadvantage", "Cannot be run without the interpreter and may take longer to execute."], ["Compiler disadvantage", "Takes longer to write, test and debug during development."],
  ["Executable", "Machine code that can be run directly without a translator."], ["Distribution", "Giving the finished program to its users."],
]);
