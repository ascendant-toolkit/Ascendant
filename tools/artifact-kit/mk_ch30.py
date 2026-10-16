"""Builds the three ch30 part pages (ut1..ut3) from slices of ut.* plus new content. Run: python3 tools/artifact-kit/mk_ch30.py"""
from splitter import Src, page, write, key
S = Src("ut")
HEAD = S.j_((1, 18))
EY = "A Level Economics · 9708 · Syllabus 7.1 · Part {} of 3"
NOTE = '<p class="note">Examples are explained in general terms. The numbers are simple on purpose, to show the idea.</p>\n'
def MCQ(*n): return 'Lib.quiz($("#qz2"), { qs: [\n' + S.j_(*[(i, i) for i in n]) + '] });\n'
def QZ(*n, extra=""): return 'Lib.quiz($("#qz1"), { qs: [\n' + S.j_(*[(i, i) for i in n]) + extra + '] });\n'
def CARDS(*n, extra=""): return 'Lib.cards($("#fc1"), { cards: [\n' + S.j_(*[(i, i) for i in n]) + extra + '] });\n'
def CALC(*n, extra=""): return 'Lib.calc($("#c1"), { qs: [\n' + S.j_(*[(i, i) for i in n]) + extra + '] });\n'
def TIPS(lis, rows): return '<h2>Top tips</h2>\n  <ul class="tips">\n' + S.b(*lis) + '  </ul>\n  <h2>Sentences you can use</h2>\n  <div class="tw"><table class="t">\n    <tr><th>You want to say</th><th>Use this sentence</th></tr>\n' + S.b(*rows) + '  </table></div>\n'
def CMD(*r): return '<h2>Command words</h2>\n  <div class="tw"><table class="t">\n    <tr><th>Command word</th><th>What it asks for</th></tr>\n' + "".join(f"    <tr><td>{a}</td><td>{b}</td></tr>\n" for a, b in r) + '  </table></div>\n'
EXP = ("Explain", "Give reasons, with a clear chain of cause and effect.")
EVA = ("Evaluate", "Weigh up the strength of the arguments and reach a supported conclusion.")
KEYL = '<div class="key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>\n'
FC = '<h2>Flashcards</h2><div id="fc1"></div>\n'

# ------------------------------------------------------------------ 30.1
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Utility</b> is the satisfaction a consumer gets from consuming a good. <b>Total utility</b> (TU) is all of it and <b>marginal utility</b> (MU) is the extra from one more unit. The <b>law of diminishing marginal utility</b> says MU falls as consumption rises: TU rises at a decreasing rate, peaks where MU = 0, then falls once MU is negative. It explains why people will pay less for the next unit than for the last, the first step towards a downward-sloping demand curve.</p></div>
''' + S.b((25, 42), (44, 45)) + '''
  <h2>3 · Reading the two curves</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Total utility curve</th><th>Marginal utility curve</th></tr>
    <tr><td><b>Shape</b></td><td>Rises, flattens at a peak, then falls</td><td>Slopes down from the first unit and crosses zero</td></tr>
    <tr><td><b>Link</b></td><td>The slope of TU at a point is MU</td><td>The area under MU up to a quantity is TU</td></tr>
    <tr><td><b>Peak or zero</b></td><td>Maximum at the 6th slice</td><td>MU = 0 at the 6th slice</td></tr>
  </table></div>
  <div class="tip"><b class="h">The paradox of value</b>Water has a huge total utility but is cheap, because it is plentiful and the MU of one more unit is low. Diamonds have much lower total utility but are dear, because the MU of one more is high. Price follows marginal, not total, utility.</div>
'''
watch = S.b((76, 78))
explore = S.b((91, 96))
practise = '''
  <h2>1 · What does the sign of MU tell you?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = NOTE + S.b((144, 145)) + '''  <div class="rw"><h3>Your fourth cup of coffee</h3><p>The first cup in the morning is valuable. By the fourth, it adds little, and a fifth could leave you jittery. The same drink gives less and less extra satisfaction.</p><div class="use"><b>Exam use:</b> a quick example of diminishing marginal utility. Say what happens to MU and what happens to TU.</div></div>
'''
exam = '''
  <h2>Past paper questions on total and marginal utility</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). The ideas in this part are tested mostly in Paper 3 multiple choice, which are shown below, and as the opening paragraph of the longer questions in parts 2 and 3. A practice question with a model answer is included. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>5 shown below</td><td>2021 to 2024</td></tr>
    <tr><td>Longer questions</td><td>Opening definitions in the 12 mark questions</td><td>See parts 2 and 3</td></tr>
  </table></div>
  <h2>A · Practice question with a model answer</h2>
  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">8 marks</span> Explain the law of diminishing marginal utility, using an example.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>Define utility, TU and MU. State the law. Use a numerical or everyday example. Say what happens to TU as MU falls, including the zero and negative stages.</div>
''' + KEYL + '''
    <div class="ans">
    <p><span class="mk k" data-t="K">Utility is the satisfaction a consumer gets from consuming a good. Total utility is the total satisfaction from a quantity, and marginal utility is the additional satisfaction from consuming one more unit. The law of diminishing marginal utility states that as a consumer consumes more of a good, the marginal utility from each additional unit falls.</span></p>
    <p><span class="mk a" data-t="A">For example, a hungry person eating slices of pizza may gain 20 utils from the first slice, 16 from the second and 12 from the third, so MU is falling.</span> <span class="mk n" data-t="N">Total utility is still rising, to 20, 36 and 48, but at a decreasing rate, because each slice adds less than the last. If the person eats until the sixth slice adds nothing, MU is zero and total utility is at its maximum. A seventh slice could make them feel ill, so MU is negative and total utility falls.</span> <span class="mk e" data-t="E">This depends on the units being similar and consumed in a short period, because a rest between slices could restore the satisfaction.</span></p></div>
  </div></details>
  <h2>B · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips = TIPS([(244, 245)], [(257, 257)]) + CMD(EXP, EVA) + FC
js = HEAD + S.j_((19, 49), (97, 115), (167, 176)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Utility", "The satisfaction a consumer gets from consuming a good"],
  ["Total utility", "All the satisfaction from a given quantity"],
  ["Marginal utility", "The extra satisfaction from one more unit"],
  ["Diminishing marginal utility", "Each extra unit adds less satisfaction than the one before"],
  ["Util", "An imaginary unit used to measure utility"],
  ["Paradox of value", "Water is cheap and diamonds dear because price follows marginal, not total, utility"],
], done: "Six words for the building blocks." });
''' + CALC(204, 205, 206, extra='''  { q: "The marginal utilities of the 1st, 2nd and 3rd slices are 20, 16 and 12. What is the total utility of 3 slices?", a: 48, sol: "20 + 16 + 12 = <b>48</b>." },
  { q: "Total utility is 60 at 5 slices and 60 at 6 slices. What is the marginal utility of the 6th slice?", a: 0, sol: "60 − 60 = <b>0</b>: total utility is at its maximum." },
''') + QZ(213, 214, extra='''  { q: "Marginal utility is negative. Total utility is:", opts: ["rising", "falling", "at its maximum", "zero"], a: 1, why: "A negative MU means the extra unit reduces total satisfaction." },
  { q: "Water is cheap but diamonds are dear because:", opts: ["water has no utility", "price depends on marginal utility, which is low for plentiful water", "diamonds have higher total utility", "demand for water is zero"], a: 1, why: "The MU of one more unit of a plentiful good is low." },
''') + CARDS(221, 222, 223, 224, 225, 226, 227, 233) + MCQ(240, 242, 247, 249, 250)
write("ut1", page(EY.format(1), "Total and Marginal Utility",
  "How economists measure satisfaction: total and marginal utility, the three stages of the TU and MU curves and the law of diminishing marginal utility. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Total and Marginal Utility", "total-and-marginal-utility")

# ------------------------------------------------------------------ 30.2
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A consumer has a limited income, so more of one good means less of another. To get the most total utility from a budget, a <b>rational consumer</b> compares the <b>marginal utility per dollar</b> of each good and switches spending towards the good with the higher ratio. At the optimum <b>MUx ÷ Px = MUy ÷ Py</b>, so no switch can raise total utility: this is <b>consumer equilibrium</b>, or the <b>equi-marginal principle</b>. The rule uses prices, so equal MU or equal total utility is not enough.</p></div>
''' + S.b((47, 55)).replace("3 · Consumer", "1 · Consumer") + '''
  <h2>2 · The worked example in a table</h2>
  <p>Income $24, Px = $4 and Py = $2. The consumer buys each unit in turn, always choosing the one with the highest marginal utility per dollar.</p>
  <div class="tw"><table class="t">
    <tr><th>Unit</th><th>MUx</th><th>MUx ÷ $4</th><th>MUy</th><th>MUy ÷ $2</th></tr>
    <tr><td>1st</td><td>24</td><td>6</td><td>15</td><td>7.5</td></tr>
    <tr><td>2nd</td><td>20</td><td>5</td><td>12</td><td>6</td></tr>
    <tr><td>3rd</td><td>16</td><td>4</td><td>9</td><td>4.5</td></tr>
    <tr><td>4th</td><td>12</td><td><b>3</b></td><td>6</td><td><b>3</b></td></tr>
    <tr><td>5th</td><td>8</td><td>2</td><td>3</td><td>1.5</td></tr>
  </table></div>
  <p>Taking the highest ratios first, the $24 buys four units of X ($16) and four of Y ($8), where both ratios are 3. Total utility is 72 + 42 = <b>114</b>. Any other way of spending the $24 gives less.</p>
  <h2>3 · How to write it in an answer</h2>
  <ul>
    <li>State the aim: a rational consumer maximises total utility from a limited income.</li>
    <li>Use <b>two goods</b> and write the condition MUx/Px = MUy/Py.</li>
    <li>Show what happens when the ratios differ: switch spending towards the higher ratio until MU falls and the ratios are equal.</li>
    <li>Add a numerical example with a budget.</li>
  </ul>
'''
watch = S.b((80, 82))
explore = S.b((98, 103)) + '''
  <h2>Lab 2 · Which good next?</h2>
  <p>Choose how many units of X ($4) and Y ($2) have been bought already, and see which good the next dollar should go to. The rule: buy the good with the higher MU per dollar.</p>
  <div class="card"><div class="grid2"><div><div id="g6"></div><div id="g7"></div>
    <div class="readout"><div><small>Next X: MU per $</small><strong id="n1"></strong></div><div><small>Next Y: MU per $</small><strong id="n2"></strong></div><div><small>Buy next</small><strong id="n3"></strong></div></div>
    <div class="verdict" id="nv"></div></div>
    <div><svg id="labN" viewBox="0 0 420 240" role="img" aria-label="Bars comparing the marginal utility per dollar of the next unit of X and Y"></svg></div></div></div>
'''
practise = '''
  <h2>1 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>2 · Put the equilibrium argument in order</h2><div id="o1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = NOTE + S.b((146, 147)) + '''  <div class="rw"><h3>Choosing a meal deal</h3><p>If a sandwich costs twice as much as a drink, it should give about twice as much extra satisfaction to be worth buying. If it gives less, a shopper may swap to the cheaper item.</p><div class="use"><b>Exam use:</b> the idea that it is utility per dollar, not utility alone, that guides spending.</div></div>
'''
exam = '''
  <h2>Past paper questions on consumer equilibrium</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the 12 mark questions on the equilibrium of a consumer and the equi-marginal rule, and Paper 3 multiple choice questions. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 12 marks (Paper 4)</td><td>3</td><td>Feb/March 2020 (42); May/June 2021 (41, 43); Oct/Nov 2021 (43)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>4 shown below</td><td>2020 to 2025</td></tr>
  </table></div>
  <h2>A · 12 mark questions</h2>
''' + KEYL + S.b((201, 204), (225, 228), (230, 233)) + '''
  <h2>B · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips = TIPS([(246, 247)], [(258, 258)]) + CMD(EXP, ("Examine", "Look closely at the analysis and how the parts connect.")) + FC
js = HEAD + S.j_((50, 72), (116, 135)) + '''
/* ---------- Lab 2: which good next ---------- */
function labNext() {
  if (!$("#ax") || !$("#ay")) return;
  const x = +$("#ax").value, y = +$("#ay").value, mx = x < 6 ? MUX[x] / 4 : 0, my = y < 6 ? MUY[y] / PY : 0;
  $("#n1").textContent = x < 6 ? Lib.fmtN(mx, 2) : "none left"; $("#n2").textContent = y < 6 ? Lib.fmtN(my, 2) : "none left"; $("#n3").textContent = mx === my ? "Either" : mx > my ? "X" : "Y";
  $("#nv").textContent = mx === my ? "The ratios are equal. A switch would not raise total utility: this is equilibrium (if the budget is spent)."
    : `The next unit of ${mx > my ? "X gives " + Lib.fmtN(mx, 2) + " utils per dollar and Y only " + Lib.fmtN(my, 2) : "Y gives " + Lib.fmtN(my, 2) + " utils per dollar and X only " + Lib.fmtN(mx, 2)}, so spending on ${mx > my ? "X" : "Y"} next raises total utility more.`;
  let o = SV.line(30, 190, 400, 190);
  [[90, mx, "f1", "Next X"], [250, my, "f4", "Next Y"]].forEach(([bx, v, c, l]) => { o += SV.rect(bx, 190 - 12 * v, 90, 12 * v, c) + SV.text(bx + 45, 190 - 12 * v - 8, Lib.fmtN(v, 2), "lbl bd", { "text-anchor": "middle" }) + SV.text(bx + 45, 212, l + " (MU per $)", "sm", { "text-anchor": "middle" }); });
  $("#labN").innerHTML = o;
}
Lib.slider($("#g6"), { id: "ax", label: "Units of X bought so far ($4 each): ", min: 0, max: 6, step: 1, value: 2, fmt: (v) => v, onInput: labNext });
Lib.slider($("#g7"), { id: "ay", label: "Units of Y bought so far ($2 each): ", min: 0, max: 6, step: 1, value: 2, fmt: (v) => v, onInput: labNext });

Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Rational consumer", "A consumer who aims to maximise utility"],
  ["Budget constraint", "The limit on spending set by income and prices"],
  ["Marginal utility per dollar", "MU divided by the price of the good"],
  ["Equi-marginal principle", "Utility is maximised when MU ÷ price is equal across goods"],
  ["Consumer equilibrium", "The bundle that gives the most total utility from a budget"],
  ["Marginal utility of money", "The extra utility from one more dollar, assumed constant"],
], done: "Six words for equilibrium." });
Lib.order($("#o1"), { prompt: "Put the explanation of consumer equilibrium in order.", items: [
  "The consumer has a limited income and faces prices for two goods",
  "The consumer aims to maximise total utility",
  "Compare the marginal utility per dollar of each good: MUx ÷ Px and MUy ÷ Py",
  "If one ratio is higher, switch spending towards that good",
  "As more of it is bought its MU falls, and as less of the other is bought its MU rises",
  "At equilibrium MUx ÷ Px = MUy ÷ Py and total utility is at its maximum",
], done: "Always use two goods and the prices." });
''' + CALC(207, 208, 210, extra='''  { q: "A consumer has bought 2 units of X (Px = $4) and 2 of Y (Py = $2). The next X gives 16 utils and the next Y gives 9. Which gives more utility per dollar? (type X or Y)", t: ["Y"], ph: "X or Y", sol: "X: 16 ÷ 4 = 4. Y: 9 ÷ 2 = 4.5. The next dollar should go to <b>Y</b>." },
  { q: "At the $24 budget optimum the consumer buys 4 units of X (total 72 utils) and 4 of Y (total 42 utils). What is the total utility?", a: 114, sol: "72 + 42 = <b>114</b>." },
  { q: "Check the budget: 4 units of X at $4 and 4 units of Y at $2. How much is spent ($)?", a: 24, sol: "16 + 8 = <b>$24</b>: the whole income is spent." },
''') + QZ(215, extra='''  { q: "The equi-marginal principle says total utility is greatest when:", opts: ["MUx = MUy", "TUx = TUy", "marginal utility per dollar is equal across goods", "prices are equal"], a: 2, why: "The rule is about utility per dollar." },
  { q: "A consumer has MUx ÷ Px = 6 and MUy ÷ Py = 3. To raise total utility the consumer should:", opts: ["buy more Y", "buy more X and less Y", "buy more of both", "do nothing"], a: 1, why: "The last dollar on X gives more utility, so switch spending towards X." },
  { q: "As a consumer buys more X, MUx:", opts: ["rises", "falls", "stays constant", "becomes infinite"], a: 1, why: "Diminishing marginal utility lowers the ratio until it equals the other good's." },
''') + CARDS(228, 229, 235, extra='''  ["Budget constraint", "Spending cannot exceed income, given prices."],
  ["MU per dollar", "Marginal utility divided by price."],
  ["Consumer equilibrium", "The bundle where MU per dollar is equal for every good, so total utility is maximised."],
''') + MCQ(241, 243, 244, 246)
write("ut2", page(EY.format(2), "Consumer Equilibrium and the Equi-Marginal Principle",
  "How a rational consumer splits a limited budget between two goods: marginal utility per dollar, switching spending and the condition MUx/Px = MUy/Py. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Consumer Equilibrium and the Equi-Marginal Principle", "consumer-equilibrium-equi-marginal")

# ------------------------------------------------------------------ 30.3
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>When the price of X falls, MUx ÷ Px rises above MUy ÷ Py, so a rational consumer buys more X until MU has fallen enough for the ratios to be equal again. Plotting the price of X against the quantity bought at each equilibrium gives the <b>individual demand curve</b>, and adding across consumers gives the <b>market demand curve</b>. In Marshall's version the demand curve is the MU curve in money terms, and the gap between what a consumer would pay and what is paid is <b>consumer surplus</b>. The theory rests on strong assumptions (measurable utility, rational choice), which is where evaluation comes from.</p></div>
''' + S.b((57, 64)).replace("4 · Deriving", "1 · Deriving") + '''
  <h2>2 · Consumer surplus in numbers</h2>
  <p>A consumer would pay up to $10, $8, $6, $4 and $2 for successive units. At a market price of $5 the consumer buys three units (the first three are worth more than $5 each) and gets a surplus of (10 − 5) + (8 − 5) + (6 − 5) = <b>$9</b>. If the price falls to $3 the consumer buys four units and surplus rises to 7 + 5 + 3 + 1 = <b>$16</b>. A lower price means more units and more surplus.</p>
''' + S.b((66, 71)).replace("5 · Assumptions", "3 · Assumptions")
watch = S.b((84, 86))
explore = S.b((105, 110)).replace("Lab 3 ·", "Lab 1 ·") + S.b((112, 117)).replace("Lab 4 ·", "Lab 2 ·")
practise = '''
  <h2>1 · Assumption of the theory, or criticism of it?</h2><div id="cl2" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the derivation of demand in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = NOTE + S.b((148, 149)) + '''  <div class="rw"><h3>Multi-buy offers</h3><p>"Buy two, get the third half price" works because the third unit is worth less to most buyers than the first. A lower price for the extra unit matches its lower marginal utility.</p><div class="use"><b>Exam use:</b> an everyday example of a downward-sloping demand curve built from diminishing marginal utility.</div></div>
'''
exam = '''
  <h2>Past paper questions on demand and utility theory</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the essay questions that ask for the derivation of the demand curve and for an evaluation of marginal utility theory, a practice question and Paper 3 multiple choice questions. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 12 marks (Paper 4)</td><td>3</td><td>Oct/Nov 2020 (41, 43); Oct/Nov 2021 (42)</td></tr>
    <tr><td>Essay, 13 marks (Paper 4)</td><td>1</td><td>Feb/March 2020 (42), compares indifference curves with MU</td></tr>
    <tr><td>Essay, 20 marks (Paper 4)</td><td>1</td><td>Oct/Nov 2024 (42)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>2 shown below</td><td>2022 to 2023</td></tr>
  </table></div>
  <h2>A · Essay questions</h2>
''' + KEYL + S.b((167, 180), (182, 199), (206, 212), (214, 218), (220, 223)) + '''
  <h2>B · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips = TIPS([(248, 251)], [(259, 261)]) + CMD(EXP, EVA, ("Compare and contrast", "Similarities and differences between two approaches."), ("Examine", "Look closely at the analysis and how the parts connect.")) + FC
js = HEAD + S.j_((73, 96), (136, 166), (177, 184), (195, 202)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Individual demand curve", "Price plotted against the quantity one consumer buys at each equilibrium"],
  ["Market demand curve", "The sum of all individual demand curves"],
  ["Consumer surplus", "The gap between what a consumer is willing to pay and what is paid"],
  ["Cardinal utility", "Utility measured in numbers (utils), as in Marshall's analysis"],
  ["Ordinal utility", "Utility only ranked (more or less), as in indifference curve analysis"],
  ["Bounded rationality", "People use rules of thumb because they cannot process all the information"],
  ["Marginal utility of money", "The extra utility from one more dollar, assumed constant"],
], done: "Seven words for demand and evaluation." });
''' + CALC(209, extra='''  { q: "A consumer would pay $10, $8, $6, $4 and $2 for successive units. The price falls from $5 to $3. How many units are bought at $3?", a: 4, sol: "Buy every unit worth more than $3: $10, $8, $6 and $4, so <b>4 units</b>." },
  { q: "What is the consumer surplus at a price of $3 ($)?", a: 16, sol: "(10 − 3) + (8 − 3) + (6 − 3) + (4 − 3) = 7 + 5 + 3 + 1 = <b>$16</b>." },
  { q: "Using MU analysis, a consumer buys 3 units at $5 and 4 units at $3. What are the two points on the demand curve? Give the quantity at the lower price.", a: 4, sol: "(Q = 3, P = $5) and (Q = 4, P = $3): the quantity at $3 is <b>4</b>." },
''') + QZ(216, 217, 218) + CARDS(230, 231, 232, 234, extra='''  ["Individual demand curve", "Price against quantity for one consumer, from equilibrium at each price."],
  ["Market demand curve", "The horizontal sum of individual demand curves."],
''') + MCQ(245, 248)
write("ut3", page(EY.format(3), "Deriving Demand from Utility and Evaluating the Theory",
  "From a falling price to a new equilibrium: how marginal utility theory builds the individual and market demand curves, consumer surplus, and the assumptions and limits that evaluation questions target. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Deriving Demand from Utility and Evaluating the Theory", "deriving-demand-from-utility")
