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
Lib.classify($("#cl1"), { prompt: "Does the event tend to raise or lower the money supply?", buckets: [{"label": "Raises it"}, {"label": "Lowers it"}], items: [{"text": "The central bank cuts the required reserve ratio", "b": 0}, {"text": "The central bank raises interest rates and sells bonds", "b": 1}, {"text": "Quantitative easing", "b": 0}, {"text": "Banks become fearful and cut lending", "b": 1}, {"text": "A large rise in capital inflows (not offset)", "b": 0}, {"text": "A current account deficit financed from reserves", "b": 1}, {"text": "The government prints money to pay for spending", "b": 0}, {"text": "Borrowers repay bank loans", "b": 1}], done: "More credit creation, more central bank money or net foreign inflows raise the money supply." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Reserve ratio", "Cash reserves as a share of deposits"], ["Capital ratio", "Capital as a share of risk-weighted assets"], ["Credit multiplier", "1 ÷ reserve ratio: how much deposits expand"], ["Lender of last resort", "The central bank lending to banks short of liquidity"], ["Quantitative easing", "The central bank buying assets with new money"], ["Financial intermediation", "Channelling funds from savers to borrowers"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put credit creation in order.", items: ["A customer deposits cash in a bank", "The bank keeps a reserve and lends the rest", "The borrower spends the loan and the seller deposits it in a bank", "That bank keeps a reserve and lends part again", "Total deposits expand by a multiple of the original deposit"], done: "Each loan becomes a new deposit, so deposits grow in successive rounds." });
Lib.calc($("#c1"), { qs: [
  {"q": "The reserve ratio is 20%. Calculate the credit multiplier.", "a": 5, "tol": 0.01, "hint": "1 ÷ 0.2.", "sol": "<b>5</b>."},
  {"q": "A new deposit of $5,000 with a reserve ratio of 10% and no cash drain. Calculate the maximum total deposits ($).", "a": 50000, "unit": "$", "tol": 1, "hint": "5000 × 10.", "sol": "<b>$50,000</b>."},
  {"q": "The reserve ratio is 8% and the cash drain is 2% of loans. Calculate the credit multiplier.", "a": 10, "tol": 0.05, "hint": "1 ÷ (0.08 + 0.02).", "sol": "1 ÷ 0.10 = <b>10</b>."},
  {"q": "A bank has deposits of $800m and cash reserves of $64m. Calculate its reserve ratio (%).", "a": 8, "unit": "%", "tol": 0.05, "hint": "64 ÷ 800.", "sol": "<b>8%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which asset of a bank is the most liquid?", opts: ["Loans to customers", "Cash at the central bank", "Government bonds", "Buildings"], a: 1, why: "Cash is already money." },
  { q: "Why do the three objectives of a commercial bank conflict?", opts: ["Liquid and safe assets earn lower returns than riskier and less liquid ones", "Banks cannot lend", "Customers do not deposit", "Central banks forbid profit"], a: 0, why: "More liquidity and security means less profit." },
  { q: "Which would reduce the credit multiplier?", opts: ["A fall in the reserve ratio", "A rise in the reserve ratio", "A rise in lending", "A fall in interest rates"], a: 1, why: "The multiplier is 1 ÷ reserve ratio." },
  { q: "A government sells bonds to the non-bank public to finance a deficit. What is the effect on the money supply?", opts: ["It rises sharply", "It falls sharply", "It changes little", "It doubles"], a: 2, why: "Money is transferred from savers to the government, then spent." },
  { q: "A role of the central bank that a commercial bank does not have is:", opts: ["Taking deposits from households", "Being the lender of last resort", "Making loans to firms", "Charging interest on overdrafts"], a: 1, why: "Only the central bank can act as lender of last resort." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Financial intermediary", "Brings savers and borrowers together."],
  ["Reserve ratio", "Cash reserves ÷ deposits."],
  ["Capital ratio", "Capital ÷ risk-weighted assets."],
  ["Credit multiplier", "1 ÷ reserve ratio."],
  ["Liquidity", "Ease of converting assets into cash."],
  ["Lender of last resort", "Central bank lends to banks short of cash."],
  ["Quantitative easing", "Central bank buys assets with newly created money."],
  ["Sterilisation", "Offsetting the effect of foreign currency flows on the money supply."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A world financial crisis was partly linked to the actions of commercial banks. Which actions could have led to it? (May/June 2024 · 31 · Q16, reworded)", opts: ["Being subject to tight controls by the central bank over credit creation", "Holding reserves above the agreed reserve ratio", "Taking excessive risks by demanding too little security from borrowers", "Widening the gap in favour of assets over liabilities"], a: 2, why: "Lending with too little security meant losses when borrowers defaulted." },
  { q: "Which statement applies to a central bank and to a commercial bank? (Feb/March 2023 · 32 · Q18, reworded)", opts: ["Both issue bank notes", "Both are the lender of last resort", "A commercial bank aims to maximise profit, a central bank does not", "A central bank receives deposits from the public"], a: 2, why: "Central banks pursue policy objectives and stability, not profit." },
  { q: "The cash deposit ratio of banks changed from 5% to 10%. What will be the result? (Oct/Nov 2021 · 32 · Q27, reworded)", opts: ["Bank deposits will fall by 10%", "Bank deposits will rise by 5%", "The credit multiplier will fall by 50%", "The credit multiplier will rise by 5%"], a: 2, why: "The multiplier is 1 ÷ ratio, so it falls from 20 to 10: a 50% fall." },
  { q: "In which context relevant to growth in the money supply is the term 'total currency flow' used? (May/June 2022 · 32 · Q24, reworded)", opts: ["Between central banks and commercial banks", "Between central banks and governments", "Between domestic residents and foreign residents", "Between the general public and the financial sector"], a: 2, why: "Total currency flow is the money flowing in and out of the country through the balance of payments." },
  { q: "A central bank buys government securities from the private sector. What is the likely effect on long-term interest rates and the money supply? (May/June 2020 · 31 · Q26, reworded)", opts: ["Long-term rates fall, money supply falls", "Long-term rates fall, money supply rises", "Long-term rates rise, money supply falls", "Long-term rates rise, money supply rises"], a: 1, why: "Buying securities raises their price (so yields fall) and puts new money into the economy." },
  { q: "Which policy does a central bank carry out to pursue quantitative easing? (May/June 2021 · 31 · Q26, reworded)", opts: ["Buying long-term government debt from the public", "Buying short-term government debt from the public", "Selling long-term government debt to the public", "Selling short-term government debt to the public"], a: 0, why: "QE is the purchase of long-term assets, mainly government bonds, with newly created money." },
  { q: "A central bank sells securities on the open market. What does Keynesian theory predict? (Oct/Nov 2020 · 31 · Q26, reworded)", opts: ["A fall in the price level", "A fall in unemployment", "A rise in the price level", "A rise in the rate of interest"], a: 3, why: "Selling securities reduces the money supply, so the interest rate rises." },
] });
