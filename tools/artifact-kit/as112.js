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
  const draw = (s) => { const k = Math.round(s.i); const L = [["FOR Count ← 1 TO 3", "runs 3 times: count-controlled"], ["WHILE X < 3", "tests first, then runs"], ["REPEAT ... UNTIL X >= 3", "runs, then tests"], ["Loop ends: test satisfied", "(or counter past the end)"]]; let o = SV.rect(10, 10, 320, 34, k === 3 ? "f2" : "cell", { rx: 6 }) + SV.text(24, 33, L[k][0], "lbl bd", { style: "font-size:14px;font-family:monospace" }); o += SV.text(24, 66, L[k][1], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 340, h: 82, label: "Loops", base: { i: 0 }, draw, tween: 100, dwell: 2000, steps: ["FOR repeats a set number of times.", "WHILE tests before each pass.", "REPEAT tests after each pass.", "All three end when the condition says so."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const cl = [1, 2, 3, "OTHERWISE"]; const draw = (s) => { const k = Math.round(s.i); let o = SV.text(14, 18, "CaseVar = " + [2, 2, 7][k > 2 ? 2 : k > 0 ? 1 : 0], "lbl bd", { style: "font-size:13px" }); const val = [2, 2, 7][k > 2 ? 2 : k > 0 ? 1 : 0]; const hit = val === 1 ? 0 : val === 2 ? 1 : val === 3 ? 2 : 3; cl.forEach((c, i) => o += SV.rect(14, 28 + i * 28, 200, 24, k >= 1 && i === hit ? "f3" : "cell", { rx: 4 }) + SV.text(22, 45 + i * 28, c + " : ThisChar ← " + ["'a'", "'y'", "'7'", "'*'"][i], "lbl bd", { style: "font-size:12px;font-family:monospace" })); o += SV.text(14, 152, k === 0 ? "Test CaseVar against each clause value" : k === 1 ? "Only the matching clause runs" : "Nothing matches: OTHERWISE runs", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 330, h: 165, label: "CASE", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["CaseVar is compared with each value.", "CaseVar = 2: clause 2 runs, the others are skipped.", "CaseVar = 7 matches nothing, so OTHERWISE runs."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const vals = [4, 9, -3, 6]; const draw = (s) => { const k = Math.round(s.i); let o = ""; vals.forEach((v, i) => o += SV.rect(14 + i * 60, 14, 52, 26, i < k ? "f3" : "cell", { rx: 4 }) + SV.text(40 + i * 60, 32, v, "lbl bd", { "text-anchor": "middle" })); const t = vals.slice(0, k).reduce((a, b) => a + b, 0); o += SV.text(14, 66, "Total = " + t + "     Count = " + k, "lbl bd t3", { style: "font-size:14px" }); o += SV.text(14, 88, k === 0 ? "Set Total ← 0 and Count ← 0 before the loop" : k < 4 ? "Total ← Total + value; Count ← Count + 1" : "Loop finished: OUTPUT Total, Count", "lbl", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stC"), { w: 270, h: 104, label: "Total and count", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["Initialise.", "Add the first value.", "Add the second.", "Add the third.", "Add the fourth: the loop ends."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const inp = $("#lp_x"); const paint = () => { let x0 = Math.round(+inp.value || 0); const run = (kind) => { let x = x0, n = 0; if (kind === "FOR") { for (let c = x0; c <= 5; c++) n++; return n; } if (kind === "WHILE") { while (x < 5 && n < 100) { x++; n++; } return n; } do { x++; n++; } while (!(x >= 5) && n < 100); return n; };
    $("#lpV").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Loop</th><th>Test</th><th>Times it runs</th></tr>' + [["FOR X ← " + x0 + " TO 5", "counter ≤ 5", run("FOR")], ["WHILE X < 5", "before each pass", run("WHILE")], ["REPEAT ... UNTIL X >= 5", "after each pass", run("REPEAT")]].map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td><b>${r[2]}</b></td></tr>`).join("") + "</table></div>" + (x0 >= 5 ? '<div class="verdict">X already meets the end condition: WHILE and FOR run zero times, but REPEAT still runs once.</div>' : ""); };
  inp.oninput = paint; paint();
})();
(function () {
  const bar = $("#csB"); const out = $("#csV"); const map = { 1: "'a'", 2: "'y'", 3: "'7'" };
  [1, 2, 3, 4, 7].forEach((v) => { const b = document.createElement("button"); b.textContent = "MySwitch = " + v; b.onclick = () => { bar.querySelectorAll("button").forEach((x) => x.className = x === b ? "on" : ""); const r = map[v] || "'*'"; out.innerHTML = `<div class="verdict">ThisChar = <b>${r}</b> ${map[v] ? "" : "(OTHERWISE / the final ELSE)"}</div><p class="mono">CASE: matches ${map[v] ? "clause " + v : "no clause, so OTHERWISE"}.<br>IF: ${v === 1 ? "the first test is true" : v === 2 ? "the first test is false, the second is true" : v === 3 ? "the first two tests are false, the third is true" : "all three tests are false, so ELSE"}.</p>`; }; bar.appendChild(b); });
})();
btnTable("lcB", "lcO", [
  ["Process exactly 30 students", "FOR", "the count is known"],
  ["Read lines until the end of a file that may be empty", "WHILE", "may run zero times"],
  ["Ask for a PIN at least once, until it is right", "REPEAT ... UNTIL", "must run once before the test"],
  ["Add numbers until a rogue value 0, even if the first is 0", "WHILE", "test before the first pass"],
  ["Step through the 12 months in an array", "FOR", "the count is known"]
], ["Task", "Loop", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which construct is the statement?", buckets: [{"label": "Selection"}, {"label": "Iteration"}, {"label": "Assignment"}], items: [{"text": "IF Mark > 74 THEN", "b": 0}, {"text": "WHILE AllDone() = TRUE", "b": 1}, {"text": "Count ← Count + 1", "b": 2}, {"text": "CASE OF CaseVar", "b": 0}, {"text": "FOR Index ← 1 TO 3", "b": 1}, {"text": "Total ← 0", "b": 2}], done: "Choose, repeat, store." });
Lib.classify($("#cl2"), { prompt: "Which loop is best?", buckets: [{"label": "FOR"}, {"label": "WHILE"}, {"label": "REPEAT ... UNTIL"}], items: [{"text": "Process exactly 30 students", "b": 0}, {"text": "Read lines until the end of a file, which might be empty", "b": 1}, {"text": "Ask for a password at least once, until it is right", "b": 2}, {"text": "Step through an array of 12 months", "b": 0}, {"text": "Add values until the rogue value 0 is input; the first input may already be 0", "b": 1}, {"text": "Show a menu and repeat until Quit is chosen", "b": 2}], done: "Known count: FOR. May run zero times: WHILE. Run at least once: REPEAT." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Sequence", "Statements run in order"], ["Selection", "A choice (IF, CASE)"], ["Iteration", "Repetition (FOR, WHILE, REPEAT)"], ["Count-controlled", "A set number of repeats"], ["Condition-controlled", "Repeats until a test is satisfied"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the algorithm for counting the values 100 to 200 that end in 7 in order.", items: ["Declare ThisInt and Count and set Count to 0", "FOR ThisInt from 100 to 200", "IF ThisInt MOD 10 = 7", "OUTPUT ThisInt and add 1 to Count", "After the loop OUTPUT Count"], done: "Initialise, loop, test, act, report." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many values from 100 to 200 inclusive end in the digit 7?", "a": 10, "unit": "", "tol": 0.01, "hint": "107, 117 ... 197.", "sol": "<b>10</b>."},
  {"q": "How many times does FOR Index ← 1 TO 20 STEP 3 run?", "a": 7, "unit": "", "tol": 0.01, "hint": "1, 4, 7, 10, 13, 16, 19.", "sol": "<b>7</b>."},
  {"q": "A REPEAT loop starts with X = 10 and stops UNTIL X >= 5, adding 1 each time. How many times does it run?", "a": 1, "unit": "", "tol": 0.01, "hint": "Tested after the first pass.", "sol": "<b>1</b>."},
  {"q": "A WHILE loop starts with X = 10, runs WHILE X < 5. How many times does it run?", "a": 0, "unit": "", "tol": 0.01, "hint": "Tested first.", "sol": "<b>0</b>."},
  {"q": "A CASE has clauses 1, 2, 3, 4 and OTHERWISE. CaseVar is 9. Which clause runs?", "a": 5, "unit": "th clause", "tol": 0.01, "hint": "Counting OTHERWISE as the fifth.", "sol": "<b>OTHERWISE</b> (the fifth clause)."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The loop that tests its condition last:", opts: ["REPEAT ... UNTIL", "WHILE", "FOR", "CASE"], a: 0, why: "Post-condition." },
  { q: "A loop that may run zero times:", opts: ["WHILE", "REPEAT ... UNTIL", "Both", "Neither"], a: 0, why: "WHILE tests first." },
  { q: "CASE OTHERWISE covers:", opts: ["Any value not listed", "Only the first value", "The end of the program", "Errors only"], a: 0, why: "Default." },
  { q: "A program freezes. A likely cause:", opts: ["A conditional loop whose end condition is never true", "A FOR loop with 10 passes", "An IF statement", "A constant"], a: 0, why: "Infinite loop." },
  { q: "Initialise a total:", opts: ["Before the loop", "Inside the loop at the start", "After the loop", "Never"], a: 0, why: "Else it restarts." },
  { q: "Which is not a construct?", opts: ["Variable", "Selection", "Iteration", "Sequence"], a: 0, why: "A variable is data." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Selection", "Choose a path: IF, CASE."],
  ["Iteration", "Repeat: FOR, WHILE, REPEAT."],
  ["FOR", "Count-controlled."],
  ["WHILE", "Test first; may not run."],
  ["REPEAT", "Test last; runs once at least."],
  ["OTHERWISE", "The default CASE clause."],
  ["Infinite loop", "End condition never true."],
  ["Initialise", "Set counts and totals before a loop."],
] });
