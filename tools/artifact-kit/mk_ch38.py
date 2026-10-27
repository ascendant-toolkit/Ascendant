"""Builds the four ch38 part pages (gp1..gp4) from slices of gp.* plus new content. Run: python3 tools/artifact-kit/mk_ch38.py"""
from splitter import Src, page, write, key
S = Src("gp0")  # frozen slice source; gp.body.html now carries the extended whole-chapter page
HEAD = S.j_((1, 9))
import pathlib
_D = pathlib.Path(__file__).parent
def snip(name, n=""): return (_D / f"{name}.html").read_text().replace("__N__", str(n))
EY = "A Level Economics · 9708 · Syllabus 8.1 · Part {} of 4"
def MCQ(old=(), new=""):
    return 'Lib.quiz($("#qz2"), { qs: [\n' + S.j_(*[(i, i) for i in old]) + new + '] });\n'

# ---- 38.1 price controls
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A <b>maximum price</b> (ceiling) is a legal limit set <b>below</b> the equilibrium price, so quantity demanded exceeds quantity supplied and there is a <b>shortage</b>. A <b>minimum price</b> (floor) is set <b>above</b> equilibrium, so supply exceeds demand and there is a <b>surplus</b>. Neither works unless it is <b>binding</b>, meaning it sits on the wrong side of the market price. Both create winners and losers, so the evaluation is about who gains, who loses and what the government does next.</p></div>
''' + snip('gp_lead') + S.b((39, 46)).replace('2 · Price controls','1 · Price controls') + '''
  <h2>2 · Who gains and who loses</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Maximum price (below equilibrium)</th><th>Minimum price (above equilibrium)</th></tr>
    <tr><td><b>Likely gainers</b></td><td>Consumers who still manage to buy at the low price</td><td>Producers who sell at the higher price</td></tr>
    <tr><td><b>Likely losers</b></td><td>Consumers who are rationed out; producers, who sell less and may cut quality</td><td>Consumers, who pay more and buy less; producers who cannot sell all they supply</td></tr>
    <tr><td><b>What replaces the price mechanism</b></td><td>Queues, waiting lists, favouritism, a <b>black market</b> where buyers pay more than the legal price</td><td>Unsold stock, which the government may buy and store, or which goes to waste</td></tr>
    <tr><td><b>Cost to the government</b></td><td>Enforcement; sometimes it must ration or supply the good itself</td><td>Buying the surplus: <b>surplus x price</b>, paid for out of taxation</td></tr>
  </table></div>
  <h2>3 · Evaluating price controls</h2>
  <ul>
    <li><b>Size of the gap.</b> The further the control is from equilibrium, the bigger the shortage or surplus.</li>
    <li><b>Elasticity.</b> The more elastic demand and supply, the larger the shortage or surplus. Supply is usually more elastic in the long run, so a rent ceiling may do more damage over time as landlords sell up or stop building.</li>
    <li><b>Time.</b> A temporary ceiling in an emergency is easier to defend than a permanent one.</li>
    <li><b>Alternatives.</b> A subsidy, a cash benefit or more supply can help the same people without a shortage.</li>
  </ul>
  <div class="tip"><b class="h">Black markets</b>When a ceiling holds quantity supplied at 20, buyers who value the good at up to $80 may be willing to pay far more than the legal $40. The gap invites illegal trade. Watch the third animation.</div>
'''
watch = '''
  <h2>1 · A maximum price</h2><p>Demand P = 100 − Q, supply P = 20 + Q. The government sets a maximum price of $40. Press Play, or click the steps.</p><div id="stA"></div>
  <h2>2 · A minimum price</h2><p>The same market with a minimum price of $80.</p><div id="stB"></div>
  <h2>3 · The black market</h2><p>What happens to the price buyers are really willing to pay when a ceiling holds supply down.</p><div id="stK"></div>
'''
explore = S.b((96, 101)) + '''
  <h2>Lab 2 · The cost of buying the surplus</h2>
  <p>A government sets a minimum price and promises to buy whatever is not sold to consumers. Demand is P = 100 − Q and supply is P = 20 + Q. Below $60 the floor does not bind.</p>
  <div class="card"><div class="grid2"><div><div id="g6"></div>
    <div class="readout"><div><small>Quantity demanded</small><strong id="m1r"></strong></div><div><small>Quantity supplied</small><strong id="m2r"></strong></div><div><small>Surplus</small><strong id="m3r"></strong></div><div><small>Cost to government ($)</small><strong id="m4r"></strong></div></div>
    <div class="verdict" id="mv"></div></div>
    <div><svg id="labE" viewBox="0 0 420 320" role="img" aria-label="Supply and demand with a minimum price and the shaded cost of buying the surplus"></svg></div></div></div>
'''
practise = '''
  <h2>1 · Shortage, surplus or no effect?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the maximum price argument in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = '<p class="note">Examples are explained in general terms. Check current details before quoting them in an exam answer.</p>\n' + S.b((150, 151)) + '''  <div class="rw"><h3>Price caps on energy bills</h3><p>In energy crises several governments capped what suppliers could charge households. Bills were held down, but the cap meant the government (and so taxpayers) or the suppliers carried the gap between the cap and wholesale costs, and the lower price gave households less reason to cut back.</p><div class="use"><b>Exam use:</b> a ceiling used to protect incomes. Evaluate: who pays the difference, and the weaker incentive to save energy.</div></div>
  <div class="rw"><h3>Agricultural guaranteed prices</h3><p>Guaranteeing farmers a price above the market level encouraged over-production in some farm policies, leaving stocks that had to be stored, sold abroad cheaply or destroyed.</p><div class="use"><b>Exam use:</b> the standard minimum price example. Draw the surplus, then say who pays for it.</div></div>
'''
exam = '''
  <h2>Past paper questions on price controls</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Price controls have not been the main focus of a Paper 4 essay in that period. They appear as part of the intervention essays (see part 4 of this chapter) and in Paper 3 multiple choice. Below are the multiple choice questions, then a practice question with a model answer. Mark scheme points are summarised in our own words, not copied.</p>
  <h2>A · Practice question with a model answer</h2>
  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">12 marks</span> Explain, with the help of a diagram, the likely effects of a maximum price set below the equilibrium price in the market for rented housing.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>Define the control. Diagram: demand, supply, ceiling below equilibrium, Qs and Qd, shortage. Effects on tenants, landlords and the market. One evaluative point on elasticity or alternatives.</div>
''' + key() + '''
    <div class="ans">
    <p><span class="mk k" data-t="K">A maximum price is a legal limit on the price that may be charged, set here below the equilibrium rent so that it is binding.</span></p>
    <p><span class="mk n" data-t="N">At the lower rent, the quantity of housing demanded could rise as renting becomes cheaper, while the quantity supplied is likely to fall because landlords earn less and some may sell or convert their properties.</span> <span class="mk n" data-t="N">Demand is then greater than supply, so there is a shortage equal to the gap between Qd and Qs.</span> <span class="mk a" data-t="A">Without the price mechanism, flats may be rationed by waiting lists or by who the landlord prefers, and some tenants may pay extra payments to secure a home.</span></p>
    <p><span class="mk n" data-t="N">Tenants who keep a flat at the capped rent gain, but people who cannot find a home lose, and the quality of housing may fall if landlords spend less on repairs.</span> <span class="mk e" data-t="E">The size of the shortage may depend on elasticity: supply of housing is likely to be more inelastic in the short run, so the shortage may be smaller at first and grow over time. Subsidies for tenants or building more homes could help low-income households without a shortage.</span></p></div>
  </div></details>
  <h2>B · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips = '''
  <h2>Top tips</h2>
  <ul class="tips">
    <li><b>Check where the control sits.</b> A ceiling only bites below the equilibrium price and a floor only above it. Say so, and show it on the diagram.</li>
    <li><b>Label Qd, Qs and the gap.</b> The shortage or surplus is the horizontal distance at the controlled price, not at equilibrium.</li>
    <li><b>Name the rationing method.</b> Queues, waiting lists, favouritism and black markets are the application marks for a ceiling.</li>
    <li><b>For a floor, say who pays for the surplus.</b> Government buying costs surplus times price, funded by taxpayers.</li>
    <li><b>Pick winners and losers.</b> Consumers who get the good against those who do not; producers who sell against those who cannot.</li>
    <li><b>Evaluate with elasticity, time and alternatives.</b> Subsidies or income support can help the same people without a shortage.</li>
  </ul>
  <h2>Sentences you can use</h2>
  <div class="tw"><table class="t">
    <tr><th>You want to say</th><th>Use this sentence</th></tr>
    <tr><td>Ceiling</td><td>"A maximum price set below the equilibrium price creates excess demand, so there is a shortage and some form of rationing is needed."</td></tr>
    <tr><td>Floor</td><td>"A minimum price above equilibrium leaves a surplus, which the government may have to buy at the taxpayers' expense."</td></tr>
    <tr><td>Black market</td><td>"Because supply is held down, buyers who value the good highly may be willing to pay more than the legal price, which could encourage an illegal market."</td></tr>
    <tr><td>Not binding</td><td>"A price control set on the wrong side of equilibrium would not be binding, so it may have no effect."</td></tr>
  </table></div>
  <h2>Command words</h2>
  <div class="tw"><table class="t">
    <tr><th>Command word</th><th>What it asks for</th></tr>
    <tr><td>Explain</td><td>Give reasons, with a chain of cause and effect.</td></tr>
    <tr><td>Analyse</td><td>Break the effect down step by step, usually with a diagram.</td></tr>
    <tr><td>Evaluate</td><td>Weigh the arguments and reach a supported conclusion.</td></tr>
  </table></div>
  <h2>Flashcards</h2><div id="fc1"></div>
'''
js = HEAD + S.j_((10, 42)) + '''
/* black market (Watch 3) */
function bmDraw(s) {
  let o = axes() + marketLines({ d: 1, s: 1 });
  o += SV.line(70, Y(40), X(90), Y(40), "c4", { "stroke-width": 3, ...op(s.c) }) + SV.text(X(90) - 4, Y(40) + 18, "Maximum price $40", "lbl bd t4", { "text-anchor": "end", ...op(s.c) });
  o += SV.line(X(20), Y(40), X(20), Y(80), "gr", op(s.u)) + SV.circle(X(20), Y(40), 6, "dot2", op(s.u)) + SV.circle(X(20), Y(80), 6, "dot1", op(s.u)) + SV.text(X(20), 350, "Qs = 20", "lbl bd", { "text-anchor": "middle", ...op(s.u) });
  o += SV.line(70, Y(80), X(20), Y(80), "c3", { "stroke-dasharray": "6 5", ...op(s.bm) }) + SV.text(66, Y(80) + 4, "80", "sm bd", { "text-anchor": "end", ...op(s.bm) }) + SV.text(X(20) + 14, Y(80) - 12, "Black market price up to $80", "lbl bd t3", { ...halo, ...op(s.bm) });
  return o;
}
Lib.stepper($("#stK"), { w: 780, h: 370, label: "A maximum price holding supply at 20 units while buyers would pay up to 80", base: { c: 0, u: 0, bm: 0 }, draw: bmDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The ceiling.</b> The government holds the price at <b>$40</b>, below the $60 equilibrium.", s: { c: 1 } },
  { cap: "<b>Supply is held down.</b> At $40 firms supply only <b>20</b> units. Read up the vertical line to the demand curve.", s: { c: 1, u: 1 } },
  { cap: "<b>Buyers would pay up to $80</b> for the 20th unit (the demand curve at 20). The legal price of $40 leaves a big gap that sellers can exploit: a <b>black market</b> may charge close to $80, so the ceiling can help some consumers but hurt others.", s: { c: 1, u: 1, bm: 1 } },
] });
''' + S.j_((61, 76)) + '''
/* ---------- Lab 2: buying the surplus ---------- */
function lab5() {
  if (!$("#mp")) return;
  const p = +$("#mp").value, qd = Math.max(0, 100 - p), qs = Math.max(0, p - 20), sur = p > 60 ? qs - qd : 0, cost = sur * p;
  $("#m1r").textContent = qd; $("#m2r").textContent = qs; $("#m3r").textContent = sur || "none"; $("#m4r").textContent = "$" + cost;
  $("#mv").textContent = p <= 60 ? `A minimum of $${p} is at or below the market price of $60, so it is not binding: no surplus and no cost.`
    : `At $${p} consumers buy ${qd} but firms supply ${qs}: a surplus of ${sur}. If the government buys it all, the cost is ${sur} x $${p} = $${cost}, paid by taxpayers. The higher the floor, the bigger the surplus and the bill.`;
  const x = (v) => 40 + v * 3.9, y = (v) => 270 - v * 2.4;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "Price ($)", "sm");
  if (sur > 0) o += SV.rect(x(qd), y(p), x(qs) - x(qd), 270 - y(p), "f3") + SV.text((x(qd) + x(qs)) / 2, y(p) + (270 - y(p)) / 2 + 4, "cost $" + cost, "lbl bd", { "text-anchor": "middle" });
  o += SV.line(x(0), y(100), x(90), y(10), "c1") + SV.line(x(0), y(20), x(80), y(100), "c2") + SV.line(40, y(p), 400, y(p), p > 60 ? "c3" : "gr", { "stroke-width": 3 });
  o += SV.circle(x(qd), y(p), 6, "dot1") + SV.circle(x(qs), y(p), 6, "dot2") + SV.text(x(qd), 288, "Qd", "sm bd t1", { "text-anchor": "middle" }) + SV.text(x(qs), 306, "Qs", "sm bd t2", { "text-anchor": "middle" });
  $("#labE").innerHTML = o;
}
Lib.slider($("#g6"), { id: "mp", label: "Minimum price ($): ", min: 40, max: 100, step: 5, value: 80, fmt: (v) => v, onInput: lab5 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "The market price is $60. What happens with each price control?",
  buckets: [{ label: "Shortage" }, { label: "Surplus" }, { label: "No effect" }],
  items: [
    { text: "Maximum price of $40", b: 0 }, { text: "Rent ceiling below the market rent", b: 0 }, { text: "Cap on bread prices below the market price", b: 0 },
    { text: "Minimum price of $80", b: 1 }, { text: "Guaranteed farm price above the market price", b: 1 }, { text: "Minimum price for alcohol above the market price", b: 1 },
    { text: "Maximum price of $80", b: 2 }, { text: "Minimum price of $50", b: 2 }, { text: "A ceiling above the price firms already charge", b: 2 },
  ], done: "Only a control on the wrong side of the market price is binding.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Maximum price", "A legal limit below the market price, causing a shortage"],
  ["Minimum price", "A legal floor above the market price, causing a surplus"],
  ["Binding", "A control set on the side of equilibrium where it changes the outcome"],
  ["Shortage", "Quantity demanded is greater than quantity supplied"],
  ["Surplus", "Quantity supplied is greater than quantity demanded"],
  ["Rationing", "Deciding who gets the good when there is not enough, by queue, waiting list or favour"],
  ["Black market", "Illegal trade at a price above the legal maximum"],
], done: "Seven words to use in every price control answer." });
''' + S.j_((164, 171)) + '''
Lib.calc($("#c1"), { qs: [
  { q: "Demand is P = 100 − Q and supply is P = 20 + Q. A maximum price of $40 is set. What is the shortage (units)?", a: 40, hint: "Qd = 100 − P and Qs = P − 20.", sol: "Qd = 60, Qs = 20, shortage = <b>40</b>." },
  { q: "A minimum price of $80 is set in the same market. What is the surplus (units)?", a: 40, sol: "Qd = 20, Qs = 60, surplus = <b>40</b>." },
  { q: "Another market has Qd = 200 − 10P and Qs = 50 + 5P. A maximum price of $6 is set. What is the shortage (units)?", a: 60, hint: "Equilibrium is $10 and 100 units, so $6 is binding.", sol: "Qd = 200 − 60 = 140, Qs = 50 + 30 = 80. Shortage = <b>60</b>." },
  { q: "In that market a minimum price of $14 is set. What is the surplus (units)?", a: 60, sol: "Qd = 200 − 140 = 60, Qs = 50 + 70 = 120. Surplus = <b>60</b>." },
  { q: "The government buys the whole surplus at $14. What is the cost ($)?", a: 840, sol: "60 x 14 = <b>$840</b>." },
  { q: "With the $6 maximum only 80 units are supplied. At what price would consumers demand exactly 80 units, a guide to the black market price ($)?", a: 12, hint: "Solve 200 − 10P = 80.", sol: "10P = 120, so P = <b>$12</b>, double the legal price." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A maximum price set above the equilibrium price is likely to:", opts: ["cause a shortage", "cause a surplus", "have no effect", "raise supply"], a: 2, why: "It is not binding, because the market price is already below the limit." },
  { q: "A binding minimum price will most likely:", opts: ["leave a surplus", "cause a shortage", "lower the price", "raise quantity demanded"], a: 0, why: "At the higher price, quantity supplied exceeds quantity demanded." },
  { q: "Rent control is an example of:", opts: ["a minimum price", "a maximum price", "a subsidy", "a tradable permit"], a: 1, why: "It sets a legal limit on the rent a landlord may charge." },
  { q: "Who pays for a surplus bought by the government after a minimum price?", opts: ["Taxpayers", "Consumers only", "Producers only", "Nobody"], a: 0, why: "The purchase is funded from tax revenue." },
  { q: "A black market is most likely to appear when:", opts: ["a ceiling holds supply well below demand", "a floor is above equilibrium", "supply is perfectly elastic", "the government subsidises the good"], a: 0, why: "Buyers who cannot get the good at the legal price may pay more to illegal sellers." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Maximum price", "A legal limit below equilibrium: causes a shortage."],
  ["Minimum price", "A legal floor above equilibrium: causes a surplus."],
  ["Binding", "A control that is on the wrong side of the market price, so it changes the outcome."],
  ["Shortage", "Quantity demanded greater than quantity supplied."],
  ["Surplus", "Quantity supplied greater than quantity demanded."],
  ["Rationing", "How scarce goods are shared when price cannot do it: queues, waiting lists, favouritism."],
  ["Black market", "Illegal trade above the legal maximum price."],
  ["Guaranteed price", "A minimum price, usually for farm products, backed by government buying."],
  ["Cost of buying the surplus", "Surplus times the minimum price."],
  ["Alternatives to price controls", "Subsidies, cash benefits and increasing supply."],
] });
''' + MCQ([215], '''  { q: "[Oct/Nov 2023 · 33 · Q15] To control the cost of living, governments have sometimes imposed a maximum price on certain goods that is below the free market price. What is often an undesirable side effect of such a policy?", opts: ["accelerating general inflation", "an increase in profits above normal profits", "an increase in the stocks of unsold goods held by firms", "shortages of the good"], a: 3, why: "A price below equilibrium makes quantity demanded exceed quantity supplied. C describes the effect of a minimum price." },
  { q: "[May/June 2021 · 31 · Q30] A government is increasing the role of market forces in its economy. However, it imposed temporary maximum price controls. Why might a government, committed to reducing central planning, introduce price controls?", opts: ["to increase allocative efficiency", "to increase the incentive for producers to raise supply", "to reduce consumer demand", "to reduce expectations of inflation"], a: 3, why: "A temporary cap on prices may stop price rises being expected while markets are freed. A ceiling does not raise efficiency, supply or cut demand." },
''')
write("gp1", page(EY.format(1), "Maximum and Minimum Prices",
  "Price ceilings and floors: what a binding control does to quantity demanded and supplied, who gains and loses, how black markets appear and what it costs to buy up a surplus. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Maximum and Minimum Prices", "maximum-minimum-prices")

# ---- 38.2 taxes, subsidies and permits
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>An <b>indirect tax</b> raises the cost of supply, so price rises and quantity falls, and an <b>external cost</b> can be corrected if the tax equals it. A <b>subsidy</b> lowers the cost of supply, so price falls and quantity rises, which suits goods with <b>external benefits</b>. <b>Tradable permits</b> fix the total amount of pollution and let firms trade the right to emit, so the cap is met at the lowest cost. All three use the price mechanism rather than orders, but each depends on the government getting the size or the cap right.</p></div>
''' + S.b((48, 55)).replace('3 · Indirect','1 · Indirect') + '''
  <h2>2 · Who really pays? Elasticity and incidence</h2>
  <div class="tw"><table class="t">
    <tr><th>Situation</th><th>Who bears more of the tax</th><th>Effect on quantity</th></tr>
    <tr><td>Demand inelastic (steep), supply elastic</td><td>Consumers</td><td>Falls only a little</td></tr>
    <tr><td>Demand elastic, supply inelastic (steep)</td><td>Producers</td><td>Falls a little</td></tr>
    <tr><td>Both elastic</td><td>Shared</td><td>Falls a lot</td></tr>
  </table></div>
  <p>This is why a tax on cigarettes raises plenty of revenue but may not cut smoking much, and why a tax is better at reducing consumption when demand is elastic. Use the Explore tab to see it.</p>

  <h2>3 · Subsidies</h2>
  <p>A per-unit subsidy shifts the supply curve <b>down</b> by the subsidy. In the market with demand P = 100 − Q and supply P = 20 + Q, a $20 subsidy moves the equilibrium from 40 units at $60 to <b>50 units</b>: consumers pay <b>$50</b>, producers receive <b>$70</b>, and the cost to the government is $20 x 50 = <b>$1000</b>. The gain is shared, here equally, and again the split depends on elasticities.</p>
  <ul>
    <li><b>Why:</b> positive externalities and merit goods are under-consumed, so a subsidy moves output towards the social optimum.</li>
    <li><b>Costs:</b> paid by taxpayers (an opportunity cost), may go to people who would have bought anyway, and is hard to set at the right level.</li>
  </ul>
''' + S.b((57, 58)) + '''
  <ul>
    <li>With no trading, each of two firms must cut by 5 units. A cuts a unit for $2 and B for $8, so the total cost is 5 x 2 + 5 x 8 = $50.</li>
    <li>With trading, A cuts all 10 units for $20 and sells its spare permits to B, which avoids the dearer cuts. The cap is the same, but the total cost is $20.</li>
  </ul>
  <h2>5 · Choosing between them</h2>
  <div class="tw"><table class="t">
    <tr><th>Tool</th><th>Strength</th><th>Weakness</th></tr>
    <tr><td>Tax</td><td>Raises revenue; firms choose how to cut</td><td>Hard to set equal to the external cost; regressive; little effect if demand is inelastic</td></tr>
    <tr><td>Subsidy</td><td>Encourages good outputs; popular</td><td>Costs taxpayers; may be wasted</td></tr>
    <tr><td>Permits</td><td>Fixes the amount of pollution; lowest cost cut</td><td>Cap may be too high; needs monitoring; prices can swing</td></tr>
  </table></div>
'''
watch = '''
  <h2>1 · An indirect tax and who pays it</h2><p>A $20 per unit tax on the market with demand P = 100 − Q and supply P = 20 + Q.</p><div id="stC"></div>
  <h2>2 · A subsidy</h2><p>The same market with a $20 per unit subsidy.</p><div id="stS"></div>
  <h2>3 · Tradable pollution permits</h2><p>Two firms, each emitting 10 units, with a cap of 10 in total. A cuts a unit for $2 and B for $8. Permits trade at $5.</p><div id="stP"></div>
'''
explore = S.b((103, 115)).replace('Lab 2 · Who','Lab 1 · Who').replace('Lab 3 · Trading','Lab 2 · Trading') + '''
  <h2>Lab 3 · Who gains from the subsidy?</h2>
  <p>Demand is P = 100 − Q and supply is P = 20 + Q. Set the subsidy and read off what consumers pay, what producers receive and what it costs.</p>
  <div class="card"><div class="grid2"><div><div id="g7"></div>
    <div class="readout"><div><small>Consumers pay</small><strong id="b1"></strong></div><div><small>Producers receive</small><strong id="b2"></strong></div><div><small>Quantity</small><strong id="b3"></strong></div><div><small>Cost to government</small><strong id="b4"></strong></div></div>
    <div class="verdict" id="bv"></div></div>
    <div><svg id="labF" viewBox="0 0 420 300" role="img" aria-label="Supply and demand with a per unit subsidy showing what consumers pay and producers receive"></svg></div></div></div>
'''
practise = '''
  <h2>1 · Tax, subsidy or permits?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the tax explanation in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = '<p class="note">Examples are explained in general terms. Check current details before quoting them in an exam answer.</p>\n' + S.b((149, 149), (152, 152)) + '''  <div class="rw"><h3>Subsidies for electric vehicles and solar panels</h3><p>Many governments have paid part of the cost of electric cars or solar panels to speed up a switch away from fossil fuels. Prices to buyers are lower and demand is higher, but taxpayers pay, and some buyers would have bought anyway.</p><div class="use"><b>Exam use:</b> a subsidy for a good with positive externalities. Evaluate: cost, who benefits, and whether the subsidy equals the external benefit.</div></div>
  <div class="rw"><h3>Congestion and parking permits</h3><p>Some cities have tried tradable parking permits or congestion charges to cut road use. The idea is to put a price on a cost drivers otherwise ignore.</p><div class="use"><b>Exam use:</b> a Paper 3 question asked why tradable parking permits might fail: if too few households own extra cars, the permit market is very small.</div></div>
'''
exam = '''
  <h2>Past paper questions on taxes, subsidies and permits</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). The long written questions on taxes and subsidies for externalities sit in syllabus 7.4, part 3 (policies for externalities). Here are the Paper 3 multiple choice questions on the tools themselves, and a practice question with a model answer. Mark scheme points are summarised in our own words, not copied.</p>
  <h2>A · Practice question with a model answer</h2>
  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">12 marks</span> Using a diagram, explain who is likely to bear most of an indirect tax on cigarettes.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>Define an indirect tax and show S shifting up. Mark the price consumers pay, the price producers receive and the tax revenue. Link the split to elasticity. Evaluate.</div>
''' + key() + '''
    <div class="ans">
    <p><span class="mk k" data-t="K">An indirect tax is a tax on spending, charged per unit on producers, which raises their cost of supply, so the supply curve shifts up by the amount of the tax.</span></p>
    <p><span class="mk n" data-t="N">Demand for cigarettes is likely to be price inelastic because they are addictive and have few substitutes, so the demand curve is steep. When supply shifts up, the price rises by a large part of the tax, and the quantity falls by only a small amount.</span> <span class="mk a" data-t="A">Smokers are therefore likely to bear most of the tax, and producers keep a larger share of the price, while the government collects large revenue because so many units are still sold.</span></p>
    <p><span class="mk e" data-t="E">The split could differ in the long run, because demand may become more elastic as people quit or switch to alternatives, and because tax is often a larger share of low incomes. Overall, consumers are likely to bear most of the burden, which suits raising revenue more than cutting consumption.</span></p></div>
  </div></details>
  <h2>B · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips = '''
  <h2>Top tips</h2>
  <ul class="tips">
    <li><b>Draw the tax as a shift of supply up by the tax</b>, then label the price consumers pay, the price producers receive, the new quantity and the revenue box.</li>
    <li><b>Talk about elasticity and incidence.</b> Inelastic demand means little change in quantity and more of the burden on consumers.</li>
    <li><b>A tax equal to the external cost internalises it.</b> Say so, and then say that the government may not know the right figure.</li>
    <li><b>For a subsidy, shift supply down</b> and show the cost as subsidy times quantity. Link it to positive externalities and merit goods.</li>
    <li><b>For permits, say the total is capped and the cost of cutting is minimised.</b> Evaluate the level of the cap and permit price swings.</li>
    <li><b>Compare the tools</b> in evaluation: cost, revenue, certainty about the outcome and who is affected.</li>
  </ul>
  <h2>Sentences you can use</h2>
  <div class="tw"><table class="t">
    <tr><th>You want to say</th><th>Use this sentence</th></tr>
    <tr><td>Tax incidence</td><td>"Because demand is inelastic, consumers bear most of the tax and the quantity falls only slightly."</td></tr>
    <tr><td>Internalise</td><td>"A tax equal to the external cost could internalise the externality and move output towards the social optimum."</td></tr>
    <tr><td>Subsidy</td><td>"A subsidy lowers the cost of supply, so price falls and quantity rises, but it is paid for by taxpayers."</td></tr>
    <tr><td>Permits</td><td>"Tradable permits cap total pollution while allowing firms with low abatement costs to cut more and sell their permits."</td></tr>
  </table></div>
  <h2>Command words</h2>
  <div class="tw"><table class="t">
    <tr><th>Command word</th><th>What it asks for</th></tr>
    <tr><td>Explain</td><td>Give reasons, with a chain of cause and effect.</td></tr>
    <tr><td>Assess</td><td>Judge how important or effective something is, with reasons.</td></tr>
    <tr><td>Evaluate</td><td>Weigh the arguments and reach a supported conclusion.</td></tr>
  </table></div>
  <h2>Flashcards</h2><div id="fc1"></div>
'''
js = HEAD + S.j_((44, 59)) + '''
/* subsidy (Watch 2) */
function subDraw(s) {
  let o = axes() + marketLines(s) + eqMark(s);
  if (s.sub > 0) o += SV.line(X(0), Y(0), X(80), Y(80), "c3", { "stroke-dasharray": "6 5", ...op(s.sub) }) + SV.text(X(68), Y(68) + 22, "S − subsidy $20", "lbl bd t3", { ...halo, ...op(s.sub) });
  if (s.res > 0) o += SV.rect(70, Y(60), X(50) - 70, Y(50) - Y(60), "f1", op(s.res)) + SV.rect(70, Y(70), X(50) - 70, Y(60) - Y(70), "f4", op(s.res)) + SV.line(X(50), Y(70), X(50), 330, "gr", op(s.res)) +
    SV.circle(X(50), Y(50), 6, "dot1", op(s.res)) + SV.circle(X(50), Y(70), 6, "dot4", op(s.res)) + SV.text(66, Y(70) + 4, "70", "sm bd", { "text-anchor": "end", ...op(s.res) }) + SV.text(66, Y(50) + 4, "50", "sm bd", { "text-anchor": "end", ...op(s.res) }) + SV.text(X(50), 350, "50", "lbl bd", { "text-anchor": "middle", ...op(s.res) }) +
    SV.text(X(25), Y(55) + 4, "consumers gain $10 a unit", "lbl bd t1", { "text-anchor": "middle", ...halo, ...op(s.res) }) + SV.text(X(25), Y(65) + 4, "producers gain $10 a unit", "lbl bd t4", { "text-anchor": "middle", ...halo, ...op(s.res) });
  return o;
}
Lib.stepper($("#stS"), { w: 780, h: 370, label: "A per unit subsidy shifting supply down and the gain shared between consumers and producers", base: { d: 0, s: 0, eq: 0, sub: 0, res: 0 }, draw: subDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The free market.</b> Equilibrium at $60 and 40 units.", s: { d: 1, s: 1, eq: 1 } },
  { cap: "<b>The subsidy.</b> A payment of $20 on each unit lowers every supplier's cost by $20, so the supply curve shifts <b>down by $20</b>.", s: { d: 1, s: 1, eq: 0.6, sub: 1 } },
  { cap: "<b>The new equilibrium.</b> Quantity rises to <b>50</b>. Consumers pay <b>$50</b>, a fall of $10. Producers receive $50 + $20 = <b>$70</b>, a rise of $10. Each side gains half of the subsidy here because demand and supply have equal slopes.", s: { d: 1, s: 1, eq: 0.6, sub: 1, res: 1 } },
  { cap: "<b>The cost to the government</b> is $20 × 50 = <b>$1000</b>, paid by taxpayers. For a good with a positive externality, the extra output moves the market towards the social optimum.", s: { d: 1, s: 1, eq: 0.6, sub: 1, res: 1 } },
] });

/* permits (Watch 3) */
function permDraw(s) {
  const base = 250, H = (v) => v * 4;
  let o = SV.line(60, base, 740, base) + SV.text(62, 24, "Cost ($)", "sm");
  [["Firm A", 110, 10, -5], ["Firm B", 330, 40, 25], ["Total", 550, 50, 20]].forEach(([l, x, n, t]) => {
    if (s.n > 0) { const h = H(n) * s.n; o += SV.rect(x, base - h, 70, h, "f2", op(s.n)) + SV.text(x + 35, base - h - 6, "$" + n, "lbl bd", { "text-anchor": "middle", ...op(s.n) }) + SV.text(x + 35, 304, "No trading", "sm", { "text-anchor": "middle", ...op(s.n) }); }
    if (s.t > 0) { const h = H(Math.abs(t)) * s.t, up = t >= 0; o += SV.rect(x + 80, up ? base - h : base, 70, h, "f3", op(s.t)) + SV.text(x + 115, up ? base - h - 6 : base + h + 16, (t < 0 ? "−" : "") + "$" + Math.abs(t), "lbl bd", { "text-anchor": "middle", ...op(s.t) }) + SV.text(x + 115, 304, "Trading at $5", "sm", { "text-anchor": "middle", ...op(s.t) }); }
    o += SV.text(x + 75, 332, l, "lbl bd", { "text-anchor": "middle" });
  });
  return o;
}
Lib.stepper($("#stP"), { w: 780, h: 345, label: "Costs of cutting pollution for two firms with and without permit trading", base: { n: 0, t: 0 }, draw: permDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The cap.</b> Each firm emits 10 units. The government wants no more than 10 in total, so it issues <b>5 permits to each firm</b>.", s: { n: 0, t: 0 } },
  { cap: "<b>No trading.</b> Each firm must cut 5 units. A pays 5 × $2 = $10, B pays 5 × $8 = $40: a total cost of <b>$50</b>.", s: { n: 1, t: 0 } },
  { cap: "<b>Trading at $5.</b> A cuts all 10 units for $20 and sells 5 spare permits for $25, so its net cost is <b>−$5</b>. B buys 5 permits for $25 instead of cutting its own pollution at $8 a unit.", s: { n: 1, t: 1 } },
  { cap: "<b>The same cap, a lower cost.</b> The real cost of cutting falls from $50 to <b>$20</b>, a saving of $30, because cuts are made where they are cheapest. Both firms are better off than with no trading.", s: { n: 1, t: 1 } },
] });
''' + S.j_((78, 112)) + '''
/* ---------- Lab 3: subsidy ---------- */
function lab6() {
  if (!$("#sb")) return;
  const s = +$("#sb").value, q = (80 + s) / 2, pc = 100 - q, pp = pc + s, cost = s * q;
  $("#b1").textContent = "$" + Lib.fmtN(pc, 1); $("#b2").textContent = "$" + Lib.fmtN(pp, 1); $("#b3").textContent = Lib.fmtN(q, 1); $("#b4").textContent = "$" + Lib.fmtN(cost, 0);
  $("#bv").textContent = s === 0 ? "No subsidy: the market is at its equilibrium of $60 and 40 units."
    : `Consumers pay $${Lib.fmtN(pc, 1)}, $${Lib.fmtN(60 - pc, 1)} less than before, and producers receive $${Lib.fmtN(pp, 1)}, $${Lib.fmtN(pp - 60, 1)} more. Output rises from 40 to ${Lib.fmtN(q, 1)}. The government pays ${s} on each of ${Lib.fmtN(q, 1)} units: $${Lib.fmtN(cost, 0)}.`;
  const x = (v) => 40 + v * 3.6, y = (v) => 270 - v * 2.4;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "Price ($)", "sm");
  o += SV.rect(40, y(60), x(q) - 40, y(pc) - y(60), "f1") + SV.rect(40, y(pp), x(q) - 40, y(60) - y(pp), "f4");
  o += SV.line(x(0), y(100), x(100), y(0), "c1") + SV.line(x(0), y(20), x(80), y(100), "c2") + (s > 0 ? SV.line(x(0), y(20 - s), x(80), y(100 - s), "c3", { "stroke-dasharray": "6 5" }) : "");
  o += SV.circle(x(q), y(pc), 6, "dot1") + SV.circle(x(q), y(pp), 6, "dot4") + SV.text(x(q) + 10, y(pc) + 16, "consumers pay", "sm bd t1") + SV.text(x(q) + 10, y(pp) - 6, "producers receive", "sm bd t4");
  $("#labF").innerHTML = o;
}
Lib.slider($("#g7"), { id: "sb", label: "Subsidy per unit ($): ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v, onInput: lab6 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Which tool fits each problem best?",
  buckets: [{ label: "Indirect tax" }, { label: "Subsidy" }, { label: "Tradable permits" }],
  items: [
    { text: "Cigarettes (a demerit good)", b: 0 }, { text: "Plastic bags", b: 0 }, { text: "Fuel with a carbon cost", b: 0 },
    { text: "Vaccinations (positive externality)", b: 1 }, { text: "Rooftop solar panels", b: 1 }, { text: "Public transport use", b: 1 },
    { text: "Power stations with a fixed national limit on emissions", b: 2 }, { text: "Factories that can cut pollution at very different costs", b: 2 },
  ], done: "Tax and permits for negative externalities, subsidy for positive ones.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Indirect tax", "A tax on spending that raises the cost of supply"],
  ["Specific tax", "A fixed amount per unit"],
  ["Ad valorem tax", "A percentage of the price"],
  ["Tax incidence", "How the burden of a tax is shared between buyers and sellers"],
  ["Subsidy", "A payment that lowers the cost of supply or consumption"],
  ["Tradable permits", "A cap on pollution with permits that firms can buy and sell"],
  ["Internalise an externality", "Make the decision maker pay the external cost"],
], done: "Seven words that cover the price tools." });
Lib.order($("#o1"), { prompt: "Put the explanation of a per-unit tax in order.", items: [
  "The government imposes a tax per unit on producers",
  "Costs of supply rise by the amount of the tax, so the supply curve shifts up",
  "The market price rises and the equilibrium quantity falls",
  "The burden is shared between consumers and producers, depending on elasticities",
  "The government collects revenue equal to the tax times the new quantity",
  "Evaluate: elasticity, whether the tax equals the external cost, and who is hit hardest",
], done: "This chain works for any indirect tax question." });
Lib.calc($("#c1"), { qs: [
  { q: "Demand is P = 100 − Q and supply is P = 20 + Q. A $20 tax shifts supply to P = 40 + Q. What is the new quantity?", a: 30, sol: "100 − Q = 40 + Q gives Q = <b>30</b>." },
  { q: "What is the government's tax revenue ($)?", a: 600, sol: "20 x 30 = <b>$600</b>." },
  { q: "The price consumers pay rises from $60 to $70. What share of the $20 tax do consumers bear (%)?", a: 50, sol: "10 ÷ 20 x 100 = <b>50%</b>." },
  { q: "A $20 subsidy shifts supply to P = Q. What is the new quantity?", a: 50, sol: "100 − Q = Q gives Q = <b>50</b>." },
  { q: "What is the cost of the subsidy to the government ($)?", a: 1000, sol: "20 x 50 = <b>$1000</b>." },
  { q: "What price do producers receive after the subsidy ($)?", a: 70, hint: "Consumers pay 50. Add the subsidy.", sol: "50 + 20 = <b>$70</b>." },
  { q: "Without trading each firm cuts 5 units: A at $2 and B at $8 a unit. With trading A cuts all 10 units. By how much does the total cost fall ($)?", a: 30, sol: "Before: 5 x 2 + 5 x 8 = 50. After: 10 x 2 = 20. Fall = <b>$30</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An indirect tax shifts the supply curve:", opts: ["up by the amount of the tax", "down by the amount of the tax", "to the right", "not at all"], a: 0, why: "The tax is a cost to producers, so supply moves up (to the left)." },
  { q: "A per-unit tax on a good with inelastic demand will mostly:", opts: ["cut quantity sharply", "raise the price paid by consumers and cut quantity little", "reduce the price paid by consumers", "have no effect on government revenue"], a: 1, why: "Consumers bear most of the burden and quantity changes little." },
  { q: "A subsidy to producers:", opts: ["raises price and lowers quantity", "lowers price and raises quantity", "lowers price and quantity", "has no effect on price"], a: 1, why: "Supply shifts down, so price falls and quantity rises." },
  { q: "Tradable pollution permits are most likely to:", opts: ["remove the cap on emissions", "meet a pollution cap at lower total cost", "raise emissions", "make permits free for ever"], a: 1, why: "Firms with low abatement costs cut more and sell permits." },
  { q: "The best reason for a tax set equal to the external cost is that it:", opts: ["raises more revenue than any other", "makes the decision maker pay the full cost", "stops all pollution", "has no effect on prices"], a: 1, why: "It internalises the externality." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Indirect tax", "A tax on spending, which shifts supply up by the amount of the tax."],
  ["Specific tax", "A fixed amount per unit sold."],
  ["Ad valorem tax", "A percentage of the price."],
  ["Subsidy", "A payment that lowers firms' costs, shifting supply down."],
  ["Tax incidence", "Who actually bears the burden of a tax, decided by elasticities."],
  ["Tax revenue", "Tax per unit times quantity sold after the tax."],
  ["Internalise", "Make the producer or consumer pay the external cost."],
  ["Tradable permits", "A cap on total pollution with permits that can be traded."],
  ["Abatement cost", "The cost of reducing a unit of pollution."],
  ["Regressive tax", "Takes a larger share of income from low earners."],
] });
''' + MCQ([216], '''  { q: "[Feb/March 2025 · 32 · Q10] What is not a reason for imposing a tax on producers based on the amount of pollution caused in the production process?", opts: ["Firms have a financial incentive to reduce pollution.", "It is relatively hard to administer and monitor this tax scheme.", "Some firms cause less pollution than others.", "Taxes on pollution reduce negative production externalities."], a: 1, why: "Difficulty of administration is a drawback, not a reason for the tax. A, C and D are arguments in its favour." },
  { q: "[Feb/March 2025 · 32 · Q11] A government introduced a tax on soft drinks containing sugar. It was forecast that the tax would raise £520m per year, but the tax received was £240m. What is the most likely reason why the tax collected was lower than forecast?", opts: ["a specific tax instead of an ad valorem tax was introduced", "fewer drinks than originally forecast contained sugar", "most retailers did not increase the price of soft drinks", "the demand for soft drinks was price inelastic"], a: 1, why: "If firms reduced the sugar in their drinks, fewer products were taxed. Inelastic demand would have kept revenue high." },
  { q: "[Feb/March 2022 · 32 · Q13] A government wishes to reduce the negative externalities caused by the use of coal. Which policy should the government use?", opts: ["Impose an indirect tax on the production of hydroelectric power.", "Increase income tax.", "Remove any restrictions on coal production.", "Subsidise wind-powered electricity production."], a: 3, why: "Subsidising a cleaner substitute reduces the use of coal. A and C would increase or not change the use of coal." },
  { q: "[May/June 2022 · 31 · Q14] A government issues free non-tradeable pollution permits to firms. In a change in legislation, the permits can be traded with other firms. What will be the impact on the profits of the firms that are now buyers or sellers of the permits?", opts: ["buyers decrease, sellers decrease", "buyers decrease, sellers increase", "buyers increase, sellers decrease", "buyers increase, sellers increase"], a: 1, why: "Buyers now pay for permits they used to receive free, so their profit falls; sellers earn revenue from permits they no longer need." },
  { q: "[May/June 2022 · 32 · Q13] To reduce road congestion caused by parked cars, a local government introduced a system of tradable parking permits. Households were given a permit allowing them to park one car. Households with more than one car could buy extra permits from households with no cars. What is the most likely reason for this policy to fail?", opts: ["Fines for drivers parking without a permit will internalise the externality.", "The local government has a monopoly over the issue of parking permits.", "Those suffering from too many parked cars are compensated by the households owning extra cars.", "Too many households own cars so the market in permits is very small."], a: 3, why: "A permit market needs buyers and sellers. If few households have spare permits to sell, trading cannot work well." },
''')
write("gp2", page(EY.format(2), "Indirect Taxes, Subsidies and Tradable Permits",
  "The price-based tools for market failure: how a tax shifts supply and who bears it, how a subsidy works, and how permits cap pollution at the lowest cost. Animated diagrams built from numbers, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Indirect Taxes, Subsidies and Tradable Permits", "taxes-subsidies-permits")

# ---- 38.3 regulation, provision, privatisation, nudges
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>When prices and taxes are not enough, governments use <b>laws</b> (regulation and competition policy), <b>ownership and provision</b> (nationalisation, privatisation, public goods and merit goods supplied by the state) and <b>information and nudges</b>. A <b>natural monopoly</b> such as a water network cannot easily be made competitive, so the choice is between public ownership and a regulated private firm, often with a <b>price cap</b>. A cap at marginal cost is allocatively efficient but may leave the firm making a loss, while a cap at average cost keeps normal profit. Each approach has costs, so the evaluation compares them.</p></div>

  <h2>1 · Regulation and competition policy</h2>
  <div class="grid2">
    <div class="card"><h3>Regulation</h3><p>Rules backed by law: bans, standards, licences, price caps and quality targets. They are quick and certain, but cost money to enforce, give no reward for doing better than the standard and may be influenced by the firms being regulated (<b>regulatory capture</b>).</p></div>
    <div class="card"><h3>Competition policy</h3><p>Laws that review mergers, ban cartels and stop firms abusing a dominant position. The aim is to keep prices low and choice high. Regulators may lack information on costs, and breaking up firms can lose economies of scale.</p></div>
  </div>

  <h2>2 · A price cap on a natural monopoly</h2>
  <p>A water network has a fixed cost of $800 and a marginal cost of $20 a unit, so average cost falls as output rises. Demand is P = 100 − Q. Left alone, the monopolist sets MR = MC: <b>Q = 40, P = $60</b> and a supernormal profit of $800.</p>
  <ul>
    <li><b>Cap at marginal cost ($20):</b> allocative efficiency, output 80, but the firm loses $800 and needs a subsidy or may leave.</li>
    <li><b>Cap at average cost ($31.70):</b> output 68, price just covers cost, so the firm earns only normal profit and consumers get far more than under monopoly.</li>
  </ul>
  <p>The Watch and Explore tabs show this. Regulators rarely know the true cost curves, which is why price cap regulation is only as good as its information.</p>
''' + S.b((65, 65)) + '''
  <h2>3 · State provision, nationalisation and privatisation</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>In favour</th><th>Against</th></tr>
    <tr><td><b>State provision / nationalisation</b></td><td>Public goods and merit goods are supplied whatever the profit; control of natural monopolies; decisions may reflect social benefits</td><td>Risk of X-inefficiency (costs higher than necessary), losses paid by taxpayers, political interference, may crowd out private supply</td></tr>
    <tr><td><b>Privatisation</b></td><td>Competition and shareholder scrutiny may raise efficiency; access to private funds; government stops funding losses and receives sale proceeds</td><td>A state monopoly may become a private monopoly; unprofitable but valuable services may be cut; regulation is still needed</td></tr>
  </table></div>
  <p>Evaluation turns on whether competition can develop. Privatising a market that can be competitive is likely to improve efficiency; privatising a natural monopoly leaves the monopoly problem, so strong regulation matters.</p>

  <h2>4 · Information and nudges</h2>
  <p>People often choose badly because they lack information, put off decisions or follow the default. Governments can respond with <b>information</b> (health warnings, labelling, campaigns) and <b>nudges</b>: changes to how a choice is presented that influence behaviour without banning anything or changing prices. Opt-out organ donation and placing fruit at eye level are nudges; a tax or a ban is not.</p>
  <ul>
    <li><b>For nudges:</b> cheap, keep freedom of choice, can work where taxes would be unpopular.</li>
    <li><b>Against:</b> the effect may be small or uncertain, may not reach the people who need it, and someone must decide what is the "right" choice.</li>
  </ul>
''' + snip('gp_other', 5)
watch = '''
  <h2>1 · Price cap on a natural monopoly</h2><p>Fixed cost $800, marginal cost $20, demand P = 100 − Q. Press Play, or click the steps.</p><div id="stN"></div>
  <h2>2 · The power of a default</h2><p>An illustrative model of opt-in against opt-out organ donation. These are not real data.</p><div id="stD2"></div>
'''
explore = '''
  <h2>Lab 1 · Set the price cap</h2>
  <p>The monopolist has MC = $20, a fixed cost of $800 and faces demand P = 100 − Q. Move the cap. Without regulation it charges $60.</p>
  <div class="card"><div class="grid2"><div><div id="g8"></div>
    <div class="readout"><div><small>Price</small><strong id="n1"></strong></div><div><small>Output</small><strong id="n2"></strong></div><div><small>Profit or loss</small><strong id="n3"></strong></div><div><small>Efficiency</small><strong id="n4"></strong></div></div>
    <div class="verdict" id="nv"></div></div>
    <div><svg id="labG" viewBox="0 0 420 300" role="img" aria-label="Natural monopoly with demand, marginal cost, average cost and a price cap showing profit or loss"></svg></div></div></div>

  <h2>Lab 2 · Defaults and donors</h2>
  <p>Choose how many people just accept the default, and how many would donate if they thought about it. These numbers are illustrative.</p>
  <div class="card"><div class="grid2"><div><div id="g9"></div><div id="g10"></div>
    <div class="readout"><div><small>Opt-in donors</small><strong id="d1"></strong></div><div><small>Opt-out donors</small><strong id="d2"></strong></div><div><small>Difference</small><strong id="d3"></strong></div></div>
    <div class="verdict" id="dv"></div></div>
    <div><svg id="labH" viewBox="0 0 420 260" role="img" aria-label="Bars comparing the share of donors under opt-in and opt-out"></svg></div></div></div>
'''
practise = '''
  <h2>1 · What type of policy?</h2><div id="cl1" class="card"></div>
  <h2>2 · For or against privatisation?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Put the price cap argument in order</h2><div id="o1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''
real = '<p class="note">Examples are explained in general terms. Check current details before quoting them in an exam answer.</p>\n' + S.b((153, 154)) + '''  <div class="rw"><h3>Competition authorities and mergers</h3><p>Competition authorities in many countries review large mergers and can block them or require firms to sell parts of the business. The aim is to stop a merger that would give the new firm power over prices.</p><div class="use"><b>Exam use:</b> competition policy. Evaluate: authorities may lack information, and a merger can bring lower costs as well as higher power.</div></div>
  <div class="rw"><h3>State-funded health care and education</h3><p>Many governments provide or fund health care and schooling because they are merit goods with external benefits, and because access based on ability to pay may be thought unfair.</p><div class="use"><b>Exam use:</b> state provision. Evaluate: efficiency, cost to taxpayers, quality and whether private providers could be better or worse.</div></div>
'''
exam = '''
  <h2>Past paper questions on regulation, provision, privatisation and nudges</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the essays on privatisation and public provision, a monopoly question, the data response parts on nudge theory, and Paper 3 multiple choice questions. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 20 marks</td><td>2</td><td>Oct/Nov 2023 (41); Oct/Nov 2024 (42)</td></tr>
    <tr><td>Essay part, 13 marks</td><td>1</td><td>Feb/March 2020 (42)</td></tr>
    <tr><td>Data response parts</td><td>4</td><td>Feb/March 2022 (42); May/June 2020 (41, 43, not sat); May/June 2021 (41, 43)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>7 shown below</td><td>2020 to 2023</td></tr>
  </table></div>
  <h2>A · 20 mark essays</h2>
''' + S.b((173, 184), (186, 189)) + '''
  <h2>B · A 13 mark question</h2>
''' + S.b((208, 216)) + '''
  <h2>C · Data response parts</h2>
''' + S.b((219, 222)) + '''
  <h2>D · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips = '''
  <h2>Top tips</h2>
  <ul class="tips">
    <li><b>Name the type of policy.</b> Regulation, ownership and provision, or information and nudges. Then link it to the failure it fits.</li>
    <li><b>For privatisation, split the industry:</b> can competition develop, or is it a natural monopoly? Mention regulators.</li>
    <li><b>For a price cap, compare the two levels.</b> At marginal cost is efficient but loss-making; at average cost keeps normal profit.</li>
    <li><b>Know what a nudge is.</b> It changes the way choices are presented (defaults, placement) and leaves people free. A tax or a ban is not a nudge.</li>
    <li><b>Use the merit good link for state provision:</b> external benefits, under-consumption, equity, and the risk of X-inefficiency.</li>
    <li><b>Test strong words:</b> "all", "always", "no limits". Weigh both sides and conclude.</li>
  </ul>
  <h2>Sentences you can use</h2>
  <div class="tw"><table class="t">
    <tr><th>You want to say</th><th>Use this sentence</th></tr>
    <tr><td>Privatisation</td><td>"A state monopoly may simply be replaced with a private monopoly, so a regulator may still be needed."</td></tr>
    <tr><td>Price cap</td><td>"A cap at marginal cost could be allocatively efficient but may leave the firm making a loss."</td></tr>
    <tr><td>Nudge</td><td>"Changing the default could raise participation while leaving people free to choose."</td></tr>
    <tr><td>Provision</td><td>"Public provision could ensure access for those unable to pay, but may be subject to X-inefficiency."</td></tr>
  </table></div>
  <h2>Command words</h2>
  <div class="tw"><table class="t">
    <tr><th>Command word</th><th>What it asks for</th></tr>
    <tr><td>Evaluate</td><td>Weigh the arguments and reach a supported conclusion.</td></tr>
    <tr><td>Consider</td><td>Look at the issue from several sides and judge how strong each is.</td></tr>
    <tr><td>Discuss</td><td>Arguments on both sides, then a judgement.</td></tr>
  </table></div>
  <h2>Flashcards</h2><div id="fc1"></div>
'''
js = HEAD + '''
/* ---------- natural monopoly: MC 20, fixed cost 800, D: P = 100 - Q ---------- */
const NX = (q) => 70 + q * 6.8, NY = (p) => 330 - p * 3, AC = (q) => 20 + 800 / q;
function nmBase(s) {
  const acPts = []; for (let q = 10; q <= 100; q += 2) acPts.push([NX(q), NY(AC(q))]);
  return axes() + SV.line(NX(0), NY(100), NX(100), NY(0), "c1", op(s.d)) + SV.line(NX(0), NY(100), NX(50), NY(0), "c3", op(s.d)) + SV.line(NX(0), NY(20), NX(100), NY(20), "c2", op(s.d)) + SV.path(ptsPath(acPts), "c4", op(s.d)) +
    SV.text(NX(100) - 4, NY(0) - 8, "D", "lbl bd t1", { "text-anchor": "end", ...op(s.d) }) + SV.text(NX(50) + 6, NY(0) - 8, "MR", "lbl bd t3", op(s.d)) + SV.text(NX(100) - 4, NY(28) - 8, "AC", "lbl bd t4", { "text-anchor": "end", ...op(s.d) }) + SV.text(NX(100) - 4, NY(20) + 18, "MC", "lbl bd t2", { "text-anchor": "end", ...op(s.d) });
}
const nmPoint = (q, p, pl, ql, o, c) => SV.line(NX(q), NY(p), NX(q), 330, "gr", op(o)) + SV.line(70, NY(p), NX(q), NY(p), "gr", op(o)) + SV.circle(NX(q), NY(p), 6, c, op(o)) + SV.text(66, NY(p) + 4, pl, "sm bd", { "text-anchor": "end", ...op(o) }) + SV.text(NX(q), 350, ql, "lbl bd", { "text-anchor": "middle", ...op(o) });
function nmDraw(s) {
  let o = nmBase(s);
  if (s.u > 0) o += SV.rect(70, NY(60), NX(40) - 70, NY(40) - NY(60), "f3", op(s.u)) + nmPoint(40, 60, "60", "40", s.u, "dot3") + SV.text(NX(20), NY(50) + 4, "profit 800", "lbl bd", { "text-anchor": "middle", ...halo, ...op(s.u) });
  if (s.c1 > 0) o += SV.rect(70, NY(30), NX(80) - 70, NY(20) - NY(30), "f2", op(s.c1)) + nmPoint(80, 20, "20", "80", s.c1, "dot2") + SV.text(NX(40), NY(25) + 4, "loss 800", "lbl bd t2", { "text-anchor": "middle", ...halo, ...op(s.c1) });
  if (s.c2 > 0) o += nmPoint(68.3, 31.7, "31.7", "68", s.c2, "dot1") + SV.text(NX(34), NY(31.7) - 10, "cap = AC: normal profit", "lbl bd t1", { "text-anchor": "middle", ...halo, ...op(s.c2) });
  return o;
}
Lib.stepper($("#stN"), { w: 780, h: 370, label: "A natural monopoly with a price cap at marginal cost and at average cost", base: { d: 0, u: 0, c1: 0, c2: 0 }, draw: nmDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>A natural monopoly.</b> A big fixed cost ($800) means average cost (AC) keeps falling as output rises, so one firm is cheapest. Marginal cost (MC) is $20 and demand is P = 100 − Q.", s: { d: 1 } },
  { cap: "<b>Left alone.</b> The monopolist produces where MR = MC: <b>40 units at $60</b>, above average cost of $40. The shaded box is a supernormal profit of $20 × 40 = <b>$800</b>. Price is well above marginal cost, so output is too low.", s: { d: 1, u: 1 } },
  { cap: "<b>Cap at marginal cost ($20).</b> Output rises to <b>80</b> and price equals MC: allocative efficiency. But AC at 80 is $30, so the firm loses $10 a unit, <b>$800</b> in all. It may need a subsidy or leave.", s: { d: 1, c1: 1 } },
  { cap: "<b>Cap at average cost ($31.70).</b> Where D meets AC output is about <b>68</b>. The firm earns only normal profit, so it stays in business, and consumers get more output at a lower price. Regulators rarely know the true AC curve, though.", s: { d: 1, c2: 1 } },
] });

/* ---------- default effect ---------- */
function defDraw(s) {
  let o = SV.line(60, 250, 740, 250) + SV.text(62, 24, "Share of people who are donors", "sm");
  const H = (v) => 2.2 * v;
  if (s.a > 0) o += SV.rect(180, 250 - H(30) * s.a, 130, H(30) * s.a, "f2", op(s.a)) + SV.text(245, 250 - H(30) * s.a - 8, "30%", "lbl bd", { "text-anchor": "middle", ...op(s.a) });
  if (s.b > 0) o += SV.rect(440, 250 - H(80) * s.b, 130, H(80) * s.b, "f3", op(s.b)) + SV.text(505, 250 - H(80) * s.b - 8, "80%", "lbl bd", { "text-anchor": "middle", ...op(s.b) });
  o += SV.text(245, 274, "Opt-in", "lbl bd", { "text-anchor": "middle", ...op(s.a) }) + SV.text(505, 274, "Opt-out", "lbl bd", { "text-anchor": "middle", ...op(s.b) });
  return o;
}
Lib.stepper($("#stD2"), { w: 780, h: 300, label: "Share of donors under opt-in and opt-out systems in an illustrative model", base: { a: 0, b: 0 }, draw: defDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The set-up.</b> Suppose 60% of people would donate if they made an active choice, and half of all people simply accept whatever the default is. (Illustrative numbers.)", s: { a: 0, b: 0 } },
  { cap: "<b>Opt-in.</b> The default is not to donate. Only those who actively choose and want to donate sign up: 50% × 60% = <b>30%</b>.", s: { a: 1, b: 0 } },
  { cap: "<b>Opt-out.</b> The default is to donate. The 50% who accept the default are donors, and half of the active choosers (60% of 50% = 30%) also donate: <b>80%</b>.", s: { a: 1, b: 1 } },
  { cap: "<b>Same freedom, different outcome.</b> Everyone can still choose, nothing is banned and no price changes, but the default moves the donor rate by 50 percentage points. That is what a <b>nudge</b> does.", s: { a: 1, b: 1 } },
] });

/* ---------- Lab 1: price cap ---------- */
function labN() {
  if (!$("#cap")) return;
  const c = +$("#cap").value, free = c >= 60, p = free ? 60 : c, q = free ? 40 : 100 - c, prof = (p - 20) * q - 800;
  $("#n1").textContent = "$" + p; $("#n2").textContent = q; $("#n3").textContent = (prof >= 0 ? "$" : "−$") + Math.abs(Math.round(prof)); $("#n4").textContent = p === 20 ? "Allocative" : "Not allocative";
  $("#nv").textContent = free ? "The cap is at or above the price the monopolist would charge ($60), so it is not binding: output stays at 40 and profit at $800."
    : c === 20 ? "Price equals marginal cost: output is at the allocatively efficient level of 80. But average cost is $30, so the firm loses $800 and may need a subsidy."
    : prof >= 0 ? `Price falls to $${c} and output rises to ${q}. The firm still earns a profit of $${Math.round(prof)}, so it stays in business, and consumers gain. A lower cap would give them more.`
    : `At $${c} the price is below average cost ($${Lib.fmtN(AC(q), 1)}), so the firm loses $${Math.abs(Math.round(prof))}. In the long run it may leave or need a subsidy. Output is higher, but the service may not be sustainable.`;
  const x = (v) => 40 + v * 3.6, y = (v) => 270 - v * 2.4, acp = []; for (let k = 10; k <= 100; k += 2) acp.push([x(k), y(AC(k))]);
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "Price ($)", "sm");
  o += SV.rect(40, Math.min(y(p), y(AC(q))), x(q) - 40, Math.abs(y(p) - y(AC(q))), prof >= 0 ? "f3" : "f2");
  o += SV.line(x(0), y(100), x(100), y(0), "c1") + SV.line(x(0), y(20), x(100), y(20), "c2") + SV.path(ptsPath(acp), "c4") + SV.line(40, y(p), 400, y(p), free ? "gr" : "c3", { "stroke-width": 3 }) + SV.circle(x(q), y(p), 6, "dot1") + SV.text(x(100) - 4, y(0) - 6, "D", "sm bd t1", { "text-anchor": "end" }) + SV.text(x(100) - 4, y(20) + 16, "MC", "sm bd t2", { "text-anchor": "end" }) + SV.text(x(100) - 4, y(28) - 6, "AC", "sm bd t4", { "text-anchor": "end" });
  $("#labG").innerHTML = o;
}
Lib.slider($("#g8"), { id: "cap", label: "Price cap ($): ", min: 20, max: 70, step: 1, value: 40, fmt: (v) => v, onInput: labN });

/* ---------- Lab 2: defaults ---------- */
function labD() {
  if (!$("#inr") || !$("#sup")) return;
  const f = +$("#inr").value / 100, t = +$("#sup").value / 100, a = (1 - f) * t * 100, b = (f + (1 - f) * t) * 100;
  $("#d1").textContent = Math.round(a) + "%"; $("#d2").textContent = Math.round(b) + "%"; $("#d3").textContent = "+" + Math.round(b - a) + " points";
  $("#dv").textContent = f === 0 ? "If nobody follows the default, the system makes no difference: both give the same donor rate."
    : `With ${Math.round(f * 100)}% accepting the default and ${Math.round(t * 100)}% in favour, opt-in gives ${Math.round(a)}% donors and opt-out ${Math.round(b)}%. The more people go along with defaults, the bigger the effect of the nudge.`;
  const H = (v) => 1.8 * v;
  let o = SV.line(30, 220, 400, 220);
  [[70, a, "f2", "Opt-in"], [240, b, "f3", "Opt-out"]].forEach(([x, v, c, l]) => { o += SV.rect(x, 220 - H(v), 100, H(v), c) + SV.text(x + 50, 220 - H(v) - 8, Math.round(v) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 240, l, "sm", { "text-anchor": "middle" }); });
  $("#labH").innerHTML = o;
}
Lib.slider($("#g9"), { id: "inr", label: "People who just accept the default: ", min: 0, max: 80, step: 10, value: 50, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g10"), { id: "sup", label: "People who would donate if they chose: ", min: 40, max: 80, step: 10, value: 60, fmt: (v) => v + "%", onInput: labD });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "What type of policy is each one?",
  buckets: [{ label: "Regulation and legal limits" }, { label: "Provision and ownership" }, { label: "Information and nudges" }],
  items: [
    { text: "A ban on new petrol cars", b: 0 }, { text: "Emission standards for factories", b: 0 }, { text: "Competition law blocking a merger", b: 0 }, { text: "A price cap on a water company", b: 0 },
    { text: "Free vaccination provided by the state", b: 1 }, { text: "Nationalising the railways", b: 1 }, { text: "Selling a state-owned airline", b: 1 }, { text: "Street lighting provided by the council", b: 1 },
    { text: "Opt-out organ donation", b: 2 }, { text: "Health warnings on cigarette packs", b: 2 }, { text: "Fruit placed at eye level in canteens", b: 2 },
  ], done: "A nudge changes how choices are presented without forcing them; a ban is regulation and a tax is a price tool.",
});
Lib.classify($("#cl2"), {
  prompt: "Is each point an argument for or against privatisation?",
  buckets: [{ label: "For privatisation" }, { label: "Against privatisation" }],
  items: [
    { text: "Competition may cut costs and prices", b: 0 }, { text: "Shareholders scrutinise managers", b: 0 }, { text: "Access to private funds for investment", b: 0 }, { text: "The government stops funding losses and receives sale proceeds", b: 0 },
    { text: "A state monopoly may become a private monopoly", b: 1 }, { text: "Unprofitable but socially valuable services may be cut", b: 1 }, { text: "Natural monopolies cannot easily be made competitive", b: 1 }, { text: "A regulator will still be needed", b: 1 },
  ], done: "Weigh these by asking whether the industry can really become competitive.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Natural monopoly", "An industry where one firm is cheapest because of very high fixed costs"],
  ["Price cap", "A limit on the price a regulated firm may charge"],
  ["Privatisation", "Selling state-owned firms to the private sector"],
  ["Nationalisation", "Taking private firms into state ownership"],
  ["Nudge", "A change in how choices are presented that influences behaviour without forcing it"],
  ["Regulatory capture", "When the regulator ends up serving the firms it regulates"],
  ["X-inefficiency", "Costs higher than necessary because of weak pressure to cut them"],
  ["Competition policy", "Laws on mergers and cartels to protect competition"],
], done: "Eight words for regulation, ownership and nudges." });
Lib.order($("#o1"), { prompt: "Put the explanation of price cap regulation of a natural monopoly in order.", items: [
  "A natural monopoly has high fixed costs, so one firm is cheapest",
  "Unregulated, it sets MR = MC, so price is high and output is low",
  "The regulator sets a maximum price below the monopoly price",
  "Output rises and price falls, moving towards allocative efficiency",
  "A cap at marginal cost may leave the firm making a loss; a cap at average cost allows normal profit",
  "Evaluate: the regulator may lack information about costs, and may be influenced by the firm",
], done: "A reliable structure for regulation of monopoly." });
Lib.calc($("#c1"), { qs: [
  { q: "A natural monopoly has MC = $20, a fixed cost of $800 and faces P = 100 − Q. It sets MR = MC, where MR = 100 − 2Q. What quantity does it produce?", a: 40, sol: "100 − 2Q = 20 gives Q = <b>40</b>, and P = $60." },
  { q: "What is its profit ($)?", a: 800, hint: "(P − MC) x Q − fixed cost.", sol: "(60 − 20) x 40 − 800 = <b>$800</b>." },
  { q: "A regulator caps the price at $20. What quantity is demanded?", a: 80, sol: "100 − 20 = <b>80</b>." },
  { q: "What is the firm's profit or loss at the $20 cap ($; use a negative for a loss)?", a: -800, sol: "(20 − 20) x 80 − 800 = <b>−$800</b>." },
  { q: "The cap is set at $36. What is the profit ($)?", a: 224, hint: "Q = 100 − 36 = 64.", sol: "(36 − 20) x 64 − 800 = 1024 − 800 = <b>$224</b>." },
  { q: "In an organ donation model 50% accept the default and 60% of the others would donate. What share are donors under opt-in (%)?", a: 30, sol: "50% x 60% = <b>30%</b>." },
  { q: "What share are donors under opt-out (%)?", a: 80, sol: "50% + 30% = <b>80%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is an example of a nudge?", opts: ["A tax on sugary drinks", "A ban on smoking indoors", "An opt-out organ donation system", "A subsidy for fruit"], a: 2, why: "Changing the default influences choice without forcing it." },
  { q: "Privatising a natural monopoly may lead to:", opts: ["perfect competition at once", "a private monopoly that needs regulation", "no change in ownership", "zero profit"], a: 1, why: "Competition is unrealistic on a network, so a regulator is usually needed." },
  { q: "A price cap on a natural monopoly set at marginal cost is likely to:", opts: ["be allocatively efficient but cause a loss", "raise the price", "reduce output", "give supernormal profit"], a: 0, why: "P = MC is efficient, but average cost is above marginal cost, so the firm loses money." },
  { q: "X-inefficiency means:", opts: ["costs are higher than necessary", "output is too high", "prices are below cost", "there is perfect competition"], a: 0, why: "Weak pressure to control costs lets average cost rise above the minimum possible." },
  { q: "Public goods are best provided by the state because:", opts: ["firms can easily charge for them", "free riders make private supply unprofitable", "demand is always elastic", "they have no external benefits"], a: 1, why: "Non-excludability means people can use them without paying." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Production quota", "A legal limit on the quantity produced or sold; supply is fixed at the quota."],
  ["Prohibition", "An outright ban on producing, selling or using a good."],
  ["Licence", "Permission needed to produce or sell; the number of licences may be limited."],
  ["Deregulation", "Removing rules that restrict entry or competition, to encourage new firms."],
  ["Property rights", "Legal ownership or use of an asset, letting owners stop others imposing costs or charge them."],
  ["Regulation", "Legal rules such as bans, standards, price caps and competition law."],
  ["Competition policy", "Laws on mergers and cartels to protect competition."],
  ["Natural monopoly", "A market where one firm is cheapest because of very high fixed costs."],
  ["Price cap", "A maximum price set by a regulator for a monopoly."],
  ["State provision", "The government supplies the good, funded from taxation."],
  ["Nationalisation", "Taking private firms into state ownership."],
  ["Privatisation", "Selling state-owned firms to the private sector."],
  ["X-inefficiency", "Costs higher than necessary through lack of competitive pressure."],
  ["Nudge", "A change in the presentation of choices that influences behaviour without forcing it."],
  ["Regulatory capture", "When regulators serve the interests of the firms they regulate."],
  ["Cross-subsidisation", "Charging high prices to some consumers to fund low prices for others."],
] });
''' + MCQ([209, 210, 211, 212, 213, 214, 219])
write("gp3", page(EY.format(3), "Regulation, Public Provision, Privatisation and Nudges",
  "The legal and ownership tools: regulation and competition policy, price caps on natural monopolies, state provision, nationalisation and privatisation, and information and nudges. Animated diagrams built from numbers, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Regulation, Public Provision, Privatisation and Nudges", "regulation-provision-privatisation")


EXTRA_ROWS = """    <tr><td><b>Production quota</b></td><td>Legal limit on quantity produced or sold, so supply is fixed.</td><td>Over-production, demerit goods, over-use of resources</td><td>Black markets, windfall profits from the higher price, hard to share fairly</td></tr>
    <tr><td><b>Prohibition and licences</b></td><td>A ban, or permission needed to produce or sell.</td><td>Serious harm (ban); demerit goods and information failure (licences)</td><td>Enforcement cost, black markets, loss of choice; limited licences can protect incumbents</td></tr>
    <tr><td><b>Deregulation</b></td><td>Removes rules that restrict entry or competition.</td><td>Monopoly power created by barriers to entry</td><td>Lower standards, exploitation where information is poor; only works if firms enter</td></tr>
    <tr><td><b>Property rights</b></td><td>Assigns ownership so owners can stop or charge those who impose costs, or keep benefits (patents).</td><td>Externalities with identifiable parties</td><td>Cannot cover air or the sea; bargaining costs and unequal power</td></tr>
"""
# ---- 38.4 government failure and choosing the right policy
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Intervention is justified when a market fails, but <b>government failure</b> occurs when intervention leaves resources allocated no better, or worse. It has several causes: poor information, time lags, unintended consequences, the cost of administration and enforcement, and political pressure. Choosing the right tool means matching it to the type of failure and its cause and then weighing it against these risks. The final judgement compares the size of the market failure with the likely success and cost of the policy.</p></div>
''' + S.b((67, 76)).replace('6 · Government failure', '1 · Sources of government failure') + '''
''' + snip('gp_match', 2) + '''
  <h2>3 · The toolkit: every tool on the syllabus list</h2>
''' + S.b((26, 37)).replace('  </table></div>', EXTRA_ROWS + '  </table></div>') + '''
  <h2>4 · Free market or intervention?</h2>
  <div class="grid2">
    <div class="card"><h3>The case for the free market</h3><p>Prices carry information, so resources may flow to their most valued uses without anyone planning it. Profit gives firms an incentive to be efficient and to innovate, and consumers have choice. Intervention costs money and can be captured by special interests.</p></div>
    <div class="card"><h3>The case for intervention</h3><p>Markets may ignore external costs and benefits, under-supply public goods, leave monopolies unchecked, suffer from poor information and produce an unequal distribution of income. In each case government action may raise welfare.</p></div>
  </div>
  <p>Almost every economy is <b>mixed</b>: the question is how much intervention, and of what kind. Good answers avoid "the market always works" and "the government always helps".</p>

  <h2>5 · A checklist for evaluating a policy</h2>
  <ul>
    <li><b>Effectiveness:</b> does it deal with the cause of the failure, and by how much?</li>
    <li><b>Cost:</b> to the government (taxes, administration) and to those affected.</li>
    <li><b>Side effects:</b> black markets, avoidance, new distortions.</li>
    <li><b>Fairness:</b> who gains and loses, and is it regressive?</li>
    <li><b>Time:</b> how long before it works, and does the effect last?</li>
    <li><b>Information:</b> does the government know enough to set the right level?</li>
    <li><b>Alternatives:</b> would another tool do the job at lower cost?</li>
  </ul>
'''
watch = '''
  <h2>1 · Setting the tax at the wrong level</h2>
  <p>Demand is P = 100 − Q, private marginal cost is P = 20 + 0.5Q and there is an external cost of $15 a unit that the government cannot measure exactly. Press Play, or click the steps.</p><div id="stG"></div>
'''
explore = S.b((117, 122)).replace('Lab 4 · Getting', 'Lab 1 · Getting') + '''
  <h2>Lab 2 · Is the policy worth it?</h2>
  <p>A policy removes some of a market failure but costs money to run. Set the size of the failure, the share the policy removes and its cost, and see whether society gains.</p>
  <div class="card"><div class="grid2"><div><div id="g11"></div><div id="g12"></div><div id="g13"></div>
    <div class="readout"><div><small>Welfare loss removed</small><strong id="w1"></strong></div><div><small>Cost of the policy</small><strong id="w2"></strong></div><div><small>Net gain</small><strong id="w3"></strong></div></div>
    <div class="verdict" id="wv"></div></div>
    <div><svg id="labI" viewBox="0 0 420 260" role="img" aria-label="Bars comparing the welfare loss removed with the cost of the policy"></svg></div></div></div>
'''
practise = '''
  <h2>1 · What kind of government failure?</h2><div id="cl1" class="card"></div>
''' + S.b((130, 131)).replace('2 · Which', '2 · Which') + '''
  <h2>3 · Name the failure from the scenario</h2><div id="cl3" class="card"></div>
  <h2>4 · Best policy, and the one that does not fit</h2><div id="qz3"></div>
  <h2>5 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>6 · Put the evaluation of a policy in order</h2><div id="o1" class="card"></div>
  <h2>7 · Calculations</h2><div id="c1"></div>
  <h2>8 · Multiple choice</h2><div id="qz1"></div>
'''
real = '<p class="note">Examples are explained in general terms. Check current details before quoting them in an exam answer.</p>\n' + '''  <div class="rw"><h3>Sugar taxes and reformulation</h3><p>Several countries have taxed soft drinks by sugar content. Some manufacturers cut the sugar in their drinks to avoid the tax, so revenue was lower than forecast and consumption of sugar fell, though the government raised less money than it expected.</p><div class="use"><b>Exam use:</b> a policy that works better than expected on the aim but worse on revenue. Forecasting is hard, which is one cause of government failure.</div></div>
  <div class="rw"><h3>Food subsidies and land clearance</h3><p>Subsidies to grow fresh fruit and vegetables can encourage farmers to clear land. The merit good is encouraged, but habitats may be lost, an unintended external cost.</p><div class="use"><b>Exam use:</b> an unintended consequence. A Paper 3 question asked which result of such a subsidy would be a government failure: the loss of wildlife.</div></div>
  <div class="rw"><h3>Fuel subsidies</h3><p>Some governments hold fuel prices low with subsidies. They can help poorer households but are often used mostly by richer households with more vehicles, they cost a lot, and they encourage use of fossil fuels.</p><div class="use"><b>Exam use:</b> poor targeting and high cost as sources of government failure.</div></div>
''' + S.b((150, 150))
exam = '''
  <h2>Past paper questions on intervention and government failure</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the essays asking whether the free market or government intervention is better, a practice question with a model answer, and Paper 3 multiple choice questions on government failure and policy. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 20 marks</td><td>1</td><td>May/June 2025 (44)</td></tr>
    <tr><td>Essay, 25 marks</td><td>2</td><td>May/June 2020 (42, not sat); May/June 2021 (41, 43)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>6 shown below</td><td>2022 to 2025</td></tr>
  </table></div>
''' + snip('gp_stems') + '''
  <h2>A · 20 and 25 mark essays</h2>
''' + S.b((191, 205)) + '''
  <h2>B · Practice question with a model answer</h2>
  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">12 marks</span> Evaluate the view that government intervention in markets always makes society better off.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>Say when intervention helps (market failure) and give one example with a diagram or numbers. Then give causes of government failure and an example. Conclude with a judgement on "always".</div>
''' + key() + '''
    <div class="ans">
    <p><span class="mk k" data-t="K">Government intervention means actions such as taxes, subsidies, regulation and provision that aim to correct market failure and raise society's welfare.</span></p>
    <p><span class="mk n" data-t="N">Intervention could make society better off where the market fails. If a firm ignores an external cost, such as pollution, output is above the social optimum; a tax equal to the external cost could raise the firm's costs by that amount and move output towards the optimum, removing a welfare loss.</span> <span class="mk a" data-t="A">Similarly, state provision of street lighting could supply a public good that private firms would not.</span></p>
    <p><span class="mk e" data-t="E">However, intervention may not always help. The government may lack the information to set the tax at the right level: a tax well above the external cost could cut output too far and cause a welfare loss as big as no tax at all. Policies may also have time lags, administration costs and unintended effects, such as a rubbish tax leading to fly-tipping.</span> <span class="mk e" data-t="E">Overall, intervention is likely to improve welfare when the failure is large and the government is well informed, but it is unlikely to do so in every case, so the claim that it always makes society better off is too strong.</span></p></div>
  </div></details>
  <h2>C · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips = '''
  <h2>Top tips</h2>
  <ul class="tips">
    <li><b>Always include government failure</b> in evaluation: poor information, time lags, unintended effects, cost, lobbying.</li>
    <li><b>Give a specific cause, then a specific example.</b> "Poor information, so the tax may be set too high" beats "the government may fail".</li>
    <li><b>Compare the size of the market failure with the risk of government failure</b> in your conclusion.</li>
    <li><b>Test strong words:</b> "always", "all", "neither possible nor desirable". Weigh both sides and conclude.</li>
    <li><b>Name the failure before the policy.</b> Production or consumption, over- or under-provided, then the tool (see the table in the Learn tab). A policy that does not fit the failure scores little.</li>
    <li><b>Match tool to failure</b> before evaluating: negative externality (tax, permits, regulation), positive externality or merit good (subsidy, provision), public good (provision), monopoly (regulation), information failure (labels, nudges).</li>
    <li><b>Mention mixed economies.</b> Real economies use markets and government together.</li>
  </ul>
  <h2>Sentences you can use</h2>
  <div class="tw"><table class="t">
    <tr><th>You want to say</th><th>Use this sentence</th></tr>
    <tr><td>Information</td><td>"However, intervention may fail if the government lacks the information needed to set the right level of tax."</td></tr>
    <tr><td>Time lag</td><td>"There could be a time lag between spotting the problem and the policy taking effect, by which time conditions may have changed."</td></tr>
    <tr><td>Unintended</td><td>"The policy might create new problems, such as black markets or avoidance."</td></tr>
    <tr><td>Conclusion</td><td>"Intervention is likely to help where the market failure is large and the policy is well targeted, but it is unlikely to help in every case."</td></tr>
  </table></div>
  <h2>Command words</h2>
  <div class="tw"><table class="t">
    <tr><th>Command word</th><th>What it asks for</th></tr>
    <tr><td>Evaluate</td><td>Weigh the arguments and reach a supported conclusion.</td></tr>
    <tr><td>Assess</td><td>Judge how important or effective something is, with reasons.</td></tr>
    <tr><td>Discuss</td><td>Arguments on both sides, then a judgement.</td></tr>
  </table></div>
  <h2>Flashcards</h2><div id="fc1"></div>
'''
js = HEAD + '''
/* ---------- wrong tax (Watch) : D = 100 - Q, MPC = 20 + 0.5Q, external cost 15 ---------- */
const GX = (q) => 70 + q * 7, GY = (p) => 330 - p * 3;
function wrongDraw(s) {
  let o = axes() + SV.line(GX(0), GY(100), GX(88), GY(12), "c1", op(s.d)) + SV.line(GX(0), GY(20), GX(88), GY(64), "c2", op(s.d)) +
    SV.text(GX(88) + 6, GY(12) + 4, "D = MSB", "lbl bd t1", op(s.d)) + SV.text(GX(88) + 6, GY(64) + 4, "S = MPC", "lbl bd t2", op(s.d));
  if (s.eq > 0) o += SV.line(GX(53.3), GY(46.7), GX(53.3), 330, "gr", op(s.eq)) + SV.line(70, GY(46.7), GX(53.3), GY(46.7), "gr", op(s.eq)) + SV.circle(GX(53.3), GY(46.7), 6, "dot3", op(s.eq)) + SV.text(GX(53.3), 350, "53", "lbl bd", { "text-anchor": "middle", ...op(s.eq) });
  if (s.msc > 0) o += SV.line(GX(0), GY(35), GX(88), GY(79), "c3", { "stroke-width": 2.5, ...op(s.msc) }) + SV.text(GX(88) + 6, GY(79) + 4, "MSC", "lbl bd t3", op(s.msc)) +
    SV.line(GX(43.3), GY(56.7), GX(43.3), 330, "gr", op(s.msc)) + SV.circle(GX(43.3), GY(56.7), 6, "dot1", op(s.msc)) + SV.text(GX(43.3), 350, "43", "lbl bd", { "text-anchor": "middle", ...op(s.msc) });
  if (s.l1 > 0) o += SV.poly([[GX(43.3), GY(56.7)], [GX(53.3), GY(46.7)], [GX(53.3), GY(61.7)]], "f2", op(s.l1)) + SV.text(GX(53.3) + 12, GY(46.7) + 16, "welfare loss 75", "lbl bd t2", { ...halo, ...op(s.l1) });
  if (s.t30 > 0) o += SV.line(GX(0), GY(50), GX(88), GY(94), "c4", { "stroke-dasharray": "6 5", ...op(s.t30) }) + SV.text(GX(88) + 6, GY(94) + 4, "S + tax $30", "lbl bd t4", op(s.t30)) + SV.line(GX(33.3), GY(66.7), GX(33.3), 330, "gr", op(s.t30)) + SV.circle(GX(33.3), GY(66.7), 6, "dot4", op(s.t30)) + SV.text(GX(33.3), 350, "33", "lbl bd", { "text-anchor": "middle", ...op(s.t30) });
  if (s.l2 > 0) o += SV.poly([[GX(33.3), GY(51.7)], [GX(33.3), GY(66.7)], [GX(43.3), GY(56.7)]], "f2", op(s.l2)) + SV.text(GX(33.3) - 10, GY(51.7) + 22, "loss 75", "lbl bd t2", { "text-anchor": "end", ...halo, ...op(s.l2) });
  return o;
}
Lib.stepper($("#stG"), { w: 780, h: 370, label: "A tax set too low, correctly and too high compared with the external cost", base: { d: 0, eq: 0, msc: 0, l1: 0, t30: 0, l2: 0 }, draw: wrongDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The free market</b> ignores the external cost. Demand meets private marginal cost at <b>53 units</b> and $46.67.", s: { d: 1, eq: 1 } },
  { cap: "<b>The social optimum.</b> Adding the external cost of $15 gives marginal social cost (MSC). It meets demand at <b>43 units</b>. The market overproduces by 10 units, and the triangle is a <b>welfare loss of 75</b>.", s: { d: 1, eq: 1, msc: 1, l1: 1 } },
  { cap: "<b>The right tax.</b> A tax of exactly $15 shifts supply up to the MSC curve. Output falls to 43 and the welfare loss is removed. This needs the government to know the external cost exactly.", s: { d: 1, eq: 0.4, msc: 1, l1: 0.2 } },
  { cap: "<b>A tax set too high.</b> Suppose the government overestimates the external cost and taxes at $30. Output falls to <b>33</b>, below the optimum, and there is a new welfare loss, again <b>75</b>.", s: { d: 1, eq: 0.4, msc: 1, l1: 0, t30: 1, l2: 1 } },
  { cap: "<b>Government failure.</b> The over-tax leaves society no better off than doing nothing, because of poor information. A tax between about $0 and $30 would reduce the loss; one above $30 is worse than no tax.", s: { d: 1, eq: 0.4, msc: 1, l1: 0, t30: 1, l2: 1 } },
] });
''' + S.j_((114, 130)).replace('"f2"', '"f2"') + '''
/* ---------- Lab 2: is it worth it ---------- */
function labW() {
  if (!$("#wl") || !$("#ws") || !$("#wc")) return;
  const L = +$("#wl").value, sh = +$("#ws").value / 100, c = +$("#wc").value, rem = L * sh, net = rem - c;
  $("#w1").textContent = Math.round(rem); $("#w2").textContent = c; $("#w3").textContent = (net >= 0 ? "+" : "−") + Math.abs(Math.round(net));
  $("#wv").textContent = net > 0.5 ? `The policy removes ${Math.round(rem)} of welfare loss and costs ${c}, so society gains ${Math.round(net)}. Intervention is justified here.`
    : net < -0.5 ? `The policy removes ${Math.round(rem)} but costs ${c}: society loses ${Math.abs(Math.round(net))}. This is government failure, even though the market failure is real.`
    : "The benefit equals the cost: the policy is not clearly worthwhile.";
  const H = (v) => 150 * (v / 250);
  let o = SV.line(30, 200, 400, 200);
  [[60, rem, "f3", "Loss removed"], [210, c, net >= 0 ? "f4" : "f2", "Cost of policy"]].forEach(([x, v, col, l]) => { o += SV.rect(x, 200 - H(v), 100, H(v), col) + SV.text(x + 50, 200 - H(v) - 8, Math.round(v), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 220, l, "sm", { "text-anchor": "middle" }); });
  $("#labI").innerHTML = o;
}
Lib.slider($("#g11"), { id: "wl", label: "Size of the market failure (welfare loss): ", min: 0, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labW });
Lib.slider($("#g12"), { id: "ws", label: "Share the policy removes: ", min: 0, max: 100, step: 10, value: 60, fmt: (v) => v + "%", onInput: labW });
Lib.slider($("#g13"), { id: "wc", label: "Cost of running the policy: ", min: 0, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labW });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Which cause of government failure does each example show?",
  buckets: [{ label: "Poor information" }, { label: "Time lags" }, { label: "Unintended consequences" }, { label: "Cost of administration" }, { label: "Political pressure" }],
  items: [
    { text: "The external cost cannot be measured, so the tax is set wrongly", b: 0 }, { text: "The government does not know firms' true costs when setting a price cap", b: 0 },
    { text: "Years pass between spotting a problem and the law taking effect", b: 1 }, { text: "A policy fits last year's conditions, not this year's", b: 1 },
    { text: "A tax on rubbish leads to fly-tipping", b: 2 }, { text: "Subsidised fuel is mostly used by richer households", b: 2 },
    { text: "Inspectors are needed to check every factory", b: 3 }, { text: "Running a permit market needs monitoring staff", b: 3 },
    { text: "Firms lobby for weaker standards", b: 4 }, { text: "A policy is chosen for votes, not efficiency", b: 4 },
  ], done: "Name the cause, then give an example from the question.",
});
''' + S.j_((143, 153)) + '''
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Government failure", "Intervention that leaves resources less efficiently used"],
  ["Market failure", "When the market leaves resources allocated inefficiently"],
  ["Time lag", "Delay between a problem arising and a policy taking effect"],
  ["Unintended consequence", "A side effect that the policy-maker did not plan for"],
  ["Regulatory capture", "When the regulator ends up serving the firms it regulates"],
  ["Mixed economy", "An economy with both market forces and government intervention"],
  ["Regressive", "Takes a larger share of income from low earners"],
], done: "Seven words for evaluating policy." });
Lib.order($("#o1"), { prompt: "Put the evaluation of a policy in order.", items: [
  "Identify the market failure and the policy aimed at it",
  "Explain how the policy should work and what it changes",
  "Consider how well it fits the cause and how large the effect is",
  "Weigh the costs: administration, side effects, who pays",
  "Consider information, time lags and alternatives",
  "Reach a judgement comparing market failure with government failure",
], done: "A reliable structure for policy evaluation." });
Lib.calc($("#c1"), { qs: [
  { q: "Demand is P = 100 − Q and private marginal cost is P = 20 + 0.5Q. What output does the free market produce (units, 1 decimal place)?", a: 53.3, tol: 0.1, sol: "100 − Q = 20 + 0.5Q gives 1.5Q = 80, Q = <b>53.3</b>." },
  { q: "The external cost is $15, so MSC = 35 + 0.5Q. What is the socially optimal output (units, 1 decimal place)?", a: 43.3, tol: 0.1, sol: "100 − Q = 35 + 0.5Q gives 1.5Q = 65, Q = <b>43.3</b>." },
  { q: "The welfare loss from the free market is a triangle with base 10 (53.3 − 43.3) and height 15. What is its area?", a: 75, sol: "0.5 x 10 x 15 = <b>75</b>." },
  { q: "The government wrongly sets a tax of $30. What is the output after the tax (units, 1 decimal place)?", a: 33.3, tol: 0.1, sol: "100 − Q = 50 + 0.5Q gives Q = <b>33.3</b>." },
  { q: "What is the new welfare loss (a triangle with base 10 and height 15)?", a: 75, sol: "0.5 x 10 x 15 = <b>75</b>, no better than doing nothing." },
  { q: "A policy removes 60% of a welfare loss of 150 and costs 100 to run. What is the net gain (negative if a loss)?", a: -10, sol: "0.6 x 150 = 90; 90 − 100 = <b>−10</b>: government failure." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a cause of government failure?", opts: ["Perfect information", "Time lags between a problem and a policy's effect", "An externality", "Public goods"], a: 1, why: "Delays can mean the policy fits conditions that have already changed. Externalities and public goods are market failures." },
  { q: "A tax set above the external cost will most likely:", opts: ["raise output above the optimum", "cut output below the optimum", "leave output unchanged", "remove all external costs"], a: 1, why: "It overcorrects, so output falls below the social optimum." },
  { q: "Regulatory capture means:", opts: ["firms capture more of the market", "regulators serve the interests of the firms they regulate", "regulators close firms down", "the government buys a firm"], a: 1, why: "The regulator's decisions favour the industry rather than the public." },
  { q: "Which is a reason to prefer a nudge to a tax?", opts: ["It always works better", "It keeps people free to choose and may cost less", "It raises revenue", "It changes the price"], a: 1, why: "Nudges leave choice intact and are often cheap, though the effect can be uncertain." },
  { q: "An economy that uses both markets and government intervention is:", opts: ["a free market economy", "a command economy", "a mixed economy", "a subsistence economy"], a: 2, why: "Almost all real economies are mixed." },
] });
Lib.classify($("#cl3"), {
  prompt: "Which market failure does each situation show?",
  buckets: [{ label: "Negative externality" }, { label: "Positive externality / merit good" }, { label: "Public good" }, { label: "Monopoly power" }, { label: "Information failure" }],
  items: [
    { text: "A chemical plant dumps waste into a river that a fishing community uses", b: 0 }, { text: "Traffic fumes raise asthma rates for people who never drive", b: 0 },
    { text: "Many parents under-value vaccination, so uptake is low and diseases spread", b: 1 }, { text: "A firm's research produces knowledge that rivals can copy for free", b: 1 },
    { text: "A flood barrier protects a whole town, and nobody can be excluded from its benefit", b: 2 }, { text: "Street lighting that private firms have no way of charging for", b: 2 },
    { text: "One firm supplies all the water pipes in a region and sets a high price", b: 3 }, { text: "Two firms hold 95% of the market and block new entrants", b: 3 },
    { text: "Buyers cannot tell whether a used product is safe", b: 4 }, { text: "Patients cannot judge whether a treatment is needed", b: 4 },
  ], done: "Name the failure first. The policy follows from it.",
});
Lib.quiz($("#qz3"), { qs: [
  { q: "A city wants to cut congestion caused by private cars. Which policy fits the failure best?", opts: ["A subsidy on petrol", "A congestion charge and better public transport", "A maximum price for parking", "Information only"], a: 1, why: "Congestion is a negative externality of consumption. A charge raises the private cost towards the social cost, and public transport offers an alternative. A subsidy or a low price for parking would increase car use." },
  { q: "Which policy is the poorest fit for the failure named?", opts: ["Direct provision of a flood barrier (public good)", "A subsidy to cut the price of vaccination (positive externality)", "A subsidy for coal power (negative externality)", "A price cap on a water monopoly"], a: 2, why: "A subsidy increases output of a good that already has too much, so it moves the market away from the social optimum." },
  { q: "Why might a government use a specific tax instead of an ad valorem tax on petrol?", opts: ["The harm depends on litres burned, not on the price", "It is always higher", "It shifts the supply curve less", "It cannot be avoided"], a: 0, why: "Emissions are the same for each litre whatever it costs, so a fixed amount per unit lines up with the external cost." },
  { q: "A government wants to reduce consumption of a demerit good by encouraging better choices without limiting freedom. Which tool is that?", opts: ["Prohibition", "Production quota", "A nudge", "A licence"], a: 2, why: "Nudges change how choices are presented and leave people free to choose. The other three are legal limits." },
  { q: "For which failure is deregulation most relevant?", opts: ["A public good", "A negative production externality", "Monopoly power created by barriers to entry", "A merit good"], a: 2, why: "Removing rules that restrict entry lets new firms compete with the incumbent." },
  { q: "Which is a weakness of using property rights to correct an externality?", opts: ["They cost the government a lot in subsidies", "Nobody can own the air or the sea, and many people may be affected", "They always set the tax too high", "They cause shortages"], a: 1, why: "Where the resource cannot be owned or many parties are affected, bargaining breaks down." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Market-based policy", "Works through prices and ownership (taxes, subsidies, permits, property rights) and leaves decisions to buyers and sellers."],
  ["Command and control", "Rules and limits backed by penalties (regulation, bans, quotas, licences)."],
  ["Specific tax", "A fixed amount per unit; shifts supply parallel."],
  ["Ad valorem tax", "A percentage of the price; supply pivots."],
  ["Government failure", "Intervention that makes the allocation of resources worse or no better."],
  ["Information failure (government)", "The government cannot measure costs and benefits well enough to set the right policy."],
  ["Time lag", "Delay between the problem arising and the policy working."],
  ["Unintended consequence", "A side effect the policy-maker did not plan for."],
  ["Regulatory capture", "Regulators serve the firms they regulate rather than the public."],
  ["Opportunity cost of policy", "What else the money could have done."],
  ["Mixed economy", "An economy with both markets and government intervention."],
  ["Free market", "Resources allocated by prices and private decisions, with no government role."],
  ["Regressive tax", "Takes a larger share of income from low earners."],
] });
''' + MCQ([217, 218, 220], '''  { q: "[May/June 2020 · 31 · Q13] Which policy is not designed to correct a market failure?", opts: ["government provision of healthcare", "price controls on large firms", "regulations to limit smoke pollution", "removing import quotas"], a: 3, why: "Healthcare provision, price controls on large firms with market power and pollution rules all target a market failure. Removing import quotas is a trade policy." },
  { q: "[May/June 2023 · 31 · Q12] One reason for market failure is the existence of public goods. Which policy option is appropriate for addressing such a market failure?", opts: ["direct provision of the good by the government", "provision of detailed information to consumers", "subsidising firms that currently produce the good", "the adoption of maximum price controls"], a: 0, why: "Free riders mean private firms may not supply a public good, so the government provides it from taxation." },
  { q: "[Feb/March 2024 · 32 · Q11] A government wishes to use market forces to remove a negative externality in the consumption of a good. Which policy is likely to be the most effective?", opts: ["provide information about the undesirable side-effects", "give producers a subsidy so consumers can buy more cheaply", "impose an indirect tax on consumers to reduce consumption to the socially efficient level", "not interfere at all"], a: 2, why: "A tax works through the price, a market force, and cuts consumption towards the social optimum. A subsidy would raise it." },
  { q: "[Feb/March 2023 · 32 · Q15] A government wishes to reduce the use of cars in cities. Which policy should be used?", opts: ["a decrease in parking charges", "lowering tax on petrol (gasoline)", "restricting cycling", "subsidising public transport"], a: 3, why: "A cheaper alternative cuts car use. A, B and C all make driving cheaper or alternatives harder." },
  { q: "[Feb/March 2025 · 32 · Q8] What is not an example of government failure?", opts: ["decreased maximum price causing producers to leave the market", "higher guaranteed price encouraging suppliers to overproduce", "increased minimum wage leading to employers dismissing workers", "increased subsidies encouraging the consumption of a socially desirable product"], a: 3, why: "Encouraging consumption of a socially desirable good is the aim of a subsidy. A, B and C are harmful side effects." },
  { q: "[Oct/Nov 2022 · 33 · Q13] A government regards fresh fruit and vegetables as merit goods, and subsidises agriculture to boost their production. What could be a government failure arising from these subsidies?", opts: ["cheaper fresh fruit and vegetables", "land clearance reducing wildlife", "lower spending on treating dietary illnesses", "more jobs picking fruit and vegetables"], a: 1, why: "Land clearance is an unintended external cost. A, C and D are intended benefits." },
''')
write("gp4", page(EY.format(4), "Government Failure and Choosing the Right Policy",
  "Why intervention can leave society worse off, how to match each tool to the failure it fits, and how to weigh the free market against government action. Animated diagrams built from numbers, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Government Failure and Choosing the Right Policy", "government-failure-choosing-policy")
