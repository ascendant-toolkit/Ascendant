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

/* ---------- Radar helpers ---------- */
const NAMES = ["Price stability", "Employment", "Growth", "Current account", "Sustainability", "Equity"];
const CX0 = 380, CY0 = 175, RR = 125;
const pt = (i, v) => { const a = -Math.PI / 2 + i * Math.PI / 3; return [CX0 + Math.cos(a) * RR * v / 10, CY0 + Math.sin(a) * RR * v / 10]; };
function radarPoly(vals, cls, v) { return SV.poly(vals.map((x, i) => pt(i, x)), cls, { opacity: v, stroke: "var(--ink)", "stroke-width": 2 }); }
function radarGrid() { let o = ""; [10, 7.5, 5, 2.5].forEach((l) => (o += `<polygon points="${[0, 1, 2, 3, 4, 5].map((i) => pt(i, l).join(",")).join(" ")}" fill="none" stroke="var(--line)" stroke-width="1"/>`)); NAMES.forEach((n, i) => { const p = pt(i, 10), q = pt(i, 11.8); o += SV.line(CX0, CY0, p[0], p[1], "gr") + SV.text(q[0], q[1] + 4, n, "lbl bd", { "text-anchor": i === 0 || i === 3 ? "middle" : i < 3 ? "start" : "end" }); }); return o; }
const A = [9, 8, 5, 6, 4, 3], B = [5, 4, 9, 3, 3, 5];
$("#pic1").innerHTML = `<svg viewBox="0 0 760 350" role="img" aria-label="Radar diagram with six macroeconomic objectives: price stability, employment, growth, current account, sustainability and equity">${radarGrid()}${radarPoly([10, 10, 10, 10, 10, 10], "f3", 0.15)}${tag(380, 340, "outer edge = objective fully met", "t3", 1, "middle")}</svg>`;
function radDraw(s) { let o = radarGrid() + radarPoly([10, 10, 10, 10, 10, 10], "f3", 0.12 * s.t); o += radarPoly(A.map((x) => x * s.a), "f1", 0.35 * s.a) + radarPoly(B.map((x) => x * s.b), "f4", 0.35 * s.b); if (s.a > 0) o += tag(40, 40, "Country A", "t1", s.a); if (s.b > 0) o += tag(40, 62, "Country B", "t4", s.b); return o; }
Lib.stepper($("#stR"), { w: 760, h: 350, label: "Radar chart comparing two economies against macroeconomic objectives", base: { t: 0, a: 0, b: 0 }, draw: radDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>The ideal.</b> Six objectives: price stability, employment, growth, the current account, sustainability and equity. The outer edge means the objective is fully met. No real economy fills the whole shape.", s: { t: 1 } },
  { cap: "<b>Country A.</b> Stable prices and high employment, but modest growth, a weak current account and poor scores on sustainability and equity. It is a mature, ageing economy.", s: { t: 1, a: 1 } },
  { cap: "<b>Country B.</b> Very fast growth, but higher inflation and unemployment, a large current account deficit and weaker sustainability. It is a fast-growing emerging economy.", s: { t: 1, a: 1, b: 1 } },
  { cap: "<b>Trade-offs.</b> Neither country meets every objective, and the shapes show different priorities. Pursuing one objective, such as growth, often costs another, such as the current account or sustainability.", s: { t: 1, a: 0.6, b: 1 } },
] });

/* ---------- Watch 2: inflation target ---------- */
const IQ = [1.8, 2.1, 2.6, 3.4, 4.5, 5.6, 5.9, 5.1, 4.0, 3.0, 2.3, 2.0], IX = (q) => 90 + q * 55, IY = (v) => 300 - v * 36;
function infDraw(s) {
  let o = axes(70, 300, 740, 30, "Quarter", "Inflation (%)") + SV.rect(70, IY(3), 660, IY(1) - IY(3), "f3", op(0.4)) + tag(726, IY(3) + 16, "target band 1% to 3%", "t3", 1, "end");
  [0, 2, 4, 6].forEach((v) => (o += SV.text(64, IY(v) + 4, v, "sm", { "text-anchor": "end" })));
  const n = Math.round(s.n), pts = IQ.slice(0, n).map((v, i) => [IX(i), IY(v)]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c2"); pts.forEach((p) => (o += SV.circle(p[0], p[1], 4, "dot2")));
  if (s.a > 0) o += tag(IX(5), IY(6.9), "inflation overshoots", "t2", s.a, "middle");
  if (s.b > 0) o += tag(IX(7.5), IY(5.9), "interest rates raised", "t1", s.b, "middle");
  if (s.c > 0) o += tag(IX(10.5), IY(3.6), "back in the band", "t3", s.c, "middle");
  return o;
}
Lib.stepper($("#stI"), { w: 760, h: 345, label: "Inflation rising above a target band and returning after policy tightening", base: { n: 1, a: 0, b: 0, c: 0 }, draw: infDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>On target.</b> Inflation is inside the 1% to 3% band. Price stability is met.", s: { n: 3 } },
  { cap: "<b>Overshoot.</b> Demand and costs push inflation up to almost 6%, far outside the band. Price stability is failing.", s: { n: 7, a: 1 } },
  { cap: "<b>Policy response.</b> The central bank raises interest rates to reduce demand. Inflation is slow to fall because of time lags, and growth and employment may suffer.", s: { n: 9, a: 1, b: 1 } },
  { cap: "<b>Back in the band.</b> Inflation returns to about 2%. The cost: slower growth and higher unemployment for a time, which shows how objectives conflict.", s: { n: 12, a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1: scorecard ---------- */
function labScore() {
  if (!$("#in") || !$("#un") || !$("#gr") || !$("#ca")) return;
  const inf = +$("#in").value / 10, un = +$("#un").value / 10, gr = +$("#gr").value / 10, ca = +$("#ca").value / 10;
  const rows = [["Inflation", inf, 1, 3, "price stability"], ["Unemployment", un, 0, 5, "low unemployment"], ["Growth", gr, 2, 4, "growth"], ["Current account", ca, -3, 3, "balance of payments"]];
  const ok = rows.map((r) => r[1] >= r[2] && r[1] <= r[3]), met = ok.filter(Boolean).length;
  const dist = rows.map((r) => (r[1] < r[2] ? r[2] - r[1] : r[1] > r[3] ? r[1] - r[3] : 0)), worst = dist.indexOf(Math.max(...dist));
  $("#r1").textContent = met + " of 4"; $("#r2").textContent = met === 4 ? "None" : rows[worst][0]; $("#r3").textContent = Lib.fmtN(inf + un, 1);
  $("#rv").textContent = met === 4 ? "All four indicators are inside their target ranges. This is the ideal, and it is rare." : `${met} of 4 objectives are met. The biggest miss is ${rows[worst][0].toLowerCase()} (${Lib.fmtN(rows[worst][1], 1)}${worst === 3 ? "% of GDP" : "%"}). Policy aimed at it may affect the other objectives: check for a conflict before choosing the tool.`;
  const X = (v, lo, hi) => 120 + (v - lo) / (hi - lo) * 260; let o = "";
  const ranges = [[-2, 10], [0, 16], [-6, 10], [-12, 8]];
  rows.forEach((r, i) => { const y = 40 + i * 62, [lo, hi] = ranges[i]; o += SV.line(120, y, 380, y, "gr") + SV.rect(X(r[2], lo, hi), y - 12, X(r[3], lo, hi) - X(r[2], lo, hi), 24, "f3", { opacity: 0.55 }) + SV.circle(X(Math.max(lo, Math.min(hi, r[1])), lo, hi), y, 8, ok[i] ? "dot3" : "dot2") + SV.text(10, y + 4, r[0], "lbl bd") + SV.text(400, y + 4, ok[i] ? "met" : "missed", "sm bd", { "text-anchor": "end" }); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "in", label: "Inflation (%) ", min: -10, max: 100, step: 5, value: 20, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labScore });
Lib.slider($("#g2"), { id: "un", label: "Unemployment (%) ", min: 20, max: 150, step: 5, value: 50, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labScore });
Lib.slider($("#g3"), { id: "gr", label: "Real GDP growth (%) ", min: -50, max: 80, step: 5, value: 25, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labScore });
Lib.slider($("#g4"), { id: "ca", label: "Current account (% GDP) ", min: -100, max: 60, step: 5, value: 0, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labScore });
labScore();
btnTable("lbBtns", "lbOut", [
  ["Deep recession, inflation near zero", "Unemployment and growth", "There is spare capacity and little inflation risk, so demand stimulus carries few costs."],
  ["Inflation at 9% with a positive output gap", "Price stability", "High inflation erodes savings and competitiveness, and tighter policy is needed even at some cost to growth."],
  ["Low-income country with widespread poverty", "Growth and development", "Raising incomes and living standards matters most, and GDP growth must reach poorer households."],
  ["Large persistent current account deficit and falling reserves", "Balance of payments", "Borrowing cannot continue indefinitely, so policy must improve competitiveness or cut spending on imports."],
  ["Rapid growth with severe pollution", "Sustainability", "Growth that destroys natural capital reduces future potential, so environmental policy takes priority."],
  ["Record inequality and rising poverty", "Redistribution", "Equity concerns and social stability call for tax and benefit policy and investment in skills."]
], ["Situation", "Likely priority", "Why"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which objective does the indicator mainly measure?", buckets: [{"label": "Price stability"}, {"label": "Employment"}, {"label": "Growth"}, {"label": "Balance of payments"}, {"label": "Distribution / development"}], items: [{"text": "Consumer price index", "b": 0}, {"text": "Claimant count and unemployment rate", "b": 1}, {"text": "Annual change in real GDP", "b": 2}, {"text": "Balance on trade in goods and services", "b": 3}, {"text": "Gini coefficient", "b": 4}, {"text": "Human Development Index", "b": 4}, {"text": "Core inflation rate", "b": 0}, {"text": "Participation rate and employment rate", "b": 1}], done: "Match each indicator to the objective it shows." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Price stability", "Low and stable inflation"], ["Full employment", "Everyone willing and able to work can find a job"], ["Current account stability", "No large persistent deficit or surplus"], ["Sustainability", "Growth that does not reduce future productive potential"], ["Redistribution", "A fairer spread of income and wealth through tax and benefits"], ["Misery index", "Inflation rate plus unemployment rate"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the policy-making cycle in order.", items: ["Identify the problem from the indicators", "Set a target for the objective", "Choose a tool: fiscal, monetary, supply-side, exchange rate or trade", "Implement the policy", "Monitor the results and adjust"], done: "Policy is a loop: results feed back into the next decision." });
Lib.calc($("#c1"), { qs: [
  {"q": "The consumer price index rises from 120 to 123.6 in a year. Calculate the inflation rate (%).", "a": 3, "unit": "%", "tol": 0.05, "hint": "Change ÷ original × 100.", "sol": "3.6 ÷ 120 × 100 = <b>3%</b>."},
  {"q": "Inflation is 4.5% and unemployment is 6.5%. Calculate the misery index.", "a": 11, "tol": 0.05, "hint": "Add the two rates.", "sol": "4.5 + 6.5 = <b>11</b>."},
  {"q": "A country's exports of goods and services are $180bn, imports are $200bn and GDP is $1,000bn. Calculate the balance on trade in goods and services as a percentage of GDP.", "a": -2, "unit": "%", "tol": 0.05, "hint": "(X − M) ÷ GDP.", "sol": "(180 − 200) ÷ 1000 × 100 = <b>−2%</b>, a deficit."},
  {"q": "Nominal GDP rises by 6% and inflation is 2.5%. Calculate the approximate rate of real growth (%).", "a": 3.5, "unit": "%", "tol": 0.05, "hint": "Nominal growth minus inflation.", "sol": "6 − 2.5 = <b>3.5%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is an indicator of price stability?", opts: ["The Gini coefficient", "The consumer price index", "The HDI", "The current account balance"], a: 1, why: "The CPI measures changes in the price level." },
  { q: "Why may sustainability conflict with short-run growth?", opts: ["Environmental policy may raise costs and reduce output in some industries", "It always raises unemployment", "It has no link to production", "It reduces inflation"], a: 0, why: "Pollution controls and carbon taxes raise costs, which can cut output in the short run." },
  { q: "Which objective is most likely to come first in a deep recession?", opts: ["Reducing inflation from 2%", "Reducing unemployment and raising growth", "Reducing the budget surplus", "Raising the exchange rate"], a: 1, why: "Spare capacity means demand policy has few costs." },
  { q: "Which objective is separate from growth?", opts: ["Economic development", "Real GDP", "Production", "National income"], a: 0, why: "Development covers health, education and living standards as well as income." },
  { q: "A government cuts taxes to raise growth and this increases imports. Which objective could be harmed?", opts: ["Current account balance", "The unemployment rate", "Population", "Resource base"], a: 0, why: "Higher incomes raise spending on imports and worsen the current account." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Price stability", "Low, stable inflation (target often 2%)."],
  ["Full employment", "Everyone willing and able can find a job at the going wage."],
  ["Economic growth", "Rise in real GDP over time."],
  ["Current account stability", "No large persistent deficit or surplus."],
  ["Economic development", "Improved living standards: income, health, education."],
  ["Sustainability", "Growth without reducing future potential."],
  ["Redistribution", "Tax and benefit changes to spread income more fairly."],
  ["Misery index", "Inflation rate plus unemployment rate."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which macroeconomic policy objective will not apply to a government in a closed economy? (Feb/March 2024 · 32 · Q21, reworded)", opts: ["A low and steady rate of inflation", "A more equal distribution of income", "A surplus on the balance of payments", "A sustainable rate of economic growth"], a: 2, why: "A closed economy has no trade with other countries, so there is no balance of payments." },
  { q: "Which government aim is least likely to be achieved using monetary policy? (Feb/March 2023 · 32 · Q22, reworded)", opts: ["Low unemployment", "A more equal income distribution", "A stable exchange rate", "Steady prices"], a: 1, why: "Monetary policy works through interest rates and the money supply. Changing the distribution of income needs tax and benefit policy." },
  { q: "When is a policy of redistributing income from rich to poor most appropriate? (Feb/March 2022 · 32 · Q15, reworded)", opts: ["When controlling demand-pull inflation is the priority", "When equality is valued more highly than efficiency", "When monetary reward is the best incentive to take risks", "When the rich have higher marginal utility curves"], a: 1, why: "Redistribution is justified when fairness is given more weight than the incentive effects on efficiency." },
  { q: "Governments set economic policy aims. What would be least likely to occur if all the aims were achieved? (Oct/Nov 2023 · 32 · Q24, reworded)", opts: ["A fall in the average standard of living", "A fall in the exchange rate", "A rise in frictional unemployment", "A rise in the rate of inflation"], a: 0, why: "If all aims, including growth, were achieved, living standards would not fall." },
  { q: "What is meant by sustainable economic growth? (May/June 2022 · 32 · Q18, reworded)", opts: ["Raising productive potential as fast as possible", "Raising productive potential using only low-cost resources", "Raising productive potential without reducing future potential", "Raising future potential as fast as possible"], a: 2, why: "Sustainable growth must not reduce what future generations can produce." },
  { q: "It is often argued that the HDI is a better indicator of development than income per head because it adjusts for: (Oct/Nov 2024 · 31 · Q27, reworded)", opts: ["Average hours worked", "Environmental pollution", "Inequality in income distribution", "Life expectancy at birth"], a: 3, why: "The HDI combines income with life expectancy and years of schooling." },
  { q: "What is the best description of sustainable economic development? (May/June 2025 · 34 · Q16, reworded)", opts: ["A long-term rise in actual output", "A long-term rise in living standards without damage to the environment", "A long-term rise in productive potential", "A long-term rise in living standards for every member of society"], a: 1, why: "Development includes living standards, and sustainable development means achieving this without harming the environment." },
  { q: "The Measure of Economic Welfare (MEW) is often seen as a better measure of welfare than GDP per head. What is additionally included in MEW? (May/June 2021 · 31 · Q20, reworded)", opts: ["The cost of paid work", "The cost of producing armaments", "An estimate of environmental damage", "The impact of the shadow economy"], a: 2, why: "MEW adjusts GDP for environmental costs and the value of unpaid work and leisure." },
] });
