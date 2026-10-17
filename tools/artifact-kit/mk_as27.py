"""AS syllabus 2.5.3-2.5.4 Causes of changes in consumer and producer surplus; the role of elasticity. Run: python3 tools/artifact-kit/mk_as27.py"""
from asx import *
EY = EYAS("2.5.3 to 2.5.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Consumer and producer surplus change whenever the <b>price or quantity traded</b> changes: a <b>shift of demand</b> or <b>supply</b>, an <b>indirect tax or subsidy</b>, a <b>maximum or minimum price</b>, or a change in <b>trade policy</b> such as a tariff. In general, <b>a fall in price raises consumer surplus</b> and a rise lowers it, while <b>a rise in price raises producer surplus</b> and a fall lowers it. <b>Price elasticity of demand and supply decide how big the changes are</b>: for the same price change, flatter (elastic) curves mean a bigger change in quantity and so a bigger change in surplus; for the same shift of supply, steeper (inelastic) demand means a larger price change. Policies that move the market away from equilibrium can cause a <b>welfare loss</b>, where total surplus falls.</p></div>

  <h2>1 · Causes of changes (2.5.3)</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>Consumer surplus</th><th>Producer surplus</th></tr>
    <tr><td><b>Demand rises</b></td><td>Rises (more willing to pay)</td><td>Rises (higher price and quantity)</td></tr>
    <tr><td><b>Demand falls</b></td><td>Falls</td><td>Falls</td></tr>
    <tr><td><b>Supply rises</b> (lower costs, technology, subsidy)</td><td>Rises (lower price, more quantity)</td><td>Depends: lower price but more units sold</td></tr>
    <tr><td><b>Supply falls</b> (higher costs, indirect tax)</td><td>Falls (higher price, less quantity)</td><td>Depends: higher price but fewer units sold</td></tr>
    <tr><td><b>Effective maximum price</b></td><td>Rises for those who can still buy, but quantity falls and some lose</td><td>Falls</td></tr>
    <tr><td><b>Effective minimum price</b></td><td>Falls</td><td>Rises for sellers who can sell, but some are left with unsold stock</td></tr>
    <tr><td><b>Tariff on imports</b></td><td>Falls (price rises, quantity falls)</td><td>Domestic producers' surplus rises</td></tr>
  </table></div>
  <ul>
    <li>An <b>indirect tax</b> shifts supply to the left; the price consumers pay rises and CS falls. Part of the tax is borne by producers, whose PS also falls, and the government gains revenue.</li>
    <li>A <b>subsidy</b> shifts supply to the right; consumers pay less, so CS rises, and producers receive the subsidy as well as the market price.</li>
    <li>A price control that stops trade at the equilibrium creates a <b>welfare loss</b> (a deadweight loss): surplus on trades that no longer happen.</li>
  </ul>

  <h2>2 · The role of elasticity (2.5.4)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>For the same supply shift to the left (a tax or cost rise):</b> if demand is <b>price inelastic</b> (steep), price rises a lot and quantity falls a little; if <b>elastic</b> (flat), price rises a little and quantity falls a lot. The consumer surplus loss is usually <b>larger for inelastic demand</b>, as in the example shown, because consumers pay much more for most units.</li>
    <li><b>For the same price fall:</b> with <b>elastic</b> demand quantity rises a lot, so many extra consumers gain and CS rises more.</li>
    <li>The more <b>inelastic supply</b>, the more of a tax is borne by producers and the more producer surplus falls.</li>
    <li><b>Judgement:</b> the extent of any change in surplus depends on the <b>size of the price change</b> as well as elasticity, and surplus cannot be measured exactly in real markets.</li>
  </ul>
  <div id="pic2" class="card"></div>
  <div class="tip"><b class="h">Exam tip</b>Draw <b>two diagrams</b> (or two demand curves) to compare elastic and inelastic demand, shade the lost consumer surplus on each and say which is bigger and <b>why</b>. Give a conclusion: the effect depends on PED and the size of the shift.</div>
'''

watch = '''
  <h2>1 · The same tax on two goods</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stT"></div>
  <h2>2 · The same price fall on two goods</h2>
  <div id="stF"></div>
'''

explore = '''
  <h2>Lab 1 · What happens to each surplus?</h2>
  <p>Choose a change in the market. The shaded areas show consumer surplus (blue) and producer surplus (green) afterwards.</p>
  <div class="card"><div class="grid2"><div><div id="evB" class="btnrow"></div>
    <div class="readout"><div><small>Consumer surplus</small><strong id="r1"></strong></div><div><small>Producer surplus</small><strong id="r2"></strong></div><div><small>Welfare loss</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Supply and demand with consumer and producer surplus after the chosen change"></svg></div></div></div>

  <h2>Lab 2 · Does elasticity matter?</h2>
  <p>A cost rise shifts supply to the left. Change how price elastic demand is and how big the cost rise is, and see the loss in consumer surplus.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>PED at equilibrium</small><strong id="t1"></strong></div><div><small>New price</small><strong id="t2"></strong></div><div><small>CS before to after</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="A leftward shift of supply with the lost consumer surplus shaded for the chosen demand elasticity"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Up or down?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of a tax on surplus in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Taxing cigarettes", "Smokers have inelastic demand, so a tax raises the price a lot and cuts quantity only a little. Consumer surplus falls sharply, producers lose less volume, and the government raises large revenue.", "inelastic demand, a large price rise and a big loss of consumer surplus.") +
rw("A subsidy on vaccines", "A subsidy shifts supply to the right, so vaccinations become cheaper and more people are vaccinated. Consumer surplus rises, and the gain is larger when demand is elastic because more extra people take the vaccine.", "a subsidy raising consumer surplus, and the role of elasticity.") +
rw("Price cap on energy bills", "A cap below the market price helps households that can buy at the lower price, but firms supply less. Producer surplus falls and some households cannot get all the energy they want, so total surplus falls.", "a maximum price causing a welfare loss.") +
rw("A tariff on imported steel", "A tariff raises the price of steel, so buyers lose consumer surplus. Domestic steel producers gain producer surplus, and the government gains revenue, but there is a welfare loss as less steel is traded.", "trade protection and the distribution of surplus.")
)

mc_exam = [
  mcq("s22_14", 17, "The market for good X is in equilibrium. A government then introduces an effective minimum price on good X. What will decrease as a result of this minimum price?", ["the excess supply of the product", "the market price of the product", "the quantity of the product supplied", "the size of the consumer surplus"], 3, "A price above equilibrium raises the price and cuts quantity demanded, so consumer surplus falls. Excess supply and quantity supplied rise."),
  mcq("s23_13", 14, "There are 10 000 tickets available to watch a sports final. The initial market equilibrium ticket price is $20. The government decides to fix an effective minimum price for the tickets. Under which conditions will the consumer surplus decrease the most as a result of the minimum price? (minimum price $18 or $22; price elasticity of demand −0.5 or −1.5)", ["$18 and −0.5", "$18 and −1.5", "$22 and −0.5", "$22 and −1.5"], 2, "A minimum price at $18 is below equilibrium and has no effect. At $22 the price paid rises, and with inelastic demand (−0.5) buyers keep buying most tickets at a much higher price, so the loss of consumer surplus is largest."),
  mcq("s20_13", 8, "The equilibrium price of a product is $10. The government introduces an effective minimum price of $12 for the product. Under which condition will the value of the producer surplus increase the most?", ["price elasticity of demand is 0", "price elasticity of demand is between 0 and 1", "price elasticity of demand is 1", "price elasticity of demand is greater than 1"], 0, "If demand is perfectly inelastic, quantity sold does not fall, so producers gain the full higher price on every unit."),
  mcq("s24_13", 27, "A country imports natural gas for which it has price-inelastic demand. What is the effect if that country imposes an import duty on the gas?", ["Consumers in the importing country will suffer a loss of consumer surplus", "The exporting country will gain export revenue", "The importing country's primary income will increase", "The price of natural gas will rise in other importing countries"], 0, "The duty raises the price paid. With inelastic demand consumers keep buying, so they pay more for the same quantity and lose consumer surplus.")
]

exam = exam_page("changes in consumer and producer surplus",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Changes in consumer surplus after a tax, subsidy or price control are an 8 mark Paper 2 part nearly every year, and a 12 mark part on elasticity and surplus has appeared. Reworded past questions are below, with four Paper 1 multiple choice questions that do not need a diagram.",
  [("Essay parts, 8 marks", "3", "Oct/Nov 2021 (22) Q3(a); May/June 2021 (21) Q3(a); Oct/Nov 2020 (22) Q2(a)"), ("Essay parts, 12 marks", "1", "May/June 2023 (23) Q2(b)"), ("Multiple choice (Paper 1)", "4 shown below", "2020 to 2024")],
  [
  eq(P("w21_22", "3(a)"), "8 marks", "Explain what is meant by consumer surplus and use diagrams to assess the impact on consumer surplus when an indirect tax is imposed on a good with price-elastic demand compared with the impact when the demand is price inelastic.",
     ["Knowledge (up to 2): consumer surplus is the difference between the price a consumer is willing to pay and the price actually paid.",
      "Application (up to 3): a diagram for price-elastic demand (flatter demand curve and a leftward shift of supply), the impact on price and quantity, and the fall in consumer surplus.",
      "Application (up to 3): a diagram for price-inelastic demand (steeper demand curve), the impact on price and quantity, the impact on consumer surplus compared with the elastic case, and possible reasons for the difference such as substitutability or addiction."],
     "Define CS. Two diagrams: tax shifts supply left. Elastic: smaller price rise, larger quantity fall. Inelastic: larger price rise. Compare CS losses.",
     [[("k", "Consumer surplus is the difference between the price consumers are willing to pay for a product and the market price actually paid, shown as the triangle below the demand curve and above the price.")], [("n", "An indirect tax shifts the supply curve to the left, raising the price and cutting quantity. If demand is price elastic (a flatter curve), consumers have many substitutes, so the price rises only a little and quantity falls a lot, and the fall in consumer surplus is smaller per unit sold. If demand is inelastic (a steeper curve), perhaps because the good is addictive or has few substitutes, the price rises by more and quantity falls little, so consumers lose a larger area of consumer surplus. Comparing the two diagrams, the inelastic case shows the bigger loss for the same tax.")]]),
  eq(P("s21_21", "3(a)"), "8 marks", "With the aid of diagrams, explain how consumer surplus is affected by a decrease in the price of a luxury product with many substitutes and of an essential product with few substitutes.",
     ["Knowledge (up to 2): a correct diagram, with axes labelled price and quantity (1) and the existence of consumer surplus shown (1).",
      "Application (up to 3): how consumer surplus is affected by a decrease in the price of a luxury product with many substitutes (elastic PED).",
      "Application (up to 3): how consumer surplus is affected by a decrease in the price of an essential product with few substitutes (inelastic PED)."],
     "Diagram with CS. A price fall raises CS as more consumers are willing to pay. Luxury: elastic, quantity rises a lot. Essential: inelastic.",
     [[("k", "On a demand diagram with price and quantity axes, consumer surplus is the triangle below the demand curve and above the price.")], [("n", "A fall in price increases consumer surplus, because existing buyers pay less and additional buyers whose willingness to pay is above the new price enter the market. For a luxury product with many substitutes, demand is elastic, so the quantity bought rises sharply and many new consumers gain surplus. For an essential product with few substitutes, demand is inelastic, so the quantity rises only slightly, and the gain is mainly to existing buyers who pay less for the same quantity. The extent of the change therefore depends on price elasticity of demand.")]]),
  eq(P("w20_22", "2(a)"), "8 marks", "Use a diagram to explain how a subsidy given to producers in the market for vaccinations will affect the market price and explain the impact of this subsidy upon the consumer surplus in this market.",
     ["Knowledge (up to 2): the meaning of consumer surplus.",
      "Application (up to 4): an accurately labelled diagram showing the supply curve shifting right (1), the fall in equilibrium price and rise in equilibrium quantity (1), the consumer surplus before the subsidy (1) and the rise in consumer surplus after the subsidy (1).",
      "Application (up to 2): another factor determining the fall in price, such as price elasticity of demand, price elasticity of supply or the size of the subsidy (1), and another factor determining the change in consumer surplus (1)."],
     "Define CS. Supply shifts right, price falls, quantity up, CS rises. Size depends on PED, PES and the subsidy.",
     [[("k", "Consumer surplus is the difference between what consumers are willing to pay and the price they actually pay.")], [("n", "A subsidy to vaccine producers lowers their costs, so supply shifts to the right. The equilibrium price falls and the quantity rises, so the consumer surplus triangle becomes larger: existing buyers pay less and new buyers join. The size of the change in price depends on the size of the subsidy and on the price elasticities of demand and supply, so these also determine how much consumer surplus rises.")]]),
  eq(P("s23_23", "2(b)"), "12 marks", "When the price of a product changes, it usually changes the consumer surplus in the market. Assess how variations in price elasticity of demand for a product determine the extent of changes in consumer surplus in a market.",
     ["Knowledge and analysis (up to 8): consumer surplus with an accurate labelled diagram; the effects on consumer surplus when price increases and decreases; the change for a product with price elastic demand and for one with inelastic demand; a comparison where PED varies. A one-sided answer is capped at Level 2.",
      "Evaluation (up to 4): the change depends on the relative extent of the price change, and other factors alongside elasticity; a justified conclusion."],
     "Define CS with a diagram. Price up/down. Elastic vs inelastic. Compare. Evaluate: size of price change, other factors.",
     [[("n", "Consumer surplus is the triangle between the demand curve and the price. If price rises, for example because of a tax, consumer surplus falls. With inelastic demand, quantity falls little, so most consumers continue to buy at the higher price and lose a large amount of surplus. With elastic demand, consumers switch away, so quantity falls more and the price rise is smaller, so the loss on each unit is smaller. If price falls, elastic demand brings in many new consumers, so the gain is larger than for inelastic demand for the same price fall.")], [("e", "Elasticity is not the only factor: the extent of the price change matters at least as much, and a large price change on an elastic product could cut surplus more than a small one on an inelastic product. Elasticity therefore determines how quantity responds, but the overall change in consumer surplus depends on both.")]])
  ],
  )

tips = tips_html(
  [("Name the cause and the direction.", "Tax: supply left, price up, CS down."),
   ("Compare two diagrams.", "Elastic and inelastic demand side by side."),
   ("Say which loses more and why.", "For a tax, inelastic demand usually loses more CS: price rises more."),
   ("Mention extra consumers.", "A price fall brings new buyers: bigger gain when demand is elastic."),
   ("Producers matter too.", "Inelastic supply means producers bear more of a tax."),
   ("Price controls cause welfare loss.", "Trade stops below the equilibrium quantity."),
   ("Conclude with 'depends'.", "On elasticity and the size of the price change.")],
  [("Consumer surplus", "A tax may reduce consumer surplus, by more when demand is inelastic."),
   ("Producer surplus", "A fall in price could reduce producer surplus."),
   ("Welfare loss", "A minimum price below the equilibrium quantity causes a welfare loss."),
   ("Elasticity", "Elasticity determines how far quantity changes when price changes."),
   ("Assess", "The extent depends on the price elasticity of demand and the size of the price change.")],
  [CW["define"], CW["explain"], CW["assess"], CW["evaluate"]]) + FC

js = SDJS + '''
const dEnd = (m) => Math.min(100, 50 + 45 / m);
/* ---------- shared panel drawing ---------- */
function panel(x0, m, L, k, name) {
  const X = (q) => x0 + q * 2.7, Y = (p) => 250 - p * 1.65, dint = 50 + 50 * m, Dp = (q) => 50 + m * (50 - q);
  const q1 = (40 + 50 * m - 0.8 * L) / (m + 0.8), p1 = Dp(q1);
  let o = SV.line(x0, 250, x0 + 300, 250) + SV.line(x0, 250, x0, 60) + SV.text(x0 + 6, 56, "Price", "sm") + SV.text(x0 + 300, 270, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(x0 + 150, 40, name, "lbl bd", { "text-anchor": "middle" });
  o += SV.line(X(0), Y(dint), X(dEnd(m)), Y(Dp(dEnd(m))), "c2", { "stroke-width": 3 }) + SV.line(X(0), Y(10), X(100), Y(90), "c1", { "stroke-width": 3 });
  o += SV.poly([[X(0), Y(dint)], [X(0), Y(50)], [X(50), Y(50)]], "f3", op(0.4)) + SV.circle(X(50), Y(50), 5, "dot1");
  const cs0 = 0.5 * 50 * (dint - 50), cs1 = 0.5 * q1 * (dint - p1);
  if (k > 0) {
    o += SV.line(X(0), Y(10 + 0.8 * L), X(100 - L), Y(90), "c3", { "stroke-width": 3, ...op(k) });
    o += SV.poly([[X(0), Y(dint)], [X(0), Y(p1)], [X(q1), Y(p1)]], "f3", op(0.4 * k)) + SV.poly([[X(0), Y(p1)], [X(0), Y(50)], [X(50), Y(50)], [X(q1), Y(p1)]], "f2", op(0.7 * k));
    o += SV.circle(X(q1), Y(p1), 6, "dot3", op(k)) + SV.text(x0 + 150, 292, "CS " + Lib.fmtN(cs0, 0) + " to " + Lib.fmtN(cs1, 0) + " (loss " + Lib.fmtN(cs0 - cs1, 0) + ")", "lbl bd", { "text-anchor": "middle", ...op(k) });
  } else o += SV.text(x0 + 150, 292, "CS " + Lib.fmtN(cs0, 0), "lbl bd", { "text-anchor": "middle" });
  return o;
}
function twoDraw(s) { return panel(40, 0.4, 15, s.k, "Elastic demand (flat)") + panel(420, 1.2, 15, s.k, "Inelastic demand (steep)"); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Supply shifts left on an elastic and an inelastic demand curve and consumer surplus falls by more on the inelastic one">${twoDraw({ k: 1 })}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 300, label: "The same leftward shift of supply with elastic and inelastic demand", base: { k: 0 }, draw: twoDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Before.</b> Two markets with the same supply curve and the same equilibrium ($50, 50 units). Demand is flat (elastic) in one and steep (inelastic) in the other. Consumer surplus is the shaded triangle: 500 and 1,500.", s: { k: 0 } },
  { cap: "<b>An indirect tax (or cost rise) shifts supply to the left</b> by the same amount in both markets. The shaded loss of consumer surplus is shown in green, with the remaining surplus in blue.", s: { k: 1 } },
  { cap: "<b>Elastic demand:</b> price up only a little ($54) and quantity down to 40; consumer surplus falls 180. <b>Inelastic demand:</b> price up more ($57) and quantity down to 44; consumer surplus falls about 338. The steeper demand curve suffers the bigger loss.", s: { k: 1 } },
] });

/* ---------- price fall ---------- */
function fallDraw(s) {
  const one = (x0, m, name) => {
    const X = (q) => x0 + q * 2.7, Y = (p) => 250 - p * 1.65, dint = 50 + 50 * m, q1 = 50 + 10 / m, gain = 10 * (50 + q1) / 2;
    let o = SV.line(x0, 250, x0 + 300, 250) + SV.line(x0, 250, x0, 60) + SV.text(x0 + 150, 40, name, "lbl bd", { "text-anchor": "middle" }) + SV.line(X(0), Y(dint), X(dEnd(m)), Y(50 + m * (50 - dEnd(m))), "c2", { "stroke-width": 3 });
    o += SV.line(X(0), Y(50), X(q1), Y(50), "dash") + SV.line(X(0), Y(40), X(q1), Y(40), "dash") + SV.poly([[X(0), Y(dint)], [X(0), Y(50)], [X(50), Y(50)]], "f3", op(0.35));
    if (s.k > 0) o += SV.poly([[X(0), Y(50)], [X(0), Y(40)], [X(q1), Y(40)], [X(50), Y(50)]], "f2", op(0.75 * s.k)) + SV.text(x0 + 150, 292, "Gain in CS: " + Lib.fmtN(gain, 0) + " (quantity " + Lib.fmtN(q1, 0) + ")", "lbl bd", { "text-anchor": "middle", ...op(s.k) });
    return o + SV.text(x0 - 6, Y(50) + 4, "50", "sm", { "text-anchor": "end" }) + SV.text(x0 - 6, Y(40) + 4, "40", "sm", { "text-anchor": "end" });
  };
  return one(40, 0.4, "Elastic demand") + one(420, 1.2, "Inelastic demand");
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="The same fall in price raises consumer surplus by more when demand is elastic">${fallDraw({ k: 1 })}</svg>`;
Lib.stepper($("#stF"), { w: 760, h: 300, label: "The same price fall from $50 to $40 with elastic and inelastic demand", base: { k: 0 }, draw: fallDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Before.</b> The price is $50 in both markets. Demand is elastic on the left and inelastic on the right.", s: { k: 0 } },
  { cap: "<b>The price falls to $40.</b> The extra consumer surplus (green) is the gain for existing buyers plus the gain for new buyers. With elastic demand quantity rises to 75, so the gain is about 625. With inelastic demand quantity rises to about 58, so the gain is about 542.", s: { k: 1 } },
] });

/* ---------- Lab 1: events ---------- */
const EVN = [
  ["Demand rises", { d: 15, s: 0 }, "More demand raises the price and quantity, so consumers gain willingness to pay and producers sell more at a higher price."],
  ["Demand falls", { d: -15, s: 0 }, "Less demand lowers the price and quantity, so both surpluses fall."],
  ["Costs fall (supply rises)", { d: 0, s: 10 }, "Supply moves right, the price falls and quantity rises: consumer surplus up."],
  ["Indirect tax (supply falls)", { d: 0, s: -15 }, "Supply moves left, the price rises and quantity falls: consumer surplus down, and producers also lose volume."],
  ["Maximum price $35", { p: 35 }, "Below equilibrium: quantity traded is set by supply, so some buyers cannot buy and total surplus falls."],
  ["Minimum price $65", { p: 65 }, "Above equilibrium: quantity traded is set by demand, so consumer surplus falls and some producers cannot sell."],
];
const polyS = (pts, c, v) => SV.poly(pts.map(([q, p]) => [SDX(q), SDY(p)]), c, op(v));
function showEv(i) {
  const [nm, a, why] = EVN[i]; let cs, ps, o, qd = 0;
  $$("#evB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  if (a.p !== undefined) {
    const p = a.p, up = p > 50, Q = up ? (90 - p) / 0.8 : (p - 10) / 0.8;
    cs = up ? 0.5 * Q * (90 - p) : 90 * Q - 0.4 * Q * Q - p * Q; ps = up ? p * Q - (10 * Q + 0.4 * Q * Q) : 0.5 * Q * (p - 10);
    const pts = up ? [[[0, 90], [0, p], [Q, p]], [[0, 10], [0, p], [Q, p], [Q, 10 + 0.8 * Q]]] : [[[0, 90], [0, p], [Q, p], [Q, 90 - 0.8 * Q]], [[0, 10], [0, p], [Q, p]]];
    o = sdPlot({ d: 0, s: 0, g: 0 }) + polyS(pts[0], "f3", 0.5) + polyS(pts[1], "f2", 0.5) + SV.line(70, SDY(p), SDX(Math.max(Q, 50)), SDY(p), "c4", { "stroke-width": 2.5 });
  } else {
    const e = sdEq(a.d, a.s), di = 90 + 0.8 * a.d, si = 10 - 0.8 * a.s; cs = 0.5 * e.q * (di - e.p); ps = 0.5 * e.q * (e.p - si);
    o = sdPlot({ d: a.d, s: a.s, g: 0, n: 1 }) + polyS([[0, di], [0, e.p], [e.q, e.p]], "f3", 0.5) + polyS([[0, si], [0, e.p], [e.q, e.p]], "f2", 0.5) + SV.circle(SDX(e.q), SDY(e.p), 5, "dot3");
  }
  $("#r1").textContent = Lib.fmtN(cs, 0) + (cs > 1005 ? " (up)" : cs < 995 ? " (down)" : ""); $("#r2").textContent = Lib.fmtN(ps, 0) + (ps > 1005 ? " (up)" : ps < 995 ? " (down)" : ""); $("#r3").textContent = a.p !== undefined ? Lib.fmtN(Math.max(0, 2000 - cs - ps), 0) : "None";
  $("#rv").textContent = nm + ". " + why + (a.p !== undefined ? " Starting surpluses are 1,000 each." : " Starting surpluses are 1,000 each; the market still trades at its new equilibrium, so there is no welfare loss.");
  $("#labA").innerHTML = o;
}
$("#evB").innerHTML = EVN.map((e, i) => `<button class="b" data-i="${i}">${e[0]}</button>`).join("");
$$("#evB button").forEach((b) => (b.onclick = () => showEv(+b.dataset.i)));
showEv(0);

/* ---------- Lab 2 ---------- */
function labE() {
  if (!$("#sl") || !$("#cc")) return;
  const m = +$("#sl").value / 10, L = +$("#cc").value, dint = 50 + 50 * m, q1 = (40 + 50 * m - 0.8 * L) / (m + 0.8), p1 = 50 + m * (50 - q1), cs0 = 0.5 * 50 * (dint - 50), cs1 = 0.5 * q1 * (dint - p1), ped = 1 / m;
  $("#t1").textContent = Lib.fmtN(ped, 2); $("#t2").textContent = "$" + Lib.fmtN(p1, 1); $("#t3").textContent = Lib.fmtN(cs0, 0) + " to " + Lib.fmtN(cs1, 0);
  $("#tv").textContent = L === 0 ? "No cost rise, so nothing changes." : `Supply shifts left by ${L}. With PED ${Lib.fmtN(ped, 2)} (${ped > 1 ? "elastic" : ped < 1 ? "inelastic" : "unit"}) the price rises by $${Lib.fmtN(p1 - 50, 1)} to $${Lib.fmtN(p1, 1)} and quantity falls from 50 to ${Lib.fmtN(q1, 0)}. Consumer surplus falls by ${Lib.fmtN(cs0 - cs1, 0)}. ${ped < 1 ? "Steeper demand means a bigger price rise, so the loss is larger." : "Flatter demand means a smaller price rise but a larger quantity fall."}`;
  const X = (q) => 60 + q * 5.5, Y = (p) => 270 - p * 1.7; let o = SV.line(60, 270, 600, 270) + SV.line(60, 270, 60, 30);
  o += SV.line(X(0), Y(dint), X(dEnd(m)), Y(50 + m * (50 - dEnd(m))), "c2", { "stroke-width": 3 }) + SV.line(X(0), Y(10), X(100), Y(90), "c1", { "stroke-width": 3 }) + SV.line(X(0), Y(10 + 0.8 * L), X(100 - L), Y(90), "c3", { "stroke-width": 3 });
  o += SV.poly([[X(0), Y(dint)], [X(0), Y(p1)], [X(q1), Y(p1)]], "f3", op(0.4)) + SV.poly([[X(0), Y(p1)], [X(0), Y(50)], [X(50), Y(50)], [X(q1), Y(p1)]], "f2", op(0.7)) + SV.circle(X(50), Y(50), 5, "dot1") + SV.circle(X(q1), Y(p1), 6, "dot3");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sl", label: "Steepness of demand (3 = flat and elastic, 12 = steep and inelastic) ", min: 3, max: 12, step: 1, value: 4, fmt: (v) => v, onInput: labE });
Lib.slider($("#g2"), { id: "cc", label: "Size of the leftward shift of supply ", min: 0, max: 30, step: 5, value: 15, fmt: (v) => v, onInput: labE });
labE();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What happens to consumer surplus?", ["Rises", "Falls", "Depends"],
  [("A subsidy to producers lowers the price", 0), ("An indirect tax on a good", 1), ("Demand shifts right", 0), ("An effective minimum price above equilibrium", 1), ("Costs fall and supply shifts right", 0), ("An import tariff raises the price", 1), ("The price falls but quantity bought is fixed", 0), ("A tax: size of the loss for steep vs flat demand", 2)],
  "A lower price raises consumer surplus; a higher price lowers it. The size of the change depends on elasticity.") + MATCH([
  ["Welfare loss", "Lost total surplus when trades no longer happen"],
  ["Indirect tax", "Shifts supply left, lowers CS, raises government revenue"],
  ["Subsidy", "Shifts supply right, raises CS"],
  ["Minimum price", "Raises price above equilibrium, lowers CS"],
  ["Inelastic demand", "Steep demand: price changes a lot, quantity little"],
  ["Elastic demand", "Flat demand: quantity changes a lot, price little"]]) + ORDER(
  "Put the effect of a tax on surplus in order.",
  ["An indirect tax is imposed on the good", "Supply shifts to the left", "The price consumers pay rises and quantity falls", "Consumer surplus (and producer surplus) fall", "The size of the fall depends on elasticity"],
  "Tax, supply left, price up, surplus down, size depends on elasticity.") + CALC([
  {"q": "Demand: P = 100 − 2Q; original supply P = 10 + Q, equilibrium Q = 30, P = $40. Consumer surplus = ½ × 30 × 60. What is it?", "a": 900, "unit": "$", "tol": 1, "hint": "½ × 30 × 60.", "sol": "<b>$900</b>."},
  {"q": "A tax shifts supply to P = 25 + Q. What is the new equilibrium quantity?", "a": 25, "unit": "units", "tol": 0.5, "hint": "100 − 2Q = 25 + Q.", "sol": "75 = 3Q, so Q = <b>25</b>, P = $50."},
  {"q": "What is the new consumer surplus (½ × Q × (100 − P))?", "a": 625, "unit": "$", "tol": 1, "hint": "½ × 25 × 50.", "sol": "<b>$625</b>."},
  {"q": "By how much did consumer surplus fall ($)?", "a": 275, "unit": "$", "tol": 1, "hint": "900 − 625.", "sol": "<b>$275</b>."}]) + MCQ([
  ("A fall in price will usually cause consumer surplus to:", ["Rise", "Fall", "Stay the same", "Become zero"], 0, "Buyers pay less than before."),
  ("A tax shifts supply left. Consumer surplus falls most when demand is:", ["Inelastic (steep)", "Elastic (flat)", "Perfectly elastic", "Unit elastic only"], 0, "A steeper demand curve means a larger price rise."),
  ("A price control that stops some mutually beneficial trades causes:", ["A welfare loss", "A rise in total surplus", "More consumer surplus only", "No change"], 0, "Total surplus falls."),
  ("A subsidy to producers will usually:", ["Raise consumer surplus", "Lower consumer surplus", "Raise the price", "Reduce quantity"], 0, "Price falls and quantity rises."),
  ("An effective maximum price:", ["Reduces producer surplus", "Raises producer surplus", "Has no effect on surplus", "Always raises total surplus"], 0, "Producers receive a lower price and sell fewer units.")
], "qz1") + CARDS([
  ("Price up", "CS down, PS up."),
  ("Price down", "CS up, PS down."),
  ("Tax", "Supply left, CS down."),
  ("Subsidy", "Supply right, CS up."),
  ("Max price", "Shortage, PS down."),
  ("Min price", "Surplus, CS down."),
  ("Welfare loss", "Lost total surplus."),
  ("Elasticity", "Decides how big the change is.")]) + MCQ(mc_exam)

build("as27", "as-surplus-changes-elasticity", "Changes in Consumer and Producer Surplus", EY,
  "2.5.3 to 2.5.4: causes of changes in consumer and producer surplus and how price elasticity of demand and supply affect the extent of the change. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
