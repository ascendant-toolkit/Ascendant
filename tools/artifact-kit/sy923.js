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

/* ---------- Learn picture and Watch 1: the cycle ---------- */
const CX = (t) => 70 + t * 660, TR = (t) => 250 - t * 70, WV = (t) => TR(t) - 70 * Math.sin(2 * Math.PI * 1.5 * t);
function cycPath(p) { const pts = []; for (let t = 0; t <= p + 1e-9; t += 0.01) pts.push([CX(t), WV(t)]); return Lib.ptsPath(pts); }
function cycDraw(s) {
  let o = axes(70, 330, 740, 40, "Time", "Real GDP") + SV.line(CX(0), TR(0), CX(1), TR(1), "c3 dash") + tag(CX(1) - 4, TR(1) + 22, "trend growth", "t3", 1, "end");
  o += SV.path(cycPath(s.p), "c1");
  const mk = [[1 / 6, "Boom (peak)", -22, 1], [1 / 3, "Downturn / recession", -34, 2], [0.5, "Trough (slump)", 28, 3], [2 / 3, "Recovery", 28, 4], [5 / 6, "Boom (peak)", -22, 5]];
  mk.forEach(([t, l, dy, k]) => { const v = Math.max(0, Math.min(1, (s.p - t) / 0.03 + 0.5)); if (v > 0 && s.p >= t - 0.001) o += SV.circle(CX(t), WV(t), 6, k % 2 ? "dot4" : "dot2", op(v)) + tag(CX(t), WV(t) + dy, l, k === 1 || k === 5 ? "t4" : k === 3 ? "t2" : "t1", v, "middle"); });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 360" role="img" aria-label="Business cycle: output rising and falling around a rising trend through boom, recession, trough and recovery">${cycDraw({ p: 1 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 360, label: "Business cycle drawn phase by phase around a rising trend line", base: { p: 0.01 }, draw: cycDraw, tween: 1400, dwell: 5600, steps: [
  { cap: "<b>Trend growth.</b> Potential output grows steadily over time (the dashed line). Actual output does not follow it exactly: it swings above and below, and that swing is the business cycle.", s: { p: 0.01 } },
  { cap: "<b>Boom.</b> Spending, investment and credit rise, output moves above trend (a positive output gap), unemployment is low and inflation rises.", s: { p: 0.17 } },
  { cap: "<b>Downturn and recession.</b> Confidence drops, firms cut investment and stocks, and growth slows then turns negative. If real GDP falls for two quarters or more, it is a <b>recession</b>.", s: { p: 0.34 } },
  { cap: "<b>Trough.</b> Output is at its lowest, well below trend (a negative gap). Unemployment is high, inflation is low and profits are poor.", s: { p: 0.5 } },
  { cap: "<b>Recovery.</b> Stocks are rebuilt and demand returns. Growth is positive again, the gap narrows, and unemployment falls slowly because firms hire late.", s: { p: 0.68 } },
  { cap: "<b>The next boom.</b> The cycle repeats, but never exactly. The length and size of each phase differ, which is why governments use policy and automatic stabilisers to smooth it.", s: { p: 0.84 } },
] });

/* ---------- Watch 2: automatic stabilisers ---------- */
function stabDraw(s) {
  const names = ["Income", "Tax paid", "Benefits received", "Disposable income"], base = 280, k = 7, xs = [110, 270, 430, 590];
  let o = SV.line(60, base, 740, base) + tag(60, 36, "Change in a household group's finances, $ per month", "t1");
  [s.a, s.b, s.c, s.d].forEach((v, i) => { const h = Math.abs(v) * k, y = v >= 0 ? base - h : base, cls = i === 3 ? "f3" : v >= 0 ? "f1" : "f2"; o += SV.rect(xs[i], y, 90, Math.max(h, 2), cls) + tag(xs[i] + 45, v >= 0 ? y - 8 : y + h + 16, (v > 0 ? "+" : "") + Lib.fmtN(v, 0), i === 3 ? "t3" : v >= 0 ? "t1" : "t2", 1, "middle") + SV.text(xs[i] + 45, base + 24, names[i], "sm bd", { "text-anchor": "middle" }); });
  if (s.n > 0) o += tag(400, 70, "Without stabilisers disposable income would fall by 10", "t2", s.n, "middle");
  if (s.m > 0) o += tag(400, 96, "The tax and benefit system cushions the fall", "t3", s.m, "middle");
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 330, label: "Bars showing income falling, tax paid falling, benefits rising and disposable income falling by less", base: { a: 0, b: 0, c: 0, d: 0, n: 0, m: 0 }, draw: stabDraw, tween: 900, dwell: 5200, steps: [
  { cap: "<b>The downturn hits.</b> Households' pre-tax income falls by 10 a month as firms cut hours and jobs.", s: { a: -10 } },
  { cap: "<b>Tax paid falls.</b> With a progressive income tax, the loss of income pushes people into lower tax bands, so tax paid falls by <b>more than proportionally</b>.", s: { a: -10, b: -3, n: 1 } },
  { cap: "<b>Benefits rise.</b> More people qualify for unemployment and means-tested benefits, so benefits received rise.", s: { a: -10, b: -3, c: 2, n: 1 } },
  { cap: "<b>Disposable income falls by less.</b> The fall is 10 − 3 (less tax) − 2 (more benefits) = 5, half of what it would have been. Households keep spending more than they otherwise would, so the recession is milder.", s: { a: -10, b: -3, c: 2, d: -5, n: 1, m: 1 } },
  { cap: "<b>The budget moves automatically.</b> Lower tax receipts and higher benefit payments push the government budget towards a <b>deficit</b> with no new law. In a boom the reverse happens and the budget moves towards surplus.", s: { a: -10, b: -3, c: 2, d: -5, n: 1, m: 1 } },
] });

/* ---------- Lab 1: stabilisers ---------- */
function labStab() {
  if (!$("#sh") || !$("#mp") || !$("#tx")) return;
  const S = +$("#sh").value, c = +$("#mp").value / 100, t = +$("#tx").value / 100, k0 = 1 / (1 - c), k1 = 1 / (1 - c * (1 - t)), f0 = S * k0, f1 = S * k1;
  $("#r1").textContent = Lib.fmtN(k0, 2); $("#r2").textContent = Lib.fmtN(k1, 2); $("#r3").textContent = "$" + Lib.fmtN(f0 - f1, 0) + "bn";
  $("#rv").textContent = `A $${S}bn fall in spending cuts national income by $${Lib.fmtN(f0, 0)}bn with no tax and $${Lib.fmtN(f1, 0)}bn with a ${Math.round(t * 100)}% tax rate. The tax system saves $${Lib.fmtN(f0 - f1, 0)}bn of lost output, which is why a more progressive system smooths the cycle.`;
  const mx = Math.max(f0, 1), y = (v) => 250 - v / mx * 200;
  let o = SV.line(40, 250, 400, 250) + SV.rect(90, y(f0), 90, 250 - y(f0), "f2") + SV.rect(240, y(f1), 90, 250 - y(f1), "f3") + tag(135, y(f0) - 6, "$" + Lib.fmtN(f0, 0) + "bn", "t2", 1, "middle") + tag(285, y(f1) - 6, "$" + Lib.fmtN(f1, 0) + "bn", "t3", 1, "middle") + SV.text(135, 272, "No tax", "sm bd", { "text-anchor": "middle" }) + SV.text(285, 272, "With tax rate", "sm bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sh", label: "Fall in spending ($bn) ", min: 10, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labStab });
Lib.slider($("#g2"), { id: "mp", label: "MPC (%) ", min: 50, max: 90, step: 5, value: 75, fmt: (v) => v, onInput: labStab });
Lib.slider($("#g3"), { id: "tx", label: "Average tax rate (%) ", min: 0, max: 50, step: 5, value: 20, fmt: (v) => v, onInput: labStab });
labStab();
btnTable("lbBtns", "lbOut", [
  ["Growth 4.5%, unemployment 3.8%, inflation rising", "Boom (peak)", "Above-trend growth, a positive output gap, tight labour market and rising prices"],
  ["Growth slowing to 0.3%, firms cutting orders", "Downturn", "Growth is still positive but falling fast; confidence and investment are dropping"],
  ["GDP down for two quarters, unemployment rising", "Recession", "Negative growth for two or more quarters, unemployment rising, inflation slowing"],
  ["Output at its lowest, unemployment 9%, inflation near zero", "Trough (slump)", "Lowest output, a large negative gap and heavy spare capacity"],
  ["Growth back to 2%, stocks rebuilt, unemployment still high", "Recovery", "Output rising again but unemployment lags behind and the gap is still negative"]
], ["Indicators", "Phase", "Why"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which phase of the cycle is each description of?", buckets: [{"label": "Boom"}, {"label": "Recession / trough"}, {"label": "Recovery"}], items: [{"text": "Unemployment at a record low and firms cannot find workers", "b": 0}, {"text": "Output falling for two quarters in a row", "b": 1}, {"text": "Growth returns but unemployment is still falling slowly", "b": 2}, {"text": "Inflation rising and the output gap positive", "b": 0}, {"text": "Firms running down stocks and cutting investment", "b": 1}, {"text": "Stocks being rebuilt and orders picking up", "b": 2}, {"text": "Output at its lowest, profits poor, large spare capacity", "b": 1}, {"text": "Housing prices and credit growing fast, confidence high", "b": 0}], done: "Match output, unemployment and mood to the phase." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Recession", "Falling real GDP for at least two consecutive quarters"], ["Trend growth", "The long-run average rate of growth of potential output"], ["Automatic stabiliser", "A tax or benefit that offsets the cycle without a new decision"], ["Discretionary policy", "A deliberate change in government spending or taxes"], ["Stock cycle", "Swings in output caused by firms building up and running down stocks"], ["Animal spirits", "Waves of optimism and pessimism that drive spending"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put a downturn in order, starting with the first event.", items: ["Consumer and business confidence falls", "Households cut spending and firms cut investment and stocks", "Firms produce less and cut jobs", "Unemployment rises and incomes fall further", "Tax revenue falls and benefits rise, so the deficit widens"], done: "The multiplier makes each round of lost income reduce spending again, until stabilisers and policy cushion the fall." });
Lib.calc($("#c1"), { qs: [
  {"q": "A closed economy has a marginal propensity to consume of 0.75 and an average tax rate of 20%. Calculate the multiplier. Use 1 ÷ (1 − MPC × (1 − t)).", "a": 2.5, "tol": 0.01, "hint": "MPC × (1 − t) = 0.75 × 0.8.", "sol": "0.75 × 0.8 = 0.6, so multiplier = 1 ÷ (1 − 0.6) = <b>2.5</b>."},
  {"q": "Using the multiplier in the previous question, by how much does national income fall (in $bn) if spending falls by $20bn?", "a": 50, "unit": "$bn", "tol": 0.01, "hint": "Change in income = multiplier × change in spending.", "sol": "2.5 × 20 = <b>$50bn</b>."},
  {"q": "Real GDP growth in four quarters is −0.3%, −0.8%, −0.5% and +0.4%. How many consecutive quarters of negative growth were there?", "a": 3, "tol": 0.01, "hint": "Count the run before growth turns positive.", "sol": "Quarters 1 to 3 were negative: <b>3</b>, so the economy was in recession."},
  {"q": "Potential GDP is $1,000bn and grows at 2.5% a year. After two years actual GDP is $1,020bn. Calculate the output gap as a percentage of potential GDP (use a minus sign if negative, one decimal place).", "a": -2.9, "tol": 0.1, "hint": "Potential after two years is 1000 × 1.025².", "sol": "Potential = 1000 × 1.050625 = 1050.6. Gap = (1020 − 1050.6) ÷ 1050.6 × 100 = <b>−2.9%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is most likely to be found at the trough of a business cycle?", opts: ["A positive output gap", "Rapidly rising inflation", "Spare capacity and high unemployment", "Labour shortages"], a: 2, why: "At the trough output is far below trend, so there is spare capacity and unemployment is high." },
  { q: "A recession is normally defined as:", opts: ["Any fall in the rate of inflation", "A fall in real GDP for two or more consecutive quarters", "A fall in the stock market", "Growth below 2% for a year"], a: 1, why: "A recession is a period of negative real growth, usually two quarters or more." },
  { q: "Which is an automatic stabiliser?", opts: ["A cut in interest rates by the central bank", "A new spending programme announced in a budget", "Unemployment benefits that rise as unemployment rises", "A fall in the exchange rate"], a: 2, why: "Benefits change without any new decision when unemployment changes." },
  { q: "What effect do automatic stabilisers have on the multiplier?", opts: ["They raise it", "They reduce it", "They have no effect", "They make it negative"], a: 1, why: "Taxes and benefits mean less of each extra dollar of income is spent, so the multiplier is lower." },
  { q: "Which would be a cause of the business cycle from the supply side?", opts: ["A fall in consumer confidence", "A sharp rise in oil prices", "A rise in the interest rate", "A stock cycle"], a: 1, why: "An oil price shock raises costs and cuts output. The others are demand-side causes." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Business cycle", "Fluctuations of actual output around the long-run trend."],
  ["Boom", "Phase with above-trend growth, low unemployment and rising inflation."],
  ["Recession", "Falling real GDP for two or more consecutive quarters."],
  ["Trough", "Lowest point of the cycle: spare capacity, high unemployment."],
  ["Recovery", "Growth returns and the output gap narrows; unemployment lags."],
  ["Automatic stabiliser", "Tax or benefit that cushions the cycle without any new decision."],
  ["Discretionary policy", "A deliberate change in G or T to influence demand."],
  ["Crowding out", "Government borrowing reducing private sector spending, usually via higher interest rates."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The table shows real GDP growth for three countries. What can be concluded? Brazil: 2014 +0.5%, 2015 −3.5%, 2016 −3.3%, 2017 +1.1%. Spain: 2012 −2.9%, 2013 −1.7%, 2014 +1.4%, 2015 +3.7%. (May/June 2022 · 31 · Q18, reworded)", opts: ["Brazil was in the downturn of its trade cycle in 2015", "Spain's real GDP was smallest in 2014", "Brazil experienced the best recovery of the period", "Spain was in the downturn of its trade cycle in 2014"], a: 0, why: "Brazil's growth turned sharply negative in 2015, so it was in the downturn. Spain's growth turned positive in 2014, which is a recovery." },
  { q: "Which would be the least likely consequence of a large rise in unemployment during a recession? (Oct/Nov 2022 · 32 · Q23, reworded)", opts: ["A fall in aggregate demand", "A fall in expenditure on welfare", "A fall in income tax revenue", "A fall in the rate of economic growth"], a: 1, why: "Welfare spending rises when more people are unemployed. The other three all follow from a downturn." },
  { q: "Higher government borrowing raises interest charges and reduces private investment. What is this an example of? (May/June 2023 · 32 · Q23, reworded)", opts: ["An automatic stabiliser", "Crowding out", "The accelerator", "The substitution effect"], a: 1, why: "Crowding out is when government borrowing reduces private sector spending, often through higher interest rates." },
  { q: "Which pair of tax and benefit systems produces automatic stabilisation? (May/June 2025 · 32 · Q17, reworded)", opts: ["A progressive income tax and means-tested benefits", "A progressive income tax and a universal flat-rate benefit", "A regressive income tax and means-tested benefits", "A regressive income tax and a universal benefit"], a: 0, why: "Progressive taxes and means-tested benefits respond most strongly to changes in income, so they move the budget against the cycle." },
  { q: "Which combination would be most likely to bring a country out of recession? (May/June 2024 · 32 · Q22, reworded)", opts: ["Expansionary fiscal and monetary policy together with supply-side policies", "Expansionary fiscal policy and tight monetary policy", "Tight fiscal and monetary policy", "Supply-side policy alone"], a: 0, why: "Demand needs a boost now (fiscal and monetary) and supply-side policies raise capacity for later. Supply-side alone is too slow." },
  { q: "An economy has a sudden rise in inflation from higher energy prices and also enters a recession with rising unemployment. A fall in which would most reduce the recession without pushing prices up further? (May/June 2024 · 31 · Q22, reworded)", opts: ["Direct taxation", "Government spending", "Indirect taxation", "The interest rate"], a: 2, why: "Cutting indirect taxes lowers prices directly while also raising real incomes. Cutting direct taxes, raising spending or cutting interest rates would add to demand-pull pressure." },
  { q: "What is the most likely result of a period of negative actual growth? (Oct/Nov 2024 · 33 · Q22, reworded)", opts: ["A rise in the surplus on the financial account", "A rise in the deficit on the current account", "A rise in the rate of inflation", "A rise in the rate of unemployment"], a: 3, why: "Falling output means firms cut jobs, so unemployment is likely to rise." },
  { q: "Why might a cut in the interest rate fail to boost aggregate demand in a recession? (Oct/Nov 2024 · 33 · Q18, reworded)", opts: ["Business confidence is low", "It causes deflation", "It raises the exchange rate", "It reduces the money supply"], a: 0, why: "If firms and households expect weak demand they may not borrow or spend even at low interest rates." },
] });
