const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)";
const note = (x, y, t, cls = "", anchor = "middle") => SV.text(x, y, t, "lbl bd " + cls, { "text-anchor": anchor });
const sm = (x, y, t, anchor = "middle") => SV.text(x, y, t, "sm", { "text-anchor": anchor });
const panel = (x, y, w, h, title, col, o = 1) => SV.rect(x, y, w, h, "", { rx: 12, style: `fill:var(--surface);stroke:${col};stroke-width:3`, opacity: o }) + (title ? SV.text(x + w / 2, y + 22, title, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) : "");
const rg = (x, y, w, h, name, val, hi, col = ACC) => SV.rect(x, y, w, h, "", { rx: 8, style: `fill:${hi ? "var(--soft)" : "var(--surface)"};stroke:${hi ? col : MUT};stroke-width:${hi ? 4 : 2}` }) + sm(x + w / 2, y + 17, name) + SV.text(x + w / 2, y + h - 12, val, "lbl bd", { "text-anchor": "middle", style: `fill:${hi ? col : "var(--ink)"}` });
const arr = (x1, y1, x2, y2, col, dash) => SV.line(x1, y1, x2, y2, "", { style: `stroke:${col};stroke-width:4;${dash ? "stroke-dasharray:7 6" : ""}` }) + SV.arrowHead(x2, y2, x2 >= x1 ? "r" : "l", "").replace('class=""', `style="fill:${col}"`);
const chip = (x, y, w, t, col) => SV.rect(x, y, w, 26, "", { rx: 13, style: `fill:${col}` }) + SV.text(x + w / 2, y + 18, t, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:12px" });

/* ---------- 2. sensor, processor, actuator ---------- */
function sensChart(s) {
  const k = Math.round(s.k), t = k >= 5 ? 24 : 31;
  const hi = (a, b) => (k >= a && k <= b ? ACC : MUT);
  let o = panel(15, 85, 150, 100, "Sensor", hi(1, 1)) + sm(90, 130, "temperature") + sm(90, 150, k >= 1 ? "reads " + t + " °C" : "");
  o += panel(205, 85, 150, 100, "ADC", hi(2, 2)) + sm(205 + 75, 130, k >= 2 ? "analogue →" : "analogue to digital") + sm(280, 150, k >= 2 ? "00011111" : "");
  o += panel(395, 85, 150, 100, "Processor", hi(3, 3)) + sm(470, 130, "target 25 °C") + sm(470, 150, k === 3 ? "31 > 25: too hot" : k >= 5 ? "24 < 25: fine" : "");
  o += panel(585, 85, 160, 100, "Actuator", k >= 4 && k <= 4 ? GOOD : MUT) + sm(665, 130, "motor on window") + sm(665, 150, k === 4 ? "OPENING" : k >= 5 ? "stopped" : "closed");
  o += k >= 1 ? arr(165, 135, 205, 135, ACC) : "";
  o += k >= 2 ? arr(355, 135, 395, 135, ACC) : "";
  o += k >= 4 ? arr(545, 135, 585, 135, GOOD) : "";
  o += note(380, 35, "Greenhouse: " + t + " °C", k >= 5 ? "t3" : "t2") + sm(380, 60, "Target: 25 °C");
  o += chip(250, 225, 260, k === 0 ? "Too warm for the plants" : k <= 3 ? "Data is being processed" : k === 4 ? "Window opens, heat escapes" : "Temperature back to normal", k >= 5 ? GOOD : ACC);
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 270, label: "Sensor, processor and actuator in a greenhouse", base: { k: 0 }, tween: 1, dwell: 4000, draw: sensChart, steps: [
  { cap: "A greenhouse should stay at <b>25 °C</b> but it is <b>31 °C</b>. A computer system controls it.", s: { k: 0 } },
  { cap: "The <b>temperature sensor</b> measures the real-world temperature. It captures <b>analogue</b> data.", s: { k: 1 } },
  { cap: "An <b>analogue-to-digital converter (ADC)</b> turns the reading into digital data (here 31 in binary).", s: { k: 2 } },
  { cap: "The <b>processor</b> compares the reading with the stored target: 31 is above 25.", s: { k: 3 } },
  { cap: "It sends a signal to the <b>actuator</b>, a motor, which opens a window. Sensors measure; actuators act.", s: { k: 4 } },
  { cap: "The temperature falls to 24 °C. The processor stops the motor. The loop keeps running.", s: { k: 5 } },
] });

/* ---------- Lab 2: choose the sensor ---------- */
(() => {
  const SENS = ["Acoustic", "Accelerometer", "Flow", "Gas", "Humidity", "Infra-red", "Level", "Light", "Magnetic field", "Moisture", "pH", "Pressure", "Proximity", "Temperature"];
  const ALL = [
    ["Switch the street lights on at dusk", "Light"], ["Warn of a gas leak in a kitchen", "Gas"], ["Check a swimming pool is safe to swim in", "pH"], ["Water a plant only when its soil is dry", "Moisture"],
    ["Tell a driver how close the car is to the wall when parking", "Proximity"], ["Turn a phone's screen when it is rotated", "Accelerometer"], ["Warn that a door has been opened (magnet in the frame)", "Magnetic field"],
    ["Stop a water tank overflowing", "Level"], ["Set off an alarm when glass breaks", "Acoustic"], ["Keep an oven at the right heat", "Temperature"], ["Measure how fast water moves through a pipe", "Flow"],
    ["Switch a security light on when a person walks past", "Infra-red"], ["Keep the air in a greenhouse moist enough", "Humidity"], ["Detect someone stepping on a pressure mat", "Pressure"],
  ];
  const el = $("#sn"), v = $("#sv");
  function fill() {
    const set = shuffle(ALL).slice(0, 6);
    el.innerHTML = set.map((s, i) => `<div class="r" data-a="${s[1]}"><span class="q">${s[0]}</span><select class="sel" aria-label="Sensor for: ${s[0]}"><option value="">Choose a sensor…</option>${SENS.map((x) => `<option>${x}</option>`).join("")}</select></div>`).join("") + `<div class="row"><button class="b" type="button" id="snew">New set</button></div>`;
    v.textContent = "Choose a sensor for each job.";
    $$(".r", el).forEach((r) => $("select", r).addEventListener("change", (e) => { r.classList.remove("ok", "no"); if (e.target.value) r.classList.add(e.target.value === r.dataset.a ? "ok" : "no"); const ok = $$(".r.ok", el).length; v.innerHTML = `${ok} of ${$$(".r", el).length} correct. Red means a different sensor measures that quantity.`; }));
    $("#snew").onclick = fill;
  }
  fill();
})();


/* ---------- Lab 2 ---------- */
(() => {
  const OUT = ["LCD screen", "LED screen", "Inkjet printer", "Laser printer", "3D printer", "Speaker", "Actuator", "LCD projector", "DLP projector"];
  const ALL = [
    ["Print a full-colour photograph at home", "Inkjet printer"], ["Print 500 black-and-white pages quickly in an office", "Laser printer"], ["Make a plastic model of a new product design", "3D printer"], ["Play music for a class", "Speaker"],
    ["Open a window automatically when a greenhouse gets too hot", "Actuator"], ["Show a computer image on a large screen for a room, using tiny mirrors", "DLP projector"], ["Show an image by passing light through small LCD panels onto a screen", "LCD projector"],
  ];
  const el = $("#sn2"), v = $("#sv2");
  el.innerHTML = ALL.map((s) => `<div class="r" data-a="${s[1]}"><span class="q">${s[0]}</span><select class="sel" aria-label="Output device for: ${s[0]}"><option value="">Choose a device…</option>${OUT.map((x) => `<option>${x}</option>`).join("")}</select></div>`).join("");
  v.textContent = "Choose an output device for each job.";
  $$(".r", el).forEach((r) => $("select", r).addEventListener("change", (e) => { r.classList.remove("ok", "no"); if (e.target.value) r.classList.add(e.target.value === r.dataset.a ? "ok" : "no"); v.textContent = `${$$(".r.ok", el).length} of ${$$(".r", el).length} correct.`; }));
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl2"), { prompt: "Drag each device to input or output.", buckets: [{ label: "Input device" }, { label: "Output device" }], items: [
  { text: "Keyboard", b: 0 }, { text: "Barcode scanner", b: 0 }, { text: "Microphone", b: 0 }, { text: "Touch screen (capacitive)", b: 0 }, { text: "QR code scanner", b: 0 }, { text: "3D scanner", b: 0 }, { text: "Optical mouse", b: 0 }, { text: "Temperature sensor", b: 0 },
  { text: "Inkjet printer", b: 1 }, { text: "Speaker", b: 1 }, { text: "3D printer", b: 1 }, { text: "DLP projector", b: 1 }, { text: "Laser printer", b: 1 }, { text: "Actuator", b: 1 }, { text: "LED screen", b: 1 }, { text: "LCD projector", b: 1 },
], done: "Input puts data in; output presents results (an actuator makes something move)." });

Lib.match($("#m2"), { prompt: "Match each sensor to the job it suits best.", pairs: [
  ["Light", "Switching street lamps on at dusk"], ["Proximity", "A parking aid that beeps near a wall"], ["pH", "Checking swimming pool water"], ["Moisture", "Watering a garden when the soil is dry"],
  ["Magnetic field", "A door alarm contact"], ["Accelerometer", "A phone step counter"], ["Gas", "A carbon monoxide alarm"], ["Level", "A fuel gauge in a tank"],
] });

Lib.classify($("#cl3"), { prompt: "Which type of touch screen does each statement describe?", buckets: [{ label: "Resistive" }, { label: "Capacitive" }, { label: "Infra-red" }], items: [
  { text: "Two layers pressed together by a touch", b: 0 }, { text: "Works with a stylus or a gloved finger", b: 0 },
  { text: "A finger changes the electric field", b: 1 }, { text: "Needs a conductive touch such as a finger", b: 1 }, { text: "Supports multi-touch (pinch and zoom)", b: 1 },
  { text: "A grid of beams is broken by a touch", b: 2 }, { text: "Light beams across the screen locate the position", b: 2 },
], done: "Pressure, electric field, or beams of light." });

Lib.calc($("#c1"), { qs: [
  { q: "An ADC outputs 8-bit values. How many different values can it output?", a: 256, sol: "2⁸ = 256 values (0 to 255).", hint: "Each bit has 2 values." },
  { q: "A temperature sensor reading of 25 is converted by an ADC to binary. Give the 8-bit binary number.", t: ["00011001"], ph: "8 bits", sol: "25 = 16 + 8 + 1 = 00011001." },
  { q: "A security system has 12 pressure sensors and 4 infra-red sensors. How many sensors is that in total?", a: 16, sol: "12 + 4 = 16 sensors." },
  { q: "A photo is 4000 pixels wide and 3000 pixels high. How many pixels is it? (give the number)", a: 12000000, tol: 0.5, sol: "4000 × 3000 = 12,000,000 pixels (12 megapixels)." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "Which sensor suits an automatic security light that reacts to body heat?", opts: ["Light", "Pressure", "Infra-red", "pH"], a: 2, why: "An infra-red sensor detects heat from people." },
  { q: "What does an ADC do for a sensor?", opts: ["Turns analogue data into digital data", "Makes the sensor more accurate", "Powers the actuator", "Stores data"], a: 0, why: "Sensors capture analogue data; the computer needs digital." },
  { q: "Which output device builds an object layer by layer?", opts: ["Inkjet printer", "3D printer", "DLP projector", "Speaker"], a: 1, why: "A 3D printer builds from a digital model layer by layer." },
  { q: "Which device is an input device?", opts: ["Speaker", "Actuator", "QR code scanner", "Laser printer"], a: 2, why: "A QR code scanner reads data into the computer." },
  { q: "What does an actuator do?", opts: ["Measures temperature", "Turns an electrical signal into movement", "Stores data", "Prints a page"], a: 1, why: "Actuators move things: motors, valves, locks." },
  { q: "Which sensor suits a car parking aid?", opts: ["Proximity", "Humidity", "pH", "Moisture"], a: 0, why: "Proximity sensors measure how near an object is." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Input device", "A device that enters data or instructions into a computer."],
  ["Output device", "A device that presents the results of processing in a form people can use."],
  ["Sensor", "An input device that measures a physical quantity, such as temperature or light."],
  ["Actuator", "An output device that turns an electrical signal into movement."],
  ["ADC", "Analogue-to-digital converter: changes the analogue readings from sensors into digital data."],
  ["Resistive touch screen", "Two layers pressed together by a touch; works with a finger, stylus or glove."],
  ["Capacitive touch screen", "A finger changes the electric field; supports multi-touch; needs a conductive touch."],
  ["Infra-red touch screen", "A grid of infra-red beams; a touch breaks the beams to give the position."],
  ["Inkjet printer", "Sprays droplets of ink through nozzles; good for photos, lower volume."],
  ["Laser printer", "A laser charges a drum, toner sticks to it and is fused with heat; fast, high volume."],
  ["3D printer", "Builds a solid object layer by layer from a digital model."],
  ["DLP projector", "Light is reflected off thousands of tiny mirrors to form the image."],
  ["Proximity sensor", "Measures how near an object is."],
  ["pH sensor", "Measures acidity or alkalinity."]
] });
