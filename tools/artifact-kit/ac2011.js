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
  const lines = ["LDM #500", "LDD 500", "LDI 500"];
  const draw = (s) => {
    const c = Math.round(s.i); let o = "";
    o += codeList(30, 40, lines, c - 1, 1, 34, 190);
    o += memCell(430, 40, 100, 20, c >= 3 ? "cell-ok" : "f3", 1) + memCell(430, 100, 500, 100, "f3", 1);
    o += regBox(250, 170, "ACC", c === 0 ? "" : c === 1 ? 500 : c === 2 ? 100 : 20, "f2", 1);
    o += SV.text(430, 32, "memory", "sm") + SV.text(30, 32, "program", "sm");
    if (c === 1) o += arrow(140, 108 - 34, 250, 195, "r", "c1", 1);
    if (c === 2) o += arrow(430, 120, 372, 190, "l", "c2", 1) + SV.text(596, 125, "read address 500", "sm");
    if (c === 3) o += arrow(505, 140, 505, 124, "u", "c3", 1) + arrow(430, 60, 372, 185, "l", "c2", 1) + SV.text(596, 125, "1: read address 500 = 100", "sm") + SV.text(596, 65, "2: read address 100 = 20", "sm");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 250, label: "Immediate, direct and indirect addressing", base: { i: 0 }, draw, tween: 500, dwell: 4000, steps: [
    { cap: "Address <b>500</b> holds <b>100</b> and address <b>100</b> holds <b>20</b>. Three instructions use the same operand, 500. ACC is empty.", s: { i: 0 } },
    { cap: "<code>LDM #500</code> is <b>immediate</b>: the operand (marked with #) is the data. ACC = <b>500</b>. No memory is read.", s: { i: 1 } },
    { cap: "<code>LDD 500</code> is <b>direct</b>: the operand is the address that holds the data. Read address 500: ACC = <b>100</b>.", s: { i: 2 } },
    { cap: "<code>LDI 500</code> is <b>indirect</b>: address 500 holds <b>100</b>, and that is itself an address. Read address 100: ACC = <b>20</b>. Two reads.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const c = Math.round(s.i); let o = "";
    for (let k = 0; k < 5; k++) o += memCell(430, 30 + k * 44, 200 + k, [11, 22, 33, 44, 55][k], c >= 3 && k === 3 ? "cell-ok" : "f3", 1);
    o += SV.text(430, 22, "array stored from address 200", "sm");
    o += regBox(40, 40, "Index register IX", c >= 1 ? 3 : "", "f1", c >= 1 ? 1 : 0.35, 200);
    o += SV.text(40, 130, "LDX 200", "lbl bd", { style: "font-family:var(--mono);font-size:20px" });
    if (c >= 2) o += SV.text(40, 165, "200 + IX = 200 + 3 = 203", "lbl", { style: "font-family:var(--mono);font-size:16px" });
    if (c >= 3) o += arrow(300, 160, 430, 142 + 22, "r", "c2", 1) + regBox(40, 195, "ACC", 44, "f2", 1);
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 260, label: "Indexed addressing", base: { i: 0 }, draw, tween: 500, dwell: 4000, steps: [
    { cap: "An array is stored from address <b>200</b>. To read any element, use one instruction, <code>LDX 200</code>, and change the index register.", s: { i: 0 } },
    { cap: "The <b>index register (IX)</b> holds <b>3</b>: the position of the element wanted (counting from 0).", s: { i: 1 } },
    { cap: "<b>Indexed addressing</b> adds IX to the operand: 200 + 3 = <b>203</b>.", s: { i: 2 } },
    { cap: "The contents of address 203 are loaded: ACC = <b>44</b>. Add 1 to IX and the same instruction reads the next element.", s: { i: 3 } }] });
})();

(function () {
  const L = ["1049  LDD Count", "1050  JMR +4", "1051  ADD One", "1052  STO Count", "1053  OUT", "1054  END"];
  const draw = (s) => {
    const c = Math.round(s.i); let o = codeList(30, 30, L, c === 0 ? -1 : c === 1 ? 1 : 5, 1, 34, 260);
    o += regBox(400, 60, "PC (current instruction)", c === 0 ? 1049 : c === 1 ? 1050 : 1054, "f1", 1, 240);
    if (c >= 1) o += SV.text(400, 160, "operand = offset +4", "lbl", { style: "font-family:var(--mono);font-size:16px" });
    if (c >= 2) o += SV.text(400, 190, "1050 + 4 = 1054", "lbl bd", { style: "font-family:var(--mono);font-size:18px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 250, label: "Relative addressing", base: { i: 0 }, draw, tween: 500, dwell: 4000, steps: [
    { cap: "The program counter (PC) holds the address of the current instruction. A <b>relative</b> jump gives an <b>offset</b>, not a fixed address.", s: { i: 0 } },
    { cap: "At address <b>1050</b> the instruction is a relative jump of <b>+4</b>.", s: { i: 1 } },
    { cap: "The next address is the current address plus the offset: 1050 + 4 = <b>1054</b>, so the three instructions in between are skipped.", s: { i: 2 } },
    { cap: "If this block of code were loaded at a different address, the jump would still land in the right place, because the offset is measured from where the instruction is. That is why relative addressing makes code <b>position-independent</b>.", s: { i: 2 } }] });
})();

(function () {
  const L = ["total = 0", "count = 1", "while count <= 3:", "    total = total + count", "    count = count + 1"];
  const seq = [[0, 0, 0, -1], [0, 1, 0, -1], [1, 0, 1, 2], [3, 0, 1, 3], [4, 0, 2, 4], [3, 1, 2, 3], [4, 1, 3, 4], [3, 3, 3, 3], [4, 3, 4, 4]];
  const draw = (s) => {
    const k = Math.round(s.i), st = [["", ""], ["0", ""], ["0", "1"], ["0", "1"], ["1", "1"], ["1", "2"], ["3", "2"], ["3", "3"], ["6", "4"]][k], hl = [-1, 0, 1, 3, 4, 3, 4, 3, 4][k];
    let o = codeList(30, 30, L, hl, 1, 34, 300);
    o += regBox(420, 50, "total", st[0], "f1", 1) + regBox(560, 50, "count", st[1], "f2", 1);
    o += SV.text(420, 140, "the state changes one command at a time", "sm");
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 230, label: "An imperative program changing state", base: { i: 0 }, draw, tween: 400, dwell: 2500, steps: [
    { cap: "A short program with two variables. Nothing has run yet, so there is no state.", s: { i: 0 } },
    { cap: "<code>total = 0</code>: the first command sets the state.", s: { i: 1 } },
    { cap: "<code>count = 1</code>: executed next, in the order written.", s: { i: 2 } },
    { cap: "The loop adds count to total: total becomes <b>1</b>.", s: { i: 4 } },
    { cap: "count becomes <b>2</b>. Each line changes something: this is what makes it imperative.", s: { i: 5 } },
    { cap: "Second pass: total becomes <b>3</b>.", s: { i: 6 } },
    { cap: "count becomes <b>3</b>.", s: { i: 7 } },
    { cap: "Third pass: total becomes <b>6</b>, count becomes <b>4</b>, and the loop condition now fails.", s: { i: 8 } }] });
})();

/* Lab 1: addressing explorer */
(function () {
  const M = { 20: 7, 31: 9, 100: 20, 101: 31, 102: 42, 103: 53, 104: 64, 200: 101, 201: 202, 300: 100, 500: 100 };
  const modes = [["Immediate", "LDM #"], ["Direct", "LDD "], ["Indirect", "LDI "], ["Indexed", "LDX "]];
  let m = 2, op = 500, ix = 1;
  const cell = (a) => (a in M ? M[a] : 0);
  const paint = () => {
    $$("#mB button").forEach((b, i) => b.classList.toggle("pri", i === m));
    let addr = "none", val = op, why = "";
    if (m === 0) { why = `The operand ${op} is the value, so no memory is read.`; }
    if (m === 1) { addr = op; val = cell(op); why = `Read address ${op}: it holds ${val}.`; }
    if (m === 2) { const a2 = cell(op); addr = op + " then " + a2; val = cell(a2); why = `Read address ${op}: it holds ${a2}. Use ${a2} as an address: it holds ${val}.`; }
    if (m === 3) { addr = op + ix; val = cell(op + ix); why = `Address = ${op} + IX (${ix}) = ${op + ix}, which holds ${val}.`; }
    $("#a1").textContent = modes[m][1] + op; $("#a2").textContent = addr; $("#a3").textContent = val; $("#av").textContent = why;
    $("#mX").style.display = m === 3 ? "" : "none";
    const keys = Object.keys(M).map(Number).sort((a, b) => a - b);
    $("#mS").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Address</th>' + keys.map((k) => `<td>${k}</td>`).join("") + "</tr><tr><th>Contents</th>" + keys.map((k) => `<td>${M[k]}</td>`).join("") + "</tr></table></div>";
  };
  $("#mB").innerHTML = modes.map((x, i) => `<button class="b" data-i="${i}">${x[0]}</button>`).join("");
  $$("#mB button").forEach((b) => (b.onclick = () => { m = +b.dataset.i; if (m === 3 && op > 200) op = 100; if (m === 2 && ![100, 200, 300, 500].includes(op)) op = 500; paint(); }));
  const opts = [100, 101, 200, 300, 500];
  Lib.slider($("#mO"), { id: "mos", label: "Operand ", min: 0, max: opts.length - 1, value: 4, fmt: (x) => opts[x], onInput: (v) => { op = opts[v]; paint(); } });
  Lib.slider($("#mX"), { id: "mxs", label: "Index register IX ", min: 0, max: 4, value: ix, fmt: (x) => x, onInput: (v) => { ix = v; paint(); } });
  paint();
})();

/* Lab 2: step through the assembly program */
(function () {
  const prog = ["LDM #20", "STO Twenty", "LDI Y", "ADD Twenty", "STO Z", "END"];
  const mem0 = () => ({ Twenty: 0, Y: 700, Z: 0, 700: 35 });
  let pc = 0, acc = "", mem = mem0();
  const paint = (msg) => {
    $("#pS").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Next</th><th>Instruction</th><th>ACC</th><th>Twenty</th><th>Y</th><th>Z</th><th>addr 700</th></tr><tr><td>' + (pc < prog.length ? pc + 1 : "-") + "</td><td>" + (pc < prog.length ? prog[pc] : "finished") + "</td><td>" + acc + "</td><td>" + mem.Twenty + "</td><td>" + mem.Y + "</td><td>" + mem.Z + "</td><td>" + mem[700] + "</td></tr></table></div>";
    $("#pv").textContent = msg || "Press Step to run the first instruction.";
  };
  $("#pN").onclick = () => {
    if (pc >= prog.length) return;
    const ins = prog[pc]; let msg = "";
    if (ins === "LDM #20") { acc = 20; msg = "LDM #20: immediate, ACC = 20."; }
    else if (ins === "STO Twenty") { mem.Twenty = acc; msg = "STO Twenty: the 20 in ACC is stored at the labelled address, so it can be added later."; }
    else if (ins === "LDI Y") { acc = mem[mem.Y]; msg = `LDI Y: Y holds ${mem.Y}, so ACC takes the contents of address ${mem.Y}, which is ${acc}.`; }
    else if (ins === "ADD Twenty") { acc = acc + mem.Twenty; msg = `ADD Twenty: ACC = 35 + 20 = ${acc}.`; }
    else if (ins === "STO Z") { mem.Z = acc; msg = `STO Z: Z now holds ${acc}.`; }
    else msg = "END: the program stops. Z = 55, the value pointed to by Y plus 20.";
    pc++; paint(msg);
  };
  $("#pR").onclick = () => { pc = 0; acc = ""; mem = mem0(); paint(); };
  paint();
})();

btnTable("eB", "eO", [
  ["Low-level", "Instructions from the processor's instruction set; direct control of registers and memory", "Assembly language, e.g. LDD, ADD, STO", "Small fast programs for embedded devices and drivers; hard to write and not portable", "Saying it is 'the language with no loops'"],
  ["Imperative (procedural)", "A sequence of commands, in the order written, that change the program state; procedures and functions", "Python, Pascal, C-style code with assignments and loops", "Most programs; structured and easy to follow", "Defining it only by 'uses IF and loops'"],
  ["Object-oriented", "Objects created from classes; data and methods together; inheritance, polymorphism, encapsulation", "Java, Python classes", "Large systems with many related things to model", "Mixing up class (the template) and object (an instance)"],
  ["Declarative", "States what result is wanted using facts and rules; the system works out how, by satisfying a goal", "Prolog, SQL", "Queries over knowledge: family trees, databases, expert systems", "Calling it 'code without variables'"]
], ["Paradigm", "Key idea", "Example", "Typical use", "Trap"]);
Lib.classify($("#cl1"), { prompt: "Which paradigm does each piece of code show?", buckets: [{"label": "Low-level"}, {"label": "Imperative"}, {"label": "Object-oriented"}, {"label": "Declarative"}], items: [{"text": "LDM #5 then ADD Total then STO Total", "b": 0}, {"text": "while x < 10: x = x + 1", "b": 1}, {"text": "class Dog: def __init__(self, name): self.name = name", "b": 2}, {"text": "parent(sam, tom). father(X, Y) :- parent(X, Y), male(X).", "b": 3}, {"text": "JMP Loop", "b": 0}, {"text": "for item in items: total = total + item", "b": 1}, {"text": "class Circle(Shape):", "b": 2}, {"text": "female(ethel). ?- female(X).", "b": 3}], done: "Opcodes: low-level. Assignments in order: imperative. class: object-oriented. Facts, rules and a query: declarative." });
Lib.classify($("#cl2"), { prompt: "Which addressing mode is each description?", buckets: [{"label": "Immediate"}, {"label": "Direct"}, {"label": "Indirect"}, {"label": "Indexed"}, {"label": "Relative"}], items: [{"text": "The operand is the value to use", "b": 0}, {"text": "The operand is the address that holds the value", "b": 1}, {"text": "The operand is the address of a location that holds the address of the value", "b": 2}, {"text": "The address used is the operand plus the contents of the index register", "b": 3}, {"text": "An offset is added to the address of the current instruction", "b": 4}, {"text": "LDM #7", "b": 0}, {"text": "LDD 7", "b": 1}, {"text": "LDI 7", "b": 2}, {"text": "Suits reading each element of an array in turn", "b": 3}], done: "Immediate: the data. Direct: one read. Indirect: two reads. Indexed: operand + IX. Relative: offset from where the instruction is." });
Lib.order($("#o1"), { prompt: "Put the steps for LDI 500 in order.", items: ["Fetch the instruction LDI 500", "Read the contents of address 500", "Use that value as a second address", "Read the contents of the second address", "Store that value in ACC"], done: "Two reads: the address, then the value." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Opcode", "The part of an instruction that says what to do"], ["Operand", "The part of an instruction that gives the data or where it is"], ["Addressing mode", "The way the operand is used to find the data"], ["Assembler", "Translates assembly language into machine code"], ["Index register", "A register whose contents are added to the operand to give the address"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Address 40 holds 7 and address 7 holds 90. What does LDM #40 put in ACC?", "a": 40, "unit": "", "tol": 0.01, "hint": "Immediate: the operand is the data.", "sol": "<b>40</b>."},
  {"q": "Address 40 holds 7 and address 7 holds 90. What does LDD 40 put in ACC?", "a": 7, "unit": "", "tol": 0.01, "hint": "Direct: the contents of address 40.", "sol": "<b>7</b>."},
  {"q": "Address 40 holds 7 and address 7 holds 90. What does LDI 40 put in ACC?", "a": 90, "unit": "", "tol": 0.01, "hint": "Indirect: address 40 holds 7, then read address 7.", "sol": "<b>90</b>."},
  {"q": "IX holds 5. Which address does LDX 300 read?", "a": 305, "unit": "", "tol": 0.01, "hint": "300 + 5.", "sol": "<b>305</b>."},
  {"q": "A relative jump of +6 is at address 2000. At which address does the program continue?", "a": 2006, "unit": "", "tol": 0.01, "hint": "Current address plus the offset.", "sol": "<b>2006</b>."},
  {"q": "ACC holds 10. Address 20 holds 4. What does ACC hold after ADD 20?", "a": 14, "unit": "", "tol": 0.01, "hint": "10 + 4.", "sol": "<b>14</b>."},
  {"q": "Address 8 holds 12. After LDD 8 then ADD 8, what does ACC hold?", "a": 24, "unit": "", "tol": 0.01, "hint": "12, then 12 + 12.", "sol": "<b>24</b>."},
  {"q": "How many memory reads does LDI need to get the data?", "a": 2, "unit": "reads", "tol": 0.01, "hint": "The address, then the value.", "sol": "<b>2</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is an addressing mode?", opts: ["The speed of the processor", "The way the operand is used to find the data", "The type of memory used", "The size of an instruction"], a: 1, why: "It is how the operand is interpreted." },
  { q: "Which mode puts the operand itself into the register?", opts: ["Direct", "Indirect", "Immediate", "Indexed"], a: 2, why: "Immediate: the operand is the data." },
  { q: "A programmer wants to read every element of an array with one instruction in a loop. Which mode suits?", opts: ["Immediate", "Indexed", "Direct", "Relative"], a: 1, why: "Indexed adds a changing index to the start address." },
  { q: "Which description fits an imperative program?", opts: ["States the result wanted using facts and rules", "A sequence of commands that change the program state", "A set of classes and objects", "Instructions of the processor"], a: 1, why: "That is the definition the mark scheme uses." },
  { q: "What is a drawback of low-level programs?", opts: ["They run slowly", "They are hard to write and not portable", "They cannot control memory", "They cannot use registers"], a: 1, why: "They are processor-specific and hard to maintain." },
  { q: "Which paradigm is Prolog?", opts: ["Low-level", "Imperative", "Object-oriented", "Declarative"], a: 3, why: "Prolog uses facts, rules and queries." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Programming paradigm", "A style of programming, a way of organising a program."],
  ["Low-level", "Uses the processor's instruction set. Direct control, not portable."],
  ["Imperative", "Sequence of commands, in order, changing the program state."],
  ["Immediate", "The operand is the value. LDM #n."],
  ["Direct", "The operand is the address holding the value. LDD."],
  ["Indirect", "The address holds another address; read twice. LDI."],
  ["Indexed", "Address = operand + IX. Arrays."],
  ["Relative", "Address = current address + offset. Position-independent."],
] });
