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

function popChart(s) {
  const x0 = 80, k = 6, bh = 54; let o = "";
  const row = (y, v, parts) => { let x = x0, g = ""; parts.forEach(([n, w, c]) => { g += SV.rect(x, y, w * k, bh, "", { style: `fill:var(${c});stroke:var(--surface);stroke-width:2`, opacity: 0.85 }); g += w * k < 90 ? SV.text(x + (w * k) / 2, y + bh + 18, n.replace("Unemp.", "Unemployed") + " " + w, "lbl bd t2", { "text-anchor": "middle" }) : SV.text(x + (w * k) / 2, y + bh / 2 + 5, n + " " + w, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:15px" }); x += w * k; }); return `<g opacity="${v}">${g}</g>`; };
  o += row(30, clamp(s.n, 0, 1), [["Working-age population", 100, "--accent"]]);
  o += row(120, clamp(s.n - 1, 0, 1), [["Labour force", 67, "--good"], ["Not in labour force", 33, "--muted"]]);
  o += row(210, clamp(s.n - 2, 0, 1), [["Employed", 62, "--n"], ["Unemp.", 5, "--bad"]]);
  const v = clamp(s.n - 3, 0, 1);
  o += `<g opacity="${v}">` + SV.text(380, 318, "Unemployment rate = 5 ÷ 67 × 100 = 7.5%", "lbl bd t2", { "text-anchor": "middle", style: "font-size:18px" }) + SV.text(380, 348, "Not 5 ÷ 100: the rate uses the labour force, not the whole population", "sm", { "text-anchor": "middle" }) + "</g>";
  return o;
}

Lib.stepper($("#stL"), { w: 760, h: 400, label: "Who is in the labour force?", base: { n: 0 }, draw: popChart, steps: [
  { cap: "Start with the <b>working-age population</b>: all the people old enough to work. Here there are 100 (million).", s: { n: 1 } },
  { cap: "Not everyone wants a job. 33 are <b>not in the labour force</b>: students, retired people, full-time carers. The other 67 make up the <b>labour force</b>.", s: { n: 2 } },
  { cap: "The labour force splits into the <b>employed (62)</b> and the <b>unemployed (5)</b>: people without a job who are willing, able and looking for work.", s: { n: 3 } },
  { cap: "Unemployment rate = unemployed ÷ <b>labour force</b> × 100 = 5 ÷ 67 × 100 = <b>7.5%</b>. Students and retired people are not counted.", s: { n: 4 } },
] });

/* Lab 1: labour force calculator */
function labL() {
  if (!$("#la") || !$("#lb") || !$("#lc")) return;
  const e = +$("#la").value, u = +$("#lb").value, o = +$("#lc").value, lf = e + u, pop = lf + o;
  $("#la1").textContent = lf + "m"; $("#la2").textContent = lf ? money((u / lf) * 100, 1) + "%" : "0%"; $("#la3").textContent = pop ? money((e / pop) * 100, 1) + "%" : "0%"; $("#la4").textContent = pop ? money((lf / pop) * 100, 1) + "%" : "0%";
  $("#lav").textContent = lf === 0 ? "No labour force." : `Labour force = ${e} + ${u} = ${lf}m. Unemployment rate = ${u} ÷ ${lf} × 100 = ${money((u / lf) * 100, 1)}%. The ${o}m outside the labour force are not counted as unemployed. Move that slider: the unemployment rate does not change, but the participation rate does.`;
  const x0 = 70, k = 600 / Math.max(1, pop); let g = SV.text(70, 30, "Working-age population: " + pop + "m", "sm"), x = x0;
  [["Employed", e, "--n"], ["Unemployed", u, "--bad"], ["Not in labour force", o, "--muted"]].forEach(([n, v, c]) => { if (v > 0) g += SV.rect(x, 60, v * k, 70, "", { style: `fill:var(${c});stroke:var(--surface);stroke-width:2`, opacity: 0.85 }) + SV.text(x + (v * k) / 2, 100, v * k > 70 ? n + " " + v : v, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:13px" }); x += v * k; });
  g += SV.rect(x0, 160, (e + u) * k, 14, "", { style: "fill:var(--good)", opacity: 0.7 }) + SV.text(x0, 195, "Labour force " + lf + "m", "sm");
  $("#labL").innerHTML = g;
}
Lib.slider($("#g1"), { id: "la", label: "Employed (millions)", min: 10, max: 80, step: 1, value: 62, fmt: (v) => v + "m", onInput: labL });
Lib.slider($("#g2"), { id: "lb", label: "Unemployed (millions)", min: 0, max: 30, step: 1, value: 5, fmt: (v) => v + "m", onInput: labL });
Lib.slider($("#g3"), { id: "lc", label: "Not in the labour force (millions)", min: 0, max: 60, step: 1, value: 33, fmt: (v) => v + "m", onInput: labL });
const CS = [
  { n: "Full-time student", a: "Not in the labour force", w: "Not looking for work, so not unemployed." },
  { n: "Retired person", a: "Not in the labour force", w: "Not looking for work." },
  { n: "Teacher in a paid job", a: "Employed", w: "In paid work." },
  { n: "Factory worker laid off and applying for jobs", a: "Unemployed", w: "Without a job, willing, able and looking." },
  { n: "Parent caring for children full time, not looking for work", a: "Not in the labour force", w: "Not looking for paid work." },
  { n: "Part-time worker who wants full-time hours", a: "Employed (underemployed)", w: "In paid work, so counted as employed, but underemployed." },
  { n: "Worker who gave up looking after months of rejections", a: "Not counted (hidden unemployed)", w: "Official figures miss them, but they would work if jobs were available." },
  { n: "School leaver searching for first job", a: "Unemployed", w: "Willing, able and looking, but never had a job." },
];
button_table("csBtns", "csOut", CS, 0, (p) => `<div class="tw"><table class="t"><tr><th>Counted as</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each person <b>employed</b>, <b>unemployed</b> or <b>not in the labour force</b>?", buckets: [{ label: "Employed" }, { label: "Unemployed" }, { label: "Not in labour force" }], items: [
  { text: "A bus driver", b: 0 }, { text: "A self-employed plumber", b: 0 }, { text: "An office worker made redundant and applying for jobs", b: 1 }, { text: "A graduate looking for a first job", b: 1 },
  { text: "A full-time university student", b: 2 }, { text: "A retired person", b: 2 }, { text: "A full-time carer not looking for paid work", b: 2 }, { text: "A shop assistant working part time", b: 0 },
], done: "Unemployed = without a job and looking. Others outside the labour force are not counted." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Employment", "Being in paid work"],
  ["Unemployment", "Being willing and able to work, and looking, but unable to find a job"],
  ["Labour force", "People who are employed plus those who are unemployed"],
  ["Full employment", "Everyone willing and able to work has a job; only a little frictional unemployment remains"],
  ["Participation rate", "Labour force as a percentage of the working-age population"],
  ["Hidden unemployment", "People who would work but have stopped looking, so are not counted"],
], done: "Good vocabulary scores marks." });
Lib.calc($("#c1"), { qs: [
  { q: "A country has 40 million employed and 2 million unemployed. What is the labour force (millions)?", a: 42, sol: "40 + 2 = <b>42 million</b>." },
  { q: "There are 3 million unemployed in a labour force of 30 million. What is the unemployment rate (%)?", a: 10, sol: "3 ÷ 30 × 100 = <b>10%</b>." },
  { q: "The working-age population is 50 million and the labour force is 35 million. What is the participation rate (%)?", a: 70, sol: "35 ÷ 50 × 100 = <b>70%</b>." },
  { q: "A country has 60 million employed, 4 million unemployed and 26 million not in the labour force. What is the unemployment rate (%, 1 d.p.)?", a: 6.3, tol: 0.1, sol: "4 ÷ 64 × 100 = <b>6.3%</b> (students and others not in the labour force are left out)." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Who is counted as unemployed?", opts: ["Anyone without a job", "Someone without a job who is willing, able and looking for work", "A full-time student", "A retired person"], a: 1, why: "Unemployed people are actively seeking work." },
  { q: "What is the labour force?", opts: ["Everyone in the country", "The employed plus the unemployed", "Only people in full-time jobs", "Everyone of working age"], a: 1, why: "It is those in work or looking for it." },
  { q: "Which statement about full employment is correct?", opts: ["It means zero unemployment", "It means only a small amount of (frictional) unemployment", "It means everyone works full time", "It means high inflation"], a: 1, why: "There are always some people between jobs." },
  { q: "A full-time student is:", opts: ["Unemployed", "Employed", "Not in the labour force", "Hidden unemployed"], a: 2, why: "Students are not looking for work." },
  { q: "What is hidden unemployment?", opts: ["People who have retired", "People who would work but have stopped looking", "Workers in the informal economy", "People who are employed part time"], a: 1, why: "They are not counted in official figures." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Employment", "Being in paid work."],
  ["Unemployment", "Being without a job while willing, able and looking for work."],
  ["Labour force", "The employed plus the unemployed."],
  ["Full employment", "Everyone willing and able to work has a job; only a small amount of frictional unemployment."],
  ["Working-age population", "People old enough to work."],
  ["Participation rate", "The labour force as a percentage of the working-age population."],
  ["Underemployment", "Working fewer hours than wanted or in a job below one's skills."],
  ["Hidden unemployment", "People who would work but have stopped looking, so are not counted."],
  ["Not in the labour force", "People not working and not looking, such as students, retirees and carers."],
] });
labL(); 
