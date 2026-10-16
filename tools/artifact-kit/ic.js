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

/* ---------- Learn: static picture (normal good) ---------- */
(function () {
  const F = FR(60, 330, 620, 280, 60, 60);
  $("#pic1").innerHTML = `<svg viewBox="0 0 760 390" role="img" aria-label="Indifference curve tangent to a budget line, with the equilibrium point and the next higher indifference curve out of reach">${drawDecomp(NORM, F, NORM.px0, { bl0: 1, ic0: 1, pa: 1 })}
    ${icLine(NORM, F, 28, "c4", { opacity: 0.7 })}${icLine(NORM, F, 14, "c1", { opacity: 0.35 })}
    ${SV.text(F.X(22), F.Y(8), "Budget line", "lbl bd", { "text-anchor": "middle" })}${SV.text(F.X(22) + 40, F.Y(18) - 10, "Tangent: MRS = Px ÷ Py", "lbl bd t1", {})}
    ${SV.text(F.X(33), F.Y(41), "Higher curve: more satisfaction, but out of reach", "sm", { "text-anchor": "start" })+SV.text(F.X(2), F.Y(13), "Lower curve: affordable, but not the best", "sm", { "text-anchor": "start" })}</svg>`;
})();

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
decompStepper("#stB", INF, 1.5, "Price effect for an inferior good split into substitution and income effects", (d) => [
  `<b>Equilibrium A.</b> Income $60, Y costs $1, X costs $3. The consumer buys ${Lib.fmtN(d.A.x, 1)} units of X and ${Lib.fmtN(d.A.y, 0)} of Y.`,
  "<b>The price of X falls to $1.50.</b> The budget line pivots outwards around the Y-axis intercept.",
  `<b>New equilibrium B</b> on a higher curve: ${Lib.fmtN(d.B.x, 1)} units of X. The total change is ${sg(d.B.x - d.A.x)}.`,
  "<b>The compensating budget line</b> (dashed): parallel to the new budget line and touching the original curve IC1 at C.",
  `<b>Substitution effect, A to C:</b> the consumer moves along IC1 towards the cheaper good: <b>${sg(d.SE)}</b> units of X.`,
  `<b>Income effect, C to B:</b> the consumer is richer in real terms and buys <b>less</b> X, <b>${sg(d.IE)}</b>, because X is inferior. The IE is <b>smaller</b> than the SE, so the net change is still <b>${sg(d.B.x - d.A.x)}</b>: the demand curve still slopes downward. If the IE were bigger, the good would be Giffen.`,
]);

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
const l2 = () => decompLab(NORM, "np", "s", "labB", vNorm), l3 = () => decompLab(INF, "ip", "t", "labC", vInf);
Lib.slider($("#g4"), { id: "np", label: "New price of X ($): ", min: 1.5, max: 8, step: 0.5, value: 2, fmt: (v) => v, onInput: l2 });
Lib.slider($("#g5"), { id: "ip", label: "New price of X ($): ", min: 1, max: 5, step: 0.1, value: 1.5, fmt: (v) => Lib.fmtN(v, 1), onInput: l3 });

/* ---------- Lab 4: normal, inferior or Giffen ---------- */
function lab4() {
  if (!$("#se1") || !$("#ie1")) return;
  const se = +$("#se1").value, ie = +$("#ie1").value, net = se + ie, cx = 240, k = 6.5;
  $("#e1").textContent = sg(se); $("#e2").textContent = sg(ie); $("#e3").textContent = sg(net);
  $("#ev").textContent = ie >= 0 ? "Normal good: both effects raise the quantity of X when its price falls. The demand curve slopes downward."
    : net > 0 ? "Inferior good, not Giffen: the income effect works against the substitution effect but is smaller. Quantity still rises. Demand slopes downward."
    : net < 0 ? "Giffen good: the negative income effect is larger than the substitution effect, so quantity falls when the price falls. Demand slopes upward."
    : "Borderline: the effects cancel exactly.";
  const bar = (y, v, cls, name) => SV.rect(Math.min(cx, cx + v * k), y, Math.abs(v) * k, 38, cls) + SV.text(cx + (v >= 0 ? -8 : 8), y + 24, name, "lbl bd", { "text-anchor": v >= 0 ? "end" : "start" }) + SV.text(cx + v * k + (v >= 0 ? 8 : -8), y + 24, sg(v), "lbl bd", { "text-anchor": v >= 0 ? "start" : "end" });
  $("#labD").innerHTML = SV.line(cx, 20, cx, 250) + bar(40, se, "f3", "SE") + bar(105, ie, "f2", "IE") + bar(180, net, net < 0 ? "f2" : "f1", "Net") + SV.text(cx, 282, "Change in quantity of X (units) when the price falls", "sm", { "text-anchor": "middle" });
}
Lib.slider($("#g6"), { id: "se1", label: "Substitution effect (units of X): ", min: 0, max: 20, step: 1, value: 12, fmt: (v) => "+" + v, onInput: lab4 });
Lib.slider($("#g7"), { id: "ie1", label: "Income effect (units of X): ", min: -30, max: 15, step: 1, value: 5, fmt: (v) => (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v), onInput: lab4 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "How does the budget line change?",
  buckets: [{ label: "Parallel shift" }, { label: "Pivots (slope changes)" }, { label: "No change" }],
  items: [
    { text: "Income rises", b: 0 }, { text: "Income falls", b: 0 }, { text: "Government gives a cash grant", b: 0 },
    { text: "Price of X falls, Y unchanged", b: 1 }, { text: "A sales tax on X", b: 1 }, { text: "A subsidy on Y", b: 1 }, { text: "Price of Y rises", b: 1 },
    { text: "The consumer's tastes change", b: 2 }, { text: "The consumer prefers X to Y more strongly", b: 2 },
  ], done: "The budget line depends on income and prices only, not on preferences.",
});
Lib.classify($("#cl2"), {
  prompt: "Match each description to a type of good (price fall).",
  buckets: [{ label: "Normal" }, { label: "Inferior (not Giffen)" }, { label: "Giffen" }],
  items: [
    { text: "SE +10, IE +4", b: 0 }, { text: "Both effects raise quantity", b: 0 }, { text: "Demand rises a lot when price falls", b: 0 },
    { text: "SE +12, IE −4", b: 1 }, { text: "IE negative but smaller than the SE", b: 1 }, { text: "Quantity rises, but by less than for a normal good", b: 1 },
    { text: "SE +6, IE −10", b: 2 }, { text: "IE negative and larger than the SE", b: 2 }, { text: "Demand curve slopes upward", b: 2 },
  ], done: "The sign and size of the income effect decide the type.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Indifference curve", "All combinations of two goods giving the same satisfaction"],
  ["Budget line", "All combinations of two goods the consumer can afford"],
  ["Marginal rate of substitution", "The rate at which a consumer will swap one good for another, the slope of the indifference curve"],
  ["Consumer equilibrium", "Where the budget line is tangent to the highest reachable indifference curve"],
  ["Substitution effect", "The change in quantity from relative prices changing, keeping satisfaction constant"],
  ["Income effect", "The change in quantity from the change in real income caused by a price change"],
  ["Inferior good", "A good whose demand falls when income rises (negative income effect)"],
  ["Giffen good", "An inferior good whose negative income effect outweighs the substitution effect"],
], done: "Know these eight and you can build any diagram." });
Lib.order($("#o1"), { prompt: "Put the analysis of a fall in the price of X in order.", items: [
  "Draw the original budget line and indifference curve; mark equilibrium A at the tangency",
  "The price of X falls: the budget line pivots outwards around the Y-axis intercept",
  "Mark the new equilibrium B on a higher indifference curve",
  "Draw a dashed line parallel to the new budget line, touching the original curve at C",
  "A to C is the substitution effect; C to B is the income effect",
  "Say whether the good is normal, inferior or Giffen from the sign and size of the income effect",
], done: "This order works for every price-effect question." });
Lib.calc($("#c1"), { qs: [
  { q: "Income is $120, the price of X is $4 and the price of Y is $2. How many units of X could be bought if all income is spent on X?", a: 30, sol: "120 ÷ 4 = <b>30</b>." },
  { q: "Same income and prices. How many units of Y if all income is spent on Y?", a: 60, sol: "120 ÷ 2 = <b>60</b>." },
  { q: "What is the slope of that budget line (Px ÷ Py)?", a: 2, sol: "4 ÷ 2 = <b>2</b>: for each extra unit of X, give up 2 units of Y." },
  { q: "The price of X falls from $4 to $3. What is the new maximum quantity of X (income $120)?", a: 40, sol: "120 ÷ 3 = <b>40</b>. The X-axis intercept moves out from 30 to 40." },
  { q: "A fall in the price of X has a substitution effect of +14 units and an income effect of −6 units. What is the net change in X?", a: 8, sol: "14 − 6 = <b>+8</b> units. Inferior, but not Giffen." },
  { q: "SE is +5 and IE is −9. What is the net change in X?", a: -4, sol: "5 − 9 = <b>−4</b>. Quantity falls when the price falls: a Giffen good." },
  { q: "At equilibrium Px is $6 and Py is $3. What is the MRS?", a: 2, hint: "At tangency, MRS = Px ÷ Py.", sol: "6 ÷ 3 = <b>2</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A rise in income, with prices unchanged, causes the budget line to:", opts: ["pivot inwards", "pivot outwards", "shift outwards in parallel", "become flatter"], a: 2, why: "The slope (Px ÷ Py) is unchanged, so the line shifts in parallel." },
  { q: "The consumer is in equilibrium where:", opts: ["the budget line crosses an indifference curve", "the budget line is a tangent to the highest reachable indifference curve", "the indifference curve touches the axis", "income is zero"], a: 1, why: "Any crossing point lies on a lower curve than one the consumer could reach." },
  { q: "Indifference curves are convex to the origin because of:", opts: ["diminishing marginal rate of substitution", "rising prices", "falling income", "economies of scale"], a: 0, why: "The more X you have, the less Y you will give up to get another unit of X." },
  { q: "The substitution effect of a fall in the price of X is:", opts: ["a rise in the quantity of X", "a fall in the quantity of X", "sometimes up, sometimes down", "zero for normal goods"], a: 0, why: "The relatively cheaper good is substituted for the dearer one, so the SE is always in this direction." },
  { q: "For an inferior good (not Giffen), a price fall causes:", opts: ["quantity to fall", "quantity to rise by more than for a normal good", "quantity to rise by less than for a normal good", "no change"], a: 2, why: "The negative income effect offsets part of the positive substitution effect." },
  { q: "Which condition makes a good a Giffen good?", opts: ["Positive income effect larger than the SE", "Negative income effect larger than the SE", "Zero income effect", "Negative substitution effect"], a: 1, why: "Only then does quantity fall when the price falls, giving an upward sloping demand curve." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Indifference curve", "A curve joining all combinations of two goods that give the same satisfaction."],
  ["Indifference map", "A set of indifference curves; further from the origin means higher satisfaction."],
  ["Marginal rate of substitution (MRS)", "The amount of one good the consumer will give up for one more unit of the other. The slope of the indifference curve."],
  ["Diminishing MRS", "Why indifference curves are convex to the origin."],
  ["Budget line", "All combinations of two goods affordable with a given income and prices."],
  ["Slope of the budget line", "Px ÷ Py."],
  ["Consumer equilibrium", "Tangency of the budget line with the highest reachable indifference curve: MRS = Px ÷ Py."],
  ["Price effect", "The total change in quantity from a price change: substitution effect plus income effect."],
  ["Substitution effect", "Change in quantity from the change in relative prices, along the same indifference curve."],
  ["Income effect", "Change in quantity from the change in real income caused by the price change."],
  ["Compensating budget line", "A line parallel to the new budget line that touches the original indifference curve. Used to find the SE."],
  ["Normal good", "Positive income effect: demand rises with income. Both effects raise quantity when price falls."],
  ["Inferior good", "Negative income effect. Demand still usually slopes downward."],
  ["Giffen good", "Inferior good whose negative income effect exceeds the SE; the demand curve slopes upward."],
  ["Price consumption curve", "The path of equilibria as the price of one good changes. Used to derive the demand curve."],
] });

/* ---------- Past paper MCQ (text) ---------- */
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2024 · 32 · Q2] What does an indifference curve show?", opts: ["the amount of two products achievable with given income and prices", "the different combinations of two goods that give a consumer equal utility", "the income available to buy the two goods", "the rate at which marginal utility changes as consumption changes"], a: 1, why: "A is the budget line. B is the indifference curve." },
  { q: "[Feb/March 2025 · 32 · Q5] Which statement about the downward sloping demand curve of an inferior good is correct?", opts: ["Negative income effect and substitution effect move in opposite directions, leading to a steeper demand curve.", "Negative income effect and substitution effect move in the same direction, leading to a flatter demand curve.", "Positive income effect and substitution effect move in opposite directions, leading to a steeper demand curve.", "Positive income effect and substitution effect move in the same direction, leading to a flatter demand curve."], a: 0, why: "The IE opposes the SE (so part of the SE is cancelled), making demand less responsive: a steeper curve." },
  { q: "[May/June 2022 · 32 · Q6] When the price of a good falls, the overall effect on the quantity demanded can be separated into income and substitution effects. Which statement describes a Giffen good?", opts: ["The income effect is irrelevant for a Giffen good.", "The income effect works in the same direction as the substitution effect.", "The income effect works against the substitution effect and is of a greater magnitude.", "The income effect works against the substitution effect but is of a smaller magnitude."], a: 2, why: "D describes an ordinary inferior good. A Giffen good has the larger, opposing income effect." },
  { q: "[May/June 2023 · 31 · Q3] Which assumption in relation to an indifference theory diagram is not correct?", opts: ["The consumer's income may change.", "The consumer may change their satisfaction-maximising objective.", "The consumers may change their tastes and preferences.", "The relative prices of products may change."], a: 1, why: "The theory assumes the consumer always aims to maximise satisfaction. Income, tastes and prices can change." },
  { q: "[May/June 2025 · 31 · Q3] What would not affect the budget line of an individual consumer?", opts: ["the individual's preference for various goods", "the level of income tax", "the money prices of goods", "the incomes earned by the individual"], a: 0, why: "Preferences determine the indifference curves, not the budget line. Income tax changes disposable income." },
  { q: "[Oct/Nov 2021 · 31 · Q5] What does a budget line on an indifference curve diagram show?", opts: ["the amount that a household has available to spend plotted against time", "the combinations of two goods that can be purchased when all income is spent", "the difference between a government's income and expenditure plotted against time", "the relationship between the price of a good and the amount demanded"], a: 1, why: "A budget line is the set of affordable combinations at the given income and prices." },
  { q: "[Oct/Nov 2022 · 32 · Q5] Which statement about a budget line in consumer behaviour theory is correct?", opts: ["It illustrates consumer preference between two goods.", "It illustrates combinations of two goods that consumers are able to purchase with a given income.", "It illustrates the least cost combination of goods that yield the same level of utility.", "It illustrates the income effect of a price change."], a: 1, why: "Preferences belong to the indifference curves." },
  { q: "[Oct/Nov 2022 · 32 · Q6] When the price of a good increases, which statement is correct according to the analysis that uses budget lines and indifference curves?", opts: ["The income and substitution effects of the price increase will work in opposite directions in the case of a Giffen good.", "The income effect of the price increase will result in reduced consumption for all goods.", "The new equilibrium position will be where the new budget line meets the original indifference curve.", "The price rise will be represented by a parallel shift inwards of the original budget line."], a: 0, why: "B is wrong for inferior goods, C confuses the new equilibrium with the compensating line, and D describes an income fall; a price rise pivots the line." },
  { q: "[Oct/Nov 2023 · 32 · Q2] Which statement about such an indifference curve diagram is correct?", opts: ["The range of indifference curves shows the combination of products a consumer can purchase with a given income.", "If an indifference curve is a downward-sloping straight line, the principle of diminishing marginal utility must be operating.", "Indifference curves never cross, because this means that a consumer would be indifferent between combinations of two goods, even when one combination provides more of each good.", "The gap between indifference curves is always constant."], a: 2, why: "If curves crossed, a bundle with more of both goods would give the same satisfaction, which contradicts 'more is better'." },
  { q: "[Oct/Nov 2024 · 33 · Q2] Which statement about indifference curves is not correct?", opts: ["Indifference curves are usually convex to the origin of the diagram.", "Indifference curves can intersect each other.", "The consumer always prefers a higher indifference curve to a lower one.", "The slope of the indifference curve represents the marginal rate of substitution."], a: 1, why: "Indifference curves cannot intersect." },
  { q: "[Oct/Nov 2024 · 31 · Q2] What is a characteristic of an indifference curve?", opts: ["It will remain concave to the origin of the diagram.", "It will remain convex to the origin of the diagram.", "It can intersect other indifference curves at any point.", "The lower the indifference curve, the greater the satisfaction attainable."], a: 1, why: "Convex to the origin because of the diminishing marginal rate of substitution." },
  { q: "[Oct/Nov 2023 · 33 · Q2] An indifference curve is typically drawn with a convex shape. Which economic concept explains the reason for this convex shape?", opts: ["allocative efficiency", "diminishing marginal rate of substitution", "Pareto optimality", "the equi-marginal principle"], a: 1, why: "As X rises, the consumer will give up less Y for each extra unit of X." },
] });
