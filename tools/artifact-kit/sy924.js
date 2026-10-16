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

/* ---------- AD and AS model shared by the diagrams ---------- */
const AX = (q) => 70 + q * 6.6, AY = (p) => 320 - p * 3.0;
function adas(o, a, sh, lr, col = "") {
  const sras = (q) => 15 + 0.7 * (q - sh), Q = (a - 15 + 0.7 * sh) / 1.6, P = sras(Q);
  let s = axes(70, 320, 740, 30, "Real GDP", "Price level");
  s += SV.line(AX(lr), 320, AX(lr), 40, "c3") + tag(AX(lr) + 6, 52, "LRAS", "t3");
  s += SV.line(AX(0), AY(sras(0)), AX(100), AY(sras(100)), "c2") + tag(AX(100) - 4, AY(sras(100)) - 8, "SRAS", "t2", 1, "end");
  s += SV.line(AX(0), AY(a), AX(100), AY(a - 90), "c1") + tag(AX(100) - 4, AY(a - 90) + 18, "AD", "t1", 1, "end");
  s += SV.line(AX(Q), AY(P), AX(Q), 320, "gr") + SV.line(70, AY(P), AX(Q), AY(P), "gr") + SV.circle(AX(Q), AY(P), 7, "dot4");
  return { s, Q, P };
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 360" role="img" aria-label="AD shifting right: with spare capacity output rises a lot, near the LRAS mostly prices rise">${(() => { const A = adas(0, 100, 0, 60), B = adas(0, 111, 0, 60), C = adas(0, 135, 0, 60); return A.s + SV.line(AX(0), AY(111), AX(100), AY(21), "c1 dash") + SV.line(AX(0), AY(135), AX(100), AY(45), "c1 dash") + tag(AX(B.Q) + 10, AY(B.P) - 12, "Output up, prices barely move", "t3") + tag(AX(C.Q) + 10, AY(C.P) - 14, "At capacity: mostly prices rise", "t2"); })()}</svg>`;

/* ---------- Watch 1: demand boost ---------- */
function demDraw(s) {
  const r = adas(0, s.a, 0, 60); let o = r.s;
  if (s.v > 0) o += tag(AX(r.Q) + 12, AY(r.P) + 28, "Q = " + Lib.fmtN(r.Q, 0) + ", P = " + Lib.fmtN(r.P, 0), "t4", s.v);
  if (s.g > 0 && r.Q < 59) o += SV.line(AX(r.Q), 296, AX(60), 296, "c2", { "stroke-width": 5, ...op(s.g) }) + tag(AX((r.Q + 60) / 2), 288, "spare capacity", "t2", s.g, "middle");
  return o;
}
Lib.stepper($("#stD"), { w: 760, h: 360, label: "AD shifting right first with spare capacity then at full capacity", base: { a: 100, v: 1, g: 1 }, draw: demDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Starting point.</b> There is a negative output gap: equilibrium output is below the vertical LRAS. Q is about 53 and P about 52.", s: {} },
  { cap: "<b>Expansionary policy.</b> Lower interest rates or a rise in government spending shift <b>AD to the right</b>. Output rises towards potential and the price level rises only a little, because spare capacity can absorb the extra demand.", s: { a: 111 } },
  { cap: "<b>Capacity reached.</b> The economy is now on the LRAS. The gap is closed and actual growth has used up all the slack.", s: { a: 111, g: 0 } },
  { cap: "<b>More stimulus.</b> AD shifts again. Output cannot rise much above potential, so the extra demand mostly raises the <b>price level</b>. This is why demand-side policy loses effectiveness near full capacity.", s: { a: 135, g: 0 } },
] });

/* ---------- Watch 2: supply-side policy ---------- */
function supDraw(s) {
  const r = adas(0, 111, s.sh, 60 + s.sh); let o = r.s;
  if (s.sh > 0) o += SV.line(AX(60), 320, AX(60), 40, "c3 dash") + tag(AX(60) - 6, 52, "LRAS₁", "t3", 1, "end");
  if (s.v > 0) o += tag(AX(r.Q) + 12, AY(r.P) + 28, "Q = " + Lib.fmtN(r.Q, 0) + ", P = " + Lib.fmtN(r.P, 0), "t4", s.v);
  return o;
}
Lib.stepper($("#stU"), { w: 760, h: 360, label: "Supply side policy shifting LRAS and SRAS to the right, raising output and lowering prices", base: { sh: 0, v: 1 }, draw: supDraw, tween: 1100, dwell: 5600, steps: [
  { cap: "<b>The economy at full capacity.</b> AD crosses SRAS on the LRAS at Q = 60 and P = 57. The only way to grow faster without inflation is to raise capacity.", s: {} },
  { cap: "<b>Supply-side policy.</b> Education, infrastructure, investment incentives and competition raise the quantity, quality or productivity of factors. <b>LRAS and SRAS shift to the right</b>.", s: { sh: 8 } },
  { cap: "<b>The result.</b> Output is higher and the price level lower than before: potential growth with <b>less</b> inflationary pressure. This is why supply-side policy is a long-run answer, though it works slowly and costs money.", s: { sh: 16 } },
] });

/* ---------- Lab 1: policy mix ---------- */
function labMix() {
  if (!$("#ad") || !$("#sp")) return;
  const dA = +$("#ad").value, dS = +$("#sp").value, a0 = 100, a = a0 + dA, lr = 60 + dS, sh = dS, r0 = adas(0, a0, 0, 60), r1 = adas(0, a, sh, lr);
  const gq = (r1.Q - r0.Q) / r0.Q * 100, gp = (r1.P - r0.P) / r0.P * 100, gap = (r1.Q - lr) / lr * 100;
  $("#r1").textContent = (gq >= 0 ? "+" : "") + Lib.fmtN(gq, 1) + "%"; $("#r2").textContent = (gp >= 0 ? "+" : "") + Lib.fmtN(gp, 1) + "%"; $("#r3").textContent = Lib.fmtN(gap, 1) + "%";
  const note = dA === 0 && dS === 0 ? "No policy: the negative gap stays." : dS === 0 ? (gap > 0.5 ? "Demand-side only: output grows but pushes above potential, so prices rise." : "Demand-side only: spare capacity is used up with little inflation.") : dA === 0 ? "Supply-side only: potential rises and prices fall, but the gap widens because demand has not moved." : "Mix: demand uses spare capacity while the supply side raises potential, so growth is faster with less inflation pressure.";
  $("#rv").textContent = note + ` (Output ${Lib.fmtN(r0.Q, 0)} to ${Lib.fmtN(r1.Q, 0)}; price level ${Lib.fmtN(r0.P, 0)} to ${Lib.fmtN(r1.P, 0)}.)`;
  const X = (q) => 40 + q * 3.6, Y = (p) => 260 - p * 2.2;
  let o = SV.line(40, 260, 400, 260) + SV.line(40, 260, 40, 20) + SV.text(400, 282, "Real GDP", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Price level", "sm") + SV.line(X(lr), 260, X(lr), 30, "c3") + tag(X(lr) + 4, 42, "LRAS", "t3");
  o += SV.line(X(0), Y(15 + 0.7 * (0 - sh)), X(100), Y(15 + 0.7 * (100 - sh)), "c2") + SV.line(X(0), Y(a), X(100), Y(a - 90), "c1") + SV.circle(X(r1.Q), Y(r1.P), 6, "dot4");
  o += SV.line(X(0), Y(a0), X(100), Y(a0 - 90), "c1 dash", op(0.45)) + SV.circle(X(r0.Q), Y(r0.P), 5, "dot2", op(0.6)) + tag(X(r0.Q) - 8, Y(r0.P) + 20, "start", "t2", 0.8, "end");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ad", label: "Demand stimulus (AD shift) ", min: 0, max: 40, step: 1, value: 0, fmt: (v) => v, onInput: labMix });
Lib.slider($("#g2"), { id: "sp", label: "Supply-side improvement (LRAS shift) ", min: 0, max: 20, step: 1, value: 0, fmt: (v) => v, onInput: labMix });
labMix();
btnTable("lbBtns", "lbOut", [
  ["Cut interest rates", "Demand-side (monetary)", "Cheaper borrowing raises consumption and investment; a lower exchange rate lifts exports", "6 to 18 months", "Weak if confidence is low or in a liquidity trap; inflation risk"],
  ["Raise government spending", "Demand-side (fiscal)", "Injection into the circular flow, multiplied", "Months to a year", "Deficit and debt, crowding out, imports leak out"],
  ["Build roads, rail and broadband", "Supply-side (interventionist)", "Lower costs and wider markets, higher productivity", "3 to 10 years", "Expensive, project quality varies, planning delays"],
  ["Fund education and training", "Supply-side (interventionist)", "Higher skills, productivity and employment", "10 to 20 years", "Slow, skills may not match demand, high cost"],
  ["Privatise and deregulate", "Supply-side (market-based)", "Competition and profit motive cut costs", "2 to 8 years", "Private monopolies, job losses, inequality"],
  ["Cut income tax", "Supply-side (market-based) and demand", "More incentive to work and invest; also raises disposable income", "1 to 5 years", "Budget deficit, benefits go mostly to high earners, effect on work effort is small"]
], ["Policy", "Type", "How it raises growth", "Time lag", "Main weakness"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is the policy mainly demand-side or supply-side?", buckets: [{"label": "Demand-side (actual growth)"}, {"label": "Supply-side (potential growth)"}], items: [{"text": "Cut the interest rate", "b": 0}, {"text": "Fund apprenticeships and training", "b": 1}, {"text": "Increase government spending on benefits", "b": 0}, {"text": "Privatise a state-owned airline", "b": 1}, {"text": "Quantitative easing", "b": 0}, {"text": "Offer tax breaks for research and development", "b": 1}, {"text": "Devalue the currency", "b": 0}, {"text": "Build a new power grid", "b": 1}], done: "Demand-side moves AD. Supply-side moves LRAS." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Infrastructure", "Basic facilities that businesses need: roads, power, ports, broadband"], ["Deregulation", "Removing rules that restrict competition"], ["Privatisation", "Selling state-owned firms to the private sector"], ["Crowding out", "Government borrowing reduces private sector investment"], ["Time lag", "The delay between a policy change and its full effect"], ["FDI", "Investment by a foreign firm in productive assets in another country"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of better education and training in order.", items: ["The government increases funding for training", "Workers' skills and productivity improve", "Firms can produce more output per worker at lower unit cost", "LRAS shifts right", "Potential output rises and the price level is lower than it would have been"], done: "Supply-side policy works through the quality of factors of production." });
Lib.calc($("#c1"), { qs: [
  {"q": "A government increases spending by $30bn. The marginal propensity to consume is 0.6 and there are no taxes or imports. Calculate the total increase in national income (in $bn).", "a": 75, "unit": "$bn", "tol": 0.01, "hint": "Multiplier = 1 ÷ (1 − MPC).", "sol": "Multiplier = 1 ÷ 0.4 = 2.5. Rise in income = 2.5 × 30 = <b>$75bn</b>."},
  {"q": "Potential GDP is growing at 2.5% a year. Actual GDP is $950bn and potential is $1,000bn. Spending rises so that actual GDP grows by 6% in the next year. Calculate the new output gap as a percentage of potential GDP (ignore growth in potential; one decimal place, minus sign if negative).", "a": 0.7, "tol": 0.1, "hint": "New actual = 950 × 1.06.", "sol": "950 × 1.06 = 1007. Gap = (1007 − 1000) ÷ 1000 × 100 = <b>+0.7%</b>."},
  {"q": "Real GDP is $2,000bn. Over five years it grows at a steady 3% a year. Calculate real GDP after five years (to the nearest $bn).", "a": 2319, "unit": "$bn", "tol": 1, "hint": "2000 × 1.03⁵.", "sol": "1.03⁵ = 1.1593, so GDP = <b>$2,319bn</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which policy is most likely to raise potential output?", opts: ["A cut in the interest rate", "Higher government spending on benefits", "Investment in education and training", "A fall in the exchange rate"], a: 2, why: "Training raises the quality of labour and shifts LRAS to the right. The other policies move AD." },
  { q: "Why may expansionary fiscal policy be ineffective at full capacity?", opts: ["Taxes have no effect on demand", "Extra demand mainly raises prices", "The multiplier becomes negative", "Imports always fall"], a: 1, why: "With no spare capacity extra demand raises the price level rather than output." },
  { q: "Which is a market-based supply-side policy?", opts: ["Building a new railway", "Funding an apprenticeship scheme", "Deregulating an industry to increase competition", "Increasing the budget deficit"], a: 2, why: "Deregulation relies on markets and competition to raise efficiency. The railway and training are interventionist." },
  { q: "A government builds roads and broadband. Which describes the likely effects?", opts: ["Only a short-run rise in AD", "A short-run rise in AD and a long-run rise in potential output", "Only a long-run fall in prices", "No effect on either AD or AS"], a: 1, why: "Construction spending is an injection now and better infrastructure raises productivity later." },
  { q: "What is the main limitation of supply-side policies?", opts: ["They always raise inflation", "They take a long time to have an effect", "They reduce potential output", "They cannot be financed"], a: 1, why: "Education, infrastructure and reform take years to raise output." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Demand-side policy", "Policy that shifts AD (fiscal, monetary, exchange rate) to raise actual growth."],
  ["Supply-side policy", "Policy that raises productive capacity and shifts LRAS right."],
  ["Market-based supply-side", "Deregulation, privatisation, tax cuts, competition policy."],
  ["Interventionist supply-side", "Education, training, infrastructure, R&D subsidies."],
  ["Infrastructure", "Roads, rail, ports, power, broadband and other basic facilities."],
  ["Multiplier", "The rise in income from an injection is a multiple of the injection."],
  ["Time lag", "The delay between a policy and its effect on output."],
  ["Crowding out", "Public borrowing pushes up interest rates and reduces private investment."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What would be the biggest contribution to sustainable economic growth in a developed economy? (Feb/March 2020 · 32 · Q18, reworded)", opts: ["Movement of people from rural to urban areas", "An increase in technical training", "An increase in the size of the population", "Rising consumer credit"], a: 1, why: "Technical training raises productivity over the long run without using up resources." },
  { q: "Which Keynesian policy would most clearly reduce cyclical unemployment? (Feb/March 2020 · 32 · Q23, reworded)", opts: ["Higher government spending on new infrastructure such as roads", "Higher government spending on retraining workers", "A cut in the tax rate on imports", "A cut in the tax rate on goods and services"], a: 0, why: "Cyclical unemployment comes from weak demand, so a direct rise in government spending on projects raises AD and jobs." },
  { q: "What would reduce the effectiveness of a supply-side stimulus to the economy? (May/June 2023 · 31 · Q25, reworded)", opts: ["A limit on the hours people can work in a week", "A rise in public sector spending", "New training schemes", "Relaxed import controls on raw materials"], a: 0, why: "A cap on working hours restricts labour supply and works against the stimulus." },
  { q: "A government raises its deficit to spend on infrastructure and finances it by printing money. How is this likely to affect unemployment, inflation and growth? (Feb/March 2024 · 32 · Q22, reworded)", opts: ["Unemployment less likely, inflation less likely, growth more likely", "Unemployment less likely, inflation more likely, growth less likely", "Unemployment more likely, inflation more likely, growth less likely", "Unemployment more likely, inflation more likely, growth more likely"], a: 1, why: "More spending and money should cut unemployment, but printing money and extra demand raise inflation risk, and high inflation can reduce growth." },
  { q: "What is most likely to encourage foreign direct investment into a developing economy? (Feb/March 2022 · 32 · Q20, reworded)", opts: ["Better health and safety standards", "Higher import quotas", "More spending on infrastructure", "A minimum wage"], a: 2, why: "Better infrastructure cuts firms' costs, which attracts FDI." },
  { q: "Which government measure is most likely to encourage faster and more sustainable growth? (Oct/Nov 2022 · 33 · Q18, reworded)", opts: ["Subsidies to firms that use recycled materials", "Grants to explore new oil deposits", "More spending on environmental education in schools", "Stricter controls on emissions"], a: 0, why: "Subsidies for recycling raise output while saving resources. The oil grants use up finite resources." },
  { q: "Low wages and cheap land will not attract foreign investment into manufacturing in which circumstance? (Oct/Nov 2023 · 33 · Q30, reworded)", opts: ["Genuine central bank independence", "A privatisation programme", "A lack of well-developed infrastructure", "Profits can be sent home freely"], a: 2, why: "Without transport, power and communication the cost advantage of cheap labour is lost." },
] });
