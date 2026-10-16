"""Syllabus 11.4.1 Population growth and structure, optimum population, urbanisation. Run: python3 tools/artifact-kit/mk_sy1141.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.4.1"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Population change is the sum of <b class="kw">natural increase</b> (<b>birth rate minus death rate</b>) and <b class="kw">net migration</b>. In developing countries <b>high birth rates and falling death rates</b> give rapid growth and a young population with a high <b class="kw">dependency ratio</b>; in developed countries <b>low birth rates and long life expectancy</b> give an ageing population and a different dependency problem. The <b class="kw">optimum population</b> is the size that gives the <b>highest income per head</b> with the existing resources, capital and technology, and <b>urbanisation</b> (the share of people living in towns and cities) rises as economies develop. Each has costs and benefits for growth and living standards.</p></div>

  <h2>1 · Measuring population change</h2>
  <div class="tw"><table class="t">
    <tr><th>Measure</th><th>Meaning</th><th>Calculation</th></tr>
    <tr><td><b>Birth rate</b></td><td>Live births per 1,000 people per year</td><td>Births ÷ population × 1,000</td></tr>
    <tr><td><b>Death rate</b></td><td>Deaths per 1,000 people per year</td><td>Deaths ÷ population × 1,000</td></tr>
    <tr><td><b>Natural increase</b></td><td>Birth rate minus death rate</td><td>Per 1,000; divide by 10 for a percentage</td></tr>
    <tr><td><b>Infant mortality rate</b></td><td>Deaths of babies under one year old per 1,000 live births</td><td>Infant deaths ÷ live births × 1,000</td></tr>
    <tr><td><b>Net migration</b></td><td>Immigrants minus emigrants</td><td>Per 1,000 or in numbers</td></tr>
    <tr><td><b>Population growth rate</b></td><td>Natural increase plus net migration</td><td>(Birth − death + net migration) ÷ 10 gives %</td></tr>
  </table></div>

  <h2>2 · Causes of changes in birth, death and migration</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Birth rate:</b> <b>falls</b> with higher incomes, better education (especially of women), access to contraception, urbanisation (children are costly in cities), pensions that remove the need for children to support old age, and lower infant mortality (parents need fewer births to ensure survivors). <b>Higher</b> where children are needed as farm labour, where infant mortality is high, and where culture or religion favours large families.</li>
    <li><b>Death rate:</b> <b>falls</b> with better nutrition, clean water and sanitation, health care and vaccination. It <b>rises</b> with disease epidemics, famine, conflict and an ageing population.</li>
    <li><b>Infant mortality:</b> falls with maternal health care, immunisation, clean water and education.</li>
    <li><b>Net migration:</b> <b>pull factors</b> (jobs, higher wages, services, safety) and <b>push factors</b> (unemployment, poverty, conflict, climate) together with immigration rules. Rural-urban migration within a country is also important in development.</li>
  </ul>
  <h3>The demographic transition</h3>
  <p>As an economy develops, <b>death rates fall first</b> (health and food improve) and <b>birth rates fall later</b>, so population growth speeds up and then slows: stage 1 both high; stage 2 death rate falls, population rises fast; stage 3 birth rate falls; stage 4 both low, with an ageing population.</p>

  <h2>3 · Population structure and the dependency ratio</h2>
  <ul>
    <li><b>Dependency ratio</b> = (people under 15 + people over 64) ÷ (people aged 15 to 64) × 100. It shows how many dependants each 100 workers support.</li>
    <li><b>Developing economies</b> usually have a <b>young</b> population (a broad base on the age pyramid) and a <b>high dependency ratio</b> from children. Income per head is low, so saving, investment and spending on education are squeezed.</li>
    <li><b>Developed economies</b> often have an <b>ageing</b> population: low birth rates and long life expectancy. The old-age dependency ratio rises, so the workforce shrinks, and more is needed for pensions and health care, which could raise taxes or debt.</li>
    <li>A fall in the birth rate can create a <b>demographic dividend</b>: a large working-age population with fewer dependants can raise savings, investment and growth, if there are jobs for them.</li>
  </ul>

  <h2>4 · Optimum population</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li>The <b>optimum population</b> is the size of population that, with the available resources, capital and technology, <b>gives the highest output (income) per head</b>, maximising the standard of living.</li>
    <li><b>Under-population:</b> too few workers to use resources fully; more people would raise output per head (division of labour, bigger markets). <b>Over-population:</b> too many for the resources; diminishing returns lower output per head.</li>
    <li>The optimum is <b>not fixed</b>: <b>better technology, more capital, higher labour productivity, new resources</b> and more education <b>raise</b> it, so a country can support more people. Resource depletion lowers it.</li>
    <li>Note that a rise in birth rate does not raise the optimum; it changes the actual population.</li>
  </ul>

  <h2>5 · Urbanisation</h2>
  <ul>
    <li><b>Urbanisation</b> is the growing share of the population living in cities. It rises as people move from low-productivity farming to jobs in industry and services (pull) and as rural poverty pushes them out.</li>
    <li><b>Benefits:</b> higher productivity (agglomeration, shared infrastructure), larger markets, easier access to health, education and services, and a lower birth rate.</li>
    <li><b>Costs:</b> slums and informal housing, congestion and pollution, strain on water, sanitation and transport, urban unemployment, and loss of labour in rural areas.</li>
  </ul>
  <div class="tip"><b class="h">Evaluation point</b>Whether a rising or falling population is a problem depends on the structure and on whether output per head is rising. A rapid rise in a poor country may strain resources, but a younger population can supply labour and demand. A falling population in a rich country can cause a shortage of workers, but productivity growth and immigration can offset it.</div>
'''

watch = '''
  <h2>1 · The demographic transition</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stD"></div>
  <h2>2 · Optimum population</h2>
  <div id="stO"></div>
'''

explore = '''
  <h2>Lab 1 · Population change</h2>
  <p>Set the birth rate, the death rate and net migration (all per 1,000 people per year). See the growth rate and how long the population takes to double.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Natural increase</small><strong id="r1"></strong></div><div><small>Growth rate</small><strong id="r2"></strong></div><div><small>Years to double</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of birth rate, death rate, net migration and the resulting growth per 1000 people"></svg></div></div></div>

  <h2>Lab 2 · The dependency ratio</h2>
  <p>Set the share of the population under 15 and over 64. The rest are of working age.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Working age</small><strong id="t1"></strong></div><div><small>Dependency ratio</small><strong id="t2"></strong></div><div><small>Structure</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Stacked bar of the young, working age and old shares of the population"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which change raises or lowers the birth rate?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the stages of the demographic transition in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("China's changing population", "China's one-child policy lowered the birth rate, and later the two-child and three-child policies tried to raise it. The working-age population has started to shrink and the share of older people is rising. Economists link this to a smaller labour force, higher pension and health costs and slower growth.", "an ageing population, the dependency ratio and the optimum population.") +
rw("Japan's ageing society", "Japan has one of the highest shares of older people and a falling population. Responses include raising the retirement age, encouraging more women and older people to work, using robots and technology, and slowly opening up to migrant workers.", "the effects of an ageing population in a developed economy.") +
rw("Sub-Saharan Africa's young population", "Many countries in the region have median ages below 20 and birth rates well above the world average. The large working-age population to come could bring a demographic dividend if jobs, education and health improve, or high unemployment if they do not.", "a youthful structure, the dependency ratio and the demographic dividend.") +
rw("Rapid urbanisation in Lagos and Dhaka", "Cities in developing countries have grown quickly as people move from farms. The cities offer jobs and services but many residents live in informal settlements with poor sanitation and long commutes, which shows the costs of urbanisation as well as the gains.", "the costs and benefits of urbanisation.")
)

mc_exam = [
  ("What is least likely to lead to an increase in the optimum population? (Feb/March 2025 · 32 · Q27, reworded)", ["An improvement in labour productivity", "An improvement in the quality of capital and technology", "An increase in the birth rate and a fall in the death rate", "An increase in the availability of natural resources"], 2, "The optimum depends on productivity, capital, technology and resources. A higher birth rate or lower death rate changes the actual population, not the optimum."),
  ("What will increase the size of a country's optimum population? (May/June 2024 · 31 · Q29, reworded)", ["A rise in the birth rate", "A lower retirement age", "A rise in the stock of capital", "A fall in productivity in industry"], 2, "More capital raises output per head at each population size, so the optimum moves to the right."),
  ("The optimum population is the level at which real output per head is highest. The diagram shows output per head against population for two years, with the curve shifting up and to the right in year 2. Which change could not satisfactorily explain the shift? (Oct/Nov 2024 · 33 · Q25, reworded)", ["Population has increased", "The state of technology has improved", "The stock of capital has increased", "The volume of productive resources in use has increased"], 0, "A larger actual population is a movement along a curve, not a shift of the curve. Technology, capital and resources shift it."),
  ("In some countries life expectancy has fallen but the birth rate remains high. Which effect will this have? (May/June 2022 · 32 · Q28, reworded)", ["Fewer schools will be needed", "More facilities will be needed for older people", "The population will age", "The working population will tend to become a smaller share of the total"], 3, "With a high birth rate and early deaths, the young make up a larger share and the working-age group a smaller one."),
  ("The table gives birth rate, death rate and infant mortality per 1,000, and the share under 16, for Singapore (12, 4, 5, 18%), Hong Kong (15, 6, 8, 20%) and China (20, 9, 28, 38%). Which conclusion can be drawn? (May/June 2024 · 32 · Q29, reworded)", ["China had the highest percentage of children who died in infancy", "People in Hong Kong lived the longest", "Singapore had the largest number of people over 16", "Singapore's population was expected to fall in the next five years"], 0, "Infant mortality of 28 per 1,000 is the highest. The table gives no life expectancy or population totals."),
  ("A table shows urbanisation in more developed, less developed and least developed regions between 2010 and 2050: 75% to 86%, 45% to 66% and 29% to 55%. Which relationship can be confirmed? (Oct/Nov 2022 · 31 · Q29, reworded)", ["The least developed regions have the largest urban populations in both years", "The more developed regions have the lowest growth in urbanisation between 2010 and 2050", "The region with the biggest total population in 2010 has the fastest population growth", "The region with the largest urban population in 2010 has the highest urbanisation level by 2050"], 1, "The urbanised share rises by 11 points in more developed regions against 21 and 26 points in the others."),
  ("China's census shows a falling birth rate, more people reaching retirement age and a shrinking share of working-age people. Which policy would most quickly sustain economic growth? (Oct/Nov 2023 · 33 · Q19, reworded)", ["Allow more immigration of labour", "Encourage women to leave work to have more children", "Increase research to raise labour productivity", "Tax workers more to pay for pensions"], 0, "Immigration adds workers straight away. Having children takes about 20 years, and research takes time to raise productivity."),
  ("Which influence is least likely to promote sustainable economic growth in a developing economy? (Feb/March 2021 · 32 · Q18, reworded)", ["High saving rates", "Involvement in free trade", "Protected property rights", "Rapid population growth"], 3, "Very fast population growth can reduce capital per worker and spread resources thinly."),
  ("Over a year, nominal national income increased by 2%, inflation was 3% and population rose by 1%. Which statement is correct? (Feb/March 2024 · 32 · Q19, reworded)", ["Real income per head fell by about 2%", "Real income per head rose by 1%", "Real income per head rose by 4%", "There was no change in real income per head"], 0, "Real income fell about 1% (2 − 3). Spread over a population that grew 1%, real income per head fell about 2%.")
]

exam = exam_page("population, dependency, optimum population and urbanisation",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Population and dependency questions appear as 2 to 7 mark data response parts, as 12 and 13 mark essay parts and in 25 mark essays. Reworded past questions are below, with nine Paper 3 multiple choice questions.",
  [("Data response parts, 2 to 7 marks", "3", "Feb/March 2025 (42) Q1(a), (c), (d)"), ("Essay parts, 12 and 13 marks", "2", "May/June 2020 (41) Q7(a) (see 11.3.1); Feb/March 2021 (42) Q5(b)"), ("Essay, 25 marks", "1", "Oct/Nov 2022 (43) Q6"), ("Multiple choice (Paper 3)", "9 shown below", "2020 to 2025")],
  [
  eq("Based on Feb/March 2025 · 9708/42 · Q1(a)", "2 marks", "Explain what is meant by an optimum population.",
     ["The size of population which, with the existing resources, factors of production and state of technology, yields the highest income per head (1).",
      "Where the standard of living is at a maximum (1)."],
     "Highest income per head. With given resources, capital and technology.",
     [[("k", "An optimum population is the size at which, given the economy's resources, capital and technology, income per head is highest, so the standard of living is at a maximum.")]]),
  eq("Based on Feb/March 2025 · 9708/42 · Q1(c)", "6 marks", "A country's birth rate has fallen sharply, and the share of its population above retirement age has risen. Identify two observations economists would make about these changes and analyse how each would affect GDP.",
     ["Observation 1: fewer young people means a smaller pool of future workers, innovators and entrepreneurs, which lowers output and productivity.",
      "Observation 2: a larger share of older people raises the cost of pensions, health and social services, which may increase the budget deficit and reduce investment.",
      "Each observation analysed with a link to GDP, with a mark for identification and marks for development."],
     "Observation, link, GDP effect, twice.",
     [[("k", "One observation is that a smaller number of young people is entering the labour force."), ("n", "This means a smaller pool of potential workers, innovators and entrepreneurs, so the growth of the labour force and productivity could slow. Aggregate supply may grow more slowly and GDP could be lower.")],
      [("k", "A second observation is that the share of older people is rising."), ("n", "This could raise government spending on pensions, health care and social services. If funded by borrowing or higher taxes, the budget deficit may rise or private spending and investment may fall, which could reduce GDP.")]]),
  eq("Based on Feb/March 2021 · 9708/42 · Q5(b)", "13 marks", "'Rising population levels in a developing economy create many problems while falling population levels in a developed economy cause even greater problems.' To what extent is this true?",
     ["Give equal attention to both parts.",
      "Developing economy: a high birth rate gives a high dependency ratio; discuss the link between population growth, dependency, saving, investment and growth.",
      "Developed economy: an ageing population with a falling birth rate; need for a workforce to support the growing number of older people.",
      "Level 4 (9 to 13) analyses both and decides how far the statement is true."],
     "Part 1: developing: dependency, saving, resources. Part 2: developed: ageing, pensions, labour shortage. Compare which is greater. Judge.",
     [[("k", "In a developing economy, a high birth rate gives a young population and a high dependency ratio."), ("n", "A large share of income may be spent on feeding and educating children, so saving and investment could be low, and rapid growth could put pressure on land, jobs and public services. Output per head may fall if capital does not grow as fast as the population.")],
      [("n", "In a developed economy, falling population and ageing mean fewer workers supporting more pensioners. This could raise taxes or debt, lower the labour force and slow growth, although productivity growth, higher retirement ages and immigration could offset this."), ("e", "The developed economy has more resources to adapt, whereas developing economies have fewer, so the problems of rapid growth may be at least as serious. Overall the statement is probably only partly true, depending on how quickly each economy adjusts.")]]),
  eq("Based on Oct/Nov 2022 · 9708/43 · Q6", "25 marks", "Developing economies have a high proportion of economically inactive people relative to the labour force (a high dependency ratio). This is the main reason why the standard of living is low in developing economies. Evaluate this statement.",
     ["Explain the dependency ratio and why it is high in developing economies (high birth rates, so many children).",
      "Link a high dependency ratio to low living standards: insufficient wealth creation per person, less tax revenue for public and merit goods, lower saving and investment.",
      "Evaluation: other factors also contribute: reliance on primary products, low investment, weak education and training, limited resources; living standards are hard to measure and GDP per head omits many factors. So it is hard to accept that the dependency ratio is the main reason."],
     "Define. Link to income and tax. Other causes. Measurement problems. Conclusion.",
     [[("k", "The dependency ratio compares the number of people who are too young or too old to work with those of working age. In developing economies it is often high because high birth rates give a large number of children."), ("n", "Each worker must then support more dependants, so income per head is lower and less is available for saving and investment. The government also collects less tax from a small working population, so it may have less to spend on health and education, which could keep productivity and living standards low.")],
      [("e", "However, dependency is probably not the only reason. Many developing economies rely on primary products with volatile prices, have low levels of capital and weak access to education and training. Living standards are also hard to measure, since GDP per head ignores many factors. So a high dependency ratio is likely to be one important cause, but not clearly the main one.")]])
  ],
  )

tips = tips_html(
  [("Define each measure.", "Birth rate and death rate are per 1,000 per year. Natural increase is the difference."),
   ("Know the dependency ratio formula.", "(Under 15 plus over 64) divided by (15 to 64), times 100."),
   ("Distinguish young and old dependency.", "Developing: mainly children. Developed: ageing, pensions and health costs."),
   ("Draw output per head against population.", "An inverted U with the optimum at the peak. Technology shifts it up and right."),
   ("Say that the optimum shifts.", "Capital, technology and productivity raise it. More births do not."),
   ("Give costs and benefits of urbanisation.", "Productivity and services against slums, congestion and pollution."),
   ("Judge, do not just describe.", "Population change is a problem only if output per head and structure are unfavourable.")],
  [("Natural increase", "Natural increase is the birth rate minus the death rate, which could be converted to a percentage by dividing by ten."),
   ("Dependency", "A high dependency ratio may mean that a larger share of income goes on supporting dependants, leaving less for investment."),
   ("Optimum", "The optimum population gives the highest output per head with given resources, capital and technology."),
   ("Ageing", "An ageing population could shrink the workforce and raise spending on pensions and health care."),
   ("Urbanisation", "Urbanisation may raise productivity but could also create congestion, slums and pollution.")],
  [CW["define"], CW["explain"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- Demographic transition ---------- */
const sm = (x) => { const k = Math.max(0, Math.min(1, x)); return k * k * (3 - 2 * k); }, bR = (t) => 40 - 28 * sm((t - 42) / 43), dR = (t) => 36 - 26 * sm((t - 12) / 33) + 1.5 * sm((t - 80) / 20);
const DX = (t) => 80 + t * 6.4, DY = (r) => 300 - r * 6.4;
function dtDraw(s) {
  let o = axes(70, 300, 730, 30, "Time as the economy develops", "Rate per 1,000 people"); [0, 10, 20, 30, 40].forEach((v) => (o += SV.text(64, DY(v) + 4, v, "sm", { "text-anchor": "end" })));
  const n = Math.min(100, s.p), bp = [], dp = []; for (let t = 0; t <= n; t += 2) { bp.push([DX(t), DY(bR(t))]); dp.push([DX(t), DY(dR(t))]); }
  if (bp.length > 1) { o += SV.poly([...bp, ...dp.slice().reverse()], "f1", op(0.28)) + SV.path(Lib.ptsPath(bp), "c2") + SV.path(Lib.ptsPath(dp), "c1"); }
  o += tag(DX(30), DY(40) - 8, "Birth rate", "t2", s.p > 0 ? 1 : 0, "middle") + tag(DX(60), DY(10) + 22, "Death rate", "t1", s.p > 0 ? 1 : 0, "middle");
  const stg = [["Stage 1: both rates high, stable population"], ["Stage 2: deaths fall, population surges"], ["Stage 3: births fall, growth slows"], ["Stage 4: both low, ageing population"]][n < 22 ? 0 : n < 52 ? 1 : n < 82 ? 2 : 3];
  if (s.p > 0) o += tag(400, 334, stg[0], "t4", 1, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Demographic transition: death rate falls first, then birth rate, leaving a gap of natural increase that widens then narrows">${dtDraw({ p: 100 })}</svg>`;
Lib.stepper($("#stD"), { w: 760, h: 345, label: "Demographic transition: birth and death rate over time, with the gap showing natural increase", base: { p: 0 }, draw: dtDraw, tween: 1600, dwell: 5800, steps: [
  { cap: "<b>Stage 1.</b> Birth and death rates are both high (about 40 and 36 per 1,000). The population is almost stable, with a young age structure.", s: { p: 10 } },
  { cap: "<b>Stage 2.</b> Better food, clean water and medicine cut the death rate, but the birth rate stays high. The gap (natural increase) widens and the population rises rapidly.", s: { p: 35 } },
  { cap: "<b>Stage 3.</b> Rising incomes, education, urbanisation and contraception pull the birth rate down. The gap narrows, so growth slows and the dependency ratio falls (the demographic dividend).", s: { p: 70 } },
  { cap: "<b>Stage 4.</b> Both rates are low. The population is stable or falling and ageing, so the old-age dependency ratio rises.", s: { p: 100 } },
] });

/* ---------- Optimum population ---------- */
const OX = (p) => 80 + p * 6.4, OY = (y) => 300 - y * 2.4;
const opt = (tt) => 50 + 15 * tt, hgt = (tt) => 70 + 30 * tt, oy = (p, tt) => Math.max(0, hgt(tt) * (1 - Math.pow((p - opt(tt)) / 72, 2)));
function optDraw(s) {
  let o = axes(70, 300, 730, 30, "Population", "Output per head");
  const pts0 = [], pts1 = []; for (let p = 0; p <= 100; p += 2) { pts0.push([OX(p), OY(oy(p, 0))]); pts1.push([OX(p), OY(oy(p, s.t))]); }
  if (s.t > 0) o += SV.path(Lib.ptsPath(pts0), "c3 dash", op(0.4));
  o += SV.path(Lib.ptsPath(pts1), "c1");
  const po = opt(s.t); o += SV.line(OX(po), OY(oy(po, s.t)), OX(po), 300, "c4 dash") + SV.circle(OX(po), OY(oy(po, s.t)), 7, "dot4") + tag(OX(po), 322, "optimum", "t4", 1, "middle");
  if (s.m > 0) { const p = s.m, y = oy(p, s.t); o += SV.circle(OX(p), OY(y), 7, "dot2") + tag(OX(p) + (p < po ? 12 : -12), OY(y) - 12, p < po ? "under-populated" : "over-populated", "t2", 1, p < po ? "start" : "end"); }
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Output per head against population: an inverted U with the optimum at the peak">${optDraw({ t: 0, m: 0 })}</svg>`;
Lib.stepper($("#stO"), { w: 760, h: 345, label: "Output per head against population: the optimum, under- and over-population and the effect of technology", base: { t: 0, m: 0 }, draw: optDraw, tween: 1300, dwell: 5800, steps: [
  { cap: "<b>The curve.</b> With given resources, capital and technology, output per head first rises as more workers allow specialisation and then falls as diminishing returns set in.", s: { t: 0, m: 0 } },
  { cap: "<b>Optimum population.</b> The peak of the curve is the population that maximises output (income) per head.", s: { t: 0, m: 0 } },
  { cap: "<b>Under-population.</b> At a smaller population, resources are not fully used and a larger population would raise output per head.", s: { t: 0, m: 22 } },
  { cap: "<b>Over-population.</b> Beyond the peak, extra people share the same resources, so output per head falls.", s: { t: 0, m: 88 } },
  { cap: "<b>New technology or capital</b> shifts the curve up and to the right: the optimum is higher and a larger population can now be supported.", s: { t: 1, m: 88 } },
] });

/* ---------- Lab 1 ---------- */
function labP() {
  if (!$("#br") || !$("#dr") || !$("#nm")) return;
  const b = +$("#br").value, d = +$("#dr").value, m = +$("#nm").value, ni = b - d, gr = (ni + m) / 10;
  $("#r1").textContent = ni + " per 1,000"; $("#r2").textContent = (gr >= 0 ? "+" : "") + Lib.fmtN(gr, 1) + "% a year"; $("#r3").textContent = gr > 0.05 ? Lib.fmtN(70 / gr, 0) + " yrs" : "none";
  $("#rv").textContent = `Natural increase is ${b} − ${d} = ${ni} per 1,000. Adding net migration of ${m} gives ${ni + m} per 1,000, a growth rate of ${Lib.fmtN(gr, 1)}% a year. ${gr > 0.05 ? "The population doubles in roughly " + Lib.fmtN(70 / gr, 0) + " years (rule of 70)." : gr < -0.05 ? "The population is shrinking." : "The population is roughly stable."}`;
  const Y = (v) => 150 - v * 3.2; let o = SV.line(40, 150, 400, 150) + SV.line(40, 20, 40, 280) + SV.text(46, 16, "per 1,000 people", "sm");
  [["Births", b, "f2"], ["Deaths", -d, "f1"], ["Net migration", m, "f1"], ["Growth", ni + m, "f3"]].forEach(([l, v, c], i) => { const x = 55 + i * 85, y = Y(Math.max(-40, Math.min(40, v))); o += SV.rect(x, Math.min(y, 150), 60, Math.abs(y - 150), c) + SV.text(x + 30, 296, l, "sm", { "text-anchor": "middle" }) + tag(x + 30, v >= 0 ? y - 6 : y + 16, Math.abs(v) + (v < 0 && l === "Deaths" ? "" : ""), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "br", label: "Birth rate per 1,000 ", min: 8, max: 45, step: 1, value: 30, fmt: (v) => v, onInput: labP });
Lib.slider($("#g2"), { id: "dr", label: "Death rate per 1,000 ", min: 4, max: 30, step: 1, value: 10, fmt: (v) => v, onInput: labP });
Lib.slider($("#g3"), { id: "nm", label: "Net migration per 1,000 ", min: -10, max: 15, step: 1, value: -2, fmt: (v) => v, onInput: labP });
labP();

/* ---------- Lab 2 ---------- */
function labD() {
  if (!$("#yg") || !$("#og")) return;
  let y = +$("#yg").value, o2 = +$("#og").value; if (y + o2 > 95) o2 = 95 - y; const w = 100 - y - o2, dep = (y + o2) / w * 100;
  $("#t1").textContent = w + "%"; $("#t2").textContent = Lib.fmtN(dep, 0); $("#t3").textContent = y >= 30 ? "Youthful" : o2 >= 15 ? "Ageing" : "Mature";
  $("#tv").textContent = `${y}% are under 15 and ${o2}% are over 64, so ${w}% are of working age. The dependency ratio is (${y} + ${o2}) ÷ ${w} × 100 = ${Lib.fmtN(dep, 0)}: each 100 workers support about ${Lib.fmtN(dep, 0)} dependants. ${y >= 30 ? "A young structure like this is typical of a developing economy: spending on children and education competes with investment." : o2 >= 15 ? "An ageing structure like this is typical of a developed economy: pensions and health care raise costs while the workforce shrinks." : "A mature structure with moderate numbers of both groups."}`;
  const X = (v) => 40 + v * 3.4; let o = SV.line(40, 200, 400, 200) + SV.text(40, 20, "Share of population (%)", "sm");
  [["Under 15", y, "f2"], ["15 to 64", w, "f1"], ["Over 64", o2, "f3"]].forEach(([l, v, c], i, arr) => { const x0 = arr.slice(0, i).reduce((a, q) => a + q[1], 0); o += SV.rect(X(x0), 120, v * 3.4, 80, c, op(0.7)) + SV.text(X(x0 + v / 2), 164, v + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(x0 + v / 2), 220 + (i % 2) * 18, l, "sm", { "text-anchor": "middle" }); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "yg", label: "Under 15 (% of population) ", min: 10, max: 50, step: 1, value: 35, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g5"), { id: "og", label: "Over 64 (% of population) ", min: 2, max: 30, step: 1, value: 5, fmt: (v) => v + "%", onInput: labD });
labD();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Does it tend to raise or lower the birth rate?", ["Raise", "Lower"],
  [("Children are needed to work on the family farm", 0), ("More girls complete secondary education", 1), ("Wider access to contraception", 1), ("High infant mortality", 0), ("Introduction of pensions for old age", 1), ("Rapid urbanisation, where housing costs are high", 1), ("A cultural preference for large families", 0), ("Higher incomes and better jobs for women", 1)],
  "Education, contraception, pensions and urban living lower the birth rate. Farm labour needs and high infant mortality raise it.") + MATCH([
  ["Natural increase", "Birth rate minus death rate"],
  ["Dependency ratio", "Under 15s plus over 64s as a percentage of those aged 15 to 64"],
  ["Optimum population", "The size that gives the highest income per head"],
  ["Infant mortality rate", "Deaths of babies under one year per 1,000 live births"],
  ["Net migration", "Immigration minus emigration"],
  ["Urbanisation", "The rising share of people living in cities"]]) + ORDER(
  "Put the stages of the demographic transition in order.",
  ["Both birth and death rates are high; population is stable", "The death rate falls; population grows quickly", "The birth rate falls; growth slows", "Both rates are low; population ageing"],
  "Death rates fall before birth rates.") + CALC([
  {"q": "The birth rate is 30 per 1,000 and the death rate is 10 per 1,000. Net migration is −2 per 1,000. Calculate the population growth rate (% a year).", "a": 1.8, "unit": "%", "tol": 0.05, "hint": "(30 − 10 − 2) ÷ 10.", "sol": "18 per 1,000 = <b>1.8%</b>."},
  {"q": "35% of a population are under 15 and 5% are over 64. Calculate the dependency ratio (1 decimal place).", "a": 66.7, "unit": "", "tol": 0.1, "hint": "(35 + 5) ÷ 60 × 100.", "sol": "40 ÷ 60 × 100 = <b>66.7</b>."},
  {"q": "There were 280 infant deaths among 10,000 live births. Calculate the infant mortality rate per 1,000 live births.", "a": 28, "unit": "per 1,000", "tol": 0.5, "hint": "280 ÷ 10,000 × 1,000.", "sol": "<b>28 per 1,000</b>."},
  {"q": "A country has 150 million people and 45 million of them live in cities. Calculate the urbanisation rate (%).", "a": 30, "unit": "%", "tol": 0.5, "hint": "45 ÷ 150.", "sol": "<b>30%</b>."}]) + MCQ([
  ("The dependency ratio is the number of:", ["Under 15s and over 64s per 100 people aged 15 to 64", "Workers per 100 people", "Unemployed per 100 workers", "Births per 1,000 people"], 0, "It shows how many dependants each 100 workers support."),
  ("Which would raise the optimum population?", ["Better technology", "A higher birth rate", "A fall in capital", "More emigration"], 0, "Technology raises output per head at every population size."),
  ("A typical developing economy has:", ["A high birth rate and a high dependency ratio", "An ageing population", "A very high life expectancy", "Falling urbanisation"], 0, "Large numbers of children raise the dependency ratio."),
  ("Net migration is equal to:", ["Immigration minus emigration", "Births minus deaths", "Emigration plus deaths", "Immigration plus births"], 0, "It is the net inflow of people."),
  ("Which is a cost of rapid urbanisation?", ["Pressure on housing, water and transport", "Smaller markets", "Lower productivity everywhere", "Higher birth rates"], 0, "Cities can be overwhelmed by rapid inflows.")
], "qz1") + CARDS([
  ("Natural increase", "Birth rate − death rate."),
  ("Net migration", "Immigrants − emigrants."),
  ("Dependency ratio", "(Under 15 + over 64) ÷ (15 to 64) × 100."),
  ("Demographic dividend", "A large working-age group with fewer dependants."),
  ("Optimum population", "Maximises income per head."),
  ("Under-population", "Too few people to use resources fully."),
  ("Over-population", "Diminishing returns reduce output per head."),
  ("Urbanisation", "Rising share of people in cities.")]) + MCQ(mc_exam)

build("sy1141", "population-growth-structure", "Population Growth, Structure and Urbanisation", EY,
  "11.4.1: measuring population change, the causes of changes in birth rate, death rate and migration, the dependency ratio, optimum population and urbanisation. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
