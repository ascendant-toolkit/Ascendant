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

/* ---------- Employment shares ---------- */
const ES = [["Low", [65, 10, 25]], ["Lower-middle", [40, 20, 40]], ["Upper-middle", [20, 28, 52]], ["High", [3, 20, 77]]], EC = ["f2", "f1", "f3"], EN = ["Primary", "Secondary", "Tertiary"];
function empDraw(s) {
  let o = SV.line(70, 290, 730, 290) + SV.line(70, 290, 70, 30) + SV.text(76, 24, "Share of employment (%)", "sm"); [0, 50, 100].forEach((v) => (o += SV.text(64, 290 - v * 2.4 + 4, v, "sm", { "text-anchor": "end" })));
  ES.forEach(([g, v], i) => { const k = Math.max(0, Math.min(1, s.i - i)); if (k <= 0) return; let c = 0; v.forEach((p, j) => { const h = p * 2.4 * k; o += SV.rect(130 + i * 155, 290 - c * 2.4 * k - h, 100, h, EC[j], op(0.75)); if (p >= 8) o += SV.text(180 + i * 155, 290 - c * 2.4 * k - h / 2 + 5, p + "%", "lbl bd", { "text-anchor": "middle", ...op(k) }); c += p; }); o += SV.text(180 + i * 155, 312, g + " income", "sm", { "text-anchor": "middle", ...op(k) }); });
  EN.forEach((n, j) => { o += SV.rect(520 + j * 70, 332 - 0, 10, 10, EC[j], op(0.75)) + SV.text(534 + j * 70, 341, n, "sm"); });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 350" role="img" aria-label="Stacked bars of employment shares in the primary, secondary and tertiary sectors for low, lower-middle, upper-middle and high-income countries">${empDraw({ i: 4 })}</svg>`;
Lib.stepper($("#stE"), { w: 760, h: 350, label: "Employment shares by sector in four income groups", base: { i: 0 }, draw: empDraw, tween: 1200, dwell: 5600, steps: [
  { cap: "<b>Low income.</b> About 65% of workers are in the primary sector, mostly farming, with productivity low.", s: { i: 1 } },
  { cap: "<b>Lower-middle income.</b> Farm productivity rises, labour is released, and manufacturing and services grow: primary falls to about 40%.", s: { i: 2 } },
  { cap: "<b>Upper-middle income.</b> The secondary sector peaks (about 28%) while services take over as the main source of jobs.", s: { i: 3 } },
  { cap: "<b>High income.</b> The primary share is tiny (3%), manufacturing falls back (de-industrialisation) and services employ over three quarters. (Illustrative typical values.)", s: { i: 4 } },
] });

/* ---------- Commodity prices and terms of trade ---------- */
const CP = [100, 118, 95, 122, 90, 108, 84, 96, 80], MP = [100, 102, 105, 107, 110, 113, 116, 119, 122], TX = (i) => 90 + i * 76, TY = (v) => 300 - (v - 60) * 3.4;
function totDraw(s) {
  let o = axes(70, 300, 730, 30, "Time (years)", "Price index"); [60, 80, 100, 120].forEach((v) => (o += SV.text(64, TY(v) + 4, v, "sm", { "text-anchor": "end" }) + SV.line(70, TY(v), 730, TY(v), "gr", op(0.3))));
  const ln = (arr, c, k) => { const n = Math.max(0, Math.min(8, k * 8)), pts = []; for (let i = 0; i <= Math.floor(n); i++) pts.push([TX(i), TY(arr[i])]); if (n % 1 > 0 && Math.floor(n) < 8) { const a = Math.floor(n), f = n - a; pts.push([TX(a + f), TY(arr[a] + (arr[a + 1] - arr[a]) * f)]); } return pts.length > 1 ? SV.path(Lib.ptsPath(pts), c) : ""; };
  o += ln(CP, "c2", s.a) + (s.a > 0 ? tag(TX(8) + 6, TY(CP[8]) - 18, "Commodity price index", "t2", s.a, "end") : "");
  if (s.b > 0) o += ln(MP, "c1", s.b) + tag(TX(8) + 6, TY(MP[8]) - 8, "Manufactures price index", "t1", s.b, "end");
  if (s.c > 0) { const tt = CP.map((v, i) => v / MP[i] * 100); o += ln(tt, "c4 dash", s.c) + tag(TX(8) - 10, TY(tt[8]) - 12, "Terms of trade: " + Lib.fmtN(tt[8], 0), "t4", s.c, "end"); }
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 345, label: "A primary commodity price index swinging, manufactured prices rising steadily and the terms of trade falling", base: { a: 0, b: 0, c: 0 }, draw: totDraw, tween: 1500, dwell: 5800, steps: [
  { cap: "<b>Volatile prices.</b> Demand for a primary good is inelastic and its supply changes with the weather, so the price swings widely from year to year, with no clear rise over time.", s: { a: 1 } },
  { cap: "<b>Manufactures</b> are priced steadily and tend to rise as technology and brand strength keep prices up.", s: { a: 1, b: 1 } },
  { cap: "<b>The terms of trade</b> (commodity prices ÷ manufacture prices × 100) fall from 100 to about 66. The country must now export about 50% more to pay for the same imports.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labT() {
  if (!$("#xp") || !$("#mp")) return;
  const x = +$("#xp").value, m = +$("#mp").value, tot = x / m * 100, need = m / x;
  $("#r1").textContent = Lib.fmtN(tot, 1); $("#r2").textContent = (tot >= 100 ? "+" : "") + Lib.fmtN(tot - 100, 1) + "%"; $("#r3").textContent = Lib.fmtN(need, 2) + " units";
  $("#rv").textContent = tot < 99.5 ? `The terms of trade have deteriorated to ${Lib.fmtN(tot, 1)}: import prices have risen more (or export prices fallen more) than the other. The country needs ${Lib.fmtN(need, 2)} units of exports to buy each unit of imports it used to get for 1 unit.` : tot > 100.5 ? `The terms of trade have improved to ${Lib.fmtN(tot, 1)}: each unit of exports now buys more imports, about ${Lib.fmtN(1 / need, 2)} units.` : "The terms of trade are unchanged, so each unit of exports buys the same amount of imports.";
  const Y = (v) => 270 - v * 1.25; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "Index", "sm");
  [["Export prices", x, "f1"], ["Import prices", m, "f2"], ["Terms of trade", tot, "f3"]].forEach(([l, v, c], i) => { const px = 60 + i * 115, y = Y(Math.min(v, 200)); o += SV.rect(px, y, 80, 270 - y, c) + SV.text(px + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(px + 40, y - 6, Lib.fmtN(v, 0), "t1", 1, "middle"); });
  $("#labA").innerHTML = o + SV.line(40, Y(100), 400, Y(100), "gr dash");
}
Lib.slider($("#g1"), { id: "xp", label: "Export price index (base 100) ", min: 50, max: 160, step: 5, value: 80, fmt: (v) => v, onInput: labT });
Lib.slider($("#g2"), { id: "mp", label: "Import price index (base 100) ", min: 60, max: 160, step: 5, value: 110, fmt: (v) => v, onInput: labT });
labT();

/* ---------- Lab 2 ---------- */
function labS() {
  if (!$("#sp") || !$("#ss")) return;
  const p = +$("#sp").value; let sec = +$("#ss").value; if (p + sec > 98) sec = 98 - p; const ter = 100 - p - sec, grp = p >= 50 ? "Low-income" : p >= 30 ? "Lower-middle income" : p >= 12 ? "Upper-middle income" : "High-income", ex = p >= 50 ? "Primary products" : p >= 30 ? "Primary and simple manufactures" : p >= 12 ? "Manufactures" : "Capital goods and services";
  $("#t1").textContent = ter + "%"; $("#t2").textContent = grp; $("#t3").textContent = ex;
  $("#tv").textContent = `With ${p}% in the primary sector, ${sec}% in the secondary sector and ${ter}% in services, this structure looks most like a ${grp.toLowerCase()} economy. A high primary share usually means low-productivity farming and exports of primary goods; a large services share is typical of high-income countries. These are tendencies, not rules: oil exporters can be rich with a large primary sector.`;
  const X = (v) => 40 + v * 3.4; let o = SV.line(40, 200, 400, 200) + SV.text(40, 20, "Share of employment (%)", "sm");
  [["Primary", p, "f2"], ["Secondary", sec, "f1"], ["Tertiary", ter, "f3"]].forEach(([l, v, c], i, arr) => { const x0 = arr.slice(0, i).reduce((a, q) => a + q[1], 0); o += SV.rect(X(x0), 120, v * 3.4, 80, c, op(0.7)) + (v > 6 ? SV.text(X(x0 + v / 2), 164, v + "%", "lbl bd", { "text-anchor": "middle" }) : "") + SV.text(X(x0 + v / 2), 220 + i * 18, l, "sm", { "text-anchor": "middle" }); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "sp", label: "Primary sector share, % ", min: 2, max: 80, step: 1, value: 40, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g4"), { id: "ss", label: "Secondary sector share, % ", min: 5, max: 40, step: 1, value: 20, fmt: (v) => v + "%", onInput: labS });
labS();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which sector is it?", buckets: [{"label": "Primary"}, {"label": "Secondary"}, {"label": "Tertiary"}], items: [{"text": "Growing coffee", "b": 0}, {"text": "Assembling cars in a factory", "b": 1}, {"text": "A bank branch", "b": 2}, {"text": "Copper mining", "b": 0}, {"text": "Building houses", "b": 1}, {"text": "A hotel and tourism business", "b": 2}, {"text": "Fishing", "b": 0}, {"text": "A software firm", "b": 2}], done: "Primary: extraction and farming. Secondary: making and building. Tertiary: services." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Primary sector", "Farming, fishing, forestry and mining"], ["De-industrialisation", "A fall in the share of manufacturing in output or jobs"], ["Terms of trade", "Export price index divided by import price index, times 100"], ["Engel's law", "As incomes rise, the share spent on food falls"], ["Diversification", "Spreading production and exports across more products"], ["Intra-industry trade", "Two-way trade in similar goods between countries"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain from higher incomes to a shift in jobs in order.", items: ["Incomes rise", "Spending on food rises slowly but spending on manufactures and services rises faster", "Demand for non-farm output grows", "Farm productivity rises so fewer farm workers are needed", "Labour moves from the primary sector to industry and services"], done: "Income elasticity and productivity both push labour out of farming." });
Lib.calc($("#c1"), { qs: [
  {"q": "Export prices rise from 100 to 108 and import prices rise from 100 to 120. Calculate the terms of trade index.", "a": 90, "unit": "", "tol": 0.5, "hint": "108 ÷ 120 × 100.", "sol": "<b>90</b>: a deterioration of 10%."},
  {"q": "A country's terms of trade fall from 100 to 80. By what percentage have they fallen (%)?", "a": 20, "unit": "%", "tol": 0.5, "hint": "20 ÷ 100.", "sol": "<b>20%</b>."},
  {"q": "Of 40 million workers, 14 million work in agriculture. Calculate the share of employment in the primary sector (%).", "a": 35, "unit": "%", "tol": 0.5, "hint": "14 ÷ 40.", "sol": "<b>35%</b>."},
  {"q": "A country earns $12bn from exports of coffee out of total exports of $15bn. Calculate the share of coffee in exports (%).", "a": 80, "unit": "%", "tol": 0.5, "hint": "12 ÷ 15.", "sol": "<b>80%</b>: a high degree of dependence."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which sector includes manufacturing?", opts: ["Primary", "Secondary", "Tertiary", "Informal"], a: 1, why: "Making goods is the secondary sector." },
  { q: "Low-income countries typically export mainly:", opts: ["Primary products", "Capital goods", "Financial services", "Software"], a: 0, why: "They have few manufactured exports." },
  { q: "A fall in the terms of trade means:", opts: ["More exports must be sold to buy the same imports", "Fewer exports are needed per unit of imports", "Export prices rise faster than import prices", "The exchange rate has been fixed"], a: 0, why: "Import prices have risen relative to export prices." },
  { q: "Which makes primary product prices volatile?", opts: ["Inelastic demand and supply that varies with the weather", "Elastic demand and steady supply", "Fixed prices", "Government price setting"], a: 0, why: "Small shifts cause large price changes." },
  { q: "As an economy develops, the share of agriculture in employment usually:", opts: ["Falls", "Rises", "Stays the same", "Doubles"], a: 0, why: "Labour moves to industry and services." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Primary sector", "Farming, mining, fishing."],
  ["Secondary sector", "Manufacturing and construction."],
  ["Tertiary sector", "Services."],
  ["Engel's law", "Food share of spending falls as income rises."],
  ["Terms of trade", "(Export prices ÷ import prices) × 100."],
  ["Prebisch-Singer", "Primary prices fall relative to manufactures."],
  ["Diversification", "Many products, not one commodity."],
  ["Export-led growth", "Exports as an injection with a multiplier."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which is the most accurate statement about developing economies? (Oct/Nov 2020 · 33 · Q20, reworded)", opts: ["Dependence on primary products for export revenue leaves them reliant on the industrialised world for manufactured goods", "High capital per head means they must trade to grow", "High real GDP per head and high population growth reduce their ability to raise living standards", "Migration from rural to urban areas matters only if it causes labour shortages in rural areas"], a: 0, why: "Developing countries often export primary goods and import manufactures. Capital per head is low, and the other statements are not accurate." },
  { q: "In a developing economy, which policy is most likely to increase the rate of growth but restrict economic development? (Oct/Nov 2021 · 32 · Q28, reworded)", opts: ["More health care provision", "A higher school leaving age", "Removing health and safety regulations", "Promoting export-led growth"], a: 2, why: "Removing safety rules may cut costs and raise output, but worsens working conditions and health, so well-being does not improve." },
  { q: "The current account of the balance of payments moves into deficit. What is a possible reason? (Feb/March 2025 · 32 · Q22, reworded)", opts: ["A decrease in tax revenue", "Export-led growth", "Repaying debts to other countries", "The import of new technology"], a: 3, why: "Imports of new technology raise import spending, which can cause a deficit. Export-led growth and debt repayments do not directly add to the current account deficit." },
  { q: "A low-income economy heavily dependent on primary products receives a car factory built by a foreign company. What will not be a long-lasting benefit? (Oct/Nov 2022 · 31 · Q27, reworded)", opts: ["The company introduces new technology", "The company diversifies the economy's production", "The company provides skills training for local workers", "The company buys non-renewable local construction materials"], a: 3, why: "Using up non-renewable materials is a one-off, not a lasting benefit. The other three improve productivity and diversification." },
  { q: "What has not accompanied global economic growth over the last 25 years? (Oct/Nov 2023 · 32 · Q26, reworded)", opts: ["A depletion of non-renewable resources", "A decrease in international trade", "Growing urbanisation", "More atmospheric pollution"], a: 1, why: "International trade has expanded." },
  { q: "The table shows urbanisation rates for more developed (75% to 86%), less developed (45% to 66%) and least developed (29% to 55%) regions between 2010 and 2050. Which relationship can be confirmed? (Oct/Nov 2022 · 31 · Q29, reworded)", opts: ["The least developed regions have the largest urban populations in both years", "The more developed regions have the lowest growth rate of urbanisation between 2010 and 2050", "The largest region in 2010 will have the fastest population growth", "The region with the largest urban population in 2010 will have the highest urbanisation by 2050"], a: 1, why: "Urbanisation is already high in more developed regions, so it rises by only 11 points, against 21 and 26 elsewhere." },
] });
