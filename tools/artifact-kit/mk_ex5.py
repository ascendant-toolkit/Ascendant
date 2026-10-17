"""AS exam technique: Paper 2 data response and essays. Run: python3 tools/artifact-kit/mk_ex5.py"""
from as6k import *
EY = "AS Level Economics · 9708 · Exam technique"

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p>Paper 2 lasts <b>2 hours</b>, carries <b>60 marks</b> and has three sections, each worth <b>20 marks</b>: <b>Section A</b> is one compulsory <b>data response</b> question (Question 1, parts (a) to (e), on an unseen extract), <b>Section B</b> asks you to answer <b>one</b> microeconomics essay question from two, and <b>Section C</b> asks you to answer <b>one</b> macroeconomics and international question from two; each essay question has a part <b>(a) worth 8 marks</b> and a part <b>(b) worth 12 marks</b>. That is <b>2 minutes per mark</b>, and the marks are split between knowledge (AO1), analysis (AO2) and evaluation (AO3) in different proportions in each part, so the skill is to give each part <b>exactly what it is marked for and no more</b>. The short data parts reward <b>precise, data-based answers</b> with no padding; the 8 mark part rewards a <b>definition or diagram, a developed chain and a short judgement</b>; and the 12 mark part rewards <b>balanced, developed analysis and a justified evaluation</b>. Most marks lost are for answering a different question from the one asked (the command word or scope word), vague answers that could be about any economy, and poor use of time.</p></div>

  <h2>1 · The paper at a glance</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Section</th><th>Questions</th><th>Marks</th><th>Content</th></tr>
    <tr><td><b>A</b> Data response</td><td>Question 1: all parts</td><td>20</td><td>An extract with data and text, usually macroeconomic or international; parts (a) 2, (b) 2, (c) 4, (d) 6, (e) 6</td></tr>
    <tr><td><b>B</b> Microeconomics essay</td><td>One of Questions 2 and 3</td><td>20</td><td>Topics 1 to 3: for example PPC, subsidies, taxes, demerit goods; part (a) 8, part (b) 12</td></tr>
    <tr><td><b>C</b> Macroeconomics and international essay</td><td>One of Questions 4 and 5</td><td>20</td><td>Topics 4 to 6: for example circular flow, trade, fiscal policy; part (a) 8, part (b) 12</td></tr>
  </table></div>
  <ul>
    <li>You answer <b>three questions in total</b>, on the answer booklet. A calculator is allowed.</li>
    <li>You may answer <b>with reference to any economy you have studied</b>, where it is relevant to the question.</li>
    <li>Each part shows its marks in brackets: use them to decide how much to write.</li>
  </ul>

  <h2>2 · Using the 120 minutes</h2>
  <div class="tw"><table class="t">
    <tr><th>Stage</th><th>Minutes</th><th>Notes</th></tr>
    <tr><td><b>Read, choose and plan</b></td><td>5 to 8</td><td>Read the extract once for the overall story. Read both essay questions in B and in C; choose the one where you can answer both (a) and (b), and check the scope words.</td></tr>
    <tr><td><b>Section A</b></td><td>about 35</td><td>(a) 4, (b) 4, (c) 8, (d) 9, (e) 9: about 2 minutes per mark, slightly less for the shortest parts.</td></tr>
    <tr><td><b>Section B</b></td><td>about 35</td><td>Part (a) 13 minutes, part (b) 22 minutes, including 2 minutes planning the 12 mark answer.</td></tr>
    <tr><td><b>Section C</b></td><td>about 35</td><td>The same as Section B.</td></tr>
    <tr><td><b>Check</b></td><td>5 to 10</td><td>Read back; add a missing conclusion; check diagrams are labelled.</td></tr>
  </table></div>

  <h2>3 · Part by part: what each is marked for</h2>
  <div class="tw"><table class="t">
    <tr><th>Part</th><th>Marks</th><th>Typical command words</th><th>Marked for</th><th>What to write</th></tr>
    <tr><td><b>1(a)</b></td><td>2</td><td>Compare, describe, calculate, identify</td><td>Reading data (AO1/AO2)</td><td>An <b>explicit comparison</b> or calculation using figures: 1 to 2 sentences</td></tr>
    <tr><td><b>1(b)</b></td><td>2</td><td>Explain one reason, state, define</td><td>AO1 and AO2: 1 + 1</td><td>The point (1) and one development (1): 2 sentences</td></tr>
    <tr><td><b>1(c)</b></td><td>4</td><td>Consider, state two and consider which</td><td>3 analysis + 1 evaluation</td><td>Two developed points (or a point on each side) using the data, and one evaluative sentence</td></tr>
    <tr><td><b>1(d), 1(e)</b></td><td>6</td><td>Assess, discuss, use AD/AS analysis</td><td>4 analysis + 2 evaluation</td><td>Two developed chains (both sides or two causes), a diagram if asked, and a 2 sentence evaluation with a conclusion</td></tr>
    <tr><td><b>Essay (a)</b></td><td>8</td><td>Explain and consider; with the help of a diagram/formula</td><td>AO1 3, AO2 3, AO3 2</td><td>Definition or diagram, a developed chain, and a short judgement</td></tr>
    <tr><td><b>Essay (b)</b></td><td>12</td><td>Assess, discuss</td><td>AO1 + AO2 out of 8 (Table A), AO3 out of 4 (Table B)</td><td>Balanced developed analysis, evaluation with conditions, and a conclusion</td></tr>
  </table></div>

  <h2>4 · Section A: the data response</h2>
  <ul>
    <li><b>Skim the extract first:</b> what is the story (inflation falling, a recession fear)? Underline the figures. Note the units (%, $bn, index).</li>
    <li><b>Use the data:</b> mark schemes for (d) and (e) say the explanation should be "correctly applied to the data". Quote the figures: "from 0.25% in January 2022 to 4.5% in December 2022".</li>
    <li><b>(a) is not a description:</b> a comparison needs <b>both series and a link</b>: "the inflation rate rose and then fell while the interest rate rose continuously".</li>
    <li><b>Do not over-write (a) and (b):</b> two marks do not need a paragraph. Spend the time on (d) and (e).</li>
    <li><b>For 4 and 6 mark parts,</b> keep the evaluation short but specific: one reason the effect might be small or large, and a conclusion on the extent.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Part (from one real paper)</th><th>A full-mark answer looks like</th></tr>
    <tr><td><b>1(a), 2 marks:</b> compare changes in the inflation rate and the interest rate (data given)</td><td>"The inflation rate rose and then fell, while the interest rate rose continuously. The percentage rises in the interest rate were always greater than those in the inflation rate."</td></tr>
    <tr><td><b>1(b), 2 marks:</b> explain one reason why the CPI may not give an accurate inflation rate</td><td>"The CPI is based on a basket for the average household, but buying patterns change so the basket may no longer be typical."</td></tr>
    <tr><td><b>1(c), 4 marks:</b> consider whether disinflation is more harmful than deflation</td><td>Disinflation defined and its problems; deflation defined and its problems (3 marks); one evaluative point on the extent or duration (1 mark).</td></tr>
    <tr><td><b>1(d), 6 marks:</b> assess whether interest rate rises make a recession inevitable</td><td>Rates rose from 0.25% to 4.5%: borrowing dearer, AD and AS fall, unemployment rises, recession (up to 3); but demand may not be interest elastic and other factors affect AD and AS (up to 3); evaluation and conclusion (2).</td></tr>
  </table></div>

  <h2>5 · Essay part (a): 8 marks in about 13 minutes</h2>
  <p>The question has two halves: <b>explain</b> something, and <b>consider</b> a limit, extent or alternative. The marks follow the same split: <b>AO1 3, AO2 3, AO3 2</b>.</p>
  <div class="tw"><table class="t">
    <tr><th>Paragraph</th><th>What it contains</th><th>Marks</th><th>Size</th></tr>
    <tr><td><b>1 · Knowledge</b></td><td>The definition or formula the question needs, and the diagram if it says "with the help of a diagram" (labelled, with the shift)</td><td>AO1: up to 3</td><td>2 to 4 lines</td></tr>
    <tr><td><b>2 · Analysis</b></td><td>A developed chain from cause to effect, referring to the diagram, applied to the case</td><td>AO2: up to 3</td><td>5 to 7 lines</td></tr>
    <tr><td><b>3 · Consider</b></td><td>A condition that affects the result (elasticity, spare capacity, time), and a short conclusion in the question's words</td><td>AO3: up to 2</td><td>3 to 4 lines</td></tr>
  </table></div>
  <ul>
    <li>If the question says <b>two causes</b>, <b>two methods</b>, <b>one demand-side and one supply-side</b>, give exactly that, labelled.</li>
    <li>If it says "with the help of a formula" or "a diagram", that is an AO1 mark: do not omit it.</li>
    <li>Do not write a 12 mark answer for an 8 mark part: the extra length earns nothing.</li>
  </ul>

  <h2>6 · Essay part (b): 12 marks in about 22 minutes</h2>
  <div class="tw"><table class="t">
    <tr><th>Paragraph</th><th>What it contains</th><th>Size</th></tr>
    <tr><td><b>Opener</b> (optional)</td><td>One definition only if the question turns on a term, or one sentence naming the scope. Do not restate the question.</td><td>1 to 2 lines</td></tr>
    <tr><td><b>1 · Analysis: the case for</b></td><td>The strongest argument as a developed chain with a diagram where possible, applied to the good or economy</td><td>6 to 8 lines</td></tr>
    <tr><td><b>2 · Analysis: the case against or an alternative</b></td><td>A second developed chain: a limit, a cost or an alternative policy</td><td>6 to 8 lines</td></tr>
    <tr><td><b>3 · Evaluation</b></td><td>Two conditions (elasticity, time, spare capacity, context, trade-off), each as Condition, If, Then, then weigh one against the other</td><td>8 to 10 lines</td></tr>
    <tr><td><b>4 · Conclusion</b></td><td>A direct answer in the question's words, the main reason, and the condition that would change it. No new content.</td><td>2 to 3 lines</td></tr>
  </table></div>
  <p><b>If you are short of time:</b> drop the opener, keep paragraphs 1 and 3 in full, shorten paragraph 2, but never drop the conclusion: it is where much of the evaluation credit sits.</p>

  <h2>7 · Command words and scope words</h2>
  <div class="tw"><table class="t">
    <tr><th>Word</th><th>What it asks for</th><th>Not</th></tr>
    <tr><td><b>Explain</b></td><td>A chain: point, mechanism, consequence</td><td>A list; an opinion</td></tr>
    <tr><td><b>Consider</b></td><td>Review an argument and respond, leading to a judgement; in practice weigh both sides</td><td>A one-sided summary</td></tr>
    <tr><td><b>Assess, discuss, to what extent</b></td><td>Both sides developed, then a reasoned judgement that answers the question</td><td>Two lists with no verdict</td></tr>
    <tr><td><b>Compare</b></td><td>Similarities and differences, with figures</td><td>Two separate descriptions</td></tr>
    <tr><td><b>Calculate</b></td><td>The number, with formula and unit</td><td>An explanation</td></tr>
    <tr><td><b>ALL, ALWAYS, ONLY</b></td><td>Find a case where the claim fails; the scope word is part of the question</td><td>One example where it works</td></tr>
    <tr><td><b>For a named economy</b> (developing, open, trade-dependent)</td><td>Analysis and evaluation in that context; mark schemes cap answers that ignore it at Level 2</td><td>Generic analysis</td></tr>
  </table></div>

  <h2>8 · Diagrams, calculations and application</h2>
  <ul>
    <li><b>Diagrams:</b> draw one clear, large diagram, label axes and curves, show the shift and the new equilibrium, then <b>refer to it</b> in the text. Place it next to the paragraph it supports.</li>
    <li><b>Calculations:</b> write the formula, show working and give the unit; use the extract's figures.</li>
    <li><b>Application:</b> use the named good, the country in the extract, or an economy you know. A sentence that could be about any market is generic.</li>
    <li><b>Time between parts:</b> if you run out of time, finish with a brief conclusion rather than leaving (b) unfinished.</li>
  </ul>

  <h2>9 · Common ways to lose marks</h2>
  <ul>
    <li><b>Not answering the question (NAQ):</b> writing about the topic, ignoring the command word or the scope word.</li>
    <li><b>Vague answers:</b> "the economy suffers", "this could affect things". Name the mechanism.</li>
    <li><b>Writing too much for (a) and (b) in Section A,</b> and too little for (d) and (e).</li>
    <li><b>Writing a long (a) and a short (b):</b> (b) is worth more.</li>
    <li><b>One-sided essays:</b> capped at Level 2, with no evaluation marks.</li>
    <li><b>No conclusion</b>, or a conclusion that does not use the question's words.</li>
    <li><b>Unlabelled diagrams</b> or diagrams not referred to.</li>
    <li><b>Ignoring the data</b> in the extract.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Before writing each part, write in the margin: <b>marks</b>, <b>command word</b>, <b>scope word</b>. Then plan the number of paragraphs the marks justify (2 marks: 2 sentences; 6 marks: two chains and a short evaluation; 12 marks: four paragraphs).</div>
'''

watch = '''
  <h2>1 · Reading a question before writing</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · An 8 mark part in three paragraphs</h2>
  <div id="stB"></div>
  <h2>3 · A 12 mark answer in four paragraphs</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Time plan for the 120 minutes</h2>
  <p>Set the time for reading and checking and the time for Section A. The lab shows the minutes left for each essay question.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Minutes for each essay question</small><strong id="r1"></strong></div><div><small>Minutes per mark in Section A</small><strong id="r2"></strong></div><div><small>Minutes per mark in an essay</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 200" role="img" aria-label="A bar divided into reading, Section A, Section B, Section C and checking"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · What does this part want?", "Choose a part to see its marks, what it is marked for, the time to give it and the length to aim for.", ["Marked for", "What to write", "Time and length"]) + chooser_html("k", "Lab 3 · Read the question", "Choose a question to see the command word, the scope word and what a good answer must do.", ["Command word", "Scope or context", "A good answer must"])

practise = '''
  <h2>1 · Which part is it?</h2><div id="cl1" class="card"></div>
  <h2>2 · Where does the sentence belong in a 12 mark answer?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the planning steps in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the part to its marks</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Data part: an explicit comparison", "In a question asking for a comparison of the inflation rate and the interest rate from a table, the mark scheme said marks go to an explicit comparison, not to a description of the changes in each month: one series rose then fell, the other rose continuously, and the interest rate rose proportionately faster.", "linking both series in the answer.") +
rw("Data part: use the figures", "A 6 mark question on interest rate rises said the explanation should be applied to the data: rates rose from 0.25% to 4.5% over the year. Quoting those figures is how the answer is 'applied'.", "using the extract.") +
rw("An 8 mark part with two halves", "'Explain how the circular flow changes from a closed to an open economy and consider what determines the extent of the change.' The explanation earns knowledge and analysis marks; the 'consider' half earns the evaluation marks.", "writing both halves.") +
rw("Part (b) and the word 'always'", "'Assess whether expansionary fiscal policy always benefits an economy.' The word always asks for a case where it does not: when there is no spare capacity, or when debt is already high.", "the scope word.") +
rw("Choosing the essay", "Part (b) is worth 12 of the 20 marks in an essay question, so choosing a question because part (a) looks easy is a risk. Read both parts of both questions before choosing, and check the scope words in each part (b).", "choosing by the whole question.")
)

mc_exam = [
  mcq("s25_11", 6, "What is not a function of the price mechanism?", ["To act as a signal to firms when allocating resources", "To maximise consumer surplus", "To provide an incentive to firms to produce goods", "To ration scarce resources"], 1, "Paper 1 and Paper 2 share syllabus content; Paper 2 tests the same ideas through written answers."),
  mcq("s24_12", 3, "Earth observation satellites designed to acquire information are close to the theoretical case of a public good. In 2011, the World Meteorological Organisation estimated that improving satellite observations would cost an extra $1 billion a year. What is a normative statement about Earth observation satellites?", ["The estimated cost of improving satellite observations is $1 billion a year.", "The information received from the satellites is non-rival.", "The satellites are designed to benefit all countries.", "The government should pay for the improvement of satellite observations."], 3, "'Should' is a value judgement, which is also the language of an evaluation: be ready to justify it.")
]

exam = exam_page("Paper 2 technique: one real paper, part by part",
  "These are the parts of the May/June 2025 Paper 21, reworded, so that you can see how the marks are split in each type of question. Read the key for each: the knowledge (K), analysis (N) and evaluation (E) marks are coloured. The extract and tables are not reproduced because of copyright, so the data parts are described.",
  exam_rows([("s25_21","1(a)",2),("s25_21","1(b)",2),("s25_21","1(c)",4),("s25_21","1(d)",6),("s25_21","1(e)",6),("s25_21","3(a)",8),("s25_21","4(a)",8),("s25_21","5(a)",8),("s25_21","4(b)",12),("s25_21","5(b)",12)], ["s25_11","s24_12"]),
  [
  eq(P("s25_21", "1(a)"), "2 marks", "Data response: using a table of the inflation rate and the interest rate in the US in three months, compare the changes in the inflation rate and the changes in the interest rate.",
     ["Marks are for an explicit comparison of the changes in the two series, not for a description of each in turn: the inflation rate rose and then fell while the interest rate rose continuously (1); the proportionate changes in the interest rate were always greater than those in the inflation rate (1)."],
     "One sentence comparing the pattern, one using figures and proportions.",
     [[("k", "The inflation rate rose and then fell, while the interest rate rose continuously."), ("n", "The proportionate rises in the interest rate were always greater than the changes in the inflation rate.")]]),
  grab("s25_21", "1(b)"),
  grab("s25_21", "1(c)"),
  eq(P("s25_21", "1(d)"), "6 marks", "Assess whether increases in the interest rate make a recession in an economy inevitable. (The extract showed rates rising from 0.25% in January to 4.5% in December.)",
     ["Analysis (up to 4): inevitable: higher interest rates make borrowing more expensive for consumers and firms, so there is a fall in both AD and AS, leading to higher unemployment and a recession (up to 3); not inevitable: demand and supply may not be interest elastic and there are other factors that can influence AD and AS (up to 3).",
      "Evaluation (up to 2): relevant evaluation which considers both the likelihood of recession and the possibility of there not being one, and weighs up the factors (1); reserve 1 mark for a conclusion on whether the increases make a recession inevitable (1)."],
     "Inevitable: dearer borrowing, C and I fall, AD left (and costs rise, AS). Not inevitable: interest-inelastic demand, other factors. Weigh; conclude.",
     [[("n", "With the interest rate raised from 0.25% to 4.5%, borrowing is dearer for households and firms, so consumption and investment fall, AD shifts left, and rising costs may also reduce AS. Output falls and unemployment rises, so a recession is likely. But a recession is not inevitable: if households have fixed-rate loans or high savings, demand may not respond much to the interest rate, and other factors such as government spending or exports may offset the fall."), ("e", "A recession is therefore likely but not inevitable. The outcome depends on how sensitive demand is to interest rates and what else is happening to AD, so increases in the rate make a recession more likely rather than certain.")]]),
  grab("s25_21", "1(e)"),
  grab("s25_21", "3(a)"),
  grab("s25_21", "4(a)"),
  grab("s25_21", "5(a)"),
  grab("s25_21", "4(b)"),
  grab("s25_21", "5(b)")
  ],
  )

tips = tips_html(
  [("Write marks, command word and scope word first.", "In the margin before each part."),
   ("2 minutes a mark.", "But spend less on 1(a) and 1(b), more on (d) and (e)."),
   ("Use the data.", "Quote figures in Section A."),
   ("(a): knowledge, chain, judgement.", "Three paragraphs for 8 marks."),
   ("(b): analysis, analysis, evaluation, conclusion.", "Four paragraphs for 12 marks."),
   ("Always conclude in the question's words.", "Even if short of time."),
   ("Choose the essay by both parts.", "Read (a) and (b) of both questions.")],
  [("Section A", "Section A is the compulsory data response question worth 20 marks."),
   ("Section B and C", "Each is a choice of one essay question worth 20 marks: part (a) 8 and part (b) 12."),
   ("Table A", "Table A marks knowledge and analysis out of 8 in the 12 mark part."),
   ("Table B", "Table B marks evaluation out of 4 in the 12 mark part."),
   ("NAQ", "NAQ means the answer does not answer the question that was asked.")],
  [CW["explain"], CW["consider"], CW["assess"], CW["discuss"]]) + FC

js = CHAINJS + '''
$("#pic1").innerHTML = (() => {
  const B = [["Section A", "Q1 data response", "20 marks", 20, "f1"], ["Section B", "One micro essay: (a) 8 + (b) 12", "20 marks", 270, "f2"], ["Section C", "One macro essay: (a) 8 + (b) 12", "20 marks", 520, "f3"]];
  let o = ""; B.forEach(([n, d, m, x, c]) => { o += SV.rect(x, 12, 220, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 40, n, "lbl bd", { "text-anchor": "middle", style: "font-size:17px" }) + SV.text(x + 110, 62, d, "sm", { "text-anchor": "middle" }) + SV.text(x + 110, 84, m, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 114" role="img" aria-label="Paper 2 has three sections each worth 20 marks">${o}</svg>`;
})();
chainStep("#stA", "Reading a question before writing", ["Find the marks: 12 marks, so developed analysis and evaluation", "Underline the command word: 'Assess whether'", "Circle the scope word: 'always'", "Underline the context: 'expansionary fiscal policy' / 'an economy'", "Plan: one case where it works, one where it does not, two conditions, a conclusion with 'always'"], [
  "<b>Marks</b> decide the length and the paragraphs.", "<b>Command word:</b> both sides, then a judgement.", "<b>Scope word:</b> find a case where it fails.", "<b>Context:</b> stay on the policy and the economy named.", "<b>The plan</b> takes about 2 minutes."]);
chainStep("#stB", "An 8 mark part in three paragraphs", ["Paragraph 1 (AO1): definition and a labelled diagram, in 3 or 4 lines", "Paragraph 2 (AO2): a developed chain that refers to the diagram, in 5 to 7 lines", "Paragraph 3 (AO3): a condition and a short conclusion in the question's words, in 3 lines", "Check: both halves of the question answered ('explain' and 'consider')"], [
  "<b>Up to 3 knowledge marks.</b>", "<b>Up to 3 analysis marks.</b>", "<b>Up to 2 evaluation marks.</b>", "<b>Do not write more than 8 marks deserve.</b>"]);
chainStep("#stC", "A 12 mark answer in four paragraphs", ["Opener (optional, 1 to 2 lines): scope or one definition", "Paragraph 1: the case for, as a developed chain with a diagram (6 to 8 lines)", "Paragraph 2: the case against or an alternative, as a developed chain (6 to 8 lines)", "Paragraph 3: evaluation: two conditions as Condition, If, Then, then weigh them (8 to 10 lines)", "Conclusion: a direct answer in the question's words, with the reason and the condition (2 to 3 lines)"], [
  "<b>Skip it if short of time.</b>", "<b>Analysis (Table A).</b>", "<b>Balance: needed for Level 3.</b>", "<b>Evaluation (Table B).</b>", "<b>Never drop the conclusion.</b>"]);

function pl() {
  const ids = ["rd", "ck", "sa"];
  if (!ids.every((i) => $("#" + i))) return;
  const [rd, ck, sa] = ids.map((i) => +$("#" + i).value), left = 120 - rd - ck - sa, each = left / 2;
  $("#r1").textContent = Lib.fmtN(each, 1) + " min"; $("#r2").textContent = Lib.fmtN(sa / 20, 2) + " min"; $("#r3").textContent = Lib.fmtN(each / 20, 2) + " min";
  $("#rv").textContent = `Reading ${rd} min, checking ${ck} min and Section A ${sa} min leave ${left} minutes: about ${Lib.fmtN(each, 0)} minutes for each 20 mark essay question (about ${Lib.fmtN(each * 0.37, 0)} for part (a) and ${Lib.fmtN(each * 0.63, 0)} for part (b)). ` + (each < 33 ? "This is tight: the essays are worth as much as Section A, so protect their time." : each > 40 ? "Generous: you may be over-investing in the essays; check Section A has enough time." : "A sensible balance.");
  const W = 380, X = (v) => 20 + (v / 120) * W;
  const segs = [["Read", rd, "f3"], ["A", sa, "f1"], ["B", each, "f2"], ["C", each, "f2"], ["Check", ck, "f3"]]; let o = "", acc = 0;
  segs.forEach(([n, v, c]) => { o += SV.rect(X(acc), 70, X(acc + v) - X(acc), 50, c, op(0.5)) + SV.text(X(acc + v / 2), 100, n, "sm", { "text-anchor": "middle" }); acc += v; });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "rd", label: "Reading and planning, minutes ", min: 3, max: 12, step: 1, value: 6, fmt: (v) => v, onInput: pl });
Lib.slider($("#g2"), { id: "ck", label: "Final check, minutes ", min: 3, max: 12, step: 1, value: 7, fmt: (v) => v, onInput: pl });
Lib.slider($("#g3"), { id: "sa", label: "Section A, minutes ", min: 28, max: 50, step: 1, value: 36, fmt: (v) => v, onInput: pl });
pl();

chooser("h", [
  ["1(a): 2 marks, compare data", "Reading data: an explicit comparison", "One or two sentences with figures, linking both series", "About 3 to 4 minutes; 25 to 40 words", 3],
  ["1(b): 2 marks, explain one reason", "AO1 and AO2: 1 + 1", "The point, then a development", "About 4 minutes; 2 sentences", 3],
  ["1(c): 4 marks, consider", "3 analysis + 1 evaluation", "Two developed points using the data, and one evaluative sentence", "About 8 minutes; 70 to 100 words", 4],
  ["1(d), 1(e): 6 marks, assess", "4 analysis + 2 evaluation", "Two developed chains, a diagram if asked, a 2 sentence evaluation with a conclusion", "About 9 to 12 minutes; 120 to 170 words", 5],
  ["Essay (a): 8 marks", "AO1 3, AO2 3, AO3 2", "Definition or diagram, a developed chain, a short judgement", "About 13 to 16 minutes; 150 to 230 words", 5],
  ["Essay (b): 12 marks", "AO1 + AO2 out of 8, AO3 out of 4", "Balanced developed analysis, evaluation with conditions, a conclusion", "About 22 to 24 minutes; 350 to 500 words", 5]
], (it) => `${it[0]}. Marked for: ${it[1].toLowerCase()}. Write: ${it[2].toLowerCase()}. Time and length (a guide): ${it[3].toLowerCase()}.`, "Importance of the part");
chooser("k", [
  ["'Assess whether expansionary fiscal policy always benefits an economy.'", "Assess: both sides then a judgement", "ALWAYS: find a case where it does not (no spare capacity, high debt)", "Show benefits and costs, then say when it fails", 5],
  ["'Explain how the circular flow changes from a closed to an open economy and consider what determines the extent.'", "Explain, then consider", "The 'consider' half asks what determines the extent (size of X and M, openness)", "Explain the new flows (X, M); then name what determines how large the change is", 5],
  ["'Assess whether protectionism is the best way to reduce a current account deficit.'", "Assess: compare policies", "BEST: compare with at least one other policy", "Analyse protection and an alternative, then judge which is best", 5],
  ["'With the help of a diagram, explain how a subsidy affects the market and consider how the cost is affected by elasticity.'", "Explain with a diagram, then consider", "The diagram is an AO1 mark; the 'consider' half is about elasticity and cost", "Draw and label the diagram, explain, then link cost to PED", 4],
  ["'Discuss whether a government should always aim to balance its budget.'", "Discuss: both sides then a judgement", "ALWAYS and SHOULD: find the cases where it should not", "Compare balanced, deficit and surplus; judge over the cycle", 4]
], (it) => `${it[0]} Command word: ${it[1].toLowerCase()}. Scope word or context: ${it[2].toLowerCase()}. A good answer must: ${it[3].toLowerCase()}.`, "How much the scope word matters");
''' + CLASSIFY("cl1", "Which part is each question?", ["Data response (1a/1b)", "Data response (1c to 1e)", "Essay (a)", "Essay (b)"],
  [("Compare the changes in two series in a table (2 marks)", 0), ("Explain one reason why the CPI may be inaccurate (2 marks)", 0), ("Consider whether disinflation is more harmful than deflation (4 marks)", 1), ("Assess whether a policy is likely to be helpful using the extract (6 marks)", 1), ("With the help of a diagram, explain a change and consider the extent (8 marks)", 2), ("Assess whether a policy always benefits an economy (12 marks)", 3)],
  "Short data parts test reading and short explanations; 4 and 6 mark parts need analysis and a little evaluation; essays are 8 and 12 marks.") + CLASSIFY("cl2", "Where does the sentence belong in a 12 mark answer?", ["Analysis paragraph", "Evaluation paragraph", "Conclusion"],
  [("A minimum price raises price above equilibrium, so quantity demanded contracts.", 0), ("If demand is inelastic, consumption falls only a little, so the policy is less effective.", 1), ("Therefore a minimum price is unlikely to be the best policy on its own, because demand is likely to be inelastic.", 2), ("A tax shifts supply left, raising the price and cutting quantity.", 0), ("This depends on the time period: the effect may be larger in the long run.", 1), ("Overall, a tariff is only effective if demand for imports is elastic and there is no retaliation.", 2)],
  "Analysis explains how; evaluation introduces conditions; the conclusion answers the question.") + ORDER(
  "Put the steps in order for planning an essay part (b).",
  ["Read the question and find the marks, command word and scope word", "Choose the two sides or the policy and an alternative", "Plan the two evaluation conditions and the conclusion", "Write the analysis paragraphs with a diagram", "Write the evaluation and the conclusion in the question's words"],
  "Read, plan, analyse, evaluate, conclude.") + MATCH([
  ["Question 1(a)", "2 marks: an explicit comparison or calculation from the data"],
  ["Question 1(c)", "4 marks: 3 analysis and 1 evaluation"],
  ["Question 1(d)", "6 marks: 4 analysis and 2 evaluation"],
  ["Essay part (a)", "8 marks: AO1 3, AO2 3, AO3 2"],
  ["Essay part (b)", "12 marks: AO1 + AO2 out of 8 and AO3 out of 4"],
  ["Paper 2", "60 marks in 2 hours: three sections of 20 marks"]]) + CALC([
  {"q": "Paper 2 is 60 marks in 120 minutes. How many minutes per mark?", "a": 2, "unit": "min", "tol": 0.05, "hint": "120 ÷ 60.", "sol": "<b>2 minutes</b>."},
  {"q": "A 12 mark part gets 22 minutes. How many minutes per mark (1 decimal place)?", "a": 1.8, "unit": "min", "tol": 0.1, "hint": "22 ÷ 12.", "sol": "<b>1.8</b>."},
  {"q": "An essay question is (a) 8 marks and (b) 12 marks. What fraction of its marks is in part (b) (%)?", "a": 60, "unit": "%", "tol": 0.5, "hint": "12 ÷ 20.", "sol": "<b>60%</b>."},
  {"q": "In a 6 mark data response part, 2 marks are for evaluation. What percentage is that (1 decimal place)?", "a": 33.3, "unit": "%", "tol": 0.3, "hint": "2 ÷ 6.", "sol": "<b>33.3%</b>."},
  {"q": "Section A has parts worth 2, 2, 4, 6 and 6 marks. What is the total?", "a": 20, "unit": "marks", "tol": 0.1, "hint": "2 + 2 + 4 + 6 + 6.", "sol": "<b>20</b> marks."}]) + MCQ([
  ("How many questions must you answer in Paper 2?", ["Two", "Three", "Four", "Five"], 1, "Question 1, one from Section B and one from Section C."),
  ("How is a part (a) of 8 marks marked from 2023?", ["AO1 3, AO2 3, AO3 2", "AO2 8", "AO1 4, AO3 4", "AO3 8"], 0, "Point marks across the three objectives."),
  ("What does a scope word such as 'always' tell you?", ["Look for a case where the claim fails", "Write more", "Ignore it", "Define it"], 0, "The claim is rarely true in every case."),
  ("Which part should usually receive the most time per part?", ["Essay part (b)", "1(a)", "1(b)", "The introduction"], 0, "12 marks, with analysis and evaluation."),
  ("Why quote figures from the extract?", ["The mark scheme expects the analysis to be applied to the data", "It makes the answer longer", "It is compulsory in essays", "Examiners prefer numbers"], 0, "Application to the data earns analysis credit.")
], "qz1") + CARDS([
  ("Paper 2", "60 marks, 2 hours, 3 sections of 20."),
  ("Section A", "Data response: 2, 2, 4, 6, 6."),
  ("Essay (a)", "8 marks: AO1 3, AO2 3, AO3 2."),
  ("Essay (b)", "12 marks: Table A out of 8, Table B out of 4."),
  ("2 min a mark", "Less for 1(a) and 1(b)."),
  ("Scope words", "ALL, ALWAYS, ONLY: find the exception."),
  ("Use the data", "Quote figures."),
  ("Conclude", "In the question's words.")]) + MCQ(mc_exam)

build("ex5", "as-paper2-technique", "Paper 2 Data Response and Essays: Technique and Practice", EY,
  "How Paper 2 is built, a 120 minute plan, what each part is marked for, the structure of an 8 mark and a 12 mark answer, command and scope words, and one real paper worked part by part.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
