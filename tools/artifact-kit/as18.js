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

/* ---------- grid ---------- */
function gridDraw(s) {
  let o = SV.rect(90, 40, 310, 130, "f1", op(0.15)) + SV.rect(400, 40, 310, 130, "f1", op(0.15)) + SV.rect(90, 170, 310, 130, "f1", op(0.15)) + SV.rect(400, 170, 310, 130, "f1", op(0.15));
  o += SV.text(245, 28, "Excludable", "lbl bd", { "text-anchor": "middle" }) + SV.text(555, 28, "Non-excludable", "lbl bd", { "text-anchor": "middle" }) + SV.text(82, 110, "Rival", "lbl bd", { "text-anchor": "end" }) + SV.text(82, 240, "Non-rival", "lbl bd", { "text-anchor": "end" });
  const q = (x, y, t, sub, c, k) => (k > 0 ? SV.rect(x, y, 310, 130, c, op(0.45 * k)) + SV.text(x + 155, y + 56, t, "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text(x + 155, y + 82, sub, "sm", { "text-anchor": "middle", ...op(k) }) : "");
  o += q(90, 40, "PRIVATE GOOD", "bread, a haircut, school meals", "f3", s.a) + q(400, 170, "PUBLIC GOOD", "national defence, street lighting", "f2", s.b) + q(400, 40, "Common resource (in between)", "fish in the open sea", "f1", s.c) + q(90, 170, "Club good (in between)", "a cinema seat when the film is half empty", "f1", s.c);
  if (s.d > 0) o += SV.text(400, 322, "FREE GOOD: not scarce (e.g. fresh air), no opportunity cost: outside this grid", "lbl bd", { "text-anchor": "middle", style: "fill:var(--accent)", ...op(s.d) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 335" role="img" aria-label="A grid of rival and excludable goods: private goods, public goods and in-between cases">${gridDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 335, label: "A grid of rival and excludable goods showing private goods, public goods and free goods", base: { a: 0, b: 0, c: 0, d: 0 }, draw: gridDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Private (economic) goods</b> are rival and excludable. A loaf of bread eaten by one person is gone, and the shop can refuse a customer who does not pay. They are scarce and have a price.", s: { a: 1 } },
  { cap: "<b>Public goods</b> are non-rival and non-excludable. Street lighting helps everyone and cannot be withheld from those who did not pay.", s: { a: 1, b: 1 } },
  { cap: "<b>In between</b> are goods that are only partly rival or excludable, such as a half-empty cinema or fish in the open sea. A beach is a good example of a quasi-public good.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Free goods</b> are a separate idea: they are not scarce, so there is no opportunity cost. Do not confuse them with goods that are only free of charge.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- free rider ---------- */
function frDraw(s) {
  let o = SV.text(40, 26, "Four neighbours each value a street lamp at $30. The lamp costs $100.", "lbl bd");
  for (let i = 0; i < 4; i++) { const x = 70 + i * 160; o += SV.circle(x + 40, 80, 20, "dot1", op(0.8)) + SV.text(x + 40, 130, "Neighbour " + (i + 1), "sm", { "text-anchor": "middle" }); if (s.v > 0) o += SV.text(x + 40, 150, "values it at $30", "sm", { "text-anchor": "middle", ...op(s.v) }); if (s.w > 0) o += SV.rect(x + 5, 170, 70, 36, "f2", op(0.5 * s.w)) + SV.text(x + 40, 193, "pays $0", "lbl bd", { "text-anchor": "middle", ...op(s.w) }); if (s.t > 0) o += SV.rect(x + 5, 215, 70, 36, "f3", op(0.6 * s.t)) + SV.text(x + 40, 238, "tax $25", "lbl bd", { "text-anchor": "middle", ...op(s.t) }); }
  if (s.w > 0) o += SV.text(380, 285, "Voluntary: total paid $0. The lamp is not built.", "lbl bd", { "text-anchor": "middle", style: "fill:var(--bad)", ...op(s.w) });
  if (s.t > 0) o += SV.text(380, 310, "Tax: 4 × $25 = $100. The lamp is built and every neighbour gains $30.", "lbl bd", { "text-anchor": "middle", style: "fill:var(--good)", ...op(s.t) });
  return o;
}
Lib.stepper($("#stF"), { w: 760, h: 325, label: "Four neighbours, a street lamp, free riding and a tax", base: { v: 0, w: 0, t: 0 }, draw: frDraw, tween: 800, dwell: 5800, steps: [
  { cap: "<b>The benefit.</b> Each of four neighbours gets $30 of value from a street lamp, so the total benefit is $120, which is more than its $100 cost. It would be worth building.", s: { v: 1 } },
  { cap: "<b>Free riding.</b> Once the lamp is built, no neighbour can be excluded. Each hopes the others will pay, so each pays nothing. A firm collects no revenue, so it will not build the lamp. The market fails.", s: { v: 1, w: 1 } },
  { cap: "<b>The government solution.</b> A tax of $25 on each neighbour pays for the lamp. Everyone is better off: they pay $25 and get $30 of benefit.", s: { v: 1, w: 1, t: 1 } },
] });
$("#pic2").innerHTML = `<svg viewBox="0 0 760 325" role="img" aria-label="Four neighbours who each value a street lamp at 30 dollars, voluntary payment fails and a tax of 25 dollars each succeeds">${frDraw({ v: 1, w: 1, t: 1 })}</svg>`;

/* ---------- Lab 1 ---------- */
function labK() {
  if (!$("#rv1") || !$("#ex")) return;
  const r = +$("#rv1").value, e = +$("#ex").value, rt = r >= 50, et = e >= 50, type = rt && et ? "Private good" : !rt && !et ? "Public good" : rt && !et ? "Common resource" : "Club good", ex = rt && et ? "bread, a haircut, school lunches" : !rt && !et ? "national defence, street lighting, a lighthouse" : rt && !et ? "fish in the open sea, a crowded free beach" : "a half-empty cinema, a toll motorway at quiet times";
  $("#r1").textContent = rt ? "Rival" : "Non-rival"; $("#r2").textContent = et ? "Excludable" : "Non-excludable"; $("#r3").textContent = type;
  $("#rv").textContent = `${rt ? "Rival" : "Non-rival"} and ${et ? "excludable" : "non-excludable"}: a ${type.toLowerCase()}, for example ${ex}. ${type === "Public good" ? "A free market will not supply it because people can free ride, so the government provides it." : type === "Private good" ? "A free market can supply it because non-payers are excluded and each unit is used by one person." : "This good is in between the two main types, so the market may supply it only partly."}`;
  const X = (v) => 40 + v * 3.4, Y = (v) => 270 - v * 2.4; let o = SV.rect(40, 30, 170, 120, "f1", op(0.15)) + SV.rect(210, 30, 170, 120, "f1", op(0.15)) + SV.rect(40, 150, 170, 120, "f1", op(0.15)) + SV.rect(210, 150, 170, 120, "f1", op(0.15));
  o += SV.text(125, 22, "Non-excludable", "sm", { "text-anchor": "middle" }) + SV.text(295, 22, "Excludable", "sm", { "text-anchor": "middle" }) + SV.text(125, 288, "PUBLIC", "sm", { "text-anchor": "middle" }) + SV.text(295, 288, "CLUB", "sm", { "text-anchor": "middle" }) + SV.text(125, 50, "COMMON RESOURCE", "sm", { "text-anchor": "middle" }) + SV.text(295, 50, "PRIVATE", "sm", { "text-anchor": "middle" });
  o += SV.circle(X(e), Y(r), 9, "dot4"); $("#labA").innerHTML = o + SV.text(400, 300, "Excludability →", "sm", { "text-anchor": "end" }) + SV.text(4, 16, "Rivalry ↑", "sm");
}
Lib.slider($("#g1"), { id: "rv1", label: "Rivalry (0 = non-rival, 100 = very rival) ", min: 0, max: 100, step: 5, value: 20, fmt: (v) => v, onInput: labK });
Lib.slider($("#g2"), { id: "ex", label: "Excludability (0 = cannot exclude, 100 = easy) ", min: 0, max: 100, step: 5, value: 10, fmt: (v) => v, onInput: labK });
labK();

/* ---------- Lab 2 ---------- */
function labF() {
  if (!$("#nn") || !$("#bb") || !$("#ee")) return;
  const n = +$("#nn").value, b = +$("#bb").value, e = +$("#ee").value / 100, ben = n * b, rev = ben * e, cost = 1000, ok = rev >= cost, soc = ben >= cost;
  $("#t1").textContent = "$" + ben.toLocaleString("en-US"); $("#t2").textContent = "$" + Math.round(rev).toLocaleString("en-US"); $("#t3").textContent = ok ? "Market provides it" : soc ? "Worth building, market will not" : "Not worth building";
  $("#tv").textContent = ok ? `A private firm can collect $${Math.round(rev).toLocaleString("en-US")} from those it can exclude, which covers the $1,000 cost, so it will build the lamp. Because most users can be made to pay, the good behaves like a private good.` : soc ? `The residents together gain $${ben.toLocaleString("en-US")}, more than the $1,000 cost, so the lamp is worth building. But the firm can only charge ${Lib.fmtN(e * 100, 0)}% of users, so it collects $${Math.round(rev).toLocaleString("en-US")} and makes a loss. The market will not supply it: the free rider problem. The government could tax residents and build it.` : "The total benefit is less than the cost, so it would not be worth building even if everyone paid.";
  const Y = (v) => 270 - v / Math.max(2000, ben) * 220; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(46, 22, "$", "sm");
  [["Cost", cost, "f2"], ["Total benefit", ben, "f3"], ["Revenue firm can collect", rev, "f1"]].forEach(([l, v, c], i) => { const x = 55 + i * 115; o += SV.rect(x, Y(v), 80, 270 - Y(v), c, op(0.75)) + SV.text(x + 40, 290, l.split(" ").slice(0, 2).join(" "), "sm", { "text-anchor": "middle" }) + tag(x + 40, Y(v) - 6, "$" + Math.round(v).toLocaleString("en-US"), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "nn", label: "Number of residents ", min: 5, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labF });
Lib.slider($("#g4"), { id: "bb", label: "Value each places on the lamp, $ ", min: 5, max: 60, step: 5, value: 30, fmt: (v) => v, onInput: labF });
Lib.slider($("#g5"), { id: "ee", label: "Share of users the firm can exclude, % ", min: 0, max: 100, step: 5, value: 0, fmt: (v) => v + "%", onInput: labF });
labF();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which type of good is it?", buckets: [{"label": "Private good"}, {"label": "Free good"}, {"label": "Public good"}], items: [{"text": "A loaf of bread", "b": 0}, {"text": "Fresh air", "b": 1}, {"text": "National defence", "b": 2}, {"text": "School lunches provided free by the government", "b": 0}, {"text": "Sunshine on a clear day", "b": 1}, {"text": "Street lighting", "b": 2}, {"text": "A haircut", "b": 0}, {"text": "A lighthouse beam", "b": 2}], done: "Private: rival and excludable. Free: not scarce. Public: non-rival and non-excludable." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Rivalry", "One person's use reduces what is left for others"], ["Excludability", "Non-payers can be kept from using the good"], ["Free rider", "Someone who benefits without paying"], ["Public good", "Non-rival and non-excludable"], ["Free good", "Not scarce and has zero opportunity cost"], ["Quasi-public good", "A good that is partly rival or excludable"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the free rider problem in order.", items: ["A good is non-excludable, so non-payers cannot be kept out", "Each person has an incentive to let others pay", "Few or no people pay voluntarily", "A private firm earns no revenue and will not supply the good", "The government supplies it and pays for it through taxation"], done: "Non-excludability leads to free riding, which leads to market failure." });
Lib.calc($("#c1"), { qs: [
  {"q": "A street lamp costs $1,000. 40 residents each value it at $30. What is the total benefit ($)?", "a": 1200, "unit": "$", "tol": 1, "hint": "40 × 30.", "sol": "<b>$1,200</b>, more than the cost."},
  {"q": "A tax raises the $1,000 equally from the 40 residents. How much does each pay ($)?", "a": 25, "unit": "$", "tol": 0.5, "hint": "1,000 ÷ 40.", "sol": "<b>$25</b>. Each gets $30 of benefit, so everyone gains $5."},
  {"q": "A firm can charge only 10% of the residents (because the rest cannot be excluded). Each pays $30. What revenue does it collect ($)?", "a": 120, "unit": "$", "tol": 1, "hint": "4 residents × 30.", "sol": "4 × 30 = <b>$120</b>, far below the $1,000 cost."},
  {"q": "Using the figures above, what is the firm's profit or loss ($, use a minus sign for a loss)?", "a": -880, "unit": "$", "tol": 1, "hint": "120 − 1,000.", "sol": "<b>−$880</b>: the market will not provide it."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A public good is:", opts: ["Non-rival and non-excludable", "Rival and excludable", "Any good supplied by the government", "A good that has no price"], a: 0, why: "Both characteristics define a public good." },
  { q: "Why will a free market not supply a pure public good?", opts: ["Free riders mean no revenue", "It is too cheap", "Consumers do not want it", "It has no opportunity cost"], a: 0, why: "Firms cannot make a profit if non-payers cannot be excluded." },
  { q: "A free good is one that:", opts: ["Is not scarce and has zero opportunity cost", "Is free of charge to users", "Is provided by the government", "Is non-rival and non-excludable"], a: 0, why: "Free of charge is not the same as free." },
  { q: "School lunches provided free by a government are:", opts: ["Private goods", "Public goods", "Free goods", "Demerit goods"], a: 0, why: "They are rival and excludable." },
  { q: "Which could make a public good into a private good?", opts: ["Technology that makes it excludable", "A rise in taxes", "More free riders", "A fall in demand"], a: 0, why: "If non-payers can be excluded, a charge is possible." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Private good", "Rival and excludable."],
  ["Public good", "Non-rival and non-excludable."],
  ["Free good", "Not scarce; zero opportunity cost."],
  ["Free rider", "Benefits without paying."],
  ["Free of charge", "Not the same as a free good."],
  ["Quasi-public", "Partly rival or excludable."],
  ["Provision", "Public goods: government, tax-funded."],
  ["Technology", "Can make a good excludable."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is a necessary characteristic of a public good? (May/June 2020 · 11 · Q18, reworded)", opts: ["It has a fixed maximum price", "It has an opportunity cost of production of zero", "It is non-excludable", "It is an essential good"], a: 2, why: "Non-excludability, together with non-rivalry, defines a public good. Public goods have an opportunity cost, because they use resources." },
  { q: "Which statement is correct? (Oct/Nov 2020 · 12 · Q2, reworded)", opts: ["Private goods are both non-rival and non-excludable", "Private goods are only provided by the private sector", "Public goods are both non-rival and non-excludable", "Public goods do not incur opportunity costs"], a: 2, why: "Public goods are non-rival and non-excludable. Private goods can be provided by the state, and public goods use resources." },
  { q: "What is characterised as a free good? (Oct/Nov 2020 · 13 · Q2, reworded)", opts: ["One that has zero opportunity cost", "One that is non-excludable and non-rivalrous", "One that is supplied by the government with no charge", "One that receives a 100% government subsidy"], a: 0, why: "A free good is not scarce and has no opportunity cost. Option B describes a public good, and C and D describe goods free of charge." },
  { q: "A local council provides a tap for drinking water in a town. Would this make drinking water a free good? (Oct/Nov 2022 · 11 · Q2, reworded)", opts: ["No, because it is possible to exclude some people from using the tap", "No, because it requires the use of scarce resources", "Yes, because it is available to all passers-by", "Yes, because it is impossible to charge for it"], a: 1, why: "The water is provided free of charge, but it uses scarce resources (pipes, pumping, labour), so it has an opportunity cost and is not a free good." },
  { q: "What is an example of a free good? (Oct/Nov 2023 · 13 · Q4, reworded)", opts: ["A government sponsoring a free vaccination programme", "A hospital providing free treatment to the poor", "A school providing free education to outstanding students", "Anything that provides free utility but is not scarce"], a: 3, why: "A free good is not scarce. The first three are free of charge to the user but use scarce resources." },
  { q: "Which type of good does not consume scarce resources? (Oct/Nov 2024 · 13 · Q2, reworded)", opts: ["Economic good", "Free good", "Merit good", "Public good"], a: 1, why: "Only a free good uses no scarce resources and has zero opportunity cost." },
  { q: "Which statement is not correct? (Oct/Nov 2024 · 11 · Q3, reworded)", opts: ["Addictive drugs are regarded as demerit goods because users are unaware of the full damage they do", "Air is regarded as a free good because its use has no opportunity cost", "National defence is regarded as a public good because one citizen consuming it reduces the amount available to others", "Visits to a doctor are regarded as private goods partly because they are rival"], a: 2, why: "National defence is a public good because it is non-rival: one citizen's consumption does not reduce what is available to others." },
  { q: "A government department provides milk at no charge to very low-income families. Which term best describes the milk? (May/June 2021 · 13 · Q1, reworded)", opts: ["Free good", "Inferior good", "Private good", "Public good"], a: 2, why: "Milk is rival and excludable, so it is a private good even though the state provides it free of charge." },
  { q: "How can a public good become a private good? (May/June 2025 · 11 · Q5, reworded)", opts: ["Consumers are dissatisfied with the performance of state-run services", "New technological developments make the good excludable", "The government privatises the industry producing the good", "The price of the good increases so it becomes more profitable"], a: 1, why: "If technology makes it possible to exclude non-payers, the good is no longer a public good." },
  { q: "A good is provided by the government. Consumption by one person does not affect the amount of the good available for others. Which type of good must this be? (Oct/Nov 2020 · 11 · Q17, reworded)", opts: ["Complementary good", "Merit good", "Private good", "Public good"], a: 3, why: "Consumption by one person leaving the amount available unaffected is non-rivalry, a feature of a public good." },
  { q: "A tourist visits a government-owned tropical beach. She pays $10 to enter but finds it overcrowded. Which type of good is the beach? (May/June 2025 · 13 · Q1, reworded)", opts: ["A free good", "An inferior good", "A public good", "A private good"], a: 3, why: "The entry fee shows it is excludable and overcrowding shows it is rival, so in this case it is a private good." },
  { q: "A country's health care is funded by taxation but can be used free of charge by patients. Which type of good is health care in this country? (Oct/Nov 2023 · 11 · Q3, reworded)", opts: ["Demerit good", "Free good", "Private good", "Public good"], a: 2, why: "A doctor's time and hospital beds are rival and excludable, so health care is a private good provided by the state." },
] });
