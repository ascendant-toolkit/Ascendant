"""A Level Economics Paper 4 Section A (data response) technique. Run: python3 tools/artifact-kit/mk_ap4.py"""
import splitter
from syl import *
splitter.TABS = [("question", "The question"), ("parts", "Part by part"), ("data", "Using the data"), ("eval", "Evaluating in short parts"), ("practise", "Practise"), ("past", "Past questions"), ("tips", "Tips &amp; timing")]
EY = "A Level Economics · 9708 · Paper 4 Section A technique"

question = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Section A of Paper 4 is <b>one compulsory data response question worth 20 marks</b>, split into <b>four parts</b>, and it is based on a short passage plus a table or figure. The parts get harder and bigger: in the 40 papers we studied the <b>last part was worth 7 or 8 marks in 34 of them</b>, and the first part was usually only 2 to 4. Most marks are awarded <b>one per point</b>, so you gain by being <b>precise, using the source and developing each point briefly</b>, not by writing essays on the small parts. The last part usually needs <b>evaluation</b> (a judgement), and the passage is there to be used.</p></div>

  <h2>1 · The paper</h2>
  <div class="tw"><table class="t">
    <tr><th>Paper 4</th><th>What you need to know</th></tr>
    <tr><td><b>Time and marks</b></td><td>2 hours, 60 marks. Three sections of 20 marks each.</td></tr>
    <tr><td><b>Section A</b></td><td>One compulsory data response question, four parts, 20 marks. Passage with numbers or a figure.</td></tr>
    <tr><td><b>Sections B and C</b></td><td>One 20 mark essay from a choice of two in each section (microeconomics in B, macroeconomics in C). See the Paper 4 essay page.</td></tr>
    <tr><td><b>Assessment</b></td><td>Knowledge, analysis and evaluation. Section A parts include evaluation "where appropriate".</td></tr>
    <tr><td><b>Time for Section A</b></td><td>About 35 to 40 minutes including reading: roughly 1.7 minutes per mark.</td></tr>
  </table></div>

  <h2>2 · How the 20 marks are split</h2>
  <p>We counted the marks for the four parts in all 40 Paper 4 papers (2020 to 2025) in our folder. The most common patterns are 2, 4, 6, 8 (six papers), 4, 4, 4, 8 (four), 2, 5, 6, 7 (four) and 3, 3, 6, 8 (four). The largest part is always last.</p>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Part</th><th>Typical marks</th><th>Typical command words</th><th>What it tests</th></tr>
    <tr><td><b>(a)</b></td><td>2 to 4</td><td>Explain what is meant by..., identify, describe, define</td><td>Knowledge of a term or reading a figure</td></tr>
    <tr><td><b>(b)</b></td><td>3 to 6</td><td>Explain, analyse, distinguish, with a diagram</td><td>A short chain of reasoning</td></tr>
    <tr><td><b>(c)</b></td><td>3 to 6</td><td>Consider with reference to the table, use the data</td><td>Using and interpreting the data</td></tr>
    <tr><td><b>(d)</b></td><td>6 to 10 (usually 8)</td><td>Assess, evaluate, discuss, to what extent</td><td>Judgement using the passage</td></tr>
  </table></div>

  <h2>3 · Using about 40 minutes</h2>
  <div id="stT"></div>
'''

parts = '''
  <h2>What mark schemes reward</h2>
  <p>Mark schemes for Section A are mostly lists of points worth one mark each, often with <b>"development" worth up to two marks</b>. Three real examples, in our words:</p>
  <div class="tw"><table class="t">
    <tr><th>Question (marks)</th><th>How the marks were built</th></tr>
    <tr><td>Describe the Gini coefficient and its range (3)</td><td>What it measures (1), the range 0 to 1 (1), what 0 and 1 mean (1)</td></tr>
    <tr><td>Explain how an over-valued exchange rate may affect an economy (4)</td><td>Import prices fall and export prices rise (1); imports rise and exports fall (1); up to 2 more marks for developing the effect on one macro objective</td></tr>
    <tr><td>Use one fiscal and one supply-side policy to assess how to make income more equal (8)</td><td>For each policy: a correct example (1), development (2), link to equality (1). That is 4 + 4 = 8 marks</td></tr>
  </table></div>

  <h2>A recipe for each part</h2>
  <div class="tw"><table class="t">
    <tr><th>If the command word is...</th><th>Do this</th><th>Marks come from</th></tr>
    <tr><td><b>Identify, state, give</b></td><td>Write the answer only. No explanation. One short line per mark.</td><td>One mark per correct item</td></tr>
    <tr><td><b>Define, what is meant by</b></td><td>Precise meaning, plus a short example or figure if the marks allow.</td><td>Meaning (1), second feature or example (1)</td></tr>
    <tr><td><b>Describe</b></td><td>State the main features or the pattern in the data, using numbers.</td><td>One mark per feature</td></tr>
    <tr><td><b>Explain</b></td><td>Point, because, so: a chain of cause and effect. Use a diagram if asked.</td><td>Point (1) + reasoning (1 or 2)</td></tr>
    <tr><td><b>Analyse</b></td><td>Break the effect into steps with a diagram where it helps; link to the objective named.</td><td>Steps in the chain, diagram marks</td></tr>
    <tr><td><b>Distinguish</b></td><td>Define both terms and state the difference between them.</td><td>Each meaning (1), difference (1)</td></tr>
    <tr><td><b>Consider with reference to the table</b></td><td>Quote numbers, calculate a change, say what it shows, then say what it cannot show.</td><td>Data use (up to 2), interpretation, qualification</td></tr>
    <tr><td><b>Assess, evaluate, discuss, to what extent</b></td><td>Two or three developed points, a counter-point and a reasoned judgement that uses the passage.</td><td>Analysis marks plus evaluation marks</td></tr>
  </table></div>

  <h2>Spending the marks on the last part</h2>
  <p>An 8 mark part often follows one of two shapes. <b>Two items each worth 4</b> (example, development, link) as in "use one fiscal and one supply-side policy". Or <b>four for support and four against</b>, as in "to what extent do you agree with the advice". Read the stem to see which, then give each side its share and end with a judgement.</p>
'''

data = '''
  <h2>Data skills worth marks</h2>
  <div class="tw"><table class="t">
    <tr><th>Skill</th><th>What to do</th></tr>
    <tr><td><b>Quote accurately</b></td><td>Give the number, the unit and the year: "GDP per head at PPP rose from $9,000 to $11,500 between 2015 and 2020". Quoting alone often earns only part of the data marks.</td></tr>
    <tr><td><b>Calculate a change</b></td><td>Percentage change = (new − old) ÷ old × 100. A rise from 9,000 to 11,500 is 27.8%.</td></tr>
    <tr><td><b>Percentage points are not percentages</b></td><td>Unemployment from 6% to 5% is a fall of 1 percentage point (and 16.7% in relative terms).</td></tr>
    <tr><td><b>Compare, do not just list</b></td><td>"Country X's rose faster than Y's" and then say what it means.</td></tr>
    <tr><td><b>Do not confuse correlation and cause</b></td><td>A pattern across a few countries is not proof of cause; say what else could explain it.</td></tr>
    <tr><td><b>State what the data cannot show</b></td><td>Few countries, one year, averages that hide inequality, no PPP, no information on relative poverty or on the environment.</td></tr>
    <tr><td><b>Read figures</b></td><td>Describe direction, size and turning points: "rose until 2011 then stabilised". Compare lines by gap and by trend.</td></tr>
  </table></div>

  <h2>Anatomy of a 6 mark "consider with reference to the data" answer</h2>
  <p>Press Play, or click the numbered steps. The question: <b>Consider, with reference to the table, the change in the standard of living in Country X and Country Y between 2015 and 2020.</b> (Our own figures: GDP per head at PPP: X $9,000 to $11,500, Y $4,000 to $4,400; unemployment: X 6% to 5%, Y 8% to 7.5%; Gini coefficient: X 0.40 to 0.35, Y 0.32 to 0.37.)</p>
  <div id="stA"></div>

  <h2>Lab 1 · Percentage change or percentage points?</h2>
  <p>Enter an old and a new value. See the change in units, in percentage points (for rates) and in relative percentage terms.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Change</small><strong id="r1"></strong></div><div><small>Percentage change</small><strong id="r2"></strong></div><div><small>If both are rates (points)</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of the old value and the new value with the changes"></svg></div></div></div>

  <h2>Lab 2 · Does the table support the claim?</h2>
  <p>Claim: <b>greater inequality is linked to a lower share of women who can read and to more people in poverty</b>. Five countries are shown. Change country C's figures and watch the correlation. A correlation of 0 means no linear link; near +1 or −1 is a strong link.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Gini vs literacy ratio</small><strong id="t1"></strong></div><div><small>Gini vs poverty</small><strong id="t2"></strong></div><div><small>Claim</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Scatter of the Gini coefficient against the share of people in poverty for five countries"></svg></div></div></div>
'''

evl = '''
  <h2>Evaluation inside a short part</h2>
  <p>You do not write a mini-essay. In a 6 to 8 mark part, one or two well-aimed evaluative sentences earn the marks. Use one of these moves after you have made a point.</p>
  <div class="tw"><table class="t">
    <tr><th>Move</th><th>What it adds</th><th>Sentence starter</th></tr>
    <tr><td><b>Depends on size</b></td><td>The effect is bigger or smaller depending on elasticity, scale or share</td><td>"This depends on how elastic..."</td></tr>
    <tr><td><b>Short run versus long run</b></td><td>The effect changes with time</td><td>"In the short run this may..., but over time..."</td></tr>
    <tr><td><b>Other factors</b></td><td>Something else could explain or offset the result</td><td>"However, other factors such as... may..."</td></tr>
    <tr><td><b>Who gains and loses</b></td><td>Different groups are affected differently</td><td>"This could benefit... but harm..."</td></tr>
    <tr><td><b>Evidence limits</b></td><td>The data in the passage cannot prove the claim</td><td>"The data cover only five countries, so..."</td></tr>
    <tr><td><b>Judgement</b></td><td>A final reasoned view that answers the question</td><td>"Overall, ... is probably..., because..."</td></tr>
  </table></div>

  <h2>Using the passage in the last part</h2>
  <ul>
    <li>Quote or paraphrase a line from the passage to support each point, for example "the article says the IMF encouraged palm oil exports to repay debt".</li>
    <li>If the stem says "with reference to the article" or "using the information", answers that ignore the passage lose marks.</li>
    <li>Link the passage to a theory: the quotation is application; the economics is analysis; the judgement is evaluation.</li>
  </ul>

  <h2>Diagrams in short parts</h2>
  <ul>
    <li>A 3 to 4 mark part that says "with the help of a diagram" usually gives about half the marks for the diagram: <b>correct axes, curves labelled, a clear shift and the new and old equilibria</b>.</li>
    <li>Draw it small but complete, then write one or two sentences to explain it. A diagram with no explanation, or an explanation with no diagram, loses marks.</li>
    <li>Common short-part diagrams: a PPC for potential versus actual growth, supply and demand for an externality or a tax, AD and AS for a shock, a Lorenz curve, the money market, a tariff diagram.</li>
  </ul>
  <div class="tip"><b class="h">Good habits</b>Answer the parts in order, but if you are stuck on (c) or (d) leave a gap and return. Never leave an identify or define part blank: they are the easiest marks.</div>
'''

practise = '''
  <h2>1 · What should you write?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the command word to what it asks for</h2><div id="m1" class="card"></div>
  <h2>3 · Put the steps for Section A in order</h2><div id="o1" class="card"></div>
  <h2>4 · Quick calculations</h2><div id="c1"></div>
  <h2>5 · Check your technique</h2><div id="qz1"></div>
'''

past = '''
  <h2>Three Section A questions in full, reworded</h2>
  <p>These follow real Section A questions from 2023 to 2025. The data and wording are our own, so they are safe to set as practice. Read each part, decide the command word and marks, and then open the mark scheme points and the model answer.</p>
  <h2>A · Income inequality and poverty (modelled on May/June 2024 · 9708/41 · Question 1)</h2>
  <p><b>Passage (summary):</b> Income inequality has fallen in some low-income countries. The Gini coefficient is the most widely used measure of inequality, but it ignores wealth and the informal economy. Governments could use fiscal and supply-side policies to make the distribution of income more equal. <b>Table:</b> Country A: Gini 0.52, ratio of female to male literacy 1.00, 5% of people below the poverty line. Country B: 0.41, 0.97, 8%. Country C: 0.38, 0.93, 12%. Country D: 0.34, 0.88, 22%. Country E: 0.29, 0.70, 31%.</p>
  <div id="pastA"></div>
  <h2>B · Population change (modelled on Feb/March 2025 · 9708/42 · Question 1)</h2>
  <p><b>Passage (summary):</b> For decades a country's economy was built on a large supply of low-cost labour. Its birth rate has fallen sharply, the share of people above retirement age has risen, and annual population growth has slowed each decade, although the total was still rising in the latest year. Some economists warn of lower output and a pension burden; the government disagrees and has introduced policies to raise the birth rate.</p>
  <div id="pastB"></div>
  <h2>C · Palm oil, debt and the IMF (modelled on Oct/Nov 2022 · 9708/43 · Question 1)</h2>
  <p><b>Passage (summary):</b> Palm oil production has quadrupled in twenty years and brings rural incomes and foreign exchange to producing countries. After a financial crisis, one producer faced external debt, and the IMF encouraged it to expand palm oil exports. A multinational company invested heavily in plantations. Clearing rainforest creates large external costs. <b>Figure:</b> European use of palm oil: biodiesel rising every year; heating and electricity rising and then levelling off after 2011; food and animal feed falling slowly.</p>
  <div id="pastC"></div>
'''

tips = tips_html(
  [("Read the mark and the command word first.", "Marks tell you how many points; the command word tells you what to do with them."),
   ("Match your length to the marks.", "Roughly one point per mark. A 2 mark part is one or two sentences, not a paragraph."),
   ("Use the source.", "Quote the figures or the passage in parts (c) and (d). The source is the application."),
   ("Show the calculation.", "Write the formula and the numbers. A wrong final answer can still earn method marks."),
   ("Judge in the last part.", "End with a reasoned conclusion that answers the question: 'to a large extent', 'only partly', 'depends on'."),
   ("Draw when asked.", "Labelled axes, curves and equilibria, then explain it in words."),
   ("Leave time for (d).", "It is the biggest part. Do not run out of time on the 2 and 4 mark parts.")],
  [("Identify", "The HDI includes life expectancy, years of schooling and income per head."),
   ("Data", "GDP per head at PPP rose by about 28% in country X, compared with 10% in country Y."),
   ("Limit", "The table covers only five countries and one year, so it could not prove a cause."),
   ("Application", "The article says the IMF encouraged palm oil expansion to earn foreign exchange, which could help repay debt."),
   ("Judgement", "Overall, the policy may help in the short run but could be less sound in the long run because of the external costs.")],
  [("Identify, state", "Name or select; no explanation."),
   ("Explain", "Reasons with cause and effect."),
   ("Consider with reference to the table", "Use the data, interpret it and say what it cannot show."),
   ("Assess, evaluate", "Weigh arguments and make a judgement."),
   ("To what extent", "Say how far you agree, with reasons.")]) + FC

js = '''
/* ---------- marks pattern ---------- */
const LM = [[5, 1], [6, 3], [7, 10], [8, 24], [9, 1], [10, 1]];
$("#pic1").innerHTML = (() => { let o = SV.line(70, 190, 730, 190) + SV.line(70, 190, 70, 20) + SV.text(76, 16, "Papers (out of 40) by marks for the last part of Section A", "sm"); LM.forEach(([m, n], i) => { const x = 110 + i * 100, h = n * 6.2; o += SV.rect(x, 190 - h, 60, h, m === 8 ? "f3" : "f1", op(0.75)) + SV.text(x + 30, 210, m + " marks", "sm", { "text-anchor": "middle" }) + SV.text(x + 30, 190 - h - 8, n, "lbl bd", { "text-anchor": "middle" }); }); return `<svg viewBox="0 0 760 225" role="img" aria-label="Marks for the last part of Section A across 40 papers: 8 marks in 24, 7 marks in 10, 6 marks in 3 and 5, 9 and 10 marks once each">${o}</svg>`; })();

/* ---------- 40 minutes ---------- */
const MX = (m) => 70 + m * 16.4;
function tmDraw(s) {
  let o = SV.line(70, 150, 730, 150) + SV.text(70, 28, "0", "sm") + SV.text(730, 28, "40 min", "sm", { "text-anchor": "end" });
  [0, 10, 20, 30, 40].forEach((m) => (o += SV.line(MX(m), 144, MX(m), 156) + SV.text(MX(m), 176, m, "sm", { "text-anchor": "middle" })));
  const blk = (a, b, c, l, sub, k) => (k > 0 ? SV.rect(MX(a), 60, MX(b) - MX(a), 76, c, op(0.65 * k)) + SV.text((MX(a) + MX(b)) / 2, 92, l, "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text((MX(a) + MX(b)) / 2, 112, sub, "sm", { "text-anchor": "middle", ...op(k) }) : "");
  o += blk(0, 5, "f2", "Read", "5 min", s.a) + blk(5, 8.4, "f1", "(a)", "2 marks", s.b) + blk(8.4, 15.2, "f1", "(b)", "4 marks", s.c) + blk(15.2, 25.4, "f1", "(c)", "6 marks", s.d) + blk(25.4, 40, "f3", "(d)", "8 marks, about 14 min", s.e);
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 215, label: "A 40 minute plan for Section A with marks 2, 4, 6 and 8", base: { a: 0, b: 0, c: 0, d: 0, e: 0 }, draw: tmDraw, tween: 700, dwell: 5600, steps: [
  { cap: "<b>Read, 5 minutes.</b> Read the four questions first, then the passage and table, underlining data and phrases that answer each part.", s: { a: 1 } },
  { cap: "<b>Part (a), about 3 minutes.</b> A definition or identification: write the answer, check the marks, move on.", s: { a: 1, b: 1 } },
  { cap: "<b>Part (b), about 7 minutes.</b> A short chain of reasoning, with a diagram if the question asks.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Part (c), about 10 minutes.</b> Use the data: quote, calculate, interpret and state a limit.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>Part (d), about 14 minutes.</b> The biggest part: two developed points, a counter-point and a judgement using the passage. Roughly 1.7 minutes per mark overall.", s: { a: 1, b: 1, c: 1, d: 1, e: 1 } },
] });

/* ---------- anatomy of a 6 mark answer ---------- */
const AN = [["1 K", ["The standard of living is the material and non-material", "well-being of people."], "f1"], ["2 A", ["GDP per head at PPP rose 27.8% in X ($9,000 to $11,500)", "and 10% in Y ($4,000 to $4,400)."], "f3"], ["1 A", ["Unemployment fell in both: X from 6% to 5%, Y from 8% to 7.5%."], "f3"], ["1 N", ["The Gini fell in X (0.40 to 0.35), so gains were more evenly spread;", "it rose in Y (0.32 to 0.37), so gains were less evenly spread."], "f1"], ["1 E", ["So material living standards probably rose more in X;", "in Y the average may overstate the gain for typical households."], "f2"], ["1 E", ["The table omits health, education and the environment."], "f2"]];
function anDraw(s) {
  let y = 14, o = "";
  AN.forEach(([m, lines, c], i) => { const k = Math.max(0, Math.min(1, s.n - i)), h = 22 + lines.length * 18; if (k > 0) o += SV.rect(60, y, 660, h, c, op(0.3 * k)) + SV.rect(10, y, 44, h, c, op(0.7 * k)) + SV.text(32, y + h / 2 + 5, m, "lbl bd", { "text-anchor": "middle", ...op(k) }) + lines.map((l, j) => SV.text(72, y + 22 + j * 18, l, "lbl", op(k))).join(""); y += h + 8; });
  return o;
}
Lib.stepper($("#stA"), { w: 740, h: 388, label: "Six sentences that each earn a mark in a 6 mark data question", base: { n: 0 }, draw: anDraw, tween: 700, dwell: 5600, steps: [
  { cap: "<b>Define the term (1 mark).</b> One short sentence shows you know what 'standard of living' means. K = knowledge.", s: { n: 1 } },
  { cap: "<b>Quote and calculate (2 marks).</b> Use numbers, units and a percentage change. A = application of the data.", s: { n: 2 } },
  { cap: "<b>Second indicator (1 mark).</b> Quote the unemployment figures for both countries.", s: { n: 3 } },
  { cap: "<b>Interpret (1 mark).</b> Say what the Gini change means for how the gains are shared. N = analysis.", s: { n: 4 } },
  { cap: "<b>Judge (1 mark).</b> Reach a view about which country improved more and qualify it. E = evaluation.", s: { n: 5 } },
  { cap: "<b>State a limit (1 mark).</b> Say what the data cannot show. Six sentences, six marks.", s: { n: 6 } },
] });

/* ---------- Lab 1 ---------- */
function labP() {
  if (!$("#ov") || !$("#nv")) return;
  const a = +$("#ov").value / 10, b = +$("#nv").value / 10, d = b - a, pc = d / a * 100;
  $("#r1").textContent = (d >= 0 ? "+" : "") + Lib.fmtN(d, 1); $("#r2").textContent = (pc >= 0 ? "+" : "") + Lib.fmtN(pc, 1) + "%"; $("#r3").textContent = (d >= 0 ? "+" : "") + Lib.fmtN(d, 1) + " points";
  $("#rv").textContent = `From ${Lib.fmtN(a, 1)} to ${Lib.fmtN(b, 1)}: the change is ${Lib.fmtN(d, 1)}, which is ${Lib.fmtN(pc, 1)}% of the starting value. If these are percentages (for example unemployment rates), say it ${d >= 0 ? "rose" : "fell"} by ${Lib.fmtN(Math.abs(d), 1)} percentage points, which is a ${Lib.fmtN(Math.abs(pc), 1)}% ${d >= 0 ? "rise" : "fall"} in relative terms. Examiners expect the right wording.`;
  const Y = (v) => 270 - v * 2.4; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "Value", "sm");
  [["Old", a, "f1"], ["New", b, "f3"]].forEach(([l, v, c], i) => { const x = 90 + i * 130; o += SV.rect(x, Y(Math.min(v, 105)), 90, 270 - Y(Math.min(v, 105)), c, op(0.75)) + SV.text(x + 45, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 45, Y(Math.min(v, 105)) - 6, Lib.fmtN(v, 1), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ov", label: "Old value ", min: 10, max: 1000, step: 5, value: 60, fmt: (v) => (v / 10).toFixed(1), onInput: labP });
Lib.slider($("#g2"), { id: "nv", label: "New value ", min: 10, max: 1000, step: 5, value: 50, fmt: (v) => (v / 10).toFixed(1), onInput: labP });
labP();

/* ---------- Lab 2 ---------- */
const CT = [["A", 0.52, 1.0, 5], ["B", 0.41, 0.97, 8], ["C", 0.38, 0.93, 12], ["D", 0.34, 0.88, 22], ["E", 0.29, 0.70, 31]];
const corr = (x, y) => { const n = x.length, mx = x.reduce((a, b) => a + b) / n, my = y.reduce((a, b) => a + b) / n; let sxy = 0, sxx = 0, syy = 0; for (let i = 0; i < n; i++) { sxy += (x[i] - mx) * (y[i] - my); sxx += (x[i] - mx) ** 2; syy += (y[i] - my) ** 2; } return sxy / Math.sqrt(sxx * syy); };
function labK() {
  if (!$("#cg") || !$("#cp")) return;
  const rows = CT.map((r) => r.slice()); rows[2][1] = +$("#cg").value / 100; rows[2][3] = +$("#cp").value;
  const g = rows.map((r) => r[1]), l = rows.map((r) => r[2]), p = rows.map((r) => r[3]), rl = corr(g, l), rp = corr(g, p);
  $("#t1").textContent = (rl >= 0 ? "+" : "") + rl.toFixed(2); $("#t2").textContent = (rp >= 0 ? "+" : "") + rp.toFixed(2); const sup = rl < -0.5 && rp > 0.5; $("#t3").textContent = sup ? "Supported" : "Not supported";
  $("#tv").textContent = sup ? "Higher Gini goes with lower literacy ratios and with more poverty here, so the data are consistent with the claim. But five countries cannot prove cause: income level, schooling policy and other factors could explain both." : `The claim needs a negative link between the Gini and the literacy ratio (r near −1) and a positive link between the Gini and poverty (r near +1). Here r is ${rl.toFixed(2)} and ${rp.toFixed(2)}, so the table does not support it. In any case five countries cannot prove cause.`;
  const X = (v) => 50 + (v - 0.25) * 600, Y = (v) => 270 - v * 7; let o = SV.line(50, 270, 400, 270) + SV.line(50, 270, 50, 20) + SV.text(400, 294, "Gini coefficient", "sm", { "text-anchor": "end" }) + SV.text(56, 16, "% below the poverty line", "sm");
  rows.forEach((r, i) => { o += SV.circle(X(r[1]), Y(r[3]), 7, i === 2 ? "dot4" : "dot1") + tag(X(r[1]) + 10, Y(r[3]) - 8, r[0], i === 2 ? "t4" : "t1"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "cg", label: "Country C: Gini coefficient × 100 ", min: 25, max: 60, step: 1, value: 38, fmt: (v) => (v / 100).toFixed(2), onInput: labK });
Lib.slider($("#g4"), { id: "cp", label: "Country C: % below the poverty line ", min: 2, max: 40, step: 1, value: 12, fmt: (v) => v + "%", onInput: labK });
labK();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What should you write?", ["Name only", "Chain of reasons", "Data and interpretation", "Judgement"],
  [("Identify what is included in the HDI. (3 marks)", 0), ("Explain how an over-valued currency may affect an economy. (4 marks)", 1), ("Consider, with reference to the table, whether inequality is linked to poverty. (6 marks)", 2), ("To what extent do you agree with the IMF's advice? (8 marks)", 3), ("State two trends shown in the figure. (2 marks)", 0), ("Analyse why a producer sees palm oil as a way to reduce poverty. (4 marks)", 1), ("Use the data to comment on the change in living standards between the two years. (6 marks)", 2), ("Assess whether a government can reduce inequality with one fiscal and one supply-side policy. (8 marks)", 3)],
  "Identify: name only. Explain or analyse: reasons. Consider with the table: quote and interpret. Assess, evaluate, to what extent: judge.") + MATCH([
  ["Identify", "Name or select; no explanation needed"],
  ["Describe", "State the main features or the pattern in the data"],
  ["Explain", "Give reasons with cause and effect"],
  ["Distinguish", "Define both terms and state the difference"],
  ["Consider", "Review the information and respond to it, using the data"],
  ["Assess", "Make an informed judgement"]]) + ORDER(
  "Put the steps for Section A in order.",
  ["Read the questions and note the marks and command words", "Read the passage and underline data and key phrases", "Answer part (a) briefly, then (b) with a chain or diagram", "Answer (c) using the data with calculations and a limit", "Answer (d) with developed points, a counter-point and a judgement, using the passage"],
  "Questions first, then the source, then parts in order, saving time for the last part.") + CALC([
  {"q": "GDP per head rises from $4,171 to $4,740. Calculate the percentage change (%, 1 decimal place).", "a": 13.6, "unit": "%", "tol": 0.1, "hint": "569 ÷ 4,171.", "sol": "569 ÷ 4,171 × 100 = <b>13.6%</b>."},
  {"q": "Unemployment falls from 5.8% to 5.5%. By how many percentage points has it fallen?", "a": 0.3, "unit": "points", "tol": 0.01, "hint": "5.8 − 5.5.", "sol": "<b>0.3 percentage points</b>."},
  {"q": "The Gini coefficient falls from 0.437 to 0.385. Calculate the percentage change (%, 1 decimal place).", "a": -11.9, "unit": "%", "tol": 0.1, "hint": "(0.385 − 0.437) ÷ 0.437.", "sol": "−0.052 ÷ 0.437 = <b>−11.9%</b>."},
  {"q": "Palm oil makes up 80% of a country's exports and exports are 30% of GDP. What share of GDP is palm oil exports (%)?", "a": 24, "unit": "%", "tol": 0.1, "hint": "0.8 × 30.", "sol": "<b>24%</b> of GDP."},
  {"q": "A 20 mark Section A should take about 36 minutes. How many minutes per mark is that (1 decimal place)?", "a": 1.8, "unit": "min", "tol": 0.05, "hint": "36 ÷ 20.", "sol": "<b>1.8 minutes per mark</b>."}]) + MCQ([
  ("How many marks are usually given to the last part of Section A?", ["2", "4", "7 or 8", "15"], 2, "In 34 of 40 papers it was 7 or 8 marks, the largest part."),
  ("A part says 'Identify two...' for 2 marks. The best answer is:", ["Two short named points", "A paragraph of analysis for each", "One long sentence", "A diagram"], 0, "Identify needs no explanation. Do not waste time."),
  ("In a 'consider with reference to the table' part, the best approach is to:", ["Quote data, say what it shows and say what it cannot show", "Copy the table", "Ignore the table and write from memory", "Only calculate percentages"], 0, "Use the data, interpret it and qualify it."),
  ("Unemployment rises from 4% to 5%. The correct description is:", ["A rise of 1 percentage point (25% in relative terms)", "A rise of 1%", "A rise of 20%", "A fall of 1 point"], 0, "Rates change in percentage points; the relative change is 25%."),
  ("What is the best way to end the 8 mark part?", ["A reasoned judgement that answers the question", "A repeat of the first paragraph", "A new unrelated point", "Nothing"], 0, "The evaluation mark needs a justified conclusion."),
  ("Why should you quote the passage in part (d)?", ["It is the application and shows you used the source", "It is a waste of time", "It adds words", "It replaces analysis"], 0, "Using the passage is part of what the question asks."),
  ("A correlation across five countries shows that:", ["There is a pattern, but it does not prove cause", "One variable causes the other", "The data are wrong", "There is no link at all"], 0, "Five countries cannot prove cause; other factors may matter."),
  ("If you are stuck on part (c), you should:", ["Leave a gap and return, after attempting the other parts", "Stop the paper", "Skip all remaining parts", "Spend 20 minutes on it"], 0, "Moving on protects marks in the biggest part.")
], "qz1") + CARDS([
  ("Section A", "20 marks, four parts, last part largest."),
  ("Typical pattern", "2, 4, 6, 8 marks."),
  ("One mark per point", "Be precise and develop briefly."),
  ("Identify", "Name only."),
  ("Consider with the table", "Quote, calculate, interpret, limit."),
  ("Percentage points", "Used for changes in rates."),
  ("Last part", "Judge with the passage."),
  ("Time", "About 1.8 minutes per mark.")]) + '''
Lib.eqNoop = 0;
'''

# the past tab is built with eq() blocks injected into the page HTML below
past_a = (
  eq("Part (a) · Describe", "3 marks", "Describe what is meant by the Gini coefficient and its possible range of values.",
     ["A measure of income inequality (or less often wealth) among a population (1).", "It ranges from 0 to 1, or 0% to 100% (1).", "0 means perfect equality and 1 means perfect inequality (1)."],
     "What it measures. The range. What 0 and 1 mean.",
     [[("k", "The Gini coefficient measures the inequality of income, or sometimes wealth, in a population. It ranges from 0 to 1, where 0 is perfect equality and 1 is perfect inequality, with one person having everything.")]]) +
  eq("Part (b) · Distinguish", "3 marks", "Distinguish between absolute poverty and relative poverty.",
     ["Absolute poverty: income too low to buy what is needed to sustain life, often shown as a fixed line such as the World Bank's international poverty line.", "Relative poverty: income low compared with that of other groups in the same society.", "Credit for the difference, not just two definitions."],
     "Absolute against a fixed line. Relative against others.",
     [[("k", "Absolute poverty is having an income below the amount needed to meet basic needs, usually measured against a fixed line. Relative poverty is having an income that is low compared with others in the same society, so it can exist in rich countries.")]]) +
  eq("Part (c) · Consider with reference to the table", "6 marks", "Consider whether the table supports the conclusion that greater inequality is linked to lower female to male literacy and leads to greater poverty.",
     ["No apparent link to poor literacy: countries with higher Gini coefficients have better literacy ratios.", "Higher Gini coefficients are found where fewer people are below the poverty line, so no link to absolute poverty.", "Cause and effect cannot be determined; nothing about relative poverty.", "Up to 2 marks for correct use of the data."],
     "Quote A and E. Say the pattern is opposite. Say what is missing.",
     [[("n", "The table does not support the conclusion. Country A has the highest Gini (0.52) but the highest literacy ratio (1.00) and the lowest share in poverty (5%), whereas country E has the lowest Gini (0.29) but a ratio of only 0.70 and 31% in poverty.")], [("e", "In any case, five countries cannot show cause. The table says nothing about relative poverty, and income levels or education policy could explain the pattern.")]]) +
  eq("Part (d) · Assess", "8 marks", "Use one supply-side policy and one fiscal policy to assess how a government could make the distribution of income more equal.",
     ["Fiscal: correct example (1), development (2), link to equality (1).", "Supply-side: correct example (1), development (2), link to equality (1)."],
     "Fiscal: progressive tax and transfers. Supply-side: education. Develop each and link to the Gini.",
     [[("k", "A fiscal policy is a more progressive income tax with higher benefits."), ("n", "This takes a larger share of high incomes and raises the incomes of low earners, so it could reduce the Gini coefficient quickly, although high marginal rates may reduce incentives.")], [("k", "A supply-side policy is spending on education and training."), ("n", "This may raise the productivity and wages of low-paid workers, so incomes become more equal over time, although the effect takes years.")]])
)
past_b = (
  eq("Part (a) · Explain", "2 marks", "Explain what is meant by an optimum population.",
     ["The size of population which, with existing resources, factors of production and technology, gives the highest income per head (1).", "Where the standard of living is at a maximum (1)."],
     "Highest income per head, given resources, capital and technology.",
     [[("k", "An optimum population is the size at which, given the economy's resources, capital and technology, income per head is highest, so the standard of living is at a maximum.")]]) +
  eq("Part (b) · Explain and consider", "5 marks", "Explain how the age structure changed between 1970 and 2020, and consider whether the claim that the population is falling is supported by data showing annual population growth was positive every year to 2020 but falling.",
     ["Falling birth rate (1); ageing population (1); rising dependency ratio (1).", "The data show the population still growing, only more slowly (1), so the claim 'it is falling' is not supported (1)."],
     "Three structure changes. Then the data: still positive, so not falling.",
     [[("k", "The birth rate fell, so the share of young people fell and the share of older people rose, giving an ageing population. As fewer workers support more retirees, the dependency ratio increased.")], [("n", "The data show that annual population growth was positive in every year to 2020, even though it slowed, so the total population was still rising. The claim that the population is falling is therefore not supported by this evidence.")]]) +
  eq("Part (c) · Identify and analyse", "6 marks", "Identify two observations economists have made about the changes in the population and analyse how each would affect GDP.",
     ["Fewer young people mean a smaller pool of workers, innovators and entrepreneurs, lowering output and productivity.", "More older people raise spending on pensions and care, which may raise the budget deficit and reduce investment, lowering GDP."],
     "Observation, link, GDP effect, twice.",
     [[("k", "One observation is that there are fewer young people."), ("n", "This means a smaller pool of future workers and entrepreneurs, so labour force growth and productivity may slow and GDP could be lower.")], [("k", "A second is that the share of older people is rising."), ("n", "This may raise government spending on pensions and health care, which could widen the deficit or crowd out investment, reducing GDP.")]]) +
  eq("Part (d) · Consider", "7 marks", "The government says the economists' warnings are alarmist and has introduced policies to raise the birth rate. Consider the effects on the economy of these policies.",
     ["The earlier policy to cut births moved the economy towards a skills-based economy, but led to a more dependent population, lower savings and investment and lower long-term AS and AD.", "The new policy aims to rebuild a young, skilled workforce supported by technology, which could raise competitiveness and long-run AS and AD."],
     "Explain the aim. Effects on workforce, AS and AD. Time lag and judgement.",
     [[("k", "The policy aims to raise the birth rate so that a larger young workforce grows up."), ("n", "In the long run, more young, skilled workers could raise potential output and aggregate supply, and support demand, making the economy more competitive.")], [("e", "However, the effect has a long time lag of about twenty years, and in the short run more children raise dependency and costs for families and the government. So the policy may help in the long run, but is unlikely to solve the problem quickly.")]])
)
past_c = (
  eq("Part (a) · Identify", "3 marks", "Identify the trends in demand for the different uses of palm oil shown in the figure.",
     ["Biodiesel use rises throughout the period (1).", "Heating and electricity use rises and then stabilises after 2011 (1).", "Food and animal feed use falls over the period (1)."],
     "One trend per use: rising, rising then flat, falling.",
     [[("k", "Biodiesel use rises every year. Use for heating and electricity rises and then levels off after 2011. Use in food and animal feed declines over the period.")]]) +
  eq("Part (b) · Analyse", "4 marks", "Analyse why developing countries that produce palm oil see it as a way to reduce poverty.",
     ["Agriculture is linked to rural economies that suffer underemployment and low, seasonal incomes (1).", "High world demand makes palm oil a source of income and foreign exchange (1) so rural incomes rise (1) and more people leave poverty (1).", "More employment; multinationals' investment supports rural economies."],
     "Demand, income and jobs, foreign exchange, rural living standards.",
     [[("k", "World demand for palm oil is high, so it earns income and foreign exchange."), ("n", "Production in rural areas creates jobs for people who were underemployed, and raises incomes and living standards, which could lift many households out of poverty. Investment by multinationals expands production and sustains these rural economies.")]]) +
  eq("Part (c) · Explain", "5 marks", "Explain how a proposed removal of a subsidy on biodiesel by a European parliament could affect palm oil producing countries.",
     ["Removing the subsidy raises biodiesel prices for consumers in Europe, which could lower demand and imports, and so the demand for palm oil (up to 2).", "Adverse effects on the balance of payments (1), incomes (1) and employment (1) in producing countries.", "Multinationals may cut investment if profits fall."],
     "Subsidy removal, higher price, lower demand for palm oil, then BoP, incomes, jobs.",
     [[("k", "Removing the subsidy raises the price of biodiesel in Europe."), ("n", "Demand for biodiesel and so for palm oil could fall, reducing export earnings for producing countries and worsening their current account. Lower export earnings may reduce incomes and employment in the sector, and multinationals might cut investment if profits fall.")]]) +
  eq("Part (d) · To what extent", "8 marks", "To what extent do you agree with the IMF's advice to expand palm oil production in order to deal with external debt?",
     ["In support (up to 4): the country had external debt problems, palm oil is a big earner of foreign exchange which could repay debt, and incomes could rise.", "Against (up to 4): clearing rainforest destroys habitats and releases greenhouse gases, so external costs exceed private costs; dependence on one crop (monoculture) leaves earnings exposed to foreign buyers and price swings."],
     "For: foreign exchange and incomes. Against: external costs and monoculture. Judge.",
     [[("k", "The IMF advice could help. Palm oil is a large earner of foreign currency, so expansion may reduce the current account deficit and provide funds to repay external debt, and raise rural incomes.")], [("e", "However, clearing rainforest creates external costs, including lost habitats and greenhouse gas emissions, which may exceed the private benefits. Dependence on one crop leaves the economy exposed to price falls. So the advice may help in the short run but is less sound for sustainable development.")]])
)

build_args = dict(question=question, parts=parts, data=data, eval=evl, practise=practise, past=past, tips=tips)
js = js.replace('\nLib.eqNoop = 0;\n', '\n')
past_html = past.replace('<div id="pastA"></div>', past_a).replace('<div id="pastB"></div>', past_b).replace('<div id="pastC"></div>', past_c)
build_args["past"] = past_html
build("ap4", "a-level-paper4-data-response", "Paper 4 Section A: Data Response Technique", EY,
  "How to score on the 20 mark data response question: the structure, what each part asks, using the data, evaluating in short parts and three full reworded Section A questions. Animated diagrams, labs, drills and practice.",
  build_args, js)
