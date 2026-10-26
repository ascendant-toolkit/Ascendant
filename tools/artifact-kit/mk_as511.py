"""AS CS 5.1.1: the operating system and its key management tasks. Run: python3 tools/artifact-kit/mk_as511.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>The <b>operating system (OS)</b> is system software that <b>hides the complexity of the hardware</b> from the user, <b>provides a platform for application software to run</b> and <b>provides a user interface</b>. Its key management tasks are <b>process management</b> (scheduling which process runs next, multitasking, resolving conflicts), <b>memory management</b> (allocating RAM to processes and freeing it), <b>file management</b> (organising files and folders on storage), <b>security management</b> (users, passwords, access rights) and <b>hardware management</b> (device drivers, input and output, interrupts, buffers). A question usually asks you to <b>identify</b> tasks (a name per mark) or to <b>describe</b> them (a name and a matching description). Give a specific description for each task, not just its name. Interrupts and buffers belong partly to hardware management.</p></div>

  <h2>1 · Purposes of an operating system</h2>
  <ul>
    <li>To <b>hide the complexities of the hardware</b> from the user and from application programs.</li>
    <li>To <b>provide a platform</b> for application software to run on.</li>
    <li>To provide a <b>user interface</b> so the user can communicate with the computer.</li>
  </ul>

  <h2>2 · The key management tasks</h2>
  <div class="tw"><table class="t">
    <tr><th>Task</th><th>What it does</th></tr>
    <tr><td><b>Process management</b></td><td>Decides which process runs next (scheduling) and allocates time slices; moves processes between states (ready, running, waiting); supports multitasking so several programs seem to run at once; resolves conflicts when two processes need the same resource; allows processes to share data and prevents them interfering with each other</td></tr>
    <tr><td><b>Memory management</b></td><td>Allocates RAM to processes when they start and frees it when they close; makes sure two processes do not access the same memory; controls the movement of data between RAM, the processor and virtual memory</td></tr>
    <tr><td><b>File management</b></td><td>Divides storage into file allocation units and allocates space to files; creates and maintains directory (folder) structures; names, creates, renames, opens, closes, copies, moves and deletes files; sets the logical file system (such as FAT or NTFS); controls access, access rights and sharing; marks unallocated space as available</td></tr>
    <tr><td><b>Security management</b></td><td>Prevents unauthorised access by validating users and processes (accounts and passwords); implements access rights and permissions; provides or updates a firewall and anti-malware; provides recovery of lost data; applies OS security updates; keeps logs and audits activity</td></tr>
    <tr><td><b>Hardware management</b></td><td>Installs and loads <b>device drivers</b> for devices connected to external ports; manages communication between devices and the computer, sending data to output devices and receiving it from input devices; handles <b>buffers</b> for different speeds; manages hardware <b>interrupts</b></td></tr>
  </table></div>

  <h2>3 · Multitasking</h2>
  <p>With one processor core the OS shares processor time between processes in <b>time slices</b>: each process runs for a short slice, is paused, and the next one runs. This happens so fast that the user sees several programs running at once. The OS decides the order using a scheduling algorithm (for example giving a high-priority process more or earlier time) and keeps each process's registers so it can resume exactly where it stopped.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Listing only the task name when the question says "describe". Add what it does.</li>
    <li>Describing file management as "storing files". Say it creates directories, allocates space and controls access.</li>
    <li>Mixing process and memory management: scheduling is process management; allocating RAM is memory management.</li>
    <li>Saying hardware management "controls the hardware". Say it installs device drivers, manages communication and interrupts.</li>
    <li>Saying the OS is "the interface". That is one purpose among three.</li>
  </ul>
'''

watch = '''
  <h2>1 · Multitasking by time slices</h2>
  <div id="stA"></div>
  <h2>2 · Memory management</h2>
  <div id="stB"></div>
  <h2>3 · An application asks the OS</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Time slices</h2>
  <p>Three processes share one processor. Change the length of the time slice.</p>
  <div class="card"><div id="tS"></div><div id="tG"></div><div id="tV" class="verdict"></div></div>
  <h2>Lab 2 · Which management task?</h2>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>
  <h2>Lab 3 · Memory allocation</h2>
  <div class="card"><div class="btnrow"><button id="mm_a">Open a program</button><button id="mm_b">Close the last program</button><button id="mm_r">Reset</button></div><div id="mmG"></div><div id="mmV" class="verdict"></div></div>
'''

_pr, _prjs = PR(["Which management task?", "Purpose or management task?", "Match the task to its description", "Put the multitasking steps in order", "Working out", "Multiple choice"],
  ("Which key management task does it describe?", ["Process", "Memory", "File", "Security", "Hardware"], [("Decides which process runs next", 0), ("Allocates RAM to a program when it starts", 1), ("Creates and maintains folders", 2), ("Validates a user's password", 3), ("Installs a device driver", 4), ("Allows two processes to share data", 0)], "Match the job to the task."),
  ("Is it a purpose of the OS or a key management task?", ["Purpose", "Management task"], [("Provide a user interface", 0), ("Memory management", 1), ("Hide the complexity of the hardware", 0), ("Security management", 1), ("Provide a platform for software to run", 0), ("File management", 1)], "Purposes: hide, platform, interface."),
  [["Process management", "Dynamically decides which process runs next"], ["Memory management", "Allocates RAM to processes and frees it"], ["File management", "Marks unallocated file storage for availability"], ["Security management", "Validates user and process authenticity"], ["Hardware management", "Installs device drivers for external ports"]],
  ("Put the multitasking steps in order.", ["Process A runs for its time slice", "The OS stores A's registers", "The OS loads the registers of process B", "Process B runs for its time slice", "The OS returns to A when it is its turn again"], "Run, store, load, run, return."),
  [{"q": "Three processes each get a 10 ms time slice in turn. How many ms before process A runs again?", "a": 30, "unit": "ms", "tol": 0.1, "hint": "3 × 10.", "sol": "<b>30</b> ms."}, {"q": "A computer has 8 GB of RAM and the OS uses 2 GB. How many GB are free for processes?", "a": 6, "unit": "GB", "tol": 0.01, "hint": "8 − 2.", "sol": "<b>6</b> GB."}, {"q": "Four programs need 1 GB each. How many can run in 6 GB free RAM?", "a": 4, "unit": "", "tol": 0.01, "hint": "All four fit (4 GB).", "sol": "<b>4</b>."}, {"q": "A file is stored in allocation units of 4 KiB. A 10 KiB file needs how many units?", "a": 3, "unit": "", "tol": 0.01, "hint": "10 ÷ 4 rounded up.", "sol": "<b>3</b>."}, {"q": "How many key management tasks are listed in the Learn tab?", "a": 5, "unit": "", "tol": 0.01, "hint": "Process, memory, file, security, hardware.", "sol": "<b>5</b>."}],
  [("A purpose of the OS is to:", ["Hide the complexity of the hardware", "Compile programs", "Store files only", "Increase the clock speed"], 0, "Hide hardware complexity."), ("Scheduling belongs to:", ["Process management", "Memory management", "File management", "Security management"], 0, "Process."), ("Device drivers are installed by:", ["Hardware management", "File management", "Memory management", "Process management"], 0, "Hardware."), ("Access rights are part of:", ["Security management", "Hardware management", "Process management", "Memory management"], 0, "Security."), ("Multitasking is done by:", ["Time slices", "Faster RAM", "Two screens", "Compression"], 0, "Time slices."), ("File management does:", ["Create and maintain directories", "Allocate RAM", "Schedule processes", "Install drivers"], 0, "Directories.")],
  [("OS purposes", "Hide hardware, platform, user interface."), ("Process", "Scheduling, multitasking, conflicts."), ("Memory", "Allocate and free RAM."), ("File", "Folders, space, names, access."), ("Security", "Accounts, passwords, access rights."), ("Hardware", "Drivers, communication, interrupts."), ("Time slice", "Short turn on the processor."), ("Device driver", "Software to control a device.")])

real = RWNOTE + (
rw("Running music while you type", "The OS gives the music player and the word processor turns on the processor, so both seem to run at the same time.", "multitasking: process management.") +
rw("Plugging in a printer", "The OS finds and loads the printer's driver so programs can print without knowing how the printer works.", "hardware management hides complexity.") +
rw("Logging into a school computer", "Your account decides which files you can open: the OS checks your identity and your access rights.", "security management.") +
rw("Closing a program frees memory", "When you close an app, the OS takes its RAM back so another program can use it.", "memory management.") +
rw("Creating a new folder", "The OS records the folder in its directory structure and later finds the files stored in it.", "file management.")
)

where = [
  ("M/J 2021", "11, 13", "2(b)", "4", "Identify four key management tasks of the OS"),
  ("O/N 2021", "12", "7(b)", "4", "Describe the file management tasks"),
  ("M/J 2022", "13", "4(a)", "4", "Describe the key management tasks"),
  ("O/N 2022", "13", "3", "4", "Match four OS management tasks to their descriptions"),
  ("M/J 2023", "11", "3(a), (b)", "4 + 2", "How the OS manages peripherals; two other management tasks"),
  ("M/J 2023", "12", "5(d)(i)", "5", "How the OS manages processes"),
  ("O/N 2023", "12", "8(a)", "1", "One purpose of the OS"),
  ("O/N 2024", "11", "4(a)(i)", "2", "File management tasks"),
  ("O/N 2024", "12", "3(c)", "4", "Process management tasks"),
  ("M/J 2025", "11", "6(b)", "5", "The purpose of an OS"),
  ("O/N 2025", "11", "5(a)", "2 + 2", "Hardware management and security management tasks"),
  ("O/N 2025", "13", "8(d)", "3", "Three key management tasks other than memory management"),
  ("M/J 2026", "12", "7(a)(i), (ii)", "2 + 2", "Process management and memory management tasks"),
  ("M/J 2026", "13", "5(a)", "2 + 2", "Hardware management tasks; two other key tasks")]

past = '''  <p class="note">The OS management tasks are asked in Paper 1 every series, in a different form each time (identify, describe, match). Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "11/13", "Q2(b)"), "4 marks", "Identify",
  "Bingwen's computer comes with an Operating System and utility software. Identify four key management tasks that the Operating System will perform.", "Memory, file, security, hardware, process.",
  "<p>" + mks(["Memory management", "File management", "Security management", "Hardware (or input/output) management", "Process management"]) + " (any four)</p>", None) + peq(SRC("w21", "12", "Q7(b)"), "4 marks", "Describe",
  "Describe the file management tasks that an Operating System performs.", "Allocation units, directories, naming, access.",
  "<p>Any four: " + mks(["Storage space is divided into file allocation units", "Space is allocated to particular files", "Maintains or creates directory structures", "Specifies the logical method of file storage (such as FAT or NTFS)", "Provides file naming conventions", "Controls access, implements access rights or password protection, makes file sharing possible", "Specifies the tasks that can be performed on a file (open, close, delete, copy, create, move)"]) + "</p>", "Writing 'it saves files'. Name the directory, allocation and access tasks.") + peq(SRC("s22", "13", "Q4(a)"), "4 marks", "Describe",
  "Describe the key management tasks of an operating system.", "A task name and a matching description, for several tasks.",
  "<p>One mark for identifying a task, up to two marks for its description (max 2 for tasks with no description): " + mks(["Memory management: controls the movement of data between RAM, the processor and virtual memory; allocates memory to processes", "File management: creates files and folders; renames files and folders", "Security management: creates accounts and passwords; provides or upgrades a firewall or anti-malware", "Hardware management: receives data from input devices, sends data to output devices; uses device drivers", "Process management: decides which process to run next; supports multitasking"]) + "</p>", None) + peq(SRC("w22", "13", "Q3"), "4 marks", "Match",
  "Draw one line from each OS management task to its most appropriate description. Tasks: hardware management; security management; memory management; process management. Descriptions: dynamically allocates memory to processes; marks unallocated file storage for availability; installs programs for devices connected to external ports; validates user and process authenticity; allows processes to transfer data to and from each other.", "One description is a distractor (file management).",
  "<p>" + mks(["Hardware management: installs programs for devices connected to external ports", "Security management: validates user and process authenticity", "Memory management: dynamically allocates memory to processes", "Process management: allows processes to transfer data to and from each other"]) + "</p>", "Matching memory management to 'marks unallocated file storage'. That is file management.") + peq(SRC("s23", "11", "Q3(a)(b)"), "4 + 2 marks", "Describe / Identify",
  "A computer has an Operating System. (a) Describe how the OS manages the peripheral hardware devices of the computer. (b) Hardware management is one key management task. Identify two other key management tasks.", "Drivers, send and receive data, buffers, interrupts. Memory, file, security, process.",
  "<p><b>(a)</b> Any four: " + mks(["Installs device drivers", "to allow communication between the peripherals and the computer", "Sends data to and receives data from peripherals, such as to an output device and from an input device", "Handles buffers for the transfer of data", "to ensure smooth transfer between devices that transmit and receive at different speeds", "Manages interrupts or signals from the device"]) + "</p><p><b>(b)</b> " + mks(["Memory management", "File management", "Security management", "Process management", "Error checking and recovery"], "a") + " (any two)</p>", None) + peq(SRC("s23", "12", "Q5(d)(i)"), "5 marks", "Describe",
  "Describe how the Operating System manages processes in the computer.", "Scheduling, resources, sharing data, no interference, multitasking.",
  "<p>Any five: " + mks(["Manages the scheduling of processes (decides which order to run processes)", "Manages which resources the processes require, such as allocating memory", "Enables processes to share data", "Prevents interference between processes (resolution of conflicts)", "Handles the process queue", "Allows multitasking or multiprocessing", "by ensuring fair access, handling priorities and handling interrupts"]) + "</p>", None) + peq(SRC("w23", "12", "Q8(a)"), "1 mark", "State",
  "State one purpose of the Operating System.", "Hide hardware, platform, interface.",
  "<p>One: " + mks(["To hide the complexities of the hardware from the user", "To provide a platform for software to run", "To provide a user interface"]) + "</p>", None) + peq(SRC("w24", "11", "Q4(a)(i)"), "2 marks", "Describe",
  "Describe the file management tasks carried out by an OS.", "Two of the file management points.",
  "<p>Any two: " + mks(["Secondary storage space is divided into file allocation units", "Space on secondary storage is allocated to particular files", "Maintains or creates directory structures", "Specifies the logical method of file storage, such as FAT or NTFS", "Provides file naming conventions", "Controls user access, implements access rights or password protection, makes file sharing possible", "Specifies the tasks that can be performed on a file", "Allows searching for a file"]) + "</p>", None) + peq(SRC("w24", "12", "Q3(c)"), "4 marks", "Describe",
  "One of the key management tasks of the OS is process management. Describe the process management tasks performed by an OS.", "Scheduling, multitasking, fairness, interrupts, resources, sharing, conflicts.",
  "<p>Any four: " + mks(["It manages the scheduling of processes (decides which process is to be run next)", "Allows multitasking or multi-processing", "Ensures fair access", "Handles interrupts", "Manages or allocates which resources the processes require", "Facilitates the sharing and exchange of data between processes", "Prevents interference between processes (conflict resolution)"]) + "</p>", None) + peq(SRC("s25", "11", "Q6(b)"), "5 marks", "Describe",
  "Describe the purpose of an OS in a computer.", "User interface, memory, files, input and output, processes.",
  "<p>Any five: " + mks(["To provide a user interface so that the user is able to communicate with the hardware", "To manage memory so that data can be stored and accessed and multitasking is possible", "To manage files, allowing the user to create, edit, update and delete files and folders", "To manage inputs and outputs from hardware and peripherals", "To handle processes, making sure each process has fair access"]) + "</p>", None) + peq(SRC("w25", "11", "Q5(a)"), "2 + 2 marks", "State",
  "The OS is responsible for hardware and security management. (i) State two tasks performed by hardware management. (ii) State two tasks performed by security management.", "Drivers, communication, interrupts. Authentication, access rights, recovery, updates, logs.",
  "<p><b>(i)</b> Any two: " + mks(["Installs driver software for devices connected to external ports", "Manages communication between devices", "Manages hardware interrupts"]) + "</p><p><b>(ii)</b> Any two: " + mks(["Prevents unauthorised access by providing authentication or validating users and processes", "Implements access rights and permissions", "Makes provision for the recovery of lost data", "Carries out OS security updates", "Carries out auditing and keeps logs of activity"], "a") + "</p>", None) + peq(SRC("w25", "13", "Q8(d)"), "3 marks", "Give",
  "Memory management is one key management task performed by an OS. Give three other key management tasks that are performed by an OS.", "File, security, hardware, process.",
  "<p>" + mks(["File management", "Security management", "Hardware, peripheral or input/output management", "Process management"]) + " (any three)</p>", None) + peq(SRC("s26", "12", "Q7(a)(i)(ii)"), "2 + 2 marks", "Identify",
  "A student uses a computer that comes with an OS. (i) Identify two tasks the OS performs as part of process management. (ii) Identify two tasks the OS performs as part of memory management.", "Scheduling, time slices, conflicts. Allocate RAM, free memory.",
  "<p><b>(i)</b> Any two: " + mks(["Efficient allocation of resources to processes", "Moving processes between states", "Allocating time slices to processes", "Scheduling processes (an example of a scheduling algorithm)", "Resolution of conflicts when two processes require the same resource", "Allows communication between processes"]) + "</p><p><b>(ii)</b> Any two: " + mks(["Dynamically allocates RAM to processes", "Frees up memory when the process closes", "Makes sure two processes do not access the same memory", "Accesses data from RAM when needed"], "a") + "</p>", None) + peq(SRC("s26", "13", "Q5(a)"), "2 + 2 marks", "Identify",
  "(i) Identify two tasks the OS performs as part of hardware management. (ii) Identify two other key management tasks that the OS performs.", "Transfer data, drivers, abstraction. Memory, process, file, security.",
  "<p><b>(i)</b> Any two: " + mks(["Transfer data between peripheral devices", "Translate data from input/output or peripheral devices", "Loading and installation of device drivers", "Hardware abstraction (hiding hardware differences from applications)", "Power management"]) + "</p><p><b>(ii)</b> Any two: " + mks(["Memory management", "Process management", "File management", "Security management (managing user accounts)", "Provide a platform for running applications"], "a") + "</p>", None)

review = req("2 marks", "State", "State two purposes of an operating system.", "Hide, platform, interface.", "<p>" + mks(["To hide the complexities of the hardware", "To provide a user interface"]) + "</p>", None) + req("3 marks", "Describe", "Describe how the OS performs memory management when you open and close a program.", "Allocate and free.", "<p>" + mks(["It allocates RAM to the program when it opens", "It makes sure two programs do not use the same memory", "It frees the memory when the program closes"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a computer with one processor core can appear to run several programs at once.", "Time slices.", "<p>" + mks(["The OS gives each process a short time slice in turn", "switching so quickly that they appear to run at once (multitasking)"]) + "</p>", None) + req("2 marks", "Describe", "Describe one security management task.", "Accounts, access rights.", "<p>" + mks(["It creates user accounts protected by passwords", "and sets access rights so users can only open permitted files"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a new printer needs a device driver.", "Hide complexity.", "<p>" + mks(["The driver allows the OS to communicate with the printer", "so programs can print without knowing how the printer works (hardware management)"]) + "</p>", None)

tips = tips_html([
  ("Name each task, then describe it.", "Marks come in pairs."),
  ("Three purposes.", "Hide hardware, platform, user interface."),
  ("Process: scheduling.", "Memory: allocate and free RAM."),
  ("File: directories, space, access.", "Not just 'stores files'."),
  ("Hardware: drivers and interrupts.", "Security: accounts and rights."),
  ("Use the scenario.", "A printer, a login, a new app."),
], [("an operating system", "System software that manages the hardware and runs applications."), ("multitasking", "Sharing processor time so several processes seem to run together."), ("a device driver", "Software that lets the OS control a device."), ("a time slice", "The short period a process runs before the next one.")],
  [("Identify", "Name the tasks."), ("State", "Short answer."), ("Describe", "Several points."), ("Match", "Link each task to its description.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const names = ["A", "B", "C"]; const draw = (s) => { const k = Math.round(s.i); let o = ""; for (let i = 0; i < 6; i++) { const p = names[i % 3]; o += SV.rect(30 + i * 85, 50, 80, 36, i === k ? "f3" : i < k ? "f1" : "cell", { rx: 6 }) + SV.text(70 + i * 85, 73, "Process " + p, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); }
    o += SV.text(30, 30, "time →", "sm") + SV.text(30, 120, k < 6 ? "Process " + names[k % 3] + " has the processor now; the others wait" : "", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 135, label: "Time slices", base: { i: 0 }, draw, tween: 100, dwell: 1600, steps: [0, 1, 2, 3, 4, 5].map((i) => ({ cap: i === 0 ? "The OS gives <b>process A</b> a time slice." : i < 3 ? `The OS stores the registers and gives <b>process ${names[i]}</b> the next slice.` : "The cycle repeats: each process gets a turn again.", s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const blocks = [["OS", 3, "f3"], ["Browser", k >= 1 ? 3 : 0, "f1"], ["Game", k >= 2 ? 4 : 0, "f2"], ["free", 10 - 3 - (k >= 1 ? 3 : 0) - (k >= 2 ? 4 : 0) + (k >= 3 ? 3 : 0), "cell"]]; let x = 30, o = "";
    const list = k >= 3 ? [["OS", 3, "f3"], ["free", 3, "cell"], ["Game", 4, "f2"], ["free", 0, "cell"]] : blocks; let rest = 10; list.forEach(([n, w, c]) => { if (w > 0) { o += SV.rect(x, 40, w * 45, 44, c, { rx: 4 }) + SV.text(x + w * 22, 67, n, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); x += w * 45; rest -= w; } });
    if (k >= 3) { o = ""; x = 30; [["OS", 3, "f3"], ["free", 3, "cell"], ["Game", 4, "f2"]].forEach(([n, w, c]) => { o += SV.rect(x, 40, w * 45, 44, c, { rx: 4 }) + SV.text(x + w * 22, 67, n, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); x += w * 45; }); }
    o += SV.text(30, 20, "RAM", "sm") + SV.text(30, 115, ["only the OS in memory", "the OS allocates RAM to the browser", "and to the game; neither can touch the other's memory", "the browser closes: its RAM is freed for others"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 520, h: 130, label: "Memory", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [0, 1, 2, 3].map((i) => ({ cap: ["RAM holds only the OS.", "The OS <b>allocates</b> RAM to the browser.", "It allocates RAM to the game and makes sure they do not share memory.", "When the browser closes the OS <b>frees</b> its memory."][i], s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 120, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 60, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); let o = B(20, "Application", k >= 0) + B(220, "OS", k >= 1) + B(420, "Printer", k >= 3) + SV.path("M140,62 H220", "ax") + SV.path("M340,62 H420", "ax");
    o += SV.text(260, 125, ["Word processor: Print", "the OS receives the request (a platform for the app)", "the OS finds the printer's device driver", "the driver controls the printer; the app never needed to know how"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 140, label: "OS and hardware", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [0, 1, 2, 3].map((i) => ({ cap: ["An application asks to print.", "The OS handles the request.", "Hardware management: the OS uses the printer's <b>driver</b>.", "The OS hides the printer's complexity from the application."][i], s: { i } })) });
})();

(function () {
  let slice = 20; const paint = () => { const T = 240; let o = '<svg viewBox="0 0 440 90" style="width:440px;max-width:100%;display:block">'; const col = ["var(--accent)", "var(--good)", "var(--warn,#c89500)"]; let t = 0, i = 0, n = 0; while (t < T && n < 40) { const w = Math.min(slice, T - t); o += `<rect x="${20 + t * 1.6}" y="20" width="${Math.max(w * 1.6 - 1, 1)}" height="40" fill="${col[i % 3]}" opacity=".8"/>`; t += w; i++; n++; }
    o += `<text x="20" y="80" class="sm" style="font-size:11px">0</text><text x="${20 + T * 1.6}" y="80" class="sm" text-anchor="end" style="font-size:11px">${T} ms</text></svg>`; $("#tG").innerHTML = o; const sw = Math.ceil(T / slice) - 1;
    $("#tV").innerHTML = `With a <b>${slice} ms</b> time slice, each process gets the processor ${Math.ceil(T / slice / 3)} times in ${T} ms, so the OS makes about <b>${sw} switches</b>. Short slices make the programs seem to run at once but cost more switching; long slices switch less but a process may wait longer.`; };
  Lib.slider($("#tS"), { id: "t1", label: "Time slice (ms) ", min: 5, max: 80, step: 5, value: slice, fmt: (x) => x, onInput: (v) => { slice = v; paint(); } }); paint();
})();
btnTable("mB", "mO", [
  ["Scheduling which program runs next", "Process management", "Time slices and priorities"],
  ["Giving a new program some RAM", "Memory management", "Allocate and free"],
  ["Creating a new folder", "File management", "Directory structures"],
  ["Checking a password at log-in", "Security management", "Authentication"],
  ["Loading a driver for a new mouse", "Hardware management", "Device driver"],
  ["Handling a key press interrupt", "Hardware management", "Manages interrupts"]
], ["Job", "Task", "Detail"]);
(function () {
  const total = 10; let progs = []; let next = 1;
  const paint = () => { const used = progs.reduce((a, p) => a + p.w, 0) + 2; let x = 0, o = '<svg viewBox="0 0 480 80" style="width:480px;max-width:100%;display:block">'; const seg = (n, w, c) => { o += `<rect x="${10 + x * 45}" y="10" width="${w * 45 - 2}" height="40" rx="4" class="${c}"/><text x="${10 + x * 45 + w * 22}" y="35" text-anchor="middle" class="lbl bd" style="font-size:11px">${n}</text>`; x += w; };
    seg("OS", 2, "f3"); progs.forEach((p) => seg(p.n, p.w, "f1")); if (total - used > 0) seg("free", total - used, "cell"); $("#mmG").innerHTML = o + "</svg>"; $("#mmV").innerHTML = `RAM in use: <b>${used} of ${total} GB</b>. The OS allocates memory when a program opens and frees it when the program closes.`; };
  $("#mm_a").onclick = () => { const used = progs.reduce((a, p) => a + p.w, 0) + 2; if (used + 2 <= total) { progs.push({ n: "P" + next++, w: 2 }); paint(); } else $("#mmV").innerHTML = "Not enough free RAM: the OS cannot allocate memory for another program (it would use virtual memory)."; };
  $("#mm_b").onclick = () => { progs.pop(); paint(); }; $("#mm_r").onclick = () => { progs = []; next = 1; paint(); }; paint();
})();
''' + _prjs

finish("as-5-1-1-operating-system-management", "as511", "The Operating System and its Management Tasks",
  "The purposes of an operating system and its key management tasks (process, memory, file, security and hardware), with animations, labs and the real Paper 1 questions from 2021 to 2026.",
  "5.1.1", "5 · System software", "section 5.1 Operating systems", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on the operating system and its management tasks (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
