/* shared helpers for the IGCSE CS chapter 4 reviews */
const MONO = "font-family:ui-monospace,Menlo,Consolas,monospace;";
const mk = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
function section(id, parts) { const root = $("#" + id); parts.forEach((p) => { if (p.h) root.appendChild(mk("h2", "", p.h)); if (p.p) root.appendChild(mk("p", "", p.p)); const d = mk("div", p.card ? "card" : ""); root.appendChild(d); p.run && p.run(d); }); }

/* node-and-arrow stepper. nodes: {id,x,y,w,h,t,s,c(colour var),from}; edges: [a,b]; steps: {cap,on,e,set,msg:[x,y,text,colourVar]} */
function flow(el, o) {
  const N = Object.fromEntries(o.nodes.map((n) => [n.id, n]));
  const cx = (n, side) => side === "l" ? n.x : side === "r" ? n.x + n.w : n.x + n.w / 2;
  const cy = (n, side) => side === "t" ? n.y : side === "b" ? n.y + n.h : n.y + n.h / 2;
  o.steps.forEach((S) => { if (S.msg && typeof S.msg[0] !== "object") S.msg = [S.msg]; if (S.txt && typeof S.txt[0] !== "object") S.txt = [S.txt]; });
  let ys = o.nodes.flatMap((n) => [n.y, n.y + n.h]); o.steps.forEach((S) => { (S.msg || []).forEach((m) => ys.push(m[1] - 16, m[1] + 14)); (S.txt || []).forEach((m) => ys.push(m[1] - 14, m[1] + 6)); });
  const y0 = Math.min(...ys) - 18, hh = Math.max(...ys) - y0 + 18;
  const draw = (st) => {
    const k = Math.round(st.k), S = o.steps[k], on = S.on || [], eon = S.e || [];
    let out = "";
    o.edges.forEach((e, i) => {
      const a = N[e[0]], b = N[e[1]]; if ((a.from || 0) > k || (b.from || 0) > k) return;
      const horiz = Math.abs(cx(b) - cx(a)) >= Math.abs(cy(b) - cy(a)) && (b.x > a.x + a.w - 2 || b.x + b.w < a.x + 2);
      let x1, y1, x2, y2, dir;
      if (horiz) { const r = b.x > a.x; x1 = cx(a, r ? "r" : "l"); x2 = cx(b, r ? "l" : "r"); y1 = cy(a); y2 = cy(b); dir = r ? "r" : "l"; }
      else { const d = b.y > a.y; y1 = cy(a, d ? "b" : "t"); y2 = cy(b, d ? "t" : "b"); x1 = cx(a); x2 = cx(b); dir = d ? "d" : "u"; }
      const act = eon.includes(i), col = act ? "var(--accent)" : "var(--line)";
      out += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" style="stroke:${col};stroke-width:${act ? 4 : 2.5}${e[2] === "dash" ? ";stroke-dasharray:6 5" : ""}"/>` + SV.arrowHead(x2, y2, dir, "").replace('class=""', `style="fill:${col}"`);
    });
    o.nodes.forEach((n) => {
      if ((n.from || 0) > k) return;
      const act = on.includes(n.id), col = n.c || "var(--accent)", ov = (S.set || {})[n.id] || {}, t = ov.t != null ? ov.t : n.t, s = ov.s != null ? ov.s : n.s;
      out += `<rect x="${n.x}" y="${n.y}" width="${n.w}" height="${n.h}" rx="11" style="fill:${act ? "var(--accent-soft)" : "var(--surface)"};stroke:${act ? col : "var(--line)"};stroke-width:${act ? 3.5 : 2}"/>`;
      const lines = s ? (Array.isArray(s) ? s : [s]) : [];
      const y0 = n.y + (lines.length ? 22 : n.h / 2 + 5);
      out += `<text x="${n.x + n.w / 2}" y="${y0}" text-anchor="middle" class="lbl bd" style="fill:${act ? col : "var(--ink)"}">${t}</text>`;
      lines.forEach((l, i) => (out += `<text x="${n.x + n.w / 2}" y="${y0 + 19 + i * 17}" text-anchor="middle" class="sm" ${n.mono ? `style="${MONO}font-size:12px"` : ""}>${l}</text>`));
    });
    (S.msg || []).forEach((m) => { const w = 12 + m[2].length * 7.2; out += `<rect x="${m[0] - w / 2}" y="${m[1] - 14}" width="${w}" height="26" rx="13" style="fill:${m[3] || "var(--accent)"}"/><text x="${m[0]}" y="${m[1] + 4}" text-anchor="middle" class="lbl bd" style="fill:#fff;font-size:12px">${m[2]}</text>`; });
    (S.txt || []).forEach((m) => (out += `<text x="${m[0]}" y="${m[1]}" text-anchor="${m[4] || "middle"}" class="lbl bd" style="fill:${m[3] || "var(--ink)"}">${m[2]}</text>`));
    return `<g transform="translate(0,${-y0})">${out}</g>`;
  };
  Lib.stepper(el, { w: o.w || 760, h: hh, label: o.label, base: { k: 0 }, tween: 1, dwell: o.dwell || 4600, draw, steps: o.steps.map((s, i) => ({ cap: s.cap, s: { k: i } })) });
}

/* watch tab: [{h, spec}] */
function watch(list) { section("watch", [{ p: "Press Play, or click the numbered steps." }].concat(list.map((w) => ({ h: w.h, run: (d) => flow(d, w.spec) })))); }

/* practise tab: [{h, type, ...opts}] */
function practise(list) {
  section("practise", list.map((it) => ({ h: it.h, p: it.note, card: ["classify", "match", "order"].includes(it.type), run: (d) => {
    const t = it.type; if (t === "classify") Lib.classify(d, it); else if (t === "match") Lib.match(d, it); else if (t === "order") Lib.order(d, it); else if (t === "calc") Lib.calc(d, it); else if (t === "quiz") Lib.quiz(d, it);
  } })));
}

/* exam tab: items {cmd, m, q, tip, ans:[[cls,text],...], warn} */
function exam(list) {
  const root = $("#exam");
  root.innerHTML = `<h2>Exam-style questions</h2><p>Open each question for reminders, a model answer and a common mistake. Each underlined phrase earns one mark; the number shows which mark point it is.</p>` + list.map((x, i) => `<details class="eq"><summary>Q${i + 1} <span class="cmd">${x.cmd}</span> <span class="mark">${x.m} mark${x.m > 1 ? "s" : ""}</span> ${x.q}</summary><div class="body"><div class="tip"><b class="h">Reminder</b>${x.tip}</div><div class="ans">${x.ans.map((a, k) => `<span class="mk ${a[0]}" data-t="${k + 1}">${a[1]}</span>`).join(" ")}</div><div class="warn"><b class="h">Common mistake</b>${x.warn}</div></div></details>`).join("");
}

function real(list, intro) { $("#real").innerHTML = `<p class="note">${intro || "Descriptions are kept general. Check current details before quoting specifics."}</p>` + list.map((r) => `<div class="rw"><h3>${r[0]}</h3><p>${r[1]}</p><div class="use"><b>Exam use:</b> ${r[2]}</div></div>`).join(""); }

function tips(list, flash) {
  $("#tips").innerHTML = `<h2>Top tips</h2><ul class="tips">${list.map((t) => `<li>${t}</li>`).join("")}</ul><h2>Command words</h2><div class="tw"><table class="t"><tr><th>Command word</th><th>What it asks for</th></tr><tr><td>State / Name / Give</td><td>A short fact. No explanation.</td></tr><tr><td>Describe</td><td>What happens, step by step, or the main features.</td></tr><tr><td>Explain</td><td>What happens and why. Use because or so.</td></tr><tr><td>Compare</td><td>Similarities and differences, side by side.</td></tr></table></div><h2>Keyword flashcards</h2><div id="fc1"></div>`;
  Lib.cards($("#fc1"), { cards: flash });
}

const pick = (a) => a[Math.floor(Math.random() * a.length)];
const stateBtns = (el, items, cb) => { el.innerHTML = items.map((x, i) => `<button type="button" class="b" data-i="${i}">${x}</button>`).join(""); $$("button", el).forEach((b) => (b.onclick = () => { $$("button", el).forEach((x) => x.classList.remove("pri")); b.classList.add("pri"); cb(+b.dataset.i); })); };

/* ---------- Watch ---------- */
watch([
  { h: "1 · Printing a document", spec: { label: "The OS manages a print job", nodes: [
    { id: "a", x: 20, y: 100, w: 120, h: 70, t: "Application", s: "Print" },
    { id: "o", x: 190, y: 100, w: 130, h: 70, t: "Operating system", s: "hardware mgmt" },
    { id: "q", x: 370, y: 20, w: 120, h: 60, t: "Queue", s: "if printer busy", c: "var(--warn)" },
    { id: "b", x: 370, y: 130, w: 120, h: 60, t: "Buffer", s: "waiting data" },
    { id: "p", x: 560, y: 100, w: 150, h: 70, t: "Printer", s: "prints slowly", c: "var(--good)" },
  ], edges: [["a", "o"], ["o", "q"], ["o", "b"], ["q", "b"], ["b", "p"]], steps: [
    { cap: "The user presses Print in an application.", on: ["a"] },
    { cap: "The OS takes over <b>hardware peripheral management</b>. It finds and loads the <b>printer driver</b>.", on: ["a", "o"], e: [0] },
    { cap: "If the printer is busy, or the job has a low priority, the job waits in a <b>queue</b>.", on: ["o", "q"], e: [1] },
    { cap: "The data is sent to the printer <b>buffer</b>, a memory area holding it temporarily.", on: ["q", "b"], e: [2, 3] },
    { cap: "The buffer feeds the printer, and the OS sends control commands. Printing is much slower than the processor, so the processor can do other work.", on: ["b", "p"], e: [4] },
    { cap: "If the printer reports an error (such as a paper jam), the OS <b>receives and handles</b> the error message or interrupt.", on: ["p", "o"], msg: [365, 225, "error: paper jam", "var(--bad)"] },
  ] } },
  { h: "2 · Pre-emptive multitasking", spec: { label: "The CPU is shared between processes", nodes: [
    { id: "p1", x: 20, y: 20, w: 150, h: 54, t: "Spreadsheet" }, { id: "p2", x: 20, y: 90, w: 150, h: 54, t: "Email" },
    { id: "p3", x: 20, y: 160, w: 150, h: 54, t: "Web browser" }, { id: "p4", x: 20, y: 230, w: 150, h: 54, t: "Anti-virus", s: "low priority" },
    { id: "o", x: 290, y: 100, w: 190, h: 90, t: "Operating system", s: "monitors every process" }, { id: "c", x: 590, y: 100, w: 140, h: 90, t: "CPU", s: "one at a time", c: "var(--good)" },
  ], edges: [["p1", "o"], ["p2", "o"], ["p3", "o"], ["p4", "o"], ["o", "c"]], steps: [
    { cap: "Four processes are open. The OS monitors the status of each one so they do not clash.", on: ["o"] },
    { cap: "The spreadsheet is given the CPU for a <b>fixed time limit</b>.", on: ["p1", "o", "c"], e: [0, 4], msg: [535, 80, "time slice 1", "var(--accent)"] },
    { cap: "The time is up, so the OS <b>interrupts</b> the process. The email process gets its slice.", on: ["p2", "o", "c"], e: [1, 4], msg: [535, 80, "time slice 2", "var(--accent)"] },
    { cap: "The browser runs next. A process with a high priority may get more resources than another.", on: ["p3", "o", "c"], e: [2, 4], msg: [535, 80, "time slice 3", "var(--accent)"] },
    { cap: "The anti-virus has a <b>low priority</b>. If higher-priority work keeps arriving, it may be <b>starved</b> of CPU time. That is the risk of priorities.", on: ["p4"], e: [3], msg: [235, 255, "waits...", "var(--bad)"] },
  ] } },
]);

/* ---------- Lab 1: memory protection ---------- */
(() => {
  let ram; const reset = () => { ram = [..."A1A2A3A4A5A6B1B2B3B4B5B6".match(/../g)]; paint(); $("#mpV").textContent = "App A holds A1 to A6. App B holds B1 to B6."; };
  const paint = () => ($("#mpRam").innerHTML = ram.map((c, i) => `<div class="blk" style="background:${c.includes("!") ? "#b3372f" : c[0] === "A" ? "#2b5d7c" : "#a85d00"}">${c}</div>`).join(""));
  $("#mpGo").onclick = () => {
    if ($("#mpOn").checked) { $("#mpV").innerHTML = "✓ <b>Blocked.</b> The OS refuses: these locations belong to app A. B receives an error, and A's data stays safe."; return; }
    ram = ram.map((c, i) => (i >= 3 && i < 6 ? "B!" : c)); paint();
    $("#mpV").innerHTML = "✗ B has <b>overwritten</b> app A's data. A may now produce wrong results, or the computer could crash, and private data could end up where other software can reach it.";
  };
  $("#mpReset").onclick = reset; reset();
})();

/* ---------- Lab 2: multitasking ---------- */
(() => {
  const COL = ["#2b5d7c", "#a85d00", "#7a3fa0"]; let sl;
  const upd = () => {
    const mode = $("#msM").value, slice = sl ? sl.get() : 2, flood = $("#msFl").checked && mode === "pr"; $("#msF").style.display = mode === "pr" ? "" : "none"; $("#msS").style.display = mode === "rr" ? "" : "none";
    const need = [flood ? 1e9 : 8, 8, 8], fin = [null, null, null], line = []; let cur = 0, used = 0;
    for (let t = 1; t <= 30; t++) {
      const ready = [0, 1, 2].filter((i) => need[i] > 0); if (!ready.length) break; let p;
      if (mode === "pr") p = ready[0];
      else { if (!ready.includes(cur) || used >= slice) { const nxt = ready.find((i) => i > cur) ?? ready[0]; if (nxt !== cur || !ready.includes(cur)) cur = nxt; used = 0; } p = cur; used++; }
      need[p]--; line.push(p); if (need[p] === 0) fin[p] = t;
    }
    $("#msT").innerHTML = line.map((p, i) => `<div class="blk" style="background:${COL[p]};width:28px;height:28px" title="unit ${i + 1}">P${p + 1}</div>`).join("");
    [0, 1, 2].forEach((i) => ($("#mf" + (i + 1)).textContent = fin[i] ? "unit " + fin[i] : i === 0 && flood ? "never" : "not yet"));
    $("#msV").innerHTML = mode === "rr" ? `Everyone takes turns, so each process makes steady progress. A shorter time slice switches more often, so the user feels everything is running at once.` : flood ? "<b>P2 and P3 are starved.</b> Higher-priority work keeps arriving, so the low-priority processes never get the CPU. That is the risk of priority scheduling." : "P1 runs first, then P2, then P3. The high-priority process finishes fast, but the low-priority one has to wait for all the others.";
  };
  sl = Lib.slider($("#msS"), { id: "msSl", label: "Time slice (units)", min: 1, max: 4, value: 2, onInput: upd });
  $("#msM").onchange = upd; $("#msFl").onchange = upd; upd();
})();

/* ---------- Lab 3: CLI or GUI ---------- */
(() => {
  const Q = [
    ["A technician needs to alter computer configuration settings and find an error.", 0, "CLI: direct communication with the computer and not restricted to pre-set options. Technicians and programmers use it."],
    ["A young child wants to open a drawing app and play a game.", 1, "GUI: icons need no commands to learn, so it is user-friendly."],
    ["A tiny embedded computer has very little memory.", 0, "CLI: it uses a small amount of memory, whereas a GUI uses considerably more."],
    ["A shopper wants to launch a banking app on a phone with a touch screen.", 1, "GUI: tap the icon. Nothing needs to be typed."],
    ["A programmer wants to start a memory dump to find an error.", 0, "CLI: used by programmers and analysts who need direct communication."],
  ];
  const el = $("#ifc"); let i = 0, score = 0;
  const draw = () => { if (i >= Q.length) { el.innerHTML = `<p><b>Done. Score ${score} / ${Q.length}.</b></p><button class="b" id="ifr">Try again</button>`; $("#ifr").onclick = () => { i = score = 0; draw(); }; return; }
    el.innerHTML = `<p><b>${i + 1}.</b> ${Q[i][0]}</p><div class="ch"><button data-a="0">Command line interface (CLI)</button><button data-a="1">Graphical user interface (GUI)</button></div><div class="verdict" id="ifv" hidden></div>`;
    $$("button", el).forEach((b) => (b.onclick = () => { const ok = +b.dataset.a === Q[i][1]; $$(".ch button", el).forEach((x) => (x.disabled = true)); b.classList.add(ok ? "ok" : "no"); if (ok) score++; const v = $("#ifv"); v.hidden = false; v.innerHTML = (ok ? "✓ " : "✗ ") + Q[i][2] + `<br><button class="b" id="ifn" style="margin-top:8px">Next</button>`; $("#ifn").onclick = () => { i++; draw(); }; })); };
  draw();
})();

/* ---------- Practise ---------- */
practise([
  { h: "1 · CLI or GUI?", type: "classify", prompt: "Drag each statement to the interface it describes.", buckets: [{ label: "CLI" }, { label: "GUI" }], items: [
    { text: "The user types commands", b: 0 }, { text: "Not limited to pre-determined options", b: 0 }, { text: "Uses a small amount of memory", b: 0 }, { text: "Commands must be spelled correctly", b: 0},
    { text: "Uses icons, menus and windows", b: 1 }, { text: "No commands to learn", b: 1 }, { text: "Uses considerably more memory", b: 1 }, { text: "Suits the ordinary end-user", b: 1 },
  ], done: "Type for control, click for ease." },
  { h: "2 · Match the OS function", type: "match", prompt: "Match each function to its description.", pairs: [
    ["Memory management", "Keeps track of RAM and stops two applications using the same locations"], ["Security management", "Updates, firewall links, passwords and access rights"],
    ["Hardware peripheral management", "Uses drivers, queues and buffers to run input and output devices"], ["File management", "Create, open, copy, rename and delete files; maintains directories"],
    ["Multitasking", "Shares the CPU between several processes at once"], ["Management of user accounts", "Separate settings and files for each user, controlled by an administrator"],
  ] },
  { h: "3 · Printing a document", type: "order", prompt: "Put the printing steps in order.", items: [
    "The printer driver is located and loaded", "Data is sent to the printer buffer (or the queue if busy)", "The OS sends control commands to the printer", "The printer prints from the buffer", "Any printer errors are received and handled",
  ], done: "Driver, buffer, commands, print, handle errors." },
  { h: "4 · Multiple choice", type: "quiz", qs: [
    { q: "What does memory protection prevent?", opts: ["Two applications using the same memory locations at the same time", "Files being deleted", "The CPU overheating", "Passwords being forgotten"], a: 0, why: "Otherwise data could be lost, results wrong or the computer could crash." },
    { q: "Who would most likely use a CLI?", opts: ["A programmer", "A young child", "A shopper using a phone", "A tourist with a map app"], a: 0, why: "Programmers and technicians need direct communication with the computer." },
    { q: "In pre-emptive multitasking, what can happen to a low-priority process?", opts: ["It is starved of resources", "It always runs first", "It is deleted", "It becomes a GUI"], a: 0, why: "Higher-priority processes may take the resources." },
    { q: "What does WIMP stand for?", opts: ["Windows, icons, menu, pointing device", "Write, input, memory, process", "Wide input management protocol", "Windows, internet, mouse, printer"], a: 0, why: "It describes a typical GUI on a PC." },
    { q: "Which function stores the printer buffer and queue?", opts: ["Hardware peripheral management", "File management", "Security management", "Screen saving"], a: 0, why: "The OS controls queues and buffers for input and output devices." },
  ] },
]);

real([
  ["Windows, macOS, Android and iOS", "Every phone, tablet and laptop runs an OS. Android and iOS are the main ones on phones, and each one handles the interface, memory, files and security for apps.", "Name real examples of operating systems."],
  ["Switching between apps on your phone", "You can listen to music, receive a message and have a map open all at once. The OS shares the processor's time between them in very small slices, so it feels simultaneous.", "A practical example of multitasking."],
  ["School network log-ins", "Each student logs in with a user name and password and sees their own files. Teachers have wider access levels. An administrator creates and removes accounts.", "Management of user accounts and multi-access levels."],
  ["The print queue in an office", "Many people send jobs to one printer. The OS holds them in a queue, and a job with a higher priority may be printed first.", "Queues, buffers and priorities in hardware management."],
  ["A command prompt for IT staff", "Technicians sometimes type commands to check a network connection or change a setting that no icon offers.", "Why some users prefer a CLI."],
]);

exam([
  { cmd: "Describe", m: 4, q: "Choose <b>four</b> functions of an operating system and describe each.", tip: "Name the function, then say what it does. One mark each.", ans: [["k", "Memory management: keeps track of RAM and moves data between RAM and storage."], ["k", "Security management: controls log-ins, access rights and links with a firewall."], ["k", "File management: allows files to be created, opened, copied, renamed and deleted, and keeps directories."], ["k", "Multitasking: shares the processor so more than one process runs at a time."]], warn: "Naming a function without saying what it does." },
  { cmd: "Describe", m: 4, q: "Describe two differences between a CLI and a GUI.", tip: "Make a comparison for each difference.", ans: [["k", "A CLI needs commands to be typed, whereas a GUI uses icons and menus."], ["k", "A CLI must be typed in the correct format and spelling,"], ["k", "so a GUI is easier for a beginner."], ["k", "A GUI needs more memory than a CLI."]], warn: "Saying a GUI is \"better\". Give a reason." },
  { cmd: "State", m: 2, q: "Give one type of user who would use a CLI and explain why.", tip: "A user type plus a reason.", ans: [["k", "A programmer or technician,"], ["k", "because they need direct communication with the computer and are not restricted to pre-set options."]], warn: "Naming an end-user." },
  { cmd: "Explain", m: 3, q: "Explain why memory protection is needed.", tip: "Two competing applications, then the effects.", ans: [["k", "Without it two applications could use the same memory locations at the same time."], ["k", "Data could be lost or the applications could give incorrect results."], ["k", "In extreme cases, the computer could crash (or private data could be exposed)."]], warn: "Describing RAM only." },
  { cmd: "Describe", m: 4, q: "Describe how the operating system manages the printing of a document.", tip: "Driver, buffer or queue, commands, errors.", ans: [["k", "The printer driver is found and loaded."], ["k", "The data is sent to the printer buffer, or to a queue if the printer is busy or the job has a low priority."], ["k", "Control commands are sent to the printer during printing."], ["k", "The OS receives and handles error messages and interrupts from the printer."]], warn: "Forgetting the queue. It is separate from the buffer." },
  { cmd: "Explain", m: 3, q: "Explain how multitasking works and one risk for a low-priority process.", tip: "Share resources, time limits, starvation.", ans: [["k", "Several processes share the hardware resources under control of the OS."], ["k", "Each process is given resources for a time limit and can be interrupted."], ["e", "A low-priority process may be starved of resources if higher-priority processes keep taking them."]], warn: "Saying the CPU does many things at exactly the same moment." },
  { cmd: "Describe", m: 3, q: "Describe how the operating system manages user accounts on a school network.", tip: "Log-in, separate files, administrator.", ans: [["k", "Each user has a user name and password to log on."], ["k", "Each user has their own settings, folders and files, stored separately."], ["k", "An administrator can create, delete or restrict accounts, and different access levels can limit what each user sees."]], warn: "Writing about passwords only." },
]);

tips([
  "<b>Name the function, then say what it does.</b> A bare list of function names earns nothing.",
  "<b>CLI = type. GUI = click.</b> Then add a reason from the table: memory, ease, flexibility.",
  "<b>Match the user to the interface:</b> programmers and technicians use CLI, end-users use GUI.",
  "<b>Memory protection stops clashes</b> between applications. Say what could go wrong: lost data, wrong results, crash.",
  "<b>Buffer and queue are different.</b> A queue holds waiting jobs. A buffer holds data on its way to a slow device.",
  "<b>Multitasking is time-sharing.</b> Processes take very small turns. Say \"may be starved\" for low priority.",
  "<b>Security aims:</b> integrity, confidentiality (privacy) and availability of data.",
  "<b>Use the key words:</b> driver, buffer, queue, priority, process, access rights, administrator.",
], [
  ["Operating system (OS)", "Software that provides the platform for applications and a usable interface between human and computer."], ["Human computer interface (HCI)", "How the user communicates with the computer: a CLI or a GUI."],
  ["Command line interface (CLI)", "An interface where the user types in commands."], ["Graphical user interface (GUI)", "An interface that uses icons, windows and menus."],
  ["WIMP", "Windows, icons, menu and pointing device."], ["Memory management", "Managing RAM and tracking memory locations, including memory protection."],
  ["Memory protection", "Making sure two applications cannot use the same memory locations at the same time."], ["Buffer", "A memory area that stores data temporarily."],
  ["Queue", "A list of jobs waiting for a device, such as a printer."], ["Multitasking", "Carrying out more than one process at a time by sharing hardware resources."],
  ["Pre-emptive multitasking", "Processes get resources for a time limit, can be interrupted and have priorities."], ["Starved", "A low-priority process that never gets resources because higher priority ones keep taking them."],
  ["Access rights", "What each user is allowed to see or do on a computer or file."], ["Administrator", "The person who creates, deletes and restricts user accounts."],
]);
