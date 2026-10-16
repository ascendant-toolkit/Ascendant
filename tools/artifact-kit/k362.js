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

const QS = [2, 3, 4, 5, 6, 7, 8, 9, 10], VCS = [50, 66, 80, 100, 126, 160, 204, 260, 330], FCc = 100;
const cx = (q) => 90 + q * 60, cy = (c) => 310 - c * 3;
const AFCf = (i) => FCc / QS[i], AVCf = (i) => VCS[i] / QS[i], ATCf = (i) => AFCf(i) + AVCf(i);
function costAxes() { return SV.line(cx(0), cy(0), cx(0), cy(80)) + SV.line(cx(0), cy(0), cx(11), cy(0)) + SV.text(cx(0) + 8, 14, "Cost per unit ($)", "sm") + SV.text(cx(11), cy(0) + 24, "Output (units)", "sm", { "text-anchor": "end" }); }
function costLine(fn, cls, lab, tcl) { let d = ""; QS.forEach((q, i) => d += (d ? "L" : "M") + cx(q).toFixed(1) + " " + cy(fn(i)).toFixed(1)); const li = QS.length - 1; return SV.path(d, cls) + SV.text(cx(QS[li]) + 6, cy(fn(li)) + 4, lab, "lbl bd " + tcl); }
function costDraw(show, sel) {
  let o = costAxes();
  if (show >= 1) o += costLine(AFCf, "c3", "AFC", "t3");
  if (show >= 2) o += costLine(AVCf, "c2", "AVC", "t2");
  if (show >= 3) o += costLine(ATCf, "c1", "ATC", "t1");
  if (sel !== undefined && sel >= 0) { const q = QS[sel]; o += SV.line(cx(q), cy(0), cx(q), cy(ATCf(sel)), "gr") + SV.circle(cx(q), cy(ATCf(sel)), 6, "dot2") + SV.circle(cx(q), cy(AVCf(sel)), 5, "dot1") + SV.circle(cx(q), cy(AFCf(sel)), 5, "dot3") + SV.text(cx(q), cy(0) + 18, q, "sm bd", { "text-anchor": "middle" }); }
  return o;
}
Lib.stepper($("#st0"), { w: 760, h: (380), label: "Average cost curves", base: { show: 0 }, draw: (s) => costDraw(s.show), steps: [
  { cap: "Output on the horizontal axis; cost per unit on the vertical axis.", s: { show: 0 } },
  { cap: "<b>AFC</b> always falls: fixed cost is spread over more units.", s: { show: 1 } },
  { cap: "<b>AVC</b> falls, then rises as diminishing returns set in: U-shaped.", s: { show: 2 } },
  { cap: "<b>ATC = AFC + AVC</b> is U-shaped. Its lowest point is the most efficient output.", s: { show: 3 } },
]  });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "From table to diagram", base: { n: 0 }, draw: mkChain(["Find FC and VC at each output", "Add to get TC", "Divide FC, VC and TC by output for AFC, AVC and ATC", "Plot each against output", "Join the points to draw the cost curves"], "--accent"), steps: chainSteps(["Find FC and VC at each output", "Add to get TC", "Divide FC, VC and TC by output for AFC, AVC and ATC", "Plot each against output", "Join the points to draw the cost curves"]) });
function labA() {
  const ids = ["a0"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const i = QS.indexOf(v[0]), tc = FCc + VCS[i], mn = ATCf(QS.indexOf(6)); return { r: ['$' + tc, '$' + ATCf(i).toFixed(1), '$' + AFCf(i).toFixed(1) + ' / $' + AVCf(i).toFixed(1)], t: 'At ' + v[0] + ' units: FC $' + FCc + ', VC $' + VCS[i] + ', TC $' + tc + '. AFC = ' + FCc + ' ÷ ' + v[0] + ' = $' + AFCf(i).toFixed(1) + '; AVC = ' + VCS[i] + ' ÷ ' + v[0] + ' = $' + AVCf(i).toFixed(1) + '; ATC = $' + ATCf(i).toFixed(1) + '. ' + (v[0] < 6 ? 'ATC is still falling: economies of scale.' : v[0] <= 7 ? 'This is near the lowest ATC.' : 'ATC is rising: diseconomies of scale.'), svg: costDraw(3, i) };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Output (units, 2 to 10)", min: 2, max: 10, step: 1, value: 6, fmt: (v) => v, onInput: labA });
const L2 = [{"n": "AFC", "a": "Falls all the way", "b": "Fixed cost spread over more units."}, {"n": "AVC", "a": "U-shaped", "b": "Specialisation, then diminishing returns."}, {"n": "ATC", "a": "U-shaped", "b": "ATC = AFC + AVC."}, {"n": "Gap between ATC and AVC", "a": "Shrinks as output rises", "b": "It equals AFC."}, {"n": "Lowest point of ATC", "a": "Minimum efficient scale", "b": "Lowest cost per unit."}, {"n": "Beyond the minimum", "a": "ATC rises", "b": "Diseconomies of scale."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Shape</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Does each cost <b>rise</b>, <b>fall</b> or have a <b>U shape</b> as output rises?", buckets: [{"label": "Falls"}, {"label": "U-shaped"}, {"label": "Rises"}], items: [{"text": "Average fixed cost", "b": 0}, {"text": "Average total cost", "b": 1}, {"text": "Average variable cost", "b": 1}, {"text": "Total cost", "b": 2}, {"text": "Total variable cost", "b": 2}, {"text": "Fixed cost per unit", "b": 0}], done: "Shapes of cost curves." });
Lib.classify($("#cl2"), { prompt: "Is each calculation <b>correct</b> or <b>incorrect</b> for FC $100, VC $50, output 10?", buckets: [{"label": "Correct"}, {"label": "Incorrect"}], items: [{"text": "TC = $150", "b": 0}, {"text": "AFC = $10", "b": 0}, {"text": "AVC = $5", "b": 0}, {"text": "ATC = $15", "b": 0}, {"text": "ATC = $5", "b": 1}, {"text": "AFC = $100", "b": 1}], done: "Check each formula." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["AFC curve", "Always falls as output rises"], ["AVC curve", "U-shaped"], ["ATC curve", "U-shaped; AFC + AVC"], ["Minimum efficient scale", "Output with the lowest ATC"], ["Diminishing returns", "Extra output costs more per unit"], ["Economies of scale", "Falling unit cost as output rises"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why ATC is U-shaped</b>.", items: ["Output starts low", "AFC falls quickly and AVC falls: ATC falls", "Output reaches its efficient level: ATC is lowest", "Diminishing returns push AVC up", "ATC rises: a U shape"], done: "AFC + AVC." });
Lib.calc($("#c1"), { qs: [
  { q: "At output 6, VC is $126 and FC is $100. What is ATC (1 decimal place, $)?", a: 37.7, sol: "226 ÷ 6 = <b>$37.7</b>." },
  { q: "At output 4, VC is $80. What is AVC ($)?", a: 20, sol: "80 ÷ 4 = <b>$20</b>." },
  { q: "At output 10, TC is $430. What is ATC ($)?", a: 43, sol: "430 ÷ 10 = <b>$43</b>." },
  { q: "AFC is $12.5 and AVC is $25.5. What is ATC ($)?", a: 38, sol: "12.5 + 25.5 = <b>$38</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The AFC curve:", opts: ["Rises", "Falls throughout", "Is U-shaped", "Is flat"], a: 1, why: "Spread over more units." },
  { q: "ATC is:", opts: ["Downward-sloping only", "U-shaped", "Upward-sloping only", "Vertical"], a: 1, why: "Falls then rises." },
  { q: "The gap between ATC and AVC is:", opts: ["VC", "AFC", "FC", "TC"], a: 1, why: "ATC − AVC = AFC." },
  { q: "ATC rises at high output because of:", opts: ["Economies of scale", "Diseconomies of scale", "Lower FC", "Subsidies"], a: 1, why: "Too big." },
  { q: "The lowest point of ATC is the:", opts: ["Maximum output", "Minimum efficient scale", "Break-even only", "Highest profit"], a: 1, why: "Lowest unit cost." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Average cost curves", "Curves showing AFC, AVC and ATC at each output."],
  ["Minimum efficient scale", "The output at which ATC is lowest."],
  ["Diminishing returns", "Each extra input adds less to output, raising marginal cost."],
  ["Economies of scale", "Falling unit cost with higher output."],
  ["Diseconomies of scale", "Rising unit cost with higher output."],
  ["U-shaped", "A curve that falls and then rises."],
  ["Rectangular hyperbola", "The shape of the AFC curve."],
  ["Marginal cost", "The cost of one more unit."],
  ["Efficiency", "Producing at the lowest unit cost."],
] });
labA(); 
