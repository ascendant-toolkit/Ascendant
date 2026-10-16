"""Builds the three IGCSE Economics 3.4 Firms reviews (3.4.1 to 3.4.3). Run: python3 tools/artifact-kit/mk_ig34.py"""
from igtext import *

# ---------------------------------------------------------------- 3.4.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Firms can be classified by the <b>sector</b> of the economy they work in (primary, secondary, tertiary), by <b>ownership</b> (private or public sector) and by <b>size</b> (small or large). Each type has its own strengths and weaknesses.</p></div>

  <h2>By sector</h2>
  <div class="tw"><table class="t">
    <tr><th>Sector</th><th>What it does</th><th>Examples</th></tr>
    <tr><td><b>Primary</b></td><td>Extracts or grows natural resources</td><td>Farming, fishing, mining, oil extraction, forestry</td></tr>
    <tr><td><b>Secondary</b></td><td>Manufactures and builds, turning raw materials into products</td><td>Car makers, bakeries, steel mills, construction</td></tr>
    <tr><td><b>Tertiary</b></td><td>Provides services</td><td>Banks, hospitals, shops, teachers, tourism, transport</td></tr>
  </table></div>
  <p class="note">As countries develop, the economy typically shifts from primary to secondary and then to tertiary activity.</p>

  <h2>By ownership</h2>
  <div class="tw"><table class="t">
    <tr><th>Sector</th><th>Owned by</th><th>Main aim</th><th>Examples</th></tr>
    <tr><td><b>Private sector</b></td><td>Individuals or shareholders</td><td>Profit</td><td>Sole traders, partnerships, companies</td></tr>
    <tr><td><b>Public sector</b></td><td>The government</td><td>Providing a service; social welfare; sometimes profit</td><td>State schools, public hospitals, state railways</td></tr>
  </table></div>

  <h2>Small and large firms</h2>
  <div class="grid2">
    <div class="card"><h3>Small firms</h3><p><b>Advantages:</b> personal service, flexible, quick decisions, close to customers, easy to start, owner motivated.<br><b>Disadvantages:</b> limited finance, no economies of scale, higher unit costs, risk of failure, limited bargaining power.</p></div>
    <div class="card"><h3>Large firms</h3><p><b>Advantages:</b> economies of scale (lower unit costs), easier to raise finance, market power, can afford R&amp;D and advertising, diversify risk.<br><b>Disadvantages:</b> diseconomies of scale, slower decisions, less personal, may be remote from customers, may abuse market power.</p></div>
  </div>
'''
steppers = [
  ("Production chain across the three sectors", "--accent", ["Primary: a farmer grows wheat", "Secondary: a mill turns it into flour and a bakery bakes bread", "Tertiary: a supermarket sells the bread", "Each sector adds value", "The three sectors are linked"]),
  ("Why large firms have lower costs", "--good", ["A large firm buys materials in bulk", "It gets discounts and uses specialised machines", "Output is high so fixed costs are spread", "Cost per unit is lower", "Large firms may undercut small firms"]),
]
lab1 = dict(title="Share of the economy by sector", intro="Set the share of output by sector for an economy. See which stage of development it looks like.", rl=["Tertiary share", "Looks like", "Total (check)"],
  sliders=[("Primary sector share (%)", 0, 80, 5, 10, "v + '%'"), ("Secondary sector share (%)", 0, 80, 5, 25, "v + '%'")],
  fn="const t = Math.max(0, 100 - v[0] - v[1]), st = v[0] >= 40 ? 'A low-income, farm-based economy' : t >= 60 ? 'A developed service economy' : 'An industrialising economy'; return { r: [t + '%', st, (v[0] + v[1] + t) + '%'], t: 'Primary ' + v[0] + '%, secondary ' + v[1] + '% and tertiary ' + t + '%: ' + st.toLowerCase() + '. As incomes rise, economies usually move from primary to secondary and then to tertiary activity.', bars: [['Primary', v[0], '--good'], ['Secondary', v[1], '--warn'], ['Tertiary', t, '--accent']] };")
lab2 = dict(title="Classify the firm", intro="Pick a firm to see its sector and ownership.", h1="Sector", h2="Ownership and why",
  items=[("A wheat farm", "Primary", "Private; grows raw materials."), ("A car factory", "Secondary", "Private; manufactures."), ("A state hospital", "Tertiary", "Public; provides a service."), ("A coal mine", "Primary", "Private or public; extracts."), ("A private bank", "Tertiary", "Private; provides finance."), ("A state-owned rail firm", "Tertiary", "Public; provides transport.")])
cl = [("Which <b>sector</b> is each firm?", ["Primary", "Secondary", "Tertiary"], [("A fishing company", 0), ("A copper mine", 0), ("A shoe factory", 1), ("A construction firm", 1), ("A hairdresser", 2), ("An airline", 2)], "Extract, make, serve."),
      ("Is each an advantage of a <b>small firm</b> or a <b>large firm</b>?", ["Small firm", "Large firm"], [("Personal service", 0), ("Flexible decision-making", 0), ("Close contact with customers", 0), ("Economies of scale", 1), ("Easier to raise finance", 1), ("Can afford research", 1)], "Size matters.")]
match = [["Primary sector", "Extracts natural resources"], ["Secondary sector", "Manufactures and builds"], ["Tertiary sector", "Provides services"], ["Private sector", "Firms owned by individuals or shareholders"], ["Public sector", "Firms owned by the government"], ["Diseconomies of scale", "Rising unit costs from being too large"]]
order = ("Put the chain in order: <b>how a loaf of bread moves through the sectors</b>.", ["A farmer grows wheat (primary)", "A mill turns wheat into flour (secondary)", "A bakery makes bread (secondary)", "A shop sells bread (tertiary)", "The consumer buys the bread"], "From farm to consumer.")
calcs = [("A country's output is $100bn: primary $15bn and secondary $30bn. What percentage is tertiary?", 55, "100 − 15 − 30 = $55bn: <b>55%</b>.", None, None), ("A firm has 200 workers; a small firm has 20. How many times larger is the first?", 10, "200 ÷ 20 = <b>10</b>.", None, None)]
mcq = [("Mining is in the:", ["Primary sector", "Secondary sector", "Tertiary sector", "Public sector only"], 0, "Extraction."), ("Car manufacturing is in the:", ["Primary sector", "Secondary sector", "Tertiary sector", "Quaternary sector"], 1, "Making goods."), ("Banking is in the:", ["Primary sector", "Secondary sector", "Tertiary sector", "Public sector only"], 2, "A service."), ("A public sector firm is owned by:", ["Shareholders", "The government", "Families", "Customers"], 1, "State ownership."), ("An advantage of small firms is:", ["Economies of scale", "Personal service", "Easy finance", "Market power"], 1, "Close to customers.")]
cards = [("Primary sector", "Firms that extract or grow natural resources."), ("Secondary sector", "Firms that manufacture or build."), ("Tertiary sector", "Firms that provide services."), ("Private sector", "Firms owned by individuals or shareholders."), ("Public sector", "Firms owned by the government."), ("Small firm", "A firm with few employees and little output."), ("Large firm", "A firm with many employees and large output."), ("Economies of scale", "Lower unit costs from larger size."), ("Diseconomies of scale", "Higher unit costs from being too large.")]
exam_qs = [
  Q(1, "Identify", 3, "Identify the primary, secondary and tertiary sector firm in this list: a bank, a coal mine, a car factory.", "Coal mine; car factory; bank.", "[K|Primary: coal mine.] [K|Secondary: car factory.] [K|Tertiary: bank.]"),
  Q(2, "Explain", 4, "Explain two advantages of small firms.", "Personal service, flexibility.", "[K|Small firms can offer personal service.] [N|They know their customers, which builds loyalty.] [K|They can make decisions quickly.] [N|They can respond to changes in demand faster than large firms.]"),
  Q(3, "Explain", 4, "Explain two advantages of large firms.", "Economies of scale; finance.", "[K|Large firms benefit from economies of scale,] [N|so cost per unit is lower.] [K|They find it easier to raise finance,] [N|so they can invest and expand.]"),
  Q(4, "Explain", 4, "Explain the difference between private sector and public sector firms.", "Ownership; aims.", "[K|Private sector firms are owned by individuals or shareholders] [N|and aim mainly to make a profit.] [K|Public sector firms are owned by the government] [N|and aim to provide a service or promote social welfare.]"),
]
tips_ = [("Primary: extract; secondary: make; tertiary: serve.", "Use examples."), ("Private: profit; public: service.", "Ownership and aims."), ("Small: personal, flexible; large: scale.", "Both sides."), ("As economies develop, tertiary grows.", "Useful evaluation.")]
real_items = [("Apple and Amazon", "Large firms with huge scale, market power and global supply chains.", "Large firms."), ("Local bakeries", "Small firms known for personal service.", "Small firms."), ("NHS hospitals", "Public sector providers of healthcare.", "Public sector."), ("Saudi Aramco", "A very large primary-sector firm, mostly state-owned.", "Primary and public.")]
review("ig-types-of-firms", "f341", "3.4.1", "Different Types of Firms", "Primary, secondary and tertiary firms, private and public sector firms, and small and large firms. Syllabus 3.4.1.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Identify", "Explain"], real_items)

# ---------------------------------------------------------------- 3.4.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <span class="kw">merger</span> is when two or more firms join to form one. There are three types. A <b>horizontal merger</b> joins firms at the <b>same stage</b> of production in the same industry. A <b>vertical merger</b> joins firms at <b>different stages</b> of the same production chain. A <b>conglomerate merger</b> joins firms in <b>different industries</b>.</p></div>

  <h2>Types of merger</h2>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Definition</th><th>Example</th><th>Advantages</th><th>Disadvantages</th></tr>
    <tr><td><b>Horizontal</b></td><td>Firms at the same stage in the same industry</td><td>Two supermarkets; two car makers</td><td>Economies of scale; more market share; less competition; cost savings from removing duplication</td><td>Possible monopoly power and higher prices; job losses; diseconomies of scale; culture clashes</td></tr>
    <tr><td><b>Vertical</b></td><td>Firms at different stages of the same chain: <b>backward</b> (towards suppliers) or <b>forward</b> (towards customers)</td><td>A bakery buying a flour mill (backward); a brewer buying pubs (forward)</td><td>Secure supplies or outlets; cut out middlemen's profit; better quality control</td><td>Less flexibility; may lack expertise in the new stage; may reduce competition</td></tr>
    <tr><td><b>Conglomerate</b></td><td>Firms in unrelated industries</td><td>A food firm merging with a mobile phone firm</td><td>Spreads risk (diversification); access to new markets; use of surplus profits</td><td>Lack of expertise; no economies of scale; managing different businesses is hard</td></tr>
  </table></div>

  <h2>Why firms merge</h2>
  <ul>
    <li>To grow quickly and reach <b>economies of scale</b>.</li>
    <li>To gain <b>market power</b> or remove rivals.</li>
    <li>To <b>spread risk</b> or enter new markets.</li>
    <li>To secure <b>supply chains</b> or outlets.</li>
  </ul>
  <p class="note">Mergers can reduce competition, so governments (competition authorities) may investigate or block large mergers.</p>
'''
steppers = [
  ("A horizontal merger", "--accent", ["Two supermarket chains merge", "Combined size raises buying power", "Costs fall through economies of scale", "Competition in the market falls", "Prices may rise if market power grows"]),
  ("A vertical merger", "--good", ["A bakery buys a flour mill (backward integration)", "It controls its flour supply", "It cuts out the miller's profit margin", "Quality and supply are more secure", "But the bakery needs new skills to run a mill"]),
  ("A conglomerate merger", "--warn", ["A food firm buys a software firm", "Its profits are spread across industries", "A fall in food demand matters less", "But managers lack software experience", "Gains are mainly diversification, not scale"]),
]
lab1 = dict(title="Merger savings", intro="Two firms merge. Set their costs and the savings from merging and see the effect on unit costs.", rl=["Combined output", "Unit cost before", "Unit cost after"],
  sliders=[("Output of each firm (units)", 100, 1000, 100, 500, "v"), ("Cost per unit before ($)", 5, 30, 1, 20, "'$' + v"), ("Cost saving from the merger (%)", 0, 30, 5, 10, "v + '%'")],
  fn="const q = v[0] * 2, after = v[1] * (1 - v[2] / 100), saving = (v[1] - after) * q; return { r: [q + ' units', '$' + v[1].toFixed(2), '$' + after.toFixed(2)], t: 'Two firms each making ' + v[0] + ' units at $' + v[1] + ' merge into one making ' + q + ' units. A ' + v[2] + '% saving cuts unit cost to $' + after.toFixed(2) + ' and saves $' + saving.toFixed(0) + ' in total. Gains come from economies of scale (horizontal merger), but if the merged firm has market power, prices could rise.', bars: [['Cost before', v[1], '--bad'], ['Cost after', after, '--good']] };")
lab2 = dict(title="Which type of merger?", intro="Pick a merger to see its type and why.", h1="Type", h2="Why",
  items=[("Two car makers merge", "Horizontal", "Same stage, same industry."), ("A bakery buys a flour mill", "Vertical (backward)", "Different stage, towards suppliers."), ("A brewer buys pubs", "Vertical (forward)", "Different stage, towards customers."), ("A food firm buys a software firm", "Conglomerate", "Unrelated industries."), ("Two banks merge", "Horizontal", "Same stage, same industry."), ("A car maker buys a tyre firm", "Vertical (backward)", "Supplier.")])
cl = [("Which <b>type of merger</b> is each?", ["Horizontal", "Vertical", "Conglomerate"], [("Two supermarkets", 0), ("Two airlines", 0), ("A brewer and a chain of pubs", 1), ("A bakery and a flour mill", 1), ("A food firm and a phone maker", 2), ("A bank and a car maker", 2)], "Same, linked, unrelated."),
      ("Is each an <b>advantage</b> or a <b>disadvantage</b> of mergers?", ["Advantage", "Disadvantage"], [("Economies of scale", 0), ("Spreading risk", 0), ("Secure supplies", 0), ("Job losses", 1), ("Less competition and higher prices", 1), ("Culture clashes", 1)], "Weigh both.")]
match = [["Merger", "Two firms joining to form one"], ["Horizontal merger", "Same stage, same industry"], ["Vertical merger", "Different stages of the same chain"], ["Conglomerate merger", "Firms in unrelated industries"], ["Backward integration", "Merging with a supplier"], ["Diversification", "Spreading risk across different activities"]]
order = ("Put the chain in order: <b>how a horizontal merger may raise prices</b>.", ["Two rivals merge", "Competition in the market falls", "The merged firm gains market power", "It faces less pressure to cut prices", "Prices may rise"], "Market power.")
calcs = [("Two firms each have $50m revenue and merge. Costs fall by $4m. If total costs were $80m, what are the new costs ($m)?", 76, "80 − 4 = <b>$76m</b>.", None, None), ("Firm A has 30% of the market and Firm B 25%. What is the combined share (%)?", 55, "30 + 25 = <b>55%</b>.", None, None)]
mcq = [("A horizontal merger joins firms:", ["At different stages", "At the same stage in the same industry", "In different industries", "Abroad only"], 1, "Same stage."), ("A bakery buying a flour mill is:", ["Horizontal", "Vertical", "Conglomerate", "Hostile"], 1, "Backward vertical."), ("A conglomerate merger helps to:", ["Spread risk", "Create a monopoly", "Cut competition", "Raise prices"], 0, "Diversification."), ("A disadvantage of horizontal mergers is:", ["Economies of scale", "Possible monopoly power", "Diversification", "Secure supplies"], 1, "Less competition."), ("Forward integration is merging with a:", ["Supplier", "Customer or retailer", "Rival", "Bank"], 1, "Towards the customer.")]
cards = [("Merger", "Two firms joining to form one."), ("Horizontal merger", "Firms at the same stage in the same industry."), ("Vertical merger", "Firms at different stages of the same chain."), ("Conglomerate merger", "Firms in unrelated industries."), ("Backward integration", "Merging with a supplier."), ("Forward integration", "Merging with a retailer or customer."), ("Diversification", "Spreading risk across different activities."), ("Market power", "The ability to influence price."), ("Competition authority", "A body that investigates mergers.")]
exam_qs = [
  Q(1, "Define", 2, "Define a horizontal merger.", "Same stage, same industry.", "[K|A horizontal merger is when firms at the same stage of production] [K|in the same industry join together.]"),
  Q(2, "Explain", 4, "Explain the difference between a vertical and a conglomerate merger.", "Linked stages vs unrelated.", "[K|A vertical merger joins firms at different stages of the same production chain,] [N|for example a brewer buying pubs.] [K|A conglomerate merger joins firms in unrelated industries,] [N|for example a food firm buying a software company.]"),
  Q(3, "Explain", 4, "Explain two advantages of a horizontal merger for firms.", "Scale, market share, less competition.", "[K|The merged firm can gain economies of scale,] [N|so unit costs fall.] [K|It gains a larger market share and less competition,] [N|so it may raise prices or profit.]"),
  Q(4, "Discuss", 8, "Discuss whether a merger between two large supermarkets would benefit consumers.", "Lower costs, prices vs market power, choice. Judgement.", "[K|A horizontal merger could create economies of scale, lowering costs and possibly prices.] [N|Bigger firms may offer wider choice and invest more.] [N|However, less competition may let the merged firm raise prices and cut choice.] [N|Smaller suppliers and workers may lose out.] [E|Overall, consumers gain only if cost savings are passed on and competition remains strong, so regulators may need to approve it carefully.]", key=True),
]
tips_ = [("Three types: horizontal, vertical, conglomerate.", "Define each."), ("Use examples.", "Supermarkets, bakery and mill, food and phones."), ("Advantages and disadvantages.", "Scale vs market power."), ("Link to competition.", "Regulators may block.")]
real_items = [("Disney and Pixar", "Horizontal-style combinations in entertainment can raise market share.", "Merger motives."), ("Amazon buying Whole Foods", "A move into grocery retail, partly diversification.", "Entering new markets."), ("Facebook (Meta) buying Instagram", "Acquiring a rival to grow market share.", "Horizontal."), ("Brewers owning pubs", "Forward integration ensures outlets for their beer.", "Vertical.")]
review("ig-mergers", "f342", "3.4.2", "Mergers", "Horizontal, vertical and conglomerate mergers, with examples, advantages and disadvantages. Syllabus 3.4.2.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Explain", "Discuss"], real_items)

# ---------------------------------------------------------------- 3.4.3
ATCJS = '''
const PXo = (q) => 90 + q * 5, PYc = (c) => 310 - (c - 6) * 9;
const atcF = (q, sh) => 12 + 0.004 * Math.pow(q - 60, 2) - (sh || 0);
function atcAxes() { return SV.line(PXo(0), PYc(6), PXo(0), PYc(32)) + SV.line(PXo(0), PYc(6), PXo(130), PYc(6)) + SV.text(PXo(0) + 8, 14, "Average total cost ($ per unit)", "sm") + SV.text(PXo(130), PYc(6) + 24, "Output (units)", "sm", { "text-anchor": "end" }); }
function atcPath(sh) { let d = ""; for (let q = 8; q <= 118; q += 2) d += (d ? "L" : "M") + PXo(q).toFixed(1) + " " + PYc(atcF(q, sh)).toFixed(1); return d; }
function atcDraw(sh, q, show) {
  let o = atcAxes() + SV.path(atcPath(0), sh ? "c3" : "c1");
  if (sh) o += SV.path(atcPath(sh), "c2") + SV.text(PXo(112), PYc(atcF(112, sh)) - 8, "ATC₁", "lbl bd t2");
  else o += SV.text(PXo(112), PYc(atcF(112, 0)) - 8, "ATC", "lbl bd t1");
  if (show) { o += SV.rect(PXo(8), PYc(31), PXo(60) - PXo(8), PYc(6) - PYc(31), "", { style: "fill:var(--good)", opacity: 0.1 }) + SV.rect(PXo(60), PYc(31), PXo(118) - PXo(60), PYc(6) - PYc(31), "", { style: "fill:var(--bad)", opacity: 0.1 }) + SV.text(PXo(34), PYc(30), "Economies of scale", "sm bd t3", { "text-anchor": "middle" }) + SV.text(PXo(89), PYc(30), "Diseconomies of scale", "sm bd t4", { "text-anchor": "middle" }) + SV.line(PXo(60), PYc(12), PXo(60), PYc(6), "gr") + SV.text(PXo(60), PYc(6) + 18, "Minimum efficient scale", "sm bd", { "text-anchor": "middle" }); }
  if (q) o += SV.line(PXo(q), PYc(atcF(q, sh || 0)), PXo(q), PYc(6), "gr") + SV.line(PXo(0), PYc(atcF(q, sh || 0)), PXo(q), PYc(atcF(q, sh || 0)), "gr") + SV.circle(PXo(q), PYc(atcF(q, sh || 0)), 7, "dot2") + SV.text(PXo(0) - 8, PYc(atcF(q, sh || 0)), "$" + atcF(q, sh || 0).toFixed(1), "sm bd", { "text-anchor": "end" }) + SV.text(PXo(q), PYc(6) + 18, q, "sm bd", { "text-anchor": "middle" });
  return o;
}
'''
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Economies of scale</span> are the advantages of producing on a larger scale: <b>average total cost (ATC) falls as output rises</b>. <span class="kw">Diseconomies of scale</span> are the disadvantages of becoming too large: ATC <b>rises</b> as output rises. Together they give the <b>U-shaped ATC curve</b>.</p></div>

  <h2>Internal economies of scale (within the firm)</h2>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>How unit costs fall</th></tr>
    <tr><td><b>Purchasing (bulk-buying)</b></td><td>Large orders earn discounts from suppliers</td></tr>
    <tr><td><b>Technical</b></td><td>Large firms use bigger, more efficient machines and mass production</td></tr>
    <tr><td><b>Managerial</b></td><td>Specialist managers raise efficiency</td></tr>
    <tr><td><b>Financial</b></td><td>Large firms borrow at lower interest and raise finance more easily</td></tr>
    <tr><td><b>Marketing</b></td><td>Advertising costs are spread over more units</td></tr>
    <tr><td><b>Risk-bearing</b></td><td>Diversifying products and markets reduces risk</td></tr>
  </table></div>

  <h2>External economies of scale (from the industry)</h2>
  <ul>
    <li>Industry growth brings <b>skilled labour pools</b>, specialist suppliers, better transport and shared research: <b>all firms in the industry</b> benefit (for example the tech cluster in Silicon Valley).</li>
    <li>They shift the whole ATC curve <b>downwards</b>.</li>
  </ul>

  <h2>Diseconomies of scale</h2>
  <ul>
    <li><b>Internal:</b> poor communication, slow decisions, management difficulties, low morale and motivation, weak control and coordination.</li>
    <li><b>External:</b> congestion, rising wages and land prices, shortage of resources as an industry grows too large.</li>
  </ul>

  <h2>The ATC diagram</h2>
  <ul>
    <li>ATC falls as output rises (<b>economies of scale</b>), reaches a <b>minimum</b> (the lowest cost per unit, the minimum efficient scale), then rises (<b>diseconomies of scale</b>).</li>
    <li><b>External economies</b> shift the whole ATC curve down; <b>external diseconomies</b> shift it up.</li>
  </ul>
'''
steppers = [
  dict(title="The U-shaped ATC curve", base="{ sh: 0, q: 0, show: 0 }", draw="(s) => atcDraw(s.sh, s.q, s.show)", steps="""[
  { cap: "Average total cost (ATC) at different levels of output.", s: { sh: 0, q: 0, show: 0 } },
  { cap: "At low output ATC is high. As output rises, <b>economies of scale</b> cut ATC.", s: { sh: 0, q: 20, show: 1 } },
  { cap: "At <b>minimum efficient scale</b> ATC is at its lowest.", s: { sh: 0, q: 60, show: 1 } },
  { cap: "Beyond that, <b>diseconomies of scale</b> raise ATC again.", s: { sh: 0, q: 100, show: 1 } },
] """),
  dict(title="External economies of scale", base="{ sh: 0, q: 60, show: 0 }", draw="(s) => atcDraw(s.sh, s.q, s.show)", steps="""[
  { cap: "A firm produces 60 units at ATC $12.", s: { sh: 0, q: 60, show: 0 } },
  { cap: "The industry grows: skilled workers, suppliers and transport improve for <b>all firms</b>. The whole ATC curve shifts <b>down</b> to ATC₁: <b>external economies of scale</b>.", s: { sh: 3, q: 60, show: 0 } },
] """),
  ("Internal diseconomies of scale", "--bad", ["A firm grows very large", "Communication between departments slows", "Decisions take longer; workers feel remote", "Productivity and quality fall", "Average cost per unit rises"]),
]
lab1 = dict(title="Where is the firm on its ATC curve?", intro="Move output along the ATC curve and add an external economy of scale that shifts the curve down.", rl=["ATC", "Scale effect", "Minimum ATC"],
  sliders=[("Output (units)", 10, 115, 5, 30, "v"), ("External economies (fall in ATC, $)", 0, 5, 1, 0, "'$' + v")],
  fn="const c = atcF(v[0], v[1]), st = v[0] < 55 ? 'Economies of scale (ATC falling)' : v[0] <= 65 ? 'Close to minimum efficient scale' : 'Diseconomies of scale (ATC rising)'; return { r: ['$' + c.toFixed(1), st, '$' + (12 - v[1]).toFixed(1)], t: 'At ' + v[0] + ' units ATC is $' + c.toFixed(1) + ': ' + st.toLowerCase() + '. ' + (v[1] ? 'External economies have shifted the whole curve down by $' + v[1] + ', so every output level is cheaper.' : 'Raise the external economies slider to shift the ATC curve downwards.'), svg: atcDraw(v[1], v[0], 1) };")
lab2 = dict(title="Economy or diseconomy?", intro="Pick an effect to see which type of economy or diseconomy of scale it shows.", h1="Type", h2="Why",
  items=[("A big firm gets bulk discounts", "Internal economy (purchasing)", "Large orders cost less per unit."), ("Specialist managers raise efficiency", "Internal economy (managerial)", "Better management."), ("A skilled labour pool grows near the industry", "External economy", "All firms benefit."), ("Communication slows in a huge firm", "Internal diseconomy", "Poor coordination."), ("Congestion raises transport costs", "External diseconomy", "Industry too large for its area."), ("A large firm borrows at lower interest", "Internal economy (financial)", "Lenders trust it.")])
cl = [("Is each an <b>economy</b> or a <b>diseconomy</b> of scale?", ["Economy of scale", "Diseconomy of scale"], [("Bulk-buying discounts", 0), ("Cheaper loans for big firms", 0), ("Specialist managers", 0), ("Slow communication", 1), ("Low morale in a huge workforce", 1), ("Management hard to coordinate", 1)], "Unit costs fall or rise."),
      ("Is each <b>internal</b> or <b>external</b>?", ["Internal", "External"], [("Technical economies from large machines", 0), ("Purchasing discounts", 0), ("Slow communication in the firm", 0), ("A skilled labour pool in the region", 1), ("Better transport links built for the industry", 1), ("Congestion in an industrial area", 1)], "Within the firm vs the industry.")]
match = [["Economies of scale", "Unit costs fall as output rises"], ["Diseconomies of scale", "Unit costs rise as output rises"], ["Internal economies", "Savings within the firm"], ["External economies", "Savings from the industry's growth"], ["Average total cost", "Total cost divided by output"], ["Minimum efficient scale", "The output with the lowest ATC"]]
order = ("Put the chain in order: <b>how bulk-buying leads to economies of scale</b>.", ["A firm grows and orders more materials", "Suppliers give discounts for large orders", "The cost of inputs per unit falls", "Average total cost falls", "The firm gains an economy of scale"], "Purchasing economy.")
calcs = [("Total cost is $6,000 for 500 units. What is ATC ($)?", 12, "6,000 ÷ 500 = <b>$12</b>.", None, None), ("ATC is $12 at 60 units and $14 at 100 units. By what percentage does ATC rise?", 17, "2 ÷ 12 × 100 ≈ <b>17%</b>.", None, None)]
mcq = [("Economies of scale mean:", ["Unit costs fall as output rises", "Unit costs rise as output rises", "Fixed costs rise", "Prices fall"], 0, "Lower ATC."), ("A diseconomy of scale is:", ["Bulk-buying discounts", "Poor communication in a large firm", "Cheaper loans", "Specialist managers"], 1, "Unit costs rise."), ("External economies of scale:", ["Affect one firm only", "Benefit all firms in the industry", "Raise costs", "Are internal"], 1, "Industry-wide."), ("On the ATC curve, the lowest point is:", ["Where ATC is highest", "Minimum efficient scale", "Zero output", "Maximum output"], 1, "Lowest unit cost."), ("Which is an internal economy?", ["A skilled labour pool in the region", "Better local roads", "Bulk-buying discounts", "A nearby supplier"], 2, "Within the firm.")]
cards = [("Economies of scale", "Falling average cost as output increases."), ("Diseconomies of scale", "Rising average cost as output increases."), ("Internal economies", "Cost savings arising within a firm."), ("External economies", "Cost savings arising from industry growth."), ("Average total cost", "Total cost divided by output."), ("Minimum efficient scale", "The output at which ATC is lowest."), ("Bulk-buying", "Buying inputs in large quantities for a discount."), ("Technical economies", "Using larger, more efficient machinery."), ("Managerial economies", "Savings from specialist managers.")]
exam_qs = [
  Q(1, "Define", 2, "Define economies of scale.", "Average costs fall as output rises.", "[K|Economies of scale are the advantages of large-scale production] [K|that cause average total costs to fall as output rises.]"),
  Q(2, "Explain", 4, "Explain two internal economies of scale.", "Purchasing, technical, managerial, financial.", "[K|Purchasing economies: large firms buy in bulk.] [N|They get discounts, so cost per unit falls.] [K|Technical economies: large firms use efficient machines.] [N|Output per worker rises and unit costs fall.]"),
  Q(3, "Explain", 4, "Explain two causes of diseconomies of scale.", "Communication, management, morale.", "[K|Communication problems in a large firm slow decisions,] [N|so costs per unit rise.] [K|Workers may feel remote and less motivated,] [N|so productivity falls and unit costs rise.]"),
  Q(4, "Analyse", 6, "Analyse, using an ATC diagram, how a firm may experience economies and diseconomies of scale.", "U-shaped ATC; falling then rising.", "[K|ATC falls as output rises because of economies of scale such as bulk-buying and specialisation.] [N|ATC reaches a minimum at the minimum efficient scale.] [N|Beyond this, communication and coordination problems raise ATC: diseconomies of scale.] [E|The firm should aim to operate near the minimum.]", key=True),
]
tips_ = [("Draw a U-shaped ATC and label axes.", "Mark minimum efficient scale."), ("Internal vs external.", "Within the firm or industry."), ("Give causes for both economies and diseconomies.", "Two of each."), ("External economies shift the curve down.", "Internal ones are movements along it.")]
real_items = [("Supermarket giants", "Large chains negotiate low prices from suppliers.", "Purchasing economies."), ("Silicon Valley", "A cluster of skilled workers and suppliers lowers costs for all tech firms.", "External economies."), ("Over-large corporations", "Some very large firms split up because management became too complex.", "Diseconomies."), ("Mass car production", "Assembly lines cut cost per car.", "Technical economies.")]
review("ig-economies-of-scale", "f343", "3.4.3", "Economies and Diseconomies of Scale", "How internal and external economies and diseconomies of scale affect costs, and the U-shaped ATC diagram. Syllabus 3.4.3.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Explain", "Analyse"], real_items, prelude=ATCJS)
