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

/* ---------- bath ---------- */
function bathDraw(s) {
  let o = SV.rect(260, 70, 240, 180, "f1", op(0.15)) + SV.line(260, 70, 260, 250) + SV.line(500, 70, 500, 250) + SV.line(260, 250, 500, 250);
  const h = Math.min(180, s.w * 1.8); o += SV.rect(261, 250 - h, 238, h, "f2", op(0.6));
  o += SV.text(380, 62, "Wealth (stock): the level of water", "lbl bd", { "text-anchor": "middle" });
  if (s.i > 0) o += SV.line(90, 100, 255, 100, "c2", { "stroke-width": 4, ...op(s.i) }) + SV.arrowHead(258, 100, "r", "dot2") + SV.text(90, 88, "Income (flow) per year", "lbl bd", { ...op(s.i) });
  if (s.o > 0) o += SV.line(505, 200, 690, 200, "c3", { "stroke-width": 4, ...op(s.o) }) + SV.arrowHead(692, 200, "r", "dot3") + SV.text(520, 188, "Spending (flow out)", "lbl bd", { ...op(s.o) });
  if (s.w > 0) o += SV.text(380, 280, "Saved income adds to wealth", "sm", { "text-anchor": "middle", ...op(s.w > 40 ? 1 : 0) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Income flows into a tank of wealth and spending flows out">${bathDraw({ w: 60, i: 1, o: 1 })}</svg>`;
Lib.stepper($("#stF"), { w: 760, h: 300, label: "Income as a flow into the stock of wealth", base: { w: 0, i: 0, o: 0 }, draw: bathDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Wealth is a stock.</b> It is the amount of assets owned at one moment, like the water level in a bath. It starts low.", s: { w: 10, i: 0, o: 0 } },
  { cap: "<b>Income is a flow.</b> Wages, rent and interest flow in over time, measured per week or per year.", s: { w: 10, i: 1, o: 0 } },
  { cap: "<b>Spending is a flow out.</b> What is not spent is saved and builds up as wealth.", s: { w: 40, i: 1, o: 1 } },
  { cap: "<b>The stock rises</b> when saving is positive. Households with high income can save more, which is why wealth is usually more unequal than income.", s: { w: 80, i: 1, o: 1 } },
] });

/* ---------- Lorenz ---------- */
const BASE = [4, 8, 12, 20, 56];
const shares = (w) => BASE.map((b) => (1 - w) * b + w * 20);
const cum = (sh) => { let c = 0; return [0, ...sh.map((v) => (c += v))]; };
const gini = (sh) => { const c = cum(sh); let a = 0; for (let i = 1; i < c.length; i++) a += ((c[i - 1] + c[i]) / 2) * 20; return 1 - a / 5000; };
function lorenz(x0, y0, w, h, sh, k = 1, showA = true) {
  const c = cum(sh), X = (p) => x0 + (p / 100) * w, Y = (v) => y0 - (v / 100) * h;
  let o = SV.line(x0, y0, x0 + w, y0) + SV.line(x0, y0, x0, y0 - h) + SV.text(x0 + w, y0 + 22, "Cumulative % of population", "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y0 - h - 6, "Cumulative % of income", "sm");
  o += SV.line(X(0), Y(0), X(100), Y(100), "dash") + SV.text(X(62), Y(66), "Line of equality", "sm");
  const pts = c.map((v, i) => [X(i * 20), Y(v)]);
  if (showA) o += SV.poly([[X(0), Y(0)], [X(100), Y(100)], ...pts.slice(1, 5).reverse()], "f3", op(0.4 * k));
  o += SV.path("M" + pts.map((p) => p.join(",")).join(" L"), "c2", { fill: "none", "stroke-width": 3, ...op(k) });
  pts.forEach((p) => (o += SV.circle(p[0], p[1], 4, "dot2", op(k))));
  return o;
}
function lzDraw(s) {
  let o = lorenz(120, 250, 300, 200, BASE, s.c, s.a > 0.5);
  if (s.a > 0.5) o += SV.text(440, 120, "A", "lbl bd", { ...halo }) + SV.text(440, 140, "area between the line", "sm") + SV.text(440, 156, "and the Lorenz curve", "sm");
  if (s.f > 0) { const g = gini(BASE); o += SV.text(440, 200, "Gini = A ÷ (A + B)", "lbl bd", op(s.f)) + SV.text(440, 222, "= " + Lib.fmtN(g, 2), "lbl bd", { style: "fill:var(--accent)", ...op(s.f) }); }
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A Lorenz curve below the line of equality with the area between them shaded">${lzDraw({ c: 1, a: 1, f: 1 })}</svg>`;
Lib.stepper($("#stL"), { w: 760, h: 300, label: "Building a Lorenz curve and reading the Gini coefficient", base: { c: 0, a: 0, f: 0 }, draw: lzDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The line of equality.</b> If every 20% of the population earned 20% of income, the Lorenz curve would be this diagonal line.", s: { c: 0, a: 0, f: 0 } },
  { cap: "<b>The Lorenz curve.</b> Here the poorest 20% earn 4% of income, the next 20% earn 8%, then 12%, 20% and the richest 20% earn 56%. The curve bows below the line.", s: { c: 1, a: 0, f: 0 } },
  { cap: "<b>The area A</b> between the line and the curve measures inequality. The bigger it is, the greater the inequality.", s: { c: 1, a: 1, f: 0 } },
  { cap: "<b>The Gini coefficient</b> is the area A as a share of the whole triangle under the line of equality (A + B). It runs from 0 to 1.", s: { c: 1, a: 1, f: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labL() {
  if (!$("#rd")) return;
  const w = +$("#rd").value / 100, sh = shares(w), g = gini(sh);
  $("#r1").textContent = Lib.fmtN(sh[0], 1) + "%"; $("#r2").textContent = Lib.fmtN(sh[4], 1) + "%"; $("#r3").textContent = Lib.fmtN(g, 2);
  $("#rv").textContent = w === 0 ? `Before redistribution the richest 20% receive ${Lib.fmtN(sh[4], 0)}% of income and the poorest 20% only ${Lib.fmtN(sh[0], 0)}%, a Gini of ${Lib.fmtN(g, 2)}.` : `After moving ${Lib.fmtN(w * 100, 0)}% of the way to equality, the poorest 20% have ${Lib.fmtN(sh[0], 1)}% and the richest 20% have ${Lib.fmtN(sh[4], 1)}%. The Lorenz curve moves towards the line of equality and the Gini falls to ${Lib.fmtN(g, 2)}.${w === 1 ? " At full equality the Gini is zero." : ""}`;
  $("#labA").innerHTML = lorenz(60, 250, 320, 210, sh, 1, true);
}
Lib.slider($("#g1"), { id: "rd", label: "How far income is moved towards equality, % ", min: 0, max: 100, step: 10, value: 0, fmt: (v) => v + "%", onInput: labL });
labL();

/* ---------- Lab 2 ---------- */
const CT = [["Sweden", 0.28], ["Germany", 0.31], ["United Kingdom", 0.35], ["United States", 0.41], ["Brazil", 0.53], ["South Africa", 0.63]];
function showC(i) {
  const [n, g] = CT[i]; $$("#cB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = n; $("#t2").textContent = g.toFixed(2); $("#t3").textContent = g < 0.3 ? "Fairly equal" : g < 0.4 ? "Moderate" : g < 0.5 ? "High" : "Very high";
  $("#tv").textContent = `${n} has a Gini coefficient of about ${g.toFixed(2)}. ${g < 0.35 ? "Income is spread comparatively evenly." : g < 0.5 ? "There is a sizeable gap between rich and poor." : "A large share of income goes to the richest households."} A Gini of 0 would mean perfect equality and 1 would mean one person receives everything.`;
  const X = (v) => 30 + v * 360; let o = SV.line(30, 110, 390, 110) + [0, 0.2, 0.4, 0.6, 0.8, 1].map((v) => SV.line(X(v), 104, X(v), 116) + SV.text(X(v), 134, v.toFixed(1), "sm", { "text-anchor": "middle" })).join("");
  CT.forEach(([m, v], k) => (o += SV.circle(X(v), 110, k === i ? 9 : 5, k === i ? "dot3" : "dot1", op(k === i ? 1 : 0.5))));
  o += SV.text(X(g), 88, n + " " + g.toFixed(2), "lbl bd", { "text-anchor": "middle", ...halo }) + SV.text(30, 170, "Equality (0)", "sm") + SV.text(390, 170, "Total inequality (1)", "sm", { "text-anchor": "end" });
  $("#labB").innerHTML = o;
}
$("#cB").innerHTML = CT.map((c, i) => `<button class="b" data-i="${i}">${c[0]}</button>`).join("");
$$("#cB button").forEach((b) => (b.onclick = () => showC(+b.dataset.i)));
showC(0);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is it income or wealth?", buckets: [{"label": "Income (flow)"}, {"label": "Wealth (stock)"}], items: [{"text": "A monthly salary", "b": 0}, {"text": "A house owned outright", "b": 1}, {"text": "Dividends paid on shares", "b": 0}, {"text": "Shares held in a company", "b": 1}, {"text": "Interest earned this year", "b": 0}, {"text": "Savings in a bank account", "b": 1}, {"text": "Rent received each month", "b": 0}, {"text": "A pension fund", "b": 1}], done: "Income is a flow over time. Wealth is a stock of assets at a point in time." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Lorenz curve", "Plots cumulative income share against cumulative population share"], ["Gini coefficient", "A measure of inequality from 0 to 1"], ["Gini of 0", "Perfect equality"], ["Gini of 1", "One person has all the income"], ["Wealth", "A stock of assets less debts"], ["Income", "A flow of earnings over a period"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of reading the Gini coefficient in order.", items: ["Plot the cumulative share of population against the cumulative share of income", "Draw the line of equality", "Find the area between the line and the Lorenz curve", "Divide it by the whole area under the line of equality", "Read the Gini coefficient between 0 and 1"], done: "Gini = area between the curves ÷ the area under the line of equality." });
Lib.calc($("#c1"), { qs: [
  {"q": "A person owns property worth $60,000, savings of $4,000, shares of $6,000 and has debts of $20,000. What is their wealth ($)?", "a": 50000, "unit": "$", "tol": 1, "hint": "Assets minus debts.", "sol": "70,000 − 20,000 = <b>$50,000</b>."},
  {"q": "A country's Gini coefficient falls from 0.52 to 0.44. By how many points has it fallen?", "a": 0.08, "unit": "", "tol": 0.005, "hint": "0.52 − 0.44.", "sol": "<b>0.08</b>."},
  {"q": "The richest 20% earn 56% of income. How many times the share of the poorest 20% (4%) is this?", "a": 14, "unit": "times", "tol": 0.2, "hint": "56 ÷ 4.", "sol": "<b>14 times</b>."},
  {"q": "A worker earns $2,000 a month and spends $1,800. By how much does the worker's wealth rise in a year if the saving is all kept ($)?", "a": 2400, "unit": "$", "tol": 1, "hint": "(2,000 − 1,800) × 12.", "sol": "<b>$2,400</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Income is best described as:", opts: ["A flow", "A stock", "An asset", "A debt"], a: 0, why: "It is measured per period." },
  { q: "A Gini coefficient close to 1 means:", opts: ["Great inequality", "Perfect equality", "Zero inflation", "Low unemployment"], a: 0, why: "One person has nearly everything." },
  { q: "A Lorenz curve bowing further from the line of equality shows:", opts: ["More inequality", "Less inequality", "No change", "A higher income"], a: 0, why: "A bigger area A." },
  { q: "Which is a stock?", opts: ["Savings in a bank", "Monthly wages", "Annual dividends", "Weekly rent"], a: 0, why: "Assets owned at a point in time." },
  { q: "Wealth is hard to measure partly because:", opts: ["Some is hidden or held overseas", "It is always in cash", "It is the same as income", "Governments record every asset"], a: 0, why: "Tax havens and transfers." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Income", "Flow per period."],
  ["Wealth", "Stock of assets less debts."],
  ["Lorenz curve", "Cumulative income against population."],
  ["Gini", "0 equality, 1 total inequality."],
  ["Cause", "Skills, assets, employment."],
  ["Benefit", "Incentives and enterprise."],
  ["Cost", "Wasted talent."],
  ["Measuring wealth", "Many forms, hidden, transferred."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The table shows Gini coefficients for income and wealth in two countries: country P income 0.6, wealth 0.4; country Q income 0.5, wealth 0.7. Which statement is correct? (Feb/March 2023 · 12 · Q14, reworded)", opts: ["Gini coefficients are not comparable between income and wealth because one is a flow concept and the other is a stock concept", "Income inequality is greater in country P than in country Q", "Wealth inequality is greater in country P than in country Q", "Wealth inequality is greater than income inequality in both countries"], a: 1, why: "A higher Gini means more inequality: income Gini is 0.6 in P and 0.5 in Q. Wealth inequality is greater in Q." },
  { q: "The table shows the Gini coefficient for income: Costa Rica 0.479, 0.478 and 0.497 (2018, 2019, 2020); New Zealand 0.330, 0.326 and 0.320; Sweden 0.275, 0.280 and 0.278. What can be concluded from this data? (Feb/March 2025 · 12 · Q15, reworded)", opts: ["All three countries have seen an overall improvement in income equality", "Costa Rica has the highest level of consumer income of all three countries", "New Zealand's income inequality worsened between 2018 and 2020", "Sweden's economy has the highest income equality of all three countries"], a: 3, why: "Sweden's Gini is lowest, so income is most equally distributed there. Costa Rica's Gini rose, and New Zealand's fell." },
  { q: "The table shows the income and wealth of Yasmin: children's welfare benefits $1,000, dividends from shares $1,000, property owned $40,000, savings in bank $1,000, shares $2,000, wages $10,000. What is the value of Yasmin's wealth? (May/June 2023 · 11 · Q16, reworded)", opts: ["$41,000", "$43,000", "$44,000", "$45,000"], a: 1, why: "Wealth is the stock of assets: property 40,000 + savings 1,000 + shares 2,000. Benefits, dividends and wages are income." },
  { q: "Which statement is a positive statement? (Feb/March 2021 · 12 · Q4, reworded)", opts: ["The distribution of income and wealth in most western European countries is unequal", "The government ought to increase income tax on high earners", "There should be more legal rights given to workers to protect their status in the workplace", "Wages of those on low incomes should be increased"], a: 0, why: "Only the first can be tested against facts. The others contain value judgements such as ought and should." },
] });
