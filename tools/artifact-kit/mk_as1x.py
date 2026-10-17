"""AS syllabus 1.4.4 The mixed economy. Run: python3 tools/artifact-kit/mk_as1x.py"""
from as6k import *
EY = EYAS("1.4.4")

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p>A <b class="kw">mixed economy</b> combines the <b>price mechanism</b>, which allocates most goods and services, with <b>government intervention</b>, which provides <b>public goods</b> and some <b>merit goods</b> (such as health and education), regulates markets, taxes and subsidises, redistributes income and sometimes owns industries. Almost every real economy is mixed, and economies lie on a <b class="kw">spectrum</b> between the extremes of a pure market and a pure planned system, with the position depending on the <b>share of government spending</b>, the amount of <b>state ownership</b> and the degree of <b>regulation and price control</b>. The advantages are that it keeps the <b>efficiency, choice and incentives</b> of markets while the government corrects <b>market failure</b> and reduces <b>inequality</b>. The disadvantages are that intervention can itself cause problems (<b>government failure</b>, distorted prices, higher taxes reducing incentives, inefficient state firms) and that there is no agreement on the right balance. Merit goods are often supplied by <b>both</b> the public and private sectors.</p></div>

  <h2>1 · Features of a mixed economy</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Both sectors:</b> a <b>private sector</b> of firms and households operating in markets, and a <b>public sector</b> owned or run by the government.</li>
    <li><b>Prices allocate most resources</b>, but the government changes outcomes through taxes, subsidies, regulation and provision.</li>
    <li><b>Mixed ownership:</b> most firms are private, some industries may be state-owned (nationalised), such as utilities or transport.</li>
    <li><b>Social aims:</b> a safety net, equal access to essentials and protection for consumers and workers.</li>
  </ul>

  <h2>2 · The role of government in a mixed economy</h2>
  <div class="tw"><table class="t">
    <tr><th>Role</th><th>What the government does</th><th>Reason</th></tr>
    <tr><td><b>Provide public goods</b></td><td>Defence, street lighting, flood defences, roads</td><td>The market will not supply them (free riders)</td></tr>
    <tr><td><b>Provide or subsidise merit goods</b></td><td>Education, healthcare, vaccinations</td><td>Under-consumed because of information failure and limited incomes</td></tr>
    <tr><td><b>Discourage demerit goods</b></td><td>Taxes, bans, warnings, minimum prices</td><td>Over-consumed because of imperfect information</td></tr>
    <tr><td><b>Control prices</b></td><td>Maximum and minimum prices</td><td>Affordability and stable incomes</td></tr>
    <tr><td><b>Regulate and promote competition</b></td><td>Competition law, consumer protection, health and safety</td><td>Prevents monopoly power and harm</td></tr>
    <tr><td><b>Redistribute income</b></td><td>Progressive taxes, benefits, free services</td><td>Reduces inequality</td></tr>
    <tr><td><b>Own some industries</b></td><td>Nationalised utilities, state firms</td><td>Strategic or public interest reasons</td></tr>
    <tr><td><b>Stabilise the economy</b></td><td>Fiscal and monetary policy, supply-side policy</td><td>Macroeconomic objectives</td></tr>
  </table></div>

  <h2>3 · The spectrum: how mixed is the economy?</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Share of government spending</b> in GDP: a higher share means a more mixed or state-led economy.</li>
    <li><b>State ownership:</b> a larger public sector means less reliance on the market.</li>
    <li><b>Regulation and price controls:</b> more rules mean more intervention.</li>
    <li>There is no single correct balance. Economies move along the spectrum over time, for example towards more privatisation or more provision.</li>
  </ul>

  <h2>4 · Advantages and disadvantages</h2>
  <div class="tw"><table class="t">
    <tr><th>Advantages</th><th>Disadvantages</th></tr>
    <tr><td><b>Efficiency and choice</b> from competition and the price mechanism in most markets</td><td><b>Government failure:</b> lack of information, poor decisions, bureaucracy and waste</td></tr>
    <tr><td><b>Public and merit goods</b> provided for all</td><td><b>Distorted prices</b> from taxes, subsidies and price controls</td></tr>
    <tr><td><b>Safety net:</b> less extreme inequality and protection for the vulnerable</td><td><b>High taxes</b> to fund provision may reduce work and enterprise incentives</td></tr>
    <tr><td><b>Regulation</b> protects consumers and workers and limits monopoly power</td><td><b>State firms</b> may be inefficient without a profit motive</td></tr>
    <tr><td><b>Flexibility:</b> the balance can be adjusted</td><td><b>No agreement</b> on the right balance; policies change with governments</td></tr>
  </table></div>
  <ul>
    <li><b>Merit goods are provided by both sectors:</b> the government cannot afford to supply everything, so private providers add capacity, choice and quality for those able to pay.</li>
    <li><b>Reducing the role of the market:</b> consumers may benefit through merit goods, fairness and protection, but may lose through inefficiency, less choice and higher taxes.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Always say that a mixed economy is a <b>spectrum</b> and ask <b>how mixed</b>. For each government role, name the <b>market failure</b> that justifies it, then give a possible <b>government failure</b> in the evaluation. Compare with a planned and a market economy where the question asks.</div>
'''

watch = '''
  <h2>1 · Why the market alone is not enough</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · Government failure</h2>
  <div id="stB"></div>
  <h2>3 · Merit goods from both sectors</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Where does the economy sit?</h2>
  <p>Set the share of government spending, state ownership and regulation. The labels describe the type of system.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Government role index</small><strong id="r1"></strong></div><div><small>Position</small><strong id="r2"></strong></div><div><small>Likely strength</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 130" role="img" aria-label="A scale from market economy to planned economy with the chosen position marked"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Choose a government role", "Choose a role of government to see the market failure behind it and a possible government failure.", ["Market failure addressed", "Government action", "Possible government failure"])

practise = '''
  <h2>1 · Government role or market outcome?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which type of good is it?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the move from market towards mixed in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
''' 

real = RWNOTE + (
rw("A mixed economy in action", "A typical economy has private shops, farms and factories operating through prices, together with state-funded schools, hospitals, roads and policing, regulation of food safety and taxes that fund benefits.", "a mixed economy as a combination of both.") +
rw("Education and healthcare from both sectors", "In many countries state schools and hospitals exist alongside private ones. The state provides access for everyone, while the private sector adds capacity and choice for those who pay.", "merit goods provided by both sectors.") +
rw("Nationalised industries", "A government may own railways, water or power companies to protect the public interest. Critics argue that state firms can be inefficient without competition, while supporters point to universal service.", "state ownership as an element of a mixed economy.") +
rw("Taxes on harmful goods", "A government places a high tax on cigarettes and bans smoking in public places. These interventions aim to reduce a demerit good that markets over-supply.", "government intervention to correct market failure.") +
rw("Price controls on essentials", "Rent controls and food price floors are used to protect households or farmers. They can improve fairness but may cause shortages or surpluses, an example of government failure.", "price controls and their side effects.")
)

mc_exam = [
  mcq("m24_12", 4, "What is the main reason an economy is unlikely to rely completely on market forces to allocate resources?", ["Demerit goods will be over supplied", "Merit goods will be under supplied", "Private goods will not be supplied", "Public goods will not be supplied"], 3, "Public goods would not be provided at all in a pure market, which is the most serious failure."),
  mcq("s24_12", 2, "What is produced in a mixed economy but not in a free market economy?", ["Demerit goods", "Free goods", "Private goods", "Public goods"], 3, "Governments provide public goods in a mixed economy; a free market would not supply them."),
  mcq("s25_13", 5, "Which goods would be expected to be produced in a mixed economy?", ["private goods, public goods and goods with external benefits", "private goods and public goods only", "private goods and goods with external benefits only", "goods with external benefits only"], 0, "A mixed economy produces private goods through markets, and public goods and goods with external benefits (merit goods) through government provision or support."),
  mcq("s25_14", 3, "Under which conditions are free market forces most likely to allocate resources efficiently in an economy? (the number of demerit, merit and public goods needed by consumers)", ["a few of each type", "many demerit, many merit and a few public goods", "no demerit goods, many merit goods and no public goods", "no demerit goods, no merit goods and no public goods"], 3, "Markets work best when there is no market failure, so no demerit, merit or public goods are needed.")
]

exam = exam_page("the mixed economy",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The mixed economy is among the most common 12 mark Paper 2 questions, asking about advantages, the role of government, how mixed an economy should be and moving between systems. Reworded past questions are below, with four Paper 1 multiple choice questions.",
  [("Essay parts, 12 marks", "5", "Feb/March 2023 (22) Q2(b); May/June 2022 (21) Q2(b); Oct/Nov 2021 (23) Q2(b); Oct/Nov 2024 (21) Q3(b); Oct/Nov 2020 (21) Q2(b)"), ("Multiple choice (Paper 1)", "4 shown below", "2024 to 2025")],
  [
  eq(P("m23_22", "2(b)"), "12 marks", "Assess whether all market economies should become mixed economies.",
     ["Analysis (up to 8): for staying a market economy: little government intervention, decisions based on demand and supply, competition makes production more efficient, consumers and producers act in their own interests.",
      "For becoming mixed: market economies fail to provide public goods, under-consume merit goods, over-consume demerit goods and may have prices that are too low, too high or too unstable.",
      "A one-sided response can only reach Level 2.",
      "Evaluation (up to 4): whether all market economies should become mixed, leading to a justified conclusion; a one-sided answer cannot gain evaluation marks."],
     "Case for staying market. Case for mixed (market failure). Judge: how much government is needed.",
     [[("k", "A market economy relies on the price mechanism and private firms. The argument for staying as it is rests on competition, which encourages productive efficiency and innovation, and on consumers' freedom to choose, with little bureaucracy."), ("n", "The argument for becoming mixed is that markets fail. They do not provide public goods because of free riders, they under-consume merit goods such as education and over-consume demerit goods such as tobacco, and prices of essentials may be too high or unstable. Government provision, taxes, subsidies and regulation can correct these problems.")], [("e", "Most economies are already mixed, so the real question is how mixed. If a market economy already has strong institutions and few failures, it may need only limited intervention. But because public goods will not be provided in a pure market, some government role is probably needed in all economies.")]]),
  eq(P("s22_21", "2(b)"), "12 marks", "Discuss the advantages of a mixed economy and whether it is always preferable to a planned economy.",
     ["Analysis (up to 8): the advantages and disadvantages of a mixed economy (up to 4), such as the price mechanism operating in many areas with its functions of rationing, signalling and transmitting preferences, government intervention through maximum or minimum prices and nationalised industries, against distorted price mechanisms from taxes and subsidies and the possibility of market failure; and the advantages and disadvantages of a planned economy (up to 4), such as the government directly providing certain goods and services, against bureaucracy and less efficiency.",
      "Evaluation (up to 4): a judgement on whether a mixed economy is always preferable to a planned economy, with a reserved mark for a conclusion."],
     "Mixed: price mechanism plus intervention; risks of distortion. Planned: provision, but bureaucracy and inefficiency. Judge: usually preferable, but depends on how mixed.",
     [[("n", "A mixed economy lets the price mechanism ration goods, signal preferences and incentivise firms in most markets, while the government provides public goods, regulates and may use price controls or nationalisation. But taxes and subsidies can distort prices and market failure may remain. A planned economy lets the state provide goods directly, but a larger role for government brings bureaucracy and less efficiency, with no price signals to guide planners.")], [("e", "A mixed economy is usually preferable to a planned economy because it keeps efficiency and choice, but it is not always so: where the government is weak or corrupt, or where goods must be shared fairly in a crisis, more planning may work better. The answer depends on how mixed the economy is.")]]),
  eq(P("w21_23", "2(b)"), "12 marks", "Discuss the view that in a mixed economy the only role of government should be to provide public goods and the supply of merit goods should be left to the private sector.",
     ["Analysis (up to 8): why the government provides public goods (the free rider problem, non-excludability and non-rivalry); the case for the private sector supplying merit goods, such as efficiency and choice; and the case against, such as under-consumption and under-provision of merit goods because of information failure and low incomes.",
      "Evaluation (up to 4): a judgement on whether the only role of government should be to provide public goods; without government involvement some merit goods may be under-provided, and a reserved mark for a conclusion. No KU marks for merely defining terms in the question."],
     "Public goods: the government must supply. Merit goods: private sector efficiency versus under-provision. Judge: government role in merit goods is also needed.",
     [[("n", "Public goods must be provided by the government because they are non-excludable and non-rival, so private firms cannot charge and free riders mean no supply. Leaving merit goods to the private sector could bring efficiency, choice and competition, but merit goods such as education and healthcare are under-consumed because people lack information or income, so a private-only supply would leave many without access.")], [("e", "The government's role should not be restricted to public goods. Some merit goods may be under-provided without government involvement, so a mixture of public provision or subsidy and private supply is likely to give the best outcome.")]]),
  eq(P("w24_21", "3(b)"), "12 marks", "Assess whether consumers always benefit when the government of a mixed economy reduces the role of the market mechanism in allocating resources.",
     ["Analysis (up to 8): the advantages of the market mechanism in a mixed economy (decisions made by individual consumers and producers acting in their own interest, resources allocated by price with little intervention) and its disadvantages (under-provision of merit goods, over-provision of demerit goods, public goods not provided); the advantages of government intervention (decisions in the national interest, a more equitable distribution of income) and its disadvantages.",
      "Evaluation (up to 4): a judgement on whether consumers always benefit, with a conclusion. A one-sided response cannot gain evaluation marks."],
     "Market: choice, efficiency; fails for public, merit, demerit goods. Government: equity, national interest; costs, inefficiency. Judge: depends on the market failure and how well the state acts.",
     [[("n", "Consumers may benefit when the government reduces the role of the market, because it can provide public goods, subsidise merit goods, curb demerit goods and make the distribution of income fairer. But the market mechanism offers choice, competition and prices that reflect preferences, and a bigger government role may mean taxes and subsidies that distort prices, bureaucracy and less choice.")], [("e", "Consumers do not always benefit. Where market failure is serious, as with public goods, more government involvement helps, but where intervention is badly designed, consumers can lose out through higher taxes and less choice. The effect depends on how well the government acts.")]]),
  eq(P("w20_21", "2(b)"), "12 marks", "Discuss why in most mixed economies, resources are mainly allocated using market forces and the price mechanism.",
     ["Analysis (up to 8): analysis of the market forces and price mechanism element (up to 4): the price mechanism, prices as signals of consumer preferences, private ownership and decision-making with little government intervention; and of the government intervention element (up to 4): the use of the word 'mainly' makes clear that market forces are not the exclusive method of allocation, with a public sector providing public and merit goods.",
      "Evaluation (up to 4): a judgement on why resources are mainly, but not exclusively, allocated using market forces and the price mechanism, with a reserved mark for a conclusion."],
     "Market: price signals, efficiency, choice, incentives. Government: public and merit goods, regulation. Judge: markets are efficient for most goods, but fail for some.",
     [[("n", "Most resources are allocated by markets because the price mechanism rations scarce goods, signals consumer preferences and gives firms an incentive to be efficient, with little need for central planning. Private ownership and competition encourage innovation and choice. But markets fail to provide public goods, under-consume merit goods and over-consume demerit goods, so governments provide or regulate these, which is why resources are only mainly, not entirely, allocated by markets.")], [("e", "The market is the main method because it is generally efficient and flexible, whereas heavy government control tends to be slow and inefficient. A government role remains necessary where markets fail, so a mixed system, with the market doing most of the allocation, is likely to work best.")]])
  ],
  )

tips = tips_html(
  [("Say 'spectrum'.", "Ask how mixed the economy is."),
   ("Name the government roles.", "Public goods, merit goods, regulation, redistribution."),
   ("Link each to a market failure.", "Why the government intervenes."),
   ("Cover government failure.", "Information, cost, distorted prices."),
   ("Merit goods from both sectors.", "State plus private supply."),
   ("Compare systems.", "Market, planned and mixed."),
   ("Judge.", "Depends on how well the state acts.")],
  [("Mixed economy", "A mixed economy combines the price mechanism with government intervention."),
   ("Public sector", "The public sector is the part of the economy owned or run by the government."),
   ("Private sector", "The private sector is the part owned by households and firms."),
   ("Nationalisation", "Nationalisation is the transfer of a private firm to state ownership."),
   ("Government failure", "Government failure is when intervention makes the allocation of resources worse.")],
  [CW["define"], CW["explain"], CW["assess"], CW["discuss"]]) + FC

js = CHAINJS + '''
$("#pic1").innerHTML = (() => {
  const B = [["Private sector", "Firms and households in markets: prices allocate most goods", 30, "f1"], ["Public sector", "Government provides public and merit goods, regulates, taxes", 270, "f2"], ["Mixed economy", "Both together: how mixed varies by country", 510, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 220, 100, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 44, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }); const w = d.split(": "); w.forEach((p, i) => { o += SV.text(x + 110, 70 + i * 20, i === 0 ? p + ":" : p, "sm", { "text-anchor": "middle" }); }); });
  return `<svg viewBox="0 0 760 124" role="img" aria-label="A mixed economy has a private sector and a public sector">${o}</svg>`;
})();
function specDraw(x) {
  let o = SV.line(60, 70, 700, 70, "c4", { "stroke-width": 4 }) + SV.text(60, 40, "Market economy", "lbl bd") + SV.text(700, 40, "Planned economy", "lbl bd", { "text-anchor": "end" }) + SV.text(380, 40, "Mixed economies", "lbl bd", { "text-anchor": "middle" });
  o += SV.text(60, 108, "little government role", "sm") + SV.text(700, 108, "state decides almost everything", "sm", { "text-anchor": "end" });
  const px = 60 + (x / 100) * 640; o += SV.circle(px, 70, 10, "dot3") + SV.text(px, 58, Math.round(x) + "", "lbl bd", { "text-anchor": "middle" });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 130" role="img" aria-label="The spectrum from market to planned economy">${specDraw(45)}</svg>`;
chainStep("#stA", "Why the market alone is not enough", ["A pure market has no government role", "Public goods are not supplied (free riders)", "Merit goods are under-consumed; demerit goods over-consumed", "Essentials may be unaffordable to those with low incomes", "Governments intervene: the economy becomes mixed"], [
  "<b>Pure market:</b> the price mechanism alone.", "<b>No revenue</b> for firms providing public goods.", "<b>Imperfect information</b> and limited incomes.", "<b>Inequality:</b> output goes to those who can pay.", "<b>The mixed economy</b> adds provision, regulation and taxes."]);
chainStep("#stB", "Government failure", ["The government intervenes to correct a market failure", "It lacks full information about the right quantity or price", "Taxes, subsidies or price controls distort prices", "Waste, shortages or surpluses, or reduced incentives follow", "The result may be a worse allocation: government failure"], [
  "<b>Good intention:</b> fix market failure.", "<b>Information problem</b> for officials.", "<b>Price distortion.</b>", "<b>Unintended consequences.</b>", "<b>Evaluation point:</b> intervention does not always improve outcomes."]);
chainStep("#stC", "Merit goods from both sectors", ["Education and healthcare are merit goods: under-consumed in a free market", "The government provides or subsidises them so everyone has access", "Public funds are limited, so state provision may not meet all demand", "Private firms provide extra capacity and choice for those who can pay", "Both sectors supply: a mixed system for merit goods"], [
  "<b>Merit goods:</b> better than people realise.", "<b>Government role:</b> access for all.", "<b>The state cannot afford everything.</b>", "<b>The private sector</b> fills gaps.", "<b>Result:</b> a mixture of public and private supply."]);

function labS() {
  if (!["gs", "so", "rg"].every((i) => $("#" + i))) return;
  const gs = +$("#gs").value, so = +$("#so").value, rg = +$("#rg").value, idx = (gs / 70) * 40 + (so / 100) * 35 + (rg / 100) * 25;
  const name = idx < 15 ? "Close to a market economy" : idx < 35 ? "Mixed, market-led" : idx < 55 ? "Mixed, government-led" : idx < 80 ? "Heavily state-led" : "Close to a planned economy";
  $("#r1").textContent = Lib.fmtN(idx, 0); $("#r2").textContent = name; $("#r3").textContent = idx < 35 ? "Efficiency and choice" : idx < 55 ? "Balance of efficiency and equity" : "Equity and provision for all";
  $("#rv").textContent = `Government spending of ${gs}% of GDP, state ownership of ${so}% of industry and regulation at ${rg}% give a government role index of ${Lib.fmtN(idx, 0)}: ${name.toLowerCase()}. ${idx < 35 ? "Prices allocate most resources; the risk is market failure and inequality." : idx < 80 ? "The market and government share the work; the risks are government failure, high taxes and reduced incentives." : "Planners allocate most resources; the risks are the lack of price signals, shortages and weak incentives."}`;
  $("#labA").innerHTML = specDraw(idx);
}
Lib.slider($("#g1"), { id: "gs", label: "Government spending, % of GDP ", min: 10, max: 70, step: 5, value: 40, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g2"), { id: "so", label: "Share of industry owned by the state, % ", min: 0, max: 100, step: 10, value: 20, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g3"), { id: "rg", label: "Level of regulation and price controls, % ", min: 0, max: 100, step: 10, value: 40, fmt: (v) => v + "%", onInput: labS });
labS();

chooser("h", [
  ["Providing public goods", "Free riders: the market does not supply them", "Fund and provide them from taxes", "Wrong quantity chosen because people do not reveal their valuation", 5],
  ["Providing or subsidising merit goods", "Under-consumption through imperfect information and low incomes", "Free provision, subsidies, information campaigns", "Waste, excess demand, high opportunity cost", 5],
  ["Taxing or banning demerit goods", "Over-consumption because harm is underestimated", "Taxes, bans, warnings, minimum prices", "Black markets; the tax may fall on the poor", 4],
  ["Price controls on essentials", "Prices too high for low-income households or unstable farm incomes", "Maximum or minimum prices", "Shortages or surpluses", 3],
  ["Regulating monopolies", "Market power: high prices and low output", "Competition law and price regulation", "Regulators lack information; may be captured by firms", 3],
  ["Redistributing income", "Inequality: output goes to those who can pay", "Progressive taxes and benefits", "Reduced incentives to work; cost", 3]
], (it) => `${it[0]}: the market failure is ${it[1].toLowerCase()}. The government acts through ${it[2].toLowerCase()}. A possible government failure: ${it[3].toLowerCase()}.`, "Strength of the case for intervention");
''' + CLASSIFY("cl1", "Is it a government role or a market outcome?", ["Government role in a mixed economy", "Market outcome"],
  [("Providing street lighting from taxes", 0), ("Firms producing what is profitable", 1), ("Banning smoking in public places", 0), ("Price rising when demand rises", 1), ("Subsidising healthcare", 0), ("Consumers choosing between brands", 1), ("Regulating monopolies", 0), ("Firms entering a profitable market", 1)],
  "The government provides public goods, corrects failure and regulates; the market allocates through prices and profit.") + CLASSIFY("cl2", "Which type of good is it?", ["Public good", "Merit good", "Demerit good"],
  [("Street lighting", 0), ("Education", 1), ("Tobacco", 2), ("National defence", 0), ("Vaccinations", 1), ("Harmful drugs", 2), ("Flood defences", 0), ("Healthcare", 1)],
  "Public goods are non-excludable and non-rival; merit goods are under-consumed; demerit goods are over-consumed.") + ORDER(
  "Put the move from a pure market towards a mixed economy in order.",
  ["A pure market fails to supply public goods", "Merit goods are under-consumed and demerit goods over-consumed", "The government provides, taxes and regulates", "The economy becomes mixed", "Government failure may then need to be addressed"],
  "Market failure leads to intervention and a mixed economy.") + MATCH([
  ["Mixed economy", "Price mechanism plus government intervention"],
  ["Public sector", "The part of the economy owned or run by government"],
  ["Private sector", "The part owned by households and firms"],
  ["Nationalisation", "Transfer of a firm to state ownership"],
  ["Government failure", "Intervention that makes the allocation worse"],
  ["Spectrum", "The range between pure market and pure planned economies"]]) + CALC([
  {"q": "Government spending is $400bn and GDP is $1000bn. What share of GDP is government spending (%)?", "a": 40, "unit": "%", "tol": 0.1, "hint": "400 ÷ 1000.", "sol": "<b>40%</b>."},
  {"q": "A government raises $120bn in tax and spends $150bn. What is the budget deficit ($bn)?", "a": 30, "unit": "$bn", "tol": 0.5, "hint": "150 − 120.", "sol": "<b>$30bn</b>."},
  {"q": "State firms produce $200bn of a $800bn GDP. What share is produced by the state (%)?", "a": 25, "unit": "%", "tol": 0.1, "hint": "200 ÷ 800.", "sol": "<b>25%</b>."},
  {"q": "Spending on healthcare is $80bn and GDP is $1600bn. What share of GDP is this (%)?", "a": 5, "unit": "%", "tol": 0.1, "hint": "80 ÷ 1600.", "sol": "<b>5%</b>."}]) + MCQ([
  ("A mixed economy combines:", ["The price mechanism and government intervention", "Planning and no prices", "Only private firms", "Only state firms"], 0, "Both methods of allocation."),
  ("Which is provided in a mixed economy but not in a pure market?", ["Public goods", "Private goods", "Luxury goods", "Substitutes"], 0, "Free riders stop market supply."),
  ("A disadvantage of a mixed economy is:", ["Government failure", "Wide consumer choice", "Efficient competition", "Public goods are provided"], 0, "Intervention can fail."),
  ("Merit goods in a mixed economy are often supplied by:", ["Both public and private sectors", "Only the state", "Only the market", "Only charities"], 0, "State plus private provision."),
  ("How mixed an economy is depends on:", ["Government spending, state ownership and regulation", "Only the exchange rate", "Only population", "Only tax rates"], 0, "The size of the government role.")
], "qz1") + CARDS([
  ("Mixed economy", "Markets plus government."),
  ("Spectrum", "How mixed is the economy?"),
  ("Public goods", "Government provides."),
  ("Merit goods", "State and private supply."),
  ("Demerit goods", "Taxes, bans, warnings."),
  ("Advantages", "Efficiency plus equity."),
  ("Disadvantages", "Government failure, distortion."),
  ("Nationalisation", "State ownership of a firm.")]) + MCQ(mc_exam)

build("as1x", "as-mixed-economy", "The Mixed Economy and the Role of Government", EY,
  "1.4.4: how a mixed economy combines markets and government, the roles of government, how mixed an economy is, and its advantages and disadvantages. Animated diagrams, labs, drills and past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
