"""A Level Economics Paper 3 multiple choice technique. Run: python3 tools/artifact-kit/mk_ap3.py"""
import splitter
from syl import *
splitter.TABS = [("paper", "The paper"), ("method", "The method"), ("types", "Question types"), ("traps", "Traps and timing"), ("practise", "Practise"), ("past", "Past questions"), ("tips", "Tips &amp; keywords")]
EY = "A Level Economics · 9708 · Paper 3 technique"

paper = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Paper 3 is <b>30 multiple choice questions in 1 hour 15 minutes</b>, one mark each, with <b>no marks lost for a wrong answer</b>, so you should answer every question. It covers the whole <b>A Level content (topics 7 to 11)</b> and assumes AS knowledge, and it is <b>17% of the A Level</b>. Questions test <b>knowledge, application and analysis</b> through definitions, calculations, diagrams, tables of data and statements to judge. The marks go to students who <b>read carefully, work out an answer before looking at the options, and use the options to eliminate</b>, not to students who know the most facts.</p></div>

  <h2>1 · The facts</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Paper 3 (A Level)</th></tr>
    <tr><td><b>Time and marks</b></td><td>1 hour 15 minutes, 30 marks</td></tr>
    <tr><td><b>Questions</b></td><td>30 multiple choice, four options (A to D)</td></tr>
    <tr><td><b>Content</b></td><td>A Level topics 7 to 11, with AS knowledge assumed</td></tr>
    <tr><td><b>Weighting</b></td><td>17% of the A Level</td></tr>
    <tr><td><b>Time per question</b></td><td>2.5 minutes</td></tr>
    <tr><td><b>Negative marking</b></td><td>None: never leave a blank</td></tr>
  </table></div>

  <h2>2 · Using 75 minutes</h2>
  <div id="pic1" class="card"></div>

  <h2>3 · What the paper tends to cover</h2>
  <p>From the 24 Paper 3 papers (2020 to 2025) in our folder, the questions follow a rough order. This is a pattern, not a rule, but it helps you see where the time goes.</p>
  <div class="tw"><table class="t">
    <tr><th>Question numbers</th><th>Themes you usually meet</th><th>Typical style</th></tr>
    <tr><td><b>1 to 6</b></td><td>Consumer choice and utility, efficiency and market failure, costs and revenue</td><td>Definitions, short concepts, simple logic</td></tr>
    <tr><td><b>7 to 12</b></td><td>Firms: economies of scale, objectives, market structures, pricing, mergers</td><td>Which statement is correct; diagrams of costs; negative stems</td></tr>
    <tr><td><b>13 to 18</b></td><td>Government microeconomics, labour markets, inequality and poverty</td><td>Policy effects, tables of yes/no, Lorenz and Gini</td></tr>
    <tr><td><b>19 to 24</b></td><td>Economic growth, development, unemployment, inflation, policy</td><td>Calculations, data tables, combinations</td></tr>
    <tr><td><b>25 to 30</b></td><td>Money, interest rates, the balance of payments, exchange rates, development, globalisation</td><td>Combination tables, diagrams (J curve, trade), short calculations</td></tr>
  </table></div>
  <p>Across the 1,155 questions, the correct answer letter was <b>A 21%, B 27%, C 28% and D 24%</b>. The differences are small, so there is no letter worth guessing. If you must guess, remove options first, then pick.</p>
  <div id="pic2" class="card"></div>
'''

method = '''
  <h2>The four steps</h2>
  <div class="tw"><table class="t">
    <tr><th>Step</th><th>What to do</th><th>Time</th></tr>
    <tr><td><b>1 · Read the stem</b></td><td>Cover the options. Underline the <b>qualifier</b> (not, least likely, most likely, definitely, only) and the <b>key concept</b>. Note any figures.</td><td>15 s</td></tr>
    <tr><td><b>2 · Predict</b></td><td>Say or write your own answer before you look. For a calculation do the sum. For a diagram sketch the shift. For a "not" question list what would be true.</td><td>30 s</td></tr>
    <tr><td><b>3 · Eliminate</b></td><td>Read each option and cross out those that are wrong, with a reason. Do not stop at the first one that looks right.</td><td>45 s</td></tr>
    <tr><td><b>4 · Check</b></td><td>Re-read the stem and make sure your answer fits the qualifier. Mark the answer sheet carefully and flag it if you are unsure.</td><td>10 s</td></tr>
  </table></div>

  <h2>Watch the method on a real question</h2>
  <p>Press Play, or click the numbered steps. The question is one of the Paper 3 questions (reworded): <b>What is least likely to lead to an increase in a country's optimum population?</b></p>
  <div id="stM"></div>

  <h2>How wrong options are built</h2>
  <p>Examiners write the three wrong options (distractors) from common mistakes. Recognising the pattern speeds up elimination.</p>
  <div class="tw"><table class="t">
    <tr><th>Distractor pattern</th><th>What it looks like</th><th>Example</th></tr>
    <tr><td><b>Reversed direction</b></td><td>Right idea, wrong way round</td><td>"A rise in the interest rate raises bond prices"</td></tr>
    <tr><td><b>True but irrelevant</b></td><td>A correct statement that does not answer this question</td><td>An external benefit that is actually a private benefit</td></tr>
    <tr><td><b>Neighbouring concept</b></td><td>Confuses two similar terms</td><td>Laffer curve, Lorenz curve, Kuznets curve, Phillips curve</td></tr>
    <tr><td><b>Half right</b></td><td>The first part is correct and the second is wrong (in combination tables)</td><td>"Current account improves; financial account improves" when only one does</td></tr>
    <tr><td><b>Calculation slip</b></td><td>The answer you get if you forget a step</td><td>Real income per head without dividing by population</td></tr>
    <tr><td><b>Extreme words</b></td><td>"always", "never", "only", "must" make a statement easy to disprove</td><td>"Tariffs always raise welfare"</td></tr>
  </table></div>
'''

types = '''
  <h2>Seven question types and how to attack them</h2>
  <p>In the past papers roughly <b>one question in six has a negative stem</b> (not, least, except) and about <b>one in five refers to a diagram, graph or chart</b>. Know what to do for each type.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>How to spot it</th><th>What to do</th></tr>
    <tr><td><b>1 · Negative</b></td><td>"What is not...", "least likely", "which does not"</td><td>Underline the qualifier. Mark each option T or F. The odd one out is your answer.</td></tr>
    <tr><td><b>2 · Definition or concept</b></td><td>"What is meant by...", "Which describes..."</td><td>Say the definition in your own words first. Beware the neighbouring concept.</td></tr>
    <tr><td><b>3 · Calculation</b></td><td>Numbers in the stem, "what is the approximate change"</td><td>Write the formula, then substitute. Check units and whether per head or in total. Estimate to the nearest whole number.</td></tr>
    <tr><td><b>4 · Diagram or graph</b></td><td>A figure, curve or shaded areas</td><td>Label axes and curves yourself. Find the starting equilibrium, then the shift, then the new equilibrium. Read what each area represents.</td></tr>
    <tr><td><b>5 · Combination table</b></td><td>A grid of yes/no, rise/fall or high/low</td><td>Decide each column separately, then find the row that matches both (or all) columns.</td></tr>
    <tr><td><b>6 · Data interpretation</b></td><td>"What can be concluded from the table?"</td><td>Only accept statements the table proves. Watch for totals versus per head, and cause versus correlation.</td></tr>
    <tr><td><b>7 · Application or best example</b></td><td>A short real-world scenario</td><td>Match the scenario to the concept it illustrates. Check who is affected (third parties for externalities).</td></tr>
  </table></div>

  <h2>Formulas that pay off</h2>
  <div class="tw"><table class="t">
    <tr><th>Topic</th><th>Formula</th></tr>
    <tr><td>Real income per head</td><td>about nominal growth − inflation − population growth; exactly (1 + n) ÷ (1 + p) ÷ (1 + q) − 1</td></tr>
    <tr><td>Labour force and unemployment</td><td>Labour force = employed + unemployed; rate = unemployed ÷ labour force × 100</td></tr>
    <tr><td>Gini coefficient</td><td>Area between line and Lorenz curve ÷ area under the line of equality; 0 to 1</td></tr>
    <tr><td>Multiplier</td><td>1 ÷ (1 − MPC) or 1 ÷ marginal propensity to withdraw</td></tr>
    <tr><td>Price elasticity</td><td>% change in quantity ÷ % change in price; Marshall-Lerner: PEDx + PEDm greater than 1</td></tr>
    <tr><td>Dependency ratio</td><td>(under 15 + over 64) ÷ (15 to 64) × 100</td></tr>
    <tr><td>Terms of trade</td><td>(export price index ÷ import price index) × 100</td></tr>
    <tr><td>Real interest rate</td><td>nominal rate − inflation</td></tr>
    <tr><td>Quantity theory</td><td>MV = PT</td></tr>
  </table></div>
'''

traps = '''
  <h2>Lab 1 · The calculation trap</h2>
  <p>Examiners build the wrong options from forgotten steps. Set nominal growth, inflation and population growth and see the right answer and the three common wrong ones.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Correct: real per head</small><strong id="r1"></strong></div><div><small>Forgot population</small><strong id="r2"></strong></div><div><small>Forgot inflation</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars for the correct real income per head change and two wrong answers from missing steps"></svg></div></div></div>

  <h2>Lab 2 · Plan your 75 minutes</h2>
  <p>Set your speed on the first pass, how many questions you flag as hard, and how long you give each on the second pass. See how much time is left to check.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div><div id="g6"></div>
    <div class="readout"><div><small>First pass</small><strong id="t1"></strong></div><div><small>Second pass</small><strong id="t2"></strong></div><div><small>Time left to check</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Stacked bar of the first pass, second pass and checking time against 75 minutes"></svg></div></div></div>

  <h2>Words in stems that change the answer</h2>
  <div class="tw"><table class="t">
    <tr><th>Word</th><th>What it means for you</th></tr>
    <tr><td><b>least likely, not, except</b></td><td>Three options are true or likely. You need the odd one out.</td></tr>
    <tr><td><b>most likely, best</b></td><td>More than one option may be possible. Choose the strongest.</td></tr>
    <tr><td><b>definitely</b></td><td>The conclusion must always follow. Reject options that only might be true.</td></tr>
    <tr><td><b>in the short run, long run</b></td><td>The time period can reverse the answer, as with the J curve.</td></tr>
    <tr><td><b>per head, per capita</b></td><td>Divide by population. Totals and averages can move in opposite directions.</td></tr>
    <tr><td><b>real, nominal</b></td><td>Real means adjusted for inflation.</td></tr>
    <tr><td><b>ceteris paribus (all else equal)</b></td><td>Change one thing only. Do not bring in other effects.</td></tr>
  </table></div>
'''

practise = '''
  <h2>1 · Which type of question is it?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the stem word to what it tells you</h2><div id="m1" class="card"></div>
  <h2>3 · Put the four steps in order</h2><div id="o1" class="card"></div>
  <h2>4 · Quick calculations</h2><div id="c1"></div>
  <h2>5 · Practice questions</h2><p>These are our own questions, each with the reason for the right answer and the pattern of the wrong ones.</p><div id="qz1"></div>
'''

past = '''
  <h2>Twelve past Paper 3 questions, by type</h2>
  <p>Reworded from the paper and question number shown. The label at the start tells you which type to apply. Try each with the four steps before you click.</p>
  <div id="qz2"></div>
'''

tips = tips_html(
  [("Answer every question.", "There is no penalty. Fill in any blank in the last minute."),
   ("Cover the options.", "Read the stem, predict, then look. It stops the options from steering you."),
   ("Underline the qualifier.", "Not, least, most likely, definitely: the wrong answer to a negative question is usually the one you would pick for a positive one."),
   ("Sketch a diagram.", "Even a rough supply and demand or AD and AS sketch saves mistakes."),
   ("Estimate numbers.", "Round before you calculate and check which options are near. Beware unit and per head traps."),
   ("Flag and move on.", "Do not spend more than about 3 minutes. Mark the question and come back."),
   ("Check the answer sheet.", "Make sure the question number and the letter match.")],
  [("Elimination", "Option C changes the actual population but not the optimum population, so it is the odd one out."),
   ("Calculation", "Real income per head falls because prices rose faster than nominal income, and population also grew."),
   ("Diagram", "The supply curve shifts right, so the equilibrium price falls and quantity rises."),
   ("Data", "The table shows a correlation for five countries but cannot prove cause."),
   ("Combination", "Column one is correct, but column two is not, so that row is wrong.")],
  [("Not / least likely", "Three options are true or likely and one is not. Find the exception."),
   ("Calculate", "Work out from the numbers given, then check against the options."),
   ("Which statement is correct", "Test each option as true or false."),
   ("Most likely", "Choose the most probable of the possible effects."),
   ("What can be concluded", "Only choose a statement that the data prove.")]) + FC

js = '''
/* ---------- 75 minutes ---------- */
const TX = (m) => 70 + m * 8.8;
function timeDraw(s) {
  let o = SV.line(70, 150, 730, 150) + SV.text(70, 28, "0 min", "sm") + SV.text(730, 28, "75 min", "sm", { "text-anchor": "end" });
  [0, 15, 30, 45, 60, 75].forEach((m) => (o += SV.line(TX(m), 144, TX(m), 156) + SV.text(TX(m), 176, m, "sm", { "text-anchor": "middle" })));
  const blk = (a, b, c, l, sub, k) => (k > 0 ? SV.rect(TX(a), 60, TX(b) - TX(a), 76, c, op(0.65 * k)) + SV.text((TX(a) + TX(b)) / 2, 92, l, "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text((TX(a) + TX(b)) / 2, 112, sub, "sm", { "text-anchor": "middle", ...op(k) }) : "");
  o += blk(0, 50, "f1", "First pass", "30 questions, about 100 seconds each", s.a) + blk(50, 66, "f3", "Second pass", "hard ones", s.b) + blk(66, 75, "f2", "Check", "sheet", s.c);
  if (s.d > 0) o += tag(400, 220, "Total: 75 minutes. Any blank at the end gets a guess: there is no penalty.", "t4", s.d, "middle");
  return o;
}
Lib.stepper($("#pic1"), { w: 760, h: 250, label: "A 75 minute timeline split into a 50 minute first pass, a 16 minute second pass and a 9 minute check", base: { a: 0, b: 0, c: 0, d: 0 }, draw: timeDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>First pass, about 50 minutes.</b> Go through all 30 questions at roughly 100 seconds each. Answer what you can, make a best guess on the rest and flag anything that needs more than a minute or two.", s: { a: 1 } },
  { cap: "<b>Second pass, about 16 minutes.</b> Return to the flagged questions. Use the four-step method and give each a fair try, but stop at 3 minutes.", s: { a: 1, b: 1 } },
  { cap: "<b>Check, about 9 minutes.</b> Make sure every question has an answer, the letters match the question numbers, and re-read the stems of the negative questions.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Total 75 minutes.</b> There is no negative marking, so fill every blank before time runs out.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });
$("#pic2").innerHTML = (() => { const v = [["A", 21], ["B", 27], ["C", 28], ["D", 24]]; let o = SV.line(70, 190, 730, 190) + SV.line(70, 190, 70, 20) + SV.text(76, 16, "Share of correct answers (%)", "sm"); v.forEach(([l, p], i) => { const x = 130 + i * 140, h = p * 5; o += SV.rect(x, 190 - h, 80, h, "f1", op(0.7)) + SV.text(x + 40, 210, "Answer " + l, "sm", { "text-anchor": "middle" }) + SV.text(x + 40, 190 - h - 8, p + "%", "lbl bd", { "text-anchor": "middle" }); }); return `<svg viewBox="0 0 760 225" role="img" aria-label="Correct answers by letter in 1,155 Paper 3 questions: A 21 percent, B 27, C 28, D 24">${o}</svg>`; })();

/* ---------- the four steps on a real question ---------- */
const OPT = ["A  An improvement in labour productivity", "B  An improvement in the quality of capital and technology", "C  An increase in the birth rate and a fall in the death rate", "D  An increase in the availability of natural resources"];
function stepDraw(s) {
  let o = SV.rect(40, 14, 680, 44, "f1", op(0.25)) + SV.text(60, 42, "What is", "lbl bd") + SV.text(120, 42, "least likely", "lbl bd", { style: "fill:var(--bad)" + (s.q > 0 ? ";text-decoration:underline" : "") }) + SV.text(220, 42, "to lead to an increase in a country's optimum population?", "lbl bd");
  if (s.p > 0) o += SV.rect(40, 66, 680, 34, "f3", op(0.3 * s.p)) + SV.text(60, 88, "My prediction: optimum rises with productivity, capital, technology and resources. Look for the one that is not.", "sm", op(s.p));
  OPT.forEach((t, i) => { const y = 112 + i * 44, el = i !== 2 ? Math.max(0, Math.min(1, s.e)) : 0, ok = i === 2 && s.c > 0; o += SV.rect(40, y, 680, 36, ok ? "f3" : "f1", op(ok ? 0.55 : 0.18)) + SV.text(60, y + 24, t, "lbl", { style: el > 0.5 ? "text-decoration:line-through;opacity:.45" : "" }) + (el > 0.5 ? SV.text(700, y + 24, "✗ raises the optimum", "sm", { "text-anchor": "end", style: "fill:var(--bad)" }) : "") + (ok ? SV.text(700, y + 24, "✓ changes actual, not optimum", "sm", { "text-anchor": "end", style: "fill:var(--good)" }) : ""); });
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 300, label: "The four steps applied to a negative optimum population question", base: { q: 0, p: 0, e: 0, c: 0 }, draw: stepDraw, tween: 700, dwell: 6200, steps: [
  { cap: "<b>Step 1 · Read the stem.</b> Underline <b>least likely</b>. This is a negative question: three options raise the optimum population and one does not.", s: { q: 1 } },
  { cap: "<b>Step 2 · Predict.</b> Before reading the options, list what raises the optimum population: higher productivity, better capital and technology, more resources.", s: { q: 1, p: 1 } },
  { cap: "<b>Step 3 · Eliminate.</b> A, B and D each raise output per head at every population size, so they raise the optimum. Cross them out.", s: { q: 1, p: 1, e: 1 } },
  { cap: "<b>Step 4 · Check.</b> C changes the actual size of the population, not the best size. It is the answer to 'least likely'.", s: { q: 1, p: 1, e: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labC() {
  if (!$("#nm") || !$("#in") || !$("#pg")) return;
  const n = +$("#nm").value / 10, p = +$("#in").value / 10, q = +$("#pg").value / 10, right = ((1 + n / 100) / (1 + p / 100) / (1 + q / 100) - 1) * 100, noPop = ((1 + n / 100) / (1 + p / 100) - 1) * 100, noInf = ((1 + n / 100) / (1 + q / 100) - 1) * 100;
  $("#r1").textContent = (right >= 0 ? "+" : "") + Lib.fmtN(right, 1) + "%"; $("#r2").textContent = (noPop >= 0 ? "+" : "") + Lib.fmtN(noPop, 1) + "%"; $("#r3").textContent = (noInf >= 0 ? "+" : "") + Lib.fmtN(noInf, 1) + "%";
  $("#rv").textContent = `Nominal income grew ${Lib.fmtN(n, 1)}%, prices ${Lib.fmtN(p, 1)}% and population ${Lib.fmtN(q, 1)}%. Real income per head changed by about ${Lib.fmtN(right, 1)}%. Forgetting the population gives ${Lib.fmtN(noPop, 1)}% and forgetting inflation gives ${Lib.fmtN(noInf, 1)}%: examiners often include these as the wrong options. Quick check: ${Lib.fmtN(n, 1)} − ${Lib.fmtN(p, 1)} − ${Lib.fmtN(q, 1)} = ${Lib.fmtN(n - p - q, 1)}.`;
  const Y = (v) => 150 - v * 8; let o = SV.line(40, 150, 400, 150) + SV.line(40, 20, 40, 280) + SV.text(46, 16, "% change", "sm");
  [["Correct", right, "f3"], ["No population", noPop, "f2"], ["No inflation", noInf, "f2"]].forEach(([l, v, c], i) => { const x = 60 + i * 115, y = Y(Math.max(-16, Math.min(16, v))); o += SV.rect(x, Math.min(y, 150), 80, Math.abs(y - 150), c, op(i ? 0.5 : 0.85)) + SV.text(x + 40, 296, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, v >= 0 ? y - 6 : y + 16, (v >= 0 ? "+" : "") + Lib.fmtN(v, 1), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "nm", label: "Nominal income growth, % ", min: -20, max: 100, step: 5, value: 20, fmt: (v) => (v / 10).toFixed(1), onInput: labC });
Lib.slider($("#g2"), { id: "in", label: "Inflation, % ", min: 0, max: 100, step: 5, value: 30, fmt: (v) => (v / 10).toFixed(1), onInput: labC });
Lib.slider($("#g3"), { id: "pg", label: "Population growth, % ", min: -10, max: 30, step: 5, value: 10, fmt: (v) => (v / 10).toFixed(1), onInput: labC });
labC();

/* ---------- Lab 2 ---------- */
function labT() {
  if (!$("#sp") || !$("#fl") || !$("#fs")) return;
  const sp = +$("#sp").value, fl = +$("#fl").value, fs = +$("#fs").value, p1 = 30 * sp / 60, p2 = fl * fs / 60, left = 75 - p1 - p2;
  $("#t1").textContent = Lib.fmtN(p1, 0) + " min"; $("#t2").textContent = Lib.fmtN(p2, 0) + " min"; $("#t3").textContent = (left >= 0 ? "" : "−") + Lib.fmtN(Math.abs(left), 0) + " min";
  $("#tv").textContent = left >= 8 ? `At ${sp} seconds per question you finish the first pass in ${Lib.fmtN(p1, 0)} minutes, spend ${Lib.fmtN(p2, 0)} on the ${fl} flagged questions and still have ${Lib.fmtN(left, 0)} minutes to check. That is a safe plan.` : left >= 0 ? `This leaves only ${Lib.fmtN(left, 0)} minutes to check. Speed up the first pass or flag fewer questions.` : `This plan takes ${Lib.fmtN(-left, 0)} minutes more than you have. Cut the time on the second pass: guess on the hardest questions rather than run out of time.`;
  const X = (m) => 30 + m * 4.6; let o = SV.line(30, 160, 380, 160) + SV.text(30, 40, "0", "sm") + SV.text(X(75), 40, "75 min", "sm", { "text-anchor": "end" });
  const segs = [["First pass", p1, "f1"], ["Second pass", p2, "f3"], ["Left to check", Math.max(0, left), left >= 8 ? "f1" : "f2"]]; let x0 = 0;
  segs.forEach(([l, v, c], i) => { const w = Math.min(v, 75 - x0) * 4.6; o += SV.rect(X(x0), 80, Math.max(0, w), 60, c, op(i === 2 ? 0.35 : 0.7)) + (w > 28 ? SV.text(X(x0) + w / 2, 115, Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }) : "") + SV.text(X(x0) + w / 2, 180 + i * 14, l, "sm", { "text-anchor": "middle" }); x0 += v; });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "sp", label: "Seconds per question on the first pass ", min: 60, max: 130, step: 5, value: 95, fmt: (v) => v, onInput: labT });
Lib.slider($("#g5"), { id: "fl", label: "Questions flagged as hard ", min: 0, max: 15, step: 1, value: 6, fmt: (v) => v, onInput: labT });
Lib.slider($("#g6"), { id: "fs", label: "Seconds per flagged question on the second pass ", min: 45, max: 240, step: 15, value: 120, fmt: (v) => v, onInput: labT });
labT();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which type of question is it?", ["Negative", "Calculation", "Diagram or data", "Combination table"],
  [("Which of these is not a function of the IMF?", 0), ("GNP rises 3%, prices 4% and population 1%. What is the approximate change in real income per head?", 1), ("The diagram shows a Lorenz curve with areas X and Y. How is the Gini coefficient calculated?", 2), ("What is the effect on the current account and the financial account? (Improves or worsens for each)", 3), ("What is least likely to raise the optimum population?", 0), ("Employed 900,000 and unemployed 300,000. What is the unemployment rate?", 1), ("From the table of birth rates and death rates, which conclusion can be drawn?", 2), ("Which row shows the effect on employment, investment and the balance of payments (yes or no)?", 3)],
  "Negative: not, least. Calculation: numbers and a rate. Diagram or data: a figure or table to read. Combination: a grid of yes/no columns.") + MATCH([
  ["Not, except, least likely", "Three options are true; find the odd one out"],
  ["Most likely, best", "Choose the strongest of several possibilities"],
  ["Definitely", "The conclusion must always follow, not just sometimes"],
  ["Per head", "Divide the total by the population"],
  ["Real", "Adjusted for inflation"],
  ["In the short run", "Before everything has adjusted; time can reverse the answer"]]) + ORDER(
  "Put the four steps in order.",
  ["Read the stem and underline the qualifier", "Predict your own answer", "Eliminate the wrong options with reasons", "Check the answer against the qualifier and mark the sheet"],
  "Read, predict, eliminate, check.") + CALC([
  {"q": "Over a year nominal national income rises 5%, prices rise 3% and population rises 1%. By roughly what percentage does real income per head change (%, nearest whole number)?", "a": 1, "unit": "%", "tol": 0.1, "hint": "5 − 3 − 1.", "sol": "<b>+1%</b>: 1.05 ÷ 1.03 ÷ 1.01 = 1.009."},
  {"q": "Employed 1,500,000 and unemployed 100,000. Calculate the unemployment rate (%, 1 decimal place).", "a": 6.3, "unit": "%", "tol": 0.1, "hint": "Labour force = 1.6m.", "sol": "100,000 ÷ 1,600,000 × 100 = <b>6.3%</b>."},
  {"q": "The area between the line of equality and the Lorenz curve is 0.1 and the area under the Lorenz curve is 0.4. Calculate the Gini coefficient.", "a": 0.2, "unit": "", "tol": 0.005, "hint": "0.1 ÷ (0.1 + 0.4).", "sol": "<b>0.20</b>."},
  {"q": "The MPC is 0.75. Calculate the multiplier.", "a": 4, "unit": "", "tol": 0.01, "hint": "1 ÷ (1 − 0.75).", "sol": "<b>4</b>."},
  {"q": "Export prices rise 10% and import prices rise 25% (starting at 100 each). Calculate the terms of trade index.", "a": 88, "unit": "", "tol": 0.5, "hint": "110 ÷ 125 × 100.", "sol": "<b>88</b>: a deterioration."}]) + MCQ([
  ("[Negative] Which is least likely to cause an increase in a country's long-run economic growth?", ["Higher spending on education", "A fall in the capital stock", "Better technology", "More skilled migrants"], 1, "A fall in the capital stock reduces productive capacity. The other three raise it. Notice the qualifier: you need the one that does not help."),
  ("[Calculation] Nominal GDP rises 6% and prices rise 4%. Population is unchanged. What is the approximate change in real GDP per head?", ["−2%", "0%", "+2%", "+10%"], 2, "6 − 4 = 2. The 10% option adds instead of subtracting, and −2% reverses the sign."),
  ("[Combination] A country's currency depreciates and the Marshall-Lerner condition holds. What happens to exports and to imports in domestic currency terms? Exports (volume) and import prices.", ["Exports rise; import prices rise", "Exports rise; import prices fall", "Exports fall; import prices rise", "Exports fall; import prices fall"], 0, "Cheaper for foreigners means more exports, and a lower currency makes imports dearer at home. Half-right options reverse one column."),
  ("[Concept] Which curve shows income inequality rising and then falling as income per head rises?", ["Lorenz curve", "Laffer curve", "Kuznets curve", "Phillips curve"], 2, "Four similar sounding curves are the classic 'neighbouring concept' distractor."),
  ("[Data] A table shows that in five countries those with a higher Gini coefficient also have a lower share of people below the poverty line. What can be concluded?", ["Inequality causes lower poverty", "Inequality causes higher poverty", "There is a negative relationship in these countries but cause is not proved", "Poverty has fallen over time"], 2, "Data about five countries at one time show a pattern, not a cause or a trend."),
  ("[Application] A new factory pollutes a river used by a village downstream. This is an example of:", ["A positive consumption externality", "A negative production externality", "A private cost", "A public good"], 1, "The cost falls on a third party (the village) and arises in production."),
  ("[Diagram] Supply of a good shifts right while demand is unchanged. What happens to equilibrium price and quantity?", ["Price rises, quantity rises", "Price rises, quantity falls", "Price falls, quantity rises", "Price falls, quantity falls"], 2, "Sketch it: a rightward supply shift moves down the demand curve."),
  ("[Extreme wording] Which statement about tariffs is most likely to be correct?", ["Tariffs always raise welfare", "Tariffs never affect prices", "Tariffs may protect domestic jobs but raise prices to consumers", "Tariffs only affect exporters"], 2, "The correct option is hedged ('may'). Statements with always, never and only are easy to disprove.")
], "qz1") + CARDS([
  ("The four steps", "Read, predict, eliminate, check."),
  ("Negative stem", "Three true, one odd one out."),
  ("Real income per head", "Nominal growth − inflation − population growth."),
  ("Unemployment rate", "Unemployed ÷ (employed + unemployed)."),
  ("Neighbouring concept", "Laffer, Lorenz, Kuznets, Phillips: know each."),
  ("Combination tables", "Decide each column, then match the row."),
  ("No negative marking", "Answer every question."),
  ("Timing", "About 100 seconds a question, then flagged ones, then check.")]) + MCQ([
  ("[Negative] Which is not a source of market failure? (May/June 2022 · 31 · Q13, reworded)", ["Imperfect information", "Income inequality", "Monopoly power", "Non-excludability"], 1, "Inequality is an equity issue, not a failure of the market to allocate resources efficiently. The others are classic causes of market failure."),
  ("[Negative] Which is not a reason for small firms to survive in a market dominated by large firms? (Oct/Nov 2020 · 31 · Q12, reworded)", ["Small firms can concentrate on specialist services", "Small firms enjoy greater economies of scale", "Small firms enter with new ideas", "Small firms know local markets well"], 1, "Large firms, not small ones, usually enjoy the economies of scale."),
  ("[Negative] A government wants to reduce pollution from producing a good. Which policy does not make use of market forces? (May/June 2024 · 32 · Q11, reworded)", ["A quota to limit production", "A regulation banning production", "A tax on production", "A tradable pollution permit system"], 1, "A ban is direct regulation. Taxes and tradable permits use prices and trading."),
  ("[Concept] If consumers aim to maximise utility, how will they arrange their spending? (Oct/Nov 2024 · 32 · Q1, reworded)", ["Equal total utility from each commodity", "Equal total utility per $ on each commodity", "Equal utility from the last unit of each commodity", "Equal utility from the last $ spent on each commodity"], 3, "The equi-marginal principle: marginal utility per dollar is equal across goods. Options A to C mix up total, unit and per-dollar measures."),
  ("[Application] Helmets become compulsory for motorbike riders. What would be a positive externality of consumption? (Oct/Nov 2024 · 32 · Q4, reworded)", ["Less pressure on the provision of health care", "Costs of checking that riders comply", "Increased life expectancy of riders", "Higher profits for helmet makers"], 0, "An externality affects third parties. Riders' longer lives are a private benefit and manufacturers' profits are not an externality."),
  ("[Calculation] In one year national income in money terms rose 3%, prices rose 4% and population rose 1%. What was the approximate change in real income per head? (May/June 2020 · 31 · Q23, reworded)", ["−1%", "−2%", "+2%", "+3%"], 1, "3 − 4 − 1 = −2. Forgetting population gives −1%."),
  ("[Calculation] Employed 15m, unemployed 0.5m, not available for work 7m, working-age population 23m. What is the size of the labour force? (Oct/Nov 2021 · 32 · Q21, reworded)", ["15m", "15.5m", "22m", "22.5m"], 1, "The labour force is the employed plus the unemployed. Those not available for work are outside it."),
  ("[Calculation] Total population 2,000,000; labour force 1,200,000; employed 900,000; unemployed 300,000. What is the unemployment rate? (Oct/Nov 2024 · 31 · Q20, reworded)", ["25%", "33%", "60%", "75%"], 0, "300,000 ÷ 1,200,000 = 25%. 15% would come from dividing by total population."),
  ("[Combination] A multinational buys a manufacturing firm in a developing country that sells to local consumers, and then exports machinery and raw materials to it. What is the likely effect on the current account and the financial account? (May/June 2024 · 32 · Q28, reworded)", ["Both improve", "Current improves; financial worsens", "Current worsens; financial improves", "Both worsen"], 2, "Imports of machinery worsen the current account; the purchase is a capital inflow. Decide each column separately."),
  ("[Combination] FDI trains workers (raising productivity) but profits are sent home. How do aggregate demand and aggregate supply shift? (Oct/Nov 2020 · 33 · Q21, reworded)", ["AD left; AS left", "AD right; AS left", "AD left; AS right", "AD right; AS right"], 2, "Skills shift AS right; the profit outflow lowers domestic demand. Treat each curve on its own."),
  ("[Data] GDP and population: Bangladesh $206.7bn and 153.5m; India $2,989bn and 1,147.9m; Nigeria $292.7bn and 138.3m; South Africa $467.1bn and 43.8m. Which is likely to have the lowest standard of living? (May/June 2024 · 31 · Q28, reworded)", ["Bangladesh", "India", "Nigeria", "South Africa"], 0, "GDP per head: about $1,350, $2,600, $2,100 and $10,700. India has the largest GDP but is not lowest per head."),
  ("[Data] The table gives birth rate, death rate, infant mortality and the share under 16: Singapore 12, 4, 5, 18%; Hong Kong 15, 6, 8, 20%; China 20, 9, 28, 38%. Which conclusion can be drawn? (May/June 2024 · 32 · Q29, reworded)", ["China had the highest percentage of children who died in infancy", "People in Hong Kong lived the longest", "Singapore had the most people over 16", "Singapore's population was expected to fall"], 0, "Infant mortality of 28 per 1,000 is the highest. The other statements need data the table does not give.")
])

build("ap3", "a-level-paper3-mcq-technique", "Paper 3 Multiple Choice: Technique and Practice", EY,
  "How to score on Paper 3: the format, a four-step method, the seven question types, calculation and wording traps, timing, and twelve past questions by type. Animated diagrams, labs, drills and practice.",
  dict(paper=paper, method=method, types=types, traps=traps, practise=practise, past=past, tips=tips), js)
