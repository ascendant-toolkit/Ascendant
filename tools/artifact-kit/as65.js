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

function chainDraw(nodes, k) {
  const H = 40, G = 16; let o = "";
  nodes.forEach((t, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const y = 8 + i * (H + G);
    o += SV.rect(30, y, 700, H, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.55 * v) }) + SV.text(380, y + 25, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
    if (i > 0) o += SV.poly([[373, y - 10], [387, y - 10], [380, y - 2]], "dot4", op(v));
  });
  return o;
}
function chainStep(el, label, nodes, caps) {
  Lib.stepper($(el), { w: 760, h: 16 + nodes.length * 56, label, base: { k: 0 }, draw: (s) => chainDraw(nodes, s.k), tween: 700, dwell: 5200, steps: nodes.map((n, i) => ({ cap: caps[i], s: { k: i + 1 } })) });
}
function chooser(p, items, tmpl) {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, "Strength of the case: " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}

$("#pic1").innerHTML = (() => {
  const items = [["Imports rise", "Strong demand, high exchange rate, high costs", "f3"], ["Exports fall", "Poor competitiveness, weak demand abroad", "f3"], ["Income outflows", "Profits and interest paid abroad", "f3"], ["Current account deficit", "Payments exceed receipts", "f2"]];
  let o = ""; items.forEach(([n, d, c], i) => { const y = 12 + i * 58; o += SV.rect(30, y, 700, 46, c, { rx: 8, ...op(0.45) }) + SV.text(50, y + 20, n, "lbl bd") + SV.text(50, y + 38, d, "sm"); });
  return `<svg viewBox="0 0 760 252" role="img" aria-label="Causes of a current account deficit: higher imports, lower exports and income outflows">${o}</svg>`;
})();
chainStep("#stA", "How a deficit can build up", ["Incomes and consumer spending rise strongly", "Households buy more imports (high income elasticity)", "Domestic firms are less competitive, so exports lag", "Imports exceed exports", "A current account deficit appears and persists"], [
  "<b>Strong growth</b> and cheap credit raise spending.", "<b>More spending on imports</b> as people buy foreign goods and services.", "<b>High costs or a high exchange rate</b> make exports dearer abroad.", "<b>The trade balance</b> moves into deficit.", "<b>If the structure does not change</b>, the deficit may last."]);
chainStep("#stB", "What a persistent deficit may lead to", ["Net exports are negative, so AD is lower", "Output and employment could be weaker", "The currency may come under downward pressure", "The country may borrow or run down reserves", "Policy makers may adopt contractionary or supply-side policies"], [
  "<b>Net exports</b> subtract from AD.", "<b>Lower AD</b> could reduce output and jobs.", "<b>Demand for the currency</b> falls relative to supply.", "<b>Financing the gap</b> may mean more debt or lost reserves.", "<b>Policies to correct the deficit</b> may be needed, with their own costs."]);

chooser("g", [
  ["Strong consumer spending", "Imports rise because of high incomes", "Goods and services", "Persistent if growth is led by consumption, not investment", 3],
  ["Poor competitiveness", "Exports fall and imports rise", "Goods and services", "Low productivity and quality are slow to fix", 5],
  ["High exchange rate", "Exports dearer, imports cheaper", "Goods and services", "May reverse as the currency adjusts, unless fixed", 3],
  ["Falling terms of trade", "Export revenue buys fewer imports", "Goods mainly", "Persistent if commodity prices stay low", 4],
  ["Weak world demand", "Exports fall", "Goods and services", "Usually temporary, as it follows the world cycle", 2],
  ["Profits sent abroad", "Primary income outflow rises", "Primary income", "Persistent when much of industry is foreign-owned", 4]
], (it) => `${it[0]}: ${it[1].toLowerCase()}, mainly affecting ${it[2].toLowerCase()}. ${it[3]}.`);

chooser("h", [
  ["Lower AD and output (deficit)", "Domestic households and firms", "Down: negative net exports", "Size of the deficit and spare capacity", 4],
  ["Currency depreciation (deficit)", "Importers, exporters, consumers", "Down: higher import prices, cheaper exports", "Fixed exchange rate; central bank action", 3],
  ["Debt and asset sales (deficit)", "Future generations, the external sector", "Up: more income flows abroad later", "Whether borrowing funds investment", 4],
  ["Higher AD and jobs (surplus)", "Exporters and their workers", "Up: net exports are positive", "Whether the surplus comes from weak demand", 3],
  ["Currency appreciation (surplus)", "Exporters; importers gain", "Up: export prices rise abroad", "Central bank intervention", 3],
  ["Harm to trading partners (surplus)", "Deficit countries", "Their deficits and unemployment rise", "Size of the surplus; retaliation risk", 3]
], (it) => `${it[0]}: this affects ${it[1].toLowerCase()}, with the direction: ${it[2].toLowerCase()}. It may be limited by ${it[3].toLowerCase()}.`);
Lib.classify($("#cl1"), { prompt: "Is it a possible cause of a deficit or of a surplus?", buckets: [{"label": "Deficit"}, {"label": "Surplus"}], items: [{"text": "Rapid growth in consumer spending", "b": 0}, {"text": "Low productivity and high costs", "b": 0}, {"text": "Strong price competitiveness", "b": 1}, {"text": "A high exchange rate", "b": 0}, {"text": "High household saving and weak spending", "b": 1}, {"text": "A fall in commodity export prices", "b": 0}, {"text": "Low value of the currency", "b": 1}, {"text": "Large profits sent to foreign owners", "b": 0}], done: "Deficit causes raise imports or lower exports; surplus causes do the opposite." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Current account deficit", "Payments to the rest of the world exceed receipts"], ["Persistent deficit", "A deficit that lasts for many years"], ["Primary income", "Investment income and employee pay from abroad"], ["Secondary income", "Transfers such as aid and remittances"], ["Competitiveness", "Ability to sell goods at attractive price and quality"], ["Reserves", "Foreign currency held by the central bank"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of a persistent deficit in order.", items: ["Imports exceed exports", "Net exports lower AD", "The currency comes under downward pressure", "The country borrows or uses reserves", "Policy makers consider corrective policies"], done: "Deficit lowers AD, pressures the currency and needs financing." });
Lib.calc($("#c1"), { qs: [
  {"q": "Goods balance -40, services balance +25, primary income +10, secondary income -5 (all $bn). What is the current account balance ($bn)?", "a": -10, "unit": "$bn", "tol": 0.5, "hint": "-40 + 25 + 10 - 5.", "sol": "<b>-$10bn</b>, a deficit."},
  {"q": "GDP is $500bn and the current account deficit is $20bn. What is the deficit as a % of GDP?", "a": 4, "unit": "%", "tol": 0.05, "hint": "20 ÷ 500.", "sol": "<b>4%</b>."},
  {"q": "The accounts sum to zero. Current account -30, capital account +5, financial account +20. What is the balancing item?", "a": 5, "unit": "", "tol": 0.5, "hint": "-30 + 5 + 20 + b = 0.", "sol": "<b>+5</b>."},
  {"q": "Exports are $250bn and imports $200bn of goods and services. What is the surplus ($bn)?", "a": 50, "unit": "$bn", "tol": 0.5, "hint": "250 - 200.", "sol": "<b>$50bn</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A current account deficit means:", opts: ["Payments exceed receipts", "Receipts exceed payments", "Exports exceed imports", "No trade"], a: 0, why: "Outflows are larger." },
  { q: "A likely cause of a deficit is:", opts: ["A high exchange rate", "A low exchange rate", "High saving", "Weak imports"], a: 0, why: "Exports dear, imports cheap." },
  { q: "A fixed exchange rate with a deficit may cause:", opts: ["Falling reserves", "Rising reserves", "No effect", "Lower imports"], a: 0, why: "The central bank buys the currency." },
  { q: "A surplus could be a sign of:", opts: ["Weak domestic demand", "Strong imports", "Falling exports", "A depreciation only"], a: 0, why: "Low spending reduces imports." },
  { q: "A persistent deficit could lead to:", opts: ["More debt or asset sales", "Higher reserves", "Lower AD only if exports rise", "No consequences"], a: 0, why: "The gap has to be financed." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Deficit", "Payments exceed receipts."],
  ["Surplus", "Receipts exceed payments."],
  ["Cause: competitiveness", "Costs, quality, productivity."],
  ["Cause: exchange rate", "High rate hurts exports."],
  ["Cause: terms of trade", "Export revenue buys less."],
  ["Consequence", "Lower AD, depreciation, debt."],
  ["Surplus risk", "Weak demand; partners hurt."],
  ["Judge", "Size, cause, persistence."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is not a likely cause of a deficit in the current account of the balance of payments? (Feb/March 2024 · 12 · Q30, reworded)", opts: ["Consumer spending is low.", "Primary incomes in the form of investment income are low.", "The rate of exchange is high.", "Wage costs of production are high."], a: 0, why: "Low consumer spending means fewer imports, which would tend to help the current account." },
  { q: "High economic growth is often accompanied by a worsening of the current account of the balance of payments. Which reason for this trend is not valid? (Feb/March 2025 · 12 · Q20, reworded)", opts: ["Economic growth raises domestic consumption, leaving very little to sell to overseas consumers.", "Economic growth raises domestic output, leading to lower prices and more price-competitive goods both at home and abroad.", "Economic growth raises incomes and leads to rising demand for foreign goods.", "Economic growth results in rising requirements of inputs from other countries."], a: 1, why: "Lower prices and greater competitiveness would help rather than worsen the current account." },
  { q: "An extract from a country's balance of payments ($ billion): trade in goods, exports 150 and imports 200; trade in services, exports 70 and imports 50; primary (investment) income, receipts 120 and payments 100; secondary (transfer) income, receipts 15 and payments 20. What is the current account balance? (Feb/March 2024 · 12 · Q27, reworded)", opts: ["-$10bn", "-$15bn", "-$30bn", "-$50bn"], a: 1, why: "(150 - 200) + (70 - 50) + (120 - 100) + (15 - 20) = -50 + 20 + 20 - 5 = -15." },
  { q: "The figures are from New Zealand's balance of payments for 2017 (NZ$m): capital account balance 1300, current account balance -7000, financial account balance 7600, goods balance -3000, services balance 5000. What was the value of the balancing item (net errors and omissions) in NZ$m? (May/June 2021 · 12 · Q23, reworded)", opts: ["-3900", "-2000", "-1900", "5700"], a: 2, why: "The accounts sum to zero: -7000 + 1300 + 7600 + balancing item = 0, so the balancing item is -1900." },
  { q: "A country with a floating exchange rate experiences a large surplus on the current account of its balance of payments. What is likely to decrease as a consequence? (Feb/March 2020 · 12 · Q24, reworded)", opts: ["exports of capital from the country", "the level of employment in the country", "the prices of imports into the country", "the value of the country's currency"], a: 2, why: "A surplus tends to raise demand for the currency, so the exchange rate rises and import prices fall." },
  { q: "Why is a balance of payments deficit a potential problem for an economy with a fixed exchange rate? (May/June 2020 · 13 · Q27, reworded)", opts: ["Domestic money supply will increase.", "Rival economies may react with trade protection measures.", "The economy's foreign exchange reserves may decrease.", "The economy's short-run standard of living will be reduced."], a: 2, why: "Under a fixed rate the central bank buys the currency using reserves, which fall." },
  { q: "Other things being equal, what is most likely to be reduced by falling labour productivity? (Feb/March 2021 · 12 · Q29, reworded)", opts: ["the balance of trade deficit", "the internal value of money", "the level of unemployment", "the rate of domestic inflation"], a: 1, why: "Lower productivity raises unit costs and prices, so the internal value of money falls." },
] });
