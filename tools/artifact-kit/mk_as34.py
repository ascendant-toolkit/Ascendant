"""AS syllabus 3.1.3 and 3.2.4 Reasons for and effects of maximum and minimum prices. Run: python3 tools/artifact-kit/mk_as34.py"""
from asx import *
EY = EYAS("3.1.3 and 3.2.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A <b class="kw">maximum price</b> (price ceiling) is a legal limit on how <b>high</b> a price can go, used to make essentials affordable; to be <b>effective</b> it must be set <b>below the equilibrium price</b>, which creates <b>excess demand (a shortage)</b>, so goods have to be <b>rationed</b> and a <b>black market</b> may appear. A <b class="kw">minimum price</b> (price floor) is a legal limit on how <b>low</b> a price can fall, used to protect producers' incomes or discourage consumption of demerit goods; to be effective it must be <b>above the equilibrium price</b>, which creates <b>excess supply (a surplus)</b> that the government may need to buy or that wastes resources. In both cases the <b>price mechanism stops clearing the market</b>, some consumers or producers gain and others lose, and total surplus usually falls.</p></div>

  <h2>1 · Maximum prices (3.2.4)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Reasons (3.1.3):</b> make food, housing (rent control) or fuel <b>affordable for low-income households</b>; limit <b>inflation</b> in key goods; prevent <b>price gouging</b> in an emergency.</li>
    <li><b>Effect:</b> quantity demanded rises and quantity supplied falls, so there is a <b>shortage</b>. The quantity traded is the <b>smaller</b> amount supplied.</li>
    <li><b>Problems:</b> rationing by queues, waiting lists or favouritism; <b>black markets</b> where goods sell above the legal price; lower quality; <b>less incentive to supply</b>, and in the long run less investment (for example fewer rented homes).</li>
    <li><b>Winners and losers:</b> consumers who still get the good pay less; consumers who cannot buy and producers lose.</li>
    <li>A maximum price <b>at or above</b> the equilibrium has <b>no effect</b>.</li>
  </ul>

  <h2>2 · Minimum prices</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Reasons (3.1.3):</b> support <b>farmers'</b> incomes and ensure the long-run supply of food; discourage consumption of <b>demerit goods</b> such as alcohol; a <b>minimum wage</b> is a minimum price for labour.</li>
    <li><b>Effect:</b> quantity supplied rises and quantity demanded falls, so there is a <b>surplus</b>. The quantity traded is the <b>smaller</b> amount demanded.</li>
    <li><b>Problems:</b> the government may need to <b>buy up the surplus</b> (cost to taxpayers) or destroy or export it; consumers pay more and <b>consumer surplus falls</b>; producers may become <b>inefficient</b>; the policy may encourage <b>illegal selling</b> below the minimum.</li>
    <li>Producers gain if demand is <b>inelastic</b>, because revenue rises; if demand is elastic, sales fall by more and some producers lose.</li>
    <li>A minimum price <b>at or below</b> the equilibrium has <b>no effect</b>.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th></th><th>Maximum price</th><th>Minimum price</th></tr>
    <tr><td><b>Set</b></td><td>Below equilibrium</td><td>Above equilibrium</td></tr>
    <tr><td><b>Creates</b></td><td>Shortage (excess demand)</td><td>Surplus (excess supply)</td></tr>
    <tr><td><b>Quantity traded</b></td><td>Quantity supplied</td><td>Quantity demanded</td></tr>
    <tr><td><b>Typical aim</b></td><td>Affordability</td><td>Producer income, cut demerit goods</td></tr>
    <tr><td><b>Typical result</b></td><td>Rationing, black markets</td><td>Government buying, waste</td></tr>
  </table></div>

  <h2>3 · Worked examples</h2>
  <p>Demand is P = 90 − Q and supply is P = 10 + Q, so equilibrium is a price of $50 and a quantity of 40.</p>
  <div class="tw"><table class="t">
    <tr><th>Maximum price of $30</th><th>Working</th><th>Result</th></tr>
    <tr><td>Quantity demanded</td><td>90 − 30</td><td>60</td></tr>
    <tr><td>Quantity supplied</td><td>30 − 10</td><td>20</td></tr>
    <tr><td>Shortage</td><td>60 − 20</td><td>40 units</td></tr>
    <tr><td>Quantity actually traded</td><td>The lower amount</td><td>20 units</td></tr>
    <tr><td>Possible black market price</td><td>The price at which consumers would buy the 20 available units: 90 − 20</td><td>$70</td></tr>
  </table></div>
  <div class="tw"><table class="t">
    <tr><th>Minimum price of $70</th><th>Working</th><th>Result</th></tr>
    <tr><td>Quantity supplied</td><td>70 − 10</td><td>60</td></tr>
    <tr><td>Quantity demanded</td><td>90 − 70</td><td>20</td></tr>
    <tr><td>Surplus</td><td>60 − 20</td><td>40 units</td></tr>
    <tr><td>Cost if the government buys the surplus</td><td>40 × $70</td><td>$2,800</td></tr>
    <tr><td>Quantity actually traded to consumers</td><td>The lower amount</td><td>20 units</td></tr>
  </table></div>

  <h2>4 · Who gains and who loses?</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Maximum price (below equilibrium)</th><th>Minimum price (above equilibrium)</th></tr>
    <tr><td><b>Consumers</b></td><td>Those who get the good gain (lower price); those who cannot find it lose; consumer surplus changes</td><td>Pay a higher price and buy less; consumer surplus falls</td></tr>
    <tr><td><b>Producers</b></td><td>Lower price and output; producer surplus falls; less incentive to invest</td><td>Higher price; those who sell gain; but sales fall if demand is elastic and some producers cannot sell all their output</td></tr>
    <tr><td><b>Government</b></td><td>May have to enforce, ration or fund alternatives</td><td>May buy the surplus (cost) or store or export it</td></tr>
    <tr><td><b>Society</b></td><td>Welfare loss from lost trades; resources spent queuing</td><td>Welfare loss; waste of resources producing unsold output</td></tr>
  </table></div>

  <h2>5 · Special cases and elasticity</h2>
  <ul>
    <li><b>Rent controls:</b> a maximum price on rented housing. In the short run tenants gain, but over time landlords supply fewer homes or let quality fall, so shortages worsen.</li>
    <li><b>Minimum wage:</b> a minimum price for labour. Low-paid workers who stay in work gain, but if the wage is above equilibrium some workers may lose their jobs, especially if demand for labour is elastic.</li>
    <li><b>Minimum price for demerit goods:</b> for example a minimum price per unit of alcohol. It targets cheap, strong drinks, but if demand is inelastic consumption falls little, and consumers may switch to other products or buy illegally. The extra revenue goes to sellers, unlike a tax, where it goes to the government.</li>
    <li><b>Farm minimum prices:</b> support farmers' incomes and secure food supply, but create surpluses and make food dearer.</li>
    <li><b>Elasticity matters:</b> the more elastic demand and supply are, the bigger the shortage or surplus created by a control of a given size.</li>
  </ul>

  <h2>6 · Alternatives to price controls</h2>
  <ul>
    <li><b>Instead of a maximum price:</b> subsidise producers or consumers, give cash transfers to low-income households, or increase supply (for example build more homes).</li>
    <li><b>Instead of a minimum price:</b> direct income support for farmers, buffer stocks (see 3.2.5), or an indirect tax on demerit goods.</li>
    <li>These alternatives often cost the government money but avoid shortages or surpluses; price controls shift costs onto consumers or producers.</li>
  </ul>
  <div class="warn"><b class="h">Do not write this</b>A maximum price always causes a shortage. It only does so if it is set <b>below</b> the equilibrium price. The same goes for a minimum price, which only creates a surplus if it is above equilibrium. Always check where the control is set.</div>
  <div class="tip"><b class="h">Exam tip</b>Draw the control line <b>on the correct side</b> of equilibrium, mark the shortage or surplus, say who <b>gains and loses</b>, and add at least one <b>unintended consequence</b>. Then evaluate with <b>elasticity</b> and <b>alternatives</b> such as subsidies or taxes.</div>
'''

watch = '''
  <h2>1 · A maximum price creates a shortage</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stM"></div>
  <h2>2 · A minimum price creates a surplus</h2>
  <div id="stN"></div>
'''

explore = '''
  <h2>Lab 1 · Set a price control</h2>
  <p>Choose a maximum or a minimum price and set the level. The market equilibrium is $50 and 50 units.</p>
  <div class="card"><div class="grid2"><div><div id="kind" class="btnrow"></div><div id="g1"></div>
    <div class="readout"><div><small>Quantity demanded</small><strong id="r1"></strong></div><div><small>Quantity supplied</small><strong id="r2"></strong></div><div><small>Result</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Supply and demand with a price control line and the shortage or surplus"></svg></div></div></div>

  <h2>Lab 2 · The black market</h2>
  <p>A maximum price below $50. When supply is inelastic the shortage is smaller, but buyers will pay a lot more than the legal price to get the goods that exist.</p>
  <div class="card"><div class="grid2"><div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Shortage</small><strong id="t1"></strong></div><div><small>Legal price</small><strong id="t2"></strong></div><div><small>Black market price</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="Demand and supply with a legal maximum price and the price buyers would pay for the limited supply"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Effective or not?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effects of a maximum price in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Rent control", "A cap on rents below the market level makes housing cheaper for tenants who find a home. But landlords supply fewer homes and spend less on upkeep, so there is a shortage, long waiting lists and sometimes illegal side payments.", "a maximum price, shortage, rationing and a black market.") +
rw("Minimum alcohol price", "A minimum price per unit of alcohol targets the cheapest, strongest drinks. It cuts consumption among heavy drinkers if demand is elastic, but if demand is inelastic spending rises and producers gain.", "a minimum price on a demerit good and the role of elasticity.") +
rw("Farm price support", "A guaranteed minimum price for grain encourages farmers to produce. The state must buy or store the surplus, which costs taxpayers and may be dumped abroad at low prices.", "a surplus and the cost of buying it.") +
rw("Minimum wage", "A legal minimum wage is a price floor in the labour market. Low-paid workers who keep their jobs gain, but if the minimum is above the equilibrium wage employers may hire fewer workers.", "a minimum price applied to labour.") +
rw("Minimum unit pricing for alcohol", "Scotland introduced a minimum price per unit of alcohol in 2018 to reduce harmful drinking. It targets cheap, strong drinks, but the effect depends on how many drinkers respond to the higher price and on whether they switch to other products.", "a minimum price used for a demerit good.") +
rw("The minimum wage", "A legal minimum wage is a minimum price for labour. Workers on low pay who keep their jobs gain, but if it is set too high above the equilibrium wage, employers may cut jobs or hours.", "a minimum price in the labour market.")
)

mc_exam = [
  mcq("m20_12", 15, "A government imposes a maximum rent in order to make rented housing more affordable. What is likely to be a long-run consequence if the maximum is set below the current free market level?", ["a shortage of applicants for rented housing", "a shortage of rented housing", "an increase in supply to satisfy the increased demand for rented housing", "an increase in the number of houses being rented"], 1, "A rent limit below the market level discourages landlords from supplying, so there is a shortage of housing."),
  mcq("m22_12", 15, "What are the effects of a government imposing a maximum price below the equilibrium price on demand and supply?", ["demand falls, supply falls", "demand falls, supply rises", "demand rises, supply falls", "demand rises, supply rises"], 2, "The lower price extends quantity demanded and contracts quantity supplied."),
  mcq("s22_11", 14, "Which row shows the effect of a maximum price above equilibrium, a maximum price below equilibrium and a minimum price above equilibrium?", ["excess demand, no effect, no effect", "excess supply, no effect, no effect", "no effect, excess demand, excess supply", "no effect, excess supply, excess demand"], 2, "A maximum above equilibrium has no effect, one below creates excess demand, and a minimum above equilibrium creates excess supply."),
  mcq("s22_12", 15, "The demand and supply functions for a product are quantity demanded = 1500 + 50P and quantity supplied = 300P − 2000, where P is price. With government regulation, the current price in the market is $15. What can be concluded about the form of price regulation and the balance of demand and supply?", ["effective maximum price, excess demand", "effective maximum price, excess supply", "effective minimum price, excess demand", "effective minimum price, excess supply"], 3, "Equilibrium is at P = $14. At $15 quantity demanded is 2,250 and supplied 2,500, so there is excess supply, which means an effective minimum price."),
  mcq("s22_13", 17, "A government imposes a maximum price on medical face masks, below the market equilibrium. What is the most likely effect of this?", ["Some consumers will be unable to buy face masks at the maximum price", "Firms will produce more masks to meet the excess demand at the maximum price", "Poorer consumers will be able to obtain all the masks they need at the maximum price", "The market will clear at the maximum price"], 0, "A shortage means some consumers cannot buy at the capped price."),
  mcq("m21_12", 14, "After a series of poor harvests, a government imposes an effective maximum price on cereals. What would be a consequence of this policy?", ["Both rich and poor people would satisfy their demands equally", "Illegal buying and selling through a black market would be prevented", "Rationing would be necessary to ensure a fair distribution of cereals", "The market would fail to clear leaving a surplus of cereals"], 2, "A shortage means rationing is needed. A black market becomes more likely."),
  mcq("s25_13", 12, "Which statement about maximum and minimum prices is correct?", ["With an effective maximum price for a product, a shortage will develop", "With an effective maximum price for a product, the market price will rise", "With an effective minimum price for a product, rationing will be necessary", "With an effective minimum price for a product, the market price will fall"], 0, "A maximum price below equilibrium creates excess demand, a shortage.")
]

exam = exam_page("maximum and minimum prices",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Price controls are one of the most common Paper 2 topics: an 8 mark diagram part or a 12 mark discussion in nearly every series, plus short data-response parts, and they appear in Paper 1 every year. Reworded past questions are below, with seven Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "2", "Oct/Nov 2021 (21) Q3(a); May/June 2025 (24) Q3(a)"), ("Essay parts, 12 marks", "4", "Oct/Nov 2023 (21) Q3(b); Feb/March 2023 (22) Q3(b); Oct/Nov 2022 (23) Q2(b); May/June 2024 (22) Q3(b)"), ("Data response, 4 to 6 marks", "3", "Oct/Nov 2022 (21) Q1(c); Oct/Nov 2022 (21) Q1(e); May/June 2021 (23) Q1(d)"), ("Multiple choice (Paper 1)", "7 shown below", "2020 to 2025")],
  [
  eq(P("w21_21", "3(a)"), "8 marks", "With the aid of a diagram, explain the consequences for consumers and producers of introducing a minimum price in the market for a product.",
     ["Knowledge (up to 2): a correct diagram with price and quantity axes labelled (1); a minimum price shown above the equilibrium, with demand and supply labelled (1).",
      "Application (up to 3): consequences for consumers, who pay a higher price, which discourages consumption and is beneficial if the good is a demerit good.",
      "Application (up to 3): consequences for producers, whose incomes may rise, but who face excess supply because consumers do not buy at the higher price, so government action may be needed to buy up or restrict the surplus."],
     "Diagram: minimum price above equilibrium. Consumers pay more, buy less. Producers: higher price but a surplus, government may buy it.",
     [[("k", "A minimum price is a legal floor below which the price cannot fall. On a diagram it is a horizontal line above the equilibrium price, where quantity supplied exceeds quantity demanded.")], [("n", "Consumers face a higher price than in the free market, so quantity demanded falls, which would be a benefit if the product were a demerit good such as alcohol, but a cost to consumers who lose consumer surplus. Producers receive a higher price, which may raise their incomes if demand is inelastic, but not all they supply is bought, so there is excess supply. The government may have to buy the surplus, restrict output or accept waste.")]]),
  eq(P("s25_24", "3(a)"), "8 marks", "With the help of a diagram, explain the impact of introducing an effective minimum price for a product and consider the effect on the consumer surplus for that product.",
     ["Knowledge (up to 3): an accurately drawn supply and demand diagram (1); a minimum price above the equilibrium, with supply exceeding demand (1); an explanation that this leads to a surplus in the market (1).",
      "Analysis (up to 3): what is meant by consumer surplus (1); use of the diagram to show the fall in consumer surplus (1); an explanation of why consumer surplus will fall (1).",
      "Evaluation (up to 2): the overall effect on consumer surplus is that it will fall, but the extent depends on factors such as price elasticity of demand, with a justified conclusion (1)."],
     "Diagram with a minimum price above equilibrium. Surplus. Consumer surplus: smaller triangle. Evaluate: depends on PED.",
     [[("k", "On a supply and demand diagram, an effective minimum price is set above the equilibrium price. At that price quantity supplied exceeds quantity demanded, creating a surplus.")], [("n", "Consumer surplus is the difference between what consumers are willing to pay and what they pay. The higher price and the fall in quantity bought shrink the consumer surplus triangle on the diagram, so consumers are worse off.")], [("e", "Consumer surplus will fall, but by how much depends on the price elasticity of demand: if demand is inelastic, quantity falls little but consumers pay much more, while if it is elastic, quantity falls a lot. So the extent of the loss depends on elasticity and on the level of the minimum price.")]]),
  eq(P("w23_21", "3(b)"), "12 marks", "Governments sometimes fix maximum prices on goods for different reasons. Assess whether the use of a maximum price is always advantageous.",
     ["Analysis (up to 8): advantages, such as limiting the price of essential foods, making them more affordable and reducing poverty (up to 4); disadvantages, such as excess demand in the market, queuing or rationing, and the creation of a black or illegal market (up to 4).",
      "Evaluation (up to 4): the balance of advantages and disadvantages, the effect on producers and consumers, and a conclusion on whether the policy will be effective and always advantageous."],
     "Advantages: affordability, poverty. Disadvantages: shortage, rationing, black market. Evaluate: who gains, whether it works.",
     [[("n", "A maximum price below equilibrium can make essentials such as bread or rent more affordable, which helps low-income households and could reduce poverty. But it cuts the incentive to supply and raises quantity demanded, so there is excess demand. Goods must be rationed by queues or waiting lists, and a black market may appear in which the goods sell far above the legal price, harming the poorest.")], [("e", "A maximum price is not always advantageous. Those who obtain the good gain, but producers lose, and those who are unable to buy are worse off. It works best as a short-term measure in an emergency, while alternatives such as subsidies or income support might be better in the long run.")]]),
  eq(P("m23_22", "3(b)"), "12 marks", "With the help of a diagram, assess whether the introduction of a minimum price in a market can be justified.",
     ["Analysis (up to 8): a correctly labelled diagram of a minimum price above the equilibrium; the advantages, such as making demerit goods dearer to discourage consumption and protecting producers' incomes; the disadvantages and limitations, such as excess supply, reduced efficiency of producers, and why a minimum price might be ineffective. A missing diagram caps at Level 2, and a one-sided response also caps at Level 2.",
      "Evaluation (up to 4): an evaluation of the potential effectiveness of a minimum price, which may include alternative policies if the advantages and disadvantages have been discussed."],
     "Diagram. Advantages: cut demerit use, support incomes. Disadvantages: surplus, inefficiency, may be ineffective. Judge.",
     [[("n", "On the diagram a minimum price lies above the equilibrium price. It can be justified for a demerit good, because the higher price should reduce consumption, and for farm goods, because it protects producers' incomes and secures long-run supply. But at that price there is excess supply, which the government might have to buy, and producers may become less efficient because they are protected. The policy could also be ineffective if demand is inelastic, since people keep buying, or if illegal sales appear below the minimum.")], [("e", "A minimum price can be justified where the aim is clear and demand is elastic enough to change behaviour, but taxes or information may do the job at lower cost. The overall justification depends on the good and on how well the price is enforced.")]]),
  eq(P("w22_21", "1(c)"), "4 marks", "With the help of a diagram, explain how an effective minimum price would affect the market for a basic food such as rice.",
     ["A correctly labelled diagram showing a minimum price above the equilibrium (1).", "The price rises and quantity supplied rises (1).", "Quantity demanded falls (1).", "There is excess supply, which may need to be bought by the government or wasted (1)."],
     "Minimum price above equilibrium. Price up, supply up, demand down. Surplus.",
     [[("k", "An effective minimum price is a line above the equilibrium price. At that price quantity supplied rises and quantity demanded falls, so there is excess supply."), ("n", "Rice farmers receive a higher price, but consumers buy less, and the surplus rice may have to be bought by the government, stored or exported.")]]),
  eq(P("w22_23", "2(b)"), "12 marks", "Discuss the extent to which the introduction of a maximum price in a market will benefit consumers.",
     ["Analysis (up to 8): how a maximum price may benefit consumers (up to 4): it ensures access to essential products such as food, water and power, and frees up income to buy other essentials; how it may not benefit consumers (up to 4). To be effective the maximum price must be below the equilibrium price; an accurate diagram is not required but would enhance the analysis.",
      "Evaluation (up to 4): considers the extent to which consumers may benefit (up to 3), with a reasoned conclusion (1)."],
     "Benefit: affordability, access, income for other goods. Cost: shortage, rationing, black market, lower quality. Judge: depends on how far below equilibrium and who gets the goods.",
     [[("n", "A maximum price set below the equilibrium price makes essentials such as food cheaper, so low-income households can afford them and have more income left for other goods. But the lower price increases quantity demanded and reduces quantity supplied, so a shortage appears. Goods have to be rationed by queues or waiting lists, a black market may emerge with higher prices, and quality may fall as producers cut costs, so some consumers end up worse off.")], [("e", "Consumers may benefit in the short run, particularly those who can obtain the good, but the benefit is limited by shortages and by the loss of supply in the longer term. The extent depends on how far below equilibrium the price is set and how well the good is rationed. Targeted help such as subsidies or transfers could be more effective.")]]),
  eq(P("s24_22", "3(b)"), "12 marks", "Assess whether fixing a minimum price is likely to be the best policy to reduce the consumption of a demerit good.",
     ["Analysis (up to 8): use of minimum pricing to raise the price of a demerit good and reduce consumption; problems of minimum pricing, such as inelastic demand, the persistence of information failure and the emergence of informal markets; and alternative policies such as indirect taxes, education and the provision of information, with their advantages and disadvantages, including ease of introduction, time and cost and reception by consumers.",
      "Evaluation (up to 4): a judgement on whether a minimum price is likely to be the best policy, with a conclusion."],
     "Minimum price: raises price, cuts consumption if demand elastic; inelastic demand, informal markets. Alternatives: tax, education, information. Judge: a combination may be best.",
     [[("n", "A minimum price raises the price of cheap, strong products, which should reduce quantity demanded, particularly if demand is elastic. But if demand is inelastic, because the good is addictive, consumption may fall little, and the information failure that causes over-consumption remains. Informal markets may develop, and the extra revenue goes to sellers rather than the government. An indirect tax would raise revenue for the state, education and information tackle the cause of the problem but work slowly.")], [("e", "A minimum price is unlikely to be the best policy on its own. It may work for goods with elastic demand, but a combination of price measures and information is likely to be more effective at reducing consumption.")]]),
  eq(P("w22_21", "1(e)"), "6 marks", "Discuss whether maximum price controls will always be effective in controlling inflation.",
     ["Analysis (up to 5): the advantages of a maximum price (up to 3): the price will be lower than otherwise, which means a lower rate of inflation, and helps the poor afford necessities such as foodstuffs, housing rents and transport; the disadvantages (up to 3), such as lower prices stimulating demand-pull inflation elsewhere and shortages.",
      "Reserve 1 mark for a conclusion."],
     "Advantages: lower prices, affordability. Disadvantages: shortages, black markets, demand-pull pressure elsewhere. Conclude: not always effective.",
     [[("n", "A maximum price on essentials keeps their prices below the market level, which lowers measured inflation and helps poorer households to afford food and rent. But the lower price raises quantity demanded and cuts supply, causing shortages and black markets where prices may be higher, and the extra spending power left may stimulate demand-pull pressure on other prices."), ("e", "Maximum prices will not always be effective in controlling inflation: they may help in the short run but are unlikely to deal with its causes, so they are better used alongside other policies.")]]),
  eq(P("s21_23", "1(d)"), "6 marks", "Discuss whether a minimum price for fuel would be effective in reducing the congestion caused by the demand for roads exceeding supply.",
     ["Analysis (up to 5): the effect of introducing a minimum price in a market (up to 3): a minimum price above the equilibrium raises the price for drivers and in theory reduces demand and congestion; why it may not be effective (up to 3): it works only if demand for fuel is price elastic, it creates excess supply and possible informal markets, and depends on the government's ability to enforce it.",
      "Reserve 1 mark for a justified conclusion."],
     "Minimum price: higher fuel price, less driving, less congestion, but only if demand is elastic. Surplus, informal markets, enforcement. Conclude: probably limited.",
     [[("n", "A minimum price for fuel above the equilibrium raises the cost of driving, which could reduce demand for fuel and so the number of cars on the road. But fuel has few substitutes, so demand is likely to be inelastic and traffic will fall little. The policy also creates a surplus of fuel and may lead to informal markets, and it depends on the government being able to enforce the price."), ("e", "A minimum price is therefore unlikely to be effective on its own; other policies, such as better public transport or road charges, may reduce congestion more.")]])
  ],
  )

tips = tips_html(
  [("Put the line on the right side.", "Maximum below equilibrium, minimum above it."),
   ("Say effective or not.", "A control on the wrong side has no effect."),
   ("Name the result.", "Maximum: shortage. Minimum: surplus."),
   ("Quantity traded is the smaller side.", "Maximum: Qs. Minimum: Qd."),
   ("Give winners and losers.", "Consumers and producers are affected differently."),
   ("Add an unintended consequence.", "Black market, rationing, government buying, waste."),
   ("Evaluate with elasticity.", "Inelastic demand: a minimum price raises producers' revenue.")],
  [("Maximum price", "A maximum price below the equilibrium creates excess demand."),
   ("Minimum price", "A minimum price above the equilibrium creates excess supply."),
   ("Black market", "A shortage may encourage a black market."),
   ("Rationing", "Without a price signal, goods have to be rationed in another way."),
   ("Assess", "A price control may not always be advantageous, as it depends on elasticity and enforcement.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + '''
function pcDraw(s) {
  const p = s.p, qd = Math.max(0, (90 - p) / 0.8), qs = Math.max(0, (p - 10) / 0.8); let o = sdPlot({ d: 0, s: 0, g: 0 });
  o += SV.line(70, SDY(p), 720, SDY(p), "c4", { "stroke-width": 2.5, ...op(s.v) }) + tag(724, SDY(p) - 6, p < 50 ? "Max price" : "Min price", "c4", s.v, "end");
  if (s.v > 0.2 && Math.abs(qd - qs) > 1) o += SV.rect(SDX(Math.min(qd, qs)), SDY(p) - 8, Math.abs(SDX(qd) - SDX(qs)), 16, p < 50 ? "f3" : "f2", op(0.7 * s.v)) + SV.circle(SDX(qd), SDY(p), 6, "dot2", op(s.v)) + SV.circle(SDX(qs), SDY(p), 6, "dot1", op(s.v)) + tag(SDX(Math.max(qd, qs)) + 10, SDY(p) + 22, (p < 50 ? "shortage " : "surplus ") + Lib.fmtN(Math.abs(qd - qs), 0), p < 50 ? "c3" : "c2", s.v);
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A maximum price below equilibrium creates a shortage">${pcDraw({ p: 35, v: 1 })}</svg>`;
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A minimum price above equilibrium creates a surplus">${pcDraw({ p: 65, v: 1 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 300, label: "A maximum price of $35", base: { p: 35, v: 0 }, draw: pcDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The market clears at $50 and 50 units. Housing, bread and fuel are common targets for price caps.", s: { p: 35, v: 0 } },
  { cap: "<b>A maximum price of $35</b> is below equilibrium. At $35 buyers want 69 units but firms supply only 31: a <b>shortage</b> of 38.", s: { p: 35, v: 1 } },
  { cap: "<b>Only 31 units are traded.</b> They must be rationed by queues, waiting lists or contacts, and a <b>black market</b> may form where buyers pay more than $35.", s: { p: 35, v: 1 } },
] });
Lib.stepper($("#stN"), { w: 760, h: 300, label: "A minimum price of $65", base: { p: 65, v: 0 }, draw: pcDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The market clears at $50 and 50 units.", s: { p: 65, v: 0 } },
  { cap: "<b>A minimum price of $65</b> is above equilibrium. At $65 firms supply 69 units but buyers want only 31: a <b>surplus</b> of 38.", s: { p: 65, v: 1 } },
  { cap: "<b>Only 31 units are bought.</b> The government may buy the surplus (a cost to taxpayers) or it may go to waste. Consumers pay more and lose consumer surplus.", s: { p: 65, v: 1 } },
] });

/* ---------- Lab 1 ---------- */
let kd = "max";
function labP() {
  if (!$("#pc")) return;
  const p = +$("#pc").value, qd = Math.max(0, (90 - p) / 0.8), qs = Math.max(0, (p - 10) / 0.8), eff = kd === "max" ? p < 50 : p > 50, gap = Math.abs(qd - qs);
  $$("#kind button").forEach((b) => b.classList.toggle("pri", b.dataset.k === kd));
  $("#r1").textContent = Lib.fmtN(eff ? qd : 50, 0); $("#r2").textContent = Lib.fmtN(eff ? qs : 50, 0); $("#r3").textContent = !eff ? "No effect" : kd === "max" ? "Shortage " + Lib.fmtN(gap, 0) : "Surplus " + Lib.fmtN(gap, 0);
  $("#rv").textContent = !eff ? `A ${kd === "max" ? "maximum" : "minimum"} price of $${p} is ${kd === "max" ? "at or above" : "at or below"} the equilibrium of $50, so it has no effect: the market still clears at $50 and 50 units.` : kd === "max" ? `At $${p} buyers want ${Lib.fmtN(qd, 0)} units but firms supply ${Lib.fmtN(qs, 0)}, so there is a shortage of ${Lib.fmtN(gap, 0)}. Only ${Lib.fmtN(qs, 0)} are traded and they must be rationed; a black market is likely.` : `At $${p} firms supply ${Lib.fmtN(qs, 0)} units but buyers want ${Lib.fmtN(qd, 0)}, so there is a surplus of ${Lib.fmtN(gap, 0)}. Only ${Lib.fmtN(qd, 0)} are traded. If the government buys the surplus it spends $${Lib.fmtN(p * gap, 0)}.`;
  $("#labA").innerHTML = pcDraw({ p: eff ? p : 50, v: eff ? 1 : 0 }) + (eff ? "" : SV.line(70, SDY(p), 720, SDY(p), "c4", { "stroke-width": 2.5, "stroke-dasharray": "6 4" }) + tag(724, SDY(p) - 6, kd === "max" ? "Max price" : "Min price", "c4", 1, "end"));
}
$("#kind").innerHTML = `<button class="b" data-k="max">Maximum price</button><button class="b" data-k="min">Minimum price</button>`;
$$("#kind button").forEach((b) => (b.onclick = () => { kd = b.dataset.k; const el = $("#pc"); el.value = kd === "max" ? 35 : 65; el.dispatchEvent(new Event("input", { bubbles: true })); }));
Lib.slider($("#g1"), { id: "pc", label: "Controlled price, $ ", min: 20, max: 80, step: 5, value: 35, fmt: (v) => "$" + v, onInput: labP });
labP();

/* ---------- Lab 2 ---------- */
function labB() {
  if (!$("#cap") || !$("#sn")) return;
  const p = +$("#cap").value, n = +$("#sn").value / 10, qs = 50 + (p - 50) / n, qd = 50 + (50 - p) / 0.8, pb = 50 + 0.8 * (50 - qs), X = (q) => 70 + q * 6, Y = (v) => 270 - v * 2.2;
  $("#t1").textContent = Lib.fmtN(qd - qs, 0); $("#t2").textContent = "$" + p; $("#t3").textContent = "$" + Lib.fmtN(pb, 0);
  $("#tv").textContent = `With a legal maximum of $${p} firms supply only ${Lib.fmtN(qs, 0)} units and buyers want ${Lib.fmtN(qd, 0)}, a shortage of ${Lib.fmtN(qd - qs, 0)}. Buyers would pay up to $${Lib.fmtN(pb, 0)} for the last unit supplied, so a black market could charge about $${Lib.fmtN(pb - p, 0)} above the legal price. ${n >= 0.8 ? "Supply is inelastic, so the shortage is smaller but the black-market premium is large." : "Supply is elastic, so firms cut output a lot and the shortage is bigger."}`;
  let o = SV.line(70, 270, 700, 270) + SV.line(70, 270, 70, 30) + SV.line(X(0), Y(50 + 50 * 0.8), X(100), Y(50 - 50 * 0.8), "c2", { "stroke-width": 3 }) + SV.line(X(0), Y(Math.max(0, 50 - 50 * n)), X(100), Y(50 + 50 * n), "c1", { "stroke-width": 3 });
  o += SV.line(70, Y(p), X(qd), Y(p), "c4", { "stroke-width": 2.5 }) + SV.line(X(qs), Y(p), X(qs), Y(pb), "dash") + SV.line(70, Y(pb), X(qs), Y(pb), "dash") + SV.circle(X(qs), Y(pb), 6, "dot3") + SV.circle(X(qs), Y(p), 5, "dot1") + SV.circle(X(qd), Y(p), 5, "dot2");
  o += SV.text(62, Y(p) + 4, "$" + p, "sm", { "text-anchor": "end" }) + SV.text(62, Y(pb) + 4, "$" + Lib.fmtN(pb, 0), "sm", { "text-anchor": "end" });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "cap", label: "Legal maximum price, $ ", min: 20, max: 45, step: 5, value: 35, fmt: (v) => "$" + v, onInput: labB });
Lib.slider($("#g3"), { id: "sn", label: "Steepness of supply (3 = elastic, 10 = inelastic) ", min: 3, max: 10, step: 1, value: 8, fmt: (v) => v, onInput: labB });
labB();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What is the effect?", ["Shortage", "Surplus", "No effect"],
  [("Maximum price of $35, equilibrium $50", 0), ("Minimum price of $65, equilibrium $50", 1), ("Maximum price of $60, equilibrium $50", 2), ("Minimum price of $40, equilibrium $50", 2), ("Rent controlled below the market rent", 0), ("Guaranteed price for wheat above the market price", 1), ("Price cap on bread set at the market price", 2), ("Minimum price per unit of alcohol above the market price", 1)],
  "A maximum below equilibrium creates a shortage; a minimum above equilibrium creates a surplus; on the wrong side, no effect.") + MATCH([
  ["Maximum price", "A legal limit on how high a price can go"],
  ["Minimum price", "A legal limit on how low a price can go"],
  ["Black market", "Illegal trade at a price above the legal maximum"],
  ["Rationing", "Sharing out a shortage without using price"],
  ["Excess supply", "Quantity supplied exceeds quantity demanded"],
  ["Effective control", "Set on the side of equilibrium where it binds"]]) + ORDER(
  "Put the effects of a maximum price in order.",
  ["The government sets a maximum price below equilibrium", "Quantity demanded rises and quantity supplied falls", "A shortage develops", "Goods must be rationed and a black market may appear", "Some consumers gain and others cannot buy"],
  "Cap, shortage, rationing, black market.") + CALC([
  {"q": "Equilibrium price is $50. A maximum price of $35 gives Qd = 69 and Qs = 31. What is the shortage (units)?", "a": 38, "unit": "units", "tol": 0.5, "hint": "69 − 31.", "sol": "<b>38</b>."},
  {"q": "With a minimum price of $65, Qs = 69 and Qd = 31. What is the surplus?", "a": 38, "unit": "units", "tol": 0.5, "hint": "69 − 31.", "sol": "<b>38</b>."},
  {"q": "The government buys the surplus of 38 units at the minimum price of $65. What does it cost ($)?", "a": 2470, "unit": "$", "tol": 1, "hint": "65 × 38.", "sol": "<b>$2,470</b>."},
  {"q": "A cap of $35 is set. Quantity traded is the quantity supplied (31). What is consumers' spending at the legal price ($)?", "a": 1085, "unit": "$", "tol": 1, "hint": "35 × 31.", "sol": "<b>$1,085</b>."}]) + MCQ([
  ("An effective maximum price is set:", ["Below the equilibrium price", "Above the equilibrium price", "At the equilibrium price", "At the cost of production"], 0, "Below equilibrium."),
  ("An effective minimum price creates:", ["A surplus", "A shortage", "A black market", "No change"], 0, "Qs > Qd."),
  ("A likely consequence of a maximum price is:", ["A black market", "Excess supply", "Falling demand", "Lower quantity demanded"], 0, "Shortage encourages illegal trade."),
  ("Minimum prices on demerit goods aim to:", ["Reduce consumption", "Raise consumption", "Lower the price", "Shift supply right"], 0, "Higher price cuts demand."),
  ("A price control set at the equilibrium:", ["Has no effect", "Creates a shortage", "Creates a surplus", "Raises quantity"], 0, "Nothing binds.")
], "qz1") + CARDS([
  ("Maximum price", "Below equilibrium: shortage."),
  ("Minimum price", "Above equilibrium: surplus."),
  ("Quantity traded", "The smaller side."),
  ("Rationing", "Queues and waiting lists."),
  ("Black market", "Illegal sales above cap."),
  ("Surplus", "Government may buy it."),
  ("Winners", "Consumers who still get the good."),
  ("Evaluate", "Elasticity, alternatives.")]) + MCQ(mc_exam)

build("as34", "as-maximum-minimum-prices", "Maximum and Minimum Prices", EY,
  "3.1.3 and 3.2.4: why governments control prices and the effects of maximum and minimum prices, including shortages, surpluses, black markets and government buying. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
