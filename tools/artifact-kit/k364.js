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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Sales and revenue at a fixed price", base: { n: 0 }, draw: mkChain(["A shop sells 100 items at $10: TR = $1,000", "Advertising lifts sales to 150", "TR = 150 × $10 = $1,500", "Revenue rises with sales", "AR is still $10"], "--good"), steps: chainSteps(["A shop sells 100 items at $10: TR = $1,000", "Advertising lifts sales to 150", "TR = 150 × $10 = $1,500", "Revenue rises with sales", "AR is still $10"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "A price cut and revenue", base: { n: 0 }, draw: mkChain(["A firm cuts price from $10 to $8", "Quantity sold rises from 20 to 40", "TR rises from $200 to $320", "Demand is elastic: revenue rises", "Beyond a point further cuts reduce revenue"], "--warn"), steps: chainSteps(["A firm cuts price from $10 to $8", "Quantity sold rises from 20 to 40", "TR rises from $200 to $320", "Demand is elastic: revenue rises", "Beyond a point further cuts reduce revenue"]) });
function labA() {
  const ids = ["a0"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const q = { 10: 20, 8: 40, 6: 60, 4: 70, 2: 80 }[v[0]], tr = v[0] * q, best = Math.max(200, 320, 360, 280, 160); return { r: [q, '$' + tr, '$' + v[0]], t: 'At $' + v[0] + ' the firm sells ' + q + ' units: TR = $' + v[0] + ' × ' + q + ' = $' + tr + ' and AR = $' + v[0] + '. ' + (tr === best ? 'This is the highest revenue in the table.' : 'Revenue would be higher at $6 ($360).') + ' Lowering price raises sales, but revenue only rises while the quantity gain is proportionately bigger than the price fall.', bars: [[ '$10', 200, '--accent'], ['$8', 320, '--accent'], ['$6', 360, '--accent'], ['$4', 280, '--accent'], ['$2', 160, '--accent']].map((b, i) => [b[0], b[1], [10, 8, 6, 4, 2][i] === v[0] ? '--good' : '--accent', '$' + b[1]]) };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Price ($)", min: 2, max: 10, step: 2, value: 6, fmt: (v) => '$' + v, onInput: labA });
const L2 = [{"n": "Successful advertising", "a": "Revenue rises", "b": "More sold at the same price (demand shifts right)."}, {"n": "A price cut with elastic demand", "a": "Revenue rises", "b": "Quantity rises by more than price falls."}, {"n": "A price cut with inelastic demand", "a": "Revenue falls", "b": "Quantity rises by less than price falls."}, {"n": "A price rise with elastic demand", "a": "Revenue falls", "b": "Quantity falls by more."}, {"n": "A price rise with inelastic demand", "a": "Revenue rises", "b": "Quantity falls by less."}, {"n": "A rival cuts its price", "a": "Revenue falls", "b": "Customers switch away."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect on revenue</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "What happens to <b>total revenue</b>?", buckets: [{"label": "Rises"}, {"label": "Falls"}], items: [{"text": "Sales rise at a constant price", "b": 0}, {"text": "Price cut, elastic demand", "b": 0}, {"text": "Price rise, inelastic demand", "b": 0}, {"text": "Sales fall at a constant price", "b": 1}, {"text": "Price cut, inelastic demand", "b": 1}, {"text": "Price rise, elastic demand", "b": 1}], done: "Link to PED." });
Lib.classify($("#cl2"), { prompt: "Is each way to <b>increase sales</b> or a <b>result</b> of higher sales?", buckets: [{"label": "Way to increase sales"}, {"label": "Result of higher sales"}], items: [{"text": "Advertising", "b": 0}, {"text": "Lower price", "b": 0}, {"text": "Better quality", "b": 0}, {"text": "Higher total revenue", "b": 1}, {"text": "Larger market share", "b": 1}, {"text": "More production needed", "b": 1}], done: "Cause and effect." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Total revenue", "Price × quantity"], ["Average revenue", "TR ÷ quantity"], ["Elastic demand", "Price cut raises revenue"], ["Inelastic demand", "Price cut lowers revenue"], ["Advertising", "Aims to raise sales at every price"], ["Sales", "Quantity sold"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how advertising raises revenue</b>.", items: ["A firm runs an advertising campaign", "Demand for its product rises", "More units are sold at the same price", "Total revenue = price × higher quantity", "Revenue rises"], done: "Sales up, revenue up." });
Lib.calc($("#c1"), { qs: [
  { q: "Price falls from $8 to $6 and quantity rises from 40 to 60. What is the new TR ($)?", a: 360, sol: "6 × 60 = <b>$360</b>." },
  { q: "Price is $6 and TR is $360. How many units were sold?", a: 60, sol: "360 ÷ 6 = <b>60</b>." },
  { q: "Sales rise from 150 to 180 at a constant price of $10. By how much does TR rise ($)?", a: 300, sol: "30 × 10 = <b>$300</b>." },
  { q: "A firm sells 400 units for TR of $2,000. What is AR ($)?", a: 5, sol: "2,000 ÷ 400 = <b>$5</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "If price is constant, a rise in sales:", opts: ["Raises TR", "Lowers TR", "Leaves TR unchanged", "Lowers AR"], a: 0, why: "More units, same price." },
  { q: "A price cut raises revenue when demand is:", opts: ["Inelastic", "Elastic", "Zero", "Fixed"], a: 1, why: "Quantity gain bigger." },
  { q: "AR =", opts: ["TR ÷ quantity", "TR × quantity", "TC ÷ quantity", "Price × cost"], a: 0, why: "Per unit." },
  { q: "Advertising aims to:", opts: ["Raise demand and sales", "Cut costs", "Raise taxes", "Lower AR"], a: 0, why: "More sales." },
  { q: "Revenue is the same as profit:", opts: ["True", "False", "Only for large firms", "Only in the long run"], a: 1, why: "Profit is revenue minus costs." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Total revenue", "Price × quantity sold."],
  ["Average revenue", "Total revenue ÷ quantity."],
  ["Sales", "The quantity sold."],
  ["Elastic demand", "Quantity responds strongly to price."],
  ["Inelastic demand", "Quantity responds weakly to price."],
  ["Advertising", "Promotion to raise demand."],
  ["Market share", "A firm's share of total sales."],
  ["Demand schedule", "A table of prices and quantities."],
  ["Profit", "TR − TC."],
] });
labA(); 
