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

/* ---------- Learn pictures ---------- */
function bars(items, base, k, w) {
  let o = SV.line(40, base, 720, base);
  items.forEach((it, i) => { const x = 70 + i * (w + 25), v = it.v, h = Math.abs(v) * k, y = v >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), it.c) + tag(x + w / 2, v >= 0 ? y - 8 : y + h + 16, it.t, it.cls, 1, "middle") + SV.text(x + w / 2, base + (v >= 0 ? 20 : -6), it.l, "sm", { "text-anchor": "middle" }); });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 250" role="img" aria-label="Components of aggregate demand: consumption, investment, government spending and net exports">${bars([
  { v: 60, c: "f1", t: "C", l: "Consumption", cls: "t1" }, { v: 18, c: "f4", t: "I", l: "Investment", cls: "t4" }, { v: 20, c: "f3", t: "G", l: "Government spending", cls: "t3" }, { v: 6, c: "f2", t: "X", l: "Exports", cls: "t2" }, { v: -7, c: "f2", t: "M", l: "Imports", cls: "t2" }], 190, 2.6, 100)}</svg>`;
$("#pic2").innerHTML = `<svg viewBox="0 0 760 270" role="img" aria-label="Net exports as exports minus imports">${SV.line(60, 220, 700, 220) + SV.rect(120, 90, 130, 130, "f3") + SV.rect(330, 120, 130, 100, "f2") + SV.rect(540, 190, 130, 30, "f1") + tag(185, 80, "Exports X", "t3", 1, "middle") + tag(395, 110, "Imports M", "t2", 1, "middle") + tag(605, 180, "Net exports X − M", "t1", 1, "middle") + tag(185, 245, "130", "t3", 1, "middle") + tag(395, 245, "100", "t2", 1, "middle") + tag(605, 245, "+30 (a surplus)", "t1", 1, "middle")}</svg>`;

/* ---------- Watch 1: net exports ---------- */
function neDraw(s) {
  const base = 250, k = 1.3, xs = [110, 270, 430, 590], X = 100 + s.x, M = 90 + s.m, N = X - M;
  const vals = [["Exports X", X, "f3", "t3"], ["Imports M", M, "f2", "t2"], ["Net exports", N, N >= 0 ? "f1" : "f2", N >= 0 ? "t1" : "t2"]];
  let o = SV.line(60, base, 600, base);
  vals.forEach(([l, v, c, t], i) => { const h = Math.abs(v) * k, y = v >= 0 ? base - h : base; o += SV.rect(xs[i] - 40, y, 80, Math.max(h, 2), c) + tag(xs[i], v >= 0 ? y - 8 : y + h + 16, Lib.fmtN(v, 0), t, 1, "middle") + SV.text(xs[i], base + 22, l, "sm", { "text-anchor": "middle" }); });
  if (s.n) o += tag(640, 60, s.n, "t4", 1, "middle");
  return o;
}
Lib.stepper($("#stN"), { w: 760, h: 300, label: "Exports, imports and net exports before and after a fall in the exchange rate and a rise in foreign income", base: { x: 0, m: 0 }, draw: neDraw, tween: 1000, dwell: 5400, steps: [
  { cap: "<b>Start.</b> Exports are 100, imports are 90, so net exports are +10, a small surplus.", s: { x: 0, m: 0 } },
  { cap: "<b>The exchange rate falls.</b> Exports are cheaper abroad, so foreign buyers purchase more: exports rise to 112. Imports are dearer, so households buy slightly fewer: imports fall to 86.", s: { x: 12, m: -4 } },
  { cap: "<b>Foreign income rises.</b> Customers abroad have more to spend, so exports rise further, to 120.", s: { x: 20, m: -4 } },
  { cap: "<b>Home income rises.</b> The economy grows, and part of the extra income is spent on imports (the marginal propensity to import), so imports rise to 98.", s: { x: 20, m: 8 } },
  { cap: "<b>Net exports are +22.</b> The fall in the exchange rate and the rise in foreign income raised X. Growth at home pulled in imports, which cut part of the gain. Net exports are a balance of both flows.", s: { x: 20, m: 8 } },
] });

/* ---------- Watch 2: government spending and the multiplier ---------- */
function gmDraw(s) {
  const base = 270, xs = [90, 220, 350, 480, 610], vals = [["G rises", 20, "f3"], ["Round 2", 12, "f1"], ["Round 3", 7.2, "f1"], ["Round 4", 4.3, "f1"], ["All later", 6.5, "f1"]];
  let o = SV.line(60, base, 720, base) + tag(60, 34, "Extra income created, $bn (G rises by 20, mpc and tax leave 0.6 spent)", "t1");
  vals.forEach(([l, v, c], i) => { const f = Math.max(0, Math.min(1, s.n - i)); if (f <= 0) return; const h = v * 9 * f; o += SV.rect(xs[i] - 40, base - h, 80, h, c, op(f)) + tag(xs[i], base - h - 8, Lib.fmtN(v, 1), "t1", f, "middle") + SV.text(xs[i], base + 20, l, "sm", { "text-anchor": "middle", ...op(f) }); });
  if (s.t) o += tag(400, 70, "Total rise in income = 20 + 12 + 7.2 + 4.3 + 6.5 = 50 = 20 × 2.5", "t3", 1, "middle");
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 310, label: "Rounds of extra spending after a rise in government spending of 20", base: { n: 0, t: 0 }, draw: gmDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>The government spends 20.</b> The firms and workers who receive it have 20 of extra income.", s: { n: 1 } },
  { cap: "<b>Round 2.</b> They spend 60% of the extra income (the rest is saved, taxed or spent on imports): 12 of new spending.", s: { n: 2 } },
  { cap: "<b>Round 3.</b> Those who receive the 12 spend 60% of it: 7.2.", s: { n: 3 } },
  { cap: "<b>Round 4.</b> And again: 4.3. Each round is smaller, because part leaks out.", s: { n: 4 } },
  { cap: "<b>The later rounds</b> add up to about 6.5.", s: { n: 5 } },
  { cap: "<b>The total.</b> Income rises by 50, which is 20 × 2.5. The multiplier is 1 ÷ (1 − 0.6). A larger share spent on imports or taxed would shrink it.", s: { n: 5, t: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labNe() {
  if (!$("#fx") || !$("#fi") || !$("#hi")) return;
  const fx = +$("#fx").value, fi = +$("#fi").value, hi = +$("#hi").value, X0 = 100, M0 = 90;
  const X = X0 * (1 + 0.8 * fx / 100 + 0.9 * fi / 100), M = M0 * (1 - 0.7 * fx / 100 + 0.8 * hi / 100), N = X - M, N0 = X0 - M0;
  $("#r1").textContent = Lib.fmtN(X, 1); $("#r2").textContent = Lib.fmtN(M, 1); $("#r3").textContent = (N >= 0 ? "+" : "−") + Lib.fmtN(Math.abs(N), 1);
  $("#rv").textContent = `Net exports change from +${N0} to ${N >= 0 ? "+" : "−"}${Lib.fmtN(Math.abs(N), 1)}. ` + (N > N0 ? "Net exports rise, which adds to aggregate demand." : N < N0 ? "Net exports fall, which reduces aggregate demand." : "Net exports are unchanged.");
  const base = 245, k = 1.2, vals = [[X0, "f3", 90, "X"], [X, "f3", 130, "X"], [M0, "f2", 220, "M"], [M, "f2", 260, "M"]];
  let o = SV.line(30, base, 400, base);
  vals.forEach(([v, c, x, l], i) => { const h = v * k; o += SV.rect(x - 14, base - h, 28, h, c, i % 2 ? {} : { opacity: 0.45 }) + tag(x, base - h - 6, Lib.fmtN(v, 0), i < 2 ? "t3" : "t2", 1, "middle"); });
  o += SV.text(110, 268, "Exports before and after", "sm", { "text-anchor": "middle" }) + SV.text(240, 268, "Imports before and after", "sm", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "fx", label: "Change in the exchange rate (% fall, negative is a rise) ", min: -10, max: 20, step: 2, value: 0, fmt: (v) => v, onInput: labNe });
Lib.slider($("#g2"), { id: "fi", label: "Rise in foreign income (%) ", min: 0, max: 10, step: 1, value: 0, fmt: (v) => v, onInput: labNe });
Lib.slider($("#g3"), { id: "hi", label: "Rise in home income (%) ", min: 0, max: 10, step: 1, value: 0, fmt: (v) => v, onInput: labNe });
labNe();
btnTable("lbBtns", "lbOut", [
  ["Exchange rate falls 10%", "Net exports rise (if elastic)", "Exports cheaper abroad, imports dearer at home; check the Marshall-Lerner condition."],
  ["Home inflation above trading partners'", "Net exports fall", "Exports are relatively dearer and imports relatively cheaper."],
  ["A recession abroad", "Net exports fall", "Foreign incomes fall, so demand for exports falls."],
  ["Productivity rises faster than rivals'", "Net exports rise", "Lower unit costs, so exports are more price competitive."],
  ["Home income grows quickly", "Net exports fall", "A share of the extra income is spent on imports (mpm)."]
], ["Change", "Effect on net exports", "Why"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Does each change raise or lower net exports?", buckets: [{"label": "Raises net exports"}, {"label": "Lowers net exports"}], items: [{"text": "A recession in the main export markets", "b": 1}, {"text": "A fall in the exchange rate (with elastic demand)", "b": 0}, {"text": "Higher productivity than competitors", "b": 0}, {"text": "Home inflation higher than that of trading partners", "b": 1}, {"text": "A boom in a trading partner's economy", "b": 0}, {"text": "Fast growth in home income that raises imports", "b": 1}, {"text": "Better quality and design of exports", "b": 0}, {"text": "A rise in the value of the currency", "b": 1}], done: "Think about price competitiveness and incomes at home and abroad." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Net exports", "Exports minus imports (X − M)"], ["Marginal propensity to import", "The change in imports divided by the change in income"], ["Average propensity to import", "Imports divided by income"], ["Price competitiveness", "How cheap a country's goods are relative to those of rivals"], ["Autonomous government spending", "Spending set by policy, not by the level of income"], ["Transfer payment", "A payment such as a benefit or pension where nothing is produced in exchange"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of a fall in the exchange rate in order, starting with the first event.", items: ["The exchange rate falls", "Exports become cheaper for foreign buyers and imports dearer for home buyers", "The volume of exports rises and the volume of imports falls", "Net exports rise, which raises aggregate demand", "National income rises by a multiple of the change in net exports"], done: "The effect depends on elasticities, spare capacity and the time lag." });
Lib.calc($("#c1"), { qs: [
  {"q": "A country exports $250bn and imports $210bn. Calculate net exports in $bn.", "a": 40, "unit": "$bn", "tol": 0.01, "hint": "X − M.", "sol": "250 − 210 = <b>+$40bn</b>."},
  {"q": "An economy has a national income of $3,200bn and imports of $630bn. Calculate the average propensity to import to two decimal places.", "a": 0.2, "tol": 0.01, "hint": "Imports ÷ income.", "sol": "630 ÷ 3200 = 0.197, so <b>0.20</b>."},
  {"q": "Income rises by $400bn and imports rise by $80bn. Calculate the marginal propensity to import.", "a": 0.2, "tol": 0.01, "hint": "Change in imports ÷ change in income.", "sol": "80 ÷ 400 = <b>0.2</b>."},
  {"q": "The government raises its spending by $30bn. The multiplier is 2.5. By how much does national income rise? Give the answer in $bn.", "a": 75, "unit": "$bn", "tol": 0.01, "hint": "Change in income = injection × multiplier.", "sol": "30 × 2.5 = <b>$75bn</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which would be most likely to reduce a country's net exports?", opts: ["A fall in the exchange rate", "Faster productivity growth than its rivals", "A higher rate of inflation than its trading partners", "A boom in its main export markets"], a: 2, why: "Higher relative inflation makes exports dearer and imports relatively cheaper." },
  { q: "Which is a determinant of government spending?", opts: ["The marginal propensity to consume", "The age structure of the population", "The exchange rate alone", "The profits of firms"], a: 1, why: "An older population raises spending on health and pensions." },
  { q: "What is the main effect of government spending on aggregate demand?", opts: ["It is a withdrawal", "It is an injection", "It has no effect", "It is a leakage"], a: 1, why: "G is an injection into the circular flow." },
  { q: "Why may a rise in home income reduce net exports?", opts: ["Imports are an injection", "Part of extra income is spent on imports", "Exports fall automatically", "The exchange rate rises automatically"], a: 1, why: "The marginal propensity to import means imports rise with income." },
  { q: "A fall in the exchange rate will increase net exports if:", opts: ["The sum of the price elasticities of demand for exports and imports is greater than one", "Demand for exports is perfectly inelastic", "Imports are essential goods with inelastic demand", "Foreign incomes fall"], a: 0, why: "This is the Marshall-Lerner condition." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Net exports", "Exports minus imports (X − M); a component of AD."],
  ["Price competitiveness", "Depends on relative productivity, relative inflation and the exchange rate."],
  ["Quality competitiveness", "Rises with net investment, training and innovation."],
  ["Marginal propensity to import", "Change in imports ÷ change in income."],
  ["Average propensity to import", "Imports ÷ income."],
  ["Government spending", "An injection set by policy, the cycle, the size of the state, population and shocks."],
  ["Marshall-Lerner condition", "A fall in the exchange rate improves the trade balance if the sum of the price elasticities of exports and imports exceeds one."],
  ["Capital vs current spending", "Capital spending raises productive capacity; current spending is used up in the year."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which change is most likely to increase a country's net exports? (Practice, not a past paper question)", opts: ["A rise in its inflation rate relative to its trading partners", "A rise in incomes in its main trading partners", "A rise in the value of its exchange rate", "A fall in its labour productivity"], a: 1, why: "Higher foreign incomes raise demand for exports. The other options make exports dearer or less competitive." },
  { q: "Which is most likely to lead to higher government spending as a share of GDP? (Practice, not a past paper question)", opts: ["A fall in the death rate leading to an older population", "A rise in net emigration of young workers", "A decision to privatise health services", "A fall in the unemployment rate"], a: 0, why: "An older population raises health and pension spending." },
  { q: "An economy's marginal propensity to import is 0.3. Income rises by $200bn. By how much do imports rise? (Practice, not a past paper question)", opts: ["$30bn", "$60bn", "$140bn", "$200bn"], a: 1, why: "Change in imports = mpm × change in income = 0.3 × 200 = $60bn." },
] });
