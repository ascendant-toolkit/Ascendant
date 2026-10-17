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

chainStep("#stA", "Expenditure-switching through a depreciation", ["The currency depreciates or is devalued", "Exports are cheaper abroad; imports are dearer at home", "Spending switches from imports to domestic goods", "Exports rise and imports fall", "The deficit narrows, if PEDx + PEDm is above one"], [
  "<b>A fall in the exchange rate</b> is the starting point.", "<b>Relative prices change.</b>", "<b>Spending switches</b> without cutting total demand.", "<b>Volumes adjust</b>, though slowly (the J-curve).", "<b>The Marshall-Lerner condition</b> must hold for the balance to improve."]);
chainStep("#stB", "Expenditure-reducing policy", ["The government raises taxes or cuts spending", "Disposable income and AD fall", "Households and firms buy fewer imports", "The current account deficit narrows", "Output and employment may fall, with lower inflation"], [
  "<b>Contractionary policy</b> is chosen to cut spending.", "<b>AD falls</b> through lower consumption and government spending.", "<b>Imports fall</b>, because they depend on income.", "<b>The deficit narrows.</b>", "<b>The cost:</b> slower growth and higher unemployment, though inflation may ease."]);

function labA() {
  if (!["g1v", "g2v"].every((i) => $("#" + i))) return;
  const dep = +$("#g1v").value, cut = +$("#g2v").value;
  const X = 200 * (1 + 0.007 * dep), M = 240 * (1 + dep / 100) * (1 - 0.007 * dep) * (1 - 0.012 * cut), def = M - X, out = -cut + 0.5 * dep;
  $("#r1").textContent = Lib.fmtN(def, 1); $("#r2").textContent = (out >= 0 ? "+" : "") + Lib.fmtN(out, 1) + "%";
  const mx = 300, W = (v) => (v / mx) * 300;
  $("#labA").innerHTML = SV.text(30, 24, "Exports", "sm") + SV.rect(100, 10, W(X), 22, "f1", op(0.7)) + SV.text(104 + W(X), 26, Lib.fmtN(X, 0), "lbl bd") + SV.text(30, 64, "Imports", "sm") + SV.rect(100, 50, W(M), 22, "f3", op(0.7)) + SV.text(104 + W(M), 66, Lib.fmtN(M, 0), "lbl bd") + SV.text(30, 120, "Deficit " + Lib.fmtN(def, 1), "lbl bd") + SV.rect(100, 130, Math.max(2, W(Math.max(def, 0))), 22, "f2", op(0.7)) + SV.text(30, 190, "Original deficit: 40", "sm");
  $("#rv").textContent = `With a depreciation of ${dep}% and a fall in AD of ${cut}%, exports are ${Lib.fmtN(X, 0)} and imports ${Lib.fmtN(M, 0)}, so the deficit is ${Lib.fmtN(def, 1)}. ` + (cut > 0 ? "The cut in AD reduces output (and may raise unemployment). " : "") + (dep > 0 ? "The depreciation raises import prices and may add to inflation. " : "") + "This is a simple illustration with assumed elasticities.";
}
Lib.slider($("#g1"), { id: "g1v", label: "Depreciation, % ", min: 0, max: 20, step: 2, value: 10, fmt: (v) => v + "%", onInput: labA });
Lib.slider($("#g2"), { id: "g2v", label: "Fall in AD from tax rises or spending cuts, % ", min: 0, max: 10, step: 1, value: 0, fmt: (v) => v + "%", onInput: labA });
labA();

chooser("h", [
  ["Depreciation or devaluation", "Cheaper exports, dearer imports", "Elasticities, J-curve, imported inflation", "Medium", 3],
  ["Tariffs and quotas", "Dearer or restricted imports", "Retaliation; inelastic demand", "Fast", 3],
  ["Export subsidies", "Lower export prices", "Cost to taxpayers; retaliation", "Fast", 2],
  ["Contractionary fiscal policy", "Lower income, so fewer imports", "Lower output and jobs", "Medium", 3],
  ["Higher interest rates", "Less spending; may attract funds", "May raise the currency and hurt exports", "Medium", 2],
  ["Supply-side policies", "Better quality and lower costs", "Slow, costly, uncertain", "Slow", 4]
], (it) => `${it[0]}: it works through ${it[1].toLowerCase()}. The main limit is ${it[2].toLowerCase()}. Speed: ${it[3].toLowerCase()}.`, "Long-run effectiveness");
Lib.classify($("#cl1"), { prompt: "Is it expenditure-switching or expenditure-reducing?", buckets: [{"label": "Expenditure-switching"}, {"label": "Expenditure-reducing"}], items: [{"text": "A tariff on imports", "b": 0}, {"text": "Higher income tax", "b": 1}, {"text": "A depreciation of the currency", "b": 0}, {"text": "A cut in government spending", "b": 1}, {"text": "Export subsidies", "b": 0}, {"text": "A rise in interest rates to cut spending", "b": 1}, {"text": "A quota on imports", "b": 0}, {"text": "A reduction in the money supply", "b": 1}], done: "Switching policies change relative prices; reducing policies cut total spending." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Expenditure-switching", "Moves spending from imports to domestic goods"], ["Expenditure-reducing", "Reduces total spending, including on imports"], ["Devaluation", "An official fall in a fixed exchange rate"], ["Supply-side policy", "Raises long-run competitiveness"], ["Retaliation", "A trading partner's response with its own barriers"], ["Marshall-Lerner condition", "PEDx + PEDm above one"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of expenditure-reducing policy in order.", items: ["The government raises taxes or cuts spending", "AD falls", "Imports fall", "The deficit narrows", "Output and employment may fall"], done: "Cut spending, lower imports, narrower deficit, but lower output." });
Lib.calc($("#c1"), { qs: [
  {"q": "A deficit of $40bn falls by 25% after a policy. What is the new deficit ($bn)?", "a": 30, "unit": "$bn", "tol": 0.5, "hint": "40 × 0.75.", "sol": "<b>$30bn</b>."},
  {"q": "Imports are $240bn and the income elasticity of demand for imports is 1.2. AD falls 5%. What is the % fall in imports?", "a": 6, "unit": "%", "tol": 0.1, "hint": "1.2 × 5.", "sol": "<b>6%</b>."},
  {"q": "What is the fall in imports in $bn?", "a": 14.4, "unit": "$bn", "tol": 0.1, "hint": "0.06 × 240.", "sol": "<b>$14.4bn</b>."},
  {"q": "A 10% tariff is charged on $200bn of imports. What is the tariff revenue ($bn), if imports do not change?", "a": 20, "unit": "$bn", "tol": 0.5, "hint": "0.10 × 200.", "sol": "<b>$20bn</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An expenditure-switching policy is:", opts: ["A tariff", "Higher income tax", "A cut in government spending", "Higher interest rates"], a: 0, why: "Changes relative prices." },
  { q: "An expenditure-reducing policy is:", opts: ["Higher income tax", "A tariff", "An export subsidy", "A depreciation"], a: 0, why: "Cuts spending." },
  { q: "A limit of tariffs is:", opts: ["Retaliation", "Lower prices", "More imports", "No effect on prices"], a: 0, why: "Trading partners may respond." },
  { q: "Supply-side policy mainly affects the deficit:", opts: ["Slowly, in the long run", "Immediately", "Not at all", "Only in the short run"], a: 0, why: "Productivity takes time." },
  { q: "A cost of expenditure-reducing policy is:", opts: ["Lower output and employment", "Higher imports", "Higher AD", "Retaliation"], a: 0, why: "Spending falls across the economy." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Switching", "Imports to domestic goods."],
  ["Reducing", "Cut total spending."],
  ["Depreciation", "Switching via the exchange rate."],
  ["Tariff", "Switching via import prices."],
  ["Contractionary policy", "Reducing; costs output."],
  ["Supply-side", "Slow, but tackles the cause."],
  ["Limits", "Retaliation, elasticity, output."],
  ["Judge", "Cause, speed, side effects."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is an expenditure-switching policy to reduce a country's balance of payments deficit? (May/June 2020 · 11 · Q25, reworded)", opts: ["an increase in budget surplus", "an increase in direct taxes", "an increase in import tariffs", "an increase in interest rates"], a: 2, why: "Tariffs switch spending from imports to domestic goods." },
  { q: "Which policy aimed at correcting a balance of trade deficit is an expenditure-reducing policy? (May/June 2021 · 12 · Q29, reworded)", opts: ["depreciation of the currency", "increased direct taxation", "tax incentives for exporters", "the imposition of protectionist tariffs"], a: 1, why: "Higher direct taxes reduce disposable income, spending and imports." },
  { q: "Which policy measure is an expenditure-switching measure designed to reduce a current account surplus? (May/June 2020 · 13 · Q30, reworded)", opts: ["a cut in income tax rates", "a depreciation of the exchange rate", "the removal of limits on bank lending", "the removal of subsidies to exporters"], a: 3, why: "Removing export subsidies raises export prices, switching spending away from exports." },
  { q: "A country has a deficit on the current account of its balance of payments. What might help the country to reduce its deficit? (Feb/March 2021 · 12 · Q23, reworded)", opts: ["a decrease in its rate of income tax", "a decrease in its tariffs", "an increase in its level of employment", "an increase in its subsidies to exporters"], a: 3, why: "Export subsidies lower export prices and may raise exports." },
  { q: "The government of a country is worried about a large deficit on the current account of its balance of payments and an increasing rate of inflation. The country has a fixed exchange rate for its currency. Which policy measure is most likely to help the government to reduce the current account deficit and lower the rate of inflation? (May/June 2022 · 11 · Q30, reworded)", opts: ["devaluation of the currency", "increasing government spending", "decreasing the direct taxes", "increasing the interest rate"], a: 3, why: "A higher interest rate reduces spending and inflation, and cuts imports." },
  { q: "A country with low unemployment and a managed floating exchange rate has a persistent current account deficit on its balance of payments. Which policy to reduce this deficit is most likely to keep unemployment low, but cause inflation? (May/June 2022 · 12 · Q30, reworded)", opts: ["depreciating its currency", "higher direct taxation", "higher import tariffs", "higher interest rates"], a: 0, why: "A depreciation raises net exports and AD, keeping employment high, but raises import prices and so inflation." },
  { q: "A government raises interest rates to improve the current account of the balance of payments. What might reduce the effectiveness of this policy? (Feb/March 2023 · 12 · Q30, reworded)", opts: ["a fall in domestic growth", "consumer pessimism", "increased domestic saving", "price-elastic demand for exports"], a: 3, why: "Higher rates may raise the exchange rate, and if demand for exports is elastic, export revenue falls sharply." },
] });
