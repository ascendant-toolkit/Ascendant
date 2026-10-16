/* ---------- model: P = 100 - Q (AR), MR = 100 - 2Q, MC = 20, fixed cost 400, AC = 20 + 400/Q ---------- */
const PRO = (q) => (100 - q) * q - 20 * q - 400, REV = (q) => (100 - q) * q;
const Q_PM = 40, Q_RM = 50, Q_SM = 40 + Math.sqrt(1200);     // profit, revenue, sales maximisation (AR = AC)
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const AX = (q) => 70 + q * 6.5, AY = (p) => 330 - p * 3.1;
const aAxes = () => SV.line(70, 330, 720, 330) + SV.line(70, 330, 70, 20) + SV.text(720, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price, cost, revenue ($)", "sm");
const acPts = () => { const a = []; for (let q = 8; q <= 100; q += 2) a.push([AX(q), AY(20 + 400 / q)]); return a; };
/* ---------- Watch 2: price discrimination ---------- */
const PX = (ox) => (q) => ox + q * 3.3, PY = (p) => 300 - p * 2.8;
function panel(ox, a, name, s, flag, eq) {
  const X = PX(ox), mq = a / 2, q = (a - 10) / 2, p = a - q;     // MR = a - 2Q = 10
  let o = SV.line(X(0), PY(0), X(90), PY(0)) + SV.line(X(0), PY(0), X(0), PY(95)) + SV.text(X(90), PY(0) + 24, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(X(0) + 6, PY(95) + 4, "Price ($)", "sm");
  o += SV.text(X(45), 18, name, "lbl bd", { "text-anchor": "middle", ...op(s[flag]) });
  if (s[flag] > 0) o += SV.line(X(0), PY(a), X(a), PY(0), "c1", op(s[flag])) + SV.line(X(0), PY(a), X(mq), PY(0), "c4", op(s[flag])) + SV.text(X(a) - 4, PY(0) - 8, "D", "lbl bd t1", { "text-anchor": "end", ...op(s[flag]) }) + SV.text(X(mq) - 4, PY(0) - 8, "MR", "lbl bd t4", { "text-anchor": "end", ...op(s[flag]) });
  if (s.mc > 0) o += SV.line(X(0), PY(10), X(90), PY(10), "c2", op(s.mc)) + SV.text(X(90), PY(10) - 6, "MC = 10", "lbl bd t2", { "text-anchor": "end", ...op(s.mc) });
  if (s[eq] > 0) o += SV.rect(X(0), PY(p), X(q) - X(0), PY(10) - PY(p), "f3", op(s[eq])) + SV.line(X(q), PY(p), X(q), PY(0), "gr", op(s[eq])) + SV.line(X(0), PY(p), X(q), PY(p), "gr", op(s[eq])) + SV.circle(X(q), PY(p), 6, "dot3", op(s[eq])) + SV.text(X(q) + 10, PY(p) - 8, `P = $${p}, Q = ${q}`, "lbl bd t3", op(s[eq])) + SV.text(X(q) / 2 + X(0) / 2, PY(10) - 8 - (PY(10) - PY(p)) / 2 + 12, "profit " + (p - 10) * q, "sm bd t3", { "text-anchor": "middle", ...op(s[eq]) });
  return o;
}
function pdDraw(s) {
  return panel(40, 90, "Market A: adults (inelastic)", s, "a", "ea") + panel(410, 50, "Market B: students (elastic)", s, "b", "eb") + (s.tot > 0 ? SV.text(380, 372, "Total profit with two prices: 1,600 + 400 = 2,000  (best single price: 1,800)", "lbl bd t3", { "text-anchor": "middle", ...op(s.tot) }) : "");
}
Lib.stepper($("#stB"), { w: 760, h: 385, label: "Third degree price discrimination in two markets with the same marginal cost", base: { a: 0, b: 0, mc: 0, ea: 0, eb: 0, tot: 0 }, draw: pdDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Two separate markets.</b> Adults have <b>less elastic</b> demand (they would still pay a high price). The firm can tell the groups apart and they cannot resell.", s: { a: 1, b: 1 } },
  { cap: "<b>Same marginal cost.</b> It costs $10 to serve a customer in either market.", s: { a: 1, b: 1, mc: 1 } },
  { cap: "<b>Market A: MR = MC.</b> Output 40, price <b>$50</b>. Profit = (50 − 10) × 40 = 1,600.", s: { a: 1, b: 1, mc: 1, ea: 1 } },
  { cap: "<b>Market B: MR = MC.</b> Output 20, price <b>$30</b>. Profit = (30 − 10) × 20 = 400. The elastic market gets the lower price.", s: { a: 1, b: 1, mc: 1, ea: 1, eb: 1 } },
  { cap: "<b>The result.</b> Total profit is <b>2,000</b>, more than the best single price (1,800 at $40). Students gain a lower price, adults pay more, and the firm captures more consumer surplus.", s: { a: 1, b: 1, mc: 1, ea: 1, eb: 1, tot: 1 } },
] });

/* ---------- Lab 2: price discrimination ---------- */
function lab2() {
  if (!$("#pd1") || !$("#pd2")) return;
  const pa = +$("#pd1").value, pb = +$("#pd2").value, qa = Math.max(0, 90 - pa), qb = Math.max(0, 50 - pb);
  const prof = (pa - 10) * qa + (pb - 10) * qb, cs = 0.5 * qa * qa + 0.5 * qb * qb;
  $("#s1").textContent = "$" + Lib.fmtN(prof, 0); $("#s2").textContent = "$" + Lib.fmtN(cs, 0); $("#s3").textContent = qa + qb;
  $("#sv").textContent = pa === pb ? `One price for both markets: profit $${Lib.fmtN(prof, 0)}. The best single price is $40 (profit $1,800). Now try different prices.`
    : prof > 1800 ? `Profit $${Lib.fmtN(prof, 0)} beats the best single price ($1,800): discrimination works because the prices follow the elasticities.${Math.abs(prof - 2000) < 1 ? " This is the maximum, $2,000 (adults $50, students $30): MR = MC in both." : ""}`
    : pa < pb ? "You charged the elastic market more than the inelastic one. That lowers profit. Set the higher price where demand is less elastic." : `Profit $${Lib.fmtN(prof, 0)} is below the best single price of $1,800. Move the prices towards $50 and $30.`;
  const H = (v) => 210 - v * 0.09, bw = 70, bars = [[40, 1800, "f1", "Best single price"], [150, prof, prof > 1800 ? "f3" : "f4", "Your prices"], [260, 2000, "f3", "Best two prices"]];
  let o = SV.line(30, 210, 400, 210) + SV.text(32, 24, "Profit ($)", "sm");
  bars.forEach(([x, v, c, l]) => { o += SV.rect(x, H(v), bw, 210 - H(v), c) + SV.text(x + bw / 2, H(v) - 6, Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 228, l, "sm", { "text-anchor": "middle" }); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "pd1", label: "Price in Market A (adults) $: ", min: 10, max: 90, step: 1, value: 40, fmt: (v) => v, onInput: lab2 });
Lib.slider($("#g4"), { id: "pd2", label: "Price in Market B (students) $: ", min: 10, max: 50, step: 1, value: 40, fmt: (v) => v, onInput: lab2 });

/* ---------- Practise ---------- */
Lib.order($("#o1"), { prompt: "Put the explanation of third degree price discrimination in order.", items: [
  "The firm has market power, so it can set its own price",
  "It splits customers into separate markets that cannot resell to each other",
  "The markets have different price elasticities of demand",
  "The firm sets MR = MC in each market",
  "Price is higher in the inelastic market and lower in the elastic market",
  "Evaluate: producer gains consumer surplus, some consumers gain, long-run effects depend on competition",
], done: "A reliable structure for 13 and 20 mark answers." });
Lib.classify($("#cl1"), {
  prompt: "In third degree price discrimination, which market is likely to pay the higher price?",
  buckets: [{ label: "Higher price (inelastic demand)" }, { label: "Lower price (elastic demand)" }],
  items: [
    { text: "Business travellers booking at the last minute", b: 0 }, { text: "Commuters at peak times", b: 0 }, { text: "Customers with few alternatives", b: 0 }, { text: "Buyers for whom the product is a necessity", b: 0 },
    { text: "Students with limited income", b: 1 }, { text: "Leisure travellers who can choose another day", b: 1 }, { text: "Customers with many substitutes", b: 1 }, { text: "Bargain hunters who shop around", b: 1 },
  ], done: "Charge more where demand is inelastic and less where it is elastic.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Price discrimination", "Charging different prices for the same product, not due to cost"],
  ["First degree", "Each buyer pays the most they are willing to pay"],
  ["Second degree", "Price depends on the quantity bought"],
  ["Third degree", "Different prices for different groups or times"],
  ["Separable markets", "The firm can stop buyers moving between the markets"],
  ["Resale", "Buying at the low price to sell at the high price, which would undo the policy"],
  ["Consumer surplus", "What buyers would pay minus what they do pay"],
], done: "Seven words for price discrimination." });
Lib.calc($("#c1"), { qs: [
  { q: "In Market A the price is $50, MC is $10 and output is 40. What is the profit ($)?", a: 1600, sol: "(50 − 10) × 40 = <b>$1,600</b>." },
  { q: "In Market B the price is $30, MC is $10 and output is 20. What is the profit ($)?", a: 400, sol: "(30 − 10) × 20 = <b>$400</b>." },
  { q: "Using the two markets above, how much more profit does price discrimination earn than the best single price of $1,800 ($)?", a: 200, sol: "1,600 + 400 = 2,000. 2,000 − 1,800 = <b>$200</b>." },
  { q: "In the cinema example, adults pay $50 for 40 tickets and the marginal cost is $10. What is the profit from adults ($)?", a: 1600, sol: "(50 − 10) × 40 = <b>$1,600</b>." },
  { q: "Students pay $30 for 20 tickets at a marginal cost of $10. What is their profit ($)?", a: 400, sol: "(30 − 10) × 20 = <b>$400</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which condition is NOT needed for price discrimination?", opts: ["The firm can set its price", "The markets can be separated", "The product is resold between markets", "Price elasticity of demand differs"], a: 2, why: "Resale would remove the price difference, so it must be prevented." },
  { q: "Third degree price discrimination charges a higher price to the group with:", opts: ["more elastic demand", "less elastic demand", "lower income", "more substitutes"], a: 1, why: "A firm can raise the price more where buyers do not respond much." },
  { q: "If buyers could resell the product, price discrimination would:", opts: ["be easier", "break down because buyers would buy at the low price and resell", "raise profit", "make demand more inelastic"], a: 1, why: "The low-price group would supply the high-price group, removing the price difference." },
  { q: "A firm that practises price discrimination will most likely:", opts: ["earn a lower profit than with one price", "earn at least as much profit as with one price", "have to reduce output", "have perfectly elastic demand"], a: 1, why: "If it could not earn at least as much, it would charge one price." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Price discrimination", "Charging different prices for the same product to different groups, not due to cost."],
  ["Third degree price discrimination", "Different prices for different groups or times: higher where demand is inelastic."],
  ["Separable markets", "A condition for price discrimination: the firm can stop buyers moving between markets."],
  ["Price elasticity of demand and price", "The more inelastic the market, the higher the price charged."],
  ["Consumer surplus transfer", "Price discrimination can move surplus from consumers to the firm."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Oct/Nov 2020 · 31 · Q9] What is necessary for price discrimination to be profitable in different markets?", opts: ["There must be many buyers.", "There must be markets with different price elasticities of demand.", "There must be product differentiation.", "There must be geographically separate markets."], a: 1, why: "Different elasticities give a reason for different prices. Markets must be separable, but not necessarily by geography." },
  { q: "[Oct/Nov 2023 · 31 · Q6] What is a key condition for effective price discrimination?", opts: ["The product cannot be resold to another consumer.", "The product must be price inelastic.", "The profits from one market can be used to subsidise another market.", "There are low barriers to entry into the market."], a: 0, why: "Without a ban on resale, buyers in the cheap market could undercut the firm in the dear market." },
  { q: "[Oct/Nov 2022 · 31 · Q10] Which conditions enable price discrimination? (1) The firm can separate the total market into sub-markets. (2) There are different price elasticities of demand in each sub-market. (3) The marginal revenue curve is the same in each separate market.", opts: ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], a: 0, why: "The marginal revenue curves differ because the demand curves differ. 3 is not a condition." },
  { q: "[Oct/Nov 2023 · 33 · Q7] Which condition is necessary for a firm to practise third degree price discrimination effectively?", opts: ["All consumers and producers must be in the same geographical location.", "Customers must be divided into separate markets for the same product.", "Each separate market must have identical price elasticities of demand.", "Price undercutting is required to enter a monopolistic market."], a: 1, why: "Separate markets are essential. Identical elasticities would give no reason to discriminate." },
  { q: "[May/June 2023 · 32 · Q3] What is not necessary for successful price discrimination?", opts: ["ability to separate markets", "different price elasticities of demand in each market", "monopoly power", "price leadership"], a: 3, why: "The firm needs some power to set price (not necessarily a pure monopoly) but price leadership is an oligopoly behaviour and is not a condition." },
  { q: "[Oct/Nov 2024 · 32 · Q7] A bus company has a monopoly and specialises in long-distance travel. It initially sells its tickets to customers one month in advance of the journey. As the departure date approaches, the price of a ticket increases. Which kind of pricing policy does the bus company operate?", opts: ["minimum pricing", "predatory pricing", "price discrimination", "price leadership"], a: 2, why: "The same service is sold at different prices to groups with different elasticities (early and late bookers), not because of cost." },
] });
