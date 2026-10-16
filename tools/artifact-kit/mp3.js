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
/* ---------- 4. AD / AS ---------- */
const asP = (y) => (y <= 60 ? 30 + 0.4 * y : 54 + 2.2 * (y - 60));
function solveAD(sh) {
  const c = 90 + 0.8 * sh; let y = (c - 30) / 1.2;
  if (y > 60) y = (c + 78) / 3;
  return [y, asP(y), c];
}
function adLine(c, cls, label, o = {}) {
  const lo = Math.max(0, (c - 108) / 0.8), hi = Math.min(100, (c - 8) / 0.8);
  let r = SV.line(QX(lo), PY(c - 0.8 * lo), QX(hi), PY(c - 0.8 * hi), cls, o.attrs);
  if (label) r += SV.text(QX(hi) + 6, PY(c - 0.8 * hi) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), o.attrs && o.attrs.opacity !== undefined ? { opacity: o.attrs.opacity } : {});
  return r;
}
function adChart(s) {
  const sh = s.sh, [y1, p1, c] = solveAD(sh), moved = Math.abs(sh) >= 1;
  let o = axes("Price level", "Real GDP");
  o += SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: moved ? 0.4 : 1 } });
  if (moved) o += adLine(c, sh > 0 ? "c2" : "c4", sh > 0 ? "AD₁" : "AD₂", { t: sh > 0 ? "t2" : "t4" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: moved ? 0.45 : 1 });
  if (moved) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, sh > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Monetary policy shifting aggregate demand", base: { sh: 0 }, draw: adChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b> where AD meets AS. <b>AD = C + I + G + (X − M)</b>. Monetary policy works on <b>C and I</b> (interest rates, money supply) and on <b>X − M</b> (exchange rate).", s: { sh: 0 } },
  { cap: "<b>Expansionary monetary policy</b>: lower interest rates, a bigger money supply and/or a lower exchange rate. AD shifts <b>right</b> to AD₁. Real GDP rises (<b>growth</b>), unemployment is likely to fall and the price level edges up.", s: { sh: 15 } },
  { cap: "<b>Evaluate:</b> push too hard when the economy is close to full capacity and AS is steep. Output barely rises and most of the effect is a <b>higher price level</b>: inflation. Imports may also rise and the exchange rate fall further.", s: { sh: 40 } },
  { cap: "<b>Contractionary monetary policy</b>: higher interest rates, a smaller money supply and/or a higher exchange rate. AD shifts <b>left</b> to AD₂. Inflation pressure eases, but output and jobs are likely to fall too.", s: { sh: -15 } },
] });


const MCH = ["Central bank cuts the base interest rate", "Borrowing is cheaper: consumption ↑ and investment ↑", "AD shifts to the right", "Real GDP ↑ and unemployment ↓", "Price level ↑: risk of demand-pull inflation", "Imports ↑ and the currency may fall: current account effect unclear"];
function mchain(s) {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  MCH.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap), col = i < 4 ? "--good" : "--bad";
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < MCH.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 400, label: "Gains and costs of cutting interest rates", base: { n: 0 }, draw: mchain, steps: [
  { cap: "The central bank <b>cuts the base interest rate</b> to support the economy.", s: { n: 1 } },
  { cap: "Borrowing is cheaper and saving pays less, so <b>consumption and investment rise</b>.", s: { n: 2 } },
  { cap: "AD shifts <b>right</b>.", s: { n: 3 } },
  { cap: "<b>Gains:</b> real GDP rises and firms take on more workers. Growth and employment aims move closer.", s: { n: 4 } },
  { cap: "<b>Cost:</b> as demand rises the price level may rise, especially near full capacity: demand-pull inflation. This is a <b>conflict of aims</b>.", s: { n: 5 } },
  { cap: "Higher incomes raise <b>imports</b>, and lower rates may weaken the currency. The effect on the current account depends on elasticity.", s: { n: 6 } },
] });
/* Lab 3: monetary policy simulator. Shift in AD = -5 x change in rate + 1.25 x money supply change - 0.5 x exchange rate change. */
function labM() {
  if (!$("#mi") || !$("#mm") || !$("#mf")) return;
  const dr = +$("#mi").value, dm = +$("#mm").value, fx = +$("#mf").value, sh = -5 * dr + 1.25 * dm - 0.5 * fx, [y, p] = solveAD(sh);
  $("#ma1").textContent = money(y, 1) + (y > 50.5 ? " ▲" : y < 49.5 ? " ▼" : ""); $("#ma2").textContent = money(p, 1) + (p > 50.5 ? " ▲" : p < 49.5 ? " ▼" : "");
  $("#ma3").textContent = money(5 + dr, 1) + "%"; $("#ma4").textContent = sh > 1 ? "Expansionary" : sh < -1 ? "Contractionary" : "Neutral";
  let v;
  if (Math.abs(sh) < 1) v = "The three changes roughly cancel out, so aggregate demand hardly moves.";
  else if (sh > 0) v = `Aggregate demand shifts right. Real GDP rises by ${money(y - 50, 1)} and the price level by ${money(p - 50, 1)}. ${y > 61 ? "The economy is near full capacity, so much of the extra demand shows up as higher prices." : "Output rises by more than prices, so growth and employment are likely to benefit."}${fx < -3 ? " A lower exchange rate also makes imports dearer." : ""}`;
  else v = `Aggregate demand shifts left. Real GDP falls by ${money(50 - y, 1)} and the price level by ${money(50 - p, 1)}. Inflation pressure eases but jobs are at risk.${fx > 3 ? " A higher exchange rate also hurts exporters." : ""}`;
  $("#mav").textContent = v;
  $("#labM").innerHTML = adChart({ sh });
}
Lib.slider($("#g5"), { id: "mi", label: "Change in the base interest rate", min: -3, max: 3, step: 0.5, value: -1, fmt: (v) => (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v) + " pts", onInput: labM });
Lib.slider($("#g6"), { id: "mm", label: "Change in the money supply", min: -10, max: 10, step: 1, value: 0, fmt: (v) => (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v) + "%", onInput: labM });
Lib.slider($("#g7"), { id: "mf", label: "Change in the exchange rate (+ = rises)", min: -15, max: 15, step: 1, value: 0, fmt: (v) => (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v) + "%" + (v < 0 ? " depreciation" : v > 0 ? " appreciation" : ""), onInput: labM });

/* Lab 4: policy scorecard */
const SC = [
  { n: "Cut interest rates", g: "▲ rises", u: "▼ falls", i: "▲ may rise", c: "▼ may worsen", catch: "Savers earn less. Effect is delayed, and weak if confidence is low or banks do not pass the cut on." },
  { n: "Raise interest rates", g: "▼ slows", u: "▲ may rise", i: "▼ eases", c: "▲ may improve", catch: "Mortgage holders and borrowers are squeezed. Can push a weak economy into recession." },
  { n: "Increase money supply", g: "▲ rises", u: "▼ falls", i: "▲ risk of high inflation", c: "▼ may worsen", catch: "Too much money chasing too few goods. Banks may hold the money instead of lending it." },
  { n: "Reduce money supply", g: "▼ slows", u: "▲ may rise", i: "▼ eases", c: "▲ may improve", catch: "Credit becomes harder to get, which hits small firms and house buyers first." },
  { n: "Lower the exchange rate", g: "▲ rises", u: "▼ falls", i: "▲ imported inflation", c: "▲ if demand is elastic", catch: "Imports and foreign debts cost more. Trading partners may retaliate. Gain is small if demand is inelastic." },
  { n: "Raise the exchange rate", g: "▼ slows", u: "▲ exporters may cut jobs", i: "▼ cheaper imports", c: "▼ exports dearer", catch: "Exporters and tourism firms lose competitiveness. Cheaper imports help consumers and lower costs." },
];
function showSC(i) {
  const p = SC[i];
  $("#scBtns").innerHTML = SC.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
  $$("#scBtns .b").forEach((b) => (b.onclick = () => showSC(+b.dataset.j)));
  $("#scOut").innerHTML = `<div class="tw"><table class="t"><tr><th>Economic growth</th><th>Unemployment</th><th>Inflation</th><th>Current account</th></tr><tr><td>${p.g}</td><td>${p.u}</td><td>${p.i}</td><td>${p.c}</td></tr></table></div><div class="warn"><b class="h">The catch</b>${p.catch}</div>`;
}
showSC(0);


/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>gain</b> or a <b>cost or risk</b> of expansionary monetary policy?", buckets: [{ label: "Gain" }, { label: "Cost or risk" }], items: [
  { text: "Real GDP could rise", b: 0 }, { text: "Unemployment could fall", b: 0 }, { text: "Firms find investment cheaper", b: 0 }, { text: "Exports become cheaper if the currency falls", b: 0 },
  { text: "Demand-pull inflation", b: 1 }, { text: "Savers earn less", b: 1 }, { text: "Imported inflation if the currency falls", b: 1 }, { text: "Higher imports and a worse current account", b: 1 },
], done: "Every policy has gains and costs: that is evaluation." });
Lib.classify($("#cl2"), { prompt: "Which <b>macroeconomic aim</b> is each measure mainly <b>aimed at</b>? Think about the problem the central bank is trying to fix.", buckets: [{ label: "Growth and jobs" }, { label: "Stable prices" }, { label: "Balance of payments" }], items: [
  { text: "Cut interest rates because the economy is in a slump", b: 0 }, { text: "Increase the money supply because unemployment is high", b: 0 },
  { text: "Raise interest rates because demand-pull inflation is rising", b: 1 }, { text: "Reduce the money supply because prices are rising quickly", b: 1 },
  { text: "Lower the exchange rate because the current account deficit is large", b: 2 }, { text: "Devalue the currency to make exports cheaper and imports dearer", b: 2 },
], done: "Name the problem being fixed. Note that one tool can affect several aims: a lower exchange rate helps the current account but may raise import prices." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why a cut in interest rates could conflict with stable prices</b>.", items: [
  "The central bank cuts interest rates",
  "Borrowing rises and saving falls",
  "Spending increases and AD shifts right",
  "AD grows faster than the economy can supply",
  "Demand-pull inflation",
], done: "A conflict between full employment and stable prices." });
Lib.calc($("#c1"), { qs: [
  { q: "Real GDP is $400bn and rises to $412bn. What is the percentage growth?", a: 3, sol: "12 ÷ 400 × 100 = <b>3%</b>." },
  { q: "The price level rises from 125 to 130. What is the inflation rate (%)?", a: 4, sol: "5 ÷ 125 × 100 = <b>4%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A cut in interest rates could create a conflict between:", opts: ["Full employment and stable prices", "Equal pay and growth", "Free trade and tariffs", "Poverty and population"], a: 0, why: "More spending may cut unemployment but raise demand-pull inflation." },
  { q: "Which is a limit on the effectiveness of monetary policy?", opts: ["Low confidence among borrowers", "Higher AD", "More jobs", "Lower rates"], a: 0, why: "If households and firms are worried, they may not borrow even at low rates." },
  { q: "A central bank is worried about inflation. The measure most likely to help is:", opts: ["Cutting rates", "Raising rates", "Increasing the money supply", "Lowering the exchange rate"], a: 1, why: "Higher rates reduce AD." },
  { q: "A country that fixes its currency to the US dollar will find that:", opts: ["It can set its own interest rates freely", "It tends to follow the interest rates of the US", "Its exports always rise", "Its currency never changes"], a: 1, why: "A peg limits independent monetary policy." },
  { q: "A lower exchange rate is most likely to:", opts: ["Reduce the price of imports", "Make exports cheaper for foreign buyers", "Raise the interest rate", "Reduce AD"], a: 1, why: "Exports become more price competitive." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Expansionary monetary policy", "Lower interest rates, a bigger money supply and/or a lower exchange rate to raise AD."],
  ["Contractionary monetary policy", "Higher interest rates, a smaller money supply and/or a higher exchange rate to reduce AD."],
  ["Demand-pull inflation", "A rise in the price level caused by aggregate demand growing faster than supply."],
  ["Imported inflation", "A rise in prices caused by dearer imports, often after a currency falls."],
  ["Time lag", "The delay between a policy change and its effects."],
  ["Fixed exchange rate", "A rate held at a set value by the central bank."],
  ["Depreciation", "A fall in the value of a floating currency against other currencies."],
  ["Appreciation", "A rise in the value of a floating currency against other currencies."],
] });
labM(); showSC(0);
