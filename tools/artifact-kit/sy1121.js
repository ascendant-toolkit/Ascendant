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

/* ---------- Nominal, prices, real ---------- */
const RX = (i) => 90 + i * 130, RY = (v) => 300 - (v - 94) * 13;
const YRS = [0, 1, 2, 3, 4], NOM = [100, 99, 98, 97, 96], PR = [100, 103, 106.1, 109.3, 112.6];
function realDraw(s) {
  let o = axes(70, 300, 730, 30, "Year", "Index (year 0 = 100)"); [100, 104, 108, 112].forEach((v) => (o += SV.text(64, RY(v) + 4, v, "sm", { "text-anchor": "end" }) + SV.line(70, RY(v), 730, RY(v), "gr", op(0.35))));
  YRS.forEach((i) => (o += SV.text(RX(i), 322, "Y" + i, "sm", { "text-anchor": "middle" })));
  const ln = (arr, c, k) => { const n = Math.max(0, Math.min(4, k * 4)), pts = []; for (let i = 0; i <= Math.floor(n); i++) pts.push([RX(i), RY(arr[i])]); if (n % 1 > 0 && Math.floor(n) < 4) { const a = Math.floor(n), f = n - a; pts.push([RX(a + f), RY(arr[a] + (arr[a + 1] - arr[a]) * f)]); } return pts.length > 1 ? SV.path(Lib.ptsPath(pts), c) : ""; };
  o += ln(NOM, "c1", s.a) + (s.a > 0 ? tag(RX(4) + 4, RY(NOM[4]) - 8, "Nominal rate index", "t1", s.a, "end") : "");
  if (s.b > 0) o += ln(PR, "c3 dash", s.b) + tag(RX(4) + 4, RY(PR[4]) - 4, "Domestic ÷ foreign prices", "t3", s.b, "end");
  if (s.c > 0) { const real = NOM.map((n, i) => n * PR[i] / 100); o += ln(real, "c4", s.c) + SV.circle(RX(4), RY(real[4]), 7, "dot4", op(s.c)) + tag(RX(4) - 12, RY(real[4]) + 22, "Real rate up " + Lib.fmtN(real[4] - 100, 1) + "%", "t4", s.c, "end"); }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Nominal exchange rate index falling to 96, relative prices rising to 112.6 and the real exchange rate rising to 108.1">${realDraw({ a: 1, b: 1, c: 1 })}</svg>`;
Lib.stepper($("#stR"), { w: 760, h: 340, label: "Nominal rate falling, relative prices rising and the real exchange rate rising", base: { a: 0, b: 0, c: 0 }, draw: realDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>The nominal exchange rate</b> falls by 1% a year: the index drops from 100 to 96, a 4% depreciation. Looking only at this line, home goods look cheaper abroad.", s: { a: 1 } },
  { cap: "<b>Relative prices.</b> The home country has 3% inflation a year while its partner has none. The ratio of domestic to foreign prices climbs to about 112.6, so home goods are dearer at home relative to abroad.", s: { a: 1, b: 1 } },
  { cap: "<b>The real exchange rate</b> is the nominal rate multiplied by the price ratio: 96 × 112.6 ÷ 100 = 108.1. It has risen about 8%, a real appreciation.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>The meaning.</b> The 4% nominal depreciation was more than cancelled out by higher inflation at home. Home goods are about 8% dearer relative to foreign goods, so competitiveness has fallen even though the currency has depreciated.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Trade-weighted index ---------- */
const TW = [0.5, 0.3, 0.2], TN = ["Partner A (50%)", "Partner B (30%)", "Partner C (20%)"], TI = [110, 95, 100];
const TX = (i) => 130 + i * 150, TY = (v) => 300 - (v - 80) * 7.5;
function twDraw(s) {
  let o = axes(70, 300, 730, 30, "", "Index (last year = 100)"); [80, 90, 100, 110, 120].forEach((v) => (o += SV.text(64, TY(v) + 4, v, "sm", { "text-anchor": "end" }) + SV.line(70, TY(v), 730, TY(v), v === 100 ? "ax" : "gr", op(0.4))));
  const tw = TW.reduce((a, w, i) => a + w * TI[i], 0);
  TI.forEach((v, i) => { const k = [s.a, s.b, s.c][i]; if (k > 0) { const y = TY(100 + (v - 100) * k); o += SV.rect(TX(i) - 28, Math.min(y, TY(100)), 56, Math.abs(y - TY(100)), i === 1 ? "f2" : "f1", op(k)) + tag(TX(i), 320, TN[i], "t1", k, "middle") + tag(TX(i), (v >= 100 ? y - 8 : y + 18), v, "t1", k, "middle"); } });
  if (s.d > 0) { const y = TY(100 + (tw - 100) * s.d); o += SV.rect(TX(3) - 28, Math.min(y, TY(100)), 56, Math.abs(y - TY(100)), "f3", op(s.d)) + tag(TX(3), 320, "Weighted index", "t4", s.d, "middle") + tag(TX(3), y - 8, Lib.fmtN(tw, 1), "t4", s.d, "middle"); }
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 340, label: "Three bilateral currency indices combined into a trade-weighted index", base: { a: 0, b: 0, c: 0, d: 0 }, draw: twDraw, tween: 1200, dwell: 6000, steps: [
  { cap: "<b>Against partner A</b> (half of all trade) the currency has risen 10%: the index is 110.", s: { a: 1 } },
  { cap: "<b>Against partner B</b> (30% of trade) it has fallen 5%: the index is 95.", s: { a: 1, b: 1 } },
  { cap: "<b>Against partner C</b> (20% of trade) it is unchanged at 100.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>The weighted index.</b> 0.5 × 110 + 0.3 × 95 + 0.2 × 100 = 103.5. The currency has risen 3.5% overall, because the biggest partner counts for most.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labR() {
  if (!$("#nm") || !$("#id") || !$("#if")) return;
  const n = +$("#nm").value, pd = +$("#id").value, pf = +$("#if").value, real = ((1 + n / 100) * (1 + pd / 100) / (1 + pf / 100) - 1) * 100, rel = ((1 + pd / 100) / (1 + pf / 100) - 1) * 100;
  $("#r1").textContent = (n >= 0 ? "+" : "") + Lib.fmtN(n, 1) + "%"; $("#r2").textContent = (rel >= 0 ? "+" : "") + Lib.fmtN(rel, 1) + "%"; $("#r3").textContent = (real >= 0 ? "+" : "") + Lib.fmtN(real, 1) + "%";
  $("#rv").textContent = real > 0.5 ? `The real exchange rate has risen about ${Lib.fmtN(real, 1)}%: home goods are relatively dearer, so price competitiveness has fallen.` : real < -0.5 ? `The real exchange rate has fallen about ${Lib.fmtN(-real, 1)}%: home goods are relatively cheaper, so price competitiveness has improved.` : "The real exchange rate is almost unchanged: the nominal movement and the inflation gap cancel out, so competitiveness is about the same.";
  const Y = (v) => 150 - v * 5; let o = SV.line(40, 150, 400, 150) + SV.line(40, 20, 40, 280) + SV.text(46, 16, "Change (%)", "sm");
  [["Nominal", n, "f1"], ["Relative prices", rel, "f2"], ["Real", real, "f3"]].forEach(([l, v, c], i) => { const x = 70 + i * 115, y = Y(Math.max(-26, Math.min(26, v))); o += SV.rect(x, Math.min(y, 150), 70, Math.abs(y - 150), c) + SV.text(x + 35, 296, l, "sm", { "text-anchor": "middle" }) + tag(x + 35, v >= 0 ? y - 8 : y + 18, (v >= 0 ? "+" : "") + Lib.fmtN(v, 1) + "%", "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "nm", label: "Change in the nominal rate, % (+ = appreciation) ", min: -20, max: 20, step: 1, value: 0, fmt: (v) => v, onInput: labR });
Lib.slider($("#g2"), { id: "id", label: "Domestic inflation, % ", min: 0, max: 15, step: 1, value: 6, fmt: (v) => v, onInput: labR });
Lib.slider($("#g3"), { id: "if", label: "Foreign inflation, % ", min: 0, max: 15, step: 1, value: 2, fmt: (v) => v, onInput: labR });
labR();

/* ---------- Lab 2 ---------- */
function labT() {
  if (!$("#ta") || !$("#tb") || !$("#tc")) return;
  const v = [+$("#ta").value, +$("#tb").value, +$("#tc").value], tw = 0.5 * v[0] + 0.3 * v[1] + 0.2 * v[2];
  $("#t1").textContent = Lib.fmtN(tw, 1); $("#t2").textContent = (tw >= 100 ? "+" : "") + Lib.fmtN(tw - 100, 1) + "%"; $("#t3").textContent = tw > 100.2 ? "Appreciation" : tw < 99.8 ? "Depreciation" : "No change";
  $("#tv").textContent = `Weighted index = 0.5 × ${v[0]} + 0.3 × ${v[1]} + 0.2 × ${v[2]} = ${Lib.fmtN(tw, 1)}. ${Math.abs(v[0] - 100) > Math.abs(v[2] - 100) ? "Partner A has the biggest weight, so its movement counts most." : "Partner C has the smallest weight, so its movement counts least."}`;
  const Y = (x) => 150 - (x - 100) * 5; let o = SV.line(40, 150, 400, 150) + SV.line(40, 20, 40, 280) + SV.text(46, 16, "Index (100 = last year)", "sm");
  [["A", v[0], "f1"], ["B", v[1], "f1"], ["C", v[2], "f1"], ["TWI", tw, "f3"]].forEach(([l, x, c], i) => { const px = 60 + i * 85, y = Y(Math.max(75, Math.min(125, x))); o += SV.rect(px, Math.min(y, 150), 55, Math.abs(y - 150), c) + SV.text(px + 27, 296, l, "sm", { "text-anchor": "middle" }) + tag(px + 27, x >= 100 ? y - 8 : y + 18, Lib.fmtN(x, 1), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "ta", label: "Index against partner A (50% weight) ", min: 80, max: 120, step: 1, value: 110, fmt: (v) => v, onInput: labT });
Lib.slider($("#g5"), { id: "tb", label: "Index against partner B (30% weight) ", min: 80, max: 120, step: 1, value: 95, fmt: (v) => v, onInput: labT });
Lib.slider($("#g6"), { id: "tc", label: "Index against partner C (20% weight) ", min: 80, max: 120, step: 1, value: 100, fmt: (v) => v, onInput: labT });
labT();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which measure is it?", buckets: [{"label": "Nominal rate"}, {"label": "Real rate"}, {"label": "Trade-weighted index"}], items: [{"text": "The price of the pound in US dollars on the market today", "b": 0}, {"text": "An exchange rate that adjusts for differences in inflation between countries", "b": 1}, {"text": "A basket of partner currencies weighted by trade shares", "b": 2}, {"text": "£1 = €1.15", "b": 0}, {"text": "Shows whether home goods have become dearer relative to foreign goods", "b": 1}, {"text": "Counts a fall against the largest trading partner more heavily", "b": 2}, {"text": "Unchanged while home inflation is higher than abroad", "b": 0}, {"text": "Rises when domestic prices rise faster than foreign prices at a constant nominal rate", "b": 1}], done: "Nominal: price of one currency in another. Real: adjusts for prices. Trade-weighted: a basket, weighted by trade." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Nominal exchange rate", "The price of one currency in terms of another"], ["Real exchange rate", "The nominal rate adjusted for relative price levels"], ["Trade-weighted index", "The currency against a basket, weighted by trade shares"], ["Real effective exchange rate", "The trade-weighted index adjusted for relative prices"], ["Real appreciation", "Home goods become relatively dearer"], ["Purchasing power parity", "A theory that exchange rates move to equalise the price of goods"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for finding the change in a real exchange rate in order.", items: ["Find the change in the nominal exchange rate", "Find domestic and foreign inflation", "Work out the relative price change (domestic divided by foreign)", "Multiply the nominal index by the relative price index", "Judge the effect on competitiveness"], done: "Real rate = nominal rate × domestic prices ÷ foreign prices." });
Lib.calc($("#c1"), { qs: [
  {"q": "The pound rises from $1.50 to $1.65. Calculate the percentage appreciation of the pound against the dollar (%).", "a": 10, "unit": "%", "tol": 0.05, "hint": "Change ÷ original.", "sol": "(1.65 − 1.50) ÷ 1.50 = <b>10%</b>."},
  {"q": "The nominal exchange rate index rises from 100 to 105. Domestic prices rise from 100 to 108 and foreign prices from 100 to 103. Calculate the real exchange rate index (1 decimal place).", "a": 110.1, "unit": "", "tol": 0.1, "hint": "105 × 108 ÷ 103.", "sol": "105 × 108 ÷ 103 = <b>110.1</b>: a real appreciation of about 10%."},
  {"q": "A trade-weighted index uses weights of 0.5, 0.3 and 0.2. The currency indices against the three partners are 110, 95 and 100. Calculate the trade-weighted index (1 decimal place).", "a": 103.5, "unit": "", "tol": 0.05, "hint": "Multiply each index by its weight and add.", "sol": "55 + 28.5 + 20 = <b>103.5</b>."},
  {"q": "The nominal exchange rate falls by 5%. Domestic and foreign inflation are both 3%. By roughly what percentage does the real exchange rate fall (%)?", "a": 5, "unit": "%", "tol": 0.1, "hint": "No relative price change.", "sol": "With equal inflation the relative price change is 0, so the real fall is <b>5%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A real exchange rate adjusts the nominal rate for:", opts: ["Interest rates", "Relative price levels", "Trade shares", "Tariffs"], a: 1, why: "Real = nominal × domestic prices ÷ foreign prices." },
  { q: "A country's nominal exchange rate is unchanged and its inflation is higher than its partners'. Its real exchange rate:", opts: ["Rises", "Falls", "Is unchanged", "Cannot be known"], a: 0, why: "Home goods have become relatively dearer, a real appreciation." },
  { q: "The weights in a trade-weighted exchange rate index depend on:", opts: ["Each partner's share of the country's trade", "Each partner's population", "Each partner's inflation", "The interest rates abroad"], a: 0, why: "Larger trading partners count for more." },
  { q: "A real depreciation will most likely:", opts: ["Raise price competitiveness", "Lower price competitiveness", "Have no effect", "Raise imports by itself"], a: 0, why: "Home goods become relatively cheaper for foreigners." },
  { q: "A country's currency rises 8% against one partner and falls 2% against another. The best summary of the overall change is:", opts: ["A trade-weighted index", "The nominal rate against one partner", "The balance of payments", "The terms of trade"], a: 0, why: "A weighted index combines bilateral movements by trade share." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Nominal exchange rate", "Price of one currency in another."],
  ["Real exchange rate", "Nominal rate adjusted for relative prices."],
  ["Real appreciation", "Home goods become relatively dearer; competitiveness falls."],
  ["Trade-weighted index", "Basket of currencies weighted by trade shares."],
  ["REER", "Trade-weighted index adjusted for relative prices."],
  ["Purchasing power parity", "Exchange rates adjust to equalise prices of goods."],
  ["Over-valued currency", "Above its equilibrium or PPP value."],
  ["Appreciation vs revaluation", "Floating rate vs fixed rate."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "An economy imports a large proportion of its raw materials. Its exchange rate depreciates. What is the effect on the external value and the internal value of its money? (May/June 2025 · 31 · Q24, reworded)", opts: ["External value rises; internal value rises", "External value rises; internal value falls", "External value falls; internal value rises", "External value falls; internal value falls"], a: 3, why: "A depreciation is a fall in the external value of the currency. Dearer imported raw materials raise costs and prices, so the internal value (purchasing power at home) also falls." },
  { q: "An economy's currency appreciates and the Marshall-Lerner condition holds. What is the likely effect on imported inflation and on unemployment? (Oct/Nov 2023 · 32 · Q24, reworded)", opts: ["Imported inflation falls; unemployment falls", "Imported inflation falls; unemployment rises", "Imported inflation rises; unemployment falls", "Imported inflation rises; unemployment rises"], a: 1, why: "A stronger currency makes imports cheaper, so imported inflation falls. Exports become dearer, so net exports and employment may fall." },
  { q: "An economy imports most of the factors of production used to make its exports. What effect would a depreciation of its exchange rate have on the price of imported goods and on the price of exported goods, in the domestic currency? (May/June 2023 · 32 · Q26, reworded)", opts: ["Imported goods fall; exported goods fall", "Imported goods fall; exported goods rise", "Imported goods rise; exported goods fall", "Imported goods rise; exported goods rise"], a: 3, why: "The depreciation raises the price of imports. Because export producers rely on imported inputs, their costs rise too, so export prices in the domestic currency rise as well." },
  { q: "A country imports most of the raw materials used as factor inputs. Which policy is most likely to control cost-push inflation? (Feb/March 2024 · 32 · Q26, reworded)", opts: ["An appreciation of the exchange rate", "An increase in the rate of income tax", "An increase in the rate of interest", "An increase in the rate of sales tax"], a: 0, why: "A stronger currency lowers the domestic price of imported inputs, which reduces cost-push pressure directly." },
  { q: "What is likely to be the most effective policy to reduce inflation caused by a rapid rise in import prices? (Feb/March 2024 · 32 · Q20, reworded)", opts: ["A decrease in the domestic rate of interest", "A decrease in the rate of income tax", "An increase in trade tariffs on imports", "A revaluation of the exchange rate"], a: 3, why: "A revaluation lowers the domestic currency price of imports, tackling the source of the inflation. Tariffs would raise import prices further." },
  { q: "Which change would most likely increase structural unemployment in the manufacturing sector of the US? (Oct/Nov 2021 · 33 · Q21, reworded)", opts: ["Asian exporters of manufactured goods to the US experience a fall in labour costs per unit of output", "Tariffs on Asian manufacturing imports increase", "The share of US manufacturing workers in trade unions falls", "The US dollar's real effective exchange rate against Asian currencies falls"], a: 0, why: "Cheaper Asian output makes US producers less competitive. A fall in the US real effective exchange rate would make US goods more competitive, and tariffs would protect them." },
] });
