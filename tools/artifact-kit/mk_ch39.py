"""Builds the three ch39 part pages (eq1..eq3) from slices of eq.* plus new content. Run: python3 tools/artifact-kit/mk_ch39.py"""
from splitter import *
mktips = tips
S = Src("eq")
HEAD = S.j_((1, 14))
EY = "A Level Economics · 9708 · Syllabus 8.2 · Part {} of 3"
RW = '<p class="note">Examples are explained in general terms. Check current details before quoting them in an exam answer.</p>\n'

# ------------------------------------------------------------------ 39.1
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b>Economic equality</b> means an equal distribution of income, wealth or opportunity, while <b>equity</b> means <b>fairness</b>, a value judgement about what distribution is just. <b>Income</b> is a flow received over a period and <b>wealth</b> is a stock of assets at a point in time, and wealth is usually distributed more unequally. Inequality is measured with the <b>Lorenz curve</b>, which plots cumulative % of income against cumulative % of the population, and the <b>Gini coefficient</b>, the area between the curve and the line of equality as a share of the area under that line. <b>Absolute poverty</b> is income below a survival level; <b>relative poverty</b> is low income compared with the average.</p></div>
''' + S.b((25, 32), (34, 47))
watch = S.b((82, 84))
explore = S.b((97, 102)) + '''
  <h2>Lab 2 · Absolute and relative poverty</h2>
  <p>Five households have incomes of $8k, $12k, $18k, $30k and $60k. The absolute poverty line is $10k. The relative poverty line is 50% of the median income. Raise every income by the same percentage and see which poverty measure changes.</p>
  <div class="card"><div class="grid2"><div><div id="g7"></div>
    <div class="readout"><div><small>Median income</small><strong id="v1"></strong></div><div><small>Below absolute line ($10k)</small><strong id="v2"></strong></div><div><small>Relative line (50% of median)</small><strong id="v3"></strong></div><div><small>Below relative line</small><strong id="v4"></strong></div></div>
    <div class="verdict" id="vv"></div></div>
    <div><svg id="labW" viewBox="0 0 420 280" role="img" aria-label="Household incomes with the absolute and relative poverty lines"></svg></div></div></div>
'''
practise = S.b((134, 135)).replace("3 · Income", "1 · Income") + S.b((140, 141)).replace("5 · Put", "2 · Put") + '''
  <h2>3 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = RW + S.b((153, 153)) + '''  <div class="rw"><h3>Income compared with wealth</h3><p>A household may have a modest salary but own a valuable house. Its income is low and its wealth is high. Wealth is usually shared more unequally than income because assets are passed on and can grow.</p><div class="use"><b>Exam use:</b> distinguishing income (a flow) from wealth (a stock).</div></div>
'''
exam = '''
  <h2>Past paper questions on equity, equality and measuring inequality</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the data response parts on equity, equality, the Gini coefficient and poverty, and Paper 3 multiple choice questions on the Lorenz curve and the distribution of income. The June 2020 papers were not sat. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Data response parts, 3 to 11 marks</td><td>6</td><td>May/June 2024 (41, 43); Feb/March 2024 (42); Feb/March 2021 (42); Oct/Nov 2023 (42, 43)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>4 shown below</td><td>2020 to 2025</td></tr>
  </table></div>
  <h2>A · Data response parts</h2>
''' + KEYL + S.b((175, 181), (183, 189), (200, 203), (205, 207), (209, 209), (211, 211)) + '''
''' + MCQTAIL.format("B · Multiple choice questions (Paper 3)")
tips = mktips(S, (236, 237, 238, 239), "", (249, 250)) + cmd(("Describe", "Give the main features or meaning."), ("Distinguish", "Say clearly how two ideas differ."), CW["consider"]) + FC
js = HEAD + S.j_((15, 40), (81, 98)) + '''
/* ---------- Lab 2: poverty lines ---------- */
function labPov() {
  if (!$("#gr")) return;
  const g = +$("#gr").value / 100, inc = [8, 12, 18, 30, 60].map((v) => v * (1 + g)), med = inc[2], rel = 0.5 * med, a = inc.filter((v) => v < 10).length, r = inc.filter((v) => v < rel).length;
  $("#v1").textContent = "$" + Lib.fmtN(med, 1) + "k"; $("#v2").textContent = a + " of 5"; $("#v3").textContent = "$" + Lib.fmtN(rel, 1) + "k"; $("#v4").textContent = r + " of 5";
  $("#vv").textContent = g === 0 ? "With incomes as they are, one household is below the absolute line and one below the relative line."
    : `Every income has risen ${Math.round(g * 100)}%. The absolute line is fixed at $10k, so ${a === 0 ? "nobody" : a + (a === 1 ? " household is" : " households are")} below it. The relative line moves up with the median to $${Lib.fmtN(rel, 1)}k, and ${r} household${r === 1 ? " is" : "s are"} still below it. Absolute poverty can fall while relative poverty stays the same.`;
  const base = 240, H = (v) => v * 2.6, bw = 40;
  let o = SV.line(30, base, 400, base) + SV.text(30, 20, "Income ($k)", "sm");
  inc.forEach((v, i) => { const x = 50 + i * 68; o += SV.rect(x, base - H(v), bw, H(v), v < 10 || v < rel ? "f2" : "f1") + SV.text(x + bw / 2, base - H(v) - 6, Lib.fmtN(v, 1), "sm bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, base + 16, "H" + (i + 1), "sm", { "text-anchor": "middle" }); });
  o += SV.line(30, base - H(10), 400, base - H(10), "c3", { "stroke-dasharray": "6 5" }) + SV.text(398, base - H(10) - 6, "absolute $10k", "sm bd t3", { "text-anchor": "end", style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px" }) + SV.line(30, base - H(rel), 400, base - H(rel), "c4", { "stroke-dasharray": "3 4" }) + SV.text(398, base - H(rel) + 16, "relative $" + Lib.fmtN(rel, 1) + "k", "sm bd t4", { "text-anchor": "end", style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px" });
  $("#labW").innerHTML = o;
}
Lib.slider($("#g7"), { id: "gr", label: "Rise in every household's income: ", min: 0, max: 100, step: 10, value: 0, fmt: (v) => v + "%", onInput: labPov });

/* ---------- Practise ---------- */
''' + S.j_((165, 172), (183, 190)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Economic equality", "An equal distribution of income, wealth or opportunities"],
  ["Equity", "Fairness in the distribution of resources, a value judgement"],
  ["Income", "A flow received over a period"],
  ["Wealth", "A stock of assets at a point in time"],
  ["Lorenz curve", "Cumulative % of income against cumulative % of the population"],
  ["Gini coefficient", "Area A ÷ (A + B), from 0 (equality) to 1 (inequality)"],
  ["Absolute poverty", "Income below the level needed for basic survival"],
  ["Relative poverty", "Income low compared with the average in the same society"],
], done: "Eight words for measuring inequality." });
''' + calc(S, (192, 193, 198), '''  { q: "The richest 20% receive 50% of income and the poorest 20% receive 5%. By how many percentage points does the richest share exceed the poorest share?", a: 45, sol: "50 − 5 = <b>45</b> percentage points." },
  { q: "Five household incomes are $8k, $12k, $18k, $30k and $60k. What is the median ($k)?", a: 18, sol: "The middle value of the five, in order, is <b>$18k</b>." },
''') + qz(S, (201, 202, 205), '''  { q: "Relative poverty is measured against:", opts: ["a fixed survival income", "the average income in the same society", "the poverty line of another country", "zero income"], a: 1, why: "Relative poverty compares a household with the typical household in its own society." },
''') + cards(S, tuple(range(209, 218))) + mcq(S, (232, 233, 234, 235))
write("eq1", page(EY.format(1), "Equity, Equality and Measuring Inequality",
  "Equity and equality, income and wealth, absolute and relative poverty, the Lorenz curve and the Gini coefficient. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Equity, Equality and Measuring Inequality", "equity-equality-measuring-inequality")

# ------------------------------------------------------------------ 39.2
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Taxes are classified by how the <b>average tax rate</b> changes with income. A <b>progressive</b> tax takes a larger share of income as income rises (income tax with higher bands and a tax-free allowance), a <b>proportional</b> tax takes the same share, and a <b>regressive</b> tax takes a smaller share (many sales taxes, because the poor spend a larger share of income). <b>Direct</b> taxes (income, wealth, inheritance) are paid on income or wealth, <b>indirect</b> taxes (sales, fuel duty) on spending. A government can reduce inequality by making the tax system more progressive and by taxing wealth, but very high rates may affect incentives and encourage avoidance.</p></div>
''' + S.b((49, 61)) + '''
  <h2>2 · Average and marginal rates</h2>
  <p>The <b>average rate</b> is total tax divided by income. The <b>marginal rate</b> is the tax on the next dollar earned. With a tax-free allowance of $10,000 and a 20% rate above it, a person on $30,000 pays $4,000 (an average rate of 13.3%) and the marginal rate is 20%. As income rises, the average rate climbs towards 20% but never reaches it, which makes the tax progressive.</p>
  <div class="tip"><b class="h">Disposable income</b>Disposable income is income minus direct taxes plus cash benefits. Sales taxes are paid out of disposable income, so they are not subtracted when it is calculated. If a household earns $100 and pays $45 income tax and receives $5 in benefits, its disposable income is $100 − $45 + $5 = $60.</div>
'''
watch = S.b((86, 88)).replace("2 · Progressive", "1 · Progressive")
explore = S.b((104, 109)).replace("Lab 2 ·", "Lab 1 ·") + '''
  <h2>Lab 2 · Tax with an allowance</h2>
  <p>A tax-free allowance of $10,000 and a tax rate you choose on income above it. Move income and see the average rate rise towards the headline rate.</p>
  <div class="card"><div class="grid2"><div><div id="g8"></div><div id="g9"></div>
    <div class="readout"><div><small>Tax paid</small><strong id="x1"></strong></div><div><small>Average rate</small><strong id="x2"></strong></div><div><small>Marginal rate</small><strong id="x3"></strong></div><div><small>Disposable income</small><strong id="x4"></strong></div></div>
    <div class="verdict" id="xv"></div></div>
    <div><svg id="labX" viewBox="0 0 420 260" role="img" aria-label="Bars showing income, tax and income after tax"></svg></div></div></div>
'''
practise = S.b((128, 129)) + '''
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = RW + S.b((154, 155)) + '''  <div class="rw"><h3>A tax-free allowance</h3><p>Most income taxes let people earn a first slice free of tax. A person on a low income may pay no tax at all, while a person on a high income pays tax on most of what they earn, so the average rate rises with income.</p><div class="use"><b>Exam use:</b> why an allowance makes an income tax progressive.</div></div>
'''
exam = '''
  <h2>Past paper questions on taxes and the distribution of income</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Tax questions on this topic appear mostly as Paper 3 multiple choice questions and in the policy parts of data responses (part 3). Below are two Paper 3 questions and a practice question with a model answer. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>2 shown below</td><td>2023</td></tr>
    <tr><td>Policy parts of data responses</td><td>See part 3</td><td>2020 to 2025</td></tr>
  </table></div>
  <h2>A · Practice question with a model answer</h2>
  <div class="key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>
''' + S.b((215, 221)) + '''
''' + MCQTAIL.format("B · Multiple choice questions (Paper 3)")
tips = mktips(S, (240,), '''    <li><b>Use average rates to classify a tax.</b> Progressive means the average rate rises with income, proportional means it is constant and regressive means it falls.</li>
''', (251,)) + cmd(("Describe", "Give the main features or meaning."), CW["consider"], CW["evaluate"]) + FC
js = HEAD + S.j_((41, 60), (100, 114)) + '''
/* ---------- Lab 2: allowance ---------- */
function labAllow() {
  if (!$("#ai") || !$("#ar")) return;
  const inc = +$("#ai").value, r = +$("#ar").value / 100, tax = Math.max(0, inc - 10000) * r, avg = inc ? tax / inc : 0;
  $("#x1").textContent = "$" + Lib.fmtN(tax, 0); $("#x2").textContent = Lib.fmtN(avg * 100, 1) + "%"; $("#x3").textContent = inc > 10000 ? Math.round(r * 100) + "%" : "0%"; $("#x4").textContent = "$" + Lib.fmtN(inc - tax, 0);
  $("#xv").textContent = inc <= 10000 ? "Income is within the tax-free allowance, so no tax is paid: average and marginal rates are zero."
    : `Tax is ${Math.round(r * 100)}% of the $${Lib.fmtN(inc - 10000, 0)} above the allowance, $${Lib.fmtN(tax, 0)}. The average rate (${Lib.fmtN(avg * 100, 1)}%) is below the marginal rate (${Math.round(r * 100)}%) and rises with income: a progressive tax.`;
  const H = (v) => v / 600, base = 200;
  let o = SV.line(30, base, 400, base);
  [[60, inc, "f1", "Income"], [160, tax, "f2", "Tax"], [260, inc - tax, "f3", "After tax"]].forEach(([x, v, c, l]) => { o += SV.rect(x, base - H(v), 70, H(v), c) + SV.text(x + 35, base - H(v) - 6, "$" + Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 35, 220, l, "sm", { "text-anchor": "middle" }); });
  $("#labX").innerHTML = o;
}
Lib.slider($("#g8"), { id: "ai", label: "Income ($): ", min: 5000, max: 100000, step: 5000, value: 30000, fmt: (v) => v.toLocaleString(), onInput: labAllow });
Lib.slider($("#g9"), { id: "ar", label: "Tax rate above $10,000: ", min: 10, max: 50, step: 5, value: 20, fmt: (v) => v + "%", onInput: labAllow });

/* ---------- Practise ---------- */
''' + S.j_((147, 155)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Progressive tax", "The average tax rate rises as income rises"],
  ["Proportional tax", "The average tax rate is the same at all incomes"],
  ["Regressive tax", "The average tax rate falls as income rises"],
  ["Direct tax", "A tax on income or wealth"],
  ["Indirect tax", "A tax on spending"],
  ["Average tax rate", "Total tax divided by income"],
  ["Marginal tax rate", "The tax on the next dollar earned"],
  ["Tax-free allowance", "A slice of income on which no tax is paid"],
], done: "Eight words for the tax system." });
''' + calc(S, (194, 195, 196), '''  { q: "The top 20% of earners pay 45% of their income in income tax and receive 5% in cash benefits. What percentage of their income is disposable?", a: 60, sol: "100 − 45 + 5 = <b>60%</b>." },
  { q: "With a $10,000 allowance and a 20% rate above it, what is the average tax rate for a person on $50,000 (%)?", a: 16, sol: "Tax = 20% × 40,000 = $8,000; 8,000 ÷ 50,000 = <b>16%</b>." },
''') + qz(S, (203,), '''  { q: "A tax with a tax-free allowance and a flat rate above it is:", opts: ["regressive", "proportional", "progressive", "indirect"], a: 2, why: "The average rate rises with income, towards the flat rate." },
  { q: "A sales tax takes a larger share of income from poor households because:", opts: ["the rate is higher for the poor", "poor households spend a larger share of income", "the poor pay more income tax", "it is a direct tax"], a: 1, why: "Spending is a bigger share of a low income, so a tax on spending is regressive." },
''') + cards(S, (218, 219, 220), '''  ["Average tax rate", "Total tax divided by income."],
  ["Marginal tax rate", "The tax on the next dollar of income."],
  ["Tax-free allowance", "Income below which no tax is paid, making an income tax progressive."],
  ["Disposable income", "Income minus direct taxes plus cash benefits."],
''') + mcq(S, (230,), '''  { q: "[Feb/March 2023 · 32 · Q16] In a country, the top 20% of earners pay 45% in income tax and 25% on sales taxes, and receive 5% in cash benefits. What is the percentage of disposable income for this group?", opts: ["30%", "55%", "60%", "80%"], a: 2, why: "Disposable income is income minus income tax plus benefits: 100 − 45 + 5 = 60%. Sales taxes are paid out of disposable income and are not subtracted." },
''')
write("eq2", page(EY.format(2), "Taxes and the Tax System",
  "Progressive, proportional and regressive taxes, direct and indirect taxes, average and marginal rates and the effect of a tax-free allowance. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Taxes and the Tax System", "taxes-and-the-tax-system")

# ------------------------------------------------------------------ 39.3
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Governments reduce inequality with <b>fiscal policy</b> (progressive taxes and <b>transfer payments</b> such as means-tested benefits, pensions and free public services) and with <b>supply-side and labour market policies</b> (education, training, a minimum wage) that raise low earners' incomes. These policies involve trade-offs: very high taxes may weaken <b>incentives</b>, benefits that are withdrawn as earnings rise can create a <b>poverty trap</b>, redistribution costs money and can be avoided, and some policies take years to work. Evaluation weighs <b>equity against efficiency</b> and asks how large each effect is.</p></div>
''' + S.b((63, 67), (69, 77)).replace("4 · Benefits", "1 · Benefits").replace("5 · Trade-offs", "2 · Trade-offs")
watch = S.b((90, 92)).replace("3 · The poverty", "1 · The poverty")
explore = S.b((111, 116), (118, 123)).replace("Lab 3 ·", "Lab 1 ·").replace("Lab 4 ·", "Lab 2 ·")
practise = S.b((131, 132)).replace("2 · Fiscal", "1 · Fiscal") + '''
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = RW + S.b((156, 158))
exam = '''
  <h2>Past paper questions on redistribution policies</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the data response part on supply-side and fiscal policy, practice essays with plans and model answers (our own, not past paper questions), and Paper 3 multiple choice questions. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Data response part, 8 marks</td><td>1</td><td>May/June 2024 (41, 43)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>6 shown below</td><td>2020 to 2025</td></tr>
  </table></div>
  <h2>A · Data response part</h2>
''' + KEYL + S.b((191, 198)) + '''
  <h2>B · Practice questions (our own, not past paper questions)</h2>
''' + S.b((222, 225)) + '''
''' + MCQTAIL.format("C · Multiple choice questions (Paper 3)")
tips = mktips(S, (241, 242, 243), '', (252, 253)) + cmd(CW["explain"], CW["consider"], CW["evaluate"], CW["discuss"]) + FC
js = HEAD + S.j_((61, 80), (116, 144)) + '''
/* ---------- Practise ---------- */
''' + S.j_((156, 164)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Transfer payment", "A payment such as a benefit with no good or service produced in return"],
  ["Means-tested benefit", "A benefit paid only to people below an income or wealth level"],
  ["Universal benefit", "A benefit paid to everyone who qualifies, whatever their income"],
  ["Poverty trap", "Little gain from earning more because benefits are withdrawn and tax is paid"],
  ["Supply-side policy", "A policy that raises the productive capacity or skills of workers"],
  ["Fiscal policy", "Use of government spending and taxation"],
  ["Equity versus efficiency", "The trade-off between a fairer distribution and incentives"],
], done: "Seven words for redistribution." });
''' + calc(S, (197,), '''  { q: "A means-tested benefit is withdrawn at 60 cents for each $1 earned and income tax is 20%. How much of an extra $100 of earnings does the worker keep ($)?", a: 20, sol: "Tax $20 + benefit lost $60 = $80 lost. Worker keeps <b>$20</b>." },
  { q: "A worker is offered a job that adds $200 to monthly earnings. Tax is $40 and benefits fall by $120. What is the net gain ($)?", a: 40, sol: "200 − 40 − 120 = <b>$40</b>." },
  { q: "The effective marginal tax rate in that case is (tax + benefit lost) ÷ extra earnings. What is it (%)?", a: 80, sol: "(40 + 120) ÷ 200 × 100 = <b>80%</b>." },
''') + qz(S, (204, 206), '''  { q: "Which policy is a supply-side way to reduce inequality?", opts: ["a higher top rate of income tax", "free education and training", "a cash benefit for pensioners", "a wealth tax"], a: 1, why: "It raises earning power rather than redistributing existing income." },
  { q: "The poverty trap is most likely when:", opts: ["benefits are universal", "benefits are withdrawn quickly as earnings rise", "income tax is zero", "wages fall"], a: 1, why: "A high withdrawal rate leaves the worker keeping little of any extra earnings." },
''') + cards(S, (221, 222, 223)) + mcq(S, (228, 229, 231, 236), '''  { q: "[Feb/March 2021 · 32 · Q20] The diagram shows Lorenz curves for a developed economy, X (before) and Y (after, closer to the line of equality). Which combination of supply-side policies would shift the Lorenz curve from X to Y? (top rate of income tax, education, national minimum wage)", opts: ["increase, free, increase", "increase, students pay, abolish", "reduce, free, abolish", "reduce, students pay, increase"], a: 0, why: "Moving the curve towards equality needs a higher top tax rate, free education that raises the skills of low earners, and a higher minimum wage." },
''')
write("eq3", page(EY.format(3), "Redistribution Policies, Benefits and Trade-offs",
  "Fiscal and supply-side policies to reduce inequality, transfer payments and the poverty trap, and the trade-offs between equity and efficiency. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Redistribution Policies, Benefits and Trade-offs", "redistribution-policies-benefits")
