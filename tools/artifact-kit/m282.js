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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Why the market can lead to inequality", base: { n: 0 }, draw: mkChain(["Goods are allocated to those willing and able to pay", "Low-income households have little purchasing power", "They cannot afford essentials such as healthcare", "Firms supply those who can pay, not those with the greatest need", "Inequality of outcomes"], "--bad"), steps: chainSteps(["Goods are allocated to those willing and able to pay", "Low-income households have little purchasing power", "They cannot afford essentials such as healthcare", "Firms supply those who can pay, not those with the greatest need", "Inequality of outcomes"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Why the market encourages innovation", base: { n: 0 }, draw: mkChain(["Profit rewards successful new products", "Firms invest in research and new methods", "New products and cheaper methods appear", "Consumers gain more choice and lower prices", "Living standards may rise"], "--good"), steps: chainSteps(["Profit rewards successful new products", "Firms invest in research and new methods", "New products and cheaper methods appear", "Consumers gain more choice and lower prices", "Living standards may rise"]) });
Lib.stepper($("#st2"), { w: 760, h: 380, label: "Why the market ignores external costs", base: { n: 0 }, draw: mkChain(["A firm produces and pollutes a river", "The cost of the pollution falls on society", "The firm ignores it in its decisions", "Too much of the good is produced", "Resources are misallocated: market failure"], "--warn"), steps: chainSteps(["A firm produces and pollutes a river", "The cost of the pollution falls on society", "The firm ignores it in its decisions", "Too much of the good is produced", "Resources are misallocated: market failure"]) });
function labA() {
  const ids = ["a0","a1","a2","a3"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const nm = ['Efficiency', 'Choice and innovation', 'Fairness', 'Environment/public goods'], avg = (v.reduce((a, b) => a + b, 0) / 4).toFixed(1), hi = nm[v.indexOf(Math.max(...v))], lo = nm[v.indexOf(Math.min(...v))]; return { r: [avg + '/10', hi, lo], t: 'A market economy tends to score well on efficiency and choice but worse on fairness and the environment. Your scores average ' + avg + '/10, with ' + hi.toLowerCase() + ' strongest and ' + lo.toLowerCase() + ' weakest. A balanced evaluation weighs these and may favour government action where the weakest aim matters most.', bars: nm.map((n, i) => [n, v[i], ['--accent', '--good', '--warn', '--bad'][i]]) };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Efficiency", min: 1, max: 10, step: 1, value: 8, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Choice and innovation", min: 1, max: 10, step: 1, value: 8, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Fairness (equity)", min: 1, max: 10, step: 1, value: 3, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga3"), { id: "a3", label: "Environment and public goods", min: 1, max: 10, step: 1, value: 3, fmt: (v) => v, onInput: labA });
const L2 = [{"n": "Efficiency", "a": "Competition keeps costs and prices down", "b": "Monopolies may raise prices."}, {"n": "Choice", "a": "Firms supply what consumers want", "b": "Only for those who can pay."}, {"n": "Innovation", "a": "Profit rewards new ideas", "b": "Some research (e.g. for rare diseases) is unprofitable."}, {"n": "Fairness", "a": "Rewards effort", "b": "Inequality; low-income households go without."}, {"n": "Environment", "a": "Prices can reflect scarcity", "b": "External costs are ignored."}, {"n": "Stability", "a": "Prices adjust to shocks", "b": "Booms, recessions and unemployment."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Strength</th><th>Weakness</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Is each an <b>advantage</b> or a <b>disadvantage</b> of the market system?", buckets: [{"label": "Advantage"}, {"label": "Disadvantage"}], items: [{"text": "Efficiency through competition", "b": 0}, {"text": "Consumer choice", "b": 0}, {"text": "Innovation", "b": 0}, {"text": "Inequality", "b": 1}, {"text": "Neglect of public goods", "b": 1}, {"text": "Pollution and external costs", "b": 1}], done: "Weigh both." });
Lib.classify($("#cl2"), { prompt: "Which <b>problem</b> does each describe?", buckets: [{"label": "Inequality"}, {"label": "Market failure"}, {"label": "Monopoly power"}], items: [{"text": "Poor households cannot afford healthcare", "b": 0}, {"text": "Factory pollution not paid for by the firm", "b": 1}, {"text": "A dominant firm restricts output", "b": 2}, {"text": "Street lighting is not provided by firms", "b": 1}, {"text": "A firm raises prices because it has no rivals", "b": 2}], done: "Know the weaknesses." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Efficiency", "Using resources well at low cost"], ["Inequality", "Unequal distribution of income and goods"], ["Innovation", "New products and methods"], ["External cost", "A cost to third parties"], ["Monopoly", "A dominant single seller"], ["Public good", "A good the market under-provides"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how profit leads to innovation</b>.", items: ["Firms see a chance of higher profit", "They invest in research and new methods", "New products appear", "Consumers gain more choice", "Firms with good ideas earn profit"], done: "Incentives drive innovation." });
Lib.calc($("#c1"), { qs: [
  { q: "A firm spends $2m on research and earns $5m extra revenue from the new product. What is the net gain ($m)?", a: 3, sol: "5 − 2 = <b>$3m</b>." },
  { q: "Income of the richest 10% is $40bn of a $100bn total. What percentage is that?", a: 40, sol: "40 ÷ 100 × 100 = <b>40%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An advantage of the market system is:", opts: ["Inequality", "Efficiency through competition", "Under-provision of public goods", "Monopoly"], a: 1, why: "Competition." },
  { q: "A disadvantage is:", opts: ["Consumer choice", "Innovation", "Ignoring external costs", "Low administration costs"], a: 2, why: "Spillovers are ignored." },
  { q: "Public goods are under-provided because:", opts: ["They are unprofitable for private firms", "They are too cheap", "They are banned", "Consumers dislike them"], a: 0, why: "No profit." },
  { q: "The market system rewards risk-taking through:", opts: ["Taxes", "Profit", "Subsidies", "Quotas"], a: 1, why: "Incentive." },
  { q: "A reason many countries use a mixed system:", opts: ["Markets fail in some areas", "Markets are perfect", "Prices do not exist", "Planned economies are always better"], a: 0, why: "To correct failures." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Efficiency", "Using resources well, with little waste."],
  ["Inequality", "An unequal distribution of income or goods."],
  ["Innovation", "The introduction of new products or methods."],
  ["External cost", "A cost to third parties not paid by the producer."],
  ["Public good", "A good that markets under-provide."],
  ["Monopoly", "A single dominant seller."],
  ["Merit good", "A good that markets under-consume."],
  ["Demerit good", "A good that markets over-consume."],
  ["Instability", "Fluctuations in output and employment."],
] });
labA(); 
