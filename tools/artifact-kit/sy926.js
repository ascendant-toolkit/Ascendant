const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.slice(1).map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

/* ---------- Learn picture and Watch 1: logistic stock ---------- */
function simStock(h, r, n = 40, K = 100) { const s = [K]; let x = K; for (let t = 0; t < n; t++) { x = Math.max(0, x + r * x * (1 - x / K) - h); s.push(x); } return s; }
const SX = (t) => 70 + t * 16.5, SY = (v) => 300 - v * 2.5;
function stockDraw(s) {
  let o = axes(70, 300, 740, 40, "Years", "Fish stock") + SV.line(70, SY(100), 730, SY(100), "gr") + SV.text(66, SY(100) + 4, "100", "sm", { "text-anchor": "end" });
  [10, 20, 30, 40].forEach((t) => (o += SV.text(SX(t), 318, t, "sm", { "text-anchor": "middle" })));
  const A = simStock(s.h, 0.4), n = Math.round(s.n);
  if (s.show > 0) o += SV.path(Lib.ptsPath(A.slice(0, n + 1).map((v, i) => [SX(i), SY(v)])), s.h > 10 ? "c2" : "c3", op(1));
  if (s.show > 0) o += tag(SX(n) + 8, SY(A[n]) - 10, "harvest " + s.h + " a year", s.h > 10 ? "t2" : "t3");
  if (s.h === 10 && s.show > 0) o += tag(380, 62, "Maximum sustainable yield = 10 with regrowth 0.4", "t3", 1, "middle");
  if (s.h > 10 && s.show > 0 && A[n] < 1) o += tag(SX(n) - 8, SY(2) - 14, "stock collapses", "t2", 1, "end");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Fish stock over 40 years: stable when harvest is 8 or 10 a year, collapsing when harvest is 14 a year">${(() => { let o = axes(70, 300, 740, 40, "Years", "Resource stock") + SV.line(70, 50, 730, 50, "gr"); [[8, "c3", "harvest below regrowth: sustainable"], [10, "c1", "maximum sustainable yield"], [14, "c2", "overharvest: collapse"]].forEach(([h, c, l], i) => { const A = simStock(h, 0.4); o += SV.path(Lib.ptsPath(A.map((v, k) => [SX(k), SY(v) - 20 + 20])), c, {}); o += tag(SX(40) - 4, SY(A[40]) - 8 - (i === 1 ? 0 : 0), l, c === "c2" ? "t2" : c === "c3" ? "t3" : "t1", 1, "end"); }); return o; })()}</svg>`;
Lib.stepper($("#stR"), { w: 760, h: 340, label: "Fish stock over 40 years under three different harvest rates", base: { h: 8, n: 0, show: 0 }, draw: stockDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>A renewable resource.</b> A fish stock of 100 regrows each year: fast when it is small and plentiful food, slower as it nears its limit. There is a level of catch the stock can replace every year.", s: { h: 8, n: 0, show: 0 } },
  { cap: "<b>Harvest below regrowth.</b> Catching 8 a year is less than the stock can replace. The stock settles at a stable level and fishers can keep going. <b>This is sustainable.</b>", s: { h: 8, n: 40, show: 1 } },
  { cap: "<b>The maximum sustainable yield.</b> Catching 10 a year is the most the stock can replace at this regrowth rate. It stays stable at half its original size, with no margin for a bad year.", s: { h: 10, n: 40, show: 1 } },
  { cap: "<b>Overharvesting.</b> Catching 14 a year is more than the stock can replace. The stock falls faster and faster until it collapses. Short-run output rises, then the industry and its jobs vanish: <b>not sustainable</b>.", s: { h: 14, n: 40, show: 1 } },
] });

/* ---------- Watch 2: carbon tax ---------- */
const EX = (q) => 70 + q * 6.5, EY = (p) => 320 - p * 2.6;
function taxDraw(s) {
  const dmd = (q) => 100 - q, mpc = (q) => 10 + 0.5 * q, msc = (q) => 30 + 0.5 * q, tc = (q) => 10 + 0.5 * q + 20 * s.t;
  let o = axes(70, 320, 740, 30, "Output of the good", "Price and cost ($)");
  o += SV.line(EX(0), EY(dmd(0)), EX(100), EY(dmd(100)), "c1") + tag(EX(97), EY(dmd(97)) - 8, "Demand (MSB)", "t1", 1, "end");
  o += SV.line(EX(0), EY(mpc(0)), EX(100), EY(mpc(100)), "c2") + tag(EX(100) - 4, EY(mpc(100)) + 18, "MPC", "t2", 1, "end");
  if (s.e > 0) o += SV.line(EX(0), EY(msc(0)), EX(100), EY(msc(100)), "c3 dash", op(s.e)) + tag(EX(100) - 4, EY(msc(100)) - 10, "MSC", "t3", s.e, "end");
  if (s.t > 0) o += SV.line(EX(0), EY(tc(0)), EX(100), EY(tc(100)), "c4", op(s.t)) + tag(EX(0) + 8, EY(tc(0)) - 8, "MPC + tax", "t4", s.t);
  if (s.m > 0) o += SV.circle(EX(60), EY(40), 7, "dot2", op(s.m)) + SV.line(EX(60), EY(40), EX(60), 320, "gr", op(s.m)) + tag(EX(60) + 10, EY(40) + 22, "market: Q=60", "t2", s.m);
  if (s.o > 0) o += SV.circle(EX(46.7), EY(53.3), 7, "dot3", op(s.o)) + SV.line(EX(46.7), EY(53.3), EX(46.7), 320, "gr", op(s.o)) + tag(EX(46.7) - 10, EY(53.3) - 12, "optimum: Q=47", "t3", s.o, "end");
  if (s.w > 0) o += SV.poly([[EX(46.7), EY(53.3)], [EX(60), EY(40)], [EX(60), EY(60)]], "f2", op(s.w)) + tag(EX(63), EY(58), "welfare loss", "t2", s.w);
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 345, label: "Demand, private marginal cost and social marginal cost with a carbon tax moving output to the social optimum", base: { e: 0, t: 0, m: 0, o: 0, w: 0 }, draw: taxDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>The market ignores the damage.</b> Producers pay only their private cost (MPC). Where demand meets MPC the market produces <b>60 units</b> at a price of $40.", s: { m: 1 } },
  { cap: "<b>The external cost.</b> Burning fuel creates emissions that damage others by $20 a unit. Adding this to MPC gives the <b>marginal social cost (MSC)</b>.", s: { m: 1, e: 1 } },
  { cap: "<b>Overproduction.</b> The efficient output is where demand meets MSC: about <b>47 units</b>. The market produces too much, and the shaded triangle is the <b>welfare loss</b>. This is resource misallocation.", s: { m: 1, e: 1, o: 1, w: 1 } },
  { cap: "<b>A carbon tax of $20 per unit.</b> The tax raises producers' cost to MPC + tax, which lies on the MSC curve. Output falls to the efficient 47 units and the price consumers pay rises to about $53. The externality is internalised.", s: { m: 0.4, e: 1, o: 1, t: 1, w: 0.3 } },
] });

/* ---------- Lab 1: fish stock ---------- */
function labFish() {
  if (!$("#fh") || !$("#fr")) return;
  const h = +$("#fh").value, r = +$("#fr").value / 100, A = simStock(h, r), msy = r * 100 / 4;
  $("#r1").textContent = Lib.fmtN(msy, 1) + " a year"; $("#r2").textContent = Lib.fmtN(A[40], 0); const ok = A[40] > 20; $("#r3").textContent = A[40] <= 0.5 ? "Collapse" : ok ? "Sustainable" : "At risk";
  const gone = A.findIndex((v) => v <= 0.5);
  $("#rv").textContent = h > msy ? (gone > 0 ? `Catching ${h} a year is above the maximum sustainable yield of ${Lib.fmtN(msy, 1)}. The stock is wiped out after about ${gone} years.` : `Catching ${h} a year is above the maximum sustainable yield of ${Lib.fmtN(msy, 1)}, but the stock has not yet collapsed. It is at risk.`) : `Catching ${h} a year is at or below the maximum sustainable yield of ${Lib.fmtN(msy, 1)}. The stock settles at ${Lib.fmtN(A[40], 0)} and the harvest can continue.`;
  const X = (t) => 40 + t * 8.6, Y = (v) => 260 - v * 2.2;
  let o = SV.line(40, 260, 400, 260) + SV.line(40, 260, 40, 30) + SV.text(400, 282, "Years", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "Stock", "sm") + SV.line(40, Y(100), 400, Y(100), "gr");
  o += SV.path(Lib.ptsPath(A.map((v, i) => [X(i), Y(v)])), ok ? "c3" : "c2") + tag(396, Y(A[40]) - 8, "stock " + Lib.fmtN(A[40], 0), ok ? "t3" : "t2", 1, "end");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "fh", label: "Fish caught each year ", min: 0, max: 30, step: 1, value: 8, fmt: (v) => v, onInput: labFish });
Lib.slider($("#g2"), { id: "fr", label: "Regrowth rate (% a year) ", min: 20, max: 60, step: 5, value: 40, fmt: (v) => v, onInput: labFish });
labFish();

/* ---------- Lab 2: carbon tax ---------- */
function labTax() {
  if (!$("#ct")) return;
  const t = +$("#ct").value, Q = (90 - t) / 1.5, P = 100 - Q, nsb = (q) => 70 * q - 0.75 * q * q, loss = nsb(46.667) - nsb(Q);
  $("#t1").textContent = Lib.fmtN(Q, 1); $("#t2").textContent = Lib.fmtN(Q / 60 * 100, 0); $("#t3").textContent = "$" + Lib.fmtN(Math.max(loss, 0), 0);
  $("#tv").textContent = t === 20 ? `A $20 tax equals the external cost. Output falls to the efficient ${Lib.fmtN(Q, 1)} units, emissions fall to ${Lib.fmtN(Q / 60 * 100, 0)}% of the market level and the welfare loss is removed. Tax revenue is $${Lib.fmtN(t * Q, 0)}.` : t < 20 ? `The tax of $${t} is below the $20 external cost, so output is still too high and a welfare loss of about $${Lib.fmtN(loss, 0)} remains. Revenue $${Lib.fmtN(t * Q, 0)}.` : `The tax of $${t} is above the $20 external cost, so output is cut too far and a different welfare loss of about $${Lib.fmtN(loss, 0)} appears. Revenue $${Lib.fmtN(t * Q, 0)}.`;
  const X = (q) => 40 + q * 3.3, Y = (p) => 270 - p * 2.3;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 290, "Output", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "$", "sm");
  o += SV.line(X(0), Y(100), X(100), Y(0), "c1") + tag(X(100) - 2, Y(0) - 8, "D", "t1", 1, "end") + SV.line(X(0), Y(10), X(100), Y(60), "c2", op(0.5)) + SV.line(X(0), Y(30), X(100), Y(80), "c3 dash") + tag(X(100) - 2, Y(80) - 8, "MSC", "t3", 1, "end");
  o += SV.line(X(0), Y(10 + t), X(100), Y(60 + t), "c4") + tag(X(100) - 2, Y(60 + t) + 16, "MPC + tax", "t4", 1, "end") + SV.circle(X(Q), Y(P), 6, "dot4") + SV.line(X(Q), Y(P), X(Q), 270, "gr");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "ct", label: "Tax per unit ($) ", min: 0, max: 40, step: 2, value: 0, fmt: (v) => v, onInput: labTax });
labTax();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is the activity consistent with sustainable growth?", buckets: [{"label": "Likely sustainable"}, {"label": "Likely unsustainable"}], items: [{"text": "Catching fish at or below the regrowth rate", "b": 0}, {"text": "Clear-cutting a rainforest for short-term timber", "b": 1}, {"text": "Replanting a tree for every tree cut", "b": 0}, {"text": "Burning more coal for cheap electricity with no carbon cost", "b": 1}, {"text": "Investing carbon-tax revenue in solar and wind power", "b": 0}, {"text": "Pumping groundwater faster than rain refills it", "b": 1}, {"text": "Recycling metals and reusing components", "b": 0}, {"text": "Exporting a non-renewable mineral and spending all the revenue on consumption", "b": 1}], done: "Sustainable growth keeps future productive potential intact." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Sustainable growth", "Growth that does not reduce future generations' ability to meet their needs"], ["Intergenerational equity", "Fairness between present and future generations"], ["Negative externality", "A cost of production or consumption borne by a third party"], ["Tradable permit", "A right to emit a set amount of pollution that can be bought and sold"], ["Carbon tax", "A tax per tonne of emissions to raise private cost to social cost"], ["MEW", "A measure of welfare that adjusts GDP for environmental costs and unpaid work"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of a carbon tax in order.", items: ["The government taxes each tonne of carbon emitted", "Producers' marginal cost rises", "Output and prices adjust: price rises and quantity falls", "Emissions fall and the external cost is reduced", "The government uses the revenue, for example to fund renewables"], done: "The tax internalises the external cost and moves output towards the social optimum." });
Lib.calc($("#c1"), { qs: [
  {"q": "A country's GDP is $2,000bn. Environmental damage is estimated at $150bn and depletion of natural capital at $100bn. Calculate a green GDP measure (in $bn) by subtracting both.", "a": 1750, "unit": "$bn", "tol": 0.5, "hint": "2000 − 150 − 100.", "sol": "2000 − 150 − 100 = <b>$1,750bn</b>."},
  {"q": "A carbon tax cuts output of a polluting good from 60 units to 47 units. Calculate the percentage fall in output (to one decimal place).", "a": 21.7, "unit": "%", "tol": 0.1, "hint": "Change ÷ original × 100.", "sol": "13 ÷ 60 × 100 = <b>21.7%</b>."},
  {"q": "The government taxes 50 million tonnes of carbon at $30 a tonne. Calculate the tax revenue (in $m).", "a": 1500, "unit": "$m", "tol": 0.5, "hint": "Tonnes × tax per tonne.", "sol": "50 × 30 = <b>$1,500m</b>."},
  {"q": "A fish stock regrows by 40% of its size when it is small, and the maximum sustainable yield is rK ÷ 4. If K = 200 and r = 0.4, what is the maximum sustainable yield per year?", "a": 20, "tol": 0.01, "hint": "r × K ÷ 4.", "sol": "0.4 × 200 ÷ 4 = <b>20</b> per year."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which would be an example of unsustainable growth?", opts: ["Replanting forests at the rate they are cut", "Using solar power to replace coal", "Catching fish faster than they can breed", "Recycling aluminium"], a: 2, why: "Overharvesting reduces the stock that future generations can use." },
  { q: "Why do markets tend to overproduce goods with negative externalities?", opts: ["Consumers value the goods too little", "Producers do not pay the external costs", "The government fixes the price", "Supply is perfectly inelastic"], a: 1, why: "The market price reflects private costs only, so output is above the social optimum." },
  { q: "A carbon tax equal to the marginal external cost will:", opts: ["Raise output", "Move output to the socially efficient level", "Remove all pollution", "Reduce the price consumers pay"], a: 1, why: "The tax moves MPC to MSC. Pollution falls but is not eliminated." },
  { q: "Which is an advantage of tradable permits over a carbon tax?", opts: ["The price of carbon is certain", "The total quantity of emissions is certain", "They are free to administer", "They remove the need for monitoring"], a: 1, why: "The cap fixes the quantity, while the permit price varies." },
  { q: "Which is the main reason international agreements on climate change are hard to enforce?", opts: ["Countries cannot measure emissions", "Each country gains from others' efforts even if it does not act (free riding)", "Carbon taxes are illegal", "Emissions have no effect on other countries"], a: 1, why: "Because everyone benefits from a stable climate, each country has an incentive to free-ride." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Sustainable growth", "Growth that does not reduce future productive potential."],
  ["Natural capital", "Stocks of natural resources such as forests, fish, soil and a stable climate."],
  ["Sustainable yield", "The harvest a renewable resource can replace each year."],
  ["Negative externality", "A cost to third parties that the market price ignores."],
  ["Carbon tax", "Tax on emissions to raise private cost to social cost."],
  ["Tradable permits", "Capped emission rights that firms can buy and sell."],
  ["Free rider", "Gains from others' action without contributing."],
  ["MEW", "Measure of Economic Welfare: GDP adjusted for environmental costs and unpaid work."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is meant by sustainable economic growth? (May/June 2022 · 32 · Q18, reworded)", opts: ["Raising productive potential as fast as possible", "Raising productive potential using only low-cost resources", "Raising productive potential without reducing the potential of future generations", "Raising future potential as fast as possible"], a: 2, why: "Sustainable growth does not reduce future productive potential." },
  { q: "Which influence is least likely to promote sustainable growth in a developing economy? (Feb/March 2021 · 32 · Q18, reworded)", opts: ["High saving rates", "Involvement in free trade", "Protected property rights", "Rapid population growth"], a: 3, why: "Rapid population growth can use up resources and dilute capital per head, so it is least supportive. High saving, trade and property rights support investment." },
  { q: "Which cause of growth is most likely to make growth sustainable? (Oct/Nov 2023 · 31 · Q20, reworded)", opts: ["Deregulation of industry that uses minerals and fossil fuels", "More spending on environmental education, paid for by taxes on harmful goods", "Higher trade barriers to protect jobs", "Fewer planning rules to allow building in areas of natural beauty"], a: 1, why: "Education and taxes on harmful goods change behaviour and fund conservation. The other options increase resource use or damage." },
  { q: "A government wants sustainable growth in the fishing industry. Which policy is most likely to achieve it? (May/June 2023 · 31 · Q18, reworded)", opts: ["Give bigger boats and nets to fishers", "Pay bonuses for larger catches", "Set up a co-operative so fishers get a higher price", "Subsidise fish farms so fishers can switch from sea fishing"], a: 3, why: "Fish farms reduce pressure on wild stocks. The other options encourage more catching." },
  { q: "Which policy to counter climate change is regulatory rather than market-based? (Oct/Nov 2023 · 31 · Q19, reworded)", opts: ["Carbon taxes", "Tradable pollution permits", "Government subsidies", "Industrial emission standards"], a: 3, why: "Emission standards set limits by law. Taxes, permits and subsidies work through prices." },
  { q: "Which government measure is most likely to encourage faster and more sustainable growth? (Oct/Nov 2022 · 33 · Q18, reworded)", opts: ["Subsidies to firms using recycled materials", "Grants to explore and exploit new oil deposits", "More spending on environmental education in schools", "Tougher laws on air and water emissions"], a: 0, why: "Recycling raises output while conserving resources. Oil exploration uses up finite resources." },
  { q: "What is additionally included when calculating the Measure of Economic Welfare (MEW) compared with GDP per head? (May/June 2021 · 31 · Q20, reworded)", opts: ["The cost of paid work", "The cost of producing armaments", "An estimate of environmental damage", "The impact of the shadow economy"], a: 2, why: "MEW adjusts for environmental costs and the value of unpaid work and leisure." },
  { q: "Rapid growth is claimed to harm the environment. Which outcome would not harm it? (Feb/March 2022 · 32 · Q24, reworded)", opts: ["More workers commuting by vehicle", "Higher incomes that reduce family size and fertility", "Moving workers from agriculture to manufacturing", "Using new technology to reach previously inaccessible natural resources"], a: 1, why: "Falling fertility reduces population pressure on resources. The other options raise pollution or resource use." },
] });
