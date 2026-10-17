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

/* ---------- marks pattern ---------- */
const LM = [[5, 1], [6, 3], [7, 10], [8, 24], [9, 1], [10, 1]];
$("#pic1").innerHTML = (() => { let o = SV.line(70, 190, 730, 190) + SV.line(70, 190, 70, 20) + SV.text(76, 16, "Papers (out of 40) by marks for the last part of Section A", "sm"); LM.forEach(([m, n], i) => { const x = 110 + i * 100, h = n * 6.2; o += SV.rect(x, 190 - h, 60, h, m === 8 ? "f3" : "f1", op(0.75)) + SV.text(x + 30, 210, m + " marks", "sm", { "text-anchor": "middle" }) + SV.text(x + 30, 190 - h - 8, n, "lbl bd", { "text-anchor": "middle" }); }); return `<svg viewBox="0 0 760 225" role="img" aria-label="Marks for the last part of Section A across 40 papers: 8 marks in 24, 7 marks in 10, 6 marks in 3 and 5, 9 and 10 marks once each">${o}</svg>`; })();

/* ---------- 40 minutes ---------- */
const MX = (m) => 70 + m * 16.4;
function tmDraw(s) {
  let o = SV.line(70, 150, 730, 150) + SV.text(70, 28, "0", "sm") + SV.text(730, 28, "40 min", "sm", { "text-anchor": "end" });
  [0, 10, 20, 30, 40].forEach((m) => (o += SV.line(MX(m), 144, MX(m), 156) + SV.text(MX(m), 176, m, "sm", { "text-anchor": "middle" })));
  const blk = (a, b, c, l, sub, k) => (k > 0 ? SV.rect(MX(a), 60, MX(b) - MX(a), 76, c, op(0.65 * k)) + SV.text((MX(a) + MX(b)) / 2, 92, l, "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text((MX(a) + MX(b)) / 2, 112, sub, "sm", { "text-anchor": "middle", ...op(k) }) : "");
  o += blk(0, 5, "f2", "Read", "5 min", s.a) + blk(5, 8.4, "f1", "(a)", "2 marks", s.b) + blk(8.4, 15.2, "f1", "(b)", "4 marks", s.c) + blk(15.2, 25.4, "f1", "(c)", "6 marks", s.d) + blk(25.4, 40, "f3", "(d)", "8 marks, about 14 min", s.e);
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 215, label: "A 40 minute plan for Section A with marks 2, 4, 6 and 8", base: { a: 0, b: 0, c: 0, d: 0, e: 0 }, draw: tmDraw, tween: 700, dwell: 5600, steps: [
  { cap: "<b>Read, 5 minutes.</b> Read the four questions first, then the passage and table, underlining data and phrases that answer each part.", s: { a: 1 } },
  { cap: "<b>Part (a), about 3 minutes.</b> A definition or identification: write the answer, check the marks, move on.", s: { a: 1, b: 1 } },
  { cap: "<b>Part (b), about 7 minutes.</b> A short chain of reasoning, with a diagram if the question asks.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Part (c), about 10 minutes.</b> Use the data: quote, calculate, interpret and state a limit.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>Part (d), about 14 minutes.</b> The biggest part: two developed points, a counter-point and a judgement using the passage. Roughly 1.7 minutes per mark overall.", s: { a: 1, b: 1, c: 1, d: 1, e: 1 } },
] });

/* ---------- anatomy of a 6 mark answer ---------- */
const AN = [["1 K", ["The standard of living is the material and non-material", "well-being of people."], "f1"], ["2 A", ["GDP per head at PPP rose 27.8% in X ($9,000 to $11,500)", "and 10% in Y ($4,000 to $4,400)."], "f3"], ["1 A", ["Unemployment fell in both: X from 6% to 5%, Y from 8% to 7.5%."], "f3"], ["1 N", ["The Gini fell in X (0.40 to 0.35), so gains were more evenly spread;", "it rose in Y (0.32 to 0.37), so gains were less evenly spread."], "f1"], ["1 E", ["So material living standards probably rose more in X;", "in Y the average may overstate the gain for typical households."], "f2"], ["1 E", ["The table omits health, education and the environment."], "f2"]];
function anDraw(s) {
  let y = 14, o = "";
  AN.forEach(([m, lines, c], i) => { const k = Math.max(0, Math.min(1, s.n - i)), h = 22 + lines.length * 18; if (k > 0) o += SV.rect(60, y, 660, h, c, op(0.3 * k)) + SV.rect(10, y, 44, h, c, op(0.7 * k)) + SV.text(32, y + h / 2 + 5, m, "lbl bd", { "text-anchor": "middle", ...op(k) }) + lines.map((l, j) => SV.text(72, y + 22 + j * 18, l, "lbl", op(k))).join(""); y += h + 8; });
  return o;
}
Lib.stepper($("#stA"), { w: 740, h: 388, label: "Six sentences that each earn a mark in a 6 mark data question", base: { n: 0 }, draw: anDraw, tween: 700, dwell: 5600, steps: [
  { cap: "<b>Define the term (1 mark).</b> One short sentence shows you know what 'standard of living' means. K = knowledge.", s: { n: 1 } },
  { cap: "<b>Quote and calculate (2 marks).</b> Use numbers, units and a percentage change. A = application of the data.", s: { n: 2 } },
  { cap: "<b>Second indicator (1 mark).</b> Quote the unemployment figures for both countries.", s: { n: 3 } },
  { cap: "<b>Interpret (1 mark).</b> Say what the Gini change means for how the gains are shared. N = analysis.", s: { n: 4 } },
  { cap: "<b>Judge (1 mark).</b> Reach a view about which country improved more and qualify it. E = evaluation.", s: { n: 5 } },
  { cap: "<b>State a limit (1 mark).</b> Say what the data cannot show. Six sentences, six marks.", s: { n: 6 } },
] });

/* ---------- Lab 1 ---------- */
function labP() {
  if (!$("#ov") || !$("#nv")) return;
  const a = +$("#ov").value / 10, b = +$("#nv").value / 10, d = b - a, pc = d / a * 100;
  $("#r1").textContent = (d >= 0 ? "+" : "") + Lib.fmtN(d, 1); $("#r2").textContent = (pc >= 0 ? "+" : "") + Lib.fmtN(pc, 1) + "%"; $("#r3").textContent = (d >= 0 ? "+" : "") + Lib.fmtN(d, 1) + " points";
  $("#rv").textContent = `From ${Lib.fmtN(a, 1)} to ${Lib.fmtN(b, 1)}: the change is ${Lib.fmtN(d, 1)}, which is ${Lib.fmtN(pc, 1)}% of the starting value. If these are percentages (for example unemployment rates), say it ${d >= 0 ? "rose" : "fell"} by ${Lib.fmtN(Math.abs(d), 1)} percentage points, which is a ${Lib.fmtN(Math.abs(pc), 1)}% ${d >= 0 ? "rise" : "fall"} in relative terms. Examiners expect the right wording.`;
  const Y = (v) => 270 - v * 2.4; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "Value", "sm");
  [["Old", a, "f1"], ["New", b, "f3"]].forEach(([l, v, c], i) => { const x = 90 + i * 130; o += SV.rect(x, Y(Math.min(v, 105)), 90, 270 - Y(Math.min(v, 105)), c, op(0.75)) + SV.text(x + 45, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 45, Y(Math.min(v, 105)) - 6, Lib.fmtN(v, 1), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ov", label: "Old value ", min: 10, max: 1000, step: 5, value: 60, fmt: (v) => (v / 10).toFixed(1), onInput: labP });
Lib.slider($("#g2"), { id: "nv", label: "New value ", min: 10, max: 1000, step: 5, value: 50, fmt: (v) => (v / 10).toFixed(1), onInput: labP });
labP();

/* ---------- Lab 2 ---------- */
const CT = [["A", 0.52, 1.0, 5], ["B", 0.41, 0.97, 8], ["C", 0.38, 0.93, 12], ["D", 0.34, 0.88, 22], ["E", 0.29, 0.70, 31]];
const corr = (x, y) => { const n = x.length, mx = x.reduce((a, b) => a + b) / n, my = y.reduce((a, b) => a + b) / n; let sxy = 0, sxx = 0, syy = 0; for (let i = 0; i < n; i++) { sxy += (x[i] - mx) * (y[i] - my); sxx += (x[i] - mx) ** 2; syy += (y[i] - my) ** 2; } return sxy / Math.sqrt(sxx * syy); };
function labK() {
  if (!$("#cg") || !$("#cp")) return;
  const rows = CT.map((r) => r.slice()); rows[2][1] = +$("#cg").value / 100; rows[2][3] = +$("#cp").value;
  const g = rows.map((r) => r[1]), l = rows.map((r) => r[2]), p = rows.map((r) => r[3]), rl = corr(g, l), rp = corr(g, p);
  $("#t1").textContent = (rl >= 0 ? "+" : "") + rl.toFixed(2); $("#t2").textContent = (rp >= 0 ? "+" : "") + rp.toFixed(2); const sup = rl < -0.5 && rp > 0.5; $("#t3").textContent = sup ? "Supported" : "Not supported";
  $("#tv").textContent = sup ? "Higher Gini goes with lower literacy ratios and with more poverty here, so the data are consistent with the claim. But five countries cannot prove cause: income level, schooling policy and other factors could explain both." : `The claim needs a negative link between the Gini and the literacy ratio (r near −1) and a positive link between the Gini and poverty (r near +1). Here r is ${rl.toFixed(2)} and ${rp.toFixed(2)}, so the table does not support it. In any case five countries cannot prove cause.`;
  const X = (v) => 50 + (v - 0.25) * 600, Y = (v) => 270 - v * 7; let o = SV.line(50, 270, 400, 270) + SV.line(50, 270, 50, 20) + SV.text(400, 294, "Gini coefficient", "sm", { "text-anchor": "end" }) + SV.text(56, 16, "% below the poverty line", "sm");
  rows.forEach((r, i) => { o += SV.circle(X(r[1]), Y(r[3]), 7, i === 2 ? "dot4" : "dot1") + tag(X(r[1]) + 10, Y(r[3]) - 8, r[0], i === 2 ? "t4" : "t1"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "cg", label: "Country C: Gini coefficient × 100 ", min: 25, max: 60, step: 1, value: 38, fmt: (v) => (v / 100).toFixed(2), onInput: labK });
Lib.slider($("#g4"), { id: "cp", label: "Country C: % below the poverty line ", min: 2, max: 40, step: 1, value: 12, fmt: (v) => v + "%", onInput: labK });
labK();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What should you write?", buckets: [{"label": "Name only"}, {"label": "Chain of reasons"}, {"label": "Data and interpretation"}, {"label": "Judgement"}], items: [{"text": "Identify what is included in the HDI. (3 marks)", "b": 0}, {"text": "Explain how an over-valued currency may affect an economy. (4 marks)", "b": 1}, {"text": "Consider, with reference to the table, whether inequality is linked to poverty. (6 marks)", "b": 2}, {"text": "To what extent do you agree with the IMF's advice? (8 marks)", "b": 3}, {"text": "State two trends shown in the figure. (2 marks)", "b": 0}, {"text": "Analyse why a producer sees palm oil as a way to reduce poverty. (4 marks)", "b": 1}, {"text": "Use the data to comment on the change in living standards between the two years. (6 marks)", "b": 2}, {"text": "Assess whether a government can reduce inequality with one fiscal and one supply-side policy. (8 marks)", "b": 3}], done: "Identify: name only. Explain or analyse: reasons. Consider with the table: quote and interpret. Assess, evaluate, to what extent: judge." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Identify", "Name or select; no explanation needed"], ["Describe", "State the main features or the pattern in the data"], ["Explain", "Give reasons with cause and effect"], ["Distinguish", "Define both terms and state the difference"], ["Consider", "Review the information and respond to it, using the data"], ["Assess", "Make an informed judgement"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for Section A in order.", items: ["Read the questions and note the marks and command words", "Read the passage and underline data and key phrases", "Answer part (a) briefly, then (b) with a chain or diagram", "Answer (c) using the data with calculations and a limit", "Answer (d) with developed points, a counter-point and a judgement, using the passage"], done: "Questions first, then the source, then parts in order, saving time for the last part." });
Lib.calc($("#c1"), { qs: [
  {"q": "GDP per head rises from $4,171 to $4,740. Calculate the percentage change (%, 1 decimal place).", "a": 13.6, "unit": "%", "tol": 0.1, "hint": "569 ÷ 4,171.", "sol": "569 ÷ 4,171 × 100 = <b>13.6%</b>."},
  {"q": "Unemployment falls from 5.8% to 5.5%. By how many percentage points has it fallen?", "a": 0.3, "unit": "points", "tol": 0.01, "hint": "5.8 − 5.5.", "sol": "<b>0.3 percentage points</b>."},
  {"q": "The Gini coefficient falls from 0.437 to 0.385. Calculate the percentage change (%, 1 decimal place).", "a": -11.9, "unit": "%", "tol": 0.1, "hint": "(0.385 − 0.437) ÷ 0.437.", "sol": "−0.052 ÷ 0.437 = <b>−11.9%</b>."},
  {"q": "Palm oil makes up 80% of a country's exports and exports are 30% of GDP. What share of GDP is palm oil exports (%)?", "a": 24, "unit": "%", "tol": 0.1, "hint": "0.8 × 30.", "sol": "<b>24%</b> of GDP."},
  {"q": "A 20 mark Section A should take about 36 minutes. How many minutes per mark is that (1 decimal place)?", "a": 1.8, "unit": "min", "tol": 0.05, "hint": "36 ÷ 20.", "sol": "<b>1.8 minutes per mark</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "How many marks are usually given to the last part of Section A?", opts: ["2", "4", "7 or 8", "15"], a: 2, why: "In 34 of 40 papers it was 7 or 8 marks, the largest part." },
  { q: "A part says 'Identify two...' for 2 marks. The best answer is:", opts: ["Two short named points", "A paragraph of analysis for each", "One long sentence", "A diagram"], a: 0, why: "Identify needs no explanation. Do not waste time." },
  { q: "In a 'consider with reference to the table' part, the best approach is to:", opts: ["Quote data, say what it shows and say what it cannot show", "Copy the table", "Ignore the table and write from memory", "Only calculate percentages"], a: 0, why: "Use the data, interpret it and qualify it." },
  { q: "Unemployment rises from 4% to 5%. The correct description is:", opts: ["A rise of 1 percentage point (25% in relative terms)", "A rise of 1%", "A rise of 20%", "A fall of 1 point"], a: 0, why: "Rates change in percentage points; the relative change is 25%." },
  { q: "What is the best way to end the 8 mark part?", opts: ["A reasoned judgement that answers the question", "A repeat of the first paragraph", "A new unrelated point", "Nothing"], a: 0, why: "The evaluation mark needs a justified conclusion." },
  { q: "Why should you quote the passage in part (d)?", opts: ["It is the application and shows you used the source", "It is a waste of time", "It adds words", "It replaces analysis"], a: 0, why: "Using the passage is part of what the question asks." },
  { q: "A correlation across five countries shows that:", opts: ["There is a pattern, but it does not prove cause", "One variable causes the other", "The data are wrong", "There is no link at all"], a: 0, why: "Five countries cannot prove cause; other factors may matter." },
  { q: "If you are stuck on part (c), you should:", opts: ["Leave a gap and return, after attempting the other parts", "Stop the paper", "Skip all remaining parts", "Spend 20 minutes on it"], a: 0, why: "Moving on protects marks in the biggest part." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Section A", "20 marks, four parts, last part largest."],
  ["Typical pattern", "2, 4, 6, 8 marks."],
  ["One mark per point", "Be precise and develop briefly."],
  ["Identify", "Name only."],
  ["Consider with the table", "Quote, calculate, interpret, limit."],
  ["Percentage points", "Used for changes in rates."],
  ["Last part", "Judge with the passage."],
  ["Time", "About 1.8 minutes per mark."],
] });

