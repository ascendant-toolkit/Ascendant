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


/* ---------- Watch: building the diagram ---------- */
(function () {
  const F = FR(60, 300, 600, 260, 60, 60), M = NORM.M;
  function draw(s) {
    let o = frameAxes(F, "Good X", "Good Y");
    if (s.ic > 0) o += icLine(NORM, F, 20, "c1", op(s.ic)) + SV.text(F.X(52), F.Y(400 / 52) - 12, "IC", "lbl bd t1", op(s.ic));
    if (s.pts > 0) [[10, 40, "a"], [20, 20, "b"], [40, 10, "c"]].forEach(([x, y, l]) => { o += SV.circle(F.X(x), F.Y(y), 6, "dot1", op(s.pts)) + SV.text(F.X(x) + 14, F.Y(y) - 8, l, "lbl bd t1", op(s.pts)); });
    if (s.map > 0) o += icLine(NORM, F, 28, "c4", op(s.map)) + icLine(NORM, F, 12, "c3", op(s.map)) + SV.text(F.X(52), F.Y(784 / 52) - 12, "higher", "sm bd t4", op(s.map)) + SV.text(F.X(40), F.Y(144 / 40) - 12, "lower", "sm bd t3", op(s.map));
    if (s.aff > 0) o += SV.poly([[F.X(0), F.Y(0)], [F.X(30), F.Y(0)], [F.X(0), F.Y(60)]], "f1", { opacity: 0.18 * s.aff });
    if (s.bl > 0) o += bline(F, 4, 2, M, "gr", { "stroke-width": 3, ...op(s.bl) }) + SV.text(F.X(30), F.Y(0) - 8, "30", "sm bd", { "text-anchor": "middle", ...op(s.bl) }) + SV.text(F.X(0) + 8, F.Y(60) + 4, "60", "sm bd", op(s.bl)) + SV.text(F.X(1.5), F.Y(22), "budget line", "lbl bd", { "text-anchor": "start", ...op(s.bl) });
    if (s.eq > 0) o += icLine(NORM, F, Math.sqrt(450), "c2", op(s.eq)) + SV.circle(F.X(15), F.Y(30), 7, "dot2", op(s.eq)) + SV.text(F.X(15) + 16, F.Y(30) - 10, "best choice", "lbl bd t2", op(s.eq));
    return o;
  }
  Lib.stepper($("#stI"), { w: 740, h: 380, label: "Building an indifference curve, an indifference map and a budget line", base: { ic: 0, pts: 0, map: 0, aff: 0, bl: 0, eq: 0 }, draw, tween: 800, dwell: 5600, steps: [
    { cap: "<b>An indifference curve.</b> Points a, b and c are different bundles of X and Y that give the <b>same satisfaction</b>: 10 X with 40 Y, 20 with 20, or 40 with 10. The consumer is indifferent between them.", s: { ic: 1, pts: 1 } },
    { cap: "<b>The curve slopes down and bends in.</b> To keep satisfaction the same, more X means less Y. It is <b>convex</b> because the more X the consumer has, the less Y they will give up for one more X (diminishing MRS).", s: { ic: 1, pts: 1 } },
    { cap: "<b>An indifference map.</b> A curve further from the origin has more of both goods, so it gives <b>more satisfaction</b>. Curves never cross.", s: { ic: 1, pts: 0.4, map: 1 } },
    { cap: "<b>A budget line.</b> With income $120, Px = $4 and Py = $2 the consumer can buy at most 30 X or 60 Y. The line joins these points and the shaded triangle is everything <b>affordable</b>. Its slope is Px ÷ Py = 2.", s: { ic: 0.4, map: 0.4, aff: 1, bl: 1 } },
    { cap: "<b>Putting them together.</b> The best choice is on the <b>highest indifference curve the budget line allows</b>, where the line just touches the curve: 15 X and 30 Y. Part 2 explains why.", s: { ic: 0.3, map: 0.3, aff: 1, bl: 1, eq: 1 } },
  ] });
})();

/* ---------- Lab 1: budget line ---------- */
function labBL() {
  if (!$("#bm") || !$("#bx") || !$("#by")) return;
  const M = +$("#bm").value, px = +$("#bx").value, py = +$("#by").value, mx = M / px, my = M / py, cost = 20 * px + 20 * py, ok = cost <= M, F = FR(50, 290, 340, 250, 80, 80);
  $("#b1").textContent = Lib.fmtN(mx, 1); $("#b2").textContent = Lib.fmtN(my, 1); $("#b3").textContent = Lib.fmtN(px / py, 2); $("#b4").textContent = ok ? "Yes ($" + cost + ")" : "No ($" + cost + ")";
  $("#bv").textContent = `With $${M} the consumer can buy at most ${Lib.fmtN(mx, 1)} X or ${Lib.fmtN(my, 1)} Y. The slope is Px ÷ Py = ${Lib.fmtN(px / py, 2)}: giving up 1 X frees enough money for ${Lib.fmtN(px / py, 2)} Y. The bundle (20, 20) costs $${cost}, so it is ${ok ? "inside the budget" : "beyond the budget line"}.`;
  const x2 = Math.min(mx, 80), y1 = Math.min(my, 80);
  let o = frameAxes(F, "Good X", "Good Y") + SV.poly([[F.X(0), F.Y(0)], [F.X(Math.min(mx, 80)), F.Y(0)], [F.X(0), F.Y(Math.min(my, 80))]], "f1", { opacity: 0.18 }) + bline(F, px, py, M, "c3", { "stroke-width": 3 }) + SV.circle(F.X(20), F.Y(20), 7, ok ? "dot3" : "dot2") + SV.text(F.X(20) + 12, F.Y(20) - 10, "(20, 20)", "lbl bd", {});
  $("#labP").innerHTML = o;
}
Lib.slider($("#g8"), { id: "bm", label: "Income ($): ", min: 40, max: 160, step: 10, value: 120, fmt: (v) => v, onInput: labBL });
Lib.slider($("#g9"), { id: "bx", label: "Price of X ($): ", min: 2, max: 8, step: 1, value: 4, fmt: (v) => v, onInput: labBL });
Lib.slider($("#g10"), { id: "by", label: "Price of Y ($): ", min: 2, max: 8, step: 1, value: 2, fmt: (v) => v, onInput: labBL });

/* ---------- Lab 2: compare bundles ---------- */
function labBun() {
  if (!$("#qx") || !$("#qy")) return;
  const x = +$("#qx").value, y = +$("#qy").value, u = Math.sqrt(x * y), F = FR(50, 290, 340, 250, 60, 60), d = u - 20;
  $("#c1r").textContent = Lib.fmtN(u, 1); $("#c2r").textContent = Math.abs(d) < 0.05 ? "Same" : d > 0 ? "Better" : "Worse"; $("#c3r").textContent = Lib.fmtN(y / x, 2);
  $("#cv").textContent = Math.abs(d) < 0.05 ? "This bundle lies on the same indifference curve as the reference: the consumer is indifferent."
    : d > 0 ? `This bundle is on a higher indifference curve (${Lib.fmtN(u, 1)} against 20): the consumer prefers it. More of both goods always raises satisfaction.`
    : `This bundle is on a lower curve (${Lib.fmtN(u, 1)} against 20): the consumer likes it less. The MRS here is ${Lib.fmtN(y / x, 2)}: the consumer would give up ${Lib.fmtN(y / x, 2)} Y for one more X.`;
  $("#labQ").innerHTML = frameAxes(F, "Good X", "Good Y") + icLine(NORM, F, 20, "c3", { "stroke-dasharray": "6 5" }) + SV.text(F.X(58), F.Y(400 / 58) - 12, "reference curve", "sm bd t3", { "text-anchor": "end" }) + icLine(NORM, F, u, "c1") + SV.circle(F.X(20), F.Y(20), 5, "dot3") + SV.circle(F.X(x), F.Y(y), 7, "dot1") + SV.text(F.X(x) + 12, F.Y(y) - 10, "your bundle", "lbl bd t1");
}
Lib.slider($("#g11"), { id: "qx", label: "Units of X: ", min: 5, max: 50, step: 1, value: 30, fmt: (v) => v, onInput: labBun });
Lib.slider($("#g12"), { id: "qy", label: "Units of Y: ", min: 5, max: 50, step: 1, value: 20, fmt: (v) => v, onInput: labBun });

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
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Indifference curve", "A curve joining combinations of two goods that give the same satisfaction"],
  ["Indifference map", "A set of indifference curves; further from the origin means higher satisfaction"],
  ["Marginal rate of substitution", "How much of one good is given up for one more unit of the other, the slope of the curve"],
  ["Diminishing MRS", "The reason indifference curves are convex to the origin"],
  ["Budget line", "All combinations of two goods affordable with a given income and prices"],
  ["Slope of the budget line", "Px ÷ Py"],
  ["Affordable region", "The area on and below the budget line"],
], done: "Seven words for the building blocks." });
Lib.calc($("#c1"), { qs: [
  { q: "Income is $120, the price of X is $4 and the price of Y is $2. How many units of X could be bought if all income is spent on X?", a: 30, sol: "120 ÷ 4 = <b>30</b>." },
  { q: "Same income and prices. How many units of Y if all income is spent on Y?", a: 60, sol: "120 ÷ 2 = <b>60</b>." },
  { q: "What is the slope of that budget line (Px ÷ Py)?", a: 2, sol: "4 ÷ 2 = <b>2</b>: for each extra unit of X, give up 2 units of Y." },
  { q: "Income is $90, Px = $3 and Py = $6. What is the maximum quantity of X?", a: 30, sol: "90 ÷ 3 = <b>30</b>." },
  { q: "An indifference curve passes through 10 X with 40 Y and 20 X with 20 Y. How many units of Y does the consumer give up, on average, for each of the extra 10 units of X?", a: 2, sol: "Y falls by 20 over 10 extra units of X: <b>2 Y for each X</b>. This is the average MRS." },
  { q: "Income rises from $120 to $150 with prices unchanged (Px = $4, Py = $2). What is the new maximum quantity of Y?", a: 75, sol: "150 ÷ 2 = <b>75</b>. The line shifts out in parallel." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A rise in income, with prices unchanged, causes the budget line to:", opts: ["pivot inwards", "pivot outwards", "shift outwards in parallel", "become flatter"], a: 2, why: "The slope (Px ÷ Py) is unchanged, so the line shifts in parallel." },
  { q: "Indifference curves are convex to the origin because of:", opts: ["diminishing marginal rate of substitution", "rising prices", "falling income", "economies of scale"], a: 0, why: "The more X you have, the less Y you will give up to get another unit of X." },
  { q: "Indifference curves never cross because:", opts: ["income is constant", "a crossing point would be on two different levels of satisfaction", "prices are constant", "MRS is zero"], a: 1, why: "If they crossed, one bundle would give two different levels of satisfaction." },
  { q: "The slope of the budget line is:", opts: ["Py ÷ Px", "Px ÷ Py", "income ÷ price", "MUx ÷ MUy"], a: 1, why: "It shows how many units of Y must be given up for one more X." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Indifference curve", "A curve joining all combinations of two goods that give the same satisfaction."],
  ["Indifference map", "A set of indifference curves; further from the origin means higher satisfaction."],
  ["Marginal rate of substitution (MRS)", "The amount of one good the consumer will give up for one more unit of the other. The slope of the indifference curve."],
  ["Diminishing MRS", "Why indifference curves are convex to the origin."],
  ["Budget line", "All combinations of two goods affordable with a given income and prices."],
  ["Slope of the budget line", "Px ÷ Py."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2024 · 32 · Q2] What does an indifference curve show?", opts: ["the amount of two products achievable with given income and prices", "the different combinations of two goods that give a consumer equal utility", "the income available to buy the two goods", "the rate at which marginal utility changes as consumption changes"], a: 1, why: "A is the budget line. B is the indifference curve." },
  { q: "[May/June 2023 · 31 · Q3] Which assumption in relation to an indifference theory diagram is not correct?", opts: ["The consumer's income may change.", "The consumer may change their satisfaction-maximising objective.", "The consumers may change their tastes and preferences.", "The relative prices of products may change."], a: 1, why: "The theory assumes the consumer always aims to maximise satisfaction. Income, tastes and prices can change." },
  { q: "[May/June 2025 · 31 · Q3] What would not affect the budget line of an individual consumer?", opts: ["the individual's preference for various goods", "the level of income tax", "the money prices of goods", "the incomes earned by the individual"], a: 0, why: "Preferences determine the indifference curves, not the budget line. Income tax changes disposable income." },
  { q: "[Oct/Nov 2021 · 31 · Q5] What does a budget line on an indifference curve diagram show?", opts: ["the amount that a household has available to spend plotted against time", "the combinations of two goods that can be purchased when all income is spent", "the difference between a government's income and expenditure plotted against time", "the relationship between the price of a good and the amount demanded"], a: 1, why: "A budget line is the set of affordable combinations at the given income and prices." },
  { q: "[Oct/Nov 2022 · 32 · Q5] Which statement about a budget line in consumer behaviour theory is correct?", opts: ["It illustrates consumer preference between two goods.", "It illustrates combinations of two goods that consumers are able to purchase with a given income.", "It illustrates the least cost combination of goods that yield the same level of utility.", "It illustrates the income effect of a price change."], a: 1, why: "Preferences belong to the indifference curves." },
  { q: "[Oct/Nov 2024 · 33 · Q2] Which statement about indifference curves is not correct?", opts: ["Indifference curves are usually convex to the origin of the diagram.", "Indifference curves can intersect each other.", "The consumer always prefers a higher indifference curve to a lower one.", "The slope of the indifference curve represents the marginal rate of substitution."], a: 1, why: "Indifference curves cannot intersect." },
  { q: "[Oct/Nov 2024 · 31 · Q2] What is a characteristic of an indifference curve?", opts: ["It will remain concave to the origin of the diagram.", "It will remain convex to the origin of the diagram.", "It can intersect other indifference curves at any point.", "The lower the indifference curve, the greater the satisfaction attainable."], a: 1, why: "Convex to the origin because of the diminishing marginal rate of substitution." },
  { q: "[Oct/Nov 2023 · 33 · Q2] An indifference curve is typically drawn with a convex shape. Which economic concept explains the reason for this convex shape?", opts: ["allocative efficiency", "diminishing marginal rate of substitution", "Pareto optimality", "the equi-marginal principle"], a: 1, why: "As X rises, the consumer will give up less Y for each extra unit of X." },
  { q: "[Oct/Nov 2021 · 32 · Q4] A consumer currently consumes 10 units of good X and 10 units of good Y at point Z on an indifference curve. The consumer's marginal utilities from consuming both good X and good Y are positive. Which combination of good X and good Y could be on the same indifference curve as point Z?", opts: ["9 units of X and 11 of Y", "10 units of X and 11 of Y", "11 units of X and 10 of Y", "12 units of X and 12 of Y"], a: 0, why: "On the same curve, less of one good must be offset by more of the other. B, C and D have at least as much of both goods, so they give more satisfaction." },
  { q: "[May/June 2022 · 32 · Q5] What does a budget line show?", opts: ["the behaviour of a utility-maximising consumer", "the difference between an individual's consumption and saving", "the monetary value of the disposable income of a consumer", "the maximum combinations of two products that a consumer can buy with a given level of income"], a: 3, why: "The budget line shows the affordable combinations of two goods." },
] });
