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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "How the market answers 'what to produce'", base: { n: 0 }, draw: mkChain(["Consumers spend more on a good", "Its price and profit rise", "Firms, seeking profit, produce more of it", "Resources move into the good", "Consumer sovereignty decides what is produced"], "--accent"), steps: chainSteps(["Consumers spend more on a good", "Its price and profit rise", "Firms, seeking profit, produce more of it", "Resources move into the good", "Consumer sovereignty decides what is produced"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Competition and efficiency", base: { n: 0 }, draw: mkChain(["A firm charges a high price and earns high profit", "Rival firms enter and compete for customers", "Firms cut prices and improve quality", "Consumers benefit from lower prices and better products", "Competition pushes firms towards efficiency"], "--good"), steps: chainSteps(["A firm charges a high price and earns high profit", "Rival firms enter and compete for customers", "Firms cut prices and improve quality", "Consumers benefit from lower prices and better products", "Competition pushes firms towards efficiency"]) });
function labA() {
  const ids = ["a0","a1","a2"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const s = Math.round((v[0] + v[1] + (100 - v[2])) / 3); const c = s >= 80 ? 'Market economy' : s >= 40 ? 'Mixed economy' : 'Planned economy'; return { r: [s + '/100', c, v[2] + '%'], t: 'Private ownership ' + v[0] + '%, price freedom ' + v[1] + '% and a government role of ' + v[2] + '% give a market score of ' + s + ': ' + c.toLowerCase() + '. A pure market economy would score near 100; in practice most economies are mixed.', bars: [['Private ownership', v[0], '--accent'], ['Price freedom', v[1], '--good'], ['Government role', v[2], '--warn']] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Share of production in private hands", min: 0, max: 100, step: 10, value: 80, fmt: (v) => v + '%', onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Freedom of prices (set by demand and supply)", min: 0, max: 100, step: 10, value: 80, fmt: (v) => v + '%', onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Government role in decisions", min: 0, max: 100, step: 10, value: 20, fmt: (v) => v + '%', onInput: labA });
const L2 = [{"n": "Private ownership", "a": "Individuals and firms own resources", "b": "Decisions are made by owners seeking profit."}, {"n": "Price mechanism", "a": "Prices signal and ration", "b": "Prices adjust to demand and supply."}, {"n": "Profit motive", "a": "Firms aim for profit", "b": "Profit is the reward for taking risks."}, {"n": "Consumer sovereignty", "a": "Consumers decide what is made", "b": "Spending acts like votes."}, {"n": "Competition", "a": "Firms rival each other", "b": "Keeps prices down and quality up."}, {"n": "Limited government", "a": "The state does little", "b": "Law, property rights and defence."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Feature</th><th>Meaning</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Is each a feature of a <b>market economy</b> or a <b>planned economy</b>?", buckets: [{"label": "Market economy"}, {"label": "Planned economy"}], items: [{"text": "Private ownership of resources", "b": 0}, {"text": "Prices set by demand and supply", "b": 0}, {"text": "Profit motive", "b": 0}, {"text": "Competition between firms", "b": 0}, {"text": "Government decides output", "b": 1}, {"text": "State ownership of most resources", "b": 1}, {"text": "Central planners set prices", "b": 1}], done: "Market: private and price-led." });
Lib.classify($("#cl2"), { prompt: "Which <b>question</b> does each answer?", buckets: [{"label": "What to produce"}, {"label": "How to produce"}, {"label": "For whom to produce"}], items: [{"text": "Consumers spend more on organic food", "b": 0}, {"text": "Firms switch to cheaper machines", "b": 1}, {"text": "Goods go to those willing and able to pay", "b": 2}, {"text": "Resources move to high-profit goods", "b": 0}, {"text": "Competition forces cost-cutting methods", "b": 1}], done: "What, how, for whom." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Market economy", "Prices and private decisions allocate resources"], ["Consumer sovereignty", "Consumers' spending decides what is produced"], ["Profit motive", "Firms' aim of earning profit"], ["Price mechanism", "Prices adjusting to demand and supply"], ["Competition", "Rivalry between firms for customers"], ["Private ownership", "Resources owned by individuals and firms"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how competition benefits consumers</b>.", items: ["Firms compete for customers", "Firms cut prices or improve quality", "Consumers benefit from lower prices and better quality", "Inefficient firms lose customers", "Firms become more efficient"], done: "Competition drives efficiency." });
Lib.calc($("#c1"), { qs: [
  { q: "A market has a score of (80 + 70 + 90) ÷ 3 on three features. What is the average?", a: 80, sol: "240 ÷ 3 = <b>80</b>." },
  { q: "A firm's revenue is $500,000 and costs are $420,000. What is profit ($)?", a: 80000, sol: "500,000 − 420,000 = <b>$80,000</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "In a market economy, resources are allocated mainly by:", opts: ["The government", "The price mechanism", "Planners", "Trade unions"], a: 1, why: "Prices." },
  { q: "Consumer sovereignty means:", opts: ["The government decides", "Consumers' spending decides what is produced", "Firms decide alone", "Prices are fixed"], a: 1, why: "Consumers have the power." },
  { q: "Firms in a market economy are motivated by:", opts: ["Social welfare only", "Profit", "Taxes", "Planning"], a: 1, why: "Profit motive." },
  { q: "Which is a feature of a market economy?", opts: ["State ownership of most firms", "Competition between firms", "Central planning", "Fixed prices"], a: 1, why: "Competition." },
  { q: "No country has a pure market economy because:", opts: ["Governments always play some role", "Prices do not exist", "Firms are banned", "Wants are limited"], a: 0, why: "Most are mixed." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Market economic system", "An economy where resources are mainly privately owned and allocated by the price mechanism."],
  ["Price mechanism", "Prices adjusting to allocate resources."],
  ["Consumer sovereignty", "Consumers' spending decides what is produced."],
  ["Profit motive", "Firms' aim of earning profit."],
  ["Competition", "Rivalry between firms for customers."],
  ["Private ownership", "Resources owned by individuals and firms."],
  ["Free market", "A market with little government interference."],
  ["Planned economy", "An economy where the government allocates resources."],
  ["Mixed economy", "An economy combining market and government decision-making."],
] });
labA(); 
