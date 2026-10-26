"""AS CS 3.1.2: hardware device operations. Run: python3 tools/artifact-kit/mk_as312.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>The syllabus asks for the <b>principal operation</b> of a set of devices: laser printer, 3D printer, microphone, speakers, magnetic hard disk, solid state (flash) drive, optical disc reader/writer, touchscreens (resistive and capacitive) and a virtual reality headset. For each you need an ordered account of what physically happens, using the key terms. Mark schemes award one mark per correct stage, so learn each device as a short chain of steps. Several devices also use sensors, buffers or microprocessors, which links back to earlier pages. Papers 1 and 2 most often ask about the hard disk, flash memory, touchscreens, the 3D printer, the microphone and the VR headset.</p></div>

  <h2>1 · Magnetic hard disk</h2>
  <ul>
    <li>One or more <b>platters</b> (disks) coated with a magnetisable (ferrous oxide) material, mounted on a central <b>spindle</b>, inside a sealed box.</li>
    <li>The platters <b>rotate at high speed</b>. Each surface has a <b>read/write head</b> on an <b>arm</b> just above the surface; electronic circuits control the arm movement.</li>
    <li>The surface is divided into concentric <b>tracks</b> and <b>sectors</b>.</li>
    <li><b>Writing:</b> the head produces a magnetic field that sets the magnetic pattern (north/south) of tiny areas, representing 1s and 0s. <b>Reading:</b> the head detects the pattern of the magnetised areas.</li>
  </ul>

  <h2>2 · Solid state (flash) drive</h2>
  <ul>
    <li>No moving parts: data is stored in cells built from <b>transistors</b> arranged as <b>NAND</b> or <b>NOR</b> gates, using <b>1 or 2 transistors per cell</b>.</li>
    <li>Each cell has a <b>floating gate</b> that can <b>retain electrons without power</b> (this stores the bit) and a <b>control gate</b> that allows or stops current from passing.</li>
    <li>Writing changes the charge on the floating gate; reading checks whether the cell conducts. Data is erased in blocks.</li>
    <li>Compared with magnetic: faster access, silent, more robust, lower power; but more expensive per GB and cells wear out after many write cycles.</li>
  </ul>

  <h2>3 · Optical disc (CD, DVD, Blu-ray)</h2>
  <ul>
    <li>Data is stored on a spiral track as <b>pits and lands</b> on the surface. A <b>laser</b> shines on the surface while the disc spins.</li>
    <li><b>Reading:</b> light reflects differently from a pit and a land, and a sensor reads the changes as 1s and 0s. <b>Writing</b> (recordable discs): a higher-power laser burns marks into a dye layer (or changes a phase-change layer); rewritable discs can be erased by a different laser setting.</li>
  </ul>

  <h2>4 · Touchscreens</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Resistive</th><th>Capacitive</th></tr>
    <tr><td>Layers</td><td>Two layers (flexible top layer and rigid bottom layer) separated by a small gap</td><td>Several layers; the top one is glass with a transparent conductor</td></tr>
    <tr><td>Operation</td><td>Pressing makes the layers touch and <b>completes a circuit</b>; a microprocessor finds the coordinates</td><td>Touching with a conductive object (a finger) causes a <b>change in the electric current</b> or electrostatic field at that point; a microprocessor finds the coordinates</td></tr>
    <tr><td>Works with</td><td>Any object that presses</td><td>Only conductive objects (not a plain stylus or ordinary gloves)</td></tr>
  </table></div>

  <h2>5 · Microphone and speakers</h2>
  <p><b>Microphone (dynamic):</b> sound waves cause a <b>diaphragm</b> to vibrate; this moves a <b>coil past a magnet</b> (or a magnet past a coil), which produces an <b>electrical signal</b> that is then sampled. In a condenser microphone the vibration changes the <b>capacitance</b>; in a crystal microphone it deforms a crystal.</p>
  <p><b>Speaker:</b> an electrical signal (converted from digital data by a DAC) passes through a <b>coil</b> attached to a <b>cone</b> near a <b>permanent magnet</b>. The changing current makes the coil and cone vibrate, which creates sound waves.</p>

  <h2>6 · Laser printer</h2>
  <ol>
    <li>The page data arrives and is held in a <b>buffer</b>; a raster image of the page is built.</li>
    <li>A laser draws the image onto a <b>rotating, electrically charged drum</b>, leaving charge in the pattern of the page.</li>
    <li><b>Toner</b> (powder) sticks to the charged areas of the drum.</li>
    <li>Paper is fed through, with a charge that pulls the toner from the drum onto the paper.</li>
    <li>A <b>fuser</b> (heated rollers) melts the toner into the paper, which is then ejected.</li>
  </ol>

  <h2>7 · 3D printer</h2>
  <ul>
    <li>It uses <b>additive manufacturing</b>: a digital 3D model (a <b>CAD</b> file) is built up <b>one layer at a time</b> from the bottom, using x, y and z coordinates; the material is fused or cured layer by layer.</li>
    <li><b>FDM:</b> material is heated and pushed through a nozzle. <b>SLA:</b> a UV laser cures liquid resin. <b>DLP:</b> a projector/lamp cures resin. <b>SLS:</b> a laser fuses powdered material.</li>
    <li>A <b>temperature sensor</b> stops overheating and ensures the material is hot enough. The printer has a <b>buffer</b> (often DRAM) for print data.</li>
  </ul>

  <h2>8 · Virtual reality headset</h2>
  <ul>
    <li>One or two <b>(LCD) displays/lenses</b> output the image; <b>speakers</b> give surround sound.</li>
    <li>A <b>gyroscope/accelerometer</b> detects head movement; a microprocessor works out the <b>direction and speed</b> of movement and updates the image.</li>
    <li>Some headsets use <b>digital cameras</b> to record eye movements, and a buffer to hold data from the computer.</li>
  </ul>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Writing "the head reads the disk" without saying that the surface is divided into magnetised areas or that the platters spin.</li>
    <li>Describing flash memory as having a "moving part" or saying that it uses magnetism.</li>
    <li>Mixing up resistive (circuit completed) and capacitive (change in current).</li>
    <li>Not saying "layer by layer" for a 3D printer.</li>
  </ul>
'''

watch = '''
  <h2>1 · Reading and writing on a hard disk</h2>
  <div id="stA"></div>
  <h2>2 · Resistive and capacitive touchscreens</h2>
  <div id="stB"></div>
  <h2>3 · A 3D printer builds layer by layer</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Build a 3D object</h2>
  <p>Change the layer height and the object height to see how many layers (and how much time) are needed.</p>
  <div class="card"><div id="lS1"></div><div id="lS2"></div><div id="lV" class="verdict"></div></div>
  <h2>Lab 2 · Which device?</h2>
  <div class="card"><div id="dB" class="btnrow"></div><div id="dO"></div></div>
  <h2>Lab 3 · Resistive or capacitive?</h2>
  <div class="card"><div id="tB" class="btnrow"></div><div id="tO"></div></div>
'''

_pr, _prjs = PR(["Magnetic or solid state?", "Resistive or capacitive?", "Match the device to its key part", "Put the laser printer steps in order", "Working out", "Multiple choice"],
  ("Magnetic hard disk or solid state drive?", ["Magnetic hard disk", "Solid state drive"], [("Platters on a spindle", 0), ("Floating gate and control gate", 1), ("Read/write head on an arm", 0), ("NAND or NOR gates", 1), ("Data stored as magnetised areas", 0), ("No moving parts", 1)], "Magnetic: moving parts. Solid state: transistors."),
  ("Resistive or capacitive touchscreen?", ["Resistive", "Capacitive"], [("Two layers touch to complete a circuit", 0), ("Change in electric current when touched", 1), ("Works with any pressing object", 0), ("Needs a conductive object such as a finger", 1), ("Pressure presses top layer to the bottom layer", 0), ("Several layers, top is glass", 1)], "Resistive presses together; capacitive senses the finger."),
  [["Diaphragm", "Microphone vibrates with sound waves"], ["Fuser", "Laser printer melts toner onto paper"], ["Gyroscope", "VR headset detects head movement"], ["Floating gate", "Flash memory holds electrons without power"], ["Nozzle", "FDM 3D printer pushes heated material out"]],
  ("Put the laser printer stages in order.", ["Page data is received and built into an image", "A laser draws the image onto the charged drum", "Toner sticks to the charged areas of the drum", "Toner transfers from the drum to the paper", "A fuser melts the toner into the paper"], "Image, laser, toner on drum, to paper, fuse."),
  [{"q": "A 3D object is 60 mm high and printed in layers of 0.2 mm. How many layers?", "a": 300, "unit": "", "tol": 0.01, "hint": "60 ÷ 0.2.", "sol": "<b>300</b>."}, {"q": "Each layer takes 40 seconds. How many minutes to print the 300 layers?", "a": 200, "unit": "min", "tol": 0.5, "hint": "300 × 40 = 12000 s ÷ 60.", "sol": "<b>200</b> min."}, {"q": "A disk spins at 7200 revolutions per minute. How many revolutions per second?", "a": 120, "unit": "", "tol": 0.01, "hint": "7200 ÷ 60.", "sol": "<b>120</b>."}, {"q": "A flash cell stores 1 bit. How many cells are needed to store 1 byte?", "a": 8, "unit": "", "tol": 0.01, "hint": "8 bits.", "sol": "<b>8</b>."}, {"q": "A sound is sampled 44100 times a second with 2 bytes per sample. How many bytes per second (one channel)?", "a": 88200, "unit": "bytes", "tol": 0.5, "hint": "44100 × 2.", "sol": "<b>88200</b>."}],
  [("Which device uses a diaphragm?", ["Microphone", "Laser printer", "Hard disk", "SSD"], 0, "Microphone."), ("Which part of flash memory retains electrons without power?", ["Floating gate", "Control gate", "Platter", "Spindle"], 0, "Floating gate."), ("A 3D printer builds an object:", ["Layer by layer", "By cutting from a block", "By melting everything at once", "By photographing it"], 0, "Additive manufacturing."), ("A capacitive touchscreen detects:", ["A change in electric current", "A completed circuit between layers", "Sound", "Heat only"], 0, "Change in current."), ("A VR headset detects head movement with:", ["Gyroscope or accelerometer", "A laser drum", "A platter", "A fuser"], 0, "Gyroscope."), ("On a hard disk the surface is divided into:", ["Tracks and sectors", "Pits and lands", "Cells and gates", "Layers"], 0, "Tracks and sectors.")],
  [("Hard disk", "Platters, spindle, head on arm, magnetised areas."), ("SSD", "NAND/NOR, floating gate, control gate."), ("Optical disc", "Laser reads pits and lands."), ("Resistive screen", "Layers touch, circuit completed."), ("Capacitive screen", "Change in electric current."), ("Microphone", "Diaphragm, coil and magnet, electrical signal."), ("Laser printer", "Charged drum, toner, fuser."), ("3D printer", "Additive; layer by layer from a CAD model.")])

real = RWNOTE + (
rw("A phone screen", "Your finger changes the electric field at one spot on a capacitive screen; a gloved hand or plain plastic stylus often does not work.", "capacitive needs a conductive touch.") +
rw("A supermarket checkout screen", "Staff can use gloves or a pen because many are resistive: pressing makes two layers touch.", "resistive works with any object.") +
rw("A laptop upgrade", "Swapping a hard disk for an SSD makes start-up faster because there is no head to move and no disk to spin up.", "no moving parts.") +
rw("A 3D-printed part", "Engineers print prototypes and replacement parts from a CAD file layer by layer, wasting less material than cutting from a block.", "additive manufacturing.") +
rw("Gaming with a VR headset", "Turning your head changes the view straight away because the sensors report the direction and speed of your head movement to the microprocessor.", "gyroscope and accelerometer.")
)

where = [
  ("M/J 2021", "12", "3(a)", "3", "Describe the principal operation of a microphone"),
  ("M/J 2022", "11", "2(b)", "5", "Describe the principal operations of a magnetic hard disk"),
  ("M/J 2022", "12", "2(c)", "1", "True or false statements about a resistive touchscreen"),
  ("M/J 2023", "13", "3(a)", "5", "Complete a description of resistive and capacitive touchscreens"),
  ("O/N 2023", "11", "7(a), (b)", "3 + 2", "The principal operations of a 3D printer; the purpose of its temperature sensor"),
  ("M/J 2024", "11", "2(c)(ii)", "4", "Principal operation of solid state (flash) memory"),
  ("O/N 2024", "12", "2(a)", "4", "Complete a description of a virtual reality headset"),
  ("O/N 2024", "12", "2(c)", "3", "Benefits of EEPROM in the headset")]

past = '''  <p class="note">The principal-operation questions are reworded from the papers; check the original paper and mark scheme for the exact wording. The laser printer, speakers and optical disc are on the syllabus but no question on them was found in the 2021 to 2026 Paper 1 and 2 papers I checked, so learn them from the Learn tab rather than from past questions.</p>
''' + peq(SRC("s21", "12", "Q3(a)"), "3 marks", "Describe",
  "Describe the principal operation of a microphone.", "Diaphragm, vibration, coil and magnet, electrical signal.",
  "<p>Any three: " + mks(["The microphone has a diaphragm (or ribbon)", "The incoming sound waves cause vibrations of the diaphragm", "causing a coil to move past a magnet (or a magnet past a coil), or changing the capacitance (condenser), or deforming a crystal (crystal microphone)", "An electrical signal is produced"]) + "</p>", None) + peq(SRC("s22", "11", "Q2(b)"), "5 marks", "Describe",
  "A magnetic hard disk is used to store data on the computer. Describe the principal operations of a magnetic hard disk.", "Platters, magnetised surface, spindle, rotation, head on arm, tracks and sectors, magnetic pattern.",
  "<p>Any five: " + mks(["The hard disk has one or more platters", "Each surface is capable of being magnetised (ferrous oxide)", "The platters are mounted on a central spindle", "The mechanism is in a sealed box", "The disks are rotated at high speed", "Each surface has a read/write head mounted on an arm just above the surface", "Electronic circuits control the movement of the arm and heads", "The surface is divided into concentric tracks and sectors", "Writing creates a magnetic pattern; reading detects the pattern"]) + "</p>", "Describing a hard disk as 'a disk that stores data'. Each mark needs a named part and what it does.") + peq(SRC("s22", "12", "Q2(c)"), "1 mark", "Tick",
  "The car has a resistive touchscreen. Tick one box in each row to show whether the statement is true or false. The screen always has five different layers. A processor determines the horizontal and vertical coordinates of the point of contact. The touchscreen will work if any object touches the screen.", "A resistive screen has two layers; any object presses.",
  "<p>" + mks(["Five layers: false", "A processor determines the coordinates: true", "Works with any object: true"]) + " (all three correct for the mark)</p>", None) + peq(SRC("s23", "13", "Q3(a)"), "5 marks", "Complete",
  "Complete the description of the principal operation of touchscreens. A ... touchscreen has two layers. When the user touches the screen, the layers touch and a ... is completed. A ... touchscreen has several layers. When the top layer is touched, there is a ... in the electric current. A microprocessor identifies the ... of the touch.", "Resistive, circuit, capacitive, change, coordinates.",
  "<p>" + mks(["resistive", "circuit", "capacitive", "change (increase or decrease)", "coordinates"]) + "</p>", None) + peq(SRC("w23", "11", "Q7(a)(b)"), "3 + 2 marks", "Describe",
  "(a) Describe the principal operations of a 3D printer. (b) Describe the purpose of a temperature sensor within the 3D printer.", "Additive, CAD, layers, specific type. Temperature: overheating, hot enough.",
  "<p><b>(a)</b> Any three: " + mks(["Additive manufacturing", "Uses a digital 3D model or a CAD file", "Builds up the model one layer at a time", "starting from the bottom, using x, y and z coordinates", "The material is fused or cured together layer by layer", "FDM: material is heated and pushed through a nozzle", "SLA: photosensitive liquid resin exposed to a UV laser", "SLS: a laser forms objects from powdered material"]) + "</p><p><b>(b)</b> Any two: " + mks(["To prevent overheating, or ensure the material is hot enough", "by identifying the temperature of the object being printed", "by identifying the temperature of the material being used"], "a") + "</p>", None) + peq(SRC("s24", "11", "Q2(c)(ii)"), "4 marks", "Complete",
  "The video doorbell has a solid state (flash) secondary storage device. Complete the table about the principal operation of solid state memory: the two types of logic gate that can be used; the number of transistors in each cell; the type of gate that can retain electrons without power; the type of gate that allows or stops current from passing.", "NAND and NOR; 1 or 2; floating; control.",
  "<p>" + mks(["NAND and NOR (both for the mark)", "1 or 2 transistors", "floating (gate)", "control (gate)"]) + "</p>", None) + peq(SRC("s24", "12", "Q2(a)"), "4 marks", "Complete",
  "A headset can have one or two ... that output the image to the user. The headset has speakers that output surround sound. The user's head movements are detected using a sensor. This sensor is a ... . The data is transmitted to a microprocessor that analyses the data to identify the ... of movement. Some headsets use ... that record the user's eye movements for analysis.", "Displays, gyroscope or accelerometer, direction or speed, digital cameras.",
  "<p>" + mks(["(LCD) displays, screens or lenses", "gyroscope or accelerometer", "direction or speed", "digital cameras"]) + "</p>", None) + peq(SRC("s24", "12", "Q2(c)"), "3 marks", "Explain",
  "The VR headset has EEPROM. Explain the benefits of using EEPROM instead of other types of ROM in the headset.", "Rewritable many times, in situ, no technical expertise, cheaper.",
  "<p>Any three: " + mks(["EEPROM allows frequent read/write/erase operations", "so the headset can take advantage of new features", "without fully erasing the contents of the firmware first (a particular byte can be erased)", "without removing the chip from the headset", "The contents of the firmware can be changed by the user without technical expertise", "Cheaper to manufacture, so the headset is cheaper to purchase"]) + "</p>", None)

review = req("5 marks", "Describe", "Describe how a laser printer prints a page.", "Drum, laser, toner, paper, fuser.", "<p>" + mks(["The page data is held in a buffer and the image is built", "A laser draws the image onto the charged rotating drum", "Toner sticks to the charged areas of the drum", "The toner is transferred to the paper", "A fuser (heated rollers) melts the toner into the paper"]) + "</p>", None) + req("3 marks", "Describe", "Describe how a speaker produces sound from a digital sound file.", "DAC, coil, magnet, cone.", "<p>" + mks(["The digital data is converted to an electrical (analogue) signal", "The signal passes through a coil attached to a cone, near a magnet", "The coil and cone vibrate, creating sound waves"]) + "</p>", None) + req("3 marks", "Describe", "Describe how data is read from an optical disc.", "Laser, pits and lands.", "<p>" + mks(["A laser shines on the spinning disc's surface", "Light reflects differently from pits and lands", "A sensor detects the differences as 1s and 0s"]) + "</p>", None) + req("2 marks", "Explain", "Explain one advantage of a solid state drive over a magnetic hard disk in a laptop.", "No moving parts.", "<p>" + mks(["It has no moving parts", "so it is faster, silent, more robust and uses less power"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between how a resistive and a capacitive touchscreen detect a touch.", "Circuit against current.", "<p>" + mks(["Resistive: pressing makes two layers touch and completes a circuit", "Capacitive: a conductive touch causes a change in the electric current"]) + "</p>", None)

tips = tips_html([
  ("One mark per stage.", "Write each device as a chain of steps."),
  ("Hard disk: platters, spindle, head, arm.", "Say rotating and magnetised areas."),
  ("Flash: floating gate, control gate.", "NAND and NOR, 1 or 2 transistors."),
  ("Resistive: circuit. Capacitive: change in current.", "Do not swap them."),
  ("3D printer: additive, layers, CAD.", "Name x, y and z if you can."),
  ("VR: gyroscope, direction and speed.", "Cameras for eye tracking."),
], [("a read/write head", "Reads and writes the magnetic pattern on a platter."), ("a floating gate", "Holds electrons in flash memory without power."), ("additive manufacturing", "Building an object up layer by layer."), ("a diaphragm", "The part of a microphone that vibrates with sound.")],
  [("Describe", "Several points in order."), ("Complete", "Fill in the missing words."), ("Explain", "Reasons as well."), ("Tick", "True or false.")]) + FC

js = AKJS + AK20JS + r'''
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
''' + _prjs

finish("as-3-1-2-hardware-device-operations", "as312", "Hardware Device Operations",
  "How a magnetic hard disk, solid state drive, optical disc, touchscreen, microphone, speaker, laser printer, 3D printer and VR headset work, with animations, a 3D printing lab and the real Paper 1 questions from 2021 to 2026.",
  "3.1.2", "3 · Hardware", "section 3.1 Computers and their components", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on how devices work (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
