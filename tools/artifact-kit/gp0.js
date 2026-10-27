/* ---------- model: demand P = 100 - Q, supply P = 20 + Q (equilibrium Q = 40, P = 60) ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const X = (q) => 70 + q * 7.5, Y = (p) => 330 - p * 3;
const axes = () => SV.line(70, 330, 750, 330) + SV.line(70, 330, 70, 20) + SV.text(750, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price ($)", "sm");
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const marketLines = (s) => (s.d > 0 ? SV.line(X(0), Y(100), X(90), Y(10), "c1", op(s.d)) + SV.text(X(90) - 4, Y(10) - 8, "D", "lbl bd t1", { "text-anchor": "end", ...op(s.d) }) : "") +
  (s.s > 0 ? SV.line(X(0), Y(20), X(80), Y(100), "c2", op(s.s)) + SV.text(X(80) - 4, Y(100) + 16, "S", "lbl bd t2", { "text-anchor": "end", ...op(s.s) }) : "");
const eqMark = (s) => s.eq > 0 ? SV.line(X(40), Y(60), X(40), 330, "gr", op(s.eq)) + SV.line(70, Y(60), X(40), Y(60), "gr", op(s.eq)) + SV.circle(X(40), Y(60), 6, "dot3", op(s.eq)) + SV.text(66, Y(60) + 4, "60", "sm bd", { "text-anchor": "end", ...op(s.eq) }) + SV.text(X(40), 350, "40", "lbl bd", { "text-anchor": "middle", ...op(s.eq) }) : "";

/* maximum price (Learn picture and Watch 1) */
function ceilingDraw(s) {
  let o = axes() + marketLines(s) + eqMark(s);
  if (s.c > 0) o += SV.line(70, Y(40), X(90), Y(40), "c4", { "stroke-width": 3, ...op(s.c) }) + SV.text(X(90) - 4, Y(40) + 18, "Maximum price $40", "lbl bd t4", { "text-anchor": "end", ...op(s.c) });
  if (s.q > 0) o += SV.line(X(20), Y(40), X(20), 330, "gr", op(s.q)) + SV.line(X(60), Y(40), X(60), 330, "gr", op(s.q)) + SV.circle(X(20), Y(40), 6, "dot2", op(s.q)) + SV.circle(X(60), Y(40), 6, "dot1", op(s.q)) + SV.text(X(20), 350, "Qs = 20", "lbl bd", { "text-anchor": "middle", ...op(s.q) }) + SV.text(X(60), 350, "Qd = 60", "lbl bd", { "text-anchor": "middle", ...op(s.q) });
  if (s.sh > 0) o += SV.rect(X(20), Y(40) - 7, X(60) - X(20), 14, "f2", op(s.sh)) + SV.text((X(20) + X(60)) / 2, Y(40) - 16, "Shortage = 40", "lbl bd t2", { "text-anchor": "middle", ...halo, ...op(s.sh) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 780 370" role="img" aria-label="Supply and demand with a maximum price at 40 causing a shortage, and a minimum price at 80 causing a surplus">${axes()}${marketLines({ d: 1, s: 1 })}${eqMark({ eq: 1 })}
  ${SV.line(70, Y(40), X(90), Y(40), "c4", { "stroke-width": 3 })}${SV.text(X(90) - 4, Y(40) + 18, "Maximum price $40: shortage 40", "lbl bd t4", { "text-anchor": "end", ...halo })}
  ${SV.line(70, Y(80), X(90), Y(80), "c3", { "stroke-width": 3 })}${SV.text(X(90) - 4, Y(80) - 8, "Minimum price $80: surplus 40", "lbl bd t3", { "text-anchor": "end", ...halo })}
  ${SV.rect(X(20), Y(40) - 6, X(60) - X(20), 12, "f2")}${SV.rect(X(20), Y(80) - 6, X(60) - X(20), 12, "f3")}</svg>`;
Lib.stepper($("#stA"), { w: 780, h: 370, label: "A maximum price below the equilibrium price causing a shortage", base: { d: 0, s: 0, eq: 0, c: 0, q: 0, sh: 0 }, draw: ceilingDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The free market.</b> Demand meets supply at <b>$60</b> and <b>40 units</b>. There is no shortage or surplus.", s: { d: 1, s: 1, eq: 1 } },
  { cap: "<b>The government sets a maximum price of $40</b>, below the equilibrium price, to make the good more affordable. The line is a legal limit.", s: { d: 1, s: 1, eq: 1, c: 1 } },
  { cap: "<b>Quantities at $40.</b> Consumers now want <b>60</b> units (Qd). But at that price firms are only willing to supply <b>20</b> (Qs).", s: { d: 1, s: 1, eq: 1, c: 1, q: 1 } },
  { cap: "<b>A shortage of 40.</b> Only 20 units are traded. Goods must be rationed by queues, favouritism or a <b>black market</b>, and suppliers may cut quality or leave the market. Consumers who get the good gain, others lose out.", s: { d: 1, s: 1, eq: 1, c: 1, q: 1, sh: 1 } },
] });

/* minimum price (Watch 2) */
function floorDraw(s) {
  let o = axes() + marketLines(s) + eqMark(s);
  if (s.c > 0) o += SV.line(70, Y(80), X(90), Y(80), "c3", { "stroke-width": 3, ...op(s.c) }) + SV.text(X(90) - 4, Y(80) - 8, "Minimum price $80", "lbl bd t3", { "text-anchor": "end", ...op(s.c) });
  if (s.q > 0) o += SV.line(X(20), Y(80), X(20), 330, "gr", op(s.q)) + SV.line(X(60), Y(80), X(60), 330, "gr", op(s.q)) + SV.circle(X(20), Y(80), 6, "dot1", op(s.q)) + SV.circle(X(60), Y(80), 6, "dot2", op(s.q)) + SV.text(X(20), 350, "Qd = 20", "lbl bd", { "text-anchor": "middle", ...op(s.q) }) + SV.text(X(60), 350, "Qs = 60", "lbl bd", { "text-anchor": "middle", ...op(s.q) });
  if (s.sh > 0) o += SV.rect(X(20), Y(80) - 7, X(60) - X(20), 14, "f3", op(s.sh)) + SV.text((X(20) + X(60)) / 2, Y(80) - 16, "Surplus = 40", "lbl bd t3", { "text-anchor": "middle", ...halo, ...op(s.sh) });
  return o;
}
Lib.stepper($("#stB"), { w: 780, h: 370, label: "A minimum price above the equilibrium price causing a surplus", base: { d: 0, s: 0, eq: 0, c: 0, q: 0, sh: 0 }, draw: floorDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The free market.</b> Equilibrium at $60 and 40 units.", s: { d: 1, s: 1, eq: 1 } },
  { cap: "<b>The government sets a minimum price of $80</b>, above the equilibrium price. For example to raise farmers' incomes, or to cut consumption of a demerit good such as cheap alcohol.", s: { d: 1, s: 1, eq: 1, c: 1 } },
  { cap: "<b>Quantities at $80.</b> Consumers buy only <b>20</b> (Qd). Firms want to supply <b>60</b> (Qs).", s: { d: 1, s: 1, eq: 1, c: 1, q: 1 } },
  { cap: "<b>A surplus of 40.</b> Producers are left with unsold stock. The government may have to buy and store it, or it goes to waste. Consumers pay more and buy less; producers who sell gain.", s: { d: 1, s: 1, eq: 1, c: 1, q: 1, sh: 1 } },
] });

/* indirect tax (Watch 3) */
function taxDraw(s) {
  let o = axes() + marketLines(s) + eqMark(s);
  if (s.tax > 0) o += SV.line(X(0), Y(40), X(80), Y(120), "c4", { "stroke-dasharray": "6 5", ...op(s.tax) }) + SV.text(X(60), Y(100) - 0, "S + tax $20", "lbl bd t4", { ...halo, ...op(s.tax) });
  if (s.res > 0) o += SV.rect(70, Y(70), X(30) - 70, Y(60) - Y(70), "f1", op(s.res)) + SV.rect(70, Y(60), X(30) - 70, Y(50) - Y(60), "f4", op(s.res)) +
    SV.poly([[X(30), Y(70)], [X(30), Y(50)], [X(40), Y(60)]], "f2", op(s.res)) + SV.line(X(30), Y(70), X(30), 330, "gr", op(s.res)) + SV.circle(X(30), Y(70), 6, "dot4", op(s.res)) + SV.circle(X(30), Y(50), 6, "dot4", op(s.res)) +
    SV.text(66, Y(70) + 4, "70", "sm bd", { "text-anchor": "end", ...op(s.res) }) + SV.text(66, Y(50) + 4, "50", "sm bd", { "text-anchor": "end", ...op(s.res) }) + SV.text(X(30), 350, "30", "lbl bd", { "text-anchor": "middle", ...op(s.res) }) +
    SV.text(X(15), Y(65) + 4, "paid by consumers $10", "lbl bd t1", { "text-anchor": "middle", ...halo, ...op(s.res) }) + SV.text(X(15), Y(55) + 4, "paid by producers $10", "lbl bd t4", { "text-anchor": "middle", ...halo, ...op(s.res) }) + SV.text(X(30) + 12, Y(60) - 14, "welfare loss", "sm bd t2", { ...halo, ...op(s.res) });
  return o;
}
Lib.stepper($("#stC"), { w: 780, h: 370, label: "A per unit tax shifting supply up and the burden shared between consumers and producers", base: { d: 0, s: 0, eq: 0, tax: 0, res: 0 }, draw: taxDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The free market.</b> Equilibrium at $60 and 40 units.", s: { d: 1, s: 1, eq: 1 } },
  { cap: "<b>The tax.</b> A tax of $20 on each unit sold raises every supplier's cost by $20, so the supply curve shifts <b>up by $20</b> (a vertical distance equal to the tax).", s: { d: 1, s: 1, eq: 0.6, tax: 1 } },
  { cap: "<b>The new equilibrium.</b> Consumers now pay <b>$70</b> and quantity falls to <b>30</b>. Producers receive $70 − $20 = <b>$50</b> after paying the tax. Each side bears $10 of the $20: the burden is shared equally here because demand and supply have equal slopes.", s: { d: 1, s: 1, eq: 0.6, tax: 1, res: 1 } },
  { cap: "<b>Tax revenue</b> is $20 × 30 = <b>$600</b>. The red triangle is the <b>welfare loss</b> from the fall in output, the units between 30 and 40 that were worth more than they cost. If the tax is set equal to an external cost, this loss is more than offset by correcting the externality.", s: { d: 1, s: 1, eq: 0.6, tax: 1, res: 1 } },
] });

/* ---------- Lab 1: price control ---------- */
function lab1() {
  if (!$("#pc")) return;
  const p = +$("#pc").value, qd = Math.max(0, 100 - p), qs = Math.max(0, p - 20), tr = Math.min(qd, qs), gap = qd - qs;
  $("#r1").textContent = qd; $("#r2").textContent = qs; $("#r3").textContent = gap === 0 ? "none" : gap > 0 ? "shortage " + gap : "surplus " + -gap; $("#r4").textContent = tr;
  $("#rv").textContent = p === 60 ? "The price equals the market price, so there is no shortage or surplus: the control has no effect."
    : p < 60 ? `A maximum price at $${p} is below the market price. Consumers want ${qd} but suppliers offer only ${qs}: a shortage of ${gap}. Only ${tr} units are traded, so some buyers go without or pay on a black market.`
    : `A minimum price at $${p} is above the market price. Consumers buy only ${qd} but suppliers offer ${qs}: a surplus of ${-gap}. Only ${tr} units are sold.`;
  const x = (v) => 40 + v * 3.9, y = (v) => 270 - v * 2.4;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "Price ($)", "sm");
  o += SV.line(x(0), y(100), x(90), y(10), "c1") + SV.line(x(0), y(20), x(80), y(100), "c2") + SV.line(40, y(p), 400, y(p), p < 60 ? "c4" : p > 60 ? "c3" : "gr", { "stroke-width": 3 });
  if (gap !== 0) o += SV.rect(x(Math.min(qd, qs)), y(p) - 6, Math.abs(x(qd) - x(qs)), 12, gap > 0 ? "f2" : "f3");
  o += SV.circle(x(qd), y(p), 6, "dot1") + SV.circle(x(qs), y(p), 6, "dot2") + SV.text(x(qd), 288, "Qd", "sm bd t1", { "text-anchor": "middle" }) + SV.text(x(qs), 306, "Qs", "sm bd t2", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pc", label: "Legal price ($): ", min: 20, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: lab1 });

/* ---------- Lab 2: tax incidence ---------- */
function lab2() {
  if (!$("#tx") || !$("#kk")) return;
  const t = +$("#tx").value, k = +$("#kk").value, q0 = 80 / (1 + k), p0 = 100 - q0, q1 = (80 - t) / (1 + k), pc = 100 - q1, pp = pc - t;
  $("#s1").textContent = "$" + Lib.fmtN(pc, 1); $("#s2").textContent = "$" + Lib.fmtN(pp, 1); $("#s3").textContent = t === 0 ? "–" : Math.round(((pc - p0) / t) * 100) + "%"; $("#s4").textContent = "$" + Lib.fmtN(t * q1, 0);
  $("#sv").textContent = t === 0 ? "No tax: the market is at its equilibrium."
    : k < 0.9 ? `Supply is flat (elastic). Producers can cut output easily, so most of the tax is passed on: consumers pay $${Lib.fmtN(pc - p0, 1)} of the $${t}. Quantity falls from ${Lib.fmtN(q0, 1)} to ${Lib.fmtN(q1, 1)}.`
    : k > 1.1 ? `Supply is steep (inelastic). Producers cannot adjust output easily, so they bear most of the tax: consumers pay $${Lib.fmtN(pc - p0, 1)} of the $${t}.`
    : `Supply and demand have equal slopes, so the tax is shared equally: consumers pay $${Lib.fmtN(pc - p0, 1)} and producers $${Lib.fmtN(p0 - pp, 1)}.`;
  const x = (v) => 40 + v * 3.6, y = (v) => 270 - v * 2.4;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "Price ($)", "sm");
  o += SV.rect(40, y(pc), x(q1) - 40, y(p0) - y(pc), "f1") + SV.rect(40, y(p0), x(q1) - 40, y(pp) - y(p0), "f4");
  const sy = (q, add) => 20 + add + k * q;
  o += SV.line(x(0), y(100), x(100), y(0), "c1") + SV.line(x(0), y(20), x(Math.min(100, 80 / k)), y(sy(Math.min(100, 80 / k), 0)), "c2") + (t > 0 ? SV.line(x(0), y(20 + t), x(Math.min(100, (100 - 20 - t) / k)), y(sy(Math.min(100, (100 - 20 - t) / k), t)), "c4", { "stroke-dasharray": "6 5" }) : "");
  o += SV.circle(x(q1), y(pc), 6, "dot1") + SV.circle(x(q1), y(pp), 6, "dot4") + SV.text(x(q1) + 10, y(pc) - 6, "consumers pay", "sm bd t1") + SV.text(x(q1) + 10, y(pp) + 16, "producers receive", "sm bd t4");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "tx", label: "Tax per unit ($): ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v, onInput: lab2 });
Lib.slider($("#g3"), { id: "kk", label: "Supply steepness (1 = same as demand): ", min: 0.25, max: 4, step: 0.25, value: 1, fmt: (v) => Lib.fmtN(v, 2), onInput: lab2 });

/* ---------- Lab 3: permits ---------- */
function lab3() {
  if (!$("#pp")) return;
  const p = +$("#pp").value, trade = p > 2 && p < 8, a = trade ? 20 - 5 * p : 10, b = trade ? 5 * p : 40, tot = trade ? 20 : 50;
  $("#t1").textContent = "$" + Lib.fmtN(a, 1); $("#t2").textContent = "$" + Lib.fmtN(b, 1); $("#t3").textContent = "$" + tot;
  $("#tv").textContent = trade ? `At $${p} a permit, A abates all 10 units (cost $20) and sells 5 permits for $${Lib.fmtN(5 * p, 1)}. B buys them instead of cutting its own pollution. The cap of 10 is still met, but the real cost falls from $50 to $20 and both firms gain: a saving of $30 shared out by the permit price.`
    : p <= 2 ? "At $2 or less, A will not sell permits (it costs A $2 to cut a unit, so the permit must fetch more than that). No trade: each firm cuts 5 units, costing $50 in all."
    : "At $8 or more, B will not buy (it is cheaper for B to cut a unit at $8). No trade: each firm cuts 5 units, costing $50 in all.";
  const H = (v) => 150 * (v / 50), bw = 70;
  let o = SV.line(30, 190, 400, 190) + SV.text(32, 22, "Cost ($)", "sm");
  [[40, a, "f1", "Firm A net"], [140, b, "f4", "Firm B net"], [240, tot, trade ? "f3" : "f2", "Total real cost"]].forEach(([x, v, c, l]) => { const up = v >= 0, h = Math.abs(H(v)); o += SV.rect(x, up ? 190 - h : 190, bw, h, c) + SV.text(x + bw / 2, up ? 190 - h - 6 : 190 + h + 14, (up ? "" : "−") + "$" + Lib.fmtN(Math.abs(v), 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 236, l, "sm", { "text-anchor": "middle" }); });
  o += SV.line(240, 190 - H(50), 240 + bw, 190 - H(50), "gr", { "stroke-dasharray": "4 3" }) + SV.text(240 + bw + 6, 190 - H(50) + 4, "no trade: 50", "sm");
  $("#labC").innerHTML = o;
}
Lib.slider($("#g4"), { id: "pp", label: "Permit price ($): ", min: 0, max: 10, step: 0.5, value: 5, fmt: (v) => v, onInput: lab3 });

/* ---------- Lab 4: getting the tax right ---------- */
function lab4() {
  if (!$("#ge")) return;
  const e = +$("#ge").value, q = (80 - e) / 1.5, qs = 65 / 1.5;
  const loss = q > qs ? 0.5 * (q - qs) * (1.5 * q - 65) : 0.5 * (qs - q) * (65 - 1.5 * q), better = loss < 74.9;
  $("#u1").textContent = Lib.fmtN(q, 1); $("#u2").textContent = Lib.fmtN(loss, 0); $("#u3").textContent = Math.abs(loss - 75) < 0.5 ? "Same" : better ? "Yes" : "No: worse";
  $("#uv").textContent = e === 15 ? "The estimate equals the true external cost ($15): output is at the social optimum and the welfare loss is zero."
    : e === 0 ? "No tax. Output is above the optimum and the welfare loss is 75."
    : e < 15 ? `The tax ($${e}) is too low. Output is still above the optimum, but the loss is smaller than with no tax.`
    : better ? `The tax ($${e}) is too high. It overcorrects: output is now below the optimum. The loss is still less than doing nothing.`
    : `The tax ($${e}) is far too high. It cuts output well below the social optimum, and the welfare loss ($${Lib.fmtN(loss, 0)}) is greater than doing nothing. This is government failure caused by poor information.`;
  const H = (v) => 170 * (v / 300), bw = 90;
  let o = SV.line(30, 200, 400, 200) + SV.text(32, 22, "Welfare loss", "sm");
  [[60, 75, "f2", "No tax"], [210, loss, better ? "f3" : "f4", "With the government's tax"]].forEach(([x, v, c, l]) => { o += SV.rect(x, 200 - H(v), bw, H(v), c) + SV.text(x + bw / 2, 200 - H(v) - 6, Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 218, l, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g5"), { id: "ge", label: "Government's estimate of the external cost ($): ", min: 0, max: 45, step: 1, value: 25, fmt: (v) => v, onInput: lab4 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "What type of policy is each one?",
  buckets: [{ label: "Price-based (market tool)" }, { label: "Regulation and legal limits" }, { label: "Provision and ownership" }, { label: "Information and nudges" }],
  items: [
    { text: "A tax on carbon emissions", b: 0 }, { text: "A subsidy for solar panels", b: 0 }, { text: "Tradable pollution permits", b: 0 }, { text: "A minimum price for alcohol", b: 0 },
    { text: "A ban on new petrol cars", b: 1 }, { text: "Emission standards for factories", b: 1 }, { text: "Competition law blocking a merger", b: 1 },
    { text: "Free vaccination provided by the state", b: 2 }, { text: "Nationalising the railways", b: 2 },
    { text: "Opt-out organ donation", b: 3 }, { text: "Health warnings on cigarette packs", b: 3 }, { text: "Fruit placed at eye level in canteens", b: 3 },
  ], done: "A nudge changes how choices are presented without forcing them; taxes and bans are not nudges.",
});
Lib.classify($("#cl2"), {
  prompt: "Which market failure does each policy best fit?",
  buckets: [{ label: "Negative externality" }, { label: "Merit good / positive externality" }, { label: "Public good" }, { label: "Monopoly power" }, { label: "Information failure" }],
  items: [
    { text: "A per-unit tax on pollution", b: 0 }, { text: "Tradable emission permits", b: 0 },
    { text: "A subsidy for vaccination", b: 1 }, { text: "Free state education", b: 1 },
    { text: "Street lighting provided by the local authority", b: 2 }, { text: "National defence funded by taxation", b: 2 },
    { text: "A price cap on a water monopoly", b: 3 }, { text: "Breaking up a cartel", b: 3 },
    { text: "Compulsory nutrition labels", b: 4 }, { text: "An advertising campaign on the risks of smoking", b: 4 },
  ], done: "Match the tool to the cause, then weigh it against its costs and government failure.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Maximum price", "A legal limit below the market price, causing a shortage"],
  ["Minimum price", "A legal floor above the market price, causing a surplus"],
  ["Tax incidence", "How the burden of a tax is shared between buyers and sellers"],
  ["Tradable permits", "A cap on pollution with permits that firms can buy and sell"],
  ["Nudge", "A change in how choices are presented that influences behaviour without forcing it"],
  ["Privatisation", "Selling state-owned firms to the private sector"],
  ["Natural monopoly", "An industry where one firm is cheapest because of very high fixed costs"],
  ["Government failure", "Intervention that leaves resources less efficiently used"],
], done: "These eight words cover most of the chapter." });
Lib.order($("#o1"), { prompt: "Put the explanation of a maximum price in order.", items: [
  "The government sets a maximum price below the equilibrium price",
  "At the lower price the quantity demanded rises",
  "At the lower price the quantity supplied falls",
  "Quantity demanded is greater than quantity supplied: a shortage",
  "The good must be rationed, and black markets and lower quality may appear",
  "Evaluate: who gains (those who get the good), who loses, and alternatives such as subsidies",
], done: "This chain works for any price ceiling question, for example rent control." });
Lib.calc($("#c1"), { qs: [
  { q: "Demand is P = 100 − Q and supply is P = 20 + Q. A maximum price of $40 is set. What is the shortage (units)?", a: 40, hint: "Qd = 100 − P and Qs = P − 20.", sol: "Qd = 60, Qs = 20, shortage = <b>40</b>." },
  { q: "A minimum price of $80 is set in the same market. What is the surplus (units)?", a: 40, sol: "Qd = 20, Qs = 60, surplus = <b>40</b>." },
  { q: "A $20 tax shifts supply to P = 40 + Q. What is the new quantity?", a: 30, sol: "100 − Q = 40 + Q gives Q = <b>30</b>." },
  { q: "What is the government's tax revenue ($)?", a: 600, sol: "20 × 30 = <b>$600</b>." },
  { q: "The price consumers pay rises from $60 to $70. What share of the $20 tax do consumers bear (%)?", a: 50, sol: "10 ÷ 20 × 100 = <b>50%</b>." },
  { q: "Without trading each firm cuts 5 units: A at $2 and B at $8 a unit. With trading A cuts all 10 units. By how much does the total cost fall ($)?", a: 30, sol: "Before: 5×2 + 5×8 = 50. After: 10×2 = 20. Fall = <b>$30</b>." },
  { q: "A subsidy of $10 a unit raises output to 50 units. What is the cost to the government ($)?", a: 500, sol: "10 × 50 = <b>$500</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A maximum price set below the equilibrium price causes:", opts: ["a surplus", "a shortage", "no change", "a rise in supply"], a: 1, why: "At a lower price, quantity demanded rises and quantity supplied falls." },
  { q: "A minimum price on alcohol is mainly intended to:", opts: ["raise supply", "reduce consumption of a demerit good", "lower prices", "create a shortage"], a: 1, why: "A floor above the market price reduces quantity demanded." },
  { q: "A per-unit tax on a good with inelastic demand will mostly:", opts: ["cut quantity sharply", "raise the price paid by consumers and cut quantity little", "reduce the price paid by consumers", "have no effect on government revenue"], a: 1, why: "Consumers bear most of the burden and quantity changes little." },
  { q: "Tradable pollution permits are most likely to:", opts: ["remove the cap on emissions", "meet a pollution cap at lower total cost", "raise emissions", "make permits free for ever"], a: 1, why: "Firms with low abatement costs cut more and sell permits." },
  { q: "Which is an example of a nudge?", opts: ["A tax on sugary drinks", "A ban on smoking indoors", "An opt-out organ donation system", "A subsidy for fruit"], a: 2, why: "Changing the default influences choice without forcing it." },
  { q: "Privatising a natural monopoly may lead to:", opts: ["perfect competition at once", "a private monopoly that needs regulation", "no change in ownership", "zero profit"], a: 1, why: "Competition is unrealistic on a network, so a regulator is usually needed." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Indirect tax", "A tax on spending, which shifts supply up by the amount of the tax."],
  ["Subsidy", "A payment that lowers firms' costs, shifting supply down."],
  ["Maximum price", "A legal limit below equilibrium: causes a shortage."],
  ["Minimum price", "A legal floor above equilibrium: causes a surplus."],
  ["Tax incidence", "Who actually bears the burden of a tax, decided by elasticities."],
  ["Tradable permits", "A cap on total pollution with permits that can be traded."],
  ["Regulation", "Legal rules such as bans, standards, price caps and competition law."],
  ["State provision", "The government supplies the good, funded from taxation."],
  ["Nudge", "A change in the presentation of choices that influences behaviour without forcing it."],
  ["Privatisation", "Selling state-owned firms to the private sector."],
  ["Nationalisation", "Taking private firms into state ownership."],
  ["Natural monopoly", "A market where one firm is cheapest because of very high fixed costs."],
  ["Competition policy", "Laws on mergers and cartels to protect competition."],
  ["Cross-subsidisation", "Charging high prices to some consumers to fund low prices for others."],
  ["Government failure", "Intervention that makes the allocation of resources worse or no better."],
] });

/* ---------- Past paper MCQ (text) ---------- */
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2022 · 31 · Q10] In which circumstance would direct provision of a product by the government be least likely?", opts: ["when fixed costs are very high", "when the demand for the product is very high but unit costs are low", "when the industry faces large natural barriers to entry", "when the minimum efficient scale of production is above the level of demand at current prices"], a: 1, why: "Direct provision is most likely where private firms would not enter (high fixed costs, natural barriers, small demand). High demand and low unit costs mean private firms would supply it." },
  { q: "[May/June 2022 · 31 · Q15] What is an example of 'nudge' theory when applied to encouraging healthy eating?", opts: ["advertising the benefits of healthy eating", "increasing tax on sugary foods", "introducing a subsidy for fruit growers", "supermarkets putting fruit near cash registers"], a: 3, why: "A nudge changes how choices are presented without forcing them. Advertising is information, a tax and subsidy are price tools." },
  { q: "[Feb/March 2022 · 32 · Q14] What would be an example of 'nudge' theory?", opts: ["a subsidy on fresh fruit to increase demand", "a unit tax on unhealthy food to reduce demand", "banning all unhealthy food to reduce demand", "putting fresh fruit at eye level in shops to increase demand"], a: 3, why: "Placing fruit at eye level changes the choice environment but leaves people free." },
  { q: "[May/June 2022 · 32 · Q14] What is not an example of the application of 'nudge' theory?", opts: ["A chain of coffee shops offers its customers a larger coffee if they bring their own reusable cup.", "A government imposes an indirect tax on the purchase of sugary snacks, to try to reduce childhood obesity.", "A government introduces an opt-out system for organ donation, to try to increase the number of organs donated.", "A restaurant chain introduces smaller-sized main courses on its menu, to try to reduce the amount of food wasted."], a: 1, why: "A tax changes the price (and the budget), so it is not a nudge." },
  { q: "[May/June 2023 · 31 · Q12] One reason for market failure is the existence of public goods. Which policy option is appropriate for addressing such a market failure?", opts: ["direct provision of the good by the government", "provision of detailed information to consumers", "subsidising firms that currently produce the good", "the adoption of maximum price controls"], a: 0, why: "The free-rider problem means the market will not supply public goods, so the state provides them." },
  { q: "[May/June 2023 · 31 · Q13] In 2020, the governor of California issued an order to ban the sale of new vehicles from 2035 that are powered by petrol or diesel fuel. Which type of government policy is this?", opts: ["a nudge", "a permit to pollute", "nationalisation", "regulation"], a: 3, why: "A legal ban is regulation." },
  { q: "[May/June 2023 · 32 · Q17] A government imposes a maximum price for electricity. Which statement justifying this measure might be considered valid on economic grounds?", opts: ["It will encourage electricity suppliers to invest in additional capacity.", "It will increase the incentive for consumers to conserve energy.", "It will prevent the monopolistic exploitation of consumers.", "It will prevent the rationing of electricity through power cuts."], a: 2, why: "A price cap can limit the price a monopoly supplier charges. A, B and D are the opposite of what a ceiling does." },
  { q: "[Feb/March 2024 · 32 · Q11] A government wishes to use market forces to remove a negative externality in the consumption of a good. Which policy is likely to be the most effective?", opts: ["It should provide information about the undesirable side-effects of the good.", "It should give producers a subsidy, to allow consumers to purchase the product more cheaply.", "It should impose an indirect tax on consumers, to reduce consumption to the socially efficient level.", "It should not interfere at all, to allow the free market to generate maximum efficiency."], a: 2, why: "A tax uses the price mechanism (market forces) to cut consumption to the efficient level. A subsidy would raise it." },
  { q: "[Feb/March 2024 · 32 · Q13] What is a failure of government microeconomic intervention?", opts: ["An indirect tax equal to external costs is imposed on cigarettes and the demand falls.", "Limits are placed on a trade union's restrictions that increase labour mobility.", "Price controls on bread are removed which allow a free market to operate.", "Tariffs are imposed on imported goods which cause the Gini coefficient to increase."], a: 3, why: "The tariffs made inequality worse: an unintended harmful side-effect. A, B and C are successful or neutral." },
  { q: "[May/June 2024 · 33 · Q11] The government can use policies to reduce the environmental damage caused by the amount of rubbish created by firms and households. Which policy is most likely to lead to government failure?", opts: ["an incentive payment for firms who reduce the levels of rubbish", "a tax on the amount of rubbish a firm or household creates", "an advertising campaign about the problems created by rubbish", "government grants to firms researching how to safely dispose of rubbish"], a: 1, why: "Taxing rubbish can lead to fly-tipping, so it may increase the problem and be costly to monitor." },
  { q: "[Feb/March 2020 · 32 · Q12] A government divides a nationalised rail service and sells it to five private companies. The largest dominates the four smaller companies. How will these changes affect the market structure for rail services?", opts: ["It will change from monopoly to monopolistic competition.", "It will create an oligopoly with the possibility of price leadership.", "It will encourage freedom of entry due to lower capital costs.", "It will guarantee ticket prices based on average costs."], a: 1, why: "Five firms with one dominant firm form an oligopoly in which the large firm may act as price leader." },
  { q: "[May/June 2020 (not sat) · 31 · Q13] Which policy is not designed to correct a market failure?", opts: ["government provision of healthcare", "price controls on large firms", "regulations to limit smoke pollution", "removing import quotas"], a: 3, why: "Removing import quotas is a trade liberalisation measure. The others address merit goods, monopoly power and an externality." },
] });
