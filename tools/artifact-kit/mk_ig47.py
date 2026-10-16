"""Builds the five IGCSE Economics 4.7 Inflation reviews (4.7.1 to 4.7.5), written from scratch.
Run: python3 tools/artifact-kit/mk_ig47.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

# =========================================================== 4.7.1 Definitions
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Inflation</span> is a <b>sustained (persistent) rise in the general price level</b> over time. <span class="kw">Deflation</span> is a <b>sustained fall in the general price level</b>. Inflation means each unit of money buys less, so its <b>purchasing power falls</b>. The <b>inflation rate</b> is the percentage rise in the price level over a year. Stable, low inflation is one of the government's macroeconomic aims.</p></div>

  <h2>Three different situations</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>What happens</th><th>Example</th></tr>
    <tr><td><b>Inflation</b></td><td>Price level rises over time</td><td>Prices rise 4% a year</td></tr>
    <tr><td><b>Disinflation</b></td><td>The <b>rate</b> of inflation falls, but prices are still rising</td><td>Inflation falls from 8% to 2%: prices still rise, more slowly</td></tr>
    <tr><td><b>Deflation</b></td><td>The price level <b>falls</b> (negative inflation rate)</td><td>Inflation of −2%: prices are 2% lower than a year ago</td></tr>
  </table></div>
  <p class="note">Common mistake: a <b>fall in the inflation rate</b> is not deflation. Deflation needs the price level itself to fall.</p>

  <h2>What inflation does to the value of money</h2>
  <p>If prices rise 5% a year, $100 buys about 5% less each year. The money is worth less: the <span class="kw">purchasing power of money</span> falls. This is why inflation matters for savers, workers on fixed pay and anyone on a fixed income.</p>
  <div class="formula">Inflation rate = (price level this year − price level last year) ÷ price level last year × 100</div>

  <h2>Levels of inflation</h2>
  <ul>
    <li><b>Low, stable inflation</b> (around 2% in many countries) is the usual target of central banks. A little inflation is normal in a growing economy.</li>
    <li><b>High inflation</b> (for example 10% or more) causes problems for savers, workers, firms and exporters.</li>
    <li><b>Hyperinflation</b> is extremely rapid inflation (often defined as over 50% a month), when money loses its value so fast that people stop using it.</li>
    <li><b>Deflation</b> may sound good (cheaper goods) but is often harmful: see 4.7.4.</li>
  </ul>
  <p class="note">A rise in <b>one</b> price is not inflation. Inflation is about the <b>general</b> price level, usually measured by the Consumer Prices Index (4.7.2).</p>
'''
js = HEAD + COMMON + '''
function priceChart(s) {
  const mode = s.mode, yrs = 10, X = (t) => 80 + t * 60, Y = (v) => 330 - (v - 60) * 1.8;
  const vals = [100]; for (let t = 0; t < yrs; t++) { const r = mode === "inf" ? 4 : mode === "dis" ? 8 - 0.6 * t : -3; vals.push(vals[t] * (1 + r / 100)); }
  let o = SV.line(80, 340, 80, 30) + SV.line(80, 340, 700, 340) + SV.text(86, 40, "Price level (index)", "sm") + SV.text(700, 362, "Years", "sm", { "text-anchor": "end" });
  [80, 100, 120, 140, 160].forEach((v) => (o += SV.line(80, Y(v), 700, Y(v), "gr") + SV.text(72, Y(v) + 4, v, "sm", { "text-anchor": "end" })));
  const col = mode === "inf" ? "c2" : mode === "dis" ? "c1" : "c4", t1 = mode === "inf" ? "t2" : mode === "dis" ? "t1" : "t4";
  const n = Math.min(yrs, s.n), pts = []; for (let t = 0; t <= Math.floor(n); t++) pts.push([X(t), Y(vals[t])]);
  if (n > Math.floor(n)) { const t = Math.floor(n), f = n - t; pts.push([X(t + f), Y(vals[t] + (vals[t + 1] - vals[t]) * f)]); }
  if (pts.length > 1) o += SV.path(ptsPath(pts), col, { "stroke-width": 3 });
  pts.forEach((p, i) => (o += SV.circle(p[0], p[1], 4, mode === "inf" ? "dot2" : mode === "dis" ? "dot1" : "dot4")));
  if (s.n >= yrs) o += SV.text(X(yrs) - 6, Y(vals[yrs]) - 12, money(vals[yrs], 0), "lbl bd " + t1, { "text-anchor": "end" });
  o += SV.text(90, 62, mode === "inf" ? "Inflation: prices rise 4% a year" : mode === "dis" ? "Disinflation: inflation falls from 8% to 2%, prices still rise" : "Deflation: prices fall 3% a year", "lbl bd " + t1, { style: "font-size:15px" });
  return o;
}
Lib.stepper($("#stI"), { w: 760, h: 400, label: "Inflation, disinflation and deflation", base: { mode: "inf", n: 0 }, draw: priceChart, steps: [
  { cap: "<b>Inflation:</b> the general price level rises. Here prices rise <b>4% a year</b>, so after 10 years a basket that cost 100 costs about 148.", s: { mode: "inf", n: 10 } },
  { cap: "<b>Disinflation:</b> prices rise by 8%, then 7.4%, then less each year, down to about 2%. The inflation <b>rate falls</b>, but the price level is <b>still rising</b>.", s: { mode: "dis", n: 10 } },
  { cap: "<b>Deflation:</b> the price level <b>falls</b> 3% a year. After 10 years the same basket costs about 74. Falling prices may look good, but they can discourage spending and lead to recession.", s: { mode: "def", n: 10 } },
] });
function powerChart(s) {
  const base = 320, k = 2.4, ys = [0, 5, 10, 15, 20], vs = ys.map((y) => 100 / Math.pow(1.05, y)); let o = SV.line(60, base, 710, base) + SV.text(60, 30, "What $100 buys, as a share of what it buys today (5% inflation)", "sm");
  vs.forEach((v, i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 90 + i * 120, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 80, h, "", { style: "fill:var(--bad)", opacity: 0.8 }) + SV.text(x + 40, base - h - 8, money(v, 0) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 40, base + 20, i ? "Year " + ys[i] : "Today", "sm", { "text-anchor": "middle" }) + "</g>"; });
  return o;
}
Lib.stepper($("#stV"), { w: 760, h: 400, label: "Inflation reduces the value of money", base: { n: 0 }, draw: powerChart, steps: [
  { cap: "Today $100 buys one basket of goods.", s: { n: 1 } },
  { cap: "With <b>5% inflation</b> a year, in 5 years prices are about 28% higher, so $100 buys only about <b>78%</b> of the basket.", s: { n: 2 } },
  { cap: "After 10 years it buys about <b>61%</b>.", s: { n: 3 } },
  { cap: "After 20 years it buys under <b>40%</b>. Money that is saved or on a fixed income <b>loses its purchasing power</b>.", s: { n: 5 } },
] });

/* Lab 1 */
function labI() {
  if (!$("#ia") || !$("#ib")) return;
  const r = +$("#ia").value, n = +$("#ib").value, p = 100 * Math.pow(1 + r / 100, n), pp = 100 / Math.pow(1 + r / 100, n);
  $("#ia1").textContent = money(p, 1); $("#ia2").textContent = "$" + money(pp, 1); $("#ia3").textContent = r > 0.05 ? "Inflation" : r < -0.05 ? "Deflation" : "Stable";
  $("#iav").textContent = r > 0 ? `At ${r}% inflation a $100 basket costs $${money(p, 1)} after ${n} years, so $100 buys only the equivalent of $${money(pp, 1)} of goods today: its purchasing power has fallen.` : r < 0 ? `Prices fall ${-r}% a year: the basket costs $${money(p, 1)} after ${n} years and $100 buys the equivalent of $${money(pp, 1)}. Money gains purchasing power, but falling prices can discourage spending.` : "Prices do not change: stable purchasing power.";
  const base = 300, mx = Math.max(100, p), mn = Math.min(100, p), lo = Math.min(60, mn - 5), hi = Math.max(160, mx + 5), Y = (v) => base - ((v - lo) / (hi - lo)) * 250, X = (t) => 80 + (t / n) * 600; const pts = []; for (let t = 0; t <= n; t += n > 12 ? 0.5 : 1) pts.push([X(t), Y(100 * Math.pow(1 + r / 100, t))]);
  let o = SV.line(80, base, 700, base) + SV.line(80, base, 80, 30) + SV.text(86, 40, "Price of a $100 basket", "sm") + SV.line(80, Y(100), 700, Y(100), "dash", { style: "stroke:var(--muted);stroke-width:1.5" });
  o += SV.path(ptsPath(pts), r > 0 ? "c2" : "c4", { "stroke-width": 3 }) + SV.text(X(n) - 4, Y(p) - 10, "$" + money(p, 0), "lbl bd", { "text-anchor": "end" }) + SV.text(700, base + 22, n + " years", "sm", { "text-anchor": "end" });
  $("#labI").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ia", label: "Inflation rate each year", min: -5, max: 15, step: 0.5, value: 4, fmt: (v) => v + "%", onInput: labI });
Lib.slider($("#g2"), { id: "ib", label: "Number of years", min: 1, max: 20, step: 1, value: 10, fmt: (v) => v + " years", onInput: labI });
const SQ = [
  { n: "Prices: 100, 104, 108, 112", a: "Inflation", w: "The price level is rising by about 4% a year." },
  { n: "Inflation rate: 9%, 6%, 4%, 3%", a: "Disinflation", w: "The rate is falling but each figure is positive, so prices are still rising." },
  { n: "Prices: 100, 98, 96, 94", a: "Deflation", w: "The price level is falling." },
  { n: "Inflation rate: −1%, −2%, −1%", a: "Deflation", w: "Negative inflation means the price level is falling." },
  { n: "Inflation rate rises from 2% to 5%", a: "Higher inflation", w: "Prices still rise, and faster. Not deflation or disinflation." },
  { n: "The price of one product rises 20%", a: "Not inflation", w: "Inflation is about the general price level, not one price." },
];
button_table("sqBtns", "sqOut", SQ, 0, (p) => `<div class="tw"><table class="t"><tr><th>It is</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each <b>inflation</b>, <b>disinflation</b> or <b>deflation</b>?", buckets: [{ label: "Inflation" }, { label: "Disinflation" }, { label: "Deflation" }], items: [
  { text: "Prices rise by 3% a year", b: 0 }, { text: "The price level rises for several years in a row", b: 0 },
  { text: "Inflation falls from 6% to 3%", b: 1 }, { text: "The rate of price rises slows but prices still rise", b: 1 },
  { text: "The price level falls by 2%", b: 2 }, { text: "The inflation rate is −1%", b: 2 },
], done: "Deflation needs prices to fall. A lower inflation rate is disinflation." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Inflation", "A sustained rise in the general price level over time"],
  ["Deflation", "A sustained fall in the general price level"],
  ["Disinflation", "A fall in the rate of inflation: prices still rise"],
  ["Purchasing power", "What a unit of money can buy"],
  ["Hyperinflation", "Extremely rapid inflation"],
  ["Price stability", "Low and stable inflation"],
], done: "Good vocabulary scores marks." });
''' + calc_js([
    ("The price level was 120 last year and is 126 this year. What is the inflation rate (%)?", 5, "(126 − 120) ÷ 120 × 100 = <b>5%</b>.", None, None),
    ("The price level falls from 200 to 190. What is the rate of inflation (%)?", -5, "(190 − 200) ÷ 200 × 100 = <b>−5%</b>: deflation.", None, None),
    ("Inflation is 10% a year. A basket costs $50 today. What will it cost in a year ($)?", 55, "50 × 1.10 = <b>$55</b>.", None, None),
    ("Roughly how many years does it take for prices to double at 5% inflation (70 ÷ rate)?", 14, "70 ÷ 5 = <b>14 years</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is inflation?", ["A rise in the price of one good", "A sustained rise in the general price level", "A rise in output", "A fall in unemployment"], 1, "Inflation is a persistent rise in the general price level."),
    ("What is deflation?", ["A fall in the rate of inflation", "A sustained fall in the general price level", "A fall in output", "A rise in interest rates"], 1, "The price level itself falls."),
    ("The inflation rate falls from 8% to 3%. This is:", ["Deflation", "Disinflation", "Hyperinflation", "Stability"], 1, "Prices still rise, but more slowly."),
    ("When there is inflation, the value of money:", ["Rises", "Falls", "Stays the same", "Doubles"], 1, "Each unit buys less."),
    ("Which is not inflation?", ["Rise in the general price level", "Rise in the price of one product only", "Persistent price rises", "Prices rising faster each year"], 1, "One price is not the general price level."),
]) + "\n" + cards_js([("Inflation", "A sustained rise in the general price level over time."), ("Deflation", "A sustained fall in the general price level."), ("Disinflation", "A fall in the rate of inflation: prices still rise, but more slowly."), ("Inflation rate", "The percentage rise in the price level over a period, usually a year."), ("Price level", "The average level of prices in an economy."), ("Purchasing power", "The amount of goods and services that a unit of money can buy."), ("Hyperinflation", "Extremely rapid inflation, when money loses its value very quickly."), ("Price stability", "Low and stable inflation, a macroeconomic aim.")]) + "labI();\n"
explore = '''
  <h2>Lab 1 · Inflation and the value of money</h2>
  <p>Set an inflation rate and a number of years. See what a $100 basket costs, and what $100 buys.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Price of the basket</small><strong id="ia1"></strong></div><div><small>What $100 buys (in today's $)</small><strong id="ia2"></strong></div><div><small>Type</small><strong id="ia3"></strong></div></div><div class="verdict" id="iav"></div></div></div>
    <svg id="labI" viewBox="0 0 760 340" role="img" aria-label="Price level over time"></svg>
  </div>

  <h2>Lab 2 · Inflation, disinflation or deflation?</h2>
  <p>Pick a case to see how to classify it.</p>
  <div class="card"><div class="row" id="sqBtns"></div><div id="sqOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define inflation. (Oct/Nov 2022, P21)", "Rise, general price level, over time or persistent.", "[K|Inflation is a sustained rise in the general price level] [K|over time.]", warn="Saying 'prices go up'. It must be the general level, and sustained."),
    Q(2, "Define", 2, "Define deflation.", "Sustained fall in the general price level.", "[K|Deflation is a sustained fall] [K|in the general price level (a negative inflation rate).]"),
    Q(3, "Explain", 4, "Explain the difference between disinflation and deflation.", "Use 'whereas'. Disinflation: rate falls, prices still rise. Deflation: prices fall.",
      "[K|Disinflation is a fall in the rate of inflation,] [N|so prices are still rising but more slowly, for example inflation falling from 8% to 3%,] [K|whereas deflation is a fall in the price level itself,] [N|so the inflation rate is negative and goods get cheaper.]"),
    Q(4, "Explain", 4, "Explain what is meant by an inflation rate of 4%, and how it affects the purchasing power of money.", "State the meaning, then the effect: money buys less.",
      "[K|An inflation rate of 4% means the general price level is 4% higher than a year earlier.] [N|Each unit of money buys about 4% fewer goods and services,] [A|so $100 that bought a basket last year would buy less than the full basket now.] [N|The purchasing power of money has fallen.]"),
)
tp = tips([
    ("Inflation = sustained rise in the general price level.", "Both 'general' and 'sustained' earn marks."),
    ("Disinflation is not deflation.", "A falling inflation rate still means prices rise."),
    ("Link to purchasing power.", "Inflation means each unit of money buys less."),
    ("Use the formula.", "(new − old) ÷ old × 100."),
], cmds("Define", "Explain"))
body = page(CL("4.7.1 Definitions of inflation and deflation"), "Definitions of Inflation and Deflation", "What inflation, disinflation and deflation mean and how inflation changes the value of money. Syllabus 4.7.1.",
    learn=learn, watch=watch(("Inflation, disinflation and deflation", "stI"), ("Inflation reduces the value of money", "stV")), explore=explore,
    practise=practise(("Inflation, disinflation or deflation?", "cl1", "card"), ("Match the term", "m1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Inflation above 10% in 2022", "After energy and food prices surged, inflation passed 10% in several European countries in 2022, and central banks raised interest rates sharply.", "High inflation, its causes and policy response."),
        rw("Japan's deflation", "Japan had falling or flat prices for much of the 1990s and 2000s. Consumers expected prices to fall, so delayed spending, and growth was weak.", "Deflation and why it can harm an economy."),
        rw("Hyperinflation in Zimbabwe", "In the late 2000s Zimbabwe's prices rose so fast that people carried bundles of notes, and the currency was abandoned.", "Hyperinflation and money losing its value."),
        rw("The 2% target", "Central banks in the UK, the euro area and the US aim for around 2% inflation, believing it gives stability while allowing prices to adjust.", "Price stability does not mean zero inflation.")),
    exam=ex, tips=tp)
write("in1", body, js, "Definitions of Inflation and Deflation", "ig-inflation-definitions")

# =========================================================== 4.7.2 Measurement
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Inflation is measured using the <span class="kw">Consumer Prices Index (CPI)</span>: a measure of the average change in the prices of a <b>basket of goods and services</b> bought by a typical household, with each item <b>weighted</b> by its importance in household spending. The inflation rate is the percentage change in the CPI over a year.</p></div>

  <h2>How a CPI is built</h2>
  <ol>
    <li><b>Choose a basket.</b> Goods and services typical households buy (food, housing, transport, clothes, leisure...), based on household spending surveys.</li>
    <li><b>Give weights.</b> Each item is weighted by the share of household spending it takes. Housing or food has a larger weight than a rarely bought item.</li>
    <li><b>Collect prices</b> regularly and compare them with the prices in the <b>base year</b>, when the index is set to 100.</li>
    <li><b>Calculate the index</b> as a weighted average of the price changes.</li>
    <li><b>Calculate the inflation rate</b> from the change in the index.</li>
  </ol>
  <div class="formula">Inflation rate = (CPI this year − CPI last year) ÷ CPI last year × 100</div>
  <p><b>Weighted example:</b> food (weight 40%) prices +5%, housing (30%) +2%, transport (20%) +10%, leisure (10%) −5%. Inflation = 0.4 × 5 + 0.3 × 2 + 0.2 × 10 + 0.1 × (−5) = 2.0 + 0.6 + 2.0 − 0.5 = <b>4.1%</b>.</p>

  <h2>Reading index numbers</h2>
  <p>If the CPI is 100 in the base year and 108 later, prices are on average 8% higher than in the base year. If the CPI goes from 108 to 111.24 the next year, inflation was (111.24 − 108) ÷ 108 × 100 = 3%.</p>

  <h2>Limitations of the CPI</h2>
  <ul>
    <li><b>No household is typical.</b> A pensioner or a student spends differently from the average, so their personal inflation rate may differ.</li>
    <li><b>The basket changes</b> over time (new products, changing tastes), and weights may be out of date.</li>
    <li><b>Quality changes:</b> a more expensive phone may be better, so not all of the rise is inflation.</li>
    <li><b>Substitution:</b> people switch to cheaper goods when prices rise.</li>
    <li><b>Regional and data differences</b> and the informal economy make measurement harder.</li>
  </ul>
'''
js = HEAD + COMMON + '''
const ITEMS = [["Food", 40, 5], ["Housing", 30, 2], ["Transport", 20, 10], ["Leisure", 10, -5]];
function cpiChart(s) {
  const base = 240; let o = SV.line(60, base, 710, base) + SV.line(60, base - 4, 60, 60);
  ITEMS.forEach(([n, w, c], i) => {
    const x = 100 + i * 150; let g = "";
    g += `<g opacity="${s.a}">` + SV.rect(x, base - w * 3.5, 50, w * 3.5, "", { style: "fill:var(--accent)", opacity: 0.85 }) + SV.text(x + 25, base - w * 3.5 - 6, w + "%", "sm bd", { "text-anchor": "middle" }) + "</g>";
    const h = Math.abs(c) * 10, y = c >= 0 ? base - h : base;
    g += `<g opacity="${s.b}">` + SV.rect(x + 56, y, 40, h, "", { style: `fill:var(${c >= 0 ? "--bad" : "--good"})`, opacity: 0.8 }) + SV.text(x + 76, c >= 0 ? y - 6 : y + h + 14, (c > 0 ? "+" : "") + c + "%", "sm bd", { "text-anchor": "middle" }) + "</g>";
    g += SV.text(x + 48, base + 78, n, "sm", { "text-anchor": "middle" });
    g += `<g opacity="${s.c}">` + SV.text(x + 48, base + 98, (w / 100 * c >= 0 ? "+" : "") + money((w / 100) * c, 1), "lbl bd t2", { "text-anchor": "middle" }) + "</g>";
    o += g;
  });
  o += SV.text(60, 50, s.a > 0 ? "Blue: weight in spending · Red/green: price change" : "", "sm");
  o += `<g opacity="${s.c}">` + SV.text(380, base + 128, "Weighted total = 4.1% inflation", "lbl bd t3", { "text-anchor": "middle", style: "font-size:18px" }) + "</g>";
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 400, label: "Building the CPI", base: { a: 0, b: 0, c: 0 }, draw: cpiChart, steps: [
  { cap: "<b>Step 1: the basket and weights.</b> Statisticians survey household spending. Food takes 40% of spending, housing 30%, transport 20%, leisure 10%. These are the <b>weights</b>.", s: { a: 1, b: 0, c: 0 } },
  { cap: "<b>Step 2: price changes.</b> Over the year food rose 5%, housing 2%, transport 10%, and leisure fell 5%.", s: { a: 1, b: 1, c: 0 } },
  { cap: "<b>Step 3: weighted average.</b> Each price change is multiplied by its weight: 2.0 + 0.6 + 2.0 − 0.5 = <b>4.1%</b>. This is the inflation rate. Items with larger weights matter more.", s: { a: 1, b: 1, c: 1 } },
] });
function idxChart(s) {
  const base = 320, k = 2.2, vals = [100, 103, 106.1, 109.3], labs = ["Year 0", "Year 1", "Year 2", "Year 3"]; let o = SV.line(60, base, 710, base);
  vals.forEach((v, i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 100 + i * 150, h = (v - 60) * 5; o += `<g opacity="${op}">` + SV.rect(x, base - h, 100, h, "", { style: "fill:var(--accent)", opacity: 0.8 }) + SV.text(x + 50, base - h - 8, money(v, 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, base + 20, labs[i], "sm", { "text-anchor": "middle" }); if (i) o += SV.text(x + 50, base - h - 28, "+" + money(((v - vals[i - 1]) / vals[i - 1]) * 100, 1) + "%", "lbl bd t2", { "text-anchor": "middle" }); o += "</g>"; });
  return o;
}
Lib.stepper($("#stN"), { w: 760, h: 400, label: "From CPI numbers to the inflation rate", base: { n: 0 }, draw: idxChart, steps: [
  { cap: "In the <b>base year</b> the CPI is set at <b>100</b>.", s: { n: 1 } },
  { cap: "Next year the CPI is <b>103</b>. Inflation = (103 − 100) ÷ 100 × 100 = <b>3%</b>.", s: { n: 2 } },
  { cap: "Then <b>106.1</b>: (106.1 − 103) ÷ 103 × 100 = <b>3%</b>. The index rises every year, because prices are still rising: the <b>rate</b> is what changes.", s: { n: 3 } },
  { cap: "Year 3: <b>109.3</b>. Compared with the base year, prices are <b>9.3% higher</b>. Always divide by the <b>earlier</b> index number.", s: { n: 4 } },
] });

/* Lab 1: weighted inflation */
function labC() {
  if (!$("#ca") || !$("#cb") || !$("#cc") || !$("#cd")) return;
  const ch = [+$("#ca").value, +$("#cb").value, +$("#cc").value, +$("#cd").value], w = [40, 30, 20, 10], infl = ch.reduce((a, c, i) => a + (c * w[i]) / 100, 0), simple = ch.reduce((a, c) => a + c, 0) / 4;
  $("#ca1").textContent = money(infl, 1) + "%"; $("#ca2").textContent = money(simple, 1) + "%";
  $("#cav").textContent = `Weighted inflation = ${ch.map((c, i) => `${w[i]}% × ${c}%`).join(" + ")} = ${money(infl, 1)}%. A simple average would give ${money(simple, 1)}%, which ignores how much households spend on each item. Weights matter: raise the price of food (40%) and see the effect, then try leisure (10%).`;
  const base = 280; let o = SV.line(60, base, 700, base);
  [["Food", ch[0], 40], ["Housing", ch[1], 30], ["Transport", ch[2], 20], ["Leisure", ch[3], 10]].forEach(([n, c, wt], i) => { const x = 100 + i * 150, h = Math.abs((c * wt) / 100) * 22, y = c >= 0 ? base - h : base; o += SV.rect(x, y, 100, h, "", { style: `fill:var(${c >= 0 ? "--accent" : "--good"})`, opacity: 0.85 }) + SV.text(x + 50, base + 22, n + " (" + wt + "%)", "sm", { "text-anchor": "middle" }) + SV.text(x + 50, c >= 0 ? y - 6 : y + h + 14, (c * wt / 100 >= 0 ? "+" : "") + money((c * wt) / 100, 1), "lbl bd", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o + SV.text(60, 30, "Contribution to inflation (weight × price change)", "sm");
}
Lib.slider($("#g1"), { id: "ca", label: "Food prices (weight 40%)", min: -10, max: 20, step: 1, value: 5, fmt: (v) => v + "%", onInput: labC });
Lib.slider($("#g2"), { id: "cb", label: "Housing (weight 30%)", min: -10, max: 20, step: 1, value: 2, fmt: (v) => v + "%", onInput: labC });
Lib.slider($("#g3"), { id: "cc", label: "Transport (weight 20%)", min: -10, max: 20, step: 1, value: 10, fmt: (v) => v + "%", onInput: labC });
Lib.slider($("#g4"), { id: "cd", label: "Leisure (weight 10%)", min: -10, max: 20, step: 1, value: -5, fmt: (v) => v + "%", onInput: labC });
/* Lab 2: different households */
const HH = [
  { n: "Typical household (the CPI)", w: [40, 30, 20, 10] },
  { n: "Pensioner", w: [35, 45, 5, 15] },
  { n: "Student", w: [25, 40, 10, 25] },
  { n: "Family with a long commute", w: [35, 25, 30, 10] },
];
const PC = [5, 2, 10, -5];
button_table("hhBtns", "hhOut", HH, 0, (p) => { const infl = p.w.reduce((a, w, i) => a + (w * PC[i]) / 100, 0); return `<div class="tw"><table class="t"><tr><th>Food</th><th>Housing</th><th>Transport</th><th>Leisure</th><th>Their inflation</th></tr><tr><td>${p.w[0]}%</td><td>${p.w[1]}%</td><td>${p.w[2]}%</td><td>${p.w[3]}%</td><td><b>${money(infl, 1)}%</b></td></tr></table></div><p class="note">Same price changes (food +5%, housing +2%, transport +10%, leisure −5%), different spending, different personal inflation. This is why the CPI is not exact for every household.</p>`; });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>step in building the CPI</b> or a <b>limitation of the CPI</b>?", buckets: [{ label: "Step in building the CPI" }, { label: "Limitation" }], items: [
  { text: "Survey household spending to choose a basket", b: 0 }, { text: "Give each item a weight by share of spending", b: 0 }, { text: "Collect prices and compare with the base year", b: 0 }, { text: "Calculate a weighted average of price changes", b: 0 },
  { text: "No household buys exactly the average basket", b: 1 }, { text: "Quality improvements are hard to measure", b: 1 }, { text: "Consumers switch to cheaper goods", b: 1 }, { text: "Weights can be out of date", b: 1 },
], done: "A good answer on the CPI has the method and its limits." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Consumer Prices Index", "A weighted measure of the average change in prices of a basket of goods and services"],
  ["Basket of goods", "The goods and services typical households buy"],
  ["Weights", "The importance of each item, based on its share of spending"],
  ["Base year", "The year when the index is set at 100"],
  ["Price index", "A number showing the price level compared with the base year"],
  ["Inflation rate", "The percentage change in the CPI over a year"],
], done: "Good vocabulary scores marks." });
''' + calc_js([
    ("The CPI was 125 last year and is 130 this year. Calculate the inflation rate (%).", 4, "(130 − 125) ÷ 125 × 100 = <b>4%</b>.", None, None),
    ("The CPI rises from 100 in the base year to 112 three years later. By how much have prices risen overall (%)?", 12, "(112 − 100) ÷ 100 × 100 = <b>12%</b>.", None, None),
    ("Food (weight 50%) rises 4% and everything else (weight 50%) is unchanged. What is the inflation rate (%)?", 2, "0.5 × 4 = <b>2%</b>.", None, None),
    ("Housing (weight 30%) rises 10%, transport (20%) rises 5% and the other 50% falls 2%. What is the inflation rate (%)?", 3, "0.3 × 10 + 0.2 × 5 + 0.5 × (−2) = 3 + 1 − 1 = <b>3%</b>.", None, None),
    ("The CPI is 150 in Year 2 and 144 in Year 1. What is the inflation rate (%, 1 d.p.)?", 4.2, "(150 − 144) ÷ 144 × 100 = <b>4.2%</b>.", None, 0.1),
]) + mcq_js("qz1", [
    ("What does the CPI measure?", ["Output", "The average change in prices of a basket of goods and services", "Employment", "The exchange rate"], 1, "A weighted index of consumer prices."),
    ("Why are weights used in the CPI?", ["Because some items are more important in household spending", "Because all prices change equally", "To measure output", "To raise inflation"], 0, "Bigger spending shares matter more."),
    ("The CPI rises from 100 to 105. Inflation is:", ["105%", "5%", "0.5%", "10%"], 1, "(105 − 100) ÷ 100 × 100."),
    ("Which is a limitation of the CPI?", ["It is a weighted average", "It uses a basket", "It may not match the spending of every household", "It uses a base year"], 2, "No household is typical."),
    ("The base year of an index has a value of:", ["0", "1", "100", "1,000"], 2, "The index starts at 100."),
]) + "\n" + cards_js([("Consumer Prices Index (CPI)", "A weighted measure of the average change in the prices of a basket of goods and services."), ("Basket of goods and services", "The items typical households buy that are used to calculate the CPI."), ("Weights", "The importance given to each item, based on its share of household spending."), ("Base year", "The year used as the starting point of an index, set at 100."), ("Price index", "A number that shows price levels compared with a base year."), ("Weighted average", "An average where each item counts according to its importance."), ("Cost of living", "The cost of the goods and services households need to live."), ("Inflation rate", "The percentage rise in the price level, usually per year.")]) + "labC(); showHH0();\n".replace("showHH0();", "")
explore = '''
  <h2>Lab 1 · Weighted inflation</h2>
  <p>Change the price of each group. Food has the biggest weight, so changes there matter most to the CPI.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>Inflation (weighted)</small><strong id="ca1"></strong></div><div><small>Simple average</small><strong id="ca2"></strong></div></div><div class="verdict" id="cav"></div></div></div>
    <svg id="labC" viewBox="0 0 760 330" role="img" aria-label="Contribution of each group to inflation"></svg>
  </div>

  <h2>Lab 2 · Different households, different inflation</h2>
  <p>Pick a household to see how its own inflation differs from the CPI.</p>
  <div class="card"><div class="row" id="hhBtns"></div><div id="hhOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define a Consumer Prices Index. (Oct/Nov 2023, P23)", "A measure of inflation or cost of living; weights; basket.", "[K|A Consumer Prices Index is a measure of inflation (or the cost of living)] [K|using a weighted basket of goods and services.]"),
    Q(2, "Calculate", 2, "The CPI was 120 last year and 126 this year. Calculate the inflation rate.", "Change ÷ original × 100. Show working.", "[A|(126 − 120) ÷ 120 × 100 = 5%.]"),
    Q(3, "Explain", 4, "Explain how a consumer prices index is calculated.", "Basket, weights, prices compared with base year, weighted average.",
      "[K|Statisticians choose a basket of goods and services that typical households buy, based on household spending surveys.] [N|Each item is given a weight according to its share of spending.] [N|Prices are collected regularly and compared with the base year, when the index is 100,] [N|and a weighted average of the price changes gives the index. The percentage change in the index is the inflation rate.]"),
    Q(4, "Explain", 4, "Explain two reasons why the CPI may not accurately show the inflation experienced by every household.", "Different spending patterns; quality changes; substitution; weights out of date.",
      "[K|Households spend their income differently.] [N|A pensioner may spend a larger share on housing and heating than the typical household, so if those prices rise fast their personal inflation could be higher than the CPI.] [K|The basket and weights may be out of date.] [N|If consumers switch to cheaper goods or new products appear, the index may not reflect what households actually buy.]"),
)
tp = tips([
    ("CPI = weighted basket.", "Two words that earn the definition marks: basket and weights."),
    ("Inflation rate = (new CPI − old CPI) ÷ old CPI × 100.", "Divide by the earlier figure."),
    ("Weights matter.", "Larger share of spending means more effect."),
    ("Limitations.", "No household is typical; quality; substitution; outdated basket."),
], cmds("Define", "Calculate", "Explain"))
body = page(CL("4.7.2 Measurement of inflation"), "Measurement of Inflation", "How the Consumer Prices Index is built, how to calculate the inflation rate from it, and its limitations. Syllabus 4.7.2.",
    learn=learn, watch=watch(("Building the CPI", "stC"), ("From CPI numbers to the inflation rate", "stN")), explore=explore,
    practise=practise(("Method or limitation?", "cl1", "card"), ("Match the term", "m1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Why people disagree with the official figure", "Official inflation can feel different from lived experience: if the items you buy most often (such as food and fuel) rise faster than the average, your own inflation is higher.", "A limitation of the CPI."),
        rw("Updating the basket", "Statistical offices review the basket regularly: new items such as streaming services and smartphones are added and old items removed.", "The basket is not fixed."),
        rw("Tunisia's wages and inflation", "A past paper asks students to analyse the relationship between a country's average wage and its inflation rate using the table of data.", "Reading inflation data from a table.")),
    exam=ex, tips=tp)
write("in2", body, js, "Measurement of Inflation", "ig-inflation-measurement")

# =========================================================== 4.7.3 Causes
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The syllabus gives two causes of inflation: <span class="kw">demand-pull</span> and <span class="kw">cost-push</span>. <b>Demand-pull inflation</b> happens when total demand grows faster than the economy can supply. <b>Cost-push inflation</b> happens when firms' costs of production rise and they pass them on in higher prices. On an AD/AS diagram, demand-pull is AD shifting right; cost-push is AS shifting left.</p></div>

  <h2>Demand-pull inflation</h2>
  <ul>
    <li><b>What happens:</b> AD rises faster than AS, so firms raise prices. It is strongest when the economy is close to full capacity.</li>
    <li><b>Causes of a rise in AD:</b> more consumer spending (lower interest rates, tax cuts, higher confidence, a rise in the money supply, higher wages), more investment, more government spending, more exports.</li>
    <li><b>Typical signs:</b> low unemployment, strong growth, rising wages.</li>
  </ul>
  <h2>Cost-push inflation</h2>
  <ul>
    <li><b>What happens:</b> firms' costs rise, so they raise prices to protect profits. AS shifts left: output may fall while prices rise.</li>
    <li><b>Causes:</b> wages rising faster than productivity; higher prices of raw materials and energy; higher indirect taxes; a <b>fall in the exchange rate</b>, which raises the price of imported inputs (<b>imported inflation</b>); higher profit margins; tariffs.</li>
  </ul>
  <div class="grid2">
    <div class="card"><h3>Wage-price spiral</h3><p>Higher prices lead workers to demand higher wages, which raise firms' costs, so prices rise again. Wage rises can be both demand-pull (more spending) and cost-push (higher costs).</p></div>
    <div class="card"><h3>Inflation can fall even when demand rises</h3><p>If supply grows by more (productivity gains, lower costs, a stronger exchange rate), the price level can fall or rise by less even when AD increases.</p></div>
  </div>

  <h2>Telling them apart</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Demand-pull</th><th>Cost-push</th></tr>
    <tr><td>Diagram</td><td>AD shifts right</td><td>AS shifts left</td></tr>
    <tr><td>Output</td><td>Rises (until capacity)</td><td>Falls</td></tr>
    <tr><td>Unemployment</td><td>Falls</td><td>Rises</td></tr>
    <tr><td>Example</td><td>Tax cuts, lower interest rates, booming exports</td><td>Oil price rise, wage increases above productivity, weaker currency</td></tr>
  </table></div>
'''
js = HEAD + COMMON + '''
Lib.stepper($("#stD"), { w: 760, h: 400, label: "Demand-pull inflation", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b>.", s: { sh: 0, a: 0 } },
  { cap: "Spending rises: lower interest rates, tax cuts, booming exports. <b>AD shifts right</b>. Output rises and the price level rises.", s: { sh: 14, a: 0 } },
  { cap: "If the economy is <b>close to full capacity</b>, AS is steep. The same rise in demand gives a small rise in output and a <b>big rise in prices</b>: <b>demand-pull inflation</b>.", s: { sh: 40, a: 0 } },
] });
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Cost-push inflation", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b>.", s: { sh: 0, a: 0 } },
  { cap: "Costs rise: oil and raw material prices, wages above productivity, a weaker currency raising import costs. <b>AS shifts left</b> to AS₁.", s: { sh: 0, a: -12 } },
  { cap: "Output <b>falls</b> to Y₁ and the price level <b>rises</b> to P₁: <b>cost-push inflation</b>. Unemployment may rise as well.", s: { sh: 0, a: -12 } },
] });
const WSP = ["Prices rise, so workers' real wages fall", "Workers (and unions) demand higher wages", "Firms' costs rise: cost-push pressure", "Higher wages also raise spending: demand-pull pressure", "Firms raise prices again", "The cycle repeats: a wage-price spiral"];
Lib.stepper($("#stW"), { w: 760, h: 400, label: "The wage-price spiral", base: { n: 0 }, draw: mkChain(WSP, "--bad"), steps: chainSteps(["Prices rise, so workers' <b>real wages fall</b>.", "Workers and unions <b>demand higher wages</b>.", "<b>Firms' costs rise</b>: cost-push pressure.", "Higher pay also raises spending: <b>demand-pull pressure</b>.", "Firms <b>raise prices</b> again.", "The cycle <b>repeats</b>: a wage-price spiral. Expectations of inflation make it harder to stop."]) });

/* Lab 1 */
function labT() {
  if (!$("#ta") || !$("#tb")) return;
  const sh = +$("#ta").value, a = -(+$("#tb").value), [y, p] = solve2(sh, a), dy = y - 50, dp = p - 50;
  $("#ta1").textContent = (dy >= 0 ? "+" : "−") + money(Math.abs(dy), 1); $("#ta2").textContent = (dp >= 0.05 ? "+" : dp <= -0.05 ? "−" : "") + money(Math.abs(dp), 1);
  $("#ta3").textContent = sh > 0 && a === 0 ? "Demand-pull" : sh === 0 && a < 0 ? "Cost-push" : sh > 0 && a < 0 ? "Both" : "None";
  $("#tav").textContent = sh === 0 && a === 0 ? "Move a slider." : a === 0 ? `AD shifts right: output +${money(dy, 1)} and prices +${money(dp, 1)}. Demand-pull inflation. The nearer to full capacity, the more of it is prices.` : sh === 0 ? `AS shifts left: output ${money(dy, 1)} and prices +${money(dp, 1)}. Cost-push inflation: prices rise while output falls.` : `Both: prices rise by ${money(dp, 1)}. Output changes by ${dy >= 0 ? "+" : ""}${money(dy, 1)}.`;
  $("#labT").innerHTML = adasChart({ sh, a });
}
Lib.slider($("#g1"), { id: "ta", label: "Rise in AD (demand-pull)", min: 0, max: 50, step: 2, value: 14, fmt: (v) => "+" + v, onInput: labT });
Lib.slider($("#g2"), { id: "tb", label: "Rise in costs (AS shifts left)", min: 0, max: 20, step: 1, value: 0, fmt: (v) => v, onInput: labT });
const CAUSE = [
  { n: "Higher consumer spending", t: "Demand-pull", e: "Lower interest rates, tax cuts or higher confidence raise C and so AD." },
  { n: "Higher government spending", t: "Demand-pull", e: "G is a part of AD; a large stimulus may overheat the economy." },
  { n: "Booming exports", t: "Demand-pull", e: "Strong overseas demand raises X and so AD." },
  { n: "Rise in the money supply", t: "Demand-pull", e: "More money and credit raise spending." },
  { n: "Wages rise faster than productivity", t: "Cost-push (and demand-pull)", e: "Labour costs per unit rise; higher pay can also raise spending." },
  { n: "Higher oil or raw material prices", t: "Cost-push", e: "Firms' costs rise across many industries, so prices rise." },
  { n: "Fall in the exchange rate", t: "Cost-push (imported inflation)", e: "Imported inputs and goods cost more in the home currency." },
  { n: "Higher indirect taxes", t: "Cost-push", e: "VAT and excise duties raise the price firms and consumers pay." },
];
button_table("ctBtns", "ctOut", CAUSE, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type of inflation</th><th>How it works</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a cause of <b>demand-pull</b> or <b>cost-push</b> inflation?", buckets: [{ label: "Demand-pull" }, { label: "Cost-push" }], items: [
  { text: "Consumer confidence and spending surge", b: 0 }, { text: "Interest rates are cut", b: 0 }, { text: "A government stimulus package", b: 0 }, { text: "A boom in exports", b: 0 },
  { text: "A rise in oil prices", b: 1 }, { text: "Wages rise faster than productivity", b: 1 }, { text: "The currency falls, raising import costs", b: 1 }, { text: "Firms face higher raw material costs", b: 1 },
], done: "Demand-pull: AD shifts right. Cost-push: AS shifts left." });
Lib.classify($("#cl2"), { prompt: "Which <b>diagram shift and effect</b> fits each type?", buckets: [{ label: "AD shifts right" }, { label: "AS shifts left" }], items: [
  { text: "Demand-pull inflation", b: 0 }, { text: "Output rises and unemployment falls", b: 0 }, { text: "Tax cuts raise spending", b: 0 },
  { text: "Cost-push inflation", b: 1 }, { text: "Output falls and unemployment may rise", b: 1 }, { text: "Energy costs surge", b: 1 },
], done: "Link the type to the diagram." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Demand-pull inflation", "Inflation caused by total demand growing faster than supply"],
  ["Cost-push inflation", "Inflation caused by a rise in firms' costs of production"],
  ["Imported inflation", "Inflation caused by dearer imports, often after a currency falls"],
  ["Wage-price spiral", "Wages and prices pushing each other up"],
  ["Productivity", "Output per worker"],
  ["Full capacity", "When resources are fully used and output cannot rise more"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a fall in the exchange rate could cause inflation</b>.", items: [
  "The currency falls against other currencies",
  "Imported raw materials and goods cost more in the home currency",
  "Firms' costs of production rise",
  "AS shifts to the left",
  "Firms raise prices: cost-push inflation",
], done: "Imported inflation chain." });
''' + calc_js([
    ("Wages rise 6% and productivity rises 2%. By roughly what percentage do labour costs per unit rise?", 4, "6 − 2 = <b>about 4%</b>.", None, None),
    ("A raw material that makes up 30% of a firm's costs rises in price by 20%. By how much do the firm's total costs rise (%)?", 6, "30% × 20% = <b>6%</b>.", None, None),
    ("Total spending rises 5% but output can only rise 2%. By roughly how much could the price level rise (%)?", 3, "5 − 2 = <b>about 3%</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which is a cause of demand-pull inflation?", ["A rise in oil prices", "A cut in interest rates leading to higher spending", "A rise in productivity", "A fall in wages"], 1, "Higher spending raises AD."),
    ("Which is a cause of cost-push inflation?", ["Higher consumer confidence", "A rise in firms' raw material costs", "A rise in exports", "More government spending"], 1, "Higher costs shift AS left."),
    ("A fall in the exchange rate may cause inflation because:", ["Imported inputs cost more", "Exports fall", "Wages fall", "Spending falls"], 0, "Imported inflation."),
    ("Demand-pull inflation is most likely when the economy is:", ["In deep recession", "Close to full capacity", "Producing far below capacity", "In deflation"], 1, "Prices rise when output cannot."),
    ("Wages rising faster than productivity is most likely to cause:", ["Cost-push inflation", "Deflation", "Lower prices", "Falling costs"], 0, "Unit labour costs rise."),
]) + "\n" + cards_js([("Demand-pull inflation", "A rise in the price level caused by AD growing faster than AS."), ("Cost-push inflation", "A rise in the price level caused by a rise in firms' costs."), ("Imported inflation", "Inflation caused by rising import prices, often after a fall in the exchange rate."), ("Wage-price spiral", "A cycle where higher wages raise prices, which lead to higher wage demands."), ("Productivity", "Output per worker or per unit of input."), ("Full capacity", "When resources are fully used so output cannot rise more."), ("Unit labour costs", "Labour cost per unit of output."), ("Total demand", "Aggregate demand: C + I + G + (X − M)."), ("Supply shock", "A sudden change in costs or supply, such as an oil price rise.")]) + "labT();\n"
explore = '''
  <h2>Lab 1 · Demand-pull or cost-push?</h2>
  <p>Raise AD, raise costs (AS shifts left), or both, and see the effect on output and the price level.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Change in real GDP</small><strong id="ta1"></strong></div><div><small>Change in price level</small><strong id="ta2"></strong></div><div><small>Type</small><strong id="ta3"></strong></div></div><div class="verdict" id="tav"></div></div></div>
    <svg id="labT" viewBox="0 0 760 400" role="img" aria-label="Aggregate demand and supply diagram"></svg>
  </div>

  <h2>Lab 2 · What caused it?</h2>
  <p>Pick a cause to see which type of inflation it leads to.</p>
  <div class="card"><div class="row" id="ctBtns"></div><div id="ctOut"></div></div>
'''
ex = exam(
    Q(1, "Identify", 2, "Identify two possible causes of demand-pull inflation. (May/June 2020, P22)", "Name two things that raise total demand.", "[K|A cut in interest rates (or income tax) raising consumer spending.] [K|An increase in government spending (or exports).]"),
    Q(2, "Explain", 4, "Explain two causes of inflation. (Oct/Nov 2021, P21)", "One demand-pull and one cost-push is the simplest pair, each developed.",
      "[K|One cause is demand-pull inflation.] [N|If consumers spend more, for example after a cut in income tax or interest rates, total demand could rise faster than supply, so firms could raise prices.] [K|Another cause is cost-push inflation.] [N|If wages or raw material prices rise, firms' costs rise and they may pass this on as higher prices.]"),
    Q(3, "Explain", 4, "Explain two ways an increase in wages can cause inflation. (Oct/Nov 2021, P23)", "One way is demand-pull (spending), one is cost-push (costs).",
      "[K|Higher wages raise workers' incomes and so consumption,] [N|which increases total demand and could cause demand-pull inflation if supply cannot keep up.] [K|Higher wages also raise firms' costs of production,] [N|so firms may raise prices, causing cost-push inflation.]"),
    Q(4, "Explain", 4, "Explain why inflation may fall even if there is an increase in total demand. (Oct/Nov 2020, P21)", "Supply must rise by more: productivity, technology, lower costs, stronger exchange rate.",
      "[K|An increase in total supply may be greater than the increase in total demand,] [N|for example if productivity or technology improves so firms can produce more at lower cost.] [N|Costs of production may also fall, for example because of lower raw material prices or a stronger exchange rate, which lowers import costs,] [N|so firms may not need to raise prices and the price level may rise by less or fall.]"),
    Q(5, "Analyse", 6, "Analyse how a rise in tourism can increase inflation in an economy. (Oct/Nov 2024, P21)", "Tourism raises demand; may raise costs (wages, rents). Both types.",
      "[K|A rise in tourism increases spending in the economy, by foreign visitors, so total demand could rise.] [N|Hotels, restaurants and shops are likely to sell more and may raise prices if they are close to capacity, causing demand-pull inflation.] [N|Tourism could also raise demand for workers and land, pushing up wages and rents,] [N|which raise firms' costs and could cause cost-push inflation.] [N|A rise in the exchange rate from higher foreign currency inflows may offset some of this.]", key=True),
    Q(6, "Analyse", 6, "Analyse how a fall in a country's foreign exchange rate could increase its inflation rate. (Oct/Nov 2022, P22)", "Imports dearer; raw materials; cost-push; also exports cheaper raise demand.",
      "[K|A fall in the exchange rate makes imports dearer in the home currency.] [N|Imported raw materials, fuel and components cost firms more, so costs of production rise and AS could shift left, causing cost-push inflation.] [N|Imported consumer goods also cost more, which directly raises the price level.] [N|At the same time exports are cheaper, so demand for them could rise, raising AD and causing demand-pull inflation.] [E|The size of the effect depends on how much the country imports.]", key=True),
)
tp = tips([
    ("Two causes:", "demand-pull and cost-push."),
    ("Demand-pull: AD shifts right. Cost-push: AS shifts left.", "Draw the diagram."),
    ("Wages can be both.", "More spending (demand) and higher costs (cost-push)."),
    ("Exchange rate fall = imported inflation.", "Cost-push, plus cheaper exports raising demand."),
    ("Mention capacity.", "Demand-pull is stronger near full capacity."),
], cmds("Identify", "Explain", "Analyse"))
body = page(CL("4.7.3 Causes of inflation"), "Causes of Inflation", "Demand-pull and cost-push inflation, the wage-price spiral, and imported inflation. Syllabus 4.7.3.",
    learn=learn, watch=watch(("Demand-pull inflation", "stD"), ("Cost-push inflation", "stP"), ("The wage-price spiral", "stW")), explore=explore,
    practise=practise(("Demand-pull or cost-push?", "cl1", "card"), ("Which diagram shift?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("The 1970s oil shocks", "When oil prices quadrupled in 1973, firms' costs rose sharply and many economies had high inflation and high unemployment together.", "Cost-push inflation from higher raw material prices."),
        rw("Energy and food prices in 2022", "Energy and food prices surged after Russia's invasion of Ukraine, pushing up firms' costs and household bills in many countries.", "Cost-push inflation. Some countries also had demand-pull from earlier stimulus."),
        rw("Pakistan's demand-pull in 2017", "A past paper asks for causes of demand-pull inflation in Pakistan, where government spending and consumer spending were growing.", "Identify two causes."),
        rw("A weaker currency in Turkey", "When the Turkish lira fell sharply, imports cost much more in lira and inflation rose well above 50% at one stage.", "Imported inflation after a fall in the exchange rate.")),
    exam=ex, tips=tp)
write("in3", body, js, "Causes of Inflation", "ig-inflation-causes")

# =========================================================== 4.7.4 Consequences
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Inflation makes <b>some people better off and some worse off</b>. The main idea is the <span class="kw">real interest rate</span>: the nominal interest rate minus the inflation rate. If inflation is higher than the interest rate, <b>savers and lenders lose</b> (their money buys less) and <b>borrowers gain</b> (the real value of their debt falls). Inflation also affects consumers, workers, firms and the whole economy, and deflation has its own costs.</p></div>

  <h2>Savers, lenders and borrowers</h2>
  <div class="formula">Real interest rate ≈ nominal interest rate − inflation rate</div>
  <div class="tw"><table class="t">
    <tr><th>Group</th><th>When inflation is higher than the interest rate</th></tr>
    <tr><td><b>Savers</b></td><td>The real value of savings falls: $1,000 earning 3% grows to $1,030, but with 5% inflation it buys less than before (real rate ≈ −2%)</td></tr>
    <tr><td><b>Lenders</b></td><td>Are repaid in money that is worth less. They lose unless the interest rate rises with inflation</td></tr>
    <tr><td><b>Borrowers</b></td><td>Repay in money that is worth less, so the real value of the debt falls. They gain, particularly with fixed-rate loans</td></tr>
  </table></div>

  <h2>Consequences for other groups</h2>
  <div class="tw"><table class="t">
    <tr><th>Group</th><th>Possible consequences of inflation</th></tr>
    <tr><td><b>Consumers</b></td><td>Purchasing power falls; people on fixed incomes (pensioners) lose most; may buy now before prices rise further</td></tr>
    <tr><td><b>Workers</b></td><td>Real wages fall if pay does not keep up; pressure for higher pay, possible strikes; uncertainty</td></tr>
    <tr><td><b>Producers and firms</b></td><td>Higher costs and menu costs (changing prices); uncertainty reduces investment; exports less competitive if inflation is higher than rivals; but may gain if prices rise faster than costs</td></tr>
    <tr><td><b>The economy</b></td><td>Falling international competitiveness and a worse current account; lower growth if uncertainty cuts investment; redistribution from savers to borrowers; very high inflation can destroy confidence in money</td></tr>
  </table></div>

  <h2>Advantages of low inflation</h2>
  <ul>
    <li>Purchasing power is not eroded much and wages may keep pace.</li>
    <li>Greater <b>certainty</b> encourages investment and so growth and jobs.</li>
    <li>Exports stay <b>price competitive</b>, helping the current account.</li>
    <li>Savings keep their value.</li>
  </ul>

  <h2>Consequences of deflation</h2>
  <ul>
    <li><b>Spending may be delayed</b> as people wait for lower prices, so demand and output fall.</li>
    <li><b>Firms' profits fall</b> and they may cut jobs: unemployment rises, and a recession may follow.</li>
    <li><b>The real value of debt rises</b>, hurting borrowers.</li>
    <li><b>But:</b> if it is caused by lower costs or better technology, output can rise, and exports may become more competitive.</li>
  </ul>
'''
js = HEAD + COMMON + '''
function realChart(s) {
  const base = 320, k = 0.22; let o = SV.line(60, base, 710, base);
  const bars = [["Savings today", 1000, "--muted", clamp(s.n, 0, 1)], ["After a year: money", 1030, "--accent", clamp(s.n - 1, 0, 1)], ["After a year: what it buys", 1030 / 1.05, "--bad", clamp(s.n - 2, 0, 1)]];
  bars.forEach(([n, v, c, op], i) => { if (op <= 0) return; const x = 110 + i * 200, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 130, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, base - h - 8, "$" + money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 22, n, "sm", { "text-anchor": "middle" }) + "</g>"; });
  if (s.n > 3) o += SV.text(380, 50, "Real value falls by about 1.9%: a real interest rate of about −2%", "lbl bd t2", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 400, label: "What inflation does to savings", base: { n: 0 }, draw: realChart, steps: [
  { cap: "A saver has <b>$1,000</b>. The bank pays <b>3% interest</b>.", s: { n: 1 } },
  { cap: "After a year she has <b>$1,030</b>: a nominal rise of 3%.", s: { n: 2 } },
  { cap: "But prices rose <b>5%</b>. In terms of what the money buys, $1,030 is worth only about <b>$981</b> in last year's prices.", s: { n: 3 } },
  { cap: "She has <b>lost purchasing power</b>: the <b>real interest rate</b> is 3% − 5% = about <b>−2%</b>. A <b>borrower</b> with a fixed-rate loan gains in the same way, as their debt is worth less.", s: { n: 4 } },
] });
const ICH = ["Inflation in the country is higher than in its trading partners", "Its exports become dearer than rivals' exports", "Foreign buyers switch away: exports fall", "Imports look cheaper, so imports rise", "The current account moves towards deficit", "Output and jobs in export industries are hit"];
Lib.stepper($("#stX"), { w: 760, h: 400, label: "Inflation and international competitiveness", base: { n: 0 }, draw: mkChain(ICH, "--bad"), steps: chainSteps(["The country has <b>higher inflation</b> than its trading partners.", "Its goods become <b>dearer</b> compared with rivals'.", "Foreign buyers <b>switch away</b>: exports fall.", "Domestic buyers switch to cheaper <b>imports</b>.", "The <b>current account</b> moves towards deficit.", "Output and jobs in export industries are hit: a cost of high inflation to the economy."]) });

/* Lab 1: real interest rate */
function labR() {
  if (!$("#ra") || !$("#rb")) return;
  const i = +$("#ra").value, p = +$("#rb").value, real = ((1 + i / 100) / (1 + p / 100) - 1) * 100, sav = 10000 * real / 100;
  $("#ra1").textContent = (real >= 0 ? "+" : "−") + money(Math.abs(real), 1) + "%"; $("#ra2").textContent = (sav >= 0 ? "+$" : "−$") + Math.abs(Math.round(sav)).toLocaleString("en-US");
  $("#ra3").textContent = real < -0.05 ? "Borrowers" : real > 0.05 ? "Savers" : "Neither";
  $("#rav").textContent = real < -0.05 ? `Inflation (${p}%) is higher than the interest rate (${i}%), so the real rate is ${money(real, 1)}%. Savers lose purchasing power; borrowers gain because their debt is worth less in real terms.` : real > 0.05 ? `Interest (${i}%) is above inflation (${p}%): savers earn a positive real return and borrowers pay a real cost.` : "Interest equals inflation: savers just keep their purchasing power.";
  const base = 290, k = 14; let o = SV.line(60, base, 700, base);
  [["Nominal interest", i, "--accent"], ["Inflation", p, "--bad"], ["Real interest", real, real >= 0 ? "--good" : "--warn"]].forEach(([n, v, c], j) => { const x = 120 + j * 190, h = Math.abs(v) * k, y = v >= 0 ? base - h : base; o += SV.rect(x, y, 130, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, v >= 0 ? y - 8 : y + h + 16, (v >= 0 ? "" : "−") + money(Math.abs(v), 1) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 40, n, "sm", { "text-anchor": "middle" }); });
  $("#labR").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ra", label: "Nominal interest rate", min: 0, max: 12, step: 0.5, value: 3, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g2"), { id: "rb", label: "Inflation rate", min: -2, max: 15, step: 0.5, value: 5, fmt: (v) => v + "%", onInput: labR });
const WG = [
  { n: "Savers", g: "Gain if the interest rate is above inflation.", l: "Lose purchasing power if inflation is above the interest rate." },
  { n: "Lenders", g: "Gain if rates rise with inflation or are variable.", l: "Lose with fixed-rate loans when inflation rises: repaid in money worth less." },
  { n: "Borrowers", g: "The real value of the debt falls (fixed-rate loans).", l: "Lose if interest rates are raised to fight inflation (variable rates)." },
  { n: "Pensioners and fixed incomes", g: "Few gains unless pensions rise with prices.", l: "Purchasing power falls each year." },
  { n: "Workers", g: "Gain if wages rise faster than prices.", l: "Real wages fall if pay lags inflation; uncertainty and disputes." },
  { n: "Firms", g: "May gain if prices rise faster than costs; debts eased.", l: "Higher costs, menu costs, uncertainty, and exports less competitive." },
  { n: "Exporters", g: "None, unless inflation is lower than rivals'.", l: "Higher prices abroad reduce sales if inflation is higher than competitors'." },
];
button_table("wgBtns", "wgOut", WG, 0, (p) => `<div class="tw"><table class="t"><tr><th>Possible gains</th><th>Possible losses</th></tr><tr><td>${p.g}</td><td>${p.l}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "When inflation is <b>higher than the interest rate</b>, who is likely to <b>gain</b> and who to <b>lose</b>?", buckets: [{ label: "Gains" }, { label: "Loses" }], items: [
  { text: "A borrower with a fixed-rate loan", b: 0 }, { text: "A household whose mortgage debt is worth less in real terms", b: 0 }, { text: "A firm whose output prices rise faster than costs", b: 0 },
  { text: "A saver with money in a bank account", b: 1 }, { text: "A pensioner on a fixed income", b: 1 }, { text: "A lender with a fixed-rate loan", b: 1 }, { text: "An exporter whose prices rise above competitors'", b: 1 },
], done: "Real interest rate = nominal rate − inflation." });
Lib.classify($("#cl2"), { prompt: "Is each a consequence of <b>inflation</b> or of <b>deflation</b>?", buckets: [{ label: "Inflation" }, { label: "Deflation" }], items: [
  { text: "Purchasing power of money falls", b: 0 }, { text: "Exports become less competitive if inflation is above rivals'", b: 0 }, { text: "Savers lose purchasing power", b: 0 },
  { text: "Consumers delay spending, expecting lower prices", b: 1 }, { text: "The real value of debt rises", b: 1 }, { text: "Firms' profits fall and jobs may be cut", b: 1 },
], done: "Both can cause problems: stable prices are the aim." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Real interest rate", "Nominal interest rate minus inflation"],
  ["Nominal interest rate", "The interest rate not adjusted for inflation"],
  ["Menu costs", "The cost to firms of changing prices"],
  ["Fixed income", "Income that does not rise with prices, such as some pensions"],
  ["Real wage", "Wages adjusted for inflation: what pay can buy"],
  ["Price competitiveness", "How cheap a country's goods are compared with rivals'"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how deflation could cause a recession</b>.", items: [
  "The price level falls",
  "Consumers expect lower prices and delay spending",
  "Total demand falls",
  "Firms' sales and profits fall",
  "Firms cut output and jobs: unemployment rises",
  "Real GDP falls: recession",
], done: "Why deflation can harm an economy." });
''' + calc_js([
    ("Interest on savings is 4% and inflation is 6%. What is the real interest rate (%)?", -2, "4 − 6 = <b>−2%</b>.", None, None),
    ("A worker's pay rises 3% while inflation is 5%. What is the approximate change in real pay (%)?", -2, "3 − 5 = <b>−2%</b>.", None, None),
    ("A saver has $2,000 earning 2% interest while inflation is 5%. After a year she has $2,040. What would the original basket of goods cost now ($)?", 2100, "2,000 × 1.05 = <b>$2,100</b>, so she cannot afford it.", None, None),
    ("A borrower owes $10,000 at a fixed rate. After a year of 8% inflation, what is the debt worth in last year's prices (nearest $)?", 9259, "10,000 ÷ 1.08 ≈ <b>$9,259</b>.", None, 1),
]) + mcq_js("qz1", [
    ("Who is most likely to gain from unexpected inflation?", ["A saver", "A pensioner on a fixed income", "A borrower with a fixed-rate loan", "A lender with a fixed-rate loan"], 2, "The real value of the debt falls."),
    ("The real interest rate is:", ["Nominal rate + inflation", "Nominal rate − inflation", "Inflation − nominal rate", "The base rate"], 1, "Adjust for inflation."),
    ("A consequence of high inflation for exporters is:", ["Exports become more competitive", "Exports become less competitive if inflation is higher than rivals'", "No effect", "Exports are always higher"], 1, "Prices rise relative to competitors'."),
    ("A harmful effect of deflation is:", ["People delay spending", "Prices rise", "Debt falls", "Savers lose"], 0, "Expecting lower prices, they wait."),
    ("A benefit of low inflation is:", ["Uncertainty", "Higher interest rates", "Price stability that encourages investment", "Lower exports"], 2, "Certainty helps firms plan."),
]) + "\n" + cards_js([("Real interest rate", "The nominal interest rate minus the inflation rate."), ("Nominal interest rate", "The interest rate before adjusting for inflation."), ("Real wage", "Wages adjusted for inflation: what pay can actually buy."), ("Menu costs", "The costs to firms of changing prices."), ("Fixed income", "Income that does not change with prices, such as some pensions."), ("Price competitiveness", "How cheap a country's goods are compared with those of rivals."), ("Redistribution by inflation", "Inflation moves wealth from lenders and savers to borrowers."), ("Debt deflation", "When falling prices raise the real value of debts."), ("Hyperinflation", "Extremely rapid inflation that destroys confidence in money.")]) + "labR();\n"
explore = '''
  <h2>Lab 1 · The real interest rate</h2>
  <p>Set an interest rate and an inflation rate. See who gains: savers or borrowers.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Real interest rate</small><strong id="ra1"></strong></div><div><small>Real gain on $10,000 saved</small><strong id="ra2"></strong></div><div><small>Gainers</small><strong id="ra3"></strong></div></div><div class="verdict" id="rav"></div></div></div>
    <svg id="labR" viewBox="0 0 760 340" role="img" aria-label="Nominal interest, inflation and the real interest rate"></svg>
  </div>

  <h2>Lab 2 · Who gains and who loses?</h2>
  <p>Pick a group to see how inflation may affect it.</p>
  <div class="card"><div class="row" id="wgBtns"></div><div id="wgOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain how inflation could affect savers and borrowers.", "Real interest rate: if inflation above interest rate, savers lose and borrowers gain.",
      "[K|If inflation is higher than the interest rate, the real interest rate is negative.] [N|Savers lose because the money in their accounts buys less than before.] [N|Borrowers gain because they repay loans in money that is worth less, so the real value of their debt falls.] [A|For example, a saver with 3% interest and 5% inflation loses about 2% of purchasing power.]"),
    Q(2, "Explain", 4, "Explain two consequences of deflation. (May/June 2020, P21)", "Reduced demand, unemployment, recession, real debt; or lower costs and exports.",
      "[K|Output may fall.] [N|If prices fall because of lower demand, firms cut production as sales and profits fall.] [K|Unemployment may rise.] [N|With less output, firms need fewer workers, so jobs could be lost and a recession may follow.]"),
    Q(3, "Analyse", 6, "Analyse the advantages of a low rate of inflation. (May/June 2021, P21)", "Purchasing power, certainty and investment, competitiveness, savings. Credit employment once.",
      "[K|Low inflation means prices are rising only slowly.] [N|Purchasing power is not eroded much, so wages may keep pace with prices and savings keep their value.] [N|There is more certainty, so firms are more willing to invest, which could raise output and employment.] [N|The country's goods could be more price competitive than those of countries with higher inflation, so exports could rise and imports fall, improving the current account.]", key=True),
    Q(4, "Explain", 4, "Explain two reasons why a low inflation rate may increase a country's economic growth rate. (Oct/Nov 2023, P22)", "Certainty and investment; competitiveness and exports; spending power.",
      "[K|A low inflation rate creates certainty.] [N|Firms can plan and are more likely to invest, which increases total demand and productive capacity, raising growth.] [K|It also helps price competitiveness.] [N|If prices rise more slowly than abroad, exports are cheaper and may rise, raising AD and growth.]"),
    Q(5, "Discuss", 8, "Discuss whether or not inflation will harm a country's firms. (Feb/Mar 2025, P22)", "Both sides. Harm: higher costs, uncertainty, menu costs, exports less competitive, wage demands. Not harm: prices may rise faster than costs, debts eased, low inflation helps. End with 'depends on the rate'.",
      "[K|Inflation is a sustained rise in the general price level.] [N|It could harm firms by raising their costs of production, such as wages and raw materials, which may reduce profits if they cannot pass them on.] [N|Uncertainty may reduce investment, firms face menu costs of changing prices, and if inflation is higher than competitors' abroad their exports could become less competitive.] [E|These effects are larger the higher and more unpredictable inflation is.] [N|However, firms may gain if their prices rise faster than their costs, and borrowing firms see the real value of their debts fall.] [N|Low, stable inflation can give firms the confidence to invest and may raise demand.] [E|Overall, high inflation is likely to harm most firms, particularly exporters, but low and stable inflation is unlikely to do so. It depends on the rate, whether it is expected, and whether firms can raise their prices.]", key=True),
    Q(6, "Discuss", 8, "Discuss whether or not inflation is always a disadvantage to an economy. (May/June 2022, P23)", "'Always' invites 'not always'. Disadvantages and when it might be helpful (borrowers, growth, low and stable).",
      "[K|Inflation is a sustained rise in the general price level.] [N|It can be a disadvantage because it reduces the purchasing power of savers and people on fixed incomes, raises firms' costs, creates uncertainty and can make exports less competitive.] [N|High inflation could redistribute income unfairly and reduce growth.] [E|However, it is not always a disadvantage.] [N|Low, stable inflation can accompany growth and falling unemployment, borrowers gain as the real value of their debt falls, and firms may see profits rise if prices rise faster than costs.] [E|Overall, high or unpredictable inflation is mostly harmful, but low inflation (around 2%) is not always a problem and may be a sign of a healthy economy.]", key=True),
    Q(7, "Discuss", 8, "Discuss whether or not deflation will benefit an economy. (Oct/Nov 2020, P23)", "For: cheaper goods, lower costs, exports competitive. Against: delayed spending, falling profits, unemployment, real debt, recession.",
      "[K|Deflation is a sustained fall in the general price level.] [N|It could benefit consumers by raising the purchasing power of their money, and if it is caused by lower costs or better technology, firms could produce more cheaply and exports could become more competitive.] [N|However, deflation caused by weak demand is likely to harm the economy, as consumers delay spending, firms' profits fall, and jobs are cut.] [N|The real value of debts rises, which hurts borrowers and could cause defaults.] [E|Overall, deflation is more likely to harm an economy, especially if it is caused by falling demand, although a mild fall caused by productivity gains could be beneficial.]", key=True),
)
tp = tips([
    ("Real interest rate = nominal − inflation.", "Savers lose when it is negative; borrowers gain."),
    ("Always say who gains and who loses.", "Savers, lenders, borrowers, workers, firms, exporters."),
    ("Link inflation to competitiveness.", "Higher than rivals' inflation hurts exports."),
    ("Say whether inflation is high, low, expected.", "Effects depend on the level and predictability."),
    ("Deflation can be harmful.", "Delayed spending, real debt, falling profits."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("4.7.4 Consequences of inflation"), "Consequences of Inflation", "How inflation affects savers, lenders and borrowers, consumers, workers, firms and the economy, and the effects of deflation. Syllabus 4.7.4.",
    learn=learn, watch=watch(("What inflation does to savings", "stS"), ("Inflation and international competitiveness", "stX")), explore=explore,
    practise=practise(("Who gains and who loses?", "cl1", "card"), ("Inflation or deflation?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the deflation chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Savers in the 1970s", "Inflation was above interest rates in several countries in the 1970s, so savers lost purchasing power while borrowers, including home buyers, gained.", "Real interest rates and redistribution."),
        rw("Wage demands in 2022-23", "As prices rose quickly, workers in many sectors went on strike for higher pay to protect their real wages.", "Consequences for workers and the wage-price spiral."),
        rw("Japan's lost decades", "Prolonged deflation in Japan made consumers delay purchases and raised the real burden of debt, contributing to weak growth.", "Consequences of deflation."),
        rw("Venezuela's hyperinflation", "Inflation of many thousand per cent destroyed savings and made it hard for firms to plan, and many people left the country.", "Extreme consequences for savers, firms and the economy.")),
    exam=ex, tips=tp)
write("in4", body, js, "Consequences of Inflation", "ig-inflation-consequences")

# =========================================================== 4.7.5 Policies
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The range of policies to control inflation includes <b>monetary policy</b> (raise interest rates, reduce the money supply, raise the exchange rate), <b>fiscal policy</b> (cut government spending, raise taxes) and <b>supply-side policy</b> (raise productivity and cut costs). The right policy depends on the <b>cause</b>: demand-side policy targets demand-pull inflation, while supply-side policy and a stronger exchange rate target cost-push inflation. Every policy has costs, such as lost output and jobs.</p></div>

  <h2>The range of policies</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>How it reduces inflation</th><th>Best for</th></tr>
    <tr><td><b>Raise interest rates</b> (central bank)</td><td>Borrowing dearer, saving rewarded: consumption and investment fall, AD shifts left</td><td>Demand-pull</td></tr>
    <tr><td><b>Reduce the money supply</b></td><td>Less lending and spending: AD shifts left</td><td>Demand-pull</td></tr>
    <tr><td><b>Allow the exchange rate to rise</b></td><td>Imports and raw materials become cheaper, and exports dearer: costs fall, AD falls</td><td>Cost-push (imported)</td></tr>
    <tr><td><b>Raise taxes</b> (income tax) or <b>cut government spending</b></td><td>Lower disposable income and G: AD shifts left</td><td>Demand-pull</td></tr>
    <tr><td><b>Supply-side policy</b> (training, infrastructure, competition, deregulation)</td><td>Raise productivity and lower costs: AS shifts right</td><td>Cost-push, and long-run</td></tr>
    <tr><td><b>Controls on wages and prices</b></td><td>Limit increases directly</td><td>Wage-price spiral (but difficult)</td></tr>
  </table></div>
  <p><b>To avoid deflation</b> a central bank can do the opposite: cut interest rates, increase the money supply (for example quantitative easing), and governments can raise spending or cut taxes.</p>

  <h2>Effectiveness and costs</h2>
  <div class="grid2">
    <div class="card"><h3>Demand-side policy</h3><ul><li><b>Pros:</b> can act fairly quickly; effective against excess demand.</li><li><b>Cons:</b> lower output and <b>higher unemployment</b> (a conflict of aims); time lags; weak against cost-push inflation.</li></ul></div>
    <div class="card"><h3>Supply-side policy</h3><ul><li><b>Pros:</b> lowers costs without cutting output; gives growth and low inflation together.</li><li><b>Cons:</b> slow and costly; uncertain results.</li></ul></div>
  </div>
  <ul>
    <li><b>Higher interest rates</b> hurt borrowers and may cut the investment that raises capacity.</li>
    <li><b>A higher exchange rate</b> makes exports dearer and may worsen the current account.</li>
    <li><b>Higher taxes or lower spending</b> are politically difficult.</li>
    <li><b>Wage and price controls</b> are hard to enforce and distort markets.</li>
    <li>Policy must match the cause: raising interest rates does little against a supply shock such as an oil price rise.</li>
    <li><b>Expectations</b> matter: credible central banks with inflation targets can hold inflation down more easily.</li>
  </ul>
'''
js = HEAD + COMMON + '''
Lib.stepper($("#stD"), { w: 760, h: 400, label: "Contractionary policy against demand-pull inflation", base: { sh: 14, a: 0 }, draw: adasChart, steps: [
  { cap: "Excess demand has pushed AD to the <b>right</b>. The price level is rising: <b>demand-pull inflation</b>.", s: { sh: 30, a: 0 } },
  { cap: "The central bank <b>raises interest rates</b> and the government cuts spending or raises taxes. <b>AD shifts back to the left</b>.", s: { sh: 14, a: 0 } },
  { cap: "The price level stops rising (or rises more slowly): inflation falls. <b>Evaluate:</b> output also falls, so <b>unemployment may rise</b>. That is the cost of controlling demand-pull inflation.", s: { sh: 0, a: 0 } },
] });
const IR = ["Central bank raises the interest rate", "Borrowing costs more and saving pays more", "Consumption and investment fall", "The currency may rise, so imports are cheaper", "AD shifts left and costs fall", "Inflation falls, but output and jobs are at risk"];
Lib.stepper($("#stR"), { w: 760, h: 400, label: "How higher interest rates reduce inflation", base: { n: 0 }, draw: mkChain(IR, "--accent"), steps: chainSteps(["The central bank <b>raises interest rates</b>.", "Borrowing costs more and <b>saving pays more</b>.", "<b>Consumption and investment fall</b>.", "The <b>currency may rise</b>, making imports and raw materials cheaper.", "<b>AD shifts left</b> and costs fall.", "<b>Inflation falls</b>. Evaluate: growth slows, unemployment may rise, and borrowers suffer."]) });
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Supply-side policy against cost-push inflation", base: { sh: 0, a: -12 }, draw: adasChart, steps: [
  { cap: "Rising costs have shifted AS <b>left</b>: output has fallen and prices have risen: <b>cost-push inflation</b>.", s: { sh: 0, a: -12 } },
  { cap: "The government invests in <b>training, infrastructure and competition</b>. Productivity rises and firms' costs fall.", s: { sh: 0, a: 0 } },
  { cap: "AS shifts <b>right</b>: output rises and the price level falls. <b>Evaluate:</b> it works slowly and costs money, but it does not cost jobs.", s: { sh: 0, a: 12 } },
] });

/* Lab 1: policy simulator */
function labP() {
  if (!$("#pa") || !$("#pb")) return;
  const pol = +$("#pa").value, sup = +$("#pb").value, sh0 = 24, [y0, p0] = solve2(sh0, 0), [y, p] = solve2(sh0 - pol, sup);
  $("#pa1").textContent = (p - p0 >= 0 ? "+" : "−") + money(Math.abs(p - p0), 1); $("#pa2").textContent = (y - y0 >= 0 ? "+" : "−") + money(Math.abs(y - y0), 1); $("#pa3").textContent = money(p, 1);
  $("#pav").textContent = pol === 0 && sup === 0 ? "The economy starts overheated: AD has shifted +24 and the price level is high. Choose a policy." : pol > 0 && sup === 0 ? `Contractionary policy cuts AD by ${pol}: the price level falls by ${money(p0 - p, 1)}, but output falls by ${money(y0 - y, 1)}, so jobs may be lost.` : pol === 0 ? `Supply-side policy raises AS by ${sup}: the price level changes by ${p - p0 >= 0 ? "+" : "−"}${money(Math.abs(p - p0), 1)} and output rises by ${money(y - y0, 1)}. It does not cost output, but it takes years.` : `A mix: the price level falls by ${money(p0 - p, 1)} and output changes by ${y - y0 >= 0 ? "+" : "−"}${money(Math.abs(y - y0), 1)}.`;
  let o = axes("Price level", "Real GDP") + SV.path(ptsPath([[QX(sup), PY(30)], [QX(60 + sup), PY(54)], [QX(87.7 + sup), PY(115)]]), "c3") + SV.text(QX(87.7 + sup) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90 + 0.8 * sh0, "c1", "AD", { t: "t1", attrs: { opacity: pol ? 0.4 : 1 } }); if (pol) o += adLine(90 + 0.8 * (sh0 - pol), "c4", "AD₁", { t: "t4" });
  o += hline(p0, "gr", y0) + vline(y0, p0) + SV.circle(QX(y0), PY(p0), 6, "dot1", { opacity: 0.5 }) + ylab(p0, "P", "sm bd") + xlab(y0, "Y", "sm bd");
  if (pol || sup) o += hline(p, "gr", y) + vline(y, p) + SV.circle(QX(y), PY(p), 6, "dot2") + ylab(p, "P₁", "sm bd") + xlab(y, "Y₁", "sm bd");
  $("#labP").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pa", label: "Contractionary demand-side policy (AD shift left)", min: 0, max: 30, step: 2, value: 12, fmt: (v) => "−" + v, onInput: labP });
Lib.slider($("#g2"), { id: "pb", label: "Supply-side policy (AS shift right)", min: 0, max: 24, step: 2, value: 0, fmt: (v) => "+" + v, onInput: labP });
/* Lab 2: which policy for which cause */
const TYPES = ["Demand-pull", "Cost-push: wages", "Cost-push: imports (weak currency)"], POLS = ["Raise interest rates", "Cut spending or raise taxes", "Supply-side policy (training, competition)", "Let the exchange rate rise", "Wage and price controls"];
const RATE = [[3, 1, 1], [3, 1, 0], [1, 3, 2], [1, 1, 3], [1, 2, 1]];
const NOTE = [["Cuts spending and AD, tackling excess demand.", "Reduces spending but does not lower wage costs; may cause unemployment.", "A higher rate can raise the exchange rate, which lowers import prices: some help."], ["Directly reduces demand-pull pressure.", "May reduce pressure on wages if unemployment rises, but a blunt tool.", "Does not address imported costs."], ["Raising capacity eases demand-pull pressure only slowly.", "Productivity gains offset wage rises: lowers unit labour costs.", "Competition and domestic substitutes reduce reliance on imports."], ["Lower import prices help a little but also reduce exports.", "Little effect on wages.", "Directly lowers the cost of imported inputs and goods."], ["Cannot easily control spending.", "Limits wage growth directly, but hard to enforce and may cause disputes.", "Cannot control world prices."]];
const RL = ["Little effect", "Some help", "Moderate help", "Very effective"];
let selT = 0, selP = 0;
function showMatrix() {
  $("#mxT").innerHTML = TYPES.map((t, j) => `<button class="b${j === selT ? " pri" : ""}" data-j="${j}">${t}</button>`).join("");
  $("#mxP").innerHTML = POLS.map((t, j) => `<button class="b${j === selP ? " pri" : ""}" data-j="${j}">${t}</button>`).join("");
  $$("#mxT .b").forEach((b) => (b.onclick = () => { selT = +b.dataset.j; showMatrix(); }));
  $$("#mxP .b").forEach((b) => (b.onclick = () => { selP = +b.dataset.j; showMatrix(); }));
  const r = RATE[selP][selT];
  $("#mxOut").innerHTML = `<div class="verdict"><b>${POLS[selP]}</b> against <b>${TYPES[selT].toLowerCase()}</b> inflation: <b>${RL[r]}</b>. ${NOTE[selP][selT]}</div>`;
}
showMatrix();

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>monetary</b>, <b>fiscal</b> or <b>supply-side</b> way to control inflation?", buckets: [{ label: "Monetary" }, { label: "Fiscal" }, { label: "Supply-side" }], items: [
  { text: "Raise the interest rate", b: 0 }, { text: "Reduce the money supply", b: 0 }, { text: "Let the currency rise", b: 0 },
  { text: "Raise income tax", b: 1 }, { text: "Cut government spending", b: 1 },
  { text: "Train workers to raise productivity", b: 2 }, { text: "Increase competition between firms", b: 2 }, { text: "Improve infrastructure to cut firms' costs", b: 2 },
], done: "Match the type of policy to how it works." });
Lib.classify($("#cl2"), { prompt: "Which type of inflation does each policy mainly address?", buckets: [{ label: "Demand-pull" }, { label: "Cost-push" }], items: [
  { text: "Higher interest rates", b: 0 }, { text: "Higher taxes", b: 0 }, { text: "Cutting government spending", b: 0 },
  { text: "Training that raises productivity", b: 1 }, { text: "A stronger currency lowering import costs", b: 1 }, { text: "Deregulation lowering firms' costs", b: 1 },
], done: "Demand-pull: cut demand. Cost-push: cut costs." });
Lib.match($("#m1"), { prompt: "Match the policy to its main weakness.", pairs: [
  ["Raise interest rates", "Raises unemployment and hurts borrowers"],
  ["Cut government spending", "Reduces services and jobs"],
  ["Raise income tax", "Politically unpopular; may reduce work incentives"],
  ["Let the currency rise", "Makes exports dearer"],
  ["Supply-side policy", "Slow and costly"],
  ["Wage and price controls", "Hard to enforce and distorts markets"],
], done: "Every policy needs an evaluation point." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a rise in income tax could reduce demand-pull inflation</b>.", items: [
  "The government raises income tax",
  "Households' disposable income falls",
  "Consumption falls",
  "Aggregate demand shifts left",
  "Demand-pull pressure on prices eases",
], done: "A fiscal policy chain." });
''' + calc_js([
    ("Inflation is 8% and the central bank wants 2%. By how many percentage points does it need to fall?", 6, "8 − 2 = <b>6 percentage points</b>.", None, None),
    ("The CPI is 105 and the inflation target is 2%. What CPI would match 2% next year?", 107.1, "105 × 1.02 = <b>107.1</b>.", None, 0.1),
    ("A tax rise cuts consumption by $12bn and the multiplier is 1.5. By how much does AD fall ($bn)?", 18, "12 × 1.5 = <b>$18bn</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which policy is most likely to reduce demand-pull inflation?", ["Cutting interest rates", "Raising interest rates", "Increasing government spending", "Cutting taxes"], 1, "Higher rates reduce spending."),
    ("Which policy would best reduce cost-push inflation caused by low productivity?", ["Raising interest rates", "Supply-side policy such as training", "Cutting benefits", "Raising taxes"], 1, "Higher productivity lowers costs."),
    ("A disadvantage of raising interest rates to control inflation is:", ["Lower unemployment", "Slower growth and possible higher unemployment", "Higher spending", "Lower saving"], 1, "AD falls, so output may fall."),
    ("A central bank could avoid deflation by:", ["Raising interest rates", "Cutting interest rates and increasing the money supply", "Cutting government spending", "Raising the exchange rate"], 1, "Expansionary monetary policy."),
    ("A higher exchange rate may reduce inflation because:", ["Imports become cheaper", "Exports rise", "Wages fall", "Spending rises"], 0, "Import costs fall."),
]) + "\n" + cards_js([("Contractionary policy", "Policy that reduces aggregate demand, such as higher interest rates or higher taxes."), ("Inflation target", "A rate of inflation that the central bank aims to achieve, often 2%."), ("Monetary policy", "Interest rates, money supply and exchange rate used to influence AD and inflation."), ("Fiscal policy", "Government spending and taxation used to influence AD."), ("Supply-side policy", "Measures to raise productive capacity and lower costs."), ("Price controls", "Government limits on how much prices can rise."), ("Central bank independence", "When a central bank sets interest rates without political interference."), ("Quantitative easing", "A central bank buying bonds to increase the money supply."), ("Time lag", "The delay between a policy change and its effect.")]) + "labP(); showMatrix();\n"
explore = '''
  <h2>Lab 1 · Cooling an overheated economy</h2>
  <p>AD has shifted right by 24 and prices are high. Use contractionary demand-side policy, supply-side policy, or both, and see the effect on prices and output.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Change in price level</small><strong id="pa1"></strong></div><div><small>Change in real GDP</small><strong id="pa2"></strong></div><div><small>Price level now</small><strong id="pa3"></strong></div></div><div class="verdict" id="pav"></div></div></div>
    <svg id="labP" viewBox="0 0 760 400" role="img" aria-label="Aggregate demand and supply diagram"></svg>
  </div>

  <h2>Lab 2 · Which policy for which cause?</h2>
  <p>Choose a type of inflation and a policy to see how effective the policy is likely to be.</p>
  <div class="card"><p><b>Cause of inflation</b></p><div class="row" id="mxT"></div><p style="margin-top:14px"><b>Policy</b></p><div class="row" id="mxP"></div><div id="mxOut" style="margin-top:14px"></div></div>
'''
ex = exam(
    Q(1, "Analyse", 6, "Analyse how a central bank could reduce inflation. (Feb/Mar 2021, P22)", "Contractionary monetary policy: interest rates, money supply, exchange rate. Chain each. Avoid a list.",
      "[K|A central bank could use contractionary monetary policy.] [N|If it raises the interest rate, borrowing becomes dearer and saving more attractive, so households cut consumption and firms cut investment.] [N|Lower total demand reduces demand-pull inflation.] [N|It could also reduce the money supply, for example by selling government bonds, which restricts bank lending and spending.] [N|A higher interest rate may raise the exchange rate, lowering the price of imports and reducing cost-push inflation.] [E|However, it can slow growth and raise unemployment.]", key=True),
    Q(2, "Analyse", 6, "Analyse how an increase in income tax can affect a country's inflation rate. (May/June 2022, P21)", "Lower disposable income, lower consumption, AD left, lower inflation. Mention possible cost effect and unemployment.",
      "[K|An increase in income tax reduces households' disposable income.] [N|Consumption is likely to fall, so aggregate demand shifts left, reducing demand-pull inflationary pressure.] [N|Workers may also demand higher gross wages to keep their take-home pay, which raises firms' costs and could cause cost-push inflation.] [E|The net effect depends on whether demand-pull or cost-push dominates.]", key=True),
    Q(3, "Explain", 4, "Explain how a decrease in borrowing could reduce the chance of high inflation. (May/June 2021, P23)", "Less borrowing, less spending, AD falls, demand-pull falls.",
      "[K|If borrowing falls, households and firms have less money to spend and invest.] [N|Consumption and investment fall, so aggregate demand is lower.] [N|With less demand pressure, firms are less likely to raise prices, so demand-pull inflation is less likely.]"),
    Q(4, "Analyse", 6, "Analyse how an increase in a country's foreign exchange rate could reduce inflation. (Oct/Nov 2023, P23)", "Imports cheaper; raw materials; exports dearer reduces AD; competition.",
      "[K|A higher exchange rate makes imports cheaper in the home currency.] [N|Imported raw materials and components cost firms less, so costs of production fall and AS may shift right.] [N|Cheaper imported consumer goods directly lower the price level, and increased competition from imports may force domestic firms to hold prices down.] [N|Exports become dearer, so net exports fall and AD shifts left, reducing demand-pull inflation.] [E|However, exports and jobs may suffer.]", key=True),
    Q(5, "Analyse", 6, "Analyse how a central bank could avoid deflation. (May/June 2021, P21)", "Expansionary monetary policy: lower rates, more money, lower exchange rate. Chain.",
      "[K|A central bank could use expansionary monetary policy.] [N|It could cut interest rates, so borrowing is cheaper and saving less attractive, raising consumption and investment.] [N|It could increase the money supply, for example by buying bonds, giving banks more to lend.] [N|It might allow the exchange rate to fall, making exports cheaper and imports dearer.] [N|These raise aggregate demand, so the price level is less likely to fall.]", key=True),
    Q(6, "Discuss", 8, "Discuss whether or not an increase in the rate of income tax will reduce inflation. (Oct/Nov 2020, P22)", "For: lower disposable income, lower AD. Against: cost-push if wages rise, effect weak, saving rather than spending, unemployment, time lag.",
      "[K|Inflation is a sustained rise in the general price level and an increase in income tax is contractionary fiscal policy.] [N|Higher income tax reduces households' disposable income, so consumption could fall and aggregate demand could shift left.] [N|This reduces demand-pull inflation, particularly if the economy is close to full capacity.] [E|It is likely to work best when inflation is caused by excess demand.] [N|However, if inflation is cost-push, a tax rise will not lower firms' costs, and workers might demand higher wages, which could raise costs further.] [N|Households could also cut saving rather than spending, so the effect may be small, and lower demand could raise unemployment.] [E|Overall, a tax rise could reduce demand-pull inflation but it is unlikely to help with cost-push inflation, so the effect depends on the cause and the state of the economy.]", key=True),
    Q(7, "Discuss", 8, "Discuss whether or not a cut in the interest rate will reduce inflation. (Oct/Nov 2024, P23)", "A cut normally raises AD, so inflation could rise; but if cost-push or it lowers firms' costs (borrowing costs), or the currency effect... evaluate.",
      "[K|A cut in the interest rate makes borrowing cheaper and saving less attractive.] [N|This is likely to raise consumption and investment, so aggregate demand could shift right and demand-pull inflation could increase, so a cut in the interest rate is more likely to raise inflation than reduce it.] [N|A lower exchange rate could also raise import prices.] [E|However, a cut could reduce firms' borrowing costs, which could lower their costs of production, and investment may raise capacity over time, which could reduce inflation.] [N|If the economy is in recession or deflation, a cut could raise demand towards a normal level and avoid deflation.] [E|Overall, a cut is more likely to raise inflation in the short run, except where it helps supply or the economy has spare capacity.]", key=True),
)
tp = tips([
    ("Match policy to cause.", "Demand-pull: cut demand. Cost-push: cut costs, supply-side, stronger currency."),
    ("Name the policy precisely.", "Raise interest rates, cut the money supply, raise taxes, cut spending."),
    ("Use chains, not lists.", "Cambridge limits list-style answers to half marks."),
    ("Evaluate.", "Unemployment, time lags, borrowers hurt, exports less competitive, wrong cause."),
    ("To avoid deflation, do the opposite.", "Cut interest rates, increase the money supply."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("4.7.5 Policies to control inflation"), "Policies to Control Inflation", "Monetary, fiscal and supply-side policies to control inflation, matched to the cause, and how effective they are. Syllabus 4.7.5.",
    learn=learn, watch=watch(("Contractionary policy against demand-pull inflation", "stD"), ("How higher interest rates reduce inflation", "stR"), ("Supply-side policy against cost-push inflation", "stS")), explore=explore,
    practise=practise(("Monetary, fiscal or supply-side?", "cl1", "card"), ("Which type of inflation?", "cl2", "card"), ("Match the policy to its weakness", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Rate rises in 2022-23", "The US Federal Reserve, the Bank of England and the European Central Bank raised interest rates in a series of steps to bring inflation back towards 2%. Mortgage costs rose and growth slowed.", "Contractionary monetary policy and its costs."),
        rw("Inflation targeting", "Many central banks have a target, such as 2%, and independence to set interest rates. This helps people expect low inflation, which makes it easier to achieve.", "Why credibility and expectations matter."),
        rw("Austerity to control prices", "Some countries cut spending and raised taxes during high inflation. Inflation fell but unemployment rose.", "Fiscal contraction and its trade-off."),
        rw("Price controls", "Some governments have capped the prices of fuel, bread or rents to limit inflation. Shortages and black markets often followed.", "Direct controls and their drawbacks.")),
    exam=ex, tips=tp)
write("in5", body, js, "Policies to Control Inflation", "ig-inflation-policies")
