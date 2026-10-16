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

/* ---------- Learn picture: mobility as barriers ---------- */
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A worker in a region of high unemployment facing barriers of housing, transport and family ties before reaching a region with vacancies, and a skills gap between a declining and a growing occupation">${(() => { let o = SV.rect(40, 70, 190, 110, "f2") + tag(135, 100, "Region A", "t2", 1, "middle") + SV.text(135, 128, "unemployment 12%", "lbl", { "text-anchor": "middle" }) + SV.text(135, 150, "few vacancies", "lbl", { "text-anchor": "middle" }); o += SV.rect(530, 70, 190, 110, "f3") + tag(625, 100, "Region B", "t3", 1, "middle") + SV.text(625, 128, "unemployment 3%", "lbl", { "text-anchor": "middle" }) + SV.text(625, 150, "vacancies unfilled", "lbl", { "text-anchor": "middle" }); o += arrow(235, 125, 525, 125, "r", "c1", 1) + tag(380, 112, "geographical mobility", "t1", 1, "middle"); ["housing", "transport", "family", "moving cost"].forEach((l, i) => { const x = 280 + i * 62; o += SV.rect(x, 140, 4, 40, "f4") + SV.text(x + 2, 198, l, "sm", { "text-anchor": "middle" }); }); o += SV.rect(60, 232, 150, 44, "f2") + SV.text(135, 259, "Declining occupation", "lbl bd", { "text-anchor": "middle" }) + SV.rect(550, 232, 150, 44, "f3") + SV.text(625, 259, "Growing occupation", "lbl bd", { "text-anchor": "middle" }) + arrow(215, 254, 545, 254, "r", "c3", 1) + tag(380, 228, "occupational mobility: skills, training, qualifications", "t3", 1, "middle"); return o; })()}</svg>`;

/* ---------- Watch 1: regions ---------- */
function regDraw(s) {
  const m = s.m, ua = 12 - 5 * m, ub = 3 + 1.5 * m, wa = 80 + 10 * m, wb = 120 - 10 * m;
  let o = tag(70, 28, "Unemployment rate (%)", "t1") + tag(420, 28, "Average wage ($ thousand)", "t1");
  const Y = (v, k) => 280 - v * k;
  [[ua, "Region A", 70], [ub, "Region B", 190]].forEach(([v, l, x]) => { o += SV.rect(x, Y(v, 14), 90, 280 - Y(v, 14), l === "Region A" ? "f2" : "f3") + tag(x + 45, Y(v, 14) - 8, Lib.fmtN(v, 1) + "%", l === "Region A" ? "t2" : "t3", 1, "middle") + SV.text(x + 45, 300, l, "sm bd", { "text-anchor": "middle" }); });
  [[wa, "Region A", 420], [wb, "Region B", 540]].forEach(([v, l, x]) => { o += SV.rect(x, Y(v, 2), 90, 280 - Y(v, 2), l === "Region A" ? "f2" : "f3") + tag(x + 45, Y(v, 2) - 8, "$" + Lib.fmtN(v, 0) + "k", l === "Region A" ? "t2" : "t3", 1, "middle") + SV.text(x + 45, 300, l, "sm bd", { "text-anchor": "middle" }); });
  o += SV.line(60, 280, 330, 280) + SV.line(410, 280, 680, 280);
  if (s.b > 0) o += tag(380, 70, "barriers: housing, transport, family ties", "t4", s.b, "middle");
  if (s.a > 0) o += arrow(300, 140, 360, 140, "r", "c1", s.a) + tag(330, 132, "workers move", "t1", s.a, "middle");
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 330, label: "Unemployment and wages in two regions as labour mobility increases", base: { m: 0, b: 0, a: 0 }, draw: regDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>Immobile labour.</b> Region A has unemployment of 12% and wages of $80k. Region B has 3% unemployment, vacancies and wages of $120k. If workers could move freely, labour would flow from A to B.", s: { m: 0 } },
  { cap: "<b>Barriers.</b> Housing in B is dear, public transport is poor, families and schools tie workers to A, and moving is costly. Few people move, so the gaps stay open: <b>regional structural unemployment</b>.", s: { m: 0, b: 1 } },
  { cap: "<b>Policy to raise mobility.</b> Affordable housing, relocation grants, better transport and job information reduce the barriers. Some workers move from A to B.", s: { m: 0.5, b: 0.5, a: 1 } },
  { cap: "<b>Greater mobility.</b> Unemployment in A falls, wages in A rise a little, and B fills its vacancies, though B's wages fall slightly as labour supply grows. The gaps narrow and the economy produces more.", s: { m: 1, b: 0, a: 1 } },
] });

/* ---------- Watch 2: skills gap ---------- */
function skDraw(s) {
  let o = SV.rect(60, 100, 200, 120, "f2") + tag(160, 130, "Declining job", "t2", 1, "middle") + SV.text(160, 160, "e.g. coal mining", "lbl", { "text-anchor": "middle" }) + SV.text(160, 182, "skills: heavy machinery,", "sm", { "text-anchor": "middle" }) + SV.text(160, 198, "safety, teamwork", "sm", { "text-anchor": "middle" });
  o += SV.rect(500, 100, 200, 120, "f3") + tag(600, 130, "Growing job", "t3", 1, "middle") + SV.text(600, 160, "e.g. solar installer", "lbl", { "text-anchor": "middle" }) + SV.text(600, 182, "needs: electrical skills,", "sm", { "text-anchor": "middle" }) + SV.text(600, 198, "certification, roof safety", "sm", { "text-anchor": "middle" });
  const gx = 270 + (1 - s.g) * 0, w = 220 * s.g; o += SV.rect(270, 150, 220, 22, "f4", op(0.35)) + SV.rect(270, 150, 220 - w, 22, "f4", op(0.9)) + SV.rect(270 + 220 - w, 150, w, 22, "f3", op(0.9)) + tag(380, 140, s.g < 0.99 ? "skills gap" : "gap closed", s.g < 0.99 ? "t4" : "t3", 1, "middle");
  if (s.t > 0) o += tag(380, 200, s.l, "t1", s.t, "middle");
  return o;
}
Lib.stepper($("#stO"), { w: 760, h: 300, label: "Skills gap between a declining occupation and a growing occupation closing with training", base: { g: 0, t: 0, l: "" }, draw: skDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>A mismatch.</b> A mine closes while installers of solar panels are in short supply. The miners are unemployed and the installers' jobs are vacant, because the skills do not match: <b>occupational immobility</b>.", s: { g: 0 } },
  { cap: "<b>Transferable skills.</b> Some skills carry over (working with machinery, safety, teamwork), which narrows the gap a little. Workers with transferable skills move more easily.", s: { g: 0.3, t: 1, l: "transferable skills" } },
  { cap: "<b>Retraining.</b> Subsidised courses in electrical skills and certification close most of the gap. This costs money and takes months.", s: { g: 0.8, t: 1, l: "retraining and certification" } },
  { cap: "<b>The move.</b> Workers are hired as installers. Structural unemployment falls and vacancies are filled, but it only works if enough vacancies exist and the pay is attractive.", s: { g: 1, t: 1, l: "workers hired" } },
] });

/* ---------- Lab 1: move or stay ---------- */
function labMove() {
  if (!$("#mw") || !$("#mc") || !$("#mh") || !$("#my")) return;
  const w = +$("#mw").value, c = +$("#mc").value, h = +$("#mh").value, y = +$("#my").value, net = w - h, pay = c > 0 && net > 0 ? c / net : Infinity, total = net * y - c;
  $("#r1").textContent = "$" + Lib.fmtN(net, 0); $("#r2").textContent = isFinite(pay) ? Lib.fmtN(pay, 1) + " years" : "Never"; $("#r3").textContent = (total >= 0 ? "+$" : "−$") + Lib.fmtN(Math.abs(total), 0);
  $("#rv").textContent = net <= 0 ? "Higher housing and living costs wipe out the pay rise, so a rational worker would not move. This is geographical immobility caused by costs." : total > 0 ? `The extra net pay of $${net} a year repays the $${c} cost of moving in ${Lib.fmtN(pay, 1)} years and leaves a net gain of $${Lib.fmtN(total, 0)} over ${y} years: the worker is likely to move.` : `It would take ${Lib.fmtN(pay, 1)} years to repay the cost of moving, longer than the ${y} years the worker expects to stay, so the move does not pay.`;
  const mx = Math.max(net * y, c, 1) * 1.1, Y = (v) => 250 - v / mx * 200;
  let o = SV.line(40, 250, 400, 250) + SV.rect(90, Y(Math.max(net, 0) * y), 90, 250 - Y(Math.max(net, 0) * y), "f3") + SV.rect(240, Y(c), 90, 250 - Y(c), "f2") + tag(135, Y(Math.max(net, 0) * y) - 6, "$" + Lib.fmtN(Math.max(net, 0) * y, 0), "t3", 1, "middle") + tag(285, Y(c) - 6, "$" + c, "t2", 1, "middle") + SV.text(135, 270, "Extra net pay over " + y + " yrs", "sm bd", { "text-anchor": "middle" }) + SV.text(285, 270, "Cost of moving", "sm bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "mw", label: "Extra annual pay in region B ($) ", min: 0, max: 12000, step: 500, value: 6000, fmt: (v) => v, onInput: labMove });
Lib.slider($("#g2"), { id: "mh", label: "Extra housing and living costs a year ($) ", min: 0, max: 12000, step: 500, value: 3000, fmt: (v) => v, onInput: labMove });
Lib.slider($("#g3"), { id: "mc", label: "One-off cost of moving ($) ", min: 0, max: 15000, step: 500, value: 4500, fmt: (v) => v, onInput: labMove });
Lib.slider($("#g4"), { id: "my", label: "Years the worker expects to stay ", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: labMove });
labMove();
btnTable("lbBtns", "lbOut", [
  ["High house prices where the jobs are", "Geographical", "Workers cannot afford to move to jobs", "Affordable housing, relocation grants, rent support"],
  ["Poor public transport", "Geographical", "Commuting to vacancies is slow or costly", "Transport investment, remote working, commuter subsidies"],
  ["Family and school ties", "Geographical", "Workers unwilling to leave the area", "Remote work, support for relocating families"],
  ["Skills specific to one industry", "Occupational", "Workers cannot do the vacant jobs", "Retraining, apprenticeships, general education"],
  ["Professional licences and union entry rules", "Occupational", "Hard to enter new occupations", "Recognise experience and foreign qualifications"],
  ["Lack of information about vacancies", "Both", "Workers do not know where jobs are", "Job centres, online vacancy platforms, careers advice"],
  ["Older age and short working life left", "Occupational", "Little incentive to retrain", "Training subsidies for older workers, anti-age-discrimination laws"]
], ["Barrier", "Type affected", "Effect", "Possible policy"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Does the factor mainly affect geographical or occupational mobility?", buckets: [{"label": "Geographical mobility"}, {"label": "Occupational mobility"}], items: [{"text": "High rents in the city with the vacancies", "b": 0}, {"text": "A skills certificate for a growing industry", "b": 1}, {"text": "Poor rail links between regions", "b": 0}, {"text": "Professional licensing rules", "b": 1}, {"text": "Family and school ties", "b": 0}, {"text": "Transferable skills from general education", "b": 1}, {"text": "Visa and immigration rules", "b": 0}, {"text": "A government retraining subsidy", "b": 1}], done: "Geographical is where you work; occupational is what you do." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Geographical mobility", "Ability to move area or country for work"], ["Occupational mobility", "Ability to change job or industry"], ["Structural unemployment", "Mismatch of skills or location with vacancies"], ["Transferable skills", "Skills useful in many jobs"], ["Remittances", "Money sent home by migrant workers"], ["Brain drain", "Emigration of skilled workers from a country"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of low mobility in order.", items: ["An industry declines and jobs are lost in one region", "Workers cannot move or retrain because of high housing costs and specific skills", "Unemployment stays high in that region while vacancies exist elsewhere", "The natural rate of unemployment is higher", "Output is lower than it could be"], done: "Low mobility turns a local shock into lasting structural unemployment." });
Lib.calc($("#c1"), { qs: [
  {"q": "A worker would earn $6,000 a year more in another city but pay $3,000 more in housing costs. Calculate the extra net income a year ($).", "a": 3000, "unit": "$", "tol": 0.5, "hint": "Subtract the extra cost.", "sol": "6,000 − 3,000 = <b>$3,000</b>."},
  {"q": "Moving costs the worker $4,500 once. Using the extra net income above, calculate how many years it takes to repay the cost.", "a": 1.5, "unit": "years", "tol": 0.05, "hint": "Cost ÷ extra net income.", "sol": "4,500 ÷ 3,000 = <b>1.5 years</b>."},
  {"q": "Region A has 80,000 unemployed and 5,000 vacancies. Calculate the number of unemployed people per vacancy.", "a": 16, "tol": 0.05, "hint": "Unemployed ÷ vacancies.", "sol": "80,000 ÷ 5,000 = <b>16</b>."},
  {"q": "A retraining programme costs $8,000 per worker and 400 workers take part. Calculate the total cost ($ million).", "a": 3.2, "unit": "$m", "tol": 0.05, "hint": "8,000 × 400 = 3,200,000.", "sol": "8,000 × 400 = $3.2 million."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a barrier to geographical mobility?", opts: ["Retraining schemes", "High house prices in areas with vacancies", "General education", "Online job boards"], a: 1, why: "If housing is unaffordable where the jobs are, workers cannot move." },
  { q: "Which is a barrier to occupational mobility?", opts: ["Skills specific to one industry", "Cheap public transport", "Low rents", "Relocation grants"], a: 0, why: "Specific skills prevent a move to a different type of job." },
  { q: "Unemployment and vacancies both rise in a country. What is the most likely explanation?", opts: ["Demand-deficient unemployment", "A mismatch of skills or location", "A rise in the minimum wage only", "A fall in the labour force"], a: 1, why: "The unemployed lack the skills or location the vacancies need: structural unemployment." },
  { q: "A government subsidises retraining. Which effect on the labour market is most likely?", opts: ["Occupational mobility rises", "Geographical mobility must fall", "The natural rate rises", "Demand for labour falls"], a: 0, why: "Retraining gives workers the skills to move into other occupations." },
  { q: "Which is a possible cost of large-scale emigration for the home country?", opts: ["A brain drain", "Lower remittances", "A fall in wages abroad", "A larger labour force"], a: 0, why: "Skilled workers who leave reduce the home country's productive capacity." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Geographical mobility", "Ease of moving area or country for work."],
  ["Occupational mobility", "Ease of changing job or industry."],
  ["Structural unemployment", "Mismatch of skills or location with the jobs available."],
  ["Transferable skills", "Skills that can be used in many jobs."],
  ["Brain drain", "Skilled workers emigrating."],
  ["Remittances", "Money migrants send home."],
  ["Relocation grant", "Payment to help a worker move for a job."],
  ["Job centre", "Service that matches unemployed workers with vacancies."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is likely to improve the occupational mobility of labour? (Feb/March 2025 · 32 · Q18, reworded)", opts: ["A cut in income tax that raises aggregate demand", "A cut in unemployment benefit", "An increase in retraining schemes for the unemployed", "More advertising of vacancies across the economy"], a: 2, why: "Retraining gives workers the skills to move between occupations. Advertising helps information more than skills." },
  { q: "What is a factor affecting the occupational mobility of labour? (May/June 2025 · 31 · Q18, reworded)", opts: ["Education and training", "Immigration controls", "The price of housing", "Transport infrastructure"], a: 0, why: "Education and training decide which jobs a worker can do. Housing and transport affect geographical mobility." },
  { q: "Which government policy is most likely to improve occupational mobility? (Oct/Nov 2023 · 32 · Q16, reworded)", opts: ["Lower income tax rates", "More spending on education and training", "More spending on infrastructure", "Subsidies to firms that employ school leavers"], a: 1, why: "Education and training build skills that let workers change occupation." },
  { q: "In country X, unemployment is rising at the same time as the number of job vacancies. What is the most likely reason? (Oct/Nov 2024 · 31 · Q17, reworded)", opts: ["Economic growth is falling", "Economic growth is rising", "Geographical mobility of labour is rising", "Occupational immobility of labour is rising"], a: 3, why: "If the unemployed lack the skills for the vacancies, both can rise together: structural unemployment." },
  { q: "When is the natural rate of unemployment most likely to fall? (Oct/Nov 2024 · 32 · Q17, reworded)", opts: ["When education levels fall", "When income tax rises", "When labour mobility increases", "When unemployment benefits rise"], a: 2, why: "More mobile workers fill vacancies faster, which reduces frictional and structural unemployment." },
  { q: "Which statement about unemployment is correct? (Oct/Nov 2022 · 31 · Q21, reworded)", opts: ["Cyclical unemployment is caused by occupational immobility", "Frictional unemployment is caused by lack of information on jobs", "Structural unemployment is caused by deficient aggregate demand", "Voluntary unemployment is caused by seasonal variation in demand"], a: 1, why: "Poor information about vacancies lengthens the search period. Occupational immobility causes structural unemployment, not cyclical." },
  { q: "Many workers in developed countries work from home after a pandemic, leading to closures of city-centre cafes and retailers. If this continues, what is most likely? (Oct/Nov 2023 · 33 · Q18, reworded)", opts: ["Frictional unemployment will decrease", "Geographical mobility of labour will increase", "Structural unemployment will increase", "Voluntary unemployment will increase"], a: 2, why: "Jobs in city-centre services disappear and the former workers need new skills or locations: structural unemployment." },
  { q: "A firm faces a shortage of labour and starts its own training scheme for school leavers. What is the most likely effect on the firm? (Oct/Nov 2023 · 31 · Q13, reworded)", opts: ["A fall in the number of workers employed", "A fall in the productivity of the workforce", "A rise in the geographical mobility of its labour", "A shift of the supply curve of labour to the firm to the right"], a: 3, why: "Training creates more workers with the right skills, shifting the supply of labour to the firm to the right." },
] });
