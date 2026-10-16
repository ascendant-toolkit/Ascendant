"""Builds the two IGCSE Economics 5.1 Living standards reviews (5.1.1, 5.1.2), written from scratch.
Run: python3 tools/artifact-kit/mk_ig51.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

# =========================================================== 5.1.1 Indicators
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Living standards</span> describe the quality and quantity of goods and services people can obtain, and how well they live. Two main indicators are <b>real GDP per head</b> (average income) and the <b>Human Development Index (HDI)</b>, which adds <b>health</b> and <b>education</b> to income. Each has advantages and disadvantages, so good answers use both and say what they miss.</p></div>

  <h2>Real GDP per head</h2>
  <div class="formula">Real GDP per head = real GDP ÷ population</div>
  <ul>
    <li><b>Real</b> means adjusted for inflation, so it shows changes in output, not prices.</li>
    <li><b>Per head</b> means divided by population, so it is the <b>average income</b> per person. A big economy with a huge population can have a low figure.</li>
    <li>Higher real GDP per head usually means people can afford more food, housing, healthcare and education.</li>
  </ul>
  <div class="grid2">
    <div class="card"><h3>Advantages</h3><ul><li>Simple and quick to find, and updated regularly</li><li>Adjusted for inflation and population</li><li>Easy to compare over time and between countries</li><li>Linked to spending power</li></ul></div>
    <div class="card"><h3>Disadvantages</h3><ul><li>An <b>average</b>: hides inequality</li><li>Leaves out the <b>informal economy</b> and unpaid work</li><li>Ignores health, education, leisure, freedom and the environment</li><li>Counts harmful output (pollution clean-up, weapons)</li><li>Cost of living differs between countries</li></ul></div>
  </div>

  <h2>Human Development Index (HDI)</h2>
  <p>The HDI is a <b>composite index</b> between 0 and 1. A higher value means higher human development. It combines three parts:</p>
  <div class="tw"><table class="t">
    <tr><th>Component</th><th>Measured by</th><th>What it shows</th></tr>
    <tr><td><b>Health</b></td><td>Life expectancy at birth</td><td>How long people can expect to live</td></tr>
    <tr><td><b>Education</b></td><td>Mean years of schooling (adults) and expected years of schooling (children)</td><td>Access to and level of education</td></tr>
    <tr><td><b>Income</b></td><td>Gross national income (GNI) per head, adjusted for price differences between countries</td><td>Material standard of living</td></tr>
  </table></div>
  <p>Each part is turned into an index between 0 and 1 and the three are combined into one HDI. Countries are grouped as <b>very high</b> (0.800 or above), <b>high</b> (0.700 to 0.799), <b>medium</b> (0.550 to 0.699) and <b>low</b> (below 0.550) human development.</p>
  <div class="grid2">
    <div class="card"><h3>Advantages of the HDI</h3><ul><li>Includes <b>health and education</b>, not just income</li><li>A single number that is easy to compare</li><li>Can show a country is doing well or badly for its income</li></ul></div>
    <div class="card"><h3>Disadvantages of the HDI</h3><ul><li>Still an <b>average</b>: hides inequality</li><li>Leaves out the <b>environment</b>, freedom, crime, leisure and quality of life</li><li>The quality of education and healthcare is not measured</li><li>Data may be inaccurate, and countries with similar HDI can differ widely</li></ul></div>
  </div>

  <h2>Other indicators</h2>
  <p>Many other measures are used: <b>life expectancy</b>, <b>infant mortality</b>, <b>literacy rate</b>, <b>doctors per 1,000 people</b>, <b>access to clean water</b> and electricity, <b>internet use</b>, housing quality and calorie intake.</p>
  <p class="note">GDP per head and HDI are usually positively related: richer countries tend to have longer life expectancy and more schooling. But there are exceptions, so be ready to use data.</p>
'''
js = HEAD + COMMON + '''
function gdpChart(s) {
  const base = 330, k = 0.36; let o = SV.line(60, base, 710, base);
  const bars = [["Real GDP ($bn)", s.g, "--accent", 1, "$"], ["Population (m)", s.p, "--warn", 1, ""], ["Real GDP per head ($)", (s.g * 1000) / s.p, "--good", s.o, "$"]];
  bars.forEach(([n, v, c, op, pre], i) => { if (op <= 0.02) return; const sc = i === 2 ? 0.0028 : i === 0 ? 0.4 : 4; const x = 110 + i * 200, h = v * sc; o += `<g opacity="${op}">` + SV.rect(x, base - h, 130, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, base - h - 8, pre + Math.round(v).toLocaleString("en-US"), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 22, n, "sm", { "text-anchor": "middle" }) + "</g>"; });
  if (s.t) o += SV.text(380, 40, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 400, label: "Real GDP per head", base: { g: 600, p: 20, o: 0, t: "" }, draw: gdpChart, steps: [
  { cap: "A country has <b>real GDP of $600bn</b> and a <b>population of 20 million</b>.", s: { g: 600, p: 20, o: 0, t: "" } },
  { cap: "<b>Real GDP per head</b> = $600bn ÷ 20 million = <b>$30,000</b>. This is the average income per person.", s: { g: 600, p: 20, o: 1, t: "$30,000 per person" } },
  { cap: "Real GDP grows 4% to <b>$624bn</b>, but population grows 6% to <b>21.2 million</b>. Output rose, but real GDP per head <b>falls</b> to about <b>$29,400</b>: the average person is a little worse off.", s: { g: 624, p: 21.2, o: 1, t: "Output up, but per head down" } },
] });
function hdiChart(s) {
  const base = 320, k = 240; let o = SV.line(60, base, 710, base) + SV.line(60, base, 60, 60) + SV.text(66, 60, "Index (0 to 1)", "sm");
  const bars = [["Health", 0.85, "--good", s.a], ["Education", 0.70, "--n", s.b], ["Income", 0.75, "--warn", s.c]];
  bars.forEach(([n, v, c, op], i) => { if (op <= 0.02) return; const x = 100 + i * 140, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 100, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 50, base - h - 8, money(v, 2), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, base + 20, n, "sm", { "text-anchor": "middle" }) + "</g>"; });
  const hdi = Math.cbrt(0.85 * 0.7 * 0.75);
  if (s.d > 0.02) { const h = hdi * k; o += `<g opacity="${s.d}">` + SV.rect(540, base - h, 130, h, "", { style: "fill:var(--accent)", opacity: 0.9 }) + SV.text(605, base - h - 8, "HDI " + money(hdi, 2), "lbl bd t3", { "text-anchor": "middle" }) + SV.text(605, base + 20, "Combined", "sm", { "text-anchor": "middle" }) + "</g>"; }
  return o;
}
Lib.stepper($("#stH"), { w: 760, h: 400, label: "How the HDI is built", base: { a: 0, b: 0, c: 0, d: 0 }, draw: hdiChart, steps: [
  { cap: "<b>Health:</b> life expectancy at birth is turned into an index from 0 to 1. Here the country scores <b>0.85</b>.", s: { a: 1, b: 0, c: 0, d: 0 } },
  { cap: "<b>Education:</b> mean and expected years of schooling give an index of <b>0.70</b>.", s: { a: 1, b: 1, c: 0, d: 0 } },
  { cap: "<b>Income:</b> GNI per head (adjusted for price differences) gives an index of <b>0.75</b>.", s: { a: 1, b: 1, c: 1, d: 0 } },
  { cap: "The three are combined into one <b>HDI of about 0.76</b>: <b>high</b> human development. A country can raise its HDI by improving health or education, even if income is unchanged.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });
function twoChart(s) {
  const base = 320, k = 0.0085; let o = SV.line(60, base, 710, base);
  const c = [["Country A", 20000, 0.8], ["Country B", 20000, 0.7]];
  c.forEach(([n, g, h], i) => { const x = 130 + i * 300, op = i === 0 ? 1 : s.b; if (op <= 0.02) return; o += `<g opacity="${op}">` + SV.rect(x, base - g * k * 0.9, 90, g * k * 0.9, "", { style: "fill:var(--warn)", opacity: 0.85 }) + SV.text(x + 45, base - g * k * 0.9 - 8, "$20,000", "lbl bd", { "text-anchor": "middle" }) + SV.rect(x + 100, base - h * 200, 90, h * 200, "", { style: "fill:var(--accent)", opacity: 0.85 }) + SV.text(x + 145, base - h * 200 - 8, "HDI " + h.toFixed(2), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 95, base + 22, n, "lbl bd", { "text-anchor": "middle" }) + "</g>"; });
  if (s.t) o += SV.text(380, 40, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 400, label: "Why add health and education to income?", base: { b: 0, t: "" }, draw: twoChart, steps: [
  { cap: "<b>Country A</b> has GDP per head of $20,000 and an HDI of <b>0.80</b>: people are healthy and well educated.", s: { b: 0, t: "" } },
  { cap: "<b>Country B</b> has the <b>same GDP per head</b> but an HDI of only <b>0.70</b>.", s: { b: 1, t: "Same income, different HDI" } },
  { cap: "B's income is spent differently: lower life expectancy and fewer years of schooling. <b>GDP per head alone would hide this</b>. That is the advantage of the HDI.", s: { b: 1, t: "GDP per head hides the difference" } },
] });

/* Lab 1: HDI calculator */
function labH() {
  if (!$("#ha") || !$("#hb") || !$("#hc") || !$("#hd")) return;
  const le = +$("#ha").value, my = +$("#hb").value, ey = +$("#hc").value, gni = +$("#hd").value;
  const I = (v, a, b) => clamp((v - a) / (b - a), 0, 1), li = I(le, 20, 85), ei = (I(my, 0, 15) + I(ey, 0, 18)) / 2, ii = clamp((Math.log(gni) - Math.log(100)) / (Math.log(75000) - Math.log(100)), 0, 1), hdi = Math.cbrt(li * ei * ii);
  $("#ha1").textContent = money(li, 2); $("#ha2").textContent = money(ei, 2); $("#ha3").textContent = money(ii, 2); $("#ha4").textContent = money(hdi, 3);
  const cat = hdi >= 0.8 ? "very high" : hdi >= 0.7 ? "high" : hdi >= 0.55 ? "medium" : "low";
  $("#hav").textContent = `HDI = about ${money(hdi, 3)}: ${cat} human development. Try raising life expectancy or schooling while keeping income fixed: HDI rises. Income is on a log scale, so doubling a low income helps the HDI much more than doubling a high one.`;
  const base = 300; let o = SV.line(60, base, 700, base);
  [["Health", li, "--good"], ["Education", ei, "--n"], ["Income", ii, "--warn"], ["HDI", hdi, "--accent"]].forEach(([n, v, c], i) => { const x = 100 + i * 150, h = v * 240; o += SV.rect(x, base - h, 100, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 50, base - h - 8, money(v, 2), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, base + 20, n, "sm", { "text-anchor": "middle" }); });
  $("#labH").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ha", label: "Life expectancy at birth", min: 40, max: 85, step: 1, value: 72, fmt: (v) => v + " years", onInput: labH });
Lib.slider($("#g2"), { id: "hb", label: "Mean years of schooling (adults)", min: 1, max: 15, step: 0.5, value: 9, fmt: (v) => v + " years", onInput: labH });
Lib.slider($("#g3"), { id: "hc", label: "Expected years of schooling (children)", min: 4, max: 18, step: 0.5, value: 13, fmt: (v) => v + " years", onInput: labH });
Lib.slider($("#g4"), { id: "hd", label: "GNI per head ($, adjusted)", min: 500, max: 75000, step: 500, value: 15000, fmt: (v) => "$" + v.toLocaleString("en-US"), onInput: labH });
/* Lab 2: scatter */
const CT = [["Niger", 600, 61, 0.39], ["Ethiopia", 1000, 66, 0.49], ["Nigeria", 2200, 53, 0.54], ["India", 2500, 68, 0.64], ["Eswatini", 4000, 58, 0.61], ["Vietnam", 4000, 74, 0.73], ["Brazil", 8700, 73, 0.76], ["China", 12600, 78, 0.78], ["Japan", 34000, 85, 0.92], ["United Kingdom", 46000, 81, 0.93], ["Singapore", 80000, 83, 0.94]];
let selC = 8;
function labS() {
  const X = (g) => 70 + ((Math.log(g) - Math.log(400)) / (Math.log(100000) - Math.log(400))) * 600, Y = (v) => 300 - ((v - 45) / (90 - 45)) * 250;
  let o = SV.line(70, 300, 690, 300) + SV.line(70, 300, 70, 40) + SV.text(690, 330, "GDP per head (log scale)", "sm", { "text-anchor": "end" }) + SV.text(76, 44, "Life expectancy (years)", "sm");
  [50, 60, 70, 80, 90].forEach((v) => (o += SV.line(70, Y(v), 690, Y(v), "gr") + SV.text(62, Y(v) + 4, v, "sm", { "text-anchor": "end" })));
  CT.forEach(([n, g, l], i) => { o += SV.circle(X(g), Y(l), i === selC ? 9 : 6, i === selC ? "dot2" : "dot1", { opacity: i === selC ? 1 : 0.7 }); if (i === selC) o += SV.text(X(g) + 12, Y(l) - 8, n, "lbl bd t2", { style: halo }); });
  $("#labS").innerHTML = o;
  const c = CT[selC];
  $("#hsBtns").innerHTML = CT.map((q, j) => `<button class="b${j === selC ? " pri" : ""}" data-j="${j}">${q[0]}</button>`).join("");
  $$("#hsBtns .b").forEach((b) => (b.onclick = () => { selC = +b.dataset.j; labS(); }));
  $("#hsOut").innerHTML = `<div class="tw"><table class="t"><tr><th>GDP per head</th><th>Life expectancy</th><th>HDI</th></tr><tr><td>$${c[1].toLocaleString("en-US")}</td><td>${c[2]} years</td><td>${c[3].toFixed(2)}</td></tr></table></div>`;
}
const IND = [
  { n: "Real GDP per head", m: "Average income per person, adjusted for inflation.", s: "Simple, regular, comparable over time and countries.", w: "Average hides inequality; misses informal economy, health, education, environment." },
  { n: "HDI", m: "Combines health, education and income into one index.", s: "Broader than income; easy to compare.", w: "Hides inequality; leaves out environment, freedom and quality." },
  { n: "Life expectancy", m: "Average years a newborn can expect to live.", s: "Reflects health, nutrition and sanitation.", w: "An average; says little about quality of life." },
  { n: "Literacy rate", m: "Share of adults who can read and write.", s: "Simple measure of education.", w: "Says nothing about quality of education." },
  { n: "Infant mortality", m: "Deaths of babies per 1,000 births.", s: "Sensitive to healthcare, nutrition and poverty.", w: "Only one aspect of health." },
  { n: "Access to clean water", m: "Share of people with safe drinking water.", s: "Basic need linked to health.", w: "Ignores quantity and other needs." },
];
button_table("inBtns", "inOut", IND, 0, (p) => `<div class="tw"><table class="t"><tr><th>What it measures</th><th>Strength</th><th>Weakness</th></tr><tr><td>${p.m}</td><td>${p.s}</td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>HDI component</b> does each measure belong to?", buckets: [{ label: "Health" }, { label: "Education" }, { label: "Income" }], items: [
  { text: "Life expectancy at birth", b: 0 }, { text: "Mean years of schooling", b: 1 }, { text: "Expected years of schooling", b: 1 },
  { text: "Gross national income per head", b: 2 }, { text: "Average income, adjusted for price differences", b: 2 }, { text: "How long people can expect to live", b: 0 },
], done: "Three components: health, education, income." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>disadvantage of GDP per head</b>, a <b>disadvantage of HDI</b> or <b>both</b>?", buckets: [{ label: "GDP per head only" }, { label: "HDI only" }, { label: "Both" }], items: [
  { text: "Does not measure health or education", b: 0 }, { text: "Counts harmful output such as pollution clean-up", b: 0 },
  { text: "Education measure ignores quality of schooling", b: 1 }, { text: "Equal weighting of three parts may be arbitrary", b: 1 },
  { text: "Hides income inequality", b: 2 }, { text: "Ignores the environment", b: 2 }, { text: "Leaves out freedom and crime", b: 2 },
], done: "Both hide inequality and the environment; HDI at least covers health and education." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Living standards", "The quality and quantity of goods and services people can obtain"],
  ["Real GDP per head", "Real GDP divided by population"],
  ["Human Development Index", "A composite index of health, education and income between 0 and 1"],
  ["Life expectancy", "The average number of years a newborn is expected to live"],
  ["Composite index", "An index that combines several measures into one number"],
  ["Informal economy", "Activity that is not regulated, recorded or taxed"],
], done: "Good vocabulary scores marks." });
''' + calc_js([
    ("Real GDP is $800bn and the population is 20 million. Calculate real GDP per head ($).", 40000, "$800bn ÷ 20m = <b>$40,000</b>.", "$800bn = 800,000m.", None),
    ("Real GDP rises 3% a year and population rises 1% a year. Roughly, what is the growth of real GDP per head (%)?", 2, "3 − 1 = <b>about 2%</b>.", None, None),
    ("An HDI is 0.64 in Year 1 and 0.70 in Year 5. By how much has it risen?", 0.06, "0.70 − 0.64 = <b>0.06</b>.", None, 0.001),
    ("A country's life expectancy index is 0.8, education index 0.6 and income index 0.5. What is the average of the three (to 2 d.p.)? (The HDI uses a similar but slightly different method.)", 0.63, "(0.8 + 0.6 + 0.5) ÷ 3 = <b>0.63</b>.", None, 0.01),
]) + mcq_js("qz1", [
    ("What does real GDP per head show?", ["Total output", "Average income per person, adjusted for inflation", "Population growth", "Unemployment"], 1, "Real GDP divided by population."),
    ("Which is a component of the HDI?", ["Inflation", "Life expectancy", "Unemployment", "The exchange rate"], 1, "Health, education and income."),
    ("Which is a limitation of real GDP per head?", ["It is adjusted for inflation", "It hides inequality", "It is divided by population", "It is easy to compare"], 1, "It is an average."),
    ("A country has a falling GDP per head but a rising HDI. This could be because:", ["Education and healthcare are improving", "Income is rising fast", "The HDI ignores education", "Population is falling"], 0, "Health and education offset falling income."),
    ("Which statement about the HDI is correct?", ["It only measures income", "It is a value between 0 and 1", "It includes the environment", "It includes unemployment"], 1, "A composite index from 0 to 1."),
]) + "\n" + cards_js([("Living standards", "The quality and quantity of goods and services people can obtain."), ("Real GDP per head", "Real GDP divided by population: the average income per person adjusted for inflation."), ("Human Development Index (HDI)", "A composite index of life expectancy, years of schooling and income per head, between 0 and 1."), ("Composite index", "An index that combines several measures into one value."), ("Life expectancy", "The average number of years a newborn is expected to live."), ("Mean years of schooling", "The average number of years of education adults have completed."), ("Expected years of schooling", "The number of years of schooling a child entering school can expect to receive."), ("GNI per head", "Gross national income divided by population."), ("Informal economy", "Activity that is not regulated, recorded or taxed."), ("Infant mortality", "The number of deaths of babies under one year per 1,000 live births.")]) + "labH(); labS();\n"
explore = '''
  <h2>Lab 1 · HDI calculator</h2>
  <p>Set life expectancy, schooling and income. Each is turned into an index from 0 to 1 and combined into the HDI. (Simplified from the UN method.)</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>Health index</small><strong id="ha1"></strong></div><div><small>Education index</small><strong id="ha2"></strong></div><div><small>Income index</small><strong id="ha3"></strong></div><div><small>HDI</small><strong id="ha4"></strong></div></div><div class="verdict" id="hav"></div></div></div>
    <svg id="labH" viewBox="0 0 760 340" role="img" aria-label="HDI components and HDI"></svg>
  </div>

  <h2>Lab 2 · Income and life expectancy</h2>
  <p>Pick a country to see where it sits. Generally richer countries have longer life expectancy, but there are exceptions such as Eswatini and Nigeria. Figures are rounded and illustrative.</p>
  <div class="card"><div class="row" id="hsBtns" style="margin-bottom:10px"></div><svg id="labS" viewBox="0 0 760 350" role="img" aria-label="GDP per head against life expectancy"></svg><div id="hsOut"></div></div>

  <h2>Lab 3 · Indicator comparison</h2>
  <p>Pick an indicator to see what it measures, its strength and its weakness.</p>
  <div class="card"><div class="row" id="inBtns"></div><div id="inOut"></div></div>
'''
ex = exam(
    Q(1, "Identify", 2, "Identify two measures of living standards. (Feb/Mar 2021, P22)", "Real GDP per head and HDI are safest.", "[K|Real GDP per head (average income).] [K|The Human Development Index (HDI).]"),
    Q(2, "Explain", 2, "Explain how real GDP per head can be an indicator of living standards. (May/June 2024, P23)", "Adjusted for inflation and population; average income; spending on necessities.",
      "[K|Real GDP per head is the average income per person adjusted for inflation,] [N|so a higher value suggests people can spend more and afford more goods, services and basic necessities, raising living standards.]"),
    Q(3, "Explain", 4, "Explain the three components of the Human Development Index.", "Health, education, income, each with how it is measured.",
      "[K|The HDI includes health, measured by life expectancy at birth.] [K|It includes education, measured by mean and expected years of schooling.] [K|It includes income, measured by gross national income per head adjusted for price differences.] [N|These are combined into one value between 0 and 1, so a higher HDI means higher human development.]"),
    Q(4, "Explain", 4, "Explain two disadvantages of using real GDP per head as an indicator of living standards.", "Average hides inequality; informal economy; ignores health, education, environment.",
      "[K|Real GDP per head is an average.] [N|A country may have a high average but with income concentrated among a few, so many people could still live in poverty.] [K|It also ignores things that affect well-being.] [N|It does not measure health, education, leisure or pollution, so a country with high GDP per head might have long working hours and poor air quality, lowering living standards.]"),
    Q(5, "Analyse", 5, "Analyse the relationship between GDP per head and life expectancy. (Feb/Mar 2022, P22)", "Use data: say the overall relationship, give a high and low example, then explain why. Note an exception if there is one.",
      "[A|Generally there is a positive relationship: countries with a higher GDP per head tend to have a longer life expectancy.] [A|For example, a country with GDP per head of $45,000 may have life expectancy of 81, whereas one with $2,000 may have life expectancy of about 60.] [N|Higher incomes allow better food, housing, sanitation and healthcare, and governments collect more tax to spend on health.] [E|However, the relationship is not exact: some countries with similar incomes differ because of how well healthcare is organised and spent.]", key=True),
    Q(6, "Analyse", 5, "Analyse the relationship between Greece's GDP per head and its HDI value. (May/June 2020, P23)", "Use the data trend: GDP per head fell while HDI rose. Explain why using the HDI components.",
      "[A|Greece's GDP per head fell between 2010 and 2015 while its HDI value rose, so over this period the relationship was negative.] [N|The HDI includes health and education as well as income.] [N|Improvements in education and healthcare could have more than offset the fall in income,] [N|so the HDI could rise even while GDP per head fell.]", key=True),
    Q(7, "Explain", 4, "Explain two ways climate change can lead to a fall in the Human Development Index of a country. (May/June 2024, P23)", "One link per HDI component: floods and schools, disease and life expectancy, farmland and income.",
      "[K|Floods can damage schools,] [N|which reduces mean and expected years of schooling, lowering the education part of the HDI.] [K|Flooding can also increase disease,] [N|which reduces life expectancy, lowering the health part of the HDI.]"),
    Q(8, "Discuss", 8, "Discuss whether or not people living in countries with a high GDP enjoy higher living standards than people in countries with a low GDP. (May/June 2024, P21)", "For: afford housing, nutrition, healthcare, education. Against: GDP not GDP per head; inequality; informal economy; prices; long hours; pollution. Use 'it depends'.",
      "[K|Living standards describe the quality and quantity of goods and services people can obtain.] [N|People in countries with high GDP may be able to afford better housing, food and healthcare, which could increase life expectancy, and higher incomes may buy more and better quality products and education.] [E|This is more likely if the high GDP is shared across the population.] [N|However, high GDP does not necessarily mean high GDP per head, so incomes could still be low.] [N|Income may be unevenly distributed, so some people live in poverty, and a large informal sector may mean GDP under-records income.] [N|People in a rich country may work long hours with little leisure, face higher prices, and experience pollution and congestion.] [E|Overall, people in high-GDP countries are likely to enjoy higher living standards on average, but it depends on GDP per head, how income is distributed and non-income factors such as health, leisure and the environment.]", key=True),
)
tp = tips([
    ("Real, per head.", "Real removes inflation; per head divides by population."),
    ("HDI has three parts.", "Health (life expectancy), education (years of schooling), income (GNI per head)."),
    ("Both hide inequality.", "Always give this as a limitation."),
    ("Use the data in analysis questions.", "State the pattern, quote figures, then explain why."),
    ("Include a non-income factor.", "Leisure, environment, freedom, crime: ideas beyond GDP."),
], cmds("Identify", "Explain", "Analyse", "Discuss"))
body = page(CL("5.1.1 Indicators of living standards"), "Indicators of Living Standards", "Real GDP per head and the Human Development Index, with the advantages and disadvantages of each. Syllabus 5.1.1.",
    learn=learn, watch=watch(("Real GDP per head", "stG"), ("How the HDI is built", "stH"), ("Why add health and education to income?", "stT")), explore=explore,
    practise=practise(("Which HDI component?", "cl1", "card"), ("Which disadvantage?", "cl2", "card"), ("Match the term", "m1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Income is not everything", "Some countries, for example Equatorial Guinea, have relatively high GDP per head from oil but a lower HDI because health and education lag behind. Others with modest incomes, such as Costa Rica, have a high HDI.", "Why the HDI gives a different picture from GDP per head."),
        rw("Greece after 2010", "A past paper shows Greece's GDP per head falling after 2010 while its HDI rose, because education and healthcare improved.", "Interpreting the relationship from data."),
        rw("Climate change and HDI in Indonesia", "A past paper asks how flooding could reduce Indonesia's HDI through schooling, disease and farm incomes.", "Linking an event to each HDI component."),
        rw("Working hours in rich countries", "In some high-income economies people work very long hours, with less time for family and leisure, which GDP does not capture.", "A non-income factor when evaluating GDP per head.")),
    exam=ex, tips=tp)
write("lv1", body, js, "Indicators of Living Standards", "ig-living-standards-indicators")

# =========================================================== 5.1.2 Comparing
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Living standards and income differ <b>between countries</b> and also <b>within</b> them. Between countries, differences come from productivity, capital, education, health, technology, institutions, trade, conflict and natural resources. Within a country, income is <b>unequally distributed</b> between rich and poor, urban and rural, regions, and by gender, because of differences in skills, jobs, wealth, taxes and benefits. An average such as GDP per head hides these differences.</p></div>

  <h2>Why living standards differ between countries</h2>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>How it raises (or lowers) living standards</th></tr>
    <tr><td><b>Productivity and technology</b></td><td>More output per worker means higher incomes; low productivity keeps incomes low</td></tr>
    <tr><td><b>Capital and investment</b></td><td>More machinery, roads and power raise output; poor countries often lack capital and save little</td></tr>
    <tr><td><b>Education and health</b></td><td>Skilled, healthy workers earn more; poor health and low schooling hold back growth</td></tr>
    <tr><td><b>Institutions and stability</b></td><td>Strong property rights, low corruption and political stability attract investment; conflict destroys capital</td></tr>
    <tr><td><b>Natural resources and geography</b></td><td>Oil, minerals and fertile land can raise income; landlocked countries, deserts and disaster-prone areas face costs</td></tr>
    <tr><td><b>Trade and globalisation</b></td><td>Open trade and investment can raise growth; dependence on a few exports can leave countries vulnerable</td></tr>
    <tr><td><b>Population growth</b></td><td>Fast population growth can spread resources thinly</td></tr>
    <tr><td><b>Government policies</b></td><td>Spending on schools, health and infrastructure and sensible economic policy raise living standards</td></tr>
  </table></div>

  <h2>Why income is unequally distributed within a country</h2>
  <ul>
    <li><b>Wages and skills:</b> highly educated workers earn more than unskilled workers.</li>
    <li><b>Unemployment and low pay:</b> some groups face unemployment or low-paid, insecure jobs.</li>
    <li><b>Ownership of wealth:</b> people who own property, shares or businesses earn rents, profits and dividends.</li>
    <li><b>Location:</b> cities usually have higher wages and better services than rural areas; some regions are left behind.</li>
    <li><b>Discrimination and gender:</b> unequal pay or access to education and jobs.</li>
    <li><b>Taxes and benefits:</b> progressive taxes and generous benefits reduce inequality; the opposite increases it.</li>
    <li><b>Informal work:</b> many poorer workers have no pension or protection.</li>
  </ul>

  <h2>Measuring income distribution</h2>
  <p>Households can be ranked from poorest to richest and split into five equal groups (<b>quintiles</b>). In an equal country each group has about 20% of income. In an unequal country the richest 20% may have 50% or more and the poorest 20% only a few per cent.</p>
  <div class="grid2">
    <div class="card"><h3>Cities and rural areas</h3><p>City dwellers often have higher wages, more jobs and better schools and hospitals, but higher housing costs, congestion, pollution and slums. Rural dwellers may have lower incomes and poorer services, but lower living costs and cleaner air.</p></div>
    <div class="card"><h3>Low-income farmers</h3><p>Low productivity (little capital, small plots), low and unstable prices, weather risks and seasonal work give low and uncertain incomes; poor roads, schools and healthcare lower living standards further.</p></div>
  </div>
'''
js = HEAD + COMMON + '''
const QA = [16, 18, 20, 22, 24], QB = [4, 8, 14, 24, 50], QN = ["Poorest 20%", "Next 20%", "Middle 20%", "Next 20%", "Richest 20%"];
function quintChart(s) {
  const base = 320, k = 5; let o = SV.line(60, base, 710, base) + SV.text(60, 30, "Average income per head in each fifth of the population ($ thousand)", "sm");
  s.q.forEach((v, i) => { const x = 90 + i * 120, h = v * k; o += SV.rect(x, base - h, 90, h, "", { style: `fill:var(${i === 0 ? "--bad" : i === 4 ? "--accent" : "--muted"})`, opacity: 0.85 }) + SV.text(x + 45, base - h - 8, "$" + money(v, 0) + "k", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 45, base + 20, QN[i], "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  if (s.t) o += SV.text(380, 58, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stQ"), { w: 760, h: 400, label: "Same average income, different distribution", base: { q: QA, t: "" }, draw: quintChart, steps: [
  { cap: "<b>Country A</b>: income per head is spread fairly evenly. The average is <b>$20,000</b> and the poorest fifth earns <b>$16,000</b>.", s: { q: QA, t: "Country A: average $20k" } },
  { cap: "<b>Country B</b> has the <b>same average income of $20,000</b>, but the richest fifth gets $50,000 each and the poorest fifth only <b>$4,000</b>.", s: { q: QB, t: "Country B: average still $20k" } },
  { cap: "GDP per head is the same, but <b>living standards for most people are very different</b>. An average hides the distribution.", s: { q: QB, t: "Average hides inequality" } },
] });
const LOW = ["Low income, so little saving and investment", "Little capital, technology and education", "Low productivity", "Low output and low incomes", "Poor health and schooling: less skills and ability to work", "Low living standards persist: a poverty trap"];
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Why poor countries can stay poor", base: { n: 0 }, draw: mkChain(LOW, "--bad"), steps: chainSteps(["<b>Low income</b> means little saving and little tax revenue.", "So there is <b>little investment</b> in capital, technology and education.", "Workers have <b>low productivity</b>.", "<b>Output and incomes stay low</b>.", "Poor health and schooling make it even harder to raise productivity.", "<b>Living standards stay low</b>: a poverty trap. Policies and aid are needed to break the cycle."]) });
const FAR = ["Small plots, little capital and technology", "Low yields: low productivity", "Low and unstable crop prices; weather risk", "Low, seasonal and uncertain income", "Little spent on education, healthcare, nutrition", "Low living standards for farm families"];
Lib.stepper($("#stF"), { w: 760, h: 400, label: "Low-income farmers", base: { n: 0 }, draw: mkChain(FAR, "--warn"), steps: chainSteps(["<b>Small plots</b>, little capital and old methods.", "<b>Low yields</b>: low productivity.", "Crop prices are <b>low and unstable</b>, and weather brings risk.", "Income is <b>low, seasonal and uncertain</b>.", "Little can be spent on <b>education, healthcare and nutrition</b>.", "<b>Living standards are low</b>. Evaluate: roads, markets, irrigation and training can help."]) });

/* Lab 1: distribution simulator */
function labQ() {
  if (!$("#qa") || !$("#qb")) return;
  const u = +$("#qa").value / 100, r = +$("#qb").value / 100;
  const pre = QA.map((a, i) => a * (1 - u) + QB[i] * u), tot = pre.reduce((a, b) => a + b, 0), shares = pre.map((v) => v / tot);
  const post = shares.map((sh) => sh * (1 - r) + 0.2 * r), inc = post.map((sh) => sh * 100);
  $("#qa1").textContent = "$20k"; $("#qa2").textContent = "$" + money(inc[0], 1) + "k"; $("#qa3").textContent = money(post[4] * 100, 0) + "%"; $("#qa4").textContent = money(post[4] / post[0], 1) + " times";
  $("#qav").textContent = `Average income stays at $20,000, but the poorest fifth gets $${money(inc[0], 1)}k and the richest fifth $${money(inc[4], 1)}k: the richest fifth earns ${money(post[4] / post[0], 1)} times as much. ${r > 0 ? "Progressive taxes and benefits (redistribution) have narrowed the gap." : "Move the second slider to see how taxes and benefits narrow the gap."}`;
  $("#labQ").innerHTML = quintChart({ q: inc, t: "" });
}
Lib.slider($("#g1"), { id: "qa", label: "How unequal the pre-tax distribution is (0 = Country A, 100 = Country B)", min: 0, max: 100, step: 5, value: 100, fmt: (v) => v + "%", onInput: labQ });
Lib.slider($("#g2"), { id: "qb", label: "Redistribution through progressive taxes and benefits", min: 0, max: 80, step: 10, value: 0, fmt: (v) => v + "%", onInput: labQ });
const FX = [
  { n: "Productivity and technology", t: "Between countries", e: "High-productivity economies produce more per worker, so incomes are higher.", x: "Germany compared with a subsistence farming economy" },
  { n: "Education and health", t: "Between and within", e: "Skilled, healthy workers earn more; people without schooling are more likely to be poor.", x: "Higher wages for graduates" },
  { n: "Conflict and instability", t: "Between countries", e: "War destroys capital and deters investment, lowering living standards.", x: "Countries emerging from civil war" },
  { n: "Natural resources", t: "Between countries", e: "Oil and minerals can raise national income, if the gains are shared and not wasted.", x: "Guyana's oil discovery (past paper)" },
  { n: "Urban and rural location", t: "Within a country", e: "Cities have higher wages and services; rural areas lag.", x: "Rural farmers compared with city workers" },
  { n: "Ownership of wealth", t: "Within a country", e: "Owners of property and firms earn rents and profits on top of wages.", x: "Landowners and shareholders" },
  { n: "Taxes and benefits", t: "Within a country", e: "Progressive taxes and benefits reduce inequality; regressive taxes increase it.", x: "Welfare states have lower inequality" },
  { n: "Gender and discrimination", t: "Within a country", e: "Unequal pay and access to education and jobs lower incomes of some groups.", x: "Gender pay gaps" },
];
button_table("fxBtns", "fxOut", FX, 0, (p) => `<div class="tw"><table class="t"><tr><th>Applies</th><th>How it affects living standards</th><th>Example</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td><td>${p.x}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each factor explain differences <b>between countries</b> or <b>within a country</b>?", buckets: [{ label: "Between countries" }, { label: "Within a country" }], items: [
  { text: "Differences in national productivity and technology", b: 0 }, { text: "War and political instability in one country", b: 0 }, { text: "Oil and mineral resources", b: 0 }, { text: "A landlocked location with high transport costs", b: 0 },
  { text: "Higher wages in cities than in the countryside", b: 1 }, { text: "Unequal pay between men and women", b: 1 }, { text: "Some people own property and shares", b: 1 }, { text: "Progressive taxes and benefits narrowing the gap", b: 1 },
], done: "Know both: international differences and distribution inside a country." });
Lib.classify($("#cl2"), { prompt: "Does each <b>raise</b> or <b>lower</b> inequality within a country?", buckets: [{ label: "Raises inequality" }, { label: "Reduces inequality" }], items: [
  { text: "Regressive taxes", b: 0 }, { text: "Wide gaps in education access", b: 0 }, { text: "Ownership of wealth concentrated in few hands", b: 0 }, { text: "Discrimination in hiring", b: 0 },
  { text: "Progressive income tax", b: 1 }, { text: "More generous state benefits", b: 1 }, { text: "Free education and healthcare", b: 1 }, { text: "A national minimum wage", b: 1 },
], done: "Policies that move income from rich to poor reduce inequality." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Income distribution", "How a country's income is shared among its people"],
  ["Quintile", "One fifth (20%) of the population ranked by income"],
  ["Inequality", "A gap in income or wealth between richer and poorer people"],
  ["Urban area", "A city or town"],
  ["Rural area", "A countryside area, often with farming"],
  ["Poverty trap", "A cycle where low income keeps people poor"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why low-income farmers have low living standards</b>.", items: [
  "Small plots and little capital",
  "Low yields and productivity",
  "Low and unstable crop prices and weather risk",
  "Low, seasonal and uncertain income",
  "Little spending on education, healthcare and nutrition",
  "Low living standards",
], done: "A complete 6-mark chain." });
''' + calc_js([
    ("The richest 20% earn $60,000 each and the poorest 20% earn $5,000 each. How many times more do the richest earn?", 12, "60,000 ÷ 5,000 = <b>12 times</b>.", None, None),
    ("The richest 20% of households receive 50% of national income. How much do the other 80% receive (%)?", 50, "100 − 50 = <b>50%</b>.", None, None),
    ("City incomes average $30,000 and rural incomes average $12,000. By what percentage are city incomes higher than rural incomes?", 150, "(30,000 − 12,000) ÷ 12,000 × 100 = <b>150%</b>.", None, None),
    ("A country with a population of 50 million has GDP of $500bn. What is GDP per head ($)?", 10000, "500,000m ÷ 50m = <b>$10,000</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which would most likely increase living standards between countries over time?", ["Falling productivity", "Investment in education and capital", "Civil war", "Falling investment"], 1, "Better capital and skills raise output."),
    ("Which is a likely cause of income inequality within a country?", ["Free education for all", "Wide gaps in skills and wages", "Progressive taxation", "A national minimum wage"], 1, "Differences in skills lead to pay gaps."),
    ("Why may low-income farmers have low living standards?", ["High and stable crop prices", "Low productivity and uncertain incomes", "Easy access to healthcare", "Many machines"], 1, "Low and unstable incomes."),
    ("Average income is the same in two countries. Which statement is correct?", ["Living standards must be the same", "Living standards could differ because distribution differs", "The poor are equally well off", "HDI must be the same"], 1, "An average hides inequality."),
    ("Which is a disadvantage of living in a city?", ["Higher wages", "More jobs", "Higher housing costs and pollution", "Better schools"], 2, "Cities have costs as well as benefits."),
]) + "\n" + cards_js([("Income distribution", "How a country's income is shared among its people."), ("Inequality", "A gap between the incomes or wealth of richer and poorer people."), ("Quintile", "One fifth of the population, ranked by income."), ("Productivity", "Output per worker."), ("Poverty trap", "A cycle in which low income keeps people poor."), ("Urban", "Relating to cities and towns."), ("Rural", "Relating to the countryside."), ("Redistribution", "Moving income from richer to poorer people, for example by progressive taxes and benefits."), ("Tertiary sector", "The service industries, such as banking, tourism and retail.")]) + "labQ(); \n"
explore = '''
  <h2>Lab 1 · Income distribution</h2>
  <p>Average income is $20,000. Make the pre-tax distribution more unequal, then use progressive taxes and benefits to narrow it.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Average income</small><strong id="qa1"></strong></div><div><small>Poorest 20% get</small><strong id="qa2"></strong></div><div><small>Richest 20% share</small><strong id="qa3"></strong></div><div><small>Richest ÷ poorest</small><strong id="qa4"></strong></div></div><div class="verdict" id="qav"></div></div></div>
    <svg id="labQ" viewBox="0 0 760 350" role="img" aria-label="Income by fifth of the population"></svg>
  </div>

  <h2>Lab 2 · Reasons for differences</h2>
  <p>Pick a factor to see how it affects living standards between or within countries.</p>
  <div class="card"><div class="row" id="fxBtns"></div><div id="fxOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain two reasons for differences in living standards between countries. (Oct/Nov 2022, P23)", "Two different reasons, each with a link: productivity, education and health, capital, resources, stability.",
      "[K|One reason is differences in productivity and technology.] [N|Countries with more capital and better technology produce more per worker, so incomes and the goods people can afford are higher.] [K|Another reason is education and health.] [N|Healthy, skilled workers earn more and countries with better schooling and healthcare can grow faster, raising living standards.]"),
    Q(2, "Explain", 4, "Explain two factors that could influence living standards, apart from unemployment rates. (Oct/Nov 2024, P21)", "Income, education, health, cost of living, working hours, environment.",
      "[K|Income or wage levels are one factor.] [N|Higher wages allow people to afford more goods and services, so living standards are higher.] [K|Another factor is the cost of living.] [N|If prices are high relative to incomes, purchasing power is lower and people can afford less.]"),
    Q(3, "Explain", 4, "Explain two reasons why income may be unequally distributed within a country.", "Skills and wages; ownership of wealth; location; tax and benefits; discrimination.",
      "[K|Differences in skills and education lead to differences in wages.] [N|Highly qualified workers can earn much more than unskilled workers, so income is unequal.] [K|Ownership of wealth is also unequal.] [N|People who own property, shares or businesses earn rent, dividends and profits on top of wages, so they can earn much more than those who rely on wages alone.]"),
    Q(4, "Analyse", 6, "Analyse why low-income farmers are likely to have low living standards. (Feb/Mar 2023, P22)", "Chain: low productivity, low and unstable income, little spending on necessities, poor access to services.",
      "[K|Low-income farmers often farm small plots with little capital and old methods, so yields and productivity are low.] [N|Crop prices may be low and unstable and the weather brings risks, so incomes are low and uncertain.] [N|With low income they can afford less food, healthcare and schooling,] [N|which lowers their health, education and ability to raise productivity.] [N|Poor roads and markets may increase costs and cut them off from services, keeping living standards low.]", key=True),
    Q(5, "Analyse", 6, "Analyse how growth in a country's tertiary sector can increase its living standards. (Oct/Nov 2024, P22)", "Services create jobs and income; tax revenue; better services; link to GDP per head.",
      "[K|The tertiary sector provides services such as banking, tourism, health and education.] [N|Growth creates jobs and raises incomes, so spending power and GDP per head could rise.] [N|Higher output and profits raise tax revenue, which the government can spend on schools and hospitals.] [N|The services themselves, such as better healthcare and education, directly improve living standards.] [E|However, the gains may be concentrated in cities or among skilled workers.]", key=True),
    Q(6, "Discuss", 8, "Discuss whether or not people living in cities have a higher living standard than those living in rural areas. (Oct/Nov 2023, P22)", "Cities: wages, jobs, services; costs: housing, congestion, slums, pollution. Rural: lower income but lower costs, cleaner air. End with 'it depends on income, costs and quality of life'.",
      "[K|Living standards describe the goods, services and quality of life people can obtain.] [N|People in cities often have higher wages and more job opportunities, and better access to schools, hospitals, transport and entertainment, which could raise living standards.] [E|This is likely to be more important in poor countries where rural areas lack services.] [N|However, cities have higher housing and living costs, congestion and pollution, and low-paid workers may live in slums.] [N|Rural areas may have lower incomes but also lower costs, cleaner air and stronger communities.] [E|Overall, average living standards are likely to be higher in cities, but it depends on the person's income and housing costs, and on non-income factors such as pollution and leisure.]", key=True),
    Q(7, "Discuss", 6, "Discuss whether or not a cut in income tax rates will increase living standards. (May/June 2022, P22)", "For: higher disposable income. Against: lower tax revenue and public services; benefits high earners; inequality; saving.",
      "[K|A cut in income tax rates raises people's disposable income.] [N|They can afford more goods and services, so living standards could rise, and the incentive to work may increase, raising output.] [N|However, lower tax revenue may mean less government spending on healthcare, schools and benefits, which could reduce living standards, particularly for low-income households.] [N|The gains may also go mainly to higher earners, and people may save the extra income.] [E|Overall, a tax cut could raise living standards for those who gain, but the effect on the whole population depends on how the government pays for it and who benefits most.]", key=True),
)
tp = tips([
    ("Split between and within countries.", "Different factors apply to each."),
    ("Give a link for each factor.", "'Education raises skills, so wages and living standards are higher.'"),
    ("Averages hide distribution.", "Use quintile or rich/poor ideas."),
    ("Name the group affected.", "Farmers, city workers, women, low-skilled workers."),
    ("Evaluate with costs as well as benefits.", "City living costs, pollution, who gains from a tax cut."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("5.1.2 Comparing living standards and income distribution"), "Comparing Living Standards and Income Distribution", "Why living standards differ between countries and why income is unequally distributed within them. Syllabus 5.1.2.",
    learn=learn, watch=watch(("Same average income, different distribution", "stQ"), ("Why poor countries can stay poor", "stP"), ("Low-income farmers", "stF")), explore=explore,
    practise=practise(("Between or within countries?", "cl1", "card"), ("Raises or reduces inequality?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the farmers' chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Norway and Niger", "Norway's real GDP per head is more than 100 times that of Niger. Differences in productivity, capital, education, health, stability and institutions all help to explain the gap.", "Reasons for differences between countries."),
        rw("Cities and slums", "In many fast-growing countries, city incomes are far above rural incomes, but a large share of city dwellers live in informal settlements with poor sanitation.", "Both sides of urban living standards."),
        rw("Oil in Guyana", "A past paper asks whether the discovery of oil is likely to raise living standards in Guyana. The answer depends on who gains and how the revenue is used.", "Natural resources and the distribution of income."),
        rw("Reducing inequality through taxes and benefits", "Countries such as Denmark and Sweden have high taxes and generous benefits and have a smaller gap between rich and poor than many countries with low taxes.", "How taxes and benefits change distribution.")),
    exam=ex, tips=tp)
write("lv2", body, js, "Comparing Living Standards and Income Distribution", "ig-living-standards-comparison")
