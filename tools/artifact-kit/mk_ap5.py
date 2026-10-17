"""A Level Economics revision plan and exam-day page. Run: python3 tools/artifact-kit/mk_ap5.py"""
import splitter
from syl import *
splitter.TABS = [("plan", "The plan"), ("map", "Topic tracker"), ("papers", "Past papers"), ("methods", "How to revise"), ("last", "Last week and exam day"), ("practise", "Practise"), ("tips", "Tips &amp; checklist")]
EY = "A Level Economics · 9708 · Revision plan"

plan = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A good plan has <b>three phases</b>: rebuild your knowledge, practise questions by topic, then sit <b>timed papers</b> and fix the gaps. Spend your time where the syllabus is biggest <b>and</b> where you are weakest, and use <b>active methods</b> (recall, practice questions, diagrams from memory) that are far better than re-reading. Space your reviews out, because <b>reviewing after a day, a week and a month beats cramming</b> the night before. This page gives you the planner, a topic tracker, a past paper routine, a last-week checklist and an exam-day plan.</p></div>

  <h2>1 · What you are preparing for</h2>
  <div class="tw"><table class="t">
    <tr><th>Paper</th><th>Time and marks</th><th>Weight of the A Level</th><th>What it is</th></tr>
    <tr><td><b>Paper 1</b></td><td>1 hour, 30 marks</td><td>17%</td><td>AS multiple choice (topics 1 to 6), if you take all four papers in one series</td></tr>
    <tr><td><b>Paper 2</b></td><td>2 hours, 60 marks</td><td>33%</td><td>AS data response and structured essays</td></tr>
    <tr><td><b>Paper 3</b></td><td>1 hour 15 minutes, 30 marks</td><td>17%</td><td>A Level multiple choice (topics 7 to 11, AS assumed)</td></tr>
    <tr><td><b>Paper 4</b></td><td>2 hours, 60 marks</td><td>33%</td><td>A Level data response (20 marks) and two 20-mark essays, one micro and one macro</td></tr>
  </table></div>
  <p>The A Level content (topics 7 to 11) is <b>122 numbered syllabus bullets</b>: topic 7 has 47, topic 8 has 17, topic 9 has 24, topic 10 has 9 and topic 11 has 25. AS knowledge is assumed, so the plan includes a recap.</p>
  <div id="pic1" class="card"></div>

  <h2>2 · The three phases</h2>
  <div id="stP"></div>
  <div class="tw"><table class="t">
    <tr><th>Phase</th><th>Share of your time</th><th>What you do</th><th>You are ready to move on when...</th></tr>
    <tr><td><b>1 · Rebuild</b></td><td>about 40%</td><td>Work through each topic: read, then close the book and write what you remember. Draw every diagram. Use the lesson pages and flashcards.</td><td>You can explain each syllabus bullet in your own words</td></tr>
    <tr><td><b>2 · Practise</b></td><td>about 40%</td><td>Answer past questions by topic, untimed first, then timed. Mark them with the mark scheme and log your errors.</td><td>Your error log shows fewer repeats</td></tr>
    <tr><td><b>3 · Perform</b></td><td>about 20%</td><td>Full timed papers under exam conditions, then fix the gaps they expose. Rehearse the exam-day routine.</td><td>You finish on time and your scores are steady</td></tr>
  </table></div>

  <h2>3 · The planner</h2>
  <p>Set how many weeks you have and how many hours a week you can study. Set your confidence in each topic (1 is very weak, 5 is very strong). The planner shares your time using the number of syllabus bullets in each topic, weighted towards the topics where you feel least confident.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div id="g4"></div><div id="g5"></div><div id="g6"></div><div id="g7"></div><div id="g8"></div>
    <div class="readout"><div><small>Total hours</small><strong id="r1"></strong></div><div><small>A Level topics 7 to 11</small><strong id="r2"></strong></div><div><small>Per phase (1 / 2 / 3)</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 330" role="img" aria-label="Bars showing the hours suggested for each A Level topic"></svg></div></div></div>
'''

map_ = '''
  <h2>Topic tracker</h2>
  <p>Rate each sub-topic <b>R</b> (red, I cannot do it), <b>A</b> (amber, I can do it with notes) or <b>G</b> (green, I can do it from memory). Your choices are saved in this browser. The bullet count shows how much of the syllabus each one covers. Each title links to the lesson page.</p>
  <div class="card"><div class="readout"><div><small>Green</small><strong id="k1">0</strong></div><div><small>Amber</small><strong id="k2">0</strong></div><div><small>Red / not rated</small><strong id="k3">24</strong></div></div>
  <div class="verdict" id="kv">Rate the topics to see where to focus.</div></div>
  <div id="trk"></div>

  <h2>Diagrams to draw from memory</h2>
  <div class="tw"><table class="t">
    <tr><th>Topic</th><th>Diagrams</th></tr>
    <tr><td><b>7 · Firms and consumers</b></td><td>Total and marginal utility; indifference curves with a budget line; demand from IC analysis (income and substitution effects); externalities; short-run and long-run cost curves; perfect competition, monopoly, monopolistic competition, kinked demand oligopoly; price discrimination</td></tr>
    <tr><td><b>8 · Government and labour</b></td><td>Tax, subsidy, price controls, tradable permits; Lorenz curve; labour market under perfect competition, monopsony, minimum wage and union; MRP; economic rent and transfer earnings</td></tr>
    <tr><td><b>9 · The macroeconomy</b></td><td>Circular flow with injections and withdrawals; multiplier; AD and AS (Keynesian and classical); output gap; business cycle; PPC and growth; credit creation; money market (liquidity preference) and loanable funds</td></tr>
    <tr><td><b>10 · Macro policy</b></td><td>Short-run and long-run Phillips curve; Laffer curve; fiscal, monetary and supply-side effects on AD and AS</td></tr>
    <tr><td><b>11 · International</b></td><td>Currency market (fixed and managed rates); J curve; tariff and trade creation and diversion; Kuznets curve; Lorenz curve for development; circular flow with exports</td></tr>
  </table></div>

  <h2>Formulas and calculations</h2>
  <div class="tw"><table class="t">
    <tr><th>Formula</th><th>Where it appears</th></tr>
    <tr><td>Real value = nominal ÷ price index × 100; real income per head ≈ nominal growth − inflation − population growth</td><td>9.2, 11.3</td></tr>
    <tr><td>Multiplier = 1 ÷ (1 − MPC) or 1 ÷ marginal propensity to withdraw</td><td>9.1</td></tr>
    <tr><td>Unemployment rate = unemployed ÷ labour force × 100</td><td>9.3</td></tr>
    <tr><td>MV = PT; credit multiplier = 1 ÷ reserve ratio</td><td>9.4</td></tr>
    <tr><td>Gini = A ÷ (A + B); dependency ratio = (under 15 + over 64) ÷ (15 to 64) × 100</td><td>11.4</td></tr>
    <tr><td>Marshall-Lerner: PEDx + PEDm greater than 1; terms of trade = export prices ÷ import prices × 100</td><td>11.2, 11.4</td></tr>
    <tr><td>Elasticities, profit = revenue − cost, average and marginal cost and revenue, concentration ratios</td><td>7.5, 7.6, AS topic 2</td></tr>
  </table></div>
'''

papers = '''
  <h2>A past paper routine that works</h2>
  <p>We counted the Paper 3 papers (24 papers, 1,155 questions) and the Paper 4 papers (40) from 2020 to 2025. The mark schemes for the questions are free to download from the exam board, and every lesson page has an exam questions tab with reworded versions.</p>
  <div class="tw"><table class="t">
    <tr><th>Stage</th><th>When</th><th>How</th></tr>
    <tr><td><b>1 · By topic, untimed</b></td><td>During phase 1 and 2</td><td>After revising a topic, do the exam questions tab and then 8 to 10 real past questions on that topic. Use the mark scheme straight away.</td></tr>
    <tr><td><b>2 · By section, timed</b></td><td>Middle of phase 2</td><td>Paper 3 in blocks of 10 questions in 25 minutes. Paper 4 Section A in 36 minutes, an essay in 36 minutes.</td></tr>
    <tr><td><b>3 · Full papers</b></td><td>Phase 3</td><td>Two or three complete papers under exam conditions: quiet room, no notes, exact timing. Do them about a week apart, so you have time to fix the errors.</td></tr>
    <tr><td><b>4 · Learn from the last ones</b></td><td>Final week</td><td>Re-do the questions you got wrong and re-read your error log. Do not start a new paper in the last 24 hours.</td></tr>
  </table></div>

  <h2>Mark honestly and keep an error log</h2>
  <ul>
    <li>Mark in a different colour with the mark scheme beside you. Check points, levels and what the examiner asks for.</li>
    <li>For every lost mark, write one line in the log: the question, the <b>type of mistake</b> and the fix.</li>
    <li>Review the log weekly. The mistakes that keep repeating are your priorities.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Type of mistake</th><th>Typical fix</th></tr>
    <tr><td><b>Knowledge gap</b></td><td>Go back to the lesson page, then write a flashcard and re-test in 3 days</td></tr>
    <tr><td><b>Misread the question or the qualifier</b></td><td>Underline command words and "not/least/most likely" every time</td></tr>
    <tr><td><b>Calculation slip</b></td><td>Write the formula first and check units; practise the same type twice</td></tr>
    <tr><td><b>Diagram error</b></td><td>Redraw it from memory three times and add labels</td></tr>
    <tr><td><b>No evaluation or no conclusion</b></td><td>Add a judgement sentence to every plan: see the Paper 4 essay page</td></tr>
    <tr><td><b>Ran out of time</b></td><td>Practise timed sections and set a hard stop for each part</td></tr>
  </table></div>

  <h2>Which technique page to use</h2>
  <ul>
    <li><b>Paper 3:</b> the Paper 3 multiple choice technique page (four-step method, question types, timing).</li>
    <li><b>Paper 4 Section A:</b> the Section A data response page (mark patterns, using the data, evaluating in short parts).</li>
    <li><b>Paper 4 Sections B and C:</b> the 20-mark essay page (application, analysis, evaluation, model essays).</li>
  </ul>
'''

methods = '''
  <h2>What works and what does not</h2>
  <div class="tw"><table class="t">
    <tr><th>Method</th><th>Why it works (or does not)</th><th>How to use it in economics</th></tr>
    <tr><td><b>Retrieval practice</b></td><td>Trying to recall strengthens memory far more than re-reading</td><td>Close the book, write everything you know on a topic, then check</td></tr>
    <tr><td><b>Spaced review</b></td><td>Revisiting just as you start to forget flattens the forgetting curve</td><td>Review a topic after 1 day, 3 days, 1 week, 2 weeks and a month</td></tr>
    <tr><td><b>Interleaving</b></td><td>Mixing topics trains you to choose the right idea for the question</td><td>Do mixed sets of questions: one micro, one macro, one international</td></tr>
    <tr><td><b>Practice questions</b></td><td>It is the closest thing to the exam</td><td>Past questions, marked with the mark scheme</td></tr>
    <tr><td><b>Diagram drills</b></td><td>Diagrams carry marks and show understanding</td><td>Draw, label and explain 3 diagrams from memory each day</td></tr>
    <tr><td><b>Teach it</b></td><td>Explaining shows the gaps in your understanding</td><td>Explain a chain of reasoning aloud, or write a 60-second summary</td></tr>
    <tr><td><b>Essay planning</b></td><td>Planning is faster than writing and builds structure</td><td>Plan a 20-mark essay in 5 minutes: three points, one evaluation each, conclusion</td></tr>
    <tr><td><b>Re-reading and highlighting</b></td><td>Feels productive, but gives a false sense of knowing</td><td>Use only as a first pass, never as the main method</td></tr>
  </table></div>

  <h2>The forgetting curve</h2>
  <p>This is a simple model, for illustration, of how much you remember. Without review memory drops quickly. Each review makes the memory last longer, so the gaps between reviews can grow. Choose how many reviews you do and how much each strengthens the memory.</p>
  <div class="card"><div class="grid2"><div><div id="g9"></div><div id="g10"></div>
    <div class="readout"><div><small>No reviews, day 30</small><strong id="t1"></strong></div><div><small>With reviews, day 30</small><strong id="t2"></strong></div><div><small>Review days</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Retention over 45 days with and without spaced reviews"></svg></div></div></div>

  <h2>A weekly rhythm</h2>
  <div class="tw"><table class="t">
    <tr><th>Day</th><th>Session</th></tr>
    <tr><td>Monday and Tuesday</td><td>New topic: lesson page, notes, diagrams, flashcards</td></tr>
    <tr><td>Wednesday</td><td>Review last week's topic from memory, then exam questions on it</td></tr>
    <tr><td>Thursday</td><td>Timed past question set (Paper 3 block or one essay or a Section A), mark it, update the error log</td></tr>
    <tr><td>Friday</td><td>Fix the errors; redo wrong questions; mixed recall</td></tr>
    <tr><td>Weekend</td><td>One longer session: a timed paper in phase 3, or catch-up and a rest day</td></tr>
  </table></div>
'''

last = '''
  <h2>The last week</h2>
  <p>Tick off each item. Your ticks are saved in this browser.</p>
  <div id="chk"></div>

  <h2>Paper 4: a 120 minute plan</h2>
  <div id="stX"></div>
  <ul>
    <li>Each section is worth 20 marks, so give each about 36 minutes. Keep to it: a 20-mark essay worth the same as the data response should not get 60 minutes.</li>
    <li>For the essay, plan for 4 to 5 minutes (three points with application, analysis and evaluation, and a conclusion), then write for about 30 minutes.</li>
    <li>Check Section B and C choices in the first 6 minutes: pick the question where you can draw the diagram and name an example without hesitating.</li>
  </ul>

  <h2>Paper 3: a 75 minute plan</h2>
  <ul>
    <li>First pass about 50 minutes (100 seconds each), second pass about 16 minutes, check about 9 minutes. There is no negative marking: answer every question.</li>
  </ul>

  <h2>Exam day</h2>
  <div class="tw"><table class="t">
    <tr><th>When</th><th>What to do</th></tr>
    <tr><td><b>The night before</b></td><td>Light review of your diagram and formula sheet only. Pack ID, pens, a calculator that is allowed, water. Sleep.</td></tr>
    <tr><td><b>The morning</b></td><td>Eat, arrive early, avoid last-minute panic conversations. Look at your formula sheet once.</td></tr>
    <tr><td><b>First 5 minutes</b></td><td>Read the whole paper. Underline command words and marks. Choose the essays. Note times for each section.</td></tr>
    <tr><td><b>During</b></td><td>Stick to your time per section. If stuck, move on and return. Draw diagrams neatly with labels.</td></tr>
    <tr><td><b>Last 5 to 10 minutes</b></td><td>Check every part has an answer, diagram labels, units and conclusions.</td></tr>
    <tr><td><b>Between papers</b></td><td>Do not post-mortem. Rest, eat and move on to the next paper.</td></tr>
  </table></div>
'''

practise = '''
  <h2>1 · Active or passive revision?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the revision cycle in order</h2><div id="o1" class="card"></div>
  <h2>4 · Planning calculations</h2><div id="c1"></div>
  <h2>5 · Check your plan</h2><div id="qz1"></div>
'''

tips = tips_html(
  [("Start with a recap of AS.", "A Level questions assume AS topics, so patch gaps first."),
   ("Weight your time.", "More time for bigger topics (7, 11, 9) and for the ones you rate red."),
   ("Close the book.", "Recall first, then check. If you can't write it from memory, you don't know it yet."),
   ("Space it out.", "Review after 1 day, 3 days, a week, two weeks and a month."),
   ("Draw every diagram.", "Draw, label and explain each one without looking."),
   ("Practise like the exam.", "Timed, quiet, no notes, then mark with the mark scheme."),
   ("Rest before the exam.", "Sleep, food and a calm morning improve marks more than another late night.")],
  [("Plan", "I will spend 40% of my time rebuilding knowledge, 40% on practice questions and 20% on timed papers."),
   ("Error log", "I lost this mark because I forgot the Marshall-Lerner condition, so I will make a flashcard and retest it in three days."),
   ("Weighting", "I rated topic 11.4 red, so it gets more of my hours than topic 10.1."),
   ("Review", "I will test myself on this topic again in a week, then in a month."),
   ("Exam day", "I will read the whole paper first and note my time for each section.")],
  [("Recall", "Write what you remember without looking."),
   ("Retrieval practice", "Testing yourself to strengthen memory."),
   ("Spaced review", "Revisiting at growing gaps."),
   ("Interleaving", "Mixing topics in practice."),
   ("Error log", "A record of mistakes and fixes.")]) + FC

js = '''
/* ---------- topic data ---------- */
const TOP = [["7", "Firms, costs and market structures", 47, "f1"], ["8", "Government, equity and labour", 17, "f2"], ["9", "The macroeconomy and money", 24, "f3"], ["10", "Macro policy", 9, "f2"], ["11", "International and development", 25, "f1"]];
const SUB = [["7.1", "Utility", 5], ["7.2", "Indifference curves and budget lines", 4], ["7.3", "Efficiency and market failure", 6], ["7.4", "Private and social costs and benefits, externalities", 7], ["7.5", "Costs, revenue and profit; short and long run", 10], ["7.6", "Different market structures", 5], ["7.7", "Growth and survival of firms", 5], ["7.8", "Differing objectives and policies of firms", 5], ["8.1", "Government policies for efficiency and market failure", 2], ["8.2", "Equity and redistribution of income and wealth", 5], ["8.3", "Labour market forces and intervention", 10], ["9.1", "The circular flow of income", 3], ["9.2", "Economic growth and sustainability", 6], ["9.3", "Employment and unemployment", 7], ["9.4", "Money and banking", 8], ["10.1", "Government macroeconomic policy objectives", 1], ["10.2", "Links between macroeconomic problems", 5], ["10.3", "Effectiveness of policy options", 3], ["11.1", "Policies to correct balance of payments disequilibrium", 3], ["11.2", "Exchange rates", 5], ["11.3", "Economic development", 4], ["11.4", "Countries at different levels of development", 3], ["11.5", "Relationships between countries at different levels", 7], ["11.6", "Globalisation", 3]];

/* ---------- bullets chart ---------- */
$("#pic1").innerHTML = (() => { let o = SV.line(70, 190, 730, 190) + SV.line(70, 190, 70, 20) + SV.text(76, 16, "Numbered syllabus bullets (122 in total)", "sm"); TOP.forEach(([n, l, v, c], i) => { const x = 110 + i * 125, h = v * 3.2; o += SV.rect(x, 190 - h, 70, h, c, op(0.75)) + SV.text(x + 35, 210, "Topic " + n, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 35, 190 - h - 8, v, "lbl bd", { "text-anchor": "middle" }); }); return `<svg viewBox="0 0 760 225" role="img" aria-label="Syllabus bullets by topic: topic 7 has 47, topic 8 has 17, topic 9 has 24, topic 10 has 9 and topic 11 has 25">${o}</svg>`; })();

/* ---------- three phases stepper ---------- */
const PX = (w) => 70 + w * 6.6;
function phDraw(s) {
  let o = SV.line(70, 150, 730, 150) + SV.text(70, 28, "Start", "sm") + SV.text(730, 28, "Exam", "sm", { "text-anchor": "end" });
  const blk = (a, b, c, l, sub, k) => (k > 0 ? SV.rect(PX(a), 60, PX(b) - PX(a), 76, c, op(0.65 * k)) + SV.text((PX(a) + PX(b)) / 2, 92, l, "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text((PX(a) + PX(b)) / 2, 112, sub, "sm", { "text-anchor": "middle", ...op(k) }) : "");
  o += blk(0, 40, "f1", "1 · Rebuild", "about 40%", s.a) + blk(40, 80, "f3", "2 · Practise", "about 40%", s.b) + blk(80, 100, "f2", "3 · Perform", "20%", s.c);
  if (s.d > 0) o += tag(400, 200, "Spaced reviews of earlier topics run through all three phases.", "t4", s.d, "middle") + SV.line(PX(0), 176, PX(100), 176, "c4 dash", op(s.d));
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 230, label: "Three revision phases: rebuild, practise, perform", base: { a: 0, b: 0, c: 0, d: 0 }, draw: phDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Phase 1 · Rebuild.</b> Cover each topic: read the lesson, close the book, write what you remember, draw each diagram and make flashcards for what you missed.", s: { a: 1 } },
  { cap: "<b>Phase 2 · Practise.</b> Answer past questions by topic, untimed first, then timed. Mark them with the mark scheme and keep an error log.", s: { a: 1, b: 1 } },
  { cap: "<b>Phase 3 · Perform.</b> Full timed papers under exam conditions, then fix the weaknesses they expose. Rehearse the exam-day routine.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Throughout.</b> Review earlier topics at growing gaps so you do not forget phase 1 by the time you reach phase 3.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Planner ---------- */
function labPlan() {
  if (!$("#wk") || !$("#hr") || !$("#rc") || TOP.some((t, i) => !$("#cf" + i))) return;
  const wk = +$("#wk").value, hr = +$("#hr").value, rc = +$("#rc").value / 100, total = wk * hr, recap = total * rc, pool = total - recap;
  const conf = TOP.map((t, i) => +$("#cf" + i).value), w = TOP.map((t, i) => t[2] * (6 - conf[i])), sw = w.reduce((a, b) => a + b, 0), hrs = w.map((x) => pool * x / sw);
  $("#r1").textContent = Lib.fmtN(total, 0) + " h"; $("#r2").textContent = Lib.fmtN(pool, 0) + " h"; $("#r3").textContent = Lib.fmtN(total * 0.4, 0) + " / " + Lib.fmtN(total * 0.4, 0) + " / " + Lib.fmtN(total * 0.2, 0);
  const top = hrs.indexOf(Math.max(...hrs));
  $("#rv").textContent = `${wk} weeks at ${hr} hours is ${Lib.fmtN(total, 0)} hours. Setting aside ${Lib.fmtN(recap, 0)} hours for an AS recap leaves ${Lib.fmtN(pool, 0)} hours for topics 7 to 11. Topic ${TOP[top][0]} gets the most (${Lib.fmtN(hrs[top], 0)} hours) because of its size and your confidence rating. As a guide, that is about ${Lib.fmtN(pool / wk, 1)} hours of A Level topic study each week, with the first 40% of the time for rebuilding, the next 40% for practice and the last 20% for timed papers. Move the confidence sliders as your practice results change.`;
  const Y = (v) => 300 - v * (240 / Math.max(10, ...hrs)); let o = SV.line(40, 300, 410, 300) + SV.line(40, 300, 40, 24) + SV.text(46, 16, "Hours", "sm");
  TOP.forEach(([n, l, v, c], i) => { const x = 55 + i * 70, yy = Y(hrs[i]); o += SV.rect(x, yy, 52, 300 - yy, c, op(0.75)) + SV.text(x + 26, 320, "Topic " + n, "sm", { "text-anchor": "middle" }) + tag(x + 26, yy - 6, Lib.fmtN(hrs[i], 0), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "wk", label: "Weeks until the exam ", min: 4, max: 24, step: 1, value: 12, fmt: (v) => v, onInput: labPlan });
Lib.slider($("#g2"), { id: "hr", label: "Study hours a week for economics ", min: 3, max: 16, step: 1, value: 6, fmt: (v) => v, onInput: labPlan });
Lib.slider($("#g3"), { id: "rc", label: "Share of time for the AS recap, % ", min: 5, max: 35, step: 5, value: 15, fmt: (v) => v + "%", onInput: labPlan });
[["g4", 0], ["g5", 1], ["g6", 2], ["g7", 3], ["g8", 4]].forEach(([g, i]) => Lib.slider($("#" + g), { id: "cf" + i, label: "Confidence, topic " + TOP[i][0] + ": " + TOP[i][1] + " ", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labPlan }));
labPlan();

/* ---------- Topic tracker ---------- */
function saveGet() { try { return JSON.parse(localStorage.getItem("econ-revision-tracker") || "{}"); } catch (e) { return {}; } }
function saveSet(o) { try { localStorage.setItem("econ-revision-tracker", JSON.stringify(o)); } catch (e) {} }
(function () {
  const st = saveGet(), box = $("#trk"); if (!box) return;
  const row = (s, i) => { const slug = "s" + s[0].replace(".", "-"); return `<tr><td><b>${s[0]}</b></td><td><a href="../../a-econ/a-level/${slug}/">${s[1]}</a></td><td style="text-align:center">${s[2]}</td><td><select class="rag" data-id="${s[0]}" aria-label="Rating for ${s[0]}"><option value="">–</option><option value="R">R</option><option value="A">A</option><option value="G">G</option></select></td></tr>`; };
  box.innerHTML = `<div class="tw"><table class="t"><tr><th>Topic</th><th>Title (lesson page)</th><th>Bullets</th><th>Rating</th></tr>${SUB.map(row).join("")}</table></div>`;
  const upd = () => { let g = 0, a = 0, gb = 0, tb = 0; SUB.forEach((s) => { tb += s[2]; const v = st[s[0]]; if (v === "G") { g++; gb += s[2]; } else if (v === "A") a++; }); $("#k1").textContent = g; $("#k2").textContent = a; $("#k3").textContent = 24 - g - a; $("#kv").textContent = g + a === 0 ? "Rate the topics to see where to focus." : `${Lib.fmtN(gb / tb * 100, 0)}% of the syllabus bullets are in topics you rate green. Start with the red or unrated ones that have the most bullets: ` + (SUB.filter((s) => st[s[0]] !== "G" && st[s[0]] !== "A").sort((x, y) => y[2] - x[2]).slice(0, 3).map((s) => s[0]).join(", ") || "none, well done") + "."; };
  $$(".rag", box).forEach((sel) => { sel.value = st[sel.dataset.id] || ""; sel.onchange = () => { st[sel.dataset.id] = sel.value; saveSet(st); upd(); }; });
  upd();
})();

/* ---------- Forgetting curve ---------- */
function labF() {
  if (!$("#nr") || !$("#mm")) return;
  const nr = +$("#nr").value, m = +$("#mm").value / 10, days = [1, 3, 7, 14, 28].slice(0, nr);
  const ret = (t, rev) => { let S = 1.5, last = 0; rev.forEach((d) => { if (d <= t) { S *= m; last = d; } }); return Math.exp(-(t - last) / S); };
  $("#t1").textContent = Lib.fmtN(ret(30, []) * 100, 0) + "%"; $("#t2").textContent = Lib.fmtN(ret(30, days) * 100, 0) + "%"; $("#t3").textContent = days.length ? days.join(", ") : "none";
  $("#tv").textContent = nr === 0 ? "With no reviews you keep very little after a month. Cramming the night before gives a short boost that fades quickly." : `With reviews on day ${days.join(", ")} the memory lasts much longer each time. By day 30 you retain about ${Lib.fmtN(ret(30, days) * 100, 0)}%, against ${Lib.fmtN(ret(30, []) * 100, 0)}% with no review. This is a simplified model, but real experiments show the same pattern: spaced practice beats massed practice.`;
  const X = (t) => 40 + t * 8, Y = (v) => 270 - v * 240; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 292, "Days", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Memory strength", "sm");
  const p0 = [], p1 = []; for (let t = 0; t <= 45; t += 0.5) { p0.push([X(t), Y(ret(t, []))]); p1.push([X(t), Y(ret(t, days))]); }
  o += SV.path(Lib.ptsPath(p0), "c2 dash", op(0.6)) + SV.path(Lib.ptsPath(p1), "c1"); days.forEach((d) => (o += SV.line(X(d), 270, X(d), 30, "c4 dash", op(0.45)) + SV.text(X(d), 286, "R", "sm", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g9"), { id: "nr", label: "Number of reviews (days 1, 3, 7, 14, 28) ", min: 0, max: 5, step: 1, value: 4, fmt: (v) => v, onInput: labF });
Lib.slider($("#g10"), { id: "mm", label: "How much each review strengthens memory × 10 ", min: 15, max: 35, step: 1, value: 23, fmt: (v) => "×" + (v / 10).toFixed(1), onInput: labF });
labF();

/* ---------- Last week checklist ---------- */
const CK = [["T−7", "Sit a full timed Paper 4 and mark it with the mark scheme"], ["T−6", "Fix the errors from that paper; update the error log"], ["T−5", "Sit a full timed Paper 3 (75 minutes) and mark it"], ["T−5", "Redraw every diagram on your list from memory"], ["T−4", "Recall session on your amber and red topics only"], ["T−3", "Re-do wrong questions; write three 5-minute essay plans"], ["T−3", "Make a one-page sheet of formulas and key definitions"], ["T−2", "Light recall of all topics; no new papers"], ["T−1", "Read the formula and diagram sheet once; pack your bag; sleep early"], ["Exam", "Read the whole paper first; plan your time; answer every question"]];
(function () {
  const box = $("#chk"); if (!box) return; let st = {}; try { st = JSON.parse(localStorage.getItem("econ-revision-check") || "{}"); } catch (e) {}
  box.innerHTML = `<div class="tw"><table class="t"><tr><th>When</th><th>Do this</th><th>Done</th></tr>${CK.map((c, i) => `<tr><td><b>${c[0]}</b></td><td>${c[1]}</td><td style="text-align:center"><input type="checkbox" data-i="${i}" aria-label="Done: ${c[1]}"></td></tr>`).join("")}</table></div>`;
  $$("input[type=checkbox]", box).forEach((cb) => { cb.checked = !!st[cb.dataset.i]; cb.onchange = () => { st[cb.dataset.i] = cb.checked; try { localStorage.setItem("econ-revision-check", JSON.stringify(st)); } catch (e) {} }; });
})();

/* ---------- Paper 4 plan ---------- */
const QX = (m) => 70 + m * 5.5;
function p4Draw(s) {
  let o = SV.line(70, 150, 730, 150) + SV.text(70, 28, "0", "sm") + SV.text(730, 28, "120 min", "sm", { "text-anchor": "end" });
  [0, 30, 60, 90, 120].forEach((m) => (o += SV.line(QX(m), 144, QX(m), 156) + SV.text(QX(m), 176, m, "sm", { "text-anchor": "middle" })));
  const blk = (a, b, c, l, sub, k) => (k > 0 ? SV.rect(QX(a), 60, QX(b) - QX(a), 76, c, op(0.65 * k)) + SV.text((QX(a) + QX(b)) / 2, 92, l, "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text((QX(a) + QX(b)) / 2, 112, sub, "sm", { "text-anchor": "middle", ...op(k) }) : "");
  o += blk(0, 6, "f2", "Read", "6", s.a) + blk(6, 42, "f1", "Section A", "20 marks, 36 min", s.b) + blk(42, 78, "f3", "Section B", "20 marks, 36 min", s.c) + blk(78, 114, "f3", "Section C", "20 marks, 36 min", s.d) + blk(114, 120, "f2", "Check", "6", s.e);
  return o;
}
Lib.stepper($("#stX"), { w: 760, h: 215, label: "A 120 minute plan for Paper 4: read, Sections A, B and C, check", base: { a: 0, b: 0, c: 0, d: 0, e: 0 }, draw: p4Draw, tween: 700, dwell: 5600, steps: [
  { cap: "<b>Read, 6 minutes.</b> Read the whole paper. Choose your essays. Underline command words and marks.", s: { a: 1 } },
  { cap: "<b>Section A, 36 minutes.</b> The 20-mark data response, parts in order, with the biggest part last.", s: { a: 1, b: 1 } },
  { cap: "<b>Section B, 36 minutes.</b> A micro essay: plan 5 minutes, write about 30.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Section C, 36 minutes.</b> A macro essay with the same plan.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>Check, 6 minutes.</b> Diagrams labelled, every part answered, conclusions written.", s: { a: 1, b: 1, c: 1, d: 1, e: 1 } },
] });

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Is it active or passive revision?", ["Active", "Passive"],
  [("Closing the book and writing everything you remember about the money market", 0), ("Re-reading your notes three times", 1), ("Answering past questions and marking them with the mark scheme", 0), ("Highlighting a textbook chapter in four colours", 1), ("Drawing a diagram from memory and labelling it", 0), ("Copying out the lesson page word for word", 1), ("Explaining the multiplier aloud to a friend", 0), ("Watching a video without taking notes or pausing", 1)],
  "Active methods make you produce answers. Passive methods only expose you to information.") + MATCH([
  ["Retrieval practice", "Testing yourself to recall information from memory"],
  ["Spaced review", "Revisiting topics at growing gaps"],
  ["Interleaving", "Mixing different topics in one practice session"],
  ["Error log", "A record of lost marks, the type of mistake and the fix"],
  ["Timed paper", "A past paper done under exam conditions"],
  ["Phase 3", "Full timed papers and fixing weaknesses"]]) + ORDER(
  "Put the revision cycle in order.",
  ["Learn the topic from the lesson page", "Close the book and recall it", "Answer past questions on it", "Mark the answers and log the errors", "Review it again after a few days, then a week"],
  "Learn, recall, practise, review, repeat with growing gaps.") + CALC([
  {"q": "You have 12 weeks and study 6 hours a week. How many hours is that in total?", "a": 72, "unit": "h", "tol": 0.5, "hint": "12 × 6.", "sol": "<b>72 hours</b>."},
  {"q": "15% of those 72 hours go on an AS recap. How many hours are left for topics 7 to 11 (1 decimal place)?", "a": 61.2, "unit": "h", "tol": 0.1, "hint": "72 × 0.85.", "sol": "<b>61.2 hours</b>."},
  {"q": "Topic 7 has 47 of the 122 syllabus bullets. What percentage is that (1 decimal place)?", "a": 38.5, "unit": "%", "tol": 0.1, "hint": "47 ÷ 122.", "sol": "<b>38.5%</b>."},
  {"q": "Paper 4 lasts 120 minutes with 60 marks. How many minutes per mark (1 decimal place)?", "a": 2, "unit": "min", "tol": 0.05, "hint": "120 ÷ 60.", "sol": "<b>2.0 minutes per mark</b>, including reading and checking."},
  {"q": "Paper 3 has 30 questions in 75 minutes. How many minutes is that per question (1 decimal place)?", "a": 2.5, "unit": "min", "tol": 0.05, "hint": "75 ÷ 30.", "sol": "<b>2.5 minutes</b>, or about 100 seconds on a first pass."}]) + MCQ([
  ("Which is the best use of a past paper?", ["Do it timed, mark it with the mark scheme and log your errors", "Read the questions and look at the answers", "Do it once in the last hour", "Skip the questions you are unsure about"], 0, "Timed practice, honest marking and an error log turn each paper into learning."),
  ("Why space your reviews out?", ["It helps you remember for longer", "It saves time in total", "It stops you needing to practise questions", "It is easier"], 0, "Each review at a growing gap makes the memory last longer."),
  ("Which topic should get the most time, other things equal?", ["The largest topic that you rate weak", "The smallest topic that you rate strong", "The topic you like most", "The topic you did last"], 0, "Size of syllabus and your weakness together set priorities."),
  ("What should you do in the last 24 hours?", ["Light recall, check your sheet, sleep", "Start three new papers", "Study all night", "Learn new topics"], 0, "Rest and a calm routine help performance."),
  ("An error log is most useful when you:", ["Review it weekly for repeated mistakes", "Never read it again", "Only note correct answers", "Use it to avoid hard questions"], 0, "Repeated mistakes show your priorities."),
  ("In Paper 4, how long should each 20-mark section take?", ["About 36 minutes", "About 10 minutes", "About 60 minutes", "About 90 minutes"], 0, "Each section is worth a third of the marks; keep to time."),
  ("Which of these is passive?", ["Highlighting your notes", "Drawing a diagram from memory", "Answering a past question", "Teaching a friend"], 0, "Highlighting does not make you retrieve anything."),
  ("What do you do first when the exam starts?", ["Read the whole paper and plan your time", "Answer question 1 immediately", "Start the longest essay", "Draw diagrams"], 0, "Reading first lets you choose essays and set times.")
], "qz1") + CARDS([
  ("Three phases", "Rebuild, practise, perform."),
  ("Time split", "About 40%, 40%, 20%."),
  ("Spaced review", "After 1 day, 3 days, 1 week, 2 weeks, 1 month."),
  ("Active revision", "Recall, past questions, diagrams, teaching."),
  ("Error log", "Question, mistake type, fix."),
  ("Paper 3", "75 minutes: 50 first pass, 16 second, 9 check."),
  ("Paper 4", "120 minutes: 6 read, 36 per section, 6 check."),
  ("Last 24 hours", "Light recall and sleep.")])

build("ap5", "a-level-revision-plan", "A Level Economics Revision Plan and Exam Day", EY,
  "A revision plan for A Level Economics: three phases, a planner that weights your time by syllabus size and confidence, a topic tracker, a past paper routine, how to revise, and a last-week and exam-day plan. Animated diagrams, labs, drills and practice.",
  dict(plan=plan, map=map_, papers=papers, methods=methods, last=last, practise=practise, tips=tips), js)
