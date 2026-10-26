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
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "Program (logical)", "lbl bd") + SV.text(300, 20, "RAM (frames)", "lbl bd") + SV.text(510, 20, "Page table", "lbl bd");
    const frames = { 0: 2, 1: 0, 2: 3, 3: 1 }; // page -> frame
    [0, 1, 2, 3].forEach((p) => { o += SV.rect(20, 32 + p * 52, 130, 42, k === 3 && p === 3 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(85, 58 + p * 52, "page " + p, "lbl", { "text-anchor": "middle" }); });
    [0, 1, 2, 3].forEach((f) => { const p = Object.keys(frames).find((x) => frames[x] === f); const here = k >= 1 && p !== undefined && (+p !== 3 || k >= 4); o += SV.rect(300, 32 + f * 52, 130, 42, here ? "f" + (f + 1) : "cell", { rx: 6, ...op(here ? 1 : 0.5) }) + SV.rect(300, 32 + f * 52, 130, 42, "ax", { rx: 6, fill: "none", ...op(here ? 1 : 0.4) }) + SV.text(365, 58 + f * 52, here ? "page " + p : "frame " + f + " (free)", "lbl", { "text-anchor": "middle", ...op(here ? 1 : 0.6) }); });
    [0, 1, 2, 3].forEach((p) => { const inmem = p !== 3 || k >= 4; o += SV.rect(510, 32 + p * 52, 150, 42, k >= 2 ? "cell" : "cell", { rx: 6, ...op(k >= 2 ? 1 : 0.35) }) + (k >= 2 ? SV.text(585, 58 + p * 52, p + " → " + (inmem ? "frame " + frames[p] : "on disk"), "lbl", { "text-anchor": "middle" }) : ""); });
    if (k >= 1) [0, 1, 2].forEach((p) => (o += SV.path("M150," + (53 + p * 52) + " L300," + (53 + frames[p] * 52), "edge", { ...op(0.55) }))); if (k >= 4) o += SV.path("M150,209 L300,85", "edge", { style: "stroke:var(--accent);stroke-width:3.5" });
    return o; };
  Lib.stepper($("#stA"), { w: 700, h: 252, label: "Paging", base: { i: 0 }, draw, tween: 140, dwell: 2800, steps: [
    { cap: "A program has four <b>pages</b> of the same size. RAM is divided into <b>frames</b> of the same size.", s: { i: 0 } },
    { cap: "Pages 0, 1 and 2 are loaded into frames. They do not have to be next to each other, and not every page has to be in RAM.", s: { i: 1 } },
    { cap: "The <b>page table</b> records which frame each page is in. Page 3 is still on the disk.", s: { i: 2 } },
    { cap: "The program needs page 3. It is not in RAM: a <b>page fault</b>. The OS must fetch it from the disk.", s: { i: 3 } },
    { cap: "The OS loads page 3 into a free frame and updates the page table. The program carries on.", s: { i: 4 } }] });
})();
(function () {
  const segs = [["Main code", 3], ["Procedure", 2], ["Data", 4], ["Stack", 1]]; const base = [0, 3, 5, 9], tw = 40;
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "Segments (logical, different sizes)", "lbl bd") + SV.text(380, 20, "RAM", "lbl bd") + SV.text(380, 168, "", "sm");
    let y = 30; segs.forEach(([n, h], i) => { o += SV.rect(20, y, 220, 14 * h + 8, i === 2 && k === 3 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(130, y + (14 * h + 8) / 2 + 5, i + ": " + n + " (size " + h + ")", "lbl", { "text-anchor": "middle" }); y += 14 * h + 16; });
    segs.forEach(([n, h], i) => { const on = k >= 1; o += SV.rect(380, 30 + base[i] * 18, 150, 18 * h - 2, on ? "f" + (i + 1) : "cell", { rx: 4, ...op(on ? 1 : 0.35) }) + (on ? SV.text(455, 30 + base[i] * 18 + (18 * h - 2) / 2 + 5, n, "lbl", { "text-anchor": "middle" }) : ""); });
    if (k >= 2) { o += SV.text(570, 36, "Segment map table", "lbl bd"); segs.forEach(([n, h], i) => (o += SV.text(570, 62 + i * 24, i + " → base " + base[i] + ", size " + h, "lbl", { style: "font-size:12.5px" }))); }
    if (k === 3) o += SV.text(380, 252, "address (2, 3): segment 2, offset 3 → base 5 + 3 = 8", "lbl bd t3", { style: "font-size:13px" });
    return o; };
  Lib.stepper($("#stB"), { w: 800, h: 280, label: "Segmentation", base: { i: 0 }, draw, tween: 140, dwell: 2800, steps: [
    { cap: "The program is divided into logical <b>segments</b> of <b>different sizes</b>: code, a procedure, data, and the stack.", s: { i: 0 } },
    { cap: "Each segment is loaded into a block of RAM large enough to hold it.", s: { i: 1 } },
    { cap: "The <b>segment map table</b> records the start address (base) and size of each segment.", s: { i: 2 } },
    { cap: "A logical address is a <b>segment number and an offset</b>. (2, 3) means segment 2, offset 3: base 5 + offset 3 = physical 8. The offset must be less than the segment's size.", s: { i: 3 } }] });
})();
(function () {
  const pts = [[1, 30], [2, 55], [3, 80], [4, 95], [5, 80], [6, 45], [7, 18], [8, 8]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.path("M60,20 V190 H500", "ax") + SV.text(280, 214, "number of programs running", "sm", { "text-anchor": "middle" }) + SV.text(14, 14, "CPU doing useful work (%)", "sm");
    let d = ""; pts.slice(0, k).forEach(([n, u], i) => { const x = 60 + n * 52, y = 190 - u * 1.7; d += (i ? "L" : "M") + x + "," + y + " "; o += SV.circle(x, y, 5, k >= 6 && n >= 6 ? "dot2" : "dot3") + SV.text(x, 208, String(n), "sm", { "text-anchor": "middle", style: "display:none" }); });
    if (k > 1) o += SV.path(d, "c3"); if (k >= 5) o += SV.text(250, 38, "RAM is full: pages are swapped in and out", "lbl bd t4", { style: "font-size:13px" }); if (k >= 7) o += SV.text(380, 120, "thrashing", "lbl bd t2"); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 230, label: "Thrashing", base: { i: 0 }, draw, tween: 120, dwell: 2200, steps: [{ cap: "One program: the CPU is often idle waiting for the disk.", s: { i: 1 } }, { cap: "More programs: the CPU is used more.", s: { i: 3 } }, { cap: "A peak: RAM holds just enough pages for every program.", s: { i: 4 } }, { cap: "Too many programs: RAM is full and pages are swapped in and out all the time.", s: { i: 5 } }, { cap: "More swapping means more disk head movement and long waits.", s: { i: 6 } }, { cap: "<b>Thrashing</b>: more time is spent swapping pages than processing data, so useful work falls to a few percent.", s: { i: 8 } }] });
})();

(function () {
  const PT = { 0: 5, 1: 2, 2: 7, 3: 1 }; let a = 3000; const PS = 1024;
  const paint = () => { const pg = Math.floor(a / PS), off = a % PS, fr = PT[pg]; $("#aO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Page</th><th>Frame</th></tr>' + Object.entries(PT).map(([p, f]) => `<tr${+p === pg ? ' style="background:var(--accent-soft);font-weight:700"' : ""}><td>${p}</td><td>${f}</td></tr>`).join("") + "</table></div>" + `<div class="verdict">Logical address <b>${a}</b>: page = ${a} ÷ ${PS} = <b>${pg}</b>, offset = <b>${off}</b>. ` + (fr === undefined ? "This page is not in the page table: page fault." : `Page ${pg} is in frame ${fr}: physical address = ${fr} × ${PS} + ${off} = <b>${fr * PS + off}</b>.`) + "</div>"; };
  Lib.slider($("#aS"), { id: "as", label: "Logical address ", min: 0, max: 4095, value: a, fmt: (x) => x, onInput: (v) => { a = v; paint(); } }); paint();
})();
(function () {
  const refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]; let nf = 3, pol = "FIFO"; const b = $("#rB");
  const run = () => { const fr = [], last = {}, out = []; refs.forEach((p, i) => { const f = !fr.includes(p); if (f) { if (fr.length === nf) { const v = pol === "FIFO" ? fr[0] : fr.reduce((m, x) => (last[x] < last[m] ? x : m)); fr.splice(fr.indexOf(v), 1); } fr.push(p); } last[p] = i; out.push([p, fr.slice(), f]); }); return out; };
  const paint = () => { const tr = run(); let h = '<div class="tw"><table class="t mono"><tr><th>Page</th>' + tr.map(([p]) => `<td>${p}</td>`).join("") + "</tr>"; for (let r = 0; r < nf; r++) h += `<tr><th>frame ${r + 1}</th>` + tr.map(([, f]) => `<td>${f[r] === undefined ? "" : f[r]}</td>`).join("") + "</tr>"; h += "<tr><th>fault</th>" + tr.map(([, , f]) => `<td>${f ? "F" : ""}</td>`).join("") + "</tr></table></div>";
    $("#rO").innerHTML = h + `<div class="verdict">${pol}, ${nf} frames: <b>${tr.filter((x) => x[2]).length}</b> page faults out of ${refs.length} references. ${nf >= 5 ? "With enough frames only the first use of each page faults." : ""}</div>`; b.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === pol ? "on" : "")); };
  ["FIFO", "LRU"].forEach((k) => { const x = document.createElement("button"); x.textContent = k === "FIFO" ? "First in first out" : "Least recently used"; x.dataset.k = k; x.onclick = () => { pol = k; paint(); }; b.appendChild(x); });
  Lib.slider($("#rS"), { id: "rs", label: "Frames ", min: 2, max: 6, value: nf, fmt: (x) => x, onInput: (v) => { nf = v; paint(); } }); paint();
})();
(function () {
  let n = 3;
  const paint = () => { const need = 3 * n, ram = 12, fault = Math.max(0, (need - ram) / need), useful = Math.round(Math.min(1, 0.28 * n) * (1 - Math.min(0.96, 2.2 * fault)) * 100);
    $("#tO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Programs</th><th>Frames needed</th><th>RAM</th><th>Pages swapped a lot?</th><th>Useful CPU work</th></tr>' + `<tr><td>${n}</td><td>${need}</td><td>${ram}</td><td>${need > ram ? "yes" : "no"}</td><td>${useful}%</td></tr></table></div>`;
    $("#tV").innerHTML = need <= ram ? "All the pages the programs need fit in RAM, so there is little swapping." : "The programs need <b>" + need + "</b> frames but RAM has only 12. Pages are swapped between RAM and the disk all the time. " + (useful < 30 ? "This is <b>thrashing</b>: more time is spent swapping than processing." : "Performance is falling."); };
  Lib.slider($("#tS"), { id: "ts", label: "Programs running ", min: 1, max: 8, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();
Lib.classify($("#cl1"), { prompt: "Is it a feature of paging or segmentation?", buckets: [{"label": "Paging"}, {"label": "Segmentation"}], items: [{"text": "Blocks are all the same size", "b": 0}, {"text": "Blocks vary in size", "b": 1}, {"text": "The OS divides memory into the blocks", "b": 0}, {"text": "The compiler works out the sizes", "b": 1}, {"text": "The address is a page number and an offset", "b": 0}, {"text": "The address is a segment number and an offset", "b": 1}, {"text": "Uses a page table", "b": 0}, {"text": "Uses a segment map table", "b": 1}], done: "Paging: fixed, OS. Segmentation: variable, logical units." });
Lib.classify($("#cl2"), { prompt: "True or false about virtual memory?", buckets: [{"label": "True"}, {"label": "False"}], items: [{"text": "It uses secondary storage to extend RAM", "b": 0}, {"text": "It is faster than RAM", "b": 1}, {"text": "The CPU appears to have more memory", "b": 0}, {"text": "It is created temporarily when needed", "b": 0}, {"text": "It is a type of RAM chip", "b": 1}, {"text": "Data not in use can be moved to it", "b": 0}], done: "Disk space, slower than RAM." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Page", "Fixed-size block of the logical address space"], ["Frame", "Fixed-size block of physical memory"], ["Page fault", "The page needed is not in RAM"], ["Segment", "Variable-size logical part of a program"], ["Thrashing", "More time swapping pages than processing"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of a page fault in order.", items: ["The CPU needs a page that is not in RAM", "The OS finds the page on the disk", "A free frame is found, or a page is replaced", "The page is loaded into the frame and the page table is updated", "The program carries on"], done: "Need, find, frame, load, continue." });
Lib.calc($("#c1"), { qs: [
  {"q": "The page size is 1024 bytes. Which page contains the logical address 5000?", "a": 4, "unit": "", "tol": 0.01, "hint": "5000 ÷ 1024 = 4.88.", "sol": "<b>4</b>."},
  {"q": "What is the offset of the logical address 5000 (page size 1024)?", "a": 904, "unit": "", "tol": 0.01, "hint": "5000 − 4 × 1024.", "sol": "5000 − 4096 = <b>904</b>."},
  {"q": "Page 4 is in frame 2. What is the physical address of logical address 5000?", "a": 2952, "unit": "", "tol": 0.01, "hint": "2 × 1024 + 904.", "sol": "2048 + 904 = <b>2952</b>."},
  {"q": "A segment starts at base 5 (in blocks) and the offset is 3. What is the physical block?", "a": 8, "unit": "", "tol": 0.01, "hint": "Base plus offset.", "sol": "<b>8</b>."},
  {"q": "A program has 6 pages. RAM can hold 4 of them. How many pages are on the disk?", "a": 2, "unit": "", "tol": 0.01, "hint": "6 − 4.", "sol": "<b>2</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Virtual memory uses:", opts: ["Extra RAM chips", "Secondary storage", "Cache only", "ROM"], a: 1, why: "Disk space." },
  { q: "Pages are:", opts: ["Variable-size blocks", "Fixed-size blocks of logical memory", "Files", "Folders"], a: 1, why: "Fixed-size blocks." },
  { q: "Which maps a segment number to a physical address?", opts: ["Segment map table", "Page table", "Directory", "Stack"], a: 0, why: "The segment map table." },
  { q: "Disk thrashing happens when:", opts: ["The disk is full", "Main memory is full and pages are swapped constantly", "The CPU is too fast", "The screen is off"], a: 1, why: "Constant swapping." },
  { q: "Who decides the segment sizes?", opts: ["The user's keyboard", "The programmer or compiler", "The printer", "The monitor"], a: 1, why: "Logical units." },
  { q: "A page fault means:", opts: ["The disk has failed", "The page is not in RAM", "The page is corrupt", "The CPU is hot"], a: 1, why: "The page is not in RAM." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Virtual memory", "Disk used to extend RAM; temporary."],
  ["Paging", "Fixed-size pages and frames; page table; page number + offset."],
  ["Segmentation", "Variable-size logical segments; segment map table."],
  ["Page fault", "Needed page not in RAM; load from disk."],
  ["Page replacement", "Choose a page to move out when RAM is full."],
  ["Thrashing", "Too much swapping: more time swapping than processing."],
  ["Fix thrashing", "More RAM or fewer programs."],
  ["Paging v segmentation", "Fixed v variable; OS v compiler."],
] });
