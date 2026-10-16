const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const QX = (q) => 80 + 6 * q, PY = (p) => 360 - 2.7 * p;
function seg(m, c) { // clip P = mQ + c to 0<=Q<=100, 0<=P<=120
  let lo = 0, hi = 100;
  if (m !== 0) { const a = (0 - c) / m, z = (120 - c) / m; lo = Math.max(lo, Math.min(a, z)); hi = Math.min(hi, Math.max(a, z)); }
  return [lo, m * lo + c, hi, m * hi + c];
}
function curve(m, c, cls, label, o = {}) {
  const [q1, p1, q2, p2] = seg(m, c);
  if (q2 <= q1) return "";
  let s = SV.line(QX(q1), PY(p1), QX(q2), PY(p2), cls, o.attrs);
  if (label) { const a = { "text-anchor": "start" }; if (o.attrs && o.attrs.opacity !== undefined) a.opacity = o.attrs.opacity; s += SV.text(QX(q2) + (o.dx ?? 6), PY(p2) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), a); }
  return s;
}
function axes(yl = "Price", xl = "Quantity") {
  return SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) +
    SV.text(QX(0) + 6, PY(120) + 6, yl, "sm") + SV.text(QX(104), PY(0) + 22, xl, "sm", { "text-anchor": "end" });
}
const hline = (p, c = "gr", x2 = 100) => SV.line(QX(0), PY(p), QX(x2), PY(p), c);
const vline = (q, p, c = "gr") => SV.line(QX(q), PY(p), QX(q), PY(0), c);
const ylab = (p, t, c = "sm") => SV.text(QX(0) - 8, PY(p) + 4, t, c, { "text-anchor": "end" });
const xlab = (q, t, c = "sm") => SV.text(QX(q), PY(0) + 18, t, c, { "text-anchor": "middle" });
const money = (v, d = 1) => Lib.fmtN(v, d);
const halo = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
/* ---------- 1. interest rate chains ---------- */
const CHAINS = {
  cut: ["Central bank cuts the base interest rate", "Borrowing is cheaper and saving pays less", "Households spend more (C ↑) and firms invest more (I ↑)", "The currency may fall, making exports cheaper (X − M ↑)", "Aggregate demand shifts to the right", "Real GDP ↑, jobs ↑, price level ↑ a little"],
  rise: ["Central bank raises the base interest rate", "Borrowing costs more and saving pays more", "Households spend less (C ↓) and firms invest less (I ↓)", "The currency may rise, making exports dearer (X − M ↓)", "Aggregate demand shifts to the left", "Inflation pressure ↓, but growth ↓ and jobs at risk"],
};
function chainChart(s) {
  const list = CHAINS[s.kind], bh = 46, gap = 14, x = 110, w = 540, col = s.kind === "cut" ? "--good" : "--bad";
  let o = "";
  list.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1);
    if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:15px" });
    if (i < list.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 400, label: "How interest rate changes reach aggregate demand", base: { n: 0, kind: "cut" }, draw: chainChart, steps: [
  { cap: "The central bank sets the <b>base interest rate</b>. Here it <b>cuts</b> it, for example from 5% to 3%. Commercial banks usually follow with lower loan and saving rates.", s: { n: 1, kind: "cut" } },
  { cap: "Loans, credit cards and mortgages <b>cost less</b>, and saving <b>pays less</b>. Spending is more attractive than saving.", s: { n: 2, kind: "cut" } },
  { cap: "Households are likely to <b>spend more</b> (consumption rises) and, with cheaper loans, more investment projects look profitable so firms may <b>invest more</b>.", s: { n: 3, kind: "cut" } },
  { cap: "Lower returns on deposits make the currency less attractive, so its value <b>may fall</b>. Exports become cheaper abroad and imports dearer: <b>X − M could improve</b>.", s: { n: 4, kind: "cut" } },
  { cap: "C, I and X − M all point the same way: <b>aggregate demand shifts right</b>.", s: { n: 5, kind: "cut" } },
  { cap: "Real GDP rises (<b>growth</b>), firms need more workers (<b>jobs</b>) and the price level edges up. <b>Evaluate:</b> the effect takes time, and it is weak if confidence is low.", s: { n: 6, kind: "cut" } },
  { cap: "Now the reverse. To cool an overheating economy the central bank <b>raises</b> the rate. Borrowing costs more, saving pays more.", s: { n: 2, kind: "rise" } },
  { cap: "Spending and investment fall, the currency may rise, <b>AD shifts left</b>. Inflation pressure eases, but <b>growth slows and unemployment may rise</b>: the trade-off.", s: { n: 6, kind: "rise" } },
] });

/* ---------- 2. money market ---------- */
function moneyChart(s) {
  const q = s.q, q0 = s.q0, r = 120 - q, moved = Math.abs(q - q0) > 1;
  let o = axes("", "Quantity of money") + SV.text(QX(0) - 6, PY(120) + 6, "Interest rate", "sm", { "text-anchor": "end" });
  o += curve(-1, 120, "c1") + SV.text(QX(24), PY(96) - 10, "Demand for money", "lbl bd t1");
  if (moved) o += SV.line(QX(q0), PY(0), QX(q0), PY(112), "c3", { opacity: 0.4 }) + SV.text(QX(q0), PY(112) - 8, "MS", "lbl bd t3", { "text-anchor": "middle", opacity: 0.5 });
  o += SV.line(QX(q), PY(0), QX(q), PY(112), moved ? (q > q0 ? "c2" : "c4") : "c3") + SV.text(QX(q), PY(112) - 8, moved ? "MS₁" : "MS", "lbl bd " + (moved ? (q > q0 ? "t2" : "t4") : "t3"), { "text-anchor": "middle" });
  if (moved) o += hline(120 - q0, "gr", q0) + SV.circle(QX(q0), PY(120 - q0), 6, "dot1", { opacity: 0.45 }) + ylab(120 - q0, "6%", "sm");
  o += hline(r, "gr", q) + SV.circle(QX(q), PY(r), 6, moved ? (q > q0 ? "dot2" : "dot4") : "dot1") + ylab(r, money(r / 10, 0) + "%", "sm bd");
  return o;
}
Lib.stepper($("#stMS"), { w: 760, h: 400, label: "The money supply and the interest rate", base: { q: 60, q0: 60 }, draw: moneyChart, steps: [
  { cap: "The money market: people and firms want to hold money, and they hold less of it when interest rates are high (the <b>demand for money</b> slopes down). The central bank fixes the <b>money supply (MS)</b>. They meet at an interest rate of <b>6%</b>.", s: { q: 60, q0: 60 } },
  { cap: "The central bank <b>increases the money supply</b>, for example by buying government bonds from banks. MS shifts right and the interest rate falls to <b>4%</b>.", s: { q: 80, q0: 60 } },
  { cap: "Banks have more to lend and borrowing is cheaper, so <b>consumption and investment are likely to rise</b>. <b>Evaluate:</b> too big an increase in a near-full economy could cause <b>demand-pull inflation</b>, and banks may refuse to lend if they are cautious.", s: { q: 80, q0: 60 } },
  { cap: "The opposite: the central bank <b>reduces the money supply</b> (for example by selling bonds). MS shifts left and the interest rate rises to <b>8%</b>. Spending is squeezed, which can help against inflation.", s: { q: 40, q0: 60 } },
] });

/* ---------- 3. exchange rate ---------- */
function fxChart(s) {
  const r = s.r, base = 330, k = 0.28, xp = 1000 * r, mp = 400 / r, r0 = 0.8;
  let o = SV.line(40, base, 720, base);
  o += SV.text(380, 34, "A$1 = US$" + r.toFixed(2), "lbl bd " + (r < r0 - 0.01 ? "t2" : r > r0 + 0.01 ? "t4" : "t1"), { "text-anchor": "middle", style: "font-size:20px" });
  const bar = (x, v, v0, col, top, bot) => {
    let g = SV.rect(x, base - v * k, 130, v * k, "", { style: `fill:var(${col})`, opacity: 0.85 });
    g += SV.rect(x, base - v0 * k, 130, v0 * k, "", { style: `fill:none;stroke:var(--muted);stroke-width:2;stroke-dasharray:6 4` });
    g += SV.text(x + 65, base - Math.max(v, v0) * k - 10, top, "lbl bd", { "text-anchor": "middle" });
    g += SV.text(x + 65, base + 22, bot, "sm", { "text-anchor": "middle" });
    return g;
  };
  o += bar(110, xp, 1000 * r0, "--good", "US$" + money(xp, 0), "Machine price abroad");
  o += bar(470, mp, 400 / r0, "--warn", "A$" + money(mp, 0), "Phone price at home");
  o += SV.text(175, base + 42, "(costs A$1,000 to make)", "sm", { "text-anchor": "middle" }) + SV.text(535, base + 42, "(costs US$400 abroad)", "sm", { "text-anchor": "middle" });
  if (s.vol) o += SV.text(175, 66, "Machines sold: " + money(s.vol[0], 0), "lbl bd t3", { "text-anchor": "middle" }) + SV.text(535, 66, "Phones bought: " + money(s.vol[1], 0), "lbl bd t3", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stX"), { w: 760, h: 400, label: "A fall in the exchange rate", base: { r: 0.8 }, draw: fxChart, steps: [
  { cap: "At <b>A$1 = US$0.80</b>, a machine that costs A$1,000 to make sells abroad for <b>US$800</b>. A phone that costs US$400 abroad costs <b>A$500</b> at home. The dashed outlines mark these starting prices.", s: { r: 0.8 } },
  { cap: "The Australian dollar <b>falls</b> to US$0.60 (a <b>depreciation</b>, or a <b>devaluation</b> if the central bank sets the rate). The same machine now costs <b>US$600</b> abroad: cheaper. The phone now costs <b>A$667</b> at home: dearer.", s: { r: 0.6 } },
  { cap: "Exports are <b>more competitive</b> and imports are <b>less attractive</b>. If demand is elastic, export sales rise, import purchases fall, and <b>X − M improves</b>. AD shifts right and jobs in exporting and import-competing firms could rise. <b>Evaluate:</b> imported inputs now cost more, which may push up prices.", s: { r: 0.6 } },
  { cap: "The reverse: if the currency <b>rises</b> to US$1.00 (an <b>appreciation</b>), the machine costs <b>US$1,000</b> abroad and the phone only <b>A$400</b>. Exporters struggle, imports are cheap, and inflation pressure eases.", s: { r: 1.0 } },
] });

/* Lab 1: interest rate and investment */
const PROJ = [2.5, 4, 5.5, 6.5, 7.5, 9, 10.5, 12];
function labI() {
  if (!$("#ia") || !$("#ib")) return;
  const r = +$("#ia").value, m = +$("#ib").value, hurdle = r + m, go = PROJ.filter((p) => p > hurdle).length;
  $("#ia1").textContent = go + " of 8"; $("#ia2").textContent = "$" + Math.round(200000 * r / 100).toLocaleString("en-US"); $("#ia3").textContent = "$" + Math.round(10000 * r / 100).toLocaleString("en-US");
  $("#iav").textContent = go === 0 ? "No project beats the cost of borrowing, so firms invest nothing new. Aggregate demand gets no support from investment." :
    go === 8 ? "Every project beats the cost of borrowing: investment spending is likely to be high, which raises aggregate demand." :
    `${go} project${go > 1 ? "s" : ""} earn more than the ${money(hurdle, 1)}% needed. Lower the interest rate and more bars turn green: that is how a rate cut raises investment. ${m >= 3 ? "Notice that a high risk margin keeps projects on hold even when rates are low: low confidence limits the power of a rate cut." : ""}`;
  const base = 350, k = 24, w = 62, x0 = 70;
  let o = SV.line(x0 - 10, base, 740, base) + SV.text(x0 - 10, 26, "Expected yearly return", "sm");
  PROJ.forEach((p, i) => {
    const x = x0 + i * 82, on = p > hurdle;
    o += SV.rect(x, base - p * k, w, p * k, "", { style: `fill:var(${on ? "--good" : "--muted"})`, opacity: on ? 0.85 : 0.4 });
    o += SV.text(x + w / 2, base - p * k - 8, p + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + w / 2, base + 20, "Project " + (i + 1), "sm", { "text-anchor": "middle" });
  });
  const y = base - hurdle * k;
  o += SV.line(x0 - 10, y, 740, y, "dash", { style: "stroke:var(--bad);stroke-width:2.5" });
  o += SV.text(740, y - 8, "Cost of borrowing " + money(r, 1) + "%" + (m ? " + risk " + money(m, 1) + "% = " + money(hurdle, 1) + "%" : ""), "lbl bd t2", { "text-anchor": "end", style: halo });
  $("#labI").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ia", label: "Interest rate", min: 0, max: 12, step: 0.5, value: 5, fmt: (v) => v + "%", onInput: labI });
Lib.slider($("#g2"), { id: "ib", label: "Risk margin firms demand (low confidence = high)", min: 0, max: 6, step: 0.5, value: 0, fmt: (v) => v + " points", onInput: labI });

/* Lab 2: exchange rate and trade */
function labX() {
  if (!$("#xa") || !$("#xb")) return;
  const r = +$("#xa").value, e = +$("#xb").value, r0 = 0.8;
  const xv = 100 * Math.pow(r / r0, -e), mv = 100 * Math.pow(r / r0, e), xp = 1000 * r, mp = 400 / r;
  const net = (1000 * xv - mp * mv) / 1000;
  $("#xa1").textContent = "US$" + money(xp, 0); $("#xa2").textContent = "A$" + money(mp, 0); $("#xa3").textContent = money(net, 1);
  let v;
  if (Math.abs(r - r0) < 0.03) v = "No change from the starting rate. Move the exchange rate to see prices and trade respond.";
  else if (r < r0) v = `A lower exchange rate cuts the price of machines abroad to US$${money(xp, 0)} and raises the home price of phones to A$${money(mp, 0)}. Machine sales rise to about ${money(xv, 0)} and phone purchases fall to about ${money(mv, 0)}. ${net > 50.5 ? "Net exports improve, so AD could rise." : "But with demand this inelastic, the extra phone bill outweighs the extra export income, so net exports get worse: elasticity matters."}`;
  else v = `A higher exchange rate raises the price of machines abroad to US$${money(xp, 0)} and cuts the home price of phones to A$${money(mp, 0)}. Machine sales fall to about ${money(xv, 0)} and phone purchases rise to about ${money(mv, 0)}. ${net < 49.5 ? "Net exports worsen, so AD could fall; cheaper imports help against inflation." : "With demand this inelastic, net exports still improve in this model, but exporters sell less."}`;
  $("#xav").textContent = v;
  $("#labX").innerHTML = fxChart({ r, vol: [xv, mv] });
}
Lib.slider($("#g3"), { id: "xa", label: "Exchange rate (US$ per A$1)", min: 0.5, max: 1.2, step: 0.05, value: 0.8, fmt: (v) => "US$" + v.toFixed(2), onInput: labX });
Lib.slider($("#g4"), { id: "xb", label: "Price sensitivity of buyers (elasticity)", min: 0.2, max: 2, step: 0.1, value: 1.2, fmt: (v) => v.toFixed(1) + (v < 1 ? " inelastic" : v > 1 ? " elastic" : ""), onInput: labX });


/* ================= PRACTISE ================= */
Lib.classify($("#cl2"), { prompt: "Which <b>monetary policy tool</b> is being used?", buckets: [{ label: "Interest rate" }, { label: "Money supply" }, { label: "Exchange rate" }], items: [
  { text: "Base rate cut from 4% to 2%", b: 0 }, { text: "Central bank lifts its lending rate to banks", b: 0 },
  { text: "Central bank buys bonds from banks", b: 1 }, { text: "Quantitative easing of $50bn", b: 1 },
  { text: "Government devalues the currency against the US dollar", b: 2 }, { text: "Central bank sells foreign currency reserves to defend its currency", b: 2 },
  { text: "Central bank prints extra notes", b: 1 }, { text: "Central bank raises rates to attract foreign savers", b: 0 },
], done: "Three tools: rates, money supply, exchange rate." });
Lib.classify($("#cl3"), { prompt: "Is each a result of a <b>lower</b> exchange rate (depreciation) or a <b>higher</b> exchange rate (appreciation)?", buckets: [{ label: "Lower exchange rate" }, { label: "Higher exchange rate" }], items: [
  { text: "Exports are cheaper for foreign buyers", b: 0 }, { text: "Imported raw materials cost more", b: 0 }, { text: "Exporters could take on more workers", b: 0 }, { text: "Cost-push inflation risk", b: 0 },
  { text: "Foreign holidays become cheaper for residents", b: 1 }, { text: "Domestic firms face more import competition", b: 1 }, { text: "Exporters may lose sales and cut jobs", b: 1 }, { text: "Inflation pressure from import prices eases", b: 1 },
], done: "Lower exchange rate helps exports; higher helps imports and inflation." });
Lib.classify($("#cl4"), { prompt: "Who is likely to <b>gain</b> from a <b>rise</b> in interest rates, and who is likely to <b>lose</b>?", buckets: [{ label: "Gains" }, { label: "Loses" }], items: [
  { text: "A pensioner with large savings", b: 0 }, { text: "A bank earning more on loans", b: 0 }, { text: "An importer when the currency rises", b: 0 }, { text: "A household with a variable rate mortgage", b: 1 },
  { text: "A firm planning to borrow to expand", b: 1 }, { text: "An exporter when the currency rises", b: 1 }, { text: "A government with a large national debt", b: 1 }, { text: "Someone saving to buy a car", b: 0 },
], done: "Savers and importers gain; borrowers and exporters lose." });
Lib.order($("#o1"), { prompt: "Put the chain for a <b>cut in interest rates</b> in order.", items: [
  "The central bank cuts the base interest rate",
  "Commercial banks lower loan and saving rates",
  "Borrowing is cheaper and saving is less attractive",
  "Households and firms increase spending and investment",
  "Aggregate demand shifts to the right",
  "Real GDP and employment rise; the price level may rise",
], done: "A full analysis chain." });
Lib.order($("#o2"), { prompt: "Put the chain for a <b>fall in the exchange rate</b> in order.", items: [
  "The currency falls against other currencies",
  "Exports become cheaper abroad and imports dearer at home",
  "Export demand rises and import demand falls",
  "Total demand for domestic output rises",
  "Firms earn more revenue and increase output",
  "Firms take on more workers and employment rises",
], done: "That is the mark scheme chain." });
Lib.match($("#m1"), { prompt: "Match the measure to what it does.", pairs: [
  ["Cut interest rates", "Cheaper borrowing, less reward for saving: spending is likely to rise"],
  ["Raise interest rates", "Costlier borrowing, more reward for saving: spending is likely to fall"],
  ["Increase money supply", "Banks have more to lend, which tends to push rates down"],
  ["Quantitative easing", "Central bank buys large amounts of bonds to raise the money supply"],
  ["Lower the exchange rate", "Exports cheaper abroad, imports dearer at home"],
  ["Raise the exchange rate", "Exports dearer abroad, imports cheaper at home"],
], done: "Link each measure to its effect." });
Lib.calc($("#c1"), { qs: [
  { q: "A saver deposits $5,000 at an interest rate of 4% a year. How much interest does she earn in one year ($)?", a: 200, sol: "5,000 × 4% = <b>$200</b>." },
  { q: "A firm borrows $50,000 at 6%. The central bank cuts the rate and the firm's rate falls to 4%. How much does it save in interest each year ($)?", a: 1000, hint: "Work out the interest at each rate.", sol: "At 6%: $3,000. At 4%: $2,000. Saving = <b>$1,000</b>." },
  { q: "The money supply is $800bn. It increases by 5%. What is the new money supply ($bn)?", a: 840, sol: "800 × 1.05 = <b>$840bn</b>." },
  { q: "A car costs €20,000 in Germany. The exchange rate is €1 = US$1.25. What does it cost in US dollars?", a: 25000, sol: "20,000 × 1.25 = <b>US$25,000</b>." },
  { q: "£1 = US$1.50. A UK machine costs £500. The pound falls to £1 = US$1.20. By what percentage does the US dollar price of the machine fall?", a: 20, hint: "Price before is $750.", sol: "Before: 500 × 1.50 = $750. After: 500 × 1.20 = $600. Fall = 150 ÷ 750 × 100 = <b>20%</b>." },
  { q: "A US phone costs US$300. £1 = US$1.50. What does it cost in pounds (£)?", a: 200, sol: "300 ÷ 1.50 = <b>£200</b>." },
  { q: "The pound now falls to £1 = US$1.20. What does the same US$300 phone cost in pounds (£)?", a: 250, sol: "300 ÷ 1.20 = <b>£250</b>: imports have become dearer after a fall." },
  { q: "The exchange rate was US$1.60 = £1 and falls to US$1.40 = £1. What is the percentage fall in the value of the pound? (1 d.p.)", a: 12.5, tol: 0.1, sol: "(1.60 − 1.40) ÷ 1.60 × 100 = <b>12.5%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a monetary policy measure?", opts: ["A change in income tax rates", "A change in government spending on roads", "A change in interest rates", "A change in subsidies to farmers"], a: 2, why: "Interest rates, money supply and the exchange rate are the monetary tools." },
  { q: "A central bank wants to reduce demand-pull inflation. What should it do?", opts: ["Cut interest rates", "Raise interest rates", "Increase the money supply", "Lower the exchange rate"], a: 1, why: "Higher rates cut borrowing and spending, so AD shifts left." },
  { q: "A fall in the exchange rate is most likely to:", opts: ["Make exports more expensive for foreigners", "Make imports cheaper", "Make exports cheaper for foreigners", "Reduce the risk of imported inflation"], a: 2, why: "A lower exchange rate cuts the foreign currency price of exports." },
  { q: "Which is a likely effect of an increase in the money supply?", opts: ["Interest rates tend to rise", "Banks have more to lend, so interest rates may fall", "Aggregate demand falls", "The exchange rate is certain to rise"], a: 1, why: "More money in the banking system makes credit cheaper and easier to get." },
  { q: "A rise in interest rates is most likely to benefit:", opts: ["A household with a variable mortgage", "A firm planning to borrow", "A saver", "An exporter when the currency rises"], a: 2, why: "Savers earn more. Borrowers pay more." },
  { q: "Buying government bonds from banks is likely to:", opts: ["Reduce the money supply", "Increase the money supply", "Raise taxes", "Raise the interest rate"], a: 1, why: "The central bank pays the banks, so they have more to lend." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Interest rate", "The price of borrowing and the reward for saving."],
  ["Base rate", "The central bank's main interest rate, which commercial banks follow."],
  ["Foreign exchange rate", "The price of one currency in terms of another."],
  ["Floating exchange rate", "A rate set by demand and supply in the foreign exchange market."],
  ["Fixed exchange rate", "A rate held at a set value by the central bank."],
  ["Depreciation", "A fall in the value of a floating currency against other currencies."],
  ["Appreciation", "A rise in the value of a floating currency against other currencies."],
  ["Devaluation", "A government sets a lower fixed value for its currency."],
  ["Revaluation", "A government sets a higher fixed value for its currency."],
  ["Quantitative easing", "A central bank buying large amounts of bonds to increase the money supply."],
  ["Imported inflation", "A rise in prices caused by dearer imports, often after a currency falls."],
  ["Time lag", "The delay between a policy change and its effects."],
] });
labI(); labX();
