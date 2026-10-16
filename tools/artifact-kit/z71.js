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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Building a 2-mark definition", base: { n: 0 }, draw: mkChain(["Read the command word: Define", "Recall the key terms from the syllabus", "Write one sentence with both key ideas", "Check each key idea is a separate mark", "Move on: do not add explanation"], "--accent"), steps: chainSteps(["Read the command word: Define", "Recall the key terms from the syllabus", "Write one sentence with both key ideas", "Check each key idea is a separate mark", "Move on: do not add explanation"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "A full calculation answer", base: { n: 0 }, draw: mkChain(["Read the question: Calculate PED", "Write the formula: %ΔQd ÷ %ΔP", "Work out each percentage change", "Divide to get the answer", "State the result with its meaning (e.g. −1.5: elastic)"], "--good"), steps: chainSteps(["Read the question: Calculate PED", "Write the formula: %ΔQd ÷ %ΔP", "Work out each percentage change", "Divide to get the answer", "State the result with its meaning (e.g. −1.5: elastic)"]) });
function labA() {
  const ids = ["a0","a1","a2"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const per = (v[2] - 10) / v[1], t = per * v[0]; return { r: [t.toFixed(1) + ' min', per.toFixed(2), '10 min'], t: 'With ' + v[1] + ' marks in ' + v[2] + ' minutes and 10 minutes kept for checking, you have about ' + per.toFixed(2) + ' minutes per mark. A ' + v[0] + '-mark question deserves about ' + t.toFixed(1) + ' minutes. Short AO1 parts (define, identify, calculate) should take less than this, which leaves more time for the longer analysis and evaluation parts.', bars: [['Time for question', t, '--accent', t.toFixed(1) + ' min'], ['Min per mark ×5', per * 5, '--good', per.toFixed(2)], ['Checking time', 10, '--warn']] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Marks for the question", min: 1, max: 20, step: 1, value: 6, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Total marks on the paper", min: 40, max: 80, step: 10, value: 80, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Time on the paper (minutes)", min: 60, max: 120, step: 10, value: 120, fmt: (v) => v, onInput: labA });
const L2 = [{"n": "Define", "a": "One precise sentence with the key terms", "b": "Opportunity cost is the next best alternative given up."}, {"n": "Identify", "a": "Just the name or choice", "b": "Two free goods: sunlight and air."}, {"n": "State", "a": "A short clear statement", "b": "State one function of money: a medium of exchange."}, {"n": "Give", "a": "A fact or example asked for", "b": "Give one example of a tertiary sector firm: a bank."}, {"n": "Calculate", "a": "Formula, working, answer, units", "b": "PED = −30% ÷ +20% = −1.5."}, {"n": "Describe", "a": "Main features or characteristics", "b": "A monopoly has one seller and high barriers to entry."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>What to write</th><th>Example</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Which <b>command word</b> asks for each response?", buckets: [{"label": "Define"}, {"label": "Identify"}, {"label": "Calculate"}], items: [{"text": "A precise meaning in one sentence", "b": 0}, {"text": "Just the name of the term", "b": 1}, {"text": "Formula, working and answer", "b": 2}, {"text": "The key terms in a sentence", "b": 0}, {"text": "Pick the correct item from the data", "b": 1}, {"text": "Work out from given figures", "b": 2}], done: "Match the command word." });
Lib.classify($("#cl2"), { prompt: "Is each skill <b>AO1</b>, <b>AO2</b> or <b>AO3</b>?", buckets: [{"label": "AO1 Knowledge"}, {"label": "AO2 Analysis"}, {"label": "AO3 Evaluation"}], items: [{"text": "Define inflation", "b": 0}, {"text": "Use the formula for total revenue", "b": 0}, {"text": "Explain how a tax raises prices using a chain of reasoning", "b": 1}, {"text": "Interpret data from an extract", "b": 1}, {"text": "Weigh two sides and reach a conclusion", "b": 2}, {"text": "Recognise that outcomes are uncertain", "b": 2}], done: "Know the three objectives." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Define", "Give precise meaning"], ["Identify", "Name, select or recognise"], ["State", "Express in clear terms"], ["Give", "Produce an answer from a source or memory"], ["Calculate", "Work out from given facts or figures"], ["Describe", "State the points or features of a topic"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps in order: <b>answering a calculate question</b>.", items: ["Read the question and find the data", "Write the formula", "Substitute the figures", "Work out the answer", "Add the unit or a short interpretation"], done: "Show the working." });
Lib.calc($("#c1"), { qs: [
  { q: "Paper 2 is 80 marks in 120 minutes. How many minutes per mark (1 decimal place)?", a: 1.5, sol: "120 ÷ 80 = <b>1.5</b>." },
  { q: "A question is worth 6 marks. How many minutes should you spend at 1.5 minutes per mark?", a: 9, sol: "6 × 1.5 = <b>9</b>." },
  { q: "AO1 is 43% of a qualification. Out of 100 marks of weighting, how many are AO1?", a: 43, sol: "<b>43</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "AO1 stands for:", opts: ["Analysis", "Knowledge and understanding", "Evaluation", "Application"], a: 1, why: "Assessment Objective 1." },
  { q: "Which command word asks for a precise meaning?", opts: ["Describe", "Define", "Discuss", "Analyse"], a: 1, why: "Define." },
  { q: "In a Calculate question you should show:", opts: ["Only the answer", "Formula, working and answer", "A diagram", "A conclusion"], a: 1, why: "Working earns marks." },
  { q: "What share of Paper 1 is AO1?", opts: ["10%", "40%", "50%", "100%"], a: 2, why: "Paper 1 is 50% AO1." },
  { q: "A 2-mark Identify question needs:", opts: ["A long paragraph", "Two names or choices", "An evaluation", "A diagram"], a: 1, why: "Keep it short." },
] });

Lib.cards($("#fc1"), { cards: [
  ["AO1", "Knowledge and understanding of definitions, formulas, concepts and theories, and use of terminology."],
  ["Define", "Give precise meaning."],
  ["Identify", "Name, select or recognise."],
  ["State", "Express in clear terms."],
  ["Give", "Produce an answer from a given source or from memory."],
  ["Calculate", "Work out from given facts, figures or information."],
  ["Describe", "State the points of a topic; give characteristics and main features."],
  ["Terminology", "Using the correct economic words."],
  ["Formula", "A rule for calculating a quantity."],
] });
labA(); 
