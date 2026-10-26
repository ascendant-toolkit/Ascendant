"""AS CS 4.1.3: fetch-execute cycle in register transfer notation, and interrupts. Run: python3 tools/artifact-kit/mk_as413.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>The CPU repeats the <b>fetch-execute (F-E) cycle</b> for every instruction: <b>fetch</b> it from main memory using the PC, MAR, MDR and CIR, then <b>decode</b> and <b>execute</b> it. In <b>register transfer notation (RTN)</b> the fetch is: <b>MAR ← [PC]</b>, <b>PC ← [PC] + 1</b>, <b>MDR ← [[MAR]]</b>, <b>CIR ← [MDR]</b>. An <b>interrupt</b> is a signal from a device or a process seeking the attention of the processor. At the end of each cycle the processor checks for an interrupt; if its <b>priority</b> is higher than the current process, the processor stores the registers on the <b>stack</b>, calls the <b>interrupt service routine (ISR)</b>, then restores the registers and carries on. Interrupts come from hardware (key pressed, power failure, printer out of paper, buffer full) or from software (division by zero, stack overflow, invalid memory access).</p></div>

  <h2>1 · Register transfer notation</h2>
  <p>Square brackets mean "the contents of"; the arrow means "is copied to". <b>[[MAR]]</b> means the contents of the memory location whose address is held in the MAR.</p>
  <div class="tw"><table class="t">
    <tr><th>Step</th><th>RTN</th><th>Meaning</th></tr>
    <tr><td>1</td><td class="mono">MAR ← [PC]</td><td>The contents of the PC (the address of the next instruction) are copied to the MAR</td></tr>
    <tr><td>2</td><td class="mono">PC ← [PC] + 1</td><td>The address in the PC is incremented, ready for the next instruction</td></tr>
    <tr><td>3</td><td class="mono">MDR ← [[MAR]]</td><td>The data at the address held in the MAR is copied to the MDR (via the data bus; the address bus carries the MAR)</td></tr>
    <tr><td>4</td><td class="mono">CIR ← [MDR]</td><td>The contents of the MDR (the instruction) are copied into the CIR</td></tr>
  </table></div>
  <p>The same order is accepted if steps 1 and 2 are done together. The PC is <b>incremented</b>, never decremented, and step 3 uses the <b>contents of the address</b> in the MAR, not the MAR itself. After step 4 the CU <b>decodes</b> the instruction in the CIR and the processor <b>executes</b> it (for example the ALU adds a number to the ACC).</p>

  <h2>2 · Interrupts</h2>
  <p><b>Purpose:</b> an interrupt sends a signal from a device or process seeking the attention of the processor, so that urgent events can be dealt with without the processor constantly polling.</p>
  <div class="tw"><table class="t">
    <tr><th>Hardware interrupt</th><th>Software interrupt</th></tr>
    <tr><td>Buffer full; printer out of paper; a key pressed; power failure; a device finished transferring data</td><td>Division by zero (a run-time error); an attempt to access an invalid memory location; array index out of bounds; stack overflow; a program requesting a device</td></tr>
  </table></div>
  <p><b>Detected:</b> at the <b>end</b> (or start) of each fetch-execute cycle, after the execute stage has finished, the processor checks the <b>interrupt register</b>. <b>Handled:</b></p>
  <ol>
    <li>An interrupt flag is raised in the interrupt register.</li>
    <li>The <b>priority</b> of the interrupt is checked. If it is <b>lower</b> than the current process, the F-E cycle simply continues.</li>
    <li>If it is <b>higher</b>, the state of the current process is saved: the <b>contents of the registers are stored on the stack</b>.</li>
    <li>The source and type of interrupt is identified, and the appropriate <b>interrupt service routine (ISR)</b> (its address is loaded into the PC) is called.</li>
    <li>When the ISR has finished, the processor checks again for further interrupts of higher priority.</li>
    <li>If none, the <b>registers are restored from the stack</b> and the interrupted process continues with the next F-E cycle.</li>
  </ol>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Writing PC ← [PC] − 1 or leaving out the double brackets in MDR ← [[MAR]].</li>
    <li>Explaining the interrupt with no mention of priority, the stack, or the ISR.</li>
    <li>Saying the processor stops everything: it only changes to the ISR if the priority is higher than the current process.</li>
    <li>Saying the registers are "deleted" or "saved on the hard disk". They are stored on the stack.</li>
  </ul>
'''

watch = '''
  <h2>1 · The fetch stage in RTN</h2>
  <div id="stA"></div>
  <h2>2 · Handling an interrupt</h2>
  <div id="stB"></div>
  <h2>3 · Priority of interrupts</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Step through the F-E cycle</h2>
  <p>Press Step to run each register transfer. The program adds 3 to 5 and stores the result.</p>
  <div class="card"><div class="btnrow"><button id="fe_step">Step</button><button id="fe_reset">Reset</button></div><div id="feR"></div><div id="feM"></div><div id="feL" class="verdict"></div></div>
  <h2>Lab 2 · Hardware or software interrupt?</h2>
  <div class="card"><div id="iB" class="btnrow"></div><div id="iO"></div></div>
  <h2>Lab 3 · Interrupt or not?</h2>
  <div class="card"><div id="pS"></div><div id="pV" class="verdict"></div></div>
'''

_pr, _prjs = PR(["Hardware or software interrupt?", "Is the RTN statement correct?", "Match the RTN to its description", "Put the interrupt handling in order", "Working out", "Multiple choice"],
  ("Hardware interrupt or software interrupt?", ["Hardware", "Software"], [("A key is pressed", 0), ("Division by zero", 1), ("The printer is out of paper", 0), ("Stack overflow", 1), ("Power failure", 0), ("Array index out of bounds", 1)], "Hardware: devices. Software: program errors."),
  ("Is the RTN statement correct for the fetch stage?", ["Correct", "Incorrect"], [("MAR ← [PC]", 0), ("PC ← [PC] − 1", 1), ("MDR ← [[MAR]]", 0), ("MDR ← [MAR]", 1), ("CIR ← [MDR]", 0), ("PC ← [PC] + 1", 0)], "PC is incremented; MDR takes the contents of the address in the MAR."),
  [["MAR ← [PC]", "The contents of the PC are copied to the MAR"], ["PC ← [PC] + 1", "The address in the PC is incremented"], ["MDR ← [[MAR]]", "The data at the address held in the MAR is copied to the MDR"], ["CIR ← [MDR]", "The contents of the MDR are copied into the CIR"], ["ISR", "Routine called to handle an interrupt"]],
  ("Put the interrupt handling steps in order.", ["The interrupt flag is set and the F-E cycle ends", "The priority of the interrupt is checked", "The contents of the registers are stored on the stack", "The appropriate ISR is called and runs", "The registers are restored from the stack and the process continues"], "Flag, priority, stack, ISR, restore."),
  [{"q": "The PC holds 100. After the fetch stage (PC ← [PC] + 1) what does it hold?", "a": 101, "unit": "", "tol": 0.01, "hint": "Increment by 1.", "sol": "<b>101</b>."}, {"q": "A program has 8 instructions. How many fetch stages (one per instruction)?", "a": 8, "unit": "", "tol": 0.01, "hint": "One each.", "sol": "<b>8</b>."}, {"q": "Each F-E cycle takes 4 clock ticks. How many ticks for 8 instructions?", "a": 32, "unit": "", "tol": 0.01, "hint": "8 × 4.", "sol": "<b>32</b>."}, {"q": "An interrupt has priority 5 and the running process priority 3. Should the F-E cycle be interrupted? Answer 1 for yes, 0 for no.", "a": 1, "unit": "", "tol": 0.01, "hint": "Higher priority interrupts.", "sol": "<b>1</b>: yes."}, {"q": "How many RTN steps are in the fetch stage?", "a": 4, "unit": "", "tol": 0.01, "hint": "MAR, PC, MDR, CIR.", "sol": "<b>4</b>."}],
  [("PC ← [PC] + 1 means:", ["The address in the PC is incremented", "The PC is decremented", "The PC is cleared", "MAR is incremented"], 0, "Incremented."), ("MDR ← [[MAR]] copies:", ["The data at the address in the MAR", "The MAR itself", "The PC", "The CIR"], 0, "Data at that address."), ("Interrupts are checked:", ["At the end of each F-E cycle", "Only at start-up", "Never", "Once an hour"], 0, "End of cycle."), ("Registers are saved on:", ["The stack", "The ROM", "The hard disk", "The cache only"], 0, "The stack."), ("A power failure is a:", ["Hardware interrupt", "Software interrupt", "Compiler error", "Syntax error"], 0, "Hardware."), ("The ISR is:", ["A routine that handles the interrupt", "A register", "A bus", "A type of memory"], 0, "Interrupt service routine.")],
  [("Fetch (RTN)", "MAR←[PC]; PC←[PC]+1; MDR←[[MAR]]; CIR←[MDR]."), ("Decode, execute", "CU decodes the CIR; the instruction runs."), ("Interrupt", "Signal seeking the processor's attention."), ("Detected", "At the end of an F-E cycle."), ("Priority", "Checked; higher interrupts the process."), ("Stack", "Registers stored there."), ("ISR", "Routine called to handle it."), ("Restore", "Registers reloaded; process continues.")])

real = RWNOTE + (
rw("Typing while a video plays", "Each key press is an interrupt: the CPU pauses the video work briefly, runs the keyboard routine, then returns to the video.", "hardware interrupt, ISR, back to the process.") +
rw("A game crashing with 'stack overflow'", "A program that calls itself too deeply uses up the stack and raises a software interrupt, which the OS handles.", "software interrupt.") +
rw("Unplugging the power", "The power failure interrupt has the highest priority: the processor can save critical data before everything stops.", "priority.") +
rw("An app 'not responding'", "The CPU still runs the fetch-execute cycle millions of times a second; the app is waiting for data and the OS handles other work in between.", "the cycle never stops.") +
rw("Why saving the registers matters", "When you return from a notification, your program carries on exactly where it was because its registers were stored and restored.", "stack.")
)

where = [
  ("O/N 2021", "11, 13", "6(a)", "4", "Find two errors in the fetch-execute register transfer notation"),
  ("O/N 2021", "12", "7(a)", "3", "Hardware or software interrupt for six events"),
  ("M/J 2022", "11", "6(a)(i), (ii)", "5 + 5", "The role of the registers in the F-E cycle; when interrupts are detected and handled"),
  ("O/N 2022", "11", "5(c), (d)", "2 + 2", "The purpose of an interrupt; two causes of a software interrupt"),
  ("O/N 2022", "13", "4(a)(ii)", "1", "When interrupts are detected during the F-E cycle"),
  ("O/N 2022", "13", "2(a), (b)", "3 + 5", "Describe three RTN steps; how interrupts are handled"),
  ("M/J 2023", "11", "6", "5", "How the computer handles the interrupt from a key press"),
  ("O/N 2023", "13", "9(b), (c), (d)", "4 + 1 + 3", "Complete RTN steps; a software interrupt; the stages of interrupt handling"),
  ("M/J 2025", "12", "1(c)", "4", "How an interrupt from an input device is detected and handled"),
  ("M/J 2025", "13", "2(a)(ii)", "4", "The stages of the F-E cycle in RTN")]

past = '''  <p class="note">The fetch stage in RTN and the interrupt handling steps are asked almost every series; the interrupt marks come from the same list of points in different wording. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("w21", "11/13", "Q6(a)"), "4 marks", "Complete",
  "There are two errors in the following register transfer notation for the fetch-execute cycle. Line 1: MAR ← [PC]. Line 2: PC ← [PC] − 1. Line 3: MDR ← [MAR]. Line 4: CIR ← [MDR]. Complete the table by identifying the line number of each error, describing the error and writing the correct statement.", "Line 2: incremented, not decremented. Line 3: contents of the address in the MAR.",
  "<p>" + mks(["Line 2: the PC should be incremented, not decremented", "Line 2 correct statement: PC ← [PC] + 1", "Line 3: it should be the contents of the address in the MAR", "Line 3 correct statement: MDR ← [[MAR]]"]) + "</p>", "Correcting line 4 as well. CIR ← [MDR] is right.") + peq(SRC("w21", "12", "Q7(a)"), "3 marks", "Tick",
  "Tick one box in each row to identify whether each event is a hardware interrupt or a software interrupt: buffer full; printer is out of paper; user has pressed a key on the keyboard; division by zero; power failure; stack overflow.", "Devices are hardware; errors in a program are software.",
  "<p>One mark per pair of rows: " + mks(["Hardware: buffer full, printer out of paper, key pressed, power failure", "Software: division by zero, stack overflow"]) + "</p>", None) + peq(SRC("s22", "11", "Q6(a)"), "5 + 5 marks", "Describe",
  "A computer system is designed using the basic Von Neumann model. (i) Describe the role of the registers in the F-E cycle. (ii) Describe when interrupts are detected in the F-E cycle and how they are handled.", "PC, MAR, MDR, CIR roles. Detection at the end of a cycle, priority, stack, ISR.",
  "<p><b>(i)</b> Any five: " + mks(["The Program Counter holds the address of the next instruction", "and its contents are incremented each cycle", "The MAR holds the address to fetch the data from (taken from the PC)", "The MDR holds the data at the address in the MAR", "The instruction is transferred to the CIR for decoding and execution"]) + "</p><p><b>(ii)</b> Detected: " + mks(["At the start or end of an F-E cycle"], "a") + " Handled (max 4): " + mks(["Priority is checked", "If lower priority than the current process, continue with the F-E cycle", "If higher, the state of the current process (the registers) is stored on the stack", "The type of interrupt is identified and the appropriate ISR is called", "When the ISR is finished, check for further higher priority interrupts", "Otherwise load the data from the stack and continue with the process"], "b") + "</p>", "Writing that the processor stops. It checks priority and stores the registers.") + peq(SRC("w22", "11", "Q5(c)(d)"), "2 + 2 marks", "Describe / Identify",
  "(c) Describe the purpose of an interrupt in a computer system. (d) Identify two causes of a software interrupt.", "A signal seeking attention. Division by zero, invalid memory, index out of bounds, stack overflow.",
  "<p><b>(c)</b> " + mks(["To send a signal from a device or process", "seeking the attention of the processor"]) + "</p><p><b>(d)</b> Any two: " + mks(["Division by zero or a run-time error in a program", "An attempt to access an invalid memory location", "Array index out of bounds", "Stack overflow"], "a") + "</p>", None) + peq(SRC("w22", "13", "Q4(a)(ii), Q2"), "1 + 3 + 5 marks", "State / Describe",
  "(Q4a ii) State when interrupts are detected during the F-E cycle. (Q2a) Describe each of the steps PC ← [PC] + 1, MDR ← [[MAR]], MAR ← [PC]. (Q2b) Explain how interrupts are handled during the F-E cycle.", "After the execute stage. The three steps. Priority, stack, ISR.",
  "<p><b>Q4(a)(ii)</b> " + mks(["After completion of the execute stage, before the cycle begins"]) + "</p><p><b>Q2(a)</b> " + mks(["PC ← [PC] + 1: the address in the PC is incremented", "MDR ← [[MAR]]: the data in the address held in the MAR is copied to the MDR", "MAR ← [PC]: the contents of the PC are copied to the MAR"], "a") + "</p><p><b>Q2(b)</b> Any five: " + mks(["Check for an interrupt at the start or end of the F-E cycle", "Priority is checked", "If lower priority, continue the F-E cycle", "If higher, the registers are stored on the stack", "The location or type of interrupt is identified", "The appropriate ISR is called", "When finished, check for further higher priority interrupts", "Otherwise load the data from the stack and continue with the next cycle"], "b") + "</p>", None) + peq(SRC("s23", "11", "Q6"), "5 marks", "Explain",
  "An interrupt is generated when a key is pressed on a computer keyboard. Explain how the computer handles this interrupt.", "Flag, end of cycle, priority, stack, ISR, restore.",
  "<p>Any five: " + mks(["An interrupt flag is raised in the interrupt register", "At the end of the current F-E cycle (or at the start of the next)", "The system checks the interrupt register for higher priority interrupts than the current process", "If true, it stores the current contents of the registers on the stack", "The appropriate ISR for the key press is called", "The input data from the keyboard is processed", "The contents of the registers are restored from the stack", "and control is passed back to the previous process"]) + "</p>", None) + peq(SRC("w23", "13", "Q9(b)(c)(d)"), "4 + 1 + 3 marks", "Complete / State",
  "(b) Complete the table of F-E steps and descriptions: the missing step 'The address in PC is incremented'; MDR ← [[MAR]]; MAR ← [PC]; the missing step 'The contents of MDR are copied into CIR'. (c) State one cause of a software interrupt. (d) Complete the interrupt stages by writing the letter of the missing statements: 1 At the end of each F-E cycle, the processor checks if an interrupt flag is set. 2 ... 3 If the interrupt priority is high enough, the processor saves the current contents of the registers. 4 ... 5 When servicing of the interrupt is complete, the processor restores the registers. 6 ... Statements: A The address of the ISR is loaded into the PC. B Lower priority interrupts are re-enabled. C The device causing the interrupt transfers data to the CPU. D The processor identifies the source of the interrupt and checks the priority.", "PC ← [PC] + 1 and CIR ← [MDR]. Order: D, A, B.",
  "<p><b>(b)</b> " + mks(["PC ← [PC] + 1", "The data in the location pointed to by the MAR is copied to the MDR", "The contents of the PC are copied to the MAR", "CIR ← [MDR]"]) + "</p><p><b>(c)</b> " + mks(["Division by zero, a run-time error, out of memory bounds, a program requesting an external device, or a buffer overflow"], "a") + "</p><p><b>(d)</b> " + mks(["2: D", "4: A", "6: B"], "b") + "</p>", "Putting B before A. Lower priority interrupts are only re-enabled at the end.") + peq(SRC("s25", "12", "Q1(c)"), "4 marks", "Explain",
  "Explain how an interrupt from an input device will be detected and handled in the F-E cycle.", "Check at start or end, priority, stack, ISR, restore.",
  "<p>Any four: " + mks(["At the start or end of the F-E cycle the interrupt register is checked", "The priority of any interrupts waiting is checked", "If the priority is higher than the current process, the contents of the registers are stored on the stack", "The relevant ISR is called to process the interrupt", "When the ISR has finished, a further check is made for higher priority interrupts", "If none, the register contents are restored and the next F-E cycle continues"]) + "</p>", None) + peq(SRC("s25", "13", "Q2(a)(ii)"), "4 marks", "Write",
  "The processor runs the Fetch-Execute cycle. Write the stages of the F-E cycle using register transfer notation.", "Four steps in the right order.",
  "<p>" + mks(["MAR ← [PC] and PC ← [PC] + 1", "MDR ← [[MAR]]", "CIR ← [MDR]", "In the correct order"]) + "</p>", "Writing MDR before MAR. The address must be in the MAR before the data can be fetched.")

review = req("2 marks", "Explain", "Explain why the PC is incremented during the fetch stage.", "Ready for the next instruction.", "<p>" + mks(["So that the PC holds the address of the next instruction", "which will be fetched in the next cycle"]) + "</p>", None) + req("3 marks", "Describe", "Describe what happens to the registers when a higher priority interrupt is detected.", "Stack and restore.", "<p>" + mks(["The contents of the registers are stored on the stack", "The ISR runs", "The registers are restored from the stack afterwards so the process continues"]) + "</p>", None) + req("2 marks", "State", "State two examples of a hardware interrupt.", "Key press, power failure.", "<p>" + mks(["A key pressed", "Power failure, printer out of paper or buffer full"]) + " (any two)</p>", None) + req("2 marks", "Explain", "Explain why the interrupt is checked after the execute stage rather than in the middle of an instruction.", "Complete instructions.", "<p>" + mks(["The instruction that is running is finished first", "so the registers hold a consistent state that can be stored and restored"]) + "</p>", None) + req("4 marks", "Write", "Write the RTN for the fetch stage and say what the CU does next.", "RTN then decode.", "<p>" + mks(["MAR ← [PC]", "PC ← [PC] + 1 and MDR ← [[MAR]]", "CIR ← [MDR]", "The CU decodes the instruction in the CIR"]) + "</p>", None)

tips = tips_html([
  ("Fetch in four steps.", "MAR←[PC]; PC←[PC]+1; MDR←[[MAR]]; CIR←[MDR]."),
  ("Increment, not decrement.", "And double brackets for MDR."),
  ("Check at the end of the cycle.", "After execute, before the next fetch."),
  ("Priority first.", "Lower: carry on. Higher: handle it."),
  ("Stack, ISR, restore.", "The three nouns of every interrupt answer."),
  ("Hardware or software.", "Devices against errors in a program."),
], [("RTN", "Register transfer notation: a way of writing register moves."), ("an interrupt", "A signal seeking the attention of the processor."), ("the stack", "Where registers are stored while an ISR runs."), ("an ISR", "The routine that handles the interrupt.")],
  [("State", "Short answer."), ("Describe", "Several points."), ("Explain", "Reasons as well."), ("Complete", "Fill in the table.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const R = (x, y, t, v, on) => SV.rect(x, y, 120, 44, on ? "f3" : "cell", { rx: 6 }) + SV.text(x + 60, y + 18, t, "sm", { "text-anchor": "middle" }) + SV.text(x + 60, y + 36, v, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" });
    const pc = k >= 2 ? 101 : 100; let o = R(20, 20, "PC", pc, k === 2 || k === 1) + R(180, 20, "MAR", k >= 1 ? 100 : "", k === 1 || k === 3) + R(340, 20, "MDR", k >= 3 ? "LDM #5" : "", k === 3 || k === 4) + R(500, 20, "CIR", k >= 4 ? "LDM #5" : "", k === 4);
    o += SV.text(300, 110, ["", "MAR ← [PC]", "PC ← [PC] + 1", "MDR ← [[MAR]]", "CIR ← [MDR]"][k], "lbl bd t3", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stA"), { w: 640, h: 130, label: "Fetch", base: { i: 0 }, draw, tween: 100, dwell: 2500, steps: [{ cap: "The PC holds 100, the address of the next instruction.", s: { i: 0 } }, { cap: "The contents of the PC are copied to the <b>MAR</b>.", s: { i: 1 } }, { cap: "The PC is <b>incremented</b>, ready for the next instruction.", s: { i: 2 } }, { cap: "The data at the address in the MAR is copied to the <b>MDR</b> (the double brackets).", s: { i: 3 } }, { cap: "The MDR contents are copied to the <b>CIR</b>. The CU then decodes it.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, w, t, on) => SV.rect(x, y, w, 40, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + w / 2, y + 26, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" });
    let o = B(20, 30, 130, "running process", k <= 1 || k >= 6) + B(200, 30, 130, "F-E cycle ends", k === 1) + B(380, 30, 150, "check interrupt flag", k === 2) + B(380, 90, 150, "registers to stack", k === 3) + B(200, 90, 130, "ISR runs", k === 4) + B(20, 90, 130, "registers restored", k >= 5);
    return o; };
  Lib.stepper($("#stB"), { w: 560, h: 150, label: "Interrupt handling", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "A process is running its F-E cycles.", s: { i: 0 } }, { cap: "A key is pressed; an interrupt flag is set. The current cycle finishes.", s: { i: 1 } }, { cap: "The processor <b>checks the interrupt register</b> and the interrupt's priority.", s: { i: 2 } }, { cap: "Higher priority: the <b>registers are stored on the stack</b>.", s: { i: 3 } }, { cap: "The <b>ISR</b> for the key press runs.", s: { i: 4 } }, { cap: "The registers are <b>restored from the stack</b>.", s: { i: 5 } }, { cap: "The process continues with the next F-E cycle.", s: { i: 6 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const lvl = (y, t, p, on) => SV.rect(40, y, 400, 34, on ? "f3" : "cell", { rx: 6 }) + SV.text(52, y + 22, t + " (priority " + p + ")", "lbl", { style: "font-size:13px" });
    return lvl(20, "Power failure", 5, k === 3) + lvl(62, "Keyboard key press", 3, k === 2) + lvl(104, "Running program", 2, k <= 1) + SV.text(250, 165, ["", "", "key press: higher than the program, so it interrupts", "power failure outranks everything"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); };
  Lib.stepper($("#stC"), { w: 480, h: 180, label: "Priority", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "Interrupts have priorities.", s: { i: 0 } }, { cap: "A running program has priority 2.", s: { i: 1 } }, { cap: "A key press (3) is higher, so it <b>interrupts</b> the program.", s: { i: 2 } }, { cap: "A power failure (5) is higher still and is dealt with first.", s: { i: 3 } }] });
})();

(function () {
  const prog = ["LDM #5", "ADD #3", "STO 200", "END"]; let st;
  const reset = () => { st = { pc: 100, mar: "", mdr: "", cir: "", acc: 0, mem200: 0, k: 0, log: ["Ready: PC = 100."] }; paint(); };
  const step = () => { const s = st; if (s.done) return; const ph = s.k % 5;
    if (ph === 0) { s.mar = s.pc; s.log.push("MAR ← [PC]: MAR = " + s.mar); }
    else if (ph === 1) { s.pc++; s.log.push("PC ← [PC] + 1: PC = " + s.pc); }
    else if (ph === 2) { s.mdr = prog[s.mar - 100]; s.log.push("MDR ← [[MAR]]: MDR = " + s.mdr); }
    else if (ph === 3) { s.cir = s.mdr; s.log.push("CIR ← [MDR]: CIR = " + s.cir); }
    else { const [op, a] = s.cir.split(" "); if (op === "LDM") s.acc = +a.slice(1); if (op === "ADD") s.acc += +a.slice(1); if (op === "STO") s.mem200 = s.acc; if (op === "END") s.done = true; s.log.push("Decode and execute " + s.cir + (op === "END" ? ": stop." : ": ACC = " + s.acc + (op === "STO" ? ", location 200 = " + s.mem200 : "")) ); }
    s.k++; paint(); };
  const paint = () => { const s = st; const R = (n, v) => `<span style="display:inline-block;min-width:96px;border:1px solid var(--border);border-radius:8px;padding:6px 10px;margin:3px"><span class="sm">${n}</span><br><b>${v === "" ? "·" : v}</b></span>`;
    $("#feR").innerHTML = R("PC", s.pc) + R("MAR", s.mar) + R("MDR", s.mdr) + R("CIR", s.cir) + R("ACC", s.acc);
    $("#feM").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Address</th><th>Contents</th></tr>' + prog.map((p, i) => `<tr style="${s.mar === 100 + i && s.k % 5 !== 0 ? "background:var(--accent-soft);font-weight:700" : ""}"><td>${100 + i}</td><td>${p}</td></tr>`).join("") + `<tr><td>200</td><td>${s.mem200}</td></tr></table></div>`;
    $("#feL").innerHTML = s.log.slice(-3).join("<br>"); };
  $("#fe_step").onclick = step; $("#fe_reset").onclick = reset; reset();
})();
btnTable("iB", "iO", [
  ["A key is pressed", "Hardware", "A device asks for attention"],
  ["The printer is out of paper", "Hardware", "A device event"],
  ["Division by zero", "Software", "Error in the program"],
  ["Stack overflow", "Software", "Program uses too much stack"],
  ["Power failure", "Hardware", "Highest priority"],
  ["Array index out of bounds", "Software", "Invalid access in the program"]
], ["Event", "Type", "Why"]);
(function () {
  let p = 3; const cur = 2; const paint = () => { $("#pV").innerHTML = p > cur ? `The interrupt (priority <b>${p}</b>) is higher than the running process (<b>${cur}</b>): the registers are <b>stored on the stack</b> and the <b>ISR</b> runs.` : `The interrupt (priority <b>${p}</b>) is not higher than the running process (<b>${cur}</b>): the F-E cycle <b>continues</b> and the interrupt waits.`; };
  Lib.slider($("#pS"), { id: "p1", label: "Interrupt priority (running process is 2) ", min: 1, max: 5, value: p, fmt: (x) => x, onInput: (v) => { p = v; paint(); } }); paint();
})();
''' + _prjs

finish("as-4-1-3-fetch-execute-interrupts", "as413", "The Fetch-Execute Cycle and Interrupts",
  "The fetch-execute cycle in register transfer notation, a step-through simulator, and how interrupts are detected and handled with the stack and ISR, with animations, labs and the real Paper 1 questions from 2021 to 2026.",
  "4.1.3", "4 · Processor fundamentals", "section 4.1 Central Processing Unit architecture", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on the fetch-execute cycle and interrupts (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
