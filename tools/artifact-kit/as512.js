const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

const bin = (n, w = 8) => n.toString(2).padStart(w, "0");
const hx = (n, w = 2) => n.toString(16).toUpperCase().padStart(w, "0");
const grp4 = (s) => s.replace(/(.{4})(?=.)/g, "$1 ");
const clamp01 = (v) => Math.max(0, Math.min(1, v));
/* row of boxes: items [{t, c, v}] t text, c fill class, v opacity */
function boxRow(items, x0, y, w = 64, h = 52, gap = 10, o = {}) {
  let s = "";
  items.forEach((it, i) => {
    const x = x0 + i * (w + gap), v = it.v === undefined ? 1 : it.v;
    if (v <= 0) return;
    s += SV.rect(x, y, w, h, it.c || "f3", { rx: 8, ...op(v * (it.c ? 0.55 : 0.18)) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) });
    s += SV.text(x + w / 2, y + h / 2 + 8, it.t, "lbl bd", { "text-anchor": "middle", style: "font-size:" + (o.fs || 22) + "px;font-family:var(--mono)", ...op(v) });
    if (it.top !== undefined) s += SV.text(x + w / 2, y - 8, it.top, "sm", { "text-anchor": "middle", ...op(v) });
    if (it.bot !== undefined) s += SV.text(x + w / 2, y + h + 18, it.bot, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return s;
}

/* memory cell: address on the left, value in the box */
function memCell(x, y, addr, val, cls = "f3", v = 1, w = 150, h = 40) {
  return SV.rect(x, y, w, h, cls, { rx: 6, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 6, fill: "none", ...op(v) }) +
    SV.text(x + 10, y + h / 2 + 6, String(addr), "sm", { style: "font-family:var(--mono)", ...op(v) }) +
    SV.text(x + w - 12, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono);font-size:17px", ...op(v) });
}
function regBox(x, y, name, val, cls = "f2", v = 1, w = 120, h = 46) {
  return SV.rect(x, y, w, h, cls, { rx: 8, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) }) +
    SV.text(x + 10, y - 7, name, "sm", op(v)) + SV.text(x + w / 2, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:19px", ...op(v) });
}
/* a list of code lines; hl is the highlighted index (or -1) */
function codeList(x, y, lines, hl, v = 1, lh = 30, w = 230) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 4, i === hl ? "cell-warn" : "cell", { rx: 4, ...op(v) }) + SV.text(x + 10, y + i * lh + 18, l, "lbl", { style: "font-family:var(--mono);font-size:14px;white-space:pre", ...op(v) })).join("");
}

(function () {
  const draw = (s) => { const k = Math.round(s.i); const scattered = "ABACBCAB".split(""), tidy = "AAABBBCC".split(""), arr = k >= 2 ? tidy : scattered; const col = { A: "f1", B: "f2", C: "f3" }; let o = ""; arr.forEach((c, i) => { o += SV.rect(30 + i * 60, 40, 54, 40, col[c], { rx: 4 }) + SV.text(57 + i * 60, 65, c, "lbl bd", { "text-anchor": "middle" }); });
    o += SV.text(30, 110, ["Files A, B and C are split into fragments around the disk", "To read file A the head must jump between three separate places", "Defragmentation moves the fragments so each file is contiguous", "Now each file is read in one go: less head movement"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 540, h: 130, label: "Defragmentation", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [0, 1, 2, 3].map((i) => ({ cap: ["After a lot of saving and deleting, files are fragmented.", "Reading file A means moving the read/write head to three places.", "<b>Defragmentation</b> makes each file contiguous.", "Access is faster because there is less head movement."][i], s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const items = ["check for errors", "partitions", "file system", "boot sector", "ready"]; let o = ""; items.forEach((t, i) => { o += SV.rect(20 + i * 108, 40, 100, 44, i <= k ? "f1" : "cell", { rx: 6 }) + SV.text(70 + i * 108, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); }); return o; };
  Lib.stepper($("#stB"), { w: 560, h: 110, label: "Formatting", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["The formatter checks the new disk for errors.", "It creates partitions.", "It sets up the file system and allocation table.", "It writes a boot sector and a volume label.", "The disk is now ready to store files."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, t, on) => SV.rect(x, y, 120, 40, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 60, y + 25, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); let o = B(20, 20, "Program 1", k >= 1) + B(20, 80, "Program 2", k >= 2) + B(300, 50, "graphics.dll", k >= 1);
    if (k >= 1) o += SV.path("M140,40 H300", "ax"); if (k >= 2) o += SV.path("M140,100 L300,80", "ax"); o += SV.text(20, 150, ["", "Program 1 needs the DLL: it is loaded into memory", "Program 2 uses the same copy: loaded only once", "The DLL is updated: both programs benefit with no recompile"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 170, label: "DLL", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [0, 1, 2, 3].map((i) => ({ cap: ["A DLL is a library file kept separate from programs.", "Program 1 needs it, so it is <b>loaded when needed</b>.", "Program 2 <b>shares</b> the same copy in memory.", "An update to the DLL applies to every program that uses it, with no recompile."][i], s: { i } })) });
})();

(function () {
  const colors = ["f1", "f2", "f3"]; const init = "ABACBCAB".split(""); let arr, done;
  const reset = () => { arr = init.slice(); done = false; paint(); };
  const paint = () => { let o = '<svg viewBox="0 0 500 70" style="width:500px;max-width:100%;display:block">'; arr.forEach((c, i) => { o += `<rect x="${10 + i * 60}" y="10" width="54" height="40" rx="4" class="${colors[c.charCodeAt(0) - 65]}"/><text x="${37 + i * 60}" y="35" text-anchor="middle" class="lbl bd">${c}</text>`; }); $("#dfG").innerHTML = o + "</svg>";
    const jumps = (f) => { let n = 0; for (let i = 1; i < arr.length; i++) if (arr[i] === f && arr[i - 1] !== f) n++; return n + (arr[0] === f ? 1 : 0); };
    $("#dfV").innerHTML = `Starts of separate fragments: file A <b>${jumps("A")}</b>, B <b>${jumps("B")}</b>, C <b>${jumps("C")}</b>.` + (done ? " After defragmentation each file is in one contiguous run, so the head moves less." : " Press Defragment."); };
  $("#df_go").onclick = () => { arr = arr.slice().sort(); done = true; paint(); }; $("#df_reset").onclick = reset; reset();
})();
btnTable("uB", "uO", [
  ["A new USB drive that Windows cannot use yet", "Disk formatter", "Sets up the file system"],
  ["A disk that takes a long time to open files", "Defragmentation", "Makes files contiguous"],
  ["Copy homework to a cloud drive every night", "Back-up software", "Restore if lost"],
  ["Remove a trojan from a laptop", "Virus checker", "Deletes or quarantines malware"],
  ["Fit a big folder in an email attachment limit", "File compression", "Smaller file"],
  ["A disk with unreadable areas", "Disk repair", "Marks bad sectors"]
], ["Situation", "Utility", "Why"]);
(function () {
  let mb = 48, pct = 60; const paint = () => { const c = mb * (1 - pct / 100); $("#cV").innerHTML = `A <b>${mb} MB</b> file compressed by <b>${pct}%</b> becomes <b>${c.toFixed(1)} MB</b>. At 4 MB per second it uploads in <b>${(c / 4).toFixed(1)} s</b> instead of <b>${(mb / 4).toFixed(1)} s</b>: it saves storage space and transmission time.`; };
  Lib.slider($("#cS").appendChild(document.createElement("div")), { id: "c1", label: "File size (MB) ", min: 4, max: 200, value: mb, fmt: (x) => x, onInput: (v) => { mb = v; paint(); } });
  Lib.slider($("#cS").appendChild(document.createElement("div")), { id: "c2", label: "Compression ", min: 0, max: 95, value: pct, fmt: (x) => x + "%", onInput: (v) => { pct = v; paint(); } }); paint();
})();
Lib.classify($("#cl1"), { prompt: "Which utility does it describe?", buckets: [{"label": "Defragmentation"}, {"label": "Back-up"}, {"label": "Disk formatter"}, {"label": "Virus checker"}, {"label": "Compression"}], items: [{"text": "Moves file parts so each file is contiguous", "b": 0}, {"text": "Makes a copy in case the original is lost", "b": 1}, {"text": "Sets up a new disk to store files", "b": 2}, {"text": "Scans for malicious program code", "b": 3}, {"text": "Decreases the file size", "b": 4}, {"text": "Reduces head movement when reading files", "b": 0}], done: "Match the purpose." });
Lib.classify($("#cl2"), { prompt: "Is the point a general library point or specific to a DLL?", buckets: [{"label": "Program library"}, {"label": "DLL"}], items: [{"text": "Pre-written and pre-tested routines", "b": 0}, {"text": "Loaded into memory only when needed", "b": 1}, {"text": "Saves time writing code from scratch", "b": 0}, {"text": "Updated without recompiling the main program", "b": 1}, {"text": "Shared by several programs at once", "b": 1}, {"text": "Makes the source code easier to read", "b": 0}], done: "DLL: separate, loaded when needed, shared, updatable." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Disk formatter", "Prepares a disk for use by setting up the file system"], ["Defragmentation", "Makes files contiguous"], ["Virus checker", "Scans for and removes malicious code"], ["Back-up", "Copies files in case the original is lost"], ["Disk repair", "Checks for and fixes inconsistencies on a disk"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of formatting a new disk in order.", items: ["The disk is checked for errors", "Partitions are created", "A file system (allocation table) is set up", "A boot sector and volume label are created", "The disk is ready to store files"], done: "Check, partition, file system, boot sector, ready." });
Lib.calc($("#c1"), { qs: [
  {"q": "A 24 MB file is compressed by 75%. How many MB is the compressed file?", "a": 6, "unit": "MB", "tol": 0.01, "hint": "25% of 24.", "sol": "<b>6</b> MB."},
  {"q": "A 12 MB file is sent at 2 MB per second. How many seconds? Then compressed to a third of the size: how many seconds now? Give the saving in seconds.", "a": 4, "unit": "s", "tol": 0.01, "hint": "6 − 2.", "sol": "<b>4</b> s (6 s down to 2 s)."},
  {"q": "A backup is made every 6 hours. How many backups in a week (7 days)?", "a": 28, "unit": "", "tol": 0.01, "hint": "4 per day × 7.", "sol": "<b>28</b>."},
  {"q": "Three programs each load a 5 MB library. With a shared DLL loaded once, how many MB are saved?", "a": 10, "unit": "MB", "tol": 0.01, "hint": "15 − 5.", "sol": "<b>10</b> MB."},
  {"q": "A file is stored in 6 fragments. After defragmentation it is stored in 1 contiguous block. How many fewer head movements to find the file's parts (assume one per fragment gap)?", "a": 5, "unit": "", "tol": 0.01, "hint": "6 − 1.", "sol": "<b>5</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Defragmentation improves performance by:", opts: ["Making files contiguous, so less head movement", "Compressing files", "Deleting files", "Adding RAM"], a: 0, why: "Contiguous files." },
  { q: "A back-up is used to:", opts: ["Restore lost data", "Scan for viruses", "Format a disk", "Speed up the CPU"], a: 0, why: "Restore." },
  { q: "A program library is:", opts: ["Pre-written, pre-tested routines", "A building", "A text file", "A type of RAM"], a: 0, why: "Pre-written routines." },
  { q: "A DLL is:", opts: ["Loaded only when needed", "Always in RAM", "A compiler", "A utility"], a: 0, why: "Loaded when needed." },
  { q: "A disk formatter:", opts: ["Prepares a disk for use", "Defragments", "Repairs viruses", "Compiles"], a: 0, why: "Prepares." },
  { q: "A drawback of library routines:", opts: ["May not match the needs exactly", "Take longer to write", "Are untested by definition", "Cannot be imported"], a: 0, why: "May not match." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Utility software", "Housekeeping and maintenance tasks."],
  ["Disk formatter", "Initialises a disk; file system, partitions."],
  ["Defragmentation", "Contiguous files; less head movement."],
  ["Back-up", "Regular copies; restore if lost."],
  ["Compression", "Smaller files; less storage and time."],
  ["Virus checker", "Scans, deletes or quarantines malware."],
  ["Program library", "Pre-written, pre-tested routines."],
  ["DLL", "Loaded when needed; shared; updated alone."],
] });
