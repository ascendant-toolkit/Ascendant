"""Builds the three IGCSE Economics 4.3 Monetary policy reviews (4.3.1 to 4.3.3) from slices of mon.* plus new content.
Run: python3 tools/artifact-kit/mk_ig43.py"""
from igsy import *
M = Old("mon")
HEAD = M.j_((2, 25))
CL = lambda t: f"IGCSE Economics · 0455 · {t}"
EX, RW = details(M), rws(M)
CALC, QUIZ = 'Lib.calc($("#c1")', 'Lib.quiz($("#qz1")'
CARDS = {a: b for a, b in pick_cards(M, ["Money supply", "Monetary policy", "Central bank", "Interest rate", "Base rate", "Foreign exchange rate", "Floating exchange rate", "Fixed exchange rate", "Depreciation", "Appreciation", "Devaluation", "Revaluation", "Quantitative easing", "Expansionary monetary policy", "Contractionary monetary policy", "Demand-pull inflation", "Imported inflation", "Time lag"])}
cards = lambda *names: cards_js([(n, CARDS[n]) for n in names])

# =========================================================== 4.3.1 Definitions
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The <span class="kw">money supply</span> is the total amount of money in an economy. <span class="kw">Monetary policy</span> is the use of the money supply, interest rates and the foreign exchange rate to influence aggregate demand and inflation. It is usually run by the <b>central bank</b>, which sets the main interest rate and has the tools to change how much money is available.</p></div>

  <h2>What is in the money supply?</h2>
  <div class="grid2">
    <div class="card"><h3>Notes and coins</h3><p>Cash in circulation, issued by the central bank.</p></div>
    <div class="card"><h3>Bank deposits</h3><p>The money households and firms hold in current and saving accounts, which they can spend by card or transfer. This is most of the money supply in many countries.</p></div>
  </div>
  <p>Commercial banks <b>create</b> money when they lend: a loan becomes a new deposit in the borrower's account. This is why the central bank can influence the money supply by influencing how much banks lend.</p>
''' + M.b((25, 32)) + '''
  <h2>The chain of control</h2>
  <ol>
    <li>The <b>central bank</b> sets the base interest rate and the conditions for the money supply.</li>
    <li><b>Commercial banks</b> follow: they adjust the rates they charge borrowers and pay savers.</li>
    <li><b>Households and firms</b> borrow, save and spend in response.</li>
    <li><b>Aggregate demand</b> changes, and so do output, jobs and prices.</li>
  </ol>
''' + M.b((107, 116))
flow = '''
const WHO = ["The central bank sets the base interest rate and controls the money supply", "Commercial banks change their lending and saving rates", "Households and firms borrow, save and spend differently", "Total spending (aggregate demand) changes", "Output, jobs and prices respond"];
function flowChart(s) {
  const bh = 52, gap = 22, x = 110, w = 540; let o = "";
  WHO.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: "fill:var(--accent);fill-opacity:0.14;stroke:var(--accent);stroke-width:2" });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1") + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < WHO.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
}
Lib.stepper($("#stW"), { w: 760, h: 400, label: "Who does what in monetary policy", base: { n: 0 }, draw: flowChart, steps: [
  { cap: "In most countries the <b>central bank</b> runs monetary policy. It sets the <b>base interest rate</b> and can change the <b>money supply</b>.", s: { n: 1 } },
  { cap: "<b>Commercial banks</b> follow the central bank, raising or lowering the rates on loans, mortgages and savings.", s: { n: 2 } },
  { cap: "<b>Households and firms</b> respond to the new rates by borrowing, saving and spending more or less.", s: { n: 3 } },
  { cap: "Their decisions change <b>total spending: aggregate demand</b>.", s: { n: 4 } },
  { cap: "Output, jobs and prices respond. That is why monetary policy is aimed at <b>aggregate demand and inflation</b>.", s: { n: 5 } },
] });
'''
explore = '''
  <h2>Lab 1 · From the base rate to your wallet</h2>
  <p>Commercial banks set their own rates around the central bank's base rate. Here the loan rate is 3 points above base and the savings rate is 1 point below.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Savings rate</small><strong id="wa1"></strong></div><div><small>Loan rate</small><strong id="wa2"></strong></div><div><small>Yearly interest on a $200,000 loan</small><strong id="wa3"></strong></div><div><small>Yearly interest on $10,000 savings</small><strong id="wa4"></strong></div></div><div class="verdict" id="wav"></div></div></div>
    <svg id="labW" viewBox="0 0 760 340" role="img" aria-label="Base rate, saving rate and loan rate"></svg>
  </div>

  <h2>Lab 2 · What is the stance?</h2>
  <p>Choose a move for each tool and see whether the overall policy is expansionary, contractionary or mixed.</p>
  <div class="card"><div id="stBtns"></div><div class="verdict" id="stOut"></div></div>
'''
labw = '''
function labW() {
  if (!$("#wa")) return;
  const r = +$("#wa").value, sv = Math.max(0, r - 1), ln = r + 3;
  $("#wa1").textContent = money(sv, 1) + "%"; $("#wa2").textContent = money(ln, 1) + "%";
  $("#wa3").textContent = "$" + Math.round(200000 * ln / 100).toLocaleString("en-US"); $("#wa4").textContent = "$" + Math.round(10000 * sv / 100).toLocaleString("en-US");
  $("#wav").textContent = r <= 2 ? "A low base rate means cheap borrowing and little reward for saving: households and firms are likely to spend and invest more." : r >= 7 ? "A high base rate makes borrowing expensive and saving rewarding: spending and investment are likely to fall." : "A middle rate: neither strongly encouraging nor discouraging spending.";
  const base = 290, k = 17; let o = SV.line(60, base, 700, base);
  [["Savings rate", sv, "--good"], ["Base rate", r, "--accent"], ["Loan rate", ln, "--bad"]].forEach(([n, v, c], i) => {
    const x = 130 + i * 190, h = v * k;
    o += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, money(v, 1) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 22, n, "sm", { "text-anchor": "middle" });
  });
  $("#labW").innerHTML = o;
}
Lib.slider($("#g1"), { id: "wa", label: "Central bank base rate", min: 0, max: 10, step: 0.5, value: 4, fmt: (v) => v + "%", onInput: labW });
const TOOLS = [["Interest rate", ["Raise", "Hold", "Cut"]], ["Money supply", ["Reduce", "Hold", "Increase"]], ["Exchange rate", ["Raise", "Hold", "Lower"]]];
const pick = [1, 1, 1];
function stance() {
  $("#stBtns").innerHTML = TOOLS.map(([n, o], i) => `<div class="row" style="margin:6px 0"><b style="min-width:120px;display:inline-block">${n}</b>${o.map((t, j) => `<button class="b${pick[i] === j ? " pri" : ""}" data-i="${i}" data-j="${j}">${t}</button>`).join("")}</div>`).join("");
  $$("#stBtns .b").forEach((b) => (b.onclick = () => { pick[+b.dataset.i] = +b.dataset.j; stance(); }));
  const sc = pick.reduce((a, j) => a + (j - 1), 0);
  $("#stOut").textContent = sc >= 2 ? "Expansionary: these moves are likely to raise aggregate demand. Watch for inflation." : sc <= -2 ? "Contractionary: these moves are likely to reduce aggregate demand. Watch for unemployment." : sc === 0 && pick.every((j) => j === 1) ? "No change: policy is unchanged." : sc > 0 ? "Mildly expansionary: the net effect is a modest rise in AD." : sc < 0 ? "Mildly contractionary: the net effect is a modest fall in AD." : "Mixed: the moves pull in opposite directions, so the overall effect on AD is small.";
}
stance();
'''
js = HEAD + flow + seg(M, "/* ---------- 4.", "/* ======") + labw + '''
/* ================= PRACTISE ================= */
''' + blk(M, 'Lib.classify($("#cl1")') + '''Lib.classify($("#cl2"), { prompt: "Is each <b>fiscal</b> or <b>monetary</b> policy?", buckets: [{ label: "Fiscal policy" }, { label: "Monetary policy" }], items: [
  { text: "Raise income tax", b: 0 }, { text: "Build a new hospital", b: 0 }, { text: "Cut VAT", b: 0 }, { text: "Increase unemployment benefit", b: 0 },
  { text: "Central bank cuts the base rate", b: 1 }, { text: "Central bank buys government bonds", b: 1 }, { text: "Currency allowed to fall", b: 1 }, { text: "Central bank raises its lending rate", b: 1 },
], done: "Fiscal: government spending and taxes. Monetary: interest rates, money supply, exchange rate." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Money supply", "Total amount of money in an economy"],
  ["Monetary policy", "Use of money supply, interest rates and exchange rates to influence AD and inflation"],
  ["Central bank", "Banker to the government and commercial banks, and monetary authority"],
  ["Commercial bank", "A bank that takes deposits and makes loans to households and firms"],
  ["Base rate", "The central bank's main interest rate"],
  ["Expansionary policy", "Aims to raise aggregate demand"],
  ["Contractionary policy", "Aims to reduce aggregate demand"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the <b>chain of control</b> in order.", items: [
  "The central bank changes the base interest rate",
  "Commercial banks change their loan and saving rates",
  "Households and firms borrow, save and spend differently",
  "Aggregate demand changes",
  "Output, jobs and prices respond",
], done: "The route from the central bank to the economy." });
''' + calc_js([
    ("The money supply is $500bn. It rises by 8%. What is the new money supply ($bn)?", 540, "500 × 1.08 = <b>$540bn</b>.", None, None),
    ("A bank pays 3% interest on savings. How much interest does $2,000 earn in a year ($)?", 60, "2,000 × 3% = <b>$60</b>.", None, None),
], items(M, CALC, 0, 2)) + mcq_js("qz1", [
    ("What is the money supply?", ["The amount of money the government spends", "The total amount of money in an economy", "The amount of gold a country holds", "The amount of tax collected"], 1, "It includes notes, coins and bank deposits."),
    ("Which organisation usually carries out monetary policy?", ["The central bank", "The tax authority", "A trade union", "A commercial firm"], 0, "The central bank sets interest rates and influences the money supply."),
    ("Which is a monetary policy measure?", ["Cutting income tax", "Cutting the base interest rate", "Building a motorway", "Raising VAT"], 1, "Interest rates are monetary; tax and spending are fiscal."),
    ("Which is expansionary monetary policy?", ["Raising interest rates", "Increasing the money supply", "Raising the exchange rate", "Cutting government spending"], 1, "A bigger money supply tends to lower rates and raise spending."),
    ("The main aim of monetary policy is to influence:", ["Aggregate demand and inflation", "The size of firms", "The level of tax revenue only", "Population growth"], 0, "Monetary policy works through AD and the price level."),
]) + "\n" + cards("Money supply", "Monetary policy", "Central bank", "Interest rate", "Base rate", "Expansionary monetary policy", "Contractionary monetary policy") + "labW();\n"
ex = exam(EX[0],
    Q(2, "Define", 2, "What is meant by the money supply?", "Two ideas: the total amount of money, and what it includes (notes, coins and bank deposits).",
      "[K|The money supply is the total amount of money in an economy,] [K|including notes and coins in circulation and the money held in bank accounts.]"),
    Q(3, "Explain", 4, "Explain two functions a central bank performs for its government. (May/June 2022, P22)", "Pick two clear functions and develop each: banker to the government, manages the national debt, holds reserves, sets interest rates, implements monetary policy.",
      "[K|A central bank acts as the government's banker.] [N|It holds the government's accounts and handles payments, and may help the government to borrow by selling its bonds.] [K|It also carries out the government's monetary policy.] [N|It sets the base interest rate and controls the money supply, which could be used to influence aggregate demand and inflation.]"),
    Q(4, "Explain", 4, "Explain one difference between monetary policy and fiscal policy.", "Use 'whereas'. Compare the tools, or who decides.",
      "[K|Monetary policy uses interest rates, the money supply and the exchange rate,] [K|whereas fiscal policy uses government spending and taxation.] [A|Interest rate decisions are often made by an independent central bank,] [N|whereas a budget is decided by the government, so fiscal policy can be targeted at a group or a project while a change in interest rates affects the whole economy.]"),
)
tp = tips([
    ("Three tools:", "interest rates, money supply, exchange rate. Name all three."),
    ("Say what the policy is for.", "To influence aggregate demand and inflation."),
    ("Central bank, not government.", "In most countries the central bank sets interest rates."),
    ("Do not mix up fiscal and monetary.", "Tax and spending are fiscal."),
    ("Money supply includes deposits.", "Not just notes and coins."),
], cmds("Define", "Identify", "Explain"))
body = page(CL("4.3.1 Definitions of money supply and monetary policy"), "Money Supply and Monetary Policy", "What the money supply is, what monetary policy is, what a central bank does, and how policy is passed to the economy. Syllabus 4.3.1.",
    learn=learn, watch=watch(("Who does what in monetary policy", "stW"), ("Monetary policy and AD / AS", "stA")), explore=explore,
    practise=practise(("Expansionary or contractionary?", "cl1", "card"), ("Fiscal or monetary?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain of control", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(RW[0], RW[1], RW[4], rw("Independent central banks", "In many countries, including the UK and the eurozone, the central bank sets interest rates independently of politicians, with a target for inflation.", "A reason why monetary policy may be more consistent than fiscal policy: decisions are less tied to elections.")), exam=ex, tips=tp)
write("mp1", body, js, "Money Supply and Monetary Policy", "ig-monetary-definitions")

# =========================================================== 4.3.2 Measures
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The syllabus lists three monetary policy measures: changes in the <b>interest rate</b>, the <b>money supply</b> and the <b>foreign exchange rate</b>. Each can be expansionary or contractionary. For each one, follow the chain: what changes, who is affected, and what happens to aggregate demand.</p></div>
''' + M.b((34, 53)) + M.b((54, 63)) + M.b((64, 83))
explore = M.b((130, 136)).replace("Lab 1 ·", "Lab 1 ·") + M.b((137, 143))
js = HEAD + seg(M, "/* ---------- 1.", "/* ---------- 4.") + seg(M, "/* Lab 1", "/* Lab 3") + '''
/* ================= PRACTISE ================= */
''' + blk(M, 'Lib.classify($("#cl2")') + blk(M, 'Lib.classify($("#cl3")') + blk(M, 'Lib.classify($("#cl4")') + blk(M, 'Lib.order($("#o1")') + blk(M, 'Lib.order($("#o2")') + '''Lib.match($("#m1"), { prompt: "Match the measure to what it does.", pairs: [
  ["Cut interest rates", "Cheaper borrowing, less reward for saving: spending is likely to rise"],
  ["Raise interest rates", "Costlier borrowing, more reward for saving: spending is likely to fall"],
  ["Increase money supply", "Banks have more to lend, which tends to push rates down"],
  ["Quantitative easing", "Central bank buys large amounts of bonds to raise the money supply"],
  ["Lower the exchange rate", "Exports cheaper abroad, imports dearer at home"],
  ["Raise the exchange rate", "Exports dearer abroad, imports cheaper at home"],
], done: "Link each measure to its effect." });
''' + calc_js([], items(M, CALC, 0, 1, 2, 3, 4, 5, 6, 7)).replace("[\n", "[\n", 1) + "" + mcq_js("qz1", [
    ("Which is a monetary policy measure?", ["A change in income tax rates", "A change in government spending on roads", "A change in interest rates", "A change in subsidies to farmers"], 2, "Interest rates, money supply and the exchange rate are the monetary tools."),
    ("A central bank wants to reduce demand-pull inflation. What should it do?", ["Cut interest rates", "Raise interest rates", "Increase the money supply", "Lower the exchange rate"], 1, "Higher rates cut borrowing and spending, so AD shifts left."),
    ("A fall in the exchange rate is most likely to:", ["Make exports more expensive for foreigners", "Make imports cheaper", "Make exports cheaper for foreigners", "Reduce the risk of imported inflation"], 2, "A lower exchange rate cuts the foreign currency price of exports."),
    ("Which is a likely effect of an increase in the money supply?", ["Interest rates tend to rise", "Banks have more to lend, so interest rates may fall", "Aggregate demand falls", "The exchange rate is certain to rise"], 1, "More money in the banking system makes credit cheaper and easier to get."),
    ("A rise in interest rates is most likely to benefit:", ["A household with a variable mortgage", "A firm planning to borrow", "A saver", "An exporter when the currency rises"], 2, "Savers earn more. Borrowers pay more."),
    ("Buying government bonds from banks is likely to:", ["Reduce the money supply", "Increase the money supply", "Raise taxes", "Raise the interest rate"], 1, "The central bank pays the banks, so they have more to lend."),
]) + "\n" + cards("Interest rate", "Base rate", "Foreign exchange rate", "Floating exchange rate", "Fixed exchange rate", "Depreciation", "Appreciation", "Devaluation", "Revaluation", "Quantitative easing", "Imported inflation", "Time lag") + "labI(); labX();\n"
ex = exam(EX[1], EX[2], EX[3],
    Q(4, "Explain", 4, "Explain how a central bank could increase the money supply.", "Name a method and follow it through: bonds, banks' lending, interest rates.",
      "[K|A central bank could buy government bonds from banks and investors.] [N|It pays for them with new money, so banks have more funds available to lend.] [N|More lending increases the amount of money in the economy and tends to push interest rates down, which could raise spending.] [A|Large-scale bond buying of this kind is called quantitative easing.]"),
    Q(5, "Explain", 4, "Explain how a rise in the interest rate may affect households and firms.", "Both groups, each with a chain. Borrowers and savers.",
      "[K|A rise in the interest rate makes borrowing more expensive and saving more rewarding.] [N|Households with loans or variable-rate mortgages have higher payments and less income to spend, so consumption could fall, though savers earn more.] [N|Firms face higher borrowing costs, so fewer investment projects look profitable and investment may fall.]"),
)
tp = tips([
    ("Three tools only:", "interest rate, money supply, exchange rate. Name the one in the question."),
    ("Interest rate chains need both sides.", "Borrowers and savers, households and firms."),
    ("Money supply up usually means interest rates down.", "Link the two."),
    ("Exchange rate chains start with prices.", "Export price abroad, import price at home, competitiveness, demand, jobs."),
    ("Elasticity decides how big the effect is.", "Inelastic demand means a lower exchange rate may not improve trade much."),
], cmds("Identify", "Explain", "Analyse"))
body = page(CL("4.3.2 Monetary policy measures"), "Monetary Policy Measures", "Changes in the interest rate, the money supply and the foreign exchange rate: how each works and who it affects. Syllabus 4.3.2.",
    learn=learn, watch=watch(("Interest rates and aggregate demand", "stC"), ("The money supply and the interest rate", "stMS"), ("A fall in the exchange rate", "stX")), explore=explore,
    practise=practise(("Which tool?", "cl2", "card"), ("Depreciation or appreciation?", "cl3", "card"), ("Who gains from a rate rise?", "cl4", "card"), ("Match the measure", "m1", "card"), ("Order the interest rate chain", "o1", "card"), ("Order the exchange rate chain", "o2", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(RW[0], RW[1], RW[3], RW[5], RW[6], RW[7]), exam=ex, tips=tp)
write("mp2", body, js, "Monetary Policy Measures", "ig-monetary-measures")

# =========================================================== 4.3.3 Effects on aims
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Monetary policy can help a government meet its macroeconomic aims, but each measure helps some aims and may harm others. <b>Expansionary</b> policy (lower rates, more money, a lower exchange rate) tends to help growth and jobs but risks inflation and a worse current account. <b>Contractionary</b> policy tends to help prices but risks growth and jobs. Good answers name the aim, follow the chain, then evaluate.</p></div>
''' + M.b((84, 94)) + M.b((95, 105))
flowc = '''
const MCH = ["Central bank cuts the base interest rate", "Borrowing is cheaper: consumption ↑ and investment ↑", "AD shifts to the right", "Real GDP ↑ and unemployment ↓", "Price level ↑: risk of demand-pull inflation", "Imports ↑ and the currency may fall: current account effect unclear"];
function mchain(s) {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  MCH.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap), col = i < 4 ? "--good" : "--bad";
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < MCH.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 400, label: "Gains and costs of cutting interest rates", base: { n: 0 }, draw: mchain, steps: [
  { cap: "The central bank <b>cuts the base interest rate</b> to support the economy.", s: { n: 1 } },
  { cap: "Borrowing is cheaper and saving pays less, so <b>consumption and investment rise</b>.", s: { n: 2 } },
  { cap: "AD shifts <b>right</b>.", s: { n: 3 } },
  { cap: "<b>Gains:</b> real GDP rises and firms take on more workers. Growth and employment aims move closer.", s: { n: 4 } },
  { cap: "<b>Cost:</b> as demand rises the price level may rise, especially near full capacity: demand-pull inflation. This is a <b>conflict of aims</b>.", s: { n: 5 } },
  { cap: "Higher incomes raise <b>imports</b>, and lower rates may weaken the currency. The effect on the current account depends on elasticity.", s: { n: 6 } },
] });
'''
explore = M.b((145, 152)).replace("Lab 3 ·", "Lab 1 ·") + M.b((153, 157)).replace("Lab 4 ·", "Lab 2 ·")
js = HEAD + seg(M, "/* ---------- 4.", "/* ======") + flowc + seg(M, "/* Lab 3", "/* ======") + '''
/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>gain</b> or a <b>cost or risk</b> of expansionary monetary policy?", buckets: [{ label: "Gain" }, { label: "Cost or risk" }], items: [
  { text: "Real GDP could rise", b: 0 }, { text: "Unemployment could fall", b: 0 }, { text: "Firms find investment cheaper", b: 0 }, { text: "Exports become cheaper if the currency falls", b: 0 },
  { text: "Demand-pull inflation", b: 1 }, { text: "Savers earn less", b: 1 }, { text: "Imported inflation if the currency falls", b: 1 }, { text: "Higher imports and a worse current account", b: 1 },
], done: "Every policy has gains and costs: that is evaluation." });
Lib.classify($("#cl2"), { prompt: "Which <b>macroeconomic aim</b> is each measure mainly <b>aimed at</b>? Think about the problem the central bank is trying to fix.", buckets: [{ label: "Growth and jobs" }, { label: "Stable prices" }, { label: "Balance of payments" }], items: [
  { text: "Cut interest rates because the economy is in a slump", b: 0 }, { text: "Increase the money supply because unemployment is high", b: 0 },
  { text: "Raise interest rates because demand-pull inflation is rising", b: 1 }, { text: "Reduce the money supply because prices are rising quickly", b: 1 },
  { text: "Lower the exchange rate because the current account deficit is large", b: 2 }, { text: "Devalue the currency to make exports cheaper and imports dearer", b: 2 },
], done: "Name the problem being fixed. Note that one tool can affect several aims: a lower exchange rate helps the current account but may raise import prices." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why a cut in interest rates could conflict with stable prices</b>.", items: [
  "The central bank cuts interest rates",
  "Borrowing rises and saving falls",
  "Spending increases and AD shifts right",
  "AD grows faster than the economy can supply",
  "Demand-pull inflation",
], done: "A conflict between full employment and stable prices." });
''' + calc_js([
    ("Real GDP is $400bn and rises to $412bn. What is the percentage growth?", 3, "12 ÷ 400 × 100 = <b>3%</b>.", None, None),
    ("The price level rises from 125 to 130. What is the inflation rate (%)?", 4, "5 ÷ 125 × 100 = <b>4%</b>.", None, None),
]) + mcq_js("qz1", [
    ("A cut in interest rates could create a conflict between:", ["Full employment and stable prices", "Equal pay and growth", "Free trade and tariffs", "Poverty and population"], 0, "More spending may cut unemployment but raise demand-pull inflation."),
    ("Which is a limit on the effectiveness of monetary policy?", ["Low confidence among borrowers", "Higher AD", "More jobs", "Lower rates"], 0, "If households and firms are worried, they may not borrow even at low rates."),
    ("A central bank is worried about inflation. The measure most likely to help is:", ["Cutting rates", "Raising rates", "Increasing the money supply", "Lowering the exchange rate"], 1, "Higher rates reduce AD."),
    ("A country that fixes its currency to the US dollar will find that:", ["It can set its own interest rates freely", "It tends to follow the interest rates of the US", "Its exports always rise", "Its currency never changes"], 1, "A peg limits independent monetary policy."),
    ("A lower exchange rate is most likely to:", ["Reduce the price of imports", "Make exports cheaper for foreign buyers", "Raise the interest rate", "Reduce AD"], 1, "Exports become more price competitive."),
]) + "\n" + cards("Expansionary monetary policy", "Contractionary monetary policy", "Demand-pull inflation", "Imported inflation", "Time lag", "Fixed exchange rate", "Depreciation", "Appreciation") + "labM(); showSC(0);\n"
ex = exam(EX[4], EX[5], EX[6], EX[7])
tp = tips([
    ("Name the aim, then follow the chain.", "Growth, employment, prices, balance of payments."),
    ("Always give a cost as well as a gain.", "Expansionary: inflation, imports. Contractionary: jobs, growth."),
    ("Conflict questions: name two pairs of aims.", "For example employment and inflation, growth and the current account."),
    ("Evaluate with lags, confidence, elasticity and the state of the economy.", "Spare capacity or near full capacity matters most."),
    ("Fixed exchange rate:", "certainty and discipline, but no independent monetary policy."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("4.3.3 Effect of monetary policy on macroeconomic aims"), "Effects of Monetary Policy on the Aims", "How monetary policy measures could help a government meet its macroeconomic aims, the conflicts between them and the limits of monetary policy. Syllabus 4.3.3.",
    learn=learn, watch=watch(("Gains and costs of cutting interest rates", "stG"), ("Monetary policy and AD / AS", "stA")), explore=explore,
    practise=practise(("Gain or cost?", "cl1", "card"), ("Which aim does it support?", "cl2", "card"), ("Order the conflict chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(RW[0], RW[1], RW[2], RW[5], RW[6], RW[7]), exam=ex, tips=tp)
write("mp3", body, js, "Effects of Monetary Policy on the Aims", "ig-monetary-aims")
