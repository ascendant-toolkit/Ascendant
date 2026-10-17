"""AS syllabus 4.4.1-4.4.3 Economic growth: meaning, measurement, nominal and real GDP. Run: python3 tools/artifact-kit/mk_as46.py"""
from asx import *
EY = EYAS("4.4.1 to 4.4.3")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Economic growth</b> is an <b>increase in the real value of the goods and services an economy produces over time</b>, usually measured as the <b>percentage change in real GDP</b> from one period to the next (actual growth), while an outward shift of the production possibility curve or LRAS is growth in <b>potential output</b>. <b class="kw">Nominal GDP</b> is measured at <b>current prices</b>, so it rises with both output and inflation; <b class="kw">real GDP</b> is adjusted for <b>inflation</b> using a price index such as the <b>GDP deflator</b>, so it shows only the change in output. <b>Negative economic growth</b> is a fall in real GDP, and a <b>recession</b> is usually defined as two or more consecutive quarters of falling real GDP. GDP per head, adjusted for prices, is used to compare <b>living standards</b>, though it has limits.</p></div>

  <h2>1 · Meaning and measurement (4.4.1 to 4.4.2)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Growth rate</b> = (real GDP this year − real GDP last year) ÷ real GDP last year × 100.</li>
    <li><b>Actual growth:</b> a rise in real output as spare capacity is used (a movement towards the PPC or AD rising); <b>potential growth:</b> an increase in productive capacity (the PPC or LRAS shifting outwards).</li>
    <li><b>Negative growth</b> is a fall in real GDP; a <b>recession</b> is two consecutive quarters of falling real GDP.</li>
    <li><b>Per capita:</b> real GDP ÷ population shows the average output per person, a better guide to <b>living standards</b>. GDP can grow while GDP per head falls if the population grows faster.</li>
    <li><b>Limits of GDP as a measure:</b> it ignores the <b>informal economy</b>, unpaid work, <b>income distribution</b>, environmental damage and leisure; comparisons across countries depend on exchange rates and different price levels.</li>
  </ul>

  <h2>2 · Nominal and real GDP (4.4.3)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Nominal (money) GDP</th><th>Real GDP</th></tr>
    <tr><td><b>Prices used</b></td><td>Current prices</td><td>Constant (base-year) prices</td></tr>
    <tr><td><b>Changes with</b></td><td>Output and prices</td><td>Output only</td></tr>
    <tr><td><b>Calculation</b></td><td>Value of output at today's prices</td><td>Nominal GDP ÷ price index × 100</td></tr>
    <tr><td><b>Use</b></td><td>Size of the economy in money terms</td><td>Measuring growth and living standards</td></tr>
  </table></div>
  <ul>
    <li><b>Example:</b> nominal GDP rises from $500bn to $577.5bn while prices rise 5%. Real GDP = 577.5 ÷ 1.05 = <b>$550bn</b>, so real growth is 10%.</li>
    <li>Approximately: <b>real growth ≈ nominal growth − inflation</b>.</li>
    <li>If nominal GDP rises by less than the rate of inflation, <b>real GDP falls</b>.</li>
  </ul>

  <h2>3 · Worked examples</h2>
  <p><b>Calculating real growth.</b> The table gives nominal GDP and a GDP deflator (price index, base year = 100).</p>
  <div class="tw"><table class="t">
    <tr><th>Year</th><th>Nominal GDP ($bn)</th><th>Price index</th><th>Real GDP ($bn)</th><th>Real growth</th></tr>
    <tr><td>1</td><td>200</td><td>100</td><td>200</td><td>–</td></tr>
    <tr><td>2</td><td>220</td><td>109</td><td>201.8</td><td>+0.9%</td></tr>
    <tr><td>3</td><td>240</td><td>125</td><td>192.0</td><td>−4.9%</td></tr>
    <tr><td>4</td><td>300</td><td>149</td><td>201.3</td><td>+4.9%</td></tr>
  </table></div>
  <ul>
    <li>Nominal GDP rises every year, but real GDP <b>falls in year 3</b> because prices rose by 14.7% (109 to 125) while nominal GDP rose by only 9.1%. Always deflate before judging growth.</li>
    <li><b>Real GDP = nominal GDP ÷ price index × 100.</b> Year 2: 220 ÷ 109 × 100 = 201.8. <b>Real growth</b> = (201.8 − 200) ÷ 200 = 0.9%.</li>
    <li><b>Quick check:</b> real growth ≈ nominal growth − inflation. Year 2: nominal 10%, inflation 9%, so growth ≈ 1%.</li>
  </ul>
  <p><b>GDP per head.</b> If real GDP rises 3% and the population rises 1%, GDP per head rises by about 2%. If the population rises 4%, GDP per head falls by about 1%, even though total GDP is growing.</p>

  <h2>4 · Actual and potential growth</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Actual growth</th><th>Potential growth</th></tr>
    <tr><td><b>Meaning</b></td><td>Increase in real GDP: output actually produced</td><td>Increase in the economy's productive capacity</td></tr>
    <tr><td><b>Diagram</b></td><td>A move towards (or along) the PPC; AD shifts right along SRAS</td><td>Outward shift of the PPC; LRAS shifts right</td></tr>
    <tr><td><b>Causes</b></td><td>Higher AD using spare capacity</td><td>More and better factors of production, technology</td></tr>
    <tr><td><b>Limit</b></td><td>Cannot go beyond potential for long without inflation</td><td>Slow and costly to achieve</td></tr>
  </table></div>
  <ul>
    <li>The <b>output gap</b> is the difference between actual and potential output. A negative gap means spare capacity; a positive gap means output above sustainable levels.</li>
  </ul>

  <h2>5 · The business cycle</h2>
  <ul>
    <li><b>Boom:</b> fast growth, falling unemployment, rising inflation and demand for imports.</li>
    <li><b>Slowdown:</b> growth continues but more slowly.</li>
    <li><b>Recession:</b> two or more consecutive quarters of falling real GDP; unemployment rises and inflation falls.</li>
    <li><b>Recovery:</b> real GDP begins to rise again, initially using spare capacity.</li>
    <li>Real GDP tends to follow a <b>trend of long-run growth</b> with cyclical fluctuations around it.</li>
  </ul>

  <h2>6 · Using GDP to compare living standards: limits</h2>
  <ul>
    <li><b>Population:</b> use per capita figures.</li>
    <li><b>Prices:</b> use real figures; compare countries using purchasing power adjustments, since exchange rates do not reflect local prices.</li>
    <li><b>Distribution:</b> an average hides inequality.</li>
    <li><b>Unrecorded output:</b> informal activity and unpaid work are missed.</li>
    <li><b>Quality of life:</b> health, leisure, education and the environment are not captured (indicators such as the Human Development Index try to include some).</li>
    <li><b>Composition:</b> output of weapons or the cost of repairing disasters counts as GDP but does not raise welfare.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>When asked to calculate growth, make sure you are using <b>real</b> figures. Show the formula and the steps: deflate first, then find the percentage change.</div>
'''

watch = '''
  <h2>1 · Nominal growth, inflation and real growth</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stR"></div>
  <h2>2 · The business cycle</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Deflate nominal GDP</h2>
  <p>Enter nominal GDP in two years and the price index. See real GDP and real growth.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Real GDP year 2</small><strong id="r1"></strong></div><div><small>Nominal growth</small><strong id="r2"></strong></div><div><small>Real growth</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of nominal and real GDP for two years"></svg></div></div></div>

  <h2>Lab 2 · GDP per head</h2>
  <p>Real GDP growth and population growth together decide growth in GDP per head.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>GDP growth</small><strong id="t1"></strong></div><div><small>Population growth</small><strong id="t2"></strong></div><div><small>GDP per head</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Bars comparing GDP and population growth"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Nominal or real?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the steps for finding real growth in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Prices up, output flat", "A country's nominal GDP rises 6% in a year, but prices also rise 6%. Real GDP is unchanged: the economy produced the same amount, and the extra money value only reflects higher prices.", "nominal versus real GDP.") +
rw("A recession", "Real GDP falls for two successive quarters as spending drops. Firms cut output and jobs, and unemployment rises. Economists call this a recession, a period of negative growth.", "negative growth and its definition.") +
rw("Fast GDP growth, fast population growth", "An economy grows 3% a year, but its population grows 3% as well. GDP per head does not rise, so average living standards are unchanged even though total output is larger.", "why per capita figures matter.") +
rw("The informal economy", "In many developing countries much work is done for cash or at home and never recorded. Official GDP therefore understates output, which makes growth hard to measure accurately.", "limits of GDP as a measure.") +
rw("Nominal growth that is only inflation", "A country reports a 15% rise in nominal GDP, but prices rose 14%. Real GDP grew by about 1%, so output hardly changed.", "real versus nominal GDP.") +
rw("A recession", "During a recession real GDP falls for two or more quarters, firms cut jobs and investment, and unemployment rises. Governments often respond with expansionary policy.", "negative growth and its consequences.")
)

mc_exam = [
  mcq("m23_12", 29, "The table shows GDP indices over three years: real GDP 100, 105, 106 and money GDP 100, 107, 115 (years 1 to 3). Inflation and economic growth are two macroeconomic policy objectives. Which row gives a correct assessment of the country's achievement of these objectives over the period?", ["rate of inflation: cannot tell; economic growth: positive", "rate of inflation: declining; economic growth: cannot tell", "rate of inflation: positive; economic growth: declining", "rate of inflation: rising; economic growth: negative"], 2, "Money GDP grows faster than real GDP in every year, so there is inflation. Real growth is 5% then about 1%, so growth is positive but declining."),
  mcq("s23_13", 18, "The table gives data for an economy: GDP at current prices ($ billion) 200, 220, 240, 300, 320 for 2010 to 2014, and the GDP deflator 100, 109, 125, 149, 154. In which year did real GDP decline compared with the previous year?", ["2011", "2012", "2013", "2014"], 1, "Real GDP is nominal ÷ deflator × 100: 200, 201.8, 192.0, 201.3, 207.8. It fell in 2012."),
  mcq("s23_13", 20, "In year 1, a country's real GDP was $500 billion. In year 2, nominal GDP rose to $577.5 billion and the prices increased by 5%. What is the real GDP in year 2?", ["$4.76 billion", "$5 billion", "$476 billion", "$550 billion"], 3, "577.5 ÷ 1.05 = 550."),
  mcq("s22_13", 23, "A household's income increased by 3%. Over the same period, the rate of inflation was also 3%. Which statement is correct?", ["Both the nominal income and the real income of the household increased by 3%", "The nominal income remained unchanged while the real income increased by 3%", "The nominal income of the household increased by 3% while the real income was unchanged", "Both nominal income and real income remained unchanged"], 2, "Real income is nominal income adjusted for inflation: +3% less 3% inflation is no change."),
  mcq("s24_12", 16, "The table gives the value of the price index of an economy in two years: year 1 is 60 and year 2 is 120. What can be concluded about the period?", ["Nominal income doubled", "Real income doubled", "The cost of living doubled", "The standard of living doubled"], 2, "A price index that doubles means the cost of living doubled. Nothing is known about income."),
  mcq("s20_13", 25, "The real national income of a country fell by 3%. What could have caused this?", ["Money national income fell by 3% when the rate of inflation was 6%", "Money national income fell by 6% when the rate of inflation was 3%", "Money national income rose by 3% when the rate of inflation was 6%", "Money national income rose by 6% when the rate of inflation was 3%"], 2, "Real change ≈ money change minus inflation: +3 − 6 = −3. In option B the real change would be −9%.")
]

exam = exam_page("economic growth and real GDP",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Growth measures appear in short data-response parts (2 marks) asking for a meaning or a calculation, and in Paper 1 as real GDP and index questions. Reworded past questions are below, with six Paper 1 multiple choice questions.",
  [("Data response, 2 marks", "2", "May/June 2025 (24) Q1(b); Oct/Nov 2023 (23) Q1(a)"), ("Multiple choice (Paper 1)", "6 shown below", "2020 to 2024")],
  [
  eq(P("s25_24", "1(b)"), "2 marks", "Explain what is meant by 'real GDP'.",
     ["GDP is the total value of goods and services produced in an economy (1).", "Real GDP is GDP corrected for or taking account of the effects of inflation or price changes (1). Real GDP is nominal GDP less the rate of inflation (2). Maximum 2 marks."],
     "GDP: value of output. Real: adjusted for inflation.",
     [[("k", "GDP is the total value of goods and services produced in an economy in a year. Real GDP is GDP adjusted for inflation, so it shows the change in output rather than in prices.")]]),
  eq(P("w23_23", "1(a)"), "2 marks", "Explain the meaning of 'negative economic growth'.",
     ["A decrease or fall in national income or output (1), as measured by GDP or real GDP (1), or shown as a movement within a PPC or an inward shift (1). Maximum 2."],
     "A fall in real GDP or national income over time.",
     [[("k", "Negative economic growth is a fall in national output over time, measured by a decrease in real GDP. On a PPC diagram it can be shown by a move to a point further inside the curve.")]])
  ],
  )

tips = tips_html(
  [("Growth means real.", "Always use real GDP unless told otherwise."),
   ("Show the formula.", "(new − old) ÷ old × 100."),
   ("Deflate first.", "Real GDP = nominal ÷ price index × 100."),
   ("Real growth ≈ nominal growth − inflation.", "Use as a check."),
   ("Recession = two quarters of falling real GDP.", "Negative growth."),
   ("Use per capita for living standards.", "Divide by population."),
   ("Know the limits.", "Informal economy, distribution, environment.")],
  [("Economic growth", "Economic growth is an increase in real GDP over time."),
   ("Real GDP", "Real GDP is GDP adjusted for inflation."),
   ("Nominal GDP", "Nominal GDP is measured at current prices."),
   ("Negative growth", "Negative growth is a fall in real GDP."),
   ("Per capita", "GDP per head divides real GDP by population.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = '''
/* ---------- nominal vs real ---------- */
function nrDraw(s) {
  const Y = (v) => 250 - v * 1.7, W = 80; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "GDP ($bn)", "sm");
  const bar = (x, v, c, l, vis) => vis > 0 ? SV.rect(x, Y(v), W, 250 - Y(v), c, op(0.65 * vis)) + SV.text(x + W / 2, 270, l, "sm", { "text-anchor": "middle", ...op(vis) }) + SV.text(x + W / 2, Y(v) - 6, Lib.fmtN(v, 1), "lbl bd", { "text-anchor": "middle", ...op(vis) }) : "";
  o += bar(120, 100, "f1", "Year 1 (real = nominal)", s.a) + bar(280, 108, "f2", "Year 2 nominal", s.b) + bar(440, 108 / 1.05, "f3", "Year 2 real", s.c);
  if (s.d > 0) o += tag(380, 70, "Nominal growth 8%, inflation 5%, real growth ≈ 2.9%", "c3", s.d, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Nominal GDP rises 8 percent, prices 5 percent, so real GDP rises 2.9 percent">${nrDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stR"), { w: 760, h: 290, label: "Nominal GDP, inflation and real GDP", base: { a: 0, b: 0, c: 0, d: 0 }, draw: nrDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>Year 1.</b> GDP is $100bn. Taking year 1 as the base year, real and nominal GDP are the same.", s: { a: 1 } },
  { cap: "<b>Year 2 nominal GDP</b> is $108bn at year 2 prices: nominal growth of 8%.", s: { a: 1, b: 1 } },
  { cap: "<b>But prices rose 5%.</b> Deflating: real GDP = 108 ÷ 1.05 = $102.9bn.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Real growth is only about 2.9%.</b> Most of the nominal rise was inflation. Approximately, real growth = nominal growth − inflation.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });
const cyc = (x) => 150 + (x - 20) * 0.55 - 50 * Math.sin((x - 20) / 12);
function cyDraw(s) {
  let o = axes(70, 270, 720, 25, "Time", "Real GDP"), d = "", t = "", n = Math.round(s.k);
  for (let i = 0; i <= 100; i += 2) { const x = 70 + i * 6, y = 145 - i * 0.495 + 45 * Math.sin(i / 12); t += (i ? " L" : "M") + x + "," + (145 - i * 0.495); if (i <= n) d += (d ? " L" : "M") + x + "," + y; }
  o += SV.path(t, "dash", { fill: "none" }) + tag(660, 90, "Trend (potential)", "c4", 1, "end");
  o += d ? SV.path(d, "c2", { fill: "none", "stroke-width": 3.5 }) : "";
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Real GDP rising, peaking, falling and recovering around a trend">${cyDraw({ k: 100 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Real GDP over the business cycle", base: { k: 0 }, draw: cyDraw, tween: 1000, dwell: 5200, steps: [
  { cap: "<b>Trend growth.</b> The dashed line shows the rise in potential output over time.", s: { k: 0 } },
  { cap: "<b>Expansion.</b> Real GDP grows faster than the trend: unemployment falls and spare capacity is used up.", s: { k: 30 } },
  { cap: "<b>Peak and recession.</b> Growth slows and real GDP falls for two or more quarters: <b>negative growth</b>, rising unemployment.", s: { k: 65 } },
  { cap: "<b>Trough and recovery.</b> Output stops falling and begins to rise again towards trend.", s: { k: 100 } },
] });

/* ---------- Lab 1 ---------- */
function labN() {
  if (!["n1", "n2", "pi"].every((i) => $("#" + i))) return;
  const n1 = +$("#n1").value, n2 = +$("#n2").value, pi = +$("#pi").value, r2 = n2 / (pi / 100), ng = (n2 - n1) / n1 * 100, rg = (r2 - n1) / n1 * 100;
  $("#r1").textContent = "$" + Lib.fmtN(r2, 1) + "bn"; $("#r2").textContent = Lib.fmtN(ng, 1) + "%"; $("#r3").textContent = Lib.fmtN(rg, 1) + "%";
  $("#rv").textContent = `Year 2 nominal GDP of $${n2}bn at a price index of ${pi} (year 1 = 100) is $${Lib.fmtN(r2, 1)}bn in year 1 prices. Nominal growth is ${Lib.fmtN(ng, 1)}%, but real growth is ${Lib.fmtN(rg, 1)}%. ${rg < 0 ? "Real GDP has fallen: negative growth, even though nominal GDP rose." : rg < ng ? "Inflation has eaten part of the nominal rise." : ""}`;
  const Y = (v) => 250 - v * 0.8; let o = SV.line(40, 250, 400, 250);
  [["Y1 real", n1, "f1"], ["Y2 nominal", n2, "f2"], ["Y2 real", r2, "f3"]].forEach(([l, v, c], i) => (o += SV.rect(60 + i * 110, Y(v), 80, 250 - Y(v), c, op(0.65)) + SV.text(100 + i * 110, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(100 + i * 110, Y(v) - 6, Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "n1", label: "Year 1 nominal GDP (index 100), $bn ", min: 200, max: 400, step: 10, value: 300, fmt: (v) => v, onInput: labN });
Lib.slider($("#g2"), { id: "n2", label: "Year 2 nominal GDP, $bn ", min: 200, max: 450, step: 10, value: 330, fmt: (v) => v, onInput: labN });
Lib.slider($("#g3"), { id: "pi", label: "Year 2 price index (year 1 = 100) ", min: 95, max: 125, step: 1, value: 106, fmt: (v) => v, onInput: labN });
labN();

/* ---------- Lab 2 ---------- */
function labP() {
  if (!["gr", "po"].every((i) => $("#" + i))) return;
  const g = +$("#gr").value, p = +$("#po").value, pc = ((1 + g / 100) / (1 + p / 100) - 1) * 100;
  $("#t1").textContent = g + "%"; $("#t2").textContent = p + "%"; $("#t3").textContent = (pc > 0 ? "+" : "") + Lib.fmtN(pc, 1) + "%";
  $("#tv").textContent = `Real GDP grows ${g}% and the population ${p}%, so GDP per head changes by ${Lib.fmtN(pc, 1)}%. ${pc > 0.05 ? "Average output per person rises, which usually means rising living standards." : pc < -0.05 ? "GDP per head falls although GDP grows: living standards on average fall." : "GDP per head is unchanged."}`;
  const Y = (v) => 150 - v * 12; let o = SV.line(40, 150, 400, 150) + SV.line(40, 20, 40, 190);
  [["GDP", g, "f2"], ["Population", p, "f1"], ["GDP per head", pc, pc >= 0 ? "f2" : "f3"]].forEach(([l, v, c], i) => (o += SV.rect(70 + i * 110, v >= 0 ? Y(v) : 150, 80, Math.abs(Y(v) - 150), c, op(0.65)) + SV.text(110 + i * 110, 185, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, (v >= 0 ? Y(v) : 150 + Math.abs(Y(v) - 150)) + (v >= 0 ? -6 : 14), Lib.fmtN(v, 1) + "%", "lbl bd", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "gr", label: "Real GDP growth, % ", min: -2, max: 8, step: 1, value: 3, fmt: (v) => v + "%", onInput: labP });
Lib.slider($("#g5"), { id: "po", label: "Population growth, % ", min: -1, max: 5, step: 1, value: 2, fmt: (v) => v + "%", onInput: labP });
labP();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Nominal or real?", ["Nominal (current prices)", "Real (adjusted for inflation)"],
  [("GDP measured at today's prices", 0), ("GDP deflated by a price index", 1), ("Rises when only prices rise", 0), ("Rises only if output rises", 1), ("Used to measure economic growth", 1), ("Used to show the money value of output", 0), ("Also called money GDP", 0), ("GDP in constant base-year prices", 1)],
  "Nominal includes inflation; real removes it.") + MATCH([
  ["Economic growth", "A rise in real GDP over time"],
  ["Nominal GDP", "GDP at current prices"],
  ["Real GDP", "GDP adjusted for inflation"],
  ["Recession", "Two or more quarters of falling real GDP"],
  ["GDP per capita", "Real GDP divided by population"],
  ["GDP deflator", "Price index used to convert nominal to real GDP"]]) + ORDER(
  "Put the steps for finding real growth in order.",
  ["Take nominal GDP for each year", "Divide by the price index and multiply by 100", "This gives real GDP for each year", "Find the change in real GDP", "Divide by the earlier year and multiply by 100"],
  "Deflate first, then find the percentage change.") + CALC([
  {"q": "Nominal GDP is $630bn and the price index is 105 (base year 100). What is real GDP ($bn)?", "a": 600, "unit": "$bn", "tol": 0.5, "hint": "630 ÷ 1.05.", "sol": "<b>$600bn</b>."},
  {"q": "Real GDP in the previous year was $580bn. What is real growth (to one decimal place)?", "a": 3.4, "unit": "%", "tol": 0.1, "hint": "20 ÷ 580.", "sol": "<b>3.4%</b>."},
  {"q": "Nominal GDP rises 4% and inflation is 6%. Approximately what is real growth?", "a": -2, "unit": "%", "tol": 0.2, "hint": "4 − 6.", "sol": "<b>−2%</b>: real GDP falls."},
  {"q": "Real GDP grows 3% and population grows 1%. Approximately what is growth in GDP per head?", "a": 2, "unit": "%", "tol": 0.2, "hint": "3 − 1.", "sol": "<b>2%</b>."}]) + MCQ([
  ("Economic growth is measured by:", ["The percentage change in real GDP", "The percentage change in nominal GDP", "The rise in prices", "The fall in unemployment"], 0, "Real, not nominal."),
  ("Real GDP is:", ["GDP adjusted for inflation", "GDP at current prices", "GDP less imports", "GDP per head"], 0, "Corrected for price changes."),
  ("If nominal GDP rises by less than inflation, real GDP:", ["Falls", "Rises", "Stays the same", "Doubles"], 0, "Negative real growth."),
  ("A recession is usually defined as:", ["Two consecutive quarters of falling real GDP", "A rise in prices", "A fall in nominal GDP in one quarter", "Rising unemployment only"], 0, "Negative growth."),
  ("GDP per head rises when:", ["GDP grows faster than population", "Population grows faster than GDP", "Prices rise", "Imports fall"], 0, "Average output per person.")
], "qz1") + CARDS([
  ("Growth", "Rise in real GDP."),
  ("Nominal GDP", "Current prices."),
  ("Real GDP", "Adjusted for inflation."),
  ("Real = ", "Nominal ÷ index × 100."),
  ("Recession", "Two quarters of falling real GDP."),
  ("Per capita", "GDP ÷ population."),
  ("Actual growth", "Using spare capacity."),
  ("Potential growth", "LRAS or PPC shifts out.")]) + MCQ(mc_exam)

build("as46", "as-economic-growth-measurement", "Economic Growth: Meaning and Measurement", EY,
  "4.4.1 to 4.4.3: the meaning and measurement of economic growth, and the difference between growth in nominal and real GDP. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
