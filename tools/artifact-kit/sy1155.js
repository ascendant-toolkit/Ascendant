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

/* ---------- Debt burden ---------- */
const DY = (v) => 300 - v * 2.4, DB = [["Start", 100, 15], ["Export prices fall", 70, 15], ["Interest rates rise", 70, 21], ["Currency falls 20%", 70, 26]];
function debtDraw(s) {
  let o = axes(70, 300, 730, 30, "", "$bn a year"); [0, 25, 50, 75, 100].forEach((v) => (o += SV.text(64, DY(v) + 4, v, "sm", { "text-anchor": "end" })));
  DB.forEach(([l, ex, ds], i) => { const k = Math.max(0, Math.min(1, s.n - i)); if (k <= 0) return; const x = 110 + i * 150; o += SV.rect(x, DY(ex * k), 50, ex * k * 2.4, "f1", op(0.75)) + SV.rect(x + 56, DY(ds * k), 50, ds * k * 2.4, "f2", op(0.75)) + tag(x + 25, DY(ex * k) - 6, ex, "t1", k, "middle") + tag(x + 81, DY(ds * k) - 6, ds, "t2", k, "middle") + tag(x + 53, 320, l, "sm", k, "middle") + tag(x + 53, DY(ex * k) - 24, "ratio " + Lib.fmtN(ds / ex * 100, 0) + "%", "t4", k, "middle"); });
  o += SV.rect(520, 330, 10, 10, "f1", op(0.75)) + SV.text(536, 339, "Export earnings", "sm") + SV.rect(640, 330, 10, 10, "f2", op(0.75)) + SV.text(656, 339, "Debt service", "sm");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 350" role="img" aria-label="Export earnings and debt service over four stages with the debt service ratio rising from 15 to 37 percent">${debtDraw({ n: 4 })}</svg>`;
Lib.stepper($("#stD"), { w: 760, h: 350, label: "Export earnings and debt service: the debt service ratio rises after shocks", base: { n: 0 }, draw: debtDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>Start.</b> Export earnings are $100bn and debt service (interest plus repayments) is $15bn: a debt service ratio of 15%.", s: { n: 1 } },
  { cap: "<b>Export prices fall.</b> A drop in the world price of the main export cuts earnings to $70bn. The debt service is unchanged, so the ratio rises to 21%.", s: { n: 2 } },
  { cap: "<b>Interest rates rise.</b> If part of the debt has variable interest, debt service rises to $21bn: a ratio of 30%.", s: { n: 3 } },
  { cap: "<b>The currency falls.</b> The debt is in dollars, so a 20% fall in the currency raises the debt service in local terms and the ratio climbs to 37%. Less is left for imports, health and education.", s: { n: 4 } },
] });

/* ---------- IMF loan flow ---------- */
function imfDraw(s) {
  const box = (x, y, w, h, t, c, k) => { if (k <= 0) return ""; const L = t.split("|"); return SV.rect(x, y, w, h, c, op(0.5 * k)) + L.map((ln, i) => SV.text(x + w / 2, y + h / 2 - (L.length - 1) * 8 + i * 16 + 5, ln, "lbl bd", { "text-anchor": "middle", ...op(k) })).join(""); };
  const ar = (x1, y1, x2, y2, d, k) => (k > 0 ? SV.line(x1, y1, x2, y2, "c1", { "stroke-width": 2.5, ...op(k) }) + SV.arrowHead(x2, y2, d, "dot1") : "");
  let o = box(20, 115, 130, 70, "Balance of|payments crisis", "f2", s.a);
  o += ar(150, 150, 190, 150, "r", s.b) + box(190, 115, 130, 70, "IMF short-term|loan", "f1", s.b);
  o += ar(320, 150, 360, 150, "r", s.c) + box(360, 95, 150, 110, "Conditions:|cut the deficit,|free trade, devalue", "f3", s.c);
  o += ar(510, 150, 550, 150, "r", s.d) + box(550, 40, 190, 80, "Benefits: confidence|and stability", "f1", s.d) + box(550, 180, 190, 80, "Costs: austerity,|inflation, unemployment", "f2", s.d);
  if (s.d > 0) o += ar(530, 130, 550, 85, "r", s.d) + ar(530, 170, 550, 215, "r", s.d);
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A balance of payments crisis, an IMF loan, conditions and the resulting benefits and costs">${imfDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stI"), { w: 760, h: 300, label: "From a balance of payments crisis to an IMF loan with conditions and their effects", base: { a: 0, b: 0, c: 0, d: 0 }, draw: imfDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>The crisis.</b> Foreign exchange reserves run low, the currency is under attack and lenders refuse to lend.", s: { a: 1 } },
  { cap: "<b>The IMF steps in</b> with a short-term loan so the country can pay for essential imports and meet its foreign debts.", s: { a: 1, b: 1 } },
  { cap: "<b>Conditions.</b> The loan comes with structural adjustment: cut the budget deficit, reduce import restrictions, privatise and often devalue the currency.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Effects.</b> Confidence and stability may return, but austerity can raise unemployment, and devaluation can raise import prices. The net effect depends on how severe the crisis was.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labD() {
  if (!$("#db") || !$("#ir") || !$("#rp") || !$("#ex")) return;
  const d = +$("#db").value, r = +$("#ir").value / 10, rep = +$("#rp").value, ex = +$("#ex").value, ds = d * r / 100 + rep, ratio = ds / ex * 100;
  $("#r1").textContent = "$" + Lib.fmtN(ds, 1) + "bn"; $("#r2").textContent = Lib.fmtN(ratio, 1) + "%"; $("#r3").textContent = "$" + Lib.fmtN(ex - ds, 1) + "bn";
  $("#rv").textContent = `Debt service = interest ($${Lib.fmtN(d * r / 100, 1)}bn) + repayments ($${rep}bn) = $${Lib.fmtN(ds, 1)}bn, which is ${Lib.fmtN(ratio, 1)}% of export earnings of $${ex}bn. ${ratio > 30 ? "This is a very heavy burden: little foreign exchange is left for imports, and the country is likely to need rescheduling or relief." : ratio > 20 ? "This ratio is high by many standards, so a fall in export earnings could create a crisis." : "This ratio looks manageable, though it would rise if exports fell or rates rose."}`;
  const Y = (v) => 270 - v * 1.1; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "$bn", "sm");
  [["Exports", ex, "f1"], ["Debt service", ds, "f2"], ["Left over", Math.max(0, ex - ds), "f3"]].forEach(([l, v, c], i) => { const x = 60 + i * 115, yy = Y(Math.min(v, 230)); o += SV.rect(x, yy, 80, 270 - yy, c) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, yy - 6, Lib.fmtN(v, 1), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "db", label: "External debt, $bn ", min: 20, max: 150, step: 5, value: 100, fmt: (v) => v, onInput: labD });
Lib.slider($("#g2"), { id: "ir", label: "Interest rate, % ", min: 10, max: 120, step: 5, value: 50, fmt: (v) => (v / 10).toFixed(1) + "%", onInput: labD });
Lib.slider($("#g3"), { id: "rp", label: "Repayments of principal, $bn a year ", min: 0, max: 30, step: 1, value: 10, fmt: (v) => v, onInput: labD });
Lib.slider($("#g3b"), { id: "ex", label: "Export earnings, $bn ", min: 30, max: 200, step: 5, value: 100, fmt: (v) => v, onInput: labD });
labD();

/* ---------- Lab 2 ---------- */
function labC() {
  if (!$("#cf")) return;
  const f = +$("#cf").value / 100, rate = 10 / (1 - f), debt = 10 * rate, ratio = debt / 50;
  $("#t1").textContent = Lib.fmtN(rate, 1) + " per $"; $("#t2").textContent = Lib.fmtN(debt, 0) + "bn"; $("#t3").textContent = Lib.fmtN(ratio, 2) + " times";
  $("#tv").textContent = f === 0 ? "At 10 local units per dollar, $10bn of debt is 100bn local units, twice annual government revenue of 50bn." : `A ${Lib.fmtN(f * 100, 0)}% fall in the currency takes the rate to ${Lib.fmtN(rate, 1)} units per dollar. The dollar debt of $10bn is now ${Lib.fmtN(debt, 0)}bn in local units, ${Lib.fmtN(ratio, 2)} times government revenue, even though the government has borrowed nothing more.`;
  const Y = (v) => 270 - v * 0.9; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "Local currency, bn", "sm");
  [["Revenue", 50, "f1"], ["Debt before", 100, "f1"], ["Debt after", debt, "f2"]].forEach(([l, v, c], i) => { const x = 60 + i * 115, yy = Y(Math.min(v, 270)); o += SV.rect(x, yy, 80, 270 - yy, c, op(i === 1 ? 0.5 : 0.85)) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, yy - 6, Lib.fmtN(v, 0), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "cf", label: "Fall in the currency against the dollar, % ", min: 0, max: 60, step: 5, value: 25, fmt: (v) => v + "%", onInput: labC });
labC();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "IMF or World Bank?", buckets: [{"label": "IMF"}, {"label": "World Bank"}], items: [{"text": "Short-term loan to a country short of foreign exchange", "b": 0}, {"text": "Long-term loan to build a road network", "b": 1}, {"text": "Promotes exchange rate stability", "b": 0}, {"text": "Loans and grants through the IBRD and IDA", "b": 1}, {"text": "Attaches conditions such as cutting the budget deficit", "b": 0}, {"text": "Funds schools, clinics and water supplies", "b": 1}, {"text": "Surveillance of members' economic policies", "b": 0}, {"text": "Aims mainly at reducing poverty and long-term development", "b": 1}], done: "IMF: monetary stability and balance of payments. World Bank: long-term development projects." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["External debt", "Money owed by residents of a country to foreign lenders"], ["Debt service ratio", "Interest plus repayments as a percentage of export earnings"], ["Conditionality", "Policy changes a lender requires in return for a loan"], ["Debt relief", "Cancelling or reducing a country's debt"], ["Structural adjustment", "Market-oriented reforms required by the IMF"], ["Moral hazard", "Debt relief may encourage irresponsible borrowing later"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the debt trap in order.", items: ["A country borrows in dollars", "Export prices fall or interest rates rise", "The currency falls, so the debt costs more in local currency", "More is spent on debt service and less on health and education", "Growth slows, making the debt harder to repay"], done: "A cycle: heavy debt, less investment, weaker growth, heavier debt." });
Lib.calc($("#c1"), { qs: [
  {"q": "Debt service is $8bn and export earnings are $40bn. Calculate the debt service ratio (%).", "a": 20, "unit": "%", "tol": 0.5, "hint": "8 ÷ 40.", "sol": "<b>20%</b>."},
  {"q": "A country owes $60bn and its GDP is $150bn. Calculate the debt-to-GDP ratio (%).", "a": 40, "unit": "%", "tol": 0.5, "hint": "60 ÷ 150.", "sol": "<b>40%</b>."},
  {"q": "A government owes $8bn. The exchange rate rises from 10 to 12.5 local units per dollar. By how much does the debt rise in local currency (bn units)?", "a": 20, "unit": "bn", "tol": 0.5, "hint": "8 × 12.5 − 8 × 10.", "sol": "100 − 80 = <b>20bn</b> local units."},
  {"q": "Interest on a $100bn debt at 5% is added to $10bn of repayments. Export earnings are $100bn. Calculate the debt service ratio (%).", "a": 15, "unit": "%", "tol": 0.5, "hint": "(5 + 10) ÷ 100.", "sol": "<b>15%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The debt service ratio is:", opts: ["Interest and repayments as a % of export earnings", "Debt as a % of GDP", "Exports as a % of imports", "Aid as a % of GNI"], a: 0, why: "It shows how much foreign exchange earnings are used to service debt." },
  { q: "The IMF mainly:", opts: ["Lends short term to countries with balance of payments problems", "Builds roads", "Sets tariffs", "Pays for schools"], a: 0, why: "It supports monetary stability and the balance of payments." },
  { q: "The World Bank mainly provides:", opts: ["Long-term loans and grants for development", "Short-term loans for currency crises only", "Exchange rate fixes", "Tax advice"], a: 0, why: "It focuses on development and poverty reduction." },
  { q: "Debt owed in dollars becomes more expensive in local currency when:", opts: ["The local currency falls", "The local currency rises", "Exports rise", "Inflation falls"], a: 0, why: "More local currency is needed to buy each dollar." },
  { q: "A possible cost of IMF conditions is:", opts: ["Austerity and higher unemployment", "Larger reserves", "No change in policy", "Cheaper imports in all cases"], a: 0, why: "Cutting the deficit can reduce demand." },
] });
Lib.cards($("#fc1"), { cards: [
  ["External debt", "Owed to foreign lenders."],
  ["Debt service ratio", "(Interest + repayments) ÷ exports."],
  ["IMF", "Short-term BoP help; monetary stability."],
  ["World Bank", "Long-term development loans and grants."],
  ["Conditionality", "Policy conditions on loans."],
  ["Structural adjustment", "Free-market reforms."],
  ["Debt relief", "Cancelling debt; moral hazard risk."],
  ["Debt trap", "Debt, weak growth, more debt."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which role is performed by the World Bank but not by the International Monetary Fund? (Feb/March 2025 · 32 · Q29, reworded)", opts: ["Facilitating free trade among member countries", "Helping member countries to plan fiscal policy", "Providing bailout packages to countries facing external account problems", "Providing money to member countries to build infrastructure"], a: 3, why: "The World Bank lends for long-term development projects. The IMF handles balance of payments support and monetary cooperation." },
  { q: "What is not a function of the International Monetary Fund? (May/June 2025 · 31 · Q28, reworded)", opts: ["Encouraging exchange rate stability", "Providing financial assistance to a country with failed economic policies", "Providing funds for a water purification plant in a developing country", "Providing loans to countries after a natural disaster"], a: 2, why: "Funding specific water projects is a development role of the World Bank." },
  { q: "What is the role of the International Monetary Fund? (Oct/Nov 2023 · 33 · Q28, reworded)", opts: ["To advise countries with trade disputes", "To help charities providing emergency aid", "To offer short-term help to countries with balance of payments problems", "To provide interest-free credit to developing countries for infrastructure"], a: 2, why: "The IMF supports countries with balance of payments difficulties in the short term." },
  { q: "Low-income countries that asked the IMF for loans usually had to introduce structural adjustment programmes promoting a free-market economy. Which action would be included? (Oct/Nov 2021 · 31 · Q23, reworded)", opts: ["Deregulation of agricultural markets", "Extending food subsidies", "Nationalising the water supply", "Restricting the flow of international capital"], a: 0, why: "Structural adjustment promoted markets, privatisation and deregulation, not subsidies, nationalisation or controls." },
  { q: "Which condition attached to IMF loans would conflict with the infant industry argument? (May/June 2025 · 32 · Q29, reworded)", opts: ["The need to allow free trade", "The need to control inflation", "A contractionary fiscal policy", "The need to privatise state firms"], a: 0, why: "The infant industry argument supports temporary protection, which free trade conditions would remove." },
  { q: "What are the characteristics of most developing economies? Ratio of government debt to GDP, and average propensity to save. (Oct/Nov 2021 · 31 · Q27, reworded)", opts: ["High debt ratio, high propensity to save", "High debt ratio, low propensity to save", "Low debt ratio, high propensity to save", "Low debt ratio, low propensity to save"], a: 1, why: "Developing countries often borrow heavily, and low incomes mean little saving." },
] });
