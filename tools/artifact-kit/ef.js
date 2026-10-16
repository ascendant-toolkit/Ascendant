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

/* ---------- Lab 4: free rider ---------- */
function lab4() {
  if (!$("#fv") || !$("#fn")) return;
  const v = +$("#fv").value, n = +$("#fn").value, tot = v * n, net = tot - 100;
  $("#u1").textContent = "$" + tot; $("#u2").textContent = (net >= 0 ? "+$" : "−$") + Math.abs(net); $("#u3").textContent = "No";
  $("#uv").textContent = net > 0 ? `Total benefit ($${tot}) is greater than the cost ($100), so building it is worth $${net} to society. But a private firm cannot charge: once built, everyone can use it without paying (non-excludable), and each user hopes others will pay (free riding). The market fails to provide a good that society values: a missing market. The government could provide it, funded by tax.`
    : net === 0 ? "Benefit equals cost, so society is indifferent. A private firm still could not charge for it." : `Total benefit ($${tot}) is below the cost ($100), so it is efficient not to build it. Move the sliders until total benefit exceeds $100.`;
  const m = Math.max(100, tot), H = (x) => 190 * (x / m), bw = 70;
  let o = SV.line(30, 210, 400, 210) + SV.text(32, 22, "$", "sm");
  [[40, 100, "f2", "Cost to build"], [150, v, "f1", "One user's value"], [260, tot, net > 0 ? "f3" : "f4", "Total benefit"]].forEach(([x, val, c, l]) => { o += SV.rect(x, 210 - H(val), bw, H(val), c) + SV.text(x + bw / 2, 210 - H(val) - 6, "$" + val, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 228, l, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g5"), { id: "fv", label: "Value to each user ($): ", min: 2, max: 30, step: 1, value: 15, fmt: (v) => v, onInput: lab4 });
Lib.slider($("#g6"), { id: "fn", label: "Number of users: ", min: 2, max: 20, step: 1, value: 10, fmt: (v) => v, onInput: lab4 });

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
Lib.classify($("#cl2"), {
  prompt: "Which cause of market failure is each example?",
  buckets: [{ label: "Externality" }, { label: "Public good" }, { label: "Merit or demerit good" }, { label: "Information failure" }, { label: "Monopoly power" }],
  items: [
    { text: "A factory's smoke harms nearby residents", b: 0 }, { text: "Traffic congestion slows other drivers", b: 0 },
    { text: "Street lighting that cannot be charged for", b: 1 }, { text: "National defence: free riders benefit without paying", b: 1 },
    { text: "Vaccinations are under-consumed", b: 2 }, { text: "Cigarettes are over-consumed", b: 2 },
    { text: "A used car buyer cannot tell the car's quality", b: 3 }, { text: "A smoker underestimates the health risk", b: 3 },
    { text: "A sole supplier restricts output and raises price", b: 4 },
  ], done: "Name the cause, then explain how it leads to allocative inefficiency.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Productive efficiency", "Producing at the lowest possible average cost"],
  ["Allocative efficiency", "Resources go to the goods consumers value most: P = MC"],
  ["Dynamic efficiency", "Lower costs over time through investment and innovation"],
  ["X-inefficiency", "Costs higher than necessary because of weak competitive pressure"],
  ["Pareto efficiency", "No one can be better off without someone else being worse off"],
  ["Market failure", "The free market does not allocate resources efficiently"],
  ["Free-rider problem", "People use a good without paying for it, so the market does not provide it"],
  ["Asymmetric information", "One side of a transaction knows more than the other"],
], done: "These eight words are the core of the chapter." });
Lib.order($("#o1"), { prompt: "Put the explanation of why monopoly is allocatively inefficient in order.", items: [
  "The monopolist faces a downward sloping demand curve, so MR is below price",
  "It maximises profit where MR = MC",
  "At that output the price on the demand curve is above marginal cost",
  "Output is lower than the allocatively efficient output (where P = MC)",
  "Units that consumers value more than they cost are not produced, creating a welfare loss",
  "Evaluate: economies of scale or dynamic efficiency may offset the loss, and regulation may reduce it",
], done: "This chain works for a 13 or 20 mark answer." });
Lib.calc($("#c1"), { qs: [
  { q: "Demand is P = 100 − Q and MC = $20. What output is allocatively efficient?", a: 80, sol: "P = MC: 100 − Q = 20, so Q = <b>80</b>." },
  { q: "A monopolist faces the same demand and MC = $20. What output does it choose?", a: 40, hint: "MR = 100 − 2Q. Set MR = MC.", sol: "100 − 2Q = 20, so Q = <b>40</b>." },
  { q: "What price does the monopolist charge ($)?", a: 60, sol: "P = 100 − 40 = <b>$60</b>." },
  { q: "What is the welfare loss from the monopoly ($)?", a: 800, hint: "Triangle: half × (60 − 20) × (80 − 40).", sol: "½ × 40 × 40 = <b>$800</b>." },
  { q: "A firm's average cost is $12. The lowest possible average cost is $10. By what percentage is it above the minimum?", a: 20, sol: "(12 − 10) ÷ 10 × 100 = <b>20%</b>. Some of this may be X-inefficiency." },
  { q: "A lighthouse costs $100. Ten users each value it at $15. What is the net social benefit ($)?", a: 50, sol: "Total benefit 150 − cost 100 = <b>$50</b>. Worth building, but a private firm could not charge for it." },
  { q: "Unit cost is $50 and falls 10% a year because of R&D. What is it after 2 years ($)?", a: 40.5, sol: "50 × 0.9 × 0.9 = <b>$40.50</b>. This is dynamic efficiency." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Allocative efficiency is achieved where:", opts: ["price equals average cost", "price equals marginal cost", "marginal cost is at a minimum", "profit is zero"], a: 1, why: "Price measures the value of the last unit, marginal cost its cost." },
  { q: "Productive efficiency is achieved when a firm produces:", opts: ["where MR = MC", "at the minimum point of average cost", "where price equals marginal revenue", "the most output possible"], a: 1, why: "At the lowest point of the AC curve, MC = AC." },
  { q: "Which is most likely to achieve dynamic efficiency?", opts: ["A firm earning only normal profit with no spare funds", "A firm that reinvests supernormal profit in R&D", "A firm with constant costs", "A firm that cuts output"], a: 1, why: "R&D investment lowers long-run average cost over time." },
  { q: "A public good is:", opts: ["rival and excludable", "non-rival and non-excludable", "rival and non-excludable", "provided by the government only"], a: 1, why: "Because non-payers cannot be excluded, free riders mean the market does not provide it." },
  { q: "Which would NOT be a source of market failure in the efficiency sense?", opts: ["Externalities", "Monopoly power", "Asymmetric information", "A free market with perfect information and no externalities"], a: 3, why: "Market failure arises when the conditions for efficiency are not met." },
  { q: "A move from a point inside the PPC to a point on it, with more of both goods, is:", opts: ["a Pareto improvement", "a loss of efficiency", "a move to allocative inefficiency", "impossible"], a: 0, why: "Someone gains and no one loses." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Productive efficiency", "Producing at the lowest possible average cost: the minimum of the AC curve, or on the PPC."],
  ["Allocative efficiency", "Resources allocated to maximise consumer satisfaction: P = MC (or MSB = MSC)."],
  ["Dynamic efficiency", "Falling costs over time from investment and innovation."],
  ["X-inefficiency", "Average costs above the minimum because a firm faces little competitive pressure."],
  ["Pareto efficiency", "No reallocation can make someone better off without making someone worse off."],
  ["Pareto improvement", "A change that makes at least one person better off and no one worse off."],
  ["Static efficiency", "Efficiency at one point in time (productive and allocative)."],
  ["Welfare loss (deadweight loss)", "The loss of total surplus when output differs from the efficient level."],
  ["Total surplus", "Consumer surplus plus producer surplus."],
  ["Market failure", "The free market does not allocate resources efficiently."],
  ["Public good", "Non-rival and non-excludable. Leads to the free-rider problem."],
  ["Merit good", "Under-consumed because consumers undervalue the benefit (education, vaccination)."],
  ["Demerit good", "Over-consumed because consumers undervalue the harm (cigarettes)."],
  ["Asymmetric information", "One party knows more than the other, which can distort choices."],
  ["Government failure", "Intervention that leaves resources less efficiently allocated, or no better than before."],
] });

/* ---------- Past paper MCQ (text) ---------- */
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2023 · 32 · Q4] What is likely to help create dynamic efficiency?", opts: ["Entry barriers are reduced to increase competition in the market.", "Firms are legally bound to produce where price equals marginal cost.", "Taxes on profits are raised to encourage firms to produce where price equals average cost.", "Taxes on retained profits are reduced to encourage investment in new technology."], a: 3, why: "Dynamic efficiency comes from investment in new technology, which is encouraged if retained profits are taxed less." },
  { q: "[Feb/March 2024 · 32 · Q7] In which market structure is dynamic efficiency least likely to occur?", opts: ["oligopoly", "monopolistic competition", "monopoly", "perfectly competitive"], a: 3, why: "Perfectly competitive firms earn only normal profit in the long run, leaving little to invest in R&D." },
  { q: "[May/June 2022 · 31 · Q1] Which statement identifies the condition necessary to achieve Pareto optimality?", opts: ["All consumers maximise their utility subject to their available income.", "It is not possible to produce greater output with the resources available.", "It is not possible to reallocate resources to make someone better off without someone else becoming worse off.", "Potential losers from any reallocation of resources cannot be compensated by those who gain."], a: 2, why: "That is the definition of Pareto optimality." },
  { q: "[May/June 2022 · 31 · Q13] What is not a source of market failure?", opts: ["imperfect information", "income inequality", "monopoly", "non-excludability"], a: 1, why: "Income inequality is an equity issue. The others stop the market allocating resources efficiently." },
  { q: "[May/June 2022 · 32 · Q2] What must equal marginal cost when a profit-maximising firm produces at its allocatively efficient output?", opts: ["average revenue", "average total cost", "total revenue", "total cost"], a: 0, why: "Price (average revenue) equals marginal cost at the allocatively efficient output." },
  { q: "[May/June 2022 · 32 · Q3] What might reduce dynamic efficiency in an economy?", opts: ["government expenditure on enterprise education", "reinvestment of profits", "rising shareholder dividends", "the increase in innovation"], a: 2, why: "Higher dividends mean less profit retained for investment. The others support dynamic efficiency." },
  { q: "[May/June 2025 · 32 · Q2] When is allocative efficiency achieved?", opts: ["when a perfectly competitive market is in equilibrium", "when everybody who needs the product can obtain it", "when firms produce at the lowest possible cost", "when monopolistic firms make normal profits"], a: 0, why: "In a perfectly competitive equilibrium, price equals marginal cost. C describes productive efficiency." },
  { q: "[Oct/Nov 2021 · 32 · Q1] Which statement best defines productive efficiency?", opts: ["It is not possible to increase profits by changing the level of production.", "It is not possible to make anyone better off without others becoming worse off.", "It is not possible to produce the level of output at a lower unit cost.", "It is not possible to produce outside the production possibility curve."], a: 2, why: "A is profit maximisation, B is Pareto efficiency, D describes the PPC boundary." },
  { q: "[Oct/Nov 2022 · 33 · Q1] When is Pareto efficiency achieved?", opts: ["at a level of output that is productively and allocatively efficient", "when everyone has equal amounts of goods and services", "when social benefits are greater than private benefits", "when social marginal benefit is greater than social marginal cost"], a: 0, why: "Pareto efficiency requires both productive and allocative efficiency. Equality is not a condition." },
  { q: "[Oct/Nov 2022 · 32 · Q1] What is most likely to improve the allocative efficiency of a market?", opts: ["a higher market concentration ratio", "collusion between firms in the market", "entry of new firms into the market", "mergers of firms in the market"], a: 2, why: "More firms means more competition, pushing price towards marginal cost." },
  { q: "[Oct/Nov 2023 · 33 · Q10] What is consistent with a movement towards Pareto optimality?", opts: ["when negative externality lowers the utility of an individual", "when consumption of a good is non-rival", "when reallocation of resources can make someone better off without making any other person worse off", "when trade takes place to make one nation better off at the expense of its trading partner"], a: 2, why: "That is a Pareto improvement." },
  { q: "[Oct/Nov 2020 · 33 · Q3] Which situation should not lead to market failure?", opts: ["Managers in a firm have information unavailable to shareholders.", "Resources such as solar energy can be continuously renewed.", "Resource allocation is not always Pareto efficient.", "Undesirable goods are overproduced."], a: 1, why: "A renewable resource does not by itself cause market failure. A is information failure, C is the definition of failure, D is demerit goods." },
  { q: "[Oct/Nov 2021 · 33 · Q2] Why are public goods an example of market failure?", opts: ["Producers undervalue the benefits of a public good.", "Public goods have high fixed costs of production.", "The non-excludability of a public good leads to the free rider problem.", "When a public good is consumed by one person, it is not available to others."], a: 2, why: "Non-excludability means people can use the good without paying, so the market does not provide it. D describes a rival good." },
] });
