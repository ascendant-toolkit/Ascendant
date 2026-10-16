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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Why a mixed economy helps", base: { n: 0 }, draw: mkChain(["Markets create efficiency and choice", "Market failure leaves gaps", "The government fills the gaps with public and merit goods", "Welfare benefits protect those in need", "A mixed economy blends efficiency and fairness"], "--good"), steps: chainSteps(["Markets create efficiency and choice", "Market failure leaves gaps", "The government fills the gaps with public and merit goods", "Welfare benefits protect those in need", "A mixed economy blends efficiency and fairness"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Why the mix can go wrong", base: { n: 0 }, draw: mkChain(["The government raises taxes to fund services", "Incentives to work or invest may fall", "State firms face no competition and become inefficient", "Government decisions may be poor (government failure)", "A mixed economy can be less efficient"], "--bad"), steps: chainSteps(["The government raises taxes to fund services", "Incentives to work or invest may fall", "State firms face no competition and become inefficient", "Government decisions may be poor (government failure)", "A mixed economy can be less efficient"]) });
function labA() {
  const ids = ["a0","a1","a2","a3"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const nm = ['Efficiency/choice', 'Fairness/welfare', 'Public goods', 'Incentives/taxes'], avg = (v.reduce((a, b) => a + b, 0) / 4).toFixed(1), hi = nm[v.indexOf(Math.max(...v))], lo = nm[v.indexOf(Math.min(...v))]; return { r: [avg + '/10', hi, lo], t: 'A mixed economy usually does better than a pure market on fairness and public goods, and better than a planned system on efficiency and incentives. Here the average is ' + avg + '/10, strongest on ' + hi.toLowerCase() + ' and weakest on ' + lo.toLowerCase() + '. The best balance depends on what a country values most.', bars: nm.map((n, i) => [n, v[i], ['--accent', '--good', '--warn', '--bad'][i]]) };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Efficiency and choice", min: 1, max: 10, step: 1, value: 7, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Fairness and welfare", min: 1, max: 10, step: 1, value: 7, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Provision of public goods", min: 1, max: 10, step: 1, value: 8, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga3"), { id: "a3", label: "Incentives and low taxes", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: labA });
const L2 = [{"n": "Efficiency", "a": "Market competition in most sectors", "b": "State-run firms may be inefficient."}, {"n": "Fairness", "a": "Welfare and progressive taxes reduce inequality", "b": "High taxes may reduce incentives."}, {"n": "Public goods", "a": "The government provides what the market will not", "b": "Costs fall on taxpayers."}, {"n": "Stability", "a": "The government can manage the economy", "b": "It may make poor decisions."}, {"n": "Regulation", "a": "Protects consumers and the environment", "b": "Raises costs; red tape."}, {"n": "Choice", "a": "Consumers choose in private markets", "b": "Public services may offer less choice."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Strength</th><th>Weakness</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Is each an <b>advantage</b> or a <b>disadvantage</b> of a mixed economy?", buckets: [{"label": "Advantage"}, {"label": "Disadvantage"}], items: [{"text": "Public goods are provided", "b": 0}, {"text": "A welfare safety net", "b": 0}, {"text": "Correcting externalities", "b": 0}, {"text": "High taxes reduce incentives", "b": 1}, {"text": "Government failure", "b": 1}, {"text": "State firms may be inefficient", "b": 1}], done: "Weigh both." });
Lib.classify($("#cl2"), { prompt: "Does each <b>favour a market</b> or a <b>favour government action</b>?", buckets: [{"label": "Favours market"}, {"label": "Favours government"}], items: [{"text": "Efficiency from competition", "b": 0}, {"text": "Consumer choice", "b": 0}, {"text": "Reducing pollution", "b": 1}, {"text": "Reducing inequality", "b": 1}, {"text": "Providing defence", "b": 1}, {"text": "Innovation through profit", "b": 0}], done: "Know what each does best." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Government failure", "Intervention that worsens the outcome"], ["Safety net", "Benefits that protect low-income households"], ["Bureaucracy", "Slow, rule-bound administration"], ["Incentives", "Rewards that encourage effort"], ["Progressive tax", "A tax that takes a larger share of higher incomes"], ["Crowding out", "Public spending that reduces private activity"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how high taxes can reduce growth</b>.", items: ["The government raises taxes", "Firms and workers keep less of their earnings", "Incentives to work and invest fall", "Less output is produced", "Economic growth slows"], done: "A disadvantage of a larger public sector." });
Lib.calc($("#c1"), { qs: [
  { q: "Income is $50,000 and tax is 30%. How much tax is paid ($)?", a: 15000, sol: "30% × 50,000 = <b>$15,000</b>." },
  { q: "Government spending is $120bn and tax revenue is $100bn. What is the budget deficit ($bn)?", a: 20, sol: "120 − 100 = <b>$20bn</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An advantage of a mixed economy is:", opts: ["Higher taxes", "Provision of public goods", "State inefficiency", "Bureaucracy"], a: 1, why: "The state fills gaps." },
  { q: "A disadvantage is:", opts: ["Consumer choice", "Government failure", "Competition", "Innovation"], a: 1, why: "Poor government decisions." },
  { q: "High taxes may:", opts: ["Raise incentives", "Reduce incentives to work", "Increase profit", "Remove inequality"], a: 1, why: "Disincentives." },
  { q: "State-owned firms may be inefficient because:", opts: ["They face no competition", "They are too small", "They make profit", "Prices are zero"], a: 0, why: "No rivals." },
  { q: "A mixed economy is better than a pure market at:", opts: ["Reducing inequality", "Lowering taxes", "Cutting spending", "Raising profit"], a: 0, why: "Welfare and redistribution." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Government failure", "Intervention that leads to a worse outcome."],
  ["Safety net", "Welfare support for those in need."],
  ["Bureaucracy", "Complex, slow administration."],
  ["Incentive", "A reward that encourages effort."],
  ["Progressive tax", "Takes a larger share of higher incomes."],
  ["Crowding out", "Public spending reducing private activity."],
  ["Budget deficit", "Government spending greater than revenue."],
  ["Welfare", "Society's well-being."],
  ["Regulation", "Government rules on firms."],
] });
labA(); 
