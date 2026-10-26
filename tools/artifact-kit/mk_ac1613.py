"""A Level CS syllabus 16.1.3: scheduling routines (FCFS, SJF, SRT, round robin). Run: python3 tools/artifact-kit/mk_ac1613.py"""
import json
from ak16 import *

PA = [("P1", 0, 7), ("P2", 1, 4), ("P3", 2, 1), ("P4", 3, 4)]
PB = [("A", 0, 5), ("B", 2, 3), ("C", 4, 1), ("D", 6, 2)]
PC = [("P1", 0, 3), ("P2", 0, 6), ("P3", 0, 4), ("P4", 0, 2)]
sched_check([PA, PB, PC])
names = [p[0] for p in PA]


def plist(pr):
    return '<div class="tw"><table class="t mono"><tr><th>Process</th><th>Arrives</th><th>Burst time</th></tr>' + "".join(f"<tr><td>{n}</td><td>{a}</td><td>{b}</td></tr>" for n, a, b in pr) + "</table></div>"


def result(pr, algo, q=3, label=None):
    segs, st = schedule(pr, algo, q)
    avg = sum(v[2] for v in st.values()) / len(st)
    t = '<div class="tw"><table class="t mono"><tr><th>Process</th><th>Finishes</th><th>Turnaround</th><th>Waiting</th></tr>' + "".join(f"<tr><td>{n}</td><td>{v[0]}</td><td>{v[1]}</td><td>{v[2]}</td></tr>" for n, v in st.items()) + f"<tr><td><b>average</b></td><td></td><td></td><td><b>{avg:g}</b></td></tr></table></div>"
    return f"<h3>{label or algo}</h3>" + gantt(segs, [p[0] for p in pr]) + t


learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>With many processes ready to run and one CPU, the OS needs <b>scheduling</b> to choose which process runs next, so that the CPU is never idle, all processes get fair access and high-priority jobs finish first. The syllabus routines are <b>first come first served</b> (run in order of arrival, to completion), <b>shortest job first</b> (run the process with the shortest burst time, to completion), <b>shortest remaining time</b> (the pre-emptive form of shortest job first) and <b>round robin</b> (each process gets a fixed time slice in turn). Each has a benefit and a drawback: shortest job first and shortest remaining time give the lowest waiting times but can <b>starve</b> long processes, round robin is fair but swaps processes often, first come first served is simple but short jobs wait behind long ones. The <b>average waiting time</b> is the usual way to compare them.</p></div>

  <h2>1 · Why scheduling is needed</h2>
  <ul>
    <li>It makes <b>multi-tasking</b> possible: several processes appear to run at the same time.</li>
    <li>It keeps the <b>CPU busy</b> all the time, which reduces idle time.</li>
    <li>It gives all processes <b>fair access</b> to the CPU, and prevents <b>starvation</b> (a process never getting a turn).</li>
    <li>It allows <b>high-priority</b> jobs to be completed first.</li>
    <li>It keeps waiting times short and makes processes execute efficiently.</li>
  </ul>

  <h2>2 · Words to know</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th></tr>
    <tr><td><b>Burst time</b></td><td>The CPU time a process needs to finish.</td></tr>
    <tr><td><b>Waiting time</b></td><td>Time a process spends in the ready queue: turnaround time minus burst time.</td></tr>
    <tr><td><b>Turnaround time</b></td><td>Time from arrival to finishing.</td></tr>
    <tr><td><b>Throughput</b></td><td>Number of processes completed per unit of time.</td></tr>
    <tr><td><b>Pre-emptive</b></td><td>The scheduler can stop a running process before it has finished (time slice ended, or a better process arrived).</td></tr>
    <tr><td><b>Non-pre-emptive</b></td><td>A process keeps the CPU until it finishes or blocks.</td></tr>
    <tr><td><b>Time quantum (slice)</b></td><td>The fixed length of time each process may run in round robin.</td></tr>
    <tr><td><b>Starvation</b></td><td>A process is held back for ever because others are always chosen first.</td></tr>
  </table></div>

  <h2>3 · The four routines</h2>
  <div class="tw"><table class="t">
    <tr><th>Routine</th><th>Function</th><th>Benefit</th><th>Drawback</th></tr>
    <tr><td><b>First come first served (FCFS)</b></td><td>Processes are queued as they arrive and run one at a time, in that order. Non-pre-emptive.</td><td>Simple: no complex logic, little processor overhead; no starvation because every process eventually runs.</td><td>Short jobs wait behind long ones, so the average waiting time can be long.</td></tr>
    <tr><td><b>Shortest job first (SJF)</b></td><td>The process with the shortest burst time is chosen next and runs to completion. Non-pre-emptive.</td><td>Short jobs do not wait for long ones; the average waiting time is low and throughput is high.</td><td>Long jobs may starve if shorter ones keep arriving.</td></tr>
    <tr><td><b>Shortest remaining time (SRT)</b></td><td>The pre-emptive version of SJF: the process with the least time left runs. When a process with a shorter burst time arrives, the running process is replaced.</td><td>Short processes finish very quickly; waiting time is minimised.</td><td>Long processes may starve; many switches.</td></tr>
    <tr><td><b>Round robin (RR)</b></td><td>Each process runs for a fixed time quantum in turn; when its slice ends, its state is saved and it goes to the back of the queue. Pre-emptive.</td><td>Fair: no starvation, and a short response time for every process.</td><td>Many switches between processes; long jobs take longer overall; poor if the quantum is badly chosen.</td></tr>
  </table></div>

  <h2>4 · A worked example</h2>
  <p>Four processes arrive and need the CPU. Round robin uses a time quantum of 3.</p>
  ''' + plist(PA) + result(PA, "FCFS", label="First come first served") + result(PA, "SJF", label="Shortest job first") + result(PA, "SRT", label="Shortest remaining time") + result(PA, "RR", 3, label="Round robin (quantum 3)") + '''
  <p>Average waiting times: FCFS 6, SJF 5.25, SRT 3.25, round robin 7.5. SRT has the smallest average because short processes never wait behind long ones, but the long process P1 is pushed to the end. Round robin has a higher average here, but every process gets its first turn quickly.</p>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Writing only "it is fair" or "it is fast". Name the property: no starvation, shortest waiting time, a fixed time slice.</li>
    <li>Describing shortest job first as pre-emptive. SJF runs to completion; the pre-emptive routine is shortest remaining time.</li>
    <li>Giving no function for round robin: a fixed time quantum, state saved when the slice ends, the next process runs.</li>
    <li>Forgetting that a drawback of SJF and SRT is starvation of long processes.</li>
    <li>Mixing waiting time (in the queue) with burst time (CPU needed).</li>
  </ul>
'''

watch = '''
  <h2>1 · First come first served</h2>
  <p>Press Play. The bar shows who has the CPU; the caption shows who is waiting.</p>
  <div id="stA"></div>
  <h2>2 · Shortest remaining time</h2>
  <div id="stB"></div>
  <h2>3 · Round robin with a time quantum of 3</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Scheduling simulator</h2>
  <p>Choose a set of processes and a routine. The Gantt chart and the waiting times are worked out for you.</p>
  <div class="card"><div id="sP" class="btnrow"></div><div id="sA" class="btnrow"></div><div id="sQ"></div><div id="sO"></div></div>

  <h2>Lab 2 · Which routine suits?</h2>
  <div class="card"><div id="rB" class="btnrow"></div><div id="rO"></div></div>
'''

practise = '''
  <h2>1 · Which routine?</h2><div id="cl1" class="card"></div>
  <h2>2 · Benefit or drawback?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the routine to its function</h2><div id="m1" class="card"></div>
  <h2>4 · Put the round robin steps in order</h2><div id="o1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The queue at a canteen", "First come first served: the first person in the queue is served first. It is fair, but someone who only wants a drink waits behind a large order.", "FCFS has no starvation but short jobs may wait.") +
rw("The express till", "Shortest job first: customers with few items go first. Waiting is shorter overall, but a customer with a full trolley may be pushed back if express customers keep arriving.", "SJF risks starving long jobs.") +
rw("A teacher helping a class", "Round robin: the teacher gives each student two minutes, then moves to the next, and comes back round. Nobody is ignored, but no student gets a long uninterrupted time.", "fixed time slices, state saved between turns.") +
rw("A hospital emergency department", "Priority scheduling: the most urgent case is seen first and may interrupt a less urgent one (pre-emption).", "higher-priority jobs are completed first.") +
rw("Your computer running many apps", "Operating systems mix these ideas: time slices for fairness, priorities for important tasks, and short jobs quickly so the system feels responsive.", "real schedulers combine routines.")
)

where = [
  ("O/N 2022", "32", "9(a), 9(b)", "3 + 6", "Need for scheduling; describe shortest job first, round robin and first come first served and give a benefit of each"),
  ("M/J 2025", "31", "8(b)", "4", "Function of shortest remaining time and a benefit"),
  ("M/J 2025", "32", "5(b)", "4", "Function of shortest job first and a benefit"),
  ("M/J 2025", "33", "6(a), (b)", "2 + 4", "A reason scheduling is necessary; function of round robin and a benefit"),
  ("O/N 2025", "31", "4(a)", "2", "Identify two scheduling routines")]

past = '''  <p class="note">Scheduling has been examined in Paper 3 in Oct/Nov 2022, May/June 2025 (all three papers, each a different routine) and Oct/Nov 2025. There have been no scheduling calculations or Gantt charts in these papers; every question asks for a function, a benefit or a reason. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("w25", "31", "Q4(a)"), "2 marks", "Identify",
  "A scheduling routine determines how processes are managed by the operating system. Identify two scheduling routines.",
  "Any two of the four named in the syllabus.",
  "<p>Any two: " + mks(["Round robin", "Shortest job first", "First come first served", "Shortest remaining time"]) + "</p>", "Writing 'priority', 'FIFO' or 'multi-tasking'. Use the four names in the syllabus.") + peq(SRC("w22", "32", "Q9"), "3 + 6 marks", "Explain / Describe",
  "(a) Explain the need for scheduling in process management. (b) Describe these scheduling routines and identify a benefit for each one: shortest job first; round robin; first come first served.",
  "(b) two marks each: function and benefit.",
  "<p><b>(a)</b> Any three: " + mks(["Scheduling allows more than one program or task to appear to be executed at the same time (multi-tasking, multiprogramming)", "To allow high-priority jobs to be completed first", "To keep the CPU busy all the time", "to ensure that all processes execute efficiently", "and have reduced waiting times, fair access to the CPU and no starvation of some processes"]) + "</p><p><b>(b)</b> " + mks(["Shortest job first: processes are executed in ascending order of CPU time required, so short processes run first and then longer ones", "Benefit: increased throughput, because more processes can be executed in a smaller amount of time"]) + "<br>" + mks(["Round robin: each process is served by the CPU for a fixed time slice, so all processes get the same priority", "Benefit: starvation does not occur, because in each cycle every process gets a time slice"], "a") + "<br>" + mks(["First come first served: no complex logic, each process request is queued as it is received and executed one by one", "Benefit: starvation does not occur because every process will eventually run, or there is less processor overhead"], "n") + "</p>", "Describing shortest job first as 'the quickest process' without saying the processes run in ascending order of CPU time needed, and giving no benefit.") + peq(SRC("s25", "32", "Q5(b)"), "4 marks", "Describe",
  "Describe the function of the shortest job first scheduling routine and give a benefit of this routine.",
  "Function (up to three marks) and one benefit.",
  "<p>Function, up to three: " + mks(["The processes are queued as they arrive", "The process with the shortest time to complete (burst time) is selected first and executed", "The process continues until complete or put in a waiting state; it is non-pre-emptive", "The scheduler continues to choose shorter processes over longer ones if they keep being added, which can cause starvation for longer jobs"]) + "</p><p>Benefit, one: " + mks(["Shorter jobs do not have to wait for longer jobs; significantly reduces average waiting time; or higher throughput"], "a") + "</p>", "Calling it pre-emptive. A shortest job first process keeps the CPU until it is complete or waiting.") + peq(SRC("s25", "31", "Q8(b)"), "4 marks", "Explain",
  "Explain the function of the shortest remaining time scheduling routine and give a benefit of this routine.",
  "Shortest burst first, but pre-emptive.",
  "<p>Function, up to three: " + mks(["The processes are queued as they arrive", "Processes with the shortest burst time are executed first", "It is a pre-emptive scheduling routine: when a process with a shorter burst time arrives, the existing process is replaced by the shorter process", "The scheduler continues to choose shorter processes over longer ones, which can cause starvation for longer jobs"]) + "</p><p>Benefit, one: " + mks(["Processes with a short burst time are processed very quickly; or waiting time is minimised"], "a") + "</p>", "Leaving out that a newly arrived shorter process pre-empts the running one. That is what separates it from shortest job first.") + peq(SRC("s25", "33", "Q6"), "2 + 4 marks", "Describe / Explain",
  "(a) Describe one reason why scheduling is necessary in process management. (b) Explain the function of the round robin scheduling routine and give a benefit of this routine.",
  "(b) fixed time quantum, state saved, next process, plus a benefit.",
  "<p><b>(a)</b> Any two marks: " + mks(["Scheduling is required so all processes are executed in a timely manner", "and enables multi-tasking or multiprogramming", "to minimise CPU idle time", "to ensure no process is starved of resources, or fair access to resources", "ensures jobs are completed in order of priority"]) + "</p><p><b>(b)</b> Function, up to three: " + mks(["Processes are queued as they arrive", "It is a pre-emptive routine", "A fixed time quantum (equal time slice) is given to each process", "When a time slice ends the status of the process is saved and queued so it can continue next time", "The next process is executed for its time slice; its previous state is restored if applicable", "If a process completes within its time slice, the next process is executed"]) + "</p><p>Benefit, one: " + mks(["Reduces average response time by limiting each process to a fixed amount of time; or no starvation of resources"], "a") + "</p>", None)

review = req("2 marks", "Distinguish", "Distinguish between shortest job first and shortest remaining time.", "Pre-emption.", "<p>" + mks(["Shortest job first runs the chosen process to completion (non-pre-emptive)", "Shortest remaining time replaces the running process when a process with a shorter remaining time arrives (pre-emptive)"]) + "</p>", None) + req("3 marks", "Calculate", "Three processes arrive at time 0 with burst times P1 = 5, P2 = 2 and P3 = 3. Using first come first served, state the waiting time of each process and the average.", "P1 first.", "<p>" + mks(["P1 waits 0, P2 waits 5, P3 waits 7", "Total waiting = 12", "Average = 12 / 3 = 4"]) + "</p>", None) + req("3 marks", "Calculate", "For the same processes use shortest job first. State the order, each waiting time and the average.", "Shortest first: P2, P3, P1.", "<p>" + mks(["Order: P2, P3, P1", "Waiting: P2 = 0, P3 = 2, P1 = 5", "Average = 7 / 3 = 2.33 (shorter than FCFS)"]) + "</p>", None) + req("3 marks", "Explain", "Explain one drawback of round robin when the time quantum is very small.", "What happens at each switch?", "<p>" + mks(["The OS must switch between processes very often", "Each switch needs the state of the process to be saved and restored", "So much of the CPU time is spent switching instead of running the processes"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a long process may starve under shortest remaining time.", "Shorter processes keep arriving.", "<p>" + mks(["The scheduler always chooses the process with the least time left", "If shorter processes keep arriving, the long one is never chosen"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on scheduling (Paper 3), 2022 and 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Four routines.", "Round robin, shortest job first, first come first served, shortest remaining time."),
  ("Function plus benefit.", "Most questions want both. Learn one of each for every routine."),
  ("SJF runs to completion.", "SRT is the pre-emptive one: a shorter arrival replaces the running process."),
  ("Round robin: fixed time slice.", "State saved when the slice ends; the next process runs."),
  ("Starvation.", "SJF and SRT can starve long jobs; FCFS and round robin do not."),
  ("Waiting time is time in the queue.", "Turnaround minus burst."),
], [
  ("scheduling", "Choosing which process the CPU runs next."),
  ("burst time", "The CPU time a process needs."),
  ("pre-emptive", "The running process can be stopped before it finishes."),
  ("starvation", "A process never gets the CPU."),
], [("Identify", "Name them only."), ("Describe", "Say what it does in several points."), ("Explain", "Give the reasons and a benefit."), ("Calculate", "Show waiting or turnaround times.")]) + FC

js = AKJS + AK20JS + AK16JS + "const PRE = " + json.dumps({"A": PA, "B": PB, "C": PC}) + ";\n" + r'''
function ganttHtml(segs, names) {
  const w = (s, e) => e - s;
  return '<div class="gantt">' + segs.map(([s, e, n]) => `<div class="gb c${names.indexOf(n) % 5}" style="flex:${w(s, e)}">${n}</div>`).join("") + '</div><div class="gticks">' + segs.map(([s, e]) => `<span style="flex:${w(s, e)}">${e}</span>`).join("") + "</div>";
}
function schedStepper(el, procs, algo, q) {
  const { segs, stats } = schedule(procs, algo, q), total = segs[segs.length - 1][1], names = procs.map((p) => p[0]), sc = 560 / total;
  const arr = Object.fromEntries(procs.map((p) => [p[0], p[1]])), burst = Object.fromEntries(procs.map((p) => [p[0], p[2]]));
  const ran = (n, t) => segs.reduce((a, [s, e, m]) => a + (m === n ? Math.max(0, Math.min(e, t) - s) : 0), 0);
  const draw = (st) => { const k = Math.round(st.i); let o = SV.text(20, 20, "CPU timeline", "lbl bd");
    segs.slice(0, k).forEach(([s, e, n]) => { o += SV.rect(30 + s * sc, 32, (e - s) * sc, 40, "f" + (names.indexOf(n) % 4 + 1), { rx: 3 }) + SV.rect(30 + s * sc, 32, (e - s) * sc, 40, "ax", { rx: 3, fill: "none" }) + SV.text(30 + (s + e) * sc / 2, 57, n, "lbl bd", { "text-anchor": "middle" }) + SV.text(30 + e * sc, 92, String(e), "sm", { "text-anchor": "middle" }); });
    o += SV.text(30, 92, "0", "sm", { "text-anchor": "middle" });
    if (k === segs.length) { const avg = Object.values(stats).reduce((a, v) => a + v[2], 0) / names.length; o += SV.text(30, 130, "Average waiting time = " + (Math.round(avg * 100) / 100), "lbl bd t3"); }
    return o; };
  const steps = [{ cap: "Processes: " + procs.map((p) => p[0] + " (arrives " + p[1] + ", burst " + p[2] + ")").join(", ") + ".", s: { i: 0 } }].concat(segs.map(([s, e, n], i) => {
    const waiting = procs.filter((p) => p[1] <= s && p[0] !== n && burst[p[0]] - ran(p[0], s) > 0).map((p) => p[0] + " (needs " + (burst[p[0]] - ran(p[0], s)) + ")");
    const why = algo === "FCFS" ? "it arrived first" : algo === "SJF" ? "it has the shortest burst time of those waiting" : algo === "SRT" ? "it has the least time left" : "it is next in the queue; it runs for at most " + q;
    return { cap: `Time ${s}: <b>${n}</b> runs until ${e}: ${why}. Waiting: ${waiting.length ? waiting.join(", ") : "nobody"}.`, s: { i: i + 1 } }; }));
  Lib.stepper(el, { w: 620, h: 150, label: algo, base: { i: 0 }, draw, tween: 100, dwell: 2600, steps });
}
schedStepper($("#stA"), PRE.A, "FCFS", 3);
schedStepper($("#stB"), PRE.A, "SRT", 3);
schedStepper($("#stC"), PRE.A, "RR", 3);

(function () {
  let set = "A", algo = "FCFS", q = 3; const pb = $("#sP"), ab = $("#sA");
  const paint = () => { const procs = PRE[set], names = procs.map((p) => p[0]), { segs, stats } = schedule(procs, algo, q); const avg = Object.values(stats).reduce((a, v) => a + v[2], 0) / names.length;
    let h = '<div class="tw"><table class="t mono"><tr><th>Process</th><th>Arrives</th><th>Burst</th><th>Finishes</th><th>Turnaround</th><th>Waiting</th></tr>';
    procs.forEach(([n, a, b]) => (h += `<tr><td>${n}</td><td>${a}</td><td>${b}</td><td>${stats[n][0]}</td><td>${stats[n][1]}</td><td>${stats[n][2]}</td></tr>`));
    $("#sO").innerHTML = ganttHtml(segs, names) + h + `</table></div><div class="verdict">Average waiting time: <b>${Math.round(avg * 100) / 100}</b>. ${algo === "RR" ? "Quantum " + q + "." : ""}</div>`;
    pb.querySelectorAll("button").forEach((b) => (b.className = b.dataset.k === set ? "on" : "")); ab.querySelectorAll("button").forEach((b) => (b.className = b.dataset.k === algo ? "on" : "")); };
  Object.keys(PRE).forEach((k) => { const x = document.createElement("button"); x.textContent = "Set " + k; x.dataset.k = k; x.onclick = () => { set = k; paint(); }; pb.appendChild(x); });
  [["FCFS", "First come first served"], ["SJF", "Shortest job first"], ["SRT", "Shortest remaining time"], ["RR", "Round robin"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { algo = k; paint(); }; ab.appendChild(x); });
  Lib.slider($("#sQ"), { id: "sq", label: "Round robin time quantum ", min: 1, max: 6, value: q, fmt: (x) => x, onInput: (v) => { q = v; paint(); } }); paint();
})();
btnTable("rB", "rO", [
  ["Keep things simple", "First come first served", "No complex logic and no starvation", "Short jobs may wait a long time"],
  ["Smallest average waiting time", "Shortest remaining time", "Short processes finish very quickly", "Long jobs may starve"],
  ["Every process must get a regular turn", "Round robin", "Fixed time slice; no starvation", "Many switches; long jobs take longer"],
  ["Short jobs first, no interruption", "Shortest job first", "Short jobs do not wait for long ones; high throughput", "Long jobs may starve"],
  ["Urgent jobs must be done first", "Priority scheduling", "High-priority jobs finish first", "Low priority jobs may wait for ever"]
], ["Need", "Routine", "Benefit", "Drawback"]);
''' + CLASSIFY("cl1", "Which routine matches the description?", ["First come first served", "Shortest job first", "Shortest remaining time", "Round robin"],
  [("Processes run in the order they arrive, one at a time", 0), ("The process with the shortest burst time is chosen and runs to completion", 1), ("A running process is replaced when a shorter one arrives", 2), ("Each process gets a fixed time quantum in turn", 3), ("Needs no complex logic and has little overhead", 0), ("Pre-emptive and based on the time left", 2)],
  "FCFS by arrival, SJF by burst, SRT by time left, RR by quantum.") + CLASSIFY("cl2", "Is it a benefit or a drawback?", ["Benefit", "Drawback"],
  [("Round robin: no starvation", 0), ("Shortest job first: long jobs may starve", 1), ("First come first served: little processor overhead", 0), ("Shortest remaining time: waiting time is minimised", 0), ("First come first served: short jobs wait behind long ones", 1), ("Round robin: many switches between processes", 1)],
  "Match the routine with its strength or weakness.") + MATCH([
  ["First come first served", "Queued as received, executed one by one"], ["Shortest job first", "Ascending order of CPU time required"], ["Shortest remaining time", "Pre-emptive: shorter arrival replaces the running process"], ["Round robin", "Fixed time quantum for each process in turn"], ["Starvation", "A process never gets the CPU"]]) + ORDER(
  "Put the round robin steps in order.",
  ["Processes are queued as they arrive", "The first process runs for one time quantum", "Its state is saved and it goes to the back of the queue", "The next process in the queue runs for its quantum", "A process that finishes inside its quantum leaves the queue"],
  "Queue, run, save, next, finish.") + CALC([
  {"q": "Three processes arrive at time 0 with burst times 5, 2 and 3 (in that order). Using FCFS, what is the average waiting time?", "a": 4, "unit": "", "tol": 0.01, "hint": "Waits are 0, 5 and 7.", "sol": "(0 + 5 + 7) / 3 = <b>4</b>."},
  {"q": "The same processes with shortest job first: what is the average waiting time? (2 decimal places)", "a": 2.33, "unit": "", "tol": 0.01, "hint": "Order 2, 3, 5: waits 0, 2, 5.", "sol": "(0 + 2 + 5) / 3 = <b>2.33</b>."},
  {"q": "A process arrives at time 4, starts at time 9 and needs 3 units of CPU time. What is its waiting time?", "a": 5, "unit": "", "tol": 0.01, "hint": "Starts minus arrives, with no interruption.", "sol": "<b>5</b>."},
  {"q": "A process arrives at 2, has a burst time of 6 and finishes at 14. What is its turnaround time?", "a": 12, "unit": "", "tol": 0.01, "hint": "Finish minus arrival.", "sol": "<b>12</b>."},
  {"q": "The process above: what is its waiting time?", "a": 6, "unit": "", "tol": 0.01, "hint": "Turnaround minus burst.", "sol": "12 − 6 = <b>6</b>."}]) + MCQ([
  ("Which routine is pre-emptive and picks the process with the least time left?", ["FCFS", "Shortest job first", "Shortest remaining time", "None"], 2, "SRT."),
  ("Which routine can cause starvation of long jobs?", ["Round robin", "First come first served", "Shortest job first", "All of them"], 2, "SJF."),
  ("Round robin gives each process:", ["The whole CPU", "A fixed time quantum", "No time", "The shortest slot"], 1, "A time quantum."),
  ("A benefit of first come first served is:", ["It is the fastest", "It is simple, with no complex logic", "It always has the lowest waiting time", "It is pre-emptive"], 1, "Simple."),
  ("What is the waiting time?", ["Time in the ready queue", "Time using the CPU", "Time to switch on", "Time to finish a file"], 0, "Time in the queue."),
  ("Which routine saves a process's state when its time slice ends?", ["Round robin", "Shortest job first", "FCFS", "None"], 0, "Round robin.")], "qz1") + CARDS([
  ("FCFS", "Queue order; no starvation; short jobs wait."), ("SJF", "Shortest burst first; runs to completion; may starve long jobs."), ("SRT", "Pre-emptive SJF; shorter arrival replaces the running process."), ("Round robin", "Fixed quantum; state saved; no starvation."),
  ("Burst time", "CPU time needed."), ("Waiting time", "Turnaround − burst."), ("Pre-emptive", "Running process can be stopped."), ("Starvation", "Never gets the CPU.")])

build("ac1613", "ac-16-1-3-scheduling-routines", "Scheduling Routines", EYA("16.1.3"),
  "Why scheduling is needed and the four routines (first come first served, shortest job first, shortest remaining time, round robin) with Gantt charts and waiting times; animations, a scheduling simulator and the real Paper 3 questions from 2022 and 2025.",
  dict(sub=CBK("Chapter 16 · System software, section 16.1 Purposes of an operating system"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
