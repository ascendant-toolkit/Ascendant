"""AS CS 4.2.1: assembly language, the assembler (one-pass and two-pass) and instruction groups. Run: python3 tools/artifact-kit/mk_as421.py"""
from ak42 import *

IGROUPS = '''<div class="tw"><table class="t">
    <tr><th>Instruction group</th><th>What it does</th><th>Examples from the instruction set</th></tr>
    <tr><td>Data movement</td><td>Loads, stores and moves data</td><td>LDM #n, LDD address, LDI address, LDX address, LDR #n, MOV IX, STO address</td></tr>
    <tr><td>Input and output of data</td><td>Takes input from the user or outputs a character</td><td>IN, OUT</td></tr>
    <tr><td>Arithmetic operations</td><td>Adds and subtracts, increments and decrements</td><td>ADD address, ADD #n, SUB address, INC ACC, INC IX, DEC ACC</td></tr>
    <tr><td>Compare instructions</td><td>Compares the ACC with a value; the result is used by the next jump</td><td>CMP address, CMP #n</td></tr>
    <tr><td>Unconditional and conditional instructions</td><td>Jumps to another instruction: always (unconditional) or following a compare (conditional)</td><td>JMP address, JPE address, JPN address</td></tr>
  </table></div>'''

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Machine code</b> is the binary instructions the processor executes directly; <b>assembly language</b> is a low-level language that uses <b>mnemonics</b> (LDD, ADD, STO) instead of binary, with one assembly instruction for each machine code instruction. Each instruction has an <b>opcode</b> (what to do) and an <b>operand</b> (what to do it to), written with <b>absolute addresses</b> (such as 365) or <b>symbolic addresses</b> (such as Total) using labels. An <b>assembler</b> translates assembly language into machine code (binary). A <b>one-pass</b> assembler translates in one go; a <b>two-pass</b> assembler is needed to deal with labels used before they are defined: the <b>first pass</b> creates a <b>symbol table</b> (each label and its address), and the <b>second pass</b> translates each instruction, replacing every label by its address. The instruction set is arranged into <b>groups</b>: data movement, input and output, arithmetic, compare, and conditional and unconditional jumps.</p></div>

  <h2>1 · Machine code, assembly and high-level languages</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Machine code</th><th>Assembly language</th><th>High-level language</th></tr>
    <tr><td>Written as</td><td>Binary (or hex)</td><td>Mnemonics, labels</td><td>Statements close to English</td></tr>
    <tr><td>Translation</td><td>None: run directly</td><td>Assembler to machine code</td><td>Compiler or interpreter</td></tr>
    <tr><td>Relationship to the processor</td><td>One instruction per operation</td><td>One assembly instruction per machine instruction; processor-specific</td><td>Many machine instructions per statement; portable</td></tr>
  </table></div>
  <p>An instruction is made of an <b>opcode</b> and an <b>operand</b>. For <span class="mono">LDD 365</span> the opcode is LDD (load direct) and the operand is address 365. <span class="mono">#</span> marks a denary number, <span class="mono">B</span> a binary number and <span class="mono">&amp;</span> a hexadecimal number.</p>

  <h2>2 · The assembler</h2>
  <p>A program with labels cannot be translated line by line in one go, because an instruction may refer to a label that is defined later. The two-pass assembler solves this:</p>
  <ol>
    <li><b>First pass:</b> read the program, work out the address of every instruction, and create a <b>symbol table</b> of each label and its address (symbolic addresses are noted, nothing is translated yet).</li>
    <li><b>Second pass:</b> translate each instruction: the mnemonic becomes its binary opcode, and each label used as an operand is replaced by its address from the symbol table. The result is the machine code.</li>
  </ol>
  <p>A one-pass assembler translates in a single pass and must keep a list of the places where forward-referenced labels were used so they can be filled in later (backpatched).</p>

  <h2>3 · Instruction groups</h2>
  ''' + IGROUPS + '''

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Saying the first pass "translates the program". It creates the symbol table.</li>
    <li>Saying an assembler translates to "binary or machine code", but writing "high-level language" instead of assembly code.</li>
    <li>Giving an example instruction with no operand, for example just LDM. Every example needs a suitable operand.</li>
    <li>Putting CMP in the conditional group. CMP is a compare instruction; JPE and JPN are the conditional jumps.</li>
    <li>Mixing up the opcode (the operation) with the operand (the data or address).</li>
  </ul>
'''

watch = '''
  <h2>1 · Assembly language to machine code</h2>
  <div id="stA"></div>
  <h2>2 · The first pass builds the symbol table</h2>
  <div id="stB"></div>
  <h2>3 · The second pass uses it</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Two-pass assembler</h2>
  <p>Step through the program. The first pass finds the addresses of labels; the second replaces them. (The binary opcodes here are illustrative.)</p>
  <div class="card"><div class="btnrow"><button id="as_step">Step</button><button id="as_reset">Reset</button></div><div id="asP"></div><div id="asS"></div><div id="asM"></div><div id="asL" class="verdict"></div></div>
  <h2>Lab 2 · Which instruction group?</h2>
  <div class="card"><div id="gB" class="btnrow"></div><div id="gO"></div></div>
  <h2>Lab 3 · Opcode and operand</h2>
  <div class="card"><div id="oB" class="btnrow"></div><div id="oO"></div></div>
'''

_pr, _prjs = PR(["Which instruction group?", "Pass one or pass two?", "Match the term to its meaning", "Put the assembling steps in order", "Working out", "Multiple choice"],
  ("Which instruction group does it belong to?", ["Data movement", "Arithmetic", "Compare", "Jump"], [("LDM #5", 0), ("ADD 100", 1), ("CMP 101", 2), ("JPE 96", 3), ("STO 200", 0), ("INC ACC", 1)], "Load and store: data movement. ADD, INC: arithmetic."),
  ("Pass one or pass two of a two-pass assembler?", ["First pass", "Second pass"], [("Creates the symbol table", 0), ("Replaces labels by addresses", 1), ("Works out the address of each label", 0), ("Translates mnemonics into binary opcodes", 1), ("Produces the machine code", 1), ("Records each label and its address", 0)], "Pass one: symbol table. Pass two: machine code."),
  [["Opcode", "The part of an instruction that says what to do"], ["Operand", "The data or address the instruction acts on"], ["Assembler", "Translates assembly language into machine code"], ["Symbol table", "Each label and its address"], ["Mnemonic", "A short word standing for an opcode, such as ADD"]],
  ("Put the steps of a two-pass assembler in order.", ["Read the whole program", "Work out the address of each instruction", "Add each label and its address to the symbol table", "Translate each instruction on the second pass", "Replace each label by its address from the symbol table"], "Read, addresses, symbol table, translate, replace."),
  [{"q": "A program starts at address 100 and each instruction takes one location. A label is on the fourth instruction. What address goes in the symbol table?", "a": 103, "unit": "", "tol": 0.01, "hint": "100, 101, 102, 103.", "sol": "<b>103</b>."}, {"q": "A program has 12 instructions, one location each. How many passes does a two-pass assembler make over the program?", "a": 2, "unit": "", "tol": 0.01, "hint": "Two passes.", "sol": "<b>2</b>."}, {"q": "How many instruction groups are listed in the Learn tab?", "a": 5, "unit": "", "tol": 0.01, "hint": "Data movement, input/output, arithmetic, compare, jumps.", "sol": "<b>5</b>."}, {"q": "An opcode is 4 bits and an operand is 8 bits. How many bits per instruction?", "a": 12, "unit": "bits", "tol": 0.01, "hint": "4 + 8.", "sol": "<b>12</b> bits."}, {"q": "With a 4-bit opcode, how many different opcodes are possible?", "a": 16, "unit": "", "tol": 0.01, "hint": "2^4.", "sol": "<b>16</b>."}],
  [("An assembler translates:", ["Assembly language into machine code", "High-level code into assembly", "Machine code into text", "Binary into hex"], 0, "Assembly to machine code."), ("The first pass creates the:", ["Symbol table", "Machine code", "Operand", "Stack"], 0, "Symbol table."), ("JPE is a:", ["Conditional jump", "Compare", "Data movement", "Input"], 0, "Conditional."), ("In LDD 365, 365 is the:", ["Operand", "Opcode", "Mnemonic", "Label"], 0, "Operand."), ("IN and OUT belong to the group:", ["Input and output", "Data movement", "Arithmetic", "Compare"], 0, "Input and output."), ("Assembly language is:", ["Processor-specific", "Portable between all processors", "A high-level language", "Binary"], 0, "Processor-specific.")],
  [("Machine code", "Binary instructions run directly."), ("Assembly language", "Mnemonics; one per machine instruction."), ("Assembler", "Assembly to machine code."), ("First pass", "Builds the symbol table."), ("Second pass", "Translates; replaces labels."), ("Symbol table", "Labels and their addresses."), ("Opcode / operand", "What to do / what to do it to."), ("Groups", "Data movement, I/O, arithmetic, compare, jumps.")])

real = RWNOTE + (
rw("The code inside a microwave", "The program was written in a language close to the processor, such as assembly, because the chip has very little memory and each instruction counts.", "assembly for small embedded systems.") +
rw("Why old games run fast on old consoles", "Developers wrote in assembly to control every instruction of the processor.", "low-level control.") +
rw("Debugging a crash", "Engineers read the assembly the compiler produced to find which instruction failed.", "assembly maps one-to-one to machine code.") +
rw("A label in a loop", "In 'LOOP: ADD #1 ... JPN LOOP' the assembler works out the address of LOOP once, so the programmer never counts addresses.", "symbol table.") +
rw("Portable against fast", "An assembly program only runs on the processor it was written for; a high-level program can be recompiled for another processor.", "assembly is processor-specific.")
)

where = [
  ("O/N 2021", "11, 13", "4(d)", "4", "Complete the descriptions of compilers, interpreters and assemblers"),
  ("O/N 2021", "12", "8(b)(ii)", "4", "An example instruction from each instruction group"),
  ("O/N 2022", "13", "3(b)", "4", "Describe two instruction groups"),
  ("O/N 2023", "11", "8(a), (b)(i)", "1 + 3", "The purpose of the first pass of a two-pass assembler; an example from each group"),
  ("O/N 2023", "12", "9(a)", "4", "Identify the group for IN, ADD, JPE and CMI"),
  ("M/J 2025", "13", "6(c)", "3", "Name the group for loading data, incrementing the index register and branching")]

past = '''  <p class="note">The two-pass assembler is examined directly in only one series (O/N 2023); the instruction groups are asked about two or three times a year. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording. The instruction set table is printed on the paper, so you do not have to learn every opcode, but you must be able to read it.</p>
''' + peq(SRC("w21", "11/13", "Q4(d)"), "4 marks", "Complete",
  "Complete the descriptions of language translators by writing the missing words. ... are usually used when a high-level language program is complete. They translate all the code at the same time and then run the program. They produce ... files that can be run without the source code. ... translate one line of a high-level language program at a time, and then run that line. Assemblers are used to translate assembly code into ... .", "Compilers, executable, interpreters, machine code.",
  "<p>" + mks(["Compilers", "executable (or .exe or object code) files", "Interpreters", "binary or machine code"]) + "</p>", None) + peq(SRC("w21", "12", "Q8(b)(ii)"), "4 marks", "Give",
  "Give one example instruction from the table for each instruction group: data movement; input and output of data; arithmetic operations; unconditional and conditional instructions; compare instructions. Each instruction must have a suitable operand. (The table has LDM, LDD, STO, INC, CMP, JPN, JMP, IN, OUT and END.)", "LDM #2, OUT, INC ACC, JMP 100, CMP 100.",
  "<p>" + mks(["Data movement: LDM #2", "Input and output of data: IN or OUT", "Arithmetic operations: INC ACC or INC IX", "Unconditional and conditional: JPN 100 or JMP 100", "Compare: CMP 100"]) + " (one mark each, max 4)</p>", "Giving the instruction with no operand, for example just STO.") + peq(SRC("w22", "13", "Q3(b)"), "4 marks", "Describe",
  "The instructions LDM, LDD and LDI are examples of the data movement group. Describe two other instruction groups.", "Group name and what it does.",
  "<p>One mark for the group name and one for a description, twice: " + mks(["Input and output of data: takes an input from the user or outputs the character of the binary number", "Arithmetic operations: performs addition and subtraction", "Unconditional and conditional instructions: move to another instruction (identified by a label)", "Compare instructions: compare the result to another value"]) + "</p>", None) + peq(SRC("w23", "11", "Q8(a)(b)(i)"), "1 + 3 marks", "Identify / Give",
  "(a) Identify the purpose of the first pass of a two-pass assembler. (b)(i) Give one example of an instruction that belongs to each of these groups: data movement, arithmetic operation, conditional instruction. Use only the instructions LDR #n, STO address, ADD address, INC register, CMP #n, JPE address, OUT, each with a suitable operand.", "Create a symbol table. LDR #50, ADD 100, JPE 96.",
  "<p><b>(a)</b> " + mks(["To create a symbol table"]) + "</p><p><b>(b)(i)</b> " + mks(["Data movement: LDR #50 or STO 201", "Arithmetic operation: ADD 100 or INC IX", "Conditional instruction: JPE 96"]) + "</p>", "Writing 'translates the program' for the first pass. It makes the symbol table; the translation is the second pass.") + peq(SRC("w23", "12", "Q9(a)"), "4 marks", "Identify",
  "Identify the instruction group for each of the opcodes IN, ADD, JPE and CMI.", "I/O; arithmetic; conditional; compare.",
  "<p>" + mks(["IN: input and output of data", "ADD: arithmetic operations", "JPE: unconditional and conditional instructions", "CMI: compare instructions"]) + "</p>", None) + peq(SRC("s25", "13", "Q6(c)"), "3 marks", "Complete",
  "Assembly language instructions are grouped. Loading data into the accumulator is an example of an instruction in the ... group. Incrementing the index register is an example of the ... group. Branching to another address is an example of the ... group.", "Data movement, arithmetic, conditional and unconditional.",
  "<p>" + mks(["Data movement", "Arithmetic operations", "Conditional and unconditional (jump) instructions"]) + "</p>", None)

review = req("2 marks", "State", "State two differences between assembly language and a high-level language.", "Processor-specific, mnemonics.", "<p>" + mks(["Assembly language is specific to one processor; a high-level language is portable", "Assembly uses mnemonics with one instruction per machine instruction; a high-level statement becomes several machine instructions"]) + "</p>", None) + req("3 marks", "Describe", "Describe the two passes of a two-pass assembler.", "Symbol table, then translate.", "<p>" + mks(["First pass: creates a symbol table of labels and their addresses", "Second pass: translates each mnemonic into its binary opcode", "and replaces each label used as an operand by its address from the symbol table"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a program with labels needs a symbol table.", "Forward references.", "<p>" + mks(["An instruction may use a label that is defined later in the program", "so the address of every label must be known before the instructions can be translated"]) + "</p>", None) + req("1 mark", "State", "State the group of the instruction CMP #5.", "Compare.", "<p>" + mks(["Compare instructions"]) + "</p>", None) + req("2 marks", "Identify", "In the instruction LDD 365, identify the opcode and the operand.", "Operation, address.", "<p>" + mks(["Opcode: LDD", "Operand: 365"]) + "</p>", None)

tips = tips_html([
  ("First pass: symbol table.", "Second pass: machine code."),
  ("Opcode: what. Operand: on what.", "Name them in that order."),
  ("Examples need an operand.", "'LDM #2', not 'LDM'."),
  ("CMP compares; JPE jumps.", "Two different groups."),
  ("Assembler: assembly to machine code.", "Not high-level."),
  ("One assembly line, one machine instruction.", "That is why it is low-level."),
], [("a mnemonic", "A short word standing for an opcode."), ("a symbol table", "A table of labels and their addresses."), ("a label", "A name given to an address."), ("an operand", "The data or address an instruction acts on.")],
  [("Identify", "Name the point."), ("Describe", "Several points."), ("Give", "An example."), ("Complete", "Fill in the missing words.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const lines = [["LDM #5", "0001 00000101"], ["ADD #3", "0010 00000011"], ["STO 200", "0101 11001000"]];
    let o = SV.text(120, 20, "assembly", "lbl bd", { "text-anchor": "middle" }) + SV.text(430, 20, "machine code", "lbl bd", { "text-anchor": "middle" }) + SV.rect(240, 70, 100, 40, "f3", { rx: 8 }) + SV.text(290, 95, "assembler", "lbl bd", { "text-anchor": "middle", style: "font-size:13px" });
    lines.forEach(([a, m], i) => { o += SV.rect(30, 30 + i * 34, 180, 28, "cell", { rx: 4 }) + SV.text(40, 49 + i * 34, a, "lbl"); if (k > i) o += SV.rect(360, 30 + i * 34, 180, 28, "f1", { rx: 4 }) + SV.text(370, 49 + i * 34, m, "lbl"); });
    if (k > 0) o += SV.path("M210,90 H240", "ax") + SV.path("M340,90 H360", "ax"); return o; };
  Lib.stepper($("#stA"), { w: 580, h: 150, label: "Assembler", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "Assembly language uses mnemonics and operands.", s: { i: 0 } }, { cap: "The assembler translates <b>LDM #5</b> into a binary opcode and operand.", s: { i: 1 } }, { cap: "<b>ADD #3</b> is translated next.", s: { i: 2 } }, { cap: "<b>STO 200</b> is translated. The result is machine code: binary.", s: { i: 3 } }] });
})();
const ASM = [["", "LDM #0"], ["LOOP", "ADD #1"], ["", "CMP #3"], ["", "JPN LOOP"], ["", "END"]], OPC = { LDM: "0001", ADD: "0010", CMP: "0011", JPN: "0100", END: "1111" }, BASE = 100;
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; ASM.forEach(([l, ins], i) => { o += SV.rect(30, 20 + i * 30, 250, 26, i === 1 && k >= 1 ? "f3" : "cell", { rx: 4 }) + SV.text(40, 38 + i * 30, (BASE + i) + "  " + (l ? l + ": " : "") + ins, "lbl"); });
    if (k >= 1) o += SV.rect(340, 60, 190, 60, "f1", { rx: 6 }) + SV.text(435, 82, "symbol table", "sm", { "text-anchor": "middle" }) + SV.text(435, 106, "LOOP = 101", "lbl bd", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stB"), { w: 560, h: 190, label: "First pass", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "The first pass reads the program and numbers each instruction from 100.", s: { i: 0 } }, { cap: "It finds the label <b>LOOP</b> on address 101 and records it in the <b>symbol table</b>.", s: { i: 1 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 20, 160, 40, "f1", { rx: 6 }) + SV.text(100, 45, "LOOP = 101", "lbl bd", { "text-anchor": "middle" }) + SV.rect(240, 20, 150, 28, "cell", { rx: 4 }) + SV.text(250, 38, "103  JPN LOOP", "lbl");
    if (k >= 1) o += SV.path("M180,40 H240", "ax"); if (k >= 2) o += SV.rect(240, 70, 300, 28, "f3", { rx: 4 }) + SV.text(250, 88, "0100 01100101   (JPN, 101)", "lbl"); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 120, label: "Second pass", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "On the second pass the assembler reaches <b>JPN LOOP</b>.", s: { i: 0 } }, { cap: "It looks LOOP up in the symbol table: address <b>101</b>.", s: { i: 1 } }, { cap: "It writes the opcode for JPN and the address 101 as machine code.", s: { i: 2 } }] });
})();

(function () {
  let st; const bin8 = (n) => ("00000000" + n.toString(2)).slice(-8);
  const reset = () => { st = { k: 0, sym: {}, mc: [] }; paint(); };
  const step = () => { const n = ASM.length; if (st.k < n) { const [l] = ASM[st.k]; if (l) st.sym[l] = BASE + st.k; } else if (st.k < 2 * n) { const i = st.k - n; const [l, ins] = ASM[i]; const [op, a] = ins.split(" "); let v = 0; if (a) v = a[0] === "#" ? +a.slice(1) : st.sym[a]; st.mc[i] = OPC[op] + " " + bin8(v); } else return; st.k++; paint(); };
  const paint = () => { const n = ASM.length; const pass = st.k < n ? 1 : 2; const cur = st.k < n ? st.k : st.k - n;
    $("#asP").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Address</th><th>Source</th><th>Machine code</th></tr>' + ASM.map(([l, ins], i) => `<tr style="${st.k < 2 * n && i === cur ? "background:var(--accent-soft);font-weight:700" : ""}"><td>${BASE + i}</td><td>${l ? l + ": " : ""}${ins}</td><td>${st.mc[i] || ""}</td></tr>`).join("") + "</table></div>";
    $("#asS").innerHTML = "<b>Symbol table:</b> " + (Object.keys(st.sym).length ? Object.entries(st.sym).map(([k, v]) => k + " = " + v).join(", ") : "empty");
    $("#asL").innerHTML = st.k >= 2 * n ? "Assembly finished: the program is now machine code." : st.k < n ? `First pass: reading instruction at address ${BASE + cur}.` : `Second pass: translating address ${BASE + cur}.`; };
  $("#as_step").onclick = step; $("#as_reset").onclick = reset; reset();
})();
btnTable("gB", "gO", [
  ["LDD 365", "Data movement", "Loads data from an address"],
  ["IN", "Input and output", "Takes a character from the keyboard"],
  ["ADD #5", "Arithmetic", "Adds a number to the ACC"],
  ["CMP 366", "Compare", "Compares ACC with a location"],
  ["JPE 209", "Conditional jump", "Jumps if the compare was true"],
  ["JMP 200", "Unconditional jump", "Always jumps"]
], ["Instruction", "Group", "What it does"]);
btnTable("oB", "oO", [
  ["LDM #5", "LDM", "#5 (denary 5)"],
  ["STO 200", "STO", "200 (an address)"],
  ["JPN LOOP", "JPN", "LOOP (a symbolic address)"],
  ["AND B00001111", "AND", "B00001111 (a binary mask)"],
  ["END", "END", "no operand"]
], ["Instruction", "Opcode", "Operand"]);
''' + _prjs

finish("as-4-2-1-assembly-language-assembler", "as421", "Assembly Language and the Assembler",
  "Machine code against assembly language, opcode and operand, how a two-pass assembler builds a symbol table and translates, and the instruction groups, with animations, an assembler lab and the real Paper 1 questions from 2021 to 2026.",
  "4.2.1", "4 · Processor fundamentals", "section 4.2 Assembly language", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on assembly language, the assembler and instruction groups (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
