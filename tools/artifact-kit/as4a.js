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

/* ---------- CPI build ---------- */
const CPI = [["Food", 30, 10, "f3"], ["Housing", 25, 4, "f1"], ["Transport", 15, 8, "f2"], ["Clothing", 10, 2, "f1"], ["Other", 20, 3, "f2"]];
function cpDraw(s) {
  const Y = (v) => 250 - v * 28; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "Contribution to inflation (% points)", "sm");
  let y = 250;
  CPI.forEach(([n, w, ch, c], i) => { const v = Math.max(0, Math.min(1, s.k - i)), h = (w * ch / 100) * 28 * v; if (v > 0) o += SV.text(110 + i * 110, 270, n + " (weight " + w + "%)", "sm", { "text-anchor": "middle", ...op(v) }) + SV.rect(80 + i * 110, 250 - (w * ch / 100) * 28 * v, 60, (w * ch / 100) * 28 * v, c, op(0.7)) + SV.text(110 + i * 110, 244 - (w * ch / 100) * 28 * v, "+" + Lib.fmtN(w * ch / 100, 1) + "  (" + ch + "% × " + w + "%)", "sm", { "text-anchor": "middle", ...op(v) }); });
  if (s.k >= 5.5) o += tag(380, 70, "Inflation = 3.0 + 1.0 + 1.2 + 0.2 + 0.6 = 6.0%", "c3", Math.min(1, s.k - 5), "middle");
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Weighted contributions of five categories to inflation of 6 percent">${cpDraw({ k: 6 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 290, label: "Building the CPI from weights and price changes", base: { k: 0 }, draw: cpDraw, tween: 900, dwell: 5000, steps: [
  { cap: "<b>Food</b> is 30% of household spending. Food prices rose 10%, so food adds 10% × 30% = 3.0 percentage points to inflation.", s: { k: 1 } },
  { cap: "<b>Housing</b> (25%) rose 4%: contribution 1.0.", s: { k: 2 } },
  { cap: "<b>Transport</b> (15%) rose 8%: contribution 1.2.", s: { k: 3 } },
  { cap: "<b>Clothing</b> (10%) rose 2%: 0.2.", s: { k: 4 } },
  { cap: "<b>Other goods and services</b> (20%) rose 3%: 0.6.", s: { k: 5 } },
  { cap: "<b>Total inflation</b> = the sum of the weighted contributions = 6.0%. Food has the biggest effect because of its weight and its large price rise.", s: { k: 6 } },
] });

/* ---------- inflation, disinflation, deflation ---------- */
const IR = [4, 4, 3, 1.5, -1, -2], CP = [100]; IR.forEach((r) => CP.push(CP[CP.length - 1] * (1 + r / 100)));
function dfDraw(s) {
  const n = Math.round(s.t); let o = SV.line(60, 120, 700, 120) + SV.line(60, 120, 60, 20) + SV.text(66, 14, "CPI (price level)", "sm") + SV.line(60, 270, 700, 270) + SV.line(60, 190, 60, 270) + SV.text(66, 186, "Inflation rate (%)", "sm") + SV.line(60, 230, 700, 230, "dash");
  let d = ""; CP.forEach((v, i) => { if (i <= n) { const x = 100 + i * 90, y = 120 - (v - 95) * 3; d += (i ? " L" : "M") + x + "," + y; o += SV.circle(x, y, 4, "dot2") + SV.text(x, y - 10, Lib.fmtN(v, 0), "sm", { "text-anchor": "middle" }); } });
  if (d) o += SV.path(d, "c2", { fill: "none", "stroke-width": 3 });
  IR.forEach((r, i) => { if (i + 1 <= n) { const x = 145 + i * 90, h = r * 8; o += SV.rect(x - 14, r >= 0 ? 230 - h : 230, 28, Math.abs(h), r >= 0 ? "f2" : "f3", op(0.7)) + SV.text(x, r >= 0 ? 224 - h : 244 - h, (r > 0 ? "+" : "") + r + "%", "sm", { "text-anchor": "middle" }) + SV.text(x, 285, "Yr " + (i + 1), "sm", { "text-anchor": "middle" }); } });
  const lab = n >= 6 ? "Deflation: prices fall (negative inflation)" : n >= 4 ? "Disinflation: prices still rise but more slowly" : n >= 1 ? "Inflation: prices rise" : ""; if (lab) o += SV.text(380, 40, lab, "lbl bd", { "text-anchor": "middle", style: "fill:var(--accent)" });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 295" role="img" aria-label="A price index rising, rising more slowly and then falling, with the inflation rate below">${dfDraw({ t: 6 })}</svg>`;
Lib.stepper($("#stD"), { w: 760, h: 295, label: "Inflation, disinflation and deflation over six years", base: { t: 0 }, draw: dfDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Start.</b> The price index is 100 and the inflation rate is plotted below.", s: { t: 0 } },
  { cap: "<b>Inflation.</b> Prices rise 4% a year for two years: the price level rises and the inflation rate is positive.", s: { t: 2 } },
  { cap: "<b>Disinflation.</b> The inflation rate falls to 3% then 1.5%. Prices are still <b>rising</b>, just more slowly.", s: { t: 4 } },
  { cap: "<b>Deflation.</b> The inflation rate becomes negative (−1%, −2%): the price level actually <b>falls</b>.", s: { t: 6 } },
] });

/* ---------- Lab 1 ---------- */
function labI() {
  if (!["fd", "hs", "tr", "ot"].every((i) => $("#" + i))) return;
  const v = [["Food", 30, +$("#fd").value, "f3"], ["Housing", 25, +$("#hs").value, "f1"], ["Transport", 15, +$("#tr").value, "f2"], ["Other", 30, +$("#ot").value, "f1"]], parts = v.map(([n, w, c]) => w * c / 100), tot = parts.reduce((a, b) => a + b, 0), big = parts.indexOf(Math.max(...parts));
  $("#r1").textContent = Lib.fmtN(tot, 1) + "%"; $("#r2").textContent = v[big][0] + " (" + Lib.fmtN(parts[big], 1) + " pts)"; $("#r3").textContent = Lib.fmtN(100 + tot, 1);
  $("#rv").textContent = `Weighted contributions: ${v.map(([n, w, c], i) => n + " " + Lib.fmtN(parts[i], 1)).join(", ")}. Inflation is ${Lib.fmtN(tot, 1)}% and the CPI moves from 100 to ${Lib.fmtN(100 + tot, 1)}. ${tot < 0 ? "Prices fall on average: deflation." : "Prices rise on average."} Food has a large weight, so a food price change moves the index more than the same change in another category.`;
  let o = SV.line(40, 250, 400, 250) + SV.line(40, 250, 40, 40), y = 250; const sc = 20;
  v.forEach(([n, w, c, k], i) => { const h = parts[i] * sc; if (h >= 0) { o += SV.rect(130, y - h, 140, h, k, op(0.65)); if (h > 14) o += SV.text(200, y - h / 2 + 5, n + " " + Lib.fmtN(parts[i], 1), "lbl bd", { "text-anchor": "middle" }); y -= h; } });
  o += SV.text(200, 270, "Total " + Lib.fmtN(tot, 1) + "%", "lbl bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "fd", label: "Food prices, % change ", min: -5, max: 15, step: 1, value: 8, fmt: (v) => v + "%", onInput: labI });
Lib.slider($("#g2"), { id: "hs", label: "Housing costs, % change ", min: -5, max: 15, step: 1, value: 4, fmt: (v) => v + "%", onInput: labI });
Lib.slider($("#g3"), { id: "tr", label: "Transport costs, % change ", min: -5, max: 15, step: 1, value: 6, fmt: (v) => v + "%", onInput: labI });
Lib.slider($("#g4"), { id: "ot", label: "Other goods and services, % change ", min: -5, max: 15, step: 1, value: 2, fmt: (v) => v + "%", onInput: labI });
labI();

/* ---------- Lab 2 ---------- */
function labR() {
  if (!["pw", "ir", "inf"].every((i) => $("#" + i))) return;
  const p = +$("#pw").value, r = +$("#ir").value, f = +$("#inf").value, rr = p - f, ri = r - f, buy = 100 / (1 + f / 100);
  $("#t1").textContent = (rr >= 0 ? "+" : "") + Lib.fmtN(rr, 1) + "%"; $("#t2").textContent = (ri >= 0 ? "+" : "") + Lib.fmtN(ri, 1) + "%"; $("#t3").textContent = "$" + Lib.fmtN(buy, 1) + " worth";
  $("#tv").textContent = `A ${p}% pay rise with ${f}% inflation changes real income by about ${Lib.fmtN(rr, 1)}%: ${rr < 0 ? "workers can buy less than before" : rr > 0 ? "workers can buy more" : "no change in purchasing power"}. A savings rate of ${r}% gives a real return of ${Lib.fmtN(ri, 1)}%${ri < 0 ? ": savers lose in real terms" : ""}. After a year of ${f}% inflation, $100 buys only $${Lib.fmtN(buy, 1)} worth of today's goods.`;
  const Y = (v) => 120 - v * 12; let o = SV.line(40, 120, 400, 120) + SV.line(40, 20, 40, 190);
  [["Pay rise", p, "f2"], ["Inflation", f, "f3"], ["Real change", rr, rr >= 0 ? "f2" : "f3"]].forEach(([l, v, k], i) => (o += SV.rect(70 + i * 110, v >= 0 ? Y(v) : 120, 80, Math.abs(Y(v) - 120), k, op(0.65)) + SV.text(110 + i * 110, 185, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, (v >= 0 ? Y(v) - 6 : 120 + Math.abs(Y(v) - 120) + 14), Lib.fmtN(v, 1) + "%", "lbl bd", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g5"), { id: "pw", label: "Nominal pay rise, % ", min: 0, max: 12, step: 1, value: 3, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g6"), { id: "ir", label: "Savings interest rate, % ", min: 0, max: 10, step: 1, value: 2, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g7"), { id: "inf", label: "Inflation rate, % ", min: 0, max: 12, step: 1, value: 5, fmt: (v) => v + "%", onInput: labR });
labR();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Inflation, disinflation or deflation?", buckets: [{"label": "Inflation"}, {"label": "Disinflation"}, {"label": "Deflation"}], items: [{"text": "Prices rise 5% this year", "b": 0}, {"text": "The inflation rate falls from 5% to 2%", "b": 1}, {"text": "The price level falls 1%", "b": 2}, {"text": "CPI rises from 100 to 103", "b": 0}, {"text": "CPI rises 3% after rising 6% last year", "b": 1}, {"text": "A negative inflation rate", "b": 2}, {"text": "Annual inflation of 8%", "b": 0}, {"text": "Prices still rise but at a slower rate", "b": 1}], done: "Inflation: prices rise. Disinflation: they rise more slowly. Deflation: they fall." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["CPI", "Weighted average price change of a typical household basket"], ["Weights", "Show the share of spending on each item"], ["Base year", "The year with CPI = 100"], ["Real value", "Value adjusted for inflation: what money can buy"], ["Nominal value", "Value at current prices"], ["Price stability", "Avoiding prolonged inflation and deflation"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of calculating the CPI in order.", items: ["Survey households to find what they buy", "Set weights by share of spending", "Price the basket in the base year (CPI = 100)", "Price the basket again in the current period", "Calculate the weighted change and the inflation rate"], done: "Basket and weights first, then prices, then the index." });
Lib.calc($("#c1"), { qs: [
  {"q": "CPI rises from 120 to 126. What is the inflation rate (%)?", "a": 5, "unit": "%", "tol": 0.1, "hint": "6 ÷ 120.", "sol": "<b>5%</b>."},
  {"q": "Food (weight 40%) rises 10% and everything else (60%) rises 2%. What is the inflation rate (%)?", "a": 5.2, "unit": "%", "tol": 0.1, "hint": "4 + 1.2.", "sol": "<b>5.2%</b>."},
  {"q": "A worker's pay rises 4% and inflation is 6%. What is the approximate change in real income (%)?", "a": -2, "unit": "%", "tol": 0.2, "hint": "4 − 6.", "sol": "<b>−2%</b>."},
  {"q": "A savings account pays 3% and inflation is 2%. What is the approximate real interest rate (%)?", "a": 1, "unit": "%", "tol": 0.1, "hint": "3 − 2.", "sol": "<b>+1%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Inflation is:", opts: ["A sustained rise in the general price level", "A fall in prices", "A fall in the inflation rate", "A rise in output"], a: 0, why: "General price level." },
  { q: "Disinflation means:", opts: ["The inflation rate is falling", "Prices are falling", "Prices have doubled", "Output is falling"], a: 0, why: "Slower rises." },
  { q: "The CPI is weighted because:", opts: ["Households spend different shares on different items", "All prices rise equally", "It excludes food", "It measures output"], a: 0, why: "Importance of items." },
  { q: "A difficulty with the CPI is:", opts: ["The basket becomes out of date", "It is exact", "It includes everyone's spending", "It measures wealth"], a: 0, why: "Buying patterns change." },
  { q: "If prices double the real value of money:", opts: ["Halves", "Doubles", "Is unchanged", "Is zero"], a: 0, why: "It buys half as much." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Inflation", "Sustained rise in the price level."],
  ["Disinflation", "Inflation rate falls."],
  ["Deflation", "Price level falls."],
  ["CPI", "Weighted basket of prices."],
  ["Weights", "Share of spending."],
  ["Real", "Adjusted for inflation."],
  ["Real income", "Pay rise minus inflation."],
  ["Difficulty", "Basket, quality, substitution."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which statement describes disinflation? (Feb/March 2020 · 12 · Q26, reworded)", opts: ["a fall in the price level", "a fall in the rate of inflation", "a rise in the value of money", "inflation below zero"], a: 1, why: "Disinflation is a fall in the rate of inflation. Prices are still rising." },
  { q: "The table shows the levels of a country's consumer prices index (CPI) between 2015 and 2019: 2015 100, 2016 99, 2017 98, 2018 101, 2019 102. Compared with the previous year, in which year was there disinflation but not deflation? (May/June 2021 · 11 · Q23, reworded)", opts: ["2016", "2017", "2018", "2019"], a: 3, why: "In 2019 prices still rose (101 to 102, +1%) but more slowly than in 2018 (+3.1%): disinflation. In 2016 and 2017 prices fell, which is deflation." },
  { q: "According to US Consumer Prices Index statistics, an identical good that cost $100 in 1913 would cost $2,359.60 in 2013. What was the approximate cumulative rate of inflation over the period? (May/June 2020 · 12 · Q23, reworded)", opts: ["23%", "230%", "2,300%", "23,000%"], a: 2, why: "(2,359.6 − 100) ÷ 100 × 100 = 2,260%, which is approximately 2,300%." },
  { q: "The table shows a country's consumer prices index (CPI) for March and April 2018: 151.3 and 148.6. Which statement correctly describes what happened between these two months? (Feb/March 2021 · 12 · Q26, reworded)", opts: ["There was a decrease in the annual rate of inflation", "There was a decrease in real interest rates", "There was an increase in the purchasing power of money", "There was an increase in the standard of living"], a: 2, why: "The CPI fell, so the same money buys more: purchasing power rose." },
  { q: "What would be certain to cause a fall in a country's cost of living? (May/June 2021 · 13 · Q19, reworded)", opts: ["a fall in real incomes", "a fall in the inflation rate", "a negative inflation rate", "a reduction in direct tax rates"], a: 2, why: "A negative inflation rate means prices fall. A lower rate of inflation could still mean rising prices." },
  { q: "Governments may have price stability as a macroeconomic objective. What is meant by price stability? (Feb/March 2025 · 12 · Q16, reworded)", opts: ["All equilibrium prices are maintained in the long run", "Demand-pull inflation cancels out any cost-push inflation", "Only disinflation is present in the economy in the long run", "Prolonged periods of inflation and deflation are avoided"], a: 3, why: "Price stability means avoiding sustained inflation and deflation." },
  { q: "If the rate of inflation rises from 2% to 20%, which function of money is likely to be most affected? (May/June 2021 · 12 · Q3, reworded)", opts: ["medium of exchange", "standard for deferred payment", "store of value", "unit of account"], a: 2, why: "High inflation quickly erodes the value of money held over time." },
  { q: "In an economy with an interest rate of 4% per annum, the rate of inflation falls from 5% to 3% per annum. What will be a benefit of this fall? (May/June 2020 · 12 · Q27, reworded)", opts: ["Menu costs will fall to zero", "People on fixed incomes will be better off in real terms", "Savers will gain in real terms", "The purchasing power of the currency will rise"], a: 2, why: "The real interest rate changes from −1% to +1%, so savers gain in real terms. Prices still rise, so purchasing power still falls." },
] });
