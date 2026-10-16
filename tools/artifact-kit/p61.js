const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)", WARN = "var(--warn)";
const note = (x, y, t, cls = "", anchor = "middle") => SV.text(x, y, t, "lbl bd " + cls, { "text-anchor": anchor });
const sm = (x, y, t, anchor = "middle") => SV.text(x, y, t, "sm", { "text-anchor": anchor });
const panel = (x, y, w, h, title, col, o = 1) => SV.rect(x, y, w, h, "", { rx: 12, style: `fill:var(--surface);stroke:${col};stroke-width:3`, opacity: o }) + (title ? SV.text(x + w / 2, y + 22, title, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) : "");
const arr = (x1, y1, x2, y2, col, dash) => SV.line(x1, y1, x2, y2, "", { style: `stroke:${col};stroke-width:3;${dash ? "stroke-dasharray:7 6" : ""}` });
const chip = (x, y, w, t, col) => SV.rect(x, y, w, 26, "", { rx: 13, style: `fill:${col}` }) + SV.text(x + w / 2, y + 18, t, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:12px" });
const range = (a, b) => { const r = []; for (let i = a; i <= b; i++) r.push(i); return r; };
/* select-one-per-row chooser. items: [text, correctOption] */
function chooser(el, v, opts, items, ph) {
  el.innerHTML = items.map((s) => `<div class="r" data-a="${esc(s[1])}"><span class="q">${s[0]}</span><select class="sel" aria-label="${esc(s[0].replace(/<[^>]+>/g, ""))}"><option value="">${ph || "Choose…"}</option>${opts.map((x) => `<option>${esc(x)}</option>`).join("")}</select></div>`).join("");
  v.textContent = "Choose an answer for each row.";
  $$(".r", el).forEach((r) => $("select", r).addEventListener("change", (e) => { r.classList.remove("ok", "no"); if (e.target.value) r.classList.add(e.target.value === r.dataset.a ? "ok" : "no"); v.textContent = `${$$(".r.ok", el).length} of ${$$(".r", el).length} correct. Red means a different answer fits better.`; }));
}
/* ---------- 1. street light ---------- */
function slChart(s) {
  const k = Math.round(s.k), night = k >= 1 && k <= 3, reading = [80, 25, 25, 5, 60][k], on = k === 3 || k === 2 && false;
  let o = SV.rect(10, 10, 290, 230, "", { rx: 12, style: `fill:${night ? "#1f2a44" : "#cfe6f7"};stroke:var(--line);stroke-width:2` });
  o += night ? SV.circle(240, 55, 22, "", { style: "fill:#f3f0d8" }) + SV.circle(250, 50, 18, "", { style: "fill:#1f2a44" }) : SV.circle(240, 55, 24, "", { style: "fill:#f5c542" });
  o += SV.rect(110, 90, 8, 130, "", { style: "fill:#555" }) + SV.rect(80, 84, 60, 10, "", { rx: 4, style: "fill:#555" }) + SV.circle(110, 104, 12, "", { style: `fill:${on ? "#ffe066" : "#999"}` });
  if (on) o += SV.poly([[96, 112], [124, 112], [160, 220], [60, 220]], "", { style: "fill:#ffe066;opacity:.3" });
  o += SV.rect(10, 220, 290, 20, "", { style: "fill:#3b6b3b" });
  o += panel(330, 40, 120, 110, "Light sensor", k === 1 || k === 4 ? ACC : MUT) + SV.text(390, 100, String(reading), "lbl bd", { "text-anchor": "middle", style: "font-size:28px;font-family:var(--mono)" }) + sm(390, 125, "reading");
  o += panel(480, 40, 130, 110, "Microprocessor", k === 2 || k === 4 ? ACC : MUT) + sm(545, 85, "stored value: 30") + SV.text(545, 118, k === 2 ? "25 < 30: ON" : k === 4 ? "60 > 30: OFF" : k === 1 ? "comparing…" : "waiting", "lbl bd", { "text-anchor": "middle", style: `fill:${k === 2 ? GOOD : k === 4 ? BAD : "var(--muted)"}` });
  o += panel(640, 40, 110, 110, "Actuator", k === 3 ? GOOD : MUT) + sm(695, 100, "lamp switch") + sm(695, 122, on ? "ON" : "OFF");
  if (k >= 1) o += arr(450, 95, 480, 95, ACC); if (k >= 2 && k !== 4 || k === 4) o += arr(610, 95, 640, 95, k === 4 ? BAD : GOOD);
  o += note(540, 200, ["Daytime: bright, lamp off", "Dusk: the light level falls", "25 is below the stored value of 30", "Night: lamp on", "Dawn: 60 is above 30, lamp off"][k], "t1");
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 250, label: "An automatic street light", base: { k: 0 }, tween: 1, dwell: 3800, draw: slChart, steps: [
  { cap: "It is day. The <b>light sensor</b> reads 80. The microprocessor has a stored value of <b>30</b>. The lamp is off.", s: { k: 0 } },
  { cap: "At dusk the light falls. The sensor measures <b>25</b> (analogue, converted by an ADC).", s: { k: 1 } },
  { cap: "The <b>microprocessor compares</b> 25 with the stored value 30. It is lower, so it sends the signal to switch the lamp <b>on</b>.", s: { k: 2 } },
  { cap: "The <b>actuator</b> (a switch) turns the lamp on. The sensor keeps measuring through the night.", s: { k: 3 } },
  { cap: "At dawn the sensor reads <b>60</b>, above 30, so the microprocessor sends a signal and the lamp goes <b>off</b>. The loop repeats every day.", s: { k: 4 } },
] });

/* ---------- 2. feedback ---------- */
function fbChart(s) {
  const k = Math.round(s.k), m = s.m, pump = k >= 2 && k <= 4;
  let o = panel(20, 20, 150, 80, "Moisture sensor", k === 1 || k === 5 ? ACC : MUT) + sm(95, 76, "reads " + Math.round(m) + " %");
  o += panel(235, 20, 150, 80, "Microprocessor", k === 1 || k === 4 || k === 5 ? ACC : MUT) + sm(310, 76, "target: 50 %");
  o += panel(450, 20, 140, 80, "Pump (actuator)", pump ? GOOD : MUT) + sm(520, 76, pump ? "ON" : "OFF");
  o += arr(170, 60, 235, 60, ACC) + arr(385, 60, 450, 60, pump ? GOOD : MUT);
  o += SV.rect(640, 20, 100, 170, "", { rx: 10, style: "fill:var(--surface);stroke:var(--muted);stroke-width:2" }) + SV.rect(641, 190 - m * 1.7, 98, m * 1.7, "", { style: "fill:#7a5230;opacity:.8" }) + sm(690, 14, "soil") + SV.line(640, 190 - 85, 740, 190 - 85, "", { style: "stroke:var(--good);stroke-width:2;stroke-dasharray:5 4" });
  o += SV.path("M520 100 L520 150 L640 150", "", { style: `fill:none;stroke:${pump ? "var(--good)" : "var(--muted)"};stroke-width:3;stroke-dasharray:6 5` });
  o += SV.path("M690 190 L690 215 L95 215 L95 100", "", { style: "fill:none;stroke:var(--muted);stroke-width:2;stroke-dasharray:3 4" }) + sm(390, 232, "feedback: the sensor measures the soil again");
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 245, label: "Feedback in automatic watering", base: { k: 0, m: 30 }, tween: 1000, dwell: 3800, draw: fbChart, steps: [
  { cap: "The soil is dry: <b>30 %</b> moisture. The target is 50 %.", s: { k: 0, m: 30 } },
  { cap: "The sensor sends the reading. The microprocessor <b>compares</b> 30 % with the stored target 50 %: too dry.", s: { k: 1, m: 30 } },
  { cap: "It sends a signal to the <b>pump</b> (actuator), which switches on.", s: { k: 2, m: 38 } },
  { cap: "Water soaks in. The sensor keeps measuring: 45 %. Still below 50 %, so the pump stays on.", s: { k: 3, m: 45 } },
  { cap: "At 52 % the microprocessor sees the target is reached and switches the pump <b>off</b>.", s: { k: 4, m: 52 } },
  { cap: "The loop never stops: as the soil dries, the reading falls and the cycle starts again. That is <b>feedback</b>.", s: { k: 5, m: 48 } },
] });

/* ---------- Learn code ---------- */
Lib.codePanel($("#cdAuto"), { pseudo: ["WHILE TRUE DO", "    INPUT Temperature", "    IF Temperature > 26", "      THEN", "        Window ← OPEN", "      ELSE", "        Window ← CLOSED", "    ENDIF", "    IF Temperature < 18", "      THEN", "        Heater ← ON", "      ELSE", "        Heater ← OFF", "    ENDIF", "ENDWHILE"], py: ["while True:", "    temperature = read_sensor()", "    if temperature > 26:", "        window = OPEN", "    else:", "        window = CLOSED", "    if temperature < 18:", "        heater = ON", "    else:", "        heater = OFF"] });

/* ---------- Lab 1: greenhouse ---------- */
(() => {
  let lo, hi, out;
  const svg = $("#gs");
  function sim(auto) {
    const L = lo.get(), H = Math.max(hi.get(), L + 1), O = out.get(); let T = 22, heat = false, win = false, ts = [T], hs = 0, wo = 0, inr = 0;
    for (let i = 0; i < 100; i++) {
      if (auto) { const wasH = heat, wasW = win; heat = T < L ? true : T > L + 1 ? false : heat; win = T > H ? true : T < H - 1 ? false : win; if (heat && !wasH) hs++; if (win && !wasW) wo++; }
      T += (O - T) * 0.06 + (heat ? 1.1 : 0) - (win ? 1.1 : 0); ts.push(T); if (T >= L && T <= H) inr++;
    }
    return { ts, hs, wo, inr };
  }
  function upd() {
    if (!lo || !hi || !out) return;
    const a = sim(true), b = sim(false), L = lo.get(), H = Math.max(hi.get(), L + 1), y = (t) => 220 - ((t - 0) / 45) * 200, x = (i) => 40 + i * 5.7;
    let s = SV.rect(40, y(H), 570, y(L) - y(H), "", { style: "fill:var(--good-soft)" }) + SV.line(40, 20, 40, 220, "", { style: "stroke:var(--muted);stroke-width:2" }) + SV.line(40, 220, 610, 220, "", { style: "stroke:var(--muted);stroke-width:2" });
    [0, 10, 20, 30, 40].forEach((t) => (s += sm(30, y(t) + 4, t, "end")));
    s += sm(325, 238, "time") + SV.text(14, 120, "°C", "sm", {});
    s += SV.path("M" + b.ts.map((t, i) => `${x(i)} ${y(t)}`).join(" L"), "", { style: "fill:none;stroke:var(--muted);stroke-width:2;stroke-dasharray:5 4" });
    s += SV.path("M" + a.ts.map((t, i) => `${x(i)} ${y(t)}`).join(" L"), "", { style: "fill:none;stroke:var(--accent);stroke-width:3" });
    svg.innerHTML = s;
    $("#ga").textContent = Math.round((a.inr / 100) * 100) + " %"; $("#gb").textContent = a.hs; $("#gc").textContent = a.wo;
    $("#gv").innerHTML = `Automated (solid line): in range <b>${Math.round(a.inr)}%</b> of the time. With no automation (dashed): <b>${Math.round(b.inr)}%</b>. The sensor-microprocessor-actuator loop keeps the temperature between ${L} and ${H} °C by switching the heater and the window.`;
  }
  lo = Lib.slider($("#g1"), { id: "gl", label: "Low limit", min: 10, max: 25, value: 20, fmt: (v) => v + " °C", onInput: upd });
  hi = Lib.slider($("#g2"), { id: "gh", label: "High limit", min: 18, max: 35, value: 26, fmt: (v) => v + " °C", onInput: upd });
  out = Lib.slider($("#g3"), { id: "go", label: "Outside temperature", min: 0, max: 40, value: 8, fmt: (v) => v + " °C", onInput: upd });
  upd();
})();

/* ---------- Lab 2 ---------- */
const PAIRS = ["Light sensor → lamp", "Moisture sensor → pump", "Temperature sensor → heater", "Pressure sensor → alarm siren", "Infra-red sensor → door motor", "Gas sensor → ventilation fan", "Proximity sensor → brakes"];
chooser($("#sn"), $("#sv"), PAIRS, [
  ["Street lights that switch on at dusk", "Light sensor → lamp"], ["Watering a field only when the soil is dry", "Moisture sensor → pump"], ["Keeping a greenhouse warm on cold nights", "Temperature sensor → heater"], ["A burglar alarm triggered by someone stepping on a mat", "Pressure sensor → alarm siren"],
  ["A supermarket door that opens when someone approaches", "Infra-red sensor → door motor"], ["A kitchen that clears a dangerous gas leak", "Gas sensor → ventilation fan"], ["A driverless car stopping before an obstacle", "Proximity sensor → brakes"],
]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is each point an advantage or a disadvantage of an automated system?", buckets: [{ label: "Advantage" }, { label: "Disadvantage" }], items: [
  { text: "Works 24 hours a day without breaks", b: 0 },
  { text: "More accurate and consistent than people", b: 0 },
  { text: "Can work in dangerous places", b: 0 },
  { text: "Fast response to changes", b: 0 },
  { text: "High cost to install and program", b: 1 },
  { text: "Jobs may be lost", b: 1 },
  { text: "A fault or power cut can stop it", b: 1 },
  { text: "Cannot cope with unexpected situations", b: 1 },
  { text: "Can be hacked", b: 1 },
], done: "Speed and accuracy against cost, jobs and faults." });

Lib.classify($("#cl2"), { prompt: "Which area is each automated system from?", buckets: [{ label: "Industry" }, { label: "Transport" }, { label: "Agriculture" }, { label: "Weather" }, { label: "Lighting" }], items: [
  { text: "Production line that assembles cars", b: 0 },
  { text: "Robot checking products for faults", b: 0 },
  { text: "Driverless train", b: 1 },
  { text: "Automatic traffic lights", b: 1 },
  { text: "Moisture sensors switching on pumps", b: 2 },
  { text: "Automated milking machines", b: 2 },
  { text: "Weather station measuring rainfall", b: 3 },
  { text: "Storm warning sensors", b: 3 },
  { text: "Street lights that react to daylight", b: 4 },
  { text: "Motion-activated lights", b: 4 },
], done: "Match the system to its area." });

Lib.order($("#o1"), { prompt: "Put the steps of an automated control loop in order.", items: [
  "The sensor measures a physical quantity",
  "An ADC converts the analogue reading to digital",
  "The microprocessor compares it with the stored value",
  "The microprocessor sends a signal to the actuator",
  "The actuator acts, and the sensor measures again"
], done: "Measure, convert, compare, signal, act, repeat." });

Lib.match($("#m1"), { prompt: "Match each part to its job.", pairs: [
  ["Sensor", "Measures a physical quantity"],
  ["ADC", "Converts analogue readings to digital data"],
  ["Microprocessor", "Compares readings with a stored value and decides"],
  ["Actuator", "Turns a signal into physical action"],
  ["Feedback", "The action changes the next reading, and the loop repeats"],
  ["Stored value", "The limit or target the reading is compared with"]
] });

Lib.calc($("#c1"), { qs: [
  { q: "The street light switches ON when the reading is below 30. The readings are 55, 42, 28, 31, 19. How many readings switch the light ON?", a: 2, sol: "28 and 19 are below 30: 2 readings." },
  { q: "A greenhouse heater turns ON below 18 °C. Readings: 20, 17, 18, 15, 22. How many readings turn the heater ON?", a: 2, sol: "17 and 15 are below 18: 2 (18 is not below 18).", hint: "Is 18 below 18?" },
  { q: "An automated factory makes 12 items an hour for 24 hours. How many items does it make?", a: 288, sol: "12 × 24 = 288." },
  { q: "A worker makes 5 items an hour for an 8-hour shift. How many items?", a: 40, sol: "5 × 8 = 40." },
  { q: "A sensor reading of 7 is converted to 4-bit binary by an ADC. Give the binary number.", t: ["0111"], ph: "4 bits", sol: "7 = 4 + 2 + 1 = 0111." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "What does an actuator do?", opts: ["Measures", "Turns a signal into action", "Stores data", "Compares values"], a: 1, why: "Actuators move or switch something." },
  { q: "What does the microprocessor compare a sensor reading with?", opts: ["A stored value", "A random number", "The previous user", "Nothing"], a: 0, why: "It compares with a stored (target or limit) value." },
  { q: "Why is an ADC needed?", opts: ["Sensors give analogue data", "Actuators are digital", "To save power", "To make noise"], a: 0, why: "The microprocessor needs digital data." },
  { q: "Which is an advantage of automation?", opts: ["High cost", "Can work 24 hours a day", "Needs maintenance", "Jobs lost"], a: 1, why: "Automated systems do not need breaks." },
  { q: "What is feedback?", opts: ["The action changes the next reading", "A user complaint", "An error message", "A power cut"], a: 0, why: "The loop repeats using the new reading." },
  { q: "Which sensor suits automatic watering?", opts: ["Moisture", "Sound", "Pressure plate", "Magnetic"], a: 0, why: "A moisture sensor reads soil dampness." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Automated system", "A system that carries out a task with little or no human involvement, using sensors, a microprocessor and actuators."],
  ["Sensor", "An input device that measures a physical quantity."],
  ["Microprocessor", "Compares sensor readings with stored values and decides what to do."],
  ["Actuator", "An output device that turns a signal into physical action."],
  ["ADC", "Analogue-to-digital converter: converts sensor readings for the microprocessor."],
  ["DAC", "Digital-to-analogue converter: converts a digital signal for an analogue actuator."],
  ["Feedback", "The effect of an action changes the next reading, so the loop repeats."],
  ["Stored value", "The target or limit that readings are compared with."]
] });
