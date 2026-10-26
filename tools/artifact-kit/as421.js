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
  const draw = (s) => { const k = Math.round(s.i); const lines = [["LDM #5", "0001 00000101"], ["ADD #3", "0010 00000011"], ["STO 200", "0101 11001000"]];
    let o = SV.text(120, 20, "assembly", "lbl bd", { "text-anchor": "middle" }) + SV.text(430, 20, "machine code", "lbl bd", { "text-anchor": "middle" }) + SV.rect(240, 70, 100, 40, "f3", { rx: 8 }) + SV.text(290, 95, "assembler", "lbl bd", { "text-anchor": "middle", style: "font-size:13px" });
    lines.forEach(([a, m], i) => { o += SV.rect(30, 30 + i * 34, 180, 28, "cell", { rx: 4 }) + SV.text(40, 49 + i * 34, a, "lbl"); if (k > i) o += SV.rect(360, 30 + i * 34, 180, 28, "f1", { rx: 4 }) + SV.text(370, 49 + i * 34, m, "lbl"); });
    if (k > 0) o += SV.path("M210,90 H240", "ax") + SV.path("M340,90 H360", "ax"); return o; };
  Lib.stepper($("#stA"), { w: 580, h: 150, label: "Assembler", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "Assembly language uses mnemonics and operands.", s: { i: 0 } }, { cap: "The assembler translates <b>LDM #5</b> into a binary opcode and operand.", s: { i: 1 } }, { cap: "<b>ADD #3</b> is translated next.", s: { i: 2 } }, { cap: "<b>STO 200</b> is translated. The result is machine code: binary.", s: { i: 3 } }] });
})();
const ASM = [["", "LDM #0"], ["LOOP", "ADD #1"], ["", "CMP #3"], ["", "JPN LOOP"], ["", "END"]], OPC = { LDM: "0001", ADD: "0010", CMP: "0011", JPN: "0100", END: "1111" }, BASE = 100;
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; ASM.forEach(([l, ins], i) => { o += SV.rect(30, 20 + i * 30, 250, 26, i === 1 && k >= 1 ? "f3" : "cell", { rx: 4 }) + SV.text(40, 38 + i * 30, (BASE + i) + "  " + (l ? l + ": " : "") + ins, "lbl"); });
    if (k >= 1) o += SV.rect(340, 60, 190, 60, "f1", { rx: 6 }) + SV.text(435, 82, "symbol table", "sm", { "text-anchor": "middle" }) + SV.text(435, 106, "LOOP = 101", "lbl bd", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stB"), { w: 560, h: 190, label: "First pass", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "The first pass reads the program and numbers each instruction from 100.", s: { i: 0 } }, { cap: "It finds the label <b>LOOP</b> on address 101 and records it in the <b>symbol table</b>.", s: { i: 1 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 20, 160, 40, "f1", { rx: 6 }) + SV.text(100, 45, "LOOP = 101", "lbl bd", { "text-anchor": "middle" }) + SV.rect(240, 20, 150, 28, "cell", { rx: 4 }) + SV.text(250, 38, "103  JPN LOOP", "lbl");
    if (k >= 1) o += SV.path("M180,40 H240", "ax"); if (k >= 2) o += SV.rect(240, 70, 300, 28, "f3", { rx: 4 }) + SV.text(250, 88, "0100 01100101   (JPN, 101)", "lbl"); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 120, label: "Second pass", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "On the second pass the assembler reaches <b>JPN LOOP</b>.", s: { i: 0 } }, { cap: "It looks LOOP up in the symbol table: address <b>101</b>.", s: { i: 1 } }, { cap: "It writes the opcode for JPN and the address 101 as machine code.", s: { i: 2 } }] });
})();

(function () {
  let st; const bin8 = (n) => ("00000000" + n.toString(2)).slice(-8);
  const reset = () => { st = { k: 0, sym: {}, mc: [] }; paint(); };
  const step = () => { const n = ASM.length; if (st.k < n) { const [l] = ASM[st.k]; if (l) st.sym[l] = BASE + st.k; } else if (st.k < 2 * n) { const i = st.k - n; const [l, ins] = ASM[i]; const [op, a] = ins.split(" "); let v = 0; if (a) v = a[0] === "#" ? +a.slice(1) : st.sym[a]; st.mc[i] = OPC[op] + " " + bin8(v); } else return; st.k++; paint(); };
  const paint = () => { const n = ASM.length; const pass = st.k < n ? 1 : 2; const cur = st.k < n ? st.k : st.k - n;
    $("#asP").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Address</th><th>Source</th><th>Machine code</th></tr>' + ASM.map(([l, ins], i) => `<tr style="${st.k < 2 * n && i === cur ? "background:var(--accent-soft);font-weight:700" : ""}"><td>${BASE + i}</td><td>${l ? l + ": " : ""}${ins}</td><td>${st.mc[i] || ""}</td></tr>`).join("") + "</table></div>";
    $("#asS").innerHTML = "<b>Symbol table:</b> " + (Object.keys(st.sym).length ? Object.entries(st.sym).map(([k, v]) => k + " = " + v).join(", ") : "empty");
    $("#asL").innerHTML = st.k >= 2 * n ? "Assembly finished: the program is now machine code." : st.k < n ? `First pass: reading instruction at address ${BASE + cur}.` : `Second pass: translating address ${BASE + cur}.`; };
  $("#as_step").onclick = step; $("#as_reset").onclick = reset; reset();
})();
btnTable("gB", "gO", [
  ["LDD 365", "Data movement", "Loads data from an address"],
  ["IN", "Input and output", "Takes a character from the keyboard"],
  ["ADD #5", "Arithmetic", "Adds a number to the ACC"],
  ["CMP 366", "Compare", "Compares ACC with a location"],
  ["JPE 209", "Conditional jump", "Jumps if the compare was true"],
  ["JMP 200", "Unconditional jump", "Always jumps"]
], ["Instruction", "Group", "What it does"]);
btnTable("oB", "oO", [
  ["LDM #5", "LDM", "#5 (denary 5)"],
  ["STO 200", "STO", "200 (an address)"],
  ["JPN LOOP", "JPN", "LOOP (a symbolic address)"],
  ["AND B00001111", "AND", "B00001111 (a binary mask)"],
  ["END", "END", "no operand"]
], ["Instruction", "Opcode", "Operand"]);
Lib.classify($("#cl1"), { prompt: "Which instruction group does it belong to?", buckets: [{"label": "Data movement"}, {"label": "Arithmetic"}, {"label": "Compare"}, {"label": "Jump"}], items: [{"text": "LDM #5", "b": 0}, {"text": "ADD 100", "b": 1}, {"text": "CMP 101", "b": 2}, {"text": "JPE 96", "b": 3}, {"text": "STO 200", "b": 0}, {"text": "INC ACC", "b": 1}], done: "Load and store: data movement. ADD, INC: arithmetic." });
Lib.classify($("#cl2"), { prompt: "Pass one or pass two of a two-pass assembler?", buckets: [{"label": "First pass"}, {"label": "Second pass"}], items: [{"text": "Creates the symbol table", "b": 0}, {"text": "Replaces labels by addresses", "b": 1}, {"text": "Works out the address of each label", "b": 0}, {"text": "Translates mnemonics into binary opcodes", "b": 1}, {"text": "Produces the machine code", "b": 1}, {"text": "Records each label and its address", "b": 0}], done: "Pass one: symbol table. Pass two: machine code." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Opcode", "The part of an instruction that says what to do"], ["Operand", "The data or address the instruction acts on"], ["Assembler", "Translates assembly language into machine code"], ["Symbol table", "Each label and its address"], ["Mnemonic", "A short word standing for an opcode, such as ADD"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of a two-pass assembler in order.", items: ["Read the whole program", "Work out the address of each instruction", "Add each label and its address to the symbol table", "Translate each instruction on the second pass", "Replace each label by its address from the symbol table"], done: "Read, addresses, symbol table, translate, replace." });
Lib.calc($("#c1"), { qs: [
  {"q": "A program starts at address 100 and each instruction takes one location. A label is on the fourth instruction. What address goes in the symbol table?", "a": 103, "unit": "", "tol": 0.01, "hint": "100, 101, 102, 103.", "sol": "<b>103</b>."},
  {"q": "A program has 12 instructions, one location each. How many passes does a two-pass assembler make over the program?", "a": 2, "unit": "", "tol": 0.01, "hint": "Two passes.", "sol": "<b>2</b>."},
  {"q": "How many instruction groups are listed in the Learn tab?", "a": 5, "unit": "", "tol": 0.01, "hint": "Data movement, input/output, arithmetic, compare, jumps.", "sol": "<b>5</b>."},
  {"q": "An opcode is 4 bits and an operand is 8 bits. How many bits per instruction?", "a": 12, "unit": "bits", "tol": 0.01, "hint": "4 + 8.", "sol": "<b>12</b> bits."},
  {"q": "With a 4-bit opcode, how many different opcodes are possible?", "a": 16, "unit": "", "tol": 0.01, "hint": "2^4.", "sol": "<b>16</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An assembler translates:", opts: ["Assembly language into machine code", "High-level code into assembly", "Machine code into text", "Binary into hex"], a: 0, why: "Assembly to machine code." },
  { q: "The first pass creates the:", opts: ["Symbol table", "Machine code", "Operand", "Stack"], a: 0, why: "Symbol table." },
  { q: "JPE is a:", opts: ["Conditional jump", "Compare", "Data movement", "Input"], a: 0, why: "Conditional." },
  { q: "In LDD 365, 365 is the:", opts: ["Operand", "Opcode", "Mnemonic", "Label"], a: 0, why: "Operand." },
  { q: "IN and OUT belong to the group:", opts: ["Input and output", "Data movement", "Arithmetic", "Compare"], a: 0, why: "Input and output." },
  { q: "Assembly language is:", opts: ["Processor-specific", "Portable between all processors", "A high-level language", "Binary"], a: 0, why: "Processor-specific." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Machine code", "Binary instructions run directly."],
  ["Assembly language", "Mnemonics; one per machine instruction."],
  ["Assembler", "Assembly to machine code."],
  ["First pass", "Builds the symbol table."],
  ["Second pass", "Translates; replaces labels."],
  ["Symbol table", "Labels and their addresses."],
  ["Opcode / operand", "What to do / what to do it to."],
  ["Groups", "Data movement, I/O, arithmetic, compare, jumps."],
] });
