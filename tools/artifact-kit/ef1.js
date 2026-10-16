/* ---------- model: market D: P = 100 - Q, MC = 20 + 0.5Q. Firm: TC = 600 + 20Q + 0.25Q^2 (AC min at Q = 49, about $44.5) ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const QS = 160 / 3, PS = 140 / 3;                       // allocatively efficient output and price (P = MC)
const QM = 32, PM = 68, MCM = 20 + 0.5 * 32;             // monopoly output, price, marginal cost there
const TSF = (q) => 80 * q - 0.75 * q * q, TSMAX = TSF(QS);
const ACF = (q) => 600 / q + 20 + 0.25 * q, MCF = (q) => 20 + 0.5 * q, QMIN = Math.sqrt(2400), ACMIN = ACF(QMIN);

/* ---------- Watch 2: perfect competition vs monopoly (one firm) ---------- */
const FX = (q) => 70 + q * 8.2, FY = (p) => 330 - p * 3.6;
function firmDraw(s) {
  let o = SV.line(70, 330, 730, 330) + SV.line(70, 330, 70, 20) + SV.text(730, 358, "Output of the firm", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price and cost ($)", "sm");
  const pts = []; for (let q = 9; q <= 80; q += 1) { const a = ACF(q); if (a < 88) pts.push([FX(q), FY(a)]); }
  if (s.ac > 0) o += SV.path(Lib.ptsPath(pts), "c3", op(s.ac)) + SV.text(FX(78), FY(ACF(78)) - 10, "AC", "lbl bd t3", { "text-anchor": "end", ...op(s.ac) });
  if (s.mc > 0) o += SV.line(FX(0), FY(20), FX(80), FY(60), "c2", op(s.mc)) + SV.text(FX(80) - 4, FY(60) + 18, "MC", "lbl bd t2", { "text-anchor": "end", ...op(s.mc) });
  if (s.min > 0) o += SV.circle(FX(QMIN), FY(ACMIN), 6, "dot3", op(s.min)) + SV.line(FX(QMIN), FY(ACMIN), FX(QMIN), 330, "gr", op(s.min)) + SV.text(FX(QMIN), 348, "49", "lbl bd", { "text-anchor": "middle", ...op(s.min) }) + SV.text(725, FY(ACMIN) + 50, "Minimum AC $44.5: productively efficient", "lbl bd t3", { "text-anchor": "end", ...op(s.min) });
  if (s.pc > 0) o += SV.line(FX(0), FY(ACMIN), FX(80), FY(ACMIN), "c1", op(s.pc)) + SV.text(FX(1), FY(ACMIN) - 10, "Perfect competition: P = AR = MR = $44.5", "lbl bd t1", op(s.pc));
  if (s.mon > 0) {
    o += SV.poly([[FX(0), FY(PM)], [FX(QM), FY(PM)], [FX(QM), FY(ACF(QM))], [FX(0), FY(ACF(QM))]], "f3", op(s.mon * 0.8)) + SV.line(FX(0), FY(100), FX(80), FY(20), "c1", op(s.mon)) + SV.text(FX(80) - 4, FY(20) - 10, "D = AR", "lbl bd t1", { "text-anchor": "end", ...op(s.mon) }) +
      SV.line(FX(0), FY(100), FX(50), FY(0), "c4", op(s.mon)) + SV.text(FX(50) - 4, FY(0) - 8, "MR", "lbl bd t4", { "text-anchor": "end", ...op(s.mon) }) + SV.circle(FX(QM), FY(PM), 6, "dot4", op(s.mon)) + SV.line(FX(QM), FY(PM), FX(QM), 330, "gr", op(s.mon)) + SV.text(FX(QM), 348, "32", "lbl bd", { "text-anchor": "middle", ...op(s.mon) }) +
      SV.text(FX(QM) - 8, FY(PM) - 10, "Monopoly P = 68", "lbl bd t4", { "text-anchor": "end", ...op(s.mon) }) + SV.text(FX(2), FY(57), "supernormal profit", "sm bd t3", op(s.mon)) + SV.circle(FX(QM), FY(MCF(QM)), 5, "dot2", op(s.mon)) + SV.text(FX(QM) + 10, FY(MCF(QM)) + 18, "MC = 36", "lbl bd t2", op(s.mon));
  }
  if (s.al > 0) o += SV.circle(FX(QS), FY(PS), 6, "dot3", op(s.al)) + SV.text(725, FY(PS) - 44, "Allocatively efficient: Q = 53", "lbl bd t3", { "text-anchor": "end", ...op(s.al) });
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 375, label: "One firm's cost curves, with perfect competition and monopoly compared for efficiency", base: { ac: 0, mc: 0, min: 0, pc: 0, mon: 0, al: 0 }, draw: firmDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Productive efficiency.</b> Average cost is U-shaped. MC cuts AC at its minimum, at output 49 and a cost of $44.5. Producing there uses the fewest resources per unit.", s: { ac: 1, mc: 1, min: 1 } },
  { cap: "<b>Perfect competition, long run.</b> Free entry removes supernormal profit, so the price is pushed down to the minimum AC of $44.5. The firm sets MR = MC at Q = 49: <b>P = MC</b> (allocative) and <b>P = min AC</b> (productive).", s: { ac: 1, mc: 1, min: 1, pc: 1 } },
  { cap: "<b>Monopoly.</b> Now demand slopes down. The firm sets MR = MC at output <b>32</b> and charges <b>$68</b> from the demand curve. The price is well above MC ($36) and above AC ($46.75), so it earns <b>supernormal profit</b> (shaded).", s: { ac: 1, mc: 1, min: 1, pc: 0.3, mon: 1 } },
  { cap: "<b>Comparison.</b> The monopoly produces <b>less than the allocatively efficient output</b> (53) and on a point <b>above the minimum AC</b> (output 32 is below 49). It fails both tests. But the supernormal profit might fund <b>dynamic efficiency</b>, and the risk is X-inefficiency.", s: { ac: 1, mc: 1, min: 1, pc: 0.3, mon: 1, al: 1 } },
] });

/* ---------- Watch 3: PPC and Pareto improvement ---------- */
const PX = (x) => 60 + x * 6, PYv = (y) => 330 - y * 2.9, ppc = (x) => 100 * Math.sqrt(Math.max(0, 1 - (x / 100) ** 2));
function ppcDraw(s) {
  let o = SV.line(60, 330, 680, 330) + SV.line(60, 330, 60, 30) + SV.text(680, 356, "Good X", "sm", { "text-anchor": "end" }) + SV.text(66, 34, "Good Y", "sm");
  const arc = (a, b) => { const p = []; for (let x = a; x <= b + 0.01; x += 1) p.push([PX(x), PYv(ppc(x))]); return p; };
  o += SV.path(Lib.ptsPath(arc(0, 100)), "c1") + SV.text(PX(88), PYv(ppc(88)) - 14, "PPC", "lbl bd t1", {});
  const I = { x: 40, y: 55 }, x2 = Math.sqrt(10000 - 55 * 55), y1 = ppc(40);
  if (s.imp > 0) o += SV.poly([[PX(40), PYv(55)], [PX(40), PYv(y1)], ...arc(40, x2), [PX(x2), PYv(55)]], "f3", op(s.imp)) + SV.text(PX(52), PYv(64), "Pareto improvements", "lbl bd t3", { "text-anchor": "middle", ...op(s.imp) });
  if (s.i > 0) o += SV.circle(PX(I.x), PYv(I.y), 7, "dot2", op(s.i)) + SV.text(PX(I.x) - 12, PYv(I.y) + 22, "Inside the PPC: productively inefficient", "lbl bd t2", { "text-anchor": "start", ...op(s.i) });
  if (s.e > 0) o += SV.circle(PX(60), PYv(80), 7, "dot3", op(s.e)) + SV.text(PX(60) + 12, PYv(80) - 10, "E: on the PPC", "lbl bd t3", op(s.e));
  if (s.p3 > 0) o += SV.circle(PX(80), PYv(60), 7, "dot4", op(s.p3)) + SV.text(PX(80) + 12, PYv(60) - 10, "F: also on the PPC", "lbl bd t4", op(s.p3)) + SV.line(PX(60), PYv(80), PX(80), PYv(60), "c4", { "stroke-dasharray": "5 4", ...op(s.p3) });
  return o;
}
Lib.stepper($("#stC"), { w: 740, h: 375, label: "Production possibility curve showing a point inside the curve, Pareto improvements and points on the curve", base: { imp: 0, i: 0, e: 0, p3: 0 }, draw: ppcDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The production possibility curve (PPC)</b> shows the most the economy can produce with its resources. Points <b>on</b> it are productively efficient.", s: {} },
  { cap: "<b>A point inside the PPC.</b> Resources are unemployed or wasted, so the economy is productively inefficient and not Pareto efficient.", s: { i: 1 } },
  { cap: "<b>Pareto improvements.</b> Any move into the green area gives <b>more of at least one good and less of none</b>, so someone gains and no one loses.", s: { i: 1, imp: 1 } },
  { cap: "<b>Point E on the PPC.</b> Moving from inside to E is a Pareto improvement. At E, producing more of one good means producing less of the other.", s: { i: 1, imp: 1, e: 1 } },
  { cap: "<b>Moving along the PPC to F.</b> More X but less Y, so some people gain and others lose: <b>not a Pareto improvement</b>. Only one point on the PPC, where marginal social benefit equals marginal cost (the mix society values most), is also <b>allocatively efficient</b>. Pareto efficiency needs both.", s: { i: 0.5, imp: 0.4, e: 1, p3: 1 } },
] });

/* ---------- Lab 2: productive efficiency and X-inefficiency ---------- */
function lab2() {
  if (!$("#f1") || !$("#f2")) return;
  const q = +$("#f1").value, sl = +$("#f2").value / 100, ac = ACF(q) * (1 + sl), waste = ac - ACMIN;
  $("#s1").textContent = "$" + Lib.fmtN(ac, 1); $("#s2").textContent = "$" + Lib.fmtN(ACMIN, 1); $("#s3").textContent = "$" + Lib.fmtN(waste, 1);
  $("#sv").textContent = sl > 0 && waste > 0.5 ? `Cost is $${Lib.fmtN(waste, 1)} a unit above the minimum possible. Part of this is the scale of output (${q < 45 ? "below" : q > 53 ? "above" : "near"} the minimum efficient scale) and ${Math.round(sl * 100)}% is X-inefficiency: costs higher than they need to be because there is little pressure from competitors.`
    : waste < 0.5 ? "The firm is productively efficient: at the minimum of the average cost curve, with no X-inefficiency." : `Cost is $${Lib.fmtN(waste, 1)} a unit above the minimum possible, because output (${q}) is ${q < QMIN ? "below" : "above"} the cost-minimising level of 49. Moving towards 49 cuts average cost.`;
  const X = (v) => 40 + v * 3.6, Y = (v) => 270 - v * 2.4, pts = [], pts2 = [];
  for (let v = 9; v <= 100; v += 1) { const a = ACF(v); if (a < 100) pts.push([X(v), Y(a)]); const b = a * (1 + sl); if (b < 100) pts2.push([X(v), Y(b)]); }
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Output", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "$ per unit", "sm");
  o += SV.path(Lib.ptsPath(pts), "c3", { opacity: sl > 0 ? 0.4 : 1 }) + (sl > 0 ? SV.path(Lib.ptsPath(pts2), "c2") : "") + SV.line(X(0), Y(20), X(100), Y(70), "c4", { opacity: 0.6 }) + SV.line(40, Y(ACMIN), X(100), Y(ACMIN), "gr");
  o += SV.circle(X(q), Y(ac), 7, "dot2") + SV.text(X(QMIN), 288, "49", "sm bd", { "text-anchor": "middle" }) + SV.text(X(100) - 4, Y(ACMIN) - 6, "lowest possible AC", "sm", { "text-anchor": "end" });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "f1", label: "Firm's output: ", min: 10, max: 100, step: 1, value: 30, fmt: (v) => v, onInput: lab2 });
Lib.slider($("#g3"), { id: "f2", label: "X-inefficiency (extra cost): ", min: 0, max: 30, step: 1, value: 0, fmt: (v) => v + "%", onInput: lab2 });

/* ---------- Lab 3: dynamic efficiency ---------- */
function lab3() {
  if (!$("#rd")) return;
  const s = +$("#rd").value / 100, rate = 0.15 * s, c10 = 40 * (1 - rate) ** 10;
  $("#t1").textContent = "$" + Lib.fmtN(c10, 1); $("#t2").textContent = Lib.fmtN(((40 - c10) / 40) * 100, 0) + "%";
  $("#tv").textContent = s === 0 ? "No reinvestment: unit cost stays at $40. The firm may be productively efficient today but has no dynamic efficiency."
    : `Reinvesting ${Math.round(s * 100)}% of profit cuts unit cost by about ${Lib.fmtN(rate * 100, 1)}% a year. After 10 years the whole average cost curve has shifted down to $${Lib.fmtN(c10, 1)}. This is dynamic efficiency, and the lower costs could be passed on in lower prices.`;
  const X = (y) => 50 + y * 33, Y = (c) => 240 - c * 5, pts = []; for (let y = 0; y <= 10; y++) pts.push([X(y), Y(40 * (1 - rate) ** y)]);
  let o = SV.line(50, 240, 390, 240) + SV.line(50, 240, 50, 20) + SV.text(386, 272, "Years", "sm", { "text-anchor": "end" }) + SV.text(56, 24, "Unit cost ($)", "sm");
  o += SV.line(X(0), Y(40), X(10), Y(40), "gr", { "stroke-width": 3 }) + SV.text(X(10), Y(40) - 8, "no R&D", "sm", { "text-anchor": "end" }) + SV.path(Lib.ptsPath(pts), "c3") + SV.text(X(10), Y(40 * (1 - rate) ** 10) - 8, "with R&D", "lbl bd t3", { "text-anchor": "end" });
  for (let y = 0; y <= 10; y += 2) o += SV.text(X(y), 256, y, "sm", { "text-anchor": "middle" });
  $("#labC").innerHTML = o;
}
Lib.slider($("#g4"), { id: "rd", label: "Share of profit reinvested in R&D: ", min: 0, max: 50, step: 5, value: 20, fmt: (v) => v + "%", onInput: lab3 });


/* ---------- Lab 3: Pareto test ---------- */
function labPar() {
  if (!$("#da") || !$("#db")) return;
  const a = +$("#da").value, b = +$("#db").value, t = a + b, imp = a >= 0 && b >= 0 && (a > 0 || b > 0);
  $("#p1").textContent = (a > 0 ? "+" : a < 0 ? "−" : "") + Math.abs(a); $("#p2").textContent = (b > 0 ? "+" : b < 0 ? "−" : "") + Math.abs(b); $("#p3").textContent = (t > 0 ? "+" : t < 0 ? "−" : "") + Math.abs(t); $("#p4").textContent = imp ? "Yes" : a === 0 && b === 0 ? "No change" : "No";
  $("#pv").textContent = a === 0 && b === 0 ? "Nothing changes, so the allocation is unchanged."
    : imp ? "Nobody is worse off and at least one person is better off: this is a Pareto improvement."
    : t > 0 ? "One person loses, so it is not a Pareto improvement, even though the total gain is positive. If the winner compensated the loser and still gained, it might count as a potential Pareto improvement."
    : "One person loses and the total is not positive: society is no better off.";
  const H = (v) => 7 * v, base = 130;
  let o = SV.line(30, base, 400, base);
  [[80, a, "Person A"], [240, b, "Person B"]].forEach(([x, v, l]) => { const up = v >= 0; o += SV.rect(x, up ? base - H(v) : base, 90, Math.abs(H(v)), up ? "f3" : "f2") + SV.text(x + 45, up ? base - H(v) - 8 : base + Math.abs(H(v)) + 16, (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 45, 240, l, "sm", { "text-anchor": "middle" }); });
  $("#labS").innerHTML = o;
}
Lib.slider($("#g7"), { id: "da", label: "Change in A's satisfaction: ", min: -10, max: 10, step: 1, value: 4, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labPar });
Lib.slider($("#g8"), { id: "db", label: "Change in B's satisfaction: ", min: -10, max: 10, step: 1, value: -2, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labPar });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Put each statement under the type of efficiency it describes.",
  buckets: [{ label: "Productive" }, { label: "Allocative" }, { label: "Dynamic" }, { label: "X-inefficiency" }, { label: "Pareto" }],
  items: [
    { text: "Output at the minimum point of the AC curve", b: 0 }, { text: "An economy operating on its production possibility curve", b: 0 },
    { text: "Price equals marginal cost", b: 1 }, { text: "Marginal social benefit equals marginal social cost", b: 1 },
    { text: "Profits reinvested in R&D to cut LRAC over time", b: 2 }, { text: "The LRAC curve shifts down", b: 2 },
    { text: "A sole supplier lets costs drift above the minimum", b: 3 }, { text: "Little competition, so little pressure to control costs", b: 3 },
    { text: "No one can be made better off without making someone worse off", b: 4 },
  ], done: "Each type has its own condition: minimum AC, P = MC, a falling LRAC curve, costs above the minimum, no possible Pareto improvement.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Productive efficiency", "Output at the lowest possible average cost"],
  ["Dynamic efficiency", "Falling costs over time from investment and innovation"],
  ["X-inefficiency", "Costs above the minimum because of weak competitive pressure"],
  ["Pareto efficiency", "No reallocation can make someone better off without making someone worse off"],
  ["Pareto improvement", "A change that makes someone better off and no one worse off"],
  ["Static efficiency", "Efficiency at one point in time"],
  ["Production possibility curve", "The maximum combinations of two goods an economy can produce"],
], done: "Seven words for the types of efficiency." });
Lib.calc($("#c1"), { qs: [
  { q: "A firm's average cost is $12. The lowest possible average cost is $10. By what percentage is it above the minimum?", a: 20, sol: "(12 − 10) ÷ 10 × 100 = <b>20%</b>. Some of this may be X-inefficiency." },
  { q: "Unit cost is $50 and falls 10% a year because of R&D. What is it after 2 years ($)?", a: 40.5, sol: "50 × 0.9 × 0.9 = <b>$40.50</b>. This is dynamic efficiency." },
  { q: "A firm's lowest possible average cost is $8 but it produces at $10. By what percentage is it above the minimum?", a: 25, sol: "(10 − 8) ÷ 8 × 100 = <b>25%</b>." },
  { q: "Unit cost is $100 and falls 5% a year through investment. What is it after 2 years ($, 2 decimal places)?", a: 90.25, tol: 0.01, sol: "100 × 0.95 × 0.95 = <b>$90.25</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Productive efficiency is achieved when a firm produces:", opts: ["where MR = MC", "at the minimum point of average cost", "where price equals marginal revenue", "the most output possible"], a: 1, why: "At the lowest point of the AC curve, MC = AC." },
  { q: "Which is most likely to achieve dynamic efficiency?", opts: ["A firm earning only normal profit with no spare funds", "A firm that reinvests supernormal profit in R&D", "A firm with constant costs", "A firm that cuts output"], a: 1, why: "R&D investment lowers long-run average cost over time." },
  { q: "A move from a point inside the PPC to a point on it, with more of both goods, is:", opts: ["a Pareto improvement", "a loss of efficiency", "a move to allocative inefficiency", "impossible"], a: 0, why: "Someone gains and no one loses." },
  { q: "A policy gives person A +5 and person B −2. This is:", opts: ["a Pareto improvement", "not a Pareto improvement, because B loses", "always desirable", "always inefficient"], a: 1, why: "A Pareto improvement requires that nobody loses." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Productive efficiency", "Producing at the lowest possible average cost: the minimum of the AC curve, or on the PPC."],
  ["Allocative efficiency", "Resources allocated to maximise consumer satisfaction: P = MC (or MSB = MSC)."],
  ["Dynamic efficiency", "Falling costs over time from investment and innovation."],
  ["X-inefficiency", "Average costs above the minimum because a firm faces little competitive pressure."],
  ["Pareto efficiency", "No reallocation can make someone better off without making someone worse off."],
  ["Pareto improvement", "A change that makes at least one person better off and no one worse off."],
  ["Static efficiency", "Efficiency at one point in time (productive and allocative)."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2023 · 32 · Q4] What is likely to help create dynamic efficiency?", opts: ["Entry barriers are reduced to increase competition in the market.", "Firms are legally bound to produce where price equals marginal cost.", "Taxes on profits are raised to encourage firms to produce where price equals average cost.", "Taxes on retained profits are reduced to encourage investment in new technology."], a: 3, why: "Dynamic efficiency comes from investment in new technology, which is encouraged if retained profits are taxed less." },
  { q: "[Feb/March 2024 · 32 · Q7] In which market structure is dynamic efficiency least likely to occur?", opts: ["oligopoly", "monopolistic competition", "monopoly", "perfectly competitive"], a: 3, why: "Perfectly competitive firms earn only normal profit in the long run, leaving little to invest in R&D." },
  { q: "[May/June 2022 · 31 · Q1] Which statement identifies the condition necessary to achieve Pareto optimality?", opts: ["All consumers maximise their utility subject to their available income.", "It is not possible to produce greater output with the resources available.", "It is not possible to reallocate resources to make someone better off without someone else becoming worse off.", "Potential losers from any reallocation of resources cannot be compensated by those who gain."], a: 2, why: "That is the definition of Pareto optimality." },
  { q: "[May/June 2022 · 32 · Q3] What might reduce dynamic efficiency in an economy?", opts: ["government expenditure on enterprise education", "reinvestment of profits", "rising shareholder dividends", "the increase in innovation"], a: 2, why: "Higher dividends mean less profit retained for investment. The others support dynamic efficiency." },
  { q: "[Oct/Nov 2021 · 32 · Q1] Which statement best defines productive efficiency?", opts: ["It is not possible to increase profits by changing the level of production.", "It is not possible to make anyone better off without others becoming worse off.", "It is not possible to produce the level of output at a lower unit cost.", "It is not possible to produce outside the production possibility curve."], a: 2, why: "A is profit maximisation, B is Pareto efficiency, D describes the PPC boundary." },
  { q: "[Oct/Nov 2022 · 33 · Q1] When is Pareto efficiency achieved?", opts: ["at a level of output that is productively and allocatively efficient", "when everyone has equal amounts of goods and services", "when social benefits are greater than private benefits", "when social marginal benefit is greater than social marginal cost"], a: 0, why: "Pareto efficiency requires both productive and allocative efficiency. Equality is not a condition." },
  { q: "[Oct/Nov 2023 · 33 · Q10] What is consistent with a movement towards Pareto optimality?", opts: ["when negative externality lowers the utility of an individual", "when consumption of a good is non-rival", "when reallocation of resources can make someone better off without making any other person worse off", "when trade takes place to make one nation better off at the expense of its trading partner"], a: 2, why: "That is a Pareto improvement." },
] });
