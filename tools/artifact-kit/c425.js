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

/* scenario chooser: choose(el, ["Option A","Option B"], [[scenario, correctIndex, explanation], ...]) */
function choose(el, O, Q) {
  let i = 0, score = 0;
  const draw = () => {
    if (i >= Q.length) { el.innerHTML = `<p><b>Done. Score ${score} / ${Q.length}.</b></p><button class="b" data-r>Try again</button>`; $("[data-r]", el).onclick = () => { i = score = 0; draw(); }; return; }
    el.innerHTML = `<p><b>${i + 1}.</b> ${Q[i][0]}</p><div class="ch">${O.map((o, k) => `<button data-a="${k}">${o}</button>`).join("")}</div><div class="verdict" data-v hidden></div>`;
    $$(".ch button", el).forEach((b) => (b.onclick = () => { const ok = +b.dataset.a === Q[i][1]; $$(".ch button", el).forEach((x) => (x.disabled = true)); b.classList.add(ok ? "ok" : "no"); if (ok) score++; const v = $("[data-v]", el); v.hidden = false; v.innerHTML = (ok ? "✓ " : "✗ ") + Q[i][2] + `<br><button class="b" data-n style="margin-top:8px">Next</button>`; $("[data-n]", el).onclick = () => { i++; draw(); }; }));
  };
  draw();
}

/* ---------- Watch ---------- */
watch([
  { h: "From typing code to a working program", spec: { label: "An IDE puts the tools in one place", nodes: [
    { id: "e", x: 20, y: 20, w: 200, h: 70, t: "Code editor", s: "colour coding, auto-completion" },
    { id: "d", x: 290, y: 20, w: 200, h: 70, t: "Error diagnostics", s: "underlines mistakes", c: "var(--bad)" },
    { id: "t", x: 560, y: 20, w: 170, h: 70, t: "Translator", s: "compiler / interpreter", c: "var(--warn)" },
    { id: "r", x: 560, y: 170, w: 170, h: 70, t: "Program runs", s: "" },
    { id: "g", x: 290, y: 170, w: 200, h: 70, t: "Debugger", s: "step, breakpoint, variables", c: "var(--good)" },
  ], edges: [["e", "d"], ["d", "t"], ["t", "r"], ["r", "g"], ["g", "e", "dash"]], steps: [
    { cap: "The programmer types in the <b>code editor</b>. Words are colour-coded and laid out clearly (<b>prettyprinting</b>), and <b>auto-completion</b> offers names and reserved words.", on: ["e"] },
    { cap: "<b>Dynamic error checking</b> underlines a mistake as it is typed and suggests a correction.", on: ["e", "d"], e: [0] },
    { cap: "The built-in <b>translator</b> (compiler and/or interpreter) turns the code into something that can run.", on: ["d", "t"], e: [1] },
    { cap: "The program runs inside the IDE's runtime environment. The result does not look right.", on: ["t", "r"], e: [2] },
    { cap: "The <b>debugger</b> lets the programmer single-step, use a breakpoint and watch the variables to find the logic error.", on: ["r", "g"], e: [3] },
    { cap: "The programmer goes back to the editor, fixes the code and tries again, without leaving the IDE.", on: ["g", "e"], e: [4] },
  ] } },
]);

/* ---------- Lab 1: editor ---------- */
(() => {
  const KW = ["for", "in", "range", "print", "if", "while", "input"]; let fixed;
  const hi = (s) => esc(s).replace(/("[^"]*")/g, '<span class="str">$1</span>').replace(/\b(\d+)\b/g, '<span class="num">$1</span>').replace(new RegExp("\\b(" + KW.join("|") + ")\\b", "g"), '<span class="kwd">$1</span>').replace(/(#.*)$/, '<span class="cm">$1</span>');
  const code = () => ['name = input("Your name? ")', fixed ? 'print("Hello " + name)' : 'prnt("Hello " + name)', "for counter in range(3):", '    print("Hi")'];
  const draw = () => {
    const P = $("#edP").checked, E = $("#edE").checked;
    $("#edC").innerHTML = code().map((l, i) => `<span class="ln ${E && i === 1 && !fixed ? "err" : ""}"><span class="cm">${i + 1}  </span>${P ? hi(l) : esc(l)}${E && i === 1 && !fixed ? '   <span class="neg">⚠ prnt is not defined. Did you mean "print"?</span>' : ""}</span>`).join("");
    $("#edV").innerHTML = fixed ? "No errors. Prettyprinting colours the strings, numbers and keywords, and keeps the layout clear." : E ? "Dynamic error checking marks line 2 <b>as you type</b> and suggests a correction, before the program is run." : "Error checking is off. The mistake on line 2 would only be found when the program is translated or run.";
  };
  $("#edP").onchange = $("#edE").onchange = draw; $("#edF").onclick = () => { fixed = true; draw(); }; $("#edR").onclick = () => { fixed = false; draw(); }; fixed = false; draw();
})();

/* ---------- Lab 2: auto-completion ---------- */
(() => {
  const W = ["print", "private", "range", "return", "total", "counter", "name", "input", "int", "import"]; const I = $("#acI");
  const upd = () => { const v = I.value.trim().toLowerCase(), m = v ? W.filter((w) => w.startsWith(v)) : []; $("#acL").innerHTML = ""; m.forEach((w) => { const b = mk("button", "b", `<b>${w.slice(0, v.length)}</b>${w.slice(v.length)}`); b.onclick = () => { I.value = w; upd(); }; $("#acL").appendChild(b); });
    $("#acV").innerHTML = !v ? "Type at least one letter." : m.length ? `${m.length} suggestion${m.length > 1 ? "s" : ""}. Click one to complete it. Auto-completion saves typing and avoids spelling mistakes in variable names and reserved words.` : "No suggestion for this."; };
  I.oninput = upd; upd();
})();

/* ---------- Lab 3: debugger ---------- */
(() => {
  let ver = 0, tr, cur, bp = new Set();
  const src = (v) => ["total = 0", "for i in range(1, 4):", v ? "    total = total + 1" : "    total = total + i", "print(total)"];
  const trace = (v) => { const t = [{ l: 0, i: "-", tot: "-", o: "-" }]; let tot = 0; t.push({ l: 0, i: "-", tot: 0, o: "-" }); for (let i = 1; i <= 3; i++) { t.push({ l: 1, i, tot, o: "-" }); tot = v ? tot + 1 : tot + i; t.push({ l: 2, i, tot, o: "-" }); } t.push({ l: 3, i: 3, tot, o: "-" }); t.push({ l: -1, i: 3, tot, o: tot }); return t; };
  const draw = () => {
    const s = tr[cur];
    $("#dbC").innerHTML = src(ver).map((l, k) => `<span class="ln ${s.l === k ? "on" : ""}"><a href="#" data-b="${k}" style="color:${bp.has(k) ? "var(--bad)" : "var(--muted)"};text-decoration:none" title="Toggle breakpoint">${bp.has(k) ? "●" : k + 1 + " "} </a> ${esc(l)}</span>`).join("");
    $$("[data-b]", $("#dbC")).forEach((a) => (a.onclick = (e) => { e.preventDefault(); const k = +a.dataset.b; bp.has(k) ? bp.delete(k) : bp.add(k); draw(); }));
    $("#dbI").textContent = s.i; $("#dbT").textContent = s.tot; $("#dbO").textContent = s.o;
    $("#dbM").innerHTML = s.l === -1 ? (+s.o === 6 ? "✓ Output 6: correct." : `✗ Output ${s.o}, but 1 + 2 + 3 = 6. Look at the report window: <b>total</b> went up by 1 each time, not by <b>i</b>. The bug is on line 3.`) : cur === 0 ? "Press Step to run line 1. Click a line number to set a breakpoint (●)." : `Line ${s.l + 1} has run.`;
  };
  const reset = () => { tr = trace(ver); cur = 0; draw(); };
  stateBtns($("#dbV"), ["Correct program", "Buggy program (logic error)"], (i) => { ver = i; reset(); }); $("#dbV button").click();
  $("#dbS").onclick = () => { if (cur < tr.length - 1) cur++; draw(); };
  $("#dbB").onclick = () => { do cur++; while (cur < tr.length - 1 && !bp.has(tr[cur].l)); cur = Math.min(cur, tr.length - 1); draw(); };
  $("#dbR").onclick = reset;
})();

/* ---------- Practise ---------- */
practise([
  { h: "1 · Match the IDE feature", type: "match", prompt: "Match each feature to what it does.", pairs: [
    ["Code editor", "Lets the program be written and edited in the same environment"], ["Debugger", "Runs the program and lets you single step and set breakpoints"],
    ["Dynamic error checking", "Underlines errors as they are typed and suggests corrections"], ["Auto-completion", "Offers to complete variable names and reserved words"],
    ["Prettyprinting", "Colour-codes the code and lays it out clearly"], ["Auto-documenter", "Explains the purpose of a piece of code"],
  ] },
  { h: "2 · Which feature is it?", type: "classify", prompt: "Drag each situation to the IDE feature that helps.", buckets: [{ label: "Debugger" }, { label: "Error diagnostics" }, { label: "Prettyprinting / completion" }], items: [
    { text: "Run the program one line at a time", b: 0 }, { text: "Stop at line 12 to look at the variables", b: 0 },
    { text: "A red underline appears as soon as a word is mistyped", b: 1 }, { text: "A suggested correction is shown", b: 1 },
    { text: "Strings are shown in red", b: 2 }, { text: "The editor offers \"counter\" after typing \"co\"", b: 2 },
  ], done: "Debug, diagnose, or format." },
  { h: "3 · Multiple choice", type: "quiz", qs: [
    { q: "What does a breakpoint do?", opts: ["Stops the program at a chosen line", "Deletes a line", "Compiles the program", "Colours the code"], a: 0, why: "Execution halts so variables can be checked." },
    { q: "What does single stepping do?", opts: ["Runs the program one line at a time", "Runs it faster", "Prints it", "Saves it"], a: 0, why: "It lets the programmer watch what each line does." },
    { q: "What is prettyprinting?", opts: ["Colour coding and laying out the code clearly", "Printing on paper", "Compressing the code", "Translating the code"], a: 0, why: "It makes the code easier to read." },
    { q: "Why does a report window of variables help?", opts: ["It shows if a logic error is changing values wrongly", "It makes the program quicker", "It deletes variables", "It stops syntax errors"], a: 0, why: "The programmer can compare values with what was expected." },
    { q: "Which IDE is commonly used for Python?", opts: ["PyCharm", "Excel", "Paint", "Chrome"], a: 0, why: "PyCharm is for Python, Visual Studio for Visual Basic, BlueJ for Java." },
  ] },
]);

real([
  ["PyCharm, Visual Studio and BlueJ", "These are IDEs students and professionals use. BlueJ is for Java, PyCharm for Python and Visual Studio supports several languages including Visual Basic.", "Name an example of an IDE."],
  ["Red wavy lines under code", "Many editors underline a mistake in red as soon as you type it, and show a lightbulb or message suggesting a fix.", "Dynamic error checking with a suggested correction."],
  ["Pressing the pause button on code in school", "Teachers often use the debugger to stop a program at a line and show students what each variable holds.", "A breakpoint and the report window of variables."],
  ["Autocompleting long names", "In a big program the editor can finish names like customerAddressLine2 after a few letters, so you spend less time typing and make fewer typing errors.", "Auto-completion."],
  ["Coloured keywords", "Keywords, strings and comments each appear in a different colour, so a missing closing quote is obvious because everything after it changes colour.", "Prettyprinting makes code easier to read."],
]);

exam([
  { cmd: "Describe", m: 3, q: "Suki is writing a program in a high-level language. Describe three features of an IDE that she would find helpful.", tip: "Name the feature, say how it helps.", ans: [["k", "Error diagnostics: it underlines mistakes as she types and suggests corrections."], ["k", "Auto-completion: it offers to complete variable names and reserved words, saving time."], ["k", "A debugger: she can single step or use breakpoints to look at variables and find logic errors."]], warn: "Listing a feature without saying what it does." },
  { cmd: "Explain", m: 3, q: "Explain how a debugger helps a programmer find a logic error.", tip: "Single step, breakpoint, variables.", ans: [["k", "The program can be run one line at a time (single stepping) or stopped at a breakpoint."], ["k", "A report window shows the contents of the variables at that point."], ["k", "The programmer can compare the values with what was expected to find the line causing the error."]], warn: "Saying the debugger \"fixes\" errors. It helps find them." },
  { cmd: "State", m: 2, q: "What is meant by prettyprinting?", tip: "Colour and layout.", ans: [["k", "The code editor colour codes the words in the program"], ["k", "and lays the program out in a meaningful way, making it easier to read."]], warn: "Saying it prints the program." },
  { cmd: "Describe", m: 2, q: "Describe auto-completion in a code editor.", tip: "Prompts, names, reserved words.", ans: [["k", "The editor offers context-sensitive prompts as the programmer types,"], ["k", "completing variable names and reserved words."]], warn: "Saying it writes the whole program." },
  { cmd: "Describe", m: 2, q: "Describe how dynamic error checking helps a programmer.", tip: "As typed, suggested correction.", ans: [["k", "It finds possible errors as the code is being typed and alerts the programmer."], ["k", "It provides a suggested correction, so errors are fixed before the program is run."]], warn: "Saying it finds errors only after the program is run." },
  { cmd: "State", m: 2, q: "State two reasons why an IDE usually includes a translator.", tip: "Compiler and/or interpreter.", ans: [["k", "So the program can be run from the same environment without switching software."], ["k", "The interpreter can be used during development and the compiler to produce the final version."]], warn: "Saying an IDE has no translator." },
]);

tips([
  "<b>Name the feature, then say what it does.</b> The mark is for the effect, not the name.",
  "<b>Know the seven features:</b> editor, translator, debugger, error diagnostics, auto-completion, auto-documenter, prettyprinting.",
  "<b>Debugger:</b> single step, breakpoint, variable report window. Used to find <b>logic</b> errors.",
  "<b>Dynamic error checking</b> works while you type, before the program is run.",
  "<b>Prettyprinting = colour coding plus layout.</b> It has nothing to do with printing.",
  "<b>Auto-completion</b> covers variable names and reserved words.",
  "<b>Name examples:</b> PyCharm (Python), Visual Studio (Visual Basic), BlueJ (Java).",
  "<b>Link to translators:</b> the interpreter is often used for developing and the compiler for the final version.",
], [
  ["Integrated development environment (IDE)", "A program that gathers tools to help a programmer write and develop programs."], ["Code editor", "A window where the program is written and edited."],
  ["Debugger", "A program that runs a program under development so the programmer can single step and set breakpoints."], ["Single stepping", "Running a program one line at a time."],
  ["Breakpoint", "A point in the source code where execution stops."], ["Dynamic error checking", "Finding possible errors as the code is typed and suggesting corrections."],
  ["Auto-completion", "Context-sensitive prompts that complete variable names and reserved words."], ["Auto-documenter", "A feature that explains the purpose of programming code."],
  ["Prettyprinting", "Colour coding the words in a program and laying it out meaningfully."], ["Logic error", "A mistake that makes a program give the wrong result even though it runs."],
]);
