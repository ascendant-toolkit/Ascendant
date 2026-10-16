"""Syllabus 11.5.2-11.5.4 Trade and investment, multinational companies and FDI. Run: python3 tools/artifact-kit/mk_sy1152.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.5.2 to 11.5.4"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Trade and investment link economies at different levels of development: <b>trade</b> lets countries specialise, but rich-country barriers and falling primary prices can hold poor countries back, while <b>investment</b> flows as <b class="kw">portfolio investment</b> (shares and bonds) or <b class="kw">foreign direct investment (FDI)</b>, which is the purchase or building of real productive assets abroad. A <b class="kw">multinational company (MNC)</b> is a firm that owns or controls production in more than one country, and its FDI can bring <b>capital, jobs, technology, skills, exports and tax revenue</b> to the host country. The costs can include <b>profit repatriation, transfer pricing, environmental damage, pressure on local firms and dependence</b>, so the net effect depends on the host's policies and conditions.</p></div>

  <h2>1 · Trade and investment between rich and poor countries (11.5.2)</h2>
  <ul>
    <li><b>Gains from trade:</b> specialising by comparative advantage, access to larger markets, economies of scale, cheaper imports of capital goods and technology, and competition that raises efficiency. For many developing countries, <b>exports are a main source of foreign exchange</b>.</li>
    <li><b>Obstacles for developing countries:</b> tariffs and quotas, and especially <b>subsidies to farmers</b> in high-income countries that depress world prices; <b>tariff escalation</b> (low tariffs on raw materials but high tariffs on processed goods, which discourages processing); dependence on primary products with falling or volatile prices; weak transport and infrastructure; and a lack of finance and skills.</li>
    <li><b>Helps:</b> preferential access schemes (lower tariffs for poorer countries), regional trade agreements, fair trade schemes and trade-related technical assistance.</li>
    <li><b>Investment flows:</b> <b>portfolio investment</b> (buying shares and bonds) can be sold quickly and is volatile ("hot money"); <b>FDI</b> is long-term, builds productive capacity and is less volatile. Emerging economies attract more of both than low-income countries.</li>
  </ul>

  <h2>2 · Multinational companies (11.5.3)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Definition:</b> a firm that has operations (factories, offices, mines or shops) in <b>two or more countries</b>, usually controlled from a home country headquarters.</li>
    <li><b>Activities:</b> producing and selling in several countries; moving production to low-cost locations; research and development; raising finance worldwide; managing global supply chains; <b>transfer pricing</b> (setting prices for transactions between subsidiaries); lobbying governments.</li>
    <li><b>Why they locate abroad:</b> lower labour and land costs, access to raw materials, access to large markets, lower taxes and fewer regulations, avoiding trade barriers, and following customers.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th></th><th>Possible benefits</th><th>Possible costs</th></tr>
    <tr><td><b>Host country</b></td><td>Jobs and higher wages; investment and the multiplier; transfer of technology and management skills; training and human capital; exports and foreign exchange; tax revenue; competition and better infrastructure</td><td>Profits sent home (repatriation); transfer pricing to cut tax; may use local resources unsustainably; environmental damage and weak working standards; local firms may be driven out; dependence on the MNC; capital-intensive methods create few jobs; the MNC may leave</td></tr>
    <tr><td><b>Home country</b></td><td>Profits and dividends returned; cheaper imports; export of capital goods and services; cheaper inputs raise competitiveness</td><td>Jobs lost when production moves abroad; lower investment at home; tax revenue lost</td></tr>
  </table></div>

  <h2>3 · Foreign direct investment (11.5.4)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Definition:</b> an investment by a firm in one country in <b>real assets or a lasting controlling interest</b> (often 10% or more of the shares) in a business in another country. <b>Greenfield FDI</b> builds a new plant; <b>brownfield FDI</b> buys an existing firm.</li>
    <li><b>Consequences for a developing host country:</b>
      <b>Capital inflow</b> (financial account improves) and <b>higher investment</b>, a multiplier effect on income and jobs; <b>technology and skills</b> that raise productivity (shifting AS right); <b>export growth</b> and import substitution that may improve the current account; <b>higher tax revenue</b>.
      But <b>profit repatriation</b> and imports of machinery and materials worsen the current account (primary income and goods), the investment may be in <b>enclave</b> industries with few links to the local economy, <b>local firms can be crowded out</b>, and <b>environmental and social costs</b> may rise.</li>
    <li><b>What attracts FDI:</b> infrastructure, a skilled and low-cost workforce, political and economic stability, market size, access to resources, tax incentives, open trade and secure property rights.</li>
    <li><b>Balance of payments effect over time:</b> in the short run the capital inflow improves the financial account and imports of capital goods worsen the current account; later, exports may rise, but repatriated profits flow out.</li>
  </ul>
  <div class="tip"><b class="h">Evaluation point</b>Whether MNCs and FDI help growth and development depends on the sector (resource extraction versus manufacturing), how much is bought locally, the terms the host negotiates (tax, local content, training, environmental rules) and whether the host has the skills and institutions to absorb the technology. FDI is often one of several routes to growth, along with domestic investment, aid and export promotion.</div>
'''

watch = '''
  <h2>1 · An MNC and its two countries</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stM"></div>
  <h2>2 · FDI and the balance of payments over time</h2>
  <div id="stF"></div>
'''

explore = '''
  <h2>Lab 1 · The multiplier effect of FDI</h2>
  <p>FDI of $120m is a boost to investment. The rise in GDP depends on the multiplier. Some of the extra income is profit that is sent home, so the rise in national income (GNI) is smaller.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g3b"></div>
    <div class="readout"><div><small>Multiplier</small><strong id="r1"></strong></div><div><small>Rise in GDP</small><strong id="r2"></strong></div><div><small>Rise in GNI</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of the FDI injection, the rise in GDP and the rise in GNI after profit repatriation"></svg></div></div></div>

  <h2>Lab 2 · Transfer pricing and the host's tax revenue</h2>
  <p>An MNC's subsidiary in a host country earns $100m profit. The host taxes at 30%. Shifting profit to a haven subsidiary taxed at 10% by over-charging for inputs reduces the host's tax. Choose how much is shifted.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div>
    <div class="readout"><div><small>Tax paid, host</small><strong id="t1"></strong></div><div><small>Tax paid, haven</small><strong id="t2"></strong></div><div><small>Host's loss</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars of tax paid in the host country and the haven for the chosen amount of shifted profit"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Benefit or cost to the host country?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of new FDI on income in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Car factories in emerging economies", "Vehicle makers have built plants in countries such as Mexico, Thailand and Turkey. They bring jobs, supplier industries, training and exports, but also profits sent abroad, imports of parts and a risk of closure if costs change.", "FDI in manufacturing, the multiplier, exports and the risk of dependence.") +
rw("Mining and extraction", "Foreign mining and oil firms often invest in resource-rich low-income countries. They can bring export earnings and tax revenue, but with few local linkages, profits sent overseas, pollution and little lasting benefit if the resources run out or the contracts are generous.", "enclave investment and sustainability issues in resource-based FDI.") +
rw("Palm oil plantations", "A multinational food company expanded palm oil plantations in Malaysia and Indonesia, which raised rural incomes and exports. It also led to large-scale clearance of rainforest and loss of habitats, showing how private benefits and external costs can differ.", "the link between MNC investment, growth and sustainability, as in a recent Paper 4 data set.") +
rw("Transfer pricing and tax", "Some multinationals set the prices of goods and services passed between subsidiaries so that profits show up in low-tax countries. Governments in host countries lose revenue and have tried to counter this with rules on arm's-length pricing.", "a cost of MNCs to the host country's government revenue.")
)

mc_exam = [
  ("A government wants to attract foreign direct investment to develop its economy. What is most likely to encourage this? (Feb/March 2022 · 32 · Q20, reworded)", ["Improved health and safety standards for workers", "Increased import quotas", "Increased spending on infrastructure", "Introducing a minimum wage"], 2, "Roads, power and ports lower firms' costs, so FDI is attracted. A minimum wage raises costs and quotas restrict trade."),
  ("In what circumstances will low wages and low-cost land not attract foreign investment in manufacturing in a low-income country? (Oct/Nov 2023 · 33 · Q30, reworded)", ["If the country creates an independent central bank", "If the country privatises state firms", "If the country lacks well-developed infrastructure", "If the country allows repatriation of profits"], 2, "Without reliable transport and power, low wages are not enough to make production profitable."),
  ("What is the most likely consequence of an increase in the number of multinational companies? (May/June 2024 · 31 · Q27, reworded)", ["Fewer advances in technology", "Less foreign direct investment", "More exports", "More unemployment"], 2, "MNCs trade globally and set up export production, so international trade tends to rise."),
  ("An MNC buys a manufacturing firm in a developing country that sells to local consumers. The MNC then exports machinery and raw materials to it. What is the most likely effect on the developing country's balance of payments? (May/June 2024 · 32 · Q28, reworded)", ["Current account improves; financial account improves", "Current account improves; financial account worsens", "Current account worsens; financial account improves", "Current account worsens; financial account worsens"], 2, "The imported machinery and materials worsen the current account, and the purchase is a capital inflow, which improves the financial account."),
  ("FDI brings better training and higher productivity, but profits are sent back to the investor's home country. What is the effect on aggregate demand and aggregate supply in the host country? (Oct/Nov 2020 · 33 · Q21, reworded)", ["AD shifts left; AS shifts left", "AD shifts right; AS shifts left", "AD shifts left; AS shifts right", "AD shifts right; AS shifts right"], 2, "Better skills shift AS right. The profit outflow reduces spending in the host country's circular flow, so AD shifts left."),
  ("Country X has low inflation, a stable currency and unemployed resources. It attracts $25bn of FDI. What is most likely to be a positive benefit? (Oct/Nov 2022 · 32 · Q28, reworded)", ["Aggregate demand rises through the investment multiplier", "It must use its reserves to eliminate any trade deficit", "The balance of payments is affected by the outflow of profits", "Inflation rises if capacity is raised"], 0, "With spare resources, the extra investment raises output and employment by a multiple of the original amount. The other three are costs."),
  ("What is most likely to result from foreign direct investment in a developing economy? (Oct/Nov 2024 · 33 · Q28, reworded)", ["An improved trade balance", "A rise in net investment income", "A fall in government tax revenue", "A fall in wage levels"], 0, "FDI that builds export capacity or replaces imports can improve the trade balance. Profit outflows reduce net investment income, and tax revenue and wages are more likely to rise."),
  ("Company X makes batteries for electric cars and invests in a new factory in country N. Under which conditions is this most likely to improve N's current account? Share of raw materials supplied by N, and income elasticity of demand for electric cars outside N. (Oct/Nov 2024 · 32 · Q28, reworded)", ["10%, 0.5", "10%, 1.5", "90%, 0.5", "90%, 1.5"], 3, "Buying most materials locally reduces imports, and high income elasticity abroad means export sales rise strongly as incomes grow."),
  ("A multinational firm wants to minimise costs and maximise profits. What would least assist it? (Oct/Nov 2021 · 31 · Q9, reworded)", ["Near-monopoly status to control output and prices", "Locating its home base in a low corporation tax country", "Operating in a cartel with production quotas", "Owning subsidiaries in several countries to gain economies of scale"], 2, "A cartel needs agreement between rival firms, and tends to break down; it does not follow from being multinational. The other three help directly.")
]

exam = exam_page("trade, investment, multinational companies and FDI",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Multinational companies and FDI are among the most common 20 and 25 mark questions, and FDI also appears as a 13 mark part. Reworded past questions are below, with nine Paper 3 multiple choice questions.",
  [("Essay parts, 13 marks", "1", "May/June 2020 (41) Q7(b)"), ("Essays, 20 and 25 marks", "4", "Oct/Nov 2020 (42) Q6; Oct/Nov 2022 (42) Q7; Oct/Nov 2023 (42) Q4; Oct/Nov 2021 (41) Q6"), ("Multiple choice (Paper 3)", "9 shown below", "2020 to 2025")],
  [
  eq("Based on May/June 2020 · 9708/41 · Q7(b)", "13 marks", "Assess the view that foreign direct investment remains the key to economic growth in developing countries.",
     ["Explain FDI, referring to the role of private multinational corporations and how they improve labour skills, build factories and promote research and development.",
      "Define economic growth clearly as the increase in real GDP over a period, and consider alternative strategies such as export-led growth, direct government investment and structural change.",
      "Compare the importance of FDI with those alternatives and reach a conclusion."],
     "What FDI does. How it raises growth. Alternatives. Compare. Judge.",
     [[("k", "FDI is investment by a foreign firm, usually a multinational, in factories and other real assets in a developing country. It adds to capital, and may bring technology, training and management skills, so productivity could rise and aggregate supply could increase."), ("n", "The extra investment also raises demand through the multiplier, creating jobs, and may raise exports and tax revenue.")],
      [("e", "However, FDI is not the only route. Export-led growth, government investment in infrastructure and education, and structural change from farming to industry can also raise growth. FDI may have limited benefits if profits are repatriated or if few local suppliers are used. So FDI is probably an important route but not the only key, and works best alongside domestic investment and good institutions.")]]),
  eq("Based on Oct/Nov 2020 · 9708/42 · Q6", "25 marks", "'Investment by multinational corporations (MNCs) in a developing country always promotes sustainable economic growth in that country.' Discuss.",
     ["Investment and the multiplier effect on the demand for labour and production of goods and services; new techniques and technology and effects on output and the demand for labour.",
      "Sustainability, especially resource-based MNCs; effects on growth, the current and capital accounts of the balance of payments, inflation, the rural-urban balance and exchange rates; a production possibility frontier may be used.",
      "Level 4 (18 to 25) develops the advantages and disadvantages of MNC investment for sustainable growth and draws a conclusion (maximum 21 without one)."],
     "Benefits: investment, multiplier, technology, skills, exports. Costs: profits sent home, resource depletion, pollution, local firms, urban-rural imbalance. Sustainability. Conclude: not always.",
     [[("k", "An MNC investing in a developing country may raise growth. The investment adds to capital and demand, and through the multiplier could raise output, income and employment. New technology and training could raise productivity and potential output, and exports may improve the balance of payments."), ("n", "Tax revenue from the firm could fund infrastructure, health and education, which may support growth over a longer period.")],
      [("e", "However, growth may not be sustainable. Resource-based investment such as mining or palm oil may use up non-renewable resources, damage the environment and leave little once the resources are gone. Profits may be repatriated and transfer pricing may reduce tax revenue, and the firm may drive out local producers or create jobs mainly in cities, widening regional inequality. The result depends on the sector, the host government's rules and how much is bought locally, so the statement is too strong: investment by MNCs does not always promote sustainable growth.")]]),
  eq("Based on Oct/Nov 2022 · 9708/42 · Q7", "25 marks", "Discuss the ability of multinational corporations to increase living standards in their home country and the other countries in which they operate.",
     ["Define an MNC and the standard of living.",
      "Analyse the effect of an MNC on its host and its home country and the effects on living standards through employment, investment, exports and imports, remittances, transfer of externalities, urbanisation, tax revenue and spending.",
      "Level 4 (18 to 25) discusses effects on both home and host countries; with a conclusion for 22 to 25 marks."],
     "Define both terms. Host country: jobs, income, technology, tax; costs. Home country: profits and cheaper goods; lost jobs. Compare. Conclude.",
     [[("k", "A multinational corporation is a firm with operations in more than one country, and the standard of living is the material and non-material well-being of people."), ("n", "In host countries an MNC may create jobs, raise incomes and bring technology and skills, so real incomes and access to goods may rise. It may also pay taxes that finance public services. In the home country the profits sent back raise incomes of shareholders, and cheaper imported goods raise real incomes.")],
      [("e", "However, host countries may suffer from profit repatriation, pollution, poor working conditions or damage to local firms, and an MNC may use transfer pricing to avoid tax. In the home country, jobs may be lost when production moves abroad. The net effect on living standards depends on the sector, the terms the host negotiates and the strength of regulation, so MNCs may raise living standards, but not for everyone and not automatically.")]]),
  eq("Based on Oct/Nov 2023 · 9708/42 · Q4", "20 marks", "The presence of multinational corporations in a low-income country always promotes economic growth in that country. Evaluate this statement.",
     ["Transfer of skills and knowledge, both managerial and workshop; a larger tax base so the government can invest; short-term (actual) and long-term (potential) growth.",
      "The impact of FDI on aggregate supply or the PPF, using the multiplier, circular flow or AD/AS; better education and health and long-term growth.",
      "Evaluation: MNCs may export 'dirty' industries and evade legal limits at home; they may destroy indigenous industry, with a negative effect on employment that exceeds the jobs created."],
     "Benefits with a diagram (AS shift). Costs. When it works and when it does not.",
     [[("k", "An MNC may raise actual growth by adding investment, which increases aggregate demand through the multiplier, and raise potential growth by transferring technology and skills that shift the PPC outwards or aggregate supply to the right. A bigger tax base may allow the government to spend more on education and health."), ("n", "Over time, trained workers and local suppliers could raise the productivity of the whole economy.")],
      [("e", "On the other hand, an MNC may avoid strict environmental or employment laws in its home country by moving polluting production abroad, transferring negative externalities to the host. Large-scale production may also destroy local industries, so the loss of jobs could outweigh those created. Profits may be repatriated too. Therefore the statement is too strong: MNCs may promote growth, but the effect depends on the host country's policies and the type of investment.")]])
  ],
  )

tips = tips_html(
  [("Define MNC and FDI separately.", "MNC: operates in more than one country. FDI: investment in real assets abroad."),
   ("Draw the AS shift.", "Technology and training shift AS to the right (or the PPC outwards)."),
   ("Use the multiplier.", "FDI is an injection that raises income by more than the original amount."),
   ("List costs too.", "Profit repatriation, transfer pricing, pollution, crowding out local firms."),
   ("Split host and home.", "Effects differ for the country receiving the investment and the country the MNC comes from."),
   ("Link to the balance of payments.", "Financial account up, imports of machinery down on the current account, later exports and profit outflows."),
   ("Conclude with 'depends on'.", "The sector, local linkages, host policies and governance.")],
  [("MNC", "A multinational company operates in more than one country, often controlling production from a home headquarters."),
   ("FDI", "Foreign direct investment is investment in real assets abroad, which may bring capital, technology and skills."),
   ("Multiplier", "FDI is an injection that could raise national income by a multiple of the original amount."),
   ("Costs", "Profits may be repatriated and transfer pricing could reduce the host's tax revenue."),
   ("Judge", "The benefits may depend on the sector, the host's policies and how much of the output is linked to local firms.")],
  [CW["define"], CW["explain"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- MNC network ---------- */
function mncDraw(s) {
  const box = (x, y, w, h, t, c, k) => (k > 0 ? SV.rect(x, y, w, h, c, op(0.5 * k)) + SV.text(x + w / 2, y + h / 2 + 5, t, "lbl bd", { "text-anchor": "middle", ...op(k) }) : "");
  const ar = (x1, y1, x2, y2, d, t, k, ty, tx) => (k > 0 ? SV.line(x1, y1, x2, y2, "c1", { "stroke-width": 2.5, ...op(k) }) + SV.arrowHead(x2, y2, d, "dot1") + tag(tx, ty, t, "t1", k, "middle") : "");
  let o = box(40, 120, 190, 70, "Home HQ (parent company)", "f1", 1) + box(530, 120, 190, 70, "Host subsidiary (factory)", "f3", 1);
  o += ar(230, 140, 530, 140, "r", "FDI: capital, technology, managers", s.a, 130, 380);
  if (s.b > 0) o += box(540, 40, 170, 40, "Jobs, training, wages", "f3", s.b) + ar(625, 120, 625, 82, "u", "", s.b, 100, 625);
  if (s.b > 0) o += box(540, 230, 170, 40, "Exports and tax revenue", "f3", s.b) + ar(625, 190, 625, 228, "d", "", s.b, 210, 625);
  if (s.c > 0) o += ar(530, 175, 230, 175, "l", "Profits repatriated; transfer pricing", s.c, 200, 380);
  if (s.d > 0) o += box(260, 230, 210, 44, "Environmental and local-firm costs", "f2", s.d) + ar(530, 190, 470, 245, "l", "", s.d, 210, 500);
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A multinational's home headquarters sending FDI to a host country subsidiary, which returns profits">${mncDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 300, label: "An MNC investing abroad: FDI flows out, benefits and costs flow in the host, and profits flow home", base: { a: 0, b: 0, c: 0, d: 0 }, draw: mncDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>FDI.</b> The parent company in its home country builds or buys a subsidiary in the host country, sending capital, technology and managers.", s: { a: 1 } },
  { cap: "<b>Benefits for the host.</b> The subsidiary creates jobs, trains workers, pays wages and taxes and may export.", s: { a: 1, b: 1 } },
  { cap: "<b>Profits flow home.</b> The parent receives profits and dividends (repatriation), and may use transfer pricing to book profits in low-tax locations. This reduces the net gain for the host.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Other costs.</b> The host may suffer environmental damage and pressure on local firms. The balance depends on the sector and the rules the host sets.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- FDI and the balance of payments over time ---------- */
const BP = [["Year 1", 60, -20], ["Year 3", 25, -8], ["Year 6", 5, 4], ["Year 10", 0, 10]], BY = (v) => 170 - v * 1.7;
function bpDraw(s) {
  let o = axes(70, 170, 730, 20, "", "$m") + SV.line(70, BY(0), 730, BY(0), "ax"); [-20, 0, 20, 40, 60].forEach((v) => (o += SV.text(64, BY(v) + 4, v, "sm", { "text-anchor": "end" })));
  BP.forEach(([l, fa, ca], i) => { const k = Math.max(0, Math.min(1, s.n - i)); if (k <= 0) return; const x = 120 + i * 150; o += SV.rect(x, BY(fa * k), 50, Math.abs(fa * k) * 1.7, "f3", op(0.8)) + SV.rect(x + 56, ca >= 0 ? BY(ca * k) : BY(0), 50, Math.abs(ca * k) * 1.7, ca >= 0 ? "f1" : "f2", op(0.8)) + tag(x + 78, 296, l, "sm", k, "middle") + tag(x + 25, BY(fa * k) - 6, "+" + fa, "t3", k, "middle") + tag(x + 81, ca >= 0 ? BY(ca * k) - 6 : BY(0) + Math.abs(ca * k) * 1.7 + 14, (ca >= 0 ? "+" : "") + ca, ca >= 0 ? "t1" : "t2", k, "middle"); });
  o += SV.rect(520, 312, 10, 10, "f3", op(0.8)) + SV.text(536, 321, "Financial account (FDI inflow)", "sm") + SV.rect(520, 330, 10, 10, "f1", op(0.8)) + SV.text(536, 339, "Current account", "sm");
  return o;
}
Lib.stepper($("#stF"), { w: 760, h: 345, label: "FDI and the balance of payments over time: a financial account inflow, a current account deficit that later improves", base: { n: 0 }, draw: bpDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>Year 1.</b> The FDI inflow ($60m) improves the financial account. The new factory imports machinery and materials, so the current account worsens ($20m).", s: { n: 1 } },
  { cap: "<b>Year 3.</b> Less new investment arrives and the factory begins to export, so the current account deficit narrows.", s: { n: 2 } },
  { cap: "<b>Year 6.</b> Exports from the factory now exceed its imports, but profit payments abroad appear in the current account, so the surplus is small.", s: { n: 3 } },
  { cap: "<b>Year 10.</b> Exports are established: a current account surplus. The capital inflow has stopped, and profit repatriation is a continuing outflow.", s: { n: 4 } },
] });

/* ---------- Lab 1 ---------- */
function labF() {
  if (!$("#mc") || !$("#tx") || !$("#mm") || !$("#rp")) return;
  const c = +$("#mc").value / 100, t = +$("#tx").value / 100, m = +$("#mm").value / 100, rp = +$("#rp").value / 100, k = 1 / (1 - c * (1 - t) + m), gdp = 120 * k, gni = gdp * (1 - rp);
  $("#r1").textContent = Lib.fmtN(k, 2); $("#r2").textContent = "$" + Lib.fmtN(gdp, 0) + "m"; $("#r3").textContent = "$" + Lib.fmtN(gni, 0) + "m";
  $("#rv").textContent = `Multiplier = 1 ÷ (1 − ${c.toFixed(2)} × (1 − ${t.toFixed(2)}) + ${m.toFixed(2)}) = ${Lib.fmtN(k, 2)}. FDI of $120m raises GDP by $${Lib.fmtN(gdp, 0)}m. If ${Lib.fmtN(rp * 100, 0)}% of the extra income is profit sent abroad, national income (GNI) rises by only $${Lib.fmtN(gni, 0)}m.`;
  const Y = (v) => 270 - v * 0.9; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "$m", "sm");
  [["FDI", 120, "f1"], ["Rise in GDP", gdp, "f3"], ["Rise in GNI", gni, "f2"]].forEach(([l, v, cl], i) => { const x = 60 + i * 115, yy = Y(Math.min(v, 280)); o += SV.rect(x, yy, 80, 270 - yy, cl) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, yy - 6, "$" + Lib.fmtN(v, 0) + "m", "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "mc", label: "Marginal propensity to consume, % ", min: 50, max: 90, step: 5, value: 80, fmt: (v) => v + "%", onInput: labF });
Lib.slider($("#g2"), { id: "tx", label: "Tax rate, % ", min: 0, max: 40, step: 5, value: 25, fmt: (v) => v + "%", onInput: labF });
Lib.slider($("#g3"), { id: "mm", label: "Marginal propensity to import, % ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v + "%", onInput: labF });
Lib.slider($("#g3b"), { id: "rp", label: "Share of extra income sent abroad as profit, % ", min: 0, max: 60, step: 5, value: 30, fmt: (v) => v + "%", onInput: labF });
labF();

/* ---------- Lab 2 ---------- */
function labX() {
  if (!$("#sf")) return;
  const s = +$("#sf").value, th = 0.3 * (100 - s), tv = 0.1 * s, loss = 30 - th;
  $("#t1").textContent = "$" + Lib.fmtN(th, 1) + "m"; $("#t2").textContent = "$" + Lib.fmtN(tv, 1) + "m"; $("#t3").textContent = "$" + Lib.fmtN(loss, 1) + "m";
  $("#tv").textContent = s === 0 ? "No profit is shifted: $100m is taxed in the host at 30%, giving $30m of revenue." : `Shifting $${s}m of profit to the haven means $${100 - s}m is taxed in the host at 30% ($${Lib.fmtN(th, 1)}m) and $${s}m at 10% in the haven ($${Lib.fmtN(tv, 1)}m). The group's total tax falls from $30m to $${Lib.fmtN(th + tv, 1)}m and the host loses $${Lib.fmtN(loss, 1)}m of tax revenue that it could have spent on public services.`;
  const Y = (v) => 270 - v * 8; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "Tax paid ($m)", "sm");
  [["Host", th, "f2"], ["Haven", tv, "f1"], ["Host's loss", loss, "f3"]].forEach(([l, v, c], i) => { const x = 60 + i * 115; o += SV.rect(x, Y(v), 80, 270 - Y(v), c) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, Y(v) - 6, Lib.fmtN(v, 1), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "sf", label: "Profit shifted to the haven, $m ", min: 0, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labX });
labX();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Is it mainly a benefit or a cost for the host country?", ["Benefit", "Cost"],
  [("Training for local workers", 0), ("Profits sent back to the home country", 1), ("New jobs in a factory", 0), ("Pollution from a mine", 1), ("Transfer of new technology", 0), ("Local firms driven out by a large competitor", 1), ("Extra tax revenue for the government", 0), ("Transfer pricing used to cut tax", 1)],
  "Benefits: jobs, skills, technology, tax. Costs: repatriation, pollution, competition and transfer pricing.") + MATCH([
  ["Multinational company", "A firm that operates in two or more countries"],
  ["Foreign direct investment", "Investment in real assets or control of a firm in another country"],
  ["Portfolio investment", "Buying shares or bonds without control; easily sold"],
  ["Profit repatriation", "Sending profits back to the home country"],
  ["Transfer pricing", "Setting prices between subsidiaries to shift profits to low-tax places"],
  ["Greenfield FDI", "Building a new plant abroad"]]) + ORDER(
  "Put the effect of new FDI on income in order.",
  ["A multinational builds a factory in a host country", "Investment spending and demand for local labour rise", "Workers and suppliers earn income and spend part of it", "Income rises by a multiple of the original investment", "Part of the profit is sent abroad, limiting the rise in national income"],
  "The multiplier works through rounds of spending, with leakages.") + CALC([
  {"q": "The MPC is 0.8, the tax rate is 25% and the marginal propensity to import is 0.2. Calculate the multiplier (2 decimal places).", "a": 1.67, "unit": "", "tol": 0.02, "hint": "1 ÷ (1 − 0.8 × 0.75 + 0.2).", "sol": "1 ÷ (1 − 0.6 + 0.2) = 1 ÷ 0.6 = <b>1.67</b>."},
  {"q": "FDI of $120m is made with a multiplier of 1.67. Calculate the rise in GDP ($m).", "a": 200, "unit": "$m", "tol": 1, "hint": "120 × 1.67.", "sol": "<b>$200m</b>."},
  {"q": "30% of the extra $200m of income is sent abroad as profit. Calculate the rise in GNI ($m).", "a": 140, "unit": "$m", "tol": 1, "hint": "200 × 0.7.", "sol": "<b>$140m</b>."},
  {"q": "A subsidiary earns $100m. The host taxes at 30% and the haven at 10%. If $40m of profit is shifted to the haven, by how much does the host's tax revenue fall ($m)?", "a": 12, "unit": "$m", "tol": 0.5, "hint": "30% of 40.", "sol": "Host tax falls by 0.3 × 40 = <b>$12m</b> (the group pays $4m in the haven, saving $8m overall)."}]) + MCQ([
  ("A multinational company is a firm that:", ["Operates in more than one country", "Sells only to its home market", "Is owned by the government", "Has no overseas staff"], 0, "It has production or operations in two or more countries."),
  ("FDI differs from portfolio investment because FDI:", ["Is investment in real assets or a controlling stake", "Can be sold instantly", "Involves only government bonds", "Is always short term"], 0, "Portfolio investment is in shares and bonds without control."),
  ("Transfer pricing is a problem for host countries because it:", ["Reduces tax revenue", "Raises wages", "Raises exports", "Increases competition"], 0, "Profits are shown in low-tax countries."),
  ("A benefit of FDI to a host country is:", ["Transfer of technology and skills", "Outflow of profits", "Loss of local firms", "A larger national debt"], 0, "Technology and skills may raise productivity."),
  ("Which is most likely to attract FDI?", ["Good infrastructure and political stability", "High tariffs", "Poor roads", "Unpredictable laws"], 0, "Reliable conditions lower risk and costs.")
], "qz1") + CARDS([
  ("MNC", "A firm operating in more than one country."),
  ("FDI", "Investment in real assets abroad."),
  ("Portfolio investment", "Shares and bonds; volatile."),
  ("Profit repatriation", "Profits sent to the home country."),
  ("Transfer pricing", "Shifting profit through internal prices."),
  ("Greenfield / brownfield", "New plant / buying an existing firm."),
  ("Benefits for host", "Jobs, technology, tax, exports."),
  ("Costs for host", "Repatriation, pollution, local firms hurt.")]) + MCQ(mc_exam)

build("sy1152", "trade-investment-mncs-fdi", "Trade, Investment, MNCs and FDI", EY,
  "11.5.2 to 11.5.4: trade and investment between rich and poor countries, what multinational companies do, foreign direct investment and its benefits and costs for host and home countries. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
