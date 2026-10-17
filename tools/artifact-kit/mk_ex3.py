"""AS exam technique: AO3 evaluation, how each mark and level is reached. Run: python3 tools/artifact-kit/mk_ex3.py"""
from as6k import *
EY = "AS Level Economics · 9708 · Exam technique"

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p><b class="kw">AO3 is evaluation</b>: recognising assumptions and limitations of economic information and models, assessing the strengths and weaknesses of arguments, recognising that some decisions involve <b>priorities and value judgements</b>, and communicating <b>reasoned judgements and conclusions</b> based on the arguments. In the 12 mark question it is marked out of <b>4 in Table B</b> in two levels: <b>Level 1 (1 to 2)</b> is a vague or general conclusion and simple evaluative comments with no development, and <b>Level 2 (3 to 4)</b> is a <b>justified conclusion that addresses the specific requirements of the question</b> together with <b>developed, reasoned and well-supported</b> evaluative comments. In the 8 mark part it is worth <b>2 marks</b>, in a 6 mark data response part <b>2 marks</b>, and in a 4 mark part <b>1 mark</b>. Evaluation marks are only available when the analysis is two-sided: mark schemes say <i>"a one-sided response cannot gain any marks for evaluation"</i>. This page shows exactly what earns each mark, with examples.</p></div>

  <h2>1 · Where AO3 marks are, and what they are worth</h2>
  <div class="tw"><table class="t">
    <tr><th>Question type</th><th>Marks</th><th>AO3 marks</th><th>What the mark scheme typically awards</th></tr>
    <tr><td><b>Data response, "explain" or "state"</b></td><td>2</td><td>0</td><td>None: these parts test knowledge and analysis</td></tr>
    <tr><td><b>Data response (c)</b>: "consider"</td><td>4</td><td>1</td><td>One mark for a relevant evaluative point, such as the extent, the time period or how it compares with other countries</td></tr>
    <tr><td><b>Data response (d), (e)</b>: "assess", "discuss"</td><td>6</td><td>2</td><td>A comment that weighs both sides (1) and a conclusion on the extent (1)</td></tr>
    <tr><td><b>Essay part (a)</b>: "consider"</td><td>8</td><td>2</td><td>A valid explanation of a limit or condition (1) and a justified conclusion (1)</td></tr>
    <tr><td><b>Essay part (b)</b>: "assess", "discuss"</td><td>12</td><td>4</td><td>Table B: Level 1 (1 to 2) or Level 2 (3 to 4); one mark is usually reserved for the conclusion</td></tr>
  </table></div>
  <p class="note">So a third of the 12 mark question is evaluation: about <b>6 to 10 lines</b> of a 12 mark answer. In papers up to 2022 the 12 mark evaluation was 4 marks with <b>one mark reserved for a conclusion</b>, and the 8 mark part gave evaluation within the application marks.</p>

  <h2>2 · Table B: the two levels in plain English</h2>
  <div class="tw"><table class="t">
    <tr><th>Level and marks</th><th>What the mark scheme says</th><th>What it looks like</th></tr>
    <tr><td><b>Level 2</b><br>3 to 4</td><td>Provides a <b>justified conclusion or judgement that addresses the specific requirements of the question</b>. Makes <b>developed, reasoned and well-supported</b> evaluative comment(s).</td><td>One or two evaluative points, each with a named <b>condition</b>, a <b>reason</b> and a <b>consequence</b>, followed by a conclusion that answers the question in its own words ("best", "always", "to what extent") and says <b>why</b>.</td></tr>
    <tr><td><b>Level 1</b><br>1 to 2</td><td>Provides a <b>vague or general</b> conclusion or judgement. Makes <b>simple</b> evaluative comment(s) with <b>no development and little supporting evidence</b>.</td><td>"It depends on many factors", a summary of the earlier points with "overall it has advantages and disadvantages", or a single comment that is never explained.</td></tr>
    <tr><td><b>0</b></td><td>No creditable response.</td><td>No evaluation, or a conclusion with no link to the argument.</td></tr>
  </table></div>

  <h2>3 · How to get each mark: 1, 2, 3 and 4</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Mark</th><th>What is needed</th><th>Typical length</th></tr>
    <tr><td><b>1</b></td><td>One simple evaluative comment, or a very general conclusion</td><td>1 sentence</td></tr>
    <tr><td><b>2</b></td><td>A simple comment plus a general conclusion, or two simple comments: nothing is developed or supported</td><td>2 to 3 sentences, about 30 words</td></tr>
    <tr><td><b>3</b></td><td>One evaluative point that is <b>developed and reasoned</b> (a condition and why it matters), with a conclusion that addresses the question but is thinly justified; or two developed points with a weak conclusion</td><td>4 to 6 sentences, about 60 to 80 words</td></tr>
    <tr><td><b>4</b></td><td><b>At least two developed, supported evaluative points</b> and a <b>conclusion that answers the specific question and says why</b>, using the question's own words</td><td>8 to 10 sentences, about 120 to 150 words</td></tr>
  </table></div>
  <p class="note">The lengths are a guide to what it takes to develop the points, not a mark scheme rule. A long list of unsupported comments stays at Level 1; a short, well-reasoned judgement can reach Level 2.</p>

  <h2>4 · One question, four evaluations</h2>
  <p><b>Question:</b> <i>Assess whether fixing a minimum price is likely to be the best policy to reduce the consumption of a demerit good.</i> (The analysis is assumed to be two-sided, with alternatives, as the AO2 review shows.)</p>
  <div class="card"><h3>1 mark (Level 1, about 15 words)</h3>
  <p>A minimum price may not work if demand for the demerit good is inelastic.</p>
  <p class="note"><b>Why 1:</b> a relevant evaluative comment, but it is a bare statement: no reason why elasticity matters and no judgement.</p></div>
  <div class="card"><h3>2 marks (top of Level 1, about 35 words)</h3>
  <p>A minimum price may not work if demand is inelastic, and there are other policies such as taxes. Overall a minimum price is quite a good policy but it has some problems.</p>
  <p class="note"><b>Why 2:</b> two simple comments and a conclusion, but the conclusion is <b>vague</b> ("quite good", "some problems") and does not say which policy is best or why. Nothing is developed.</p></div>
  <div class="card"><h3>3 marks (Level 2, about 70 words)</h3>
  <p>Whether a minimum price is the best policy depends on how responsive drinkers are to price. If demand for cheap alcohol among dependent drinkers is price inelastic, a 20% price rise may cut quantity by only 5%, so consumption of the demerit good falls very little while their spending rises. A minimum price is therefore not the best policy for these drinkers.</p>
  <p class="note"><b>Why 3:</b> one point is <b>developed and reasoned</b> (condition, figure, consequence) and the conclusion addresses the question. But there is only one evaluative point, and the conclusion does not weigh the policy against the alternatives.</p></div>
  <div class="card"><h3>4 marks (top of Level 2, about 140 words)</h3>
  <p><b>First,</b> the answer depends on elasticity. If demand is inelastic, as with dependent drinkers, a minimum price cuts consumption very little and the extra revenue goes to retailers; if the main buyers are young or low-income drinkers whose demand is more elastic, consumption falls more. <b>Second,</b> it depends on whether the cause of over-consumption is price or information. Where people underestimate the harm, a price rise alone leaves the information failure in place, so education may have a longer-lasting effect even though it works slowly. <b>Third,</b> an indirect tax would apply to all alcohol and give the government revenue, which a minimum price does not.</p>
  <p><b>Therefore</b> a minimum price is unlikely to be the <b>best</b> policy on its own to reduce consumption of a demerit good. It is most effective for cheap, strong drinks where demand is elastic and is best combined with information and a tax, because the policy that works depends on whether over-consumption is driven by price or by lack of information.</p>
  <p class="note"><b>Why 4:</b> at least two developed evaluative points (elasticity, price versus information), each reasoned and supported; the conclusion <b>uses the wording of the question</b> ("best policy", "reduce consumption of a demerit good"), makes a judgement and gives the reason. It does not repeat the analysis; it introduces conditions.</p></div>

  <h2>5 · The 8 mark part and data response: 1 or 2 evaluation marks</h2>
  <div class="tw"><table class="t">
    <tr><th>Question</th><th>What earns the evaluation marks (from the mark scheme)</th><th>Example</th></tr>
    <tr><td>8 marks: "Consider whether a depreciation is likely to increase domestic real output" (2 marks)</td><td>1 mark for a valid explanation that the effect assumes the economy is not at full capacity, or depends on elasticities; the second mark is for a justified conclusion</td><td>"This depends on spare capacity: near full capacity extra demand mainly raises prices, so a depreciation raises output only if there are unused resources. A depreciation is therefore likely to raise output only when the economy is below capacity."</td></tr>
    <tr><td>4 marks: "Consider whether disinflation is more harmful than deflation" (1 mark)</td><td>One mark for a relevant evaluation, such as by how much the inflation rate is falling, how long it will last, or what other countries are experiencing</td><td>"It depends on how far inflation falls: a fall to 1% is mild, but a fall that brings negative inflation is more harmful."</td></tr>
    <tr><td>6 marks: "Assess whether an inflation target is likely to be helpful" (2 marks)</td><td>Relevant evaluation, such as in relation to the particular target, plus 1 mark reserved for a conclusion</td><td>"A 2% target is helpful if people believe the central bank will meet it. If the bank is unwilling to risk a downturn, the target loses credibility, so the benefit depends on the bank's credibility."</td></tr>
  </table></div>

  <h2>6 · The evaluation levers</h2>
  <div class="tw"><table class="t">
    <tr><th>Lever</th><th>Question to ask</th><th>Example</th></tr>
    <tr><td><b>Magnitude</b></td><td>Is the effect big enough to matter?</td><td>"A 2% tax rise will change little if demand is inelastic."</td></tr>
    <tr><td><b>Time</b></td><td>Does the short-run effect differ from the long-run?</td><td>"Training raises AD at once but raises productivity only after several years."</td></tr>
    <tr><td><b>Elasticity</b></td><td>Does the outcome depend on PED, PES, YED or XED?</td><td>"A tariff cuts imports only if demand for imports is elastic."</td></tr>
    <tr><td><b>Spare capacity</b></td><td>Is the economy near full capacity?</td><td>"Extra AD raises output if there is spare capacity but mainly raises prices if not."</td></tr>
    <tr><td><b>Context or type</b></td><td>Does it differ by economy, market or group?</td><td>"Free trade may suit an economy with strong factor endowments more than one with infant industries."</td></tr>
    <tr><td><b>Trade-off and priorities</b></td><td>Does fixing one problem create another? Who gains and loses?</td><td>"Higher interest rates reduce inflation but may raise unemployment."</td></tr>
    <tr><td><b>Alternatives</b></td><td>Is there a better policy for the same aim?</td><td>"Information tackles the cause; a tax raises revenue."</td></tr>
    <tr><td><b>Assumptions and data limits</b></td><td>What does the model or data assume or leave out?</td><td>"The circular flow model ignores the size and timing of the effects."</td></tr>
  </table></div>

  <h2>7 · The CIT method: Condition, If, Then</h2>
  <ul>
    <li><b>Condition:</b> name the factor the judgement depends on (a lever above), using the good or the economy in the question.</li>
    <li><b>If:</b> say what happens if that condition holds, and what happens if it does not.</li>
    <li><b>Then:</b> give the outcome for the claim in the question, with the reason.</li>
    <li>Repeat for a second condition, then write one sentence that weighs one against the other and answers the question.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Vague (Level 1)</th><th>Developed (Level 2)</th></tr>
    <tr><td>"It depends on many factors."</td><td>"It depends on the price elasticity of demand for cigarettes among long-term smokers. If it is inelastic, a 20% tax raises revenue but barely reduces consumption, because addicted smokers keep buying; if it is elastic, consumption falls by more than the price rises."</td></tr>
    <tr><td>"There are advantages and disadvantages."</td><td>"The advantage of the tax is revenue and the disadvantage is that it is regressive: poorer smokers pay a larger share of their income, so the policy reduces the externality at a cost to the poorest. The cost matters more if the tax is large."</td></tr>
    <tr><td>"Overall it is quite effective."</td><td>"Overall a minimum price is not the best policy for dependent drinkers, because demand is inelastic, but it can work for cheap drinks where substitutes exist."</td></tr>
  </table></div>

  <h2>8 · Writing the judgement</h2>
  <ul>
    <li><b>Answer the question that was asked.</b> If it says "best", say which is best. If it says "always", say when it is not. If it says "to what extent", give an extent ("to a limited extent, because...").</li>
    <li><b>Use the question's wording</b> in the conclusion so that the examiner can see it addresses the specific requirements.</li>
    <li><b>Give the reason and the condition:</b> "...because...; this would change if...".</li>
    <li><b>No new analysis</b> and no summary of what you have already said.</li>
    <li><b>Keep the scope word</b> in mind: "all", "always", "only" ask you to find a case where the claim fails.</li>
  </ul>

  <h2>9 · Common ways to lose evaluation marks</h2>
  <ul>
    <li><b>One-sided analysis</b>, so no evaluation marks are available at all.</li>
    <li><b>"It depends"</b> with no named factor, mechanism or judgement.</li>
    <li><b>Repeating the analysis</b> under the heading "evaluation".</li>
    <li><b>Evaluating a different question</b>: for example discussing whether a policy works when the question asks whether it is the best.</li>
    <li><b>Two lists</b> (for and against) never weighed against each other.</li>
    <li><b>A conclusion that does not conclude</b>: "overall there are pros and cons".</li>
    <li><b>Generic conditions</b> ("the economy", "consumers") instead of the named good, group or country.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Save the last 5 or 6 minutes of a 12 mark answer for evaluation. Use <b>two conditions</b> and a <b>conclusion in the question's words</b>. Check each evaluative sentence: does it introduce a condition that has not been mentioned before? If not, it is probably summary.</div>
'''

watch = '''
  <h2>1 · Building evaluation from 1 mark to 4 marks</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · The CIT method on one point</h2>
  <div id="stB"></div>
  <h2>3 · From a vague conclusion to a justified one</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · How many evaluation marks?</h2>
  <p>Describe the evaluation in a 12 mark answer. The lab applies Table B and the rule that one-sided analysis earns no evaluation marks. It is a teaching model, not an official mark.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Estimated AO3 mark (out of 4)</small><strong id="r1"></strong></div><div><small>Level</small><strong id="r2"></strong></div><div><small>To gain another mark</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 200" role="img" aria-label="A bar showing the estimated evaluation mark out of four"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Build a CIT point", "Choose a lever to see the vague version, the developed version and the question it fits.", ["Vague (Level 1)", "Developed (Level 2)", "Question it fits"]) + chooser_html("k", "Lab 3 · Improve the conclusion", "Choose a weak conclusion to see why it earns little and a better version.", ["Why it scores low", "A better version", "What the better version adds"])

practise = '''
  <h2>1 · Not evaluation, vague, or developed?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which lever is it?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the CIT sentence in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the mark to the feature</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The conclusion carries a mark", "Mark schemes for 12 mark questions say 'reserve 1 mark for a conclusion' and ask for a judgement that addresses the specific question, such as 'which policy is best' or 'whether a rise or a fall benefits the economy'.", "writing a conclusion in the question's words.") +
rw("One-sided means no evaluation marks", "A question on whether free trade is always positive had the note 'a one-sided response cannot gain any marks for evaluation'. The same note appears for a surplus on the current account and for tools of protection.", "both sides before evaluating.") +
rw("Conditions the mark scheme looks for", "Examples of evaluation points in mark schemes: spare capacity, the elasticity of demand, the time period, the size of the change, whether other countries are doing the same, and how open the economy is.", "choosing levers that examiners expect.") +
rw("Context-based evaluation", "A question about a developing economy carried the note that if the analysis is not in the context of a developing economy, Level 2 is the maximum. Name the type of economy in your conditions and your conclusion.", "naming the economy in the condition.") +
rw("Short evaluation in data response", "In a 6 mark part examiners award up to 2 marks for evaluative comment, for example that a policy might make the problem worse, or for a conclusion on the extent. A single sentence with a reason can earn a mark.", "being brief but specific.")
)

mc_exam = [
  mcq("w21_12", 29, "What would make a policy of raising interest rates less likely to be effective in reducing inflation?", ["Aggregate supply is increasing faster than aggregate demand", "Consumers expect prices to rise even faster in the future", "Consumers' spending is largely paid for on credit", "Interest rates are still higher abroad"], 1, "A condition that limits the policy: if consumers expect faster price rises, they bring forward spending."),
  mcq("m25_12", 24, "A government decides to use supply-side policy to increase long-run aggregate supply (LRAS). What is the most likely reason why this policy tool will not lead to a fall in the price level?", ["Aggregate demand will also increase.", "Labour productivity levels will increase.", "Workers will save any extra wages they earn.", "Workers will spend any extra wages on imports."], 0, "An evaluation point: supply-side spending also raises AD, offsetting the fall in prices."),
  mcq("s25_13", 25, "A government has a target to reduce the rate of inflation. Why might it not want to raise interest rates to achieve this target?", ["aggregate demand may fall", "aggregate supply may fall", "saving may fall", "the exchange rate may fall"], 1, "A cost of the policy: higher borrowing costs for firms can reduce capacity."),
  mcq("m24_12", 25, "A government decides to allow the country's currency to depreciate to remove the deficit on its current account. What is the most likely reason why this would not work?", ["The country gains a competitive advantage from the depreciation.", "The country has a surplus on its capital and financial accounts.", "The price elasticities of demand for the country's exports and imports are greater than one.", "There are high trade barriers with the country's main trading partners."], 3, "A limiting condition: trade barriers reduce the rise in exports."),
  mcq("s21_13", 25, "A country has a balance of trade deficit. When will this be least likely to be improved as a result of a depreciation of its currency?", ["if it is currently operating with a significant amount of unused resources", "if the sum of the price elasticities of demand for exports and imports is less than 1", "if in the long term, the price elasticity of demand for exports should increase", "if the country uses a relatively small proportion of imports in their production process"], 1, "The elasticity condition: if the sum is below one the trade balance may worsen.")
]

exam = exam_page("evaluation: how each mark is reached",
  "We chose past questions where the mark scheme spells out the evaluation: 12 mark questions with Table B and one-sided caps, an 8 mark part, and data response parts of 4 and 6 marks. Compare your own conclusion with the evaluation point in each key (marked E).",
  exam_rows([("m24_22","4(a)",8),("s24_22","3(b)",12),("w24_22","5(b)",12),("s25_23","4(b)",12),("m24_22","5(b)",12),("s25_21","1(c)",4),("s25_21","1(e)",6)], ["w21_12","m25_12","s25_13","m24_12","s21_13"]),
  [
  grab("m24_22", "4(a)"),
  grab("s24_22", "3(b)"),
  grab("w24_22", "5(b)"),
  grab("s25_23", "4(b)"),
  grab("m24_22", "5(b)"),
  grab("s25_21", "1(c)"),
  grab("s25_21", "1(e)")
  ],
  )

tips = tips_html(
  [("Do both sides first.", "One-sided analysis earns no evaluation marks."),
   ("Name the condition.", "Elasticity, time, spare capacity, size, context."),
   ("Use Condition, If, Then.", "Reason and consequence, not a bare 'it depends'."),
   ("Two developed points beat four thin ones.", "Level 2 needs development."),
   ("Conclude in the question's words.", "Best, always, to what extent."),
   ("Give the reason for the judgement.", "And say what would change it."),
   ("No new analysis in the conclusion.", "Introduce conditions, not summary.")],
  [("Evaluation", "Evaluation weighs the arguments and reaches a justified judgement."),
   ("Judgement", "A judgement is a reasoned answer to the specific question asked."),
   ("Condition", "A condition is a factor on which the outcome depends."),
   ("Justified", "A justified conclusion gives the reason and the condition."),
   ("Level 2 evaluation", "Level 2 evaluation is developed, reasoned and well supported.")],
  [CW["assess"], CW["discuss"], CW["consider"], CW["evaluate"] if "evaluate" in CW else CW["assess"]]) + FC

js = CHAINJS + '''
$("#pic1").innerHTML = (() => {
  const L = [["1 mark", "One simple comment", 15, "f3"], ["2 marks", "Comments + vague conclusion", 205, "f3"], ["3 marks", "One developed point + conclusion", 395, "f1"], ["4 marks", "Two developed points + justified conclusion", 585, "f2"]];
  let o = ""; L.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 165, 80, c, { rx: 12, ...op(0.45) }) + SV.text(x + 82, 40, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }); const w = d.split(" + "); w.forEach((p, i) => { o += SV.text(x + 82, 62 + i * 18, (i ? "+ " : "") + p, "sm", { "text-anchor": "middle" }); }); });
  return `<svg viewBox="0 0 760 104" role="img" aria-label="Evaluation marks from one to four">${o}</svg>`;
})();
chainStep("#stA", "Building evaluation from 1 mark to 4 marks", ["1 mark: 'A minimum price may not work if demand is inelastic.'", "2 marks: add a second simple comment and a general conclusion ('overall quite good')", "3 marks: develop one point: if demand is inelastic, a 20% price rise cuts quantity by only 5%, so consumption barely falls", "4 marks: add a second condition (information failure remains) and a justified conclusion in the question's words"], [
  "<b>One bare comment.</b>", "<b>Still Level 1:</b> nothing is supported and the conclusion is vague.", "<b>Level 2:</b> a condition, a reason and a consequence.", "<b>Top of Level 2:</b> two developed points and a conclusion that says which policy is best and why."]);
chainStep("#stB", "The CIT method on one point", ["Condition: it depends on the price elasticity of demand among heavy drinkers", "If demand is inelastic: a 20% price rise cuts quantity by only 5%, so consumption barely falls", "If demand is elastic: consumption falls by more than the price rise", "Then: a minimum price is only effective where demand is elastic", "Weigh it: heavy drinkers are the target group and tend to be inelastic, so the policy is limited"], [
  "<b>Condition</b> names the lever (elasticity) and the group.", "<b>If</b> shows the mechanism for one case.", "<b>The opposite case</b> shows you have considered both.", "<b>Then</b> connects the result to the claim in the question.", "<b>Weigh</b> which condition is more likely, with the reason."]);
chainStep("#stC", "From a vague conclusion to a justified one", ["Vague: 'Overall a minimum price is quite good but has problems.'", "Say which: 'A minimum price is not the best policy on its own.'", "Use the question's words: '...to reduce consumption of a demerit good.'", "Add the reason: 'because demand is likely to be inelastic and information failure remains.'", "Add the condition: 'It would work better for cheap drinks where substitutes exist, or with information.'"], [
  "<b>Level 1:</b> no judgement.", "<b>A judgement</b> that answers 'best'.", "<b>Addresses the specific requirements</b> of the question.", "<b>Justified:</b> a reason that links to the analysis.", "<b>Developed:</b> the condition under which the answer would change."]);

function ev() {
  const ids = ["pt", "sp", "cn", "sd"];
  if (!ids.every((i) => $("#" + i))) return;
  const [pts, sup, con, both] = ids.map((i) => +$("#" + i).value);
  let m, why = "";
  if (!both) { m = 0; why = " The analysis is one-sided, so no evaluation marks are available."; }
  else {
    const dev = Math.min(pts, 2) * (sup >= 1 ? 1 : 0.5) * (sup >= 2 ? 1.2 : 1), cc = con === 2 ? 1.5 : con === 1 ? 0.7 : 0;
    m = Math.round(Math.min(4, dev * 1.1 + cc));
    if (con < 2) m = Math.min(m, 3);
    if (pts === 0 && con === 0) m = 0;
    if (sup === 0) m = Math.min(m, 2);
  }
  const L = m >= 3 ? 2 : m >= 1 ? 1 : 0;
  $("#r1").textContent = m + " / 4"; $("#r2").textContent = L ? "Level " + L : "No credit";
  $("#r3").textContent = !both ? "Analyse the other side first" : m >= 4 ? "At the top" : con < 2 ? "Make the conclusion answer the question and give the reason" : sup < 2 ? "Support each point with a reason or figure" : pts < 2 ? "Add a second developed condition" : "Check the conclusion uses the question's words";
  $("#rv").textContent = `${pts} evaluative point(s), support ${["none", "some", "strong"][sup]}, conclusion ${["absent", "vague", "justified and answers the question"][con]}, ${both ? "analysis two-sided" : "analysis one-sided"}: about ${m} out of 4 (${L ? "Level " + L : "no credit"}).` + why;
  const W = 340, X = (v) => 40 + (v / 4) * W;
  let o = SV.rect(X(0), 70, X(2) - X(0), 40, "f3", op(0.4)) + SV.rect(X(2), 70, X(4) - X(2), 40, "f2", op(0.4)) + SV.text(X(1), 95, "Level 1", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(3), 95, "Level 2", "lbl bd", { "text-anchor": "middle" });
  o += SV.line(X(m), 50, X(m), 130, "c4", { "stroke-width": 3 }) + SV.text(X(m), 44, m + "", "lbl bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pt", label: "Evaluative points made (0 to 3) ", min: 0, max: 3, step: 1, value: 1, fmt: (v) => v, onInput: ev });
Lib.slider($("#g2"), { id: "sp", label: "Support: 0 none, 1 some, 2 reasoned with evidence ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["none", "some", "strong"][v], onInput: ev });
Lib.slider($("#g3"), { id: "cn", label: "Conclusion: 0 none, 1 vague, 2 justified ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["none", "vague", "justified"][v], onInput: ev });
Lib.slider($("#g4"), { id: "sd", label: "Both sides analysed? (0 no, 1 yes) ", min: 0, max: 1, step: 1, value: 1, fmt: (v) => (v ? "yes" : "no"), onInput: ev });
ev();

chooser("h", [
  ["Elasticity", "It depends on how people respond to price.", "It depends on the price elasticity of demand for cigarettes among long-term smokers: if it is inelastic, a 20% tax raises revenue but barely cuts consumption.", "Is an indirect tax the best way to reduce consumption of a demerit good?", 5],
  ["Time", "In the long run it might be different.", "In the short run, spending on roads raises AD and may raise prices; in the long run, better roads raise capacity and lower prices.", "Will supply-side policy raise inflation?", 5],
  ["Spare capacity", "It depends on the state of the economy.", "If the economy has spare capacity, extra AD raises output; near full capacity it mainly raises the price level, so the policy is less beneficial.", "Does expansionary fiscal policy always benefit an economy?", 5],
  ["Context or type", "It is different in different countries.", "For a developing economy with infant industries, free trade may cause unemployment; for one with strong factor endowments, it is more likely to bring gains.", "Is free trade always better than protectionism?", 4],
  ["Trade-off", "There are good and bad points.", "Higher interest rates reduce demand-pull inflation, but they also raise firms' costs and unemployment, so the benefit depends on how much slack there is.", "Is contractionary monetary policy the best way to reduce inflation?", 4],
  ["Alternatives", "Other policies exist.", "Information tackles the cause of over-consumption, but is slow; a tax is quicker and raises revenue, so a combination is likely to work best.", "Is information the best way to reduce demerit goods?", 4]
], (it) => `${it[0]}. Vague: "${it[1]}" Developed: "${it[2]}" Fits: ${it[3]}`, "How often this lever is useful");
chooser("k", [
  ["'Overall it has advantages and disadvantages.'", "It restates both sides but makes no judgement", "'Overall the policy is likely to work for goods with elastic demand, but not for addictive goods, so it is not the best policy on its own.'", "A judgement, a condition and a reason", 1],
  ["'It depends.'", "No factor, mechanism or answer", "'It depends on whether demand is inelastic: if it is, the tax barely reduces consumption, so it is not the best policy.'", "A named condition and a result", 1],
  ["'So the government should use this policy.'", "A claim with no reason and no weighing", "'The government should combine it with information, because price alone leaves the lack of knowledge in place.'", "A reason that links to the analysis", 2],
  ["'In conclusion, as I said above, a minimum price raises the price.'", "Repeats the analysis", "'In conclusion, a minimum price is unlikely to be the best policy, because demand is likely to be inelastic and an alternative gives more revenue.'", "A judgement using the question's words", 2],
  ["'Overall it is a good policy.'", "A vague judgement with no support", "'Overall it is a good policy for cheap, strong drinks with substitutes, because quantity demanded falls most there.'", "The condition and the group", 2]
], (it) => `Weak: ${it[0]} Why it scores low: ${it[1].toLowerCase()}. Better: ${it[2]} It adds: ${it[3].toLowerCase()}.`, "Marks lost by the weak version (out of 4)");
''' + CLASSIFY("cl1", "Not evaluation, vague evaluation or developed evaluation?", ["Not evaluation", "Vague (Level 1)", "Developed (Level 2)"],
  [("A minimum price is set above the equilibrium price.", 0), ("It depends on many things.", 1), ("If demand is price inelastic, a 20% rise in price cuts quantity by only 5%, so consumption barely falls and the policy is not effective.", 2), ("A tax shifts the supply curve left.", 0), ("Overall there are good and bad points.", 1), ("A tariff only helps if demand for imports is elastic; if trading partners retaliate, exporters lose, so the benefit depends on retaliation.", 2)],
  "Analysis and facts are not evaluation. Vague comments name no factor. Developed evaluation gives the condition, the reason and the consequence.") + CLASSIFY("cl2", "Which evaluation lever is it?", ["Time", "Elasticity", "Spare capacity", "Trade-off"],
  [("Training raises productivity only after several years.", 0), ("A tax only cuts consumption if demand is elastic.", 1), ("Extra AD mainly raises prices if the economy is near full capacity.", 2), ("Higher interest rates cut inflation but may raise unemployment.", 3), ("The short-run effect is bigger than the long-run effect.", 0), ("Imports fall only if the sum of the price elasticities is above one.", 1)],
  "Time, elasticity, spare capacity and trade-off are four common levers.") + ORDER(
  "Put the sentence parts in order: Condition, If, Then.",
  ["It depends on the price elasticity of demand for cigarettes among long-term smokers", "If it is inelastic, a 20% tax raises revenue but barely reduces consumption", "Then the tax is not effective at reducing consumption of this demerit good", "So overall the tax is better at raising revenue than at cutting smoking"],
  "Condition, If, Then, and a weighing sentence.") + MATCH([
  ["1 mark", "A simple evaluative comment"],
  ["2 marks", "Simple comments with a vague conclusion"],
  ["3 marks", "One developed point with a conclusion that addresses the question"],
  ["4 marks", "Two developed points with a justified conclusion"],
  ["No evaluation marks", "The analysis was one-sided"],
  ["Justified conclusion", "A judgement with the reason and the condition"]]) + CALC([
  {"q": "A 12 mark question gives 4 marks for evaluation. What percentage of the marks is that?", "a": 33.3, "unit": "%", "tol": 0.3, "hint": "4 ÷ 12.", "sol": "<b>33.3%</b>."},
  {"q": "An 8 mark part gives 2 marks for evaluation. What percentage is that?", "a": 25, "unit": "%", "tol": 0.1, "hint": "2 ÷ 8.", "sol": "<b>25%</b>."},
  {"q": "A 6 mark data response part has 2 marks for evaluation. What percentage is that (1 decimal place)?", "a": 33.3, "unit": "%", "tol": 0.3, "hint": "2 ÷ 6.", "sol": "<b>33.3%</b>."},
  {"q": "At 2 minutes a mark, how long should the evaluation of a 12 mark answer take (4 marks)?", "a": 8, "unit": "min", "tol": 0.1, "hint": "4 × 2.", "sol": "<b>8 minutes</b>, including planning."}]) + MCQ([
  ("A response says 'it depends on many factors' and nothing else. Which Table B level is the best fit?", ["Level 1", "Level 2", "Level 0 only", "Level 3"], 0, "A vague comment with no development is Level 1."),
  ("Which feature is required for Level 2 evaluation?", ["A justified conclusion addressing the question and developed, supported comments", "A long introduction", "A repeat of the analysis", "A list of definitions"], 0, "These are the two Table B descriptors."),
  ("A mark scheme says a one-sided response cannot gain evaluation marks. What should the student do?", ["Analyse both sides before evaluating", "Write a longer conclusion", "Only evaluate", "Skip the analysis"], 0, "Evaluation requires a balanced analysis."),
  ("Which conclusion is best for 'assess whether X is the best policy'?", ["It says which policy is best, uses the question's words and gives a reason", "It lists pros and cons", "It repeats the analysis", "It introduces a new point"], 0, "That is a justified conclusion that addresses the question."),
  ("Which is a developed evaluative comment?", ["Demand may be inelastic.", "If demand is inelastic, the tax cuts consumption little, so the policy fails its aim.", "There are other policies.", "Elasticity is important."], 1, "Condition, if and then.")
], "qz1") + CARDS([
  ("Table B", "Level 1: vague. Level 2: justified and developed."),
  ("4 marks", "Two developed points + justified conclusion."),
  ("Levers", "Magnitude, time, elasticity, capacity, context, trade-off."),
  ("CIT", "Condition, If, Then."),
  ("One-sided", "No evaluation marks."),
  ("Conclusion", "Use the question's words and give the reason."),
  ("8 mark part", "2 evaluation marks."),
  ("Avoid", "'It depends' alone.")]) + MCQ(mc_exam)

build("ex3", "as-ao3-evaluation", "AO3 Evaluation: How Each Mark and Level Is Reached", EY,
  "Exactly what earns 1, 2, 3 and 4 evaluation marks: Table B explained, the levers and the Condition, If, Then method, with examples at every mark for 12 mark, 8 mark and data response questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
