"""Syllabus 11.6.1 Globalisation: meaning, causes and consequences. Run: python3 tools/artifact-kit/mk_sy1161.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.6.1"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Globalisation</b> is the growing integration of economies through <b>trade in goods and services, flows of capital and foreign direct investment, migration of labour, and the spread of technology, information and culture</b>. It has been driven by <b>falling transport and communication costs, trade liberalisation, multinational companies and global supply chains, deregulated capital markets</b> and the opening up of large economies such as China and India. Its consequences include <b>lower prices, more choice, faster growth and technology transfer</b>, but also <b>job losses in some industries, rising inequality, environmental damage, loss of sovereignty and greater exposure to shocks elsewhere</b>, so the gains are real but not shared equally.</p></div>

  <h2>1 · The meaning of globalisation</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Trade:</b> world trade has grown faster than world output, so trade makes up a larger share of GDP in most countries (a rise in openness).</li>
    <li><b>Capital flows:</b> FDI and portfolio investment move across borders in large amounts, and financial markets are linked worldwide.</li>
    <li><b>Labour:</b> migration and remittances connect labour markets, although labour is less mobile than capital.</li>
    <li><b>Technology and information:</b> ideas, patents and know-how spread quickly; production is organised in <b>global supply chains</b> (a product may be designed in one country, made from parts from several others and assembled in another).</li>
    <li><b>Culture and consumption:</b> the same brands, media and consumer tastes appear worldwide.</li>
  </ul>

  <h2>2 · Causes of globalisation</h2>
  <ul>
    <li><b>Lower transport and communication costs:</b> containerisation, cheaper air freight, the internet and mobile phones.</li>
    <li><b>Trade liberalisation:</b> reductions in tariffs and quotas through the GATT and World Trade Organization, regional agreements and unilateral reforms.</li>
    <li><b>Multinational companies and FDI:</b> firms locate production where costs are lowest and sell worldwide.</li>
    <li><b>Deregulation of capital markets</b> and the end of exchange controls, which allowed large capital flows.</li>
    <li><b>Political change:</b> the opening of China, the end of the Soviet bloc and market reforms in India and elsewhere added large labour forces and markets.</li>
    <li><b>Technology and rising incomes:</b> new products, automation and growing demand in emerging economies.</li>
  </ul>

  <h2>3 · Consequences of globalisation</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Benefits</th><th>Costs</th></tr>
    <tr><td><b>Consumers</b></td><td>Lower prices and greater variety</td><td>Product safety and quality concerns; loss of local varieties</td></tr>
    <tr><td><b>Workers</b></td><td>New jobs in export industries; higher wages in some sectors</td><td>Job losses (structural unemployment) in industries facing cheap imports; pressure on wages of low-skilled workers; poor conditions in some low-wage factories</td></tr>
    <tr><td><b>Firms</b></td><td>Larger markets, economies of scale, cheaper inputs, access to technology</td><td>Intense competition; supply chain risks</td></tr>
    <tr><td><b>Governments and economies</b></td><td>Faster growth, higher tax revenue, technology transfer, poverty reduction (as in East Asia)</td><td>Loss of policy independence and sovereignty; tax avoidance; exposure to shocks (the 2008 financial crisis, pandemics, shipping disruptions); dependence on a few trading partners</td></tr>
    <tr><td><b>Income distribution and environment</b></td><td>Convergence of incomes in fast-growing emerging economies</td><td>Rising inequality within many countries; environmental damage and transferred pollution; depletion of resources</td></tr>
  </table></div>
  <h3>High-income and low-income countries</h3>
  <ul>
    <li><b>High-income countries</b> gain cheaper goods and larger markets for high-value goods and services, but face job losses in manufacturing and inequality.</li>
    <li><b>Low-income countries</b> may gain markets, FDI, jobs and technology; growth and tax revenue may help living standards. But they can suffer from <b>dependence on primary exports, exploitation of labour, competition that destroys local industries, volatile capital flows and a lack of bargaining power</b>. The gains depend on whether they can diversify and have good institutions.</li>
  </ul>
  <h3>The backlash</h3>
  <p>Concerns about jobs, inequality and security have led to <b>protectionism</b> (higher tariffs and trade wars), calls to bring production back home, and tensions between major economies. These are threats to the continued growth of globalisation.</p>
  <div class="tip"><b class="h">Evaluation point</b>Whether globalisation raises living standards depends on whether the gains in GDP reach the poor, on the extent of environmental costs, on how well countries support displaced workers (retraining, social protection) and on the type of country. Gains are real in aggregate, but they are not automatically or equally shared, so the answer is usually "it depends".</div>
'''

watch = '''
  <h2>1 · Openness rising over time</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stT"></div>
  <h2>2 · Winners and losers</h2>
  <div id="stW"></div>
'''

explore = '''
  <h2>Lab 1 · Cheaper imports: consumers and displaced workers</h2>
  <p>An economy has $1,000m of spending on imported goods. Imports become cheaper, and some jobs in import-competing firms are lost (each displaced worker loses $40,000 of income a year until they find new work). Compare the gain to consumers with the loss to displaced workers.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Consumers gain</small><strong id="r1"></strong></div><div><small>Displaced workers lose</small><strong id="r2"></strong></div><div><small>Net</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of the gain to consumers, the loss to displaced workers and the net effect"></svg></div></div></div>

  <h2>Lab 2 · Openness and exposure to shocks</h2>
  <p>The more an economy depends on trade, the more a fall in demand abroad affects it. Set exports and imports as shares of GDP and the fall in foreign demand.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Openness</small><strong id="t1"></strong></div><div><small>Direct hit to GDP</small><strong id="t2"></strong></div><div><small>Exposure</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars of exports share, imports share and the direct hit to GDP from a fall in foreign demand"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Cause, benefit or cost of globalisation?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the chain from cheaper transport to a global supply chain in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The shipping container", "Standardised steel containers made loading and unloading cargo much cheaper and faster from the 1960s. Together with bigger ships and ports they cut the cost of moving goods across oceans, which made it profitable to make parts in one country and assemble them in another.", "falling transport costs as a cause of globalisation and global supply chains.") +
rw("China and the 'China shock'", "China's entry into the world trade system after 2001 made many consumer goods cheaper in rich countries but hit towns that made furniture, clothing and electronics, where jobs disappeared and some workers found it hard to retrain. China's incomes and exports rose very rapidly and hundreds of millions of people moved out of absolute poverty.", "benefits for a developing economy and costs for workers in high-income countries.") +
rw("The Suez Canal blockage and supply chains", "In 2021 a container ship stuck in the Suez Canal delayed hundreds of ships and caused shortages around the world. The event showed how interdependent supply chains have become and how a shock in one place can spread.", "interdependence and vulnerability to shocks.") +
rw("Trade tensions and tariffs", "In recent years some governments have raised tariffs on imports to protect jobs and national security and have encouraged firms to bring production home. Supporters point to jobs and resilience, while critics point to higher prices and retaliation.", "protectionism as a threat to globalisation.")
)

mc_exam = [
  ("What is not a threat to globalisation? (May/June 2024 · 31 · Q23, reworded)", ["Fear of losing jobs to immigrant workers", "Political tensions among major economies", "Stronger trade unions in industries that compete with imports", "Withdrawal of government support for inefficient industries"], 3, "Removing support for inefficient industries opens markets rather than restricting them. The other three encourage protectionism."),
  ("In 2021 a cargo ship carrying over 18,000 containers blocked the Suez Canal for seven days and delayed 350 ships, causing shortages around the world. Which consequence of globalisation does this best illustrate? (Oct/Nov 2023 · 32 · Q28, reworded)", ["Cheaper products for consumers", "Greater choice of products", "Increased interdependence between countries", "Increased migration of labour"], 2, "A disruption in one place spread because supply chains link countries together."),
  ("What is a likely result of globalisation? (Oct/Nov 2024 · 32 · Q30, reworded)", ["Absolute advantage replaces comparative advantage as the basis for trade", "Firms' supply chains are shortened", "Trade is less exposed to international shocks", "Higher standards of living"], 3, "Trade and growth raise real incomes, although not automatically for everyone. Supply chains lengthen and exposure to shocks increases."),
  ("What would increase structural unemployment in the manufacturing sector of the US? (Oct/Nov 2021 · 33 · Q21, reworded)", ["Asian exporters of manufactured goods to the US lower their labour costs per unit of output", "Tariffs on Asian manufacturing imports rise", "The share of US manufacturing workers in unions falls", "The US dollar's real effective exchange rate against Asian currencies falls"], 0, "Cheaper imports reduce demand for US-made goods. Tariffs and a lower real exchange rate would protect US producers."),
  ("The US introduced tariffs on a wide range of imports from China in 2018. Which type of policy was this? (Oct/Nov 2024 · 32 · Q25, reworded)", ["Expenditure-reducing", "Expenditure-switching", "Expansionary monetary", "Contractionary monetary"], 1, "Tariffs switch spending from imports to domestically produced goods."),
  ("A country imposes a tariff on steel imports. What is the likely effect on its economy? (May/June 2025 · 31 · Q25, reworded)", ["Its steel exports become more price competitive", "Productive inefficiency in its steel industry", "An improvement in its terms of trade", "A fall in producer surplus for its steel producers"], 1, "Protection reduces competition, so domestic producers may have less incentive to cut costs.")
]

exam = exam_page("globalisation: causes, consequences and effects on living standards",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Globalisation is among the most frequently set Paper 4 essay topics, with a 20 mark question in most recent series. Reworded past questions are below, with six Paper 3 multiple choice questions.",
  [("Essays, 20 marks", "5", "Feb/March 2023 (42) Q5; Feb/March 2024 (42) Q5; May/June 2024 (42) Q5; May/June 2025 (42) Q5; Oct/Nov 2023 (41) Q5"), ("Multiple choice (Paper 3)", "6 shown below", "2021 to 2025")],
  [
  eq("Based on Feb/March 2023 · 9708/42 · Q5", "20 marks", "Assess the impact of globalisation on the standard of living in low-income countries.",
     ["Globalisation promotes free trade, free movement of capital and labour and the transfer of technology; cultural and political ties are strengthened.",
      "Low-income countries have low productivity, high dependency ratios, low GDP per capita and depend on primary goods; living standards are linked to poverty, inequality, housing, education and health.",
      "An improvement in living standards is closely linked to improved economic performance (GDP per head, productivity); trade and technology transfer create more real wealth; tax revenue may fund health, housing and education.",
      "Evaluation: the links from globalisation to GDP and living standards are not clear; labour may be exploited; economic dependency and instability; effects may be unequal."],
     "Define globalisation. Benefits: trade, FDI, technology, tax revenue to fund services. Link GDP to living standards. Costs: exploitation, dependency, inequality, volatility. Judge.",
     [[("k", "Globalisation is the growing integration of economies through trade, investment, labour and technology flows. A low-income country typically has low productivity, a large primary sector and a high dependency ratio, so its living standards are low."), ("n", "Globalisation could raise living standards by giving access to world markets, bringing FDI and technology and creating jobs. Higher output and exports could raise real income per head, and more tax revenue may let the government spend more on health, education and housing.")],
      [("e", "However, the link to living standards is not automatic. Workers may be exploited in low-wage factories, the gains may go to a small group, and dependence on primary exports or on a few foreign firms leaves the economy exposed to price swings and shocks. Local industries may be destroyed by cheaper imports. Overall, globalisation could raise living standards in the long run if the country diversifies and shares the gains, but the effect may be uneven and uncertain.")]]),
  eq("Based on Feb/March 2024 · 9708/42 · Q5", "20 marks", "Globalisation will help to achieve economic growth in high-income economies and this will automatically improve living standards. Evaluate this statement.",
     ["Globalisation promotes free trade, free movement of capital and labour, and technology transfer.",
      "High-income countries have high productivity and GDP per head and rely on secondary and tertiary output; high living standards go with low poverty, advanced infrastructure, good housing, education and health, and low infant mortality.",
      "Growth is measured by changes in real GDP per head; an improvement in living standards is closely linked to economic performance.",
      "Evaluation: the link from growth to living standards is not automatic; globalisation brings job losses and inequality in some sectors, and non-monetary aspects of living standards matter."],
     "How globalisation raises growth in rich countries. Link to living standards. Why it is not automatic: inequality, unemployment, environment. Conclude.",
     [[("k", "In high-income economies globalisation could raise growth through specialisation, access to larger markets and cheaper imports, which lowers costs and prices. Real GDP per head may rise, and higher incomes and tax revenue could improve health, education and infrastructure."), ("n", "Consumers gain from lower prices and a wider choice, and exporters of high-value goods and services gain from larger markets.")],
      [("e", "However, growth does not automatically improve living standards for everyone. Workers in industries that face cheap imports may lose jobs, which raises structural unemployment and inequality. The environment may be damaged and the economy is more exposed to shocks from elsewhere. Living standards also depend on non-monetary factors such as leisure and the environment. So the statement is too strong; globalisation could help, but the effect depends on how the gains are shared.")]]),
  eq("Based on Oct/Nov 2023 · 9708/41 · Q5", "20 marks", "To what extent do you agree with the view that globalisation benefits high-income countries at the expense of low-income countries?",
     ["Globalisation raises trade, FDI and technology flows for both groups; high-income countries have advantages in capital, technology and bargaining power.",
      "Possible ways high-income countries gain: cheaper goods, markets for high-value exports, profits from MNCs, access to resources; possible losses for low-income countries: dependence on primary exports with falling terms of trade, low wages, profit repatriation, environmental damage.",
      "Evaluation: low-income countries also gain (exports, jobs, technology, growth as in East Asia), and high-income countries can lose (jobs, inequality), so it is not a simple transfer."],
     "Case for. Case against. Examples of gains for both. Judge: depends on country, policy and the type of trade.",
     [[("k", "Globalisation could benefit high-income countries because their firms have more capital, technology and brands, so they may capture a larger share of the gains. MNCs based there can send profits home, and rich countries can protect their own farmers while selling manufactured goods to poorer countries."), ("n", "Low-income countries often export primary products with volatile prices and a falling terms of trade, and may have weak bargaining power, so a larger share of the gains could go to the rich.")],
      [("e", "However, it is not simply at the expense of low-income countries. Several East Asian economies grew rapidly by exporting, attracting FDI and learning technology, and many people moved out of poverty. High-income countries also lose, for example when jobs in manufacturing move abroad. The extent depends on the country's policies, the type of trade and the terms of investment, so the statement is only partly true.")]])
  ],
  )

tips = tips_html(
  [("Define it with examples.", "Trade, capital, labour and technology flows, with global supply chains."),
   ("Give three causes.", "Cheaper transport and communication, trade liberalisation, multinationals and FDI."),
   ("Split high-income and low-income.", "Effects differ. Say which group is affected and why."),
   ("Link to living standards carefully.", "GDP per head is not the whole story: distribution, health, environment."),
   ("Use both sides.", "Benefits and costs for consumers, workers, firms and governments."),
   ("Mention the backlash.", "Protectionism and trade wars may threaten globalisation."),
   ("Judge with 'depends on'.", "Policies, institutions, flexibility and support for displaced workers.")],
  [("Definition", "Globalisation is the increasing integration of economies through trade, investment, labour and technology flows."),
   ("Causes", "Lower transport costs, trade liberalisation and multinational companies may all have encouraged globalisation."),
   ("Benefits", "Specialisation and larger markets could raise growth and lower prices."),
   ("Costs", "Globalisation might cause job losses in some industries and could widen inequality."),
   ("Judge", "The effect on living standards may depend on how the gains are shared.")],
  [CW["define"], CW["explain"], CW["assess"], CW["evaluate"]]) + FC

js = '''
/* ---------- Openness over time ---------- */
const TY = [[1960, 24], [1970, 26], [1980, 36], [1990, 39], [2000, 47], [2008, 61], [2015, 56], [2020, 52]], TX = (y) => 90 + (y - 1960) / 60 * 600, TV = (v) => 300 - v * 3.6;
function opDraw(s) {
  let o = axes(70, 300, 730, 30, "Year", "World trade as % of world GDP (approx.)"); [0, 20, 40, 60].forEach((v) => (o += SV.text(64, TV(v) + 4, v, "sm", { "text-anchor": "end" }) + SV.line(70, TV(v), 730, TV(v), "gr", op(0.3))));
  TY.forEach(([y]) => (o += SV.text(TX(y), 320, y, "sm", { "text-anchor": "middle" })));
  const n = Math.min(7, s.p * 7), pts = []; for (let i = 0; i <= Math.floor(n); i++) pts.push([TX(TY[i][0]), TV(TY[i][1])]); if (n % 1 > 0 && Math.floor(n) < 7) { const a = Math.floor(n), f = n - a; pts.push([TX(TY[a][0]) + (TX(TY[a + 1][0]) - TX(TY[a][0])) * f, TV(TY[a][1] + (TY[a + 1][1] - TY[a][1]) * f)]); }
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c1");
  const last = pts[pts.length - 1]; o += SV.circle(last[0], last[1], 6, "dot4");
  if (s.l > 0) o += tag(TX(1975), TV(26) + 30, "Containers, lower tariffs", "t1", s.l, "middle");
  if (s.l > 1) o += tag(TX(1993), TV(40) - 26, "China, ex-Soviet bloc open up", "t3", Math.min(1, s.l - 1), "middle");
  if (s.l > 2) o += tag(TX(2008), TV(61) - 14, "2008 peak", "t4", Math.min(1, s.l - 2), "middle");
  if (s.l > 3) o += tag(TX(2017), TV(54) + 38, "Crisis, tariffs, pandemic", "t2", Math.min(1, s.l - 3), "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="World trade as a share of world GDP rising from about 24 percent in 1960 to about 60 percent in 2008 and slipping since">${opDraw({ p: 1, l: 4 })}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 340, label: "World trade as a share of world GDP, rising and then levelling off (approximate values)", base: { p: 0, l: 0 }, draw: opDraw, tween: 1800, dwell: 5800, steps: [
  { cap: "<b>1960 to 1980.</b> Trade grows as tariffs fall and shipping gets cheaper with containers, so trade rises from about a quarter to over a third of world output.", s: { p: 0.3, l: 1 } },
  { cap: "<b>1980 to 2008.</b> China, India and the former Soviet bloc open up, global supply chains spread and capital flows grow. Trade climbs to about 60% of world GDP.", s: { p: 0.85, l: 2 } },
  { cap: "<b>2008.</b> The peak of this wave of globalisation, just before the global financial crisis.", s: { p: 0.88, l: 3 } },
  { cap: "<b>After 2008.</b> The financial crisis, trade tensions and tariffs, and the pandemic slow the rise, and the share levels off or dips. (Approximate figures, for illustration.)", s: { p: 1, l: 4 } },
] });

/* ---------- Winners and losers ---------- */
const WG = [["Consumers", 6], ["Exporters", 4], ["Skilled workers", 3], ["Displaced workers", -5], ["Low-skill workers", -7]], WL = [["Export sectors", 5], ["Factory workers", 3], ["Local firms", -3], ["Small farmers", -4]];
function wlDraw(s) {
  let o = SV.line(60, 160, 730, 160); const bars = (set, x0, title, k, w) => { if (k <= 0) return ""; let r = SV.text(x0 + set.length * w / 2, 36, title, "lbl bd", { "text-anchor": "middle", ...op(k) }); set.forEach(([l, v], i) => { const x = x0 + i * w + 6, y = 160 - v * 12 * k; r += SV.rect(x, Math.min(y, 160), w - 14, Math.abs(y - 160), v > 0 ? "f3" : "f2", op(0.8)) + tag(x + (w - 14) / 2, v > 0 ? y - 6 : y + 16, (v > 0 ? "+" : "") + v, v > 0 ? "t3" : "t2", k, "middle") + SV.text(x + (w - 14) / 2, 278, l.split(" ").slice(0, 1).join(" "), "sm", { "text-anchor": "middle", ...op(k) }) + SV.text(x + (w - 14) / 2, 292, l.split(" ").slice(1).join(" "), "sm", { "text-anchor": "middle", ...op(k) }); }); return r; };
  o += bars(WG, 70, "High-income country (illustrative net effects)", s.a, 80) + bars(WL, 500, "Low-income country", s.b, 58);
  if (s.c > 0) o += tag(380, 314, "On average a gain, but the gains and losses fall on different people", "t4", s.c, "middle");
  return o;
}
Lib.stepper($("#stW"), { w: 760, h: 324, label: "Illustrative winners and losers from globalisation in a high-income and a low-income country", base: { a: 0, b: 0, c: 0 }, draw: wlDraw, tween: 1100, dwell: 5800, steps: [
  { cap: "<b>High-income country.</b> Consumers (cheaper goods), exporters and skilled workers gain. Workers in industries facing cheap imports lose jobs or wages, especially low-skilled manufacturing workers.", s: { a: 1 } },
  { cap: "<b>Low-income country.</b> Export sectors and factory workers gain jobs and income, but local firms and subsistence farmers may suffer from imports, and conditions in some factories are poor.", s: { a: 1, b: 1 } },
  { cap: "<b>Overall.</b> The net effect may be positive, but gains and losses go to different groups, so policies to retrain workers and spread the gains matter. (Values are illustrative.)", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labG() {
  if (!$("#pf") || !$("#jl")) return;
  const pf = +$("#pf").value / 100, jl = +$("#jl").value, gain = 1000 * pf, lose = jl * 0.04, net = gain - lose;
  $("#r1").textContent = "$" + Lib.fmtN(gain, 0) + "m"; $("#r2").textContent = "$" + Lib.fmtN(lose, 0) + "m"; $("#r3").textContent = (net >= 0 ? "+$" : "−$") + Lib.fmtN(Math.abs(net), 0) + "m";
  $("#rv").textContent = `A ${Lib.fmtN(pf * 100, 0)}% fall in import prices saves consumers $${Lib.fmtN(gain, 0)}m a year. ${jl} lost jobs cost workers ${jl} × $40,000 = $${Lib.fmtN(lose, 0)}m a year. ${net >= 0 ? "The net effect is positive, so the winners could in theory compensate the losers, but the benefits are spread thinly across many consumers while the costs fall heavily on a few workers and towns, which is why retraining and support matter." : "Here the loss to displaced workers outweighs the gain to consumers."}`;
  const Y = (v) => 270 - v * 0.5; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "$m a year", "sm");
  [["Consumers gain", gain, "f3"], ["Workers lose", lose, "f2"], ["Net", Math.max(0, net), net >= 0 ? "f1" : "f2"]].forEach(([l, v, c], i) => { const x = 60 + i * 115, yy = Y(Math.min(v, 480)); o += SV.rect(x, yy, 80, 270 - yy, c) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, yy - 6, "$" + Lib.fmtN(v, 0) + "m", "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pf", label: "Fall in import prices, % ", min: 0, max: 30, step: 1, value: 10, fmt: (v) => v + "%", onInput: labG });
Lib.slider($("#g2"), { id: "jl", label: "Jobs lost in import-competing firms ", min: 0, max: 5000, step: 250, value: 1500, fmt: (v) => v.toLocaleString("en-US"), onInput: labG });
labG();

/* ---------- Lab 2 ---------- */
function labO() {
  if (!$("#xs") || !$("#ms") || !$("#fd")) return;
  const x = +$("#xs").value, m = +$("#ms").value, fd = +$("#fd").value, open_ = x + m, hit = x * fd / 100;
  $("#t1").textContent = open_ + "% of GDP"; $("#t2").textContent = "−" + Lib.fmtN(hit, 1) + "% of GDP"; $("#t3").textContent = open_ > 100 ? "Very high" : open_ > 60 ? "High" : "Moderate";
  $("#tv").textContent = `Exports are ${x}% of GDP and imports ${m}%, so openness is ${open_}% of GDP. If foreign demand falls ${fd}%, exports fall by ${fd}% of ${x}%, a direct hit of ${Lib.fmtN(hit, 1)}% of GDP (before multiplier effects). A more open economy gains from trade in good times but is more exposed to shocks abroad.`;
  const Y = (v) => 270 - v * 2; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "% of GDP", "sm");
  [["Exports", x, "f1"], ["Imports", m, "f2"], ["Direct hit", hit, "f3"]].forEach(([l, v, c], i) => { const px = 60 + i * 115, yy = Y(Math.min(v, 120)); o += SV.rect(px, yy, 80, 270 - yy, c) + SV.text(px + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(px + 40, yy - 6, Lib.fmtN(v, 1) + "%", "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "xs", label: "Exports, % of GDP ", min: 5, max: 90, step: 1, value: 30, fmt: (v) => v + "%", onInput: labO });
Lib.slider($("#g4"), { id: "ms", label: "Imports, % of GDP ", min: 5, max: 90, step: 1, value: 30, fmt: (v) => v + "%", onInput: labO });
Lib.slider($("#g5"), { id: "fd", label: "Fall in foreign demand, % ", min: 0, max: 30, step: 1, value: 10, fmt: (v) => v + "%", onInput: labO });
labO();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Is it mainly a cause, a benefit or a cost of globalisation?", ["Cause", "Benefit", "Cost"],
  [("Containerisation lowers shipping costs", 0), ("Consumers pay lower prices for imported goods", 1), ("Workers lose jobs when production moves to a low-wage country", 2), ("Governments cut tariffs under trade agreements", 0), ("Technology transfer from multinationals raises productivity", 1), ("A financial crisis spreads across countries", 2), ("The internet cuts the cost of global communication", 0), ("Transfer of polluting production to countries with weak rules", 2)],
  "Causes: cheaper transport and communication, liberalisation, MNCs. Benefits: prices, growth, technology. Costs: job losses, inequality, shocks, pollution.") + MATCH([
  ["Globalisation", "The growing integration of economies through trade, capital, labour and technology flows"],
  ["Global supply chain", "Production of a good spread across several countries"],
  ["Openness", "Trade (exports plus imports) as a share of GDP"],
  ["Trade liberalisation", "Reducing tariffs and other barriers to trade"],
  ["Protectionism", "Policies such as tariffs and quotas to limit imports"],
  ["Structural unemployment", "Unemployment from the decline of an industry"]]) + ORDER(
  "Put the chain from cheaper transport to a global supply chain in order.",
  ["Shipping and communication costs fall", "Firms can sell and source goods in more countries", "Production moves to the lowest-cost locations", "Parts are made in different countries", "A global supply chain develops"],
  "Lower transport costs make worldwide specialisation profitable.") + CALC([
  {"q": "Exports are $400bn, imports are $350bn and GDP is $1,000bn. Calculate openness, (X + M) ÷ GDP, as a percentage (%).", "a": 75, "unit": "%", "tol": 0.5, "hint": "(400 + 350) ÷ 1,000.", "sol": "<b>75%</b>."},
  {"q": "Exports are 40% of GDP. Foreign demand falls by 10%. Calculate the direct fall in GDP (% of GDP).", "a": 4, "unit": "%", "tol": 0.05, "hint": "0.4 × 10.", "sol": "<b>4%</b> of GDP, before multiplier effects."},
  {"q": "Consumers spend $800m on imports and prices fall by 5%. Calculate the saving to consumers ($m).", "a": 40, "unit": "$m", "tol": 0.5, "hint": "800 × 0.05.", "sol": "<b>$40m</b>."},
  {"q": "A country's imports of manufactured goods rise and 2,000 workers each lose $30,000 a year. Calculate the total loss ($m a year).", "a": 60, "unit": "$m", "tol": 0.5, "hint": "2,000 × 30,000.", "sol": "<b>$60m</b>."}]) + MCQ([
  ("Which is a cause of globalisation?", ["Falling transport and communication costs", "Higher tariffs", "Exchange controls", "Shorter supply chains"], 0, "Cheaper movement of goods and information integrates markets."),
  ("A possible cost of globalisation for high-income countries is:", ["Structural unemployment in industries facing cheap imports", "Higher prices for all goods", "Lower access to technology", "Smaller markets"], 0, "Workers in import-competing sectors can lose jobs."),
  ("Openness is measured by:", ["Exports plus imports as a share of GDP", "Exports minus imports", "The exchange rate", "The inflation rate"], 0, "It shows how much of the economy depends on trade."),
  ("Protectionism is a threat to globalisation because it:", ["Restricts trade flows", "Lowers transport costs", "Raises FDI", "Opens markets"], 0, "Tariffs and quotas reduce trade."),
  ("An advantage of globalisation for consumers is:", ["Lower prices and wider choice", "Fewer products", "Higher import tariffs", "Less competition"], 0, "Competition and specialisation lower prices.")
], "qz1") + CARDS([
  ("Globalisation", "Growing integration of economies."),
  ("Causes", "Cheaper transport, liberalisation, MNCs."),
  ("Global supply chain", "Production across many countries."),
  ("Openness", "(Exports + imports) ÷ GDP."),
  ("Benefits", "Lower prices, growth, technology."),
  ("Costs", "Job losses, inequality, pollution, shocks."),
  ("Protectionism", "Barriers to limit imports."),
  ("Evaluation", "Gains are real but not shared equally.")]) + MCQ(mc_exam)

build("sy1161", "globalisation", "Globalisation: Causes and Consequences", EY,
  "11.6.1: what globalisation means, why it has grown, and its effects on consumers, workers, firms and countries at different levels of development. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
