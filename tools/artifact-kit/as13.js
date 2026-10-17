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

/* ---------- four factors ---------- */
const FAC = [["Land", "natural resources", "Rent", "f1"], ["Labour", "human effort", "Wages", "f2"], ["Capital", "man-made equipment", "Interest", "f3"], ["Enterprise", "organises and takes risk", "Profit", "f1"]];
function facDraw(s) {
  let o = ""; FAC.forEach(([n, d, r, c], i) => { const k = Math.max(0, Math.min(1, s.a - i)), kr = Math.max(0, Math.min(1, s.r - i)), y = 16 + i * 62; if (k > 0) o += SV.rect(30, y, 230, 50, c, op(0.45 * k)) + SV.text(46, y + 22, n, "lbl bd", op(k)) + SV.text(46, y + 40, d, "sm", op(k)); if (kr > 0) o += SV.line(262, y + 25, 480, y + 25, "c1", { "stroke-width": 2.2, ...op(kr) }) + SV.arrowHead(480, y + 25, "r", "dot1") + SV.rect(484, y, 220, 50, c, op(0.7 * kr)) + SV.text(594, y + 31, r + (r === "Profit" ? " (residual)" : ""), "lbl bd", { "text-anchor": "middle", ...op(kr) }); });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 740 262" role="img" aria-label="The four factors of production and their rewards: land earns rent, labour earns wages, capital earns interest and enterprise earns profit">${facDraw({ a: 4, r: 4 })}</svg>`;
Lib.stepper($("#stF"), { w: 740, h: 262, label: "A bakery's four factors of production and the reward each earns", base: { a: 0, r: 0 }, draw: facDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Land</b> is the site and natural resources: the bakery's plot of land and the wheat fields that supply flour.", s: { a: 1, r: 0 } },
  { cap: "<b>Labour</b> is the bakers and shop assistants who do the work.", s: { a: 2, r: 0 } },
  { cap: "<b>Capital</b> is the ovens, mixers and delivery van: man-made equipment, not the money used to buy them.", s: { a: 3, r: 0 } },
  { cap: "<b>Enterprise</b> is the owner who organises everything and risks her own money.", s: { a: 4, r: 0 } },
  { cap: "<b>Rewards.</b> Land earns <b>rent</b>, labour <b>wages</b> and capital <b>interest</b>: these are agreed in advance. Enterprise earns <b>profit</b>, what is left after the others are paid. It can be negative.", s: { a: 4, r: 4 } },
] });

/* ---------- human vs physical capital ---------- */
const HV = [["Worker alone", 10, "f1"], ["+ training (human capital)", 14, "f3"], ["+ machine (physical capital)", 20, "f2"], ["Both together", 30, "f3"]];
function hcDraw(s) {
  let o = SV.line(70, 250, 730, 250) + SV.line(70, 250, 70, 30) + SV.text(76, 22, "Output per worker per day", "sm");
  HV.forEach(([l, v, c], i) => { const k = Math.max(0, Math.min(1, s.n - i)); if (k <= 0) return; const x = 110 + i * 150, h = v * 6.4 * k; o += SV.rect(x, 250 - h, 100, h, c, op(0.75)) + SV.text(x + 50, 250 - h - 8, v, "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text(x + 50, 270, l, "sm", { "text-anchor": "middle", ...op(k) }); });
  return o;
}
Lib.stepper($("#stH"), { w: 760, h: 290, label: "Output per worker rising with training, a machine and both together", base: { n: 0 }, draw: hcDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>A worker alone</b> with basic tools produces 10 units a day.", s: { n: 1 } },
  { cap: "<b>Human capital.</b> Training raises the worker's skills, so output rises to 14 units.", s: { n: 2 } },
  { cap: "<b>Physical capital.</b> A machine, even without more training, lifts output to 20 units.", s: { n: 3 } },
  { cap: "<b>Both together.</b> A trained worker using the machine produces 30 units, more than the sum of the two separate gains: skills make machines more productive.", s: { n: 4 } },
] });
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Output per worker rising from 10 to 14 with training, 20 with a machine and 30 with both">${hcDraw({ n: 4 })}</svg>`;

/* ---------- Lab 1 ---------- */
function labR() {
  if (!$("#rv1") || !$("#wg") || !$("#rn") || !$("#it")) return;
  const rev = +$("#rv1").value, w = +$("#wg").value, rn = +$("#rn").value, it = +$("#it").value, cost = w + rn + it, pf = rev - cost;
  $("#r1").textContent = "$" + cost + "k"; $("#r2").textContent = (pf >= 0 ? "+$" : "−$") + Math.abs(pf) + "k"; $("#r3").textContent = Lib.fmtN(pf / rev * 100, 1) + "%";
  $("#rv").textContent = pf >= 0 ? `Revenue of $${rev}k pays wages ($${w}k), rent ($${rn}k) and interest ($${it}k) first. The $${pf}k that is left is profit: the reward for enterprise and for taking the risk.` : `Revenue of $${rev}k is less than the $${cost}k that must be paid in wages, rent and interest. The entrepreneur makes a loss of $${-pf}k, so enterprise earns a negative reward. Wages, rent and interest still have to be paid.`;
  const sc = 250 / Math.max(rev, cost), X = 100; let y = 250, o = SV.line(60, 250, 360, 250) + SV.text(70, 28, "$ thousands", "sm");
  const seg = (v, c, l) => { const h = v * sc; y -= h; return SV.rect(X, y, 100, h, c, op(0.75)) + (h > 16 ? SV.text(X + 50, y + h / 2 + 5, l + " " + v, "lbl bd", { "text-anchor": "middle" }) : ""); };
  o += seg(w, "f1", "Wages") + seg(rn, "f2", "Rent") + seg(it, "f1", "Interest") + (pf > 0 ? seg(pf, "f3", "Profit") : "");
  o += SV.rect(240, 250 - rev * sc, 100, rev * sc, "f3", op(0.25)) + SV.text(290, 250 - rev * sc - 8, "Revenue " + rev, "lbl bd", { "text-anchor": "middle" });
  if (pf < 0) o += SV.text(X + 50, 250 - cost * sc - 8, "Costs " + cost + " (loss " + (-pf) + ")", "lbl bd", { "text-anchor": "middle", style: "fill:var(--bad)" });
  $("#labA").innerHTML = o + SV.text(X + 50, 272, "Costs", "sm", { "text-anchor": "middle" }) + SV.text(290, 272, "Revenue", "sm", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "rv1", label: "Revenue, $ thousand ", min: 50, max: 300, step: 5, value: 160, fmt: (v) => v, onInput: labR });
Lib.slider($("#g2"), { id: "wg", label: "Wages, $ thousand ", min: 20, max: 150, step: 5, value: 80, fmt: (v) => v, onInput: labR });
Lib.slider($("#g3"), { id: "rn", label: "Rent, $ thousand ", min: 5, max: 60, step: 5, value: 20, fmt: (v) => v, onInput: labR });
Lib.slider($("#g4"), { id: "it", label: "Interest, $ thousand ", min: 0, max: 40, step: 2, value: 10, fmt: (v) => v, onInput: labR });
labR();

/* ---------- Lab 2 ---------- */
function labK() {
  if (!$("#tr") || !$("#mc")) return;
  const tr = +$("#tr").value, mc = +$("#mc").value, base = 10, a = 0.8 * tr, b = 3 * mc, c = 0.45 * tr * mc, out = base + a + b + c;
  $("#t1").textContent = Lib.fmtN(out, 1) + " units"; $("#t2").textContent = "+" + Lib.fmtN(a, 1); $("#t3").textContent = "+" + Lib.fmtN(b + c, 1);
  $("#tv").textContent = `With ${tr} years of training and ${mc} machine${mc === 1 ? "" : "s"} per worker, output per worker is ${Lib.fmtN(out, 1)} units, compared with 10 for a worker with basic tools. Training adds ${Lib.fmtN(a, 1)} and machines add ${Lib.fmtN(b, 1)}, and the combination adds a further ${Lib.fmtN(c, 1)}, because skilled workers get more from the same machines.`;
  const Y = (v) => 270 - v * 3.4; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(46, 22, "Output per worker", "sm"); let y0 = 0;
  [["Base", base, "f1"], ["Training", a, "f3"], ["Machines", b, "f2"], ["Together", c, "f3"]].forEach(([l, v, cl], i) => { const x = 60 + i * 85; o += SV.rect(x, Y(y0 + v), 60, v * 3.4, cl, op(0.75)) + SV.text(x + 30, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 30, Y(y0 + v) - 6, "+" + Lib.fmtN(v, 1), "t1", 1, "middle"); y0 += v; });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g5"), { id: "tr", label: "Years of training ", min: 0, max: 10, step: 1, value: 4, fmt: (v) => v, onInput: labK });
Lib.slider($("#g6"), { id: "mc", label: "Machines per worker ", min: 0, max: 5, step: 1, value: 2, fmt: (v) => v, onInput: labK });
labK();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which factor of production is it?", buckets: [{"label": "Land"}, {"label": "Labour"}, {"label": "Capital"}, {"label": "Enterprise"}], items: [{"text": "A copper mine", "b": 0}, {"text": "A team of software engineers", "b": 1}, {"text": "A delivery van", "b": 2}, {"text": "The founder who risks her savings to start a firm", "b": 3}, {"text": "A forest", "b": 0}, {"text": "A nurse's skills and time", "b": 1}, {"text": "An oven in a bakery", "b": 2}, {"text": "A manager who organises the factors and bears the loss if sales fall", "b": 3}], done: "Land: nature's gifts. Labour: people's effort. Capital: man-made equipment. Enterprise: organising and risk-taking." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Land", "Rent"], ["Labour", "Wages"], ["Capital", "Interest"], ["Enterprise", "Profit"], ["Human capital", "Knowledge and skills of workers"], ["Physical capital", "Man-made equipment used in production"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for setting up a bakery in order.", items: ["An entrepreneur decides to start the business and takes the risk", "Land is found for the bakery", "Capital equipment such as ovens is bought", "Labour is hired and trained", "Rent, wages and interest are paid and profit is the residual"], done: "Enterprise comes first, then the other factors, then the rewards." });
Lib.calc($("#c1"), { qs: [
  {"q": "A firm has revenue of $250,000. It pays wages of $120,000, rent of $30,000 and interest of $20,000. Calculate its profit ($).", "a": 80000, "unit": "$", "tol": 1, "hint": "250,000 − 170,000.", "sol": "<b>$80,000</b>."},
  {"q": "Next year revenue falls to $150,000 but the other payments are the same. Calculate its profit or loss ($, use a minus sign for a loss).", "a": -20000, "unit": "$", "tol": 1, "hint": "150,000 − 170,000.", "sol": "<b>−$20,000</b>, a loss."},
  {"q": "Output per worker rises from 10 to 14 units after training. Calculate the percentage increase (%).", "a": 40, "unit": "%", "tol": 0.5, "hint": "4 ÷ 10.", "sol": "<b>40%</b>."},
  {"q": "Wages are $80,000 of a $200,000 total cost. What percentage of costs is wages (%)?", "a": 40, "unit": "%", "tol": 0.5, "hint": "80 ÷ 200.", "sol": "<b>40%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is the reward to enterprise?", opts: ["Profit", "Interest", "Rent", "Wages"], a: 0, why: "Enterprise earns profit; the other rewards go to the other factors." },
  { q: "Which is NOT classified as capital by economists?", opts: ["Money in a bank account", "A factory building", "A tractor", "A delivery van"], a: 0, why: "Money is financial capital, which buys factors but is not itself a factor." },
  { q: "Human capital is increased by:", opts: ["Training workers", "Buying a new machine", "Finding new oil", "Lowering interest rates"], a: 0, why: "Training raises skills and knowledge." },
  { q: "Profit differs from the other rewards because it:", opts: ["Is a residual and can be negative", "Is set by law", "Is paid first", "Is fixed in advance"], a: 0, why: "It is what is left after other rewards are paid." },
  { q: "Land in economics includes:", opts: ["Oil and fish stocks", "Machines", "Skilled workers", "Shares"], a: 0, why: "Land means all natural resources." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Land", "Natural resources; earns rent."],
  ["Labour", "Human effort; earns wages."],
  ["Capital", "Man-made equipment; earns interest."],
  ["Enterprise", "Organises and bears risk; earns profit."],
  ["Human capital", "Skills and knowledge of workers."],
  ["Physical capital", "Machines, buildings, tools."],
  ["Profit", "Residual; can be negative."],
  ["Not capital", "Money, shares and loans (financial)."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A European airline opens a new route. It buys aeroplanes, rents landing slots, hires pilots and buys back some shares. What is an example of the factor of production capital? (Oct/Nov 2021 · 11 · Q1, reworded)", opts: ["Aeroplanes", "Landing slots", "Pilots", "Shares"], a: 0, why: "Aeroplanes are human-made resources used in production. Pilots are labour; shares are financial assets." },
  { q: "Which statement about the factors of production is correct? (Oct/Nov 2021 · 12 · Q4, reworded)", opts: ["The factor capital includes shares and deposit accounts at banks", "The factor labour includes human-made resources", "The factor land includes forests and undiscovered copper", "The factor enterprise takes risks and is rewarded with interest"], a: 2, why: "Land is all natural resources, whether or not they have been discovered. Enterprise is rewarded with profit, and capital excludes financial assets." },
  { q: "A UK food company diversifying its range borrows $10m from a bank to buy land, build and equip a bakery. What would an economist not classify as a factor of production? (May/June 2021 · 13 · Q10, reworded)", opts: ["The $10m loan", "The land on which the bakery is built", "The ovens", "The soya used to make bread"], a: 0, why: "The loan is money, which pays for factors but is not itself a factor. Land, ovens and the raw material are resources." },
  { q: "Which term assumes the existence of 'qualities, knowledge and skills' that allow an individual to be more productive? (May/June 2022 · 13 · Q4, reworded)", opts: ["Enterprise investment", "Human capital", "Mechanisation", "Specialisation"], a: 1, why: "Human capital is the knowledge and skills embodied in workers." },
  { q: "Which action would not raise the quality of the particular factor of production? (Oct/Nov 2022 · 13 · Q1, reworded)", opts: ["Capital: operating a machine continuously at full capacity", "Enterprise: providing risk management advice", "Land: increasing the use of fertilisers", "Labour: making apprenticeships and training compulsory"], a: 0, why: "Using a machine harder uses it more but does not improve its quality. Fertiliser, training and advice raise quality." },
  { q: "The factors of production earn different rewards. What identifies the correct economic term for these rewards? (Oct/Nov 2024 · 13 · Q3, reworded)", opts: ["Capital: surpluses", "Enterprise: dividends", "Labour: interest", "Land: rents"], a: 3, why: "Land earns rent, labour wages, capital interest and enterprise profit." },
  { q: "The share of total incomes from profit shows more variation over time than incomes from interest, rent and wages. What is the most likely reason? (May/June 2024 · 12 · Q5, reworded)", opts: ["Interest rates are set by government", "Profit is what is left after interest, rent and wages are subtracted from total income", "Rent is only the return to the factor and so is always the smallest", "Wages only change annually"], a: 1, why: "Profit is the residual, so it absorbs all the changes in revenue and costs." },
  { q: "Which factor of production is needed first in order to set up a new business? (May/June 2023 · 12 · Q1, reworded)", opts: ["Capital", "Enterprise", "Labour", "Land"], a: 1, why: "An entrepreneur must decide to combine the other factors and take the risk, before they can be hired." },
  { q: "A country increases spending on education and training. It pays for this by reducing unemployment benefit payments and increasing taxes on imports of machinery. What is the likely effect on human capital and physical capital? (May/June 2025 · 12 · Q4, reworded)", opts: ["Human capital decreases; physical capital decreases", "Human capital decreases; physical capital increases", "Human capital increases; physical capital decreases", "Human capital increases; physical capital increases"], a: 2, why: "More education raises human capital. Taxing imports of machinery makes machines dearer, so the stock of physical capital is likely to grow more slowly." },
  { q: "A wine producer wants to expand production significantly and offers investors meals discounts if they buy 2,000 shares. Which factors of production are most likely to be involved in the expansion? (Oct/Nov 2024 · 12 · Q3, reworded)", opts: ["Labour, land, capital and enterprise", "Labour, land and capital only", "Enterprise and land only", "Enterprise only"], a: 0, why: "Expanding a wine business needs vineyards (land), workers (labour), equipment (capital) and an organiser who takes the risk (enterprise)." },
  { q: "A large farm uses labour and capital equipment as substitutes. The government subsidises capital equipment. What happens to the quantities of labour and capital used? (Oct/Nov 2024 · 13 · Q14, reworded)", opts: ["Labour decreases; capital increases", "Both decrease", "Labour increases; capital decreases", "Both increase"], a: 0, why: "Cheaper capital makes it more attractive than labour, so firms substitute capital for labour." },
] });
