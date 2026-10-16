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

/* ---------- Watch 3: demand curve ---------- */
(function () {
  const PR = [6, 4, 3, 2], F1 = FR(50, 300, 300, 250, 60, 60), F2 = FR(430, 300, 290, 250, 36, 8);
  const qty = (p) => NORM.best(NORM.M, p, NORM.py).x, yv = NORM.best(NORM.M, 4, 2).y;
  function draw(s) {
    const d = s.d, n = Math.floor(d), fr = d - n; let o = frameAxes(F1, "Good X", "Good Y") + frameAxes(F2, "Quantity of X", "Price of X ($)");
    o += SV.text(50, 18, "Indifference curves and budget lines", "lbl bd") + SV.text(430, 18, "Demand curve for X", "lbl bd");
    [0, 2, 4, 6, 8].forEach((p) => { o += SV.text(F2.x0 - 6, F2.Y(p) + 4, p, "sm", { "text-anchor": "end" }); });
    PR.forEach((p, i) => {
      const v = i < n ? 1 : i === n ? fr : 0; if (v <= 0) return; const q = qty(p), U = NORM.u(q, yv);
      o += bline(F1, p, 2, 120, "c3", op(v)) + icLine(NORM, F1, U, "c1", op(v * 0.7)) + SV.circle(F1.X(q), F1.Y(yv), 6, "dot1", op(v));
      o += SV.circle(F2.X(q), F2.Y(p), 6, "dot1", op(v)) + SV.text(F2.X(q) + 10, F2.Y(p) - 8, `$${p}, ${Lib.fmtN(q, 0)}`, "sm bd t1", op(v));
    });
    if (n >= 2) { const pts = PR.slice(0, n).map((p) => [F2.X(qty(p)), F2.Y(p)]); o += SV.path(Lib.ptsPath(pts), "c1"); }
    if (n >= 4) o += SV.text(F2.X(33), F2.Y(1.2), "D", "lbl bd t1", {});
    return o;
  }
  Lib.stepper($("#stC"), { w: 760, h: 360, label: "Building the demand curve for X from budget line pivots", base: { d: 0 }, draw, tween: 800, dwell: 5200, steps: [
    { cap: "<b>Start.</b> Income $120, price of Y $2. We will change the price of X and note the quantity bought each time. Left: the diagram. Right: the demand curve.", s: { d: 0 } },
    { cap: `<b>Price $6.</b> The budget line touches an indifference curve at ${Lib.fmtN(qty(6), 0)} units of X. Plot (${Lib.fmtN(qty(6), 0)}, $6).`, s: { d: 1 } },
    { cap: `<b>Price $4.</b> The budget line <b>pivots outwards</b> around the Y-axis intercept. New tangency at ${Lib.fmtN(qty(4), 0)} units. Plot (${Lib.fmtN(qty(4), 0)}, $4).`, s: { d: 2 } },
    { cap: `<b>Price $3.</b> Pivots again: ${Lib.fmtN(qty(3), 0)} units. Plot (${Lib.fmtN(qty(3), 0)}, $3).`, s: { d: 3 } },
    { cap: `<b>Price $2.</b> ${Lib.fmtN(qty(2), 0)} units. <b>Joining the points gives the demand curve.</b> It slopes downward because for a normal good the substitution and income effects both raise quantity when the price falls.`, s: { d: 4 } },
  ] });
})();

/* ---------- Lab 1: equilibrium finder ---------- */
function lab1() {
  if (!$("#mm") || !$("#px1") || !$("#py1")) return;
  const M = +$("#mm").value, px = +$("#px1").value, py = +$("#py1").value, x = M / (2 * px), y = M / (2 * py), U = Math.sqrt(x * y), F = FR(50, 290, 340, 260, 80, 80);
  $("#r1").textContent = `${Lib.fmtN(x, 1)} X, ${Lib.fmtN(y, 1)} Y`; $("#r2").textContent = Lib.fmtN(y / x, 2); $("#r3").textContent = Lib.fmtN(px / py, 2);
  $("#rv").textContent = `The budget line meets the highest affordable indifference curve at a tangent. There the slope of the curve (the MRS = ${Lib.fmtN(y / x, 2)}) equals the slope of the budget line (Px ÷ Py = ${Lib.fmtN(px / py, 2)}). Spending: $${Lib.fmtN(px * x + py * y, 0)} = all of the income.`;
  $("#labA").innerHTML = frameAxes(F, "Good X", "Good Y") + icLine(NORM, F, U * 0.7, "c1", { opacity: 0.35 }) + icLine(NORM, F, U, "c1") + icLine(NORM, F, U * 1.3, "c1", { opacity: 0.35 }) + bline(F, px, py, M, "c3") + SV.circle(F.X(x), F.Y(y), 7, "dot2") + SV.text(F.X(x) + 12, F.Y(y) - 10, "equilibrium", "lbl bd t2");
}
Lib.slider($("#g1"), { id: "mm", label: "Income ($): ", min: 40, max: 160, step: 10, value: 120, fmt: (v) => v, onInput: lab1 });
Lib.slider($("#g2"), { id: "px1", label: "Price of X ($): ", min: 2, max: 8, step: 1, value: 4, fmt: (v) => v, onInput: lab1 });
Lib.slider($("#g3"), { id: "py1", label: "Price of Y ($): ", min: 2, max: 8, step: 1, value: 2, fmt: (v) => v, onInput: lab1 });

/* ---------- Lab 2: more income ---------- */
function labInc() {
  if (!$("#im")) return;
  const M = +$("#im").value, x = M / 8, y = M / 4, u = Math.sqrt(x * y), F = FR(50, 290, 340, 250, 80, 80);
  $("#i1").textContent = `${Lib.fmtN(x, 1)} X, ${Lib.fmtN(y, 1)} Y`; $("#i2").textContent = Lib.fmtN(u, 1); $("#i3").textContent = "2.00";
  $("#iv").textContent = `With income $${M} the consumer buys ${Lib.fmtN(x, 1)} X and ${Lib.fmtN(y, 1)} Y. Because prices have not changed, the slope stays at 2: the line shifts in parallel. Both goods rise with income, so both are normal goods here.`;
  let o = frameAxes(F, "Good X", "Good Y");
  [40, 80, 120, 160].forEach((m) => { const on = m === M; o += bline(F, 4, 2, m, on ? "c3" : "gr", on ? { "stroke-width": 3 } : { opacity: 0.35 }); });
  const path = []; for (let m = 40; m <= 160; m += 10) path.push([F.X(m / 8), F.Y(m / 4)]);
  o += SV.path(Lib.ptsPath(path), "c4", { "stroke-dasharray": "5 4", opacity: 0.8 }) + icLine(NORM, F, u, "c1") + SV.circle(F.X(x), F.Y(y), 7, "dot2") + SV.text(F.X(x) + 12, F.Y(y) - 10, "equilibrium", "lbl bd t2");
  $("#labR").innerHTML = o;
}
Lib.slider($("#g13"), { id: "im", label: "Income ($): ", min: 40, max: 160, step: 10, value: 80, fmt: (v) => v, onInput: labInc });

/* ---------- Practise ---------- */
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Consumer equilibrium", "The bundle on the highest indifference curve the budget line allows"],
  ["Tangent", "A line that touches a curve at one point without crossing it"],
  ["MRS = Px ÷ Py", "The condition at the consumer's equilibrium"],
  ["Price consumption curve", "The path of equilibria as the price of one good changes"],
  ["Individual demand curve", "Price against quantity bought at each equilibrium"],
  ["Income consumption curve", "The path of equilibria as income changes"],
], done: "Six words for equilibrium and demand." });
Lib.order($("#o1"), { prompt: "Put the derivation of a demand curve with indifference curves in order.", items: [
  "Draw an indifference map and a budget line, and mark the tangency as equilibrium A",
  "Lower the price of X so the budget line pivots outwards around the Y-axis intercept",
  "Find the new tangency on a higher indifference curve: equilibrium B",
  "Note the quantity of X bought at each price",
  "Plot each price against its quantity on a second diagram",
  "Join the points to give the individual demand curve, which slopes down for a normal good",
], done: "Repeat for several prices, then add across consumers for the market demand curve." });
Lib.calc($("#c1"), { qs: [
  { q: "The price of X falls from $4 to $3. What is the new maximum quantity of X (income $120)?", a: 40, sol: "120 ÷ 3 = <b>40</b>. The X-axis intercept moves out from 30 to 40." },
  { q: "At equilibrium Px is $6 and Py is $3. What is the MRS?", a: 2, hint: "At tangency, MRS = Px ÷ Py.", sol: "6 ÷ 3 = <b>2</b>." },
  { q: "Income is $120, Px = $4 and Py = $2. The consumer spends half of income on each good. How many units of X are bought?", a: 15, sol: "$60 ÷ $4 = <b>15</b>." },
  { q: "How many units of Y are bought?", a: 30, sol: "$60 ÷ $2 = <b>30</b>." },
  { q: "Using the same rule, the price of X falls to $2. How many units of X are now bought?", a: 30, sol: "$60 ÷ $2 = <b>30</b>. The demand curve gains a second point: (30, $2)." },
  { q: "Income rises from $120 to $160 with prices unchanged. How many units of X are bought (same half-and-half rule)?", a: 20, sol: "$80 ÷ $4 = <b>20</b>: a normal good." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The consumer is in equilibrium where:", opts: ["the budget line crosses an indifference curve", "the budget line is a tangent to the highest reachable indifference curve", "the indifference curve touches the axis", "income is zero"], a: 1, why: "Any crossing point lies on a lower curve than one the consumer could reach." },
  { q: "At the consumer's equilibrium, the MRS equals:", opts: ["Py ÷ Px", "Px ÷ Py", "income", "1"], a: 1, why: "The curve and the budget line have the same slope at a tangent." },
  { q: "A fall in the price of X will pivot the budget line:", opts: ["inwards around the X intercept", "outwards around the Y intercept", "outwards in parallel", "inwards in parallel"], a: 1, why: "The Y intercept (income ÷ Py) is unchanged; the X intercept moves out." },
  { q: "Joining the equilibria found at different prices of X gives:", opts: ["the budget line", "the indifference map", "the individual demand curve (via price and quantity)", "total utility"], a: 2, why: "Price against the quantity bought forms the demand curve." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Consumer equilibrium", "Tangency of the budget line with the highest reachable indifference curve: MRS = Px ÷ Py."],
  ["Price consumption curve", "The path of equilibria as the price of one good changes. Used to derive the demand curve."],
  ["Income consumption curve", "The path of equilibria as income changes, prices fixed."],
  ["Tangent", "A line touching a curve at one point."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Oct/Nov 2022 · 31 · Q6] The diagram shows two budget lines for a consumer of product X when its price changes, with two indifference curves and equilibria E1 and E2 (E2 is further to the right than E1). What is not a valid statement?", opts: ["Product X must be a Giffen good, since the consumer spends more on other goods after the price change.", "The consumer has greater satisfaction at E2 than at E1.", "The prices of other goods are assumed to be held constant when drawing the budget lines.", "The shift from the first budget line to the second represents a fall in the price of product X."], a: 0, why: "Spending more on other goods after a price fall does not make X a Giffen good: the quantity of X still rises. B, C and D are valid." },
] });
