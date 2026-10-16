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
  { h: "1 · Booting up", spec: { label: "From power on to a running application", nodes: [
    { id: "pw", x: 20, y: 110, w: 100, h: 64, t: "Power on" },
    { id: "bi", x: 175, y: 110, w: 140, h: 64, t: "BIOS", s: "in EEPROM", c: "var(--warn)" },
    { id: "st", x: 370, y: 20, w: 150, h: 64, t: "Storage", s: "HDD / SSD holds the OS" },
    { id: "rm", x: 370, y: 190, w: 150, h: 64, t: "RAM", s: ["part of the OS"] , c: "var(--good)" },
    { id: "os", x: 580, y: 110, w: 150, h: 64, t: "Operating system", s: "running" , from: 4},
  ], edges: [["pw", "bi"], ["bi", "st"], ["st", "rm"], ["rm", "os"]], steps: [
    { cap: "The computer is switched on. The processor starts running the <b>BIOS</b>, which is firmware stored in EEPROM.", on: ["pw", "bi"], e: [0] },
    { cap: "The BIOS handles the start-up of the motherboard, then finds <b>where the storage device that holds the OS</b> is.", on: ["bi", "st"], e: [1] },
    { cap: "The part of the OS that is needed is read from the storage device (the <b>bootstrap loader</b> at work).", on: ["st", "rm"], e: [2], msg: [445, 135, "OS data", "var(--accent)"] },
    { cap: "It is now loaded into <b>RAM</b>, because the processor can only run programs that are in RAM.", on: ["rm"] },
    { cap: "The BIOS hands over and the OS is <b>executed</b>. The computer is booted, and applications can now run.", on: ["rm", "os"], e: [3] },
  ] } },
  { h: "2 · How the layers fit together", spec: { label: "An application request passes down through the layers", nodes: [
    { id: "a", x: 190, y: 20, w: 380, h: 52, t: "Application software", s: "" },
    { id: "o", x: 190, y: 100, w: 380, h: 52, t: "Operating system" },
    { id: "f", x: 190, y: 180, w: 380, h: 52, t: "Firmware (BIOS)", s: "", c: "var(--warn)" },
    { id: "h", x: 190, y: 260, w: 380, h: 52, t: "Hardware", s: "", c: "var(--good)" },
  ], edges: [["a", "o"], ["o", "f"], ["f", "h"]], steps: [
    { cap: "A user asks an application to do something, such as save a picture.", on: ["a"] },
    { cap: "The application depends on the <b>operating system</b> as its platform. It hands the request down.", on: ["a", "o"], e: [0] },
    { cap: "The OS uses <b>firmware</b> as the interface to the hardware, providing low-level control of the devices.", on: ["o", "f"], e: [1] },
    { cap: "The firmware drives the <b>hardware</b>, and the work is done. Remove any layer and the application cannot run.", on: ["f", "h"], e: [2] },
  ] } },
]);

/* ---------- Lab 1: BIOS / CMOS ---------- */
(() => {
  let st; const reset = () => { st = { ver: "1.0", clock: 3.0, bat: true }; paint("Start-up complete. The BIOS program is in EEPROM, and the settings are in CMOS."); };
  const paint = (m) => { $("#bEE").textContent = "BIOS program\nversion " + st.ver; $("#bCM").textContent = "Settings\nclock speed " + st.clock.toFixed(1) + " GHz\nbattery " + (st.bat ? "connected" : "REMOVED"); $("#bV").innerHTML = m; };
  const A = [
    ["Change clock speed to 4.0 GHz", () => { st.clock = 4.0; paint("The new setting is saved in the <b>CMOS</b>."); }],
    ["Switch off, then on", () => paint("Power is off. The EEPROM keeps the BIOS program, and the battery keeps the CMOS settings. Both are unchanged after switching on.")],
    ["Remove CMOS battery, then switch on", () => { st.bat = false; st.clock = 3.0; paint("The CMOS lost power, so the settings reset to the <b>factory defaults</b> (3.0 GHz). The BIOS program in EEPROM is unaffected, so the computer still starts."); }],
    ["Update the BIOS (rewrite EEPROM)", () => { st.ver = "2.0"; paint("EEPROM is flash memory, so the BIOS can be <b>rewritten or updated</b> (it can also be deleted)."); }],
    ["Reset", reset],
  ];
  A.forEach(([t, f]) => { const b = mk("button", "b", t); b.onclick = f; $("#bB").appendChild(b); }); reset();
})();

/* ---------- Lab 2: what is missing ---------- */
(() => {
  const ids = ["lHw", "lFw", "lOs", "lAp"], names = ["Hardware", "Firmware", "OS", "Application"], col = ["#1d7a4c", "#a85d00", "#2b5d7c", "#7a3fa0"];
  const upd = () => {
    const on = ids.map((i) => $("#" + i).checked);
    $("#lSt").innerHTML = names.map((n, i) => `<div class="blk" style="width:110px;background:${on[i] ? col[i] : "var(--soft)"};color:${on[i] ? "#fff" : "var(--muted)"}">${n}${on[i] ? "" : " ✗"}</div>`).join("");
    const [hw, fw, os, ap] = on; let m;
    if (!hw) m = "No hardware: there is nothing to run any software on.";
    else if (!fw) m = "No firmware: nothing tells the computer where the OS is or how to start, so it cannot boot.";
    else if (!os) m = "No operating system: the BIOS starts the hardware but has nothing to load. There is no platform, interface or file management.";
    else if (!ap) m = "No application: the computer boots, but there is nothing to do the user's task.";
    else m = "All four layers are present, so the application can run.";
    $("#lV").innerHTML = (on.every(Boolean) ? "✓ " : "✗ ") + m;
  };
  ids.forEach((i) => ($("#" + i).onchange = upd)); upd();
})();

/* ---------- Practise ---------- */
practise([
  { h: "1 · Match the term", type: "match", prompt: "Match each term to its description.", pairs: [
    ["Bootstrap loader", "Loads part of the OS into RAM when the computer starts"], ["BIOS", "Starts up the motherboard and finds the storage holding the OS"],
    ["Firmware", "A program giving low-level control of devices"], ["EEPROM", "Flash memory that holds the BIOS program when the power is off"],
    ["CMOS", "A chip that holds the BIOS settings, kept alive by a battery"], ["Booting up", "Loading the OS into RAM when the computer starts"],
  ] },
  { h: "2 · Where is it stored?", type: "classify", prompt: "Drag each item to where it is kept.", buckets: [{ label: "EEPROM" }, { label: "CMOS" }, { label: "HDD / SSD" }], items: [
    { text: "The BIOS program", b: 0 }, { text: "Can be rewritten or updated", b: 0 }, { text: "The clock speed setting", b: 1 }, { text: "Reset if the battery is removed", b: 1 },
    { text: "The operating system when switched off", b: 2 }, { text: "Application files", b: 2 },
  ], done: "Program in EEPROM, settings in CMOS, OS on the drive." },
  { h: "3 · Start-up order", type: "order", prompt: "Put the start-up steps in order.", items: [
    "The computer is switched on and the BIOS starts", "The BIOS finds the storage device holding the OS", "Part of the OS is loaded into RAM", "The OS is executed", "The user runs an application",
  ], done: "BIOS, find, load, execute, application." },
  { h: "4 · Multiple choice", type: "quiz", qs: [
    { q: "What does the BIOS do when a computer is switched on?", opts: ["Finds the storage device holding the OS and loads it", "Edits documents", "Deletes old files", "Updates the anti-virus"], a: 0, why: "It starts the motherboard and loads the needed part of the OS." },
    { q: "Why are the BIOS settings kept in CMOS?", opts: ["It stays powered by a battery, so settings are kept between starts", "It is a type of RAM that is cheap", "It is larger than the hard drive", "It runs the screen saver"], a: 0, why: "The CMOS is powered at all times from a rechargeable battery." },
    { q: "What happens to the BIOS settings if the CMOS battery is removed?", opts: ["They reset to the factory defaults", "The BIOS program is deleted", "The OS is uninstalled", "Nothing changes"], a: 0, why: "The settings revert to factory defaults. The BIOS program stays in EEPROM." },
    { q: "Which is described as firmware?", opts: ["BIOS", "A word processor", "A spreadsheet", "A web page"], a: 0, why: "Firmware gives low-level control for devices." },
    { q: "Why is the OS loaded into RAM?", opts: ["The processor runs programs that are in RAM", "RAM is permanent storage", "The HDD is too small", "To save power"], a: 0, why: "A program must be in main memory to be executed." },
  ] },
]);

real([
  ["Pressing a key at start-up to enter BIOS settings", "Many computers let you press a key as they start to reach a BIOS setup screen, where you can change settings such as the boot order or clock speed.", "Shows that the BIOS settings can be changed and are stored in CMOS."],
  ["The coin battery on a motherboard", "A small round battery on the motherboard keeps the CMOS powered. If it runs flat, an old computer may forget the date and time when it is switched off.", "A concrete picture of the CMOS battery and why it exists."],
  ["BIOS update from a manufacturer", "Manufacturers sometimes publish a BIOS update to fix problems or support new hardware. Because the BIOS lives in flash memory, it can be rewritten, but a failed update may stop the computer from starting.", "EEPROM can be rewritten, updated or even deleted."],
  ["Firmware in a washing machine or router", "Everyday devices have firmware too: small programs that control the hardware directly, with no full operating system.", "Firmware is a program providing low-level control for devices, including embedded systems."],
  ["\"Operating system not found\"", "This message appears when the BIOS cannot find an OS on the storage device it looks at. The hardware and firmware work, but there is nothing to load.", "Explains why the OS is needed in addition to hardware and firmware."],
], "Descriptions are kept general. Check current details before quoting specifics.");

exam([
  { cmd: "Describe", m: 2, q: "Describe what is meant by a BIOS and state its function.", tip: "What it is, then what it does.", ans: [["k", "The BIOS is firmware, a program that provides low-level control of the hardware (stored in EEPROM)."], ["k", "Its function is to start up the computer and load the operating system."]], warn: "Calling it \"hardware\"." },
  { cmd: "Describe", m: 3, q: "Describe the task of the BIOS when a computer is first switched on.", tip: "Start up, locate, load.", ans: [["k", "It handles the start-up of the motherboard."], ["k", "It tells the computer where the storage device holding the operating system is."], ["k", "It loads the part of the operating system that is needed into RAM and executes it."]], warn: "Saying the BIOS loads the application." },
  { cmd: "Explain", m: 4, q: "The BIOS program and the BIOS settings are stored in different types of memory. Describe each type and explain why both are used.", tip: "EEPROM for the program, CMOS for the settings.", ans: [["k", "The BIOS program is stored in EEPROM, flash memory whose contents remain when the power is off."], ["k", "The BIOS settings are stored on a CMOS chip."], ["k", "The CMOS is kept powered by a rechargeable battery, so the settings are kept."], ["k", "EEPROM can be rewritten/updated, but the settings need a separate memory so they can be changed and reset."]], warn: "Saying CMOS holds the BIOS program." },
  { cmd: "Explain", m: 2, q: "A computer's clock speed was changed in the BIOS. The CMOS battery is then removed and replaced. State what happens to the clock speed and explain why.", tip: "Factory default.", ans: [["k", "The clock speed returns to the factory default setting,"], ["k", "because the CMOS lost power and so lost the changed settings."]], warn: "Saying the BIOS program is deleted." },
  { cmd: "State", m: 2, q: "State what is meant by firmware.", tip: "Low level control.", ans: [["k", "A program that provides low-level control for devices"], ["k", "(for example the BIOS, which acts as an interface between the OS and the hardware)."]], warn: "Confusing firmware with application software." },
  { cmd: "Explain", m: 3, q: "Explain why hardware, firmware and an operating system are all needed to run an application.", tip: "One reason for each layer.", ans: [["k", "Hardware is needed to carry out the instructions."], ["k", "Firmware starts the computer and links the OS to the hardware."], ["k", "The operating system provides the platform on which the application can run."]], warn: "Leaving out the firmware." },
  { cmd: "Describe", m: 2, q: "What is meant by a bootstrap loader?", tip: "Loads the OS.", ans: [["k", "A small program that runs when the computer starts"], ["k", "and loads part of the operating system into RAM."]], warn: "Describing the BIOS settings." },
]);

tips([
  "<b>Three layers under every app:</b> hardware, firmware, operating system. Give a job for each.",
  "<b>The BIOS starts the computer.</b> It finds the OS and loads the needed part into RAM.",
  "<b>EEPROM = the program. CMOS = the settings.</b> The CMOS needs a battery to keep its settings.",
  "<b>Remove the battery:</b> settings go back to factory defaults. The BIOS program is not lost.",
  "<b>Booting up</b> means loading the OS into RAM. Do not say the \"computer turns on\" only.",
  "<b>Firmware</b> is a program (software), even though it is built into hardware.",
  "<b>Link it to RAM:</b> programs have to be in RAM before the processor can run them.",
  "<b>EEPROM details are beyond the syllabus.</b> Use them only to explain the BIOS.",
], [
  ["Booting up", "Loading part of the operating system into RAM when the computer starts."], ["Bootstrap loader", "The program that loads the OS into RAM at start-up."],
  ["BIOS", "Basic input/output system: firmware that starts the motherboard and finds the OS."], ["Firmware", "A program that provides low-level control for devices."],
  ["EEPROM", "Electrically erasable programmable ROM: flash memory that holds the BIOS program."], ["CMOS", "Complementary metal oxide semiconductor: a battery-powered chip holding BIOS settings."],
  ["Platform", "The environment (the OS) in which application software can run."], ["Factory default", "The original settings made when the device was built."],
]);
