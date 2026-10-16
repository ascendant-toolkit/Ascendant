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
  { h: "1 · Servicing an interrupt", spec: { label: "Save, run the ISR, restore, carry on", nodes: [
    { id: "t", x: 20, y: 110, w: 150, h: 70, t: "Current task", s: "PC = 105" },
    { id: "i", x: 230, y: 10, w: 150, h: 56, t: "Interrupt", s: "e.g. printer is empty", c: "var(--bad)" },
    { id: "s", x: 230, y: 110, w: 150, h: 70, t: "Save status", s: ["PC = 105", "registers"], c: "var(--warn)", from: 2 },
    { id: "r", x: 440, y: 110, w: 150, h: 70, t: "Run the ISR", s: "PC = ISR start address", from: 3 },
    { id: "b", x: 440, y: 230, w: 150, h: 60, t: "Restore status", s: "PC back to 105", c: "var(--good)", from: 4 },
  ], edges: [["i", "s"], ["t", "s"], ["s", "r"], ["r", "b"], ["b", "t"]], steps: [
    { cap: "The processor is running a task. The program counter shows the next instruction to fetch.", on: ["t"] },
    { cap: "A device sends an <b>interrupt signal</b>. The processor works out its <b>type</b> and <b>priority</b>.", on: ["t", "i"], e: [] },
    { cap: "The priority is high enough, so the processor <b>saves</b> the contents of the program counter and the other registers.", on: ["s"], e: [0, 1] },
    { cap: "The <b>start address of the ISR</b> (interrupt service routine) is loaded into the program counter, and the ISR runs.", on: ["s", "r"], e: [2] },
    { cap: "The interrupt is fully serviced. The saved registers are <b>restored</b>.", on: ["r", "b"], e: [3] },
    { cap: "The interrupted task carries on exactly where it left off.", on: ["b", "t"], e: [4] },
  ] } },
  { h: "2 · Printing with a buffer and interrupts", spec: { label: "The processor does other work while the printer prints", nodes: [
    { id: "m", x: 20, y: 90, w: 140, h: 70, t: "Memory", s: "document" },
    { id: "b", x: 250, y: 90, w: 140, h: 70, t: "Printer buffer", s: "temporary store" },
    { id: "p", x: 480, y: 90, w: 140, h: 70, t: "Printer", s: "slow", c: "var(--good)" },
    { id: "c", x: 250, y: 230, w: 140, h: 60, t: "Processor", s: "other tasks", c: "var(--warn)" },
  ], edges: [["m", "b"], ["b", "p"], ["p", "c", "dash"]], steps: [
    { cap: "The document is sent from memory to the <b>printer buffer</b>.", on: ["m", "b"], e: [0], msg: [205, 70, "data", "var(--accent)"] },
    { cap: "The buffer feeds the printer. Printing takes far longer than sending the data.", on: ["b", "p"], e: [1] },
    { cap: "Meanwhile the processor is <b>free to carry out other tasks</b>.", on: ["c"] },
    { cap: "When all the data in the buffer has been printed, the buffer is empty and an <b>interrupt</b> is sent to the processor.", on: ["p", "c"], e: [2], msg: [430, 215, "interrupt: more data!", "var(--bad)"] },
    { cap: "The current task is suspended while the interrupt is serviced, and more data is sent to the buffer.", on: ["m", "b", "c"], e: [0] },
  ] } },
]);

/* ---------- Lab 1: streaming ---------- */
(() => {
  let sd, sp, st;
  const upd = () => {
    if (!sd || !sp || !st) return;
    const dl = sd.get(), pl = sp.get(), th = st.get(); let buf = 0, playing = false, wait = null, freezes = 0, was = false; const pts = [];
    for (let t = 0; t <= 60; t++) {
      buf += dl;
      if (!playing && buf >= th) { playing = true; if (wait === null) wait = t; if (was) {} }
      if (playing) { if (buf >= pl) buf -= pl; else { playing = false; freezes++; } }
      pts.push(buf);
    }
    const mx = Math.max(10, ...pts), X = (t) => 30 + (t * 300) / 60, Y = (v) => 165 - (v * 140) / mx;
    $("#sbC").innerHTML = `<line x1="30" y1="165" x2="335" y2="165" class="ax" style="stroke:var(--line)"/><line x1="30" y1="15" x2="30" y2="165" style="stroke:var(--line)"/>` + `<polyline fill="none" stroke="var(--accent)" stroke-width="3" points="${pts.map((v, t) => X(t).toFixed(1) + "," + Y(v).toFixed(1)).join(" ")}"/><text x="34" y="26" class="sm">buffer level</text><text x="335" y="182" text-anchor="end" class="sm">time (60 seconds)</text>`;
    $("#sbF").textContent = freezes; $("#sbW").textContent = wait === null ? "never starts" : wait + " s";
    $("#sbV").innerHTML = dl >= pl ? `Data arrives <b>at least as fast</b> as it is played, so once the buffer has started to fill the video plays smoothly.` : `Data arrives <b>slower</b> than the player uses it, so the buffer keeps running empty and the video <b>freezes</b> ${freezes} time${freezes === 1 ? "" : "s"}. A bigger start-up buffer only delays the first freeze.`;
  };
  sd = Lib.slider($("#sbD"), { id: "sbd", label: "Download speed (units per second)", min: 1, max: 12, value: 6, onInput: upd });
  sp = Lib.slider($("#sbP"), { id: "sbp", label: "Playback rate (units per second)", min: 1, max: 10, value: 5, onInput: upd });
  st = Lib.slider($("#sbT"), { id: "sbt", label: "Buffer needed before play starts", min: 1, max: 60, value: 10, onInput: upd });
  upd();
})();

/* ---------- Lab 2: interrupts ---------- */
(() => {
  const PRI = 2; let pc;
  const ev = [["Key pressed", 2], ["Printer needs more data", 2], ["Timer signal", 1], ["Printer paper jam", 4], ["Division by zero", 3]];
  const L = $("#inL"), log = (t, c) => { L.insertAdjacentHTML("beforeend", `<div class="${c || ""}">${t}</div>`); L.scrollTop = L.scrollHeight; };
  const show = () => { $("#inPC").textContent = pc; $("#inSV").textContent = "-"; };
  const reset = () => { pc = 100; show(); L.innerHTML = ""; log("Program running at priority 2. PC = 100."); };
  $("#inS").onclick = () => { pc++; show(); log("Executed an instruction. PC = " + pc); };
  $("#inR").onclick = reset;
  ev.forEach(([t, p]) => { const b = mk("button", "b", `${t} (priority ${p})`); b.onclick = () => {
    log(`Interrupt: ${t}, priority ${p}.`, "hi");
    if (p < PRI) { log("Priority is lower than the running program, so it is <b>ignored for now</b> and handled later."); return; }
    $("#inSV").textContent = "PC = " + pc + ", registers";
    log("1. Save the PC (" + pc + ") and the other registers.");
    log("2. Load the ISR start address into the PC.");
    $("#inPC").textContent = "ISR";
    log("3. Run the interrupt service routine for: " + t + ".");
    log("4. Restore the saved registers. PC = " + pc + ".");
    $("#inPC").textContent = pc; log("The program carries on from where it stopped.", "gd");
  }; $("#inB").appendChild(b); });
  reset();
})();

/* ---------- Lab 3: printer ---------- */
(() => {
  let pd, pb;
  const upd = () => {
    if (!pd || !pb) return;
    const pages = pd.get(), buf = pb.get(), ints = Math.ceil(pages / buf), send = ints * 2, total = pages * 3, free = total - send;
    $("#prI").textContent = ints; $("#prS").textContent = send; $("#prF").textContent = free;
    $("#prV").innerHTML = `The printer buffer holds ${buf} page${buf > 1 ? "s" : ""}, so ${pages} pages need <b>${ints}</b> interrupt${ints > 1 ? "s" : ""}. In this simple model, each load of data takes the CPU 2 units to send, and printing takes 3 units a page. The CPU is free for other work for about <b>${free}</b> of the ${total} units. Without a buffer and interrupts it would have to wait for the whole print job.`;
  };
  pd = Lib.slider($("#prD"), { id: "prd", label: "Pages in the document", min: 1, max: 160, value: 160, onInput: upd });
  pb = Lib.slider($("#prB"), { id: "prb", label: "Pages the printer memory holds", min: 1, max: 40, value: 20, onInput: upd });
  upd();
})();

/* ---------- Practise ---------- */
practise([
  { h: "1 · What caused the interrupt?", type: "classify", prompt: "Drag each event to its type of cause.", buckets: [{ label: "Hardware" }, { label: "Software" }, { label: "User" }], items: [
    { text: "Paper jam in the printer", b: 0 }, { text: "Printer buffer is empty", b: 0 }, { text: "Disk drive needs more data", b: 0 },
    { text: "Divide by zero", b: 1 }, { text: ".exe file cannot be found", b: 1 }, { text: "Two processes use the same memory location", b: 1 },
    { text: "Ctrl-Alt-Break pressed", b: 2 }, { text: "A key pressed", b: 2 },
  ], done: "Hardware, software or user." },
  { h: "2 · Servicing an interrupt: the order", type: "order", prompt: "Put the steps in order.", items: [
    "An interrupt signal arrives and its type and priority are identified", "The program counter and registers of the current task are saved", "The start address of the ISR is loaded into the program counter", "The ISR runs", "The saved registers are restored and the task carries on",
  ], done: "Identify, save, load ISR address, run, restore." },
  { h: "3 · Match the term", type: "match", prompt: "Match each term to its description.", pairs: [
    ["Interrupt", "A signal to the processor to temporarily stop its current task"], ["ISR", "The routine run to deal with an interrupt"],
    ["Buffer", "A memory area that stores data temporarily"], ["Program counter", "Holds the address of the next instruction; saved when interrupted"],
    ["Priority", "Decides whether an interrupt is serviced straight away"],
  ] },
  { h: "4 · Calculations", type: "calc", qs: [
    { q: "A printer's memory holds 20 pages. How many times must it be refilled to print a 160-page document (so, how many interrupts)?", a: 8, sol: "160 ÷ 20 = 8.", hint: "Divide the pages by the pages held." },
    { q: "A printer holds 25 pages. How many interrupts are needed for 110 pages? (Round up.)", a: 5, sol: "110 ÷ 25 = 4.4, so 5 loads.", hint: "Any part load still needs an interrupt." },
  ] },
  { h: "5 · Multiple choice", type: "quiz", qs: [
    { q: "What does the processor save before it runs an ISR?", opts: ["The program counter and registers", "The whole hard drive", "The user's files", "The printer buffer"], a: 0, why: "So the interrupted task can carry on after the interrupt." },
    { q: "Why is a buffer used when streaming a video?", opts: ["To stop the video freezing when download speed and playback speed differ", "To make the video larger", "To encrypt it", "To delete old data"], a: 0, why: "The buffer stores data temporarily so playback can carry on smoothly." },
    { q: "Which could cause an interrupt?", opts: ["A hardware fault", "A fast processor", "Using a pen", "A new colour theme"], a: 0, why: "Faults, I/O, timers, user actions and software errors cause interrupts." },
    { q: "Why does a printer use a buffer and interrupts?", opts: ["So the processor can carry on with other tasks while printing", "So printing is faster than the processor", "So no data is needed", "So the printer needs no driver"], a: 0, why: "Printing is slow compared with the processor." },
  ] },
]);

real([
  ["Watching a film while a file downloads", "Your device shows the film, plays sound and downloads a file at once. Interrupts and buffers let each task have the processor in turn, so the user feels that they happen simultaneously.", "The textbook example of interrupts letting several functions co-exist."],
  ["The film that freezes", "When the connection is slow, the buffer runs empty, the film pauses and the screen shows a spinning circle until the buffer has refilled.", "Streaming needs the data rate into the buffer to exceed the playback rate."],
  ["Pressing Ctrl-Alt-Delete", "A key combination is an interrupt from the user. The system stops what it is doing so it can respond immediately.", "User interaction as a cause of an interrupt."],
  ["A printer reporting \"out of ink\"", "The printer sends an interrupt, the OS suspends the print job, and an error message is shown. When the ink is replaced the job carries on.", "A hardware-fault interrupt, and the OS handling it."],
  ["Typing while the computer is busy", "Each key press interrupts the processor. The key is held briefly in a buffer, so your letters appear even when the computer is busy.", "Interrupts and buffers working together."],
]);

exam([
  { cmd: "State", m: 2, q: "What is meant by an interrupt?", tip: "Signal, to the processor, stops.", ans: [["k", "A signal sent from a device or software to the microprocessor"], ["k", "which causes it to temporarily stop what it is doing so the interrupt can be serviced."]], warn: "Saying the computer \"crashes\"." },
  { cmd: "State", m: 3, q: "Give three causes of an interrupt.", tip: "Use the five types.", ans: [["k", "A timing signal / a hardware fault such as a paper jam"], ["k", "An input/output process (such as a disk drive needing data) / a user pressing a key"], ["k", "A software error (such as division by zero)"]], warn: "Giving three examples of the same type." },
  { cmd: "Describe", m: 4, q: "Describe how the processor deals with an interrupt.", tip: "Identify, save, ISR, restore.", ans: [["k", "The type and priority of the interrupt are identified."], ["k", "The contents of the program counter and the registers are saved."], ["k", "The start address of the interrupt service routine is loaded into the program counter and the ISR is run."], ["k", "The saved registers are restored and the interrupted task carries on."]], warn: "Forgetting to say the status is saved." },
  { cmd: "Explain", m: 2, q: "Mike is streaming a video. The data arrives from the internet more slowly than the media player needs it. What could stop the video freezing?", tip: "A memory area.", ans: [["k", "A buffer"], ["k", "that stores data temporarily so the media player has data while more arrives."]], warn: "Saying \"a faster processor\"." },
  { cmd: "Describe", m: 4, q: "While watching, Mike prints a 160-page document. The printer holds 20 pages at a time. Describe how interrupts allow both at once.", tip: "Buffer, other tasks, empty, interrupt.", ans: [["k", "20 pages are sent to the printer buffer."], ["k", "The processor can carry on with other tasks (such as the video) while the printer prints."], ["k", "When the buffer is empty, the printer sends an interrupt to request more data."], ["k", "The current task is paused while the interrupt is serviced (this happens 8 times)."]], warn: "Saying the processor prints the pages itself." },
  { cmd: "Describe", m: 2, q: "Describe what happens if the printer runs out of ink during the job.", tip: "Interrupt, error message.", ans: [["k", "The printer sends an interrupt (an error signal) to the processor/OS."], ["k", "The job is paused and an error message is displayed until the ink is replaced."]], warn: "Saying the document is deleted." },
  { cmd: "Explain", m: 3, q: "Explain why the use of buffers and interrupts helps the processor to be used efficiently.", tip: "Slow device, idle, other tasks.", ans: [["k", "A printer is much slower than the processor."], ["k", "Without buffers and interrupts the processor would be idle, waiting for the printer."], ["k", "With them the processor can carry out other tasks, increasing its processing power and speed."]], warn: "Mentioning only that \"it is faster\"." },
]);

tips([
  "<b>Interrupt = a signal that makes the processor pause.</b> Always say signal, processor, temporarily.",
  "<b>Know the five causes:</b> timer, input/output, hardware fault, user action, software error.",
  "<b>Servicing order:</b> identify type and priority, save PC and registers, run the ISR, restore, carry on.",
  "<b>Buffer = temporary store.</b> It evens out the speed difference between two devices.",
  "<b>Printing:</b> buffer empties, interrupt asks for more data, the processor suspends its task, then resumes.",
  "<b>Streaming:</b> data must come in faster than it is played, otherwise the video freezes.",
  "<b>Use numbers where you can:</b> 160 pages ÷ 20 pages = 8 interrupts.",
  "<b>Link to efficiency:</b> the processor is not left idle waiting for a slow device.",
], [
  ["Interrupt", "A signal from a device or software to the microprocessor, causing it to temporarily stop its current task."], ["Interrupt priority", "How urgent an interrupt is, which decides whether it is serviced straight away."],
  ["Interrupt service routine (ISR)", "The routine that is run to deal with an interrupt."], ["Program counter (PC)", "A register holding the address of the next instruction to be fetched."],
  ["Buffer", "A memory area that stores data temporarily."], ["Printer buffer", "Memory in or for the printer that holds data waiting to be printed."],
  ["Register", "A small fast store inside the processor."], ["Streaming", "Playing data (such as a movie) while it is still being downloaded."],
]);
