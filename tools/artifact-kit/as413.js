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
  const draw = (s) => { const k = Math.round(s.i); const R = (x, y, t, v, on) => SV.rect(x, y, 120, 44, on ? "f3" : "cell", { rx: 6 }) + SV.text(x + 60, y + 18, t, "sm", { "text-anchor": "middle" }) + SV.text(x + 60, y + 36, v, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" });
    const pc = k >= 2 ? 101 : 100; let o = R(20, 20, "PC", pc, k === 2 || k === 1) + R(180, 20, "MAR", k >= 1 ? 100 : "", k === 1 || k === 3) + R(340, 20, "MDR", k >= 3 ? "LDM #5" : "", k === 3 || k === 4) + R(500, 20, "CIR", k >= 4 ? "LDM #5" : "", k === 4);
    o += SV.text(300, 110, ["", "MAR ← [PC]", "PC ← [PC] + 1", "MDR ← [[MAR]]", "CIR ← [MDR]"][k], "lbl bd t3", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stA"), { w: 640, h: 130, label: "Fetch", base: { i: 0 }, draw, tween: 100, dwell: 2500, steps: [{ cap: "The PC holds 100, the address of the next instruction.", s: { i: 0 } }, { cap: "The contents of the PC are copied to the <b>MAR</b>.", s: { i: 1 } }, { cap: "The PC is <b>incremented</b>, ready for the next instruction.", s: { i: 2 } }, { cap: "The data at the address in the MAR is copied to the <b>MDR</b> (the double brackets).", s: { i: 3 } }, { cap: "The MDR contents are copied to the <b>CIR</b>. The CU then decodes it.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, w, t, on) => SV.rect(x, y, w, 40, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + w / 2, y + 26, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" });
    let o = B(20, 30, 130, "running process", k <= 1 || k >= 6) + B(200, 30, 130, "F-E cycle ends", k === 1) + B(380, 30, 150, "check interrupt flag", k === 2) + B(380, 90, 150, "registers to stack", k === 3) + B(200, 90, 130, "ISR runs", k === 4) + B(20, 90, 130, "registers restored", k >= 5);
    return o; };
  Lib.stepper($("#stB"), { w: 560, h: 150, label: "Interrupt handling", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "A process is running its F-E cycles.", s: { i: 0 } }, { cap: "A key is pressed; an interrupt flag is set. The current cycle finishes.", s: { i: 1 } }, { cap: "The processor <b>checks the interrupt register</b> and the interrupt's priority.", s: { i: 2 } }, { cap: "Higher priority: the <b>registers are stored on the stack</b>.", s: { i: 3 } }, { cap: "The <b>ISR</b> for the key press runs.", s: { i: 4 } }, { cap: "The registers are <b>restored from the stack</b>.", s: { i: 5 } }, { cap: "The process continues with the next F-E cycle.", s: { i: 6 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const lvl = (y, t, p, on) => SV.rect(40, y, 400, 34, on ? "f3" : "cell", { rx: 6 }) + SV.text(52, y + 22, t + " (priority " + p + ")", "lbl", { style: "font-size:13px" });
    return lvl(20, "Power failure", 5, k === 3) + lvl(62, "Keyboard key press", 3, k === 2) + lvl(104, "Running program", 2, k <= 1) + SV.text(250, 165, ["", "", "key press: higher than the program, so it interrupts", "power failure outranks everything"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); };
  Lib.stepper($("#stC"), { w: 480, h: 180, label: "Priority", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "Interrupts have priorities.", s: { i: 0 } }, { cap: "A running program has priority 2.", s: { i: 1 } }, { cap: "A key press (3) is higher, so it <b>interrupts</b> the program.", s: { i: 2 } }, { cap: "A power failure (5) is higher still and is dealt with first.", s: { i: 3 } }] });
})();

(function () {
  const prog = ["LDM #5", "ADD #3", "STO 200", "END"]; let st;
  const reset = () => { st = { pc: 100, mar: "", mdr: "", cir: "", acc: 0, mem200: 0, k: 0, log: ["Ready: PC = 100."] }; paint(); };
  const step = () => { const s = st; if (s.done) return; const ph = s.k % 5;
    if (ph === 0) { s.mar = s.pc; s.log.push("MAR ← [PC]: MAR = " + s.mar); }
    else if (ph === 1) { s.pc++; s.log.push("PC ← [PC] + 1: PC = " + s.pc); }
    else if (ph === 2) { s.mdr = prog[s.mar - 100]; s.log.push("MDR ← [[MAR]]: MDR = " + s.mdr); }
    else if (ph === 3) { s.cir = s.mdr; s.log.push("CIR ← [MDR]: CIR = " + s.cir); }
    else { const [op, a] = s.cir.split(" "); if (op === "LDM") s.acc = +a.slice(1); if (op === "ADD") s.acc += +a.slice(1); if (op === "STO") s.mem200 = s.acc; if (op === "END") s.done = true; s.log.push("Decode and execute " + s.cir + (op === "END" ? ": stop." : ": ACC = " + s.acc + (op === "STO" ? ", location 200 = " + s.mem200 : "")) ); }
    s.k++; paint(); };
  const paint = () => { const s = st; const R = (n, v) => `<span style="display:inline-block;min-width:96px;border:1px solid var(--border);border-radius:8px;padding:6px 10px;margin:3px"><span class="sm">${n}</span><br><b>${v === "" ? "·" : v}</b></span>`;
    $("#feR").innerHTML = R("PC", s.pc) + R("MAR", s.mar) + R("MDR", s.mdr) + R("CIR", s.cir) + R("ACC", s.acc);
    $("#feM").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Address</th><th>Contents</th></tr>' + prog.map((p, i) => `<tr style="${s.mar === 100 + i && s.k % 5 !== 0 ? "background:var(--accent-soft);font-weight:700" : ""}"><td>${100 + i}</td><td>${p}</td></tr>`).join("") + `<tr><td>200</td><td>${s.mem200}</td></tr></table></div>`;
    $("#feL").innerHTML = s.log.slice(-3).join("<br>"); };
  $("#fe_step").onclick = step; $("#fe_reset").onclick = reset; reset();
})();
btnTable("iB", "iO", [
  ["A key is pressed", "Hardware", "A device asks for attention"],
  ["The printer is out of paper", "Hardware", "A device event"],
  ["Division by zero", "Software", "Error in the program"],
  ["Stack overflow", "Software", "Program uses too much stack"],
  ["Power failure", "Hardware", "Highest priority"],
  ["Array index out of bounds", "Software", "Invalid access in the program"]
], ["Event", "Type", "Why"]);
(function () {
  let p = 3; const cur = 2; const paint = () => { $("#pV").innerHTML = p > cur ? `The interrupt (priority <b>${p}</b>) is higher than the running process (<b>${cur}</b>): the registers are <b>stored on the stack</b> and the <b>ISR</b> runs.` : `The interrupt (priority <b>${p}</b>) is not higher than the running process (<b>${cur}</b>): the F-E cycle <b>continues</b> and the interrupt waits.`; };
  Lib.slider($("#pS"), { id: "p1", label: "Interrupt priority (running process is 2) ", min: 1, max: 5, value: p, fmt: (x) => x, onInput: (v) => { p = v; paint(); } }); paint();
})();
Lib.classify($("#cl1"), { prompt: "Hardware interrupt or software interrupt?", buckets: [{"label": "Hardware"}, {"label": "Software"}], items: [{"text": "A key is pressed", "b": 0}, {"text": "Division by zero", "b": 1}, {"text": "The printer is out of paper", "b": 0}, {"text": "Stack overflow", "b": 1}, {"text": "Power failure", "b": 0}, {"text": "Array index out of bounds", "b": 1}], done: "Hardware: devices. Software: program errors." });
Lib.classify($("#cl2"), { prompt: "Is the RTN statement correct for the fetch stage?", buckets: [{"label": "Correct"}, {"label": "Incorrect"}], items: [{"text": "MAR ← [PC]", "b": 0}, {"text": "PC ← [PC] − 1", "b": 1}, {"text": "MDR ← [[MAR]]", "b": 0}, {"text": "MDR ← [MAR]", "b": 1}, {"text": "CIR ← [MDR]", "b": 0}, {"text": "PC ← [PC] + 1", "b": 0}], done: "PC is incremented; MDR takes the contents of the address in the MAR." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["MAR ← [PC]", "The contents of the PC are copied to the MAR"], ["PC ← [PC] + 1", "The address in the PC is incremented"], ["MDR ← [[MAR]]", "The data at the address held in the MAR is copied to the MDR"], ["CIR ← [MDR]", "The contents of the MDR are copied into the CIR"], ["ISR", "Routine called to handle an interrupt"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the interrupt handling steps in order.", items: ["The interrupt flag is set and the F-E cycle ends", "The priority of the interrupt is checked", "The contents of the registers are stored on the stack", "The appropriate ISR is called and runs", "The registers are restored from the stack and the process continues"], done: "Flag, priority, stack, ISR, restore." });
Lib.calc($("#c1"), { qs: [
  {"q": "The PC holds 100. After the fetch stage (PC ← [PC] + 1) what does it hold?", "a": 101, "unit": "", "tol": 0.01, "hint": "Increment by 1.", "sol": "<b>101</b>."},
  {"q": "A program has 8 instructions. How many fetch stages (one per instruction)?", "a": 8, "unit": "", "tol": 0.01, "hint": "One each.", "sol": "<b>8</b>."},
  {"q": "Each F-E cycle takes 4 clock ticks. How many ticks for 8 instructions?", "a": 32, "unit": "", "tol": 0.01, "hint": "8 × 4.", "sol": "<b>32</b>."},
  {"q": "An interrupt has priority 5 and the running process priority 3. Should the F-E cycle be interrupted? Answer 1 for yes, 0 for no.", "a": 1, "unit": "", "tol": 0.01, "hint": "Higher priority interrupts.", "sol": "<b>1</b>: yes."},
  {"q": "How many RTN steps are in the fetch stage?", "a": 4, "unit": "", "tol": 0.01, "hint": "MAR, PC, MDR, CIR.", "sol": "<b>4</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "PC ← [PC] + 1 means:", opts: ["The address in the PC is incremented", "The PC is decremented", "The PC is cleared", "MAR is incremented"], a: 0, why: "Incremented." },
  { q: "MDR ← [[MAR]] copies:", opts: ["The data at the address in the MAR", "The MAR itself", "The PC", "The CIR"], a: 0, why: "Data at that address." },
  { q: "Interrupts are checked:", opts: ["At the end of each F-E cycle", "Only at start-up", "Never", "Once an hour"], a: 0, why: "End of cycle." },
  { q: "Registers are saved on:", opts: ["The stack", "The ROM", "The hard disk", "The cache only"], a: 0, why: "The stack." },
  { q: "A power failure is a:", opts: ["Hardware interrupt", "Software interrupt", "Compiler error", "Syntax error"], a: 0, why: "Hardware." },
  { q: "The ISR is:", opts: ["A routine that handles the interrupt", "A register", "A bus", "A type of memory"], a: 0, why: "Interrupt service routine." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Fetch (RTN)", "MAR←[PC]; PC←[PC]+1; MDR←[[MAR]]; CIR←[MDR]."],
  ["Decode, execute", "CU decodes the CIR; the instruction runs."],
  ["Interrupt", "Signal seeking the processor's attention."],
  ["Detected", "At the end of an F-E cycle."],
  ["Priority", "Checked; higher interrupts the process."],
  ["Stack", "Registers stored there."],
  ["ISR", "Routine called to handle it."],
  ["Restore", "Registers reloaded; process continues."],
] });
