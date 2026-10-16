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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Barriers protect a monopoly", base: { n: 0 }, draw: mkChain(["A firm holds a patent on a medicine", "Rivals cannot copy it legally", "The firm faces no competition", "It sets a high price", "High profits persist"], "--accent"), steps: chainSteps(["A firm holds a patent on a medicine", "Rivals cannot copy it legally", "The firm faces no competition", "It sets a high price", "High profits persist"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Monopoly and consumers", base: { n: 0 }, draw: mkChain(["A single supplier controls the market", "It restricts output", "It raises the price", "Consumers pay more and choose from fewer products", "Real incomes and welfare fall"], "--bad"), steps: chainSteps(["A single supplier controls the market", "It restricts output", "It raises the price", "Consumers pay more and choose from fewer products", "Real incomes and welfare fall"]) });
Lib.stepper($("#st2"), { w: 760, h: 380, label: "A possible benefit of monopoly", base: { n: 0 }, draw: mkChain(["A monopoly earns high profit", "It invests in research and technology", "It produces on a very large scale", "Economies of scale cut costs", "Prices may fall and quality may improve"], "--good"), steps: chainSteps(["A monopoly earns high profit", "It invests in research and technology", "It produces on a very large scale", "Economies of scale cut costs", "Prices may fall and quality may improve"]) });
function labA() {
  const ids = ["a0","a1","a2","a3"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const p = v[0] * (1 + v[2] / 100), q = 1000 * (1 - v[3] / 100), comp = (v[0] - v[1]) * 1000, mono = (p - v[1]) * q; return { r: ['$' + p.toFixed(0), q.toFixed(0), (mono - comp >= 0 ? '+' : '−') + '$' + Math.abs(mono - comp).toFixed(0)], t: 'A competitive market sells 1,000 units at $' + v[0] + ' (profit $' + comp.toFixed(0) + '). The monopoly charges $' + p.toFixed(0) + ' and sells ' + q.toFixed(0) + ' units, earning $' + mono.toFixed(0) + '. Consumers pay more and buy less, while barriers to entry let the monopoly keep the extra profit.', bars: [['Competitive price', v[0], '--good'], ['Monopoly price', p, '--bad'], ['Output ÷ 50', q / 50, '--accent', q.toFixed(0)]] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Competitive price ($)", min: 5, max: 50, step: 5, value: 20, fmt: (v) => '$' + v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Cost per unit ($)", min: 2, max: 40, step: 2, value: 16, fmt: (v) => '$' + v, onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Monopoly mark-up over competitive price (%)", min: 0, max: 100, step: 10, value: 40, fmt: (v) => v + '%', onInput: labA });
Lib.slider($("#ga3"), { id: "a3", label: "Cut in output (%)", min: 0, max: 60, step: 5, value: 20, fmt: (v) => v + '%', onInput: labA });
const L2 = [{"n": "Patents", "a": "Legal protection from copying", "b": "A new medicine."}, {"n": "High start-up costs", "a": "Few firms can afford to enter", "b": "Building a railway network."}, {"n": "Control of resources", "a": "Rivals cannot obtain inputs", "b": "A mine owner."}, {"n": "Economies of scale", "a": "Rivals cannot match low costs", "b": "A large utility."}, {"n": "Brand loyalty", "a": "Customers stay with the leader", "b": "A dominant software firm."}, {"n": "Government licence", "a": "Only one firm is allowed", "b": "A state postal service."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>How it protects</th><th>Example</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Is each a <b>barrier to entry</b> or <b>not</b>?", buckets: [{"label": "Barrier to entry"}, {"label": "Not a barrier"}], items: [{"text": "A patent", "b": 0}, {"text": "Huge start-up costs", "b": 0}, {"text": "A legal licence", "b": 0}, {"text": "Low start-up costs", "b": 1}, {"text": "Many suppliers of inputs", "b": 1}, {"text": "Customers easily switch", "b": 1}], done: "What blocks rivals." });
Lib.classify($("#cl2"), { prompt: "Is each an <b>advantage</b> or a <b>disadvantage</b> of monopoly?", buckets: [{"label": "Advantage"}, {"label": "Disadvantage"}], items: [{"text": "Economies of scale", "b": 0}, {"text": "Funds research", "b": 0}, {"text": "Avoids duplicated networks", "b": 0}, {"text": "Higher prices", "b": 1}, {"text": "Less choice", "b": 1}, {"text": "Little pressure to be efficient", "b": 1}], done: "Weigh both." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Monopoly", "A single dominant seller"], ["Barriers to entry", "Obstacles that stop new firms entering"], ["Price maker", "A firm that sets its own price"], ["Natural monopoly", "A market best supplied by one firm"], ["Patent", "Legal protection for an invention"], ["Supernormal profit", "Profit above the minimum needed to stay in business"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a monopoly can reduce consumer welfare</b>.", items: ["A firm is the only seller", "It faces no competition", "It restricts output and raises price", "Consumers pay more and have less choice", "Consumer welfare falls"], done: "Market power harms consumers." });
Lib.calc($("#c1"), { qs: [
  { q: "A monopoly raises its price from $20 to $28. What is the percentage rise?", a: 40, sol: "8 ÷ 20 × 100 = <b>40%</b>." },
  { q: "A monopoly sells 800 units at $28 with cost $16 per unit. What is its profit ($)?", a: 9600, sol: "(28 − 16) × 800 = <b>$9,600</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A monopoly has:", opts: ["Many firms", "One dominant firm", "No profit", "Many substitutes"], a: 1, why: "A single seller." },
  { q: "A barrier to entry is:", opts: ["A patent", "Low cost of entry", "Many suppliers", "Easy information"], a: 0, why: "Blocks rivals." },
  { q: "A monopoly is likely to charge:", opts: ["Lower prices than competition", "Higher prices", "Zero prices", "Equal prices"], a: 1, why: "No rivals." },
  { q: "An advantage of monopoly is:", opts: ["Economies of scale", "Higher prices", "Less choice", "Restricted output"], a: 0, why: "Lower unit costs possible." },
  { q: "A price maker:", opts: ["Accepts the market price", "Sets the price", "Has no profit", "Faces many rivals"], a: 1, why: "Market power." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Monopoly", "A market with a single dominant seller."],
  ["Barriers to entry", "Obstacles that stop new firms entering a market."],
  ["Price maker", "A firm that can set its own price."],
  ["Natural monopoly", "A market where one firm supplies at lowest cost."],
  ["Patent", "Legal protection for an invention."],
  ["Supernormal profit", "Profit above normal profit."],
  ["Market power", "The ability to influence price."],
  ["Regulation", "Government rules to limit abuse of power."],
  ["Competition authority", "A body that investigates monopolies and mergers."],
] });
labA(); 
