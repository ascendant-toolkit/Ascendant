"""Syllabus 10.1.1 Government macroeconomic policy objectives. Run: python3 tools/artifact-kit/mk_sy1011.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 10.1.1"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Governments set <b class="kw">macroeconomic objectives</b> for the whole economy: <b>price stability</b> (low, stable inflation), <b>low unemployment</b>, <b>economic growth</b>, a <b>sustainable balance of payments</b>, <b>economic development</b>, <b>sustainability</b> and a fairer <b>distribution of income and wealth</b>. Each objective has an indicator and a target, such as a CPI inflation rate near 2%. The objectives are <b>linked</b>, and some conflict, so no government achieves all of them at once. Which one comes first depends on the country and the time.</p></div>

  <h2>1 · The objectives, their indicators and why they matter</h2>
  <div class="tw"><table class="t">
    <tr><th>Objective</th><th>Indicator</th><th>Typical target</th><th>Why it matters</th></tr>
    <tr><td><b>Price stability</b></td><td>Inflation rate (CPI)</td><td>Low and stable, often about 2%</td><td>Protects the value of money and savings, keeps firms' planning certain, protects competitiveness</td></tr>
    <tr><td><b>Low unemployment</b></td><td>Unemployment rate</td><td>At or near the natural rate (full employment)</td><td>Wasted resources, lost output and income, social costs, higher benefit spending</td></tr>
    <tr><td><b>Economic growth</b></td><td>Annual change in real GDP</td><td>Steady growth near the trend rate</td><td>Higher incomes and living standards, jobs, tax revenue</td></tr>
    <tr><td><b>Balance of payments</b></td><td>Current account as a % of GDP</td><td>Stable, no large persistent deficit</td><td>Persistent deficits mean borrowing, pressure on the currency and a loss of control</td></tr>
    <tr><td><b>Economic development</b></td><td>HDI, income per head, poverty rate</td><td>Rising living standards for all</td><td>Growth alone may not improve health, education or equality</td></tr>
    <tr><td><b>Sustainability</b></td><td>Emissions, resource depletion</td><td>Growth that does not reduce future potential</td><td>Protects the environment and future generations</td></tr>
    <tr><td><b>Redistribution of income and wealth</b></td><td>Gini coefficient, poverty rate</td><td>A fairer spread, judged by equity</td><td>Fairness, social stability, support for poorer households</td></tr>
  </table></div>
  <div id="pic1" class="card"></div>

  <h2>2 · Tools used to reach the objectives</h2>
  <ul>
    <li><b>Fiscal policy:</b> government spending and taxes.</li>
    <li><b>Monetary policy:</b> interest rates, the money supply, quantitative easing.</li>
    <li><b>Supply-side policy:</b> education, training, infrastructure, competition, labour market reform.</li>
    <li><b>Exchange rate policy:</b> managing or targeting the currency's value.</li>
    <li><b>International trade policy:</b> tariffs, quotas, trade agreements.</li>
  </ul>
  <p>No tool works on one objective alone. Interest rates, for example, affect inflation, growth, unemployment and the exchange rate together. That is why 10.2 (links) and 10.3 (conflicts) follow.</p>

  <h2>3 · Priorities differ</h2>
  <div class="grid2">
    <div class="card"><h3>Developed economies</h3><p>Often focus on <b>stable inflation, low unemployment and steady growth</b>, with an independent central bank targeting inflation. Sustainability and the distribution of income have become more prominent.</p></div>
    <div class="card"><h3>Developing economies</h3><p>Often put <b>growth, development and reducing poverty</b> first, and need to manage <b>the balance of payments and debt</b>. Primary-product exporters may care about stable export earnings.</p></div>
  </div>
  <div class="tip"><b class="h">Strategy for exam answers</b>Name the objective, give its indicator, say why it matters, say which tool targets it, and mention that a tool aimed at one objective may help or harm another. Link to the stage of the economy: in a deep recession unemployment and growth usually come before inflation; when inflation is high it often comes first.</div>
'''

watch = '''
  <h2>1 · Scoring an economy against its objectives</h2>
  <p>Each axis shows how close the economy is to its target (10 = target met). Press Play, or click the numbered steps.</p>
  <div id="stR"></div>
  <h2>2 · An inflation target in practice</h2>
  <div id="stI"></div>
'''

explore = '''
  <h2>Lab 1 · Macroeconomic scorecard</h2>
  <p>Enter four indicators for an economy. The lab checks each against a typical target and shows which objectives are met.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Objectives met</small><strong id="r1"></strong></div><div><small>Biggest problem</small><strong id="r2"></strong></div><div><small>Misery index</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Four indicators shown against their target ranges"></svg></div></div></div>

  <h2>Lab 2 · Which objective comes first?</h2>
  <p>Pick a situation to see which objective is likely to be the main priority and why.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Which objective does the indicator measure?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the policy cycle in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Inflation targeting", "Many central banks, including the Bank of England and the European Central Bank, aim for inflation of about 2% a year and set interest rates to keep it near that level. The target makes price stability the clearest objective and the central bank is judged on it.", "an example of a numerical target for one objective. Evaluate by noting that a single target can pull interest rates away from jobs and growth.") +
rw("The misery index", "Adding the inflation rate and the unemployment rate gives a simple measure of how bad conditions feel. Stagflation in the 1970s pushed the index very high, because both numbers rose together.", "a way to combine two objectives and a reminder that they can move in different directions.") +
rw("Development goals in low-income countries", "Many governments in low-income countries aim for growth, poverty reduction and better health and education rather than only low inflation. Growth that leaves poverty untouched is judged a failure.", "development as an objective separate from growth. Say that GDP does not capture health, education or inequality.") +
rw("Net zero targets", "Governments have set targets to cut greenhouse gas emissions to zero by about 2050. This is a sustainability objective that sits beside growth and jobs, and policies such as carbon taxes affect prices, output and employment.", "sustainability as a macroeconomic objective, and the conflicts it can create with short-run growth.")
)

mc_exam = [
  ("Which macroeconomic policy objective will not apply to a government in a closed economy? (Feb/March 2024 · 32 · Q21, reworded)", ["A low and steady rate of inflation", "A more equal distribution of income", "A surplus on the balance of payments", "A sustainable rate of economic growth"], 2, "A closed economy has no trade with other countries, so there is no balance of payments."),
  ("Which government aim is least likely to be achieved using monetary policy? (Feb/March 2023 · 32 · Q22, reworded)", ["Low unemployment", "A more equal income distribution", "A stable exchange rate", "Steady prices"], 1, "Monetary policy works through interest rates and the money supply. Changing the distribution of income needs tax and benefit policy."),
  ("When is a policy of redistributing income from rich to poor most appropriate? (Feb/March 2022 · 32 · Q15, reworded)", ["When controlling demand-pull inflation is the priority", "When equality is valued more highly than efficiency", "When monetary reward is the best incentive to take risks", "When the rich have higher marginal utility curves"], 1, "Redistribution is justified when fairness is given more weight than the incentive effects on efficiency."),
  ("Governments set economic policy aims. What would be least likely to occur if all the aims were achieved? (May/June 2023 · 32 · Q24, reworded)", ["A fall in the average standard of living", "A fall in the exchange rate", "A rise in frictional unemployment", "A rise in the rate of inflation"], 0, "If all aims, including growth, were achieved, living standards would not fall."),
  ("What is meant by sustainable economic growth? (May/June 2022 · 32 · Q18, reworded)", ["Raising productive potential as fast as possible", "Raising productive potential using only low-cost resources", "Raising productive potential without reducing future potential", "Raising future potential as fast as possible"], 2, "Sustainable growth must not reduce what future generations can produce."),
  ("It is often argued that the HDI is a better indicator of development than income per head because it adjusts for: (Oct/Nov 2024 · 31 · Q27, reworded)", ["Average hours worked", "Environmental pollution", "Inequality in income distribution", "Life expectancy at birth"], 3, "The HDI combines income with life expectancy and years of schooling."),
  ("What is the best description of sustainable economic development? (May/June 2025 · 34 · Q16, reworded)", ["A long-term rise in actual output", "A long-term rise in living standards without damage to the environment", "A long-term rise in productive potential", "A long-term rise in living standards for every member of society"], 1, "Development includes living standards, and sustainable development means achieving this without harming the environment."),
  ("The Measure of Economic Welfare (MEW) is often seen as a better measure of welfare than GDP per head. What is additionally included in MEW? (May/June 2021 · 31 · Q20, reworded)", ["The cost of paid work", "The cost of producing armaments", "An estimate of environmental damage", "The impact of the shadow economy"], 2, "MEW adjusts GDP for environmental costs and the value of unpaid work and leisure.")
]

exam = exam_page("macroeconomic objectives",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Questions on objectives mostly appear as the opening data-response parts and as essays on which aim matters most. Reworded questions are below, with a practice question and eight Paper 3 multiple choice questions.",
  [("Data response parts, 3 to 4 marks", "2", "Oct/Nov 2020 (41) 1(b)(i), (ii)"), ("Essay part, 12 or 13 marks", "2", "Feb/March 2021 (42) Q7(a); Oct/Nov 2021 (41) Q5(b)"), ("Practice question", "1", "Whether sustainability is a macroeconomic objective"), ("Multiple choice (Paper 3)", "8 shown below", "2021 to 2025")],
  [
  eq("Based on Oct/Nov 2020 · 9708/41 · Q1(b)", "3 + 4 marks", "(i) State three macroeconomic aims a government might have. (ii) A report says a country has an unemployment rate of 3.9%, a current account surplus, inflation of 1.8% and growth of 1.5%. Is there evidence that the country is achieving any of the aims?",
     ["<b>(i)</b> Any three: price stability, low unemployment, economic growth, a stable balance of payments, redistribution of income, sustainability or development (1 each).",
      "<b>(ii)</b> Use the figures: unemployment of 3.9% is low and near full employment; a current account surplus shows a healthy balance of payments; inflation of 1.8% is close to the usual 2% target.",
      "Credit a comment on growth: 1.5% is positive but modest, so that aim is only partly achieved. Quote numbers and compare each with a target."],
     "List three aims. For each piece of data say which aim it measures and whether it is met."),
  eq("Based on Oct/Nov 2021 · 9708/41 · Q5(b)", "13 marks", "To what extent do you agree that controlling inflation should be a government's most important macroeconomic aim?",
     ["Case for: inflation erodes the value of money and savings, creates uncertainty, harms competitiveness and the current account, and can feed expectations that make it hard to reverse (the wage-price spiral).",
      "Case against: high unemployment and recession waste resources and cause lasting harm (hysteresis); growth, development and poverty reduction may matter more, especially in low-income countries; controlling inflation can conflict with other aims.",
      "A conclusion that relates the answer to the situation: priority depends on how high inflation is, the size of the output gap and the country's level of development."],
     "Case for. Case against. Link to the economic situation. Judgement."),
  eq("Based on Feb/March 2021 · 9708/42 · Q7(a)", "12 marks", "'Economic growth should be the most important macroeconomic aim.' Discuss.",
     ["Define growth and list the other aims.",
      "Benefits of growth: higher incomes, jobs, tax revenue, resources for public services. Costs: inflation, a current account deficit, inequality, pollution and resource depletion.",
      "The aims are linked, so pursuing one affects the others. Level 4 needs a conclusion about the extent to which the statement holds."],
     "Define. For and against. Links between aims. Conclude on when growth should come first."),
  eq("Practice (not a past paper question)", "8 marks", "Explain why sustainability might be treated as a macroeconomic objective, and how it could conflict with other objectives.",
     ["Explain sustainability: growth that meets present needs without reducing future productive potential, including environmental limits.",
      "Why it is a macro objective: GDP growth can use up resources and damage the environment, and costs fall on future generations, so the whole economy's path matters.",
      "Conflicts: tough environmental policy may raise costs and prices, reduce growth or jobs in some industries in the short run, and may hit poorer households.",
      "Evaluation: green investment may create jobs and long-run growth, so the conflict may be temporary."],
     "Define. Why macro. Two conflicts. One reason the conflict may be smaller than it looks.",
     [[("k", "Sustainability means economic growth that meets the needs of the present without reducing the ability of future generations to meet their own needs."), ("n", "It is a macroeconomic objective because GDP growth can use up non-renewable resources and cause pollution and climate change, and the costs of this fall on future generations and on the economy as a whole. A government that only targets growth may raise output today by reducing productive potential tomorrow.")],
      [("n", "Sustainability could conflict with other objectives. A carbon tax raises production costs and prices in energy-intensive industries, which could raise inflation and reduce output and jobs in the short run, so it may conflict with the aims of low unemployment and growth. The costs of higher energy prices also fall more heavily on poorer households, which conflicts with the aim of a fairer distribution of income."), ("e", "However, investment in renewable energy and efficiency could create jobs and raise productivity over time, so the conflict may be smaller in the long run than in the short run.")]])
  ],
  )

tips = tips_html(
  [("List the objectives with their indicators.", "Inflation (CPI), unemployment rate, real GDP growth, current account, HDI, emissions, Gini."),
   ("Use numbers.", "Compare data to a target: 'inflation of 1.8% is close to the 2% target'."),
   ("Say objectives are linked.", "A tool aimed at one objective affects the others. This sets up a conflict or a benefit."),
   ("Priorities change.", "In a deep recession jobs and growth first. With high inflation, price stability first. Developing economies often put development first."),
   ("Name the tool.", "Fiscal, monetary, supply-side, exchange rate or trade policy, matched to the objective."),
   ("Include the newer objectives.", "Development, sustainability and distribution are on the syllabus list. Mention at least one when the question allows."),
   ("Separate growth from development.", "Growth is a rise in real GDP. Development covers health, education and living standards.")],
  [("Define", "Price stability means keeping the rate of inflation low and stable, usually close to a target such as 2%."),
   ("Link", "Policies aimed at one objective may help or harm another, for example higher interest rates may reduce inflation but also slow growth."),
   ("Priority", "In a deep recession a government may give priority to reducing unemployment because there is spare capacity and little inflation risk."),
   ("Develop", "Economic growth does not guarantee development, because the gains may not reach poorer households."),
   ("Judge", "Which objective matters most depends on the state of the economy and its level of development.")],
  [CW["define"], CW["explain"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- Radar helpers ---------- */
const NAMES = ["Price stability", "Employment", "Growth", "Current account", "Sustainability", "Equity"];
const CX0 = 380, CY0 = 175, RR = 125;
const pt = (i, v) => { const a = -Math.PI / 2 + i * Math.PI / 3; return [CX0 + Math.cos(a) * RR * v / 10, CY0 + Math.sin(a) * RR * v / 10]; };
function radarPoly(vals, cls, v) { return SV.poly(vals.map((x, i) => pt(i, x)), cls, { opacity: v, stroke: "var(--ink)", "stroke-width": 2 }); }
function radarGrid() { let o = ""; [10, 7.5, 5, 2.5].forEach((l) => (o += `<polygon points="${[0, 1, 2, 3, 4, 5].map((i) => pt(i, l).join(",")).join(" ")}" fill="none" stroke="var(--line)" stroke-width="1"/>`)); NAMES.forEach((n, i) => { const p = pt(i, 10), q = pt(i, 11.8); o += SV.line(CX0, CY0, p[0], p[1], "gr") + SV.text(q[0], q[1] + 4, n, "lbl bd", { "text-anchor": i === 0 || i === 3 ? "middle" : i < 3 ? "start" : "end" }); }); return o; }
const A = [9, 8, 5, 6, 4, 3], B = [5, 4, 9, 3, 3, 5];
$("#pic1").innerHTML = `<svg viewBox="0 0 760 350" role="img" aria-label="Radar diagram with six macroeconomic objectives: price stability, employment, growth, current account, sustainability and equity">${radarGrid()}${radarPoly([10, 10, 10, 10, 10, 10], "f3", 0.15)}${tag(380, 340, "outer edge = objective fully met", "t3", 1, "middle")}</svg>`;
function radDraw(s) { let o = radarGrid() + radarPoly([10, 10, 10, 10, 10, 10], "f3", 0.12 * s.t); o += radarPoly(A.map((x) => x * s.a), "f1", 0.35 * s.a) + radarPoly(B.map((x) => x * s.b), "f4", 0.35 * s.b); if (s.a > 0) o += tag(40, 40, "Country A", "t1", s.a); if (s.b > 0) o += tag(40, 62, "Country B", "t4", s.b); return o; }
Lib.stepper($("#stR"), { w: 760, h: 350, label: "Radar chart comparing two economies against macroeconomic objectives", base: { t: 0, a: 0, b: 0 }, draw: radDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>The ideal.</b> Six objectives: price stability, employment, growth, the current account, sustainability and equity. The outer edge means the objective is fully met. No real economy fills the whole shape.", s: { t: 1 } },
  { cap: "<b>Country A.</b> Stable prices and high employment, but modest growth, a weak current account and poor scores on sustainability and equity. It is a mature, ageing economy.", s: { t: 1, a: 1 } },
  { cap: "<b>Country B.</b> Very fast growth, but higher inflation and unemployment, a large current account deficit and weaker sustainability. It is a fast-growing emerging economy.", s: { t: 1, a: 1, b: 1 } },
  { cap: "<b>Trade-offs.</b> Neither country meets every objective, and the shapes show different priorities. Pursuing one objective, such as growth, often costs another, such as the current account or sustainability.", s: { t: 1, a: 0.6, b: 1 } },
] });

/* ---------- Watch 2: inflation target ---------- */
const IQ = [1.8, 2.1, 2.6, 3.4, 4.5, 5.6, 5.9, 5.1, 4.0, 3.0, 2.3, 2.0], IX = (q) => 90 + q * 55, IY = (v) => 300 - v * 36;
function infDraw(s) {
  let o = axes(70, 300, 740, 30, "Quarter", "Inflation (%)") + SV.rect(70, IY(3), 660, IY(1) - IY(3), "f3", op(0.4)) + tag(726, IY(3) + 16, "target band 1% to 3%", "t3", 1, "end");
  [0, 2, 4, 6].forEach((v) => (o += SV.text(64, IY(v) + 4, v, "sm", { "text-anchor": "end" })));
  const n = Math.round(s.n), pts = IQ.slice(0, n).map((v, i) => [IX(i), IY(v)]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c2"); pts.forEach((p) => (o += SV.circle(p[0], p[1], 4, "dot2")));
  if (s.a > 0) o += tag(IX(5), IY(6.9), "inflation overshoots", "t2", s.a, "middle");
  if (s.b > 0) o += tag(IX(7.5), IY(5.9), "interest rates raised", "t1", s.b, "middle");
  if (s.c > 0) o += tag(IX(10.5), IY(3.6), "back in the band", "t3", s.c, "middle");
  return o;
}
Lib.stepper($("#stI"), { w: 760, h: 345, label: "Inflation rising above a target band and returning after policy tightening", base: { n: 1, a: 0, b: 0, c: 0 }, draw: infDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>On target.</b> Inflation is inside the 1% to 3% band. Price stability is met.", s: { n: 3 } },
  { cap: "<b>Overshoot.</b> Demand and costs push inflation up to almost 6%, far outside the band. Price stability is failing.", s: { n: 7, a: 1 } },
  { cap: "<b>Policy response.</b> The central bank raises interest rates to reduce demand. Inflation is slow to fall because of time lags, and growth and employment may suffer.", s: { n: 9, a: 1, b: 1 } },
  { cap: "<b>Back in the band.</b> Inflation returns to about 2%. The cost: slower growth and higher unemployment for a time, which shows how objectives conflict.", s: { n: 12, a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1: scorecard ---------- */
function labScore() {
  if (!$("#in") || !$("#un") || !$("#gr") || !$("#ca")) return;
  const inf = +$("#in").value / 10, un = +$("#un").value / 10, gr = +$("#gr").value / 10, ca = +$("#ca").value / 10;
  const rows = [["Inflation", inf, 1, 3, "price stability"], ["Unemployment", un, 0, 5, "low unemployment"], ["Growth", gr, 2, 4, "growth"], ["Current account", ca, -3, 3, "balance of payments"]];
  const ok = rows.map((r) => r[1] >= r[2] && r[1] <= r[3]), met = ok.filter(Boolean).length;
  const dist = rows.map((r) => (r[1] < r[2] ? r[2] - r[1] : r[1] > r[3] ? r[1] - r[3] : 0)), worst = dist.indexOf(Math.max(...dist));
  $("#r1").textContent = met + " of 4"; $("#r2").textContent = met === 4 ? "None" : rows[worst][0]; $("#r3").textContent = Lib.fmtN(inf + un, 1);
  $("#rv").textContent = met === 4 ? "All four indicators are inside their target ranges. This is the ideal, and it is rare." : `${met} of 4 objectives are met. The biggest miss is ${rows[worst][0].toLowerCase()} (${Lib.fmtN(rows[worst][1], 1)}${worst === 3 ? "% of GDP" : "%"}). Policy aimed at it may affect the other objectives: check for a conflict before choosing the tool.`;
  const X = (v, lo, hi) => 120 + (v - lo) / (hi - lo) * 260; let o = "";
  const ranges = [[-2, 10], [0, 16], [-6, 10], [-12, 8]];
  rows.forEach((r, i) => { const y = 40 + i * 62, [lo, hi] = ranges[i]; o += SV.line(120, y, 380, y, "gr") + SV.rect(X(r[2], lo, hi), y - 12, X(r[3], lo, hi) - X(r[2], lo, hi), 24, "f3", { opacity: 0.55 }) + SV.circle(X(Math.max(lo, Math.min(hi, r[1])), lo, hi), y, 8, ok[i] ? "dot3" : "dot2") + SV.text(10, y + 4, r[0], "lbl bd") + SV.text(400, y + 4, ok[i] ? "met" : "missed", "sm bd", { "text-anchor": "end" }); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "in", label: "Inflation (%) ", min: -10, max: 100, step: 5, value: 20, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labScore });
Lib.slider($("#g2"), { id: "un", label: "Unemployment (%) ", min: 20, max: 150, step: 5, value: 50, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labScore });
Lib.slider($("#g3"), { id: "gr", label: "Real GDP growth (%) ", min: -50, max: 80, step: 5, value: 25, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labScore });
Lib.slider($("#g4"), { id: "ca", label: "Current account (% GDP) ", min: -100, max: 60, step: 5, value: 0, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labScore });
labScore();
btnTable("lbBtns", "lbOut", [
  ["Deep recession, inflation near zero", "Unemployment and growth", "There is spare capacity and little inflation risk, so demand stimulus carries few costs."],
  ["Inflation at 9% with a positive output gap", "Price stability", "High inflation erodes savings and competitiveness, and tighter policy is needed even at some cost to growth."],
  ["Low-income country with widespread poverty", "Growth and development", "Raising incomes and living standards matters most, and GDP growth must reach poorer households."],
  ["Large persistent current account deficit and falling reserves", "Balance of payments", "Borrowing cannot continue indefinitely, so policy must improve competitiveness or cut spending on imports."],
  ["Rapid growth with severe pollution", "Sustainability", "Growth that destroys natural capital reduces future potential, so environmental policy takes priority."],
  ["Record inequality and rising poverty", "Redistribution", "Equity concerns and social stability call for tax and benefit policy and investment in skills."]
], ["Situation", "Likely priority", "Why"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which objective does the indicator mainly measure?", ["Price stability", "Employment", "Growth", "Balance of payments", "Distribution / development"],
  [("Consumer price index", 0), ("Claimant count and unemployment rate", 1), ("Annual change in real GDP", 2), ("Balance on trade in goods and services", 3), ("Gini coefficient", 4), ("Human Development Index", 4), ("Core inflation rate", 0), ("Participation rate and employment rate", 1)],
  "Match each indicator to the objective it shows.") + MATCH([
  ["Price stability", "Low and stable inflation"],
  ["Full employment", "Everyone willing and able to work can find a job"],
  ["Current account stability", "No large persistent deficit or surplus"],
  ["Sustainability", "Growth that does not reduce future productive potential"],
  ["Redistribution", "A fairer spread of income and wealth through tax and benefits"],
  ["Misery index", "Inflation rate plus unemployment rate"]]) + ORDER(
  "Put the policy-making cycle in order.",
  ["Identify the problem from the indicators", "Set a target for the objective", "Choose a tool: fiscal, monetary, supply-side, exchange rate or trade", "Implement the policy", "Monitor the results and adjust"],
  "Policy is a loop: results feed back into the next decision.") + CALC([
  {"q": "The consumer price index rises from 120 to 123.6 in a year. Calculate the inflation rate (%).", "a": 3, "unit": "%", "tol": 0.05, "hint": "Change ÷ original × 100.", "sol": "3.6 ÷ 120 × 100 = <b>3%</b>."},
  {"q": "Inflation is 4.5% and unemployment is 6.5%. Calculate the misery index.", "a": 11, "tol": 0.05, "hint": "Add the two rates.", "sol": "4.5 + 6.5 = <b>11</b>."},
  {"q": "A country's exports of goods and services are $180bn, imports are $200bn and GDP is $1,000bn. Calculate the balance on trade in goods and services as a percentage of GDP.", "a": -2, "unit": "%", "tol": 0.05, "hint": "(X − M) ÷ GDP.", "sol": "(180 − 200) ÷ 1000 × 100 = <b>−2%</b>, a deficit."},
  {"q": "Nominal GDP rises by 6% and inflation is 2.5%. Calculate the approximate rate of real growth (%).", "a": 3.5, "unit": "%", "tol": 0.05, "hint": "Nominal growth minus inflation.", "sol": "6 − 2.5 = <b>3.5%</b>."}]) + MCQ([
  ("Which is an indicator of price stability?", ["The Gini coefficient", "The consumer price index", "The HDI", "The current account balance"], 1, "The CPI measures changes in the price level."),
  ("Why may sustainability conflict with short-run growth?", ["Environmental policy may raise costs and reduce output in some industries", "It always raises unemployment", "It has no link to production", "It reduces inflation"], 0, "Pollution controls and carbon taxes raise costs, which can cut output in the short run."),
  ("Which objective is most likely to come first in a deep recession?", ["Reducing inflation from 2%", "Reducing unemployment and raising growth", "Reducing the budget surplus", "Raising the exchange rate"], 1, "Spare capacity means demand policy has few costs."),
  ("Which objective is separate from growth?", ["Economic development", "Real GDP", "Production", "National income"], 0, "Development covers health, education and living standards as well as income."),
  ("A government cuts taxes to raise growth and this increases imports. Which objective could be harmed?", ["Current account balance", "The unemployment rate", "Population", "Resource base"], 0, "Higher incomes raise spending on imports and worsen the current account.")
], "qz1") + CARDS([
  ("Price stability", "Low, stable inflation (target often 2%)."),
  ("Full employment", "Everyone willing and able can find a job at the going wage."),
  ("Economic growth", "Rise in real GDP over time."),
  ("Current account stability", "No large persistent deficit or surplus."),
  ("Economic development", "Improved living standards: income, health, education."),
  ("Sustainability", "Growth without reducing future potential."),
  ("Redistribution", "Tax and benefit changes to spread income more fairly."),
  ("Misery index", "Inflation rate plus unemployment rate.")]) + MCQ(mc_exam)

build("sy1011", "macroeconomic-policy-objectives", "Government Macroeconomic Policy Objectives", EY,
  "10.1.1: the objectives governments set for inflation, unemployment, growth, the balance of payments, development, sustainability and redistribution, their indicators and targets, and why priorities differ. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
