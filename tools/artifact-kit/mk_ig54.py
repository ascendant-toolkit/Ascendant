"""Builds the IGCSE Economics 5.4.1 Causes and consequences of international differences review, written from scratch.
Run: python3 tools/artifact-kit/mk_ig54.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Economic development</span> is an improvement in the <b>standard of living and quality of life</b> of the people of a country: higher income per head, but also better education, healthcare and living conditions (measured by indicators such as the HDI). It is wider than <b>economic growth</b>, which is only a rise in real GDP. Countries differ widely in development. The syllabus gives eight areas of difference, which are both <b>causes</b> and <b>consequences</b> of development: <b>income, productivity, population growth, the size of the primary, secondary and tertiary sectors, saving and investment, education, healthcare and natural resources</b>.</p></div>

  <h2>Development compared with growth</h2>
  <div class="grid2">
    <div class="card"><h3>Economic growth</h3><p>A rise in real GDP over time. It is about the quantity of output. A country can grow without improving the lives of most people, for example if the gains go to a few.</p></div>
    <div class="card"><h3>Economic development</h3><p>A rise in living standards and quality of life, measured by GDP per head, education, healthcare, life expectancy and the HDI. Growth is usually <b>needed</b> for development but is <b>not enough</b> by itself.</p></div>
  </div>
  <p>Countries are often grouped as <b>high-income</b> (more developed) and <b>low-income</b> (less developed) with middle-income countries in between. Development is the process by which low-income economies become high-income economies.</p>

  <h2>The eight differences between countries</h2>
  <div class="tw"><table class="t">
    <tr><th>Difference</th><th>Typical in a lower-income country</th><th>Typical in a higher-income country</th><th>Link to development</th></tr>
    <tr><td><b>Income</b> (GDP per head)</td><td>Low: little to spend on food, education, healthcare</td><td>High</td><td>Low income limits consumption, saving and spending on services</td></tr>
    <tr><td><b>Productivity</b></td><td>Low output per worker: little capital, old technology, low skills</td><td>High</td><td>Productivity drives wages and output</td></tr>
    <tr><td><b>Population growth</b></td><td>Often high: more dependants, pressure on resources</td><td>Often low: ageing</td><td>Fast growth can spread resources thinly and reduce GDP per head</td></tr>
    <tr><td><b>Size of sectors</b></td><td>Large primary sector (farming, mining, fishing)</td><td>Large tertiary sector (services), with a smaller primary sector</td><td>Value added and incomes are higher in secondary and tertiary</td></tr>
    <tr><td><b>Saving and investment</b></td><td>Low saving, little investment in capital</td><td>High saving, more investment</td><td>Investment builds capital and raises productivity</td></tr>
    <tr><td><b>Education</b></td><td>Fewer years of schooling, lower literacy, fewer skills</td><td>More schooling and skills</td><td>Skills raise productivity, wages and job opportunities</td></tr>
    <tr><td><b>Healthcare</b></td><td>Poor: higher infant mortality and lower life expectancy; more days lost to sickness</td><td>Good</td><td>Healthy workers produce more and live longer</td></tr>
    <tr><td><b>Natural resources</b></td><td>May have few, or may export them as raw materials with low value added</td><td>Often well used, or imports resources and adds value</td><td>Resources can raise income but do not guarantee development</td></tr>
  </table></div>

  <h2>The three sectors</h2>
  <div class="tw"><table class="t">
    <tr><th>Sector</th><th>What it does</th><th>Examples</th></tr>
    <tr><td><b>Primary</b></td><td>Extracts or grows natural resources</td><td>Farming, fishing, forestry, mining, oil extraction</td></tr>
    <tr><td><b>Secondary</b></td><td>Processes raw materials into goods and builds things</td><td>Manufacturing (cars, clothes, food processing), construction</td></tr>
    <tr><td><b>Tertiary</b></td><td>Provides services</td><td>Banking, retail, tourism, education, healthcare, transport</td></tr>
  </table></div>
  <p>As a country develops, its economy tends to <b>shift from the primary sector to the secondary and then the tertiary sector</b>. <b>Value added</b> (the extra value created at each stage) is usually lowest in the primary sector, so countries that depend on raw materials often have lower incomes. Primary products also have unstable prices and may run out.</p>

  <h2>Causes of development, and why differences continue</h2>
  <ul>
    <li><b>Investment in capital and technology</b> raises productivity.</li>
    <li><b>Education and healthcare</b> raise the quality of labour.</li>
    <li><b>Government spending</b> on infrastructure, schools and hospitals; stable institutions and low corruption.</li>
    <li><b>Foreign direct investment (FDI)</b> from multinationals, and trade.</li>
    <li><b>Making better use of natural resources</b>, and shifting to higher-value sectors.</li>
  </ul>
  <p>Differences often <b>reinforce themselves</b>. Low income means low saving and investment, so low productivity and low income again: a <b>vicious circle</b>. High income allows more spending on education and health and more investment: a <b>virtuous circle</b>.</p>

  <h2>Consequences of the differences</h2>
  <ul>
    <li>Big gaps in <b>living standards</b>, life expectancy and poverty between countries.</li>
    <li><b>Migration</b> of workers, often skilled, from poorer to richer countries (brain drain).</li>
    <li><b>Dependence</b> on a few exports, on aid or on other countries; vulnerability to price falls and shocks.</li>
    <li>Trade patterns: poorer countries often export primary products and import manufactured goods and services.</li>
  </ul>
'''
js = HEAD + COMMON + '''
function secChart(s) {
  const cols = [["Primary", "--warn"], ["Secondary", "--n"], ["Tertiary", "--accent"]], data = [["Low-income country", [45, 20, 35]], ["Middle-income country", [15, 35, 50]], ["High-income country", [3, 22, 75]]], base = 300, bw = 130, h = 240;
  let o = SV.line(60, base, 710, base) + SV.text(60, 28, "Share of output by sector (%)", "sm");
  data.forEach(([n, v], i) => {
    const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 110 + i * 210; let y = base, g = `<g opacity="${op}">`;
    v.forEach((p, j) => { const hh = (p / 100) * h; y -= hh; g += SV.rect(x, y, bw, hh, "", { style: `fill:var(${cols[j][1]});stroke:var(--surface);stroke-width:2`, opacity: 0.85 }); if (hh > 16) g += SV.text(x + bw / 2, y + hh / 2 + 5, cols[j][0].slice(0, 3) + ". " + p + "%", "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:13px" }); });
    o += g + SV.text(x + bw / 2, base + 22, n, "sm bd", { "text-anchor": "middle" }) + "</g>";
  });
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 400, label: "The sectors as a country develops", base: { n: 0 }, draw: secChart, steps: [
  { cap: "In a <b>low-income country</b> the <b>primary sector</b> (farming, mining, fishing) is large: here 45% of output. Value added is low, prices are unstable and productivity is low.", s: { n: 1 } },
  { cap: "In a <b>middle-income country</b> industry grows: the <b>secondary sector</b> (manufacturing, construction) expands as workers move out of farming. Incomes rise.", s: { n: 2 } },
  { cap: "In a <b>high-income country</b> the <b>tertiary sector</b> (services) dominates, with 75% of output, and the primary sector is small. Services such as finance, tourism and healthcare add high value. Figures are illustrative.", s: { n: 3 } },
] });
const VIC = ["Low income: little saving or tax revenue", "Little investment in capital, education and healthcare", "Low productivity and a large, low-value primary sector", "Output and income stay low", "Population grows quickly and resources are spread thinly", "The country stays poor: a vicious circle"];
Lib.stepper($("#stV"), { w: 760, h: 400, label: "The vicious circle of low development", base: { n: 0 }, draw: mkChain(VIC, "--bad"), steps: chainSteps(["<b>Low income</b> means little saving and little tax revenue.", "There is <b>little investment</b> in capital, education and healthcare.", "<b>Productivity is low</b> and the economy relies on low-value primary products.", "<b>Output and income stay low</b>.", "Fast <b>population growth</b> spreads resources thinly.", "<b>The country stays poor</b>: a vicious circle. Aid, FDI, better policy and education can break it."]) });
const VIR = ["Higher income allows more saving and tax revenue", "More investment in capital, schools and hospitals", "Workers are more skilled and healthier; capital is better", "Productivity rises and the economy moves to higher-value sectors", "Output and income rise further", "Development continues: a virtuous circle"];
Lib.stepper($("#stW"), { w: 760, h: 400, label: "The virtuous circle of development", base: { n: 0 }, draw: mkChain(VIR, "--good"), steps: chainSteps(["<b>Higher income</b> allows more saving and more tax revenue.", "There is <b>more investment</b> in capital, schools and hospitals.", "Workers are <b>more skilled and healthier</b>; capital is better.", "<b>Productivity rises</b> and the economy moves to <b>higher-value sectors</b>.", "<b>Output and income rise</b> further.", "<b>Development continues</b>: a virtuous circle. Evaluate: it needs stability, good institutions and shared gains."]) });

/* Lab 1: country profiles */
const PRO = [
  { n: "Low-income country", inc: 800, prod: 3, pg: 3.0, sec: [45, 20, 35], si: [12, 14], ed: 4, le: 60, res: "Few, or exported unprocessed" },
  { n: "Middle-income country", inc: 6000, prod: 15, pg: 1.2, sec: [15, 35, 50], si: [28, 26], ed: 9, le: 74, res: "Used to build industry" },
  { n: "High-income country", inc: 45000, prod: 60, pg: 0.3, sec: [3, 22, 75], si: [25, 22], ed: 13, le: 82, res: "Imports many, adds high value" },
];
let selP = 1;
function labC() {
  const p = PRO[selP]; $("#cpBtns").innerHTML = PRO.map((q, j) => `<button class="b${j === selP ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
  $$("#cpBtns .b").forEach((b) => (b.onclick = () => { selP = +b.dataset.j; labC(); }));
  $("#cpOut").innerHTML = `<div class="tw"><table class="t"><tr><th>Income per head</th><th>Output per worker</th><th>Population growth</th><th>Primary / secondary / tertiary</th><th>Saving / investment (% GDP)</th><th>Years of schooling</th><th>Life expectancy</th><th>Natural resources</th></tr><tr><td>$${p.inc.toLocaleString("en-US")}</td><td>$${p.prod}k</td><td>${p.pg}%</td><td>${p.sec.join(" / ")}%</td><td>${p.si[0]}% / ${p.si[1]}%</td><td>${p.ed}</td><td>${p.le}</td><td>${p.res}</td></tr></table></div><p class="note">Illustrative figures to show typical patterns, not data for a particular country.</p>`;
  const mx = Math.max(...PRO.map((q) => q.inc)), base = 250; let o = SV.line(60, base, 700, base) + SV.text(60, 20, "Income per head ($, illustrative)", "sm");
  PRO.forEach((q, j) => { const x = 130 + j * 190, h = (Math.log(q.inc) - Math.log(300)) / (Math.log(mx) - Math.log(300)) * 200 + 8; o += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${j === selP ? "--accent" : "--muted"})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, "$" + q.inc.toLocaleString("en-US"), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 20, q.n.replace(" country", ""), "sm", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o;
}
/* Lab 2: development simulator */
function labG() {
  if (!$("#ga") || !$("#gb") || !$("#gc")) return;
  const inv = +$("#ga").value, ed = +$("#gb").value, pg = +$("#gc").value, g = 0.1 * inv + 0.2 * (ed - 2) - pg, start = 2000;
  const v = []; for (let t = 0; t <= 30; t += 5) v.push(start * Math.pow(1 + g / 100, t));
  $("#ga1").textContent = (g >= 0 ? "+" : "") + money(g, 1) + "%"; $("#ga2").textContent = "$" + Math.round(v[6]).toLocaleString("en-US"); $("#ga3").textContent = money(v[6] / start, 1) + " times";
  $("#gav").textContent = `With investment of ${inv}% of GDP, ${ed} years of schooling and population growth of ${pg}%, income per head grows about ${money(g, 1)}% a year, from $2,000 to $${Math.round(v[6]).toLocaleString("en-US")} in 30 years. ${g < 1 ? "Growth in income per head is slow: the country struggles to catch up." : "Faster growth lets the country narrow the gap."} (A simple illustrative model.)`;
  const base = 290, mx = Math.max(...v), k = 220 / mx; let o = SV.line(60, base, 700, base);
  v.forEach((val, i) => { const x = 90 + i * 90, h = Math.max(4, val * k); o += SV.rect(x, base - h, 60, h, "", { style: `fill:var(${g >= 1 ? "--good" : "--warn"})`, opacity: 0.85 }) + SV.text(x + 30, base - h - 8, "$" + Math.round(val / 100) / 10 + "k", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 30, base + 20, i ? "Year " + i * 5 : "Now", "sm", { "text-anchor": "middle" }); });
  $("#labG").innerHTML = o + SV.text(60, 24, "Income per head ($)", "sm");
}
Lib.slider($("#g1"), { id: "ga", label: "Saving and investment (% of GDP)", min: 5, max: 35, step: 1, value: 22, fmt: (v) => v + "%", onInput: labG });
Lib.slider($("#g2"), { id: "gb", label: "Average years of schooling", min: 2, max: 14, step: 1, value: 8, fmt: (v) => v + " years", onInput: labG });
Lib.slider($("#g3"), { id: "gc", label: "Population growth", min: 0, max: 4, step: 0.5, value: 2, fmt: (v) => v + "%", onInput: labG });
const DF = [
  { n: "Income", c: "Low income limits what people can spend on food, education and healthcare, and how much they can save.", e: "Two countries with GDP per head of $800 and $45,000." },
  { n: "Productivity", c: "More capital, better technology and skills raise output per worker and wages.", e: "A modern factory worker compared with a farmer using hand tools." },
  { n: "Population growth", c: "Fast growth increases dependants and pressure on resources, which can lower GDP per head.", e: "Many low-income countries have growth above 2% a year." },
  { n: "Sector sizes", c: "A large primary sector means low value added and unstable incomes; services add more value.", e: "Agriculture is a large share of output in many low-income economies." },
  { n: "Saving and investment", c: "Low saving means little to invest in capital, so growth in capacity is slow.", e: "East Asian economies invested heavily and grew fast." },
  { n: "Education", c: "More schooling raises skills, productivity, wages and job opportunities.", e: "Higher years of schooling in higher-income countries." },
  { n: "Healthcare", c: "Healthier workers lose fewer days to illness and live longer.", e: "Life expectancy of 60 compared with 82." },
  { n: "Natural resources", c: "Resources can raise income, but exporting them raw gives low value added; dependence on one resource is risky.", e: "Oil exporters can still have low HDI." },
];
button_table("dfBtns", "dfOut", DF, 0, (p) => `<div class="tw"><table class="t"><tr><th>How it causes differences in development</th><th>Example</th></tr><tr><td>${p.c}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>sector</b> is each?", buckets: [{ label: "Primary" }, { label: "Secondary" }, { label: "Tertiary" }], items: [
  { text: "Farming", b: 0 }, { text: "Mining", b: 0 }, { text: "Fishing", b: 0 }, { text: "Oil extraction", b: 0 },
  { text: "Car manufacturing", b: 1 }, { text: "Construction", b: 1 }, { text: "Food processing", b: 1 },
  { text: "Banking", b: 2 }, { text: "Tourism", b: 2 }, { text: "Education", b: 2 }, { text: "Retail", b: 2 },
], done: "Primary: extract. Secondary: make. Tertiary: serve." });
Lib.classify($("#cl2"), { prompt: "Is each more typical of a <b>low-income</b> or a <b>high-income</b> country?", buckets: [{ label: "Low-income country" }, { label: "High-income country" }], items: [
  { text: "Large primary sector", b: 0 }, { text: "Low life expectancy", b: 0 }, { text: "High population growth", b: 0 }, { text: "Low saving and investment", b: 0 },
  { text: "Large tertiary sector", b: 1 }, { text: "High average years of schooling", b: 1 }, { text: "High productivity", b: 1 }, { text: "Ageing population", b: 1 },
], done: "Typical patterns, with exceptions." });
Lib.classify($("#cl3"), { prompt: "Is each <b>economic growth</b> or <b>economic development</b>?", buckets: [{ label: "Economic growth" }, { label: "Economic development" }], items: [
  { text: "A rise in real GDP", b: 0 }, { text: "An increase in output over time", b: 0 },
  { text: "A rise in life expectancy and schooling", b: 1 }, { text: "An improvement in the HDI", b: 1 }, { text: "Better living standards and quality of life", b: 1 },
], done: "Growth is about output; development is about living standards." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Economic development", "An improvement in living standards and quality of life"],
  ["Primary sector", "Extracts or grows natural resources"],
  ["Secondary sector", "Manufactures goods and builds"],
  ["Tertiary sector", "Provides services"],
  ["Value added", "The extra value created at each stage of production"],
  ["Foreign direct investment", "Investment in a country by foreign firms"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how low investment keeps a country poor</b>.", items: [
  "Low income means little saving",
  "Little investment in capital, education and healthcare",
  "Low productivity",
  "Low output and income",
  "Little saving again: the cycle repeats",
], done: "The vicious circle of poverty." });
''' + calc_js([
    ("A country's output is $20bn from primary, $30bn from secondary and $50bn from tertiary. What percentage of output is tertiary?", 50, "50 ÷ 100 × 100 = <b>50%</b>.", None, None),
    ("In Jordan 2 million people are in the labour force and 0.3 million work in the secondary sector. What percentage of the labour force is this?", 15, "0.3 ÷ 2 × 100 = <b>15%</b>.", None, None),
    ("GDP is $60bn and the population is 20 million. What is GDP per head ($)?", 3000, "60,000m ÷ 20m = <b>$3,000</b>.", None, None),
    ("A country saves 8% of a GDP of $50bn. How much is saved ($bn)?", 4, "8% × 50 = <b>$4bn</b>.", None, None),
    ("Output per worker is $4,000 in country A and $40,000 in country B. How many times higher is productivity in B?", 10, "40,000 ÷ 4,000 = <b>10 times</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is economic development?", ["A rise in real GDP only", "An improvement in living standards and quality of life", "A rise in population", "An increase in exports"], 1, "It is wider than growth."),
    ("Which sector includes farming and mining?", ["Primary", "Secondary", "Tertiary", "Quaternary"], 0, "Extraction of natural resources."),
    ("A large primary sector is most often linked to:", ["High incomes", "Lower incomes and low value added", "High productivity", "A large services sector"], 1, "Raw materials add little value."),
    ("Which is likely to raise development in the long run?", ["Less education", "More investment in capital and education", "Higher population growth only", "Fewer hospitals"], 1, "Higher productivity and quality of labour."),
    ("A vicious circle of poverty means:", ["Low income leads to low investment and so low income", "High income leads to high investment", "Prices fall", "Exports rise"], 0, "Poverty reinforces itself."),
]) + "\n" + cards_js([("Economic development", "An improvement in the standard of living and quality of life of the people of a country."), ("Economic growth", "A rise in real GDP over time."), ("Primary sector", "The sector that extracts or grows natural resources, such as farming, mining and fishing."), ("Secondary sector", "The sector that manufactures goods and builds, such as car making and construction."), ("Tertiary sector", "The sector that provides services, such as banking, tourism and education."), ("Value added", "The extra value created at each stage of production."), ("Productivity", "Output per worker."), ("Saving", "Income not spent now."), ("Investment", "Spending on capital goods such as machinery and buildings."), ("Foreign direct investment (FDI)", "Investment in a country by foreign firms, such as multinationals."), ("Vicious circle of poverty", "A cycle in which low income leads to low saving and investment, keeping income low."), ("Natural resources", "Raw materials found in nature, such as oil, minerals and fertile land.")]) + "labC(); labG();\n"
explore = '''
  <h2>Lab 1 · Three kinds of country</h2>
  <p>Pick a country type to see how the eight differences usually line up. The figures are illustrative.</p>
  <div class="card"><div class="row" id="cpBtns" style="margin-bottom:10px"></div><svg id="labC" viewBox="0 0 760 280" role="img" aria-label="Income per head by country type"></svg><div id="cpOut"></div></div>

  <h2>Lab 2 · What helps a country catch up?</h2>
  <p>Change saving and investment, schooling and population growth. See how income per head could grow over 30 years starting from $2,000. (Simple illustrative model.)</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Growth of income per head</small><strong id="ga1"></strong></div><div><small>Income per head in 30 years</small><strong id="ga2"></strong></div><div><small>Compared with today</small><strong id="ga3"></strong></div></div><div class="verdict" id="gav"></div></div></div>
    <svg id="labG" viewBox="0 0 760 330" role="img" aria-label="Income per head over 30 years"></svg>
  </div>

  <h2>Lab 3 · The eight differences</h2>
  <p>Pick a difference to see how it affects development.</p>
  <div class="card"><div class="row" id="dfBtns"></div><div id="dfOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define economic development. (May/June 2021, P23)", "Improvement in living standards or quality of life. An increase in GDP alone is not enough.", "[K|Economic development is an improvement in the standard of living and quality of life of the people of a country,] [K|for example through higher income per head, better education and healthcare.]", warn="Saying 'a rise in GDP'. That is economic growth."),
    Q(2, "Define", 2, "Define secondary sector using an example apart from construction. (May/June 2024, P23)", "Manufacturing or processing raw materials, plus an example.", "[K|The secondary sector covers manufacturing and processing of raw materials into goods,] [A|for example car manufacturing.]"),
    Q(3, "Define", 2, "Define tertiary sector using an example apart from healthcare. (May/June 2024, P21)", "Services, plus an example.", "[K|The tertiary sector is the sector that provides services,] [A|for example banking or tourism.]"),
    Q(4, "Identify", 2, "Identify two industries, other than agriculture, that operate in the primary sector. (May/June 2021, P21)", "Mining, fishing, forestry, oil extraction.", "[K|Mining.] [K|Fishing (or forestry, oil extraction).]"),
    Q(5, "Explain", 2, "Explain the meaning of a change from an economy based on the primary sector to one based on the tertiary sector. (Oct/Nov 2022, P21)", "One mark for primary example, one for tertiary example.", "[K|It means the economy moves from mainly primary industries such as agriculture or fishing] [K|to mainly tertiary industries such as tourism or banking.]"),
    Q(6, "Explain", 4, "Explain two causes of differences in economic development between countries. (Oct/Nov 2020, P23)", "Two different causes with a link: income, education, healthcare, investment, resources, productivity, sectors, population growth.",
      "[K|One cause is differences in education.] [N|Countries with more years of schooling have more skilled workers, who are more productive and earn higher wages, so incomes and living standards are higher.] [K|Another cause is differences in saving and investment.] [N|A country that invests more in machinery and infrastructure raises productivity and output, so it can develop faster than one with low investment.]"),
    Q(7, "Explain", 4, "Explain two causes of an increase in a country's economic development. (Oct/Nov 2023, P23)", "Education, healthcare, investment, FDI, better use of resources.",
      "[K|A rise in spending on healthcare is one cause.] [N|Healthier people live longer and lose fewer days to illness, so the HDI and output both rise.] [K|Foreign direct investment is another.] [N|Multinationals bring capital, technology and jobs, raising productivity and incomes.]"),
    Q(8, "Analyse", 6, "Analyse the causes of differences in economic development between countries. (Oct/Nov 2024, P23)", "Several differences, each with a link: income, education, healthcare, population growth, sector size, government spending and FDI, resources. Do not say growth is the same as development.",
      "[K|Countries differ in the level of income.] [N|Higher income allows more spending on goods and services, and more saving and investment.] [K|Education differs.] [N|More schooling gives workers skills, raising productivity and job opportunities.] [K|Healthcare differs.] [N|Better health means longer life expectancy and fewer days lost, so output is higher.] [N|Population growth differs: fast growth increases dependants and spreads resources thinly.] [N|A large primary sector usually means lower value added and lower income than a large secondary or tertiary sector.] [E|Government spending and foreign investment on infrastructure, education and healthcare also differ and can create jobs and reduce poverty.]", key=True),
    Q(9, "Analyse", 5, "Analyse the relationship between the size of countries' primary sector output and GDP per head. (Feb/Mar 2020, P22 style)", "State the overall pattern, quote data for a high and low example, explain why. Say if there is an exception.",
      "[A|Generally there is a negative relationship: countries with a larger primary sector share tend to have a lower GDP per head.] [A|For example, a country where primary output is 40% of GDP may have GDP per head of $1,500, whereas one with primary output of 2% may have $45,000.] [N|The primary sector has low value added and unstable prices, so countries that rely on it have lower incomes.] [N|Higher-income countries have a larger secondary and tertiary sector with higher productivity.] [E|There may be exceptions, such as oil exporters with a large primary sector and high income.]", key=True),
    Q(10, "Discuss", 8, "Discuss whether or not having a large primary sector is a disadvantage to an economy. (May/June 2022, P23)", "Disadvantages: low value added, unstable prices, low productivity, risk of specialising, resources can run out. Advantages: jobs, exports, low start-up costs, high-value resources (oil, gold), funds for diversification.",
      "[K|The primary sector extracts or grows natural resources, such as farming, mining and oil.] [N|A large primary sector could be a disadvantage because primary products usually have low value added and low prices, so incomes and living standards may be low.] [N|Prices of primary products are unstable, so incomes and export earnings fluctuate, and depending on one sector is risky.] [N|Resources may be used up, making growth unsustainable.] [E|This is more serious for low-skill, low-productivity farming.] [N|However, a large primary sector can provide jobs, especially for low-skilled workers, and low start-up costs.] [N|Some primary products such as oil and gold earn high export revenue and the money can be used to diversify into other sectors.] [E|Overall, a large primary sector is more likely to be a disadvantage when it is low-value and unstable, but it can be an advantage when resources are valuable and the revenue is invested wisely.]", key=True),
    Q(11, "Discuss", 8, "Discuss whether or not the growth of the primary sector is beneficial to a country. (Oct/Nov 2020, P21)", "Compare jobs and exports with low value added, price instability and sustainability.",
      "[K|The primary sector includes farming, mining and fishing.] [N|Growth of the primary sector could create jobs, raise output and export earnings, especially if the country has valuable resources, and can use the income to invest.] [N|It can raise incomes for rural workers and reduce inequality between urban and rural areas.] [E|The gains are larger when demand for the product is strong.] [N|However, primary products have low value added and volatile prices, and the sector may use up resources or damage the environment.] [N|It may also lead the country to depend on a few exports rather than developing manufacturing and services.] [E|Overall, primary sector growth is more likely to benefit a country in the short run than as a long-term development strategy, unless the proceeds are invested in other sectors and education.]", key=True),
)
tp = tips([
    ("Development is not growth.", "Development means living standards and quality of life; growth is only real GDP."),
    ("Eight differences:", "income, productivity, population growth, sector size, saving and investment, education, healthcare, natural resources."),
    ("Give a link for each.", "'More schooling raises skills, so productivity and wages are higher.'"),
    ("Primary: low value added.", "Secondary and tertiary add more value, so incomes are higher."),
    ("Mention circles.", "Poverty reinforces itself; development can feed itself."),
    ("Evaluate with 'it depends'.", "On how resources are used, stability and shared gains."),
], cmds("Define", "Identify", "Explain", "Analyse", "Discuss"))
body = page(CL("5.4.1 Causes and consequences of international differences"), "Differences in Economic Development Between Countries", "Economic development, and how income, productivity, population growth, sector sizes, saving and investment, education, healthcare and natural resources differ between countries. Syllabus 5.4.1.",
    learn=learn, watch=watch(("The sectors as a country develops", "stS"), ("The vicious circle of low development", "stV"), ("The virtuous circle of development", "stW")), explore=explore,
    practise=practise(("Which sector?", "cl1", "card"), ("Low-income or high-income?", "cl2", "card"), ("Growth or development?", "cl3", "card"), ("Match the term", "m1", "card"), ("Order the vicious circle", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("South Korea's rapid development", "In the 1960s South Korea was a low-income, mainly agricultural country. High saving and investment, heavy spending on education and a shift to manufacturing and then services raised incomes more than tenfold in a few decades.", "Investment, education and a change of sectors raising development."),
        rw("Mauritius", "A past paper describes Mauritius moving from an economy based on sugar to one based on tourism and services, with rising life expectancy and falling infant mortality.", "A shift from primary to tertiary sector and healthcare improving."),
        rw("Oil and diamonds", "Countries such as Saudi Arabia and Botswana have used revenue from oil or diamonds, with varying success, to fund schools and infrastructure. Others have remained dependent on primary exports with limited diversification.", "Natural resources: a chance, not a guarantee."),
        rw("Niger", "Niger has one of the world's lowest HDI values, with a large primary sector, high population growth, few years of schooling and low productivity.", "Several differences combining in a vicious circle."),
        rw("Bermuda", "A past paper asks students to explain two reasons why Bermuda has a higher level of development than many countries.", "Linking development to sectors, education, healthcare and investment.")),
    exam=ex, tips=tp)
write("dv1", body, js, "Differences in Economic Development Between Countries", "ig-development-differences")
