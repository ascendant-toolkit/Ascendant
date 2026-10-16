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
  ["Principal", "The owner (shareholder) who hires someone to act for them"],
  ["Agent", "The person (manager) who acts on the owner's behalf"],
  ["Asymmetric information", "One side knows more than the other"],
  ["Satisficing", "Making a satisfactory level of profit, then pursuing other goals"],
  ["Price discrimination", "Charging different prices for the same product, not explained by cost"],
  ["Limit pricing", "A price set to deter new entrants"],
  ["Predatory pricing", "A price below cost to force existing rivals out"],
  ["Divorce of ownership and control", "Shareholders own the firm but managers run it"],
], done: "These eight words cover most of the chapter." });
Lib.order($("#o1"), { prompt: "Put the explanation of third degree price discrimination in order.", items: [
  "The firm has market power, so it can set its own price",
  "It splits customers into separate markets that cannot resell to each other",
  "The markets have different price elasticities of demand",
  "The firm sets MR = MC in each market",
  "Price is higher in the inelastic market and lower in the elastic market",
  "Evaluate: producer gains consumer surplus, some consumers gain, long-run effects depend on competition",
], done: "A reliable structure for 13 and 20 mark answers." });
Lib.calc($("#c1"), { qs: [
  { q: "A firm uses cost-plus pricing with a 25% mark-up. Unit cost is $40. What is the price ($)?", a: 50, sol: "40 × 1.25 = <b>$50</b>." },
  { q: "Demand is P = 100 − Q and MC = $20. What is the profit-maximising output?", a: 40, hint: "MR = 100 − 2Q. Set MR = MC.", sol: "100 − 2Q = 20, so Q = <b>40</b>." },
  { q: "Demand is P = 60 − 2Q. What output maximises revenue?", a: 15, hint: "MR = 60 − 4Q. Set MR = 0.", sol: "60 − 4Q = 0, so Q = <b>15</b>." },
  { q: "In Market A the price is $50, MC is $10 and output is 40. What is the profit ($)?", a: 1600, sol: "(50 − 10) × 40 = <b>$1,600</b>." },
  { q: "In Market B the price is $30, MC is $10 and output is 20. What is the profit ($)?", a: 400, sol: "(30 − 10) × 20 = <b>$400</b>." },
  { q: "Using the two markets above, how much more profit does price discrimination earn than the best single price of $1,800 ($)?", a: 200, sol: "1,600 + 400 = 2,000. 2,000 − 1,800 = <b>$200</b>." },
  { q: "Demand is P = 100 − Q. At the revenue-maximising output of 50, what is total revenue ($)?", a: 2500, sol: "P = 50, so revenue = 50 × 50 = <b>$2,500</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which objective is achieved where MR = 0?", opts: ["Profit maximisation", "Revenue maximisation", "Sales volume maximisation", "Satisficing"], a: 1, why: "When MR is zero, an extra unit adds nothing to revenue, so total revenue is at its highest." },
  { q: "Compared with profit maximisation, sales maximisation (earning normal profit) is likely to give:", opts: ["a higher price and lower output", "a lower price and higher output", "the same price and output", "a higher price and higher output"], a: 1, why: "Output extends to AR = AC, beyond MR = MC, so price is lower and output is higher." },
  { q: "The principal-agent problem is most likely when:", opts: ["owners run the firm themselves", "managers have different aims from shareholders", "there is perfect information", "all workers are paid the same"], a: 1, why: "Agents (managers) act for principals (shareholders) but may pursue their own aims." },
  { q: "Which condition is NOT needed for price discrimination?", opts: ["The firm can set its price", "The markets can be separated", "The product is resold between markets", "Price elasticity of demand differs"], a: 2, why: "Resale would remove the price difference, so it must be prevented." },
  { q: "A firm sells below cost to force an existing rival out of the market. This is:", opts: ["limit pricing", "predatory pricing", "price discrimination", "cost-plus pricing"], a: 1, why: "Below-cost pricing against a firm already in the market is predatory." },
  { q: "Which is most likely to reduce the principal-agent problem?", opts: ["Managers paid a flat salary regardless of results", "Share options for managers", "Less reporting to shareholders", "Bonuses on revenue only"], a: 1, why: "Share options tie the manager's reward to the firm's value, which aligns interests." },
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
  ["Price discrimination", "Charging different prices for the same product to different groups, not due to cost."],
  ["Third degree price discrimination", "Different prices for different groups or times: higher where demand is inelastic."],
  ["Limit pricing", "A price set below the monopoly price to deter new entrants."],
  ["Predatory pricing", "A price below cost to force existing rivals out of the market."],
  ["Cost-plus pricing", "Price set by adding a percentage mark-up to unit cost."],
] });

/* ---------- Past paper MCQ (text) ---------- */
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2022 · 32 · Q12] What is generally associated with the principal agent problem?", opts: ["Directors prefer company growth to greater shareholder dividends.", "Managers ignore workers' concerns about safety in the workplace.", "Shareholders determine the price of products.", "Workers go on strike against managers' reorganisation plans."], a: 0, why: "Directors (agents) pursue growth, which suits them, rather than the dividends shareholders (principals) want." },
  { q: "[Oct/Nov 2021 · 32 · Q11] What is an example of the principal–agent problem?", opts: ["the disincentive effect for entrepreneurs of high government tax rates", "the existence of a trade union to put forward workers' views to managers", "the lack of consumer knowledge of the quality of firms' products", "the separation of the owners of a firm from the firm's managers"], a: 3, why: "Owners (principals) and managers (agents) are separate people with possibly different aims." },
  { q: "[Oct/Nov 2020 · 33 · Q12] Which objective involves the managers of a firm operating with just enough profit to keep shareholders happy whilst maintaining sales revenue above its profit-maximising level?", opts: ["achieving below normal profit", "maximising the quality of the output", "profit satisficing", "sales revenue maximisation"], a: 2, why: "Satisficing means a good-enough profit and other goals. Revenue maximisation does not include a profit target." },
  { q: "[May/June 2023 · 31 · Q11] What would definitely result from the divorce of ownership and control?", opts: ["decreased moral hazard", "the principal agent problem", "greater productive efficiency", "increased profit maximisation"], a: 1, why: "Separating ownership from control creates a principal (owner) and an agent (manager), so the problem is a risk. Greater efficiency or more profit maximisation is not guaranteed." },
  { q: "[Oct/Nov 2023 · 33 · Q3] What is most likely to increase the principal–agent problem?", opts: ["ensuring the actions of agents are known by the managers", "linking the rewards of managers with the profitability of the firm", "removing from managers the opportunity to hold shares", "preparing contracts that compel agents to work in the interest of the principal"], a: 2, why: "Managers who cannot hold shares have less reason to care about the firm's value. A, B and D reduce the problem." },
  { q: "[Feb/March 2024 · 32 · Q8] Which type of employment contract is most likely to overcome the principal agent problem?", opts: ["increasing monthly salaries of waiters in a restaurant to decrease their dependence on tips from customers", "linking workers' pay with the profits of the firm to motivate them to raise the profitability of the firm", "making full fee payment in advance to a lawyer to motivate him to prepare a legal case well", "offering permanent contracts to give workers job security"], a: 1, why: "Linking pay to profit aligns the agent's reward with the principal's aim." },
  { q: "[May/June 2020 · 32 · Q10] When will the 'principal-agent' problem occur?", opts: ["when managers are not allowed to become shareholders", "when members of a cartel collude to gain higher profit", "when one firm dominates the market", "when owners have different objectives to managers"], a: 3, why: "It is the clash of aims between owners (principals) and managers (agents)." },
  { q: "[Oct/Nov 2020 · 31 · Q9] What is necessary for price discrimination to be profitable in different markets?", opts: ["There must be many buyers.", "There must be markets with different price elasticities of demand.", "There must be product differentiation.", "There must be geographically separate markets."], a: 1, why: "Different elasticities give a reason for different prices. Markets must be separable, but not necessarily by geography." },
  { q: "[Oct/Nov 2023 · 31 · Q6] What is a key condition for effective price discrimination?", opts: ["The product cannot be resold to another consumer.", "The product must be price inelastic.", "The profits from one market can be used to subsidise another market.", "There are low barriers to entry into the market."], a: 0, why: "Without a ban on resale, buyers in the cheap market could undercut the firm in the dear market." },
  { q: "[Oct/Nov 2022 · 31 · Q10] Which conditions enable price discrimination? (1) The firm can separate the total market into sub-markets. (2) There are different price elasticities of demand in each sub-market. (3) The marginal revenue curve is the same in each separate market.", opts: ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], a: 0, why: "The marginal revenue curves differ because the demand curves differ. 3 is not a condition." },
  { q: "[Oct/Nov 2023 · 33 · Q7] Which condition is necessary for a firm to practise third degree price discrimination effectively?", opts: ["All consumers and producers must be in the same geographical location.", "Customers must be divided into separate markets for the same product.", "Each separate market must have identical price elasticities of demand.", "Price undercutting is required to enter a monopolistic market."], a: 1, why: "Separate markets are essential. Identical elasticities would give no reason to discriminate." },
  { q: "[May/June 2023 · 32 · Q3] What is not necessary for successful price discrimination?", opts: ["ability to separate markets", "different price elasticities of demand in each market", "monopoly power", "price leadership"], a: 3, why: "The firm needs some power to set price (not necessarily a pure monopoly) but price leadership is an oligopoly behaviour and is not a condition." },
] });
