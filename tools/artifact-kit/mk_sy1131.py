"""Syllabus 11.3.1-11.3.2 Classifying economies by development and by income. Run: python3 tools/artifact-kit/mk_sy1131.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.3.1 to 11.3.2"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Economies are grouped by <b class="kw">level of development</b> (developed, emerging and newly industrialised, developing, least developed), using features such as <b>output per head, health, education, the structure of the economy and trade</b>, and by <b class="kw">level of national income</b>, mainly the World Bank's four groups based on <b>gross national income (GNI) per capita</b>: low, lower-middle, upper-middle and high. Income is easy to measure, so it is used for lending and aid decisions, but it <b>says little about distribution, health, education or sustainability</b>. <b>Development</b> means improvements in people's well-being and choices, whereas <b>growth</b> is a rise in real output, so countries with the same income can sit at very different levels of development.</p></div>

  <h2>1 · Classification by level of development (11.3.1)</h2>
  <div class="tw"><table class="t">
    <tr><th>Group</th><th>Description</th><th>Typical features</th></tr>
    <tr><td><b>Developed (advanced) economies</b></td><td>High incomes, mature industry and services</td><td>High output per head, long life expectancy, high education, large tertiary sector, low birth and death rates, well-developed infrastructure, trade mostly in manufactures and services</td></tr>
    <tr><td><b>Emerging and newly industrialised economies</b></td><td>Fast-growing economies shifting from agriculture to industry</td><td>Rapid growth, rising incomes, growing manufacturing exports, rapid urbanisation, improving but uneven living standards</td></tr>
    <tr><td><b>Developing economies</b></td><td>Lower incomes, still reliant on agriculture or primary products</td><td>Low output per head, low productivity, high dependency ratio, high birth rate, weaker health and education, reliance on primary exports, more informal work</td></tr>
    <tr><td><b>Least developed countries (UN list)</b></td><td>The poorest countries with the most structural weaknesses</td><td>Very low incomes, low human capital, vulnerability to shocks, heavy reliance on aid and a narrow range of exports</td></tr>
  </table></div>
  <ul>
    <li>The <b>UN Human Development Index (HDI)</b> also groups countries as <b>very high, high, medium or low human development</b>, using income, health and education together.</li>
    <li>Economists often compare developed and developing economies using the indicators in 11.3.3 and the characteristics in 11.4: population, income distribution and economic structure.</li>
    <li><b>Development is not the same as growth.</b> Growth is a rise in real GDP. Development adds <b>improvements in life expectancy, health, schooling, poverty reduction, freedom and sustainability</b>. A country can grow without developing (for example when gains go to a few or the environment is damaged).</li>
  </ul>

  <h2>2 · Classification by level of national income (11.3.2)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li>The <b>World Bank</b> ranks countries by <b>GNI per capita</b> (using an Atlas exchange rate to smooth movements) into <b>low, lower-middle, upper-middle and high income</b>. The cut-offs are updated every year for inflation, and in recent years have been roughly <b>$1,200, $4,500 and $14,000</b>. Always say &ldquo;roughly&rdquo; and do not quote exact thresholds in an exam.</li>
    <li>Countries move between groups as incomes rise (or fall). For example, Bangladesh moved from the low-income to the lower-middle-income group in the mid-2010s.</li>
    <li><b>Uses:</b> to compare countries, to set eligibility for concessional loans and aid, to monitor progress and to target policy.</li>
    <li><b>Limitations:</b> GNI per capita is an <b>average</b> that hides inequality; exchange rates and prices differ (so PPP may be better for living standards); some oil-rich countries have high incomes but weaker health and education; groups are wide, so countries in the same group may be very different; the thresholds are somewhat arbitrary.</li>
  </ul>
  <div class="tip"><b class="h">Income group versus development group</b>The two systems overlap but are not the same. A high-income oil exporter may have a lower HDI than an upper-middle income country with strong health and education. Use this contrast as evaluation when asked whether income is a good way to classify countries.</div>
'''

watch = '''
  <h2>1 · The four income groups and a country on the move</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stI"></div>
  <h2>2 · What changes as incomes rise</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Which income group?</h2>
  <p>Set a country's GNI per capita. The group changes at roughly $1,200, $4,500 and $14,000, and the typical features are shown.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div>
    <div class="readout"><div><small>GNI per capita</small><strong id="r1"></strong></div><div><small>Income group</small><strong id="r2"></strong></div><div><small>Typical development</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Income groups on a scale with a marker for the chosen GNI per capita"></svg></div></div></div>

  <h2>Lab 2 · How long to reach the next group?</h2>
  <p>A lower-middle income country has GNI per capita of $3,000. At a steady growth rate, how many years to pass the $4,500 line, and the $14,000 line?</p>
  <div class="card"><div class="grid2"><div><div id="g2"></div>
    <div class="readout"><div><small>Years to $4,500</small><strong id="t1"></strong></div><div><small>Years to $14,000</small><strong id="t2"></strong></div><div><small>GNI after 20 years</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="GNI per capita over time at the chosen growth rate with the two thresholds"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Developed, developing or emerging?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the income groups in order, lowest first</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Bangladesh moves up", "Bangladesh grew steadily for decades, helped by garment exports, remittances and rising productivity, and moved from the World Bank's low-income group to lower-middle income in the mid-2010s. Its HDI also rose, though many workers remain in low-paid, informal jobs.", "a country changing income group and the difference between growth and development.") +
rw("South Korea's rise", "In the 1960s South Korea was among the poorer economies. Rapid investment, education and exporting of manufactured goods moved it to high-income status within a few decades, and it is often described as a newly industrialised economy that became developed.", "emerging economies, structural change and how a country can move between groups.") +
rw("High income, uneven development", "Some oil-exporting countries have very high GNI per capita because of resource revenue, yet in the past have had weaker education, health or political freedoms than countries with similar incomes. Income alone does not show how well the money is used.", "why income classification is limited and why HDI is also used.") +
rw("The least developed countries", "The UN identifies a group of least developed countries, mostly in Sub-Saharan Africa and parts of Asia, that have low incomes, low human capital and high vulnerability to shocks. They receive special support in trade and aid.", "the difference between a developing and a least developed country, and how classifications guide aid.")
)

mc_exam = [
  ("The table shows data for four countries in 2015: GDP, HDI and population. Which country is most likely to be classed as developed? A: GDP $10.9 trillion, HDI 0.727, population 1.37 billion. B: $2.4 trillion, 0.897, 66.8 million. C: $481 billion, 0.527, 182.2 million. D: $19 billion, 0.516, 15.6 million. (Feb/March 2020 · 32 · Q22, reworded)", ["A", "B", "C", "D"], 1, "B has the highest HDI (0.897) and a high GDP per head (GDP divided by a small population). A has the biggest GDP but a lower HDI and a huge population."),
  ("What is likely to happen in a developing country as it becomes more developed? (Feb/March 2024 · 32 · Q30, reworded)", ["A lower percentage of people will go to university", "Average life expectancy will rise", "The rate of population growth will increase", "The tertiary sector will decline in importance"], 1, "Better health care and nutrition raise life expectancy. Population growth usually slows and the tertiary sector grows."),
  ("Which combination of characteristics is usually associated with a low-income country? (May/June 2025 · 34 · Q28, reworded)", ["High death rate and low levels of productivity", "High GDP and low infant mortality", "Low birth rate and a large share of income from primary industries", "Low capital exports and a large tertiary sector"], 0, "Low incomes go with weaker health (higher death rates) and low productivity. The others describe richer or inconsistent economies."),
  ("Which row correctly identifies the characteristics of a low-income economy? Dependence on the primary sector, Gini coefficient and real income per capita. (Oct/Nov 2023 · 33 · Q27, reworded)", ["High, high, high", "High, high, low", "High, low, low", "Low, high, low"], 1, "Low-income economies rely on primary products, have unequal income distribution (high Gini) and low real income per head."),
  ("The table shows the percentage of employment in the primary, secondary and tertiary sectors in four countries. Which is most likely a high-income country? A: 15, 40, 45. B: 30, 40, 30. C: 35, 45, 20. D: 45, 35, 20. (Oct/Nov 2024 · 33 · Q30, reworded)", ["A", "B", "C", "D"], 0, "High-income countries have the largest tertiary sector and smallest primary sector. A has 45% in services and only 15% in the primary sector."),
  ("Which indicator is least likely to be used when comparing the economic development of countries? (Feb/March 2022 · 32 · Q21, reworded)", ["Adult literacy rate", "Life expectancy at birth", "Real GNP per head", "Size of population"], 3, "Literacy, life expectancy and income per head show well-being. Total population does not.")
]

exam = exam_page("classifying economies by development and income",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Comparing developed and developing economies is a regular 12 mark question, and the classification of economies by income and development appears in data response questions on countries such as Bangladesh. Reworded questions are below, with a practice question and six Paper 3 multiple choice questions.",
  [("Essay parts, 12 marks", "3", "May/June 2020 (42) Q6(a); May/June 2022 (42) Q6(a); May/June 2020 (41) Q7(a)"), ("Multiple choice (Paper 3)", "6 shown below", "2020 to 2025")],
  [
  eq("Based on May/June 2020 · 9708/42 · Q6(a) and May/June 2022 · 9708/42 · Q6(a)", "12 marks", "Compare the characteristics of developed and developing countries.",
     ["Develop at least three characteristics, saying how each differs. The mark scheme lists population growth and structure, income distribution, economic structure and employment composition, external trade, urbanisation, GDP per head, education, health care, foreign debt and infrastructure.",
      "Level 4 (9 to 12) needs three or more characteristics explained and analysed, including the link between them (for example low income, low savings and low investment).",
      "Diagrams are credited where they help, for example a Lorenz curve or a population pyramid."],
     "Pick three or four: income per head, population, structure of production and employment, trade, income distribution. For each: developed versus developing, and why.",
     [[("k", "Developed economies have high real income per head, while developing economies have low income per head, which means less is available for saving, investment and health or education spending."), ("n", "Population also differs. Developing countries often have higher birth rates and a young population with a high dependency ratio, so more spending goes on supporting dependants and less on investment. Developed economies usually have low birth and death rates and an ageing population.")],
      [("k", "The structure of production differs. Developing economies often employ a large share of workers in the primary sector, often with low productivity, whereas developed economies have a large tertiary sector."), ("n", "This links to trade: developing countries may export primary products, whose prices are volatile, while developed countries export manufactures and services, which may have higher value added."), ("e", "These groups are broad, so some emerging economies show features of both.")]]),
  eq("Based on May/June 2020 · 9708/41 · Q7(a)", "12 marks", "Developing countries have low levels of productivity and a high dependency ratio. Explain the meaning of these two characteristics and consider whether they are linked.",
     ["Productivity: output per unit of input, such as output per worker; the dependency ratio: the number of dependants (young and old) per person of working age.",
      "Links: low productivity gives low incomes, which restricts spending on education and health, so productivity stays low; a high dependency ratio lowers saving and investment per head, reducing capital and productivity.",
      "Evaluation: the links are not automatic; for example, other factors such as technology and institutions affect productivity, and a young population may become a future benefit (demographic dividend)."],
     "Define both terms. Link 1: productivity to income to human capital. Link 2: dependency to saving and investment. Judge: linked but not the only cause.",
     [[("k", "Productivity is output per worker or per unit of input. The dependency ratio is the number of people not of working age, such as children and the elderly, relative to those of working age."), ("n", "The two may be linked because a high dependency ratio means that a large share of income is spent on supporting dependants. This could reduce saving and investment, so each worker has less capital and productivity may be lower. Low productivity then means low incomes and less spending on schools and health, which can keep productivity low.")],
      [("e", "However, productivity also depends on technology, infrastructure and institutions, so the link may not be the main cause. A young population could also raise future output if education improves.")]]),
  eq("Practice question · modelled on the 8 mark style (no past paper)", "8 marks", "Explain two limitations of using GNI per capita to classify economies.",
     ["An average that hides income inequality, so many people may be much poorer than the figure suggests.",
      "Exchange rates and price levels differ, so GNI at market exchange rates may not show real living standards; it ignores non-income factors (health, education, environment) and unrecorded activity.",
      "Each limitation developed with a reason and an example."],
     "Limitation 1 with a chain. Limitation 2 with a chain.",
     [[("k", "GNI per capita is an average, found by dividing total income by population."), ("n", "It does not show how income is shared. In a country with a high Gini coefficient a small group may take most of the income, so the typical citizen could be much worse off than the average suggests, and the country could be placed in a higher group than most people's experience.")],
      [("n", "It also ignores non-income aspects of development. Two countries with the same GNI per head may have very different life expectancy, schooling and environmental quality, so the classification may give a misleading picture of development. Prices also differ, so converting at the market exchange rate may understate real living standards in low-price economies.")]])
  ],
  )

tips = tips_html(
  [("Compare, do not list.", "For each characteristic say how developed and developing economies differ and why."),
   ("Use three or four characteristics.", "Income per head, population, structure of production, trade, income distribution."),
   ("Say 'roughly' for thresholds.", "World Bank cut-offs change every year. The idea matters, not the number."),
   ("Growth is not development.", "Growth is higher real GDP. Development is better lives: health, education, poverty, freedom."),
   ("Link the features.", "Low income leads to low saving, low investment, low productivity, so low income again."),
   ("Evaluate classifications.", "Averages hide inequality; groups are broad; some high-income countries have weaker development."),
   ("Use the HDI groups too.", "Very high, high, medium and low human development.")],
  [("Classify", "Economies may be classified by income, using GNI per capita, or by development, using indicators such as the HDI."),
   ("Compare", "Developing economies tend to have lower productivity, a higher dependency ratio and a larger primary sector than developed economies."),
   ("Link", "Low incomes may restrict saving and investment, which could keep productivity and incomes low."),
   ("Limit", "GNI per capita is an average, so it may hide inequality and does not measure well-being directly."),
   ("Growth", "A country could experience growth without development if the benefits are not widely shared.")],
  [CW["define"], CW["explain"], CW["consider"], CW["evaluate"]]) + FC

js = '''
/* ---------- Income groups ---------- */
const LX = (g) => 90 + (Math.log10(g) - Math.log10(300)) / (Math.log10(60000) - Math.log10(300)) * 620, TH = [1200, 4500, 14000], GN = ["Low income", "Lower-middle", "Upper-middle", "High income"], GC = ["f2", "f1", "f1", "f3"];
function incDraw(s) {
  let o = SV.line(90, 210, 710, 210) + SV.text(710, 254, "GNI per capita ($, log scale)", "sm", { "text-anchor": "end" });
  const edges = [300, ...TH, 60000]; [300, 1200, 4500, 14000, 60000].forEach((g) => (o += SV.line(LX(g), 205, LX(g), 215) + SV.text(LX(g), 232, "$" + g.toLocaleString("en-US"), "sm", { "text-anchor": "middle" })));
  for (let i = 0; i < 4; i++) { const k = Math.max(0, Math.min(1, s.z - i)); if (k > 0) o += SV.rect(LX(edges[i]), 150, LX(edges[i + 1]) - LX(edges[i]), 55, GC[i], op(0.25 + 0.5 * k * (i % 2 ? 0.7 : 1))) + tag((LX(edges[i]) + LX(edges[i + 1])) / 2, 182, GN[i], "t1", k, "middle"); }
  if (s.m > 0) { const g = s.p, x = LX(g); o += SV.circle(x, 140, 8, "dot4", op(s.m)) + SV.line(x, 148, x, 150, "c4", op(s.m)) + tag(x, 120, "$" + Lib.fmtN(g, 0), "t4", s.m, "middle") + tag(x, 104, "a country on the move", "t4", s.m, "middle"); }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 260" role="img" aria-label="Income groups on a logarithmic scale of GNI per capita">${incDraw({ z: 4, p: 3000, m: 0 })}</svg>`;
Lib.stepper($("#stI"), { w: 760, h: 260, label: "The four World Bank income groups on a log scale and a country moving between groups", base: { z: 0, p: 3000, m: 0 }, draw: incDraw, tween: 1100, dwell: 5600, steps: [
  { cap: "<b>Low income:</b> GNI per capita below about $1,200. Many people rely on subsistence farming and basic services are limited.", s: { z: 1 } },
  { cap: "<b>Lower-middle income:</b> roughly $1,200 to $4,500. Manufacturing and urban jobs start to grow, but much work is informal.", s: { z: 2 } },
  { cap: "<b>Upper-middle income:</b> roughly $4,500 to $14,000. Industry and services are larger, and schooling and health are better.", s: { z: 3 } },
  { cap: "<b>High income:</b> above roughly $14,000. A large services sector, high productivity and wide access to health and education.", s: { z: 4 } },
  { cap: "<b>A lower-middle income country</b> has GNI per capita of $3,000.", s: { z: 4, p: 3000, m: 1 } },
  { cap: "<b>Moving up.</b> At 4% growth a year it passes the $4,500 line in about 10 years and moves from the lower-middle to the upper-middle group.", s: { z: 4, p: 4900, m: 1 } },
] });

/* ---------- What changes ---------- */
const CHG = [["Life expectancy (years)", [62, 68, 74, 80], 90, "f1"], ["Workers in agriculture (%)", [60, 40, 20, 3], 100, "f2"], ["Births per 1,000 people", [35, 25, 15, 11], 50, "f3"]];
function chgDraw(s) {
  let o = SV.line(70, 250, 730, 250) + SV.line(70, 250, 70, 30);
  CHG.forEach((c, k) => { const p = Math.max(0, Math.min(1, s.i - k)); if (p <= 0) return; const [name, vals, mx, cls] = c; o += SV.text(70 + k * 220 + 70, 24 - 0, name, "lbl bd", { "text-anchor": "middle", ...op(p) }); vals.forEach((v, i) => { const h = v / mx * 180 * p, x = 80 + k * 220 + i * 46; o += SV.rect(x, 250 - h, 34, h, cls, op(0.35 + 0.18 * i)) + SV.text(x + 17, 244 - h, v, "sm", { "text-anchor": "middle", ...op(p) }) + SV.text(x + 17, 266, ["L", "LM", "UM", "H"][i], "sm", { "text-anchor": "middle" }); }); });
  return o + SV.text(730, 290, "L low, LM lower-middle, UM upper-middle, H high income (typical values, for illustration)", "sm", { "text-anchor": "end" });
}
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Typical life expectancy, share of workers in agriculture and birth rate across the four income groups", base: { i: 0 }, draw: chgDraw, tween: 1100, dwell: 5600, steps: [
  { cap: "<b>Life expectancy</b> rises with income: better health care, nutrition and sanitation. This is a development gain beyond income itself.", s: { i: 1 } },
  { cap: "<b>The share of workers in agriculture</b> falls sharply: labour moves from low-productivity farming to industry and services (structural change).", s: { i: 2 } },
  { cap: "<b>The birth rate</b> falls as incomes, education and health improve, so the dependency ratio falls and more can be saved and invested.", s: { i: 3 } },
] });

/* ---------- Lab 1 ---------- */
function labI() {
  if (!$("#gn")) return;
  const g = Math.round(Math.pow(10, +$("#gn").value)), k = g < 1200 ? 0 : g < 4500 ? 1 : g < 14000 ? 2 : 3, feat = ["Mostly primary sector; low productivity; high birth rate", "Growing industry and cities; large informal sector", "Larger industry and services; better health and schooling", "Large tertiary sector; high productivity; ageing population"];
  $("#r1").textContent = "$" + g.toLocaleString("en-US"); $("#r2").textContent = GN[k]; $("#r3").textContent = ["Early", "Developing", "Emerging", "Developed"][k];
  $("#rv").textContent = `${GN[k]} (roughly): ${feat[k]}. This is only a typical pattern: income per head is an average, and countries with the same income can differ in health, education and inequality.`;
  $("#labA").innerHTML = (() => { const X = (v) => 30 + (Math.log10(v) - Math.log10(300)) / (Math.log10(60000) - Math.log10(300)) * 360; let o = SV.line(30, 160, 390, 160) + SV.text(390, 196, "GNI per capita ($, log scale)", "sm", { "text-anchor": "end" }); const e = [300, 1200, 4500, 14000, 60000]; for (let i = 0; i < 4; i++) o += SV.rect(X(e[i]), 110, X(e[i + 1]) - X(e[i]), 50, GC[i], op(i === k ? 0.85 : 0.25)) + SV.text((X(e[i]) + X(e[i + 1])) / 2, 140, ["Low", "Lower-mid", "Upper-mid", "High"][i], "sm", { "text-anchor": "middle" }); o += SV.circle(X(g), 98, 8, "dot4") + tag(X(g), 80, "$" + g.toLocaleString("en-US"), "t4", 1, "middle"); return o; })();
}
Lib.slider($("#g1"), { id: "gn", label: "GNI per capita (log scale) ", min: 2.5, max: 4.7, step: 0.02, value: 3.5, fmt: (v) => "$" + Math.round(Math.pow(10, v)).toLocaleString("en-US"), onInput: labI });
labI();

/* ---------- Lab 2 ---------- */
function labG() {
  if (!$("#gr")) return;
  const r = +$("#gr").value / 10 / 100, yrs = (t) => Math.log(t / 3000) / Math.log(1 + r), y45 = yrs(4500), y14 = yrs(14000), g20 = 3000 * Math.pow(1 + r, 20);
  $("#t1").textContent = Lib.fmtN(y45, 1); $("#t2").textContent = Lib.fmtN(y14, 1); $("#t3").textContent = "$" + Math.round(g20).toLocaleString("en-US");
  $("#tv").textContent = `At ${Lib.fmtN(r * 100, 1)}% a year, GNI per capita passes $4,500 after about ${Lib.fmtN(y45, 0)} years and $14,000 after about ${Lib.fmtN(y14, 0)} years. Lasting growth of a few percent a year takes decades to change a country's income group.`;
  const X = (t) => 40 + t * 7, Y = (v) => 270 - (v / 20000) * 240; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 292, "Years", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "GNI per capita ($)", "sm");
  [4500, 14000].forEach((th) => (o += SV.line(40, Y(th), 400, Y(th), "c4 dash", op(0.6)) + SV.text(44, Y(th) - 4, "$" + th.toLocaleString("en-US"), "sm")));
  const pts = []; for (let t = 0; t <= 50; t += 1) pts.push([X(t), Math.max(20, Y(3000 * Math.pow(1 + r, t)))]);
  $("#labB").innerHTML = o + SV.path(Lib.ptsPath(pts), "c1");
}
Lib.slider($("#g2"), { id: "gr", label: "Growth rate of GNI per capita, % a year × 10 ", min: 10, max: 80, step: 5, value: 40, fmt: (v) => (v / 10).toFixed(1) + "%", onInput: labG });
labG();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which type of economy does the description fit best?", ["Developed", "Emerging", "Developing"],
  [("A very large tertiary sector and low birth and death rates", 0), ("Fast growth, rapid urbanisation and rising manufacturing exports", 1), ("Most workers in low-productivity farming and a high dependency ratio", 2), ("An ageing population and high productivity", 0), ("Moving workers from agriculture into factories at speed", 1), ("Heavy reliance on exporting a few primary products", 2), ("Wide access to health care and long life expectancy", 0), ("Rising incomes but still large informal sector", 1)],
  "Developed: high income and services. Emerging: fast structural change. Developing: low income and primary reliance.") + MATCH([
  ["GNI per capita", "A country's total income from residents divided by its population"],
  ["Low-income country", "Below about $1,200 GNI per capita in the World Bank classification"],
  ["Emerging economy", "A fast-growing economy shifting from agriculture to industry"],
  ["Economic development", "Improvements in living standards, health, education and choice"],
  ["Dependency ratio", "Dependants (young and old) per person of working age"],
  ["HDI", "A composite of income, health and education"]]) + ORDER(
  "Put the World Bank income groups in order, lowest income first.",
  ["Low income", "Lower-middle income", "Upper-middle income", "High income"],
  "Thresholds are roughly $1,200, $4,500 and $14,000 of GNI per capita.") + CALC([
  {"q": "A country has GNI of $60bn and a population of 15 million. Calculate GNI per capita ($).", "a": 4000, "unit": "$", "tol": 0.5, "hint": "60bn ÷ 15m.", "sol": "60,000m ÷ 15m = <b>$4,000</b>: lower-middle income."},
  {"q": "GNI per capita rises from $3,000 to $3,150 in a year. Calculate the percentage growth (%).", "a": 5, "unit": "%", "tol": 0.05, "hint": "150 ÷ 3000.", "sol": "<b>5%</b>."},
  {"q": "A country has 4 dependants for every 10 people of working age. Calculate the dependency ratio as a percentage (%).", "a": 40, "unit": "%", "tol": 0.5, "hint": "4 ÷ 10.", "sol": "<b>40%</b>."},
  {"q": "Using a growth rate of 5% a year, by about how many years would $3,000 double? (Rule of 70, years)", "a": 14, "unit": "years", "tol": 0.5, "hint": "70 ÷ 5.", "sol": "70 ÷ 5 = <b>14 years</b>."}]) + MCQ([
  ("Which is used to classify countries into low, lower-middle, upper-middle and high income?", ["GNI per capita", "The HDI only", "Population", "The Gini coefficient"], 0, "The World Bank uses GNI per capita."),
  ("A country has grown fast but most people have not seen better health or schooling. This shows:", ["Growth without development", "Development without growth", "Neither", "Both"], 0, "Output rose but well-being did not improve widely."),
  ("A typical developing economy has:", ["A large primary sector", "A very small dependency ratio", "The highest life expectancy", "A very large tertiary sector"], 0, "Many workers are in farming and primary activities."),
  ("An advantage of classifying by GNI per capita is that:", ["It is easy to measure and compare", "It measures well-being fully", "It shows income distribution", "It includes health and education"], 0, "It is a simple, widely available statistic."),
  ("Which statement is true of income groups?", ["Countries can move between them as incomes change", "The thresholds never change", "They show equality", "They include education"], 0, "Bangladesh moved up from low to lower-middle income, for example.")
], "qz1") + CARDS([
  ("Developed", "High income, large services sector, high life expectancy."),
  ("Emerging", "Fast growth and structural change."),
  ("Developing", "Lower income, primary reliance, high dependency."),
  ("LDC", "Least developed country on the UN list."),
  ("GNI per capita", "Income of residents ÷ population."),
  ("Income groups", "Low, lower-middle, upper-middle, high."),
  ("Growth vs development", "Output rises vs lives improve."),
  ("Limit of income groups", "An average that hides inequality and well-being.")]) + MCQ(mc_exam)

build("sy1131", "classifying-economies", "Classifying Economies by Development and Income", EY,
  "11.3.1 to 11.3.2: how economies are grouped by level of development and by national income, why the groups matter and where they mislead. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
