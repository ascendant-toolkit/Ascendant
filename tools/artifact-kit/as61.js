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

/* ---------- formula bars ---------- */
function tfDraw(s) {
  const Y = (v) => 250 - v * 1.6; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "Index (base year = 100)", "sm");
  const e = s.e, m = s.m, t = e / m * 100;
  o += SV.rect(120, Y(e), 100, 250 - Y(e), "f2", op(0.65)) + SV.text(170, 270, "Export price index", "sm", { "text-anchor": "middle" }) + SV.text(170, Y(e) - 6, Lib.fmtN(e, 0), "lbl bd", { "text-anchor": "middle" });
  o += SV.rect(280, Y(m), 100, 250 - Y(m), "f3", op(0.65)) + SV.text(330, 270, "Import price index", "sm", { "text-anchor": "middle" }) + SV.text(330, Y(m) - 6, Lib.fmtN(m, 0), "lbl bd", { "text-anchor": "middle" });
  o += SV.rect(440, Y(t), 100, 250 - Y(t), t >= 100 ? "f1" : "f3", op(0.65)) + SV.text(490, 270, "Terms of trade", "sm", { "text-anchor": "middle" }) + SV.text(490, Y(t) - 6, Lib.fmtN(t, 1), "lbl bd", { "text-anchor": "middle" }) + SV.line(60, Y(100), 700, Y(100), "dash") + SV.text(698, Y(100) - 6, "100", "sm", { "text-anchor": "end" });
  o += tag(620, 70, t > 100.5 ? "Improvement" : t < 99.5 ? "Deterioration" : "No change", t > 100.5 ? "c2" : "c3", 1, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="An export price index of 110 and an import price index of 100 give terms of trade of 110">${tfDraw({ e: 110, m: 100 })}</svg>`;
Lib.stepper($("#stF"), { w: 760, h: 290, label: "The terms of trade from two price indices", base: { e: 100, m: 100 }, draw: tfDraw, tween: 900, dwell: 5200, steps: [
  { cap: "<b>Base year.</b> Export and import price indices are both 100, so the terms of trade are 100.", s: { e: 100, m: 100 } },
  { cap: "<b>Export prices rise 10%</b> and import prices are unchanged: terms of trade = 110 ÷ 100 × 100 = <b>110</b>. This is an <b>improvement</b>.", s: { e: 110, m: 100 } },
  { cap: "<b>Import prices now rise 25%</b> (an oil price shock): terms of trade = 110 ÷ 125 × 100 = <b>88</b>. A <b>deterioration</b>.", s: { e: 110, m: 125 } },
] });

/* ---------- what a unit buys ---------- */
function ubDraw(s) {
  const t = s.t, bar = (n, c, y, lab) => { let o = SV.text(40, y + 14, lab, "lbl bd"); for (let i = 0; i < Math.floor(n); i++) o += SV.rect(300 + i * 36, y, 28, 22, c, { rx: 4, ...op(0.7) }); const f = n - Math.floor(n); if (f > 0.05) o += SV.rect(300 + Math.floor(n) * 36, y, 28 * f, 22, c, { rx: 4, ...op(0.7) }); return o + SV.text(300 + Math.ceil(n) * 36 + 10, y + 16, Lib.fmtN(n, 1), "lbl bd"); };
  return bar(1, "f2", 60, "1 unit of exports (a car)") + bar(2 * t / 100, "f3", 120, "buys imports (barrels of oil)") + SV.text(40, 190, "Terms of trade = " + Lib.fmtN(t, 0), "lbl bd", { style: "fill:var(--accent)" });
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 220" role="img" aria-label="At terms of trade of 100 one car buys two barrels of oil, at 70 it buys 1.4">${ubDraw({ t: 70 })}</svg>`;
Lib.stepper($("#stB"), { w: 760, h: 220, label: "Imports bought per unit of exports as the terms of trade change", base: { t: 100 }, draw: ubDraw, tween: 900, dwell: 5200, steps: [
  { cap: "<b>Terms of trade 100.</b> One car exchanges for two barrels of oil.", s: { t: 100 } },
  { cap: "<b>Terms of trade fall to 70.</b> Oil has become dearer relative to cars, so one car now buys only 1.4 barrels: a <b>deterioration</b>. The country must export more to buy the same imports.", s: { t: 70 } },
  { cap: "<b>Terms of trade rise to 130.</b> One car now buys 2.6 barrels: an <b>improvement</b>, which raises purchasing power, but if the higher export price cuts sales, the trade balance may worsen.", s: { t: 130 } },
] });

/* ---------- Lab 1 ---------- */
function labT() {
  if (!["xp", "mp"].every((i) => $("#" + i))) return;
  const e = +$("#xp").value, m = +$("#mp").value, t = e / m * 100, ch = t - 100;
  $("#r1").textContent = Lib.fmtN(t, 1); $("#r2").textContent = (ch >= 0 ? "+" : "") + Lib.fmtN(ch, 1) + "%"; $("#r3").textContent = Lib.fmtN(2 * t / 100, 2);
  $("#rv").textContent = `Terms of trade = ${e} ÷ ${m} × 100 = ${Lib.fmtN(t, 1)}. ${ch > 0.05 ? "The index is above 100: an improvement. Each unit of exports buys more imports." : ch < -0.05 ? "The index is below 100: a deterioration. More exports are needed to buy the same imports." : "No change from the base year."} If one unit of exports bought 2 units of imports in the base year it now buys ${Lib.fmtN(2 * t / 100, 2)}.`;
  $("#labA").innerHTML = tfDraw({ e, m });
}
Lib.slider($("#g1"), { id: "xp", label: "Export price index ", min: 70, max: 140, step: 5, value: 110, fmt: (v) => v, onInput: labT });
Lib.slider($("#g2"), { id: "mp", label: "Import price index ", min: 70, max: 140, step: 5, value: 100, fmt: (v) => v, onInput: labT });
labT();

/* ---------- Lab 2 ---------- */
const CS = [["Currency depreciates 10%", -8, 6, "A weaker currency makes exports cheaper abroad and imports dearer at home."], ["Currency appreciates 10%", 8, -6, "A stronger currency makes exports dearer abroad and imports cheaper."], ["Higher inflation at home than abroad", 6, 0, "Export prices rise faster than import prices."], ["World demand for exports rises", 12, 0, "Higher demand raises export prices."], ["World oil price jumps", 0, 15, "Import prices rise."], ["A glut of the country's commodity exports", -15, 0, "Export prices fall."]];
function showE(i) {
  const [n, e, m, why] = CS[i], t = (100 + e) / (100 + m) * 100; $$("#cB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = (e >= 0 ? "+" : "") + e + "%"; $("#t2").textContent = (m >= 0 ? "+" : "") + m + "%"; $("#t3").textContent = Lib.fmtN(t, 1) + " (" + (t > 100 ? "improves" : "deteriorates") + ")";
  $("#tv").textContent = `${n}: ${why} Export prices change by ${e}% and import prices by ${m}%, so the terms of trade = ${100 + e} ÷ ${100 + m} × 100 = ${Lib.fmtN(t, 1)}, an ${t > 100 ? "improvement" : "deterioration"}.`;
  const Y = (v) => 180 - v * 1.2; $("#labB").innerHTML = SV.line(40, 180, 400, 180) + [["Export price", 100 + e, "f2"], ["Import price", 100 + m, "f3"], ["Terms of trade", t, t >= 100 ? "f1" : "f3"]].map(([l, v, c], k) => SV.rect(70 + k * 110, Y(v), 80, 180 - Y(v), c, op(0.65)) + SV.text(110 + k * 110, 198, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + k * 110, Y(v) - 6, Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" })).join("");
}
$("#cB").innerHTML = CS.map((c, i) => `<button class="b" data-i="${i}">${c[0]}</button>`).join("");
$$("#cB button").forEach((b) => (b.onclick = () => showE(+b.dataset.i)));
showE(0);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What happens to the terms of trade?", buckets: [{"label": "Improve"}, {"label": "Deteriorate"}], items: [{"text": "Export prices rise, import prices unchanged", "b": 0}, {"text": "The exchange rate depreciates", "b": 1}, {"text": "World oil prices rise (country imports oil)", "b": 1}, {"text": "Higher inflation than trading partners", "b": 0}, {"text": "The currency appreciates", "b": 0}, {"text": "Export prices fall", "b": 1}, {"text": "Import prices fall", "b": 0}, {"text": "A glut lowers the price of the main export", "b": 1}], done: "The index rises when export prices rise relative to import prices." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Terms of trade", "Export price index ÷ import price index × 100"], ["Improvement", "Index rises; a unit of exports buys more imports"], ["Deterioration", "Index falls; more exports needed per import"], ["Balance of trade", "Value of exports minus value of imports"], ["Primary products", "Raw materials and farm goods with volatile prices"], ["Price elasticity", "Decides the effect of price changes on trade volumes"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of a depreciation on the terms of trade in order.", items: ["The exchange rate depreciates", "Export prices fall in foreign currency", "Import prices rise in home currency", "Export price index falls relative to import price index", "The terms of trade deteriorate"], done: "Cheaper exports and dearer imports lower the index." });
Lib.calc($("#c1"), { qs: [
  {"q": "Export price index 120 and import price index 100. What is the terms of trade?", "a": 120, "unit": "", "tol": 0.5, "hint": "120 ÷ 100 × 100.", "sol": "<b>120</b>: an improvement."},
  {"q": "Export price index 105, import price index 125. What are the terms of trade (to one decimal place)?", "a": 84, "unit": "", "tol": 0.2, "hint": "105 ÷ 125 × 100.", "sol": "<b>84</b>: a deterioration."},
  {"q": "The terms of trade index rises from 100 to 110. By what % have the terms of trade improved?", "a": 10, "unit": "%", "tol": 0.1, "hint": "10 ÷ 100.", "sol": "<b>10%</b>."},
  {"q": "Export prices rise 6% and import prices rise 10%. Approximately what is the change in the terms of trade (%)?", "a": -3.6, "unit": "%", "tol": 0.3, "hint": "1.06 ÷ 1.10 − 1.", "sol": "<b>−3.6%</b>: a deterioration."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The terms of trade are measured as:", opts: ["Export price index ÷ import price index × 100", "Value of exports − value of imports", "Exports ÷ imports in volume", "Export income ÷ GDP"], a: 0, why: "A ratio of price indices." },
  { q: "An improvement in the terms of trade means:", opts: ["Export prices rise relative to import prices", "The trade balance improves", "Imports fall", "Exports rise in volume"], a: 0, why: "Relative prices." },
  { q: "A depreciation will usually:", opts: ["Worsen the terms of trade", "Improve the terms of trade", "Not affect the terms of trade", "Raise the index above 100"], a: 0, why: "Exports cheaper, imports dearer." },
  { q: "The terms of trade have no units because:", opts: ["They are a ratio of two indices", "They use several currencies", "They are not measurable", "They are a percentage of GDP"], a: 0, why: "Index ÷ index." },
  { q: "A country that exports primary products may find its terms of trade:", opts: ["Deteriorate over time", "Always improve", "Never change", "Equal the trade balance"], a: 0, why: "Volatile prices and slow demand growth." },
] });
Lib.cards($("#fc1"), { cards: [
  ["ToT formula", "Export index ÷ import index × 100."],
  ["Improvement", "Index rises."],
  ["Deterioration", "Index falls."],
  ["Depreciation", "ToT deteriorate."],
  ["Appreciation", "ToT improve."],
  ["Higher inflation", "Export prices up, ToT improve."],
  ["Not BoT", "ToT is prices; BoT is values."],
  ["Evaluate", "Elasticity and competitiveness."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A country's terms of trade changed from 100 to 95. What is most likely to have caused this change? (Feb/March 2021 · 12 · Q20, reworded)", opts: ["a depreciation of the country's currency", "a reduction in import tariffs", "a rise in the price of exported goods", "an improvement in the balance of trade"], a: 0, why: "A depreciation lowers export prices relative to import prices, so the index falls." },
  { q: "The terms of trade index for Mauritius fell from 111.2 in the first quarter of 2018 to 106.1 in the second quarter. Which combination could have produced this outcome? (export prices, import prices) (Feb/March 2022 · 12 · Q21, reworded)", opts: ["rose, fell", "rose, rose", "rose, unchanged", "unchanged, fell"], a: 1, why: "The index falls only if import prices rise by more than export prices. Both could rise, with imports rising faster." },
  { q: "The prices of a country's exports rise by 5% while the prices of its imports fall by 5%. What will definitely improve in the country as a result of these changes? (Feb/March 2022 · 12 · Q25, reworded)", opts: ["balance of trade", "current account balance", "exchange rate", "terms of trade"], a: 3, why: "Export prices rising relative to import prices improves the terms of trade. The effect on the trade balance depends on elasticities." },
  { q: "What can be best understood from a knowledge of a country's terms of trade? (Feb/March 2023 · 12 · Q24, reworded)", opts: ["its balance of payments performance", "the purchasing power of its exports", "the standard of living within the country", "the value of its real exchange rate"], a: 1, why: "The terms of trade show how many imports a unit of exports can buy." },
  { q: "When must the terms of trade of a country change? (Feb/March 2024 · 12 · Q26, reworded)", opts: ["when the volume of exports falls and the volume of imports rises", "when the total value of exports falls and the total value of imports rises", "when the balance of trade in goods moves from deficit to surplus", "when the average price of exports rises and the average price of imports falls"], a: 3, why: "The terms of trade depend on prices, not volumes or values." },
  { q: "Country X trades with country Y. What are the terms of trade for country X? (Feb/March 2025 · 12 · Q26, reworded)", opts: ["the average price of country X's exports divided by the average price of country Y's exports", "the ratio of an index of country X's export prices to an index of its import prices", "the value of country X's exports divided by the value of country Y's exports", "the value of country X's imports divided by the value of country Y's imports"], a: 1, why: "Terms of trade = export price index ÷ import price index." },
  { q: "Why does the value of a country's terms of trade have no monetary units? (May/June 2020 · 12 · Q25, reworded)", opts: ["It cannot be calculated accurately enough", "It includes more than one currency", "It is a ratio of two index numbers", "It measures change over time"], a: 2, why: "A ratio of two indices has no units." },
  { q: "The table shows the relative price of exports compared with imports as an index (2013 = 100): 2013 is 100, 2014 is 97 and 2015 is 95. Which statement about the period 2013 to 2015 is correct? (May/June 2020 · 13 · Q23, reworded)", opts: ["Export prices have increased each year", "The general level of prices has fallen", "The terms of trade have deteriorated", "The volume of imports increasingly exceeds the volume of exports"], a: 2, why: "A falling index of export prices relative to import prices is a deterioration." },
  { q: "Why might an unfavourable movement in a country's terms of trade benefit its economy? (May/June 2021 · 11 · Q20, reworded)", opts: ["It would force inefficient firms out of business", "It would increase the quantity of goods available for domestic consumption", "It would make domestically-produced goods more expensive than imports", "It would make the country's exports relative to imports more competitive internationally"], a: 3, why: "Lower export prices relative to import prices improve competitiveness." },
  { q: "What leads to a fall in a country's terms of trade? (May/June 2022 · 11 · Q24, reworded)", opts: ["a fall in the price of exports relative to the price of imports", "a fall in the price of imports relative to the price of exports", "a fall in the quantity of exports relative to the quantity of imports", "a fall in the quantity of imports relative to the quantity of exports"], a: 0, why: "The terms of trade are based on relative prices." },
  { q: "What will lead to an improvement in the terms of trade? (May/June 2022 · 12 · Q21, reworded)", opts: ["Export prices fall by 10% and import prices fall by 5%", "Export prices fall by 10% and import prices rise by 5%", "Export prices rise by 5% and import prices rise by 10%", "Export prices rise by 10% and import prices rise by 5%"], a: 3, why: "The index rises only if export prices rise by more than (or fall by less than) import prices." },
  { q: "What could explain an improvement in the terms of trade for a country? (May/June 2022 · 13 · Q20, reworded)", opts: ["an increase in tariffs on imports", "a decrease in the volume of imports sold", "an increase in the prices of exports", "a decrease in the volume of exports sold"], a: 2, why: "Higher export prices improve the terms of trade. Volumes and tariffs do not change the price ratio directly." },
] });
