"""Builds the two IGCSE Economics 1.3 Opportunity cost reviews (1.3.1, 1.3.2).
Run: python3 tools/artifact-kit/mk_ig13.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

# =========================================================== 1.3.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Opportunity cost</span> is the <b>next best alternative given up</b> when a choice is made. It is not the cost of everything you give up, only the <b>single best alternative</b>. Because resources are scarce, every choice has an opportunity cost, except for <b>free goods</b>, which use no scarce resources.</p></div>

  <h2>Working it out</h2>
  <p>List your options, rank them, choose one. The opportunity cost is the <b>one ranked next</b>.</p>
  <div class="tw"><table class="t">
    <tr><th>You have $50 and choose to buy…</th><th>Your ranking of options</th><th>Opportunity cost</th></tr>
    <tr><td>Concert tickets</td><td>1. Concert tickets &nbsp; 2. New trainers &nbsp; 3. Meal out</td><td><b>The trainers</b> (not trainers and the meal)</td></tr>
  </table></div>

  <h2>Examples in different contexts</h2>
  <div class="tw"><table class="t">
    <tr><th>Context</th><th>Choice</th><th>Opportunity cost</th></tr>
    <tr><td><b>Consumer</b></td><td>Spend $30 on a game</td><td>The next best thing the $30 could have bought</td></tr>
    <tr><td><b>Worker</b></td><td>Spend two years on an apprenticeship</td><td>The wages that could have been earned in a full-time job</td></tr>
    <tr><td><b>Leisure time</b></td><td>Cycle for an afternoon</td><td>The next best use of the time: studying, earning or relaxing</td></tr>
    <tr><td><b>Firm</b></td><td>Invest in new technology</td><td>Spending on advertising or on paying higher wages</td></tr>
    <tr><td><b>Farmer</b></td><td>Grow apples on a field</td><td>The next best crop that could have been grown</td></tr>
    <tr><td><b>Government</b></td><td>Spend on roads</td><td>The hospitals or schools that could have been funded</td></tr>
    <tr><td><b>Country</b></td><td>Produce more capital goods</td><td>The consumer goods given up (shown on a PPC)</td></tr>
  </table></div>
  <p class="note"><b>Free goods</b> such as sunshine have <b>no opportunity cost</b>: no scarce resources are used, so nothing is given up. Opportunity cost is not always measured in money: time and benefits count too.</p>
'''
js = HEAD + COMMON + '''
const OP = ["Resources are scarce", "A choice must be made between alternatives", "One option is chosen", "The next best alternative is given up", "That is the opportunity cost"];
Lib.stepper($("#stO"), { w: 760, h: 380, label: "From scarcity to opportunity cost", base: { n: 0 }, draw: mkChain(OP, "--accent"), steps: chainSteps(["Resources are <b>scarce</b>.", "A <b>choice</b> must be made between alternatives.", "<b>One option</b> is chosen.", "The <b>next best alternative</b> is given up.", "That is the <b>opportunity cost</b>."]) });
function rankChart(s) {
  const opts = [["Concert", 1], ["Trainers", 2], ["Meal out", 3]]; let o = SV.text(60, 26, "You have $50 and can do one thing", "sm");
  opts.forEach(([n, r], i) => { const x = 80 + i * 210, chosen = s.n >= 1 && r === 1, oc = s.n >= 2 && r === 2, lost = s.n >= 3 && r === 3; const c = chosen ? "--good" : oc ? "--bad" : "--accent", op = lost ? 0.35 : 0.85; o += SV.rect(x, 60, 180, 110, "", { style: `fill:var(${c})`, opacity: op }) + SV.text(x + 90, 105, n, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:16px" }) + SV.text(x + 90, 130, "Rank " + r, "sm", { "text-anchor": "middle", style: "fill:#fff" }) + (chosen ? SV.text(x + 90, 200, "CHOSEN", "lbl bd t3", { "text-anchor": "middle" }) : "") + (oc ? SV.text(x + 90, 200, "OPPORTUNITY COST", "lbl bd t2", { "text-anchor": "middle", style: "font-size:12px" }) : "") + (lost ? SV.text(x + 90, 200, "also given up, but not the cost", "sm", { "text-anchor": "middle", style: "font-size:11px" }) : ""); });
  return o;
}
Lib.stepper($("#stR"), { w: 760, h: 240, label: "Ranking the alternatives", base: { n: 0 }, draw: rankChart, steps: [
  { cap: "You rank three options for your $50: concert, trainers, meal out.", s: { n: 0 } },
  { cap: "You choose the <b>concert</b> (your first choice).", s: { n: 1 } },
  { cap: "The <b>opportunity cost</b> is your second choice only: the <b>trainers</b>.", s: { n: 2 } },
  { cap: "The meal out is also not bought, but it is <b>not</b> the opportunity cost: only the next best alternative counts.", s: { n: 3 } },
] });

/* Lab 1: choose */
const OPTS = [["Concert tickets", 7], ["New trainers", 8], ["Meal out", 5], ["Save the money", 4]];
function labO() {
  if (!$("#oa")) return;
  const i = +$("#oa").value, chosen = OPTS[i], rest = OPTS.filter((_, j) => j !== i).sort((a, b) => b[1] - a[1]), nb = rest[0];
  $("#oa1").textContent = chosen[0]; $("#oa2").textContent = nb[0]; $("#oa3").textContent = nb[1] + " / 10";
  $("#oav").textContent = `You choose ${chosen[0]} (value ${chosen[1]}/10 to you). The alternatives ranked by value are ${rest.map((r) => r[0] + " " + r[1]).join(", ")}. The opportunity cost is the best of them: ${nb[0]}. Choose a different option and the opportunity cost can change.`;
  const base = 280; let o = SV.line(60, base, 700, base);
  OPTS.forEach(([n, v], j) => { const x = 90 + j * 150, h = v * 22, c = j === i ? "--good" : n === nb[0] ? "--bad" : "--accent"; o += SV.rect(x, base - h, 110, h, "", { style: `fill:var(${c})`, opacity: j === i || n === nb[0] ? 0.9 : 0.4 }) + SV.text(x + 55, base - h - 8, v, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 55, base + 20, n, "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  $("#labO").innerHTML = o + SV.text(60, 24, "Green: chosen. Red: opportunity cost.", "sm");
}
Lib.slider($("#g1"), { id: "oa", label: "Choose an option (0 to 3)", min: 0, max: 3, step: 1, value: 0, fmt: (v) => OPTS[v][0], onInput: labO });
const OE = [
  { n: "A student studies instead of working a part-time job", c: "The wages from the job" },
  { n: "A government builds a road", c: "The hospital or school that could have been built" },
  { n: "A farmer grows wheat on a field", c: "The next best crop (e.g. barley)" },
  { n: "A firm buys a new machine", c: "The next best use of the money (e.g. advertising)" },
  { n: "A person takes a two-year apprenticeship", c: "The wages from a full-time job over the two years" },
  { n: "A country makes more weapons", c: "The consumer goods given up" },
];
button_table("oeBtns", "oeOut", OE, 0, (p) => `<div class="tw"><table class="t"><tr><th>Opportunity cost</th></tr><tr><td><b>${p.c}</b></td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>decision-maker</b> faces each opportunity cost?", buckets: [{ label: "Consumer" }, { label: "Worker" }, { label: "Firm" }, { label: "Government" }], items: [
  { text: "The trainers given up to buy a game", b: 0 }, { text: "The meal out given up for concert tickets", b: 0 },
  { text: "Wages lost while doing an apprenticeship", b: 1 }, { text: "Leisure given up for overtime", b: 1 },
  { text: "Advertising given up for new machinery", b: 2 }, { text: "The next best crop on a farm", b: 2 },
  { text: "Schools given up to build roads", b: 3 }, { text: "Hospitals given up to fund defence", b: 3 },
], done: "Everyone gives up the next best alternative." });
Lib.classify($("#cl2"), { prompt: "Does each have an <b>opportunity cost</b>?", buckets: [{ label: "Has an opportunity cost" }, { label: "No opportunity cost" }], items: [
  { text: "Building a hospital", b: 0 }, { text: "Buying a phone", b: 0 }, { text: "Studying for a degree", b: 0 }, { text: "Using a field for wheat", b: 0 },
  { text: "Enjoying sunshine", b: 1 }, { text: "Breathing fresh air in the open", b: 1 }, { text: "Rain falling on a garden", b: 1 },
], done: "Only free goods have no opportunity cost." });
Lib.match($("#m1"), { prompt: "Match the choice to its opportunity cost.", pairs: [
  ["Going to university", "Wages from a job"],
  ["Building a road", "A hospital"],
  ["Growing apples", "The next best crop"],
  ["Producing consumer goods", "Capital goods given up"],
  ["Using leisure time to cycle", "Studying or earning"],
  ["A free good", "No opportunity cost"],
], done: "Learn these examples." });
Lib.order($("#o1"), { prompt: "Put the steps in order: <b>working out an opportunity cost</b>.", items: [
  "List the alternatives",
  "Rank them from best to worst",
  "Choose the best",
  "The second best is given up",
  "That second best is the opportunity cost",
], done: "The next best alternative." });
''' + calc_js([
    ("You have $20 and can buy a book ($20), a cinema ticket ($20) or two snacks ($20). You choose the cinema and your next best is the book. What is the opportunity cost?", 1, "<b>One book</b>: the next best alternative.", None, None),
    ("A farmer can grow 40 tonnes of wheat or 30 tonnes of barley on a field. If wheat is grown, how many tonnes of barley are given up?", 30, "<b>30 tonnes</b> of barley.", None, None),
    ("An apprenticeship lasts 2 years. A full-time job would pay $15,000 a year. What wages are given up ($)?", 30000, "2 × 15,000 = <b>$30,000</b>.", None, None),
]) + mcq_js("qz1", [
    ("Opportunity cost is:", ["The money price", "The next best alternative given up", "All alternatives given up", "The first choice"], 1, "Only the next best."),
    ("What is the opportunity cost of building a road?", ["The cost of materials only", "Another project that could have been funded", "Nothing", "The road itself"], 1, "Resources used elsewhere."),
    ("Which has no opportunity cost?", ["A free good", "A car", "Healthcare", "A house"], 0, "Free goods."),
    ("A worker doing a 2-year apprenticeship gives up:", ["Nothing", "Wages from a job", "Leisure only", "All jobs"], 1, "Lost earnings."),
    ("Opportunity cost exists because:", ["Wants are limited", "Resources are scarce", "Money exists", "Taxes exist"], 1, "Scarcity forces choice."),
]) + "\n" + cards_js([("Opportunity cost", "The next best alternative given up when a choice is made."), ("Choice", "Selecting between alternatives."), ("Scarcity", "Limited resources compared with unlimited wants."), ("Trade-off", "Giving up one thing to get another."), ("Alternative", "Another option that could have been chosen."), ("Free good", "A good with no opportunity cost because it is not scarce."), ("Economic good", "A scarce good that uses resources."), ("Apprenticeship", "Paid work with training, usually lasting a few years."), ("Resource allocation", "How scarce resources are shared between uses.")]) + "labO(); \n"
explore = '''
  <h2>Lab 1 · Find the opportunity cost</h2>
  <p>You have $50 and four options, each worth a score out of 10 to you. Choose one and see the opportunity cost.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Chosen</small><strong id="oa1"></strong></div><div><small>Opportunity cost</small><strong id="oa2"></strong></div><div><small>Value given up</small><strong id="oa3"></strong></div></div><div class="verdict" id="oav"></div></div></div>
    <svg id="labO" viewBox="0 0 760 320" role="img" aria-label="Chosen option and next best alternative"></svg>
  </div>

  <h2>Lab 2 · Opportunity costs in context</h2>
  <p>Pick a choice to see its opportunity cost.</p>
  <div class="card"><div class="row" id="oeBtns"></div><div id="oeOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define opportunity cost. (May/June 2021, P22 style)", "Next best alternative given up.", "[K|Opportunity cost is the next best alternative] [K|that is given up when a choice is made.]"),
    Q(2, "Identify", 2, "Identify two possible opportunity costs of a Danish person using their leisure time to cycle. (Oct/Nov 2020, P22 style)", "Any two other uses of the time: studying, working, relaxing, spending time with family.", "[K|Time that could have been used to work and earn income.] [K|Time that could have been used to study (or relax).]"),
    Q(3, "State", 2, "State why sunshine has no opportunity cost. (Oct/Nov 2022, P22 style)", "Not scarce; no resources used.", "[K|Sunshine is a free good: it is not scarce] [K|and uses no scarce resources, so nothing is given up.]"),
    Q(4, "Explain", 4, "Explain opportunity cost and how it can influence a farmer's decision to grow apples. (May/June 2023, P22 style)", "Next best crop; compare incomes; choose.",
      "[K|Opportunity cost is the next best alternative given up.] [N|If the farmer grows apples on the land, the opportunity cost is the next best crop, such as barley.] [N|The farmer is more likely to grow apples if the expected income is greater than the income from the next best crop.]"),
    Q(5, "Explain", 4, "Explain the opportunity cost to India of exporting more textiles. (Feb/Mar 2023, P22 style)", "Resources used for textiles cannot be used elsewhere; the next best use.",
      "[K|India has scarce resources such as labour, land and capital.] [N|Using more of them to make textiles for export means they cannot be used for something else,] [N|such as producing other goods or food for the home market, which is the opportunity cost.]"),
)
tp = tips([
    ("Opportunity cost is only the next best alternative.", "Not everything given up."),
    ("Say what is given up.", "Name the actual alternative in the question."),
    ("Not just money.", "Time, wages, benefits and other projects count."),
    ("Free goods have none.", "Not scarce, no resources used."),
    ("Link to scarcity.", "Resources limited, so choice, so opportunity cost."),
], cmds("Define", "Identify", "Explain"))
body = page(CL("1.3.1 Opportunity cost"), "Opportunity Cost", "Defining opportunity cost and finding it in examples for consumers, workers, firms, governments and countries. Syllabus 1.3.1.",
    learn=learn, watch=watch(("From scarcity to opportunity cost", "stO"), ("Ranking the alternatives", "stR")), explore=explore,
    practise=practise(("Who faces it?", "cl1", "card"), ("Opportunity cost or not?", "cl2", "card"), ("Match the choice", "m1", "card"), ("Order the steps", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("University or a job", "A school leaver who goes to university gives up the wages they could have earned, as well as paying fees.", "A worker's opportunity cost."),
        rw("Government budgets", "Money spent on one public project cannot be spent on another, for example a new road or a hospital.", "Government opportunity cost."),
        rw("Fields for farming", "Land used for biofuel crops cannot be used for food, so some farmers weigh the price of each.", "A farmer's choice."),
        rw("Your time", "An hour spent on social media is an hour not spent on revision, work or sleep.", "Time as a scarce resource.")),
    exam=ex, tips=tp)
write("e31", body, js, "Opportunity Cost", "ig-opportunity-cost")

# =========================================================== 1.3.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Opportunity cost affects <b>every decision</b>. Each decision-maker compares the <b>benefit of a choice</b> with the <b>opportunity cost</b>. If the benefit is greater, they go ahead; if not, they choose something else. As opportunity costs change (prices, wages, incomes), decisions change too.</p></div>

  <h2>How it influences decisions</h2>
  <div class="tw"><table class="t">
    <tr><th>Decision-maker</th><th>Decision</th><th>How opportunity cost influences it</th></tr>
    <tr><td><b>Consumers</b></td><td>What to buy with limited income</td><td>Buying one good means giving up others, so consumers choose what gives the most satisfaction for the money; a price rise raises the opportunity cost of a good, so they may buy less of it</td></tr>
    <tr><td><b>Workers</b></td><td>Whether to work, train, work overtime or retire</td><td>Training or study costs lost wages; overtime costs leisure; workers compare the extra pay with what they give up. Higher wages raise the opportunity cost of leisure, so some choose to work more</td></tr>
    <tr><td><b>Producers (firms)</b></td><td>What to make, how much to invest, which methods</td><td>Funds used on new technology cannot be used for wages or advertising; firms switch to the most profitable use of resources</td></tr>
    <tr><td><b>Governments</b></td><td>How to spend limited tax revenue</td><td>Spending on healthcare means less on education, defence or transport; governments weigh the benefits to society of each</td></tr>
  </table></div>

  <h2>Changes in opportunity cost</h2>
  <ul>
    <li>If the price of a good <b>rises</b>, the opportunity cost of buying it rises, so quantity demanded tends to fall.</li>
    <li>If wages rise, the opportunity cost of leisure or study rises, so more people may work rather than study.</li>
    <li>If the price of one crop rises, the opportunity cost of growing a different one rises, so farmers switch.</li>
    <li>If a government needs to fund defence in an emergency, the opportunity cost is less spending on other services.</li>
  </ul>
  <p class="note">Good economic decisions weigh <b>benefits against opportunity cost</b>. Mistakes happen when decisions ignore what is given up.</p>
'''
js = HEAD + COMMON + '''
const CN = ["The price of a good rises", "Buying it means giving up more other goods", "The opportunity cost of the good rises", "Consumers buy less of it", "Quantity demanded falls"];
Lib.stepper($("#stC"), { w: 760, h: 380, label: "Consumer decisions", base: { n: 0 }, draw: mkChain(CN, "--accent"), steps: chainSteps(["The <b>price of a good rises</b>.", "Buying it means giving up <b>more other goods</b>.", "The <b>opportunity cost</b> of the good rises.", "Consumers <b>buy less</b> of it.", "<b>Quantity demanded falls</b>."]) });
const GV = ["The government has a limited tax budget", "It could spend on a hospital or on a new school", "Building the hospital means no school (opportunity cost)", "It compares the benefits of each to society", "It chooses the option with greater benefit"];
Lib.stepper($("#stG"), { w: 760, h: 380, label: "Government decisions", base: { n: 0 }, draw: mkChain(GV, "--good"), steps: chainSteps(["The government has a <b>limited budget</b>.", "It could spend on a <b>hospital</b> or on a <b>new school</b>.", "Building the hospital means <b>no school</b>: the opportunity cost.", "It <b>compares the benefits</b> of each to society.", "It chooses the option with the <b>greater benefit</b>."]) });
const FM = ["A firm has $1m to invest", "Options: new machines, advertising, or staff pay rises", "It compares expected extra profit of each", "It chooses the best; the next best is the opportunity cost", "If costs or benefits change, the decision may change"];
Lib.stepper($("#stF"), { w: 760, h: 380, label: "Firm decisions", base: { n: 0 }, draw: mkChain(FM, "--warn"), steps: chainSteps(["A firm has <b>$1m to invest</b>.", "Options: <b>new machines</b>, <b>advertising</b>, or <b>staff pay rises</b>.", "It compares the <b>expected extra profit</b> of each.", "It chooses the best; the <b>next best is the opportunity cost</b>.", "If costs or benefits change, the <b>decision may change</b>."]) });

/* Lab 1: work or study */
function labW() {
  if (!$("#wa") || !$("#wb")) return;
  const wage = +$("#wa").value, ben = +$("#wb").value, yrs = 3, cost = wage * yrs, gain = ben * 30 - cost, go = ben * 10 > wage * 1;
  $("#wa1").textContent = "$" + cost.toLocaleString(); $("#wa2").textContent = "$" + (ben * 30).toLocaleString(); $("#wa3").textContent = (gain >= 0 ? "+" : "−") + "$" + Math.abs(gain).toLocaleString();
  $("#wav").textContent = `Studying for 3 years gives up $${cost.toLocaleString()} of wages (the opportunity cost). If the degree raises pay by $${ben.toLocaleString()} a year for 30 years that is $${(ben * 30).toLocaleString()}. Net gain: ${gain >= 0 ? "+" : "−"}$${Math.abs(gain).toLocaleString()}. ${gain > 0 ? "Study looks worthwhile." : "The opportunity cost outweighs the benefit, so working may be better."} Higher wages raise the opportunity cost of study.`;
  const base = 280, k = 200 / Math.max(cost, ben * 30, 1); let o = SV.line(60, base, 700, base);
  [["Opportunity cost (wages lost)", cost, "--bad"], ["Benefit (extra pay later)", ben * 30, "--good"]].forEach(([n, v, c], i) => { const x = 140 + i * 280, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, "$" + v.toLocaleString(), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 20, n, "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  $("#labW").innerHTML = o;
}
Lib.slider($("#g1"), { id: "wa", label: "Yearly wage if you worked instead", min: 5000, max: 40000, step: 1000, value: 15000, fmt: (v) => "$" + v.toLocaleString(), onInput: labW });
Lib.slider($("#g2"), { id: "wb", label: "Extra yearly pay from the qualification", min: 1000, max: 20000, step: 1000, value: 6000, fmt: (v) => "$" + v.toLocaleString(), onInput: labW });
const DM = [
  { n: "Consumer", d: "Which goods to buy", e: "Gives up other goods; a higher price raises the opportunity cost." },
  { n: "Worker", d: "Work, study or leisure", e: "Study loses wages; overtime loses leisure; higher wages raise the cost of leisure." },
  { n: "Firm", d: "Invest or advertise", e: "Funds used on one project cannot be used on another." },
  { n: "Government", d: "Health, education, defence", e: "More on one means less on another." },
];
button_table("dmBtns", "dmOut", DM, 0, (p) => `<div class="tw"><table class="t"><tr><th>Decision</th><th>Influence of opportunity cost</th></tr><tr><td>${p.d}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>decision-maker</b> makes each decision?", buckets: [{ label: "Consumer" }, { label: "Worker" }, { label: "Firm" }, { label: "Government" }], items: [
  { text: "Whether to buy a phone or save", b: 0 }, { text: "Whether to buy a cheaper brand", b: 0 },
  { text: "Whether to take unpaid training", b: 1 }, { text: "Whether to work overtime", b: 1 },
  { text: "Whether to invest in a new machine", b: 2 }, { text: "Which product to make", b: 2 },
  { text: "How to divide the budget between health and education", b: 3 }, { text: "Whether to build a bridge or a school", b: 3 },
], done: "All face opportunity cost." });
Lib.classify($("#cl2"), { prompt: "Would a rise in the opportunity cost make each choice <b>more</b> or <b>less</b> likely?", buckets: [{ label: "More likely" }, { label: "Less likely" }], items: [
  { text: "Higher wages: choosing to work rather than study", b: 0 }, { text: "Higher price of wheat: a farmer switches to wheat", b: 0 },
  { text: "Higher wages: a student staying in education", b: 1 }, { text: "Higher price of a good: consumers buying it", b: 1 },
  { text: "A pay cut: working extra hours", b: 1 }, { text: "Higher wages: choosing leisure over work", b: 1 },
], done: "A higher opportunity cost makes the choice less attractive." });
Lib.match($("#m1"), { prompt: "Match the decision to the opportunity cost involved.", pairs: [
  ["A worker takes unpaid training", "Wages lost"],
  ["A firm buys new technology", "Advertising or wage rises given up"],
  ["A government spends on healthcare", "Education or defence given up"],
  ["A consumer buys a holiday", "Other goods given up"],
  ["A farmer grows apples", "The next best crop"],
  ["A student studies", "Leisure or work time"],
], done: "Link each decision to what is given up." });
Lib.order($("#o1"), { prompt: "Put the steps in order: <b>how a government uses opportunity cost</b>.", items: [
  "The government has a limited budget",
  "It lists projects it could fund",
  "It compares the benefits of each to society",
  "It chooses the project with the most benefit",
  "The other projects are the opportunity cost",
], done: "Weighing benefits against opportunity cost." });
''' + calc_js([
    ("A student could earn $18,000 a year or study for 4 years. What wages are given up ($)?", 72000, "4 × 18,000 = <b>$72,000</b>.", None, None),
    ("A degree raises pay by $8,000 a year for 25 years. What is the total extra pay ($)?", 200000, "8,000 × 25 = <b>$200,000</b>.", None, None),
    ("A government has $10bn. It spends $6bn on healthcare. How much is left for other uses ($bn)?", 4, "10 − 6 = <b>$4bn</b>.", None, None),
]) + mcq_js("qz1", [
    ("A rise in wages raises the opportunity cost of:", ["Work", "Leisure", "Training being free", "Machines"], 1, "More pay given up for each hour of leisure."),
    ("A government that spends on defence has an opportunity cost of:", ["Nothing", "Other public services", "Free goods", "Taxes"], 1, "Less for health, education, etc."),
    ("A firm's opportunity cost of investing in new technology is:", ["The technology itself", "The next best use of the funds", "Nothing", "Profit"], 1, "What the money could have done."),
    ("When the price of a good rises, consumers may:", ["Buy more", "Buy less as the opportunity cost rises", "Ignore it", "Buy free goods"], 1, "Higher opportunity cost."),
    ("Good decisions compare:", ["Costs only", "Benefits with opportunity cost", "Only price", "Only time"], 1, "Weigh both."),
]) + "\n" + cards_js([("Opportunity cost", "The next best alternative given up."), ("Benefit", "The gain from a decision."), ("Trade-off", "Giving up one thing for another."), ("Decision-maker", "A consumer, worker, producer or government making a choice."), ("Cost-benefit", "Comparing the benefits of a decision with its costs."), ("Leisure", "Time not spent working."), ("Investment", "Spending on capital goods."), ("Budget", "A plan of income and spending."), ("Satisfaction", "The benefit a consumer gets from a good.")]) + "labW(); \n"
explore = '''
  <h2>Lab 1 · Work or study?</h2>
  <p>A student can work for 3 years or study for 3 years. Compare the wages given up with the extra pay a qualification brings over 30 years.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Opportunity cost</small><strong id="wa1"></strong></div><div><small>Benefit</small><strong id="wa2"></strong></div><div><small>Net gain</small><strong id="wa3"></strong></div></div><div class="verdict" id="wav"></div></div></div>
    <svg id="labW" viewBox="0 0 760 320" role="img" aria-label="Opportunity cost and benefit of study"></svg>
  </div>

  <h2>Lab 2 · Decision-makers</h2>
  <p>Pick a decision-maker to see how opportunity cost affects them.</p>
  <div class="card"><div class="row" id="dmBtns"></div><div id="dmOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain the influence of opportunity cost on consumers' decisions. (Feb/Mar 2021, P12 style)", "Limited income; giving up other goods; compare satisfaction; price changes.",
      "[K|Consumers have limited incomes, so buying one good means giving up others.] [N|They compare the satisfaction from each and choose the option that gives the most.] [N|If the price of a good rises, the opportunity cost of buying it rises, so they may buy less of it.]"),
    Q(2, "Explain", 4, "Explain, using an example, the influence of opportunity cost on government decision-making. (Oct/Nov 2021, P12 style)", "Limited revenue; spending on one project means not on another; example: hospital vs school.",
      "[K|A government has a limited tax revenue, so spending on one project means less is available for others.] [N|For example, building a new hospital may mean a new school cannot be built.] [N|The government compares the benefits to society of each and chooses the one with the greater benefit.]"),
    Q(3, "Explain", 4, "Explain two possible opportunity costs for firms if they invest in the latest technology. (May/June 2024, P22 style)", "Advertising, higher wages, dividends, other projects.",
      "[K|One opportunity cost is spending on advertising.] [N|The money used for technology cannot be used to promote the firm's products.] [K|Another is higher wages for staff.] [N|The funds cannot be used to raise pay or recruit more workers.]"),
    Q(4, "Explain", 4, "Explain how opportunity cost will influence a government's decision on whether to spend tax revenue on a new road. (Oct/Nov 2023, P12 style)", "Other uses of the revenue; compare benefits; choose.",
      "[K|Spending the revenue on a road means it cannot be used for something else, such as healthcare or education.] [N|The government has to compare the benefits of the road with the benefits of the alternatives.] [N|If the benefits of the road are greater than the benefits of the next best use, it is more likely to go ahead.]"),
    Q(5, "Analyse", 6, "Analyse, using a production possibility curve, the opportunity cost to an economy of producing more consumer goods. (May/June 2022, P22 style)", "More consumer goods means fewer capital goods; movement along PPC.",
      "[K|A PPC shows the maximum combinations of two types of goods an economy can produce with its resources.] [N|Moving along the PPC to produce more consumer goods means resources are shifted from capital goods production.] [N|The opportunity cost is the capital goods given up, which could reduce future growth.] [E|If the PPC is curved, the opportunity cost rises as more consumer goods are produced.]", key=True),
)
tp = tips([
    ("Always name the alternative given up.", "Be specific to the context."),
    ("Compare benefits with opportunity cost.", "That is how decisions are made."),
    ("Use an example.", "Hospital vs school; study vs wages; machines vs advertising."),
    ("Say how a change alters the decision.", "A price rise raises the opportunity cost."),
    ("Limited resources first.", "Then choice, then opportunity cost."),
], cmds("Explain", "Analyse"))
body = page(CL("1.3.2 The influence of opportunity cost on decision-making"), "Opportunity Cost and Decision-Making", "How consumers, workers, firms and governments weigh benefits against opportunity cost. Syllabus 1.3.2.",
    learn=learn, watch=watch(("Consumer decisions", "stC"), ("Government decisions", "stG"), ("Firm decisions", "stF")), explore=explore,
    practise=practise(("Who decides?", "cl1", "card"), ("More or less likely?", "cl2", "card"), ("Match the decision", "m1", "card"), ("Order the steps", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Healthcare vs education budgets", "Governments with limited revenue must weigh each extra dollar on health against the same dollar on education.", "Government decisions."),
        rw("Gap years", "A student who takes a gap year gives up a year of earnings after graduating but may gain experience.", "Workers' decisions."),
        rw("Firms and automation", "A firm that spends on robots has less to spend on staff pay or advertising.", "Firms' decisions."),
        rw("Streaming vs cinema", "A consumer who pays for a streaming subscription has less to spend on other entertainment.", "Consumer decisions.")),
    exam=ex, tips=tp)
write("e32", body, js, "Opportunity Cost and Decision-Making", "ig-opportunity-cost-decisions")
