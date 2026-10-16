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
/* ---------- 1. number line ---------- */
const NL = { lo: 1, hi: 100, x0: 60, x1: 700, min: -20, max: 125 };
const nx = (v) => NL.x0 + ((v - NL.min) / (NL.max - NL.min)) * (NL.x1 - NL.x0);
function nlChart(s) {
  const k = Math.round(s.k);
  let o = SV.rect(nx(NL.lo), 95, nx(NL.hi) - nx(NL.lo), 36, "", { rx: 4, style: "fill:var(--good-soft);stroke:var(--good);stroke-width:2" }) + sm((nx(NL.lo) + nx(NL.hi)) / 2, 118, "accepted: 1 to 100") + SV.line(NL.x0, 150, NL.x1, 150, "", { style: "stroke:var(--muted);stroke-width:3" });
  [1, 50, 100, -20, 120].forEach((v) => (o += SV.line(nx(v), 144, nx(v), 156, "", { style: "stroke:var(--muted);stroke-width:2" }) + sm(nx(v), 174, v)));
  const pt = (v, col, lab, up) => SV.circle(nx(v), 150, up === 1 ? 13 : 8, "", { style: up === 1 ? `fill:none;stroke:${col};stroke-width:4` : `fill:${col}` }) + SV.text(nx(v), up ? 70 - (up - 1) * 22 : 205, lab, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) + SV.line(nx(v), up ? 160 - 0 : 160, nx(v), up ? 160 : 190, "", { style: "stroke:none" });
  if (k >= 1) o += pt(50, ACC, "50 normal", 0);
  if (k >= 2) o += pt(1, GOOD, "1 extreme", 0).replace(/y="205"/, 'y="205"') + pt(100, GOOD, "100 extreme", 0);
  if (k >= 3) o += pt(0, WARN, "0 boundary", 1) + pt(101, WARN, "101 boundary", 1);
  if (k >= 4) o += pt(-15, BAD, "−15", 2) + pt(115, BAD, "115", 2) + SV.rect(285, 215, 190, 30, "", { rx: 14, style: "fill:var(--bad)" }) + SV.text(380, 235, "\"abc\"  abnormal", "lbl bd", { "text-anchor": "middle", style: "fill:#fff" });
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 255, label: "Test data on a number line for a range of 1 to 100", base: { k: 0 }, tween: 1, dwell: 3800, draw: nlChart, steps: [
  { cap: "A program accepts whole numbers from <b>1 to 100</b>. The green zone is the accepted range.", s: { k: 0 } },
  { cap: "<b>Normal</b> data: a typical value well inside the range, such as 50. Expected: accepted.", s: { k: 1 } },
  { cap: "<b>Extreme</b> data: the smallest and largest acceptable values, <b>1</b> and <b>100</b>. Expected: accepted.", s: { k: 2 } },
  { cap: "<b>Boundary</b> data adds the nearest <b>rejected</b> values, <b>0</b> and <b>101</b>, either side of the limits. Expected: rejected.", s: { k: 3 } },
  { cap: "<b>Abnormal</b> data should be rejected: values far outside the range, or the wrong data type such as text.", s: { k: 4 } },
] });

/* ---------- 2. a test plan ---------- */
const TP = [["40", "Normal", "Accepted", "Accepted", 1], ["18", "Extreme", "Accepted", "Rejected", 0], ["17", "Boundary", "Rejected", "Rejected", 1], ["65", "Extreme", "Accepted", "Accepted", 1], ["abc", "Abnormal", "Rejected", "Rejected", 1]];
function tpChart(s) {
  const k = Math.round(s.k), xs = [40, 150, 270, 400, 530];
  let o = ["Test data", "Type", "Expected", "Actual", "Result"].map((t, i) => SV.text(xs[i], 28, t, "lbl bd", { "text-anchor": "start", style: "font-size:12px" })).join("") + SV.line(30, 38, 720, 38, "", { style: "stroke:var(--muted);stroke-width:2" });
  TP.forEach((r, i) => { if (i >= k) return; const y = 72 + i * 38, bad = !r[4]; if (bad) o += SV.rect(30, y - 22, 690, 32, "", { rx: 8, style: "fill:var(--bad-soft)" });
    [r[0], r[1], r[2], r[3], r[4] ? "✓ pass" : "✗ FAIL"].forEach((t, j) => (o += SV.text(xs[j], y, t, "lbl bd", { "text-anchor": "start", style: `font-size:13px;${j === 4 ? `fill:${r[4] ? "var(--good)" : "var(--bad)"}` : ""}` }))); });
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 270, label: "A test plan that finds an error", base: { k: 1 }, tween: 1, dwell: 3800, draw: tpChart, steps: [
  { cap: "The age check should accept 18 to 65. The code written is <b>IF Age &gt; 18 AND Age &lt;= 65</b>. Test 1: <b>40</b>, normal data, passes.", s: { k: 1 } },
  { cap: "Test 2: <b>18</b>, an extreme value. Expected: accepted. Actual: <b>rejected</b>. The test <b>fails</b>: an error has been found.", s: { k: 2 } },
  { cap: "Test 3: <b>17</b>, boundary. Expected: rejected. Actual: rejected. Pass.", s: { k: 3 } },
  { cap: "Test 4: <b>65</b>. Passes. Test 5: <b>abc</b>, abnormal. Rejected. Passes.", s: { k: 5 } },
  { cap: "A normal value like 40 would never have found the bug. Only the <b>extreme</b> test did. The code is corrected to <b>Age &gt;= 18</b> and all tests are run again.", s: { k: 5 } },
] });

/* ---------- Learn code ---------- */
Lib.codePanel($("#cdRng"), { pseudo: ["IF Age >= 18 AND Age <= 65", "  THEN", '    OUTPUT "Accepted"', "  ELSE", '    OUTPUT "Rejected"', "ENDIF"], py: ["if 18 <= age <= 65:", '    print("Accepted")', "else:", '    print("Rejected")'] });

/* ---------- Lab 1 ---------- */
(() => {
  let lo, hi; const rv = $("#rv");
  function upd() {
    if (!lo || !hi) return;
    let a = lo.get(), b = hi.get(); if (b <= a) { b = a + 1; }
    const mid = Math.round((a + b) / 2);
    $("#rt").innerHTML = `<tr><th>Type</th><th>Test data</th><th>Expected</th></tr><tr><td>Normal</td><td>${mid}</td><td>Accepted</td></tr><tr><td>Extreme</td><td>${a}, ${b}</td><td>Accepted</td></tr><tr><td>Boundary</td><td>${a - 1}, ${a}, ${b}, ${b + 1}</td><td>${a}, ${b} accepted; ${a - 1}, ${b + 1} rejected</td></tr><tr><td>Abnormal</td><td>${a - 20}, ${b + 20}, "abc"</td><td>Rejected</td></tr>`;
    const t = rv.value.trim(); let r;
    if (!/^-?\d+$/.test(t)) r = `<span class="flag">Abnormal</span> "${esc(t)}" is not a whole number, so it should be <b>rejected</b>.`;
    else { const n = +t, inR = n >= a && n <= b;
      if (n === a || n === b) r = `<span class="okf">Extreme</span> ${n} is the ${n === a ? "smallest" : "largest"} acceptable value (it is also a boundary value). It should be <b>accepted</b>.`;
      else if (n === a - 1 || n === b + 1) r = `<span class="flag">Boundary</span> ${n} is the nearest rejected value ${n < a ? "below" : "above"} the range. It should be <b>rejected</b>.`;
      else if (inR) r = `<span class="okf">Normal</span> ${n} is a typical value inside the range. It should be <b>accepted</b>.`;
      else r = `<span class="flag">Abnormal</span> ${n} is far outside the range. It should be <b>rejected</b>.`; }
    $("#rvv").innerHTML = r;
  }
  lo = Lib.slider($("#r1"), { id: "rl", label: "Lowest allowed", min: 0, max: 40, value: 1, onInput: upd });
  hi = Lib.slider($("#r2"), { id: "rh", label: "Highest allowed", min: 10, max: 120, value: 100, onInput: upd });
  rv.addEventListener("input", upd); upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  const V = [["Version 1", "IF Age >= 18 AND Age <= 65", (a) => a >= 18 && a <= 65], ["Version 2", "IF Age > 18 AND Age <= 65", (a) => a > 18 && a <= 65], ["Version 3", "IF Age >= 18 AND Age < 65", (a) => a >= 18 && a < 65]];
  const sel = $("#bv"), log = $("#bl"), msg = $("#bm"), inp = $("#bi"); let rows = [];
  sel.innerHTML = V.map((v, i) => `<option value="${i}">${v[0]}</option>`).join("");
  const show = () => Lib.codePanel($("#bcode"), { pseudo: [V[+sel.value][1], "  THEN", '    OUTPUT "Accepted"', "  ELSE", '    OUTPUT "Rejected"', "ENDIF"], py: [V[+sel.value][1].replace("IF ", "if ").replace(/Age/g, "age").replace(/AND/g, "and") + ":", '    print("Accepted")', "else:", '    print("Rejected")'] });
  function run(t) {
    t = String(t).trim(); const isN = /^-?\d+$/.test(t), n = +t, exp = isN && n >= 18 && n <= 65, act = isN && V[+sel.value][2](n);
    if (rows.some((r) => r[0] === t)) return;
    rows.push([t, exp ? "Accepted" : "Rejected", act ? "Accepted" : "Rejected", exp === act]); draw();
  }
  function draw() {
    log.innerHTML = `<tr><th>Test</th><th>Expected</th><th>Actual</th><th>Result</th></tr>` + rows.map((r) => `<tr style="${r[3] ? "" : "background:var(--bad-soft)"}"><td>${esc(r[0])}</td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3] ? "✓" : "✗ FAIL"}</td></tr>`).join("");
    const f = rows.filter((r) => !r[3]);
    msg.innerHTML = !rows.length ? "Run a test." : f.length ? `<b>Error found.</b> ${f.map((r) => r[0]).join(", ")} gave the wrong result. It is an <b>extreme/boundary</b> value, which a normal value would have missed.` : sel.value === "0" ? "All tests pass. This version is correct. Try the other versions with the standard set." : "No failures yet. Try the extreme values 18 and 65 and the boundaries 17 and 66.";
  }
  $("#bt").onclick = () => run(inp.value); $("#bs").onclick = () => ["40", "18", "65", "17", "66", "abc"].forEach(run); $("#bc").onclick = () => { rows = []; draw(); };
  sel.onchange = () => { rows = []; show(); draw(); }; show(); draw();
})();

/* ---------- Lab 3 ---------- */
chooser($("#sn"), $("#sv"), ["Normal", "Abnormal", "Extreme", "Boundary (just outside)"], [
  ["25", "Normal"], ["1", "Extreme"], ["50", "Extreme"], ["0", "Boundary (just outside)"], ["51", "Boundary (just outside)"], ["\"five\"", "Abnormal"], ["75", "Abnormal"], ["−2", "Abnormal"],
]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "A program accepts whole numbers from 1 to 100. Sort each test value.", buckets: [{ label: "Normal" }, { label: "Abnormal" }, { label: "Extreme" }, { label: "Boundary (rejected side)" }], items: [
  { text: "50", b: 0 },
  { text: "33", b: 0 },
  { text: "72", b: 0 },
  { text: "\"abc\"", b: 1 },
  { text: "250", b: 1 },
  { text: "−7", b: 1 },
  { text: "1", b: 2 },
  { text: "100", b: 2 },
  { text: "0", b: 3 },
  { text: "101", b: 3 },
], done: "Normal inside, abnormal far outside or wrong type, extreme the edges, boundary just outside." });

Lib.classify($("#cl2"), { prompt: "A program accepts ages from 18 to 65 inclusive. Should each value be accepted or rejected?", buckets: [{ label: "Accepted" }, { label: "Rejected" }], items: [
  { text: "18", b: 0 },
  { text: "65", b: 0 },
  { text: "40", b: 0 },
  { text: "30", b: 0 },
  { text: "17", b: 1 },
  { text: "66", b: 1 },
  { text: "0", b: 1 },
  { text: "\"ten\"", b: 1 },
  { text: "100", b: 1 },
], done: "The limits themselves are accepted; just outside is rejected." });

Lib.match($("#m1"), { prompt: "Match each type of test data to its meaning.", pairs: [
  ["Normal", "Typical valid data that should be accepted"],
  ["Abnormal", "Data that should be rejected, such as the wrong type"],
  ["Extreme", "The largest and smallest acceptable values"],
  ["Boundary", "The edge values plus the nearest rejected values"],
  ["Expected result", "What a test should produce, worked out in advance"],
  ["Test plan", "A table of test data, expected and actual results"]
] });

Lib.order($("#o1"), { prompt: "Put the steps of testing a program in order.", items: [
  "Choose test data of each type",
  "Work out the expected result for each test",
  "Run the program with each piece of test data",
  "Compare the actual results with the expected results",
  "Correct any errors and test again"
], done: "Choose, predict, run, compare, fix." });

Lib.calc($("#c1"), { qs: [
  { q: "A program accepts whole numbers from 1 to 12 (months). What is the smallest extreme value?", a: 1, sol: "The smallest acceptable value: 1." },
  { q: "What is the largest boundary value that should be rejected for a range of 1 to 12?", a: 13, sol: "The nearest rejected value above 12 is 13." },
  { q: "A range check accepts 18 to 65. How many whole-number boundary test values are there in total (both limits, accepted and rejected sides)?", a: 4, sol: "17, 18, 65, 66." },
  { q: "A password must be 8 to 12 characters. What is the smallest length that should be rejected at the top end?", a: 13, sol: "13 characters is the nearest rejected length above 12." },
  { q: "How many test data types are there?", a: 4, sol: "Normal, abnormal, extreme and boundary." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "What is normal test data?", opts: ["Valid typical data", "Data that crashes the program", "Only the largest value", "Text only"], a: 0, why: "Typical valid data that should be accepted." },
  { q: "Which value is extreme for a range of 1 to 50?", opts: ["25", "50", "51", "abc"], a: 1, why: "50 is the largest acceptable value." },
  { q: "Which is boundary data (rejected side) for a range of 1 to 50?", opts: ["0", "25", "50", "30"], a: 0, why: "0 is the nearest rejected value below 1." },
  { q: "Which is abnormal data for an integer range?", opts: ["10", "abc", "1", "50"], a: 1, why: "Text is the wrong data type, so it should be rejected." },
  { q: "Why test with 18 when the range is 18 to 65?", opts: ["It finds > instead of >=", "It is the most common age", "It is normal data", "To crash the program"], a: 0, why: "A > 18 error rejects 18." },
  { q: "What is compared in testing?", opts: ["Actual and expected results", "Two flowcharts", "Two programmers", "Code and comments"], a: 0, why: "Actual results against expected results." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Test data", "Chosen values used to check that a program works."],
  ["Normal data", "Typical valid data that should be accepted."],
  ["Abnormal data", "Data that should be rejected, such as the wrong data type or a value far outside the range."],
  ["Extreme data", "The largest and smallest acceptable values."],
  ["Boundary data", "The largest and smallest acceptable values and the nearest rejected values either side."],
  ["Expected result", "What the program should produce for a test, worked out in advance."],
  ["Test plan", "A table of test data, types, expected results and actual results."]
] });
