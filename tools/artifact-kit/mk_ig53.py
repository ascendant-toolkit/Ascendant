"""Builds the two IGCSE Economics 5.3 Population reviews (5.3.1, 5.3.2), written from scratch.
Run: python3 tools/artifact-kit/mk_ig53.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

PYR = '''
const PYR = {
  young: { n: "Young population (like Haiti or Niger)", b: [33, 27, 20, 14, 6] },
  mid: { n: "Middle-aged population (like Chile)", b: [20, 24, 24, 22, 10] },
  old: { n: "Ageing population (like Japan)", b: [12, 14, 16, 30, 28] },
};
const BANDS = ["0-14", "15-29", "30-44", "45-64", "65+"];
function pyrChart(b) {
  const cx = 380, k = 9, bh = 46; let o = SV.line(cx, 20, cx, 290) + SV.text(cx - 6, 14, "Male", "sm", { "text-anchor": "end" }) + SV.text(cx + 6, 14, "Female", "sm");
  b.forEach((v, i) => { const y = 250 - i * (bh + 6), w = (v / 2) * k; o += SV.rect(cx - w, y, w, bh, "", { style: `fill:var(${i === 0 || i === 4 ? "--warn" : "--accent"})`, opacity: 0.85 }) + SV.rect(cx, y, w, bh, "", { style: `fill:var(${i === 0 || i === 4 ? "--warn" : "--accent"})`, opacity: 0.85 }) + SV.text(cx - w - 8, y + bh / 2 + 4, v + "%", "sm bd", { "text-anchor": "end" }) + SV.text(cx + 330, y + bh / 2 + 4, BANDS[i], "sm"); });
  return o + SV.text(cx + 330, 300, "Age", "sm") + SV.text(60, 326, "Amber bars: dependants (0-14 and 65+). Blue: working age.", "sm");
}
'''

# =========================================================== 5.3.1 Factors
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A country's population changes for two reasons: <b>natural change</b> (births minus deaths) and <b>net migration</b> (people moving in minus people moving out). Economists use rates per 1,000 people so countries of different sizes can be compared. Birth rates, death rates and migration differ between countries because of income, healthcare, education, culture, jobs and safety.</p></div>

  <h2>Key definitions</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th></tr>
    <tr><td><b>Birth rate</b></td><td>The number of live births per 1,000 of the population in a year</td></tr>
    <tr><td><b>Death rate</b></td><td>The number of deaths per 1,000 of the population in a year</td></tr>
    <tr><td><b>Natural increase</b></td><td>Birth rate − death rate (per 1,000). Divide by 10 to get a percentage</td></tr>
    <tr><td><b>Immigration</b></td><td>People moving into a country to live</td></tr>
    <tr><td><b>Emigration</b></td><td>People leaving a country to live in another country</td></tr>
    <tr><td><b>Net migration</b></td><td>Immigration − emigration</td></tr>
    <tr><td><b>Population growth rate</b></td><td>Natural increase + net migration (as a percentage)</td></tr>
  </table></div>
  <div class="formula">Population change = (births − deaths) + (immigrants − emigrants)</div>

  <h2>Why birth rates differ between countries</h2>
  <div class="grid2">
    <div class="card"><h3>Higher birth rates</h3><ul><li>High infant mortality, so families have more children</li><li>Children help on farms and support parents in old age</li><li>Little access to contraception or family planning</li><li>Low education and employment for women</li><li>Cultural or religious preferences for large families</li><li>A young population has many people of child-bearing age</li></ul></div>
    <div class="card"><h3>Lower birth rates</h3><ul><li>Higher cost of raising children (education, housing)</li><li>More women in education and work, who delay or limit childbirth</li><li>Access to contraception</li><li>State pensions and welfare reduce the need for children</li><li>Low infant mortality</li><li>Ageing population: fewer women of child-bearing age</li></ul></div>
  </div>

  <h2>Why death rates differ</h2>
  <ul>
    <li><b>Income and living standards:</b> better food, housing and sanitation.</li>
    <li><b>Healthcare and medical technology:</b> vaccines, hospitals, clean water.</li>
    <li><b>Education:</b> health knowledge and nutrition.</li>
    <li><b>Age structure:</b> a country with many old people has a higher death rate even if healthcare is good.</li>
    <li><b>War, disease and disasters</b> (for example HIV, COVID-19, famine, earthquakes).</li>
    <li><b>Lifestyle</b> factors such as diet, smoking and accidents.</li>
  </ul>

  <h2>Migration: push and pull</h2>
  <div class="tw"><table class="t">
    <tr><th>Push factors (leaving)</th><th>Pull factors (arriving)</th></tr>
    <tr><td>Low wages and unemployment</td><td>Higher wages and more job opportunities</td></tr>
    <tr><td>War, persecution, political instability</td><td>Safety and stability</td></tr>
    <tr><td>Poverty and poor services</td><td>Better healthcare and education, higher living standards</td></tr>
    <tr><td>Natural disasters, drought</td><td>Family and friends already there</td></tr>
  </table></div>
  <p>People may also move <b>within</b> a country (<b>internal migration</b>), often from rural areas to cities. Young, skilled people are most likely to migrate, which can leave the home country with an older population and a loss of skilled workers (a <b>brain drain</b>).</p>

  <h2>Changes in the age and gender structure</h2>
  <p>The <b>age structure</b> shows the share of the population in each age group. A country can become an <b>ageing population</b> (a growing share aged 65 and over) because of:</p>
  <ul>
    <li>A <b>fall in the death rate</b> and rising life expectancy (better healthcare, nutrition, income).</li>
    <li>A <b>fall in the birth rate</b>, so fewer young people.</li>
    <li><b>Emigration of young people</b>.</li>
  </ul>
  <p><b>Gender structure:</b> a country may have more women than men because women tend to live longer, because men die in war or dangerous work, or because young men emigrate to work abroad.</p>
'''
js = HEAD + COMMON + PYR + '''
function natChart(s) {
  const x0 = 330, k = 16; let o = "";
  const row = (i, label, v, c, op) => { const y = 40 + i * 62, w = Math.abs(v) * k; return `<g opacity="${op}">` + SV.text(24, y + 24, label, "lbl bd", { "text-anchor": "start" }) + SV.rect(v >= 0 ? x0 : x0 + v * k, y, w, 38, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(v >= 0 ? x0 + w + 8 : x0 + v * k - 8, y + 25, (v >= 0 ? "" : "−") + Math.abs(v), "lbl bd", { "text-anchor": v >= 0 ? "start" : "end" }) + "</g>"; };
  o += SV.line(x0, 30, x0, 300);
  o += row(0, "Births per 1,000", 20, "--good", clamp(s.n, 0, 1)) + row(1, "Deaths per 1,000", -8, "--bad", clamp(s.n - 1, 0, 1)) + row(2, "Natural increase", 12, "--accent", clamp(s.n - 2, 0, 1)) + row(3, "Net migration", 2, "--warn", clamp(s.n - 3, 0, 1));
  o += `<g opacity="${clamp(s.n - 4, 0, 1)}">` + SV.text(380, 340, "Population change = 12 + 2 = 14 per 1,000 = 1.4% a year", "lbl bd t3", { "text-anchor": "middle", style: "font-size:17px" }) + "</g>";
  return o;
}
Lib.stepper($("#stN"), { w: 760, h: 380, label: "Natural increase and net migration", base: { n: 0 }, draw: natChart, steps: [
  { cap: "The <b>birth rate</b> is 20 live births per 1,000 people a year.", s: { n: 1 } },
  { cap: "The <b>death rate</b> is 8 deaths per 1,000 people a year.", s: { n: 2 } },
  { cap: "<b>Natural increase</b> = births − deaths = 20 − 8 = <b>12 per 1,000</b> (1.2%).", s: { n: 3 } },
  { cap: "<b>Net migration</b> = immigrants − emigrants = <b>+2 per 1,000</b>: more people moved in than left.", s: { n: 4 } },
  { cap: "The population grows by <b>14 per 1,000</b>, or <b>1.4%</b> a year. A negative figure for either part could make the population fall.", s: { n: 5 } },
] });
const dth = (t) => (t < 12 ? 36 : t < 45 ? 36 - 27 * (0.5 - 0.5 * Math.cos(((t - 12) / 33) * Math.PI)) : 9);
const brt = (t) => (t < 30 ? 38 : t < 85 ? 38 - 27 * (0.5 - 0.5 * Math.cos(((t - 30) / 55) * Math.PI)) : 11);
function dtmChart(s) {
  const X = (t) => 80 + t * 6.2, Y = (v) => 330 - v * 7; let o = SV.line(80, 340, 80, 40) + SV.line(80, 340, 710, 340) + SV.text(86, 34, "Rate per 1,000", "sm") + SV.text(710, 362, "Time as a country develops", "sm", { "text-anchor": "end" });
  const pts = [], pb = [], pd = []; for (let t = 0; t <= s.t; t += 1) { pb.push([X(t), Y(brt(t))]); pd.push([X(t), Y(dth(t))]); }
  if (pb.length > 1) { o += SV.poly(pb.concat(pd.slice().reverse()), "f1", { style: "fill:var(--accent);fill-opacity:0.18" }); o += SV.path(ptsPath(pb), "c2", { "stroke-width": 3 }) + SV.path(ptsPath(pd), "c4", { "stroke-width": 3 }); }
  if (pb.length > 1) o += SV.text(X(s.t) - 14, Y(brt(s.t)) - 18, "Birth rate", "lbl bd t2", { "text-anchor": "end" }) + SV.text(X(s.t) - 4, Y(dth(s.t)) + 20, "Death rate", "lbl bd t4", { "text-anchor": "end" });
  if (s.lbl) o += SV.text(X(s.t), 80, s.lbl, "lbl bd t3", { "text-anchor": s.t > 80 ? "end" : "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stD"), { w: 760, h: 400, label: "How birth and death rates change as a country develops", base: { t: 0, lbl: "" }, draw: dtmChart, steps: [
  { cap: "<b>Stage 1:</b> both rates are high. Many babies are born but many die (poor healthcare and food). The population grows slowly.", s: { t: 10, lbl: "Stage 1" } },
  { cap: "<b>Stage 2:</b> better healthcare, food and sanitation make the <b>death rate fall</b> quickly, but the birth rate stays high: <b>fast population growth</b> (the shaded gap).", s: { t: 32, lbl: "Stage 2" } },
  { cap: "<b>Stage 3:</b> as incomes and education rise, women have jobs, contraception is used and fewer babies die: the <b>birth rate falls</b>. The gap narrows.", s: { t: 65, lbl: "Stage 3" } },
  { cap: "<b>Stage 4:</b> both rates are low. Population growth is slow, and the population ages. Some countries now have birth rates below death rates. This is a simplified model: real countries vary.", s: { t: 100, lbl: "Stage 4" } },
] });
const AGE = ["Healthcare and nutrition improve: the death rate falls", "People live longer: life expectancy rises", "Meanwhile the birth rate falls (costs, careers, contraception)", "Fewer young people and more old people", "The share of the population aged 65+ rises: an ageing population"];
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Why populations age", base: { n: 0 }, draw: mkChain(AGE, "--warn"), steps: chainSteps(["<b>Healthcare and nutrition improve</b>: the death rate falls.", "<b>Life expectancy rises</b>: people live longer.", "Meanwhile the <b>birth rate falls</b>: fewer babies are born.", "There are <b>fewer young</b> and <b>more old</b> people.", "<b>An ageing population:</b> the share aged 65+ rises. Emigration of the young can add to this."]) });

/* Lab 1: population calculator */
function labP() {
  if (!$("#pa") || !$("#pb") || !$("#pc") || !$("#pd") || !$("#pe")) return;
  const P0 = +$("#pa").value, b = +$("#pb").value, d = +$("#pc").value, im = +$("#pd").value, em = +$("#pe").value, nat = b - d, net = im - em, g = (nat + net) / 10;
  $("#pa1").textContent = (nat >= 0 ? "+" : "") + nat + " per 1,000"; $("#pa2").textContent = (net >= 0 ? "+" : "") + net + " per 1,000"; $("#pa3").textContent = (g >= 0 ? "+" : "") + money(g, 1) + "%";
  const pop = [P0]; for (let i = 1; i <= 6; i++) pop.push(pop[i - 1] * Math.pow(1 + g / 100, 5));
  $("#pav").textContent = `Natural increase = ${b} − ${d} = ${nat} per 1,000. Net migration = ${im} − ${em} = ${net}. Total change = ${nat + net} per 1,000 = ${money(g, 1)}% a year, so the population goes from ${P0}m to about ${money(pop[6], 1)}m in 30 years. ${g < 0 ? "The population is falling." : ""}`;
  const base = 290, mx = Math.max(...pop), mn = Math.min(...pop), lo = Math.min(P0 * 0.5, mn * 0.9), k = 230 / Math.max(1, mx - lo); let o = SV.line(60, base, 700, base);
  pop.forEach((v, i) => { const x = 90 + i * 90, h = (v - lo) * k + 10; o += SV.rect(x, base - h, 60, h, "", { style: `fill:var(${g >= 0 ? "--accent" : "--bad"})`, opacity: 0.85 }) + SV.text(x + 30, base - h - 8, money(v, 0) + "m", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 30, base + 20, i ? "Year " + i * 5 : "Now", "sm", { "text-anchor": "middle" }); });
  $("#labP").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pa", label: "Population today (millions)", min: 10, max: 100, step: 5, value: 50, fmt: (v) => v + "m", onInput: labP });
Lib.slider($("#g2"), { id: "pb", label: "Birth rate (per 1,000)", min: 8, max: 45, step: 1, value: 20, fmt: (v) => v, onInput: labP });
Lib.slider($("#g3"), { id: "pc", label: "Death rate (per 1,000)", min: 4, max: 25, step: 1, value: 8, fmt: (v) => v, onInput: labP });
Lib.slider($("#g4"), { id: "pd", label: "Immigration (per 1,000)", min: 0, max: 15, step: 1, value: 3, fmt: (v) => v, onInput: labP });
Lib.slider($("#g5"), { id: "pe", label: "Emigration (per 1,000)", min: 0, max: 15, step: 1, value: 1, fmt: (v) => v, onInput: labP });
/* Lab 2: age structure */
let selA = "young";
function labA() {
  const t = PYR[selA]; $("#paBtns").innerHTML = Object.keys(PYR).map((k) => `<button class="b${k === selA ? " pri" : ""}" data-k="${k}">${PYR[k].n}</button>`).join("");
  $$("#paBtns .b").forEach((b) => (b.onclick = () => { selA = b.dataset.k; labA(); }));
  const y = t.b[0], o = t.b[4], w = 100 - y - o, dep = (y + o) / w;
  $("#paOut").innerHTML = `<div class="tw"><table class="t"><tr><th>Aged 0-14</th><th>Working age (15-64)</th><th>Aged 65+</th><th>Dependency ratio</th></tr><tr><td>${y}%</td><td>${w}%</td><td>${o}%</td><td>${money(dep, 2)} dependants per worker</td></tr></table></div><p class="note">Illustrative shares. A young structure has many children to support; an ageing one has many pensioners.</p>`;
  $("#labA").innerHTML = pyrChart(t.b);
}
const PP = [
  { n: "Low wages and unemployment at home", t: "Push", e: "People leave to find work and higher pay abroad." },
  { n: "War or persecution", t: "Push", e: "People flee for safety (refugees)." },
  { n: "Natural disaster or drought", t: "Push", e: "Farms and homes destroyed; people move to survive." },
  { n: "Higher wages abroad", t: "Pull", e: "Migrants gain more income, and can send money home." },
  { n: "Better healthcare and education abroad", t: "Pull", e: "Migrants and their children can access better services." },
  { n: "Family already living abroad", t: "Pull", e: "Support with housing, jobs and settling in." },
  { n: "Political stability and rights", t: "Pull", e: "Safe, predictable conditions to live and work." },
];
button_table("ppBtns", "ppOut", PP, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>How it affects migration</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each factor <b>raise</b> or <b>lower</b> the birth rate?", buckets: [{ label: "Raises birth rate" }, { label: "Lowers birth rate" }], items: [
  { text: "High infant mortality", b: 0 }, { text: "Children are needed to work the farm and support parents", b: 0 }, { text: "Little access to contraception", b: 0 }, { text: "Large share of women of child-bearing age", b: 0 },
  { text: "More women in higher education and work", b: 1 }, { text: "State pensions reduce the need for children", b: 1 }, { text: "Higher cost of raising children", b: 1 }, { text: "Wide use of contraception", b: 1 },
], done: "Think about cost, education, income and need for children." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>push</b> factor or a <b>pull</b> factor for migration?", buckets: [{ label: "Push" }, { label: "Pull" }], items: [
  { text: "High unemployment at home", b: 0 }, { text: "War in the home country", b: 0 }, { text: "Drought destroys crops", b: 0 }, { text: "Very low wages", b: 0 },
  { text: "Higher wages in another country", b: 1 }, { text: "Better schools and hospitals abroad", b: 1 }, { text: "Relatives already living there", b: 1 }, { text: "A safe, stable society", b: 1 },
], done: "Push: reasons to leave. Pull: reasons to go." });
Lib.classify($("#cl3"), { prompt: "Does each lead to an <b>ageing population</b>?", buckets: [{ label: "Leads to ageing" }, { label: "Does not" }], items: [
  { text: "Fall in the death rate and higher life expectancy", b: 0 }, { text: "Fall in the birth rate", b: 0 }, { text: "Emigration of young adults", b: 0 }, { text: "Better healthcare for older people", b: 0 },
  { text: "A rise in the birth rate", b: 1 }, { text: "Large immigration of young workers", b: 1 }, { text: "A rise in infant deaths", b: 1 }, { text: "More young families moving in", b: 1 },
], done: "Fewer young, longer lives, or young people leaving." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Birth rate", "Live births per 1,000 of the population in a year"],
  ["Death rate", "Deaths per 1,000 of the population in a year"],
  ["Immigration", "People moving into a country to live"],
  ["Emigration", "People leaving a country to live in another"],
  ["Net migration", "Immigration minus emigration"],
  ["Life expectancy", "The average number of years a newborn is expected to live"],
], done: "Good vocabulary scores marks." });
''' + calc_js([
    ("A country has a birth rate of 24 and a death rate of 9 per 1,000. What is its natural increase (per 1,000)?", 15, "24 − 9 = <b>15 per 1,000</b>.", None, None),
    ("Immigration is 4 per 1,000 and emigration is 7 per 1,000. What is net migration (per 1,000)?", -3, "4 − 7 = <b>−3 per 1,000</b>: more people leave than arrive.", None, None),
    ("Natural increase is 15 per 1,000 and net migration is −3 per 1,000. What is the population growth rate (%)?", 1.2, "(15 − 3) ÷ 10 = <b>1.2%</b>.", None, 0.01),
    ("A country has 40 million people and a birth rate of 15 per 1,000. How many babies are born in a year (thousands)?", 600, "40,000 × 15 = <b>600 thousand</b> (0.6 million).", "40 million = 40,000 thousand.", None),
    ("A country's population is 8.5 million of which 2.2 million are foreign nationals. What percentage are foreign nationals (1 d.p.)?", 25.9, "2.2 ÷ 8.5 × 100 = <b>25.9%</b>.", None, 0.1),
]) + mcq_js("qz1", [
    ("What is the birth rate?", ["Total number of babies born", "Live births per 1,000 of the population in a year", "Babies born per family", "Births per 100 people"], 1, "A rate per 1,000."),
    ("Net migration is:", ["Immigration + emigration", "Immigration − emigration", "Births − deaths", "Population ÷ area"], 1, "Arrivals minus departures."),
    ("Which could cause a fall in the death rate?", ["Better healthcare", "A war", "A famine", "A new epidemic"], 0, "Fewer deaths from illness."),
    ("Which is a pull factor for migration?", ["War", "Unemployment at home", "Higher wages abroad", "Drought"], 2, "A reason to move to a country."),
    ("Which could cause a fall in the birth rate?", ["Fewer women in education", "Higher cost of raising children", "Higher infant mortality", "No contraception"], 1, "Costs discourage large families."),
]) + "\n" + cards_js([("Birth rate", "The number of live births per 1,000 of the population in a year."), ("Death rate", "The number of deaths per 1,000 of the population in a year."), ("Natural increase", "The birth rate minus the death rate."), ("Immigration", "People moving into a country to live."), ("Emigration", "People leaving a country to live in another country."), ("Net migration", "Immigration minus emigration."), ("Life expectancy", "The average number of years a newborn is expected to live."), ("Ageing population", "A rising share of the population aged 65 and over."), ("Dependency ratio", "The number of dependants (young and old) compared with the working-age population."), ("Push and pull factors", "Reasons for leaving a place (push) and reasons for moving to another (pull)."), ("Internal migration", "People moving from one part of a country to another."), ("Brain drain", "The emigration of skilled and educated workers.")]) + "labP(); labA();\n"
explore = '''
  <h2>Lab 1 · Population change calculator</h2>
  <p>Set the birth rate, death rate and migration (per 1,000 people). See the growth rate and what the population could be in 30 years.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div><div id="g5"></div></div>
    <div><div class="readout"><div><small>Natural increase</small><strong id="pa1"></strong></div><div><small>Net migration</small><strong id="pa2"></strong></div><div><small>Growth rate</small><strong id="pa3"></strong></div></div><div class="verdict" id="pav"></div></div></div>
    <svg id="labP" viewBox="0 0 760 330" role="img" aria-label="Projected population"></svg>
  </div>

  <h2>Lab 2 · Age structure</h2>
  <p>Pick a type of population. A young structure has a wide base; an ageing one is wide at the top.</p>
  <div class="card"><div class="row" id="paBtns" style="margin-bottom:10px"></div><svg id="labA" viewBox="0 0 760 335" role="img" aria-label="Population pyramid"></svg><div id="paOut"></div></div>

  <h2>Lab 3 · Push and pull factors</h2>
  <p>Pick a factor to see whether it pushes people out or pulls them in.</p>
  <div class="card"><div class="row" id="ppBtns"></div><div id="ppOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define birth rate. (May/June 2021, P22)", "Live births, per 1,000, in a year.", "[K|The birth rate is the number of live births per 1,000 of the population] [K|in a year.]", warn="Giving only the number of births. It must be per 1,000."),
    Q(2, "Define", 2, "Define emigration. (May/June 2023, P23)", "Leaving a country to live in another.", "[K|Emigration is when people leave a country] [K|to live in another country.]"),
    Q(3, "Identify", 2, "Identify two reasons why death rates may vary between countries. (May/June 2023, P21)", "Differences in income, healthcare, education, nutrition, average age, disease. Not population size.", "[K|Differences in healthcare.] [K|Differences in income or standard of living (or nutrition, education, average age).]"),
    Q(4, "Explain", 4, "Explain two causes of a decrease in the death rate. (May/June 2020, P22)", "Income, education, healthcare, end of war, each with a link.",
      "[K|One cause is better healthcare.] [N|Advances in medical technology, vaccines and more hospitals mean people survive illnesses that were once fatal, so deaths per 1,000 fall.] [K|Another cause is a rise in income.] [N|People can afford better food, housing and sanitation, which improves their health and reduces the number of deaths.]"),
    Q(5, "Explain", 4, "Explain two causes of a fall in the birth rate. (Oct/Nov 2020, P23)", "Cost of children, women's education and work, state pensions, contraception, lower infant mortality.",
      "[K|A rise in the education of women is one cause.] [N|Educated women may be more likely to enter employment and delay having children, so fewer babies are born.] [K|Another is greater access to contraception.] [N|This makes family planning more effective, so couples can choose to have fewer children.]"),
    Q(6, "Explain", 4, "Explain two causes of an ageing population. (May/June 2021, P21)", "Fall in the death rate or higher life expectancy; fall in the birth rate; emigration of young people.",
      "[K|A fall in the death rate and rise in life expectancy is one cause.] [N|Better healthcare, nutrition and incomes mean people live longer, so the share of older people rises.] [K|A fall in the birth rate is another.] [N|If fewer babies are born because of higher costs of raising children or more women working, the proportion of older people in the population rises.]"),
    Q(7, "Explain", 4, "Explain two reasons why emigration from a country may increase. (Oct/Nov 2020, P22)", "Push factors: unemployment, low wages, conflict, disasters; pull factors abroad.",
      "[K|High unemployment and low wages at home are one reason.] [N|People may emigrate to countries where they can find jobs and earn higher incomes, so more leave.] [K|War or political instability is another.] [N|People may leave to find safety, increasing emigration.]"),
    Q(8, "Analyse", 6, "Analyse the causes of migration between countries. (Oct/Nov 2024, P23)", "Pull factors (wages, jobs, services, family); push factors; each with a link. Identifying alone is capped at 3 marks.",
      "[K|People may migrate to countries with higher wages and more job opportunities.] [N|This raises their income and the goods and services they can consume, so their standard of living rises.] [N|They may also move to gain better healthcare or education, to improve life expectancy and the job prospects of their children.] [N|Push factors such as unemployment, low pay, war or natural disasters at home may force people to leave.] [N|Some move to join family members already abroad, which makes settling in easier.] [E|The importance of each depends on the migrant and on the country.]", key=True),
)
tp = tips([
    ("Rates are per 1,000.", "Say 'per 1,000' in every definition."),
    ("Natural increase = births − deaths. Net migration = immigration − emigration.", "Add them for total change."),
    ("Give a reason and a link.", "'Better healthcare, so fewer people die.'"),
    ("Use push and pull for migration.", "Say what pushes people out and what pulls them in."),
    ("Ageing: lower death rate, lower birth rate, young people leaving.", "Three causes to remember."),
], cmds("Define", "Identify", "Explain", "Analyse"))
body = page(CL("5.3.1 Factors that affect population growth"), "Factors that Affect Population Growth", "Birth rates, death rates and migration, why they vary between countries, and what changes the age and gender structure of a population. Syllabus 5.3.1.",
    learn=learn, watch=watch(("Natural increase and net migration", "stN"), ("How birth and death rates change as a country develops", "stD"), ("Why populations age", "stA")), explore=explore,
    practise=practise(("Raises or lowers the birth rate?", "cl1", "card"), ("Push or pull?", "cl2", "card"), ("Does it lead to an ageing population?", "cl3", "card"), ("Match the term", "m1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Niger and Japan", "Niger has one of the highest birth rates in the world, with an average of around six or seven children per woman, while Japan's birth rate is very low and its population is falling.", "Why birth rates differ: income, education, infant mortality and cost of children."),
        rw("Romania's falling population", "A past paper notes that Romania's population fell between 1990 and 2022, because of a low birth rate and emigration of workers to other EU countries.", "Natural change and net migration both negative."),
        rw("The UAE's foreign workers", "Most residents of the United Arab Emirates are foreign nationals who migrated for work. A past paper asks for the percentage of foreign nationals.", "Immigration pulled by jobs and higher wages."),
        rw("Refugees from conflict", "Millions of Syrians left their country after 2011 because of war, an example of push factors causing emigration.", "Push factors: war and persecution."),
        rw("COVID-19 and death rates", "The pandemic raised death rates in many countries in 2020 and 2021, particularly among the old.", "Disease affecting the death rate and age structure.")),
    exam=ex, tips=tp)
write("pp1", body, js, "Factors that Affect Population Growth", "ig-population-factors")

# =========================================================== 5.3.2 Effects
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The <span class="kw">optimum population</span> is the size of population that produces the <b>highest output (income) per head</b> given a country's resources, capital and technology. Below it the country is <b>underpopulated</b>; above it, <b>overpopulated</b>. Changes in population size and in the age and gender structure affect output, the labour force, public spending and living standards. Always say whether the effect is good or bad, who it affects and what it depends on.</p></div>

  <h2>Optimum, under- and over-population</h2>
  <div class="tw"><table class="t">
    <tr><th>Situation</th><th>What it means</th><th>Effect of more people</th></tr>
    <tr><td><b>Underpopulation</b></td><td>Too few people to use the resources fully</td><td>Output per head rises (more workers, specialisation, bigger market)</td></tr>
    <tr><td><b>Optimum population</b></td><td>Output per head is highest</td><td>Neither more nor fewer people raises output per head</td></tr>
    <tr><td><b>Overpopulation</b></td><td>Too many people for the resources and capital available</td><td>Output per head falls (pressure on land, housing, jobs, services)</td></tr>
  </table></div>
  <p class="note">The optimum is <b>not fixed</b>: new technology, more capital and better education <b>raise</b> it, so a country can support more people at a high income. Using up resources or climate change can lower it.</p>

  <h2>Effects of an increase in population size</h2>
  <div class="grid2">
    <div class="card"><h3>Possible benefits</h3><ul><li>Larger <b>labour force</b> and a bigger market for firms (more demand)</li><li>Economies of scale and more specialisation</li><li>More tax revenue and a younger, adaptable workforce</li><li>Higher growth if the country was underpopulated; more entrepreneurs and ideas</li></ul></div>
    <div class="card"><h3>Possible costs</h3><ul><li>Pressure on resources, food, housing, water and land; more pollution</li><li>More spending needed on schools, hospitals and infrastructure</li><li>Unemployment if jobs do not grow; lower wages</li><li>Lower output per head if the country is overpopulated</li></ul></div>
  </div>
  <p>On diagrams: a bigger population increases <b>demand</b> in markets (housing, food, clothing, toys: demand shifts right, price rises), increases the <b>supply of labour</b> (wages may fall) and could shift the <b>PPC outwards</b> as more labour is available.</p>

  <h2>Effects of a decrease in population size</h2>
  <div class="grid2">
    <div class="card"><h3>Possible benefits</h3><ul><li>Less pressure on resources, housing, congestion and pollution</li><li>Higher output per head if the country was overpopulated</li><li>Fewer dependants to support if the cause is a fall in children</li></ul></div>
    <div class="card"><h3>Possible costs</h3><ul><li>Smaller labour force, labour shortages and less demand</li><li>Lower tax revenue and slower growth; PPC shifts inwards</li><li>An ageing population if caused by a lower birth rate or emigration of the young</li><li>Pressure to cut services, empty areas</li></ul></div>
  </div>

  <h2>Age structure</h2>
  <div class="tw"><table class="t">
    <tr><th>Structure</th><th>Possible advantages</th><th>Possible disadvantages</th></tr>
    <tr><td><b>Young population</b> (large share under 15)</td><td>Future labour force; adaptable and innovative workers; demand for goods; low pension costs</td><td>High <b>dependency ratio</b> now; spending on schools and childcare; need jobs for a large number of young people</td></tr>
    <tr><td><b>Ageing population</b> (large share aged 65+)</td><td>Experienced workers; demand for leisure, healthcare and related industries; volunteers and savings</td><td>Pensions and healthcare costs; higher taxes or borrowing; labour shortages; slower growth; less spending on durable goods; fewer people save as they retire</td></tr>
  </table></div>
  <div class="formula">Dependency ratio = (population aged 0 to 14 + aged 65 and over) ÷ population aged 15 to 64</div>
  <p><b>Spending and saving:</b> older people usually have lower incomes and spend more of it on healthcare and essentials and less on new goods, and many draw down their savings, so national saving falls as the share of older people rises, while working-age people may save more for retirement.</p>

  <h2>Gender structure</h2>
  <p>A population with <b>more women than men</b> (or the reverse) can affect the labour force, birth rates and demand for goods and services. A shortage of men of working age (through war or emigration) can reduce the labour force; a shortage of women could reduce future birth rates.</p>
'''
js = HEAD + COMMON + PYR + '''
function optChart(s) {
  const T = s.T, Ls = 40 * T, Ym = 20 * T, f = (L) => Math.max(0, Ym * (1 - Math.pow((L - Ls) / (Ls + 20), 2))), X = (L) => 80 + L * 6, Y = (v) => 330 - v * 6.2;
  let o = SV.line(80, 340, 80, 40) + SV.line(80, 340, 710, 340) + SV.text(86, 48, "Output per head", "sm") + SV.text(710, 362, "Population size", "sm", { "text-anchor": "end" });
  const pts = []; for (let L = 4; L <= 100; L += 2) pts.push([X(L), Y(f(L))]);
  o += SV.path(ptsPath(pts), "c1", { "stroke-width": 3 }) + SV.line(X(Ls), Y(Ym), X(Ls), 340, "dash", { style: "stroke:var(--good);stroke-width:2" }) + SV.text(X(Ls), 358, "Optimum", "sm bd", { "text-anchor": "middle" });
  o += SV.circle(X(s.L), Y(f(s.L)), 8, Math.abs(s.L - Ls) < 4 ? "dot3" : "dot2");
  const st = Math.abs(s.L - Ls) < 5 ? "Optimum population" : s.L < Ls ? "Underpopulated" : "Overpopulated";
  o += SV.text(X(s.L), Y(f(s.L)) - 18, st, "lbl bd t2", { "text-anchor": "middle", style: halo });
  return o;
}
Lib.stepper($("#stO"), { w: 760, h: 400, label: "Under-population, optimum and over-population", base: { L: 15, T: 1 }, draw: optChart, steps: [
  { cap: "The country is <b>underpopulated</b>: there are too few people to use its land and resources. Output per head is low and <b>more people would raise it</b>.", s: { L: 15, T: 1 } },
  { cap: "As population grows to the <b>optimum</b>, workers specialise, markets grow and output per head <b>reaches its maximum</b>.", s: { L: 40, T: 1 } },
  { cap: "Beyond the optimum the country is <b>overpopulated</b>: too many people share the same land and capital. Output per head <b>falls</b>.", s: { L: 75, T: 1 } },
  { cap: "New <b>technology, capital and education</b> raise the optimum. The same population is now closer to the optimum, with higher output per head: the optimum is <b>not fixed</b>.", s: { L: 75, T: 1.8 } },
] });
function ppcChart(s) {
  const ox = 90, oy = 330, X = 250 * s.s, Y = 215 * s.s, X0 = 250, Y0 = 215;
  const curve = (X, Y) => { const p = []; for (let t = 0; t <= 90; t += 5) { const r = (t * Math.PI) / 180; p.push([ox + X * Math.cos(r), oy - Y * Math.sin(r)]); } return p; };
  let o = SV.line(ox, oy, ox, 30) + SV.line(ox, oy, 700, oy) + SV.text(ox + 6, 40, "Capital goods", "sm") + SV.text(700, oy + 24, "Consumer goods", "sm", { "text-anchor": "end" });
  if (Math.abs(s.s - 1) > 0.02) o += SV.path(ptsPath(curve(X0, Y0)), "c3", { opacity: 0.4 }) + SV.text(ox + X0 * Math.cos(0.9) + 6, oy - Y0 * Math.sin(0.9) - 8, "PPC", "lbl bd t3", { opacity: 0.6 });
  o += SV.path(ptsPath(curve(X, Y)), "c1") + SV.text(ox + X * 0.7071 + 12, oy - Y * 0.7071 - 6, Math.abs(s.s - 1) > 0.02 ? "PPC₁" : "PPC", "lbl bd t1");
  const px = ox + X * 0.7071, py = oy - Y * 0.7071; o += SV.line(px, py, px, oy, "gr") + SV.line(ox, py, px, py, "gr") + SV.circle(px, py, 7, s.s > 1.02 ? "dot2" : s.s < 0.98 ? "dot4" : "dot1");
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Population change and the PPC", base: { s: 1 }, draw: ppcChart, steps: [
  { cap: "The PPC shows the most the economy can produce with its <b>labour</b>, capital and land.", s: { s: 1 } },
  { cap: "<b>An increase in the labour force</b> (from higher births or immigration) means more can be produced: the PPC shifts <b>outwards</b> to PPC₁. Total output could rise.", s: { s: 1.2 } },
  { cap: "<b>A fall in the population</b> (emigration, a falling birth rate) reduces the labour force: the PPC shifts <b>inwards</b> to PPC₁. The economy can produce less in total.", s: { s: 0.8 } },
  { cap: "<b>Evaluate:</b> total output may fall but output <b>per head</b> may rise if the country was overpopulated. It depends on whether the people leaving are skilled workers.", s: { s: 0.8 } },
] });
function dsChart(s) {
  const d = s.d; let o = axes("Price", "Quantity") + curve(-1, 110, "c1", "D", { t: "t1", attrs: { opacity: d > 1 ? 0.4 : 1 } }) + curve(1, 10, "c3", "S", { t: "t3" });
  if (d > 1) o += curve(-1, 110 + d, "c2", "D₁", { t: "t2" });
  const q0 = 50, p0 = 60, q1 = (100 + d) / 2, p1 = 60 + d / 2;
  o += hline(p0, "gr", q0) + vline(q0, p0) + SV.circle(QX(q0), PY(p0), 6, "dot1", { opacity: d > 1 ? 0.5 : 1 }) + ylab(p0, "P") + xlab(q0, "Q");
  if (d > 1) o += hline(p1, "gr", q1) + vline(q1, p1) + SV.circle(QX(q1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(q1, "Q₁", "sm bd");
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 400, label: "A bigger population and the market for clothing", base: { d: 0 }, draw: dsChart, steps: [
  { cap: "The market for <b>clothing</b> is in equilibrium at price <b>P</b> and quantity <b>Q</b>.", s: { d: 0 } },
  { cap: "The <b>population increases</b> (more births or immigration). More people want clothes at each price, so <b>demand shifts right</b> to D₁.", s: { d: 24 } },
  { cap: "The new equilibrium has a <b>higher price (P₁)</b> and <b>higher quantity (Q₁)</b>. Firms in the market could earn more revenue and expand. (The same applies to housing, food and toys.)", s: { d: 24 } },
] });
const ACH = ["The share of the population aged 65+ rises", "The dependency ratio rises: fewer workers per pensioner", "Pension and healthcare spending rise; tax revenue grows more slowly", "The government raises taxes, borrows more or cuts other spending", "A smaller labour force may slow growth and productivity", "Evaluation: later retirement, immigration and technology can ease the strain"];
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Effects of an ageing population", base: { n: 0 }, draw: mkChain(ACH, "--warn"), steps: chainSteps(["The <b>share aged 65+ rises</b>.", "The <b>dependency ratio rises</b>: fewer workers support each pensioner.", "<b>Pension and healthcare spending rise</b>; tax revenue grows more slowly.", "The government <b>raises taxes, borrows more or cuts other spending</b>.", "A smaller labour force may <b>slow growth and productivity</b>.", "<b>Evaluate:</b> later retirement, immigration, higher productivity and automation can ease the strain."]) });

/* Lab 1: optimum population */
function labO() {
  if (!$("#oa") || !$("#ob")) return;
  const L = +$("#oa").value, T = +$("#ob").value / 100, Ls = 40 * T, Ym = 20 * T, f = Math.max(0, Ym * (1 - Math.pow((L - Ls) / (Ls + 20), 2)));
  $("#oa1").textContent = "$" + money(f, 1) + "k"; $("#oa2").textContent = Math.round(Ls) + "m"; $("#oa3").textContent = Math.abs(L - Ls) < 5 ? "Optimum" : L < Ls ? "Under" : "Over";
  $("#oav").textContent = Math.abs(L - Ls) < 5 ? `At ${L}m people, output per head is close to its maximum of $${money(Ym, 1)}k.` : L < Ls ? `With ${L}m people the country is underpopulated: more people would raise output per head towards $${money(Ym, 1)}k at ${Math.round(Ls)}m.` : `With ${L}m people the country is overpopulated: output per head is only $${money(f, 1)}k. Fewer people (or better technology) would help.`;
  $("#labO").innerHTML = optChart({ L, T });
}
Lib.slider($("#g1"), { id: "oa", label: "Population (millions)", min: 10, max: 100, step: 5, value: 20, fmt: (v) => v + "m", onInput: labO });
Lib.slider($("#g2"), { id: "ob", label: "Technology and capital (100 = today)", min: 100, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labO });
/* Lab 2: dependency */
function labD() {
  if (!$("#da") || !$("#db")) return;
  const y = +$("#da").value, o = +$("#db").value, w = 100 - y - o, dep = (y + o) / w, per = w / o;
  $("#da1").textContent = w + "%"; $("#da2").textContent = money(dep, 2); $("#da3").textContent = money(per, 1);
  $("#dav").textContent = `${y}% are children and ${o}% are 65 or over, so ${w}% are of working age. There are ${money(dep, 2)} dependants for each worker, and ${money(per, 1)} workers for each person aged 65+. ${o > 22 ? "A high share of old people means high pension and healthcare costs." : y > 30 ? "A high share of children means high spending on schools, but a large future workforce." : ""}`;
  const base = 290; let g = SV.line(60, base, 700, base);
  [["Aged 0-14", y, "--warn"], ["Working age", w, "--accent"], ["Aged 65+", o, "--bad"]].forEach(([n, v, c], i) => { const x = 130 + i * 190, h = v * 3.2; g += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, v + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 20, n, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = g;
}
Lib.slider($("#g3"), { id: "da", label: "Share of the population aged 0 to 14", min: 10, max: 45, step: 1, value: 20, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g4"), { id: "db", label: "Share of the population aged 65 and over", min: 3, max: 35, step: 1, value: 15, fmt: (v) => v + "%", onInput: labD });
const EF = [
  { n: "A rapidly growing population", b: "Bigger labour force and market; more future workers.", c: "Pressure on food, housing and services; more dependants; possible overpopulation and lower output per head." },
  { n: "A falling population", b: "Less pressure on resources and the environment.", c: "Fewer workers and customers; ageing; lower tax revenue and growth." },
  { n: "A young population", b: "Large future workforce; adaptable; lower pension costs.", c: "High dependency now; need schools and jobs." },
  { n: "An ageing population", b: "Experienced workers; demand for healthcare and leisure.", c: "Pensions and healthcare costs; labour shortages; slower growth." },
  { n: "Large-scale immigration", b: "More workers and skills; more tax revenue; younger population.", c: "Pressure on housing and services; wages may fall for some; brain drain from the home country." },
  { n: "Large-scale emigration", b: "Remittances sent home; less unemployment.", c: "Loss of skilled workers; labour shortages; ageing population." },
];
button_table("efBtns", "efOut", EF, 0, (p) => `<div class="tw"><table class="t"><tr><th>Possible benefits</th><th>Possible costs</th></tr><tr><td>${p.b}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a possible <b>benefit</b> or <b>cost</b> of a <b>rapidly growing</b> population?", buckets: [{ label: "Benefit" }, { label: "Cost" }], items: [
  { text: "Larger labour force", b: 0 }, { text: "Bigger market for firms", b: 0 }, { text: "More tax revenue", b: 0 }, { text: "Economies of scale", b: 0 },
  { text: "Pressure on food and water", b: 1 }, { text: "More spending on schools and hospitals", b: 1 }, { text: "Unemployment and lower wages", b: 1 }, { text: "Output per head may fall (overpopulation)", b: 1 },
], done: "Always give both sides." });
Lib.classify($("#cl2"), { prompt: "Does each describe <b>underpopulation</b> or <b>overpopulation</b>?", buckets: [{ label: "Underpopulation" }, { label: "Overpopulation" }], items: [
  { text: "Too few workers to use the land and resources", b: 0 }, { text: "More people would raise output per head", b: 0 }, { text: "Unused natural resources", b: 0 }, { text: "Labour shortages", b: 0 },
  { text: "Too many people for the available resources", b: 1 }, { text: "Output per head falls as population rises", b: 1 }, { text: "Overcrowding and pressure on housing", b: 1 }, { text: "Fewer people would raise living standards", b: 1 },
], done: "The optimum maximises output per head." });
Lib.classify($("#cl3"), { prompt: "Is each effect more likely with an <b>ageing</b> or a <b>young</b> population?", buckets: [{ label: "Ageing population" }, { label: "Young population" }], items: [
  { text: "Rising pension and healthcare costs", b: 0 }, { text: "Labour shortages in the future", b: 0 }, { text: "Less spending on durable goods and more on healthcare", b: 0 },
  { text: "Large spending on schools", b: 1 }, { text: "A large future workforce", b: 1 }, { text: "High demand for jobs", b: 1 },
], done: "Both structures have costs and benefits." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Optimum population", "The population that gives the highest output per head"],
  ["Overpopulation", "Too many people for the resources and capital available"],
  ["Underpopulation", "Too few people to use resources fully"],
  ["Dependency ratio", "Dependants (young and old) compared with those of working age"],
  ["Ageing population", "A rising share of the population aged 65 and over"],
  ["Labour force", "People who are employed or looking for work"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how an ageing population could slow economic growth</b>.", items: [
  "The share of older people rises",
  "The labour force grows more slowly or shrinks",
  "Fewer workers produce less output",
  "Tax revenue grows slowly and spending on pensions and healthcare rises",
  "Less money is available for investment",
  "Economic growth may slow",
], done: "A full analysis chain." });
''' + calc_js([
    ("A country has 10 million people aged 0-14, 30 million aged 15-64 and 10 million aged 65+. What is the dependency ratio?", 0.67, "(10 + 10) ÷ 30 = <b>0.67</b>.", None, 0.01),
    ("GDP is $300bn and the population is 10 million. What is GDP per head ($)?", 30000, "$300,000m ÷ 10m = <b>$30,000</b>.", None, None),
    ("The population rises to 12 million while GDP rises to $330bn. Does GDP per head rise or fall? Give the new GDP per head ($).", 27500, "330,000 ÷ 12 = <b>$27,500</b>: GDP per head falls.", None, None),
    ("There are 4 workers for each person aged 65+. In 20 years there will be 2 workers for each. By what percentage does the ratio fall?", 50, "(4 − 2) ÷ 4 × 100 = <b>50%</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is the optimum population?", ["The largest possible population", "The population that gives the highest output per head", "The population with no unemployment", "The population of working age"], 1, "It maximises output per head."),
    ("Overpopulation is most likely to cause:", ["A rise in output per head", "A fall in output per head", "Labour shortages", "A rise in wages"], 1, "Too many people for the resources."),
    ("An ageing population is most likely to cause:", ["Falling pension costs", "Higher healthcare and pension costs", "A larger labour force", "Lower dependency"], 1, "More older people need support."),
    ("Which could increase the optimum population?", ["New technology and capital", "Depletion of resources", "Pollution", "War"], 0, "A country can support more people at high income."),
    ("A rise in the population is most likely to shift the demand for housing:", ["Left", "Right", "Not at all", "Down"], 1, "More people want homes."),
]) + "\n" + cards_js([("Optimum population", "The population size that gives the highest output per head."), ("Overpopulation", "Too many people for the resources and capital available, so output per head falls."), ("Underpopulation", "Too few people to use resources fully."), ("Dependency ratio", "The number of dependants (aged 0-14 and 65+) divided by the number of working-age people."), ("Ageing population", "A rising share of the population aged 65 and over."), ("Young population", "A large share of the population aged under 15."), ("Labour force", "People who are employed or looking for work."), ("Economies of scale", "Lower average costs from larger output."), ("Remittances", "Money sent home by migrants working abroad."), ("Brain drain", "The emigration of skilled and educated workers.")]) + "labO(); labD();\n"
explore = '''
  <h2>Lab 1 · Finding the optimum population</h2>
  <p>Change the population and the level of technology and capital. Output per head is highest at the optimum, which moves when technology improves.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Output per head</small><strong id="oa1"></strong></div><div><small>Optimum population</small><strong id="oa2"></strong></div><div><small>Status</small><strong id="oa3"></strong></div></div><div class="verdict" id="oav"></div></div></div>
    <svg id="labO" viewBox="0 0 760 380" role="img" aria-label="Output per head against population size"></svg>
  </div>

  <h2>Lab 2 · The dependency ratio</h2>
  <p>Set the shares of children and older people. Working-age people support them, directly or through taxes.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>Working age</small><strong id="da1"></strong></div><div><small>Dependency ratio</small><strong id="da2"></strong></div><div><small>Workers per person aged 65+</small><strong id="da3"></strong></div></div><div class="verdict" id="dav"></div></div></div>
    <svg id="labD" viewBox="0 0 760 330" role="img" aria-label="Shares of the population by age"></svg>
  </div>

  <h2>Lab 3 · Effects of population changes</h2>
  <p>Pick a change to see the possible benefits and costs.</p>
  <div class="card"><div class="row" id="efBtns"></div><div id="efOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "What is meant by the optimum population?", "Population giving highest output (income) per head, given resources and technology.", "[K|The optimum population is the size of population that gives the highest output or income per head] [K|given the country's resources, capital and technology.]"),
    Q(2, "Explain", 4, "Explain two benefits a firm may gain from an increase in the size of a country's population. (May/June 2024, P21)", "Bigger market and sales; larger labour force and lower wages; economies of scale.",
      "[K|A larger population means more potential customers.] [N|Demand for the firm's product could rise, so sales and revenue may increase.] [K|It also means a larger pool of workers.] [N|The firm may find it easier to recruit and wage costs could be lower, and higher output could bring economies of scale.]"),
    Q(3, "Explain", 4, "Explain the effects of an ageing population on spending and saving levels. (Oct/Nov 2024, P21)", "Retired people have lower incomes, spend more on healthcare, may spend less on durables; saving falls as people draw on savings.",
      "[K|Older people tend to have lower incomes after retiring,] [N|so they may spend less on consumer goods and more on healthcare and essentials, so the pattern of spending changes.] [K|Saving is likely to fall.] [N|Retired people draw on their savings, so a larger share of older people may reduce total saving in the economy, although workers may save more for retirement.]"),
    Q(4, "Analyse", 6, "Analyse the disadvantages of a rapidly growing population. (Feb/Mar 2020, P22)", "Resources, overpopulation, dependants, pressure on services, depends on cause.",
      "[K|A rapidly growing population may use resources more quickly,] [N|so the country's ability to grow in future and its sustainability fall, and pollution may rise.] [N|It could take the population beyond the optimum level, so output per head falls and there may be overcrowding.] [N|If the cause is a high birth rate, more resources have to be spent on schools and healthcare for dependants,] [N|and if it is immigration, there may be pressure on housing and services.] [E|These costs are smaller if the economy grows quickly enough to provide jobs.]", key=True),
    Q(5, "Analyse", 6, "Analyse the advantages to a country of having a young population. (Oct/Nov 2023, P23)", "Future workforce, adaptable, demand, lower pension costs, tax revenue.",
      "[K|A young population means a large share of people will join the labour force.] [N|A growing workforce can increase output and economic growth, and young workers are often adaptable and open to new technology.] [N|They may spend on housing and consumer goods, raising demand and profits.] [N|Government spending on pensions and healthcare is lower, and as they enter jobs, they pay taxes that fund services.] [E|However, this depends on there being enough jobs and education.]", key=True),
    Q(6, "Discuss", 8, "Discuss whether or not an ageing population is a benefit to an economy. (May/June 2020, P22)", "Costs: pensions, healthcare, labour shortages. Benefits: experience, demand for services, volunteers; depends on health and retirement age.",
      "[K|An ageing population means a rising share of people aged 65 and over.] [N|It could harm the economy because more people need pensions and healthcare, so government spending rises while the labour force shrinks, which may mean higher taxes or borrowing and slower growth.] [N|It could also reduce productivity if older workers adapt less to new technology and cut saving.] [E|These problems are larger if people retire early and have poor health.] [N|However, older workers bring experience and can work longer, and older people create demand for healthcare, leisure and care services, and can volunteer.] [N|Governments can raise the retirement age or encourage immigration of young workers.] [E|Overall, an ageing population is more likely to be a problem than a benefit, but its effect depends on health, the retirement age and productivity.]", key=True),
    Q(7, "Discuss", 8, "Discuss whether or not a very low birth rate would be a cause for concern for a government. (May/June 2022, P22)", "Concern: ageing, smaller labour force, dependency, tax revenue, below optimum. Not: less overcrowding, pollution, resource depletion.",
      "[K|A very low birth rate means few babies are born, so the population may fall and age.] [N|It could be a concern because the labour force may shrink in future, the dependency ratio rises and tax revenue falls while pension and healthcare spending rise.] [N|If the population falls below the optimum level, output per head could fall.] [E|The effects take time to appear.] [N|However, a low birth rate could reduce overcrowding, pollution and depletion of non-renewable resources, and parents may stay in the labour force in the short run.] [E|Overall, a very low birth rate is likely to be a concern in the long run, especially if the population is already ageing, but it could be a benefit in an overpopulated country.]", key=True),
    Q(8, "Discuss", 8, "Discuss whether or not having a large population is beneficial for the economy. (May/June 2023, P23)", "For: labour, markets, scale; against: resources, overpopulation, dependants, unemployment. Depends on the optimum.",
      "[K|A large population means many people live in the country.] [N|It could be beneficial because it provides a large labour force and a big market, so firms can benefit from economies of scale and demand is high, which could raise growth and tax revenue.] [N|A diverse population can also produce more entrepreneurs and ideas.] [E|This is more likely if the country is underpopulated.] [N|However, a large population may put pressure on resources, land and services, and could cause overcrowding, pollution and unemployment, and may lower output per head if the country is overpopulated.] [E|Overall, whether a large population is beneficial depends on whether it is above or below the optimum, and on the level of capital, technology and education.]", key=True),
)
tp = tips([
    ("Optimum = highest output per head.", "Not the biggest or the smallest population."),
    ("Give both sides for every population change.", "Benefits and costs, then 'it depends on the optimum, age structure and jobs'."),
    ("Know the dependency ratio.", "(0-14 + 65+) ÷ (15-64)."),
    ("Use diagrams where asked.", "PPC shifts out or in; demand shifts right for a larger population."),
    ("Ageing: pensions, healthcare, labour shortage, saving falls.", "Add that retirement age and technology can help."),
], cmds("Define", "Explain", "Analyse", "Discuss"))
body = page(CL("5.3.2 The effects of changes in the size and structure of populations"), "Effects of Changes in the Size and Structure of Populations", "The optimum population, the effects of rising and falling population, and of ageing, young and unbalanced populations. Syllabus 5.3.2.",
    learn=learn, watch=watch(("Under-population, optimum and over-population", "stO"), ("Population change and the PPC", "stP"), ("A bigger population and the market for clothing", "stM"), ("Effects of an ageing population", "stA")), explore=explore,
    practise=practise(("Benefit or cost?", "cl1", "card"), ("Under- or overpopulation?", "cl2", "card"), ("Ageing or young population?", "cl3", "card"), ("Match the term", "m1", "card"), ("Order the ageing chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Japan's shrinking population", "Japan's population has been falling since around 2010 and a large share is aged over 65. Spending on pensions and healthcare is rising and some regions face labour shortages.", "Ageing and a falling population: costs and some adjustments such as robots and later retirement."),
        rw("China's one-child policy", "China limited most families to one child for decades. The birth rate fell, and now the population is ageing quickly with a shrinking labour force, though there is a larger share of men than women.", "Effects of changes in size, age and gender structure."),
        rw("Nigeria's young population", "Nigeria has a very young population, with around 40% aged under 15. This promises a large future workforce but requires many jobs and schools.", "A young population: advantages and disadvantages."),
        rw("Migrants in Gulf states", "Gulf countries such as the UAE rely on migrant workers, who make up most of the labour force, boosting construction and services, while the countries have a high share of men.", "Immigration, labour force and gender structure."),
        rw("Overcrowded cities", "Fast-growing cities such as Lagos and Dhaka face pressure on housing, transport and water as the population increases faster than infrastructure.", "Overpopulation and pressure on services.")),
    exam=ex, tips=tp)
write("pp2", body, js, "Effects of Changes in the Size and Structure of Populations", "ig-population-effects")
