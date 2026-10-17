"""AS syllabus 5.3.1-5.3.2 Monetary policy: tools and the central bank. Run: python3 tools/artifact-kit/mk_as54.py"""
from as6k import *
EY = EYAS("5.3.1 to 5.3.2")

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p><b class="kw">Monetary policy</b> is the use of <b>interest rates, the money supply and credit regulation</b> to influence aggregate demand and meet macroeconomic objectives, and it is usually carried out by the <b class="kw">central bank</b>. The central bank sets the <b class="kw">base (policy) interest rate</b>, which feeds through to the rates that banks charge borrowers and pay savers, so changing it alters the <b>cost of borrowing</b>, the <b>reward for saving</b>, the <b>exchange rate</b> and <b>expectations</b>. It can also change the <b>money supply</b> (for example through <b class="kw">quantitative easing</b>) and the <b>rules on bank lending</b> (<b class="kw">credit regulation</b>) to make credit easier or harder to obtain. Many central banks have an <b>inflation target</b> and an independent role, which helps to make their policy credible. Each tool works through <b>consumption, investment and net exports</b>, and the effects depend on how people respond to interest rates and on the state of confidence.</p></div>

  <h2>1 · Monetary policy and the central bank</h2>
  <ul>
    <li><b>Who:</b> the <b>central bank</b> (for example the Bank of England, the US Federal Reserve, the European Central Bank). It is often <b>independent</b> of the government, so decisions are not driven by election timing.</li>
    <li><b>Objectives:</b> usually <b>price stability</b> (an <b>inflation target</b>, often 2%), while supporting growth and employment, and keeping the financial system stable.</li>
    <li><b>Other roles:</b> bank to the government and to commercial banks, lender of last resort, and manager of the currency and foreign exchange reserves.</li>
    <li><b>Compare with fiscal policy:</b> fiscal policy uses government spending and taxation, decided by the government; monetary policy works through the price and quantity of money and credit, decided by the central bank. Changes in monetary policy are usually quicker to decide, but take time to work.</li>
  </ul>
  <div id="pic1" class="card"></div>

  <h2>2 · Tool 1: Interest rates</h2>
  <ul>
    <li>The central bank sets the <b>base rate</b>, the rate at which it lends to commercial banks. Banks then adjust their own rates on <b>mortgages, loans, credit cards and savings</b>.</li>
    <li><b>A cut in the rate:</b> borrowing becomes cheaper, saving less rewarding, so households and firms spend and invest more. People with variable-rate mortgages have more disposable income. Asset prices (houses, shares) tend to rise, creating a <b>wealth effect</b>. The currency may weaken as hot money flows out, which raises net exports.</li>
    <li><b>A rise in the rate:</b> the opposite. Spending and investment fall, saving rises, and the currency may strengthen.</li>
    <li><b>Real interest rate</b> = nominal rate − inflation. It is the real cost of borrowing and the real reward for saving. A negative real rate means borrowers gain and savers lose in real terms.</li>
    <li><b>Who gains and loses from higher rates:</b> savers gain; borrowers (especially mortgage holders) and firms with debts lose.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Channel</th><th>How a rate cut works</th></tr>
    <tr><td><b>Consumption</b></td><td>Cheaper credit, lower return on saving, more disposable income for borrowers, higher asset values</td></tr>
    <tr><td><b>Investment</b></td><td>Lower cost of financing projects, so more become profitable</td></tr>
    <tr><td><b>Exchange rate</b></td><td>Lower returns on holding the currency, so it may depreciate, raising net exports</td></tr>
    <tr><td><b>Expectations and confidence</b></td><td>Signals that the central bank wants more spending, but weak confidence may offset it</td></tr>
  </table></div>

  <h2>3 · Tool 2: The money supply</h2>
  <ul>
    <li><b>Money</b> includes cash and bank deposits. Banks create money when they lend, so the amount of credit in the economy is closely linked to the money supply.</li>
    <li><b>Open market operations:</b> the central bank buys or sells <b>government bonds</b>. Buying bonds puts money into the banking system, raising the money supply; selling bonds removes money.</li>
    <li><b>Quantitative easing (QE):</b> large-scale purchases of bonds, often when interest rates are already close to zero, to raise the money supply, lower long-term interest rates and encourage lending and spending.</li>
    <li><b>Reserve requirements:</b> rules on how much banks must hold in reserve, which limit how much they can lend.</li>
    <li>A larger money supply tends to <b>lower interest rates and raise spending</b>; a smaller one does the reverse. Too fast an expansion risks <b>inflation</b>.</li>
  </ul>

  <h2>4 · Tool 3: Credit regulation</h2>
  <ul>
    <li><b>Credit regulation</b> is the rules governing how banks lend, which affect how easily households and firms can borrow.</li>
    <li><b>Examples:</b> capital requirements for banks, limits on <b>loan-to-value</b> (the deposit a buyer must put down), checks on borrowers' ability to pay, and limits on the growth of lending.</li>
    <li><b>Loosening</b> the rules (lower deposits, easier loans) is <b>expansionary</b>; <b>tightening</b> them is <b>contractionary</b>.</li>
    <li>It can target a particular problem, such as a house-price bubble, without changing interest rates for everyone.</li>
  </ul>

  <h2>5 · Inflation targets and credibility</h2>
  <ul>
    <li>Many central banks aim for a published <b>inflation target</b>. If people believe the target, <b>expectations</b> of inflation stay low, which helps to avoid a wage-price spiral.</li>
    <li>A target may be unhelpful if the bank is unwilling to take the steps needed, because raising rates to meet it risks a downturn.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Name the <b>tool</b>, explain <b>how it changes</b> borrowing and spending (the transmission), and say whether it is <b>expansionary or contractionary</b>. Use <b>real</b> interest rates when asked about the cost of borrowing. The effects on AD and the evaluation come on the next page.</div>
'''

watch = '''
  <h2>1 · How a rate cut works through the economy</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stT"></div>
  <h2>2 · How quantitative easing works</h2>
  <div id="stQ"></div>
  <h2>3 · Tightening credit regulation</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · A change in the base rate: who gains and loses?</h2>
  <p>A household has a variable-rate mortgage and some savings. Change the base rate to see the effect on monthly payments and interest earned.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Monthly mortgage interest</small><strong id="r1"></strong></div><div><small>Yearly interest on savings</small><strong id="r2"></strong></div><div><small>Net change in monthly budget</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 220" role="img" aria-label="Bars for monthly mortgage interest and savings interest"></svg></div></div></div>

  <h2>Lab 2 · Real interest rates</h2>
  <p>Households and firms respond to the real interest rate. Set the nominal rate and inflation.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Real interest rate</small><strong id="t1"></strong></div><div><small>Effect on borrowing</small><strong id="t2"></strong></div><div><small>Effect on saving</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Bars for nominal interest rate, inflation and real interest rate"></svg></div></div></div>
''' + chooser_html("h", "Lab 3 · Choose a tool", "Choose a tool of monetary policy to see how it works, which way it pushes AD and the main drawback.", ["How it works", "Direction (cut or loosen)", "Main drawback"])

practise = '''
  <h2>1 · Which tool is it?</h2><div id="cl1" class="card"></div>
  <h2>2 · Expansionary or contractionary?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the effect of a rate rise in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A central bank sets the base rate", "A central bank meets regularly to decide the base rate. If inflation is above its target, it may raise the rate; if the economy is weak, it may cut it. Commercial banks then change their mortgage and loan rates.", "interest rates as the main tool.") +
rw("Mortgage holders and savers", "When rates rise, people with variable-rate mortgages pay more each month, so they have less to spend, while savers earn more. The overall effect on spending depends on who has the larger response.", "the effects of interest rates on households.") +
rw("Quantitative easing", "With interest rates close to zero, a central bank creates money to buy government bonds, lowering longer-term interest rates and raising the money supply to encourage spending and lending.", "money supply as a tool of expansionary policy.") +
rw("Easier credit rules", "A central bank relaxes the deposit rules for mortgages. More households can borrow to buy homes, spending rises and house prices may rise. This is expansionary credit regulation.", "credit regulation.") +
rw("Inflation targeting", "A central bank announces a 2% inflation target. If people believe it, they expect low inflation, which helps to keep wage demands and price rises down.", "inflation targets and expectations.")
)

mc_exam = [
  mcq("m25_12", 23, "A country's central bank decides to reduce the level of credit regulation. What is this an example of?", ["contractionary fiscal policy", "contractionary monetary policy", "expansionary fiscal policy", "expansionary monetary policy"], 3, "Looser credit rules make borrowing easier, which is expansionary monetary policy."),
  mcq("s20_12", 19, "What is likely to cause a decrease in aggregate demand?", ["an appreciation in the exchange rate", "an improvement in consumer confidence", "an increase in government expenditure", "an increase in the money supply"], 0, "A higher exchange rate lowers net exports, reducing AD. The other options raise AD."),
  mcq("m22_12", 23, "The diagram shows a shift in an economy's aggregate demand curve from AD1 to AD2 (to the right). What could not be a cause of the shift?", ["a decrease in income tax", "a decrease in the price of goods", "an increase in money wage rates", "an increase in the money supply"], 1, "A change in the price level causes a movement along AD, not a shift."),
  mcq("m23_12", 22, "What is most likely to cause a rise in a country's exchange rate?", ["a fall in its direct taxes", "a fall in its export orders", "a rise in its interest rates", "a rise in its imports"], 2, "Higher interest rates attract funds from abroad, raising demand for the currency."),
  mcq("s20_13", 22, "A country operates a floating exchange rate. What will cause the demand curve for the country's currency to shift left in the foreign exchange market?", ["a decrease in the country's interest rate", "a decrease in the country's money supply", "an increase in the country's export sales", "an increase in the country's import purchases"], 0, "Lower interest rates reduce the return on holding the currency, so demand falls."),
  mcq("s21_12", 30, "Which policy will not cause a reduction in the rate of inflation?", ["increasing income tax", "reducing government spending", "reducing interest rates", "removing subsidies"], 2, "Cutting interest rates raises AD, which would add to inflation."),
  mcq("m21_12", 28, "The table shows the consumer prices index (CPI) for an economy: 2016 100, 2017 103, 2018 101, 2019 97. Which action is the government most likely to take to achieve price stability?", ["appreciate the exchange rate", "decrease the budget deficit", "increase the money supply", "increase the rate of interest"], 2, "Prices are falling, so an increase in the money supply would raise AD and push prices up."),
  mcq("s20_12", 27, "In an economy with an interest rate of 4% per annum, the rate of inflation falls from 5% to 3% per annum. What will be a benefit of this fall?", ["Menu costs will fall to zero.", "People on fixed incomes will be better off in real terms.", "Savers will gain in real terms.", "The purchasing power of the currency will rise."], 2, "The real interest rate rises from −1% to +1%, so savers now earn a positive real return.")
]

exam = exam_page("monetary policy tools",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The tools of monetary policy appear in 2 to 6 mark data-response parts (real interest rates, inflation targets) and in many Paper 1 questions on shifts of AD, credit and the exchange rate. Two reworded Paper 2 parts are below, with eight Paper 1 multiple choice questions that do not need a diagram.",
  [("Data response, 2 marks", "1", "Oct/Nov 2024 (21) Q1(b)"), ("Data response, 6 marks", "1", "May/June 2025 (21) Q1(e)"), ("Multiple choice (Paper 1)", "8 shown below", "2020 to 2025")],
  [
  eq(P("w24_21", "1(b)"), "2 marks", "Explain what is meant by 'the real interest rate will be negative' in an economy where the nominal interest rate is 40% and the inflation rate is 50%.",
     ["A negative real interest rate is when the interest rate is lower than the inflation rate (1).", "The real interest rate is calculated as the nominal rate minus inflation, so here it is 40 − 50 = −10% (1). The original question asked for the figure for Argentina in January 2022 or the method of calculation."],
     "Real rate = nominal − inflation. Negative when inflation exceeds the interest rate. Here −10%.",
     [[("k", "The real interest rate is the nominal interest rate minus inflation. It is negative when inflation is higher than the interest rate, so 40% − 50% gives −10%."), ("n", "This means borrowers gain in real terms because the value of their debt falls, and savers lose.")]]),
  eq(P("s25_21", "1(e)"), "6 marks", "Assess whether a central bank setting an inflation target as part of its monetary policy is likely to be helpful for its economy.",
     ["Analysis (up to 4): possibly helpful, because it helps to create and maintain stability and confidence at a time of significant price increases, informing consumers and firms that action will be taken to stop inflation becoming too high, and it can influence inflation expectations; if these stay stable, it may help to prevent a wage-price spiral (up to 3); possibly unhelpful, because the bank may not be willing to take the measures needed to keep inflation at the target, knowing there is a delicate balance between holding inflation close to a target and the risk of an economic downturn (up to 3).",
      "Evaluation (up to 2): relevant evaluation, for example in relation to the particular target adopted, and a reserved mark for a conclusion on whether it is helpful."],
     "Helpful: confidence, expectations, no wage-price spiral. Unhelpful: bank may not act; target may risk a downturn. Judge: credibility decides.",
     [[("n", "An inflation target could help by giving consumers and firms confidence that the central bank will act to stop prices rising too quickly, which keeps inflation expectations stable and may prevent a wage-price spiral. But the target may not help if the bank is reluctant to raise interest rates enough, because that could cause a slowdown and higher unemployment.")], [("e", "The target is likely to be helpful if the central bank is credible and independent, and if the target level is realistic. Its benefit depends on whether the bank is willing to meet it at the cost of lower growth.")]])
  ],
  )

tips = tips_html(
  [("Name the three tools.", "Interest rates, money supply, credit regulation."),
   ("Explain the transmission.", "Rate change, borrowing and saving, C and I, AD."),
   ("Use real rates.", "Nominal minus inflation."),
   ("Say expansionary or contractionary.", "Cut or loosen versus raise or tighten."),
   ("Who gains and loses.", "Savers versus borrowers."),
   ("Mention the exchange rate.", "Interest rates change hot money and net exports."),
   ("Know the central bank's role.", "Independent, inflation target, credibility.")],
  [("Monetary policy", "Monetary policy uses interest rates, the money supply and credit regulation."),
   ("Base rate", "The base rate is the central bank's policy interest rate."),
   ("Quantitative easing", "Quantitative easing is the creation of money to buy bonds and raise the money supply."),
   ("Credit regulation", "Credit regulation is the set of rules governing how banks lend."),
   ("Real interest rate", "The real interest rate is the nominal interest rate minus inflation.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + ADASJS + CHAINJS + '''
$("#pic1").innerHTML = (() => {
  const B = [["Interest rates", "The base rate and the rates that follow it", 30, "f1"], ["Money supply", "Open market operations and QE", 270, "f2"], ["Credit regulation", "Rules on bank lending", 510, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 20, 220, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 55, n, "lbl bd", { "text-anchor": "middle", style: "font-size:18px" }) + SV.text(x + 110, 82, d, "sm", { "text-anchor": "middle" }); });
  o += SV.text(380, 142, "All three change the cost and availability of credit, so spending and AD change", "sm", { "text-anchor": "middle" });
  return `<svg viewBox="0 0 760 160" role="img" aria-label="The three tools of monetary policy">${o}</svg>`;
})();
chainStep("#stT", "A cut in the base rate", ["The central bank cuts the base rate", "Commercial banks cut mortgage and loan rates; saving returns fall", "Borrowing is cheaper and saving less attractive", "Consumption and investment rise; asset prices rise", "The currency may fall, raising net exports; AD shifts right"], [
  "<b>Expansionary monetary policy</b> begins with the base rate.", "<b>Pass-through</b> to the rates households and firms face.", "<b>Incentives change:</b> spend and invest rather than save.", "<b>Components of AD rise</b> and wealth effects add to spending.", "<b>AD shifts right</b>, with net exports helped by a weaker currency."]);
chainStep("#stQ", "Quantitative easing", ["Interest rates are already close to zero", "The central bank creates money and buys government bonds", "Bond prices rise, so long-term interest rates fall", "Banks and investors have more money to lend and invest", "Spending and AD rise, if people borrow and spend"], [
  "<b>The usual tool is exhausted</b> at the zero bound.", "<b>Open market purchases</b> put money into the banking system.", "<b>Lower long-term rates</b> make borrowing cheaper.", "<b>More credit</b> is available.", "<b>The effect depends</b> on confidence and the willingness to borrow."]);
chainStep("#stC", "Tightening credit regulation", ["The central bank raises deposit and capital requirements", "Banks lend less and check borrowers more strictly", "Households find it harder to borrow, especially for housing", "Spending and house prices rise more slowly", "AD grows more slowly, reducing inflationary pressure"], [
  "<b>Contractionary credit regulation.</b>", "<b>Credit supply</b> falls.", "<b>Borrowing</b> becomes harder, even at the same interest rate.", "<b>House purchases</b> slow.", "<b>AD growth falls</b> without changing the base rate."]);

/* ---------- Lab 1 ---------- */
function labM() {
  if (!["rt", "mg", "sv"].every((i) => $("#" + i))) return;
  const r = +$("#rt").value / 10, mg = +$("#mg").value, sv = +$("#sv").value, mi = (mg * r) / 100 / 12, si = (sv * r) / 100 * 0.5, base = (mg * 4) / 100 / 12, bs = (sv * 4) / 100 * 0.5, net = (si - bs) / 12 - (mi - base);
  $("#r1").textContent = "$" + Lib.fmtN(mi, 0); $("#r2").textContent = "$" + Lib.fmtN(si, 0); $("#r3").textContent = (net >= 0 ? "+" : "−") + "$" + Lib.fmtN(Math.abs(net), 0);
  $("#rv").textContent = `At a rate of ${Lib.fmtN(r, 1)}% the monthly mortgage interest on $${Lib.fmtN(mg, 0)} is $${Lib.fmtN(mi, 0)}, compared with $${Lib.fmtN(base, 0)} at 4%. Savings earn about half the base rate here ($${Lib.fmtN(si, 0)} a year). The household's monthly budget is ${net >= 0 ? "better" : "worse"} by $${Lib.fmtN(Math.abs(net), 0)}. ${net < 0 ? "A rate rise reduces the spending power of borrowers, which is how it reduces AD." : net > 0 ? "A rate cut raises the spending power of borrowers." : ""}`;
  const mx = Math.max(mi, si / 12, 1), W = (v) => (v / mx) * 250, bar = (y, l, v, c) => SV.text(10, y + 15, l, "sm") + SV.rect(150, y, Math.max(2, W(v)), 24, c, op(0.7)) + SV.text(156 + W(v), y + 17, "$" + Lib.fmtN(v, 0), "lbl bd");
  $("#labA").innerHTML = bar(40, "Mortgage interest / month", mi, "f3") + bar(100, "Savings interest / month", si / 12, "f1");
}
Lib.slider($("#g1"), { id: "rt", label: "Base rate, % × 10 ", min: 10, max: 100, step: 5, value: 40, fmt: (v) => Lib.fmtN(v / 10, 1) + "%", onInput: labM });
Lib.slider($("#g2"), { id: "mg", label: "Variable-rate mortgage, $ ", min: 50000, max: 400000, step: 25000, value: 200000, fmt: (v) => Lib.fmtN(v, 0), onInput: labM });
Lib.slider($("#g3"), { id: "sv", label: "Savings, $ ", min: 0, max: 100000, step: 5000, value: 20000, fmt: (v) => Lib.fmtN(v, 0), onInput: labM });
labM();

/* ---------- Lab 2 ---------- */
function labI() {
  if (!["nm", "fl"].every((i) => $("#" + i))) return;
  const n = +$("#nm").value, f = +$("#fl").value, r = n - f;
  $("#t1").textContent = (r >= 0 ? "+" : "") + Lib.fmtN(r, 1) + "%"; $("#t2").textContent = r < 0 ? "Very attractive" : r < 2 ? "Moderate" : "Discouraged"; $("#t3").textContent = r < 0 ? "Savers lose" : r < 2 ? "Modest reward" : "Rewarded";
  $("#tv").textContent = `A nominal rate of ${n}% with inflation of ${f}% gives a real rate of ${Lib.fmtN(r, 1)}%. ${r < 0 ? "Borrowing costs less than inflation: the real value of debt falls, so borrowing is attractive and savers lose in real terms." : r < 2 ? "A low real rate keeps borrowing fairly cheap." : "A high real rate makes borrowing costly and saving rewarding, which reduces spending."}`;
  const Y = (v) => 120 - v * 8; let o = SV.line(40, 120, 400, 120) + SV.line(40, 20, 40, 190);
  [["Nominal rate", n, "f1"], ["Inflation", f, "f3"], ["Real rate", r, r >= 0 ? "f2" : "f3"]].forEach(([l, v, c], i) => (o += SV.rect(70 + i * 110, v >= 0 ? Y(v) : 120, 80, Math.abs(Y(v) - 120), c, op(0.65)) + SV.text(110 + i * 110, 185, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, v >= 0 ? Y(v) - 6 : 120 + Math.abs(Y(v) - 120) + 14, Lib.fmtN(v, 1) + "%", "lbl bd", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "nm", label: "Nominal interest rate, % ", min: 0, max: 12, step: 0.5, value: 4, fmt: (v) => v + "%", onInput: labI });
Lib.slider($("#g5"), { id: "fl", label: "Inflation rate, % ", min: 0, max: 12, step: 0.5, value: 6, fmt: (v) => v + "%", onInput: labI });
labI();

/* ---------- Lab 3 ---------- */
chooser("h", [
  ["Interest rates", "A change in the base rate alters borrowing costs and the return on saving", "Cut: expansionary", "Responses may be weak if confidence is low; time lags", 5],
  ["Quantitative easing", "The central bank buys bonds, raising the money supply and lowering long-term rates", "Expansionary", "Banks may not lend; may raise asset prices more than spending", 3],
  ["Open market sales of bonds", "The central bank sells bonds, taking money out of the banking system", "Contractionary", "Raises yields; effects on spending slow", 3],
  ["Credit regulation (looser)", "Easier lending rules let more people borrow", "Expansionary", "Risk of excess lending and asset bubbles", 4],
  ["Credit regulation (tighter)", "Stricter rules limit borrowing", "Contractionary", "May reduce lending to good borrowers", 4],
  ["Inflation target", "Anchors expectations of future inflation", "Neither (framework)", "Only works if the bank is credible and willing to act", 3]
], (it) => `${it[0]}: ${it[1].toLowerCase()}. It is ${it[2].toLowerCase()}. Main drawback: ${it[3].toLowerCase()}.`, "Importance as a tool");
''' + CLASSIFY("cl1", "Which tool of monetary policy is it?", ["Interest rates", "Money supply", "Credit regulation"],
  [("Raising the base rate", 0), ("Quantitative easing", 1), ("Lowering the deposit needed for a mortgage", 2), ("Selling government bonds to banks", 1), ("Cutting the rate at which the central bank lends to banks", 0), ("Higher capital requirements for banks", 2)],
  "Interest rates: the price of money. Money supply: the amount of money. Credit regulation: rules on lending.") + CLASSIFY("cl2", "Expansionary or contractionary monetary policy?", ["Expansionary", "Contractionary"],
  [("A cut in the base rate", 0), ("A rise in the base rate", 1), ("Quantitative easing", 0), ("Reducing the money supply", 1), ("Looser rules on mortgage lending", 0), ("Tighter credit regulation for banks", 1), ("Lowering interest rates to end deflation", 0), ("Raising rates to reduce inflation", 1)],
  "Expansionary: cheaper, easier credit. Contractionary: dearer, tighter credit.") + ORDER(
  "Put the effect of a rise in interest rates in order.",
  ["The central bank raises the base rate", "Banks raise mortgage and loan rates", "Borrowing becomes dearer and saving more attractive", "Consumption and investment fall", "AD shifts to the left"],
  "Higher rates reduce spending and AD.") + MATCH([
  ["Monetary policy", "Use of interest rates, money supply and credit regulation"],
  ["Base rate", "The central bank's policy interest rate"],
  ["Quantitative easing", "Creating money to buy bonds and raise the money supply"],
  ["Credit regulation", "Rules on how banks lend"],
  ["Real interest rate", "Nominal rate minus inflation"],
  ["Inflation target", "A published goal for the inflation rate"]]) + CALC([
  {"q": "The nominal interest rate is 5% and inflation 3%. What is the real interest rate (%)?", "a": 2, "unit": "%", "tol": 0.1, "hint": "5 − 3.", "sol": "<b>2%</b>."},
  {"q": "The nominal rate is 3% and inflation 7%. What is the real interest rate (%)?", "a": -4, "unit": "%", "tol": 0.1, "hint": "3 − 7.", "sol": "<b>−4%</b>."},
  {"q": "A firm borrows $200,000 at 6%. What is the yearly interest ($)?", "a": 12000, "unit": "$", "tol": 1, "hint": "0.06 × 200,000.", "sol": "<b>$12,000</b>."},
  {"q": "The rate rises to 8%. What is the new yearly interest ($)?", "a": 16000, "unit": "$", "tol": 1, "hint": "0.08 × 200,000.", "sol": "<b>$16,000</b>."},
  {"q": "By what % has the cost of borrowing risen?", "a": 33.3, "unit": "%", "tol": 0.3, "hint": "4,000 ÷ 12,000.", "sol": "<b>33.3%</b>."}]) + MCQ([
  ("Monetary policy uses:", ["Interest rates, money supply and credit regulation", "Taxes and spending", "Training schemes", "Tariffs"], 0, "Not fiscal."),
  ("A rise in the base rate will usually:", ["Make borrowing dearer", "Make borrowing cheaper", "Raise investment", "Lower saving"], 0, "The cost of credit rises."),
  ("Quantitative easing is:", ["Expansionary", "Contractionary", "A tax", "A subsidy"], 0, "Raises the money supply."),
  ("Credit regulation is:", ["Rules on how banks lend", "A tax on loans", "The base rate", "A subsidy to borrowers"], 0, "Controls access to credit."),
  ("A negative real interest rate means:", ["Inflation is above the nominal rate", "The nominal rate is zero", "Savers gain", "Borrowers lose"], 0, "Borrowers gain, savers lose in real terms.")
], "qz1") + CARDS([
  ("Tools", "Rates, money supply, credit rules."),
  ("Base rate", "Central bank's policy rate."),
  ("QE", "Creates money for bonds."),
  ("Credit rules", "Looser = expansionary."),
  ("Real rate", "Nominal − inflation."),
  ("Pass-through", "Base rate feeds into loan and saving rates."),
  ("Inflation target", "Anchors expectations."),
  ("Central bank", "Often independent.")]) + MCQ(mc_exam)

build("as54", "as-monetary-policy", "Monetary Policy: Tools and the Central Bank", EY,
  "5.3.1 to 5.3.2: the central bank, interest rates, the money supply, credit regulation and inflation targets, and how each changes borrowing and spending. Animated chains, labs, drills and past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
