/* ---------- model: market D: P = 100 - Q, MC = 20 + 0.5Q. Firm: TC = 600 + 20Q + 0.25Q^2 (AC min at Q = 49, about $44.5) ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const QS = 160 / 3, PS = 140 / 3;                       // allocatively efficient output and price (P = MC)
const QM = 32, PM = 68, MCM = 20 + 0.5 * 32;             // monopoly output, price, marginal cost there
const TSF = (q) => 80 * q - 0.75 * q * q, TSMAX = TSF(QS);
const ACF = (q) => 600 / q + 20 + 0.25 * q, MCF = (q) => 20 + 0.5 * q, QMIN = Math.sqrt(2400), ACMIN = ACF(QMIN);

/* ---------- market diagram (Watch 1 and Learn) ---------- */
const MX = (q) => 70 + q * 6.8, MY = (p) => 330 - p * 3;
const mAxes = () => SV.line(70, 330, 750, 330) + SV.line(70, 330, 70, 20) + SV.text(750, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price and cost ($)", "sm");
function mkt(s) {
  let o = mAxes();
  if (s.sur > 0) o += SV.poly([[MX(0), MY(100)], [MX(0), MY(PS)], [MX(QS), MY(PS)]], "f1", op(s.sur)) + SV.poly([[MX(0), MY(20)], [MX(0), MY(PS)], [MX(QS), MY(PS)]], "f3", op(s.sur)) +
    SV.text(MX(10), MY(66) + 4, "Consumer surplus", "lbl bd t1", op(s.sur)) + SV.text(MX(4), MY(33) + 4, "Producer surplus", "lbl bd t3", op(s.sur));
  if (s.w > 0) o += SV.poly([[MX(QM), MY(PM)], [MX(QM), MY(MCM)], [MX(QS), MY(PS)]], "f2", op(s.w)) + SV.text(MX(QM) + 8, MY(52), "Welfare loss", "lbl bd t2", op(s.w));
  if (s.d > 0) o += SV.line(MX(0), MY(100), MX(100), MY(0), "c1", op(s.d)) + SV.text(MX(100) - 4, MY(0) - 8, "D = MSB", "lbl bd t1", { "text-anchor": "end", ...op(s.d) });
  if (s.c > 0) o += SV.line(MX(0), MY(20), MX(100), MY(70), "c2", op(s.c)) + SV.text(MX(100) - 4, MY(70) - 8, "MC", "lbl bd t2", { "text-anchor": "end", ...op(s.c) });
  if (s.e > 0) o += SV.line(MX(QS), MY(PS), MX(QS), MY(0), "gr", op(s.e)) + SV.line(MX(0), MY(PS), MX(QS), MY(PS), "gr", op(s.e)) + SV.circle(MX(QS), MY(PS), 6, "dot3", op(s.e)) + SV.text(MX(QS), 348, "Q* = 53", "lbl bd", { "text-anchor": "middle", ...op(s.e) }) + SV.text(MX(QS) + 12, MY(PS) + 22, "P = MC: allocatively efficient", "lbl bd t3", op(s.e));
  if (s.m > 0) o += SV.line(MX(0), MY(100), MX(50), MY(0), "c4", op(s.m)) + SV.text(MX(50) - 4, MY(0) - 8, "MR", "lbl bd t4", { "text-anchor": "end", ...op(s.m) }) + SV.line(MX(QM), MY(PM), MX(QM), MY(0), "gr", op(s.m)) + SV.line(MX(0), MY(PM), MX(QM), MY(PM), "gr", op(s.m)) + SV.circle(MX(QM), MY(PM), 6, "dot4", op(s.m)) + SV.text(MX(QM), 348, "32", "lbl bd", { "text-anchor": "middle", ...op(s.m) }) + SV.text(MX(QM) - 8, MY(PM) - 10, "Monopoly: P = 68, Q = 32", "lbl bd t4", { "text-anchor": "end", ...op(s.m) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 780 370" role="img" aria-label="Demand and marginal cost with the efficient output, and the welfare loss if output is restricted to the monopoly level">${mkt({ d: 1, c: 1, e: 1, m: 1, w: 1 })}</svg>`;
Lib.stepper($("#stA"), { w: 780, h: 370, label: "Allocative efficiency, surplus and the welfare loss from a monopoly", base: { d: 0, c: 0, e: 0, sur: 0, m: 0, w: 0 }, draw: mkt, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Demand and marginal cost.</b> Demand shows the marginal social benefit of each unit. The MC curve shows the cost of producing it.", s: { d: 1, c: 1 } },
  { cap: "<b>Allocative efficiency.</b> At Q* = 53, price (the value of the last unit) equals marginal cost. Every unit where benefit exceeds cost has been produced, and no more. <b>P = MC.</b>", s: { d: 1, c: 1, e: 1 } },
  { cap: "<b>Surplus.</b> Consumer surplus (blue) plus producer surplus (green) is the <b>largest possible</b>: 2,133. This is what efficiency means in welfare terms.", s: { d: 1, c: 1, e: 1, sur: 1 } },
  { cap: "<b>A monopolist restricts output.</b> It sets MR = MC, giving Q = 32 and a price of $68, well above the MC of $36. Units between 32 and 53 are worth more to consumers than they cost, but are not produced.", s: { d: 1, c: 1, e: 1, sur: 0.4, m: 1 } },
  { cap: "<b>The welfare loss.</b> The red triangle is the surplus lost on the 21 units not produced: about 341. Price above marginal cost means <b>allocative inefficiency</b>.", s: { d: 1, c: 1, e: 1, sur: 0.25, m: 1, w: 1 } },
] });

/* ---------- Lab 1: welfare loss ---------- */
function lab1() {
  if (!$("#q1")) return;
  const q = +$("#q1").value, p = 100 - q, mc = 20 + 0.5 * q, ts = TSF(q), loss = Math.max(0, TSMAX - ts);
  $("#r1").textContent = "$" + Lib.fmtN(p, 1); $("#r2").textContent = "$" + Lib.fmtN(mc, 1); $("#r3").textContent = Lib.fmtN(ts, 0); $("#r4").textContent = Lib.fmtN(loss, 0);
  $("#rv").textContent = Math.abs(q - QS) < 1 ? "Allocatively efficient: price (the value of the last unit) equals marginal cost. Total surplus is at its maximum, about 2,133."
    : q < QS ? `Underproduction. The last unit is worth $${Lib.fmtN(p, 1)} to consumers but costs only $${Lib.fmtN(mc, 1)}, so more units would add surplus.${q === 32 ? " This is the profit-maximising monopoly output." : ""}`
    : `Overproduction. The last unit costs $${Lib.fmtN(mc, 1)} but is worth only $${Lib.fmtN(p, 1)}, so surplus is wasted.`;
  const X = (v) => 40 + v * 3.6, Y = (v) => 270 - v * 2.5;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "$", "sm");
  o += SV.poly([[X(q), Y(p)], [X(q), Y(mc)], [X(QS), Y(PS)]], "f2");
  o += SV.line(X(0), Y(100), X(100), Y(0), "c1") + SV.line(X(0), Y(20), X(100), Y(70), "c2") + SV.line(X(q), Y(p), X(q), 270, "gr") + SV.circle(X(q), Y(p), 6, "dot1") + SV.circle(X(q), Y(mc), 6, "dot2") + SV.text(X(q), 288, q, "sm bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "q1", label: "Market output: ", min: 10, max: 90, step: 1, value: 40, fmt: (v) => v, onInput: lab1 });


/* ---------- Lab 2: surplus at a price ---------- */
function labSur() {
  if (!$("#pr")) return;
  const p = +$("#pr").value, qd = 100 - p, qs = Math.max(0, 2 * (p - 20)), q = Math.min(qd, qs), cs = 100 * q - q * q / 2 - p * q, ps = p * q - 20 * q - q * q / 4, ts = cs + ps, mx = TSF(QS);
  $("#k1").textContent = Lib.fmtN(q, 1); $("#k2").textContent = Lib.fmtN(cs, 0); $("#k3").textContent = Lib.fmtN(ps, 0); $("#k4").textContent = Lib.fmtN(ts, 0) + " (" + Math.round(ts / mx * 100) + "% of max)";
  $("#kv").textContent = Math.abs(p - PS) < 0.8 ? "At the equilibrium price the quantity traded is 53.3 and total surplus is at its maximum of about " + Lib.fmtN(mx, 0) + ": allocative efficiency."
    : p < PS ? `At $${p} consumers want ${Lib.fmtN(qd, 1)} but firms supply only ${Lib.fmtN(qs, 1)}, so only ${Lib.fmtN(q, 1)} are traded. Total surplus falls to ${Math.round(ts / mx * 100)}% of the maximum: units worth more than they cost are not made.`
    : `At $${p} firms supply ${Lib.fmtN(qs, 1)} but consumers buy only ${Lib.fmtN(qd, 1)}, so only ${Lib.fmtN(q, 1)} are traded. Total surplus falls to ${Math.round(ts / mx * 100)}% of the maximum.`;
  const x = (v) => 40 + v * 3.6, y = (v) => 270 - v * 2.4;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "$", "sm");
  o += SV.poly([[x(0), y(100)], [x(q), y(100 - q)], [x(q), y(p)], [x(0), y(p)]], "f1", { opacity: 0.55 }) + SV.poly([[x(0), y(p)], [x(q), y(p)], [x(q), y(20 + 0.5 * q)], [x(0), y(20)]], "f4", { opacity: 0.55 });
  o += SV.line(x(0), y(100), x(100), y(0), "c1") + SV.line(x(0), y(20), x(100), y(70), "c2") + SV.line(40, y(p), 400, y(p), "gr", { "stroke-width": 2.5 }) + SV.text(x(100) - 4, y(0) - 6, "D", "sm bd t1", { "text-anchor": "end" }) + SV.text(x(100) - 4, y(70) + 16, "S = MC", "sm bd t2", { "text-anchor": "end" });
  o += SV.text(x(q / 4) + 4, y((100 + p) / 2) + 4, "CS", "lbl bd t1", { "text-anchor": "middle" }) + SV.text(x(q / 4) + 4, y((20 + p) / 2) + 4, "PS", "lbl bd t3", { "text-anchor": "middle" });
  $("#labT").innerHTML = o;
}
Lib.slider($("#g9"), { id: "pr", label: "Price ($): ", min: 30, max: 90, step: 1, value: 60, fmt: (v) => v, onInput: labSur });

/* ---------- Practise ---------- */
Lib.order($("#o1"), { prompt: "Put the explanation of why monopoly is allocatively inefficient in order.", items: [
  "The monopolist faces a downward sloping demand curve, so MR is below price",
  "It maximises profit where MR = MC",
  "At that output the price on the demand curve is above marginal cost",
  "Output is lower than the allocatively efficient output (where P = MC)",
  "Units that consumers value more than they cost are not produced, creating a welfare loss",
  "Evaluate: economies of scale or dynamic efficiency may offset the loss, and regulation may reduce it",
], done: "This chain works for a 13 or 20 mark answer." });
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Allocative efficiency", "Resources go to the goods consumers want most: P = MC"],
  ["Consumer surplus", "What consumers would pay minus what they do pay"],
  ["Producer surplus", "What producers receive minus the cost of supplying"],
  ["Total surplus", "Consumer surplus plus producer surplus"],
  ["Welfare loss", "The loss of total surplus when output is not the efficient output"],
  ["Monopoly", "A single seller that can set price above marginal cost"],
  ["Economies of scale", "Average cost falls as output rises"],
], done: "Seven words for allocative efficiency." });
Lib.calc($("#c1"), { qs: [
  { q: "Demand is P = 100 − Q and MC = $20. What output is allocatively efficient?", a: 80, sol: "P = MC: 100 − Q = 20, so Q = <b>80</b>." },
  { q: "A monopolist faces the same demand and MC = $20. What output does it choose?", a: 40, hint: "MR = 100 − 2Q. Set MR = MC.", sol: "100 − 2Q = 20, so Q = <b>40</b>." },
  { q: "What price does the monopolist charge ($)?", a: 60, sol: "P = 100 − 40 = <b>$60</b>." },
  { q: "What is the welfare loss from the monopoly ($)?", a: 800, hint: "Triangle: half × (60 − 20) × (80 − 40).", sol: "½ × 40 × 40 = <b>$800</b>." },
  { q: "Demand is P = 100 − Q and MC = 20 + 0.5Q. What is the allocatively efficient output (units, 1 decimal place)?", a: 53.3, tol: 0.1, sol: "100 − Q = 20 + 0.5Q gives Q = <b>53.3</b>." },
  { q: "A monopolist in that market sets MR = MC, with MR = 100 − 2Q. What output does it produce (units)?", a: 32, sol: "100 − 2Q = 20 + 0.5Q gives 2.5Q = 80, so Q = <b>32</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Allocative efficiency is achieved where:", opts: ["price equals average cost", "price equals marginal cost", "marginal cost is at a minimum", "profit is zero"], a: 1, why: "Price measures the value of the last unit, marginal cost its cost." },
  { q: "Total surplus is greatest where:", opts: ["price equals marginal cost", "profit is greatest", "demand is inelastic", "average cost is rising"], a: 0, why: "At P = MC every unit worth more than it costs is produced." },
  { q: "Compared with perfect competition, a monopoly produces:", opts: ["more output at a lower price", "less output at a higher price", "the same output", "more output at a higher price"], a: 1, why: "It restricts output to raise price." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Welfare loss (deadweight loss)", "The loss of total surplus when output differs from the efficient level."],
  ["Total surplus", "Consumer surplus plus producer surplus."],
  ["Allocative efficiency", "Resources allocated to maximise consumer satisfaction: P = MC (or MSB = MSC)."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2022 · 32 · Q2] What must equal marginal cost when a profit-maximising firm produces at its allocatively efficient output?", opts: ["average revenue", "average total cost", "total revenue", "total cost"], a: 0, why: "Price (average revenue) equals marginal cost at the allocatively efficient output." },
  { q: "[May/June 2025 · 32 · Q2] When is allocative efficiency achieved?", opts: ["when a perfectly competitive market is in equilibrium", "when everybody who needs the product can obtain it", "when firms produce at the lowest possible cost", "when monopolistic firms make normal profits"], a: 0, why: "In a perfectly competitive equilibrium, price equals marginal cost. C describes productive efficiency." },
  { q: "[Oct/Nov 2022 · 32 · Q1] What is most likely to improve the allocative efficiency of a market?", opts: ["a higher market concentration ratio", "collusion between firms in the market", "entry of new firms into the market", "mergers of firms in the market"], a: 2, why: "More firms means more competition, pushing price towards marginal cost." },
] });
