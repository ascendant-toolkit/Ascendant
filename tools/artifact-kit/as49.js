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

/* ---------- PPC and unemployment ---------- */
function ppDraw(s) {
  const X = (q) => 80 + q * 6, Y = (p) => 270 - p * 2.4; let o = axes(80, 270, 700, 30, "Capital goods", "Consumer goods"), d = "";
  for (let a = 0; a <= 90; a += 5) { const r = a * Math.PI / 180, x = 85 * Math.cos(r), y = 95 * Math.sin(r); d += (a ? " L" : "M") + X(x) + "," + Y(y); }
  o += SV.path(d, "c2", { fill: "none", "stroke-width": 3.5 }) + tag(X(75), Y(18), "PPC", "c2");
  const f = 1 - 0.3 * s.u, px = 60 * f, py = 66 * f; o += SV.circle(X(px), Y(py), 8, "dot3") + SV.text(X(px) + 14, Y(py) + 4, s.u > 0.5 ? "Actual output (unemployment)" : "Full employment", "lbl bd", { ...halo });
  if (s.u > 0.5) { const qx = 60, qy = 66; o += SV.line(X(px), Y(py), X(qx) - 4, Y(qy) + 4, "dash") + SV.circle(X(qx), Y(qy), 6, "dot1", op(0.6)) + SV.text(X(qx) + 10, Y(qy) - 8, "Potential", "sm"); }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Output inside the production possibility curve because of unemployment">${ppDraw({ u: 1 })}</svg>`;
Lib.stepper($("#stP"), { w: 760, h: 300, label: "Unemployment and the production possibility curve", base: { u: 0 }, draw: ppDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Full employment.</b> The economy uses all its resources and produces on the PPC.", s: { u: 0 } },
  { cap: "<b>Unemployment.</b> Workers and capital are idle, so the economy produces at a point <b>inside</b> the PPC: less of both goods than it could.", s: { u: 1 } },
  { cap: "<b>Recovery.</b> When the unemployed find work, output moves back towards the PPC, raising living standards.", s: { u: 0 } },
] });

function bgDraw(s) {
  const Y = (v) => 250 - v * 2; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "$bn", "sm");
  const tax = 100 - 12 * s.u, ben = 30 + 18 * s.u;
  o += SV.rect(150, Y(tax), 120, 250 - Y(tax), "f2", op(0.65)) + SV.text(210, 270, "Tax revenue", "sm", { "text-anchor": "middle" }) + SV.text(210, Y(tax) - 6, Lib.fmtN(tax, 0), "lbl bd", { "text-anchor": "middle" });
  o += SV.rect(330, Y(ben), 120, 250 - Y(ben), "f3", op(0.65)) + SV.text(390, 270, "Benefit spending", "sm", { "text-anchor": "middle" }) + SV.text(390, Y(ben) - 6, Lib.fmtN(ben, 0), "lbl bd", { "text-anchor": "middle" });
  o += SV.rect(510, Y(Math.max(0, ben - tax + 70)), 120, 250 - Y(Math.max(0, ben - tax + 70)), "f1", op(0.65)) + SV.text(570, 270, "Pressure on budget", "sm", { "text-anchor": "middle" }) + SV.text(570, Y(Math.max(0, ben - tax + 70)) - 6, Lib.fmtN(ben - tax + 70, 0), "lbl bd", { "text-anchor": "middle" });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Tax revenue falls and benefit spending rises as unemployment rises">${bgDraw({ u: 1 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 290, label: "Tax revenue and benefit spending as unemployment rises", base: { u: 0 }, draw: bgDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Low unemployment.</b> Tax revenue is high and benefit spending low.", s: { u: 0 } },
  { cap: "<b>Unemployment rises.</b> Fewer people pay income tax and VAT, so revenue falls, and more people claim benefits, so spending rises.", s: { u: 1 } },
  { cap: "<b>A recession deepens.</b> The gap between spending and revenue widens: a larger budget deficit, with an opportunity cost for other services.", s: { u: 2 } },
] });

/* ---------- Lab 1 ---------- */
function labC() {
  if (!["un", "wg", "tx", "bn"].every((i) => $("#" + i))) return;
  const u = +$("#un").value, w = +$("#wg").value, t = +$("#tx").value / 100, b = +$("#bn").value, out = u * w / 1000, tax = out * t, ben = u * b / 1000;
  $("#r1").textContent = "$" + Lib.fmtN(out, 1) + "bn"; $("#r2").textContent = "$" + Lib.fmtN(tax, 1) + "bn"; $("#r3").textContent = "$" + Lib.fmtN(ben, 1) + "bn";
  $("#rv").textContent = `${u} thousand unemployed workers who could earn $${Lib.fmtN(w, 0)} each would produce about $${Lib.fmtN(out, 1)}bn a year. The government loses $${Lib.fmtN(tax, 1)}bn in tax and pays $${Lib.fmtN(ben, 1)}bn in benefits: a swing of $${Lib.fmtN(tax + ben, 1)}bn against the budget, which could have funded other services (the opportunity cost).`;
  const Y = (v) => 250 - v * 14; let o = SV.line(40, 250, 400, 250);
  [["Lost output", out, "f1"], ["Lost tax", tax, "f3"], ["Extra benefits", ben, "f3"]].forEach(([l, v, c], i) => (o += SV.rect(70 + i * 110, Math.max(30, Y(v)), 80, 250 - Math.max(30, Y(v)), c, op(0.65)) + SV.text(110 + i * 110, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, Math.max(30, Y(v)) - 6, Lib.fmtN(v, 1), "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "un", label: "Number of unemployed, thousands ", min: 100, max: 1000, step: 50, value: 500, fmt: (v) => v, onInput: labC });
Lib.slider($("#g2"), { id: "wg", label: "Output each could produce, $ per year ", min: 20000, max: 60000, step: 5000, value: 40000, fmt: (v) => "$" + Lib.fmtN(v, 0), onInput: labC });
Lib.slider($("#g3"), { id: "tx", label: "Average tax rate on that income, % ", min: 10, max: 40, step: 5, value: 25, fmt: (v) => v + "%", onInput: labC });
Lib.slider($("#g4"), { id: "bn", label: "Benefit paid per unemployed person, $ per year ", min: 5000, max: 20000, step: 1000, value: 9000, fmt: (v) => "$" + Lib.fmtN(v, 0), onInput: labC });
labC();

/* ---------- Lab 2 ---------- */
const GR = [["Unemployed individuals", "Lower income, skill decay, poorer health", "More leisure time (small)", "Income falls, so living standards and spending fall. The longer the spell, the more skills and confidence decay."], ["Firms", "Weaker demand for products", "Easier and cheaper recruitment", "Falling incomes cut spending, so firms sell less, but they may hire at lower wages."], ["The government", "Lower tax revenue and more benefits", "Less wage pressure and lower inflation", "The budget deficit rises, and the money has an opportunity cost in schools or hospitals."], ["The economy", "Output below potential, inside the PPC", "Lower inflation pressure", "Wasted resources reduce living standards and may reduce long-run growth if skills are lost."], ["Society", "Poverty, inequality and social problems", "None significant", "Concentrated unemployment can lead to crime, family stress and regional decline."]];
function showG(i) {
  const [g, m, o, why] = GR[i]; $$("#wB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = g; $("#t2").textContent = m; $("#t3").textContent = o; $("#tv").textContent = why;
  $("#labB").innerHTML = SV.rect(60, 50, 300, 90, "f3", { rx: 12, ...op(0.45) }) + SV.text(210, 105, g, "lbl bd", { "text-anchor": "middle", style: "font-size:20px" });
}
$("#wB").innerHTML = GR.map((g, i) => `<button class="b" data-i="${i}">${g[0]}</button>`).join("");
$$("#wB button").forEach((b) => (b.onclick = () => showG(+b.dataset.i)));
showG(0);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Cost or possible benefit of unemployment?", buckets: [{"label": "Cost"}, {"label": "Possible benefit"}], items: [{"text": "Lower income for the unemployed", "b": 0}, {"text": "Easier recruitment for firms", "b": 1}, {"text": "Lower government tax revenue", "b": 0}, {"text": "Less pressure on wages and inflation", "b": 1}, {"text": "Output below potential", "b": 0}, {"text": "Skills decay over time", "b": 0}, {"text": "Higher spending on benefits", "b": 0}, {"text": "Lower wage costs for employers", "b": 1}], done: "Costs fall on individuals, the government and the economy. Firms may gain easier recruitment and less wage pressure." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Opportunity cost", "Other spending given up to pay benefits"], ["Long-term unemployment", "Out of work for a year or more, with skills decaying"], ["Automatic stabiliser", "Benefits and taxes that cushion falling demand"], ["Inside the PPC", "Output below potential because resources are idle"], ["Hysteresis (skill decay)", "Long spells of unemployment reduce employability"], ["Youth unemployment", "Young people miss early work experience"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of rising unemployment on the budget in order.", items: ["More people lose their jobs", "Income tax and VAT revenue fall", "Spending on unemployment benefits rises", "The budget deficit widens", "Other spending may have to be cut or taxes raised"], done: "Lower revenue plus higher spending widens the deficit." });
Lib.calc($("#c1"), { qs: [
  {"q": "800,000 unemployed workers could each produce $30,000 a year. What output is lost ($bn)?", "a": 24, "unit": "$bn", "tol": 0.1, "hint": "800,000 × 30,000.", "sol": "<b>$24bn</b>."},
  {"q": "The average tax rate on that income is 20%. How much tax is lost ($bn)?", "a": 4.8, "unit": "$bn", "tol": 0.05, "hint": "0.2 × 24.", "sol": "<b>$4.8bn</b>."},
  {"q": "Benefits of $8,000 a year are paid to each of the 800,000. What is the total ($bn)?", "a": 6.4, "unit": "$bn", "tol": 0.05, "hint": "800,000 × 8,000.", "sol": "<b>$6.4bn</b>."},
  {"q": "What is the total effect on the budget (lost tax plus benefits) ($bn)?", "a": 11.2, "unit": "$bn", "tol": 0.05, "hint": "4.8 + 6.4.", "sol": "<b>$11.2bn</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A cost of unemployment to the government is:", opts: ["Lower tax revenue and higher benefits", "Higher tax revenue", "Lower welfare spending", "A budget surplus"], a: 0, why: "Both sides of the budget worsen." },
  { q: "Unemployment means the economy produces:", opts: ["Inside its PPC", "On its PPC", "Beyond its PPC", "At a fixed point"], a: 0, why: "Resources idle." },
  { q: "The most damaging type of unemployment is often:", opts: ["Long-term", "Frictional", "Seasonal for a week", "Voluntary"], a: 0, why: "Skills decay." },
  { q: "A possible benefit of unemployment for firms is:", opts: ["Easier recruitment", "Higher demand", "Higher tax revenue", "Lower inflation target"], a: 0, why: "More workers available." },
  { q: "Very low unemployment can cause:", opts: ["Wage and inflation pressure", "Deflation", "Lower AD", "A budget surplus always"], a: 0, why: "Labour shortages." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Individual", "Lower income, skill decay."],
  ["Firms", "Weaker demand."],
  ["Government", "Less tax, more benefits."],
  ["Economy", "Inside the PPC."],
  ["Society", "Inequality, crime."],
  ["Long-term", "Most damaging."],
  ["Low unemployment", "Inflation risk."],
  ["Opportunity cost", "Spending forgone."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is a cost of negative economic growth? (May/June 2024 · 13 · Q18, reworded)", opts: ["deteriorating balance of payments", "higher inflation", "higher unemployment", "increased pollution"], a: 2, why: "A falling real GDP means firms need fewer workers, so unemployment rises." },
  { q: "A major trading nation, country X, is in equilibrium at the full employment level of real output. There is then a recession in its main international markets. What are the most likely consequences of this change for country X? (rate of inflation, unemployment) (May/June 2024 · 11 · Q18, reworded)", opts: ["decrease, decrease", "decrease, increase", "unchanged, decrease", "unchanged, increase"], a: 1, why: "Falling export demand shifts AD left, lowering the price level and output, so unemployment rises." },
  { q: "The transition of centrally planned economies to market economies was accompanied by a significant change in the composition of output. What was an immediate consequence of this transition? (May/June 2020 · 11 · Q1, reworded)", opts: ["a build-up of unsold stocks of goods", "an increase in exports of goods", "an increase in unemployment", "decreasing prices of goods and services"], a: 2, why: "Closing inefficient state industries created structural unemployment." },
] });
