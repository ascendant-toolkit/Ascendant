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

/* ---------- GDP to NNI ---------- */
const GY = (v) => 300 - v * 2.2;
function gdpDraw(s) {
  let o = axes(70, 300, 730, 30, "", "$bn"); [0, 40, 80, 120].forEach((v) => (o += SV.text(64, GY(v) + 4, v, "sm", { "text-anchor": "end" })));
  const bar = (i, v, c, l, k) => (k > 0 ? SV.rect(110 + i * 150, GY(v), 100, 300 - GY(v), c, op(k)) + tag(160 + i * 150, GY(v) - 8, v, "t1", k, "middle") + tag(160 + i * 150, 322, l, "t1", k, "middle") : "");
  o += bar(0, 120, "f1", "GDP", s.a) + bar(1, 114, "f1", "GNI", s.b) + bar(2, 105, "f3", "NNI", s.c);
  if (s.b > 0) o += tag(310, GY(114) - 28, "− 6 net income paid abroad", "t2", s.b, "middle");
  if (s.c > 0) o += tag(460, GY(105) - 28, "− 9 depreciation", "t2", s.c, "middle");
  if (s.d > 0) o += SV.rect(600, 190, 130, 110, "f2", op(0.6 * s.d)) + tag(665, 230, "÷ 10m people", "t4", s.d, "middle") + tag(665, 256, "= $10,500", "t4", s.d, "middle") + tag(665, 322, "NNI per head", "t4", s.d, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="GDP of 120, GNI of 114 after net income paid abroad and NNI of 105 after depreciation, then NNI per head">${gdpDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 340, label: "From GDP to GNI to NNI and then per head", base: { a: 0, b: 0, c: 0, d: 0 }, draw: gdpDraw, tween: 1100, dwell: 5600, steps: [
  { cap: "<b>GDP</b> is the value of everything produced inside the country: $120bn.", s: { a: 1 } },
  { cap: "<b>GNI.</b> Foreign firms and investors take $6bn of profit and interest abroad that residents do not earn. Add net property income from abroad (here −$6bn): GNI is $114bn.", s: { a: 1, b: 1 } },
  { cap: "<b>NNI.</b> Capital wears out (depreciation $9bn). Deduct it to find income that could be spent without shrinking the capital stock: $105bn.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Per head.</b> With a population of 10 million, NNI per head is $10,500. Adjusting for inflation gives the real figure used to track living standards.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Market versus PPP ---------- */
const PB = (v) => 300 - v * 0.0052;
function ppDraw(s) {
  let o = axes(70, 300, 730, 30, "", "GDP per head ($)"); [0, 15000, 30000, 45000].forEach((v) => (o += SV.text(64, PB(v) + 4, v.toLocaleString("en-US"), "sm", { "text-anchor": "end" })));
  const bar = (x, v, c, l, k) => (k > 0 ? SV.rect(x, PB(v), 80, 300 - PB(v), c, op(k)) + tag(x + 40, PB(v) - 8, "$" + Math.round(v).toLocaleString("en-US"), "t1", k, "middle") + tag(x + 40, 322, l, "sm", k, "middle") : "");
  o += bar(120, 3000, "f2", "Country A: market", s.a) + bar(240, 45000, "f1", "Country B: market", s.a);
  o += bar(400, 3000 + 6000 * Math.min(1, s.b), "f2", "Country A: PPP", s.b) + bar(520, 45000, "f1", "Country B: PPP", s.b);
  if (s.c > 0) o += tag(400, 34, "Gap: 15 to 1 at market rates, 5 to 1 at PPP", "t4", s.c, "middle");
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 340, label: "GDP per head at market exchange rates compared with PPP for a low-price and a high-price country", base: { a: 0, b: 0, c: 0 }, draw: ppDraw, tween: 1300, dwell: 5800, steps: [
  { cap: "<b>At market exchange rates</b> country A's GDP per head is $3,000 and country B's is $45,000: B looks 15 times richer.", s: { a: 1 } },
  { cap: "<b>But prices differ.</b> Food, housing and services cost much less in A. A basket of goods costs one third of what it does in B.", s: { a: 1 } },
  { cap: "<b>PPP adjustment.</b> Using the cost of the same basket, A's income buys what $9,000 buys in B. The gap narrows to 5 to 1.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labR() {
  if (!$("#ng") || !$("#pi") || !$("#pp")) return;
  const n = +$("#ng").value / 10, p = +$("#pi").value / 10, q = +$("#pp").value / 10, real = ((1 + n / 100) / (1 + p / 100) - 1) * 100, ph = ((1 + real / 100) / (1 + q / 100) - 1) * 100;
  $("#r1").textContent = Lib.fmtN(real, 1) + "%"; $("#r2").textContent = (ph >= 0 ? "+" : "") + Lib.fmtN(ph, 1) + "%"; $("#r3").textContent = ph > 0.05 ? Lib.fmtN(70 / ph, 0) + " yrs" : "never";
  $("#rv").textContent = `Nominal GDP grows ${Lib.fmtN(n, 1)}%, but inflation of ${Lib.fmtN(p, 1)}% leaves real growth of ${Lib.fmtN(real, 1)}%. With population growth of ${Lib.fmtN(q, 1)}%, real GDP per head changes by ${Lib.fmtN(ph, 1)}%. ${ph > 0.05 ? "At that rate real income per head doubles in about " + Lib.fmtN(70 / ph, 0) + " years (rule of 70)." : "Real income per head is not rising, so material living standards are not improving on this measure."}`;
  const Y = (v) => 150 - v * 8; let o = SV.line(40, 150, 400, 150) + SV.line(40, 20, 40, 280) + SV.text(46, 16, "% a year", "sm");
  [["Nominal GDP", n, "f1"], ["Real GDP", real, "f1"], ["Real GDP per head", ph, "f3"]].forEach(([l, v, c], i) => { const x = 60 + i * 115, y = Y(Math.max(-17, Math.min(17, v))); o += SV.rect(x, Math.min(y, 150), 80, Math.abs(y - 150), c) + SV.text(x + 40, 296, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, v >= 0 ? y - 8 : y + 18, Lib.fmtN(v, 1) + "%", "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ng", label: "Nominal GDP growth, % ", min: 0, max: 200, step: 5, value: 90, fmt: (v) => (v / 10).toFixed(1), onInput: labR });
Lib.slider($("#g2"), { id: "pi", label: "Inflation, % ", min: 0, max: 150, step: 5, value: 40, fmt: (v) => (v / 10).toFixed(1), onInput: labR });
Lib.slider($("#g3"), { id: "pp", label: "Population growth, % ", min: 0, max: 50, step: 1, value: 15, fmt: (v) => (v / 10).toFixed(1), onInput: labR });
labR();

/* ---------- Lab 2 ---------- */
function labP() {
  if (!$("#bk")) return;
  const b = +$("#bk").value, ppp = b / 10, mk = 600000 / 60, pp = 600000 / ppp;
  $("#t1").textContent = Lib.fmtN(ppp, 0) + " per $"; $("#t2").textContent = "$" + Math.round(mk).toLocaleString("en-US"); $("#t3").textContent = "$" + Math.round(pp).toLocaleString("en-US");
  $("#tv").textContent = b < 600 ? `The basket costs ${b} local units against $10 in the US, so one dollar of income buys the same basket as ${Lib.fmtN(ppp, 0)} local units, compared with the market rate of 60. The currency is worth more at PPP, so GDP per head at PPP ($${Math.round(pp).toLocaleString("en-US")}) is higher than at the market rate.` : b > 600 ? `Prices here are higher than the market exchange rate suggests, so GDP per head at PPP is lower than at the market rate.` : "The PPP rate equals the market rate, so both measures agree.";
  const Y = (v) => 270 - v / 40000 * 240; let o = SV.line(60, 270, 400, 270) + SV.line(60, 270, 60, 20) + SV.text(66, 16, "GDP per head ($)", "sm");
  [["Market rate", mk, "f1"], ["PPP", pp, "f3"]].forEach(([l, v, c], i) => { const x = 100 + i * 140; o += SV.rect(x, Y(Math.min(v, 40000)), 90, 270 - Y(Math.min(v, 40000)), c) + SV.text(x + 45, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 45, Y(Math.min(v, 40000)) - 8, "$" + Math.round(v).toLocaleString("en-US"), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "bk", label: "Local price of the basket (units) ", min: 100, max: 900, step: 25, value: 300, fmt: (v) => v, onInput: labP });
labP();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which measure is it?", buckets: [{"label": "GDP"}, {"label": "GNI"}, {"label": "NNI"}], items: [{"text": "Value of output produced inside the country's borders", "b": 0}, {"text": "GDP plus net property income from abroad", "b": 1}, {"text": "GNI minus depreciation of capital", "b": 2}, {"text": "Includes profits that foreign-owned firms in the country send home", "b": 0}, {"text": "Income earned by a country's residents wherever their assets are", "b": 1}, {"text": "Shows income that could be consumed without running down the capital stock", "b": 2}, {"text": "Output method, income method or expenditure method", "b": 0}, {"text": "Used by the World Bank for income classification", "b": 1}], done: "GDP: inside the borders. GNI: residents' income. NNI: GNI minus depreciation." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Real GDP per capita", "GDP adjusted for inflation and divided by the population"], ["Purchasing power parity", "Compares the cost of the same basket of goods in two countries"], ["Informal economy", "Unrecorded economic activity that is missing from official statistics"], ["Net property income from abroad", "Income earned abroad less income paid abroad"], ["Rule of 70", "Years to double ≈ 70 ÷ growth rate"], ["Low base effect", "A poor country's fast growth adds little in absolute terms"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps to a real per capita figure in order.", items: ["Start with GDP (or GNI) in current prices", "Adjust for price changes using a price index and a base year", "Divide by the population", "Compare the growth rate over time", "Use PPP if comparing between countries"], done: "Real removes inflation; per capita removes population; PPP adjusts for price levels." });
Lib.calc($("#c1"), { qs: [
  {"q": "GDP is $200bn. Net property income from abroad is −$12bn and depreciation is $15bn. Calculate NNI ($bn).", "a": 173, "unit": "$bn", "tol": 0.5, "hint": "GDP + net income − depreciation.", "sol": "200 − 12 − 15 = <b>$173bn</b>."},
  {"q": "Real GDP is $90bn and the population is 30 million. Calculate real GDP per head ($).", "a": 3000, "unit": "$", "tol": 0.5, "hint": "90,000m ÷ 30m.", "sol": "<b>$3,000</b>."},
  {"q": "Nominal GDP rises by 8% and prices by 5%. Calculate the approximate real growth (%, 1 decimal place).", "a": 2.9, "unit": "%", "tol": 0.1, "hint": "1.08 ÷ 1.05 − 1.", "sol": "1.08 ÷ 1.05 = 1.0286, so about <b>2.9%</b> (roughly 3%)."},
  {"q": "A basket costs 750 rupees in one country and $5 in the US. Calculate the PPP rate (rupees per $).", "a": 150, "unit": "rupees", "tol": 0.5, "hint": "750 ÷ 5.", "sol": "<b>150 rupees = $1</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "GNI is calculated as:", opts: ["GDP + net property income from abroad", "GDP − depreciation", "GDP + imports", "GDP − taxes"], a: 0, why: "GNI adds income from abroad and subtracts income paid abroad." },
  { q: "PPP is used to:", opts: ["Adjust for differences in price levels between countries", "Measure inflation", "Calculate unemployment", "Convert at market exchange rates"], a: 0, why: "It compares the cost of the same basket." },
  { q: "Which is a problem with GDP per head as a measure of living standards?", opts: ["It ignores income distribution", "It is always accurate", "It includes leisure", "It includes the informal economy fully"], a: 0, why: "An average hides who gets the income." },
  { q: "Real GDP per head differs from nominal GDP because it:", opts: ["Removes the effect of inflation", "Includes the shadow economy", "Is measured in dollars", "Counts only exports"], a: 0, why: "Prices are held constant using a base year." },
  { q: "Which is a non-monetary indicator of the standard of living?", opts: ["Life expectancy", "GDP per head", "GNI", "Average wage"], a: 0, why: "Life expectancy measures health outcomes directly." },
] });
Lib.cards($("#fc1"), { cards: [
  ["GDP", "Value of output within the country."],
  ["GNI", "GDP + net property income from abroad."],
  ["NNI", "GNI − depreciation."],
  ["Real", "Adjusted for inflation."],
  ["Per capita", "Divided by population."],
  ["PPP", "Cost of the same basket in two countries."],
  ["Problems of GDP", "Informal economy, distribution, externalities, accuracy."],
  ["Rule of 70", "70 ÷ growth rate = years to double."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which statement about national income accounting is correct? (May/June 2021 · 31 · Q21, reworded)", opts: ["Depreciation does not need to be subtracted from GDP because firms have already allowed for it", "GDP overstates the value of output because profit includes supernormal profit", "GDP is a better measure of living standards than GNP because net property income from abroad is not available to citizens", "GNP per capita ignores many important factors that affect citizens' living standards"], a: 3, why: "GNP per head is an average of money income. It ignores distribution, leisure, the environment and many non-material factors." },
  { q: "A government uses personal disposable income per head as a measure of the standard of living. What does this measure not take into account? (Oct/Nov 2021 · 31 · Q21, reworded)", opts: ["Changes in the average price level", "The level of direct taxation", "The level of national income", "The size of the population"], a: 0, why: "Disposable income is after tax and per head, but unless it is deflated (made real) it ignores price changes." },
  { q: "GNP per head has increased by 10% over five years. What is not a valid reason to doubt that average living standards have risen by 10%? (Oct/Nov 2021 · 33 · Q19, reworded)", opts: ["The distribution of income may have changed a lot", "The general price level is likely to have changed", "The size of the population may have changed", "The workforce may have produced more by working longer hours"], a: 2, why: "A per head figure already allows for population. The other three are valid doubts: distribution, inflation and longer working hours." },
  { q: "Real GNP per capita is used to compare living standards in a developed and a developing country. What is not a good reason to question the accuracy of this comparison? (Oct/Nov 2022 · 33 · Q20, reworded)", opts: ["Spending patterns differ, so price indices are not accurate", "People enjoy very different amounts of leisure time", "The extent of the unrecorded economy differs", "Purchasing power parity has been used to make the comparison"], a: 3, why: "PPP improves the comparison. The other three are genuine reasons for caution." },
  { q: "What is a definition of purchasing power parity? (Oct/Nov 2023 · 31 · Q28, reworded)", opts: ["The amount of domestic currency needed to buy a unit of foreign currency", "The quantity of a currency needed to buy the same basket of goods in both countries", "The quantity of goods a person on an average income can buy", "The value of household spending on goods and services in a country"], a: 1, why: "PPP compares the cost of an identical basket in two countries." },
  { q: "Which combination indicates that GDP per capita is likely to be an accurate indicator of living standards over time? Hidden economy as a share of GDP, quality of goods and services, income distribution. (Oct/Nov 2022 · 31 · Q20, reworded)", opts: ["Large, improving, unequal", "Large, constant, equal", "Small, improving, equal", "Small, constant, unequal"], a: 2, why: "A small hidden economy, improving quality and equal distribution make average income closer to the typical person's experience." },
  { q: "The table shows GDP and population of four countries. Which is most likely to have the lowest standard of living? A: Bangladesh, GDP $206.7bn, population 153.5m. B: India, $2,989bn, 1,147.9m. C: Nigeria, $292.7bn, 138.3m. D: South Africa, $467.1bn, 43.8m. (May/June 2024 · 31 · Q28, reworded)", opts: ["A", "B", "C", "D"], a: 0, why: "GDP per head: A about $1,350, B about $2,600, C about $2,100, D about $10,700. Bangladesh has the lowest." },
  { q: "Why is real GDP per head thought to be an imperfect measure of welfare in developed economies? (Feb/March 2022 · 32 · Q19, reworded)", opts: ["Governments often manipulate data", "No account is taken of inflation", "The data's content and coverage are restricted", "The shadow economy is bigger than the official economy"], a: 2, why: "It leaves out unpaid work, leisure, the environment and distribution." },
] });
