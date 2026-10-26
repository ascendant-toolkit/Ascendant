"""AS CS syllabus 3.1.1: input, output, primary and secondary storage, embedded systems, buffers. Run: python3 tools/artifact-kit/mk_as311.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>Every computer needs <b>input</b> devices to get data in, <b>output</b> devices to give results out, <b>primary memory</b> (RAM and ROM) that the processor can reach directly, and <b>secondary storage</b> for permanent, large-capacity storage, including <b>removable</b> storage that can be taken away. Primary memory is fast but limited and (RAM) loses its contents when the power goes off; secondary storage is slower, larger and keeps data without power. An <b>embedded system</b> is a microprocessor or microcontroller built into a larger device to do one dedicated task, such as a washing machine controller; it has benefits (cheap, reliable, small) and drawbacks (hard to update or repair). A <b>buffer</b> is a temporary store that holds data between two devices working at different speeds, so the faster one is not held up waiting for the slower.</p></div>

  <h2>1 · Input, output and storage</h2>
  <div class="tw"><table class="t">
    <tr><th>Part</th><th>Purpose</th><th>Examples</th></tr>
    <tr><td><b>Input device</b></td><td>Gets data from the user or environment into the computer</td><td>Keyboard, mouse, microphone, touchscreen, sensors, camera</td></tr>
    <tr><td><b>Output device</b></td><td>Presents the results of processing</td><td>Screen, printer, speakers, actuators</td></tr>
    <tr><td><b>Primary memory</b></td><td>Directly accessible to the processor; holds the instructions and data in use. <b>RAM</b> holds the running programs, data and part of the OS (volatile); <b>ROM</b> holds the start-up (boot) instructions or BIOS (non-volatile)</td><td>RAM, ROM, cache</td></tr>
    <tr><td><b>Secondary storage</b></td><td>Permanent, non-volatile storage of programs and data, not directly accessed by the processor: data must be loaded into RAM first. Larger and cheaper per byte, but slower</td><td>Magnetic hard disk, solid state drive</td></tr>
    <tr><td><b>Removable storage</b></td><td>Secondary storage that can be taken out and moved between computers: for backups and transfer</td><td>USB flash drive, optical disc, external hard disk, memory card</td></tr>
  </table></div>
  <p>Primary memory is needed because the processor can only work on data that it can reach quickly. Secondary storage is needed because RAM is volatile and too small to keep everything. Magnetic storage is cheaper per unit, long-lived under heavy read/write use and suits very large files such as continuous CCTV recordings; solid state storage has no moving parts, is faster and quieter and uses less power.</p>

  <h2>2 · Embedded systems</h2>
  <p>An <b>embedded system</b> is a microprocessor or microcontroller <b>within a larger system</b> that performs <b>one specific task</b>, for example the controller in a washing machine that runs the wash programs and does nothing else. Typical characteristics:</p>
  <ul>
    <li><b>Dedicated</b> to a single task, with a limited number of functions.</li>
    <li><b>Built into</b> a larger system (the washing machine, car lane-detection system, video doorbell).</li>
    <li>Needs only a <b>small amount of processing power</b>, and has no general-purpose operating system.</li>
    <li>Contains a <b>processor, memory and input/output</b> capability, with <b>firmware</b> in ROM that the owner cannot easily change.</li>
  </ul>
  <p>In a washing machine <b>ROM</b> stores the start-up instructions (the program for the wash cycles) and <b>RAM</b> stores the choices the user has entered, the readings from the sensors and the time left in the programme.</p>
  <div class="tw"><table class="t">
    <tr><th>Benefits</th><th>Drawbacks</th></tr>
    <tr><td>Cheap to make and run; small; low power; reliable because it does one task</td><td>Difficult for the user to change or update the firmware; errors cannot be fixed easily and repair is a specialist task; functionality cannot be extended or adapted; faulty or outdated devices are often thrown away, leading to e-waste</td></tr>
  </table></div>

  <h2>3 · Buffers</h2>
  <p>A <b>buffer</b> is a <b>temporary store</b> of data held <b>until the device is ready to receive it</b>. It is needed where two components work at <b>different speeds</b>. For example, a computer sends a document to a printer much faster than the printer can print it:</p>
  <ol>
    <li>The computer sends the print data to the buffer <b>at computer speed</b>.</li>
    <li>The data is passed from the buffer to the printer <b>at printer speed</b>.</li>
    <li>The processor is <b>free to carry on</b> with other tasks instead of waiting for the slower printer.</li>
    <li>When the buffer is empty the printer sends an <b>interrupt</b> to ask for more data; when it is full the computer is told to stop sending.</li>
  </ol>
  <p>Buffers are used with printers, 3D printers, hard disk drives, VR headsets, speakers (sound data stored until the player takes it) and in streaming video.</p>

  <h2>4 · Common ways to lose marks</h2>
  <ul>
    <li>Defining an embedded system as "a small computer". It is a dedicated microprocessor built into a larger system to do one task.</li>
    <li>Writing that RAM "stores the operating system" for ROM, or mixing them up. ROM holds boot-up instructions; RAM holds what is running now.</li>
    <li>Describing a buffer as storage "to make it faster". It stores data until the device can process it, to cope with a difference in speed.</li>
    <li>Saying secondary storage is "slower RAM". It is non-volatile storage that the processor cannot access directly.</li>
    <li>Writing one drawback of embedded systems without the reason, such as "they break". Say the firmware cannot be easily changed or repaired.</li>
  </ul>
'''

watch = '''
  <h2>1 · From input to storage</h2>
  <div id="stA"></div>
  <h2>2 · A buffer between a fast computer and a slow printer</h2>
  <p>Press Play.</p>
  <div id="stB"></div>
  <h2>3 · Inside an embedded system</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · The buffer</h2>
  <p>The computer sends data into the buffer at one speed; the printer takes it out more slowly. Change the speeds and the buffer size.</p>
  <div class="card"><div id="bS1"></div><div id="bS2"></div><div id="bS3"></div><div id="bG"></div><div class="verdict" id="bV"></div></div>
  <h2>Lab 2 · Primary or secondary?</h2>
  <div class="card"><div id="pB" class="btnrow"></div><div id="pO"></div></div>
  <h2>Lab 3 · Embedded or general-purpose?</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

_pr, _prjs = PR(["Primary or secondary?", "Benefit or drawback of embedded systems?", "Match the term to its meaning", "Put the buffer steps in order", "Working out", "Multiple choice"],
  ("Is it primary memory or secondary storage?", ["Primary memory", "Secondary storage"], [("RAM", 0), ("Magnetic hard disk", 1), ("Directly accessed by the processor", 0), ("Keeps data when the power is off, in large amounts", 1), ("Holds the start-up instructions in ROM", 0), ("USB flash drive", 1)], "Primary: reached directly. Secondary: permanent, loaded into RAM first."),
  ("Is it a benefit or a drawback of embedded systems?", ["Benefit", "Drawback"], [("Cheap and small", 0), ("Firmware is hard for the user to update", 1), ("Reliable because it does one task", 0), ("Faulty devices are often thrown away", 1), ("Needs little processing power", 0), ("Cannot easily be adapted for another task", 1)], "Dedicated: cheap and reliable, but fixed."),
  [["Embedded system", "A dedicated microprocessor inside a larger device"], ["Buffer", "A temporary store between devices of different speeds"], ["Primary memory", "Memory the processor can access directly"], ["Secondary storage", "Permanent non-volatile storage"], ["Removable storage", "Storage that can be moved between computers"]],
  ("Put the printing steps with a buffer in order.", ["The computer sends the data to the buffer at its own speed", "The processor carries on with other tasks", "The buffer passes data to the printer at the printer's speed", "The buffer becomes empty", "The printer sends an interrupt asking for more data"], "Send, carry on, pass on, empty, interrupt."),
  [{"q": "A computer sends 120 pages' data to the buffer in 6 seconds and the printer prints 4 pages per second. How many seconds does printing take?", "a": 30, "unit": "s", "tol": 0.1, "hint": "120 ÷ 4.", "sol": "<b>30</b> s."}, {"q": "In the same case, how many seconds is the computer free to do other tasks while the printer works (after the 6 s)?", "a": 24, "unit": "s", "tol": 0.1, "hint": "30 − 6.", "sol": "<b>24</b> s."}, {"q": "A video file of 4 GB is stored on a 500 GB drive. How many such files fit (whole files)?", "a": 125, "unit": "", "tol": 0.01, "hint": "500 ÷ 4.", "sol": "<b>125</b>."}, {"q": "A washing machine controller stores 12 programs of 2 KiB each in ROM. How many KiB is that?", "a": 24, "unit": "KiB", "tol": 0.01, "hint": "12 × 2.", "sol": "<b>24</b> KiB."}, {"q": "How many examples of removable storage were listed in the Learn tab (USB drive, optical disc, external hard disk, memory card)?", "a": 4, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>4</b>."}],
  [("Which keeps data when the power is off?", ["RAM", "Secondary storage", "Cache only", "Registers"], 1, "Secondary storage."), ("An embedded system:", ["Does one dedicated task inside a larger device", "Is a general-purpose PC", "Has no processor", "Is a type of cable"], 0, "Dedicated task."), ("A buffer is used when:", ["Devices work at different speeds", "A device is switched off", "Data is deleted", "A file is compressed"], 0, "Different speeds."), ("In a washing machine, ROM stores:", ["The start-up instructions", "The time left", "The user's choices", "Nothing"], 0, "Start-up instructions."), ("Removable storage is:", ["Taken out and moved between computers", "Always inside the CPU", "The same as RAM", "Only wireless"], 0, "Can be moved."), ("An embedded-system drawback is:", ["Firmware hard to update", "Too many functions", "Too much processing", "Too large"], 0, "Hard to update.")],
  [("Input / output", "Data in / results out."), ("Primary memory", "RAM and ROM; direct access."), ("Secondary storage", "Permanent; larger; slower."), ("Removable storage", "USB drive, optical disc."), ("Embedded system", "Dedicated microprocessor in a larger device."), ("Embedded drawbacks", "Hard to update, repair, adapt; e-waste."), ("Buffer", "Temporary store until the device is ready."), ("Buffer interrupt", "Empty: ask for more. Full: stop sending.")])

real = RWNOTE + (
rw("Printing a long document", "Your computer sends the whole document to the printer's buffer in seconds, then you carry on while it prints page by page.", "a buffer frees the processor.") +
rw("A microwave or a washing machine", "A small chip runs the programs for one job. You cannot install new software on it, which is why it counts as an embedded system.", "dedicated task, firmware you cannot change.") +
rw("Why your computer slows when RAM is full", "RAM is fast but limited. If it fills, data has to be fetched from secondary storage, which is slower.", "primary memory is fast; secondary storage is slower.") +
rw("A USB stick", "You save a file on it and take it to another computer. It is removable secondary storage.", "removable storage.") +
rw("Smart doorbells and car systems", "A small dedicated computer inside the product does one job, such as detecting motion or keeping the car in its lane.", "embedded systems are built into larger systems.")
)

where = [
  ("M/J 2021", "11, 13", "5(a), (b)", "2 + 2", "What an embedded system is; the purpose of RAM and ROM in a washing machine"),
  ("M/J 2022", "11", "2(a)(i)", "5", "Complete a description of primary memory, RAM, ROM, SRAM and DRAM"),
  ("M/J 2022", "12", "2(a), (b)", "2 + 2", "Why a lane-detection system is an embedded system; data in primary and secondary storage"),
  ("M/J 2023", "11", "4(a)(i), (b)", "2 + 4", "The contents of ROM; two reasons magnetic storage suits a CCTV computer more than solid state"),
  ("O/N 2023", "12", "1(c)", "2 + 1", "Features of embedded systems; a drawback"),
  ("O/N 2023", "11", "9(b)", "3", "An example of an embedded system with an explanation"),
  ("O/N 2024", "12", "2(a)", "3", "Drawbacks of embedded systems"),
  ("O/N 2024", "13", "2(b)", "4", "How a memory buffer is used when transferring data to a hard disk"),
  ("O/N 2025", "11", "10(b)", "1", "Why a 3D printer needs a buffer"),
  ("M/J 2026", "13", "8(c)", "3", "The purpose of a buffer when sound data is sent to speakers")]

past = '''  <p class="note">Embedded systems, primary and secondary storage and buffers are tested in Paper 1 most series; the buffer question has appeared with a different device each time (printer, hard disk, 3D printer, VR headset, speakers). Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "11/13", "Q5(a)(b)"), "2 + 2 marks", "Describe / State",
  "Kiara has an embedded system in her washing machine. (a) Describe what is meant by an embedded system, using the washing machine as an example. (b) The washing machine's embedded system makes use of both Random Access Memory (RAM) and Read Only Memory (ROM). State the purpose of RAM and ROM within the washing machine's embedded system.",
  "(a) Definition and example. (b) RAM: current data; ROM: start-up instructions.",
  "<p><b>(a)</b> " + mks(["A microprocessor or microcontroller within a larger system, which performs one specific task"]) + " " + mks(["Example: the embedded system in the washing machine only controls the programs for the washing cycle; it is part of the machine but does not perform any other function"], "a") + "</p><p><b>(b)</b> " + mks(["RAM: stores the choices (wash programme) the user has entered, or the data read from the sensors, or the time left in the programme"]) + " " + mks(["ROM: stores the start-up instructions (for the washing cycles)"], "a") + "</p>", "Describing an embedded system as 'a computer in a washing machine' with no mention of it being dedicated to one task.") + peq(SRC("s22", "11", "Q2(a)(i)"), "5 marks", "Complete",
  "Complete the description of computer memory. Random Access Memory (RAM) and Read Only Memory (ROM) are both examples of ... memory. One item that is stored in RAM is ... . One item that is stored in ROM is ... . RAM can be either Static RAM (SRAM) or Dynamic RAM (DRAM). SRAM uses transistors arranged as ... . DRAM uses transistors and ... .",
  "Primary, current software or data, start-up instructions, flip-flops, capacitors.",
  "<p>" + mks(["primary", "the currently running software, data or part of the OS", "the start-up (boot-up) instructions or BIOS", "flip-flops (or latches)", "capacitors"]) + "</p>", None) + peq(SRC("s22", "12", "Q2(a)(b)"), "2 + 2 marks", "Explain / Identify",
  "A car has a lane detection system that monitors the lines on either side of the lane and automatically moves the car away from a line if it gets too close. (a) Explain why the lane detection system is an example of an embedded system. (b) Two other features record the number of miles in the current journey (from engine on to engine off) and the total number of miles the car has travelled since it was built. Identify the data that will be stored in the primary and secondary storage of the car for these two features.",
  "(a) Built in, one task, not easily changed. (b) Current journey in primary; total in secondary.",
  "<p><b>(a)</b> Any two: " + mks(["The lane detection system is built into or integrated into the car", "It only performs one task", "It is not easily changed or updated by the car owner"]) + "</p><p><b>(b)</b> " + mks(["Primary: the miles travelled in the current journey, before the engine is turned off"]) + " " + mks(["Secondary: the total miles travelled since the car was built (or the miles for the most recent journey after the engine is switched off)"], "a") + "</p>", "Putting the total mileage in primary memory. It must survive the power being switched off, so it goes in secondary storage.") + peq(SRC("s23", "11", "Q4(a)(i)(b)"), "2 + 4 marks", "Describe",
  "A CCTV system's central computer has both ROM and RAM and stores video files on secondary storage. (a)(i) Describe the contents of the ROM in the central computer. (b) Describe two reasons why magnetic storage is more appropriate than solid state storage for this computer.",
  "(a) bootstrap or start-up instructions, firmware, part of the OS. (b) reason plus application.",
  "<p><b>(a)(i)</b> Any two: " + mks(["The bootstrap program (start-up instructions) for the central computer, or the BIOS", "The start-up instructions or firmware for the CCTV system and cameras", "The kernel or parts of the operating system"]) + "</p><p><b>(b)</b> Two reasons, each with an application: " + mks(["The computer will have a large number of read/write operations because it is working all the time", "and magnetic storage has more longevity"]) + " " + mks(["Magnetic storage costs less per storage unit", "and videos are large files, so a very large storage capacity is required"], "a") + "</p>", None) + peq(SRC("w23", "12", "Q1(c)"), "2 + 1 marks", "Identify",
  "The factory has many different machines with embedded systems. (i) Identify two features of embedded systems. (ii) Identify one drawback of embedded systems.",
  "Dedicated, built in, contains processor, memory, I/O; hard to update.",
  "<p><b>(i)</b> Any two: " + mks(["Dedicated to a single task (a limited number of functions)", "Built into or integrated into a larger system", "Must contain a processor, memory and an input/output capability (dedicated hardware)"]) + "</p><p><b>(ii)</b> One: " + mks(["It is difficult for the user to change or update the firmware, or to upgrade devices", "It cannot be easily adapted for another task", "Troubleshooting faults or upgrading is a specialist task", "Devices are often thrown away rather than repaired"], "a") + "</p>", None) + peq(SRC("w24", "12", "Q2(a)"), "3 marks", "Describe",
  "Embedded systems are used in many electronic devices. Describe the drawbacks of embedded systems.",
  "Hard to update, errors, adaptation, e-waste.",
  "<p>Any three: " + mks(["It is difficult to change or update the firmware by the user", "Errors cannot be fixed easily; troubleshooting and repair is a specialist, expensive task", "Functionality cannot be changed or extended easily, or adapted for another task", "Faulty or outdated devices are often thrown away rather than repaired", "leading to e-waste"]) + "</p>", None) + peq(SRC("w24", "13", "Q2(b)"), "4 marks", "Explain",
  "Explain how a memory buffer is used when a computer is transferring data to its magnetic hard disk drive.",
  "Different speeds; temporary store; computer not held up; data passed on at the slower rate.",
  "<p>Any four: " + mks(["The computer and the hard disk drive transmit and receive at different speeds: the computer transfers data faster than the drive can receive it", "The buffer is used for temporary storage", "so that the computer can transfer data to the buffer at the higher speed", "and is not held up waiting for the data to transfer", "and so that data is transferred to the hard disk drive from the buffer at the slower rate"]) + "</p>", None) + peq(SRC("w25", "11", "Q10(b)"), "1 mark", "State",
  "State why a 3D printer needs a buffer.",
  "Speed mismatch with the processor, so the processor is free.",
  "<p>One: " + mks(["To free up the processor to carry out other tasks, because the rate at which data is received by the printer is different from the rate at which it can be processed", "To manage the mismatch in speed between the processor and the peripheral (the 3D printer)"]) + "</p>", None) + peq(SRC("s26", "13", "Q8(c)"), "3 marks", "Describe",
  "The computer outputs the sound through external speakers. The computer transfers the data to a buffer before the speakers output the sound. Describe the purpose of the buffer.",
  "Temporary storage until the device is ready; speed difference; processor free.",
  "<p>Any three: " + mks(["Temporary storage of data", "until the device is ready to receive it, or until a sound player takes the data", "Data may be sent faster than it can be received: it allows for different speeds of transmission between devices", "Allows the processor to carry out other tasks"]) + "</p>", None)

review = req("2 marks", "State", "State one item of data held in primary memory and one held in secondary storage in a digital camera.", "In use now, or saved.", "<p>" + mks(["Primary: the settings or the image currently being processed", "Secondary: the saved photographs"]) + "</p>", None) + req("3 marks", "Explain", "Explain why an embedded system in a smart thermostat does not need a general-purpose operating system.", "One dedicated task.", "<p>" + mks(["It performs only one dedicated task", "its needs are limited, so a small program in ROM (firmware) is enough", "A full OS would add cost and complexity it does not need"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a USB drive is called removable secondary storage.", "Where is it used?", "<p>" + mks(["It keeps data permanently, without power", "and can be taken out and used in another computer"]) + "</p>", None) + req("3 marks", "Describe", "Describe how a buffer is used when a laptop sends a print job.", "Two speeds.", "<p>" + mks(["The laptop sends the print data to the buffer at its own speed", "The printer takes data from the buffer at its slower speed", "so the laptop can carry on with other tasks instead of waiting"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between RAM and secondary storage.", "Direct access, volatility.", "<p>" + mks(["RAM is primary memory the processor accesses directly; it is volatile and holds data and programs in use", "Secondary storage is non-volatile, larger and slower; data must be loaded into RAM first"]) + "</p>", None)

tips = tips_html([
  ("Embedded: dedicated, built in.", "A microprocessor performing one task inside a larger system."),
  ("RAM now, ROM start-up.", "RAM holds what is running; ROM holds the boot instructions."),
  ("Primary: direct. Secondary: permanent.", "Secondary data must be loaded into RAM first."),
  ("Buffer: temporary store.", "Different speeds; the faster device is not held up."),
  ("Interrupt when the buffer is empty.", "The device asks for more data."),
  ("Embedded drawbacks.", "Firmware hard to change; repair is specialist; e-waste."),
], [("an embedded system", "A dedicated microprocessor within a larger system."), ("primary memory", "Memory the processor can access directly (RAM and ROM)."), ("secondary storage", "Permanent non-volatile storage."), ("a buffer", "A temporary store between devices of different speeds.")],
  [("State / Identify", "Short answer."), ("Describe", "Several points."), ("Explain", "Reasons as well."), ("Complete", "Fill in the missing words.")]) + FC

js = AKJS + AK20JS + r'''
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
''' + _prjs

finish("as-3-1-1-memory-storage-embedded-buffers", "as311", "Input, Output, Storage, Embedded Systems and Buffers",
  "Input and output devices, primary memory and secondary and removable storage, embedded systems with their benefits and drawbacks, and how buffers cope with devices of different speeds; animations, a buffer lab and the real Paper 1 questions from 2021 to 2026.",
  "3.1.1", "3 · Hardware", "section 3.1 Computers and their components", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on memory, storage, embedded systems and buffers (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
