"""A Level CS syllabus 15.1.1: RISC and CISC processors, pipelining and interrupt handling. Run: python3 tools/artifact-kit/mk_ac1511.py"""
from ak20 import *


def pipe_table(n, stages=("IF", "ID", "OF", "IE", "WB")):
    """HTML table of n instructions through the stages, one stage per clock cycle (the exam's layout)."""
    cyc = n + len(stages) - 1
    h = '<div class="tw"><table class="t mono"><tr><th>Stage</th>' + "".join(f"<th>{c}</th>" for c in range(1, cyc + 1)) + "</tr>"
    for si, st in enumerate(stages):
        h += f"<tr><td><b>{st}</b></td>"
        for c in range(1, cyc + 1):
            i = c - si
            h += f"<td>{('I' + str(i)) if 1 <= i <= n else ''}</td>"
        h += "</tr>"
    return h + "</table></div>"


learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>RISC</b> (Reduced Instruction Set Computer) processor has a <b>small set of simple, fixed-length instructions</b>, each normally completing in <b>one clock cycle</b>, with <b>many general-purpose registers</b> and a hardwired control unit, so it suits <b>pipelining</b>. A <b>CISC</b> (Complex Instruction Set Computer) processor has a <b>large set of complex, variable-length instructions</b>, many addressing modes, <b>few registers</b> and a programmable (micro-coded) control unit, and an instruction may take several clock cycles. <b>Pipelining</b> splits the fetch-execute cycle into stages and overlaps the stages of different instructions so a new instruction can finish every clock cycle, which raises <b>instruction throughput</b>. When an <b>interrupt</b> arrives the processor stops the current program, saves the register contents on the stack, runs an interrupt service routine, then restores the registers and carries on. Pipelining makes interrupts harder to handle because several instructions are in progress at once.</p></div>

  <h2>1 · RISC and CISC</h2>
  <div class="tw"><table class="t">
    <tr><th>Feature</th><th>RISC</th><th>CISC</th></tr>
    <tr><td>Instruction set</td><td><b>Small</b>: fewer, simpler instructions</td><td><b>Large</b>: many, complex instructions</td></tr>
    <tr><td>Instruction length and format</td><td><b>Fixed length</b>, few formats</td><td><b>Variable length</b>, many formats</td></tr>
    <tr><td>Clock cycles</td><td>Usually <b>one cycle</b> per instruction</td><td>Often <b>several cycles</b> (an instruction may be split into sub-instructions)</td></tr>
    <tr><td>Addressing modes</td><td>Few (limited)</td><td>Many</td></tr>
    <tr><td>Registers</td><td><b>Many</b> general-purpose registers</td><td><b>Few</b> registers</td></tr>
    <tr><td>Control unit</td><td><b>Hardwired</b></td><td><b>Programmable</b> (micro-programmed / micro-coded); hardwired is also possible</td></tr>
    <tr><td>Pipelining</td><td>Straightforward: well suited</td><td>Harder: poorer pipelineability</td></tr>
    <tr><td>Memory access</td><td>Only <b>load and store</b> instructions address memory; more use of RAM</td><td>Many instruction types address memory; frequent use of cache</td></tr>
    <tr><td>Circuits</td><td>Simpler; fewer transistors</td><td>More complex circuits</td></tr>
    <tr><td>Design emphasis</td><td>On the <b>software</b>: the compiler does the work</td><td>On the <b>hardware</b>: it handles complex instructions</td></tr>
    <tr><td>Cache</td><td>Cache is often split into separate data and instruction caches</td><td>Often a single cache</td></tr>
  </table></div>
  <div class="tip"><b class="h">Remember</b>RISC: <b>R</b>educed means few, simple, one cycle, many registers, hardwired, pipelining. CISC: <b>C</b>omplex means many, long and varied, several cycles, few registers, programmable control unit.</div>

  <h2>2 · Pipelining</h2>
  <p>The fetch-execute cycle for one instruction is divided into <b>stages</b>. In a typical five-stage pipeline: <b>IF</b> instruction fetch, <b>ID</b> instruction decode, <b>OF</b> operand fetch, <b>IE</b> instruction execute, <b>WB</b> write back the result. Each stage uses a different part of the processor (and its own registers), so the stages of <b>different instructions can happen at the same time</b>.</p>
  <ul>
    <li>Each stage takes <b>one clock cycle</b>.</li>
    <li>No two instructions can be in the <b>same stage</b> in the same clock cycle.</li>
    <li>While one instruction is being decoded, the next is being fetched, and so on.</li>
  </ul>
  <p>Six instructions through a five-stage pipeline take <b>10</b> clock cycles (5 for the first, then one more for each of the other 5), instead of 30 without pipelining:</p>
  ''' + pipe_table(6) + '''
  <div class="tw"><table class="t">
    <tr><th>Instructions</th><th>Without pipelining</th><th>With a 5-stage pipeline</th></tr>
    <tr><td>6</td><td>6 × 5 = 30 cycles</td><td>5 + (6 − 1) = 10 cycles</td></tr>
    <tr><td>n</td><td>5n</td><td>5 + (n − 1)</td></tr>
  </table></div>
  <p>The benefit is <b>increased CPU instruction throughput</b>: the number of instructions completed per unit of time goes up, although each single instruction still needs all five cycles. Pipelining works best for RISC because the instructions are the same length and each stage takes one cycle.</p>

  <h2>3 · Interrupt handling</h2>
  <p>An <b>interrupt</b> is a signal that tells the processor something needs attention (an input, a timer, an error). The processor checks for interrupts at the <b>end of each fetch-execute cycle</b>.</p>
  <ol>
    <li>The processor <b>detects the interrupt</b> at the start or end of a fetch-execute cycle.</li>
    <li>The current program is <b>temporarily stopped</b> and the <b>contents of the registers</b> (including the program counter) are <b>stored on the stack</b>.</li>
    <li>The processor runs the <b>interrupt service routine (ISR)</b>.</li>
    <li>When the ISR finishes, the <b>registers are restored</b> from the stack and the original program carries on from where it stopped.</li>
  </ol>
  <h3>Interrupts and pipelining</h3>
  <p>With a pipeline, <b>several instructions are in progress</b> when an interrupt arrives, so there is added complexity. Usually the <b>instructions currently in the pipeline are discarded</b> (except the one at the last stage, which is allowed to finish), the interrupt handler is run, and when the interrupt has been serviced the processor <b>restarts with the next instruction in the sequence</b>.</p>

  <h2>4 · Common ways to lose marks</h2>
  <ul>
    <li>Writing "RISC is faster". Give the reason: simple single-cycle instructions that pipeline well.</li>
    <li>Mixing the features: <b>many registers</b> is RISC; <b>many instruction formats and addressing modes</b> is CISC.</li>
    <li>Describing pipelining as "doing two things at once" without the stages of different instructions overlapping.</li>
    <li>Forgetting to store the register contents on the <b>stack</b> in interrupt handling, or to restore them afterwards.</li>
    <li>In a pipeline table, starting instruction 2 in the same cycle as instruction 1, or putting two instructions in one stage in the same cycle.</li>
    <li>Saying CISC is "slower" without the reason: instructions need several cycles and are harder to pipeline.</li>
  </ul>
'''

watch = '''
  <h2>1 · A pipeline fills up</h2>
  <p>Press Play, or click the steps. Six instructions, five stages: IF, ID, OF, IE, WB.</p>
  <div id="stA"></div>
  <h2>2 · Handling an interrupt</h2>
  <div id="stB"></div>
  <h2>3 · An interrupt arrives while the pipeline is full</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Pipeline calculator</h2>
  <p>Choose the number of instructions. The table shows each instruction moving through the stages, and the cycles needed with and without pipelining.</p>
  <div class="card"><div id="pS"></div><div id="pT"></div><div class="readout"><div><small>Without pipelining</small><strong id="p1"></strong></div><div><small>With pipelining</small><strong id="p2"></strong></div><div><small>Speed-up</small><strong id="p3"></strong></div></div></div>

  <h2>Lab 2 · An interrupt in a pipeline</h2>
  <p>Choose the clock cycle in which an interrupt arrives. See which instructions are discarded and which finish.</p>
  <div class="card"><div id="iS"></div><div id="iT"></div><div class="verdict" id="iV"></div></div>

  <h2>Lab 3 · RISC or CISC?</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · RISC or CISC?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which processor suits the statement?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps of interrupt handling in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Counting cycles</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Phones and tablets", "Most phone and tablet chips use a RISC design: simple instructions that are quick to carry out, using little power. That helps battery life.", "RISC: fewer transistors, simple single-cycle instructions, low power.") +
rw("Desktop and laptop processors", "Traditional PC processors have a very large instruction set built up over the years and break complex instructions into smaller internal steps.", "CISC: a large instruction set with complex, variable-length instructions.") +
rw("A pipelined assembly line", "Like a car factory, one stage of a pipeline is working on each car at once. Each car still takes the whole time, but a finished car leaves every cycle.", "pipelining raises throughput, not the time for one instruction.") +
rw("Pressing a key while a program runs", "The keyboard sends an interrupt. The processor saves where it was, runs the routine that reads the key, then picks the program up again.", "interrupt handling uses the stack to save and restore the registers.") +
rw("A branch in a program", "If a program jumps, the instructions already fetched into the pipeline may be the wrong ones and have to be discarded, which costs time.", "pipelines add complexity when the sequence of instructions changes.")
)

where = [
  ("M/J 2022", "31, 33", "4(a), 4(b)", "4 + 2", "Describe RISC and CISC; two differences"),
  ("O/N 2022", "31, 33", "10(a), 10(b)", "2 + 4", "Tick RISC or CISC for five statements; describe pipelining in RISC"),
  ("M/J 2023", "32", "8(a), 8(b)", "2 + 4", "Describe pipelining in RISC; complete a pipeline table for six instructions"),
  ("M/J 2024", "31, 33", "11(a), (b), (c)", "2 + 3 + 3", "Two RISC features; interrupt handling; how pipelining affects interrupts"),
  ("O/N 2024", "31, 33", "2", "4", "Four features of a RISC processor"),
  ("O/N 2024", "32", "8", "4", "Four features of a CISC processor")]

past = '''  <p class="note">RISC and CISC are tested in Paper 3 in most series from May/June 2022 to Oct/Nov 2024. Pipelining and interrupts are asked with them. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>RISC and CISC</h3>
''' + peq(SRC("s22", "31, 33", "Q4"), "4 + 2 marks", "Describe / Identify",
  "Reduced Instruction Set Computers (RISC) and Complex Instruction Set Computers (CISC) are two types of processor. (a) Describe what is meant by RISC and CISC processors. (b) Identify two differences between RISC and CISC processors.",
  "(a) two features of each. (b) a difference needs both sides: RISC has ..., CISC has ...",
  "<p><b>(a)</b> RISC (max 2): " + mks(["Uses simple instructions", "Uses fixed-length instructions", "Instructions only require one clock cycle", "Uses many registers", "Makes use of pipelining", "Hardwired control unit"]) + " CISC (max 2): " + mks(["Uses many instruction formats", "Uses variable-length instructions", "Makes use of different addressing modes", "Uses few registers", "Has a large instruction set", "Programmable control unit", "Instructions may need many clock cycles"], "a") + "</p><p><b>(b)</b> Any two differences: " + mks(["RISC has fewer instructions; CISC has more", "RISC has many registers; CISC has few", "RISC instructions are simpler; CISC's are more complex", "RISC usually uses single-cycle instructions; CISC uses multi-cycle", "RISC uses fixed-length instructions; CISC uses variable-length", "RISC has better pipelineability; CISC poorer", "RISC has a hard-wired control unit; CISC a programmable one", "RISC only uses load and store instructions to address memory"]) + "</p>", "Giving only one side of a difference, for example 'RISC has many registers', with nothing about CISC.") + peq(SRC("w24", "31, 33", "Q2"), "4 marks", "Identify",
  "Reduced Instruction Set Computers (RISC) is a type of processor. Identify four features of a RISC processor.",
  "Choose four from the list.",
  "<p>Any four: " + mks(["A low number of instruction formats / a small instruction set", "Single-clock-cycle instructions", "Fixed-length instructions", "Many general-purpose registers", "Works well with pipelining", "A hard-wired control unit", "Makes extensive use of RAM", "A low number of addressing modes", "The design emphasis is on the software"]) + "</p>", None) + peq(SRC("w24", "32", "Q8"), "4 marks", "Identify",
  "Complex Instruction Set Computer (CISC) is a type of processor. Identify four features of a CISC processor.",
  "The opposite of RISC.",
  "<p>Any four: " + mks(["Many instruction formats are possible", "A large instruction set", "Many addressing modes are available", "Variable-length / multi-operation instructions", "Multi-clock-cycle instructions", "Complex decoding of instructions", "Uses complex circuits", "Makes frequent use of cache memory", "Uses a programmable (micro-programmed) control unit", "The hardware has to handle complex instructions by converting them into sub-instructions; the design emphasis is on hardware"]) + "</p>", None) + peq(SRC("w22", "31, 33", "Q10(a)"), "2 marks", "Tick",
  "Tick one box in each row to show whether the statement applies to RISC or CISC processors: (1) uses a smaller instruction set; (2) uses single-cycle instructions and limited addressing modes; (3) uses fewer general-purpose registers; (4) uses both hardwired and micro-coded control units; (5) uses a system where cache is split between data and instructions.",
  "Two marks for all five rows right, one mark for four right.",
  "<p>" + mks(["(1) RISC", "(2) RISC", "(3) CISC", "(4) CISC", "(5) RISC"]) + " (two marks for all five, one for four)</p>", "Ticking CISC for the split cache. A separate data cache and instruction cache is a RISC feature.") + '''
  <h3>Pipelining and interrupts</h3>
''' + peq(SRC("w22", "31, 33", "Q10(b)"), "4 marks", "Describe",
  "Describe the process of pipelining during the fetch-execute cycle in RISC processors.",
  "Stages, one cycle each, overlapping instructions, no two in the same stage.",
  "<p>Any four: " + mks(["Instructions are divided into subtasks / five stages", "Instruction fetch (IF), instruction decode (ID), operand fetch (OF), instruction execute (IE), write back (WB)", "Each subtask is completed during one clock cycle", "No two instructions can execute the same stage in the same clock cycle", "The second instruction begins in the second clock cycle while the first moves on to its second subtask", "The third instruction begins in the third cycle while the first and second move on to their second and third subtasks, and so on"]) + "</p>", None) + peq(SRC("s23", "32", "Q8"), "2 + 4 marks", "Describe / Complete",
  "(a) Describe the use of pipelining in Reduced Instruction Set Computers (RISC). (b) The processing of instructions is divided into five stages: instruction fetch (IF), instruction decode (ID), operand fetch (OF), instruction execute (IE), write back result (WB). Each stage is carried out using a different register when pipelining is used. Complete the table to show how a program consisting of six instructions would be completed using pipelining." + qcode('''Stage  1  2  3  4  5  6  7  8  9  10
IF
ID
OF
IE
WB'''),
  "Instruction 1 starts in cycle 1; instruction 2 starts in cycle 2; and so on. Six instructions take ten cycles.",
  "<p><b>(a)</b> Any two: " + mks(["Pipelining allows several instructions to be processed simultaneously / concurrently", "so increasing CPU instruction throughput: more instructions completed per unit of time", "Each stage is completed in one clock cycle and no two instructions use the same stage in the same cycle", "While one instruction is being decoded the next can be fetched"]) + "</p><p><b>(b)</b> Four marks: " + mks(["the first stage of the first instruction is in the first clock cycle", "the first instruction is completed over five clock cycles", "the remaining instructions are completed over ten clock cycles", "with no extra instruction sections added on any row"], "a") + "</p>" + pipe_table(6), "Putting two instructions in the same stage in one clock cycle, or ending after 30 cycles. With pipelining the six instructions finish in ten cycles.") + peq(SRC("s24", "31, 33", "Q11"), "2 + 3 + 3 marks", "State / Outline / Explain",
  "Reduced Instruction Set Computers (RISC) and Complex Instruction Set Computers (CISC) are two types of processor. (a) State two features of RISC processors. (b) Outline the process of interrupt handling as it could be applied to RISC or CISC processors. (c) Explain how pipelining affects interrupt handling for RISC processors.",
  "(b) detect, save the registers on the stack, ISR, restore. (c) several instructions are in the pipeline.",
  "<p><b>(a)</b> Any two: " + mks(["Uses hard-wired control units", "Uses relatively few, simple instructions", "Relatively few addressing modes", "A single cycle for each instruction", "Fixed-length instructions", "General-purpose registers", "Pipelining is straightforward to apply"]) + "</p><p><b>(b)</b> Up to three: " + mks(["The processor detects an interrupt at the start or end of the fetch-execute cycle", "The current program is temporarily stopped and the status of each register is stored on the stack", "After the interrupt has been serviced (the interrupt service routine executed)", "the registers are restored to their original status from the stack"], "a") + "</p><p><b>(c)</b> Up to three: " + mks(["Pipelining adds complexity: there could be a number of instructions still in the pipeline when the interrupt is received", "All the instructions currently in operation are usually discarded except for the last one (the one at write-back)", "the interrupt handler routine is applied to the remaining instruction", "Once the interrupt has been serviced the processor can restart with the next instruction in the sequence"]) + "</p>", "Describing what the interrupt is for, instead of what the processor does: save the registers, run the ISR, restore.")

review = req("3 marks", "Explain", "Explain why RISC processors are well suited to pipelining.", "Think about instruction length and cycles.",
  "<p>" + mks(["RISC instructions are all the same (fixed) length and have few formats, so each can be fetched and decoded in a predictable way.", "Most instructions take a single clock cycle, so each pipeline stage takes one cycle.", "So the stages of different instructions can overlap without waiting."]) + "</p>", None) + req("3 marks", "Calculate", "A program of 20 instructions runs on a five-stage pipeline with one clock cycle per stage. How many clock cycles does it need with and without pipelining?", "5 + (n − 1) against 5n.",
  "<p>" + mks(["Without pipelining: 20 × 5 = 100 cycles", "With pipelining: 5 + 19 = 24 cycles", "A speed-up of about 4.2 times"]) + "</p>", None) + req("2 marks", "State", "State two reasons why CISC processors are harder to pipeline than RISC.", "Length and cycles.",
  "<p>" + mks(["Instructions have variable lengths and many formats, so decoding takes different times.", "Instructions need different numbers of clock cycles, so the stages do not line up."]) + "</p>", None) + req("3 marks", "Describe", "A key is pressed while a program is running. Describe what the processor does with the registers.", "Stack, ISR, restore.",
  "<p>" + mks(["It stops the current program at the end of the fetch-execute cycle and stores the register contents on the stack.", "It runs the interrupt service routine to deal with the key press.", "It then restores the register contents from the stack and continues the program."]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between the control units of RISC and CISC processors.", "How they are built.",
  "<p>" + mks(["A RISC control unit is hardwired.", "A CISC control unit is usually programmable (micro-programmed), so complex instructions are broken into micro-operations."]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on RISC, CISC, pipelining and interrupts (Paper 3), 2022 to 2024. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Give both sides of a difference.", "'RISC has many registers whereas CISC has few.'"),
  ("RISC: reduced and simple.", "Small set, fixed length, one cycle, many registers, hardwired, pipelining."),
  ("CISC: complex.", "Large set, variable length, many cycles, few registers, programmable control unit."),
  ("Pipeline tables: staircase.", "Instruction n starts in cycle n. n instructions take n + 4 cycles for five stages."),
  ("Interrupts: stack.", "Save the registers on the stack, run the ISR, restore them."),
  ("Pipelining and interrupts: the pipeline is full.", "Several instructions are in progress, so most are discarded and the processor restarts at the next instruction."),
], [
  ("what pipelining does", "It overlaps the stages of different instructions so more instructions are completed per unit of time."),
  ("why RISC suits pipelining", "Its instructions are simple, fixed length and take one clock cycle."),
  ("how an interrupt is handled", "The registers are stored on the stack, the ISR is run, then the registers are restored."),
  ("how pipelining affects interrupts", "Several instructions are in the pipeline, so they are usually discarded and the processor restarts with the next instruction."),
], [("State / Identify", "Give the features or answers only."), ("Describe", "Say how it works, in several points."), ("Outline", "Give the main steps."), ("Explain", "Give the reason as well.")]) + FC

js = AKJS + AK20JS + r'''
const ST = ["IF", "ID", "OF", "IE", "WB"];
function pipeGrid(n, upto, discardFrom) {
  const cyc = n + 4; let h = '<div class="tw"><table class="t mono"><tr><th>Stage</th>' + Array.from({ length: cyc }, (_, c) => `<th>${c + 1}</th>`).join("") + "</tr>";
  ST.forEach((s, si) => { h += `<tr><td><b>${s}</b></td>`; for (let c = 1; c <= cyc; c++) { const i = c - si, show = i >= 1 && i <= n && c <= upto, disc = discardFrom && show && c >= discardFrom.c && !(si === 4 && c === discardFrom.c); h += `<td style="${show ? (disc ? "background:var(--bad-soft);text-decoration:line-through" : "background:var(--good-soft)") : ""}">${show ? "I" + i : ""}</td>`; } h += "</tr>"; });
  return h + "</table></div>";
}

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 18, "cycle →", "sm");
    for (let c = 1; c <= 10; c++) o += SV.text(94 + (c - 1) * 62, 18, String(c), "sm", { "text-anchor": "middle" });
    ST.forEach((st, si) => { o += SV.text(30, 52 + si * 38, st, "lbl bd"); for (let c = 1; c <= 10; c++) { const i = c - si; if (i >= 1 && i <= 6 && c <= k) o += SV.rect(66 + (c - 1) * 62, 32 + si * 38, 56, 30, ["f1", "f2", "f3", "f4", "f1", "f2"][i - 1], { rx: 5 }) + SV.text(94 + (c - 1) * 62, 52 + si * 38, "I" + i, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); } });
    if (k === 5) o += SV.text(30, 245, "cycle 5: the pipeline is full; instruction 1 finishes", "lbl bd t3", { style: "font-size:14px" });
    if (k === 10) o += SV.text(30, 245, "10 cycles for 6 instructions (30 without pipelining)", "lbl bd t3", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 258, label: "A five-stage pipeline", base: { i: 0 }, draw, tween: 200, dwell: 1600, steps: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map((i) => ({ cap: i === 0 ? "Each instruction goes through five stages: <b>IF, ID, OF, IE, WB</b>, one stage per clock cycle. Instruction 1 starts in cycle 1." : i === 1 ? "Cycle 1: I1 is fetched." : i === 2 ? "Cycle 2: I1 is decoded while <b>I2 is fetched</b>. Two instructions are in progress at once." : i === 5 ? "Cycle 5: five instructions are in progress, one in each stage. I1 writes back its result." : i === 10 ? "Cycle 10: the last instruction, I6, writes back. A finished instruction came out every cycle after cycle 5." : "Cycle " + i + ": each instruction moves on one stage and a new one is fetched until I6 has started.", s: { i } })) });
})();

(function () {
  const rows = ["Interrupt detected at the end of the fetch-execute cycle", "Register contents (including the PC) saved on the stack", "Interrupt service routine (ISR) runs", "Registers restored from the stack", "The original program carries on"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    rows.forEach((r, i) => (o += SV.rect(30, 14 + i * 40, 430, 34, k === i ? "cell-warn" : k > i ? "cell-ok" : "cell", { rx: 6 }) + SV.text(44, 36 + i * 40, r, "lbl", { style: "font-size:13px" })));
    o += SV.text(500, 24, "stack", "sm");
    for (let i = 0; i < 4; i++) o += SV.rect(500, 34 + (3 - i) * 36, 200, 30, k >= 1 && k <= 3 && i < 2 ? "f3" : "cell", { rx: 4, ...op(k >= 1 && k <= 3 && i < 2 ? 1 : 0.4) }) + (k >= 1 && k <= 3 && i < 2 ? SV.text(512, 54 + (3 - i) * 36, ["PC and ACC", "other registers"][i], "lbl", { style: "font-size:12px" }) : "");
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 225, label: "Interrupt handling", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: rows.map((r, i) => ({ cap: ["The processor checks for an interrupt at the end of each fetch-execute cycle and finds one.", "The program is paused. The register contents, including the program counter, are <b>pushed on the stack</b>.", "The <b>interrupt service routine</b> deals with whatever caused the interrupt.", "The ISR is finished. The registers are <b>restored</b> (popped) from the stack.", "The original program <b>carries on</b> exactly where it left off."][i], s: { i } })) });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = pipeSvg(k);
    return o;
  };
  function pipeSvg(k) {
    let o = SV.text(30, 18, "an interrupt arrives in cycle 5", "sm");
    ST.forEach((st, si) => { o += SV.text(30, 52 + si * 38, st, "lbl bd"); for (let c = 1; c <= 5; c++) { const i = c - si; if (i >= 1 && i <= 5) o += SV.rect(66 + (c - 1) * 80, 32 + si * 38, 74, 30, k >= 2 && c === 5 && si < 4 ? "cell-no" : k >= 1 && c === 5 ? "cell-ok" : "f3", { rx: 5 }) + SV.text(103 + (c - 1) * 80, 52 + si * 38, "I" + i, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); } });
    if (k >= 1) o += SV.text(66, 235, "cycle 5: I1 to I5 are all in the pipeline when the interrupt is received", "lbl bd", { style: "font-size:13px" });
    if (k >= 2) o += SV.text(66, 255, "I2, I3, I4, I5 are discarded; I1 (at write-back) is allowed to finish", "lbl bd t2", { style: "font-size:13px" });
    if (k >= 3) o += SV.text(66, 275, "after the ISR the processor restarts with the next instruction in the sequence (I2)", "lbl bd t3", { style: "font-size:13px" });
    return o;
  }
  Lib.stepper($("#stC"), { w: 760, h: 285, label: "Interrupt and a full pipeline", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "A program is running in a pipeline: several instructions are in progress at the same moment.", s: { i: 0 } },
    { cap: "An interrupt arrives at cycle 5. Instructions 1 to 5 are all in the pipeline: this is the extra <b>complexity</b> pipelining brings.", s: { i: 1 } },
    { cap: "Usually the instructions in the pipeline are <b>discarded</b>, except the one at the last (write-back) stage, which is allowed to finish.", s: { i: 2 } },
    { cap: "After the interrupt service routine, the processor <b>restarts with the next instruction in the sequence</b>.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  let n = 6;
  const paint = () => { $("#pT").innerHTML = pipeGrid(n, n + 4); $("#p1").textContent = n * 5 + " cycles"; $("#p2").textContent = n + 4 + " cycles"; $("#p3").textContent = (n * 5 / (n + 4)).toFixed(2) + "×"; };
  Lib.slider($("#pS"), { id: "pss", label: "Number of instructions ", min: 1, max: 12, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();

/* Lab 2 */
(function () {
  let c = 4;
  const paint = () => {
    $("#iT").innerHTML = pipeGrid(6, c, { c });
    const inFlight = [0, 1, 2, 3, 4].map((si) => c - si).filter((i) => i >= 1 && i <= 6);
    $("#iV").textContent = "Interrupt in cycle " + c + ": instructions " + inFlight.map((i) => "I" + i).join(", ") + " are in the pipeline. " + (inFlight.length > 1 ? "All except the one at write-back (struck-through ones are discarded) are discarded; the processor restarts with the next instruction after the ISR." : "Only one instruction is in the pipeline, so little is lost.");
  };
  Lib.slider($("#iS"), { id: "iss", label: "Interrupt arrives in clock cycle ", min: 1, max: 10, value: c, fmt: (x) => x, onInput: (v) => { c = v; paint(); } }); paint();
})();

btnTable("eB", "eO", [
  ["Instruction set", "Small, simple instructions", "Large, complex instructions", "Fewer instructions = RISC"],
  ["Instruction length", "Fixed", "Variable", "Fixed suits pipelining"],
  ["Cycles per instruction", "Usually one", "Several", "One cycle per stage"],
  ["Registers", "Many general-purpose registers", "Few registers", "Many = RISC"],
  ["Control unit", "Hardwired", "Programmable (micro-coded)", "Hardwired = RISC"],
  ["Pipelining", "Well suited", "Harder", "RISC: better pipelineability"]
], ["Feature", "RISC", "CISC", "Point to make"]);
''' + CLASSIFY("cl1", "Is the feature RISC or CISC?", ["RISC", "CISC"],
  [("Many general-purpose registers", 0), ("Variable-length instructions", 1), ("Single-cycle instructions", 0), ("A large instruction set", 1), ("A hard-wired control unit", 0), ("Many addressing modes", 1), ("Makes frequent use of cache memory", 1), ("The design emphasis is on the software", 0)],
  "RISC: simple, fixed, one cycle, many registers. CISC: complex, variable, many modes.") + CLASSIFY("cl2", "Which does the statement describe?", ["Pipelining", "Interrupt handling"],
  [("Stages of different instructions overlap", 0), ("Registers are stored on the stack", 1), ("Increases instruction throughput", 0), ("An interrupt service routine is run", 1), ("No two instructions in the same stage in a cycle", 0), ("Registers are restored afterwards", 1)],
  "Pipelining overlaps stages. Interrupt handling saves state, runs the ISR, restores it.") + ORDER(
  "Put the steps of interrupt handling in order.",
  ["The processor detects the interrupt", "The register contents are stored on the stack", "The interrupt service routine is executed", "The registers are restored from the stack", "The interrupted program continues"],
  "Detect, save, ISR, restore, continue.") + MATCH([
  ["RISC", "Reduced instruction set: simple, fixed-length, single-cycle"], ["CISC", "Complex instruction set: many formats and addressing modes"], ["Pipelining", "Overlapping the stages of different instructions"], ["Throughput", "Instructions completed per unit of time"], ["ISR", "The routine that deals with an interrupt"]]) + CALC([
  {"q": "A five-stage pipeline runs 6 instructions. How many clock cycles in total?", "a": 10, "unit": "", "tol": 0.01, "hint": "5 + (6 − 1).", "sol": "<b>10</b>."},
  {"q": "The same 6 instructions without pipelining. How many clock cycles?", "a": 30, "unit": "", "tol": 0.01, "hint": "6 × 5.", "sol": "<b>30</b>."},
  {"q": "A five-stage pipeline runs 100 instructions. How many clock cycles?", "a": 104, "unit": "", "tol": 0.01, "hint": "5 + 99.", "sol": "<b>104</b>."},
  {"q": "In which clock cycle does instruction 3 reach the OF (third) stage?", "a": 5, "unit": "", "tol": 0.01, "hint": "Instruction n is in stage s in cycle n + s − 1: 3 + 3 − 1.", "sol": "<b>5</b>."},
  {"q": "How many instructions are in a full five-stage pipeline at one moment?", "a": 5, "unit": "", "tol": 0.01, "hint": "One in each stage.", "sol": "<b>5</b>."}]) + MCQ([
  ("Which is a RISC feature?", ["Variable-length instructions", "Many registers", "A large instruction set", "A programmable control unit"], 1, "RISC has many general-purpose registers."),
  ("Which is a CISC feature?", ["Single-cycle instructions", "Hard-wired control unit", "Many addressing modes", "Easy pipelining"], 2, "CISC has many addressing modes."),
  ("What does pipelining improve?", ["Memory size", "Instruction throughput", "Screen resolution", "Clock speed"], 1, "More instructions completed per unit of time."),
  ("Where are the registers stored when an interrupt is handled?", ["On the stack", "In ROM", "On the hard disk", "They are lost"], 0, "They are stored on the stack."),
  ("What usually happens to instructions in the pipeline when an interrupt arrives?", ["They all finish", "Most are discarded; the last-stage one finishes", "They are copied to RAM", "Nothing"], 1, "Most are discarded."),
  ("How many stages does the exam's pipeline have?", ["3", "4", "5", "6"], 2, "IF, ID, OF, IE, WB.")], "qz1") + CARDS([
  ("RISC", "Few simple fixed-length instructions, one cycle, many registers, hardwired."), ("CISC", "Large complex variable-length instructions, several cycles, few registers, programmable."), ("Pipelining", "Overlap the stages of different instructions. Throughput up."), ("Five stages", "IF, ID, OF, IE, WB."),
  ("n instructions", "5 + (n − 1) cycles with a five-stage pipeline."), ("Interrupt", "Detect, stack the registers, ISR, restore, continue."), ("Pipeline + interrupt", "Several instructions in progress: usually discarded; restart at the next."), ("Design emphasis", "RISC: software. CISC: hardware.")])

build("ac1511", "ac-15-1-1-risc-cisc-pipelining", "RISC, CISC, Pipelining and Interrupts", EYA("15.1.1"),
  "RISC and CISC processors compared, five-stage pipelining with pipeline tables, interrupt handling and how pipelining affects it; animations, a pipeline calculator and the real Paper 3 questions from 2022 to 2024.",
  dict(sub=CBK("Chapter 15 · Hardware and virtual machines, section 15.1 Processors, parallel processing and virtual machines"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
