const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

/* ---------- Learn picture: two values of money ---------- */
$("#pic1").innerHTML = `<svg viewBox="0 0 760 330" role="img" aria-label="Link between the internal value of money, inflation, the exchange rate and import prices">${(() => { let o = ""; const box = (x, y, w, l, c) => SV.rect(x, y, w, 56, c) + SV.text(x + w / 2, y + 33, l, "lbl bd", { "text-anchor": "middle" }); o += box(40, 40, 190, "Higher domestic inflation", "f2") + box(285, 40, 190, "Exports dearer, imports cheaper", "f4") + box(530, 40, 190, "Demand for currency falls", "f1") + box(530, 220, 190, "Currency depreciates", "f2") + box(285, 220, 190, "Import prices rise", "f4") + box(40, 220, 190, "Domestic inflation rises again", "f2"); o += arrow(235, 68, 280, 68, "r", "c1", 1) + arrow(480, 68, 525, 68, "r", "c1", 1) + arrow(625, 100, 625, 215, "d", "c1", 1) + arrow(525, 248, 480, 248, "l", "c1", 1) + arrow(280, 248, 235, 248, "l", "c1", 1) + arrow(135, 215, 135, 100, "u", "c2", 1); o += tag(380, 170, "a vicious circle", "t2", 1, "middle") + tag(380, 192, "low inflation and an appreciation can run the same loop in reverse", "t3", 1, "middle"); return o; })()}</svg>`;

/* ---------- Watch 1: circle animation ---------- */
const CBOX = [[40, 40], [285, 40], [530, 40], [530, 220], [285, 220], [40, 220]];
const LV = ["Higher domestic inflation", "Exports dearer, imports cheaper", "Demand for currency falls", "Currency depreciates", "Import prices rise", "Domestic inflation rises again"];
const LV2 = ["Lower domestic inflation", "Exports cheaper, imports dearer", "Demand for currency rises", "Currency appreciates", "Import prices fall", "Domestic inflation falls further"];
function circDraw(s) {
  const lab = s.m > 0.5 ? LV2 : LV; let o = "";
  CBOX.forEach((b, i) => { const v = Math.max(0, Math.min(1, s.n - i)); if (v <= 0) return; o += SV.rect(b[0], b[1], 190, 56, s.m > 0.5 ? "f3" : i === 5 || i === 0 || i === 3 ? "f2" : "f4", op(v)) + SV.text(b[0] + 95, b[1] + 33, lab[i], "lbl bd", { "text-anchor": "middle", ...op(v) }); });
  const AR = [[235, 68, 280, 68, "r"], [480, 68, 525, 68, "r"], [625, 100, 625, 215, "d"], [525, 248, 480, 248, "l"], [280, 248, 235, 248, "l"], [135, 215, 135, 100, "u"]];
  AR.forEach((a, i) => { const v = Math.max(0, Math.min(1, s.n - i - 0.5)); if (v > 0) o += arrow(a[0], a[1], a[2], a[3], a[4], s.m > 0.5 ? "c3" : "c2", v); });
  if (s.n >= 6.4) o += tag(380, 170, s.m > 0.5 ? "a virtuous circle" : "a vicious circle", s.m > 0.5 ? "t3" : "t2", 1, "middle");
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 310, label: "Vicious circle linking inflation and the exchange rate, then the virtuous circle in reverse", base: { n: 0, m: 0 }, draw: circDraw, tween: 1400, dwell: 5600, steps: [
  { cap: "<b>The start.</b> Domestic prices rise faster than prices abroad. The internal value of money falls.", s: { n: 1.2 } },
  { cap: "<b>Competitiveness.</b> Exports become dearer for foreign buyers and imports cheaper for home buyers, so the current account worsens and demand for the currency falls.", s: { n: 3 } },
  { cap: "<b>Depreciation.</b> The currency's external value falls. Import prices in domestic currency rise.", s: { n: 5 } },
  { cap: "<b>The circle closes.</b> Dearer imports raise costs and prices, so domestic inflation rises again. The loop feeds itself: a <b>vicious circle</b>. Policy may need a tighter stance or a credible target to break it.", s: { n: 6.6 } },
  { cap: "<b>The reverse.</b> Low inflation, an appreciating currency and falling import prices can reinforce each other: a <b>virtuous circle</b>. The cost is that exporters become less competitive.", s: { n: 6.6, m: 1 } },
] });

/* ---------- Watch 2: growth, inflation and current account ---------- */
const GXX = (x) => 90 + x * 62, GYY = (v) => 170 - v * 30;
const gg = (x) => (x <= 3 ? x : 3 + 0.1 * (x - 3)), ii = (x) => 1.5 + (x <= 3 ? 0.1 * x : 0.3 + 0.9 * (x - 3)), cc = (x) => 0.5 - 0.5 * x;
function triDraw(s) {
  let o = SV.line(70, 170, 740, 170) + SV.line(70, 40, 70, 320) + SV.text(740, 190, "Growth of aggregate demand (% a year)", "sm", { "text-anchor": "end" }) + SV.text(76, 34, "% (growth, inflation) and % of GDP (current account)", "sm");
  [0, 2, 4, 6, 8, 10].forEach((x) => (o += SV.text(GXX(x), 186, x, "sm", { "text-anchor": "middle" })));
  const draw = (f, cls, tcls, label, v) => { if (v <= 0) return ""; const pts = []; for (let x = 0; x <= 10.001; x += 0.2) pts.push([GXX(x), GYY(f(x))]); return SV.path(Lib.ptsPath(pts), cls, op(v)) + tag(GXX(10) + 4, GYY(f(10)) + 4, label, tcls, v); };
  o += draw(gg, "c1", "t1", "growth", s.a) + draw(ii, "c2", "t2", "inflation", s.b) + draw(cc, "c4", "t4", "current account", s.c);
  if (s.d > 0) o += SV.line(GXX(3), 40, GXX(3), 320, "gr", op(s.d)) + tag(GXX(3) + 6, 56, "capacity reached", "t3", s.d);
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 340, label: "Growth, inflation and the current account as aggregate demand grows faster", base: { a: 0, b: 0, c: 0, d: 0 }, draw: triDraw, tween: 1100, dwell: 5800, steps: [
  { cap: "<b>Growth.</b> With spare capacity, faster demand growth gives faster real growth. Once the economy reaches <b>capacity</b>, further demand adds little to output.", s: { a: 1, d: 1 } },
  { cap: "<b>Inflation.</b> Below capacity inflation stays low. Beyond it, extra demand raises prices instead of output, so inflation accelerates: growth above the sustainable rate brings <b>demand-pull inflation</b>.", s: { a: 1, b: 1, d: 1 } },
  { cap: "<b>The current account.</b> Faster growth in income raises imports all the way, so the current account moves into deficit, and more rapidly once inflation hits competitiveness.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>The trade-off.</b> The best range for demand growth is near the capacity point: more growth than that brings little extra output but costs inflation and a larger deficit. Supply-side growth (a higher capacity point) is how to get both.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Lab 1: PPP ---------- */
function labPPP() {
  if (!$("#pd") || !$("#pf") || !$("#py")) return;
  const d = +$("#pd").value / 10, f = +$("#pf").value / 10, yrs = +$("#py").value;
  const Pd = (t) => 100 * Math.pow(1 + d / 100, t), Pf = (t) => 100 * Math.pow(1 + f / 100, t), E = (t) => 100 * Pd(t) / Pf(t) / 1;
  const e = (t) => 100 * Math.pow((1 + d / 100) / (1 + f / 100), t);
  $("#r1").textContent = Lib.fmtN(Pd(yrs), 0); $("#r2").textContent = Lib.fmtN(Pf(yrs), 0); $("#r3").textContent = Lib.fmtN(e(yrs), 0);
  const chg = (e(yrs) / 100 - 1) * 100;
  $("#rv").textContent = Math.abs(chg) < 0.5 ? "Inflation is about the same at home and abroad, so there is no pressure on the exchange rate." : chg > 0 ? `Home prices rose ${Lib.fmtN(Pd(yrs) - 100, 0)}% against ${Lib.fmtN(Pf(yrs) - 100, 0)}% abroad. To keep the same goods costing the same, the home currency would need to depreciate: the rate moves from 100 to ${Lib.fmtN(e(yrs), 0)} units of home currency per unit of foreign currency (a ${Lib.fmtN(chg, 0)}% fall in its external value).` : `Home inflation is lower than abroad, so purchasing power parity points to an appreciation: the rate falls to ${Lib.fmtN(e(yrs), 0)} units of home currency per unit of foreign currency.`;
  const X = (t) => 50 + t * 34, Y = (v) => 260 - (v - 80) * 0.9; const mx = Math.max(Pd(yrs), Pf(yrs), e(yrs), 130);
  const Y2 = (v) => 260 - (v - 80) / (mx - 80) * 210;
  let o = SV.line(50, 260, 400, 260) + SV.line(50, 260, 50, 30) + SV.text(400, 282, "Years", "sm", { "text-anchor": "end" });
  const line = (fn, c) => { const pts = []; for (let t = 0; t <= yrs; t += 0.25) pts.push([50 + t / yrs * 340, Y2(fn(t))]); return SV.path(Lib.ptsPath(pts), c); };
  o += line(Pd, "c2") + line(Pf, "c1") + line(e, "c4") + tag(396, Y2(Pd(yrs)) - 6, "home prices", "t2", 1, "end") + tag(396, Y2(Pf(yrs)) + 14, "foreign prices", "t1", 1, "end") + tag(396, Y2(e(yrs)) + (e(yrs) > Pd(yrs) ? -6 : 14), "exchange rate", "t4", 1, "end");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pd", label: "Home inflation (%) ", min: 0, max: 200, step: 5, value: 80, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labPPP });
Lib.slider($("#g2"), { id: "pf", label: "Foreign inflation (%) ", min: 0, max: 100, step: 5, value: 20, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labPPP });
Lib.slider($("#g3"), { id: "py", label: "Years ", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: labPPP });
labPPP();

/* ---------- Lab 2: growth and imports ---------- */
function labGI() {
  if (!$("#gg") || !$("#gm") || !$("#gx")) return;
  const g = +$("#gg").value / 10 / 100, m = +$("#gm").value / 100, x = +$("#gx").value / 10 / 100, dY = 1000 * g, dM = m * dY, dX = 200 * x, ca = 200 + dX - (200 + dM);
  $("#t1").textContent = "+" + Lib.fmtN(dM, 1); $("#t2").textContent = "+" + Lib.fmtN(dX, 1); $("#t3").textContent = (ca >= 0 ? "+" : "") + Lib.fmtN(ca, 1) + " (" + Lib.fmtN(ca / (1000 + dY) * 100, 1) + "% of GDP)";
  $("#tv").textContent = ca < -0.5 ? `GDP grows by ${Lib.fmtN(dY, 0)}. With ${Math.round(m * 100)}% of extra income spent on imports, imports rise by ${Lib.fmtN(dM, 1)}, more than the ${Lib.fmtN(dX, 1)} rise in exports: the current account moves into deficit.` : ca > 0.5 ? `Exports rise by ${Lib.fmtN(dX, 1)}, more than the ${Lib.fmtN(dM, 1)} rise in imports, so the current account moves into surplus: this is export-led growth.` : "Extra imports and extra exports roughly cancel, so the current account stays close to balance.";
  const mx = Math.max(200 + dX, 200 + dM, 220) * 1.1, Y = (v) => 250 - v / mx * 200; let o = SV.line(40, 250, 400, 250);
  const bars = [["Exports before", 200, "f1"], ["Imports before", 200, "f2"], ["Exports after", 200 + dX, "f1"], ["Imports after", 200 + dM, "f2"]];
  bars.forEach((b, i) => { const xx = 60 + i * 85; o += SV.rect(xx, Y(b[1]), 60, 250 - Y(b[1]), b[2], { opacity: i < 2 ? 0.5 : 0.9 }) + tag(xx + 30, Y(b[1]) - 6, Lib.fmtN(b[1], 0), i % 2 ? "t2" : "t1", 1, "middle") + SV.text(xx + 30, 268, b[0], "sm bd", { "text-anchor": "middle" }); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "gg", label: "Real GDP growth (%) ", min: 0, max: 80, step: 5, value: 40, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labGI });
Lib.slider($("#g5"), { id: "gm", label: "Share of extra income spent on imports (%) ", min: 10, max: 60, step: 5, value: 35, fmt: (v) => v, onInput: labGI });
Lib.slider($("#g6"), { id: "gx", label: "Export growth (%) ", min: 0, max: 80, step: 5, value: 20, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labGI });
labGI();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Does the change tend to raise or lower the external value of the currency (the exchange rate)?", buckets: [{"label": "Raises external value"}, {"label": "Lowers external value"}], items: [{"text": "Home inflation falls below that of trading partners", "b": 0}, {"text": "Home inflation rises well above that of trading partners", "b": 1}, {"text": "Interest rates rise and attract foreign savers", "b": 0}, {"text": "A large current account deficit emerges", "b": 1}, {"text": "Foreign demand for exports rises", "b": 0}, {"text": "Quantitative easing expands the money supply", "b": 1}, {"text": "Investors expect the currency to appreciate", "b": 0}, {"text": "Capital flows out of the country", "b": 1}], done: "Higher demand for the currency raises its value; higher supply lowers it." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Internal value of money", "Purchasing power at home, the inverse of the price level"], ["External value of money", "The exchange rate: what the currency buys abroad"], ["Purchasing power parity", "The idea that the exchange rate adjusts so that price levels are equal"], ["Imported inflation", "Higher prices caused by dearer imports after a depreciation"], ["Marginal propensity to import", "Share of extra income spent on imports"], ["Import suction", "Rise in imports caused by rising national income"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the vicious circle in order, starting with higher inflation.", items: ["Domestic inflation is higher than abroad", "Exports become less competitive and imports cheaper", "Demand for the currency falls and it depreciates", "Imported raw materials and goods cost more", "Domestic inflation rises again"], done: "Depreciation feeds inflation and inflation feeds depreciation." });
Lib.calc($("#c1"), { qs: [
  {"q": "Home prices rise 6% a year and foreign prices 2% a year. Using PPP, calculate the approximate annual fall in the external value of the home currency (%).", "a": 4, "unit": "%", "tol": 0.05, "hint": "Inflation differential.", "sol": "6 − 2 = <b>4%</b> a year (approximately)."},
  {"q": "A country's exchange rate is 1.00 foreign currency units per unit of home currency. It depreciates by 12%. How many foreign currency units does one unit of home currency now buy?", "a": 0.88, "tol": 0.005, "hint": "1.00 × (1 − 0.12).", "sol": "1.00 × 0.88 = <b>0.88</b>."},
  {"q": "GDP grows by $50bn and the marginal propensity to import is 0.3. Calculate the extra imports ($bn).", "a": 15, "unit": "$bn", "tol": 0.05, "hint": "MPM × change in income.", "sol": "0.3 × 50 = <b>$15bn</b>."},
  {"q": "A country's price index is 100 at home and 100 abroad, and the exchange rate is 1. After a year home prices are 105 and foreign prices are 102 with the nominal rate unchanged. What is the real exchange rate index (home price level × rate ÷ foreign price level × 100)?", "a": 102.9, "tol": 0.1, "hint": "105 × 1 ÷ 102 × 100.", "sol": "105 ÷ 102 × 100 = <b>102.9</b>: the home country has become about 3% less competitive."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is true of purchasing power parity?", opts: ["Exchange rates do not change", "The exchange rate adjusts so that the same goods cost the same in different countries", "Interest rates equal inflation", "Imports equal exports"], a: 1, why: "PPP links the exchange rate to relative price levels." },
  { q: "A depreciation of the currency is most likely to cause:", opts: ["Higher import prices and a rise in the price level", "Lower export volumes immediately", "Lower inflation", "A rise in the external value"], a: 0, why: "Imports cost more in domestic currency, which raises the price level." },
  { q: "Growth is likely to worsen the current account when:", opts: ["The marginal propensity to import is high", "Exports grow faster than income", "Imports are inelastic and unaffected by income", "Growth comes entirely from export demand"], a: 0, why: "A high propensity to import means extra income is spent on imports." },
  { q: "Which is the best example of supply-side growth that need not cause inflation?", opts: ["A rise in consumer confidence", "Investment in education and infrastructure that raises capacity", "A cut in interest rates", "A rise in government spending"], a: 1, why: "LRAS shifts right, allowing output to rise without pressure on prices." },
  { q: "A government raises interest rates to cut inflation. What effect could this have on the current account?", opts: ["Higher interest rates could attract hot money, raise the exchange rate and reduce export competitiveness", "No effect at all", "It always improves exports", "It always raises imports"], a: 0, why: "A stronger currency makes exports dearer and imports cheaper, which could worsen the current account." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Internal value of money", "Purchasing power at home; falls with inflation."],
  ["External value of money", "Exchange rate; what the currency buys abroad."],
  ["Purchasing power parity", "Exchange rate adjusts so price levels are equal."],
  ["Imported inflation", "Rise in domestic prices from dearer imports."],
  ["Marginal propensity to import", "Share of extra income spent on imports."],
  ["Marshall-Lerner condition", "A depreciation improves the current account if PEDx + PEDm > 1."],
  ["Demand-pull inflation", "Prices rise because AD exceeds capacity."],
  ["Export-led growth", "Growth driven by rising exports."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "If prices increase in country X but stay the same in country Y, what is the most likely effect on the internal and external value of money in country X? (Feb/March 2025 · 32 · Q20, reworded)", opts: ["Internal value falls and external value falls", "Internal value falls and external value rises", "Internal value rises and external value falls", "Internal value rises and external value rises"], a: 0, why: "Higher prices reduce purchasing power at home, and higher relative prices weaken demand for the currency." },
  { q: "A government uses quantitative easing to raise growth. What is the most likely effect on the internal and external value of its currency? (May/June 2020 · 31 · Q29, reworded)", opts: ["Both fall", "Internal value falls and external value rises", "Both rise", "Internal value rises and external value falls"], a: 0, why: "More money and lower interest rates raise prices and weaken the exchange rate." },
  { q: "In which situation is devaluation most likely to cause inflation? (Feb/March 2024 · 32 · Q25, reworded)", opts: ["Excess capacity is available", "Import tariffs are cut", "Local substitutes for imported raw materials are unavailable", "Demand for exports is price inelastic"], a: 2, why: "If firms cannot replace imported inputs, higher import prices feed straight into costs and prices." },
  { q: "A country imports most of its raw materials. Which policy is most likely to control cost-push inflation? (Feb/March 2024 · 32 · Q26, reworded)", opts: ["An appreciation of the exchange rate", "A rise in income tax", "A rise in interest rates", "A rise in sales tax"], a: 0, why: "A stronger currency makes imported inputs cheaper." },
  { q: "Which would be the most effective policy to reduce inflation caused by a rapid rise in import prices? (Feb/March 2024 · 32 · Q20, reworded)", opts: ["A fall in the interest rate", "A fall in income tax", "A rise in tariffs", "A revaluation of the exchange rate"], a: 3, why: "Revaluation lowers the domestic price of imports. Tariffs would raise them." },
  { q: "Which would not lead to a rise in the value of a country's currency? (Feb/March 2025 · 32 · Q23, reworded)", opts: ["A rise in domestic inflation", "A rise in domestic interest rates", "A rise in incomes abroad", "More tourists visiting"], a: 0, why: "Higher inflation weakens competitiveness and so lowers demand for the currency." },
  { q: "Nominal national income rose 2% in a year, inflation was 3% and population rose 1%. What happened to real income per head? (Feb/March 2024 · 32 · Q19, reworded)", opts: ["It fell by 2%", "It rose by 1%", "It rose by 4%", "It did not change"], a: 0, why: "Real national income fell about 1%, and with 1% more people real income per head fell about 2%." },
  { q: "The current account moves into deficit. What is a possible reason? (Feb/March 2025 · 32 · Q22, reworded)", opts: ["A fall in tax revenue", "Export-led growth", "Repaying debts to other countries", "Imports of new technology"], a: 3, why: "Imports of goods raise the import bill; debt repayment is in the financial account and export-led growth tends to improve the current account." },
] });
