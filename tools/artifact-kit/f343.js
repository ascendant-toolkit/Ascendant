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

const PXo = (q) => 90 + q * 5, PYc = (c) => 310 - (c - 6) * 9;
const atcF = (q, sh) => 12 + 0.004 * Math.pow(q - 60, 2) - (sh || 0);
function atcAxes() { return SV.line(PXo(0), PYc(6), PXo(0), PYc(32)) + SV.line(PXo(0), PYc(6), PXo(130), PYc(6)) + SV.text(PXo(0) + 8, 14, "Average total cost ($ per unit)", "sm") + SV.text(PXo(130), PYc(6) + 24, "Output (units)", "sm", { "text-anchor": "end" }); }
function atcPath(sh) { let d = ""; for (let q = 8; q <= 118; q += 2) d += (d ? "L" : "M") + PXo(q).toFixed(1) + " " + PYc(atcF(q, sh)).toFixed(1); return d; }
function atcDraw(sh, q, show) {
  let o = atcAxes() + SV.path(atcPath(0), sh ? "c3" : "c1");
  if (sh) o += SV.path(atcPath(sh), "c2") + SV.text(PXo(112), PYc(atcF(112, sh)) - 8, "ATC₁", "lbl bd t2");
  else o += SV.text(PXo(112), PYc(atcF(112, 0)) - 8, "ATC", "lbl bd t1");
  if (show) { o += SV.rect(PXo(8), PYc(31), PXo(60) - PXo(8), PYc(6) - PYc(31), "", { style: "fill:var(--good)", opacity: 0.1 }) + SV.rect(PXo(60), PYc(31), PXo(118) - PXo(60), PYc(6) - PYc(31), "", { style: "fill:var(--bad)", opacity: 0.1 }) + SV.text(PXo(34), PYc(30), "Economies of scale", "sm bd t3", { "text-anchor": "middle" }) + SV.text(PXo(89), PYc(30), "Diseconomies of scale", "sm bd t4", { "text-anchor": "middle" }) + SV.line(PXo(60), PYc(12), PXo(60), PYc(6), "gr") + SV.text(PXo(60), PYc(6) + 18, "Minimum efficient scale", "sm bd", { "text-anchor": "middle" }); }
  if (q) o += SV.line(PXo(q), PYc(atcF(q, sh || 0)), PXo(q), PYc(6), "gr") + SV.line(PXo(0), PYc(atcF(q, sh || 0)), PXo(q), PYc(atcF(q, sh || 0)), "gr") + SV.circle(PXo(q), PYc(atcF(q, sh || 0)), 7, "dot2") + SV.text(PXo(0) - 8, PYc(atcF(q, sh || 0)), "$" + atcF(q, sh || 0).toFixed(1), "sm bd", { "text-anchor": "end" }) + SV.text(PXo(q), PYc(6) + 18, q, "sm bd", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#st0"), { w: 760, h: (380), label: "The U-shaped ATC curve", base: { sh: 0, q: 0, show: 0 }, draw: (s) => atcDraw(s.sh, s.q, s.show), steps: [
  { cap: "Average total cost (ATC) at different levels of output.", s: { sh: 0, q: 0, show: 0 } },
  { cap: "At low output ATC is high. As output rises, <b>economies of scale</b> cut ATC.", s: { sh: 0, q: 20, show: 1 } },
  { cap: "At <b>minimum efficient scale</b> ATC is at its lowest.", s: { sh: 0, q: 60, show: 1 } },
  { cap: "Beyond that, <b>diseconomies of scale</b> raise ATC again.", s: { sh: 0, q: 100, show: 1 } },
]  });
Lib.stepper($("#st1"), { w: 760, h: (380), label: "External economies of scale", base: { sh: 0, q: 60, show: 0 }, draw: (s) => atcDraw(s.sh, s.q, s.show), steps: [
  { cap: "A firm produces 60 units at ATC $12.", s: { sh: 0, q: 60, show: 0 } },
  { cap: "The industry grows: skilled workers, suppliers and transport improve for <b>all firms</b>. The whole ATC curve shifts <b>down</b> to ATC₁: <b>external economies of scale</b>.", s: { sh: 3, q: 60, show: 0 } },
]  });
Lib.stepper($("#st2"), { w: 760, h: 380, label: "Internal diseconomies of scale", base: { n: 0 }, draw: mkChain(["A firm grows very large", "Communication between departments slows", "Decisions take longer; workers feel remote", "Productivity and quality fall", "Average cost per unit rises"], "--bad"), steps: chainSteps(["A firm grows very large", "Communication between departments slows", "Decisions take longer; workers feel remote", "Productivity and quality fall", "Average cost per unit rises"]) });
function labA() {
  const ids = ["a0","a1"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const c = atcF(v[0], v[1]), st = v[0] < 55 ? 'Economies of scale (ATC falling)' : v[0] <= 65 ? 'Close to minimum efficient scale' : 'Diseconomies of scale (ATC rising)'; return { r: ['$' + c.toFixed(1), st, '$' + (12 - v[1]).toFixed(1)], t: 'At ' + v[0] + ' units ATC is $' + c.toFixed(1) + ': ' + st.toLowerCase() + '. ' + (v[1] ? 'External economies have shifted the whole curve down by $' + v[1] + ', so every output level is cheaper.' : 'Raise the external economies slider to shift the ATC curve downwards.'), svg: atcDraw(v[1], v[0], 1) };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Output (units)", min: 10, max: 115, step: 5, value: 30, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "External economies (fall in ATC, $)", min: 0, max: 5, step: 1, value: 0, fmt: (v) => '$' + v, onInput: labA });
const L2 = [{"n": "A big firm gets bulk discounts", "a": "Internal economy (purchasing)", "b": "Large orders cost less per unit."}, {"n": "Specialist managers raise efficiency", "a": "Internal economy (managerial)", "b": "Better management."}, {"n": "A skilled labour pool grows near the industry", "a": "External economy", "b": "All firms benefit."}, {"n": "Communication slows in a huge firm", "a": "Internal diseconomy", "b": "Poor coordination."}, {"n": "Congestion raises transport costs", "a": "External diseconomy", "b": "Industry too large for its area."}, {"n": "A large firm borrows at lower interest", "a": "Internal economy (financial)", "b": "Lenders trust it."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Is each an <b>economy</b> or a <b>diseconomy</b> of scale?", buckets: [{"label": "Economy of scale"}, {"label": "Diseconomy of scale"}], items: [{"text": "Bulk-buying discounts", "b": 0}, {"text": "Cheaper loans for big firms", "b": 0}, {"text": "Specialist managers", "b": 0}, {"text": "Slow communication", "b": 1}, {"text": "Low morale in a huge workforce", "b": 1}, {"text": "Management hard to coordinate", "b": 1}], done: "Unit costs fall or rise." });
Lib.classify($("#cl2"), { prompt: "Is each <b>internal</b> or <b>external</b>?", buckets: [{"label": "Internal"}, {"label": "External"}], items: [{"text": "Technical economies from large machines", "b": 0}, {"text": "Purchasing discounts", "b": 0}, {"text": "Slow communication in the firm", "b": 0}, {"text": "A skilled labour pool in the region", "b": 1}, {"text": "Better transport links built for the industry", "b": 1}, {"text": "Congestion in an industrial area", "b": 1}], done: "Within the firm vs the industry." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Economies of scale", "Unit costs fall as output rises"], ["Diseconomies of scale", "Unit costs rise as output rises"], ["Internal economies", "Savings within the firm"], ["External economies", "Savings from the industry's growth"], ["Average total cost", "Total cost divided by output"], ["Minimum efficient scale", "The output with the lowest ATC"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how bulk-buying leads to economies of scale</b>.", items: ["A firm grows and orders more materials", "Suppliers give discounts for large orders", "The cost of inputs per unit falls", "Average total cost falls", "The firm gains an economy of scale"], done: "Purchasing economy." });
Lib.calc($("#c1"), { qs: [
  { q: "Total cost is $6,000 for 500 units. What is ATC ($)?", a: 12, sol: "6,000 ÷ 500 = <b>$12</b>." },
  { q: "ATC is $12 at 60 units and $14 at 100 units. By what percentage does ATC rise?", a: 17, sol: "2 ÷ 12 × 100 ≈ <b>17%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Economies of scale mean:", opts: ["Unit costs fall as output rises", "Unit costs rise as output rises", "Fixed costs rise", "Prices fall"], a: 0, why: "Lower ATC." },
  { q: "A diseconomy of scale is:", opts: ["Bulk-buying discounts", "Poor communication in a large firm", "Cheaper loans", "Specialist managers"], a: 1, why: "Unit costs rise." },
  { q: "External economies of scale:", opts: ["Affect one firm only", "Benefit all firms in the industry", "Raise costs", "Are internal"], a: 1, why: "Industry-wide." },
  { q: "On the ATC curve, the lowest point is:", opts: ["Where ATC is highest", "Minimum efficient scale", "Zero output", "Maximum output"], a: 1, why: "Lowest unit cost." },
  { q: "Which is an internal economy?", opts: ["A skilled labour pool in the region", "Better local roads", "Bulk-buying discounts", "A nearby supplier"], a: 2, why: "Within the firm." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Economies of scale", "Falling average cost as output increases."],
  ["Diseconomies of scale", "Rising average cost as output increases."],
  ["Internal economies", "Cost savings arising within a firm."],
  ["External economies", "Cost savings arising from industry growth."],
  ["Average total cost", "Total cost divided by output."],
  ["Minimum efficient scale", "The output at which ATC is lowest."],
  ["Bulk-buying", "Buying inputs in large quantities for a discount."],
  ["Technical economies", "Using larger, more efficient machinery."],
  ["Managerial economies", "Savings from specialist managers."],
] });
labA(); 
