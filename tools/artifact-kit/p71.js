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
/* ---------- 1. stages ---------- */
const ST = ["Analysis", "Design", "Coding", "Testing"];
const TASKS = [["Identify the problem", "Abstraction and decomposition", "Write down the requirements"], ["Structure diagram", "Flowchart", "Pseudocode"], ["Write the program code", "Test each part as you go", "Fix errors straight away"], ["Run with test data", "Compare actual and expected", "Fix errors, then retest"]];
function stChart(s) {
  const k = Math.round(s.k); let o = "";
  ST.forEach((n, i) => { const on = k === i || (k === 4 && i === 2), x = 20 + i * 185; o += panel(x, 40, 160, 70, n, on ? ACC : MUT) + sm(x + 80, 92, "Stage " + (i + 1)); if (i < 3) o += arr(x + 160, 75, x + 185, 75, MUT); });
  if (k >= 4) o += arr(655, 110, 655, 150, BAD, 1) + arr(655, 150, 470, 150, BAD, 1) + arr(470, 150, 470, 110, BAD, 1) + note(562, 142, "error found: back to coding", "t2");
  const L = k < 4 ? TASKS[k] : ["Error found in testing", "Go back to coding (or design)", "Fix it and test again"];
  o += SV.rect(60, 185, 640, 120, "", { rx: 12, style: "fill:var(--soft);stroke:var(--line);stroke-width:2" });
  L.forEach((t, i) => (o += SV.text(380, 220 + i * 30, "• " + t, "lbl bd " + (k >= 4 ? "t2" : ""), { "text-anchor": "middle" })));
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 320, label: "The four stages of the program development life cycle", base: { k: 0 }, tween: 1, dwell: 3800, draw: stChart, steps: [
  { cap: "<b>Analysis.</b> Find out what the program must do: the problem and its requirements. Use abstraction and decomposition.", s: { k: 0 } },
  { cap: "<b>Design.</b> Plan the solution with structure diagrams, flowcharts and pseudocode.", s: { k: 1 } },
  { cap: "<b>Coding.</b> Write the program code, testing each part as it is written (iterative testing).", s: { k: 2 } },
  { cap: "<b>Testing.</b> Run the finished program with test data and compare actual results with expected results.", s: { k: 3 } },
  { cap: "If testing finds an error, the programmer goes <b>back</b> (usually to coding), fixes it and tests again. That is why it is a <b>cycle</b>.", s: { k: 4 } },
] });

/* ---------- 2. abstraction ---------- */
function abChart(s) {
  const k = s.k, dOp = k <= 1 ? 1 - 0.8 * k : Math.max(0, 0.2 * (2 - k)), t = Math.max(0, Math.min(1, k - 1));
  const real = [[120, 215], [300, 105], [480, 225], [650, 95]], names = ["A", "B", "C", "D"];
  let o = `<g opacity="${dOp.toFixed(2)}">`;
  [[20, 60, 740, 70], [20, 250, 740, 240], [180, 20, 190, 290], [380, 20, 420, 290], [560, 20, 540, 290], [20, 160, 740, 170]].forEach((r) => (o += SV.line(r[0], r[1], r[2], r[3], "", { style: "stroke:var(--line);stroke-width:7" })));
  [[60, 90], [230, 160], [250, 250], [440, 80], [520, 160], [600, 250], [700, 160], [340, 270], [90, 255]].forEach((b) => (o += SV.rect(b[0], b[1], 46, 32, "", { rx: 4, style: "fill:var(--soft);stroke:var(--line)" })));
  [[160, 50], [420, 45], [580, 60], [710, 230], [30, 130]].forEach((c) => (o += SV.circle(c[0], c[1], 12, "dot3", { opacity: 0.5 })));
  o += "</g>";
  const pts = real.map((p) => [p[0], p[1] + (150 - p[1]) * t]);
  o += SV.path("M" + pts.map((p) => p.join(" ")).join(" L"), "", { style: `fill:none;stroke:var(--accent);stroke-width:${5 - 0 * t}` });
  pts.forEach((p, i) => (o += SV.circle(p[0], p[1], 13, "dot1") + SV.text(p[0], p[1] + 5, names[i], "lbl bd", { "text-anchor": "middle", style: "fill:#fff" })));
  o += note(380, 300, k < 0.5 ? "A real map: streets, buildings, trees and stations" : k < 1.5 ? "Details the traveller does not need are fading" : "Abstraction: just stations and connections", t > 0.5 ? "t3" : "");
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 316, label: "Abstraction turning a street map into a station diagram", base: { k: 0 }, tween: 1200, dwell: 3800, draw: abChart, steps: [
  { cap: "A real map has streets, buildings and trees. A traveller only needs to know <b>which stations connect to which</b>.", s: { k: 0 } },
  { cap: "<b>Abstraction</b>: the details that do not help (streets, buildings, trees) are hidden.", s: { k: 1 } },
  { cap: "Only the important details are kept: the stations and how they are linked. The problem is now simpler to work with.", s: { k: 2 } },
] });

/* ---------- Lab 1: abstraction ---------- */
(() => {
  const ITEMS = [["Menu items and prices", 1], ["Student's name and class", 1], ["Pickup time", 1], ["Allergy information", 1], ["Student's account balance", 1], ["Colour of the canteen walls", 0], ["The chef's favourite music", 0], ["Number of tiles on the floor", 0], ["Year the building was built", 0], ["Brand of the kitchen ovens", 0]];
  const el = $("#ab"), v = $("#abv");
  const fill = () => { el.innerHTML = ITEMS.map((it, i) => `<label data-i="${i}"><input type="checkbox"> ${it[0]}</label>`).join(""); v.textContent = ""; };
  $("#abc").onclick = () => { let ok = 0; $$("label", el).forEach((l) => { const want = ITEMS[+l.dataset.i][1], got = $("input", l).checked; const good = want === +got; l.classList.toggle("ok", good); l.classList.toggle("no", !good); if (good) ok++; }); v.innerHTML = ok === ITEMS.length ? "All correct. The program needs the items, names, times, allergies and balance. The rest is detail it can ignore: <b>abstraction</b>." : `${ok} of ${ITEMS.length} correct. Green is right. Red: either you ticked something the program does not need, or missed something it does.`; };
  $("#abr").onclick = fill; fill();
})();

/* ---------- Lab 2: which stage ---------- */
chooser($("#sn"), $("#sv"), ST, [
  ["Work out the inputs and outputs the program needs", "Analysis"], ["Draw a flowchart of the algorithm", "Design"], ["Write the loop in Python", "Coding"], ["Run the program with extreme test data", "Testing"],
  ["Break the problem into three smaller parts", "Analysis"], ["Write pseudocode for the password check", "Design"], ["Test one function straight after writing it", "Coding"], ["Compare actual results with expected results", "Testing"],
]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Drag each task to its stage.", buckets: [{ label: "Analysis" }, { label: "Design" }, { label: "Coding" }, { label: "Testing" }], items: [
  { text: "Identify the problem and its requirements", b: 0 },
  { text: "Use abstraction to remove unnecessary detail", b: 0 },
  { text: "Decompose the problem into parts", b: 0 },
  { text: "Draw a structure diagram", b: 1 },
  { text: "Draw a flowchart", b: 1 },
  { text: "Write pseudocode", b: 1 },
  { text: "Write the program code", b: 2 },
  { text: "Test each part as it is written", b: 2 },
  { text: "Fix errors straight away", b: 2 },
  { text: "Run with test data", b: 3 },
  { text: "Compare actual and expected results", b: 3 },
  { text: "Check the finished program works", b: 3 },
], done: "Analyse, design, code, test." });

Lib.classify($("#cl2"), { prompt: "Which technique is each statement describing?", buckets: [{ label: "Abstraction" }, { label: "Decomposition" }], items: [
  { text: "Hiding details that are not needed", b: 0 },
  { text: "Keeping only what matters", b: 0 },
  { text: "A map showing only stations and lines", b: 0 },
  { text: "Focusing on the important features", b: 0 },
  { text: "Splitting a problem into smaller parts", b: 1 },
  { text: "Each part can be solved and tested separately", b: 1 },
  { text: "A game split into graphics, sound and scoring", b: 1 },
  { text: "Breaking each part down again", b: 1 },
], done: "Detail removed against problem split." });

Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Abstraction", "Removing unnecessary detail and keeping what matters"],
  ["Decomposition", "Breaking a problem into smaller parts"],
  ["Requirements", "What the program must do"],
  ["Iterative testing", "Testing each part of the program as it is written"],
  ["Test data", "Chosen values used to test a program"],
  ["Flowchart", "A diagram of an algorithm using shapes and arrows"]
] });

Lib.order($("#o1"), { prompt: "Put these tasks for building a temperature logger in the order they happen.", items: [
  "Decide what data must be recorded and displayed",
  "Draw a flowchart of how the readings are processed",
  "Write the code that reads the sensor and test it",
  "Run the finished program with test data",
  "Fix an error found in testing and test again"
], done: "Analyse, design, code, test, fix." });

Lib.quiz($("#qz1"), { qs: [
  { q: "Which stage uses abstraction?", opts: ["Analysis", "Coding", "Testing", "Maintenance"], a: 0, why: "Abstraction is used in analysis to remove unnecessary detail." },
  { q: "Which is a design method?", opts: ["Flowchart", "Test data", "Compiler", "Debugger"], a: 0, why: "Flowcharts, structure diagrams and pseudocode are design methods." },
  { q: "What is decomposition?", opts: ["Hiding all detail", "Breaking a problem into smaller parts", "Writing code", "Running tests"], a: 1, why: "Decomposition splits a problem into parts." },
  { q: "What is iterative testing?", opts: ["Testing only at the end", "Testing parts of the program as they are written", "Testing with no data", "Testing the design"], a: 1, why: "Parts are tested repeatedly while coding." },
  { q: "What is compared in the testing stage?", opts: ["Actual and expected results", "Two flowcharts", "Two programmers", "Code and comments"], a: 0, why: "Actual results are compared with expected results." },
  { q: "Testing finds an error. What happens next?", opts: ["The program is released", "The programmer returns to an earlier stage, fixes it and retests", "The testing stage is removed", "Nothing"], a: 1, why: "It is a cycle: errors send you back." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Program development life cycle", "The four stages of making a program: analysis, design, coding and testing."],
  ["Analysis", "Identify the problem and requirements, using abstraction and decomposition."],
  ["Design", "Plan the solution using decomposition, structure diagrams, flowcharts and pseudocode."],
  ["Coding", "Write the program code and test it iteratively."],
  ["Testing", "Run the program with test data and compare actual and expected results."],
  ["Abstraction", "Removing unnecessary detail and keeping what matters."],
  ["Decomposition", "Breaking a problem into smaller parts."],
  ["Requirements", "What the program must do: inputs, processes, outputs, storage."],
  ["Iterative testing", "Testing each part of a program as it is written, then fixing errors."],
  ["Test data", "Chosen values used to check that a program works."]
] });
