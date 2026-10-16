"""Syllabus 9.2.6 Sustainable economic growth (chapter 42). Run: python3 tools/artifact-kit/mk_sy926.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.2.6"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Sustainable economic growth</b> is growth that meets the needs of people today <b>without reducing the ability of future generations to meet theirs</b>: in terms of the earlier definitions, it raises productive potential without reducing <b>future</b> productive potential. It depends on how resources are <b>used and conserved</b>, because non-renewable resources run out and renewable ones can be harvested faster than they regrow. Growth can damage the <b>environment</b> and contribute to <b>climate change</b> through pollution, emissions and loss of habitats, which are <b>negative externalities</b>. Governments can respond with taxes, tradable permits, subsidies, regulation and international agreements, each with costs and limits.</p></div>

  <h2>1 · What sustainable growth means</h2>
  <ul>
    <li><b>Intergenerational equity:</b> fairness between present and future generations. Using up natural capital for today's output may leave less for later.</li>
    <li><b>Productive potential:</b> growth is sustainable if the stock of capital (including natural capital such as forests, fish stocks, soil and a stable climate) is maintained or replaced.</li>
    <li><b>GDP is not enough:</b> GDP does not subtract depletion or pollution. Measures such as <b>MEW</b> (Measure of Economic Welfare) and <b>green GDP</b> adjust for environmental costs and unpaid work.</li>
  </ul>
  <div class="tip"><b class="h">Sustainable growth versus sustainable development</b>Sustainable <b>growth</b> is about real output over time without eroding future capacity. Sustainable <b>development</b> is wider: long-run improvement in living standards (health, education, equity) without damage to the environment.</div>

  <h2>2 · Using and conserving resources</h2>
  <div class="grid2">
    <div class="card"><h3>Non-renewable</h3><p>Fossil fuels and minerals. Once used they are gone, so extraction today reduces what is left. Sustainability needs <b>substitutes</b>, <b>recycling</b>, efficiency and investment in other forms of capital.</p></div>
    <div class="card"><h3>Renewable</h3><p>Fish, forests, soil, water. They regenerate, so a <b>sustainable yield</b> exists: harvest no more than regrowth. Overfishing and deforestation harvest faster than regrowth, so the stock collapses.</p></div>
  </div>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Why markets overuse resources:</b> the full social cost is not paid (external costs), property rights are weak (the tragedy of the commons), and people discount the future.</li>
    <li><b>Conserving resources:</b> quotas and licences, property rights, recycling and reuse, efficiency standards, renewable energy and technology that cuts resource use per unit of output.</li>
  </ul>

  <h2>3 · Growth, the environment and climate change</h2>
  <div class="tw"><table class="t">
    <tr><th>Cost of growth</th><th>Link to economic theory</th></tr>
    <tr><td>Greenhouse gas emissions and climate change</td><td>A negative externality: the social cost of carbon is not in the market price, so output is above the social optimum (resource misallocation).</td></tr>
    <tr><td>Air, water and land pollution</td><td>External costs fall on third parties; MSC is above MPC.</td></tr>
    <tr><td>Deforestation, loss of biodiversity</td><td>Natural capital is used up; the habitat has no market price.</td></tr>
    <tr><td>Congestion and urban sprawl</td><td>Congestion is a classic negative externality.</td></tr>
  </table></div>
  <p>But growth also gives <b>resources and technology</b> to protect the environment: richer countries can afford cleaner technology and regulation. Some argue that pollution first rises then falls as income per head rises (an environmental Kuznets curve), though this is not automatic, and the poorest countries often bear the worst effects of climate change.</p>

  <h2>4 · Policies to reduce the impact of growth on the environment</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>How it works</th><th>Evaluation</th></tr>
    <tr><td><b>Carbon tax / pollution tax</b></td><td>Raises the private cost to the social cost, so output falls to the efficient level</td><td>Hard to set the right rate, may be regressive, may hurt competitiveness, but raises revenue</td></tr>
    <tr><td><b>Tradable permits</b> (emissions trading)</td><td>Caps total emissions; firms buy and sell the right to emit</td><td>Cap is certain but the permit price varies; needs monitoring; cap may be set too high</td></tr>
    <tr><td><b>Subsidies for renewables and R&amp;D</b></td><td>Lower the cost of clean energy and technology</td><td>Cost to taxpayers, may back the wrong technology, does not penalise polluters</td></tr>
    <tr><td><b>Regulation</b> (emission limits, bans)</td><td>Directly sets limits on pollution or activities</td><td>Certain outcome but inflexible, costly to enforce, no incentive to do better than the limit</td></tr>
    <tr><td><b>Property rights and conservation</b></td><td>Owners have an incentive to preserve the resource; protected areas, quotas</td><td>Hard to apply to the atmosphere or oceans</td></tr>
    <tr><td><b>International agreements</b></td><td>Countries commit to emission cuts (for example the Paris Agreement)</td><td>Free-rider problem, enforcement is weak, developing countries argue rich countries should do more</td></tr>
    <tr><td><b>Education and information, nudges</b></td><td>Change behaviour and preferences</td><td>Slow, limited effect on its own</td></tr>
  </table></div>
  <div class="tip"><b class="h">Evaluation checklist</b>Cost of implementation, environmental effectiveness, effect on production costs and jobs, fairness (regressive effects on poorer households), international spillovers and free riding, time lags and political feasibility.</div>
'''

watch = '''
  <h2>1 · A renewable resource: harvest versus regrowth</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stR"></div>
  <h2>2 · A carbon tax and the external cost</h2>
  <div id="stT"></div>
'''

explore = '''
  <h2>Lab 1 · Fish stock: can you keep harvesting?</h2>
  <p>A fish stock starts at 100 and regrows. Choose how much is caught each year and how fast the stock regenerates. Find out how long the harvest can continue.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Maximum sustainable yield</small><strong id="r1"></strong></div><div><small>Stock after 40 years</small><strong id="r2"></strong></div><div><small>Result</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Line chart of fish stock over 40 years for the chosen harvest rate"></svg></div></div></div>

  <h2>Lab 2 · Set the carbon tax</h2>
  <p>The market price of an energy-intensive good ignores a $20 external cost per unit. Set a tax and see output, price, emissions, revenue and the welfare loss that remains.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div>
    <div class="readout"><div><small>Output</small><strong id="t1"></strong></div><div><small>Emissions index</small><strong id="t2"></strong></div><div><small>Welfare loss left</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Demand, private and social marginal cost with a tax shifting the supply curve"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Sustainable or not?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the carbon tax chain in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Overfishing and the collapse of the Grand Banks cod", "Heavy fishing off Newfoundland caught fish faster than they could breed. The cod stock collapsed in the early 1990s and the fishery was closed, leaving thousands without work. Recovery has been slow.", "a renewable resource harvested above the sustainable yield. Use it for intergenerational equity, weak property rights and the case for quotas.") +
rw("The EU Emissions Trading System", "Large emitters in the EU must hold permits for each tonne of carbon dioxide. The number of permits is capped and falls over time; firms can trade them. The permit price has varied widely.", "tradable permits as a market-based policy. Evaluate on certainty of the cap against uncertainty of the price, and on carbon leakage if firms move abroad.") +
rw("Renewable energy subsidies", "Governments have supported solar and wind power through subsidies and guaranteed prices. Costs have fallen sharply as output has grown, and the share of renewables in electricity has risen in many countries.", "subsidies to speed up clean technology. Evaluate: cost to taxpayers, risk of backing the wrong technology, and no penalty on polluters.") +
rw("The Paris Agreement and free riders", "Almost all countries agreed to limit warming, but each sets its own targets and there are no strong penalties. A country gains from others cutting emissions even if it does not, which weakens commitment.", "international action and the free-rider problem. Mention that poorer countries argue that richer ones caused most past emissions.")
)

mc_exam = [
  ("What is meant by sustainable economic growth? (May/June 2022 · 32 · Q18, reworded)", ["Raising productive potential as fast as possible", "Raising productive potential using only low-cost resources", "Raising productive potential without reducing the potential of future generations", "Raising future potential as fast as possible"], 2, "Sustainable growth does not reduce future productive potential."),
  ("Which influence is least likely to promote sustainable growth in a developing economy? (Feb/March 2021 · 32 · Q18, reworded)", ["High saving rates", "Involvement in free trade", "Protected property rights", "Rapid population growth"], 3, "Rapid population growth can use up resources and dilute capital per head, so it is least supportive. High saving, trade and property rights support investment."),
  ("Which cause of growth is most likely to make growth sustainable? (Oct/Nov 2023 · 31 · Q20, reworded)", ["Deregulation of industry that uses minerals and fossil fuels", "More spending on environmental education, paid for by taxes on harmful goods", "Higher trade barriers to protect jobs", "Fewer planning rules to allow building in areas of natural beauty"], 1, "Education and taxes on harmful goods change behaviour and fund conservation. The other options increase resource use or damage."),
  ("A government wants sustainable growth in the fishing industry. Which policy is most likely to achieve it? (May/June 2023 · 31 · Q18, reworded)", ["Give bigger boats and nets to fishers", "Pay bonuses for larger catches", "Set up a co-operative so fishers get a higher price", "Subsidise fish farms so fishers can switch from sea fishing"], 3, "Fish farms reduce pressure on wild stocks. The other options encourage more catching."),
  ("Which policy to counter climate change is regulatory rather than market-based? (Oct/Nov 2023 · 31 · Q19, reworded)", ["Carbon taxes", "Tradable pollution permits", "Government subsidies", "Industrial emission standards"], 3, "Emission standards set limits by law. Taxes, permits and subsidies work through prices."),
  ("Which government measure is most likely to encourage faster and more sustainable growth? (Oct/Nov 2022 · 33 · Q18, reworded)", ["Subsidies to firms using recycled materials", "Grants to explore and exploit new oil deposits", "More spending on environmental education in schools", "Tougher laws on air and water emissions"], 0, "Recycling raises output while conserving resources. Oil exploration uses up finite resources."),
  ("What is additionally included when calculating the Measure of Economic Welfare (MEW) compared with GDP per head? (May/June 2021 · 31 · Q20, reworded)", ["The cost of paid work", "The cost of producing armaments", "An estimate of environmental damage", "The impact of the shadow economy"], 2, "MEW adjusts for environmental costs and the value of unpaid work and leisure."),
  ("Rapid growth is claimed to harm the environment. Which outcome would not harm it? (Feb/March 2022 · 32 · Q24, reworded)", ["More workers commuting by vehicle", "Higher incomes that reduce family size and fertility", "Moving workers from agriculture to manufacturing", "Using new technology to reach previously inaccessible natural resources"], 1, "Falling fertility reduces population pressure on resources. The other options raise pollution or resource use.")
]

exam = exam_page("sustainable growth, resources and climate change",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Sustainability and climate change questions are common in Paper 4 and often draw on externalities and market failure from earlier chapters. Reworded questions are below, with eight Paper 3 multiple choice questions.",
  [("Essay, 20 marks", "1", "Feb/March 2024 (42) Q2"), ("Essay, 25 marks", "1", "Oct/Nov 2020 (42) Q6"), ("Essay parts, 12 and 13 marks", "2", "May/June 2022 (42) Q4(a) and (b)"), ("Data response parts, 2 to 8 marks", "2", "May/June 2025 (42) 1(a), (b); Oct/Nov 2022 (43) 1(d)"), ("Multiple choice (Paper 3)", "8 shown below", "2020 to 2023")],
  [
  eq("Based on May/June 2025 · 9708/42 · Q1(a) and (b)", "2 + 4 marks", "(a) Define economic sustainability and give one example of a change that illustrates it. (b) Several countries refused to sign an international agreement to phase out coal. Comment on the possible effects on their economies.",
     ["<b>(a)</b> Meeting present economic needs without reducing the ability of future generations to do the same (1). An example such as switching from coal to renewable energy (1).",
      "<b>(b)</b> Possible benefits: cheap coal power keeps energy costs and production costs low, protecting jobs and competitiveness in the short run. Possible costs: trade penalties or carbon border taxes, lost investment in clean technology, pollution and health costs, stranded assets, worse climate effects (2 benefits or costs developed for 4 marks)."],
     "Define in one sentence plus an example. For (b), one short-run gain, then two longer-run costs."),
  eq("Based on May/June 2022 · 9708/42 · Q4(a)", "12 marks", "Explain how climate change may be seen as a result of resource misallocation.",
     ["Burning fossil fuels creates a negative externality: the social cost of emissions (climate damage, health costs) is not paid by producers or consumers.",
      "Show with marginal private cost and marginal social cost: the market equilibrium is where MPC meets demand, and output is above the social optimum where MSC meets demand. This is overproduction and misallocation.",
      "Level 4 (9 to 12) links externalities, private and social costs and benefits, and efficiency. A labelled diagram strengthens the answer.",
      "Add that missing property rights over the atmosphere and the long time horizon make the problem worse."],
     "Define the externality. Draw MPC, MSC and demand. Show the gap and the welfare loss. Link to misallocation."),
  eq("Based on May/June 2022 · 9708/42 · Q4(b)", "13 marks", "Evaluate two policies a government could use to reduce the impact of climate change.",
     ["Two policies from: carbon tax, subsidies for clean energy, bans or regulation, tradable permits, improved information.",
      "Analysis: how each changes costs, incentives and emissions.",
      "Evaluation: cost of implementation, effectiveness in cutting emissions, effect on production costs and jobs, whether the cost falls more on poorer households, international spillovers and free riding.",
      "Level 4 needs analysis of two policies and evaluation."],
     "Pick two contrasting policies, such as a carbon tax and subsidies. Mechanism, then strength and weakness of each. Judge which is more effective."),
  eq("Based on Feb/March 2024 · 9708/42 · Q2", "20 marks", "With the help of a diagram, assess how effective government intervention in the price mechanism could be in tackling the causes of climate change.",
     ["<b>Knowledge and analysis (14):</b> link between climate change and negative externalities; diagram with MPC, MSC and the welfare loss; intervention through the price mechanism such as a carbon tax, tradable permits or subsidies, and how each moves output towards the social optimum.",
      "<b>Evaluation (6):</b> difficulty valuing the external cost, tax set too high or low, global nature of the problem and free riding, impact on competitiveness and on low-income households, time lags, alternatives such as regulation."],
     "Externality diagram first. A tax shifting MPC to MSC. A second price-based tool. Then limits and a judgement."),
  eq("Based on Oct/Nov 2022 · 9708/43 · Q1(d)", "8 marks", "A developing country with large forests and a major cash-crop export is advised to expand production of that crop. The crop earns export revenue and jobs but expansion would clear forest. To what extent do you agree with the advice?",
     ["For: export earnings, jobs, tax revenue, poverty reduction, foreign exchange, multiplier effects.",
      "Against: loss of forest and habitats, greenhouse gas emissions, falling soil quality, risk of overdependence on one crop and price swings, possible trade restrictions by importers.",
      "A conclusion on balance: depends on the time horizon, alternatives and whether growth is sustainable."],
     "Two points for, two against, then a judgement on time horizon."),
  eq("Based on Oct/Nov 2020 · 9708/42 · Q6", "25 marks", "'Investment by multinational corporations in a developing country always promotes sustainable economic growth in that country.' Discuss.",
     ["Define sustainable growth. Explain how FDI may raise capital, technology, skills, jobs, exports and tax revenue.",
      "Counter: profit outflows, environmental damage, resource depletion, low-wage jobs, dependency, limited local linkages, transfer pricing, weak regulation.",
      "The word 'always' invites a judgement: it depends on the sector, the regulation and the contract terms, so 'not always'."],
     "Define sustainability. Benefits. Costs. Then the word 'always' and a conclusion.")
  ],
  )

tips = tips_html(
  [("Define sustainable growth in terms of future generations.", "Meeting needs now without reducing the ability to meet future needs, or raising potential without reducing future potential."),
   ("Use the externality diagram for climate questions.", "MPC, MSC and demand. Market output is above the social optimum. A tax shifts MPC to MSC."),
   ("Separate renewable and non-renewable.", "Renewable resources have a sustainable yield. Non-renewable resources are depleted whatever the rate, so substitutes and recycling matter."),
   ("Name two policies and compare them.", "A market-based tool (tax or permits) and a regulatory or subsidy tool. Analyse each then judge."),
   ("Mention the global problem.", "Climate change crosses borders, so free riding and fairness between rich and poor countries are key evaluation points."),
   ("Include the costs of policy.", "Higher prices, jobs lost in polluting industries, effect on poorer households, competitiveness."),
   ("Growth is not always the enemy.", "Richer countries may afford cleaner technology. Say growth could be made more sustainable, not just that it harms the environment.")],
  [("Define", "Sustainable economic growth is growth that meets the needs of the present without reducing the ability of future generations to meet their own needs."),
   ("Externality", "Burning fossil fuels creates a negative externality, because the social cost of emissions is not paid by the producer or consumer, so output is above the social optimum."),
   ("Carbon tax", "A carbon tax could raise the private cost of production to the social cost, which may reduce output and emissions."),
   ("Evaluate", "However, it is difficult to measure the external cost, so the tax may be set too high or too low."),
   ("Global", "Because climate change is global, countries may free-ride on the efforts of others.")],
  [CW["define"], CW["explain"], CW["assess"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- Learn picture and Watch 1: logistic stock ---------- */
function simStock(h, r, n = 40, K = 100) { const s = [K]; let x = K; for (let t = 0; t < n; t++) { x = Math.max(0, x + r * x * (1 - x / K) - h); s.push(x); } return s; }
const SX = (t) => 70 + t * 16.5, SY = (v) => 300 - v * 2.5;
function stockDraw(s) {
  let o = axes(70, 300, 740, 40, "Years", "Fish stock") + SV.line(70, SY(100), 730, SY(100), "gr") + SV.text(66, SY(100) + 4, "100", "sm", { "text-anchor": "end" });
  [10, 20, 30, 40].forEach((t) => (o += SV.text(SX(t), 318, t, "sm", { "text-anchor": "middle" })));
  const A = simStock(s.h, 0.4), n = Math.round(s.n);
  if (s.show > 0) o += SV.path(Lib.ptsPath(A.slice(0, n + 1).map((v, i) => [SX(i), SY(v)])), s.h > 10 ? "c2" : "c3", op(1));
  if (s.show > 0) o += tag(SX(n) + 8, SY(A[n]) - 10, "harvest " + s.h + " a year", s.h > 10 ? "t2" : "t3");
  if (s.h === 10 && s.show > 0) o += tag(380, 62, "Maximum sustainable yield = 10 with regrowth 0.4", "t3", 1, "middle");
  if (s.h > 10 && s.show > 0 && A[n] < 1) o += tag(SX(n) - 8, SY(2) - 14, "stock collapses", "t2", 1, "end");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Fish stock over 40 years: stable when harvest is 8 or 10 a year, collapsing when harvest is 14 a year">${(() => { let o = axes(70, 300, 740, 40, "Years", "Resource stock") + SV.line(70, 50, 730, 50, "gr"); [[8, "c3", "harvest below regrowth: sustainable"], [10, "c1", "maximum sustainable yield"], [14, "c2", "overharvest: collapse"]].forEach(([h, c, l], i) => { const A = simStock(h, 0.4); o += SV.path(Lib.ptsPath(A.map((v, k) => [SX(k), SY(v) - 20 + 20])), c, {}); o += tag(SX(40) - 4, SY(A[40]) - 8 - (i === 1 ? 0 : 0), l, c === "c2" ? "t2" : c === "c3" ? "t3" : "t1", 1, "end"); }); return o; })()}</svg>`;
Lib.stepper($("#stR"), { w: 760, h: 340, label: "Fish stock over 40 years under three different harvest rates", base: { h: 8, n: 0, show: 0 }, draw: stockDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>A renewable resource.</b> A fish stock of 100 regrows each year: fast when it is small and plentiful food, slower as it nears its limit. There is a level of catch the stock can replace every year.", s: { h: 8, n: 0, show: 0 } },
  { cap: "<b>Harvest below regrowth.</b> Catching 8 a year is less than the stock can replace. The stock settles at a stable level and fishers can keep going. <b>This is sustainable.</b>", s: { h: 8, n: 40, show: 1 } },
  { cap: "<b>The maximum sustainable yield.</b> Catching 10 a year is the most the stock can replace at this regrowth rate. It stays stable at half its original size, with no margin for a bad year.", s: { h: 10, n: 40, show: 1 } },
  { cap: "<b>Overharvesting.</b> Catching 14 a year is more than the stock can replace. The stock falls faster and faster until it collapses. Short-run output rises, then the industry and its jobs vanish: <b>not sustainable</b>.", s: { h: 14, n: 40, show: 1 } },
] });

/* ---------- Watch 2: carbon tax ---------- */
const EX = (q) => 70 + q * 6.5, EY = (p) => 320 - p * 2.6;
function taxDraw(s) {
  const dmd = (q) => 100 - q, mpc = (q) => 10 + 0.5 * q, msc = (q) => 30 + 0.5 * q, tc = (q) => 10 + 0.5 * q + 20 * s.t;
  let o = axes(70, 320, 740, 30, "Output of the good", "Price and cost ($)");
  o += SV.line(EX(0), EY(dmd(0)), EX(100), EY(dmd(100)), "c1") + tag(EX(97), EY(dmd(97)) - 8, "Demand (MSB)", "t1", 1, "end");
  o += SV.line(EX(0), EY(mpc(0)), EX(100), EY(mpc(100)), "c2") + tag(EX(100) - 4, EY(mpc(100)) + 18, "MPC", "t2", 1, "end");
  if (s.e > 0) o += SV.line(EX(0), EY(msc(0)), EX(100), EY(msc(100)), "c3 dash", op(s.e)) + tag(EX(100) - 4, EY(msc(100)) - 10, "MSC", "t3", s.e, "end");
  if (s.t > 0) o += SV.line(EX(0), EY(tc(0)), EX(100), EY(tc(100)), "c4", op(s.t)) + tag(EX(0) + 8, EY(tc(0)) - 8, "MPC + tax", "t4", s.t);
  if (s.m > 0) o += SV.circle(EX(60), EY(40), 7, "dot2", op(s.m)) + SV.line(EX(60), EY(40), EX(60), 320, "gr", op(s.m)) + tag(EX(60) + 10, EY(40) + 22, "market: Q=60", "t2", s.m);
  if (s.o > 0) o += SV.circle(EX(46.7), EY(53.3), 7, "dot3", op(s.o)) + SV.line(EX(46.7), EY(53.3), EX(46.7), 320, "gr", op(s.o)) + tag(EX(46.7) - 10, EY(53.3) - 12, "optimum: Q=47", "t3", s.o, "end");
  if (s.w > 0) o += SV.poly([[EX(46.7), EY(53.3)], [EX(60), EY(40)], [EX(60), EY(60)]], "f2", op(s.w)) + tag(EX(63), EY(58), "welfare loss", "t2", s.w);
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 345, label: "Demand, private marginal cost and social marginal cost with a carbon tax moving output to the social optimum", base: { e: 0, t: 0, m: 0, o: 0, w: 0 }, draw: taxDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>The market ignores the damage.</b> Producers pay only their private cost (MPC). Where demand meets MPC the market produces <b>60 units</b> at a price of $40.", s: { m: 1 } },
  { cap: "<b>The external cost.</b> Burning fuel creates emissions that damage others by $20 a unit. Adding this to MPC gives the <b>marginal social cost (MSC)</b>.", s: { m: 1, e: 1 } },
  { cap: "<b>Overproduction.</b> The efficient output is where demand meets MSC: about <b>47 units</b>. The market produces too much, and the shaded triangle is the <b>welfare loss</b>. This is resource misallocation.", s: { m: 1, e: 1, o: 1, w: 1 } },
  { cap: "<b>A carbon tax of $20 per unit.</b> The tax raises producers' cost to MPC + tax, which lies on the MSC curve. Output falls to the efficient 47 units and the price consumers pay rises to about $53. The externality is internalised.", s: { m: 0.4, e: 1, o: 1, t: 1, w: 0.3 } },
] });

/* ---------- Lab 1: fish stock ---------- */
function labFish() {
  if (!$("#fh") || !$("#fr")) return;
  const h = +$("#fh").value, r = +$("#fr").value / 100, A = simStock(h, r), msy = r * 100 / 4;
  $("#r1").textContent = Lib.fmtN(msy, 1) + " a year"; $("#r2").textContent = Lib.fmtN(A[40], 0); const ok = A[40] > 20; $("#r3").textContent = A[40] <= 0.5 ? "Collapse" : ok ? "Sustainable" : "At risk";
  const gone = A.findIndex((v) => v <= 0.5);
  $("#rv").textContent = h > msy ? (gone > 0 ? `Catching ${h} a year is above the maximum sustainable yield of ${Lib.fmtN(msy, 1)}. The stock is wiped out after about ${gone} years.` : `Catching ${h} a year is above the maximum sustainable yield of ${Lib.fmtN(msy, 1)}, but the stock has not yet collapsed. It is at risk.`) : `Catching ${h} a year is at or below the maximum sustainable yield of ${Lib.fmtN(msy, 1)}. The stock settles at ${Lib.fmtN(A[40], 0)} and the harvest can continue.`;
  const X = (t) => 40 + t * 8.6, Y = (v) => 260 - v * 2.2;
  let o = SV.line(40, 260, 400, 260) + SV.line(40, 260, 40, 30) + SV.text(400, 282, "Years", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "Stock", "sm") + SV.line(40, Y(100), 400, Y(100), "gr");
  o += SV.path(Lib.ptsPath(A.map((v, i) => [X(i), Y(v)])), ok ? "c3" : "c2") + tag(396, Y(A[40]) - 8, "stock " + Lib.fmtN(A[40], 0), ok ? "t3" : "t2", 1, "end");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "fh", label: "Fish caught each year ", min: 0, max: 30, step: 1, value: 8, fmt: (v) => v, onInput: labFish });
Lib.slider($("#g2"), { id: "fr", label: "Regrowth rate (% a year) ", min: 20, max: 60, step: 5, value: 40, fmt: (v) => v, onInput: labFish });
labFish();

/* ---------- Lab 2: carbon tax ---------- */
function labTax() {
  if (!$("#ct")) return;
  const t = +$("#ct").value, Q = (90 - t) / 1.5, P = 100 - Q, nsb = (q) => 70 * q - 0.75 * q * q, loss = nsb(46.667) - nsb(Q);
  $("#t1").textContent = Lib.fmtN(Q, 1); $("#t2").textContent = Lib.fmtN(Q / 60 * 100, 0); $("#t3").textContent = "$" + Lib.fmtN(Math.max(loss, 0), 0);
  $("#tv").textContent = t === 20 ? `A $20 tax equals the external cost. Output falls to the efficient ${Lib.fmtN(Q, 1)} units, emissions fall to ${Lib.fmtN(Q / 60 * 100, 0)}% of the market level and the welfare loss is removed. Tax revenue is $${Lib.fmtN(t * Q, 0)}.` : t < 20 ? `The tax of $${t} is below the $20 external cost, so output is still too high and a welfare loss of about $${Lib.fmtN(loss, 0)} remains. Revenue $${Lib.fmtN(t * Q, 0)}.` : `The tax of $${t} is above the $20 external cost, so output is cut too far and a different welfare loss of about $${Lib.fmtN(loss, 0)} appears. Revenue $${Lib.fmtN(t * Q, 0)}.`;
  const X = (q) => 40 + q * 3.3, Y = (p) => 270 - p * 2.3;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 290, "Output", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "$", "sm");
  o += SV.line(X(0), Y(100), X(100), Y(0), "c1") + tag(X(100) - 2, Y(0) - 8, "D", "t1", 1, "end") + SV.line(X(0), Y(10), X(100), Y(60), "c2", op(0.5)) + SV.line(X(0), Y(30), X(100), Y(80), "c3 dash") + tag(X(100) - 2, Y(80) - 8, "MSC", "t3", 1, "end");
  o += SV.line(X(0), Y(10 + t), X(100), Y(60 + t), "c4") + tag(X(100) - 2, Y(60 + t) + 16, "MPC + tax", "t4", 1, "end") + SV.circle(X(Q), Y(P), 6, "dot4") + SV.line(X(Q), Y(P), X(Q), 270, "gr");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "ct", label: "Tax per unit ($) ", min: 0, max: 40, step: 2, value: 0, fmt: (v) => v, onInput: labTax });
labTax();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Is the activity consistent with sustainable growth?", ["Likely sustainable", "Likely unsustainable"],
  [("Catching fish at or below the regrowth rate", 0), ("Clear-cutting a rainforest for short-term timber", 1), ("Replanting a tree for every tree cut", 0), ("Burning more coal for cheap electricity with no carbon cost", 1), ("Investing carbon-tax revenue in solar and wind power", 0), ("Pumping groundwater faster than rain refills it", 1), ("Recycling metals and reusing components", 0), ("Exporting a non-renewable mineral and spending all the revenue on consumption", 1)],
  "Sustainable growth keeps future productive potential intact.") + MATCH([
  ["Sustainable growth", "Growth that does not reduce future generations' ability to meet their needs"],
  ["Intergenerational equity", "Fairness between present and future generations"],
  ["Negative externality", "A cost of production or consumption borne by a third party"],
  ["Tradable permit", "A right to emit a set amount of pollution that can be bought and sold"],
  ["Carbon tax", "A tax per tonne of emissions to raise private cost to social cost"],
  ["MEW", "A measure of welfare that adjusts GDP for environmental costs and unpaid work"]]) + ORDER(
  "Put the effect of a carbon tax in order.",
  ["The government taxes each tonne of carbon emitted", "Producers' marginal cost rises", "Output and prices adjust: price rises and quantity falls", "Emissions fall and the external cost is reduced", "The government uses the revenue, for example to fund renewables"],
  "The tax internalises the external cost and moves output towards the social optimum.") + CALC([
  {"q": "A country's GDP is $2,000bn. Environmental damage is estimated at $150bn and depletion of natural capital at $100bn. Calculate a green GDP measure (in $bn) by subtracting both.", "a": 1750, "unit": "$bn", "tol": 0.5, "hint": "2000 − 150 − 100.", "sol": "2000 − 150 − 100 = <b>$1,750bn</b>."},
  {"q": "A carbon tax cuts output of a polluting good from 60 units to 47 units. Calculate the percentage fall in output (to one decimal place).", "a": 21.7, "unit": "%", "tol": 0.1, "hint": "Change ÷ original × 100.", "sol": "13 ÷ 60 × 100 = <b>21.7%</b>."},
  {"q": "The government taxes 50 million tonnes of carbon at $30 a tonne. Calculate the tax revenue (in $m).", "a": 1500, "unit": "$m", "tol": 0.5, "hint": "Tonnes × tax per tonne.", "sol": "50 × 30 = <b>$1,500m</b>."},
  {"q": "A fish stock regrows by 40% of its size when it is small, and the maximum sustainable yield is rK ÷ 4. If K = 200 and r = 0.4, what is the maximum sustainable yield per year?", "a": 20, "tol": 0.01, "hint": "r × K ÷ 4.", "sol": "0.4 × 200 ÷ 4 = <b>20</b> per year."}]) + MCQ([
  ("Which would be an example of unsustainable growth?", ["Replanting forests at the rate they are cut", "Using solar power to replace coal", "Catching fish faster than they can breed", "Recycling aluminium"], 2, "Overharvesting reduces the stock that future generations can use."),
  ("Why do markets tend to overproduce goods with negative externalities?", ["Consumers value the goods too little", "Producers do not pay the external costs", "The government fixes the price", "Supply is perfectly inelastic"], 1, "The market price reflects private costs only, so output is above the social optimum."),
  ("A carbon tax equal to the marginal external cost will:", ["Raise output", "Move output to the socially efficient level", "Remove all pollution", "Reduce the price consumers pay"], 1, "The tax moves MPC to MSC. Pollution falls but is not eliminated."),
  ("Which is an advantage of tradable permits over a carbon tax?", ["The price of carbon is certain", "The total quantity of emissions is certain", "They are free to administer", "They remove the need for monitoring"], 1, "The cap fixes the quantity, while the permit price varies."),
  ("Which is the main reason international agreements on climate change are hard to enforce?", ["Countries cannot measure emissions", "Each country gains from others' efforts even if it does not act (free riding)", "Carbon taxes are illegal", "Emissions have no effect on other countries"], 1, "Because everyone benefits from a stable climate, each country has an incentive to free-ride.")
], "qz1") + CARDS([
  ("Sustainable growth", "Growth that does not reduce future productive potential."),
  ("Natural capital", "Stocks of natural resources such as forests, fish, soil and a stable climate."),
  ("Sustainable yield", "The harvest a renewable resource can replace each year."),
  ("Negative externality", "A cost to third parties that the market price ignores."),
  ("Carbon tax", "Tax on emissions to raise private cost to social cost."),
  ("Tradable permits", "Capped emission rights that firms can buy and sell."),
  ("Free rider", "Gains from others' action without contributing."),
  ("MEW", "Measure of Economic Welfare: GDP adjusted for environmental costs and unpaid work.")]) + MCQ(mc_exam)

build("sy926", "sustainable-economic-growth", "Sustainable Economic Growth", EY,
  "9.2.6: what sustainable growth means, using and conserving resources, the environmental cost of growth and climate change, and policies to reduce it. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
