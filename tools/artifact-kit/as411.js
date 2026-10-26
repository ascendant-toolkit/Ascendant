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
Lib.classify($("#cl1"), { prompt: "Special purpose or general purpose register?", buckets: [{"label": "Special purpose"}, {"label": "General purpose"}], items: [{"text": "Program Counter", "b": 0}, {"text": "Holds temporary data during operations", "b": 1}, {"text": "Status Register", "b": 0}, {"text": "Can be used for any purpose the programmer defines", "b": 1}, {"text": "Memory Address Register", "b": 0}, {"text": "Accumulator", "b": 1}], done: "PC, MAR, MDR, CIR, IX, SR are special. ACC is general." });
Lib.classify($("#cl2"), { prompt: "Which bus carries it?", buckets: [{"label": "Address bus"}, {"label": "Data bus"}, {"label": "Control bus"}], items: [{"text": "The address from the MAR", "b": 0}, {"text": "The instruction read from memory", "b": 1}, {"text": "A timing signal from the clock", "b": 2}, {"text": "A read signal", "b": 2}, {"text": "The data to be written to memory", "b": 1}, {"text": "The address of the next instruction", "b": 0}], done: "Address, data, control." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["PC", "Address of the next instruction to be fetched"], ["MAR", "Address of the location being read or written"], ["MDR", "Data read from, or to be written to, memory"], ["CIR", "Instruction currently being decoded and executed"], ["SR", "Flags set by arithmetic, logic and interrupts"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the stored program steps in order.", items: ["The program is loaded into main memory", "The PC holds the address of the first instruction", "The CPU fetches the instruction from main memory", "The instruction is decoded and executed", "The PC moves on to the next instruction"], done: "Load, PC, fetch, execute, next." });
Lib.calc($("#c1"), { qs: [
  {"q": "An address bus has 16 lines. How many memory locations can it address?", "a": 65536, "unit": "", "tol": 0.01, "hint": "2^16.", "sol": "<b>65536</b>."},
  {"q": "An address bus has 20 lines. How many locations (in thousands, 1 K = 1024)? Give the number of K.", "a": 1024, "unit": "K", "tol": 0.5, "hint": "2^20 ÷ 1024.", "sol": "<b>1024</b> K (1 M)."},
  {"q": "A data bus is 32 bits wide. How many bytes are transferred at once?", "a": 4, "unit": "bytes", "tol": 0.01, "hint": "32 ÷ 8.", "sol": "<b>4</b> bytes."},
  {"q": "A CPU runs at 3 GHz and one fetch-execute cycle takes 3 clock ticks. How many cycles per second, in millions?", "a": 1000, "unit": "million", "tol": 0.5, "hint": "3000 ÷ 3.", "sol": "<b>1000</b> million."},
  {"q": "How many special purpose registers are listed in the Learn tab table (PC, MAR, MDR, CIR, IX, SR)?", "a": 6, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>6</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The Program Counter holds:", opts: ["The address of the next instruction", "The next instruction", "The result", "The flags"], a: 0, why: "Address." },
  { q: "The control bus carries:", opts: ["Control signals", "Only addresses", "Only data", "Power"], a: 0, why: "Control signals." },
  { q: "Which is a general purpose register?", opts: ["Accumulator", "PC", "MAR", "SR"], a: 0, why: "ACC." },
  { q: "The stored program concept means:", opts: ["Instructions and data are in the same memory", "Programs are stored on paper", "Data is in ROM only", "The CPU stores programs"], a: 0, why: "Same memory space." },
  { q: "A wider data bus allows:", opts: ["More data to be transferred at once", "More memory addresses", "A faster clock", "More registers"], a: 0, why: "More data at once." },
  { q: "The system clock:", opts: ["Synchronises operations with timing signals", "Stores data", "Does arithmetic", "Holds the PC"], a: 0, why: "Timing signals." },
] });
Lib.cards($("#fc1"), { cards: [
  ["ALU", "Arithmetic and logic operations."],
  ["CU", "Decodes, coordinates and sends control signals."],
  ["PC", "Address of the next instruction."],
  ["MAR", "Address being read or written."],
  ["MDR", "Data read or to be written."],
  ["CIR", "Instruction being executed."],
  ["Address bus", "Carries the address; one way."],
  ["Data bus", "Carries data and instructions; both ways."],
] });
