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
  { h: "1 · One high-level statement, several machine instructions", spec: { label: "A high-level statement is translated into machine code", nodes: [
    { id: "h", x: 20, y: 80, w: 220, h: 70, t: "High-level statement", s: "Sum := First + Second", mono: 1 },
    { id: "t", x: 300, y: 80, w: 130, h: 70, t: "Translator", s: "compiler", c: "var(--warn)", from: 1 },
    { id: "m1", x: 500, y: 10, w: 230, h: 44, t: "0001 00010010", mono: 1, from: 2 }, { id: "m2", x: 500, y: 85, w: 230, h: 44, t: "0100 00010011", mono: 1, from: 3 }, { id: "m3", x: 500, y: 160, w: 230, h: 44, t: "0000 00011010", mono: 1, from: 4 },
  ], edges: [["h", "t"], ["t", "m1"], ["t", "m2"], ["t", "m3"]], steps: [
    { cap: "The programmer writes <b>one</b> easy-to-read statement that adds two numbers.", on: ["h"] },
    { cap: "A <b>translator</b> converts it into machine code the processor can run.", on: ["h", "t"], e: [0] },
    { cap: "First machine instruction: load the first number (<b>LDA</b> in assembly).", on: ["t", "m1"], e: [1] },
    { cap: "Second instruction: add the second number (<b>ADD</b>).", on: ["t", "m2"], e: [2] },
    { cap: "Third instruction: store the result (<b>STO</b>). One high-level statement became several machine code instructions.", on: ["t", "m3"], e: [3] },
  ] } },
  { h: "2 · Why high-level code is portable", spec: { label: "The same program translated for two different computers", nodes: [
    { id: "p", x: 20, y: 85, w: 170, h: 70, t: "High-level program", s: "one version" },
    { id: "ta", x: 270, y: 20, w: 150, h: 60, t: "Translator for A", c: "var(--warn)", from: 1 }, { id: "tb", x: 270, y: 160, w: 150, h: 60, t: "Translator for B", c: "var(--warn)", from: 2 },
    { id: "ca", x: 510, y: 20, w: 220, h: 60, t: "Machine code for A", s: "runs on Computer A", c: "var(--good)", from: 1 }, { id: "cb", x: 510, y: 160, w: 220, h: 60, t: "Machine code for B", s: "runs on Computer B", c: "var(--good)", from: 2 },
  ], edges: [["p", "ta"], ["p", "tb"], ["ta", "ca"], ["tb", "cb"]], steps: [
    { cap: "A program written in a high-level language does not depend on any particular hardware.", on: ["p"] },
    { cap: "Translated for Computer A, it becomes machine code for A's instruction set.", on: ["p", "ta", "ca"], e: [0, 2] },
    { cap: "The <b>same program</b> can also be translated for Computer B. That is what <b>portable</b> means.", on: ["p", "tb", "cb"], e: [1, 3] },
  ] } },
]);

/* ---------- Lab 1: three levels ---------- */
(() => {
  const T = [
    { n: "Add two numbers", h: ["Sum := FirstNumber + SecondNumber"], a: ["LDA First", "ADD Second", "STO Sum"], m: [["0001", "00010010", "12"], ["0100", "00010011", "13"], ["0000", "00011010", "1A"]] },
    { n: "Add three numbers", h: ["Total := A + B + C"], a: ["LDA A", "ADD B", "ADD C", "STO Total"], m: [["0001", "00010010", "12"], ["0100", "00010011", "13"], ["0100", "00010100", "14"], ["0000", "00011010", "1A"]] },
  ];
  const draw = (i) => {
    const t = T[i], ln = (a) => a.map((x) => `<span class="ln">${x}</span>`).join("");
    $("#lvH").innerHTML = ln(t.h); $("#lvA").innerHTML = ln(t.a);
    $("#lvM").innerHTML = t.m.map((x) => `<span class="ln">${x[0]} ${x[1]}    <span class="cm">(operand in hex: ${x[2]})</span></span>`).join("");
    $("#lvV").innerHTML = `High-level: <b>${t.h.length}</b> statement. Assembly: <b>${t.a.length}</b> instructions (usually one per machine code instruction). Machine code: <b>${t.m.length}</b> instructions in binary. The high-level version is shortest and easiest to read, but the low-level versions are tied to one type of computer.`;
  };
  stateBtns($("#lvT"), T.map((t) => t.n), draw); $("#lvT button").click();
})();

/* ---------- Lab 2: portability ---------- */
(() => {
  const L = [["High-level language", 1], ["Assembly language", 0], ["Machine code", 0]];
  const draw = (i) => {
    const ok = L[i][1];
    $("#pbA").innerHTML = `<h3>Computer A</h3><p>The program was written for this computer.</p><p class="pos">✓ Runs${i === 0 ? " (after translation for A)" : ""}</p>`;
    $("#pbB").innerHTML = `<h3>Computer B</h3><p>Different processor, different instruction set.</p><p class="${ok ? "pos" : "neg"}">${ok ? "✓ Runs (after translation for B)" : "✗ Does not run"}</p>`;
    $("#pbV").innerHTML = ok ? "A high-level program is <b>machine independent</b>. A translator for Computer B turns the same source code into B's machine code." : "Low-level code is written for the <b>instruction set of one type of computer</b>, so it has to be rewritten for Computer B. It is <b>machine dependent</b>.";
  };
  stateBtns($("#pbL"), L.map((x) => x[0]), draw); $("#pbL button").click();
})();

/* ---------- Lab 3: choose ---------- */
(() => {
  const Q = [
    ["A school student is learning to program and wants to write a quiz that is easy to debug.", 0, "High-level: easier to read, write and debug."],
    ["A tiny controller in a toy has very little memory and must respond quickly.", 1, "Low-level: it can take up little memory and perform tasks quickly."],
    ["A company wants one app to run on many types of computer.", 0, "High-level: independent of the type of computer (portable)."],
    ["A programmer needs to use a special instruction that only one processor has.", 1, "Low-level: it can use special hardware and machine-dependent instructions."],
    ["A large program will be updated by a team for many years.", 0, "High-level: easier to maintain."],
  ];
  const el = $("#chL"); let i = 0, score = 0;
  const draw = () => { if (i >= Q.length) { el.innerHTML = `<p><b>Done. Score ${score} / ${Q.length}.</b></p><button class="b" id="chr">Try again</button>`; $("#chr").onclick = () => { i = score = 0; draw(); }; return; }
    el.innerHTML = `<p><b>${i + 1}.</b> ${Q[i][0]}</p><div class="ch"><button data-a="0">High-level language</button><button data-a="1">Low-level language</button></div><div class="verdict" id="chv" hidden></div>`;
    $$(".ch button", el).forEach((b) => (b.onclick = () => { const ok = +b.dataset.a === Q[i][1]; $$(".ch button", el).forEach((x) => (x.disabled = true)); b.classList.add(ok ? "ok" : "no"); if (ok) score++; const v = $("#chv"); v.hidden = false; v.innerHTML = (ok ? "✓ " : "✗ ") + Q[i][2] + `<br><button class="b" id="chn" style="margin-top:8px">Next</button>`; $("#chn").onclick = () => { i++; draw(); }; })); };
  draw();
})();

/* ---------- Practise ---------- */
practise([
  { h: "1 · High-level or low-level?", type: "classify", prompt: "Drag each statement to the correct type of language.", buckets: [{ label: "High-level" }, { label: "Low-level" }], items: [
    { text: "Independent of the type of computer", b: 0 }, { text: "Easier to read, write and debug", b: 0 }, { text: "Programs can take longer to execute", b: 0 }, { text: "Examples: Python, Java, C++", b: 0 },
    { text: "Can use special hardware", b: 1 }, { text: "Takes longer to write and debug", b: 1 }, { text: "Includes machine-dependent instructions", b: 1 }, { text: "Examples: assembly, machine code", b: 1 },
  ], done: "High-level for the programmer, low-level for the machine." },
  { h: "2 · True or false?", type: "classify", prompt: "Decide whether each statement is true or false.", buckets: [{ label: "True" }, { label: "False" }], items: [
    { text: "It is more difficult to write a program in a low-level language", b: 0 }, { text: "It is quicker to develop a program using a high-level language", b: 0 }, { text: "Low-level languages are machine dependent", b: 0 },
    { text: "Java is an assembly language", b: 1 }, { text: "An assembler translates a high-level language program", b: 1 }, { text: "Machine code is easy for people to read", b: 1 },
  ], done: "Java is high-level. An assembler translates assembly." },
  { h: "3 · Match the term", type: "match", prompt: "Match each term to its meaning.", pairs: [
    ["Machine code", "Binary instructions the computer understands"], ["Assembly language", "A low-level language that uses mnemonics"], ["High-level language", "A language designed for programmers, closer to English"],
    ["Portable", "Can be used on different types of computer"], ["Machine dependent", "Only works on one type of processor"],
  ] },
  { h: "4 · Quick calculations", type: "calc", qs: [
    { q: "The machine code operand 0001 0010 is shown in hexadecimal as 12. What is the hexadecimal for 0001 1010?", t: ["1A"], ph: "hex", sol: "0001 = 1, 1010 = A, so 1A." },
    { q: "Convert the binary 00010010 to denary.", a: 18, sol: "16 + 2 = 18." },
    { q: "A program has 250 high-level statements. On average each becomes 4 machine code instructions. How many machine code instructions is that?", a: 1000, sol: "250 × 4 = 1000." },
  ] },
  { h: "5 · Multiple choice", type: "quiz", qs: [
    { q: "Why do some programmers write in assembly language?", opts: ["To make use of special hardware", "Because it is portable", "Because it is easier to read", "Because it needs no translator"], a: 0, why: "Also for speed, small size and machine-dependent instructions." },
    { q: "What does portable mean?", opts: ["The program can be used on different types of computer", "The program fits on a USB stick", "The program is very short", "The program needs no translator"], a: 0, why: "High-level programs are often portable." },
    { q: "In which type of language is a program most likely to take up the least primary memory?", opts: ["Low-level", "High-level", "Both the same", "Neither"], a: 0, why: "Low-level code can be written to take up little space." },
    { q: "Which is in machine code?", opts: ["0001 00010010", "LDA First", "Sum := A + B", "print(\"hi\")"], a: 0, why: "Machine code is binary (usually shown in hexadecimal)." },
  ] },
]);

real([
  ["Python and Java in everyday software", "Most apps, websites and games are written in high-level languages. The same Python or Java program can run on several operating systems.", "Examples of high-level languages, and why portability matters."],
  ["Code inside a washing machine", "A small controller may have only a few kilobytes of memory. Parts of its code may be written in a low-level language to save space and respond fast.", "Low-level code can take up little primary memory and run quickly."],
  ["Games consoles and special hardware", "Some of the fastest sections of game code use low-level instructions to make the most of one particular chip.", "Low-level code can use special hardware and machine-dependent instructions."],
  ["Learning with Scratch", "A block-based language like Scratch hides every detail of the processor, so beginners can focus on the problem.", "A high-level language lets the programmer focus on the problem."],
  ["Old programs that cannot move", "Software written in machine code for an old computer often cannot run on a modern one without being rewritten.", "Low-level code is machine dependent."],
]);

exam([
  { cmd: "State", m: 2, q: "Give two advantages of writing a program in a high-level language.", tip: "Easier, portable, quicker.", ans: [["k", "It is easier to read, write, debug and maintain (closer to English)."], ["k", "It is independent of the type of computer (portable)."]], warn: "Saying \"it is faster\". High-level programs can take longer to run." },
  { cmd: "State", m: 2, q: "Give two disadvantages of a high-level language.", tip: "Size, speed, hardware.", ans: [["k", "Programs can be larger and may take longer to execute."], ["k", "It may not be able to make use of special hardware."]], warn: "Repeating the same point twice." },
  { cmd: "Explain", m: 2, q: "Explain why a programmer might choose a low-level language.", tip: "Hardware, speed, memory.", ans: [["k", "To make use of special hardware or machine-dependent instructions."], ["k", "To write code that takes up little memory and runs quickly."]], warn: "Saying low-level is \"easier\"." },
  { cmd: "State", m: 2, q: "What is machine code?", tip: "Binary instructions.", ans: [["k", "The binary instructions (often shown in hexadecimal)"], ["k", "that a computer processor understands directly."]], warn: "Saying it is a \"computer language like Python\"." },
  { cmd: "Explain", m: 3, q: "Explain why high-level programs are said to be portable, but low-level programs are not.", tip: "Instruction set.", ans: [["k", "A high-level program does not depend on the hardware or instruction set."], ["k", "It can be translated for different types of computer."], ["k", "A low-level program is written for the architecture of one type of computer, so it may have to be rewritten for another."]], warn: "Saying it \"fits on any disk\"." },
  { cmd: "State", m: 2, q: "Identify whether each statement is True or False: (a) Java is an assembly language. (b) A low-level language is machine dependent.", tip: "Two answers.", ans: [["k", "(a) False: Java is a high-level language."], ["k", "(b) True."]], warn: "Mixing up assembly and high-level." },
]);

tips([
  "<b>High-level = for people, low-level = for the machine.</b> Use that to organise every answer.",
  "<b>Portable</b> means can run on different types of computer. Only high-level is portable.",
  "<b>Four reasons for low-level:</b> special hardware, special instructions, small memory, speed.",
  "<b>Four advantages of high-level:</b> easier to read, write, debug and maintain.",
  "<b>One high-level statement</b> becomes several machine code instructions.",
  "<b>Machine code is binary,</b> shown in hexadecimal to make it readable.",
  "<b>Do not say \"high-level is faster\".</b> The machine code made from it can be longer and run slower.",
  "<b>Name an example</b> of each type: Python for high-level, assembly for low-level.",
], [
  ["Program", "A list of instructions that enable a computer to perform a specific task."], ["High-level language", "A programming language designed for programmers, independent of the computer's hardware."],
  ["Low-level language", "A language related to the architecture and hardware of a particular type of computer."], ["Machine code", "The binary instructions that a computer understands directly."],
  ["Assembly language", "A low-level language using mnemonics, which must be translated into machine code."], ["Portable", "Able to be used on different types of computer."],
  ["Machine dependent", "Works only on a particular type of computer or processor."], ["Instruction set", "The set of machine code instructions a processor can carry out."],
]);
