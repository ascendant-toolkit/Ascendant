const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const QX = (q) => 80 + 6 * q, PY = (p) => 360 - 2.7 * p;
function seg(m, c) { // clip P = mQ + c to 0<=Q<=100, 0<=P<=120
  let lo = 0, hi = 100;
  if (m !== 0) { const a = (0 - c) / m, z = (120 - c) / m; lo = Math.max(lo, Math.min(a, z)); hi = Math.min(hi, Math.max(a, z)); }
  return [lo, m * lo + c, hi, m * hi + c];
}
function curve(m, c, cls, label, o = {}) {
  const [q1, p1, q2, p2] = seg(m, c);
  if (q2 <= q1) return "";
  let s = SV.line(QX(q1), PY(p1), QX(q2), PY(p2), cls, o.attrs);
  if (label) { const a = { "text-anchor": "start" }; if (o.attrs && o.attrs.opacity !== undefined) a.opacity = o.attrs.opacity; s += SV.text(QX(q2) + (o.dx ?? 6), PY(p2) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), a); }
  return s;
}
function axes(yl = "Price", xl = "Quantity") {
  return SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) +
    SV.text(QX(0) + 6, PY(120) + 6, yl, "sm") + SV.text(QX(104), PY(0) + 22, xl, "sm", { "text-anchor": "end" });
}
const hline = (p, c = "gr", x2 = 100) => SV.line(QX(0), PY(p), QX(x2), PY(p), c);
const vline = (q, p, c = "gr") => SV.line(QX(q), PY(p), QX(q), PY(0), c);
const ylab = (p, t, c = "sm") => SV.text(QX(0) - 8, PY(p) + 4, t, c, { "text-anchor": "end" });
const xlab = (q, t, c = "sm") => SV.text(QX(q), PY(0) + 18, t, c, { "text-anchor": "middle" });
const money = (v, d = 1) => Lib.fmtN(v, d);
const halo = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
const asP = (y) => (y <= 60 ? 30 + 0.4 * y : 54 + 2.2 * (y - 60));
function solveAD(sh) {
  const c = 90 + 0.8 * sh; let y = (c - 30) / 1.2;
  if (y > 60) y = (c + 78) / 3;
  return [y, asP(y), c];
}
function adLine(c, cls, label, o = {}) {
  const lo = Math.max(0, (c - 108) / 0.8), hi = Math.min(100, (c - 8) / 0.8);
  let r = SV.line(QX(lo), PY(c - 0.8 * lo), QX(hi), PY(c - 0.8 * hi), cls, o.attrs);
  if (label) r += SV.text(QX(hi) + 6, PY(c - 0.8 * hi) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), o.attrs && o.attrs.opacity !== undefined ? { opacity: o.attrs.opacity } : {});
  return r;
}
function adChart(s) {
  const sh = s.sh, [y1, p1, c] = solveAD(sh), moved = Math.abs(sh) >= 1;
  let o = axes("Price level", "Real GDP");
  o += SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: moved ? 0.4 : 1 } });
  if (moved) o += adLine(c, sh > 0 ? "c2" : "c4", sh > 0 ? "AD₁" : "AD₂", { t: sh > 0 ? "t2" : "t4" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: moved ? 0.45 : 1 });
  if (moved) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, sh > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}

function solve2(sh, a) {
  const c = 90 + 0.8 * sh; let y = (c - 30 + 0.4 * a) / 1.2;
  if (y - a > 60) y = (c + 78 + 2.2 * a) / 3;
  return [y, c - 0.8 * y, c];
}
function adasChart(s) {
  const sh = s.sh, a = s.a, [y1, p1, c] = solve2(sh, a), movedAD = Math.abs(sh) >= 1, movedAS = Math.abs(a) >= 1;
  const pts = (x) => [[QX(Math.max(0, x)), PY(x < 0 ? 30 - 0.4 * x : 30)], [QX(60 + x), PY(54)], [QX(87.7 + x), PY(115)]];
  let o = axes("Price level", "Real GDP");
  if (movedAS) o += SV.path(ptsPath(pts(0)), "c3", { opacity: 0.4 });
  o += SV.path(ptsPath(pts(a)), "c3") + SV.text(QX(87.7 + a) + 6, PY(115) + 4, movedAS ? "AS₁" : "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: movedAD ? 0.4 : 1 } });
  if (movedAD) o += adLine(c, "c2", "AD₁", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: movedAD || movedAS ? 0.45 : 1 });
  if (movedAD || movedAS) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
const mkChain = (list, col) => (s) => {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  list.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < list.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
};
const chainSteps = (caps) => caps.map((c, i) => ({ cap: c, s: { n: i + 1 } }));
function button_table(btnId, outId, data, cols, fn) {
  const show = (i) => {
    $("#" + btnId).innerHTML = data.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
    $$("#" + btnId + " .b").forEach((b) => (b.onclick = () => show(+b.dataset.j)));
    $("#" + outId).innerHTML = fn(data[i]);
  };
  show(0);
}
Lib.stepper($("#st0"), { w: 760, h: 380, label: "A developed chain of reasoning", base: { n: 0 }, draw: mkChain(["Oil prices rise (the cause in the question)", "Firms' costs of production increase", "Firms raise prices or cut supply", "The general price level rises", "Inflation increases: the effect asked for"], "--accent"), steps: chainSteps(["Oil prices rise (the cause in the question)", "Firms' costs of production increase", "Firms raise prices or cut supply", "The general price level rises", "Inflation increases: the effect asked for"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Using data from the extract", base: { n: 0 }, draw: mkChain(["Read the extract and find the relevant figures", "Quote them: 'unemployment rose from 5% to 8%'", "Interpret the trend: fewer people in work", "Link to the economics: lower spending, lower AD", "Use it to support the argument"], "--good"), steps: chainSteps(["Read the extract and find the relevant figures", "Quote them: 'unemployment rose from 5% to 8%'", "Interpret the trend: fewer people in work", "Link to the economics: lower spending, lower AD", "Use it to support the argument"]) });
Lib.stepper($("#st2"), { w: 760, h: 380, label: "A demand and supply diagram answer", base: { n: 0 }, draw: mkChain(["Draw D and S with axes labelled", "Mark the original equilibrium P, Q", "Shift the curve affected and label it (S₁)", "Mark the new equilibrium P₁, Q₁", "Explain the change in words"], "--warn"), steps: chainSteps(["Draw D and S with axes labelled", "Mark the original equilibrium P, Q", "Shift the curve affected and label it (S₁)", "Mark the new equilibrium P₁, Q₁", "Explain the change in words"]) });
function labA() {
  const ids = ["a0","a1","a2"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const dev = Math.min(v[0], 2) * Math.min(v[1], 3), ctx = v[2] >= 3 ? 1 : 0, m = Math.min(6, Math.round(dev * 0.7 + ctx + (v[0] > 2 ? 0 : 0))), lvl = m >= 5 ? 'Developed and applied' : m >= 3 ? 'Some development' : 'Mostly description', nx = v[1] < 3 ? 'Develop each point into at least three links' : v[2] < 3 ? 'Use figures or names from the extract' : v[0] < 2 ? 'Add a second chain' : 'Add a diagram or check the logic'; return { r: [m + '/6', lvl, nx], t: v[0] + ' point' + (v[0] > 1 ? 's' : '') + ' with ' + v[1] + ' link' + (v[1] > 1 ? 's' : '') + ' each and ' + (v[2] >= 3 ? 'good' : 'weak') + ' use of context score about ' + m + ' out of 6 (illustrative). More than two points does not raise the mark; deeper chains and use of context do. Next: ' + nx.toLowerCase() + '.', bars: [['Points (max 2 count)', Math.min(v[0], 2), '--accent'], ['Links per point', Math.min(v[1], 5), '--good'], ['Context use', v[2], '--warn'], ['Marks', m, '--bad']] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Number of separate points made", min: 1, max: 4, step: 1, value: 2, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Links developed per point (1 to 5)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Use of the context or data (1 none, 5 strong)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labA });
const L2 = [{"n": "Analyse how a subsidy affects the market for solar panels", "a": "A subsidy is money from the government.", "b": "A subsidy lowers costs, so supply shifts right; price falls and quantity rises, so more solar panels are bought."}, {"n": "Explain why unemployment may rise in a recession", "a": "Unemployment is people without jobs.", "b": "Falling demand makes firms cut output, so they need fewer workers and lay some off."}, {"n": "Analyse a rise in the price of milk on producers' revenue", "a": "Milk is a food.", "b": "A higher price means each litre earns more, but quantity falls; if demand is inelastic, revenue rises."}, {"n": "Explain why a monopoly may charge a high price", "a": "A monopoly is one firm.", "b": "With no rivals and high barriers to entry, it can raise the price without losing customers."}, {"n": "Analyse how a fall in the exchange rate affects exports", "a": "The exchange rate is the price of a currency.", "b": "Exports become cheaper abroad, so foreign demand rises and export revenue increases."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Weak answer</th><th>Stronger answer</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Is each a <b>description</b> or <b>analysis</b>?", buckets: [{"label": "Description"}, {"label": "Analysis"}], items: [{"text": "A subsidy is a payment to producers", "b": 0}, {"text": "Unemployment is people without jobs", "b": 0}, {"text": "Higher costs mean firms cut supply, so prices rise", "b": 1}, {"text": "Falling demand leads to job cuts and lower incomes", "b": 1}, {"text": "Inflation is a rise in the price level", "b": 0}, {"text": "Higher wages raise costs, so firms raise prices, so inflation rises", "b": 1}], done: "Analysis shows how and why." });
Lib.classify($("#cl2"), { prompt: "Which <b>connective</b> signals a link in a chain?", buckets: [{"label": "Links in a chain"}, {"label": "Not a link"}], items: [{"text": "because", "b": 0}, {"text": "so", "b": 0}, {"text": "which leads to", "b": 0}, {"text": "as a result", "b": 0}, {"text": "for example", "b": 1}, {"text": "also", "b": 1}], done: "Use linking words." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Explain", "Say why or how, with support"], ["Analyse", "Examine in detail to show relationships"], ["Chain of reasoning", "Linked steps from cause to effect"], ["Application", "Using the context in the question"], ["Data interpretation", "Selecting and reading figures"], ["Diagram", "A labelled graph showing an economic change"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a tax on cigarettes reduces smoking</b>.", items: ["The government raises the tax on cigarettes", "Producers' costs rise, so supply shifts left", "The market price of cigarettes rises", "Smokers can afford fewer cigarettes", "Quantity demanded falls"], done: "Link each step." });
Lib.calc($("#c1"), { qs: [
  { q: "An extract says GDP rose from $200bn to $212bn. What is the growth rate (%)?", a: 6, sol: "12 ÷ 200 × 100 = <b>6%</b>." },
  { q: "Unemployment rose from 5% to 8%. By how many percentage points?", a: 3, sol: "8 − 5 = <b>3</b> percentage points." },
  { q: "Prices rose from an index of 100 to 104. What is the inflation rate (%)?", a: 4, sol: "4 ÷ 100 × 100 = <b>4%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "AO2 stands for:", opts: ["Knowledge", "Analysis", "Evaluation", "Recall"], a: 1, why: "Assessment Objective 2." },
  { q: "A chain of reasoning means:", opts: ["One long sentence about definitions", "Linked steps from cause to effect", "A list of facts", "A conclusion only"], a: 1, why: "Point, because, so." },
  { q: "In an extract question you should:", opts: ["Ignore the data", "Use figures and names from the extract", "Write about another country", "Draw only"], a: 1, why: "Application." },
  { q: "Analyse means:", opts: ["Give a short answer", "Examine in detail to show relationships", "Name a term", "State a value"], a: 1, why: "Detailed relationships." },
  { q: "In a diagram answer you should also:", opts: ["Say nothing", "Explain the change in words", "Add three more diagrams", "Skip labels"], a: 1, why: "Diagram plus words." },
] });

Lib.cards($("#fc1"), { cards: [
  ["AO2", "Analysis: selecting and applying economic information and developing links and relationships."],
  ["Explain", "Set out reasons; say why or how, supported with evidence."],
  ["Analyse", "Examine in detail to show meaning and the relationships between elements."],
  ["Chain of reasoning", "A sequence of linked steps from cause to effect."],
  ["Application", "Using the context in the question."],
  ["Context", "The country, industry or information given."],
  ["Data", "Figures in the extract, tables or graphs."],
  ["Link", "A step that connects one idea to the next."],
  ["Diagram", "A labelled graph showing an economic change."],
] });
labA(); 
