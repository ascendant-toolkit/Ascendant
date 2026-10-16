/* ---------- data: pizza (single good) and X, Y (two goods, income $24, Py = $2) ---------- */
const TUp = [0, 20, 36, 48, 56, 60, 60, 56, 48];            // total utility of n slices
const MUp = (n) => TUp[n] - TUp[n - 1];
const MUX = [24, 20, 16, 12, 8, 4], MUY = [15, 12, 9, 6, 3, 1], INC = 24, PY = 2;
const cum = (a) => { let t = [0]; a.forEach((v) => t.push(t[t.length - 1] + v)); return t; };
const CX = cum(MUX), CY = cum(MUY);
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
function best(px) {
  let b = { x: 0, y: 0, tu: -1, spend: 0 };
  for (let x = 0; x <= 6; x++) for (let y = 0; y <= 6; y++) {
    const sp = px * x + PY * y; if (sp > INC) continue;
    const tu = CX[x] + CY[y];
    if (tu > b.tu || (tu === b.tu && sp > b.spend)) b = { x, y, tu, spend: sp };
  }
  return b;
}
const PRICES = [8, 6, 4, 3, 2, 1];

/* ---------- Watch 2: equi-marginal ---------- */
const ORDER = ["Y", "X", "Y", "X", "Y", "X", "X", "Y"];
const RX = MUX.map((m) => m / 4), RY = MUY.map((m) => m / PY);
function equiDraw(s) {
  const k = Math.round(s.k), bx = ORDER.slice(0, k).filter((c) => c === "X").length, by = k - bx, spent = 4 * bx + 2 * by, H = 28, base = 290;
  let o = SV.line(40, base, 740, base);
  const group = (arr, x0, name, bought, cls) => {
    arr.forEach((v, i) => { const x = x0 + i * 52, isB = i < bought; o += SV.rect(x, base - v * H, 40, v * H, isB ? cls : "ax", isB ? { rx: 3 } : { fill: "none", rx: 3, "stroke-dasharray": "4 3" }) + SV.text(x + 20, base - v * H - 6, Lib.fmtN(v, 1), "sm bd", { "text-anchor": "middle" }) + SV.text(x + 20, base + 16, "#" + (i + 1), "sm", { "text-anchor": "middle" }); });
    o += SV.text(x0 + 130, base + 40, name, "lbl bd", { "text-anchor": "middle" });
  };
  group(RX, 50, "Good X: MUx ÷ $4 (utils per $)", bx, "f1"); group(RY, 410, "Good Y: MUy ÷ $2 (utils per $)", by, "f3");
  o += SV.text(40, 24, `Purchases made: ${k}   ·   X: ${bx}   ·   Y: ${by}   ·   spent $${spent} of $24   ·   total utility ${CX[bx] + CY[by]}`, "lbl bd");
  if (s.l > 0.5) o += SV.line(40, base - 3 * H, 740, base - 3 * H, "gr", { "stroke-dasharray": "6 5" }) + SV.text(390, 46, "Dashed line: 3 utils per $ for the last unit bought of both goods", "sm bd t3", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 345, label: "Spending a budget of $24 on goods X and Y by always buying the unit with the highest utility per dollar", base: { k: 0, l: 0 }, draw: equiDraw, tween: 700, dwell: 5600, steps: [
  { cap: "<b>Utility per dollar</b> for each unit: MU divided by price. Filled bars are bought. Budget $24, X costs $4, Y costs $2. No purchases yet.", s: { k: 0 } },
  { cap: "<b>First two purchases.</b> Y#1 gives 7.5 utils per $, the best. Then X#1 (6.0) and Y#2 (6.0) tie. Spending $8 so far (Y, X, Y).", s: { k: 3 } },
  { cap: "<b>Four purchases in.</b> The next best are X#2 (5.0) and Y#3 (4.5). Utility per dollar of each new purchase keeps <b>falling</b> because MU diminishes.", s: { k: 5 } },
  { cap: "<b>Six purchases.</b> X#3 (4.0). Now the best remaining are X#4 and Y#4, both worth <b>3.0</b> per dollar. Spent $18.", s: { k: 6 } },
  { cap: "<b>Equilibrium.</b> Buy X#4 and Y#4: 4 units of X and 4 of Y, spending exactly $24. The last unit of each gives <b>3 utils per $</b>: MUx/Px = MUy/Py = 3. Total utility is 114, the most possible.", s: { k: 8, l: 1 } },
] });

/* ---------- Lab 2: spend the budget ---------- */
function lab2() {
  if (!$("#bx") || !$("#by")) return;
  const x = +$("#bx").value, y = +$("#by").value, sp = 4 * x + 2 * y, tu = CX[x] + CY[y], ok = sp <= INC;
  const rx = x > 0 ? MUX[x - 1] / 4 : null, ry = y > 0 ? MUY[y - 1] / 2 : null;
  $("#s1").textContent = "$" + sp; $("#s2").textContent = ok ? tu : "over budget"; $("#s3").textContent = (rx === null ? "–" : Lib.fmtN(rx, 1)) + " / " + (ry === null ? "–" : Lib.fmtN(ry, 1));
  $("#sv").textContent = !ok ? `This costs $${sp}, more than your $24. Cut back on X or Y.`
    : tu === 114 ? "This is the best possible bundle (total utility 114). The last unit of each good gives 3 utils per dollar, so MUx/Px = MUy/Py."
    : rx !== null && ry !== null && rx > ry ? `Not the best. The last dollar on X gives ${Lib.fmtN(rx, 1)} utils, on Y only ${Lib.fmtN(ry, 1)}. Switch spending from Y to X.`
    : rx !== null && ry !== null && ry > rx ? `Not the best. The last dollar on Y gives ${Lib.fmtN(ry, 1)} utils, on X only ${Lib.fmtN(rx, 1)}. Switch spending from X to Y.`
    : `Total utility ${tu}. Money is left over or one good is missing: more spending would add utility.`;
  const H = (v) => 200 - v * 22, bw = 60;
  let o = SV.line(20, 200, 400, 200) + SV.text(24, 22, "Utils per $ of the last unit bought", "sm");
  [[50, rx || 0, "f1", "X"], [150, ry || 0, "f3", "Y"]].forEach(([bx, v, c, l]) => { o += SV.rect(bx, H(v), bw, 200 - H(v), c) + SV.text(bx + bw / 2, H(v) - 6, Lib.fmtN(v, 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(bx + bw / 2, 218, l, "sm", { "text-anchor": "middle" }); });
  o += SV.text(260, 70, "Your total utility: " + (ok ? tu : "–"), "lbl bd t1") + SV.text(260, 96, "Best possible: 114", "lbl bd t3") + SV.text(260, 122, "Budget used: $" + sp + " of $24", "sm");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "bx", label: "Units of X ($4 each): ", min: 0, max: 6, step: 1, value: 2, fmt: (v) => v, onInput: lab2 });
Lib.slider($("#g3"), { id: "by", label: "Units of Y ($2 each): ", min: 0, max: 6, step: 1, value: 2, fmt: (v) => v, onInput: lab2 });


/* ---------- Lab 2: which good next ---------- */
function labNext() {
  if (!$("#ax") || !$("#ay")) return;
  const x = +$("#ax").value, y = +$("#ay").value, mx = x < 6 ? MUX[x] / 4 : 0, my = y < 6 ? MUY[y] / PY : 0;
  $("#n1").textContent = x < 6 ? Lib.fmtN(mx, 2) : "none left"; $("#n2").textContent = y < 6 ? Lib.fmtN(my, 2) : "none left"; $("#n3").textContent = mx === my ? "Either" : mx > my ? "X" : "Y";
  $("#nv").textContent = mx === my ? "The ratios are equal. A switch would not raise total utility: this is equilibrium (if the budget is spent)."
    : `The next unit of ${mx > my ? "X gives " + Lib.fmtN(mx, 2) + " utils per dollar and Y only " + Lib.fmtN(my, 2) : "Y gives " + Lib.fmtN(my, 2) + " utils per dollar and X only " + Lib.fmtN(mx, 2)}, so spending on ${mx > my ? "X" : "Y"} next raises total utility more.`;
  let o = SV.line(30, 190, 400, 190);
  [[90, mx, "f1", "Next X"], [250, my, "f4", "Next Y"]].forEach(([bx, v, c, l]) => { o += SV.rect(bx, 190 - 12 * v, 90, 12 * v, c) + SV.text(bx + 45, 190 - 12 * v - 8, Lib.fmtN(v, 2), "lbl bd", { "text-anchor": "middle" }) + SV.text(bx + 45, 212, l + " (MU per $)", "sm", { "text-anchor": "middle" }); });
  $("#labN").innerHTML = o;
}
Lib.slider($("#g6"), { id: "ax", label: "Units of X bought so far ($4 each): ", min: 0, max: 6, step: 1, value: 2, fmt: (v) => v, onInput: labNext });
Lib.slider($("#g7"), { id: "ay", label: "Units of Y bought so far ($2 each): ", min: 0, max: 6, step: 1, value: 2, fmt: (v) => v, onInput: labNext });

Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Rational consumer", "A consumer who aims to maximise utility"],
  ["Budget constraint", "The limit on spending set by income and prices"],
  ["Marginal utility per dollar", "MU divided by the price of the good"],
  ["Equi-marginal principle", "Utility is maximised when MU ÷ price is equal across goods"],
  ["Consumer equilibrium", "The bundle that gives the most total utility from a budget"],
  ["Marginal utility of money", "The extra utility from one more dollar, assumed constant"],
], done: "Six words for equilibrium." });
Lib.order($("#o1"), { prompt: "Put the explanation of consumer equilibrium in order.", items: [
  "The consumer has a limited income and faces prices for two goods",
  "The consumer aims to maximise total utility",
  "Compare the marginal utility per dollar of each good: MUx ÷ Px and MUy ÷ Py",
  "If one ratio is higher, switch spending towards that good",
  "As more of it is bought its MU falls, and as less of the other is bought its MU rises",
  "At equilibrium MUx ÷ Px = MUy ÷ Py and total utility is at its maximum",
], done: "Always use two goods and the prices." });
Lib.calc($("#c1"), { qs: [
  { q: "MUx is 12 and Px is $4. What is the marginal utility per dollar of X?", a: 3, sol: "12 ÷ 4 = <b>3</b> utils per $." },
  { q: "A consumer is in equilibrium. MUx = 24, Px = $6 and Py = $3. What is MUy?", a: 12, hint: "In equilibrium MUx ÷ Px = MUy ÷ Py.", sol: "24 ÷ 6 = 4. MUy ÷ 3 = 4, so MUy = <b>12</b>." },
  { q: "MUx ÷ Px = 5 and MUy ÷ Py = 3. Should the consumer buy more X or more Y? (type X or Y)", t: ["X"], ph: "X or Y", sol: "The last dollar on X gives 5 utils, on Y only 3, so buy more <b>X</b> (and less Y) until the ratios are equal." },
  { q: "A consumer has bought 2 units of X (Px = $4) and 2 of Y (Py = $2). The next X gives 16 utils and the next Y gives 9. Which gives more utility per dollar? (type X or Y)", t: ["Y"], ph: "X or Y", sol: "X: 16 ÷ 4 = 4. Y: 9 ÷ 2 = 4.5. The next dollar should go to <b>Y</b>." },
  { q: "At the $24 budget optimum the consumer buys 4 units of X (total 72 utils) and 4 of Y (total 42 utils). What is the total utility?", a: 114, sol: "72 + 42 = <b>114</b>." },
  { q: "Check the budget: 4 units of X at $4 and 4 units of Y at $2. How much is spent ($)?", a: 24, sol: "16 + 8 = <b>$24</b>: the whole income is spent." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A consumer maximises utility when:", opts: ["MUx = MUy", "TUx = TUy", "MUx ÷ Px = MUy ÷ Py", "Px = Py"], a: 2, why: "Equal marginal utility per dollar. Option A ignores prices." },
  { q: "The equi-marginal principle says total utility is greatest when:", opts: ["MUx = MUy", "TUx = TUy", "marginal utility per dollar is equal across goods", "prices are equal"], a: 2, why: "The rule is about utility per dollar." },
  { q: "A consumer has MUx ÷ Px = 6 and MUy ÷ Py = 3. To raise total utility the consumer should:", opts: ["buy more Y", "buy more X and less Y", "buy more of both", "do nothing"], a: 1, why: "The last dollar on X gives more utility, so switch spending towards X." },
  { q: "As a consumer buys more X, MUx:", opts: ["rises", "falls", "stays constant", "becomes infinite"], a: 1, why: "Diminishing marginal utility lowers the ratio until it equals the other good's." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Equi-marginal principle", "Utility is maximised when MU ÷ price is the same for every good."],
  ["Rational consumer", "A consumer who aims to maximise utility given income and prices."],
  ["Marginal utility of money", "The extra utility from one more dollar. Assumed constant in simple MU theory."],
  ["Budget constraint", "Spending cannot exceed income, given prices."],
  ["MU per dollar", "Marginal utility divided by price."],
  ["Consumer equilibrium", "The bundle where MU per dollar is equal for every good, so total utility is maximised."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Oct/Nov 2022 · 31 · Q4] What is a correct statement of the equi-marginal utility rule?", opts: ["The marginal utility of X must equal the marginal utility of Y.", "The marginal utility of X divided by the price of X must equal the marginal utility of Y divided by the price of Y.", "The marginal utility of X divided by the price of Y must equal the marginal utility of Y divided by the price of Y.", "The price of X must equal the price of Y."], a: 1, why: "Each good's MU is divided by its own price. C mixes up the prices." },
  { q: "[Oct/Nov 2024 · 32 · Q1] If consumers aim to maximise their utility, how will they arrange their spending?", opts: ["to obtain the same total utility from each commodity", "to obtain the same total utility per $ spent on each commodity", "to obtain the same utility from the last unit of each commodity", "to obtain the same utility from the last $ spent on each commodity"], a: 3, why: "Equal marginal utility per dollar: the last $ on each good gives the same utility." },
  { q: "[May/June 2025 · 31 · Q1] What is the equi-marginal principle?", opts: ["As consumption of a product increases, the satisfaction from consumption of the product decreases by an equal amount.", "Consumers maximise utility where their marginal valuation for each product consumed is the same.", "The total satisfaction received by consumers from consumption of a product is constant.", "The marginal utility derived by consumers from the consumption of one more unit of a product is constant."], a: 1, why: "The marginal valuation per dollar is equalised across products. A and D describe constant MU, which is not the principle." },
  { q: "[May/June 2020 · 31 · Q4] An individual consumes goods X and Y. The marginal utility of good X is positive and falling. The consumer is at the point where the ratio of the marginal utility of the two goods is equal to the ratio of their prices. What can be concluded?", opts: ["the consumer will continue to consume additional units of X until marginal utility is zero", "the consumer will purchase more of X if the price of Y rises", "total utility will be negative on the additional unit of X consumed", "total utility will be rising at an increasing rate on the additional unit of X consumed"], a: 1, why: "If Py rises, MUy ÷ Py falls below MUx ÷ Px, so the consumer shifts to X. The consumer is in equilibrium, so would not keep consuming X to zero MU." },
] });
