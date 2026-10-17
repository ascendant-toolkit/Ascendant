"""AS syllabus 2.2.1 Price elasticity of demand. Run: python3 tools/artifact-kit/mk_as28.py"""
from as6k import *
EY = EYAS("2.2.1")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Price elasticity of demand (PED)</b> measures how responsive the quantity demanded is to a change in price: <b>PED = % change in quantity demanded ÷ % change in price</b>. It is normally <b>negative</b> because demand slopes downward, and what matters is its <b>size</b>: demand is <b class="kw">elastic</b> if the size is above 1 (quantity changes by a bigger percentage than price), <b class="kw">inelastic</b> if it is between 0 and 1, <b>unitary</b> if it equals 1, <b>perfectly inelastic</b> (0) and <b>perfectly elastic</b> (infinite) at the extremes. It is determined by the <b>availability and closeness of substitutes</b>, whether the good is a <b>necessity or a luxury</b>, the <b>proportion of income</b> spent on it, <b>habit or addiction</b>, how <b>narrowly the market is defined</b> and the <b>time period</b>. PED tells a firm what a price change may do to <b>total revenue</b>: with elastic demand a price cut may raise revenue, with inelastic demand a price rise may raise revenue.</p></div>

  <h2>1 · Calculating and interpreting PED</h2>
  <div class="tw"><table class="t">
    <tr><th>PED (size)</th><th>Description</th><th>Price rise of 10% means</th><th>Total revenue after a price rise</th></tr>
    <tr><td>0</td><td>Perfectly inelastic</td><td>Quantity unchanged</td><td>Rises</td></tr>
    <tr><td>0 to 1</td><td>Inelastic</td><td>Quantity falls by less than 10%</td><td>Rises</td></tr>
    <tr><td>1</td><td>Unitary</td><td>Quantity falls by 10%</td><td>Unchanged</td></tr>
    <tr><td>Above 1</td><td>Elastic</td><td>Quantity falls by more than 10%</td><td>Falls</td></tr>
    <tr><td>Infinite</td><td>Perfectly elastic</td><td>Quantity falls to zero</td><td>Falls to zero</td></tr>
  </table></div>
  <ul>
    <li><b>Total revenue (total expenditure)</b> = price × quantity. A price cut raises revenue if demand is elastic, lowers it if inelastic, and leaves it unchanged if unitary.</li>
    <li><b>Along a straight-line demand curve</b> PED changes: it is elastic at high prices, unitary at the mid-point and inelastic at low prices, even though the slope is constant.</li>
  </ul>
  <div id="pic1" class="card"></div>

  <h2>2 · Determinants of PED</h2>
  <ul>
    <li><b>Substitutes:</b> the more and the closer the substitutes, the more elastic demand. A single brand has more elastic demand than the product as a whole.</li>
    <li><b>Necessity or luxury:</b> necessities tend to be inelastic, luxuries elastic.</li>
    <li><b>Proportion of income:</b> the larger the share of income, the more elastic.</li>
    <li><b>Habit or addiction:</b> tends to make demand more inelastic.</li>
    <li><b>Time:</b> demand tends to be more elastic in the long run, as people find substitutes.</li>
    <li><b>Definition of the market:</b> the narrower the definition, the more elastic.</li>
  </ul>

  <h2>3 · Why it matters</h2>
  <ul>
    <li><b>Firms:</b> pricing decisions and forecasting revenue; <b>price discrimination</b> is easier when elasticities differ between groups.</li>
    <li><b>Government:</b> an indirect tax raises more revenue on goods with inelastic demand; taxes on demerit goods may do little to cut consumption if demand is inelastic.</li>
    <li><b>Producers' limits:</b> firms may find it hard to control the determinants of PED, for example by building brand loyalty or reducing substitutes.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Write the <b>formula</b>, say <b>percentage</b> change (not "large or small" changes), and always link elasticity to <b>total revenue</b> for both a price rise <b>and</b> a price cut. Use "may" and "likely".</div>
'''

watch = '''
  <h2>1 · PED and total revenue along a demand curve</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · What happens after a price cut</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Move along the demand curve</h2>
  <p>Demand is Q = 100 − P. Move the price and watch PED and total revenue change.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div>
    <div class="readout"><div><small>Quantity</small><strong id="r1"></strong></div><div><small>PED (size)</small><strong id="r2"></strong></div><div><small>Total revenue</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="A straight line demand curve with a revenue rectangle at the chosen price"></svg></div></div></div>

  <h2>Lab 2 · Price change calculator</h2>
  <p>Choose a PED and a price change to see the effect on quantity and revenue.</p>
  <div class="card"><div class="grid2"><div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Change in quantity demanded</small><strong id="t1"></strong></div><div><small>Change in total revenue</small><strong id="t2"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Bars showing the change in price, quantity and revenue"></svg></div></div></div>
'''

practise = practise_html("Elastic or inelastic?", "Match the term to its description", "Put the effects of a price cut with elastic demand in order")

real = RWNOTE + (
rw("Petrol and fuel", "Drivers need fuel to commute, and there are few close substitutes in the short run, so demand is likely to be inelastic. A price rise may raise revenue for sellers, and tax on fuel raises a lot of revenue.", "an inelastic necessity.") +
rw("A named brand of coffee", "If one brand raises its price, customers can switch to many other brands, so demand for that brand is likely to be elastic, even though demand for coffee in general may be inelastic.", "substitutes and the definition of the market.") +
rw("Cinema ticket discounts", "A cinema cuts ticket prices on quiet nights to fill seats. If demand is elastic, the rise in tickets sold outweighs the lower price and revenue could rise.", "elastic demand and revenue.") +
rw("Cigarettes and addiction", "Habit and addiction make demand more inelastic, so a tax increase may raise revenue but reduce consumption by less than hoped.", "habit and inelastic demand.")
)

mc_exam = [
  mcq("m20_12", 5, "In which circumstance will the total expenditure by consumers on a good increase when its price increases?", ["Demand for the good is income elastic.", "Demand for the good is price inelastic.", "The price of a complementary good also increases.", "The price of substitute goods also increases."], 1, "With inelastic demand quantity falls by a smaller percentage than price rises, so expenditure rises."),
  mcq("m25_12", 11, "A decrease in the quantity demanded of a product results in a proportionate decrease in sales revenues. What is true about its price elasticity of demand?", ["It is between zero and one.", "It is infinite.", "It is unitary.", "It is zero."], 1, "Revenue falls in proportion to quantity only if price is unchanged, which is the case when demand is perfectly elastic at that price."),
  mcq("s20_11", 13, "The economics department of a university calculates that the price elasticity of demand for the products of a local firm is between -1.1 and -1.3. Which decision could be justified by the research?", ["Increase prices to increase profit.", "Invest in more capital to increase output.", "Reduce advertising to reduce costs.", "Reduce prices to increase revenue."], 3, "Demand is elastic, so a price cut raises total revenue."),
  mcq("s20_12", 6, "A manufacturer progressively reduces the price of his product. The table shows the outcome: at prices of $10, $9 and $8, total revenue is $750 (000s) each time. What is the price elasticity of demand for the product?", ["perfectly inelastic", "relatively inelastic", "perfectly elastic", "unitary"], 3, "Revenue does not change when price changes, so demand is unitary."),
  mcq("s21_11", 8, "Why is the price elasticity of demand for a particular brand of coffee likely to be higher than the price elasticity of demand for coffee in general?", ["Coffee in general takes up a higher proportion of consumers' income.", "Consumers may be very loyal to a particular brand of coffee.", "There are more substitutes for a particular brand of coffee than for coffee in general.", "Total demand for coffee is higher than for any one brand."], 2, "Other brands are close substitutes for a single brand."),
  mcq("s21_12", 6, "The price elasticity of demand for a firm's product is equal to one for all price changes. What would be the result of this?", ["A percentage increase in price will cause demand to fall by a larger percentage.", "A percentage increase in price will cause demand to increase by the same percentage.", "Quantity demanded will always be the same whatever the price.", "The firm's revenue will always be the same whatever the price."], 3, "With unitary elasticity, price and quantity change by the same percentage in opposite directions, so revenue is constant."),
  mcq("s22_12", 9, "What would be the most likely reason for a firm's decision to calculate the price elasticity of demand for its product?", ["to provide retail statistics for the government", "to predict the change in its total revenue after it raises prices", "to calculate the firm's competitive position", "to enable the firm to complete consumer satisfaction surveys"], 1, "PED shows how revenue may respond to a price change."),
  mcq("s22_14", 11, "The price elasticity of demand for a high-quality smartphone is elastic. The price of the smartphone decreases. What is the impact on the quantity demanded and total revenue? (quantity demanded, total revenue)", ["rises by a greater percentage than the price fall, falls", "rises by a greater percentage than the price fall, rises", "rises by a smaller percentage than the price fall, falls", "rises by a smaller percentage than the price fall, rises"], 1, "With elastic demand, quantity rises by a greater percentage than price falls, so revenue rises."),
  mcq("s23_13", 5, "When is the price elasticity of demand for a product most likely to be price elastic?", ["A large percentage of income is spent on the product.", "It is measured in the short run.", "It is a necessity product.", "There are few substitutes available."], 0, "A large share of income makes consumers more responsive to price."),
  mcq("s23_13", 10, "When the price of a firm's product falls by 5%, its total revenue also falls by 5%. What describes the product's price elasticity of demand?", ["elastic", "infinite", "unitary", "zero"], 3, "Quantity is unchanged, so demand is perfectly inelastic (zero).")
]

exam = exam_page("price elasticity of demand",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). PED is a regular 8 mark Paper 2 part (formula, meaning and what it tells a firm) and appears in 12 mark comparisons with other elasticities. Reworded past questions are below, with ten Paper 1 multiple choice questions that do not need a diagram.",
  [("Essay parts, 8 marks", "3", "May/June 2025 (24) Q2(a); Oct/Nov 2023 (22) Q2(a); Oct/Nov 2022 (21) Q2(a)"), ("Essay parts, 12 marks", "1", "May/June 2022 (22) Q3(b)"), ("Multiple choice (Paper 1)", "10 shown below", "2020 to 2025")],
  [
  eq(P("s25_24", "2(a)"), "8 marks", "With the help of a formula, explain the meaning of price elasticity of demand and consider the significance to a firm of having price elastic or price inelastic demand for its product.",
     ["Knowledge (up to 3): it measures the responsiveness of changes in demand to changes in price (1); the correct formula (1); the meaning of price elastic and inelastic in terms of the percentage or proportionate response (1).",
      "Analysis (up to 3): the impact of rising or falling prices on the demand for a firm's products when PED is inelastic (1) and when it is elastic (1), with both rising and falling prices considered.",
      "Evaluation (up to 2): a valid judgement on the importance of the distinction between elastic and inelastic demand for the effect of price changes on sales, with a mark for assessing what a firm should do to influence demand or spending."],
     "Formula and meaning. Elastic: price cut raises revenue. Inelastic: price rise raises revenue. Judge: the firm should use elasticity, but other factors matter.",
     [[("k", "Price elasticity of demand measures how responsive the quantity demanded is to a price change. It equals the percentage change in quantity demanded divided by the percentage change in price. Demand is elastic if the quantity changes by a greater percentage than price, and inelastic if by a smaller percentage.")], [("n", "If demand is elastic, a fall in price may raise total revenue because the rise in quantity outweighs the lower price, while a rise in price may reduce revenue. If demand is inelastic, a rise in price may raise revenue because quantity falls by less than price rises, while a price cut would reduce revenue.")], [("e", "Knowing whether demand is elastic or inelastic is likely to be very useful in setting prices, as it suggests whether to raise or cut prices to increase revenue. But the estimate may be inaccurate and other factors, such as competitors' responses, could change the outcome.")]]),
  eq(P("w23_22", "2(a)"), "8 marks", "With the help of a formula, explain what is meant by the term price elasticity of demand for a product and consider the extent to which it allows an entrepreneur to determine the effect of price changes on the total expenditure on their product.",
     ["Knowledge (up to 3): a clear understanding of the meaning of PED (1), an accurate formula (1), and what price elastic and inelastic mean in terms of relative proportionate or percentage changes rather than large or small changes (1).",
      "Analysis (up to 3): how total expenditure is affected by price changes if demand is elastic (up to 2) and if demand is inelastic (up to 2); both price increases and decreases should be considered, otherwise a maximum of 1 mark for that part.",
      "Evaluation (up to 2): considering the extent to which the concept helps the entrepreneur to determine the effect."],
     "Formula and meaning. Elastic: price and expenditure move in opposite directions. Inelastic: same direction. Evaluate: estimates and other factors.",
     [[("k", "Price elasticity of demand is the percentage change in quantity demanded divided by the percentage change in price. Demand is elastic if the percentage change in quantity is greater than the percentage change in price, and inelastic if it is smaller.")], [("n", "If demand is elastic, a price rise leads to a larger percentage fall in quantity, so total expenditure falls, and a price cut raises total expenditure. If demand is inelastic, a price rise leads to a smaller percentage fall in quantity, so expenditure rises, and a price cut lowers it.")], [("e", "PED helps an entrepreneur predict the effect on expenditure, but only to the extent that the estimate is accurate. Elasticity can change along the demand curve and over time, and other factors such as rivals' prices may alter the outcome.")]]),
  eq(P("w22_21", "2(a)"), "8 marks", "Explain two factors that will determine the price elasticity of demand for a particular brand of car and how this price elasticity of demand may change over time.",
     ["Knowledge (up to 2): a correct definition of PED, the extent to which a change in price leads to a change in quantity demanded (1), and a correct formula (1).",
      "Application (up to 6): one factor affecting PED for a particular brand of car, taking into account how it may change over time (up to 3), and a second factor (up to 3). Factors include the availability and price of substitutes, price relative to income, brand loyalty, need or want, and the time period."],
     "Define and formula. Factor 1: substitutes (many brands, so elastic; may change as brands change). Factor 2: loyalty or proportion of income. Time: more elastic in the long run.",
     [[("k", "Price elasticity of demand measures the extent to which a change in price changes the quantity demanded. It equals the percentage change in quantity demanded divided by the percentage change in price.")], [("n", "One factor is the availability of substitutes. With many car makers offering similar models, demand for a particular brand is likely to be elastic, and over time, as new rivals enter, it could become more elastic still. A second factor is the proportion of income spent, since a car is a large purchase, which makes demand more elastic, although as incomes rise this could fall over time. Brand loyalty could make demand less elastic, but may fade if competitors improve their cars.")]]),
  eq(P("s22_22", "3(b)"), "12 marks", "Discuss the difficulties that businesses might have when they try to control the factors that determine the price elasticity of demand for a product and consider whether attempts to control these factors are likely to be successful.",
     ["Analysis (up to 8): the difficulties a business might have controlling a factor that influences PED (up to 4 per factor; at least two factors for full marks). Factors include whether the good is a necessity, whether it is habit forming, the availability and attractiveness of substitutes, the proportion of income spent and the time period. Simply explaining the factors without reference to control is not rewarded.",
      "Evaluation (up to 4): whether the difficulties can be overcome (up to 3) and a reasoned conclusion (1)."],
     "Factors: substitutes, habit, proportion of income, time. Difficulties: firms cannot control rivals or incomes. Evaluate: advertising, loyalty schemes, innovation may help.",
     [[("n", "A firm may try to reduce the availability of substitutes by differentiating its product through branding, advertising and innovation, but rivals can copy it or launch alternatives, and consumers' tastes are hard to control. A firm may try to make a product habit forming through loyalty schemes or subscriptions, but it cannot easily make a product a necessity or change the proportion of income a household spends on it, which depends on incomes and the firm's own price. Time is also outside the firm's control, as demand tends to become more elastic in the long run.")], [("e", "Attempts to control the factors may be partly successful, especially through brand loyalty and product differentiation, which can make demand less elastic. But the success could be limited by competition and by consumer incomes, so the firm is unlikely to control elasticity fully.")]])
  ],
  )

tips = tips_html(
  [("Write the formula.", "% change in quantity demanded ÷ % change in price."),
   ("Use percentages.", "Not 'big' or 'small' changes."),
   ("Link to revenue.", "Both a price rise and a price cut."),
   ("Give the determinants.", "Substitutes, necessity, income share, habit, time."),
   ("Drop the minus sign.", "Talk about size: above or below 1."),
   ("Apply it.", "Name a product and say why."),
   ("Evaluate.", "Estimates change; other factors matter.")],
  [("PED", "Price elasticity of demand measures the responsiveness of quantity demanded to a change in price."),
   ("Elastic", "Demand is elastic if the percentage change in quantity is greater than the percentage change in price."),
   ("Inelastic", "Demand is inelastic if the percentage change in quantity is smaller than the percentage change in price."),
   ("Total revenue", "Total revenue is price multiplied by quantity sold."),
   ("Unitary", "Unitary elasticity means a price change leaves revenue unchanged.")],
  [CW["explain"], CW["consider"], CW["discuss"], CW["assess"]]) + FC

js = SDJS + CHAINJS + '''
const pedAt = (p) => ({ q: 100 - p, ped: p / (100 - p), tr: p * (100 - p) });
function demDraw(p, k = 1) {
  const d = pedAt(p); let o = axes(70, 270, 720, 25, "Quantity", "Price") + SV.line(SDX(0), SDY(100), SDX(100), SDY(0), "c2", { "stroke-width": 3 }) + tag(SDX(100) + 4, SDY(0) - 4, "Demand", "c2");
  o += SV.rect(SDX(0), SDY(p), SDX(d.q) - SDX(0), SDY(0) - SDY(p), "f1", op(0.5 * k)) + SV.text(SDX(d.q / 2), SDY(p / 2) + 4, "Total revenue " + Lib.fmtN(d.tr, 0), "sm", { "text-anchor": "middle", ...op(k) });
  o += SV.circle(SDX(d.q), SDY(p), 6, "dot3", op(k)) + SV.text(SDX(d.q) + 10, SDY(p) - 8, "P = " + p + ", PED " + Lib.fmtN(d.ped, 2), "sm", op(k));
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Demand curve with PED elastic at high prices and inelastic at low prices">${demDraw(80)}</svg>`;
Lib.stepper($("#stA"), { w: 760, h: 300, label: "PED and revenue along a straight-line demand curve", base: { p: 80 }, draw: (s) => demDraw(s.p), tween: 900, dwell: 5600, steps: [
  { cap: "<b>At a high price of 80</b>, quantity is 20 and PED is 4: <b>elastic</b>. Revenue is 1600.", s: { p: 80 } },
  { cap: "<b>At 50</b>, quantity is 50 and PED is 1: <b>unitary</b>. Revenue is at its maximum of 2500.", s: { p: 50 } },
  { cap: "<b>At a low price of 20</b>, quantity is 80 and PED is 0.25: <b>inelastic</b>. Revenue falls back to 1600.", s: { p: 20 } },
] });
chainStep("#stB", "A price cut when demand is elastic", ["The firm cuts its price by 10%", "Quantity demanded rises by more than 10% (PED above 1)", "The rise in quantity outweighs the lower price", "Total revenue rises", "If demand were inelastic, revenue would fall instead"], [
  "<b>A price cut</b> of 10%.", "<b>Elastic demand:</b> quantity rises by, say, 20%.", "<b>Revenue = price × quantity:</b> 0.90 × 1.20 = 1.08.", "<b>Revenue rises</b> by about 8%.", "<b>With inelastic demand</b> (say quantity +5%) revenue would be 0.90 × 1.05 = 0.945, a fall."]);

function labA() {
  if (!$("#g1v")) return;
  const p = +$("#g1v").value, d = pedAt(p);
  $("#r1").textContent = d.q; $("#r2").textContent = Lib.fmtN(d.ped, 2); $("#r3").textContent = Lib.fmtN(d.tr, 0);
  $("#rv").textContent = Math.abs(d.ped - 1) < 0.02 ? "PED is 1: unitary. Revenue is at its maximum; a small price change leaves it roughly unchanged." : d.ped > 1 ? `PED is ${Lib.fmtN(d.ped, 2)}: elastic. A price cut may raise revenue, and a price rise may reduce it.` : `PED is ${Lib.fmtN(d.ped, 2)}: inelastic. A price rise may raise revenue, and a price cut may reduce it.`;
  $("#labA").innerHTML = demDraw(p);
}
Lib.slider($("#g1"), { id: "g1v", label: "Price ", min: 10, max: 90, step: 5, value: 70, fmt: (v) => v, onInput: labA });
labA();
function labB() {
  if (!["g2v", "g3v"].every((i) => $("#" + i))) return;
  const ped = +$("#g2v").value / 10, pc = +$("#g3v").value, qc = -ped * pc, tr = ((1 + pc / 100) * (1 + qc / 100) - 1) * 100;
  $("#t1").textContent = (qc >= 0 ? "+" : "") + Lib.fmtN(qc, 1) + "%"; $("#t2").textContent = (tr >= 0 ? "+" : "") + Lib.fmtN(tr, 1) + "%";
  const bar = (y, lab, v, c) => SV.text(20, y + 15, lab, "sm") + SV.rect(150, y, Math.abs(v) * 8, 22, c, op(0.7)) + SV.text(156 + Math.abs(v) * 8, y + 16, (v >= 0 ? "+" : "") + Lib.fmtN(v, 1) + "%", "lbl bd");
  $("#labB").innerHTML = bar(20, "Price", pc, "f3") + bar(70, "Quantity", qc, "f1") + bar(120, "Revenue", tr, "f2");
  $("#tv").textContent = `With PED of ${Lib.fmtN(ped, 1)} (${ped > 1 ? "elastic" : ped < 1 ? "inelastic" : "unitary"}) a ${pc >= 0 ? "rise" : "fall"} of ${Math.abs(pc)}% in price changes quantity by ${Lib.fmtN(qc, 1)}% and total revenue by ${Lib.fmtN(tr, 1)}%.`;
}
Lib.slider($("#g2"), { id: "g2v", label: "PED (size) × 10 ", min: 2, max: 30, step: 2, value: 14, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labB });
Lib.slider($("#g3"), { id: "g3v", label: "Change in price, % ", min: -20, max: 20, step: 5, value: -10, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labB });
labB();
''' + CLASSIFY("cl1", "Is demand more likely to be elastic or inelastic?", ["Elastic", "Inelastic"],
  [("A single brand with many close rivals", 0), ("Petrol for daily commuting, in the short run", 1), ("A luxury holiday", 0), ("An addictive product such as cigarettes", 1), ("A good that takes a large share of income", 0), ("Table salt", 1), ("A product measured over several years", 0), ("Life-saving medicine", 1)],
  "Many substitutes, luxuries, large income share and a long period make demand more elastic; necessities, habits and small spending make it more inelastic.") + MATCH([
  ["PED", "% change in quantity demanded ÷ % change in price"],
  ["Elastic demand", "Quantity changes by a greater percentage than price"],
  ["Inelastic demand", "Quantity changes by a smaller percentage than price"],
  ["Unitary demand", "Revenue stays the same when price changes"],
  ["Total revenue", "Price × quantity"],
  ["Perfectly inelastic", "Quantity does not change when price changes"]]) + ORDER(
  "Put the effects of a price cut with elastic demand in order.",
  ["The firm cuts its price", "Quantity demanded rises by a larger percentage", "The rise in quantity outweighs the fall in price", "Total revenue rises"],
  "Elastic demand: quantity rises more than price falls, so revenue rises.") + CALC([
  {"q": "Price rises by 10% and quantity demanded falls by 25%. What is the PED (size)?", "a": 2.5, "unit": "", "tol": 0.05, "hint": "25 ÷ 10.", "sol": "<b>2.5</b>, elastic."},
  {"q": "PED is -0.4 and price rises by 15%. By what % does quantity demanded change?", "a": -6, "unit": "%", "tol": 0.1, "hint": "-0.4 × 15.", "sol": "<b>-6%</b>."},
  {"q": "Price falls from $20 to $18 and quantity rises from 100 to 130. What is the PED (size)?", "a": 3, "unit": "", "tol": 0.05, "hint": "% change in Q = 30%; % change in P = 10%.", "sol": "<b>3</b>, elastic."},
  {"q": "Using the same figures, by how much does total revenue change ($)?", "a": 340, "unit": "$", "tol": 0.5, "hint": "(18 × 130) − (20 × 100).", "sol": "2340 − 2000 = <b>$340</b> increase."}]) + MCQ([
  ("Elastic demand means:", ["PED size above 1", "PED size below 1", "PED is zero", "Price is fixed"], 0, "Quantity changes by more than price."),
  ("With inelastic demand a price rise:", ["Raises revenue", "Lowers revenue", "Leaves revenue unchanged", "Cuts quantity to zero"], 0, "Quantity falls less than price rises."),
  ("A cause of more elastic demand is:", ["Many close substitutes", "A necessity", "Addiction", "A small share of income"], 0, "Consumers can switch."),
  ("PED = ", ["% change in Q demanded ÷ % change in price", "Change in price ÷ change in Q", "Price × quantity", "% change in income ÷ % change in Q"], 0, "The PED formula."),
  ("Demand is usually more elastic:", ["In the long run", "In the short run", "For necessities", "For addictive goods"], 0, "People find substitutes over time.")
], "qz1") + CARDS([
  ("PED formula", "%ΔQd ÷ %ΔP."),
  ("Elastic", "Size above 1."),
  ("Inelastic", "Size below 1."),
  ("Unitary", "Size equals 1."),
  ("Elastic, price cut", "Revenue rises."),
  ("Inelastic, price rise", "Revenue rises."),
  ("Determinants", "Substitutes, necessity, income share, habit, time."),
  ("Along a straight line", "Elastic high, unitary mid, inelastic low.")]) + MCQ(mc_exam)

build("as28", "as-price-elasticity-of-demand", "Price Elasticity of Demand", EY,
  "2.2.1: calculating and interpreting PED, its determinants and its link to total revenue. Animated demand curves, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
