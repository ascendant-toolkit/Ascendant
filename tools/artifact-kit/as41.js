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

$("#pic1").innerHTML = (() => {
  const B = [["Output", "Value added in every industry", 30, "f1"], ["Income", "Wages, rent, interest, profit", 270, "f2"], ["Expenditure", "C + I + G + (X − M)", 510, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 20, 220, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 55, n, "lbl bd", { "text-anchor": "middle", style: "font-size:18px" }) + SV.text(x + 110, 82, d, "sm", { "text-anchor": "middle" }); });
  o += SV.text(380, 142, "Same total: value of output = incomes earned = spending on final output", "sm", { "text-anchor": "middle" });
  return `<svg viewBox="0 0 760 160" role="img" aria-label="The output, income and expenditure methods give the same GDP">${o}</svg>`;
})();
chainStep("#stA", "Value added in a chain of production", ["Farmer grows wheat and sells it for $40: value added $40", "Miller buys wheat for $40, sells flour for $70: value added $30", "Baker buys flour for $70, sells bread for $120: value added $50", "Total value added: 40 + 30 + 50 = $120", "Only the final price ($120) is counted; adding all sales ($230) would double count"], [
  "<b>The first stage:</b> no intermediate inputs, so value added is the whole $40.", "<b>The mill</b> adds $30 to the $40 wheat.", "<b>The bakery</b> adds $50 to the $70 flour.", "<b>Sum of value added</b> equals the value of the final loaf.", "<b>Double counting</b> would overstate GDP by counting wheat and flour twice."]);
const itemsE = [["C", 600, "t", 600, 0], ["I", 150, "d", 750, 600], ["G", 200, "d", 950, 750], ["X", 180, "d", 1130, 950], ["M", -160, "d", 1130, 970], ["GDP", 970, "t", 970, 0]];
function eDraw(s) { return wfDraw(itemsE, s); }
Lib.stepper($("#stB"), { w: 760, h: 290, label: "GDP by the expenditure method", base: { k: 0 }, draw: eDraw, tween: 800, dwell: 4800, steps: [
  { cap: "<b>Consumption (C)</b> is household spending: $600bn.", s: { k: 1 } },
  { cap: "<b>Investment (I)</b> by firms in capital goods and stocks adds $150bn.", s: { k: 2 } },
  { cap: "<b>Government spending (G)</b> on goods and services adds $200bn.", s: { k: 3 } },
  { cap: "<b>Exports (X)</b> are spending by foreigners on domestic output: +$180bn.", s: { k: 4 } },
  { cap: "<b>Imports (M)</b> are spending on foreign output and are subtracted: −$160bn.", s: { k: 5 } },
  { cap: "<b>GDP = 600 + 150 + 200 + (180 − 160) = $970bn.</b>", s: { k: 6 } },
] });
chainStep("#stC", "The same total three ways", ["Firms produce $970bn of final output (output method: sum of value added)", "They pay out $970bn as wages, rent, interest and profit (income method)", "Households, firms, government and foreigners spend $970bn on it (expenditure method)", "Output = income = expenditure, so GDP can be measured from any side"], [
  "<b>Output</b> is produced by firms.", "<b>Income</b> is paid to the owners of factors of production.", "<b>Expenditure</b> is the total spent on the final output.", "<b>Circular flow of income:</b> all three describe the same flow."]);

/* ---------- Lab 1 ---------- */
function labE() {
  const ids = ["gc", "gi", "gg", "gx", "gm"];
  if (!ids.every((i) => $("#" + i))) return;
  const [c, i, g, x, m] = ids.map((k) => +$("#" + k).value), gdp = c + i + g + x - m;
  $("#r1").textContent = "$" + gdp + "bn"; $("#r2").textContent = (x - m >= 0 ? "+" : "") + (x - m); $("#r3").textContent = Lib.fmtN((c / gdp) * 100, 0) + "%";
  $("#rv").textContent = `GDP = ${c} + ${i} + ${g} + (${x} − ${m}) = ${gdp}. ${x - m >= 0 ? "Net exports are positive, a trade surplus that adds to GDP." : "Net exports are negative, a trade deficit that subtracts from GDP."} Consumption is ${Lib.fmtN((c / gdp) * 100, 0)}% of GDP.`;
  const mx = Math.max(gdp, c, 1), W = (v) => (Math.abs(v) / mx) * 250, row = (y, l, v, k) => SV.text(10, y + 15, l, "sm") + SV.rect(100, y, Math.max(2, W(v)), 22, k, op(0.7)) + SV.text(106 + W(v), y + 16, (v < 0 ? "−" : "") + Math.abs(v), "lbl bd");
  $("#labA").innerHTML = row(10, "C", c, "f1") + row(48, "I", i, "f2") + row(86, "G", g, "f3") + row(124, "X", x, "f1") + row(162, "M", -m, "f3") + row(210, "GDP", gdp, "f2");
}
[["g1", "gc", "Consumption (C), $bn ", 300, 900, 600], ["g2", "gi", "Investment (I), $bn ", 50, 300, 150], ["g3", "gg", "Government spending (G), $bn ", 50, 400, 200], ["g4", "gx", "Exports (X), $bn ", 50, 400, 180], ["g5", "gm", "Imports (M), $bn ", 50, 400, 160]].forEach(([el, id, lab, mn, mx, v]) => Lib.slider($("#" + el), { id, label: lab, min: mn, max: mx, step: 10, value: v, fmt: (z) => z, onInput: labE }));
labE();

/* ---------- Lab 2 ---------- */
function labR() {
  if (!["ng", "pi", "pp"].every((i) => $("#" + i))) return;
  const n = +$("#ng").value, pi = +$("#pi").value, pop = +$("#pp").value, real = (n / pi) * 100, ph = (real * 1000) / pop;
  $("#t1").textContent = "$" + Lib.fmtN(real, 1) + "bn"; $("#t2").textContent = "$" + Lib.fmtN(ph, 0); $("#t3").textContent = Lib.fmtN(n - real, 1) + "bn";
  $("#tv").textContent = `Real GDP = ${n} ÷ ${pi} × 100 = ${Lib.fmtN(real, 1)}. ${pi > 100 ? `Prices have risen, so nominal GDP overstates the growth in output by $${Lib.fmtN(n - real, 1)}bn.` : "Prices have not risen, so nominal and real GDP are the same."} Real GDP per head is $${Lib.fmtN(ph, 0)} for a population of ${pop} million.`;
  const mx = Math.max(n, real), W = (v) => (v / mx) * 280, bar = (y, l, v, k) => SV.text(10, y + 15, l, "sm") + SV.rect(110, y, W(v), 24, k, op(0.7)) + SV.text(116 + W(v), y + 17, Lib.fmtN(v, 0), "lbl bd");
  $("#labB").innerHTML = bar(40, "Nominal", n, "f3") + bar(100, "Real", real, "f1");
}
Lib.slider($("#g6"), { id: "ng", label: "Nominal GDP, $bn ", min: 200, max: 1000, step: 10, value: 550, fmt: (v) => v, onInput: labR });
Lib.slider($("#g7"), { id: "pi", label: "Price index (base year 100) ", min: 80, max: 160, step: 5, value: 110, fmt: (v) => v, onInput: labR });
Lib.slider($("#g8"), { id: "pp", label: "Population, millions ", min: 5, max: 100, step: 5, value: 25, fmt: (v) => v, onInput: labR });
labR();

/* ---------- Lab 3 ---------- */
chooser("h", [
  ["A new car sold to a household", "Yes", "Final good produced this year", "Consumption (C)"],
  ["Flour bought by a bakery", "No (on its own)", "Intermediate good: its value is in the price of the bread", "Not counted separately"],
  ["A firm buys a new machine", "Yes", "Capital good for production", "Investment (I)"],
  ["A government pays teachers and builds schools", "Yes", "Government spending on goods and services", "Government (G)"],
  ["A pension payment to a retired person", "No", "A transfer payment: not payment for current output", "Not counted"],
  ["A second-hand car sold between households", "No", "Not produced this year; the dealer's margin is counted", "Only the margin"],
  ["Housework done by a parent", "No", "Unpaid and not recorded", "Not counted"]
].map((r) => [r[0], r[1], r[2], r[3], r[1].startsWith("Yes") ? 5 : r[1].startsWith("No (on") ? 2 : 1]), (it) => `${it[0]}: ${it[1].toLowerCase()}. ${it[2]}. ${it[3] === "Not counted" || it[3].startsWith("Not") || it[3].startsWith("Only") ? "" : "Component: " + it[3] + "."}`, "Clarity of inclusion (5 = clearly counted)");
Lib.classify($("#cl1"), { prompt: "Which component of expenditure is it?", buckets: [{"label": "C"}, {"label": "I"}, {"label": "G"}, {"label": "X − M"}], items: [{"text": "Households buy food and clothing", "b": 0}, {"text": "A firm buys a new factory machine", "b": 1}, {"text": "The government pays for road building", "b": 2}, {"text": "Foreign customers buy the country's cars", "b": 3}, {"text": "Households buy imported phones", "b": 3}, {"text": "A firm adds to its stock of unsold goods", "b": 1}, {"text": "The government pays doctors' salaries", "b": 2}, {"text": "A household buys a holiday at home", "b": 0}], done: "C consumption, I investment, G government spending, X − M net exports (imports are subtracted)." });
Lib.classify($("#cl2"), { prompt: "Is it counted in GDP?", buckets: [{"label": "Counted"}, {"label": "Not counted"}], items: [{"text": "A new house built this year", "b": 0}, {"text": "Steel sold to a car maker (an intermediate good)", "b": 1}, {"text": "A haircut paid for in cash and recorded", "b": 0}, {"text": "Unpaid voluntary work", "b": 1}, {"text": "A pension payment (transfer)", "b": 1}, {"text": "A new school built by the government", "b": 0}, {"text": "The sale of a second-hand car (only the dealer's margin counts)", "b": 1}, {"text": "Output of a foreign-owned factory in the country", "b": 0}], done: "GDP counts final goods and services produced inside the borders this year; transfers, intermediate goods, unpaid work and second-hand sales (except margins) are excluded." });
Lib.order($("#o1"), { prompt: "Put the steps in order for measuring GDP by the expenditure method.", items: ["Measure consumption (C)", "Add investment (I)", "Add government spending (G)", "Add exports and subtract imports (X − M)", "The total is GDP"], done: "C + I + G + (X − M) = GDP." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["GDP", "Value of final output produced within a country in a year"], ["Value added", "Value of output minus the cost of intermediate goods"], ["Double counting", "Counting the same output more than once"], ["Real GDP", "GDP adjusted for inflation"], ["GDP per capita", "GDP divided by population"], ["Transfer payment", "Money paid without output in return, such as a pension"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "C = 700, I = 200, G = 250, X = 220, M = 190 ($bn). What is GDP ($bn)?", "a": 1180, "unit": "$bn", "tol": 0.5, "hint": "700 + 200 + 250 + 220 − 190.", "sol": "<b>$1180bn</b>."},
  {"q": "A farmer sells wheat for $30, a miller sells flour for $55 and a baker sells bread for $100. What is the value added by the baker ($)?", "a": 45, "unit": "$", "tol": 0.5, "hint": "100 − 55.", "sol": "<b>$45</b>."},
  {"q": "What is the total value added in the chain ($)?", "a": 100, "unit": "$", "tol": 0.5, "hint": "30 + 25 + 45.", "sol": "<b>$100</b>, equal to the final price."},
  {"q": "Nominal GDP is $660bn and the price index is 120. What is real GDP ($bn)?", "a": 550, "unit": "$bn", "tol": 0.5, "hint": "660 ÷ 1.20.", "sol": "<b>$550bn</b>."},
  {"q": "Real GDP is $550bn and the population is 11 million. What is real GDP per head ($)?", "a": 50000, "unit": "$", "tol": 50, "hint": "550,000m ÷ 11m.", "sol": "<b>$50,000</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "GDP measures:", opts: ["Final goods and services produced inside the country", "All sales including intermediate goods", "Wealth", "Output of the country's firms abroad only"], a: 0, why: "A flow of final output inside the borders." },
  { q: "Expenditure GDP is:", opts: ["C + I + G + (X − M)", "C + I + G − X + M", "C + S + T", "X − M"], a: 0, why: "The expenditure formula." },
  { q: "Counting the output of the miller and the baker in full would cause:", opts: ["Double counting", "Underestimation", "Deflation", "A transfer"], a: 0, why: "Intermediate goods counted twice." },
  { q: "Real GDP is calculated by:", opts: ["Adjusting nominal GDP for inflation", "Adding net exports", "Dividing by population", "Adding taxes"], a: 0, why: "Divide by the price index." },
  { q: "A limit of GDP as a welfare measure is:", opts: ["It ignores unpaid work and the informal economy", "It counts every activity", "It is adjusted for inequality", "It deducts pollution"], a: 0, why: "Many activities are not recorded." },
] });
Lib.cards($("#fc1"), { cards: [
  ["GDP", "Final output inside the borders."],
  ["Three methods", "Output, income, expenditure."],
  ["Expenditure", "C + I + G + (X − M)."],
  ["Value added", "Output minus intermediate inputs."],
  ["Double counting", "Counting intermediate goods too."],
  ["Real GDP", "Nominal ÷ price index × 100."],
  ["Per capita", "GDP ÷ population."],
  ["Limits", "Informal, unpaid, inequality, environment."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The money income of a country rises by 10% whereas its population falls by 10% during a year. What is likely to happen to the national income per head? (Feb/March 2025 · 12 · Q19, reworded)", opts: ["It will remain unchanged", "It will rise by exactly 20%", "It will rise by less than 20%", "It will rise by more than 20%"], a: 3, why: "Income per head = 1.10 ÷ 0.90 = 1.222, a rise of about 22%, which is more than 20%." },
  { q: "What is used to convert nominal GDP to real GDP? (May/June 2023 · 12 · Q20, reworded)", opts: ["exchange rates", "changes in the price level", "interest rates", "taxation"], a: 1, why: "A price index adjusts nominal values for inflation." },
  { q: "In year 1, a country's real GDP was $500 billion. In year 2, nominal GDP rose to $577.5 billion and the prices increased by 5%. What is the real GDP in year 2? (May/June 2023 · 13 · Q20, reworded)", opts: ["$4.76 billion", "$5 billion", "$476 billion", "$550 billion"], a: 3, why: "Real GDP = 577.5 ÷ 1.05 = 550." },
  { q: "The real national income of a country fell by 3%. What could have caused this? (May/June 2020 · 13 · Q25, reworded)", opts: ["Money national income fell by 3% when the rate of inflation was 6%.", "Money national income fell by 6% when the rate of inflation was 3%.", "Money national income rose by 3% when the rate of inflation was 6%.", "Money national income rose by 6% when the rate of inflation was 3%."], a: 2, why: "Real income falls by about 3% when money income rises 3% and prices rise 6%." },
] });
