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

function schedule(procs, algo, q) {
  const P = {}, rem = {}, order = procs.map((p) => p[0]); procs.forEach(([n, a, b]) => { P[n] = [a, b]; rem[n] = b; });
  const segs = [], done = {}; let t = 0;
  const add = (n, s, e) => { const l = segs[segs.length - 1]; if (l && l[2] === n && l[1] === s) l[1] = e; else segs.push([s, e, n]); };
  const key = (n, k) => [k, P[n][0], order.indexOf(n)];
  const cmp = (x, y) => { for (let i = 0; i < x.length; i++) if (x[i] !== y[i]) return x[i] - y[i]; return 0; };
  if (algo === "FCFS") { [...order].sort((a, b) => cmp([P[a][0], order.indexOf(a)], [P[b][0], order.indexOf(b)])).forEach((n) => { t = Math.max(t, P[n][0]); add(n, t, t + P[n][1]); t += P[n][1]; done[n] = t; }); }
  else if (algo === "SJF" || algo === "SRT") {
    const left = new Set(order);
    while (left.size) { const av = [...left].filter((n) => P[n][0] <= t); if (!av.length) { t = Math.min(...[...left].map((n) => P[n][0])); continue; }
      if (algo === "SJF") { av.sort((a, b) => cmp(key(a, P[a][1]), key(b, P[b][1]))); const n = av[0]; add(n, t, t + P[n][1]); t += P[n][1]; done[n] = t; left.delete(n); }
      else { av.sort((a, b) => cmp(key(a, rem[a]), key(b, rem[b]))); const n = av[0]; add(n, t, t + 1); rem[n]--; t++; if (!rem[n]) { done[n] = t; left.delete(n); } } }
  } else {
    const pend = [...order].sort((a, b) => cmp([P[a][0], order.indexOf(a)], [P[b][0], order.indexOf(b)])), queue = [];
    const admit = () => { while (pend.length && P[pend[0]][0] <= t) queue.push(pend.shift()); };
    admit();
    while (queue.length || pend.length) { if (!queue.length) { t = P[pend[0]][0]; admit(); continue; } const n = queue.shift(), r = Math.min(q, rem[n]); add(n, t, t + r); t += r; rem[n] -= r; admit(); if (rem[n] > 0) queue.push(n); else done[n] = t; }
  }
  const stats = {}; order.forEach((n) => (stats[n] = [done[n], done[n] - P[n][0], done[n] - P[n][0] - P[n][1]]));
  return { segs, stats };
}
const PRE = {"A": [["P1", 0, 7], ["P2", 1, 4], ["P3", 2, 1], ["P4", 3, 4]], "B": [["A", 0, 5], ["B", 2, 3], ["C", 4, 1], ["D", 6, 2]], "C": [["P1", 0, 3], ["P2", 0, 6], ["P3", 0, 4], ["P4", 0, 2]]};

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
Lib.classify($("#cl1"), { prompt: "Which routine matches the description?", buckets: [{"label": "First come first served"}, {"label": "Shortest job first"}, {"label": "Shortest remaining time"}, {"label": "Round robin"}], items: [{"text": "Processes run in the order they arrive, one at a time", "b": 0}, {"text": "The process with the shortest burst time is chosen and runs to completion", "b": 1}, {"text": "A running process is replaced when a shorter one arrives", "b": 2}, {"text": "Each process gets a fixed time quantum in turn", "b": 3}, {"text": "Needs no complex logic and has little overhead", "b": 0}, {"text": "Pre-emptive and based on the time left", "b": 2}], done: "FCFS by arrival, SJF by burst, SRT by time left, RR by quantum." });
Lib.classify($("#cl2"), { prompt: "Is it a benefit or a drawback?", buckets: [{"label": "Benefit"}, {"label": "Drawback"}], items: [{"text": "Round robin: no starvation", "b": 0}, {"text": "Shortest job first: long jobs may starve", "b": 1}, {"text": "First come first served: little processor overhead", "b": 0}, {"text": "Shortest remaining time: waiting time is minimised", "b": 0}, {"text": "First come first served: short jobs wait behind long ones", "b": 1}, {"text": "Round robin: many switches between processes", "b": 1}], done: "Match the routine with its strength or weakness." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["First come first served", "Queued as received, executed one by one"], ["Shortest job first", "Ascending order of CPU time required"], ["Shortest remaining time", "Pre-emptive: shorter arrival replaces the running process"], ["Round robin", "Fixed time quantum for each process in turn"], ["Starvation", "A process never gets the CPU"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the round robin steps in order.", items: ["Processes are queued as they arrive", "The first process runs for one time quantum", "Its state is saved and it goes to the back of the queue", "The next process in the queue runs for its quantum", "A process that finishes inside its quantum leaves the queue"], done: "Queue, run, save, next, finish." });
Lib.calc($("#c1"), { qs: [
  {"q": "Three processes arrive at time 0 with burst times 5, 2 and 3 (in that order). Using FCFS, what is the average waiting time?", "a": 4, "unit": "", "tol": 0.01, "hint": "Waits are 0, 5 and 7.", "sol": "(0 + 5 + 7) / 3 = <b>4</b>."},
  {"q": "The same processes with shortest job first: what is the average waiting time? (2 decimal places)", "a": 2.33, "unit": "", "tol": 0.01, "hint": "Order 2, 3, 5: waits 0, 2, 5.", "sol": "(0 + 2 + 5) / 3 = <b>2.33</b>."},
  {"q": "A process arrives at time 4, starts at time 9 and needs 3 units of CPU time. What is its waiting time?", "a": 5, "unit": "", "tol": 0.01, "hint": "Starts minus arrives, with no interruption.", "sol": "<b>5</b>."},
  {"q": "A process arrives at 2, has a burst time of 6 and finishes at 14. What is its turnaround time?", "a": 12, "unit": "", "tol": 0.01, "hint": "Finish minus arrival.", "sol": "<b>12</b>."},
  {"q": "The process above: what is its waiting time?", "a": 6, "unit": "", "tol": 0.01, "hint": "Turnaround minus burst.", "sol": "12 − 6 = <b>6</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which routine is pre-emptive and picks the process with the least time left?", opts: ["FCFS", "Shortest job first", "Shortest remaining time", "None"], a: 2, why: "SRT." },
  { q: "Which routine can cause starvation of long jobs?", opts: ["Round robin", "First come first served", "Shortest job first", "All of them"], a: 2, why: "SJF." },
  { q: "Round robin gives each process:", opts: ["The whole CPU", "A fixed time quantum", "No time", "The shortest slot"], a: 1, why: "A time quantum." },
  { q: "A benefit of first come first served is:", opts: ["It is the fastest", "It is simple, with no complex logic", "It always has the lowest waiting time", "It is pre-emptive"], a: 1, why: "Simple." },
  { q: "What is the waiting time?", opts: ["Time in the ready queue", "Time using the CPU", "Time to switch on", "Time to finish a file"], a: 0, why: "Time in the queue." },
  { q: "Which routine saves a process's state when its time slice ends?", opts: ["Round robin", "Shortest job first", "FCFS", "None"], a: 0, why: "Round robin." },
] });
Lib.cards($("#fc1"), { cards: [
  ["FCFS", "Queue order; no starvation; short jobs wait."],
  ["SJF", "Shortest burst first; runs to completion; may starve long jobs."],
  ["SRT", "Pre-emptive SJF; shorter arrival replaces the running process."],
  ["Round robin", "Fixed quantum; state saved; no starvation."],
  ["Burst time", "CPU time needed."],
  ["Waiting time", "Turnaround − burst."],
  ["Pre-emptive", "Running process can be stopped."],
  ["Starvation", "Never gets the CPU."],
] });
