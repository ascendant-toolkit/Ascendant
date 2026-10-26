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
  const A = [
    ["SISD", 1, 1, "One processor carries out one instruction at a time on one data item."],
    ["SIMD", 1, 3, "One instruction is applied to several data items at once."],
    ["MISD", 3, 1, "Several processors apply different instructions to the same data."],
    ["MIMD", 3, 3, "Each processor runs its own instructions on its own data."]
  ];
  const draw = (s) => {
    const k = Math.round(s.i), [name, ni, nd] = A[k]; let o = SV.text(30, 26, name, "lbl bd", { style: "font-size:22px" });
    const np = Math.max(ni, nd) === 1 ? 1 : 3, cols = ["f1", "f2", "f3"];
    for (let p = 0; p < np; p++) {
      const y = 50 + p * 62, x = 330;
      o += SV.rect(x, y, 140, 48, cols[p], { rx: 8 }) + SV.text(x + 70, y + 29, "Processor " + (p + 1), "lbl bd", { "text-anchor": "middle", style: "font-size:13px" });
      const ins = ni === 1 ? "same instruction" : "instruction " + "ABC"[p], dat = nd === 1 ? "same data" : "data " + (p + 1);
      o += arrow(190, y + 24, 328, y + 24, "r", "c1", 1) + SV.text(30, y + 28, ins, "lbl", { style: "font-size:14px" }) + arrow(580, y + 24, 472, y + 24, "l", "c2", 1) + SV.text(590, y + 28, dat, "lbl", { style: "font-size:14px" });
    }
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 240, label: "The four architectures", base: { i: 0 }, draw, tween: 250, dwell: 3600, steps: A.map((a, i) => ({ cap: "<b>" + a[0] + "</b>: " + a[3], s: { i } })) });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    for (let r = 0; r < 3; r++) for (let c = 0; c < 6; c++) { const x = 40 + c * 78, y = 30 + r * 56; o += SV.rect(x, y, 66, 44, k >= 1 ? (k >= 2 ? "cell-ok" : "f3") : "cell", { rx: 6 }) + SV.text(x + 33, y + 27, "P" + (r * 6 + c + 1), "lbl", { "text-anchor": "middle", style: "font-size:12px" }); }
    if (k >= 1) o += SV.text(40, 215, "each processor gets its own part of the problem", "lbl bd", { style: "font-size:14px" });
    if (k >= 2) o += SV.text(40, 238, "all work at the same time; results shared as messages over the network", "lbl bd t3", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 255, label: "A massively parallel computer", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "A massively parallel computer links together a very large number of processors (only 18 are drawn).", s: { i: 0 } },
    { cap: "A big problem is split into parts and <b>each processor is responsible for its own part</b>.", s: { i: 1 } },
    { cap: "They <b>work simultaneously</b> and communicate by <b>sending messages</b> across the network, combining their results.", s: { i: 2 } }] });
})();

/* Lab 1 */
(function () {
  let ni = 1, nd = 1;
  const names = { "1,1": ["SISD", "One processor, one instruction at a time, one data item. Sequential."], "1,3": ["SIMD", "The same instruction on many data items at once."], "3,1": ["MISD", "Different instructions on the same data stream."], "3,3": ["MIMD", "Different instructions on different data, independently."] };
  const paint = () => {
    $$("#aI button").forEach((b, i) => b.classList.toggle("pri", (i === 0 ? 1 : 3) === ni)); $$("#aD button").forEach((b, i) => b.classList.toggle("pri", (i === 0 ? 1 : 3) === nd));
    const n = names[ni + "," + nd]; $("#aO").innerHTML = `<div class="readout"><div><small>Architecture</small><strong>${n[0]}</strong></div></div><div class="verdict">${n[1]}</div>`;
  };
  $("#aI").innerHTML = '<span style="align-self:center;margin-right:6px">Instruction streams:</span><button class="b">Single</button><button class="b">Multiple</button>';
  $("#aD").innerHTML = '<span style="align-self:center;margin-right:6px">Data streams:</span><button class="b">Single</button><button class="b">Multiple</button>';
  $$("#aI button").forEach((b, i) => (b.onclick = () => { ni = i === 0 ? 1 : 3; paint(); })); $$("#aD button").forEach((b, i) => (b.onclick = () => { nd = i === 0 ? 1 : 3; paint(); })); paint();
})();

/* Lab 2 */
(function () {
  let p = 8, c = 0; const T = 1200;
  const paint = () => { const t = T / p + c * (p - 1) * 0.5; $("#s1").textContent = T + " s"; $("#s2").textContent = t.toFixed(1) + " s"; $("#s3").textContent = (T / t).toFixed(1) + "×"; };
  Lib.slider($("#sP"), { id: "sps", label: "Number of processors ", min: 1, max: 64, value: p, fmt: (x) => x, onInput: (v) => { p = v; paint(); } });
  Lib.slider($("#sC"), { id: "scs", label: "Communication cost per extra processor (seconds × 0.5) ", min: 0, max: 5, value: c, fmt: (x) => x, onInput: (v) => { c = v; paint(); } });
  paint();
})();

btnTable("eB", "eO", [
  ["SISD", "1 instruction stream, 1 data stream", "One processor, control unit and memory; sequential", "A basic single-core processor"],
  ["SIMD", "1 instruction stream, many data streams", "Same instruction on many data items at once; array processors", "Graphics processing"],
  ["MISD", "Many instruction streams, 1 data stream", "Different operations on the same data; rare", "Fault-tolerant checking"],
  ["MIMD", "Many instruction streams, many data streams", "Many processors working independently, asynchronously", "A multi-core PC, a cluster"],
  ["Massively parallel", "Very many processors working on one problem", "Network, message passing, each processor its own part", "Weather forecasting"]
], ["Type", "Streams", "Features", "Example"]);
Lib.classify($("#cl1"), { prompt: "Which architecture is described?", buckets: [{"label": "SISD"}, {"label": "SIMD"}, {"label": "MISD"}, {"label": "MIMD"}], items: [{"text": "One processor, instructions executed sequentially", "b": 0}, {"text": "The same instruction on many data items at once", "b": 1}, {"text": "Different instructions on the same data stream", "b": 2}, {"text": "Many processors, each with its own instructions and data", "b": 3}, {"text": "Contains one processor, a control unit and a memory unit", "b": 0}, {"text": "Array processors performing the same operation", "b": 1}, {"text": "Processors operate asynchronously and independently", "b": 3}, {"text": "Several processors work on a single data stream", "b": 2}], done: "Single or multiple instructions; single or multiple data." });
Lib.classify($("#cl2"), { prompt: "Is the statement true of SIMD or of MISD?", buckets: [{"label": "SIMD"}, {"label": "MISD"}], items: [{"text": "All the processors execute the same instruction", "b": 0}, {"text": "The processors perform different instructions", "b": 1}, {"text": "Many data streams are processed at once", "b": 0}, {"text": "All processors work on the same data", "b": 1}, {"text": "Suits applying one operation to every pixel", "b": 0}, {"text": "Used where different checks are made on one data stream", "b": 1}], done: "SIMD: same instruction, many data. MISD: different instructions, same data." });
Lib.order($("#o1"), { prompt: "Put the steps of solving a problem on a massively parallel computer in order.", items: ["The problem is divided into many parts", "Each processor is given its own part", "All the processors work on their parts at the same time", "Processors exchange results by sending messages", "The results are combined into the answer"], done: "Divide, assign, work together, message, combine." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["SISD", "Single instruction, single data"], ["SIMD", "Same instruction applied to multiple data streams"], ["MISD", "Different instructions on one data stream"], ["MIMD", "Different instructions on different data, independently"], ["Massively parallel", "Very many processors working together on one problem"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A SIMD processor applies one instruction to 8 data items at a time. How many instructions are needed to process 64 items?", "a": 8, "unit": "", "tol": 0.01, "hint": "64 ÷ 8.", "sol": "<b>8</b>."},
  {"q": "1200 equal tasks of 1 second are shared equally between 24 processors with no communication cost. How long does it take?", "a": 50, "unit": "s", "tol": 0.01, "hint": "1200 ÷ 24.", "sol": "<b>50</b> seconds."},
  {"q": "The same job on a single processor takes 1200 s. What is the speed-up with 24 processors (perfect sharing)?", "a": 24, "unit": "×", "tol": 0.01, "hint": "1200 ÷ 50.", "sol": "<b>24</b> times."},
  {"q": "How many data streams does a SISD computer have?", "a": 1, "unit": "", "tol": 0.01, "hint": "Single data.", "sol": "<b>1</b>."},
  {"q": "In MIMD, 4 processors each run their own program. How many instruction streams?", "a": 4, "unit": "", "tol": 0.01, "hint": "One each.", "sol": "<b>4</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does SIMD stand for?", opts: ["Single Instruction, Multiple Data", "Several Instructions, Multiple Data", "Single Instruction, Many Devices", "Serial Instruction, Multiple Data"], a: 0, why: "Single Instruction, Multiple Data." },
  { q: "Which architecture has many processors working independently on different data?", opts: ["SISD", "SIMD", "MISD", "MIMD"], a: 3, why: "MIMD." },
  { q: "In massively parallel computers, how do processors communicate?", opts: ["By sending messages over a network", "They do not", "Through a single bus only", "By sharing one register"], a: 0, why: "A message interface over a network." },
  { q: "Which executes instructions sequentially?", opts: ["SISD", "SIMD", "MISD", "MIMD"], a: 0, why: "SISD." },
  { q: "Which applies different instructions to the same data?", opts: ["SISD", "SIMD", "MISD", "MIMD"], a: 2, why: "MISD." },
] });
Lib.cards($("#fc1"), { cards: [
  ["SISD", "One processor; one instruction at a time on one data item."],
  ["SIMD", "Same instruction, multiple data items at once."],
  ["MISD", "Multiple instructions, same data."],
  ["MIMD", "Multiple instructions, multiple data, independent."],
  ["Massively parallel", "Many processors linked together, one problem, messages."],
  ["Asynchronous", "Not in step: each processor works independently."],
  ["Array processor", "Does the same operation on many data items."],
  ["Message passing", "How processors in a massively parallel computer communicate."],
] });
