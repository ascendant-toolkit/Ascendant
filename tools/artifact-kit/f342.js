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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "A horizontal merger", base: { n: 0 }, draw: mkChain(["Two supermarket chains merge", "Combined size raises buying power", "Costs fall through economies of scale", "Competition in the market falls", "Prices may rise if market power grows"], "--accent"), steps: chainSteps(["Two supermarket chains merge", "Combined size raises buying power", "Costs fall through economies of scale", "Competition in the market falls", "Prices may rise if market power grows"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "A vertical merger", base: { n: 0 }, draw: mkChain(["A bakery buys a flour mill (backward integration)", "It controls its flour supply", "It cuts out the miller's profit margin", "Quality and supply are more secure", "But the bakery needs new skills to run a mill"], "--good"), steps: chainSteps(["A bakery buys a flour mill (backward integration)", "It controls its flour supply", "It cuts out the miller's profit margin", "Quality and supply are more secure", "But the bakery needs new skills to run a mill"]) });
Lib.stepper($("#st2"), { w: 760, h: 380, label: "A conglomerate merger", base: { n: 0 }, draw: mkChain(["A food firm buys a software firm", "Its profits are spread across industries", "A fall in food demand matters less", "But managers lack software experience", "Gains are mainly diversification, not scale"], "--warn"), steps: chainSteps(["A food firm buys a software firm", "Its profits are spread across industries", "A fall in food demand matters less", "But managers lack software experience", "Gains are mainly diversification, not scale"]) });
function labA() {
  const ids = ["a0","a1","a2"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const q = v[0] * 2, after = v[1] * (1 - v[2] / 100), saving = (v[1] - after) * q; return { r: [q + ' units', '$' + v[1].toFixed(2), '$' + after.toFixed(2)], t: 'Two firms each making ' + v[0] + ' units at $' + v[1] + ' merge into one making ' + q + ' units. A ' + v[2] + '% saving cuts unit cost to $' + after.toFixed(2) + ' and saves $' + saving.toFixed(0) + ' in total. Gains come from economies of scale (horizontal merger), but if the merged firm has market power, prices could rise.', bars: [['Cost before', v[1], '--bad'], ['Cost after', after, '--good']] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Output of each firm (units)", min: 100, max: 1000, step: 100, value: 500, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Cost per unit before ($)", min: 5, max: 30, step: 1, value: 20, fmt: (v) => '$' + v, onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Cost saving from the merger (%)", min: 0, max: 30, step: 5, value: 10, fmt: (v) => v + '%', onInput: labA });
const L2 = [{"n": "Two car makers merge", "a": "Horizontal", "b": "Same stage, same industry."}, {"n": "A bakery buys a flour mill", "a": "Vertical (backward)", "b": "Different stage, towards suppliers."}, {"n": "A brewer buys pubs", "a": "Vertical (forward)", "b": "Different stage, towards customers."}, {"n": "A food firm buys a software firm", "a": "Conglomerate", "b": "Unrelated industries."}, {"n": "Two banks merge", "a": "Horizontal", "b": "Same stage, same industry."}, {"n": "A car maker buys a tyre firm", "a": "Vertical (backward)", "b": "Supplier."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Which <b>type of merger</b> is each?", buckets: [{"label": "Horizontal"}, {"label": "Vertical"}, {"label": "Conglomerate"}], items: [{"text": "Two supermarkets", "b": 0}, {"text": "Two airlines", "b": 0}, {"text": "A brewer and a chain of pubs", "b": 1}, {"text": "A bakery and a flour mill", "b": 1}, {"text": "A food firm and a phone maker", "b": 2}, {"text": "A bank and a car maker", "b": 2}], done: "Same, linked, unrelated." });
Lib.classify($("#cl2"), { prompt: "Is each an <b>advantage</b> or a <b>disadvantage</b> of mergers?", buckets: [{"label": "Advantage"}, {"label": "Disadvantage"}], items: [{"text": "Economies of scale", "b": 0}, {"text": "Spreading risk", "b": 0}, {"text": "Secure supplies", "b": 0}, {"text": "Job losses", "b": 1}, {"text": "Less competition and higher prices", "b": 1}, {"text": "Culture clashes", "b": 1}], done: "Weigh both." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Merger", "Two firms joining to form one"], ["Horizontal merger", "Same stage, same industry"], ["Vertical merger", "Different stages of the same chain"], ["Conglomerate merger", "Firms in unrelated industries"], ["Backward integration", "Merging with a supplier"], ["Diversification", "Spreading risk across different activities"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a horizontal merger may raise prices</b>.", items: ["Two rivals merge", "Competition in the market falls", "The merged firm gains market power", "It faces less pressure to cut prices", "Prices may rise"], done: "Market power." });
Lib.calc($("#c1"), { qs: [
  { q: "Two firms each have $50m revenue and merge. Costs fall by $4m. If total costs were $80m, what are the new costs ($m)?", a: 76, sol: "80 − 4 = <b>$76m</b>." },
  { q: "Firm A has 30% of the market and Firm B 25%. What is the combined share (%)?", a: 55, sol: "30 + 25 = <b>55%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A horizontal merger joins firms:", opts: ["At different stages", "At the same stage in the same industry", "In different industries", "Abroad only"], a: 1, why: "Same stage." },
  { q: "A bakery buying a flour mill is:", opts: ["Horizontal", "Vertical", "Conglomerate", "Hostile"], a: 1, why: "Backward vertical." },
  { q: "A conglomerate merger helps to:", opts: ["Spread risk", "Create a monopoly", "Cut competition", "Raise prices"], a: 0, why: "Diversification." },
  { q: "A disadvantage of horizontal mergers is:", opts: ["Economies of scale", "Possible monopoly power", "Diversification", "Secure supplies"], a: 1, why: "Less competition." },
  { q: "Forward integration is merging with a:", opts: ["Supplier", "Customer or retailer", "Rival", "Bank"], a: 1, why: "Towards the customer." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Merger", "Two firms joining to form one."],
  ["Horizontal merger", "Firms at the same stage in the same industry."],
  ["Vertical merger", "Firms at different stages of the same chain."],
  ["Conglomerate merger", "Firms in unrelated industries."],
  ["Backward integration", "Merging with a supplier."],
  ["Forward integration", "Merging with a retailer or customer."],
  ["Diversification", "Spreading risk across different activities."],
  ["Market power", "The ability to influence price."],
  ["Competition authority", "A body that investigates mergers."],
] });
labA(); 
