const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)", WARN = "var(--warn)";
const note = (x, y, t, cls = "", anchor = "middle") => SV.text(x, y, t, "lbl bd " + cls, { "text-anchor": anchor });
const sm = (x, y, t, anchor = "middle") => SV.text(x, y, t, "sm", { "text-anchor": anchor });
const panel = (x, y, w, h, title, col, o = 1) => SV.rect(x, y, w, h, "", { rx: 12, style: `fill:var(--surface);stroke:${col};stroke-width:3`, opacity: o }) + (title ? SV.text(x + w / 2, y + 22, title, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) : "");
const arr = (x1, y1, x2, y2, col, dash) => SV.line(x1, y1, x2, y2, "", { style: `stroke:${col};stroke-width:3;${dash ? "stroke-dasharray:7 6" : ""}` });
const chip = (x, y, w, t, col) => SV.rect(x, y, w, 26, "", { rx: 13, style: `fill:${col}` }) + SV.text(x + w / 2, y + 18, t, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:12px" });
const range = (a, b) => { const r = []; for (let i = a; i <= b; i++) r.push(i); return r; };
/* select-one-per-row chooser. items: [text, correctOption] */
function chooser(el, v, opts, items, ph) {
  el.innerHTML = items.map((s) => `<div class="r" data-a="${esc(s[1])}"><span class="q">${s[0]}</span><select class="sel" aria-label="${esc(s[0].replace(/<[^>]+>/g, ""))}"><option value="">${ph || "Choose…"}</option>${opts.map((x) => `<option>${esc(x)}</option>`).join("")}</select></div>`).join("");
  v.textContent = "Choose an answer for each row.";
  $$(".r", el).forEach((r) => $("select", r).addEventListener("change", (e) => { r.classList.remove("ok", "no"); if (e.target.value) r.classList.add(e.target.value === r.dataset.a ? "ok" : "no"); v.textContent = `${$$(".r.ok", el).length} of ${$$(".r", el).length} correct. Red means a different answer fits better.`; }));
}
/* ---------- flowchart drawing ---------- */
function fcDraw(nodes, edges, hiN, hiE) {
  let o = "";
  edges.forEach((e) => { const on = hiE.has(e.id), col = on ? "var(--accent)" : "var(--muted)", p = e.pts, last = p[p.length - 1], prev = p[p.length - 2];
    o += SV.path("M" + p.map((q) => q.join(" ")).join(" L"), "", { style: `fill:none;stroke:${col};stroke-width:${on ? 4 : 2}` });
    const dx = Math.sign(last[0] - prev[0]), dy = Math.sign(last[1] - prev[1]), a = 8;
    o += SV.poly(dx ? [[last[0], last[1]], [last[0] - dx * a * 1.6, last[1] - a], [last[0] - dx * a * 1.6, last[1] + a]] : [[last[0], last[1]], [last[0] - a, last[1] - dy * a * 1.6], [last[0] + a, last[1] - dy * a * 1.6]], "", { style: `fill:${col}` });
    if (e.lab) o += SV.text(e.lx, e.ly, e.lab, "lbl bd", { "text-anchor": "middle", style: `fill:${on ? "var(--accent)" : "var(--muted)"}` }); });
  nodes.forEach((n) => { const on = hiN.has(n.id), st = `fill:${on ? "var(--accent-soft)" : "var(--surface)"};stroke:${on ? "var(--accent)" : "var(--muted)"};stroke-width:${on ? 4 : 2}`, [x, y, w, h] = [n.x, n.y, n.w, n.h];
    if (n.t === "term") o += SV.rect(x - w / 2, y - h / 2, w, h, "", { rx: h / 2, style: st });
    else if (n.t === "dec") o += SV.poly([[x, y - h / 2], [x + w / 2, y], [x, y + h / 2], [x - w / 2, y]], "", { style: st });
    else if (n.t === "io") o += SV.poly([[x - w / 2 + 14, y - h / 2], [x + w / 2 + 14, y - h / 2], [x + w / 2 - 14, y + h / 2], [x - w / 2 - 14, y + h / 2]], "", { style: st });
    else o += SV.rect(x - w / 2, y - h / 2, w, h, "", { style: st });
    o += SV.text(x, y + 5, n.l, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); });
  return o;
}
const EO_N = [{ id: "start", t: "term", x: 320, y: 28, w: 130, h: 34, l: "Start" }, { id: "in", t: "io", x: 320, y: 92, w: 150, h: 40, l: "INPUT Number" }, { id: "dec", t: "dec", x: 320, y: 175, w: 240, h: 90, l: "Number MOD 2 = 0 ?" },
  { id: "even", t: "io", x: 150, y: 280, w: 150, h: 40, l: 'OUTPUT "Even"' }, { id: "odd", t: "io", x: 490, y: 280, w: 150, h: 40, l: 'OUTPUT "Odd"' }, { id: "stop", t: "term", x: 320, y: 370, w: 130, h: 34, l: "Stop" }];
const EO_E = [{ id: "start>in", pts: [[320, 45], [320, 70]] }, { id: "in>dec", pts: [[320, 112], [320, 130]] }, { id: "dec>even", pts: [[200, 175], [150, 175], [150, 258]], lab: "Yes", lx: 170, ly: 165 },
  { id: "dec>odd", pts: [[440, 175], [490, 175], [490, 258]], lab: "No", lx: 470, ly: 165 }, { id: "even>stop", pts: [[150, 302], [150, 370], [255, 370]] }, { id: "odd>stop", pts: [[490, 302], [490, 370], [385, 370]] }];
const EO_PS = ["INPUT Number", "IF Number MOD 2 = 0", "  THEN", '    OUTPUT "Even"', "  ELSE", '    OUTPUT "Odd"', "ENDIF"];
const EO_PY = ["number = int(input())", "if number % 2 == 0:", '    print("Even")', "else:", '    print("Odd")'];
function eoFrames(n) {
  const even = n % 2 === 0, F = [], V = (N, E) => fcDraw(EO_N, EO_E, new Set(N), new Set(E)), side = even ? "even" : "odd";
  const f = (cap, ps, py, N, E, extra) => F.push({ cap, ps, py, svg: V(N, E) + (extra || "") });
  f("The flowchart starts at the <b>Start</b> terminator.", [], [], ["start"], []);
  f(`The input shape: the user types <b>${n}</b>, stored in Number.`, [0], [0], ["in"], ["start>in"], note(560, 92, "Number = " + n, "t1"));
  f(`The decision: is Number MOD 2 = 0? MOD gives the remainder. ${n} MOD 2 = <b>${n % 2}</b>.`, [1], [1], ["dec"], ["start>in", "in>dec"], note(560, 175, `${n} MOD 2 = ${n % 2}`, "t1"));
  f(even ? "The answer is <b>Yes</b>, so follow the Yes arrow." : "The answer is <b>No</b>, so follow the No arrow.", even ? [2] : [4], even ? [2] : [3], ["dec"], ["start>in", "in>dec", "dec>" + side]);
  f(`The output shape: output <b>${even ? "Even" : "Odd"}</b>.`, even ? [3] : [5], even ? [2] : [4], [side], ["start>in", "in>dec", "dec>" + side]);
  f("Both paths join and reach <b>Stop</b>. The algorithm ends.", [6], [], ["stop"], ["start>in", "in>dec", "dec>" + side, side + ">stop"]);
  return F;
}

/* ---------- 1. structure diagram ---------- */
function sdChart(s) {
  const k = Math.round(s.k), box = (x, y, w, t, on, col = ACC) => SV.rect(x, y, w, 36, "", { rx: 8, style: `fill:var(--surface);stroke:${on ? col : "var(--line)"};stroke-width:${on ? 3 : 2}`, opacity: on ? 1 : 0.15 }) + SV.text(x + w / 2, y + 23, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px", opacity: on ? 1 : 0.15 });
  const ln = (a, b, c, d, on) => SV.line(a, b, c, d, "", { style: "stroke:var(--muted);stroke-width:2", opacity: on ? 1 : 0.15 });
  const L2 = [["Browse products", 90], ["Basket", 380], ["Checkout", 620]];
  let o = box(300, 12, 160, "Online shop", true);
  L2.forEach(([t, cx]) => { o += ln(380, 48, cx, 90, k >= 1) + box(cx - 70, 90, 140, t, k >= 1, k === 1 ? ACC : MUT); });
  const L3 = [[["Search", 40, 1], ["Filter", 140, 1]], [["Add item", 330, 3], ["Remove item", 430, 3]], [["Address", 570, 2], ["Payment", 670, 2]]];
  L3.forEach((g, gi) => g.forEach(([t, cx, kk]) => { const on = k >= kk; o += ln(L2[gi][1], 126, cx, 176, on) + box(cx - 45, 176, 90, t, on, GOOD); }));
  o += note(380, 262, k === 0 ? "The whole problem" : k === 1 ? "Split into main parts" : k === 2 ? "Checkout is broken down further" : k === 3 ? "Every part is broken down to a small task" : "Each bottom box can be coded and tested by itself", k === 4 ? "t3" : "t1");
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 285, label: "A structure diagram for an online shop", base: { k: 0 }, tween: 1, dwell: 3500, draw: sdChart, steps: [
  { cap: "The whole problem sits at the <b>top</b> of the structure diagram: an online shop.", s: { k: 0 } },
  { cap: "It is <b>decomposed</b> into its main parts: browsing, the basket and the checkout.", s: { k: 1 } },
  { cap: "Each part is broken down again. The checkout needs an <b>address</b> and a <b>payment</b>.", s: { k: 2 } },
  { cap: "The basket and the browse part are broken down too, until each box is a <b>small, simple task</b>.", s: { k: 3 } },
  { cap: "Each box at the bottom can be <b>coded and tested separately</b>, and different programmers can work on different boxes.", s: { k: 4 } },
] });

/* ---------- 2. IPOS ---------- */
const IPOS = [["Inputs", ["Button pressed", "Coins inserted"], ACC], ["Processes", ["Record entry time", "Calculate the fee"], WARN], ["Outputs", ["Print a ticket", "Give change"], GOOD], ["Storage", ["Log of tickets", "Log of payments"], BAD]];
function ipChart(s) {
  const k = Math.round(s.k); let o = note(380, 24, "Car park ticket machine", "t1");
  IPOS.forEach(([n, items, col], i) => { const on = k >= i + 1, x = 20 + i * 185;
    o += panel(x, 50, 165, 160, n, on ? col : MUT, on ? 1 : 0.25);
    if (on) items.forEach((t, j) => (o += SV.text(x + 82, 100 + j * 34, "• " + t, "lbl", { "text-anchor": "middle" })));
    if (i < 3 && on) o += arr(x + 165, 130, x + 185, 130, MUT); });
  return o + note(380, 250, k === 0 ? "A machine to decompose" : k === 4 ? "Each question gives a part of the solution" : "", "t1");
}
Lib.stepper($("#stB"), { w: 760, h: 270, label: "Decomposing a ticket machine into inputs, processes, outputs and storage", base: { k: 0 }, tween: 1, dwell: 3200, draw: ipChart, steps: [
  { cap: "A <b>car park ticket machine</b>. How could it be decomposed?", s: { k: 0 } },
  { cap: "<b>Inputs</b>: what data goes in? The driver presses the button and inserts coins.", s: { k: 1 } },
  { cap: "<b>Processes</b>: what is done to it? Record the entry time and calculate the fee.", s: { k: 2 } },
  { cap: "<b>Outputs</b>: what comes out? A printed ticket and change.", s: { k: 3 } },
  { cap: "<b>Storage</b>: what must be kept? A log of tickets and payments.", s: { k: 4 } },
] });

/* ---------- 3. flowchart + pseudocode ---------- */
Lib.algo($("#aF"), { w: 640, h: 400, label: "Flowchart and pseudocode for even or odd", pseudo: EO_PS, py: EO_PY, dwell: 2600, frames: eoFrames(7) });

/* ---------- worked code ---------- */
Lib.codePanel($("#cdAvg"), { pseudo: ["Total ← 0", "FOR Count ← 1 TO 10", "    INPUT Number", "    Total ← Total + Number", "NEXT Count", "Average ← Total / 10", "OUTPUT Average"], py: ["total = 0", "for count in range(1, 11):", "    number = int(input())", "    total = total + number", "average = total / 10", "print(average)"] });

/* ---------- Lab 1 ---------- */
chooser($("#sn"), $("#sv"), ["Terminator", "Process", "Input / Output", "Decision", "Subroutine", "Flow line"], [
  ["The Start of the algorithm", "Terminator"], ["Total ← Total + Number", "Process"], ["INPUT Age", "Input / Output"], ["Age >= 18 ?  (Yes / No)", "Decision"], ["Call the CalculateTax routine", "Subroutine"], ["Shows which step comes next", "Flow line"], ["OUTPUT Total", "Input / Output"], ["The Stop of the algorithm", "Terminator"],
]);

/* ---------- Lab 2 ---------- */
(() => {
  const N = [{ id: "start", t: "term", x: 320, y: 24, w: 130, h: 34, l: "Start" }, { id: "in", t: "io", x: 320, y: 84, w: 150, h: 40, l: "INPUT Mark" }, { id: "d1", t: "dec", x: 320, y: 160, w: 220, h: 80, l: "Mark >= 70 ?" }, { id: "d2", t: "dec", x: 320, y: 280, w: 220, h: 80, l: "Mark >= 50 ?" },
    { id: "dist", t: "io", x: 80, y: 160, w: 150, h: 40, l: 'OUTPUT "Distinction"' }, { id: "pass", t: "io", x: 540, y: 280, w: 150, h: 40, l: 'OUTPUT "Pass"' }, { id: "fail", t: "io", x: 320, y: 370, w: 150, h: 40, l: 'OUTPUT "Fail"' }, { id: "stop", t: "term", x: 320, y: 436, w: 130, h: 34, l: "Stop" }];
  const E = [{ id: "start>in", pts: [[320, 41], [320, 64]] }, { id: "in>d1", pts: [[320, 104], [320, 120]] }, { id: "d1>dist", pts: [[210, 160], [166, 160]], lab: "Yes", lx: 190, ly: 150 }, { id: "d1>d2", pts: [[320, 200], [320, 240]], lab: "No", lx: 340, ly: 222 },
    { id: "d2>pass", pts: [[430, 280], [466, 280]], lab: "Yes", lx: 448, ly: 270 }, { id: "d2>fail", pts: [[320, 320], [320, 350]], lab: "No", lx: 340, ly: 338 }, { id: "dist>stop", pts: [[80, 180], [80, 436], [255, 436]] }, { id: "pass>stop", pts: [[540, 300], [540, 436], [385, 436]] }, { id: "fail>stop", pts: [[320, 390], [320, 419]] }];
  const inp = $("#mk"), svg = $("#gf"), gv = $("#gv");
  function upd() {
    const m = parseFloat(inp.value);
    if (isNaN(m) || m < 0 || m > 100) { svg.innerHTML = fcDraw(N, E, new Set(), new Set()); gv.textContent = "Enter a mark from 0 to 100."; return; }
    const res = m >= 70 ? "dist" : m >= 50 ? "pass" : "fail", path = ["start", "in", "d1"].concat(m >= 70 ? [] : ["d2"], [res, "stop"]);
    svg.innerHTML = fcDraw(N, E, new Set(path), new Set(path.slice(1).map((n, i) => path[i] + ">" + n)));
    gv.innerHTML = `Mark ${m}: ${m >= 70 ? "70 or more, so the first decision is Yes." : `below 70, so the first decision is No. ${m >= 50 ? "It is 50 or more, so the second decision is Yes." : "It is also below 50, so the second decision is No."}`} Output: <b>${res === "dist" ? "Distinction" : res === "pass" ? "Pass" : "Fail"}</b>.`;
  }
  inp.addEventListener("input", upd); upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  const C = {
    "Assignment": [["Total ← 0", "Total ← Total + Mark"], ["total = 0", "total = total + mark"]],
    "Input and output": [["INPUT Name", 'OUTPUT "Hello ", Name'], ["name = input()", 'print("Hello", name)']],
    "IF ... THEN ... ELSE": [["IF Age >= 18", "  THEN", '    OUTPUT "Adult"', "  ELSE", '    OUTPUT "Child"', "ENDIF"], ["if age >= 18:", '    print("Adult")', "else:", '    print("Child")']],
    "FOR loop": [["FOR Count ← 1 TO 5", "    OUTPUT Count", "NEXT Count"], ["for count in range(1, 6):", "    print(count)"]],
    "WHILE loop": [["WHILE Total < 100 DO", "    Total ← Total + 10", "ENDWHILE"], ["while total < 100:", "    total = total + 10"]],
    "REPEAT ... UNTIL": [["REPEAT", "    INPUT Guess", "UNTIL Guess = Secret"], ["while True:", "    guess = int(input())", "    if guess == secret:", "        break"]],
    "Arrays": [["DECLARE Marks : ARRAY[1:5] OF INTEGER", "Marks[1] ← 72", "OUTPUT Marks[1]"], ["marks = [0] * 5", "marks[0] = 72", "print(marks[0])"]],
  };
  const sel = $("#cs"); sel.innerHTML = Object.keys(C).map((k) => `<option>${k}</option>`).join("");
  const show = () => { const c = C[sel.value]; Lib.codePanel($("#cc"), { pseudo: c[0], py: c[1] }); };
  sel.onchange = show; show();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "A school canteen system. Drag each item to input, process, output or storage.", buckets: [{ label: "Input" }, { label: "Process" }, { label: "Output" }, { label: "Storage" }], items: [
  { text: "Student scans their ID card", b: 0 },
  { text: "Student chooses a meal from the screen", b: 0 },
  { text: "Work out the total price", b: 1 },
  { text: "Check the student has enough credit", b: 1 },
  { text: "Print the order for the kitchen", b: 2 },
  { text: "Display the remaining balance", b: 2 },
  { text: "File of student accounts", b: 3 },
  { text: "Record of meals sold each day", b: 3 },
], done: "Data in, work done, results out, data kept." });

Lib.match($("#m1"), { prompt: "Match each flowchart symbol to its use.", pairs: [
  ["Terminator", "The Start and Stop of the flowchart"],
  ["Process", "Something being done, such as a calculation"],
  ["Input / Output", "Data going in or out of the flowchart"],
  ["Decision", "A Yes/No question with two exits"],
  ["Subroutine", "A call to a separate procedure or function"],
  ["Flow line", "An arrow showing control passing to the next shape"]
] });

Lib.classify($("#cl2"), { prompt: "Is each pseudocode line acceptable, or too vague for an exam answer?", buckets: [{ label: "Acceptable" }, { label: "Too vague" }], items: [
  { text: "IF Score >= 50", b: 0 },
  { text: "Total ← Total + Mark", b: 0 },
  { text: "OUTPUT Total", b: 0 },
  { text: "WHILE Count <= 10 DO", b: 0 },
  { text: "IF Score is at least 50", b: 1 },
  { text: "Add Mark to Total", b: 1 },
  { text: "Show the total on screen", b: 1 },
  { text: "Repeat until we reach ten", b: 1 },
], done: "Use symbols and keywords, not English phrases." });

Lib.order($("#o1"), { prompt: "Put these flowchart steps for a password check in order.", items: [
  "Start",
  "INPUT Password",
  "Decision: is Password = \"Secret\" ?",
  "Yes: OUTPUT \"Welcome\"",
  "Stop"
], done: "Start, input, decision, output, stop." });

Lib.calc($("#c1"), { qs: [
  { q: "How many exits does a decision shape in a flowchart have?", a: 2, sol: "Two: Yes and No (or True and False)." },
  { q: "How many times does FOR Count ← 1 TO 5 repeat its loop body?", a: 5, sol: "Count takes the values 1, 2, 3, 4, 5: five times." },
  { q: "A structure diagram has 3 main parts and each part has 2 sub-parts. How many boxes are in the bottom level?", a: 6, sol: "3 × 2 = 6." },
  { q: "What is DIV(17, 5)?", a: 3, sol: "17 divided by 5 is 3 remainder 2, so DIV gives 3." },
  { q: "What is MOD(17, 5)?", a: 2, sol: "MOD gives the remainder: 17 − 15 = 2." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "What does a structure diagram show?", opts: ["The order of steps", "The parts a problem is split into", "The test data", "The program code"], a: 1, why: "It shows the hierarchy of sub-problems." },
  { q: "Which flowchart shape is used for a Yes/No question?", opts: ["Process", "Terminator", "Decision", "Subroutine"], a: 2, why: "The decision shape has two exits." },
  { q: "Which is a precise pseudocode statement?", opts: ["Add one to Count", "Count ← Count + 1", "Increase count", "Count goes up"], a: 1, why: "Use ← and symbols." },
  { q: "What does MOD return?", opts: ["The quotient", "The remainder", "The product", "The sign"], a: 1, why: "MOD gives the remainder after division." },
  { q: "Which is a design method?", opts: ["Pseudocode", "Test data", "A compiler", "A debugger"], a: 0, why: "Pseudocode, flowcharts and structure diagrams are design methods." },
  { q: "When explaining the purpose of an algorithm you should…", opts: ["Copy the code", "State what it does overall and describe the processes", "Say it is a loop", "Rewrite it in Python"], a: 1, why: "Give the overall purpose and the main processes." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Sub-system", "A smaller part of a computer system, which may itself be made of smaller parts."],
  ["Structure diagram", "A hierarchy of boxes showing the parts a problem is decomposed into."],
  ["Flowchart", "A diagram showing the steps and decisions of an algorithm with standard shapes."],
  ["Terminator", "Flowchart symbol for Start and Stop."],
  ["Decision", "Flowchart symbol for a Yes/No question, with two exits."],
  ["Pseudocode", "An algorithm written in structured, code-like English that is not tied to a language."],
  ["Input, process, output, storage", "Four questions used to decompose a problem."],
  ["Purpose of an algorithm", "What the algorithm achieves overall."],
  ["MOD", "Returns the remainder of an integer division."],
  ["DIV", "Returns the quotient of an integer division, discarding the remainder."]
] });
