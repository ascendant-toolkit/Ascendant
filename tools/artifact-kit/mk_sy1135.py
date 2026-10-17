"""Syllabus 11.3.3 composite indicators: HDI, MEW, MPI and the Kuznets curve. Run: python3 tools/artifact-kit/mk_sy1135.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.3.3 (composite indicators and the Kuznets curve)"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Composite indicators combine several measures into one number. The <b class="kw">Human Development Index (HDI)</b> combines <b>health (life expectancy), education (years of schooling) and income (GNI per capita at PPP)</b>; the <b class="kw">Measure of Economic Welfare (MEW)</b> adjusts GDP by adding <b>leisure and unpaid work</b> and deducting <b>environmental damage and regrettable spending</b>; and the <b class="kw">Multidimensional Poverty Index (MPI)</b> measures <b>deprivation in health, education and living standards</b> as the share of poor people times the intensity of their poverty. The <b class="kw">Kuznets curve</b> suggests that <b>inequality first rises and then falls</b> as income per head grows, an inverted U. All of them give a fuller picture than income alone but involve judgements about what to include and how to weight it.</p></div>

  <h2>1 · The Human Development Index (HDI)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li>Published by the <b>UN Development Programme</b>. Three dimensions, each turned into an index between 0 and 1:
      <b>health</b> (life expectancy at birth), <b>education</b> (mean years of schooling of adults and expected years of schooling of children) and <b>standard of living</b> (GNI per capita at PPP, with a logarithm so each extra dollar counts less at high incomes).</li>
    <li>The HDI is the <b>geometric mean</b> of the three indices, so a country cannot make up for a very low score in one dimension with a high score in another. It ranges from <b>0 to 1</b>.</li>
    <li>Countries are grouped as <b>very high (about 0.8 and above), high, medium and low (below about 0.55) human development</b>.</li>
    <li><b>Why it is better than income alone:</b> two countries with the same income can have very different health and education, and the HDI shows this. Countries with a high GDP rank but a lower HDI rank show that growth has not translated into well-being.</li>
    <li><b>Limits:</b> equal weights are a judgement; it ignores inequality (the Inequality-adjusted HDI corrects this), the environment, political freedom and personal safety; the data on schooling and life expectancy may be inaccurate in some countries; the three components are correlated so it may add little to income at the top; it changes slowly.</li>
  </ul>

  <h2>2 · The Measure of Economic Welfare (MEW)</h2>
  <ul>
    <li>Developed by Nordhaus and Tobin. Start with GDP (or consumption) and <b>adjust</b>:
      <b>add</b> the value of <b>leisure</b> and <b>unpaid household work</b>; <b>deduct</b> the cost of <b>environmental damage</b> and <b>"regrettable" spending</b> such as defence, commuting and crime prevention that does not raise welfare.</li>
    <li><b>Merits:</b> it measures welfare, not just output, and shows that GDP can rise while welfare falls (for example with pollution).</li>
    <li><b>Limits:</b> valuing leisure, unpaid work and pollution involves subjective estimates; data are hard to collect, especially in low-income countries; it is not published regularly like GDP and HDI, so it is rarely used for comparison.</li>
  </ul>

  <h2>3 · The Multidimensional Poverty Index (MPI)</h2>
  <ul>
    <li>Measures <b>poverty directly</b>, using ten indicators grouped into three equal dimensions: <b>health</b> (nutrition, child mortality), <b>education</b> (years of schooling, school attendance) and <b>living standards</b> (cooking fuel, sanitation, drinking water, electricity, housing, assets).</li>
    <li>A person is <b>multidimensionally poor</b> if deprived in at least about <b>one-third of the weighted indicators</b>.</li>
    <li><b>MPI = H × A</b>, where <b>H</b> is the headcount ratio (share of people who are poor) and <b>A</b> is the average intensity of deprivation among the poor (share of weighted indicators in which they are deprived).</li>
    <li><b>Merits:</b> shows <i>how</i> people are poor (which deprivations), can be broken down by region and group, and does not depend on income measurement. <b>Limits:</b> needs household survey data, the cut-offs and weights are a judgement, and it does not capture inequality within households.</li>
  </ul>

  <h2>4 · The Kuznets curve</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li>Simon Kuznets suggested that <b>income inequality rises in the early stages of growth, reaches a peak and then falls</b>, tracing an <b>inverted U</b> when inequality (for example the Gini coefficient) is plotted against income per head.</li>
    <li><b>Rising stage:</b> workers move from low-income farming to higher-paid industry in cities, and the owners of capital and skilled workers gain first, so inequality widens.</li>
    <li><b>Falling stage:</b> as more people get education and skills, the population ages and urbanises, and governments introduce <b>progressive taxes and welfare spending</b>, so inequality falls.</li>
    <li><b>Evaluation:</b> evidence is mixed; some countries have seen inequality rise again in rich economies (technology, globalisation); policy choices, not just income, shape the path; it describes a tendency, not a law, and does not say how long the rise lasts. It also suggests that early inequality is a price of growth, which governments may not accept.</li>
  </ul>
  <div class="tip"><b class="h">Using the measures in an answer</b>For "are HDI and MEW better than GNI?" say what each adds (health and education for HDI; welfare adjustments for MEW), say what each leaves out, and conclude that income is a useful, easily measured starting point but that a fuller picture needs both income and non-income indicators.</div>
'''

watch = '''
  <h2>1 · Building the HDI</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stH"></div>
  <h2>2 · The Kuznets curve</h2>
  <div id="stK"></div>
'''

explore = '''
  <h2>Lab 1 · Calculate an HDI</h2>
  <p>Set life expectancy, years of schooling and GNI per capita (PPP). The HDI is the geometric mean of the three indices. Notice that a weak dimension drags the HDI down more than an average would.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Health / Education / Income</small><strong id="r1"></strong></div><div><small>HDI</small><strong id="r2"></strong></div><div><small>Group</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of the health, education and income indices and the HDI"></svg></div></div></div>

  <h2>Lab 2 · The Multidimensional Poverty Index</h2>
  <p>MPI = H × A. Set the share of people who are poor and the average intensity of their deprivation.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>H (headcount)</small><strong id="t1"></strong></div><div><small>A (intensity)</small><strong id="t2"></strong></div><div><small>MPI</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bar for the headcount ratio, the intensity and the resulting MPI"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which measure does the description fit?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the Kuznets curve stages in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("GDP rank versus HDI rank", "The UN's HDI tables often show countries whose HDI rank is well above or below their GDP per head rank. Some middle-income countries with strong public health and education rank higher on the HDI than richer countries with weaker services, which is the usual evidence that income is an incomplete measure.", "why alternative measures are used, and how the HDI and income can tell different stories.") +
rw("The MPI and the poverty picture", "Many people who are close to the income poverty line are also deprived in sanitation, cooking fuel or schooling. The MPI shows which of these deprivations is the largest in each region, helping governments target aid and public spending.", "how the MPI shows the nature of poverty, not just its extent.") +
rw("Fast growth and pollution", "A country can raise GDP rapidly with heavy industry and coal power while air quality falls and health costs rise. A welfare measure like the MEW deducts the environmental damage, so welfare may rise by much less than GDP, or fall.", "why GDP can overstate welfare and how the MEW adjusts for this.") +
rw("Inequality over time", "Studies of some East Asian economies suggest inequality rose during rapid industrialisation. Evidence for rich economies since the 1980s shows inequality rising again in some countries, which does not fit a simple inverted U.", "evaluating the Kuznets curve.")
)

mc_exam = [
  ("What is not included in the Human Development Index? (Oct/Nov 2020 · 31 · Q18, reworded)", ["Infant mortality rates", "Gross national income per capita", "Life expectancy at birth", "Mean years of schooling"], 0, "The HDI has life expectancy, schooling and income. Infant mortality is a health indicator but is not one of the three components."),
  ("Which measurement is not included in the calculation of the HDI? (May/June 2025 · 31 · Q26, reworded)", ["Average years of schooling", "GNI per capita", "Infant mortality rate", "Life expectancy at birth"], 2, "The three dimensions use schooling, GNI per capita and life expectancy."),
  ("The HDI is often argued to be a better indicator of development than income per capita because it adjusts for: (Oct/Nov 2024 · 31 · Q27, reworded)", ["Average hours worked", "Environmental pollution", "Inequality in income distribution", "Life expectancy at birth"], 3, "The HDI adds health (life expectancy) and education to income. The standard HDI does not adjust for pollution or inequality."),
  ("The MEW is regarded as a better measure of economic welfare than GDP per head. What is additionally included in the calculation of MEW? (May/June 2021 · 31 · Q20, reworded)", ["The cost of paid work", "The cost of producing armaments", "The estimated cost of damage to the environment", "The negative effect of the shadow economy"], 2, "The MEW deducts environmental damage, and adds leisure and unpaid work."),
  ("Which adjustments are made to GDP to calculate the MEW? (Oct/Nov 2023 · 31 · Q27, reworded)", ["Value of leisure only", "Value of unpaid work only", "Leisure and unpaid work only", "Leisure, unpaid work and the cost of environmental damage"], 3, "All three adjustments are made: add leisure and unpaid work, deduct environmental costs."),
  ("What is not included as a weighted indicator of poverty in the Multidimensional Poverty Index? (Feb/March 2025 · 32 · Q28, reworded)", ["Cooking fuel", "Electricity", "Medication", "Water"], 2, "The MPI uses nutrition, child mortality, schooling, attendance, cooking fuel, sanitation, drinking water, electricity, housing and assets."),
  ("What is shown by the Kuznets curve? (May/June 2022 · 31 · Q20, reworded)", ["A rise then fall in a trade deficit after a devaluation", "A rise then fall in the growth rate as GDP rises", "A rise then fall in inequality as income per head rises", "A rise then fall in tax revenue as the tax rate rises"], 2, "The Kuznets curve is an inverted U relating inequality to income per head."),
  ("The turning point on the Kuznets curve has been estimated at about $10,500 of GDP per head. For a country with GDP per head of $8,000, what is most likely? (Oct/Nov 2023 · 31 · Q30, reworded)", ["A fall in GDP per head would have no effect on inequality", "A fall in GDP per head would increase inequality", "A rise in GDP per head would have no effect on inequality", "A rise in GDP per head would increase inequality"], 3, "The country is on the rising part of the curve, below the turning point, so further growth would be expected to raise inequality."),
  ("During a period a country with a constant population expands its output per head but also suffers more river and air pollution. In the absence of other changes, which measure would show a fall in living standards? (May/June 2024 · 32 · Q30, reworded)", ["GDP per head", "GNP per head", "HDI", "MEW"], 3, "Only the MEW deducts environmental damage."),
  ("Why do economists distinguish between economic growth and economic development? (Oct/Nov 2021 · 31 · Q29, reworded)", ["A country's development depends on its output level, not its growth rate", "Allocation of resources, not their level, decides well-being", "Concern about quality of life rather than quantity of output", "Investment, not consumption, drives development"], 2, "Development is about improvements in quality of life as well as output.")
]

exam = exam_page("composite indicators: the HDI, MEW, MPI and the Kuznets curve",
  "We searched the A Level Economics papers in the folder (2020 to 2025). The HDI appears in data response parts and in 25 mark essays on alternatives to GNI, and the Kuznets curve and the MPI appear in Paper 3 every year. Reworded past questions are below, with ten Paper 3 multiple choice questions.",
  [("Data response parts", "3", "May/June 2020 (41) Q1(d); May/June 2025 (44) Q1(a) and (d)"), ("Essay parts, 13 marks", "1", "Oct/Nov 2020 (42) Q7(b)"), ("Essay, 25 marks", "1", "May/June 2021 (42) Q5"), ("Multiple choice (Paper 3)", "10 shown below", "2020 to 2025")],
  [
  eq("Based on May/June 2025 · 9708/44 · Q1(a)", "3 marks", "Identify what is included in the HDI.",
     ["Health or life expectancy (1).", "Education or years of schooling (1).", "Income or GNI per capita (1)."],
     "Three dimensions: health, education, income.",
     [[("k", "The HDI includes life expectancy at birth (health), years of schooling (education) and gross national income per head (income).")]]),
  eq("Based on May/June 2020 · 9708/41 · Q1(d)", "6 marks", "A table shows the rank of selected countries by HDI and by GDP. Some countries have a high GDP rank but a lower HDI rank, and some with low GDP have a similar HDI. Discuss whether the information supports the idea that GDP is a good measure of well-being.",
     ["The HDI is said to be a measure of well-being. Countries are ranked by HDI and GDP; examples are given where the ranks differ.",
      "Some countries with low HDI also have low GDP, but some with a higher HDI do not have the highest GDP.",
      "Note that the GDP shown is total, not per capita and not adjusted for PPP, so there is no real evidence that GDP is a comparable, accurate measure of well-being."],
     "Quote two examples from the table. Say what it shows. Point out the GDP data are not per head or PPP. Conclude.",
     [[("k", "The HDI is designed to measure well-being using health, education and income. If GDP were a good measure, countries with higher GDP should have a higher HDI."), ("n", "The table shows this is only partly true. Some countries with large total GDP have a lower HDI rank than countries with smaller GDP, so output alone does not give a good picture of well-being. Some countries with low GDP have a low HDI, which suggests a link at the bottom.")],
      [("e", "However, the GDP in the table is a total, not per head and not at PPP, so it is not a fair comparison. The evidence is therefore weak, and it may only show that GDP is an incomplete measure.")]]),
  eq("Based on May/June 2021 · 9708/42 · Q5", "25 marks", "Discuss the extent to which the HDI and the MEW provide better measures of living standards than GNI.",
     ["Explain the alternative measures HDI and MEW. Define GNI and explain real per capita GNI and its link to the standard of living.",
      "Explain the relevance and limitations of each, and the problems of measuring each in developing countries (statistical problems, cost and accuracy of collection).",
      "Level 4 (18 to 25) describes all three measures, discusses the limitations of GNI and one other measure, and reaches a conclusion."],
     "GNI per head: use and limits. HDI: what it adds and lacks. MEW: what it adds and lacks. Developing-country data problems. Conclusion.",
     [[("k", "Real GNI per capita is income from residents, adjusted for inflation and divided by population, and is often used as a proxy for living standards. It is easy to calculate, but ignores income distribution, unpaid work, leisure and environmental damage, and is less accurate in economies with large informal sectors.")],
      [("n", "The HDI adds life expectancy and education to income at PPP, so it shows health and knowledge that GNI misses. The MEW adjusts GDP by adding leisure and unpaid work and deducting environmental damage and regrettable spending, so it focuses on welfare rather than output."), ("e", "However, the HDI uses equal weights and ignores inequality and the environment. The MEW involves subjective valuation and is rarely published. In developing countries, the cost and accuracy of data collection affect all three measures.")],
      [("e", "Overall, the HDI and MEW may be better guides to well-being than GNI, but GNI remains a useful, easily compared starting point, so the best approach may be to use several measures together.")]]),
  eq("Based on Oct/Nov 2020 · 9708/42 · Q7(b)", "13 marks", "Discuss why alternatives to GDP are increasingly used to measure the standard of living.",
     ["Limitations of GDP: inflation, population, PPP, non-marketed goods, crime, negative externalities, the nature of the goods produced, distribution and the informal economy.",
      "Alternatives: HDI, MEW, MPI and others, with how each deals with the limitations.",
      "Evaluation: alternatives have their own problems of weighting and data, so GDP is still widely used."],
     "Limits of GDP. Two alternatives. How they fix the limits. Their own problems.",
     [[("k", "GDP counts the market value of output but not distribution, unpaid work, leisure or the environment, and it includes output that may reduce welfare, such as spending on pollution clean-up."), ("n", "Alternatives such as the HDI add health and education, so they show outcomes that matter to people, and the MEW adjusts for leisure, unpaid work and environmental damage. The MPI measures deprivation directly. These measures could give a better indication of well-being, which is why they are increasingly used by international organisations.")],
      [("e", "However, they require judgements about weights, and data on health and education may be poor in some countries, so GDP remains popular because it is simple and widely available.")]])
  ],
  )

tips = tips_html(
  [("Know the three HDI parts.", "Health (life expectancy), education (years of schooling), income (GNI per capita at PPP)."),
   ("Know what MEW adds and deducts.", "Add leisure and unpaid work. Deduct environmental damage and regrettable spending."),
   ("MPI is H times A.", "Headcount of poor people times the intensity of their deprivation."),
   ("Draw the inverted U.", "Gini coefficient up the axis, income per head along it, a peak at the turning point."),
   ("Evaluate with limits.", "Weights, data quality, inequality, environment and what is left out."),
   ("Compare with GNI.", "Income is easy to measure but incomplete. Composite measures add well-being but add judgement."),
   ("Say 'could' or 'may'.", "The Kuznets curve describes a tendency, not a law.")],
  [("HDI", "The HDI combines life expectancy, years of schooling and income per head, so it could show a fuller picture of development than income alone."),
   ("MEW", "The MEW adjusts GDP by adding leisure and unpaid work and deducting environmental damage and regrettable spending."),
   ("MPI", "The MPI measures deprivation across health, education and living standards, multiplying the share of poor people by the intensity of their poverty."),
   ("Kuznets", "The Kuznets curve suggests inequality may rise at first and then fall as income per head grows."),
   ("Limits", "Each composite measure involves judgements about what to include and how much weight to give each part.")],
  [CW["define"], CW["explain"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- HDI ---------- */
const HV = [["Health index", 0.8, "f1", "Life expectancy 72 years"], ["Education index", 0.65, "f2", "Years of schooling"], ["Income index", 0.7, "f1", "GNI per head at PPP"]], HY = (v) => 290 - v * 230;
function hdiDraw(s) {
  let o = axes(70, 290, 730, 30, "", "Index (0 to 1)"); [0, 0.5, 1].forEach((v) => (o += SV.text(64, HY(v) + 4, v, "sm", { "text-anchor": "end" })));
  HV.forEach(([l, v, c, sub], i) => { const k = [s.a, s.b, s.c][i]; if (k > 0) o += SV.rect(120 + i * 140, HY(v * k), 90, 290 - HY(v * k), c, op(0.7)) + tag(165 + i * 140, HY(v * k) - 8, Lib.fmtN(v * k, 2), "t1", k, "middle") + tag(165 + i * 140, 312, l, "t1", k, "middle") + tag(165 + i * 140, 328, sub, "sm", k, "middle"); });
  if (s.d > 0) { const h = Math.cbrt(0.8 * 0.65 * 0.7); o += SV.rect(560, HY(h * s.d), 110, 290 - HY(h * s.d), "f3", op(0.8)) + tag(615, HY(h * s.d) - 8, "HDI " + Lib.fmtN(h * s.d, 2), "t4", s.d, "middle") + tag(615, 312, "Geometric mean", "t4", s.d, "middle") + tag(615, 328, "(cube root of the product)", "sm", s.d, "middle"); }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Health, education and income indices of 0.80, 0.65 and 0.70 combined into an HDI of about 0.71">${hdiDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stH"), { w: 760, h: 345, label: "Building the HDI from the health, education and income indices", base: { a: 0, b: 0, c: 0, d: 0 }, draw: hdiDraw, tween: 1100, dwell: 5600, steps: [
  { cap: "<b>Health.</b> Life expectancy of 72 years sits between a minimum of 20 and a maximum of 85: index (72 − 20) ÷ 65 = 0.80.", s: { a: 1 } },
  { cap: "<b>Education.</b> Mean and expected years of schooling give an education index of 0.65.", s: { a: 1, b: 1 } },
  { cap: "<b>Income.</b> GNI per head at PPP, on a logarithmic scale between a floor and a ceiling, gives an income index of 0.70.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>The HDI</b> is the geometric mean: (0.80 × 0.65 × 0.70)^(1/3) = 0.71. It is lower than the simple average of 0.72, because a weaker dimension counts for more.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Kuznets ---------- */
const KX = (x) => 80 + x * 6.4, KY = (g) => 300 - (g - 0.28) * 1150, kg = (x) => 0.30 + 0.17 * Math.exp(-Math.pow((x - 40) / 28, 2));
function kuzDraw(s) {
  let o = axes(70, 290, 730, 30, "Income per head", "Inequality (Gini coefficient)"); [0.3, 0.4, 0.5].forEach((v) => (o += SV.text(64, KY(v) + 4, v.toFixed(1), "sm", { "text-anchor": "end" })));
  const pts = []; for (let x = 0; x <= Math.min(100, s.p); x += 1) pts.push([KX(x), KY(kg(x))]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c1");
  if (s.p > 0) o += SV.circle(KX(Math.min(100, s.p)), KY(kg(Math.min(100, s.p))), 7, "dot4");
  if (s.l > 0) o += tag(KX(9), 314, "Farming: low inequality", "t1", s.l, "middle");
  if (s.l > 1) o += tag(KX(33), 314, "Industrialisation: rises", "t2", Math.min(1, s.l - 1), "middle");
  if (s.l > 2) o += SV.line(KX(40), KY(0.47), KX(40), 290, "c4 dash", op(Math.min(1, s.l - 2))) + tag(KX(40), KY(0.47) - 10, "turning point", "t4", Math.min(1, s.l - 2), "middle");
  if (s.l > 3) o += tag(KX(72), 314, "Mature economy: falls", "t3", Math.min(1, s.l - 3), "middle");
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Kuznets curve: an inverted U relating inequality to income per head">${kuzDraw({ p: 100, l: 4 })}</svg>`;
Lib.stepper($("#stK"), { w: 760, h: 340, label: "The Kuznets curve: inequality rises, peaks and then falls as income per head grows", base: { p: 0, l: 0 }, draw: kuzDraw, tween: 1500, dwell: 5800, steps: [
  { cap: "<b>A farming economy.</b> Incomes are low and fairly similar, so inequality is low.", s: { p: 5, l: 1 } },
  { cap: "<b>Industrialisation.</b> Workers move to higher-paid jobs in cities and owners of capital and skilled workers gain first, so inequality rises.", s: { p: 28, l: 2 } },
  { cap: "<b>The turning point.</b> Once enough people are educated and urbanised, and governments tax and spend more, inequality peaks.", s: { p: 40, l: 3 } },
  { cap: "<b>A mature economy.</b> Wider education, progressive taxes and welfare reduce inequality. The curve is an inverted U, though real countries do not all follow it.", s: { p: 100, l: 4 } },
] });

/* ---------- Lab 1 ---------- */
function labH() {
  if (!$("#le") || !$("#sc") || !$("#gn")) return;
  const le = +$("#le").value, sc = +$("#sc").value, gn = Math.round(Math.pow(10, +$("#gn").value)), hI = Math.max(0, Math.min(1, (le - 20) / 65)), eI = Math.max(0, Math.min(1, sc / 15)), iI = Math.max(0, Math.min(1, (Math.log(gn) - Math.log(100)) / (Math.log(75000) - Math.log(100)))), h = Math.cbrt(hI * eI * iI), avg = (hI + eI + iI) / 3, grp = h >= 0.8 ? "Very high" : h >= 0.7 ? "High" : h >= 0.55 ? "Medium" : "Low";
  $("#r1").textContent = hI.toFixed(2) + " / " + eI.toFixed(2) + " / " + iI.toFixed(2); $("#r2").textContent = h.toFixed(3); $("#r3").textContent = grp;
  $("#rv").textContent = `Life expectancy ${le}, ${sc} years of schooling and GNI of $${gn.toLocaleString("en-US")} give indices of ${hI.toFixed(2)}, ${eI.toFixed(2)} and ${iI.toFixed(2)}. The geometric mean is ${h.toFixed(3)} (${grp.toLowerCase()} human development), compared with a simple average of ${avg.toFixed(3)}: ${avg - h > 0.005 ? "the weakest dimension drags the HDI below the average." : "the three dimensions are balanced, so the two are close."} (Simplified formula for teaching.)`;
  const Y = (v) => 270 - v * 240; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "Index (0 to 1)", "sm");
  [["Health", hI, "f1"], ["Education", eI, "f2"], ["Income", iI, "f1"], ["HDI", h, "f3"]].forEach(([l, v, c], i) => { const x = 55 + i * 85; o += SV.rect(x, Y(v), 60, 270 - Y(v), c) + SV.text(x + 30, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 30, Y(v) - 6, v.toFixed(2), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "le", label: "Life expectancy at birth (years) ", min: 40, max: 85, step: 1, value: 72, fmt: (v) => v, onInput: labH });
Lib.slider($("#g2"), { id: "sc", label: "Years of schooling ", min: 1, max: 15, step: 0.5, value: 9.8, fmt: (v) => v, onInput: labH });
Lib.slider($("#g3"), { id: "gn", label: "GNI per head at PPP (log scale) ", min: 2.5, max: 4.8, step: 0.02, value: 3.85, fmt: (v) => "$" + Math.round(Math.pow(10, v)).toLocaleString("en-US"), onInput: labH });
labH();

/* ---------- Lab 2 ---------- */
function labM() {
  if (!$("#mh") || !$("#ma")) return;
  const H = +$("#mh").value / 100, A = +$("#ma").value / 100, m = H * A;
  $("#t1").textContent = Lib.fmtN(H * 100, 0) + "%"; $("#t2").textContent = Lib.fmtN(A * 100, 0) + "%"; $("#t3").textContent = m.toFixed(3);
  $("#tv").textContent = `${Lib.fmtN(H * 100, 0)}% of people are poor, and on average they are deprived in ${Lib.fmtN(A * 100, 0)}% of the weighted indicators. MPI = ${H.toFixed(2)} × ${A.toFixed(2)} = ${m.toFixed(3)}. The MPI falls if fewer people are poor or if the poor become less deprived, so it can improve even when the headcount does not change.`;
  const Y = (v) => 270 - v * 240; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "Share (0 to 1)", "sm");
  [["H", H, "f1"], ["A", A, "f2"], ["MPI", m, "f3"]].forEach(([l, v, c], i) => { const x = 60 + i * 110; o += SV.rect(x, Y(v), 70, 270 - Y(v), c) + SV.text(x + 35, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 35, Y(v) - 6, v.toFixed(2), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "mh", label: "Headcount ratio H (% of people who are poor) ", min: 5, max: 90, step: 1, value: 30, fmt: (v) => v + "%", onInput: labM });
Lib.slider($("#g5"), { id: "ma", label: "Intensity A (average share of weighted indicators lacking) ", min: 33, max: 80, step: 1, value: 45, fmt: (v) => v + "%", onInput: labM });
labM();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which measure does the description fit?", ["HDI", "MEW", "MPI"],
  [("Combines life expectancy, years of schooling and income at PPP", 0), ("Adds the value of leisure and unpaid work and deducts environmental damage", 1), ("The headcount ratio multiplied by the intensity of deprivation", 2), ("Uses a geometric mean of three indices", 0), ("Starts with GDP and adjusts it for welfare", 1), ("Counts deprivation in cooking fuel, sanitation and electricity", 2), ("Published by the UN Development Programme each year as a ranking", 0), ("A person is poor if deprived in about one third of weighted indicators", 2)],
  "HDI: health, education, income. MEW: welfare-adjusted GDP. MPI: multidimensional poverty.") + MATCH([
  ["Human Development Index", "Composite of life expectancy, schooling and income per head"],
  ["Measure of Economic Welfare", "GDP adjusted for leisure, unpaid work and environmental costs"],
  ["Multidimensional Poverty Index", "Headcount ratio of the poor times the intensity of deprivation"],
  ["Kuznets curve", "Inverted U: inequality rises then falls as income per head grows"],
  ["Geometric mean", "The nth root of the product of n numbers"],
  ["Regrettable expenditure", "Spending that does not raise welfare, such as defence or commuting"]]) + ORDER(
  "Put the stages of the Kuznets curve in order.",
  ["A farming economy with low inequality", "Industrialisation: some workers gain first, so inequality rises", "The turning point is reached", "Education, taxes and welfare spread gains", "Inequality falls in a mature economy"],
  "An inverted U.") + CALC([
  {"q": "Life expectancy is 70 years, the minimum is 20 and the maximum is 85. Calculate the health index (2 decimal places).", "a": 0.77, "unit": "", "tol": 0.01, "hint": "(70 − 20) ÷ 65.", "sol": "50 ÷ 65 = <b>0.77</b>."},
  {"q": "A country has health, education and income indices of 0.8, 0.5 and 0.4. Calculate the HDI as the geometric mean (2 decimal places).", "a": 0.54, "unit": "", "tol": 0.01, "hint": "Cube root of 0.8 × 0.5 × 0.4.", "sol": "0.16^(1/3) = <b>0.54</b>, compared with an average of 0.57."},
  {"q": "30% of a population are multidimensionally poor and they are deprived in 45% of the weighted indicators on average. Calculate the MPI (3 decimal places).", "a": 0.135, "unit": "", "tol": 0.002, "hint": "H × A.", "sol": "0.30 × 0.45 = <b>0.135</b>."},
  {"q": "A country's Gini coefficient was 0.36 and rises to 0.42. By how many percentage points (hundredths of a Gini point) has it risen?", "a": 6, "unit": "points", "tol": 0.1, "hint": "0.42 − 0.36 = 0.06.", "sol": "<b>6 points</b> (0.06). Inequality has risen: consistent with the early stage of the Kuznets curve."}]) + MCQ([
  ("The HDI includes:", ["Health, education and income", "Health and unemployment", "Education and inflation", "Income and crime"], 0, "Life expectancy, schooling and GNI per capita."),
  ("The MEW differs from GDP because it:", ["Adjusts for leisure, unpaid work and environmental damage", "Ignores consumption", "Is a measure of inflation", "Counts only exports"], 0, "It is a welfare-adjusted measure."),
  ("The MPI is calculated as:", ["H × A", "H + A", "H ÷ A", "H − A"], 0, "Headcount ratio times average intensity."),
  ("The Kuznets curve suggests that inequality:", ["Rises and then falls as income per head grows", "Always falls", "Always rises", "Is unrelated to income"], 0, "An inverted U."),
  ("A weakness of the HDI is that it:", ["Ignores income inequality in its basic form", "Includes pollution", "Has no income measure", "Is published only once"], 0, "The standard HDI uses averages.")
], "qz1") + CARDS([
  ("HDI", "Life expectancy, schooling, income; geometric mean."),
  ("HDI groups", "Very high, high, medium, low."),
  ("MEW", "GDP + leisure and unpaid work − environmental damage."),
  ("MPI", "H × A; ten indicators in three dimensions."),
  ("Kuznets curve", "Inverted U: inequality up, then down."),
  ("Turning point", "Where inequality peaks."),
  ("Limits of HDI", "Equal weights, no inequality or environment."),
  ("Limits of MEW", "Subjective values; little data.")]) + MCQ(mc_exam)

build("sy1135", "composite-indicators-hdi-mew-mpi-kuznets", "Composite Indicators: HDI, MEW, MPI and the Kuznets Curve", EY,
  "11.3.3: the Human Development Index, the Measure of Economic Welfare, the Multidimensional Poverty Index and the Kuznets curve of inequality. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
