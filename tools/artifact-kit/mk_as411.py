"""AS CS 4.1.1: Von Neumann model, registers, ALU, CU, clock, buses. Run: python3 tools/artifact-kit/mk_as411.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>The <b>Von Neumann model</b> has a processor (CPU) made of an <b>Arithmetic and Logic Unit (ALU)</b>, a <b>Control Unit (CU)</b>, <b>registers</b> and a <b>system clock</b>, connected by <b>buses</b> to <b>main memory</b> (the Immediate Access Store, IAS) and to input and output. Its key idea is the <b>stored program concept</b>: instructions and data are stored in the same memory space (main memory) and the CPU fetches instructions one at a time. Registers are tiny, very fast stores inside the CPU: <b>special purpose</b> registers have one defined role (PC, MAR, MDR, CIR, IX, SR) and <b>general purpose</b> registers (such as the Accumulator, ACC) hold data during operations. The <b>address bus</b> carries addresses, the <b>data bus</b> carries data and instructions, and the <b>control bus</b> carries control signals such as read, write, timing and interrupt. Exam answers state each part's purpose in one precise sentence.</p></div>

  <h2>1 · The components</h2>
  <div class="tw"><table class="t">
    <tr><th>Component</th><th>Purpose</th></tr>
    <tr><td><b>ALU</b></td><td>Performs arithmetic (add, subtract) and logical (AND, OR, shift, compare) operations</td></tr>
    <tr><td><b>Control Unit (CU)</b></td><td>Reads an instruction from the address in the PC, decodes it, coordinates and synchronises the other components, manages execution of instructions and sends and receives control signals along the control bus</td></tr>
    <tr><td><b>System clock</b></td><td>Creates timing signals (sent on the control bus) that synchronise all operations; its speed (clock speed) sets how many fetch-execute cycles can run per second</td></tr>
    <tr><td><b>Registers</b></td><td>Fast storage locations inside the CPU</td></tr>
    <tr><td><b>Main memory (IAS)</b></td><td>Holds all the instructions, data and programs currently in use; volatile; fast access</td></tr>
    <tr><td><b>Buses</b></td><td>Sets of parallel wires that carry signals between components</td></tr>
  </table></div>
  <p>The <b>stored program concept</b>: instructions and data are held together in main memory, in the same memory space, and are fetched and executed in sequence by the CPU. The program does not have to be rewired for each task: loading a different program into memory changes what the computer does.</p>

  <h2>2 · Registers</h2>
  <div class="tw"><table class="t">
    <tr><th>Register</th><th>Purpose</th><th>Type</th></tr>
    <tr><td>Program Counter (PC)</td><td>Holds the address of the next instruction to be fetched</td><td>Special</td></tr>
    <tr><td>Memory Address Register (MAR)</td><td>Holds the address of the memory location currently being read from or written to</td><td>Special</td></tr>
    <tr><td>Memory Data Register (MDR)</td><td>Holds the data or instruction read from the address in the MAR, or the data to be written to it</td><td>Special</td></tr>
    <tr><td>Current Instruction Register (CIR)</td><td>Holds the instruction currently being decoded and executed</td><td>Special</td></tr>
    <tr><td>Index Register (IX)</td><td>Holds a number that is added to the operand to form the address of the data (indexed addressing)</td><td>Special</td></tr>
    <tr><td>Status Register (SR)</td><td>Holds bits (flags) that are set or cleared by the results of arithmetic and logic operations, or by interrupts, and can be checked to change the instruction sequence</td><td>Special</td></tr>
    <tr><td>Accumulator (ACC)</td><td>Holds the intermediate results of arithmetic and logical operations</td><td>General</td></tr>
  </table></div>
  <p><b>Special purpose</b> registers have a specified role and hold the state of the program's execution; <b>general purpose</b> registers can be used for whatever the programmer defines and hold data during operations.</p>

  <h2>3 · The three buses</h2>
  <div class="tw"><table class="t">
    <tr><th>Bus</th><th>Carries</th><th>Direction</th><th>Width affects</th></tr>
    <tr><td>Address bus</td><td>The address from the MAR</td><td>One way, from the CPU to memory</td><td>How many memory locations can be addressed: <b>2<sup>n</sup></b> for n lines</td></tr>
    <tr><td>Data bus</td><td>Data and instructions, to and from the MDR</td><td>Both ways</td><td>How much data is transferred at the same time</td></tr>
    <tr><td>Control bus</td><td>Control signals: read, write, timing signals from the clock, interrupt, bus requests</td><td>Both ways</td><td>Not a performance factor</td></tr>
  </table></div>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Saying the PC "stores the next instruction". It stores the <b>address</b> of the next instruction (the corrected statement in the exam).</li>
    <li>Saying the CU sends signals "on the data bus". They travel on the <b>control bus</b>.</li>
    <li>Saying the MDR "transfers data to the address in the MAR". It holds the data read from, or to be written to, that address.</li>
    <li>Describing the clock only as "making the computer faster". Say it synchronises operations with timing signals.</li>
    <li>Confusing special and general purpose registers: special purpose have one defined role.</li>
  </ul>
'''

watch = '''
  <h2>1 · The Von Neumann model</h2>
  <div id="stA"></div>
  <h2>2 · Which bus?</h2>
  <div id="stB"></div>
  <h2>3 · The stored program concept</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Address bus width</h2>
  <p>The number of memory locations that can be addressed is 2 to the power of the number of address lines.</p>
  <div class="card"><div id="aS"></div><div id="aV" class="verdict"></div></div>
  <h2>Lab 2 · Which register?</h2>
  <div class="card"><div id="rB" class="btnrow"></div><div id="rO"></div></div>
  <h2>Lab 3 · Which bus?</h2>
  <div class="card"><div id="bB" class="btnrow"></div><div id="bO"></div></div>
'''

_pr, _prjs = PR(["Special or general purpose register?", "Which bus?", "Match the register to its role", "Put the CPU steps in order", "Working out", "Multiple choice"],
  ("Special purpose or general purpose register?", ["Special purpose", "General purpose"], [("Program Counter", 0), ("Holds temporary data during operations", 1), ("Status Register", 0), ("Can be used for any purpose the programmer defines", 1), ("Memory Address Register", 0), ("Accumulator", 1)], "PC, MAR, MDR, CIR, IX, SR are special. ACC is general."),
  ("Which bus carries it?", ["Address bus", "Data bus", "Control bus"], [("The address from the MAR", 0), ("The instruction read from memory", 1), ("A timing signal from the clock", 2), ("A read signal", 2), ("The data to be written to memory", 1), ("The address of the next instruction", 0)], "Address, data, control."),
  [["PC", "Address of the next instruction to be fetched"], ["MAR", "Address of the location being read or written"], ["MDR", "Data read from, or to be written to, memory"], ["CIR", "Instruction currently being decoded and executed"], ["SR", "Flags set by arithmetic, logic and interrupts"]],
  ("Put the stored program steps in order.", ["The program is loaded into main memory", "The PC holds the address of the first instruction", "The CPU fetches the instruction from main memory", "The instruction is decoded and executed", "The PC moves on to the next instruction"], "Load, PC, fetch, execute, next."),
  [{"q": "An address bus has 16 lines. How many memory locations can it address?", "a": 65536, "unit": "", "tol": 0.01, "hint": "2^16.", "sol": "<b>65536</b>."}, {"q": "An address bus has 20 lines. How many locations (in thousands, 1 K = 1024)? Give the number of K.", "a": 1024, "unit": "K", "tol": 0.5, "hint": "2^20 ÷ 1024.", "sol": "<b>1024</b> K (1 M)."}, {"q": "A data bus is 32 bits wide. How many bytes are transferred at once?", "a": 4, "unit": "bytes", "tol": 0.01, "hint": "32 ÷ 8.", "sol": "<b>4</b> bytes."}, {"q": "A CPU runs at 3 GHz and one fetch-execute cycle takes 3 clock ticks. How many cycles per second, in millions?", "a": 1000, "unit": "million", "tol": 0.5, "hint": "3000 ÷ 3.", "sol": "<b>1000</b> million."}, {"q": "How many special purpose registers are listed in the Learn tab table (PC, MAR, MDR, CIR, IX, SR)?", "a": 6, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>6</b>."}],
  [("The Program Counter holds:", ["The address of the next instruction", "The next instruction", "The result", "The flags"], 0, "Address."), ("The control bus carries:", ["Control signals", "Only addresses", "Only data", "Power"], 0, "Control signals."), ("Which is a general purpose register?", ["Accumulator", "PC", "MAR", "SR"], 0, "ACC."), ("The stored program concept means:", ["Instructions and data are in the same memory", "Programs are stored on paper", "Data is in ROM only", "The CPU stores programs"], 0, "Same memory space."), ("A wider data bus allows:", ["More data to be transferred at once", "More memory addresses", "A faster clock", "More registers"], 0, "More data at once."), ("The system clock:", ["Synchronises operations with timing signals", "Stores data", "Does arithmetic", "Holds the PC"], 0, "Timing signals.")],
  [("ALU", "Arithmetic and logic operations."), ("CU", "Decodes, coordinates and sends control signals."), ("PC", "Address of the next instruction."), ("MAR", "Address being read or written."), ("MDR", "Data read or to be written."), ("CIR", "Instruction being executed."), ("Address bus", "Carries the address; one way."), ("Data bus", "Carries data and instructions; both ways.")])

real = RWNOTE + (
rw("The 4 GB limit on 32-bit systems", "A 32-bit address bus can address 2^32 locations, which is 4 GB. That is why older 32-bit computers could not use more memory.", "address bus width limits memory.") +
rw("Buying a computer: '64-bit'", "A wider data bus moves more data per step, so the processor spends less time waiting for data.", "data bus width.") +
rw("Running a different app", "The same hardware runs a game or a spreadsheet because the program is stored in memory, not built into the circuits.", "stored program concept.") +
rw("A phone's clock speed", "A 3 GHz clock makes three billion timing signals each second; each fetch-execute stage waits for these signals.", "the clock synchronises operations.") +
rw("A calculator's overflow warning", "The status register holds a flag that is set when an arithmetic result is too large, and the program can check it.", "status register flags.")
)

where = [
  ("O/N 2021", "12", "8(a)", "4 + 1", "The role of the MAR and MDR; another special purpose register"),
  ("O/N 2022", "11", "5(a), (b)", "1 + 3 + 1 + 2", "The stored program concept; PC, IX and SR; the system buses; the Control Unit"),
  ("O/N 2022", "13", "4(a)(i), (b)", "2 + 2", "The roles of the MAR and MDR; the purpose of the system clock"),
  ("O/N 2023", "11", "5(a), (b)", "4 + 2", "Two other special purpose registers; the Immediate Access Store"),
  ("O/N 2023", "13", "9(a)", "3 + 2", "Other components of the Von Neumann model; special against general purpose registers"),
  ("M/J 2023", "12", "5(a)", "2", "Two signals a control bus can carry"),
  ("O/N 2024", "11", "3(a), 8", "2 + 2 + 2", "The purpose of the system clock and CU; the status register; special against general purpose registers"),
  ("O/N 2024", "12", "3(a)", "4", "The purpose of PC, MAR, MDR and IX"),
  ("M/J 2025", "12", "1(a), (b)", "3 + 2", "Correct three incorrect statements about the Von Neumann model; another register"),
  ("M/J 2025", "13", "2(a)(i)", "2", "How the CU and system clock work together"),
  ("O/N 2025", "11", "6(a)", "2", "The role of the ACC and CIR")]

past = '''  <p class="note">Register roles are tested in Paper 1 every series. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("w21", "12", "Q8(a)"), "4 + 1 marks", "Describe / Identify",
  "Describe the role of the Memory Address Register (MAR) and the Memory Data Register (MDR) in the fetch-execute cycle. Identify one other special purpose register.", "MAR: address. MDR: data from that address, then copied to the CIR.",
  "<p>Up to two marks for each register: " + mks(["MAR stores the next address to be fetched", "held in the Program Counter (PC)", "The data at this address is then fetched", "MDR stores the data from the address pointed to by the MAR", "The data in it is copied to the Current Instruction Register (CIR)"]) + "</p><p>Other register: " + mks(["Program Counter, Current Instruction Register, Status Register or Interrupt Register"], "a") + "</p>", None) + peq(SRC("w22", "11", "Q5(a)(b)"), "1 + 3 + 1 + 2 marks", "State / Tick / Describe",
  "(a) State what is meant by the stored program concept in the Von Neumann model. (b)(i) State the role of the Program Counter, the Index Register and the Status Register. (ii) Tick the system bus used by the system clock and by the MAR. (iii) Describe the purpose of the Control Unit.", "Same memory space; PC: address; IX: added to address; SR: flags. Clock on the control bus, MAR on the address bus.",
  "<p><b>(a)</b> " + mks(["Instructions and data are stored in the same memory space (main memory)"]) + "</p><p><b>(b)(i)</b> " + mks(["PC: stores the address of the next instruction to be fetched", "IX: stores a value that is added to an address to give another address", "SR: stores flags set by events, by the results of arithmetic and logic operations, and interrupt flags"], "a") + "</p><p><b>(ii)</b> " + mks(["System clock: control bus; MAR: address bus (both rows for the mark)"]) + "</p><p><b>(iii)</b> Any two: " + mks(["To coordinate or synchronise the actions of other components in the CPU", "To send and receive control signals along the control bus", "To manage the execution of instructions", "To control the communication between the components of the CPU"], "b") + "</p>", "Writing that the PC stores the instruction. It stores the address of the next instruction.") + peq(SRC("w22", "13", "Q4(a)(i)(b)"), "2 + 2 marks", "State / Describe",
  "(a)(i) State the roles of the MAR and the MDR. (b) Describe the purpose of the system clock.", "Address; data. Synchronise, timing signals.",
  "<p><b>(a)(i)</b> " + mks(["MAR: holds the address in memory from which data will be read, or to which data will be written", "MDR: holds the data or instructions that have been read from, or are to be written to, the address in the MAR"]) + "</p><p><b>(b)</b> Any two: " + mks(["To synchronise operations", "by creating timing signals", "To process operations in the correct sequence"], "a") + "</p>", None) + peq(SRC("w23", "11", "Q5(a)(b)"), "4 + 2 marks", "Identify / Describe",
  "The MDR, IX and ACC are examples of special purpose registers. (a) Identify two other special purpose registers and state their role. (b) Describe what is meant by the Immediate Access Store (IAS).", "PC, MAR, CIR, SR. IAS is main memory.",
  "<p><b>(a)</b> One mark for each register and one for its role (max 2 each): " + mks(["Program Counter: stores the address where the next instruction is to be read from", "MAR: stores the address of the memory location currently being read from or written to", "CIR: holds the instruction currently being decoded or executed", "Status Register: contains bits that are set or cleared depending on the operation, for example overflow"]) + "</p><p><b>(b)</b> Any two: " + mks(["The IAS holds all the data, instructions and programs currently in use", "The IAS is volatile memory", "The IAS has fast access times"], "a") + "</p>", None) + peq(SRC("w23", "13", "Q9(a)"), "3 + 2 marks", "Identify",
  "A computer system is designed using the basic Von Neumann model. (i) Identify three other components in the model, not including registers or buses. (ii) Identify two differences between special purpose and general purpose registers.", "CU, ALU, IAS, clock. Role against any purpose.",
  "<p><b>(i)</b> " + mks(["Control unit (CU)", "Arithmetic and Logic Unit (ALU)", "Immediate Access Store (IAS)", "(System clock)"]) + " (any three)</p><p><b>(ii)</b> Any two: " + mks(["Special purpose registers hold the status of a program; general purpose registers hold temporary data during operations", "Special purpose registers are specialised for a specific use; general purpose registers can be used for any purpose", "General purpose registers can be used by most instructions; special purpose only by certain instructions"], "a") + "</p>", None) + peq(SRC("s23", "12", "Q5(a)"), "2 marks", "Identify",
  "A laptop is designed using the Von Neumann model. Identify two types of signal that a control bus can transfer.", "Interrupt, timing, read, write.",
  "<p>" + mks(["Interrupt", "Timing", "Read", "Write"]) + " (any two)</p>", None) + peq(SRC("w24", "11", "Q3(a), Q8"), "2 + 2 + 2 marks", "State / Describe / Identify",
  "(Q3a) State the purpose of the system clock and the Control Unit in a CPU. (Q8a) Describe the purpose of the Status Register. (Q8b) Identify two differences between general purpose and special purpose registers.", "Clock: timing. CU: control signals. SR: flags.",
  "<p><b>Q3(a)</b> " + mks(["System clock: to synchronise operations by creating and transmitting timing signals on the control bus"]) + " " + mks(["CU: sends and receives control signals along the control bus, reads the instruction at the address in the PC, coordinates the other components, manages execution of instructions"], "a") + "</p><p><b>Q8(a)</b> Any two: " + mks(["To store the value of flags or bits", "that can be changed, set or cleared after arithmetic or logical operations", "To allow flags to be checked to change the instruction sequence"], "b") + "</p><p><b>Q8(b)</b> Any two: " + mks(["Special purpose registers have a specified role; general purpose registers can be used for all purposes defined by the programmer", "Special purpose registers hold the state of the program's execution; general purpose registers hold the program's data during operations"], "c") + "</p>", None) + peq(SRC("w24", "12", "Q3(a)"), "4 marks", "Complete",
  "Complete the table by describing the purpose of each register: Program Counter, Memory Address Register, Memory Data Register, Index Register.", "Address of next; address of location; data; number added to operand.",
  "<p>" + mks(["PC: stores the address of the next instruction to be fetched or executed", "MAR: stores the address of the memory location where data will be read from or written to", "MDR: stores the data read from the address in the MAR, or the data to be written to the address in the MAR", "IX: stores a number that will be added to the operand to form the address of the data"]) + "</p>", None) + peq(SRC("s25", "12", "Q1(a)(b)"), "3 + 2 marks", "Complete / Identify",
  "The table has six statements about the Von Neumann model. 1. The PC stores the next instruction to be fetched from memory. 2. The ALU performs mathematical and logical operations. 3. The CU sends signals to other components on the data bus. 4. The MDR transfers data to the memory address stored in the MAR. 5. The MAR stores an address from memory. 6. The ACC stores the result of calculations. Three statements are incorrect: write their numbers and the corrected statements. (b) Identify one other register used in the fetch-execute cycle and describe its role.", "Statements 1, 3 and 4.",
  "<p><b>(a)</b> " + mks(["1: The PC stores the address of the next instruction to be fetched from memory", "3: The CU sends signals to other components on the control bus", "4: The MDR holds the data to be stored in the memory address in the MAR (or holds the data read from that address)"]) + "</p><p><b>(b)</b> " + mks(["Current Instruction Register: stores the instruction to be decoded or executed next", "Status register: contains bits that indicate a state or event", "Interrupt register: stores details of any interrupts that have occurred"], "a") + " (name and role)</p>", "Leaving statement 6 or 2 as incorrect. They are correct.") + peq(SRC("s25", "13", "Q2(a)(i)"), "2 marks", "Explain",
  "The processor has a Control Unit and system clock. Explain how the CU and the system clock work together.", "Clock produces timing signals; CU sends commands on each, using the control bus.",
  "<p>" + mks(["The control unit synchronises the actions of the processor", "by sending a command or signal on each timing signal produced by the system clock", "using or along the control bus"]) + " (max 2)</p>", None) + peq(SRC("w25", "11", "Q6(a)"), "2 marks", "Complete",
  "Complete the table by describing the role of each register: ACC and CIR.", "Intermediate results; instruction being executed.",
  "<p>" + mks(["ACC: stores the intermediate results of arithmetic and logical operations, or the result of a calculation", "CIR: holds the instruction currently being decoded or executed"]) + "</p>", None)

review = req("2 marks", "State", "State the purpose of the ALU.", "Arithmetic and logic.", "<p>" + mks(["To perform arithmetic operations", "and logical operations such as AND, OR and comparisons"]) + "</p>", None) + req("3 marks", "Explain", "A processor has a 24-bit address bus. Calculate the number of memory locations it can address and explain what a wider address bus allows.", "2^24.", "<p>" + mks(["2^24 = 16 777 216 locations", "A wider address bus allows larger addresses to be used", "so more memory locations can be accessed directly"]) + "</p>", None) + req("2 marks", "Explain", "Explain why the data bus is bidirectional and the address bus is not.", "Data goes both ways.", "<p>" + mks(["Data and instructions travel both from memory to the CPU and from the CPU to memory", "Addresses are only sent from the CPU (the MAR) to memory"]) + "</p>", None) + req("2 marks", "Describe", "Describe the stored program concept and one effect of it.", "Same memory.", "<p>" + mks(["Instructions and data are stored in the same memory", "A different program can be loaded to make the computer do a different task"]) + "</p>", None) + req("2 marks", "Identify", "Identify the register that holds the address of the next instruction and the register that holds the instruction being executed.", "PC; CIR.", "<p>" + mks(["Program Counter", "Current Instruction Register"]) + "</p>", None)

tips = tips_html([
  ("PC holds an address.", "Never 'the next instruction'."),
  ("MAR address, MDR data.", "The MDR holds data read from, or to be written to, that address."),
  ("CU uses the control bus.", "Not the data bus."),
  ("Special: one role. General: any role.", "Give the contrast."),
  ("Same memory space.", "The stored program concept in four words."),
  ("2^n for n address lines.", "Wider address bus, more locations."),
], [("a register", "A tiny, very fast store inside the CPU."), ("a bus", "A set of wires carrying signals between components."), ("the IAS", "Main memory: holds the programs and data in use."), ("a flag", "A bit in the status register set by an operation or event.")],
  [("State / Identify", "Short answer."), ("Describe", "Several points."), ("Explain", "Reasons as well."), ("Complete", "Fill in the table.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, w, h, t, on) => SV.rect(x, y, w, h, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + w / 2, y + h / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" });
    let o = SV.rect(20, 20, 330, 160, "cell", { rx: 12, ...op(0.3) }) + SV.text(185, 38, "CPU", "lbl bd", { "text-anchor": "middle" }) + B(40, 55, 100, 40, "ALU", k === 1) + B(40, 115, 100, 40, "CU", k === 2) + B(160, 55, 170, 40, "Registers", k === 3) + B(160, 115, 170, 40, "Clock", k === 4) + B(400, 55, 150, 100, "Main memory (IAS)", k === 5);
    if (k >= 5) o += SV.path("M350,105 H400", "ax"); return o; };
  Lib.stepper($("#stA"), { w: 580, h: 205, label: "Von Neumann model", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "The CPU is connected to main memory by buses.", s: { i: 0 } }, { cap: "The <b>ALU</b> does arithmetic and logic.", s: { i: 1 } }, { cap: "The <b>Control Unit</b> decodes instructions and sends control signals.", s: { i: 2 } }, { cap: "<b>Registers</b> hold data, addresses and instructions inside the CPU.", s: { i: 3 } }, { cap: "The <b>system clock</b> produces timing signals.", s: { i: 4 } }, { cap: "<b>Main memory</b> holds the program and its data, connected by buses.", s: { i: 5 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t) => SV.rect(x, 20, 120, 40, "cell", { rx: 8 }) + SV.text(x + 60, 46, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); let o = B(30, "CPU") + B(450, "Memory");
    const bus = (y, t, on, c) => SV.path(`M150,${y} H450`, "ax", { style: `stroke:${on ? c : "var(--muted)"};stroke-width:${on ? 4 : 1.5}` }) + SV.text(300, y - 6, t, "sm", { "text-anchor": "middle" });
    o += bus(90, "address bus (one way)", k === 1, "var(--accent)") + bus(120, "data bus (both ways)", k === 2, "var(--good)") + bus(150, "control bus (signals)", k === 3, "var(--bad)");
    o += SV.text(300, 185, ["", "MAR sends the address", "MDR carries the data or instruction", "CU and clock send read, write and timing signals", ""][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 200, label: "Buses", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "Three buses connect the CPU to memory.", s: { i: 0 } }, { cap: "The <b>address bus</b> carries the address from the MAR. One way: CPU to memory.", s: { i: 1 } }, { cap: "The <b>data bus</b> carries data and instructions, both ways, via the MDR.", s: { i: 2 } }, { cap: "The <b>control bus</b> carries read, write, timing and interrupt signals.", s: { i: 3 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const cell = (a, t, on) => SV.rect(40, 30 + a * 30, 300, 26, on ? "f3" : "cell", { rx: 4 }) + SV.text(52, 48 + a * 30, t, "sm"); let o = SV.text(190, 20, "Main memory", "lbl bd", { "text-anchor": "middle" }); const rows = [["100  LDM #5", 1], ["101  ADD #3", 1], ["102  STO 200", 1], ["200  data: 0", 0], ["201  data: 0", 0]]; rows.forEach(([t, ins], i) => o += cell(i, t, k >= 1 && (k === 1 ? ins === 1 : k === 2 ? ins === 0 : false)));
    o += SV.text(380, 70, k === 1 ? "instructions" : k === 2 ? "data" : "", "lbl bd t3"); if (k >= 3) o += SV.text(380, 70, "same memory space", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 600, h: 200, label: "Stored program", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "The program and its data are loaded into main memory.", s: { i: 0 } }, { cap: "Locations 100 to 102 hold <b>instructions</b>.", s: { i: 1 } }, { cap: "Locations 200 and 201 hold <b>data</b>.", s: { i: 2 } }, { cap: "Both are in the <b>same memory space</b>: the stored program concept.", s: { i: 3 } }] });
})();

(function () {
  let n = 16; const paint = () => { const loc = 2 ** n; const t = loc >= 2 ** 40 ? (loc / 2 ** 40) + " TiB" : loc >= 2 ** 30 ? (loc / 2 ** 30) + " GiB" : loc >= 2 ** 20 ? (loc / 2 ** 20) + " MiB" : loc >= 2 ** 10 ? (loc / 2 ** 10) + " KiB" : loc + " bytes";
    $("#aV").innerHTML = `<b>${n}</b> address lines can address 2<sup>${n}</sup> = <b>${loc.toLocaleString()}</b> locations. If each holds one byte, that is <b>${t}</b>. One more line doubles the number of locations.`; };
  Lib.slider($("#aS"), { id: "a1", label: "Address lines ", min: 8, max: 40, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();
btnTable("rB", "rO", [
  ["Holds the address of the next instruction", "Program Counter (PC)", "Special purpose"],
  ["Holds the address being read or written", "Memory Address Register (MAR)", "Special purpose"],
  ["Holds data read from, or to be written to, memory", "Memory Data Register (MDR)", "Special purpose"],
  ["Holds the instruction being decoded", "Current Instruction Register (CIR)", "Special purpose"],
  ["Holds flags from arithmetic and logic", "Status Register (SR)", "Special purpose"],
  ["Holds intermediate results of calculations", "Accumulator (ACC)", "General purpose"]
], ["Role", "Register", "Type"]);
btnTable("bB", "bO", [
  ["The address in the MAR", "Address bus", "One way, CPU to memory"],
  ["An instruction fetched from memory", "Data bus", "Both ways"],
  ["A timing signal from the system clock", "Control bus", "Synchronises operations"],
  ["A read signal", "Control bus", "Tells memory to send data"],
  ["An interrupt signal", "Control bus", "A signal, not data"]
], ["Signal", "Bus", "Why"]);
''' + _prjs

finish("as-4-1-1-von-neumann-registers-buses", "as411", "Von Neumann Model, Registers and Buses",
  "The Von Neumann model, the stored program concept, special and general purpose registers and the address, data and control buses, with animations, a bus-width lab and the real Paper 1 questions from 2021 to 2026.",
  "4.1.1", "4 · Processor fundamentals", "section 4.1 Central Processing Unit architecture", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on the Von Neumann model, registers and buses (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
