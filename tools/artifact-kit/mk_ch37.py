"""Builds the three ch37 part pages (ob1..ob3) from slices of ob.* plus new content. Run: python3 tools/artifact-kit/mk_ch37.py"""
from splitter import *
mktips = tips
S = Src("ob")
HEAD = S.j_((1, 7))
EY = "A Level Economics · 9708 · Syllabus 7.8 · Part {} of 3"
RW = '<p class="note">Examples are explained in general terms. Check current details before quoting them in an exam answer.</p>\n'

# ------------------------------------------------------------------ 37.1
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Firms do not always aim for <b>maximum profit</b>. Managers may instead aim for <b>revenue maximisation</b> (MR = 0), <b>sales maximisation</b> (as many units as possible while earning normal profit, AR = AC), <b>growth</b> or <b>satisficing</b> (a satisfactory profit, then other aims). Objectives differ because of the <b>principal-agent problem</b>: owners (principals) and managers (agents) want different things and managers know more about the firm. The objective changes price and output: price is highest at profit maximisation and lowest at sales maximisation.</p></div>
''' + S.b((25, 36), (37, 40), (41, 51)) + '''
  <h2>4 · The three objectives in numbers</h2>
  <p>Demand is P = 100 − Q, marginal cost is $20 and fixed cost is $400.</p>
  <div class="tw"><table class="t">
    <tr><th>Objective</th><th>Rule</th><th>Output</th><th>Price</th><th>Profit</th></tr>
    <tr><td><b>Profit maximisation</b></td><td>MR = MC</td><td>40</td><td>$60</td><td>$1,200</td></tr>
    <tr><td><b>Revenue maximisation</b></td><td>MR = 0</td><td>50</td><td>$50</td><td>$1,100</td></tr>
    <tr><td><b>Sales maximisation (normal profit)</b></td><td>AR = AC</td><td>about 75</td><td>about $25</td><td>$0</td></tr>
  </table></div>
  <p>Output rises and price falls as the firm moves from profit to revenue to sales maximisation, while profit falls.</p>
''' + S.b((76, 77)).replace("5 · Which", "5 · Which")
watch = S.b((82, 84))
explore = S.b((97, 102), (118, 123)).replace("Lab 4 ·", "Lab 2 ·")
practise = S.b((128, 129), (131, 132)) + '''
  <h2>3 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = RW + S.b((154, 156))
exam = '''
  <h2>Past paper questions on objectives and the principal-agent problem</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). The June 2020 papers were published but not sat, so they are marked "not sat" where relevant. Below are the essays on objectives and the principal-agent problem, and Paper 3 multiple choice questions. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 20 marks</td><td>1</td><td>Oct/Nov 2024 (41)</td></tr>
    <tr><td>Essay, 25 marks</td><td>1</td><td>May/June 2020 (41, 43, not sat)</td></tr>
    <tr><td>Essay part, 13 marks</td><td>1</td><td>May/June 2020 (42, not sat)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>7 shown below</td><td>2020 to 2024</td></tr>
  </table></div>
  <h2>A · Essay questions</h2>
''' + KEYL + S.b((176, 189), (191, 204), (206, 212)) + '''
''' + MCQTAIL.format("B · Multiple choice questions (Paper 3)")
tips = mktips(S, (284, 285, 286, 287), '', (297, 298)) + cmd(CW["explain"], CW["evaluate"], CW["consider"]) + FC
js = HEAD + S.j_((8, 37), (79, 94), (129, 142)) + '''
/* ---------- Practise ---------- */
''' + S.j_((145, 162)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Profit maximisation", "Producing where MR = MC"],
  ["Revenue maximisation", "Producing where MR = 0"],
  ["Sales maximisation", "Selling as much as possible while earning normal profit: AR = AC"],
  ["Satisficing", "Earning a satisfactory profit and then pursuing other aims"],
  ["Principal", "The owner or shareholder who employs a manager"],
  ["Agent", "The manager who acts for the owner"],
  ["Divorce of ownership and control", "Shareholders own the firm but managers run it"],
  ["Asymmetric information", "One party knows more than the other"],
], done: "Eight words for objectives and the principal-agent problem." });
''' + calc(S, (193, 194, 198), '''  { q: "Demand is P = 100 − Q, MC = $20 and fixed cost is $400. At the profit-maximising output of 40, what is the profit ($)?", a: 1200, sol: "(60 − 20) × 40 − 400 = <b>$1,200</b>." },
  { q: "The firm moves to the revenue-maximising output of 50. What is its profit ($)?", a: 1100, sol: "Revenue 2,500 − total cost (20 × 50 + 400 = 1,400) = <b>$1,100</b>." },
  { q: "At the revenue-maximising output of 50, price is $50. By how much has price fallen compared with profit maximisation ($)?", a: 10, sol: "60 − 50 = <b>$10</b>." },
''') + qz(S, (201, 202, 203, 206), '''  { q: "Managers who aim for the largest possible sales while earning normal profit are pursuing:", opts: ["profit maximisation", "revenue maximisation", "sales maximisation", "satisficing"], a: 2, why: "Sales maximisation is at AR = AC, where only normal profit is earned." },
''') + cards(S, tuple(range(209, 219))) + mcq(S, tuple(range(228, 235)))
write("ob1", page(EY.format(1), "Business Objectives and the Principal-Agent Problem",
  "Profit, revenue and sales maximisation, satisficing and growth, why managers and owners differ, and how to align their aims. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Business Objectives and the Principal-Agent Problem", "business-objectives-principal-agent")

# ------------------------------------------------------------------ 37.2
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b>Price discrimination</b> is selling the same product at different prices to different groups for reasons not related to cost. It needs four conditions: the firm can set its own price, it can separate the markets, the markets have different price elasticities of demand, and there is no resale between them. In <b>third degree</b> discrimination the firm charges a higher price where demand is <b>inelastic</b> and a lower price where it is <b>elastic</b>, setting MR = MC in each market. Profit rises, some consumers gain access at a low price, and others pay more, so the effect on consumers is mixed.</p></div>

  <h2>1 · How price discrimination works</h2>
''' + S.b((54, 63)) + '''
  <h2>2 · Two markets in numbers</h2>
  <p>A cinema has adults with demand P = 90 − Q and students with demand P = 50 − Q, and a marginal cost of $10. With MR = MC in each market:</p>
  <div class="tw"><table class="t">
    <tr><th></th><th>Adults (inelastic)</th><th>Students (elastic)</th><th>Total</th></tr>
    <tr><td><b>One price of $40</b></td><td>Output 50, profit $1,500</td><td>Output 10, profit $300</td><td>Profit $1,800</td></tr>
    <tr><td><b>Two prices</b></td><td>Price $50, output 40, profit $1,600</td><td>Price $30, output 20, profit $400</td><td>Profit <b>$2,000</b></td></tr>
  </table></div>
  <p>Profit rises by $200. Students pay less and buy twice as many tickets; adults pay more and buy fewer. Total consumer surplus falls, because the price rise for adults costs more than the price fall gives to students.</p>
  <div class="tip"><b class="h">Draw it as two side-by-side diagrams</b>Same MC in both markets. For each market find MR = MC, read the price from the demand curve and shade the profit. The more inelastic market has the higher price.</div>
'''
watch = S.b((86, 88)).replace("2 · Third", "1 · Third")
explore = S.b((104, 109)).replace("Lab 2 ·", "Lab 1 ·")
practise = S.b((140, 141)).replace("5 · Put", "1 · Put") + '''
  <h2>2 · Which market pays more?</h2><div id="cl1" class="card"></div>
  <h2>3 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = RW + S.b((153, 153)) + '''  <div class="rw"><h3>Rail fares by time of day</h3><p>Commuters who must travel at peak times have inelastic demand and pay more, while leisure travellers can choose off-peak times and pay less. The train company separates the markets by the time on the ticket and cannot resell between them.</p><div class="use"><b>Exam use:</b> third degree discrimination by time, with a separable market and different elasticities.</div></div>
  <div class="rw"><h3>Student and senior discounts</h3><p>Students and pensioners often have lower incomes and more elastic demand, so many firms offer them a discount that is checked with an ID card, which keeps the markets separate.</p><div class="use"><b>Exam use:</b> the condition of separating markets and the effect on consumers and profit.</div></div>
'''
exam = '''
  <h2>Past paper questions on price discrimination</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the essays on price discrimination, and Paper 3 multiple choice questions on its conditions. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 20 marks</td><td>1</td><td>May/June 2023 (41, 43)</td></tr>
    <tr><td>Essay parts, 13 marks</td><td>3</td><td>Oct/Nov 2021 (42); May/June 2021 (41, 43); Oct/Nov 2022 (42)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>6 shown below</td><td>2020 to 2024</td></tr>
  </table></div>
  <h2>A · Essay questions</h2>
''' + KEYL + S.b((215, 221), (223, 237), (239, 243), (245, 249)) + '''
''' + MCQTAIL.format("B · Multiple choice questions (Paper 3)")
tips = mktips(S, (288, 289), '', (299,)) + cmd(CW["explain"], CW["discuss"], CW["evaluate"]) + FC
js = HEAD + S.j_((38, 59), (96, 111)) + '''
/* ---------- Practise ---------- */
''' + S.j_((183, 190)) + '''Lib.classify($("#cl1"), {
  prompt: "In third degree price discrimination, which market is likely to pay the higher price?",
  buckets: [{ label: "Higher price (inelastic demand)" }, { label: "Lower price (elastic demand)" }],
  items: [
    { text: "Business travellers booking at the last minute", b: 0 }, { text: "Commuters at peak times", b: 0 }, { text: "Customers with few alternatives", b: 0 }, { text: "Buyers for whom the product is a necessity", b: 0 },
    { text: "Students with limited income", b: 1 }, { text: "Leisure travellers who can choose another day", b: 1 }, { text: "Customers with many substitutes", b: 1 }, { text: "Bargain hunters who shop around", b: 1 },
  ], done: "Charge more where demand is inelastic and less where it is elastic.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Price discrimination", "Charging different prices for the same product, not due to cost"],
  ["First degree", "Each buyer pays the most they are willing to pay"],
  ["Second degree", "Price depends on the quantity bought"],
  ["Third degree", "Different prices for different groups or times"],
  ["Separable markets", "The firm can stop buyers moving between the markets"],
  ["Resale", "Buying at the low price to sell at the high price, which would undo the policy"],
  ["Consumer surplus", "What buyers would pay minus what they do pay"],
], done: "Seven words for price discrimination." });
''' + calc(S, (195, 196, 197), '''  { q: "In the cinema example, adults pay $50 for 40 tickets and the marginal cost is $10. What is the profit from adults ($)?", a: 1600, sol: "(50 − 10) × 40 = <b>$1,600</b>." },
  { q: "Students pay $30 for 20 tickets at a marginal cost of $10. What is their profit ($)?", a: 400, sol: "(30 − 10) × 20 = <b>$400</b>." },
''') + qz(S, (204,), '''  { q: "Third degree price discrimination charges a higher price to the group with:", opts: ["more elastic demand", "less elastic demand", "lower income", "more substitutes"], a: 1, why: "A firm can raise the price more where buyers do not respond much." },
  { q: "If buyers could resell the product, price discrimination would:", opts: ["be easier", "break down because buyers would buy at the low price and resell", "raise profit", "make demand more inelastic"], a: 1, why: "The low-price group would supply the high-price group, removing the price difference." },
  { q: "A firm that practises price discrimination will most likely:", opts: ["earn a lower profit than with one price", "earn at least as much profit as with one price", "have to reduce output", "have perfectly elastic demand"], a: 1, why: "If it could not earn at least as much, it would charge one price." },
''') + cards(S, (219, 220), '''  ["Separable markets", "A condition for price discrimination: the firm can stop buyers moving between markets."],
  ["Price elasticity of demand and price", "The more inelastic the market, the higher the price charged."],
  ["Consumer surplus transfer", "Price discrimination can move surplus from consumers to the firm."],
''') + mcq(S, (235, 236, 237, 238, 239), '''  { q: "[Oct/Nov 2024 · 32 · Q7] A bus company has a monopoly and specialises in long-distance travel. It initially sells its tickets to customers one month in advance of the journey. As the departure date approaches, the price of a ticket increases. Which kind of pricing policy does the bus company operate?", opts: ["minimum pricing", "predatory pricing", "price discrimination", "price leadership"], a: 2, why: "The same service is sold at different prices to groups with different elasticities (early and late bookers), not because of cost." },
''')
write("ob2", page(EY.format(2), "Price Discrimination",
  "The conditions for price discrimination, third degree discrimination in two markets, and who gains and who loses. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Price Discrimination", "price-discrimination")

# ------------------------------------------------------------------ 37.3
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>An incumbent firm can use price to protect its position. <b>Limit pricing</b> sets a price below the profit-maximising price, near average cost, so that a new entrant would earn only normal profit and stays out; it is aimed at <b>new</b> entrants. <b>Predatory pricing</b> sets a price below average cost, even at a loss, to force an <b>existing</b> rival out, after which the price is raised; it is anti-competitive and may be illegal. Other policies include <b>cost-plus pricing</b>, price leadership and non-price competition. Whether consumers gain depends on how long low prices last.</p></div>

  <h2>1 · Limit and predatory pricing</h2>
''' + S.b((64, 68)) + '''
  <h2>2 · Limit pricing in numbers</h2>
  <p>An incumbent has MC = $25 and demand P = 100 − Q. Its profit-maximising (monopoly) price is $62.50, selling 37.5 units for a profit of about $1,406. A rival could enter at a unit cost of $40. If the incumbent keeps the high price, the entrant undercuts it, sales halve and profit falls to about $703. If it cuts price to $40 (the entrant's cost), entry is not profitable, the incumbent sells 60 units and earns (40 − 25) × 60 = <b>$900</b>. Limit pricing is worthwhile because $900 is more than the $703 left after entry.</p>
''' + S.b((69, 74)).replace("<h3>Other policies</h3>", "<h2>3 · Other pricing policies</h2>") + '''
  <h2>4 · Evaluating</h2>
  <ul>
    <li><b>Limit pricing:</b> consumers gain in the short run from a lower price, but competition is limited and the firm may raise price later.</li>
    <li><b>Predatory pricing:</b> consumers gain while prices are low, then lose if the rival exits and the price rises. It is costly for the firm and may be illegal, and hard to prove.</li>
    <li><b>Contestability:</b> if entry and exit are easy, even a monopolist is pushed towards limit pricing.</li>
  </ul>
'''
watch = S.b((90, 92)).replace("3 · Limit", "1 · Limit")
explore = S.b((111, 116)).replace("Lab 3 ·", "Lab 1 ·")
practise = S.b((134, 135)).replace("3 · Which", "1 · Which") + '''
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = RW + S.b((157, 158))
exam = '''
  <h2>Past paper questions on limit pricing and predatory pricing</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the questions on limit and predatory pricing, and Paper 3 multiple choice questions on pricing policies and contestability. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay parts, 12 or 13 marks</td><td>2</td><td>Oct/Nov 2022 (43, 41)</td></tr>
    <tr><td>Data response part, 4 + 2 marks</td><td>1</td><td>Oct/Nov 2024 (43)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>4 shown below</td><td>2020 to 2024</td></tr>
  </table></div>
  <h2>A · Written questions</h2>
''' + KEYL + S.b((252, 265), (267, 271), (273, 273)) + '''
''' + MCQTAIL.format("B · Multiple choice questions (Paper 3)")
tips = mktips(S, (290, 291), '', (300, 301)) + cmd(CW["explain"], ("Distinguish", "Say clearly how two ideas differ."), CW["discuss"]) + FC
js = HEAD + S.j_((60, 78), (113, 127)) + '''
/* ---------- Practise ---------- */
''' + S.j_((163, 172)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Limit pricing", "A price below the monopoly price set to deter new entrants"],
  ["Predatory pricing", "A price below cost set to force an existing rival out"],
  ["Cost-plus pricing", "Price set by adding a percentage mark-up to unit cost"],
  ["Barrier to entry", "Something that makes it hard for new firms to join a market"],
  ["Contestable market", "A market where entry and exit are easy and cheap"],
  ["Price leadership", "One firm sets a price that rivals follow"],
  ["Incumbent", "A firm that is already in the market"],
], done: "Seven words for pricing policies." });
''' + calc(S, (192,), '''  { q: "An incumbent has MC = $25 and demand P = 100 − Q. It cuts its price to a limit price of $40. How many units does it sell?", a: 60, sol: "Q = 100 − 40 = <b>60</b>." },
  { q: "What is its profit at the limit price of $40 ($)?", a: 900, sol: "(40 − 25) × 60 = <b>$900</b>." },
  { q: "If it keeps the monopoly price, profit is about $1,406 but a rival enters and sales halve. What is the profit after entry ($, nearest whole number)?", a: 703, tol: 1, sol: "1,406 ÷ 2 = <b>$703</b>, less than the $900 from limit pricing." },
''') + qz(S, (205,), '''  { q: "Limit pricing is mainly aimed at:", opts: ["existing rivals", "new entrants", "customers", "suppliers"], a: 1, why: "It makes entry look unprofitable." },
  { q: "Predatory pricing involves setting price:", opts: ["below the profit-maximising price but above average cost", "below average cost to force a rival out", "equal to marginal cost", "above the monopoly price"], a: 1, why: "The aim is to drive an existing rival out, even at a loss." },
  { q: "Compared with predatory pricing, limit pricing usually:", opts: ["involves selling at a loss", "keeps price near normal profit and does not involve a loss", "has no effect on entry", "is always illegal"], a: 1, why: "The incumbent still earns at least normal profit." },
''') + cards(S, (221, 222, 223)) + mcq(S, (), '''  { q: "[May/June 2020 (not sat) · 32 · Q4] Four bus companies control more than two-thirds of the market in a country. Critics claim that these companies fix prices on some routes to maximise revenue whilst lowering prices on other routes to stop smaller competitors entering the market. Which anti-competitive practices are these companies accused of?", opts: ["collusion and limit pricing", "collusion and price leadership", "limit pricing and price discrimination", "price leadership and x-inefficiency"], a: 0, why: "Fixing prices together is collusion, and lowering prices to keep smaller firms out is limit pricing." },
  { q: "[Oct/Nov 2020 · 31 · Q11] A firm successfully engages in a policy of predatory pricing. What will happen to the prices charged by the firm in the short run and in the long run?", opts: ["rise, rise", "rise, fall", "fall, rise", "fall, fall"], a: 2, why: "Price falls to drive rivals out, then rises once they have left." },
  { q: "[May/June 2024 · 31 · Q7] Which assumption is essential for a market to be contestable?", opts: ["The market is supplied by a large number of firms.", "Firms are free to enter and leave the market.", "Firms cannot earn abnormal profits in the short run.", "Firms produce differentiated goods."], a: 1, why: "Freedom of entry and exit is what makes the threat of new entrants real." },
  { q: "[Oct/Nov 2024 · 33 · Q6] In a perfectly contestable market, entries and exits are cost-free. In reality, why is this not the case with some firms in contestable markets?", opts: ["Firms cannot recover all fixed costs if they cease operations.", "Firms in the industry all operate at the equilibrium level of output.", "Large firms do not have to increase capital to grow.", "Multinational companies always benefit from economies of scale."], a: 0, why: "Sunk costs that cannot be recovered make exit costly." },
''')
write("ob3", page(EY.format(3), "Limit Pricing, Predatory Pricing and Other Pricing Policies",
  "How an incumbent can use price to deter entrants or remove rivals, why limit and predatory pricing differ, and other pricing policies such as cost-plus. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Limit Pricing, Predatory Pricing and Other Pricing Policies", "limit-predatory-pricing")
