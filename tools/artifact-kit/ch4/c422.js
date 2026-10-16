/* ---------- Watch ---------- */
watch([
  { h: "1 · Running LDA, ADD, STO", spec: { label: "The accumulator holds the value being worked on", nodes: [
    { id: "f", x: 20, y: 20, w: 150, h: 64, t: "First", s: "7", c: "var(--accent)" },
    { id: "s", x: 20, y: 105, w: 150, h: 64, t: "Second", s: "5" },
    { id: "m", x: 20, y: 190, w: 150, h: 64, t: "Sum", s: "?" , c: "var(--good)" },
    { id: "a", x: 330, y: 85, w: 170, h: 90, t: "Accumulator", s: "empty", c: "var(--warn)" },
    { id: "i", x: 570, y: 85, w: 170, h: 90, t: "Instruction", s: "-", mono: 1 },
  ], edges: [["f", "a"], ["s", "a"], ["a", "m", "dash"]], steps: [
    { cap: "Memory holds <b>First = 7</b> and <b>Second = 5</b>. The accumulator is empty and Sum is not yet known.", on: ["f", "s"] },
    { cap: "<b>LDA First</b>: the value of First (7) is loaded into the accumulator.", on: ["f", "a", "i"], e: [0], set: { a: { s: "7" }, i: { s: "LDA First" } } },
    { cap: "<b>ADD Second</b>: the value of Second (5) is added to what is in the accumulator. 7 + 5 = 12.", on: ["s", "a", "i"], e: [1], set: { a: { s: "12" }, i: { s: "ADD Second" } } },
    { cap: "<b>STO Sum</b>: the accumulator's value is stored in the variable Sum.", on: ["a", "m", "i"], e: [2], set: { a: { s: "12" }, m: { s: "12" }, i: { s: "STO Sum" } } },
  ] } },
  { h: "2 · The assembler", spec: { label: "Assembly is translated into machine code", nodes: [
    { id: "a", x: 20, y: 70, w: 200, h: 90, t: "Assembly program", s: ["LDA First", "ADD Second", "STO Sum"], mono: 1 },
    { id: "t", x: 290, y: 85, w: 150, h: 60, t: "Assembler", c: "var(--warn)", from: 1 },
    { id: "m", x: 520, y: 70, w: 210, h: 90, t: "Machine code", s: ["0001 00010010", "0100 00010011", "0000 00011010"], mono: 1, c: "var(--good)", from: 2 },
  ], edges: [["a", "t"], ["t", "m"]], steps: [
    { cap: "The programmer writes the program using <b>mnemonics</b>.", on: ["a"] },
    { cap: "An <b>assembler</b> translates it. Usually one assembly instruction becomes one machine code instruction.", on: ["a", "t"], e: [0] },
    { cap: "The machine code is produced. It can now be run again and again <b>without re-assembling</b>.", on: ["t", "m"], e: [1] },
  ] } },
]);

/* ---------- Lab 1: stepper ---------- */
(() => {
  const P = [["LDA", "First"], ["ADD", "Second"], ["STO", "Sum"]]; let pc, acc, sum;
  const paint = () => { $("#mAcc").textContent = acc === null ? "-" : acc; $("#mSum").textContent = sum === null ? "?" : sum; $("#mProg").innerHTML = P.map((p, i) => `<span class="ln ${i === pc - 1 ? "on" : i < pc ? "done" : ""}">${p[0]} ${p[1]}</span>`).join(""); };
  const reset = () => { pc = 0; acc = null; sum = null; paint(); $("#mV").textContent = "Press Step to run LDA First."; };
  const step = () => {
    if (pc >= P.length) { $("#mV").textContent = "The program has finished."; return; }
    const F = +$("#mF").value, S = +$("#mS").value, [op] = P[pc]; pc++;
    if (op === "LDA") { acc = F; $("#mV").textContent = `LDA First: the accumulator now holds ${F}.`; }
    else if (op === "ADD") { acc += S; $("#mV").textContent = `ADD Second: ${acc - S} + ${S} = ${acc}, held in the accumulator.`; }
    else { sum = acc; $("#mV").innerHTML = `STO Sum: Sum = ${sum}. <b>Finished.</b>`; }
    paint();
  };
  $("#mStep").onclick = step; $("#mRun").onclick = () => { reset(); for (let i = 0; i < 3; i++) step(); }; $("#mRes").onclick = reset;
  ["#mF", "#mS"].forEach((i) => ($(i).oninput = reset)); reset();
})();

/* ---------- Lab 2: write and assemble ---------- */
(() => {
  const OP = { LDA: "0001", ADD: "0100", STO: "0000" }, AD = { First: "00010010", Second: "00010011", Sum: "00011010" }, el = $("#wrL");
  const mkSel = (opts, v) => `<select class="sel">${opts.map((o) => `<option${o === v ? " selected" : ""}>${o}</option>`).join("")}</select>`;
  el.innerHTML = [1, 2, 3, 4].map((n, i) => `<div class="row" style="margin-bottom:6px"><b style="width:1.5em">${n}</b>${mkSel(["(blank)", "LDA", "ADD", "STO"], "(blank)")}${mkSel(["First", "Second", "Sum"], "First")}</div>`).join("");
  const rows = $$(".row", el);
  $("#wrGo").onclick = () => {
    const prog = rows.map((r) => $$("select", r).map((s) => s.value)).filter((p) => p[0] !== "(blank)");
    $("#wrM").innerHTML = prog.length ? prog.map((p) => `<span class="ln">${OP[p[0]]} ${AD[p[1]]}   <span class="cm">${p[0]} ${p[1]}</span></span>`).join("") : "";
    let acc = null, mem = { First: 7, Second: 5, Sum: null }, err = "";
    prog.forEach((p) => { if (p[0] === "LDA") acc = mem[p[1]]; else if (p[0] === "ADD") { if (acc === null || mem[p[1]] === null) err = "ADD used before there is a value in the accumulator."; else acc += mem[p[1]]; } else { mem[p[1]] = acc; } });
    const ok = !err && mem.Sum === 12;
    $("#wrV").innerHTML = (ok ? "✓ " : "✗ ") + (err || (ok ? "First (7) + Second (5) = 12 is stored in Sum. Correct." : `Sum holds ${mem.Sum === null ? "nothing" : mem.Sum}, not 12. Load First, add Second, then store in Sum.`));
  };
})();

/* ---------- Practise ---------- */
practise([
  { h: "1 · Match the mnemonic", type: "match", prompt: "Match each mnemonic or term to its meaning.", pairs: [
    ["LDA", "Load the value of a variable into the accumulator"], ["ADD", "Add the value of a variable to the value in the accumulator"], ["STO", "Store the accumulator's value in a variable"],
    ["Assembler", "Translates assembly language into machine code"], ["Mnemonic", "A short, readable code used in place of a binary instruction"],
  ] },
  { h: "2 · Put the program in order", type: "order", prompt: "Order the instructions so that Sum = First + Second.", items: ["LDA First", "ADD Second", "STO Sum"], done: "Load, add, store." },
  { h: "3 · Assembly or machine code?", type: "classify", prompt: "Drag each item to the correct language.", buckets: [{ label: "Assembly" }, { label: "Machine code" }], items: [
    { text: "LDA First", b: 0 }, { text: "STO Sum", b: 0 }, { text: "Uses mnemonics", b: 0 }, { text: "Needs an assembler", b: 0 },
    { text: "0001 00010010", b: 1 }, { text: "Binary instructions", b: 1 }, { text: "Run directly by the processor", b: 1 },
  ], done: "Assembly is readable, machine code is binary." },
  { h: "4 · Trace it", type: "calc", qs: [
    { q: "First = 6 and Second = 9. After LDA First, ADD Second and STO Sum, what is stored in Sum?", a: 15, sol: "6 + 9 = 15." },
    { q: "First = 20, Second = 5. What does the accumulator hold after LDA First and ADD Second?", a: 25, sol: "20 + 5 = 25." },
    { q: "A program is: LDA A, ADD B, ADD C, STO Total with A = 4, B = 3, C = 10. What is Total?", a: 17, sol: "4 + 3 + 10 = 17." },
    { q: "How many machine code instructions will the four-instruction program above produce (one per assembly instruction)?", a: 4, sol: "Assembly is usually translated one-to-one, so 4." },
  ] },
  { h: "5 · Multiple choice", type: "quiz", qs: [
    { q: "What does STO do?", opts: ["Stores the accumulator's value in a variable", "Stops the program", "Subtracts a number", "Starts the assembler"], a: 0, why: "STO writes the accumulator back to memory." },
    { q: "Which program translates assembly into machine code?", opts: ["Assembler", "Compiler", "Interpreter", "Linker"], a: 0, why: "An assembler is the translator for assembly language." },
    { q: "Why might a programmer choose assembly?", opts: ["To save memory and run quickly", "To make the program portable", "Because it is easy to debug", "To avoid using the processor"], a: 0, why: "Assembly can be small and fast but is not portable." },
    { q: "Which is true of assembly language?", opts: ["It is machine dependent", "It works on every processor", "It is high-level", "It needs no translation"], a: 0, why: "It relates to one type of computer." },
  ] },
]);

real([
  ["Games and special effects", "Some graphics routines in games are hand-written in low-level code so they run as fast as possible on a particular graphics chip.", "Assembly makes use of special hardware and can perform a task very quickly."],
  ["Tiny microcontrollers", "A chip in a thermostat may have only a small memory, so a programmer may write assembly to fit the program in.", "Assembly can take up little space in primary memory."],
  ["Reverse engineering and debugging", "Security researchers and engineers often read assembly to see exactly what a program asks the processor to do.", "Shows assembly is readable compared with binary."],
  ["Early computers", "Early programmers had to write directly in machine code or assembly. High-level languages were invented to make this easier.", "Why high-level languages are easier to read, write and debug."],
  ["Different chips, different assembly", "A phone chip and a laptop chip have different instruction sets, so they use different assembly languages.", "Assembly is machine dependent."],
]);

exam([
  { cmd: "State", m: 3, q: "An assembly program has the instructions LDA, ADD and STO. State what each one does.", tip: "One mark each.", ans: [["k", "LDA loads the value of a variable into the accumulator."], ["k", "ADD adds the value of a variable to the value in the accumulator."], ["k", "STO stores the value in the accumulator in a variable."]], warn: "Saying ADD \"adds two variables\". It adds to the accumulator." },
  { cmd: "Explain", m: 2, q: "Explain why a programmer might choose to write a program in assembly language.", tip: "Two of the four reasons.", ans: [["k", "To make use of special hardware or machine-dependent instructions."], ["k", "To write code that takes up little memory or performs a task very quickly."]], warn: "Saying it is easier to write." },
  { cmd: "State", m: 2, q: "What is an assembler?", tip: "Translator, assembly, machine code.", ans: [["k", "A program that translates a program written in assembly language"], ["k", "into machine code."]], warn: "Confusing it with a compiler." },
  { cmd: "Describe", m: 2, q: "Describe one difference between assembly language and machine code.", tip: "Readable vs binary.", ans: [["k", "Assembly uses mnemonics that people can read, whereas machine code is binary."], ["k", "Assembly needs to be translated by an assembler, machine code can be run directly."]], warn: "Saying one is high-level." },
  { cmd: "Calculate", m: 3, q: "First = 8 and Second = 11. Trace LDA First, ADD Second, STO Sum. State the accumulator after each instruction.", tip: "Three values.", ans: [["k", "After LDA First: 8"], ["k", "After ADD Second: 19"], ["k", "After STO Sum: accumulator still 19, and Sum = 19"]], warn: "Forgetting that the accumulator keeps its value after STO." },
  { cmd: "State", m: 2, q: "Give two disadvantages of writing in assembly language.", tip: "Time, difficulty, portability.", ans: [["k", "It takes longer to write and debug."], ["k", "It is harder to understand and only works on one type of computer."]], warn: "Saying it is \"slow to run\"." },
]);

tips([
  "<b>Know the three mnemonics:</b> LDA loads, ADD adds, STO stores. Say \"the accumulator\" in each.",
  "<b>Trace carefully.</b> Write the accumulator value after every instruction.",
  "<b>Assembly is low-level.</b> It is machine dependent and not portable.",
  "<b>Four reasons for assembly:</b> special hardware, machine-dependent instructions, small memory, speed.",
  "<b>One-to-one:</b> usually one assembly instruction becomes one machine code instruction.",
  "<b>An assembler translates assembly.</b> A compiler translates a high-level language.",
  "<b>The machine code is what runs.</b> You do not need the assembler to run it again.",
  "<b>Do not say assembly is high-level.</b> Java is high-level, and it is not assembly.",
], [
  ["Assembly language", "A low-level language that uses mnemonics and has to be translated into machine code."], ["Mnemonic", "A short readable code that stands for an instruction, such as LDA."],
  ["Accumulator", "A register in the processor that holds the value being worked on."], ["LDA", "Load the value of a variable into the accumulator."],
  ["ADD", "Add the value of a variable to the value in the accumulator."], ["STO", "Store the value in the accumulator in a variable."],
  ["Assembler", "A program that translates assembly language into machine code."], ["Machine dependent", "Only runs on a particular type of computer or processor."],
]);
