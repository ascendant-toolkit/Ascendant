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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Investment raises productivity", base: { n: 0 }, draw: mkChain(["A firm invests in new machinery and training", "Each worker has better tools and skills", "Output per worker rises", "Unit costs fall", "The firm becomes more competitive"], "--good"), steps: chainSteps(["A firm invests in new machinery and training", "Each worker has better tools and skills", "Output per worker rises", "Unit costs fall", "The firm becomes more competitive"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "More production is not always more productivity", base: { n: 0 }, draw: mkChain(["A firm hires twice as many workers", "Output rises, but not by twice as much", "Output per worker falls", "Production is higher but productivity is lower", "Costs per unit may rise"], "--warn"), steps: chainSteps(["A firm hires twice as many workers", "Output rises, but not by twice as much", "Output per worker falls", "Production is higher but productivity is lower", "Costs per unit may rise"]) });
function labA() {
  const ids = ["a0","a1","a2"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const per = 20 + 0.04 * v[1] + 0.08 * v[2], out = per * v[0], cost = (v[0] * 100 + v[1] * 0.2 + v[2] * 0.2) / out; return { r: [Math.round(out) + ' units', per.toFixed(1), '$' + cost.toFixed(2)], t: v[0] + ' workers with $' + v[1] + 'k of machinery and $' + v[2] + 'k of training produce ' + Math.round(out) + ' units, or ' + per.toFixed(1) + ' per worker. Cost per unit is $' + cost.toFixed(2) + ' (wages $100 per worker plus annual investment costs). More investment raises output per worker and lowers unit cost (illustrative model).', bars: [['Output per worker', per, '--good'], ['Output ÷ 20', out / 20, '--accent', Math.round(out)], ['Cost per unit ×10', cost * 10, '--warn', '$' + cost.toFixed(2)]] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Number of workers", min: 10, max: 100, step: 10, value: 50, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Investment in machinery ($000)", min: 0, max: 500, step: 50, value: 100, fmt: (v) => '$' + v + 'k', onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Investment in training ($000)", min: 0, max: 200, step: 20, value: 40, fmt: (v) => '$' + v + 'k', onInput: labA });
const L2 = [{"n": "A factory makes 5,000 cars a year", "a": "Production", "b": "Total output."}, {"n": "Each worker makes 40 cars a year", "a": "Productivity", "b": "Output per worker."}, {"n": "Output rises 10% after hiring 10% more workers", "a": "Production up, productivity unchanged", "b": "Output per worker stays the same."}, {"n": "Output rises 10% with the same workers", "a": "Productivity up", "b": "Output per worker rises."}, {"n": "A country's output rises", "a": "Production", "b": "Total output."}, {"n": "New machines let each worker make more", "a": "Productivity", "b": "Better tools."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Measure</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Is each about <b>production</b> or <b>productivity</b>?", buckets: [{"label": "Production"}, {"label": "Productivity"}], items: [{"text": "Total output of 10,000 units", "b": 0}, {"text": "Total GDP", "b": 0}, {"text": "Output per worker per hour", "b": 1}, {"text": "Output per machine", "b": 1}, {"text": "A factory makes 500 shirts a day", "b": 0}, {"text": "Each worker makes 25 shirts a day", "b": 1}], done: "Total vs per input." });
Lib.classify($("#cl2"), { prompt: "Does each <b>raise</b> or <b>lower</b> productivity?", buckets: [{"label": "Raises productivity"}, {"label": "Lowers productivity"}], items: [{"text": "Better training", "b": 0}, {"text": "New technology", "b": 0}, {"text": "Better management", "b": 0}, {"text": "Poor health of workers", "b": 1}, {"text": "Outdated machines", "b": 1}, {"text": "Low motivation", "b": 1}], done: "Influences." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Production", "Total output"], ["Productivity", "Output per unit of input"], ["Investment", "Spending on capital goods or training"], ["Human capital", "Workers' skills and knowledge"], ["Technology", "Methods and machines that raise output"], ["Unit cost", "Cost per item"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how investment in training raises growth</b>.", items: ["Firms invest in training", "Workers become more skilled", "Productivity rises", "Unit costs fall and output rises", "Competitiveness and growth improve"], done: "Human capital." });
Lib.calc($("#c1"), { qs: [
  { q: "A factory with 50 workers makes 1,000 units. What is output per worker?", a: 20, sol: "1,000 ÷ 50 = <b>20</b>." },
  { q: "Output rises from 1,000 to 1,200 with the same 50 workers. By what percentage does productivity rise?", a: 20, sol: "200 ÷ 1,000 × 100 = <b>20%</b>." },
  { q: "Output rises 10% and workers rise 10%. What is the change in productivity (%)?", a: 0, sol: "Productivity is unchanged: <b>0%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Productivity is:", opts: ["Total output", "Output per unit of input", "Profit", "Wages"], a: 1, why: "Per worker or machine." },
  { q: "Which raises productivity?", opts: ["Poor training", "Investment in technology", "Lower pay", "Fewer machines"], a: 1, why: "Better tools." },
  { q: "If output rises 5% and workers rise 5%, productivity:", opts: ["Rises", "Falls", "Is unchanged", "Doubles"], a: 2, why: "Same output per worker." },
  { q: "Higher productivity usually:", opts: ["Raises unit cost", "Lowers unit cost", "Cuts output", "Raises prices"], a: 1, why: "More output per $." },
  { q: "Human capital is:", opts: ["Machines", "Workers' skills", "Money", "Land"], a: 1, why: "Skills and knowledge." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Production", "The total output of goods and services."],
  ["Productivity", "Output per unit of input, such as output per worker."],
  ["Investment", "Spending on capital goods, technology or training."],
  ["Human capital", "Workers' skills, knowledge and health."],
  ["Technology", "Methods and machines that raise output."],
  ["Unit cost", "Cost per item produced."],
  ["Competitiveness", "A firm's ability to compete on price and quality."],
  ["Economic growth", "A rise in the economy's output."],
  ["Efficiency", "Using inputs without waste."],
] });
labA(); 
