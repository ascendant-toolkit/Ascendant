"""AS syllabus 6.2.1-6.2.2 Protectionism: meaning and tools. Run: python3 tools/artifact-kit/mk_as63.py"""
from asx import *
EY = EYAS("6.2.1 to 6.2.2")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Protectionism</b> is the use of government policy to <b>protect domestic producers from foreign competition</b>, restricting free trade and raising the price competitiveness of domestic firms. The main tools are <b class="kw">tariffs</b> (taxes on imports), <b class="kw">import quotas</b> (limits on the quantity of imports), <b class="kw">export subsidies</b> (payments to exporters), <b class="kw">embargoes</b> (bans on trade) and <b class="kw">excessive administrative burdens</b> or <b>"red tape"</b> (complex rules and delays). A tariff or quota <b>raises the domestic price</b>, <b>reduces imports</b> and <b>raises domestic output</b>, helping producers but harming consumers, who pay more and have less choice, and causing a <b>welfare loss</b>. How effective a tool is depends on the <b>price elasticity</b> of demand for imports, the possibility of <b>retaliation</b> and whether domestic industries can meet the extra demand.</p></div>

  <h2>1 · Tariffs (6.2.2)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li>A <b>tariff</b> is a tax on imported goods. It raises the price of imports above the world price, so <b>domestic production rises</b>, <b>domestic consumption falls</b> and <b>imports fall</b>.</li>
    <li>The government gains <b>tariff revenue</b> (tariff per unit × quantity imported after the tariff).</li>
    <li><b>Consumers lose</b> consumer surplus (higher price, less choice); <b>domestic producers gain</b> producer surplus; there is a <b>deadweight welfare loss</b>, since resources move from efficient foreign producers to less efficient domestic ones.</li>
    <li><b>Effectiveness:</b> works better if demand for imports is <b>price elastic</b> and domestic firms can expand; may provoke <b>retaliation</b> and can raise <b>costs</b> for firms using imported inputs (cost-push inflation).</li>
  </ul>

  <h2>2 · Other tools</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Tool</th><th>How it works</th><th>Effect</th></tr>
    <tr><td><b>Import quota</b></td><td>A limit on the quantity of a good that may be imported</td><td>Raises the domestic price; the price gap goes to importers or foreign suppliers (no government revenue unless licences are sold)</td></tr>
    <tr><td><b>Export subsidy</b></td><td>A payment to domestic firms for each unit exported</td><td>Lowers export prices, raising exports; costs the government; may provoke retaliation or be challenged as dumping</td></tr>
    <tr><td><b>Embargo</b></td><td>A complete ban on trade with a country or in a good</td><td>Imports fall to zero; used for political or security reasons</td></tr>
    <tr><td><b>Excessive administrative burdens ("red tape")</b></td><td>Complicated customs rules, standards and delays</td><td>Raises the cost of importing and discourages trade; hard to measure and challenge</td></tr>
  </table></div>
  <ul>
    <li><b>Tariff versus quota:</b> a tariff gives the government revenue and keeps the price mechanism; a quota fixes the quantity more precisely but creates a quota rent for importers and may encourage corruption.</li>
    <li><b>Voluntary export restraints</b> are agreements by an exporter to limit sales, and work like a quota.</li>
    <li><b>Not protectionism:</b> a rise in domestic sales tax that applies equally to all goods, or import subsidies.</li>
  </ul>

  <h2>3 · Worked examples</h2>
  <p><b>A tariff in numbers.</b> Demand is P = 100 − 0.8Q and domestic supply is P = 20 + 0.8Q. The world price is $40. A tariff of $10 is imposed.</p>
  <div class="tw"><table class="t">
    <tr><th>Item</th><th>Before the tariff (price $40)</th><th>After the tariff (price $50)</th></tr>
    <tr><td>Domestic quantity demanded</td><td>(100 − 40) ÷ 0.8 = 75</td><td>(100 − 50) ÷ 0.8 = 62.5</td></tr>
    <tr><td>Domestic quantity supplied</td><td>(40 − 20) ÷ 0.8 = 25</td><td>(50 − 20) ÷ 0.8 = 37.5</td></tr>
    <tr><td>Imports</td><td>75 − 25 = 50</td><td>62.5 − 37.5 = 25</td></tr>
    <tr><td>Tariff revenue</td><td>–</td><td>$10 × 25 = $250</td></tr>
    <tr><td>Welfare loss (two triangles)</td><td>–</td><td>½ × $10 × 12.5 + ½ × $10 × 12.5 = $125</td></tr>
  </table></div>
  <ul>
    <li>Domestic firms gain from the higher price and extra output; the government gains revenue; consumers lose because they pay more and buy less. The loss to consumers exceeds the gains to producers and the government, leaving the welfare loss.</li>
  </ul>
  <p><b>Tariff versus quota.</b> A quota of 25 units would give the same fall in imports, the same rise in domestic price (to $50) and the same rise in domestic output, but the $250 would go to the importers or foreign suppliers who hold the right to sell at the higher price (quota rent), not to the government, unless licences are sold.</p>

  <h2>4 · Choosing between tools</h2>
  <div class="tw"><table class="t">
    <tr><th>Tool</th><th>Advantage</th><th>Disadvantage</th></tr>
    <tr><td><b>Tariff</b></td><td>Raises revenue; keeps the price mechanism; can be adjusted easily</td><td>Ineffective if demand for imports is inelastic; retaliation; raises costs for firms using imported inputs; rules in trade agreements</td></tr>
    <tr><td><b>Quota</b></td><td>Guarantees a maximum quantity of imports</td><td>No revenue for the government; quota rent goes to importers; may encourage corruption</td></tr>
    <tr><td><b>Export subsidy</b></td><td>Lowers costs and prices abroad so firms can undercut foreign rivals; may be less visible than a tariff</td><td>Opportunity cost for taxpayers; firms may become dependent; other countries may retaliate or complain to the WTO</td></tr>
    <tr><td><b>Embargo</b></td><td>Stops trade completely for security or political aims</td><td>Retaliation; loss of exports and cheaper imports; may encourage smuggling</td></tr>
    <tr><td><b>Administrative barriers</b></td><td>Hard to challenge and flexible</td><td>Hard to measure; may breach agreements; raise costs for businesses and consumers</td></tr>
  </table></div>

  <h2>5 · Effects on the terms of trade</h2>
  <ul>
    <li>A <b>tariff</b> raises the domestic price of imports, which can raise the measured import price index and so lower the terms of trade. If the importing country is large, the tariff may reduce demand for foreign exporters' goods so much that they cut their prices, which would improve the importer's terms of trade.</li>
    <li>If protection helps domestic firms to develop (for example infant industries), they may later raise export prices or export more, and the terms of trade could improve.</li>
    <li><b>Retaliation</b> by trading partners reduces exports, which may push export prices down and worsen the terms of trade.</li>
    <li><b>Export subsidies</b> lower export prices, which lowers the export price index and so the terms of trade, even though export volumes rise.</li>
    <li>Other tools, such as quotas or manipulating the exchange rate, can have similar effects on prices.</li>
  </ul>

  <h2>6 · Why tariffs and other tools may not work</h2>
  <ul>
    <li><b>Inelastic demand for imports:</b> consumers keep buying, so imports fall little and the trade deficit is not much reduced.</li>
    <li><b>Retaliation and trade wars:</b> other countries raise barriers against the exports of the country that protects, so everyone loses.</li>
    <li><b>Higher costs for firms:</b> producers using imported inputs face higher costs, which can raise prices and reduce competitiveness.</li>
    <li><b>Inefficiency:</b> protected firms face less competition and may have less incentive to cut costs.</li>
    <li><b>International rules:</b> membership of trade agreements can limit the use of tariffs and subsidies.</li>
    <li><b>Consumers lose:</b> higher prices and less choice, especially for poorer households.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Define protectionism first, then explain the tool's <b>mechanism</b> (price up, imports down, domestic output up). Include a limit: <b>retaliation</b>, <b>inelastic demand for imports</b>, higher costs or inefficiency.</div>
'''

watch = '''
  <h2>1 · How a tariff works</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stT"></div>
  <h2>2 · Imports under different tools</h2>
  <div id="stI"></div>
'''

explore = '''
  <h2>Lab 1 · Set the tariff</h2>
  <p>The world price is $40. Domestic demand is P = 100 − 0.8Q and domestic supply P = 20 + 0.8Q.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div>
    <div class="readout"><div><small>Domestic price and imports</small><strong id="r1"></strong></div><div><small>Tariff revenue</small><strong id="r2"></strong></div><div><small>Welfare loss</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Domestic supply and demand with a world price and a tariff, with imports shown"></svg></div></div></div>

  <h2>Lab 2 · Choose the tool</h2>
  <p>Choose a protectionist tool to see who gains, who loses and the main limit.</p>
  <div class="card"><div class="grid2"><div><div id="tB" class="btnrow"></div>
    <div class="readout"><div><small>Who gains</small><strong id="t1"></strong></div><div><small>Who loses</small><strong id="t2"></strong></div><div><small>Main limit</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 200" role="img" aria-label="A label for the chosen protectionist tool"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Is it protectionism?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the tool to its description</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effects of a tariff in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A tariff on steel", "A government puts a 25% tariff on imported steel. Steel becomes dearer, domestic steelmakers sell more and may hire more workers, but car makers and builders face higher costs, and trading partners may retaliate against the country's exports.", "a tariff's effects and costs.") +
rw("A quota on clothing", "A country allows only a fixed volume of clothing imports each year. The price of clothing rises because supply is restricted. Importers with licences earn extra profit, which does not go to the government.", "a quota and the quota rent.") +
rw("Export subsidies", "A government pays farmers for each tonne they export. Farm exports become cheaper abroad, harming foreign farmers, who may complain or retaliate, and costing taxpayers.", "export subsidies and their drawbacks.") +
rw("Red tape at the border", "Complex certification and long customs checks raise the cost and time of importing, discouraging foreign sellers without any tariff. It is hard to challenge because it is not an explicit tax.", "excessive administrative burdens.") +
rw("A trade war", "Two large economies each impose tariffs on the other's goods. Exporters in both lose sales, firms using imported parts face higher costs and consumers pay more, so many people lose even if some protected industries gain.", "retaliation and the costs of protection.") +
rw("Quotas and quota rent", "A country limits imports of sugar to a fixed amount. Importers who hold the licences can sell at the higher domestic price and earn extra profit, which does not go to the government.", "quota rent and the difference from a tariff.")
)

mc_exam = [
  mcq("m22_12", 20, "A government removes its quota on imported laptops. Assuming a normal demand curve and upward-sloping supply curve for laptops, what are the likely effects on domestic laptop manufacturers? (price received, income received)", ["price decreases, income decreases", "price increases, income increases", "price decreases, income uncertain", "price increases, income uncertain"], 0, "More imports lower the price and reduce domestic output, so income falls."),
  mcq("m22_12", 26, "What is not a form of protectionism?", ["embargoes", "increase in sales tax (VAT)", "subsidies on goods for export", "voluntary export restraints"], 1, "A general sales tax does not target imports. The others restrict imports or support exporters."),
  mcq("s20_11", 24, "What is not an example of protectionism?", ["export subsidies", "import subsidies", "quotas", "tariffs"], 1, "Subsidising imports would encourage imports."),
  mcq("s21_11", 26, "A small country imports tractors. The government decides to impose a quota on imported tractors. What is likely to be the effect on the price of imported tractors and on domestic output of tractors? (price of imported tractors, domestic output)", ["fall, fall", "increase, no change", "no change, fall", "no change, increase"], 3, "A quota restricts supply, so the price paid rises and domestic producers expand. The answer given in the paper is that import prices do not change (world price) and domestic output increases, since the country is small and the quota limits quantity."),
  mcq("s21_13", 20, "What is not an aim of protectionism?", ["to improve balance of trade", "to increase price of exports", "to protect infant industries", "to reduce the volume of imports"], 1, "Protectionism aims to cut imports and protect industries, not to raise the price of exports."),
  mcq("s21_13", 26, "Which statement about trade protection is correct?", ["A tariff results in a greater decrease in demand for an import the lower is its price elasticity of demand", "Embargoes are only an effective trade barrier when the demand for imports is price-elastic", "Export subsidies to domestic firms will prevent the dumping of foreign products in the domestic market", "Quotas are less effective than tariffs for raising government revenue"], 3, "A quota raises no tax revenue unless licences are sold, while a tariff does."),
  mcq("s22_12", 25, "A small country imposes no tariffs and has a perfectly elastic supply of smartphones from the rest of the world. Which statement is correct after the imposition of a tariff?", ["The domestic demand for smartphones will rise", "The domestic price of smartphones will rise", "The government will lose tax revenue", "The supply of imports will increase"], 1, "The tariff raises the price paid in the country by the amount of the tariff."),
  mcq("s22_12", 26, "In a recent year, Japanese car manufacturers agreed to limit exports of cars to the USA. Which form of protectionism is this?", ["an embargo", "an export subsidy", "a quota", "voluntary export restraint"], 3, "An exporters' agreement to limit sales is a voluntary export restraint."),
  mcq("s22_14", 20, "Which statement correctly describes how an import quota works?", ["It is a ban on the import of demerit goods", "It imposes strict product regulations on imports", "It is a unit tax that raises the price of imported goods", "It limits the quantity of certain imported goods"], 3, "A quota limits the quantity of imports."),
  mcq("s20_12", 29, "In 2018 the United States government introduced tariffs on a wide range of imports from China. Which type of policy was the US government adopting?", ["expenditure-reducing", "expenditure-switching", "monetary", "supply-side"], 1, "Tariffs switch spending from imports to domestically produced goods.")
]

exam = exam_page("protectionism and its tools",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Protectionist tools are an 8 or 12 mark Paper 2 part in most series (tariff versus quota, effectiveness of tariffs, export subsidies) and a 3 mark short part. Reworded past questions are below, with ten Paper 1 multiple choice questions that do not need a diagram.",
  [("Essay parts, 8 marks", "3", "Oct/Nov 2023 (21) Q5(a); May/June 2024 (22) Q5(a); Oct/Nov 2024 (23) Q5(a)"), ("Essay parts, 12 marks", "2", "May/June 2022 (21) Q4(b); May/June 2024 (23) Q5(b)"), ("Data response, 3 marks", "1", "Oct/Nov 2021 (23) Q1(c)"), ("Multiple choice (Paper 1)", "10 shown below", "2020 to 2022")],
  [
  eq(P("w23_21", "5(a)"), "8 marks", "Explain the difference between an import tariff and an import quota and consider why a government would choose an import tariff rather than an import quota as a tool of protection in international trade.",
     ["Knowledge (up to 3): the meaning of an import tariff (up to 2) and of an import quota (up to 2) as tools of protection. Maximum 3.",
      "Analysis (up to 3): the advantages and disadvantages of an import tariff (up to 2) and of an import quota (up to 2) as tools of protection. Maximum 3.",
      "Evaluation (up to 2): a valid judgement on why a government would choose a tariff rather than a quota, with a conclusion."],
     "Tariff: tax on imports. Quota: limit on quantity. Tariff: raises revenue. Quota: gives rent to importers, certainty of quantity. Judge: tariff for revenue.",
     [[("k", "An import tariff is a tax on imported goods, which raises their price. An import quota is a limit on the quantity of a good that can be imported, which restricts supply.")], [("n", "A tariff raises the price of imports and gives the government tax revenue, and the price mechanism still operates. A quota fixes the quantity of imports more precisely, but the higher price benefits importers or foreign suppliers who hold the licences, not the government, and may encourage corruption. A tariff can also be changed easily.")], [("e", "A government is likely to choose a tariff because it raises revenue and is more transparent, but if its main aim is to limit the quantity of imports exactly, a quota could be preferred. The choice depends on the government's objectives.")]]),
  eq(P("s24_22", "5(a)"), "8 marks", "Explain what is meant by the term protectionism and consider the effectiveness of using tariffs as a method of protectionism.",
     ["Knowledge (up to 3): protectionism is when governments attempt to protect domestic businesses against foreign competition (1); it seeks to reduce the impact of the free market or restrict free trade (1) by increasing the price competitiveness of domestic businesses against foreign competitors (1).",
      "Analysis (up to 3): how tariffs work (a diagram helps) by increasing the price of imports and increasing the price competitiveness of domestic businesses (up to 2); problems such as possible retaliation, inelastic demand for imports and cost-push inflationary pressure (up to 2).",
      "Evaluation (up to 2): a judgement on how effective tariffs are, with a conclusion."],
     "Define protectionism. Tariff: import price up, domestic firms more competitive. Problems: retaliation, inelastic demand, higher costs. Judge: effectiveness depends on elasticity and retaliation.",
     [[("k", "Protectionism is the use of government policy to protect domestic businesses from foreign competition. It restricts free trade and increases the price competitiveness of domestic firms against foreign rivals.")], [("n", "A tariff is a tax on imports, so it raises the price of imported goods, and domestic producers become relatively cheaper, so sales and output of domestic firms rise. But other countries may retaliate with tariffs on this country's exports, higher prices raise costs for firms that use imported inputs, and if demand for the imports is inelastic, imports fall by little.")], [("e", "Tariffs are likely to be effective when demand for imports is elastic and domestic firms can expand, but less effective if demand is inelastic or there is retaliation. They also cost consumers, who pay higher prices.")]]),
  eq(P("w24_23", "5(a)"), "8 marks", "Explain two methods of protection in international trade and consider which of these is likely to have the bigger impact on employment and output in the economy which imposes them.",
     ["Knowledge (up to 3): protectionism is when governments attempt to protect domestic businesses against foreign competition (1); an explanation of two methods, such as tariffs, import quotas, export subsidies, embargoes or red tape, and how each distorts the free market or supports domestic production (1 + 1).",
      "Analysis (up to 3): how each method affects domestic employment (1 + 1), for example tariffs raise import prices and encourage expenditure switching to domestic production, which raises employment as more workers are recruited; but if demand for imports is price inelastic, the reduction in imports may be smaller, so the effect on domestic output is smaller.",
      "Evaluation (up to 2): which method has the bigger impact on employment and output, with a conclusion."],
     "Two methods explained. Effect on employment: more domestic output and jobs, but depends on elasticity and retaliation. Judge which is bigger.",
     [[("k", "Protectionism means governments protecting domestic firms against foreign competition. A tariff is a tax on imports, which raises their price and encourages consumers to buy domestic goods. An import quota limits the quantity of imports allowed in, which restricts supply.")], [("n", "Both reduce imports and so shift spending to domestic firms, which increases their output and employment. A tariff only does this if demand for imports is elastic, since with inelastic demand the quantity of imports falls little. A quota guarantees a fall in imports to the set limit.")], [("e", "A quota is likely to have the bigger and more certain effect on domestic output and employment because it fixes the quantity of imports, but both can be offset by retaliation from trading partners and higher costs for firms using imported inputs.")]]),
  eq(P("w21_23", "1(c)"), "3 marks", "State one protectionist measure that may be adopted by a country in a trade war and explain what effect this would have on consumers and producers in that country.",
     ["A tariff, quota or regulation (maximum 1 mark for identifying one measure).", "It increases prices of imported goods for consumers (1) and raises costs of production for producers because of higher imported raw material costs (1), while it increases demand for domestic producers (1). Maximum 3 marks; 1 mark maximum for each effect, and both consumers and producers must be considered for full marks."],
     "Tariff. Consumers pay more. Domestic producers face higher input costs but gain sales.",
     [[("k", "A tariff on imports is one measure."), ("n", "Consumers face higher prices for imported goods, while producers who use imported raw materials see their costs rise, but domestic producers of competing goods sell more because imports have become dearer.")]]),
  eq(P("s22_21", "4(b)"), "12 marks", "Protectionism can take different forms in different countries. Discuss whether export subsidies are always a better method of protectionism than tariffs.",
     ["Analysis (up to 8): the advantages and disadvantages of export subsidies as a method of protectionism (up to 4): they allow firms to lower cost and price and undercut foreign competition, and are difficult for the WTO to deal with because they are not an overt method of protectionism; against that, they involve an opportunity cost in terms of other government spending and industries may become too dependent on the subsidy; the advantages and disadvantages of tariffs (up to 4): a tariff is a tax on imports making them more expensive and less competitive, if demand for imports is elastic demand should fall, and the government can use tariffs as a source of revenue; they will not be successful if demand for imports is price inelastic and may lead to retaliation.",
      "Evaluation (up to 4): a judgement on whether export subsidies are always a better method of protectionism than tariffs, with a reserved mark for a conclusion. No knowledge marks for merely defining or explaining terms used in the question."],
     "Export subsidy: lower prices abroad, hard to challenge; cost, dependence. Tariff: raises import price, revenue; inelastic demand, retaliation. Judge: not always; depends on aim and elasticities.",
     [[("n", "An export subsidy lowers firms' costs so they can cut prices abroad and undercut foreign rivals, and because it is not an overt trade barrier it may be harder for the WTO to challenge. But it costs taxpayers money that could be spent elsewhere, and firms may become dependent on it. A tariff makes imports dearer, reducing demand if it is elastic, and raises revenue for the government, but it is ineffective if demand for imports is inelastic, and may provoke retaliation.")], [("e", "Export subsidies are not always better. They help exporting industries but cost the government money, whereas tariffs raise revenue and protect the home market. Which is better depends on the aim (protecting the home market or boosting exports), the elasticities and the risk of retaliation.")]]),
  eq(P("s24_23", "5(b)"), "12 marks", "Assess the extent to which different tools of protection can impact on the terms of trade in an economy.",
     ["Analysis (up to 8): an explanation of what is meant by tools of protection; an explanation of the different tools and how they may affect the terms of trade; for example tariffs increase import prices, which will reduce the terms of trade, but may improve them if domestic producers, including infant industries, are encouraged to invest and build up demand and increase export prices; retaliation and inelastic PED for imports may reduce the positive impact; at least one additional tool, such as import quotas, embargoes or exchange rate manipulation, should be explained and analysed with its advantages and disadvantages for the terms of trade. Level 2 for a one-sided response.",
      "Evaluation (up to 4): must focus on the impact of the tools of protection on the terms of trade and lead to a justified conclusion. A one-sided response cannot gain any marks for evaluation."],
     "Tariff: import prices up, ToT down; but infant industries may raise export prices; retaliation. Quota, embargo, subsidy: also affect prices. Judge: depends on elasticity and size of country.",
     [[("n", "Tariffs raise the price of imports, which increases the import price index and so lowers the terms of trade. However, if the tariff helps infant industries to grow and later to raise export prices, the terms of trade could improve. Retaliation by trading partners would reduce exports and push export prices down, and inelastic demand for imports would limit any effect. Import quotas restrict supply and raise import prices in a similar way, while export subsidies lower export prices, which worsens the terms of trade even though export volumes rise.")], [("e", "Protection is likely to lower the terms of trade in the short run, because import prices rise or export prices fall, but its long-run effect depends on whether it helps firms to become competitive, on how large the country is, and on the reaction of other countries. The impact on the terms of trade is therefore uncertain and may be small.")]])
  ],
  )

tips = tips_html(
  [("Define protectionism.", "Protecting domestic firms from foreign competition."),
   ("Explain the mechanism.", "Import price up, imports down, domestic output up."),
   ("Draw the tariff diagram.", "World price, tariff, new quantities, revenue."),
   ("Name winners and losers.", "Producers and government gain; consumers lose."),
   ("Mention the welfare loss.", "Resources move to less efficient producers."),
   ("Tariff versus quota.", "Revenue to government versus rent to importers."),
   ("Limits.", "Retaliation, elasticity, higher costs.")],
  [("Protectionism", "Protectionism is the use of policy to protect domestic producers from foreign competition."),
   ("Tariff", "A tariff is a tax on imports that raises their price."),
   ("Quota", "A quota limits the quantity of imports."),
   ("Retaliation", "Retaliation by trading partners may reduce the effectiveness of protection."),
   ("Elasticity", "Tariffs work better if demand for imports is elastic.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = '''
/* ---------- tariff diagram ---------- */
const TX = (q) => 70 + q * 6.4, TY = (p) => 270 - p * 2.4, PW = 40;
function tarDraw(t, k) {
  const pt = PW + t, qd0 = (100 - PW) / 0.8, qs0 = (PW - 20) / 0.8, qd1 = (100 - pt) / 0.8, qs1 = (pt - 20) / 0.8; let o = axes(70, 270, 720, 25, "Quantity", "Price");
  o += SV.line(TX(0), TY(100), TX(100), TY(20), "c2", { "stroke-width": 3 }) + tag(TX(100) + 4, TY(20), "Domestic demand", "c2") + SV.line(TX(0), TY(20), TX(100), TY(100), "c1", { "stroke-width": 3 }) + tag(TX(100) + 4, TY(100), "Domestic supply", "c1");
  o += SV.line(70, TY(PW), 720, TY(PW), "dash") + tag(724, TY(PW) + 14, "World price $40", "c4", 1, "end");
  if (t > 0 && k > 0) {
    o += SV.line(70, TY(pt), 720, TY(pt), "c3", { "stroke-width": 2.5, ...op(k) }) + tag(724, TY(pt) - 6, "World price + tariff $" + pt, "c3", k, "end");
    const pl = (pts, c, v) => SV.poly(pts.map(([q, p]) => [TX(q), TY(p)]), c, op(v));
    o += pl([[qs0, PW], [qs1, pt], [0, pt], [0, PW]].slice(0, 0).concat([[0, PW], [qs0, PW], [qs1, pt], [0, pt]]), "f2", 0.5 * k);
    o += pl([[qs1, PW], [qd1, PW], [qd1, pt], [qs1, pt]], "f1", 0.6 * k);
    o += pl([[qd1, PW], [qd0, PW], [qd1, pt]], "f3", 0.6 * k) + pl([[qs0, PW], [qs1, PW], [qs1, pt]], "f3", 0.6 * k);
    o += SV.text(TX((qs1 + qd1) / 2), TY((pt + PW) / 2) + 4, "Tariff revenue", "sm", { "text-anchor": "middle", ...op(k) }) + SV.text(TX(qs1 / 2), TY((pt + PW) / 2) + 4, "Producer gain", "sm", { "text-anchor": "middle", ...op(k) });
    o += SV.circle(TX(qd1), TY(pt), 5, "dot3", op(k)) + SV.circle(TX(qs1), TY(pt), 5, "dot2", op(k)) + SV.circle(TX(qd0), TY(PW), 4, "dot1", op(0.6)) + SV.circle(TX(qs0), TY(PW), 4, "dot1", op(0.6));
    o += SV.line(TX(qs1), TY(pt) - 14, TX(qd1), TY(pt) - 14, "c4", { "stroke-width": 2, ...op(k) }) + SV.text(TX((qs1 + qd1) / 2), TY(pt) - 20, "Imports " + Lib.fmtN(qd1 - qs1, 1), "sm", { "text-anchor": "middle", ...op(k) });
  } else o += SV.line(TX(qs0), TY(PW) - 14, TX(qd0), TY(PW) - 14, "c4", { "stroke-width": 2 }) + SV.text(TX((qs0 + qd0) / 2), TY(PW) - 20, "Imports " + Lib.fmtN(qd0 - qs0, 0), "sm", { "text-anchor": "middle" });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A tariff raises the domestic price, reduces imports and creates tariff revenue and a welfare loss">${tarDraw(10, 1)}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 300, label: "A $10 tariff on imports with a world price of $40", base: { t: 0, k: 0 }, draw: (s) => tarDraw(s.t, s.k), tween: 900, dwell: 5800, steps: [
  { cap: "<b>Free trade.</b> At the world price of $40 consumers buy 75 units, domestic firms supply 25 and the other 50 are imported.", s: { t: 0, k: 0 } },
  { cap: "<b>A $10 tariff</b> raises the price in the country to $50. Domestic firms supply more (37.5) and consumers buy less (62.5), so imports fall to 25.", s: { t: 10, k: 1 } },
  { cap: "<b>Winners and losers.</b> Producers gain (green area), the government collects tariff revenue ($10 × 25 = $250), and consumers lose surplus. The two small triangles are the <b>welfare loss</b>: $62.5 + $62.5 = $125.", s: { t: 10, k: 1 } },
] });

/* ---------- imports under tools ---------- */
function toolDraw(s) {
  const Y = (v) => 250 - v * 3.2; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "Imports (units)", "sm");
  const T = [["Free trade", 50, "f1"], ["Tariff $10", 25, "f3"], ["Quota of 25", 25, "f2"], ["Red tape", 38, "f1"], ["Embargo", 0, "f3"]];
  T.forEach(([n, v, c], i) => { const k = Math.max(0, Math.min(1, s.k - i)); if (k > 0) o += SV.rect(90 + i * 120, Y(v * k + 0), 80, Math.max(2, 250 - Y(v)), c, op(0.65 * k)) + SV.text(130 + i * 120, 268, n, "sm", { "text-anchor": "middle", ...op(k) }) + SV.text(130 + i * 120, Y(v) - 6, v, "lbl bd", { "text-anchor": "middle", ...op(k) }); });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Imports under free trade, a tariff, a quota, red tape and an embargo">${toolDraw({ k: 5 })}</svg>`;
Lib.stepper($("#stI"), { w: 760, h: 290, label: "Imports under different tools of protection", base: { k: 0 }, draw: toolDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>Free trade:</b> 50 units are imported.", s: { k: 1 } },
  { cap: "<b>A tariff</b> raises the price and imports fall to 25. The government collects revenue.", s: { k: 2 } },
  { cap: "<b>A quota</b> limits imports to 25 directly. The price gap goes to importers.", s: { k: 3 } },
  { cap: "<b>Red tape</b> adds cost and delay, reducing imports a little (to 38) without any visible tax.", s: { k: 4 } },
  { cap: "<b>An embargo</b> bans trade: imports fall to zero.", s: { k: 5 } },
] });

/* ---------- Lab 1 ---------- */
function labT() {
  if (!$("#tf")) return;
  const t = +$("#tf").value, pt = PW + t, qd1 = (100 - pt) / 0.8, qs1 = (pt - 20) / 0.8, qd0 = (100 - PW) / 0.8, qs0 = (PW - 20) / 0.8, imp = qd1 - qs1, rev = t * imp, dwl = 0.5 * (qs1 - qs0) * t + 0.5 * (qd0 - qd1) * t;
  $("#r1").textContent = "$" + pt + ", " + Lib.fmtN(imp, 1); $("#r2").textContent = "$" + Lib.fmtN(rev, 0); $("#r3").textContent = "$" + Lib.fmtN(dwl, 1);
  $("#rv").textContent = t === 0 ? "No tariff: free trade at the world price of $40 with 50 units imported." : `A $${t} tariff raises the domestic price to $${pt}. Imports fall from 50 to ${Lib.fmtN(imp, 1)}, domestic output rises from 25 to ${Lib.fmtN(qs1, 1)} and consumption falls from 75 to ${Lib.fmtN(qd1, 1)}. The government collects $${Lib.fmtN(rev, 0)}. The welfare loss is $${Lib.fmtN(dwl, 1)}.${imp <= 0.5 ? " At this tariff imports are almost eliminated: a prohibitive tariff." : ""}`;
  $("#labA").innerHTML = tarDraw(t, 1);
}
Lib.slider($("#g1"), { id: "tf", label: "Tariff per unit, $ ", min: 0, max: 30, step: 5, value: 10, fmt: (v) => "$" + v, onInput: labT });
labT();

/* ---------- Lab 2 ---------- */
const TL = [["Tariff", "Government (revenue), domestic producers", "Consumers, foreign exporters", "Retaliation and higher input costs"], ["Import quota", "Domestic producers, importers with licences", "Consumers, the government (no revenue)", "Quota rent and possible corruption"], ["Export subsidy", "Exporters and their workers", "Taxpayers, foreign rivals", "Retaliation; high cost"], ["Embargo", "Domestic producers of substitutes", "Consumers and exporters", "Retaliation; political aims, not economic"], ["Red tape", "Domestic producers", "Consumers and importers", "Hard to measure and justify; may be challenged"]];
function showT(i) {
  const [n, g, l, m] = TL[i]; $$("#tB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = g; $("#t2").textContent = l; $("#t3").textContent = m; $("#tv").textContent = `${n}: it protects domestic producers by reducing import competition (or lowering export prices). The gainers are ${g.toLowerCase()}, the losers ${l.toLowerCase()}, and the main limit is ${m.toLowerCase()}.`;
  $("#labB").innerHTML = SV.rect(60, 50, 300, 90, "f3", { rx: 12, ...op(0.45) }) + SV.text(210, 105, n, "lbl bd", { "text-anchor": "middle", style: "font-size:22px" });
}
$("#tB").innerHTML = TL.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
$$("#tB button").forEach((b) => (b.onclick = () => showT(+b.dataset.i)));
showT(0);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Is it a form of protectionism?", ["Protectionism", "Not protectionism"],
  [("A tariff on imported steel", 0), ("A subsidy on imported goods", 1), ("An import quota", 0), ("A general sales tax on all goods", 1), ("An export subsidy", 0), ("A voluntary export restraint", 0), ("An embargo", 0), ("Removing import duties", 1)],
  "Protectionism restricts imports or supports exporters. Import subsidies and general taxes do not.") + MATCH([
  ["Tariff", "A tax on imports"],
  ["Quota", "A limit on the quantity of imports"],
  ["Embargo", "A ban on trade"],
  ["Export subsidy", "A payment to exporters per unit sold abroad"],
  ["Red tape", "Excessive administrative burdens on trade"],
  ["Protectionism", "Policy to protect domestic firms from foreign competition"]]) + ORDER(
  "Put the effects of a tariff in order.",
  ["The government imposes a tariff on imports", "The price of imports rises", "Imports fall and domestic firms sell more", "Domestic output and employment rise", "Consumers pay more and a welfare loss results"],
  "Tariff raises price, shifts demand to domestic goods, costs consumers.") + CALC([
  {"q": "World price $40, tariff $10 and imports after the tariff 25 units. What is tariff revenue ($)?", "a": 250, "unit": "$", "tol": 1, "hint": "10 × 25.", "sol": "<b>$250</b>."},
  {"q": "A tariff of 25% is placed on a $200 import. How much is the tariff ($)?", "a": 50, "unit": "$", "tol": 0.5, "hint": "0.25 × 200.", "sol": "<b>$50</b>."},
  {"q": "The price paid in the country is therefore ($)?", "a": 250, "unit": "$", "tol": 0.5, "hint": "200 + 50.", "sol": "<b>$250</b>."},
  {"q": "Imports fall from 50 to 25 units after the tariff. What is the % fall?", "a": 50, "unit": "%", "tol": 0.5, "hint": "25 ÷ 50.", "sol": "<b>50%</b>."}]) + MCQ([
  ("A tariff is:", ["A tax on imports", "A limit on imports", "A ban", "A subsidy"], 0, "Raises the price of imports."),
  ("An import quota:", ["Limits the quantity of imports", "Taxes imports", "Subsidises exports", "Bans all trade"], 0, "A physical limit."),
  ("A tariff will usually:", ["Raise the domestic price", "Lower the domestic price", "Raise imports", "Lower tariff revenue"], 0, "Imports become dearer."),
  ("Protectionism may provoke:", ["Retaliation", "More free trade", "Lower prices", "Lower tariffs"], 0, "Trading partners respond."),
  ("A tariff is more effective if demand for imports is:", ["Elastic", "Inelastic", "Perfectly inelastic", "Zero"], 0, "Imports fall by more.")
], "qz1") + CARDS([
  ("Protectionism", "Protect domestic firms."),
  ("Tariff", "Tax on imports."),
  ("Quota", "Limit on imports."),
  ("Export subsidy", "Pay exporters."),
  ("Embargo", "Trade ban."),
  ("Red tape", "Excessive rules."),
  ("Tariff effect", "Price up, imports down."),
  ("Limits", "Retaliation, elasticity, costs.")]) + MCQ(mc_exam)

build("as63", "as-protectionism-tools", "Protectionism and Its Tools", EY,
  "6.2.1 to 6.2.2: the meaning of protectionism and the impact of tariffs, quotas, export subsidies, embargoes and red tape. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
