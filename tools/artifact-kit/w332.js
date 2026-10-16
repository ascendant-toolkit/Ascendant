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

const X = (q) => 90 + q * 4.6, Y = (p) => 310 - p * 2.7;
function axes() { return SV.line(X(0), Y(0), X(0), Y(108)) + SV.line(X(0), Y(0), X(135), Y(0)) + SV.text(X(0) + 8, 14, "Price ($)", "sm") + SV.text(X(135), Y(0) + 24, "Quantity", "sm", { "text-anchor": "end" }); }
function dCurve(d, cls, lab, t) { const a = d >= 0 ? [d, 100] : [0, 100 + d], b = [100 + d, 0]; return SV.line(X(a[0]), Y(a[1]), X(b[0]), Y(b[1]), cls || "c1") + SV.text(X(b[0]) + 6, Y(b[1]) - 8, lab || "D", "lbl bd " + (t || "t1")); }
function sCurve(s, cls, lab, t) { const a = s >= 0 ? [s, 0] : [0, -s], b = [100 + s, 100]; return SV.line(X(a[0]), Y(a[1]), X(b[0]), Y(b[1]), cls || "c2") + SV.text(X(b[0]) + 6, Y(b[1]) + 4, lab || "S", "lbl bd " + (t || "t2")); }
function eq(d, s) { const q = (100 + d + s) / 2, p = q - s; return [q, p]; }
function dsDrop(q, p) { return SV.line(X(0), Y(p), X(q), Y(p), "gr") + SV.line(X(q), Y(p), X(q), Y(0), "gr"); }
function qD(p, d) { return Math.max(0, 100 + d - p); }
function qS(p, s) { return Math.max(0, p + s); }

function axes() { return SV.line(X(0), Y(0), X(0), Y(108)) + SV.line(X(0), Y(0), X(135), Y(0)) + SV.text(X(0) + 8, 14, "Wage rate ($ per hour)", "sm") + SV.text(X(135), Y(0) + 24, "Quantity of labour (workers)", "sm", { "text-anchor": "end" }); }
function lmDraw(d, s, nmw) {
  const [q0, p0] = eq(0, 0), [q, p] = eq(d, s); let o = axes() + dCurve(0, d !== 0 ? "c3" : "c1", "D", d !== 0 ? "t3" : "t1") + sCurve(0, s !== 0 ? "c3" : "c2", "S", s !== 0 ? "t3" : "t2");
  if (d !== 0) o += dCurve(d, d > 0 ? "c1" : "c4", d > 0 ? "D₁" : "D₂", d > 0 ? "t1" : "t4");
  if (s !== 0) o += sCurve(s, s > 0 ? "c2" : "c4", s > 0 ? "S₁" : "S₂", s > 0 ? "t2" : "t4");
  o += dsDrop(q, p) + SV.circle(X(q), Y(p), 7, "dot2") + SV.text(X(0) - 8, Y(p), "W", "sm bd", { "text-anchor": "end" }) + SV.text(X(q), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" });
  if (nmw && nmw > p) { const qd = qD(nmw, d), qs = qS(nmw, s); o += SV.line(X(0), Y(nmw), X(Math.max(qd, qs) + 8), Y(nmw), "c4") + SV.circle(X(qd), Y(nmw), 6, "dot3") + SV.circle(X(qs), Y(nmw), 6, "dot4") + SV.text(X(0) - 8, Y(nmw), "NMW", "sm bd t4", { "text-anchor": "end" }) + SV.text(X((qd + qs) / 2), Y(nmw) - 12, "Unemployment " + Math.round(qs - qd), "lbl bd t4", { "text-anchor": "middle" }); }
  return o;
}
Lib.stepper($("#st0"), { w: 760, h: (380), label: "Labour market equilibrium", base: { d: 0, s: 0, m: 0 }, draw: (s) => lmDraw(s.d, s.s, s.m), steps: [
  { cap: "Demand for labour D slopes down; supply S slopes up. They meet at the equilibrium wage W and employment Q.", s: { d: 0, s: 0, m: 0 } },
  { cap: "Demand for the firm's product rises, so demand for labour <b>increases</b>: D shifts right. The wage and employment both <b>rise</b>.", s: { d: 30, s: 0, m: 0 } },
  { cap: "More people enter the labour market (e.g. immigration): supply <b>increases</b>. The wage <b>falls</b> and employment <b>rises</b>.", s: { d: 0, s: 30, m: 0 } },
]  });
Lib.stepper($("#st1"), { w: 760, h: (380), label: "A national minimum wage", base: { d: 0, s: 0, m: 0 }, draw: (s) => lmDraw(s.d, s.s, s.m), steps: [
  { cap: "Labour market equilibrium at wage W and employment Q.", s: { d: 0, s: 0, m: 0 } },
  { cap: "A <b>minimum wage above equilibrium</b>: more workers want jobs than firms want to hire. A <b>surplus of labour</b> (unemployment) appears.", s: { d: 0, s: 0, m: 68 } },
  { cap: "Workers who keep jobs earn more, but fewer jobs are available. A minimum wage <b>below</b> equilibrium would have no effect.", s: { d: 0, s: 0, m: 68 } },
]  });
Lib.stepper($("#st2"), { w: 760, h: 380, label: "Union bargaining power", base: { n: 0 }, draw: mkChain(["A union has many members and rare skills", "Workers can threaten strike action", "The firm faces high costs if production stops", "The firm agrees higher pay", "Wages rise (employment may fall if demand for labour is elastic)"], "--warn"), steps: chainSteps(["A union has many members and rare skills", "Workers can threaten strike action", "The firm faces high costs if production stops", "The firm agrees higher pay", "Wages rise (employment may fall if demand for labour is elastic)"]) });
function labA() {
  const ids = ["a0","a1","a2"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const e = eq(v[0], v[1]), q = e[0], p = e[1], nm = v[2]; let u = 0, emp = q, w = p; if (nm > p) { const qd = qD(nm, v[0]), qs = qS(nm, v[1]); emp = qd; u = Math.max(0, qs - qd); w = nm; } return { r: ['$' + w.toFixed(0), emp.toFixed(0), u.toFixed(0)], t: 'Equilibrium wage is $' + p.toFixed(0) + ' with employment ' + q.toFixed(0) + '. ' + (nm > p ? 'The minimum wage of $' + nm + ' is above equilibrium: firms hire ' + emp.toFixed(0) + ' workers but ' + (emp + u).toFixed(0) + ' want jobs, so unemployment is ' + u.toFixed(0) + '.' : nm > 0 ? 'The minimum wage of $' + nm + ' is below equilibrium, so it has no effect.' : 'No minimum wage.'), svg: lmDraw(v[0], v[1], nm) };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Shift in demand for labour", min: -30, max: 30, step: 5, value: 0, fmt: (v) => (v > 0 ? '+' : '') + v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Shift in supply of labour", min: -30, max: 30, step: 5, value: 0, fmt: (v) => (v > 0 ? '+' : '') + v, onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Minimum wage ($; 0 = none)", min: 0, max: 90, step: 5, value: 0, fmt: (v) => v ? '$' + v : 'none', onInput: labA });
const L2 = [{"n": "Product demand rises", "a": "Demand for labour shifts right", "b": "Wage and employment rise."}, {"n": "Robots replace workers", "a": "Demand for labour shifts left", "b": "Wage and employment fall."}, {"n": "Immigration rises", "a": "Supply of labour shifts right", "b": "Wage falls, employment rises."}, {"n": "Many workers retire", "a": "Supply of labour shifts left", "b": "Wage rises, employment falls."}, {"n": "A minimum wage above equilibrium", "a": "Wage floor", "b": "Unemployment appears."}, {"n": "A strong union", "a": "Higher bargaining power", "b": "Higher wages."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Curve and effect</th><th>Wage and employment</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Does each shift <b>demand for labour</b> or <b>supply of labour</b>?", buckets: [{"label": "Demand for labour"}, {"label": "Supply of labour"}], items: [{"text": "Product demand rises", "b": 0}, {"text": "Productivity of workers rises", "b": 0}, {"text": "Robots replace some jobs", "b": 0}, {"text": "Immigration increases", "b": 1}, {"text": "More women enter the workforce", "b": 1}, {"text": "Retirement age rises", "b": 1}], done: "Firms vs workers." });
Lib.classify($("#cl2"), { prompt: "Is each <b>advantage</b> or <b>disadvantage</b> of a minimum wage?", buckets: [{"label": "Advantage"}, {"label": "Disadvantage"}], items: [{"text": "Reduces poverty", "b": 0}, {"text": "Raises incentive to work", "b": 0}, {"text": "Protects workers from exploitation", "b": 0}, {"text": "May cause unemployment", "b": 1}, {"text": "Raises firms' costs", "b": 1}, {"text": "May raise prices", "b": 1}], done: "Weigh both." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Demand for labour", "Firms' willingness to hire at each wage"], ["Supply of labour", "Workers' willingness to work at each wage"], ["Trade union", "Workers' group bargaining for pay and conditions"], ["Collective bargaining", "Negotiating as a group"], ["National minimum wage", "A legal floor on pay"], ["Equilibrium wage", "Where labour demand equals labour supply"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a minimum wage above equilibrium causes unemployment</b>.", items: ["The government sets a minimum wage above equilibrium", "Firms' costs rise", "Firms hire fewer workers", "More people want to work at the higher wage", "A surplus of labour: unemployment"], done: "A minimum price causes a surplus." });
Lib.calc($("#c1"), { qs: [
  { q: "The equilibrium wage is $50. A minimum wage of $68 leaves firms demanding 32 workers while 68 want jobs. How many are unemployed?", a: 36, sol: "68 − 32 = <b>36</b>." },
  { q: "A union wins a 4% pay rise for a $25,000 salary. What is the rise ($)?", a: 1000, sol: "4% × 25,000 = <b>$1,000</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An increase in demand for labour causes the wage to:", opts: ["Fall", "Rise", "Stay the same", "Be zero"], a: 1, why: "More hiring." },
  { q: "An increase in supply of labour causes the wage to:", opts: ["Rise", "Fall", "Stay the same", "Double"], a: 1, why: "More workers." },
  { q: "A minimum wage above equilibrium causes:", opts: ["Labour shortage", "Unemployment", "No effect", "Lower prices"], a: 1, why: "A surplus of labour." },
  { q: "A union's bargaining power is higher when:", opts: ["Few members", "Workers are easy to replace", "Workers have rare skills", "Unemployment is high"], a: 2, why: "Hard to replace." },
  { q: "The labour demand curve slopes:", opts: ["Down", "Up", "Vertically", "Horizontally"], a: 0, why: "Lower wage, more hired." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Demand for labour", "How many workers firms want to hire at each wage."],
  ["Supply of labour", "How many workers are willing to work at each wage."],
  ["Equilibrium wage", "The wage where labour demand equals supply."],
  ["Trade union", "An organisation of workers bargaining for better pay."],
  ["Collective bargaining", "Negotiating wages as a group."],
  ["National minimum wage", "A legal minimum rate of pay."],
  ["Productivity", "Output per worker."],
  ["Immigration", "People moving in to work."],
  ["Wage floor", "A minimum price in the labour market."],
] });
labA(); 
