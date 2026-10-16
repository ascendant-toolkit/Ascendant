"""Builds the two IGCSE Economics 1.2 Factors of production reviews (1.2.1, 1.2.2).
Run: python3 tools/artifact-kit/mk_ig12.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

# =========================================================== 1.2.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Factors of production</span> are the resources used to make goods and services. There are four: <b>land</b>, <b>labour</b>, <b>capital</b> and <b>enterprise</b>. Each earns a <b>reward</b> (a payment for its use): <b>rent</b>, <b>wages</b>, <b>interest</b> and <b>profit</b>. Because factors are scarce, they have to be allocated, and their rewards are the incomes people earn.</p></div>

  <h2>The four factors and their rewards</h2>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>Definition</th><th>Examples</th><th>Reward</th></tr>
    <tr><td><b>Land</b></td><td>All natural resources: the ground itself and what comes from or on it</td><td>Farmland, oil, minerals, forests, fish, water</td><td><b>Rent</b></td></tr>
    <tr><td><b>Labour</b></td><td>The physical and mental effort of people in production</td><td>Teachers, builders, nurses, engineers</td><td><b>Wages</b> (and salaries)</td></tr>
    <tr><td><b>Capital</b></td><td>Man-made goods used to make other goods and services</td><td>Machinery, factories, tools, computers, roads</td><td><b>Interest</b></td></tr>
    <tr><td><b>Enterprise</b></td><td>The risk-taking and organising of the other factors to produce goods and services</td><td>An entrepreneur starting a business</td><td><b>Profit</b></td></tr>
  </table></div>
  <ul>
    <li><b>Capital</b> here means physical capital, not money. Money used to buy machinery is <b>financial capital</b>; the machines themselves are the factor.</li>
    <li>An <b>entrepreneur</b> takes the risk of losing money, which is why profit (a reward for risk) can be negative.</li>
    <li>Factors can be mobile or not: labour can move between jobs and places, land cannot move.</li>
  </ul>
  <p class="note">A common exam trap: the reward for <b>capital</b> is interest, not profit. Profit is the reward for enterprise.</p>
'''
js = HEAD + COMMON + '''
const FC = ["Land supplies raw materials", "Labour works on them", "Capital (machines) makes the work more productive", "Enterprise organises the other three and takes the risk", "Goods and services are produced", "Owners earn rent, wages, interest and profit"];
Lib.stepper($("#stF"), { w: 760, h: 420, label: "Four factors make a product", base: { n: 0 }, draw: mkChain(FC, "--accent"), steps: chainSteps(["<b>Land</b> supplies raw materials such as timber.", "<b>Labour</b> works on them.", "<b>Capital</b> (machines and tools) makes the work more productive.", "<b>Enterprise</b> organises the other three and takes the risk.", "<b>Goods and services</b> are produced and sold.", "Owners of the factors earn <b>rent, wages, interest and profit</b>."]) });
function bakeChart(s) {
  const items = [["Land", "Flour from wheat fields", "--good"], ["Labour", "Bakers", "--accent"], ["Capital", "Ovens, mixers", "--warn"], ["Enterprise", "Owner who risks money", "--bad"]]; let o = SV.text(60, 26, "A bakery", "sm");
  items.forEach(([n, d, c], i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 60 + i * 170; o += `<g opacity="${op}">` + SV.rect(x, 60, 150, 90, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, 100, n, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:16px" }) + SV.text(x + 75, 125, d, "sm", { "text-anchor": "middle", style: "fill:#fff;font-size:11px" }) + SV.text(x + 75, 190, ["Rent", "Wages", "Interest", "Profit"][i], "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, 210, "is the reward", "sm", { "text-anchor": "middle" }) + "</g>"; });
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 240, label: "A bakery's factors and rewards", base: { n: 0 }, draw: bakeChart, steps: [
  { cap: "<b>Land:</b> the wheat fields that supply flour. Reward: <b>rent</b>.", s: { n: 1 } },
  { cap: "<b>Labour:</b> bakers. Reward: <b>wages</b>.", s: { n: 2 } },
  { cap: "<b>Capital:</b> ovens and mixers. Reward: <b>interest</b>.", s: { n: 3 } },
  { cap: "<b>Enterprise:</b> the owner who organises and risks money. Reward: <b>profit</b>.", s: { n: 4 } },
] });

/* Lab 1: income shares */
function labR() {
  if (!$("#ra") || !$("#rb") || !$("#rc") || !$("#rd")) return;
  const v = [+$("#ra").value, +$("#rb").value, +$("#rc").value, +$("#rd").value], tot = v.reduce((a, b) => a + b, 0), nm = ["Rent (land)", "Wages (labour)", "Interest (capital)", "Profit (enterprise)"], cl = ["--good", "--accent", "--warn", "--bad"];
  $("#ra1").textContent = "$" + tot; $("#ra2").textContent = money(tot ? (v[1] / tot) * 100 : 0, 0) + "%"; $("#ra3").textContent = nm[v.indexOf(Math.max(...v))].split(" ")[0];
  $("#rav").textContent = `A firm sells $${tot} of output and shares it between the factors: rent $${v[0]}, wages $${v[1]}, interest $${v[2]}, profit $${v[3]}. Wages take ${money(tot ? (v[1] / tot) * 100 : 0, 0)}% of the total. The more a firm pays one factor, the less is left for the others (scarcity again).`;
  const base = 280, k = 200 / Math.max(...v, 1); let o = SV.line(60, base, 700, base);
  v.forEach((x, i) => { const px = 100 + i * 150, h = x * k; o += SV.rect(px, base - h, 110, h, "", { style: `fill:var(${cl[i]})`, opacity: 0.85 }) + SV.text(px + 55, base - h - 8, "$" + x, "lbl bd", { "text-anchor": "middle" }) + SV.text(px + 55, base + 20, nm[i], "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  $("#labR").innerHTML = o;
}
[["g1", "ra", "Rent paid to landowners", 10], ["g2", "rb", "Wages paid to workers", 50], ["g3", "rc", "Interest paid on capital", 15], ["g4", "rd", "Profit kept by the entrepreneur", 25]].forEach(([g, id, l, v]) => Lib.slider($("#" + g), { id, label: l, min: 0, max: 100, step: 5, value: v, fmt: (x) => "$" + x, onInput: labR }));
const FF = [
  { n: "A farm field", f: "Land", r: "Rent" }, { n: "A teacher", f: "Labour", r: "Wages" }, { n: "A delivery lorry", f: "Capital", r: "Interest" },
  { n: "A person who starts a café and risks savings", f: "Enterprise", r: "Profit" }, { n: "An oil well", f: "Land", r: "Rent" }, { n: "A computer in an office", f: "Capital", r: "Interest" },
];
button_table("ffBtns", "ffOut", FF, 0, (p) => `<div class="tw"><table class="t"><tr><th>Factor</th><th>Reward</th></tr><tr><td><b>${p.f}</b></td><td>${p.r}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>factor of production</b> is each?", buckets: [{ label: "Land" }, { label: "Labour" }, { label: "Capital" }, { label: "Enterprise" }], items: [
  { text: "A copper mine", b: 0 }, { text: "A forest", b: 0 },
  { text: "A nurse", b: 1 }, { text: "A builder", b: 1 },
  { text: "A factory machine", b: 2 }, { text: "A tractor", b: 2 },
  { text: "An entrepreneur starting a business", b: 3 }, { text: "Taking the risk of a new product", b: 3 },
], done: "Land, labour, capital, enterprise." });
Lib.match($("#m1"), { prompt: "Match each factor to its reward.", pairs: [
  ["Land", "Rent"], ["Labour", "Wages"], ["Capital", "Interest"], ["Enterprise", "Profit"],
  ["Financial capital", "Money used to buy machinery"], ["Physical capital", "Machines used to make goods"],
], done: "Learn all four pairs." });
Lib.classify($("#cl2"), { prompt: "Which <b>reward</b> goes to the owner of each?", buckets: [{ label: "Rent" }, { label: "Wages" }, { label: "Interest" }, { label: "Profit" }], items: [
  { text: "A landowner leasing a field", b: 0 }, { text: "A worker's monthly pay", b: 1 }, { text: "A firm's machines (capital)", b: 2 }, { text: "The risk-taking owner of a business", b: 3 },
  { text: "A farm leased to a farmer", b: 0 }, { text: "A salary", b: 1 },
], done: "Reward follows the factor." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how factors of production earn incomes</b>.", items: [
  "Firms combine land, labour, capital and enterprise",
  "Goods and services are produced and sold",
  "Revenue is earned by the firm",
  "The firm pays rent, wages and interest",
  "The entrepreneur keeps the profit",
], done: "Revenue is shared between the factors." });
''' + calc_js([
    ("A firm earns $500,000 revenue and pays $100,000 wages, $50,000 rent and $30,000 interest. Ignoring other costs, what is profit ($)?", 320000, "500,000 − 100,000 − 50,000 − 30,000 = <b>$320,000</b>.", None, None),
    ("Wages are $60,000 of a firm's $200,000 costs. What percentage is this?", 30, "60 ÷ 200 × 100 = <b>30%</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is the reward to capital?", ["Rent", "Wages", "Interest", "Profit"], 2, "Capital earns interest."),
    ("What is the reward to enterprise?", ["Rent", "Wages", "Interest", "Profit"], 3, "A reward for risk-taking."),
    ("Which is an example of land?", ["A factory", "Oil reserves", "A worker", "Money"], 1, "A natural resource."),
    ("Which is an example of capital?", ["A forest", "A tractor", "A manager's effort", "Fish in the sea"], 1, "Man-made, used to produce."),
    ("Labour is rewarded with:", ["Rent", "Wages", "Interest", "Profit"], 1, "Wages."),
]) + "\n" + cards_js([("Factors of production", "The resources used to produce goods and services: land, labour, capital and enterprise."), ("Land", "All natural resources."), ("Labour", "The physical and mental effort of people in production."), ("Capital", "Man-made goods used to produce other goods and services."), ("Enterprise", "Organising the factors of production and taking risks."), ("Rent", "The reward for land."), ("Wages", "The reward for labour."), ("Interest", "The reward for capital."), ("Profit", "The reward for enterprise.")]) + "labR(); \n"
explore = '''
  <h2>Lab 1 · Sharing out revenue</h2>
  <p>Set how much a firm pays to each factor. The chart shows the rewards.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>Total rewards</small><strong id="ra1"></strong></div><div><small>Wages' share</small><strong id="ra2"></strong></div><div><small>Largest reward</small><strong id="ra3"></strong></div></div><div class="verdict" id="rav"></div></div></div>
    <svg id="labR" viewBox="0 0 760 320" role="img" aria-label="Rewards to the four factors"></svg>
  </div>

  <h2>Lab 2 · Which factor and reward?</h2>
  <p>Pick an example to see its factor and reward.</p>
  <div class="card"><div class="row" id="ffBtns"></div><div id="ffOut"></div></div>
'''
ex = exam(
    Q(1, "Identify", 2, "Identify the reward to labour and the reward to land. (Oct/Nov 2021, P22 style)", "Wages; rent.", "[K|Wages (reward to labour).] [K|Rent (reward to land).]"),
    Q(2, "Identify", 2, "Identify two rewards to factors of production. (May/June 2022, P22 style)", "Any two: rent, wages, interest, profit.", "[K|Wages (or rent).] [K|Interest (or profit).]"),
    Q(3, "Define", 2, "Define capital as a factor of production.", "Man-made goods used to produce other goods and services.", "[K|Capital is man-made goods,] [K|such as machinery, used to produce other goods and services.]"),
    Q(4, "Explain", 4, "Explain the role of enterprise as a factor of production.", "Organises other factors; takes risks; profit.",
      "[K|Enterprise organises land, labour and capital to produce goods and services.] [N|The entrepreneur takes risks because the business could make a loss.] [N|The reward for taking the risk is profit.]"),
    Q(5, "Explain", 4, "Explain the difference between land and capital as factors of production.", "Natural vs man-made; rent vs interest.",
      "[K|Land is natural resources such as oil, forests and farmland,] [N|whereas capital is man-made, such as machines.] [K|Land earns rent] [N|while capital earns interest.]"),
)
tp = tips([
    ("Four factors, four rewards:", "land-rent, labour-wages, capital-interest, enterprise-profit."),
    ("Capital means machines, not money.", "Money is financial capital."),
    ("Land includes all natural resources.", "Oil, fish, forests, not only fields."),
    ("Link examples to a factor.", "A tractor is capital; a farmer's effort is labour."),
], cmds("Identify", "Define", "Explain"))
body = page(CL("1.2.1 Factors of production and their rewards"), "Factors of Production and Their Rewards", "Land, labour, capital and enterprise, and the rewards of rent, wages, interest and profit. Syllabus 1.2.1.",
    learn=learn, watch=watch(("Four factors make a product", "stF"), ("A bakery's factors and rewards", "stB")), explore=explore,
    practise=practise(("Which factor?", "cl1", "card"), ("Match factor to reward", "m1", "card"), ("Which reward?", "cl2", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("A coffee shop", "The building and land earn rent, baristas earn wages, the machines earn a return as capital, and the owner takes the risk and earns profit.", "All four factors in one business."),
        rw("Oil-rich countries", "Countries such as Saudi Arabia have a large amount of land in the form of oil reserves, which brings in income.", "Land as a natural resource."),
        rw("A technology start-up", "The founders take large risks and may earn big profits or lose their money.", "Enterprise and profit."),
        rw("Farming", "A farmer may rent land, hire workers, buy a tractor and take the risk of a poor harvest.", "Four factors in agriculture.")),
    exam=ex, tips=tp)
write("e21", body, js, "Factors of Production and Their Rewards", "ig-factors-rewards")

# =========================================================== 1.2.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The <b>quantity</b> of a factor is how much of it is available; the <b>quality</b> is how productive each unit is. Both can <b>increase</b> over time (or fall), which changes how much an economy can produce. Changes in the quantity and quality of factors are the main causes of <b>economic growth</b> and shifts in the PPC (production possibility curve).</p></div>

  <h2>What changes quantity and quality</h2>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>Causes of a change in <b>quantity</b></th><th>Causes of a change in <b>quality</b></th></tr>
    <tr><td><b>Land</b></td><td>Discovery of new resources (oil, minerals); reclaiming land from the sea; depletion or exhaustion of resources; loss of land to flooding or building</td><td>Fertilisers and irrigation improve soil; pollution and soil erosion reduce it</td></tr>
    <tr><td><b>Labour</b></td><td>Population growth, <b>immigration</b> or emigration; ageing; changes in the retirement age; more people working (women, older workers)</td><td>Education, training, better health and nutrition; learning by experience; brain drain reduces skills</td></tr>
    <tr><td><b>Capital</b></td><td>Investment in new machinery, factories, infrastructure; depreciation and wear and tear</td><td>Technological advances: more efficient, faster machines and software</td></tr>
    <tr><td><b>Enterprise</b></td><td>More people starting businesses; government support, access to finance, lower taxes on start-ups</td><td>Better business skills, training and access to knowledge and technology</td></tr>
  </table></div>

  <h2>Consequences</h2>
  <ul>
    <li>More factors or better-quality factors increase an economy's <b>productive capacity</b>: it can make more goods and services (<b>economic growth</b>).</li>
    <li>Higher quality raises <b>productivity</b> (output per worker or per unit of capital), lowering costs.</li>
    <li>Falls in quantity or quality, such as a natural disaster, depletion or brain drain, reduce potential output.</li>
    <li>Mobility matters: factors that can move to where they are needed (labour moving to new jobs) are used more efficiently.</li>
  </ul>
  <p class="note">Quantity and quality are often linked: investing in capital raises quantity and, with new technology, quality too.</p>
'''
js = HEAD + COMMON + '''
const QT = ["More investment in machinery and technology", "Capital stock rises and improves", "Workers are more productive", "Productive capacity rises", "The economy can produce more goods and services: growth"];
Lib.stepper($("#stQ"), { w: 760, h: 380, label: "Better capital raises capacity", base: { n: 0 }, draw: mkChain(QT, "--good"), steps: chainSteps(["More <b>investment</b> in machinery and technology.", "The <b>capital stock</b> rises and improves in quality.", "Workers are <b>more productive</b>.", "<b>Productive capacity</b> rises.", "The economy can produce more goods and services: <b>growth</b>."]) });
const LB = ["The government spends more on education and training", "Workers gain skills and better health", "The quality of labour improves", "Output per worker (productivity) rises", "Costs fall and output can rise"];
Lib.stepper($("#stL"), { w: 760, h: 380, label: "Better labour", base: { n: 0 }, draw: mkChain(LB, "--accent"), steps: chainSteps(["The government spends more on <b>education and training</b>.", "Workers gain <b>skills and better health</b>.", "The <b>quality of labour</b> improves.", "<b>Output per worker</b> (productivity) rises.", "Costs fall and output can rise."]) });
const DP = ["Resources such as oil or fish are used up faster than they are replaced", "The quantity of land falls", "Output from that resource falls", "Incomes and jobs fall; the country may need to import"];
Lib.stepper($("#stD"), { w: 760, h: 340, label: "Depletion", base: { n: 0 }, draw: mkChain(DP, "--bad"), steps: chainSteps(["Resources such as oil or fish are used up <b>faster than they are replaced</b>.", "The <b>quantity</b> of the resource falls.", "<b>Output</b> from that resource falls.", "Incomes and jobs fall; the country may need to <b>import</b>."]) });

/* Lab 1: capacity */
function labC() {
  if (!$("#ca") || !$("#cb") || !$("#cc")) return;
  const q = +$("#ca").value / 100, ql = +$("#cb").value / 100, cap = +$("#cc").value / 100, base0 = 100, out = base0 * (1 + q) * (1 + ql) * (1 + cap), g = out - base0;
  $("#ca1").textContent = money(out, 0); $("#ca2").textContent = (g >= 0 ? "+" : "−") + money(Math.abs(g), 0) + "%"; $("#ca3").textContent = money((1 + ql) * (1 + cap) * 100 - 100, 0) + "%";
  $("#cav").textContent = `Labour quantity ${q >= 0 ? "+" : ""}${Math.round(q * 100)}%, labour quality ${Math.round(ql * 100)}% and capital ${Math.round(cap * 100)}%: potential output moves from 100 to ${money(out, 0)} (${money(g, 0)}%). Improving quality raises output per worker (productivity) even if the number of workers does not change.`;
  const base = 290, k = 1.6; let o = SV.line(60, base, 700, base);
  [["Before", base0, "--accent"], ["After", out, g >= 0 ? "--good" : "--bad"]].forEach(([n, v, cl], i) => { const x = 160 + i * 250, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${cl})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o + SV.text(60, 24, "Potential output (index, before = 100)", "sm");
}
Lib.slider($("#g1"), { id: "ca", label: "Change in the number of workers", min: -20, max: 30, step: 5, value: 5, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labC });
Lib.slider($("#g2"), { id: "cb", label: "Change in worker skills (quality)", min: -10, max: 30, step: 5, value: 10, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labC });
Lib.slider($("#g3"), { id: "cc", label: "Change in capital stock and technology", min: -10, max: 30, step: 5, value: 10, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labC });
const CE = [
  { n: "Discovery of oil", f: "Land", t: "Quantity", d: "Increase" },
  { n: "Soil erosion", f: "Land", t: "Quality", d: "Decrease" },
  { n: "Immigration", f: "Labour", t: "Quantity", d: "Increase" },
  { n: "More education and training", f: "Labour", t: "Quality", d: "Increase" },
  { n: "Brain drain (skilled workers leave)", f: "Labour", t: "Quality", d: "Decrease" },
  { n: "Investment in new factories", f: "Capital", t: "Quantity", d: "Increase" },
  { n: "New technology", f: "Capital", t: "Quality", d: "Increase" },
  { n: "Government support for start-ups", f: "Enterprise", t: "Quantity", d: "Increase" },
];
button_table("ceBtns", "ceOut", CE, 0, (p) => `<div class="tw"><table class="t"><tr><th>Factor</th><th>Quantity or quality</th><th>Direction</th></tr><tr><td><b>${p.f}</b></td><td>${p.t}</td><td>${p.d}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each change the <b>quantity</b> or the <b>quality</b> of a factor?", buckets: [{ label: "Quantity" }, { label: "Quality" }], items: [
  { text: "Immigration of workers", b: 0 }, { text: "New oil discovered", b: 0 }, { text: "Building new factories", b: 0 }, { text: "More people start businesses", b: 0 },
  { text: "Training that raises skills", b: 1 }, { text: "Better technology in machines", b: 1 }, { text: "Fertilisers improve the soil", b: 1 }, { text: "Better health among workers", b: 1 },
], done: "More units, or better units." });
Lib.classify($("#cl2"), { prompt: "Does each <b>increase</b> or <b>decrease</b> the factor?", buckets: [{ label: "Increase" }, { label: "Decrease" }], items: [
  { text: "Discovery of new minerals", b: 0 }, { text: "Investment in education", b: 0 }, { text: "New technology", b: 0 }, { text: "Immigration of skilled workers", b: 0 },
  { text: "Depletion of fish stocks", b: 1 }, { text: "Brain drain", b: 1 }, { text: "Machines wearing out (depreciation)", b: 1 }, { text: "A flood destroying farmland", b: 1 },
], done: "Know both directions." });
Lib.match($("#m1"), { prompt: "Match the cause to its effect.", pairs: [
  ["Education and training", "Higher quality of labour"],
  ["Immigration", "Larger labour force"],
  ["Investment in machinery", "Larger capital stock"],
  ["Discovery of oil", "More land (natural resources)"],
  ["Brain drain", "Lower quality of labour"],
  ["Depreciation", "Capital wears out"],
], done: "Link each cause to its effect." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how education improves the economy</b>.", items: [
  "The government invests in education and training",
  "Workers gain skills",
  "Labour productivity rises",
  "Output rises and costs fall",
  "Economic growth increases",
], done: "Quality leads to growth." });
''' + calc_js([
    ("A labour force of 20 million grows by 5%. How many workers are there now (million)?", 21, "20 × 1.05 = <b>21 million</b>.", None, None),
    ("Output is 200 units from 20 workers. What is output per worker?", 10, "200 ÷ 20 = <b>10 units</b>.", None, None),
    ("After training, output rises to 240 units with the same 20 workers. By what percentage does productivity rise?", 20, "(12 − 10) ÷ 10 × 100 = <b>20%</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which would increase the quantity of labour?", ["Training", "Immigration", "Better technology", "Higher wages for few"], 1, "More workers."),
    ("Which would improve the quality of labour?", ["Education and training", "Emigration", "Depreciation", "Population growth"], 0, "More skilled."),
    ("Investment in new machinery changes:", ["Quantity of capital", "Quantity of land", "Quality of enterprise only", "Nothing"], 0, "More capital."),
    ("A brain drain:", ["Raises labour quality", "Lowers labour quality", "Raises quantity of land", "Has no effect"], 1, "Skilled workers leave."),
    ("A cause of growth in an economy's factors is:", ["Depletion", "Technological advance", "Flooding", "Depreciation"], 1, "Raises quality of capital."),
]) + "\n" + cards_js([("Quantity of factors", "How much of a factor is available."), ("Quality of factors", "How productive each unit of a factor is."), ("Productivity", "Output per worker or per unit of input."), ("Investment", "Spending on capital goods."), ("Depreciation", "The wearing out of capital over time."), ("Immigration", "People moving into a country to live and work."), ("Brain drain", "The emigration of skilled and educated workers."), ("Depletion", "Using up natural resources."), ("Productive capacity", "The maximum output an economy can produce.")]) + "labC(); \n"
explore = '''
  <h2>Lab 1 · Changing quantity and quality</h2>
  <p>Change the number of workers, their skills and the capital stock. The chart shows potential output (before = 100).</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Potential output</small><strong id="ca1"></strong></div><div><small>Change</small><strong id="ca2"></strong></div><div><small>Productivity gain</small><strong id="ca3"></strong></div></div><div class="verdict" id="cav"></div></div></div>
    <svg id="labC" viewBox="0 0 760 330" role="img" aria-label="Potential output before and after"></svg>
  </div>

  <h2>Lab 2 · Causes of change</h2>
  <p>Pick a cause to see which factor it affects, whether it is quantity or quality, and the direction.</p>
  <div class="card"><div class="row" id="ceBtns"></div><div id="ceOut"></div></div>
'''
ex = exam(
    Q(1, "Identify", 2, "Identify two causes of the increase in the quantity of a country's factors of production. (Feb/Mar 2022, P22 style)", "Any two: immigration, discovery of resources, investment in capital, more enterprise.", "[K|Immigration (more labour).] [K|Investment in machinery (more capital) or discovery of new resources.]"),
    Q(2, "Explain", 4, "Explain two ways the quality of labour can be improved.", "Education, training, healthcare; productivity.",
      "[K|Education and training can increase workers' skills,] [N|so they produce more per hour.] [K|Better healthcare and nutrition keep workers healthy,] [N|so they work harder and take fewer days off.]"),
    Q(3, "Explain", 4, "Explain why a country's capital stock may increase.", "Investment; technology; depreciation offset.",
      "[K|Firms and the government may invest in new machinery, factories and infrastructure.] [N|If investment is greater than depreciation the stock of capital rises.] [N|This increases productive capacity.]"),
    Q(4, "Analyse", 6, "Analyse how an increase in the quantity and quality of its factors of production could affect an economy.", "Capacity, productivity, growth, PPC shift, costs.",
      "[K|An increase in the quantity of land, labour or capital means the economy can produce more.] [N|Better quality, through training and technology, raises productivity so output per worker rises.] [N|Costs of production fall and the economy's productive capacity rises, which is economic growth and an outward shift of the PPC.] [E|The effect depends on whether the extra factors are used and on whether demand rises to match.]", key=True),
    Q(5, "Analyse", 6, "Analyse the influences on the mobility of two factors of production. (Oct/Nov 2022, P22 style)", "Labour: skills, housing, family ties. Capital: specificity, transport costs.",
      "[K|Labour mobility is influenced by skills and training: workers need the right qualifications to move to a new job.] [N|Housing costs, family ties and language also make it harder to move.] [K|Capital mobility depends on how specific the machinery is,] [N|a specialised machine cannot easily be used in another industry, and moving large machines costs money.] [E|Mobility is usually higher for general-purpose factors and in the long run.]", key=True),
)
tp = tips([
    ("Quantity = more units; quality = better units.", "State which one."),
    ("Link to growth.", "More or better factors shift the PPC outwards."),
    ("Name specific causes.", "Immigration, investment, training, technology, discovery of resources."),
    ("Productivity is output per unit of input.", "Use it for quality."),
    ("Evaluate with time lags.", "Education and investment take years to pay off."),
], cmds("Identify", "Explain", "Analyse"))
body = page(CL("1.2.2 Quantity and quality of factors of production"), "Quantity and Quality of Factors of Production", "What increases or decreases the quantity and quality of land, labour, capital and enterprise. Syllabus 1.2.2.",
    learn=learn, watch=watch(("Better capital raises capacity", "stQ"), ("Better labour", "stL"), ("Depletion", "stD")), explore=explore,
    practise=practise(("Quantity or quality?", "cl1", "card"), ("Increase or decrease?", "cl2", "card"), ("Match the cause", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Immigration and labour supply", "Many countries have grown their labour force through immigration, which adds workers and can fill skill gaps.", "Quantity of labour."),
        rw("Education in South Korea", "Large investment in education helped raise the skills of its workforce and supported fast growth.", "Quality of labour."),
        rw("Oil discoveries", "New oil and gas finds add to a country's land resources and can raise exports and incomes.", "Quantity of land."),
        rw("Fishing and depletion", "Over-fishing has reduced fish stocks in many regions, cutting future output and jobs.", "Depletion of land resources."),
        rw("Automation", "Robots and software raise the quality of capital and productivity in factories.", "Quality of capital.")),
    exam=ex, tips=tp)
write("e22", body, js, "Quantity and Quality of Factors of Production", "ig-factors-quantity-quality")
