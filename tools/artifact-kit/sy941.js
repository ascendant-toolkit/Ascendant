const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

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
Lib.classify($("#cl1"), { prompt: "Where does the asset belong?", buckets: [{"label": "Narrow money"}, {"label": "Broad money only"}, {"label": "Not money (near money or other asset)"}], items: [{"text": "Notes and coins in circulation", "b": 0}, {"text": "Money in a current account", "b": 0}, {"text": "A notice savings account", "b": 1}, {"text": "A fixed-term deposit", "b": 1}, {"text": "Government bonds", "b": 2}, {"text": "Shares in a company", "b": 2}, {"text": "Banks' balances at the central bank", "b": 0}, {"text": "A house", "b": 2}], done: "Narrow money is the most liquid. Broad money adds less liquid deposits." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Medium of exchange", "Accepted in payment for goods and services"], ["Unit of account", "A common measure of value and prices"], ["Store of value", "Keeps purchasing power over time"], ["Standard of deferred payment", "Allows debts to be settled in the future"], ["Liquidity", "How easily an asset can be turned into cash"], ["Fiat money", "Money that has value because the government declares it legal tender"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the problems of barter in order.", items: ["A person needs something that someone else has", "They must find someone who wants what they have to offer", "The two must agree the amounts and the exchange rate for each good", "Many trades fail or take a long time", "Specialisation and trade stay limited"], done: "Barter raises the cost of trade; money lowers it." });
Lib.calc($("#c1"), { qs: [
  {"q": "Notes and coins are $60bn, current accounts $340bn, savings $450bn and time deposits $250bn. Calculate broad money ($bn).", "a": 1100, "unit": "$bn", "tol": 0.5, "hint": "Add all four.", "sol": "60 + 340 + 450 + 250 = <b>$1,100bn</b>."},
  {"q": "Using the same data, calculate narrow money (notes and coins plus current accounts) ($bn).", "a": 400, "unit": "$bn", "tol": 0.5, "hint": "60 + 340.", "sol": "<b>$400bn</b>."},
  {"q": "Prices rise 5% a year. How much does a $100 note buy, in terms of today's prices, after one year (to the nearest cent)?", "a": 95.24, "unit": "$", "tol": 0.02, "hint": "100 ÷ 1.05.", "sol": "100 ÷ 1.05 = <b>$95.24</b> of today's goods."},
  {"q": "Notes and coins are $60bn and broad money is $1,100bn. What percentage of broad money is notes and coins (to one decimal place)?", "a": 5.5, "unit": "%", "tol": 0.1, "hint": "60 ÷ 1100.", "sol": "60 ÷ 1100 × 100 = <b>5.5%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What problem does money solve?", opts: ["The double coincidence of wants", "Inflation", "Unemployment", "Scarcity"], a: 0, why: "Money lets people trade without needing someone who wants exactly what they have." },
  { q: "Which is a function of money rather than a characteristic?", opts: ["Divisibility", "Portability", "Store of value", "Durability"], a: 2, why: "Store of value is one of the four functions." },
  { q: "Which is the most liquid?", opts: ["A house", "A fixed-term deposit", "Notes and coins", "A government bond"], a: 2, why: "Cash can be used at once without loss." },
  { q: "Which would fall as a result of high inflation?", opts: ["Money's role as a store of value", "Money's divisibility", "Money's durability", "Money's portability"], a: 0, why: "Inflation reduces what money can buy in the future." },
  { q: "Most of the money supply in a modern economy is:", opts: ["Notes and coins", "Gold", "Bank deposits", "Government bonds"], a: 2, why: "Banks create deposits when they lend." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Money", "Anything generally accepted as payment and in settlement of debts."],
  ["Medium of exchange", "Accepted in payment for goods and services."],
  ["Unit of account", "Common measure of value."],
  ["Store of value", "Keeps purchasing power over time."],
  ["Standard of deferred payment", "Settles debts in the future."],
  ["Narrow money", "Most liquid forms: notes and coins, current accounts."],
  ["Broad money", "Narrow money plus savings and time deposits."],
  ["Liquidity", "Ease of converting an asset into cash."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which statement about money is correct? (Oct/Nov 2024 · 31 · Q16, reworded)", opts: ["It consists only of deposits held by commercial banks", "It functions as a medium of exchange", "Its monetary value equals its production cost", "It works only where there is a double coincidence of wants"], a: 1, why: "Money's main function is as a medium of exchange, which removes the need for a double coincidence of wants." },
  { q: "Salma agrees to pay half of a car's cost now and the other half in six months. Which function of money does this show? (Oct/Nov 2024 · 32 · Q16, reworded)", opts: ["Divisibility", "Durability", "Standard of deferred payment", "Store of value"], a: 2, why: "Money allows payment to be made at a later date." },
  { q: "A website compares the prices of groceries. Which function of money does this illustrate? (Oct/Nov 2024 · 33 · Q16, reworded)", opts: ["Medium of exchange", "Standard of deferred payment", "Store of value", "Unit of account"], a: 3, why: "Prices expressed in money allow goods to be compared." },
  { q: "What is a function of money? (Oct/Nov 2023 · 33 · Q17, reworded)", opts: ["It can be divided into small units", "It can be easily carried", "It is a standard of deferred payment", "It is widely accepted"], a: 2, why: "The other three are characteristics of money, not functions." },
  { q: "What is the definition of liquidity? (Oct/Nov 2022 · 31 · Q23, reworded)", opts: ["The ability of the foreign exchange market to buy foreign currency", "The support a central bank gives to commercial banks", "The ease with which an asset can be converted into cash", "The reaction of governments to a financial crisis"], a: 2, why: "Liquidity measures how quickly an asset can be turned into cash without loss of value." },
  { q: "A country's money in circulation can be measured in several ways. Which is the most liquid measure?", opts: ["Time deposits", "Savings deposits", "Notes and coins", "Government bonds"], a: 2, why: "Notes and coins can be used immediately in payment." },
  { q: "In a year, national income in money terms rose by 3%, prices rose by 4% and the population by 1%. What was the approximate change in real income per head? (May/June 2020 · 31 · Q23, reworded)", opts: ["A fall of 1%", "A fall of 2%", "A rise of 2%", "A rise of 3%"], a: 1, why: "Real income fell about 1% and with 1% more people real income per head fell about 2%." },
] });
