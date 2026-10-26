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

(function () {
  const L = [["User", "clicks Save"], ["Application", "asks the OS to save the file"], ["Operating system", "finds free space, chooses the file's place"], ["Device driver", "gives the disk its own commands"], ["Hardware", "the disk records the data"]];
  const draw = (s) => { const k = Math.round(s.i); let o = "";
    L.forEach(([n, t], i) => { const y = 14 + i * 58, on = i <= k, cur = i === k; o += SV.rect(20, y, 220, 46, cur ? "cell-warn" : on ? "cell-ok" : "cell", { rx: 8 }) + SV.text(34, y + 29, n, "lbl bd") + (on ? SV.text(264, y + 29, t, "lbl") : "") ; if (i < 4) o += SV.path("M130," + (y + 46) + " V" + (y + 58), "ax"); });
    o += SV.text(588, 40, "the user sees", "sm", { "text-anchor": "middle" }) + SV.text(588, 56, "only this", "sm", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stA"), { w: 640, h: 306, label: "Layers", base: { i: 0 }, draw, tween: 150, dwell: 2400, steps: [
    { cap: "The user clicks <b>Save</b>. This is all the user does.", s: { i: 0 } }, { cap: "The application does not touch the disk. It asks the <b>operating system</b> to save the file.", s: { i: 1 } },
    { cap: "The OS chooses where on the disk the file goes and records its name in the file system.", s: { i: 2 } }, { cap: "The <b>device driver</b> turns the OS's request into the commands this disk understands.", s: { i: 3 } },
    { cap: "The hardware stores the data. The user never dealt with sectors, buses or commands: the OS hid the complexity.", s: { i: 4 } }] });
})();
(function () {
  const P = [["A", "f1"], ["B", "f2"], ["C", "f3"]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "one processor", "sm");
    const seq = [0, 1, 2, 0, 1, 2], slice = 56; o += SV.text(20, 44, "multi-tasking: time slices", "lbl bd");
    for (let i = 0; i < 6; i++) { const on = i < k; if (on) o += SV.rect(20 + i * slice, 56, slice - 4, 36, P[seq[i]][1], { rx: 4 }) + SV.rect(20 + i * slice, 56, slice - 4, 36, "ax", { rx: 4, fill: "none" }) + SV.text(20 + i * slice + (slice - 4) / 2, 79, P[seq[i]][0], "lbl bd", { "text-anchor": "middle" }); }
    o += SV.text(20, 130, "no multi-tasking: one at a time", "lbl bd");
    const w3 = 112; for (let i = 0; i < 3; i++) { const on = i * 2 < k; if (on) o += SV.rect(20 + i * w3, 142, w3 - 4, 36, P[i][1], { rx: 4 }) + SV.rect(20 + i * w3, 142, w3 - 4, 36, "ax", { rx: 4, fill: "none" }) + SV.text(20 + i * w3 + (w3 - 4) / 2, 165, P[i][0], "lbl bd", { "text-anchor": "middle" }); }
    if (k === 6) o += SV.text(20, 210, "With time slices A, B and C all make progress early; one at a time, C waits for A and B to finish.", "lbl bd t3", { style: "font-size:12.5px" }); return o; };
  Lib.stepper($("#stB"), { w: 640, h: 232, label: "Multi-tasking", base: { i: 0 }, draw, tween: 150, dwell: 1600, steps: [0, 1, 2, 3, 4, 5, 6].map((i) => ({ cap: i === 0 ? "Three programs A, B and C want the one processor. Compare the two ways of sharing it." : i === 6 ? "After six slices each program has had two turns. The OS switches between them so quickly that they seem to run together." : "Slice " + i + ": the processor runs " + "ABCABC"[i - 1] + " for a short time, then the OS switches to the next process.", s: { i } })) });
})();
(function () {
  const items = [["CPU time", "scheduler shares it"], ["Memory", "memory manager allocates it"], ["Printer", "queue and driver"], ["Disk", "file system tracks files"]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 20, 180, 190, "cell", { rx: 10 }) + SV.text(110, 46, "Operating system", "lbl bd", { "text-anchor": "middle" });
    items.forEach(([n, t], i) => { const on = i < k; o += SV.rect(34, 62 + i * 36, 152, 28, on ? "cell-ok" : "cell", { rx: 6, ...op(on ? 1 : 0.35) }) + SV.text(110, 81 + i * 36, n, "lbl", { "text-anchor": "middle", ...op(on ? 1 : 0.5) }); });
    ["Program A", "Program B", "Program C"].forEach((p, i) => { o += SV.rect(330, 30 + i * 62, 130, 40, "f" + (i + 1), { rx: 8 }) + SV.rect(330, 30 + i * 62, 130, 40, "ax", { rx: 8, fill: "none" }) + SV.text(395, 55 + i * 62, p, "lbl bd", { "text-anchor": "middle" }) + SV.path("M200," + (110 + (i - 1) * 0) + " L330," + (50 + i * 62), "edge", { ...op(k > 0 ? 0.5 : 0.1) }); });
    if (k > 0) o += SV.text(250, 232, items[k - 1][0] + ": " + items[k - 1][1], "lbl bd t3"); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 250, label: "Resources", base: { i: 0 }, draw, tween: 150, dwell: 2200, steps: [{ cap: "Programs A, B and C all want the computer's resources.", s: { i: 0 } }, { cap: "The OS shares the <b>processor</b> between them by scheduling.", s: { i: 1 } }, { cap: "It gives each program its own part of <b>memory</b> and keeps them apart.", s: { i: 2 } }, { cap: "It queues requests for the <b>printer</b> and uses a driver to control it.", s: { i: 3 } }, { cap: "It tracks the files on the <b>disk</b>. All the sharing is hidden from the user.", s: { i: 4 } }] });
})();

(function () {
  let n = 1;
  const paint = () => { let o = ""; const busy = Math.min(100, Math.round(40 * n)); const cols = 10; let t = '<div class="tw"><table class="t mono"><tr><th>unit</th>' + Array.from({ length: 10 }, (_, i) => "<th>" + (i + 1) + "</th>").join("") + "</tr><tr><td>CPU</td>";
    // each program: 2 CPU units then 3 waiting units, starts offset by 2 units per program
    const cpu = Array(10).fill("");
    for (let p = 0; p < n; p++) for (let u = 0; u < 10; u++) { const ph = (u - 2 * p + 100) % 5; if (u >= 2 * p && ph < 2 && cpu[u] === "") cpu[u] = "P" + (p + 1); }
    let b = 0; cpu.forEach((c) => { t += "<td" + (c ? ' style="background:var(--good-soft)"' : ' style="background:var(--bad-soft)"') + ">" + (c || "idle") + "</td>"; if (c) b++; });
    $("#mT").innerHTML = t + "</tr></table></div>"; $("#m1").textContent = b * 10 + "%"; $("#m2").textContent = 100 - b * 10 + "%"; };
  Lib.slider($("#mS"), { id: "ms", label: "Programs running together ", min: 1, max: 3, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();
btnTable("oB", "oO", [
  ["Print a document", "Queues the job, loads the printer driver, sends data to the printer", "Device management and drivers"],
  ["Open two programs", "Allocates memory to each and shares the processor", "Memory and process management"],
  ["Save a file", "Finds free space on the disk and records the file name", "File management"],
  ["Log in", "Checks the user name and password and sets permissions", "User and security management"],
  ["Press a key", "Handles the interrupt and passes the key to the program", "Kernel as interrupt handler"],
  ["Click an icon", "Turns the click into the right action; the user need not know the hardware", "User interface"]
], ["Task", "What the OS does", "Part"]);
(function () {
  let q = 4;
  const paint = () => { const total = 12, nSw = Math.ceil(total / q); let t = '<div class="tw"><table class="t mono"><tr><th>CPU timeline (units)</th></tr><tr><td>'; const seq = []; let rem = [4, 4, 4], i = 0; while (rem.some((x) => x > 0)) { if (rem[i % 3] > 0) { const u = Math.min(q, rem[i % 3]); seq.push("P" + (i % 3 + 1) + "×" + u); rem[i % 3] -= u; } i++; }
    $("#tT").innerHTML = t + seq.join(" → ") + "</td></tr></table></div>"; $("#tV").innerHTML = "Time slice " + q + " unit" + (q > 1 ? "s" : "") + ": the OS switches process <b>" + (seq.length - 1) + "</b> times. A very short slice means many switches (more overhead); a very long slice makes the processes wait for each other."; };
  Lib.slider($("#tS"), { id: "ts", label: "Time slice (units) ", min: 1, max: 4, value: q, fmt: (x) => x, onInput: (v) => { q = v; paint(); } }); paint();
})();
Lib.classify($("#cl1"), { prompt: "Which part of the OS does the task belong to?", buckets: [{"label": "Process management"}, {"label": "Memory management"}, {"label": "File management"}, {"label": "Device management"}], items: [{"text": "Choosing which program gets the CPU next", "b": 0}, {"text": "Giving a program a block of RAM", "b": 1}, {"text": "Recording where a file is on the disk", "b": 2}, {"text": "Using a driver to control a printer", "b": 3}, {"text": "Switching between two programs many times a second", "b": 0}, {"text": "Moving unused data out of RAM to the disk", "b": 1}], done: "Processes, memory, files, devices." });
Lib.classify($("#cl2"), { prompt: "Does it help to hide the complexity of the hardware?", buckets: [{"label": "Yes"}, {"label": "No"}], items: [{"text": "A graphical user interface with icons", "b": 0}, {"text": "A device driver for a printer", "b": 0}, {"text": "Being able to save a file by name", "b": 0}, {"text": "The speed of the processor", "b": 1}, {"text": "The size of the RAM", "b": 1}, {"text": "Typing a command that sets a memory address", "b": 1}], done: "Interfaces, drivers and the file system hide the hardware." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Multi-tasking", "Many programs that appear to run at the same time"], ["Scheduling", "Managing the processes running on the CPU"], ["Interrupt handling", "Transferring control to another routine when a service is required"], ["Paging", "Reading and writing same-size blocks to and from secondary storage"], ["Virtual memory", "Using secondary storage to simulate additional main memory"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps in order for printing a document.", items: ["The user clicks Print", "The application asks the OS to print", "The OS queues the print job", "The printer driver converts the data into printer commands", "The printer prints the page"], done: "Click, application, OS, driver, hardware." });
Lib.calc($("#c1"), { qs: [
  {"q": "Each program uses the CPU for 2 units and waits 3 units. With one program, what percentage of the time is the CPU busy?", "a": 40, "unit": "%", "tol": 0.5, "hint": "2 out of 5 units.", "sol": "<b>40</b>%."},
  {"q": "With three such programs run together and perfectly spaced, how many units out of 5 is the CPU busy?", "a": 5, "unit": "", "tol": 0.01, "hint": "Each adds 2 units, up to 5 in a cycle.", "sol": "<b>5</b>: the CPU is fully used."},
  {"q": "Three processes each need 4 units and the time slice is 2 units. How many slices does the CPU run in total?", "a": 6, "unit": "", "tol": 0.01, "hint": "Two slices each.", "sol": "<b>6</b>."},
  {"q": "Three processes each need 4 units and the time slice is 4. How many switches between processes?", "a": 2, "unit": "", "tol": 0.01, "hint": "Three slices, so two switches.", "sol": "<b>2</b>."},
  {"q": "How many resources are listed in the table in the Learn tab (processor, memory, input and output devices, storage, users)?", "a": 5, "unit": "", "tol": 0.01, "hint": "Count the rows.", "sol": "<b>5</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does multi-tasking let the computer do?", opts: ["Run exactly one program", "Run, or appear to run, several programs at a time", "Make the screen larger", "Delete old files"], a: 1, why: "It shares the processor." },
  { q: "A device driver is:", opts: ["Hardware", "Software that controls a particular device", "A kind of memory", "A file"], a: 1, why: "It lets the OS control a device." },
  { q: "The kernel:", opts: ["Is the central part of the OS", "Is a printer", "Is an application", "Is a type of cable"], a: 0, why: "The core of the OS." },
  { q: "Which hides hardware complexity?", opts: ["A graphical user interface", "A bigger monitor", "A faster disk", "A longer cable"], a: 0, why: "The interface." },
  { q: "Why does the OS give each process a time slice?", opts: ["To save paper", "So all processes make progress", "To make the disk smaller", "To stop interrupts"], a: 1, why: "Sharing the processor." },
  { q: "Virtual memory uses:", opts: ["Secondary storage", "A printer", "The keyboard", "The power supply"], a: 0, why: "Disk space as extra memory." },
] });
Lib.cards($("#fc1"), { cards: [
  ["OS", "Manages the hardware and provides a platform for applications."],
  ["Resources", "Processor, memory, devices, files and users."],
  ["Multi-tasking", "Several processes appear to run at once by sharing the CPU."],
  ["User interface", "Hides the hardware: icons and menus."],
  ["Device driver", "Lets the OS control a specific device."],
  ["Kernel", "Core of the OS: processes, memory, interrupts."],
  ["Time slice", "A short turn of the CPU for one process."],
  ["Abstraction", "Showing the user only what they need."],
] });
