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

/* ---------- scarcity -> choice -> opportunity cost ---------- */
function chainDraw(s) {
  const box = (x, y, w, h, t, sub, c, k) => (k > 0 ? SV.rect(x, y, w, h, c, op(0.5 * k)) + SV.text(x + w / 2, y + 30, t, "lbl bd", { "text-anchor": "middle", ...op(k) }) + sub.split("|").map((l, i) => SV.text(x + w / 2, y + 56 + i * 17, l, "sm", { "text-anchor": "middle", ...op(k) })).join("") : "");
  const ar = (x1, x2, k) => (k > 0 ? SV.line(x1, 100, x2, 100, "c1", { "stroke-width": 2.5, ...op(k) }) + SV.arrowHead(x2, 100, "r", "dot1") : "");
  let o = box(30, 50, 200, 100, "Scarcity", "Wants are unlimited,|resources are limited", "f2", s.a) + ar(232, 272, s.b) + box(274, 50, 200, 100, "Choice", "Individuals, firms and|governments must pick", "f1", s.b) + ar(476, 516, s.c) + box(518, 50, 210, 100, "Opportunity cost", "The next best alternative|that is given up", "f3", s.c);
  if (s.d > 0) o += tag(380, 200, "Every choice has a cost, even when the price is zero.", "t4", s.d, "middle") + SV.line(60, 176, 700, 176, "c4 dash", op(s.d));
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 230, label: "Scarcity leads to choice and choice has an opportunity cost", base: { a: 0, b: 0, c: 0, d: 0 }, draw: chainDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Scarcity.</b> People want more than can be produced. Resources (land, labour, capital, enterprise) are limited, so not every want can be satisfied.", s: { a: 1 } },
  { cap: "<b>Choice.</b> Because of scarcity, individuals must choose how to spend income and time, firms how to use resources, and governments how to spend the budget.", s: { a: 1, b: 1 } },
  { cap: "<b>Opportunity cost.</b> Choosing one thing means giving up others. The opportunity cost is the value of the next best alternative that is given up.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>The result.</b> Every choice has a cost, even if the price is zero, because the resources used could have been used another way.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });
$("#pic1").innerHTML = `<svg viewBox="0 0 760 230" role="img" aria-label="Scarcity leads to choice and choice has an opportunity cost">${chainDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;

/* ---------- the next best alternative ---------- */
const HOL = [["Barcelona", 9], ["Paris", 8], ["London", 6], ["Venice", 6]];
function holDraw(s) {
  let o = SV.line(60, 250, 730, 250) + SV.line(60, 250, 60, 30) + SV.text(66, 22, "Family's preference score (10 = best)", "sm");
  HOL.forEach(([n, v], i) => { const k = Math.max(0, Math.min(1, s.a - i * 0.0)), x = 110 + i * 150, h = v * 20; o += SV.rect(x, 250 - h, 90, h, i === 0 && s.b > 0 ? "f3" : i === 1 && s.c > 0 ? "f2" : "f1", op(0.7)) + SV.text(x + 45, 270, n, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 45, 250 - h - 8, v, "lbl bd", { "text-anchor": "middle" }); });
  if (s.b > 0) o += tag(155, 250 - 9 * 20 - 28, "chosen", "t3", s.b, "middle");
  if (s.c > 0) o += tag(305, 250 - 8 * 20 - 28, "opportunity cost", "t2", s.c, "middle");
  return o;
}
Lib.stepper($("#stO"), { w: 760, h: 285, label: "Four holiday options ranked by preference with the chosen option and its opportunity cost", base: { a: 1, b: 0, c: 0 }, draw: holDraw, tween: 700, dwell: 5600, steps: [
  { cap: "<b>Four options.</b> The family ranks them by preference. Each costs the same, so only one can be chosen.", s: { a: 1 } },
  { cap: "<b>The choice.</b> The family goes to Barcelona, its first preference.", s: { a: 1, b: 1 } },
  { cap: "<b>The opportunity cost</b> is the next best alternative given up: <b>Paris</b>, the second preference. The family gives up all three other holidays, but the opportunity cost is the value of only the best of them.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labB() {
  if (!$("#hs")) return;
  const h = +$("#hs").value, sch = 100 - h;
  $("#r1").textContent = "$" + h + "m"; $("#r2").textContent = "$" + sch + "m"; $("#r3").textContent = "$10m of the other";
  $("#rv").textContent = `With $${h}m on hospitals, only $${sch}m is left for schools. Each extra $10m for hospitals means $10m less for schools, so the opportunity cost of more hospital spending is the schools forgone. The total never rises above $100m: that is scarcity.`;
  let o = SV.line(40, 120, 400, 120) + SV.text(40, 40, "Budget: $100m", "lbl bd");
  o += SV.rect(40, 130, h * 3.6, 60, "f1", op(0.7)) + SV.rect(40 + h * 3.6, 130, sch * 3.6, 60, "f3", op(0.7)) + SV.text(40 + h * 1.8, 166, "Hospitals $" + h + "m", "lbl bd", { "text-anchor": "middle" }) + (sch > 14 ? SV.text(40 + h * 3.6 + sch * 1.8, 166, "Schools $" + sch + "m", "lbl bd", { "text-anchor": "middle" }) : "");
  o += SV.line(40, 200, 400, 200, "ax") + tag(220, 226, "Every $10m moved to one is $10m taken from the other", "t4", 1, "middle");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "hs", label: "Spending on hospitals, $m ", min: 0, max: 100, step: 10, value: 60, fmt: (v) => v, onInput: labB });
labB();

/* ---------- Lab 2 ---------- */
const HN = ["Barcelona", "London", "Paris", "Venice"];
function labH() {
  if (!$("#h0") || !$("#h1") || !$("#h2") || !$("#h3")) return;
  const v = [0, 1, 2, 3].map((i) => +$("#h" + i).value), mx = Math.max(...v), best = v.map((x, i) => (x === mx ? i : -1)).filter((i) => i >= 0), rest = v.map((x, i) => (best.includes(i) ? -1 : x));
  const mx2 = Math.max(...rest), second = mx2 < 0 ? [] : rest.map((x, i) => (x === mx2 ? i : -1)).filter((i) => i >= 0);
  $("#t1").textContent = best.length > 1 ? "Tie: " + best.map((i) => HN[i]).join(" / ") : HN[best[0]]; $("#t2").textContent = best.length > 1 ? "Another top option" : second.map((i) => HN[i]).join(" and ") || "none"; $("#t3").textContent = "3 options";
  $("#tv").textContent = best.length > 1 ? "Two or more destinations tie for first place, so the family must still pick one; the opportunity cost is then the tied option given up." : `The family chooses ${HN[best[0]]} (score ${mx}). The opportunity cost is the next best alternative, ${second.map((i) => HN[i]).join(" and ")} (score ${mx2}), not the total of everything else given up.`;
  const Y = (x) => 250 - x * 20; let o = SV.line(40, 250, 400, 250) + SV.line(40, 250, 40, 30);
  v.forEach((x, i) => { const px = 60 + i * 85, cls = best.includes(i) ? "f3" : second.includes(i) ? "f2" : "f1"; o += SV.rect(px, Y(x), 60, 250 - Y(x), cls, op(0.75)) + SV.text(px + 30, 270, HN[i], "sm", { "text-anchor": "middle" }) + tag(px + 30, Y(x) - 6, x, "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
HN.forEach((n, i) => Lib.slider($("#g" + (3 + i)), { id: "h" + i, label: n + " ", min: 1, max: 10, step: 1, value: [9, 6, 8, 6][i], fmt: (v) => v, onInput: labH }));
labH();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Who is making the choice?", buckets: [{"label": "Individual"}, {"label": "Firm"}, {"label": "Government"}], items: [{"text": "Deciding whether to spend a weekend studying or working", "b": 0}, {"text": "Choosing between buying a new machine and hiring more workers", "b": 1}, {"text": "Deciding whether to spend more on hospitals or on defence", "b": 2}, {"text": "Choosing which phone to buy with a birthday gift", "b": 0}, {"text": "Deciding which of two products to make with limited factory space", "b": 1}, {"text": "Choosing between cutting taxes and building new roads", "b": 2}, {"text": "Deciding between a job offer and further study", "b": 0}, {"text": "Choosing between expanding abroad and raising output at home", "b": 1}], done: "Individuals, firms and governments all face scarcity and make choices." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Scarcity", "Unlimited wants but limited resources"], ["Choice", "Selecting between alternatives because of scarcity"], ["Opportunity cost", "The next best alternative given up"], ["What to produce", "Which goods and services, and how much of each"], ["How to produce", "Which methods and resources to use"], ["For whom to produce", "Who receives the output"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order.", items: ["Wants are unlimited", "Resources are limited, so scarcity exists", "Individuals, firms and governments must choose", "Choosing one option means giving up others", "The value of the next best alternative is the opportunity cost"], done: "Scarcity leads to choice, and choice has an opportunity cost." });
Lib.calc($("#c1"), { qs: [
  {"q": "A firm makes 100 units of Y and 200 units of X. To make 120 units of Y it can make only 170 units of X. How many units of X are given up (opportunity cost of the extra Y)?", "a": 30, "unit": "units", "tol": 0.5, "hint": "200 − 170.", "sol": "<b>30 units of X</b>."},
  {"q": "In that example, what is the opportunity cost of one extra unit of Y, in units of X (1 decimal place)?", "a": 1.5, "unit": "units", "tol": 0.05, "hint": "30 ÷ 20.", "sol": "30 ÷ 20 = <b>1.5 units of X</b>."},
  {"q": "A government has $200m and spends $120m on hospitals. How much is left for schools ($m)?", "a": 80, "unit": "$m", "tol": 0.5, "hint": "200 − 120.", "sol": "<b>$80m</b>. The opportunity cost of the hospital spending is the schools that $120m could have funded."},
  {"q": "A worker earns $30 an hour and spends 4 hours at a concert instead of working. How much pay is given up ($)?", "a": 120, "unit": "$", "tol": 0.5, "hint": "30 × 4.", "sol": "<b>$120</b> of forgone pay: part of the opportunity cost."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Scarcity exists because:", opts: ["Wants are unlimited and resources are limited", "Prices are too high", "Governments restrict supply", "Income is unequally shared"], a: 0, why: "Scarcity is the gap between limitless wants and limited resources." },
  { q: "Which is an opportunity cost of a government building a new road?", opts: ["The hospitals that the money could have paid for", "The cost of the road in taxes", "All other uses of the money together", "The profit of the road builder"], a: 0, why: "It is the next best use of the funds." },
  { q: "Scarcity differs from a shortage because scarcity:", opts: ["Cannot be removed by a price change", "Only affects poor countries", "Is temporary", "Applies only to goods that are imported"], a: 0, why: "A shortage is a market condition at a price, whereas scarcity is permanent." },
  { q: "Which is NOT one of the three basic economic questions?", opts: ["Where to produce", "What to produce", "How to produce", "For whom to produce"], a: 0, why: "The three questions are what, how and for whom." },
  { q: "Opportunity cost is best defined as:", opts: ["The value of the next best alternative given up", "The money price of a good", "The cost of producing a good", "The total cost of all alternatives"], a: 0, why: "It is the single next best alternative." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Fundamental economic problem", "Scarcity: unlimited wants, limited resources."],
  ["Choice", "Needed at every level: individuals, firms, governments."],
  ["Opportunity cost", "The next best alternative given up."],
  ["Scarcity vs shortage", "Scarcity is permanent; a shortage is a market condition."],
  ["What to produce", "Which goods and how much."],
  ["How to produce", "Methods and resources used."],
  ["For whom to produce", "Who gets the output."],
  ["Opportunity cost in units", "Units of one good given up for units of another."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "An American family chooses between four holiday destinations at the same price. Their order of preference is Barcelona 1st, Paris 2nd, London and Venice joint 3rd. If they go to Barcelona, what is the opportunity cost? (Feb/March 2021 · 12 · Q1, reworded)", opts: ["Barcelona", "London and Venice", "Paris", "London, Paris and Venice"], a: 2, why: "Opportunity cost is the next best alternative given up, which is the second choice, Paris. It is not all the others." },
  { q: "Why does the basic economic problem of scarcity apply to both the rich and the poor? (Feb/March 2023 · 12 · Q10, reworded)", opts: ["The choices people make do not depend on income inequalities", "Consumers pay the same prices for goods and services", "Human wants exceed what can be produced from available resources", "Natural resources are unevenly distributed among nations"], a: 2, why: "Scarcity comes from unlimited wants and limited resources, so it applies at every income level." },
  { q: "Which combination best describes the basic economic problem? Resources, and wants. (Feb/March 2024 · 12 · Q3, reworded)", opts: ["Limited, limited", "Limited, unlimited", "Unlimited, limited", "Unlimited, unlimited"], a: 1, why: "Limited resources cannot meet unlimited wants." },
  { q: "What is the opportunity cost to a person of spending $20 on a new pair of sports shoes? (Feb/March 2024 · 12 · Q5, reworded)", opts: ["All the other things the person could have bought", "The cost of getting to the shop", "The current value of the old pair of shoes", "The next best thing that could have been bought with the $20"], a: 3, why: "Opportunity cost is the single next best alternative, not all alternatives and not a related cost." },
  { q: "What does opportunity cost measure? (May/June 2022 · 13 · Q3, reworded)", opts: ["The benefits of a good compared with the next choice", "The benefits given up by not consuming the next best alternative", "The costs of any good not chosen", "The financial costs of consuming a good"], a: 1, why: "It is the benefit of the next best alternative that is forgone." },
  { q: "Complete the sentence: the three basic questions arising from scarcity are ___ to produce, ___ to produce and ___ to produce. (May/June 2022 · 11 · Q3, reworded)", opts: ["How, when, where", "How, where, for whom", "What, how, for whom", "What, when, where"], a: 2, why: "The three basic questions are what, how and for whom." },
  { q: "A hospital board reallocates $800,000 of its $1.2m new buildings budget to cancer care. What is the opportunity cost of this decision? (May/June 2023 · 11 · Q2, reworded)", opts: ["A cost of $400,000", "A cost of $800,000", "The cost of healthcare for cancer patients", "The loss of some new buildings"], a: 3, why: "The opportunity cost is the next best use that is given up: some of the new buildings." },
  { q: "Why does the concept of scarcity apply to the use of fossil fuels? (May/June 2024 · 11 · Q4, reworded)", opts: ["Demand fluctuates according to price changes", "Supply is insufficient to meet demand", "Their use is restricted because of pollution", "They are being replaced by renewable energy"], a: 1, why: "Scarcity means supply cannot meet all wants, which is the case with a limited resource." },
  { q: "What is essential to eliminate scarcity? (May/June 2024 · 13 · Q4, reworded)", opts: ["The existence of sufficient resources to meet all needs and wants", "Producers consistently produce more than demand", "The government has a budget surplus", "There is equilibrium in all markets"], a: 0, why: "Only resources sufficient for all wants would remove scarcity, which in practice never happens." },
  { q: "A textbook diagram should show the terms opportunity cost, scarcity and choice in the order that identifies the fundamental economic problem. What is the correct order? (May/June 2025 · 12 · Q2, reworded)", opts: ["Choice, opportunity cost, scarcity", "Choice, scarcity, opportunity cost", "Scarcity, choice, opportunity cost", "Scarcity, opportunity cost, choice"], a: 2, why: "Scarcity forces choice, and each choice has an opportunity cost." },
  { q: "A firm produces 100 units of good Y and 200 of good X with fixed resources. To raise Y to 120 units, it can produce only 170 units of X. What is the opportunity cost of the extra 20 units of Y? (May/June 2025 · 13 · Q3, reworded)", opts: ["20 units of X", "30 units of X", "120 units of X", "170 units of X"], a: 1, why: "X falls from 200 to 170, so 30 units of X are given up." },
  { q: "A doctor with long hours and a stressful job can become a teacher. What is the opportunity cost of continuing as a doctor? (Oct/Nov 2022 · 11 · Q4, reworded)", opts: ["The risk of mistakes caused by tiredness", "The possible costs of illness from stress", "The potential salary as a teacher", "The retraining costs of becoming a teacher"], a: 2, why: "The next best alternative is working as a teacher, so the opportunity cost is the salary (and benefits) of that job." },
] });
