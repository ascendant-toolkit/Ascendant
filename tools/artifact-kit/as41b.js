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

function wfDraw(items, s) {
  const max = Math.max(...items.map((it) => it[3] || 0)) * 1.15, Y = (v) => 250 - (v / max) * 190, w = 600 / items.length; let o = SV.line(50, 250, 740, 250);
  items.forEach((it, i) => {
    const [lab, val, kind, top, bot] = it, x = 70 + i * (w + 8), v = Math.max(0, Math.min(1, s.k - i));
    if (v <= 0) return;
    o += SV.rect(x, Y(top), w - 20, Math.max(2, Y(bot) - Y(top)), kind === "t" ? "f1" : val < 0 ? "f3" : "f2", op(0.65 * v)) + SV.text(x + (w - 20) / 2, Y(top) - 8, (kind === "d" && val > 0 ? "+" : "") + Lib.fmtN(val, 0), "lbl bd", { "text-anchor": "middle", ...op(v) }) + SV.text(x + (w - 20) / 2, 270, lab, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return o;
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
function chooser(p, items, tmpl, lab = "Strength of the case") {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, lab + ": " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}

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
chainStep("#stF", "Why GNI can differ from GDP", ["Foreign-owned factories produce output inside the country", "Their output counts in GDP (inside the borders)", "Profits are sent to owners abroad (primary income paid abroad)", "Residents' income is lower than the output produced here", "GNI is below GDP"], [
  "<b>Foreign ownership</b> of firms located in the country.", "<b>GDP</b> counts the output wherever the owner lives.", "<b>The profits</b> leave the country.", "<b>Residents</b> receive less than the output value.", "<b>The reverse</b> happens when residents earn income abroad."]);

function labN() {
  if (!["gd", "rc", "pd", "dp"].every((i) => $("#" + i))) return;
  const gdp = +$("#gd").value, rc = +$("#rc").value, pd = +$("#pd").value, dep = +$("#dp").value, net = rc - pd, gni = gdp + net, nni = gni - dep;
  $("#r1").textContent = (net >= 0 ? "+" : "−") + "$" + Math.abs(net) + "bn"; $("#r2").textContent = "$" + gni + "bn"; $("#r3").textContent = "$" + nni + "bn";
  $("#rv").textContent = `Net primary income = ${rc} − ${pd} = ${net}. GNI = ${gdp} ${net >= 0 ? "+" : "−"} ${Math.abs(net)} = ${gni}. NNI = ${gni} − ${dep} = ${nni}. ${net < 0 ? "More income is paid abroad than received, so GNI is below GDP." : net > 0 ? "More income is received from abroad than paid, so GNI is above GDP." : "Income flows balance, so GNI equals GDP."}`;
  const Y = (v) => 250 - v * 1.5; let o = SV.line(40, 250, 400, 250);
  [["GDP", gdp, "f1"], ["GNI", gni, "f2"], ["NNI", nni, "f3"]].forEach(([l, v, c], i) => (o += SV.rect(70 + i * 110, Y(v), 80, 250 - Y(v), c, op(0.65)) + SV.text(110 + i * 110, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, Y(v) - 6, "$" + v, "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "gd", label: "GDP, $bn ", min: 80, max: 200, step: 5, value: 120, fmt: (v) => v, onInput: labN });
Lib.slider($("#g2"), { id: "rc", label: "Primary income received from abroad, $bn ", min: 0, max: 30, step: 1, value: 10, fmt: (v) => v, onInput: labN });
Lib.slider($("#g3"), { id: "pd", label: "Primary income paid abroad, $bn ", min: 0, max: 30, step: 1, value: 15, fmt: (v) => v, onInput: labN });
Lib.slider($("#g4"), { id: "dp", label: "Capital consumption, $bn ", min: 0, max: 25, step: 1, value: 10, fmt: (v) => v, onInput: labN });
labN();

chooser("h", [
  ["Host to foreign firms", "Negative", "GNI below GDP", "Foreign-owned factories send profits home", 4],
  ["Many citizens working abroad", "Positive", "GNI above GDP", "Wages and remittances flow in", 4],
  ["Large overseas investments", "Positive", "GNI above GDP", "Profits, interest and dividends flow in", 5],
  ["Heavy foreign borrowing", "Negative", "GNI below GDP", "Interest payments flow out", 3],
  ["Balanced flows", "About zero", "GNI equals GDP", "Income received matches income paid", 1]
], (it) => `${it[0]}: net primary income is ${it[1].toLowerCase()}, so ${it[2].toLowerCase()}. Reason: ${it[3].toLowerCase()}.`, "Size of the gap between GNI and GDP");
Lib.classify($("#cl1"), { prompt: "Which measure is it?", buckets: [{"label": "GDP"}, {"label": "GNI"}, {"label": "NNI"}], items: [{"text": "Output produced inside the country's borders", "b": 0}, {"text": "Income of a country's residents wherever earned", "b": 1}, {"text": "GNI less capital consumption", "b": 2}, {"text": "GDP plus net primary income from abroad", "b": 1}, {"text": "Includes output of foreign-owned firms located here", "b": 0}, {"text": "The measure adjusted for depreciation of capital", "b": 2}, {"text": "Wages sent home by citizens working overseas are added", "b": 1}, {"text": "C + I + G + (X − M)", "b": 0}], done: "GDP: inside the borders. GNI: residents' income. NNI: GNI minus depreciation." });
Lib.classify($("#cl2"), { prompt: "Is it primary income received from abroad or paid abroad?", buckets: [{"label": "Received from abroad"}, {"label": "Paid abroad"}], items: [{"text": "Dividends from shares a resident owns in a foreign firm", "b": 0}, {"text": "Profits sent home by a foreign-owned factory", "b": 1}, {"text": "Wages earned by a resident working overseas", "b": 0}, {"text": "Interest paid on a loan from a foreign bank", "b": 1}, {"text": "Wages paid to a foreign worker in the country", "b": 1}, {"text": "Interest on foreign bonds owned by a resident", "b": 0}], done: "Received: earned by residents abroad. Paid: earned by foreign owners and workers here." });
Lib.order($("#o1"), { prompt: "Put the steps from GDP to NNI in order.", items: ["Start with GDP", "Add primary income received from abroad", "Subtract primary income paid abroad", "This gives GNI", "Subtract capital consumption to get NNI"], done: "GDP + net primary income = GNI; GNI − depreciation = NNI." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["GNI", "GDP plus net primary income from abroad"], ["NNI", "GNI minus capital consumption"], ["Primary income", "Income from factors of production such as wages, profit and interest"], ["Net primary income", "Income received from abroad less income paid abroad"], ["Capital consumption", "The value of capital worn out in a year"], ["Gross", "Before deducting depreciation"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "GDP is $500bn, income received from abroad is $40bn and income paid abroad is $70bn. What is GNI ($bn)?", "a": 470, "unit": "$bn", "tol": 0.5, "hint": "500 + 40 − 70.", "sol": "<b>$470bn</b>."},
  {"q": "Capital consumption is $45bn. What is NNI ($bn)?", "a": 425, "unit": "$bn", "tol": 0.5, "hint": "470 − 45.", "sol": "<b>$425bn</b>."},
  {"q": "GDP is $30bn, net primary income from abroad −$3bn and capital consumption $6bn. What is NNI ($bn)?", "a": 21, "unit": "$bn", "tol": 0.5, "hint": "30 − 3 − 6.", "sol": "<b>$21bn</b>."},
  {"q": "GNI is $800bn and population is 20 million. What is GNI per head ($)?", "a": 40000, "unit": "$", "tol": 50, "hint": "800,000m ÷ 20m.", "sol": "<b>$40,000</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "GNI equals:", opts: ["GDP plus net primary income from abroad", "GDP minus depreciation", "GDP plus taxes", "Exports minus imports"], a: 0, why: "Income of residents." },
  { q: "NNI is calculated by:", opts: ["Subtracting capital consumption from GNI", "Adding subsidies to GDP", "Adding net exports", "Subtracting taxes from GNI"], a: 0, why: "Net of depreciation." },
  { q: "A country with mostly foreign-owned firms is likely to have:", opts: ["GNI below GDP", "GNI above GDP", "NNI above GNI", "GDP of zero"], a: 0, why: "Profits flow out." },
  { q: "Wages sent home by citizens working abroad:", opts: ["Raise GNI", "Lower GDP", "Are not income", "Raise depreciation"], a: 0, why: "Primary income from abroad." },
  { q: "Which is not needed to calculate NNI?", opts: ["National debt", "GDP", "Net primary income", "Capital consumption"], a: 0, why: "Debt is not part of the calculation." },
] });
Lib.cards($("#fc1"), { cards: [
  ["GNI", "GDP + net primary income."],
  ["NNI", "GNI − depreciation."],
  ["Primary income", "Wages, profit, interest."],
  ["Net primary income", "Received − paid abroad."],
  ["Capital consumption", "Wear and tear of capital."],
  ["Foreign ownership", "GNI below GDP."],
  ["Overseas earnings", "GNI above GDP."],
  ["NNI use", "Sustainable income."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The table shows selected information from a country's national accounts ($ billion): GDP 28, net property income from abroad −3, capital consumption 6, national debt 2. What is the country's net national income? (Feb/March 2023 · 12 · Q16, reworded)", opts: ["$19 billion", "$25 billion", "$31 billion", "$33 billion"], a: 0, why: "GNI = 28 − 3 = 25. NNI = 25 − 6 = 19. National debt is not part of the calculation." },
  { q: "The table gives details of national income statistics ($bn): consumption 2000, investment 500, government expenditure 600, net exports −100, net foreign factor income −200, depreciation 100. What is the net national income for this economy? (May/June 2023 · 13 · Q21, reworded)", opts: ["$2,700bn", "$2,800bn", "$2,900bn", "$3,000bn"], a: 0, why: "GDP = 2000 + 500 + 600 − 100 = 3000. GNI = 3000 − 200 = 2800. NNI = 2800 − 100 = 2700." },
  { q: "Which factor explains the difference between GDP and GNI? (May/June 2024 · 12 · Q19, reworded)", opts: ["foreign investment in the domestic automobile industry", "revenues received from exporting capital goods", "revenues received from exporting consumer goods", "salaries remitted by those working abroad to their home accounts"], a: 3, why: "GNI adds net primary income from abroad, such as wages sent home by residents working overseas. Exports are already in GDP." },
] });
