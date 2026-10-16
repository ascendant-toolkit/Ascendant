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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Fixed and variable costs", base: { n: 0 }, draw: mkChain(["A bakery pays rent of $100 a day whatever it bakes", "It also pays $2 of flour and energy per loaf", "Rent is a fixed cost; flour is a variable cost", "TC = FC + VC", "Total cost rises as output rises"], "--accent"), steps: chainSteps(["A bakery pays rent of $100 a day whatever it bakes", "It also pays $2 of flour and energy per loaf", "Rent is a fixed cost; flour is a variable cost", "TC = FC + VC", "Total cost rises as output rises"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Why AFC falls with output", base: { n: 0 }, draw: mkChain(["Fixed cost is $100", "At 10 units, AFC = $10", "At 50 units, AFC = $2", "At 100 units, AFC = $1", "Fixed cost is spread over more units"], "--good"), steps: chainSteps(["Fixed cost is $100", "At 10 units, AFC = $10", "At 50 units, AFC = $2", "At 100 units, AFC = $1", "Fixed cost is spread over more units"]) });
function labA() {
  const ids = ["a0","a1","a2"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const vc = v[1] * v[2], tc = v[0] + vc, atc = tc / v[2], afc = v[0] / v[2], avc = vc / v[2]; return { r: ['$' + tc, '$' + atc.toFixed(2), '$' + afc.toFixed(2) + ' + $' + avc.toFixed(2)], t: 'FC = $' + v[0] + '; VC = $' + v[1] + ' × ' + v[2] + ' = $' + vc + '; TC = $' + tc + '. AFC = ' + v[0] + ' ÷ ' + v[2] + ' = $' + afc.toFixed(2) + '; AVC = $' + avc.toFixed(2) + '; ATC = ' + tc + ' ÷ ' + v[2] + ' = $' + atc.toFixed(2) + ' (which equals AFC + AVC). Raise output and AFC falls while AVC stays the same here.', bars: [['AFC', afc, '--warn', '$' + afc.toFixed(2)], ['AVC', avc, '--accent', '$' + avc.toFixed(2)], ['ATC', atc, '--good', '$' + atc.toFixed(2)]] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Fixed cost ($)", min: 0, max: 500, step: 50, value: 100, fmt: (v) => '$' + v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Variable cost per unit ($)", min: 1, max: 20, step: 1, value: 4, fmt: (v) => '$' + v, onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Output (units)", min: 10, max: 200, step: 10, value: 50, fmt: (v) => v, onInput: labA });
const L2 = [{"n": "Factory rent", "a": "Fixed", "b": "Same whatever the output."}, {"n": "Raw materials", "a": "Variable", "b": "Rises with output."}, {"n": "Manager's salary", "a": "Fixed", "b": "Paid regardless of output."}, {"n": "Piece-rate wages", "a": "Variable", "b": "Linked to output."}, {"n": "Electricity for machines", "a": "Variable", "b": "More output, more power."}, {"n": "Loan interest", "a": "Fixed", "b": "Does not change with output."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Is each a <b>fixed</b> or <b>variable</b> cost?", buckets: [{"label": "Fixed cost"}, {"label": "Variable cost"}], items: [{"text": "Rent", "b": 0}, {"text": "Insurance", "b": 0}, {"text": "Manager's salary", "b": 0}, {"text": "Raw materials", "b": 1}, {"text": "Packaging", "b": 1}, {"text": "Wages paid per item made", "b": 1}], done: "Does it change with output?" });
Lib.classify($("#cl2"), { prompt: "Which <b>cost measure</b> is each formula?", buckets: [{"label": "TC"}, {"label": "AFC"}, {"label": "AVC"}, {"label": "ATC"}], items: [{"text": "FC + VC", "b": 0}, {"text": "FC ÷ output", "b": 1}, {"text": "VC ÷ output", "b": 2}, {"text": "TC ÷ output", "b": 3}, {"text": "AFC + AVC", "b": 3}], done: "Learn the formulas." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Fixed cost", "Does not change with output"], ["Variable cost", "Changes with output"], ["Total cost", "FC + VC"], ["Average total cost", "TC ÷ output"], ["Average fixed cost", "FC ÷ output"], ["Average variable cost", "VC ÷ output"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps in order: <b>calculating ATC</b>.", items: ["Find fixed cost", "Find variable cost", "Add them to get total cost", "Divide total cost by output", "The result is average total cost"], done: "ATC = TC ÷ output." });
Lib.calc($("#c1"), { qs: [
  { q: "FC is $100 and VC is $200. What is TC ($)?", a: 300, sol: "100 + 200 = <b>$300</b>." },
  { q: "TC is $300 and output is 50 units. What is ATC ($)?", a: 6, sol: "300 ÷ 50 = <b>$6</b>." },
  { q: "FC is $100 and output is 50. What is AFC ($)?", a: 2, sol: "100 ÷ 50 = <b>$2</b>." },
  { q: "VC is $200 and output is 50. What is AVC ($)?", a: 4, sol: "200 ÷ 50 = <b>$4</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Total cost is:", opts: ["FC − VC", "FC + VC", "FC × VC", "VC ÷ FC"], a: 1, why: "Sum." },
  { q: "Which is a fixed cost?", opts: ["Raw materials", "Rent", "Packaging", "Piece-rate pay"], a: 1, why: "Does not vary." },
  { q: "ATC equals:", opts: ["TC ÷ output", "FC ÷ VC", "VC ÷ TC", "Output ÷ TC"], a: 0, why: "Per unit." },
  { q: "As output rises, AFC:", opts: ["Rises", "Falls", "Stays constant", "Doubles"], a: 1, why: "Spread over more units." },
  { q: "ATC =", opts: ["AFC + AVC", "AFC − AVC", "AFC × AVC", "AVC ÷ AFC"], a: 0, why: "Sum of averages." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Fixed cost", "A cost that does not change with output."],
  ["Variable cost", "A cost that changes with output."],
  ["Total cost", "Fixed cost plus variable cost."],
  ["Average fixed cost", "Fixed cost divided by output."],
  ["Average variable cost", "Variable cost divided by output."],
  ["Average total cost", "Total cost divided by output."],
  ["Output", "The quantity produced."],
  ["Short run", "A period in which some costs are fixed."],
  ["Unit cost", "Cost per item."],
] });
labA(); 
