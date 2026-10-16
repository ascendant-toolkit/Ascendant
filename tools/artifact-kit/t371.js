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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Competition lowers price", base: { n: 0 }, draw: mkChain(["Many bakeries sell similar bread", "One bakery raises its price", "Customers switch to rivals", "The bakery loses sales and cuts its price", "Competition keeps prices low"], "--good"), steps: chainSteps(["Many bakeries sell similar bread", "One bakery raises its price", "Customers switch to rivals", "The bakery loses sales and cuts its price", "Competition keeps prices low"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Competition limits profit", base: { n: 0 }, draw: mkChain(["A firm in a market earns high profit", "Other firms see this and enter easily", "Supply rises and price falls", "Profit per firm falls", "Profit returns to a normal level"], "--accent"), steps: chainSteps(["A firm in a market earns high profit", "Other firms see this and enter easily", "Supply rises and price falls", "Profit per firm falls", "Profit returns to a normal level"]) });
function labA() {
  const ids = ["a0","a1"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const p = 10 + 40 / Math.sqrt(v[0]) - v[1] * 0.2, ch = Math.round(v[0] * 1.5), pr = Math.max(0, 50 / v[0] - v[1] * 0.4); return { r: ['$' + p.toFixed(1), ch, '$' + pr.toFixed(1) + 'k'], t: 'With ' + v[0] + ' firms and entry ease ' + v[1] + ', the price is about $' + p.toFixed(1) + ', buyers have ' + ch + ' products to choose from and profit per firm is about $' + pr.toFixed(1) + 'k. More firms and easier entry push price and profit down and choice up (illustrative model).', bars: [['Price', p, '--warn', '$' + p.toFixed(1)], ['Choice ÷ 3', ch / 3, '--accent', ch], ['Profit per firm', pr, '--bad', '$' + pr.toFixed(1) + 'k']] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Number of firms", min: 1, max: 30, step: 1, value: 8, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Ease of entry (1 hard, 10 easy)", min: 1, max: 10, step: 1, value: 7, fmt: (v) => v, onInput: labA });
const L2 = [{"n": "Hundreds of small sellers", "a": "Yes", "b": "Many firms."}, {"n": "A single supplier", "a": "No", "b": "That is a monopoly."}, {"n": "Easy entry for new firms", "a": "Yes", "b": "Low barriers."}, {"n": "Huge patents block entry", "a": "No", "b": "Barriers to entry."}, {"n": "Identical products", "a": "Yes", "b": "Firms compete on price."}, {"n": "One firm sets the price", "a": "No", "b": "Price maker, not taker."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Fits competitive market?</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Is each effect of <b>competition</b> likely to <b>rise</b> or <b>fall</b>?", buckets: [{"label": "Rises"}, {"label": "Falls"}], items: [{"text": "Quality of products", "b": 0}, {"text": "Consumer choice", "b": 0}, {"text": "Efficiency", "b": 0}, {"text": "Prices", "b": 1}, {"text": "Profit per firm", "b": 1}, {"text": "Barriers to entry", "b": 1}], done: "Many firms." });
Lib.classify($("#cl2"), { prompt: "Is each an <b>advantage</b> or a <b>disadvantage</b> of competitive markets?", buckets: [{"label": "Advantage"}, {"label": "Disadvantage"}], items: [{"text": "Lower prices", "b": 0}, {"text": "Wider choice", "b": 0}, {"text": "Innovation", "b": 0}, {"text": "Little profit to fund research", "b": 1}, {"text": "Firms may fail", "b": 1}, {"text": "Cutting quality to cut costs", "b": 1}], done: "Weigh both." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Competitive market", "Many firms, easy entry, little control over price"], ["Price taker", "A firm that must accept the market price"], ["Barriers to entry", "Obstacles stopping new firms entering"], ["Substitutes", "Goods that can replace each other"], ["Normal profit", "The minimum profit to keep a firm in business"], ["Consumer sovereignty", "Consumers decide what is produced"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how competition improves quality</b>.", items: ["Many firms compete for customers", "Firms want to stand out", "They improve quality and service", "Customers choose the better products", "Overall quality rises"], done: "Competition drives quality." });
Lib.calc($("#c1"), { qs: [
  { q: "The market price is $8 and a firm tries $10. Customers switch. By what percentage was the firm's price above the market price?", a: 25, sol: "2 ÷ 8 × 100 = <b>25%</b>." },
  { q: "There are 20 firms each with 5% market share. What is the total market share (%)?", a: 100, sol: "20 × 5 = <b>100%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A feature of a competitive market is:", opts: ["One firm controls price", "Many firms", "High barriers to entry", "No substitutes"], a: 1, why: "Many firms." },
  { q: "Competition usually leads to:", opts: ["Higher prices", "Lower prices", "Less choice", "Lower quality"], a: 1, why: "Undercutting." },
  { q: "Easy entry means:", opts: ["Firms can join the market easily", "Firms cannot join", "Prices are fixed", "There is one seller"], a: 0, why: "Low barriers." },
  { q: "A disadvantage of competitive markets is:", opts: ["Higher prices", "Low profit may limit research", "Less choice", "Monopoly power"], a: 1, why: "Little left to invest." },
  { q: "A price taker:", opts: ["Sets the market price", "Accepts the market price", "Is a monopoly", "Charges more than rivals"], a: 1, why: "No price power." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Competitive market", "A market with many firms, easy entry and little price control."],
  ["Price taker", "A firm that cannot influence the market price."],
  ["Barriers to entry", "Obstacles that stop new firms entering a market."],
  ["Substitute", "A good that can replace another."],
  ["Normal profit", "The minimum profit needed to stay in business."],
  ["Competition", "Rivalry between firms for customers."],
  ["Consumer choice", "The range of products available."],
  ["Efficiency", "Producing without waste."],
  ["Innovation", "New products or methods."],
] });
labA(); 
