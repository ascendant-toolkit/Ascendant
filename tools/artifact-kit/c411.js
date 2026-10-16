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
  { h: "1 · Saving a file: who does what?", spec: { label: "Layers of software between the user and the hardware", h: 330, nodes: [
    { id: "u", x: 20, y: 120, w: 110, h: 70, t: "User", s: "clicks Save" },
    { id: "a", x: 175, y: 120, w: 140, h: 70, t: "Application", s: "word processor" },
    { id: "o", x: 360, y: 120, w: 140, h: 70, t: "Operating system", s: "file management" },
    { id: "d", x: 545, y: 120, w: 90, h: 70, t: "Driver", s: "SSD driver" },
    { id: "h", x: 660, y: 120, w: 90, h: 70, t: "Hardware", s: "SSD", c: "var(--good)" },
  ], edges: [["u", "a"], ["a", "o"], ["o", "d"], ["d", "h"]], steps: [
    { cap: "The user is working in an <b>application</b>. Application software does a specific job: here, writing a document.", on: ["u", "a"] },
    { cap: "The user clicks Save. The application does not write to the disk itself. It <b>asks the operating system</b>.", on: ["a", "o"], e: [1], msg: [250, 215, "save request", "var(--accent)"] },
    { cap: "The <b>operating system</b> (system software) deals with <b>file management</b>: it chooses a file name, a location and free space.", on: ["o"] },
    { cap: "The OS passes the data to the <b>device driver</b>, which translates it into a form the SSD understands.", on: ["o", "d"], e: [2] },
    { cap: "The driver talks to the <b>hardware</b>, and the file is stored. Without the driver, the device would be \"not recognised\".", on: ["d", "h"], e: [3] },
  ] } },
  { h: "2 · Plugging in a USB memory stick", spec: { label: "The operating system looks for a driver", h: 300, nodes: [
    { id: "s", x: 20, y: 90, w: 150, h: 80, t: "USB memory stick", s: ["VID, PID,", "serial number"], c: "var(--good)" },
    { id: "o", x: 300, y: 90, w: 160, h: 80, t: "Operating system", s: "looks for a driver" },
    { id: "d", x: 590, y: 20, w: 150, h: 70, t: "Driver found", s: "device works", c: "var(--good)", from: 3 },
    { id: "x", x: 590, y: 130, w: 150, h: 70, t: "No driver", s: "\"device not recognised\"", c: "var(--bad)", from: 4 },
  ], edges: [["s", "o"], ["o", "d"], ["o", "x"]], steps: [
    { cap: "A memory stick is plugged into a USB port.", on: ["s"] },
    { cap: "The OS asks the new device what it is. The device replies with its <b>descriptors</b>: vendor ID, product ID and a unique serial number.", on: ["s", "o"], e: [0], msg: [235, 75, "descriptors", "var(--accent)"] },
    { cap: "The OS uses the descriptors to look for the right <b>device driver</b>.", on: ["o"] },
    { cap: "Driver found: the OS loads it and the stick works. Because it has a serial number, the OS also recognises the <i>same</i> stick next time.", on: ["o", "d"], e: [1] },
    { cap: "No driver found: the OS cannot translate data for the device, so an error message such as \"device not recognised\" appears.", on: ["o", "x"], e: [2] },
  ] } },
]);

/* ---------- Lab 1: defragmentation ---------- */
(() => {
  const COL = { A: "#2b5d7c", B: "#a85d00", C: "#7a3fa0" };
  let disk;
  const start = () => { disk = [..."AA..BB.AAB.CC.AB..CCC.B."].map((c) => (c === "." ? null : c)); };
  const frags = (f) => { let n = 0; disk.forEach((c, i) => { if (c === f && disk[i - 1] !== f) n++; }); return n; };
  function paint(msg) {
    $("#dfd").innerHTML = disk.map((c) => `<div class="blk ${c ? "" : "e"}" style="${c ? "background:" + COL[c] : ""}">${c || "·"}</div>`).join("");
    const a = frags("A"), b = frags("B"), c = frags("C");
    $("#dfa").textContent = a; $("#dfbn").textContent = b; $("#dfc").textContent = c; $("#dft").textContent = a + b + c;
    $("#dfv").innerHTML = msg || (a + b + c <= 3 ? "Each file is in one piece (<b>contiguous</b>): the head moves once per file." : `The files are scattered, so the head needs <b>${a + b + c}</b> separate movements to read all three. That is slow on an HDD.`);
  }
  const extend = (f) => { let n = 2; disk = disk.map((c) => (c === null && n > 0 ? (n--, f) : c)); paint(); };
  const del = (f) => { disk = disk.map((c) => (c === f ? null : c)); paint(`File ${f} deleted. Its blocks are now free gaps, and the other files stay where they were.`); };
  const defrag = () => { const order = ["A", "B", "C"].flatMap((f) => disk.filter((c) => c === f)); disk = order.concat(Array(disk.length - order.length).fill(null)); paint("Defragmented: each file now sits in <b>contiguous</b> blocks and the free space is together. Fewer head movements means faster access."); };
  const bs = $("#dfb");
  [["Delete file B", () => del("B")], ["Extend file A (+2)", () => extend("A")], ["Extend file C (+2)", () => extend("C")], ["Defragment", defrag], ["Reset", () => { start(); paint(); }]].forEach(([t, f], i) => { const b = mk("button", "b" + (i === 3 ? " pri" : ""), t); b.onclick = f; bs.appendChild(b); });
  start(); paint();
})();

/* ---------- Lab 2: back-up ---------- */
(() => {
  const local = $("#bk1"), remote = $("#bk2"), v = $("#bkv");
  const D = [
    ["Hard drive fails", (l, r) => ({ ok: l || r, t: `The working copy is gone. ${l || r ? "You can <b>restore</b> it from " + (l ? "the local back-up" : "the remote back-up") + "." : "With no back-up, the file is <b>lost</b>."}` })],
    ["Burglary or fire at home", (l, r) => ({ ok: r, t: `The computer <b>and</b> the local back-up are both gone. ${r ? "The <b>remote</b> copy, stored well away from the computer, survives." : "Every copy was in the same place, so the file is <b>lost</b>."}` })],
    ["File overwritten by mistake", (l, r) => ({ ok: l || r, t: l || r ? "Back-up software that keeps older versions or a <b>restore point</b> lets you go back to the earlier version." : "No earlier version exists, so the file cannot be recovered." })],
  ];
  const bs = $("#bkb");
  D.forEach(([t, f]) => { const b = mk("button", "b", t); b.onclick = () => { const r = f(local.checked, remote.checked); v.innerHTML = (r.ok ? "✓ " : "✗ ") + r.t; v.style.background = r.ok ? "var(--good-soft)" : "var(--bad-soft)"; v.style.borderColor = r.ok ? "var(--good)" : "var(--bad)"; }; bs.appendChild(b); });
})();

/* ---------- Lab 3: anti-virus ---------- */
(() => {
  const F = [
    ["invoice.exe", "A virus already in the database", { virus: 1, db: 1 }],
    ["game_crack.exe", "A brand new virus: copies itself and edits system files", { virus: 1, behaviour: 1 }],
    ["holiday.jpg", "A harmless photo", {}],
    ["disk_tool.exe", "A harmless tool that edits lots of system files (looks suspicious)", { behaviour: 1, clean: 1 }],
    ["old_report.dll", "A virus sleeping inside a file that is never opened. It is in the database only after an update", { virus: 1, dormant: 1, newdb: 1 }],
  ];
  $("#avt").innerHTML = `<tr><th>File</th><th>What it really is</th><th>Result</th></tr>` + F.map((f, i) => `<tr><td><code>${f[0]}</code></td><td>${f[1]}</td><td id="avr${i}">not scanned</td></tr>`).join("");
  $("#avs").onclick = () => {
    const upd = $("#avu").checked, heu = $("#avh").checked, full = $("#avf").checked; let miss = 0, fp = 0, caught = 0;
    F.forEach((f, i) => {
      const o = f[2], seen = !o.dormant || full, inDb = o.db || (o.newdb && upd), hit = seen && (inDb || (heu && o.behaviour));
      let r;
      if (hit && o.virus) { r = `<span class="pos">Quarantined</span> ${inDb ? "(matched the database)" : "(found by heuristic checking)"}`; caught++; }
      else if (hit) { r = `<span class="neg">False positive</span>: a clean file was quarantined`; fp++; }
      else if (o.virus) { r = `<span class="neg">Missed</span> ${!seen ? "(never scanned: dormant)" : "(not in database, no heuristics)"}`; miss++; }
      else r = "Clean";
      $("#avr" + i).innerHTML = r;
    });
    $("#avv").innerHTML = `Caught ${caught} of 3 viruses · missed ${miss} · false positives ${fp}. ` + (miss ? "Turn on updates, heuristics and a full scan to catch more." : fp ? "Heuristic checking can flag clean files. The user can check quarantined files before deleting them." : "Every virus caught, with no false alarms.");
  };
})();

/* ---------- Practise ---------- */
practise([
  { h: "1 · System or application software?", type: "classify", prompt: "Drag each program to the correct type of software.", buckets: [{ label: "System software" }, { label: "Application software" }], items: [
    { text: "Screensaver", b: 0 }, { text: "Anti-virus software", b: 0 }, { text: "Printer driver", b: 0 }, { text: "Compiler", b: 0 }, { text: "Operating system", b: 0 },
    { text: "Control and measuring software", b: 1 }, { text: "Video editing software", b: 1 }, { text: "QR code reader", b: 1 }, { text: "On-screen calculator", b: 1 },
  ], done: "Software that runs the computer is system software; software that does the user's job is application software." },
  { h: "2 · Match the utility to its job", type: "match", prompt: "Match each utility to what it does.", pairs: [
    ["Anti-virus", "Compares files with a database of known viruses and checks their behaviour"], ["Defragmenter", "Rearranges file blocks on an HDD so each file is contiguous"],
    ["Back-up software", "Makes copies of files so they can be restored later"], ["Security software", "Manages user accounts, firewalls and encryption"],
    ["Screensaver", "Shows an image after inactivity and can lock the computer"], ["Device driver", "Translates data into a format a hardware device understands"],
  ] },
  { h: "3 · How anti-virus deals with a file", type: "order", prompt: "Put these steps in the right order.", items: [
    "The file is checked before it is run or loaded", "It is compared with the database of known viruses", "Heuristic checking looks at what the file would do", "A suspect file is put into quarantine", "The file is deleted, or the user decides what to do with it",
  ], done: "Check, compare, heuristics, quarantine, delete." },
  { h: "4 · Quick checks", type: "calc", qs: [
    { q: "Three versions of a file are recommended for total security: the working copy, a local back-up and a remote back-up. How many copies is that in total?", a: 3, sol: "Working copy + local back-up + remote back-up = 3." },
    { q: "File X is stored in 5 separate pieces and file Y in 3 separate pieces. How many head jumps are needed to read both?", a: 8, sol: "5 + 3 = 8 separate pieces to find.", hint: "One jump for each separate piece." },
    { q: "After defragmentation, each of those two files is contiguous. How many head jumps are needed now?", a: 2, sol: "One jump for each file: 2." },
  ] },
  { h: "5 · Multiple choice", type: "quiz", qs: [
    { q: "Which is an example of system software?", opts: ["Spreadsheet", "Device driver", "Photo editor", "Web game"], a: 1, why: "A device driver helps the OS communicate with hardware." },
    { q: "Why does defragmentation speed up an HDD?", opts: ["It deletes old files", "It puts each file's blocks next to each other, so the head moves less", "It increases the RAM", "It compresses the files"], a: 1, why: "Contiguous blocks mean fewer read-write head movements." },
    { q: "What is a false positive in anti-virus software?", opts: ["A virus that is missed", "A clean file flagged as a virus", "A virus that is deleted", "A backed-up file"], a: 1, why: "The software wrongly identifies a harmless file as infected." },
    { q: "Why is heuristic checking useful?", opts: ["It can spot a new virus that is not yet in the database", "It makes the database smaller", "It stops all false positives", "It defragments the disk"], a: 0, why: "It looks at behaviour rather than matching a known virus." },
    { q: "Which of these is a USB descriptor?", opts: ["Vendor ID", "Cursor position", "Window title", "File extension"], a: 0, why: "Descriptors are the vendor ID, product ID and serial number." },
    { q: "How can a screensaver help security?", opts: ["It encrypts the hard drive", "It locks the computer after inactivity", "It scans emails", "It speeds up the CPU"], a: 1, why: "After a period of inactivity the user can be logged out and the screen locked." },
  ] },
]);

/* ---------- Real world ---------- */
real([
  ["Windows File History and Mac Time Machine", "Both are back-up utilities. Windows File History takes snapshots of files to an external drive, by default every hour. Mac Time Machine backs up every hour, keeps daily back-ups for the past month and weekly back-ups after that, and deletes the oldest when the drive fills.", "Examples of a scheduled back-up utility that can restore earlier versions."],
  ["Anti-virus on a phone", "Phones and tablets can catch malware too. Many security apps scan downloads before they open and keep their virus lists up to date in the background.", "Shows that anti-virus checks files before they run and needs regular updates."],
  ["Why your printer \"just works\"", "When you plug in a common printer, the operating system often finds and installs the driver on its own. If it cannot, you see an error and have to download the driver yourself.", "A concrete example of a device driver translating data for a peripheral."],
  ["The school computer that locks itself", "Computers in an office or school lock after a few minutes idle. This is the screensaver doubling as a security feature, so a passer-by cannot use a logged-in machine.", "A standard example for how a screensaver adds security."],
  ["Garden and factory control systems", "A greenhouse can use control and measuring software: a sensor reads the temperature, the software compares it with the stored target, and a signal switches the heater or opens a vent.", "Control and measuring software is an application that uses sensors, stored data and output signals."],
]);

/* ---------- Exam ---------- */
exam([
  { cmd: "State", m: 2, q: "Give <b>two</b> differences between system software and application software.", tip: "Say what each is <b>for</b>.", ans: [["k", "System software manages and controls the hardware and provides a platform for other software to run on,"], ["k", "whereas application software allows the user to carry out a specific task (such as writing a document)."]], warn: "Listing examples only. A difference needs a statement about purpose." },
  { cmd: "State", m: 4, q: "Name <b>two</b> examples of system software and <b>two</b> examples of application software.", tip: "Name the program type, not a product brand.", ans: [["k", "System: operating system"], ["k", "System: utility program / device driver / compiler"], ["k", "Application: word processor / spreadsheet"], ["k", "Application: photo editing / database / video editing"]], warn: "Putting a screensaver or anti-virus under application software. Both are system (utility) software." },
  { cmd: "Describe", m: 4, q: "Describe how anti-virus software protects a computer.", tip: "Checking, comparing, behaviour, quarantine.", ans: [["k", "It checks software and files before they are run or loaded."], ["k", "It compares them with a database of known viruses."], ["k", "Heuristic checking looks for behaviour that could indicate a virus, so a new virus can be found."], ["k", "Infected files are quarantined, and then deleted automatically or the user decides."]], warn: "Saying it \"stops all viruses\". It needs regular updates, and it can still miss new ones." },
  { cmd: "Explain", m: 3, q: "Explain why a hard disk drive may become slow to use, and how defragmentation helps.", tip: "Scattered blocks, more head movement, then the fix.", ans: [["k", "Files get deleted and extended over time, so their blocks become scattered over the disk."], ["k", "The read-write head may then need many movements to find all the blocks of one file, which slows access."], ["k", "Defragmentation rearranges the blocks so each file is stored in contiguous sectors, reducing head movement."]], warn: "Saying defragmentation \"frees up memory\" or \"deletes files\"." },
  { cmd: "Explain", m: 2, q: "Explain why defragmentation is not normally needed on a solid state drive.", tip: "What does an SSD not have?", ans: [["k", "An SSD has no moving read-write head,"], ["k", "so scattered blocks do not slow access in the same way."]], warn: "Confusing an SSD with RAM." },
  { cmd: "Describe", m: 3, q: "Describe how back-up software helps to keep data safe.", tip: "Schedule, changes only, restore, and where to keep the copies.", ans: [["k", "It can back up files automatically on a schedule."], ["k", "It can copy only files that have changed."], ["e", "Files can be restored after loss or corruption; storing a copy remotely (for example in the cloud) may protect against a fire or theft at the original site."]], warn: "Only saying \"it makes a copy\". Add how it is used or where the copy is kept." },
  { cmd: "Explain", m: 4, q: "Explain the purpose of a device driver, and the role of descriptors when a new USB device is plugged in.", tip: "Driver = translator. Descriptors = the device's ID.", ans: [["k", "A device driver communicates with the operating system and translates data into a format the device can understand."], ["k", "Without it the device may not work."], ["k", "Descriptors (vendor ID, product ID and serial number) let the computer identify what the device is,"], ["k", "so the operating system can find the correct driver."]], warn: "Saying a driver is \"hardware\". It is software." },
  { cmd: "Explain", m: 2, q: "Explain what is meant by a false positive in anti-virus software.", tip: "Clean file, wrongly flagged.", ans: [["k", "A file or program that is not infected"], ["k", "is wrongly identified as a virus (and may be quarantined)."]], warn: "Describing a missed virus. That is a false <b>negative</b>." },
]);

/* ---------- Tips and flashcards ---------- */
tips([
  "<b>System software runs the computer. Application software does the user's job.</b> Use those two ideas to answer almost any classification question.",
  "<b>Utilities are system software.</b> Anti-virus, defragmenter, back-up and screensavers are not applications.",
  "<b>Anti-virus has three habits:</b> check before running, compare with a database, check behaviour (heuristics). Add quarantine.",
  "<b>Defragmentation:</b> scattered blocks, many head movements, slow. Defragment, contiguous blocks, fewer movements, faster. HDD only.",
  "<b>Three copies:</b> working, local back-up, remote back-up. Say why remote matters: it survives a fire or theft at the original site.",
  "<b>A driver is a translator.</b> It turns the OS's data into something the device understands.",
  "<b>False positive means a clean file flagged.</b> Do not mix it up with a missed virus.",
  "<b>Screensavers can be security:</b> after inactivity they lock the screen or log the user out.",
], [
  ["System software", "Programs that control and manage the hardware and provide a platform for other software to run on."], ["Application software", "Programs that let a user do a specific task, such as writing a document."],
  ["Utility program", "System software that manages, maintains and controls computer resources, such as a virus checker or a defragmenter."], ["Malware", "Programs such as viruses, worms and Trojan horses installed with the aim of deleting, corrupting or manipulating data illegally."],
  ["Anti-virus software", "Software that quarantines and deletes files or programs infected by a virus."], ["Heuristic checking", "Checking software for behaviour that could indicate a possible virus."],
  ["Quarantine", "Isolating a file identified by anti-virus software as infected, in order to delete it later."], ["False positive", "A clean file that anti-virus software wrongly identifies as a virus."],
  ["Defragmentation", "Reorganising the sectors on an HDD so that each file's blocks are contiguous."], ["Contiguous", "Next to each other."],
  ["Back-up", "A copy of files made on another storage medium in case the original is corrupted or deleted."], ["Screensaver", "Software that shows a still or moving image when the computer has been inactive for a period of time."],
  ["Device driver", "Software that communicates with the operating system and translates data into a format a hardware device understands."], ["Descriptor", "Information (such as vendor ID, product ID and serial number) that a USB device gives the computer to identify itself."],
]);
