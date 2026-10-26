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
  const draw = (s) => { const k = Math.round(s.i); const bx = (x, y, w, t, c) => SV.rect(x, y, w, 46, c || "cell", { rx: 8 }) + SV.text(x + w / 2, y + 28, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" });
    let o = bx(20, 50, 100, "Input", k >= 1 ? "cell-warn" : "cell") + bx(180, 50, 140, "Processor", k >= 2 ? "cell-warn" : "cell") + bx(380, 50, 100, "Output", k >= 3 ? "cell-warn" : "cell") + SV.path("M120,73 H180", "ax") + SV.path("M320,73 H380", "ax");
    o += bx(180, 150, 140, "Primary memory", k >= 2 ? "f3" : "cell") + SV.path("M250,96 V150", "ax") + bx(380, 150, 150, "Secondary storage", k >= 4 ? "cell-warn" : "cell") + SV.path("M320,173 H380", "ax", { style: "stroke-dasharray:5 4" });
    o += SV.text(20, 130, k === 0 ? "" : ["", "keyboard, mouse, sensors", "RAM holds programs and data in use", "screen, printer, speakers", "saved permanently, kept without power"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 220, label: "Computer parts", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "A computer takes in data, works on it, gives results and stores things.", s: { i: 0 } }, { cap: "<b>Input devices</b> get data into the computer.", s: { i: 1 } }, { cap: "The processor works on data held in <b>primary memory</b> (RAM and ROM), which it can reach directly.", s: { i: 2 } }, { cap: "<b>Output devices</b> present the results.", s: { i: 3 } }, { cap: "<b>Secondary storage</b> keeps data permanently. Data must be loaded into RAM before the processor can use it.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 40, 120, 70, "cell", { rx: 8 }) + SV.text(80, 70, "Computer", "lbl bd", { "text-anchor": "middle" }) + SV.text(80, 92, k >= 3 ? "free for other tasks" : "", "sm", { "text-anchor": "middle" }) + SV.rect(230, 55, 140, 40, "cell", { rx: 6 }) + SV.text(300, 80, "buffer", "lbl bd", { "text-anchor": "middle" }) + SV.rect(470, 40, 110, 70, "cell", { rx: 8 }) + SV.text(525, 70, "Printer", "lbl bd", { "text-anchor": "middle" }) + SV.text(525, 92, "(slow)", "sm", { "text-anchor": "middle" });
    const fill = [0, 5, 5, 3, 0][k]; for (let i = 0; i < 5; i++) o += SV.rect(238 + i * 25, 62, 20, 26, i < fill ? "f1" : "cell", { rx: 3 }); if (k >= 1) o += SV.path("M140,75 H230", "ax", { style: "stroke:var(--accent);stroke-width:3" }) + SV.text(185, 62, "fast", "sm", { "text-anchor": "middle" }); if (k >= 2) o += SV.path("M370,75 H470", "ax", { style: "stroke:var(--good);stroke-width:3" }) + SV.text(420, 62, "slow", "sm", { "text-anchor": "middle" }); if (k >= 4) o += SV.text(300, 150, "buffer empty: interrupt asks the computer for more data", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 170, label: "Buffer", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "The computer works much faster than the printer.", s: { i: 0 } }, { cap: "The computer sends the print data to the <b>buffer</b> at its own high speed.", s: { i: 1 } }, { cap: "The printer takes data from the buffer at its own, slower speed.", s: { i: 2 } }, { cap: "The computer is <b>free to carry on</b> instead of waiting for the printer.", s: { i: 3 } }, { cap: "When the buffer is empty the printer sends an <b>interrupt</b> asking for more data.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(210, 30, 180, 140, "f3", { rx: 12, ...op(0.5) }) + SV.text(300, 54, "Microcontroller", "lbl bd", { "text-anchor": "middle" }) + SV.rect(225, 66, 70, 34, "cell", { rx: 4 }) + SV.text(260, 88, "ROM", "lbl bd", { "text-anchor": "middle" }) + SV.rect(305, 66, 70, 34, "cell", { rx: 4 }) + SV.text(340, 88, "RAM", "lbl bd", { "text-anchor": "middle" });
    o += SV.rect(20, 80, 110, 40, "cell", { rx: 6 }) + SV.text(75, 105, "buttons, sensors", "lbl", { "text-anchor": "middle", style: "font-size:12px" }) + SV.rect(470, 80, 110, 40, "cell", { rx: 6 }) + SV.text(525, 105, "motor, heater", "lbl", { "text-anchor": "middle", style: "font-size:12px" });
    if (k >= 1) o += SV.path("M130,100 H210", "ax", { style: "stroke:var(--accent);stroke-width:3" }); if (k >= 2) o += SV.text(260, 125, "program", "sm", { "text-anchor": "middle" }) + SV.text(340, 125, "choices, readings", "sm", { "text-anchor": "middle" }); if (k >= 3) o += SV.path("M390,100 H470", "ax", { style: "stroke:var(--good);stroke-width:3" }); return o; };
  Lib.stepper($("#stC"), { w: 600, h: 190, label: "Embedded system", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "A washing machine contains an <b>embedded system</b>: a microcontroller that does one job.", s: { i: 0 } }, { cap: "Inputs: the user's choices and sensor readings arrive.", s: { i: 1 } }, { cap: "<b>ROM</b> holds the wash programme (start-up instructions); <b>RAM</b> holds the choices, readings and the time left.", s: { i: 2 } }, { cap: "Outputs control the motor and heater. It does nothing else.", s: { i: 3 } }] });
})();

(function () {
  let inr = 8, out = 3, size = 20; const paint = () => { const T = 20; let buf = 0, sent = 0, stall = 0; const pts = []; for (let t = 0; t <= T; t++) { pts.push(buf); const room = size - buf; const push = Math.min(inr, room); if (push < inr) stall++; buf += push; sent += push; buf = Math.max(0, buf - out); } let d = ""; pts.forEach((p, i) => (d += (i ? "L" : "M") + (40 + i * 18) + "," + (140 - (p / Math.max(size, 1)) * 100) + " "));
    $("#bG").innerHTML = `<svg viewBox="0 0 420 170" style="width:420px;max-width:100%;display:block"><path d="M40,20 V140 H400" class="ax"/><line x1="40" y1="40" x2="400" y2="40" stroke="var(--bad)" stroke-dasharray="5 4"/><text x="46" y="34" class="sm" style="font-size:11px">buffer full (${size} units)</text><path d="${d}" fill="none" stroke="var(--accent)" stroke-width="3"/><text x="400" y="162" class="sm" text-anchor="end" style="font-size:11px">time</text></svg>`;
    $("#bV").innerHTML = inr <= out ? "The printer is as fast as the computer: the buffer is hardly needed." : stall ? `The buffer fills up (${size} units) and the computer has to <b>wait</b> from time to time. A bigger buffer, or a faster printer, would help.` : "The buffer is big enough: the computer sends everything quickly and is then <b>free for other tasks</b>."; };
  Lib.slider($("#bS1"), { id: "b1", label: "Computer speed (units per second) ", min: 1, max: 20, value: inr, fmt: (x) => x, onInput: (v) => { inr = v; paint(); } });
  Lib.slider($("#bS2"), { id: "b2", label: "Printer speed (units per second) ", min: 1, max: 20, value: out, fmt: (x) => x, onInput: (v) => { out = v; paint(); } });
  Lib.slider($("#bS3"), { id: "b3", label: "Buffer size (units) ", min: 5, max: 200, value: size, fmt: (x) => x, onInput: (v) => { size = v; paint(); } }); paint();
})();
btnTable("pB", "pO", [
  ["The program currently running", "Primary memory (RAM)", "The processor accesses it directly"],
  ["Start-up (boot) instructions", "Primary memory (ROM)", "Non-volatile, read by the processor at start-up"],
  ["Your saved photographs", "Secondary storage", "Kept without power; loaded into RAM to view"],
  ["A backup taken to another site", "Removable secondary storage", "Can be taken out and moved"],
  ["The current journey's mileage in a car", "Primary memory", "Only needed while the journey is in progress"],
  ["The car's lifetime mileage", "Secondary storage", "Must survive power being switched off"]
], ["Item", "Where", "Why"]);
btnTable("eB", "eO", [
  ["The controller in a washing machine", "Embedded", "One dedicated task inside a larger device"],
  ["A school laptop", "General-purpose", "Runs many programs and an operating system"],
  ["A video doorbell's motion controller", "Embedded", "Built in; dedicated to detecting and recording"],
  ["A games console", "General-purpose", "Runs many different games and apps"],
  ["Lane detection in a car", "Embedded", "Built in; one task; owner cannot change it"],
  ["A smartphone", "General-purpose", "Many apps; the user installs software"]
], ["Device", "Type", "Reason"]);
Lib.classify($("#cl1"), { prompt: "Is it primary memory or secondary storage?", buckets: [{"label": "Primary memory"}, {"label": "Secondary storage"}], items: [{"text": "RAM", "b": 0}, {"text": "Magnetic hard disk", "b": 1}, {"text": "Directly accessed by the processor", "b": 0}, {"text": "Keeps data when the power is off, in large amounts", "b": 1}, {"text": "Holds the start-up instructions in ROM", "b": 0}, {"text": "USB flash drive", "b": 1}], done: "Primary: reached directly. Secondary: permanent, loaded into RAM first." });
Lib.classify($("#cl2"), { prompt: "Is it a benefit or a drawback of embedded systems?", buckets: [{"label": "Benefit"}, {"label": "Drawback"}], items: [{"text": "Cheap and small", "b": 0}, {"text": "Firmware is hard for the user to update", "b": 1}, {"text": "Reliable because it does one task", "b": 0}, {"text": "Faulty devices are often thrown away", "b": 1}, {"text": "Needs little processing power", "b": 0}, {"text": "Cannot easily be adapted for another task", "b": 1}], done: "Dedicated: cheap and reliable, but fixed." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Embedded system", "A dedicated microprocessor inside a larger device"], ["Buffer", "A temporary store between devices of different speeds"], ["Primary memory", "Memory the processor can access directly"], ["Secondary storage", "Permanent non-volatile storage"], ["Removable storage", "Storage that can be moved between computers"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the printing steps with a buffer in order.", items: ["The computer sends the data to the buffer at its own speed", "The processor carries on with other tasks", "The buffer passes data to the printer at the printer's speed", "The buffer becomes empty", "The printer sends an interrupt asking for more data"], done: "Send, carry on, pass on, empty, interrupt." });
Lib.calc($("#c1"), { qs: [
  {"q": "A computer sends 120 pages' data to the buffer in 6 seconds and the printer prints 4 pages per second. How many seconds does printing take?", "a": 30, "unit": "s", "tol": 0.1, "hint": "120 ÷ 4.", "sol": "<b>30</b> s."},
  {"q": "In the same case, how many seconds is the computer free to do other tasks while the printer works (after the 6 s)?", "a": 24, "unit": "s", "tol": 0.1, "hint": "30 − 6.", "sol": "<b>24</b> s."},
  {"q": "A video file of 4 GB is stored on a 500 GB drive. How many such files fit (whole files)?", "a": 125, "unit": "", "tol": 0.01, "hint": "500 ÷ 4.", "sol": "<b>125</b>."},
  {"q": "A washing machine controller stores 12 programs of 2 KiB each in ROM. How many KiB is that?", "a": 24, "unit": "KiB", "tol": 0.01, "hint": "12 × 2.", "sol": "<b>24</b> KiB."},
  {"q": "How many examples of removable storage were listed in the Learn tab (USB drive, optical disc, external hard disk, memory card)?", "a": 4, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>4</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which keeps data when the power is off?", opts: ["RAM", "Secondary storage", "Cache only", "Registers"], a: 1, why: "Secondary storage." },
  { q: "An embedded system:", opts: ["Does one dedicated task inside a larger device", "Is a general-purpose PC", "Has no processor", "Is a type of cable"], a: 0, why: "Dedicated task." },
  { q: "A buffer is used when:", opts: ["Devices work at different speeds", "A device is switched off", "Data is deleted", "A file is compressed"], a: 0, why: "Different speeds." },
  { q: "In a washing machine, ROM stores:", opts: ["The start-up instructions", "The time left", "The user's choices", "Nothing"], a: 0, why: "Start-up instructions." },
  { q: "Removable storage is:", opts: ["Taken out and moved between computers", "Always inside the CPU", "The same as RAM", "Only wireless"], a: 0, why: "Can be moved." },
  { q: "An embedded-system drawback is:", opts: ["Firmware hard to update", "Too many functions", "Too much processing", "Too large"], a: 0, why: "Hard to update." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Input / output", "Data in / results out."],
  ["Primary memory", "RAM and ROM; direct access."],
  ["Secondary storage", "Permanent; larger; slower."],
  ["Removable storage", "USB drive, optical disc."],
  ["Embedded system", "Dedicated microprocessor in a larger device."],
  ["Embedded drawbacks", "Hard to update, repair, adapt; e-waste."],
  ["Buffer", "Temporary store until the device is ready."],
  ["Buffer interrupt", "Empty: ask for more. Full: stop sending."],
] });
