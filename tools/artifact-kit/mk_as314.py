"""AS CS 3.1.4: monitoring and control systems, sensors, actuators, feedback. Run: python3 tools/artifact-kit/mk_as314.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>monitoring system</b> uses <b>sensors</b> to collect data and records, displays or reports it, but takes no action that changes what the sensors measure. A <b>control system</b> uses sensors and a microprocessor to decide what to do and sends a signal to an <b>actuator</b> that changes the environment, so the sensor's next reading is affected: that loop is <b>feedback</b>. Sensors produce analogue signals, which an <b>ADC</b> converts to digital for the processor; a <b>DAC</b> converts the processor's output for actuators that need an analogue signal. Exam questions always ask you to <b>identify</b> the system (no mark) and <b>justify</b> it (the marks), so learn the justification phrases. Typical sensors: temperature, light, pressure, infra-red, moisture, humidity, sound, gas, pH, magnetic field and motion.</p></div>

  <h2>1 · Sensors and actuators</h2>
  <div class="tw"><table class="t">
    <tr><th>Sensor</th><th>Measures</th><th>Example use</th></tr>
    <tr><td>Temperature</td><td>Heat</td><td>Central heating, 3D printer, fridge</td></tr>
    <tr><td>Light</td><td>Brightness (daylight level)</td><td>Floodlight that comes on at dusk</td></tr>
    <tr><td>Pressure</td><td>Force on an area</td><td>Door open/closed, burglar alarm mat</td></tr>
    <tr><td>Infra-red / proximity</td><td>Presence or distance of a person or object</td><td>Counting chocolate bars on a conveyor; automatic doors; car braking</td></tr>
    <tr><td>Moisture / humidity</td><td>Water in soil or air</td><td>Greenhouse watering</td></tr>
    <tr><td>Sound, gas, pH, magnetic field, motion</td><td>As named</td><td>Burglar alarm, gas leak, pond monitoring, door sensor, doorbell</td></tr>
  </table></div>
  <p>An <b>actuator</b> converts an electrical signal from the processor into a physical action, for example a motor, valve, heater or the arm that pushes an incorrectly weighted chocolate bar off the production line. In the exam: an actuator <b>generates a signal or causes an action</b>, <b>converting electrical energy into a mechanical force</b>.</p>

  <h2>2 · Monitoring system</h2>
  <ul>
    <li>Collects, stores, displays or transmits the sensor data.</li>
    <li>The output (a light, an alarm, a display) <b>does not affect the input</b> to the sensors.</li>
    <li><b>No actuator</b> and <b>no feedback</b>: the warnings are just warnings.</li>
    <li>Examples: a security system that sounds an alarm, a heart-rate monitor sending to a phone, a weather station.</li>
  </ul>

  <h2>3 · Control system</h2>
  <ul>
    <li>The processor <b>acts independently</b> (autonomously) on sensor data.</li>
    <li>It sends a signal to an <b>actuator</b>, which <b>changes the environment</b>, so the next sensor input is different: <b>feedback</b>.</li>
    <li>Feedback keeps the system <b>operating within set limits</b>, because its output affects its next input and conditions are adjusted automatically.</li>
    <li>Examples: a fridge that switches the cooling on above 6 °C and off below 4 °C; automatic doors that open when a person is within 2 m and close when nobody is; a car that brakes harder as an object gets closer.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Question to ask</th><th>Monitoring</th><th>Control</th></tr>
    <tr><td>Is there an actuator?</td><td>No</td><td>Yes</td></tr>
    <tr><td>Does the output change the next input?</td><td>No</td><td>Yes: feedback</td></tr>
    <tr><td>Does the system act on its own?</td><td>It only records or warns</td><td>Yes, it acts autonomously</td></tr>
  </table></div>

  <h2>4 · Analogue to digital</h2>
  <p>Sensors give analogue readings; the microprocessor needs digital. An <b>ADC</b> converts them, and a <b>DAC</b> converts digital output to analogue for actuators such as a motor or speaker.</p>

  <h2>5 · Combining sensors with logic</h2>
  <p>Sensors often feed logic. For a security system with E = system switched on, A = daylight level low, C = person within 2 m, B and D = front and back doors open: floodlight <b>X = E AND A AND C</b>; audio alarm <b>Y = E AND (B OR C OR D)</b>. This links to the logic gates page.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Writing "it is a control system because it controls the lights". You must refer to feedback and the effect on the input.</li>
    <li>Saying a monitoring system "just monitors". Say that the output does not affect the sensor input and there is no actuator.</li>
    <li>Calling a warning light an actuator in a monitoring system.</li>
    <li>Forgetting that a sensor measures a physical quantity and the processor, not the sensor, makes the decision.</li>
  </ul>
'''

watch = '''
  <h2>1 · A control loop: the fridge</h2>
  <div id="stA"></div>
  <h2>2 · A monitoring system has no loop</h2>
  <div id="stB"></div>
  <h2>3 · From sensor to actuator</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Fridge control</h2>
  <p>The microprocessor turns the cooling on above the upper limit and off below the lower limit. Change the limits and see the temperature.</p>
  <div class="card"><div id="fS1"></div><div id="fS2"></div><div id="fG"></div><div id="fV" class="verdict"></div></div>
  <h2>Lab 2 · Monitoring or control?</h2>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>
  <h2>Lab 3 · Pick the sensor</h2>
  <div class="card"><div id="nB" class="btnrow"></div><div id="nO"></div></div>
'''

_pr, _prjs = PR(["Monitoring or control?", "Sensor or actuator?", "Match the sensor to its use", "Put the control loop steps in order", "Working out", "Multiple choice"],
  ("Monitoring system or control system?", ["Monitoring", "Control"], [("Records heart rate and sends it to a phone", 0), ("Switches a heater on when it is too cold", 1), ("The output does not affect the sensor input", 0), ("Uses feedback", 1), ("Has no actuator", 0), ("Opens a door when a person is detected", 1)], "Control: actuator and feedback."),
  ("Sensor or actuator?", ["Sensor", "Actuator"], [("Infra-red detector", 0), ("Motor that opens a door", 1), ("Pressure pad", 0), ("Heater", 1), ("Light-dependent resistor", 0), ("Valve that waters a greenhouse", 1)], "Sensors input; actuators act."),
  [["Temperature sensor", "Heating, fridge or 3D printer"], ["Light sensor", "Floodlight at dusk"], ["Pressure sensor", "Detecting an open door"], ["Infra-red sensor", "Counting items on a conveyor"], ["Moisture sensor", "Watering plants"]],
  ("Put the control loop in order.", ["The sensor measures the temperature", "The ADC converts the reading to digital", "The microprocessor compares it with the limits", "The microprocessor signals the actuator", "The actuator changes the temperature, which the sensor then measures"], "Sense, convert, compare, signal, act, repeat."),
  [{"q": "A fridge stays between 4 and 6 °C. How wide is the allowed range in °C?", "a": 2, "unit": "°C", "tol": 0.01, "hint": "6 − 4.", "sol": "<b>2</b> °C."}, {"q": "A sensor reading is 0 to 5 V and an ADC has 8 bits. How many different values can it give?", "a": 256, "unit": "", "tol": 0.01, "hint": "2^8.", "sol": "<b>256</b>."}, {"q": "A temperature is read every 2 seconds. How many readings in one minute?", "a": 30, "unit": "", "tol": 0.01, "hint": "60 ÷ 2.", "sol": "<b>30</b>."}, {"q": "An infra-red sensor counts 3 bars each second for 90 seconds. How many bars?", "a": 270, "unit": "", "tol": 0.01, "hint": "3 × 90.", "sol": "<b>270</b>."}, {"q": "X = E AND A AND C. For E=1, A=1, C=0, what is X?", "a": 0, "unit": "", "tol": 0.01, "hint": "AND needs all 1.", "sol": "<b>0</b>."}],
  [("A control system must have:", ["An actuator and feedback", "Only a display", "A printer", "No sensor"], 0, "Actuator and feedback."), ("A monitoring system:", ["Output does not affect the input", "Always has an actuator", "Uses feedback", "Controls a motor"], 0, "No effect on the input."), ("An actuator:", ["Causes a physical action", "Measures light", "Stores data", "Converts digital to text"], 0, "Causes an action."), ("An ADC:", ["Analogue to digital", "Digital to analogue", "Adds data", "Draws"], 0, "Analogue to digital."), ("Which sensor counts items on a conveyor belt?", ["Infra-red", "pH", "Sound", "Humidity"], 0, "Infra-red."), ("Feedback means:", ["Output affects the next input", "Data is stored", "Power is saved", "A message is sent"], 0, "Output affects input.")],
  [("Sensor", "Measures a physical quantity."), ("Actuator", "Causes a physical action."), ("Monitoring", "No actuator, no feedback."), ("Control", "Actuator and feedback."), ("Feedback", "Output affects the next input."), ("ADC", "Analogue to digital."), ("DAC", "Digital to analogue."), ("Autonomous", "Acts without a person deciding.")])

real = RWNOTE + (
rw("A home thermostat", "It switches the boiler on when the room is too cold and off when it is warm enough. The heating changes the temperature the sensor reads: feedback.", "a control system.") +
rw("A smartwatch", "It measures your heart rate and shows it on your phone, but nothing it does changes your heart rate.", "a monitoring system.") +
rw("A supermarket automatic door", "An infra-red sensor detects you and a motor opens the door; when you have gone through the door closes.", "actuator and feedback.") +
rw("Cruise control or automatic braking", "A car measures distance and brakes harder as an object gets closer; braking changes the distance, which is then measured again.", "feedback loop.") +
rw("A burglar alarm", "It sounds a siren when the sensors are triggered but does not change the sensors' input.", "monitoring with warnings only.")
)

where = [
  ("M/J 2021", "11, 13", "5(c)", "2", "Why the refrigerator system is a control and not a monitoring system"),
  ("M/J 2024", "11", "2(a), (b)", "2 + 2", "Embedded characteristics of a video doorbell; monitoring or control with justification"),
  ("O/N 2023", "12", "1(a), (b)", "1 + 2", "A sensor to count items; the role of an actuator"),
  ("O/N 2023", "11", "9(a)", "2", "The importance of feedback in a control system"),
  ("O/N 2024", "11", "5", "1 + 2 + 3", "Sensors for a security system; logic expressions; monitoring or control"),
  ("O/N 2024", "13", "3", "3", "Why an automatic braking system is a control system"),
  ("O/N 2025", "12", "11", "3", "Whether an automatic door system is monitoring or control"),
  ("M/J 2026", "12", "6(a), (b), (c)", "3 + 2 + 2", "A health monitor: embedded, monitoring or control, RAM against ROM")]

past = '''  <p class="note">The identification of monitoring or control earns no mark in these questions; the marks are for the justification. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "11/13", "Q5(c)"), "2 marks", "Explain",
  "The temperature in Kiara's refrigerator must be kept between 4 and 6 degrees Celsius. The microprocessor turns on the cooling if the temperature is too high, and turns off the cooling if the temperature is too low. Explain why the system in the refrigerator is a control and not a monitoring system.", "Feedback; action changes the temperature.",
  "<p>" + mks(["The system uses feedback", "The system causes the temperature to change, or produces an action"]) + "</p>", None) + peq(SRC("s24", "11", "Q2(b)"), "2 marks", "State / Justify",
  "A video doorbell uses a motion sensor to start a digital camera and send a message to a smartphone. State whether the video doorbell is a monitoring system or a control system. Justify your choice.", "No mark for the choice; justify with output not affecting input, or processing causing a signal.",
  "<p>No mark for the choice. " + mks(["Monitoring: turning on the camera does not affect the input to the sensor or button", "Monitoring: the transmission of the video does not affect the input to the sensor", "Control: the data is processed, generating a signal to start the camera recording", "Control: motion detected causes a signal to be sent over a network to the smartphone"]) + " (any two)</p>", "Just writing 'it is a monitoring system because it monitors'. The justification must link the output to the input.") + peq(SRC("w23", "12", "Q1(a)(b)"), "1 + 2 marks", "Identify / Describe",
  "An automated system counts the number of chocolate bars made at the end of production using a sensor above the conveyor belt. (a) Identify one appropriate type of sensor. A second automated system removes chocolate bars with an incorrect weight. (b) Describe the role of an actuator in this system.", "Infra-red. Actuator generates a signal and pushes the bar off.",
  "<p><b>(a)</b> " + mks(["infra-red or proximity sensor"]) + "</p><p><b>(b)</b> " + mks(["The actuator generates a signal, causes an action, or converts electrical energy into a mechanical force", "to push an arm, open a trap door or pick up the chocolate bar with the incorrect weight"]) + "</p>", None) + peq(SRC("w23", "11", "Q9(a)"), "2 marks", "Explain",
  "Explain the importance of feedback in a control system.", "Operates within limits; output affects input; adjusts automatically.",
  "<p>Any two: " + mks(["Feedback ensures that a system operates within set criteria or constraints", "by enabling system output to affect (subsequent) system input", "thus allowing conditions to be automatically adjusted"]) + "</p>", None) + peq(SRC("w24", "11", "Q5(a)(b)(c)"), "1 + 2 + 3 marks", "Complete / Write / Explain",
  "A security system has a floodlight (X) and an audio alarm (Y). Sensors detect if doors are open, the external daylight level and whether people are within a set distance. (a) Identify the most appropriate sensor for: a door is open; daylight below a set amount; a person detected within 2 metres. (b) Parameters: A = low daylight, B = front door open, C = person within 2 m, D = back door open, E = system on. The floodlight turns on if the system is on, and daylight is low, and a person is detected within 2 m. The alarm turns on if the system is on and one or more doors are open or a person is detected within 2 m. Write logic expressions for X and Y. (c) Explain whether the security system is a monitoring or a control system.", "Pressure or infra-red; light; infra-red. X = E AND A AND C. Y = E AND (B OR C OR D). Monitoring: no feedback, no actuator.",
  "<p><b>(a)</b> " + mks(["Door open: pressure or infra-red; daylight: light sensor; person: infra-red (all three for the mark)"]) + "</p><p><b>(b)</b> " + mks(["X = E AND A AND C", "Y = E AND (B OR C OR D)"]) + "</p><p><b>(c)</b> No mark for identification. Monitoring: " + mks(["There is no feedback; the light and alarm are just warnings", "The output of the floodlight or alarm does not affect the input of data from the sensors", "The system does not have any actuators"]) + "</p>", "Calling the system a control system because the floodlight 'controls' the light. A floodlight is a warning output, not a feedback loop.") + peq(SRC("w24", "13", "Q3"), "3 marks", "Explain",
  "A car has an automatic braking system. A sensor measures the distance to objects in front. The car brakes automatically if an object is too close or the distance is decreasing too quickly. The closer the object, the harder the car brakes. Explain the reasons why the automatic braking system is a control system.", "Feedback, acts independently, braking changes the distance.",
  "<p>Any three: " + mks(["The system uses feedback", "The system acts independently", "Input data causes the car to brake", "braking decreases or changes the distance to the object", "this new distance is used to determine whether or how hard the car needs to brake"]) + "</p>", None) + peq(SRC("w25", "12", "Q11"), "3 marks", "Identify / Justify",
  "An automated system opens doors when a person is detected within 2 metres and closes them when there is no longer a person within 2 metres. Identify whether it is a monitoring system or a control system. Justify your choice.", "Control: actuator, output changes input, autonomous feedback.",
  "<p>Control (no mark). " + mks(["The system uses an actuator to open or close the doors", "The output (opening the doors) allows people to move, which changes the input to the sensor", "The system acts autonomously on the feedback from a sensor"]) + "</p>", None) + peq(SRC("s26", "12", "Q6(a)(b)(c)"), "3 + 2 + 2 marks", "Explain / Tick / Describe",
  "A health monitor attaches to a person's arm and measures key health information, such as heart rate, and transmits it to a smartphone, which analyses it and displays the results. (a) Explain the reasons why it is an embedded system. (b) Tick monitoring or control and justify. (c) The monitor contains RAM and ROM. Describe two differences between RAM and ROM.", "(a) One function, dedicated hardware, firmware. (b) Monitoring: only records, no feedback, no actuator. (c) Read/write against read only; volatile against non-volatile; running data against boot-up.",
  "<p><b>(a)</b> Any three: " + mks(["It only has one function, to monitor health", "All the hardware such as sensors and a microprocessor is dedicated to this task", "The firmware cannot be easily amended or updated because its function is preset"]) + "</p><p><b>(b)</b> No mark for the choice. Monitoring, any two: " + mks(["The system only records or transmits the data", "It does not use feedback or change the environment", "The output does not affect the next input", "It does not contain an actuator"], "a") + "</p><p><b>(c)</b> Any two (must refer to both): " + mks(["RAM can be read from and written to; ROM can only be read", "RAM is volatile; ROM is non-volatile", "RAM stores currently running data and instructions; ROM stores boot-up instructions or firmware"], "b") + "</p>", "Writing about only RAM or only ROM. A difference needs both sides.")

review = req("2 marks", "Justify", "A greenhouse system measures the humidity and switches on a sprinkler when it is too dry. State, with a justification, whether it is a monitoring or control system.", "Actuator and feedback.", "<p>Control. " + mks(["It uses an actuator (the sprinkler)", "which changes the humidity that the sensor then measures (feedback)"]) + "</p>", None) + req("2 marks", "Justify", "A weather station measures temperature and rainfall and stores the readings. State, with a justification, whether it is monitoring or control.", "Output does not change input.", "<p>Monitoring. " + mks(["It only records the readings", "It has no actuator and no feedback, so nothing it does changes what the sensors measure"]) + "</p>", None) + req("1 mark", "Identify", "Identify a sensor for each: (i) detecting a person approaching a door; (ii) detecting that it is getting dark.", "Infra-red; light.", "<p>" + mks(["Infra-red and light sensors (both for the mark)"]) + "</p>", None) + req("2 marks", "Write", "A gate opens (G = 1) when the system is on (S) and a car is detected (C) or a button is pressed (B). Write a logic expression for G.", "AND with OR in brackets.", "<p>" + mks(["G = S AND (C OR B)"]) + " (2 marks: structure and brackets)</p>", None) + req("2 marks", "Explain", "Explain why a sensor reading must pass through an ADC before the microprocessor can use it.", "Analogue to digital.", "<p>" + mks(["Sensors produce analogue signals", "the microprocessor can only process digital data, so an ADC converts them"]) + "</p>", None)

tips = tips_html([
  ("No mark for the choice.", "The justification earns the marks."),
  ("Control: actuator, feedback.", "The output changes the next input."),
  ("Monitoring: no actuator, no feedback.", "Warnings do not change the input."),
  ("Name the sensor properly.", "Infra-red, light, pressure, temperature."),
  ("Actuator: converts electrical energy to a physical action.", "Give the action in the scenario."),
  ("Link to the scenario.", "Name the fridge, the door, the car."),
], [("a sensor", "A device that measures a physical quantity."), ("an actuator", "A device that causes a physical action."), ("feedback", "System output affecting the next input."), ("an ADC", "A converter from analogue to digital.")],
  [("Identify", "Name the point."), ("Justify", "Reasons in the scenario."), ("Explain", "Reasons as well."), ("Write", "Give the expression.")]) + FC

js = AKJS + AK20JS + r'''
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
''' + _prjs

finish("as-3-1-4-monitoring-control-sensors-feedback", "as314", "Monitoring and Control Systems",
  "Sensors, actuators and feedback, how to tell a monitoring system from a control system, with a control-loop animation, a fridge lab and the real Paper 1 questions from 2021 to 2026.",
  "3.1.4", "3 · Hardware", "section 3.1 Computers and their components", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on monitoring and control systems (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
