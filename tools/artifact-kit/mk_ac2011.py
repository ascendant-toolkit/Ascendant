"""A Level CS syllabus 20.1.1: programming paradigms, low-level (addressing modes) and imperative. Run: python3 tools/artifact-kit/mk_ac2011.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>programming paradigm</b> is a style of programming, a way of thinking about how a program is built. <b>Low-level</b> programs work with the processor's own instruction set and give direct control of registers and memory, and the way an instruction finds its data is the <b>addressing mode</b>: immediate, direct, indirect, indexed or relative. <b>Imperative (procedural)</b> programs are an ordered list of commands that change the program's state, organised into procedures and functions. <b>Object-oriented</b> programs are built from classes and objects, and <b>declarative</b> programs state facts and rules and ask a question. This page covers the first two paradigms; the next pages take the other two.</p></div>

  <h2>1 · What is a programming paradigm?</h2>
  <p>A paradigm is a way of organising a program. The same problem can be solved in more than one paradigm, and a paradigm suits some problems better than others. Many languages support more than one: Python can be written in an imperative, an object-oriented or a (partly) functional style.</p>
  <div class="tw"><table class="t">
    <tr><th>Paradigm</th><th>The program is...</th><th>You will see</th></tr>
    <tr><td><b>Low-level</b></td><td>a list of instructions from the processor's instruction set</td><td>Opcodes and operands: <code>LDD 500</code>, <code>ADD Total</code>, <code>STO Z</code></td></tr>
    <tr><td><b>Imperative (procedural)</b></td><td>an explicit sequence of commands that update the program state, with or without procedure calls</td><td>Variables, <code>IF</code>, <code>FOR</code>, <code>WHILE</code>, procedures and functions</td></tr>
    <tr><td><b>Object-oriented</b></td><td>objects of classes that hold data and the methods that use it</td><td><code>class</code>, inheritance, polymorphism, encapsulation</td></tr>
    <tr><td><b>Declarative</b></td><td>a description of the result wanted (facts, rules and a goal), not the steps to get there</td><td><code>parent(john, ethel).</code> and queries</td></tr>
  </table></div>

  <h2>2 · Low-level programming</h2>
  <p><b>Low-level</b> code is written close to the hardware. <b>Machine code</b> is binary the processor runs directly; <b>assembly language</b> uses short readable mnemonics (<code>LDD</code>, <code>ADD</code>) that an <b>assembler</b> translates into machine code. Each assembly instruction is usually one machine instruction, and every processor family has its own instruction set.</p>
  <div class="tw"><table class="t">
    <tr><th>Benefits</th><th>Drawbacks</th></tr>
    <tr><td>Direct control of registers, memory and hardware; small, fast programs; no hidden overheads</td><td>Hard to write, read, debug and maintain; many lines for one simple task</td></tr>
    <tr><td>Used where speed or size matters: device drivers, embedded systems, parts of an operating system</td><td>Not portable: the code is written for one processor, so it must be rewritten for another</td></tr>
  </table></div>

  <h2>3 · Addressing modes</h2>
  <p>An instruction has an <b>opcode</b> (what to do) and an <b>operand</b> (the data, or where to find it). The <b>addressing mode</b> is the way the operand is used to find the data. The exam gives the instruction set, so learn the idea behind each mode rather than the mnemonics.</p>
  <div class="tw"><table class="t">
    <tr><th>Mode</th><th>How the operand is used</th><th>Example (ACC after)</th></tr>
    <tr><td><b>Immediate</b></td><td>The operand <i>is</i> the value</td><td><code>LDM #500</code>: ACC = 500</td></tr>
    <tr><td><b>Direct</b></td><td>The operand is the address that holds the value</td><td><code>LDD 500</code>: ACC = the contents of address 500</td></tr>
    <tr><td><b>Indirect</b></td><td>The operand is the address of a location that holds <i>another address</i>, and the value is at that second address</td><td><code>LDI 500</code>: read address 500, use what it holds as an address, load from there</td></tr>
    <tr><td><b>Indexed</b></td><td>The address used is the operand <i>plus</i> the contents of the index register (IX)</td><td><code>LDX 200</code> with IX = 3: load from address 203</td></tr>
    <tr><td><b>Relative</b></td><td>The address used is found by adding an offset (the operand) to the address of the current instruction</td><td>A relative jump of +4 from address 1050 continues at 1054</td></tr>
  </table></div>
  <div class="tip"><b class="h">Worked example (May/June 2022)</b>Address 500 holds 100 and address 100 holds 20. <code>LDM #500</code> loads 500 (immediate). <code>LDD 500</code> loads 100 (direct: the contents of address 500). <code>LDI 500</code> loads 20 (indirect: address 500 holds 100, so go to address 100). Same operand, three different answers.</div>
  <p><b>Why indexed addressing exists:</b> arrays. Store the first element at address 200, then set IX to 0, 1, 2... and the same instruction <code>LDX 200</code> reads each element in turn. <b>Why relative addressing exists:</b> the code works wherever it is placed in memory, because jumps are measured from where they are, not from a fixed address.</p>

  <h2>4 · Writing a low-level program</h2>
  <p>The May/June 2022 question asked for code to add the constant 20 to the value stored at the address held in variable Y, and store the result in Z. The steps are always the same: load, calculate, store, then declare the data after the code with labels.</p>
  <div class="code">''' + pc('''LDM #20       // load the constant
STO Twenty    // the constant must be stored somewhere so it can be added
LDI Y         // indirect: Y holds an address, load the value at that address
ADD Twenty    // add the constant
STO Z         // store the answer
END
Twenty: #0
Y:      #0
Z:      #0''') + '''</div>
  <p class="note">Only ACC can be added to, and ADD works on an address, not a number. That is why the constant is stored first. Labels for data go after the program code.</p>

  <h2>5 · Imperative (procedural) programming</h2>
  <p>An <b>imperative</b> program is a sequence of commands, run in the order written, where each command changes something: a variable, an output, a file. Procedural code is imperative code organised into <b>procedures and functions</b>, so a task can be named, reused and tested on its own. You already write this: every Paper 4 program is imperative.</p>
  <ul>
    <li><b>Variables</b> hold the state, and assignment changes it.</li>
    <li><b>Constructs:</b> sequence, selection (<code>IF</code>, <code>CASE</code>) and iteration (<code>FOR</code>, <code>WHILE</code>, <code>REPEAT</code>).</li>
    <li><b>Procedures</b> do a job; <b>functions</b> return a value. Parameters pass data in.</li>
    <li><b>Structured programming</b> (AS 11.3): modules with one entry and one exit, top-down design, no unstructured jumps.</li>
  </ul>
  <div class="code">''' + pc('''total = 0
for i in range(1, 5):
    total = total + i      # each pass changes the state of total
print(total)               # 10''') + '''</div>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Describing imperative code as "code that uses loops". The mark is for the <b>sequence of commands that change the program state</b>, in the order written.</li>
    <li>Calling <code>LDD 500</code> "immediate" because the number is written in the instruction. Immediate has the <code>#</code>: the number is the data.</li>
    <li>Stopping one step early on indirect addressing. Indirect needs two reads: the address, then the value.</li>
    <li>Forgetting to store a constant at an address before using ADD, or putting the labelled data in the middle of the program.</li>
    <li>Writing "declarative means no loops". Say it states the result wanted using facts and rules, not how to get it.</li>
  </ul>
'''

watch = '''
  <h2>1 · Immediate, direct and indirect</h2>
  <p>Press Play, or click the steps. Address 500 holds 100 and address 100 holds 20, as in the May/June 2022 question.</p>
  <div id="stA"></div>
  <h2>2 · Indexed addressing</h2>
  <div id="stB"></div>
  <h2>3 · Relative addressing</h2>
  <div id="stC"></div>
  <h2>4 · An imperative program changes state</h2>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · Which value does ACC get?</h2>
  <p>Memory is shown below. Choose the addressing mode, the operand and (for indexed) the index register, and read how the value is found.</p>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div><div id="mX"></div><div id="mS"></div>
    <div class="readout"><div><small>Instruction</small><strong id="a1"></strong></div><div><small>Address used</small><strong id="a2"></strong></div><div><small>ACC becomes</small><strong id="a3"></strong></div></div>
    <div class="verdict" id="av"></div></div>

  <h2>Lab 2 · Run the assembly program</h2>
  <p>The May/June 2022 program adds 20 to the value that Y points to. Step through it and watch ACC and memory. Y holds the address 700, and address 700 holds 35.</p>
  <div class="card"><div id="pS"></div><div class="btnrow"><button class="b pri" id="pN">Step</button><button class="b" id="pR">Reset</button></div><div class="verdict" id="pv"></div></div>

  <h2>Lab 3 · Compare the paradigms</h2>
  <p>Choose a paradigm to see its key facts in the words an answer needs.</p>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · Which paradigm is this code?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which addressing mode?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps of indirect addressing in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · What does ACC hold?</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A washing machine controller", "The program in a simple appliance often runs on a small microcontroller with very little memory. It can be written in assembly or very close to it so it fits and responds instantly.", "low-level code is chosen for tiny devices where speed and size matter, at the cost of portability.") +
rw("Device drivers and boot code", "The first instructions that run when a computer starts, and the code that talks to a graphics card or a disk, need exact control of registers and memory addresses, so parts of them are low-level.", "low-level gives direct hardware control that a high-level language hides.") +
rw("A spreadsheet macro or a Python script", "A list of commands such as read the file, loop through the rows, add the total, print the result is imperative: each step changes the state and the order matters.", "imperative means a sequence of commands that change the program state, in the order written.") +
rw("Arrays and indexed addressing", "When a program reads item after item from a list, the processor adds an index to the start address of the list. That is indexed addressing, one instruction used over and over with a changing index.", "indexed addressing is the answer when a question mentions arrays or tables of data.") +
rw("Position-independent code", "Code that uses relative addresses can be loaded anywhere in memory without changing its jumps, which is why shared libraries use it.", "relative addressing measures from the current instruction, not from a fixed address.")
)

where = [
  ("M/J 2021", "31, 32, 33", "9(a), 9(b)", "2 + 2", "Describe imperative and declarative programming"),
  ("M/J 2021", "31, 32, 33", "9(c)", "4", "Identify the paradigm of four code examples"),
  ("O/N 2021", "31, 32", "2", "4", "Match four paradigms to their descriptions"),
  ("M/J 2022", "31, 33", "9(a)", "3", "State the addressing mode and ACC for LDM, LDD and LDI"),
  ("M/J 2022", "31, 33", "9(b)", "7", "Write assembly code using the given instruction set")]

past = '''  <p class="note">Indexed and relative addressing, and the imperative paradigm on its own, have not been asked as separate questions in Papers 3 and 4 (May/June 2021 to Oct/Nov 2025). Every Paper 4 program is written in an imperative style, so imperative skills are tested in all of them. Questions below are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Describing and identifying paradigms</h3>
''' + peq(SRC("s21", "31, 32, 33", "Q9(a), (b)"), "2 + 2 marks", "Describe",
  "(a) Describe what is meant by an imperative (procedural) programming language. (b) Describe what is meant by a declarative programming language.",
  "Two marks each. (a) is about a sequence of commands that change the state. (b) is about stating what is wanted, using facts and rules.",
  "<p><b>(a)</b> " + mks(["The statements form a sequence of commands for the computer to perform", "in the order written, and each line of code changes something in the program state."]) + "</p><p><b>(b)</b> " + mks(["It states what needs to be done instead of how to do it,", "using facts and rules that are queried to satisfy a goal."], "a") + "</p>",
  "Defining imperative as \"uses loops and IF statements\". That describes constructs, not the paradigm.") + peq(SRC("s21", "31, 32, 33", "Q9(c)"), "4 marks", "Identify",
  "Identify the programming paradigm for each of these program code examples.<pre class=\"plain\">(1)  male(john).\n     female(ethel).\n     parent(john, ethel).\n\n(2)  FOR Counter = 1 TO 20\n         X = X * Counter\n     NEXT Counter\n\n(3)  Start: LDD Counter\n            INC ACC\n            STO Counter\n\n(4)  public class Vehicle\n     {\n         private speed;\n         public Vehicle()\n         {\n             speed = 0;\n         }\n     }</pre>",
  "Look for the giveaway: facts ending in a full stop, a counted loop, mnemonics with a label, the word class.",
  "<p>" + mks(["(1) Declarative (facts, so logic programming)", "(2) Imperative / procedural (assignment inside a loop)", "(3) Low-level / assembly (opcode and operand, label)", "(4) Object-oriented (a class with a constructor)"]) + "</p>",
  "Calling (3) imperative. It does change state in order, but the opcodes and labels make it low-level.") + peq(SRC("w21", "31, 32", "Q2"), "4 marks", "Match",
  "Draw one line from each programming paradigm to its most appropriate description. Paradigms: declarative, imperative, low-level, object-oriented. Descriptions: (A) programs using the instruction set of a processor; (B) programs based on events such as user actions or sensor outputs; (C) programs using the concepts of class, inheritance, encapsulation and polymorphism; (D) programs with an explicit sequence of commands that update the program state, with or without procedure calls; (E) programs that specify the desired result rather than how to get to it.",
  "Four paradigms, five descriptions: one description is a distractor.",
  "<p>" + mks(["Low-level matches (A) the processor's instruction set", "Object-oriented matches (C) class, inheritance, encapsulation, polymorphism", "Imperative matches (D) a sequence of commands that update the state", "Declarative matches (E) the desired result, not how to get it"]) + "</p><p>Description (B) is the odd one out: it describes event-driven programming, which is not one of the four paradigms.</p>",
  "Matching imperative to \"specify the desired result\". That is declarative: imperative gives the steps.") + '''
  <h3>Addressing modes and writing assembly</h3>
''' + peq(SRC("s22", "31, 33", "Q9(a)"), "3 marks", "State",
  "A processor has one general purpose register, the accumulator (ACC). The table shows part of its instruction set. The address 500 contains the value 100 and the address 100 contains the value 20. State the addressing mode and the contents of ACC after each instruction has been executed: <code>LDM #500</code>, <code>LDD 500</code>, <code>LDI 500</code>."
  + '<div class="tw"><table class="t"><tr><th>Instruction</th><th>Explanation</th></tr><tr><td><code>LDM #n</code></td><td>Load the number n to ACC</td></tr><tr><td><code>LDD &lt;address&gt;</code></td><td>Load the contents of the given address to ACC</td></tr><tr><td><code>LDI &lt;address&gt;</code></td><td>The address to be used is at the given address. Load the contents of this second address to ACC</td></tr><tr><td><code>ADD &lt;address&gt;</code></td><td>Add the contents of the given address to the ACC</td></tr><tr><td><code>STO &lt;address&gt;</code></td><td>Store the contents of the ACC at the given address</td></tr><tr><td><code>&lt;label&gt;: &lt;data&gt;</code></td><td>Gives a symbolic address to the memory location holding the data; the label can be used in place of an address. # denotes a denary number</td></tr></table></div>',
  "One mark per instruction, and the mode and the ACC value must both be right. Indirect needs two reads.",
  "<p>" + mks(["LDM #500: immediate, ACC = 500", "LDD 500: direct, ACC = 100", "LDI 500: indirect, ACC = 20 (address 500 holds 100, so read address 100)"]) + "</p>",
  "Answering 100 for LDI. That stops after the first read. Indirect follows the address once more.") + peq(SRC("s22", "31, 33", "Q9(b)"), "7 marks", "Write",
  "Using only the instruction set above, write assembly language code to: use the constant 20, which needs to be stored; add this constant to the value stored in the address contained in the variable Y; and store the result in variable Z.",
  "Plan: load the constant, store it with a label, load indirectly through Y, add, store in Z, then label the data after the code.",
  "<p>Seven marks: " + mks(["<code>LDM #20</code> seen", "store 20 at an address", "that address labelled (e.g. Twenty) away from the program code", "Y and Z labelled away from the program code", "correct use of <code>LDI Y</code>", "correct use of <code>STO Z</code>", "correct use of <code>ADD</code> with the labelled address"]) + "</p>" + pc('''LDM #20
STO Twenty
LDI Y
ADD Twenty
STO Z
Twenty: #0
Y:      #0
Z:      #0'''),
  "Using <code>ADD #20</code>. The instruction set has no immediate ADD, which is why the constant is stored first. Also using LDD Y, which gives the address held in Y, not the value it points to.")

review = req("2 marks", "Distinguish", "Distinguish between immediate and direct addressing.", "One mark each: what the operand is in each mode. Give an example instruction if you can.",
  "<p>" + mks(["Immediate: the operand is the value to use, e.g. LDM #25 loads 25.", "Direct: the operand is the address that holds the value, e.g. LDD 25 loads the contents of address 25."]) + "</p>", "Saying direct uses the value in the instruction. That is immediate.") + req("3 marks", "Explain", "A program reads each element of an array stored from address 300 onwards. Explain why indexed addressing suits this task.", "Say what the effective address is, and what changes between elements.",
  "<p>" + mks(["In indexed addressing the address used is the operand plus the contents of the index register.", "The operand can be the start address of the array (300) and stay the same.", "Adding one to the index register each time moves to the next element, so one instruction can read every element in a loop."]) + "</p>", None) + req("2 marks", "State", "Index register IX holds 4 and address 204 holds 77. State the value loaded by LDX 200.", "Add the operand and IX first.",
  "<p>" + mks(["Address = 200 + 4 = 204", "ACC = 77"]) + "</p>", None) + req("3 marks", "Give", "Give three drawbacks of writing a program in a low-level language.", "Think about the programmer, the processor and the time taken.",
  "<p>" + mks(["Hard to write, read and debug; one task needs many instructions.", "Not portable: it only runs on the processor it was written for.", "The programmer must manage registers and memory directly, so errors are easier to make."]) + "</p>", None) + req("2 marks", "State", "Name the paradigm described: a program is a set of facts and rules and a goal that the system tries to satisfy. Name the paradigm used by a program with classes Customer and Order.", "One paradigm each.",
  "<p>" + mks(["Declarative", "Object-oriented"]) + "</p>", None) + req("3 marks", "Complete", "ACC holds 12. Address 50 holds 8 and address 8 holds 30. Give the value in ACC after each instruction, run one after another: ADD 50, then LDI 50, then LDM #50.", "Run them in order and track ACC. Each load replaces ACC; ADD adds to it.",
  "<p>" + mks(["ADD 50: 12 + 8 = 20", "LDI 50: address 50 holds 8, so ACC = the contents of address 8 = 30", "LDM #50: ACC = 50"]) + "</p>", "Adding the contents of address 8 in the first step. ADD is direct, so it uses address 50 itself.")

exam = exam20("Part 1 is real 9618 questions on the paradigms and low-level programming (Paper 3). Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Name the paradigm by its giveaway.", "Facts and rules: declarative. Class: object-oriented. Opcodes and labels: low-level. Assignments in loops: imperative."),
  ("Write the full definition.", "Imperative: a sequence of commands, in order, that change the program state. Declarative: say what is wanted, using facts and rules, not how."),
  ("Count the reads.", "Immediate zero, direct one, indirect two. Write each address you visit."),
  ("Track ACC line by line.", "Load replaces ACC. ADD changes it. STO does not change ACC."),
  ("Store the constant first.", "There is no immediate ADD in the exam instruction set."),
  ("Data labels go last.", "Place labelled data after the program code and before nothing else in the answer."),
], [
  ("imperative", "A sequence of commands that are carried out in the order written and change the state of the program."),
  ("declarative", "The program states what result is wanted, using facts and rules, instead of how to reach it."),
  ("low-level", "The program uses the instruction set of the processor, with direct control of registers and memory."),
  ("indirect addressing", "The operand is the address of a location that holds the address of the data."),
], [("State", "A short fact or the value, no explanation."), ("Describe", "Say what it is or how it works, in a few clear points."), ("Identify", "Pick the right paradigm or mode and name it."), ("Write", "Produce code that follows the given instruction set exactly.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const lines = ["LDM #500", "LDD 500", "LDI 500"];
  const draw = (s) => {
    const c = Math.round(s.i); let o = "";
    o += codeList(30, 40, lines, c - 1, 1, 34, 190);
    o += memCell(430, 40, 100, 20, c >= 3 ? "cell-ok" : "f3", 1) + memCell(430, 100, 500, 100, "f3", 1);
    o += regBox(250, 170, "ACC", c === 0 ? "" : c === 1 ? 500 : c === 2 ? 100 : 20, "f2", 1);
    o += SV.text(430, 32, "memory", "sm") + SV.text(30, 32, "program", "sm");
    if (c === 1) o += arrow(140, 108 - 34, 250, 195, "r", "c1", 1);
    if (c === 2) o += arrow(430, 120, 372, 190, "l", "c2", 1) + SV.text(596, 125, "read address 500", "sm");
    if (c === 3) o += arrow(505, 140, 505, 124, "u", "c3", 1) + arrow(430, 60, 372, 185, "l", "c2", 1) + SV.text(596, 125, "1: read address 500 = 100", "sm") + SV.text(596, 65, "2: read address 100 = 20", "sm");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 250, label: "Immediate, direct and indirect addressing", base: { i: 0 }, draw, tween: 500, dwell: 4000, steps: [
    { cap: "Address <b>500</b> holds <b>100</b> and address <b>100</b> holds <b>20</b>. Three instructions use the same operand, 500. ACC is empty.", s: { i: 0 } },
    { cap: "<code>LDM #500</code> is <b>immediate</b>: the operand (marked with #) is the data. ACC = <b>500</b>. No memory is read.", s: { i: 1 } },
    { cap: "<code>LDD 500</code> is <b>direct</b>: the operand is the address that holds the data. Read address 500: ACC = <b>100</b>.", s: { i: 2 } },
    { cap: "<code>LDI 500</code> is <b>indirect</b>: address 500 holds <b>100</b>, and that is itself an address. Read address 100: ACC = <b>20</b>. Two reads.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const c = Math.round(s.i); let o = "";
    for (let k = 0; k < 5; k++) o += memCell(430, 30 + k * 44, 200 + k, [11, 22, 33, 44, 55][k], c >= 3 && k === 3 ? "cell-ok" : "f3", 1);
    o += SV.text(430, 22, "array stored from address 200", "sm");
    o += regBox(40, 40, "Index register IX", c >= 1 ? 3 : "", "f1", c >= 1 ? 1 : 0.35, 200);
    o += SV.text(40, 130, "LDX 200", "lbl bd", { style: "font-family:var(--mono);font-size:20px" });
    if (c >= 2) o += SV.text(40, 165, "200 + IX = 200 + 3 = 203", "lbl", { style: "font-family:var(--mono);font-size:16px" });
    if (c >= 3) o += arrow(300, 160, 430, 142 + 22, "r", "c2", 1) + regBox(40, 195, "ACC", 44, "f2", 1);
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 260, label: "Indexed addressing", base: { i: 0 }, draw, tween: 500, dwell: 4000, steps: [
    { cap: "An array is stored from address <b>200</b>. To read any element, use one instruction, <code>LDX 200</code>, and change the index register.", s: { i: 0 } },
    { cap: "The <b>index register (IX)</b> holds <b>3</b>: the position of the element wanted (counting from 0).", s: { i: 1 } },
    { cap: "<b>Indexed addressing</b> adds IX to the operand: 200 + 3 = <b>203</b>.", s: { i: 2 } },
    { cap: "The contents of address 203 are loaded: ACC = <b>44</b>. Add 1 to IX and the same instruction reads the next element.", s: { i: 3 } }] });
})();

(function () {
  const L = ["1049  LDD Count", "1050  JMR +4", "1051  ADD One", "1052  STO Count", "1053  OUT", "1054  END"];
  const draw = (s) => {
    const c = Math.round(s.i); let o = codeList(30, 30, L, c === 0 ? -1 : c === 1 ? 1 : 5, 1, 34, 260);
    o += regBox(400, 60, "PC (current instruction)", c === 0 ? 1049 : c === 1 ? 1050 : 1054, "f1", 1, 240);
    if (c >= 1) o += SV.text(400, 160, "operand = offset +4", "lbl", { style: "font-family:var(--mono);font-size:16px" });
    if (c >= 2) o += SV.text(400, 190, "1050 + 4 = 1054", "lbl bd", { style: "font-family:var(--mono);font-size:18px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 250, label: "Relative addressing", base: { i: 0 }, draw, tween: 500, dwell: 4000, steps: [
    { cap: "The program counter (PC) holds the address of the current instruction. A <b>relative</b> jump gives an <b>offset</b>, not a fixed address.", s: { i: 0 } },
    { cap: "At address <b>1050</b> the instruction is a relative jump of <b>+4</b>.", s: { i: 1 } },
    { cap: "The next address is the current address plus the offset: 1050 + 4 = <b>1054</b>, so the three instructions in between are skipped.", s: { i: 2 } },
    { cap: "If this block of code were loaded at a different address, the jump would still land in the right place, because the offset is measured from where the instruction is. That is why relative addressing makes code <b>position-independent</b>.", s: { i: 2 } }] });
})();

(function () {
  const L = ["total = 0", "count = 1", "while count <= 3:", "    total = total + count", "    count = count + 1"];
  const seq = [[0, 0, 0, -1], [0, 1, 0, -1], [1, 0, 1, 2], [3, 0, 1, 3], [4, 0, 2, 4], [3, 1, 2, 3], [4, 1, 3, 4], [3, 3, 3, 3], [4, 3, 4, 4]];
  const draw = (s) => {
    const k = Math.round(s.i), st = [["", ""], ["0", ""], ["0", "1"], ["0", "1"], ["1", "1"], ["1", "2"], ["3", "2"], ["3", "3"], ["6", "4"]][k], hl = [-1, 0, 1, 3, 4, 3, 4, 3, 4][k];
    let o = codeList(30, 30, L, hl, 1, 34, 300);
    o += regBox(420, 50, "total", st[0], "f1", 1) + regBox(560, 50, "count", st[1], "f2", 1);
    o += SV.text(420, 140, "the state changes one command at a time", "sm");
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 230, label: "An imperative program changing state", base: { i: 0 }, draw, tween: 400, dwell: 2500, steps: [
    { cap: "A short program with two variables. Nothing has run yet, so there is no state.", s: { i: 0 } },
    { cap: "<code>total = 0</code>: the first command sets the state.", s: { i: 1 } },
    { cap: "<code>count = 1</code>: executed next, in the order written.", s: { i: 2 } },
    { cap: "The loop adds count to total: total becomes <b>1</b>.", s: { i: 4 } },
    { cap: "count becomes <b>2</b>. Each line changes something: this is what makes it imperative.", s: { i: 5 } },
    { cap: "Second pass: total becomes <b>3</b>.", s: { i: 6 } },
    { cap: "count becomes <b>3</b>.", s: { i: 7 } },
    { cap: "Third pass: total becomes <b>6</b>, count becomes <b>4</b>, and the loop condition now fails.", s: { i: 8 } }] });
})();

/* Lab 1: addressing explorer */
(function () {
  const M = { 20: 7, 31: 9, 100: 20, 101: 31, 102: 42, 103: 53, 104: 64, 200: 101, 201: 202, 300: 100, 500: 100 };
  const modes = [["Immediate", "LDM #"], ["Direct", "LDD "], ["Indirect", "LDI "], ["Indexed", "LDX "]];
  let m = 2, op = 500, ix = 1;
  const cell = (a) => (a in M ? M[a] : 0);
  const paint = () => {
    $$("#mB button").forEach((b, i) => b.classList.toggle("pri", i === m));
    let addr = "none", val = op, why = "";
    if (m === 0) { why = `The operand ${op} is the value, so no memory is read.`; }
    if (m === 1) { addr = op; val = cell(op); why = `Read address ${op}: it holds ${val}.`; }
    if (m === 2) { const a2 = cell(op); addr = op + " then " + a2; val = cell(a2); why = `Read address ${op}: it holds ${a2}. Use ${a2} as an address: it holds ${val}.`; }
    if (m === 3) { addr = op + ix; val = cell(op + ix); why = `Address = ${op} + IX (${ix}) = ${op + ix}, which holds ${val}.`; }
    $("#a1").textContent = modes[m][1] + op; $("#a2").textContent = addr; $("#a3").textContent = val; $("#av").textContent = why;
    $("#mX").style.display = m === 3 ? "" : "none";
    const keys = Object.keys(M).map(Number).sort((a, b) => a - b);
    $("#mS").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Address</th>' + keys.map((k) => `<td>${k}</td>`).join("") + "</tr><tr><th>Contents</th>" + keys.map((k) => `<td>${M[k]}</td>`).join("") + "</tr></table></div>";
  };
  $("#mB").innerHTML = modes.map((x, i) => `<button class="b" data-i="${i}">${x[0]}</button>`).join("");
  $$("#mB button").forEach((b) => (b.onclick = () => { m = +b.dataset.i; if (m === 3 && op > 200) op = 100; if (m === 2 && ![100, 200, 300, 500].includes(op)) op = 500; paint(); }));
  const opts = [100, 101, 200, 300, 500];
  Lib.slider($("#mO"), { id: "mos", label: "Operand ", min: 0, max: opts.length - 1, value: 4, fmt: (x) => opts[x], onInput: (v) => { op = opts[v]; paint(); } });
  Lib.slider($("#mX"), { id: "mxs", label: "Index register IX ", min: 0, max: 4, value: ix, fmt: (x) => x, onInput: (v) => { ix = v; paint(); } });
  paint();
})();

/* Lab 2: step through the assembly program */
(function () {
  const prog = ["LDM #20", "STO Twenty", "LDI Y", "ADD Twenty", "STO Z", "END"];
  const mem0 = () => ({ Twenty: 0, Y: 700, Z: 0, 700: 35 });
  let pc = 0, acc = "", mem = mem0();
  const paint = (msg) => {
    $("#pS").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Next</th><th>Instruction</th><th>ACC</th><th>Twenty</th><th>Y</th><th>Z</th><th>addr 700</th></tr><tr><td>' + (pc < prog.length ? pc + 1 : "-") + "</td><td>" + (pc < prog.length ? prog[pc] : "finished") + "</td><td>" + acc + "</td><td>" + mem.Twenty + "</td><td>" + mem.Y + "</td><td>" + mem.Z + "</td><td>" + mem[700] + "</td></tr></table></div>";
    $("#pv").textContent = msg || "Press Step to run the first instruction.";
  };
  $("#pN").onclick = () => {
    if (pc >= prog.length) return;
    const ins = prog[pc]; let msg = "";
    if (ins === "LDM #20") { acc = 20; msg = "LDM #20: immediate, ACC = 20."; }
    else if (ins === "STO Twenty") { mem.Twenty = acc; msg = "STO Twenty: the 20 in ACC is stored at the labelled address, so it can be added later."; }
    else if (ins === "LDI Y") { acc = mem[mem.Y]; msg = `LDI Y: Y holds ${mem.Y}, so ACC takes the contents of address ${mem.Y}, which is ${acc}.`; }
    else if (ins === "ADD Twenty") { acc = acc + mem.Twenty; msg = `ADD Twenty: ACC = 35 + 20 = ${acc}.`; }
    else if (ins === "STO Z") { mem.Z = acc; msg = `STO Z: Z now holds ${acc}.`; }
    else msg = "END: the program stops. Z = 55, the value pointed to by Y plus 20.";
    pc++; paint(msg);
  };
  $("#pR").onclick = () => { pc = 0; acc = ""; mem = mem0(); paint(); };
  paint();
})();

btnTable("eB", "eO", [
  ["Low-level", "Instructions from the processor's instruction set; direct control of registers and memory", "Assembly language, e.g. LDD, ADD, STO", "Small fast programs for embedded devices and drivers; hard to write and not portable", "Saying it is 'the language with no loops'"],
  ["Imperative (procedural)", "A sequence of commands, in the order written, that change the program state; procedures and functions", "Python, Pascal, C-style code with assignments and loops", "Most programs; structured and easy to follow", "Defining it only by 'uses IF and loops'"],
  ["Object-oriented", "Objects created from classes; data and methods together; inheritance, polymorphism, encapsulation", "Java, Python classes", "Large systems with many related things to model", "Mixing up class (the template) and object (an instance)"],
  ["Declarative", "States what result is wanted using facts and rules; the system works out how, by satisfying a goal", "Prolog, SQL", "Queries over knowledge: family trees, databases, expert systems", "Calling it 'code without variables'"]
], ["Paradigm", "Key idea", "Example", "Typical use", "Trap"]);
''' + CLASSIFY("cl1", "Which paradigm does each piece of code show?", ["Low-level", "Imperative", "Object-oriented", "Declarative"],
  [("LDM #5 then ADD Total then STO Total", 0), ("while x < 10: x = x + 1", 1), ("class Dog: def __init__(self, name): self.name = name", 2), ("parent(sam, tom). father(X, Y) :- parent(X, Y), male(X).", 3), ("JMP Loop", 0), ("for item in items: total = total + item", 1), ("class Circle(Shape):", 2), ("female(ethel). ?- female(X).", 3)],
  "Opcodes: low-level. Assignments in order: imperative. class: object-oriented. Facts, rules and a query: declarative.") + CLASSIFY("cl2", "Which addressing mode is each description?", ["Immediate", "Direct", "Indirect", "Indexed", "Relative"],
  [("The operand is the value to use", 0), ("The operand is the address that holds the value", 1), ("The operand is the address of a location that holds the address of the value", 2), ("The address used is the operand plus the contents of the index register", 3), ("An offset is added to the address of the current instruction", 4), ("LDM #7", 0), ("LDD 7", 1), ("LDI 7", 2), ("Suits reading each element of an array in turn", 3)],
  "Immediate: the data. Direct: one read. Indirect: two reads. Indexed: operand + IX. Relative: offset from where the instruction is.") + ORDER(
  "Put the steps for LDI 500 in order.",
  ["Fetch the instruction LDI 500", "Read the contents of address 500", "Use that value as a second address", "Read the contents of the second address", "Store that value in ACC"],
  "Two reads: the address, then the value.") + MATCH([
  ["Opcode", "The part of an instruction that says what to do"], ["Operand", "The part of an instruction that gives the data or where it is"], ["Addressing mode", "The way the operand is used to find the data"], ["Assembler", "Translates assembly language into machine code"], ["Index register", "A register whose contents are added to the operand to give the address"]]) + CALC([
  {"q": "Address 40 holds 7 and address 7 holds 90. What does LDM #40 put in ACC?", "a": 40, "unit": "", "tol": 0.01, "hint": "Immediate: the operand is the data.", "sol": "<b>40</b>."},
  {"q": "Address 40 holds 7 and address 7 holds 90. What does LDD 40 put in ACC?", "a": 7, "unit": "", "tol": 0.01, "hint": "Direct: the contents of address 40.", "sol": "<b>7</b>."},
  {"q": "Address 40 holds 7 and address 7 holds 90. What does LDI 40 put in ACC?", "a": 90, "unit": "", "tol": 0.01, "hint": "Indirect: address 40 holds 7, then read address 7.", "sol": "<b>90</b>."},
  {"q": "IX holds 5. Which address does LDX 300 read?", "a": 305, "unit": "", "tol": 0.01, "hint": "300 + 5.", "sol": "<b>305</b>."},
  {"q": "A relative jump of +6 is at address 2000. At which address does the program continue?", "a": 2006, "unit": "", "tol": 0.01, "hint": "Current address plus the offset.", "sol": "<b>2006</b>."},
  {"q": "ACC holds 10. Address 20 holds 4. What does ACC hold after ADD 20?", "a": 14, "unit": "", "tol": 0.01, "hint": "10 + 4.", "sol": "<b>14</b>."},
  {"q": "Address 8 holds 12. After LDD 8 then ADD 8, what does ACC hold?", "a": 24, "unit": "", "tol": 0.01, "hint": "12, then 12 + 12.", "sol": "<b>24</b>."},
  {"q": "How many memory reads does LDI need to get the data?", "a": 2, "unit": "reads", "tol": 0.01, "hint": "The address, then the value.", "sol": "<b>2</b>."}]) + MCQ([
  ("What is an addressing mode?", ["The speed of the processor", "The way the operand is used to find the data", "The type of memory used", "The size of an instruction"], 1, "It is how the operand is interpreted."),
  ("Which mode puts the operand itself into the register?", ["Direct", "Indirect", "Immediate", "Indexed"], 2, "Immediate: the operand is the data."),
  ("A programmer wants to read every element of an array with one instruction in a loop. Which mode suits?", ["Immediate", "Indexed", "Direct", "Relative"], 1, "Indexed adds a changing index to the start address."),
  ("Which description fits an imperative program?", ["States the result wanted using facts and rules", "A sequence of commands that change the program state", "A set of classes and objects", "Instructions of the processor"], 1, "That is the definition the mark scheme uses."),
  ("What is a drawback of low-level programs?", ["They run slowly", "They are hard to write and not portable", "They cannot control memory", "They cannot use registers"], 1, "They are processor-specific and hard to maintain."),
  ("Which paradigm is Prolog?", ["Low-level", "Imperative", "Object-oriented", "Declarative"], 3, "Prolog uses facts, rules and queries.")], "qz1") + CARDS([
  ("Programming paradigm", "A style of programming, a way of organising a program."), ("Low-level", "Uses the processor's instruction set. Direct control, not portable."), ("Imperative", "Sequence of commands, in order, changing the program state."), ("Immediate", "The operand is the value. LDM #n."),
  ("Direct", "The operand is the address holding the value. LDD."), ("Indirect", "The address holds another address; read twice. LDI."), ("Indexed", "Address = operand + IX. Arrays."), ("Relative", "Address = current address + offset. Position-independent.")])

build("ac2011", "ac-20-1-1-paradigms-low-level-imperative", "Programming Paradigms: Low-level and Imperative", EYA("20.1.1"),
  "What a programming paradigm is, low-level programming and the five addressing modes, imperative (procedural) programming, step-by-step animations, labs and the real past paper questions on paradigms.",
  dict(sub=CBK("Chapter 20 · Further programming, section 20.1 Programming paradigms"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
