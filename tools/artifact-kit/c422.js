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
  { h: "1 · Running LDA, ADD, STO", spec: { label: "The accumulator holds the value being worked on", nodes: [
    { id: "f", x: 20, y: 20, w: 150, h: 64, t: "First", s: "7", c: "var(--accent)" },
    { id: "s", x: 20, y: 105, w: 150, h: 64, t: "Second", s: "5" },
    { id: "m", x: 20, y: 190, w: 150, h: 64, t: "Sum", s: "?" , c: "var(--good)" },
    { id: "a", x: 330, y: 85, w: 170, h: 90, t: "Accumulator", s: "empty", c: "var(--warn)" },
    { id: "i", x: 570, y: 85, w: 170, h: 90, t: "Instruction", s: "-", mono: 1 },
  ], edges: [["f", "a"], ["s", "a"], ["a", "m", "dash"]], steps: [
    { cap: "Memory holds <b>First = 7</b> and <b>Second = 5</b>. The accumulator is empty and Sum is not yet known.", on: ["f", "s"] },
    { cap: "<b>LDA First</b>: the value of First (7) is loaded into the accumulator.", on: ["f", "a", "i"], e: [0], set: { a: { s: "7" }, i: { s: "LDA First" } } },
    { cap: "<b>ADD Second</b>: the value of Second (5) is added to what is in the accumulator. 7 + 5 = 12.", on: ["s", "a", "i"], e: [1], set: { a: { s: "12" }, i: { s: "ADD Second" } } },
    { cap: "<b>STO Sum</b>: the accumulator's value is stored in the variable Sum.", on: ["a", "m", "i"], e: [2], set: { a: { s: "12" }, m: { s: "12" }, i: { s: "STO Sum" } } },
  ] } },
  { h: "2 · The assembler", spec: { label: "Assembly is translated into machine code", nodes: [
    { id: "a", x: 20, y: 70, w: 200, h: 90, t: "Assembly program", s: ["LDA First", "ADD Second", "STO Sum"], mono: 1 },
    { id: "t", x: 290, y: 85, w: 150, h: 60, t: "Assembler", c: "var(--warn)", from: 1 },
    { id: "m", x: 520, y: 70, w: 210, h: 90, t: "Machine code", s: ["0001 00010010", "0100 00010011", "0000 00011010"], mono: 1, c: "var(--good)", from: 2 },
  ], edges: [["a", "t"], ["t", "m"]], steps: [
    { cap: "The programmer writes the program using <b>mnemonics</b>.", on: ["a"] },
    { cap: "An <b>assembler</b> translates it. Usually one assembly instruction becomes one machine code instruction.", on: ["a", "t"], e: [0] },
    { cap: "The machine code is produced. It can now be run again and again <b>without re-assembling</b>.", on: ["t", "m"], e: [1] },
  ] } },
]);

/* ---------- Lab 1: stepper ---------- */
(() => {
  const P = [["LDA", "First"], ["ADD", "Second"], ["STO", "Sum"]]; let pc, acc, sum;
  const paint = () => { $("#mAcc").textContent = acc === null ? "-" : acc; $("#mSum").textContent = sum === null ? "?" : sum; $("#mProg").innerHTML = P.map((p, i) => `<span class="ln ${i === pc - 1 ? "on" : i < pc ? "done" : ""}">${p[0]} ${p[1]}</span>`).join(""); };
  const reset = () => { pc = 0; acc = null; sum = null; paint(); $("#mV").textContent = "Press Step to run LDA First."; };
  const step = () => {
    if (pc >= P.length) { $("#mV").textContent = "The program has finished."; return; }
    const F = +$("#mF").value, S = +$("#mS").value, [op] = P[pc]; pc++;
    if (op === "LDA") { acc = F; $("#mV").textContent = `LDA First: the accumulator now holds ${F}.`; }
    else if (op === "ADD") { acc += S; $("#mV").textContent = `ADD Second: ${acc - S} + ${S} = ${acc}, held in the accumulator.`; }
    else { sum = acc; $("#mV").innerHTML = `STO Sum: Sum = ${sum}. <b>Finished.</b>`; }
    paint();
  };
  $("#mStep").onclick = step; $("#mRun").onclick = () => { reset(); for (let i = 0; i < 3; i++) step(); }; $("#mRes").onclick = reset;
  ["#mF", "#mS"].forEach((i) => ($(i).oninput = reset)); reset();
})();

/* ---------- Lab 2: write and assemble ---------- */
(() => {
  const OP = { LDA: "0001", ADD: "0100", STO: "0000" }, AD = { First: "00010010", Second: "00010011", Sum: "00011010" }, el = $("#wrL");
  const mkSel = (opts, v) => `<select class="sel">${opts.map((o) => `<option${o === v ? " selected" : ""}>${o}</option>`).join("")}</select>`;
  el.innerHTML = [1, 2, 3, 4].map((n, i) => `<div class="row" style="margin-bottom:6px"><b style="width:1.5em">${n}</b>${mkSel(["(blank)", "LDA", "ADD", "STO"], "(blank)")}${mkSel(["First", "Second", "Sum"], "First")}</div>`).join("");
  const rows = $$(".row", el);
  $("#wrGo").onclick = () => {
    const prog = rows.map((r) => $$("select", r).map((s) => s.value)).filter((p) => p[0] !== "(blank)");
    $("#wrM").innerHTML = prog.length ? prog.map((p) => `<span class="ln">${OP[p[0]]} ${AD[p[1]]}   <span class="cm">${p[0]} ${p[1]}</span></span>`).join("") : "";
    let acc = null, mem = { First: 7, Second: 5, Sum: null }, err = "";
    prog.forEach((p) => { if (p[0] === "LDA") acc = mem[p[1]]; else if (p[0] === "ADD") { if (acc === null || mem[p[1]] === null) err = "ADD used before there is a value in the accumulator."; else acc += mem[p[1]]; } else { mem[p[1]] = acc; } });
    const ok = !err && mem.Sum === 12;
    $("#wrV").innerHTML = (ok ? "✓ " : "✗ ") + (err || (ok ? "First (7) + Second (5) = 12 is stored in Sum. Correct." : `Sum holds ${mem.Sum === null ? "nothing" : mem.Sum}, not 12. Load First, add Second, then store in Sum.`));
  };
})();

/* ---------- Practise ---------- */
practise([
  { h: "1 · Match the mnemonic", type: "match", prompt: "Match each mnemonic or term to its meaning.", pairs: [
    ["LDA", "Load the value of a variable into the accumulator"], ["ADD", "Add the value of a variable to the value in the accumulator"], ["STO", "Store the accumulator's value in a variable"],
    ["Assembler", "Translates assembly language into machine code"], ["Mnemonic", "A short, readable code used in place of a binary instruction"],
  ] },
  { h: "2 · Put the program in order", type: "order", prompt: "Order the instructions so that Sum = First + Second.", items: ["LDA First", "ADD Second", "STO Sum"], done: "Load, add, store." },
  { h: "3 · Assembly or machine code?", type: "classify", prompt: "Drag each item to the correct language.", buckets: [{ label: "Assembly" }, { label: "Machine code" }], items: [
    { text: "LDA First", b: 0 }, { text: "STO Sum", b: 0 }, { text: "Uses mnemonics", b: 0 }, { text: "Needs an assembler", b: 0 },
    { text: "0001 00010010", b: 1 }, { text: "Binary instructions", b: 1 }, { text: "Run directly by the processor", b: 1 },
  ], done: "Assembly is readable, machine code is binary." },
  { h: "4 · Trace it", type: "calc", qs: [
    { q: "First = 6 and Second = 9. After LDA First, ADD Second and STO Sum, what is stored in Sum?", a: 15, sol: "6 + 9 = 15." },
    { q: "First = 20, Second = 5. What does the accumulator hold after LDA First and ADD Second?", a: 25, sol: "20 + 5 = 25." },
    { q: "A program is: LDA A, ADD B, ADD C, STO Total with A = 4, B = 3, C = 10. What is Total?", a: 17, sol: "4 + 3 + 10 = 17." },
    { q: "How many machine code instructions will the four-instruction program above produce (one per assembly instruction)?", a: 4, sol: "Assembly is usually translated one-to-one, so 4." },
  ] },
  { h: "5 · Multiple choice", type: "quiz", qs: [
    { q: "What does STO do?", opts: ["Stores the accumulator's value in a variable", "Stops the program", "Subtracts a number", "Starts the assembler"], a: 0, why: "STO writes the accumulator back to memory." },
    { q: "Which program translates assembly into machine code?", opts: ["Assembler", "Compiler", "Interpreter", "Linker"], a: 0, why: "An assembler is the translator for assembly language." },
    { q: "Why might a programmer choose assembly?", opts: ["To save memory and run quickly", "To make the program portable", "Because it is easy to debug", "To avoid using the processor"], a: 0, why: "Assembly can be small and fast but is not portable." },
    { q: "Which is true of assembly language?", opts: ["It is machine dependent", "It works on every processor", "It is high-level", "It needs no translation"], a: 0, why: "It relates to one type of computer." },
  ] },
]);

real([
  ["Games and special effects", "Some graphics routines in games are hand-written in low-level code so they run as fast as possible on a particular graphics chip.", "Assembly makes use of special hardware and can perform a task very quickly."],
  ["Tiny microcontrollers", "A chip in a thermostat may have only a small memory, so a programmer may write assembly to fit the program in.", "Assembly can take up little space in primary memory."],
  ["Reverse engineering and debugging", "Security researchers and engineers often read assembly to see exactly what a program asks the processor to do.", "Shows assembly is readable compared with binary."],
  ["Early computers", "Early programmers had to write directly in machine code or assembly. High-level languages were invented to make this easier.", "Why high-level languages are easier to read, write and debug."],
  ["Different chips, different assembly", "A phone chip and a laptop chip have different instruction sets, so they use different assembly languages.", "Assembly is machine dependent."],
]);

exam([
  { cmd: "State", m: 3, q: "An assembly program has the instructions LDA, ADD and STO. State what each one does.", tip: "One mark each.", ans: [["k", "LDA loads the value of a variable into the accumulator."], ["k", "ADD adds the value of a variable to the value in the accumulator."], ["k", "STO stores the value in the accumulator in a variable."]], warn: "Saying ADD \"adds two variables\". It adds to the accumulator." },
  { cmd: "Explain", m: 2, q: "Explain why a programmer might choose to write a program in assembly language.", tip: "Two of the four reasons.", ans: [["k", "To make use of special hardware or machine-dependent instructions."], ["k", "To write code that takes up little memory or performs a task very quickly."]], warn: "Saying it is easier to write." },
  { cmd: "State", m: 2, q: "What is an assembler?", tip: "Translator, assembly, machine code.", ans: [["k", "A program that translates a program written in assembly language"], ["k", "into machine code."]], warn: "Confusing it with a compiler." },
  { cmd: "Describe", m: 2, q: "Describe one difference between assembly language and machine code.", tip: "Readable vs binary.", ans: [["k", "Assembly uses mnemonics that people can read, whereas machine code is binary."], ["k", "Assembly needs to be translated by an assembler, machine code can be run directly."]], warn: "Saying one is high-level." },
  { cmd: "Calculate", m: 3, q: "First = 8 and Second = 11. Trace LDA First, ADD Second, STO Sum. State the accumulator after each instruction.", tip: "Three values.", ans: [["k", "After LDA First: 8"], ["k", "After ADD Second: 19"], ["k", "After STO Sum: accumulator still 19, and Sum = 19"]], warn: "Forgetting that the accumulator keeps its value after STO." },
  { cmd: "State", m: 2, q: "Give two disadvantages of writing in assembly language.", tip: "Time, difficulty, portability.", ans: [["k", "It takes longer to write and debug."], ["k", "It is harder to understand and only works on one type of computer."]], warn: "Saying it is \"slow to run\"." },
]);

tips([
  "<b>Know the three mnemonics:</b> LDA loads, ADD adds, STO stores. Say \"the accumulator\" in each.",
  "<b>Trace carefully.</b> Write the accumulator value after every instruction.",
  "<b>Assembly is low-level.</b> It is machine dependent and not portable.",
  "<b>Four reasons for assembly:</b> special hardware, machine-dependent instructions, small memory, speed.",
  "<b>One-to-one:</b> usually one assembly instruction becomes one machine code instruction.",
  "<b>An assembler translates assembly.</b> A compiler translates a high-level language.",
  "<b>The machine code is what runs.</b> You do not need the assembler to run it again.",
  "<b>Do not say assembly is high-level.</b> Java is high-level, and it is not assembly.",
], [
  ["Assembly language", "A low-level language that uses mnemonics and has to be translated into machine code."], ["Mnemonic", "A short readable code that stands for an instruction, such as LDA."],
  ["Accumulator", "A register in the processor that holds the value being worked on."], ["LDA", "Load the value of a variable into the accumulator."],
  ["ADD", "Add the value of a variable to the value in the accumulator."], ["STO", "Store the value in the accumulator in a variable."],
  ["Assembler", "A program that translates assembly language into machine code."], ["Machine dependent", "Only runs on a particular type of computer or processor."],
]);
