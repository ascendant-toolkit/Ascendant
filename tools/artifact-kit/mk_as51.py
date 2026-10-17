"""AS syllabus 5.1 and 5.2.1-5.2.3 Macroeconomic objectives, the government budget and the national debt. Run: python3 tools/artifact-kit/mk_as51.py"""
from asx import *
EY = EYAS("5.1 and 5.2.1 to 5.2.3")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Governments use macroeconomic policy to pursue objectives such as <b>price stability</b> (a low, stable rate of inflation), <b>low unemployment</b> and <b>economic growth</b>, and AS Level does not require knowledge of policy conflicts and trade-offs. The <b class="kw">government budget</b> is the annual statement of the government's <b>revenue</b> (mainly taxes) and <b>expenditure</b>; if spending exceeds revenue there is a <b class="kw">budget deficit</b>, if revenue exceeds spending a <b class="kw">budget surplus</b>, and if they are equal a <b>balanced budget</b>. The <b class="kw">national debt</b> is the <b>total stock</b> of money the government owes, built up from past deficits, while the deficit is a <b>flow</b> within a single year. A large debt has <b>interest costs</b> and an opportunity cost, but it matters most relative to the size of the economy (the <b>debt to GDP ratio</b>) and who owns it.</p></div>

  <h2>1 · Macroeconomic objectives (5.1.1)</h2>
  <div class="tw"><table class="t">
    <tr><th>Objective</th><th>What it means</th><th>Typical measure</th></tr>
    <tr><td><b>Price stability</b></td><td>Avoiding high inflation and deflation, often a low target such as 2%</td><td>Consumer price index</td></tr>
    <tr><td><b>Low unemployment</b></td><td>Keeping as many people as possible in work</td><td>Unemployment rate</td></tr>
    <tr><td><b>Economic growth</b></td><td>Raising real output over time</td><td>Annual change in real GDP</td></tr>
  </table></div>
  <ul>
    <li>The government can use <b>fiscal policy</b> (taxes and spending), <b>monetary policy</b> (interest rates, money supply, credit rules) and <b>supply-side policy</b> to pursue them.</li>
    <li>Policies may be <b>expansionary</b> (to raise AD and output) or <b>contractionary</b> (to reduce AD and inflation).</li>
  </ul>

  <h2>2 · The government budget (5.2.1 to 5.2.2)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Revenue:</b> income tax, corporation tax, sales taxes (VAT), duties, charges and sales of assets. <b>Expenditure:</b> current spending (wages of public workers, benefits) and capital spending (roads, hospitals).</li>
    <li><b>Budget deficit</b> = spending − revenue when spending is greater; the government <b>borrows</b> the difference.</li>
    <li><b>Budget surplus</b> = revenue − spending when revenue is greater; it can be used to <b>repay debt</b>.</li>
    <li><b>Balanced budget:</b> revenue equals spending.</li>
    <li>A deficit tends to <b>increase AD</b> (expansionary); a surplus tends to <b>reduce</b> it (contractionary). Deficits <b>rise in recessions</b> because tax revenue falls and benefit spending rises.</li>
  </ul>

  <h2>3 · The national debt (5.2.3)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Flow</th><th>Stock</th></tr>
    <tr><td><b>Budget deficit</b>: borrowing in one year</td><td><b>National debt</b>: all outstanding government borrowing</td></tr>
    <tr><td>Deficits <b>add</b> to the debt</td><td>Surpluses <b>reduce</b> the debt</td></tr>
  </table></div>
  <ul>
    <li><b>Significance of a large debt:</b> <b>interest payments</b> take money from other spending (opportunity cost); a burden on <b>future taxpayers</b>; possible <b>crowding out</b> of private investment if the government borrows heavily; lenders may lose confidence and demand <b>higher interest rates</b>.</li>
    <li><b>Why it may be less serious:</b> if the debt is owed to domestic residents it is a transfer within the country; the debt may have financed <b>productive investment</b>; what matters is the <b>debt relative to GDP</b> and whether growth is faster than the interest rate.</li>
    <li>The debt can be reduced by running <b>surpluses</b>, raising taxes, cutting spending, or <b>growing</b> the economy.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Do not mix up the <b>deficit</b> (a flow, one year) and the <b>debt</b> (a stock, accumulated). Avoid confusing a budget deficit with a <b>current account</b> deficit: the question may state this is not about trade.</div>
'''

watch = '''
  <h2>1 · Deficit, balance or surplus</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stB"></div>
  <h2>2 · Deficits build up the national debt</h2>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · The budget balance</h2>
  <p>Set revenue and spending ($bn) and see the balance and the extra debt.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Budget balance</small><strong id="r1"></strong></div><div><small>Position</small><strong id="r2"></strong></div><div><small>National debt after the year</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of revenue and expenditure with the balance"></svg></div></div></div>

  <h2>Lab 2 · The debt to GDP ratio</h2>
  <p>Debt matters relative to the size of the economy. Set the yearly deficit and the growth of nominal GDP and watch the ratio over ten years (starting at 60%).</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Debt ratio, year 10</small><strong id="t1"></strong></div><div><small>Direction</small><strong id="t2"></strong></div><div><small>Stable ratio needs deficit of</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Debt to GDP ratio over ten years"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Flow or stock?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put how a deficit becomes debt in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A recession and the deficit", "When the economy shrinks, fewer people pay income tax and VAT, and more claim benefits. The budget moves into deficit even if policy has not changed, which helps support demand.", "why deficits rise in recessions.") +
rw("Paying interest on the debt", "A government with a large debt spends a big share of revenue on interest. That money cannot be used for schools or hospitals, so there is an opportunity cost.", "the opportunity cost of the national debt.") +
rw("Debt and GDP", "A debt of $2,000bn sounds large, but in an economy with GDP of $4,000bn it is 50% of GDP. A country with the same debt and GDP of $1,000bn has a ratio of 200%, which is much harder to manage.", "why the ratio matters more than the size.") +
rw("Borrowing to invest", "A government borrows to build railways and broadband. The debt rises, but if the investment raises productivity and growth, future tax revenue may rise enough to pay for it.", "debt that finances productive spending.")
)

mc_exam = [
  mcq("m22_12", 14, "To improve its financial position, a government decided to reduce expenditure on investment in the public sector. There was not a fall in economic growth. What was the most likely effect of the government's action?", ["An original budget deficit was reduced", "An original budget surplus was reduced", "Consumer expenditure decreased", "Public sector productivity decreased"], 0, "Lower spending with unchanged growth (and revenue) reduces a deficit."),
  mcq("m24_12", 20, "A government has a balanced budget. It decides to increase its spending by 10%. Which increase in government revenue would produce a budget surplus?", ["−10%", "0%", "+10%", "+20%"], 3, "With a balanced budget, revenue must rise by more than the 10% rise in spending to create a surplus."),
  mcq("s20_12", 28, "Which combination correctly classifies an expansionary fiscal measure and its impact on a budget deficit? (fiscal policy, budget deficit)", ["increased quantitative easing, unchanged", "increased welfare spending, increased", "lower income tax, reduced", "lower interest rates, unchanged"], 1, "Welfare spending is a fiscal measure that raises the deficit. Quantitative easing and interest rates are monetary policy, and lower income tax would raise the deficit.")
]

exam = exam_page("macroeconomic objectives, the budget and the national debt",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The budget and national debt appear as an 8 mark part (surplus versus deficit) and a 12 mark discussion on balancing the budget in most years, with short definitions. Reworded past questions are below, with three Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "1", "May/June 2025 (21) Q5(a)"), ("Essay parts, 12 marks", "2", "Oct/Nov 2023 (21) Q4(b); Oct/Nov 2024 (22) Q5(b)"), ("Data response, 2 marks", "1", "Oct/Nov 2020 (21) Q1(d)(i)"), ("Multiple choice (Paper 1)", "3 shown below", "2020 to 2024")],
  [
  eq(P("s25_21", "5(a)"), "8 marks", "Explain the difference between a budget surplus and a budget deficit and consider the extent to which a budget surplus is better than a budget deficit.",
     ["Knowledge (up to 3): understanding of a government budget (1), a budget surplus (1) and a budget deficit (1).",
      "Analysis (up to 3): the benefits and limitations of a budget surplus (up to 2) and of a budget deficit (up to 2). If only a surplus or only a deficit is considered the maximum is 2, with no evaluation marks. The question is not about the current account of the balance of payments.",
      "Evaluation (up to 2): a valid judgement on the extent to which a surplus is better than a deficit (1) and a conclusion (1)."],
     "Budget: revenue and spending. Surplus: revenue greater. Deficit: spending greater. Weigh benefits and limits of each. Judge: depends on the economy.",
     [[("k", "The government budget shows planned revenue and spending. A budget surplus is when revenue exceeds spending, and a budget deficit is when spending exceeds revenue, which has to be financed by borrowing.")], [("n", "A surplus allows the government to repay debt and reduces interest payments, but it takes demand out of the economy and may mean cuts to services or higher taxes. A deficit can boost AD and support output and jobs, especially in a recession, and can finance investment, but it adds to the national debt and interest costs, and may crowd out private investment.")], [("e", "A surplus is not always better. In a boom a surplus can help control inflation and reduce debt, but in a recession a deficit is probably more appropriate to support demand. The right position depends on the stage of the economic cycle.")]]),
  eq(P("w23_21", "4(b)"), "12 marks", "Assess whether a government should always aim to balance its budget rather than have a budget surplus or a budget deficit.",
     ["Analysis (up to 8): the arguments for balancing the budget, such as avoiding debt and interest costs, fairness to future taxpayers and keeping confidence of lenders (up to 4); the arguments for a deficit or surplus, such as supporting AD and growth in a recession with a deficit, investing in infrastructure, or repaying debt and reducing inflationary pressure with a surplus (up to 4).",
      "Evaluation (up to 4): a judgement on whether a balanced budget should always be the aim, taking account of the stage of the economic cycle, the level of debt and the purpose of spending, with a conclusion."],
     "For balance: debt, interest, future taxpayers. Against: deficit in recession, borrowing to invest; surplus in boom. Judge: depends on the cycle and debt level.",
     [[("n", "A balanced budget avoids adding to the national debt, so there are no growing interest payments, future taxpayers are not burdened and lenders stay confident. But always balancing the budget would mean cutting spending or raising taxes in a recession, when revenue falls, which would reduce AD and deepen the downturn. A deficit used to invest in infrastructure can raise future growth, while a surplus in a boom can control inflation and repay debt.")], [("e", "A government should not always aim for balance. A deficit is justified in a recession or to fund productive investment, provided the debt is sustainable relative to GDP, while a surplus is more suitable in a boom. Over the cycle the budget may roughly balance.")]]),
  eq(P("w20_21", "1(d)"), "2 marks", "Explain what is meant by a 'budget deficit'.",
     ["A budget shows the details of government expenditure and government revenue (1).", "A budget deficit is the amount by which government expenditure exceeds government revenue (1)."],
     "Budget: spending and revenue. Deficit: spending exceeds revenue.",
     [[("k", "A government budget sets out planned revenue and expenditure. A budget deficit is when government spending exceeds revenue in a year, so the government must borrow the difference.")]])
  ],
  )

tips = tips_html(
  [("Know the three objectives.", "Price stability, low unemployment, growth."),
   ("Deficit is a flow; debt is a stock.", "Deficits add to the debt."),
   ("Define the budget.", "Planned revenue and spending."),
   ("Surplus is not always better.", "It depends on the economic cycle."),
   ("Mention the debt ratio.", "Debt relative to GDP."),
   ("Say what deficits do to AD.", "A deficit is expansionary; a surplus is contractionary."),
   ("Do not mix with the current account.", "Budget deficit ≠ trade deficit.")],
  [("Budget", "The government budget shows planned revenue and spending."),
   ("Deficit", "A budget deficit means spending exceeds revenue."),
   ("Surplus", "A budget surplus means revenue exceeds spending."),
   ("National debt", "The national debt is the total stock of government borrowing."),
   ("Judge", "A deficit may be appropriate in a recession.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = '''
/* ---------- budget bars ---------- */
function bdDraw(s) {
  const Y = (v) => 250 - v * 1.7; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "$bn", "sm");
  const rev = 100, spend = s.e; o += SV.rect(180, Y(rev), 120, 250 - Y(rev), "f2", op(0.65)) + SV.text(240, 270, "Revenue", "sm", { "text-anchor": "middle" }) + SV.text(240, Y(rev) - 6, rev, "lbl bd", { "text-anchor": "middle" });
  o += SV.rect(400, Y(spend), 120, 250 - Y(spend), "f3", op(0.65)) + SV.text(460, 270, "Expenditure", "sm", { "text-anchor": "middle" }) + SV.text(460, Y(spend) - 6, Lib.fmtN(spend, 0), "lbl bd", { "text-anchor": "middle" });
  const b = rev - spend; o += SV.text(380, 60, Math.abs(b) < 0.5 ? "Balanced budget" : b < 0 ? "Budget deficit of " + Lib.fmtN(-b, 0) + ": the government borrows" : "Budget surplus of " + Lib.fmtN(b, 0) + ": it can repay debt", "lbl bd", { "text-anchor": "middle", style: "fill:var(--accent)" });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Revenue of 100 against expenditure of 120 gives a budget deficit">${bdDraw({ e: 120 })}</svg>`;
Lib.stepper($("#stB"), { w: 760, h: 290, label: "Revenue against expenditure", base: { e: 100 }, draw: bdDraw, tween: 900, dwell: 5200, steps: [
  { cap: "<b>Balanced budget.</b> Revenue ($100bn) equals expenditure ($100bn).", s: { e: 100 } },
  { cap: "<b>Budget deficit.</b> Spending rises to $120bn. The $20bn gap is the deficit and must be borrowed. It adds to AD.", s: { e: 120 } },
  { cap: "<b>Budget surplus.</b> Spending falls to $85bn. The $15bn surplus can repay debt, but takes demand out of the economy.", s: { e: 85 } },
] });

/* ---------- debt path ---------- */
const DEF = [20, 25, 15, 10, -5, -10, 5, 10];
function dbDraw(s) {
  const n = Math.round(s.t); let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "$bn", "sm"), debt = 100, pts = [];
  o += SV.text(60, 270, "", "sm");
  for (let i = 0; i <= 8; i++) { if (i > 0) debt += DEF[i - 1]; if (i <= n) { const x = 100 + i * 70, h = debt * 1.4; o += SV.rect(x - 22, 250 - h, 44, h, "f1", op(0.5)) + SV.text(x, 244 - h, Lib.fmtN(debt, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x, 268, i === 0 ? "Start" : "Y" + i, "sm", { "text-anchor": "middle" }); if (i > 0) o += SV.text(x, 230 - h, (DEF[i - 1] > 0 ? "+" : "") + DEF[i - 1], "sm", { "text-anchor": "middle", style: DEF[i - 1] > 0 ? "fill:var(--bad)" : "fill:var(--good)" }); } }
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="National debt rising with deficits and falling with surpluses">${dbDraw({ t: 8 })}</svg>`;
Lib.stepper($("#stD"), { w: 760, h: 290, label: "The national debt as deficits and surpluses accumulate", base: { t: 0 }, draw: dbDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>Start.</b> The national debt is $100bn: the stock of past borrowing.", s: { t: 0 } },
  { cap: "<b>Deficits add to the debt.</b> Deficits of $20bn, $25bn, $15bn and $10bn take it to $170bn.", s: { t: 4 } },
  { cap: "<b>Surpluses reduce it.</b> Surpluses of $5bn and $10bn pay the debt down to $155bn.", s: { t: 6 } },
  { cap: "<b>Deficits resume,</b> raising it again to $170bn. The debt is the accumulated total of all the yearly flows.", s: { t: 8 } },
] });

/* ---------- Lab 1 ---------- */
function labB() {
  if (!["rvn", "spd", "dbt"].every((i) => $("#" + i))) return;
  const r = +$("#rvn").value, e = +$("#spd").value, d = +$("#dbt").value, b = r - e, nd = d - b;
  $("#r1").textContent = (b >= 0 ? "+" : "−") + "$" + Math.abs(b) + "bn"; $("#r2").textContent = b > 0 ? "Surplus" : b < 0 ? "Deficit" : "Balanced"; $("#r3").textContent = "$" + nd + "bn";
  $("#rv").textContent = b === 0 ? `Revenue of $${r}bn equals spending of $${e}bn: a balanced budget, so the national debt is unchanged at $${d}bn.` : b < 0 ? `Spending ($${e}bn) exceeds revenue ($${r}bn) by $${-b}bn: a budget deficit, financed by borrowing. The national debt rises from $${d}bn to $${nd}bn.` : `Revenue ($${r}bn) exceeds spending ($${e}bn) by $${b}bn: a surplus, which can repay debt. The national debt falls from $${d}bn to $${nd}bn.`;
  const Y = (v) => 250 - v * 0.9; let o = SV.line(40, 250, 400, 250);
  [["Revenue", r, "f2"], ["Spending", e, "f3"]].forEach(([l, v, c], i) => (o += SV.rect(80 + i * 140, Y(v), 100, 250 - Y(v), c, op(0.65)) + SV.text(130 + i * 140, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(130 + i * 140, Y(v) - 6, "$" + v, "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "rvn", label: "Government revenue, $bn ", min: 60, max: 200, step: 5, value: 100, fmt: (v) => "$" + v, onInput: labB });
Lib.slider($("#g2"), { id: "spd", label: "Government spending, $bn ", min: 60, max: 200, step: 5, value: 115, fmt: (v) => "$" + v, onInput: labB });
Lib.slider($("#g3"), { id: "dbt", label: "National debt at start of year, $bn ", min: 100, max: 800, step: 50, value: 400, fmt: (v) => "$" + v, onInput: labB });
labB();

/* ---------- Lab 2 ---------- */
function labR() {
  if (!["df", "gn"].every((i) => $("#" + i))) return;
  const def = +$("#df").value, g = +$("#gn").value; let d = 60, pts = [d]; for (let i = 0; i < 10; i++) { d = (d + def) / (1 + g / 100); pts.push(d); }
  const stable = 60 * g / (100 + g) * 1;
  $("#t1").textContent = Lib.fmtN(d, 0) + "% of GDP"; $("#t2").textContent = d > 60.5 ? "Rising" : d < 59.5 ? "Falling" : "Stable"; $("#t3").textContent = Lib.fmtN(stable, 1) + "% of GDP";
  $("#tv").textContent = `With a deficit of ${def}% of GDP each year and nominal GDP growth of ${g}%, the debt ratio moves from 60% to ${Lib.fmtN(d, 0)}% in ten years. ${d > 61 ? "The ratio is rising, so interest costs may take a growing share of revenue." : d < 59 ? "The ratio is falling because the economy is growing faster than the debt." : "The ratio is roughly stable."} A deficit of about ${Lib.fmtN(stable, 1)}% of GDP would keep the ratio at 60% at this growth rate.`;
  const Y = (v) => 200 - v * 1.2; let o = SV.line(40, 200, 400, 200) + SV.line(40, 200, 40, 20) + SV.text(46, 16, "Debt, % of GDP", "sm"), p = ""; pts.forEach((v, i) => (p += (i ? " L" : "M") + (40 + i * 34) + "," + Y(v)));
  o += SV.path(p, "c3", { fill: "none", "stroke-width": 3 }) + SV.line(40, Y(60), 400, Y(60), "dash") + SV.text(398, Y(60) - 6, "60% start", "sm", { "text-anchor": "end" });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "df", label: "Budget deficit, % of GDP each year ", min: 0, max: 10, step: 1, value: 4, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g5"), { id: "gn", label: "Growth of nominal GDP, % per year ", min: 0, max: 8, step: 1, value: 4, fmt: (v) => v + "%", onInput: labR });
labR();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Flow or stock?", ["Flow (one year)", "Stock (accumulated)"],
  [("The budget deficit", 0), ("The national debt", 1), ("Government spending this year", 0), ("Total government borrowing outstanding", 1), ("Tax revenue in a year", 0), ("Debt as a share of GDP at the end of the year", 1), ("A budget surplus", 0), ("The debt built up over 20 years", 1)],
  "The deficit and surplus are annual flows. The national debt is the accumulated stock.") + MATCH([
  ["Budget deficit", "Spending exceeds revenue in a year"],
  ["Budget surplus", "Revenue exceeds spending in a year"],
  ["National debt", "Total stock of government borrowing"],
  ["Debt to GDP ratio", "The debt relative to the size of the economy"],
  ["Balanced budget", "Revenue equals spending"],
  ["Price stability", "A low, stable rate of inflation"]]) + ORDER(
  "Put how a deficit becomes debt in order.",
  ["Government spending exceeds revenue", "A budget deficit arises", "The government borrows to cover it", "The national debt increases", "Interest must be paid on the larger debt"],
  "Deficits add to debt, and debt costs interest.") + CALC([
  {"q": "Revenue is $180bn and spending $200bn. What is the budget balance (deficit as a negative, $bn)?", "a": -20, "unit": "$bn", "tol": 0.5, "hint": "180 − 200.", "sol": "<b>−$20bn</b>, a deficit."},
  {"q": "The national debt was $500bn. After that deficit, what is it ($bn)?", "a": 520, "unit": "$bn", "tol": 0.5, "hint": "500 + 20.", "sol": "<b>$520bn</b>."},
  {"q": "GDP is $1,000bn. What is the debt to GDP ratio (%)?", "a": 52, "unit": "%", "tol": 0.2, "hint": "520 ÷ 1,000.", "sol": "<b>52%</b>."},
  {"q": "The government pays 4% interest on the $520bn debt. How much is the interest ($bn)?", "a": 20.8, "unit": "$bn", "tol": 0.1, "hint": "0.04 × 520.", "sol": "<b>$20.8bn</b>."}]) + MCQ([
  ("A budget deficit means:", ["Government spending exceeds revenue", "Revenue exceeds spending", "Exports exceed imports", "Imports exceed exports"], 0, "Government budget, not trade."),
  ("The national debt is:", ["The total stock of government borrowing", "The annual deficit", "A trade deficit", "Household debt"], 0, "Accumulated."),
  ("A deficit usually:", ["Raises AD", "Lowers AD", "Reduces debt", "Cuts unemployment only"], 0, "Expansionary."),
  ("A government runs a surplus. The national debt:", ["Falls", "Rises", "Is unchanged", "Doubles"], 0, "Surpluses reduce debt."),
  ("Which is an objective of macroeconomic policy?", ["Price stability", "A trade deficit", "Higher debt", "Lower growth"], 0, "Stable prices.")
], "qz1") + CARDS([
  ("Budget", "Planned revenue and spending."),
  ("Deficit", "Spending > revenue."),
  ("Surplus", "Revenue > spending."),
  ("Debt", "Accumulated borrowing."),
  ("Deficit adds", "To the debt."),
  ("Debt ratio", "Debt ÷ GDP."),
  ("Cost of debt", "Interest, opportunity cost."),
  ("Objectives", "Prices, jobs, growth.")]) + MCQ(mc_exam)

build("as51", "as-objectives-budget-national-debt", "Macroeconomic Objectives, the Budget and the National Debt", EY,
  "5.1 and 5.2.1 to 5.2.3: macroeconomic policy objectives, the government budget, budget deficits and surpluses, and the national debt. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
