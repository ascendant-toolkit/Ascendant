"""AS syllabus 3.3.1-3.3.3 Income and wealth, measuring inequality, causes of inequality. Run: python3 tools/artifact-kit/mk_as36.py"""
from asx import *
EY = EYAS("3.3.1 to 3.3.3")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Income</b> is a <b>flow</b> of earnings over a period of time (wages, rent, interest, dividends, benefits), while <b class="kw">wealth</b> is a <b>stock</b> of assets owned at a point in time (property, savings, shares, pensions) minus debts, so wealth is usually spread <b>far more unequally</b> than income. Inequality is shown with a <b class="kw">Lorenz curve</b> and summarised by the <b class="kw">Gini coefficient</b>, which runs from <b>0 (perfect equality)</b> to <b>1 (one person has everything)</b>; its calculation is not required. Income inequality arises from differences in <b>employment, skills and education, occupation and sector, assets owned, discrimination, taxes and transfers</b>, and some economists argue that a degree of inequality <b>rewards effort and enterprise</b>, while others say large gaps waste talent and harm growth. Wealth is hard to measure because assets are varied, change in value, can be <b>hidden</b> or moved to family or tax havens.</p></div>

  <h2>1 · Income as a flow, wealth as a stock (3.3.1)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Income (flow)</th><th>Wealth (stock)</th></tr>
    <tr><td><b>Meaning</b></td><td>Money received over a period (a week, a year)</td><td>Value of assets owned at one moment, less debts</td></tr>
    <tr><td><b>Examples</b></td><td>Wages, profit, interest, rent, dividends, pensions, benefits</td><td>Property, savings, shares, pensions, valuables</td></tr>
    <tr><td><b>Relationship</b></td><td>Saved income adds to wealth</td><td>Wealth produces income (interest, rent)</td></tr>
    <tr><td><b>Distribution</b></td><td>Unequal</td><td>Usually more unequal than income</td></tr>
  </table></div>

  <h2>2 · Measuring inequality: Lorenz curve and Gini (3.3.2)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li>The <b>Lorenz curve</b> plots the <b>cumulative share of income</b> against the <b>cumulative share of the population</b>, from poorest to richest. The <b>45-degree line</b> is perfect equality; the further the curve bows below it, the greater the inequality.</li>
    <li><b>Gini coefficient = area between the line of equality and the Lorenz curve ÷ the area under the line of equality.</b> 0 = perfect equality, 1 = total inequality. (You do not need to calculate it.)</li>
    <li>A <b>fall</b> in the Gini coefficient, for example from 0.52 to 0.44, means income is more equally distributed.</li>
    <li><b>Limitations:</b> it is a single number so different Lorenz curves can have the same Gini; it ignores wealth, the black economy and non-money income; and definitions of income vary between countries.</li>
    <li><b>Difficulties measuring wealth:</b> it has <b>many forms</b> (housing, savings, pensions, financial assets) and countries measure differently; values <b>change</b> with house and share prices; some is <b>hidden</b> in tax havens or transferred to relatives.</li>
  </ul>

  <h2>3 · Causes of inequality (3.3.3)</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>How it widens income or wealth gaps</th></tr>
    <tr><td><b>Employment status</b></td><td>The unemployed or part-time workers earn far less than full-time workers</td></tr>
    <tr><td><b>Skills, education and experience</b></td><td>Higher skills bring higher pay; poor education and training limit access to well-paid jobs</td></tr>
    <tr><td><b>Occupation and sector</b></td><td>Pay differs between industries and between public and private sectors</td></tr>
    <tr><td><b>Ownership of assets and inheritance</b></td><td>Owners of property and shares earn rent, interest and dividends and pass on wealth</td></tr>
    <tr><td><b>Low saving</b></td><td>Poorer households save little and cannot buy assets, while property prices favour existing owners</td></tr>
    <tr><td><b>Discrimination and unequal opportunities</b></td><td>Gender, race or location can limit access to jobs and education</td></tr>
    <tr><td><b>Taxes and transfer payments</b></td><td>A regressive tax system or low benefits widen gaps; progressive taxes and benefits narrow them</td></tr>
    <tr><td><b>Low-income countries</b></td><td>Few employment opportunities, poor investment in education and health, and a large informal sector</td></tr>
  </table></div>
  <ul>
    <li><b>Can inequality benefit an economy?</b> It may <b>incentivise</b> effort, enterprise and retraining; but extreme inequality can <b>waste talent</b>, reduce spending power of the poor, and cause social tension.</li>
  </ul>

  <h2>4 · Worked examples</h2>
  <p><b>Reading a Lorenz curve.</b> Suppose the poorest 20% of households receive 5% of national income, the poorest 40% receive 15%, the poorest 60% receive 32% and the poorest 80% receive 55%. If incomes were equal, each 20% would receive 20%, 40%, 60% and 80%. The gaps between the equality line and the actual shares (15, 25, 28 and 25 percentage points) show how far the curve bows below the line.</p>
  <div class="tw"><table class="t">
    <tr><th>Share of households (poorest first)</th><th>Share of income if equal</th><th>Actual share</th><th>Gap</th></tr>
    <tr><td>Poorest 20%</td><td>20%</td><td>5%</td><td>15 points</td></tr>
    <tr><td>Poorest 40%</td><td>40%</td><td>15%</td><td>25 points</td></tr>
    <tr><td>Poorest 60%</td><td>60%</td><td>32%</td><td>28 points</td></tr>
    <tr><td>Poorest 80%</td><td>80%</td><td>55%</td><td>25 points</td></tr>
  </table></div>
  <p>The richest 20% therefore receive 45% of income (100% − 55%), over twice an equal share. If later data shows the poorest 40% now receive 20%, the Lorenz curve has moved closer to the line of equality and the Gini coefficient has fallen.</p>
  <p><b>Interpreting the Gini.</b> A fall in the Gini coefficient from 0.52 to 0.44 means that income is more equally distributed, so the Lorenz curve has moved closer to the line of equality. It does not say that people are better off in absolute terms, and it does not show who has gained or why.</p>

  <h2>5 · Why wealth is harder to measure than income</h2>
  <ul>
    <li><b>Many forms:</b> housing, savings, pensions, shares, business assets and valuables each need valuing in a different way.</li>
    <li><b>Values change:</b> house and share prices move, so wealth can rise or fall without any saving or spending.</li>
    <li><b>Hidden wealth:</b> assets may be held abroad, in tax havens, or transferred to relatives to avoid tax and detection.</li>
    <li><b>Informal ownership:</b> in many low-income countries land and property are not formally registered.</li>
    <li><b>Debts:</b> wealth should be net of debts, which are not always known.</li>
  </ul>

  <h2>6 · Two reasons for inequality in a low-income country: a worked comparison</h2>
  <ul>
    <li><b>Unequal access to education:</b> children from poor households leave school early, so they have few skills and earn low wages, while children from richer families gain qualifications and well-paid jobs. This is persistent because the gap passes to the next generation.</li>
    <li><b>Unequal ownership of land and assets:</b> owners earn rent and profit while landless workers rely on low wages or informal work. If most land is held by a few owners, income gaps are large.</li>
    <li><b>Which is stronger?</b> Education reforms act slowly, while land ownership is unequal immediately and fixed by history, so it may explain more of the current gap, but over time education may matter more for changes in inequality. Judge using the evidence given.</li>
  </ul>

  <h2>7 · Does inequality matter?</h2>
  <div class="tw"><table class="t">
    <tr><th>Case that some inequality is beneficial</th><th>Case that large inequality is harmful</th></tr>
    <tr><td>Rewards effort, skills and enterprise, so people have an incentive to work, train and take risks</td><td>Wastes talent when poorer people cannot afford education or health care</td></tr>
    <tr><td>Higher earners save and invest, which may raise growth</td><td>Poorer households spend most of their income, so low incomes limit demand</td></tr>
    <tr><td>Differences in pay move labour to where it is most needed</td><td>Can cause social tension, crime and political instability</td></tr>
    <tr><td></td><td>Poverty can reduce health, productivity and life chances</td></tr>
  </table></div>
  <ul>
    <li>The effect depends on the <b>size</b> of the gap, whether it comes from <b>effort or inheritance</b>, and whether there is <b>social mobility</b>.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Give <b>two</b> developed reasons for inequality, not a list. For measurement, define the Gini (0 to 1) and say what a change means. For wealth, explain <b>why</b> it is harder to measure than income.</div>
'''

watch = '''
  <h2>1 · The bath: income flows, wealth is the stock</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stF"></div>
  <h2>2 · Building a Lorenz curve</h2>
  <div id="stL"></div>
'''

explore = '''
  <h2>Lab 1 · Redistribute income</h2>
  <p>Start with an unequal economy and move income towards equality. Watch the Lorenz curve and the Gini coefficient.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div>
    <div class="readout"><div><small>Poorest 20% share</small><strong id="r1"></strong></div><div><small>Richest 20% share</small><strong id="r2"></strong></div><div><small>Gini coefficient</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="A Lorenz curve against the line of equality"></svg></div></div></div>

  <h2>Lab 2 · Compare countries</h2>
  <p>Choose a country to see its Gini coefficient on the scale from perfect equality to complete inequality. The figures are approximate and for illustration only.</p>
  <div class="card"><div class="grid2"><div><div id="cB" class="btnrow"></div>
    <div class="readout"><div><small>Country</small><strong id="t1"></strong></div><div><small>Gini coefficient</small><strong id="t2"></strong></div><div><small>Reading</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 200" role="img" aria-label="A scale from zero to one with the chosen country's Gini marked"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Income or wealth?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the Gini calculation steps in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A teacher and a landlord", "A teacher earns a salary (income, a flow). A landlord owns several flats (wealth, a stock) and earns rent from them (income). The landlord's wealth also grows if property prices rise, which helps explain why wealth is more unequal than income.", "income as a flow and wealth as a stock, and how they feed each other.") +
rw("A falling Gini coefficient", "A country's Gini falls from 0.52 to 0.44 after it expands education and benefits. Income is now more equally spread, though the country is still far from perfect equality, which would be zero.", "reading a change in the Gini.") +
rw("Hidden wealth", "Rich individuals may hold assets through trusts or overseas accounts, and families may transfer property to relatives. Official surveys therefore understate the wealth of the top few percent.", "why wealth is hard to measure.") +
rw("Skills and pay", "A surgeon trains for many years and earns much more than an unskilled worker. This reflects differences in skills, scarcity and the cost of training. Poor schools in some regions limit access to these careers.", "skills, education and occupation as causes of inequality.") +
rw("A fall in the Gini coefficient", "A country's Gini coefficient falls from 0.52 to 0.44 over five years. Income is more equally distributed, though average incomes might still be low and the gap between the richest and poorest may remain large.", "interpreting a change in the Gini coefficient.") +
rw("Hidden wealth", "Some wealthy households hold assets in overseas accounts or in family members' names. Official wealth statistics therefore understate the wealth of the richest and make wealth inequality hard to measure.", "why wealth is difficult to measure.")
)

mc_exam = [
  mcq("m23_12", 14, "The table shows Gini coefficients for income and wealth in two countries: country P income 0.6, wealth 0.4; country Q income 0.5, wealth 0.7. Which statement is correct?", ["Gini coefficients are not comparable between income and wealth because one is a flow concept and the other is a stock concept", "Income inequality is greater in country P than in country Q", "Wealth inequality is greater in country P than in country Q", "Wealth inequality is greater than income inequality in both countries"], 1, "A higher Gini means more inequality: income Gini is 0.6 in P and 0.5 in Q. Wealth inequality is greater in Q."),
  mcq("m25_12", 15, "The table shows the Gini coefficient for income: Costa Rica 0.479, 0.478 and 0.497 (2018, 2019, 2020); New Zealand 0.330, 0.326 and 0.320; Sweden 0.275, 0.280 and 0.278. What can be concluded from this data?", ["All three countries have seen an overall improvement in income equality", "Costa Rica has the highest level of consumer income of all three countries", "New Zealand's income inequality worsened between 2018 and 2020", "Sweden's economy has the highest income equality of all three countries"], 3, "Sweden's Gini is lowest, so income is most equally distributed there. Costa Rica's Gini rose, and New Zealand's fell."),
  mcq("s23_11", 16, "The table shows the income and wealth of Yasmin: children's welfare benefits $1,000, dividends from shares $1,000, property owned $40,000, savings in bank $1,000, shares $2,000, wages $10,000. What is the value of Yasmin's wealth?", ["$41,000", "$43,000", "$44,000", "$45,000"], 1, "Wealth is the stock of assets: property 40,000 + savings 1,000 + shares 2,000. Benefits, dividends and wages are income."),
  mcq("m21_12", 4, "Which statement is a positive statement?", ["The distribution of income and wealth in most western European countries is unequal", "The government ought to increase income tax on high earners", "There should be more legal rights given to workers to protect their status in the workplace", "Wages of those on low incomes should be increased"], 0, "Only the first can be tested against facts. The others contain value judgements such as ought and should.")
]

exam = exam_page("income, wealth and inequality",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Inequality appears as an 8 mark Paper 2 part most years (Gini coefficient, reasons for inequality, measuring wealth) and as short data-response parts. Reworded past questions are below, with four Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "3", "May/June 2024 (22) Q2(a); Oct/Nov 2024 (23) Q3(a); Feb/March 2023 (22) Q3(a)"), ("Data response, 2 marks", "1", "Oct/Nov 2024 (22) Q1(c)"), ("Multiple choice (Paper 1)", "4 shown below", "2020 to 2025")],
  [
  eq(P("s24_22", "2(a)"), "8 marks", "Explain how the Gini coefficient is used to measure income inequality and consider the relative strength of two economic reasons suggested for such inequality in a low-income country.",
     ["Knowledge (up to 3): the Gini coefficient is a numerical measure of the extent of income inequality (1); zero means no inequality and one means all income earned by one person (1); the nearer to zero the more equal, the nearer to one the more unequal (1).",
      "Analysis (up to 3): reasons may include a lack of employment opportunities, because industry is less developed; poor vocational training, because of a lack of finance; or a lack of investment in education and health, which lowers potential incomes (each explained, with why it may be more of a problem in a low-income country).",
      "Evaluation (up to 2): a judgement on the relative strength of the two reasons."],
     "Gini: 0 to 1, what each end means. Two reasons for a low-income country, explained. Compare their strength.",
     [[("k", "The Gini coefficient is a number between zero and one that measures income inequality. Zero means perfect equality, with everyone earning the same, and one means one person earns all the income, so the closer to one, the more unequal the distribution.")], [("n", "In a low-income country a lack of employment opportunities may be a major cause of inequality, because industry is poorly developed and many people have no formal job. Poor education and health spending is another: those who cannot afford schooling stay in low-paid work, while a few with qualifications earn much more.")], [("e", "Of the two, a lack of education investment is probably the stronger long-term cause, since it keeps incomes low across generations, while a lack of jobs might ease if the economy grows. Both matter, and they reinforce each other.")]]),
  eq(P("w24_23", "3(a)"), "8 marks", "Explain two economic reasons for inequality in the distribution of income and wealth and consider why inequality in the distribution of wealth cannot easily be measured.",
     ["Knowledge (up to 3): inequality means an uneven distribution of income and wealth among a population (1); two reasons explained, for example poor education and training, leading to fewer marketable skills (1) and low saving, making it harder to buy property, with rising property prices benefiting existing owners (1).",
      "Analysis (up to 3): why wealth is hard to measure, for example because it has many sources such as housing, savings, financial instruments and pensions, measured differently in different countries (1); some may be hidden in tax havens (1); ownership may be transferred to family members (1).",
      "Evaluation (up to 2): a judgement about how difficult measurement really is."],
     "Define inequality. Two reasons explained. Why wealth is hard to measure: many forms, hidden, transferred.",
     [[("k", "Inequality means income and wealth are unevenly shared across the population. One reason is education and training: people with fewer marketable skills cannot apply for well-paid jobs. A second is low saving: poorer households cannot save enough to buy property, while rising property prices benefit existing owners, so wealth gaps widen.")], [("n", "Wealth is hard to measure because it takes many forms, such as housing, savings, shares and pensions, which different countries count differently and whose values change. Wealthy individuals may also hold assets in tax havens or transfer ownership to relatives, so some wealth is never recorded.")], [("e", "Measurement is therefore less reliable for wealth than for income, which is mainly recorded through tax and payroll. Surveys can still give a rough guide, but they probably understate the wealth of the richest.")]]),
  eq(P("m23_22", "3(a)"), "8 marks", "Explain the possible economic reasons for inequality of income and consider whether inequality of income can benefit an economy.",
     ["Knowledge (up to 3): a clear understanding of at least two reasons for inequality of income, such as whether a person is employed or unemployed (1), skills, qualifications and experience across occupations (1), public or private sector employment (1), full-time or part-time work (1), transfer payments (1) and the level and type of taxation (1). Two reasons well explained earn up to 3.",
      "Analysis (up to 3): the focus is on whether inequality generates benefits, for example incentivising workers and raising productivity, encouraging enterprise and encouraging workers to retrain or reskill.",
      "Evaluation (up to 2): a judgement on whether income inequality can benefit an economy."],
     "Two reasons explained. Benefits: incentives, enterprise, retraining. Judge: some inequality may help, extreme inequality does not.",
     [[("k", "Income inequality may result from differences in skills and qualifications, because highly qualified workers in skilled occupations earn more, and from whether people are in work at all, since the unemployed receive far less than the employed. Differences in taxation and transfer payments also change the gap.")], [("n", "Some inequality may benefit an economy because higher pay rewards effort and productivity, encourages enterprise and gives workers a reason to retrain or gain new skills.")], [("e", "However, a very large gap could waste talent, since poorer people may be unable to afford education, and reduce spending power. So a moderate amount of inequality may help, but not an extreme level.")]]),
  eq(P("w24_22", "1(c)"), "2 marks", "A country's Gini coefficient falls from 0.52 to 0.44 over five years. Explain what is meant by this fall.",
     ["1 mark for an accurate definition, for example that the Gini coefficient measures income inequality (1).", "1 mark for explaining that the fall means that income is more equally distributed (1). Maximum 2."],
     "Define the Gini coefficient. A fall means income is more equally distributed.",
     [[("k", "The Gini coefficient is a measure of income inequality between zero and one. A fall from 0.52 to 0.44 means that income has become more equally distributed, although some inequality remains.")]])
  ],
  )

tips = tips_html(
  [("Flow versus stock.", "Income is a flow per period; wealth is a stock at a point in time."),
   ("Gini runs from 0 to 1.", "0 = equality, 1 = one person has it all."),
   ("A fall means more equal.", "A rise means more unequal."),
   ("Explain, don't list, reasons.", "Two developed reasons beat five short ones."),
   ("Link causes to skills, assets, tax.", "Employment, education, ownership, discrimination."),
   ("Explain wealth measurement problems.", "Many forms, values change, hidden or transferred."),
   ("Evaluate incentives.", "Some inequality rewards effort; extreme inequality wastes talent.")],
  [("Income", "Income is a flow of earnings over a period of time."),
   ("Wealth", "Wealth is a stock of assets owned at a point in time."),
   ("Gini coefficient", "The Gini coefficient measures income inequality on a scale of zero to one."),
   ("Lorenz curve", "A Lorenz curve that bows further from the line of equality shows greater inequality."),
   ("Cause", "Poor education and training may limit people to low-paid work.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = '''
/* ---------- bath ---------- */
function bathDraw(s) {
  let o = SV.rect(260, 70, 240, 180, "f1", op(0.15)) + SV.line(260, 70, 260, 250) + SV.line(500, 70, 500, 250) + SV.line(260, 250, 500, 250);
  const h = Math.min(180, s.w * 1.8); o += SV.rect(261, 250 - h, 238, h, "f2", op(0.6));
  o += SV.text(380, 62, "Wealth (stock): the level of water", "lbl bd", { "text-anchor": "middle" });
  if (s.i > 0) o += SV.line(90, 100, 255, 100, "c2", { "stroke-width": 4, ...op(s.i) }) + SV.arrowHead(258, 100, "r", "dot2") + SV.text(90, 88, "Income (flow) per year", "lbl bd", { ...op(s.i) });
  if (s.o > 0) o += SV.line(505, 200, 690, 200, "c3", { "stroke-width": 4, ...op(s.o) }) + SV.arrowHead(692, 200, "r", "dot3") + SV.text(520, 188, "Spending (flow out)", "lbl bd", { ...op(s.o) });
  if (s.w > 0) o += SV.text(380, 280, "Saved income adds to wealth", "sm", { "text-anchor": "middle", ...op(s.w > 40 ? 1 : 0) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Income flows into a tank of wealth and spending flows out">${bathDraw({ w: 60, i: 1, o: 1 })}</svg>`;
Lib.stepper($("#stF"), { w: 760, h: 300, label: "Income as a flow into the stock of wealth", base: { w: 0, i: 0, o: 0 }, draw: bathDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Wealth is a stock.</b> It is the amount of assets owned at one moment, like the water level in a bath. It starts low.", s: { w: 10, i: 0, o: 0 } },
  { cap: "<b>Income is a flow.</b> Wages, rent and interest flow in over time, measured per week or per year.", s: { w: 10, i: 1, o: 0 } },
  { cap: "<b>Spending is a flow out.</b> What is not spent is saved and builds up as wealth.", s: { w: 40, i: 1, o: 1 } },
  { cap: "<b>The stock rises</b> when saving is positive. Households with high income can save more, which is why wealth is usually more unequal than income.", s: { w: 80, i: 1, o: 1 } },
] });

/* ---------- Lorenz ---------- */
const BASE = [4, 8, 12, 20, 56];
const shares = (w) => BASE.map((b) => (1 - w) * b + w * 20);
const cum = (sh) => { let c = 0; return [0, ...sh.map((v) => (c += v))]; };
const gini = (sh) => { const c = cum(sh); let a = 0; for (let i = 1; i < c.length; i++) a += ((c[i - 1] + c[i]) / 2) * 20; return 1 - a / 5000; };
function lorenz(x0, y0, w, h, sh, k = 1, showA = true) {
  const c = cum(sh), X = (p) => x0 + (p / 100) * w, Y = (v) => y0 - (v / 100) * h;
  let o = SV.line(x0, y0, x0 + w, y0) + SV.line(x0, y0, x0, y0 - h) + SV.text(x0 + w, y0 + 22, "Cumulative % of population", "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y0 - h - 6, "Cumulative % of income", "sm");
  o += SV.line(X(0), Y(0), X(100), Y(100), "dash") + SV.text(X(62), Y(66), "Line of equality", "sm");
  const pts = c.map((v, i) => [X(i * 20), Y(v)]);
  if (showA) o += SV.poly([[X(0), Y(0)], [X(100), Y(100)], ...pts.slice(1, 5).reverse()], "f3", op(0.4 * k));
  o += SV.path("M" + pts.map((p) => p.join(",")).join(" L"), "c2", { fill: "none", "stroke-width": 3, ...op(k) });
  pts.forEach((p) => (o += SV.circle(p[0], p[1], 4, "dot2", op(k))));
  return o;
}
function lzDraw(s) {
  let o = lorenz(120, 250, 300, 200, BASE, s.c, s.a > 0.5);
  if (s.a > 0.5) o += SV.text(440, 120, "A", "lbl bd", { ...halo }) + SV.text(440, 140, "area between the line", "sm") + SV.text(440, 156, "and the Lorenz curve", "sm");
  if (s.f > 0) { const g = gini(BASE); o += SV.text(440, 200, "Gini = A ÷ (A + B)", "lbl bd", op(s.f)) + SV.text(440, 222, "= " + Lib.fmtN(g, 2), "lbl bd", { style: "fill:var(--accent)", ...op(s.f) }); }
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A Lorenz curve below the line of equality with the area between them shaded">${lzDraw({ c: 1, a: 1, f: 1 })}</svg>`;
Lib.stepper($("#stL"), { w: 760, h: 300, label: "Building a Lorenz curve and reading the Gini coefficient", base: { c: 0, a: 0, f: 0 }, draw: lzDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The line of equality.</b> If every 20% of the population earned 20% of income, the Lorenz curve would be this diagonal line.", s: { c: 0, a: 0, f: 0 } },
  { cap: "<b>The Lorenz curve.</b> Here the poorest 20% earn 4% of income, the next 20% earn 8%, then 12%, 20% and the richest 20% earn 56%. The curve bows below the line.", s: { c: 1, a: 0, f: 0 } },
  { cap: "<b>The area A</b> between the line and the curve measures inequality. The bigger it is, the greater the inequality.", s: { c: 1, a: 1, f: 0 } },
  { cap: "<b>The Gini coefficient</b> is the area A as a share of the whole triangle under the line of equality (A + B). It runs from 0 to 1.", s: { c: 1, a: 1, f: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labL() {
  if (!$("#rd")) return;
  const w = +$("#rd").value / 100, sh = shares(w), g = gini(sh);
  $("#r1").textContent = Lib.fmtN(sh[0], 1) + "%"; $("#r2").textContent = Lib.fmtN(sh[4], 1) + "%"; $("#r3").textContent = Lib.fmtN(g, 2);
  $("#rv").textContent = w === 0 ? `Before redistribution the richest 20% receive ${Lib.fmtN(sh[4], 0)}% of income and the poorest 20% only ${Lib.fmtN(sh[0], 0)}%, a Gini of ${Lib.fmtN(g, 2)}.` : `After moving ${Lib.fmtN(w * 100, 0)}% of the way to equality, the poorest 20% have ${Lib.fmtN(sh[0], 1)}% and the richest 20% have ${Lib.fmtN(sh[4], 1)}%. The Lorenz curve moves towards the line of equality and the Gini falls to ${Lib.fmtN(g, 2)}.${w === 1 ? " At full equality the Gini is zero." : ""}`;
  $("#labA").innerHTML = lorenz(60, 250, 320, 210, sh, 1, true);
}
Lib.slider($("#g1"), { id: "rd", label: "How far income is moved towards equality, % ", min: 0, max: 100, step: 10, value: 0, fmt: (v) => v + "%", onInput: labL });
labL();

/* ---------- Lab 2 ---------- */
const CT = [["Sweden", 0.28], ["Germany", 0.31], ["United Kingdom", 0.35], ["United States", 0.41], ["Brazil", 0.53], ["South Africa", 0.63]];
function showC(i) {
  const [n, g] = CT[i]; $$("#cB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = n; $("#t2").textContent = g.toFixed(2); $("#t3").textContent = g < 0.3 ? "Fairly equal" : g < 0.4 ? "Moderate" : g < 0.5 ? "High" : "Very high";
  $("#tv").textContent = `${n} has a Gini coefficient of about ${g.toFixed(2)}. ${g < 0.35 ? "Income is spread comparatively evenly." : g < 0.5 ? "There is a sizeable gap between rich and poor." : "A large share of income goes to the richest households."} A Gini of 0 would mean perfect equality and 1 would mean one person receives everything.`;
  const X = (v) => 30 + v * 360; let o = SV.line(30, 110, 390, 110) + [0, 0.2, 0.4, 0.6, 0.8, 1].map((v) => SV.line(X(v), 104, X(v), 116) + SV.text(X(v), 134, v.toFixed(1), "sm", { "text-anchor": "middle" })).join("");
  CT.forEach(([m, v], k) => (o += SV.circle(X(v), 110, k === i ? 9 : 5, k === i ? "dot3" : "dot1", op(k === i ? 1 : 0.5))));
  o += SV.text(X(g), 88, n + " " + g.toFixed(2), "lbl bd", { "text-anchor": "middle", ...halo }) + SV.text(30, 170, "Equality (0)", "sm") + SV.text(390, 170, "Total inequality (1)", "sm", { "text-anchor": "end" });
  $("#labB").innerHTML = o;
}
$("#cB").innerHTML = CT.map((c, i) => `<button class="b" data-i="${i}">${c[0]}</button>`).join("");
$$("#cB button").forEach((b) => (b.onclick = () => showC(+b.dataset.i)));
showC(0);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Is it income or wealth?", ["Income (flow)", "Wealth (stock)"],
  [("A monthly salary", 0), ("A house owned outright", 1), ("Dividends paid on shares", 0), ("Shares held in a company", 1), ("Interest earned this year", 0), ("Savings in a bank account", 1), ("Rent received each month", 0), ("A pension fund", 1)],
  "Income is a flow over time. Wealth is a stock of assets at a point in time.") + MATCH([
  ["Lorenz curve", "Plots cumulative income share against cumulative population share"],
  ["Gini coefficient", "A measure of inequality from 0 to 1"],
  ["Gini of 0", "Perfect equality"],
  ["Gini of 1", "One person has all the income"],
  ["Wealth", "A stock of assets less debts"],
  ["Income", "A flow of earnings over a period"]]) + ORDER(
  "Put the steps of reading the Gini coefficient in order.",
  ["Plot the cumulative share of population against the cumulative share of income", "Draw the line of equality", "Find the area between the line and the Lorenz curve", "Divide it by the whole area under the line of equality", "Read the Gini coefficient between 0 and 1"],
  "Gini = area between the curves ÷ the area under the line of equality.") + CALC([
  {"q": "A person owns property worth $60,000, savings of $4,000, shares of $6,000 and has debts of $20,000. What is their wealth ($)?", "a": 50000, "unit": "$", "tol": 1, "hint": "Assets minus debts.", "sol": "70,000 − 20,000 = <b>$50,000</b>."},
  {"q": "A country's Gini coefficient falls from 0.52 to 0.44. By how many points has it fallen?", "a": 0.08, "unit": "", "tol": 0.005, "hint": "0.52 − 0.44.", "sol": "<b>0.08</b>."},
  {"q": "The richest 20% earn 56% of income. How many times the share of the poorest 20% (4%) is this?", "a": 14, "unit": "times", "tol": 0.2, "hint": "56 ÷ 4.", "sol": "<b>14 times</b>."},
  {"q": "A worker earns $2,000 a month and spends $1,800. By how much does the worker's wealth rise in a year if the saving is all kept ($)?", "a": 2400, "unit": "$", "tol": 1, "hint": "(2,000 − 1,800) × 12.", "sol": "<b>$2,400</b>."}]) + MCQ([
  ("Income is best described as:", ["A flow", "A stock", "An asset", "A debt"], 0, "It is measured per period."),
  ("A Gini coefficient close to 1 means:", ["Great inequality", "Perfect equality", "Zero inflation", "Low unemployment"], 0, "One person has nearly everything."),
  ("A Lorenz curve bowing further from the line of equality shows:", ["More inequality", "Less inequality", "No change", "A higher income"], 0, "A bigger area A."),
  ("Which is a stock?", ["Savings in a bank", "Monthly wages", "Annual dividends", "Weekly rent"], 0, "Assets owned at a point in time."),
  ("Wealth is hard to measure partly because:", ["Some is hidden or held overseas", "It is always in cash", "It is the same as income", "Governments record every asset"], 0, "Tax havens and transfers.")
], "qz1") + CARDS([
  ("Income", "Flow per period."),
  ("Wealth", "Stock of assets less debts."),
  ("Lorenz curve", "Cumulative income against population."),
  ("Gini", "0 equality, 1 total inequality."),
  ("Cause", "Skills, assets, employment."),
  ("Benefit", "Incentives and enterprise."),
  ("Cost", "Wasted talent."),
  ("Measuring wealth", "Many forms, hidden, transferred.")]) + MCQ(mc_exam)

build("as36", "as-income-wealth-inequality", "Income, Wealth and Inequality", EY,
  "3.3.1 to 3.3.3: income as a flow and wealth as a stock, measuring inequality with the Lorenz curve and Gini coefficient, and the economic reasons for inequality. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
