/* ---------- model: kink at P = 10, Q = 5 ----------
   upper demand  P = 14 - 0.8Q   (rivals ignore a rise)   MR = 14 - 1.6Q
   lower demand  P = 10 - s2 (Q - 5), default s2 = 2 so P = 20 - 2Q (rivals match a cut)   MR = 10 + 5 s2 - 2 s2 Q
   MC passes through (5, c), slope 0.6; c = 5 gives MC = 2 + 0.6Q */
const S1 = 0.8, KQ = 5, KP = 10;
const D1 = (q) => 14 - S1 * q, MR1 = (q) => 14 - 2 * S1 * q;
const D2 = (q, s2) => KP - s2 * (q - KQ), MR2 = (q, s2) => KP + KQ * s2 - 2 * s2 * q;
const MCf = (q, c) => c - 0.6 * KQ + 0.6 * q;
const op = (v) => ({ style: `opacity:${Math.max(0, Math.min(1, v))}` });
const opf = (v, k = 1) => ({ style: `opacity:${Math.max(0, Math.min(1, v)) * 0.28 * k}` });
const halo = "paint-order:stroke;stroke:var(--surface);stroke-width:5px";
const fr = (x0, xs, y0, ys) => ({ X: (q) => x0 + q * xs, Y: (p) => y0 - p * ys, x0, y0 });
const BIG = fr(70, 66, 290, 16.5), SMALL = fr(52, 43, 262, 14);

/* where does MC cut MR? returns {q, p, where} */
function solve(c, s2) {
  const hi = MR1(KQ), lo = MR2(KQ, s2);
  if (c > hi) { const q = (14 - (c - 3)) / (1.6 + 0.6); return { q, p: D1(q), where: "above" }; }
  if (c < lo) { const q = (KP + KQ * s2 - (c - 3)) / (2 * s2 + 0.6); return { q, p: D2(q, s2), where: "below" }; }
  return { q: KQ, p: KP, where: "in" };
}

function axes(F, W, H) {
  const { X, Y } = F;
  return SV.line(F.x0, Y(16), F.x0, Y(-6)) + SV.line(F.x0, Y(0), W, Y(0)) + SV.text(F.x0 + 6, Y(16) - 2, "Price / cost ($)", "sm") + SV.text(W - 2, Y(0) - 8, "Quantity", "sm", { "text-anchor": "end" });
}
function seg(F, f, q0, q1, u, cls, o) {
  const q = q0 + (q1 - q0) * u;
  return u > 0.001 ? SV.line(F.X(q0), F.Y(f(q0)), F.X(q), F.Y(f(q)), cls, o) : "";
}

/* the kinked-demand picture; s controls what is shown */
function kinkDraw(F, W, s) {
  const { X, Y } = F, s2 = s.s2 ?? 2, c = s.c ?? 5;
  const qd2 = Math.min(10, KQ + 10 / s2), qm2 = Math.min(10, (16 + KQ * s2) / (2 * s2));
  let o = axes(F, W);
  o += SV.text(X(KQ), Y(-6) + 16, "Q₀ = 5", "sm bd", { "text-anchor": "middle", ...op(s.pt) }) ;
  o += SV.text(F.x0 - 6, Y(KP) + 4, "P₀ = 10", "sm bd", { "text-anchor": "end", ...op(s.pt) });
  if (s.pt > 0) o += SV.line(F.x0, Y(KP), X(KQ), Y(KP), "gr", op(s.pt)) + SV.line(X(KQ), Y(KP), X(KQ), Y(-6), "gr", op(s.pt));
  o += seg(F, D1, 0, KQ, s.d1 ?? 0, "c1") + seg(F, (q) => D2(q, s2), KQ, qd2, s.d2 ?? 0, "c1");
  if ((s.dl ?? 0) > 0) o += SV.text(X(0.3), Y(D1(0.3)) - 9, "D, elastic above the kink", "lbl bd t1", op(s.dl)) + SV.text(X(5.5) + 12, Y(D2(5.5, s2)) - 6, "D, inelastic below", "lbl bd t1", op(s.dl));
  o += seg(F, MR1, 0, KQ, s.m1 ?? 0, "c3 dash") + seg(F, (q) => MR2(q, s2), KQ, qm2, s.m2 ?? 0, "c3 dash");
  if ((s.m1 ?? 0) > 0.6) o += SV.text(X(2.2) - 8, Y(MR1(2.2)) + 16, "MR (upper)", "lbl bd t3", { "text-anchor": "end", ...op(s.m1) });
  if ((s.m2 ?? 0) > 0.6) o += SV.text(X(Math.min(qm2, 7.5)), Y(MR2(Math.min(qm2, 7.5), s2)) + (qm2 < 7.5 ? 14 : 14), "MR (lower)", "lbl bd t3", { "text-anchor": "start", ...op(s.m2) });
  if ((s.gap ?? 0) > 0) {
    const hi = MR1(KQ), lo = MR2(KQ, s2);
    o += SV.rect(X(KQ) - 5, Y(hi), 10, Y(lo) - Y(hi), "f4", opf(s.gap, 1.3)) + SV.line(X(KQ), Y(hi), X(KQ), Y(lo), "c4", { "stroke-width": 3, ...op(s.gap) });
    o += SV.text(X(KQ) + 12, (Y(hi) + Y(lo)) / 2 + 4, "gap in MR: $" + fmtN(lo, 1) + " to $" + fmtN(hi, 1), "lbl bd t4", { style: `${halo};opacity:${Math.max(0, Math.min(1, s.gap))}` });
  }
  if ((s.mc ?? 0) > 0) {
    o += seg(F, (q) => MCf(q, c), 0, 10, s.mc, "c2");
    if (s.mc > 0.6) o += SV.text(X(10) - 2, Y(MCf(10, c)) - 8, "MC", "lbl bd t2", { "text-anchor": "end", ...op(s.mc) });
  }
  if (s.ghost !== undefined && (s.mc ?? 0) > 0.5) o += seg(F, (q) => MCf(q, s.ghost), 0, 10, 1, "c2 dash", { style: "opacity:.35" });
  if ((s.pm ?? 0) > 0) {
    const r = solve(c, s2);
    o += SV.line(F.x0, Y(r.p), X(r.q), Y(r.p), "gr", op(s.pm)) + SV.line(X(r.q), Y(r.p), X(r.q), Y(0), "gr", op(s.pm));
    o += SV.circle(X(r.q), Y(r.p), 7, "dot1", op(s.pm)) + SV.text(X(r.q) + 12, Y(r.p) - 10, `profit-max: price $${fmtN(r.p, 2)}, output ${fmtN(r.q, 2)}`, "lbl bd t1", { style: `${halo};opacity:${Math.max(0, Math.min(1, s.pm))}` });
  } else if ((s.pt ?? 0) > 0) o += SV.circle(X(KQ), Y(KP), 6, "dot1", op(s.pt));
  return o;
}
const wrap = (F, W, H, s, label) => `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${label}">${kinkDraw(F, W, s)}</svg>`;
const ALL = { pt: 1, d1: 1, d2: 1, dl: 1, m1: 1, m2: 1, gap: 1, mc: 1, pm: 1 };

/* Learn picture */
$("#pic1").innerHTML = wrap(BIG, 780, 425, ALL, "Kinked demand curve with two segments of marginal revenue, the gap between them and a marginal cost curve running through the gap");

/* Watch 1: building the kink */
Lib.stepper($("#stA"), { w: 780, h: 425, label: "Building a kinked demand curve step by step", base: { pt: 0, d1: 0, d2: 0, dl: 0, m1: 0, m2: 0, gap: 0, mc: 0, pm: 0 }, draw: (s) => kinkDraw(BIG, 780, s), tween: 900, dwell: 5600, steps: [
  { cap: "<b>The starting point.</b> An oligopolist charges <b>$10</b> and sells <b>5 units</b>. It shares the market with a few rivals, so it must think about how they would respond to any price change.", s: { pt: 1 } },
  { cap: "<b>Price rise: rivals do not follow.</b> If the firm charges more than $10, its rivals keep their prices and customers switch to them. Quantity falls a lot, so demand above $10 is <b>elastic</b> (a flatter line) and revenue falls.", s: { pt: 1, d1: 1 } },
  { cap: "<b>Price cut: rivals match.</b> If the firm charges less than $10, rivals cut too to avoid losing customers. The firm gains little, so demand below $10 is <b>inelastic</b> (a steeper line) and revenue falls again.", s: { pt: 1, d1: 1, d2: 1, dl: 1 } },
  { cap: "<b>MR above the kink.</b> Marginal revenue for the flatter segment starts on the vertical axis at $14 and falls at twice the slope. At 5 units it is <b>$6</b>.", s: { pt: 1, d1: 1, d2: 1, dl: 1, m1: 1 } },
  { cap: "<b>MR below the kink.</b> The steeper segment has its own MR, which at 5 units is only <b>$0</b>. The price has to fall further for each extra unit sold, and the loss on the first 5 units is bigger.", s: { pt: 1, d1: 1, d2: 1, dl: 1, m1: 1, m2: 1 } },
  { cap: "<b>The gap in MR.</b> At 5 units MR drops vertically from $6 to $0. This is the vertical break in the marginal revenue curve, and it is a gap in <b>MR</b>, not in MC.", s: { pt: 1, d1: 1, d2: 1, dl: 1, m1: 1, m2: 1, gap: 1 } },
  { cap: "<b>Marginal cost.</b> The usual upward-sloping MC curve passes through the gap, cutting the vertical part of MR at 5 units. At 5 units MC is $5.", s: { pt: 1, d1: 1, d2: 1, dl: 1, m1: 1, m2: 1, gap: 1, mc: 1 } },
  { cap: "<b>Profit maximisation.</b> MC = MR at 5 units, and the demand curve says buyers will pay <b>$10</b> for that output. The firm sits at the kink. Any MC curve through the gap would give the same answer.", s: { pt: 1, d1: 1, d2: 1, dl: 1, m1: 1, m2: 1, gap: 1, mc: 1, pm: 1 } },
] });

/* Watch 2: why MR drops (waterfall) */
const U = 22, BASE = 330;
function wfDraw(s) {
  const cols = [{ x: 60, loss: S1 * KQ, title: "Just left of the kink", sub: "flatter segment: rivals ignore a rise" }, { x: 420, loss: 2 * KQ, title: "Just right of the kink", sub: "steeper segment: rivals match a cut" }];
  let o = SV.line(40, BASE, 760, BASE);
  cols.forEach((c, i) => {
    const mr = KP - c.loss;
    o += SV.text(c.x + 155, 34, c.title, "lbl bd", { "text-anchor": "middle" }) + SV.text(c.x + 155, 52, c.sub, "sm", { "text-anchor": "middle" });
    o += SV.rect(c.x, BASE - KP * U, 90, KP * U, "f1", opf(s.a, 1.2)) + SV.text(c.x + 45, BASE - KP * U - 8, "$10", "lbl bd t1", { "text-anchor": "middle", ...op(s.a) }) + SV.text(c.x + 45, BASE + 18, "Price of the", "sm", { "text-anchor": "middle", ...op(s.a) }) + SV.text(c.x + 45, BASE + 32, "extra unit", "sm", { "text-anchor": "middle", ...op(s.a) });
    const lossH = c.loss * U * Math.min(1, s.b);
    o += SV.rect(c.x + 110, BASE - KP * U, 90, lossH, "f2", opf(s.b, 1.2)) + SV.text(c.x + 155, BASE - KP * U - 8, "− $" + fmtN(c.loss, 0), "lbl bd t2", { "text-anchor": "middle", ...op(s.b) }) + SV.text(c.x + 155, BASE + 18, "Lost on the 5 units", "sm", { "text-anchor": "middle", ...op(s.b) }) + SV.text(c.x + 155, BASE + 32, i ? "(2.00 x 5)" : "(0.80 x 5)", "sm", { "text-anchor": "middle", ...op(s.b) });
    o += SV.rect(c.x + 220, BASE - mr * U * Math.min(1, s.c), 90, mr * U * Math.min(1, s.c), "f3", opf(s.c, 1.2)) + SV.text(c.x + 265, BASE - Math.max(mr, 0) * U - 8, "= $" + fmtN(mr, 0), "lbl bd t3", { "text-anchor": "middle", ...op(s.c) }) + SV.text(c.x + 265, BASE + 18, "Marginal", "sm", { "text-anchor": "middle", ...op(s.c) }) + SV.text(c.x + 265, BASE + 32, "revenue", "sm", { "text-anchor": "middle", ...op(s.c) });
  });
  if (s.d > 0) o += SV.text(390, 380, "MR falls from $6 to $0 at 5 units: a gap of $6", "lbl bd t4", { "text-anchor": "middle", ...op(s.d) });
  return o;
}
Lib.stepper($("#stB"), { w: 780, h: 400, label: "Marginal revenue calculated just left and just right of the kink", base: { a: 0, b: 0, c: 0, d: 0 }, draw: wfDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The question.</b> The firm is selling 5 units at $10 and asks: what extra revenue would a 6th unit bring? The answer depends on how far price must fall to sell it.", s: {} },
  { cap: "<b>Price of the extra unit: $10</b> on both sides. At the kink the price is the same whichever demand segment you use.", s: { a: 1 } },
  { cap: "<b>Cost of selling more.</b> To sell one more unit the price must fall on <b>every</b> unit. On the flatter segment it falls only $0.80 so the firm loses $4 on its first 5. On the steeper segment it falls $2, so the loss is $10.", s: { a: 1, b: 1 } },
  { cap: "<b>Marginal revenue</b> is the price less this loss: <b>$6</b> on the left and <b>$0</b> on the right. Same price, same output, different slope, so different MR.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>That vertical drop is the gap.</b> A steeper demand curve means a bigger loss on existing sales, and the gap equals output times the difference in slopes: 5 x (2 − 0.8) = $6.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* Watch 3: MC shocks */
const WS = { pt: 1, d1: 1, d2: 1, dl: 0, m1: 1, m2: 1, gap: 1, mc: 1, pm: 1 };
Lib.stepper($("#stC"), { w: 780, h: 425, label: "Marginal cost moving up within the gap, above the gap and down inside the gap", base: { ...WS, c: 5 }, draw: (s) => kinkDraw(BIG, 780, { ...s, ghost: 5 }), tween: 1100, dwell: 5600, steps: [
  { cap: "<b>The starting position.</b> MC passes through the gap at $5 when output is 5 units. The firm charges $10 and sells 5 units.", s: { c: 5 } },
  { cap: "<b>A small cost rise.</b> Imagine ingredient prices drift up so that MC at 5 units is now $5.80. MC still cuts the vertical gap, so output stays at 5 and price stays at <b>$10</b>. Profit per unit falls but the firm does not change its price.", s: { c: 5.8 } },
  { cap: "<b>A large cost rise.</b> A cost shock takes MC at 5 units to $8, above the gap. MC now cuts the upper MR curve at a lower output, so the firm cuts output to about 4.1 units and raises price to about <b>$10.73</b>. If rivals face the same shock they are likely to follow, which would shift the kink.", s: { c: 8 } },
  { cap: "<b>A cost fall.</b> Efficiency savings reduce MC at 5 units to $2. This is still inside the gap, so price stays at <b>$10</b>: the firm keeps the extra margin instead of cutting price into a rival's reaction.", s: { c: 2 } },
  { cap: "<b>Summary.</b> The vertical gap in MR gives MC a range of positions in which the profit-maximising price does not move. Only a shock big enough to leave the gap changes the price.", s: { c: 5 } },
] });

/* ---------- Lab 1 ---------- */
const SC = [
  { n: "Small cost drift", c: 5.8, t: "Ingredient or fuel prices drift up by a few percent: MC rises a little and stays inside the gap." },
  { n: "Industry-wide cost shock", c: 8.5, t: "A sharp rise in a key input, such as cocoa or jet fuel: MC leaves the gap. Because rivals face the same cost they are likely to raise their prices too." },
  { n: "Efficiency saving", c: 2.5, t: "A cheaper way to make each unit: MC falls but stays in the gap, so price is likely to stay at $10 and margin widens." },
  { n: "Head office rent rises", c: 5, t: "A fixed cost: MC does not move at all, so neither price nor output changes (profit falls)." },
];
let lc, ls;
function lab1() {
  const c = lc.get(), s2 = ls.get(), r = solve(c, s2), hi = MR1(KQ), lo = MR2(KQ, s2);
  $("#r1").textContent = "$" + fmtN(r.p, 2); $("#r2").textContent = fmtN(r.q, 2); $("#r3").textContent = "$" + fmtN(c, 2); $("#r4").textContent = "$" + fmtN(lo, 2) + " to $" + fmtN(hi, 2);
  $("#rv").innerHTML = r.where === "in"
    ? `<b>Price stays at $10.</b> MC at 5 units ($${fmtN(c, 2)}) is inside the gap in MR ($${fmtN(lo, 2)} to $${fmtN(hi, 2)}), so MC cuts MR at 5 units. Output stays at 5, whatever MC does inside the gap.`
    : r.where === "above"
      ? `<b>MC has left the gap from above.</b> MC now cuts the upper MR segment, so the firm cuts output to ${fmtN(r.q, 2)} and raises price to $${fmtN(r.p, 2)}. Rivals facing the same costs are likely to follow.`
      : `<b>MC has left the gap from below.</b> MC now cuts the lower MR segment, so output rises to ${fmtN(r.q, 2)} and price falls to $${fmtN(r.p, 2)}. This needs MC to be very low, below the bottom of the gap.`;
  $("#labA").innerHTML = kinkDraw(SMALL, 520, { ...ALL, dl: 0, c, s2, ghost: 5 });
}
ls = Lib.slider($("#g2"), { id: "s2", label: "Rivals' reaction to a price cut (steepness below the kink): ", min: 1, max: 2.4, step: 0.1, value: 2, fmt: (v) => fmtN(v, 1) + "x", onInput: () => lc && lab1() });
lc = Lib.slider($("#g1"), { id: "c5", label: "Marginal cost at 5 units ($): ", min: 0.5, max: 10, step: 0.25, value: 5, fmt: (v) => "$" + fmtN(v, 2), onInput: () => lc && lab1() });
SC.forEach((s) => { const b = document.createElement("button"); b.className = "b"; b.textContent = s.n; b.onclick = () => { lc.set(s.c); ls.set(2); $("#rv").innerHTML += `<br><i>${s.t}</i>`; }; $("#scn").appendChild(b); });
lab1();

/* ---------- Lab 2: test the kink ---------- */
let tp, tf;
const TC = (q) => 5 + 2 * q + 0.3 * q * q;
function lab2() {
  const p = tp.get(), f = tf.get(), up = S1 + (2 - S1) * f;
  const qAt = (x) => (x >= KP ? KQ - (x - KP) / up : KQ + (KP - x) / 2);
  const q = qAt(p), tr = p * q, pi = tr - TC(q), pi0 = KP * KQ - TC(KQ);
  $("#t1").textContent = fmtN(q, 2); $("#t2").textContent = fmtN(tr, 2); $("#t3").textContent = fmtN(pi, 2); $("#t4").textContent = fmtN(pi0, 2);
  const d = pi - pi0;
  $("#tv").innerHTML = Math.abs(p - KP) < 0.01 ? `<b>At the kink.</b> Profit is $${fmtN(pi0, 2)}. Try a higher and a lower price.`
    : d < -0.005 ? `<b>Worse than staying at $10</b> by $${fmtN(-d, 2)}. ${p > KP ? "Customers switch to rivals who did not follow the rise, so the extra price does not make up for the lost sales." : "Rivals match the cut, so few extra sales come in and revenue per unit falls."} The firm is better off at the kink.`
      : `<b>Better than staying at $10</b> by $${fmtN(d, 2)}. ${p > KP ? "Because rivals follow the rise, demand above $10 is less elastic and few customers are lost. There is no real kink, so the firm would raise its price." : "This price beats $10, so the kink does not hold."}`;
  const F = SMALL, { X, Y } = F, qd = Math.min(10, KQ + 10 / 2);
  let o = axes(F, 520);
  const upD = (x) => KP + KQ * up - up * x;   // upper demand with slope 'up'
  o += SV.line(X(0), Y(upD(0)), X(KQ), Y(KP), "c1") + SV.line(X(KQ), Y(KP), X(qd), Y(D2(qd, 2)), "c1");
  o += SV.circle(X(KQ), Y(KP), 6, "dot3") + SV.text(X(KQ) + 10, Y(KP) - 10, "kink", "sm bd t3");
  o += SV.line(F.x0, Y(p), X(q), Y(p), "gr") + SV.line(X(q), Y(p), X(q), Y(0), "gr") + SV.circle(X(q), Y(p), 7, d > 0.005 ? "dot3" : "dot1");
  o += SV.text(X(q) + 12, Y(p) - 10, `price $${fmtN(p, 2)}`, "lbl bd t1", { style: halo });
  o += SV.text(X(0.2), Y(upD(0.2)) - 10, "D", "lbl bd t1", { style: halo });
  $("#labB").innerHTML = o;
}
tf = Lib.slider($("#g4"), { id: "fo", label: "How far rivals follow a price rise: ", min: 0, max: 1, step: 0.05, value: 0, fmt: (v) => Math.round(v * 100) + "%", onInput: () => tp && lab2() });
tp = Lib.slider($("#g3"), { id: "pr", label: "Price charged ($): ", min: 6, max: 13, step: 0.25, value: 11, fmt: (v) => "$" + fmtN(v, 2), onInput: () => tp && lab2() });
lab2();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Place each description on the segment of the kinked demand curve it fits.",
  buckets: [{ label: "Above the kink (price rise)" }, { label: "Below the kink (price cut)" }],
  items: [
    { text: "Rivals do not follow", b: 0 }, { text: "Relatively elastic demand", b: 0 }, { text: "Flatter slope", b: 0 }, { text: "Customers switch to rivals", b: 0 }, { text: "A rise lowers revenue", b: 0 },
    { text: "Rivals match the change", b: 1 }, { text: "Relatively inelastic demand", b: 1 }, { text: "Steeper slope", b: 1 }, { text: "Few extra customers gained", b: 1 }, { text: "A cut lowers revenue", b: 1 },
  ], done: "The same price, two different elasticities: that is the kink.",
});
Lib.classify($("#cl2"), {
  prompt: "Does the change move the marginal cost curve, or is it a fixed cost?",
  buckets: [{ label: "Moves MC" }, { label: "Fixed cost, MC unchanged" }],
  items: [
    { text: "Cocoa price rises for a chocolate maker", b: 0 }, { text: "Jet fuel used per passenger gets dearer", b: 0 }, { text: "Hourly wage rate rises for checkout staff", b: 0 }, { text: "Packaging cost per unit falls", b: 0 }, { text: "Electricity for a production line running longer", b: 0 },
    { text: "Annual rent on a head office rises", b: 1 }, { text: "Insurance premium on the delivery fleet rises", b: 1 }, { text: "A national TV advertising campaign", b: 1 }, { text: "Interest on a loan for a new factory", b: 1 }, { text: "Salaried managers get a pay rise", b: 1 },
  ], done: "Only per-unit (marginal) cost changes can move MC. Fixed costs change profit, never the profit-maximising price.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Kink", "The point on the demand curve at the current price where its slope changes"],
  ["Interdependence", "Each firm's best decision depends on how its rivals react"],
  ["Elastic demand", "Quantity changes by a bigger percentage than price, as above the kink"],
  ["Inelastic demand", "Quantity changes by a smaller percentage than price, as below the kink"],
  ["Gap in MR", "The vertical break in marginal revenue at the kink output"],
  ["Price rigidity", "Price staying the same even when costs change by a little"],
  ["Non-price competition", "Competing through advertising, quality or service instead of price"],
], done: "Seven terms to use in every kinked demand answer." });
Lib.order($("#o1"), { prompt: "Put the explanation of why price is sticky in order.", items: [
  "Firms are interdependent, so each must anticipate how rivals will react",
  "A price rise is not followed by rivals, so demand above P₀ is elastic",
  "A price cut is matched by rivals, so demand below P₀ is inelastic",
  "The slopes differ, so marginal revenue drops vertically at Q₀: a gap in MR",
  "A change in MC that stays inside the gap still cuts MR at Q₀",
  "Output and price stay the same; evaluate the limits of the model",
], done: "This chain works for any question on the kinked demand curve." });

Lib.calc($("#c1"), { qs: [
  { q: "The upper segment is P = 14 − 0.8Q. What output is sold at the kink price of $10?", a: 5, hint: "Solve 10 = 14 − 0.8Q.", sol: "0.8Q = 4, so Q = <b>5</b>." },
  { q: "MR for the upper segment is 14 − 1.6Q. What is MR at 5 units ($)?", a: 6, sol: "14 − 1.6 x 5 = 14 − 8 = <b>$6</b>." },
  { q: "The lower segment is P = 20 − 2Q, so its MR is 20 − 4Q. What is MR at 5 units ($)?", a: 0, sol: "20 − 4 x 5 = <b>$0</b>." },
  { q: "How big is the vertical gap in MR at 5 units ($)?", a: 6, hint: "Subtract the lower MR from the upper MR.", sol: "6 − 0 = <b>$6</b>. Or: 5 x (2 − 0.8) = 6." },
  { q: "MC = 2 + 0.6Q. What is MC at 5 units ($)?", a: 5, sol: "2 + 0.6 x 5 = <b>$5</b>, between $0 and $6, so inside the gap." },
  { q: "What is the highest MC at 5 units ($) that still leaves price at $10?", a: 6, hint: "It is the top of the gap.", sol: "The top of the gap, <b>$6</b>. Above that MC cuts the upper MR curve at a lower output." },
  { q: "Revenue at the kink (price x quantity, $)?", a: 50, sol: "10 x 5 = <b>$50</b>." },
  { q: "The firm raises price to $12 along the upper segment P = 14 − 0.8Q. What is its revenue ($)?", a: 30, hint: "Find Q first: 12 = 14 − 0.8Q.", sol: "Q = 2.5, revenue = 12 x 2.5 = <b>$30</b>, much less than $50." },
  { q: "The firm cuts price to $8 along the lower segment P = 20 − 2Q. What is its revenue ($)?", a: 48, sol: "Q = 6, revenue = 8 x 6 = <b>$48</b>, also less than $50. Neither move pays." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Why is demand relatively elastic above the kink?", opts: ["Rivals match a price rise", "Rivals do not follow a price rise, so customers switch", "The firm is a monopolist", "Demand is perfectly elastic"], a: 1, why: "If rivals keep their prices, a firm that raises its own loses many customers." },
  { q: "The gap in marginal revenue arises because:", opts: ["MC falls at the kink", "total revenue is maximised at the kink", "the two demand segments have different slopes, so MR differs on each side at the kink output", "fixed costs change"], a: 2, why: "A steeper segment has a lower MR at the same output, so MR drops vertically." },
  { q: "At the kink output MR is $6 on the upper segment and $0 on the lower. The MC curve cuts MR at the kink output when MC at that output is:", opts: ["$7", "$3", "−$1", "$6.50"], a: 1, why: "MC must lie between $0 and $6, inside the gap." },
  { q: "A rent rise on the firm's premises is likely to:", opts: ["shift MC upward and raise price", "shift MC downward", "leave MC and the profit-maximising price unchanged", "remove the kink"], a: 2, why: "Rent is a fixed cost. It lowers profit but does not change marginal cost." },
  { q: "Which is a limitation of the kinked demand curve model?", opts: ["It explains how the initial price was set", "It does not explain how the original price was set", "It assumes there are many firms", "It assumes firms are price takers"], a: 1, why: "The model takes P₀ as given and only explains why it might stick." },
  { q: "All airlines on a route face a large jump in jet fuel costs. The model is most likely to:", opts: ["predict no price change", "fail, because rivals are likely to raise fares too", "predict that every airline cuts fares", "predict perfect competition"], a: 1, why: "A common cost shock makes rivals follow a rise, so the upper segment is not elastic." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Kinked demand curve", "An oligopoly model: rivals ignore a price rise but match a cut, so demand is elastic above the current price and inelastic below it."],
  ["Kink", "The point on the demand curve at the current price where the slope changes."],
  ["Interdependence", "Each firm's decisions depend on how rivals respond."],
  ["Gap in MR", "A vertical break in marginal revenue at the kink output, because the two demand segments have different slopes."],
  ["Price rigidity", "Price staying unchanged over long periods, even when costs change a little."],
  ["Marginal cost (MC)", "The extra cost of producing one more unit. Only marginal cost changes move the MC curve."],
  ["Fixed cost", "A cost that does not vary with output (rent, insurance). It does not move MC."],
  ["MC = MR", "The profit-maximising rule. In the gap, MC cuts MR at the kink output."],
  ["Price leadership", "One firm sets the price and the others follow. An alternative explanation of stable oligopoly prices."],
  ["Non-price competition", "Competing on advertising, quality or service rather than price."],
  ["Limit of the model", "It does not explain how the original price was set, and it fails when all firms face the same cost change."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2021 · 31 · Q6] A kinked demand curve is often used when economists analyse oligopolists. What does the kinked demand curve indicate?", opts: ["Oligopolists are unable to achieve profit maximisation.", "Satisficing is the best objective for firms that operate under conditions of oligopoly.", "There are always benefits available for oligopolists if they reduce price, but not if they increase it.", "There is a tendency towards price stability when firms operate under conditions of oligopoly."], a: 3, why: "Rivals match a price cut but ignore a rise, so firms have little incentive to change price." },
  { q: "[Written for this page] On a kinked demand curve diagram, a firm's marginal cost curve shifts upward but still passes through the gap in marginal revenue. What happens to price and output?", opts: ["Price rises and output falls", "Price and output are unchanged", "Price falls and output rises", "Output rises and price is unchanged"], a: 1, why: "MC still cuts MR at the kink output, so the profit-maximising price and output do not change." },
  { q: "[Written for this page] Which statement about marginal revenue on a kinked demand curve is correct?", opts: ["MR is continuous at the kink", "MR is discontinuous at the kink output", "MR is above demand at every output", "MR equals price at every output"], a: 1, why: "The two segments have different slopes, so MR drops vertically at the kink output." },
] });
