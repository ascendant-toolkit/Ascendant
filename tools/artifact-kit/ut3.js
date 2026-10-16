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

Lib.classify($("#cl2"), {
  prompt: "Is each item an assumption of utility theory, or a criticism of it?",
  buckets: [{ label: "Assumption" }, { label: "Criticism" }],
  items: [
    { text: "Consumers aim to maximise utility", b: 0 }, { text: "Consumers have complete information", b: 0 }, { text: "Utility can be measured in utils", b: 0 }, { text: "The marginal utility of money is constant", b: 0 }, { text: "Tastes, income and other prices do not change", b: 0 },
    { text: "People follow habits and are influenced by advertising", b: 1 }, { text: "It cannot explain Giffen goods", b: 1 }, { text: "It is hard to apply to one-off purchases like a house", b: 1 }, { text: "A dollar means more to a poor person than a rich one", b: 1 }, { text: "Satisfaction cannot really be measured in utils", b: 1 },
  ], done: "Assumptions are the starting points; criticisms question whether they hold in reality.",
});
Lib.order($("#o1"), { prompt: "Put the derivation of a point on the demand curve in order.", items: [
  "The consumer is in equilibrium: MUx ÷ Px = MUy ÷ Py",
  "The price of X falls",
  "MUx ÷ Px is now greater than MUy ÷ Py",
  "The consumer switches spending towards X, so the quantity of X rises",
  "MUx falls as more X is bought, until the ratios are equal again",
  "Plot the lower price and the higher quantity: a new point on the demand curve",
], done: "Repeat for each price, then add across consumers for the market demand curve." });
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Individual demand curve", "Price plotted against the quantity one consumer buys at each equilibrium"],
  ["Market demand curve", "The sum of all individual demand curves"],
  ["Consumer surplus", "The gap between what a consumer is willing to pay and what is paid"],
  ["Cardinal utility", "Utility measured in numbers (utils), as in Marshall's analysis"],
  ["Ordinal utility", "Utility only ranked (more or less), as in indifference curve analysis"],
  ["Bounded rationality", "People use rules of thumb because they cannot process all the information"],
  ["Marginal utility of money", "The extra utility from one more dollar, assumed constant"],
], done: "Seven words for demand and evaluation." });
Lib.calc($("#c1"), { qs: [
  { q: "A consumer would pay $10, $8, $6, $4 and $2 for successive units. The price is $5. What is the consumer surplus ($)?", a: 9, hint: "Buy every unit worth more than the price. Add up (willingness to pay − price).", sol: "Units worth $10, $8, $6: surplus 5 + 3 + 1 = <b>$9</b>." },
  { q: "A consumer would pay $10, $8, $6, $4 and $2 for successive units. The price falls from $5 to $3. How many units are bought at $3?", a: 4, sol: "Buy every unit worth more than $3: $10, $8, $6 and $4, so <b>4 units</b>." },
  { q: "What is the consumer surplus at a price of $3 ($)?", a: 16, sol: "(10 − 3) + (8 − 3) + (6 − 3) + (4 − 3) = 7 + 5 + 3 + 1 = <b>$16</b>." },
  { q: "Using MU analysis, a consumer buys 3 units at $5 and 4 units at $3. What are the two points on the demand curve? Give the quantity at the lower price.", a: 4, sol: "(Q = 3, P = $5) and (Q = 4, P = $3): the quantity at $3 is <b>4</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The price of X falls. At the old quantity, MUx ÷ Px is now:", opts: ["lower than MUy ÷ Py", "higher than MUy ÷ Py", "equal to MUy ÷ Py", "zero"], a: 1, why: "The same MU divided by a smaller price is larger, so the consumer buys more X." },
  { q: "Which is a criticism of marginal utility theory?", opts: ["It shows demand slopes downward", "It assumes utility can be measured and that the marginal utility of money is constant", "It uses a budget constraint", "It uses prices"], a: 1, why: "Utility is hard to measure, and a dollar is worth more to a poorer person than to a richer one." },
  { q: "Marginal utility theory cannot explain a Giffen good because it:", opts: ["ignores price", "does not separate income and substitution effects", "assumes no income", "uses indifference curves"], a: 1, why: "A Giffen good needs a strong income effect, which MU theory does not separate out." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Cardinal utility", "Utility measured in numbers (utils), as in Marshall's analysis."],
  ["Ordinal utility", "Utility only ranked (more or less), as in indifference curve analysis."],
  ["Consumer surplus", "The difference between what consumers are willing to pay and what they pay."],
  ["Bounded rationality", "People use simple rules because they cannot process all information."],
  ["Individual demand curve", "Price against quantity for one consumer, from equilibrium at each price."],
  ["Market demand curve", "The horizontal sum of individual demand curves."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2022 · 32 · Q4] How can the concept of marginal utility explain the shape of the downward sloping demand curve?", opts: ["Consumer tastes and preferences only change when their spending power increases.", "Extra utility gained from consuming successive units of a good will fall continuously.", "Satisfaction of consuming one more unit of a good is greater than the loss of money spent.", "Total utility gained from buying more and more units of a good will continue to increase indefinitely."], a: 1, why: "Falling MU means consumers will only buy more at a lower price. C is not about diminishing MU." },
  { q: "[Feb/March 2023 · 32 · Q1] Utility theory is based on the assumption of the 'rational consumer'. What is necessary to act as a 'rational consumer'? (access to complete information / addictive behaviour / choice independent of other consumers)", opts: ["no / yes / yes", "yes / no / no", "yes / yes / no", "yes / no / yes"], a: 3, why: "A rational consumer has full information, is not driven by addiction, and decides independently of others." },
] });
