"""Builds the four IGCSE Economics 2.9 Market failure reviews (2.9.1 to 2.9.4). Run: python3 tools/artifact-kit/mk_ig29.py"""
from igtext import *

# ---------------------------------------------------------------- 2.9.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Market failure</span> occurs when the <b>price mechanism fails to allocate resources efficiently</b>, so that society gets a <b>misallocation of resources</b>: too much of some goods, too little of others, or none at all. It means the market outcome is not the best for society as a whole.</p></div>

  <h2>What goes wrong</h2>
  <div class="tw"><table class="t">
    <tr><th>Type of failure</th><th>What happens</th><th>Example</th></tr>
    <tr><td><b>Over-provision / over-consumption</b></td><td>More is produced or consumed than is best for society</td><td>Demerit goods (cigarettes), goods with external costs (pollution)</td></tr>
    <tr><td><b>Under-provision / under-consumption</b></td><td>Less is produced or consumed than is best for society</td><td>Merit goods (education), goods with external benefits (vaccination)</td></tr>
    <tr><td><b>Non-provision</b></td><td>The market does not supply the good at all</td><td>Public goods (street lighting, national defence)</td></tr>
    <tr><td><b>Restricted supply, higher prices</b></td><td>A dominant firm limits output and charges more</td><td>Monopoly</td></tr>
  </table></div>

  <h2>Why it matters</h2>
  <ul>
    <li>Markets are efficient only if prices reflect <b>all</b> the costs and benefits to society.</li>
    <li>When they do not, there is a case for <b>government intervention</b> (see 2.10).</li>
  </ul>
  <p class="note">Market failure does not mean the market has stopped working: it means the <b>outcome is not the best use of resources</b>. Diagrams of market failure are not required at IGCSE.</p>
'''
steppers = [
  ("From market to market failure", "--bad", ["The price mechanism allocates resources", "Prices reflect only private costs and benefits", "Some costs or benefits fall on third parties", "Output is too high or too low for society", "Resources are misallocated: market failure"]),
  ("Over-consumption of a demerit good", "--warn", ["Consumers buy cigarettes at the market price", "Smoking harms smokers and others", "Consumers ignore the full harm", "More is consumed than is best for society", "Market failure: over-consumption"]),
]
lab1 = dict(title="Private and social cost", intro="Add the external cost to the private cost to find the social cost, and see how much society loses when the market ignores it.", rl=["Social cost per unit", "Total external cost", "Over-production?"],
  sliders=[("Private cost per unit ($)", 5, 50, 5, 20, "'$' + v"), ("External cost per unit ($)", 0, 30, 5, 10, "'$' + v"), ("Units produced", 10, 200, 10, 100, "v")],
  fn="const sc = v[0] + v[1], tot = v[1] * v[2]; return { r: ['$' + sc, '$' + tot, v[1] > 0 ? 'Yes' : 'No'], t: 'Private cost $' + v[0] + ' plus external cost $' + v[1] + ' gives a social cost of $' + sc + ' per unit. The firm pays only $' + v[0] + ', so over ' + v[2] + ' units society bears $' + tot + ' of external cost it never pays for. ' + (v[1] > 0 ? 'The market over-produces: this is a market failure.' : 'With no external cost, private and social costs are the same.'), bars: [['Private cost', v[0], '--accent'], ['External cost', v[1], '--bad'], ['Social cost', sc, '--warn']] };")
lab2 = dict(title="Types of market failure", intro="Pick an example to see which type of market failure it shows.", h1="Type of failure", h2="Why",
  items=[("Pollution from a factory", "Over-provision (external cost)", "The firm does not pay for the damage."), ("Cigarettes", "Over-consumption (demerit good)", "Consumers ignore the full harm."), ("Education", "Under-consumption (merit good)", "Society benefits more than the individual sees."), ("Street lighting", "Non-provision (public good)", "Firms cannot charge users."), ("A dominant water firm", "Restricted supply (monopoly)", "No rivals: higher prices."), ("Vaccination", "Under-provision (external benefit)", "Others are protected too.")])
cl = [("Is each <b>over-provided</b>, <b>under-provided</b> or <b>not provided</b> by the market?", ["Over-provided", "Under-provided", "Not provided"], [("Cigarettes", 0), ("Goods that cause pollution", 0), ("Education", 1), ("Vaccinations", 1), ("National defence", 2), ("Street lighting", 2)], "Know the three outcomes."),
      ("Is each statement about market failure <b>true</b> or <b>false</b>?", ["True", "False"], [("It is a misallocation of resources", 0), ("It can justify government intervention", 0), ("It means the market is always efficient", 1), ("It means the price mechanism has ended", 1)], "Misallocation of resources.")]
match = [["Market failure", "The price mechanism misallocates resources"], ["Misallocation", "Resources not used in the best way for society"], ["Over-consumption", "More consumed than is best for society"], ["Under-consumption", "Less consumed than is best for society"], ["Non-provision", "The market does not supply the good at all"], ["Government intervention", "Action to correct market failure"]]
order = ("Put the chain in order: <b>how an external cost leads to market failure</b>.", ["A firm produces a good that causes pollution", "The cost of the pollution falls on others", "The firm ignores it in its price", "Too much of the good is produced", "Resources are misallocated"], "A spillover leads to over-production.")
calcs = [("Private cost is $20 per unit and external cost is $8 per unit. What is the social cost per unit ($)?", 28, "20 + 8 = <b>$28</b>.", None, None), ("A firm produces 500 units each with an external cost of $4. What is the total external cost ($)?", 2000, "500 × 4 = <b>$2,000</b>.", None, None)]
mcq = [("Market failure occurs when:", ["Resources are efficiently allocated", "The price mechanism misallocates resources", "Prices fall", "Demand is zero"], 1, "Misallocation."), ("Which is an example of non-provision?", ["Cigarettes", "Street lighting", "Education", "Cars"], 1, "A public good."), ("Over-consumption is linked to:", ["Merit goods", "Demerit goods", "Public goods", "Free goods"], 1, "Demerit goods."), ("Under-consumption is linked to:", ["Demerit goods", "Merit goods", "Pollution", "Monopoly"], 1, "Merit goods."), ("Social cost equals:", ["Private cost only", "Private cost plus external cost", "External cost only", "Revenue"], 1, "Private plus external.")]
cards = [("Market failure", "When the price mechanism misallocates resources."), ("Misallocation of resources", "Resources not used in the best way for society."), ("Over-consumption", "Consuming more than is best for society."), ("Under-consumption", "Consuming less than is best for society."), ("Non-provision", "The market does not supply the good."), ("Social cost", "Private cost plus external cost."), ("Government intervention", "Government action to correct market failure."), ("Spillover", "A cost or benefit that affects a third party."), ("Externality", "Another word for spillover.")]
exam_qs = [
  Q(1, "Define", 2, "Define market failure. (May/June 2020, P22 style)", "Misallocation of resources by the price mechanism.", "[K|Market failure is when the price mechanism fails to allocate resources efficiently,] [K|leading to a misallocation of resources.]"),
  Q(2, "Explain", 4, "Explain two types of market failure.", "Over-provision, under-provision, non-provision, monopoly.", "[K|Over-consumption of demerit goods such as cigarettes is a market failure.] [N|Consumers ignore the full harm, so more is consumed than is best for society.] [K|Non-provision of public goods such as street lighting is another.] [N|Firms cannot charge users, so the market does not supply them.]"),
  Q(3, "Explain", 4, "Explain why external costs lead to market failure.", "Costs on third parties ignored; over-production.", "[K|External costs are costs that fall on third parties, such as pollution.] [N|The producer does not pay them, so the price is too low.] [N|Too much of the good is produced, so resources are misallocated.]"),
]
tips_ = [("Define market failure with 'misallocation'.", "That is the key word."), ("Name the type.", "Over, under, non-provision, monopoly."), ("Give an example.", "Cigarettes, education, street lighting."), ("Link to government intervention.", "Why it is needed.")]
real_items = [("Climate change", "Greenhouse gas emissions impose costs on the world that polluters do not pay for.", "External costs."), ("Street lights", "Private firms cannot charge for light on a public road, so councils provide it.", "Non-provision."), ("Vaccines", "People gain private protection but also protect others.", "External benefits."), ("A single local water supplier", "With no rivals, prices may be high.", "Monopoly.")]
review("ig-market-failure-definition", "mf291", "2.9.1", "Definition of Market Failure", "What market failure is and the forms it takes: over-provision, under-provision, non-provision and monopoly. Syllabus 2.9.1.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Explain"], real_items)

# ---------------------------------------------------------------- 2.9.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Market failure uses a set of key terms: <b>public goods</b>, <b>merit goods</b>, <b>demerit goods</b>, <b>private</b>, <b>external</b> and <b>social</b> costs and benefits, and <b>monopoly</b>. Learn each definition precisely, because exam questions ask for them directly.</p></div>

  <h2>Costs and benefits</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Definition</th><th>Example</th></tr>
    <tr><td><b>Private benefits</b></td><td>Benefits to the individual consumer or producer of an activity</td><td>A graduate's higher pay</td></tr>
    <tr><td><b>External benefits</b></td><td>Benefits to third parties, not the buyer or seller</td><td>Neighbours protected when others are vaccinated</td></tr>
    <tr><td><b>Social benefits</b></td><td>Private benefits + external benefits</td><td>Total benefit of education to the graduate and society</td></tr>
    <tr><td><b>Private costs</b></td><td>Costs paid by the individual consumer or producer</td><td>A firm's wage and materials bill</td></tr>
    <tr><td><b>External costs</b></td><td>Costs to third parties, not paid by the buyer or seller</td><td>Pollution harming nearby residents</td></tr>
    <tr><td><b>Social costs</b></td><td>Private costs + external costs</td><td>Total cost of a factory including pollution</td></tr>
  </table></div>

  <h2>Types of goods</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Definition</th><th>Examples</th></tr>
    <tr><td><b>Public good</b></td><td>A good that is <b>non-excludable</b> (cannot stop people using it) and <b>non-rival</b> (one person's use does not reduce another's): the market does not supply it</td><td>National defence, street lighting, lighthouses</td></tr>
    <tr><td><b>Merit good</b></td><td>A good that gives <b>more benefit</b> to society than consumers realise, so it is <b>under-consumed</b> by the market</td><td>Education, healthcare, vaccinations</td></tr>
    <tr><td><b>Demerit good</b></td><td>A good that causes <b>more harm</b> than consumers realise, so it is <b>over-consumed</b></td><td>Cigarettes, alcohol, drugs, junk food</td></tr>
    <tr><td><b>Monopoly</b></td><td>A market with a <b>single dominant seller</b> (or one with a very large share), which can restrict output and raise price</td><td>A single water supplier in an area</td></tr>
  </table></div>
  <p class="note">Public goods have the <b>free-rider problem</b>: people can enjoy them without paying, so firms cannot earn profit and do not provide them.</p>
'''
steppers = [
  ("Public goods and the free-rider problem", "--accent", ["Street lighting benefits everyone on the street", "Nobody can be excluded from using it", "Many people choose not to pay: free riders", "A private firm cannot earn profit", "The market does not supply it: the government does"]),
  ("From private to social benefit", "--good", ["A student gains from education: private benefit", "Employers and society gain too: external benefit", "Private benefit + external benefit = social benefit", "The market ignores the external part", "Education is under-consumed"]),
]
lab1 = dict(title="Social benefit of education", intro="Add the private and external benefit to find the social benefit, and see why the market under-provides.", rl=["Social benefit", "External share", "Market view"],
  sliders=[("Private benefit per student ($000)", 5, 60, 5, 30, "'$' + v + 'k'"), ("External benefit per student ($000)", 0, 60, 5, 20, "'$' + v + 'k'")],
  fn="const s = v[0] + v[1], sh = Math.round(v[1] / s * 100); return { r: ['$' + s + 'k', sh + '%', 'Sees only $' + v[0] + 'k'], t: 'A student gains $' + v[0] + 'k privately and society gains a further $' + v[1] + 'k: a social benefit of $' + s + 'k. The market takes account only of the private benefit, so too little education is bought: this is under-consumption of a merit good.', bars: [['Private benefit', v[0], '--accent'], ['External benefit', v[1], '--good'], ['Social benefit', s, '--warn']] };")
lab2 = dict(title="Which type of good?", intro="Pick a good to see its type and why.", h1="Type", h2="Why",
  items=[("Street lighting", "Public good", "Non-excludable and non-rival."), ("Education", "Merit good", "More benefit than consumers realise."), ("Cigarettes", "Demerit good", "More harm than consumers realise."), ("A private cinema ticket", "Private good", "Excludable and rival."), ("National defence", "Public good", "Protects everyone; cannot exclude."), ("A single local railway", "Monopoly", "One seller.")])
cl = [("Which <b>type of good</b> is each?", ["Public good", "Merit good", "Demerit good"], [("National defence", 0), ("Street lighting", 0), ("Education", 1), ("Vaccinations", 1), ("Cigarettes", 2), ("Alcohol", 2)], "Public, merit, demerit."),
      ("Is each a <b>private</b>, <b>external</b> or <b>social</b> cost or benefit?", ["Private", "External", "Social"], [("A firm's wage bill", 0), ("Pollution harming residents", 1), ("Total cost of production plus pollution", 2), ("A graduate's higher pay", 0), ("Neighbours protected by vaccination", 1), ("Private plus external benefit", 2)], "Private, external, social.")]
match = [["Public good", "Non-excludable and non-rival"], ["Merit good", "Under-consumed: more benefit than realised"], ["Demerit good", "Over-consumed: more harm than realised"], ["External cost", "Cost borne by third parties"], ["Social benefit", "Private plus external benefit"], ["Monopoly", "A single dominant seller"]]
order = ("Put the chain in order: <b>why public goods are not provided by the market</b>.", ["The good benefits everyone", "Nobody can be excluded", "Some people free-ride without paying", "A private firm cannot make a profit", "The market does not provide it"], "The free-rider problem.")
calcs = [("A student's private benefit is $30k and the external benefit is $20k. What is the social benefit ($k)?", 50, "30 + 20 = <b>$50k</b>.", None, None), ("A firm's private cost is $60 and the external cost is $15. What is the social cost ($)?", 75, "60 + 15 = <b>$75</b>.", None, None)]
mcq = [("A public good is:", ["Excludable and rival", "Non-excludable and non-rival", "A demerit good", "Free of charge only"], 1, "Cannot exclude; use does not reduce others'."), ("A merit good is:", ["Over-consumed", "Under-consumed", "A public good", "Always free"], 1, "More benefit than realised."), ("Which is a demerit good?", ["Education", "Cigarettes", "Street lighting", "Vaccination"], 1, "More harm than realised."), ("Social cost =", ["Private cost", "External cost", "Private cost + external cost", "Revenue − cost"], 2, "Sum."), ("A free rider:", ["Pays more", "Uses a good without paying", "Produces for free", "Owns a monopoly"], 1, "Enjoys it without paying.")]
cards = [("Public good", "A non-excludable, non-rival good that the market does not supply."), ("Merit good", "A good with more benefit than consumers realise; under-consumed."), ("Demerit good", "A good with more harm than consumers realise; over-consumed."), ("Private benefit", "Benefit to the individual buyer or seller."), ("External benefit", "Benefit to third parties."), ("Social benefit", "Private benefit plus external benefit."), ("Private cost", "Cost to the individual buyer or seller."), ("External cost", "Cost to third parties."), ("Social cost", "Private cost plus external cost.")]
exam_qs = [
  Q(1, "Define", 2, "Define a public good. (Oct/Nov 2021, P22 style)", "Non-excludable and non-rival.", "[K|A public good is non-excludable, so people cannot be stopped from using it,] [K|and non-rival, so one person's use does not reduce another's.]"),
  Q(2, "Define", 2, "Define a merit good.", "More benefit than realised; under-consumed.", "[K|A merit good is a good that gives more benefit to society than consumers realise,] [K|so it is under-consumed by the market.]"),
  Q(3, "Define", 2, "Define social costs.", "Private + external.", "[K|Social costs are the private costs] [K|plus the external costs of an activity.]"),
  Q(4, "Explain", 4, "Explain the difference between a merit good and a demerit good.", "Under- vs over-consumed.", "[K|A merit good gives more benefit than consumers realise,] [N|so it is under-consumed, such as education.] [K|A demerit good causes more harm than consumers realise,] [N|so it is over-consumed, such as cigarettes.]"),
]
tips_ = [("Learn the definitions exactly.", "Short and precise."), ("Public goods: non-excludable, non-rival.", "Free riders."), ("Social = private + external.", "For costs and benefits."), ("Use examples.", "Education, cigarettes, street lighting.")]
real_items = [("Lighthouses", "Ships cannot be excluded from using the light and one ship's use does not reduce another's.", "A public good."), ("Education", "Schooling gives individuals higher pay and society a more productive workforce.", "A merit good."), ("Tobacco", "Smoking harms health and others via passive smoking.", "A demerit good."), ("Traffic congestion", "One driver's trip raises delay for others.", "An external cost.")]
review("ig-market-failure-terms", "mf292", "2.9.2", "Definitions of Terms Associated with Market Failure", "Public goods, merit goods, demerit goods, private, external and social costs and benefits, and monopoly. Syllabus 2.9.2.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Explain"], real_items)

# ---------------------------------------------------------------- 2.9.3
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Market failure has several <b>causes</b>. Public goods are <b>not provided</b> because firms cannot charge. Merit goods and goods with external benefits are <b>under-consumed</b> because consumers undervalue the benefits. Demerit goods and goods with external costs are <b>over-consumed</b> because consumers ignore the harm. Monopoly power lets firms <b>restrict output</b> and raise prices.</p></div>

  <h2>Causes of market failure</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>Why the market fails</th></tr>
    <tr><td><b>Public goods</b></td><td>Non-excludable and non-rival: <b>free riders</b> mean firms cannot earn profit, so they do not provide them</td></tr>
    <tr><td><b>Merit goods</b></td><td>Consumers <b>lack information</b> or undervalue the benefits, and may be unable to afford them, so they buy too little</td></tr>
    <tr><td><b>Demerit goods</b></td><td>Consumers <b>underestimate the harm</b> (addiction, imperfect information), so they buy too much</td></tr>
    <tr><td><b>External costs</b></td><td>Producers or consumers <b>do not pay</b> the cost imposed on third parties (pollution, congestion), so prices are too low and output too high</td></tr>
    <tr><td><b>External benefits</b></td><td>Third parties gain without paying (vaccination, education), so prices are too high for the social benefit and output is too low</td></tr>
    <tr><td><b>Abuse of monopoly power</b></td><td>A dominant firm faces little competition, so it can <b>raise prices and restrict output</b> and may be less efficient</td></tr>
  </table></div>

  <h2>Common underlying problems</h2>
  <ul>
    <li><b>Imperfect information:</b> buyers do not know the true costs or benefits.</li>
    <li><b>Ignoring third parties:</b> the price mechanism only reflects private costs and benefits.</li>
    <li><b>Lack of competition:</b> a monopolist can set price above cost.</li>
    <li><b>Inability to charge:</b> for non-excludable goods.</li>
  </ul>
  <p class="note">In an exam, link the <b>cause</b> to the <b>market outcome</b>: say <b>who</b> ignores the cost or benefit, and what is <b>over- or under-produced</b>.</p>
'''
steppers = [
  ("Why public goods are not supplied", "--accent", ["A public good cannot exclude non-payers", "People can free-ride on others' payments", "Few choose to pay", "Firms cannot earn profit", "The market does not supply the good"]),
  ("Why demerit goods are over-consumed", "--bad", ["Consumers underestimate the harm of the good", "Addiction or imperfect information", "Demand is higher than the real benefit justifies", "More is consumed than is best for society", "Market failure: over-consumption"]),
  ("Why monopolies restrict output", "--warn", ["A firm is the only seller", "It faces no competition", "It cuts output and raises the price", "Consumers pay more and get less", "Market failure: restricted supply"]),
]
lab1 = dict(title="Abuse of monopoly power", intro="Compare a competitive market and a monopoly. Set the monopoly's price mark-up and its output cut.", rl=["Monopoly price", "Monopoly output", "Consumer loss"],
  sliders=[("Competitive price ($)", 10, 50, 5, 20, "'$' + v"), ("Monopoly mark-up (%)", 0, 100, 10, 40, "v + '%'"), ("Cut in output (%)", 0, 60, 5, 25, "v + '%'")],
  fn="const p = v[0] * (1 + v[1] / 100), q = 100 * (1 - v[2] / 100), loss = (p - v[0]) * q; return { r: ['$' + p.toFixed(0), q.toFixed(0) + ' units', '$' + loss.toFixed(0)], t: 'A competitive market sells 100 units at $' + v[0] + '. A monopoly raises the price to $' + p.toFixed(0) + ' (a ' + v[1] + '% mark-up) and cuts output to ' + q.toFixed(0) + ' units. Consumers pay an extra $' + loss.toFixed(0) + ' on the units they still buy, and ' + (100 - q).toFixed(0) + ' units are no longer bought: a market failure caused by lack of competition.', bars: [['Competitive price', v[0], '--good'], ['Monopoly price', p, '--bad'], ['Output (units ÷ 5)', q / 5, '--accent', q.toFixed(0)]] };")
lab2 = dict(title="Cause and outcome", intro="Pick a cause to see the market outcome.", h1="Outcome", h2="Why",
  items=[("Public good", "Not provided", "Free riders; no profit."), ("Merit good", "Under-consumed", "Benefits undervalued; imperfect information."), ("Demerit good", "Over-consumed", "Harm underestimated; addiction."), ("External cost", "Over-produced", "Price ignores the cost on third parties."), ("External benefit", "Under-produced", "Price ignores the benefit to third parties."), ("Monopoly", "Output restricted; higher price", "No competition.")])
cl = [("What is the market <b>outcome</b> for each?", ["Not provided", "Over-consumed", "Under-consumed"], [("Street lighting", 0), ("National defence", 0), ("Cigarettes", 1), ("Alcohol", 1), ("Education", 2), ("Vaccinations", 2)], "Public, demerit, merit."),
      ("Which <b>cause</b> explains each failure?", ["Free-rider problem", "Imperfect information", "Ignoring third parties", "Lack of competition"], [("Firms cannot charge users of street lights", 0), ("Smokers underestimate the harm", 1), ("A factory does not pay for pollution", 2), ("A monopoly raises prices", 3), ("Parents undervalue schooling", 1)], "Link cause to outcome.")]
match = [["Free-rider problem", "Using a good without paying"], ["Imperfect information", "Buyers do not know the true costs or benefits"], ["Spillover", "Cost or benefit to a third party"], ["Monopoly abuse", "Restricting output and raising price"], ["Addiction", "Makes demerit goods over-consumed"], ["Non-excludable", "Cannot stop non-payers using it"]]
order = ("Put the chain in order: <b>how a monopoly causes market failure</b>.", ["A firm is the only supplier", "It faces no competition", "It restricts output", "It raises the price", "Consumers pay more and buy less"], "Restricted supply and higher prices.")
calcs = [("A monopoly raises the price from $20 to $28. What is the percentage rise?", 40, "8 ÷ 20 × 100 = <b>40%</b>.", None, None), ("A firm's output falls from 100 to 75 units. What is the percentage fall?", 25, "25 ÷ 100 × 100 = <b>25%</b>.", None, None)]
mcq = [("Public goods are not supplied by the market because:", ["They are too cheap", "Firms cannot charge users, so no profit", "Demand is zero", "They are demerit goods"], 1, "Free riders."), ("Why are demerit goods over-consumed?", ["Consumers underestimate the harm", "Their price is too high", "They are public goods", "They are rival"], 0, "Imperfect information."), ("An external cost leads to:", ["Under-production", "Over-production", "A shortage", "Monopoly"], 1, "Prices too low."), ("A monopoly abuses power by:", ["Raising output", "Restricting output and raising price", "Cutting prices", "Increasing competition"], 1, "No rivals."), ("Merit goods are under-consumed because:", ["Consumers undervalue the benefits", "They are too harmful", "They are public goods", "Producers refuse"], 0, "Imperfect information.")]
cards = [("Free-rider problem", "People use a good without paying, so firms cannot profit."), ("Imperfect information", "Buyers do not know the full costs or benefits."), ("Externality", "A cost or benefit to a third party."), ("Over-provision", "Producing more than is best for society."), ("Under-provision", "Producing less than is best for society."), ("Restricted supply", "A monopoly limiting output."), ("Addiction", "A compulsion that keeps demand high."), ("Competition", "Rivalry that keeps prices down."), ("Abuse of monopoly power", "Using market power to raise prices and cut output.")]
exam_qs = [
  Q(1, "Explain", 4, "Explain why the market may not provide public goods.", "Non-excludable, free riders, no profit.", "[K|Public goods are non-excludable, so firms cannot stop people using them without paying.] [N|People free-ride, so firms cannot earn a profit,] [N|and therefore the market does not supply the good.]"),
  Q(2, "Explain", 4, "Explain why demerit goods may be over-consumed.", "Underestimate harm; addiction; external costs.", "[K|Consumers underestimate the harm that demerit goods cause, or are addicted.] [N|Demand is therefore higher than the real benefit justifies,] [N|so more is consumed than is best for society.]"),
  Q(3, "Analyse", 6, "Analyse why an external cost may cause market failure.", "Third parties pay; price too low; over-production.", "[K|An external cost is a cost to third parties, such as pollution.] [N|The producer does not pay it, so the price of the good only reflects private cost and is too low.] [N|Consumers buy too much and firms produce too much.] [N|Resources are over-allocated to the good, so there is market failure.] [E|The size of the failure depends on how large the external cost is.]", key=True),
  Q(4, "Analyse", 6, "Analyse how abuse of monopoly power may lead to market failure.", "Restrict output; higher prices; less choice; inefficiency.", "[K|A monopoly is the only seller, so it faces no competition.] [N|It can restrict output to raise the price.] [N|Consumers pay more and buy less than in a competitive market.] [N|With no rivals, the firm may be less efficient and innovative.] [E|The harm depends on whether there are substitutes or new entrants.]", key=True),
]
tips_ = [("Cause, then outcome.", "Say what is over or under produced."), ("Name who ignores the cost or benefit.", "Third parties."), ("Public goods: free-rider problem.", "No profit."), ("Monopoly: restricts output, raises prices.", "Explain why."), ("Use examples.", "Pollution, cigarettes, street lighting.")]
real_items = [("Plastic pollution", "Producers do not pay for the damage to oceans, so too much plastic is made.", "External cost."), ("Tobacco addiction", "Smokers keep buying despite harm.", "Demerit good."), ("Rural broadband", "Providers may not supply sparsely populated areas because profits are low.", "Under-provision."), ("Single local supplier of water", "Without competition, prices may rise.", "Monopoly power.")]
review("ig-market-failure-causes", "mf293", "2.9.3", "Causes of Market Failure", "Why the market fails: public goods, merit and demerit goods, externalities and abuse of monopoly power. Syllabus 2.9.3.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Explain", "Analyse"], real_items)

# ---------------------------------------------------------------- 2.9.4
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The <b>consequences</b> of market failure are the <b>misallocation of resources</b>: too much of some goods (demerit goods and goods with external costs), too little of others (merit goods and goods with external benefits), <b>none</b> of public goods, and <b>higher prices and restricted supply</b> under monopoly. These harm economic welfare and living standards.</p></div>

  <h2>Consequences by cause</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>Consequence</th><th>Effects on society</th></tr>
    <tr><td><b>Demerit goods and goods with external costs</b></td><td><b>Over-consumption</b> and over-production</td><td>Health damage, pollution, congestion, higher health costs for the government, wasted resources</td></tr>
    <tr><td><b>Merit goods and goods with external benefits</b></td><td><b>Under-consumption</b> and under-production</td><td>Lower skills and health, lower productivity, lower growth and living standards</td></tr>
    <tr><td><b>Public goods</b></td><td><b>Non-provision</b></td><td>Society goes without defence, street lighting and clean air unless the government steps in</td></tr>
    <tr><td><b>Monopoly power</b></td><td><b>Restricted supply and higher prices</b></td><td>Consumers pay more and get less choice; reduced real incomes; possible inefficiency</td></tr>
  </table></div>

  <h2>Wider implications</h2>
  <ul>
    <li><b>Misallocation of resources:</b> resources are not in the most beneficial use for society.</li>
    <li><b>Reduced welfare:</b> society's well-being is lower than it could be.</li>
    <li><b>Inequality:</b> poorer households suffer more from under-consumed merit goods and pollution.</li>
    <li><b>Cost to the government:</b> it may have to pay for healthcare, clean-up and regulation.</li>
    <li><b>A case for intervention:</b> governments use taxes, subsidies, regulation and provision (see 2.10).</li>
  </ul>
  <p class="note">Use phrases such as <b>over-consumption</b>, <b>under-consumption</b>, <b>non-provision</b> and <b>restricted supply causing higher prices</b> to match the syllabus language.</p>
'''
steppers = [
  ("Consequences of over-consumption", "--bad", ["Too many demerit goods are consumed", "Health problems and pollution increase", "The government spends more on healthcare and clean-up", "Productivity and living standards suffer", "Welfare is lower than it could be"]),
  ("Consequences of under-consumption", "--warn", ["Too little education or healthcare is consumed", "Workers are less skilled and less healthy", "Productivity and earnings are lower", "Growth and living standards are reduced", "Welfare is lower than it could be"]),
  ("Consequences of non-provision", "--accent", ["The market does not provide a public good", "Society goes without it", "Everyone is worse off (no defence or lighting)", "The government must provide it", "Funding comes from taxes"]),
]
lab1 = dict(title="Cost of over-consumption", intro="A demerit good is over-consumed. Set the numbers and see the extra cost to society.", rl=["Extra units consumed", "External cost to society", "Cost per household"],
  sliders=[("Socially best quantity (million units)", 10, 100, 10, 50, "v"), ("Market quantity (million units)", 10, 150, 10, 80, "v"), ("External cost per unit ($)", 1, 20, 1, 5, "'$' + v")],
  fn="const ex = Math.max(0, v[1] - v[0]), cost = ex * v[2]; return { r: [ex + 'm', '$' + cost + 'm', '$' + (cost / 10).toFixed(0)], t: 'The market consumes ' + v[1] + 'm units but the socially best quantity is ' + v[0] + 'm, so ' + ex + 'm units are over-consumed. At an external cost of $' + v[2] + ' a unit that is $' + cost + 'm of harm to society (about $' + (cost / 10).toFixed(0) + ' per household if 10 million households share it). This is the cost of misallocated resources.', bars: [['Best quantity', v[0], '--good'], ['Market quantity', v[1], '--bad'], ['Over-consumed', ex, '--warn']] };")
lab2 = dict(title="Consequences", intro="Pick a failure to see its consequence.", h1="Consequence", h2="Effect",
  items=[("Demerit goods", "Over-consumption", "Health costs; wasted resources."), ("External costs", "Over-production", "Pollution; congestion."), ("Merit goods", "Under-consumption", "Lower skills and health."), ("External benefits", "Under-production", "Society misses out."), ("Public goods", "Non-provision", "No defence or lighting without the state."), ("Monopoly", "Restricted supply, higher prices", "Consumers lose.")])
cl = [("Is each consequence <b>over-consumption</b>, <b>under-consumption</b>, <b>non-provision</b> or <b>restricted supply</b>?", ["Over-consumption", "Under-consumption", "Non-provision", "Restricted supply"], [("Too many cigarettes smoked", 0), ("Too much polluting production", 0), ("Too little education bought", 1), ("Too few people vaccinated", 1), ("No street lighting supplied", 2), ("A monopoly raises prices and cuts output", 3)], "Match the consequence."),
      ("Who is <b>harmed</b>?", ["Society", "Consumers", "Government"], [("Pollution from factories", 0), ("A dominant firm raising prices", 1), ("Higher healthcare costs from smoking", 2), ("Lower skills from low education", 0), ("Pays to clean up a spill", 2)], "Think about who bears the cost.")]
match = [["Over-consumption", "Too much of a demerit good"], ["Under-consumption", "Too little of a merit good"], ["Non-provision", "A public good is not supplied"], ["Restricted supply", "Monopoly cuts output"], ["Misallocation", "Resources not used in the best way"], ["Welfare loss", "A fall in society's well-being"]]
order = ("Put the chain in order: <b>how under-consumption of education reduces growth</b>.", ["Consumers undervalue education", "Too little education is bought", "Workers are less skilled", "Productivity is lower", "Economic growth is lower"], "Under-consumption harms growth.")
calcs = [("The market produces 80 units but the socially best level is 50. How many units are over-produced?", 30, "80 − 50 = <b>30</b>.", None, None), ("30 extra units each cause $5 of external cost. What is the total external cost ($)?", 150, "30 × 5 = <b>$150</b>.", None, None)]
mcq = [("Over-consumption is a consequence of:", ["Merit goods", "Demerit goods", "Public goods", "Monopoly"], 1, "Demerit goods."), ("Non-provision refers to:", ["Public goods", "Merit goods", "Demerit goods", "Free goods"], 0, "Public goods."), ("A monopoly leads to:", ["Lower prices", "Restricted supply and higher prices", "More competition", "No profit"], 1, "No rivals."), ("Under-consumption leads to:", ["Higher productivity", "Lower skills and health", "More pollution", "Lower prices"], 1, "Society loses benefits."), ("Misallocation of resources means:", ["Efficient use", "Resources are not used in the best way for society", "No resources", "Surplus"], 1, "Wasted potential.")]
cards = [("Misallocation of resources", "Resources not used in the best way for society."), ("Over-consumption", "Consuming more of a good than is best."), ("Under-consumption", "Consuming less than is best."), ("Non-provision", "A good is not supplied by the market."), ("Restricted supply", "A monopoly limiting output."), ("Welfare loss", "A fall in society's well-being."), ("Living standards", "The quality of life of a population."), ("Productivity", "Output per worker."), ("Government intervention", "Action to correct market failure.")]
exam_qs = [
  Q(1, "Explain", 4, "Explain two consequences of market failure.", "Over-consumption, under-consumption, non-provision, higher prices.", "[K|Demerit goods such as cigarettes are over-consumed.] [N|This harms health and raises costs for the government.] [K|Merit goods such as education are under-consumed.] [N|This leaves workers less skilled and productivity lower.]"),
  Q(2, "Explain", 4, "Explain the consequence of non-provision of public goods.", "Society goes without; government provides.", "[K|If public goods are not provided, society goes without goods such as defence and street lighting.] [N|Everyone is worse off, so the government has to provide them and fund them through taxes.]"),
  Q(3, "Analyse", 6, "Analyse the consequences of a monopoly restricting supply. (Oct/Nov 2023, P22 style)", "Higher prices, less choice, lost consumer welfare, possible inefficiency.", "[K|A monopoly restricts output to push up the price.] [N|Consumers pay more and buy less, so their real incomes and welfare fall.] [N|They also have less choice.] [N|With no competition the firm may become inefficient.] [E|The harm depends on whether substitutes exist.]", key=True),
  Q(4, "Discuss", 8, "Discuss whether market failure is a more serious problem for developing countries than for developed countries.", "Under-provision of merit/public goods; externalities; capacity to fix; judgement.", "[K|Market failure means resources are misallocated, such as under-consumption of merit goods.] [N|Developing countries often have poor health and education provision, so under-consumption is severe.] [N|They have less tax revenue to correct it.] [N|Developed countries face pollution and monopoly problems but have more resources to intervene.] [E|Overall, the impact is likely to be greater in developing countries because needs are larger and government capacity is smaller, though the type of failure differs.]", key=True),
]
tips_ = [("Use the syllabus words.", "Over-consumption, under-consumption, non-provision."), ("Say who loses.", "Society, consumers, government."), ("Link to living standards.", "Productivity, health, welfare."), ("Mention government costs.", "Healthcare, clean-up."), ("Evaluate.", "Size of the failure, capacity to fix.")]
real_items = [("Obesity and sugary drinks", "Over-consumption raises healthcare costs and reduces productivity.", "Over-consumption."), ("Low school enrolment", "Where families undervalue education, countries have lower skills.", "Under-consumption."), ("Air pollution in big cities", "Hospital admissions and lost working days rise.", "External costs."), ("Pharmaceutical monopolies", "Patent-protected medicines can be priced very high.", "Higher prices.")]
review("ig-market-failure-consequences", "mf294", "2.9.4", "Consequences of Market Failure", "The effects of market failure: over-consumption, under-consumption, non-provision and restricted supply under monopoly. Syllabus 2.9.4.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Explain", "Analyse", "Discuss"], real_items)
