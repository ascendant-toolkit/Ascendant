const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const QX = (q) => 80 + 6 * q, PY = (p) => 360 - 2.7 * p;
function seg(m, c) { // clip P = mQ + c to 0<=Q<=100, 0<=P<=120
  let lo = 0, hi = 100;
  if (m !== 0) { const a = (0 - c) / m, z = (120 - c) / m; lo = Math.max(lo, Math.min(a, z)); hi = Math.min(hi, Math.max(a, z)); }
  return [lo, m * lo + c, hi, m * hi + c];
}
function curve(m, c, cls, label, o = {}) {
  const [q1, p1, q2, p2] = seg(m, c);
  if (q2 <= q1) return "";
  let s = SV.line(QX(q1), PY(p1), QX(q2), PY(p2), cls, o.attrs);
  if (label) { const a = { "text-anchor": "start" }; if (o.attrs && o.attrs.opacity !== undefined) a.opacity = o.attrs.opacity; s += SV.text(QX(q2) + (o.dx ?? 6), PY(p2) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), a); }
  return s;
}
function axes(yl = "Price", xl = "Quantity") {
  return SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) +
    SV.text(QX(0) + 6, PY(120) + 6, yl, "sm") + SV.text(QX(104), PY(0) + 22, xl, "sm", { "text-anchor": "end" });
}
const hline = (p, c = "gr", x2 = 100) => SV.line(QX(0), PY(p), QX(x2), PY(p), c);
const vline = (q, p, c = "gr") => SV.line(QX(q), PY(p), QX(q), PY(0), c);
const ylab = (p, t, c = "sm") => SV.text(QX(0) - 8, PY(p) + 4, t, c, { "text-anchor": "end" });
const xlab = (q, t, c = "sm") => SV.text(QX(q), PY(0) + 18, t, c, { "text-anchor": "middle" });
const money = (v, d = 1) => Lib.fmtN(v, d);
const halo = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
const asP = (y) => (y <= 60 ? 30 + 0.4 * y : 54 + 2.2 * (y - 60));
function solveAD(sh) {
  const c = 90 + 0.8 * sh; let y = (c - 30) / 1.2;
  if (y > 60) y = (c + 78) / 3;
  return [y, asP(y), c];
}
function adLine(c, cls, label, o = {}) {
  const lo = Math.max(0, (c - 108) / 0.8), hi = Math.min(100, (c - 8) / 0.8);
  let r = SV.line(QX(lo), PY(c - 0.8 * lo), QX(hi), PY(c - 0.8 * hi), cls, o.attrs);
  if (label) r += SV.text(QX(hi) + 6, PY(c - 0.8 * hi) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), o.attrs && o.attrs.opacity !== undefined ? { opacity: o.attrs.opacity } : {});
  return r;
}
function adChart(s) {
  const sh = s.sh, [y1, p1, c] = solveAD(sh), moved = Math.abs(sh) >= 1;
  let o = axes("Price level", "Real GDP");
  o += SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: moved ? 0.4 : 1 } });
  if (moved) o += adLine(c, sh > 0 ? "c2" : "c4", sh > 0 ? "AD₁" : "AD₂", { t: sh > 0 ? "t2" : "t4" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: moved ? 0.45 : 1 });
  if (moved) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, sh > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}

function solve2(sh, a) {
  const c = 90 + 0.8 * sh; let y = (c - 30 + 0.4 * a) / 1.2;
  if (y - a > 60) y = (c + 78 + 2.2 * a) / 3;
  return [y, c - 0.8 * y, c];
}
function adasChart(s) {
  const sh = s.sh, a = s.a, [y1, p1, c] = solve2(sh, a), movedAD = Math.abs(sh) >= 1, movedAS = Math.abs(a) >= 1;
  const pts = (x) => [[QX(Math.max(0, x)), PY(x < 0 ? 30 - 0.4 * x : 30)], [QX(60 + x), PY(54)], [QX(87.7 + x), PY(115)]];
  let o = axes("Price level", "Real GDP");
  if (movedAS) o += SV.path(ptsPath(pts(0)), "c3", { opacity: 0.4 });
  o += SV.path(ptsPath(pts(a)), "c3") + SV.text(QX(87.7 + a) + 6, PY(115) + 4, movedAS ? "AS₁" : "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: movedAD ? 0.4 : 1 } });
  if (movedAD) o += adLine(c, "c2", "AD₁", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: movedAD || movedAS ? 0.45 : 1 });
  if (movedAD || movedAS) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
const mkChain = (list, col) => (s) => {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  list.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < list.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
};
const chainSteps = (caps) => caps.map((c, i) => ({ cap: c, s: { n: i + 1 } }));
function button_table(btnId, outId, data, cols, fn) {
  const show = (i) => {
    $("#" + btnId).innerHTML = data.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
    $$("#" + btnId + " .b").forEach((b) => (b.onclick = () => show(+b.dataset.j)));
    $("#" + outId).innerHTML = fn(data[i]);
  };
  show(0);
}

const bar = (x, y, k, parts) => parts.map(([v, c]) => { const w = v * k, g = SV.rect(x, y, w, 46, "", { style: `fill:var(${c});stroke:var(--surface);stroke-width:2`, opacity: 0.85 }) + (w >= 26 ? SV.text(x + w / 2, y + 29, v, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:15px" }) : ""); x += w; return g; }).join("");
const legend = (y, list) => list.map(([n, c], i) => { const x = 150 + i * 190; return SV.rect(x, y - 12, 14, 14, "", { style: `fill:var(${c})` }) + SV.text(x + 22, y, n, "sm"); }).join("");
function sectorChart(s) {
  let o = legend(30, [["Primary", "--good"], ["Secondary", "--accent"], ["Tertiary", "--n"]]);
  [["Early stage", 60, 15, 25], ["Industrialising", 30, 35, 35], ["Developed", 5, 20, 75]].forEach(([n, p, q, t], i) => {
    const v = clamp(s.n - i, 0, 1), y = 60 + i * 76;
    o += `<g opacity="${v}">` + SV.text(138, y + 29, n, "lbl bd", { "text-anchor": "end", style: "font-size:14px" }) + bar(150, y, 5.8, [[p, "--good"], [q, "--accent"], [t, "--n"]]) + "</g>";
  });
  return o + SV.text(380, 300, "Share of workers in each sector (%), illustrative figures", "sm", { "text-anchor": "middle" });
}
function levelChart(s) {
  let o = legend(30, [["Employed", "--n"], ["Unemployed", "--bad"]]);
  [["Year 1", 46, 4, "8.0%"], ["Year 2", 49, 6, "10.9%"], ["Year 3", 49, 3, "5.8%"]].forEach(([n, e, u, r], i) => {
    const v = clamp(s.n - i, 0, 1), y = 60 + i * 76;
    o += `<g opacity="${v}">` + SV.text(98, y + 29, n, "lbl bd", { "text-anchor": "end", style: "font-size:14px" }) + bar(110, y, 9.4, [[e, "--n"], [u, "--bad"]]) + SV.text(670, y + 29, "rate " + r, "sm bd") + "</g>";
  });
  return o + SV.text(380, 300, "Millions of people. The labour force is the whole bar.", "sm", { "text-anchor": "middle" });
}

Lib.stepper($("#stS"), { w: 760, h: 320, label: "How employment moves between sectors", base: { n: 0 }, draw: sectorChart, steps: [
  { cap: "In an <b>early stage</b> of development many people may work in the <b>primary</b> sector: farming, fishing and mining.", s: { n: 1 } },
  { cap: "As the economy <b>industrialises</b>, more workers tend to move into the <b>secondary</b> sector: manufacturing and construction.", s: { n: 2 } },
  { cap: "In a <b>developed</b> economy most workers are likely to be in the <b>tertiary</b> sector: services such as health, banking and tourism.", s: { n: 3 } },
] });
Lib.stepper($("#stE"), { w: 760, h: 320, label: "Employment and unemployment over three years", base: { n: 0 }, draw: levelChart, steps: [
  { cap: "<b>Year 1:</b> 46 million employed and 4 million unemployed. Labour force 50 million.", s: { n: 1 } },
  { cap: "<b>Year 2:</b> employment rises by 3 million, but the labour force rises by 5 million. <b>Employment and unemployment both rise.</b>", s: { n: 2 } },
  { cap: "<b>Year 3:</b> employment stays at 49 million, but 3 million people leave the labour force. <b>Unemployment falls with no new jobs.</b>", s: { n: 3 } },
] });
const FLEX = ["Global competition increases", "Firms need to respond quickly to demand", "They change numbers, hours, tasks, places or pay", "Firms may hire more readily", "Workers may feel less secure"];
Lib.stepper($("#stF"), { w: 760, h: 320, label: "Why firms want flexible workers", base: { n: 0 }, draw: mkChain(FLEX, "--accent"), steps: chainSteps(["Competition from firms at home and abroad puts pressure on costs.", "Demand may change suddenly.", "This is a <b>flexible labour force</b>: one that adjusts quickly and smoothly.", "If workers can be let go when demand falls, firms may be more willing to take them on when it rises.", "<b>Evaluate:</b> the gain to firms may come at a cost to job security."]) });

function labE() {
  if (!$("#ej") || !$("#el")) return;
  const dj = +$("#ej").value, dl = +$("#el").value, e = 44 + dj, lf = 50 + dl, u = lf - e;
  $("#ea1").textContent = e + "m"; $("#ea2").textContent = u + "m"; $("#ea3").textContent = lf + "m"; $("#ea4").textContent = money((u / lf) * 100, 1) + "%";
  const word = (d) => (d > 0 ? "rises by " + d + "m" : d < 0 ? "falls by " + -d + "m" : "is unchanged");
  $("#eav").textContent = `Start: 44m employed, 6m unemployed. Now employment ${word(dj)} and unemployment ${word(u - 6)}.`;
}
const sign = (v) => (v > 0 ? "+" : "") + v + "m";
Lib.slider($("#g1"), { id: "ej", label: "Change in number employed", min: -3, max: 3, step: 1, value: 2, fmt: sign, onInput: labE });
Lib.slider($("#g2"), { id: "el", label: "Change in labour force", min: -3, max: 6, step: 1, value: 4, fmt: sign, onInput: labE });
function labP() {
  if (!$("#pw") || !$("#pr")) return;
  const w = +$("#pw").value, r = +$("#pr").value, lf = (w * r) / 100;
  $("#pa1").textContent = money(lf, 1) + "m"; $("#pa2").textContent = money(w - lf, 1) + "m";
  $("#pav").textContent = `Labour force = ${w}m × ${r}% = ${money(lf, 1)}m. Starting from 80m and 65% (52m), the labour force has changed by ${money(lf - 52, 1)}m.`;
}
Lib.slider($("#g3"), { id: "pw", label: "Working-age population", min: 60, max: 100, step: 1, value: 80, fmt: (v) => v + "m", onInput: labP });
Lib.slider($("#g4"), { id: "pr", label: "Participation rate", min: 40, max: 85, step: 1, value: 65, fmt: (v) => v + "%", onInput: labP });
labE(); labP();
const FA = [
  { n: "Higher wages", a: "Participation likely to rise", w: "Work becomes more rewarding, so more people may look for jobs or retire later." },
  { n: "Wider acceptance of women working", a: "Participation likely to rise", w: "More women may enter the labour force." },
  { n: "More nursery and elderly care places", a: "Participation likely to rise", w: "Carers may be freed to take paid work." },
  { n: "Better access for disabled workers", a: "Participation likely to rise", w: "Ramps, equipment and changed attitudes may let more people work." },
  { n: "More school leavers in higher education", a: "Participation likely to fall at first", w: "Full-time students are outside the labour force, although its quality may rise later." },
  { n: "More early retirement", a: "Participation likely to fall", w: "People of working age leave the labour force." },
  { n: "Net immigration", a: "Working-age population likely to rise", w: "The labour force may grow, especially if many arrivals come to work." },
  { n: "Higher birth rate", a: "Working-age population rises later", w: "There is a long delay before the children are old enough to work." },
  { n: "Lower death rate", a: "Population may rise", w: "The labour force grows mainly if more people of working age survive." },
];
button_table("faBtns", "faOut", FA, 0, (p) => `<div class="tw"><table class="t"><tr><th>Likely effect</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which change in the <b>pattern of employment</b> does each example show?", buckets: [{ label: "Sector of industry" }, { label: "Public or private" }, { label: "Hours or status" }], items: [
  { text: "Farm workers move into factory jobs", b: 0 }, { text: "Call centres and banks hire more staff while mines close", b: 0 }, { text: "A state railway is sold and its staff now work for a company", b: 1 }, { text: "The government recruits more nurses for state hospitals", b: 1 }, { text: "A full-time cashier changes to 15 hours a week", b: 2 }, { text: "An employee leaves a firm to work as a self-employed designer", b: 2 },
], done: "Name the pattern before you explain its cause." });
Lib.classify($("#cl2"), { prompt: "Is each more typical of the <b>formal</b> or the <b>informal</b> economy?", buckets: [{ label: "Formal" }, { label: "Informal" }], items: [
  { text: "A written contract and employment rights", b: 0 }, { text: "A pension scheme", b: 0 }, { text: "Union membership and collective bargaining", b: 0 }, { text: "Pay below the minimum wage may go unchecked", b: 1 }, { text: "Casual cash work with no records", b: 1 }, { text: "Little training and often low productivity", b: 1 },
], done: "Informal workers tend to have less protection." });
Lib.classify($("#cl3"), { prompt: "Other things equal, is the <b>participation rate</b> likely to rise or fall?", buckets: [{ label: "Rise" }, { label: "Fall" }], items: [
  { text: "Free childcare is expanded", b: 0 }, { text: "Wages rise sharply", b: 0 }, { text: "Workplaces become easier for disabled people to use", b: 0 }, { text: "Many more 18-year-olds go to university", b: 1 }, { text: "More workers retire at 55", b: 1 }, { text: "More adults give up paid work to be homemakers", b: 1 },
], done: "Ask whether more or fewer working-age people are working or looking for work." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Pattern of employment", "How workers are spread across sectors, types of employer, hours and kinds of job"],
  ["Informal economy", "Work that is largely unrecorded, with little legal protection"],
  ["High quality employment", "Skilled, secure work with training, progression and good conditions"],
  ["Flexible labour force", "Workers who can adjust quickly to changes in market conditions"],
  ["Participation rate", "The share of the working-age population in the labour force"],
  ["Economically inactive", "People of working age who are outside the labour force"],
], done: "Precise terms earn knowledge marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why unemployment may rise although more jobs are created</b>.", items: [
  "The working-age population grows",
  "The labour force becomes larger",
  "Firms create some extra jobs",
  "The new jobs are fewer than the new jobseekers",
  "Both employment and unemployment rise",
], done: "Compare the growth of jobs with the growth of the labour force." });
Lib.calc($("#c1"), { qs: [
  { q: "The working-age population is 40 million and the labour force is 26 million. What is the participation rate (%)?", a: 65, sol: "26 ÷ 40 × 100 = <b>65%</b>." },
  { q: "The working-age population is 90 million and the participation rate is 70%. How large is the labour force (millions)?", a: 63, sol: "90 × 0.70 = <b>63 million</b>." },
  { q: "The labour force grows by 3 million and the number employed grows by 1 million. By how many million does unemployment change?", a: 2, sol: "3 − 1 = <b>2 million more</b> unemployed." },
  { q: "Of 25 million employed people, 4 million work for the government. What percentage work in the private sector?", a: 84, sol: "(25 − 4) ÷ 25 × 100 = <b>84%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "As an economy develops, employment usually moves:", opts: ["From tertiary to primary", "From primary to secondary and then tertiary", "From secondary to primary", "Only into the public sector"], a: 1, why: "Services tend to take a growing share." },
  { q: "When could employment and unemployment both rise?", opts: ["When the labour force grows faster than the number of jobs", "When the labour force shrinks", "Never", "When every new job goes to an unemployed person and nobody joins the labour force"], a: 0, why: "Some of the extra jobseekers find no work." },
  { q: "Which person is economically inactive?", opts: ["A jobseeker", "A part-time worker", "A full-time student not looking for work", "A self-employed farmer"], a: 2, why: "They are outside the labour force." },
  { q: "Which is a likely feature of informal employment?", opts: ["Strong union protection", "A company pension", "Little job protection", "Regular formal training"], a: 2, why: "Informal work is largely outside legal protection." },
  { q: "A shift towards privatisation is likely to:", opts: ["Raise the share of workers in the private sector", "Raise the share in the public sector", "Remove all unemployment", "Shrink the working-age population"], a: 0, why: "Jobs move from state to private employers." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Industrial structure", "How output and employment are divided between the primary, secondary and tertiary sectors."],
  ["Public sector", "Organisations owned or run by the government."],
  ["Private sector", "Businesses owned and run by private individuals and firms."],
  ["Self-employed", "People who work for themselves."],
  ["Informal economy", "Largely unrecorded work with little legal protection."],
  ["Formal economy", "Recorded work covered by laws, taxes and employment rights."],
  ["High quality employment", "Skilled, secure work with training, progression and good conditions."],
  ["Low quality employment", "Unskilled work with little training and poor conditions."],
  ["Flexible labour force", "A labour force that adjusts quickly and smoothly to changes in market conditions."],
  ["Participation rate", "The labour force as a percentage of the working-age population."],
  ["Economically active", "Those in the labour force, employed or unemployed."],
  ["Economically inactive", "Those of working age outside the labour force."],
] });
