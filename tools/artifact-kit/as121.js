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
  const N = ["Analysis", "Design", "Coding", "Testing", "Maintenance"];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; N.forEach((n, i) => { const y = 6 + i * 40; o += SV.rect(40, y, 150, 24, i === k ? "f3" : i < k ? "f1" : "cell", { rx: 5 }) + SV.text(115, y + 17, n, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); if (i < N.length - 1) o += SV.text(85, y + 38, "↓", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }) + SV.text(145, y + 38, "↑", "lbl bd t2", { "text-anchor": "middle", style: "font-size:13px" }); }); return o; };
  Lib.stepper($("#stA"), { w: 230, h: 210, label: "Waterfall", base: { i: 0 }, draw, tween: 100, dwell: 2000, steps: ["Analysis: find out what is needed.", "Design: plan how it will work.", "Coding: write the program.", "Testing: check it works.", "Maintenance: keep it working. The up arrows allow a return to an earlier stage."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; for (let i = 0; i < 4; i++) { const x = 10 + i * 90; o += SV.rect(x, 12, 80, 40, i < k ? "f3" : "cell", { rx: 6 }) + SV.text(x + 40, 36, "Version " + (i + 1), "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); if (i < 3) o += SV.text(x + 82, 36, "→", "lbl", { style: "font-size:14px" }); } o += SV.text(10, 78, ["The client has some ideas.", "Prototype 1: the client reviews it.", "Prototype 2: with the feedback built in.", "Prototype 3: more features.", "Final version: agreed with the client."][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 380, h: 94, label: "Iteration", base: { i: 0 }, draw, tween: 100, dwell: 2000, steps: ["Start with the client's ideas.", "Build the first prototype.", "Improve it from the feedback.", "Add more features.", "Repeat until the client is happy."].map((c, i) => ({ cap: c, s: { i } })) });
})();
btnTable("stB1", "stO1", [
  ["Interviewing the client about the current system", "Analysis", "finding out"],
  ["Defining records and file structures", "Design", "planning how it works"],
  ["Implementing an algorithm in a language", "Coding", "writing"],
  ["Using a walkthrough or a trace table", "Testing", "checking"],
  ["Modifying the program for new hardware", "Maintenance", "after release"],
  ["Choosing a data structure", "Design", "decided in design"]
], ["Activity", "Stage", "Why"]);
btnTable("wrB", "wrO", [
  ["Requirements likely to change; first to market wins", "Iterative / RAD", "prototype early, changes easy"],
  ["Large project, fixed requirements, fixed budget", "Waterfall", "predictable cost and time"],
  ["Principal unclear on details, wants to see an early version", "Iterative / RAD", "client reviews a prototype"],
  ["All requirements are signed off before coding starts", "Waterfall", "no late changes"]
], ["Scenario", "Model", "Why"]);
(function () {
  const sel = $("#rq_st"); const paint = () => { const k = +sel.value; const wf = k === 1 ? "design, coding and testing may need to be redone" : k === 2 ? "the design, the code and the testing may need to be redone" : "almost everything is redone, and the product may already be released"; const rad = "only the current prototype is changed, in the next cycle"; $("#rqV").innerHTML = `<div class="tw"><table class="t"><tr><th>Model</th><th>Effect of the change</th></tr><tr><td>Waterfall</td><td>${wf}</td></tr><tr><td>Iterative / RAD</td><td>${rad}</td></tr></table></div><div class="verdict">A change late in a waterfall project is expensive; an iterative project absorbs it in the next prototype.</div>`; };
  sel.onchange = paint; paint();
})();
Lib.classify($("#cl1"), { prompt: "Which stage of the life cycle?", buckets: [{"label": "Analysis"}, {"label": "Design"}, {"label": "Coding"}, {"label": "Testing"}, {"label": "Maintenance"}], items: [{"text": "The client is interviewed about problems with the current system", "b": 0}, {"text": "An identifier table is produced", "b": 1}, {"text": "An algorithm is implemented in a programming language", "b": 2}, {"text": "A trace table is produced", "b": 3}, {"text": "The program is modified to run on new hardware", "b": 4}, {"text": "Records and file structures are defined", "b": 1}], done: "Find out, plan, write, check, keep up to date." });
Lib.classify($("#cl2"), { prompt: "Which model fits the description?", buckets: [{"label": "Waterfall"}, {"label": "Iterative / RAD"}], items: [{"text": "Each stage is finished before the next starts", "b": 0}, {"text": "A prototype is produced at an early stage", "b": 1}, {"text": "The client reviews each increment", "b": 1}, {"text": "All requirements are identified before coding", "b": 0}, {"text": "Late changes to requirements are hard to include", "b": 0}, {"text": "Minimal detailed planning, so changes are easy", "b": 1}], done: "Sequence: waterfall. Prototypes: RAD." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Analysis", "Requirements specification"], ["Design", "Algorithms, data structures and test plan"], ["Coding", "The program code"], ["Testing", "Test results and a fault list"], ["Maintenance", "An updated program"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the waterfall stages in order.", items: ["Analysis", "Design", "Coding", "Testing", "Maintenance"], done: "A, D, C, T, M." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many stages does the life cycle in this page have?", "a": 5, "unit": "", "tol": 0.01, "hint": "Analysis to maintenance.", "sol": "<b>5</b>."},
  {"q": "A project has 12 modules developed in 4 equal parallel teams. How many modules does each team build?", "a": 3, "unit": "", "tol": 0.01, "hint": "12 ÷ 4.", "sol": "<b>3</b>."},
  {"q": "A waterfall project has 5 stages of 2 months each. How many months until all stages are complete?", "a": 10, "unit": "", "tol": 0.01, "hint": "5 × 2.", "sol": "<b>10</b>."},
  {"q": "A RAD project delivers a prototype every 3 weeks. How many prototypes are there in 15 weeks?", "a": 5, "unit": "", "tol": 0.01, "hint": "15 ÷ 3.", "sol": "<b>5</b>."},
  {"q": "A feasibility study is part of which stage? (1 analysis, 2 design, 3 coding)", "a": 1, "unit": "", "tol": 0.01, "hint": "Done first.", "sol": "<b>1</b>: analysis."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a design activity?", opts: ["Choosing a data structure", "Interviewing the client", "Fixing a syntax error", "Running beta testing"], a: 0, why: "Design." },
  { q: "The model with a prototype early:", opts: ["Iterative / RAD", "Waterfall", "Neither", "Both"], a: 0, why: "RAD." },
  { q: "A drawback of RAD:", opts: ["Cost and time are hard to estimate", "No prototypes", "Needs all requirements first", "No client contact"], a: 0, why: "Hard to estimate." },
  { q: "Upward arrows in the waterfall model mean:", opts: ["Return to a previous stage", "Skip a stage", "Finish the project", "Cancel"], a: 0, why: "Rework." },
  { q: "A feasibility study belongs to:", opts: ["Analysis", "Coding", "Testing", "Maintenance"], a: 0, why: "Analysis." },
  { q: "A trace table is produced in:", opts: ["Testing", "Analysis", "Coding", "Maintenance"], a: 0, why: "Testing." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Analysis", "Find out what is needed."],
  ["Design", "Plan how it will work."],
  ["Coding", "Write the program."],
  ["Testing", "Check it works."],
  ["Maintenance", "Keep it working."],
  ["Waterfall", "Stages in sequence."],
  ["RAD", "Prototypes and cycles."],
  ["Prototype", "An early working version."],
] });
