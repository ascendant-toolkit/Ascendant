"""Builds IGCSE Economics 3.1.1 Money and 3.1.2 Banking and 3.2.1 Households. Run: python3 tools/artifact-kit/mk_ig31.py"""
from igtext import *

# ---------------------------------------------------------------- 3.1.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Money</span> is anything <b>generally accepted</b> as a means of payment for goods and services and for settling debts. It exists because <b>barter</b> (swapping goods directly) needs a <b>double coincidence of wants</b>, which is rare. Money solves this and makes trade, specialisation and saving possible.</p></div>

  <h2>Forms of money</h2>
  <div class="tw"><table class="t">
    <tr><th>Form</th><th>Description</th></tr>
    <tr><td><b>Commodity money</b></td><td>Goods with their own value, such as gold, silver, salt, shells</td></tr>
    <tr><td><b>Coins and notes</b> (cash)</td><td>Legal tender issued by the central bank; accepted by law</td></tr>
    <tr><td><b>Bank deposits</b></td><td>Money held in bank accounts, used with debit cards, transfers and cheques</td></tr>
    <tr><td><b>Electronic and digital money</b></td><td>Card payments, mobile payment apps, online transfers, and (not yet universal) cryptocurrencies</td></tr>
  </table></div>

  <h2>Functions of money</h2>
  <div class="tw"><table class="t">
    <tr><th>Function</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Medium of exchange</b></td><td>Accepted in payment for goods and services, avoiding barter</td><td>Paying for lunch with a note or card</td></tr>
    <tr><td><b>Measure of value (unit of account)</b></td><td>Prices are stated in money, so values can be compared</td><td>A phone costs $300 and a laptop $900</td></tr>
    <tr><td><b>Store of value</b></td><td>Money can be saved and used later, keeping its purchasing power (if inflation is low)</td><td>Savings in a bank account</td></tr>
    <tr><td><b>Method of deferred payment</b></td><td>Allows debts and credit to be settled in future</td><td>Loans, mortgages, hire purchase</td></tr>
  </table></div>

  <h2>Characteristics of good money</h2>
  <ul>
    <li><b>Acceptable:</b> widely trusted and accepted.</li>
    <li><b>Durable:</b> lasts without wearing out.</li>
    <li><b>Portable:</b> easy to carry.</li>
    <li><b>Divisible:</b> can be split into small amounts for small purchases.</li>
    <li><b>Scarce (limited in supply):</b> so it keeps its value.</li>
    <li><b>Uniform:</b> one unit is the same as another.</li>
    <li><b>Stable in value:</b> holds its purchasing power.</li>
  </ul>
'''
steppers = [
  ("The problem with barter", "--bad", ["A farmer has wheat but wants shoes", "The shoemaker wants fruit, not wheat", "No double coincidence of wants", "Trade is slow or fails", "Money solves the problem"]),
  ("How money helps trade", "--good", ["The farmer sells wheat for money", "The farmer uses the money to buy shoes", "Money acts as a medium of exchange", "Prices let everyone compare values", "Specialisation and trade grow"]),
]
lab1 = dict(title="Does it work as money?", intro="Score an item on the characteristics of money (1 = poor, 5 = excellent) and see whether it works as money.", rl=["Total score", "Verdict", "Weakest feature"],
  sliders=[("Acceptable", 1, 5, 1, 4, "v"), ("Durable", 1, 5, 1, 4, "v"), ("Portable", 1, 5, 1, 4, "v"), ("Divisible", 1, 5, 1, 4, "v"), ("Scarce / limited in supply", 1, 5, 1, 4, "v"), ("Stable in value", 1, 5, 1, 3, "v")],
  fn="const nm = ['Acceptable', 'Durable', 'Portable', 'Divisible', 'Scarce', 'Stable'], tot = v.reduce((a, b) => a + b, 0), lo = nm[v.indexOf(Math.min(...v))], vd = tot >= 24 ? 'Works well as money' : tot >= 18 ? 'Works, but with weaknesses' : 'Poor as money'; return { r: [tot + '/30', vd, lo], t: 'The item scores ' + tot + ' out of 30: ' + vd.toLowerCase() + '. Its weakest feature is ' + lo.toLowerCase() + '. For example, gold scores well on durability and scarcity but poorly on portability and divisibility; modern notes and digital money score well on portability and divisibility.', bars: nm.map((n, i) => [n, v[i], ['--accent', '--good', '--warn', '--bad', '--accent', '--good'][i]]) };")
lab2 = dict(title="Functions of money", intro="Pick an example to see which function of money it shows.", h1="Function", h2="Why",
  items=[("Buying a coffee with a card", "Medium of exchange", "Accepted in payment, no barter."), ("A price tag of $20", "Measure of value", "Prices let goods be compared."), ("Putting savings in a bank", "Store of value", "Keeps purchasing power for later."), ("Taking out a mortgage", "Deferred payment", "Pay later in money."), ("Comparing a $300 and a $900 phone", "Measure of value", "Values stated in money."), ("Paying wages at the end of the month", "Medium of exchange", "Payment accepted for work.")])
cl = [("Which <b>function of money</b> is each?", ["Medium of exchange", "Measure of value", "Store of value", "Deferred payment"], [("Paying for shopping with notes", 0), ("A shop's price list", 1), ("Saving money for next year", 2), ("Repaying a loan over 5 years", 3), ("Paying with a contactless card", 0), ("Comparing prices of two goods", 1)], "Four functions."),
      ("Is each a <b>good</b> or <b>poor</b> characteristic of money?", ["Good for money", "Poor for money"], [("Portable", 0), ("Durable", 0), ("Divisible", 0), ("Easily damaged", 1), ("Different in each unit", 1), ("Unlimited supply", 1)], "Characteristics of money.")]
match = [["Money", "Anything generally accepted as payment"], ["Barter", "Swapping goods directly"], ["Medium of exchange", "Used to pay for goods and services"], ["Store of value", "Can be saved for later"], ["Legal tender", "Money that must be accepted by law"], ["Divisible", "Can be split into small amounts"]]
order = ("Put the chain in order: <b>why money replaced barter</b>.", ["Barter needs a double coincidence of wants", "Trade was slow and difficult", "People adopted a common medium of exchange", "Goods were priced in money", "Trade and specialisation expanded"], "Money makes trade easier.")
calcs = [("A coat costs $80 and a hat costs $20. How many hats are worth one coat?", 4, "80 ÷ 20 = <b>4</b>.", None, None), ("Prices rise 5% in a year. $200 saved last year buys goods worth how many dollars of last year's goods? (200 ÷ 1.05, nearest whole number)", 190, "200 ÷ 1.05 ≈ <b>190</b>.", None, None)]
mcq = [("A function of money is:", ["Barter", "Medium of exchange", "Inflation", "Debt only"], 1, "Used to pay."), ("Barter needs:", ["A double coincidence of wants", "Banks", "Cards", "Interest"], 0, "Rare."), ("Which is a characteristic of good money?", ["Perishable", "Divisible", "Heavy", "Unlimited supply"], 1, "Small amounts."), ("Savings in a bank show money as a:", ["Medium of exchange", "Store of value", "Barter", "Tax"], 1, "Keep for later."), ("Legal tender is:", ["Any good", "Money that must be accepted by law", "Digital only", "Credit"], 1, "Required by law.")]
cards = [("Money", "Anything generally accepted as a means of payment."), ("Barter", "Exchanging goods directly without money."), ("Double coincidence of wants", "Two people each want what the other has."), ("Medium of exchange", "Function: accepted in payment."), ("Measure of value", "Function: prices stated in money."), ("Store of value", "Function: can be saved."), ("Deferred payment", "Function: debts settled in future."), ("Legal tender", "Money that must be accepted by law."), ("Divisibility", "Can be broken into small units.")]
exam_qs = [
  Q(1, "Define", 2, "Define money.", "Generally accepted means of payment.", "[K|Money is anything generally accepted] [K|as a means of payment for goods and services and to settle debts.]"),
  Q(2, "Identify", 2, "Identify two functions of money.", "Medium of exchange; measure of value; store of value; deferred payment.", "[K|Medium of exchange.] [K|Store of value (or measure of value).]"),
  Q(3, "Explain", 4, "Explain two characteristics of good money.", "Durable, portable, divisible, acceptable, scarce.", "[K|Money should be portable.] [N|People can carry it easily to pay for goods.] [K|Money should be divisible.] [N|It can be split into small amounts for low-priced goods.]"),
  Q(4, "Explain", 4, "Explain why money is better than barter.", "Double coincidence; measure of value; store.", "[K|Barter needs a double coincidence of wants, which is rare.] [N|Money is accepted by everyone, so trade is easy.] [N|It also gives a measure of value and a way to save.]"),
]
tips_ = [("Four functions.", "Exchange, value, store, deferred payment."), ("Link each function to an example.", "A card payment, a price tag, savings."), ("Characteristics: acceptable, durable, portable, divisible.", "Scarce and stable too."), ("Barter's problem: double coincidence.", "Say it.")]
real_items = [("Shell money", "Cowrie shells were once used as money in parts of Africa and Asia.", "Commodity money."), ("Contactless payments", "Mobile apps let people pay without cash, making money more digital.", "Electronic money."), ("Zimbabwe's hyperinflation", "When money lost its value, people turned to foreign currencies and barter.", "Stable value."), ("Cryptocurrencies", "Bitcoin is held by some as a store of value but its price swings widely.", "Stability of value.")]
review("ig-money", "b311", "3.1.1", "Money", "Forms, functions and characteristics of money. Syllabus 3.1.1.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Identify", "Explain"], real_items)

# ---------------------------------------------------------------- 3.1.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The banking system has two key parts. <b>Commercial banks</b> take deposits and make loans to households and firms, and provide payment services. The <b>central bank</b> is the government's bank and the banking system's regulator: it controls <b>interest rates and the money supply</b>, issues notes and coins, and acts as <b>lender of last resort</b>.</p></div>

  <h2>Commercial banks</h2>
  <ul>
    <li><b>Accept deposits</b> and provide safe places to save.</li>
    <li><b>Provide loans and overdrafts</b> to households and firms, charging interest.</li>
    <li><b>Operate payment systems:</b> accounts, cards, transfers.</li>
    <li><b>Offer advice and other services:</b> mortgages, insurance, currency exchange.</li>
    <li><b>Earn profit</b> from the gap between interest charged on loans and paid on deposits.</li>
  </ul>
  <p><b>Importance:</b> banks channel savings to investment, help firms grow and households smooth spending, and make payments easy.</p>

  <h2>Central banks</h2>
  <div class="tw"><table class="t">
    <tr><th>Role</th><th>What it means</th></tr>
    <tr><td><b>Issue notes and coins</b></td><td>Controls the supply of cash</td></tr>
    <tr><td><b>Government's bank</b></td><td>Holds government accounts, manages its borrowing</td></tr>
    <tr><td><b>Bankers' bank</b></td><td>Holds commercial banks' reserves; settles payments between them</td></tr>
    <tr><td><b>Lender of last resort</b></td><td>Lends to commercial banks in a crisis to prevent collapse</td></tr>
    <tr><td><b>Sets interest rates and manages the money supply</b></td><td>Monetary policy to control inflation and support growth</td></tr>
    <tr><td><b>Regulates and supervises banks</b></td><td>Keeps the banking system safe and stable</td></tr>
    <tr><td><b>Manages exchange rate and reserves</b></td><td>Buys and sells foreign currency</td></tr>
  </table></div>
  <p class="note">Examples of central banks: the Bank of England, the European Central Bank, the US Federal Reserve, the Reserve Bank of India.</p>
'''
steppers = [
  ("How commercial banks create value", "--accent", ["Savers deposit money in the bank", "The bank lends to borrowers at a higher interest rate", "Borrowers invest or spend the loan", "The bank earns the interest gap", "Savings are turned into investment"]),
  ("Lender of last resort", "--bad", ["A commercial bank faces a sudden run on deposits", "It cannot meet withdrawals at once", "The central bank lends it emergency funds", "Confidence is restored", "The banking system stays stable"]),
]
lab1 = dict(title="A bank's profit", intro="Set the interest rates and the amount of lending. See the bank's gross income from the interest gap.", rl=["Interest earned", "Interest paid", "Bank profit (before costs)"],
  sliders=[("Deposits ($m)", 100, 1000, 100, 500, "'$' + v + 'm'"), ("Share lent out (%)", 30, 95, 5, 80, "v + '%'"), ("Interest rate on loans (%)", 2, 15, 1, 8, "v + '%'"), ("Interest rate on deposits (%)", 0, 8, 1, 2, "v + '%'")],
  fn="const loans = v[0] * v[1] / 100, earned = loans * v[2] / 100, paid = v[0] * v[3] / 100, prof = earned - paid; return { r: ['$' + earned.toFixed(1) + 'm', '$' + paid.toFixed(1) + 'm', (prof >= 0 ? '+' : '−') + '$' + Math.abs(prof).toFixed(1) + 'm'], t: 'Of $' + v[0] + 'm deposits the bank lends $' + loans.toFixed(0) + 'm at ' + v[2] + '%, earning $' + earned.toFixed(1) + 'm, and pays savers ' + v[3] + '% on deposits: $' + paid.toFixed(1) + 'm. The gap is $' + prof.toFixed(1) + 'm before running costs. Lending out less, or a smaller gap between rates, reduces profit.', bars: [['Interest earned', earned, '--good'], ['Interest paid', paid, '--warn'], ['Profit', Math.max(0, prof), '--accent']] };")
lab2 = dict(title="Who does what?", intro="Pick a task to see whether the central bank or commercial banks do it.", h1="Done by", h2="Why",
  items=[("Taking deposits from households", "Commercial bank", "Provides safe saving."), ("Lending money for a mortgage", "Commercial bank", "A loan to a customer."), ("Setting the key interest rate", "Central bank", "Monetary policy."), ("Printing banknotes", "Central bank", "Issues legal tender."), ("Lending in an emergency to a failing bank", "Central bank", "Lender of last resort."), ("Offering a current account and cards", "Commercial bank", "Payment services.")])
cl = [("Is each done by a <b>central bank</b> or a <b>commercial bank</b>?", ["Central bank", "Commercial bank"], [("Sets interest rates", 0), ("Issues banknotes", 0), ("Lender of last resort", 0), ("Offers savings accounts", 1), ("Makes loans to firms", 1), ("Provides debit cards", 1)], "Know the two roles."),
      ("Which <b>commercial bank service</b> is each?", ["Deposits", "Loans", "Payments"], [("A savings account", 0), ("A mortgage", 1), ("A bank transfer", 2), ("An overdraft", 1), ("A current account", 0), ("A contactless card", 2)], "Bank services.")]
match = [["Commercial bank", "A bank that takes deposits and makes loans"], ["Central bank", "The government's bank and banking regulator"], ["Lender of last resort", "Lends to banks in a crisis"], ["Monetary policy", "Using interest rates and the money supply"], ["Deposit", "Money placed with a bank by a saver"], ["Overdraft", "Borrowing beyond a bank balance"]]
order = ("Put the chain in order: <b>how a central bank acts as lender of last resort</b>.", ["Depositors lose confidence in a bank", "Many withdraw their money at once", "The bank cannot pay them all", "The central bank lends it emergency funds", "Confidence returns and the system stabilises"], "Preventing a banking collapse.")
calcs = [("A bank lends $80m at 10% and pays 3% on $100m of deposits. What is the profit before costs ($m)?", 5, "Earns 8m, pays 3m: <b>$5m</b>.", None, None), ("Deposits are $200m and the bank lends 75%. How much is lent ($m)?", 150, "75% × 200 = <b>$150m</b>.", None, None)]
mcq = [("A function of the central bank is to:", ["Take deposits from households", "Set interest rates", "Sell insurance", "Run supermarkets"], 1, "Monetary policy."), ("Commercial banks earn profit from:", ["Taxes", "The gap between interest rates", "Printing money", "Selling goods"], 1, "Lend high, pay low."), ("The lender of last resort is:", ["A commercial bank", "The central bank", "A household", "A firm"], 1, "In a crisis."), ("Which is a commercial bank service?", ["Printing notes", "Accepting deposits", "Setting policy", "Controlling inflation"], 1, "Savings."), ("The central bank is the government's:", ["Customer", "Bank", "Competitor", "Regulator only"], 1, "Holds accounts.")]
cards = [("Central bank", "The government's bank; controls interest rates and the money supply."), ("Commercial bank", "A bank that takes deposits and lends to households and firms."), ("Lender of last resort", "The central bank lending to banks in a crisis."), ("Deposit", "Money placed in a bank."), ("Loan", "Money borrowed, repaid with interest."), ("Overdraft", "Borrowing beyond the account balance."), ("Monetary policy", "Interest rates and money supply management."), ("Regulation", "Rules to keep banks safe."), ("Interest rate", "The price of borrowing or reward for saving.")]
exam_qs = [
  Q(1, "Identify", 2, "Identify two functions of a central bank.", "Set interest rates, issue notes, lender of last resort, government's bank.", "[K|Setting interest rates.] [K|Acting as lender of last resort (or issuing notes).]"),
  Q(2, "Explain", 4, "Explain two functions of commercial banks.", "Deposits, loans, payments.", "[K|Commercial banks accept deposits from savers.] [N|This provides a safe place to save and funds for lending.] [K|They lend to households and firms.] [N|Loans let firms invest and households buy homes, and the bank earns interest.]"),
  Q(3, "Explain", 4, "Explain the importance of the central bank to an economy.", "Stability, interest rates, lender of last resort.", "[K|The central bank sets interest rates and controls the money supply,] [N|which helps keep inflation low and the economy stable.] [K|It acts as lender of last resort,] [N|which prevents the collapse of banks and keeps confidence in the banking system.]"),
  Q(4, "Discuss", 6, "Discuss whether commercial banks or the central bank are more important to an economy.", "Banks: loans, payments; central bank: stability, rates. Judgement.", "[K|Commercial banks provide savings, loans and payments.] [N|They channel savings to investment, helping firms grow.] [N|The central bank controls interest rates and prevents banking crises.] [E|Without commercial banks little lending would happen, but without a stable central bank the system could collapse.] [E|Overall, they depend on each other; the central bank is arguably more important in a crisis.]", key=True),
]
tips_ = [("Central bank: rates, notes, last resort.", "Government's bank."), ("Commercial banks: deposits, loans, payments.", "They earn the interest gap."), ("Give examples of each.", "Bank of England; high street banks."), ("Explain importance.", "Stability and investment.")]
real_items = [("2008 financial crisis", "Central banks lent to banks and cut interest rates to prevent a collapse.", "Lender of last resort."), ("Mobile banking in Kenya", "Phone payments extended banking to people without bank accounts.", "Payment services."), ("Interest rate decisions", "The Bank of England changes rates to control inflation.", "Central bank role."), ("Mortgages", "Banks lend large sums so households can buy homes.", "Commercial bank loans.")]
review("ig-banking", "b312", "3.1.2", "Banking", "The role and importance of central banks and commercial banks. Syllabus 3.1.2.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Identify", "Explain", "Discuss"], real_items)

# ---------------------------------------------------------------- 3.2.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Households choose how to divide their income between <b>spending</b>, <b>saving</b> and <b>borrowing</b>. Their decisions are influenced by <b>income</b>, the <b>rate of interest</b>, <b>confidence</b>, <b>age</b> and <b>culture</b>. These choices matter for firms (sales), banks (deposits and loans) and the whole economy (aggregate demand).</p></div>

  <h2>Influences on households</h2>
  <div class="tw"><table class="t">
    <tr><th>Influence</th><th>Effect on spending</th><th>Effect on saving</th><th>Effect on borrowing</th></tr>
    <tr><td><b>Income</b></td><td>Higher income: more spending</td><td>Higher income: more saving (a larger share at high incomes)</td><td>Lower income: more borrowing to cover needs; higher income can support more borrowing</td></tr>
    <tr><td><b>Rate of interest</b></td><td>Higher rates: less spending on credit</td><td>Higher rates: more saving (higher reward)</td><td>Higher rates: less borrowing (dearer)</td></tr>
    <tr><td><b>Confidence</b></td><td>Confident households spend more</td><td>Pessimistic households save more (precaution)</td><td>Confident households borrow more</td></tr>
    <tr><td><b>Age</b></td><td>Young families spend on housing and children; the old spend on healthcare</td><td>Middle-aged save for retirement; the old spend savings</td><td>Young adults borrow for homes and education</td></tr>
    <tr><td><b>Culture</b></td><td>Cultures valuing status may spend more</td><td>Some cultures stress thrift and family saving</td><td>Attitudes to debt vary (religion, tradition)</td></tr>
  </table></div>

  <h2>Consumption and saving</h2>
  <div class="formula">Income = consumption (spending) + saving (+ tax)<br>Saving ratio = saving ÷ income × 100</div>
  <ul>
    <li>If households spend more, <b>aggregate demand</b> rises, helping growth and jobs.</li>
    <li>If households save more, banks have more to lend, but spending falls in the short run.</li>
    <li>Too much borrowing can lead to <b>debt problems</b> when interest rates rise.</li>
  </ul>
'''
steppers = [
  ("A rise in interest rates", "--accent", ["The central bank raises interest rates", "Saving pays more: households save more", "Borrowing is dearer: households borrow less", "Households spend less", "Aggregate demand falls"]),
  ("Falling confidence", "--bad", ["Households worry about jobs and the economy", "They cut back on big purchases", "They save more as a precaution", "Spending falls and firms lose sales", "Economic growth slows"]),
]
lab1 = dict(title="Spend or save?", intro="Set income, interest rate and confidence and see how a household divides its income.", rl=["Spending", "Saving", "Saving ratio"],
  sliders=[("Monthly income ($)", 1000, 6000, 500, 3000, "'$' + v"), ("Interest rate on savings (%)", 0, 10, 1, 3, "v + '%'"), ("Confidence (1 low, 10 high)", 1, 10, 1, 6, "v")],
  fn="const sr = Math.max(0.02, Math.min(0.6, 0.12 + 0.015 * v[1] + 0.00002 * (v[0] - 3000) - 0.02 * (v[2] - 5))), sav = v[0] * sr, spend = v[0] - sav; return { r: ['$' + spend.toFixed(0), '$' + sav.toFixed(0), (sr * 100).toFixed(0) + '%'], t: 'With income $' + v[0] + ', a ' + v[1] + '% savings rate and confidence ' + v[2] + ', the household spends $' + spend.toFixed(0) + ' and saves $' + sav.toFixed(0) + ' (' + (sr * 100).toFixed(0) + '% of income). Higher interest rates and lower confidence push saving up; higher confidence and cheaper borrowing push spending up (illustrative model).', bars: [['Spending', spend, '--accent'], ['Saving', sav, '--good']] };")
lab2 = dict(title="Influences on households", intro="Pick an influence to see its effect.", h1="Effect on spending/saving", h2="Why",
  items=[("Income rises", "More spending and saving", "More to divide."), ("Interest rates rise", "More saving, less borrowing", "Higher reward; dearer loans."), ("Confidence falls", "Less spending, more saving", "Precaution against job loss."), ("Young age", "More borrowing", "Homes and education."), ("Middle age", "More saving", "Retirement."), ("Culture of thrift", "More saving", "Social attitudes.")])
cl = [("Does each <b>raise</b> or <b>lower</b> household spending?", ["Raises spending", "Lowers spending"], [("Higher income", 0), ("Higher confidence", 0), ("Lower interest rates", 0), ("Higher interest rates", 1), ("Fear of unemployment", 1), ("A culture of thrift", 1)], "Know the effects."),
      ("Which <b>influence</b> is each?", ["Income", "Interest rate", "Confidence", "Age", "Culture"], [("A pay rise", 0), ("Mortgage payments rise", 1), ("Worry about job losses", 2), ("Students borrowing for study", 3), ("A tradition of saving for family", 4)], "Five influences.")]
match = [["Saving", "Income not spent"], ["Consumption", "Household spending"], ["Borrowing", "Spending using money from lenders"], ["Confidence", "How optimistic households feel"], ["Interest rate", "Reward for saving and cost of borrowing"], ["Saving ratio", "Saving as a percentage of income"]]
order = ("Put the chain in order: <b>how falling confidence slows the economy</b>.", ["Households fear job losses", "They cut spending and save more", "Firms' sales fall", "Firms cut output and jobs", "Growth slows"], "Confidence drives demand.")
calcs = [("A household earns $3,000 and saves $450. What is the saving ratio (%)?", 15, "450 ÷ 3,000 × 100 = <b>15%</b>.", None, None), ("Income is $4,000, spending is $3,400 and tax is $200. How much is saved ($)?", 400, "4,000 − 3,400 − 200 = <b>$400</b>.", None, None)]
mcq = [("A rise in interest rates is likely to:", ["Reduce saving", "Increase borrowing", "Reduce borrowing", "Increase spending"], 2, "Borrowing is dearer."), ("Higher confidence leads to:", ["More spending", "Less spending", "No change", "More saving only"], 0, "Optimism."), ("Young adults tend to:", ["Save the most", "Borrow", "Retire", "Avoid debt"], 1, "Homes and education."), ("Saving ratio is:", ["Spending ÷ income", "Saving ÷ income × 100", "Income ÷ saving", "Interest ÷ saving"], 1, "Percentage."), ("Which affects borrowing attitudes?", ["Culture", "Weather", "Gravity", "Tides"], 0, "Social norms.")]
cards = [("Consumption", "Household spending on goods and services."), ("Saving", "Income not spent."), ("Borrowing", "Obtaining funds to be repaid with interest."), ("Rate of interest", "The reward for saving and cost of borrowing."), ("Confidence", "How optimistic households are about the future."), ("Saving ratio", "Saving as a percentage of income."), ("Disposable income", "Income after tax."), ("Aggregate demand", "Total spending in the economy."), ("Precautionary saving", "Saving to be ready for bad times.")]
exam_qs = [
  Q(1, "Explain", 4, "Explain how a rise in interest rates may affect households' spending and saving.", "Saving up; borrowing and spending down.", "[K|A higher interest rate raises the reward for saving,] [N|so households may save more and spend less.] [K|It also makes borrowing dearer,] [N|so households borrow less and spending falls.]"),
  Q(2, "Explain", 4, "Explain how confidence may influence households' spending.", "Optimism raises spending; fear lowers.", "[K|If households are confident about jobs and incomes they spend and borrow more.] [N|If they are worried they save more as a precaution and spend less,] [N|so firms' sales fall.]"),
  Q(3, "Analyse", 6, "Analyse how age may influence households' spending, saving and borrowing.", "Young borrow; middle save; old spend savings.", "[K|Young adults often borrow to buy homes or study and have low savings.] [N|Middle-aged households have higher incomes and save for retirement.] [N|Older households spend savings and on healthcare.] [E|Differences depend on income and culture.]", key=True),
  Q(4, "Discuss", 8, "Discuss whether income is the most important influence on household spending.", "Income vs interest rate, confidence, age, culture. Judgement.", "[K|Income decides how much households can spend.] [N|Higher income raises spending and saving.] [N|However, interest rates change the cost of borrowing and reward for saving.] [N|Confidence and age also matter.] [E|Overall, income is the main influence but others can outweigh it in the short run, for example a fall in confidence during a recession.]", key=True),
]
tips_ = [("Five influences.", "Income, interest, confidence, age, culture."), ("State the direction.", "Up or down, and why."), ("Link to firms and banks.", "Sales and deposits."), ("Evaluate with 'depends on'.", "Income level, country.")]
real_items = [("Japan's high saving rate", "Japanese households have traditionally saved a large share of income.", "Culture."), ("COVID-19 lockdowns", "Households saved more when shops closed and uncertainty rose.", "Confidence."), ("Rate rises after 2021", "Higher mortgage rates cut borrowing and spending.", "Interest rate."), ("Student loans", "Many young people borrow to study.", "Age.")]
review("ig-households", "h321", "3.2.1", "Influences on Households' Spending, Saving and Borrowing", "How income, interest rates, confidence, age and culture shape what households do with their money. Syllabus 3.2.1.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Explain", "Analyse", "Discuss"], real_items)
