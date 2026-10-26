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
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(60, 30, 200, 20, "cell", { rx: 4 }) + SV.text(160, 46, "platter (magnetic surface)", "sm", { "text-anchor": "middle" }) + SV.path("M60,70 H260", "ax") + SV.text(160, 90, "spindle rotates the platter", "sm", { "text-anchor": "middle" });
    o += SV.rect(300, 40, 90, 24, "f3", { rx: 4 }) + SV.text(345, 57, "arm + head", "sm", { "text-anchor": "middle" }); if (k >= 1) o += SV.path("M300,52 H260", "ax");
    if (k >= 2) for (let i = 0; i < 8; i++) o += SV.rect(70 + i * 24, 34, 20, 12, i % 2 ? "f1" : "f2", { rx: 2 }); if (k >= 3) o += SV.text(160, 125, "write: head sets the magnetic pattern", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); if (k >= 4) o += SV.text(160, 148, "read: head detects the pattern", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 170, label: "Hard disk", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "Platters are mounted on a spindle in a sealed box.", s: { i: 0 } }, { cap: "The head on its arm is positioned just above the surface.", s: { i: 1 } }, { cap: "The surface is magnetised in tiny areas arranged in tracks and sectors.", s: { i: 2 } }, { cap: "<b>Writing:</b> the head's magnetic field sets the pattern.", s: { i: 3 } }, { cap: "<b>Reading:</b> the head detects the magnetic pattern.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(150, 20, "Resistive", "lbl bd", { "text-anchor": "middle" }) + SV.text(450, 20, "Capacitive", "lbl bd", { "text-anchor": "middle" }) + SV.rect(60, 50 + (k >= 1 ? 22 : 0), 180, 14, "f3", { rx: 3 }) + SV.rect(60, 100, 180, 14, "cell", { rx: 3 }) + SV.rect(360, 50, 180, 14, "f3", { rx: 3 }) + SV.rect(360, 70, 180, 14, "cell", { rx: 3 }) + SV.rect(360, 90, 180, 14, "cell", { rx: 3 });
    if (k >= 1) o += SV.text(150, 140, "layers touch: circuit completed", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }) + SV.circle(450, 36, 12, "f1"); if (k >= 2) o += SV.text(450, 140, "current changes at the touch", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); if (k >= 3) o += SV.text(300, 165, "A microprocessor works out the coordinates", "sm", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 180, label: "Touchscreens", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "Two designs of touchscreen.", s: { i: 0 } }, { cap: "<b>Resistive:</b> pressing pushes the top layer onto the bottom layer.", s: { i: 1 } }, { cap: "<b>Capacitive:</b> a finger changes the electric current of the top layers.", s: { i: 2 } }, { cap: "Either way, a microprocessor identifies the coordinates of the touch.", s: { i: 3 } }] });
})();
(function () {
  const draw = (s) => { const n = Math.round(s.i); let o = SV.rect(150, 160, 300, 14, "cell", { rx: 3 }) + SV.text(300, 190, "build plate", "sm", { "text-anchor": "middle" }); for (let i = 0; i < n; i++) o += SV.rect(190 + i * 4, 146 - i * 14, 220 - i * 8, 12, i % 2 ? "f1" : "f2", { rx: 2 }); o += SV.rect(150 + n * 8, 20, 40, 22, "f3", { rx: 3 }) + SV.text(170 + n * 8, 36, "nozzle", "sm", { "text-anchor": "middle" }); o += SV.text(480, 80, n ? "layer " + n : "CAD model sliced into layers", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 600, h: 200, label: "3D printer", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: [{ cap: "A digital CAD model is sliced into thin layers.", s: { i: 0 } }, { cap: "The first layer is deposited on the plate.", s: { i: 1 } }, { cap: "Each new layer is fused to the one below.", s: { i: 2 } }, { cap: "The object is built <b>upwards, layer by layer</b>.", s: { i: 3 } }, { cap: "The finished object is complete (additive manufacturing).", s: { i: 4 } }] });
})();

(function () {
  let hh = 60, lh = 0.2; const paint = () => { const layers = Math.round(hh / lh); const mins = Math.round(layers * 40 / 60); $("#lV").innerHTML = `<b>${layers}</b> layers at 40 s each is about <b>${mins} minutes</b>. Thinner layers give a smoother surface but take much longer.`; };
  Lib.slider($("#lS1"), { id: "l1", label: "Object height (mm) ", min: 10, max: 120, value: hh, fmt: (x) => x, onInput: (v) => { hh = v; paint(); } });
  Lib.slider($("#lS2"), { id: "l2", label: "Layer height (mm) ", min: 0.1, max: 0.4, step: 0.05, value: lh, fmt: (x) => x.toFixed(2), onInput: (v) => { lh = v; paint(); } }); paint();
})();
btnTable("dB", "dO", [
  ["Coil moves past a magnet when a diaphragm vibrates", "Microphone", "Sound wave to electrical signal"],
  ["Heated rollers melt powder onto paper", "Laser printer", "The fuser"],
  ["Laser reads pits and lands", "Optical disc drive", "Reflection differs"],
  ["Gyroscope reports head movement", "VR headset", "Direction and speed"],
  ["Builds an object from a CAD file one layer at a time", "3D printer", "Additive manufacturing"],
  ["Floating gate holds electrons", "Solid state drive", "Flash memory"]
], ["Description", "Device", "Key point"]);
btnTable("tB", "tO", [
  ["Works with a pen, glove or any pressing object", "Resistive", "Pressure completes a circuit"],
  ["Needs a finger or other conductive object", "Capacitive", "Detects a change in current"],
  ["Two layers separated by a small gap", "Resistive", "Layers touch"],
  ["Several layers, top layer is glass", "Capacitive", "Used in most phones"],
  ["A circuit is completed at the point of contact", "Resistive", "Microprocessor finds the coordinates"]
], ["Description", "Type", "Key point"]);
Lib.classify($("#cl1"), { prompt: "Magnetic hard disk or solid state drive?", buckets: [{"label": "Magnetic hard disk"}, {"label": "Solid state drive"}], items: [{"text": "Platters on a spindle", "b": 0}, {"text": "Floating gate and control gate", "b": 1}, {"text": "Read/write head on an arm", "b": 0}, {"text": "NAND or NOR gates", "b": 1}, {"text": "Data stored as magnetised areas", "b": 0}, {"text": "No moving parts", "b": 1}], done: "Magnetic: moving parts. Solid state: transistors." });
Lib.classify($("#cl2"), { prompt: "Resistive or capacitive touchscreen?", buckets: [{"label": "Resistive"}, {"label": "Capacitive"}], items: [{"text": "Two layers touch to complete a circuit", "b": 0}, {"text": "Change in electric current when touched", "b": 1}, {"text": "Works with any pressing object", "b": 0}, {"text": "Needs a conductive object such as a finger", "b": 1}, {"text": "Pressure presses top layer to the bottom layer", "b": 0}, {"text": "Several layers, top is glass", "b": 1}], done: "Resistive presses together; capacitive senses the finger." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Diaphragm", "Microphone vibrates with sound waves"], ["Fuser", "Laser printer melts toner onto paper"], ["Gyroscope", "VR headset detects head movement"], ["Floating gate", "Flash memory holds electrons without power"], ["Nozzle", "FDM 3D printer pushes heated material out"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the laser printer stages in order.", items: ["Page data is received and built into an image", "A laser draws the image onto the charged drum", "Toner sticks to the charged areas of the drum", "Toner transfers from the drum to the paper", "A fuser melts the toner into the paper"], done: "Image, laser, toner on drum, to paper, fuse." });
Lib.calc($("#c1"), { qs: [
  {"q": "A 3D object is 60 mm high and printed in layers of 0.2 mm. How many layers?", "a": 300, "unit": "", "tol": 0.01, "hint": "60 ÷ 0.2.", "sol": "<b>300</b>."},
  {"q": "Each layer takes 40 seconds. How many minutes to print the 300 layers?", "a": 200, "unit": "min", "tol": 0.5, "hint": "300 × 40 = 12000 s ÷ 60.", "sol": "<b>200</b> min."},
  {"q": "A disk spins at 7200 revolutions per minute. How many revolutions per second?", "a": 120, "unit": "", "tol": 0.01, "hint": "7200 ÷ 60.", "sol": "<b>120</b>."},
  {"q": "A flash cell stores 1 bit. How many cells are needed to store 1 byte?", "a": 8, "unit": "", "tol": 0.01, "hint": "8 bits.", "sol": "<b>8</b>."},
  {"q": "A sound is sampled 44100 times a second with 2 bytes per sample. How many bytes per second (one channel)?", "a": 88200, "unit": "bytes", "tol": 0.5, "hint": "44100 × 2.", "sol": "<b>88200</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which device uses a diaphragm?", opts: ["Microphone", "Laser printer", "Hard disk", "SSD"], a: 0, why: "Microphone." },
  { q: "Which part of flash memory retains electrons without power?", opts: ["Floating gate", "Control gate", "Platter", "Spindle"], a: 0, why: "Floating gate." },
  { q: "A 3D printer builds an object:", opts: ["Layer by layer", "By cutting from a block", "By melting everything at once", "By photographing it"], a: 0, why: "Additive manufacturing." },
  { q: "A capacitive touchscreen detects:", opts: ["A change in electric current", "A completed circuit between layers", "Sound", "Heat only"], a: 0, why: "Change in current." },
  { q: "A VR headset detects head movement with:", opts: ["Gyroscope or accelerometer", "A laser drum", "A platter", "A fuser"], a: 0, why: "Gyroscope." },
  { q: "On a hard disk the surface is divided into:", opts: ["Tracks and sectors", "Pits and lands", "Cells and gates", "Layers"], a: 0, why: "Tracks and sectors." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Hard disk", "Platters, spindle, head on arm, magnetised areas."],
  ["SSD", "NAND/NOR, floating gate, control gate."],
  ["Optical disc", "Laser reads pits and lands."],
  ["Resistive screen", "Layers touch, circuit completed."],
  ["Capacitive screen", "Change in electric current."],
  ["Microphone", "Diaphragm, coil and magnet, electrical signal."],
  ["Laser printer", "Charged drum, toner, fuser."],
  ["3D printer", "Additive; layer by layer from a CAD model."],
] });
