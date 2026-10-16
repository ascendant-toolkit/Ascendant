/* ---------- shared chart helpers ---------- */
/* Steppers: L (thousand workers) 0-200 on x, wage ($ per hour) 0-28 on y */
const SX = (L) => 80 + L * 3.1, SY = (w) => 330 - w * 10.5;
function sAxes(extra) {
  return SV.line(80, 330, 710, 330) + SV.line(80, 330, 80, 30) + SV.text(710, 368, "Quantity of labour (thousand workers)", "sm", { "text-anchor": "end" }) + SV.text(86, 34, "Wage ($ per hour)", "sm") + (extra || "");
}
function sLine(a, b, L0, L1, cls, o) { return SV.line(SX(L0), SY(a + b * L0), SX(L1), SY(a + b * L1), cls, o); }
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });


/* ---------- 40.2: supply of labour and wage differentials ---------- */
const HALO = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
const hrs = (w) => 10 + 2 * w - 0.05 * w * w;                 // hours per week at hourly wage w (illustrative)
const HX = (w) => 70 + w * 16, HY = (h) => 300 - h * 7;
function supAxes() { return SV.line(70, 300, 720, 300) + SV.line(70, 300, 70, 20) + SV.text(720, 330, "Hourly wage ($)", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Hours supplied per week", "sm"); }
function curvePts(a, b) { const p = []; for (let w = a; w <= b + 0.01; w += 1) p.push([HX(w), HY(hrs(w))]); return p; }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 350" role="img" aria-label="Backward bending supply curve of labour: hours supplied rise with the wage then fall">${supAxes()}
  ${SV.path(Lib.ptsPath(curvePts(0, 20)), "c3", { "stroke-width": 4 })}${SV.path(Lib.ptsPath(curvePts(20, 40)), "c2", { "stroke-width": 4 })}
  ${SV.circle(HX(20), HY(hrs(20)), 6, "dot1")}${SV.line(HX(20), HY(hrs(20)), HX(20), 300, "gr")}
  ${SV.text(HX(8), HY(hrs(8)) - 22, "substitution effect dominates", "lbl bd t3", { "text-anchor": "middle", style: HALO })}${SV.text(HX(33), HY(hrs(33)) - 26, "income effect dominates", "lbl bd t2", { "text-anchor": "middle", style: HALO })}
  ${SV.text(HX(20), 320, "20", "lbl bd", { "text-anchor": "middle" })}</svg>`;

/* Watch 1: backward bending */
function supDraw(s) {
  let o = supAxes();
  if (s.c1 > 0) o += SV.path(Lib.ptsPath(curvePts(0, 20 * s.c1)), "c3", { "stroke-width": 4 });
  if (s.c2 > 0) o += SV.path(Lib.ptsPath(curvePts(20, 20 + 20 * s.c2)), "c2", { "stroke-width": 4 });
  if (s.r1 > 0) o += SV.text(HX(9), HY(hrs(9)) - 22, "substitution effect > income effect", "lbl bd t3", { "text-anchor": "middle", style: HALO, ...op(s.r1) });
  if (s.r2 > 0) o += SV.text(HX(32), HY(hrs(32)) - 26, "income effect > substitution effect", "lbl bd t2", { "text-anchor": "middle", style: HALO, ...op(s.r2) }) + SV.circle(HX(20), HY(hrs(20)), 6, "dot1", op(s.r2)) + SV.text(HX(20) + 8, HY(hrs(20)) - 12, "turning point", "sm bd", { style: HALO, ...op(s.r2) });
  if (s.o > 0) o += SV.line(HX(2), HY(4), HX(38), HY(24), "c4", { "stroke-dasharray": "6 5", ...op(s.o) }) + SV.text(HX(24), HY(16.2) + 24, "supply to an occupation", "lbl bd t4", { "text-anchor": "start", style: HALO, ...op(s.o) });
  return o;
}
Lib.stepper($("#stE"), { w: 760, h: 350, label: "An individual's backward-bending supply of labour and the supply to an occupation", base: { c1: 0, c2: 0, r1: 0, r2: 0, o: 0 }, draw: supDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>Low wages.</b> A higher wage makes leisure more expensive, so the worker gives up leisure for work. The <b>substitution effect</b> dominates and hours supplied <b>rise</b> with the wage.", s: { c1: 1, r1: 1 } },
  { cap: "<b>High wages.</b> The worker is now earning enough to afford more time off. The <b>income effect</b> outweighs the substitution effect and hours supplied <b>fall</b> as the wage rises: the curve <b>bends backwards</b>.", s: { c1: 1, c2: 1, r1: 0.5, r2: 1 } },
  { cap: "<b>But an occupation is different.</b> A higher wage in one occupation attracts workers from <b>other jobs</b>, so the supply curve for the occupation (dashed) keeps sloping <b>upwards</b>. Backward bending applies to one person's hours.", s: { c1: 1, c2: 1, r1: 0.4, r2: 0.5, o: 1 } },
] });

/* Watch 2: surgeon and cleaner */
const FY = (w) => 300 - w * 2.5;
function panel(x0, Lmax, title, dA, dB, sA, sB, eqL, eqW, s, key) {
  const X = (l) => x0 + (l / Lmax) * 280; let o = SV.line(x0, 300, x0 + 290, 300) + SV.line(x0, 300, x0, 40) + SV.text(x0 + 140, 336, "Workers (thousand)", "sm", { "text-anchor": "middle" }) + SV.text(x0 + 4, 34, "Wage ($/hr)", "sm") + SV.text(x0 + 140, 20, title, "lbl bd", { "text-anchor": "middle" });
  const v = s[key + "d"], su = s[key + "s"], e = s[key + "e"];
  if (v > 0) o += SV.line(X(0), FY(dA), X(Math.min(Lmax, dA / -dB)), FY(Math.max(0, dA + dB * Math.min(Lmax, dA / -dB))), "c1", op(v)) + SV.text(X(Lmax * 0.12), FY(dA + dB * Lmax * 0.12) - 8, "D = MRP", "sm bd t1", { style: HALO, ...op(v) });
  if (su > 0) o += SV.line(X(0), FY(sA), X(Lmax), FY(sA + sB * Lmax), "c2", op(su)) + SV.text(X(Lmax) - 4, FY(Math.min(98, sA + sB * Lmax)) + 14, "S", "sm bd t2", { "text-anchor": "end", style: HALO, ...op(su) });
  if (e > 0) o += SV.line(X(eqL), FY(eqW), X(eqL), 300, "gr", op(e)) + SV.line(x0, FY(eqW), X(eqL), FY(eqW), "gr", op(e)) + SV.circle(X(eqL), FY(eqW), 6, "dot3", op(e)) + SV.text(x0 - 6, FY(eqW) + 4, "$" + eqW, "lbl bd t3", { "text-anchor": "end", ...op(e) }) + SV.text(X(eqL), 316, Lib.fmtN(eqL, 0), "sm bd", { "text-anchor": "middle", ...op(e) });
  return o;
}
function diffDraw(s) {
  let o = panel(60, 300, "Cleaners", 30, -0.1, 2, 0.1, 140, 16, s, "c") + panel(420, 60, "Surgeons", 90, -1.5, 10, 1.5, 26.7, 50, s, "u");
  if (s.cmp > 0) o += SV.text(380, 356, "Surgeon wage $50 vs cleaner wage $16: explained by MRP and by scarcity of supply", "lbl bd t3", { "text-anchor": "middle", ...op(s.cmp) });
  return o;
}
Lib.stepper($("#stF"), { w: 760, h: 370, label: "Demand and supply in the labour markets for cleaners and surgeons", base: { cd: 0, cs: 0, ce: 0, ud: 0, us: 0, ue: 0, cmp: 0 }, draw: diffDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Cleaners.</b> The work needs little training, so many people could do it: supply is <b>elastic</b>. The MRP of a cleaner is modest. Demand and supply meet at a wage of <b>$16</b> and 140 thousand workers.", s: { cd: 1, cs: 1, ce: 1 } },
  { cap: "<b>Surgeons: demand.</b> A surgeon's skill adds a great deal of value for hospitals and patients, so the MRP is <b>high</b> and the demand curve is far to the right and high up.", s: { cd: 1, cs: 1, ce: 1, ud: 1 } },
  { cap: "<b>Surgeons: supply.</b> Training takes many years and is costly, and few people are able to do it. Supply is <b>small and inelastic</b>: to attract more surgeons the wage has to rise a lot.", s: { cd: 1, cs: 1, ce: 1, ud: 1, us: 1 } },
  { cap: "<b>The result.</b> High demand meeting scarce supply gives a wage of <b>$50</b> with only 27 thousand surgeons. The wage differential comes from <b>both</b> sides of the market: high MRP and restricted supply.", s: { cd: 1, cs: 1, ce: 1, ud: 1, us: 1, ue: 1, cmp: 1 } },
] });

/* ---------- Lab 1: hours ---------- */
function lab1() {
  if (!$("#sw")) return;
  const w = +$("#sw").value, h = hrs(w);
  $("#r1").textContent = Lib.fmtN(h, 1); $("#r2").textContent = "$" + Lib.fmtN(w * h, 0); $("#r3").textContent = w < 19 ? "substitution" : w > 21 ? "income" : "equal";
  $("#rv").textContent = w < 19 ? `At $${w} an hour the worker supplies ${Lib.fmtN(h, 1)} hours. A higher wage would raise hours because leisure is becoming more expensive: the substitution effect is stronger.`
    : w > 21 ? `At $${w} an hour the worker supplies ${Lib.fmtN(h, 1)} hours. Pay per hour is so high that the worker prefers to buy more leisure: the income effect is stronger and hours fall as the wage rises.`
    : "At about $20 an hour the two effects balance and hours are at their maximum (30 hours).";
  const o = supAxes() + SV.path(Lib.ptsPath(curvePts(0, 40)), "c1", { "stroke-width": 3 }) + SV.line(HX(w), HY(h), HX(w), 300, "gr") + SV.line(70, HY(h), HX(w), HY(h), "gr") + SV.circle(HX(w), HY(h), 7, w <= 20 ? "dot3" : "dot2");
  $("#labA").innerHTML = o.replace(/viewBox/g, "viewBox");
}
Lib.slider($("#g1"), { id: "sw", label: "Hourly wage ($): ", min: 2, max: 40, step: 1, value: 10, fmt: (v) => v, onInput: lab1 });

/* ---------- Lab 2: wage determination ---------- */
function lab2() {
  if (!$("#da") || !$("#sb")) return;
  const a = +$("#da").value, b = +$("#sb").value, L = Math.max(0, (a - b) / 0.2), W = (a + b) / 2;
  $("#s1").textContent = "$" + Lib.fmtN(W, 1); $("#s2").textContent = Lib.fmtN(L, 0) + "k"; $("#s3").textContent = "$" + Lib.fmtN(W - b, 1);
  $("#sv").textContent = a <= b ? "Demand is below the lowest pay anyone will accept: no one is employed." : `Demand meets supply at $${Lib.fmtN(W, 1)} an hour and ${Lib.fmtN(L, 0)} thousand workers. A rise in demand (a) raises both the wage and employment; making supply harder (b up, for example longer training) raises the wage but cuts employment.`;
  const X = (v) => 40 + v * 1.7, Y = (v) => 240 - v * 6.4;
  let o = SV.line(40, 240, 400, 240) + SV.line(40, 240, 40, 20) + SV.text(396, 262, "Workers (thousand)", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Wage ($/hr)", "sm");
  o += SV.line(X(0), Y(a), X(Math.min(200, a / 0.1)), Y(Math.max(0, a - 0.1 * Math.min(200, a / 0.1))), "c1") + SV.line(X(0), Y(b), X(200), Y(b + 20), "c2") + SV.text(X(10), Y(a) - 6, "D = MRP", "lbl bd t1", { style: HALO }) + SV.text(X(200) - 4, Y(b + 20) - 6, "S", "lbl bd t2", { "text-anchor": "end" });
  if (L > 0) o += SV.line(X(L), Y(W), X(L), 240, "gr") + SV.line(40, Y(W), X(L), Y(W), "gr") + SV.circle(X(L), Y(W), 6, "dot3");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "da", label: "Demand for labour (MRP intercept $): ", min: 14, max: 30, step: 1, value: 20, fmt: (v) => v, onInput: lab2 });
Lib.slider($("#g3"), { id: "sb", label: "Supply: lowest pay the first worker accepts ($): ", min: 2, max: 16, step: 1, value: 4, fmt: (v) => v, onInput: lab2 });

/* ---------- Lab 3: compensating differences ---------- */
function lab3() {
  if (!$("#jw") || !$("#jp")) return;
  const wb = +$("#jw").value, pt = +$("#jp").value, nb = wb - 1.5 * pt, need = 12 + 1.5 * pt;
  $("#t1").textContent = "$12.0"; $("#t2").textContent = "$" + Lib.fmtN(nb, 1); $("#t3").textContent = "$" + Lib.fmtN(need, 1);
  $("#tv").textContent = Math.abs(nb - 12) < 0.05 ? "The net advantages are equal, so workers are indifferent between the jobs. The extra wage exactly compensates for the unpleasantness."
    : nb < 12 ? `Job B has a lower net advantage ($${Lib.fmtN(nb, 1)} against $12). Workers prefer A, so B has trouble hiring: its supply of labour shifts left and its wage has to rise towards $${Lib.fmtN(need, 1)}.`
    : `Job B has a higher net advantage than A. Workers move from A to B, so B's supply rises and its wage tends to fall towards $${Lib.fmtN(need, 1)}, and A's wage rises.`;
  const H = (v) => 150 * (v / 24), bw = 80;
  let o = SV.line(30, 190, 400, 190) + SV.text(32, 22, "$ per hour", "sm");
  [[40, 12, "f1", "Net advantage A"], [150, Math.max(0, nb), nb >= 12 ? "f3" : "f2", "Net advantage B"], [260, need, "f4", "Wage B needs"]].forEach(([x, v, c, l]) => { o += SV.rect(x, 190 - H(v), bw, H(v), c) + SV.text(x + bw / 2, 190 - H(v) - 6, "$" + Lib.fmtN(v, 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 208, l, "sm", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o;
}
Lib.slider($("#g4"), { id: "jw", label: "Wage in job B ($ per hour): ", min: 6, max: 24, step: 0.5, value: 12, fmt: (v) => v, onInput: lab3 });
Lib.slider($("#g5"), { id: "jp", label: "Unpleasantness of job B (points): ", min: 0, max: 6, step: 1, value: 3, fmt: (v) => v, onInput: lab3 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Drag each event into the right bucket for the supply of labour to an occupation.",
  buckets: [{ label: "Shifts supply right" }, { label: "Shifts supply left" }, { label: "Movement along the curve" }],
  items: [
    { text: "Net migration into the economy rises", b: 0 }, { text: "Training becomes cheaper and shorter", b: 0 }, { text: "More women enter the labour force", b: 0 },
    { text: "Wages in a rival occupation rise sharply", b: 1 }, { text: "The training period is lengthened by law", b: 1 }, { text: "Unemployment benefits become more generous", b: 1 },
    { text: "The wage in this job rises and more people apply", b: 2 }, { text: "The wage in this job falls and some leave", b: 2 },
  ], done: "Wage changes in this job are movements along; everything else shifts the curve.",
});
Lib.classify($("#cl2"), {
  prompt: "What best explains each wage difference?",
  buckets: [{ label: "Scarce skills or high MRP" }, { label: "Compensating difference" }, { label: "Market imperfection" }],
  items: [
    { text: "A top surgeon earns far more than a cleaner", b: 0 }, { text: "A star footballer's pay is huge", b: 0 }, { text: "A chief executive's decisions affect all the company's revenue", b: 0 },
    { text: "Oil platform workers receive risk pay", b: 1 }, { text: "Night nurses are paid a shift premium", b: 1 }, { text: "A job far from the family home pays extra", b: 1 },
    { text: "Women are paid less for the same work", b: 2 }, { text: "Workers do not know about better-paid jobs elsewhere", b: 2 }, { text: "Workers cannot move because of housing costs", b: 2 }, { text: "A union keeps wages above the market level", b: 2 },
  ], done: "Differences from demand and supply conditions are market outcomes; imperfections explain why wages differ from the model.",
});
Lib.order($("#o1"), { prompt: "Put the explanation of why a surgeon earns more than a cleaner in order.", items: [
  "A surgeon's skills add a very large amount to revenue, so MRP and demand for surgeons are high",
  "Training is long and costly, so few people qualify",
  "The supply of surgeons is small and inelastic",
  "High demand meets scarce supply at a high wage",
  "Cleaners have low MRP and a large, elastic supply, so the wage is low",
  "Evaluate: discrimination, immobility and institutions may also affect wages",
], done: "A reliable structure for a wage differential answer." });
Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Substitution effect (labour)", "A higher wage makes leisure dearer, so workers supply more hours"],
  ["Income effect (labour)", "A higher wage lets workers afford more leisure, so they may supply fewer hours"],
  ["Backward-bending supply", "Hours supplied fall as the wage rises beyond a point"],
  ["Net advantage", "Pay plus non-pay benefits minus non-pay costs of a job"],
  ["Compensating difference", "Extra pay for a job that is unpleasant or risky"],
  ["Occupational immobility", "Difficulty moving between jobs because of a lack of skills"],
  ["Geographical immobility", "Difficulty moving to where the jobs are"],
  ["Wage differential", "A difference in pay between workers or jobs"],
], done: "Eight terms for this part." });
Lib.calc($("#c1"), { qs: [
  { q: "Demand for labour: W = 40 − 0.1L. Supply: W = 10 + 0.2L (L in thousands). What is the equilibrium employment (thousand)?", a: 100, hint: "Set demand equal to supply.", sol: "40 − 0.1L = 10 + 0.2L → 30 = 0.3L → L = <b>100</b>." },
  { q: "In the same market, what is the equilibrium wage ($)?", a: 30, sol: "W = 40 − 0.1 × 100 = <b>$30</b>." },
  { q: "Training becomes longer and supply shifts to W = 16 + 0.2L. What is the new equilibrium wage ($)?", a: 32, hint: "40 − 0.1L = 16 + 0.2L gives L = 80.", sol: "L = 80, W = 40 − 8 = <b>$32</b>. The wage rises and employment falls." },
  { q: "Job A pays $15 and is pleasant. Job B pays $19 and has 2 points of unpleasantness, each worth $2 an hour. What is the net advantage of B ($)?", a: 15, sol: "19 − 2 × 2 = <b>$15</b>, equal to A: the pay compensates for the unpleasantness." },
  { q: "A 10% rise in the wage raises the quantity of labour supplied to an occupation by 4%. Calculate the wage elasticity of supply.", a: 0.4, tol: 0.01, sol: "4% ÷ 10% = <b>0.4</b>: inelastic." },
  { q: "A surgeon earns $50 an hour and a cleaner $16. By what percentage does the surgeon's wage exceed the cleaner's (%)?", a: 212.5, tol: 0.2, sol: "(50 − 16) ÷ 16 × 100 = <b>212.5%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "At low wages the substitution effect of a wage rise is likely to:", opts: ["reduce hours supplied", "raise hours supplied", "have no effect", "reduce the demand for labour"], a: 1, why: "Leisure becomes more expensive, so workers give up leisure for work." },
  { q: "A backward-bending supply curve of labour is explained by:", opts: ["a rising MRP", "the income effect outweighing the substitution effect at high wages", "falling unemployment", "trade unions"], a: 1, why: "At high wages workers choose more leisure." },
  { q: "The supply of labour to an occupation is likely to be more inelastic when:", opts: ["Training is short", "Workers move easily between jobs", "Skills take years to acquire", "There is high unemployment"], a: 2, why: "Long training restricts the number who can quickly enter the occupation." },
  { q: "Which would shift the supply of labour in an occupation to the left?", opts: ["Higher wages in a rival occupation", "A fall in the cost of training", "Higher net migration", "A rise in the wage in this job"], a: 0, why: "Workers move to the better-paid rival. A rise in this wage is a movement along the curve." },
  { q: "A dangerous job pays more than a similar safe job. This is best explained by:", opts: ["discrimination", "a compensating difference", "monopsony", "a minimum wage"], a: 1, why: "The extra pay compensates workers for the risk so that the net advantage is similar." },
  { q: "Which is a market imperfection that could explain a wage difference?", opts: ["Perfect mobility of labour", "Perfect information about jobs", "Discrimination", "Identical workers"], a: 2, why: "Discrimination keeps some groups' pay different from the competitive outcome." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Substitution effect (labour supply)", "A higher wage makes leisure more expensive, so workers may supply more hours."],
  ["Income effect (labour supply)", "A higher wage lets workers buy more leisure, so they may supply fewer hours."],
  ["Backward-bending supply curve", "Hours supplied fall at high wages because the income effect outweighs the substitution effect."],
  ["Occupational supply", "Upward sloping, because a higher wage attracts workers from other jobs."],
  ["Elasticity of supply of labour", "Responsiveness of labour supplied to a change in the wage. Lower with long training."],
  ["Net advantage", "Wage plus non-wage benefits minus non-wage costs of a job."],
  ["Compensating differences", "Extra pay for unpleasant, risky or unsocial jobs."],
  ["Wage differential", "A difference in pay between jobs or between workers."],
  ["Occupational immobility", "Workers lack the skills to move between jobs."],
  ["Geographical immobility", "Workers cannot easily move to where the jobs are."],
  ["Discrimination", "Paying or hiring groups differently for reasons not related to productivity."],
  ["Wage taker", "A firm that has to pay the market wage."],
] });

/* ---------- Past paper MCQ (text) ---------- */
Lib.quiz($("#qz2"), { qs: [
  { q: "[Oct/Nov 2020 · 32 · Q17] A backward-sloping supply curve of labour is one where, beyond a certain point, the supply of labour:", opts: ["decreases as the demand for labour rises.", "increases as the demand for labour rises.", "decreases as wages rise.", "increases as wages rise."], a: 2, why: "At high wages the income effect dominates and hours fall as the wage rises." },
  { q: "[Oct/Nov 2023 · 32 · Q11] A backward-sloping supply curve of labour is one where, beyond a certain point, the supply of labour:", opts: ["decreases as the demand for labour rises.", "increases as the demand for labour rises.", "decreases as wages rise.", "increases as wages rise."], a: 2, why: "The same definition: supply decreases as wages rise." },
  { q: "[May/June 2025 · 32 · Q13] What is not a factor affecting the supply of labour?", opts: ["emigration rates", "labour participation rate", "labour productivity", "unemployment benefits"], a: 2, why: "Labour productivity affects the demand for labour (MRP). The others change the number or willingness of people to work." },
  { q: "[May/June 2024 · 32 · Q13] Most workers in a country are paid a fixed wage rate per hour in the manufacturing sector. What will lead to an increase in the net advantage of workers currently employed in the manufacturing sector?", opts: ["a reduction in working hours available", "a shift in the country's economy to the service sector", "a subsidised lunch is made available", "an increase in the number of jobs available"], a: 2, why: "A subsidised lunch is a non-wage benefit, which raises the net advantage of the job. The others do not add to the job's advantages." },
] });
