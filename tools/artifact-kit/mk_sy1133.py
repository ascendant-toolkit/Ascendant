"""Syllabus 11.3.3 (monetary indicators) and 11.3.4 Comparing living standards. Run: python3 tools/artifact-kit/mk_sy1133.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.3.3 to 11.3.4"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b class="kw">standard of living</b> is the material and non-material well-being of people, and the most common <b>monetary indicator</b> is <b>real income per head</b>, measured as <b>GDP</b> (output within the country), <b>GNI</b> (GDP plus net income from abroad) or <b>NNI</b> (GNI less depreciation), each divided by the population and adjusted for price changes. Because prices differ between countries, <b class="kw">purchasing power parity (PPP)</b> converts incomes using the cost of the same basket of goods rather than the market exchange rate. These indicators are easy to calculate but give an <b>imperfect comparison</b> of living standards over time and between countries because of the <b>informal economy, income distribution, quality, externalities, leisure and data errors</b>. Non-monetary indicators such as life expectancy and literacy fill some of the gaps.</p></div>

  <h2>1 · The monetary indicators</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Measure</th><th>Meaning</th><th>Calculation</th></tr>
    <tr><td><b>GDP</b> (gross domestic product)</td><td>The total value of goods and services produced <b>within</b> a country in a year</td><td>Output, expenditure or income method</td></tr>
    <tr><td><b>GNI</b> (gross national income, similar to GNP)</td><td>Income earned by a country's <b>residents</b>, wherever the assets are located</td><td>GDP + net property income from abroad</td></tr>
    <tr><td><b>NNI</b> (net national income)</td><td>GNI after allowing for the wear and tear of capital</td><td>GNI − depreciation (capital consumption)</td></tr>
    <tr><td><b>Real</b> figures</td><td>Adjusted for inflation using a price index and a base year</td><td>Nominal ÷ price index × 100</td></tr>
    <tr><td><b>Per capita</b></td><td>Divided by the population, to show the average</td><td>Total ÷ population</td></tr>
  </table></div>
  <ul>
    <li><b>Real GNI (or GDP) per head</b> is the usual starting point for the standard of living. Use real figures (to remove inflation) and per capita figures (to remove the effect of population size).</li>
    <li><b>GDP versus GNI:</b> a country with large foreign investments or with many foreign firms taking profits home will have a GNI different from its GDP. NNI is a better guide to income that can be consumed without running down the capital stock.</li>
  </ul>

  <h2>2 · Purchasing power parity</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>PPP</b> compares the cost of the <b>same bundle of goods and services</b> in two countries. If the bundle costs 500 rupees at home and $2 in the US, the PPP rate is 250 rupees = $1.</li>
    <li>Converting incomes at <b>market exchange rates</b> understates living standards in low-price countries, since a dollar of income buys much more locally. <b>PPP-adjusted GDP per capita</b> shows what incomes can actually buy and gives a better comparison.</li>
    <li>Limits: baskets differ across countries, quality differs, and non-traded goods (haircuts, rents) make comparisons rough. PPP estimates are revised when the surveys are updated.</li>
  </ul>

  <h2>3 · Problems of comparing living standards using monetary indicators</h2>
  <div class="tw"><table class="t">
    <tr><th>Problem</th><th>Why it matters</th></tr>
    <tr><td><b>Informal and subsistence economy</b></td><td>Unrecorded and unpaid output (home farming, unpaid housework) is left out, so poorer countries are understated</td></tr>
    <tr><td><b>Income distribution</b></td><td>An average hides inequality; a rise may go to a few</td></tr>
    <tr><td><b>Exchange rates and prices</b></td><td>Market exchange rates are volatile and ignore price level differences (use PPP)</td></tr>
    <tr><td><b>Quality and the composition of output</b></td><td>More output may be military, capital or poor quality; total value does not show what is produced</td></tr>
    <tr><td><b>Externalities and sustainability</b></td><td>Pollution and resource depletion are not deducted; clean-up costs even add to GDP</td></tr>
    <tr><td><b>Leisure, health, freedom, culture and climate</b></td><td>Non-material well-being is left out</td></tr>
    <tr><td><b>Accuracy and cost of data</b></td><td>Low-income countries often have weaker statistics and larger errors</td></tr>
    <tr><td><b>Population and price index choice</b></td><td>Population changes alter per capita figures; different baskets give different inflation</td></tr>
  </table></div>
  <h3>Non-monetary indicators</h3>
  <p>Life expectancy, infant mortality, literacy and years of schooling, doctors per 1,000 people, access to clean water and electricity, and the share of people in poverty. These measure outcomes more directly but are harder to combine; composite measures such as the HDI (next page) try to do so.</p>

  <h2>4 · Comparing growth rates and living standards (11.3.4)</h2>
  <ul>
    <li><b>Over time:</b> use <b>real GDP per capita</b> in constant prices. Growth rate = (new − old) ÷ old × 100. Compare average annual growth over several years and use the <b>rule of 70</b> (years to double = 70 ÷ growth rate).</li>
    <li><b>Between countries:</b> compare real GDP per capita at PPP. Compare <b>growth rates</b> too, but beware: a poor country growing at 6% from a <b>low base</b> adds less in dollars per head than a rich country growing at 2%, so a fast growth rate does not mean it has caught up.</li>
    <li><b>Growth is not the same as better living standards.</b> Check distribution, employment, health, education and the environment. Real GDP per head can rise while living standards for most people fall.</li>
  </ul>
  <div class="tip"><b class="h">Answering "to what extent can national income figures be used to compare living standards"</b>Give the definition, say what per capita, real and PPP fix, then give three or four problems (informal economy, distribution, externalities, accuracy), and finish by judging: useful as a rough guide, especially with PPP, but best used with non-monetary indicators.</div>
'''

watch = '''
  <h2>1 · From GDP to NNI per head</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stG"></div>
  <h2>2 · Market exchange rates versus PPP</h2>
  <div id="stP"></div>
'''

explore = '''
  <h2>Lab 1 · Real GDP per head over time</h2>
  <p>Set the growth of nominal GDP, inflation and population growth for a year. See the growth in real GDP per head and how long it takes to double at that rate.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Real GDP growth</small><strong id="r1"></strong></div><div><small>Real GDP per head</small><strong id="r2"></strong></div><div><small>Years to double</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of nominal GDP growth, real GDP growth and real GDP per head growth"></svg></div></div></div>

  <h2>Lab 2 · The PPP adjustment</h2>
  <p>A country's GDP per head is 600,000 local currency units. The exchange rate is 60 units per dollar. A basket of goods costs $10 in the US. Change the local price of the same basket and see GDP per head at market rates and at PPP.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div>
    <div class="readout"><div><small>PPP rate</small><strong id="t1"></strong></div><div><small>GDP per head, market rate</small><strong id="t2"></strong></div><div><small>GDP per head, PPP</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars of GDP per head at the market exchange rate and at PPP"></svg></div></div></div>
'''

practise = '''
  <h2>1 · GDP, GNI or NNI?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the steps to a real per capita figure in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("India and China at market rates and at PPP", "India's economy looks much smaller per head when measured at market exchange rates than at PPP, because prices of food, housing and services are lower than in the US. PPP estimates narrow the gap, though India is still well below the US per head on either measure.", "why PPP gives a better comparison of living standards, with limits.") +
rw("The informal economy in low-income countries", "In many low-income countries a large share of work is in subsistence farming or small informal businesses that do not appear in the official statistics. GDP therefore tends to understate output and living standards, and the growth rate may be inaccurate too.", "the problem of unrecorded output in a comparison between low- and high-income countries.") +
rw("Oil spills and GDP", "Spending on cleaning up a major oil spill raises measured output, even though the spill reduces welfare. National income statistics normally add the clean-up spending and do not deduct the environmental damage.", "externalities and why alternatives such as MEW adjust GDP.") +
rw("Growth and inequality", "Some fast-growing economies have seen the top income groups take most of the gains while the incomes of the poorest changed little. Average GDP per head rose strongly, yet many people saw little improvement.", "why a rise in GDP per head may not raise living standards for most people.")
)

mc_exam = [
  ("Which statement about national income accounting is correct? (May/June 2021 · 31 · Q21, reworded)", ["Depreciation does not need to be subtracted from GDP because firms have already allowed for it", "GDP overstates the value of output because profit includes supernormal profit", "GDP is a better measure of living standards than GNP because net property income from abroad is not available to citizens", "GNP per capita ignores many important factors that affect citizens' living standards"], 3, "GNP per head is an average of money income. It ignores distribution, leisure, the environment and many non-material factors."),
  ("A government uses personal disposable income per head as a measure of the standard of living. What does this measure not take into account? (Oct/Nov 2021 · 31 · Q21, reworded)", ["Changes in the average price level", "The level of direct taxation", "The level of national income", "The size of the population"], 0, "Disposable income is after tax and per head, but unless it is deflated (made real) it ignores price changes."),
  ("GNP per head has increased by 10% over five years. What is not a valid reason to doubt that average living standards have risen by 10%? (Oct/Nov 2021 · 33 · Q19, reworded)", ["The distribution of income may have changed a lot", "The general price level is likely to have changed", "The size of the population may have changed", "The workforce may have produced more by working longer hours"], 2, "A per head figure already allows for population. The other three are valid doubts: distribution, inflation and longer working hours."),
  ("Real GNP per capita is used to compare living standards in a developed and a developing country. What is not a good reason to question the accuracy of this comparison? (Oct/Nov 2022 · 33 · Q20, reworded)", ["Spending patterns differ, so price indices are not accurate", "People enjoy very different amounts of leisure time", "The extent of the unrecorded economy differs", "Purchasing power parity has been used to make the comparison"], 3, "PPP improves the comparison. The other three are genuine reasons for caution."),
  ("What is a definition of purchasing power parity? (Oct/Nov 2023 · 31 · Q28, reworded)", ["The amount of domestic currency needed to buy a unit of foreign currency", "The quantity of a currency needed to buy the same basket of goods in both countries", "The quantity of goods a person on an average income can buy", "The value of household spending on goods and services in a country"], 1, "PPP compares the cost of an identical basket in two countries."),
  ("Which combination indicates that GDP per capita is likely to be an accurate indicator of living standards over time? Hidden economy as a share of GDP, quality of goods and services, income distribution. (Oct/Nov 2022 · 31 · Q20, reworded)", ["Large, improving, unequal", "Large, constant, equal", "Small, improving, equal", "Small, constant, unequal"], 2, "A small hidden economy, improving quality and equal distribution make average income closer to the typical person's experience."),
  ("The table shows GDP and population of four countries. Which is most likely to have the lowest standard of living? A: Bangladesh, GDP $206.7bn, population 153.5m. B: India, $2,989bn, 1,147.9m. C: Nigeria, $292.7bn, 138.3m. D: South Africa, $467.1bn, 43.8m. (May/June 2024 · 31 · Q28, reworded)", ["A", "B", "C", "D"], 0, "GDP per head: A about $1,350, B about $2,600, C about $2,100, D about $10,700. Bangladesh has the lowest."),
  ("Why is real GDP per head thought to be an imperfect measure of welfare in developed economies? (Feb/March 2022 · 32 · Q19, reworded)", ["Governments often manipulate data", "No account is taken of inflation", "The data's content and coverage are restricted", "The shadow economy is bigger than the official economy"], 2, "It leaves out unpaid work, leisure, the environment and distribution.")
]

exam = exam_page("GDP and the other monetary measures of living standards",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Whether GDP is a good measure of living standards is among the most frequent Paper 4 questions, in 12, 13, 20 and 25 mark forms, and PPP appears in data response. Reworded past questions are below, with eight Paper 3 multiple choice questions.",
  [("Data response, 2 and 6 marks", "1", "May/June 2023 (42) Q1(a) and (c)"), ("Essay parts, 12 and 13 marks", "4", "Oct/Nov 2020 (42) Q7(a) and (b); May/June 2020 (42) Q6(b); May/June 2022 (42) Q6(b)"), ("Essays, 20 and 25 marks", "2", "May/June 2024 (41) Q5; Oct/Nov 2021 (42) Q5"), ("Multiple choice (Paper 3)", "8 shown below", "2020 to 2025")],
  [
  eq("Based on May/June 2023 · 9708/42 · Q1(a)", "2 marks", "Explain what is meant by purchasing power parity (PPP).",
     ["A comparison of the cost of a bundle of goods and services bought in the local currency with the cost of the same bundle in another currency (one mark each).",
      "An example with figures, such as a bundle costing 500 local units or $2 giving a PPP rate of 250 units to $1."],
     "Same bundle, two countries. Quote a short example.",
     [[("k", "PPP compares what the same basket of goods and services costs in two currencies. If it costs 400 units at home and $4 in the US, the PPP rate would be 100 units to the dollar.")]]),
  eq("Based on May/June 2023 · 9708/42 · Q1(c)", "6 marks", "Using the data below, consider the change in the standard of living in Country X and Country Y between 2015 and 2020. (Country X: GDP per head at PPP $9,000 to $11,500, unemployment 6% to 5%, Gini coefficient 0.40 to 0.35. Country Y: $4,000 to $4,400, unemployment 8% to 7.5%, Gini 0.32 to 0.37.)",
     ["Define the standard of living and split material from non-material.",
      "Quote changes with percentages: X's GDP per head rose by 27.8% and Y's by 10%; unemployment fell in both; the Gini fell in X and rose in Y.",
      "Link GDP per head to the material standard of living, say lower inequality in X means the gains are more evenly spread and higher inequality in Y means less evenly spread, so X has probably improved more; lower unemployment is linked to higher living standards."],
     "Define. Quote changes. Interpret each measure. Conclude: X probably better off, Y mixed.",
     [[("k", "The standard of living is the material and non-material well-being of people. GDP per head at PPP rose by about 28% in Country X and 10% in Country Y, so material living standards increased in both."), ("n", "Unemployment fell slightly in both, which is linked to a higher standard of living. However, the Gini coefficient fell in X, so the gains were more evenly shared, but it rose in Y, so the gains in Y may have gone mainly to richer households.")],
      [("e", "Overall, living standards probably rose more in X. In Y the average rise may overstate the improvement for typical households. The data do not cover health, education or the environment.")]]),
  eq("Based on May/June 2024 · 9708/41 · Q5", "20 marks", "National income statistics are often used as a measure of the standard of living. Consider to what extent they can be used to compare the standard of living between low-income and high-income countries.",
     ["Define the standard of living and the distinction between low- and high-income countries, for example by income per head.",
      "Difficulties of comparison: culture, climate, the subsistence and informal economy, difficulty of collecting data, income distribution, exchange rates and purchasing power.",
      "Comment on which measure of national income should be used (real, per capita, PPP).",
      "Evaluation: assess how closely national income links to the standard of living and bring in alternative measures such as the HDI."],
     "Define. Real per capita PPP. Four difficulties. Alternatives. Judge: useful but incomplete.",
     [[("k", "The standard of living is the material and non-material well-being of a population. National income per head, adjusted for inflation and at purchasing power parity, is often used as a proxy."), ("n", "It may be a rough guide because high-income countries usually have better health, education and housing. However, comparisons between low- and high-income countries have problems. In low-income countries a large share of output is subsistence or informal and is not recorded, so income may be understated. Data collection is also harder and less accurate.")],
      [("n", "Averages hide distribution, so a high GDP per head could coexist with many people in poverty. Market exchange rates also ignore differences in price levels, so PPP should be used. Leisure, health, education, freedom and the environment are not included, so two countries with the same income could have different living standards."), ("e", "National income statistics may therefore be useful as a first indicator, especially at PPP, but they are best supported by non-monetary indicators such as the HDI.")]]),
  eq("Based on May/June 2022 · 9708/42 · Q6(b)", "13 marks", "Discuss whether GDP is the best measure of the standard of living.",
     ["Define GDP and its use as real GDP per head as a measure of the standard of living.",
      "Discuss the merits of HDI, MEW or other alternatives, setting them against GDP.",
      "Level 4 (9 to 13) compares GDP with at least one alternative and evaluates the relative merits."],
     "GDP and why it is used. Its limits. One alternative. Judge which is better and when.",
     [[("k", "Real GDP per head measures the total value of output per person, adjusted for inflation, so it is easy to calculate and compare, and is often linked to higher living standards."), ("n", "However, it ignores distribution, unrecorded work, leisure and the environment, and spending on clean-up or defence adds to GDP. The HDI adds life expectancy and education, so it shows health and knowledge, while the MEW adjusts GDP for leisure, unpaid work and environmental damage.")],
      [("e", "GDP may be the best measure for the speed with which data can be collected and compared, but as a guide to well-being the HDI or MEW are probably better, although they involve judgements about weights.")]])
  ],
  )

tips = tips_html(
  [("Use 'real' and 'per capita'.", "Real removes inflation. Per capita removes population size. Say both."),
   ("GDP versus GNI.", "GNI = GDP + net property income from abroad. NNI = GNI minus depreciation."),
   ("PPP in one line.", "The same basket costs the same in both countries. It corrects for price level differences."),
   ("Give three or four problems.", "Informal economy, distribution, externalities, accuracy, non-material factors."),
   ("Quote percentage changes.", "In data questions, calculate the growth rate and say what it means."),
   ("Mind the low base.", "A poor country growing quickly may still add less per head than a rich one."),
   ("Judge.", "Useful as a rough guide, especially at PPP, but best used with non-monetary indicators.")],
  [("Real per capita", "Real GDP per head adjusts for inflation and population, so it may show average living standards more accurately than nominal GDP."),
   ("PPP", "Purchasing power parity adjusts for differences in price levels, so it could give a fairer comparison than market exchange rates."),
   ("Limits", "National income statistics may understate output in countries with large informal or subsistence sectors."),
   ("Average", "Average income could hide inequality, so living standards for the typical person may differ from the average."),
   ("Alternatives", "Non-monetary indicators may capture health, education and the environment that income does not.")],
  [CW["define"], CW["explain"], CW["consider"], CW["discuss"]]) + FC

js = '''
/* ---------- GDP to NNI ---------- */
const GY = (v) => 300 - v * 2.2;
function gdpDraw(s) {
  let o = axes(70, 300, 730, 30, "", "$bn"); [0, 40, 80, 120].forEach((v) => (o += SV.text(64, GY(v) + 4, v, "sm", { "text-anchor": "end" })));
  const bar = (i, v, c, l, k) => (k > 0 ? SV.rect(110 + i * 150, GY(v), 100, 300 - GY(v), c, op(k)) + tag(160 + i * 150, GY(v) - 8, v, "t1", k, "middle") + tag(160 + i * 150, 322, l, "t1", k, "middle") : "");
  o += bar(0, 120, "f1", "GDP", s.a) + bar(1, 114, "f1", "GNI", s.b) + bar(2, 105, "f3", "NNI", s.c);
  if (s.b > 0) o += tag(310, GY(114) - 28, "− 6 net income paid abroad", "t2", s.b, "middle");
  if (s.c > 0) o += tag(460, GY(105) - 28, "− 9 depreciation", "t2", s.c, "middle");
  if (s.d > 0) o += SV.rect(600, 190, 130, 110, "f2", op(0.6 * s.d)) + tag(665, 230, "÷ 10m people", "t4", s.d, "middle") + tag(665, 256, "= $10,500", "t4", s.d, "middle") + tag(665, 322, "NNI per head", "t4", s.d, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="GDP of 120, GNI of 114 after net income paid abroad and NNI of 105 after depreciation, then NNI per head">${gdpDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 340, label: "From GDP to GNI to NNI and then per head", base: { a: 0, b: 0, c: 0, d: 0 }, draw: gdpDraw, tween: 1100, dwell: 5600, steps: [
  { cap: "<b>GDP</b> is the value of everything produced inside the country: $120bn.", s: { a: 1 } },
  { cap: "<b>GNI.</b> Foreign firms and investors take $6bn of profit and interest abroad that residents do not earn. Add net property income from abroad (here −$6bn): GNI is $114bn.", s: { a: 1, b: 1 } },
  { cap: "<b>NNI.</b> Capital wears out (depreciation $9bn). Deduct it to find income that could be spent without shrinking the capital stock: $105bn.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Per head.</b> With a population of 10 million, NNI per head is $10,500. Adjusting for inflation gives the real figure used to track living standards.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Market versus PPP ---------- */
const PB = (v) => 300 - v * 0.0052;
function ppDraw(s) {
  let o = axes(70, 300, 730, 30, "", "GDP per head ($)"); [0, 15000, 30000, 45000].forEach((v) => (o += SV.text(64, PB(v) + 4, v.toLocaleString("en-US"), "sm", { "text-anchor": "end" })));
  const bar = (x, v, c, l, k) => (k > 0 ? SV.rect(x, PB(v), 80, 300 - PB(v), c, op(k)) + tag(x + 40, PB(v) - 8, "$" + Math.round(v).toLocaleString("en-US"), "t1", k, "middle") + tag(x + 40, 322, l, "sm", k, "middle") : "");
  o += bar(120, 3000, "f2", "Country A: market", s.a) + bar(240, 45000, "f1", "Country B: market", s.a);
  o += bar(400, 3000 + 6000 * Math.min(1, s.b), "f2", "Country A: PPP", s.b) + bar(520, 45000, "f1", "Country B: PPP", s.b);
  if (s.c > 0) o += tag(400, 34, "Gap: 15 to 1 at market rates, 5 to 1 at PPP", "t4", s.c, "middle");
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 340, label: "GDP per head at market exchange rates compared with PPP for a low-price and a high-price country", base: { a: 0, b: 0, c: 0 }, draw: ppDraw, tween: 1300, dwell: 5800, steps: [
  { cap: "<b>At market exchange rates</b> country A's GDP per head is $3,000 and country B's is $45,000: B looks 15 times richer.", s: { a: 1 } },
  { cap: "<b>But prices differ.</b> Food, housing and services cost much less in A. A basket of goods costs one third of what it does in B.", s: { a: 1 } },
  { cap: "<b>PPP adjustment.</b> Using the cost of the same basket, A's income buys what $9,000 buys in B. The gap narrows to 5 to 1.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labR() {
  if (!$("#ng") || !$("#pi") || !$("#pp")) return;
  const n = +$("#ng").value / 10, p = +$("#pi").value / 10, q = +$("#pp").value / 10, real = ((1 + n / 100) / (1 + p / 100) - 1) * 100, ph = ((1 + real / 100) / (1 + q / 100) - 1) * 100;
  $("#r1").textContent = Lib.fmtN(real, 1) + "%"; $("#r2").textContent = (ph >= 0 ? "+" : "") + Lib.fmtN(ph, 1) + "%"; $("#r3").textContent = ph > 0.05 ? Lib.fmtN(70 / ph, 0) + " yrs" : "never";
  $("#rv").textContent = `Nominal GDP grows ${Lib.fmtN(n, 1)}%, but inflation of ${Lib.fmtN(p, 1)}% leaves real growth of ${Lib.fmtN(real, 1)}%. With population growth of ${Lib.fmtN(q, 1)}%, real GDP per head changes by ${Lib.fmtN(ph, 1)}%. ${ph > 0.05 ? "At that rate real income per head doubles in about " + Lib.fmtN(70 / ph, 0) + " years (rule of 70)." : "Real income per head is not rising, so material living standards are not improving on this measure."}`;
  const Y = (v) => 150 - v * 8; let o = SV.line(40, 150, 400, 150) + SV.line(40, 20, 40, 280) + SV.text(46, 16, "% a year", "sm");
  [["Nominal GDP", n, "f1"], ["Real GDP", real, "f1"], ["Real GDP per head", ph, "f3"]].forEach(([l, v, c], i) => { const x = 60 + i * 115, y = Y(Math.max(-17, Math.min(17, v))); o += SV.rect(x, Math.min(y, 150), 80, Math.abs(y - 150), c) + SV.text(x + 40, 296, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, v >= 0 ? y - 8 : y + 18, Lib.fmtN(v, 1) + "%", "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ng", label: "Nominal GDP growth, % ", min: 0, max: 200, step: 5, value: 90, fmt: (v) => (v / 10).toFixed(1), onInput: labR });
Lib.slider($("#g2"), { id: "pi", label: "Inflation, % ", min: 0, max: 150, step: 5, value: 40, fmt: (v) => (v / 10).toFixed(1), onInput: labR });
Lib.slider($("#g3"), { id: "pp", label: "Population growth, % ", min: 0, max: 50, step: 1, value: 15, fmt: (v) => (v / 10).toFixed(1), onInput: labR });
labR();

/* ---------- Lab 2 ---------- */
function labP() {
  if (!$("#bk")) return;
  const b = +$("#bk").value, ppp = b / 10, mk = 600000 / 60, pp = 600000 / ppp;
  $("#t1").textContent = Lib.fmtN(ppp, 0) + " per $"; $("#t2").textContent = "$" + Math.round(mk).toLocaleString("en-US"); $("#t3").textContent = "$" + Math.round(pp).toLocaleString("en-US");
  $("#tv").textContent = b < 600 ? `The basket costs ${b} local units against $10 in the US, so one dollar of income buys the same basket as ${Lib.fmtN(ppp, 0)} local units, compared with the market rate of 60. The currency is worth more at PPP, so GDP per head at PPP ($${Math.round(pp).toLocaleString("en-US")}) is higher than at the market rate.` : b > 600 ? `Prices here are higher than the market exchange rate suggests, so GDP per head at PPP is lower than at the market rate.` : "The PPP rate equals the market rate, so both measures agree.";
  const Y = (v) => 270 - v / 40000 * 240; let o = SV.line(60, 270, 400, 270) + SV.line(60, 270, 60, 20) + SV.text(66, 16, "GDP per head ($)", "sm");
  [["Market rate", mk, "f1"], ["PPP", pp, "f3"]].forEach(([l, v, c], i) => { const x = 100 + i * 140; o += SV.rect(x, Y(Math.min(v, 40000)), 90, 270 - Y(Math.min(v, 40000)), c) + SV.text(x + 45, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 45, Y(Math.min(v, 40000)) - 8, "$" + Math.round(v).toLocaleString("en-US"), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "bk", label: "Local price of the basket (units) ", min: 100, max: 900, step: 25, value: 300, fmt: (v) => v, onInput: labP });
labP();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which measure is it?", ["GDP", "GNI", "NNI"],
  [("Value of output produced inside the country's borders", 0), ("GDP plus net property income from abroad", 1), ("GNI minus depreciation of capital", 2), ("Includes profits that foreign-owned firms in the country send home", 0), ("Income earned by a country's residents wherever their assets are", 1), ("Shows income that could be consumed without running down the capital stock", 2), ("Output method, income method or expenditure method", 0), ("Used by the World Bank for income classification", 1)],
  "GDP: inside the borders. GNI: residents' income. NNI: GNI minus depreciation.") + MATCH([
  ["Real GDP per capita", "GDP adjusted for inflation and divided by the population"],
  ["Purchasing power parity", "Compares the cost of the same basket of goods in two countries"],
  ["Informal economy", "Unrecorded economic activity that is missing from official statistics"],
  ["Net property income from abroad", "Income earned abroad less income paid abroad"],
  ["Rule of 70", "Years to double ≈ 70 ÷ growth rate"],
  ["Low base effect", "A poor country's fast growth adds little in absolute terms"]]) + ORDER(
  "Put the steps to a real per capita figure in order.",
  ["Start with GDP (or GNI) in current prices", "Adjust for price changes using a price index and a base year", "Divide by the population", "Compare the growth rate over time", "Use PPP if comparing between countries"],
  "Real removes inflation; per capita removes population; PPP adjusts for price levels.") + CALC([
  {"q": "GDP is $200bn. Net property income from abroad is −$12bn and depreciation is $15bn. Calculate NNI ($bn).", "a": 173, "unit": "$bn", "tol": 0.5, "hint": "GDP + net income − depreciation.", "sol": "200 − 12 − 15 = <b>$173bn</b>."},
  {"q": "Real GDP is $90bn and the population is 30 million. Calculate real GDP per head ($).", "a": 3000, "unit": "$", "tol": 0.5, "hint": "90,000m ÷ 30m.", "sol": "<b>$3,000</b>."},
  {"q": "Nominal GDP rises by 8% and prices by 5%. Calculate the approximate real growth (%, 1 decimal place).", "a": 2.9, "unit": "%", "tol": 0.1, "hint": "1.08 ÷ 1.05 − 1.", "sol": "1.08 ÷ 1.05 = 1.0286, so about <b>2.9%</b> (roughly 3%)."},
  {"q": "A basket costs 750 rupees in one country and $5 in the US. Calculate the PPP rate (rupees per $).", "a": 150, "unit": "rupees", "tol": 0.5, "hint": "750 ÷ 5.", "sol": "<b>150 rupees = $1</b>."}]) + MCQ([
  ("GNI is calculated as:", ["GDP + net property income from abroad", "GDP − depreciation", "GDP + imports", "GDP − taxes"], 0, "GNI adds income from abroad and subtracts income paid abroad."),
  ("PPP is used to:", ["Adjust for differences in price levels between countries", "Measure inflation", "Calculate unemployment", "Convert at market exchange rates"], 0, "It compares the cost of the same basket."),
  ("Which is a problem with GDP per head as a measure of living standards?", ["It ignores income distribution", "It is always accurate", "It includes leisure", "It includes the informal economy fully"], 0, "An average hides who gets the income."),
  ("Real GDP per head differs from nominal GDP because it:", ["Removes the effect of inflation", "Includes the shadow economy", "Is measured in dollars", "Counts only exports"], 0, "Prices are held constant using a base year."),
  ("Which is a non-monetary indicator of the standard of living?", ["Life expectancy", "GDP per head", "GNI", "Average wage"], 0, "Life expectancy measures health outcomes directly.")
], "qz1") + CARDS([
  ("GDP", "Value of output within the country."),
  ("GNI", "GDP + net property income from abroad."),
  ("NNI", "GNI − depreciation."),
  ("Real", "Adjusted for inflation."),
  ("Per capita", "Divided by population."),
  ("PPP", "Cost of the same basket in two countries."),
  ("Problems of GDP", "Informal economy, distribution, externalities, accuracy."),
  ("Rule of 70", "70 ÷ growth rate = years to double.")]) + MCQ(mc_exam)

build("sy1133", "monetary-indicators-living-standards", "Monetary Indicators of Living Standards: GDP, GNI, NNI and PPP", EY,
  "11.3.3 to 11.3.4: real income per head, GDP, GNI and NNI, purchasing power parity, the problems of comparing living standards and comparing growth rates. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
