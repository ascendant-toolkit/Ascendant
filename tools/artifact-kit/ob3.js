/* ---------- model: P = 100 - Q (AR), MR = 100 - 2Q, MC = 20, fixed cost 400, AC = 20 + 400/Q ---------- */
const PRO = (q) => (100 - q) * q - 20 * q - 400, REV = (q) => (100 - q) * q;
const Q_PM = 40, Q_RM = 50, Q_SM = 40 + Math.sqrt(1200);     // profit, revenue, sales maximisation (AR = AC)
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const AX = (q) => 70 + q * 6.5, AY = (p) => 330 - p * 3.1;
const aAxes = () => SV.line(70, 330, 720, 330) + SV.line(70, 330, 70, 20) + SV.text(720, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price, cost, revenue ($)", "sm");
const acPts = () => { const a = []; for (let q = 8; q <= 100; q += 2) a.push([AX(q), AY(20 + 400 / q)]); return a; };
/* ---------- Watch 3: limit and predatory pricing ---------- */
const TX = (t) => 70 + t * 63, TY = (p) => 330 - p * 4.4;
function pricePath(pts, c, v) { let o = ""; for (let i = 0; i < pts.length - 1; i++) o += SV.line(TX(pts[i][0]), TY(pts[i][1]), TX(pts[i + 1][0]), TY(pts[i + 1][1]), c, { "stroke-width": 4, ...op(v) }); return o; }
function lpDraw(s) {
  let o = SV.line(70, 330, 710, 330) + SV.line(70, 330, 70, 20) + SV.text(710, 358, "Time", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price ($)", "sm");
  o += SV.line(TX(0), TY(25), TX(10), TY(25), "gr") + SV.text(TX(10) - 4, TY(25) + 16, "Incumbent's average cost $25", "sm", { "text-anchor": "end" });
  o += SV.line(TX(0), TY(40), TX(10), TY(40), "gr", { "stroke-dasharray": "6 5" }) + SV.text(TX(10) - 4, TY(40) - 6, "New entrant's cost $40", "sm", { "text-anchor": "end" });
  if (s.m > 0) o += pricePath([[0, 62.5], [10, 62.5]], "c1", s.m * (1 - 0.65 * Math.max(s.l, s.p))) + SV.text(TX(0) + 6, TY(62.5) - 10, "Monopoly price $62.50", "lbl bd t1", op(s.m * (1 - 0.65 * Math.max(s.l, s.p))));
  if (s.l > 0) o += pricePath([[0, 62.5], [2, 62.5], [2, 38], [10, 38]], "c3", s.l * (1 - 0.7 * s.p)) + SV.text(TX(7.9), TY(38) + 20, "LIMIT PRICE $38: entry deterred", "lbl bd t3", { "text-anchor": "middle", ...op(s.l * (1 - 0.7 * s.p)) });
  if (s.p > 0) o += pricePath([[0, 62.5], [2, 62.5], [2, 15], [5, 15], [5, 62.5], [10, 62.5]], "c2", s.p) + SV.text(TX(3.5), TY(15) + 22, "PREDATORY: below cost", "lbl bd t2", { "text-anchor": "middle", ...op(s.p) }) + SV.text(TX(5) + 8, TY(50), "rival exits, price rises", "lbl bd t2", op(s.p));
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 380, label: "Price over time under limit pricing and predatory pricing", base: { m: 0, l: 0, p: 0 }, draw: lpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>The monopoly price.</b> The incumbent could charge $62.50 (its profit-maximising price). A new firm with unit cost $40 would see big profits and might enter.", s: { m: 1 } },
  { cap: "<b>Limit pricing.</b> The incumbent cuts its price to <b>$38</b>, below the entrant's cost of $40 but above its own cost of $25. It still makes profit and the entrant stays out. Consumers gain now.", s: { m: 1, l: 1 } },
  { cap: "<b>Predatory pricing.</b> A rival is <b>already in</b> the market. The incumbent cuts its price to <b>$15, below its own cost</b>, making a loss to force the rival out. Afterwards it raises the price again.", s: { m: 1, l: 0, p: 1 } },
  { cap: "<b>Compare.</b> Limit pricing: lower prices that last while entry is deterred, and the price could rise later. Predatory pricing: a temporary price war, then high prices once the rival has gone. The second is likely to attract the regulator's attention.", s: { m: 1, l: 1, p: 1 } },
] });

/* ---------- Lab 3: limit pricing ---------- */
function lab3() {
  if (!$("#lp1") || !$("#lp2")) return;
  const P = +$("#lp1").value, c = +$("#lp2").value, enters = P > c, base = (P - 25) * (100 - P), prof = enters ? base / 2 : base;
  const withEntry = 0.5 * 37.5 * 37.5, limit = c >= 25 ? (c - 25) * (100 - c) : 0;
  $("#u1").textContent = enters ? "Yes" : "No"; $("#u2").textContent = "$" + Lib.fmtN(prof, 0); $("#u3").textContent = "$" + P;
  $("#uv").textContent = !enters ? `Price $${P} is at or below the entrant's cost of $${c}, so entry is deterred. The incumbent keeps all sales and earns $${Lib.fmtN(prof, 0)}. Consumers pay a lower price than the $62.50 monopoly price.`
    : `Price $${P} is above the entrant's cost, so a rival enters and the incumbent's sales are halved. ${limit > withEntry ? "A limit price of $" + c + " would earn $" + Lib.fmtN(limit, 0) + ", more than letting entry happen ($" + Lib.fmtN(withEntry, 0) + "), so limit pricing is worthwhile here." : "Here a limit price of $" + c + " would earn only $" + Lib.fmtN(limit, 0) + ", less than the $" + Lib.fmtN(withEntry, 0) + " from the monopoly price with entry, so limit pricing is not worth it."}`;
  const H = (v) => 200 - v * 0.2, bw = 70, bars = [[40, prof, enters ? "f4" : "f3", "Your price"], [150, limit, "f3", "Limit price"], [260, withEntry, "f1", "Monopoly price, entry"]];
  let o = SV.line(30, 200, 400, 200) + SV.text(32, 24, "Incumbent profit ($)", "sm");
  bars.forEach(([x, v, cl, l]) => { o += SV.rect(x, H(v), bw, 200 - H(v), cl) + SV.text(x + bw / 2, H(v) - 6, Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 218, l, "sm", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o;
}
Lib.slider($("#g5"), { id: "lp1", label: "Incumbent's price $: ", min: 25, max: 70, step: 1, value: 62, fmt: (v) => v, onInput: lab3 });
Lib.slider($("#g6"), { id: "lp2", label: "Entrant's unit cost $: ", min: 30, max: 55, step: 1, value: 40, fmt: (v) => v, onInput: lab3 });

/* ---------- Practise ---------- */
Lib.classify($("#cl3"), {
  prompt: "Which pricing policy is each one?",
  buckets: [{ label: "Price discrimination" }, { label: "Limit pricing" }, { label: "Predatory pricing" }, { label: "Cost-plus pricing" }],
  items: [
    { text: "A cinema charges adults more than students for the same film", b: 0 }, { text: "An airline charges more for last-minute seats", b: 0 },
    { text: "The incumbent prices near its average cost so entrants see only normal profit", b: 1 }, { text: "A low price set just below what a newcomer needs to make a profit", b: 1 },
    { text: "Selling below cost for a year to force a rival to close, then raising prices", b: 2 }, { text: "A price below unit cost aimed at a firm already in the market", b: 2 },
    { text: "Unit cost plus 25%", b: 3 }, { text: "A builder quotes cost plus a fixed percentage", b: 3 },
  ], done: "Limit = stop entry (price near cost). Predatory = push out rivals (price below cost).",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Limit pricing", "A price below the monopoly price set to deter new entrants"],
  ["Predatory pricing", "A price below cost set to force an existing rival out"],
  ["Cost-plus pricing", "Price set by adding a percentage mark-up to unit cost"],
  ["Barrier to entry", "Something that makes it hard for new firms to join a market"],
  ["Contestable market", "A market where entry and exit are easy and cheap"],
  ["Price leadership", "One firm sets a price that rivals follow"],
  ["Incumbent", "A firm that is already in the market"],
], done: "Seven words for pricing policies." });
Lib.calc($("#c1"), { qs: [
  { q: "A firm uses cost-plus pricing with a 25% mark-up. Unit cost is $40. What is the price ($)?", a: 50, sol: "40 × 1.25 = <b>$50</b>." },
  { q: "An incumbent has MC = $25 and demand P = 100 − Q. It cuts its price to a limit price of $40. How many units does it sell?", a: 60, sol: "Q = 100 − 40 = <b>60</b>." },
  { q: "What is its profit at the limit price of $40 ($)?", a: 900, sol: "(40 − 25) × 60 = <b>$900</b>." },
  { q: "If it keeps the monopoly price, profit is about $1,406 but a rival enters and sales halve. What is the profit after entry ($, nearest whole number)?", a: 703, tol: 1, sol: "1,406 ÷ 2 = <b>$703</b>, less than the $900 from limit pricing." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A firm sells below cost to force an existing rival out of the market. This is:", opts: ["limit pricing", "predatory pricing", "price discrimination", "cost-plus pricing"], a: 1, why: "Below-cost pricing against a firm already in the market is predatory." },
  { q: "Limit pricing is mainly aimed at:", opts: ["existing rivals", "new entrants", "customers", "suppliers"], a: 1, why: "It makes entry look unprofitable." },
  { q: "Predatory pricing involves setting price:", opts: ["below the profit-maximising price but above average cost", "below average cost to force a rival out", "equal to marginal cost", "above the monopoly price"], a: 1, why: "The aim is to drive an existing rival out, even at a loss." },
  { q: "Compared with predatory pricing, limit pricing usually:", opts: ["involves selling at a loss", "keeps price near normal profit and does not involve a loss", "has no effect on entry", "is always illegal"], a: 1, why: "The incumbent still earns at least normal profit." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Limit pricing", "A price set below the monopoly price to deter new entrants."],
  ["Predatory pricing", "A price below cost to force existing rivals out of the market."],
  ["Cost-plus pricing", "Price set by adding a percentage mark-up to unit cost."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2020 (not sat) · 32 · Q4] Four bus companies control more than two-thirds of the market in a country. Critics claim that these companies fix prices on some routes to maximise revenue whilst lowering prices on other routes to stop smaller competitors entering the market. Which anti-competitive practices are these companies accused of?", opts: ["collusion and limit pricing", "collusion and price leadership", "limit pricing and price discrimination", "price leadership and x-inefficiency"], a: 0, why: "Fixing prices together is collusion, and lowering prices to keep smaller firms out is limit pricing." },
  { q: "[Oct/Nov 2020 · 31 · Q11] A firm successfully engages in a policy of predatory pricing. What will happen to the prices charged by the firm in the short run and in the long run?", opts: ["rise, rise", "rise, fall", "fall, rise", "fall, fall"], a: 2, why: "Price falls to drive rivals out, then rises once they have left." },
  { q: "[May/June 2024 · 31 · Q7] Which assumption is essential for a market to be contestable?", opts: ["The market is supplied by a large number of firms.", "Firms are free to enter and leave the market.", "Firms cannot earn abnormal profits in the short run.", "Firms produce differentiated goods."], a: 1, why: "Freedom of entry and exit is what makes the threat of new entrants real." },
  { q: "[Oct/Nov 2024 · 33 · Q6] In a perfectly contestable market, entries and exits are cost-free. In reality, why is this not the case with some firms in contestable markets?", opts: ["Firms cannot recover all fixed costs if they cease operations.", "Firms in the industry all operate at the equilibrium level of output.", "Large firms do not have to increase capital to grow.", "Multinational companies always benefit from economies of scale."], a: 0, why: "Sunk costs that cannot be recovered make exit costly." },
] });
