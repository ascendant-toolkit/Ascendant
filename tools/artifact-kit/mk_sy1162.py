"""Syllabus 11.6.2-11.6.3 Trading blocs, trade creation and trade diversion. Run: python3 tools/artifact-kit/mk_sy1162.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.6.2 to 11.6.3"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Countries link their economies in stages. In a <b class="kw">free trade area</b> members remove tariffs and quotas on trade between themselves but each sets its own tariffs on outsiders; a <b class="kw">customs union</b> adds a <b>common external tariff</b>; a <b class="kw">monetary union</b> adds a <b>single currency and central bank</b>; and a <b class="kw">full economic union</b> adds <b>common economic policies, free movement of labour and capital and a unified market</b>. Joining a customs union causes <b class="kw">trade creation</b> (higher-cost domestic output is replaced by cheaper imports from partners, a gain) and <b class="kw">trade diversion</b> (cheaper imports from the rest of the world are replaced by dearer imports from partners, a loss), so the net effect may be a gain or a loss.</p></div>

  <h2>1 · The stages of economic integration</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Stage</th><th>What members do</th><th>Examples</th><th>Main benefits</th><th>Main costs</th></tr>
    <tr><td><b>Free trade area</b></td><td>Abolish tariffs and quotas on trade among members. Each sets its own tariffs on non-members</td><td>USMCA (US, Mexico, Canada); ASEAN free trade area</td><td>Cheaper imports from partners, larger markets, specialisation, more competition</td><td>Trade deflection (outside goods enter through the lowest-tariff member); rules of origin needed; job losses in uncompetitive sectors</td></tr>
    <tr><td><b>Customs union</b></td><td>FTA plus a <b>common external tariff</b> on non-members</td><td>The EU customs union; Mercosur</td><td>Everything in an FTA, no need for rules of origin, bargaining power in trade talks, shared protection</td><td>Trade diversion; loss of the freedom to set own tariffs and make own trade deals</td></tr>
    <tr><td><b>Monetary union</b></td><td>Customs union (often a common market) plus a <b>single currency</b> and a common central bank</td><td>The euro area</td><td>No exchange rate risk or conversion costs, price transparency, more trade and investment</td><td>No independent monetary or exchange rate policy; one interest rate for all members; weaker members cannot devalue and may have to cut wages and spending</td></tr>
    <tr><td><b>Full economic union</b></td><td>Monetary union plus <b>common fiscal and other economic policies</b>, free movement of labour and capital, common regulations and a single market</td><td>An aim of the EU; no complete example</td><td>Most efficient single market; policy coordination, transfers between regions</td><td>Largest loss of national sovereignty; needs political agreement; adjustments for member countries can be painful</td></tr>
  </table></div>

  <h2>2 · Trade creation and trade diversion</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Starting point:</b> a country imposes a tariff on all imports. The domestic price is the world price plus the tariff. It buys some goods from the cheapest world supplier and pays the tariff.</li>
    <li><b>After joining a customs union</b> the country removes tariffs on a partner's goods. The partner is cheaper than the tariff-inclusive price but may be <b>dearer than the cheapest world supplier</b>. The domestic price falls to the partner's price.</li>
    <li><b>Trade creation</b> (gain): the lower price means (1) <b>domestic producers who are less efficient than the partner are replaced</b> by imports (a production effect: resources are used more efficiently), and (2) <b>consumers buy more</b> at the lower price (a consumption effect: more consumer surplus). Both are the two triangles on the diagram.</li>
    <li><b>Trade diversion</b> (loss): goods that used to be imported from the cheapest world producer are now bought from the partner at a <b>higher price (partner price minus world price)</b>. This rectangle is a loss, because resources are used less efficiently and the government also loses the tariff revenue. A common external tariff makes this likely.</li>
    <li><b>Net welfare effect = trade creation − trade diversion.</b> It is more likely to be positive if the partners are efficient, the external tariff is low, the partners have similar prices to the world price, and demand and supply are elastic.</li>
  </ul>

  <h2>3 · Evaluating membership</h2>
  <ul>
    <li><b>Gains:</b> lower prices and greater variety, economies of scale from a larger market, more competition and efficiency, more investment, stronger bargaining power in world trade talks, and dynamic gains.</li>
    <li><b>Costs:</b> trade diversion, structural unemployment where industries cannot compete, loss of sovereignty and policy independence (for a customs or monetary union), and adjustment costs. Weaker members may lose from monetary union because they cannot devalue.</li>
    <li><b>The effect depends on</b> the elasticities of demand and supply, the size of the efficiency gap between partners and non-members, the initial tariff, and macroeconomic conditions.</li>
    <li><b>Compared with global free trade,</b> blocs are a second-best: they can liberalise trade among members while raising barriers to outsiders.</li>
  </ul>
  <div class="tip"><b class="h">Evaluation point</b>An FTA does not give "all the benefits and none of the costs" of a customs union: it avoids the common external tariff (and some trade diversion) and keeps freedom to make other trade deals, but it must police rules of origin, and it lacks the shared bargaining power and simpler customs of a union.</div>
'''

watch = '''
  <h2>1 · The ladder of integration</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stL"></div>
  <h2>2 · Trade creation and trade diversion</h2>
  <div id="stT"></div>
'''

explore = '''
  <h2>Lab · Is the customs union a net gain?</h2>
  <p>A country imports a good at the world price of $3 and has a tariff. Set the tariff and the partner's price. If the partner's price is below the tariff-inclusive price, the country buys from the partner. Compare trade creation with trade diversion.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Trade creation (gain)</small><strong id="r1"></strong></div><div><small>Trade diversion (loss)</small><strong id="r2"></strong></div><div><small>Net effect</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 330" role="img" aria-label="Domestic supply and demand with the world price, the tariff-inclusive price and the partner price, showing trade creation triangles and the trade diversion rectangle"></svg></div></div></div>

  <h2>Lab 2 · Why a monetary union can hurt weaker members</h2>
  <p>Two members of a monetary union face the same interest rate. A weaker member has costs that rise 3% a year faster than a stronger member's. With no exchange rate to adjust, see how its competitiveness changes over the years.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div>
    <div class="readout"><div><small>Cost gap after the period</small><strong id="t1"></strong></div><div><small>Competitiveness</small><strong id="t2"></strong></div><div><small>Needed wage change</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="The cost level of a weaker member compared with a stronger member over time"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which type of trading bloc?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the integration stages in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The European Union", "The EU started as a customs union and developed into a single market where goods, services, capital and labour move freely, with a subset of members using the euro. It shows several stages of integration within one project.", "the ladder from a free trade area to monetary union, and the gains and costs of each stage.") +
rw("The euro area and weaker members", "After 2010, countries such as Greece and Spain with high unemployment and falling competitiveness could not devalue because they shared the euro. Adjustment came through wage cuts, lower government spending and higher unemployment, while a strong economy such as Germany gained from a currency that was weaker than its own would have been.", "the cost of a monetary union to weaker members, as in a past Paper 4 data set.") +
rw("USMCA and trade within a free trade area", "The United States, Mexico and Canada trade with few tariffs among themselves but each has its own tariffs on outsiders. Rules of origin decide how much of a vehicle must be made in the region to qualify for tariff-free trade.", "a free trade area and the need for rules of origin.") +
rw("Brexit and trade", "When the UK left the EU's single market and customs union, new customs checks and rules appeared on trade with the EU, raising costs for many firms. The UK gained the freedom to set its own tariffs and trade deals.", "the benefits of membership of a union that are lost on leaving, and the trade-off with sovereignty.")
)

mc_exam = [
  ("A country imposes a tariff on steel imports. What is the likely impact on its economy? (May/June 2025 · 31 · Q25, reworded)", ["Its steel exports become more price competitive", "Productive inefficiency in its steel industry", "An improvement in its terms of trade", "A fall in producer surplus for its steel producers"], 1, "Protection from foreign competition can reduce the incentive to cut costs. Domestic producers gain surplus, not lose it."),
  ("The US introduced tariffs on many imports from China in 2018. Which policy type was this? (Oct/Nov 2024 · 32 · Q25, reworded)", ["Expenditure-reducing", "Expenditure-switching", "Expansionary monetary", "Contractionary monetary"], 1, "Tariffs switch spending from imports to domestic goods."),
  ("What is a failure of government microeconomic intervention? (Feb/March 2024 · 32 · Q13, reworded)", ["An indirect tax equal to external costs is imposed on cigarettes and demand falls", "Limits are placed on a union's restrictions that increase labour mobility", "Price controls on bread are removed", "Tariffs on imports raise the Gini coefficient"], 3, "A policy that worsens an objective, such as higher inequality, is a government failure. The other three work as intended."),
  ("Which is an example of an expenditure-switching policy? (Feb/March 2023 · 32 · Q29, reworded)", ["Higher income tax rates", "Higher interest rates", "Higher tariff rates", "A larger money supply"], 2, "Tariffs change the mix of spending from imports to domestic goods. The others reduce total spending."),
  ("What is most likely to be an appropriate action to reduce both a current account surplus and inflation? (Oct/Nov 2021 · 32 · Q30, reworded)", ["Lower the rate of interest", "Devalue the currency", "Increase direct taxes", "Remove tariffs on imports"], 3, "Removing tariffs lowers import prices, which cuts inflation and raises imports, reducing the surplus.")
]

exam = exam_page("trading blocs, trade creation and trade diversion",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Free trade areas and customs unions appear in 20 mark essays, with a diagram usually required, and monetary union appears in data response. Reworded past questions are below, with a practice question and five Paper 3 multiple choice questions (the Paper 3 questions on trade creation and customs unions use diagrams that are not reproduced here).",
  [("Essays, 20 marks", "3", "May/June 2025 (41 and 43) Q5; Oct/Nov 2024 (41) Q5; Oct/Nov 2024 (43) Q5"), ("Data response, 8 marks", "1", "Oct/Nov 2020 (41) Q1(c)"), ("Multiple choice (Paper 3)", "5 shown below", "2021 to 2025")],
  [
  eq("Based on May/June 2025 · 9708/41 and 43 · Q5", "20 marks", "A free trade area gains all the benefits of being a member of a customs union while avoiding all the costs of membership. Evaluate this statement.",
     ["Define a free trade area (removal of tariffs and quotas between members) and a customs union (no tariffs between members plus a common external tariff).",
      "A country in an FTA can gain faster growth through specialisation and a global market; lower tariffs reduce firms' costs, raise incomes, increase competition and may raise productivity.",
      "A customs union shares protection from outsiders while giving access to a large single market, and members may gain from trade creation.",
      "Evaluation: a customs union may cost sovereignty; trade diversion can occur because members must adopt the common external tariff, causing a misallocation of resources."],
     "Define both. Benefits shared by FTA and customs union. What a union adds: common external tariff and bargaining power. Costs: sovereignty, trade diversion. Judge: statement is only partly true.",
     [[("k", "In a free trade area members remove tariffs and quotas on trade among themselves but keep their own tariffs on outsiders. A customs union does the same but also adopts a common external tariff."), ("n", "Both could give lower prices, more competition and economies of scale from specialisation, so many of the gains are the same. In a customs union, members also share protection against outside competitors, have more bargaining power in trade talks, and do not need rules of origin to stop goods entering through the lowest-tariff member.")],
      [("e", "On the other hand, a customs union has costs that an FTA avoids: a member must accept the common external tariff and gives up some sovereignty. When a member has to raise its tariff on a cheaper non-member, trade diversion may occur, which could reduce allocative efficiency. So the statement is partly true, since an FTA avoids those costs, but it does not gain all the benefits, such as the shared bargaining power. The net result may depend on the pattern of trade.")]]),
  eq("Based on Oct/Nov 2024 · 9708/41 · Q5", "20 marks", "In recent years many countries have joined or set up a free trade area. Evaluate, with the help of a diagram, whether membership of an FTA is always beneficial to a country.",
     ["Define an FTA, give examples, define a tariff and non-tariff barriers and show the effect of removing them: lower prices, more consumer surplus, greater allocative efficiency, economies of scale. A diagram is required (maximum Level 2 without).",
      "Diagram of the domestic market with a tariff, the fall in price when the tariff is removed, the change in domestic output and the gain in consumer surplus.",
      "Evaluation: the effect depends on elasticities; structural unemployment where demand shifts to imports; polluting production may move to members; cheaper inputs may raise competitiveness; at the macro level, the effect depends on the marginal propensities to export and import and the effect on net exports, employment and the multiplier."],
     "Define. Diagram: tariff removal lowers price, increases imports. Micro gains: consumer surplus, scale. Evaluation: elasticities, jobs, pollution, macro effect (X − M).",
     [[("k", "A free trade area removes tariffs and other barriers between members. A diagram of the domestic market shows that with a tariff the price is the world price plus the tariff. When the tariff is removed, the price falls, domestic output falls and consumption rises, so imports increase and consumer surplus increases."), ("n", "The lower prices raise allocative efficiency, and a larger market allows firms to benefit from economies of scale, which raises productive efficiency. Cheaper inputs may also lower firms' costs and make exports more competitive.")],
      [("e", "However, membership is not always beneficial. If demand and supply are inelastic the gains may be small. Domestic producers that cannot compete may close, causing structural unemployment, and polluting industries may relocate. At the macro level, the effect on aggregate demand depends on whether exports rise by more than imports. So membership is probably beneficial overall, but the effect depends on the country's industries and policies.")]]),
  eq("Based on Oct/Nov 2020 · 9708/41 · Q1(c)", "8 marks", "Spain and Greece use the euro and so cannot devalue. They have had to adjust their domestic policies, reducing wages and government spending. Discuss the possible effects on the Spanish and Greek economies of these policy changes.",
     ["Identify the likely policy outcome (2 marks): wages and government spending were cut.",
      "Consider the effect of wage decreases (3 marks) and of reduced government spending (3 marks)."],
     "Link cuts to wages: lower costs but lower consumption. Link cuts in government spending: lower AD, higher unemployment, but lower deficit. Judge.",
     [[("k", "Because they share the euro and cannot devalue, Spain and Greece have to improve competitiveness by cutting labour costs and reducing government spending."), ("n", "Lower wages reduce firms' costs and could make exports cheaper, raising net exports over time. However, they also lower workers' incomes and consumption, which reduces aggregate demand and may raise unemployment in the short run. Cuts in government spending could narrow the budget deficit but also reduce aggregate demand, output and public services.")],
      [("e", "The result could be a slow adjustment with high unemployment, as in these countries, while a stronger economy such as Germany had no need to adjust. The gains in competitiveness may take years, so the policies could reduce living standards in the short run.")]]),
  eq("Practice question · modelled on the 8 mark style (no past paper)", "8 marks", "Explain what is meant by trade creation and trade diversion when a country joins a customs union.",
     ["Trade creation: higher-cost domestic output replaced by lower-cost imports from a partner; gains from more efficient production and more consumption.",
      "Trade diversion: imports switched from a lower-cost non-member to a higher-cost member because of the common external tariff; a loss of efficiency.",
      "A short development, possibly with the net effect depending on the size of each."],
     "Define trade creation with the gain. Define trade diversion with the loss. Net effect.",
     [[("k", "Trade creation occurs when the removal of tariffs on a partner's goods causes domestic output that is more expensive than the partner's to be replaced by imports from the partner. Resources are used more efficiently, and consumers pay a lower price and buy more.")],
      [("k", "Trade diversion occurs when a country that joins a customs union switches from importing from a low-cost world supplier outside the union to a higher-cost partner inside, because the common external tariff makes outsiders' goods dearer."), ("n", "This is a loss because resources are used less efficiently and the government loses tariff revenue."), ("e", "The net welfare effect of joining depends on whether the gains from trade creation outweigh the loss from trade diversion.")]])
  ],
  )

tips = tips_html(
  [("Know the ladder.", "Free trade area, customs union, monetary union, full economic union: each adds something."),
   ("Say what a customs union adds.", "A common external tariff."),
   ("Draw the tariff diagram.", "Domestic supply and demand, the world price and the price with the tariff, with shaded areas."),
   ("Define trade creation and diversion with the effect.", "Creation: cheaper partner replaces dearer domestic output. Diversion: dearer partner replaces cheaper world supplier."),
   ("Say the net effect depends.", "Gains from creation against losses from diversion."),
   ("For monetary union, mention the lost tools.", "No exchange rate or independent interest rate for weaker members."),
   ("Evaluate FTA versus customs union.", "FTA keeps freedom; the union shares protection and bargaining power.")],
  [("FTA", "In a free trade area members remove barriers among themselves but keep their own tariffs on outsiders."),
   ("Customs union", "A customs union adds a common external tariff, which could cause trade diversion."),
   ("Creation", "Trade creation may occur when domestic output is replaced by cheaper imports from a partner."),
   ("Diversion", "Trade diversion may occur when imports switch from a cheaper outsider to a dearer partner."),
   ("Monetary union", "Members of a monetary union could lose the ability to use exchange rate or interest rate policy to deal with their own problems.")],
  [CW["define"], CW["explain"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- Ladder of integration ---------- */
function ladDraw(s) {
  const step = (i, t, sub, k) => { if (k <= 0) return ""; const x = 60 + i * 165, y = 230 - i * 50; return SV.rect(x, y, 150, 280 - y, "f1", op(0.25 + 0.15 * i)) + SV.text(x + 75, y + 24, t, "lbl bd", { "text-anchor": "middle", ...op(k) }) + sub.split("|").map((l, j) => SV.text(x + 75, y + 46 + j * 16, l, "sm", { "text-anchor": "middle", ...op(k) })).join(""); };
  let o = SV.line(40, 280, 730, 280); o += step(0, "Free trade area", "No internal tariffs|Own external tariffs", s.a) + step(1, "Customs union", "+ common external|tariff", s.b) + step(2, "Monetary union", "+ single currency|+ central bank", s.c) + step(3, "Full economic union", "+ common policies|+ free factor movement", s.d);
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Four steps of economic integration from a free trade area to a full economic union">${ladDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stL"), { w: 760, h: 300, label: "Ladder of economic integration", base: { a: 0, b: 0, c: 0, d: 0 }, draw: ladDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Free trade area.</b> Members abolish tariffs and quotas on trade between themselves. Each keeps its own tariffs on non-members.", s: { a: 1 } },
  { cap: "<b>Customs union.</b> Members also agree one common external tariff on outsiders, so goods can enter any member on the same terms.", s: { a: 1, b: 1 } },
  { cap: "<b>Monetary union.</b> Members share a currency and a central bank, so there is no exchange rate risk but no independent monetary policy.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Full economic union.</b> Members coordinate fiscal and other economic policies, with free movement of labour and capital and common regulations.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Trade creation and diversion diagram ---------- */
const dP = (q) => (120 - q) / 8, sP = (q) => (q + 10) / 10, qD = (p) => 120 - 8 * p, qS = (p) => Math.max(0, 10 * p - 10);
function tcModel(t, pp) { const pw = 3, p0 = pw + t, p1 = Math.min(pp, p0), qd0 = qD(p0), qs0 = qS(p0), qd1 = qD(p1), qs1 = qS(p1), prod = 0.5 * (p0 - p1) * (qs0 - qs1), cons = 0.5 * (p0 - p1) * (qd1 - qd0), tc = prod + cons, td = pp > pw && p1 === pp ? (pp - pw) * (qd0 - qs0) : 0; return { pw, p0, p1, qd0, qs0, qd1, qs1, prod, cons, tc, td, net: tc - td, same: p1 >= p0 }; }
function tcSvg(t, pp, st, X, Y, w) {
  const m = tcModel(t, pp); let o = SV.line(X(0), Y(0), X(135), Y(0)) + SV.line(X(0), Y(0), X(0), Y(9.2)) + SV.text(X(135), Y(0) + 24, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(X(0) + 6, Y(9.2) - 4, "Price ($)", "sm");
  o += SV.line(X(0), Y(15), X(120), Y(0), "c1") + tag(X(54), Y(8.1), "D", "t1", 1, "start") + SV.line(X(0), Y(1), X(135), Y(14.5), "c3") + tag(X(78), Y(8.8) - 6, "S", "t3", 1, "end");
  o += SV.line(X(0), Y(m.pw), X(135), Y(m.pw), "c2 dash") + tag(X(133), Y(m.pw) + 16, "world price " + m.pw, "t2", 1, "end") + SV.line(X(0), Y(m.p0), X(135), Y(m.p0), "c4 dash") + tag(X(133), Y(m.p0) - 6, "with tariff " + Lib.fmtN(m.p0, 1), "t4", 1, "end");
  if (st >= 1) o += SV.line(X(0), Y(pp), X(135), Y(pp), "c1 dash") + tag(X(2), Y(pp) - 6, "partner price " + Lib.fmtN(pp, 1), "t1", st >= 1 ? 1 : 0);
  if (st >= 2 && !m.same) o += SV.poly([[X(m.qs1), Y(m.p1)], [X(m.qs0), Y(m.p0)], [X(m.qs0), Y(m.p1)]], "f3", { opacity: 0.55 }) + SV.poly([[X(m.qd0), Y(m.p0)], [X(m.qd1), Y(m.p1)], [X(m.qd0), Y(m.p1)]], "f3", { opacity: 0.55 }) + tag(X((m.qs0 + m.qs1) / 2), Y(m.p1) + 20, "production gain", "t3", 1, "end") + tag(X(m.qd0 + 4), Y(m.p1) + 20, "consumption gain", "t3", 1, "start");
  if (st >= 3 && !m.same && m.td > 0) o += SV.rect(X(m.qs0), Y(m.p1), X(m.qd0) - X(m.qs0), Y(m.pw) - Y(m.p1), "f2", { opacity: 0.6 }) + tag(X((m.qs0 + m.qd0) / 2), (Y(m.p1) + Y(m.pw)) / 2 + 4, "trade diversion", "t2", 1, "middle");
  return o;
}
const TX = (q) => 70 + q * 5, TYY = (p) => 300 - p * 29;
$("#pic2").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Domestic market with a tariff, a partner price below the tariff-inclusive price, trade creation triangles and the trade diversion rectangle">${tcSvg(3, 4.2, 3, TX, TYY)}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 345, label: "A customs union: trade creation triangles and the trade diversion rectangle", base: { st: 0 }, draw: (s) => tcSvg(3, 4.2, Math.round(s.st), TX, TYY), tween: 600, dwell: 6200, steps: [
  { cap: "<b>Before.</b> The country imports at the world price of $3 plus a tariff of $3, so the domestic price is $6. Domestic firms supply 50 units, consumers buy 72, and 22 units are imported from the cheapest world supplier.", s: { st: 0 } },
  { cap: "<b>Joining the union.</b> A partner can supply tariff-free at $4.20, which is cheaper than $6 but dearer than the world price of $3. The domestic price falls to $4.20.", s: { st: 1 } },
  { cap: "<b>Trade creation.</b> Dear domestic output (50 down to 32) is replaced by cheaper imports (production gain), and consumers buy more (72 up to 86) at the lower price (consumption gain). The two shaded triangles are the gain.", s: { st: 2 } },
  { cap: "<b>Trade diversion.</b> The 22 units once bought at $3 from the world are now bought from the partner at $4.20. The rectangle ($1.20 × 22) is a loss. Net effect here: gain of 29.2 minus loss of 26.4, a small net gain.", s: { st: 3 } },
] });

/* ---------- Lab ---------- */
function labT() {
  if (!$("#tf") || !$("#pp")) return;
  const t = +$("#tf").value / 10, pp = +$("#pp").value / 10, m = tcModel(t, pp);
  $("#r1").textContent = m.same ? "none" : Lib.fmtN(m.tc, 1); $("#r2").textContent = m.same ? "none" : Lib.fmtN(m.td, 1); $("#r3").textContent = m.same ? "0" : (m.net >= 0 ? "+" : "") + Lib.fmtN(m.net, 1);
  $("#rv").textContent = m.same ? `The partner's price ($${pp.toFixed(1)}) is no lower than the tariff-inclusive price ($${m.p0.toFixed(1)}), so the country keeps buying at the world price plus the tariff and the union makes no difference to this good.` : `The price falls from $${m.p0.toFixed(1)} to $${m.p1.toFixed(1)}. Trade creation (production effect ${Lib.fmtN(m.prod, 1)} plus consumption effect ${Lib.fmtN(m.cons, 1)}) is ${Lib.fmtN(m.tc, 1)}. Trade diversion is the extra $${(pp - m.pw).toFixed(1)} paid on the ${Lib.fmtN(m.qd0 - m.qs0, 0)} units formerly imported from the world: ${Lib.fmtN(m.td, 1)}. Net effect: ${m.net >= 0 ? "a gain" : "a loss"} of ${Lib.fmtN(Math.abs(m.net), 1)}. ${m.net >= 0 ? "The union is better for the country when the partner is nearly as cheap as the rest of the world." : "The union is worse when the partner is much dearer than the world and the external tariff is high."}`;
  const X = (q) => 40 + q * 2.6, Y = (p) => 295 - p * 29; $("#labA").innerHTML = tcSvg(t, pp, 3, X, Y, 1);
}
Lib.slider($("#g1"), { id: "tf", label: "Tariff, $ ", min: 10, max: 40, step: 1, value: 30, fmt: (v) => (v / 10).toFixed(1), onInput: labT });
Lib.slider($("#g2"), { id: "pp", label: "Partner's price, $ ", min: 31, max: 70, step: 1, value: 42, fmt: (v) => (v / 10).toFixed(1), onInput: labT });
labT();

/* ---------- Lab 2 ---------- */
function labM() {
  if (!$("#yr")) return;
  const y = +$("#yr").value, gap = (Math.pow(1.03, y) - 1) * 100, adj = (1 - 1 / Math.pow(1.03, y)) * 100;
  $("#t1").textContent = "+" + Lib.fmtN(gap, 1) + "%"; $("#t2").textContent = gap > 10 ? "Badly weakened" : gap > 4 ? "Weakened" : "Slightly weaker"; $("#t3").textContent = "−" + Lib.fmtN(adj, 1) + "%";
  $("#tv").textContent = `After ${y} years of costs rising 3% a year faster than in the stronger member, the weaker member's costs are ${Lib.fmtN(gap, 1)}% higher relative to its partner. With one currency it cannot devalue, so to restore competitiveness its wages and prices must fall by about ${Lib.fmtN(adj, 1)}% relative to the partner's: an 'internal devaluation', which usually means unemployment and spending cuts.`;
  const X = (t) => 50 + t * 11, Y = (v) => 270 - (v - 100) * 4.2; let o = SV.line(50, 270, 400, 270) + SV.line(50, 270, 50, 20) + SV.text(400, 292, "Years", "sm", { "text-anchor": "end" }) + SV.text(56, 16, "Relative cost level (start = 100)", "sm") + SV.line(50, Y(100), 400, Y(100), "c3 dash");
  const pts = []; for (let t = 0; t <= y; t += 0.5) pts.push([X(t), Y(100 * Math.pow(1.03, t))]); if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c2");
  $("#labB").innerHTML = o + tag(X(y) - 4, Y(100 * Math.pow(1.03, y)) - 8, Lib.fmtN(100 * Math.pow(1.03, y), 0), "t2", 1, "end");
}
Lib.slider($("#g3"), { id: "yr", label: "Years in the union ", min: 1, max: 25, step: 1, value: 10, fmt: (v) => v, onInput: labM });
labM();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which stage of integration is it?", ["Free trade area", "Customs union", "Monetary union"],
  [("Members remove tariffs between themselves but set their own tariffs on non-members", 0), ("Members adopt a common external tariff", 1), ("Members use one currency and one central bank", 2), ("Rules of origin are needed to stop trade deflection", 0), ("No exchange rate risk between members", 2), ("Members negotiate trade deals as a single bloc", 1), ("A member can still sign its own trade agreements with outsiders", 0), ("A weaker member can no longer devalue", 2)],
  "Free trade area: no internal tariffs. Customs union: plus common external tariff. Monetary union: plus single currency.") + MATCH([
  ["Free trade area", "Members abolish tariffs and quotas between themselves"],
  ["Customs union", "A free trade area plus a common external tariff"],
  ["Monetary union", "Members share a single currency and central bank"],
  ["Trade creation", "Dearer domestic output replaced by cheaper imports from a partner"],
  ["Trade diversion", "Imports switched from a cheaper outsider to a dearer partner"],
  ["Common external tariff", "One tariff all members charge on goods from outside the union"]]) + ORDER(
  "Put the integration stages in order, least integrated first.",
  ["Free trade area", "Customs union", "Monetary union", "Full economic union"],
  "Each stage adds a new level of integration.") + CALC([
  {"q": "The world price is $3 and the tariff is $3. A partner offers $4.20 tariff-free. By how much does the domestic price fall ($)?", "a": 1.8, "unit": "$", "tol": 0.01, "hint": "6 − 4.20.", "sol": "<b>$1.80</b>."},
  {"q": "Before joining, the country imported 22 units at the world price of $3. The partner price is $4.20. Calculate the trade diversion loss ($).", "a": 26.4, "unit": "$", "tol": 0.1, "hint": "(4.20 − 3.00) × 22.", "sol": "1.20 × 22 = <b>$26.4</b>."},
  {"q": "The production effect is 16.2 and the consumption effect is 13.0. Calculate total trade creation (1 decimal place).", "a": 29.2, "unit": "", "tol": 0.1, "hint": "Add them.", "sol": "<b>29.2</b>."},
  {"q": "A member's costs rise 3% a year faster than its partner's for 10 years. By about what percentage are its costs relatively higher (%, 1 decimal place)?", "a": 34.4, "unit": "%", "tol": 0.3, "hint": "1.03^10 − 1.", "sol": "1.03^10 = 1.344, so about <b>34.4%</b>."}]) + MCQ([
  ("A customs union differs from a free trade area because it has:", ["A common external tariff", "No tariffs between members", "A single currency", "No non-tariff barriers"], 0, "Members apply the same tariff to outsiders."),
  ("Trade diversion occurs when:", ["Imports switch from a lower-cost outsider to a higher-cost partner", "Domestic output is replaced by cheaper partner imports", "Exports fall to zero", "A currency is devalued"], 0, "The common external tariff makes outside goods dearer."),
  ("Trade creation is a:", ["Gain, as cheaper imports replace dearer domestic output", "Loss, as dearer imports replace cheaper ones", "Cost of tariffs", "Change in the exchange rate"], 0, "Production and consumption efficiency improve."),
  ("A disadvantage of a monetary union for a weaker member is that it:", ["Cannot devalue its currency", "Pays more tariffs", "Loses all its exports", "Has too much monetary independence"], 0, "It has no exchange rate adjustment."),
  ("The net effect of joining a customs union is more likely to be positive if:", ["The partner's price is close to the world price", "The external tariff is very high", "The partner is much less efficient", "Demand is perfectly inelastic"], 0, "Trade diversion is smaller when the partner is nearly as efficient as outsiders.")
], "qz1") + CARDS([
  ("Free trade area", "No internal tariffs; own external tariffs."),
  ("Customs union", "FTA + common external tariff."),
  ("Monetary union", "Single currency and central bank."),
  ("Full economic union", "Common economic policies as well."),
  ("Trade creation", "Cheaper partner replaces dearer domestic output."),
  ("Trade diversion", "Dearer partner replaces cheaper outsider."),
  ("Net effect", "Creation minus diversion."),
  ("Cost of monetary union", "No devaluation or independent interest rate.")]) + MCQ(mc_exam)

build("sy1162", "trading-blocs-trade-creation-diversion", "Trading Blocs, Trade Creation and Trade Diversion", EY,
  "11.6.2 to 11.6.3: free trade areas, customs unions, monetary and full economic union, and the gains and losses from trade creation and trade diversion. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
