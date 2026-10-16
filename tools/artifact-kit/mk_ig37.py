"""Builds the two IGCSE Economics 3.7 Types of markets reviews (3.7.1 Competitive, 3.7.2 Monopoly). Run: python3 tools/artifact-kit/mk_ig37.py"""
from igtext import *

# ---------------------------------------------------------------- 3.7.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <span class="kw">competitive market</span> has <b>many firms</b> selling similar products to <b>many buyers</b>, with <b>no single firm able to control the price</b> and <b>easy entry</b> for new firms. Competition keeps <b>prices low</b>, <b>quality high</b> and <b>choice wide</b>, and keeps <b>profits</b> at a normal level. (Diagrams and perfect or imperfect competition theory are not required.)</p></div>

  <h2>Characteristics of competitive markets</h2>
  <ul>
    <li><b>A large number of firms</b> and buyers.</li>
    <li><b>Easy entry and exit:</b> low barriers to entry for new firms.</li>
    <li><b>Similar or identical products</b>, or close substitutes.</li>
    <li><b>Good information:</b> buyers and sellers know prices.</li>
    <li><b>Firms are price takers</b> or have little power over price.</li>
  </ul>

  <h2>Effect of having many firms</h2>
  <div class="tw"><table class="t">
    <tr><th>Variable</th><th>Effect of many firms competing</th></tr>
    <tr><td><b>Price</b></td><td>Lower: firms undercut each other to win customers</td></tr>
    <tr><td><b>Quality</b></td><td>Higher: firms improve quality to attract buyers</td></tr>
    <tr><td><b>Choice</b></td><td>Wider: many products and variants</td></tr>
    <tr><td><b>Profit</b></td><td>Lower: competition limits profit; new firms enter if profits are high</td></tr>
    <tr><td><b>Efficiency and innovation</b></td><td>Higher: firms cut costs and innovate to survive</td></tr>
  </table></div>

  <div class="grid2">
    <div class="card"><h3>Advantages</h3><ul><li>Lower prices for consumers</li><li>Better quality and choice</li><li>Efficient use of resources</li><li>Firms respond to consumer wants</li><li>Innovation to stay ahead</li></ul></div>
    <div class="card"><h3>Disadvantages</h3><ul><li>Low profit may leave little for research</li><li>Small firms may lack economies of scale</li><li>Firms may cut quality or wages to cut costs</li><li>Many firms may fail: job losses</li><li>Wasteful duplication or excessive advertising</li></ul></div>
  </div>
'''
steppers = [
  ("Competition lowers price", "--good", ["Many bakeries sell similar bread", "One bakery raises its price", "Customers switch to rivals", "The bakery loses sales and cuts its price", "Competition keeps prices low"]),
  ("Competition limits profit", "--accent", ["A firm in a market earns high profit", "Other firms see this and enter easily", "Supply rises and price falls", "Profit per firm falls", "Profit returns to a normal level"]),
]
lab1 = dict(title="Number of firms and the market", intro="Add firms to a market and see how the price, choice and profit per firm change (illustrative model).", rl=["Price", "Choice (products)", "Profit per firm"],
  sliders=[("Number of firms", 1, 30, 1, 8, "v"), ("Ease of entry (1 hard, 10 easy)", 1, 10, 1, 7, "v")],
  fn="const p = 10 + 40 / Math.sqrt(v[0]) - v[1] * 0.2, ch = Math.round(v[0] * 1.5), pr = Math.max(0, 50 / v[0] - v[1] * 0.4); return { r: ['$' + p.toFixed(1), ch, '$' + pr.toFixed(1) + 'k'], t: 'With ' + v[0] + ' firms and entry ease ' + v[1] + ', the price is about $' + p.toFixed(1) + ', buyers have ' + ch + ' products to choose from and profit per firm is about $' + pr.toFixed(1) + 'k. More firms and easier entry push price and profit down and choice up (illustrative model).', bars: [['Price', p, '--warn', '$' + p.toFixed(1)], ['Choice ÷ 3', ch / 3, '--accent', ch], ['Profit per firm', pr, '--bad', '$' + pr.toFixed(1) + 'k']] };")
lab2 = dict(title="Competitive market or not?", intro="Pick a market feature to see whether it fits a competitive market.", h1="Fits competitive market?", h2="Why",
  items=[("Hundreds of small sellers", "Yes", "Many firms."), ("A single supplier", "No", "That is a monopoly."), ("Easy entry for new firms", "Yes", "Low barriers."), ("Huge patents block entry", "No", "Barriers to entry."), ("Identical products", "Yes", "Firms compete on price."), ("One firm sets the price", "No", "Price maker, not taker.")])
cl = [("Is each effect of <b>competition</b> likely to <b>rise</b> or <b>fall</b>?", ["Rises", "Falls"], [("Quality of products", 0), ("Consumer choice", 0), ("Efficiency", 0), ("Prices", 1), ("Profit per firm", 1), ("Barriers to entry", 1)], "Many firms."),
      ("Is each an <b>advantage</b> or a <b>disadvantage</b> of competitive markets?", ["Advantage", "Disadvantage"], [("Lower prices", 0), ("Wider choice", 0), ("Innovation", 0), ("Little profit to fund research", 1), ("Firms may fail", 1), ("Cutting quality to cut costs", 1)], "Weigh both.")]
match = [["Competitive market", "Many firms, easy entry, little control over price"], ["Price taker", "A firm that must accept the market price"], ["Barriers to entry", "Obstacles stopping new firms entering"], ["Substitutes", "Goods that can replace each other"], ["Normal profit", "The minimum profit to keep a firm in business"], ["Consumer sovereignty", "Consumers decide what is produced"]]
order = ("Put the chain in order: <b>how competition improves quality</b>.", ["Many firms compete for customers", "Firms want to stand out", "They improve quality and service", "Customers choose the better products", "Overall quality rises"], "Competition drives quality.")
calcs = [("The market price is $8 and a firm tries $10. Customers switch. By what percentage was the firm's price above the market price?", 25, "2 ÷ 8 × 100 = <b>25%</b>.", None, None), ("There are 20 firms each with 5% market share. What is the total market share (%)?", 100, "20 × 5 = <b>100%</b>.", None, None)]
mcq = [("A feature of a competitive market is:", ["One firm controls price", "Many firms", "High barriers to entry", "No substitutes"], 1, "Many firms."), ("Competition usually leads to:", ["Higher prices", "Lower prices", "Less choice", "Lower quality"], 1, "Undercutting."), ("Easy entry means:", ["Firms can join the market easily", "Firms cannot join", "Prices are fixed", "There is one seller"], 0, "Low barriers."), ("A disadvantage of competitive markets is:", ["Higher prices", "Low profit may limit research", "Less choice", "Monopoly power"], 1, "Little left to invest."), ("A price taker:", ["Sets the market price", "Accepts the market price", "Is a monopoly", "Charges more than rivals"], 1, "No price power.")]
cards = [("Competitive market", "A market with many firms, easy entry and little price control."), ("Price taker", "A firm that cannot influence the market price."), ("Barriers to entry", "Obstacles that stop new firms entering a market."), ("Substitute", "A good that can replace another."), ("Normal profit", "The minimum profit needed to stay in business."), ("Competition", "Rivalry between firms for customers."), ("Consumer choice", "The range of products available."), ("Efficiency", "Producing without waste."), ("Innovation", "New products or methods.")]
exam_qs = [
  Q(1, "Identify", 2, "Identify two characteristics of a competitive market.", "Many firms, easy entry, similar products.", "[K|A large number of firms.] [K|Easy entry for new firms (or little control over price).]"),
  Q(2, "Explain", 4, "Explain the effect of having many firms in a market on price and quality.", "Lower prices; higher quality.", "[K|With many firms competing, each tries to win customers by cutting prices.] [N|Prices fall.] [K|Firms also improve quality to stand out,] [N|so consumers get better products.]"),
  Q(3, "Explain", 4, "Explain the effect of many firms on profit.", "Competition limits profit; entry.", "[K|If profits are high, new firms enter the market easily.] [N|Supply rises and price falls,] [N|so profit per firm falls to a normal level.]"),
  Q(4, "Discuss", 8, "Discuss whether competitive markets are good for consumers.", "Price, quality, choice vs quality cuts and little research. Judgement.", "[K|In competitive markets many firms compete, so prices tend to be low.] [N|Quality and choice are higher as firms try to win customers.] [N|Competition also encourages efficiency and innovation.] [E|However, low profits may leave little money for research, and some firms may cut quality or wages to survive.] [E|Overall, competitive markets are usually good for consumers, particularly where information is good and regulation prevents harmful cost cutting.]", key=True),
]
tips_ = [("Many firms, easy entry.", "Say both."), ("Effects: price, quality, choice, profit.", "The syllabus list."), ("Use an example market.", "Bakeries, street food, taxis."), ("Evaluate.", "Low profit, quality cutting.")]
real_items = [("Street food markets", "Many sellers offer similar dishes at competitive prices.", "Competitive market."), ("Online price comparison", "Sites let shoppers find the cheapest seller, raising competition.", "Good information."), ("Smartphone apps", "Thousands of developers compete, lowering prices and lifting quality.", "Easy entry."), ("Local taxis", "Many drivers compete on fares and service.", "Competition.")]
review("ig-competitive-markets", "t371", "3.7.1", "Competitive Markets", "Characteristics, advantages and disadvantages of competitive markets and the effect of many firms on price, quality, choice and profit. Syllabus 3.7.1.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Identify", "Explain", "Discuss"], real_items)

# ---------------------------------------------------------------- 3.7.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <span class="kw">monopoly</span> market has <b>only one firm</b> (or one that dominates), with <b>high barriers to entry</b> that stop rivals joining. Because it faces little or no competition, the monopolist can <b>set the price</b>, restrict output and earn <b>high profits</b>. (Diagrams are not required.)</p></div>

  <h2>Characteristics of a monopoly</h2>
  <ul>
    <li><b>A single seller</b> (or a very dominant one, for example over 25% of the market in some countries).</li>
    <li><b>High barriers to entry:</b> patents and licences, huge start-up costs, control of resources, economies of scale, brand loyalty, legal protection.</li>
    <li><b>No close substitutes</b> for the product.</li>
    <li>The firm is a <b>price maker</b>: it chooses price and output.</li>
  </ul>

  <h2>Effect of having only one firm</h2>
  <div class="tw"><table class="t">
    <tr><th>Variable</th><th>Effect of monopoly</th></tr>
    <tr><td><b>Price</b></td><td>Higher: no rivals to undercut</td></tr>
    <tr><td><b>Quality</b></td><td>May be lower (no pressure) but can be higher if profits fund research</td></tr>
    <tr><td><b>Choice</b></td><td>Limited: one supplier, fewer variants</td></tr>
    <tr><td><b>Profit</b></td><td>Higher, because barriers stop new firms competing it away (supernormal profit)</td></tr>
    <tr><td><b>Output</b></td><td>Often restricted</td></tr>
  </table></div>

  <div class="grid2">
    <div class="card"><h3>Advantages</h3><ul><li>Economies of scale can lower costs (and prices)</li><li>High profits can fund research and innovation</li><li>A natural monopoly (railways, water) avoids duplicated networks</li><li>Patent protection rewards inventors</li><li>Easier to regulate than many firms</li></ul></div>
    <div class="card"><h3>Disadvantages</h3><ul><li>Higher prices and restricted output</li><li>Less choice and lower pressure to improve quality</li><li>Inefficiency: no incentive to cut costs</li><li>Consumers' real incomes fall</li><li>Abuse of power: unfair practices, blocking rivals</li></ul></div>
  </div>
  <p class="note">Governments may <b>regulate</b>, break up, tax or nationalise monopolies, or encourage competition and set price caps.</p>
'''
steppers = [
  ("Barriers protect a monopoly", "--accent", ["A firm holds a patent on a medicine", "Rivals cannot copy it legally", "The firm faces no competition", "It sets a high price", "High profits persist"]),
  ("Monopoly and consumers", "--bad", ["A single supplier controls the market", "It restricts output", "It raises the price", "Consumers pay more and choose from fewer products", "Real incomes and welfare fall"]),
  ("A possible benefit of monopoly", "--good", ["A monopoly earns high profit", "It invests in research and technology", "It produces on a very large scale", "Economies of scale cut costs", "Prices may fall and quality may improve"]),
]
lab1 = dict(title="Monopoly or competition?", intro="Compare a competitive market with a monopoly for the same product. Set the mark-up and the cut in output.", rl=["Monopoly price", "Monopoly output", "Extra profit"],
  sliders=[("Competitive price ($)", 5, 50, 5, 20, "'$' + v"), ("Cost per unit ($)", 2, 40, 2, 16, "'$' + v"), ("Monopoly mark-up over competitive price (%)", 0, 100, 10, 40, "v + '%'"), ("Cut in output (%)", 0, 60, 5, 20, "v + '%'")],
  fn="const p = v[0] * (1 + v[2] / 100), q = 1000 * (1 - v[3] / 100), comp = (v[0] - v[1]) * 1000, mono = (p - v[1]) * q; return { r: ['$' + p.toFixed(0), q.toFixed(0), (mono - comp >= 0 ? '+' : '−') + '$' + Math.abs(mono - comp).toFixed(0)], t: 'A competitive market sells 1,000 units at $' + v[0] + ' (profit $' + comp.toFixed(0) + '). The monopoly charges $' + p.toFixed(0) + ' and sells ' + q.toFixed(0) + ' units, earning $' + mono.toFixed(0) + '. Consumers pay more and buy less, while barriers to entry let the monopoly keep the extra profit.', bars: [['Competitive price', v[0], '--good'], ['Monopoly price', p, '--bad'], ['Output ÷ 50', q / 50, '--accent', q.toFixed(0)]] };")
lab2 = dict(title="Barriers to entry", intro="Pick a barrier to see how it protects a monopoly.", h1="How it protects", h2="Example",
  items=[("Patents", "Legal protection from copying", "A new medicine."), ("High start-up costs", "Few firms can afford to enter", "Building a railway network."), ("Control of resources", "Rivals cannot obtain inputs", "A mine owner."), ("Economies of scale", "Rivals cannot match low costs", "A large utility."), ("Brand loyalty", "Customers stay with the leader", "A dominant software firm."), ("Government licence", "Only one firm is allowed", "A state postal service.")])
cl = [("Is each a <b>barrier to entry</b> or <b>not</b>?", ["Barrier to entry", "Not a barrier"], [("A patent", 0), ("Huge start-up costs", 0), ("A legal licence", 0), ("Low start-up costs", 1), ("Many suppliers of inputs", 1), ("Customers easily switch", 1)], "What blocks rivals."),
      ("Is each an <b>advantage</b> or a <b>disadvantage</b> of monopoly?", ["Advantage", "Disadvantage"], [("Economies of scale", 0), ("Funds research", 0), ("Avoids duplicated networks", 0), ("Higher prices", 1), ("Less choice", 1), ("Little pressure to be efficient", 1)], "Weigh both.")]
match = [["Monopoly", "A single dominant seller"], ["Barriers to entry", "Obstacles that stop new firms entering"], ["Price maker", "A firm that sets its own price"], ["Natural monopoly", "A market best supplied by one firm"], ["Patent", "Legal protection for an invention"], ["Supernormal profit", "Profit above the minimum needed to stay in business"]]
order = ("Put the chain in order: <b>how a monopoly can reduce consumer welfare</b>.", ["A firm is the only seller", "It faces no competition", "It restricts output and raises price", "Consumers pay more and have less choice", "Consumer welfare falls"], "Market power harms consumers.")
calcs = [("A monopoly raises its price from $20 to $28. What is the percentage rise?", 40, "8 ÷ 20 × 100 = <b>40%</b>.", None, None), ("A monopoly sells 800 units at $28 with cost $16 per unit. What is its profit ($)?", 9600, "(28 − 16) × 800 = <b>$9,600</b>.", None, None)]
mcq = [("A monopoly has:", ["Many firms", "One dominant firm", "No profit", "Many substitutes"], 1, "A single seller."), ("A barrier to entry is:", ["A patent", "Low cost of entry", "Many suppliers", "Easy information"], 0, "Blocks rivals."), ("A monopoly is likely to charge:", ["Lower prices than competition", "Higher prices", "Zero prices", "Equal prices"], 1, "No rivals."), ("An advantage of monopoly is:", ["Economies of scale", "Higher prices", "Less choice", "Restricted output"], 0, "Lower unit costs possible."), ("A price maker:", ["Accepts the market price", "Sets the price", "Has no profit", "Faces many rivals"], 1, "Market power.")]
cards = [("Monopoly", "A market with a single dominant seller."), ("Barriers to entry", "Obstacles that stop new firms entering a market."), ("Price maker", "A firm that can set its own price."), ("Natural monopoly", "A market where one firm supplies at lowest cost."), ("Patent", "Legal protection for an invention."), ("Supernormal profit", "Profit above normal profit."), ("Market power", "The ability to influence price."), ("Regulation", "Government rules to limit abuse of power."), ("Competition authority", "A body that investigates monopolies and mergers.")]
exam_qs = [
  Q(1, "Define", 2, "Define a monopoly.", "Single dominant seller.", "[K|A monopoly is a market in which there is only one firm,] [K|or a firm that dominates the market.]"),
  Q(2, "Identify", 2, "Identify two characteristics of a monopoly market.", "One firm, barriers to entry, price maker.", "[K|A single firm dominates the market.] [K|High barriers to entry (or the firm is a price maker).]"),
  Q(3, "Explain", 4, "Explain the effect of having only one firm in a market on price and choice.", "Higher price; less choice.", "[K|With no competition, a monopoly can raise its price.] [N|Consumers pay more.] [K|There is only one supplier,] [N|so consumers have less choice of products.]"),
  Q(4, "Explain", 4, "Explain why a monopoly may earn high profits.", "Barriers; price power.", "[K|Barriers to entry stop new firms joining the market.] [N|The monopoly can therefore keep its price high] [N|and does not lose profit to competitors.]"),
  Q(5, "Discuss", 8, "Discuss whether a monopoly is always bad for consumers.", "Higher price, less choice vs economies of scale, innovation. Judgement.", "[K|A monopoly can raise prices, restrict output and reduce choice.] [N|With no competition it may also be inefficient.] [N|However, economies of scale may lower its costs and prices, and high profits can fund research.] [N|A natural monopoly may avoid wasteful duplication.] [E|Overall, monopolies usually harm consumers, but benefits are possible if regulated to prevent abuse of power.]", key=True),
]
tips_ = [("One firm, barriers, price maker.", "Define it."), ("Effects: price, quality, choice, profit.", "Learn the list."), ("Barriers: patents, costs, licences.", "Explain how they work."), ("Evaluate: economies of scale.", "Monopoly is not always bad.")]
real_items = [("Patented medicines", "Drug firms can charge high prices during patent periods.", "Barriers to entry."), ("Local water supply", "Usually one provider per area: a natural monopoly.", "Natural monopoly."), ("Google in search", "A very dominant share of the market raises competition concerns.", "Market power."), ("State postal services", "In some countries a single state firm delivers letters.", "A legal monopoly.")]
review("ig-monopoly-markets", "t372", "3.7.2", "Monopoly Markets", "Characteristics, advantages and disadvantages of monopoly and the effect of only one firm on price, quality, choice and profit. Syllabus 3.7.2.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Identify", "Explain", "Discuss"], real_items)
