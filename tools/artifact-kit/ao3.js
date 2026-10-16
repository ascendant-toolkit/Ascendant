/* IGCSE Economics: Exam technique, Assessment Objective 3 (Evaluation) */
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const fade = (v) => clamp(v, 0, 1);

/* ---------- 1. one answer climbing the levels ---------- */
const CLIMB = [
  { tag: "Level 1", cls: "k", lines: ["A minimum wage is the lowest wage a firm is allowed to pay.", "It helps workers."], m: 2 },
  { tag: "Level 2", cls: "n", lines: ["Low-paid workers earn more, so their incomes may rise above the", "poverty line and they can afford more food: poverty may fall."], m: 4 },
  { tag: "Level 2+", cls: "n", lines: ["However, it might cause unemployment."], m: 5 },
  { tag: "Level 3", cls: "e", lines: ["Costs rise, so if demand for labour is elastic firms may cut jobs, and those", "workers lose all income. This depends on how high the wage is set."], m: 7 },
  { tag: "Level 3 top", cls: "e", lines: ["Overall a modest minimum wage is more likely to cut poverty, because", "few jobs may be lost, than a high one in a weak economy."], m: 8 },
];
function climbChart(s) {
  let o = "";
  CLIMB.forEach((r, k) => {
    const a = fade(s.i - k), y = 12 + k * 74, col = `var(--${r.cls})`;
    o += `<g opacity="${(0.08 + 0.92 * a).toFixed(2)}">` + SV.rect(12, y, 620, 66, "", { rx: 9, style: `fill:var(--surface);stroke:${col};stroke-width:${Math.round(s.i) === k ? 3.5 : 1.8}` });
    o += SV.rect(12, y, 100, 66, "", { rx: 9, style: `fill:${col};opacity:.2` }) + SV.text(62, y + 39, r.tag, "lbl bd", { "text-anchor": "middle", style: `fill:${col};font-size:13.5px` });
    r.lines.forEach((t, j) => { o += SV.text(124, y + (r.lines.length === 1 ? 39 : 29 + j * 20), t, "lbl", { style: "font-size:13px" }); });
    o += "</g>";
  });
  const mh = (s.m / 8) * 300, mx = 676;
  o += SV.rect(mx, 36, 54, 300, "", { rx: 8, style: "fill:var(--soft);stroke:var(--line);stroke-width:2" });
  o += SV.rect(mx, 336 - mh, 54, mh, "", { rx: 8, style: `fill:${s.m >= 6 ? "var(--good)" : s.m >= 3 ? "var(--warn)" : "var(--bad)"};opacity:.85` });
  [3, 6].forEach((v) => { const y = 336 - (v / 8) * 300; o += SV.line(mx - 8, y, mx + 62, y, "dash", { style: "stroke:var(--muted);stroke-width:1.5" }); });
  o += SV.text(mx + 27, 26, "Marks", "sm bd", { "text-anchor": "middle" }) + SV.text(mx + 27, 336 - mh - 8, Math.round(s.m), "lbl bd", { "text-anchor": "middle", style: "font-size:18px" });
  o += SV.text(mx - 12, 336 - (3 / 8) * 300 + 4, "L2", "sm", { "text-anchor": "end" }) + SV.text(mx - 12, 336 - (6 / 8) * 300 + 4, "L3", "sm", { "text-anchor": "end" });
  return o;
}
Lib.stepper($("#stU"), { w: 760, h: 372, label: "One answer improving from Level 1 to Level 3", base: { i: 0, m: 0 }, draw: climbChart, steps: [
  { cap: "Question: <i>Discuss whether or not a national minimum wage will reduce poverty.</i> We start with what a weak answer says.", s: { i: 0, m: 2 } },
  { cap: "<b>Level 1</b> is a definition and a loose claim. There is no chain, so the examiner has little to credit: 1 to 2 marks.", s: { i: 0, m: 2 } },
  { cap: "<b>Add analysis.</b> A developed chain of cause and effect moves the answer into Level 2: workers earn more, so poverty may fall.", s: { i: 1, m: 4 } },
  { cap: "<b>Add a second side, undeveloped.</b> \"It might cause unemployment\" is a bare statement. This is the top of Level 2.", s: { i: 2, m: 5 } },
  { cap: "<b>Develop the second side.</b> Give the reason (higher costs), the effect (firms cut jobs) and what it depends on. Now both sides are developed: Level 3.", s: { i: 3, m: 7 } },
  { cap: "<b>Conclude.</b> Pick a side and give a reason. A justified conclusion is what takes an answer to the top of Level 3.", s: { i: 4, m: 8 } },
] });

/* ---------- 2. balance ---------- */
const FOR = ["Higher incomes for low-paid workers", "Less poverty among those in work", "More spending in local shops"];
const AGAINST = ["Firms may cut jobs", "Hours may be reduced", "Prices may rise"];
function scaleChart(s) {
  const px = 380, py = 118, L = 250, th = (s.a * Math.PI) / 180, c = Math.cos(th), sn = Math.sin(th);
  const lx = px - L * c, ly = py - L * sn, rx = px + L * c, ry = py + L * sn, pw = 220;
  let o = SV.poly([[px, py + 6], [px - 40, 328], [px + 40, 328]], "f1") + SV.line(px, py, px, 328, "ax") + SV.line(px - 80, 328, px + 80, 328, "ax");
  o += SV.line(lx, ly, rx, ry, "c1", { style: "stroke-width:7;stroke-linecap:round" }) + SV.circle(px, py, 9, "dot1");
  [[lx, ly, 0], [rx, ry, 1]].forEach(([x, y, side]) => {
    o += SV.line(x - pw / 2 + 8, y, x, y + 56, "gr", { style: "stroke-dasharray:none;stroke:var(--muted)" }) + SV.line(x + pw / 2 - 8, y, x, y + 56, "gr", { style: "stroke-dasharray:none;stroke:var(--muted)" });
    o += SV.rect(x - pw / 2, y + 56, pw, 10, "", { rx: 4, style: "fill:var(--ink);opacity:.8" });
    const items = side === 0 ? FOR : AGAINST, n = side === 0 ? s.nl : s.nr, col = side === 0 ? "var(--good)" : "var(--bad)";
    items.forEach((t, k) => {
      const a = fade(n - k);
      if (a > 0.02) o += `<g opacity="${a.toFixed(2)}">` + SV.rect(x - pw / 2 + 4, y + 56 - 26 * (k + 1), pw - 8, 23, "", { rx: 5, style: `fill:var(--surface);stroke:${col};stroke-width:2` }) + SV.text(x, y + 56 - 26 * (k + 1) + 16, t, "sm", { "text-anchor": "middle", style: "font-size:11.5px;fill:var(--ink)" }) + "</g>";
    });
    const ea = side === 1 ? s.e1 : s.e2;
    if (ea > 0.02) {
      const ty = y + 56 - 26 * (items.length + 1) - 4, txt = side === 1 ? "Condition: HIGH wage, weak economy" : "Condition: MODEST wage, jobs plentiful";
      o += `<g opacity="${fade(ea).toFixed(2)}">` + SV.rect(x - pw / 2 + 2, ty, pw - 4, 36, "", { rx: 6, style: "fill:var(--warn-soft);stroke:var(--warn);stroke-width:2.5" }) + SV.text(x, ty + 15, txt.split(":")[0] + ":", "sm bd", { "text-anchor": "middle", style: "font-size:11px;fill:var(--warn)" }) + SV.text(x, ty + 29, txt.split(": ")[1], "sm bd", { "text-anchor": "middle", style: "font-size:11px;fill:var(--ink)" }) + "</g>";
    }
  });
  o += SV.text(lx, 28, "Reasons it might", "lbl bd t3", { "text-anchor": "middle", style: "font-size:14px" }) + SV.text(rx, 28, "Reasons it might not", "lbl bd t2", { "text-anchor": "middle", style: "font-size:14px" });
  if (s.j > 0.02) o += `<g opacity="${fade(s.j).toFixed(2)}">` + SV.rect(100, 346, 560, 48, "", { rx: 10, style: "fill:var(--accent-soft);stroke:var(--accent);stroke-width:2.5" }) + SV.text(380, 376, "Conclusion: it tips towards \"reduces poverty\" if the rise is modest and jobs are plentiful", "lbl bd t1", { "text-anchor": "middle", style: "font-size:13.5px" }) + "</g>";
  return o;
}
Lib.stepper($("#stW"), { w: 760, h: 410, label: "A balance scale weighing two sides of an argument", base: { a: 0, nl: 0, nr: 0, e1: 0, e2: 0, j: 0 }, draw: scaleChart, steps: [
  { cap: "<i>Discuss whether or not a minimum wage will reduce poverty.</i> The scales are empty. A conclusion is the act of <b>weighing</b>.", s: { a: 0, nl: 0, nr: 0, e1: 0, e2: 0, j: 0 } },
  { cap: "<b>Side 1:</b> the reasons it might work, each as a developed point. The scale tips to the left.", s: { a: -7, nl: 3, nr: 0, e1: 0, e2: 0, j: 0 } },
  { cap: "<b>Side 2:</b> different reasons it might not, each developed. Now both sides carry weight, and the scales are close to level: a Level 3 answer needs both.", s: { a: 1.5, nl: 3, nr: 3, e1: 0, e2: 0, j: 0 } },
  { cap: "<b>Weigh the conditions.</b> If the wage is set <b>high in a weak economy</b>, the job losses weigh more. The scale tips to the right.", s: { a: 10, nl: 3, nr: 3, e1: 1, e2: 0, j: 0 } },
  { cap: "Change the condition. If the wage is <b>modest and jobs are plentiful</b>, the job-loss arguments weigh less. The scale tips the other way.", s: { a: -10, nl: 3, nr: 3, e1: 0, e2: 1, j: 0 } },
  { cap: "<b>Conclude.</b> Say which way it is likely to tip and why. The same arguments can give a different conclusion under different conditions.", s: { a: -10, nl: 3, nr: 3, e1: 0, e2: 1, j: 1 } },
] });

/* ---------- 3. five stems ---------- */
const STEMS = [
  ["Will / would", "Will an increase in the rate of interest reduce spending?", "Say what is likely, then when it could differ: circumstances, size, time."],
  ["Benefit / harm", "Does a current account deficit harm an economy?", "Who gains, who loses; short run against long run."],
  ["Should", "Should a government impose a maximum price on food?", "Opportunity cost and alternatives; then make a choice."],
  ["Can / could", "Can a tax on a product reduce external costs?", "How far does it work: size, responsiveness, other factors."],
  ["Always / all", "Do MNCs always benefit their host countries?", "Look for the exceptions: one counter-example breaks it."],
];
function wrap(txt, max) { const out = []; let cur = ""; txt.split(" ").forEach((w) => { if ((cur + " " + w).trim().length > max) { out.push(cur.trim()); cur = w; } else cur += " " + w; }); out.push(cur.trim()); return out; }
function stemChart(s) {
  let o = "";
  STEMS.forEach((r, k) => {
    const on = Math.abs(s.i - k) < 0.5, y = 10 + k * 64;
    o += `<g opacity="${on ? 1 : 0.3}">` + SV.rect(10, y, 740, 56, "", { rx: 9, style: `fill:${on ? "var(--accent-soft)" : "var(--surface)"};stroke:${on ? "var(--accent)" : "var(--line)"};stroke-width:${on ? 3 : 1.5}` });
    o += SV.text(24, y + 24, r[0], "lbl bd", { style: "font-size:15px;fill:var(--accent)" });
    wrap(r[1], 40).forEach((l, j) => { o += SV.text(24, y + 41 + j * 12, l, "sm", { style: "font-size:11.5px;font-style:italic" }); });
    o += SV.line(300, y + 10, 300, y + 46, "gr");
    wrap(r[2], 58).forEach((l, j, a) => { o += SV.text(314, y + (a.length === 1 ? 34 : 25 + j * 17), l, "lbl", { style: "font-size:13px" }); });
    o += "</g>";
  });
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 336, label: "Five stems and what each one needs", base: { i: 0 }, draw: stemChart, steps: STEMS.map((r, k) => ({ cap: `<b>${r[0]}.</b> ${r[2]}`, s: { i: k } })) });

/* ---------- 4. timeline ---------- */
const PLAN = [["Plan", 2, "k"], ["Side 1", 3, "good"], ["Side 2", 3, "bad"], ["Conclusion", 2, "e"], ["Check", 2, "n"]];
function planChart(s) {
  const x0 = 30, W = 700, per = W / 12, y = 90;
  let o = SV.line(x0, y + 60, x0 + W, y + 60, "ax"), t = 0;
  PLAN.forEach(([n, d, cls]) => {
    const fill = clamp(s.t - t, 0, d), col = `var(--${cls})`;
    o += SV.rect(x0 + t * per, y, d * per, 52, "", { rx: 6, style: `fill:var(--surface);stroke:${col};stroke-width:2` }) + SV.rect(x0 + t * per, y, fill * per, 52, "", { rx: 6, style: `fill:${col};opacity:.35` });
    o += SV.text(x0 + (t + d / 2) * per, y + 32, n, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" }) + SV.text(x0 + (t + d / 2) * per, y + 88, d + " min", "sm", { "text-anchor": "middle" });
    t += d;
  });
  for (let m = 0; m <= 12; m += 2) o += SV.line(x0 + m * per, y + 56, x0 + m * per, y + 66, "ax") + SV.text(x0 + m * per, y + 106, m, "sm", { "text-anchor": "middle" });
  o += SV.circle(x0 + clamp(s.t, 0, 12) * per, y - 16, 8, "dot1") + SV.text(x0 + clamp(s.t, 0, 12) * per, y - 34, Math.round(s.t) + " min", "lbl bd t1", { "text-anchor": "middle" });
  o += SV.text(380, 226, "About 1.5 minutes a mark: 8 marks is about 12 minutes", "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 240, label: "A 12-minute plan for an 8-mark answer", base: { t: 0 }, draw: planChart, steps: [
  { cap: "An 8-mark Discuss answer deserves about <b>12 minutes</b>. Paper 2 is 80 marks in 120 minutes, which is 1.5 minutes a mark.", s: { t: 0 } },
  { cap: "<b>Plan, 2 minutes.</b> Underline the command and scope words (\"whether or not\", \"always\"). Jot two reasons for and two against.", s: { t: 2 } },
  { cap: "<b>Side 1, 3 minutes.</b> One or two developed points, each as a chain.", s: { t: 5 } },
  { cap: "<b>Side 2, 3 minutes.</b> A new argument with its own chain.", s: { t: 8 } },
  { cap: "<b>Conclusion, 2 minutes.</b> Which side is stronger, and why.", s: { t: 10 } },
  { cap: "<b>Check, 2 minutes</b> if you have it: are both sides developed? Does the conclusion give a reason? Hedged words, not \"will\" and \"always\"?", s: { t: 12 } },
] });

/* ================= LABS ================= */
const TOPICS = [
  { n: "A higher indirect tax on a demerit good", s: [
    "A tax that is small compared with the price may hardly change what people buy; a very large one could push buyers towards illegal markets.",
    "Habits may change slowly, so quantity could fall by more in the long run than in the short run.",
    "If demand is inelastic, as with addictive goods, quantity may fall only a little and consumers may bear most of the tax.",
    "The government gains revenue and society may gain from lower external costs, but poorer buyers and producers could lose.",
    "The revenue could fund health campaigns or healthcare, so the gain may be larger than the tax if it is well spent.",
    "The effect depends on incomes, the substitutes available and whether neighbouring countries tax the good less.",
    "Advertising bans or education campaigns might work better alongside, or instead of, the tax.",
    "Higher prices may hit poorer households hardest, which could conflict with the aim of a fairer distribution of income."] },
  { n: "A rise in government spending", s: [
    "A small rise may do little to aggregate demand; a very large one may need heavy borrowing.",
    "Benefit payments act quickly, but spending on infrastructure or education may take years to raise output.",
    "If households save or buy imports, the multiplier is smaller and the rise in AD could be limited.",
    "Workers and firms that receive the spending may gain; taxpayers and future generations could pay for it.",
    "Money spent on one project cannot be spent on another, for example healthcare instead of education.",
    "With spare capacity output may rise; near full capacity the extra demand could mainly raise prices.",
    "Tax cuts or supply-side policies might raise output with less borrowing.",
    "Growth and jobs may come at the cost of a bigger budget deficit or higher inflation."] },
  { n: "A subsidy to producers", s: [
    "A small subsidy may not change output much; a large one could be very costly for the government.",
    "Firms may expand slowly, while the cost to the government begins at once.",
    "If supply is inelastic, output may rise little and producers may keep much of the subsidy as extra profit.",
    "Producers and consumers may gain, but taxpayers pay and producers in other countries may lose sales.",
    "The same money could have paid for health or education.",
    "A subsidy to a new industry may help it grow, but a long-term subsidy could make firms less efficient.",
    "Lower taxes on the firm or investment in training might be cheaper ways of helping.",
    "It may protect jobs and output but widen the budget deficit."] },
  { n: "A maximum price (price ceiling)", s: [
    "Set just below equilibrium the shortage may be small; set far below it could be large.",
    "In the short run supply may be fixed, but over time firms may leave the market and supply could shrink.",
    "If supply is elastic, firms may cut output by a lot, so the shortage could be larger.",
    "Consumers who can buy gain; those who cannot find any, and producers, may lose.",
    "Rationing and enforcing the limit use resources, and subsidising producers would cost the government.",
    "In a short emergency a maximum price may protect poorer people, but over many years it may cause lasting shortages.",
    "Subsidies or vouchers for the poor might help without causing a shortage.",
    "It improves affordability but may create black markets and lower quality."] },
  { n: "A rise in the rate of interest", s: [
    "A small rise may do little to borrowing; a large one could cut spending sharply.",
    "Spending may take months to respond, so effects could arrive after the economy has changed.",
    "Households on fixed-rate loans, or with large savings, may change their spending very little.",
    "Savers may gain; borrowers and firms with loans lose.",
    "Firms may postpone investment, giving up future productive capacity.",
    "If confidence is very high, firms and households may keep borrowing even at higher rates.",
    "Higher taxes or lower government spending could also cool demand.",
    "It may reduce inflationary pressure but also slow growth and raise unemployment."] },
  { n: "Tariffs on imports", s: [
    "A small tariff may not change consumer choices; a very high one could shut out imports.",
    "Protected firms may become more efficient or more complacent over time, and other countries may retaliate quickly.",
    "If demand for the import is inelastic, consumers keep buying and the government earns more revenue; if elastic, imports fall.",
    "Domestic producers and their workers may gain; consumers pay more and exporters may face retaliation.",
    "Resources kept in protected industries could be used where the country is more efficient.",
    "A temporary tariff on a new industry may help it grow; on an established industry it may protect inefficiency.",
    "Subsidies or training might protect jobs without raising prices.",
    "It may protect jobs but conflict with lower prices for consumers and good trade relations."] },
  { n: "A foreign MNC opening in the country", s: [
    "A small plant may add little; a very large one could dominate the local economy.",
    "Jobs and tax revenue may come quickly, but the MNC could leave if costs rise elsewhere.",
    "If local firms can supply the MNC, benefits spread; if not, imports may rise and the local effect could be small.",
    "Workers and consumers may gain; local rivals may lose and profits may leave the country.",
    "Tax breaks used to attract it are revenue the government gives up.",
    "Where unemployment is high and skills are available the benefit is larger; where rules are weak, pollution and poor conditions may follow.",
    "Supporting local firms or training could build the economy with less dependence on one firm.",
    "More growth and jobs may come with environmental damage and less competition for local firms."] },
  { n: "A national minimum wage", s: [
    "A wage set slightly above equilibrium may cost few jobs; a high one could cause more unemployment.",
    "Firms may first absorb the cost, then cut hiring or buy machinery in the long run.",
    "If demand for labour is inelastic, little employment is lost; if elastic, job losses could be larger.",
    "Low-paid workers who keep their jobs gain; those who lose jobs, and firms with high costs, lose.",
    "Higher costs may mean less spending on training or investment.",
    "In a tight labour market the effect on jobs may be small; in a recession it could be larger.",
    "Tax credits or training might raise incomes with less risk to jobs.",
    "It may reduce poverty but raise firms' costs and prices."] },
];
const ANGLES = ["Size", "Time", "Responsiveness", "Winners and losers", "Opportunity cost", "Circumstances", "Alternatives", "Conflict of aims"];
(function () {
  const el = $("#lf");
  let ti = 0, li = 0;
  el.innerHTML = `<p class="note" style="margin-top:0">1 · Policy or event</p><div class="row" id="lft"></div><p class="note">2 · Angle</p><div class="row" id="lfl"></div>
    <div class="verdict" id="lfo" aria-live="polite" style="margin-top:14px"></div><details style="margin-top:8px"><summary style="cursor:pointer;font-weight:700">All eight questions for this topic</summary><div class="tw"><table class="t" id="lfa"></table></div></details>`;
  const tw = $("#lft"), lw = $("#lfl");
  TOPICS.forEach((t, i) => { const b = document.createElement("button"); b.className = "b"; b.type = "button"; b.textContent = t.n; b.onclick = () => { ti = i; paint(); }; tw.appendChild(b); });
  ANGLES.forEach((l, i) => { const b = document.createElement("button"); b.className = "b"; b.type = "button"; b.textContent = i + 1 + " · " + l; b.onclick = () => { li = i; paint(); }; lw.appendChild(b); });
  function paint() {
    $$("button", tw).forEach((b, i) => b.classList.toggle("pri", i === ti));
    $$("button", lw).forEach((b, i) => b.classList.toggle("pri", i === li));
    $("#lfo").innerHTML = `<b>${esc(ANGLES[li])}:</b> ${esc(TOPICS[ti].s[li])}`;
    $("#lfa").innerHTML = "<tr><th>Angle</th><th>Evaluation sentence</th></tr>" + TOPICS[ti].s.map((s, i) => `<tr><td><b>${esc(ANGLES[i])}</b></td><td>${esc(s)}</td></tr>`).join("");
  }
  paint();
})();

const GR = ["missing", "stated", "explained", "developed chain"], JR = ["none", "restates the answer", "an opinion with a reason", "picks a side, gives a reason and a condition"];
function labM() {
  if (!$("#ma") || !$("#mb") || !$("#mc")) return;
  const s1 = +$("#ma").value, s2 = +$("#mb").value, jd = +$("#mc").value, raw = s1 + s2 + jd;
  let lvl, m;
  if (s1 >= 2 && s2 >= 2 && jd >= 2) { lvl = 3; m = 6 + (s1 + s2 >= 5 ? 1 : 0) + (jd === 3 && s1 + s2 >= 5 ? 1 : 0); }
  else if (s1 >= 2 || s2 >= 2) { lvl = 2; m = 3 + (raw >= 5 ? 1 : 0) + (raw >= 6 ? 1 : 0); }
  else if (raw > 0) { lvl = 1; m = 1 + (raw >= 3 ? 1 : 0); }
  else { lvl = 0; m = 0; }
  $("#mt1").textContent = lvl ? "Level " + lvl : "None"; $("#mt2").textContent = m + " / 8";
  let tip;
  if (lvl === 3) tip = "Both sides are explained and the conclusion gives a reason. To reach the top, develop the sides further and make the conclusion name a condition.";
  else if (s1 < 2 && s2 < 2) tip = "Neither side has a developed chain yet. Add an A leads to B leads to C chain to at least one side.";
  else if (s1 < 2 || s2 < 2) tip = "One side is developed but the other is only stated. A Level 3 answer develops both sides, even if one is shorter.";
  else tip = "Both sides are developed. Finish with a conclusion that picks a side and gives a reason.";
  $("#mtv").textContent = tip;
  const bars = [["Side 1", s1], ["Side 2", s2], ["Conclusion", jd]], cols = ["var(--good)", "var(--bad)", "var(--accent)"];
  let o = SV.line(120, 250, 720, 250);
  bars.forEach(([n, v], i) => {
    const x = 180 + i * 190, h = (v / 3) * 190;
    o += SV.rect(x, 250 - h, 110, h, "", { rx: 6, style: `fill:${cols[i]};opacity:.85` }) + SV.text(x + 55, 272, n, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 55, 250 - h - 8, v ? [null, "stated", "explained", "developed"][v] : "missing", "sm bd", { "text-anchor": "middle" });
  });
  [1, 2, 3].forEach((v) => (o += SV.line(120, 250 - (v / 3) * 190, 720, 250 - (v / 3) * 190, "gr")));
  $("#labM").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ma", label: "Side 1 (reasons it might)", min: 0, max: 3, step: 1, value: 2, fmt: (v) => GR[v], onInput: labM });
Lib.slider($("#g2"), { id: "mb", label: "Side 2 (reasons it might not)", min: 0, max: 3, step: 1, value: 1, fmt: (v) => GR[v], onInput: labM });
Lib.slider($("#g3"), { id: "mc", label: "Conclusion", min: 0, max: 3, step: 1, value: 1, fmt: (v) => JR[v], onInput: labM });

(function () {
  const items = [
    ["stem", "I read the stem (will, should, can, benefit, always) and answered what it asked."],
    ["for", "I developed at least one reason it might work as a chain (A leads to B leads to C)."],
    ["against", "I developed at least one different reason it might not work as a chain."],
    ["terms", "I used at least two economic terms correctly."],
    ["judge", "My conclusion says which side is stronger and gives a reason."],
    ["hedge", "I used hedged words (could, may, likely) rather than \"will\" and \"always\"."],
  ];
  const el = $("#chk");
  el.innerHTML = items.map(([k, t]) => `<label style="display:flex;gap:10px;align-items:flex-start;margin:7px 0;cursor:pointer"><input type="checkbox" data-k="${k}" style="margin-top:5px;accent-color:var(--accent);width:18px;height:18px"><span>${t}</span></label>`).join("") + `<div class="verdict" id="chkv" aria-live="polite"></div><div id="chkm" class="note"></div>`;
  const upd = () => {
    const on = {}; $$("input", el).forEach((i) => (on[i.dataset.k] = i.checked));
    const n = Object.values(on).filter(Boolean).length;
    let lvl;
    if (on.for && on.against && on.terms && on.judge) lvl = "Level 3 (6–8 marks)" + (on.stem && on.hedge ? ": likely 7–8" : ": likely 6–7");
    else if ((on.for || on.against) && on.terms) lvl = "Level 2 (3–5 marks)";
    else if (n > 0) lvl = "Level 1 (1–2 marks)";
    else lvl = "Tick what your answer contains";
    $("#chkv").textContent = lvl;
    const miss = items.filter(([k]) => !on[k]).map(([, t]) => t);
    $("#chkm").textContent = n && miss.length ? "Next, add: " + miss[0].replace(/^I /, "") : n ? "Nothing missing. Check the timing." : "";
  };
  $$("input", el).forEach((i) => i.addEventListener("change", upd)); upd();
})();

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each sentence <b>developing a reason</b> (how it works) or part of a <b>conclusion</b> (weighing the sides and giving a reason)?", buckets: [{ label: "Developing a reason" }, { label: "Conclusion" }], items: [
  { text: "A subsidy lowers firms' costs, so supply shifts right and the price falls.", b: 0 },
  { text: "A tariff raises the price of imports, so domestic producers may sell more.", b: 0 },
  { text: "Higher interest rates make borrowing dearer, so firms may invest less.", b: 0 },
  { text: "A maximum price below equilibrium creates a shortage.", b: 0 },
  { text: "If supply is inelastic, output may rise only a little, so the benefit may go to producers.", b: 0 },
  { text: "Overall, a small tariff on a new industry is more likely to help than a high one on an old industry, because it protects jobs while firms are learning.", b: 1 },
  { text: "On balance the subsidy is more likely to benefit consumers if supply is elastic, since output could then expand and prices fall.", b: 1 },
  { text: "A rate rise is likelier to reduce inflation in a boom, provided households have borrowed heavily, because their spending would fall.", b: 1 },
  { text: "Overall, a minimum wage is likelier to cut poverty if it is modest, since few jobs may be lost.", b: 1 },
], done: "Reasons build each side; the conclusion weighs the sides and says why." });
Lib.classify($("#cl2"), { prompt: "Is each feature typical of a <b>Level 2</b> or a <b>Level 3</b> answer?", buckets: [{ label: "Level 2" }, { label: "Level 3" }], items: [
  { text: "Both sides appear, but each is one or two lines", b: 0 },
  { text: "The second side is just \"it might not work\"", b: 0 },
  { text: "Side 2 is the reverse of side 1", b: 0 },
  { text: "The conclusion repeats what was already said", b: 0 },
  { text: "Analysis stops after one step", b: 0 },
  { text: "Each side has a developed chain of reasoning", b: 1 },
  { text: "The second side gives a reason and an effect", b: 1 },
  { text: "The conclusion picks a side and says why", b: 1 },
  { text: "The answer recognises that outcomes are uncertain", b: 1 },
  { text: "Uses the context or an example to show the effect", b: 1 },
], done: "The difference is development and reasons, not length." });
Lib.match($("#m1"), { prompt: "Match each idea to the sentence that uses it.", pairs: [
  ["Size", "A very small rise in the minimum wage may have almost no effect on jobs."],
  ["Time", "Firms may cut hours only after a year, when contracts end."],
  ["Responsiveness", "If demand is elastic, a tax may cut quantity by a lot."],
  ["Winners and losers", "Tenants who find a home at the lower rent gain, but landlords lose."],
  ["Opportunity cost", "The subsidy money could have paid for new schools."],
  ["Circumstances", "In a recession, lower interest rates may not make firms borrow."],
  ["Alternatives", "Food vouchers could help the poor without causing a shortage."],
  ["Conflict of aims", "Raising rates may cut inflation but also slow growth and jobs."],
], done: "These are all good sources of a second side or a reason in your conclusion." });
Lib.match($("#m2"), { prompt: "Match the stem to the strategy.", pairs: [
  ["Will / would…", "Say what is likely, then when it could differ"],
  ["Benefit / harm…", "Who gains and who loses; short run and long run"],
  ["Should…", "Opportunity cost and alternatives, then choose"],
  ["Can / could…", "How far it works: size and responsiveness"],
  ["Always / all…", "Look for exceptions"],
], done: "The stem tells you which judgement is wanted." });
Lib.order($("#o1"), { prompt: "Put the sentences of one paragraph in order.", items: [
  "A subsidy to farmers could increase the quantity of food supplied.",
  "It lowers farmers' costs, so supply shifts to the right and the price may fall.",
  "So a subsidy could make food cheaper and more available.",
  "However, if farmers' supply is inelastic, output may rise only a little.",
  "The benefit may then go to farmers as extra profit rather than to consumers as lower prices.",
], done: "Point, explain, link, then a developed second thought." });
Lib.order($("#o2"), { prompt: "Put the steps of answering an 8-mark Discuss question in order.", items: [
  "Read the stem and underline the command and scope words",
  "Plan: two reasons for and two against",
  "Write side 1 as a developed chain",
  "Write side 2 as a different developed chain",
  "Write a conclusion that picks a side and gives a reason",
], done: "Plan first, develop both sides, conclude." });
Lib.quiz($("#qz1"), { qs: [
  { q: "Where is AO3 Evaluation assessed?", opts: ["Paper 1 multiple choice", "Paper 2, mostly in the 8-mark part (d) questions and longer Section A Discuss parts", "In the definition questions", "Equally in every question"], a: 1, why: "Paper 1 has no AO3. In Paper 2 it is worth about 15% of the marks, concentrated in the Discuss questions." },
  { q: "Which change is <b>most</b> likely to move an answer from Level 2 to Level 3?", opts: ["A longer definition", "Both sides developed, and a conclusion that gives a reason", "More diagrams", "A longer introduction"], a: 1, why: "Level 3 needs both sides developed and a justified conclusion. Length does not move the level." },
  { q: "\"Discuss whether or not MNCs <b>always</b> benefit their host countries.\" What should you do with the word <i>always</i>?", opts: ["Ignore it", "Test it by finding where it does not hold", "Agree with it", "Define it"], a: 1, why: "Scope words such as always, all and only are tested: one exception is enough to challenge the claim." },
  { q: "Which sentence best develops <b>side 2</b> for \"a tax can reduce consumption\"?", opts: ["A tax raises firms' costs.", "A tax shifts supply to the left.", "However, if demand is inelastic, quantity may fall little, so the tax may mainly raise revenue.", "A tax is a payment to the government."], a: 2, why: "It gives a different argument with a reason and an effect." },
  { q: "A student ends: \"In conclusion, there are advantages and disadvantages.\" What is missing?", opts: ["A definition", "A conclusion that picks a side and gives a reason", "A diagram", "A second conclusion"], a: 1, why: "Summarising is not concluding. The examiner wants \"overall… is likelier… because…\"." },
  { q: "\"The tax revenue could have been used to build hospitals.\" Which idea is this?", opts: ["Size", "Time", "Opportunity cost", "Alternatives"], a: 2, why: "Opportunity cost is the next best use of the resources." },
  { q: "Roughly how long should an 8-mark Discuss answer take?", opts: ["4 minutes", "12 minutes", "20 minutes", "30 minutes"], a: 1, why: "Paper 2 is 80 marks in 120 minutes: about 1.5 minutes a mark." },
] });

/* ================= PAST QUESTIONS ================= */
(function () {
  const rows = [["Will / would / likely", 67], ["Benefit / harm / advantage", 29], ["Should", 22], ["Can / could", 13], ["Other (whether, always, all…)", 13]], tot = 144;
  $("#stat").innerHTML = rows.map(([n, c]) => `<div style="display:grid;grid-template-columns:minmax(150px,230px) 1fr 70px;gap:10px;align-items:center;margin:7px 0"><b>${n}</b><div style="background:var(--soft);border-radius:7px"><div class="bar" style="width:${(c / 67) * 100}%"></div></div><span style="font:700 .9rem var(--mono)">${c} · ${Math.round((c / tot) * 100)}%</span></div>`).join("") +
    `<p class="note">A "will" stem is the most common, so practise judging <i>likelihood</i> and naming conditions. Counted by first matching keyword (should, then will/would, then can/could, then benefit/harm), so a few questions could be classed differently.</p>`;
})();
const EX = [
  { t: "Will / would", c: [
    ["Discuss whether or not a cut in the rate of interest will increase investment.", "F/M 2020 P22", "Circumstances (confidence), time lags, size of the cut."],
    ["Discuss whether or not a national minimum wage will reduce poverty.", "M/J 2020 P21", "Size, responsiveness of firms, winners and losers."],
    ["Discuss whether or not a country will benefit from having a fixed foreign exchange rate system.", "O/N 2022 P21", "Circumstances, winners and losers, conflict of aims."],
    ["Discuss whether or not a decrease in government spending will increase unemployment.", "O/N 2023 P23", "Circumstances, time, opportunity cost."]] },
  { t: "Benefit / harm", c: [
    ["Discuss whether or not trade unions benefit workers.", "O/N 2023 P21", "Winners and losers: members and those who lose jobs."],
    ["Discuss whether or not workers benefit from division of labour.", "M/J 2020 P23", "Short run against long run, who gains, size of the gains."],
    ["Discuss whether or not a current account deficit on its balance of payments harms an economy.", "M/J 2020 P21", "Size and cause of the deficit, time, circumstances."],
    ["Discuss whether or not an ageing population is a benefit to an economy.", "M/J 2020 P22", "Winners and losers, short run against long run."]] },
  { t: "Should", c: [
    ["Discuss whether or not a government should impose a maximum price on food.", "O/N 2020 P22", "Winners and losers, size, alternatives (see Model 2)."],
    ["Discuss whether or not a central bank should raise the rate of interest.", "M/J 2020 P22", "Conflict of aims, winners and losers, alternatives."],
    ["Discuss whether or not a government should introduce a maximum price on housing.", "M/J 2024 P23", "Winners and losers, time, alternatives."],
    ["Discuss whether or not a government should provide free fruit to consumers.", "F/M 2024 P22", "Opportunity cost, whether it is targeted."]] },
  { t: "Can / could", c: [
    ["Discuss whether or not a tax on a product can reduce external costs.", "O/N 2023 P21", "Responsiveness (elasticity), size, avoidance."],
    ["Discuss whether or not high tariffs can reduce unemployment.", "O/N 2024 P21", "Winners and losers, retaliation, alternatives."],
    ["Discuss whether or not a merger can help a firm survive.", "O/N 2022 P21", "Circumstances, time, winners and losers."],
    ["Discuss whether or not supply-side policy measures can reduce unemployment.", "O/N 2020 P21", "Time lags, size, circumstances."]] },
  { t: "Always / all", c: [
    ["Discuss whether or not MNCs always benefit their host countries.", "M/J 2020 P23", "Winners and losers, conflict of aims (see Model 3)."],
    ["Discuss whether or not inflation is always a disadvantage to an economy.", "M/J 2022 P23", "Size of inflation, winners and losers, time."],
    ["Discuss whether or not skilled workers are always paid more than unskilled workers.", "F/M 2020 P22", "Exceptions: demand and supply, unions, time."],
    ["Discuss whether all monopolies have low costs of production.", "F/M 2021 P22", "Exceptions: economies of scale against complacency."]] },
];
$("#ex").innerHTML = EX.map((g) => `<details class="eq"><summary><span class="cmd">${g.t}</span> four real examples</summary><div class="body"><div class="tw"><table class="t"><tr><th>Question</th><th>Paper</th><th>What the conclusion could weigh</th></tr>${g.c.map((r) => `<tr><td>${esc(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td></tr>`).join("")}</table></div></div></details>`).join("");

/* ================= FLASHCARDS ================= */
Lib.cards($("#fc1"), { cards: [
  ["Evaluation", "Weighing arguments: giving both sides developed, and reaching a conclusion that gives a reason."],
  ["Conclusion", "A final paragraph that picks the stronger side and gives a reason, naming what it depends on if it can."],
  ["Size (angle)", "How big is the change? A small change may do little; a large one may cause side effects."],
  ["Time (angle)", "Short-run and long-run effects may differ, and some effects arrive late."],
  ["Responsiveness (angle)", "How much buyers, sellers or workers react: price elasticity and the multiplier in plain words."],
  ["Winners and losers (angle)", "Who gains and who loses: consumers, producers, workers, taxpayers, government."],
  ["Opportunity cost (angle)", "What is given up. The same resources could have been used elsewhere."],
  ["Circumstances (angle)", "The state of the economy or market that changes the result: spare capacity, a recession, confidence, an addictive good."],
  ["Alternatives (angle)", "Another policy or choice that might work better or cost less."],
  ["Conflict of aims (angle)", "Helping one objective may harm another: growth against inflation, jobs against the deficit."],
  ["Scope word", "Words such as always, all, only and most. Test them by looking for exceptions."],
  ["Hedging", "Using could, may, likely and tends to, because economic outcomes are uncertain."],
] });
labM();
