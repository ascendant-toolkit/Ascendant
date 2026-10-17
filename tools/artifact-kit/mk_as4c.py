"""AS syllabus 4.6.5 Consequences of inflation. Run: python3 tools/artifact-kit/mk_as4c.py"""
from asx import *
EY = EYAS("4.6.5")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Inflation redistributes income and wealth: <b>borrowers and owners of real assets gain</b> because debts fall in real terms, while <b>savers, lenders and people on fixed incomes lose</b> purchasing power. It also imposes costs: <b>menu costs</b> (changing prices), <b>shoe leather costs</b> (searching for the best return), <b>uncertainty</b> that discourages investment, and a loss of <b>international competitiveness</b> if domestic inflation is higher than abroad, which can worsen the <b>current account</b> and push the <b>exchange rate</b> down. <b>High and accelerating inflation</b> (hyperinflation) can destroy the functions of money and cause economic collapse, while <b>deflation</b> can be harmful too, as consumers delay spending and the real burden of debt rises. A <b>low, stable rate</b> of inflation is usually considered acceptable; the severity of the consequences depends on how <b>high</b> the rate is, whether it was <b>expected</b> and who is affected.</p></div>

  <h2>1 · Domestic consequences (4.6.5)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Consequence</th><th>Explanation</th></tr>
    <tr><td><b>Loss of purchasing power</b></td><td>Money buys less; people on <b>fixed incomes</b> and <b>savers</b> (if interest rates are below inflation) lose in real terms</td></tr>
    <tr><td><b>Redistribution</b></td><td>Borrowers gain (debts shrink in real terms) and lenders lose; workers with strong bargaining power gain real pay, others lose</td></tr>
    <tr><td><b>Menu costs</b></td><td>The cost to firms of changing prices: reprinting menus, catalogues, labels</td></tr>
    <tr><td><b>Shoe leather costs</b></td><td>Time and effort spent protecting the value of money, such as moving funds to find better returns</td></tr>
    <tr><td><b>Uncertainty and lower investment</b></td><td>Firms cannot predict future costs and prices, so they invest less; planning becomes harder</td></tr>
    <tr><td><b>Wage-price spiral</b></td><td>Inflation expectations can lead to wage claims that add to costs and prices</td></tr>
  </table></div>

  <h2>2 · External consequences and extreme cases</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Competitiveness:</b> if domestic inflation is higher than in trading partners, exports become <b>dearer</b> and imports <b>cheaper</b>, so the <b>current account</b> may worsen and the exchange rate may fall.</li>
    <li><b>Hyperinflation:</b> prices rise so fast that money stops working as a <b>medium of exchange</b> and a <b>store of value</b>; people switch to barter or foreign currencies and the economy can collapse.</li>
    <li><b>Deflation:</b> falling prices make consumers delay purchases, raise the <b>real value of debt</b>, and can cause a spiral of falling spending and output.</li>
    <li><b>Possible benefits:</b> mild inflation can reduce the real burden of debt, raise profit margins, and allow real wages to adjust in a recession without cutting money wages.</li>
    <li><b>Is it always negative?</b> No: it depends on the rate, whether it was expected, who gains or loses, and how it compares with other countries. <b>Unexpected</b> and <b>high</b> inflation is the most damaging.</li>
  </ul>

  <h2>3 · Worked examples: who gains and who loses?</h2>
  <div class="tw"><table class="t">
    <tr><th>Case</th><th>Working</th><th>Result</th></tr>
    <tr><td><b>A saver</b>: $10,000 earns 2% interest while inflation is 5%</td><td>Real interest rate = 2% − 5% = −3%</td><td>Real value falls by about $300: the saver loses purchasing power</td></tr>
    <tr><td><b>A borrower</b>: owes a fixed $100,000 and prices rise 10%</td><td>Real value of the debt = 100,000 ÷ 1.10</td><td>About $90,900: the debt is worth about $9,100 less in real terms, so the borrower gains</td></tr>
    <tr><td><b>A pensioner</b> on a fixed $12,000 pension, prices up 8%</td><td>Real pension = 12,000 ÷ 1.08</td><td>About $11,100: purchasing power falls by about $900</td></tr>
    <tr><td><b>A worker</b> with a 6% pay rise while prices rise 4%</td><td>Real pay rise ≈ 6% − 4%</td><td>+2% in real terms: gains</td></tr>
    <tr><td><b>A firm</b> whose prices rise 8% while costs rise 5%</td><td>Margin gain ≈ 3 points</td><td>Profits rise</td></tr>
  </table></div>
  <ul>
    <li>Whether inflation gains or hurts depends on whether <b>incomes and interest rates keep up</b> with prices, and whether inflation was <b>expected</b>. Expected inflation can be built into wages and interest rates; <b>unexpected</b> inflation redistributes more.</li>
  </ul>

  <h2>4 · Costs of inflation explained</h2>
  <ul>
    <li><b>Menu costs:</b> the cost of changing prices, such as reprinting price lists, repricing items and updating systems. Larger when inflation is high and frequent.</li>
    <li><b>Shoe leather costs:</b> time and effort spent trying to keep the value of money, such as visiting several banks to find better rates or holding smaller amounts of cash.</li>
    <li><b>Uncertainty:</b> firms find it harder to forecast costs and revenues, so they invest less, which reduces future growth.</li>
    <li><b>Wage-price spiral:</b> expected inflation feeds into wage demands, raising costs and prices again.</li>
    <li><b>Loss of competitiveness:</b> if domestic prices rise faster than abroad, exports become dearer and imports cheaper. The current account may worsen and the exchange rate may fall, which in turn raises import prices.</li>
    <li><b>Distortion of signals:</b> when all prices are rising, it is harder to tell whether a particular price rise reflects scarcity or just general inflation.</li>
  </ul>

  <h2>5 · Internal and external effects compared</h2>
  <div class="tw"><table class="t">
    <tr><th>Internal (domestic) effects</th><th>External effects</th></tr>
    <tr><td>Redistribution of income and wealth</td><td>Falling price competitiveness of exports</td></tr>
    <tr><td>Menu and shoe leather costs</td><td>Rising demand for imports</td></tr>
    <tr><td>Uncertainty and lower investment</td><td>A worsening current account</td></tr>
    <tr><td>May stimulate output and profits if mild</td><td>A weaker currency and higher import prices</td></tr>
  </table></div>
  <ul>
    <li>Which is more serious depends on the economy: for a country that relies heavily on trade, <b>external</b> effects may matter most; for a large, less open economy, <b>internal</b> effects such as redistribution and uncertainty may matter more.</li>
  </ul>

  <h2>6 · Hyperinflation, deflation and disinflation</h2>
  <ul>
    <li><b>Hyperinflation:</b> extremely rapid price rises. Money fails as a <b>store of value</b> (it loses value daily) and as a <b>medium of exchange</b> (sellers refuse it), so people switch to barter or foreign currency. Savings are wiped out, and the economy can collapse. Zimbabwe abandoned its currency in 2008 and Venezuela suffered very high inflation.</li>
    <li><b>Disinflation</b> (a lower rate of inflation) still leaves prices rising, so the problems of inflation continue, though they are smaller; disinflation caused by contractionary policy may cost jobs and output.</li>
    <li><b>Deflation:</b> delayed spending, a higher real burden of debt and falling profits can cause a spiral of falling output. It is generally more dangerous than mild inflation, especially if caused by falling AD.</li>
  </ul>

  <h2>7 · Are the consequences always negative?</h2>
  <ul>
    <li><b>Possible benefits:</b> profits may rise if prices rise by more than costs, which can encourage investment and employment; debts fall in real terms; and mild inflation lets real wages adjust without money wage cuts.</li>
    <li><b>Judging severity:</b> consider the <b>rate</b> (2% or 20%), whether it is <b>expected</b>, <b>who</b> is affected, whether it is <b>higher than in other countries</b>, and whether incomes rise at least as fast.</li>
    <li>A <b>low, stable</b> rate is usually seen as acceptable and even desirable; <b>high and volatile</b> inflation is clearly harmful.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Name <b>who loses and who gains</b>, and use the technical terms (menu costs, shoe leather costs, purchasing power, competitiveness). In evaluation, say the effect depends on the <b>rate</b> and whether it is <b>expected</b>.</div>
'''

watch = '''
  <h2>1 · The real value of savings and debts</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stV"></div>
  <h2>2 · Inflation and competitiveness</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Winners and losers</h2>
  <p>Set the inflation rate and see the real value of a saver's money, a borrower's debt and a fixed pension after ten years.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>$1,000 saved is worth</small><strong id="r1"></strong></div><div><small>$1,000 debt is worth</small><strong id="r2"></strong></div><div><small>Fixed $1,000 pension buys</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of the real value of savings, debt and a fixed pension"></svg></div></div></div>

  <h2>Lab 2 · Competitiveness</h2>
  <p>A home firm's export price rises with domestic inflation while a foreign rival's price rises with foreign inflation. See how relative prices change over five years.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Home price after 5 years</small><strong id="t1"></strong></div><div><small>Rival price after 5 years</small><strong id="t2"></strong></div><div><small>Home relative to rival</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Lines of the home and rival export price over five years"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Who gains and who loses?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the competitiveness effect in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A pensioner on a fixed income", "A pension of $1,000 a month buys less each year if prices rise 5% a year. After five years it buys about 78% as much, so pensioners lose out unless the pension is index-linked.", "fixed income earners losing from inflation.") +
rw("A mortgage borrower", "A household owes $100,000 at a fixed rate. If prices and wages rise, the debt shrinks in real terms and is easier to repay. Lenders lose the real value of what they are owed.", "borrowers gaining and lenders losing.") +
rw("A restaurant changing its menu", "Rising costs force a restaurant to reprint menus and change prices several times a year. The time and cost are menu costs, which are small for mild inflation but large when prices rise rapidly.", "menu costs.") +
rw("Hyperinflation", "When prices rise by hundreds of percent a month, wages lose value within days. People spend money as soon as they receive it or switch to a foreign currency, and money stops working as a store of value and medium of exchange.", "extreme consequences of inflation.") +
rw("Savers and fixed incomes", "A pensioner lives on a fixed pension while prices rise 8% a year. Each year the pension buys less, so purchasing power falls.", "who loses from inflation.") +
rw("Hyperinflation", "In extreme cases, prices double within weeks. Shops reprice several times a day, workers rush to spend wages immediately, and people turn to foreign currencies, so the national currency stops working as money.", "menu costs, shoe leather costs and the functions of money.")
)

mc_exam = [
  mcq("s23_11", 17, "Which group is most likely to suffer during high inflation?", ["borrowers", "importers", "producers", "fixed wage earners"], 3, "Fixed wages lose purchasing power as prices rise. Borrowers gain."),
  mcq("s22_14", 23, "What is a likely consequence of inflation?", ["Fixed-income earners gain more than those whose income is gained from the ownership of property", "Real wages rise more than money wages", "The assets of creditors decrease in value at the expense of those of debtors", "The domestic purchasing power of money increases"], 2, "Inflation erodes the real value of money owed to creditors, which benefits debtors. Purchasing power falls."),
  mcq("s21_13", 22, "A sudden rise in the price of imported oil caused the annual rate of inflation in a given period to be higher than expected. What might be a likely result of this?", ["Borrowers would gain", "Real wages would rise", "The balance of trade would improve", "Unemployment would fall"], 0, "Unexpectedly high inflation reduces the real value of debts, so borrowers gain."),
  mcq("m21_12", 29, "Other things being equal, what is most likely to be reduced by falling labour productivity?", ["the balance of trade deficit", "the internal value of money", "the level of unemployment", "the rate of domestic inflation"], 1, "Lower productivity raises unit costs and prices, which reduces the internal value (purchasing power) of money.")
]

exam = exam_page("the consequences of inflation",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The consequences of inflation are a 12 mark Paper 2 discussion in most years (domestic versus external effects, whether they are always negative) and a 4 or 6 mark data-response part. Reworded past questions are below, with four Paper 1 multiple choice questions.",
  [("Essay parts, 12 marks", "3", "Oct/Nov 2021 (22) Q4(b); Oct/Nov 2023 (22) Q5(b); May/June 2025 (24) Q4(b)"), ("Data response, 4 to 6 marks", "5", "May/June 2022 (21) Q1(c); Oct/Nov 2024 (21) Q1(c); Feb/March 2023 (22) Q1(e); Oct/Nov 2021 (21) Q1(e); May/June 2025 (21) Q1(c)"), ("Multiple choice (Paper 1)", "4 shown below", "2020 to 2024")],
  [
  eq(P("s22_21", "1(c)"), "4 marks", "Explain one domestic consequence and one external consequence of a relatively high rate of inflation.",
     ["Identification of one possible domestic consequence (1) and an explanation (1): for example redistribution of income as real earnings of some workers rise and others fall, borrowers gaining and lenders losing, menu costs, shoe leather costs, uncertainty that could discourage investment, weaker purchasing power of money.",
      "Identification of one possible external consequence (1) and an explanation (1): for example exports become less competitive, imports more attractive, the current account worsens and the exchange rate may fall."],
     "Domestic: e.g. loss of purchasing power or menu costs. External: loss of export competitiveness.",
     [[("k", "A domestic consequence is a loss of purchasing power for people on fixed incomes, because their money buys less each year as prices rise."), ("n", "An external consequence is a loss of competitiveness: if inflation at home is higher than in other countries, exports become dearer to foreign buyers and imports become cheaper for home buyers, so the current account is likely to worsen.")]]),
  eq(P("w24_21", "1(c)"), "4 marks", "Consider the extent to which having the fifth highest inflation rate in the world is likely to be a problem for an economy.",
     ["Up to 2 marks for explaining why a high rate of inflation might be a problem: reduced purchasing power of money, less competitive exports, menu costs, shoe leather costs, uncertainty and the possible impact on investment, harm to savers and to fixed income earners.",
      "Up to 1 mark for a possible benefit, such as increased profits for firms and lower debt in real terms.",
      "1 mark for a valid judgement on the extent to which a high inflation rate is a serious problem, taking into account how it compares with other countries and the fact that inflation can have some benefits."],
     "Problems: purchasing power, competitiveness, uncertainty. A benefit: debt falls. Judge: depends on size and how it compares.",
     [[("n", "A very high inflation rate reduces the purchasing power of money, hurts savers and fixed-income earners, makes exports less competitive and creates uncertainty that may discourage investment. Some groups gain, since borrowers see debts fall in real terms and firms may see profits rise."), ("e", "Overall it is likely to be a serious problem if it is much higher than in other countries and unpredictable, but its size and whether it has been expected affect how damaging it is.")]]),
  eq(P("w21_22", "4(b)"), "12 marks", "Discuss whether the domestic effects of inflation are more serious than the external effects for an economy.",
     ["Analysis (up to 8): domestic effects, such as loss of purchasing power, redistribution between borrowers and lenders and between fixed and variable incomes, menu and shoe leather costs, and the effect of uncertainty on investment (up to 4); external effects, such as loss of competitiveness of exports, a worsening current account and a falling exchange rate (up to 4). Indicative content may include these points.",
      "Evaluation (up to 4): a judgement on which effects are more serious, depending on the rate of inflation, whether it is expected, the openness of the economy and a comparison with other countries, with a conclusion."],
     "Domestic: purchasing power, redistribution, menu costs, investment. External: competitiveness, current account, exchange rate. Judge: depends on how open the economy is.",
     [[("n", "Domestic effects of inflation include a loss of purchasing power, especially for savers and people on fixed incomes, redistribution from lenders to borrowers, menu and shoe leather costs, and uncertainty that may discourage investment. External effects arise if domestic inflation is higher than in competitor countries: exports become less competitive, imports more attractive, and the current account and the exchange rate may worsen.")], [("e", "The domestic effects are probably more serious for a mainly domestic economy, since they affect most households, while the external effects matter more for a trade-dependent economy. It also depends on how high the inflation is relative to other countries and whether it was expected.")]]),
  eq(P("s25_24", "4(b)"), "12 marks", "Assess whether the consequences of inflation in an economy are always negative.",
     ["Analysis (up to 8): the negative consequences, such as loss of purchasing power, redistribution against savers and fixed-income earners, menu and shoe leather costs, uncertainty, and loss of competitiveness (up to 4); possible positive consequences, such as reducing the real value of debts, higher profit margins that may encourage investment, and allowing real wages to adjust (up to 4).",
      "Evaluation (up to 4): a judgement on whether the consequences are always negative, depending on the rate, whether it was expected and who is affected, with a conclusion."],
     "Negatives: purchasing power, savers, costs, competitiveness. Positives: debt falls, profits. Judge: mild, expected inflation is acceptable; high, unexpected is damaging.",
     [[("n", "Inflation reduces the value of money, so savers and those on fixed incomes lose, firms face menu costs and uncertainty that can discourage investment, and exports become less competitive if inflation is higher than abroad. But inflation also reduces the real value of debts, helping borrowers and governments, and rising prices can raise profits, which may encourage investment.")], [("e", "The consequences are not always negative. Low, stable and expected inflation, around 2%, causes few problems and can help borrowers, while high, rising and unexpected inflation is damaging to most groups. The result depends on the rate, whether it was expected and who is affected.")]]),
  eq(P("w23_22", "5(b)"), "12 marks", "Assess whether the internal effects of inflation are more serious than the external effects of inflation for an economy.",
     ["Analysis (up to 8): the internal effects of inflation, those affecting the domestic economy directly: income redistribution, menu costs, shoe leather costs, uncertainty in transactions, and that it may provide a stimulus for output and be a sign of economic growth; and the external effects, those affecting international trade: declining price competitiveness of exports and increased imports, a worsening current account and effects on the exchange rate.",
      "Evaluation (up to 4): a judgement on which effects are more serious, with a conclusion."],
     "Internal: redistribution, menu and shoe leather costs, uncertainty. External: exports less competitive, imports up, current account, exchange rate. Judge: depends on how open the economy is and the rate.",
     [[("n", "Internally, inflation redistributes income from savers and people on fixed incomes to borrowers, imposes menu and shoe leather costs and creates uncertainty that discourages investment. Externally, higher domestic inflation makes exports dearer and imports cheaper, so the current account may worsen and the currency may weaken, which raises import prices.")], [("e", "Which is more serious depends on the economy. For a very open economy, external effects such as lost competitiveness may matter more, while for a less open one the internal effects such as redistribution and uncertainty may dominate. The effects are also worse when inflation is high and unexpected.")]]),
  eq(P("m23_22", "1(e)"), "6 marks", "Assess the possible consequences of a rising rate of inflation for a country such as the US.",
     ["Analysis (up to 4): possible negative consequences (up to 2): uncompetitive exports leading to a worsening current account, shoe leather costs, menu costs, planning difficulties from uncertainty, and a redistribution of income, with those on fixed incomes losing out; possible positive consequences (up to 2): increased borrowing because debt is less in real terms, higher profits for firms possibly leading to more workers being employed, and an increase in the value of assets such as property.",
      "Evaluation (up to 2): relevant evaluation, for example the extent of the increase, whether it is higher than in other countries, the price elasticity of demand for exports, whether prices are rising faster than costs and whether the rise is anticipated."],
     "Negative: exports, shoe leather and menu costs, uncertainty, fixed incomes. Positive: debt falls, profits, asset values. Judge: size of the rise, expected or not.",
     [[("n", "Rising inflation could make exports less competitive and worsen the current account, impose menu and shoe leather costs, create uncertainty and redistribute income away from those on fixed incomes. But borrowers gain as debt falls in real terms, firms' profits may rise if prices rise faster than costs, and asset values such as property may increase."), ("e", "The effect depends on how large the rise is, whether it is expected and how it compares with other countries. Mild, expected inflation has few costs, while high and unexpected inflation is more harmful.")]]),
  eq(P("w21_21", "1(e)"), "6 marks", "Discuss whether everybody in an economy such as Venezuela would be worse off as a result of hyperinflation.",
     ["Analysis (up to 5): that some people could be worse off (up to 3), for example through the erosion of the real value of money, reduced purchasing power, uncompetitive exports, redistribution to the disadvantage of those on fixed incomes, menu costs, shoe leather costs and uncertainty; that some could be better off (up to 3), for example firms whose prices rise by more than their costs, which can encourage expansion and reduce unemployment, and borrowers whose debts fall in real terms.",
      "Reserve 1 mark for a conclusion."],
     "Worse off: fixed incomes, savers, exporters, uncertainty. Better off: borrowers, firms with price rises above costs, asset owners. Conclude: most are worse off, but not everyone.",
     [[("n", "Hyperinflation erodes the real value of money and wipes out the purchasing power of people on fixed incomes and savers, makes exports uncompetitive and creates huge menu and shoe leather costs and uncertainty. But borrowers gain as their debts shrink in real terms, and firms whose prices rise faster than their costs may make bigger profits."), ("e", "Most people are likely to be worse off, particularly the poor, but some groups with debts or real assets may gain, so not everybody is worse off.")]]),
  eq(P("s25_21", "1(c)"), "4 marks", "In an attempt to bring about disinflation, a central bank used a contractionary monetary policy. Consider whether disinflation is more harmful than deflation.",
     ["Analysis (up to 3): disinflation is a fall in the rate of inflation (1), so although the problems of inflation are less they remain, such as the effect on the distribution of income, purchasing power, the competitiveness of exports, menu costs, shoe leather costs and investment planning (1); deflation is a fall in the general price level (1), which can bring problems such as a fall in AD leading to a recession, lower output and higher unemployment, and negative effects on investment (1). A maximum of 2 if only one of the two is considered.",
      "Evaluation (up to 1 or 2): for example, the extent of the disinflation, that is, by how much the rate is falling."],
     "Disinflation: prices still rise, smaller problems. Deflation: delayed spending, recession, debt. Judge: deflation is usually more harmful, unless disinflation is deep.",
     [[("n", "Disinflation is a fall in the rate of inflation, so prices still rise and the problems of inflation, such as menu costs and redistribution, remain though they are smaller. Deflation is a fall in the general price level, which can make consumers delay spending, causing a fall in AD, lower output and higher unemployment, and raising the real burden of debt."), ("e", "Deflation is generally more harmful because it can cause a spiral of falling output, whereas disinflation lowers the cost of inflation, unless the fall in inflation is so large that it risks pushing the economy into deflation.")]])
  ],
  )

tips = tips_html(
  [("Name winners and losers.", "Borrowers gain; savers and fixed incomes lose."),
   ("Use the technical terms.", "Menu costs, shoe leather costs, purchasing power."),
   ("Domestic and external.", "Competitiveness and current account are external."),
   ("Mention expectations.", "Unexpected inflation is more damaging."),
   ("Discuss rate.", "Low, stable inflation is acceptable."),
   ("Include deflation and hyperinflation.", "Extreme cases of price instability."),
   ("Judge with 'it depends'.", "Who, how high, how expected.")],
  [("Purchasing power", "Inflation reduces the purchasing power of money."),
   ("Menu costs", "Menu costs are the costs to firms of changing prices."),
   ("Shoe leather costs", "Shoe leather costs are the time and effort of looking for better returns."),
   ("Competitiveness", "Higher inflation than abroad may make exports less competitive."),
   ("Assess", "The consequences depend on the rate and whether inflation was expected.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = '''
/* ---------- real value ---------- */
function rvDraw(s) {
  const Y = (v) => 250 - v * 0.2, f = (r, n) => Math.pow(1 + r / 100, n); let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "Real value ($, year-0 prices)", "sm");
  const r = 6, yrs = s.k, v = 1000 / f(r, yrs), dpt = 1000 / f(r, yrs);
  o += SV.rect(110, Y(1000), 90, 200, "f1", op(0.25)) + SV.text(155, 270, "Cash or fixed pension", "sm", { "text-anchor": "middle" }) + SV.rect(110, Y(v), 90, 250 - Y(v), "f3", op(0.7)) + SV.text(155, Y(v) - 6, "$" + Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" });
  o += SV.rect(300, Y(1000), 90, 200, "f1", op(0.25)) + SV.text(345, 270, "A debt of $1,000", "sm", { "text-anchor": "middle" }) + SV.rect(300, Y(dpt), 90, 250 - Y(dpt), "f2", op(0.7)) + SV.text(345, Y(dpt) - 6, "$" + Lib.fmtN(dpt, 0), "lbl bd", { "text-anchor": "middle" });
  o += SV.text(540, 130, "After " + Lib.fmtN(yrs, 0) + " years at 6% inflation", "lbl bd", { "text-anchor": "middle" }) + SV.text(540, 152, "the saver loses and the borrower gains", "sm", { "text-anchor": "middle" });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Cash and debt both fall in real value after years of inflation">${rvDraw({ k: 10 })}</svg>`;
Lib.stepper($("#stV"), { w: 760, h: 290, label: "The real value of cash and of debt at 6% inflation", base: { k: 0 }, draw: rvDraw, tween: 1000, dwell: 5200, steps: [
  { cap: "<b>Start.</b> $1,000 in cash (or a fixed pension) and a $1,000 debt. The shaded boxes show the starting value.", s: { k: 0 } },
  { cap: "<b>After 5 years at 6% inflation</b> the $1,000 buys only about $747 worth of today's goods. The saver or fixed-income earner has lost; the borrower's debt is also worth only $747 in real terms.", s: { k: 5 } },
  { cap: "<b>After 10 years</b> it is worth about $558. Inflation redistributes real income from lenders and savers to borrowers.", s: { k: 10 } },
] });
const CMP = (home, rival, yr) => ({ h: 100 * Math.pow(1 + home / 100, yr), r: 100 * Math.pow(1 + rival / 100, yr) });
function cpDraw(s) {
  let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "Export price index", "sm") + SV.text(700, 270, "Years", "sm", { "text-anchor": "end" });
  let dh = "", dr = ""; for (let t = 0; t <= s.k; t += 0.25) { const p = CMP(8, 2, t), x = 60 + t * 62, yh = 250 - (p.h - 90) * 4, yr = 250 - (p.r - 90) * 4; dh += (t ? " L" : "M") + x + "," + yh; dr += (t ? " L" : "M") + x + "," + yr; }
  o += SV.path(dr, "c1", { fill: "none", "stroke-width": 3 }) + SV.path(dh, "c3", { fill: "none", "stroke-width": 3 });
  const p = CMP(8, 2, s.k); o += tag(66 + s.k * 62, 250 - (p.h - 90) * 4 - 6, "Home " + Lib.fmtN(p.h, 0), "c3") + tag(66 + s.k * 62, 250 - (p.r - 90) * 4 + 18, "Rival " + Lib.fmtN(p.r, 0), "c1");
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Home export prices rising faster than a rival's">${cpDraw({ k: 5 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 290, label: "Export prices when home inflation is 8% and the rival's 2%", base: { k: 0 }, draw: cpDraw, tween: 1000, dwell: 5200, steps: [
  { cap: "<b>Start.</b> A home exporter and a foreign rival both sell at an index price of 100.", s: { k: 0 } },
  { cap: "<b>After 3 years</b> the home price has risen 26% (inflation 8%) and the rival's 6% (inflation 2%).", s: { k: 3 } },
  { cap: "<b>After 5 years</b> the home price is about 47% higher against 10% for the rival. Home exports are now much less price competitive: sales fall and the current account is likely to worsen.", s: { k: 5 } },
] });

/* ---------- Lab 1 ---------- */
function labV() {
  if (!["in", "yr"].every((i) => $("#" + i))) return;
  const r = +$("#in").value, n = +$("#yr").value, f = Math.pow(1 + r / 100, n), v = 1000 / f;
  $("#r1").textContent = "$" + Lib.fmtN(v, 0); $("#r2").textContent = "$" + Lib.fmtN(v, 0); $("#r3").textContent = Lib.fmtN(100 / f, 0) + "% as much";
  $("#rv").textContent = `With ${r}% inflation for ${n} years prices are ${Lib.fmtN((f - 1) * 100, 0)}% higher. $1,000 held in cash or as a fixed pension buys what $${Lib.fmtN(v, 0)} bought at the start, so savers and pensioners lose. A $1,000 debt is also worth only $${Lib.fmtN(v, 0)} in real terms, so borrowers gain at the expense of lenders.`;
  const Y = (x) => 250 - x * 0.2; let o = SV.line(40, 250, 400, 250);
  [["Saved cash", v, "f3"], ["Debt owed", v, "f2"], ["Pension buys", v, "f1"]].forEach(([l, z, c], i) => (o += SV.rect(60 + i * 110, Y(1000), 80, 200, "f1", op(0.2)) + SV.rect(60 + i * 110, Y(z), 80, 250 - Y(z), c, op(0.7)) + SV.text(100 + i * 110, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(100 + i * 110, Y(z) - 6, "$" + Lib.fmtN(z, 0), "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "in", label: "Inflation rate, % per year ", min: 0, max: 15, step: 1, value: 5, fmt: (v) => v + "%", onInput: labV });
Lib.slider($("#g2"), { id: "yr", label: "Number of years ", min: 1, max: 15, step: 1, value: 10, fmt: (v) => v, onInput: labV });
labV();

/* ---------- Lab 2 ---------- */
function labK() {
  if (!["hm", "fr"].every((i) => $("#" + i))) return;
  const h = +$("#hm").value, r = +$("#fr").value, p = CMP(h, r, 5), rel = p.h / p.r * 100;
  $("#t1").textContent = Lib.fmtN(p.h, 0); $("#t2").textContent = Lib.fmtN(p.r, 0); $("#t3").textContent = Lib.fmtN(rel, 0) + "%";
  $("#tv").textContent = h > r ? `Home inflation (${h}%) exceeds the rival's (${r}%), so after 5 years home exports cost ${Lib.fmtN(rel - 100, 0)}% more relative to the rival's: less price competitive, falling export sales and a worse current account (other things equal, including the exchange rate).` : h < r ? `Home inflation (${h}%) is below the rival's (${r}%), so home exports become relatively cheaper (${Lib.fmtN(100 - rel, 0)}% cheaper): more competitive.` : "Equal inflation leaves relative prices unchanged.";
  let o = SV.line(40, 190, 400, 190) + SV.line(40, 190, 40, 20), a = "", b = ""; for (let t = 0; t <= 5; t += 0.25) { const q = CMP(h, r, t), x = 40 + t * 70; a += (t ? " L" : "M") + x + "," + (190 - (q.h - 95) * 3); b += (t ? " L" : "M") + x + "," + (190 - (q.r - 95) * 3); }
  o += SV.path(b, "c1", { fill: "none", "stroke-width": 3 }) + SV.path(a, "c3", { fill: "none", "stroke-width": 3 }) + tag(330, 40, "Home", "c3") + tag(330, 58, "Rival", "c1");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "hm", label: "Home inflation, % per year ", min: 0, max: 12, step: 1, value: 8, fmt: (v) => v + "%", onInput: labK });
Lib.slider($("#g4"), { id: "fr", label: "Foreign (rival) inflation, % per year ", min: 0, max: 12, step: 1, value: 2, fmt: (v) => v + "%", onInput: labK });
labK();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Does the group gain or lose from unexpected inflation?", ["Gains", "Loses"],
  [("A borrower with a fixed-rate loan", 0), ("A saver with low interest", 1), ("A pensioner on a fixed pension", 1), ("A firm with large debts", 0), ("A worker whose pay does not rise", 1), ("A lender", 1), ("A homeowner whose property price rises", 0), ("An exporter facing dearer home costs", 1)],
  "Inflation helps debtors and owners of real assets; it hurts savers, lenders and those on fixed incomes.") + MATCH([
  ["Menu costs", "Costs to firms of changing prices"],
  ["Shoe leather costs", "Time and effort spent looking for better returns"],
  ["Purchasing power", "What money can buy"],
  ["Hyperinflation", "Extremely rapid price rises that destroy money's functions"],
  ["Loss of competitiveness", "Exports dearer than rivals' because of higher inflation"],
  ["Fixed income", "Income that does not rise with prices"]]) + ORDER(
  "Put the competitiveness effect of inflation in order.",
  ["Domestic inflation is higher than abroad", "Home exports become dearer relative to foreign goods", "Foreign buyers switch to rivals; home buyers switch to imports", "Net exports fall and the current account worsens", "The exchange rate may fall"],
  "Higher inflation reduces competitiveness and the current account.") + CALC([
  {"q": "Prices rise 5% a year for 3 years. By roughly what percentage have they risen in total (nearest whole number)?", "a": 16, "unit": "%", "tol": 0.5, "hint": "1.05³ = 1.158.", "sol": "<b>16%</b>."},
  {"q": "A fixed pension of $1,000 a month faces inflation of 4% for a year. What is it worth in last year's prices ($, nearest whole number)?", "a": 962, "unit": "$", "tol": 1, "hint": "1,000 ÷ 1.04.", "sol": "<b>$962</b>."},
  {"q": "A savings account pays 2% and inflation is 5%. What is the real interest rate (%)?", "a": -3, "unit": "%", "tol": 0.2, "hint": "2 − 5.", "sol": "<b>−3%</b>: savers lose in real terms."},
  {"q": "A firm reprints a menu at a cost of $500 four times a year. What are its yearly menu costs ($)?", "a": 2000, "unit": "$", "tol": 1, "hint": "4 × 500.", "sol": "<b>$2,000</b>."}]) + MCQ([
  ("Who is most likely to gain from unexpected inflation?", ["Borrowers", "Savers", "Pensioners on fixed incomes", "Lenders"], 0, "Debts fall in real terms."),
  ("Menu costs are:", ["The costs of changing prices", "The costs of eating out", "The costs of borrowing", "Tax on food"], 0, "A cost to firms."),
  ("Higher inflation than competitors is likely to:", ["Reduce export competitiveness", "Raise export competitiveness", "Improve the current account", "Reduce imports"], 0, "Exports dearer."),
  ("Hyperinflation can destroy:", ["Money's functions as a medium of exchange and store of value", "Tax revenue only", "Unemployment", "Interest rates"], 0, "Money loses trust."),
  ("A low and stable rate of inflation is usually considered:", ["Acceptable", "Harmful", "The same as deflation", "Impossible"], 0, "Few costs.")
], "qz1") + CARDS([
  ("Gain", "Borrowers, owners of real assets."),
  ("Lose", "Savers, lenders, fixed incomes."),
  ("Menu costs", "Changing prices."),
  ("Shoe leather", "Searching for returns."),
  ("Uncertainty", "Less investment."),
  ("Competitiveness", "Exports dearer."),
  ("Hyperinflation", "Money fails."),
  ("Evaluate", "Rate, expected or not, who.")]) + MCQ(mc_exam)

build("as4c", "as-consequences-of-inflation", "Consequences of Inflation", EY,
  "4.6.5: the domestic and external consequences of inflation, who gains and loses, and the effects of very high inflation. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
