/* ---------- model: P = 100 - Q (AR), MR = 100 - 2Q, MC = 20, fixed cost 400, AC = 20 + 400/Q ---------- */
const PRO = (q) => (100 - q) * q - 20 * q - 400, REV = (q) => (100 - q) * q;
const Q_PM = 40, Q_RM = 50, Q_SM = 40 + Math.sqrt(1200);     // profit, revenue, sales maximisation (AR = AC)
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const AX = (q) => 70 + q * 6.5, AY = (p) => 330 - p * 3.1;
const aAxes = () => SV.line(70, 330, 720, 330) + SV.line(70, 330, 70, 20) + SV.text(720, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price, cost, revenue ($)", "sm");
const acPts = () => { const a = []; for (let q = 8; q <= 100; q += 2) a.push([AX(q), AY(20 + 400 / q)]); return a; };
function objCurves(s) {
  let o = aAxes();
  if (s.ar > 0) o += SV.line(AX(0), AY(100), AX(100), AY(0), "c1", op(s.ar)) + SV.text(AX(100) - 4, AY(0) - 8, "AR = D", "lbl bd t1", { "text-anchor": "end", ...op(s.ar) });
  if (s.mr > 0) o += SV.line(AX(0), AY(100), AX(50), AY(0), "c4", op(s.mr)) + SV.text(AX(50) - 6, AY(0) - 8, "MR", "lbl bd t4", { "text-anchor": "end", ...op(s.mr) });
  if (s.mc > 0) o += SV.line(AX(0), AY(20), AX(100), AY(20), "c2", op(s.mc)) + SV.text(AX(100) - 4, AY(20) - 8, "MC", "lbl bd t2", { "text-anchor": "end", ...op(s.mc) });
  if (s.ac > 0) o += SV.path(Lib.ptsPath(acPts()), "c3", op(s.ac)) + SV.text(AX(100) - 4, AY(24) - 22, "AC", "lbl bd t3", { "text-anchor": "end", ...op(s.ac) });
  return o;
}
function marker(q, p, cls, label, v) {
  return SV.line(AX(q), AY(p), AX(q), 330, "gr", op(v)) + SV.line(70, AY(p), AX(q), AY(p), "gr", op(v)) + SV.circle(AX(q), AY(p), 6, cls, op(v)) + SV.text(AX(q), 350, label, "lbl bd", { "text-anchor": "middle", ...op(v) });
}
function objDraw(s) {
  let o = objCurves(s);
  if (s.p1 > 0) o += SV.rect(AX(0), AY(60), AX(Q_PM) - AX(0), AY(30) - AY(60), "f3", op(s.p1)) + marker(40, 60, "dot3", "Q = 40", s.p1) + SV.text(AX(41) + 8, AY(60) - 8, "Profit max: P = $60", "lbl bd t3", op(s.p1));
  if (s.p2 > 0) o += marker(50, 50, "dot4", "Q = 50", s.p2) + SV.text(AX(51) + 8, AY(50) - 8, "Revenue max: P = $50", "lbl bd t4", op(s.p2));
  if (s.p3 > 0) o += marker(Q_SM, 100 - Q_SM, "dot2", "Q ≈ 75", s.p3) + SV.text(AX(Q_SM) + 8, AY(100 - Q_SM) - 14, "Sales max: P ≈ $25", "lbl bd t2", op(s.p3));
  return o;
}

/* ---------- Learn: static picture ---------- */
$("#pic1").innerHTML = `<svg viewBox="0 0 760 370" role="img" aria-label="Demand, marginal revenue, marginal cost and average cost with profit maximising output at 40, revenue maximising output at 50 and sales maximising output at about 75">${objDraw({ ar: 1, mr: 1, mc: 1, ac: 1, p1: 1, p2: 1, p3: 1 })}</svg>`;

/* ---------- Watch 1: three objectives ---------- */
Lib.stepper($("#stA"), { w: 760, h: 380, label: "Building the diagram for profit, revenue and sales maximisation", base: { ar: 0, mr: 0, mc: 0, ac: 0, p1: 0, p2: 0, p3: 0 }, draw: objDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>The firm's curves.</b> Demand (AR) slopes down, so <b>MR</b> falls twice as fast. <b>MC</b> is constant at $20. <b>AC</b> falls as the fixed cost is spread over more output.", s: { ar: 1, mr: 1, mc: 1, ac: 1 } },
  { cap: "<b>Profit maximisation: MR = MC.</b> Output 40, price $60, AC $30. Profit = (60 − 30) × 40 = <b>$1,200</b>. Highest price, lowest output.", s: { ar: 1, mr: 1, mc: 1, ac: 1, p1: 1 } },
  { cap: "<b>Revenue maximisation: MR = 0.</b> Output 50, price $50. Revenue is $2,500 (the most possible), profit falls to $1,100.", s: { ar: 1, mr: 1, mc: 1, ac: 1, p1: 1, p2: 1 } },
  { cap: "<b>Sales maximisation: AR = AC.</b> Keep selling until the firm only earns normal profit. Output about 75, price about $25, profit <b>zero</b> (supernormal). Lowest price, highest output.", s: { ar: 1, mr: 1, mc: 1, ac: 1, p1: 1, p2: 1, p3: 1 } },
] });

/* ---------- Lab 1: which objective ---------- */
function lab1() {
  if (!$("#ob1") || !$("#ob2")) return;
  const k = +$("#ob1").value, pmin = +$("#ob2").value, qsm = 40 + Math.sqrt(1200 - pmin);
  const q = k === 1 ? 40 : k === 2 ? (PRO(50) >= pmin ? 50 : qsm) : qsm, p = 100 - q;
  $("#r1").textContent = Lib.fmtN(q, 1); $("#r2").textContent = "$" + Lib.fmtN(p, 1); $("#r3").textContent = "$" + Lib.fmtN(REV(q), 0); $("#r4").textContent = "$" + Lib.fmtN(PRO(q), 0);
  $("#rv").textContent = k === 1 ? "Profit maximisation: MR = MC. Output 40, the highest price and the highest profit, $1,200."
    : k === 2 ? (pmin <= 1100 ? "Revenue maximisation: MR = 0. Output 50. Profit is still above the shareholders' minimum, so the constraint does not bite." : "Revenue maximisation, but shareholders insist on more profit than $1,100, so the manager has to cut output back towards 40.")
    : (pmin === 0 ? "Sales volume maximisation with only normal profit: AR = AC. Output about 75, the lowest price. Supernormal profit is zero." : "Sales volume maximisation with a minimum profit target. The higher the profit shareholders demand, the closer output gets to 40.");
  const X = (v) => 40 + v * 3.6, Y = (v) => 260 - v * 2.4, pts = []; for (let v = 8; v <= 100; v += 2) pts.push([X(v), Y(20 + 400 / v)]);
  $("#labA").innerHTML = SV.line(40, 260, 410, 260) + SV.line(40, 260, 40, 20) + SV.text(406, 282, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "$", "sm") +
    SV.line(X(0), Y(100), X(100), Y(0), "c1") + SV.line(X(0), Y(100), X(50), Y(0), "c4") + SV.line(X(0), Y(20), X(100), Y(20), "c2") + SV.path(Lib.ptsPath(pts), "c3") +
    SV.line(X(40), Y(60), X(40), 260, "gr", { opacity: 0.6 }) + SV.line(X(q), Y(p), X(q), 260, "gr") + SV.line(40, Y(p), X(q), Y(p), "gr") + SV.circle(X(q), Y(p), 7, "dot2") + SV.text(X(q), 276, "Q", "sm bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "ob1", label: "Objective: ", min: 1, max: 3, step: 1, value: 1, fmt: (v) => ["profit", "revenue", "sales volume"][v - 1], onInput: lab1 });
Lib.slider($("#g2"), { id: "ob2", label: "Minimum profit shareholders insist on ($): ", min: 0, max: 1200, step: 50, value: 0, fmt: (v) => v, onInput: lab1 });
/* ---------- Lab 4: pay and the principal-agent problem ---------- */
function lab4() {
  if (!$("#pa1")) return;
  const s = +$("#pa1").value / 100, q = 50 - 10 * s, p = 100 - q, prof = PRO(q);
  $("#v1").textContent = Lib.fmtN(q, 1); $("#v2").textContent = "$" + Lib.fmtN(prof, 0); $("#v3").textContent = "$" + Lib.fmtN(1200 - prof, 0);
  $("#vv").textContent = s === 0 ? "Pay depends only on revenue, so the manager pushes output to 50 (revenue maximisation). Shareholders lose $100 of profit."
    : s === 1 ? "Pay depends only on profit, so the manager picks MR = MC (Q = 40). The principal-agent problem is solved in this simple model."
    : `With ${Math.round(s * 100)}% of pay linked to profit the manager chooses Q = ${Lib.fmtN(q, 1)}. The more pay is tied to profit, the closer the agent gets to what shareholders want.`;
  const H = (v) => 200 - v * 0.14, bw = 90, bars = [[60, 1200, "f3", "Maximum profit"], [220, prof, "f4", "Profit with manager's choice"]];
  let o = SV.line(30, 200, 400, 200) + SV.text(32, 24, "Profit ($)", "sm");
  bars.forEach(([x, v, c, l]) => { o += SV.rect(x, H(v), bw, 200 - H(v), c) + SV.text(x + bw / 2, H(v) - 6, Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 218, l, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g7"), { id: "pa1", label: "Share of the manager's pay linked to profit: ", min: 0, max: 100, step: 5, value: 0, fmt: (v) => v + "%", onInput: lab4 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Put each statement in the right bucket.",
  buckets: [{ label: "Profit maximisation" }, { label: "Revenue maximisation" }, { label: "Sales volume maximisation" }, { label: "Satisficing" }],
  items: [
    { text: "Output where MR = MC", b: 0 }, { text: "Highest price and lowest output of the three", b: 0 },
    { text: "Output where MR = 0", b: 1 }, { text: "Managers paid on turnover", b: 1 },
    { text: "Output where AR = AC", b: 2 }, { text: "Sell as many units as possible and still earn normal profit", b: 2 },
    { text: "Just enough profit to keep shareholders happy", b: 3 }, { text: "Managers choose a quiet life once targets are met", b: 3 },
  ], done: "Know the three rules (MR = MC, MR = 0, AR = AC) and satisficing as 'good enough'.",
});
Lib.classify($("#cl2"), {
  prompt: "Does each item reduce the principal-agent problem, or make it worse?",
  buckets: [{ label: "Reduces it" }, { label: "Makes it worse" }],
  items: [
    { text: "Managers receive share options", b: 0 }, { text: "Bonuses linked to company profit", b: 0 }, { text: "Independent audits and regular reports", b: 0 }, { text: "Independent non-executive directors", b: 0 },
    { text: "Bonuses based on revenue only", b: 1 }, { text: "Managers are not allowed to own shares", b: 1 }, { text: "Complex accounts that shareholders cannot follow", b: 1 }, { text: "Guaranteed pay whatever the results", b: 1 },
  ], done: "Align the agent's rewards with the principal's aims, and reduce the information gap.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Profit maximisation", "Producing where MR = MC"],
  ["Revenue maximisation", "Producing where MR = 0"],
  ["Sales maximisation", "Selling as much as possible while earning normal profit: AR = AC"],
  ["Satisficing", "Earning a satisfactory profit and then pursuing other aims"],
  ["Principal", "The owner or shareholder who employs a manager"],
  ["Agent", "The manager who acts for the owner"],
  ["Divorce of ownership and control", "Shareholders own the firm but managers run it"],
  ["Asymmetric information", "One party knows more than the other"],
], done: "Eight words for objectives and the principal-agent problem." });
Lib.calc($("#c1"), { qs: [
  { q: "Demand is P = 100 − Q and MC = $20. What is the profit-maximising output?", a: 40, hint: "MR = 100 − 2Q. Set MR = MC.", sol: "100 − 2Q = 20, so Q = <b>40</b>." },
  { q: "Demand is P = 60 − 2Q. What output maximises revenue?", a: 15, hint: "MR = 60 − 4Q. Set MR = 0.", sol: "60 − 4Q = 0, so Q = <b>15</b>." },
  { q: "Demand is P = 100 − Q. At the revenue-maximising output of 50, what is total revenue ($)?", a: 2500, sol: "P = 50, so revenue = 50 × 50 = <b>$2,500</b>." },
  { q: "Demand is P = 100 − Q, MC = $20 and fixed cost is $400. At the profit-maximising output of 40, what is the profit ($)?", a: 1200, sol: "(60 − 20) × 40 − 400 = <b>$1,200</b>." },
  { q: "The firm moves to the revenue-maximising output of 50. What is its profit ($)?", a: 1100, sol: "Revenue 2,500 − total cost (20 × 50 + 400 = 1,400) = <b>$1,100</b>." },
  { q: "At the revenue-maximising output of 50, price is $50. By how much has price fallen compared with profit maximisation ($)?", a: 10, sol: "60 − 50 = <b>$10</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which objective is achieved where MR = 0?", opts: ["Profit maximisation", "Revenue maximisation", "Sales volume maximisation", "Satisficing"], a: 1, why: "When MR is zero, an extra unit adds nothing to revenue, so total revenue is at its highest." },
  { q: "Compared with profit maximisation, sales maximisation (earning normal profit) is likely to give:", opts: ["a higher price and lower output", "a lower price and higher output", "the same price and output", "a higher price and higher output"], a: 1, why: "Output extends to AR = AC, beyond MR = MC, so price is lower and output is higher." },
  { q: "The principal-agent problem is most likely when:", opts: ["owners run the firm themselves", "managers have different aims from shareholders", "there is perfect information", "all workers are paid the same"], a: 1, why: "Agents (managers) act for principals (shareholders) but may pursue their own aims." },
  { q: "Which is most likely to reduce the principal-agent problem?", opts: ["Managers paid a flat salary regardless of results", "Share options for managers", "Less reporting to shareholders", "Bonuses on revenue only"], a: 1, why: "Share options tie the manager's reward to the firm's value, which aligns interests." },
  { q: "Managers who aim for the largest possible sales while earning normal profit are pursuing:", opts: ["profit maximisation", "revenue maximisation", "sales maximisation", "satisficing"], a: 2, why: "Sales maximisation is at AR = AC, where only normal profit is earned." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Profit maximisation", "Producing where MR = MC, the output with the greatest gap between revenue and cost."],
  ["Revenue maximisation", "Producing where MR = 0, so total revenue is as high as possible."],
  ["Sales (volume) maximisation", "Selling as many units as possible while earning normal profit: AR = AC."],
  ["Satisficing", "Earning a satisfactory profit and then pursuing other aims."],
  ["Growth maximisation", "Aiming for a larger firm or market share, often at the cost of short-run profit."],
  ["Principal", "The owner (shareholder) who employs an agent to act for them."],
  ["Agent", "The manager who acts on behalf of the principal."],
  ["Principal-agent problem", "Agents may pursue their own aims instead of the principal's, helped by asymmetric information."],
  ["Divorce of ownership and control", "Shareholders own the firm but managers run it."],
  ["Asymmetric information", "One party in a transaction knows more than the other."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2022 · 32 · Q12] What is generally associated with the principal agent problem?", opts: ["Directors prefer company growth to greater shareholder dividends.", "Managers ignore workers' concerns about safety in the workplace.", "Shareholders determine the price of products.", "Workers go on strike against managers' reorganisation plans."], a: 0, why: "Directors (agents) pursue growth, which suits them, rather than the dividends shareholders (principals) want." },
  { q: "[Oct/Nov 2021 · 32 · Q11] What is an example of the principal–agent problem?", opts: ["the disincentive effect for entrepreneurs of high government tax rates", "the existence of a trade union to put forward workers' views to managers", "the lack of consumer knowledge of the quality of firms' products", "the separation of the owners of a firm from the firm's managers"], a: 3, why: "Owners (principals) and managers (agents) are separate people with possibly different aims." },
  { q: "[Oct/Nov 2020 · 33 · Q12] Which objective involves the managers of a firm operating with just enough profit to keep shareholders happy whilst maintaining sales revenue above its profit-maximising level?", opts: ["achieving below normal profit", "maximising the quality of the output", "profit satisficing", "sales revenue maximisation"], a: 2, why: "Satisficing means a good-enough profit and other goals. Revenue maximisation does not include a profit target." },
  { q: "[May/June 2023 · 31 · Q11] What would definitely result from the divorce of ownership and control?", opts: ["decreased moral hazard", "the principal agent problem", "greater productive efficiency", "increased profit maximisation"], a: 1, why: "Separating ownership from control creates a principal (owner) and an agent (manager), so the problem is a risk. Greater efficiency or more profit maximisation is not guaranteed." },
  { q: "[Oct/Nov 2023 · 33 · Q3] What is most likely to increase the principal–agent problem?", opts: ["ensuring the actions of agents are known by the managers", "linking the rewards of managers with the profitability of the firm", "removing from managers the opportunity to hold shares", "preparing contracts that compel agents to work in the interest of the principal"], a: 2, why: "Managers who cannot hold shares have less reason to care about the firm's value. A, B and D reduce the problem." },
  { q: "[Feb/March 2024 · 32 · Q8] Which type of employment contract is most likely to overcome the principal agent problem?", opts: ["increasing monthly salaries of waiters in a restaurant to decrease their dependence on tips from customers", "linking workers' pay with the profits of the firm to motivate them to raise the profitability of the firm", "making full fee payment in advance to a lawyer to motivate him to prepare a legal case well", "offering permanent contracts to give workers job security"], a: 1, why: "Linking pay to profit aligns the agent's reward with the principal's aim." },
  { q: "[May/June 2020 · 32 · Q10] When will the 'principal-agent' problem occur?", opts: ["when managers are not allowed to become shareholders", "when members of a cartel collude to gain higher profit", "when one firm dominates the market", "when owners have different objectives to managers"], a: 3, why: "It is the clash of aims between owners (principals) and managers (agents)." },
] });
