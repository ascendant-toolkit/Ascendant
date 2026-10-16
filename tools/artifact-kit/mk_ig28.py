"""Builds the two IGCSE Economics 2.8 Market economic system reviews (2.8.1, 2.8.2). Run: python3 tools/artifact-kit/mk_ig28.py"""
from igtext import *

# ---------------------------------------------------------------- 2.8.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <span class="kw">market economic system</span> is an economy where <b>resources are mainly privately owned</b> and the <b>price mechanism</b>, through the decisions of consumers and firms, answers the basic economic questions of what, how and for whom to produce. Firms are motivated by <b>profit</b>, consumers by <b>satisfaction</b>, and the government has a <b>limited role</b>.</p></div>

  <h2>Key features</h2>
  <div class="tw"><table class="t">
    <tr><th>Feature</th><th>In a market economy</th></tr>
    <tr><td><b>Ownership</b></td><td>Private individuals and firms own most resources and businesses</td></tr>
    <tr><td><b>Decision-making</b></td><td>Made by millions of consumers and producers, not by the government</td></tr>
    <tr><td><b>Prices</b></td><td>Set by demand and supply: they signal, give incentives and ration</td></tr>
    <tr><td><b>Motive</b></td><td>Firms seek profit; workers seek wages; consumers seek satisfaction</td></tr>
    <tr><td><b>Competition</b></td><td>Firms compete for customers, which keeps prices low and quality high</td></tr>
    <tr><td><b>Consumer sovereignty</b></td><td>Consumers' spending decides what is produced</td></tr>
    <tr><td><b>Government</b></td><td>Limited: law and order, property rights, defence</td></tr>
  </table></div>

  <h2>How it answers the three questions</h2>
  <ul>
    <li><b>What</b> to produce: whatever consumers will pay for at a profit.</li>
    <li><b>How</b> to produce: the cheapest efficient method, as firms compete on cost.</li>
    <li><b>For whom</b> to produce: those <b>willing and able to pay</b>.</li>
  </ul>
  <p class="note">No country has a pure market economy: even the most market-oriented economies have some government provision, regulation and taxation, so they are better described as <b>mixed</b>.</p>
'''
steppers = [
  ("How the market answers 'what to produce'", "--accent", ["Consumers spend more on a good", "Its price and profit rise", "Firms, seeking profit, produce more of it", "Resources move into the good", "Consumer sovereignty decides what is produced"]),
  ("Competition and efficiency", "--good", ["A firm charges a high price and earns high profit", "Rival firms enter and compete for customers", "Firms cut prices and improve quality", "Consumers benefit from lower prices and better products", "Competition pushes firms towards efficiency"]),
]
lab1 = dict(title="How market-based is the economy?", intro="Set three features of an economy and see where it sits between a market and a planned system.", rl=["Market score", "Classification", "Government share"],
  sliders=[("Share of production in private hands", 0, 100, 10, 80, "v + '%'"), ("Freedom of prices (set by demand and supply)", 0, 100, 10, 80, "v + '%'"), ("Government role in decisions", 0, 100, 10, 20, "v + '%'")],
  fn="const s = Math.round((v[0] + v[1] + (100 - v[2])) / 3); const c = s >= 80 ? 'Market economy' : s >= 40 ? 'Mixed economy' : 'Planned economy'; return { r: [s + '/100', c, v[2] + '%'], t: 'Private ownership ' + v[0] + '%, price freedom ' + v[1] + '% and a government role of ' + v[2] + '% give a market score of ' + s + ': ' + c.toLowerCase() + '. A pure market economy would score near 100; in practice most economies are mixed.', bars: [['Private ownership', v[0], '--accent'], ['Price freedom', v[1], '--good'], ['Government role', v[2], '--warn']] };")
lab2 = dict(title="Features of a market economy", intro="Pick a feature to see what it means.", h1="Feature", h2="Meaning",
  items=[("Private ownership", "Individuals and firms own resources", "Decisions are made by owners seeking profit."), ("Price mechanism", "Prices signal and ration", "Prices adjust to demand and supply."), ("Profit motive", "Firms aim for profit", "Profit is the reward for taking risks."), ("Consumer sovereignty", "Consumers decide what is made", "Spending acts like votes."), ("Competition", "Firms rival each other", "Keeps prices down and quality up."), ("Limited government", "The state does little", "Law, property rights and defence.")])
cl = [("Is each a feature of a <b>market economy</b> or a <b>planned economy</b>?", ["Market economy", "Planned economy"], [("Private ownership of resources", 0), ("Prices set by demand and supply", 0), ("Profit motive", 0), ("Competition between firms", 0), ("Government decides output", 1), ("State ownership of most resources", 1), ("Central planners set prices", 1)], "Market: private and price-led."),
      ("Which <b>question</b> does each answer?", ["What to produce", "How to produce", "For whom to produce"], [("Consumers spend more on organic food", 0), ("Firms switch to cheaper machines", 1), ("Goods go to those willing and able to pay", 2), ("Resources move to high-profit goods", 0), ("Competition forces cost-cutting methods", 1)], "What, how, for whom.")]
match = [["Market economy", "Prices and private decisions allocate resources"], ["Consumer sovereignty", "Consumers' spending decides what is produced"], ["Profit motive", "Firms' aim of earning profit"], ["Price mechanism", "Prices adjusting to demand and supply"], ["Competition", "Rivalry between firms for customers"], ["Private ownership", "Resources owned by individuals and firms"]]
order = ("Put the chain in order: <b>how competition benefits consumers</b>.", ["Firms compete for customers", "Firms cut prices or improve quality", "Consumers benefit from lower prices and better quality", "Inefficient firms lose customers", "Firms become more efficient"], "Competition drives efficiency.")
calcs = [("A market has a score of (80 + 70 + 90) ÷ 3 on three features. What is the average?", 80, "240 ÷ 3 = <b>80</b>.", None, None), ("A firm's revenue is $500,000 and costs are $420,000. What is profit ($)?", 80000, "500,000 − 420,000 = <b>$80,000</b>.", None, None)]
mcq = [("In a market economy, resources are allocated mainly by:", ["The government", "The price mechanism", "Planners", "Trade unions"], 1, "Prices."), ("Consumer sovereignty means:", ["The government decides", "Consumers' spending decides what is produced", "Firms decide alone", "Prices are fixed"], 1, "Consumers have the power."), ("Firms in a market economy are motivated by:", ["Social welfare only", "Profit", "Taxes", "Planning"], 1, "Profit motive."), ("Which is a feature of a market economy?", ["State ownership of most firms", "Competition between firms", "Central planning", "Fixed prices"], 1, "Competition."), ("No country has a pure market economy because:", ["Governments always play some role", "Prices do not exist", "Firms are banned", "Wants are limited"], 0, "Most are mixed.")]
cards = [("Market economic system", "An economy where resources are mainly privately owned and allocated by the price mechanism."), ("Price mechanism", "Prices adjusting to allocate resources."), ("Consumer sovereignty", "Consumers' spending decides what is produced."), ("Profit motive", "Firms' aim of earning profit."), ("Competition", "Rivalry between firms for customers."), ("Private ownership", "Resources owned by individuals and firms."), ("Free market", "A market with little government interference."), ("Planned economy", "An economy where the government allocates resources."), ("Mixed economy", "An economy combining market and government decision-making.")]
exam_qs = [
  Q(1, "Define", 2, "Define a market economic system.", "Resources allocated by the price mechanism.", "[K|A market economic system is an economy in which resources are allocated by the price mechanism] [K|with mainly private ownership and little government intervention.]"),
  Q(2, "Identify", 2, "Identify two features of a market economic system.", "Private ownership, price mechanism, profit motive, competition.", "[K|Private ownership of resources.] [K|Prices set by demand and supply (or competition between firms).]"),
  Q(3, "Explain", 4, "Explain how a market economic system answers the question 'what to produce'.", "Demand, price, profit, resource movement.", "[K|Consumers' spending shows what they want.] [N|When demand for a good rises, its price and profit rise,] [N|so firms produce more of it and resources move into that market.]"),
  Q(4, "Explain", 4, "Explain what is meant by consumer sovereignty.", "Consumers decide what is produced by spending.", "[K|Consumer sovereignty means consumers decide what is produced.] [N|Firms produce what consumers spend on, because that is profitable,] [N|and stop producing goods that consumers will not buy.]"),
]
tips_ = [("Ownership, prices, profit, competition.", "The four features to remember."), ("Link to what, how, for whom.", "Use the price mechanism."), ("No pure market economy exists.", "Most are mixed."), ("Say 'consumer sovereignty'.", "A key term.")]
real_items = [("Hong Kong and Singapore", "Often described as among the most market-oriented economies, with low taxes and open trade, though governments still provide services.", "Market-oriented economies."), ("Online shopping", "Thousands of sellers compete on price and quality, and consumers choose freely.", "Competition and consumer choice."), ("Uber and ride apps", "Prices rise with demand, attracting more drivers.", "The price mechanism."), ("Fast fashion", "Producers respond to fashion trends quickly to catch consumer demand.", "Consumer sovereignty.")]
review("ig-market-system", "m281", "2.8.1", "Definition of the Market Economic System", "What a market economy is, its key features and how it answers the basic economic questions. Syllabus 2.8.1.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Identify", "Explain"], real_items)

# ---------------------------------------------------------------- 2.8.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The market economic system has <b>advantages</b>, mainly <b>efficiency, choice and innovation</b>, and <b>disadvantages</b>, mainly <b>inequality, market failure and instability</b>. To evaluate it, weigh both and conclude. The strength of each depends on the good (a luxury or a necessity) and on the people affected.</p></div>

  <div class="grid2">
    <div class="card"><h3>Advantages</h3><ul>
      <li><b>Efficiency:</b> competition pushes firms to cut costs and use resources well</li>
      <li><b>Consumer choice and sovereignty:</b> firms produce what consumers want</li>
      <li><b>Innovation:</b> profit rewards new products and methods</li>
      <li><b>Flexible response:</b> prices adjust quickly to changes in demand and supply</li>
      <li><b>Incentives to work and take risks:</b> rewards for effort and enterprise</li>
      <li><b>Low administration costs:</b> no large planning bureaucracy</li>
    </ul></div>
    <div class="card"><h3>Disadvantages</h3><ul>
      <li><b>Inequality:</b> goods go to those who can pay, so low-income households go without</li>
      <li><b>Under-provision of public and merit goods</b> (street lighting, education)</li>
      <li><b>Over-provision of demerit goods</b> and <b>external costs</b> such as pollution</li>
      <li><b>Monopoly power:</b> a dominant firm may raise prices and restrict output</li>
      <li><b>Instability:</b> booms and recessions, unemployment</li>
      <li><b>Neglect of unprofitable goods</b> and some regions</li>
    </ul></div>
  </div>

  <h2>Evaluating the market system</h2>
  <ul>
    <li>It works well for goods where <b>competition</b> is strong and there are few external effects.</li>
    <li>It performs poorly for goods with <b>spillovers</b> or where consumers lack information.</li>
    <li>This is why most countries <b>mix</b> market forces with government intervention (see 2.10).</li>
  </ul>
  <p class="note">A good evaluation says <b>what the system does well</b>, <b>what it does badly</b>, and a <b>judgement</b> depending on circumstances.</p>
'''
steppers = [
  ("Why the market can lead to inequality", "--bad", ["Goods are allocated to those willing and able to pay", "Low-income households have little purchasing power", "They cannot afford essentials such as healthcare", "Firms supply those who can pay, not those with the greatest need", "Inequality of outcomes"]),
  ("Why the market encourages innovation", "--good", ["Profit rewards successful new products", "Firms invest in research and new methods", "New products and cheaper methods appear", "Consumers gain more choice and lower prices", "Living standards may rise"]),
  ("Why the market ignores external costs", "--warn", ["A firm produces and pollutes a river", "The cost of the pollution falls on society", "The firm ignores it in its decisions", "Too much of the good is produced", "Resources are misallocated: market failure"]),
]
lab1 = dict(title="Weigh the market system", intro="Rate how well a market economy performs on four aims. See the overall verdict.", rl=["Average score", "Strongest aim", "Weakest aim"],
  sliders=[("Efficiency", 1, 10, 1, 8, "v"), ("Choice and innovation", 1, 10, 1, 8, "v"), ("Fairness (equity)", 1, 10, 1, 3, "v"), ("Environment and public goods", 1, 10, 1, 3, "v")],
  fn="const nm = ['Efficiency', 'Choice and innovation', 'Fairness', 'Environment/public goods'], avg = (v.reduce((a, b) => a + b, 0) / 4).toFixed(1), hi = nm[v.indexOf(Math.max(...v))], lo = nm[v.indexOf(Math.min(...v))]; return { r: [avg + '/10', hi, lo], t: 'A market economy tends to score well on efficiency and choice but worse on fairness and the environment. Your scores average ' + avg + '/10, with ' + hi.toLowerCase() + ' strongest and ' + lo.toLowerCase() + ' weakest. A balanced evaluation weighs these and may favour government action where the weakest aim matters most.', bars: nm.map((n, i) => [n, v[i], ['--accent', '--good', '--warn', '--bad'][i]]) };")
lab2 = dict(title="Strengths and weaknesses", intro="Pick a topic to see how the market system performs.", h1="Strength", h2="Weakness",
  items=[("Efficiency", "Competition keeps costs and prices down", "Monopolies may raise prices."), ("Choice", "Firms supply what consumers want", "Only for those who can pay."), ("Innovation", "Profit rewards new ideas", "Some research (e.g. for rare diseases) is unprofitable."), ("Fairness", "Rewards effort", "Inequality; low-income households go without."), ("Environment", "Prices can reflect scarcity", "External costs are ignored."), ("Stability", "Prices adjust to shocks", "Booms, recessions and unemployment.")])
cl = [("Is each an <b>advantage</b> or a <b>disadvantage</b> of the market system?", ["Advantage", "Disadvantage"], [("Efficiency through competition", 0), ("Consumer choice", 0), ("Innovation", 0), ("Inequality", 1), ("Neglect of public goods", 1), ("Pollution and external costs", 1)], "Weigh both."),
      ("Which <b>problem</b> does each describe?", ["Inequality", "Market failure", "Monopoly power"], [("Poor households cannot afford healthcare", 0), ("Factory pollution not paid for by the firm", 1), ("A dominant firm restricts output", 2), ("Street lighting is not provided by firms", 1), ("A firm raises prices because it has no rivals", 2)], "Know the weaknesses.")]
match = [["Efficiency", "Using resources well at low cost"], ["Inequality", "Unequal distribution of income and goods"], ["Innovation", "New products and methods"], ["External cost", "A cost to third parties"], ["Monopoly", "A dominant single seller"], ["Public good", "A good the market under-provides"]]
order = ("Put the chain in order: <b>how profit leads to innovation</b>.", ["Firms see a chance of higher profit", "They invest in research and new methods", "New products appear", "Consumers gain more choice", "Firms with good ideas earn profit"], "Incentives drive innovation.")
calcs = [("A firm spends $2m on research and earns $5m extra revenue from the new product. What is the net gain ($m)?", 3, "5 − 2 = <b>$3m</b>.", None, None), ("Income of the richest 10% is $40bn of a $100bn total. What percentage is that?", 40, "40 ÷ 100 × 100 = <b>40%</b>.", None, None)]
mcq = [("An advantage of the market system is:", ["Inequality", "Efficiency through competition", "Under-provision of public goods", "Monopoly"], 1, "Competition."), ("A disadvantage is:", ["Consumer choice", "Innovation", "Ignoring external costs", "Low administration costs"], 2, "Spillovers are ignored."), ("Public goods are under-provided because:", ["They are unprofitable for private firms", "They are too cheap", "They are banned", "Consumers dislike them"], 0, "No profit."), ("The market system rewards risk-taking through:", ["Taxes", "Profit", "Subsidies", "Quotas"], 1, "Incentive."), ("A reason many countries use a mixed system:", ["Markets fail in some areas", "Markets are perfect", "Prices do not exist", "Planned economies are always better"], 0, "To correct failures.")]
cards = [("Efficiency", "Using resources well, with little waste."), ("Inequality", "An unequal distribution of income or goods."), ("Innovation", "The introduction of new products or methods."), ("External cost", "A cost to third parties not paid by the producer."), ("Public good", "A good that markets under-provide."), ("Monopoly", "A single dominant seller."), ("Merit good", "A good that markets under-consume."), ("Demerit good", "A good that markets over-consume."), ("Instability", "Fluctuations in output and employment.")]
exam_qs = [
  Q(1, "Explain", 4, "Explain two advantages of a market economic system.", "Efficiency, choice, innovation.", "[K|Competition between firms encourages efficiency] [N|so costs and prices are kept low.] [K|Consumers have a wide choice of goods] [N|because firms produce what consumers demand in order to earn profit.]"),
  Q(2, "Explain", 4, "Explain two disadvantages of a market economic system.", "Inequality, under-provision of public goods, externalities, monopoly.", "[K|Goods go to those who can afford them,] [N|so low-income households may go without essentials.] [K|The market ignores external costs] [N|such as pollution, leading to over-production of some goods.]"),
  Q(3, "Discuss", 8, "Discuss whether a market economic system is the best way to allocate a country's resources.", "Efficiency, choice, innovation vs inequality, externalities, public goods. Judgement.", "[K|In a market system the price mechanism allocates resources.] [N|Competition encourages efficiency and innovation, and consumers get what they want.] [N|There is little government cost and workers and firms are rewarded for effort.] [E|However, the market gives goods to those who can pay, so inequality can be large.] [N|It ignores external costs and under-provides public goods such as defence.] [E|Monopoly power can also raise prices.] [E|Overall, the market is good at efficiency but poor on fairness and the environment, so most countries need government intervention as well.]", key=True),
]
tips_ = [("Weigh both sides.", "Then give a judgement."), ("Use pairs: efficiency vs equity.", "Clear contrasts."), ("Link to market failure.", "Externalities, public goods, monopoly."), ("Use 'depends on' evaluation.", "The type of good matters."), ("Most countries are mixed.", "A final judgement.")]
real_items = [("Healthcare in the US", "Private provision gives choice and innovation but millions struggle to afford cover.", "Efficiency vs equity."), ("Smartphone industry", "Fierce competition has driven rapid innovation and falling prices.", "Advantages of competition."), ("Pollution from factories", "Firms that do not pay for pollution may produce too much.", "External costs."), ("Pharmaceutical research", "Firms invest in profitable drugs but neglect rare diseases.", "Market neglects unprofitable goods.")]
review("ig-market-system-evaluation", "m282", "2.8.2", "Arguments For and Against the Market Economic System", "Advantages and disadvantages of the market economic system and how to evaluate them. Syllabus 2.8.2.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Explain", "Discuss"], real_items)
