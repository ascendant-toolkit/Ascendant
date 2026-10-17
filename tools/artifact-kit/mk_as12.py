"""AS syllabus 1.2.1-1.2.4 Economic methodology. Run: python3 tools/artifact-kit/mk_as12.py"""
from asx import *
EY = EYAS("1.2.1 to 1.2.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Economics is a <b class="kw">social science</b>: it studies human behaviour using <b>models and evidence</b>, but it cannot run controlled laboratory experiments, so results are tendencies rather than laws. A <b class="kw">positive statement</b> is about facts and can be <b>tested with evidence</b> (it may be true or false), whereas a <b class="kw">normative statement</b> is a <b>value judgement or opinion</b> about what ought to be and cannot be settled by facts alone. <b class="kw">Ceteris paribus</b> means <b>"all other things being equal"</b>: economists change one variable at a time to isolate its effect. The <b class="kw">time period</b> matters: in the <b>short run</b> at least one factor is fixed, in the <b>long run</b> all factors can be varied, and in the <b>very long run</b> technology and other conditions can change.</p></div>

  <h2>1 · Economics as a social science (1.2.1)</h2>
  <ul>
    <li><b>Science</b> means building theories, testing them against evidence and revising them. Economics does this with data and models.</li>
    <li><b>Social</b> means the subject is human behaviour, which is varied and changes over time, so economists cannot control the conditions as in a laboratory.</li>
    <li>Economists therefore use <b>models</b>: simplified descriptions of reality that rely on <b>assumptions</b> (such as ceteris paribus and rational behaviour). Models are useful if they predict well, but the assumptions limit them.</li>
    <li>Results are <b>probabilities and tendencies</b>, not laws. For example, "a rise in price will reduce demand" is usually true but not in every case.</li>
  </ul>

  <h2>2 · Positive and normative statements (1.2.2)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Positive statement</th><th>Normative statement</th></tr>
    <tr><td><b>About</b></td><td>What is, was or will be: <b>facts</b> and cause and effect</td><td>What <b>ought</b> to be: <b>opinions and value judgements</b></td></tr>
    <tr><td><b>Can it be tested?</b></td><td>Yes, with data and evidence. It can be <b>true or false</b></td><td>No: it depends on values. People can reasonably disagree</td></tr>
    <tr><td><b>Typical words</b></td><td>is, was, will, increases, causes, fell, rose, "if ... then"</td><td>should, ought, fair, unfair, better, worse, best, "too high", must</td></tr>
    <tr><td><b>Example</b></td><td>"Unemployment rose from 5% to 6% last year"</td><td>"The government should reduce unemployment even if it raises inflation"</td></tr>
  </table></div>
  <ul>
    <li>A positive statement can be <b>wrong</b>: "A rise in the minimum wage will have no effect on employment" is positive even if the evidence shows it is false. What makes it positive is that it can be tested.</li>
    <li>A statement that mixes both is <b>normative</b> if it contains a value judgement. To turn a normative statement into a positive one, remove the value word: "the government should cut tax" becomes "cutting tax will raise disposable income".</li>
    <li>Economists use positive economics to explain and predict, and normative economics to recommend policy. Policy choices combine facts with values, which is why economists disagree.</li>
  </ul>

  <h2>3 · Ceteris paribus (1.2.3)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Ceteris paribus</b> is Latin for "other things being equal". An economist changes one variable and holds all the others constant, so the effect of that one variable can be seen.</li>
    <li>For example, the <b>demand curve</b> shows how the quantity demanded changes as the price changes, ceteris paribus. Income, tastes, the prices of related goods and expectations are held constant. A change in price causes a movement along the curve; a change in one of the others shifts the whole curve.</li>
    <li>Without the assumption you cannot tell which variable caused a change. If the price rises 5% and the quantity demanded rises 3% while consumers' incomes rise 4%, the law of demand has not been broken: <b>other things did not remain equal</b>, because the income rise shifted the demand curve.</li>
    <li><b>Limitations:</b> in real life other things rarely stay equal, so predictions based on ceteris paribus are approximate.</li>
  </ul>

  <h2>4 · The importance of the time period (1.2.4)</h2>
  <div class="tw"><table class="t">
    <tr><th>Time period</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Short run</b></td><td>At least one factor of production is <b>fixed</b>; firms can change only variable factors such as labour and materials</td><td>A bakery can hire extra staff but cannot build a new oven</td></tr>
    <tr><td><b>Long run</b></td><td>All factors of production can be varied, but the state of <b>technology</b> is fixed</td><td>The bakery can build a bigger factory and buy more machines</td></tr>
    <tr><td><b>Very long run</b></td><td>All factors can be varied and <b>technology</b> and other conditions can change</td><td>New production methods and automation are developed</td></tr>
  </table></div>
  <ul>
    <li>Time matters because <b>elasticities and responses differ</b>: the price elasticity of supply is higher in the long run, so a price rise brings a bigger increase in the quantity supplied. Demand also tends to be more elastic in the long run as consumers find substitutes.</li>
    <li>Policies and shocks have <b>different effects</b> in the short and long run: a tax rise may cut demand a little at first and more later.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>When classifying a statement, ask "<b>could I test this with data?</b>" If yes it is positive, even if it might be false. If it depends on what someone thinks is right or fair, it is normative.</div>
'''

watch = '''
  <h2>1 · Positive or normative?</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stP"></div>
  <h2>2 · Why ceteris paribus matters</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Test a positive statement, not a normative one</h2>
  <p>Enter the unemployment rate in two years. The positive statement can be checked against the data. The normative statement depends on your view of what is acceptable.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Positive: "unemployment fell"</small><strong id="r1"></strong></div><div><small>Normative: "it is too high"</small><strong id="r2"></strong></div><div><small>Settled by data?</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars for the unemployment rate in two years and a line for the acceptable rate chosen by the viewer"></svg></div></div></div>

  <h2>Lab 2 · The time period and supply</h2>
  <p>The price of a good rises. The price elasticity of supply is low in the short run and higher in the long run. Set the price rise and the two elasticities, starting from a supply of 100,000 units.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div><div id="g6"></div>
    <div class="readout"><div><small>Short run</small><strong id="t1"></strong></div><div><small>Long run</small><strong id="t2"></strong></div><div><small>Extra from waiting</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars of the quantity supplied now, in the short run and in the long run after a price rise"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Positive or normative?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the steps for checking a statement in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Minimum wage debates", "Economists can test whether a minimum wage reduces employment by studying data from different regions. That is positive economics. Whether the minimum wage should be raised depends on how much weight people give to the incomes of low-paid workers against possible job losses, which is normative.", "the difference between testing a claim and making a policy judgement.") +
rw("Why fuel prices respond slowly", "When the price of oil rises sharply, producers cannot increase output much in the short run because wells and refineries take years to build. In the long run, new fields and methods increase supply a lot, so the price effect fades.", "the importance of the time period and how elasticities differ.") +
rw("Ice cream and the weather", "An economist who studies the effect of a price change on ice cream sales has to hold the weather, incomes and the price of other desserts constant. If a hot summer lifts demand while the price rises, the observed sales do not show the effect of the price alone.", "ceteris paribus and why real-world data can be misleading.") +
rw("Forecasts that miss", "Central banks and governments publish economic forecasts based on models with many assumptions. When an unexpected event such as a pandemic occurs, the forecasts can be far off. This is a reminder that economics is a social science with probabilities, not exact laws.", "economics as a social science and the limits of models.")
)

mc_exam = [
  mcq("m20_12", 3, "A newspaper article says: 1. The burden of tax should be shifted more to the highest earners. 2. It is in the public interest that key services are nationalised. Which type of statement is each?", ["Both normative", "1 normative, 2 positive", "1 positive, 2 normative", "Both positive"], 0, "Both contain value judgements ('should', 'in the public interest'), so both are normative."),
  mcq("m21_12", 4, "Which statement is a positive statement?", ["The distribution of income and wealth in most western European countries is unequal", "The government ought to increase income tax on high earners", "There should be more legal rights for workers", "Wages of those on low incomes should be increased"], 0, "It describes a fact that can be tested. The others use 'ought' and 'should'."),
  mcq("m24_12", 2, "Which statement is a normative statement?", ["Aggregate demand will increase following a fall in interest rates", "A rise in unemployment will decrease inflationary pressures", "The incentive to work will rise if benefit payments are reduced", "Unsustainable economic growth is more harmful to the economy than hyperinflation"], 3, "Judging what is 'more harmful' is a value judgement. The others are predictions that can be tested."),
  mcq("s21_11", 1, "In 2015 the Chinese economy grew by 6.9%, India's by 7.6% and the US by 2.4%. Which comment contains two positive statements?", ["Chinese growth exceeded US growth by 4.5% in 2015 but was 0.7% less than India's", "Chinese growth was more than double the US's but disappointing compared with India's", "India's growth was better than that of the US", "US growth was too low in 2015 and India's was too high"], 0, "Both parts of the first comment are facts that can be checked against the figures. 'Disappointing', 'better' and 'too low' are value judgements."),
  mcq("s22_12", 1, "Which list has the most words that are likely to relate to a positive statement rather than a normative one?", ["Describe, better, should, value, emotion", "Bias, objective, ought, opinion, tastes", "Contestable, is, motive, subjective, moral", "Actual, ethics, fact, was, testable"], 3, "Words such as actual, fact, was and testable point to positive statements; should, ought, better and moral point to normative ones."),
  mcq("s21_11", 4, "What does the phrase 'ceteris paribus' mean?", ["All the resources used are of equal quality", "Everything else remains unchanged", "The price mechanism rations scarce goods", "The variable under consideration is held constant"], 1, "It means all other things are held equal. Option D is the opposite: it is the variable studied that changes."),
  mcq("m22_12", 7, "Demand curves are drawn ceteris paribus. Which 'other things' are not required to remain the same when an individual's demand curve for ice cream is constructed?", ["The consumer's income", "The consumer's tastes and preferences", "The price of fresh fruit", "The price of ice cream"], 3, "The price of ice cream is the variable on the vertical axis and is allowed to change. Everything else is held constant."),
  mcq("m25_12", 4, "The price of a good rises by 5% and the quantity demanded rises by 3%. At the same time, consumers' incomes rise by 4%. The law of demand appears not to be working. What is the most likely explanation?", ["Other things did not remain equal", "The demand for the good was price inelastic", "The real price of the good fell", "The time period was the very short run"], 0, "The rise in income shifted the demand curve, so ceteris paribus did not hold."),
  mcq("m23_12", 2, "What is the definition of the long run?", ["The time period when all factors of production are specialised", "The time period when all factors of production are variable", "The time period when all key inputs are variable and technology can change", "The time period when at least one factor of production is fixed"], 1, "In the long run all factors of production can be varied. In the short run at least one is fixed."),
  mcq("m21_12", 3, "What distinguishes the very long run from the long run?", ["The ability to change resource allocation", "The ability to change the state of technology", "The absence of government market intervention", "The existence of variable factors of production"], 1, "In the very long run technology can change, whereas it is fixed in the long run."),
  mcq("m25_12", 2, "To increase production, a firm in industry X needs to install capital equipment, while a firm in industry Y needs to research and introduce new technology. What time periods are illustrated?", ["Short run for X, long run for Y", "Long run for both", "Long run for X, very long run for Y", "Very long run for both"], 2, "Installing equipment means varying a factor of production (long run). Introducing new technology is a change in technology (very long run)."),
  mcq("s23_11", 7, "When the price of good X is $2.00, the quantity supplied is 100,000. The price elasticity of supply is 0.8 in the short run and 1.4 in the long run. The price rises to $2.20. What is the increase in the quantity supplied between the short run and the long run?", ["6,000", "60,000", "114,000", "140,000"], 0, "A 10% price rise gives +8% (108,000) in the short run and +14% (114,000) in the long run: a difference of 6,000.")
]

exam = exam_page("economic methodology: positive and normative statements, ceteris paribus and time periods",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Positive and normative statements, ceteris paribus and the time period are tested almost entirely in Paper 1, with one or more questions on them in most series, and they support the written answers in Paper 2. No full Paper 2 question was found on this part, so two practice questions in the Paper 2 style are included, with twelve Paper 1 multiple choice questions.",
  [("Paper 2 (no stand-alone question found)", "0", "Practice questions below"), ("Multiple choice (Paper 1)", "12 shown below", "2020 to 2025")],
  [
  eq("Practice question · modelled on the 4 mark style (no past paper)", "4 marks", "Distinguish between a positive statement and a normative statement, giving an example of each.",
     ["Positive: a statement of fact that can be tested with evidence and may be true or false (1); example, such as 'a rise in the minimum wage reduced employment by 2%' (1).",
      "Normative: a value judgement or opinion that cannot be settled by facts (1); example, such as 'the minimum wage should be raised' (1)."],
     "Two definitions with the key difference (testable or not). One example of each.",
     [[("k", "A positive statement is about facts and can be tested with evidence, so it can be shown to be true or false, for example 'unemployment rose from 5% to 6%'. A normative statement is a value judgement about what ought to be, for example 'the government should reduce unemployment'. It cannot be proved or disproved by data because it depends on opinion.")]]),
  eq("Practice question · modelled on the 8 mark style (no past paper)", "8 marks", "Explain what economists mean by ceteris paribus and consider whether the assumption makes economic models useful.",
     ["Knowledge (3): ceteris paribus means all other things being equal; one variable is changed while the others are held constant; an example such as the demand curve.",
      "Analysis (3): it isolates the effect of one variable; a movement along a curve is caused by a price change and a shift by a change in a variable that was held constant; without the assumption cause and effect cannot be separated.",
      "Evaluation (2): in reality other things rarely stay equal, so predictions are approximate; models are still useful as a starting point; reach a conclusion."],
     "Define with an example. Why economists use it. The limit: real life changes many things at once. Judge.",
     [[("k", "Ceteris paribus means all other things being equal. For example, when drawing a demand curve an economist changes the price and holds income, tastes and the prices of other goods constant, so that the effect of price on quantity demanded is isolated."), ("n", "This makes models useful because it lets economists see cause and effect. A change in the price causes a movement along the demand curve, whereas a change in income, which was held constant, causes the whole curve to shift. Without the assumption it would be impossible to say which variable caused a change in demand.")], [("e", "However, in the real world other things rarely stay equal. If the price of a good rises while incomes also rise, the quantity demanded may rise, so a model based on ceteris paribus could mislead. Models are therefore useful as a starting point, but predictions are approximate and the assumption needs to be checked against the data.")]])
  ],
  )

tips = tips_html(
  [("Ask 'can it be tested?'", "If data could show it is true or false it is positive. If it depends on opinion it is normative."),
   ("Spot the value words.", "Should, ought, fair, better, too high: normative."),
   ("Positive can be wrong.", "A false prediction is still a positive statement."),
   ("Define ceteris paribus with an example.", "All other things equal, with demand as the example."),
   ("Say what is held constant.", "Income, tastes, prices of related goods and expectations."),
   ("Give the three time periods.", "Short run: one fixed factor. Long run: all factors variable. Very long run: technology can change."),
   ("Link time to elasticity.", "Supply and demand are usually more elastic in the long run.")],
  [("Positive", "This is a positive statement because it can be tested against data to see whether it is true."),
   ("Normative", "This is a normative statement because it contains a value judgement about what should happen."),
   ("Ceteris paribus", "Ceteris paribus allows economists to isolate the effect of price by holding other variables constant."),
   ("Limit", "In reality other things might not remain equal, so the prediction may not hold."),
   ("Time", "In the long run all factors of production can be varied, so supply may be more elastic.")],
  [CW["define"], CW["explain"], CW["consider"], CW["evaluate"]]) + FC

js = '''
/* ---------- positive / normative ---------- */
const STM = [["The government should cut income tax", "normative", "should"], ["Cutting income tax raises disposable income", "positive", "raises"], ["Unemployment fell from 6% to 5% last year", "positive", "fell"], ["The minimum wage is unfair to small firms", "normative", "unfair"]];
function pnDraw(s) {
  let o = ""; STM.forEach(([t, kind, cue], i) => { const k = Math.max(0, Math.min(1, s.i - i)); if (k <= 0) return; const y = 20 + i * 70, c = kind === "positive" ? "f3" : "f2", cueOn = s.c > i; o += SV.rect(30, y, 540, 50, "f1", op(0.25 * k)) + SV.text(46, y + 31, t, "lbl", op(k));
    if (cueOn) { const w = t.split(" "), idx = w.findIndex((x) => x.toLowerCase().startsWith(cue)); o += SV.rect(40 + w.slice(0, idx).join(" ").length * 8.4 + (idx ? 6 : 0), y + 10, cue.length * 8.8 + 6, 30, "f2", { opacity: 0.25 * k, rx: 4 }); }
    if (s.l > i) o += SV.rect(590, y + 6, 140, 38, c, op(0.7)) + SV.text(660, y + 31, kind === "positive" ? "POSITIVE: testable" : "NORMATIVE: opinion", "lbl bd", { "text-anchor": "middle" }); });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Four statements labelled positive or normative">${pnDraw({ i: 4, c: 4, l: 4 })}</svg>`;
Lib.stepper($("#stP"), { w: 760, h: 300, label: "Four statements classified as positive or normative", base: { i: 0, c: 0, l: 0 }, draw: pnDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>A value word.</b> 'The government <u>should</u> cut income tax' contains 'should'. Nobody can prove with data that it ought to happen, so it is a value judgement.", s: { i: 1, c: 1, l: 1 } },
  { cap: "<b>A testable claim.</b> 'Cutting income tax raises disposable income' is a cause-and-effect claim that can be checked against data. It is positive.", s: { i: 2, c: 2, l: 2 } },
  { cap: "<b>A fact.</b> 'Unemployment fell from 6% to 5%' can be checked. It is positive, even if the figures turn out to be wrong.", s: { i: 3, c: 3, l: 3 } },
  { cap: "<b>Another value judgement.</b> 'Unfair' depends on what someone believes is fair, so it is normative.", s: { i: 4, c: 4, l: 4 } },
] });

/* ---------- ceteris paribus ---------- */
const CX = (q) => 70 + (q - 60) * 6.6, CY = (p) => 300 - (p - 56) * 3.1;
function cpDraw(s) {
  let o = SV.line(70, 300, 730, 300) + SV.line(70, 300, 70, 30) + SV.text(730, 326, "Quantity demanded", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price", "sm");
  const d = (sh) => [[CX(60), CY(140 + sh)], [CX(140), CY(60 + sh)]];
  o += SV.line(...d(0)[0], ...d(0)[1], "c1") + tag(CX(138), CY(62) + 22, "D₀", "t1", 1, "end");
  if (s.sh > 0.01) o += SV.line(...d(8 * s.sh)[0], ...d(8 * s.sh)[1], "c3") + tag(CX(140) + 6, CY(60 + 8 * s.sh) + 4, "D₁", "t3", 1, "start");
  o += SV.circle(CX(100), CY(100), 7, "dot1") + tag(CX(100) + 10, CY(100) + 20, "A  (P 100, Q 100)", "t1");
  if (s.m > 0) o += SV.circle(CX(100 - 5 * s.m), CY(100 + 5 * s.m), 7, "dot2") + tag(CX(100 - 5 * s.m) - 10, CY(100 + 5 * s.m) - 12, s.m > 0.9 ? "B  (P 105, Q 95)" : "", "t2", 1, "end");
  if (s.sh > 0.5) o += SV.circle(CX(95 + 8 * s.sh), CY(105), 7, "dot4") + tag(CX(95 + 8 * s.sh) + 10, CY(105) - 12, s.sh > 0.9 ? "C  observed (P 105, Q 103)" : "", "t4");
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 345, label: "Price up 5 percent along a demand curve, then an income rise shifting demand so that quantity demanded rises 3 percent", base: { sh: 0, m: 0 }, draw: cpDraw, tween: 1100, dwell: 5800, steps: [
  { cap: "<b>Start.</b> At a price of 100 the quantity demanded is 100 (point A on the demand curve D₀).", s: { sh: 0, m: 0 } },
  { cap: "<b>Ceteris paribus.</b> The price rises 5% and everything else is held constant. We move up D₀ to B: the quantity demanded falls to 95.", s: { sh: 0, m: 1 } },
  { cap: "<b>But other things change.</b> Incomes rise 4%, which shifts the demand curve right to D₁. At the new price the quantity demanded is now 103.", s: { sh: 1, m: 1 } },
  { cap: "<b>The observed result</b> (price +5%, quantity +3%) looks as if the law of demand has failed, but it has not. Other things did not remain equal.", s: { sh: 1, m: 1 } },
] });
$("#pic2").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="A demand curve and a shifted demand curve showing why other things must be held equal">${cpDraw({ sh: 1, m: 1 })}</svg>`;

/* ---------- Lab 1 ---------- */
function labS() {
  if (!$("#u0") || !$("#u1") || !$("#ac")) return;
  const a = +$("#u0").value / 10, b = +$("#u1").value / 10, ac = +$("#ac").value / 10;
  $("#r1").textContent = b < a ? "TRUE" : b > a ? "FALSE" : "FALSE (no change)"; $("#r2").textContent = b > ac ? "Agrees (for this view)" : "Disagrees (for this view)"; $("#r3").textContent = "Positive: yes. Normative: no";
  $("#rv").textContent = `Unemployment moved from ${a.toFixed(1)}% to ${b.toFixed(1)}%. The positive statement 'unemployment fell' is ${b < a ? "true" : "false"}: the data decide it. The normative statement 'unemployment is too high' is true only for someone who thinks ${ac.toFixed(1)}% is acceptable; another person may choose a different level, and no data can tell you which view is right.`;
  const Y = (v) => 270 - v * 20; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(46, 22, "Unemployment rate, %", "sm");
  [["Year 1", a, "f1"], ["Year 2", b, "f3"]].forEach(([l, v, c], i) => { const x = 80 + i * 130; o += SV.rect(x, Y(v), 80, 270 - Y(v), c, op(0.75)) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, Y(v) - 6, v.toFixed(1) + "%", "t1", 1, "middle"); });
  o += SV.line(40, Y(ac), 400, Y(ac), "c2 dash") + tag(396, Y(ac) - 6, "your 'acceptable' rate " + ac.toFixed(1) + "%", "t2", 1, "end");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "u0", label: "Unemployment, year 1, % ", min: 20, max: 120, step: 1, value: 60, fmt: (v) => (v / 10).toFixed(1), onInput: labS });
Lib.slider($("#g2"), { id: "u1", label: "Unemployment, year 2, % ", min: 20, max: 120, step: 1, value: 50, fmt: (v) => (v / 10).toFixed(1), onInput: labS });
Lib.slider($("#g3"), { id: "ac", label: "The rate YOU think is acceptable, % ", min: 20, max: 120, step: 1, value: 40, fmt: (v) => (v / 10).toFixed(1), onInput: labS });
labS();

/* ---------- Lab 2 ---------- */
function labT() {
  if (!$("#pr") || !$("#e1") || !$("#e2")) return;
  const pr = +$("#pr").value, e1 = +$("#e1").value / 10, e2 = +$("#e2").value / 10, base = 100000, sr = base * (1 + e1 * pr / 100), lr = base * (1 + e2 * pr / 100);
  $("#t1").textContent = Math.round(sr).toLocaleString("en-US"); $("#t2").textContent = Math.round(lr).toLocaleString("en-US"); $("#t3").textContent = "+" + Math.round(lr - sr).toLocaleString("en-US");
  $("#tv").textContent = `A ${pr}% price rise with a short-run price elasticity of supply of ${e1.toFixed(1)} raises the quantity supplied by ${Lib.fmtN(e1 * pr, 1)}% to ${Math.round(sr).toLocaleString("en-US")}. In the long run, with an elasticity of ${e2.toFixed(1)}, supply rises ${Lib.fmtN(e2 * pr, 1)}% to ${Math.round(lr).toLocaleString("en-US")}. Firms can adjust more as time passes, so the response is bigger.`;
  const Y = (v) => 270 - (v - 90000) / 40000 * 220; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(46, 22, "Quantity supplied", "sm");
  [["Before", base, "f1"], ["Short run", sr, "f2"], ["Long run", lr, "f3"]].forEach(([l, v, c], i) => { const x = 60 + i * 115; o += SV.rect(x, Y(v), 80, 270 - Y(v), c, op(0.75)) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, Y(v) - 6, Math.round(v / 1000) + "k", "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "pr", label: "Price rise, % ", min: 2, max: 30, step: 1, value: 10, fmt: (v) => v + "%", onInput: labT });
Lib.slider($("#g5"), { id: "e1", label: "Short-run PES × 10 ", min: 1, max: 20, step: 1, value: 8, fmt: (v) => (v / 10).toFixed(1), onInput: labT });
Lib.slider($("#g6"), { id: "e2", label: "Long-run PES × 10 ", min: 5, max: 40, step: 1, value: 14, fmt: (v) => (v / 10).toFixed(1), onInput: labT });
labT();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Positive or normative?", ["Positive", "Normative"],
  [("A rise in interest rates will reduce consumer spending", 0), ("The government should reduce income inequality", 1), ("Inflation was 3% last year", 0), ("A minimum wage is unfair to small businesses", 1), ("Higher taxes on cigarettes reduce smoking", 0), ("Healthcare ought to be free for everyone", 1), ("Unemployment is lower in country A than in country B", 0), ("Economic growth is more important than low inflation", 1)],
  "Positive: can be tested with data. Normative: a value judgement.") + MATCH([
  ["Positive statement", "A statement of fact that can be tested"],
  ["Normative statement", "A value judgement about what ought to be"],
  ["Ceteris paribus", "All other things being equal"],
  ["Short run", "At least one factor of production is fixed"],
  ["Long run", "All factors can be varied; technology fixed"],
  ["Very long run", "Technology and other conditions can change"]]) + ORDER(
  "Put the steps for classifying a statement in order.",
  ["Read the statement carefully", "Look for value words such as should, ought, fair", "Ask whether data could prove it true or false", "Label it positive if it can be tested, normative if not", "Give one reason for your label"],
  "Value words and testability decide the label.") + CALC([
  {"q": "Price elasticity of supply is 0.8 in the short run. A price rise of 10% starts from a supply of 100,000. By how many units does supply rise in the short run?", "a": 8000, "unit": "units", "tol": 1, "hint": "0.8 × 10% × 100,000.", "sol": "8% of 100,000 = <b>8,000 units</b>."},
  {"q": "In the long run the elasticity is 1.4. By how many units does supply rise for the same price rise?", "a": 14000, "unit": "units", "tol": 1, "hint": "1.4 × 10% × 100,000.", "sol": "<b>14,000 units</b>."},
  {"q": "What is the difference between the long-run and short-run increases (units)?", "a": 6000, "unit": "units", "tol": 1, "hint": "14,000 − 8,000.", "sol": "<b>6,000 units</b>."},
  {"q": "Ceteris paribus, with a price elasticity of demand of 1, a 5% price rise changes the quantity demanded by what percentage (%)?", "a": -5, "unit": "%", "tol": 0.1, "hint": "PED × % change in price, with the opposite sign.", "sol": "<b>−5%</b>: demand falls when price rises, other things equal."}]) + MCQ([
  ("Which is a normative statement?", ["Unemployment fell last year", "The government should help the unemployed", "Inflation is measured by a price index", "Higher prices reduce demand"], 1, "'Should' signals a value judgement."),
  ("Why do economists use ceteris paribus?", ["To isolate the effect of one variable", "Because everything else always changes", "To avoid using data", "To make assumptions realistic"], 0, "Holding other things constant separates cause and effect."),
  ("In the short run:", ["At least one factor of production is fixed", "All factors are variable", "Technology can change", "Supply is perfectly elastic"], 0, "That is the definition of the short run."),
  ("A positive statement:", ["Can be tested and may be false", "Is always true", "Is an opinion", "Uses the word should"], 0, "Positive statements are testable, not necessarily correct."),
  ("The price elasticity of supply is usually higher in the long run because:", ["Firms can change all factors of production", "Prices are lower", "Consumers buy more", "The government lowers taxes"], 0, "More inputs can be varied given time.")
], "qz1") + CARDS([
  ("Social science", "Studies human behaviour; results are tendencies."),
  ("Positive", "Testable fact; may be true or false."),
  ("Normative", "Value judgement; should, ought, fair."),
  ("Ceteris paribus", "All other things equal."),
  ("Short run", "At least one fixed factor."),
  ("Long run", "All factors variable."),
  ("Very long run", "Technology can change."),
  ("Why time matters", "Elasticities and responses differ.")]) + MCQ(mc_exam)

build("as12", "as-economic-methodology", "Economic Methodology: Positive and Normative, Ceteris Paribus and Time", EY,
  "1.2.1 to 1.2.4: economics as a social science, positive and normative statements, ceteris paribus and the short, long and very long run. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
