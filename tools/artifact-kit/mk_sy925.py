"""Syllabus 9.2.5 Inclusive economic growth (chapter 42). Run: python3 tools/artifact-kit/mk_sy925.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.2.5"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Inclusive economic growth</b> is growth whose benefits are <b>widely shared</b> across households, regions and groups, and which gives everyone the chance to take part in it, rather than growth that mainly raises incomes at the top. Growth can reduce <b>absolute poverty</b> and still widen <b>inequality</b>, so rising GDP alone does not show that growth is inclusive. The <b>Kuznets curve</b> suggests inequality first rises then falls as income per head rises, but this is a tendency, not a law. Governments can promote inclusion through <b>fiscal policy</b> (progressive taxes and transfers) and <b>supply-side policy</b> (education, training, infrastructure, access to finance).</p></div>

  <h2>1 · What inclusive growth means</h2>
  <ul>
    <li><b>Who gains:</b> poorer households as well as richer ones; the bottom 40% see their incomes rise at least as fast as the average.</li>
    <li><b>Who takes part:</b> access to jobs, schooling, healthcare, credit and infrastructure for women, rural and poorer regions, and small firms.</li>
    <li><b>Outcomes and opportunities:</b> both a fairer spread of incomes and fairer chances.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Equality</b></td><td>People have equal shares of income or wealth</td><td>A Gini coefficient close to 0</td></tr>
    <tr><td><b>Equity</b></td><td>A fair distribution, which need not be equal; may reflect effort, need or opportunity</td><td>Higher taxes on high earners to fund benefits for the poor</td></tr>
    <tr><td><b>Absolute poverty</b></td><td>Income below a fixed minimum needed for basic needs</td><td>Living on less than $2.15 a day</td></tr>
    <tr><td><b>Relative poverty</b></td><td>Income well below the average in that country</td><td>Below 60% of median income</td></tr>
  </table></div>

  <h2>2 · The impact of growth on equity and equality</h2>
  <div class="grid2">
    <div class="card"><h3>Growth can narrow inequality when…</h3><ul>
      <li>It creates many jobs for low-skilled workers, so unemployment falls.</li>
      <li>Tax revenue rises and funds education, healthcare and benefits.</li>
      <li>Wages at the bottom rise faster than at the top (tight labour markets).</li>
      <li>Rural and poorer regions share in the gains (trickle-down).</li>
    </ul></div>
    <div class="card"><h3>Growth can widen inequality when…</h3><ul>
      <li>Gains go mainly to owners of capital, land and scarce skills.</li>
      <li>Technology raises the pay of skilled workers but replaces routine jobs.</li>
      <li>Growth is concentrated in cities, sectors or regions.</li>
      <li>Poor access to education and credit stops poor households sharing in it.</li>
    </ul></div>
  </div>
  <div id="pic1" class="card"></div>
  <div class="tip"><b class="h">The Gini coefficient</b>On a Lorenz curve, <b>Gini = A ÷ (A + B)</b>, where A is the area between the line of perfect equality and the Lorenz curve, and B is the area under the Lorenz curve. It runs from <b>0</b> (perfect equality) to <b>1</b> (one person has everything). A rise in the Gini coefficient means growth has become less inclusive.</div>
  <h3>The Kuznets curve</h3>
  <p>Simon Kuznets suggested an <b>inverted U</b> between income per head and inequality. At low incomes most people are poor and equal. As an economy industrialises, some move to higher-paid jobs first, so inequality <b>rises</b>. At higher incomes, education, urbanisation and welfare systems spread the gains, and inequality <b>falls</b>. Evaluate: the evidence is mixed, many rich countries have seen inequality rise since the 1980s, and policy choices matter more than the stage of development.</p>

  <h2>3 · Policies to promote inclusive growth</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>How it promotes inclusion</th><th>Possible drawback</th></tr>
    <tr><td><b>Progressive income tax and transfers</b> (fiscal)</td><td>Redistributes from high to low incomes, funds benefits</td><td>May reduce incentives to work and invest, cost to the budget</td></tr>
    <tr><td><b>Spending on education, training and healthcare</b> (supply-side)</td><td>Raises the skills and earning power of poorer households, equal opportunity</td><td>Slow, costly, quality varies</td></tr>
    <tr><td><b>Infrastructure for poorer regions</b></td><td>Links remote areas to jobs and markets</td><td>High cost, benefits take years</td></tr>
    <tr><td><b>Minimum wage and labour rights</b></td><td>Raises pay at the bottom</td><td>May reduce jobs if set too high</td></tr>
    <tr><td><b>Access to finance and support for small firms</b></td><td>Lets poorer people start businesses</td><td>Risk of defaults, targeting is hard</td></tr>
    <tr><td><b>Anti-discrimination laws and equal access</b></td><td>Widens participation by women and minorities</td><td>Enforcement is difficult</td></tr>
  </table></div>
  <div class="tip"><b class="h">Evaluation: the equity-efficiency trade-off</b>High marginal tax rates and generous benefits may reduce the incentive to work, save and invest, and so slow growth. But better education and health can raise growth as well as equity, so the trade-off is not always sharp. Also judge <b>targeting</b> (do benefits reach those who need them?), <b>time lags</b> and <b>cost</b>.</div>
'''

watch = '''
  <h2>1 · Growth that does and does not share the gains</h2>
  <p>The Lorenz curve shows how far income is from being shared equally. Press Play, or click the numbered steps.</p>
  <div id="stL"></div>
  <h2>2 · The Kuznets curve</h2>
  <div id="stK"></div>
'''

explore = '''
  <h2>Lab 1 · Who gains from growth?</h2>
  <p>Average income grows. Choose how much of the extra income goes to the poorest 40% and to the richest 10%. See whether growth is inclusive.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Bottom 40% income growth</small><strong id="r1"></strong></div><div><small>Top 10% income growth</small><strong id="r2"></strong></div><div><small>Bottom 40% share of income</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars showing income growth for the bottom 40 percent, middle 50 percent and top 10 percent compared with the average"></svg></div></div></div>

  <h2>Lab 2 · Policy profile</h2>
  <p>Pick a policy to see how it promotes inclusion and what weakens it.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Does it make growth more inclusive or less?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the Kuznets curve story in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("China and India: growth with rising inequality", "Both countries grew very fast for decades and lifted hundreds of millions of people out of absolute poverty. At the same time, the gap between urban and rural areas and between top and bottom incomes widened.", "growth can cut absolute poverty and still raise inequality. Use it to show why GDP alone does not measure inclusion.") +
rw("Scandinavian welfare systems", "Countries such as Denmark and Norway combine high income per head with high progressive taxes, generous benefits and heavy investment in education. Gini coefficients are among the lowest in the world.", "fiscal policy and supply-side policy together promoting inclusion. Evaluate with the cost to taxpayers and whether it can be copied elsewhere.") +
rw("Mobile banking in Kenya", "Mobile money services let people without bank accounts send payments and save safely. This opened financial services to poorer households and small traders.", "improving access to finance as a way of widening participation. Evaluate with limits such as phone access and fees.") +
rw("Skills-biased technology", "Software and automation raised the pay of workers with advanced skills while reducing demand for routine clerical and factory jobs in many rich economies.", "a reason growth may widen inequality. Link to retraining and education as the policy response.")
)

mc_exam = [
  ("What does the Kuznets curve show? (May/June 2022 · 31 · Q20, reworded)", ["A rise then fall in the balance of trade deficit after a devaluation", "A rise then fall in the economic growth rate as GDP rises", "A rise then fall in inequality as income per head rises", "A rise then fall in tax revenue as the tax rate rises"], 2, "Kuznets proposed an inverted U between income per head and inequality."),
  ("The turning point on the Kuznets curve is estimated at about $10,500 of income per head. For a country with $8,000 per head, what is most likely? (Oct/Nov 2023 · 31 · Q30, reworded)", ["A fall in income per head would have no effect on inequality", "A fall in income per head would increase inequality", "A rise in income per head would have no effect on inequality", "A rise in income per head would increase inequality"], 3, "To the left of the turning point, growth is on the rising part of the inverted U, so inequality tends to rise."),
  ("On a Lorenz diagram area X lies between the line of perfect equality and the Lorenz curve, and Y lies under the curve. How is the Gini coefficient calculated? (May/June 2023 · 31 · Q30, reworded)", ["X ÷ (X + Y)", "(X + Y) ÷ X", "(X + Y) ÷ Y", "Y ÷ (X + Y)"], 0, "Gini is the area between the curves as a share of the whole triangle under the line of equality."),
  ("Which change in the Gini coefficient suggests a country is distributing income more equally? (Oct/Nov 2023 · 32 · Q27, reworded)", ["A move closer to 1", "A move closer to 0", "A move from negative to positive", "A move from positive to negative"], 1, "A Gini of 0 means perfect equality, so a fall means more equal."),
  ("Which fiscal changes would be most effective in reducing income inequality? (Oct/Nov 2023 · 32 · Q13, reworded)", ["Raise top income tax, raise indirect taxes, cut state benefits", "Raise top income tax, cut indirect taxes, raise state benefits", "Cut top income tax, raise indirect taxes, cut state benefits", "Cut top income tax, cut indirect taxes, cut state benefits"], 1, "Progressive direct taxes and higher benefits redistribute towards the poor, and lower indirect taxes reduce the burden on the poor."),
  ("Which policy could reduce income inequality in the short run in a country with high inequality? (Oct/Nov 2024 · 32 · Q15, reworded)", ["A higher sales tax on luxury goods", "A minimum wage", "Heavy investment in schools", "Skills and productivity training to stimulate growth"], 1, "A minimum wage lifts low pay straight away. Education and training work over many years."),
  ("What is likely to cause a more equal distribution of income in the long run? (May/June 2023 · 32 · Q15, reworded)", ["A cut in the top rate of tax", "More government spending on education and training", "A rise in unemployment", "Privatising the education sector"], 1, "Better skills raise the earning power of poorer households over time.")
]

exam = exam_page("inclusive growth, inequality and equity",
  "Inclusive growth was added in the 2026 to 2028 syllabus, so no past paper question asks for it by name. The questions below are past Paper 4 questions on closely related ideas (inequality, the Gini coefficient, equity, supply-side and fiscal policy and income distribution), reworded, plus practice questions with model answers written for this page. Paper 3 multiple choice questions on the Kuznets curve, Gini and redistribution are included.",
  [("Data response parts, 3 to 8 marks", "3", "May/June 2024 (41, 43) 1(a), (b), (d); Oct/Nov 2023 (43) 1(a)"), ("Practice questions", "2", "Model answers included"), ("Multiple choice (Paper 3)", "7 shown below", "2020 to 2024")],
  [
  eq("Based on May/June 2024 · 9708/41 and 43 · Q1(a) and (b)", "3 + 3 marks", "(a) Describe the Gini coefficient and the range of values it can take. (b) Distinguish between absolute poverty and relative poverty.",
     ["<b>(a)</b> A measure of income inequality derived from the Lorenz curve (1), equal to the area between the line of equality and the curve as a share of the area under the line (1). It ranges from 0 (perfect equality) to 1 (complete inequality) (1).",
      "<b>(b)</b> Absolute poverty: income below a fixed level needed for basic needs, the same in every country (1 to 2). Relative poverty: income below a fraction of the national average or median, so it depends on how far the person is behind others in their own country (1 to 2). Credit a contrast: relative poverty can exist in a rich country."],
     "Define Gini and give its range. For (b) give both definitions then one contrast."),
  eq("Based on Oct/Nov 2023 · 9708/43 · Q1(a)", "3 marks", "Describe what is meant by economic equality and distinguish it from equity.",
     ["Equality: income, wealth or opportunity shared equally between people or groups (1 to 2).",
      "Equity: a fair distribution, which may be unequal if the differences reflect effort, skill or need (1 to 2).",
      "Credit an example: a progressive tax can improve equity without making incomes equal."],
     "Define both, then make the distinction explicit in one sentence."),
  eq("Based on May/June 2024 · 9708/41 and 43 · Q1(d)", "8 marks", "Choose one supply-side policy and one fiscal policy. Assess how each could help a government achieve a more equal distribution of income.",
     ["For each policy: a correct example (1), developed explanation of the mechanism (2), and a link to equality (1).",
      "Fiscal example: progressive income tax with higher benefits or transfers, or higher spending on public services; explain how disposable income shifts to lower-income households.",
      "Supply-side example: spending on education and training, or an apprenticeship scheme; explain how higher skills raise earnings and employment for poorer households.",
      "Credit evaluation: time lags, cost, incentive effects, targeting."],
     "Two policies, each in the same pattern: example, mechanism, link to equality, one limit.")
  ] + [
  eq("Practice (not a past paper question)", "8 marks", "Explain what is meant by inclusive economic growth and why economic growth may not reduce inequality.",
     ["Definition: growth whose benefits are widely shared and in which all groups can participate.",
      "At least two reasons growth may widen inequality: gains go to owners of capital or scarce skills, technology replaces routine jobs, growth is concentrated in some regions, poorer households lack education or credit.",
      "Evidence or measure: the Gini coefficient or growth of incomes by group.",
      "Evaluation: growth can still cut absolute poverty, and policy can change the spread of gains."],
     "Define. Two reasons with causes. Name a measure. One evaluation point.",
     [[("k", "Inclusive economic growth is growth in real national output whose benefits are widely shared across households and regions, and in which people from all groups have the chance to take part."), ("n", "Economic growth does not always reduce inequality because the extra income may go mostly to those who already own capital or have scarce skills. For example, if technology raises the pay of highly skilled workers but replaces routine jobs, the incomes of high earners rise faster than those of low earners. Growth may also be concentrated in cities, leaving rural areas behind, and poorer households may lack the education or credit needed to share in new opportunities.")],
      [("a", "In such cases the Gini coefficient could rise even while real GDP per head is rising, which would show that growth has become less inclusive."), ("e", "However, growth could still reduce absolute poverty if the incomes of the poorest rise in dollar terms, and government policies such as progressive taxes, education and training may spread the gains more widely.")]]),
  eq("Practice (not a past paper question)", "12 marks", "Evaluate policies a government could use to make growth more inclusive.",
     ["Two or three policies explained with mechanisms: progressive tax and transfers, education and training, infrastructure for poorer regions, minimum wage, access to finance.",
      "Evaluation for each or overall: incentive effects and the equity-efficiency trade-off, cost and borrowing, time lags, targeting, enforcement.",
      "A judgement on which combination is most likely to work and over what time horizon."],
     "Fiscal policy, supply-side policy, one other. Strength and limit of each. Judge by time horizon.")
  ],
  )

tips = tips_html(
  [("Define 'inclusive' with both parts.", "Benefits widely shared and people from all groups able to take part."),
   ("Separate poverty from inequality.", "Growth can cut absolute poverty and still widen inequality. Say which one the question is about."),
   ("Use the Gini and Lorenz curve.", "Gini = A ÷ (A + B). A lower Gini means more equal. Use the numbers if you are given them."),
   ("Equality is not equity.", "Equity is fairness, which need not be equal. Use this distinction in evaluation."),
   ("Match the policy to the mechanism.", "Fiscal: redistribute through tax and transfers. Supply-side: raise skills and access. Say how each reaches poorer households."),
   ("Evaluate with the trade-off.", "Higher taxes and benefits may weaken incentives, but education and health spending can raise growth as well as equity."),
   ("Use 'could' about the Kuznets curve.", "It is a tendency, and evidence is mixed.")],
  [("Define", "Inclusive growth is growth whose benefits are widely shared and in which all groups are able to take part."),
   ("Growth and inequality", "Real GDP per head could rise while the Gini coefficient also rises, if most of the gain goes to high earners."),
   ("Kuznets", "In the early stages of development inequality may rise as workers move into higher-paid jobs, then fall as education and welfare spread the gains."),
   ("Fiscal policy", "A progressive income tax combined with benefits could redistribute income from high earners to low earners."),
   ("Evaluate", "However, higher marginal tax rates could reduce incentives to work and invest, so there may be a trade-off between equity and efficiency.")],
  [CW["define"], CW["explain"], CW["assess"], CW["evaluate"]]) + FC

js = '''
/* ---------- Lorenz picture and Watch 1 ---------- */
const LX = (v) => 80 + v * 260, LY = (v) => 310 - v * 260;
function lorenzDraw(s) {
  const k = s.k, pts = []; for (let x = 0; x <= 1.0001; x += 0.02) pts.push([LX(x), LY(Math.pow(x, k))]);
  const gini = (k - 1) / (k + 1);
  let o = axes(80, 310, 360, 40, "Cumulative % of households", "Cumulative % of income") + SV.line(LX(0), LY(0), LX(1), LY(1), "c3 dash") + tag(LX(0.55), LY(0.62) - 6, "line of equality", "t3");
  o += SV.path(Lib.ptsPath(pts) + ` L ${LX(1)} ${LY(0)} Z`, "f1", { opacity: 0.12 }) + SV.path(Lib.ptsPath(pts), "c1");
  o += tag(LX(0.78), LY(0.34), "A", "t4", 1, "middle") + tag(LX(0.8), LY(0.08), "B", "t1", 1, "middle");
  o += tag(LX(0.04), LY(0.92), "Gini = A ÷ (A + B) = " + Lib.fmtN(gini, 2), "t1", 1);
  if (s.t) o += tag(LX(0.04), LY(0.82), s.t, "t2");
  return o;
}
function lorenzOnly(k) { return lorenzDraw({ k }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 360" role="img" aria-label="Lorenz curve with the line of equality and the Gini coefficient formula, next to a line showing the Kuznets curve"><g>${lorenzDraw({ k: 2 })}</g>
  <g>${axes(430, 310, 740, 40, "Income per head", "Inequality") + SV.path("M 440 280 Q 560 40 725 270", "c2") + SV.circle(500, 156, 6, "dot2") + tag(510, 140, "industrialising: inequality rises", "t2") + SV.circle(660, 188, 6, "dot3") + tag(660, 172, "rich: inequality falls", "t3", 1, "middle") + tag(585, 60, "Kuznets curve", "t1", 1, "middle")}</g></svg>`;
Lib.stepper($("#stL"), { w: 400, h: 340, label: "Lorenz curve showing unequal growth and inclusive growth", base: { k: 2, t: "" }, draw: lorenzDraw, tween: 1100, dwell: 5600, steps: [
  { cap: "<b>Starting point.</b> The Lorenz curve shows the share of income held by each share of households. The further it bows from the line of equality, the greater the inequality. Here Gini is about 0.33.", s: { k: 2 } },
  { cap: "<b>Growth that is not inclusive.</b> GDP per head rises, but most of the gain goes to the top. The curve bows further from equality and the <b>Gini rises</b> to about 0.43, even though average income is higher.", s: { k: 2.5, t: "Gini up: gains concentrated" } },
  { cap: "<b>Inclusive growth.</b> Growth is accompanied by education, training, a progressive tax and better access for poorer households. The curve moves <b>towards</b> the line of equality and the Gini falls to about 0.2.", s: { k: 1.5, t: "Gini down: gains shared" } },
] });

/* ---------- Watch 2: Kuznets ---------- */
function kzDraw(s) {
  const KX = (x) => 70 + x * 650, KY = (x) => 280 - 220 * Math.sin(Math.PI * x) ** 1.0;
  const pts = []; for (let x = 0; x <= s.p + 1e-9; x += 0.01) pts.push([KX(x), KY(x)]);
  let o = axes(70, 300, 740, 30, "Income per head", "Inequality") + SV.path(Lib.ptsPath(pts), "c2") + SV.circle(KX(s.p), KY(s.p), 7, "dot4");
  if (s.l) o += tag(KX(s.p) + 12, KY(s.p) - 12, s.l, "t4");
  return o;
}
Lib.stepper($("#stK"), { w: 760, h: 330, label: "Kuznets curve traced from a poor agricultural economy through industrialisation to a rich economy", base: { p: 0.02, l: "" }, draw: kzDraw, tween: 1300, dwell: 5600, steps: [
  { cap: "<b>Poor, mainly agricultural.</b> Most people are poor, so income is fairly equally (poorly) shared and inequality is low.", s: { p: 0.03, l: "agricultural" } },
  { cap: "<b>Industrialising.</b> Some workers move into higher-paid city jobs and capital owners gain. Average income rises but <b>inequality rises</b> too.", s: { p: 0.3, l: "industrialising" } },
  { cap: "<b>The turning point.</b> Inequality peaks. Schooling spreads, labour becomes scarcer and the government can afford benefits and progressive taxes.", s: { p: 0.5, l: "turning point" } },
  { cap: "<b>Rich economy.</b> On this view inequality <b>falls</b> as income per head keeps rising. In reality the pattern is not automatic, and several rich countries have seen inequality rise again since the 1980s.", s: { p: 0.9, l: "rich economy" } },
] });

/* ---------- Lab 1: who gains ---------- */
function labShare() {
  if (!$("#gr") || !$("#sb") || !$("#st")) return;
  const g = +$("#gr").value / 100, sb = Math.min(+$("#sb").value, 100 - +$("#st").value) / 100, st = +$("#st").value / 100, sm = 1 - sb - st;
  const base = { b: 15, m: 50, t: 35 }, total = 100, extra = total * g;
  const gb = base.b ? extra * sb / base.b * 100 : 0, gm = extra * sm / base.m * 100, gt = extra * st / base.t * 100;
  const shareB = (base.b + extra * sb) / (total + extra) * 100;
  $("#r1").textContent = Lib.fmtN(gb, 1) + "%"; $("#r2").textContent = Lib.fmtN(gt, 1) + "%"; $("#r3").textContent = Lib.fmtN(shareB, 1) + "%";
  const avg = g * 100;
  $("#rv").textContent = gb >= avg ? `The bottom 40% gain ${Lib.fmtN(gb, 1)}%, at least as fast as the ${Lib.fmtN(avg, 1)}% average, so their share rises. This growth is inclusive.` : `The bottom 40% gain ${Lib.fmtN(gb, 1)}%, slower than the ${Lib.fmtN(avg, 1)}% average, so their share falls from 15% to ${Lib.fmtN(shareB, 1)}%. Incomes rise for all but inequality widens: growth is not inclusive.`;
  const mx = Math.max(gb, gm, gt, avg, 1) * 1.15, y = (v) => 250 - v / mx * 210;
  const bars = [["Bottom 40%", gb, "f3", "t3"], ["Middle 50%", gm, "f1", "t1"], ["Top 10%", gt, "f4", "t4"]];
  let o = SV.line(40, 250, 400, 250) + SV.line(40, y(avg), 400, y(avg), "c2 dash") + tag(396, y(avg) - 6, "average " + Lib.fmtN(avg, 1) + "%", "t2", 1, "end");
  bars.forEach((b, i) => { const x = 70 + i * 110; o += SV.rect(x, y(b[1]), 80, 250 - y(b[1]), b[2]) + tag(x + 40, y(b[1]) - 6, Lib.fmtN(b[1], 1) + "%", b[3], 1, "middle") + SV.text(x + 40, 270, b[0], "sm bd", { "text-anchor": "middle" }); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "gr", label: "Growth in total income (%) ", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: labShare });
Lib.slider($("#g2"), { id: "sb", label: "Share of extra income to bottom 40% (%) ", min: 0, max: 60, step: 5, value: 10, fmt: (v) => v, onInput: labShare });
Lib.slider($("#g3"), { id: "st", label: "Share of extra income to top 10% (%) ", min: 0, max: 80, step: 5, value: 50, fmt: (v) => v, onInput: labShare });
labShare();
btnTable("lbBtns", "lbOut", [
  ["Progressive income tax and benefits", "Fiscal", "Takes a larger share from high earners and pays benefits to low earners", "Weaker incentives, cost, targeting"],
  ["Education and training", "Supply-side", "Raises skills and earning power of poorer households", "Slow, costly, may not match jobs"],
  ["Infrastructure in poorer regions", "Supply-side", "Connects remote areas to jobs and markets", "High cost, benefits take years"],
  ["National minimum wage", "Labour market", "Raises pay at the bottom immediately", "May cut jobs if set too high"],
  ["Access to credit and small-firm support", "Supply-side", "Lets poorer people start and grow businesses", "Defaults, hard to target"],
  ["Anti-discrimination laws", "Regulation", "Widens participation by women and minorities", "Hard to enforce"]
], ["Policy", "Type", "How it promotes inclusion", "Weakness"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Does the change make growth more inclusive or less inclusive?", ["More inclusive", "Less inclusive"],
  [("Free schooling for children in poor regions", 0), ("Gains from growth go mainly to owners of capital", 1), ("Introduction of a minimum wage that raises low pay", 0), ("Growth concentrated in a single capital city", 1), ("Mobile banking opens finance to poor households", 0), ("Cuts in benefits while top tax rates are cut", 1), ("Training schemes for workers whose jobs are automated", 0), ("Rising Gini coefficient while GDP per head rises", 1)],
  "Inclusive growth shares the gains and widens participation.") + MATCH([
  ["Inclusive growth", "Growth whose benefits are widely shared and open to all groups"],
  ["Gini coefficient", "Measure of inequality from 0 (equal) to 1 (unequal)"],
  ["Kuznets curve", "Inverted U between income per head and inequality"],
  ["Equity", "A fair distribution of income, not necessarily equal"],
  ["Absolute poverty", "Income below a fixed minimum for basic needs"],
  ["Relative poverty", "Income well below the national average"]]) + ORDER(
  "Put the Kuznets curve story in order.",
  ["A poor economy is mainly agricultural, with low inequality", "Workers move to higher-paid industrial jobs and inequality rises", "Inequality reaches a peak at the turning point", "Education spreads and the state expands welfare", "Inequality falls as income per head keeps rising"],
  "The inverted U is a tendency, not a certainty.") + CALC([
  {"q": "The poorest 40% of households have a total income of $150bn. Over a year their income rises to $160bn. Calculate the percentage growth in their income.", "a": 6.7, "unit": "%", "tol": 0.1, "hint": "Change ÷ original × 100.", "sol": "10 ÷ 150 × 100 = <b>6.7%</b> (one decimal place)."},
  {"q": "Area A (between the line of equality and the Lorenz curve) is 0.12 and area B (below the Lorenz curve) is 0.38. Calculate the Gini coefficient.", "a": 0.24, "tol": 0.005, "hint": "Gini = A ÷ (A + B).", "sol": "0.12 ÷ (0.12 + 0.38) = 0.12 ÷ 0.50 = <b>0.24</b>."},
  {"q": "National income is $1,000bn and the richest 10% receive $350bn. Over the year income grows by 6% and the richest 10% receive 60% of the extra income. Calculate the richest 10%'s new share of income (percentage, one decimal place).", "a": 36.4, "unit": "%", "tol": 0.1, "hint": "Extra income = 60. Richest get 36 of it.", "sol": "Extra = $60bn. Richest receive 0.6 × 60 = $36bn, so $386bn of $1,060bn = <b>36.4%</b>."},
  {"q": "A country's average income rises 4%. The bottom 40% see their income rise 7%. Is growth inclusive by the 'bottom 40% grow at least as fast as average' test? Type 1 for yes and 0 for no.", "a": 1, "tol": 0.01, "hint": "Compare 7% with 4%.", "sol": "The bottom 40% grew faster than average, so their share rises: <b>yes (1)</b>."}]) + MCQ([
  ("Which statement about inclusive growth is correct?", ["It is the same as rapid GDP growth", "It requires the gains from growth to be widely shared", "It means everyone's income is equal", "It is only about reducing absolute poverty"], 1, "Inclusive growth is about who benefits and who can take part, not just the size of GDP."),
  ("A country's GDP per head rises 5% and the Gini coefficient also rises. What does this suggest?", ["Growth has been inclusive", "Growth has probably widened inequality", "Absolute poverty must have risen", "Income is now equally distributed"], 1, "A rising Gini means income is less equally distributed even though average income has risen."),
  ("Which policy is a supply-side way of making growth more inclusive?", ["A cut in the top rate of income tax", "Free vocational training for low-income workers", "A rise in indirect taxes", "A fall in benefits"], 1, "Training raises skills and earnings of poorer households. The other three do not raise their productivity."),
  ("What is the main objection to high marginal tax rates as a way to promote inclusive growth?", ["They always cut tax revenue", "They may weaken the incentive to work and invest", "They have no effect on income distribution", "They reduce the Gini coefficient too slowly"], 1, "The equity-efficiency trade-off: higher tax rates may reduce effort, saving and investment."),
  ("On the Kuznets curve, what happens to inequality at the earliest stage of industrialisation?", ["It falls", "It rises", "It stays constant", "It becomes zero"], 1, "On the rising part of the inverted U, inequality increases as some workers move to higher-paid jobs.")
], "qz1") + CARDS([
  ("Inclusive growth", "Growth with widely shared benefits and wide participation."),
  ("Equality", "Equal shares of income or wealth."),
  ("Equity", "A fair distribution, not necessarily equal."),
  ("Gini coefficient", "A ÷ (A + B) on a Lorenz diagram: 0 equal, 1 unequal."),
  ("Lorenz curve", "Cumulative share of income against cumulative share of households."),
  ("Kuznets curve", "Inequality rises then falls as income per head rises."),
  ("Absolute poverty", "Income below a fixed minimum for basic needs."),
  ("Relative poverty", "Income below a fraction of the national average.")]) + MCQ(mc_exam)

build("sy925", "inclusive-economic-growth", "Inclusive Economic Growth", EY,
  "9.2.5: what inclusive growth means, how growth affects equity and equality, the Gini coefficient and Kuznets curve, and policies that spread the gains. Animated diagrams, labs, drills and exam practice.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
