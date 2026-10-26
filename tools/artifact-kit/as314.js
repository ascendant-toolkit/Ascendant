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
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 60, 110, 46, "cell", { rx: 8 }) + SV.text(75, 88, "Sensor", "lbl bd", { "text-anchor": "middle" }) + SV.rect(200, 60, 150, 46, k >= 1 ? "f3" : "cell", { rx: 8 }) + SV.text(275, 88, "Microprocessor", "lbl bd", { "text-anchor": "middle" }) + SV.rect(420, 60, 110, 46, k >= 2 ? "f1" : "cell", { rx: 8 }) + SV.text(475, 88, "Cooling", "lbl bd", { "text-anchor": "middle" }) + SV.path("M130,83 H200", "ax") + SV.path("M350,83 H420", "ax");
    if (k >= 3) o += SV.path("M475,106 V150 H75 V106", "ax", { style: "stroke:var(--accent);stroke-width:3;stroke-dasharray:6 4" }) + SV.text(275, 144, "feedback: the cooling changes the temperature", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); o += SV.text(275, 30, ["", "temperature above 6 °C?", "signal to the actuator", "", ""][k], "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 600, h: 175, label: "Control loop", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "A fridge measures its temperature with a <b>sensor</b>.", s: { i: 0 } }, { cap: "The <b>microprocessor</b> compares it with 4 and 6 °C.", s: { i: 1 } }, { cap: "Above 6 °C it signals the <b>actuator</b> to switch the cooling on.", s: { i: 2 } }, { cap: "The cooling lowers the temperature, which the sensor then measures: <b>feedback</b>.", s: { i: 3 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 60, 110, 46, "cell", { rx: 8 }) + SV.text(75, 88, "Sensors", "lbl bd", { "text-anchor": "middle" }) + SV.rect(200, 60, 150, 46, k >= 1 ? "f3" : "cell", { rx: 8 }) + SV.text(275, 88, "Processor", "lbl bd", { "text-anchor": "middle" }) + SV.rect(420, 60, 110, 46, k >= 2 ? "f1" : "cell", { rx: 8 }) + SV.text(475, 88, "Alarm / display", "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }) + SV.path("M130,83 H200", "ax") + SV.path("M350,83 H420", "ax");
    if (k >= 3) o += SV.text(275, 140, "no actuator, no feedback: output does not change the sensor input", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 165, label: "Monitoring", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "A monitoring system reads its sensors.", s: { i: 0 } }, { cap: "The processor analyses the data.", s: { i: 1 } }, { cap: "It displays, records or sounds a warning.", s: { i: 2 } }, { cap: "Nothing the system does changes what the sensors measure: <b>no loop</b>.", s: { i: 3 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const bx = (x, t, on) => SV.rect(x, 60, 100, 46, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 50, 88, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); let o = bx(10, "Sensor", k >= 0) + bx(140, "ADC", k >= 1) + bx(270, "Processor", k >= 2) + bx(400, "DAC", k >= 3) + bx(530, "Actuator", k >= 4); for (let i = 0; i < 4; i++) o += SV.path(`M${110 + i * 130},83 H${140 + i * 130}`, "ax"); o += SV.text(300, 140, ["analogue reading", "analogue becomes digital", "decides what to do", "digital becomes analogue (if needed)", "physical action"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 650, h: 165, label: "Signal path", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: [{ cap: "The sensor measures a physical quantity.", s: { i: 0 } }, { cap: "The <b>ADC</b> converts the analogue signal to digital.", s: { i: 1 } }, { cap: "The microprocessor compares it with the set limits.", s: { i: 2 } }, { cap: "A <b>DAC</b> converts the output for the actuator if it needs an analogue signal.", s: { i: 3 } }, { cap: "The <b>actuator</b> changes the environment.", s: { i: 4 } }] });
})();

(function () {
  let lo = 4, hi = 6; const paint = () => { if (hi <= lo) hi = lo + 0.5; let t = 7, on = false, d = "", out = 0; for (let i = 0; i <= 120; i++) { if (t > hi) on = true; if (t < lo) on = false; t += on ? -0.18 : 0.12; if (t < lo - 0.3 || t > hi + 0.3) out++; d += (i ? "L" : "M") + (30 + i * 3.1) + "," + (150 - (t - 2) * 14) + " "; }
    const y = (v) => 150 - (v - 2) * 14;
    $("#fG").innerHTML = `<svg viewBox="0 0 420 170" style="width:420px;max-width:100%;display:block"><rect x="30" y="${y(hi)}" width="372" height="${y(lo) - y(hi)}" fill="var(--accent)" opacity=".15"/><path d="M30,10 V150 H402" class="ax"/><path d="${d}" fill="none" stroke="var(--accent)" stroke-width="2.5"/><text x="34" y="${y(hi) - 3}" class="sm" style="font-size:11px">upper limit ${hi} °C</text><text x="34" y="${y(lo) + 12}" class="sm" style="font-size:11px">lower limit ${lo} °C</text></svg>`;
    $("#fV").innerHTML = `The cooling switches on above <b>${hi} °C</b> and off below <b>${lo} °C</b>. Because the cooling changes the temperature the sensor measures, this is <b>feedback</b>, and the temperature stays near the band. Widen the band and it swings more; narrow it and the cooling switches more often.`; };
  Lib.slider($("#fS1"), { id: "f1", label: "Lower limit (°C) ", min: 2, max: 8, step: 0.5, value: lo, fmt: (x) => x, onInput: (v) => { lo = v; paint(); } });
  Lib.slider($("#fS2"), { id: "f2", label: "Upper limit (°C) ", min: 3, max: 12, step: 0.5, value: hi, fmt: (x) => x, onInput: (v) => { hi = v; paint(); } }); paint();
})();
btnTable("mB", "mO", [
  ["Fridge that switches cooling on and off", "Control", "Actuator; the cooling changes the temperature"],
  ["Health monitor that sends heart rate to a phone", "Monitoring", "No actuator; output does not affect the input"],
  ["Automatic doors", "Control", "Motor; people moving changes the sensor input"],
  ["Burglar alarm that sounds a siren", "Monitoring", "Warning only"],
  ["Car that brakes harder as the object gets closer", "Control", "Braking changes the distance"],
  ["Weather station", "Monitoring", "Records only"]
], ["System", "Type", "Why"]);
btnTable("nB", "nO", [
  ["Floodlight that comes on at dusk", "Light sensor", "Daylight level"],
  ["Counting bars on a conveyor belt", "Infra-red sensor", "Detects each bar passing"],
  ["Detecting that a door is open", "Pressure or infra-red sensor", "Pad or beam"],
  ["Watering a greenhouse", "Moisture or humidity sensor", "Dryness"],
  ["Keeping a 3D printer's nozzle hot enough", "Temperature sensor", "Prevents overheating"]
], ["Task", "Sensor", "Why"]);
Lib.classify($("#cl1"), { prompt: "Monitoring system or control system?", buckets: [{"label": "Monitoring"}, {"label": "Control"}], items: [{"text": "Records heart rate and sends it to a phone", "b": 0}, {"text": "Switches a heater on when it is too cold", "b": 1}, {"text": "The output does not affect the sensor input", "b": 0}, {"text": "Uses feedback", "b": 1}, {"text": "Has no actuator", "b": 0}, {"text": "Opens a door when a person is detected", "b": 1}], done: "Control: actuator and feedback." });
Lib.classify($("#cl2"), { prompt: "Sensor or actuator?", buckets: [{"label": "Sensor"}, {"label": "Actuator"}], items: [{"text": "Infra-red detector", "b": 0}, {"text": "Motor that opens a door", "b": 1}, {"text": "Pressure pad", "b": 0}, {"text": "Heater", "b": 1}, {"text": "Light-dependent resistor", "b": 0}, {"text": "Valve that waters a greenhouse", "b": 1}], done: "Sensors input; actuators act." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Temperature sensor", "Heating, fridge or 3D printer"], ["Light sensor", "Floodlight at dusk"], ["Pressure sensor", "Detecting an open door"], ["Infra-red sensor", "Counting items on a conveyor"], ["Moisture sensor", "Watering plants"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the control loop in order.", items: ["The sensor measures the temperature", "The ADC converts the reading to digital", "The microprocessor compares it with the limits", "The microprocessor signals the actuator", "The actuator changes the temperature, which the sensor then measures"], done: "Sense, convert, compare, signal, act, repeat." });
Lib.calc($("#c1"), { qs: [
  {"q": "A fridge stays between 4 and 6 °C. How wide is the allowed range in °C?", "a": 2, "unit": "°C", "tol": 0.01, "hint": "6 − 4.", "sol": "<b>2</b> °C."},
  {"q": "A sensor reading is 0 to 5 V and an ADC has 8 bits. How many different values can it give?", "a": 256, "unit": "", "tol": 0.01, "hint": "2^8.", "sol": "<b>256</b>."},
  {"q": "A temperature is read every 2 seconds. How many readings in one minute?", "a": 30, "unit": "", "tol": 0.01, "hint": "60 ÷ 2.", "sol": "<b>30</b>."},
  {"q": "An infra-red sensor counts 3 bars each second for 90 seconds. How many bars?", "a": 270, "unit": "", "tol": 0.01, "hint": "3 × 90.", "sol": "<b>270</b>."},
  {"q": "X = E AND A AND C. For E=1, A=1, C=0, what is X?", "a": 0, "unit": "", "tol": 0.01, "hint": "AND needs all 1.", "sol": "<b>0</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A control system must have:", opts: ["An actuator and feedback", "Only a display", "A printer", "No sensor"], a: 0, why: "Actuator and feedback." },
  { q: "A monitoring system:", opts: ["Output does not affect the input", "Always has an actuator", "Uses feedback", "Controls a motor"], a: 0, why: "No effect on the input." },
  { q: "An actuator:", opts: ["Causes a physical action", "Measures light", "Stores data", "Converts digital to text"], a: 0, why: "Causes an action." },
  { q: "An ADC:", opts: ["Analogue to digital", "Digital to analogue", "Adds data", "Draws"], a: 0, why: "Analogue to digital." },
  { q: "Which sensor counts items on a conveyor belt?", opts: ["Infra-red", "pH", "Sound", "Humidity"], a: 0, why: "Infra-red." },
  { q: "Feedback means:", opts: ["Output affects the next input", "Data is stored", "Power is saved", "A message is sent"], a: 0, why: "Output affects input." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Sensor", "Measures a physical quantity."],
  ["Actuator", "Causes a physical action."],
  ["Monitoring", "No actuator, no feedback."],
  ["Control", "Actuator and feedback."],
  ["Feedback", "Output affects the next input."],
  ["ADC", "Analogue to digital."],
  ["DAC", "Digital to analogue."],
  ["Autonomous", "Acts without a person deciding."],
] });
