"""A Level CS syllabus 16.1.2: process management, process states and interrupt handling. Run: python3 tools/artifact-kit/mk_ac1612.py"""
from ak16 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>process</b> is a program that is being executed, together with its data and the values in the registers. A process is always in one of three states: <b>running</b> (using the CPU), <b>ready</b> (able to run and waiting for the CPU) or <b>blocked</b> (waiting for an input or output operation or some other event). A running process moves to ready when its <b>time slice runs out</b> or a higher-priority process <b>pre-empts</b> it, and to blocked when it must wait for I/O; a blocked process becomes ready when the event it waited for has happened. The <b>kernel</b> acts as the <b>interrupt handler</b>: it saves the state of the running process, uses an interrupt table to find the right routine, runs it, then restores the state. This is how <b>low-level scheduling</b> reacts to events such as a timer or a finished disk transfer.</p></div>

  <h2>1 · Processes and multi-tasking</h2>
  <p>A <b>program</b> is a set of instructions stored on disk. A <b>process</b> is a program that has been loaded and is being run. With <b>multi-tasking</b> there may be many processes at once but, on a processor with one core, only one can be using the CPU at any instant. The OS keeps a record of each process (its state, the program counter, the register contents, its priority) so that a process can be stopped and later carry on exactly where it left off.</p>

  <h2>2 · The three process states</h2>
  <div class="tw"><table class="t">
    <tr><th>State</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Running</b></td><td>The CPU has been allocated and the process is being executed.</td><td>A word processor is checking spelling.</td></tr>
    <tr><td><b>Ready</b></td><td>The process could run and is waiting in the ready queue for a slice of CPU time.</td><td>A music player waiting its turn, or one that was pre-empted by a higher-priority process.</td></tr>
    <tr><td><b>Blocked</b></td><td>The process is waiting for an I/O operation or other event to be completed, so it cannot run even if the CPU is free.</td><td>A program waiting for the user to type, or for a file to load from disk.</td></tr>
  </table></div>
  <h3>Changing state</h3>
  <ul>
    <li><b>Ready → running</b>: the scheduler picks the process and gives it the CPU.</li>
    <li><b>Running → ready</b>: the process's <b>time slice has expired</b> (round robin), a <b>higher-priority process</b> arrives in the ready queue and pre-empts it, or an <b>interrupt</b> arrives and the running process is pre-empted. The process is not waiting for anything: it could run again at once.</li>
    <li><b>Running → blocked</b>: the process needs input or output that will take time, so it waits for the event.</li>
    <li><b>Blocked → ready</b>: the event has happened (the I/O is complete); the process joins the ready queue. It never goes straight from blocked to running.</li>
  </ul>

  <h2>3 · Interrupts and the kernel</h2>
  <p>An <b>interrupt</b> is a signal to the processor that something needs attention at once: a timer, a key press, a disk finishing a transfer, a hardware fault. The <b>kernel</b> acts as the <b>interrupt handler</b>:</p>
  <ol>
    <li>The kernel receives a <b>signal</b> when the interrupt is generated.</li>
    <li>It checks the <b>priority</b> of the interrupt against the process that is running. If the interrupt has higher priority the system enters <b>kernel mode</b>.</li>
    <li>It <b>saves the state</b> of the interrupted process (the contents of the registers, including the program counter) on the kernel stack.</li>
    <li>It consults the <b>interrupt dispatch table</b> (also called the interrupt vector table, IVT, or interrupt descriptor table, IDT), which maps each interrupt to its <b>interrupt service routine (ISR)</b>, and runs that routine.</li>
    <li>When the ISR has finished the kernel <b>restores the state</b> of the process, which carries on, or the scheduler picks another process.</li>
  </ol>
  <h3>Interrupts and low-level scheduling</h3>
  <p>The low-level scheduler (dispatcher) is the part of the OS that moves processes between the ready and running states. It is driven by interrupts: a <b>timer interrupt</b> marks the end of a time slice, an <b>I/O interrupt</b> tells the OS that a blocked process can become ready, and a priority interrupt can pre-empt the running process. Handling the interrupts by priority ensures that critical events are dealt with without delay.</p>

  <h2>4 · Common ways to lose marks</h2>
  <ul>
    <li>Saying a process goes from blocked straight to running. It goes to ready first and waits for the scheduler.</li>
    <li>Describing "ready" as waiting for input. That is blocked; ready means able to run, waiting for the CPU.</li>
    <li>Describing what the interrupt is for, instead of what the kernel does: receive the signal, check priority, save the state, look up the ISR, restore the state.</li>
    <li>Forgetting that the state of the interrupted process has to be saved and restored.</li>
    <li>Giving only "time ran out" for running to ready. Other valid reasons: a higher-priority process arrives, or an interrupt pre-empts it.</li>
  </ul>
'''

watch = '''
  <h2>1 · One process through its states</h2>
  <p>Press Play. The highlighted box is the state the process is in.</p>
  <div id="stA"></div>
  <h2>2 · The kernel handles an interrupt</h2>
  <div id="stB"></div>
  <h2>3 · A higher-priority process pre-empts</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Move a process between states</h2>
  <p>Use the buttons. Only the changes that are possible from the current state are enabled.</p>
  <div class="card"><div id="stL"></div><div class="btnrow" id="stB1"></div><div class="verdict" id="stV"></div></div>

  <h2>Lab 2 · Four processes and one CPU</h2>
  <p>Only one process can be running. Click a process to give it the CPU: the others return to ready, or stay blocked.</p>
  <div class="card"><div id="pL"></div><div class="verdict" id="pV"></div></div>

  <h2>Lab 3 · Does the interrupt win?</h2>
  <p>Choose the priority of the running process and of the interrupt.</p>
  <div class="card"><div id="iS1"></div><div id="iS2"></div><div class="verdict" id="iV"></div></div>
'''

practise = '''
  <h2>1 · Which process state?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which change of state?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Put the steps of interrupt handling in order</h2><div id="o1" class="card"></div>
  <h2>5 · Working out</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A download that stalls", "A program waiting for data from the network is blocked. It does not use the CPU while it waits, so other programs run faster.", "blocked means waiting for an event.") +
rw("Typing while a video plays", "Each key press is an interrupt. The kernel saves the video player's state, passes the key to the editor, then lets the video carry on.", "the kernel saves and restores state around an interrupt.") +
rw("The spinning wheel", "A program that stops responding is usually waiting for an event that never arrives, so it stays blocked.", "a blocked process cannot run until its event happens.") +
rw("Fire alarm in a building", "The fire alarm interrupts everything. Work stops, people follow the alarm routine, and normal work resumes afterwards. The higher-priority event wins.", "interrupts are handled by priority.") +
rw("A queue at a till", "People waiting in the queue are ready; the one being served is running; a person who has gone to find the price of something is blocked until they come back.", "ready, running and blocked.")
)

where = [
  ("O/N 2023", "31, 33", "7(b), (c)", "1 + 2", "Identify the third process state; when a process changes from running to ready"),
  ("O/N 2024", "32", "9(a)", "2", "How the kernel acts as an interrupt handler"),
  ("M/J 2025", "32", "5(a)", "3", "Identify three process states"),
  ("O/N 2025", "32", "5(a), (b)", "2 + 3", "How interrupt handling is used in low-level scheduling; a reason for each process state"),
  ("M/J 2021", "31, 32, 33", "3(a)", "5", "Interrupt handling and scheduling as OS terms (on the 16.1.1 page)")]

past = '''  <p class="note">Process states and interrupt handling are asked in Paper 3 almost every year. The states question is usually a straight recall mark; the interrupt question is about what the kernel does. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s25", "32", "Q5(a)"), "3 marks", "Identify",
  "The management and scheduling of processes are tasks carried out by an operating system. Identify three process states.",
  "Running, ready and blocked.",
  "<p>" + mks(["Running state", "Ready state", "Blocked state"]) + "</p>", "Writing 'waiting' for blocked, 'idle' or 'sleeping'. Use the syllabus words: running, ready, blocked.") + peq(SRC("w23", "31/33", "Q7(b)(c)"), "1 + 2 marks", "Identify / Outline",
  "Two of the process states are the running state and the ready state. (b) Identify one other process state. (c) Outline conditions under which a process could change from the running state to the ready state.",
  "(c) Time slice, higher priority, interrupt.",
  "<p><b>(b)</b> " + mks(["Blocked (state)"]) + "</p><p><b>(c)</b> Any two: " + mks(["When the time slice of the running process expires (round robin)", "When a process with a higher priority is in the ready queue, so the running process is pre-empted", "When an interrupt arrives at the CPU and the running process is pre-empted"]) + "</p>", "Saying the process moves to ready because it is waiting for input. That is blocked. A process is ready when it could run but has lost the CPU.") + peq(SRC("w25", "32", "Q5"), "2 + 3 marks", "Describe / Complete",
  "(a) Describe how interrupt handling is used in low-level scheduling. (b) In process management, a process can be in one of three process states: running, ready or blocked. Complete the table to identify one reason why a process could be in each of the three states." + '<div class="tw"><table class="t"><tr><th>Process state</th><th>Reason</th></tr><tr><td>running</td><td></td></tr><tr><td>ready</td><td></td></tr><tr><td>blocked</td><td></td></tr></table></div>',
  "(a) priority, critical events, the interrupt table, the ISR.",
  "<p><b>(a)</b> Any two: " + mks(["The low-level scheduler manages the handling of interrupts based on priority", "ensuring that critical events are handled without delay", "It uses an Interrupt Vector Table (IVT) or Interrupt Descriptor / Dispatch Table (IDT) lookup", "to map the interrupt to the specific handling routine or ISR"]) + "</p><p><b>(b)</b> One mark per correct reason: " + mks(["running: CPU time has been allocated and the process is being executed", "ready: the process is waiting in the ready queue for a slice of CPU time; it could run, or it was pre-empted by a higher-priority process", "blocked: the process is waiting for an I/O operation, or some event, to be completed"]) + "</p>", "Giving the same reason for ready and blocked. Ready means it could run now; blocked means it cannot until an event happens.") + peq(SRC("w24", "32", "Q9(a)"), "2 marks", "Outline",
  "The kernel is the central component of an Operating System (OS). Outline how the kernel of an OS acts as an interrupt handler.",
  "Receive, check priority, look up the table, save and restore state.",
  "<p>Any two: " + mks(["The kernel receives a signal when an interrupt is generated", "It checks the priority and reviews the status or priority of the current interrupts", "The system enters kernel mode if the interrupt is of higher priority than the current process", "The kernel consults the interrupt dispatch table (IDT)", "and saves the state of the interrupted process, the contents of the registers, on the kernel stack", "The kernel restores the process state, for example the register contents, once the interrupt has been serviced"]) + "</p>", "Writing about what the interrupt is (a signal from a device) and not what the kernel does with it.")

review = req("3 marks", "Describe", "A process is running. It asks for data from the disk. Describe what happens to the process state, and then when the data arrives.", "Running, blocked, ready.", "<p>" + mks(["The process moves from running to blocked because it must wait for the I/O", "When the I/O completes the process moves to ready, not straight to running", "It waits in the ready queue until the scheduler gives it the CPU, then it is running again"]) + "</p>", None) + req("2 marks", "Explain", "Explain why the state of the interrupted process is saved before an interrupt service routine runs.", "What would be lost otherwise?", "<p>" + mks(["The registers and program counter hold the process's progress, and the ISR will overwrite them", "Restoring them afterwards lets the process carry on exactly where it stopped"]) + "</p>", None) + req("2 marks", "State", "State two events that can cause a running process to be moved to the ready state.", "Time, priority.", "<p>" + mks(["Its time slice expires", "A process of higher priority joins the ready queue (it is pre-empted), or an interrupt arrives"]) + "</p>", None) + req("3 marks", "Outline", "Outline the steps the kernel takes when a key-press interrupt arrives while a game is running.", "Save, ISR, restore.", "<p>" + mks(["The kernel saves the game's state (registers and program counter)", "It uses the interrupt table to find and run the keyboard's interrupt service routine", "It restores the game's state so it continues from where it stopped"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between the ready state and the blocked state.", "Could it run right now?", "<p>" + mks(["Ready: the process could run and is waiting for the CPU", "Blocked: the process cannot run until an event (such as I/O completing) happens"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on process states and interrupt handling (Paper 3), 2021 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Three states.", "Running, ready, blocked. Use those words."),
  ("Ready can run; blocked cannot.", "Ready is waiting for the CPU. Blocked is waiting for an event."),
  ("Blocked goes to ready.", "Never straight to running."),
  ("Running to ready: three causes.", "Time slice ends, higher priority arrives, interrupt."),
  ("Interrupt handling by the kernel.", "Signal, priority check, save state, table lookup, ISR, restore."),
  ("Name the table.", "Interrupt dispatch / vector table (IDT or IVT)."),
], [
  ("a process", "A program in execution."),
  ("blocked", "A process waiting for an I/O operation or event."),
  ("pre-empted", "A running process that is stopped so another can run."),
  ("an ISR", "The interrupt service routine that handles one kind of interrupt."),
], [("Identify", "Give the names only."), ("Outline", "Give the main points briefly."), ("Describe", "Say what happens, in several points."), ("Complete", "Fill the table with a reason for each row.")]) + FC

js = AKJS + AK20JS + r'''
const SB = { ready: { x: 30, name: "Ready" }, running: { x: 270, name: "Running" }, blocked: { x: 510, name: "Blocked" } };
function stateDiagram(cur, hot) {
  let o = "";
  Object.entries(SB).forEach(([k, b]) => (o += SV.rect(b.x, 44, 140, 46, k === cur ? "cell-ok" : "cell", { rx: 10 }) + SV.text(b.x + 70, 73, b.name, "lbl bd", { "text-anchor": "middle" })));
  const arrow = (id, d, hd) => SV.path(d, "ax", { style: "stroke:" + (hot === id ? "var(--accent)" : "var(--muted)") + ";stroke-width:" + (hot === id ? 3.5 : 2) }) + hd;
  o += arrow("dispatch", "M170,58 H264", SV.arrowHead(270, 58, "r", hot === "dispatch" ? "dot1" : "arr"));
  o += arrow("preempt", "M270,78 H176", SV.arrowHead(170, 78, "l", hot === "preempt" ? "dot1" : "arr"));
  o += arrow("wait", "M410,66 H504", SV.arrowHead(510, 66, "r", hot === "wait" ? "dot1" : "arr"));
  o += arrow("ready", "M580,90 V150 H100 V96", SV.arrowHead(100, 90, "u", hot === "ready" ? "dot1" : "arr"));
  o += SV.text(220, 40, "dispatch", "sm", { "text-anchor": "middle" }) + SV.text(222, 106, "time slice ends / pre-empted", "sm", { "text-anchor": "middle" }) + SV.text(460, 54, "waits for I/O", "sm", { "text-anchor": "middle" }) + SV.text(340, 172, "I/O complete", "sm", { "text-anchor": "middle" });
  return o;
}
(function () {
  const seq = [["ready", null, "The process is loaded and waits in the <b>ready</b> queue."], ["running", "dispatch", "The scheduler gives it the CPU: <b>ready → running</b>."], ["ready", "preempt", "Its time slice ends: <b>running → ready</b>. It could still run, so it waits for the CPU."], ["running", "dispatch", "It is dispatched again: <b>ready → running</b>."], ["blocked", "wait", "It asks for data from the disk: <b>running → blocked</b>. It cannot run until the data arrives."], ["ready", "ready", "The disk finishes: <b>blocked → ready</b>, not straight to running."], ["running", "dispatch", "It gets the CPU again: <b>ready → running</b>."]];
  const draw = (s) => { const [c, h] = seq[Math.round(s.i)]; return stateDiagram(c, h); };
  Lib.stepper($("#stA"), { w: 700, h: 190, label: "Process states", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: seq.map((x, i) => ({ cap: x[2], s: { i } })) });
})();
(function () {
  const L = ["Process running", "Interrupt signal received", "Priority checked, kernel mode entered", "State of the process saved on the kernel stack", "Interrupt table looked up, ISR run", "State restored, process carries on"];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; L.forEach((t, i) => (o += SV.rect(20, 12 + i * 44, 400, 36, i === k ? "cell-warn" : i < k ? "cell-ok" : "cell", { rx: 8 }) + SV.text(34, 35 + i * 44, t, "lbl")));
    o += SV.text(480, 26, "kernel stack", "sm", { "text-anchor": "middle" }) + SV.rect(440, 36, 120, 38, k >= 3 && k < 5 ? "f3" : "cell", { rx: 6, ...op(k >= 3 && k < 5 ? 1 : 0.35) }) + (k >= 3 && k < 5 ? SV.text(500, 60, "registers, PC", "lbl", { "text-anchor": "middle" }) : "");
    o += SV.text(480, 108, "dispatch table", "sm", { "text-anchor": "middle" }) + SV.rect(440, 118, 120, 38, k === 4 ? "f1" : "cell", { rx: 6, ...op(k === 4 ? 1 : 0.35) }) + (k === 4 ? SV.text(500, 142, "→ keyboard ISR", "lbl", { "text-anchor": "middle" }) : ""); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 284, label: "Interrupt handling", base: { i: 0 }, draw, tween: 120, dwell: 2800, steps: [{ cap: "A process is running on the CPU.", s: { i: 0 } }, { cap: "A key is pressed: the kernel <b>receives the interrupt signal</b>.", s: { i: 1 } }, { cap: "It <b>checks the priority</b>. The interrupt is more important, so the system enters kernel mode.", s: { i: 2 } }, { cap: "It <b>saves the state</b> of the interrupted process (registers and program counter) on the kernel stack.", s: { i: 3 } }, { cap: "It looks the interrupt up in the <b>dispatch table</b> and runs the matching <b>interrupt service routine</b>.", s: { i: 4 } }, { cap: "The ISR is finished. The kernel <b>restores the saved state</b> and the process carries on.", s: { i: 5 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "CPU", "lbl bd") + SV.rect(20, 32, 170, 50, k >= 2 ? "cell-warn" : "cell-ok", { rx: 10 }) + SV.text(105, 63, k >= 2 ? "Process Z (priority 1)" : "Process A (priority 3)", "lbl bd", { "text-anchor": "middle" });
    o += SV.text(250, 22, "ready queue", "lbl bd"); const q = k === 0 ? ["B (2)", "C (3)"] : k === 1 ? ["Z (1)", "B (2)", "C (3)"] : k === 2 ? ["A (3)", "B (2)", "C (3)"] : ["B (2)", "C (3)", "A (3)"]; q.forEach((t, i) => (o += SV.rect(250 + i * 110, 32, 100, 50, k === 1 && i === 0 ? "cell-warn" : "cell", { rx: 8 }) + SV.text(300 + i * 110, 63, t, "lbl", { "text-anchor": "middle" })));
    if (k === 1) o += SV.text(20, 120, "Z has a higher priority (1 is highest) than A", "lbl bd t2", { style: "font-size:13px" }); if (k >= 2) o += SV.text(20, 120, "A was pre-empted: it moved to ready, not blocked", "lbl bd t2", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 600, h: 140, label: "Pre-emption", base: { i: 0 }, draw, tween: 120, dwell: 2800, steps: [{ cap: "Process A (priority 3) is running. B and C wait in the ready queue.", s: { i: 0 } }, { cap: "A new process Z with a higher priority joins the ready queue.", s: { i: 1 } }, { cap: "The scheduler <b>pre-empts</b> A and runs Z: <b>running → ready</b> for A.", s: { i: 2 } }, { cap: "A waits in the ready queue. It could run, so it is <b>ready</b>, not blocked.", s: { i: 3 } }] });
})();

(function () {
  let cur = "ready"; const log = [];
  const moves = { ready: [["dispatch", "Dispatch (give the CPU)", "running"]], running: [["preempt", "Time slice ends or pre-empted", "ready"], ["wait", "Wait for I/O", "blocked"]], blocked: [["ready", "I/O completes", "ready"]] };
  const paint = () => { $("#stL").innerHTML = '<svg viewBox="0 0 700 190" style="width:700px;max-width:100%;display:block">' + stateDiagram(cur, null) + "</svg>"; const b = $("#stB1"); b.innerHTML = "";
    Object.values(moves).flat().forEach(([id, t, to]) => { const x = document.createElement("button"); x.textContent = t; const ok = moves[cur].some((m) => m[0] === id); x.disabled = !ok; x.style.opacity = ok ? 1 : 0.35; x.onclick = () => { log.push(cur + " → " + to); cur = to; paint(); }; b.appendChild(x); });
    $("#stV").innerHTML = "State: <b>" + cur + "</b>." + (log.length ? " Moves so far: " + log.slice(-5).join(", ") + "." : " Dispatch the process to start.") + (cur === "blocked" ? " A blocked process can only go to ready, never straight to running." : ""); };
  paint();
})();
(function () {
  const P = [{ n: "A", s: "running" }, { n: "B", s: "ready" }, { n: "C", s: "blocked" }, { n: "D", s: "ready" }]; const el = $("#pL");
  const paint = () => { el.innerHTML = '<div class="btnrow"></div>'; const b = el.firstChild; P.forEach((p, i) => { const x = document.createElement("button"); x.textContent = "Process " + p.n + ": " + p.s; x.className = p.s === "running" ? "on" : ""; x.onclick = () => { if (p.s === "blocked") { p.s = "ready"; } else if (p.s === "ready") { P.forEach((q) => { if (q.s === "running") q.s = "ready"; }); p.s = "running"; } else { p.s = "blocked"; } paint(); }; b.appendChild(x); });
    const r = P.filter((p) => p.s === "running").length; $("#pV").innerHTML = "Running: <b>" + r + "</b> (a single CPU can run only one). Click a <b>ready</b> process to run it, a <b>running</b> process to block it (it waits for I/O), a <b>blocked</b> process to make it ready (its I/O is complete)."; };
  paint();
})();
(function () {
  let a = 3, b = 1;
  const paint = () => { $("#iV").innerHTML = "Running process priority <b>" + a + "</b>, interrupt priority <b>" + b + "</b> (1 is the highest): " + (b < a ? "the interrupt is <b>more important</b>. The kernel saves the process's state, runs the ISR, then restores the state." : "the interrupt is <b>not more important</b>, so the running process carries on and the interrupt waits."); };
  Lib.slider($("#iS1"), { id: "is1", label: "Running process priority ", min: 1, max: 5, value: a, fmt: (x) => x, onInput: (v) => { a = v; paint(); } });
  Lib.slider($("#iS2"), { id: "is2", label: "Interrupt priority ", min: 1, max: 5, value: b, fmt: (x) => x, onInput: (v) => { b = v; paint(); } }); paint();
})();
''' + CLASSIFY("cl1", "Which state is the process in?", ["Running", "Ready", "Blocked"],
  [("It is using the CPU now", 0), ("It is waiting in the queue for a turn on the CPU", 1), ("It is waiting for a file to finish loading", 2), ("It was stopped because a higher-priority process arrived", 1), ("It is waiting for the user to press a key", 2), ("CPU time has been allocated to it", 0)],
  "Running uses the CPU, ready could run, blocked is waiting for an event.") + CLASSIFY("cl2", "Is the change of state possible?", ["Possible", "Not possible"],
  [("Ready to running", 0), ("Running to blocked", 0), ("Blocked to ready", 0), ("Blocked to running", 1), ("Running to ready", 0), ("Ready to blocked", 1)],
  "Blocked goes to ready; ready goes only to running.") + MATCH([
  ["Interrupt", "A signal that something needs the processor's attention"], ["Kernel", "Receives the interrupt signal and starts the response"], ["ISR", "The routine that deals with one kind of interrupt"], ["Dispatch table", "Maps each interrupt to its service routine"], ["Pre-emption", "A running process is stopped so another can run"]]) + ORDER(
  "Put the steps of interrupt handling in order.",
  ["The kernel receives the interrupt signal", "The priority is checked and kernel mode entered", "The state of the running process is saved", "The ISR is found in the interrupt table and run", "The state is restored and the process carries on"],
  "Receive, priority, save, ISR, restore.") + CALC([
  {"q": "How many process states are there in the syllabus?", "a": 3, "unit": "", "tol": 0.01, "hint": "Running, ready, blocked.", "sol": "<b>3</b>."},
  {"q": "A single-core CPU has 5 processes. At most how many can be in the running state at once?", "a": 1, "unit": "", "tol": 0.01, "hint": "One CPU, one process.", "sol": "<b>1</b>."},
  {"q": "Process A is blocked. Its I/O completes. Which state does it move to? Enter 1 for running, 2 for ready.", "a": 2, "unit": "", "tol": 0.01, "hint": "Never straight to running.", "sol": "<b>2</b>: ready."},
  {"q": "A time slice is 10 ms and there are 4 ready processes in turn. How long until the first is given the CPU again after its slice (ms)?", "a": 30, "unit": "ms", "tol": 0.5, "hint": "The other three run for 10 ms each.", "sol": "<b>30</b> ms."},
  {"q": "A running process asks for disk data and later runs again. How many changes of state happen on the way (running to blocked, blocked to ready, ready to running)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Count the arrows.", "sol": "<b>3</b>."}]) + MCQ([
  ("A process waiting for a disk transfer is:", ["Running", "Ready", "Blocked", "Terminated"], 2, "Waiting for an event."),
  ("A running process's time slice expires. It moves to:", ["Blocked", "Ready", "Terminated", "Running"], 1, "Ready."),
  ("Where does the kernel save the interrupted process's state?", ["On the kernel stack", "In the monitor", "In the printer", "On paper"], 0, "On the kernel stack."),
  ("The interrupt dispatch table maps:", ["Files to folders", "Interrupts to their service routines", "Users to passwords", "Pages to frames"], 1, "Interrupt to ISR."),
  ("When is the state of the interrupted process restored?", ["Before the interrupt arrives", "After the ISR has finished", "Never", "When the computer is switched off"], 1, "After the ISR."),
  ("A higher-priority process arrives. The running process:", ["Is deleted", "Is pre-empted and goes to ready", "Goes to blocked", "Finishes first"], 1, "Pre-empted, ready.")], "qz1") + CARDS([
  ("Running", "CPU allocated, being executed."), ("Ready", "Could run; waiting in the ready queue."), ("Blocked", "Waiting for I/O or an event."), ("Running to ready", "Time slice ends, higher priority, interrupt."),
  ("Blocked to ready", "The event has happened."), ("Kernel as interrupt handler", "Signal, priority, save state, ISR, restore."), ("Dispatch table", "IVT / IDT: interrupt to ISR."), ("Low-level scheduler", "Moves processes between ready and running.")])

build("ac1612", "ac-16-1-2-process-states-interrupts", "Process States and Interrupt Handling", EYA("16.1.2"),
  "Processes, the running, ready and blocked states and the changes between them, and how the kernel handles interrupts for low-level scheduling; animations, labs and the real Paper 3 questions from 2023 to 2025.",
  dict(sub=CBK("Chapter 16 · System software, section 16.1 Purposes of an operating system"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
