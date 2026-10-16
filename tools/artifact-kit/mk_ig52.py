"""Builds the three IGCSE Economics 5.2 Poverty reviews (5.2.1 to 5.2.3), written from scratch.
Run: python3 tools/artifact-kit/mk_ig52.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

# =========================================================== 5.2.1 Definitions
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Absolute poverty</span> is when people cannot afford the <b>basic necessities of life</b>: enough food, clean water, shelter, clothing and healthcare. It is measured against a fixed <b>poverty line</b>, such as the World Bank's international poverty line of a few dollars a day (adjusted for price differences between countries). <span class="kw">Relative poverty</span> is when people's income is <b>too low compared with the rest of society</b> for them to take part in the normal activities of that society. It depends on <b>inequality</b>, so it exists in rich countries too.</p></div>

  <h2>Absolute and relative poverty</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Absolute poverty</th><th>Relative poverty</th></tr>
    <tr><td><b>Meaning</b></td><td>Cannot afford basic necessities</td><td>Income too low to take part in normal social life</td></tr>
    <tr><td><b>Measured against</b></td><td>A fixed poverty line (a set income or basket of goods)</td><td>The average or median income of the country (for example below 50% or 60% of median income)</td></tr>
    <tr><td><b>Where</b></td><td>Mostly low-income countries, but also found in rich countries among the homeless and refugees</td><td>Every country, including rich ones</td></tr>
    <tr><td><b>Falls when</b></td><td>Incomes of the poorest rise above the line, for example through economic growth</td><td>The gap between the poor and the rest narrows. It can stay high even when everyone is richer</td></tr>
    <tr><td><b>Example</b></td><td>A family that cannot afford enough food or safe drinking water</td><td>A family that can feed itself but cannot afford heating, a computer or school trips that others take for granted</td></tr>
  </table></div>

  <h2>Measuring poverty</h2>
  <ul>
    <li><b>Poverty line:</b> an income below which a person counts as poor. The international line is set by the World Bank.</li>
    <li><b>Poverty rate:</b> the percentage of the population below the poverty line.</li>
    <li><b>Number in poverty</b> = population × poverty rate.</li>
  </ul>
  <div class="formula">Poverty rate = number of people in poverty ÷ total population × 100</div>

  <h2>Why the difference matters</h2>
  <ul>
    <li><b>Economic growth</b> can lift people out of absolute poverty if the extra income reaches the poor.</li>
    <li>But if the rich gain more than the poor, <b>relative poverty</b> may not fall, or may rise, even though absolute poverty falls.</li>
    <li>Policies differ: absolute poverty needs higher incomes and basic services; relative poverty needs <b>redistribution</b> and a smaller gap.</li>
    <li>Poverty has costs: poor health, less education, lower productivity, social problems and wasted resources.</li>
  </ul>
'''
js = HEAD + COMMON + '''
const BASE = [1, 2, 3, 5, 7, 9, 12, 15, 20, 26];
function lineChart(s) {
  const base = 320, k = 6, inc = BASE.map((b) => b * s.g), sorted = inc.slice().sort((a, b) => a - b), med = (sorted[4] + sorted[5]) / 2, rel = 0.5 * med, abs = 3;
  let o = SV.line(60, base, 710, base) + SV.text(60, 28, "Income per person ($ a day) in ten households", "sm");
  inc.forEach((v, i) => { const x = 80 + i * 62, h = Math.min(v * k, 215), a = v < abs, r = v < rel; o += SV.rect(x, base - h, 44, h, "", { style: `fill:var(${a ? "--bad" : r ? "--warn" : "--accent"})`, opacity: 0.85 }) + SV.text(x + 22, base - h - 6, money(v, 0), "sm bd", { "text-anchor": "middle", style: "font-size:11px" }); });
  const ya = base - abs * k, yr = base - rel * k;
  o += SV.line(60, ya, 710, ya, "dash", { style: "stroke:var(--bad);stroke-width:2.5" }) + SV.line(70, 78, 100, 78, "dash", { style: "stroke:var(--bad);stroke-width:2.5" }) + SV.text(106, 82, "Absolute poverty line: $3 a day", "sm bd");
  if (s.r > 0.02) o += `<g opacity="${s.r}">` + SV.line(60, yr, 710, yr, "dash", { style: "stroke:var(--warn);stroke-width:2.5" }) + SV.line(70, 98, 100, 98, "dash", { style: "stroke:var(--warn);stroke-width:2.5" }) + SV.text(106, 102, "Relative poverty line: 50% of median = $" + money(rel, 1), "sm bd") + "</g>";
  const na = inc.filter((v) => v < abs).length, nr = inc.filter((v) => v < rel).length;
  o += SV.text(380, 52, "In absolute poverty: " + na + " of 10" + (s.r > 0.5 ? " · In relative poverty: " + nr + " of 10" : ""), "lbl bd t2", { "text-anchor": "middle", style: "font-size:15px" });
  return o;
}
Lib.stepper($("#stL"), { w: 760, h: 400, label: "Absolute and relative poverty lines", base: { g: 1, r: 0 }, draw: lineChart, steps: [
  { cap: "Ten households. The <b>absolute poverty line</b> is $3 a day: income needed for basic necessities. <b>Two</b> households (red) fall below it.", s: { g: 1, r: 0 } },
  { cap: "The <b>relative poverty line</b> is 50% of the <b>median</b> income, here $4 a day. <b>Three</b> households are below it: relative poverty includes people who can afford basics but not a normal life.", s: { g: 1, r: 1 } },
  { cap: "The economy grows and <b>everyone's income doubles</b>. Absolute poverty falls to <b>one</b> household, but the relative line doubles too (the median rose), so <b>three households are still in relative poverty</b>.", s: { g: 2, r: 1 } },
  { cap: "If income triples, <b>no one</b> is in absolute poverty. But the poorest are still far below the median: <b>relative poverty remains</b> unless inequality falls.", s: { g: 3, r: 1 } },
] });
function twoChart(s) {
  const base = 320, k = 4.6; let o = SV.line(60, base, 710, base) + SV.text(60, 30, "Share of the population in poverty (%)", "sm");
  [["Low-income country", [45, 55], "Low-income"], ["High-income country", [1, 15], "High-income"]].forEach(([n, v], i) => { const x = 130 + i * 300; o += `<g opacity="${i === 0 ? 1 : s.b}">` + SV.rect(x, base - v[0] * k, 80, v[0] * k, "", { style: "fill:var(--bad)", opacity: 0.85 }) + SV.text(x + 40, base - v[0] * k - 8, v[0] + "%", "lbl bd", { "text-anchor": "middle" }) + SV.rect(x + 90, base - v[1] * k, 80, v[1] * k, "", { style: "fill:var(--warn)", opacity: 0.85 }) + SV.text(x + 130, base - v[1] * k - 8, v[1] + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 85, base + 22, n, "lbl bd", { "text-anchor": "middle" }) + "</g>"; });
  o += SV.rect(520, 50, 14, 14, "", { style: "fill:var(--bad)" }) + SV.text(540, 62, "Absolute", "sm") + SV.rect(520, 72, 14, 14, "", { style: "fill:var(--warn)" }) + SV.text(540, 84, "Relative", "sm");
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 400, label: "Two types of poverty in two countries", base: { b: 0 }, draw: twoChart, steps: [
  { cap: "In a <b>low-income country</b> a large share of people (illustrative 45%) are in <b>absolute poverty</b>, and an even larger share (55%) in relative poverty.", s: { b: 0 } },
  { cap: "In a <b>high-income country</b> almost nobody is in absolute poverty (1%), but <b>15%</b> are still in <b>relative poverty</b>: their income is far below the average.", s: { b: 1 } },
  { cap: "Absolute poverty is mainly a problem of <b>low-income countries</b>; relative poverty <b>exists in every country</b>. Figures here are illustrative.", s: { b: 1 } },
] });

/* Lab 1 */
function labL() {
  if (!$("#la") || !$("#lb") || !$("#lc") || !$("#ld")) return;
  const g = +$("#la").value, u = +$("#lb").value / 100, abs = +$("#lc").value, pct = +$("#ld").value / 100;
  const inc = BASE.map((b) => (10 * (1 - u) + b * u) * g), sorted = inc.slice().sort((a, b) => a - b), med = (sorted[4] + sorted[5]) / 2, rel = pct * med;
  const na = inc.filter((v) => v < abs).length, nr = inc.filter((v) => v < rel).length;
  $("#la1").textContent = na + " of 10"; $("#la2").textContent = nr + " of 10"; $("#la3").textContent = "$" + money(med, 1);
  $("#lav").textContent = `With the absolute line at $${abs}, ${na} household${na === 1 ? " is" : "s are"} in absolute poverty. The relative line is ${Math.round(pct * 100)}% of the median ($${money(med, 1)}) = $${money(rel, 1)}, so ${nr} ${nr === 1 ? "is" : "are"} in relative poverty. ${g > 1 && nr > 0 ? "Growth raised everyone's income, but the relative line rose too." : ""} ${u === 0 ? "With no inequality, nobody falls below 50% of the median." : ""}`;
  const base = 290, k = 5; let o = SV.line(60, base, 710, base);
  inc.forEach((v, i) => { const x = 80 + i * 62, h = Math.min(v * k, 250), a = v < abs, r = v < rel; o += SV.rect(x, base - h, 44, h, "", { style: `fill:var(${a ? "--bad" : r ? "--warn" : "--accent"})`, opacity: 0.85 }) + SV.text(x + 22, base - h - 6, money(v, 0), "sm bd", { "text-anchor": "middle", style: "font-size:11px" }); });
  o += SV.line(60, base - abs * k, 710, base - abs * k, "dash", { style: "stroke:var(--bad);stroke-width:2.5" }) + SV.line(60, base - rel * k, 710, base - rel * k, "dash", { style: "stroke:var(--warn);stroke-width:2.5" });
  $("#labL").innerHTML = o + SV.text(60, 24, "Daily income per person: red = absolute poverty, amber = relative only", "sm");
}
Lib.slider($("#g1"), { id: "la", label: "Economic growth (multiplies everyone's income)", min: 1, max: 4, step: 0.25, value: 1, fmt: (v) => "×" + v, onInput: labL });
Lib.slider($("#g2"), { id: "lb", label: "Inequality (0 = everyone equal, 100 = unequal)", min: 0, max: 100, step: 10, value: 100, fmt: (v) => v + "%", onInput: labL });
Lib.slider($("#g3"), { id: "lc", label: "Absolute poverty line ($ a day)", min: 1, max: 8, step: 0.5, value: 3, fmt: (v) => "$" + v, onInput: labL });
Lib.slider($("#g4"), { id: "ld", label: "Relative poverty line (% of median income)", min: 30, max: 70, step: 5, value: 50, fmt: (v) => v + "%", onInput: labL });
const CASES = [
  { n: "A family cannot afford enough food or safe water", a: "Absolute poverty", w: "Basic necessities are out of reach." },
  { n: "A family eats well but cannot afford a computer or school trips that most children have", a: "Relative poverty", w: "Income is too low to take part in normal social life." },
  { n: "Income is below the World Bank's international poverty line", a: "Absolute poverty", w: "A fixed line based on basic needs." },
  { n: "Income is below 60% of the country's median income", a: "Relative poverty", w: "Measured against the rest of society." },
  { n: "A homeless person in a rich country", a: "Absolute poverty", w: "Cannot afford shelter, a basic necessity, even in a rich country." },
  { n: "Real incomes double, but the gap between rich and poor widens", a: "Absolute poverty falls; relative poverty may not", w: "The relative line moves up with the median." },
];
button_table("csBtns", "csOut", CASES, 0, (p) => `<div class="tw"><table class="t"><tr><th>Which type?</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each <b>absolute</b> or <b>relative</b> poverty?", buckets: [{ label: "Absolute poverty" }, { label: "Relative poverty" }], items: [
  { text: "Cannot afford enough food", b: 0 }, { text: "No access to clean water or shelter", b: 0 }, { text: "Income below the World Bank international poverty line", b: 0 }, { text: "A refugee with no home or income", b: 0 },
  { text: "Income below half of the average", b: 1 }, { text: "Cannot afford what most people in society take for granted", b: 1 }, { text: "Exists even in rich countries with high average income", b: 1 }, { text: "Depends on the gap between rich and poor", b: 1 },
], done: "Absolute: fixed line, basic needs. Relative: compared with others." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Absolute poverty", "Being unable to afford the basic necessities of life"],
  ["Relative poverty", "Having income too low to take part in the normal life of society"],
  ["Poverty line", "The income level below which people are counted as poor"],
  ["Poverty rate", "The percentage of the population below the poverty line"],
  ["Median income", "The middle income when everyone is ranked from lowest to highest"],
  ["Basic necessities", "Food, clean water, shelter, clothing and healthcare"],
], done: "Good vocabulary scores marks." });
''' + calc_js([
    ("Guyana has a population of 0.8 million and 12% live in poverty. How many people live in poverty (thousands)?", 96, "12% × 800,000 = <b>96,000</b>, so 96 thousand.", "800,000 × 0.12.", None),
    ("A country has 40 million people and 6 million live below the poverty line. What is the poverty rate (%)?", 15, "6 ÷ 40 × 100 = <b>15%</b>.", None, None),
    ("The median income is $30 a day. The relative poverty line is 60% of the median. What is the line ($)?", 18, "0.6 × 30 = <b>$18</b>.", None, None),
    ("The poverty rate falls from 20% to 15% in a population of 60 million. How many fewer people are in poverty (millions)?", 3, "5% × 60m = <b>3 million</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is absolute poverty?", ["Having less than the average income", "Being unable to afford basic necessities", "Having less than others in society", "Being unemployed"], 1, "It is about basic needs."),
    ("Which statement about relative poverty is correct?", ["It only exists in poor countries", "It is measured against the incomes of others in a country", "It is a fixed income level", "It disappears when growth occurs"], 1, "It depends on how much others earn."),
    ("Economic growth is most likely to reduce:", ["Absolute poverty, if the poor gain", "Relative poverty in all cases", "Inequality in all cases", "Population"], 0, "Higher incomes lift people over a fixed line."),
    ("Relative poverty can rise even when all incomes rise if:", ["Everyone's income rises equally", "The rich gain more than the poor", "Prices fall", "The poor gain more than the rich"], 1, "The gap widens."),
    ("Who is most likely to be in absolute poverty in a rich country?", ["A homeless person", "A student with a part-time job", "A middle manager", "A retired professor"], 0, "Cannot afford shelter."),
]) + "\n" + cards_js([("Absolute poverty", "Being unable to afford the basic necessities of life."), ("Relative poverty", "Having an income too low to take part in the normal activities of society."), ("Poverty line", "The income level below which a person is counted as poor."), ("Poverty rate", "The percentage of the population living below the poverty line."), ("Median income", "The middle income when all incomes are ranked from lowest to highest."), ("Basic necessities", "The things people need to live: food, water, shelter, clothing and healthcare."), ("International poverty line", "A standard income level, set by the World Bank, for measuring absolute poverty across countries."), ("Inequality", "An uneven distribution of income or wealth."), ("Poverty trap", "A cycle where low income keeps people poor.")]) + "labL(); \n"
explore = '''
  <h2>Lab 1 · Poverty lines and growth</h2>
  <p>Ten households. Raise incomes with growth, change how unequal the economy is, and move the absolute and relative lines. See who counts as poor.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>In absolute poverty</small><strong id="la1"></strong></div><div><small>In relative poverty</small><strong id="la2"></strong></div><div><small>Median income</small><strong id="la3"></strong></div></div><div class="verdict" id="lav"></div></div></div>
    <svg id="labL" viewBox="0 0 760 330" role="img" aria-label="Household incomes and poverty lines"></svg>
  </div>

  <h2>Lab 2 · Which type of poverty?</h2>
  <p>Pick a case to see how to classify it.</p>
  <div class="card"><div class="row" id="csBtns"></div><div id="csOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain the difference between absolute poverty and relative poverty. (May/June 2022, P21)", "One mark each for naming each type and one for the explanation. Use 'whereas'.",
      "[K|Absolute poverty is when people cannot afford the basic necessities of life, such as food, water and shelter,] [N|and is measured against a fixed poverty line, for example the World Bank's international line.] [K|Relative poverty is when people's income is too low compared with others in the country to take part in normal social activities,] [N|so it depends on inequality and can exist even in a rich country where basic needs are met.]"),
    Q(2, "Explain", 4, "Explain the two types of poverty. (Oct/Nov 2020, P21)", "Identify and explain each.",
      "[K|Absolute poverty is when someone cannot afford the basic necessities of life,] [N|for example having an income below the international poverty line.] [K|Relative poverty is when someone's income is too low to participate in the normal activities of society,] [N|which happens when there is inequality, even where basic needs are met.]"),
    Q(3, "Identify", 2, "Identify two reasons why a person may experience absolute poverty. (Oct/Nov 2023, P23)", "Short answers: unemployment, ill health, old age, war, natural disaster, low education, income too low.",
      "[K|Unemployment (no wage to buy basic necessities).] [K|Sickness or poor health (or old age, war, famine or natural disasters).]"),
    Q(4, "Calculate", 1, "Guyana has a population of 0.8 million and a poverty rate of 12%. Calculate the number of people living in poverty. (May/June 2023, P22 style)", "Population × rate. Mind units.", "[A|0.8 million × 12% = 96,000 people.]"),
    Q(5, "Explain", 4, "Explain why relative poverty may exist even in a high-income country.", "Relative to average; inequality; participation in society.",
      "[K|Relative poverty is measured against the incomes of others in the same country.] [N|In a high-income country the average income is high, so people with low incomes may still be able to afford basic necessities but not what most others take for granted, such as housing in good areas or school trips.] [N|If the rich gain more than the poor, the gap widens, so relative poverty could remain or rise even when absolute poverty is low.]"),
    Q(6, "Analyse", 6, "Analyse how economic growth could affect absolute and relative poverty.", "Growth may lift people over the line; relative poverty depends on distribution.",
      "[K|Economic growth is a rise in real GDP and raises incomes.] [N|If the extra income reaches poor households, for example through more jobs and higher wages, more people may be able to afford basic necessities, so absolute poverty could fall.] [N|However, relative poverty depends on the gap between rich and poor.] [N|If higher earners gain more, the median income rises and the relative poverty line rises with it, so relative poverty could stay the same or increase.] [E|Governments may need policies such as progressive taxes and benefits to share the gains.]", key=True),
)
tp = tips([
    ("Absolute = basic necessities, fixed line.", "Relative = compared with others in the country."),
    ("Say it can exist in rich countries.", "Relative poverty does, and so can absolute poverty among the homeless."),
    ("Growth helps absolute poverty more reliably.", "Relative poverty depends on distribution."),
    ("Use the formula.", "Poverty rate = number in poverty ÷ population × 100."),
    ("Name the line.", "International poverty line (World Bank) for absolute; percentage of median income for relative."),
], cmds("Identify", "Calculate", "Explain", "Analyse"))
body = page(CL("5.2.1 Definitions of absolute and relative poverty"), "Absolute and Relative Poverty", "What absolute and relative poverty mean, how they are measured and how they differ. Syllabus 5.2.1.",
    learn=learn, watch=watch(("Absolute and relative poverty lines", "stL"), ("Two types of poverty in two countries", "stT")), explore=explore,
    practise=practise(("Absolute or relative?", "cl1", "card"), ("Match the term", "m1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Extreme poverty falling", "The share of the world's people in extreme poverty has fallen sharply since 1990, helped by fast growth in China and India, although many people in sub-Saharan Africa remain in absolute poverty.", "Growth reducing absolute poverty."),
        rw("Relative poverty in rich countries", "In countries such as the UK and the US, millions of people are below the relative poverty line even though few are in absolute poverty. Hawaii is a past paper example, with about 9% of its population in poverty.", "Relative poverty in a high-income economy."),
        rw("Setting the line", "The World Bank has raised its international poverty line over the years to reflect higher prices; older papers used $1.90 a day, newer figures are higher.", "The line is a convention, not a fixed truth."),
        rw("Homelessness", "People sleeping on the streets of rich cities lack shelter, a basic necessity, so they are in absolute poverty even in a high-income country.", "Absolute poverty can exist in rich countries too.")),
    exam=ex, tips=tp)
write("po1", body, js, "Absolute and Relative Poverty", "ig-poverty-definitions")

# =========================================================== 5.2.2 Causes
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The syllabus lists five causes of poverty: <b>unemployment</b>, <b>low wages</b>, <b>illness</b>, <b>age</b> and <b>environmental factors</b>. They often overlap and reinforce each other, which is why poverty can last for generations. To answer well, name the cause, explain how it cuts a household's income or raises its costs, and say who is most at risk.</p></div>

  <h2>The five causes</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>How it leads to poverty</th><th>Who is at risk</th></tr>
    <tr><td><b>Unemployment</b></td><td>No wage. Benefits may be small or absent. Long spells reduce skills and make it harder to find work</td><td>Workers in declining industries, young people, people in recessions</td></tr>
    <tr><td><b>Low wages</b></td><td>Earnings too low to afford necessities, especially with a large family or high living costs</td><td>Unskilled workers, farmers with low yields, informal workers, part-time and casual workers</td></tr>
    <tr><td><b>Illness</b></td><td>Cannot work; medical bills; carers lose earnings; poor health reduces productivity and education</td><td>People without health insurance or free healthcare, those in places with disease and poor sanitation</td></tr>
    <tr><td><b>Age</b></td><td>Children cannot earn; the old may have no pension, savings or ability to work</td><td>Large families, pensioners without state pension, orphans</td></tr>
    <tr><td><b>Environmental factors</b></td><td>Drought, floods, storms, soil erosion and climate change destroy crops, fish stocks and homes, and cut incomes</td><td>Farmers, fishermen, people in disaster-prone or low-lying areas</td></tr>
  </table></div>

  <h2>Other causes that link to these</h2>
  <ul>
    <li><b>Low education and skills:</b> lead to low wages and unemployment.</li>
    <li><b>Discrimination:</b> unequal access to jobs, pay and education.</li>
    <li><b>War, conflict and refugees:</b> destroy livelihoods and force people to leave.</li>
    <li><b>Lack of state benefits and services</b> such as pensions and free healthcare.</li>
    <li><b>Lack of access to credit, markets or land.</b></li>
  </ul>

  <h2>The poverty trap</h2>
  <p>Poverty tends to <b>reinforce itself</b>: poor families cannot afford to educate their children, so the children have low skills and low wages and stay poor. Illness, lost income and low savings leave households with no cushion against shocks such as a job loss or a drought.</p>

  <h2>Poverty over the life cycle</h2>
  <p>Households often face a <b>higher risk of poverty at the start and end of life</b>: when children cannot earn and cost money, and in old age when working income falls and pensions may be small or missing.</p>
'''
js = HEAD + COMMON + '''
function lifeChart(s) {
  const base = 320, X = (a) => 80 + a * 7.2, Y = (v) => base - v * 2.4, inc = (a) => (a < 18 ? 10 : a < 25 ? 10 + (35 * (a - 18)) / 7 : a < 60 ? 45 + 55 * Math.sin(((a - 25) / 35) * Math.PI) : Math.max(15, 45 - (a - 60) * 0.9));
  let o = SV.line(80, base, 710, base) + SV.line(80, base, 80, 40) + SV.text(86, 48, "Household income", "sm") + SV.text(710, base + 28, "Age", "sm", { "text-anchor": "end" });
  o += SV.line(80, Y(35), 710, Y(35), "dash", { style: "stroke:var(--bad);stroke-width:2" }) + SV.text(86, Y(35) - 6, "Poverty line", "sm bd", { style: "fill:var(--bad)" });
  [0, 20, 40, 60, 80].forEach((a) => (o += SV.text(X(a), base + 16, a, "sm", { "text-anchor": "middle" })));
  const pts = []; for (let a = 0; a <= 85; a += 1) if (a <= s.a) pts.push([X(a), Y(inc(a))]);
  if (pts.length > 1) o += SV.path(ptsPath(pts), "c1", { "stroke-width": 3 });
  if (s.a >= 0) o += SV.circle(X(s.a), Y(inc(s.a)), 7, inc(s.a) < 35 ? "dot2" : "dot1");
  if (s.t) o += SV.text(X(s.a), Y(inc(s.a)) - 18, s.t, "lbl bd t2", { "text-anchor": "middle", style: halo });
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Poverty risk over the life cycle", base: { a: 0, t: "" }, draw: lifeChart, steps: [
  { cap: "<b>Childhood:</b> children cannot earn, and the household has more mouths to feed. Large families face a higher risk of poverty.", s: { a: 8, t: "Children" } },
  { cap: "<b>Young adults</b> start work. Wages are low at first, then rise with skills and experience.", s: { a: 30, t: "Early career" } },
  { cap: "<b>Middle age:</b> incomes peak. The risk of poverty is lowest, unless there is unemployment, illness or low pay.", s: { a: 45, t: "Peak earnings" } },
  { cap: "<b>Old age:</b> people retire or cannot work. Without a pension or savings, income falls <b>below the poverty line</b>.", s: { a: 80, t: "Old age" } },
] });
const ENV = ["A drought or flood hits farmland or fishing grounds", "Crops fail or the catch falls", "Farm or fishing income falls sharply", "Households sell assets or borrow at high interest", "They cannot afford enough food, schooling or healthcare", "Poverty deepens and the next shock is harder to survive"];
Lib.stepper($("#stE"), { w: 760, h: 400, label: "Environmental shocks and poverty", base: { n: 0 }, draw: mkChain(ENV, "--warn"), steps: chainSteps(["A <b>drought, flood or storm</b> hits farmland or fishing grounds.", "<b>Crops fail</b> or the <b>catch falls</b> (also from overfishing and climate change).", "<b>Income falls sharply</b> for farmers and fishermen.", "Households <b>sell assets or borrow</b> at high interest rates.", "They <b>cannot afford food, schooling or healthcare</b>.", "<b>Poverty deepens</b>, and the next shock is even harder to survive."]) });
const TRAP = ["Low income: cannot afford good food, healthcare or school fees", "Poor health and little education", "Low productivity: only low-paid or insecure work", "Income stays low", "Children inherit the same disadvantages", "Poverty is passed on: the poverty trap"];
Lib.stepper($("#stP"), { w: 760, h: 400, label: "The poverty trap", base: { n: 0 }, draw: mkChain(TRAP, "--bad"), steps: chainSteps(["<b>Low income:</b> the family cannot afford good food, healthcare or school fees.", "Children have <b>poor health and little education</b>.", "As adults they have <b>low productivity</b> and low-paid or insecure work.", "<b>Income stays low</b>.", "<b>Their children</b> inherit the same disadvantages.", "<b>Poverty is passed on</b>: the poverty trap. Policy has to break the cycle."]) });

/* Lab 1: shocks */
function labK() {
  if (!$("#ka") || !$("#kb") || !$("#kc") || !$("#kd")) return;
  const job = +$("#ka").value / 100, wage = +$("#kb").value / 100, med = +$("#kc").value, crop = +$("#kd").value / 100;
  const base = 420, inc = base * (1 - job) * (1 - wage) * (1 - crop), needs = 300 + med, gap = inc - needs;
  $("#ka1").textContent = "$" + Math.round(inc); $("#ka2").textContent = "$" + needs; $("#ka3").textContent = (gap >= 0 ? "+$" : "−$") + Math.abs(Math.round(gap));
  $("#kav").textContent = gap >= 0 ? `Income of $${Math.round(inc)} covers basic needs of $${needs}, with $${Math.round(gap)} spare. This household is not in absolute poverty.` : `Income of $${Math.round(inc)} is $${Math.abs(Math.round(gap))} short of basic needs of $${needs}: the household cannot afford the basic necessities: absolute poverty. Combined shocks (job loss, low pay, illness, crop failure) hit hardest.`;
  const b = 300; let o = SV.line(80, b, 700, b);
  [["Weekly income", inc, "--accent"], ["Basic needs", needs, "--warn"]].forEach(([n, v, c], i) => { const x = 160 + i * 250, h = v * 0.55; o += SV.rect(x, b - h, 150, h, "", { style: `fill:var(${gap >= 0 || i === 1 ? c : "--bad"})`, opacity: 0.85 }) + SV.text(x + 75, b - h - 8, "$" + Math.round(v), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, b + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labK").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ka", label: "Unemployment: share of working time lost", min: 0, max: 100, step: 10, value: 0, fmt: (v) => v + "%", onInput: labK });
Lib.slider($("#g2"), { id: "kb", label: "Low wages: cut in the hourly wage", min: 0, max: 50, step: 5, value: 0, fmt: (v) => v + "%", onInput: labK });
Lib.slider($("#g3"), { id: "kc", label: "Illness: extra medical costs a week", min: 0, max: 200, step: 20, value: 0, fmt: (v) => "$" + v, onInput: labK });
Lib.slider($("#g4"), { id: "kd", label: "Environmental shock: share of farm income lost", min: 0, max: 100, step: 10, value: 0, fmt: (v) => v + "%", onInput: labK });
const CAU = [
  { n: "Unemployment", m: "No wage; small or no benefits; skills fade; harder to re-enter work.", w: "Workers in declining industries; young people; people in recessions.", p: "Job creation, retraining, unemployment benefit." },
  { n: "Low wages", m: "Pay too low to afford necessities, especially with a large family.", w: "Unskilled, part-time and informal workers; small farmers.", p: "National minimum wage, education and training, growth." },
  { n: "Illness", m: "Cannot work; medical costs; carers lose earnings; lower productivity.", w: "People without healthcare; in areas with disease and poor sanitation.", p: "Free or subsidised healthcare, clean water, sickness benefits." },
  { n: "Age", m: "Children cannot earn; the old may have no pension or savings.", w: "Large families; pensioners without state pensions.", p: "State pensions, child benefits, family support." },
  { n: "Environmental factors", m: "Drought, floods, soil erosion, overfishing and climate change destroy crops, fish stocks and homes.", w: "Farmers, fishermen, people in disaster-prone areas.", p: "Irrigation, insurance, disaster relief, sustainable fishing rules." },
  { n: "Low education", m: "Low skills mean low wages and unemployment. Poor families may not afford schooling.", w: "Children of poor families; girls in some countries.", p: "Free education, school meals, grants." },
];
button_table("cuBtns", "cuOut", CAU, 0, (p) => `<div class="tw"><table class="t"><tr><th>How it causes poverty</th><th>Who is at risk</th><th>Possible response</th></tr><tr><td>${p.m}</td><td>${p.w}</td><td>${p.p}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>cause of poverty</b> is each?", buckets: [{ label: "Unemployment" }, { label: "Low wages" }, { label: "Illness" }, { label: "Age" }, { label: "Environmental" }], items: [
  { text: "A factory closes and workers have no income", b: 0 }, { text: "Pay in a job is too low for basic needs", b: 1 }, { text: "A parent cannot work because of disease", b: 2 },
  { text: "A pensioner with no state pension", b: 3 }, { text: "A drought destroys the harvest", b: 4 }, { text: "Fish stocks collapse after overfishing and warming seas", b: 4 },
  { text: "Medical bills use up the family's savings", b: 2 }, { text: "A large family of young children with one earner", b: 3 },
], done: "Five causes in the syllabus." });
Lib.classify($("#cl2"), { prompt: "Does each make poverty <b>more likely</b> or <b>less likely</b>?", buckets: [{ label: "More likely" }, { label: "Less likely" }], items: [
  { text: "Unemployment rises", b: 0 }, { text: "Illness with no health insurance", b: 0 }, { text: "Floods destroy farmland", b: 0 }, { text: "No state pension", b: 0 },
  { text: "A good education and skills", b: 1 }, { text: "Free healthcare", b: 1 }, { text: "A job paying above the poverty line", b: 1 }, { text: "A pension in old age", b: 1 },
], done: "Know both the causes and the protections." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Poverty trap", "A cycle where low income keeps people poor across generations"],
  ["Structural unemployment", "Unemployment from a mismatch of skills and jobs"],
  ["Informal economy", "Unregulated work with low and insecure pay"],
  ["Subsistence farming", "Growing food mainly for the family's own use"],
  ["Climate change", "Long-term change in weather patterns that can harm farming and fishing"],
  ["Dependency ratio", "Number of dependants (young and old) compared with workers"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why children of poor families tend to receive less education</b>.", items: [
  "The family has a low income",
  "It cannot afford fees, books, uniforms or transport",
  "Children may work or care for others instead of attending school",
  "Children leave school with few skills",
  "They find only low-paid work or unemployment",
  "They remain poor and cannot afford to educate their own children",
], done: "The poverty trap across generations." });
''' + calc_js([
    ("A worker earns $400 a week. She loses 40% of her working hours. What is her new weekly income ($)?", 240, "400 × 0.6 = <b>$240</b>.", None, None),
    ("Basic needs cost $300 a week. Her income falls to $240. How big is the shortfall ($)?", 60, "300 − 240 = <b>$60</b>.", None, None),
    ("A fisherman's catch falls from 50 kg a day to 30 kg a day. By what percentage has it fallen?", 40, "20 ÷ 50 × 100 = <b>40%</b>.", None, None),
    ("In a village of 2,000 people, 30% are children and 10% are elderly. How many are of working age?", 1200, "100% − 40% = 60%. 60% × 2,000 = <b>1,200</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which is a cause of poverty?", ["Unemployment", "High wages", "Free healthcare", "A state pension"], 0, "No wage means no money for necessities."),
    ("Why might old people be at risk of poverty?", ["They earn peak incomes", "They may have no pension or savings and cannot work", "They pay high income tax", "They are always employed"], 1, "Incomes fall in old age."),
    ("How can illness cause poverty?", ["It increases wages", "It stops people working and raises medical costs", "It raises school attendance", "It lowers prices"], 1, "Lost income and costs."),
    ("Which environmental factor could cause poverty among farmers?", ["Drought", "A good harvest", "Higher crop prices", "Irrigation"], 0, "Crops fail and incomes fall."),
    ("A poverty trap is when:", ["Poor people stay poor over generations", "Rich people lose money", "Prices fall", "Wages rise quickly"], 0, "Low income, low education and low income again."),
]) + "\n" + cards_js([("Unemployment", "Being without a job while willing, able and looking for work."), ("Low wages", "Pay too low to afford basic necessities."), ("Illness", "Poor health that prevents work and raises costs."), ("Dependants", "People who rely on others' income, such as children and the elderly."), ("Environmental factors", "Natural conditions such as drought, floods and climate change that affect income."), ("Poverty trap", "A cycle in which low income keeps people poor over generations."), ("Informal economy", "The part of the economy not regulated, protected or taxed by the government."), ("Subsistence farming", "Farming mainly to feed the farmer's own family."), ("Migration", "People moving to another place to find work or safety.")]) + "labK(); \n"
explore = '''
  <h2>Lab 1 · How shocks push a household into poverty</h2>
  <p>A family earns $420 a week and basic needs cost $300. Add shocks: job loss, lower pay, illness and crop failure. See when income no longer covers basic needs.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>Weekly income</small><strong id="ka1"></strong></div><div><small>Basic needs</small><strong id="ka2"></strong></div><div><small>Left over</small><strong id="ka3"></strong></div></div><div class="verdict" id="kav"></div></div></div>
    <svg id="labK" viewBox="0 0 760 340" role="img" aria-label="Weekly income compared with basic needs"></svg>
  </div>

  <h2>Lab 2 · Causes of poverty</h2>
  <p>Pick a cause to see how it works, who is at risk and what might help.</p>
  <div class="card"><div class="row" id="cuBtns"></div><div id="cuOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain two causes of poverty. ", "Two different causes, each developed: unemployment, low wages, illness, age, environmental factors.",
      "[K|One cause is unemployment.] [N|People without a job have no wage to buy food, water and housing, and benefits may be small or absent, so they could fall into absolute poverty.] [K|Another cause is illness.] [N|Sick people may be unable to work and have medical bills to pay, so their income falls while their costs rise.]"),
    Q(2, "Explain", 4, "Explain two causes of poverty amongst fishermen. (May/June 2021, P23)", "Environmental and economic: falling catches, climate change, overfishing, low prices, lack of capital.",
      "[K|One cause is falling fish stocks, for example from overfishing or climate change.] [N|If catches fall, fishermen have less to sell, so their incomes fall and they may be unable to afford basic necessities.] [K|Another cause is low prices and lack of capital.] [N|Small fishermen with old boats cannot catch much and may have to accept low prices from buyers, which keeps their income low.]"),
    Q(3, "Analyse", 5, "Analyse why the children of poor families tend to receive less education. (May/June 2020, P22)", "Cost of schooling, need to work, poor health, poor schools; then link to poverty cycle.",
      "[K|Poor families have low incomes and may not be able to afford school fees, books or uniforms.] [N|Children may need to work or care for family members instead of going to school.] [N|Poor nutrition and illness can reduce attendance and ability to learn, and schools in poor areas may be of low quality.] [N|With less education the children have fewer skills, so they are likely to earn low wages and remain poor.]", key=True),
    Q(4, "Analyse", 6, "Analyse how unemployment can lead to poverty.", "Chain: no wage, benefits small, skills fade, debts; then who is most affected.",
      "[K|Unemployment means people have no earnings.] [N|Without a wage a household may be unable to afford food, housing and healthcare.] [N|Unemployment benefit may be low or limited in time, or not available in some countries, so household income could fall below the poverty line.] [N|The longer someone is unemployed, the more their skills and confidence fade, making it harder to find a job again.] [N|Families may fall into debt or sell assets, making poverty last longer.]", key=True),
    Q(5, "Discuss", 8, "Discuss whether or not unemployment is the main cause of poverty.", "For: no income. Against: low wages, illness, age, environment, and employed people can be poor. Judge: depends on country.",
      "[K|Poverty means having too little income to afford the basics.] [N|Unemployment is a major cause because without a wage a household cannot buy necessities, and in countries without strong benefits unemployed households can quickly fall into absolute poverty.] [E|This is more important in recessions and in areas where an industry has closed.] [N|However, many people in work are poor because wages are too low, especially unskilled and informal workers and small farmers.] [N|Illness, old age without a pension, large families and environmental shocks such as drought are other important causes.] [E|Overall, unemployment is one of several causes. Its importance depends on the country: in rich countries unemployment and low wages may dominate, whereas in poorer countries low productivity in farming and lack of healthcare may be more important.]", key=True),
)
tp = tips([
    ("Five causes:", "unemployment, low wages, illness, age, environmental factors."),
    ("Explain how each cuts income or raises costs.", "No wage, medical bills, lost crops."),
    ("Name who is at risk.", "Fishermen, farmers, pensioners, large families."),
    ("Link causes together.", "Illness reduces work; low education leads to low wages: the poverty trap."),
    ("Use the context in the question.", "Fishermen, farmers, a specific country."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("5.2.2 Causes of poverty"), "Causes of Poverty", "Unemployment, low wages, illness, age and environmental factors, and how they combine into a poverty trap. Syllabus 5.2.2.",
    learn=learn, watch=watch(("Poverty risk over the life cycle", "stA"), ("Environmental shocks and poverty", "stE"), ("The poverty trap", "stP")), explore=explore,
    practise=practise(("Which cause?", "cl1", "card"), ("More or less likely?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Drought in the Sahel", "Repeated droughts in the Sahel region of Africa have destroyed crops and herds, pushing millions of farming families into hunger.", "Environmental causes of poverty."),
        rw("Job losses after factory closures", "When major employers close, as in former coal and steel towns, long-term unemployment and low-paid work can leave whole areas with high poverty.", "Unemployment as a cause."),
        rw("Out-of-pocket healthcare costs", "In countries with little public healthcare, medical bills are a leading reason families fall into poverty, because they sell assets or borrow to pay.", "Illness as a cause."),
        rw("Fishing communities", "A past paper asks about causes of poverty among fishermen, linked to falling fish stocks and low prices.", "Applying causes to a specific group.")),
    exam=ex, tips=tp)
write("po2", body, js, "Causes of Poverty", "ig-poverty-causes")

# =========================================================== 5.2.3 Policies
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Governments can use many policies to <b>alleviate poverty and redistribute income</b>: promoting <b>economic growth</b>, improved <b>education</b>, improved <b>healthcare</b>, more generous <b>state benefits</b>, <b>progressive taxation</b> and a <b>national minimum wage (NMW)</b>. <span class="kw">Redistribution of income</span> is the transfer of income from some people to others, usually by taxing the rich and spending on the poor. Each policy has advantages and costs: say how it raises the incomes or opportunities of the poor, then evaluate.</p></div>

  <h2>The six policies</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>How it reduces poverty</th><th>Possible problems</th></tr>
    <tr><td><b>Economic growth</b></td><td>More jobs and higher incomes; more tax revenue to spend on the poor</td><td>Gains may go to the rich; takes time; may harm the environment</td></tr>
    <tr><td><b>Improved education</b></td><td>Higher skills, productivity and wages; more job opportunities; better health knowledge</td><td>Costly; takes years; skills must match jobs; poor families may still not send children to school</td></tr>
    <tr><td><b>Improved healthcare</b></td><td>Healthier workers can earn; lower medical bills; less lost income</td><td>Costly; slow results</td></tr>
    <tr><td><b>More generous state benefits</b> (unemployment, pensions, child benefit)</td><td>Raise incomes of those who cannot work or earn little; reduce absolute poverty at once</td><td>Cost to taxpayers; may reduce incentive to work; benefits may be too small or poorly targeted</td></tr>
    <tr><td><b>Progressive taxation</b></td><td>Takes a larger share from the rich; the revenue pays for benefits and services for the poor</td><td>May reduce incentives to work, save and invest; high earners may avoid tax</td></tr>
    <tr><td><b>National minimum wage</b></td><td>Raises the pay of the lowest paid; narrows the gap</td><td>If above the equilibrium wage, firms may hire fewer workers; does not help those unable to work</td></tr>
  </table></div>

  <h2>Fiscal policy and poverty</h2>
  <p>Many of these are fiscal policy: government spending on education, healthcare, benefits, subsidised food and housing, financed by taxes. <b>Cutting government spending</b> or relying on <b>regressive taxes</b> (such as VAT) could <b>increase</b> poverty.</p>

  <h2>Other measures</h2>
  <ul>
    <li><b>Subsidies or free provision</b> of food, housing, school meals and water.</li>
    <li><b>Reducing regressive taxes</b> such as VAT on necessities.</li>
    <li><b>Lower interest rates and expansionary policy</b> can create jobs and reduce unemployment.</li>
    <li><b>Regional policy</b> and help for the unemployed to find work.</li>
  </ul>

  <h2>Evaluating</h2>
  <ul>
    <li><b>Cost and funding:</b> who pays, opportunity cost, deficits.</li>
    <li><b>Incentives:</b> high benefits or taxes may discourage work and enterprise; high minimum wages may cost jobs.</li>
    <li><b>Time lags:</b> education and growth take years; benefits work at once.</li>
    <li><b>Targeting:</b> does the help reach the poor?</li>
    <li><b>Absolute versus relative poverty:</b> growth and education help absolute poverty most; progressive taxes, benefits and the NMW help relative poverty.</li>
  </ul>
'''
js = HEAD + COMMON + '''
const QA = [16, 18, 20, 22, 24], QB = [4, 8, 14, 24, 50], QN = ["Poorest 20%", "Next 20%", "Middle 20%", "Next 20%", "Richest 20%"];
function quintChart(s) {
  const base = 320, k = 5; let o = SV.line(60, base, 710, base) + SV.text(60, 30, "Average income per head in each fifth of the population ($ thousand)", "sm");
  s.q.forEach((v, i) => { const x = 90 + i * 120, h = v * k; o += SV.rect(x, base - h, 90, h, "", { style: `fill:var(${i === 0 ? "--bad" : i === 4 ? "--accent" : "--muted"})`, opacity: 0.85 }) + SV.text(x + 45, base - h - 8, "$" + money(v, 0) + "k", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 45, base + 20, QN[i], "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  if (s.t) o += SV.text(380, 58, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
const AFTER = [10.75, 14.75, 14, 24, 35];
Lib.stepper($("#stX"), { w: 760, h: 400, label: "Progressive taxes and benefits", base: { q: QB, t: "" }, draw: quintChart, steps: [
  { cap: "Before government action income is <b>very unequal</b>: the richest fifth gets $50,000 a head, the poorest fifth only $4,000.", s: { q: QB, t: "Before tax and benefits" } },
  { cap: "A <b>progressive income tax</b> takes a larger share from high earners: the richest fifth now keeps about $35,000.", s: { q: [4, 8, 14, 24, 35], t: "After progressive tax on the rich" } },
  { cap: "The revenue pays <b>benefits and services</b> to the poorest two fifths. Their incomes rise to about $10,750 and $14,750. The gap narrows: <b>relative poverty falls</b>.", s: { q: AFTER, t: "After benefits: gap narrowed" } },
  { cap: "<b>Evaluate:</b> high tax rates may reduce incentives to work; benefits cost money; administration takes some revenue.", s: { q: AFTER, t: "" } },
] });
function nmwChart(s) {
  const w = s.w, ld = 110 - w, ls = w - 10; let o = axes("Wage", "Number of workers");
  o += curve(-1, 110, "c1", "Demand for labour", { t: "t1", dx: -90, dy: -12 }) + curve(1, 10, "c3", "Supply of labour", { t: "t3", dx: -100, dy: 14 });
  o += hline(60, "gr", 50) + vline(50, 60) + SV.circle(QX(50), PY(60), 6, "dot1") + ylab(60, "$60");
  if (s.m > 0.02) { o += `<g opacity="${s.m}">` + SV.line(QX(0), PY(w), QX(100), PY(w), "c2", { "stroke-width": 3 }) + SV.text(QX(100), PY(w) - 8, "Minimum wage $" + Math.round(w), "lbl bd t2", { "text-anchor": "end" }) + SV.line(QX(ld), PY(w), QX(ld), PY(0), "gr") + SV.line(QX(ls), PY(w), QX(ls), PY(0), "gr") + SV.circle(QX(ld), PY(w), 6, "dot2") + SV.circle(QX(ls), PY(w), 6, "dot2") + SV.text(QX(ld), PY(0) + 18, "Employed " + Math.round(ld), "sm bd", { "text-anchor": "middle" }) + SV.text(QX(ls), PY(0) + 18, "Want work " + Math.round(ls), "sm bd", { "text-anchor": "middle" }) + SV.text(QX((ld + ls) / 2), PY(w) + 22, "Unemployed: " + Math.round(ls - ld), "lbl bd t2", { "text-anchor": "middle", style: halo }) + "</g>"; }
  return o;
}
Lib.stepper($("#stN"), { w: 760, h: 400, label: "National minimum wage", base: { w: 80, m: 0 }, draw: nmwChart, steps: [
  { cap: "In a market for low-skilled labour the equilibrium wage is <b>$60</b> and <b>50</b> workers are employed.", s: { w: 80, m: 0 } },
  { cap: "The government sets a <b>national minimum wage of $80</b>, above the equilibrium wage. The low-paid who keep their jobs now earn <b>more</b>: this can reduce poverty.", s: { w: 80, m: 1 } },
  { cap: "But firms demand <b>fewer workers</b> (30) while more people want jobs (70). There are <b>40 unemployed</b>. Those who lose jobs may become poorer.", s: { w: 80, m: 1 } },
  { cap: "If the minimum wage were set <b>below $60</b> it would have no effect. <b>Evaluate:</b> the effect depends on the level, on how sensitive firms are, and it does not help those unable to work.", s: { w: 80, m: 1 } },
] });
const EDU = ["Government spends more on schools and training", "More children and adults gain skills and qualifications", "Workers become more productive", "They can get better-paid jobs and are less likely to be unemployed", "Household incomes rise above the poverty line", "Better health knowledge and the next generation also gain"];
Lib.stepper($("#stE"), { w: 760, h: 400, label: "How education reduces poverty", base: { n: 0 }, draw: mkChain(EDU, "--good"), steps: chainSteps(["The government <b>spends more on schools and training</b>.", "More people gain <b>skills and qualifications</b>.", "Workers become <b>more productive</b>.", "They find <b>better-paid jobs</b> and are less likely to be unemployed.", "<b>Household income rises</b> above the poverty line.", "<b>Evaluate:</b> it takes years and costs money, but it helps the next generation too."]) });

/* Lab 1: NMW */
function labN() {
  if (!$("#na")) return;
  const w = +$("#na").value, ld = Math.min(50, 110 - w), ls = Math.max(50, w - 10), un = w > 60 ? ls - ld : 0, wage = Math.max(60, w);
  $("#na1").textContent = "$" + wage; $("#na2").textContent = Math.round(ld); $("#na3").textContent = Math.round(un);
  $("#nav").textContent = w <= 60 ? `A minimum wage of $${w} is at or below the market wage of $60: it has no effect.` : `A minimum wage of $${w} raises pay for the ${Math.round(ld)} workers who keep jobs but ${Math.round(50 - ld)} jobs are lost and ${Math.round(un)} people are unemployed. Whether poverty falls depends on whether the gain to those in work outweighs the loss to those who lose jobs and on the size of the minimum wage.`;
  $("#labN").innerHTML = nmwChart({ w, m: 1 });
}
Lib.slider($("#g1"), { id: "na", label: "National minimum wage", min: 40, max: 100, step: 5, value: 80, fmt: (v) => "$" + v, onInput: labN });
/* Lab 2: tax and benefits */
function labT() {
  if (!$("#ta") || !$("#tb")) return;
  const t = +$("#ta").value / 100, eff = 1 - +$("#tb").value / 100, rev = QB[4] * t, pool = rev * eff * 5, q = QB.slice();
  q[4] = QB[4] - rev; q[0] = QB[0] + pool / 2; q[1] = QB[1] + pool / 2;
  $("#ta1").textContent = "$" + money(q[0], 1) + "k"; $("#ta2").textContent = "$" + money(q[4], 1) + "k"; $("#ta3").textContent = money(q[4] / q[0], 1) + " times";
  $("#tav").textContent = t === 0 ? "No tax on the richest fifth, so no redistribution. Raise the tax rate." : `The tax raises $${money(rev, 1)}k per rich person; after administration costs it is shared between the poorest two fifths. The poorest fifth rises from $4k to $${money(q[0], 1)}k and the gap falls from ${money(QB[4] / QB[0], 1)} to ${money(q[4] / q[0], 1)} times. ${t > 0.35 ? "At high rates, incentives to work and invest may fall, which is not shown here." : ""}`;
  $("#labT").innerHTML = quintChart({ q, t: "" });
}
Lib.slider($("#g2"), { id: "ta", label: "Progressive tax on the richest fifth", min: 0, max: 60, step: 5, value: 20, fmt: (v) => v + "%", onInput: labT });
Lib.slider($("#g3"), { id: "tb", label: "Share of revenue lost to administration", min: 0, max: 30, step: 5, value: 10, fmt: (v) => v + "%", onInput: labT });
const PO = [
  { n: "Economic growth", a: "Helps absolute poverty if the poor gain", w: "Jobs and incomes rise; tax revenue pays for services.", c: "Gains may go to the rich; slow; environmental cost." },
  { n: "Education", a: "Both, long run", w: "Skills raise productivity and wages.", c: "Costly; takes years; must match jobs." },
  { n: "Healthcare", a: "Both, long run", w: "Healthy people can work; lower medical costs.", c: "Costly; slow." },
  { n: "State benefits", a: "Absolute, immediately", w: "Direct income for those who cannot earn enough.", c: "Cost to taxpayers; may reduce incentives to work." },
  { n: "Progressive taxation", a: "Relative", w: "Takes more from the rich to fund help for the poor.", c: "May reduce incentives; tax avoidance." },
  { n: "National minimum wage", a: "Relative, for those in work", w: "Raises the pay of the lowest paid.", c: "May cause unemployment; no help for people who cannot work." },
];
button_table("poBtns", "poOut", PO, 0, (p) => `<div class="tw"><table class="t"><tr><th>Mainly helps</th><th>How it works</th><th>The catch</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>policy</b> is each?", buckets: [{ label: "Economic growth" }, { label: "Education or healthcare" }, { label: "Benefits or tax" }, { label: "Minimum wage" }], items: [
  { text: "Policies to raise real GDP and create jobs", b: 0 }, { text: "Investment to expand output and incomes", b: 0 },
  { text: "Free schooling and training", b: 1 }, { text: "Free or subsidised hospital care", b: 1 },
  { text: "Higher unemployment benefit", b: 2 }, { text: "A higher rate of tax on high incomes", b: 2 },
  { text: "A legal lowest hourly wage", b: 3 }, { text: "Raising the wage floor above the market wage", b: 3 },
], done: "Six policies in the syllabus." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>benefit</b> or a <b>cost / problem</b> of the policy?", buckets: [{ label: "Benefit" }, { label: "Cost or problem" }], items: [
  { text: "Raises the pay of the lowest-paid workers", b: 0 }, { text: "Gives income to people who cannot work", b: 0 }, { text: "Raises skills and productivity in the long run", b: 0 }, { text: "Narrows the gap between rich and poor", b: 0 },
  { text: "May cause unemployment among low-skilled workers", b: 1 }, { text: "Costs taxpayers more and may reduce incentives to work", b: 1 }, { text: "Takes years to have an effect", b: 1 }, { text: "High taxes may discourage effort and investment", b: 1 },
], done: "Every policy needs a cost: that is evaluation." });
Lib.match($("#m1"), { prompt: "Match the policy to how it reduces poverty.", pairs: [
  ["Education", "Raises skills so people earn more and find jobs"],
  ["Healthcare", "Healthier people can work and avoid medical bills"],
  ["State benefits", "Gives income to people who cannot earn enough"],
  ["Progressive taxation", "Takes more from the rich to pay for help for the poor"],
  ["National minimum wage", "Sets a floor under pay for the lowest paid"],
  ["Economic growth", "Creates jobs and raises incomes and tax revenue"],
], done: "Link each policy to a mechanism." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a cut in government spending might increase poverty</b>.", items: [
  "The government cuts spending on benefits, healthcare and education",
  "Poor households receive less income and fewer services",
  "Their income falls below what they need for basic necessities",
  "Reduced schooling and health care lower skills and productivity",
  "Households find it harder to earn: poverty rises and lasts longer",
], done: "Fiscal policy can reduce or raise poverty." });
''' + calc_js([
    ("The government raises a tax on the rich that brings in $2bn and spends it all on benefits for 1 million poor households. How much extra does each household get ($)?", 2000, "$2bn ÷ 1m = <b>$2,000</b>.", None, None),
    ("A minimum wage of $8 an hour is introduced and a worker works 40 hours. What is her weekly pay ($)?", 320, "8 × 40 = <b>$320</b>.", None, None),
    ("A progressive tax takes 10% of a $20,000 income and 40% of a $100,000 income. How much tax does the high earner pay ($)?", 40000, "40% × 100,000 = <b>$40,000</b>.", None, None),
    ("A benefit raises a poor household's income from $200 to $260 a week. By what percentage has it risen?", 30, "60 ÷ 200 × 100 = <b>30%</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which policy would most directly raise the incomes of unemployed people?", ["A cut in income tax for the rich", "An increase in unemployment benefit", "A rise in VAT", "A rise in interest rates"], 1, "Benefits transfer income to the unemployed."),
    ("A possible drawback of a national minimum wage is:", ["It lowers pay", "It may cause unemployment if set too high", "It increases benefits", "It cuts taxes"], 1, "Firms may hire fewer workers."),
    ("Which tax system is most likely to reduce relative poverty?", ["Regressive taxes", "Progressive taxes", "No taxes", "Flat taxes on necessities"], 1, "Higher rates on high earners fund help for the poor."),
    ("How can education reduce poverty?", ["It lowers productivity", "It raises skills and earnings", "It raises prices", "It reduces jobs"], 1, "Higher skills mean higher wages."),
    ("A cut in government spending on benefits is most likely to:", ["Reduce poverty", "Increase poverty", "Raise the minimum wage", "Have no effect"], 1, "Poor households lose income."),
]) + "\n" + cards_js([("Redistribution of income", "The transfer of income from some people to others, usually from richer to poorer."), ("State benefits", "Payments by the government, such as unemployment benefit and pensions."), ("Progressive tax", "A tax that takes a larger percentage of income from the rich than the poor."), ("National minimum wage", "A legal lowest rate of pay."), ("Education", "Learning that raises skills and productivity."), ("Healthcare provision", "Government spending on health services."), ("Economic growth", "A rise in real GDP over time."), ("Fiscal policy", "Government spending and taxation used to influence the economy."), ("Targeting", "Aiming help at the households that need it most.")]) + "labN(); labT();\n"
explore = '''
  <h2>Lab 1 · National minimum wage</h2>
  <p>The market wage for low-skilled labour is $60 with 50 workers. Set a minimum wage and see who gains and who loses.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Wage for those in work</small><strong id="na1"></strong></div><div><small>Jobs</small><strong id="na2"></strong></div><div><small>Unemployed because of it</small><strong id="na3"></strong></div></div><div class="verdict" id="nav"></div></div></div>
    <svg id="labN" viewBox="0 0 760 400" role="img" aria-label="Labour market with a minimum wage"></svg>
  </div>

  <h2>Lab 2 · Progressive tax and benefits</h2>
  <p>Tax the richest fifth and use the revenue to help the poorest two fifths. How much does the gap narrow?</p>
  <div class="card"><div class="grid2"><div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Poorest 20% get</small><strong id="ta1"></strong></div><div><small>Richest 20% keep</small><strong id="ta2"></strong></div><div><small>Richest ÷ poorest</small><strong id="ta3"></strong></div></div><div class="verdict" id="tav"></div></div></div>
    <svg id="labT" viewBox="0 0 760 350" role="img" aria-label="Income by fifth after tax and benefits"></svg>
  </div>

  <h2>Lab 3 · Policy picker</h2>
  <p>Pick a policy to see what it mainly helps, how it works and the catch.</p>
  <div class="card"><div class="row" id="poBtns"></div><div id="poOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define redistribution of income. (Oct/Nov 2021, P21)", "Transfer of income from some to others; tax the rich and spend on the poor.", "[K|Redistribution of income is the transfer of income from some people to others,] [K|for example taxing the rich and spending the revenue on the poor.]"),
    Q(2, "Explain", 4, "Explain two reasons why governments redistribute income. (Oct/Nov 2021, P21)", "Reduce poverty; equity; social problems; productivity.",
      "[K|One reason is to reduce poverty.] [N|Transferring income to poor households raises their purchasing power so they can afford basic necessities such as food, healthcare and housing.] [K|Another reason is to promote equity.] [N|Redistribution narrows the gap between rich and poor, which is seen as fairer and may reduce social problems.]"),
    Q(3, "Explain", 4, "Explain two ways a government could redistribute income. (Oct/Nov 2023, P22)", "Benefits; progressive taxes; free services.",
      "[K|A government could provide state benefits such as unemployment benefit.] [N|These raise the income of people with low or no income and help them afford basic necessities.] [K|It could use a progressive income tax system.] [N|This takes a higher proportion of the income of the rich, and the revenue can be spent to help those on low incomes.]"),
    Q(4, "Explain", 4, "Explain how having a more educated labour force can reduce poverty. (Oct/Nov 2023, P21)", "Skills, productivity, wages; job opportunities; health knowledge.",
      "[K|A more educated labour force is more skilled and productive.] [N|Firms are likely to pay higher wages, so workers can afford basic necessities.] [K|Better educated workers have more job opportunities and are less likely to be unemployed,] [N|so they may earn wages that are higher than unemployment benefits and move above the poverty line.]"),
    Q(5, "Analyse", 6, "Analyse why a cut in government spending might increase poverty. (Oct/Nov 2022, P22)", "Cuts to benefits, health, education; job losses in the public sector; lower AD.",
      "[K|A cut in government spending might reduce spending on benefits, healthcare and education.] [N|Poor households would receive less income and fewer services, so they could find it harder to afford basic necessities.] [N|Cuts to public sector jobs and contracts could raise unemployment, and lower spending reduces aggregate demand, so private firms may also cut jobs.] [N|Less education and healthcare reduce skills and health, so people find it harder to escape poverty.]", key=True),
    Q(6, "Discuss", 8, "Discuss whether or not a national minimum wage will reduce poverty. (May/June 2020, P21; Feb/Mar 2022, P22)", "For: raises pay of low-paid; reduces absolute and relative poverty. Against: set below market wage no effect; unemployment; does not help those unable to work; some receiving it are not poor.",
      "[K|A national minimum wage is a legal lowest rate of pay.] [N|If it is set above the equilibrium wage it will raise the pay of the low paid, which could reduce absolute poverty by letting them afford basic necessities and reduce relative poverty by narrowing the gap with higher earners.] [N|It may also raise employment if it motivates workers and raises demand.] [E|This is most likely if the wage is not too far above the market level.] [N|However, if it is set too high, firms' costs rise and they could hire fewer workers, so unemployment may rise and some of the poor lose their income.] [N|It does not help those who cannot work, and some people receiving it may not be in poor households.] [N|If it is set below the equilibrium wage it has no effect.] [E|Overall, a minimum wage is likely to reduce poverty among those in work if set at a sensible level, but it must be combined with other policies for the unemployed and those unable to work.]", key=True),
    Q(7, "Discuss", 8, "Discuss whether or not an increase in unemployment benefit payments would reduce poverty. (May/June 2023, P21)", "For: raises income at once; helps the unemployed afford necessities. Against: cost, may reduce incentive to look for work, may be small, does not help the low-paid.",
      "[K|Unemployment benefit is a payment by the government to people without work.] [N|An increase would raise the incomes of unemployed households straight away, so they could afford more food, housing and healthcare, and the extra spending could support demand.] [N|It could reduce absolute poverty among those who have lost their jobs, especially in a recession.] [E|The effect is largest where benefits are very low.] [N|However, higher benefits cost taxpayers and may require higher taxes or borrowing.] [N|If benefits are close to wages, some people may have less incentive to take a job, which could raise unemployment, and benefits do not help the working poor.] [E|Overall, higher unemployment benefit is likely to reduce poverty for the unemployed in the short run, but long-term solutions such as education and job creation may be needed.]", key=True),
    Q(8, "Discuss", 8, "Discuss whether or not fiscal policy is effective in reducing poverty. (Oct/Nov 2024, P21)", "For: spending on benefits, health, education; progressive taxes; subsidies. Against: costs and deficits; incentives; time lags; targeting; other policies (growth, supply-side).",
      "[K|Fiscal policy is the use of government spending and taxation to influence the economy.] [N|It can reduce poverty through spending on benefits, education and healthcare, which raise the incomes and skills of the poor, and through progressive taxes that take more from the rich.] [N|Subsidies or free provision of food and housing directly help poor households.] [E|These measures can act quickly, particularly benefits.] [N|However, spending needs funding, which could mean higher taxes or a bigger deficit, and high taxes and benefits could reduce incentives to work and invest.] [N|Education and healthcare take years to have an effect, and help may not reach those who most need it.] [E|Overall, fiscal policy is likely to be effective, particularly when well targeted, but it works best alongside policies that raise growth and employment, and its effect depends on the size of the measures and how they are funded.]", key=True),
)
tp = tips([
    ("Six policies:", "growth, education, healthcare, state benefits, progressive taxation, national minimum wage."),
    ("Explain the mechanism.", "'Education raises skills so wages rise' beats 'education helps'."),
    ("Absolute or relative?", "Growth and benefits help absolute poverty; progressive taxes and the NMW help relative poverty."),
    ("Always evaluate with a cost.", "Funding, incentives, unemployment, time lags, targeting."),
    ("Cutting spending can raise poverty.", "Fiscal policy works both ways."),
], cmds("Define", "Explain", "Analyse", "Discuss"))
body = page(CL("5.2.3 Policies to alleviate poverty and redistribute income"), "Policies to Alleviate Poverty and Redistribute Income", "Growth, education, healthcare, state benefits, progressive taxation and a national minimum wage: how each reduces poverty and the catches. Syllabus 5.2.3.",
    learn=learn, watch=watch(("Progressive taxes and benefits", "stX"), ("National minimum wage", "stN"), ("How education reduces poverty", "stE")), explore=explore,
    practise=practise(("Which policy?", "cl1", "card"), ("Benefit or cost?", "cl2", "card"), ("Match the policy", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("The UK's national living wage", "The UK introduced a national minimum wage in 1999 and raised it many times. Studies found raising pay for the low-paid with only small effects on employment, though results depend on the level.", "A minimum wage with a modest effect on jobs."),
        rw("Cash transfers in Brazil", "Brazil's Bolsa Familia paid poor families cash if their children attended school and had health check-ups. Extreme poverty fell and school attendance rose.", "Benefits linked to education and health, with targeting."),
        rw("Scandinavian welfare states", "Countries such as Denmark and Sweden use progressive taxes and generous benefits and have lower relative poverty than most others, but also high tax rates.", "Redistribution through tax and benefits and the cost."),
        rw("Austerity and poverty", "After 2010 some European governments cut benefits and public services to reduce deficits. Reports linked this to a rise in food bank use and child poverty.", "A cut in government spending increasing poverty.")),
    exam=ex, tips=tp)
write("po3", body, js, "Policies to Alleviate Poverty and Redistribute Income", "ig-poverty-policies")
