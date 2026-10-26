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
  const L = ["WHILE Count <= 10  ... NEXT Count", "Total ← Total + Value (needs *)", "Result ← 100 / Zero", "IF Mark > 74 THEN ... without ENDIF"]; const K = ["Syntax error: NEXT instead of ENDWHILE", "Logic error: the program runs but the answer is wrong", "Run-time error: divide by zero stops the program", "Syntax error: the program will not compile"]; const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(10, 8, 340, 34, "cell", { rx: 6 }) + SV.text(20, 30, L[k], "lbl bd", { style: "font-size:12px;font-family:monospace" }); o += SV.text(14, 66, K[k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stA"), { w: 360, h: 80, label: "Errors", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["A line that breaks the rules.", "A line that runs but computes the wrong thing.", "A line that is impossible at run time.", "Another syntax error."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; const vals = [148, 149, 150, 153, 155, 156, 157]; vals.forEach((v, i) => { const ok = v >= 150 && v <= 155; const on = k === 0 ? false : k === 1 ? (v === 150 || v === 155) : k === 2 ? (v === 149 || v === 156) : v === 153; o += SV.rect(8 + i * 48, 14, 44, 28, on ? "f3" : ok ? "f1" : "cell", { rx: 4 }) + SV.text(30 + i * 48, 33, v, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); }); o += SV.text(8, 66, ["Accepted range: 150 to 155 (shaded)", "Boundary: the lowest and highest accepted values", "Abnormal boundary: just outside the range", "Normal: a typical value inside"][k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 350, h: 80, label: "Boundaries", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["The valid range.", "The boundary values.", "The values just outside.", "A normal value."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const N = [["Alpha", "developers, in-house"], ["Beta", "a small group of users"], ["Acceptance", "the customer on their own hardware"]]; let o = ""; N.forEach((n, i) => o += SV.rect(10 + i * 110, 14, 100, 30, i === k ? "f3" : i < k ? "f1" : "cell", { rx: 5 }) + SV.text(60 + i * 110, 34, n[0], "lbl bd", { "text-anchor": "middle", style: "font-size:12px" })); o += SV.text(10, 70, N[k][0] + ": " + N[k][1], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stC"), { w: 350, h: 84, label: "Final testing", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["Alpha: the developers test it in-house.", "Beta: real users find the remaining problems.", "Acceptance: the customer tests the whole system."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const lo = 150, hi = 155, vals = [-5, 12, 148, 149, 150, 151, 153, 154, 155, 156, 157, 200]; const sel = new Set(); const bar = $("#tpB");
  const kind = (v) => v < lo - 1 || v > hi + 1 ? "Abnormal" : v === lo - 1 || v === hi + 1 ? "Abnormal and boundary" : v === lo || v === hi ? "Boundary (accepted)" : "Normal";
  const paint = () => { const have = [...sel].map(kind); const need = [["Normal", "Normal"], ["Lowest accepted (150)", sel.has(150)], ["Highest accepted (155)", sel.has(155)], ["Just below (149)", sel.has(149)], ["Just above (156)", sel.has(156)], ["Clearly abnormal", [...sel].some((v) => v < 149 || v > 156)]]; need[0][1] = have.includes("Normal");
    $("#tpV").innerHTML = '<div class="tw"><table class="t"><tr><th>Test data</th><th>Type</th><th>Expected result</th></tr>' + [...sel].sort((a, b) => a - b).map((v) => `<tr><td>${v}</td><td>${kind(v)}</td><td>${v >= lo && v <= hi ? "PASS" : "FAIL"}</td></tr>`).join("") + '</table></div><div class="verdict">' + need.map((n) => (n[1] ? "✓ " : "✗ ") + n[0]).join(" &nbsp; ") + "</div>" + (need.every((n) => n[1]) ? "<p>A thorough plan: every kind of test is covered.</p>" : "<p>Add the missing kinds of test data.</p>"); };
  vals.forEach((v) => { const b = document.createElement("button"); b.textContent = v; b.onclick = () => { if (sel.has(v)) sel.delete(v); else sel.add(v); b.className = sel.has(v) ? "on" : ""; paint(); }; bar.appendChild(b); }); paint();
})();
btnTable("erB", "erO", [
  ["NEXT Index used instead of ENDWHILE", "Syntax error", "breaks the rules of the language"],
  ["Total adds when it should multiply", "Logic error", "runs, wrong result"],
  ["Division by zero", "Run-time error", "an illegal operation while running"],
  ["Endless loop: the program stops responding", "Run-time error", "the end condition is never met"],
  ["An element outside the array is accessed", "Run-time error (or a logic error in the design)", "the index is outside the range"]
], ["Fault", "Error type", "Why"]);
btnTable("tsB", "tsO", [
  ["Unfinished modules replaced with simple ones that return fixed values", "Stub testing", "the rest can be tested"],
  ["Tests chosen to run every path through known code", "White-box testing", "the code is known"],
  ["Inputs checked against expected outputs, code not inspected", "Black-box testing", "only inputs and outputs"],
  ["A small group of real users try the software before release", "Beta testing", "in the real world"],
  ["The developers test in-house before release", "Alpha testing", "in-house"],
  ["Working modules are combined and tested together", "Integration testing", "modules combined"]
], ["Description", "Testing", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which type of error?", buckets: [{"label": "Syntax"}, {"label": "Logic"}, {"label": "Run-time"}], items: [{"text": "NEXT Index used instead of ENDWHILE", "b": 0}, {"text": "The program divides by zero and crashes", "b": 2}, {"text": "The program adds instead of multiplying, so the total is wrong", "b": 1}, {"text": "An endless loop makes the program stop responding", "b": 2}, {"text": "A misspelt keyword stops the program compiling", "b": 0}, {"text": "A loop runs one time too few and the output is wrong", "b": 1}], done: "Rules of the language: syntax. Wrong result: logic. Crashes or freezes: run-time." });
Lib.classify($("#cl2"), { prompt: "Type of test data for a range of 150 to 155 inclusive?", buckets: [{"label": "Normal"}, {"label": "Boundary"}, {"label": "Abnormal"}], items: [{"text": "153", "b": 0}, {"text": "150", "b": 1}, {"text": "155", "b": 1}, {"text": "200", "b": 2}, {"text": "12", "b": 2}, {"text": "152", "b": 0}], done: "Typical: normal. Edge: boundary. Outside: abnormal." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Walkthrough", "Going through code line by line with a trace table"], ["White-box", "Tests chosen to run every path through the code"], ["Black-box", "Inputs and outputs only, no view of the code"], ["Stub testing", "Simple modules replace unfinished ones"], ["Integration testing", "Modules tested together"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put these in order, from first to last.", items: ["Unit testing of a module", "Integration testing of the modules together", "Alpha testing in-house", "Beta testing by a small group of users", "Acceptance testing by the customer"], done: "Small to large, developers to customer." });
Lib.calc($("#c1"), { qs: [
  {"q": "A range is 24 to 37 inclusive. How many integers are valid?", "a": 14, "unit": "", "tol": 0.01, "hint": "37 − 24 + 1.", "sol": "<b>14</b>."},
  {"q": "A range is 0 to 40 inclusive. The largest abnormal value just above the range is?", "a": 41, "unit": "", "tol": 0.01, "hint": "One more than 40.", "sol": "<b>41</b>."},
  {"q": "A plan tests 23, 24, 25, 36, 37, 38 for 24 to 37. How many of these should be rejected?", "a": 2, "unit": "", "tol": 0.01, "hint": "23 and 38.", "sol": "<b>2</b>."},
  {"q": "A bonus table has four rows (hours and sales combinations). The fewest white-box tests to cover every row?", "a": 4, "unit": "", "tol": 0.01, "hint": "One per path.", "sol": "<b>4</b>."},
  {"q": "A program has 6 modules and 2 are unfinished. How many stubs are needed?", "a": 2, "unit": "", "tol": 0.01, "hint": "One per unfinished module.", "sol": "<b>2</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A program that runs but gives wrong totals has a:", opts: ["Logic error", "Syntax error", "Compile error", "No error"], a: 0, why: "Logic." },
  { q: "Divide by zero is a:", opts: ["Run-time error", "Syntax error", "Logic error", "Design error"], a: 0, why: "Run-time." },
  { q: "Boundary data is:", opts: ["At the edges of the valid range", "Typical data", "Random data", "Invalid data only"], a: 0, why: "Edges." },
  { q: "Beta testing is done by:", opts: ["A small group of potential users", "The developer only", "A compiler", "The customer's lawyers"], a: 0, why: "Real users." },
  { q: "A stub is:", opts: ["A simple module standing in for an unfinished one", "A syntax error", "A test plan", "An IDE tool"], a: 0, why: "Simple module." },
  { q: "A trace table is used in:", opts: ["A walkthrough or dry run", "Compiling", "Beta testing only", "Maintenance only"], a: 0, why: "Dry run." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Syntax error", "Breaks the language rules."],
  ["Logic error", "Wrong result: the algorithm is wrong."],
  ["Run-time error", "Crash or freeze while running."],
  ["Normal data", "Valid and typical."],
  ["Boundary", "At the edge of the range."],
  ["Abnormal", "Should be rejected."],
  ["Stub", "A simple stand-in module."],
  ["Beta testing", "A small group of users."],
] });
