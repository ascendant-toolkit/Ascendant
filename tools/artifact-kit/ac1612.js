const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

const bin = (n, w = 8) => n.toString(2).padStart(w, "0");
const hx = (n, w = 2) => n.toString(16).toUpperCase().padStart(w, "0");
const grp4 = (s) => s.replace(/(.{4})(?=.)/g, "$1 ");
const clamp01 = (v) => Math.max(0, Math.min(1, v));
/* row of boxes: items [{t, c, v}] t text, c fill class, v opacity */
function boxRow(items, x0, y, w = 64, h = 52, gap = 10, o = {}) {
  let s = "";
  items.forEach((it, i) => {
    const x = x0 + i * (w + gap), v = it.v === undefined ? 1 : it.v;
    if (v <= 0) return;
    s += SV.rect(x, y, w, h, it.c || "f3", { rx: 8, ...op(v * (it.c ? 0.55 : 0.18)) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) });
    s += SV.text(x + w / 2, y + h / 2 + 8, it.t, "lbl bd", { "text-anchor": "middle", style: "font-size:" + (o.fs || 22) + "px;font-family:var(--mono)", ...op(v) });
    if (it.top !== undefined) s += SV.text(x + w / 2, y - 8, it.top, "sm", { "text-anchor": "middle", ...op(v) });
    if (it.bot !== undefined) s += SV.text(x + w / 2, y + h + 18, it.bot, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return s;
}

/* memory cell: address on the left, value in the box */
function memCell(x, y, addr, val, cls = "f3", v = 1, w = 150, h = 40) {
  return SV.rect(x, y, w, h, cls, { rx: 6, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 6, fill: "none", ...op(v) }) +
    SV.text(x + 10, y + h / 2 + 6, String(addr), "sm", { style: "font-family:var(--mono)", ...op(v) }) +
    SV.text(x + w - 12, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono);font-size:17px", ...op(v) });
}
function regBox(x, y, name, val, cls = "f2", v = 1, w = 120, h = 46) {
  return SV.rect(x, y, w, h, cls, { rx: 8, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) }) +
    SV.text(x + 10, y - 7, name, "sm", op(v)) + SV.text(x + w / 2, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:19px", ...op(v) });
}
/* a list of code lines; hl is the highlighted index (or -1) */
function codeList(x, y, lines, hl, v = 1, lh = 30, w = 230) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 4, i === hl ? "cell-warn" : "cell", { rx: 4, ...op(v) }) + SV.text(x + 10, y + i * lh + 18, l, "lbl", { style: "font-family:var(--mono);font-size:14px;white-space:pre", ...op(v) })).join("");
}

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
Lib.classify($("#cl1"), { prompt: "Which state is the process in?", buckets: [{"label": "Running"}, {"label": "Ready"}, {"label": "Blocked"}], items: [{"text": "It is using the CPU now", "b": 0}, {"text": "It is waiting in the queue for a turn on the CPU", "b": 1}, {"text": "It is waiting for a file to finish loading", "b": 2}, {"text": "It was stopped because a higher-priority process arrived", "b": 1}, {"text": "It is waiting for the user to press a key", "b": 2}, {"text": "CPU time has been allocated to it", "b": 0}], done: "Running uses the CPU, ready could run, blocked is waiting for an event." });
Lib.classify($("#cl2"), { prompt: "Is the change of state possible?", buckets: [{"label": "Possible"}, {"label": "Not possible"}], items: [{"text": "Ready to running", "b": 0}, {"text": "Running to blocked", "b": 0}, {"text": "Blocked to ready", "b": 0}, {"text": "Blocked to running", "b": 1}, {"text": "Running to ready", "b": 0}, {"text": "Ready to blocked", "b": 1}], done: "Blocked goes to ready; ready goes only to running." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Interrupt", "A signal that something needs the processor's attention"], ["Kernel", "Receives the interrupt signal and starts the response"], ["ISR", "The routine that deals with one kind of interrupt"], ["Dispatch table", "Maps each interrupt to its service routine"], ["Pre-emption", "A running process is stopped so another can run"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of interrupt handling in order.", items: ["The kernel receives the interrupt signal", "The priority is checked and kernel mode entered", "The state of the running process is saved", "The ISR is found in the interrupt table and run", "The state is restored and the process carries on"], done: "Receive, priority, save, ISR, restore." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many process states are there in the syllabus?", "a": 3, "unit": "", "tol": 0.01, "hint": "Running, ready, blocked.", "sol": "<b>3</b>."},
  {"q": "A single-core CPU has 5 processes. At most how many can be in the running state at once?", "a": 1, "unit": "", "tol": 0.01, "hint": "One CPU, one process.", "sol": "<b>1</b>."},
  {"q": "Process A is blocked. Its I/O completes. Which state does it move to? Enter 1 for running, 2 for ready.", "a": 2, "unit": "", "tol": 0.01, "hint": "Never straight to running.", "sol": "<b>2</b>: ready."},
  {"q": "A time slice is 10 ms and there are 4 ready processes in turn. How long until the first is given the CPU again after its slice (ms)?", "a": 30, "unit": "ms", "tol": 0.5, "hint": "The other three run for 10 ms each.", "sol": "<b>30</b> ms."},
  {"q": "A running process asks for disk data and later runs again. How many changes of state happen on the way (running to blocked, blocked to ready, ready to running)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Count the arrows.", "sol": "<b>3</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A process waiting for a disk transfer is:", opts: ["Running", "Ready", "Blocked", "Terminated"], a: 2, why: "Waiting for an event." },
  { q: "A running process's time slice expires. It moves to:", opts: ["Blocked", "Ready", "Terminated", "Running"], a: 1, why: "Ready." },
  { q: "Where does the kernel save the interrupted process's state?", opts: ["On the kernel stack", "In the monitor", "In the printer", "On paper"], a: 0, why: "On the kernel stack." },
  { q: "The interrupt dispatch table maps:", opts: ["Files to folders", "Interrupts to their service routines", "Users to passwords", "Pages to frames"], a: 1, why: "Interrupt to ISR." },
  { q: "When is the state of the interrupted process restored?", opts: ["Before the interrupt arrives", "After the ISR has finished", "Never", "When the computer is switched off"], a: 1, why: "After the ISR." },
  { q: "A higher-priority process arrives. The running process:", opts: ["Is deleted", "Is pre-empted and goes to ready", "Goes to blocked", "Finishes first"], a: 1, why: "Pre-empted, ready." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Running", "CPU allocated, being executed."],
  ["Ready", "Could run; waiting in the ready queue."],
  ["Blocked", "Waiting for I/O or an event."],
  ["Running to ready", "Time slice ends, higher priority, interrupt."],
  ["Blocked to ready", "The event has happened."],
  ["Kernel as interrupt handler", "Signal, priority, save state, ISR, restore."],
  ["Dispatch table", "IVT / IDT: interrupt to ISR."],
  ["Low-level scheduler", "Moves processes between ready and running."],
] });
