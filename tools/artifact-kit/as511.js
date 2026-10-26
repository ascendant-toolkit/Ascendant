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
  const names = ["A", "B", "C"]; const draw = (s) => { const k = Math.round(s.i); let o = ""; for (let i = 0; i < 6; i++) { const p = names[i % 3]; o += SV.rect(30 + i * 85, 50, 80, 36, i === k ? "f3" : i < k ? "f1" : "cell", { rx: 6 }) + SV.text(70 + i * 85, 73, "Process " + p, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); }
    o += SV.text(30, 30, "time →", "sm") + SV.text(30, 120, k < 6 ? "Process " + names[k % 3] + " has the processor now; the others wait" : "", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 135, label: "Time slices", base: { i: 0 }, draw, tween: 100, dwell: 1600, steps: [0, 1, 2, 3, 4, 5].map((i) => ({ cap: i === 0 ? "The OS gives <b>process A</b> a time slice." : i < 3 ? `The OS stores the registers and gives <b>process ${names[i]}</b> the next slice.` : "The cycle repeats: each process gets a turn again.", s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const blocks = [["OS", 3, "f3"], ["Browser", k >= 1 ? 3 : 0, "f1"], ["Game", k >= 2 ? 4 : 0, "f2"], ["free", 10 - 3 - (k >= 1 ? 3 : 0) - (k >= 2 ? 4 : 0) + (k >= 3 ? 3 : 0), "cell"]]; let x = 30, o = "";
    const list = k >= 3 ? [["OS", 3, "f3"], ["free", 3, "cell"], ["Game", 4, "f2"], ["free", 0, "cell"]] : blocks; let rest = 10; list.forEach(([n, w, c]) => { if (w > 0) { o += SV.rect(x, 40, w * 45, 44, c, { rx: 4 }) + SV.text(x + w * 22, 67, n, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); x += w * 45; rest -= w; } });
    if (k >= 3) { o = ""; x = 30; [["OS", 3, "f3"], ["free", 3, "cell"], ["Game", 4, "f2"]].forEach(([n, w, c]) => { o += SV.rect(x, 40, w * 45, 44, c, { rx: 4 }) + SV.text(x + w * 22, 67, n, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); x += w * 45; }); }
    o += SV.text(30, 20, "RAM", "sm") + SV.text(30, 115, ["only the OS in memory", "the OS allocates RAM to the browser", "and to the game; neither can touch the other's memory", "the browser closes: its RAM is freed for others"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 520, h: 130, label: "Memory", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [0, 1, 2, 3].map((i) => ({ cap: ["RAM holds only the OS.", "The OS <b>allocates</b> RAM to the browser.", "It allocates RAM to the game and makes sure they do not share memory.", "When the browser closes the OS <b>frees</b> its memory."][i], s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 120, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 60, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); let o = B(20, "Application", k >= 0) + B(220, "Operating system", k >= 1) + B(420, "Printer", k >= 3) + SV.path("M140,62 H220", "ax") + SV.path("M340,62 H420", "ax");
    o += SV.text(260, 125, ["Word processor: Print", "the OS receives the request (a platform for the app)", "the OS finds the printer's device driver", "the driver controls the printer; the app never needed to know how"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 140, label: "OS and hardware", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [0, 1, 2, 3].map((i) => ({ cap: ["An application asks to print.", "The OS handles the request.", "Hardware management: the OS uses the printer's <b>driver</b>.", "The OS hides the printer's complexity from the application."][i], s: { i } })) });
})();

(function () {
  let slice = 20; const paint = () => { const T = 240; let o = '<svg viewBox="0 0 440 90" style="width:440px;max-width:100%;display:block">'; const col = ["var(--accent)", "var(--good)", "var(--warn,#c89500)"]; let t = 0, i = 0, n = 0; while (t < T && n < 40) { const w = Math.min(slice, T - t); o += `<rect x="${20 + t * 1.6}" y="20" width="${Math.max(w * 1.6 - 1, 1)}" height="40" fill="${col[i % 3]}" opacity=".8"/>`; t += w; i++; n++; }
    o += `<text x="20" y="80" class="sm" style="font-size:11px">0</text><text x="${20 + T * 1.6}" y="80" class="sm" text-anchor="end" style="font-size:11px">${T} ms</text></svg>`; $("#tG").innerHTML = o; const sw = Math.ceil(T / slice) - 1;
    $("#tV").innerHTML = `With a <b>${slice} ms</b> time slice, each process gets the processor ${Math.ceil(T / slice / 3)} times in ${T} ms, so the OS makes about <b>${sw} switches</b>. Short slices make the programs seem to run at once but cost more switching; long slices switch less but a process may wait longer.`; };
  Lib.slider($("#tS"), { id: "t1", label: "Time slice (ms) ", min: 5, max: 80, step: 5, value: slice, fmt: (x) => x, onInput: (v) => { slice = v; paint(); } }); paint();
})();
btnTable("mB", "mO", [
  ["Scheduling which program runs next", "Process management", "Time slices and priorities"],
  ["Giving a new program some RAM", "Memory management", "Allocate and free"],
  ["Creating a new folder", "File management", "Directory structures"],
  ["Checking a password at log-in", "Security management", "Authentication"],
  ["Loading a driver for a new mouse", "Hardware management", "Device driver"],
  ["Handling a key press interrupt", "Hardware management", "Manages interrupts"]
], ["Job", "Task", "Detail"]);
(function () {
  const total = 10; let progs = []; let next = 1;
  const paint = () => { const used = progs.reduce((a, p) => a + p.w, 0) + 2; let x = 0, o = '<svg viewBox="0 0 480 80" style="width:480px;max-width:100%;display:block">'; const seg = (n, w, c) => { o += `<rect x="${10 + x * 45}" y="10" width="${w * 45 - 2}" height="40" rx="4" class="${c}"/><text x="${10 + x * 45 + w * 22}" y="35" text-anchor="middle" class="lbl bd" style="font-size:11px">${n}</text>`; x += w; };
    seg("OS", 2, "f3"); progs.forEach((p) => seg(p.n, p.w, "f1")); if (total - used > 0) seg("free", total - used, "cell"); $("#mmG").innerHTML = o + "</svg>"; $("#mmV").innerHTML = `RAM in use: <b>${used} of ${total} GB</b>. The OS allocates memory when a program opens and frees it when the program closes.`; };
  $("#mm_a").onclick = () => { const used = progs.reduce((a, p) => a + p.w, 0) + 2; if (used + 2 <= total) { progs.push({ n: "P" + next++, w: 2 }); paint(); } else $("#mmV").innerHTML = "Not enough free RAM: the OS cannot allocate memory for another program (it would use virtual memory)."; };
  $("#mm_b").onclick = () => { progs.pop(); paint(); }; $("#mm_r").onclick = () => { progs = []; next = 1; paint(); }; paint();
})();
Lib.classify($("#cl1"), { prompt: "Which key management task does it describe?", buckets: [{"label": "Process"}, {"label": "Memory"}, {"label": "File"}, {"label": "Security"}, {"label": "Hardware"}], items: [{"text": "Decides which process runs next", "b": 0}, {"text": "Allocates RAM to a program when it starts", "b": 1}, {"text": "Creates and maintains folders", "b": 2}, {"text": "Validates a user's password", "b": 3}, {"text": "Installs a device driver", "b": 4}, {"text": "Allows two processes to share data", "b": 0}], done: "Match the job to the task." });
Lib.classify($("#cl2"), { prompt: "Is it a purpose of the OS or a key management task?", buckets: [{"label": "Purpose"}, {"label": "Management task"}], items: [{"text": "Provide a user interface", "b": 0}, {"text": "Memory management", "b": 1}, {"text": "Hide the complexity of the hardware", "b": 0}, {"text": "Security management", "b": 1}, {"text": "Provide a platform for software to run", "b": 0}, {"text": "File management", "b": 1}], done: "Purposes: hide, platform, interface." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Process management", "Dynamically decides which process runs next"], ["Memory management", "Allocates RAM to processes and frees it"], ["File management", "Marks unallocated file storage for availability"], ["Security management", "Validates user and process authenticity"], ["Hardware management", "Installs device drivers for external ports"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the multitasking steps in order.", items: ["Process A runs for its time slice", "The OS stores A's registers", "The OS loads the registers of process B", "Process B runs for its time slice", "The OS returns to A when it is its turn again"], done: "Run, store, load, run, return." });
Lib.calc($("#c1"), { qs: [
  {"q": "Three processes each get a 10 ms time slice in turn. How many ms before process A runs again?", "a": 30, "unit": "ms", "tol": 0.1, "hint": "3 × 10.", "sol": "<b>30</b> ms."},
  {"q": "A computer has 8 GB of RAM and the OS uses 2 GB. How many GB are free for processes?", "a": 6, "unit": "GB", "tol": 0.01, "hint": "8 − 2.", "sol": "<b>6</b> GB."},
  {"q": "Four programs need 1 GB each. How many can run in 6 GB free RAM?", "a": 4, "unit": "", "tol": 0.01, "hint": "All four fit (4 GB).", "sol": "<b>4</b>."},
  {"q": "A file is stored in allocation units of 4 KiB. A 10 KiB file needs how many units?", "a": 3, "unit": "", "tol": 0.01, "hint": "10 ÷ 4 rounded up.", "sol": "<b>3</b>."},
  {"q": "How many key management tasks are listed in the Learn tab?", "a": 5, "unit": "", "tol": 0.01, "hint": "Process, memory, file, security, hardware.", "sol": "<b>5</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A purpose of the OS is to:", opts: ["Hide the complexity of the hardware", "Compile programs", "Store files only", "Increase the clock speed"], a: 0, why: "Hide hardware complexity." },
  { q: "Scheduling belongs to:", opts: ["Process management", "Memory management", "File management", "Security management"], a: 0, why: "Process." },
  { q: "Device drivers are installed by:", opts: ["Hardware management", "File management", "Memory management", "Process management"], a: 0, why: "Hardware." },
  { q: "Access rights are part of:", opts: ["Security management", "Hardware management", "Process management", "Memory management"], a: 0, why: "Security." },
  { q: "Multitasking is done by:", opts: ["Time slices", "Faster RAM", "Two screens", "Compression"], a: 0, why: "Time slices." },
  { q: "File management does:", opts: ["Create and maintain directories", "Allocate RAM", "Schedule processes", "Install drivers"], a: 0, why: "Directories." },
] });
Lib.cards($("#fc1"), { cards: [
  ["OS purposes", "Hide hardware, platform, user interface."],
  ["Process", "Scheduling, multitasking, conflicts."],
  ["Memory", "Allocate and free RAM."],
  ["File", "Folders, space, names, access."],
  ["Security", "Accounts, passwords, access rights."],
  ["Hardware", "Drivers, communication, interrupts."],
  ["Time slice", "Short turn on the processor."],
  ["Device driver", "Software to control a device."],
] });
