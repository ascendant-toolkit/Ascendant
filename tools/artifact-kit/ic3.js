/* ---------- two preference models ----------
   NORM: U = sqrt(x*y) (normal goods). INF: U = y(1 - 0.02x) + 20 ln x (x is an inferior good at the incomes used). */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const FR = (x0, y0, w, h, xm, ym) => ({ x0, y0, w, h, xm, ym, X: (x) => x0 + (x / xm) * w, Y: (y) => y0 - (y / ym) * h });
const NORM = {
  M: 120, py: 2, px0: 4, xm: 60, ym: 60,
  u: (x, y) => Math.sqrt(x * y), icY: (U, x) => (U * U) / x,
  best: (M, px, py) => ({ x: M / (2 * px), y: M / (2 * py) }),
  comp: (U, px, py) => { const x = U * Math.sqrt(py / px), y = U * Math.sqrt(px / py); return { x, y, e: px * x + py * y }; },
};
const INF = {
  M: 60, py: 1, px0: 3, xm: 20, ym: 60,
  u: (x, y) => y * (1 - 0.02 * x) + 20 * Math.log(x), icY: (U, x) => (U - 20 * Math.log(x)) / (1 - 0.02 * x),
  best(M, px, py) { let bx = 0, bu = -1e9; const xmax = Math.min(M / px - 1e-6, 49.9); for (let i = 1; i <= 4000; i++) { const x = (xmax * i) / 4000, y = (M - px * x) / py, u = this.u(x, y); if (u > bu) { bu = u; bx = x; } } return { x: bx, y: (M - px * bx) / py }; },
  comp(U, px, py) { let b = { x: 0, y: 0, e: 1e9 }; for (let i = 1; i <= 4000; i++) { const x = (49 * i) / 4000, y = this.icY(U, x), y2 = this.icY(U, x + 0.01); if (!(y > 0) || !(y2 < y)) continue; const e = px * x + py * y; if (e < b.e) b = { x, y, e }; } return b; },
};
function decomp(m, px1) {
  const A = m.best(m.M, m.px0, m.py), U0 = m.u(A.x, A.y), C = m.comp(U0, px1, m.py), B = m.best(m.M, px1, m.py), U1 = m.u(B.x, B.y);
  return { A, B, C, U0, U1, SE: C.x - A.x, IE: B.x - C.x };
}
/* straight line  px*x + py*y = e, clipped to the frame */
function bline(F, px, py, e, cls, o) {
  let x1 = 0, y1 = e / py; if (y1 > F.ym) { y1 = F.ym; x1 = (e - py * y1) / px; }
  let x2 = e / px, y2 = 0; if (x2 > F.xm) { x2 = F.xm; y2 = (e - px * x2) / py; }
  return SV.line(F.X(x1), F.Y(y1), F.X(x2), F.Y(y2), cls, o);
}
function icLine(m, F, U, cls, o) {
  const pts = []; let prev = Infinity;
  for (let x = F.xm / 200; x <= F.xm; x += F.xm / 200) { const y = m.icY(U, x); if (!(y > 0) || y > F.ym * 1.02) { if (pts.length) break; continue; } if (y > prev) break; pts.push([F.X(x), F.Y(y)]); prev = y; }
  return pts.length > 1 ? SV.path(Lib.ptsPath(pts), cls, o) : "";
}
const frameAxes = (F, xl, yl) => SV.line(F.x0, F.y0, F.x0 + F.w + 10, F.y0) + SV.line(F.x0, F.y0, F.x0, F.y0 - F.h - 10) + SV.text(F.x0 + F.w + 10, F.y0 + 22, xl, "sm", { "text-anchor": "end" }) + SV.text(F.x0 + 6, F.y0 - F.h - 14, yl, "sm");
const dot = (F, p, cls, label, dx, dy, o) => SV.circle(F.X(p.x), F.Y(p.y), 6, cls, o) + SV.text(F.X(p.x) + dx, F.Y(p.y) + dy, label, "lbl bd", { "text-anchor": "middle", ...(o || {}) });

/* full price-effect diagram. s: flags 0..1 */
function drawDecomp(m, F, px1, s) {
  const d = decomp(m, px1); let o = frameAxes(F, "Good X", "Good Y");
  if (s.bl0 > 0) o += bline(F, m.px0, m.py, m.M, "gr", { "stroke-width": 2.5, ...op(s.bl0) });
  if (s.ic0 > 0) o += icLine(m, F, d.U0, "c1", op(s.ic0)) + SV.text(F.X(F.xm * 0.9), F.Y(m.icY(d.U0, F.xm * 0.9)) - 8, "IC1", "lbl bd t1", op(s.ic0));
  if (s.pa > 0) o += dot(F, d.A, "dot1", "A", -12, -10, op(s.pa));
  if (s.bl1 > 0) o += bline(F, px1, m.py, m.M, "c3", op(s.bl1));
  if (s.ic1 > 0) o += icLine(m, F, d.U1, "c4", op(s.ic1)) + SV.text(F.X(F.xm * 0.93), F.Y(m.icY(d.U1, F.xm * 0.93)) - 8, "IC2", "lbl bd t4", op(s.ic1));
  if (s.pb > 0) o += dot(F, d.B, "dot4", "B", 14, -10, op(s.pb));
  if (s.bc > 0) o += bline(F, px1, m.py, d.C.e, "c2", { "stroke-dasharray": "6 5", ...op(s.bc) }) + dot(F, d.C, "dot2", "C", 0, 22, op(s.bc));
  const yy = F.y0 + 36;
  if (s.se > 0) o += SV.line(F.X(d.A.x), yy, F.X(d.C.x), yy, "c3", { "stroke-width": 5, ...op(s.se) }) + SV.text((F.X(d.A.x) + F.X(d.C.x)) / 2, yy + 16, "SE", "lbl bd t3", { "text-anchor": "middle", ...op(s.se) });
  if (s.ie > 0) o += SV.line(F.X(d.C.x), yy + 22, F.X(d.B.x), yy + 22, "c2", { "stroke-width": 5, ...op(s.ie) }) + SV.text((F.X(d.C.x) + F.X(d.B.x)) / 2, yy + 38, "IE", "lbl bd t2", { "text-anchor": "middle", ...op(s.ie) });
  return o;
}
const sg = (v) => (v > 0.005 ? "+" : v < -0.005 ? "−" : "") + Lib.fmtN(Math.abs(v), 1);

/* ---------- Watch 1 and 2: decomposition steppers ---------- */
function decompStepper(sel, m, px1, lab, caps) {
  const F = FR(60, 300, 600, 260, m.xm, m.ym), d = decomp(m, px1);
  const flags = [{ bl0: 1, ic0: 1, pa: 1 }, { bl0: 1, ic0: 1, pa: 1, bl1: 1 }, { bl0: 1, ic0: 1, pa: 1, bl1: 1, ic1: 1, pb: 1 }, { bl0: 1, ic0: 1, pa: 1, bl1: 1, ic1: 1, pb: 1, bc: 1 }, { bl0: 1, ic0: 1, pa: 1, bl1: 1, ic1: 1, pb: 1, bc: 1, se: 1 }, { bl0: 1, ic0: 1, pa: 1, bl1: 1, ic1: 1, pb: 1, bc: 1, se: 1, ie: 1 }];
  Lib.stepper($(sel), { w: 740, h: 380, label: lab, base: { bl0: 0, ic0: 0, pa: 0, bl1: 0, ic1: 0, pb: 0, bc: 0, se: 0, ie: 0 }, draw: (s) => drawDecomp(m, FR(60, 300, 600, 260, m.xm, m.ym), px1, s), tween: 800, dwell: 5600, steps: caps(d).map((c, i) => ({ cap: c, s: flags[i] })) });
}
decompStepper("#stA", NORM, 2, "Price effect for a normal good split into substitution and income effects", (d) => [
  `<b>Equilibrium A.</b> Income $120, X costs $4, Y costs $2. The budget line (grey) touches the indifference curve IC1 at A: ${Lib.fmtN(d.A.x, 0)} units of X and ${Lib.fmtN(d.A.y, 0)} of Y.`,
  "<b>The price of X falls to $2.</b> The budget line <b>pivots outwards</b> around the Y-axis intercept. The consumer can now reach a higher curve.",
  `<b>New equilibrium B</b> on the higher curve IC2: ${Lib.fmtN(d.B.x, 0)} units of X. The total change in X is ${sg(d.B.x - d.A.x)} units. Now split it in two.`,
  "<b>The compensating budget line</b> (dashed). It is <b>parallel to the new budget line</b> (the new relative prices) but only just touches the <b>original</b> curve IC1, at C. This keeps real income at its old level.",
  `<b>Substitution effect, A to C.</b> At the new relative prices, X is cheaper, so the consumer moves along IC1 to ${Lib.fmtN(d.C.x, 1)} units: <b>${sg(d.SE)}</b>. Same satisfaction, more X.`,
  `<b>Income effect, C to B.</b> The price fall raises real income, so the consumer reaches IC2. X is a normal good, so ${sg(d.IE)} more units are bought: <b>${sg(d.IE)}</b>. Both effects point the same way, so the demand curve slopes downward.`,
]);
/* ---------- Lab 2 and 3: decomposition labs ---------- */
function decompLab(m, sliderId, prefix, svgId, verdictFn) {
  if (!$("#" + sliderId)) return;
  const px1 = +$("#" + sliderId).value, d = decomp(m, px1), tot = d.B.x - d.A.x;
  $("#" + prefix + "1").textContent = sg(d.SE); $("#" + prefix + "2").textContent = sg(d.IE); $("#" + prefix + "3").textContent = sg(tot);
  $("#" + (prefix === "s" ? "sv" : "tv")).textContent = verdictFn(d, px1, tot);
  $("#" + svgId).innerHTML = drawDecomp(m, FR(50, 270, 340, 240, m.xm, m.ym), px1, { bl0: 1, ic0: 1, pa: 1, bl1: 1, ic1: 1, pb: 1, bc: 1, se: 0, ie: 0 });
}
const vNorm = (d, p, t) => p === NORM.px0 ? "No price change: A, B and C are the same point." : p < NORM.px0 ? `Price falls to $${p}. SE ${sg(d.SE)} and IE ${sg(d.IE)} both raise quantity: a normal good, total ${sg(t)}.` : `Price rises to $${p}. SE ${sg(d.SE)} and IE ${sg(d.IE)} both cut quantity: total ${sg(t)}. Demand slopes downward.`;
const vInf = (d, p, t) => p === INF.px0 ? "No price change: A, B and C are the same point." : p < INF.px0 ? `Price falls to $${p}. SE ${sg(d.SE)} raises X, but IE ${sg(d.IE)} works against it (inferior good). The IE is smaller than the SE, so the total ${sg(t)} is still positive: not a Giffen good.` : `Price rises to $${p}. The SE cuts X by ${sg(d.SE)}, and the IE ${sg(d.IE)} partly offsets it. Total ${sg(t)}.`;
const l2 = () => decompLab(NORM, "np", "s", "labB", vNorm);
Lib.slider($("#g4"), { id: "np", label: "New price of X ($): ", min: 1.5, max: 8, step: 0.5, value: 2, fmt: (v) => v, onInput: l2 });

/* ---------- Practise ---------- */
Lib.order($("#o1"), { prompt: "Put the analysis of a fall in the price of X in order.", items: [
  "Draw the original budget line and indifference curve; mark equilibrium A at the tangency",
  "The price of X falls: the budget line pivots outwards around the Y-axis intercept",
  "Mark the new equilibrium B on a higher indifference curve",
  "Draw a dashed line parallel to the new budget line, touching the original curve at C",
  "A to C is the substitution effect; C to B is the income effect",
  "Say whether the good is normal, inferior or Giffen from the sign and size of the income effect",
], done: "This order works for every price-effect question." });
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Price effect", "The total change in quantity from a price change: SE plus IE"],
  ["Substitution effect", "The change in quantity from the change in relative prices, along the same indifference curve"],
  ["Income effect", "The change in quantity from the change in real income caused by the price change"],
  ["Compensating budget line", "A line parallel to the new budget line that touches the original curve"],
  ["Real income", "What income can buy, after allowing for prices"],
  ["Normal good", "A good for which quantity demanded rises when income rises"],
], done: "Six words for the price effect." });
Lib.calc($("#c1"), { qs: [
  { q: "A fall in the price of X moves the consumer from 15 units to 30 units. What is the price effect (units)?", a: 15, sol: "30 − 15 = <b>+15</b>." },
  { q: "The compensated point C is at 21.2 units. What is the substitution effect (units, 1 decimal place)?", a: 6.2, tol: 0.1, sol: "21.2 − 15 = <b>+6.2</b>." },
  { q: "What is the income effect (units, 1 decimal place)?", a: 8.8, tol: 0.1, sol: "30 − 21.2 = <b>+8.8</b>." },
  { q: "A rise in the price of a normal good has a substitution effect of −4 units. The income effect is −3 units. What is the price effect?", a: -7, sol: "−4 − 3 = <b>−7</b>: both effects cut quantity." },
  { q: "The price of X falls from $4 to $3 and income is $120. By how much does the X-axis intercept of the budget line rise (units)?", a: 10, sol: "120 ÷ 3 = 40; before 120 ÷ 4 = 30. A rise of <b>10</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The substitution effect of a fall in the price of X is:", opts: ["a rise in the quantity of X", "a fall in the quantity of X", "sometimes up, sometimes down", "zero for normal goods"], a: 0, why: "The relatively cheaper good is substituted for the dearer one, so the SE is always in this direction." },
  { q: "The income effect of a price fall for a normal good:", opts: ["raises the quantity bought", "lowers the quantity bought", "is always zero", "is the same as the substitution effect"], a: 0, why: "Real income rises, and a normal good is bought more as income rises." },
  { q: "The compensating budget line is:", opts: ["parallel to the original budget line", "parallel to the new budget line and tangent to the original curve", "tangent to the new curve and parallel to the original line", "vertical"], a: 1, why: "It keeps satisfaction at the original level at the new relative prices." },
  { q: "The substitution effect of a price rise for X:", opts: ["raises the quantity of X", "lowers the quantity of X", "depends on the good", "is zero"], a: 1, why: "X becomes relatively dearer, so the consumer moves away from it along the same curve." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Price effect", "The total change in quantity from a price change: substitution effect plus income effect."],
  ["Substitution effect", "Change in quantity from the change in relative prices, along the same indifference curve."],
  ["Income effect", "Change in quantity from the change in real income caused by the price change."],
  ["Compensating budget line", "A line parallel to the new budget line that touches the original indifference curve. Used to find the SE."],
  ["Real income", "Income measured by what it can buy at current prices."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Oct/Nov 2022 · 32 · Q6] When the price of a good increases, which statement is correct according to the analysis that uses budget lines and indifference curves?", opts: ["The income and substitution effects of the price increase will work in opposite directions in the case of a Giffen good.", "The income effect of the price increase will result in reduced consumption for all goods.", "The new equilibrium position will be where the new budget line meets the original indifference curve.", "The price rise will be represented by a parallel shift inwards of the original budget line."], a: 0, why: "B is wrong for inferior goods, C confuses the new equilibrium with the compensating line, and D describes an income fall; a price rise pivots the line." },
] });
