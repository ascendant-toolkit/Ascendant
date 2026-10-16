"""Syllabus 9.4.4-9.4.5 Commercial banks, credit creation and the causes of changes in the money supply. Run: python3 tools/artifact-kit/mk_sy944.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.4.4 to 9.4.5"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Commercial banks</b> take deposits, make loans and provide payment services, acting as <b>financial intermediaries</b> between savers and borrowers. They must balance three objectives, <b>liquidity</b>, <b>security</b> and <b>profitability</b>, which conflict, so they hold assets of different kinds and keep a <b>reserve ratio</b> and a <b>capital ratio</b>. Because banks lend out part of every deposit, they <b>create credit</b> and so most of the money supply, with a <b>bank credit multiplier</b> of 1 ÷ reserve ratio. The money supply also changes because of the <b>central bank</b>, <b>government deficit financing</b>, <b>quantitative easing</b> and the <b>balance of payments</b>.</p></div>

  <h2>1 · Functions of commercial banks (9.4.4)</h2>
  <ul>
    <li><b>Deposit accounts:</b> demand (current) accounts that can be withdrawn on request, and savings accounts that pay interest and may need notice.</li>
    <li><b>Lending:</b> overdrafts (short-term, flexible), loans and mortgages (longer term).</li>
    <li><b>Financial intermediation:</b> bringing savers and borrowers together, borrowing short and lending long (maturity transformation), and pooling and spreading risk.</li>
    <li><b>Payment services:</b> cheques, cards and transfers.</li>
    <li><b>Credit creation:</b> lending creates new deposits.</li>
    <li><b>Holding assets:</b> cash, securities, loans, deposits and equity, as shown in the bank's balance sheet.</li>
  </ul>
  <h3>A bank's balance sheet</h3>
  <div class="tw"><table class="t">
    <tr><th>Assets (what the bank owns or is owed)</th><th>Liquidity</th><th>Profitability</th></tr>
    <tr><td><b>Cash and balances at the central bank</b></td><td>Highest</td><td>Lowest (little or no interest)</td></tr>
    <tr><td><b>Money at call and short notice</b></td><td>Very high</td><td>Low</td></tr>
    <tr><td><b>Bills and short-term securities</b></td><td>High</td><td>Low to medium</td></tr>
    <tr><td><b>Investments (bonds)</b></td><td>Medium</td><td>Medium</td></tr>
    <tr><td><b>Advances (loans to customers)</b></td><td>Lowest</td><td>Highest</td></tr>
  </table></div>
  <p><b>Liabilities</b> are what the bank owes: customer <b>deposits</b> (the largest part) and shareholders' funds (<b>equity</b> or capital).</p>
  <div class="grid2">
    <div class="card"><h3>Reserve ratio</h3><div class="formula">reserve ratio = cash reserves ÷ deposits</div><p>The share of deposits kept in liquid form. Set by the bank for safety and sometimes by the central bank. A <b>higher</b> ratio makes the bank safer but cuts lending and profit.</p></div>
    <div class="card"><h3>Capital ratio</h3><div class="formula">capital ratio = capital ÷ risk-weighted assets</div><p>How much of the bank's risky assets are funded by shareholders rather than depositors. A higher ratio helps the bank absorb losses; regulators set minimums.</p></div>
  </div>
  <h3>The three objectives of a commercial bank</h3>
  <div class="tw"><table class="t">
    <tr><th>Objective</th><th>Meaning</th><th>Conflict</th></tr>
    <tr><td><b>Liquidity</b></td><td>Able to meet withdrawals on demand</td><td>Liquid assets earn little: conflicts with profitability</td></tr>
    <tr><td><b>Security</b></td><td>Low risk of losing money lent</td><td>Safe borrowers pay lower interest: conflicts with profitability</td></tr>
    <tr><td><b>Profitability</b></td><td>Earning a return for shareholders</td><td>Higher profit comes from riskier, less liquid loans</td></tr>
  </table></div>
  <div class="tip"><b class="h">The financial crisis link</b>Banks that took excessive risks, lent with too little security and held too little capital found that they could not meet withdrawals when asset values fell. Regulation of liquidity and capital ratios aims to prevent this.</div>

  <h2>2 · Credit creation and the bank credit multiplier</h2>
  <p>When a customer deposits $1,000 and the bank keeps 10% as reserves, it can lend $900. The borrower spends it, the seller deposits it in a bank, and that bank can lend 90% of it. The process continues, and total deposits expand.</p>
  <div class="formula">credit multiplier = 1 ÷ reserve ratio &nbsp; · &nbsp; maximum total deposits = initial deposit × multiplier</div>
  <div id="pic1" class="card"></div>
  <ul>
    <li>With a 10% reserve ratio the multiplier is 10, so a $1,000 deposit can support $10,000 of deposits (the original $1,000 plus $9,000 of new money).</li>
    <li>If people keep some cash (a <b>cash drain</b>) the multiplier is smaller: <b>1 ÷ (reserve ratio + cash ratio)</b>.</li>
    <li>If the reserve ratio rises from 5% to 10% the multiplier halves.</li>
    <li>The actual amount depends on the <b>demand for loans</b>, banks' willingness to lend and confidence.</li>
  </ul>

  <h2>3 · The central bank</h2>
  <ul>
    <li><b>Issues notes and coins</b> (the monopoly issuer of currency).</li>
    <li><b>Banker to the government</b> and <b>banker to commercial banks</b>: they hold reserve accounts there.</li>
    <li><b>Lender of last resort</b> to banks facing a shortage of liquidity.</li>
    <li><b>Implements monetary policy:</b> sets interest rates, controls the money supply, conducts quantitative easing.</li>
    <li><b>Regulates banks and protects financial stability:</b> liquidity and capital requirements, stress tests.</li>
    <li>Unlike a commercial bank, it does not aim to maximise profit and does not take deposits from the general public.</li>
  </ul>

  <h2>4 · What changes the money supply in an open economy (9.4.5)</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>How the money supply changes</th></tr>
    <tr><td><b>Commercial bank credit creation</b></td><td>More lending raises deposits and the money supply. Causes: a lower reserve ratio, more demand for loans, lower interest rates, more confidence.</td></tr>
    <tr><td><b>The central bank</b></td><td>Lower interest rates, lower reserve requirements or buying securities in the open market raise the money supply; the opposite actions reduce it.</td></tr>
    <tr><td><b>Government deficit financing</b></td><td>Borrowing from commercial banks or the central bank (or printing money) raises the money supply. Borrowing from the non-bank public mainly transfers existing money, so there is little change.</td></tr>
    <tr><td><b>Quantitative easing</b></td><td>The central bank buys assets (mostly government bonds) from the non-bank sector with newly created money. This raises bank deposits and reserves.</td></tr>
    <tr><td><b>The balance of payments</b></td><td>A surplus (exports and capital inflows) brings foreign currency that is exchanged for domestic currency, raising the money supply (unless the central bank sterilises it). A deficit has the opposite effect. The money flow between domestic and foreign residents is the <b>total currency flow</b>.</td></tr>
  </table></div>
'''

watch = '''
  <h2>1 · Credit creation round by round</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stC"></div>
  <h2>2 · A bank's balance sheet and the three objectives</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · The credit multiplier</h2>
  <p>Set the first deposit, the reserve ratio and how much of each loan leaks out as cash. The lab shows the multiplier and the total money created.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Credit multiplier</small><strong id="r1"></strong></div><div><small>Maximum total deposits</small><strong id="r2"></strong></div><div><small>New money created</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of the initial deposit and the total deposits created"></svg></div></div></div>

  <h2>Lab 2 · What changes the money supply?</h2>
  <p>Pick an event to see the likely effect on the money supply and why.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Does the money supply rise or fall?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put credit creation in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The 2008 financial crisis and bank capital", "Many banks held too little capital and too many illiquid assets. When mortgage losses hit, markets stopped lending to them, and governments and central banks had to rescue banks. Regulators raised capital and liquidity requirements afterwards.", "the conflict between profitability and security and liquidity, and the role of the central bank as lender of last resort.") +
rw("Northern Rock, 2007", "A British bank that funded mortgage lending from wholesale markets rather than deposits. When markets froze, depositors queued to withdraw their money, and the Bank of England had to lend and the government to guarantee deposits.", "a bank run and the lender of last resort in action. A good example of liquidity risk.") +
rw("Quantitative easing in the 2010s", "The Bank of England and other central banks created hundreds of billions in new money to buy government bonds from pension funds and banks. Bank reserves and deposits rose, but bank lending to firms rose far less than expected.", "a cause of change in the money supply (and the limits of its effect on lending).") +
rw("Capital inflows and the money supply", "When a country receives large foreign investment or has a big current account surplus, its central bank buys the foreign currency with domestic currency, increasing the money supply. Some central banks (such as China's) offset this by selling bonds.", "the balance of payments as a cause of money supply growth, and sterilisation.")
)

mc_exam = [
  ("A world financial crisis was partly linked to the actions of commercial banks. Which actions could have led to it? (May/June 2024 · 31 · Q16, reworded)", ["Being subject to tight controls by the central bank over credit creation", "Holding reserves above the agreed reserve ratio", "Taking excessive risks by demanding too little security from borrowers", "Widening the gap in favour of assets over liabilities"], 2, "Lending with too little security meant losses when borrowers defaulted."),
  ("Which statement applies to a central bank and to a commercial bank? (Feb/March 2023 · 32 · Q18, reworded)", ["Both issue bank notes", "Both are the lender of last resort", "A commercial bank aims to maximise profit, a central bank does not", "A central bank receives deposits from the public"], 2, "Central banks pursue policy objectives and stability, not profit."),
  ("The cash deposit ratio of banks changed from 5% to 10%. What will be the result? (Oct/Nov 2021 · 32 · Q27, reworded)", ["Bank deposits will fall by 10%", "Bank deposits will rise by 5%", "The credit multiplier will fall by 50%", "The credit multiplier will rise by 5%"], 2, "The multiplier is 1 ÷ ratio, so it falls from 20 to 10: a 50% fall."),
  ("In which context relevant to growth in the money supply is the term 'total currency flow' used? (May/June 2022 · 32 · Q24, reworded)", ["Between central banks and commercial banks", "Between central banks and governments", "Between domestic residents and foreign residents", "Between the general public and the financial sector"], 2, "Total currency flow is the money flowing in and out of the country through the balance of payments."),
  ("A central bank buys government securities from the private sector. What is the likely effect on long-term interest rates and the money supply? (May/June 2020 · 31 · Q26, reworded)", ["Long-term rates fall, money supply falls", "Long-term rates fall, money supply rises", "Long-term rates rise, money supply falls", "Long-term rates rise, money supply rises"], 1, "Buying securities raises their price (so yields fall) and puts new money into the economy."),
  ("Which policy does a central bank carry out to pursue quantitative easing? (May/June 2021 · 31 · Q26, reworded)", ["Buying long-term government debt from the public", "Buying short-term government debt from the public", "Selling long-term government debt to the public", "Selling short-term government debt to the public"], 0, "QE is the purchase of long-term assets, mainly government bonds, with newly created money."),
  ("A central bank sells securities on the open market. What does Keynesian theory predict? (Oct/Nov 2020 · 31 · Q26, reworded)", ["A fall in the price level", "A fall in unemployment", "A rise in the price level", "A rise in the rate of interest"], 3, "Selling securities reduces the money supply, so the interest rate rises.")
]

exam = exam_page("commercial banks, credit creation and the money supply",
  "We searched the A Level Economics papers in the folder (2020 to 2025). The roles of banks and the effects of quantitative easing appear as 12, 13 and 25 mark Paper 4 questions. Reworded questions are below, with a practice question and seven Paper 3 multiple choice questions.",
  [("Essay, 25 marks", "1", "Oct/Nov 2020 (41) Q6"), ("Essay parts, 12 and 13 marks", "4", "May/June 2020 (42) Q7(b); May/June 2021 (42) Q7(a); May/June 2022 (41, 43) Q6(b); Oct/Nov 2022 (41) Q5(b)"), ("Practice question", "1", "Credit creation"), ("Multiple choice (Paper 3)", "7 shown below", "2020 to 2024")],
  [
  eq("Based on May/June 2022 · 9708/41 and 43 · Q6(b)", "13 marks", "Discuss the role and importance of the commercial banks in a developed economy.",
     ["Key roles: safekeeping of funds, lending to consumers and firms, financial intermediation and making payments easy.",
      "Link each to the economy: savings finance investment and long-run growth; loans to consumers raise AD, output and jobs; easier payments encourage specialisation and trade; credit creation provides most of the money supply.",
      "Evaluation: the importance depends on stability (banking crises have large costs), regulation, competition and how much they lend to productive uses rather than asset purchases."],
     "Four roles. Link each to growth or stability. Then the risks of banking. Judge importance."),
  eq("Based on Oct/Nov 2022 · 9708/41 · Q5(b)", "13 marks", "'The most important aim of a central bank is to control the money supply, while the most important aim of a commercial bank is to maximise profit.' Discuss the extent to which these two aims can be achieved together.",
     ["Central bank roles: monetary policy to help meet an inflation target and financial stability, using interest rates, the money supply and other instruments.",
      "Commercial bank profit comes from lending, which creates money, so profit-seeking lending expands the money supply while the central bank may want to limit it. Conflict: a bank wants more loans, the central bank may want fewer.",
      "Compatible: stable money and a healthy banking system support profit; regulation (reserve and capital ratios) steers banks without destroying profit; interest rate changes align incentives.",
      "A conclusion on whether the two can be reconciled, and when they conflict (booms, financial risk-taking)."],
     "Define each aim. Where they conflict. Where they fit. Role of regulation. Conclude."),
  eq("Based on May/June 2021 · 9708/42 · Q7(a)", "12 marks", "Explain what is meant by quantitative easing (QE) and consider whether it is an effective policy to use in a recession.",
     ["QE: the central bank creates money electronically and uses it to buy assets, mainly long-term government bonds, from banks and other holders. This raises their price, lowers long-term interest rates, increases bank reserves and the money supply, and aims to raise lending, spending and asset prices.",
      "Effectiveness: useful when interest rates are near zero and conventional policy has run out; can stabilise financial markets and boost confidence; wealth effects from higher asset prices.",
      "Limits: banks may hold the reserves rather than lend; weak demand for loans; benefits asset owners (inequality); risk of inflation later; lags; may not reach the real economy."],
     "Define QE and the mechanism. Why it is used. Three reasons it might fail. Judge."),
  eq("Based on May/June 2020 · 9708/42 · Q7(b)", "13 marks", "Discuss the impact on the economy of the introduction of quantitative easing (QE) by the central bank.",
     ["Impact on interest rates, bank reserves, lending, AD, asset prices, the exchange rate and inflation.",
      "Positive: lower borrowing costs, higher asset prices raise wealth and spending, a lower exchange rate raises exports, avoids deflation.",
      "Negative: little effect on lending in a recession, inequality from asset price rises, risk of asset bubbles and inflation, difficulty reversing it.",
      "A reasoned conclusion on net impact."],
     "Chain from QE to interest rates, lending and AD. Exchange rate effect. Costs. Judge."),
  eq("Based on Oct/Nov 2020 · 9708/41 · Q6", "25 marks", "'The use of quantitative easing has the same effect on the economy as Keynesian fiscal demand management. Both policies create employment in the short run at the expense of inflation in the long run.' How far would you support this view?",
     ["Explain QE (monetary) and Keynesian fiscal policy (government spending or lower taxes): both raise AD.",
      "Similarities: both can raise output and jobs in a recession and risk inflation if overdone; both can raise the national debt or central bank balance sheet.",
      "Differences: fiscal policy works directly through spending and the multiplier; QE works indirectly through interest rates and asset prices and may not raise lending; fiscal policy affects the budget; effects on distribution differ.",
      "Evaluation of 'inflation in the long run': depends on spare capacity, velocity and expectations; QE after 2008 did not cause high inflation for a decade."],
     "Explain both. Compare effects and transmission. Test the claim about inflation. Judge."),
  eq("Practice (not a past paper question)", "8 marks", "A bank receives a new deposit of $2,000 and its reserve ratio is 10%. Explain how banks can use this deposit to expand the money supply, and calculate the maximum total increase in deposits.",
     ["Calculation: multiplier 1 ÷ 0.1 = 10; maximum total deposits = 2,000 × 10 = $20,000, of which $18,000 is new money.",
      "Process: the bank keeps $200 and lends $1,800; the borrower spends it and the recipient deposits it in a bank that lends 90% of it, and so on.",
      "Limits: cash drain, banks holding more reserves than required, weak demand for loans, central bank controls."],
     "Number first. Then the rounds. Then limits.",
     [[("k", "Credit creation happens because banks need to keep only part of deposits as reserves and can lend the rest. The credit multiplier is 1 divided by the reserve ratio, which is 1 ÷ 0.1 = 10."), ("a", "A $2,000 deposit could therefore support up to $20,000 of deposits, so $18,000 of new money could be created.")],
      [("n", "In the first round the bank keeps $200 and lends $1,800. The borrower spends this and the recipient deposits it in a bank, which keeps $180 and lends $1,620, and the process continues with each round smaller than the last, until the total reaches the maximum."), ("e", "In practice the increase is smaller if people keep some of the loans as cash, if banks hold more than the required reserves, or if there is little demand for loans, and the central bank can restrict the process by raising the reserve requirement or interest rates.")]])
  ],
  )

tips = tips_html(
  [("Learn the three bank objectives and the conflict.", "Liquidity, security and profitability. Liquid and safe assets earn less."),
   ("Draw the balance sheet logic.", "Cash is most liquid and least profitable. Loans are the opposite."),
   ("Credit multiplier = 1 ÷ reserve ratio.", "Show the working. Allow for cash drain if told."),
   ("Distinguish a central bank from a commercial bank.", "Central bank: lender of last resort, issues notes, implements policy, no profit motive."),
   ("List causes of money supply change.", "Credit creation, central bank, deficit financing, QE, the balance of payments."),
   ("For QE, say who is buying what.", "The central bank creates money and buys bonds, which lowers long-term rates and raises reserves."),
   ("Evaluate QE with lending and inequality.", "Banks may not lend, and asset holders gain most.")],
  [("Roles", "Commercial banks act as financial intermediaries, taking deposits from savers and lending to borrowers."),
   ("Conflict", "Holding more liquid assets increases security but reduces profitability, so the three objectives conflict."),
   ("Multiplier", "With a reserve ratio of 10% the credit multiplier is 10, so a $1,000 deposit could support $10,000 of deposits."),
   ("QE", "Quantitative easing could increase the money supply, but if banks do not lend the effect on spending may be small."),
   ("Open economy", "A surplus on the balance of payments could increase the money supply because foreign currency is exchanged for domestic currency.")],
  [CW["define"], CW["explain"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- Credit creation rounds ---------- */
function roundsDraw(s) {
  const D = 1000, r = 0.1, n = Math.round(s.n), pts = []; let tot = 0, o = SV.line(60, 280, 720, 280) + SV.text(720, 300, "Round of lending", "sm", { "text-anchor": "end" }) + tag(60, 26, "New deposit created in each round ($)", "t1");
  for (let i = 0; i < n && i < 12; i++) { const v = D * Math.pow(1 - r, i); tot += v; const h = v / D * 180, x = 70 + i * 52; o += SV.rect(x, 280 - h, 40, h, i === 0 ? "f1" : "f3") + tag(x + 20, 280 - h - 6, Lib.fmtN(v, 0), "t1", 1, "middle") + SV.text(x + 20, 296, i + 1, "sm", { "text-anchor": "middle" }); }
  const msg = n >= 12 ? "Total after many rounds approaches $" + Lib.fmtN(D / r, 0) + " = deposit × 1 ÷ reserve ratio" : "Running total of deposits: $" + Lib.fmtN(tot, 0);
  return o + tag(380, 56, msg, "t4", 1, "middle");
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 320" role="img" aria-label="Bars of the deposits created in successive rounds of lending with a 10 percent reserve ratio">${roundsDraw({ n: 12 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 320, label: "Rounds of lending after a 1,000 dollar deposit with a 10 percent reserve ratio", base: { n: 0 }, draw: roundsDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>The first deposit.</b> A customer deposits $1,000. The bank keeps 10% ($100) as reserves.", s: { n: 1 } },
  { cap: "<b>Round 2.</b> The bank lends $900. The borrower spends it and the seller deposits $900 in a bank, which keeps $90 and lends $810.", s: { n: 3 } },
  { cap: "<b>The process continues.</b> Each round creates a deposit 10% smaller than the last. The deposits ($1,000, $900, $810, $729, ...) form a geometric series.", s: { n: 7 } },
  { cap: "<b>The total.</b> The sum of all deposits approaches $10,000: the first deposit times 1 ÷ 0.1 = 10. Of this, $9,000 is <b>new money created by lending</b>.", s: { n: 12 } },
] });

/* ---------- Balance sheet ---------- */
function bsDraw(s) {
  const cash = s.c, loans = s.l, dep = s.d, mx = 1000, h = (v) => v / mx * 190; let o = tag(100, 26, "Assets", "t1") + tag(480, 26, "Liabilities", "t4");
  o += SV.line(60, 260, 340, 260) + SV.line(440, 260, 720, 260);
  o += SV.rect(80, 260 - h(cash), 120, h(cash), "f3") + SV.text(140, 260 - h(cash) / 2 + 4, "Cash and reserves " + Lib.fmtN(cash, 0), "sm bd", { "text-anchor": "middle" });
  o += SV.rect(80, 260 - h(cash) - h(loans), 120, h(loans), "f4") + SV.text(140, 260 - h(cash) - h(loans) / 2 + 4, "Loans " + Lib.fmtN(loans, 0), "sm bd", { "text-anchor": "middle" });
  o += SV.rect(460, 260 - h(dep), 120, h(dep), "f1") + SV.text(520, 260 - h(dep) / 2 + 4, "Deposits " + Lib.fmtN(dep, 0), "sm bd", { "text-anchor": "middle" });
  if (s.t > 0) o += tag(380, 296, s.m, "t3", 1, "middle");
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 320, label: "A bank balance sheet changing as a deposit arrives and part of it is lent", base: { c: 0, l: 0, d: 0, t: 1, m: "" }, draw: bsDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>An empty balance sheet.</b> Assets (what the bank owns or is owed) must equal liabilities (what it owes).", s: { m: "assets = liabilities" } },
  { cap: "<b>A deposit.</b> A customer deposits $1,000. Deposits (a liability) rise by 1,000 and so does cash (an asset). The bank is fully liquid but earns nothing on the cash.", s: { c: 1000, d: 1000, m: "liquid and safe, but no profit" } },
  { cap: "<b>Lending.</b> To earn interest, the bank lends $900 and keeps $100 as reserves. Loans are the <b>most profitable</b> asset but the <b>least liquid</b>.", s: { c: 100, l: 900, d: 1000, m: "profitable, but less liquid and carries risk" } },
  { cap: "<b>The trade-off.</b> A higher reserve ratio makes the bank safer and more liquid but reduces profit. A lower reserve ratio raises profit but risks being unable to meet withdrawals.", s: { c: 100, l: 900, d: 1000, m: "liquidity versus profitability" } },
] });

/* ---------- Lab 1: multiplier ---------- */
function labCM() {
  if (!$("#dp") || !$("#rr") || !$("#cd")) return;
  const D = +$("#dp").value, r = +$("#rr").value / 100, c = +$("#cd").value / 100, k = 1 / (r + c), tot = D * k;
  $("#r1").textContent = Lib.fmtN(k, 1); $("#r2").textContent = "$" + Lib.fmtN(tot, 0); $("#r3").textContent = "$" + Lib.fmtN(tot - D, 0);
  $("#rv").textContent = `The multiplier is 1 ÷ (${Lib.fmtN(r, 2)} + ${Lib.fmtN(c, 2)}) = ${Lib.fmtN(k, 1)}. A deposit of $${D} could support up to $${Lib.fmtN(tot, 0)} of deposits, creating $${Lib.fmtN(tot - D, 0)} of new money. Raising the reserve ratio or the cash drain would reduce this.`;
  const mx = tot * 1.1, Y = (v) => 260 - v / mx * 210; let o = SV.line(40, 260, 400, 260);
  o += SV.rect(100, Y(D), 90, 260 - Y(D), "f1") + tag(145, Y(D) - 6, "$" + D, "t1", 1, "middle") + SV.text(145, 280, "Initial deposit", "sm bd", { "text-anchor": "middle" });
  o += SV.rect(240, Y(tot), 90, 260 - Y(tot), "f3") + tag(285, Y(tot) - 6, "$" + Lib.fmtN(tot, 0), "t3", 1, "middle") + SV.text(285, 280, "Total deposits", "sm bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "dp", label: "Initial deposit ($) ", min: 100, max: 2000, step: 100, value: 1000, fmt: (v) => v, onInput: labCM });
Lib.slider($("#g2"), { id: "rr", label: "Reserve ratio (%) ", min: 5, max: 30, step: 1, value: 10, fmt: (v) => v, onInput: labCM });
Lib.slider($("#g3"), { id: "cd", label: "Cash drain (% of loans kept as cash) ", min: 0, max: 20, step: 1, value: 0, fmt: (v) => v, onInput: labCM });
labCM();
btnTable("lbBtns", "lbOut", [
  ["Commercial banks lend more because confidence returns", "Money supply rises", "Credit creation increases: more loans create more deposits"],
  ["The central bank raises the required reserve ratio", "Money supply falls", "Banks can lend less, so the credit multiplier falls"],
  ["The central bank buys government bonds from pension funds (QE)", "Money supply rises", "New money is created and deposits and reserves rise"],
  ["The government borrows from the central bank to fund a deficit", "Money supply rises", "Newly created money is spent into the economy"],
  ["The government borrows from households by selling bonds", "Little change", "Existing money is transferred from savers to the government"],
  ["A large current account surplus and capital inflow", "Money supply rises", "Foreign currency is exchanged for domestic currency (unless sterilised)"],
  ["Capital flight and a current account deficit", "Money supply falls", "Domestic currency is exchanged for foreign currency"]
], ["Event", "Effect", "Why"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Does the event tend to raise or lower the money supply?", ["Raises it", "Lowers it"],
  [("The central bank cuts the required reserve ratio", 0), ("The central bank raises interest rates and sells bonds", 1), ("Quantitative easing", 0), ("Banks become fearful and cut lending", 1), ("A large rise in capital inflows (not offset)", 0), ("A current account deficit financed from reserves", 1), ("The government prints money to pay for spending", 0), ("Borrowers repay bank loans", 1)],
  "More credit creation, more central bank money or net foreign inflows raise the money supply.") + MATCH([
  ["Reserve ratio", "Cash reserves as a share of deposits"],
  ["Capital ratio", "Capital as a share of risk-weighted assets"],
  ["Credit multiplier", "1 ÷ reserve ratio: how much deposits expand"],
  ["Lender of last resort", "The central bank lending to banks short of liquidity"],
  ["Quantitative easing", "The central bank buying assets with new money"],
  ["Financial intermediation", "Channelling funds from savers to borrowers"]]) + ORDER(
  "Put credit creation in order.",
  ["A customer deposits cash in a bank", "The bank keeps a reserve and lends the rest", "The borrower spends the loan and the seller deposits it in a bank", "That bank keeps a reserve and lends part again", "Total deposits expand by a multiple of the original deposit"],
  "Each loan becomes a new deposit, so deposits grow in successive rounds.") + CALC([
  {"q": "The reserve ratio is 20%. Calculate the credit multiplier.", "a": 5, "tol": 0.01, "hint": "1 ÷ 0.2.", "sol": "<b>5</b>."},
  {"q": "A new deposit of $5,000 with a reserve ratio of 10% and no cash drain. Calculate the maximum total deposits ($).", "a": 50000, "unit": "$", "tol": 1, "hint": "5000 × 10.", "sol": "<b>$50,000</b>."},
  {"q": "The reserve ratio is 8% and the cash drain is 2% of loans. Calculate the credit multiplier.", "a": 10, "tol": 0.05, "hint": "1 ÷ (0.08 + 0.02).", "sol": "1 ÷ 0.10 = <b>10</b>."},
  {"q": "A bank has deposits of $800m and cash reserves of $64m. Calculate its reserve ratio (%).", "a": 8, "unit": "%", "tol": 0.05, "hint": "64 ÷ 800.", "sol": "<b>8%</b>."}]) + MCQ([
  ("Which asset of a bank is the most liquid?", ["Loans to customers", "Cash at the central bank", "Government bonds", "Buildings"], 1, "Cash is already money."),
  ("Why do the three objectives of a commercial bank conflict?", ["Liquid and safe assets earn lower returns than riskier and less liquid ones", "Banks cannot lend", "Customers do not deposit", "Central banks forbid profit"], 0, "More liquidity and security means less profit."),
  ("Which would reduce the credit multiplier?", ["A fall in the reserve ratio", "A rise in the reserve ratio", "A rise in lending", "A fall in interest rates"], 1, "The multiplier is 1 ÷ reserve ratio."),
  ("A government sells bonds to the non-bank public to finance a deficit. What is the effect on the money supply?", ["It rises sharply", "It falls sharply", "It changes little", "It doubles"], 2, "Money is transferred from savers to the government, then spent."),
  ("A role of the central bank that a commercial bank does not have is:", ["Taking deposits from households", "Being the lender of last resort", "Making loans to firms", "Charging interest on overdrafts"], 1, "Only the central bank can act as lender of last resort.")
], "qz1") + CARDS([
  ("Financial intermediary", "Brings savers and borrowers together."),
  ("Reserve ratio", "Cash reserves ÷ deposits."),
  ("Capital ratio", "Capital ÷ risk-weighted assets."),
  ("Credit multiplier", "1 ÷ reserve ratio."),
  ("Liquidity", "Ease of converting assets into cash."),
  ("Lender of last resort", "Central bank lends to banks short of cash."),
  ("Quantitative easing", "Central bank buys assets with newly created money."),
  ("Sterilisation", "Offsetting the effect of foreign currency flows on the money supply.")]) + MCQ(mc_exam)

build("sy944", "commercial-banks-credit-creation", "Commercial Banks, Credit Creation and the Money Supply", EY,
  "9.4.4 to 9.4.5: the functions and objectives of commercial banks, the reserve and capital ratios, the credit multiplier, the central bank and the causes of changes in the money supply. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
