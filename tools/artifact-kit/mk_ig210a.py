"""Builds IGCSE Economics 2.10.1 and 2.10.2 (mixed economic system). Run: python3 tools/artifact-kit/mk_ig210a.py"""
from igtext import *

# ---------------------------------------------------------------- 2.10.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <span class="kw">mixed economic system</span> combines the <b>private sector</b> (the market, with firms and consumers) and the <b>public sector</b> (the government). Resources are allocated partly by the <b>price mechanism</b> and partly by <b>government decisions</b>. Almost every real economy is mixed; they differ in <b>how much</b> of each they use.</p></div>

  <h2>Market, planned and mixed</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Market economy</th><th>Planned economy</th><th>Mixed economy</th></tr>
    <tr><td><b>Who decides</b></td><td>Consumers and firms</td><td>The government</td><td>Both</td></tr>
    <tr><td><b>Ownership</b></td><td>Private</td><td>State</td><td>Private and state</td></tr>
    <tr><td><b>Prices</b></td><td>Set by demand and supply</td><td>Set by the government</td><td>Mostly by the market; some regulated</td></tr>
    <tr><td><b>Examples (leaning)</b></td><td>Hong Kong, Singapore (market-leaning)</td><td>North Korea, Cuba (plan-leaning)</td><td>UK, Germany, India, most countries</td></tr>
  </table></div>

  <h2>What the public and private sectors do</h2>
  <div class="grid2">
    <div class="card"><h3>Private sector</h3><ul><li>Most goods and services: food, cars, clothes, phones</li><li>Driven by profit and competition</li><li>Owned by individuals and shareholders</li></ul></div>
    <div class="card"><h3>Public sector</h3><ul><li>Public goods (defence, street lighting)</li><li>Merit goods (education, healthcare)</li><li>Regulation, taxation and welfare benefits</li><li>Owned and run by the state</li></ul></div>
  </div>
  <p class="note">The balance varies: some mixed economies are more market-based (the US), others rely more on the state (the Nordic countries). The public sector often exists to correct <b>market failure</b>.</p>
'''
steppers = [
  ("What the government adds to the market", "--accent", ["The market supplies most private goods", "It fails to supply public goods and under-supplies merit goods", "The government provides or funds them", "It also regulates and taxes to correct market failure", "A mixed economy: market plus government"]),
  ("From market to mixed", "--good", ["A market economy allocates by prices", "Market failure appears: pollution, inequality, monopoly", "Governments intervene with taxes, subsidies and rules", "They also provide some goods directly", "The economy becomes mixed"]),
]
lab1 = dict(title="How mixed is the economy?", intro="Set the public sector's share of three activities and see where the economy sits between market and planned.", rl=["Public share", "Classification", "Private share"],
  sliders=[("State ownership of firms", 0, 100, 10, 20, "v + '%'"), ("Government spending as a share of GDP", 0, 100, 10, 40, "v + '%'"), ("Prices set by government", 0, 100, 10, 10, "v + '%'")],
  fn="const s = Math.round((v[0] + v[1] + v[2]) / 3), c = s >= 80 ? 'Planned economy' : s >= 15 ? 'Mixed economy' : 'Close to a pure market', pv = 100 - s; return { r: [s + '%', c, pv + '%'], t: 'With state ownership ' + v[0] + '%, government spending ' + v[1] + '% and price control ' + v[2] + '%, the public sector share averages ' + s + '%: ' + c.toLowerCase() + '. Most real economies sit in the middle, with the balance between the private and public sectors varying by country.', bars: [['State ownership', v[0], '--accent'], ['Government spending', v[1], '--warn'], ['Price control', v[2], '--bad']] };")
lab2 = dict(title="Public or private?", intro="Pick a good or service to see who normally provides it in a mixed economy.", h1="Usually provided by", h2="Why",
  items=[("National defence", "Public sector", "A public good; free riders."), ("Smartphones", "Private sector", "Profitable; competitive."), ("State schools", "Public sector", "A merit good; funded by taxes."), ("Restaurants", "Private sector", "Private good."), ("Street lighting", "Public sector", "Public good."), ("Healthcare", "Both", "Public hospitals and private clinics.")])
cl = [("Is each usually <b>public sector</b> or <b>private sector</b>?", ["Public sector", "Private sector"], [("National defence", 0), ("State schools", 0), ("Street lighting", 0), ("Supermarkets", 1), ("Car manufacturers", 1), ("Fashion shops", 1)], "Who provides what."),
      ("Is each a feature of a <b>market</b>, <b>planned</b> or <b>mixed</b> economy?", ["Market", "Planned", "Mixed"], [("Prices set by demand and supply only", 0), ("Government decides all output", 1), ("Private firms and state-run services", 2), ("Profit motive and public hospitals", 2), ("State owns all resources", 1), ("Little government intervention", 0)], "Know the three systems.")]
match = [["Mixed economy", "Market and government both allocate resources"], ["Public sector", "The part of the economy run by the government"], ["Private sector", "Firms and households owned privately"], ["Market economy", "Allocation mainly by prices"], ["Planned economy", "Allocation by the government"], ["Market failure", "A reason for government involvement"]]
order = ("Put the chain in order: <b>why governments get involved in the market</b>.", ["Markets fail to supply public goods", "Some goods are over- or under-consumed", "Governments intervene with taxes, subsidies or rules", "They provide some goods directly", "The economy becomes mixed"], "Market failure justifies intervention.")
calcs = [("Government spending is $40bn and GDP is $100bn. What percentage of GDP is government spending?", 40, "40 ÷ 100 × 100 = <b>40%</b>.", None, None), ("The private sector produces 65% of output. What percentage is produced by the public sector?", 35, "100 − 65 = <b>35%</b>.", None, None)]
mcq = [("A mixed economy is one where:", ["Only the government decides", "Both the market and the government allocate resources", "Only firms decide", "There are no prices"], 1, "A mix."), ("Which is usually provided by the public sector?", ["Smartphones", "National defence", "Fashion", "Restaurants"], 1, "Public good."), ("Most economies are:", ["Pure market", "Pure planned", "Mixed", "Barter"], 2, "Mixed."), ("The private sector is motivated by:", ["Profit", "Social welfare only", "Taxes", "Quotas"], 0, "Profit motive."), ("Governments intervene mainly to:", ["Correct market failure", "Ban prices", "Remove competition", "Create unemployment"], 0, "Market failure.")]
cards = [("Mixed economic system", "An economy where both the market and the government allocate resources."), ("Public sector", "The part of the economy owned and run by the government."), ("Private sector", "The part owned by individuals and firms."), ("Market economy", "Allocation mainly by the price mechanism."), ("Planned economy", "Allocation by government decisions."), ("Public good", "A non-excludable, non-rival good."), ("Merit good", "Under-consumed good with extra benefits."), ("Regulation", "Government rules on firms."), ("Market failure", "Misallocation of resources by the market.")]
exam_qs = [
  Q(1, "Define", 2, "Define a mixed economic system.", "Both market and government.", "[K|A mixed economic system is one in which resources are allocated partly by the market (private sector)] [K|and partly by the government (public sector).]"),
  Q(2, "Explain", 4, "Explain the roles of the public sector and private sector in a mixed economy.", "Private: profit goods; public: public and merit goods, regulation.", "[K|The private sector provides most goods and services,] [N|driven by profit and competition.] [K|The public sector provides public goods and merit goods such as defence and education,] [N|and regulates and taxes to correct market failure.]"),
  Q(3, "Explain", 4, "Explain why most countries have a mixed economic system.", "Markets fail; planned economies inefficient.", "[K|A pure market economy ignores public goods, external costs and inequality,] [N|so governments need to step in.] [K|A fully planned economy is often inefficient and lacks choice,] [N|so most countries combine the strengths of both.]"),
]
tips_ = [("Mixed = market + government.", "Say both."), ("Public vs private examples.", "Defence vs smartphones."), ("Link to market failure.", "The reason for government."), ("Countries differ in the balance.", "Use examples.")]
real_items = [("The UK", "Private firms supply most goods while the NHS and state schools are public.", "A mixed economy."), ("Sweden", "High taxes fund a large public sector, yet private firms are important.", "A government-heavy mix."), ("The US", "More market-based, though government funds defence, Medicare and more.", "A market-leaning mix."), ("China", "State-owned firms operate alongside a large private sector.", "A mixed system.")]
review("ig-mixed-system", "x2101", "2.10.1", "Definition of the Mixed Economic System", "What a mixed economy is and how the public and private sectors share the allocation of resources. Syllabus 2.10.1.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Explain"], real_items)

# ---------------------------------------------------------------- 2.10.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A mixed economic system aims to keep the <b>benefits of the market</b> (efficiency, choice, innovation) while using the government to correct its <b>weaknesses</b> (inequality, public goods, externalities, monopoly). Its own problems are <b>government failure</b>, <b>higher taxes</b> and <b>reduced incentives</b>.</p></div>

  <div class="grid2">
    <div class="card"><h3>Advantages</h3><ul>
      <li>Market efficiency and consumer choice in most areas</li>
      <li>Public and merit goods are provided</li>
      <li>Government can correct external costs and limit monopoly</li>
      <li>A safety net: welfare benefits reduce poverty and inequality</li>
      <li>Government can stabilise the economy in recessions</li>
      <li>Protects consumers and workers by regulation</li>
    </ul></div>
    <div class="card"><h3>Disadvantages</h3><ul>
      <li><b>High taxes</b> to fund the public sector may reduce incentives to work and invest</li>
      <li>State-run industries can be <b>inefficient</b> without competition</li>
      <li><b>Government failure:</b> poor decisions, bureaucracy, corruption or interference</li>
      <li>Regulation can raise costs for firms</li>
      <li>Budget deficits and debt if the government overspends</li>
      <li>The balance between market and state is hard to get right</li>
    </ul></div>
  </div>

  <h2>Evaluation</h2>
  <ul>
    <li>The mix works best where intervention <b>targets real market failures</b> and is cost-effective.</li>
    <li>It works less well if the state crowds out private activity or intervenes without clear evidence.</li>
    <li>The right balance depends on a country's <b>history, income and priorities</b>.</li>
  </ul>
  <p class="note">A good answer compares the mixed system with <b>both</b> a market system and a planned system, and makes a judgement.</p>
'''
steppers = [
  ("Why a mixed economy helps", "--good", ["Markets create efficiency and choice", "Market failure leaves gaps", "The government fills the gaps with public and merit goods", "Welfare benefits protect those in need", "A mixed economy blends efficiency and fairness"]),
  ("Why the mix can go wrong", "--bad", ["The government raises taxes to fund services", "Incentives to work or invest may fall", "State firms face no competition and become inefficient", "Government decisions may be poor (government failure)", "A mixed economy can be less efficient"]),
]
lab1 = dict(title="Weigh the mixed system", intro="Rate how well a mixed economy does on four aims and see the overall verdict.", rl=["Average score", "Strongest aim", "Weakest aim"],
  sliders=[("Efficiency and choice", 1, 10, 1, 7, "v"), ("Fairness and welfare", 1, 10, 1, 7, "v"), ("Provision of public goods", 1, 10, 1, 8, "v"), ("Incentives and low taxes", 1, 10, 1, 5, "v")],
  fn="const nm = ['Efficiency/choice', 'Fairness/welfare', 'Public goods', 'Incentives/taxes'], avg = (v.reduce((a, b) => a + b, 0) / 4).toFixed(1), hi = nm[v.indexOf(Math.max(...v))], lo = nm[v.indexOf(Math.min(...v))]; return { r: [avg + '/10', hi, lo], t: 'A mixed economy usually does better than a pure market on fairness and public goods, and better than a planned system on efficiency and incentives. Here the average is ' + avg + '/10, strongest on ' + hi.toLowerCase() + ' and weakest on ' + lo.toLowerCase() + '. The best balance depends on what a country values most.', bars: nm.map((n, i) => [n, v[i], ['--accent', '--good', '--warn', '--bad'][i]]) };")
lab2 = dict(title="Strengths and weaknesses", intro="Pick an issue to see the mixed economy's strength and weakness.", h1="Strength", h2="Weakness",
  items=[("Efficiency", "Market competition in most sectors", "State-run firms may be inefficient."), ("Fairness", "Welfare and progressive taxes reduce inequality", "High taxes may reduce incentives."), ("Public goods", "The government provides what the market will not", "Costs fall on taxpayers."), ("Stability", "The government can manage the economy", "It may make poor decisions."), ("Regulation", "Protects consumers and the environment", "Raises costs; red tape."), ("Choice", "Consumers choose in private markets", "Public services may offer less choice.")])
cl = [("Is each an <b>advantage</b> or a <b>disadvantage</b> of a mixed economy?", ["Advantage", "Disadvantage"], [("Public goods are provided", 0), ("A welfare safety net", 0), ("Correcting externalities", 0), ("High taxes reduce incentives", 1), ("Government failure", 1), ("State firms may be inefficient", 1)], "Weigh both."),
      ("Does each <b>favour a market</b> or a <b>favour government action</b>?", ["Favours market", "Favours government"], [("Efficiency from competition", 0), ("Consumer choice", 0), ("Reducing pollution", 1), ("Reducing inequality", 1), ("Providing defence", 1), ("Innovation through profit", 0)], "Know what each does best.")]
match = [["Government failure", "Intervention that worsens the outcome"], ["Safety net", "Benefits that protect low-income households"], ["Bureaucracy", "Slow, rule-bound administration"], ["Incentives", "Rewards that encourage effort"], ["Progressive tax", "A tax that takes a larger share of higher incomes"], ["Crowding out", "Public spending that reduces private activity"]]
order = ("Put the chain in order: <b>how high taxes can reduce growth</b>.", ["The government raises taxes", "Firms and workers keep less of their earnings", "Incentives to work and invest fall", "Less output is produced", "Economic growth slows"], "A disadvantage of a larger public sector.")
calcs = [("Income is $50,000 and tax is 30%. How much tax is paid ($)?", 15000, "30% × 50,000 = <b>$15,000</b>.", None, None), ("Government spending is $120bn and tax revenue is $100bn. What is the budget deficit ($bn)?", 20, "120 − 100 = <b>$20bn</b>.", None, None)]
mcq = [("An advantage of a mixed economy is:", ["Higher taxes", "Provision of public goods", "State inefficiency", "Bureaucracy"], 1, "The state fills gaps."), ("A disadvantage is:", ["Consumer choice", "Government failure", "Competition", "Innovation"], 1, "Poor government decisions."), ("High taxes may:", ["Raise incentives", "Reduce incentives to work", "Increase profit", "Remove inequality"], 1, "Disincentives."), ("State-owned firms may be inefficient because:", ["They face no competition", "They are too small", "They make profit", "Prices are zero"], 0, "No rivals."), ("A mixed economy is better than a pure market at:", ["Reducing inequality", "Lowering taxes", "Cutting spending", "Raising profit"], 0, "Welfare and redistribution.")]
cards = [("Government failure", "Intervention that leads to a worse outcome."), ("Safety net", "Welfare support for those in need."), ("Bureaucracy", "Complex, slow administration."), ("Incentive", "A reward that encourages effort."), ("Progressive tax", "Takes a larger share of higher incomes."), ("Crowding out", "Public spending reducing private activity."), ("Budget deficit", "Government spending greater than revenue."), ("Welfare", "Society's well-being."), ("Regulation", "Government rules on firms.")]
exam_qs = [
  Q(1, "Explain", 4, "Explain two advantages of a mixed economic system.", "Public goods; welfare safety net; market efficiency.", "[K|The government can provide public goods such as defence that the market would not.] [N|This improves welfare for everyone.] [K|Private firms still provide choice and efficiency in most markets.] [N|Competition keeps prices low and quality high.]"),
  Q(2, "Explain", 4, "Explain two disadvantages of a mixed economic system.", "High taxes, inefficiency, government failure.", "[K|High taxes may be needed to fund the public sector.] [N|They may reduce incentives to work, save and invest.] [K|State-run industries may be inefficient] [N|because they face no competition and may be influenced by politics.]"),
  Q(3, "Discuss", 8, "Discuss whether a mixed economic system is better than a market economic system. (Oct/Nov 2022, P22 style)", "Mixed: public goods, fairness, correct externalities; market: efficiency, incentives, low taxes. Judgement.", "[K|A mixed system combines market and government decision-making.] [N|It can correct market failure by providing public and merit goods, regulating monopolies and pollution and reducing inequality.] [N|It protects the poor through welfare.] [E|However, taxes are higher, government failure can occur and state firms can be inefficient.] [N|A pure market gives more choice and incentives and lower taxes but ignores externalities and inequality.] [E|Overall, a mixed economy is likely to be better for most countries because market failure is widespread, as long as the government intervenes effectively.]", key=True),
]
tips_ = [("Compare with market and planned systems.", "Not in isolation."), ("Name advantages and disadvantages.", "Balance each."), ("Government failure.", "A key evaluation point."), ("Make a judgement.", "It depends on how well the state intervenes.")]
real_items = [("The NHS in the UK", "Healthcare funded by taxes gives access to all but needs large public spending.", "Fairness vs cost."), ("State-owned railways", "Some state railways have faced losses and criticism for inefficiency.", "Disadvantage."), ("Welfare benefits in Nordic countries", "High taxes fund strong safety nets and low inequality.", "Advantages and trade-offs."), ("Regulation of banks", "Rules after 2008 reduced the risk of financial crises but raised costs for banks.", "Regulation.")]
review("ig-mixed-system-evaluation", "x2102", "2.10.2", "Arguments For and Against the Mixed Economic System", "Advantages and disadvantages of the mixed economic system and how to evaluate it. Syllabus 2.10.2.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Explain", "Discuss"], real_items)
