"""Builds the five IGCSE Economics 4.5 Economic growth reviews (4.5.1 to 4.5.5), written from scratch.
Run: python3 tools/artifact-kit/mk_ig45.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
_src = open(D / "mk_ig44.py").read()
COMMON = _src.split("COMMON = '''")[1].split("'''")[0]   # solve2, adasChart, mkChain, chainSteps, button_table
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

CYCLE = '''
/* business cycle: GDP wiggling around a rising trend */
const gdpT = (t) => 100 + 0.6 * t + 22 * Math.sin((2 * Math.PI * t) / 50);
const CX = (t) => 60 + t * 6.4, CYv = (g) => 330 - (g - 60) * 2.2;
function cycleChart(s) {
  const t = s.t; let o = SV.line(60, 340, 60, 30) + SV.line(60, 340, 710, 340) + SV.text(66, 40, "Real GDP", "sm") + SV.text(710, 362, "Time", "sm", { "text-anchor": "end" });
  o += SV.line(CX(0), CYv(100), CX(100), CYv(160), "dash", { style: "stroke:var(--muted);stroke-width:2" }) + SV.text(CX(100) - 4, CYv(160) - 8, "Trend (long-run growth)", "sm bd", { "text-anchor": "end" });
  const pts = []; for (let i = 0; i <= 100; i += 2) pts.push([CX(i), CYv(gdpT(i))]);
  o += SV.path(ptsPath(pts), "c3", { opacity: 0.45 });
  const done = []; for (let i = 0; i <= t; i += 1) done.push([CX(i), CYv(gdpT(i))]); done.push([CX(t), CYv(gdpT(t))]);
  if (done.length > 1) o += SV.path(ptsPath(done), "c1");
  o += SV.circle(CX(t), CYv(gdpT(t)), 8, "dot2");
  if (s.lbl) o += SV.text(CX(t), CYv(gdpT(t)) - 18, s.lbl, "lbl bd t2", { "text-anchor": "middle", style: halo });
  return o;
}
'''
RWN = RWNOTE

# =========================================================== 4.5.1 Definition
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Economic growth</span> is an increase in an economy's output over time, measured as a rise in <b>real GDP</b>. It can also be described as an increase in the economy's <b>productive capacity</b>: what it could produce if resources were fully used. A growing economy can produce and consume more goods and services, which usually means higher incomes and more jobs.</p></div>

  <h2>Two ways to see growth</h2>
  <div class="grid2">
    <div class="card"><h3>Actual growth</h3><p>A rise in real GDP: output actually produced rises, for example because spending rises and unused resources are put to work. Seen as a movement towards the PPC, or an AD shift right.</p></div>
    <div class="card"><h3>Potential (long-run) growth</h3><p>A rise in productive capacity: the PPC shifts outwards, or AS shifts right. This comes from more or better resources and technology.</p></div>
  </div>

  <h2>Growth is not smooth</h2>
  <p>Real GDP does not rise in a straight line. Output usually moves in a pattern called the <span class="kw">business cycle</span> around a long-run upward trend.</p>
  <div class="tw"><table class="t">
    <tr><th>Phase</th><th>What happens to output</th><th>Typical features</th></tr>
    <tr><td><b>Boom</b></td><td>Growing fast, close to capacity</td><td>Low unemployment, rising prices, high confidence</td></tr>
    <tr><td><b>Slowdown</b></td><td>Growth slows</td><td>Spending and investment weaken</td></tr>
    <tr><td><b>Recession</b></td><td>Real GDP falls</td><td>Rising unemployment, falling profits, falling tax revenue</td></tr>
    <tr><td><b>Recovery</b></td><td>Growth returns</td><td>Confidence returns, firms start to hire</td></tr>
  </table></div>
  <p class="note">The trend line is long-run (potential) growth. The wiggles around it are short-run changes in actual output.</p>

  <h2>Why governments care</h2>
  <ul>
    <li>Growth is one of the six <b>macroeconomic aims</b>.</li>
    <li>Higher output can mean higher incomes, more jobs and more tax revenue for public services.</li>
    <li>But growth can bring costs too: pollution, inflation and unequal gains (see 4.5.3).</li>
  </ul>
'''
js = HEAD + COMMON + CYCLE + '''
function ppcChart(s) {
  const ox = 90, oy = 330, X = 250 * s.s, Y = 215 * s.s, X0 = 250, Y0 = 215;
  const curve = (X, Y) => { const p = []; for (let t = 0; t <= 90; t += 5) { const r = (t * Math.PI) / 180; p.push([ox + X * Math.cos(r), oy - Y * Math.sin(r)]); } return p; };
  let o = SV.line(ox, oy, ox, 30) + SV.line(ox, oy, 700, oy) + SV.text(ox + 6, 40, "Capital goods", "sm") + SV.text(700, oy + 24, "Consumer goods", "sm", { "text-anchor": "end" });
  if (s.s > 1.02) o += SV.path(ptsPath(curve(X0, Y0)), "c3", { opacity: 0.4 }) + SV.text(ox + X0 * 0.7071 + 10, oy - Y0 * 0.7071 + 22, "PPC", "lbl bd t3", { opacity: 0.6 });
  o += SV.path(ptsPath(curve(X, Y)), "c1") + SV.text(ox + X * 0.7071 + 12, oy - Y * 0.7071 - 6, s.s > 1.02 ? "PPC₁" : "PPC", "lbl bd t1");
  const k = s.in || 0, px = ox + (X * 0.7071) * (1 - 0.25 * (1 - k)), py = oy - (Y * 0.7071) * (1 - 0.25 * (1 - k));
  o += SV.line(px, py, px, oy, "gr") + SV.line(ox, py, px, py, "gr") + SV.circle(px, py, 7, s.s > 1.02 ? "dot2" : "dot1");
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Actual and potential growth on a PPC", base: { s: 1, in: 0 }, draw: ppcChart, steps: [
  { cap: "The economy is <b>inside its PPC</b>: some resources are unused (unemployed workers, idle factories). Output is below its potential.", s: { s: 1, in: 0 } },
  { cap: "<b>Actual growth:</b> spending rises and unused resources are put to work. The economy moves <b>towards the PPC</b>, and real GDP rises.", s: { s: 1, in: 1 } },
  { cap: "<b>Potential growth:</b> more or better resources and technology shift the PPC <b>outwards</b>. The economy can now produce more than before: <b>productive capacity</b> has grown.", s: { s: 1.2, in: 1 } },
] });
Lib.stepper($("#stC"), { w: 760, h: 400, label: "The business cycle", base: { t: 0, lbl: "" }, draw: cycleChart, steps: [
  { cap: "Real GDP tends to rise over time along a <b>long-run trend</b>, but not smoothly.", s: { t: 0, lbl: "Start" } },
  { cap: "In a <b>boom</b> output grows fast and unemployment is low. Demand may outstrip supply and prices rise.", s: { t: 12, lbl: "Boom" } },
  { cap: "Growth <b>slows</b>, then output <b>falls</b>. When real GDP falls for at least two quarters in a row, the economy is in <b>recession</b>.", s: { t: 28, lbl: "Recession" } },
  { cap: "At the <b>trough</b>, output is at its lowest. Unemployment is high and confidence is low.", s: { t: 37, lbl: "Trough" } },
  { cap: "<b>Recovery:</b> output starts to rise again, jobs return, and the economy heads back to trend and the next boom.", s: { t: 50, lbl: "Recovery" } },
] });

/* Lab 1: compound growth */
function labG() {
  if (!$("#ga") || !$("#gb")) return;
  const r = +$("#ga").value, n = +$("#gb").value, gdp = [100]; for (let i = 1; i <= n; i++) gdp.push(gdp[i - 1] * (1 + r / 100));
  $("#ga1").textContent = money(gdp[n], 1); $("#ga2").textContent = "+" + money(gdp[n] - 100, 1); $("#ga3").textContent = r > 0 ? money(70 / r, 0) + " years" : "never";
  $("#gav").textContent = `At ${r}% a year real GDP rises from 100 to ${money(gdp[n], 1)} after ${n} years. Small differences in the growth rate add up: compare 2% with 6%. A rough rule: GDP doubles in about 70 ÷ growth rate years.`;
  const base = 320, mx = Math.max(...gdp), k = 250 / Math.max(mx, 120), w = Math.min(28, 640 / (n + 1)), gap = w * 0.2;
  let o = SV.line(40, base, 740, base);
  gdp.forEach((v, i) => { const x = 50 + i * (w + gap); o += SV.rect(x, base - v * k, w, v * k, "", { style: "fill:var(--accent)", opacity: 0.8 }); if (n <= 12 || i % 2 === 0) o += SV.text(x + w / 2, base - v * k - 6, money(v, 0), "sm bd", { "text-anchor": "middle", style: "font-size:10px" }); });
  $("#labG").innerHTML = o + SV.text(40, 24, "Real GDP index (start = 100)", "sm") + SV.text(740, base + 22, "Years", "sm", { "text-anchor": "end" });
}
Lib.slider($("#g1"), { id: "ga", label: "Growth rate each year", min: 0, max: 10, step: 0.5, value: 3, fmt: (v) => v + "%", onInput: labG });
Lib.slider($("#g2"), { id: "gb", label: "Number of years", min: 1, max: 20, step: 1, value: 10, fmt: (v) => v + " years", onInput: labG });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each <b>actual growth</b> (using spare resources) or <b>potential growth</b> (more productive capacity)?", buckets: [{ label: "Actual growth" }, { label: "Potential growth" }], items: [
  { text: "Unemployed workers get jobs after a rise in spending", b: 0 }, { text: "An economy moves from inside the PPC towards it", b: 0 }, { text: "AD shifts right and spare capacity is used", b: 0 }, { text: "Firms restart idle factories", b: 0 },
  { text: "The PPC shifts outwards", b: 1 }, { text: "AS shifts right", b: 1 }, { text: "New technology raises productivity", b: 1 }, { text: "More investment in machinery raises capacity", b: 1 },
], done: "Actual growth uses spare resources; potential growth raises the limit." });
Lib.classify($("#cl2"), { prompt: "Which <b>phase of the business cycle</b> does each describe?", buckets: [{ label: "Boom" }, { label: "Recession" }, { label: "Recovery" }], items: [
  { text: "Output is growing fast and unemployment is very low", b: 0 }, { text: "Demand outstrips supply and prices are rising", b: 0 },
  { text: "Real GDP falls for two quarters in a row", b: 1 }, { text: "Firms lay off workers and profits fall", b: 1 },
  { text: "Output starts to rise again after a trough", b: 2 }, { text: "Confidence returns and firms start to hire again", b: 2 },
], done: "The cycle: boom, slowdown, recession, recovery." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Economic growth", "An increase in real GDP (output) over time"],
  ["Productive capacity", "The most an economy can produce with its resources"],
  ["Business cycle", "The pattern of booms and recessions around a long-run trend"],
  ["Recession", "A fall in real GDP for at least two quarters in a row"],
  ["Boom", "A period of fast growth, high demand and low unemployment"],
  ["Potential output", "Output when resources are fully and efficiently used"],
], done: "Good vocabulary scores marks." });
''' + calc_js([
    ("Real GDP was $2,000bn in 2022 and $2,100bn in 2023. What is the growth rate (%)?", 5, "(2,100 − 2,000) ÷ 2,000 × 100 = <b>5%</b>.", "Change divided by the original, times 100.", None),
    ("Real GDP was $8,750bn in 2016 and $9,362.5bn in 2017. Calculate the growth rate in 2017 (%). (India, past paper)", 7, "(9,362.5 − 8,750) ÷ 8,750 × 100 = <b>7%</b>.", None, None),
    ("Real GDP is $400bn and grows at 5% a year. What is it after one year ($bn)?", 420, "400 × 1.05 = <b>$420bn</b>.", None, None),
    ("An economy grows by 2% a year. Roughly how many years will it take for real GDP to double (70 ÷ rate)?", 35, "70 ÷ 2 = <b>35 years</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is economic growth?", ["A rise in the price level", "An increase in real GDP over time", "A fall in unemployment", "A rise in the exchange rate"], 1, "Growth is a rise in real output."),
    ("An outward shift of the PPC shows:", ["Recession", "Potential (long-run) growth", "Unemployment", "Inflation"], 1, "The economy can now produce more."),
    ("A recession is usually defined as:", ["A fall in prices", "A fall in real GDP for two successive quarters", "A fall in unemployment", "A rise in interest rates"], 1, "Two quarters of falling real GDP."),
    ("Which phase of the business cycle usually has the lowest unemployment?", ["Recession", "Trough", "Boom", "Recovery"], 2, "Firms are hiring to meet high demand."),
    ("Which is most likely to raise an economy's productive capacity?", ["A temporary tax cut", "Investment in new technology", "A fall in interest rates", "A rise in prices"], 1, "Technology raises output per worker."),
]) + "\n" + cards_js([("Economic growth", "An increase in real GDP over time."), ("Actual growth", "A rise in real GDP as spare resources are used."), ("Potential growth", "A rise in productive capacity, shown by an outward shift of the PPC or AS shifting right."), ("Productive capacity", "The most an economy can produce with its resources."), ("Business cycle", "The pattern of booms and recessions around a long-run trend."), ("Recession", "A fall in real GDP for at least two quarters in a row."), ("Boom", "A period of fast growth and high demand."), ("Recovery", "Output rising again after a recession."), ("Trend growth", "The long-run average rate of growth of real GDP.")]) + "labG();\n"
explore = '''
  <h2>Lab 1 · Compound growth</h2>
  <p>Real GDP starts at 100. Choose a growth rate and a number of years and watch it build up.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Real GDP at the end</small><strong id="ga1"></strong></div><div><small>Rise since the start</small><strong id="ga2"></strong></div><div><small>Doubling time (70 ÷ rate)</small><strong id="ga3"></strong></div></div><div class="verdict" id="gav"></div></div></div>
    <svg id="labG" viewBox="0 0 760 360" role="img" aria-label="Real GDP over time"></svg>
  </div>
'''
ex = exam(
    Q(1, "Define", 2, "Define economic growth. (Feb/Mar 2021, P22)", "Real GDP is the key idea, plus 'over time'. A productive capacity definition also scores.",
      "[K|Economic growth is an increase in real GDP (the output of the economy)] [K|over time.]"),
    Q(2, "Calculate", 1, "Real GDP was $8,750.0bn in 2016 and $9,362.5bn in 2017. Calculate India's economic growth rate in 2017. (Feb/Mar 2020, P22)", "Change ÷ original × 100. Give the answer as a percentage.",
      "[A|(9,362.5 − 8,750.0) ÷ 8,750.0 × 100 = 7%.]"),
    Q(3, "Explain", 4, "Explain the difference between actual growth and potential growth.", "Use 'whereas'. Actual: use of spare resources. Potential: more capacity.",
      "[K|Actual growth is a rise in real GDP as unused resources are put to work, shown by a move towards the PPC,] [K|whereas potential growth is an increase in the economy's productive capacity, shown by an outward shift of the PPC or AS shifting right.] [N|Actual growth could be quick if demand rises, but it is limited once resources are fully used,] [N|whereas potential growth usually takes longer, as it needs more or better resources or technology.]"),
    Q(4, "Explain", 4, "Explain what happens to output, jobs and prices during a boom.", "Three things, each linked. Output high, unemployment low, prices may rise.",
      "[K|In a boom real GDP grows quickly and firms are working close to capacity.] [N|Firms need more workers, so unemployment is likely to be low.] [N|With high demand and little spare capacity, firms could raise prices, so inflation may increase.]"),
)
tp = tips([
    ("Growth = rise in real GDP over time.", "Say 'real' and 'over time'."),
    ("Growth rate = change ÷ original × 100.", "Show the working."),
    ("Know actual and potential growth.", "Move towards the PPC, or the PPC shifts out."),
    ("Know the cycle.", "Boom, slowdown, recession, recovery."),
], cmds("Define", "Calculate", "Explain"))
body = page(CL("4.5.1 Definition of economic growth"), "Definition of Economic Growth", "What economic growth is, actual and potential growth, and the business cycle. Syllabus 4.5.1.",
    learn=learn, watch=watch(("Actual and potential growth on a PPC", "stP"), ("The business cycle", "stC")), explore=explore,
    practise=practise(("Actual or potential growth?", "cl1", "card"), ("Which phase of the cycle?", "cl2", "card"), ("Match the term", "m1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("China's long run of fast growth", "China's real GDP grew at around 10% a year for several decades from the 1980s, helped by investment, new technology, trade and a growing workforce. In 30 years output multiplied many times.", "Compound growth and potential growth from more and better resources."),
        rw("Japan's slow decades", "After the early 1990s Japan's growth was very low for many years, with weak demand and an ageing workforce.", "Long periods of low growth and why growth rates matter over time."),
        rw("India's growth", "A past paper describes India's growth of around 7% in 2017, driven by government spending and exports, with side effects such as pollution.", "A growth-rate calculation and a link to the costs of growth.")),
    exam=ex, tips=tp)
write("eg1", body, js, "Definition of Economic Growth", "ig-growth-definition")

# =========================================================== 4.5.2 Measurement
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Economic growth is measured by the change in <span class="kw">real GDP</span>. <span class="kw">Gross domestic product (GDP)</span> is the total value of all final goods and services produced in a country in a year. <b>Nominal GDP</b> is measured at current prices, so it rises when prices rise even if output does not. <b>Real GDP</b> removes the effect of inflation, so a rise in real GDP means more goods and services were actually produced.</p></div>

  <h2>Nominal and real GDP</h2>
  <div class="grid2">
    <div class="card"><h3>Nominal GDP</h3><p>Output valued at the prices of the year. If prices rise 4% and output stays the same, nominal GDP still rises by 4%, which would mislead.</p></div>
    <div class="card"><h3>Real GDP</h3><p>Output valued at constant (base-year) prices, adjusted for inflation. It shows the change in the amount produced.</p></div>
  </div>
  <div class="formula">Real GDP ≈ nominal GDP adjusted for inflation &nbsp;·&nbsp; Growth rate = (GDP this year − GDP last year) ÷ GDP last year × 100</div>
  <p><b>Example:</b> Nominal GDP rises from $100bn to $106bn (+6%) but prices rise 4%. Real GDP growth is about 6% − 4% = <b>2%</b>.</p>

  <h2>GDP per head (per capita)</h2>
  <p>Real GDP per head = real GDP ÷ population. It is a better guide to the average person's income than total GDP, because a large economy with a huge population can have low output per person. If population grows faster than real GDP, real GDP per head falls.</p>

  <h2>What GDP does and does not tell us</h2>
  <div class="grid2">
    <div class="card"><h3>What it is useful for</h3><ul><li>Comparing growth over time and between countries</li><li>Checking whether the economy is in a boom or recession</li><li>Seeing the size of the economy</li></ul></div>
    <div class="card"><h3>Limitations</h3><ul><li>The <b>informal economy</b> and unpaid work are missed</li><li>It says nothing about <b>how income is shared</b></li><li>It ignores <b>pollution</b> and use of resources</li><li>It does not capture <b>quality</b> of life, leisure or health</li><li>Data may be inaccurate</li></ul></div>
  </div>
'''
js = HEAD + COMMON + '''
function realChart(s) {
  const base = 320, k = 2.4, bars = [["Year 1", 100, "--muted", s.a], ["Year 2 nominal", 106, "--warn", s.b], ["Year 2 real", 106 / 1.04, "--good", s.c]];
  let o = SV.line(60, base, 700, base);
  bars.forEach(([n, v, c, op], i) => {
    const x = 110 + i * 210, h = v * k; if (op <= 0.02) return;
    o += `<g opacity="${op}">` + SV.rect(x, base - h, 130, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, base - h - 8, money(v, 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 22, n, "sm", { "text-anchor": "middle" }) + "</g>";
  });
  if (s.t) o += SV.text(380, 40, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:17px" });
  return o;
}
Lib.stepper($("#stR"), { w: 760, h: 400, label: "Nominal and real GDP", base: { a: 0, b: 0, c: 0, t: "" }, draw: realChart, steps: [
  { cap: "In Year 1 GDP is <b>100</b>. This is the base year, so nominal and real GDP are the same.", s: { a: 1, b: 0, c: 0, t: "" } },
  { cap: "In Year 2 <b>nominal GDP</b> rises to <b>106</b>: up 6%. But did the economy really produce 6% more?", s: { a: 1, b: 1, c: 0, t: "Nominal GDP +6%" } },
  { cap: "Over the year <b>prices rose 4%</b>. Part of the rise in nominal GDP is just dearer goods, not extra goods.", s: { a: 1, b: 1, c: 0, t: "Prices +4%" } },
  { cap: "<b>Real GDP</b> adjusts for inflation: 106 ÷ 1.04 ≈ <b>101.9</b>. Real growth is only about <b>1.9%</b>. This is the figure used to measure economic growth.", s: { a: 1, b: 0.5, c: 1, t: "Real growth ≈ 1.9%" } },
] });
function growthChart(s) {
  const base = 320, k = 0.032, v0 = 8750, v1 = s.v; let o = SV.line(60, base, 700, base);
  [["2016", v0, "--muted"], ["2017", v1, "--accent"]].forEach(([n, v, c], i) => {
    const x = 160 + i * 250, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, "$" + money(v, 1) + "bn", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" });
  });
  if (s.show > 0) o += SV.text(380, 40, "Growth = (" + money(v1, 1) + " − 8,750.0) ÷ 8,750.0 × 100 = " + money(((v1 - v0) / v0) * 100, 1) + "%", "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stK"), { w: 760, h: 400, label: "Calculating the growth rate", base: { v: 8750, show: 0 }, draw: growthChart, steps: [
  { cap: "India's real GDP in 2016 was <b>$8,750.0bn</b>.", s: { v: 8750, show: 0 } },
  { cap: "In 2017 it was <b>$9,362.5bn</b>: a rise of $612.5bn.", s: { v: 9362.5, show: 0 } },
  { cap: "<b>Growth rate = change ÷ original × 100</b> = 612.5 ÷ 8,750 × 100 = <b>7%</b>.", s: { v: 9362.5, show: 1 } },
] });

/* Lab 1: real growth and GDP per head */
function labR() {
  if (!$("#ra") || !$("#rb") || !$("#rc")) return;
  const nom = +$("#ra").value, inf = +$("#rb").value, pop = +$("#rc").value, real = ((1 + nom / 100) / (1 + inf / 100) - 1) * 100, pc = ((1 + real / 100) / (1 + pop / 100) - 1) * 100;
  $("#ra1").textContent = (real >= 0 ? "+" : "−") + money(Math.abs(real), 1) + "%"; $("#ra2").textContent = (pc >= 0 ? "+" : "−") + money(Math.abs(pc), 1) + "%"; $("#ra3").textContent = nom + "%";
  $("#rav").textContent = real < 0 ? "Prices rose by more than nominal GDP, so real GDP fell: the economy produced less, even though the money figure rose." : pc < 0 ? "Real GDP rose, but population grew faster, so real GDP per head fell: the average person is worse off." : `Real GDP rose by about ${money(real, 1)}%. After population growth, real GDP per head rose by about ${money(pc, 1)}%.`;
  const base = 300, k = 14; let o = SV.line(60, base, 700, base);
  [["Nominal GDP growth", nom, "--warn"], ["Real GDP growth", real, "--good"], ["Real GDP per head", pc, "--accent"]].forEach(([n, v, c], i) => {
    const x = 120 + i * 190, h = v * k, y = v >= 0 ? base - h : base;
    o += SV.rect(x, y, 130, Math.abs(h), "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, v >= 0 ? y - 8 : y + Math.abs(h) + 18, (v >= 0 ? "+" : "−") + money(Math.abs(v), 1) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 40, n, "sm", { "text-anchor": "middle" });
  });
  $("#labR").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ra", label: "Growth of nominal GDP", min: -2, max: 12, step: 0.5, value: 6, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g2"), { id: "rb", label: "Inflation (rise in prices)", min: 0, max: 10, step: 0.5, value: 4, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g3"), { id: "rc", label: "Population growth", min: 0, max: 4, step: 0.5, value: 1, fmt: (v) => v + "%", onInput: labR });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each <b>included in GDP</b>, or <b>left out</b>?", buckets: [{ label: "Included in GDP" }, { label: "Left out of GDP" }], items: [
  { text: "A new car produced and sold in the country", b: 0 }, { text: "A haircut paid for", b: 0 }, { text: "Government spending on schools", b: 0 }, { text: "Machinery produced for a factory", b: 0 },
  { text: "Unpaid housework", b: 1 }, { text: "Goods made and sold in the informal economy", b: 1 }, { text: "Second-hand goods resold", b: 1 }, { text: "The value of pollution caused", b: 1 },
], done: "GDP counts final goods and services produced and recorded." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["GDP", "Total value of final goods and services produced in a country in a year"],
  ["Nominal GDP", "GDP at current prices, not adjusted for inflation"],
  ["Real GDP", "GDP adjusted for inflation: measures change in output"],
  ["GDP per head", "GDP divided by population"],
  ["Informal economy", "Activity that is not regulated, recorded or taxed"],
  ["Economic growth rate", "Percentage change in real GDP"],
], done: "Good vocabulary scores marks." });
''' + calc_js([
    ("Real GDP was $500bn last year and is $520bn this year. What is the growth rate (%)?", 4, "20 ÷ 500 × 100 = <b>4%</b>.", None, None),
    ("Nominal GDP rises by 7% and prices rise by 3%. About what is the rise in real GDP (%)?", 4, "7 − 3 = <b>about 4%</b>.", "Subtract inflation.", None),
    ("An economy has real GDP of $600bn and a population of 20 million. What is real GDP per head ($)?", 30000, "$600bn ÷ 20m = <b>$30,000</b>.", "$600bn = 600,000m.", None),
    ("Real GDP grows by 3% but population grows by 4%. What is the approximate change in real GDP per head (%)?", -1, "3 − 4 = <b>about −1%</b>: population grew faster than output, so real GDP per head falls.", None, None),
    ("Real GDP was 200 in Year 1, 210 in Year 2 and 207 in Year 3. What is the growth rate in Year 3 (%, 1 d.p.)?", -1.4, "(207 − 210) ÷ 210 × 100 = <b>−1.4%</b>.", None, 0.1),
]) + mcq_js("qz1", [
    ("What does real GDP measure?", ["Output adjusted for inflation", "Prices only", "The size of the population", "Government spending"], 0, "Real GDP shows output at constant prices."),
    ("Nominal GDP rises by 5% and prices rise by 5%. Real GDP is likely to:", ["Rise by 5%", "Stay about the same", "Fall by 5%", "Double"], 1, "All the rise is due to price increases."),
    ("Which is a limitation of GDP as a measure of living standards?", ["It includes all output", "It does not show how income is shared", "It uses prices", "It is measured in money"], 1, "Averages hide inequality."),
    ("Real GDP per head is calculated as:", ["Real GDP × population", "Real GDP ÷ population", "Nominal GDP ÷ prices", "Real GDP − population"], 1, "Divide by the number of people."),
    ("Which is not counted in GDP?", ["Government spending on roads", "Unpaid housework", "Exports of cars", "A restaurant meal"], 1, "Unpaid work is not recorded."),
]) + "\n" + cards_js([("GDP", "The total value of final goods and services produced in a country in a year."), ("Nominal GDP", "GDP measured at current prices, not adjusted for inflation."), ("Real GDP", "GDP adjusted for inflation: measures the actual change in output."), ("GDP per head", "GDP divided by population."), ("Growth rate", "The percentage change in real GDP."), ("Informal economy", "The part of the economy not regulated, protected or taxed by the government."), ("Base year", "The year whose prices are used as the starting point for real GDP."), ("Living standards", "The quality and quantity of goods and services people can obtain.")]) + "labR();\n"
explore = '''
  <h2>Lab 1 · From nominal GDP to real GDP per head</h2>
  <p>Set nominal growth, inflation and population growth. Real growth removes inflation; GDP per head also takes account of population.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Real GDP growth</small><strong id="ra1"></strong></div><div><small>Real GDP per head growth</small><strong id="ra2"></strong></div><div><small>Nominal GDP growth</small><strong id="ra3"></strong></div></div><div class="verdict" id="rav"></div></div></div>
    <svg id="labR" viewBox="0 0 760 360" role="img" aria-label="Nominal, real and per head growth"></svg>
  </div>
'''
ex = exam(
    Q(1, "Calculate", 1, "Calculate India's economic growth rate in 2017 using the table: real GDP $8,750.0bn (2016) and $9,362.5bn (2017).", "Change ÷ original × 100.", "[A|(9,362.5 − 8,750.0) ÷ 8,750.0 × 100 = 7%.]"),
    Q(2, "Define", 2, "What is meant by real GDP?", "Two ideas: the value of output, and adjusted for inflation.",
      "[K|Real GDP is the total value of goods and services produced in a country in a year] [K|adjusted for changes in prices (inflation).]"),
    Q(3, "Explain", 4, "Explain why real GDP is a better measure of economic growth than nominal GDP.", "Prices can rise without output rising. Give a number if you can.",
      "[K|Nominal GDP is measured at current prices, so it rises if prices rise even when output is unchanged.] [N|Real GDP removes the effect of inflation, so it shows the change in the volume of goods and services produced.] [A|For example, if nominal GDP rises by 6% and prices rise by 4%, real output has risen only about 2%.]"),
    Q(4, "Explain", 4, "Explain why real GDP per head could fall even when real GDP rises.", "Population must rise faster than output.",
      "[K|Real GDP per head is real GDP divided by population.] [N|If population grows faster than real GDP, output is spread across more people,] [A|for example real GDP growing 2% while population grows 3%,] [N|so the average person has less output and real GDP per head falls.]"),
    Q(5, "Explain", 4, "Explain two limitations of using GDP to compare living standards.", "Two separate limitations: inequality, informal economy, pollution, health or leisure.",
      "[K|GDP does not show how income is shared.] [N|A country could have a high GDP but with most income going to a small group, so many people may have low living standards.] [K|It also leaves out the informal economy and unpaid work.] [N|Output in the informal economy is not recorded, so GDP could underestimate how much is produced, especially in poorer countries.]"),
)
tp = tips([
    ("Real, not nominal.", "Always use real GDP for growth; nominal includes price rises."),
    ("Growth rate = (new − old) ÷ old × 100.", "Divide by the old figure, not the new."),
    ("Show your working.", "Cambridge awards marks for method as well as answer."),
    ("GDP per head divides by population.", "It can fall even when GDP rises."),
    ("Know the limits of GDP.", "Inequality, informal economy, pollution, quality of life."),
], cmds("Define", "Calculate", "Explain"))
body = page(CL("4.5.2 Measurement of economic growth"), "Measurement of Economic Growth", "Real GDP, nominal GDP, GDP per head, how to calculate the growth rate, and the limits of GDP. Syllabus 4.5.2.",
    learn=learn, watch=watch(("Nominal and real GDP", "stR"), ("Calculating the growth rate", "stK")), explore=explore,
    practise=practise(("In GDP or left out?", "cl1", "card"), ("Match the term", "m1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("India's growth table", "A past paper gives India's real GDP, current account and car production for two years and asks for the growth rate. Real GDP rose by 7%.", "A real growth-rate calculation with a simple formula."),
        rw("Inflation and nominal GDP", "In countries with high inflation, such as Argentina in recent years, nominal GDP figures can rise sharply even when real output falls, which is why economists use real GDP.", "Why nominal figures can mislead."),
        rw("The informal economy", "In many low-income countries a large share of work is informal (street trading, small farms), so official GDP may understate total output.", "A limitation of GDP when comparing countries.")),
    exam=ex, tips=tp)
write("eg2", body, js, "Measurement of Economic Growth", "ig-growth-measurement")

# =========================================================== 4.5.3 Causes and consequences of growth
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Economic growth can be caused by an increase in <b>total demand</b>, an increase in the <b>quantity of resources</b> or an increase in the <b>quality of resources</b>. Growth has <b>advantages</b> (higher incomes, jobs, tax revenue) and <b>disadvantages</b> (pollution, inequality, inflation, a worse trade balance). Good answers separate the causes, then weigh the consequences for different groups.</p></div>

  <h2>Causes of growth</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>Examples</th><th>On the diagrams</th></tr>
    <tr><td><b>Increase in total demand</b></td><td>More consumer spending, investment, government spending or exports; lower interest rates; tax cuts</td><td>AD shifts right (actual growth)</td></tr>
    <tr><td><b>More resources (quantity)</b></td><td>Immigration, more people working, new investment in machinery, discovery of oil or minerals</td><td>AS shifts right, PPC out</td></tr>
    <tr><td><b>Better resources (quality)</b></td><td>Education and training, new technology, better management, healthier workers</td><td>AS shifts right, PPC out</td></tr>
  </table></div>
  <div class="grid2">
    <div class="card"><h3>Demand-led growth</h3><p>Works fastest, and when there is spare capacity output rises with little inflation. Near full capacity it mostly raises prices.</p></div>
    <div class="card"><h3>Supply-led growth</h3><p>Slower, but raises the economy's capacity, so growth can last without inflation.</p></div>
  </div>

  <h2>Advantages of growth</h2>
  <ul>
    <li><b>Higher incomes and living standards:</b> more goods and services per person.</li>
    <li><b>More jobs:</b> firms need more workers, so unemployment may fall.</li>
    <li><b>More tax revenue:</b> the government can fund healthcare, education and infrastructure, or reduce a deficit.</li>
    <li><b>Higher profits:</b> firms may invest more.</li>
    <li><b>Less poverty:</b> more output makes it easier to help the poor.</li>
  </ul>
  <h2>Disadvantages of growth</h2>
  <ul>
    <li><b>Pollution and resource use:</b> more output may mean more emissions, waste and depleted resources (environmental sustainability).</li>
    <li><b>Inequality:</b> the gains may go mainly to richer households and regions.</li>
    <li><b>Inflation:</b> fast demand growth near full capacity raises prices.</li>
    <li><b>Balance of payments:</b> higher incomes raise spending on imports, which may worsen the current account.</li>
    <li><b>Opportunity cost:</b> resources used to build capital now mean less consumption today; work and stress may rise.</li>
  </ul>
  <h2>Who is affected?</h2>
  <div class="tw"><table class="t">
    <tr><th>Group</th><th>Likely benefit</th><th>Possible cost</th></tr>
    <tr><td>Consumers</td><td>Higher incomes, more choice</td><td>Higher prices, pollution</td></tr>
    <tr><td>Workers</td><td>More jobs, higher wages</td><td>Pressure, inequality</td></tr>
    <tr><td>Firms</td><td>More sales and profit</td><td>Higher wage and input costs</td></tr>
    <tr><td>Government</td><td>More tax revenue</td><td>Pressure to spend on infrastructure, pollution costs</td></tr>
  </table></div>
'''
js = HEAD + COMMON + '''
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Demand-led and supply-led growth", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b> with some spare capacity.", s: { sh: 0, a: 0 } },
  { cap: "<b>Growth from higher demand:</b> consumption, investment, government spending or exports rise. AD shifts <b>right</b>. Real GDP rises and prices rise a little.", s: { sh: 14, a: 0 } },
  { cap: "<b>Evaluate:</b> push AD too far and the economy runs short of capacity. Output barely rises and most of the effect is <b>inflation</b>.", s: { sh: 40, a: 0 } },
  { cap: "<b>Growth from more or better resources:</b> AS shifts <b>right</b>. Real GDP rises and the price level <b>falls</b>: growth that can be sustained.", s: { sh: 0, a: 14 } },
] });
const GCH = ["Growth rises: real GDP and incomes increase", "Firms hire more workers: unemployment falls", "Higher incomes and profits raise tax revenue", "The government can spend more on services or cut its deficit", "But: more output may cause pollution and resource depletion", "And: gains may be unequal; imports and prices may rise"];
Lib.stepper($("#stB"), { w: 760, h: 400, label: "Benefits and costs of growth", base: { n: 0 }, draw: mkChain(GCH, "--good"), steps: chainSteps(["<b>Growth:</b> real GDP and incomes increase.", "<b>Jobs:</b> firms hire more workers and unemployment falls.", "<b>Tax revenue:</b> higher incomes and profits raise what the government collects.", "<b>Public services:</b> the government can spend more on health and education, or reduce its deficit.", "<b>Cost:</b> more output may mean more pollution and use of resources.", "<b>Cost:</b> the gains may be unequal, and higher incomes raise imports and may raise prices."]) });

/* Lab 1: AD vs AS growth */
function labC() {
  if (!$("#ca") || !$("#cb")) return;
  const sh = +$("#ca").value, a = +$("#cb").value, [y, p] = solve2(sh, a);
  $("#ca1").textContent = "+" + money(y - 50, 1); $("#ca2").textContent = (p - 50 >= 0.05 ? "+" : p - 50 <= -0.05 ? "−" : "") + money(Math.abs(p - 50), 1);
  $("#ca3").textContent = a > 0 && sh > 0 ? "Both" : a > 0 ? "Quantity or quality of resources" : sh > 0 ? "Demand" : "None";
  $("#cav").textContent = a === 0 && sh === 0 ? "Move a slider." : a === 0 ? `AD rises: output +${money(y - 50, 1)} but the price level +${money(p - 50, 1)}. Demand-led growth brings more inflationary pressure.` : sh === 0 ? `AS rises: output +${money(y - 50, 1)} and the price level ${p - 50 >= 0 ? "+" : "−"}${money(Math.abs(p - 50), 1)}. Supply-led growth can be sustained.` : "Both shift: strong growth with a modest change in prices.";
  $("#labC").innerHTML = adasChart({ sh, a });
}
Lib.slider($("#g1"), { id: "ca", label: "Rise in total demand (AD shift)", min: 0, max: 40, step: 2, value: 12, fmt: (v) => "+" + v, onInput: labC });
Lib.slider($("#g2"), { id: "cb", label: "More or better resources (AS shift)", min: 0, max: 30, step: 2, value: 0, fmt: (v) => "+" + v, onInput: labC });
/* Lab 2: winners and losers */
const WL = [
  { n: "Consumers", g: "Higher incomes and more choice; cheaper goods as firms expand.", c: "Higher prices if demand outpaces supply; pollution and congestion." },
  { n: "Workers", g: "More jobs, higher wages and more promotion chances.", c: "Pressure to work harder; those without the right skills may be left behind." },
  { n: "Producers and firms", g: "More sales and profit; funds for investment.", c: "Higher wage and input costs; stricter rules to limit pollution." },
  { n: "The government", g: "More tax revenue, fewer benefit payments.", c: "Calls for more spending on infrastructure and cleaning up pollution." },
  { n: "The environment", g: "Richer countries may pay for cleaner technology.", c: "More emissions, waste and depletion of resources." },
  { n: "Future generations", g: "Investment now leaves more capital and skills.", c: "Resources used up and pollution left behind." },
];
button_table("wlBtns", "wlOut", WL, 0, (p) => `<div class="tw"><table class="t"><tr><th>Possible benefit</th><th>Possible cost</th></tr><tr><td>${p.g}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a cause of growth from <b>higher demand</b>, <b>more resources</b> or <b>better resources</b>?", buckets: [{ label: "Higher demand" }, { label: "More resources" }, { label: "Better resources" }], items: [
  { text: "Government spending rises", b: 0 }, { text: "Exports increase", b: 0 }, { text: "Interest rates fall, so firms invest", b: 0 },
  { text: "Immigration raises the labour force", b: 1 }, { text: "Oil is discovered", b: 1 }, { text: "New factories are built", b: 1 },
  { text: "Workers receive more training", b: 2 }, { text: "New technology raises productivity", b: 2 }, { text: "Better healthcare reduces sick days", b: 2 },
], done: "Demand, quantity, quality: the three causes in the syllabus." });
Lib.classify($("#cl2"), { prompt: "Is each an <b>advantage</b> or a <b>disadvantage</b> of economic growth?", buckets: [{ label: "Advantage" }, { label: "Disadvantage" }], items: [
  { text: "Higher incomes", b: 0 }, { text: "Fewer people unemployed", b: 0 }, { text: "More tax revenue for schools", b: 0 }, { text: "Higher profits for firms", b: 0 },
  { text: "More pollution", b: 1 }, { text: "Resources are used up", b: 1 }, { text: "Richer households gain most", b: 1 }, { text: "Higher imports and a worse current account", b: 1 },
], done: "Always give both sides." });
Lib.match($("#m1"), { prompt: "Match the cause to the effect on the diagrams.", pairs: [
  ["Rise in consumer spending", "AD shifts right"],
  ["Immigration of workers", "AS shifts right: more labour"],
  ["Training programme", "AS shifts right: better labour"],
  ["Discovery of a mineral deposit", "AS shifts right: more land"],
  ["Investment in new machines", "AS shifts right: more capital"],
  ["New technology", "AS shifts right: higher productivity"],
], done: "Link each cause to a diagram." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how higher government spending could cause growth</b>.", items: [
  "The government spends more on infrastructure",
  "Firms and workers are paid and spend part of it",
  "Aggregate demand shifts to the right",
  "Real GDP rises: economic growth",
  "Firms hire more workers and tax revenue rises",
], done: "A demand-led growth chain." });
''' + calc_js([
    ("Real GDP rises from $250bn to $260bn. What is the growth rate (%)?", 4, "10 ÷ 250 × 100 = <b>4%</b>.", None, None),
    ("The labour force rises from 20 million to 21 million and output per worker stays the same. By what percentage does output rise?", 5, "1 ÷ 20 × 100 = <b>5%</b>.", None, None),
    ("Growth raises tax revenue from $50bn to $56bn. What is the percentage rise in tax revenue?", 12, "6 ÷ 50 × 100 = <b>12%</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which could cause economic growth by increasing the quality of resources?", ["Immigration", "A rise in exports", "Training and education", "A tax cut"], 2, "Training improves the quality of labour."),
    ("Which is a possible disadvantage of economic growth?", ["Higher incomes", "More jobs", "More pollution", "More tax revenue"], 2, "Higher output can mean more emissions."),
    ("A rise in total demand when the economy has spare capacity is most likely to cause:", ["Growth with little inflation", "Falling output", "Higher unemployment", "A lower exchange rate only"], 0, "Spare resources can be used."),
    ("Which is most likely to raise an economy's capacity in the long run?", ["Higher consumer spending", "Investment in capital and skills", "A fall in interest rates", "Lower exports"], 1, "More and better resources shift AS."),
    ("Economic growth could conflict with the balance of payments because:", ["Higher incomes raise spending on imports", "Higher incomes reduce imports", "It lowers the exchange rate", "It raises exports only"], 0, "More income means more imports."),
]) + "\n" + cards_js([("Total demand", "Aggregate demand: C + I + G + (X − M)."), ("Quantity of resources", "The amount of land, labour, capital or enterprise available."), ("Quality of resources", "How productive resources are, for example skills and technology."), ("Immigration", "People moving into a country, which can raise the labour force."), ("Investment", "Spending on capital goods such as machinery and buildings."), ("Environmental sustainability", "Meeting today's needs without damaging the ability of future generations to meet theirs."), ("Inequality", "An unequal distribution of income or wealth."), ("Living standards", "The quality and quantity of goods and services people can obtain.")]) + "labC();\n"
explore = '''
  <h2>Lab 1 · Demand-led or supply-led growth?</h2>
  <p>Raise total demand, resources, or both. Compare the effect on output and the price level.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Change in real GDP</small><strong id="ca1"></strong></div><div><small>Change in price level</small><strong id="ca2"></strong></div><div><small>Cause</small><strong id="ca3"></strong></div></div><div class="verdict" id="cav"></div></div></div>
    <svg id="labC" viewBox="0 0 760 400" role="img" aria-label="Aggregate demand and supply diagram"></svg>
  </div>

  <h2>Lab 2 · Who gains and who loses from growth?</h2>
  <p>Pick a group to see the likely benefits and costs.</p>
  <div class="card"><div class="row" id="wlBtns"></div><div id="wlOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain two benefits of a higher economic growth rate. (Feb/Mar 2020, P22)", "Two separate benefits, each developed: incomes and living standards, jobs, tax revenue, profits.",
      "[K|Higher growth means higher output and incomes,] [N|so people can afford more goods and services and living standards could rise.] [K|It could also increase employment.] [N|Firms need more workers to produce more output, so unemployment is likely to fall and more households have an income.]"),
    Q(2, "Analyse", 6, "Analyse how higher government spending could increase economic growth. (Feb/Mar 2021, P22)", "Government spending is part of AD. Chain: G up, AD right, multiplier, output rises. Longer run: capital and skills.",
      "[K|Government spending is a component of aggregate demand.] [A|If the government spends more on infrastructure or schools,] [N|firms and workers receive extra income and spend part of it, so AD could shift to the right with a multiplier effect.] [N|Real GDP rises, which is economic growth, and firms may hire more workers.] [N|Spending on infrastructure or education could also raise the quality and quantity of resources, raising productive capacity in the long run.] [E|However, if the economy is close to capacity, mostly prices might rise.]", key=True),
    Q(3, "Analyse", 6, "Analyse how an ageing population may affect a country's economic growth rate. (Feb/Mar 2025, P22)", "Population ages: fewer workers, more retired. Two sides if possible: lower labour supply; more spending on health and pensions.",
      "[K|An ageing population means a rising share of people are retired.] [N|The number of workers relative to the total population may fall, so the quantity of labour could fall and productive capacity could grow more slowly.] [N|Higher government spending on pensions and healthcare may need more tax or borrowing, which could reduce spending on other things that raise growth.] [N|Older workers may have experience, and demand for healthcare and leisure may rise, which could create growth in some industries.] [E|Overall the effect on growth is likely to be negative unless the country raises productivity or retirement ages.]", key=True),
    Q(4, "Analyse", 6, "Analyse how economic growth conflicts with balance of payments stability. (May/June 2021, P23)", "Growth raises incomes, which raises imports; a current account deficit may result. Mention exports if you can.",
      "[K|Economic growth is a rise in real GDP, while balance of payments stability means the current account is not in persistent deficit.] [N|As incomes rise, households and firms spend more, including on imports.] [N|If imports rise faster than exports, the current account deficit could widen.] [N|Firms may also import more machinery and raw materials to expand output.] [E|The conflict may be smaller if growth comes from higher exports.]", key=True),
    Q(5, "Discuss", 8, "Discuss whether or not governments should aim for a high rate of economic growth. (May/June 2022, P21)", "Advantages: incomes, jobs, tax revenue. Disadvantages: pollution, inequality, inflation, imports. End with 'it depends on…' what kind of growth and how the gains are used.",
      "[K|Economic growth is a rise in real GDP over time.] [N|A high growth rate could raise incomes and living standards, because there is more to spend on goods and services.] [N|It could also reduce unemployment as firms hire more workers, and raise tax revenue so that the government can pay for health, education and infrastructure.] [E|These gains are larger when growth is shared across the population.] [N|On the other hand, high growth could cause more pollution and use up resources, which harms future generations, and it may widen the gap between rich and poor.] [N|If growth is driven by demand near full capacity it could cause inflation, and higher incomes could raise imports and worsen the current account.] [E|Overall, governments are likely to benefit from aiming for growth, but they should consider the kind of growth: sustainable growth from better resources with policies to limit pollution and share the gains is more likely to benefit the economy than fast growth with high costs.]", key=True),
)
tp = tips([
    ("Three causes:", "demand, quantity of resources, quality of resources."),
    ("Link each cause to a diagram.", "AD shifts right, or AS shifts right."),
    ("Give both sides on 'should aim for growth'.", "Incomes, jobs, tax revenue against pollution, inequality, inflation, imports."),
    ("Say who gains.", "Consumers, workers, firms, government: and who may lose."),
    ("Evaluate with 'it depends'.", "On the cause of growth, the state of the economy, and how gains are shared."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("4.5.3 Causes and consequences of economic growth"), "Causes and Consequences of Economic Growth", "How growth can come from higher demand, more resources or better resources, and its advantages and disadvantages. Syllabus 4.5.3.",
    learn=learn, watch=watch(("Demand-led and supply-led growth", "stS"), ("Benefits and costs of growth", "stB")), explore=explore,
    practise=practise(("What caused growth?", "cl1", "card"), ("Advantage or disadvantage?", "cl2", "card"), ("Match the cause", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Growth fuelled by investment", "Fast-growing economies such as South Korea and China invested a large share of output in capital goods and education, which raised capacity for decades.", "Growth from more and better resources, with a long time lag."),
        rw("Growth and pollution", "A past paper describes India's rise in output bringing more air pollution, while the government encourages growth through investment and trade.", "A disadvantage of growth: environmental cost."),
        rw("Growth that bypasses some people", "In several fast-growing economies the gains have been concentrated in cities and richer households, widening the gap with rural areas.", "Inequality as a cost of growth."),
        rw("Oil discoveries", "Discovery of oil or gas can raise an economy's output and exports, but may leave it dependent on one resource.", "More resources raising growth, with a risk if prices fall.")),
    exam=ex, tips=tp)
write("eg3", body, js, "Causes and Consequences of Economic Growth", "ig-growth-causes")

# =========================================================== 4.5.4 Recession
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <span class="kw">recession</span> is a period when real GDP falls, usually defined as a fall for <b>two or more successive quarters</b>. It may be caused by a fall in <b>total demand</b>, or by a fall in the <b>quantity</b> or <b>quality</b> of resources. A recession hurts consumers, workers, firms and the government, and the effects can build on each other.</p></div>

  <h2>Causes of a recession</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>Examples</th><th>Effect</th></tr>
    <tr><td><b>Fall in total demand</b></td><td>Lower consumer or business confidence, higher interest rates, cuts in government spending, falling exports (a world slowdown), a rise in imports</td><td>AD shifts left</td></tr>
    <tr><td><b>Fall in quantity of resources</b></td><td>Emigration, a fall in population, war, natural disasters destroying factories and farms</td><td>AS shifts left</td></tr>
    <tr><td><b>Fall in quality of resources</b></td><td>Cuts to education and healthcare, falling investment so capital becomes outdated</td><td>AS shifts left</td></tr>
  </table></div>

  <h2>Consequences of a recession</h2>
  <div class="tw"><table class="t">
    <tr><th>Who</th><th>Possible consequences</th></tr>
    <tr><td><b>Consumers</b></td><td>Lower incomes and living standards; lower confidence so they spend and borrow less; they may fall into debt</td></tr>
    <tr><td><b>Workers</b></td><td>Unemployment rises; wages may be cut or frozen; fewer hours and job openings</td></tr>
    <tr><td><b>Producers and firms</b></td><td>Falling sales and profits; less investment; some firms close, especially weaker ones; falling prices</td></tr>
    <tr><td><b>The government</b></td><td>Tax revenue falls and benefit spending rises, so the budget deficit widens; borrowing and debt rise</td></tr>
  </table></div>
  <p>A recession can feed on itself: unemployment lowers spending, which lowers sales, which leads firms to cut more jobs. Firms may also cut investment because of low confidence, which reduces productive capacity for the future.</p>

  <h2>Ending a recession</h2>
  <ul>
    <li><b>Demand-side policy:</b> cut interest rates, cut taxes or raise government spending to raise AD.</li>
    <li><b>Automatic stabilisers</b> cushion the fall: benefits rise and taxes fall without new decisions.</li>
    <li><b>Supply-side policy</b> helps recovery in the long run, but is slow.</li>
    <li>Limits: low confidence may stop people spending, deficits may already be large, and effects take time.</li>
  </ul>
'''
js = HEAD + COMMON + CYCLE + '''
Lib.stepper($("#stC"), { w: 760, h: 400, label: "Recession in the business cycle", base: { t: 20, lbl: "" }, draw: cycleChart, steps: [
  { cap: "The economy is growing, but near the top of a boom.", s: { t: 12, lbl: "Boom" } },
  { cap: "Spending slows and real GDP begins to <b>fall</b>. After two quarters of falling real GDP, it is a <b>recession</b>.", s: { t: 27, lbl: "Falling GDP" } },
  { cap: "Output keeps falling to a <b>trough</b>. Unemployment is high and tax revenue is low.", s: { t: 37, lbl: "Trough" } },
  { cap: "<b>Recovery</b> begins when real GDP rises again.", s: { t: 48, lbl: "Recovery" } },
] });
Lib.stepper($("#stS"), { w: 760, h: 400, label: "A fall in total demand", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b>.", s: { sh: 0, a: 0 } },
  { cap: "Confidence collapses, the interest rate rises, or exports fall. <b>AD shifts left</b>.", s: { sh: -16, a: 0 } },
  { cap: "Real GDP <b>falls</b> to Y₁, and the price level falls or rises more slowly. Firms cut output and workers.", s: { sh: -16, a: 0 } },
  { cap: "Or the economy loses resources: war, disaster or emigration. <b>AS shifts left</b>, and real GDP falls with prices rising: a more damaging recession.", s: { sh: 0, a: -12 } },
] });
const RCH = ["Total demand falls: consumers and firms cut spending", "Firms' sales and profits fall; investment is cut", "Firms lay off workers: unemployment rises", "Household incomes fall, so spending falls further", "Tax revenue falls and benefit spending rises: bigger deficit", "Output falls again: the recession may deepen"];
Lib.stepper($("#stR"), { w: 760, h: 400, label: "The recession spiral", base: { n: 0 }, draw: mkChain(RCH, "--bad"), steps: chainSteps(["<b>Demand falls</b>: consumers and firms cut spending.", "<b>Firms:</b> sales and profits fall, so they cut investment.", "<b>Workers:</b> firms lay off workers, so unemployment rises.", "<b>Consumers:</b> lower incomes mean even less spending.", "<b>Government:</b> tax revenue falls and benefit spending rises, so the deficit widens.", "<b>The spiral:</b> less spending cuts output again. Policy (lower rates, stimulus) is needed to break it."]) });

/* Lab 1: effects of a fall in GDP */
function labF() {
  if (!$("#fa")) return;
  const d = +$("#fa").value, un = 5 + 0.5 * d, rev = 100 * (1 - 1.5 * d / 100), ben = 20 * (1 + 3 * d / 100), bal = rev - (100 + ben - 20);
  $("#fa1").textContent = "−" + d + "%"; $("#fa2").textContent = money(un, 1) + "%"; $("#fa3").textContent = "$" + money(rev, 0) + "bn"; $("#fa4").textContent = (bal >= 0 ? "+" : "−") + "$" + money(Math.abs(bal), 1) + "bn";
  $("#fav").textContent = d === 0 ? "No fall in GDP. Move the slider." : `Real GDP falls ${d}%, so unemployment rises to about ${money(un, 1)}%. Tax revenue falls to $${money(rev, 0)}bn while benefit spending rises, so the budget balance moves to ${bal >= 0 ? "+" : "−"}$${money(Math.abs(bal), 1)}bn: automatic stabilisers widen the deficit.`;
  const base = 300, k = 2; let o = SV.line(80, base, 700, base);
  [["Tax revenue", rev, "--accent"], ["Benefit spending", ben, "--warn"], ["Unemployment %", un, "--bad"]].forEach(([n, v, c], i) => {
    const x = 120 + i * 190, kk = i === 2 ? 14 : 2, h = v * kk;
    o += SV.rect(x, base - h, 130, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, base - h - 8, (i === 2 ? money(v, 1) + "%" : "$" + money(v, 0) + "bn"), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 22, n, "sm", { "text-anchor": "middle" });
  });
  $("#labF").innerHTML = o;
}
Lib.slider($("#g1"), { id: "fa", label: "Fall in real GDP", min: 0, max: 10, step: 1, value: 4, fmt: (v) => "−" + v + "%", onInput: labF });
/* Lab 2: causes picker */
const RC = [
  { n: "Fall in consumer confidence", t: "Total demand", e: "Households fear unemployment and cut spending and borrowing: AD shifts left.", ex: "Financial crisis, rising unemployment news" },
  { n: "Higher interest rates", t: "Total demand", e: "Loans and mortgages cost more, so consumption and investment fall.", ex: "Central bank tightening to fight inflation" },
  { n: "Cut in government spending", t: "Total demand", e: "G falls and jobs in the public sector are lost: AD shifts left.", ex: "Austerity after a debt crisis" },
  { n: "Fall in exports", t: "Total demand", e: "A world slowdown reduces demand for the country's exports.", ex: "Global recession, loss of a major trading partner" },
  { n: "Emigration of workers", t: "Quantity of resources", e: "The labour force shrinks: AS shifts left.", ex: "Albania after 2013 (past paper)" },
  { n: "War or natural disaster", t: "Quantity of resources", e: "Factories, farms and infrastructure are destroyed: AS shifts left.", ex: "Earthquakes, floods, conflict" },
  { n: "Falling investment and skills", t: "Quality of resources", e: "Capital becomes outdated and skills decline: productivity and AS fall.", ex: "Long-term cuts in education and training" },
];
button_table("rcBtns", "rcOut", RC, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type of cause</th><th>How it causes recession</th><th>Example</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td><td>${p.ex}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each cause of recession a fall in <b>total demand</b>, in the <b>quantity of resources</b> or in the <b>quality of resources</b>?", buckets: [{ label: "Total demand" }, { label: "Quantity of resources" }, { label: "Quality of resources" }], items: [
  { text: "Consumer confidence collapses", b: 0 }, { text: "Interest rates rise sharply", b: 0 }, { text: "Government spending is cut", b: 0 },
  { text: "Workers emigrate in large numbers", b: 1 }, { text: "A war destroys factories", b: 1 }, { text: "A natural disaster destroys farmland", b: 1 },
  { text: "Education spending is cut for many years", b: 2 }, { text: "Investment falls so machinery becomes outdated", b: 2 },
], done: "Same three headings as growth, in reverse." });
Lib.classify($("#cl2"), { prompt: "Who is affected? Put each consequence of recession with the <b>group</b>.", buckets: [{ label: "Consumers" }, { label: "Workers" }, { label: "Firms" }, { label: "Government" }], items: [
  { text: "Lower incomes and lower confidence", b: 0 }, { text: "Fall into debt", b: 0 },
  { text: "Unemployment rises", b: 1 }, { text: "Pay is frozen or cut", b: 1 },
  { text: "Falling sales and profits", b: 2 }, { text: "Some firms close", b: 2 },
  { text: "Tax revenue falls", b: 3 }, { text: "Benefit spending rises", b: 3 },
], done: "Four groups: consumers, workers, firms, government." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Recession", "A fall in real GDP for two or more successive quarters"],
  ["Trough", "The lowest point of output in the cycle"],
  ["Automatic stabilisers", "Spending and taxes that move with the cycle and cushion falls in demand"],
  ["Unemployment", "People who are able and willing to work but cannot find a job"],
  ["Budget deficit", "Government spending is higher than revenue"],
  ["Austerity", "Cuts in government spending and rises in taxes to reduce a deficit"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a rise in the interest rate could cause a recession</b>.", items: [
  "The central bank raises the interest rate",
  "Borrowing costs more and saving is rewarded",
  "Consumption and investment fall",
  "Aggregate demand shifts left",
  "Real GDP falls: recession",
], done: "A causal chain for a 6-mark answer." });
''' + calc_js([
    ("Real GDP falls from $400bn to $380bn. What is the percentage change?", -5, "(380 − 400) ÷ 400 × 100 = <b>−5%</b>.", None, None),
    ("Tax revenue is $80bn. In a recession it falls by 10%. What is the new tax revenue ($bn)?", 72, "80 × 0.9 = <b>$72bn</b>.", None, None),
    ("The unemployment rate rises from 6% to 9%. The labour force is 30 million. How many more people are unemployed (millions)?", 0.9, "3% × 30m = <b>0.9 million</b>.", None, None),
    ("A government spends $100bn and raises $85bn. In a recession revenue falls to $80bn and spending rises to $108bn. How big is the new deficit ($bn)?", 28, "108 − 80 = <b>$28bn</b>.", None, None),
]) + mcq_js("qz1", [
    ("A recession is usually defined as:", ["A fall in prices", "Two or more successive quarters of falling real GDP", "A rise in unemployment", "A fall in the exchange rate"], 1, "Real GDP falls for two quarters."),
    ("Which is a likely cause of a recession?", ["A rise in consumer confidence", "A rise in interest rates leading to lower spending", "A rise in exports", "More investment"], 1, "Higher rates cut consumption and investment."),
    ("Which is a likely consequence of a recession for the government?", ["Higher tax revenue", "Lower benefit spending", "A wider budget deficit", "Fewer borrowing needs"], 2, "Tax revenue falls and benefits rise."),
    ("Which could cause a recession by reducing the quantity of resources?", ["A rise in consumer spending", "Large-scale emigration of workers", "More training", "Lower interest rates"], 1, "Fewer workers reduce capacity."),
    ("Automatic stabilisers help in a recession because:", ["Taxes rise and benefits fall", "Benefits rise and tax revenue falls, supporting spending", "The exchange rate falls", "Interest rates rise"], 1, "They cushion the fall in demand."),
]) + "\n" + cards_js([("Recession", "A fall in real GDP for two or more successive quarters."), ("Trough", "The lowest point of output in the business cycle."), ("Recovery", "Output rising again after a recession."), ("Total demand", "Aggregate demand: C + I + G + (X − M)."), ("Consumer confidence", "How optimistic households are about the future, which affects spending and borrowing."), ("Emigration", "People leaving a country to live elsewhere."), ("Automatic stabilisers", "Government spending and taxes that cushion falls in demand without new decisions."), ("Austerity", "Cuts in government spending and rises in taxes to reduce a deficit."), ("Unemployment", "People able and willing to work who cannot find a job.")]) + "labF();\n"
explore = '''
  <h2>Lab 1 · What a fall in GDP does to jobs and the budget</h2>
  <p>Start with unemployment at 5%, tax revenue of $100bn and benefit spending of $20bn. Cut real GDP and watch the automatic effects.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Fall in real GDP</small><strong id="fa1"></strong></div><div><small>Unemployment</small><strong id="fa2"></strong></div><div><small>Tax revenue</small><strong id="fa3"></strong></div><div><small>Budget balance (start 0)</small><strong id="fa4"></strong></div></div><div class="verdict" id="fav"></div></div></div>
    <svg id="labF" viewBox="0 0 760 340" role="img" aria-label="Tax revenue, benefit spending and unemployment in a recession"></svg>
    <p class="note">Illustrative model: each 1% fall in GDP raises unemployment by 0.5 points, cuts tax revenue by 1.5% and raises benefit spending by 3%.</p>
  </div>

  <h2>Lab 2 · Causes of recession</h2>
  <p>Pick a cause to see how it brings on a recession.</p>
  <div class="card"><div class="row" id="rcBtns"></div><div id="rcOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "What is meant by a recession?", "Real GDP falls, for two or more successive quarters.",
      "[K|A recession is a fall in real GDP] [K|for two or more successive quarters (six months or more).]"),
    Q(2, "Explain", 4, "Explain two causes of a recession. (May/June 2023, P23)", "Two different causes, each developed. Fall in AD (confidence, rates, G, exports), fewer workers (emigration), loss of resources (war, disaster).",
      "[K|One cause is a fall in total demand.] [N|If consumer confidence falls, households may cut spending and borrowing, so aggregate demand shifts left and real GDP falls.] [K|A second cause is a fall in the quantity of resources, for example emigration.] [N|If many workers leave, the labour force and productive capacity could fall, so output may fall.]"),
    Q(3, "Explain", 4, "Explain two disadvantages of a recession. (May/June 2024, P21)", "Two different disadvantages: unemployment, lower incomes, firm closures, lower investment, higher deficit.",
      "[K|One disadvantage is higher unemployment.] [N|Firms cut output and lay off workers, so household incomes fall and the government has to pay more unemployment benefit.] [K|A second is lower profits and investment.] [N|With less demand, firms' profits fall and some may close, and low confidence could reduce investment in new machinery.]"),
    Q(4, "Identify", 2, "Identify two reasons why tax revenue is likely to fall during a recession. (May/June 2024, P22)", "Short answers: lower incomes, lower spending, lower profits.",
      "[K|Lower incomes mean less income tax.] [K|Lower spending means less sales tax (and lower profits mean less corporation tax).]"),
    Q(5, "Analyse", 6, "Analyse how a rise in the interest rate could cause a recession. (May/June 2021, P22)", "Chain: rate up, borrowing costs, C and I fall, AD left, GDP falls. Say what happens to firms and households.",
      "[K|A rise in the interest rate raises the cost of borrowing and the reward for saving.] [N|Households with loans and mortgages have less to spend and saving becomes more attractive, so consumption could fall.] [N|Firms find fewer investment projects profitable, so investment may fall.] [N|Lower consumption and investment shift aggregate demand to the left, so real GDP falls.] [N|If it falls for two successive quarters, the economy is in recession.] [E|The effect could be larger if confidence is already low.]", key=True),
    Q(6, "Discuss", 8, "Discuss whether or not a reduction in income tax will end a recession. (Feb/Mar 2022, P22)", "For: raises disposable income and AD. Against: people may save it, confidence, time lag, deficit, and other policies may be better.",
      "[K|A recession is a fall in real GDP for at least two quarters, and a cut in income tax is expansionary fiscal policy.] [N|Lower income tax raises disposable income, so consumption could rise and AD could shift right.] [N|Higher spending may encourage firms to produce more and hire workers, so unemployment may fall and real GDP could start to rise.] [E|The effect is likely to be stronger if households have low incomes and spend most of what they receive.] [N|However, in a recession people may be worried about their jobs and could save the tax cut, so spending might not rise by much.] [N|The cut also reduces government revenue when it is already falling, so the deficit may widen, and the effects take time.] [E|Overall, an income tax cut could help but is unlikely to end a recession on its own; it depends on how much is spent, the cause of the recession and whether it is combined with lower interest rates or government spending.]", key=True),
)
tp = tips([
    ("Recession = two or more quarters of falling real GDP.", "Quote this."),
    ("Three causes:", "fall in demand, fewer resources, lower-quality resources."),
    ("Name the group affected.", "Consumers, workers, firms, government."),
    ("Recession widens the deficit by itself.", "Tax revenue falls, benefit spending rises."),
    ("Evaluate policies for ending recession.", "Low confidence, time lags, the deficit, size of the fall."),
], cmds("Define", "Identify", "Explain", "Analyse", "Discuss"))
body = page(CL("4.5.4 Causes and consequences of recession"), "Causes and Consequences of Recession", "What a recession is, why it happens, and how it affects consumers, workers, firms and the government. Syllabus 4.5.4.",
    learn=learn, watch=watch(("Recession in the business cycle", "stC"), ("A fall in total demand", "stS"), ("The recession spiral", "stR")), explore=explore,
    practise=practise(("What caused it?", "cl1", "card"), ("Who is affected?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("The 2008 financial crisis", "After banks in the US and Europe ran into trouble in 2008, lending dried up, confidence collapsed and many economies fell into recession. Unemployment rose and governments' deficits widened.", "A fall in demand, with consequences for workers, firms and government."),
        rw("COVID-19 in 2020", "Lockdowns caused real GDP to fall sharply in most countries in 2020. Governments paid wage support and cut interest rates, which raised their deficits.", "A sharp recession and policy response. A fall in quantity of resources (workers unable to work) and demand."),
        rw("Albania and emigration", "A past paper notes that after Albania's 2013 recession, emigration rose and many workers abroad did not wish to return.", "A fall in the quantity of resources as a cause and consequence."),
        rw("Austerity in Greece", "During its crisis Greece cut spending and raised taxes. Output fell sharply for several years and unemployment passed 20%.", "How the recession spiral deepens, and the limits of cutting spending.")),
    exam=ex, tips=tp)
write("eg4", body, js, "Causes and Consequences of Recession", "ig-growth-recession")

# =========================================================== 4.5.5 Policies
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Governments can use a range of policies to promote economic growth: <b>fiscal</b>, <b>monetary</b> and <b>supply-side</b> policy, plus encouraging <b>investment</b> and <b>trade</b>. Demand-side policies work quickly but can cause inflation. Supply-side policies raise capacity but are slow. How effective each is depends on the cause of weak growth and the state of the economy.</p></div>

  <h2>The range of policies</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>Example</th><th>How it promotes growth</th></tr>
    <tr><td><b>Fiscal</b></td><td>Raise government spending, cut taxes</td><td>AD shifts right; infrastructure and education also raise capacity</td></tr>
    <tr><td><b>Monetary</b></td><td>Cut interest rates, increase money supply, lower the exchange rate</td><td>Cheaper borrowing raises C and I; a lower exchange rate raises exports</td></tr>
    <tr><td><b>Supply-side</b></td><td>Education and training, infrastructure, deregulation, lower direct taxes, privatisation</td><td>Raises quantity or quality of resources: AS shifts right</td></tr>
    <tr><td><b>Investment policies</b></td><td>Tax breaks for investment, subsidies, attracting multinational firms</td><td>More capital, jobs and technology</td></tr>
    <tr><td><b>Trade policies</b></td><td>Free trade agreements, export support, fewer trade barriers</td><td>Larger markets, more exports, competition and technology</td></tr>
  </table></div>

  <h2>How effective?</h2>
  <div class="grid2">
    <div class="card"><h3>Demand-side policies</h3><ul><li><b>Pros:</b> relatively quick; helpful when there is spare capacity.</li><li><b>Cons:</b> risk of inflation near full capacity; bigger deficit (fiscal); effect of rate cuts weak if confidence is low; higher imports.</li></ul></div>
    <div class="card"><h3>Supply-side policies</h3><ul><li><b>Pros:</b> raise capacity, so growth lasts and inflation is lower.</li><li><b>Cons:</b> slow, costly, uncertain; some measures widen inequality.</li></ul></div>
  </div>
  <div class="grid2">
    <div class="card"><h3>Investment and trade</h3><ul><li><b>Pros:</b> bring capital, skills and bigger markets.</li><li><b>Cons:</b> exposes firms to competition; dependence on other countries; foreign firms may take profits out.</li></ul></div>
    <div class="card"><h3>Choosing a policy</h3><p>If growth is low because <b>demand</b> is weak, demand-side policy fits. If it is low because <b>resources are scarce or low quality</b>, supply-side policy fits. Often a mix is best.</p></div>
  </div>

  <h2>Evaluating policy choices</h2>
  <ul>
    <li><b>Time lags</b> and <b>size of the multiplier</b> or response.</li>
    <li><b>Spare capacity:</b> with little spare capacity extra demand mostly raises prices.</li>
    <li><b>Costs:</b> deficits, debt, opportunity cost.</li>
    <li><b>Conflicts with other aims:</b> inflation, current account, inequality, environment.</li>
    <li><b>Sustainability:</b> growth that damages the environment cannot be sustained.</li>
  </ul>
'''
js = HEAD + COMMON + '''
const PCH = ["Government cuts interest rates and raises spending", "Borrowing and spending rise: AD shifts right", "Real GDP rises quickly if there is spare capacity", "But the price level may rise, and imports and the deficit grow", "Government also invests in education and infrastructure", "AS shifts right over time: growth that can last"];
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Short-run and long-run growth policies", base: { n: 0 }, draw: mkChain(PCH, "--accent"), steps: chainSteps(["<b>Demand-side:</b> the government cuts interest rates and raises spending.", "Borrowing and spending rise: <b>AD shifts right</b>.", "If there is <b>spare capacity</b>, real GDP rises quickly.", "<b>Cost:</b> the price level may rise, imports rise and the deficit grows.", "<b>Supply-side:</b> the government also invests in education and infrastructure.", "<b>AS shifts right</b> over the years: higher capacity, so growth can last with less inflation."]) });
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Demand-side and supply-side policy", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b>.", s: { sh: 0, a: 0 } },
  { cap: "<b>Demand-side policy</b> (lower interest rates, higher spending, lower taxes): AD shifts right. Output rises quickly but the price level rises.", s: { sh: 14, a: 0 } },
  { cap: "<b>Supply-side policy</b> (education, infrastructure, deregulation): AS shifts right over time. Output rises and the price level falls.", s: { sh: 0, a: 14 } },
  { cap: "A <b>mix of both</b> gives strong growth with a stable price level: demand-side policy for the short run and supply-side policy for the long run.", s: { sh: 14, a: 14 } },
] });

/* Lab 1: policy simulator */
function labP() {
  if (!$("#pa") || !$("#pb") || !$("#pc")) return;
  const f = +$("#pa").value, m = +$("#pb").value, s = +$("#pc").value, sh = f + m, [y, p] = solve2(sh, s);
  $("#pa1").textContent = "+" + money(y - 50, 1); $("#pa2").textContent = (p - 50 >= 0.05 ? "+" : p - 50 <= -0.05 ? "−" : "") + money(Math.abs(p - 50), 1);
  $("#pa3").textContent = y > 60 ? "High" : y > 54 ? "Medium" : "Low";
  $("#pav").textContent = sh === 0 && s === 0 ? "Choose a policy mix." : `Output rises by ${money(y - 50, 1)} and the price level by ${p - 50 >= 0 ? "+" : "−"}${money(Math.abs(p - 50), 1)}. ${y - 50 > 2 * Math.max(0.1, p - 50) ? "Most of the effect is extra output: growth with limited inflation." : "A large share is inflation: policy may be pushing against capacity."}${s === 0 && sh > 25 ? " Demand-side policy on its own is running out of room." : ""}${s > 0 ? " The supply-side part takes years to build." : ""}`;
  $("#labP").innerHTML = adasChart({ sh, a: s });
}
Lib.slider($("#g1"), { id: "pa", label: "Fiscal policy (AD shift)", min: 0, max: 25, step: 1, value: 8, fmt: (v) => "+" + v, onInput: labP });
Lib.slider($("#g2"), { id: "pb", label: "Monetary policy (AD shift)", min: 0, max: 25, step: 1, value: 8, fmt: (v) => "+" + v, onInput: labP });
Lib.slider($("#g3"), { id: "pc", label: "Supply-side policy (AS shift)", min: 0, max: 30, step: 2, value: 0, fmt: (v) => "+" + v, onInput: labP });
/* Lab 2: policy picker */
const PL = [
  { n: "Cut interest rates", t: "Monetary", w: "Cheaper borrowing raises consumption and investment.", sp: "Fast to change; effects take months", c: "Weak if confidence is low; may raise inflation and imports; hurts savers." },
  { n: "Raise government spending", t: "Fiscal", w: "G adds to AD with a multiplier effect; infrastructure and education raise capacity.", sp: "Medium", c: "Bigger deficit and debt; opportunity cost; inflation near capacity." },
  { n: "Cut taxes", t: "Fiscal", w: "More disposable income raises C; corporation tax cuts raise I.", sp: "Medium", c: "Part may be saved; revenue falls; may widen inequality." },
  { n: "Education and training", t: "Supply-side", w: "A more skilled workforce raises productivity and AS.", sp: "Slow (years)", c: "Costly; skills must match jobs." },
  { n: "Infrastructure", t: "Supply-side", w: "Better transport and power lower costs and raise capacity.", sp: "Slow (years)", c: "Large cost, delays, environmental damage." },
  { n: "Lower the exchange rate", t: "Monetary", w: "Cheaper exports and dearer imports raise net exports.", sp: "Medium", c: "Imported inflation; depends on elasticity." },
  { n: "Attract foreign investment", t: "Investment", w: "Multinationals bring capital, jobs and technology.", sp: "Medium", c: "Profits sent abroad; competition for local firms." },
  { n: "Free trade agreements", t: "Trade", w: "Larger markets and competition raise exports and efficiency.", sp: "Medium to slow", c: "Some firms and workers lose out; dependence on other economies." },
];
button_table("plBtns", "plOut", PL, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>How it promotes growth</th><th>Speed</th><th>The catch</th></tr><tr><td><b>${p.t}</b></td><td>${p.w}</td><td>${p.sp}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>type of policy</b> is each?", buckets: [{ label: "Fiscal" }, { label: "Monetary" }, { label: "Supply-side" }, { label: "Investment or trade" }], items: [
  { text: "Cut income tax", b: 0 }, { text: "Build new hospitals", b: 0 },
  { text: "Cut interest rates", b: 1 }, { text: "Allow the currency to fall", b: 1 },
  { text: "Fund training for workers", b: 2 }, { text: "Privatise state firms", b: 2 },
  { text: "Tax breaks for firms that invest", b: 3 }, { text: "Sign a free trade agreement", b: 3 },
], done: "Know the five groups of policies." });
Lib.classify($("#cl2"), { prompt: "Which policy fits each <b>situation</b>? Weak demand needs <b>demand-side</b> policy; low capacity needs <b>supply-side</b> policy.", buckets: [{ label: "Demand-side policy fits" }, { label: "Supply-side policy fits" }], items: [
  { text: "Unemployed workers and unused factories after a slump", b: 0 }, { text: "Consumer confidence has collapsed", b: 0 }, { text: "Exports have fallen because of a world slowdown", b: 0 }, { text: "Firms cannot find workers with the right skills", b: 1 },
  { text: "Poor roads and power cuts raise firms' costs", b: 1 }, { text: "Low productivity compared with competitors", b: 1 }, { text: "Barriers stop new firms entering markets", b: 1 }, { text: "High unemployment from low spending", b: 0 },
], done: "Match the policy to the cause of weak growth." });
Lib.match($("#m1"), { prompt: "Match the policy to its main weakness.", pairs: [
  ["Cut interest rates", "May not work if confidence is low"],
  ["Raise government spending", "Bigger deficit and debt"],
  ["Cut income tax", "People may save the money"],
  ["Education and training", "Takes years to have an effect"],
  ["Lower the exchange rate", "Imports cost more: imported inflation"],
  ["Privatisation", "May create private monopolies"],
], done: "Every policy needs an evaluation point." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a cut in the interest rate could raise growth</b>.", items: [
  "The central bank cuts the interest rate",
  "Borrowing becomes cheaper and saving less attractive",
  "Consumption and investment rise",
  "Aggregate demand shifts right",
  "Real GDP rises: economic growth",
], done: "A monetary growth chain." });
''' + calc_js([
    ("A government spends $20bn more and the multiplier is 2.5. What is the rise in real GDP ($bn)?", 50, "2.5 × 20 = <b>$50bn</b>.", None, None),
    ("Real GDP is $500bn. Policy raises growth from 2% to 4%. How much extra output is there after one year ($bn)?", 10, "2% of 500 = $10bn extra.", "Compare 4% and 2% of $500bn.", None),
    ("A tax cut of $12bn is 75% spent in the first round. How much extra spending is there in the first round ($bn)?", 9, "75% of 12 = <b>$9bn</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which policy is most likely to raise growth quickly when there is spare capacity?", ["Education reform", "Cutting interest rates", "Privatisation", "Deregulation"], 1, "Demand-side policy works faster than supply-side."),
    ("Which policy is most likely to lead to growth that can be sustained without inflation?", ["Short-term tax cut", "Investment in education and infrastructure", "Raising the money supply", "Lower interest rates"], 1, "Supply-side policy raises capacity."),
    ("A disadvantage of cutting interest rates to promote growth is:", ["It raises savings income", "It may raise inflation and imports", "It always reduces output", "It reduces investment"], 1, "Higher demand may overheat the economy."),
    ("Attracting multinational firms could promote growth because they:", ["Bring capital, jobs and technology", "Reduce competition", "Raise imports only", "Cut AD"], 0, "More resources of better quality."),
    ("A drawback of free trade agreements may be:", ["Larger markets", "Some firms and workers lose out", "Lower prices", "More choice"], 1, "Competition hurts less efficient firms."),
]) + "\n" + cards_js([("Fiscal policy", "Government spending and taxation used to influence AD."), ("Monetary policy", "Interest rates, money supply and the exchange rate used to influence AD and inflation."), ("Supply-side policy", "Measures to raise productive capacity and shift AS to the right."), ("Foreign direct investment", "Investment in a country by foreign firms, such as multinationals."), ("Free trade", "Trade between countries without barriers such as tariffs."), ("Multiplier effect", "The final impact on AD is greater than the initial change."), ("Spare capacity", "Unused resources, when output is below potential."), ("Sustainable growth", "Growth that can continue without damaging the environment or future prospects.")]) + "labP();\n"
explore = '''
  <h2>Lab 1 · Build a growth policy mix</h2>
  <p>Combine fiscal, monetary and supply-side policy. Notice that demand-side policy raises prices more and supply-side policy raises capacity.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Change in real GDP</small><strong id="pa1"></strong></div><div><small>Change in price level</small><strong id="pa2"></strong></div><div><small>Growth effect</small><strong id="pa3"></strong></div></div><div class="verdict" id="pav"></div></div></div>
    <svg id="labP" viewBox="0 0 760 400" role="img" aria-label="Aggregate demand and supply diagram"></svg>
  </div>

  <h2>Lab 2 · Policy picker</h2>
  <p>Pick a policy to see how it promotes growth, how fast it works and the catch.</p>
  <div class="card"><div class="row" id="plBtns"></div><div id="plOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain two policy measures a government could use to increase its economic growth rate.", "Two different measures, each with a chain: fiscal, monetary, supply-side, investment, trade.",
      "[K|A government could cut interest rates.] [N|Borrowing becomes cheaper and saving less attractive, so consumption and investment could rise, shifting aggregate demand right and increasing real GDP.] [K|It could also spend more on education and training.] [N|Workers would become more productive and aggregate supply could shift right, so productive capacity and output may grow.]"),
    Q(2, "Analyse", 6, "Analyse how a cut in interest rates could increase economic growth.", "Chain: rate cut, borrowing, C and I, AD, real GDP. Add a second link: exchange rate or confidence.",
      "[K|A cut in the interest rate reduces the cost of borrowing and the reward for saving.] [N|Households are likely to spend more and borrow more, so consumption could rise, and firms may find more investment projects profitable.] [N|Lower interest rates may also reduce the exchange rate, making exports cheaper and increasing net exports.] [N|Higher C, I and X − M shift AD to the right, so real GDP rises.] [E|However, if confidence is low households and firms may not respond.]", key=True),
    Q(3, "Discuss", 8, "Discuss whether or not increased international trade can promote economic growth. (Oct/Nov 2020, P21)", "For: larger markets, exports, competition, technology, specialisation. Against: competition hurts firms, dependence, imports, environment.",
      "[K|International trade is the exchange of goods and services between countries.] [N|More trade could promote growth by giving firms access to larger markets, so exports and output could rise, and firms may employ more workers.] [N|Competition from imports may push firms to cut costs and improve quality, and trade can bring in cheaper inputs and new technology, which could raise productivity.] [E|These gains are larger if the country specialises in goods in which it is efficient.] [N|On the other hand, domestic firms may struggle against imports and some workers could lose jobs, and a country that depends on a few exports may be hurt by a world slowdown.] [N|Higher incomes could also raise imports and worsen the current account.] [E|Overall, trade is likely to promote growth in the long run, but it depends on the country's industries, the kind of trade and whether workers can move to growing sectors.]", key=True),
    Q(4, "Discuss", 8, "Discuss whether fiscal policy or supply-side policy is better for promoting economic growth.", "Compare speed, inflation risk, cost and sustainability. Choose a side with 'it depends on…'.",
      "[K|Fiscal policy changes government spending and taxes to affect aggregate demand, whereas supply-side policy aims to raise productive capacity.] [N|Fiscal policy can work fairly quickly: higher spending or lower taxes raise AD, so real GDP and employment could rise, especially when there is spare capacity.] [E|However, it can raise the budget deficit and, near full capacity, cause inflation.] [N|Supply-side policy such as education and infrastructure raises the quantity and quality of resources, so growth can last with lower inflation.] [E|However, it is slow and may be costly, and some measures could widen inequality.] [E|Overall, fiscal policy may be better for a short-term boost during a slump, while supply-side policy is likely to be better for long-term growth. A government may achieve most by combining both.]", key=True),
    Q(5, "Discuss", 8, "Discuss whether or not supply-side policy measures always promote economic growth. (May/June 2022, P23)", "'Always' invites 'not always'. See also 4.4.3.",
      "[K|Supply-side measures aim to raise productive capacity, which should increase growth.] [N|Training could make workers more productive, infrastructure could cut costs and tax incentives could encourage investment.] [E|However, they do not always work.] [N|Training may not match employers' needs, firms and workers may not respond to tax cuts, and projects can be late or costly.] [E|Overall, supply-side policy is likely to promote growth in the long run if well targeted, but it is not guaranteed.]", key=True),
)
tp = tips([
    ("Five policy groups:", "fiscal, monetary, supply-side, investment, trade."),
    ("Match the policy to the cause.", "Weak demand: demand-side. Low capacity: supply-side."),
    ("Short run against long run.", "Demand-side is quick; supply-side is slow but lasting."),
    ("Always give effectiveness.", "Time lags, inflation, deficit, confidence, side effects."),
    ("Combine policies in your conclusion.", "A mix is often the best answer."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("4.5.5 Policies to promote economic growth"), "Policies to Promote Economic Growth", "The range of fiscal, monetary, supply-side, investment and trade policies that could promote growth, and how effective each might be. Syllabus 4.5.5.",
    learn=learn, watch=watch(("Short-run and long-run growth policies", "stP"), ("Demand-side and supply-side policy", "stS")), explore=explore,
    practise=practise(("Which type of policy?", "cl1", "card"), ("Which policy fits the situation?", "cl2", "card"), ("Match the policy to its weakness", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Stimulus after 2008", "Governments cut interest rates close to zero and raised spending to restart growth after the financial crisis. Growth returned, though slowly in many countries, and debts rose.", "Demand-side policy to end a recession, with a cost."),
        rw("Singapore and skills", "Singapore invests heavily in education and training and attracts foreign firms with low business taxes and strong infrastructure.", "Supply-side and investment policy raising capacity."),
        rw("Trade-led growth", "Vietnam has grown quickly by joining trade agreements and attracting foreign manufacturers, with exports a large share of output.", "Trade and FDI policy, with dependence on world demand as a risk."),
        rw("Infrastructure spending in India", "India has increased spending on roads, rail and ports to cut costs and raise capacity, though projects are large and slow.", "A supply-side policy with a long time lag.")),
    exam=ex, tips=tp)
write("eg5", body, js, "Policies to Promote Economic Growth", "ig-growth-policies")
