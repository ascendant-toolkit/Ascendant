"""AS CS 4.2.2: addressing modes and tracing assembly programs. Run: python3 tools/artifact-kit/mk_as422.py"""
from ak42 import *

def accs(prog_lines, mem, acc=0, ix=0):
    prog = {i: l for i, l in enumerate(prog_lines)}
    _, st = run(prog, mem, acc=acc, ix=ix)
    return st["acc"], st["ix"]

def chk(lines, mem, exp, acc=0, ix=0, tag=""):
    a, i = accs(lines, mem, acc, ix)
    assert a == exp, f"{tag}: {a} != {exp}"
    return a, i

# ---- exam checks (each answer is checked against the published mark scheme)
M24a = {19: 24, 20: 2, 21: 1, 22: 3, 23: 5, 24: 4, 25: 22}
chk(["LDD 20", "ADD #2"], M24a, 4, 12, 1, "s24 11 P1"); chk(["LDX 22"], M24a, 5, 12, 1, "s24 11 P2")
chk(["LDI 25", "INC ACC", "SUB 22"], M24a, 1, 12, 1, "s24 11 P3"); chk(["LDD 19", "LDM #5", "LDM #25"], M24a, 25, 12, 1, "s24 11 P4")
M24b = {10: 1, 11: 3, 12: 5, 13: 11, 14: 10, 15: 16, 16: 12}
chk(["LDI 15", "SUB #1"], M24b, 11, 10, 0, "s24 12 P1"); chk(["LDD 14", "ADD 11"], M24b, 13, 10, 0, "s24 12 P2")
chk(["LDM #11", "ADD #3", "SUB 16"], M24b, 2, 10, 0, "s24 12 P3"); a, i = chk(["LDR #2", "LDX 14", "ADD #2"], M24b, 14, 10, 0, "s24 12 P4")
M24c = {48: 51, 49: 6, 50: 48, 51: 50, 52: 49, 53: 50, 54: 6}
chk(["LDM #50", "INC ACC", "SUB #1"], M24c, 50, 2, 50, "s24 13 P1"); chk(["LDI 51", "ADD 52"], M24c, 97, 2, 50, "s24 13 P2")
chk(["LDR #2", "LDX 50", "DEC ACC"], M24c, 48, 2, 50, "s24 13 P3"); P4_24c, _ = accs(["LDD 52", "SUB 54", "INC ACC"], M24c, 2, 50)
M24d = {19: 25, 20: 23, 21: 2, 22: 4, 23: 15, 24: 50, 25: 22}
chk(["LDM #19", "DEC ACC"], M24d, 18, 50, 20, "w24 12 P1"); chk(["LDD 23", "ADD 19"], M24d, 40, 50, 20, "w24 12 P2")
chk(["LDI 25", "INC ACC"], M24d, 5, 50, 20, "w24 12 P3"); a, ix4 = chk(["LDR #21", "LDX 2"], M24d, 15, 50, 20, "w24 12 P4"); assert ix4 == 21
M24e = {50: 54, 51: 55, 52: 50, 53: 52, 54: 100, 55: 25, 56: 50}
chk(["LDD 50", "ADD #4", "ADD 54"], M24e, 158, 50, 45, "w24 13 P1"); chk(["LDI 53", "DEC ACC", "ADD 56"], M24e, 99, 50, 45, "w24 13 P2"); chk(["LDM #55", "SUB #5"], M24e, 50, 50, 45, "w24 13 P3")
M25 = {98: 8, 99: 16, 100: 3, 101: 98, 102: 32}
chk(["LDM #98"], M25, 98, 0, 2, "w25 12 a"); chk(["LDI 101"], M25, 8, 0, 2, "w25 12 b"); chk(["LDX 100"], M25, 32, 0, 2, "w25 12 c")
M22 = {100: 101, 101: 67, 102: 104, 103: 100, 104: 68}
chk(["LDM #103"], M22, 103, 0, 0, "s22 13 a"); chk(["LDD 102"], M22, 104, 0, 0, "s22 13 b"); chk(["LDI 103"], M22, 101, 0, 0, "s22 13 c")
M26 = {100: 200, 101: 205, 102: 100, 103: 50, 200: 101, 201: 100, 202: 20, 203: 13, 204: 220, 205: 30}
chk(["ADD B00000010", "INC ACC"], M26, 0b11001101, 0b11001010, 0, "s26 a1"); chk(["LDM #200", "ADD 200"], M26, 301, 100, 0, "s26 a2"); chk(["LDD 103", "DEC ACC", "DEC ACC"], M26, 48, 103, 0, "s26 a3")

# ---- traces
P21 = {200: "LDD 365", 201: "CMP 366", 202: "JPE 209", 203: "INC ACC", 204: "STO 365", 205: "MOV IX", 206: "LDX 365", 207: "OUT", 208: "JMP 200", 209: "END"}
M21 = {365: 1, 366: 3, 367: 65, 368: 66}
R21, S21 = run(P21, M21, ix=0); assert [r["out"] for r in R21 if r["out"]] == ["A", "B"]
T21 = trace_html(R21, M21, [365, 366, 367, 368], acc0=None, ix0=0, show_out=True)
P25 = {200: "LDD 81", 201: "INC ACC", 202: "STO 83", 203: "LDI 82", 204: "CMP 83", 205: "JPE 209", 206: "LDD 83", 207: "ADD #10", 208: "JMP 210", 209: "DEC ACC", 210: "STO 81", 211: "END"}
M25b = {80: 10, 81: 8, 82: 80, 83: 81}
R25, S25 = run(P25, M25b); assert S25["mem"][81] == 19
T25 = trace_html(R25, M25b, [80, 81, 82, 83], acc0=None, show_ix=False)

def prog_table(lines):
    return '<div class="tw"><table class="t mono">' + "".join(f"<tr><td>{a}</td><td>{l}</td></tr>" for a, l in lines) + "</table></div>"

def mem_table(mem):
    return '<div class="tw"><table class="t mono"><tr><th>Address</th><th>Data</th></tr>' + "".join(f"<tr><td>{a}</td><td>{d}</td></tr>" for a, d in mem.items()) + "</table></div>"

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>The <b>addressing mode</b> says how the processor finds the data an instruction uses. With <b>immediate</b> addressing the operand <em>is</em> the data (LDM #5); with <b>direct</b> addressing the operand is the address of the data (LDD 100); with <b>indirect</b> addressing the operand is the address of a location that holds the address of the data (LDI 100); with <b>indexed</b> addressing the address is the operand plus the contents of the index register IX (LDX 100); with <b>relative</b> addressing the operand is an offset from the address of the current instruction. Exam questions give a memory table and ask for the ACC after a few instructions, or ask you to <b>trace</b> a program in a table. Work one instruction at a time and write down exactly which address you used. Every trace row needs the value of the ACC or the memory location that changed.</p></div>

  <h2>1 · The addressing modes</h2>
  <div class="tw"><table class="t">
    <tr><th>Mode</th><th>Example</th><th>How the data is found</th></tr>
    <tr><td><b>Immediate</b></td><td class="mono">LDM #5</td><td>The operand is the number itself: ACC ← 5</td></tr>
    <tr><td><b>Direct</b></td><td class="mono">LDD 100</td><td>The operand is the address of the data: ACC ← contents of 100</td></tr>
    <tr><td><b>Indirect</b></td><td class="mono">LDI 100</td><td>The address to be used is at the given address: the contents of 100 are an address, and ACC ← the contents of <em>that</em> address</td></tr>
    <tr><td><b>Indexed</b></td><td class="mono">LDX 100</td><td>Form the address from the operand + the contents of IX: ACC ← contents of (100 + IX)</td></tr>
    <tr><td><b>Relative</b></td><td class="mono">JMP +3</td><td>The address is an offset number of locations away, relative to the address of the current instruction</td></tr>
  </table></div>
  <p>Worked example with memory 100: 101, 101: 67, 102: 104, 103: 100, 104: 68. <span class="mono">LDM #103</span> gives 103. <span class="mono">LDD 102</span> gives the contents of 102: 104. <span class="mono">LDI 103</span>: location 103 holds 100, so the address used is 100, which holds 101: ACC = 101.</p>
  <p><b>Similarity between direct and indexed:</b> both load the contents of an address into the accumulator. <b>Difference:</b> direct uses the address in the operand; indexed adds the contents of IX to the operand and uses the data at that calculated address.</p>

  <h2>2 · Tracing a program</h2>
  <ol>
    <li>List the instructions in address order, and the starting contents of memory, ACC and IX.</li>
    <li>Execute one instruction at a time, starting at the first. Write the instruction's address in the first column.</li>
    <li>Record the new ACC, the memory location or IX that changes, and any output on that row.</li>
    <li>For <b>CMP</b> compare the ACC with the operand; <b>JPE</b> jumps only if equal, <b>JPN</b> only if not equal; otherwise carry on with the next instruction. <b>END</b> stops.</li>
    <li>Check the jumps: a loop traces the same instruction addresses again with new values.</li>
  </ol>
  <p>The Cambridge instruction set also includes <span class="mono">SUB</span>, <span class="mono">DEC</span>, <span class="mono">IN</span>, <span class="mono">OUT</span> (outputs the ASCII character for the ACC value), <span class="mono">MOV IX</span> and <span class="mono">LDR #n</span> (loads IX). The table is printed on the paper.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Using the operand of LDI as the data. Look it up twice: first the address, then the data.</li>
    <li>Forgetting to add IX for LDX.</li>
    <li>Writing the wrong address in the first column when a jump is taken.</li>
    <li>Recording a value in memory when the instruction only changes the ACC.</li>
    <li>Treating CMP as changing the ACC. It only compares.</li>
  </ul>
'''

watch = '''
  <h2>1 · Four addressing modes, one memory</h2>
  <div id="stA"></div>
  <h2>2 · Indexed addressing</h2>
  <div id="stB"></div>
  <h2>3 · Tracing one loop</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Addressing modes</h2>
  <p>Memory is 100: 101, 101: 67, 102: 104, 103: 100, 104: 68. Choose a mode and an operand.</p>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mS"></div><div id="mV" class="verdict"></div></div>
  <h2>Lab 2 · Trace a program</h2>
  <p>Press Step to execute one instruction. Changed cells are highlighted.</p>
  <div class="card"><div class="btnrow"><button id="tr_step">Step</button><button id="tr_reset">Reset</button></div><div id="trT"></div></div>
  <h2>Lab 3 · Which mode?</h2>
  <div class="card"><div id="wB" class="btnrow"></div><div id="wO"></div></div>
'''

_pr, _prjs = PR(["Which addressing mode?", "Which instruction loads which value?", "Match the mode to its description", "Put the LDI steps in order", "Working out", "Multiple choice"],
  ("Which addressing mode is it?", ["Immediate", "Direct", "Indirect", "Indexed"], [("LDM #7", 0), ("LDD 100", 1), ("LDI 100", 2), ("LDX 100", 3), ("The operand is the data itself", 0), ("The address is the operand plus the index register", 3)], "Immediate: data. Direct: address. Indirect: address of address. Indexed: plus IX."),
  ("With memory 100: 101, 101: 67, 102: 104, 103: 100, 104: 68 what does it load into the ACC?", ["101", "104", "68"], [("LDI 103", 0), ("LDD 102", 1), ("LDD 104", 2), ("LDI 102", 2), ("LDM #101", 0), ("LDD 100", 0)], "LDI 103: 103 holds 100, 100 holds 101. LDI 102: 102 holds 104, 104 holds 68."),
  [["Immediate", "The operand is the number to use"], ["Direct", "The operand is the address of the data"], ["Indirect", "The operand is the address of the address"], ["Indexed", "Operand plus contents of IX gives the address"], ["Relative", "Offset from the current instruction address"]],
  ("Put the steps of LDI 103 in order.", ["Read the operand 103", "Read the contents of address 103", "Use that value as an address", "Read the contents of that second address", "Place the value in the ACC"], "Operand, contents, as address, contents, ACC."),
  [{"q": "IX = 2. What address does LDX 100 use?", "a": 102, "unit": "", "tol": 0.01, "hint": "100 + 2.", "sol": "<b>102</b>."}, {"q": "Memory 50 holds 70 and 70 holds 9. What does LDI 50 put in the ACC?", "a": 9, "unit": "", "tol": 0.01, "hint": "50 → 70 → 9.", "sol": "<b>9</b>."}, {"q": "ACC = 5 and memory 200 holds 6. What is the ACC after ADD 200?", "a": 11, "unit": "", "tol": 0.01, "hint": "5 + 6.", "sol": "<b>11</b>."}, {"q": "ACC = 10 after LDM #10. What is ACC after INC ACC then SUB #3?", "a": 8, "unit": "", "tol": 0.01, "hint": "10 + 1 − 3.", "sol": "<b>8</b>."}, {"q": "The ASCII code for A is 65. What is the ASCII code of the character output by OUT when ACC = 67?", "a": 67, "unit": "", "tol": 0.01, "hint": "67 outputs C.", "sol": "<b>67</b> (the character C)."}],
  [("LDM #5 uses:", ["Immediate addressing", "Direct addressing", "Indirect addressing", "Indexed addressing"], 0, "Immediate."), ("LDX needs:", ["The index register", "A stack", "A queue", "A label only"], 0, "IX."), ("CMP:", ["Compares ACC with a value", "Loads ACC", "Jumps", "Stores"], 0, "Compares."), ("JPE jumps when:", ["The compare was true", "The compare was false", "Always", "Never"], 0, "True."), ("LDI uses:", ["An address stored in another location", "The number given", "The PC", "IX only"], 0, "Address of address."), ("INC IX:", ["Adds 1 to the index register", "Adds 1 to ACC", "Clears IX", "Loads IX"], 0, "IX + 1.")],
  [("Immediate", "Operand is the data: LDM #5."), ("Direct", "Operand is the address: LDD 100."), ("Indirect", "Address of the address: LDI 100."), ("Indexed", "Operand + IX: LDX 100."), ("Relative", "Offset from the current instruction."), ("CMP", "Compare only; JPE/JPN use the result."), ("OUT", "Outputs the ASCII character in ACC."), ("Trace", "One row per instruction; record changes.")])

real = RWNOTE + (
rw("An array in a program", "Indexed addressing is how a loop moves through array elements: the base address stays in the instruction and IX moves along by one each time.", "LDX with INC IX.") +
rw("A pointer to a record", "A pointer holds the address of the data, not the data. Following it is indirect addressing.", "indirect addressing.") +
rw("A program that moves in memory", "Relative addressing lets code jump 'three instructions back' wherever it is loaded, so it still works if the program is moved.", "relative addressing.") +
rw("Debugging with a trace", "Writing down every register after each instruction is how you find where a value goes wrong.", "tracing.") +
rw("A constant in a program", "Typing a number like #5 directly into the instruction is immediate addressing: no memory lookup is needed.", "immediate addressing.")
)

where = [
  ("M/J 2021", "11, 13", "3(b)", "6", "Trace a program that loops using LDD, CMP, JPE, INC, STO, MOV IX, LDX, OUT, JMP"),
  ("O/N 2021", "12", "8(b)(iii)", "2", "Identify one other mode of addressing and describe it"),
  ("M/J 2022", "13", "3(a)", "3", "The ACC after LDM, LDD and LDI"),
  ("O/N 2023", "11", "8(b)(ii), (iii)", "2 + 1", "A similarity and a difference between direct and indexed addressing; another mode"),
  ("M/J 2024", "11", "4(a)", "4", "The ACC after four programs"),
  ("M/J 2024", "12", "5(a)", "4", "The ACC after four programs"),
  ("M/J 2024", "13", "3(a)", "4", "The ACC after four programs"),
  ("O/N 2024", "12", "8(a)", "5", "The ACC and IX after four sets of instructions"),
  ("O/N 2024", "13", "7(a)", "3", "The ACC after three programs"),
  ("M/J 2025", "11", "8(a)", "4", "Trace a program with LDI, CMP, JPE, STO"),
  ("O/N 2025", "12", "3(a), (b)", "1 + 2 + 3", "Describe relative addressing; two registers; the ACC after LDM, LDI and LDX"),
  ("M/J 2026", "11", "3(a), (c)", "3 + 3", "The ACC after instructions; identify and describe another mode of addressing")]

past = '''  <p class="note">The "ACC after each program" question has appeared in every series since 2024 with a new memory table. The trace table with a loop is the harder form. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording. Where the paper prints a trace table, the table here shows every instruction executed; only the cells that change are filled in.</p>
''' + peq(SRC("s21", "11/13", "Q3(b)"), "6 marks", "Complete",
  "A processor has an Accumulator (ACC) and an Index Register (IX). Memory: 200 LDD 365, 201 CMP 366, 202 JPE 209, 203 INC ACC, 204 STO 365, 205 MOV IX, 206 LDX 365, 207 OUT, 208 JMP 200, 209 END; 365: 1, 366: 3, 367: 65, 368: 66; IX = 0. ASCII: 65 A, 66 B, 67 C, 68 D. Complete the trace table for the program currently in main memory.", "LDD loads 1, CMP with 3 fails. INC makes 2, STO puts it in 365. MOV IX copies ACC. LDX 365 uses address 365 + IX.",
  "<p>One mark for each shaded set of values (the table has the whole loop):</p>" + T21 + "<p>" + mks(["ACC = 1 on the first pass, memory 365 = 2, IX = 2", "ACC = 65 from LDX 365 (address 367), output A", "Second pass: ACC = 2 then 3, 365 = 3, IX = 3, ACC = 66 (address 368), output B", "Third pass: CMP 366 equal (3 = 3) so JPE 209 jumps to END"]) + "</p>", "Using 365 alone for LDX. The address used is 365 + IX, which is 367 then 368.") + peq(SRC("w21", "12", "Q8(b)(iii)"), "2 marks", "Identify",
  "Identify one other mode of addressing (not immediate, direct or indexed) and describe how it works.", "Indirect or relative.",
  "<p>" + mks(["Indirect addressing: the address to be used is at the given address", "Relative addressing: the address to be used is an offset number of locations away, relative to the address of the current instruction"]) + " (name and description; any one mode)</p>", None) + peq(SRC("s22", "13", "Q3(a)"), "3 marks", "Complete",
  "Main memory: 100: 101, 101: 67, 102: 104, 103: 100, 104: 68. Write the value stored in the accumulator after each instruction: LDM #103; LDD 102; LDI 103.", "103; the contents of 102; the contents of the address that is in 103.",
  "<p>" + mks(["LDM #103: 103", "LDD 102: 104", "LDI 103: 101"]) + "</p>" + mem_table(M22), "For LDI 103 answering 100. 100 is the address; the data at 100 is 101.") + peq(SRC("w23", "11", "Q8(b)(ii)(iii)"), "2 + 1 marks", "Give / Identify",
  "The instruction LDR #2 uses immediate addressing. Give one similarity and one difference between direct addressing and indexed addressing. Identify one other mode of addressing.", "Both load contents of an address. Direct uses the operand; indexed adds IX.",
  "<p>" + mks(["Similarity: both load the contents of an address into the Accumulator", "Difference: direct accesses the address given by the operand, whereas indexed adds the contents of IX to the operand and accesses the data at that calculated address"]) + "</p><p>" + mks(["Indirect or relative addressing"], "a") + "</p>", None) + peq(SRC("s24", "11", "Q4(a)"), "4 marks", "Complete",
  "Memory: 19: 24, 20: 2, 21: 1, 22: 3, 23: 5, 24: 4, 25: 22. ACC = 12, IX = 1. Write the ACC after each program: (1) LDD 20, ADD #2; (2) LDX 22; (3) LDI 25, INC ACC, SUB 22; (4) LDD 19, LDM #5, LDM #25.", "LDX 22 uses address 22 + 1 = 23.",
  "<p>" + mks(["1: 4", "2: 5", "3: 1", "4: 25"]) + "</p>" + mem_table(M24a), None) + peq(SRC("s24", "12", "Q5(a)"), "4 marks", "Complete",
  "Memory: 10: 1, 11: 3, 12: 5, 13: 11, 14: 10, 15: 16, 16: 12. ACC = 10, IX = 0. Write the ACC after each program: (1) LDI 15, SUB #1; (2) LDD 14, ADD 11; (3) LDM #11, ADD #3, SUB 16; (4) LDR #2, LDX 14, ADD #2.", "LDI 15: location 15 holds 16; location 16 holds 12.",
  "<p>" + mks(["1: 11", "2: 13", "3: 2", "4: 14"]) + "</p>" + mem_table(M24b), None) + peq(SRC("s24", "13", "Q3(a)"), "4 marks", "Complete",
  "Memory: 48: 51, 49: 6, 50: 48, 51: 50, 52: 49, 53: 50, 54: 6. ACC = 2, IX = 50. Write the ACC after each program: (1) LDM #50, INC ACC, SUB #1; (2) LDI 51, ADD 52; (3) LDR #2, LDX 50, DEC ACC; (4) LDD 52, SUB 54, INC ACC.", "LDX 50 with IX = 2 uses address 52.",
  "<p>" + mks(["1: 50", "2: 97", "3: 48", f"4: {P4_24c}"]) + "</p>" + mem_table(M24c), None) + peq(SRC("w24", "12", "Q8(a)"), "5 marks", "Complete",
  "Memory: 19: 25, 20: 23, 21: 2, 22: 4, 23: 15, 24: 50, 25: 22. ACC = 50, IX = 20. Write the ACC and IX after each set: (1) LDM #19, DEC ACC; (2) LDD 23, ADD 19; (3) LDI 25, INC ACC; (4) LDR #21, LDX 2.", "LDR changes IX. LDX 2 uses address 2 + 21 = 23.",
  "<p>" + mks(["1: ACC 18", "2: ACC 40", "3: ACC 5", "4: ACC 15", "IX column: 20, 20, 20, 21"]) + "</p>" + mem_table(M24d), "Forgetting that LDR #21 changes IX for the next instruction.") + peq(SRC("w24", "13", "Q7(a)"), "3 marks", "Complete",
  "Memory: 50: 54, 51: 55, 52: 50, 53: 52, 54: 100, 55: 25, 56: 50. ACC = 50, IX = 45. Write the ACC after each program: (1) LDD 50, ADD #4, ADD 54; (2) LDI 53, DEC ACC, ADD 56; (3) LDM #55, SUB #5.", "LDD 50 loads 54; ADD 54 adds the contents of 54, which is 100.",
  "<p>" + mks(["1: 158", "2: 99", "3: 50"]) + "</p>" + mem_table(M24e), None) + peq(SRC("s25", "11", "Q8(a)"), "4 marks", "Trace",
  "Memory: 80: 10, 81: 8, 82: 80, 83: 81; 200 LDD 81, 201 INC ACC, 202 STO 83, 203 LDI 82, 204 CMP 83, 205 JPE 209, 206 LDD 83, 207 ADD #10, 208 JMP 210, 209 DEC ACC, 210 STO 81, 211 END. Trace the program currently in memory.", "LDI 82: location 82 holds 80, location 80 holds 10. CMP 10 with 9 is not equal, so JPE does not jump.",
  "<p>One mark for each shaded section: " + mks(["ACC 8 after LDD 81", "ACC 9 and location 83 = 9 after INC and STO", "ACC 10 after LDI 82; CMP not equal, no jump; ACC 9 after LDD 83", "ACC 19 after ADD #10; location 81 = 19 after STO 81"]) + "</p>" + T25, None) + peq(SRC("w25", "12", "Q3(a)(b)"), "1 + 2 + 3 marks", "State / Identify / Write",
  "(i) State what is meant by relative addressing. (ii) Identify two registers used in the fetch-execute cycle. (b) Memory: 98: 8, 99: 16, 100: 3, 101: 98, 102: 32; IX = 2. Write the contents of the ACC after LDM #98, then LDI 101, then LDX 100.", "Offset added to a base address. 98; 8; 32.",
  "<p><b>(i)</b> " + mks(["The operand is an offset value which is added to another base value to give the address from which the contents are loaded to the accumulator"]) + "</p><p><b>(ii)</b> Any two: " + mks(["PC", "MDR", "MAR", "CIR", "Status register"], "a") + "</p><p><b>(b)</b> " + mks(["LDM #98: 98", "LDI 101: 8", "LDX 100: 32"], "b") + "</p>" + mem_table(M25), None) + peq(SRC("s26", "11", "Q3(a)(c)"), "3 + 3 marks", "Complete / Identify",
  "Memory: 100: 200, 101: 205, 102: 100, 103: 50, 200: 101, 201: 100, 202: 20, 203: 13, 204: 220, 205: 30. Complete the table of new ACC data: ACC = B11001010 after ADD B00000010, INC ACC; ACC = #100 after LDM #200, ADD 200; ACC = #103 after LDD 103, DEC ACC, DEC ACC. (c) Immediate, relative and direct are three modes of addressing. Identify and describe one additional mode, with an example instruction.", "Add in binary; LDM replaces; LDD 103 loads 50.",
  "<p><b>(a)</b> " + mks(["B11001101", "#301", "#48"]) + "</p><p><b>(c)</b> " + mks(["Indirect: the operand stores the address where the data is found, e.g. LDI 23 loads the data in the address stored in address 23", "Indexed: the address is calculated by adding the operand to the contents of the index register, e.g. LDX 20"]) + " (name, description and example; any one mode)</p>", "Naming immediate, relative or direct: the question asks for an additional mode.")

review = req("3 marks", "Complete", "Memory 40: 7, 41: 3, 42: 41. ACC = 0. Write the ACC after: (1) LDD 40, ADD 41; (2) LDI 42, INC ACC.", "LDI 42: 42 holds 41, 41 holds 3.", "<p>" + mks(["1: 10", "2: 4"]) + "</p>", None) + req("2 marks", "State", "State how indexed addressing finds the address used by LDX 30 when IX holds 5.", "30 + 5.", "<p>" + mks(["The address is the operand plus the contents of IX", "30 + 5 = 35"]) + "</p>", None) + req("3 marks", "Trace", "A program: 100 LDM #0, 101 INC ACC, 102 CMP #3, 103 JPN 101, 104 END. State the ACC at each CMP and how many times the loop body runs.", "Count up to 3.", "<p>" + mks(["ACC at the CMP: 1, 2, 3", "The loop body runs 3 times", "The program then ends with ACC = 3"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between direct and indirect addressing.", "Address against address of address.", "<p>" + mks(["Direct: the operand is the address of the data", "Indirect: the operand is the address of a location that holds the address of the data"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a loop that works through an array is easier with indexed addressing.", "Move IX.", "<p>" + mks(["The base address is fixed in the instruction", "and IX is incremented each time to reach the next element"]) + "</p>", None)

tips = tips_html([
  ("LDM: data. LDD: address. LDI: address of address.", "Say it in that order."),
  ("LDX: operand plus IX.", "Show the sum."),
  ("Trace one instruction per row.", "Write the instruction address first."),
  ("CMP never changes ACC.", "It sets what JPE and JPN test."),
  ("Check memory after STO.", "It changes the location, not the ACC."),
  ("Loops repeat addresses.", "Rows return to the earlier instruction address."),
], [("immediate addressing", "The operand is the data."), ("direct addressing", "The operand is the address of the data."), ("indirect addressing", "The operand is the address of the address."), ("indexed addressing", "Operand plus IX forms the address.")],
  [("Complete", "Fill in the values."), ("Trace", "Complete the trace table."), ("Identify", "Name the mode or register."), ("Describe", "Several points.")]) + FC

js = AKJS + AK20JS + r'''
function asmVal(t) { t = t.trim(); if (t[0] === "#") return +t.slice(1); if (t[0] === "B") return parseInt(t.slice(1), 2); if (t[0] === "&") return parseInt(t.slice(1), 16); return null; }
function asmRun(prog, mem, acc, ix, maxs) {
  const keys = Object.keys(prog).map(Number).sort((a, b) => a - b); let pc = keys[0], m = Object.assign({}, mem), flag = false, rows = [];
  for (let n = 0; n < (maxs || 200); n++) {
    const ins = prog[pc], sp = ins.split(" "), op = sp[0], a = sp[1]; let nxt = keys[keys.indexOf(pc) + 1]; const imm = a ? asmVal(a) : null; let out = "";
    const rd = () => m[+a];
    if (op === "LDM") acc = imm; else if (op === "LDD") acc = rd(); else if (op === "LDI") acc = m[m[+a]]; else if (op === "LDX") acc = m[+a + ix]; else if (op === "LDR") ix = imm; else if (op === "MOV") ix = acc;
    else if (op === "STO") m[+a] = acc; else if (op === "ADD") acc += imm !== null ? imm : rd(); else if (op === "SUB") acc -= imm !== null ? imm : rd(); else if (op === "INC") { a === "IX" ? ix++ : acc++; } else if (op === "DEC") { a === "IX" ? ix-- : acc--; }
    else if (op === "CMP") flag = acc === (imm !== null ? imm : rd()); else if (op === "JPE") { if (flag) nxt = +a; } else if (op === "JPN") { if (!flag) nxt = +a; } else if (op === "JMP") nxt = +a;
    else if (op === "OUT") out = String.fromCharCode(acc); else if (op === "END") nxt = undefined;
    rows.push({ addr: pc, ins, acc, ix, mem: Object.assign({}, m), out });
    if (nxt === undefined) break; pc = nxt;
  }
  return rows;
}
(function () {
  const draw = (s) => { const k = Math.round(s.i); const mem = [[100, 101], [101, 67], [102, 104], [103, 100], [104, 68]]; const hot = { 1: [], 2: [102], 3: [103], 4: [103, 100] }[k] || []; let o = "";
    mem.forEach(([a, d], i) => { o += SV.rect(30, 20 + i * 30, 160, 26, hot.includes(a) ? (k === 4 && a === 100 ? "f3" : "f1") : "cell", { rx: 4 }) + SV.text(40, 38 + i * 30, a + "   " + d, "lbl"); });
    o += SV.text(240, 80, ["", "ACC = 103", "ACC = 104", "address 103 holds 100", "ACC = 101"][k], "lbl bd t3"); return o; };
  Lib.stepper($("#stA"), { w: 500, h: 190, label: "Addressing", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "Main memory, with data in 100 to 104.", s: { i: 0 } }, { cap: "<b>LDM #103</b>: <b>immediate</b>, the operand is the data. ACC = 103.", s: { i: 1 } }, { cap: "<b>LDD 102</b>: <b>direct</b>, the contents of address 102 are 104. ACC = 104.", s: { i: 2 } }, { cap: "<b>LDI 103</b>: <b>indirect</b>, address 103 holds 100, so use address 100.", s: { i: 3 } }, { cap: "Address 100 holds 101. ACC = <b>101</b>.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 20, 130, 40, "cell", { rx: 6 }) + SV.text(85, 45, "LDX 100", "lbl bd", { "text-anchor": "middle" }) + SV.rect(200, 20, 100, 40, k >= 1 ? "f3" : "cell", { rx: 6 }) + SV.text(250, 45, "IX = 2", "lbl bd", { "text-anchor": "middle" });
    if (k >= 2) o += SV.rect(350, 20, 180, 40, "f1", { rx: 6 }) + SV.text(440, 45, "100 + 2 = 102", "lbl bd", { "text-anchor": "middle" }); if (k >= 3) o += SV.rect(350, 80, 180, 40, "f2", { rx: 6 }) + SV.text(440, 105, "ACC ← contents of 102", "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 560, h: 140, label: "Indexed addressing", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "<b>LDX 100</b>: indexed addressing.", s: { i: 0 } }, { cap: "The index register IX holds 2.", s: { i: 1 } }, { cap: "The address is the operand plus IX: <b>102</b>.", s: { i: 2 } }, { cap: "The contents of address 102 are loaded into the ACC.", s: { i: 3 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const accs = [1, 1, 1, 2, 2, 2, 2]; const mem = [1, 1, 1, 1, 2, 2, 2]; let o = SV.text(20, 20, "Loop: LDD 365, CMP 366, JPE 209, INC ACC, STO 365, ...", "sm"); ["ACC", "mem 365"].forEach((n, r) => { o += SV.rect(30, 40 + r * 44, 130, 34, "cell", { rx: 6 }) + SV.text(95, 62 + r * 44, n + " = " + (r ? mem[k] : accs[k]), "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); });
    o += SV.text(220, 90, ["start: ACC = 1 from LDD 365", "CMP 366: 1 ≠ 3, JPE does not jump", "go on to INC ACC", "INC ACC: ACC = 2", "STO 365: location 365 = 2", "MOV IX: IX = 2, LDX 365 uses 367", "JMP 200: the loop runs again"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 130, label: "Trace", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [0, 1, 2, 3, 4, 5, 6].map((i) => ({ cap: ["Memory 365 holds 1, 366 holds 3.", "CMP compares ACC (1) with 3: not equal.", "JPE is not taken: the next instruction runs.", "INC ACC adds 1.", "STO puts the ACC in 365.", "The index register becomes 2, so LDX 365 will load from 367 (the letter A).", "JMP 200 sends the program back to the start."][i], s: { i } })) });
})();

(function () {
  const M = { 100: 101, 101: 67, 102: 104, 103: 100, 104: 68 }; let mode = "LDM", opd = 103, ix = 2;
  const paint = () => { let addr = null, data, how; if (mode === "LDM") { data = opd; how = `Immediate: the operand ${opd} is the data.`; } else if (mode === "LDD") { addr = opd; data = M[addr]; how = data === undefined ? `Direct: address ${addr}.` : `Direct: address ${addr} holds ${data}.`; } else if (mode === "LDI") { const a1 = M[opd]; addr = a1; data = M[a1]; how = `Indirect: address ${opd} holds ${a1}, an address` + (data === undefined ? "." : `; address ${a1} holds ${data}.`); } else { addr = opd + ix; data = M[addr]; how = `Indexed: ${opd} + IX (${ix}) = ${addr}` + (data === undefined ? "." : `; address ${addr} holds ${data}.`); }
    $("#mV").innerHTML = `<b>${mode} ${mode === "LDM" ? "#" : ""}${opd}</b>: ` + how + (data === undefined ? " That address is not in this memory table." : ` ACC = <b>${data}</b>.`); };
  const bar = $("#mB"); ["LDM", "LDD", "LDI", "LDX"].forEach((m) => { const b = document.createElement("button"); b.textContent = m; b.onclick = () => { mode = m; bar.querySelectorAll("button").forEach((x) => x.className = x === b ? "on" : ""); paint(); }; if (m === "LDM") b.className = "on"; bar.appendChild(b); });
  Lib.slider($("#mS"), { id: "m1", label: "Operand ", min: 98, max: 104, value: opd, fmt: (x) => x, onInput: (v) => { opd = v; paint(); } }); paint();
})();
(function () {
  const prog = { 200: "LDD 365", 201: "CMP 366", 202: "JPE 209", 203: "INC ACC", 204: "STO 365", 205: "MOV IX", 206: "LDX 365", 207: "OUT", 208: "JMP 200", 209: "END" }, mem0 = { 365: 1, 366: 3, 367: 65, 368: 66 };
  let rows, k;
  const reset = () => { rows = asmRun(prog, mem0, 0, 0); k = 0; paint(); };
  const paint = () => { let h = '<div class="tw"><table class="t mono"><tr><th>Address</th><th>Instruction</th><th>ACC</th><th>365</th><th>366</th><th>367</th><th>368</th><th>IX</th><th>Output</th></tr>'; let pm = mem0, pa = null, pix = 0;
    rows.slice(0, k).forEach((r, i) => { const hl = (c) => (c ? ' style="background:var(--accent-soft);font-weight:700"' : ""); h += `<tr><td>${r.addr}</td><td>${r.ins}</td><td${hl(r.acc !== pa)}>${r.acc}</td>` + [365, 366, 367, 368].map((a) => `<td${hl(r.mem[a] !== pm[a])}>${r.mem[a]}</td>`).join("") + `<td${hl(r.ix !== pix)}>${r.ix}</td><td>${r.out}</td></tr>`; pm = r.mem; pa = r.acc; pix = r.ix; });
    $("#trT").innerHTML = h + "</table></div>" + (k >= rows.length ? '<div class="verdict">The program has finished: it outputs A then B (ASCII 65 and 66).</div>' : ""); };
  $("#tr_step").onclick = () => { if (k < rows.length) { k++; paint(); } }; $("#tr_reset").onclick = reset; reset();
})();
btnTable("wB", "wO", [
  ["LDM #5", "Immediate", "The operand is the data"],
  ["LDD 100", "Direct", "The operand is the address"],
  ["LDI 100", "Indirect", "Address of the address"],
  ["LDX 100", "Indexed", "100 plus IX"],
  ["Jump 3 instructions back", "Relative", "Offset from the current instruction"]
], ["Instruction", "Mode", "Why"]);
''' + _prjs

finish("as-4-2-2-addressing-modes-tracing", "as422", "Addressing Modes and Tracing Programs",
  "Immediate, direct, indirect, indexed and relative addressing, how to trace an assembly program with a trace table, with animations, a trace simulator and the real Paper 1 questions from 2021 to 2026.",
  "4.2.2", "4 · Processor fundamentals", "section 4.2 Assembly language", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on addressing modes and tracing (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
