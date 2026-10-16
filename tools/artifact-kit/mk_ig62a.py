"""Builds IGCSE Economics 6.2.1 to 6.2.3 (globalisation, its causes and consequences, MNCs), written from scratch.
Run: python3 tools/artifact-kit/mk_ig62a.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

# =========================================================== 6.2.1 Definition
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Globalisation</span> is the increasing connection and integration of the world's economies, through growing flows of <b>goods and services, money and investment, people, ideas and technology</b> between countries. A phone designed in one country, with parts made in three others, assembled in a fifth and sold worldwide is a product of globalisation. The world acts increasingly like a single market.</p></div>

  <h2>Features of globalisation</h2>
  <div class="tw"><table class="t">
    <tr><th>Feature</th><th>What it means</th><th>Example</th></tr>
    <tr><td><b>More international trade</b></td><td>Exports and imports grow faster than output</td><td>Cheap clothes from Asia sold in Europe</td></tr>
    <tr><td><b>Multinational companies (MNCs)</b></td><td>Firms produce and sell in many countries</td><td>Global car, phone and fast-food brands</td></tr>
    <tr><td><b>Foreign direct investment (FDI)</b></td><td>Firms build factories and offices abroad</td><td>A Japanese car plant in the UK</td></tr>
    <tr><td><b>Global supply chains</b></td><td>Different stages of production in different countries</td><td>Design in the USA, chips in South Korea, assembly in China</td></tr>
    <tr><td><b>Movement of people (migration)</b></td><td>Workers, students and tourists move between countries</td><td>Migrant workers in the Gulf states</td></tr>
    <tr><td><b>Movement of money</b></td><td>Capital flows and shared financial markets</td><td>Investors buying foreign shares</td></tr>
    <tr><td><b>Spread of ideas, technology and culture</b></td><td>Quick sharing of knowledge, brands and tastes</td><td>Social media, streaming, global fashion</td></tr>
  </table></div>

  <h2>Measuring how globalised an economy is</h2>
  <div class="formula">Trade openness = (exports + imports) ÷ GDP × 100</div>
  <p>A higher percentage means the economy is more open to trade. Small countries such as Singapore have very high openness; large countries such as the USA have lower openness because they have a large home market. Other measures include <b>FDI as a share of GDP</b>, the number of MNCs, and migration and communication links.</p>

  <h2>Why it matters</h2>
  <ul>
    <li>Consumers can buy a wider range of goods, often more cheaply.</li>
    <li>Firms can sell in bigger markets and source cheaper inputs, but face more competition.</li>
    <li>Events in one country (a financial crisis, a pandemic, a war) can spread quickly to others.</li>
    <li>It affects jobs, wages, the environment and the gap between rich and poor (see 6.2.2).</li>
  </ul>
  <p class="note">Globalisation is not new, but it has speeded up since the 1980s with cheaper transport, the internet and the removal of many trade barriers.</p>
'''
js = HEAD + COMMON + '''
const FLOW = ["Trade: goods and services cross borders", "Investment: firms build factories and offices abroad (FDI)", "People: workers, students and tourists move between countries", "Ideas and technology spread quickly", "Money: capital moves between countries' financial markets", "Culture and brands become global"];
Lib.stepper($("#stF"), { w: 760, h: 400, label: "What globalisation involves", base: { n: 0 }, draw: mkChain(FLOW, "--accent"), steps: chainSteps(["<b>Trade:</b> goods and services cross borders in growing amounts.", "<b>Investment:</b> firms build factories and offices abroad (<b>FDI</b>).", "<b>People:</b> workers, students and tourists move between countries.", "<b>Ideas and technology</b> spread quickly, for example through the internet.", "<b>Money</b> moves between countries' financial markets.", "<b>Culture and brands</b> become global. Together these link the world's economies."]) });
function scChart(s) {
  const nodes = [["Design", "USA"], ["Chips", "South Korea"], ["Screen", "Japan"], ["Assembly", "China"], ["Sold", "Worldwide"]]; let o = "";
  nodes.forEach(([a, b], i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 20 + i * 146, y = 130; let g = `<g opacity="${op}">` + SV.rect(x, y, 120, 90, "", { rx: 10, style: "fill:var(--accent);fill-opacity:0.15;stroke:var(--accent);stroke-width:2" }) + SV.text(x + 60, y + 38, a, "lbl bd", { "text-anchor": "middle", style: "font-size:17px" }) + SV.text(x + 60, y + 64, b, "sm bd", { "text-anchor": "middle", style: "font-size:14px" }); if (i < 4) g += SV.line(x + 122, y + 45, x + 142, y + 45, "ax", { style: "stroke-width:2.5" }) + SV.arrowHead(x + 144, y + 45, "r", "dot1"); o += g + "</g>"; });
  if (s.n >= 5) o += SV.text(380, 300, "One product, five stages, many countries", "lbl bd t3", { "text-anchor": "middle", style: "font-size:18px" });
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 360, label: "A global supply chain", base: { n: 0 }, draw: scChart, steps: [
  { cap: "A smartphone is <b>designed</b> in one country (here the USA).", s: { n: 1 } },
  { cap: "Its <b>chips</b> are made in South Korea, where firms have the skills and technology.", s: { n: 2 } },
  { cap: "The <b>screen</b> comes from Japan.", s: { n: 3 } },
  { cap: "It is <b>assembled</b> in China, where there are many skilled workers and large factories.", s: { n: 4 } },
  { cap: "It is <b>sold worldwide</b>. Each stage is done where it is cheapest or best: this is <b>globalisation</b> in action (and also specialisation). It also means a problem in one country can disrupt the whole chain.", s: { n: 5 } },
] });
function trChart(s) {
  const d = [["1970", 26], ["1990", 39], ["2008", 61], ["2020", 52]], base = 310, k = 4.2; let o = SV.line(60, base, 710, base) + SV.text(60, 28, "World trade as a share of world GDP (%, rounded)", "sm");
  d.forEach(([y, v], i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 110 + i * 150, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 100, h, "", { style: "fill:var(--accent)", opacity: 0.85 }) + SV.text(x + 50, base - h - 8, v + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, base + 20, y, "sm", { "text-anchor": "middle" }) + "</g>"; });
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 380, label: "Trade has grown faster than output", base: { n: 0 }, draw: trChart, steps: [
  { cap: "In about <b>1970</b> trade (exports plus imports) was roughly a quarter of world GDP.", s: { n: 1 } },
  { cap: "By <b>1990</b> it had risen to around 39%, helped by lower tariffs and cheaper transport.", s: { n: 2 } },
  { cap: "By <b>2008</b> it peaked at around 60%: the height of globalisation, with global supply chains and big MNCs.", s: { n: 3 } },
  { cap: "In <b>2020</b> it fell back (pandemic, trade tensions) to roughly half of world GDP. Globalisation can slow or even go into reverse. Figures are approximate.", s: { n: 4 } },
] });

/* Lab 1 */
function labO() {
  if (!$("#oa") || !$("#ob") || !$("#oc")) return;
  const x = +$("#oa").value, m = +$("#ob").value, g = +$("#oc").value, open = ((x + m) / g) * 100;
  $("#oa1").textContent = money(open, 0) + "%"; $("#oa2").textContent = (x - m >= 0 ? "+" : "−") + "$" + Math.abs(x - m) + "bn"; $("#oa3").textContent = open > 100 ? "Very open" : open > 50 ? "Open" : open > 30 ? "Moderately open" : "Less open";
  $("#oav").textContent = `Trade openness = (${x} + ${m}) ÷ ${g} × 100 = ${money(open, 0)}%. ${open > 100 ? "Trade is larger than GDP: typical of small countries that trade re-exports or rely on imports, such as Singapore." : open > 50 ? "A very open economy: events abroad matter a lot." : "A larger, more self-contained economy: a bigger home market means less reliance on trade."}`;
  const base = 290; let o = SV.line(60, base, 700, base);
  [["This economy", open, "--accent"], ["Typical small open economy", 150, "--muted"], ["Typical large economy", 25, "--muted"]].forEach(([n, v, c], i) => { const h = Math.min(v, 160) * 1.5, xx = 120 + i * 190; o += SV.rect(xx, base - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(xx + 60, base - h - 8, money(v, 0) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(xx + 60, base + 20, n, "sm", { "text-anchor": "middle" }); });
  $("#labO").innerHTML = o + SV.text(60, 24, "Exports plus imports as % of GDP", "sm");
}
Lib.slider($("#g1"), { id: "oa", label: "Exports ($bn)", min: 10, max: 300, step: 10, value: 80, fmt: (v) => "$" + v, onInput: labO });
Lib.slider($("#g2"), { id: "ob", label: "Imports ($bn)", min: 10, max: 300, step: 10, value: 90, fmt: (v) => "$" + v, onInput: labO });
Lib.slider($("#g3"), { id: "oc", label: "GDP ($bn)", min: 100, max: 1000, step: 50, value: 400, fmt: (v) => "$" + v, onInput: labO });
const FT = [
  { n: "International trade", m: "Exports and imports grow.", e: "Shops full of goods from many countries.", x: "Gains: choice, lower prices. Risks: dependence." },
  { n: "Multinational companies", m: "Firms operate in several countries.", e: "Global brands in every city.", x: "Gains: jobs, investment. Risks: profits sent abroad." },
  { n: "Foreign direct investment", m: "Firms invest in factories, offices and shops abroad.", e: "A car plant built by a foreign firm.", x: "Gains: capital, technology. Risks: control by foreigners." },
  { n: "Migration", m: "People move to work, study or settle.", e: "Doctors from abroad working in hospitals.", x: "Gains: skills, remittances. Risks: brain drain." },
  { n: "Technology and communication", m: "Internet and mobile networks link people instantly.", e: "Video calls with overseas teams.", x: "Gains: lower costs. Risks: disruption of jobs." },
  { n: "Global culture", m: "Brands, music and ideas spread.", e: "Streaming shows watched worldwide.", x: "Gains: sharing. Risks: loss of local traditions." },
];
button_table("ftBtns", "ftOut", FT, 0, (p) => `<div class="tw"><table class="t"><tr><th>What it means</th><th>Example</th><th>Gains and risks</th></tr><tr><td>${p.m}</td><td>${p.e}</td><td>${p.x}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>feature of globalisation</b> or <b>not</b>?", buckets: [{ label: "Feature of globalisation" }, { label: "Not" }], items: [
  { text: "Rapid growth in international trade", b: 0 }, { text: "Firms producing in many countries", b: 0 }, { text: "Workers migrating to other countries", b: 0 }, { text: "Ideas and technology spreading quickly", b: 0 },
  { text: "A country banning all imports", b: 1 }, { text: "Firms only selling in their home town", b: 1 }, { text: "Trade falling to zero", b: 1 },
], done: "Globalisation is increasing integration of economies." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Globalisation", "Increasing connection and integration of the world's economies"],
  ["Multinational company", "A firm that operates in more than one country"],
  ["Foreign direct investment", "Investment by a firm in factories or offices abroad"],
  ["Supply chain", "The stages of production, often in different countries"],
  ["Trade openness", "Exports plus imports as a share of GDP"],
  ["Migration", "People moving from one country to another"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the stages in order: <b>a product made through a global supply chain</b>.", items: [
  "A firm designs a product in its home country",
  "Components are made in countries with skills and low costs",
  "The parts are shipped to a country where the product is assembled",
  "The finished product is exported to markets around the world",
  "Consumers in many countries buy it",
], done: "Different stages, different countries." });
''' + calc_js([
    ("Exports are $60bn and imports are $70bn in an economy with GDP of $260bn. Calculate trade openness (%).", 50, "(60 + 70) ÷ 260 × 100 = <b>50%</b>.", None, None),
    ("A country's exports rise from $80bn to $100bn. What is the percentage increase?", 25, "20 ÷ 80 × 100 = <b>25%</b>.", None, None),
    ("GDP is $500bn. Exports and imports together are $750bn. What is trade openness (%)?", 150, "750 ÷ 500 × 100 = <b>150%</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is globalisation?", ["A fall in world trade", "Increasing integration of the world's economies", "Protection of home industries", "Trade within one country"], 1, "Increasing integration."),
    ("Which is a feature of globalisation?", ["Fewer MNCs", "More international trade", "Fewer migrants", "More tariffs"], 1, "Trade, FDI, migration, technology."),
    ("A global supply chain means:", ["All production in one country", "Stages of production in different countries", "No exports", "Only primary products"], 1, "Different stages in different places."),
    ("Which measures how open an economy is?", ["GDP per head", "(Exports + imports) ÷ GDP", "Inflation", "Population"], 1, "Trade openness."),
    ("Foreign direct investment is:", ["Buying goods from abroad", "Firms investing in factories and offices abroad", "Government aid", "Tourism"], 1, "Capital invested abroad."),
]) + "\n" + cards_js([("Globalisation", "The increasing connection and integration of the world's economies."), ("Multinational company (MNC)", "A firm that operates in more than one country."), ("Foreign direct investment (FDI)", "Investment by firms in factories, offices or shops in other countries."), ("Supply chain", "The stages of production of a good, which may be in different countries."), ("Trade openness", "Exports plus imports as a percentage of GDP."), ("Migration", "People moving from one country to another."), ("Remittances", "Money sent home by migrants working abroad."), ("Offshoring", "Moving production to another country."), ("Global brand", "A brand sold and known worldwide.")]) + "labO(); \n"
explore = '''
  <h2>Lab 1 · How open is the economy?</h2>
  <p>Set exports, imports and GDP and see trade openness: (exports + imports) ÷ GDP.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Trade openness</small><strong id="oa1"></strong></div><div><small>Trade balance</small><strong id="oa2"></strong></div><div><small>Verdict</small><strong id="oa3"></strong></div></div><div class="verdict" id="oav"></div></div></div>
    <svg id="labO" viewBox="0 0 760 330" role="img" aria-label="Trade openness"></svg>
  </div>

  <h2>Lab 2 · Features of globalisation</h2>
  <p>Pick a feature to see what it means, an example, and its gains and risks.</p>
  <div class="card"><div class="row" id="ftBtns"></div><div id="ftOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "What is meant by globalisation?", "Increasing integration of economies through trade, investment, people and ideas.", "[K|Globalisation is the increasing connection and integration of the world's economies] [K|through growing international trade, investment, movement of people and spread of ideas and technology.]"),
    Q(2, "Identify", 2, "Identify two features of globalisation. (Oct/Nov 2024, P21)", "Trade, migration, ideas, technology, MNCs.", "[K|Increased international trade of goods and services (or more MNCs).] [K|Increased migration and movement of people (or sharing of ideas and technology).]"),
    Q(3, "Calculate", 2, "A country has exports of $60bn, imports of $70bn and GDP of $260bn. Calculate its trade openness.", "(Exports + imports) ÷ GDP × 100.", "[A|(60 + 70) ÷ 260 × 100 =] [A|50%.]"),
    Q(4, "Explain", 4, "Explain what is meant by a global supply chain, using an example.", "Stages of production in different countries; example; why.",
      "[K|A global supply chain is when different stages of making a product take place in different countries.] [A|For example, a phone may be designed in the USA, have chips made in South Korea, be assembled in China and sold worldwide.] [N|Each stage is done where it is cheapest or where skills are best, lowering costs.] [E|However, a problem in one country can disrupt the whole chain.]"),
)
tp = tips([
    ("Define it with 'increasing integration'.", "Of economies, through trade, investment, people and ideas."),
    ("Know the features.", "Trade, MNCs, FDI, supply chains, migration, technology, culture."),
    ("Trade openness = (X + M) ÷ GDP.", "Show working."),
    ("Globalisation can slow.", "It is not a one-way process."),
], cmds("Define", "Identify", "Calculate", "Explain"))
body = page(CL("6.2.1 Definition of globalisation"), "Definition of Globalisation", "What globalisation is, its main features and how to measure it. Syllabus 6.2.1.",
    learn=learn, watch=watch(("What globalisation involves", "stF"), ("A global supply chain", "stC"), ("Trade has grown faster than output", "stT")), explore=explore,
    practise=practise(("Feature of globalisation?", "cl1", "card"), ("Match the term", "m1", "card"), ("Order the supply chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("The smartphone", "A typical smartphone has parts from several countries, is assembled in Asia and sold worldwide. Apple, for example, designs in California and uses suppliers across many countries.", "A clear supply chain example."),
        rw("Global brands", "McDonald's, Coca-Cola and Toyota operate in dozens of countries, adapting products to local tastes.", "MNCs as a feature of globalisation."),
        rw("COVID-19 and supply chains", "In 2020 factory closures and shipping delays showed how a problem in one place can disrupt production elsewhere.", "A risk of global linkages."),
        rw("Remote work and services", "Firms in India and the Philippines provide customer service and IT support to clients abroad over the internet.", "Technology spreading globalisation to services.")),
    exam=ex, tips=tp)
write("gl1", body, js, "Definition of Globalisation", "ig-globalisation-definition")

# =========================================================== 6.2.2 Causes and consequences
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Globalisation is driven by <b>changes in trade restrictions</b>, <b>changes in transport costs</b>, <b>changes in communication costs</b> and the <b>movement of multinational companies (MNCs)</b>. If these changes reverse (higher tariffs, dearer shipping) globalisation can slow. Globalisation affects <b>international trade, competition, the environment, migration, income distribution and economic development</b>, with gains and losses for different groups.</p></div>

  <h2>Causes of changes in globalisation</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>How it increases (or reduces) globalisation</th></tr>
    <tr><td><b>Changes in trade restrictions</b></td><td>Lower tariffs and quotas, free trade agreements and the World Trade Organization make trade cheaper and easier. Higher restrictions (trade wars) slow globalisation</td></tr>
    <tr><td><b>Changes in transport costs</b></td><td>Container ships, bigger freighters, air freight and better ports cut the cost of moving goods, so more is traded and supply chains stretch across the world. Rising fuel costs raise them</td></tr>
    <tr><td><b>Changes in communication costs</b></td><td>The internet, mobile phones and video calls cut the cost of coordinating firms and selling abroad; online trade and services can cross borders instantly</td></tr>
    <tr><td><b>Movement of MNCs</b></td><td>MNCs set up production abroad (FDI), spread technology and create supply chains, increasing trade and investment</td></tr>
  </table></div>

  <h2>Effects of globalisation</h2>
  <div class="tw"><table class="t">
    <tr><th>Area</th><th>Possible positive effects</th><th>Possible negative effects</th></tr>
    <tr><td><b>International trade</b></td><td>More trade, specialisation, lower prices, more choice</td><td>Dependence on other countries; global shocks spread quickly</td></tr>
    <tr><td><b>Competition</b></td><td>More competition lowers prices and raises quality and innovation; consumers gain</td><td>Domestic firms that cannot compete close; jobs lost; some MNCs dominate markets</td></tr>
    <tr><td><b>The environment</b></td><td>Spread of green technology; some countries adopt higher standards</td><td>More transport emissions, pollution and resource depletion; production moves to places with weak regulations</td></tr>
    <tr><td><b>Migration</b></td><td>Workers fill skill shortages; migrants earn higher wages and send remittances; ideas spread</td><td>Brain drain from poorer countries; pressure on housing and services; wage pressure on some local workers</td></tr>
    <tr><td><b>Income distribution</b></td><td>Jobs and incomes rise in developing countries; poverty may fall</td><td>Skilled workers and owners gain more than low-skilled workers, so inequality within countries may widen; gains are uneven between countries</td></tr>
    <tr><td><b>Economic development</b></td><td>FDI, technology and export markets speed up growth and development</td><td>Dependence on a few exports or MNCs; exploitation; benefits may not reach the poor</td></tr>
  </table></div>

  <h2>Winners and losers</h2>
  <ul>
    <li><b>Winners:</b> consumers (choice and lower prices), exporters, skilled workers, MNCs, countries that attract investment.</li>
    <li><b>Losers:</b> workers in industries that cannot compete, small local firms, some low-income workers, the environment, countries left out of trade.</li>
  </ul>
  <p class="note">Because the effects differ by group and country, answers should usually weigh both sides and end with 'it depends on…'.</p>
'''
js = HEAD + COMMON + '''
const TR = ["Governments cut tariffs and quotas; join trade agreements", "Imports become cheaper and exports face fewer barriers", "Firms sell to bigger markets and source cheaper inputs", "More specialisation and international trade", "Supply chains spread across countries", "Globalisation increases"];
Lib.stepper($("#stR"), { w: 760, h: 400, label: "Lower trade restrictions", base: { n: 0 }, draw: mkChain(TR, "--accent"), steps: chainSteps(["Governments <b>cut tariffs and quotas</b> and join trade agreements.", "Imports become <b>cheaper</b> and exports face <b>fewer barriers</b>.", "Firms sell to <b>bigger markets</b> and source cheaper inputs.", "There is more <b>specialisation</b> and trade.", "<b>Supply chains</b> spread across countries.", "<b>Globalisation increases</b>. If restrictions rise instead, it slows."]) });
const TC = ["Container ships, big freighters and air freight cut shipping costs", "Internet and mobile networks cut the cost of communicating", "It is cheaper to move goods and coordinate production abroad", "Firms spread production across countries to cut costs", "More goods and services are traded; MNCs expand", "Globalisation increases"];
Lib.stepper($("#stC"), { w: 760, h: 400, label: "Lower transport and communication costs", base: { n: 0 }, draw: mkChain(TC, "--good"), steps: chainSteps(["<b>Container ships, bigger freighters and air freight</b> cut shipping costs.", "The <b>internet and mobile networks</b> cut the cost of communicating.", "It is <b>cheaper to move goods</b> and run production abroad.", "Firms <b>spread production</b> across countries to cut costs.", "More goods and services are <b>traded</b>; MNCs expand.", "<b>Globalisation increases</b>. Higher fuel costs or disruptions can reverse this."]) });
const IN = ["Globalisation raises demand for skilled workers and capital", "Skilled workers and owners see higher pay and profits", "Low-skilled workers face competition from cheaper labour abroad", "Their wages may stagnate or jobs may be lost", "The gap between rich and poor within the country may widen", "Evaluation: gains elsewhere may reduce poverty; policy can share gains"];
Lib.stepper($("#stI"), { w: 760, h: 400, label: "Globalisation and income distribution", base: { n: 0 }, draw: mkChain(IN, "--warn"), steps: chainSteps(["Globalisation raises demand for <b>skilled workers</b> and capital.", "Skilled workers and owners see <b>higher pay and profits</b>.", "<b>Low-skilled workers</b> face competition from cheaper labour abroad.", "Their <b>wages may stagnate</b> or jobs may be lost.", "The <b>gap between rich and poor</b> within the country may widen.", "<b>Evaluate:</b> jobs and incomes rose in developing countries, and taxes and education can share the gains."]) });

/* Lab 1: landed price */
function labL() {
  if (!$("#la") || !$("#lb")) return;
  const c = +$("#la").value, t = +$("#lb").value, price = (50 + c) * (1 + t / 100), qty = Math.max(0, 100 - price), base = (50 + 10) * 1.1, bq = 100 - base;
  $("#la1").textContent = "$" + money(price, 1); $("#la2").textContent = money(qty, 0); $("#la3").textContent = (qty - bq >= 0 ? "+" : "−") + money(Math.abs(qty - bq), 0);
  $("#lav").textContent = `A good costs $50 to make abroad. With transport costs of $${c} and a tariff of ${t}%, the landed price is ($50 + $${c}) × ${1 + t / 100} = $${money(price, 1)}. Consumers import ${money(qty, 0)} units. Lower transport costs or tariffs cut the price and raise trade: that is how they cause globalisation. Raising them does the reverse.`;
  const base0 = 290, k = 2.6; let o = SV.line(60, base0, 700, base0);
  [["Landed price ($)", price, "--warn", 1.5], ["Units imported", qty, "--accent", 2.6]].forEach(([n, v, cc, kk], i) => { const x = 160 + i * 250, h = v * kk; o += SV.rect(x, base0 - h, 150, h, "", { style: `fill:var(${cc})`, opacity: 0.85 }) + SV.text(x + 75, base0 - h - 8, money(v, i ? 0 : 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base0 + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labL").innerHTML = o;
}
Lib.slider($("#g1"), { id: "la", label: "Transport cost per unit", min: 0, max: 30, step: 2, value: 10, fmt: (v) => "$" + v, onInput: labL });
Lib.slider($("#g2"), { id: "lb", label: "Tariff on imports", min: 0, max: 40, step: 5, value: 10, fmt: (v) => v + "%", onInput: labL });
const EF = [
  { n: "International trade", p: "More trade, specialisation, lower prices and choice.", c: "Dependence on other countries; shocks spread quickly." },
  { n: "Competition", p: "Prices fall, quality and innovation rise; consumers gain.", c: "Weaker domestic firms close; jobs lost; large MNCs may dominate." },
  { n: "The environment", p: "Green technology spreads; higher standards in some countries.", c: "More transport emissions, pollution and resource use; production moves to weakly regulated countries." },
  { n: "Migration", p: "Skills reach where needed; migrants earn more and send remittances.", c: "Brain drain from poorer countries; pressure on housing and services." },
  { n: "Income distribution", p: "Jobs and incomes rise in developing countries; poverty may fall.", c: "Gap between skilled and unskilled, rich and poor may widen within countries." },
  { n: "Economic development", p: "FDI, technology and export markets raise growth and development.", c: "Dependence on a few exports or MNCs; benefits may not reach the poor." },
];
button_table("efBtns", "efOut", EF, 0, (p) => `<div class="tw"><table class="t"><tr><th>Possible positive effects</th><th>Possible negative effects</th></tr><tr><td>${p.p}</td><td>${p.c}</td></tr></table></div>`);
const RV = [
  { n: "Trade war: tariffs rise", e: "Imports dearer, trade falls; firms rethink supply chains.", t: "Slows globalisation" },
  { n: "Oil price spike", e: "Shipping costs rise; long supply chains become dearer.", t: "Slows globalisation" },
  { n: "Pandemic", e: "Borders and factories close; firms hold more local stocks.", t: "Slows globalisation" },
  { n: "New free trade agreement", e: "Tariffs fall; trade between members increases.", t: "Speeds globalisation" },
  { n: "Faster internet and cheaper video calls", e: "Easier to run offices and services abroad.", t: "Speeds globalisation" },
  { n: "A large MNC builds factories abroad", e: "Jobs, technology and exports grow in the host country.", t: "Speeds globalisation" },
];
button_table("rvBtns", "rvOut", RV, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect</th><th>Impact on globalisation</th></tr><tr><td>${p.e}</td><td><b>${p.t}</b></td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each <b>increase</b> or <b>reduce</b> globalisation?", buckets: [{ label: "Increases globalisation" }, { label: "Reduces globalisation" }], items: [
  { text: "Lower tariffs", b: 0 }, { text: "Cheaper shipping", b: 0 }, { text: "Cheaper internet and phone calls", b: 0 }, { text: "MNCs building factories abroad", b: 0 },
  { text: "Higher tariffs and quotas", b: 1 }, { text: "Rising fuel and shipping costs", b: 1 }, { text: "MNCs moving production back home", b: 1 }, { text: "Trade wars", b: 1 },
], done: "Four causes: restrictions, transport, communication, MNCs." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>positive</b> or <b>negative</b> effect of globalisation?", buckets: [{ label: "Positive" }, { label: "Negative" }], items: [
  { text: "Lower prices for consumers", b: 0 }, { text: "More jobs and FDI in developing countries", b: 0 }, { text: "Spread of technology and ideas", b: 0 }, { text: "More choice of goods", b: 0 },
  { text: "Job losses in industries facing imports", b: 1 }, { text: "More pollution from transport", b: 1 }, { text: "Wider gap between skilled and unskilled", b: 1 }, { text: "Brain drain from poorer countries", b: 1 },
], done: "Always weigh both sides." });
Lib.match($("#m1"), { prompt: "Match the cause to how it increases globalisation.", pairs: [
  ["Lower tariffs and quotas", "Imports cheaper and exports face fewer barriers"],
  ["Cheaper transport", "Cost of moving goods falls, so more is traded"],
  ["Cheaper communication", "Easier to coordinate production and sell abroad"],
  ["MNCs moving abroad", "FDI, technology and supply chains spread"],
  ["Trade agreements", "Countries agree to cut barriers"],
  ["Container shipping", "Goods moved cheaply in standard boxes"],
], done: "Link each cause to the effect." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how cheaper transport increases trade</b>.", items: [
  "Shipping and air freight costs fall",
  "The cost of getting goods to foreign markets falls",
  "Imports and exports become cheaper",
  "Firms sell more abroad and buy more inputs abroad",
  "International trade rises: globalisation increases",
], done: "A cause chain." });
''' + calc_js([
    ("A good costs $40 to make and $10 to ship. A 20% tariff is charged on the total. What is the landed price ($)?", 60, "(40 + 10) × 1.2 = <b>$60</b>.", None, None),
    ("Shipping costs fall from $10 to $4 on a good that costs $40. By what percentage does the shipped price fall (1 d.p.)?", 12, "From $50 to $44: 6 ÷ 50 × 100 = <b>12%</b>.", None, None),
    ("A firm's exports to a market rise from 200 to 260 units after tariffs are cut. By what percentage did exports rise?", 30, "60 ÷ 200 × 100 = <b>30%</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which is a cause of globalisation?", ["Higher tariffs", "Lower transport costs", "Higher shipping costs", "Fewer MNCs"], 1, "Cheaper movement of goods."),
    ("Globalisation is most likely to cause:", ["Less competition", "More competition between firms", "Fewer exports", "Less migration"], 1, "Firms face foreign rivals."),
    ("Which is a possible negative effect of globalisation on the environment?", ["More green technology", "More transport pollution", "Fewer emissions", "Less resource use"], 1, "More shipping and production."),
    ("Which could widen income inequality within a country?", ["Falling demand for skilled workers", "Greater competition for low-skilled workers from abroad", "A rise in the minimum wage", "More tax on the rich"], 1, "Unskilled wages may stagnate."),
    ("An increase in tariffs would most likely:", ["Speed up globalisation", "Slow globalisation", "Reduce all prices", "Increase migration"], 1, "Trade becomes dearer."),
]) + "\n" + cards_js([("Trade restrictions", "Measures such as tariffs and quotas that limit trade."), ("Transport costs", "The cost of moving goods between countries."), ("Communication costs", "The cost of sending information between countries."), ("Brain drain", "The emigration of skilled and educated workers."), ("Remittances", "Money sent home by migrants working abroad."), ("Income distribution", "How a country's income is shared among its people."), ("Competition", "Rivalry between firms for customers."), ("Trade agreement", "A deal between countries to reduce barriers to trade."), ("World Trade Organization (WTO)", "An organisation that sets rules for international trade and settles disputes.")]) + "labL(); \n"
explore = '''
  <h2>Lab 1 · Cheaper transport and lower tariffs</h2>
  <p>A good costs $50 to make abroad. Change transport costs and the tariff and see the price and the quantity imported. Cutting either speeds globalisation.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Landed price</small><strong id="la1"></strong></div><div><small>Units imported</small><strong id="la2"></strong></div><div><small>Change from base</small><strong id="la3"></strong></div></div><div class="verdict" id="lav"></div></div></div>
    <svg id="labL" viewBox="0 0 760 330" role="img" aria-label="Landed price and quantity imported"></svg>
  </div>

  <h2>Lab 2 · Effects of globalisation</h2>
  <p>Pick an area to see possible positive and negative effects.</p>
  <div class="card"><div class="row" id="efBtns"></div><div id="efOut"></div></div>

  <h2>Lab 3 · Speeding up or slowing down?</h2>
  <p>Pick an event to see whether it speeds up or slows globalisation.</p>
  <div class="card"><div class="row" id="rvBtns"></div><div id="rvOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 2, "Explain one cause of globalisation. (Feb/Mar 2021, P22)", "One mark for the cause, one for the explanation: transport costs, communication costs, trade barriers, MNCs.", "[K|A fall in transport costs,] [N|which reduces the cost of exporting and importing, so international trade increases.]"),
    Q(2, "Explain", 4, "Explain two causes of globalisation.", "Two different causes, each developed.",
      "[K|Lower trade restrictions are one cause.] [N|Cuts in tariffs and quotas, and trade agreements, make imports cheaper and exports easier, so trade increases.] [K|Improvements in communication are another.] [N|The internet and mobile phones allow firms to coordinate production and sell to customers in other countries at low cost.]"),
    Q(3, "Analyse", 6, "Analyse how globalisation could affect income distribution within a country.", "Skilled gain, low-skilled lose, owners gain; but jobs in developing countries; policy.",
      "[K|Globalisation increases demand for skilled workers and for capital.] [N|Skilled workers and owners of firms may see higher pay and profits.] [N|Low-skilled workers face competition from cheaper labour abroad, so their wages may stagnate or they could lose jobs.] [N|The gap between rich and poor within the country may therefore widen.] [E|However, globalisation can create jobs and raise incomes in developing countries, reducing poverty there, and governments can use taxes and education to share the gains.]", key=True),
    Q(4, "Analyse", 6, "Analyse how globalisation could affect the environment.", "Negative: transport, production, resource use, weak regulations. Positive: technology, standards.",
      "[K|Globalisation increases trade and production.] [N|More shipping and air freight raises emissions, and greater output uses more resources and creates more pollution.] [N|Firms may move production to countries with weaker environmental rules, increasing pollution there.] [N|However, MNCs can spread cleaner technology, and consumers and governments may demand higher standards.] [E|Overall, the effect depends on regulation and technology.]", key=True),
    Q(5, "Discuss", 8, "Discuss whether or not globalisation benefits developing countries.", "For: FDI, jobs, technology, markets, growth. Against: exploitation, dependence, competition, environment, inequality.",
      "[K|Globalisation is the increasing integration of economies through trade, investment and migration.] [N|It could benefit developing countries by bringing foreign investment, jobs and technology and giving access to large export markets, which may raise growth and reduce poverty.] [N|Consumers may benefit from cheaper and more varied goods.] [E|These gains are larger where governments invest in education and infrastructure.] [N|However, local firms may be unable to compete with large MNCs, workers may be paid low wages in poor conditions, and countries may become dependent on a few exports and vulnerable to global shocks.] [N|Gains may go mainly to the better off, widening inequality, and production may harm the environment.] [E|Overall, globalisation is likely to benefit developing countries that can attract investment and add value, but the benefits are uneven and depend on policy.]", key=True),
)
tp = tips([
    ("Four causes:", "trade restrictions, transport costs, communication costs, MNC movement."),
    ("Six effects:", "trade, competition, environment, migration, income distribution, development."),
    ("Weigh both sides.", "Positive and negative for each area."),
    ("Say who gains and who loses.", "Skilled and unskilled, rich and poor, countries."),
    ("It can reverse.", "Higher tariffs or shipping costs slow globalisation."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("6.2.2 Causes and consequences of changes in globalisation"), "Causes and Consequences of Changes in Globalisation", "What drives globalisation (trade restrictions, transport and communication costs, MNCs) and its effects on trade, competition, the environment, migration, income distribution and development. Syllabus 6.2.2.",
    learn=learn, watch=watch(("Lower trade restrictions", "stR"), ("Lower transport and communication costs", "stC"), ("Globalisation and income distribution", "stI")), explore=explore,
    practise=practise(("Increases or reduces globalisation?", "cl1", "card"), ("Positive or negative?", "cl2", "card"), ("Match the cause", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Container shipping", "The standard shipping container, introduced in the 1950s and 1960s, cut the cost and time of loading goods and made long-distance trade much cheaper.", "Lower transport costs."),
        rw("China joins the WTO", "China joined the World Trade Organization in 2001. Its exports boomed, lowering prices for consumers worldwide, but some manufacturing jobs in other countries were lost.", "Trade restrictions falling; winners and losers."),
        rw("US-China trade war", "From 2018 the US and China raised tariffs on each other's goods, raising prices and prompting firms to move some production elsewhere.", "Higher restrictions slowing globalisation."),
        rw("The internet and services", "Cheap communication allows UK banks to run call centres in India and firms to hire software developers anywhere.", "Communication costs and globalisation of services.")),
    exam=ex, tips=tp)
write("gl2", body, js, "Causes and Consequences of Changes in Globalisation", "ig-globalisation-causes")

# =========================================================== 6.2.3 MNCs
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <span class="kw">multinational company (MNC)</span> is a firm that operates (produces or sells) in more than one country. Its head office is in its <b>home country</b>; its factories, shops and offices abroad are in <b>host countries</b>. MNCs bring jobs, investment and technology to host countries but may also send profits abroad and out-compete local firms. Home countries gain profits and tax revenue but may lose jobs when production moves abroad.</p></div>

  <h2>Why MNCs locate abroad</h2>
  <ul>
    <li><b>Lower costs:</b> cheaper labour, land, raw materials; lower taxes (a 'tax haven' may have low or no corporation tax).</li>
    <li><b>Access to markets:</b> large or growing consumer markets; to <b>avoid import tariffs</b> by producing inside the country.</li>
    <li><b>Skilled workers</b> and good <b>infrastructure</b> (roads, ports, power, internet).</li>
    <li><b>Natural resources</b> close to the source.</li>
    <li><b>Political stability</b>, government incentives and grants.</li>
    <li>Spreading risk across several countries.</li>
  </ul>
  <p>Few MNCs may choose a region with <b>poor infrastructure, political instability, corruption, a small market, a shortage of skills or high taxes</b>.</p>

  <h2>Advantages and disadvantages for host countries</h2>
  <div class="grid2">
    <div class="card"><h3>Advantages</h3><ul><li><b>Jobs</b> and higher wages; fewer unemployed</li><li><b>Investment</b> in capital and infrastructure (FDI)</li><li><b>Technology and skills</b> transferred through training</li><li><b>Tax revenue</b> for the government</li><li><b>Exports</b> may rise, improving the current account; more choice, competition and lower prices</li><li>Higher output and productivity, economic growth; may reduce poverty</li></ul></div>
    <div class="card"><h3>Disadvantages</h3><ul><li><b>Profits sent back</b> to the home country</li><li>Local firms may be <b>driven out</b> by competition</li><li>Low wages, poor working conditions or exploitation of workers</li><li><b>Pollution</b> and depletion of resources</li><li><b>Tax avoidance</b>; MNCs may move away when costs rise ('footloose'), leaving unemployment</li><li>Dependence on the MNC; best-paid jobs may stay at head office</li></ul></div>
  </div>

  <h2>Advantages and disadvantages for home countries</h2>
  <div class="grid2">
    <div class="card"><h3>Advantages</h3><ul><li><b>Profits returned</b> raise income, tax revenue and the current account</li><li>Lower-cost production abroad can mean <b>lower prices</b> at home</li><li>Head-office and research jobs</li><li>Bigger markets and higher revenue for the firm</li></ul></div>
    <div class="card"><h3>Disadvantages</h3><ul><li><b>Jobs lost</b> at home when production moves abroad</li><li>Investment goes abroad instead of at home</li><li>Possible tax avoidance by moving profits abroad</li><li>Less control over standards in other countries; reputation risk</li></ul></div>
  </div>

  <h2>Do MNCs reduce poverty?</h2>
  <p>They could, by creating jobs and raising wages, training workers and paying taxes that fund services. They may not if wages stay very low, profits leave, or the benefits go to a small group.</p>
'''
js = HEAD + COMMON + '''
function mncChart(s) {
  let o = ""; const box = (x, t1, t2, c) => SV.rect(x, 70, 240, 150, "", { rx: 12, style: `fill:var(${c});fill-opacity:0.15;stroke:var(${c});stroke-width:2.5` }) + SV.text(x + 120, 105, t1, "lbl bd", { "text-anchor": "middle", style: "font-size:17px" }) + SV.text(x + 120, 130, t2, "sm", { "text-anchor": "middle" });
  o += box(40, "Home country", "Head office, research", "--accent") + box(480, "Host country", "Factories, shops, workers", "--good");
  const arr = (y, label, dir, op) => `<g opacity="${op}">` + SV.line(284, y, 476, y, "ax", { style: "stroke-width:3" }) + SV.arrowHead(dir === "r" ? 478 : 282, y, dir, "dot1") + SV.text(380, y - 8, label, "sm bd", { "text-anchor": "middle" }) + "</g>";
  o += arr(110, "Investment, technology", "r", clamp(s.n, 0, 1)) + arr(150, "Profits", "l", clamp(s.n - 1, 0, 1)) + arr(190, "Goods and services (exports)", "l", clamp(s.n - 2, 0, 1));
  o += `<g opacity="${clamp(s.n - 3, 0, 1)}">` + SV.text(600, 250, "Jobs, wages, skills, taxes", "lbl bd t3", { "text-anchor": "middle" }) + "</g>" + `<g opacity="${clamp(s.n - 4, 0, 1)}">` + SV.text(160, 250, "Profits, lower prices, head-office jobs", "lbl bd t3", { "text-anchor": "middle" }) + "</g>";
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 300, label: "How an MNC links two countries", base: { n: 0 }, draw: mncChart, steps: [
  { cap: "An MNC has its <b>head office in its home country</b> and factories or shops in <b>host countries</b>.", s: { n: 0.2 } },
  { cap: "It sends <b>investment and technology</b> to the host country (foreign direct investment).", s: { n: 1 } },
  { cap: "<b>Profits</b> flow back to the home country, which is a cost to the host.", s: { n: 2 } },
  { cap: "Goods and services made in the host country may be <b>exported</b> to the home country and elsewhere.", s: { n: 3 } },
  { cap: "The <b>host country</b> gains jobs, wages, skills and tax revenue.", s: { n: 4 } },
  { cap: "The <b>home country</b> gains profits, lower prices and head-office jobs, but may lose production jobs.", s: { n: 5 } },
] });
const HB = ["An MNC sets up a factory in a host country", "It hires local workers and pays wages", "Workers gain skills; the MNC buys from local suppliers", "Output, exports and tax revenue rise", "Incomes rise: spending increases and poverty may fall", "Evaluation: profits leave, wages may be low, local firms may close"];
Lib.stepper($("#stH"), { w: 760, h: 400, label: "How an MNC could reduce poverty in a host country", base: { n: 0 }, draw: mkChain(HB, "--good"), steps: chainSteps(["An MNC <b>sets up a factory</b> in a host country.", "It <b>hires local workers</b> and pays wages.", "Workers gain <b>skills</b>; the MNC buys from <b>local suppliers</b>.", "<b>Output, exports and tax revenue</b> rise.", "<b>Incomes rise</b>, spending increases and <b>poverty may fall</b>.", "<b>Evaluate:</b> profits leave, wages may be low and local firms may close."]) });
const HC = ["Costs rise in the host country (wages, taxes)", "The MNC moves production to another country", "The factory closes and workers lose their jobs", "Local suppliers lose orders", "Unemployment and poverty rise in the area", "Evaluation: the host country is dependent on 'footloose' firms"];
Lib.stepper($("#stC"), { w: 760, h: 400, label: "Why an MNC may leave a host country", base: { n: 0 }, draw: mkChain(HC, "--bad"), steps: chainSteps(["<b>Costs rise</b> in the host country: wages, taxes, rents.", "The MNC <b>moves production</b> to another country.", "The factory <b>closes</b> and workers lose their jobs.", "<b>Local suppliers</b> lose orders.", "<b>Unemployment and poverty</b> rise in the area.", "<b>Evaluate:</b> dependence on 'footloose' MNCs is a risk for host countries."]) });

/* Lab 1: location */
const CAND = [["Country X", [9, 3, 4, 8, 4, 3], "Low wages and low taxes, but poor skills and infrastructure"], ["Country Y", [5, 7, 7, 6, 7, 7], "Balanced: reasonable costs, skills, market and stability"], ["Country Z", [2, 9, 9, 3, 9, 9], "High costs and taxes, but skilled, rich market and stable"]];
const CRIT = ["Low wages", "Skilled workers", "Market size", "Low taxes", "Stability", "Infrastructure"];
function labM() {
  const ids = ["ma", "mb", "mc", "md", "me", "mf"]; if (!ids.every((i) => $("#" + i))) return;
  const w = ids.map((i) => +$("#" + i).value), tot = w.reduce((a, b) => a + b, 0) || 1, sc = CAND.map(([n, v]) => v.reduce((a, x, i) => a + x * w[i], 0) / tot), best = sc.indexOf(Math.max(...sc));
  $("#ma1").textContent = money(sc[0], 1); $("#ma2").textContent = money(sc[1], 1); $("#ma3").textContent = money(sc[2], 1);
  $("#mav").textContent = `Weighted scores: X ${money(sc[0], 1)}, Y ${money(sc[1], 1)}, Z ${money(sc[2], 1)} out of 10. On these priorities ${CAND[best][0]} is the most attractive location (${CAND[best][2].toLowerCase()}). An MNC cutting costs would weigh wages and taxes; one seeking a market would weigh market size and skills.`;
  const base = 290; let o = SV.line(60, base, 700, base);
  CAND.forEach(([n], i) => { const x = 130 + i * 190, h = sc[i] * 22; o += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${i === best ? "--good" : "--muted"})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, money(sc[i], 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labM").innerHTML = o + SV.text(60, 24, "Weighted attractiveness to the MNC (out of 10)", "sm");
}
[["ma", "g1", "Importance of low wages", 8], ["mb", "g2", "Importance of skilled workers", 4], ["mc", "g3", "Importance of market size", 4], ["md", "g4", "Importance of low taxes", 6], ["me", "g5", "Importance of stability", 5], ["mf", "g6", "Importance of infrastructure", 5]].forEach(([id, g, l, v]) => Lib.slider($("#" + g), { id, label: l, min: 0, max: 10, step: 1, value: v, fmt: (x) => x, onInput: labM }));
const HH = [
  { n: "Host country: gains", t: "Jobs and wages; investment; technology and skills; tax revenue; exports; more choice and lower prices.", e: "Foreign car plants creating thousands of jobs." },
  { n: "Host country: costs", t: "Profits sent abroad; local firms driven out; low pay and poor conditions; pollution; footloose firms may leave.", e: "Garment factories criticised for conditions." },
  { n: "Home country: gains", t: "Profits and tax revenue; lower prices; head office and research jobs; larger markets.", e: "Profits from overseas operations returning to the headquarters country." },
  { n: "Home country: costs", t: "Production jobs lost at home; investment goes abroad; tax avoidance.", e: "Factory closures after production moves abroad." },
];
button_table("hhBtns", "hhOut", HH, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effects</th><th>Example</th></tr><tr><td>${p.t}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>benefit</b> or a <b>cost</b> of an MNC for the <b>host</b> country?", buckets: [{ label: "Benefit" }, { label: "Cost" }], items: [
  { text: "Creates jobs and wages", b: 0 }, { text: "Brings new technology and skills", b: 0 }, { text: "Pays corporation tax", b: 0 }, { text: "Raises exports", b: 0 },
  { text: "Profits are sent abroad", b: 1 }, { text: "Local firms cannot compete", b: 1 }, { text: "Pollution and resource depletion", b: 1 }, { text: "May leave when costs rise", b: 1 },
], done: "Always give both sides for the host country." });
Lib.classify($("#cl2"), { prompt: "Is each effect most relevant to the <b>host</b> country or the <b>home</b> country of an MNC?", buckets: [{ label: "Host country" }, { label: "Home country" }], items: [
  { text: "Jobs created in new factories", b: 0 }, { text: "Local suppliers gain orders", b: 0 }, { text: "Local firms driven out of business", b: 0 },
  { text: "Profits returned to shareholders", b: 1 }, { text: "Production jobs lost when factories move abroad", b: 1 }, { text: "Head-office jobs grow", b: 1 },
], done: "Do not confuse host and home countries." });
Lib.classify($("#cl3"), { prompt: "Would each make a country <b>more</b> or <b>less</b> attractive to an MNC?", buckets: [{ label: "More attractive" }, { label: "Less attractive" }], items: [
  { text: "Low corporation tax", b: 0 }, { text: "Skilled, educated workers", b: 0 }, { text: "Large and growing market", b: 0 }, { text: "Good roads, ports and internet", b: 0 },
  { text: "Political instability", b: 1 }, { text: "Corruption and poor law enforcement", b: 1 }, { text: "Poor infrastructure", b: 1 }, { text: "Very small market and few skills", b: 1 },
], done: "Costs, market, skills, infrastructure, stability." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Multinational company", "A firm that operates in more than one country"],
  ["Home country", "The country where an MNC has its head office"],
  ["Host country", "A country where an MNC has factories or shops"],
  ["Foreign direct investment", "Investment by a firm in another country"],
  ["Tax haven", "A country with very low or no taxes on firms"],
  ["Footloose firm", "A firm that can easily move production elsewhere"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how an MNC could help a host country grow</b>.", items: [
  "The MNC invests in a factory in the host country",
  "It hires local workers and trains them",
  "Output and exports rise",
  "Government tax revenue and incomes rise",
  "Spending and living standards increase",
], done: "A benefit chain." });
''' + calc_js([
    ("An MNC employs 5,000 workers in a host country at an average wage of $6,000 a year. What is the total wage bill ($m)?", 30, "5,000 × 6,000 = <b>$30m</b>.", None, None),
    ("An MNC's profit in a host country is $50m and it pays 20% corporation tax. How much tax does the host government receive ($m)?", 10, "20% × 50 = <b>$10m</b>.", None, None),
    ("The MNC sends 70% of its $50m profit to the home country. How much is sent ($m)?", 35, "70% × 50 = <b>$35m</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is a multinational company?", ["A firm that only sells at home", "A firm that operates in more than one country", "A government firm", "A small firm"], 1, "Operates across borders."),
    ("A benefit of an MNC to a host country is:", ["Profits sent abroad", "Jobs and investment", "Local firms closing", "Pollution"], 1, "Creating employment."),
    ("A disadvantage of an MNC to a host country is:", ["Technology transfer", "Higher tax revenue", "Local firms may be driven out", "More exports"], 2, "Competition from large firms."),
    ("Which would attract an MNC to a country?", ["High taxes and instability", "Skilled workers and a large market", "Poor infrastructure", "Corruption"], 1, "Skills and demand."),
    ("A benefit to the home country of an MNC is:", ["Production jobs lost", "Profits returned and tax revenue", "Investment abroad only", "Local pollution"], 1, "Profits flow back."),
]) + "\n" + cards_js([("Multinational company (MNC)", "A firm that operates in more than one country."), ("Home country", "The country where an MNC has its head office."), ("Host country", "A country in which an MNC operates factories, shops or offices."), ("Foreign direct investment (FDI)", "Investment by a firm in capital in another country."), ("Technology transfer", "The spread of technology and skills from an MNC to the host country."), ("Tax haven", "A country with low or no taxes that attracts firms."), ("Footloose", "Able to move production easily to other places."), ("Profit repatriation", "Sending profits back to the home country."), ("Infrastructure", "The roads, ports, energy and communications networks an economy uses.")]) + "labM(); \n"
explore = '''
  <h2>Lab 1 · Where should the MNC locate?</h2>
  <p>Set how important each factor is to an MNC. Three countries are scored on them, and the best location changes with the MNC's priorities.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div><div id="g5"></div><div id="g6"></div></div>
    <div><div class="readout"><div><small>Country X (low cost)</small><strong id="ma1"></strong></div><div><small>Country Y (balanced)</small><strong id="ma2"></strong></div><div><small>Country Z (high skill, big market)</small><strong id="ma3"></strong></div></div><div class="verdict" id="mav"></div></div></div>
    <svg id="labM" viewBox="0 0 760 330" role="img" aria-label="Weighted attractiveness of three countries"></svg>
    <p class="note">Illustrative scores. X: low wages 9, skills 3, market 4, low taxes 8, stability 4, infrastructure 3. Y: 5, 7, 7, 6, 7, 7. Z: 2, 9, 9, 3, 9, 9.</p>
  </div>

  <h2>Lab 2 · Host and home country effects</h2>
  <p>Pick a group to see the possible effects.</p>
  <div class="card"><div class="row" id="hhBtns"></div><div id="hhOut"></div></div>
'''
ex = exam(
    Q(1, "Identify", 2, "State two reasons why a foreign MNC may want to operate in Bermuda. (Feb/Mar 2022, P22)", "Low taxes, high GDP per head (market), tariffs, skilled workers, low inflation.", "[K|Low or no corporation tax (a tax haven).] [K|A high GDP per head (strong market) or skilled, educated workers.]"),
    Q(2, "Explain", 4, "Explain two benefits that an MNC can bring to its host country. (Feb/Mar 2023, P22)", "Jobs, investment, technology, tax revenue, exports; each with a link.",
      "[K|An MNC creates jobs.] [N|It employs local workers and pays wages, so unemployment falls and incomes and spending rise.] [K|It brings investment and technology.] [N|Workers learn new skills and local firms may copy new methods, raising productivity and growth.]"),
    Q(3, "Explain", 4, "Explain two benefits of MNCs to their home countries. (Oct/Nov 2022, P23)", "Profits returned, tax revenue, lower prices, head-office jobs. Make sure it is the home country.",
      "[K|Profits earned abroad can be returned to the home country,] [N|raising income and tax revenue and improving the current account.] [K|Producing abroad at lower cost may reduce the price of goods at home,] [N|so home consumers could pay less.]"),
    Q(4, "Analyse", 6, "Analyse why few MNCs may choose to locate in a particular region. (May/June 2022, P23)", "Poor infrastructure, instability, small market, skills shortage, taxes, corruption.",
      "[K|MNCs choose locations that give low costs and access to markets.] [N|A region with poor infrastructure, such as roads and power, makes production and transport costly.] [N|Political instability or corruption increases the risk of losing investment.] [N|A small market or low incomes means few customers, and a shortage of skilled workers raises training costs.] [N|High taxes or tariffs on imports of inputs reduce profit.] [E|Governments could attract MNCs with incentives and by investing in education and infrastructure.]", key=True),
    Q(5, "Analyse", 6, "Analyse how a MNC could reduce poverty in a host country. (May/June 2022, P22)", "Jobs and wages, tax revenue to fund services, training, local suppliers, exports. Add a limit.",
      "[K|An MNC creates jobs and pays wages.] [N|Households that were unemployed or in low-paid work earn more, so they can afford basic necessities.] [N|The MNC pays tax, giving the government revenue to spend on education and healthcare.] [N|It trains workers and buys from local suppliers, creating more jobs and higher productivity.] [E|However, if wages are very low or profits leave the country, the effect on poverty may be small.]", key=True),
    Q(6, "Discuss", 8, "Discuss whether or not MNCs always benefit their host countries. (May/June 2020, P23)", "'Always' invites 'not always'. Benefits and costs; depends on wages, tax, local firms.",
      "[K|An MNC operates in several countries; the host country is where it has factories or shops.] [N|MNCs could benefit host countries by creating jobs, bringing investment and technology, paying taxes and raising exports.] [N|Competition may also lower prices and improve quality for consumers.] [E|These benefits are greater when MNCs buy from local suppliers and train workers.] [N|However, host countries may lose out if profits are sent abroad, workers receive low wages in poor conditions, local firms cannot compete and close, or MNCs pollute.] [N|MNCs can also move away when costs rise, leaving unemployment.] [E|Overall, MNCs usually benefit host countries but not always: it depends on how much tax they pay, whether profits are reinvested and how well the government regulates them.]", key=True),
    Q(7, "Discuss", 8, "Discuss whether or not MNCs increase production and productivity in their host countries. (May/June 2020, P21)", "For: investment, technology, skills, competition. Against: local firms close, profits leave, low-skilled jobs, may import inputs.",
      "[K|Production is the amount of output and productivity is output per worker.] [N|MNCs can raise production by investing in factories and machinery and employing more workers, and their technology and training could raise workers' skills and productivity.] [N|Competition from MNCs may force local firms to become more efficient.] [E|This is more likely if skills and technology spread to local firms.] [N|However, MNCs could drive local firms out of business, reducing local production, and may use mainly imported inputs and low-skill jobs, so productivity gains may be limited.] [E|Overall, MNCs are likely to increase production, but productivity gains depend on training, links with local firms and the type of work.]", key=True),
    Q(8, "Discuss", 6, "Discuss whether or not foreign MNCs reduce poverty in their host countries. (Feb/Mar 2025, P22)", "Jobs and wages; tax; training; against: low wages; profits sent abroad; displaced local firms.",
      "[K|Poverty is when people cannot afford basic necessities or take part in society.] [N|MNCs may reduce poverty by creating jobs and paying higher wages than local firms, so households can afford more, and by paying taxes used for services.] [N|They can train workers and give local suppliers orders.] [E|The effect is larger where MNCs employ many local people at fair wages.] [N|However, wages may be low and conditions poor, profits may be sent abroad, and MNCs may close local firms, raising unemployment.] [E|Overall, MNCs are likely to reduce poverty if they employ locals and the government taxes and regulates them well, but the benefit could be small if most gains leave the country.]", key=True),
)
tp = tips([
    ("Host or home?", "Check which country the question asks about: a common error."),
    ("Benefits: jobs, investment, technology, tax, exports.", "Link each with a result."),
    ("Costs: profits abroad, local firms, wages, pollution, footloose.", "Give at least one."),
    ("Why MNCs locate: costs, markets, skills, stability.", "And avoid tariffs by producing inside."),
    ("'Always' means 'not always'.", "It depends on tax, wages and local links."),
], cmds("Identify", "Explain", "Analyse", "Discuss"))
body = page(CL("6.2.3 Role of multinational companies (MNCs)"), "The Role of Multinational Companies", "What MNCs are, why they locate abroad, and their advantages and disadvantages for host and home countries. Syllabus 6.2.3.",
    learn=learn, watch=watch(("How an MNC links two countries", "stM"), ("How an MNC could reduce poverty in a host country", "stH"), ("Why an MNC may leave a host country", "stC")), explore=explore,
    practise=practise(("Benefit or cost for the host?", "cl1", "card"), ("Host or home?", "cl2", "card"), ("Attractive to an MNC?", "cl3", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Toyota in the UK", "Toyota opened car plants in the UK in the 1990s, creating thousands of jobs and exports, with spending with local suppliers.", "Host country benefits."),
        rw("Garment factories in Bangladesh", "Global fashion brands source clothes from factories in Bangladesh, creating millions of jobs, but accidents such as the Rana Plaza collapse in 2013 showed risks of poor working conditions.", "Benefits and costs of MNC supply chains."),
        rw("Bermuda", "A past paper asks why a foreign MNC may want to operate in Bermuda: no corporation tax, high incomes and skilled workers are among the reasons.", "Why MNCs choose a location."),
        rw("Footloose manufacturing", "Some firms moved production from Mexico to cheaper locations in Asia, leaving workers unemployed.", "A risk for host countries."),
        rw("Tax avoidance", "Some large MNCs have been criticised for shifting profits to low-tax countries, reducing tax payments in countries where they earn their revenue.", "A cost for host countries.")),
    exam=ex, tips=tp)
write("gl3", body, js, "The Role of Multinational Companies", "ig-mncs")
