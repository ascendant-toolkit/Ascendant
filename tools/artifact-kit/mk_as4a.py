"""AS syllabus 4.6.1-4.6.3 Price stability: definitions, CPI, nominal and real values. Run: python3 tools/artifact-kit/mk_as4a.py"""
from asx import *
EY = EYAS("4.6.1 to 4.6.3")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Inflation</b> is a <b>sustained rise in the general price level</b>, <b class="kw">deflation</b> is a <b>sustained fall</b> in the general price level (a negative inflation rate), and <b class="kw">disinflation</b> is a <b>fall in the rate of inflation</b>, where prices still rise but more slowly. Inflation is measured by the <b>consumer price index (CPI)</b>: a typical <b>basket</b> of goods and services is priced each period, each item is <b>weighted</b> by the share of household spending on it, and the weighted average change in prices is the inflation rate. The CPI has <b>difficulties</b>: the basket and weights become out of date, it cannot capture <b>quality changes</b>, <b>new products</b> or <b>substitution</b>, and households differ. <b>Nominal (money) values</b> are measured at current prices, while <b>real values</b> are adjusted for inflation, so rising prices reduce the <b>real value</b> and purchasing power of money.</p></div>

  <h2>1 · Inflation, deflation and disinflation (4.6.1)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th><th>Price level</th><th>Inflation rate</th></tr>
    <tr><td><b>Inflation</b></td><td>Sustained rise in the general price level</td><td>Rising</td><td>Positive</td></tr>
    <tr><td><b>Disinflation</b></td><td>Fall in the <b>rate</b> of inflation</td><td>Still rising, more slowly</td><td>Positive but falling</td></tr>
    <tr><td><b>Deflation</b></td><td>Sustained fall in the general price level</td><td>Falling</td><td>Negative</td></tr>
  </table></div>
  <ul>
    <li><b>Price stability</b> means avoiding prolonged inflation and deflation, usually a low and stable inflation rate such as 2%.</li>
    <li>With <b>inflation</b> the value of money falls (the same money buys less); with <b>deflation</b> it rises, but falling prices can cause consumers to delay spending.</li>
  </ul>

  <h2>2 · Measuring inflation with the CPI (4.6.2)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Steps:</b> (1) survey households to find what they buy and how much they spend on each category (the <b>weights</b>); (2) record the prices of the <b>basket</b> in a <b>base year</b> (index = 100); (3) record prices each period; (4) calculate the weighted average price change; (5) <b>inflation rate = % change in the CPI</b>.</li>
    <li><b>Weights</b> reflect the importance of each item: a 10% rise in the price of food (30% of spending) has a bigger effect than a 10% rise in clothing (10%).</li>
    <li><b>CPI index:</b> (cost of basket this year ÷ cost of basket in base year) × 100. <b>Inflation</b> = (CPI now − CPI before) ÷ CPI before × 100.</li>
    <li><b>Possible difficulties:</b> the <b>basket becomes out of date</b> as buying patterns change; <b>quality improvements</b> and <b>new products</b> are hard to include; consumers <b>substitute</b> cheaper goods; <b>households differ</b> (poor households spend more on food and fuel); the informal economy and regional price differences are missed.</li>
  </ul>

  <h2>3 · Nominal and real values (4.6.3)</h2>
  <ul>
    <li><b>Nominal (money)</b> values are measured at <b>current prices</b>. <b>Real</b> values are adjusted for inflation, so they show <b>purchasing power</b>.</li>
    <li><b>Real value of money</b>: if prices double, the same money buys half as much: its real value halves.</li>
    <li><b>Real income</b> ≈ nominal income growth − inflation. A 3% pay rise with 5% inflation is a 2% fall in real income.</li>
    <li><b>Real interest rate</b> ≈ nominal interest rate − inflation.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Do not confuse a <b>lower inflation rate</b> (disinflation) with <b>falling prices</b> (deflation). For CPI evaluation, give a developed reason: weights or basket becoming out of date, quality change or substitution.</div>
'''

watch = '''
  <h2>1 · Building the CPI from weighted price changes</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stC"></div>
  <h2>2 · Inflation, disinflation and deflation</h2>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · Calculate the inflation rate</h2>
  <p>The basket is weighted as food 30%, housing 25%, transport 15%, other 30%. Set the price changes.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Inflation (CPI)</small><strong id="r1"></strong></div><div><small>Biggest contributor</small><strong id="r2"></strong></div><div><small>CPI if base = 100</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Stacked bars of the weighted contribution of each category to inflation"></svg></div></div></div>

  <h2>Lab 2 · Real values</h2>
  <p>Change the pay rise, savings interest rate and inflation to see real changes.</p>
  <div class="card"><div class="grid2"><div><div id="g5"></div><div id="g6"></div><div id="g7"></div>
    <div class="readout"><div><small>Real income change</small><strong id="t1"></strong></div><div><small>Real interest rate</small><strong id="t2"></strong></div><div><small>$100 buys after a year</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Bars for nominal pay rise, inflation and real income change"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Inflation, disinflation or deflation?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the steps of calculating the CPI in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The weight of food", "In a low-income country households spend a large share of income on food, so food has a large weight in the CPI. A rise in food prices therefore pushes the CPI up a lot, and the inflation rate may overstate the experience of richer households.", "CPI weights and why households differ.") +
rw("New technology and quality", "A new phone costs the same as last year's but is much better. The CPI records the same price, so it misses the quality improvement and may overstate the true rise in the cost of living.", "a difficulty in measuring inflation.") +
rw("A pay rise that is not one", "Pay rises 3% in a year when inflation is 5%. The worker has more money but can buy less, so real income has fallen by about 2%.", "nominal versus real income.") +
rw("Japan's falling prices", "For years prices in Japan stagnated or fell. Consumers delayed purchases in the hope of lower prices, which held back spending and growth: a reason deflation is a policy concern.", "deflation discouraging consumption.")
)

mc_exam = [
  mcq("m20_12", 26, "Which statement describes disinflation?", ["a fall in the price level", "a fall in the rate of inflation", "a rise in the value of money", "inflation below zero"], 1, "Disinflation is a fall in the rate of inflation. Prices are still rising."),
  mcq("s21_11", 23, "The table shows the levels of a country's consumer prices index (CPI) between 2015 and 2019: 2015 100, 2016 99, 2017 98, 2018 101, 2019 102. Compared with the previous year, in which year was there disinflation but not deflation?", ["2016", "2017", "2018", "2019"], 3, "In 2019 prices still rose (101 to 102, +1%) but more slowly than in 2018 (+3.1%): disinflation. In 2016 and 2017 prices fell, which is deflation."),
  mcq("s20_12", 23, "According to US Consumer Prices Index statistics, an identical good that cost $100 in 1913 would cost $2,359.60 in 2013. What was the approximate cumulative rate of inflation over the period?", ["23%", "230%", "2,300%", "23,000%"], 2, "(2,359.6 − 100) ÷ 100 × 100 = 2,260%, which is approximately 2,300%."),
  mcq("m21_12", 26, "The table shows a country's consumer prices index (CPI) for March and April 2018: 151.3 and 148.6. Which statement correctly describes what happened between these two months?", ["There was a decrease in the annual rate of inflation", "There was a decrease in real interest rates", "There was an increase in the purchasing power of money", "There was an increase in the standard of living"], 2, "The CPI fell, so the same money buys more: purchasing power rose."),
  mcq("s21_13", 19, "What would be certain to cause a fall in a country's cost of living?", ["a fall in real incomes", "a fall in the inflation rate", "a negative inflation rate", "a reduction in direct tax rates"], 2, "A negative inflation rate means prices fall. A lower rate of inflation could still mean rising prices."),
  mcq("m25_12", 16, "Governments may have price stability as a macroeconomic objective. What is meant by price stability?", ["All equilibrium prices are maintained in the long run", "Demand-pull inflation cancels out any cost-push inflation", "Only disinflation is present in the economy in the long run", "Prolonged periods of inflation and deflation are avoided"], 3, "Price stability means avoiding sustained inflation and deflation."),
  mcq("s21_12", 3, "If the rate of inflation rises from 2% to 20%, which function of money is likely to be most affected?", ["medium of exchange", "standard for deferred payment", "store of value", "unit of account"], 2, "High inflation quickly erodes the value of money held over time."),
  mcq("s20_12", 27, "In an economy with an interest rate of 4% per annum, the rate of inflation falls from 5% to 3% per annum. What will be a benefit of this fall?", ["Menu costs will fall to zero", "People on fixed incomes will be better off in real terms", "Savers will gain in real terms", "The purchasing power of the currency will rise"], 2, "The real interest rate changes from −1% to +1%, so savers gain in real terms. Prices still rise, so purchasing power still falls.")
]

exam = exam_page("inflation, deflation and the consumer price index",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Measurement of inflation is in short Paper 2 data-response parts (2 marks) nearly every year, in an 8 mark part on how inflation is measured and its effects, and in Paper 1 most years. Reworded past questions are below, with eight Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "1", "Oct/Nov 2021 (23) Q4(a)"), ("Data response, 2 marks", "4", "May/June 2025 (21) Q1(b); May/June 2022 (21) Q1(b); Oct/Nov 2021 (21) Q1(a); Feb/March 2021 (22) Q1(c)"), ("Multiple choice (Paper 1)", "8 shown below", "2020 to 2025")],
  [
  eq(P("w21_23", "4(a)"), "8 marks", "Explain how inflation is measured and why a rising rate of inflation may be of concern to consumers and producers.",
     ["Knowledge (up to 2): inflation is a sustained increase in the (general) price level (1) and is normally measured by the CPI or an equivalent index (1).",
      "Application (up to 3): problems for consumers, such as loss of purchasing power for those on fixed incomes and erosion of the real value of savings (1 per explained problem).",
      "Application (up to 3): problems for producers, such as menu costs and difficulty making long-term decisions such as investment (1 per explained problem). At least two problems for each should be explained; one problem well explained can gain 2 marks."],
     "Inflation: sustained rise in the price level, measured by the CPI. Consumers: fixed incomes, savings. Producers: menu costs, uncertainty for investment.",
     [[("k", "Inflation is a sustained rise in the general price level. It is normally measured by the annual percentage change in a consumer prices index, which prices a weighted basket of goods and services bought by a typical household.")], [("n", "A rising rate of inflation reduces the purchasing power of money, so consumers on fixed incomes can buy less, and the real value of savings is eroded if interest rates are below inflation. For producers, rising prices bring menu costs, because prices must be changed, and uncertainty about future costs and prices, which makes long-term investment decisions harder.")]]),
  eq(P("s25_21", "1(b)"), "2 marks", "Explain one reason why using the Consumer Price Index (CPI) to measure the inflation rate in an economy may not produce an accurate result.",
     ["The CPI is based on the average basket of products bought by all households (1), but as buying patterns change the basket used may no longer be typical (1).",
      "OR the weights and products are usually updated every two or three years to reflect changes in buying patterns (1), but this may not be frequent enough if there is rapid change in the products bought or the proportion of income spent on them (1)."],
     "Basket or weights out of date as buying patterns change.",
     [[("k", "The CPI uses a fixed basket of goods meant to represent what a typical household buys. As buying patterns change, for example with new products, the basket becomes out of date and may no longer be typical of all households, so the measured inflation rate may be inaccurate.")]]),
  eq(P("s22_21", "1(b)"), "2 marks", "Explain why price changes in the food and the non-food sectors of an economy are treated differently when calculating the CPI.",
     ["A basic recognition that price changes in the food and non-food sectors may be different, possibly with appropriate examples (1).", "A clear recognition of the importance of weights in the construction of a CPI, with reference to weightings (1): products are given larger weights to reflect the greater proportion of income spent on them."],
     "Price changes differ by sector. Weights reflect the share of spending, so each sector counts differently.",
     [[("k", "Food prices and non-food prices may change by different amounts in the same year. The CPI gives each a weight according to the share of household spending on it, so a rise in the price of food, which takes a large share of spending, has a bigger effect on the index than a rise in the price of something that takes a small share.")]]),
  eq(P("w21_21", "1(a)"), "2 marks", "Explain how inflation can halve the 'real value' of money.",
     ["The real value is the quantity of products that can be bought for a certain amount of money (1).", "If prices double, the quantity that can be bought is halved (1)."],
     "Real value = what money buys. Prices double, so it buys half.",
     [[("k", "The real value of money is the quantity of goods and services a given amount can buy. If inflation causes prices to double, the same amount of money buys only half as much, so its real value has halved.")]]),
  eq(P("m21_22", "1(c)"), "2 marks", "Explain why deflation, as experienced by Japan, discourages consumption spending.",
     ["A clear understanding that deflation refers to a fall in the general price level (1).", "An explanation of why a fall in the general price level discourages consumption (1): consumers expect prices to fall further, so they delay purchases, and the uncertainty encourages saving."],
     "Deflation: falling price level. Consumers delay purchases expecting lower prices.",
     [[("k", "Deflation is a fall in the general price level. When prices are expected to keep falling, consumers delay spending because the same goods will be cheaper in the future, and uncertainty makes them save more, so consumption spending falls.")]])
  ],
  )

tips = tips_html(
  [("Know the three terms.", "Inflation: price level up. Disinflation: inflation rate down. Deflation: price level down."),
   ("Explain the CPI steps.", "Basket, weights, base year, index."),
   ("Weights matter.", "Bigger spending share, bigger effect."),
   ("Give a developed CPI difficulty.", "Out-of-date basket, quality, substitution."),
   ("Real = nominal adjusted for inflation.", "Real growth ≈ nominal growth − inflation."),
   ("Real value of money.", "What it can buy."),
   ("Use the formula.", "(new − old) ÷ old × 100.")],
  [("Inflation", "Inflation is a sustained rise in the general price level."),
   ("Disinflation", "Disinflation is a fall in the rate of inflation."),
   ("Deflation", "Deflation is a sustained fall in the general price level."),
   ("CPI", "The CPI measures the weighted average change in the prices of a typical household basket."),
   ("Real value", "The real value of money falls when prices rise.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = '''
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
''' + CLASSIFY("cl1", "Inflation, disinflation or deflation?", ["Inflation", "Disinflation", "Deflation"],
  [("Prices rise 5% this year", 0), ("The inflation rate falls from 5% to 2%", 1), ("The price level falls 1%", 2), ("CPI rises from 100 to 103", 0), ("CPI rises 3% after rising 6% last year", 1), ("A negative inflation rate", 2), ("Annual inflation of 8%", 0), ("Prices still rise but at a slower rate", 1)],
  "Inflation: prices rise. Disinflation: they rise more slowly. Deflation: they fall.") + MATCH([
  ["CPI", "Weighted average price change of a typical household basket"],
  ["Weights", "Show the share of spending on each item"],
  ["Base year", "The year with CPI = 100"],
  ["Real value", "Value adjusted for inflation: what money can buy"],
  ["Nominal value", "Value at current prices"],
  ["Price stability", "Avoiding prolonged inflation and deflation"]]) + ORDER(
  "Put the steps of calculating the CPI in order.",
  ["Survey households to find what they buy", "Set weights by share of spending", "Price the basket in the base year (CPI = 100)", "Price the basket again in the current period", "Calculate the weighted change and the inflation rate"],
  "Basket and weights first, then prices, then the index.") + CALC([
  {"q": "CPI rises from 120 to 126. What is the inflation rate (%)?", "a": 5, "unit": "%", "tol": 0.1, "hint": "6 ÷ 120.", "sol": "<b>5%</b>."},
  {"q": "Food (weight 40%) rises 10% and everything else (60%) rises 2%. What is the inflation rate (%)?", "a": 5.2, "unit": "%", "tol": 0.1, "hint": "4 + 1.2.", "sol": "<b>5.2%</b>."},
  {"q": "A worker's pay rises 4% and inflation is 6%. What is the approximate change in real income (%)?", "a": -2, "unit": "%", "tol": 0.2, "hint": "4 − 6.", "sol": "<b>−2%</b>."},
  {"q": "A savings account pays 3% and inflation is 2%. What is the approximate real interest rate (%)?", "a": 1, "unit": "%", "tol": 0.1, "hint": "3 − 2.", "sol": "<b>+1%</b>."}]) + MCQ([
  ("Inflation is:", ["A sustained rise in the general price level", "A fall in prices", "A fall in the inflation rate", "A rise in output"], 0, "General price level."),
  ("Disinflation means:", ["The inflation rate is falling", "Prices are falling", "Prices have doubled", "Output is falling"], 0, "Slower rises."),
  ("The CPI is weighted because:", ["Households spend different shares on different items", "All prices rise equally", "It excludes food", "It measures output"], 0, "Importance of items."),
  ("A difficulty with the CPI is:", ["The basket becomes out of date", "It is exact", "It includes everyone's spending", "It measures wealth"], 0, "Buying patterns change."),
  ("If prices double the real value of money:", ["Halves", "Doubles", "Is unchanged", "Is zero"], 0, "It buys half as much.")
], "qz1") + CARDS([
  ("Inflation", "Sustained rise in the price level."),
  ("Disinflation", "Inflation rate falls."),
  ("Deflation", "Price level falls."),
  ("CPI", "Weighted basket of prices."),
  ("Weights", "Share of spending."),
  ("Real", "Adjusted for inflation."),
  ("Real income", "Pay rise minus inflation."),
  ("Difficulty", "Basket, quality, substitution.")]) + MCQ(mc_exam)

build("as4a", "as-inflation-measurement", "Inflation, Deflation and the Consumer Price Index", EY,
  "4.6.1 to 4.6.3: inflation, deflation and disinflation, measuring price changes with the CPI and its difficulties, and nominal and real values. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
