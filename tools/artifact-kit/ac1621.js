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
  const toks = [["Total", "identifier"], ["=", "operator"], ["Price", "identifier"], ["*", "operator"], ["2", "constant"], ["+", "operator"], ["5", "constant"]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "source code", "sm") + SV.rect(20, 30, 600, 40, "cell", { rx: 6 }) + SV.text(34, 56, "Total = Price * 2 + 5   # add tax", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 1) o += SV.text(20, 100, "after removing the comment and white space: Total=Price*2+5", "sm");
    if (k >= 2) { o += SV.text(20, 126, "tokens", "sm"); toks.slice(0, k - 1).forEach(([t, ty], i) => { const x = 20 + i * 86; o += SV.rect(x, 134, 78, 40, "f" + (ty === "identifier" ? 1 : ty === "operator" ? 2 : 3), { rx: 6 }) + SV.rect(x, 134, 78, 40, "ax", { rx: 6, fill: "none" }) + SV.text(x + 39, 158, t, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" }) + SV.text(x + 39, 190, ty, "sm", { "text-anchor": "middle", style: "font-size:10px" }); }); }
    if (k >= 9) { o += SV.text(20, 224, "symbol table", "sm") + SV.rect(20, 232, 240, 26, "cell", { rx: 4 }) + SV.text(30, 250, "Total, Price (identifiers)", "lbl", { style: "font-size:12.5px" }); }
    return o; };
  Lib.stepper($("#stA"), { w: 640, h: 270, label: "Lexical analysis", base: { i: 0 }, draw, tween: 140, dwell: 2600, steps: [{ cap: "The source code contains spaces and a comment.", s: { i: 0 } }, { cap: "<b>White space and the comment are removed</b>: they are not needed to run the program.", s: { i: 1 } }, { cap: "The rest is broken into <b>tokens</b> and each is categorised: identifier, operator or constant. There are seven: <b>Total</b>, <b>=</b>, <b>Price</b>, <b>*</b>, <b>2</b>, <b>+</b>, <b>5</b>.", s: { i: 8 } }, { cap: "The identifiers are stored in the <b>symbol table</b>. An invalid token would produce an error here. The tokens go on to syntax analysis.", s: { i: 9 } }] });
})();
(function () {
  const nodes = [{ t: "=", x: 300, y: 36 }, { t: "Total", x: 170, y: 104 }, { t: "+", x: 430, y: 104 }, { t: "*", x: 350, y: 172 }, { t: "5", x: 510, y: 172 }, { t: "Price", x: 290, y: 240 }, { t: "2", x: 410, y: 240 }];
  const edges = [[0, 1], [0, 2], [2, 3], [2, 4], [3, 5], [3, 6]]; const show = [1, 2, 3, 5, 7];
  const draw = (s) => { const k = Math.round(s.i), n = show[k]; let o = "";
    edges.forEach(([a, b]) => { if (a < n && b < n) o += SV.line(nodes[a].x, nodes[a].y, nodes[b].x, nodes[b].y, "edge"); });
    nodes.slice(0, n).forEach((nd) => (o += SV.circle(nd.x, nd.y, 26, "nd", {}) + SV.text(nd.x, nd.y + 5, nd.t, "lbl bd", { "text-anchor": "middle", style: "font-size:" + (nd.t.length > 3 ? 12 : 16) + "px" })));
    o += SV.text(20, 22, "Total = Price * 2 + 5", "lbl bd", { style: "font-family:var(--mono)" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 280, label: "Parse tree", base: { i: 0 }, draw, tween: 120, dwell: 2800, steps: [{ cap: "The parser reads the tokens against the grammar. This is an <b>assignment</b>: the root is =.", s: { i: 0 } }, { cap: "On the left is the variable being assigned to, <b>Total</b>.", s: { i: 1 } }, { cap: "The expression on the right is an addition, so <b>+</b> is the other child of =. The grammar says + binds less tightly than *, so + is higher in the tree.", s: { i: 2 } }, { cap: "The addition has two children: the multiplication, which is lower down and so worked out first, and the constant <b>5</b>.", s: { i: 3 } }, { cap: "Every token is placed. The <b>parse tree</b> is the output of syntax analysis. A token in the wrong place would give a syntax error.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "Interpreter", "lbl bd") + SV.text(20, 128, "Compiler", "lbl bd");
    const prog = ["a", "b", "c"]; let x = 20; const iters = 3;
    for (let r = 0; r < iters; r++) prog.forEach((p, i) => { const idx = r * 3 + i, on = idx < k * 3 / 1; if (r * 3 + i < Math.min(9, k * 3)) o += SV.rect(20 + idx * 52, 34, 46, 34, "f1", { rx: 4 }) + SV.text(43 + idx * 52, 56, "T+R", "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); });
    o += SV.text(20, 92, "T+R = translate then run, for every line, every time round the loop", "sm");
    if (k >= 1) o += SV.rect(20, 140, 150, 34, "f2", { rx: 4 }) + SV.text(95, 162, "translate once", "lbl bd", { "text-anchor": "middle", style: "font-size:12px" });
    if (k >= 2) for (let r = 0; r < Math.min(3, k - 1); r++) o += SV.rect(190 + r * 130, 140, 120, 34, "f3", { rx: 4 }) + SV.text(250 + r * 130, 162, "run loop pass " + (r + 1), "lbl", { "text-anchor": "middle", style: "font-size:12px" });
    o += SV.text(20, 206, k >= 3 ? "Interpreter translated 9 times; compiler translated once, then only ran." : "", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 640, h: 224, label: "Interpreter and compiler", base: { i: 0 }, draw, tween: 140, dwell: 2800, steps: [{ cap: "A three-line loop runs three times. The <b>interpreter</b> translates and runs each line as it reaches it.", s: { i: 0 } }, { cap: "First pass: three lines translated and run. Meanwhile the <b>compiler</b> translates the whole program once, before anything runs.", s: { i: 1 } }, { cap: "The interpreter has to <b>translate the same lines again</b> on pass two. The compiled program just runs.", s: { i: 2 } }, { cap: "After pass three the interpreter has translated nine lines. The compiler translated once, and the executable can be run again without translating.", s: { i: 3 } }] });
})();

(function () {
  const inp = $("#lxI"), out = $("#lxO");
  const KW = ["IF", "THEN", "ELSE", "ENDIF", "FOR", "TO", "NEXT", "WHILE", "ENDWHILE", "PRINT", "OUTPUT", "INPUT", "DECLARE", "if", "else", "for", "while", "print", "input", "def", "return"];
  const paint = () => { let src = inp.value; const cm = src.indexOf("#"); const comment = cm >= 0 ? src.slice(cm) : ""; if (cm >= 0) src = src.slice(0, cm);
    const re = /\s*([A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|"[^"]*"|==|<=|>=|<>|[-+*\/=<>()\[\],:^]|\S)/g; const t = []; let m; const ids = new Set();
    while ((m = re.exec(src))) { const x = m[1]; let ty = /^[A-Za-z_]/.test(x) ? (KW.includes(x) ? "keyword" : "identifier") : /^\d/.test(x) ? "constant" : /^"/.test(x) ? "string" : /^[-+*\/=<>^]|==|<=|>=|<>$/.test(x) ? "operator" : /^[()\[\],:]$/.test(x) ? "punctuation" : "INVALID"; if (ty === "identifier") ids.add(x); t.push([x, ty]); }
    let h = '<div class="tw"><table class="t mono"><tr><th>Token</th><th>Type</th></tr>' + t.map(([x, ty]) => `<tr><td>${x.replace(/</g, "&lt;")}</td><td style="${ty === "INVALID" ? "color:var(--bad);font-weight:700" : ""}">${ty}</td></tr>`).join("") + "</table></div>";
    out.innerHTML = h + `<div class="verdict">${t.length} token${t.length === 1 ? "" : "s"}. ${comment ? "The comment <b>" + comment.replace(/</g, "&lt;") + "</b> and the white space were removed. " : "White space is removed. "}Symbol table: <b>${ids.size ? [...ids].join(", ") : "empty"}</b>.${t.some((x) => x[1] === "INVALID") ? ' <b style="color:var(--bad)">Invalid token: the lexical analyser reports an error.</b>' : ""}</div>`; };
  inp.oninput = paint; paint();
})();
(function () {
  const O = [
    ["Constant folding", "Seconds = 2 * 60 * 60", "Seconds = 7200", "A calculation on constants is done once at compile time, not every time the program runs."],
    ["Redundant code", "X = 5\nX = 10\nPRINT X", "X = 10\nPRINT X", "An assignment whose value is never used is removed, saving storage and time."],
    ["Unused variable", "Temp = A + B\nPRINT A", "PRINT A", "Code whose result is never used is removed."],
    ["Same calculation twice", "P = A * B + 1\nQ = A * B + 2", "T = A * B\nP = T + 1\nQ = T + 2", "A repeated calculation is done once, then re-used."]];
  const b = $("#opB"); const show = (i) => { const [n, a, c, why] = O[i]; $("#opO").innerHTML = `<h3>${n}</h3><div class="grid2"><div class="card"><b>Before</b><pre class="plain">${a}</pre></div><div class="card"><b>After optimisation</b><pre class="plain">${c}</pre></div></div><div class="verdict">${why}</div>`; b.querySelectorAll("button").forEach((x, j) => (x.className = j === i ? "on" : "")); };
  O.forEach((o, i) => { const x = document.createElement("button"); x.textContent = o[0]; x.onclick = () => show(i); b.appendChild(x); }); show(0);
})();
(function () {
  let n = 3;
  const paint = () => { const interp = 4 + n, comp = 5; $("#lpO").innerHTML = '<div class="tw"><table class="t mono"><tr><th></th><th>Statements translated</th></tr>' + `<tr><td>Interpreter (4 lines once + 1 line ${n} times)</td><td>${interp}</td></tr><tr><td>Compiler (all 5 lines once)</td><td>${comp}</td></tr>` + `<tr><td>Interpreter, run the program again</td><td>${interp * 2} so far</td></tr><tr><td>Compiler, run the program again</td><td>${comp} (no further translation)</td></tr></table></div>`; };
  Lib.slider($("#lpS"), { id: "lps", label: "Times the loop runs ", min: 1, max: 20, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();
Lib.classify($("#cl1"), { prompt: "Which stage of compilation?", buckets: [{"label": "Lexical analysis"}, {"label": "Syntax analysis"}, {"label": "Code generation"}, {"label": "Optimisation"}], items: [{"text": "Removes white space and comments", "b": 0}, {"text": "Produces a parse tree", "b": 1}, {"text": "Creates executable code from the parse tree", "b": 2}, {"text": "Removes redundant code", "b": 3}, {"text": "Stores identifiers in a symbol table", "b": 0}, {"text": "Checks that tokens obey the grammar", "b": 1}, {"text": "Minimises memory use and execution time", "b": 3}, {"text": "Breaks the source into tokens", "b": 0}], done: "Lexical tokens, syntax grammar, generate code, optimise resources." });
Lib.classify($("#cl2"), { prompt: "Interpreter or compiler?", buckets: [{"label": "Interpreter"}, {"label": "Compiler"}], items: [{"text": "Translates and executes one statement at a time", "b": 0}, {"text": "Produces an executable file", "b": 1}, {"text": "Translation is repeated every time the program is run", "b": 0}, {"text": "The program can run without the source code", "b": 1}, {"text": "Halts at the first error it reaches", "b": 0}, {"text": "Translates the whole program first", "b": 1}], done: "Interpreter: statement by statement. Compiler: whole program, executable." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Lexical analysis", "Converting a sequence of characters into a sequence of tokens"], ["Syntax analysis", "Using parsing algorithms to interpret the meaning of tokens"], ["Code generation", "Converting an intermediate representation into an executable form"], ["Optimisation", "Minimising execution time and memory requirements"], ["Interpreter", "Directly executing instructions, one statement at a time"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the stages of compilation in order.", items: ["Lexical analysis", "Syntax analysis", "Code generation", "Optimisation"], done: "Lexical, syntax, code generation, optimisation." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many tokens does Total = Price * 2 + 5 contain?", "a": 7, "unit": "", "tol": 0.01, "hint": "Count each name, operator and number.", "sol": "<b>7</b>."},
  {"q": "How many identifiers (for the symbol table) are in Total = Price * 2 + 5?", "a": 2, "unit": "", "tol": 0.01, "hint": "Total and Price.", "sol": "<b>2</b>."},
  {"q": "A program has 4 lines run once, and 1 line that runs 6 times in a loop. How many statements does an interpreter translate?", "a": 10, "unit": "", "tol": 0.01, "hint": "4 + 6.", "sol": "<b>10</b>."},
  {"q": "The same program with a compiler: how many statements are translated?", "a": 5, "unit": "", "tol": 0.01, "hint": "Each line once.", "sol": "<b>5</b>."},
  {"q": "How many stages of compilation are named in the syllabus?", "a": 4, "unit": "", "tol": 0.01, "hint": "Lexical, syntax, code generation, optimisation.", "sol": "<b>4</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which stage produces a parse tree?", opts: ["Lexical analysis", "Syntax analysis", "Code generation", "Optimisation"], a: 1, why: "Syntax analysis." },
  { q: "An interpreter:", opts: ["Produces an executable file", "Executes one statement at a time", "Optimises the code", "Needs no source code"], a: 1, why: "One statement at a time." },
  { q: "What does the lexical analyser create?", opts: ["A symbol table and tokens", "Machine code", "A parse tree", "A network"], a: 0, why: "Tokens and a symbol table." },
  { q: "Which stage minimises memory use?", opts: ["Optimisation", "Lexical analysis", "Syntax analysis", "Linking"], a: 0, why: "Optimisation." },
  { q: "A syntax error is reported by:", opts: ["Syntax analysis", "Code generation", "The CPU", "The printer"], a: 0, why: "The parser." },
  { q: "An interpreter finds an error. It:", opts: ["Ignores it", "Reports it and halts", "Fixes it", "Restarts"], a: 1, why: "Reports and halts." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Interpreter", "One statement at a time; no translated version; repeated every run."],
  ["Compiler", "Translates the whole program into an executable."],
  ["Lexical analysis", "Tokens, symbol table, remove white space and comments."],
  ["Syntax analysis", "Grammar check, parse tree, syntax errors."],
  ["Code generation", "Parse tree to executable code."],
  ["Optimisation", "Remove redundant code; minimum resources."],
  ["Token", "Keyword, identifier, operator, constant."],
  ["Symbol table", "Stores the identifiers."],
] });
