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

const ST = ["IF", "ID", "OF", "IE", "WB"];
function pipeGrid(n, upto, discardFrom) {
  const cyc = n + 4; let h = '<div class="tw"><table class="t mono"><tr><th>Stage</th>' + Array.from({ length: cyc }, (_, c) => `<th>${c + 1}</th>`).join("") + "</tr>";
  ST.forEach((s, si) => { h += `<tr><td><b>${s}</b></td>`; for (let c = 1; c <= cyc; c++) { const i = c - si, show = i >= 1 && i <= n && c <= upto, disc = discardFrom && show && c >= discardFrom.c && !(si === 4 && c === discardFrom.c); h += `<td style="${show ? (disc ? "background:var(--bad-soft);text-decoration:line-through" : "background:var(--good-soft)") : ""}">${show ? "I" + i : ""}</td>`; } h += "</tr>"; });
  return h + "</table></div>";
}

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 18, "cycle →", "sm");
    for (let c = 1; c <= 10; c++) o += SV.text(94 + (c - 1) * 62, 18, String(c), "sm", { "text-anchor": "middle" });
    ST.forEach((st, si) => { o += SV.text(30, 52 + si * 38, st, "lbl bd"); for (let c = 1; c <= 10; c++) { const i = c - si; if (i >= 1 && i <= 6 && c <= k) o += SV.rect(66 + (c - 1) * 62, 32 + si * 38, 56, 30, ["f1", "f2", "f3", "f4", "f1", "f2"][i - 1], { rx: 5 }) + SV.text(94 + (c - 1) * 62, 52 + si * 38, "I" + i, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); } });
    if (k === 5) o += SV.text(30, 245, "cycle 5: the pipeline is full; instruction 1 finishes", "lbl bd t3", { style: "font-size:14px" });
    if (k === 10) o += SV.text(30, 245, "10 cycles for 6 instructions (30 without pipelining)", "lbl bd t3", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 258, label: "A five-stage pipeline", base: { i: 0 }, draw, tween: 200, dwell: 1600, steps: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map((i) => ({ cap: i === 0 ? "Each instruction goes through five stages: <b>IF, ID, OF, IE, WB</b>, one stage per clock cycle. Instruction 1 starts in cycle 1." : i === 1 ? "Cycle 1: I1 is fetched." : i === 2 ? "Cycle 2: I1 is decoded while <b>I2 is fetched</b>. Two instructions are in progress at once." : i === 5 ? "Cycle 5: five instructions are in progress, one in each stage. I1 writes back its result." : i === 10 ? "Cycle 10: the last instruction, I6, writes back. A finished instruction came out every cycle after cycle 5." : "Cycle " + i + ": each instruction moves on one stage and a new one is fetched until I6 has started.", s: { i } })) });
})();

(function () {
  const rows = ["Interrupt detected at the end of the fetch-execute cycle", "Register contents (including the PC) saved on the stack", "Interrupt service routine (ISR) runs", "Registers restored from the stack", "The original program carries on"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    rows.forEach((r, i) => (o += SV.rect(30, 14 + i * 40, 430, 34, k === i ? "cell-warn" : k > i ? "cell-ok" : "cell", { rx: 6 }) + SV.text(44, 36 + i * 40, r, "lbl", { style: "font-size:13px" })));
    o += SV.text(500, 24, "stack", "sm");
    for (let i = 0; i < 4; i++) o += SV.rect(500, 34 + (3 - i) * 36, 200, 30, k >= 1 && k <= 3 && i < 2 ? "f3" : "cell", { rx: 4, ...op(k >= 1 && k <= 3 && i < 2 ? 1 : 0.4) }) + (k >= 1 && k <= 3 && i < 2 ? SV.text(512, 54 + (3 - i) * 36, ["PC and ACC", "other registers"][i], "lbl", { style: "font-size:12px" }) : "");
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 225, label: "Interrupt handling", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: rows.map((r, i) => ({ cap: ["The processor checks for an interrupt at the end of each fetch-execute cycle and finds one.", "The program is paused. The register contents, including the program counter, are <b>pushed on the stack</b>.", "The <b>interrupt service routine</b> deals with whatever caused the interrupt.", "The ISR is finished. The registers are <b>restored</b> (popped) from the stack.", "The original program <b>carries on</b> exactly where it left off."][i], s: { i } })) });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = pipeSvg(k);
    return o;
  };
  function pipeSvg(k) {
    let o = SV.text(30, 18, "an interrupt arrives in cycle 5", "sm");
    ST.forEach((st, si) => { o += SV.text(30, 52 + si * 38, st, "lbl bd"); for (let c = 1; c <= 5; c++) { const i = c - si; if (i >= 1 && i <= 5) o += SV.rect(66 + (c - 1) * 80, 32 + si * 38, 74, 30, k >= 2 && c === 5 && si < 4 ? "cell-no" : k >= 1 && c === 5 ? "cell-ok" : "f3", { rx: 5 }) + SV.text(103 + (c - 1) * 80, 52 + si * 38, "I" + i, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); } });
    if (k >= 1) o += SV.text(66, 235, "cycle 5: I1 to I5 are all in the pipeline when the interrupt is received", "lbl bd", { style: "font-size:13px" });
    if (k >= 2) o += SV.text(66, 255, "I2, I3, I4, I5 are discarded; I1 (at write-back) is allowed to finish", "lbl bd t2", { style: "font-size:13px" });
    if (k >= 3) o += SV.text(66, 275, "after the ISR the processor restarts with the next instruction in the sequence (I2)", "lbl bd t3", { style: "font-size:13px" });
    return o;
  }
  Lib.stepper($("#stC"), { w: 760, h: 285, label: "Interrupt and a full pipeline", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "A program is running in a pipeline: several instructions are in progress at the same moment.", s: { i: 0 } },
    { cap: "An interrupt arrives at cycle 5. Instructions 1 to 5 are all in the pipeline: this is the extra <b>complexity</b> pipelining brings.", s: { i: 1 } },
    { cap: "Usually the instructions in the pipeline are <b>discarded</b>, except the one at the last (write-back) stage, which is allowed to finish.", s: { i: 2 } },
    { cap: "After the interrupt service routine, the processor <b>restarts with the next instruction in the sequence</b>.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  let n = 6;
  const paint = () => { $("#pT").innerHTML = pipeGrid(n, n + 4); $("#p1").textContent = n * 5 + " cycles"; $("#p2").textContent = n + 4 + " cycles"; $("#p3").textContent = (n * 5 / (n + 4)).toFixed(2) + "×"; };
  Lib.slider($("#pS"), { id: "pss", label: "Number of instructions ", min: 1, max: 12, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();

/* Lab 2 */
(function () {
  let c = 4;
  const paint = () => {
    $("#iT").innerHTML = pipeGrid(6, c, { c });
    const inFlight = [0, 1, 2, 3, 4].map((si) => c - si).filter((i) => i >= 1 && i <= 6);
    $("#iV").textContent = "Interrupt in cycle " + c + ": instructions " + inFlight.map((i) => "I" + i).join(", ") + " are in the pipeline. " + (inFlight.length > 1 ? "All except the one at write-back (struck-through ones are discarded) are discarded; the processor restarts with the next instruction after the ISR." : "Only one instruction is in the pipeline, so little is lost.");
  };
  Lib.slider($("#iS"), { id: "iss", label: "Interrupt arrives in clock cycle ", min: 1, max: 10, value: c, fmt: (x) => x, onInput: (v) => { c = v; paint(); } }); paint();
})();

btnTable("eB", "eO", [
  ["Instruction set", "Small, simple instructions", "Large, complex instructions", "Fewer instructions = RISC"],
  ["Instruction length", "Fixed", "Variable", "Fixed suits pipelining"],
  ["Cycles per instruction", "Usually one", "Several", "One cycle per stage"],
  ["Registers", "Many general-purpose registers", "Few registers", "Many = RISC"],
  ["Control unit", "Hardwired", "Programmable (micro-coded)", "Hardwired = RISC"],
  ["Pipelining", "Well suited", "Harder", "RISC: better pipelineability"]
], ["Feature", "RISC", "CISC", "Point to make"]);
Lib.classify($("#cl1"), { prompt: "Is the feature RISC or CISC?", buckets: [{"label": "RISC"}, {"label": "CISC"}], items: [{"text": "Many general-purpose registers", "b": 0}, {"text": "Variable-length instructions", "b": 1}, {"text": "Single-cycle instructions", "b": 0}, {"text": "A large instruction set", "b": 1}, {"text": "A hard-wired control unit", "b": 0}, {"text": "Many addressing modes", "b": 1}, {"text": "Makes frequent use of cache memory", "b": 1}, {"text": "The design emphasis is on the software", "b": 0}], done: "RISC: simple, fixed, one cycle, many registers. CISC: complex, variable, many modes." });
Lib.classify($("#cl2"), { prompt: "Which does the statement describe?", buckets: [{"label": "Pipelining"}, {"label": "Interrupt handling"}], items: [{"text": "Stages of different instructions overlap", "b": 0}, {"text": "Registers are stored on the stack", "b": 1}, {"text": "Increases instruction throughput", "b": 0}, {"text": "An interrupt service routine is run", "b": 1}, {"text": "No two instructions in the same stage in a cycle", "b": 0}, {"text": "Registers are restored afterwards", "b": 1}], done: "Pipelining overlaps stages. Interrupt handling saves state, runs the ISR, restores it." });
Lib.order($("#o1"), { prompt: "Put the steps of interrupt handling in order.", items: ["The processor detects the interrupt", "The register contents are stored on the stack", "The interrupt service routine is executed", "The registers are restored from the stack", "The interrupted program continues"], done: "Detect, save, ISR, restore, continue." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["RISC", "Reduced instruction set: simple, fixed-length, single-cycle"], ["CISC", "Complex instruction set: many formats and addressing modes"], ["Pipelining", "Overlapping the stages of different instructions"], ["Throughput", "Instructions completed per unit of time"], ["ISR", "The routine that deals with an interrupt"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A five-stage pipeline runs 6 instructions. How many clock cycles in total?", "a": 10, "unit": "", "tol": 0.01, "hint": "5 + (6 − 1).", "sol": "<b>10</b>."},
  {"q": "The same 6 instructions without pipelining. How many clock cycles?", "a": 30, "unit": "", "tol": 0.01, "hint": "6 × 5.", "sol": "<b>30</b>."},
  {"q": "A five-stage pipeline runs 100 instructions. How many clock cycles?", "a": 104, "unit": "", "tol": 0.01, "hint": "5 + 99.", "sol": "<b>104</b>."},
  {"q": "In which clock cycle does instruction 3 reach the OF (third) stage?", "a": 5, "unit": "", "tol": 0.01, "hint": "Instruction n is in stage s in cycle n + s − 1: 3 + 3 − 1.", "sol": "<b>5</b>."},
  {"q": "How many instructions are in a full five-stage pipeline at one moment?", "a": 5, "unit": "", "tol": 0.01, "hint": "One in each stage.", "sol": "<b>5</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a RISC feature?", opts: ["Variable-length instructions", "Many registers", "A large instruction set", "A programmable control unit"], a: 1, why: "RISC has many general-purpose registers." },
  { q: "Which is a CISC feature?", opts: ["Single-cycle instructions", "Hard-wired control unit", "Many addressing modes", "Easy pipelining"], a: 2, why: "CISC has many addressing modes." },
  { q: "What does pipelining improve?", opts: ["Memory size", "Instruction throughput", "Screen resolution", "Clock speed"], a: 1, why: "More instructions completed per unit of time." },
  { q: "Where are the registers stored when an interrupt is handled?", opts: ["On the stack", "In ROM", "On the hard disk", "They are lost"], a: 0, why: "They are stored on the stack." },
  { q: "What usually happens to instructions in the pipeline when an interrupt arrives?", opts: ["They all finish", "Most are discarded; the last-stage one finishes", "They are copied to RAM", "Nothing"], a: 1, why: "Most are discarded." },
  { q: "How many stages does the exam's pipeline have?", opts: ["3", "4", "5", "6"], a: 2, why: "IF, ID, OF, IE, WB." },
] });
Lib.cards($("#fc1"), { cards: [
  ["RISC", "Few simple fixed-length instructions, one cycle, many registers, hardwired."],
  ["CISC", "Large complex variable-length instructions, several cycles, few registers, programmable."],
  ["Pipelining", "Overlap the stages of different instructions. Throughput up."],
  ["Five stages", "IF, ID, OF, IE, WB."],
  ["n instructions", "5 + (n − 1) cycles with a five-stage pipeline."],
  ["Interrupt", "Detect, stack the registers, ISR, restore, continue."],
  ["Pipeline + interrupt", "Several instructions in progress: usually discarded; restart at the next."],
  ["Design emphasis", "RISC: software. CISC: hardware."],
] });
