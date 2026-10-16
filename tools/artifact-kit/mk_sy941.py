"""Syllabus 9.4.1-9.4.2 Money and the money supply. Run: python3 tools/artifact-kit/mk_sy941.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.4.1 to 9.4.2"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Money</b> is anything generally accepted in payment for goods and services and in settlement of debts. It has four <b>functions</b>: a <b>medium of exchange</b>, a <b>unit of account</b>, a <b>store of value</b> and a <b>standard of deferred payment</b>. To work, it needs certain <b>characteristics</b>: acceptability, durability, portability, divisibility, uniformity and limited supply. The <b class="kw">money supply</b> is the total amount of money in the economy, measured as <b>narrow money</b> (the most liquid forms) or <b>broad money</b> (which adds less liquid deposits), and which measure is used affects how monetary policy is judged.</p></div>

  <h2>1 · Why money exists (9.4.1)</h2>
  <p>Under <b>barter</b> a trade needs a <b>double coincidence of wants</b>: each person must have what the other wants, in the right amounts. Money removes this problem, and allows specialisation and trade at lower cost.</p>
  <div id="pic1" class="card"></div>
  <h3>Functions of money</h3>
  <div class="tw"><table class="t">
    <tr><th>Function</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Medium of exchange</b></td><td>Accepted in payment, so goods can be bought and sold without barter</td><td>Paying for a coffee with a card</td></tr>
    <tr><td><b>Unit of account</b></td><td>A common measure of value, so prices can be compared</td><td>A website comparing grocery prices</td></tr>
    <tr><td><b>Store of value</b></td><td>Keeps purchasing power over time (inflation weakens this)</td><td>Savings in a bank account</td></tr>
    <tr><td><b>Standard of deferred payment</b></td><td>Allows debts and contracts to be settled in the future</td><td>Paying half a car's price now and half in six months, a mortgage</td></tr>
  </table></div>
  <h3>Characteristics of good money</h3>
  <ul>
    <li><b>Acceptable:</b> trusted and widely accepted, which is what makes money work.</li>
    <li><b>Durable:</b> does not wear out quickly.</li>
    <li><b>Portable:</b> easy to carry and transfer (bank transfers and cards are very portable).</li>
    <li><b>Divisible:</b> can be broken into small units to pay for items of different values.</li>
    <li><b>Uniform:</b> every unit of the same value is identical, so they can be exchanged without checking.</li>
    <li><b>Limited in supply (scarce):</b> if supply were unlimited its value would fall.</li>
    <li><b>Stable in value:</b> a store of value needs low inflation.</li>
  </ul>
  <p>Modern money is mostly <b>fiat money</b>: it has value because the government says it is legal tender and people trust it, not because it is made of something valuable. Most money is held as <b>bank deposits</b>, not as notes and coins.</p>

  <h2>2 · The money supply (9.4.2)</h2>
  <p>The <b>money supply</b> is the total stock of money in an economy at a point in time. Definitions differ by how liquid the assets are. <b>Liquidity</b> is the ease with which an asset can be converted into cash without losing value.</p>
  <div class="tw"><table class="t">
    <tr><th>Measure</th><th>What it includes</th><th>Liquidity</th></tr>
    <tr><td><b>Narrow money</b></td><td>Notes and coins in circulation, banks' deposits at the central bank, and (in wider definitions) current (checking) account deposits</td><td>Most liquid: used for everyday spending</td></tr>
    <tr><td><b>Broad money</b></td><td>Narrow money <b>plus</b> savings deposits, time deposits and other less liquid bank deposits</td><td>Less liquid: needs notice or may carry a penalty</td></tr>
  </table></div>
  <div class="tip"><b class="h">Money or near money?</b>Assets such as savings accounts, bonds and shares are <b>near money</b> or <b>other assets</b>. They can be turned into money but they are not generally accepted as a means of payment. Broad money counts the more liquid of these.</div>
  <ul>
    <li>Money is <b>more than cash</b>: most of the money supply is created by commercial banks when they lend (see 9.4.4 to 9.4.5).</li>
    <li>Why the measure matters: monetarists argue that the growth of the money supply drives inflation (9.4.3), so central banks need a reliable measure; but new payment technologies make the boundaries harder to draw.</li>
    <li>The <b>demand for money</b> is the desire to hold liquid assets (9.4.7). The money supply is how much of it exists.</li>
  </ul>
'''

watch = '''
  <h2>1 · From barter to money</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stB"></div>
  <h2>2 · Narrow money inside broad money</h2>
  <div id="stM"></div>
'''

explore = '''
  <h2>Lab 1 · Measuring the money supply</h2>
  <p>Set the amounts in each form ($bn). The lab adds them up as narrow and broad money and shows the share held as notes and coins.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Narrow money</small><strong id="r1"></strong></div><div><small>Broad money</small><strong id="r2"></strong></div><div><small>Cash as % of broad</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Stacked bar of notes and coins, current accounts, savings deposits and time deposits"></svg></div></div></div>

  <h2>Lab 2 · Which function of money?</h2>
  <p>Pick an everyday situation to see which function of money it shows.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Is it part of the narrow money supply, the broad money supply or neither?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the problems of barter in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Cigarettes as money in prison camps", "In some prisoner-of-war camps cigarettes became a medium of exchange and a unit of account: goods were priced in cigarettes, and cigarettes were durable, divisible and uniform. When supplies of cigarettes ran short, their value as a store of value was disrupted.", "a vivid example of the functions and characteristics of money, and why acceptability matters.") +
rw("Mobile money in Kenya", "M-Pesa lets people hold and send money using a mobile phone. Balances are stored by a mobile operator and backed by bank deposits. It acts as a medium of exchange for people without bank accounts.", "money is more than notes and coins, and new payment forms blur the boundary between narrow and broad money.") +
rw("Hyperinflation in Zimbabwe", "Prices doubled every day at the peak in 2008. People stopped holding Zimbabwean dollars as a store of value and began using the US dollar and barter. The currency lost its functions as a unit of account and store of value.", "what happens when money loses its characteristic of stable value.") +
rw("Cryptocurrencies", "Bitcoin is accepted by some firms as a medium of exchange, but its value changes sharply from day to day. It scores poorly as a store of value and unit of account, and is not legal tender in most countries.", "evaluating whether something is money: test it against the functions and characteristics.")
)

mc_exam = [
  ("Which statement about money is correct? (Oct/Nov 2024 · 31 · Q16, reworded)", ["It consists only of deposits held by commercial banks", "It functions as a medium of exchange", "Its monetary value equals its production cost", "It works only where there is a double coincidence of wants"], 1, "Money's main function is as a medium of exchange, which removes the need for a double coincidence of wants."),
  ("Salma agrees to pay half of a car's cost now and the other half in six months. Which function of money does this show? (Oct/Nov 2024 · 32 · Q16, reworded)", ["Divisibility", "Durability", "Standard of deferred payment", "Store of value"], 2, "Money allows payment to be made at a later date."),
  ("A website compares the prices of groceries. Which function of money does this illustrate? (Oct/Nov 2024 · 33 · Q16, reworded)", ["Medium of exchange", "Standard of deferred payment", "Store of value", "Unit of account"], 3, "Prices expressed in money allow goods to be compared."),
  ("What is a function of money? (Oct/Nov 2023 · 33 · Q17, reworded)", ["It can be divided into small units", "It can be easily carried", "It is a standard of deferred payment", "It is widely accepted"], 2, "The other three are characteristics of money, not functions."),
  ("What is the definition of liquidity? (Oct/Nov 2022 · 31 · Q23, reworded)", ["The ability of the foreign exchange market to buy foreign currency", "The support a central bank gives to commercial banks", "The ease with which an asset can be converted into cash", "The reaction of governments to a financial crisis"], 2, "Liquidity measures how quickly an asset can be turned into cash without loss of value."),
  ("A country's money in circulation can be measured in several ways. Which is the most liquid measure?", ["Time deposits", "Savings deposits", "Notes and coins", "Government bonds"], 2, "Notes and coins can be used immediately in payment."),
  ("In a year, national income in money terms rose by 3%, prices rose by 4% and the population by 1%. What was the approximate change in real income per head? (May/June 2020 · 31 · Q23, reworded)", ["A fall of 1%", "A fall of 2%", "A rise of 2%", "A rise of 3%"], 1, "Real income fell about 1% and with 1% more people real income per head fell about 2%.")
]

exam = exam_page("money and the money supply",
  "We searched the A Level Economics papers in the folder (2020 to 2025). The nature and functions of money are tested mainly in Paper 3 multiple choice, and money supply is the starting point of many Paper 4 monetary essays. Below are two practice questions with model answers, and seven Paper 3 multiple choice questions.",
  [("Practice questions", "2", "Functions of money; narrow and broad money"), ("Multiple choice (Paper 3)", "7 shown below", "2020 to 2024")],
  [
  eq("Practice (not a past paper question)", "8 marks", "Explain the functions of money and why money is better than barter.",
     ["Barter needs a double coincidence of wants; money solves this as a medium of exchange.",
      "Four functions explained: medium of exchange, unit of account, store of value and standard of deferred payment, each with a short example.",
      "Link to benefits: lower transaction costs, specialisation, trade, saving and borrowing.",
      "Evaluation: inflation weakens the store of value and the standard of deferred payment."],
     "Barter problem. Four functions with an example each. A limit linked to inflation.",
     [[("k", "Money is anything that is generally accepted in payment for goods and services. Under barter a trade needs a double coincidence of wants, so that each person has what the other wants, which makes trade slow and costly. Money works as a medium of exchange, which removes this problem."), ("a", "It is also a unit of account, so that a shop can price a coffee and a laptop in the same units and customers can compare them.")],
      [("n", "As a store of value it lets people save purchasing power to spend later, and as a standard of deferred payment it allows loans and contracts to be agreed in money terms, for example a mortgage. By making exchange easy, money lets people specialise in what they do best, which raises output."), ("e", "However, if inflation is high money loses value quickly, which weakens its role as a store of value and a standard of deferred payment, and in hyperinflation people may return to barter or use a foreign currency.")]]),
  eq("Practice (not a past paper question)", "4 marks", "Distinguish between narrow money and broad money.",
     ["Narrow money: the most liquid forms, such as notes and coins and balances that can be spent immediately (current accounts) (2 marks).",
      "Broad money: narrow money plus less liquid deposits such as savings and time deposits (2 marks).",
      "Credit the idea of liquidity as the basis for the distinction."],
     "One sentence each, with an example and the word 'liquid'.")
  ],
  )

tips = tips_html(
  [("Learn the four functions with examples.", "Medium of exchange, unit of account, store of value, standard of deferred payment."),
   ("Do not confuse functions and characteristics.", "Divisible, portable and durable are characteristics. The four functions are what money does."),
   ("Say 'double coincidence of wants'.", "It is the key problem of barter and the reason money exists."),
   ("Narrow versus broad is about liquidity.", "Narrow is the most liquid. Broad adds less liquid deposits."),
   ("Most money is bank deposits.", "Notes and coins are a small part of the money supply."),
   ("Say what inflation does.", "It weakens money as a store of value and standard of deferred payment."),
   ("Test new forms of money.", "Check acceptance, stability and functions before calling something money.")],
  [("Define", "Money is anything that is generally acceptable as a means of payment and in settlement of debts."),
   ("Function", "Money is a medium of exchange, which removes the need for a double coincidence of wants."),
   ("Measure", "Narrow money consists of the most liquid assets, while broad money adds less liquid deposits such as savings accounts."),
   ("Limit", "Inflation could reduce the value of money, which weakens its function as a store of value."),
   ("Link", "Because banks create deposits when they lend, the money supply is not controlled by the central bank alone.")],
  [CW["define"], CW["explain"], CW["analyse"]]) + FC

js = '''
/* ---------- Learn picture and Watch 1: barter ---------- */
function barterDraw(s) {
  let o = ""; const box = (x, y, w, l, c, v = 1) => SV.rect(x, y, w, 48, c, op(v)) + SV.text(x + w / 2, y + 29, l, "lbl bd", { "text-anchor": "middle", ...op(v) });
  o += box(40, 40, 140, "Farmer: has wheat", "f4") + box(580, 40, 140, "Tailor: has cloth", "f1") + box(310, 250, 140, "Cobbler: has shoes", "f3");
  if (s.a > 0) o += arrow(185, 64, 575, 64, "r", "c4", s.a) + arrow(575, 90, 185, 90, "l", "c1", s.a) + tag(380, 56, "wheat for cloth?", "t4", s.a, "middle");
  if (s.b > 0) o += tag(380, 118, "Tailor wants shoes, not wheat: no deal", "t2", s.b, "middle") + SV.line(300, 110, 460, 136, "c2", op(s.b));
  if (s.c > 0) o += box(310, 140, 140, "MONEY", "f3", s.c) + arrow(185, 76, 305, 160, "r", "c3", s.c) + arrow(455, 160, 575, 76, "r", "c3", s.c) + arrow(380, 190, 380, 245, "d", "c3", s.c);
  if (s.d > 0) o += tag(380, 330, "Money is accepted by everyone, so each trade is separate and simple", "t3", s.d, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 350" role="img" aria-label="Three traders and a double coincidence of wants problem solved by money">${barterDraw({ a: 1, b: 1, c: 0, d: 0 })}</svg>`;
Lib.stepper($("#stB"), { w: 760, h: 350, label: "Barter between a farmer, tailor and cobbler, and money solving the problem", base: { a: 0, b: 0, c: 0, d: 0 }, draw: barterDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>Three traders.</b> A farmer has wheat, a tailor has cloth and a cobbler has shoes. Each wants something the others have.", s: {} },
  { cap: "<b>Barter.</b> The farmer offers wheat for cloth.", s: { a: 1 } },
  { cap: "<b>No double coincidence of wants.</b> The tailor wants shoes, not wheat, so the trade fails. Barter needs each side to want what the other has.", s: { a: 1, b: 1 } },
  { cap: "<b>Money.</b> The farmer sells wheat to anyone for money, then buys cloth with it; the tailor buys shoes with the same money. Money is a <b>medium of exchange</b>.", s: { a: 0.3, b: 0, c: 1 } },
  { cap: "<b>The result.</b> Trade needs no coincidence of wants. Money is also a unit of account, a store of value and a standard of deferred payment, and it lets people specialise.", s: { a: 0.3, c: 1, d: 1 } },
] });

/* ---------- Watch 2: nested money measures ---------- */
function nestDraw(s) {
  const lay = [[360, 150, 150, "Time and wholesale deposits", "f4", s.c], [270, 150, 130, "Savings deposits", "f1", s.b], [190, 150, 100, "Current account deposits", "f3", s.a]]; let o = "";
  lay.forEach(([w, cx, cy, l, c, v]) => { if (v > 0) o += `<ellipse cx="380" cy="${185}" rx="${w * 1.0}" ry="${w * 0.5}" class="${c}" style="opacity:${0.45 * v};stroke:var(--ink);stroke-width:1.5"/>`; });
  o += `<ellipse cx="380" cy="185" rx="70" ry="38" class="f2" style="opacity:0.7;stroke:var(--ink);stroke-width:1.5"/>` + SV.text(380, 189, "Notes and coins", "lbl bd", { "text-anchor": "middle" });
  if (s.a > 0) o += tag(380, 140, "Current accounts", "t3", s.a, "middle");
  if (s.b > 0) o += tag(380, 100, "Savings deposits", "t1", s.b, "middle");
  if (s.c > 0) o += tag(380, 52, "Time and wholesale deposits", "t4", s.c, "middle");
  if (s.n > 0) o += tag(380, 330, "NARROW MONEY (inner circles)   BROAD MONEY (everything)", "t1", s.n, "middle");
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 350, label: "Nested ellipses of notes and coins, current accounts, savings deposits and time deposits showing narrow and broad money", base: { a: 0, b: 0, c: 0, n: 0 }, draw: nestDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>The most liquid.</b> Notes and coins can be spent immediately anywhere.", s: {} },
  { cap: "<b>Current accounts.</b> Money in current (checking) accounts can be spent by card or transfer at once, so it is added to notes and coins in a wider narrow money measure.", s: { a: 1 } },
  { cap: "<b>Savings deposits.</b> These earn interest but may need notice or lose some interest if withdrawn early. They are less liquid and belong in <b>broad</b> money.", s: { a: 1, b: 1, n: 1 } },
  { cap: "<b>Time and wholesale deposits.</b> Fixed-term deposits and large deposits are the least liquid part of broad money. The wider the measure, the larger the total.", s: { a: 1, b: 1, c: 1, n: 1 } },
] });

/* ---------- Lab 1: money supply ---------- */
function labMS() {
  if (!$("#nc") || !$("#ca") || !$("#sv") || !$("#tm")) return;
  const nc = +$("#nc").value, ca = +$("#ca").value, sv = +$("#sv").value, tm = +$("#tm").value, narrow = nc + ca, broad = narrow + sv + tm;
  $("#r1").textContent = "$" + narrow + "bn"; $("#r2").textContent = "$" + broad + "bn"; $("#r3").textContent = Lib.fmtN(nc / broad * 100, 1) + "%";
  $("#rv").textContent = `Narrow money is $${narrow}bn and broad money is $${broad}bn. Notes and coins are only ${Lib.fmtN(nc / broad * 100, 1)}% of the total, which shows that most of the money supply is bank deposits created by lending.`;
  const mx = broad * 1.05, Y = (v) => 270 - v / mx * 230; let y = 270, o = SV.line(40, 270, 400, 270);
  [[nc, "f2", "Notes and coins"], [ca, "f3", "Current accounts"], [sv, "f1", "Savings"], [tm, "f4", "Time deposits"]].forEach(([v, c, l]) => { const h = v / mx * 230; y -= h; o += SV.rect(150, y, 120, h, c) + SV.text(210, y + h / 2 + 4, l + " " + v, "sm bd", { "text-anchor": "middle" }); });
  o += tag(280, Y(narrow) + 4, "◀ narrow " + narrow, "t3") + tag(280, Y(broad) + 4, "◀ broad " + broad, "t1");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "nc", label: "Notes and coins ($bn) ", min: 20, max: 150, step: 10, value: 80, fmt: (v) => v, onInput: labMS });
Lib.slider($("#g2"), { id: "ca", label: "Current account deposits ($bn) ", min: 100, max: 800, step: 50, value: 400, fmt: (v) => v, onInput: labMS });
Lib.slider($("#g3"), { id: "sv", label: "Savings deposits ($bn) ", min: 100, max: 1000, step: 50, value: 500, fmt: (v) => v, onInput: labMS });
Lib.slider($("#g4"), { id: "tm", label: "Time and wholesale deposits ($bn) ", min: 0, max: 800, step: 50, value: 300, fmt: (v) => v, onInput: labMS });
labMS();
btnTable("lbBtns", "lbOut", [
  ["Paying for lunch with a card", "Medium of exchange", "Money is accepted in payment for goods"],
  ["Comparing the price of two phones in dollars", "Unit of account", "Prices in a common unit make goods easy to compare"],
  ["Putting $200 a month in a savings account", "Store of value", "Money keeps purchasing power for later"],
  ["Taking out a 25-year mortgage", "Standard of deferred payment", "Money allows payment over time in agreed units"],
  ["Prices rising 40% a year and people holding dollars instead", "Money failing as a store of value", "High inflation destroys the value of money held"],
  ["A shop that accepts only gold coins", "Failing acceptability", "Money must be widely accepted to work"]
], ["Situation", "Function shown", "Why"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Where does the asset belong?", ["Narrow money", "Broad money only", "Not money (near money or other asset)"],
  [("Notes and coins in circulation", 0), ("Money in a current account", 0), ("A notice savings account", 1), ("A fixed-term deposit", 1), ("Government bonds", 2), ("Shares in a company", 2), ("Banks' balances at the central bank", 0), ("A house", 2)],
  "Narrow money is the most liquid. Broad money adds less liquid deposits.") + MATCH([
  ["Medium of exchange", "Accepted in payment for goods and services"],
  ["Unit of account", "A common measure of value and prices"],
  ["Store of value", "Keeps purchasing power over time"],
  ["Standard of deferred payment", "Allows debts to be settled in the future"],
  ["Liquidity", "How easily an asset can be turned into cash"],
  ["Fiat money", "Money that has value because the government declares it legal tender"]]) + ORDER(
  "Put the problems of barter in order.",
  ["A person needs something that someone else has", "They must find someone who wants what they have to offer", "The two must agree the amounts and the exchange rate for each good", "Many trades fail or take a long time", "Specialisation and trade stay limited"],
  "Barter raises the cost of trade; money lowers it.") + CALC([
  {"q": "Notes and coins are $60bn, current accounts $340bn, savings $450bn and time deposits $250bn. Calculate broad money ($bn).", "a": 1100, "unit": "$bn", "tol": 0.5, "hint": "Add all four.", "sol": "60 + 340 + 450 + 250 = <b>$1,100bn</b>."},
  {"q": "Using the same data, calculate narrow money (notes and coins plus current accounts) ($bn).", "a": 400, "unit": "$bn", "tol": 0.5, "hint": "60 + 340.", "sol": "<b>$400bn</b>."},
  {"q": "Prices rise 5% a year. How much does a $100 note buy, in terms of today's prices, after one year (to the nearest cent)?", "a": 95.24, "unit": "$", "tol": 0.02, "hint": "100 ÷ 1.05.", "sol": "100 ÷ 1.05 = <b>$95.24</b> of today's goods."},
  {"q": "Notes and coins are $60bn and broad money is $1,100bn. What percentage of broad money is notes and coins (to one decimal place)?", "a": 5.5, "unit": "%", "tol": 0.1, "hint": "60 ÷ 1100.", "sol": "60 ÷ 1100 × 100 = <b>5.5%</b>."}]) + MCQ([
  ("What problem does money solve?", ["The double coincidence of wants", "Inflation", "Unemployment", "Scarcity"], 0, "Money lets people trade without needing someone who wants exactly what they have."),
  ("Which is a function of money rather than a characteristic?", ["Divisibility", "Portability", "Store of value", "Durability"], 2, "Store of value is one of the four functions."),
  ("Which is the most liquid?", ["A house", "A fixed-term deposit", "Notes and coins", "A government bond"], 2, "Cash can be used at once without loss."),
  ("Which would fall as a result of high inflation?", ["Money's role as a store of value", "Money's divisibility", "Money's durability", "Money's portability"], 0, "Inflation reduces what money can buy in the future."),
  ("Most of the money supply in a modern economy is:", ["Notes and coins", "Gold", "Bank deposits", "Government bonds"], 2, "Banks create deposits when they lend.")
], "qz1") + CARDS([
  ("Money", "Anything generally accepted as payment and in settlement of debts."),
  ("Medium of exchange", "Accepted in payment for goods and services."),
  ("Unit of account", "Common measure of value."),
  ("Store of value", "Keeps purchasing power over time."),
  ("Standard of deferred payment", "Settles debts in the future."),
  ("Narrow money", "Most liquid forms: notes and coins, current accounts."),
  ("Broad money", "Narrow money plus savings and time deposits."),
  ("Liquidity", "Ease of converting an asset into cash.")]) + MCQ(mc_exam)

build("sy941", "money-and-the-money-supply", "Money and the Money Supply", EY,
  "9.4.1 to 9.4.2: the functions and characteristics of money, and how the money supply is defined and measured. Animated diagrams, labs, drills and exam practice.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
