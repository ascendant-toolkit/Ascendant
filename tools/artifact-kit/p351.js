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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Derived demand", base: { n: 0 }, draw: mkChain(["Consumers demand more of a product", "Firms need to produce more", "They demand more labour, capital and land", "The demand for factors is derived from the product", "Factor prices (wages) may rise"], "--accent"), steps: chainSteps(["Consumers demand more of a product", "Firms need to produce more", "They demand more labour, capital and land", "The demand for factors is derived from the product", "Factor prices (wages) may rise"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Substituting capital for labour", base: { n: 0 }, draw: mkChain(["The wage rate rises", "Labour becomes dearer relative to machines", "Firms demand fewer workers", "They demand more machines", "The mix of factors changes"], "--warn"), steps: chainSteps(["The wage rate rises", "Labour becomes dearer relative to machines", "Firms demand fewer workers", "They demand more machines", "The mix of factors changes"]) });
function labA() {
  const ids = ["a0","a1","a2"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {let n = 0, rev = 0, prev = 0; for (let w = 1; w <= 12; w++) { const out = v[2] * Math.pow(0.85, w - 1), mrp = out * v[0]; if (mrp >= v[1]) { n = w; prev += out; } else break; } const tr = prev * v[0], cost = n * v[1]; return { r: [n + ' workers', '$' + tr.toFixed(0), (tr - cost >= 0 ? '+' : '−') + '$' + Math.abs(tr - cost).toFixed(0)], t: 'The firm hires workers while the extra revenue each adds (their marginal revenue product) is at least the wage. With product price $' + v[0] + ', wage $' + v[1] + ' and first-worker output ' + v[2] + ', it hires ' + n + ' workers. A higher product price or higher productivity raises the demand for labour; a higher wage lowers it.', bars: [['Workers hired', n, '--accent'], ['Revenue ÷ 20', tr / 20, '--good', '$' + tr.toFixed(0)], ['Labour cost ÷ 20', cost / 20, '--warn', '$' + cost]] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Price of the product ($)", min: 2, max: 20, step: 1, value: 10, fmt: (v) => '$' + v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Wage per worker ($)", min: 10, max: 100, step: 5, value: 40, fmt: (v) => '$' + v, onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Productivity (output of first worker)", min: 5, max: 20, step: 1, value: 12, fmt: (v) => v, onInput: labA });
const L2 = [{"n": "Demand for the product rises", "a": "Demand for factors rises", "b": "Derived demand."}, {"n": "The wage rises", "a": "Quantity of labour demanded falls", "b": "Dearer labour."}, {"n": "Machines become cheaper", "a": "Demand for labour falls, for machines rises", "b": "Substitution."}, {"n": "Workers become more productive", "a": "Demand for labour rises", "b": "More output per $."}, {"n": "A shortage of skilled workers", "a": "Quantity demanded falls", "b": "Higher price; scarce."}, {"n": "Product demand falls", "a": "Demand for factors falls", "b": "Derived demand."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect on demand for the factor</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Does each <b>increase</b> or <b>decrease</b> demand for labour?", buckets: [{"label": "Increase"}, {"label": "Decrease"}], items: [{"text": "Product demand rises", "b": 0}, {"text": "Workers become more productive", "b": 0}, {"text": "Machines become dearer", "b": 0}, {"text": "Product demand falls", "b": 1}, {"text": "Machines become much cheaper", "b": 1}, {"text": "Productivity falls", "b": 1}], done: "Derived demand." });
Lib.classify($("#cl2"), { prompt: "Which <b>influence</b> is each?", buckets: [{"label": "Product demand"}, {"label": "Price of the factor"}, {"label": "Substitute factors"}, {"label": "Availability"}, {"label": "Productivity"}], items: [{"text": "A boom in car sales", "b": 0}, {"text": "Wages rise", "b": 1}, {"text": "Robots replace workers", "b": 2}, {"text": "A shortage of engineers", "b": 3}, {"text": "Workers trained to work faster", "b": 4}], done: "Five influences." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Derived demand", "Demand for a factor that comes from demand for the product"], ["Marginal revenue product", "Extra revenue from one more unit of a factor"], ["Substitute factors", "Factors that can replace each other"], ["Complementary factors", "Factors used together"], ["Productivity", "Output per unit of input"], ["Availability", "How easy a factor is to obtain"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a rise in product demand raises demand for workers</b>.", items: ["Consumer demand for the product rises", "The firm needs to produce more", "It needs more workers", "Demand for labour rises", "Wages and employment may rise"], done: "Derived demand." });
Lib.calc($("#c1"), { qs: [
  { q: "A worker adds 8 units of output each worth $5. What is the marginal revenue product ($)?", a: 40, sol: "8 × 5 = <b>$40</b>." },
  { q: "A worker's MRP is $40 and the wage is $35. Should the firm hire? Enter the extra profit ($).", a: 5, sol: "40 − 35 = <b>$5</b>: yes." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Derived demand means demand for a factor comes from:", opts: ["Demand for the product", "The government", "Tax", "Imports"], a: 0, why: "Final product." },
  { q: "A rise in wages is likely to:", opts: ["Raise demand for labour", "Lower the quantity of labour demanded", "Have no effect", "Raise productivity"], a: 1, why: "Dearer labour." },
  { q: "Which raises demand for labour?", opts: ["Falling product demand", "Higher productivity", "Dearer product", "Cheaper machines"], a: 1, why: "More output per $." },
  { q: "Machines and workers are often:", opts: ["Substitutes", "Complements only", "Unrelated", "Free"], a: 0, why: "Can replace each other." },
  { q: "A shortage of a factor makes it:", opts: ["Cheaper", "Dearer", "Free", "Unnecessary"], a: 1, why: "Scarcity." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Derived demand", "Demand for a factor of production that comes from demand for the product it makes."],
  ["Marginal revenue product", "The extra revenue from employing one more unit of a factor."],
  ["Substitute factors", "Factors that can replace each other."],
  ["Complementary factors", "Factors used together."],
  ["Productivity", "Output per unit of input."],
  ["Availability", "How easily a factor can be obtained."],
  ["Wage rate", "The price of labour."],
  ["Capital goods", "Goods used to make other goods."],
  ["Quantity demanded", "The amount demanded at a price."],
] });
labA(); 
