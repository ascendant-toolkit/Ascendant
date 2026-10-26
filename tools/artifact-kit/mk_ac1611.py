"""A Level CS syllabus 16.1.1: purposes of an operating system, resources and the user interface. Run: python3 tools/artifact-kit/mk_ac1611.py"""
from ak16 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>An <b>operating system (OS)</b> is the system software that manages the hardware and provides a platform on which application programs run. It <b>manages the resources</b> of the computer (processor time, main memory, input and output devices and storage) and shares them between the programs that want them. It <b>maximises the use of those resources</b> by multi-tasking, scheduling processes, and using virtual memory so the processor is kept busy and memory is used well. It <b>hides the complexity of the hardware</b> from the user with a user interface, device drivers and a file system, so that the user clicks an icon instead of writing code that deals with memory addresses and buses. At the centre is the <b>kernel</b>, which handles interrupts and starts and stops processes.</p></div>

  <h2>1 · What the OS manages</h2>
  <div class="tw"><table class="t">
    <tr><th>Resource</th><th>What the OS does</th></tr>
    <tr><td><b>Processor (CPU)</b></td><td>Decides which process runs next and for how long (scheduling), so the CPU is rarely idle.</td></tr>
    <tr><td><b>Main memory</b></td><td>Gives each process the memory it needs, keeps processes apart, and uses virtual memory when RAM is short.</td></tr>
    <tr><td><b>Input and output devices</b></td><td>Controls keyboards, screens and printers through device drivers; queues requests.</td></tr>
    <tr><td><b>Secondary storage and files</b></td><td>Organises files in folders, tracks where each file is stored, and controls access.</td></tr>
    <tr><td><b>Users and security</b></td><td>Logs users in, sets permissions, and stops one process changing another's data.</td></tr>
  </table></div>

  <h2>2 · Maximising the use of resources</h2>
  <ul>
    <li><b>Multi-tasking</b> means running more than one process at the same time, or appearing to. The processor is shared by giving each process a short <b>time slice</b> in turn, so many tasks make progress instead of one task having to finish before the next starts. While one process waits for a slow input or output device, the CPU runs another.</li>
    <li><b>Scheduling</b> chooses which process gets the CPU. Good scheduling keeps the CPU busy all the time, gives all processes fair access, and lets high-priority jobs finish first (16.1.3).</li>
    <li><b>Memory management</b> shares RAM between processes, and uses <b>virtual memory</b> (part of the disk) so that more programs can be open than fit in RAM at once (16.1.4).</li>
    <li>The OS also <b>monitors the state of every process</b> so that tasks do not clash over the same resource.</li>
  </ul>

  <h2>3 · Hiding the complexity of the hardware</h2>
  <p>The hardware is complicated: buses, memory addresses, controllers, disk sectors. The OS hides this by <b>abstraction</b>, so the user and the application program only see simple things.</p>
  <ul>
    <li>The <b>user interface</b> (a graphical user interface with windows, icons, menus and a pointer, or a command-line interface) lets the user control the computer in an intuitive way, by clicking an icon rather than writing code that handles memory locations and hardware. Different interfaces also give appropriate access to users with different needs.</li>
    <li><b>Device drivers</b> are small programs that translate the OS's general instructions into the commands a particular printer, disk or screen understands. Applications ask the OS to print; the driver deals with the printer.</li>
    <li>The <b>file system</b> lets the user work with named files and folders; the OS keeps track of the sectors on the disk.</li>
    <li>The <b>application layer</b> idea: the user only sees the top layer, and the lower layers' details are hidden.</li>
  </ul>

  <h2>4 · The kernel</h2>
  <p>The <b>kernel</b> is the central part of the OS, loaded first and kept in memory. It runs in a privileged (kernel) mode with full access to the hardware. It starts, stops and switches processes, manages memory, and acts as the <b>interrupt handler</b> (16.1.2): when an interrupt arrives, the kernel saves the state of the current process, runs the right routine and restores the state afterwards.</p>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Saying the OS "runs the computer" with no detail. Name a resource and what is done with it.</li>
    <li>Describing a user interface only as "easy to use". Say that it hides the complexity of the hardware, with an example such as clicking an icon instead of writing code.</li>
    <li>Describing multi-tasking as "doing two things at exactly the same time" on one processor. It <b>appears</b> to run several processes by sharing the processor.</li>
    <li>Mixing up multi-tasking (the aim) and scheduling (how the OS decides which process to run).</li>
    <li>Writing "paging" when the question asks about virtual memory: virtual memory is the idea, paging is one way to do it.</li>
  </ul>
'''

watch = '''
  <h2>1 · Layers: what happens when you press Save</h2>
  <p>Press Play. The request passes down through the layers; the user never sees the lower ones.</p>
  <div id="stA"></div>
  <h2>2 · Multi-tasking: sharing the CPU</h2>
  <div id="stB"></div>
  <h2>3 · One resource, three programs</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Is the CPU busy?</h2>
  <p>Each program uses the CPU for 2 units, then waits 3 units for the disk. Choose how many programs the OS runs together.</p>
  <div class="card"><div id="mS"></div><div id="mT"></div><div class="readout"><div><small>CPU busy</small><strong id="m1"></strong></div><div><small>CPU idle</small><strong id="m2"></strong></div></div></div>

  <h2>Lab 2 · What does the OS do for this task?</h2>
  <div class="card"><div id="oB" class="btnrow"></div><div id="oO"></div></div>

  <h2>Lab 3 · Time slices</h2>
  <p>Three processes share one CPU. Change the time slice and see how often the OS switches.</p>
  <div class="card"><div id="tS"></div><div id="tT"></div><div class="verdict" id="tV"></div></div>
'''

practise = '''
  <h2>1 · Which part of the OS?</h2><div id="cl1" class="card"></div>
  <h2>2 · Does it hide hardware complexity?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the OS term to its description</h2><div id="m1" class="card"></div>
  <h2>4 · What happens when you print a document?</h2><div id="o1" class="card"></div>
  <h2>5 · Working out</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Having many windows open", "You can listen to music, type a document and download a file at once. The OS gives each a tiny slice of the processor many times a second, so they all seem to run together.", "multi-tasking with time slices.") +
rw("Plugging in a new printer", "The computer asks for or installs a driver. After that every program can print without knowing anything about this printer's commands.", "device drivers hide the details of the hardware.") +
rw("Dragging a file to the bin", "You never type the disk sector numbers. The OS finds, moves or frees the data for you.", "a user interface hides hardware complexity.") +
rw("Phone running out of memory", "When many apps are open, the OS moves apps that are not in use out of RAM and brings them back when you return to them.", "memory management shares RAM between processes.") +
rw("Different accounts on a shared computer", "Each user sees only their own files and settings. The OS controls who may open what.", "the OS manages users and security.")
)

where = [
  ("M/J 2021", "31, 32, 33", "3(a)", "5", "Connect five OS terms (multi-tasking, paging, interrupt handling, scheduling, virtual memory) to descriptions"),
  ("O/N 2023", "31, 33", "7(a)", "2", "A benefit of a user interface and an example"),
  ("M/J 2025", "31", "8(a)", "2", "Multi-tasking and how it benefits process management"),
  ("O/N 2024", "32", "9(b)", "1 + 2", "State what multi-tasking is; describe how it is implemented"),
  ("O/N 2025", "31", "4(b)", "4", "Two ways the complexities of the hardware are hidden from the user"),
  ("O/N 2025", "33", "5", "1 + 3", "Purpose of multi-tasking; how the OS ensures it is efficient")]

past = '''  <p class="note">Operating-system questions appear in Paper 3 in most series from 2021 to 2025. Multi-tasking and the user interface are the most common. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "31/32/33", "Q3(a)"), "5 marks", "Match",
  "Draw one line to connect each Operating System (OS) term to the most appropriate description about it. Terms: multi-tasking, paging, interrupt handling, scheduling, virtual memory. Descriptions: (A) using secondary storage to simulate additional main memory; (B) managing the processes running on the CPU; (C) managing the execution of many programs that appear to run at the same time; (D) locating non-contiguous blocks of data and relocating them; (E) transferring control to another routine when a service is required; (F) reading and writing same-size blocks of data from and to secondary storage when required.",
  "One description is a distractor.",
  "<p>" + mks(["Multi-tasking → C", "Paging → F", "Interrupt handling → E", "Scheduling → B", "Virtual memory → A"]) + "</p><p>Description D is not used: it describes defragmentation, which is utility software, not one of these OS terms.</p>", "Joining paging to A. Paging is the reading and writing of fixed-size blocks (pages); virtual memory is the idea of using storage as extra memory.") + peq(SRC("w23", "31/33", "Q7(a)"), "2 marks", "State / Give",
  "A student buys a new computer. State one benefit to the student of a user interface and give an example.",
  "Benefit: it hides the complexity of the hardware. Example: clicking an icon.",
  "<p>" + mks(["Benefit (one): it hides the complexities of the computer hardware or operating system from the user; or it gives appropriate access systems for users with differing needs; or complex commands involving memory locations, buses or hardware are avoided"]) + " " + mks(["Example (one): clicking on an icon rather than writing code; or using a graphical user interface / icons for navigation"], "a") + "</p>", "Giving only 'it is easy to use' as the benefit. Say what is made easier: the user does not have to deal with the hardware.") + peq(SRC("s25", "31", "Q8(a)"), "2 marks", "Describe",
  "Describe what is meant by multi-tasking and how it benefits process management.",
  "Meaning, then the benefit.",
  "<p>" + mks(["Running multiple processes concurrently (at the same time, or appearing to)"]) + " " + mks(["which benefits process management by allowing more tasks to complete than if they had to run one task after another"], "a") + "</p>", None) + peq(SRC("w24", "32", "Q9(b)"), "1 + 2 marks", "State / Describe",
  "(i) State what is meant by the term multi-tasking in an Operating System. (ii) Describe how multi-tasking is implemented in an Operating System.",
  "(ii) sharing, scheduling, priority interrupts.",
  "<p><b>(i)</b> " + mks(["Multi-tasking allows computers to carry out, or seem to carry out, more than one process at a time"]) + "</p><p><b>(ii)</b> Any two: " + mks(["Processor time and common hardware and resources are shared between tasks", "Scheduling is used to decide which processes are carried out, so multi-tasking operates correctly without clashes", "A task of higher priority can interrupt a task that is currently running"]) + "</p>", None) + peq(SRC("w25", "31", "Q4(b)"), "4 marks", "Describe",
  "Describe two ways in which the complexities of the computer hardware are hidden from the user.",
  "Each way is a name (1) and a description (1).",
  "<p>Two ways, each with identification and description: " + mks(["A user interface (a graphical user interface)", "lets the user interact with the computer intuitively, using icons and menus to control devices by pointing and clicking"]) + " " + mks(["Device drivers", "make it easier to control peripherals such as printers within the operating system rather than on the device itself"], "a") + "</p><p>Also accepted: device mapping (devices are easy to identify, check or use on a network), or the user working only with the application layer of a protocol suite with the lower layers hidden.</p>", "Naming a way and giving no description, or describing it without naming it. Each way is worth a mark for each.") + peq(SRC("w25", "33", "Q5"), "1 + 3 marks", "State / Explain",
  "(a) State the purpose of multi-tasking. (b) Explain how an operating system ensures that multi-tasking operates efficiently.",
  "Think of monitoring, scheduling, no clashes.",
  "<p><b>(a)</b> " + mks(["To enable multiple programs or processes to be executed at the same time"]) + "</p><p><b>(b)</b> " + mks(["The OS monitors the state of each task or process", "using scheduling to ensure hardware resources are used efficiently", "and making sure that tasks or processes do not clash"]) + "</p>", None)

review = req("3 marks", "Describe", "Describe three resources managed by an operating system and one thing it does with each.", "Processor, memory, devices, files.", "<p>" + mks(["Processor: decides which process runs and for how long", "Memory: allocates memory to processes and keeps them apart", "Input and output devices (or files): controls them through drivers (or tracks where files are stored)"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a computer with only one processor can seem to run several programs at once.", "Time slices.", "<p>" + mks(["The OS gives each process a very short time slice of the processor in turn", "The switching is so fast that the user sees all the programs making progress together"]) + "</p>", None) + req("2 marks", "State", "State two ways in which a user interface hides the complexity of the hardware.", "Icons, menus, drivers.", "<p>" + mks(["Icons and menus mean the user does not type commands that deal with memory locations or devices", "Device drivers let the user print or save without knowing how the device works"]) + "</p>", None) + req("3 marks", "Explain", "A program is waiting for data to be read from a disk. Explain how multi-tasking makes better use of the processor.", "What would the CPU do otherwise?", "<p>" + mks(["Reading from the disk is slow compared with the processor", "Without multi-tasking the processor would be idle until the data arrived", "With multi-tasking the OS gives the processor to another ready process while this one waits"]) + "</p>", None) + req("2 marks", "State", "State the role of the kernel of an operating system.", "The core.", "<p>" + mks(["It is the central part of the OS, with direct access to the hardware", "It manages processes and memory and handles interrupts"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on what an operating system does, multi-tasking and the user interface (Paper 3), 2021 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Name the resource.", "Processor, memory, devices, files: say what the OS does with each."),
  ("User interface: hides hardware.", "Benefit plus an example such as clicking an icon."),
  ("Multi-tasking: appears at the same time.", "The processor is shared; more tasks complete."),
  ("Two marks: name and describe.", "A way to hide the hardware needs both."),
  ("Do not mix terms.", "Virtual memory is the idea, paging is the method, scheduling chooses the process."),
  ("Kernel.", "The core: loads first, handles interrupts, controls processes."),
], [
  ("an operating system", "System software that manages the hardware resources and provides a platform for application software."),
  ("multi-tasking", "Running more than one process at a time, or appearing to, by sharing the processor."),
  ("a device driver", "Software that lets the OS control a particular device."),
  ("the kernel", "The central component of the OS that manages processes, memory and interrupts."),
], [("State", "Give the answer only."), ("Describe", "Say what it is or how it works in several points."), ("Explain", "Give the reasons as well."), ("Match", "Join each term to one description only.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const L = [["User", "clicks Save"], ["Application", "asks the OS to save the file"], ["Operating system", "finds free space, chooses the file's place"], ["Device driver", "gives the disk its own commands"], ["Hardware", "the disk records the data"]];
  const draw = (s) => { const k = Math.round(s.i); let o = "";
    L.forEach(([n, t], i) => { const y = 14 + i * 58, on = i <= k, cur = i === k; o += SV.rect(20, y, 220, 46, cur ? "cell-warn" : on ? "cell-ok" : "cell", { rx: 8 }) + SV.text(34, y + 29, n, "lbl bd") + (on ? SV.text(264, y + 29, t, "lbl") : "") ; if (i < 4) o += SV.path("M130," + (y + 46) + " V" + (y + 58), "ax"); });
    o += SV.text(588, 40, "the user sees", "sm", { "text-anchor": "middle" }) + SV.text(588, 56, "only this", "sm", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stA"), { w: 640, h: 306, label: "Layers", base: { i: 0 }, draw, tween: 150, dwell: 2400, steps: [
    { cap: "The user clicks <b>Save</b>. This is all the user does.", s: { i: 0 } }, { cap: "The application does not touch the disk. It asks the <b>operating system</b> to save the file.", s: { i: 1 } },
    { cap: "The OS chooses where on the disk the file goes and records its name in the file system.", s: { i: 2 } }, { cap: "The <b>device driver</b> turns the OS's request into the commands this disk understands.", s: { i: 3 } },
    { cap: "The hardware stores the data. The user never dealt with sectors, buses or commands: the OS hid the complexity.", s: { i: 4 } }] });
})();
(function () {
  const P = [["A", "f1"], ["B", "f2"], ["C", "f3"]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "one processor", "sm");
    const seq = [0, 1, 2, 0, 1, 2], slice = 56; o += SV.text(20, 44, "multi-tasking: time slices", "lbl bd");
    for (let i = 0; i < 6; i++) { const on = i < k; if (on) o += SV.rect(20 + i * slice, 56, slice - 4, 36, P[seq[i]][1], { rx: 4 }) + SV.rect(20 + i * slice, 56, slice - 4, 36, "ax", { rx: 4, fill: "none" }) + SV.text(20 + i * slice + (slice - 4) / 2, 79, P[seq[i]][0], "lbl bd", { "text-anchor": "middle" }); }
    o += SV.text(20, 130, "no multi-tasking: one at a time", "lbl bd");
    const w3 = 112; for (let i = 0; i < 3; i++) { const on = i * 2 < k; if (on) o += SV.rect(20 + i * w3, 142, w3 - 4, 36, P[i][1], { rx: 4 }) + SV.rect(20 + i * w3, 142, w3 - 4, 36, "ax", { rx: 4, fill: "none" }) + SV.text(20 + i * w3 + (w3 - 4) / 2, 165, P[i][0], "lbl bd", { "text-anchor": "middle" }); }
    if (k === 6) o += SV.text(20, 210, "With time slices A, B and C all make progress early; one at a time, C waits for A and B to finish.", "lbl bd t3", { style: "font-size:12.5px" }); return o; };
  Lib.stepper($("#stB"), { w: 640, h: 232, label: "Multi-tasking", base: { i: 0 }, draw, tween: 150, dwell: 1600, steps: [0, 1, 2, 3, 4, 5, 6].map((i) => ({ cap: i === 0 ? "Three programs A, B and C want the one processor. Compare the two ways of sharing it." : i === 6 ? "After six slices each program has had two turns. The OS switches between them so quickly that they seem to run together." : "Slice " + i + ": the processor runs " + "ABCABC"[i - 1] + " for a short time, then the OS switches to the next process.", s: { i } })) });
})();
(function () {
  const items = [["CPU time", "scheduler shares it"], ["Memory", "memory manager allocates it"], ["Printer", "queue and driver"], ["Disk", "file system tracks files"]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 20, 180, 190, "cell", { rx: 10 }) + SV.text(110, 46, "Operating system", "lbl bd", { "text-anchor": "middle" });
    items.forEach(([n, t], i) => { const on = i < k; o += SV.rect(34, 62 + i * 36, 152, 28, on ? "cell-ok" : "cell", { rx: 6, ...op(on ? 1 : 0.35) }) + SV.text(110, 81 + i * 36, n, "lbl", { "text-anchor": "middle", ...op(on ? 1 : 0.5) }); });
    ["Program A", "Program B", "Program C"].forEach((p, i) => { o += SV.rect(330, 30 + i * 62, 130, 40, "f" + (i + 1), { rx: 8 }) + SV.rect(330, 30 + i * 62, 130, 40, "ax", { rx: 8, fill: "none" }) + SV.text(395, 55 + i * 62, p, "lbl bd", { "text-anchor": "middle" }) + SV.path("M200," + (110 + (i - 1) * 0) + " L330," + (50 + i * 62), "edge", { ...op(k > 0 ? 0.5 : 0.1) }); });
    if (k > 0) o += SV.text(250, 232, items[k - 1][0] + ": " + items[k - 1][1], "lbl bd t3"); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 250, label: "Resources", base: { i: 0 }, draw, tween: 150, dwell: 2200, steps: [{ cap: "Programs A, B and C all want the computer's resources.", s: { i: 0 } }, { cap: "The OS shares the <b>processor</b> between them by scheduling.", s: { i: 1 } }, { cap: "It gives each program its own part of <b>memory</b> and keeps them apart.", s: { i: 2 } }, { cap: "It queues requests for the <b>printer</b> and uses a driver to control it.", s: { i: 3 } }, { cap: "It tracks the files on the <b>disk</b>. All the sharing is hidden from the user.", s: { i: 4 } }] });
})();

(function () {
  let n = 1;
  const paint = () => { let o = ""; const busy = Math.min(100, Math.round(40 * n)); const cols = 10; let t = '<div class="tw"><table class="t mono"><tr><th>unit</th>' + Array.from({ length: 10 }, (_, i) => "<th>" + (i + 1) + "</th>").join("") + "</tr><tr><td>CPU</td>";
    // each program: 2 CPU units then 3 waiting units, starts offset by 2 units per program
    const cpu = Array(10).fill("");
    for (let p = 0; p < n; p++) for (let u = 0; u < 10; u++) { const ph = (u - 2 * p + 100) % 5; if (u >= 2 * p && ph < 2 && cpu[u] === "") cpu[u] = "P" + (p + 1); }
    let b = 0; cpu.forEach((c) => { t += "<td" + (c ? ' style="background:var(--good-soft)"' : ' style="background:var(--bad-soft)"') + ">" + (c || "idle") + "</td>"; if (c) b++; });
    $("#mT").innerHTML = t + "</tr></table></div>"; $("#m1").textContent = b * 10 + "%"; $("#m2").textContent = 100 - b * 10 + "%"; };
  Lib.slider($("#mS"), { id: "ms", label: "Programs running together ", min: 1, max: 3, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();
btnTable("oB", "oO", [
  ["Print a document", "Queues the job, loads the printer driver, sends data to the printer", "Device management and drivers"],
  ["Open two programs", "Allocates memory to each and shares the processor", "Memory and process management"],
  ["Save a file", "Finds free space on the disk and records the file name", "File management"],
  ["Log in", "Checks the user name and password and sets permissions", "User and security management"],
  ["Press a key", "Handles the interrupt and passes the key to the program", "Kernel as interrupt handler"],
  ["Click an icon", "Turns the click into the right action; the user need not know the hardware", "User interface"]
], ["Task", "What the OS does", "Part"]);
(function () {
  let q = 4;
  const paint = () => { const total = 12, nSw = Math.ceil(total / q); let t = '<div class="tw"><table class="t mono"><tr><th>CPU timeline (units)</th></tr><tr><td>'; const seq = []; let rem = [4, 4, 4], i = 0; while (rem.some((x) => x > 0)) { if (rem[i % 3] > 0) { const u = Math.min(q, rem[i % 3]); seq.push("P" + (i % 3 + 1) + "×" + u); rem[i % 3] -= u; } i++; }
    $("#tT").innerHTML = t + seq.join(" → ") + "</td></tr></table></div>"; $("#tV").innerHTML = "Time slice " + q + " unit" + (q > 1 ? "s" : "") + ": the OS switches process <b>" + (seq.length - 1) + "</b> times. A very short slice means many switches (more overhead); a very long slice makes the processes wait for each other."; };
  Lib.slider($("#tS"), { id: "ts", label: "Time slice (units) ", min: 1, max: 4, value: q, fmt: (x) => x, onInput: (v) => { q = v; paint(); } }); paint();
})();
''' + CLASSIFY("cl1", "Which part of the OS does the task belong to?", ["Process management", "Memory management", "File management", "Device management"],
  [("Choosing which program gets the CPU next", 0), ("Giving a program a block of RAM", 1), ("Recording where a file is on the disk", 2), ("Using a driver to control a printer", 3), ("Switching between two programs many times a second", 0), ("Moving unused data out of RAM to the disk", 1)],
  "Processes, memory, files, devices.") + CLASSIFY("cl2", "Does it help to hide the complexity of the hardware?", ["Yes", "No"],
  [("A graphical user interface with icons", 0), ("A device driver for a printer", 0), ("Being able to save a file by name", 0), ("The speed of the processor", 1), ("The size of the RAM", 1), ("Typing a command that sets a memory address", 1)],
  "Interfaces, drivers and the file system hide the hardware.") + MATCH([
  ["Multi-tasking", "Many programs that appear to run at the same time"], ["Scheduling", "Managing the processes running on the CPU"], ["Interrupt handling", "Transferring control to another routine when a service is required"], ["Paging", "Reading and writing same-size blocks to and from secondary storage"], ["Virtual memory", "Using secondary storage to simulate additional main memory"]]) + ORDER(
  "Put the steps in order for printing a document.",
  ["The user clicks Print", "The application asks the OS to print", "The OS queues the print job", "The printer driver converts the data into printer commands", "The printer prints the page"],
  "Click, application, OS, driver, hardware.") + CALC([
  {"q": "Each program uses the CPU for 2 units and waits 3 units. With one program, what percentage of the time is the CPU busy?", "a": 40, "unit": "%", "tol": 0.5, "hint": "2 out of 5 units.", "sol": "<b>40</b>%."},
  {"q": "With three such programs run together and perfectly spaced, how many units out of 5 is the CPU busy?", "a": 5, "unit": "", "tol": 0.01, "hint": "Each adds 2 units, up to 5 in a cycle.", "sol": "<b>5</b>: the CPU is fully used."},
  {"q": "Three processes each need 4 units and the time slice is 2 units. How many slices does the CPU run in total?", "a": 6, "unit": "", "tol": 0.01, "hint": "Two slices each.", "sol": "<b>6</b>."},
  {"q": "Three processes each need 4 units and the time slice is 4. How many switches between processes?", "a": 2, "unit": "", "tol": 0.01, "hint": "Three slices, so two switches.", "sol": "<b>2</b>."},
  {"q": "How many resources are listed in the table in the Learn tab (processor, memory, input and output devices, storage, users)?", "a": 5, "unit": "", "tol": 0.01, "hint": "Count the rows.", "sol": "<b>5</b>."}]) + MCQ([
  ("What does multi-tasking let the computer do?", ["Run exactly one program", "Run, or appear to run, several programs at a time", "Make the screen larger", "Delete old files"], 1, "It shares the processor."),
  ("A device driver is:", ["Hardware", "Software that controls a particular device", "A kind of memory", "A file"], 1, "It lets the OS control a device."),
  ("The kernel:", ["Is the central part of the OS", "Is a printer", "Is an application", "Is a type of cable"], 0, "The core of the OS."),
  ("Which hides hardware complexity?", ["A graphical user interface", "A bigger monitor", "A faster disk", "A longer cable"], 0, "The interface."),
  ("Why does the OS give each process a time slice?", ["To save paper", "So all processes make progress", "To make the disk smaller", "To stop interrupts"], 1, "Sharing the processor."),
  ("Virtual memory uses:", ["Secondary storage", "A printer", "The keyboard", "The power supply"], 0, "Disk space as extra memory.")], "qz1") + CARDS([
  ("OS", "Manages the hardware and provides a platform for applications."), ("Resources", "Processor, memory, devices, files and users."), ("Multi-tasking", "Several processes appear to run at once by sharing the CPU."), ("User interface", "Hides the hardware: icons and menus."),
  ("Device driver", "Lets the OS control a specific device."), ("Kernel", "Core of the OS: processes, memory, interrupts."), ("Time slice", "A short turn of the CPU for one process."), ("Abstraction", "Showing the user only what they need.")])

build("ac1611", "ac-16-1-1-os-purposes-resources", "Operating Systems: Purposes and Resources", EYA("16.1.1"),
  "What an operating system does: managing resources, multi-tasking, the user interface and device drivers hiding the hardware, and the kernel; animations, labs and the real Paper 3 questions from 2021 to 2025.",
  dict(sub=CBK("Chapter 16 · System software, section 16.1 Purposes of an operating system"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
