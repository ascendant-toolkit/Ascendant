"""Builds the three IGCSE Economics 1.1 The nature of the basic economic problem reviews (1.1.1 to 1.1.3).
Run: python3 tools/artifact-kit/mk_ig11.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

# =========================================================== 1.1.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The <span class="kw">basic economic problem</span> is that people have <b>infinite (unlimited) wants</b> but the resources available to satisfy them are <b>finite (limited)</b>. This gap is called <span class="kw">scarcity</span>. Because of scarcity, everyone has to make <b>choices</b>, and every choice has an <b>opportunity cost</b>. Every consumer, worker, firm and government faces the problem; no country is free of it, however rich.</p></div>

  <h2>Key definitions</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th></tr>
    <tr><td><b>Needs</b></td><td>Goods and services essential for survival, such as food, water, shelter</td></tr>
    <tr><td><b>Wants</b></td><td>Goods and services people would like to have; they are unlimited</td></tr>
    <tr><td><b>Finite resources</b></td><td>Land, labour, capital and enterprise are limited in supply</td></tr>
    <tr><td><b>Scarcity</b></td><td>Limited resources compared with unlimited wants</td></tr>
    <tr><td><b>Choice</b></td><td>Having to select some things and give up others</td></tr>
  </table></div>

  <h2>Examples of the problem for each decision-maker</h2>
  <div class="tw"><table class="t">
    <tr><th>Decision-maker</th><th>Unlimited wants</th><th>Limited resources</th><th>Choice</th></tr>
    <tr><td><b>Consumers</b></td><td>Many goods and services</td><td>Limited income and time</td><td>Spend on a phone or on holidays</td></tr>
    <tr><td><b>Workers</b></td><td>Higher pay, leisure, job satisfaction</td><td>Limited time (24 hours a day), skills, energy</td><td>Work overtime or have more leisure</td></tr>
    <tr><td><b>Producers (firms)</b></td><td>More output and profit</td><td>Limited finance, workers, raw materials, machinery</td><td>Which product to make; whether to invest in new machinery or marketing</td></tr>
    <tr><td><b>Governments</b></td><td>Better healthcare, schools, defence, roads</td><td>Limited tax revenue and ability to borrow</td><td>Spend on hospitals or on schools</td></tr>
  </table></div>
  <p class="note">Wealthy countries still face scarcity: wants always grow with income. Saying a country is rich does not remove the problem. Answering an exam question, link the example to <b>limited resources</b> and a <b>choice</b>.</p>
'''
js = HEAD + COMMON + '''
const SC = ["People have unlimited wants", "But resources (land, labour, capital, enterprise) are finite", "Not everything can be produced or bought: scarcity", "People, firms and governments must make choices", "Every choice gives up the next best alternative: opportunity cost"];
Lib.stepper($("#stS"), { w: 760, h: 380, label: "From wants to scarcity", base: { n: 0 }, draw: mkChain(SC, "--accent"), steps: chainSteps(["People have <b>unlimited wants</b>.", "But <b>resources are finite</b>: land, labour, capital and enterprise.", "Not everything can be produced or bought: <b>scarcity</b>.", "People, firms and governments must <b>make choices</b>.", "Every choice gives up the next best alternative: <b>opportunity cost</b>."]) });
function gapChart(s) {
  let o = SV.line(60, 300, 700, 300) + SV.text(60, 26, "Wants and resources over time", "sm");
  const lab = ["Today", "Next year", "In 5 years"], res = [100, 108, 140], wants = [160, 190, 300];
  lab.forEach((l, i) => { const x = 110 + i * 200, op = clamp(s.n - i, 0, 1); if (op <= 0) return; o += `<g opacity="${op}">` + SV.rect(x, 300 - res[i], 70, res[i], "", { style: "fill:var(--good)", opacity: 0.85 }) + SV.text(x + 35, 300 - res[i] - 6, "Resources", "sm bd", { "text-anchor": "middle", style: "font-size:11px" }) + SV.rect(x + 80, 300 - wants[i] * 0.9, 70, wants[i] * 0.9, "", { style: "fill:var(--bad)", opacity: 0.85 }) + SV.text(x + 115, 300 - wants[i] * 0.9 - 6, "Wants", "sm bd", { "text-anchor": "middle", style: "font-size:11px" }) + SV.text(x + 75, 322, l, "sm", { "text-anchor": "middle" }) + "</g>"; });
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 340, label: "The gap never closes", base: { n: 0 }, draw: gapChart, steps: [
  { cap: "Today wants exceed resources: a <b>gap</b> (illustrative figures).", s: { n: 1 } },
  { cap: "Resources grow with better technology and investment, but wants grow faster.", s: { n: 2 } },
  { cap: "Even with more resources, the gap remains: <b>scarcity never disappears</b>.", s: { n: 3 } },
] });

/* Lab 1: budget choice */
function labB() {
  if (!$("#ba") || !$("#bb")) return;
  const inc = +$("#ba").value, food = +$("#bb").value, wantsList = [["Phone", 600], ["Holiday", 800], ["Games console", 400], ["New clothes", 300], ["Concert tickets", 200]];
  let left = inc - food, got = [], skipped = []; wantsList.forEach(([n, c]) => { if (c <= left) { left -= c; got.push(n); } else skipped.push(n); });
  $("#ba1").textContent = "$" + left; $("#ba2").textContent = got.length; $("#ba3").textContent = skipped.length;
  $("#bav").textContent = `With income $${inc} and $${food} needed for essentials, you can afford: ${got.join(", ") || "none"}. Unaffordable wants: ${skipped.join(", ") || "none"}. Higher income lets you buy more, but the list of wants is never finished. That is scarcity.`;
  const base = 280; let o = SV.line(60, base, 700, base);
  wantsList.forEach(([n, c], i) => { const x = 90 + i * 120, ok = got.includes(n), h = c * 0.24; o += SV.rect(x, base - h, 90, h, "", { style: `fill:var(${ok ? "--good" : "--bad"})`, opacity: ok ? 0.85 : 0.35 }) + SV.text(x + 45, base - h - 6, "$" + c, "sm bd", { "text-anchor": "middle" }) + SV.text(x + 45, base + 18, n, "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  $("#labB").innerHTML = o + SV.text(60, 24, "Green: bought. Faded red: given up.", "sm");
}
Lib.slider($("#g1"), { id: "ba", label: "Monthly income", min: 500, max: 3000, step: 100, value: 1200, fmt: (v) => "$" + v, onInput: labB });
Lib.slider($("#g2"), { id: "bb", label: "Spending on needs (food, rent)", min: 200, max: 1500, step: 50, value: 700, fmt: (v) => "$" + v, onInput: labB });
const EX = [
  { n: "Consumer", w: "Wants a phone, holiday and car", r: "Limited income", c: "Choose which to buy first" },
  { n: "Worker", w: "Wants more pay and more leisure", r: "Only 24 hours a day", c: "Overtime or free time" },
  { n: "Firm", w: "Wants more machines and staff", r: "Limited finance", c: "Invest in machinery or marketing" },
  { n: "Government", w: "Wants better hospitals, schools, roads", r: "Limited tax revenue", c: "Spend on health or education" },
];
button_table("exBtns", "exOut", EX, 0, (p) => `<div class="tw"><table class="t"><tr><th>Wants</th><th>Limited resource</th><th>Choice</th></tr><tr><td>${p.w}</td><td>${p.r}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>decision-maker</b> faces each problem?", buckets: [{ label: "Consumer" }, { label: "Worker" }, { label: "Firm" }, { label: "Government" }], items: [
  { text: "Limited income to spend on many goods", b: 0 }, { text: "Choosing between a phone and a holiday", b: 0 },
  { text: "Choosing between overtime and leisure time", b: 1 }, { text: "Only 24 hours in a day", b: 1 },
  { text: "Limited finance to buy machinery and hire staff", b: 2 }, { text: "Deciding which product to make", b: 2 },
  { text: "Limited tax revenue for hospitals and schools", b: 3 }, { text: "Choosing between defence and healthcare", b: 3 },
], done: "Everyone faces scarcity and must choose." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>want</b> or a <b>need</b> (a want is not essential for survival)?", buckets: [{ label: "Need" }, { label: "Want" }], items: [
  { text: "Clean drinking water", b: 0 }, { text: "Basic food", b: 0 }, { text: "Shelter", b: 0 },
  { text: "A designer handbag", b: 1 }, { text: "A holiday abroad", b: 1 }, { text: "The latest games console", b: 1 },
], done: "Wants are unlimited; needs are essential." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Scarcity", "Limited resources compared with unlimited wants"],
  ["Basic economic problem", "Infinite wants but finite resources"],
  ["Finite resources", "Resources limited in supply"],
  ["Wants", "Goods and services people would like to have"],
  ["Needs", "Goods and services essential for survival"],
  ["Choice", "Selecting some alternatives and giving up others"],
], done: "Good definitions score marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>from wants to opportunity cost</b>.", items: [
  "People have unlimited wants",
  "Resources are finite",
  "Scarcity exists",
  "Choices must be made",
  "Each choice has an opportunity cost",
], done: "The logic of the basic economic problem." });
''' + calc_js([
    ("A consumer earns $900 a month and spends $600 on needs. How much is left for wants ($)?", 300, "900 − 600 = <b>$300</b>.", None, None),
    ("A government has $50bn of tax revenue. It spends 30% on healthcare. How much is spent on healthcare ($bn)?", 15, "30% × 50 = <b>$15bn</b>.", None, None),
    ("A worker has 24 hours a day, sleeps 8 and works 8. How many hours are left for leisure?", 8, "24 − 8 − 8 = <b>8 hours</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is the basic economic problem?", ["Unemployment", "Infinite wants but finite resources", "Inflation", "Too many goods"], 1, "Scarcity of resources."),
    ("Scarcity exists because:", ["Wants are limited", "Resources are limited compared with wants", "Money is scarce only", "Governments exist"], 1, "Finite resources, infinite wants."),
    ("Which country faces the basic economic problem?", ["Only poor countries", "Only rich countries", "All countries", "No country"], 2, "Every country has finite resources."),
    ("For a worker, a scarce resource is:", ["Time", "Free air", "Sunlight", "Space in the ocean"], 0, "24 hours a day."),
    ("Which is an example of a government facing scarcity?", ["Choosing between schools and hospitals", "Printing money freely", "Having a surplus", "No decisions"], 0, "Limited revenue."),
]) + "\n" + cards_js([("Basic economic problem", "Infinite wants but finite resources."), ("Scarcity", "Limited resources compared with unlimited wants."), ("Finite resources", "Resources limited in supply."), ("Wants", "Goods and services people would like to have; unlimited."), ("Needs", "Goods and services essential for survival."), ("Choice", "Selecting between alternatives."), ("Opportunity cost", "The next best alternative given up."), ("Consumer", "A person who buys goods and services."), ("Producer", "A firm that makes goods and services.")]) + "labB(); \n"
explore = '''
  <h2>Lab 1 · Your monthly budget</h2>
  <p>Change income and the spending on needs, then see which wants you can afford. Whatever you do, something is left out.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Money left</small><strong id="ba1"></strong></div><div><small>Wants bought</small><strong id="ba2"></strong></div><div><small>Wants given up</small><strong id="ba3"></strong></div></div><div class="verdict" id="bav"></div></div></div>
    <svg id="labB" viewBox="0 0 760 320" role="img" aria-label="Wants bought and given up"></svg>
  </div>

  <h2>Lab 2 · Scarcity for each decision-maker</h2>
  <p>Pick a decision-maker to see their wants, limited resource and choice.</p>
  <div class="card"><div class="row" id="exBtns"></div><div id="exOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "What is the basic economic problem? (Oct/Nov 2020, P11 style)", "Infinite wants but finite resources.", "[K|The basic economic problem is that people have infinite (unlimited) wants] [K|but resources are finite (limited), so choices have to be made.]"),
    Q(2, "Define", 2, "Define scarcity.", "Limited resources compared with unlimited wants.", "[K|Scarcity is the shortage of resources] [K|in relation to unlimited wants.]"),
    Q(3, "Explain", 4, "Explain how scarcity affects consumers.", "Limited income, unlimited wants, choose, opportunity cost.",
      "[K|Consumers have limited income but unlimited wants.] [N|They cannot afford everything, so they have to choose which goods and services to buy.] [N|Buying one thing means giving up another, so every choice has an opportunity cost.]"),
    Q(4, "Explain", 4, "Explain why a government faces the basic economic problem.", "Limited revenue; wants for health, education, defence; choice.",
      "[K|A government has limited tax revenue and borrowing, but there are unlimited demands for spending on health, education, defence and roads.] [N|It has to choose between them,] [N|so spending more on one means less on another: an opportunity cost.]"),
    Q(5, "Explain", 4, "Explain why even a wealthy country such as Switzerland still faces the basic economic problem. (Oct/Nov 2022, P11 style)", "Finite resources, wants rise with income.",
      "[K|Even a wealthy country has finite resources such as land, labour and capital.] [N|People's wants are unlimited and tend to increase as incomes rise,] [N|so there are still not enough resources to produce everything, and choices must be made.]"),
)
tp = tips([
    ("Always say 'infinite wants' and 'finite resources'.", "Both halves score the mark."),
    ("Scarcity is the cause; choice is the result.", "Opportunity cost follows."),
    ("Name the decision-maker's limited resource.", "Consumers: income. Workers: time. Firms: finance. Governments: revenue."),
    ("Rich countries face scarcity too.", "Wants grow with income."),
    ("Use a specific example.", "'Spend on hospitals or schools.'"),
], cmds("Define", "Explain"))
body = page(CL("1.1.1 Finite resources and infinite wants"), "Finite Resources and Infinite Wants", "The basic economic problem, scarcity, and how it affects consumers, workers, firms and governments. Syllabus 1.1.1.",
    learn=learn, watch=watch(("From wants to scarcity", "stS"), ("The gap never closes", "stG")), explore=explore,
    practise=practise(("Who faces the problem?", "cl1", "card"), ("Want or need?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("A household budget", "A family must decide between paying for a larger home, a car, holidays and savings with a limited income each month.", "Consumers face scarcity."),
        rw("Government budgets", "Every year governments choose how to divide limited tax revenue between health, education, defence and transport.", "Government choices."),
        rw("A firm's investment choice", "A small business with a limited loan must choose between new equipment and advertising.", "Producers face scarcity."),
        rw("A student's time", "A student has a limited number of hours a day to divide between study, work, friends and sleep.", "Workers and time.")),
    exam=ex, tips=tp)
write("e11", body, js, "Finite Resources and Infinite Wants", "ig-basic-problem")

# =========================================================== 1.1.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Because of scarcity, every society must answer <b>three basic economic questions</b>: <b>what to produce</b>, <b>how to produce</b> and <b>who to produce for</b>. These decisions allocate scarce resources between competing uses. Different economic systems answer them in different ways, with the market, the government, or a mixture deciding.</p></div>

  <h2>The three basic questions</h2>
  <div class="tw"><table class="t">
    <tr><th>Question</th><th>What it means</th><th>Examples of decisions</th></tr>
    <tr><td><b>What to produce?</b></td><td>Which goods and services, and in what quantities, to make with limited resources</td><td>More healthcare or more military equipment; food or cars; wheat or cocoa</td></tr>
    <tr><td><b>How to produce?</b></td><td>Which methods and resource mix: labour-intensive or capital-intensive, which technology, which location</td><td>Hand-picked or machine-harvested crops; factory with robots or many workers; renewable or fossil energy</td></tr>
    <tr><td><b>Who to produce for?</b></td><td>Who receives the output: how income and goods are distributed</td><td>Luxury goods for the rich or basics for the poor; goods to export or for the home market</td></tr>
  </table></div>

  <h2>Who decides?</h2>
  <ul>
    <li>In a <b>market economy</b>, consumers' spending and firms' search for profit answer the questions through prices.</li>
    <li>In a <b>planned (command) economy</b>, the government decides.</li>
    <li>In a <b>mixed economy</b>, both markets and the government take part.</li>
  </ul>
  <p class="note">The questions are decisions about resource allocation: they exist <b>because of scarcity</b>. Each answer has an opportunity cost.</p>
'''
js = HEAD + COMMON + '''
const QS = ["Scarce resources must be allocated", "WHAT to produce: which goods and services, and how many", "HOW to produce: which methods, technology and resource mix", "WHO to produce for: who gets the output", "Each answer has an opportunity cost"];
Lib.stepper($("#stQ"), { w: 760, h: 380, label: "The three questions", base: { n: 0 }, draw: mkChain(QS, "--accent"), steps: chainSteps(["Because of scarcity, resources must be <b>allocated</b>.", "<b>What</b> to produce: which goods and services, and how many.", "<b>How</b> to produce: which methods, technology and resource mix.", "<b>Who</b> to produce for: who gets the output.", "Each answer has an <b>opportunity cost</b>."]) });
const MK = ["Consumers spend more on a product", "Its price and profit rise", "Firms switch resources into making it", "Resources move out of less profitable goods", "The market has answered WHAT to produce"];
Lib.stepper($("#stM"), { w: 760, h: 380, label: "How the market answers what to produce", base: { n: 0 }, draw: mkChain(MK, "--good"), steps: chainSteps(["<b>Consumers spend more</b> on a product.", "Its <b>price and profit rise</b>.", "Firms <b>switch resources</b> into making it.", "Resources <b>move out</b> of less profitable goods.", "The market has answered <b>what to produce</b>."]) });

/* Lab 1: sort decisions */
const DQ = [
  { n: "A farmer chooses wheat rather than rice", q: "What to produce", e: "A choice of output." },
  { n: "A factory installs robots instead of hiring workers", q: "How to produce", e: "A choice of production method." },
  { n: "A government gives free school meals to poor children", q: "Who to produce for", e: "A decision on who receives output." },
  { n: "A car firm makes electric rather than petrol cars", q: "What to produce", e: "A choice of output." },
  { n: "A firm uses solar rather than coal power", q: "How to produce", e: "A choice of method and resources." },
  { n: "A shop stocks luxury goods for high-income customers", q: "Who to produce for", e: "A decision on the target market." },
];
button_table("dqBtns", "dqOut", DQ, 0, (p) => `<div class="tw"><table class="t"><tr><th>Basic question</th><th>Why</th></tr><tr><td><b>${p.q}</b></td><td>${p.e}</td></tr></table></div>`);
function labW() {
  if (!$("#wa")) return;
  const l = +$("#wa").value, k = 100 - l, cost = l * 8 + k * 14, out = l * 6 + k * 12;
  $("#wa1").textContent = "$" + cost; $("#wa2").textContent = out; $("#wa3").textContent = "$" + money(cost / out, 2);
  $("#wav").textContent = `${l}% labour and ${k}% capital: cost $${cost}, output ${out}, cost per unit $${money(cost / out, 2)}. Choosing HOW to produce is a trade-off between labour-intensive and capital-intensive methods (illustrative figures).`;
  const base = 280; let o = SV.line(60, base, 700, base);
  [["Labour share", l, "--warn"], ["Capital share", k, "--accent"]].forEach(([n, v, cl], i) => { const x = 160 + i * 250, h = v * 2.2; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${cl})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, v + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labW").innerHTML = o;
}
Lib.slider($("#g1"), { id: "wa", label: "Share of production using labour", min: 0, max: 100, step: 10, value: 50, fmt: (v) => v + "%", onInput: labW });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>basic economic question</b> is each decision?", buckets: [{ label: "What to produce" }, { label: "How to produce" }, { label: "Who to produce for" }], items: [
  { text: "Wheat or rice?", b: 0 }, { text: "More hospitals or more roads?", b: 0 },
  { text: "Robots or workers?", b: 1 }, { text: "Which technology and location to use", b: 1 },
  { text: "Goods for the rich or for the poor?", b: 2 }, { text: "Export or home market?", b: 2 },
], done: "What, how, who." });
Lib.classify($("#cl2"), { prompt: "Who answers the questions in each system?", buckets: [{ label: "The market" }, { label: "The government" }, { label: "Both" }], items: [
  { text: "Consumers' spending and firms' profit", b: 0 }, { text: "Prices act as signals", b: 0 },
  { text: "Planners set output targets", b: 1 }, { text: "State-owned firms follow instructions", b: 1 },
  { text: "Private firms and public services together", b: 2 }, { text: "A mixed economy", b: 2 },
], done: "Market, planned or mixed." });
Lib.match($("#m1"), { prompt: "Match the question to the example.", pairs: [
  ["What to produce", "Solar panels or coal"],
  ["How to produce", "Machines or hand tools"],
  ["Who to produce for", "Luxury goods or basic goods"],
  ["Resource allocation", "Dividing scarce resources between uses"],
  ["Market economy", "Prices and profits decide"],
  ["Planned economy", "The government decides"],
], done: "Link each question to an example." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how the market decides what to produce</b>.", items: [
  "Consumers demand more of a good",
  "Its price and profit rise",
  "Firms move resources into producing it",
  "Output of the good rises",
  "Resources move away from goods in less demand",
], done: "A market chain." });
''' + calc_js([
    ("A firm can use 60 workers at $100 each a day, or 10 machines at $500 each a day. How much cheaper per day is the machine method ($)?", 1000, "Workers: 60 × 100 = $6,000. Machines: 10 × 500 = $5,000. Difference <b>$1,000</b>.", None, None),
    ("A country has 50% of its resources in farming and 30% in manufacturing. What percentage is left for services?", 20, "100 − 50 − 30 = <b>20%</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which is a 'how to produce' decision?", ["Making cars or bikes", "Using robots or workers", "Selling to rich or poor", "Wheat or rice"], 1, "Choice of method."),
    ("Deciding to make more healthcare and less military equipment answers:", ["How to produce", "What to produce", "Who to produce for", "None"], 1, "A choice of output."),
    ("Who to produce for is about:", ["Methods", "How output is distributed", "Quantity of output", "Prices only"], 1, "Distribution."),
    ("The three questions arise because of:", ["Inflation", "Scarcity", "Unemployment", "Trade"], 1, "Limited resources."),
    ("In a market economy the questions are answered mainly by:", ["Planners", "Consumers and firms through prices", "Courts", "Banks only"], 1, "The price mechanism."),
]) + "\n" + cards_js([("What to produce", "The decision on which goods and services to make and how many."), ("How to produce", "The decision on the methods and resources used."), ("Who to produce for", "The decision on who receives the output."), ("Resource allocation", "Dividing scarce resources between competing uses."), ("Market economy", "An economy where prices and profits decide."), ("Planned economy", "An economy where the government decides."), ("Mixed economy", "An economy with both private and public decision-making."), ("Labour-intensive", "Production that uses relatively more labour than capital."), ("Capital-intensive", "Production that uses relatively more capital than labour.")]) + "labW(); \n"
explore = '''
  <h2>Lab 1 · How to produce</h2>
  <p>Choose the share of production using labour or capital. The cost and output change.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Total cost</small><strong id="wa1"></strong></div><div><small>Output</small><strong id="wa2"></strong></div><div><small>Cost per unit</small><strong id="wa3"></strong></div></div><div class="verdict" id="wav"></div></div></div>
    <svg id="labW" viewBox="0 0 760 320" role="img" aria-label="Labour and capital shares"></svg>
  </div>

  <h2>Lab 2 · Which question?</h2>
  <p>Pick a decision to see which of the three basic questions it answers.</p>
  <div class="card"><div class="row" id="dqBtns"></div><div id="dqOut"></div></div>
'''
ex = exam(
    Q(1, "Identify", 3, "State the three basic economic questions.", "What, how, who.", "[K|What to produce.] [K|How to produce.] [K|Who to produce for.]"),
    Q(2, "Explain", 4, "Explain what is meant by the question 'what to produce'.", "Choice of goods and services and quantities; scarce resources; opportunity cost.",
      "[K|'What to produce' is the decision about which goods and services, and how many of each, are made.] [N|Resources are scarce, so producing more of one good means fewer resources for another.] [N|For example, a government may have to choose between more healthcare and more military equipment.]"),
    Q(3, "Explain", 4, "Explain what is meant by the question 'how to produce'.", "Method, labour vs capital, technology.",
      "[K|'How to produce' is the decision about the methods and mix of resources used.] [N|For example, firms can use labour-intensive methods with many workers or capital-intensive methods with machines.] [N|The choice depends on costs, technology and the resources available.]"),
    Q(4, "Explain", 4, "Explain how the market decides what to produce.", "Consumer demand, price, profit, resources move.",
      "[K|In a market economy consumers' spending shows what they want.] [N|When demand for a good rises, its price and profit rise,] [N|so firms switch resources into making it and away from less profitable goods.]"),
)
tp = tips([
    ("Three questions:", "what, how, who."),
    ("Give an example with each.", "Wheat or rice; robots or workers; rich or poor."),
    ("Link to scarcity.", "The questions exist because resources are limited."),
    ("Who decides?", "Market, government or both."),
], cmds("Identify", "Explain"))
body = page(CL("1.1.2 Resource allocation decisions"), "Resource Allocation Decisions", "What, how and who: the three basic economic questions every society must answer. Syllabus 1.1.2.",
    learn=learn, watch=watch(("The three questions", "stQ"), ("How the market answers what to produce", "stM")), explore=explore,
    practise=practise(("Which question?", "cl1", "card"), ("Who decides?", "cl2", "card"), ("Match the question", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("What to produce: Ghana's cocoa", "Ghana uses a large share of its farmland for cocoa instead of other crops, a choice about what to produce.", "What to produce."),
        rw("How to produce: farming", "Some farms harvest by hand and others use large machines, a choice about how to produce.", "How to produce."),
        rw("Who to produce for: free school meals", "Some governments provide free meals to children from low-income families, a decision about who receives output.", "Who to produce for."),
        rw("Electric vehicles", "Car makers have moved resources from petrol to electric vehicles as demand has changed.", "The market answering what to produce.")),
    exam=ex, tips=tp)
write("e12", body, js, "Resource Allocation Decisions", "ig-allocation-questions")

# =========================================================== 1.1.3
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Economic goods</span> are goods and services that are <b>scarce</b>: they take resources to produce, so they have a <b>price</b> and an <b>opportunity cost</b>. <span class="kw">Free goods</span> are goods that are <b>not scarce</b>: there is enough for everyone without using up resources, so they have <b>no price</b> and <b>no opportunity cost</b>. Most goods are economic goods, and that is why economics exists.</p></div>

  <h2>Economic goods and free goods</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Economic goods</th><th>Free goods</th></tr>
    <tr><td><b>Scarcity</b></td><td>Scarce: limited supply</td><td>Not scarce: unlimited supply</td></tr>
    <tr><td><b>Resources needed</b></td><td>Use scarce resources to produce</td><td>No scarce resources used</td></tr>
    <tr><td><b>Price</b></td><td>Have a price</td><td>No price</td></tr>
    <tr><td><b>Opportunity cost</b></td><td>Yes: resources could make something else</td><td>No opportunity cost</td></tr>
    <tr><td><b>Examples</b></td><td>Cars, food, healthcare, bottled water, clothes</td><td>Sunlight, air in the open, rain, sea water at the beach</td></tr>
  </table></div>
  <div class="card"><h3>Careful</h3>
    <ul><li>Free goods do not mean 'free of charge' goods. A school meal funded by taxes is free to the pupil but costs resources, so it is an <b>economic good</b>.</li>
    <li>A good can change category: clean air in a polluted city, or water in a drought, can become scarce and gain a price.</li>
    <li>Free goods exist, but they cannot solve the basic economic problem because they are only a small part of what people want.</li></ul></div>
'''
js = HEAD + COMMON + '''
function ecoChart(s) {
  let o = SV.line(60, 280, 700, 280) + SV.text(60, 26, "Supply and price of a good", "sm");
  [["Sunlight", "Free good", "$0", 210, "--good"], ["Tap water in a drought", "Becomes scarce", "price rises", 130, "--warn"], ["Bottled water", "Economic good", "has a price", 90, "--accent"]].forEach(([n, t, p, h, c], i) => {
    const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 110 + i * 200; o += `<g opacity="${op}">` + SV.rect(x, 280 - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 60, 280 - h - 8, t, "sm bd", { "text-anchor": "middle" }) + SV.text(x + 60, 300, n, "sm", { "text-anchor": "middle", style: "font-size:11px" }) + SV.text(x + 60, 320, p, "sm", { "text-anchor": "middle", style: "font-size:11px" }) + "</g>"; });
  return o;
}
Lib.stepper($("#stE"), { w: 760, h: 340, label: "From free to economic goods", base: { n: 0 }, draw: ecoChart, steps: [
  { cap: "Sunlight is <b>not scarce</b> and uses no resources: a <b>free good</b> with no price.", s: { n: 1 } },
  { cap: "In a drought, tap water becomes <b>scarce</b>: it takes resources to supply, so it gets a price.", s: { n: 2 } },
  { cap: "Bottled water uses resources (bottles, transport, labour): an <b>economic good</b> with a price and an opportunity cost.", s: { n: 3 } },
] });
const OC = ["Resources are scarce", "Using them to make an economic good means they cannot be used for something else", "So making the good has an opportunity cost", "A free good uses no scarce resources", "So a free good has no opportunity cost"];
Lib.stepper($("#stO"), { w: 760, h: 380, label: "Opportunity cost and the two kinds of goods", base: { n: 0 }, draw: mkChain(OC, "--accent"), steps: chainSteps(["Resources are <b>scarce</b>.", "Using them to make an <b>economic good</b> means they cannot be used for something else.", "So making the good has an <b>opportunity cost</b>.", "A <b>free good</b> uses no scarce resources.", "So a free good has <b>no opportunity cost</b>."]) });

const GG = [
  { n: "Sunlight", t: "Free good", e: "Unlimited supply; no resources used." },
  { n: "Air in an open field", t: "Free good", e: "Unlimited supply; no price." },
  { n: "Rain", t: "Free good", e: "Not scarce; no resources used." },
  { n: "Bottled water", t: "Economic good", e: "Uses resources; has a price." },
  { n: "A mobile phone", t: "Economic good", e: "Scarce; uses resources." },
  { n: "A free school meal", t: "Economic good", e: "Costs resources even if free to the pupil." },
  { n: "Clean air in a polluted city", t: "Can become an economic good", e: "Cleaning air takes resources." },
];
button_table("ggBtns", "ggOut", GG, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>Why</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td></tr></table></div>`);
function labS() {
  if (!$("#sa") || !$("#sb")) return;
  const sup = +$("#sa").value, dem = +$("#sb").value, sc = dem > sup, gap = Math.max(0, dem - sup);
  $("#sa1").textContent = sc ? "Economic good" : "Free good"; $("#sa2").textContent = gap; $("#sa3").textContent = sc ? "Yes" : "No";
  $("#sav").textContent = sc ? `At a price of zero, demand of ${dem} exceeds supply of ${sup} by ${gap}. The good is scarce, so resources are needed, it gets a price and it has an opportunity cost: an economic good.` : `At a price of zero, supply of ${sup} meets all demand of ${dem}. The good is not scarce, needs no scarce resources and has no price: a free good.`;
  const base = 280; let o = SV.line(60, base, 700, base);
  [["Supply", sup, "--good"], ["Demand", dem, "--bad"]].forEach(([n, v, cl], i) => { const x = 160 + i * 250, h = v * 1.8; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${cl})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, v, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labS").innerHTML = o + SV.text(60, 24, "Quantity available at a price of zero", "sm");
}
Lib.slider($("#g1"), { id: "sa", label: "Supply available at zero price", min: 10, max: 150, step: 10, value: 100, fmt: (v) => v, onInput: labS });
Lib.slider($("#g2"), { id: "sb", label: "Demand at zero price", min: 10, max: 150, step: 10, value: 60, fmt: (v) => v, onInput: labS });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each an <b>economic good</b> or a <b>free good</b>?", buckets: [{ label: "Economic good" }, { label: "Free good" }], items: [
  { text: "Sunlight", b: 1 }, { text: "Air in the countryside", b: 1 }, { text: "Rain", b: 1 },
  { text: "A car", b: 0 }, { text: "Healthcare", b: 0 }, { text: "Bottled water", b: 0 }, { text: "A school lunch paid for by taxes", b: 0 },
], done: "Economic goods are scarce and have a price." });
Lib.classify($("#cl2"), { prompt: "Does each describe an <b>economic good</b> or a <b>free good</b>?", buckets: [{ label: "Economic good" }, { label: "Free good" }], items: [
  { text: "Has an opportunity cost", b: 0 }, { text: "Uses scarce resources", b: 0 }, { text: "Has a price", b: 0 },
  { text: "No opportunity cost", b: 1 }, { text: "Not scarce", b: 1 }, { text: "No price", b: 1 },
], done: "Know the differences." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Economic good", "A scarce good that uses resources and has a price"],
  ["Free good", "A good that is not scarce and has no opportunity cost"],
  ["Opportunity cost", "The next best alternative given up"],
  ["Scarcity", "Limited resources compared with unlimited wants"],
  ["Price", "What a buyer pays for an economic good"],
  ["Free of charge", "Not paid for by the user but still uses resources"],
], done: "Free goods are not the same as free-of-charge goods." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why an economic good has an opportunity cost</b>.", items: [
  "Resources are scarce",
  "Making the good uses scarce resources",
  "Those resources could have made something else",
  "The next best alternative is given up",
  "So the good has an opportunity cost",
], done: "Scarcity leads to opportunity cost." });
''' + calc_js([
    ("A farmer uses 10 hectares for wheat worth $5,000. The next best use is rice worth $4,000. What is the opportunity cost of using it for wheat ($)?", 4000, "The next best alternative: <b>$4,000</b>.", None, None),
    ("A bottle of water costs $2 to produce and 100 are produced. What is the total cost ($)?", 200, "2 × 100 = <b>$200</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is an example of a free good?", ["Bottled water", "Sunlight", "A car", "Healthcare"], 1, "Not scarce, no price."),
    ("Economic goods:", ["Are not scarce", "Have no opportunity cost", "Are scarce and have an opportunity cost", "Have no price"], 2, "They use scarce resources."),
    ("A free good has:", ["A price", "No opportunity cost", "A high cost", "Scarce supply"], 1, "No scarce resources used."),
    ("A school meal paid for by taxes is:", ["A free good", "An economic good", "Not scarce", "Priceless"], 1, "It uses resources."),
    ("Why is the basic economic problem not solved by free goods?", ["They are too scarce", "They are only a small part of wants", "They cost money", "They are banned"], 1, "Most goods are economic goods."),
]) + "\n" + cards_js([("Economic good", "A good that is scarce, uses resources, has a price and an opportunity cost."), ("Free good", "A good that is not scarce, so it has no price and no opportunity cost."), ("Scarcity", "Limited resources compared with unlimited wants."), ("Opportunity cost", "The next best alternative given up."), ("Price", "What must be paid for an economic good."), ("Free of charge", "Not paid for by the user, but it still uses resources."), ("Resources", "Land, labour, capital and enterprise."), ("Supply", "The quantity firms are willing to produce at each price."), ("Demand", "The quantity buyers are willing to buy at each price.")]) + "labS(); \n"
explore = '''
  <h2>Lab 1 · Is it scarce?</h2>
  <p>Set the supply and demand for a good at a price of zero. If demand exceeds supply, it is scarce.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Type of good</small><strong id="sa1"></strong></div><div><small>Shortage</small><strong id="sa2"></strong></div><div><small>Opportunity cost?</small><strong id="sa3"></strong></div></div><div class="verdict" id="sav"></div></div></div>
    <svg id="labS" viewBox="0 0 760 320" role="img" aria-label="Supply and demand at zero price"></svg>
  </div>

  <h2>Lab 2 · Economic or free?</h2>
  <p>Pick a good to see its type and why.</p>
  <div class="card"><div class="row" id="ggBtns"></div><div id="ggOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define a free good. (Oct/Nov 2023, P11 style)", "Not scarce; no opportunity cost.", "[K|A free good is a good that is not scarce] [K|and so has no opportunity cost.]"),
    Q(2, "Identify", 2, "Identify two free goods. (Oct/Nov 2022, P12 style)", "Any two: sunlight, air, rain.", "[K|Sunlight.] [K|Air (or rain).]"),
    Q(3, "Identify", 2, "Identify a difference between economic goods and free goods.", "Economic goods scarce; free goods not.", "[K|Economic goods are scarce] [K|whereas free goods are not scarce / have no opportunity cost.]"),
    Q(4, "Explain", 4, "Explain how opportunity cost is different for economic goods and free goods. (Feb/Mar 2024, P12 style)", "Economic goods use scarce resources: opportunity cost. Free goods use none.",
      "[K|Economic goods are scarce and use up resources,] [N|so the resources could have been used to produce something else: there is an opportunity cost.] [K|Free goods are not scarce and use no scarce resources,] [N|so there is no alternative given up and no opportunity cost.]"),
    Q(5, "Explain", 4, "Explain why a free-of-charge school meal is still an economic good.", "Resources used; opportunity cost; paid by taxes.",
      "[K|The meal may be free to the pupil but producing it uses scarce resources such as food, labour and kitchens.] [N|Those resources could have been used to produce something else, so there is an opportunity cost.] [N|The meal is paid for by taxpayers, so it is an economic good.]"),
)
tp = tips([
    ("Free good = not scarce = no opportunity cost.", "Say all three."),
    ("Economic good = scarce = opportunity cost.", "Link to resources."),
    ("Free of charge is not a free good.", "Taxes pay for it."),
    ("Examples:", "sunlight, air, rain for free goods; cars, food, healthcare for economic goods."),
], cmds("Define", "Identify", "Explain"))
body = page(CL("1.1.3 Economic goods and free goods"), "Economic Goods and Free Goods", "The difference between economic goods and free goods, and why only economic goods have an opportunity cost. Syllabus 1.1.3.",
    learn=learn, watch=watch(("From free to economic goods", "stE"), ("Opportunity cost and the two kinds of goods", "stO")), explore=explore,
    practise=practise(("Economic or free?", "cl1", "card"), ("Which describes which?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Bottled water", "Water from a river is close to a free good, but bottled water uses plastic, labour and transport, and is sold for a price.", "A free good becoming an economic good."),
        rw("Clean air", "In heavily polluted cities, clean air can become scarce, and people pay for air filters and masks.", "A free good becoming scarce."),
        rw("Free healthcare", "Where treatment is free at the point of use, it still costs resources, paid for by taxes.", "Free of charge versus free good."),
        rw("Sunshine and solar panels", "Sunlight is free, but collecting its energy with solar panels uses scarce resources and has a cost.", "Free input, economic output.")),
    exam=ex, tips=tp)
write("e13", body, js, "Economic Goods and Free Goods", "ig-economic-free-goods")
