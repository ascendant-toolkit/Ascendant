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

/* ---------- waterfall ---------- */
function wfDraw(items, s) {
  // items: [label, value, kind] kind: "t" total, "d" delta; s.k = number of items visible
  const max = Math.max(...items.map((it) => it[3] || 0)) * 1.15, Y = (v) => 250 - (v / max) * 190, w = 600 / items.length; let o = SV.line(50, 250, 740, 250);
  items.forEach((it, i) => {
    const [lab, val, kind, top, bot] = it, x = 70 + i * (w + 8), v = Math.max(0, Math.min(1, s.k - i));
    if (v <= 0) return;
    o += SV.rect(x, Y(top), w - 20, Math.max(2, Y(bot) - Y(top)), kind === "t" ? "f1" : val < 0 ? "f3" : "f2", op(0.65 * v)) + SV.text(x + (w - 20) / 2, Y(top) - 8, (kind === "d" && val > 0 ? "+" : "") + Lib.fmtN(val, 0), "lbl bd", { "text-anchor": "middle", ...op(v) }) + SV.text(x + (w - 20) / 2, 270, lab, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return o;
}
const A = { gdp: 100, net: -5, dep: 10 };
const itemsA = [["GDP", 100, "t", 100, 0], ["Net income from abroad", -5, "d", 100, 95], ["GNI", 95, "t", 95, 0], ["Capital consumption", -10, "d", 95, 85], ["NNI", 85, "t", 85, 0]];
function nDraw(s) { return wfDraw(itemsA, s); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="GDP of 100, minus net income paid abroad of 5, gives GNI of 95, minus capital consumption of 10 gives NNI of 85">${nDraw({ k: 5 })}</svg>`;
Lib.stepper($("#stN"), { w: 760, h: 290, label: "GDP to GNI to NNI", base: { k: 0 }, draw: nDraw, tween: 800, dwell: 5000, steps: [
  { cap: "<b>GDP</b> counts all final output produced inside the country: $100bn here.", s: { k: 1 } },
  { cap: "<b>Net primary income from abroad.</b> Residents earn $15bn overseas but foreign owners take $20bn out, a net <b>−$5bn</b>.", s: { k: 2 } },
  { cap: "<b>GNI = GDP + net primary income from abroad = $95bn.</b> This is the income of residents.", s: { k: 3 } },
  { cap: "<b>Capital consumption</b> of $10bn (wear and tear of machinery) is subtracted.", s: { k: 4 } },
  { cap: "<b>NNI = GNI − capital consumption = $85bn.</b> A net figure is always below the gross one.", s: { k: 5 } },
] });
const itemsB = [["GDP at market prices", 120, "t", 120, 0], ["Taxes on products", -15, "d", 120, 105], ["Subsidies on products", 5, "d", 110, 105], ["GDP at basic prices", 110, "t", 110, 0]];
function bDraw(s) { return wfDraw(itemsB, s); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="GDP at market prices of 120, less taxes on products of 15, plus subsidies of 5, gives GDP at basic prices of 110">${bDraw({ k: 4 })}</svg>`;
Lib.stepper($("#stP"), { w: 760, h: 290, label: "GDP from market prices to basic prices", base: { k: 0 }, draw: bDraw, tween: 800, dwell: 5000, steps: [
  { cap: "<b>Market prices</b> are what buyers pay, including sales taxes: $120bn.", s: { k: 1 } },
  { cap: "<b>Subtract taxes on products</b> ($15bn). Producers do not receive this money.", s: { k: 2 } },
  { cap: "<b>Add subsidies on products</b> ($5bn). Producers do receive this money.", s: { k: 3 } },
  { cap: "<b>GDP at basic prices = 120 − 15 + 5 = $110bn</b>, the amount producers actually receive.", s: { k: 4 } },
] });

/* ---------- Lab 1 ---------- */
function labN() {
  if (!["gd", "nt", "dp", "tx", "sb"].every((i) => $("#" + i))) return;
  const gdp = +$("#gd").value, net = +$("#nt").value, dep = +$("#dp").value, tx = +$("#tx").value, sb = +$("#sb").value, gni = gdp + net, nni = gni - dep, basic = gdp - tx + sb;
  $("#r1").textContent = "$" + gni + "bn"; $("#r2").textContent = "$" + nni + "bn"; $("#r3").textContent = "$" + basic + "bn";
  $("#rv").textContent = `GNI = ${gdp} ${net >= 0 ? "+" : "−"} ${Math.abs(net)} = ${gni}. NNI = ${gni} − ${dep} = ${nni}. GDP at basic prices = ${gdp} − ${tx} + ${sb} = ${basic}. ${net < 0 ? "Net primary income from abroad is negative, so GNI is below GDP." : net > 0 ? "Net primary income from abroad is positive, so GNI is above GDP." : "There is no net income from abroad, so GNI equals GDP."}`;
  const Y = (v) => 250 - v * 1.5, bars = [["GDP", gdp, "f1"], ["GNI", gni, "f2"], ["NNI", nni, "f3"], ["Basic", basic, "f1"]]; let o = SV.line(40, 250, 400, 250);
  bars.forEach(([l, v, c], i) => (o += SV.rect(60 + i * 85, Y(v), 60, 250 - Y(v), c, op(0.65)) + SV.text(90 + i * 85, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(90 + i * 85, Y(v) - 6, "$" + v, "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "gd", label: "GDP at market prices, $bn ", min: 80, max: 160, step: 5, value: 120, fmt: (v) => v, onInput: labN });
Lib.slider($("#g2"), { id: "nt", label: "Net primary income from abroad, $bn ", min: -20, max: 20, step: 1, value: -5, fmt: (v) => v, onInput: labN });
Lib.slider($("#g3"), { id: "dp", label: "Capital consumption (depreciation), $bn ", min: 0, max: 25, step: 1, value: 10, fmt: (v) => v, onInput: labN });
Lib.slider($("#g4"), { id: "tx", label: "Taxes on products, $bn ", min: 0, max: 30, step: 1, value: 15, fmt: (v) => v, onInput: labN });
Lib.slider($("#g5"), { id: "sb", label: "Subsidies on products, $bn ", min: 0, max: 20, step: 1, value: 5, fmt: (v) => v, onInput: labN });
labN();

/* ---------- Lab 2 ---------- */
const CTY = [["Host to foreign firms", 100, -12, "Foreign-owned factories send profits home, so more income leaves than arrives."], ["Many citizens working abroad", 100, 10, "Remittances and overseas earnings flow in, so GNI is above GDP."], ["Balanced flows", 100, 0, "Income received from abroad matches income paid abroad."]];
function showCty(i) {
  const [n, gdp, net, why] = CTY[i], gni = gdp + net; $$("#cB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = "$" + gdp + "bn"; $("#t2").textContent = (net > 0 ? "+" : "") + net; $("#t3").textContent = "$" + gni + "bn";
  $("#tv").textContent = `${n}: ${why} GNI = ${gdp} ${net >= 0 ? "+" : "−"} ${Math.abs(net)} = ${gni}.`;
  const Y = (v) => 170 - v * 1.2; $("#labB").innerHTML = SV.line(40, 170, 400, 170) + SV.rect(100, Y(gdp), 80, 170 - Y(gdp), "f1", op(0.65)) + SV.rect(240, Y(gni), 80, 170 - Y(gni), "f2", op(0.65)) + SV.text(140, 190, "GDP", "sm", { "text-anchor": "middle" }) + SV.text(280, 190, "GNI", "sm", { "text-anchor": "middle" }) + SV.text(140, Y(gdp) - 6, gdp, "lbl bd", { "text-anchor": "middle" }) + SV.text(280, Y(gni) - 6, gni, "lbl bd", { "text-anchor": "middle" });
}
$("#cB").innerHTML = CTY.map((c, i) => `<button class="b" data-i="${i}">${c[0]}</button>`).join("");
$$("#cB button").forEach((b) => (b.onclick = () => showCty(+b.dataset.i)));
showCty(0);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which measure is it?", buckets: [{"label": "GDP"}, {"label": "GNI"}, {"label": "NNI"}], items: [{"text": "Output produced inside the country's borders", "b": 0}, {"text": "Income of a country's residents wherever earned", "b": 1}, {"text": "GNI less capital consumption", "b": 2}, {"text": "GDP plus net primary income from abroad", "b": 1}, {"text": "Includes output of foreign-owned firms located here", "b": 0}, {"text": "The measure adjusted for depreciation of capital", "b": 2}, {"text": "Wages sent home by citizens working overseas are added", "b": 1}, {"text": "C + I + G + (X − M)", "b": 0}], done: "GDP: inside the borders. GNI: residents' income. NNI: GNI minus depreciation." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["GDP", "Value of output produced within a country in a year"], ["GNI", "GDP plus net primary income from abroad"], ["NNI", "GNI minus capital consumption"], ["Basic prices", "Market prices minus taxes on products plus subsidies"], ["Net primary income", "Income received from abroad less income paid abroad"], ["Capital consumption", "The value of capital worn out in a year"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps from GDP to NNI in order.", items: ["Start with GDP", "Add net primary income from abroad", "This gives GNI", "Subtract capital consumption", "This gives NNI"], done: "GDP + net income from abroad = GNI; GNI − depreciation = NNI." });
Lib.calc($("#c1"), { qs: [
  {"q": "GDP is $500bn, net primary income from abroad is −$30bn. What is GNI ($bn)?", "a": 470, "unit": "$bn", "tol": 0.5, "hint": "500 − 30.", "sol": "<b>$470bn</b>."},
  {"q": "Capital consumption is $45bn. What is NNI ($bn)?", "a": 425, "unit": "$bn", "tol": 0.5, "hint": "470 − 45.", "sol": "<b>$425bn</b>."},
  {"q": "GDP at market prices is $200bn, taxes on products $25bn and subsidies $10bn. What is GDP at basic prices ($bn)?", "a": 185, "unit": "$bn", "tol": 0.5, "hint": "200 − 25 + 10.", "sol": "<b>$185bn</b>."},
  {"q": "National income is $900bn and population is 30 million. What is national income per head ($)?", "a": 30000, "unit": "$", "tol": 50, "hint": "900,000m ÷ 30m.", "sol": "<b>$30,000</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "GNI equals:", opts: ["GDP plus net primary income from abroad", "GDP minus depreciation", "GDP plus taxes", "Exports minus imports"], a: 0, why: "Income of residents." },
  { q: "NNI is calculated by:", opts: ["Subtracting capital consumption from GNI", "Adding subsidies to GDP", "Adding net exports", "Subtracting taxes from GNI"], a: 0, why: "Net of depreciation." },
  { q: "GDP at basic prices is found by:", opts: ["Subtracting taxes on products and adding subsidies", "Adding taxes on products", "Subtracting depreciation", "Adding net income from abroad"], a: 0, why: "What producers receive." },
  { q: "A country whose firms are mostly foreign-owned is likely to have:", opts: ["GNI below GDP", "GNI above GDP", "NNI above GNI", "GDP of zero"], a: 0, why: "Profits flow out." },
  { q: "Which is a stock rather than a flow?", opts: ["Capital goods", "GDP", "NNI", "Consumption"], a: 0, why: "Output measures are flows; capital is a stock that depreciates." },
] });
Lib.cards($("#fc1"), { cards: [
  ["GDP", "Output inside the borders."],
  ["GNI", "GDP + net primary income."],
  ["NNI", "GNI − depreciation."],
  ["Net primary income", "Received − paid abroad."],
  ["Market prices", "Include product taxes."],
  ["Basic prices", "Market − taxes + subsidies."],
  ["Gross", "Before depreciation."],
  ["Net", "After depreciation."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The table shows selected information from a country's national accounts ($ billion): GDP 28, net property income from abroad −3, capital consumption 6, national debt 2. What is the country's net national income? (Feb/March 2023 · 12 · Q16, reworded)", opts: ["$19 billion", "$25 billion", "$31 billion", "$33 billion"], a: 0, why: "GNI = 28 − 3 = 25. NNI = 25 − 6 = 19. National debt is not part of the calculation." },
  { q: "The table gives details of national income statistics ($bn): consumption 2000, investment 500, government expenditure 600, net exports −100, net foreign factor income −200, depreciation 100. What is the net national income for this economy? (May/June 2023 · 13 · Q21, reworded)", opts: ["$2,700bn", "$2,800bn", "$2,900bn", "$3,000bn"], a: 0, why: "GDP = 2000 + 500 + 600 − 100 = 3000. GNI = 3000 − 200 = 2800. NNI = 2800 − 100 = 2700." },
  { q: "A country's net national income (NNI) is less than its gross national income (GNI). What does this mean? (May/June 2024 · 11 · Q16, reworded)", opts: ["incomes earned overseas were less than incomes sent overseas", "inflation has been accounted for in NNI but not in GNI", "the country's exports decreased", "there has been a net depreciation in the value of the country's fixed capital assets"], a: 3, why: "NNI is GNI minus capital consumption, so NNI is lower when capital has depreciated." },
  { q: "Which factor explains the difference between GDP and GNI? (May/June 2024 · 12 · Q19, reworded)", opts: ["foreign investment in the domestic automobile industry", "revenues received from exporting capital goods", "revenues received from exporting consumer goods", "salaries remitted by those working abroad to their home accounts"], a: 3, why: "GNI adds net primary income from abroad, such as wages sent home by residents working overseas. Exports are already in GDP." },
  { q: "The money income of a country rises by 10% whereas its population falls by 10% during a year. What is likely to happen to the national income per head? (Feb/March 2025 · 12 · Q19, reworded)", opts: ["It will remain unchanged", "It will rise by exactly 20%", "It will rise by less than 20%", "It will rise by more than 20%"], a: 3, why: "Income per head = 1.10 ÷ 0.90 = 1.222, a rise of about 22%, which is more than 20%." },
] });
