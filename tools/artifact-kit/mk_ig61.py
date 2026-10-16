"""Builds the two IGCSE Economics 6.1 Specialisation and free trade reviews (6.1.1, 6.1.2), written from scratch.
Run: python3 tools/artifact-kit/mk_ig61.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

# =========================================================== 6.1.1 Specialisation
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Specialisation by country</span> is when a country concentrates its resources on producing a limited range of goods and services, usually the ones it can make <b>best or at lowest cost</b>, and trades them for the other things it needs. The basis for specialisation is <b>best resource allocation</b> (using land, labour, capital and skills where they are most productive) and <b>low-cost production</b>. Specialisation can raise output and income, but it makes a country <b>dependent</b> on a few products and on trade.</p></div>

  <h2>Why countries specialise in particular goods</h2>
  <div class="tw"><table class="t">
    <tr><th>Basis</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Natural resources and climate</b></td><td>Land, minerals, oil, climate and location suit certain products</td><td>Saudi Arabia: oil. Brazil: coffee. Chile: copper</td></tr>
    <tr><td><b>Labour: size, cost and skills</b></td><td>Plentiful low-cost labour suits labour-intensive goods; skilled workers suit complex goods and services</td><td>Bangladesh: clothing. India: IT services. Switzerland: watches and finance</td></tr>
    <tr><td><b>Capital and technology</b></td><td>Countries with machinery, infrastructure and technology make capital-intensive goods</td><td>Germany: machinery and cars. South Korea: electronics</td></tr>
    <tr><td><b>Skills and experience built up over time</b></td><td>"Practice makes perfect": workers and firms become more productive</td><td>Established industry clusters, such as financial services in London</td></tr>
    <tr><td><b>Economies of scale</b></td><td>Large output lowers average costs</td><td>Large-scale car or aircraft production</td></tr>
  </table></div>
  <div class="card"><h3>Low-cost production and opportunity cost</h3>
    <p>A country should specialise in the goods whose <b>opportunity cost</b> (what it gives up to make them) is lowest. Suppose country A can produce either 100 tonnes of wheat or 50 cars, and country B either 60 tonnes of wheat or 60 cars. A gives up 1 car for 2 tonnes of wheat; B gives up 1 car for 1 tonne. A is relatively better at wheat and B at cars. If each splits resources evenly they make 80 tonnes of wheat and 55 cars in total. If A makes only wheat and B only cars, they make 100 tonnes of wheat and 60 cars: <b>more of both</b>, which they can then trade.</p></div>

  <h2>Advantages of specialisation</h2>
  <ul>
    <li><b>Lower costs and prices:</b> workers gain skills (practice makes perfect), better use of machinery, economies of scale.</li>
    <li><b>Higher output and quality</b>, and less waste.</li>
    <li><b>Efficient use of resources</b>, so more total output from the same inputs.</li>
    <li><b>Exports earn income</b> and create jobs; firms gain a good reputation and higher demand; easier to mechanise and improve technology.</li>
    <li>Consumers can buy a <b>wider choice</b> of goods through trade, often cheaper.</li>
  </ul>
  <h2>Disadvantages of specialisation</h2>
  <ul>
    <li><b>Over-dependence on a few products:</b> if demand or the price falls (or a harvest fails), incomes, jobs and export earnings fall sharply.</li>
    <li><b>Vulnerable to other countries and to world prices</b> and to shocks such as wars, disasters and trade restrictions.</li>
    <li><b>Dependence on imports</b> of everything not produced: supplies can be cut off.</li>
    <li><b>Structural unemployment</b> if the main industry declines.</li>
    <li><b>Resources used up</b> or environmental damage from one industry; loss of traditional skills.</li>
  </ul>
  <p>The risk is lower if a country specialises in <b>several</b> goods or in goods with <b>strong, stable demand</b>, and can switch if conditions change.</p>

  <h2>Why a country may change its specialisation</h2>
  <ul>
    <li><b>Resources run out</b> or new ones are found (oil, minerals).</li>
    <li><b>Technology and education</b> change what the country can make well (a farming economy moves into manufacturing or services).</li>
    <li><b>Costs change:</b> rising wages make labour-intensive goods less competitive.</li>
    <li><b>Demand and world prices change</b>, or competitors with lower costs appear.</li>
    <li><b>Government policy</b>, investment in infrastructure, or changes in exchange rates and trade agreements.</li>
  </ul>
'''
js = HEAD + COMMON + '''
function spChart(s) {
  const base = 320, k = 2.6; let o = SV.line(60, base, 710, base) + SV.text(60, 28, "Total output of the two countries together", "sm");
  const grp = (x, label, parts, tot, op) => { let y = base, g = `<g opacity="${op}">`; parts.forEach(([n, v, c]) => { const h = v * k; y -= h; g += SV.rect(x, y, 90, h, "", { style: `fill:var(${c});stroke:var(--surface);stroke-width:2`, opacity: 0.85 }); if (h > 16) g += SV.text(x + 45, y + h / 2 + 5, n + " " + v, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:12px" }); }); return g + SV.text(x + 45, base - tot * k - 8, tot, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 45, base + 20, label, "sm", { "text-anchor": "middle" }) + "</g>"; };
  o += grp(90, "Wheat before", [["A", 50, "--accent"], ["B", 30, "--warn"]], 80, s.b) + grp(200, "Wheat after", [["A", 100, "--accent"]], 100, s.a) + grp(380, "Cars before", [["A", 25, "--accent"], ["B", 30, "--warn"]], 55, s.b) + grp(490, "Cars after", [["B", 60, "--warn"]], 60, s.a);
  if (s.t) o += SV.text(380, 54, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Specialisation raises total output", base: { b: 0, a: 0, t: "" }, draw: spChart, steps: [
  { cap: "Country <b>A</b> can make 100 tonnes of wheat <b>or</b> 50 cars. Country <b>B</b> can make 60 tonnes of wheat <b>or</b> 60 cars. <b>Before specialising</b> each splits its resources evenly.", s: { b: 1, a: 0, t: "" } },
  { cap: "Together they make <b>80 tonnes of wheat and 55 cars</b>.", s: { b: 1, a: 0, t: "Before: 80 wheat, 55 cars" } },
  { cap: "A gives up 1 car for 2 tonnes of wheat; B gives up only 1 tonne for 1 car. A has the <b>lower opportunity cost of wheat</b>, B of cars. So <b>A specialises in wheat</b> and <b>B in cars</b>.", s: { b: 1, a: 1, t: "After specialising" } },
  { cap: "Now they make <b>100 tonnes of wheat and 60 cars</b>: more of <b>both</b>. By trading, each can consume more than before. That is the gain from specialisation and trade.", s: { b: 1, a: 1, t: "After: 100 wheat, 60 cars" } },
] });
const SB = ["Workers and firms focus on one product", "They gain skills and use machinery more fully", "Productivity rises and average costs fall (economies of scale)", "Prices are lower and quality higher: more competitive", "More is exported: higher revenue, profit and jobs", "Higher income and growth for the country"];
Lib.stepper($("#stB"), { w: 760, h: 400, label: "How specialisation benefits a country", base: { n: 0 }, draw: mkChain(SB, "--good"), steps: chainSteps(["Workers and firms <b>focus on one product</b>.", "They gain <b>skills</b> and use machinery more fully.", "<b>Productivity rises</b> and average costs fall, with economies of scale.", "<b>Prices are lower</b> and quality is higher, so exports are more competitive.", "<b>More is exported</b>: higher revenue, profit and jobs.", "Higher <b>income and growth</b> for the country."]) });
function riskChart(s) {
  const price = [100, 100, 60, 70, 95, 100], yrs = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "Year 6"], X = (i) => 100 + i * 112, Y = (v) => 330 - (v - 40) * 3.5;
  const earn = (sh) => price.map((p) => 100 * (1 - sh) + sh * p);
  let o = SV.line(80, 340, 80, 40) + SV.line(80, 340, 710, 340) + SV.text(86, 48, "Export earnings (index)", "sm");
  [50, 75, 100].forEach((v) => (o += SV.line(80, Y(v), 710, Y(v), "gr") + SV.text(72, Y(v) + 4, v, "sm", { "text-anchor": "end" })));
  yrs.forEach((y, i) => (o += SV.text(X(i), 358, y, "sm", { "text-anchor": "middle" })));
  [[0.2, "c1", "Diversified (20% from main product)", "dot1"], [0.9, "c2", "Specialised (90% from one product)", "dot2"]].forEach(([sh, cl, lbl, dt], j) => { const e = earn(sh), pts = []; for (let i = 0; i <= Math.min(5, Math.floor(s.n)); i++) pts.push([X(i), Y(e[i])]); if (pts.length > 1) o += SV.path(ptsPath(pts), cl, { "stroke-width": 3 }); pts.forEach((p) => (o += SV.circle(p[0], p[1], 4, dt))); if (s.n >= 1) o += SV.text(660, j ? 84 : 62, lbl, "lbl bd " + (j ? "t2" : "t1"), { "text-anchor": "end", style: "font-size:13px" }); });
  return o;
}
Lib.stepper($("#stR"), { w: 760, h: 400, label: "The risk of depending on one product", base: { n: 0 }, draw: riskChart, steps: [
  { cap: "Two countries. One <b>specialises</b>: 90% of its export earnings come from a single product. The other is <b>diversified</b>: only 20% comes from its main product.", s: { n: 1 } },
  { cap: "Prices of the main product are steady for two years: both earn the same.", s: { n: 2 } },
  { cap: "Then the <b>world price of the main product falls 40%</b>. The diversified country's earnings fall only a little; the specialised country's earnings <b>fall by about a third</b>, with a risk of job losses and a government budget crisis.", s: { n: 3 } },
  { cap: "Prices recover slowly. <b>Evaluate:</b> specialisation raises income when prices are good, but exposes the country to price swings and shocks. Diversifying reduces the risk.", s: { n: 6 } },
] });

/* Lab 1: allocation */
function labA() {
  if (!$("#aa") || !$("#ab")) return;
  const a = +$("#aa").value / 100, b = +$("#ab").value / 100, wheat = 100 * (1 - a) + 60 * (1 - b), cars = 50 * a + 60 * b, base = 80, baseC = 55;
  $("#aa1").textContent = money(wheat, 0) + " t"; $("#aa2").textContent = money(cars, 0); $("#aa3").textContent = wheat >= 100 && cars >= 60 ? "Best" : wheat >= 80 && cars >= 55 ? "Better than even split" : "Worse or equal";
  $("#aav").textContent = `A puts ${Math.round(a * 100)}% of its resources into cars and B puts ${Math.round(b * 100)}%. Total output is ${money(wheat, 0)} tonnes of wheat and ${money(cars, 0)} cars. ${wheat >= 100 && cars >= 60 ? "This is full specialisation by comparative cost: A makes wheat, B makes cars: more of both than the even split (80 wheat, 55 cars)." : a > 0.99 ? "A is making cars, but A is worse at cars than B. Try swapping." : "Try putting A at 0% cars and B at 100% cars."}`;
  const base0 = 290, k = 2.2; let o = SV.line(60, base0, 700, base0);
  [["Wheat (tonnes)", wheat, "--accent", 100], ["Cars", cars, "--warn", 60]].forEach(([n, v, c, best], i) => { const x = 140 + i * 280; o += SV.rect(x, base0 - v * k, 130, v * k, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.rect(x, base0 - best * k, 130, best * k, "", { style: "fill:none;stroke:var(--muted);stroke-width:2;stroke-dasharray:6 4" }) + SV.text(x + 65, base0 - v * k - 8, money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base0 + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labA").innerHTML = o + SV.text(60, 24, "Dashed outline: output with full specialisation", "sm");
}
Lib.slider($("#g1"), { id: "aa", label: "Share of A's resources used for cars", min: 0, max: 100, step: 10, value: 50, fmt: (v) => v + "%", onInput: labA });
Lib.slider($("#g2"), { id: "ab", label: "Share of B's resources used for cars", min: 0, max: 100, step: 10, value: 50, fmt: (v) => v + "%", onInput: labA });
/* Lab 2: dependency */
function labD() {
  if (!$("#da") || !$("#db")) return;
  const sh = +$("#da").value / 100, fall = +$("#db").value / 100, loss = sh * fall;
  $("#da1").textContent = "−" + money(loss * 100, 1) + "%"; $("#da2").textContent = "$" + money(100 * (1 - loss), 0) + "bn"; $("#da3").textContent = loss > 0.2 ? "Severe" : loss > 0.08 ? "Moderate" : "Small";
  $("#dav").textContent = `If ${Math.round(sh * 100)}% of export earnings come from one product and its price falls ${Math.round(fall * 100)}%, total export earnings fall by ${Math.round(sh * 100)}% × ${Math.round(fall * 100)}% = ${money(loss * 100, 1)}%. The more a country depends on one product, the more a price fall hurts. A diversified economy is much safer.`;
  const base = 290; let o = SV.line(80, base, 700, base);
  [["Before", 100, "--accent"], ["After the price fall", 100 * (1 - loss), loss > 0.2 ? "--bad" : "--warn"]].forEach(([n, v, c], i) => { const x = 160 + i * 250, h = v * 2.2; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, "$" + money(v, 0) + "bn", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g3"), { id: "da", label: "Share of export earnings from the main product", min: 10, max: 90, step: 10, value: 70, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g4"), { id: "db", label: "Fall in the world price of that product", min: 0, max: 60, step: 5, value: 30, fmt: (v) => v + "%", onInput: labD });
const BS = [
  { n: "Natural resources and climate", e: "Land, minerals and weather suit some products and not others.", x: "Saudi Arabia (oil), Brazil (coffee), Kenya (cut flowers)" },
  { n: "Low-cost, plentiful labour", e: "Labour-intensive goods can be made cheaply.", x: "Bangladesh and Vietnam (clothing, footwear)" },
  { n: "Skilled labour and education", e: "A skilled workforce makes complex goods and services.", x: "India (IT services), Switzerland (watches, finance)" },
  { n: "Capital and technology", e: "Machinery and infrastructure raise productivity.", x: "Germany (machinery), South Korea (electronics)" },
  { n: "Economies of scale", e: "Large markets and output lower average costs.", x: "China (large-scale manufacturing)" },
  { n: "Government policy and investment", e: "Spending on education and infrastructure, or tax incentives, build new strengths.", x: "Singapore (finance and logistics)" },
];
button_table("bsBtns", "bsOut", BS, 0, (p) => `<div class="tw"><table class="t"><tr><th>Why it leads to specialisation</th><th>Example</th></tr><tr><td>${p.e}</td><td>${p.x}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each an <b>advantage</b> or a <b>disadvantage</b> of specialisation?", buckets: [{ label: "Advantage" }, { label: "Disadvantage" }], items: [
  { text: "Workers gain skills and productivity", b: 0 }, { text: "Lower average costs from economies of scale", b: 0 }, { text: "Higher output and quality", b: 0 }, { text: "Export earnings create jobs and income", b: 0 },
  { text: "Over-dependence on a few products", b: 1 }, { text: "A fall in world price causes a sharp fall in income", b: 1 }, { text: "Dependence on imports for other goods", b: 1 }, { text: "Structural unemployment if the main industry declines", b: 1 },
], done: "Always give both sides." });
Lib.classify($("#cl2"), { prompt: "What is the likely <b>basis for specialisation</b> in each case?", buckets: [{ label: "Natural resources or climate" }, { label: "Cheap or skilled labour" }, { label: "Capital and technology" }], items: [
  { text: "A country with large oil reserves exports oil", b: 0 }, { text: "A tropical country grows coffee and bananas", b: 0 },
  { text: "A country with many low-paid workers makes clothing", b: 1 }, { text: "A country with highly trained programmers sells IT services", b: 1 },
  { text: "A country with advanced factories makes machinery and cars", b: 2 }, { text: "A country with modern infrastructure and technology exports electronics", b: 2 },
], done: "Resources, labour, capital." });
Lib.classify($("#cl3"), { prompt: "Is each a reason a country may <b>change</b> its specialisation?", buckets: [{ label: "Yes, a reason to change" }, { label: "Not a reason" }], items: [
  { text: "Its main resource is running out", b: 0 }, { text: "Education and technology improve", b: 0 }, { text: "Wages rise, so labour-intensive goods cost more", b: 0 }, { text: "World demand for its product falls", b: 0 },
  { text: "It keeps the same costs and demand for decades", b: 1 }, { text: "Nothing changes in the world market", b: 1 },
], done: "Costs, resources, technology, demand." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Specialisation by country", "A country concentrating on producing a limited range of goods and services"],
  ["Opportunity cost", "The next best alternative given up"],
  ["Economies of scale", "Lower average costs as output rises"],
  ["Diversification", "Producing a wider range of goods to reduce risk"],
  ["Export", "A good or service sold to another country"],
  ["Import", "A good or service bought from another country"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why specialisation is risky</b>.", items: [
  "A country depends on one product for most of its exports",
  "The world price of that product falls",
  "Export earnings fall sharply",
  "Firms cut output and workers lose jobs",
  "Government tax revenue falls and the economy suffers",
], done: "Over-dependence." });
''' + calc_js([
    ("Country A can make 40 shirts or 20 phones. How many shirts does it give up for each phone?", 2, "40 ÷ 20 = <b>2 shirts</b>.", "Compare the two choices.", None),
    ("Country B can make 30 shirts or 30 phones. How many shirts does it give up for each phone?", 1, "30 ÷ 30 = <b>1 shirt</b>. B has the lower opportunity cost of phones, so B should make phones.", None, None),
    ("Oil is 80% of a country's export earnings of $50bn. The oil price falls 25%. By how much do total export earnings fall ($bn)?", 10, "80% × 50 = $40bn from oil. 25% × 40 = <b>$10bn</b>.", None, None),
    ("A country exports $60bn of goods, of which $45bn is one product. What percentage of exports is that product?", 75, "45 ÷ 60 × 100 = <b>75%</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is specialisation by country?", ["A country producing everything it needs", "A country concentrating on producing a limited range of goods and services", "A country banning imports", "A country with no exports"], 1, "Concentrating on what it does best."),
    ("Which is an advantage of specialisation?", ["Over-dependence on one product", "Lower costs through skills and economies of scale", "Higher import dependence", "More risk from price falls"], 1, "Productivity and costs improve."),
    ("Which is a disadvantage of specialisation?", ["Higher productivity", "Dependence on a few products", "Lower costs", "Higher output"], 1, "A price fall can hit income hard."),
    ("A country should specialise in goods with the:", ["Highest opportunity cost", "Lowest opportunity cost", "Highest tariffs", "Lowest quality"], 1, "Lowest opportunity cost: it gives up least."),
    ("Which could make a country change its specialisation?", ["New technology and education", "Unchanged costs", "No change in demand", "Fixed resources"], 0, "The pattern of what it can do best changes."),
]) + "\n" + cards_js([("Specialisation by country", "A country concentrating its resources on producing a limited range of goods and services."), ("Opportunity cost", "The next best alternative given up when a choice is made."), ("Economies of scale", "Lower average costs from producing on a larger scale."), ("Diversification", "Producing a wider range of goods and services to reduce risk."), ("Exports", "Goods and services sold to other countries."), ("Imports", "Goods and services bought from other countries."), ("Over-dependence", "Relying too much on one product or one market."), ("Resource allocation", "How a country uses its scarce resources among competing uses."), ("Structural unemployment", "Unemployment caused by the decline of an industry and a mismatch of skills.")]) + "labA(); labD();\n"
explore = '''
  <h2>Lab 1 · Who should make what?</h2>
  <p>Country A can make 100 tonnes of wheat or 50 cars. Country B can make 60 tonnes of wheat or 60 cars. Decide how much of each country's resources go to cars and see the total output.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Total wheat</small><strong id="aa1"></strong></div><div><small>Total cars</small><strong id="aa2"></strong></div><div><small>Result</small><strong id="aa3"></strong></div></div><div class="verdict" id="aav"></div></div></div>
    <svg id="labA" viewBox="0 0 760 330" role="img" aria-label="Total output of wheat and cars"></svg>
  </div>

  <h2>Lab 2 · The risk of dependence</h2>
  <p>Set how much of a country's export earnings come from one product, and how far its price falls.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>Fall in export earnings</small><strong id="da1"></strong></div><div><small>Earnings (from $100bn)</small><strong id="da2"></strong></div><div><small>Impact</small><strong id="da3"></strong></div></div><div class="verdict" id="dav"></div></div></div>
    <svg id="labD" viewBox="0 0 760 330" role="img" aria-label="Export earnings before and after a price fall"></svg>
  </div>

  <h2>Lab 3 · Why countries specialise</h2>
  <p>Pick a basis for specialisation to see how it works and an example.</p>
  <div class="card"><div class="row" id="bsBtns"></div><div id="bsOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "What is meant by specialisation by a country?", "Concentrating on producing a limited range of goods and services, those it produces best or at lowest cost.", "[K|Specialisation by a country is when it concentrates on producing a limited range of goods and services,] [K|usually those it can produce most efficiently or at lowest cost, and trades them for other goods.]"),
    Q(2, "Explain", 2, "Explain one advantage of an economy specialising. (Oct/Nov 2023, P22)", "One mark for the advantage, one for the explanation.", "[K|Workers gain skills and become more productive,] [N|so output rises and costs per unit fall.]"),
    Q(3, "Identify", 2, "Identify two disadvantages of a country specialising. (May/June 2021, P22)", "Over-dependence on a few products; vulnerability to price falls and shocks; dependence on imports; unemployment if the industry declines.", "[K|Over-dependence on a few products (so a fall in demand or price hits income).] [K|Dependence on imports, or vulnerability to events such as bad harvests or trade restrictions.]"),
    Q(4, "Explain", 4, "Explain two reasons why a country may change its specialisation. (Oct/Nov 2023, P21)", "Resources, technology, education, wages and costs, demand.",
      "[K|Its resources may run out.] [N|If an oil field or mine is exhausted, the country has to find a new industry to earn export income.] [K|Technology and education may improve.] [N|A more skilled workforce could move from farming into manufacturing or services, which may earn higher incomes.]"),
    Q(5, "Analyse", 6, "Analyse how specialisation can benefit firms. (May/June 2022, P21)", "Skills, lower costs, reputation and demand, economies of scale, technology.",
      "[K|Specialisation means a firm focuses on one product, and its workers become skilled at making it.] [N|Productivity rises and the cost of production falls, so the firm can offer lower prices.] [N|It may gain a reputation for high quality, which could raise demand, output, revenue and profit.] [N|It may also benefit from economies of scale, for example buying inputs in bulk, becoming more internationally competitive.] [N|It is easier to use machines and new technology when making one product, speeding up production.]", key=True),
    Q(6, "Discuss", 6, "Discuss whether or not specialisation at a national level is harmful to an economy. (May/June 2022, P23)", "Harm: over-dependence, price shocks, unemployment, imports. Not harm: lower costs, higher output, exports, growth. Judge.",
      "[K|National specialisation is when a country concentrates on producing a few goods or services.] [N|It could be harmful because the country becomes dependent on those industries, so a fall in world prices or demand, a poor harvest or new competitors could cut export earnings and cause unemployment.] [N|It may also depend on imports for other goods, which could be cut off.] [E|The risk is greatest where the specialisation is in one primary product.] [N|However, specialisation can raise productivity, lower costs and increase output, and exports bring income, jobs and growth.] [E|Overall, specialisation is likely to benefit an economy that can diversify across several products or switch industries, but could be harmful to one dependent on a single product with unstable prices.]", key=True),
    Q(7, "Discuss", 8, "Discuss whether or not countries specialising benefits consumers. (May/June 2021, P21)", "For: lower prices, more choice via trade, higher quality. Against: fewer domestic goods, dependence on imports, price rises if supply cut, job losses reduce incomes.",
      "[K|Specialisation is when countries produce a limited range of goods and trade for the rest.] [N|It could benefit consumers because lower costs and economies of scale mean lower prices, and trade allows consumers to buy a wider choice of goods and services, often of higher quality.] [N|Increased competition between producers can also keep prices down.] [E|This is more likely if trade is free and there are many suppliers.] [N|However, consumers may become dependent on imports, and if supplies are disrupted or a producer gains market power, prices could rise.] [N|If specialisation causes job losses in the industries a country gives up, consumers affected may have lower incomes.] [E|Overall, specialisation is likely to benefit consumers through lower prices and choice, but the benefits depend on free trade, competition and how well displaced workers find new jobs.]", key=True),
)
tp = tips([
    ("Define it precisely.", "A limited range of goods and services, produced best or at lowest cost, and traded."),
    ("Basis: resources and low cost.", "Climate, minerals, labour skills, capital, technology, economies of scale."),
    ("Link each advantage.", "'Skills rise, so productivity rises and costs fall.'"),
    ("Disadvantages: dependence.", "Price shocks, unemployment, imports, sustainability."),
    ("Judge: depends on how many goods and how stable demand is.", "Diversification reduces the risk."),
], cmds("Define", "Identify", "Explain", "Analyse", "Discuss"))
body = page(CL("6.1.1 Specialisation by country"), "Specialisation by Country", "What specialisation is, why countries specialise, its advantages and disadvantages, and why specialisation changes. Syllabus 6.1.1.",
    learn=learn, watch=watch(("Specialisation raises total output", "stP"), ("How specialisation benefits a country", "stB"), ("The risk of depending on one product", "stR")), explore=explore,
    practise=practise(("Advantage or disadvantage?", "cl1", "card"), ("Basis for specialisation", "cl2", "card"), ("Reasons for changing specialisation", "cl3", "card"), ("Match the term", "m1", "card"), ("Order the risk chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Saudi Arabia and oil", "Saudi Arabia specialises in oil, which makes up most of its exports. It earns huge revenue when prices are high but suffered when prices fell sharply in 2014 and 2020, which is why it is trying to diversify.", "Resource-based specialisation, with price risk."),
        rw("Bangladesh and clothing", "Bangladesh specialises in garments, using abundant low-cost labour. Clothing is the large majority of its exports, creating jobs, but leaving it exposed to changes in global demand.", "Low-cost labour as the basis, and over-dependence."),
        rw("Switzerland's watches and finance", "Switzerland has few natural resources but specialises in high-value watches, pharmaceuticals and banking, using skilled labour and a strong reputation.", "Specialisation based on skills."),
        rw("Venezuela and oil dependence", "Oil makes up the great majority of Venezuela's exports. When oil prices fell after 2014 its export earnings and economy shrank sharply.", "A clear example of the risk of over-dependence."),
        rw("Changing specialisation in Mauritius", "Mauritius moved from sugar to textiles, then tourism and financial services as costs and opportunities changed.", "Why countries change specialisation.")),
    exam=ex, tips=tp)
write("sf1", body, js, "Specialisation by Country", "ig-specialisation")

# =========================================================== 6.1.2 Free trade
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Free trade</span> is when countries buy and sell goods and services with each other <b>without restrictions</b> such as tariffs, quotas, subsidies or embargoes. It lets countries specialise and gain from trade, but it also exposes domestic firms to competition and makes economies dependent on others. Good answers weigh the <b>advantages</b> (lower prices, choice, competition, markets, growth) against the <b>disadvantages</b> (job losses, unfair competition, dependence) and say who gains and who loses.</p></div>

  <h2>Advantages of free trade</h2>
  <div class="grid2">
    <div class="card"><h3>For consumers</h3><ul><li><b>Lower prices</b> from competition and cheaper imports</li><li><b>Greater choice</b> of goods and services</li><li>Higher quality and new products</li></ul></div>
    <div class="card"><h3>For producers</h3><ul><li><b>Larger markets</b> for exports: higher sales and profit</li><li>Economies of scale from higher output</li><li>Access to <b>cheaper and better raw materials</b> and technology</li><li>Competition raises efficiency</li></ul></div>
    <div class="card"><h3>For the economy</h3><ul><li><b>Specialisation</b> and more efficient use of resources</li><li>Higher output, <b>economic growth</b> and jobs in export industries</li><li>Lower costs and inflation pressure</li><li>Better international relations</li></ul></div>
    <div class="card"><h3>For the government</h3><ul><li>More tax revenue as output and incomes rise</li><li>Pressure on firms to be efficient without subsidies</li></ul></div>
  </div>

  <h2>Disadvantages of free trade</h2>
  <ul>
    <li><b>Domestic firms and jobs may be lost</b> when cheaper imports arrive, especially in <b>infant industries</b> and declining industries: structural unemployment.</li>
    <li><b>Unfair competition</b> such as dumping (selling below cost), or imports made with lower wages, environmental or safety standards.</li>
    <li><b>Over-dependence</b> on other countries for essentials such as food and fuel, and on exports.</li>
    <li><b>Vulnerable to global shocks</b> and price changes.</li>
    <li><b>Loss of tariff revenue</b> for the government; risk of a larger current account deficit.</li>
    <li><b>Winners and losers:</b> inequality may widen between workers who gain and those who lose jobs; poorer countries may find it hard to compete with richer, bigger ones.</li>
    <li><b>Environmental costs</b> from more transport and production in countries with weak regulations.</li>
  </ul>

  <h2>Who gains and who loses?</h2>
  <div class="tw"><table class="t">
    <tr><th>Group</th><th>Likely gains</th><th>Likely losses</th></tr>
    <tr><td><b>Consumers</b></td><td>Lower prices, more choice</td><td>Reduced domestic varieties if firms close</td></tr>
    <tr><td><b>Exporters</b></td><td>Bigger markets, more sales and jobs</td><td>More competition abroad</td></tr>
    <tr><td><b>Import-competing firms</b></td><td>Cheaper inputs</td><td>Lost sales, closures</td></tr>
    <tr><td><b>Workers</b></td><td>Jobs in export industries</td><td>Job losses in industries hit by imports</td></tr>
    <tr><td><b>The government</b></td><td>Growth and tax revenue</td><td>Lost tariff revenue; cost of helping displaced workers</td></tr>
  </table></div>

  <h2>Moving towards free trade</h2>
  <p>A government can reduce protectionism by <b>removing or cutting tariffs</b>, <b>raising or removing quotas</b>, <b>ending embargoes</b>, <b>removing subsidies</b> and cutting red tape, and by joining <b>trade agreements</b> or trading blocs (for example free trade areas or the World Trade Organization). Other countries may then cut their own restrictions, opening export markets.</p>
'''
js = HEAD + COMMON + '''
function ftChart(s) {
  const pw = s.pw, qs = pw - 10, qd = 110 - pw; let o = axes("Price", "Quantity");
  o += curve(-1, 110, "c1", "Demand", { t: "t1", dx: -90, dy: -12 }) + curve(1, 10, "c3", "Domestic supply", { t: "t3", dx: -125, dy: 16 });
  o += hline(60, "gr", 50) + vline(50, 60) + SV.circle(QX(50), PY(60), 6, "dot1", { opacity: s.f > 0.5 ? 0.5 : 1 }) + ylab(60, "P") + xlab(50, "Q");
  if (s.f > 0.02) { o += `<g opacity="${s.f}">` + SV.line(QX(0), PY(pw), QX(100), PY(pw), "c2", { "stroke-width": 3 }) + SV.text(QX(100), PY(pw) - 8, "World price $" + Math.round(pw), "lbl bd t2", { "text-anchor": "end" }) + SV.line(QX(qs), PY(pw), QX(qs), PY(0), "gr") + SV.line(QX(qd), PY(pw), QX(qd), PY(0), "gr") + SV.circle(QX(qs), PY(pw), 6, "dot2") + SV.circle(QX(qd), PY(pw), 6, "dot2") + SV.text(QX(qs), PY(0) + 18, "Qs " + Math.round(qs), "sm bd", { "text-anchor": "middle" }) + SV.text(QX(qd), PY(0) + 18, "Qd " + Math.round(qd), "sm bd", { "text-anchor": "middle" }); if (qd > qs) o += SV.text(QX((qs + qd) / 2), PY(pw) + 22, "Imports: " + Math.round(qd - qs), "lbl bd t2", { "text-anchor": "middle", style: halo }); else if (qs > qd) o += SV.text(QX((qs + qd) / 2), PY(pw) - 14, "Exports: " + Math.round(qs - qd), "lbl bd t2", { "text-anchor": "middle", style: halo }); o += "</g>"; }
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 400, label: "Free trade in a market", base: { pw: 40, f: 0 }, draw: ftChart, steps: [
  { cap: "Without trade, the domestic market for a good has equilibrium price <b>$60</b> and quantity <b>50</b>.", s: { pw: 40, f: 0 } },
  { cap: "The country opens to <b>free trade</b>. The <b>world price is $40</b>, lower than the domestic price, so imports enter at $40.", s: { pw: 40, f: 1 } },
  { cap: "<b>Consumers gain:</b> the price falls to $40 and they buy <b>70</b> instead of 50. <b>Domestic producers lose:</b> they supply only <b>30</b>. <b>Imports of 40</b> fill the gap.", s: { pw: 40, f: 1 } },
  { cap: "<b>Evaluate:</b> consumers and importers gain, but domestic firms may close and workers lose jobs. Overall the gains to consumers could outweigh the losses, but not for those who lose jobs.", s: { pw: 40, f: 1 } },
] });
const EX = ["Free trade opens large export markets", "Exporters sell more: higher revenue and profit", "They expand output and gain economies of scale", "Jobs and incomes rise in export industries", "Imported inputs are cheaper and better", "Higher competitiveness and growth for the economy"];
Lib.stepper($("#stE"), { w: 760, h: 400, label: "How free trade could raise growth", base: { n: 0 }, draw: mkChain(EX, "--good"), steps: chainSteps(["Free trade opens <b>large export markets</b>.", "Exporters <b>sell more</b>: higher revenue and profit.", "They expand output and gain <b>economies of scale</b>.", "<b>Jobs and incomes rise</b> in export industries.", "<b>Imported inputs</b> are cheaper and better, lowering costs.", "The economy becomes more <b>competitive</b> and grows faster."]) });
const JL = ["Free trade lets cheaper imports in", "Domestic firms in that industry lose sales", "They cut output, close or lay off workers", "Unemployment rises, especially in some regions", "Workers' skills do not match new jobs: structural unemployment", "The government may need to spend on retraining and benefits"];
Lib.stepper($("#stJ"), { w: 760, h: 400, label: "How free trade can cost jobs", base: { n: 0 }, draw: mkChain(JL, "--bad"), steps: chainSteps(["Free trade lets <b>cheaper imports</b> in.", "Domestic firms in that industry <b>lose sales</b>.", "They <b>cut output, close or lay off workers</b>.", "<b>Unemployment rises</b>, especially in some regions.", "Workers' skills do not match new jobs: <b>structural unemployment</b>.", "The government may need to fund <b>retraining and benefits</b>. Evaluate: the gains to consumers and exporters may outweigh this over time."]) });

/* Lab 1 */
function labF() {
  if (!$("#fa")) return;
  const pw = +$("#fa").value, qs = Math.max(0, pw - 10), qd = Math.max(0, 110 - pw), net = qd - qs;
  $("#fa1").textContent = "$" + pw; $("#fa2").textContent = Math.round(qs); $("#fa3").textContent = net > 0 ? "Imports " + Math.round(net) : net < 0 ? "Exports " + Math.round(-net) : "None";
  $("#fav").textContent = pw < 60 ? `The world price ($${pw}) is below the domestic price of $60. Consumers pay less and buy ${Math.round(qd)}, domestic producers supply only ${Math.round(qs)}, and ${Math.round(net)} is imported. Consumers gain; producers lose.` : pw > 60 ? `The world price ($${pw}) is above the domestic price of $60. Producers can sell abroad at the higher price and supply ${Math.round(qs)}, but consumers buy only ${Math.round(qd)} at the higher price. The country exports ${Math.round(-net)}. Producers gain; consumers lose.` : "The world price equals the domestic price: no trade.";
  $("#labF").innerHTML = ftChart({ pw, f: 1 });
}
Lib.slider($("#g1"), { id: "fa", label: "World price of the good", min: 20, max: 90, step: 5, value: 40, fmt: (v) => "$" + v, onInput: labF });
const WL = [
  { n: "Consumers", g: "Lower prices, more choice and quality.", l: "Fewer local varieties if firms close; may lose income if their own jobs go." },
  { n: "Exporters", g: "Access to larger markets, more sales, scale economies.", l: "More competition in foreign markets." },
  { n: "Domestic firms facing imports", g: "Cheaper inputs and pressure to become efficient.", l: "Lost sales; some close, especially infant industries." },
  { n: "Workers in export industries", g: "More jobs and higher wages.", l: "Fewer protections in some cases." },
  { n: "Workers in import-competing industries", g: "None directly.", l: "Job losses and structural unemployment." },
  { n: "The government", g: "Growth raises tax revenue.", l: "Loses tariff revenue; pays for retraining and benefits." },
  { n: "Poorer countries", g: "Market access, technology, investment.", l: "Hard to compete with larger rich-country firms; risk of dependency." },
];
button_table("wlBtns", "wlOut", WL, 0, (p) => `<div class="tw"><table class="t"><tr><th>Possible gains</th><th>Possible losses</th></tr><tr><td>${p.g}</td><td>${p.l}</td></tr></table></div>`);
const MV = [
  { n: "Remove tariffs", w: "Imports become cheaper; domestic firms face more competition.", e: "Consumers gain; import-competing firms lose; the government loses revenue." },
  { n: "Raise or remove quotas", w: "More imports allowed; supply rises; prices fall.", e: "Consumers gain; domestic producers lose sales." },
  { n: "End embargoes (bans)", w: "Trade restarts with the banned country.", e: "Wider market and choice; may remove political pressure." },
  { n: "Remove subsidies", w: "Firms no longer artificially cheap; fairer competition.", e: "Taxpayers gain; some subsidised firms lose." },
  { n: "Cut red tape and join trade agreements", w: "Easier, cheaper cross-border trade; other countries may open their markets too.", e: "Exporters gain access to larger markets." },
];
button_table("mvBtns", "mvOut", MV, 0, (p) => `<div class="tw"><table class="t"><tr><th>What it does</th><th>Who is affected</th></tr><tr><td>${p.w}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each an <b>advantage</b> or a <b>disadvantage</b> of free trade?", buckets: [{ label: "Advantage" }, { label: "Disadvantage" }], items: [
  { text: "Lower prices for consumers", b: 0 }, { text: "Larger markets for exporters", b: 0 }, { text: "Access to cheaper raw materials", b: 0 }, { text: "More competition raises efficiency", b: 0 },
  { text: "Domestic firms may close", b: 1 }, { text: "Structural unemployment in some industries", b: 1 }, { text: "Dependence on other countries", b: 1 }, { text: "Loss of tariff revenue", b: 1 },
], done: "Always give both sides." });
Lib.classify($("#cl2"), { prompt: "Who is likely to <b>gain</b> and who to <b>lose</b> from a move to free trade?", buckets: [{ label: "Gains" }, { label: "Loses" }], items: [
  { text: "Consumers buying cheaper imports", b: 0 }, { text: "Exporters selling in new markets", b: 0 }, { text: "Firms using imported raw materials", b: 0 },
  { text: "Workers in an industry hit by imports", b: 1 }, { text: "Infant industries without protection", b: 1 }, { text: "A government that relied on tariff revenue", b: 1 },
], done: "Winners and losers." });
Lib.classify($("#cl3"), { prompt: "Does each action <b>move a country towards free trade</b>?", buckets: [{ label: "Towards free trade" }, { label: "Towards protection" }], items: [
  { text: "Cut import tariffs", b: 0 }, { text: "Increase an import quota", b: 0 }, { text: "Join a free trade agreement", b: 0 }, { text: "Remove an embargo", b: 0 },
  { text: "Raise tariffs", b: 1 }, { text: "Ban imports", b: 1 }, { text: "Subsidise domestic producers", b: 1 }, { text: "Cut an import quota", b: 1 },
], done: "Free trade removes restrictions." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Free trade", "Trade between countries without restrictions such as tariffs or quotas"],
  ["Tariff", "A tax on imports"],
  ["Import quota", "A limit on the quantity of a good that can be imported"],
  ["Embargo", "A ban on trade with a country"],
  ["Dumping", "Selling goods abroad at a price below cost"],
  ["Infant industry", "A new industry that cannot yet compete with established foreign firms"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how free trade could reduce prices for consumers</b>.", items: [
  "Trade restrictions are removed",
  "Cheaper foreign goods enter the market",
  "Domestic firms face more competition",
  "Firms cut prices and costs to compete",
  "Consumers pay lower prices and have more choice",
], done: "A competition chain." });
''' + calc_js([
    ("Domestic demand at a world price of $40 is 70 and domestic supply is 30. How many units are imported?", 40, "70 − 30 = <b>40</b>.", None, None),
    ("A good costs $60 at home and $40 in world markets. By what percentage is the world price lower than the home price (1 d.p.)?", 33.3, "(60 − 40) ÷ 60 × 100 = <b>33.3%</b>.", None, 0.1),
    ("A country exports $90bn and imports $100bn. What is the trade balance ($bn)? Use a minus sign for a deficit.", -10, "90 − 100 = <b>−$10bn</b>, a trade deficit.", None, None),
    ("Imports of $5bn face a 10% tariff. How much tariff revenue does the government lose ($bn) if the tariff is removed, assuming imports stay the same?", 0.5, "10% × 5 = <b>$0.5bn</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is free trade?", ["Trade with high tariffs", "Trade between countries without restrictions", "Trade only within a country", "Trade without money"], 1, "No tariffs, quotas or other restrictions."),
    ("Which is a benefit of free trade?", ["Higher prices", "Lower prices and greater choice", "Fewer exports", "Less competition"], 1, "Competition and imports help consumers."),
    ("Which is a disadvantage of free trade?", ["Larger markets", "Domestic firms may be unable to compete with imports", "More choice", "Specialisation"], 1, "Some firms and jobs are lost."),
    ("Which would move a country towards free trade?", ["Raising tariffs", "Banning imports", "Removing quotas", "Subsidising exports"], 2, "Quotas are a restriction."),
    ("Who is most likely to lose from free trade?", ["Consumers", "Exporters", "Workers in industries that compete with imports", "Firms buying cheaper inputs"], 2, "Import-competing industries face competition."),
]) + "\n" + cards_js([("Free trade", "Trade between countries without restrictions such as tariffs, quotas, subsidies or embargoes."), ("Tariff", "A tax on imports."), ("Quota", "A limit on the quantity of a good that can be imported."), ("Embargo", "A ban on trade with a particular country."), ("Subsidy", "A payment by the government to producers to lower their costs."), ("Protection", "Measures to protect domestic producers from foreign competition."), ("Dumping", "Selling goods abroad at a price below the cost of production."), ("Infant industry", "A new industry that is not yet able to compete with established foreign firms."), ("Trade agreement", "A deal between countries to reduce trade barriers."), ("Competitiveness", "How cheaply and well a country's firms can produce compared with rivals.")]) + "labF(); \n"
explore = '''
  <h2>Lab 1 · Opening a market to trade</h2>
  <p>Without trade, the domestic price is $60. Set the world price and see who gains and who loses.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Price after free trade</small><strong id="fa1"></strong></div><div><small>Domestic output</small><strong id="fa2"></strong></div><div><small>Trade</small><strong id="fa3"></strong></div></div><div class="verdict" id="fav"></div></div></div>
    <svg id="labF" viewBox="0 0 760 400" role="img" aria-label="Free trade in a market"></svg>
  </div>

  <h2>Lab 2 · Who gains and who loses?</h2>
  <p>Pick a group to see the likely gains and losses from free trade.</p>
  <div class="card"><div class="row" id="wlBtns"></div><div id="wlOut"></div></div>

  <h2>Lab 3 · Moving towards free trade</h2>
  <p>Pick a measure to see what it does.</p>
  <div class="card"><div class="row" id="mvBtns"></div><div id="mvOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define free trade. (May/June 2022, P23)", "Exports and imports between countries without restrictions such as tariffs or quotas.", "[K|Free trade is when countries export and import goods and services between each other] [K|without restrictions or protection such as tariffs or quotas.]"),
    Q(2, "Identify", 2, "State two benefits of free trade. (May/June 2020, P23)", "Choice, competition, lower prices, specialisation.", "[K|Lower prices (or more choice).] [K|More competition (or more specialisation).]"),
    Q(3, "Explain", 4, "Explain two benefits producers may gain from free trade. (Oct/Nov 2020, P22)", "Larger markets; economies of scale; cheaper inputs; technology; competition.",
      "[K|Producers gain access to a larger global market.] [N|They can sell more, so revenue and profit may increase.] [K|They can produce on a larger scale.] [N|Higher output lets them benefit from economies of scale, lowering average costs, and they may specialise.]"),
    Q(4, "Explain", 4, "Explain two disadvantages of free trade for a country.", "Job losses; infant industries; dependence; dumping.",
      "[K|Domestic firms may be unable to compete with cheaper imports.] [N|Some may close and workers lose their jobs, causing structural unemployment in those industries.] [K|The country may become dependent on other countries.] [N|If it relies on imports of food or fuel, supplies could be disrupted or prices could rise, harming consumers.]"),
    Q(5, "Analyse", 6, "Analyse how a government could reduce protectionism and move towards free international trade. (Oct/Nov 2023, P22)", "Remove tariffs, quotas, embargoes, subsidies; other countries may follow. Each with an effect.",
      "[K|A government could remove tariffs on imports.] [N|Imports become cheaper, so consumers pay less and firms that use imported inputs have lower costs.] [N|It could remove or raise import quotas, increasing the quantity of imports allowed, and end bans or embargoes.] [N|It could remove subsidies so firms' products are not artificially cheap.] [N|If other countries respond by removing their restrictions, the country's exports could be sold without barriers.]", key=True),
    Q(6, "Discuss", 8, "Discuss whether or not free trade between countries increases economic growth. (Oct/Nov 2024, P21)", "For: markets, scale, specialisation, competition, technology. Against: closures, unemployment, dependence, import surge, unequal gains.",
      "[K|Free trade is trade without restrictions and economic growth is a rise in real GDP.] [N|It could increase growth because firms have access to larger markets, so exports and output rise and they gain economies of scale.] [N|Specialisation and competition raise efficiency, and imports of cheaper inputs and technology raise productivity.] [E|These effects are larger for countries with strong export industries.] [N|However, domestic firms that cannot compete may close, reducing output and raising unemployment.] [N|Higher imports could create a current account deficit, and a country dependent on other markets may be hit by global shocks.] [E|Overall, free trade is likely to raise growth in the long run, particularly for efficient producers, but the benefits depend on a country's industries and how it supports workers who lose out.]", key=True),
    Q(7, "Discuss", 6, "Discuss whether or not free trade is beneficial for a city such as Cambridge. (Oct/Nov 2023, P21)", "Apply to the city: firms, universities and students, tourists, consumers; but possible local job losses.",
      "[K|Free trade means there are no restrictions on imports and exports.] [N|Cambridge firms, such as hi-tech and education providers, may gain access to larger markets, increasing sales and jobs, and residents can buy cheaper and more varied goods.] [N|Universities may attract more international students and tourism may grow.] [E|These benefits are greater for the city's export-oriented industries.] [N|However, some local firms may face competition from cheaper imports and may close, and rising demand may increase housing costs.] [E|Overall, free trade is likely to benefit a city with strong export industries such as Cambridge, although some businesses and workers could lose.]", key=True),
    Q(8, "Discuss", 8, "Discuss whether or not a reduction in a country's trade protection will reduce its current account deficit. (Oct/Nov 2020, P23)", "For: other countries cut barriers, exports rise; efficiency. Against: imports rise faster; import surge; domestic firms close.",
      "[K|A current account deficit occurs when the value of imports is greater than the value of exports and other flows; reducing protection means lowering barriers to imports.] [N|It could reduce the deficit if other countries respond by reducing their barriers, so that exports rise, and if competition makes domestic firms more efficient and competitive.] [N|Cheaper imported inputs could also lower costs and help exports.] [E|This is more likely in the longer run.] [N|However, in the short run lower tariffs and quotas make imports cheaper, so imports could rise by more than exports, increasing the deficit, and domestic firms that close may reduce exports.] [E|Overall, removing protection may widen the deficit in the short run but could help over time if the country's firms become more competitive.]", key=True),
)
tp = tips([
    ("Free trade = no tariffs, quotas, subsidies, embargoes.", "Name some."),
    ("Give benefits for specific groups.", "Consumers, producers, workers, government, economy."),
    ("Give a disadvantage for import-competing firms.", "Closures, structural unemployment, dependence."),
    ("Move towards free trade by removing restrictions.", "Tariffs, quotas, embargoes, subsidies, red tape; trade agreements."),
    ("Short run versus long run.", "Imports may rise first; competitiveness takes time."),
], cmds("Define", "Identify", "Explain", "Analyse", "Discuss"))
body = page(CL("6.1.2 Free trade"), "Free Trade", "What free trade is, its advantages and disadvantages, who gains and loses, and how to move towards it. Syllabus 6.1.2.",
    learn=learn, watch=watch(("Free trade in a market", "stM"), ("How free trade could raise growth", "stE"), ("How free trade can cost jobs", "stJ")), explore=explore,
    practise=practise(("Advantage or disadvantage?", "cl1", "card"), ("Who gains and who loses?", "cl2", "card"), ("Towards free trade or protection?", "cl3", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("The EU single market", "Within the European Union goods, services, capital and people can move freely between member countries. Trade among members has grown strongly, though some industries have lost out.", "Free trade among countries, with benefits and costs."),
        rw("China and the WTO", "China joined the World Trade Organization in 2001 and its exports expanded rapidly. Consumers elsewhere benefited from cheaper goods, but some manufacturing industries and workers in other countries lost jobs.", "Winners and losers from free trade."),
        rw("Vietnam's trade agreements", "Vietnam signed free trade agreements with many countries and its exports of electronics and clothing grew quickly, helping growth and jobs.", "Free trade raising exports and growth."),
        rw("Farmers and imports", "Farmers in some countries have protested against imports of cheaper food from abroad, arguing that they cannot compete with large, subsidised producers.", "A disadvantage of free trade for particular groups."),
        rw("Brexit and trade barriers", "After the UK left the EU's single market, new customs checks added costs and paperwork for exporters, showing the benefits of low trade barriers.", "Benefits of reducing barriers.")),
    exam=ex, tips=tp)
write("sf2", body, js, "Free Trade", "ig-free-trade")
