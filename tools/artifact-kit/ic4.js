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
decompStepper("#stB", INF, 1.5, "Price effect for an inferior good split into substitution and income effects", (d) => [
  `<b>Equilibrium A.</b> Income $60, Y costs $1, X costs $3. The consumer buys ${Lib.fmtN(d.A.x, 1)} units of X and ${Lib.fmtN(d.A.y, 0)} of Y.`,
  "<b>The price of X falls to $1.50.</b> The budget line pivots outwards around the Y-axis intercept.",
  `<b>New equilibrium B</b> on a higher curve: ${Lib.fmtN(d.B.x, 1)} units of X. The total change is ${sg(d.B.x - d.A.x)}.`,
  "<b>The compensating budget line</b> (dashed): parallel to the new budget line and touching the original curve IC1 at C.",
  `<b>Substitution effect, A to C:</b> the consumer moves along IC1 towards the cheaper good: <b>${sg(d.SE)}</b> units of X.`,
  `<b>Income effect, C to B:</b> the consumer is richer in real terms and buys <b>less</b> X, <b>${sg(d.IE)}</b>, because X is inferior. The IE is <b>smaller</b> than the SE, so the net change is still <b>${sg(d.B.x - d.A.x)}</b>: the demand curve still slopes downward. If the IE were bigger, the good would be Giffen.`,
]);
/* ---------- Lab 2 and 3: decomposition labs ---------- */
function decompLab(m, sliderId, prefix, svgId, verdictFn) {
  if (!$("#" + sliderId)) return;
  const px1 = +$("#" + sliderId).value, d = decomp(m, px1), tot = d.B.x - d.A.x;
  $("#" + prefix + "1").textContent = sg(d.SE); $("#" + prefix + "2").textContent = sg(d.IE); $("#" + prefix + "3").textContent = sg(tot);
  $("#" + (prefix === "s" ? "sv" : "tv")).textContent = verdictFn(d, px1, tot);
  $("#" + svgId).innerHTML = drawDecomp(m, FR(50, 270, 340, 240, m.xm, m.ym), px1, { bl0: 1, ic0: 1, pa: 1, bl1: 1, ic1: 1, pb: 1, bc: 1, se: 0, ie: 0 });
}
const vInf = (d, p, t) => p === INF.px0 ? "No price change: A, B and C are the same point." : p < INF.px0 ? `Price falls to $${p}. SE ${sg(d.SE)} raises X, but IE ${sg(d.IE)} works against it (inferior good). The IE is smaller than the SE, so the total ${sg(t)} is still positive: not a Giffen good.` : `Price rises to $${p}. The SE cuts X by ${sg(d.SE)}, and the IE ${sg(d.IE)} partly offsets it. Total ${sg(t)}.`;
const l3 = () => decompLab(INF, "ip", "t", "labC", vInf);
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
  ["Normal good", "Demand rises with income; both effects raise quantity when the price falls"],
  ["Inferior good", "Demand falls as income rises; the income effect works against the substitution effect"],
  ["Giffen good", "An inferior good whose negative income effect is larger than the substitution effect"],
  ["Law of demand", "Quantity demanded falls as price rises, other things equal"],
  ["Net effect", "The substitution effect plus the income effect"],
  ["Staple food", "A basic food that takes a large part of a poor household's budget"],
], done: "Six words for the kinds of good." });
Lib.calc($("#c1"), { qs: [
  { q: "A fall in the price of X has a substitution effect of +14 units and an income effect of −6 units. What is the net change in X?", a: 8, sol: "14 − 6 = <b>+8</b> units. Inferior, but not Giffen." },
  { q: "SE is +5 and IE is −9. What is the net change in X?", a: -4, sol: "5 − 9 = <b>−4</b>. Quantity falls when the price falls: a Giffen good." },
  { q: "A good has SE = +12 units and IE = −4 units after a price fall. What is the net change?", a: 8, sol: "12 − 4 = <b>+8</b>: inferior, not Giffen." },
  { q: "A good has SE = +5.4 and IE = −1.7. By how much would the IE have to change in size before the good became Giffen (units, 1 decimal place)?", a: 3.7, tol: 0.1, hint: "The net change must fall below zero.", sol: "The IE would need to exceed 5.4 in size, so it must grow by more than 5.4 − 1.7 = <b>3.7</b> units." },
  { q: "SE = +10 and IE = −10. What is the net change (units)?", a: 0, sol: "10 − 10 = <b>0</b>. The borderline case: any larger negative IE makes the good Giffen." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "For an inferior good (not Giffen), a price fall causes:", opts: ["quantity to fall", "quantity to rise by more than for a normal good", "quantity to rise by less than for a normal good", "no change"], a: 2, why: "The negative income effect offsets part of the positive substitution effect." },
  { q: "Which condition makes a good a Giffen good?", opts: ["Positive income effect larger than the SE", "Negative income effect larger than the SE", "Zero income effect", "Negative substitution effect"], a: 1, why: "Only then does quantity fall when the price falls, giving an upward sloping demand curve." },
  { q: "The demand curve for an inferior good (not Giffen) is:", opts: ["upward sloping", "downward sloping", "vertical", "horizontal"], a: 1, why: "The net effect of a price fall is still a rise in quantity." },
  { q: "A Giffen good must be:", opts: ["a normal good", "an inferior good", "a luxury", "a public good"], a: 1, why: "The negative income effect that overrides the SE comes from the good being inferior." },
  { q: "If the substitution effect of a price rise is −3 and the income effect is +5 (for a Giffen good), the net change in quantity is:", opts: ["−8", "−2", "+2", "+8"], a: 2, why: "−3 + 5 = +2: quantity rises when price rises." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Normal good", "Positive income effect: demand rises with income. Both effects raise quantity when price falls."],
  ["Inferior good", "Negative income effect. Demand still usually slopes downward."],
  ["Giffen good", "Inferior good whose negative income effect exceeds the SE; the demand curve slopes upward."],
  ["Law of demand", "Quantity demanded falls as price rises, other things equal."],
  ["Net effect", "The substitution effect plus the income effect."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2025 · 32 · Q5] Which statement about the downward sloping demand curve of an inferior good is correct?", opts: ["Negative income effect and substitution effect move in opposite directions, leading to a steeper demand curve.", "Negative income effect and substitution effect move in the same direction, leading to a flatter demand curve.", "Positive income effect and substitution effect move in opposite directions, leading to a steeper demand curve.", "Positive income effect and substitution effect move in the same direction, leading to a flatter demand curve."], a: 0, why: "The IE opposes the SE (so part of the SE is cancelled), making demand less responsive: a steeper curve." },
  { q: "[May/June 2022 · 32 · Q6] When the price of a good falls, the overall effect on the quantity demanded can be separated into income and substitution effects. Which statement describes a Giffen good?", opts: ["The income effect is irrelevant for a Giffen good.", "The income effect works in the same direction as the substitution effect.", "The income effect works against the substitution effect and is of a greater magnitude.", "The income effect works against the substitution effect but is of a smaller magnitude."], a: 2, why: "D describes an ordinary inferior good. A Giffen good has the larger, opposing income effect." },
  { q: "[May/June 2022 · 31 · Q6] Broken rice is an inferior good. What would be the resulting income and substitution effect on the quantity demanded of broken rice if its price falls? (quantity demanded due to income effect, quantity demanded due to substitution effect)", opts: ["falls, falls", "falls, rises", "rises, falls", "rises, rises"], a: 1, why: "For an inferior good a rise in real income lowers quantity, while the cheaper relative price raises it through the substitution effect." },
] });
