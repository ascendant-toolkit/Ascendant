"""Syllabus 9.4.7-9.4.8 Liquidity preference theory and interest rate determination. Run: python3 tools/artifact-kit/mk_sy947.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.4.7 to 9.4.8"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>In <b class="kw">Keynes's liquidity preference theory</b>, people demand money for three motives: <b>transactions</b>, <b>precautionary</b> (together called <b>active balances</b>, which depend mainly on income) and <b>speculative</b> (<b>idle balances</b>, which depend on the interest rate, because the interest rate is the reward for giving up liquidity). The <b>interest rate is set where the demand for money (the liquidity preference curve) meets the money supply</b>. At a very low rate, people prefer to hold money rather than bonds, so the demand curve becomes flat: a <b class="kw">liquidity trap</b>, where more money does not lower rates further. The <b class="kw">loanable funds theory</b> instead says the interest rate is the price that balances <b>saving</b> (the supply of loanable funds) with <b>borrowing for investment</b> (the demand).</p></div>

  <h2>1 · The demand for money: liquidity preference (9.4.7)</h2>
  <div class="tw"><table class="t">
    <tr><th>Motive</th><th>Why people hold money</th><th>Depends on</th><th>Type of balance</th></tr>
    <tr><td><b>Transactions</b></td><td>To pay for everyday purchases between receiving income</td><td>Income, frequency of payment, price level</td><td>Active</td></tr>
    <tr><td><b>Precautionary</b></td><td>For unexpected expenses and emergencies</td><td>Income, uncertainty</td><td>Active</td></tr>
    <tr><td><b>Speculative</b></td><td>To avoid losses on bonds and wait for better returns</td><td><b>The interest rate</b> and expectations about bond prices</td><td>Idle</td></tr>
  </table></div>
  <h3>The speculative motive and the bond price</h3>
  <ul>
    <li><b>Bond price and the interest rate move in opposite directions.</b> When the interest rate falls, bond prices rise.</li>
    <li>At a <b>high</b> interest rate bond prices are low and people expect them to rise: they buy bonds and hold <b>little</b> idle money.</li>
    <li>At a <b>low</b> interest rate bond prices are high and people expect them to fall (rates will rise): they sell bonds and hold <b>more</b> idle money.</li>
    <li>So the <b>demand for money (liquidity preference, LP) slopes downward</b>: the lower the interest rate, the more money people want to hold. In practice the opportunity cost of holding money is the interest forgone.</li>
  </ul>
  <h3>Shifts of the LP curve and the money supply</h3>
  <ul>
    <li><b>LP shifts right</b> when income or the price level rises, when payments become less frequent, when uncertainty rises or when credit is harder to obtain.</li>
    <li><b>LP shifts left</b> when payments become more frequent, when credit cards and cash machines allow smaller balances.</li>
    <li>The <b>money supply (MS)</b> is a <b>vertical</b> line, set by the central bank and banks.</li>
  </ul>

  <h2>2 · Interest rate determination: the Keynesian theory (9.4.8)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li>The equilibrium interest rate is where <b>LP meets MS</b>. If the rate is above equilibrium, people hold less money than is supplied, so they buy bonds, pushing bond prices up and the interest rate down. If below, the reverse.</li>
    <li><b>An increase in the money supply</b> (central bank buys bonds, QE) shifts MS right, so the interest rate falls; a <b>decrease</b> raises it.</li>
    <li><b>A rise in income</b> shifts LP right and raises the interest rate.</li>
    <li>The transmission to the economy: lower interest rates raise investment (depending on the marginal efficiency of capital) and consumption, raising AD. The effect is weaker if investment is interest inelastic.</li>
  </ul>
  <h3>The liquidity trap</h3>
  <p>At a very low interest rate (near zero), bond prices are very high and people expect them to fall, so they hold any extra money rather than buying bonds. The LP curve becomes <b>horizontal</b>. An increase in the money supply then <b>does not reduce the interest rate further</b>, so monetary policy loses its effect. This is a feature of deep recessions: low inflation (or deflation), low interest rates and low growth. The Keynesian remedy is <b>fiscal policy</b>.</p>

  <h2>3 · The loanable funds theory</h2>
  <ul>
    <li>The interest rate is the <b>price of loanable funds</b>, set by the <b>supply of funds</b> (saving by households, firms, governments and foreign lenders) and the <b>demand for funds</b> (borrowing for investment, consumption and government deficits).</li>
    <li>A rise in <b>saving</b> shifts supply right, lowering the interest rate and raising investment. A rise in <b>investment demand</b> (business confidence, higher expected profit) shifts demand right, raising the rate.</li>
    <li>The theory focuses on <b>real</b> flows of saving and investment, and the interest rate brings saving and investment into balance.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th></th><th>Liquidity preference (Keynes)</th><th>Loanable funds (classical)</th></tr>
    <tr><td><b>What is the interest rate?</b></td><td>The reward for giving up liquidity</td><td>The price of borrowing and the reward for saving</td></tr>
    <tr><td><b>Determined by</b></td><td>Demand for and supply of <b>money</b> (a stock)</td><td>Supply of and demand for <b>loanable funds</b> (flows of saving and investment)</td></tr>
    <tr><td><b>Role of income</b></td><td>Income affects the demand for money</td><td>Saving depends on income, but the focus is on saving and investment</td></tr>
    <tr><td><b>Saving and investment</b></td><td>Not equalised by the interest rate: they are done by different people for different reasons, and income adjusts to equalise them</td><td>The interest rate adjusts until saving equals investment</td></tr>
    <tr><td><b>Policy</b></td><td>Central bank sets the money supply and so the rate; a liquidity trap may limit it</td><td>Government deficits raise the demand for funds and can raise the rate (crowding out)</td></tr>
  </table></div>
  <div class="tip"><b class="h">Keynes versus the classical view</b>Keynes argued that saving and investment are not equalised by the interest rate. If people save more, a fall in spending reduces income, which brings saving back into line with investment (the paradox of thrift), so a rise in saving could cause a recession, not lower interest rates and more investment.</div>
'''

watch = '''
  <h2>1 · The money market: the interest rate and a rise in the money supply</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stM"></div>
  <h2>2 · The loanable funds market</h2>
  <div id="stL"></div>
'''

explore = '''
  <h2>Lab 1 · The money market</h2>
  <p>Set the money supply and the level of income. The interest rate is where the money supply meets liquidity preference. Notice what happens when the money supply is already large.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Interest rate</small><strong id="r1"></strong></div><div><small>Bond price index</small><strong id="r2"></strong></div><div><small>Regime</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Liquidity preference curve and a vertical money supply curve with the equilibrium interest rate"></svg></div></div></div>

  <h2>Lab 2 · Loanable funds</h2>
  <p>Move the supply of saving and the demand for investment funds. See the interest rate and the quantity of funds lent.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Interest rate</small><strong id="t1"></strong></div><div><small>Funds lent and invested</small><strong id="t2"></strong></div><div><small>Effect</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Supply and demand for loanable funds with the equilibrium interest rate"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which motive for holding money?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of QE on the interest rate in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Japan's decades of near-zero rates", "From the late 1990s the Bank of Japan held interest rates close to zero and later bought bonds on a huge scale. Money supply rose but lending, spending and inflation stayed weak, which is often cited as an example of a liquidity trap.", "the liquidity trap and the limits of monetary policy. Link to fiscal policy as a remedy and to the Keynesian argument.") +
rw("The US and UK after 2008", "Central banks cut rates to 0.1% to 0.5% and then used quantitative easing. Yields on bonds fell to record lows. Even so, business investment recovered slowly because firms lacked confidence.", "low interest rates may not raise investment if the marginal efficiency of capital is low.") +
rw("Rising rates in 2022", "As inflation rose, central banks raised rates sharply from near zero. Bond prices fell, and some banks holding long-dated bonds suffered losses, showing the inverse link between interest rates and bond prices.", "the inverse relationship between bond prices and interest rates, and the speculative motive.") +
rw("Global savings glut", "Before 2008, high saving in China and oil exporters increased the supply of loanable funds worldwide. This helped to keep real interest rates low, and cheap credit may have fuelled borrowing and house prices.", "an application of the loanable funds theory: a rise in saving lowers the interest rate.")
)

mc_exam = [
  ("Which combination is consistent with liquidity preference theory? Speculative demand for money depends on the interest rate; transactions demand depends on income. (Feb/March 2021 · 32 · Q25, reworded)", ["Speculative demand depends on interest rates and not on income changes; transactions demand does not depend on interest rates", "Speculative demand depends on income; transactions demand depends on interest rates", "Both depend only on interest rates", "Neither depends on interest rates"], 0, "Active balances (transactions) depend on income; idle (speculative) balances depend on the interest rate."),
  ("Which statement about Keynes's liquidity preference model is correct? (May/June 2022 · 31 · Q25, reworded)", ["Both transactions and precautionary motives are interest rate elastic", "The demand for liquidity is completely interest inelastic at low rates", "The demand to hold liquidity by households is stable", "The demand for liquidity is highly elastic at very low interest rates"], 3, "At very low rates the speculative demand is almost infinitely elastic: the liquidity trap."),
  ("According to liquidity preference theory, which money balances respond to changes in the interest rate? (Oct/Nov 2021 · 32 · Q26, reworded)", ["Idle balances only", "Active balances only", "Both", "Neither"], 0, "Idle (speculative) balances respond to the interest rate; active balances depend on income."),
  ("Keynesians say the demand for money is negatively related to the interest rate. Which motive best explains this? (Oct/Nov 2021 · 33 · Q27, reworded)", ["Income motive", "Precautionary motive", "Speculative motive", "Transactions motive"], 2, "At low interest rates (high bond prices) people hold more idle money."),
  ("In Keynesian economic theory, what is the purpose of interest? (May/June 2025 · 34 · Q18, reworded)", ["To bring national income and expenditure into line", "To control the level of economic growth", "To create a balance between saving and investment", "To provide a reward for surrendering liquidity"], 3, "Keynes saw interest as the reward for giving up liquidity, not for saving."),
  ("An individual's demand for active money balances will move to the left if there is an increase in: (May/June 2020 · 31 · Q25, reworded)", ["The frequency of income payments", "The general price level", "The individual's income", "The rate of interest"], 0, "More frequent pay means smaller balances are needed between payments."),
  ("Which characteristics describe an economy in a liquidity trap? Inflation, interest rate, growth. (May/June 2024 · 32 · Q21, reworded)", ["High inflation, high rate, low growth", "Low inflation, high rate, low growth", "Low inflation, low rate, low growth", "Low inflation, low rate, high growth"], 2, "A liquidity trap is found in a deep slump with low inflation, near-zero rates and weak growth."),
  ("According to Keynesian theory, when will an increase in the money supply leave output unchanged? (Oct/Nov 2022 · 32 · Q23, reworded)", ["When there is a liquidity trap", "When the increase was not anticipated", "When the exchange rate is floating", "When expectations adjust immediately"], 0, "In a liquidity trap extra money does not lower interest rates, so spending does not rise.")
]

exam = exam_page("liquidity preference, interest rates and the liquidity trap",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Liquidity preference and interest rate determination are standard 12 mark Paper 4 questions, often paired with a 13 mark policy question. Reworded questions are below, with eight Paper 3 multiple choice questions.",
  [("Essay parts, 12 marks", "4", "May/June 2020 (42) Q7(a); Oct/Nov 2021 (43) Q5(a); Oct/Nov 2022 (41) Q5(a); Oct/Nov 2022 (42) Q5(a)"), ("Essay parts, 13 marks", "2", "Oct/Nov 2021 (43) Q5(b); Oct/Nov 2022 (42) Q5(b)"), ("Multiple choice (Paper 3)", "8 shown below", "2020 to 2025")],
  [
  eq("Based on May/June 2020 · 9708/42 · Q7(a)", "12 marks", "Explain the Keynesian theory of the determination of the rate of interest.",
     ["The three motives for holding money: transactions and precautionary (active balances, depend on income) and speculative (idle balances, depend on the interest rate through the bond price).",
      "The liquidity preference curve slopes downward, the money supply is vertical, and the interest rate is set where they meet, shown on a diagram.",
      "Changes: a rise in the money supply lowers the rate; a rise in income shifts LP right and raises it; the liquidity trap makes LP flat at low rates.",
      "Level 4 (9 to 12) needs a correct diagram and a full explanation of the demand for money."],
     "Three motives. Bond price link. Diagram with LP and MS. A shift of each. The liquidity trap."),
  eq("Based on Oct/Nov 2021 · 9708/43 · Q5(a)", "12 marks", "Explain the role of liquidity preference in the determination of interest rates and assess its importance.",
     ["Liquidity preference: the desire to hold money for transactions, precautionary and speculative reasons; the interest rate is the reward for surrendering liquidity.",
      "Role: the interest rate equilibrates the demand for money and the money supply.",
      "Importance: it explains why very low interest rates may not be reduced further (liquidity trap) and why monetary policy can lose effect; it emphasises expectations and the stock of money; limits are that other factors (the central bank sets the policy rate, saving and investment, risk, inflation expectations) also matter in practice."],
     "Define liquidity preference. Diagram. Role in setting rates. Evaluate the importance with the liquidity trap and limits."),
  eq("Based on Oct/Nov 2021 · 9708/43 · Q5(b)", "13 marks", "Keynes argued that the rate of interest will not ensure that saving equals investment, because they are done by different people for different reasons. Discuss this view.",
     ["The classical (loanable funds) view: a rise in saving lowers the interest rate, which raises investment until saving equals investment.",
      "Keynes: savers (households, mainly depending on income) and investors (firms, depending on expected profit or the marginal efficiency of capital) are different people with different motives, and the interest rate is determined in the money market, not by saving and investment.",
      "Adjustment through income: if saving exceeds investment, income and output fall (the paradox of thrift) until saving is reduced to match investment.",
      "Evaluation: in the long run, and when the economy is at full employment, the loanable funds view may be a good guide; in a recession the Keynesian view is more relevant."],
     "Classical view. Keynes's objection. Adjustment by income. When each is relevant."),
  eq("Based on Oct/Nov 2022 · 9708/42 · Q5(a)", "12 marks", "Using the Keynesian theory of interest rate determination, explain why interest rates are sometimes very low.",
     ["Diagram with LP and MS: a large increase in the money supply (QE) or a fall in the demand for money lowers the rate.",
      "In a recession income is low, so active balances are low and LP shifts left; if the central bank also expands the money supply the rate falls.",
      "Liquidity trap: at low rates people expect rates to rise and bond prices to fall, so they hold money; LP becomes flat and extra money cannot reduce the rate further, so rates settle near their floor.",
      "A conclusion that rates are low because of weak demand and policy easing."],
     "Diagram. Cause 1: money supply up. Cause 2: weak demand. The flat part of LP."),
  eq("Based on Oct/Nov 2022 · 9708/42 · Q5(b)", "13 marks", "Discuss whether, in a period of very low interest rates, monetary policy alone can solve the problem of cyclical unemployment.",
     ["Cyclical unemployment comes from low AD. Monetary policy can lower rates, use QE and raise lending.",
      "Limits when rates are very low: a liquidity trap, little room to cut further, low business confidence and low interest elasticity of investment, banks not lending.",
      "Alternatives: fiscal policy (government spending, tax cuts, multiplier), supply-side policy for structural unemployment, exchange rate policy.",
      "A reasoned conclusion that monetary policy alone is unlikely to be sufficient in a deep recession."],
     "Monetary tools and limits. A liquidity trap. Fiscal and other policies. Judge: alone is not enough."),
  eq("Based on Oct/Nov 2022 · 9708/41 · Q5(a)", "12 marks", "Explain, with the help of a diagram, the Keynesian theory of the liquidity trap and consider the importance of the liquidity trap to government policy makers when an economy is in a recession.",
     ["LP and MS diagram with the horizontal part of LP at a very low interest rate: extra money does not reduce the rate.",
      "Why: at very low rates bond prices are very high and expected to fall, so people hold money (speculative motive).",
      "Importance: monetary policy becomes ineffective, so governments must use fiscal policy to raise AD (a larger deficit and the multiplier), and may combine with QE and supply-side measures.",
      "Evaluation: how common the trap is; fiscal policy has its own lags and debt costs; evidence from Japan and post-2008."],
     "Diagram with flat section. Reason. Policy consequence. Evidence and limits.")
  ],
  )

tips = tips_html(
  [("Draw the money market.", "Interest rate on the vertical axis, quantity of money on the horizontal axis, LP sloping down, MS vertical."),
   ("Name the three motives.", "Transactions, precautionary (income) and speculative (interest rate)."),
   ("Use the bond price link.", "Bond prices and interest rates move in opposite directions. It explains the speculative motive."),
   ("Shift or move along?", "Money supply change shifts MS. Income change shifts LP."),
   ("Draw the horizontal LP for the trap.", "Then say monetary policy loses effect and fiscal policy is needed."),
   ("Contrast the two theories.", "Liquidity preference: money market, a stock. Loanable funds: saving and investment, flows."),
   ("Evaluate with practice.", "In reality central banks set the policy rate directly, and expectations matter.")],
  [("Motives", "The speculative demand for money is inversely related to the interest rate, because a lower rate means higher bond prices and a greater expectation of a fall."),
   ("Equilibrium", "The interest rate is determined where the liquidity preference curve meets the money supply curve."),
   ("QE", "An increase in the money supply could lower the interest rate, which may raise investment and consumption."),
   ("Trap", "In a liquidity trap the LP curve is horizontal, so additional money does not reduce the interest rate further."),
   ("Contrast", "Keynes argued that income, not the interest rate, brings saving and investment into balance.")],
  [CW["define"], CW["explain"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- Money market ---------- */
const MX = (m) => 70 + m * 6.4, MY = (r) => 310 - r * 27;
const lpR = (m, sh) => { const x = Math.max(0, Math.min(100, m - sh)); return 1.5 + 9 * Math.pow((100 - x) / 100, 2.2); };
function mmDraw(s) {
  let o = axes(70, 310, 730, 30, "Quantity of money", "Interest rate (%)"); [0, 2, 4, 6, 8, 10].forEach((r) => (o += SV.text(64, MY(r) + 4, r, "sm", { "text-anchor": "end" })));
  const pts = []; for (let m = 0; m <= 99; m += 1) pts.push([MX(m), MY(lpR(m, s.sh))]);
  o += SV.path(Lib.ptsPath(pts), "c2") + tag(MX(99) - 4, MY(lpR(99, s.sh)) - 8, "LP", "t2", 1, "end");
  if (s.l > 0) { o += SV.line(MX(70), MY(2.2), MX(100), MY(2.2), "c4 dash", op(s.l)) + tag(MX(85), MY(2.2) - 12, "liquidity trap: flat", "t4", s.l, "middle"); }
  const r = lpR(s.m, s.sh);
  if (s.o > 0) o += SV.line(MX(s.o), 310, MX(s.o), 40, "c1 dash", op(0.45)) + tag(MX(s.o) + 4, 54, "MS₁", "t1", 0.7);
  o += SV.line(MX(s.m), 310, MX(s.m), 40, "c1") + tag(MX(s.m) + 4, 50, "MS", "t1");
  o += SV.circle(MX(s.m), MY(r), 7, "dot4") + SV.line(70, MY(r), MX(s.m), MY(r), "gr") + tag(76, MY(r) - 8, "r = " + Lib.fmtN(r, 1) + "%", "t4");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Money market: downward sloping liquidity preference, vertical money supply and the equilibrium interest rate">${mmDraw({ m: 50, o: 0, sh: 0, l: 0 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 340, label: "Money market with a vertical money supply, liquidity preference, a rise in the money supply and a liquidity trap", base: { m: 50, o: 0, sh: 0, l: 0 }, draw: mmDraw, tween: 1100, dwell: 5800, steps: [
  { cap: "<b>Liquidity preference.</b> The LP curve slopes down: at higher interest rates people hold less idle money, at lower rates more (the speculative motive, linked to bond prices).", s: { m: 50 } },
  { cap: "<b>Equilibrium.</b> The money supply is a vertical line set by the central bank and banks. The interest rate (about 3.5%) is where LP meets MS.", s: { m: 50 } },
  { cap: "<b>An increase in the money supply</b> (QE or lower reserve requirements) shifts MS right. People hold more money than they want, so they buy bonds, bond prices rise and the <b>interest rate falls</b> (to about 2.1%).", s: { m: 70, o: 50 } },
  { cap: "<b>The liquidity trap.</b> At very low rates bond prices are very high and people expect them to fall, so they hold money: LP becomes nearly <b>flat</b>. A further rise in MS hardly lowers the rate.", s: { m: 90, o: 70, l: 1 } },
  { cap: "<b>A rise in income</b> raises transactions demand, so LP shifts right and the interest rate rises for the same money supply.", s: { m: 50, o: 0, sh: 15, l: 0 } },
] });

/* ---------- Loanable funds ---------- */
const LX = (q) => 70 + q * 6.4, LYY = (r) => 310 - r * 30;
function lfDraw(s) {
  const sS = s.s, sD = s.d, Q = 50 + 0.5 * (sS + sD), r = 1 + 0.08 * (Q - sS);
  let o = axes(70, 310, 730, 30, "Loanable funds (saving and investment)", "Interest rate (%)"); [0, 2, 4, 6, 8, 10].forEach((v) => (o += SV.text(64, LYY(v) + 4, v, "sm", { "text-anchor": "end" })));
  if (s.o > 0) { o += SV.line(LX(0), LYY(1 + 0.08 * (0 - 0)), LX(100), LYY(1 + 0.08 * 100), "c3 dash", op(0.4)) + SV.line(LX(0), LYY(9), LX(100), LYY(1), "c1 dash", op(0.4)); }
  o += SV.line(LX(0), LYY(1 + 0.08 * (0 - sS)), LX(100), LYY(1 + 0.08 * (100 - sS)), "c3") + tag(LX(100) - 4, LYY(1 + 0.08 * (100 - sS)) - 8, "Supply of funds (saving)", "t3", 1, "end");
  o += SV.line(LX(0), LYY(9 - 0.08 * (0 - sD)), LX(100), LYY(9 - 0.08 * (100 - sD)), "c1") + tag(LX(100) - 4, LYY(9 - 0.08 * (100 - sD)) + 18, "Demand for funds (investment)", "t1", 1, "end");
  o += SV.circle(LX(Q), LYY(r), 7, "dot4") + SV.line(LX(Q), LYY(r), LX(Q), 310, "gr") + SV.line(70, LYY(r), LX(Q), LYY(r), "gr") + tag(76, LYY(r) - 8, "r = " + Lib.fmtN(r, 1) + "%", "t4") + tag(LX(Q), 330, "Q = " + Lib.fmtN(Q, 0), "t4", 1, "middle");
  return o;
}
Lib.stepper($("#stL"), { w: 760, h: 345, label: "Loanable funds market: supply of saving, demand for investment funds, a rise in saving and a rise in investment demand", base: { s: 0, d: 0, o: 0 }, draw: lfDraw, tween: 1100, dwell: 5800, steps: [
  { cap: "<b>Equilibrium.</b> Households, firms and others supply funds by saving (the supply slopes up). Firms and others borrow to invest (the demand slopes down). The interest rate (5%) balances them.", s: {} },
  { cap: "<b>More saving.</b> A rise in saving shifts the supply of funds right. The interest rate falls and more is borrowed and invested.", s: { s: 20, o: 1 } },
  { cap: "<b>Higher investment demand.</b> If business confidence rises, firms want to borrow more at every rate. Demand shifts right and the interest rate rises (about 6.6%).", s: { s: 20, d: 20, o: 1 } },
  { cap: "<b>The Keynesian objection.</b> Keynes argued the interest rate need not make saving equal to investment, because people save and invest for different reasons; income would change to bring them into balance (the paradox of thrift).", s: { s: 20, d: 20, o: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labMM() {
  if (!$("#sm") || !$("#iy")) return;
  const m = +$("#sm").value, sh = +$("#iy").value, r = lpR(m, sh), bp = 100 / (r / 3.5);
  $("#r1").textContent = Lib.fmtN(r, 1) + "%"; $("#r2").textContent = Lib.fmtN(bp, 0); $("#r3").textContent = r < 2.3 ? "Liquidity trap zone" : r > 6 ? "Tight money" : "Normal";
  $("#rv").textContent = r < 2.3 ? `At about ${Lib.fmtN(r, 1)}% the LP curve is almost flat, so more money barely cuts the rate. Monetary policy is weak and fiscal policy is more effective.` : `At a money supply of ${m} and income shift ${sh}, the interest rate is ${Lib.fmtN(r, 1)}%. Bond prices (index 100 at 3.5%) are at ${Lib.fmtN(bp, 0)}: lower rates mean higher bond prices.`;
  const X = (v) => 40 + v * 3.5, Y = (v) => 270 - v * 22; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 292, "Quantity of money", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Interest rate (%)", "sm");
  const pts = []; for (let x = 0; x <= 99; x += 1) pts.push([X(x), Y(lpR(x, sh))]); o += SV.path(Lib.ptsPath(pts), "c2") + SV.line(X(m), 270, X(m), 30, "c1") + SV.circle(X(m), Y(r), 7, "dot4") + tag(X(m) + 8, Y(r) - 10, "r = " + Lib.fmtN(r, 1) + "%", "t4");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sm", label: "Money supply ", min: 20, max: 98, step: 2, value: 50, fmt: (v) => v, onInput: labMM });
Lib.slider($("#g2"), { id: "iy", label: "Rise in income (shifts LP right) ", min: 0, max: 20, step: 2, value: 0, fmt: (v) => v, onInput: labMM });
labMM();

/* ---------- Lab 2 ---------- */
function labLF() {
  if (!$("#ls") || !$("#ld")) return;
  const sS = +$("#ls").value, sD = +$("#ld").value, Q = 50 + 0.5 * (sS + sD), r = 1 + 0.08 * (Q - sS), r0 = 5, Q0 = 50;
  $("#t1").textContent = Lib.fmtN(r, 1) + "%"; $("#t2").textContent = Lib.fmtN(Q, 0); $("#t3").textContent = sS === 0 && sD === 0 ? "None" : r < r0 - 0.1 ? "Lower rate" : r > r0 + 0.1 ? "Higher rate" : "Rate unchanged";
  $("#tv").textContent = sS > 0 && sD === 0 ? `More saving lowers the interest rate to ${Lib.fmtN(r, 1)}% and raises investment from ${Q0} to ${Lib.fmtN(Q, 0)}. This is the classical view; Keynes warns that a rise in saving may cut spending and income instead.` : sD > 0 && sS === 0 ? `More demand for investment funds raises the interest rate to ${Lib.fmtN(r, 1)}% and the quantity of funds lent to ${Lib.fmtN(Q, 0)}.` : sS === 0 && sD === 0 ? "Base case: the interest rate is 5% and 50 units are lent." : `Saving and investment demand both change: the rate is ${Lib.fmtN(r, 1)}% and funds lent are ${Lib.fmtN(Q, 0)}.`;
  const X = (q) => 40 + q * 3.5, Y = (v) => 270 - v * 25; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 292, "Loanable funds", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Interest rate (%)", "sm");
  o += SV.line(X(0), Y(1 - 0.08 * sS), X(100), Y(1 + 0.08 * (100 - sS)), "c3") + SV.line(X(0), Y(9 + 0.08 * sD), X(100), Y(9 - 0.08 * (100 - sD)), "c1") + SV.circle(X(Q), Y(r), 7, "dot4") + tag(X(Q) + 8, Y(r) - 10, "r = " + Lib.fmtN(r, 1) + "%", "t4");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "ls", label: "Rise in saving (shifts supply right) ", min: 0, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labLF });
Lib.slider($("#g4"), { id: "ld", label: "Rise in investment demand (shifts demand right) ", min: 0, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labLF });
labLF();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which motive for holding money is it?", ["Transactions", "Precautionary", "Speculative"],
  [("Keeping money to pay for the weekly shop", 0), ("Holding cash in case the car breaks down", 1), ("Holding money because bond prices are expected to fall", 2), ("Keeping funds to pay rent next week", 0), ("Holding a rainy-day balance for unexpected medical bills", 1), ("Waiting in cash because interest rates look likely to rise", 2), ("A shop keeping cash for wages on Friday", 0), ("Holding extra money when interest rates are very low", 2)],
  "Transactions and precautionary depend on income. Speculative depends on the interest rate.") + MATCH([
  ["Liquidity preference", "The demand for money for transactions, precautionary and speculative reasons"],
  ["Active balances", "Money held for transactions and precautionary motives"],
  ["Idle balances", "Money held for the speculative motive"],
  ["Liquidity trap", "A flat LP curve at very low rates: extra money does not reduce rates"],
  ["Loanable funds", "Supply of and demand for funds from saving and investment"],
  ["Paradox of thrift", "A rise in saving that reduces income and so total saving"]]) + ORDER(
  "Put the effect of QE on the interest rate in order.",
  ["The central bank buys bonds and creates money", "The money supply rises, MS shifts right", "People hold more money than they wish and buy bonds", "Bond prices rise", "The interest rate falls"],
  "Bond prices and interest rates move in opposite directions.") + CALC([
  {"q": "A bond pays a fixed $50 a year. The interest rate is 5%. Calculate the price of the bond ($).", "a": 1000, "unit": "$", "tol": 0.5, "hint": "Price = payment ÷ interest rate.", "sol": "50 ÷ 0.05 = <b>$1,000</b>."},
  {"q": "The interest rate falls to 4%. Calculate the new price of the same bond ($).", "a": 1250, "unit": "$", "tol": 0.5, "hint": "50 ÷ 0.04.", "sol": "50 ÷ 0.04 = <b>$1,250</b>: the bond price rises when the rate falls."},
  {"q": "The central bank buys $30bn of bonds and the money supply rises by the same amount. If the credit multiplier is 8, by how much could the total money supply eventually rise ($bn)?", "a": 240, "unit": "$bn", "tol": 0.5, "hint": "30 × 8.", "sol": "<b>$240bn</b> (at most)."},
  {"q": "In a loanable funds market the interest rate is 6% and inflation is 2.5%. Calculate the real interest rate (%).", "a": 3.5, "unit": "%", "tol": 0.05, "hint": "Nominal minus inflation.", "sol": "<b>3.5%</b>."}]) + MCQ([
  ("In Keynes's theory, the speculative demand for money depends mainly on:", ["Income", "The interest rate", "The price level", "The exchange rate"], 1, "Idle balances respond to the interest rate and expectations about bond prices."),
  ("A rise in the interest rate causes bond prices to:", ["Rise", "Fall", "Stay the same", "Double"], 1, "Bond prices and interest rates are inversely related."),
  ("What is a liquidity trap?", ["A situation where a rise in the money supply does not lower interest rates", "High inflation", "A budget surplus", "A fixed exchange rate"], 0, "People hold the extra money instead of buying bonds, so rates cannot fall further."),
  ("Which is a feature of the loanable funds theory?", ["The interest rate balances saving and investment", "Money supply is vertical", "Income has no effect", "Interest is the reward for liquidity"], 0, "Saving supplies funds and investment demands them."),
  ("A rise in income will shift the liquidity preference curve:", ["Left", "Right", "Not at all", "To a vertical line"], 1, "Transactions demand rises with income, so more money is wanted at each rate.")
], "qz1") + CARDS([
  ("Liquidity preference", "Demand for money: transactions, precautionary, speculative."),
  ("Active balances", "Transactions and precautionary money; depend on income."),
  ("Idle balances", "Speculative money; depend on interest rates."),
  ("Liquidity trap", "Flat LP at low rates: extra money does not lower the rate."),
  ("Bond price and interest rate", "Move in opposite directions."),
  ("Loanable funds", "Saving supplies, investment demands: rate balances them."),
  ("Paradox of thrift", "More saving may reduce income and total saving."),
  ("Keynesian interest rate", "Determined by the money market, not saving and investment.")]) + MCQ(mc_exam)

build("sy947", "liquidity-preference-interest-rates", "Liquidity Preference and Interest Rate Determination", EY,
  "9.4.7 to 9.4.8: the motives for holding money, the Keynesian money market and the liquidity trap, and the loanable funds theory of the interest rate. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
