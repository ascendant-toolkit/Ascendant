/* ---------- data: pizza (single good) and X, Y (two goods, income $24, Py = $2) ---------- */
const TUp = [0, 20, 36, 48, 56, 60, 60, 56, 48];            // total utility of n slices
const MUp = (n) => TUp[n] - TUp[n - 1];
const MUX = [24, 20, 16, 12, 8, 4], MUY = [15, 12, 9, 6, 3, 1], INC = 24, PY = 2;
const cum = (a) => { let t = [0]; a.forEach((v) => t.push(t[t.length - 1] + v)); return t; };
const CX = cum(MUX), CY = cum(MUY);
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
function best(px) {
  let b = { x: 0, y: 0, tu: -1, spend: 0 };
  for (let x = 0; x <= 6; x++) for (let y = 0; y <= 6; y++) {
    const sp = px * x + PY * y; if (sp > INC) continue;
    const tu = CX[x] + CY[y];
    if (tu > b.tu || (tu === b.tu && sp > b.spend)) b = { x, y, tu, spend: sp };
  }
  return b;
}
const PRICES = [8, 6, 4, 3, 2, 1];

/* ---------- Learn: static TU and MU picture ---------- */
function utPanels(n) {
  const X1 = (k) => 60 + k * 38, Y1 = (v) => 330 - v * 4.2, X2 = (k) => 430 + k * 38, Y2 = (v) => 230 - v * 6.5, N = Math.max(0, Math.min(8, n)), f = Math.floor(N), fr = N - f;
  let o = SV.line(60, 330, 380, 330) + SV.line(60, 330, 60, 70) + SV.text(380, 367, "Slices", "sm", { "text-anchor": "end" }) + SV.text(60, 40, "Total utility", "lbl bd t1");
  o += SV.line(430, 230, 750, 230) + SV.line(430, 100, 430, 300) + SV.text(750, 367, "Slices", "sm", { "text-anchor": "end" }) + SV.text(430, 40, "Marginal utility", "lbl bd t4");
  for (let k = 1; k <= 8; k++) o += SV.text(X1(k), 348, k, "sm", { "text-anchor": "middle" }) + SV.text(X2(k), 330, k, "sm", { "text-anchor": "middle" });
  const pts = [[X1(0), Y1(0)]];
  for (let k = 1; k <= f; k++) pts.push([X1(k), Y1(TUp[k])]);
  if (f < 8 && fr > 0) pts.push([X1(f + fr), Y1(TUp[f] + (TUp[f + 1] - TUp[f]) * fr)]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c1");
  for (let k = 1; k <= f; k++) o += SV.circle(X1(k), Y1(TUp[k]), 5, "dot1");
  for (let k = 1; k <= 8; k++) {
    const v = k <= f ? 1 : k === f + 1 ? fr : 0; if (v <= 0) continue;
    const m = MUp(k), top = Math.min(Y2(m), 230), h = Math.abs(Y2(m) - 230);
    o += SV.rect(X2(k) - 15, top, 30, h, m >= 0 ? "f4" : "f2", op(v)) + SV.text(X2(k), m >= 0 ? top - 6 : top + h + 16, m, "lbl bd", { "text-anchor": "middle", ...op(v) });
  }
  if (N >= 5.9) o += SV.text(380, 58, "TU maximum when MU = 0", "lbl bd t3", { "text-anchor": "end" });
  if (N >= 7) o += SV.text(X1(7.6), Y1(48) + 36, "TU falls", "lbl bd t2", { "text-anchor": "middle" });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 370" role="img" aria-label="Total utility rising then falling and marginal utility falling through zero to negative for slices of pizza">${utPanels(8)}</svg>`;

/* ---------- Watch 1: TU and MU ---------- */
Lib.stepper($("#stA"), { w: 760, h: 370, label: "Building total and marginal utility curves for slices of pizza", base: { n: 0 }, draw: (s) => utPanels(s.n), tween: 1200, dwell: 5200, steps: [
  { cap: "<b>The first slice</b> gives 20 utils. Total utility is 20 and marginal utility is 20.", s: { n: 1 } },
  { cap: "<b>Slices 2 and 3.</b> Total utility rises (36, 48) but marginal utility <b>falls</b> (16, 12). This is the <b>law of diminishing marginal utility</b>.", s: { n: 3 } },
  { cap: "<b>Slices 4 and 5.</b> TU still rises, <b>more slowly</b> (56, 60). MU is small (8, then 4) but still positive.", s: { n: 5 } },
  { cap: "<b>Slice 6.</b> MU = <b>0</b>. Total utility is at its <b>maximum</b> (60). A rational consumer who paid nothing might stop here.", s: { n: 6 } },
  { cap: "<b>Slices 7 and 8.</b> MU is <b>negative</b> (−4, −8) and total utility <b>falls</b>. Too much pizza makes things worse.", s: { n: 8 } },
] });

/* ---------- Watch 2: equi-marginal ---------- */
const ORDER = ["Y", "X", "Y", "X", "Y", "X", "X", "Y"];
const RX = MUX.map((m) => m / 4), RY = MUY.map((m) => m / PY);
function equiDraw(s) {
  const k = Math.round(s.k), bx = ORDER.slice(0, k).filter((c) => c === "X").length, by = k - bx, spent = 4 * bx + 2 * by, H = 28, base = 290;
  let o = SV.line(40, base, 740, base);
  const group = (arr, x0, name, bought, cls) => {
    arr.forEach((v, i) => { const x = x0 + i * 52, isB = i < bought; o += SV.rect(x, base - v * H, 40, v * H, isB ? cls : "ax", isB ? { rx: 3 } : { fill: "none", rx: 3, "stroke-dasharray": "4 3" }) + SV.text(x + 20, base - v * H - 6, Lib.fmtN(v, 1), "sm bd", { "text-anchor": "middle" }) + SV.text(x + 20, base + 16, "#" + (i + 1), "sm", { "text-anchor": "middle" }); });
    o += SV.text(x0 + 130, base + 40, name, "lbl bd", { "text-anchor": "middle" });
  };
  group(RX, 50, "Good X: MUx ÷ $4 (utils per $)", bx, "f1"); group(RY, 410, "Good Y: MUy ÷ $2 (utils per $)", by, "f3");
  o += SV.text(40, 24, `Purchases made: ${k}   ·   X: ${bx}   ·   Y: ${by}   ·   spent $${spent} of $24   ·   total utility ${CX[bx] + CY[by]}`, "lbl bd");
  if (s.l > 0.5) o += SV.line(40, base - 3 * H, 740, base - 3 * H, "gr", { "stroke-dasharray": "6 5" }) + SV.text(390, 46, "Dashed line: 3 utils per $ for the last unit bought of both goods", "sm bd t3", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 345, label: "Spending a budget of $24 on goods X and Y by always buying the unit with the highest utility per dollar", base: { k: 0, l: 0 }, draw: equiDraw, tween: 700, dwell: 5600, steps: [
  { cap: "<b>Utility per dollar</b> for each unit: MU divided by price. Filled bars are bought. Budget $24, X costs $4, Y costs $2. No purchases yet.", s: { k: 0 } },
  { cap: "<b>First two purchases.</b> Y#1 gives 7.5 utils per $, the best. Then X#1 (6.0) and Y#2 (6.0) tie. Spending $8 so far (Y, X, Y).", s: { k: 3 } },
  { cap: "<b>Four purchases in.</b> The next best are X#2 (5.0) and Y#3 (4.5). Utility per dollar of each new purchase keeps <b>falling</b> because MU diminishes.", s: { k: 5 } },
  { cap: "<b>Six purchases.</b> X#3 (4.0). Now the best remaining are X#4 and Y#4, both worth <b>3.0</b> per dollar. Spent $18.", s: { k: 6 } },
  { cap: "<b>Equilibrium.</b> Buy X#4 and Y#4: 4 units of X and 4 of Y, spending exactly $24. The last unit of each gives <b>3 utils per $</b>: MUx/Px = MUy/Py = 3. Total utility is 114, the most possible.", s: { k: 8, l: 1 } },
] });

/* ---------- Watch 3: demand curve ---------- */
const DX = (q) => 90 + q * 100, DYp = (p) => 320 - p * 34;
function demDraw(s) {
  let o = SV.line(90, 320, 700, 320) + SV.line(90, 320, 90, 30) + SV.text(700, 358, "Quantity of X", "sm", { "text-anchor": "end" }) + SV.text(96, 34, "Price of X ($)", "sm");
  for (let q = 0; q <= 6; q++) o += SV.text(DX(q), 338, q, "sm", { "text-anchor": "middle" });
  [0, 2, 4, 6, 8].forEach((p) => { o += SV.text(82, DYp(p) + 4, p, "sm", { "text-anchor": "end" }); });
  const d = s.d, pts = PRICES.map((p) => [DX(best(p).x), DYp(p)]);
  const f = Math.floor(d), fr = d - f, vis = pts.slice(0, f);
  if (vis.length > 1) o += SV.path(Lib.ptsPath(vis), "c1");
  PRICES.forEach((p, i) => { const v = i < f ? 1 : i === f ? fr : 0; if (v > 0) o += SV.circle(DX(best(p).x), DYp(p), 7, "dot1", op(v)) + SV.text(DX(best(p).x) + 12, DYp(p) + 4, `P = $${p}, Q = ${best(p).x}`, "lbl bd t1", op(v)); });
  if (f >= 6) o += SV.text(DX(5.6), DYp(1.1), "Demand curve for X", "lbl bd t1", { "text-anchor": "end" });
  return o;
}
const capD = (i) => { const p = PRICES[i], b = best(p); return `<b>Price of X = $${p}.</b> Best bundle: ${b.x} units of X and ${b.y} of Y (total utility ${b.tu}). Plot the point (Q = ${b.x}, P = $${p}).`; };
Lib.stepper($("#stC"), { w: 760, h: 365, label: "Building the demand curve for X from the best bundle at each price", base: { d: 0 }, draw: demDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>Start.</b> Income $24, Y costs $2. For each price of X, find the bundle with the highest total utility that can be afforded. Each result is one point on the demand curve.", s: { d: 0 } },
  { cap: capD(0) + " The price is high, so utility per dollar of X is low.", s: { d: 1 } },
  { cap: capD(1) + " MUx ÷ Px has risen, so the consumer buys more X.", s: { d: 2 } },
  { cap: capD(2) + " The consumer is at the equilibrium from the previous animation.", s: { d: 3 } },
  { cap: capD(3) + " More X again.", s: { d: 4 } },
  { cap: capD(4) + " The table of MU only goes to 6 units of X, so quantity stops at 6 here.", s: { d: 5 } },
  { cap: capD(5) + " <b>Joining the points gives a downward sloping demand curve.</b> It slopes down because MU diminishes: the consumer only buys more X when it is cheaper. (Flat at the end only because the table stops at 6 units.)", s: { d: 6 } },
] });

/* ---------- Lab 1: pizza ---------- */
function lab1() {
  if (!$("#n1")) return;
  const n = +$("#n1").value, tu = TUp[n], mu = n === 0 ? 0 : MUp(n), au = n === 0 ? 0 : tu / n;
  $("#r1").textContent = tu; $("#r2").textContent = n === 0 ? "–" : mu; $("#r3").textContent = n === 0 ? "–" : Lib.fmtN(au, 1);
  $("#rv").textContent = n === 0 ? "No slices yet. Total utility is zero."
    : mu > 0 ? `MU is positive (${mu}), so total utility is still rising. MU is smaller than for the last slice because of diminishing marginal utility.`
    : mu === 0 ? "MU = 0. Total utility is at its maximum. One more slice adds nothing."
    : `MU is negative (${mu}). Total utility is falling: this slice makes the person worse off.`;
  const X = (k) => 40 + k * 42, Y = (v) => 150 - v * 4;
  let o = SV.line(40, 150, 400, 150) + SV.text(396, 168, "Slices", "sm", { "text-anchor": "end" });
  for (let k = 1; k <= 8; k++) { const m = MUp(k), on = k <= n; o += SV.rect(X(k) - 14, Math.min(Y(m), 150), 28, Math.abs(Y(m) - 150), m >= 0 ? "f4" : "f2", op(on ? 1 : 0.2)) + SV.text(X(k), 266, k, "sm", { "text-anchor": "middle" }); }
  o += SV.text(44, 24, "Bars: marginal utility. Line: total utility (lower).", "sm");
  const base = 262; const ptsT = []; for (let k = 0; k <= n; k++) ptsT.push([X(k), base - TUp[k] * 0.5]);
  if (ptsT.length > 1) o += SV.path(Lib.ptsPath(ptsT), "c1"); if (n > 0) o += SV.circle(X(n), base - TUp[n] * 0.5, 6, "dot1");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "n1", label: "Slices eaten: ", min: 0, max: 8, step: 1, value: 3, fmt: (v) => v, onInput: lab1 });

/* ---------- Lab 2: spend the budget ---------- */
function lab2() {
  if (!$("#bx") || !$("#by")) return;
  const x = +$("#bx").value, y = +$("#by").value, sp = 4 * x + 2 * y, tu = CX[x] + CY[y], ok = sp <= INC;
  const rx = x > 0 ? MUX[x - 1] / 4 : null, ry = y > 0 ? MUY[y - 1] / 2 : null;
  $("#s1").textContent = "$" + sp; $("#s2").textContent = ok ? tu : "over budget"; $("#s3").textContent = (rx === null ? "–" : Lib.fmtN(rx, 1)) + " / " + (ry === null ? "–" : Lib.fmtN(ry, 1));
  $("#sv").textContent = !ok ? `This costs $${sp}, more than your $24. Cut back on X or Y.`
    : tu === 114 ? "This is the best possible bundle (total utility 114). The last unit of each good gives 3 utils per dollar, so MUx/Px = MUy/Py."
    : rx !== null && ry !== null && rx > ry ? `Not the best. The last dollar on X gives ${Lib.fmtN(rx, 1)} utils, on Y only ${Lib.fmtN(ry, 1)}. Switch spending from Y to X.`
    : rx !== null && ry !== null && ry > rx ? `Not the best. The last dollar on Y gives ${Lib.fmtN(ry, 1)} utils, on X only ${Lib.fmtN(rx, 1)}. Switch spending from X to Y.`
    : `Total utility ${tu}. Money is left over or one good is missing: more spending would add utility.`;
  const H = (v) => 200 - v * 22, bw = 60;
  let o = SV.line(20, 200, 400, 200) + SV.text(24, 22, "Utils per $ of the last unit bought", "sm");
  [[50, rx || 0, "f1", "X"], [150, ry || 0, "f3", "Y"]].forEach(([bx, v, c, l]) => { o += SV.rect(bx, H(v), bw, 200 - H(v), c) + SV.text(bx + bw / 2, H(v) - 6, Lib.fmtN(v, 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(bx + bw / 2, 218, l, "sm", { "text-anchor": "middle" }); });
  o += SV.text(260, 70, "Your total utility: " + (ok ? tu : "–"), "lbl bd t1") + SV.text(260, 96, "Best possible: 114", "lbl bd t3") + SV.text(260, 122, "Budget used: $" + sp + " of $24", "sm");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "bx", label: "Units of X ($4 each): ", min: 0, max: 6, step: 1, value: 2, fmt: (v) => v, onInput: lab2 });
Lib.slider($("#g3"), { id: "by", label: "Units of Y ($2 each): ", min: 0, max: 6, step: 1, value: 2, fmt: (v) => v, onInput: lab2 });

/* ---------- Lab 3: change the price of X ---------- */
function lab3() {
  if (!$("#px")) return;
  const p = PRICES[+$("#px").value - 1], b = best(p);
  $("#t1").textContent = `${b.x} X, ${b.y} Y`; $("#t2").textContent = b.tu;
  $("#tv").textContent = `At $${p} the best affordable bundle is ${b.x} units of X and ${b.y} of Y, costing $${b.spend}. A lower price of X means a higher MUx ÷ Px, so more X is bought.`;
  const X = (q) => 50 + q * 55, Y = (pp) => 230 - pp * 24;
  let o = SV.line(50, 230, 400, 230) + SV.line(50, 230, 50, 20) + SV.text(396, 252, "Quantity of X", "sm", { "text-anchor": "end" }) + SV.text(56, 24, "Price of X ($)", "sm");
  const pts = PRICES.map((pp) => [X(best(pp).x), Y(pp)]);
  o += SV.path(Lib.ptsPath(pts), "c1", { opacity: 0.5 });
  PRICES.forEach((pp) => { const q = best(pp).x, cur = pp === p; o += SV.circle(X(q), Y(pp), cur ? 8 : 5, cur ? "dot2" : "dot1") + (cur ? SV.text(X(q) + 12, Y(pp) + 4, `$${pp}, Q = ${q}`, "lbl bd t2") : ""); });
  $("#labC").innerHTML = o;
}
Lib.slider($("#g4"), { id: "px", label: "Price of X ($): ", min: 1, max: 6, step: 1, value: 3, fmt: (v) => PRICES[v - 1], onInput: lab3 });

/* ---------- Lab 4: consumer surplus ---------- */
const WTP = [10, 8, 6, 4, 2];
function lab4() {
  if (!$("#cs1")) return;
  const P = +$("#cs1").value, units = WTP.filter((w) => w >= P).length, sp = units * P, cs = WTP.filter((w) => w >= P).reduce((a, w) => a + (w - P), 0);
  $("#u1").textContent = units; $("#u2").textContent = "$" + sp; $("#u3").textContent = "$" + cs;
  $("#uv").textContent = units === 0 ? `At $${P} the price is above the most the consumer would pay ($10), so nothing is bought.`
    : `The consumer buys every unit worth at least $${P} to them. Consumer surplus is the gap between what they would pay and what they do pay: ${WTP.filter((w) => w >= P).map((w) => w - P).join(" + ")} = $${cs}. A lower price raises it.`;
  const X = (i) => 50 + i * 62, Y = (v) => 220 - v * 18;
  let o = SV.line(50, 220, 400, 220) + SV.line(50, 220, 50, 20) + SV.text(396, 242, "Units", "sm", { "text-anchor": "end" }) + SV.text(56, 12, "Willingness to pay ($)", "sm");
  WTP.forEach((w, i) => { const buy = w >= P; o += SV.rect(X(i), Y(w), 56, 220 - Y(w), "ax", { fill: "none", "stroke-dasharray": "3 3" }); if (buy) o += SV.rect(X(i), Y(P), 56, 220 - Y(P), "f1") + SV.rect(X(i), Y(w), 56, Y(P) - Y(w), "f3"); o += SV.text(X(i) + 28, Y(w) - 5, "$" + w, "sm bd", { "text-anchor": "middle" }) + SV.text(X(i) + 28, 238, i + 1, "sm", { "text-anchor": "middle" }); });
  o += SV.line(50, Y(P), 400, Y(P), "c2") + SV.text(396, Y(P) - 6, "price $" + P, "lbl bd t2", { "text-anchor": "end" });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g5"), { id: "cs1", label: "Market price ($): ", min: 1, max: 11, step: 1, value: 5, fmt: (v) => v, onInput: lab4 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Put each statement in the right bucket.",
  buckets: [{ label: "MU positive: TU rises" }, { label: "MU = 0: TU maximum" }, { label: "MU negative: TU falls" }],
  items: [
    { text: "The 2nd slice adds 16 utils", b: 0 }, { text: "The first sip of water after a run", b: 0 }, { text: "TU rises, but at a decreasing rate", b: 0 },
    { text: "The 6th slice adds nothing", b: 1 }, { text: "The consumer would not pay for another unit", b: 1 }, { text: "The point where TU stops rising", b: 1 },
    { text: "The 7th slice makes the person feel ill", b: 2 }, { text: "TU is falling as more is consumed", b: 2 },
  ], done: "Positive MU: TU rises. Zero MU: TU peaks. Negative MU: TU falls.",
});
Lib.classify($("#cl2"), {
  prompt: "Is each item an assumption of utility theory, or a criticism of it?",
  buckets: [{ label: "Assumption" }, { label: "Criticism" }],
  items: [
    { text: "Consumers aim to maximise utility", b: 0 }, { text: "Consumers have complete information", b: 0 }, { text: "Utility can be measured in utils", b: 0 }, { text: "The marginal utility of money is constant", b: 0 }, { text: "Tastes, income and other prices do not change", b: 0 },
    { text: "People follow habits and are influenced by advertising", b: 1 }, { text: "It cannot explain Giffen goods", b: 1 }, { text: "It is hard to apply to one-off purchases like a house", b: 1 }, { text: "A dollar means more to a poor person than a rich one", b: 1 }, { text: "Satisfaction cannot really be measured in utils", b: 1 },
  ], done: "Assumptions are the starting points; criticisms question whether they hold in reality.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Utility", "The satisfaction a consumer gets from consuming a good"],
  ["Total utility", "All the satisfaction from a given quantity"],
  ["Marginal utility", "The extra satisfaction from one more unit"],
  ["Diminishing marginal utility", "Each extra unit adds less satisfaction than the one before"],
  ["Equi-marginal principle", "Utility is maximised when MU ÷ price is equal across goods"],
  ["Rational consumer", "A consumer who aims to maximise utility"],
  ["Consumer surplus", "The gap between what a consumer is willing to pay and what is paid"],
  ["Bounded rationality", "People use rules of thumb because they cannot process all the information"],
], done: "These eight words cover the chapter." });
Lib.order($("#o1"), { prompt: "Put the derivation of a point on the demand curve in order.", items: [
  "The consumer is in equilibrium: MUx ÷ Px = MUy ÷ Py",
  "The price of X falls",
  "MUx ÷ Px is now greater than MUy ÷ Py",
  "The consumer switches spending towards X, so the quantity of X rises",
  "MUx falls as more X is bought, until the ratios are equal again",
  "Plot the lower price and the higher quantity: a new point on the demand curve",
], done: "Repeat for each price, then add across consumers for the market demand curve." });
Lib.calc($("#c1"), { qs: [
  { q: "Total utility is 36 for 2 units and 48 for 3 units. What is the marginal utility of the 3rd unit?", a: 12, sol: "48 − 36 = <b>12</b>." },
  { q: "The marginal utilities of 4 successive units are 20, 16, 12 and 8. What is the total utility of 4 units?", a: 56, sol: "20 + 16 + 12 + 8 = <b>56</b>." },
  { q: "Total utility from 5 units is 60. What is the average utility?", a: 12, sol: "60 ÷ 5 = <b>12</b>." },
  { q: "MUx is 12 and Px is $4. What is the marginal utility per dollar of X?", a: 3, sol: "12 ÷ 4 = <b>3</b> utils per $." },
  { q: "A consumer is in equilibrium. MUx = 24, Px = $6 and Py = $3. What is MUy?", a: 12, hint: "In equilibrium MUx ÷ Px = MUy ÷ Py.", sol: "24 ÷ 6 = 4. MUy ÷ 3 = 4, so MUy = <b>12</b>." },
  { q: "A consumer would pay $10, $8, $6, $4 and $2 for successive units. The price is $5. What is the consumer surplus ($)?", a: 9, hint: "Buy every unit worth more than the price. Add up (willingness to pay − price).", sol: "Units worth $10, $8, $6: surplus 5 + 3 + 1 = <b>$9</b>." },
  { q: "MUx ÷ Px = 5 and MUy ÷ Py = 3. Should the consumer buy more X or more Y? (type X or Y)", t: ["X"], ph: "X or Y", sol: "The last dollar on X gives 5 utils, on Y only 3, so buy more <b>X</b> (and less Y) until the ratios are equal." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "When marginal utility is zero, total utility is:", opts: ["at its maximum", "at its minimum", "negative", "rising at an increasing rate"], a: 0, why: "Another unit adds nothing, so total utility has stopped rising." },
  { q: "The law of diminishing marginal utility says that as a consumer consumes more of a good:", opts: ["total utility falls at once", "each extra unit adds less utility than the last", "price must fall", "marginal utility rises"], a: 1, why: "MU falls as consumption rises. Total utility can still rise while MU is positive." },
  { q: "A consumer maximises utility when:", opts: ["MUx = MUy", "TUx = TUy", "MUx ÷ Px = MUy ÷ Py", "Px = Py"], a: 2, why: "Equal marginal utility per dollar. Option A ignores prices." },
  { q: "The price of X falls. At the old quantity, MUx ÷ Px is now:", opts: ["lower than MUy ÷ Py", "higher than MUy ÷ Py", "equal to MUy ÷ Py", "zero"], a: 1, why: "The same MU divided by a smaller price is larger, so the consumer buys more X." },
  { q: "Which is a criticism of marginal utility theory?", opts: ["It shows demand slopes downward", "It assumes utility can be measured and that the marginal utility of money is constant", "It uses a budget constraint", "It uses prices"], a: 1, why: "Utility is hard to measure, and a dollar is worth more to a poorer person than to a richer one." },
  { q: "Marginal utility theory cannot explain a Giffen good because it:", opts: ["ignores price", "does not separate income and substitution effects", "assumes no income", "uses indifference curves"], a: 1, why: "A Giffen good needs a strong income effect, which MU theory does not separate out." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Utility", "The satisfaction a consumer gets from consuming a good or service."],
  ["Total utility (TU)", "The total satisfaction from consuming a given quantity of a good."],
  ["Marginal utility (MU)", "The additional satisfaction from consuming one more unit."],
  ["Diminishing marginal utility", "The extra satisfaction from each additional unit falls as consumption rises."],
  ["When MU is zero", "Total utility is at its maximum."],
  ["When MU is negative", "Total utility is falling."],
  ["Util", "An imaginary unit used to measure utility."],
  ["Equi-marginal principle", "Utility is maximised when MU ÷ price is the same for every good."],
  ["Rational consumer", "A consumer who aims to maximise utility given income and prices."],
  ["Cardinal utility", "Utility measured in numbers (utils), as in Marshall's analysis."],
  ["Ordinal utility", "Utility only ranked (more or less), as in indifference curve analysis."],
  ["Consumer surplus", "The difference between what consumers are willing to pay and what they pay."],
  ["Paradox of value", "Water is cheap and diamonds dear because price depends on marginal, not total, utility."],
  ["Bounded rationality", "People use simple rules because they cannot process all information."],
  ["Marginal utility of money", "The extra utility from one more dollar. Assumed constant in simple MU theory."],
] });

/* ---------- Past paper MCQ (text) ---------- */
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2022 · 31 · Q4] What is the central principle of marginal utility theory?", opts: ["As more is consumed of a normal good, the additional satisfaction gained increases.", "Consumers are in equilibrium when the marginal utility gained from good X equals the price of good Y.", "Consumers are in equilibrium when the ratio of the marginal utility of goods X and Y are equal to the ratio of their prices.", "Consumers are in equilibrium when the total utility gained from good X is the same as gained from good Y."], a: 2, why: "MUx ÷ MUy = Px ÷ Py, the same as MUx ÷ Px = MUy ÷ Py." },
  { q: "[Oct/Nov 2022 · 31 · Q4] What is a correct statement of the equi-marginal utility rule?", opts: ["The marginal utility of X must equal the marginal utility of Y.", "The marginal utility of X divided by the price of X must equal the marginal utility of Y divided by the price of Y.", "The marginal utility of X divided by the price of Y must equal the marginal utility of Y divided by the price of Y.", "The price of X must equal the price of Y."], a: 1, why: "Each good's MU is divided by its own price. C mixes up the prices." },
  { q: "[May/June 2024 · 31 · Q1] Which statement about the concept of utility is correct?", opts: ["Diminishing marginal utility means that producers become less efficient the more they produce.", "If marginal utility is above average utility, average utility must be rising.", "The equi-marginal principle says that a consumer gets equal total satisfaction from each item purchased.", "Total utility continually rises as the level of consumption rises."], a: 1, why: "Like any marginal and average pair, if the marginal is above the average, the average rises. A confuses utility with productivity, C mixes up total satisfaction with MU per dollar, D ignores negative MU." },
  { q: "[Oct/Nov 2024 · 32 · Q1] If consumers aim to maximise their utility, how will they arrange their spending?", opts: ["to obtain the same total utility from each commodity", "to obtain the same total utility per $ spent on each commodity", "to obtain the same utility from the last unit of each commodity", "to obtain the same utility from the last $ spent on each commodity"], a: 3, why: "Equal marginal utility per dollar: the last $ on each good gives the same utility." },
  { q: "[May/June 2025 · 31 · Q1] What is the equi-marginal principle?", opts: ["As consumption of a product increases, the satisfaction from consumption of the product decreases by an equal amount.", "Consumers maximise utility where their marginal valuation for each product consumed is the same.", "The total satisfaction received by consumers from consumption of a product is constant.", "The marginal utility derived by consumers from the consumption of one more unit of a product is constant."], a: 1, why: "The marginal valuation per dollar is equalised across products. A and D describe constant MU, which is not the principle." },
  { q: "[Feb/March 2022 · 32 · Q4] How can the concept of marginal utility explain the shape of the downward sloping demand curve?", opts: ["Consumer tastes and preferences only change when their spending power increases.", "Extra utility gained from consuming successive units of a good will fall continuously.", "Satisfaction of consuming one more unit of a good is greater than the loss of money spent.", "Total utility gained from buying more and more units of a good will continue to increase indefinitely."], a: 1, why: "Falling MU means consumers will only buy more at a lower price. C is not about diminishing MU." },
  { q: "[May/June 2020 · 31 · Q4] An individual consumes goods X and Y. The marginal utility of good X is positive and falling. The consumer is at the point where the ratio of the marginal utility of the two goods is equal to the ratio of their prices. What can be concluded?", opts: ["the consumer will continue to consume additional units of X until marginal utility is zero", "the consumer will purchase more of X if the price of Y rises", "total utility will be negative on the additional unit of X consumed", "total utility will be rising at an increasing rate on the additional unit of X consumed"], a: 1, why: "If Py rises, MUy ÷ Py falls below MUx ÷ Px, so the consumer shifts to X. The consumer is in equilibrium, so would not keep consuming X to zero MU." },
  { q: "[Oct/Nov 2023 · 31 · Q1] Economists normally assume that the marginal utility from consuming additional goods is positive and diminishing. What is the effect on total satisfaction of consuming extra units of the good?", opts: ["Total satisfaction falls at a decreasing rate.", "Total satisfaction falls at an increasing rate.", "Total satisfaction rises at a decreasing rate.", "Total satisfaction rises at an increasing rate."], a: 2, why: "Positive MU means TU rises; diminishing MU means it rises more slowly." },
  { q: "[Feb/March 2023 · 32 · Q1] Utility theory is based on the assumption of the 'rational consumer'. What is necessary to act as a 'rational consumer'? (access to complete information / addictive behaviour / choice independent of other consumers)", opts: ["no / yes / yes", "yes / no / no", "yes / yes / no", "yes / no / yes"], a: 3, why: "A rational consumer has full information, is not driven by addiction, and decides independently of others." },
  { q: "[May/June 2021 · 31 · Q5] Which act of purchase or consumption is most likely to illustrate the law of diminishing marginal utility?", opts: ["the final course of an 'eat all you can' banquet to end an evening out", "the last coin to complete an enthusiast's coin collection", "the second of the two rolls of wallpaper needed to decorate a room", "the tenth driving lesson needed to enable a learner to pass the driving test"], a: 0, why: "The last course at a banquet adds little to the diner's satisfaction. B, C and D are cases where the last unit completes a set or a need." },
  { q: "[May/June 2024 · 32 · Q1] A table shows total utility from bottles of water: 1 bottle 30, 2 bottles 40, 3 bottles 48, 4 bottles 54, 5 bottles 58. What can be concluded?", opts: ["Marginal utility increases as consumption increases.", "The consumer cannot switch expenditure to another product to increase total utility.", "The marginal utility of the 3rd unit is 8.", "The marginal utility of the 5th unit is 2."], a: 2, why: "MU of the 3rd unit = 48 − 40 = 8. MU of the 5th is 58 − 54 = 4, and MU falls as consumption rises." },
] });
