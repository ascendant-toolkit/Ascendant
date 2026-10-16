"""Builds the five IGCSE Economics 4.6 Employment and unemployment reviews (4.6.1 to 4.6.5), written from scratch.
Run: python3 tools/artifact-kit/mk_ig46.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

PPC = '''
function ppcChart(s) {
  const ox = 90, oy = 330, X = 250 * s.s, Y = 215 * s.s;
  const curve = (X, Y) => { const p = []; for (let t = 0; t <= 90; t += 5) { const r = (t * Math.PI) / 180; p.push([ox + X * Math.cos(r), oy - Y * Math.sin(r)]); } return p; };
  let o = SV.line(ox, oy, ox, 30) + SV.line(ox, oy, 700, oy) + SV.text(ox + 6, 40, "Capital goods", "sm") + SV.text(700, oy + 24, "Consumer goods", "sm", { "text-anchor": "end" });
  o += SV.path(ptsPath(curve(X, Y)), "c1") + SV.text(ox + X * 0.7071 + 12, oy - Y * 0.7071 - 6, "PPC", "lbl bd t1");
  const k = s.in, f = 1 - 0.3 * (1 - k), px = ox + X * 0.7071 * f, py = oy - Y * 0.7071 * f;
  o += SV.line(px, py, px, oy, "gr") + SV.line(ox, py, px, py, "gr") + SV.circle(px, py, 7, k > 0.5 ? "dot1" : "dot2");
  if (s.t) o += SV.text(px + 14, py + 24, s.t, "lbl bd t2", { style: halo });
  return o;
}
'''
LF = '''
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
'''

# =========================================================== 4.6.1 Definitions
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Employment</span> means being in paid work. A person is <span class="kw">unemployed</span> if they are <b>willing and able to work, are actively looking, but cannot find a job</b>. <span class="kw">Full employment</span> is when everyone who is willing and able to work has a job (in practice, only a small amount of unemployment remains). Employment and unemployment are central to the government's aim of <b>full employment (low unemployment)</b>.</p></div>

  <h2>Who is who?</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Employed</b></td><td>In paid work (full or part time, employee or self-employed)</td><td>A teacher, a taxi driver, a farmer selling crops</td></tr>
    <tr><td><b>Unemployed</b></td><td>Without a job, willing and able to work and looking for one</td><td>A factory worker laid off who is applying for jobs</td></tr>
    <tr><td><b>Labour force</b></td><td>Employed + unemployed</td><td>Everyone who is working or looking for work</td></tr>
    <tr><td><b>Not in the labour force</b></td><td>Not working and not looking, for example full-time students, retired people, full-time carers</td><td>A university student, a pensioner</td></tr>
  </table></div>
  <p>The <b>working-age population</b> is everyone old enough to work. Some of them are outside the labour force, so they are <b>not</b> counted as unemployed.</p>

  <h2>Full employment does not mean zero unemployment</h2>
  <p>Even when the economy is doing well, some people are always between jobs or changing careers. So full employment means that <b>only frictional unemployment</b> remains (a few per cent), and any other jobseeker could find a job. A government aiming for full employment is aiming for <b>low unemployment</b>, not zero.</p>

  <h2>Other terms</h2>
  <div class="grid2">
    <div class="card"><h3>Participation rate</h3><p>The labour force as a percentage of the working-age population. A fall may mean people have become discouraged, or are in education.</p></div>
    <div class="card"><h3>Underemployment and hidden unemployment</h3><p>Underemployed: working fewer hours than they would like or in jobs below their skills. Hidden unemployed: would work but have stopped looking, so they are not counted.</p></div>
  </div>
  <p class="note">Why it matters: a high employment level raises output, incomes and tax revenue; unemployment wastes resources. See 4.6.4 for the consequences.</p>
'''
js = HEAD + COMMON + LF + '''
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
''' + calc_js([
    ("A country has 40 million employed and 2 million unemployed. What is the labour force (millions)?", 42, "40 + 2 = <b>42 million</b>.", None, None),
    ("There are 3 million unemployed in a labour force of 30 million. What is the unemployment rate (%)?", 10, "3 ÷ 30 × 100 = <b>10%</b>.", None, None),
    ("The working-age population is 50 million and the labour force is 35 million. What is the participation rate (%)?", 70, "35 ÷ 50 × 100 = <b>70%</b>.", None, None),
    ("A country has 60 million employed, 4 million unemployed and 26 million not in the labour force. What is the unemployment rate (%, 1 d.p.)?", 6.3, "4 ÷ 64 × 100 = <b>6.3%</b> (students and others not in the labour force are left out).", None, 0.1),
]) + mcq_js("qz1", [
    ("Who is counted as unemployed?", ["Anyone without a job", "Someone without a job who is willing, able and looking for work", "A full-time student", "A retired person"], 1, "Unemployed people are actively seeking work."),
    ("What is the labour force?", ["Everyone in the country", "The employed plus the unemployed", "Only people in full-time jobs", "Everyone of working age"], 1, "It is those in work or looking for it."),
    ("Which statement about full employment is correct?", ["It means zero unemployment", "It means only a small amount of (frictional) unemployment", "It means everyone works full time", "It means high inflation"], 1, "There are always some people between jobs."),
    ("A full-time student is:", ["Unemployed", "Employed", "Not in the labour force", "Hidden unemployed"], 2, "Students are not looking for work."),
    ("What is hidden unemployment?", ["People who have retired", "People who would work but have stopped looking", "Workers in the informal economy", "People who are employed part time"], 1, "They are not counted in official figures."),
]) + "\n" + cards_js([("Employment", "Being in paid work."), ("Unemployment", "Being without a job while willing, able and looking for work."), ("Labour force", "The employed plus the unemployed."), ("Full employment", "Everyone willing and able to work has a job; only a small amount of frictional unemployment."), ("Working-age population", "People old enough to work."), ("Participation rate", "The labour force as a percentage of the working-age population."), ("Underemployment", "Working fewer hours than wanted or in a job below one's skills."), ("Hidden unemployment", "People who would work but have stopped looking, so are not counted."), ("Not in the labour force", "People not working and not looking, such as students, retirees and carers.")]) + "labL(); showCS0();\n".replace("showCS0();", "")
explore = '''
  <h2>Lab 1 · Labour force calculator</h2>
  <p>Set the number of people employed, unemployed and outside the labour force (millions). Notice what changes the unemployment rate and what does not.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Labour force</small><strong id="la1"></strong></div><div><small>Unemployment rate</small><strong id="la2"></strong></div><div><small>Employment rate</small><strong id="la3"></strong></div><div><small>Participation rate</small><strong id="la4"></strong></div></div><div class="verdict" id="lav"></div></div></div>
    <svg id="labL" viewBox="0 0 760 220" role="img" aria-label="Employed, unemployed and not in the labour force"></svg>
  </div>

  <h2>Lab 2 · How is this person counted?</h2>
  <p>Pick a person to see how official figures treat them.</p>
  <div class="card"><div class="row" id="csBtns"></div><div id="csOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "What is meant by unemployment?", "Two ideas: without a job, and willing and able to work (and looking).",
      "[K|Unemployment is when people are without a job] [K|although they are willing and able to work and are looking for work.]", warn="Saying 'people who do not work'. Students and retired people are not unemployed."),
    Q(2, "Define", 2, "What is meant by full employment?", "Everyone willing and able has a job; some frictional unemployment remains.",
      "[K|Full employment is when everyone who is willing and able to work has a job,] [K|so only a small amount of frictional unemployment remains.]"),
    Q(3, "Explain", 4, "Explain why a full-time student is not counted as unemployed.", "Say what unemployed means, then apply it.",
      "[K|People are only counted as unemployed if they are willing and able to work and are looking for a job.] [N|A full-time student is not looking for paid work, so is outside the labour force.] [A|If they started to apply for jobs full time they would be counted as unemployed.]"),
    Q(4, "Explain", 4, "Explain why full employment does not mean zero unemployment.", "Frictional: people between jobs. Also people changing industry or seasons.",
      "[K|Even in a strong economy some people are between jobs.] [N|Workers who leave one job take time to find another, and new entrants to the labour force need time to search, so there is always some frictional unemployment.] [N|Full employment therefore means that anyone willing and able to work could find a job in a reasonable time, not that unemployment is zero.]"),
)
tp = tips([
    ("Unemployed means looking for work.", "Students, retirees and carers are outside the labour force."),
    ("Labour force = employed + unemployed.", "Use it in the denominator of the rate."),
    ("Full employment is not zero unemployment.", "Frictional unemployment always exists."),
    ("Say willing, able and looking.", "Three words that earn definition marks."),
], cmds("Define", "Explain"))
body = page(CL("4.6.1 Definitions of employment, unemployment and full employment"), "Employment, Unemployment and Full Employment", "What employment and unemployment mean, who is in the labour force, and what full employment is. Syllabus 4.6.1.",
    learn=learn, watch=watch(("Who is in the labour force?", "stL")), explore=explore,
    practise=practise(("Employed, unemployed or neither?", "cl1", "card"), ("Match the term", "m1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Low unemployment in Japan", "Japan has had a low unemployment rate for years (around 2 to 3%), a level many economists would call full employment, even though some people are always between jobs.", "Full employment does not mean zero unemployment."),
        rw("Falling participation", "In several rich countries many older people retired early or left the labour force during COVID-19. The unemployment rate fell even though total employment was lower.", "Why unemployment rate and employment can move in different directions."),
        rw("Discouraged workers", "In countries with long spells of high unemployment, some jobseekers stop looking. They are no longer counted as unemployed, so official unemployment understates the real problem.", "Hidden unemployment and a limit on the official figure.")),
    exam=ex, tips=tp)
write("em1", body, js, "Employment, Unemployment and Full Employment", "ig-unemployment-definitions")

# =========================================================== 4.6.2 Measurement
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Unemployment is measured in two main ways: the <span class="kw">Labour Force Survey (LFS)</span> and the <span class="kw">claimant count</span>. The key statistic is the <span class="kw">unemployment rate</span>: the number of unemployed as a percentage of the labour force. Each method has strengths and weaknesses, so official figures may not tell the whole story.</p></div>

  <h2>The unemployment rate</h2>
  <div class="formula">Unemployment rate = (number unemployed ÷ labour force) × 100</div>
  <p><b>Worked example (Australia, 2021):</b> 0.56 million unemployed in a labour force of 14.0 million. 0.56 ÷ 14.0 × 100 = <b>4%</b>. The rate is a percentage of the <b>labour force</b>, not of the whole population.</p>

  <h2>Two ways to measure</h2>
  <div class="grid2">
    <div class="card"><h3>Labour Force Survey</h3>
      <p>A sample of households is asked questions: do you have a job? Have you looked for work in the last few weeks? Are you available to start? Those who say yes to the last two but have no job count as unemployed. It follows an international (ILO) definition.</p>
      <ul><li><b>For:</b> includes everyone looking for work, whether or not they claim benefit; allows comparison between countries.</li><li><b>Against:</b> based on a sample, so there are errors; costly; people may not answer truthfully.</li></ul></div>
    <div class="card"><h3>Claimant count</h3>
      <p>Counts the people who are claiming unemployment benefit.</p>
      <ul><li><b>For:</b> quick and cheap, from administrative records.</li><li><b>Against:</b> misses people who are unemployed but not entitled to or not claiming benefit; includes some who are working and still claim; changes in benefit rules change the figures.</li></ul></div>
  </div>

  <h2>Why the figure may be wrong</h2>
  <ul>
    <li><b>Hidden unemployment:</b> discouraged workers who have stopped looking are not counted.</li>
    <li><b>Underemployment:</b> part-time workers who want full-time hours are counted as employed.</li>
    <li><b>Informal economy:</b> unrecorded work, and sometimes people claiming benefit while working.</li>
    <li><b>Definitions and sample errors</b> differ between countries.</li>
  </ul>
  <p class="note">Interpreting a change: if the unemployment rate falls, it could be because more people found jobs, or because people left the labour force.</p>
'''
js = HEAD + COMMON + '''
function rateChart(s) {
  const base = 330, k = 17, w = 160; let o = SV.line(60, base, 700, base);
  const L = s.l, U = s.u, h = L * k, hu = Math.max(U * k, 4);
  o += SV.rect(130, base - h, w, h - hu, "", { style: "fill:var(--good)", opacity: 0.8 }) + SV.rect(130, base - hu, w, hu, "", { style: "fill:var(--bad)", opacity: 0.9 });
  o += SV.text(130 + w / 2, base - h - 10, "Labour force " + money(L, 1) + "m", "lbl bd", { "text-anchor": "middle" });
  if (s.show) o += SV.text(130 + w + 14, base - hu / 2 + 4, "Unemployed " + money(U, 2) + "m", "lbl bd t2");
  if (s.f) o += SV.text(380, 60, "Unemployment rate = " + money(U, 2) + " ÷ " + money(L, 1) + " × 100 = " + money((U / L) * 100, 1) + "%", "lbl bd t3", { style: "font-size:18px" });
  return o;
}
Lib.stepper($("#stR"), { w: 760, h: 400, label: "Calculating the unemployment rate", base: { l: 14, u: 0.56, show: 0, f: 0 }, draw: rateChart, steps: [
  { cap: "Australia's <b>labour force</b> in 2021 was <b>14.0 million</b>: everyone in work or looking for work.", s: { l: 14, u: 0.56, show: 0, f: 0 } },
  { cap: "Of these, <b>0.56 million</b> had no job but were willing, able and looking: the <b>unemployed</b>.", s: { l: 14, u: 0.56, show: 1, f: 0 } },
  { cap: "<b>Unemployment rate = 0.56 ÷ 14.0 × 100 = 4%</b>.", s: { l: 14, u: 0.56, show: 1, f: 1 } },
  { cap: "The 2026 forecast: labour force <b>14.8m</b>, unemployed <b>0.62m</b>. The rate is about <b>4.2%</b>: slightly higher, even though the labour force grew.", s: { l: 14.8, u: 0.62, show: 1, f: 1 } },
] });
function methodChart(s) {
  const base = 330, k = 260, bars = [["Labour Force Survey", 0.56, "--accent", clamp(s.n, 0, 1)], ["Claimant count", 0.4, "--warn", clamp(s.n - 1, 0, 1)]]; let o = SV.line(60, base, 700, base);
  bars.forEach(([n, v, c, op], i) => { if (op <= 0) return; const x = 150 + i * 250, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, money(v, 2) + "m", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }) + "</g>"; });
  if (s.n > 2) o += SV.text(380, 40, "The gap: unemployed people not claiming benefit", "lbl bd t2", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 400, label: "Two measures of unemployment", base: { n: 0 }, draw: methodChart, steps: [
  { cap: "The <b>Labour Force Survey</b> asks a sample of households about work and job search. It estimates <b>0.56 million</b> unemployed.", s: { n: 1 } },
  { cap: "The <b>claimant count</b> only counts people claiming unemployment benefit: <b>0.40 million</b>.", s: { n: 2 } },
  { cap: "The claimant count is lower because some unemployed people <b>are not eligible or do not claim</b> (for example young people or partners of earners). Some claimants may also be working. The LFS is usually the better measure.", s: { n: 3 } },
] });

/* Lab 1: discouraged workers */
function labD() {
  if (!$("#da") || !$("#db") || !$("#dc")) return;
  const L = +$("#da").value, U = +$("#db").value, d = +$("#dc").value, Ud = Math.max(0, U - d), Ld = L - d, r0 = (U / L) * 100, r1 = (Ud / Ld) * 100;
  $("#da1").textContent = money(r0, 1) + "%"; $("#da2").textContent = money(r1, 1) + "%"; $("#da3").textContent = money(d, 2) + "m";
  $("#dav").textContent = d === 0 ? `Unemployment rate = ${money(U, 2)} ÷ ${money(L, 1)} × 100 = ${money(r0, 1)}%. Now slide the discouraged workers up.` : `If ${money(d, 2)}m unemployed people give up looking, they leave the labour force. The official rate falls from ${money(r0, 1)}% to ${money(r1, 1)}% even though not one new job has been created. This is hidden unemployment.`;
  const base = 300, k = 14; let o = SV.line(60, base, 700, base);
  [["Rate if they keep looking", r0, "--bad"], ["Official rate", r1, "--accent"]].forEach(([n, v, c], i) => { const x = 160 + i * 260, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, money(v, 1) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g1"), { id: "da", label: "Labour force (millions)", min: 10, max: 20, step: 0.5, value: 14, fmt: (v) => v + "m", onInput: labD });
Lib.slider($("#g2"), { id: "db", label: "Unemployed (millions)", min: 0.2, max: 2, step: 0.02, value: 0.8, fmt: (v) => v.toFixed(2) + "m", onInput: labD });
Lib.slider($("#g3"), { id: "dc", label: "Unemployed who give up looking (millions)", min: 0, max: 0.4, step: 0.02, value: 0, fmt: (v) => v.toFixed(2) + "m", onInput: labD });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a feature of the <b>Labour Force Survey</b> or the <b>claimant count</b>?", buckets: [{ label: "Labour Force Survey" }, { label: "Claimant count" }], items: [
  { text: "Asks a sample of households about work and job search", b: 0 }, { text: "Follows an international (ILO) definition", b: 0 }, { text: "Includes unemployed people who do not claim benefit", b: 0 }, { text: "Based on a sample, so there are sampling errors", b: 0 },
  { text: "Counts people claiming unemployment benefit", b: 1 }, { text: "Cheap and quick, from official records", b: 1 }, { text: "Misses unemployed people who are not eligible", b: 1 }, { text: "Changes when benefit rules change", b: 1 },
], done: "Know both measures and a for/against of each." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Unemployment rate", "Number unemployed as a percentage of the labour force"],
  ["Labour Force Survey", "A household survey of people's work and job search"],
  ["Claimant count", "The number of people claiming unemployment benefit"],
  ["Hidden unemployment", "People who would work but have stopped looking"],
  ["Underemployment", "Working fewer hours than wanted or in a job below one's skills"],
  ["Discouraged worker", "A jobseeker who has given up looking after failing to find work"],
], done: "Good vocabulary scores marks." });
''' + calc_js([
    ("0.56 million are unemployed in a labour force of 14.0 million. Calculate the unemployment rate (%). (Australia, past paper)", 4, "0.56 ÷ 14 × 100 = <b>4%</b>.", None, None),
    ("A country has 2.4 million unemployed and a labour force of 20 million. What is the unemployment rate (%)?", 12, "2.4 ÷ 20 × 100 = <b>12%</b>.", None, None),
    ("The unemployment rate is 8% and the labour force is 25 million. How many people are unemployed (millions)?", 2, "8% × 25m = <b>2 million</b>.", None, None),
    ("Unemployment rises from 1.0 million to 1.2 million in a labour force of 20 million. By how many percentage points does the unemployment rate rise?", 1, "From 5% to 6%: <b>1 percentage point</b>.", None, None),
    ("The unemployment rate is 24% in a labour force of 10 million. How many are unemployed (millions)?", 2.4, "24% × 10m = <b>2.4 million</b>.", None, None),
]) + mcq_js("qz1", [
    ("Unemployment rate is calculated as:", ["Unemployed ÷ population × 100", "Unemployed ÷ labour force × 100", "Employed ÷ labour force × 100", "Unemployed ÷ employed × 100"], 1, "The denominator is the labour force."),
    ("Which method counts only people receiving benefit?", ["Labour Force Survey", "Claimant count", "Census", "Household budget"], 1, "The claimant count uses benefit records."),
    ("Which is a limitation of the claimant count?", ["It misses unemployed people not claiming benefit", "It uses a sample", "It follows ILO rules", "It counts students"], 0, "Not everyone unemployed claims."),
    ("The unemployment rate falls because discouraged workers leave the labour force. This is an example of:", ["Falling hidden unemployment", "Hidden unemployment hiding the true level", "Full employment", "Cyclical unemployment"], 1, "The figure falls without more jobs."),
    ("Which statement is correct?", ["The Labour Force Survey is based on a sample of households", "The claimant count is based on a sample", "Both count students", "Neither uses a definition"], 0, "The LFS surveys a sample."),
]) + "\n" + cards_js([("Unemployment rate", "The number of unemployed as a percentage of the labour force."), ("Labour Force Survey", "A survey of households that measures employment and unemployment using an international definition."), ("Claimant count", "The number of people claiming unemployment benefit."), ("Labour force", "The employed plus the unemployed."), ("Hidden unemployment", "People who would work but have stopped looking, so are not counted."), ("Discouraged worker", "A jobseeker who has given up looking for work."), ("Underemployment", "Working fewer hours than wanted or in a job below one's skills."), ("ILO", "The International Labour Organization, which defines unemployment for international comparison.")]) + "labD();\n"
explore = '''
  <h2>Lab 1 · Does a falling rate mean more jobs?</h2>
  <p>Set the labour force and the number unemployed, then let some unemployed people give up looking. Watch what happens to the official rate.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Rate if they keep looking</small><strong id="da1"></strong></div><div><small>Official rate</small><strong id="da2"></strong></div><div><small>Hidden unemployed</small><strong id="da3"></strong></div></div><div class="verdict" id="dav"></div></div></div>
    <svg id="labD" viewBox="0 0 760 340" role="img" aria-label="Unemployment rate with and without discouraged workers"></svg>
  </div>
'''
ex = exam(
    Q(1, "Identify", 2, "Identify two ways unemployment is measured. (Oct/Nov 2021, P23; Oct/Nov 2024, P21)", "Name both: claimant count and labour force survey.", "[K|The claimant count (number claiming unemployment benefit).] [K|The labour force survey (a survey of people without a job who are looking for work).]"),
    Q(2, "Calculate", 1, "In 2021 Australia had 0.56 million unemployed in a labour force of 14.0 million. Calculate the unemployment rate. (May/June 2023, P21)", "Unemployed ÷ labour force × 100.", "[A|0.56 ÷ 14.0 × 100 = 4%.]"),
    Q(3, "Define", 2, "Define unemployment rate. (Feb/Mar 2024, P22)", "Formula or words: unemployed as a percentage of the labour force.", "[K|The unemployment rate is the number of unemployed] [K|divided by the labour force, multiplied by 100 (the percentage of the labour force without a job).]"),
    Q(4, "Explain", 2, "Explain what is meant by an unemployment rate of 24%. (May/June 2020, P23)", "Use the definition: 24 out of every 100 in the labour force.", "[K|24% of the labour force is without a job] [A|but is willing and able to work, so about 24 out of every 100 people in the labour force are unemployed.]"),
    Q(5, "Explain", 4, "Explain two reasons why official unemployment figures may understate the true level.", "Hidden unemployment, underemployment, claimant count gaps. Each with a link.",
      "[K|Some people become discouraged and stop looking for work.] [N|They are no longer counted as unemployed even though they would work if jobs were available, so the measured rate is lower.] [K|The claimant count misses people who are not eligible for benefit.] [N|Young people or partners of earners may be unemployed without claiming, so the figure could be too low.]"),
)
tp = tips([
    ("Two measures:", "labour force survey and claimant count. Learn one strength and weakness of each."),
    ("Rate = unemployed ÷ labour force × 100.", "Not ÷ population."),
    ("Show working in calculations.", "Even for 1 mark, write the formula."),
    ("A falling rate may not mean more jobs.", "Discouraged workers leave the labour force."),
], cmds("Define", "Identify", "Calculate", "Explain"))
body = page(CL("4.6.2 Measurement of unemployment"), "Measurement of Unemployment", "The Labour Force Survey and the claimant count, the unemployment rate formula, and why the figures can mislead. Syllabus 4.6.2.",
    learn=learn, watch=watch(("Calculating the unemployment rate", "stR"), ("Two measures of unemployment", "stM")), explore=explore,
    practise=practise(("Which measure?", "cl1", "card"), ("Match the term", "m1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Australia's coal table", "A past paper gives Australia's labour force and number of unemployed for 2021 and a 2026 forecast, and asks for the unemployment rate: 4%.", "A one-mark rate calculation."),
        rw("Claimant count changes", "In some countries changes to benefit rules have altered the claimant count even when the number of people looking for work was similar.", "A weakness of the claimant count."),
        rw("Youth unemployment", "In many countries the unemployment rate for young people is double the national rate, and many young people are unemployed without claiming benefit.", "Why the claimant count can understate unemployment.")),
    exam=ex, tips=tp)
write("em2", body, js, "Measurement of Unemployment", "ig-unemployment-measurement")

# =========================================================== 4.6.3 Types
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The syllabus names four types of unemployment: <b>frictional</b>, <b>structural</b>, <b>cyclical</b> and <b>seasonal</b>. They have different causes, so they need different solutions. When you answer, name the type, say what causes it, and give an example.</p></div>

  <h2>The four types</h2>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>What it is</th><th>Causes</th><th>Example</th></tr>
    <tr><td><b>Frictional</b></td><td>Temporary unemployment while changing jobs; short term</td><td>Time to search and apply; lack of information; new entrants to the labour force</td><td>A graduate looking for a first job; someone who has just left a job</td></tr>
    <tr><td><b>Structural</b></td><td>Workers' skills or locations do not match the jobs available; long term</td><td>Decline of an industry; new technology; globalisation; immobility of labour</td><td>Coal miners after pit closures when vacancies are in solar installation or in another city</td></tr>
    <tr><td><b>Cyclical</b></td><td>Not enough demand in the economy; also called demand-deficient</td><td>A recession: firms cut output and jobs</td><td>Car factory workers laid off in a downturn</td></tr>
    <tr><td><b>Seasonal</b></td><td>Jobs depend on the time of year</td><td>Weather, holidays, harvests</td><td>Ski instructors in summer; fruit pickers after the harvest</td></tr>
  </table></div>

  <h2>Telling them apart</h2>
  <div class="grid2">
    <div class="card"><h3>Ask: are there vacancies?</h3><p><b>Yes, but the unemployed cannot fill them</b> (wrong skills or place): structural. <b>Yes, and they will soon fill them</b>: frictional. <b>No, because demand is low</b>: cyclical. <b>Yes, but only at certain times of year</b>: seasonal.</p></div>
    <div class="card"><h3>Ask: how long and why?</h3><p><b>Short:</b> frictional or seasonal. <b>Long:</b> structural. <b>Tied to the business cycle:</b> cyclical.</p></div>
  </div>

  <h2>What causes structural change?</h2>
  <ul>
    <li><b>Decline of an industry:</b> falling demand for coal, steel or textiles.</li>
    <li><b>Technology:</b> machines or software replace some jobs (technological unemployment).</li>
    <li><b>Globalisation:</b> firms move production to countries with lower costs.</li>
    <li><b>Immobility of labour:</b> occupational (skills) and geographical (location) barriers stop workers moving to the jobs.</li>
  </ul>
  <p class="note">Policies depend on the type: demand-side policy for cyclical, supply-side policy for structural and frictional, and diversification for seasonal. See 4.6.5.</p>
'''
js = HEAD + COMMON + '''
Lib.stepper($("#stC"), { w: 760, h: 400, label: "Cyclical unemployment", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b> with most people in work.", s: { sh: 0, a: 0 } },
  { cap: "A recession: confidence falls, so <b>AD shifts left</b>. Firms sell less.", s: { sh: -16, a: 0 } },
  { cap: "Real GDP falls to Y₁. Firms need fewer workers and <b>lay people off</b>: <b>cyclical unemployment</b> rises. There are not enough jobs for everyone who wants one.", s: { sh: -16, a: 0 } },
] });
function strChart(s) {
  const base = 320, k = 3.2; let o = SV.line(60, base, 700, base);
  const bars = [["Jobs lost: declining industry", s.l, "--bad", s.a], ["Vacancies: new industry or place", s.v, "--good", s.b], ["Still unemployed", Math.max(0, s.l - Math.min(s.l, s.v * s.m)), "--warn", s.c]];
  bars.forEach(([n, v, c, op], i) => { if (op <= 0.01) return; const x = 90 + i * 210, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 140, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 70, base - h - 8, money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 70, base + 22, n, "sm", { "text-anchor": "middle", style: "font-size:11px" }) + "</g>"; });
  if (s.t) o += SV.text(380, 40, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Structural unemployment", base: { l: 60, v: 40, m: 0, a: 0, b: 0, c: 0, t: "" }, draw: strChart, steps: [
  { cap: "A coal mine closes because demand for coal falls: <b>60 jobs are lost</b>.", s: { l: 60, v: 40, m: 0, a: 1, b: 0, c: 0, t: "" } },
  { cap: "Meanwhile a new industry (solar installation) has <b>40 vacancies</b> in another region, needing different skills.", s: { l: 60, v: 40, m: 0, a: 1, b: 1, c: 0, t: "" } },
  { cap: "The miners lack the skills and cannot move easily. <b>No match</b>: all 60 stay unemployed while 40 vacancies go unfilled. This is <b>structural unemployment</b>.", s: { l: 60, v: 40, m: 0, a: 1, b: 1, c: 1, t: "Mismatch: 60 unemployed, 40 vacancies" } },
  { cap: "With <b>retraining and help to move</b> (75% matched), 30 find jobs. Structural unemployment falls to 30. <b>Supply-side policy</b> works on the mismatch.", s: { l: 60, v: 40, m: 0.75, a: 1, b: 1, c: 1, t: "After retraining" } },
] });
function seasonChart(s) {
  const mths = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"], r = [3, 3, 4, 6, 8, 9, 9, 9, 8, 6, 4, 3], base = 320, k = 22; let o = SV.line(50, base, 710, base) + SV.text(50, 30, "Unemployment rate in a ski resort (%)", "sm");
  r.forEach((v, i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 70 + i * 52, h = v * k, hot = v >= 7; o += `<g opacity="${op}">` + SV.rect(x, base - h, 38, h, "", { style: `fill:var(${hot ? "--bad" : "--good"})`, opacity: 0.85 }) + SV.text(x + 19, base - h - 6, v, "sm bd", { "text-anchor": "middle" }) + SV.text(x + 19, base + 20, mths[i], "sm", { "text-anchor": "middle" }) + "</g>"; });
  return o;
}
Lib.stepper($("#stE"), { w: 760, h: 400, label: "Seasonal unemployment", base: { n: 0 }, draw: seasonChart, steps: [
  { cap: "In a ski resort <b>winter is the busy season</b>. From January to March resorts, hotels and lifts employ many workers, so unemployment is <b>low (3 to 4%)</b>.", s: { n: 3 } },
  { cap: "In spring and summer the resort is quiet: instructors, lift staff and hotel workers lose their work and <b>unemployment rises to about 9%</b>.", s: { n: 8 } },
  { cap: "Autumn brings the next season and unemployment falls again. This is <b>seasonal unemployment</b>: predictable and temporary, because it depends on the <b>time of year</b>.", s: { n: 12 } },
  { cap: "<b>Evaluate:</b> it is short term and can be planned for, but still costs workers income. Resorts can reduce it by diversifying (summer hiking, conferences).", s: { n: 12 } },
] });

/* Lab 1: mismatch */
function labM() {
  if (!$("#ma") || !$("#mb") || !$("#mc")) return;
  const l = +$("#ma").value, v = +$("#mb").value, m = +$("#mc").value / 100, matched = Math.min(l, v * m), u = l - matched, unfilled = v - matched;
  $("#ma1").textContent = money(matched, 0); $("#ma2").textContent = money(u, 0); $("#ma3").textContent = money(unfilled, 0);
  $("#mav").textContent = u === 0 ? "Every lost job has been matched to a vacancy: no structural unemployment." : `Of the ${l} jobs lost, only ${money(matched, 0)} workers can fill the ${v} vacancies. ${money(u, 0)} stay unemployed while ${money(unfilled, 0)} vacancies stay empty. The more the skills and locations match, the lower structural unemployment.`;
  $("#labM").innerHTML = strChart({ l, v, m, a: 1, b: 1, c: 1, t: "" });
}
Lib.slider($("#g1"), { id: "ma", label: "Jobs lost in a declining industry", min: 10, max: 100, step: 5, value: 60, fmt: (v) => v, onInput: labM });
Lib.slider($("#g2"), { id: "mb", label: "Vacancies in growing industries", min: 10, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labM });
Lib.slider($("#g3"), { id: "mc", label: "Workers able to fill vacancies (skills and location match)", min: 0, max: 100, step: 5, value: 0, fmt: (v) => v + "%", onInput: labM });
const TY = [
  { n: "Frictional", c: "Time to search, imperfect information, new entrants.", t: "Short term", p: "Better job information, job centres, online job boards.", e: "Graduate looking for a first job" },
  { n: "Structural", c: "Industries decline, technology, globalisation, immobile labour.", t: "Long term", p: "Training and retraining, help with relocation, regional policy, education.", e: "Miners after pit closures" },
  { n: "Cyclical", c: "Fall in aggregate demand in a recession.", t: "Medium term, tied to the cycle", p: "Expansionary fiscal and monetary policy.", e: "Car factory layoffs in a slump" },
  { n: "Seasonal", c: "Demand and supply of labour change with the time of year.", t: "Short and predictable", p: "Diversify the local economy, extend the season, retraining for off-season work.", e: "Ski instructors in summer" },
];
button_table("tyBtns", "tyOut", TY, 0, (p) => `<div class="tw"><table class="t"><tr><th>Causes</th><th>Length</th><th>Best response</th><th>Example</th></tr><tr><td>${p.c}</td><td>${p.t}</td><td>${p.p}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>type of unemployment</b> is each?", buckets: [{ label: "Frictional" }, { label: "Structural" }, { label: "Cyclical" }, { label: "Seasonal" }], items: [
  { text: "A graduate searching for a first job", b: 0 }, { text: "A worker between two jobs", b: 0 },
  { text: "Steelworkers whose plant closed because demand for steel fell", b: 1 }, { text: "Bank clerks replaced by online banking", b: 1 },
  { text: "Factory workers laid off in a recession", b: 2 }, { text: "Builders unemployed because spending has fallen across the economy", b: 2 },
  { text: "Fruit pickers out of work after the harvest", b: 3 }, { text: "Beach hotel staff in the off-season", b: 3 },
], done: "Name the type, then its cause." });
Lib.classify($("#cl2"), { prompt: "What is the <b>cause</b> of each type? Match each cause to the type of unemployment.", buckets: [{ label: "Frictional" }, { label: "Structural" }, { label: "Cyclical" }], items: [
  { text: "People take time to find a new job", b: 0 }, { text: "Poor information about vacancies", b: 0 },
  { text: "Skills do not match the jobs available", b: 1 }, { text: "An industry declines and workers cannot move", b: 1 }, { text: "Technology replaces workers", b: 1 },
  { text: "Aggregate demand falls", b: 2 }, { text: "The economy is in a recession", b: 2 },
], done: "Frictional: search. Structural: mismatch. Cyclical: low demand." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Frictional unemployment", "Temporary unemployment while workers move between jobs"],
  ["Structural unemployment", "Unemployment from a mismatch between workers' skills or location and available jobs"],
  ["Cyclical unemployment", "Unemployment due to a fall in aggregate demand in a recession"],
  ["Seasonal unemployment", "Unemployment due to the time of year"],
  ["Occupational immobility", "Workers lack the skills to move to other jobs"],
  ["Geographical immobility", "Workers find it hard to move to where jobs are"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how the decline of an industry causes structural unemployment</b>.", items: [
  "Demand for an industry's product falls",
  "Firms in the industry close or cut output",
  "Workers lose their jobs",
  "Their skills do not suit vacancies elsewhere",
  "They find it hard to move to where the jobs are",
  "Unemployment remains high for a long time",
], done: "Skills and location mismatch." });
''' + calc_js([
    ("In a recession, 800,000 workers are laid off from a labour force of 20 million. By how many percentage points could unemployment rise?", 4, "800,000 ÷ 20m × 100 = <b>4 percentage points</b>.", None, None),
    ("A closing mine puts 500 workers out of work. 200 find jobs in a new industry. How many remain unemployed?", 300, "500 − 200 = <b>300</b>.", None, None),
    ("Unemployment in a resort is 12% in the off-season and 3% in season. What is the percentage point difference?", 9, "12 − 3 = <b>9 percentage points</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which type of unemployment is caused by a recession?", ["Frictional", "Structural", "Cyclical", "Seasonal"], 2, "Demand-deficient unemployment follows a fall in AD."),
    ("A worker who has left one job and is looking for another is:", ["Structurally unemployed", "Frictionally unemployed", "Cyclically unemployed", "Seasonally unemployed"], 1, "Short-term, between jobs."),
    ("Unemployment caused by the decline of an industry is:", ["Structural", "Frictional", "Seasonal", "Cyclical only"], 0, "Skills and location mismatch."),
    ("Which type of unemployment is most likely to be reduced by better job information?", ["Frictional", "Structural", "Cyclical", "None"], 0, "People find jobs faster."),
    ("Tourist guides out of work in winter are an example of:", ["Frictional", "Structural", "Cyclical", "Seasonal"], 3, "It depends on the time of year."),
]) + "\n" + cards_js([("Frictional unemployment", "Temporary unemployment while workers move between jobs."), ("Structural unemployment", "Unemployment from a mismatch between skills or location and available jobs."), ("Cyclical unemployment", "Unemployment caused by a fall in total demand, often in a recession."), ("Seasonal unemployment", "Unemployment that depends on the time of year."), ("Technological unemployment", "Unemployment caused by machines or software replacing workers."), ("Occupational immobility", "Difficulty moving between jobs because of lack of skills."), ("Geographical immobility", "Difficulty moving to where jobs are."), ("Demand-deficient unemployment", "Another name for cyclical unemployment."), ("Vacancy", "A job opening that an employer wants to fill.")]) + "labM();\n"
explore = '''
  <h2>Lab 1 · Jobs lost, vacancies and the mismatch</h2>
  <p>Some jobs vanish, new vacancies appear elsewhere. How many workers can fill them depends on skills and location.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Workers matched to vacancies</small><strong id="ma1"></strong></div><div><small>Still unemployed</small><strong id="ma2"></strong></div><div><small>Vacancies left unfilled</small><strong id="ma3"></strong></div></div><div class="verdict" id="mav"></div></div></div>
    <svg id="labM" viewBox="0 0 760 360" role="img" aria-label="Jobs lost, vacancies and unemployment after matching"></svg>
  </div>

  <h2>Lab 2 · The four types compared</h2>
  <p>Pick a type to see its causes, how long it lasts and the best response.</p>
  <div class="card"><div class="row" id="tyBtns"></div><div id="tyOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define frictional unemployment. (Feb/Mar 2022, P22)", "Between jobs, temporary.", "[K|Frictional unemployment is unemployment of workers who are between jobs] [K|while they search for a new one; it is temporary.]"),
    Q(2, "Define", 2, "Define cyclical unemployment. (May/June 2021, P21)", "Lack of total demand, in a recession. Nothing for a fall in demand for one product.", "[K|Cyclical unemployment is unemployment caused by a lack of total (aggregate) demand] [K|in the economy, for example during a recession.]"),
    Q(3, "Define", 2, "Define structural unemployment. (May/June 2021, P23)", "Mismatch of skills or location; change in the structure of the economy.", "[K|Structural unemployment is unemployment caused by a change in the structure of the economy, such as the decline of an industry,] [K|where workers' skills or location do not match the jobs available.]"),
    Q(4, "Explain", 4, "Explain how frictional unemployment differs from cyclical unemployment. (May/June 2021, P22)", "Use 'whereas'. Cause, length, and whether vacancies exist.",
      "[K|Frictional unemployment is temporary unemployment while workers move between jobs,] [K|whereas cyclical unemployment is caused by a fall in total demand in a recession.] [N|Frictional unemployment exists even when the economy is doing well and there are vacancies,] [N|whereas in cyclical unemployment there are not enough jobs for all who want one, so it can last as long as the downturn.]"),
    Q(5, "Explain", 4, "Explain two types of unemployment. (Oct/Nov 2023, P22)", "Pick two and give cause and example for each.",
      "[K|Structural unemployment occurs when workers' skills do not match the jobs available.] [N|If an industry such as coal mining declines, former miners may lack the skills or be unable to move to where vacancies are, so they stay unemployed for a long time.] [K|Seasonal unemployment depends on the time of year.] [N|Hotel and ski-resort staff may lose work in the off-season, so unemployment rises and falls through the year.]"),
    Q(6, "Analyse", 6, "Analyse how new technology could cause unemployment.", "Replace workers, structural mismatch. Then evaluate: new jobs, retraining.",
      "[K|New technology such as robots or software can do tasks that workers did before.] [N|Firms may need fewer workers, so some lose their jobs.] [N|The unemployed may lack the skills for the new jobs created, or live far from them,] [N|so this is likely to be structural unemployment which could last a long time.] [E|However, technology can also create new jobs and raise incomes, so unemployment may only be temporary if workers can retrain.]", key=True),
)
tp = tips([
    ("Four types:", "frictional, structural, cyclical, seasonal."),
    ("Name the cause, not just the type.", "Search, mismatch, low demand, time of year."),
    ("Apply to the context.", "Closing mine: structural. Recession: cyclical. Tourism: seasonal."),
    ("Ask about vacancies.", "None because demand is low: cyclical. Vacancies unfilled: structural."),
    ("Link the type to the policy.", "That is how you prepare for 4.6.5."),
], cmds("Define", "Explain", "Analyse"))
body = page(CL("4.6.3 Causes and types of unemployment"), "Causes and Types of Unemployment", "Frictional, structural, cyclical and seasonal unemployment: causes, examples and how to tell them apart. Syllabus 4.6.3.",
    learn=learn, watch=watch(("Cyclical unemployment", "stC"), ("Structural unemployment", "stS"), ("Seasonal unemployment", "stE")), explore=explore,
    practise=practise(("Which type?", "cl1", "card"), ("Which cause?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Coal and steel closures", "In countries such as the UK in the 1980s the closure of coal mines and steelworks left many workers unemployed for years, as new jobs were in other industries and regions.", "Structural unemployment from industry decline and immobility."),
        rw("The 2008 recession", "After 2008, unemployment rose sharply in Spain and the US because demand fell across the economy. Spain's rate passed 25%.", "Cyclical unemployment and the link to recession."),
        rw("Tourism in Greece and Spain", "Resort areas have high unemployment in winter and low unemployment in summer.", "Seasonal unemployment."),
        rw("Jordan in 2020", "A past paper asks which type of unemployment Jordan mainly experienced in 2020, linking the type to economic conditions.", "Naming and justifying a type from context.")),
    exam=ex, tips=tp)
write("em3", body, js, "Causes and Types of Unemployment", "ig-unemployment-types")

# =========================================================== 4.6.4 Consequences
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Unemployment has costs for the <b>individual</b>, <b>firms</b>, the <b>government</b> and the <b>whole economy</b>. It wastes resources, so the economy produces less than it could. It lowers incomes and tax revenue and raises government spending on benefits. Good answers say who is affected, how, and end with the link to aims such as growth and living standards.</p></div>

  <h2>Consequences for each group</h2>
  <div class="tw"><table class="t">
    <tr><th>Who</th><th>Possible consequences</th></tr>
    <tr><td><b>The individual</b></td><td>Lower income and living standards; poverty and debt; loss of skills the longer they are unemployed; stress and poorer health; lower confidence; may affect family</td></tr>
    <tr><td><b>Firms</b></td><td>Lower consumer spending, so lower sales and profits; falling demand for products; but easier to hire workers and lower wage pressure; wasted potential</td></tr>
    <tr><td><b>The government</b></td><td>Lower tax revenue (income tax, spending taxes, corporation tax) and higher spending on benefits and other social costs, so a larger budget deficit; opportunity cost of that money</td></tr>
    <tr><td><b>The economy</b></td><td>Wasted resources: output below capacity (inside the PPC); lower real GDP and growth; lower living standards; greater inequality and poverty; social costs such as crime; may lower inflation</td></tr>
  </table></div>

  <h2>Unemployment and the PPC</h2>
  <p>Unemployed workers are an unused factor of production, so the economy produces <b>inside its PPC</b>. Putting them to work would increase output without using more scarce resources.</p>

  <h2>Unemployment and the budget</h2>
  <p>Each person who loses a job pays less tax (income tax, and less sales tax as spending falls) and may claim benefits. So a rise in unemployment moves the budget towards <b>deficit</b>. These effects work automatically, as <b>automatic stabilisers</b>, and cushion the fall in demand.</p>

  <h2>Is unemployment ever helpful?</h2>
  <ul>
    <li>Firms may find it easier to hire and wage pressure may be lower.</li>
    <li>Falling demand may reduce inflation.</li>
    <li>But these small gains are outweighed by lost output, lost incomes and social costs.</li>
  </ul>
'''
js = HEAD + COMMON + PPC + '''
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Unemployment and the PPC", base: { s: 1, in: 0, t: "" }, draw: ppcChart, steps: [
  { cap: "With <b>full employment</b> the economy produces <b>on its PPC</b>: all resources are used.", s: { s: 1, in: 1, t: "Full employment" } },
  { cap: "When workers lose their jobs, resources lie idle. The economy produces <b>inside the PPC</b>: lower output of everything.", s: { s: 1, in: 0, t: "Unemployment" } },
  { cap: "This is why unemployment is a <b>waste of resources</b>: the economy could produce more with the same factors. Bringing the unemployed back to work moves it back to the PPC.", s: { s: 1, in: 1, t: "Back to full employment" } },
] });
const UCH = ["Unemployment rises: workers lose their jobs", "Household incomes and spending fall", "Firms' sales and profits fall", "Government tax revenue falls and benefit spending rises", "The budget deficit widens: more borrowing", "Lower output: the economy produces below its potential"];
Lib.stepper($("#stU"), { w: 760, h: 400, label: "How unemployment spreads through the economy", base: { n: 0 }, draw: mkChain(UCH, "--bad"), steps: chainSteps(["<b>Individuals:</b> workers lose their jobs and their income.", "<b>Consumers:</b> lower incomes mean lower spending.", "<b>Firms:</b> sales and profits fall, so they may cut more jobs.", "<b>Government:</b> tax revenue falls and benefit spending rises.", "<b>Budget:</b> the deficit widens and the government has to borrow more.", "<b>Economy:</b> output falls below potential and living standards fall."]) });

/* Lab 1: cost to the government */
function labU() {
  if (!$("#ua") || !$("#ub") || !$("#uc")) return;
  const u = +$("#ua").value, b = +$("#ub").value, t = +$("#uc").value, tax = (u * t) / 1e6, ben = (u * b) / 1e6, tot = tax + ben;
  $("#ua1").textContent = "$" + money(tax, 2) + "bn"; $("#ua2").textContent = "$" + money(ben, 2) + "bn"; $("#ua3").textContent = "$" + money(tot, 2) + "bn";
  $("#uav").textContent = u === 0 ? "No rise in unemployment." : `If ${u.toLocaleString("en-US")} thousand more people are unemployed, the government loses about $${money(tax, 2)}bn in tax and pays about $${money(ben, 2)}bn in benefits: the budget gets worse by $${money(tot, 2)}bn. This money has an opportunity cost: it could have paid for schools or hospitals.`;
  const base = 300, k = 60 / Math.max(1, Math.max(tot, 1)) * 4; let o = SV.line(60, base, 700, base);
  [["Lost tax revenue", tax, "--accent"], ["Extra benefits", ben, "--warn"], ["Total effect on deficit", tot, "--bad"]].forEach(([n, v, c], i) => { const x = 110 + i * 190, h = Math.min(250, v * 40); o += SV.rect(x, base - h, 130, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, base - h - 8, "$" + money(v, 2) + "bn", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labU").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ua", label: "Rise in the number unemployed (thousands)", min: 0, max: 1000, step: 50, value: 500, fmt: (v) => v + "k", onInput: labU });
Lib.slider($("#g2"), { id: "ub", label: "Benefit paid to each unemployed person ($ a year)", min: 2000, max: 10000, step: 500, value: 6000, fmt: (v) => "$" + v, onInput: labU });
Lib.slider($("#g3"), { id: "uc", label: "Tax each worker used to pay ($ a year)", min: 2000, max: 15000, step: 500, value: 9000, fmt: (v) => "$" + v, onInput: labU });
const UG = [
  { n: "The individual", s: "Lower income, debt, stress and health problems; skills fade the longer the spell.", l: "Long-term unemployment can mean permanent loss of earnings and confidence.", x: "Explain two consequences of unemployment" },
  { n: "Firms", s: "Lower consumer spending cuts sales and profits; some firms close.", l: "Wasted potential workers; but firms may find hiring easier and wage costs lower.", x: "Explain two consequences to firms of unemployment" },
  { n: "The government", s: "Tax revenue falls, benefit spending rises: bigger deficit.", l: "Higher borrowing and debt; opportunity cost for other spending.", x: "Analyse how unemployment may affect the government's budget" },
  { n: "The economy", s: "Output falls below potential; lower real GDP and living standards.", l: "Wasted resources, more inequality and poverty, social costs; may lower inflation.", x: "Analyse why a government may have lower unemployment as its main aim" },
];
button_table("ugBtns", "ugOut", UG, 0, (p) => `<div class="tw"><table class="t"><tr><th>Short-run effect</th><th>Longer-run effect</th><th>Exam link</th></tr><tr><td>${p.s}</td><td>${p.l}</td><td>${p.x}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Who mainly bears each <b>consequence of unemployment</b>?", buckets: [{ label: "Individual" }, { label: "Firms" }, { label: "Government" }, { label: "Economy" }], items: [
  { text: "Lower income and stress", b: 0 }, { text: "Skills fade over time", b: 0 },
  { text: "Falling sales as customers spend less", b: 1 }, { text: "Lower profits and some closures", b: 1 },
  { text: "Lower tax revenue and higher benefit spending", b: 2 }, { text: "Larger budget deficit", b: 2 },
  { text: "Output below the PPC: wasted resources", b: 3 }, { text: "Lower real GDP and living standards", b: 3 },
], done: "Individual, firms, government, economy: the four groups in the syllabus." });
Lib.classify($("#cl2"), { prompt: "Is each effect of rising unemployment likely to <b>raise</b> or <b>lower</b> the government's budget balance?", buckets: [{ label: "Moves budget towards deficit" }, { label: "Moves budget towards surplus" }], items: [
  { text: "Less income tax from people who lost jobs", b: 0 }, { text: "More unemployment benefit paid", b: 0 }, { text: "Less sales tax as spending falls", b: 0 }, { text: "Lower corporation tax as profits fall", b: 0 },
  { text: "Government cuts benefits", b: 1 }, { text: "Government raises taxes", b: 1 },
], done: "Unemployment tends to widen the deficit." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Opportunity cost", "The next best alternative given up"],
  ["Automatic stabilisers", "Taxes and benefits that change with the cycle and cushion falls in demand"],
  ["Budget deficit", "Government spending is higher than revenue"],
  ["Long-term unemployment", "Being without a job for a long period, often a year or more"],
  ["Poverty", "A lack of income to meet basic needs"],
  ["Potential output", "Output when resources are fully used"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how unemployment could widen the budget deficit</b>.", items: [
  "Firms lay off workers",
  "Workers lose their earnings",
  "Income tax and sales tax revenue fall",
  "More people claim unemployment benefit",
  "Government spending rises while revenue falls",
  "The budget deficit widens",
], done: "A full 4-mark chain." });
''' + calc_js([
    ("A worker paid $10,000 a year in tax. She loses her job and claims $5,000 in benefit. By how much does the government's position worsen ($)?", 15000, "10,000 + 5,000 = <b>$15,000</b>.", None, None),
    ("If 400,000 workers each lose $9,000 in tax payments, how much tax revenue is lost ($bn)?", 3.6, "400,000 × 9,000 = $3.6bn = <b>$3.6bn</b>.", "400,000 × 9,000 = 3,600,000,000.", None),
    ("Unemployment benefit is $6,000 per person. 500,000 more people claim it. What is the extra cost ($bn)?", 3, "500,000 × 6,000 = <b>$3bn</b>.", None, None),
    ("Output is $800bn at full employment and $760bn with unemployment. What percentage of output is lost?", 5, "40 ÷ 800 × 100 = <b>5%</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which is a likely effect of rising unemployment on the government's budget?", ["Higher tax revenue", "A smaller deficit", "A larger deficit", "No effect"], 2, "Tax falls and benefit spending rises."),
    ("Unemployment means an economy is producing:", ["On its PPC", "Outside its PPC", "Inside its PPC", "At full employment"], 2, "Resources are not fully used."),
    ("Which is a consequence of unemployment for an individual?", ["Higher income", "Loss of skills over time", "Lower stress", "More tax paid"], 1, "Skills fade the longer someone is out of work."),
    ("Rising unemployment could reduce inflation because:", ["Total demand falls", "Output rises", "Taxes fall", "Imports rise"], 0, "Lower spending reduces demand-pull pressure."),
    ("A firm may suffer from unemployment because:", ["Customers have less to spend", "Workers become more skilled", "Taxes fall", "Imports fall"], 0, "Lower incomes mean lower sales."),
]) + "\n" + cards_js([("Opportunity cost", "The next best alternative given up when a choice is made."), ("Automatic stabilisers", "Taxes and benefits that change with the economic cycle and cushion falls in demand."), ("Budget deficit", "Government spending is higher than revenue."), ("Poverty", "A lack of income to meet basic needs."), ("Long-term unemployment", "Being without a job for a long period."), ("Living standards", "The quality and quantity of goods and services people can obtain."), ("Potential output", "Output when resources are fully and efficiently used."), ("Social costs of unemployment", "Costs to society such as crime, ill health and family problems.")]) + "labU();\n"
explore = '''
  <h2>Lab 1 · The cost to the government</h2>
  <p>When more people are unemployed, the government loses tax and pays benefits. Set the numbers and see how much the budget worsens.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Lost tax revenue</small><strong id="ua1"></strong></div><div><small>Extra benefit spending</small><strong id="ua2"></strong></div><div><small>Worsening of the budget</small><strong id="ua3"></strong></div></div><div class="verdict" id="uav"></div></div></div>
    <svg id="labU" viewBox="0 0 760 340" role="img" aria-label="Cost of unemployment to the government"></svg>
  </div>

  <h2>Lab 2 · Consequences by group</h2>
  <p>Pick a group to see the effects and the matching exam question.</p>
  <div class="card"><div class="row" id="ugBtns"></div><div id="ugOut"></div></div>
'''
ex = exam(
    Q(1, "Identify", 2, "Identify two costs of unemployment. (Feb/Mar 2025, P22)", "Short answers: lost output, lower incomes, higher benefit spending, lower tax revenue, social problems.", "[K|Lower income (poverty) for the unemployed.] [K|Lost output, because resources are unused (or higher government spending on benefits).]"),
    Q(2, "Explain", 4, "Explain two consequences of unemployment. (Feb/Mar 2022, P22)", "Two different consequences, each linked: output and growth, incomes and poverty, tax revenue and benefits.",
      "[K|Unemployment means lower output because resources are not fully used.] [N|The economy produces inside its PPC, so real GDP and economic growth are lower.] [K|Unemployed people receive lower incomes.] [N|They can buy fewer goods and services, so poverty may rise and living standards fall.]"),
    Q(3, "Explain", 4, "Explain two consequences to firms of unemployment. (May/June 2020, P21)", "Lower consumer demand, lower profits; but possibly easier recruitment and lower wage pressure.",
      "[K|Unemployed people have lower incomes, so total spending falls.] [N|Firms sell less and profits could fall, so some may cut output or close.] [K|On the other hand, a larger pool of jobseekers makes it easier to recruit.] [N|Firms may find that wage pressure is lower and they can hire workers more cheaply.]"),
    Q(4, "Analyse", 4, "Analyse how an increase in unemployment may affect a government's budget. (Oct/Nov 2022, P22)", "Both sides of the budget: revenue falls, spending rises, deficit widens.",
      "[K|A rise in unemployment is likely to increase a budget deficit.] [N|Fewer workers means less income tax, and lower spending means less sales tax; falling profits cut corporation tax.] [N|At the same time the government pays more unemployment benefit and may spend more on other social costs.] [N|With lower revenue and higher spending the deficit widens.]", key=True),
    Q(5, "Analyse", 6, "Analyse why a government may have lower unemployment as its main aim. (May/June 2022, P22)", "Wasted resources, growth, incomes, tax revenue and benefit savings, living standards, social costs.",
      "[K|Unemployment is a waste of resources, as the economy produces below its capacity.] [N|Lower unemployment would raise output and economic growth, and incomes would rise, so living standards could improve and poverty could fall.] [N|More people in work would spend more, raising total demand and firms' profits.] [N|The government would collect more tax and spend less on benefits, so the budget could improve.] [N|It might also reduce social problems such as crime.]", key=True),
    Q(6, "Discuss", 8, "Discuss whether or not a fall in a country's unemployment rate will reduce poverty. (May/June 2021, P21; Oct/Nov 2022, P23)", "For: more households with earnings. Against: low-paid or part-time jobs, other causes of poverty, people outside the labour force, inflation.",
      "[K|The unemployment rate is the percentage of the labour force without a job, and poverty means having too little income to meet basic needs.] [N|A fall could reduce poverty because more people have earnings, so more households could afford food, housing and healthcare, and spending would rise.] [N|The government may also spend less on benefits and more on services that help the poor.] [E|This is more likely if the new jobs are well paid and full time.] [N|However, the new jobs might be low paid, part time or temporary, so households could stay in poverty.] [N|Poverty also has other causes such as ill health, old age, low skills or living in a poor region, and a fall in the rate might be because people stopped looking.] [E|Overall, a fall in unemployment is likely to reduce poverty, but the amount depends on the quality of jobs and the other causes of poverty.]", key=True),
    Q(7, "Discuss", 8, "Discuss whether or not a reduction in the unemployment rate benefits an economy. (Oct/Nov 2022, P21)", "For: output, incomes, tax revenue, lower benefits. Against: inflation, wage pressure, imports, shortage of workers, if the fall is due to discouraged workers leaving.",
      "[K|A reduction in the unemployment rate means a smaller percentage of the labour force is without a job.] [N|It could benefit the economy by raising output and economic growth, as more resources are used.] [N|Higher employment raises incomes and spending, and the government collects more tax and pays less in benefits.] [E|These gains are larger if the economy has spare capacity.] [N|On the other hand, if the economy is near full capacity, more demand could raise prices, and firms may compete for scarce workers, pushing up wages and costs.] [N|Higher incomes may also raise imports, and the rate may fall because people stop looking for work.] [E|Overall, a fall in unemployment is likely to benefit the economy, particularly when it is caused by higher output rather than people leaving the labour force.]", key=True),
)
tp = tips([
    ("Four groups:", "the individual, firms, the government, the economy."),
    ("Link tax and benefits to the deficit.", "Revenue falls, spending rises."),
    ("Unemployment is a waste of resources.", "The economy is inside its PPC."),
    ("Give a benefit and a cost where asked for two sides.", "A little less inflation against lost output and income."),
    ("Use 'could' and 'may'.", "Cambridge rewards hedged reasoning."),
], cmds("Identify", "Explain", "Analyse", "Discuss"))
body = page(CL("4.6.4 Consequences of unemployment"), "Consequences of Unemployment", "How unemployment affects individuals, firms, the government and the economy. Syllabus 4.6.4.",
    learn=learn, watch=watch(("Unemployment and the PPC", "stP"), ("How unemployment spreads through the economy", "stU")), explore=explore,
    practise=practise(("Who bears the consequence?", "cl1", "card"), ("Effect on the budget", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the budget chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Youth unemployment in Spain", "After 2008, more than half of young Spaniards were without a job at one point. Many emigrated, and long spells without work lowered their later earnings.", "Consequences for individuals and the economy: lost skills and output."),
        rw("Unemployment benefit in a recession", "During COVID-19 many governments extended benefits and wage support. Their deficits rose sharply as tax revenue fell.", "Government consequences."),
        rw("Regions left behind", "Areas that lost major industries have often had high unemployment, lower incomes and social problems for decades.", "Wider social and economic costs."),
        rw("The Nigerian budget", "A past paper links rising unemployment in Nigeria to the government's budget, with lower tax revenue and higher spending.", "A 4-mark analysis of the budget.")),
    exam=ex, tips=tp)
write("em4", body, js, "Consequences of Unemployment", "ig-unemployment-consequences")

# =========================================================== 4.6.5 Policies
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>There is a <b>range of policies</b> to reduce unemployment, and which works best depends on the <b>type</b> of unemployment. <b>Demand-side policies</b> (fiscal and monetary) raise AD and reduce <b>cyclical</b> unemployment. <b>Supply-side policies</b> such as training and job information reduce <b>structural</b> and <b>frictional</b> unemployment. Evaluate with time lags, cost, inflation and conflicts with other aims.</p></div>

  <h2>The range of policies</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>How it reduces unemployment</th><th>Best for</th></tr>
    <tr><td><b>Expansionary fiscal policy</b> (more spending, lower taxes)</td><td>Raises AD, so firms hire more workers</td><td>Cyclical</td></tr>
    <tr><td><b>Expansionary monetary policy</b> (lower interest rates, lower exchange rate)</td><td>Cheaper borrowing raises C and I; exports become cheaper</td><td>Cyclical</td></tr>
    <tr><td><b>Education, training and retraining</b></td><td>Raises skills and mobility so workers can fill vacancies</td><td>Structural</td></tr>
    <tr><td><b>Better job information and matching</b> (job centres, online job boards)</td><td>Reduces the time spent searching</td><td>Frictional</td></tr>
    <tr><td><b>Labour market reforms</b> (lower benefits, easier hiring)</td><td>Raises the incentive to work and lowers hiring costs</td><td>Frictional, structural</td></tr>
    <tr><td><b>Help with moving and regional policy</b> (relocation grants, subsidies to firms in depressed regions, infrastructure)</td><td>Brings jobs to workers or workers to jobs</td><td>Structural</td></tr>
    <tr><td><b>Lower taxes, incentives to invest, deregulation, privatisation</b></td><td>Raises investment and firms' demand for labour</td><td>Cyclical, structural (longer term)</td></tr>
    <tr><td><b>Diversification of the local economy</b></td><td>Creates jobs outside the peak season</td><td>Seasonal</td></tr>
    <tr><td><b>Tariffs and protection</b></td><td>Protects domestic jobs from imports</td><td>Some structural, but risky</td></tr>
  </table></div>

  <h2>How effective are they?</h2>
  <div class="grid2">
    <div class="card"><h3>Demand-side</h3><ul><li><b>Pros:</b> relatively quick when there is spare capacity.</li><li><b>Cons:</b> risk of <b>inflation</b> (a conflict between full employment and stable prices); bigger deficit; does little for structural unemployment.</li></ul></div>
    <div class="card"><h3>Supply-side</h3><ul><li><b>Pros:</b> tackles the cause of structural and frictional unemployment; raises productivity.</li><li><b>Cons:</b> slow and costly; training may not match jobs; cuts to benefits can hurt the poor and cut demand.</li></ul></div>
  </div>
  <div class="grid2">
    <div class="card"><h3>Minimum wages</h3><p>A minimum wage helps low-paid workers but, if set above the market wage, firms may hire fewer workers, so unemployment could rise, especially among young and unskilled workers.</p></div>
    <div class="card"><h3>Tariffs</h3><p>Tariffs may protect some jobs but raise prices, invite retaliation and reduce exports, so overall employment may not rise.</p></div>
  </div>

  <h2>Evaluating</h2>
  <ul>
    <li>Identify the <b>type</b> of unemployment first: the same policy may work for one type and not another.</li>
    <li><b>Time lags:</b> training takes years; interest rate cuts take months.</li>
    <li><b>Cost and deficit:</b> spending and subsidies need funding.</li>
    <li><b>Inflation:</b> reducing unemployment may raise inflation near full capacity.</li>
    <li><b>Side effects</b> such as inequality or damage to other aims.</li>
  </ul>
'''
js = HEAD + COMMON + '''
Lib.stepper($("#stD"), { w: 760, h: 400, label: "Demand-side policy and cyclical unemployment", base: { sh: -16, a: 0 }, draw: adasChart, steps: [
  { cap: "After a recession AD has shifted <b>left</b> and cyclical unemployment is high.", s: { sh: -16, a: 0 } },
  { cap: "The government and central bank use <b>expansionary policy</b>: lower interest rates, more spending, lower taxes. <b>AD shifts back to the right</b>.", s: { sh: 0, a: 0 } },
  { cap: "Real GDP rises. Firms need more workers, so <b>cyclical unemployment falls</b>.", s: { sh: 14, a: 0 } },
  { cap: "<b>Evaluate:</b> push too far and AD runs into capacity limits: <b>inflation</b>. It does little for structural unemployment, where workers' skills do not match vacancies.", s: { sh: 40, a: 0 } },
] });
const STP = ["The government funds retraining and relocation help", "Workers gain new skills and can move to where jobs are", "The mismatch between workers and vacancies narrows", "Firms can fill vacancies: employment rises", "Structural unemployment falls", "Evaluation: slow, costly, and the skills must match the jobs"];
Lib.stepper($("#stT"), { w: 760, h: 400, label: "Supply-side policy and structural unemployment", base: { n: 0 }, draw: mkChain(STP, "--good"), steps: chainSteps(["The government funds <b>retraining and relocation help</b>.", "Workers gain <b>new skills</b> and can move to where the jobs are.", "The <b>mismatch</b> between workers and vacancies narrows.", "Firms can <b>fill vacancies</b>: employment rises.", "<b>Structural unemployment</b> falls.", "<b>Evaluate:</b> it takes years, costs money, and only works if the skills taught match what firms want."]) });

/* Lab 1: which policy for which type */
const TYPES = ["Frictional", "Structural", "Cyclical", "Seasonal"], POLS = ["Expansionary fiscal or monetary policy", "Training and retraining", "Job information and matching", "Cutting benefits (labour market reform)", "Regional policy and help to move"];
const RATE = [[1, 1, 3, 0], [1, 3, 1, 1], [3, 2, 1, 1], [2, 2, 0, 1], [1, 3, 1, 1]];
const NOTE = [["Cheaper borrowing and more spending raise demand for workers, but this does not teach skills or stop people changing jobs.", "Better skills are not the cause of unemployment in a slump; demand is.", "Raises AD, so firms hire again: the standard cure for cyclical unemployment.", "Seasonal jobs depend on the calendar, not total demand."], ["A little help, if the person lacks skills, but they are mainly between jobs.", "Directly tackles the skills mismatch: the best tool.", "Skills are not the main problem in a slump.", "Some value if workers retrain for work in the off-season."], ["Faster matching is exactly what reduces time between jobs.", "Helps workers find the vacancies that suit their skills.", "Vacancies are not available, so information does not create jobs.", "Helps people find temporary work in the off-season."], ["Lower benefits speed up job search.", "May push people into any job but does not fix a skills mismatch.", "Cutting benefits could reduce demand and make a recession worse.", "Some effect, but does not change the seasonal pattern."], ["Helps a little by moving jobs and workers closer.", "Brings jobs to depressed regions or helps workers move: tackles geographical immobility.", "Little help in a general downturn.", "May help diversify the local economy."]];
const RL = ["Little effect", "Some help", "Moderate help", "Very effective"];
let selT = 1, selP = 1;
function showMatrix() {
  $("#mxT").innerHTML = TYPES.map((t, j) => `<button class="b${j === selT ? " pri" : ""}" data-j="${j}">${t}</button>`).join("");
  $("#mxP").innerHTML = POLS.map((t, j) => `<button class="b${j === selP ? " pri" : ""}" data-j="${j}">${t}</button>`).join("");
  $$("#mxT .b").forEach((b) => (b.onclick = () => { selT = +b.dataset.j; showMatrix(); }));
  $$("#mxP .b").forEach((b) => (b.onclick = () => { selP = +b.dataset.j; showMatrix(); }));
  const r = RATE[selP][selT];
  $("#mxOut").innerHTML = `<div class="verdict"><b>${POLS[selP]}</b> for <b>${TYPES[selT].toLowerCase()}</b> unemployment: <b>${RL[r]}</b>. ${NOTE[selP][selT]}</div>`;
}
showMatrix();
const PP = [
  { n: "Expansionary fiscal policy", w: "Raises AD through G and tax cuts.", sp: "Medium", c: "Deficit; inflation near capacity; weak against structural unemployment." },
  { n: "Cut interest rates", w: "Cheaper borrowing raises C and I.", sp: "Months to a year", c: "Weak if confidence is low; may raise inflation." },
  { n: "Education and training", w: "Skills and mobility rise, filling vacancies.", sp: "Slow (years)", c: "Costly; skills must match jobs." },
  { n: "Cut unemployment benefit", w: "Raises the incentive to look for work.", sp: "Medium", c: "Hurts the poor; may cut demand; may not create jobs." },
  { n: "Minimum wage", w: "Raises incomes of low-paid workers.", sp: "Immediate", c: "May raise unemployment if set too high, especially for young and unskilled." },
  { n: "Tariffs", w: "Protect domestic jobs from imports.", sp: "Fast", c: "Higher prices, retaliation, fewer exports; other jobs may be lost." },
  { n: "Regional subsidies", w: "Encourage firms to open in depressed areas.", sp: "Medium", c: "Costly; firms may leave when subsidy ends." },
];
button_table("ppBtns", "ppOut", PP, 0, (p) => `<div class="tw"><table class="t"><tr><th>How it works</th><th>Speed</th><th>The catch</th></tr><tr><td>${p.w}</td><td>${p.sp}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>type of unemployment</b> would each policy mainly help?", buckets: [{ label: "Cyclical" }, { label: "Structural" }, { label: "Frictional" }, { label: "Seasonal" }], items: [
  { text: "Cut interest rates and raise government spending", b: 0 }, { text: "Cut taxes in a recession", b: 0 },
  { text: "Retraining programmes for ex-miners", b: 1 }, { text: "Relocation grants to move to where jobs are", b: 1 },
  { text: "An online job-matching service", b: 2 }, { text: "Better information about vacancies", b: 2 },
  { text: "Diversifying a resort's economy into summer activities", b: 3 }, { text: "Training seasonal workers for off-season jobs", b: 3 },
], done: "Match the policy to the type." });
Lib.classify($("#cl2"), { prompt: "Is each policy <b>demand-side</b> or <b>supply-side</b>?", buckets: [{ label: "Demand-side" }, { label: "Supply-side" }], items: [
  { text: "Raise government spending", b: 0 }, { text: "Cut interest rates", b: 0 }, { text: "Cut income tax to raise spending", b: 0 }, { text: "Increase the money supply", b: 0 },
  { text: "Fund apprenticeships", b: 1 }, { text: "Cut unemployment benefit to raise incentives", b: 1 }, { text: "Deregulate markets so new firms can enter", b: 1 }, { text: "Build infrastructure to lower firms' costs", b: 1 },
], done: "Demand-side shifts AD; supply-side raises capacity and matching." });
Lib.match($("#m1"), { prompt: "Match the policy to its main weakness.", pairs: [
  ["Expansionary fiscal policy", "Bigger deficit; inflation near full capacity"],
  ["Cutting interest rates", "May not work if confidence is low"],
  ["Education and training", "Takes years and skills may not match jobs"],
  ["Cutting unemployment benefit", "May hurt the poor and reduce demand"],
  ["Minimum wage", "May cause unemployment among low-skilled workers"],
  ["Tariffs", "Retaliation and higher prices"],
], done: "Every policy needs an evaluation point." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a cut in interest rates could reduce cyclical unemployment</b>.", items: [
  "The central bank cuts the interest rate",
  "Borrowing is cheaper and saving less attractive",
  "Consumption and investment rise",
  "Aggregate demand shifts right",
  "Firms produce more and hire more workers",
  "Cyclical unemployment falls",
], done: "A demand-side chain." });
''' + calc_js([
    ("A government spends $6bn on a jobs programme and the multiplier is 2. By how much does income rise ($bn)?", 12, "2 × 6 = <b>$12bn</b>.", None, None),
    ("Training moves 40% of 50,000 structurally unemployed workers into jobs. How many find work?", 20000, "40% × 50,000 = <b>20,000</b>.", None, None),
    ("The unemployment rate falls from 9% to 7% in a labour force of 25 million. How many fewer people are unemployed (millions)?", 0.5, "2% × 25m = <b>0.5 million</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which policy is most likely to reduce cyclical unemployment?", ["Retraining programmes", "Expansionary fiscal and monetary policy", "Job-matching websites", "Cuts to unemployment benefit"], 1, "It raises AD and so the demand for labour."),
    ("Which policy is most likely to reduce structural unemployment?", ["Cutting interest rates", "Education and retraining", "Raising VAT", "Higher import tariffs"], 1, "It tackles the skills mismatch."),
    ("A possible disadvantage of expansionary fiscal policy to reduce unemployment is:", ["Lower inflation", "A larger budget deficit and possible inflation", "Fewer jobs", "Lower AD"], 1, "Spending may raise prices and the deficit."),
    ("A minimum wage set above the equilibrium wage may:", ["Reduce unemployment", "Increase employers' demand for workers", "Increase unemployment among low-skilled workers", "Reduce prices"], 2, "Firms may hire fewer workers."),
    ("Which policy would best reduce frictional unemployment?", ["Better job information", "Higher government spending", "Higher interest rates", "Tariffs"], 0, "Faster matching reduces time between jobs."),
]) + "\n" + cards_js([("Demand-side policy", "Fiscal and monetary policy that changes aggregate demand."), ("Supply-side policy", "Measures to raise productive capacity and improve how labour markets work."), ("Retraining", "Teaching workers new skills so they can move to different jobs."), ("Regional policy", "Policies to create jobs and investment in depressed regions."), ("Labour market reform", "Changes to make labour markets more flexible, such as easier hiring and lower benefits."), ("Minimum wage", "The lowest wage employers can legally pay."), ("Tariff", "A tax on imports."), ("Job centre", "A service that helps unemployed people find work."), ("Diversification", "Developing different industries so an area is less dependent on one.")]) + "showMatrix();\n"
explore = '''
  <h2>Lab 1 · Which policy for which type?</h2>
  <p>Choose a type of unemployment and a policy to see how effective the policy is likely to be.</p>
  <div class="card"><p><b>Type of unemployment</b></p><div class="row" id="mxT"></div><p style="margin-top:14px"><b>Policy</b></p><div class="row" id="mxP"></div><div id="mxOut" style="margin-top:14px"></div></div>

  <h2>Lab 2 · Policy picker</h2>
  <p>Pick a policy to see how it works, how fast, and the catch.</p>
  <div class="card"><div class="row" id="ppBtns"></div><div id="ppOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain how training could reduce structural unemployment.", "Mismatch is the cause; training fixes skills and mobility; then jobs.",
      "[K|Structural unemployment is caused by a mismatch between workers' skills and the jobs available.] [N|Training and retraining give workers the skills that employers need, so they can fill vacancies in growing industries.] [N|Better qualifications can also make workers more mobile between industries, so the mismatch narrows and structural unemployment could fall.] [E|However, it can take years and the skills must match what firms need.]"),
    Q(2, "Analyse", 6, "Analyse how an increase in investment may affect unemployment. (May/June 2023, P22)", "Capital spending raises AD and demand for labour (cyclical); investment in education or infrastructure reduces structural unemployment.",
      "[K|Investment is spending on capital goods such as machinery and buildings.] [N|It adds to total demand and firms may expand output, so they might need more workers to use the new equipment, reducing cyclical unemployment.] [N|Investment in education and training could raise skills and mobility, reducing structural unemployment.] [N|Investment in infrastructure could make it easier for workers to travel to jobs and for firms to set up, creating jobs.] [E|However, new machines could replace some workers, so unemployment may rise in some jobs.]", key=True),
    Q(3, "Analyse", 6, "Analyse how the introduction of a minimum wage could affect unemployment. (May/June 2024, P22)", "Both effects: higher wages could mean fewer jobs; but also more spending. Hedge.",
      "[K|A minimum wage is a legal lowest wage that firms can pay.] [N|If it is set above the market wage, firms' labour costs rise and the quantity of labour demanded may fall, so some low-skilled workers could lose their jobs or not be hired.] [N|At the same time more people may want to work at the higher wage, so the supply of labour could rise, increasing unemployment.] [N|Firms might also replace workers with machines.] [E|However, higher incomes for low-paid workers could raise spending and demand for labour, and if the minimum is below the market wage it might have no effect.]", key=True),
    Q(4, "Discuss", 8, "Discuss whether or not an increase in government spending will reduce unemployment. (May/June 2020, P21)", "For: raises AD and the demand for labour. Against: time lags, inflation, deficit, wrong type of unemployment.",
      "[K|Government spending is a part of aggregate demand.] [N|If it rises, for example on building projects, firms are likely to hire more workers and the multiplier effect may create further jobs, so cyclical unemployment could fall.] [N|It can also be targeted at regions with high unemployment.] [E|This is most effective when there is spare capacity.] [N|However, it may take time to plan projects, and the extra spending could widen the budget deficit.] [N|If the economy is near full capacity, it may cause inflation, and it does little for structural unemployment, where workers lack the skills for the jobs.] [E|Overall, an increase in spending is likely to help when unemployment is cyclical, but its success depends on the type of unemployment and the state of the economy and the budget.]", key=True),
    Q(5, "Discuss", 8, "Discuss whether or not a government can reduce unemployment without increasing inflation. (Feb/Mar 2021, P22)", "For: supply-side policies; spare capacity. Against: demand-side policies near capacity; wage pressure.",
      "[K|A government can try to reduce unemployment using demand-side or supply-side policy.] [N|Supply-side policies such as training and job information raise productive capacity, so output and jobs can rise without pushing up prices, and they could even lower costs.] [N|If there is spare capacity, a rise in demand could also create jobs with little inflation.] [E|However, supply-side policies are slow.] [N|Demand-side policies such as spending and lower interest rates are quicker but, if the economy is near full capacity, additional demand could mostly raise prices, and a tight labour market may push up wages, increasing costs.] [E|Overall, a government is more likely to reduce unemployment without inflation if there is spare capacity or it uses supply-side measures, but the choice depends on the type of unemployment and the economy's capacity.]", key=True),
    Q(6, "Discuss", 8, "Discuss whether or not high tariffs can reduce unemployment. (Oct/Nov 2024, P21)", "For: protect jobs in domestic industries; against: retaliation, higher prices, less competition, lost export jobs.",
      "[K|A tariff is a tax on imports.] [N|High tariffs make imports dearer, so consumers may buy more domestic goods, and domestic firms could expand and employ more workers, reducing unemployment in protected industries.] [E|This may be most effective for industries facing unfair competition from abroad.] [N|However, other countries may retaliate with tariffs on this country's exports, so jobs in export industries could be lost.] [N|Higher prices reduce consumers' real incomes, and without competition domestic firms may become inefficient.] [N|Firms that rely on imported inputs also face higher costs.] [E|Overall, high tariffs may protect some jobs in the short term but are unlikely to reduce unemployment across the economy, particularly if other countries retaliate. The outcome depends on the size of the tariffs and the industries protected.]", key=True),
)
tp = tips([
    ("Identify the type first.", "Cyclical: demand-side. Structural and frictional: supply-side."),
    ("Link each policy to a mechanism.", "'Training improves skills so workers can fill vacancies.'"),
    ("Conflict: unemployment and inflation.", "Demand-side policy near full capacity raises prices."),
    ("Evaluate with time lag, cost and side effects.", "Deficit, inequality, retaliation, minimum wage unemployment."),
    ("End with 'it depends on the type and the state of the economy'.", "That is Level 3 reasoning."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("4.6.5 Policies to reduce unemployment"), "Policies to Reduce Unemployment", "The range of demand-side and supply-side policies to reduce unemployment, matched to the type of unemployment, and how effective each is. Syllabus 4.6.5.",
    learn=learn, watch=watch(("Demand-side policy and cyclical unemployment", "stD"), ("Supply-side policy and structural unemployment", "stT")), explore=explore,
    practise=practise(("Which type does it help?", "cl1", "card"), ("Demand-side or supply-side?", "cl2", "card"), ("Match the policy to its weakness", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Germany's short-time work", "During recessions Germany subsidised firms to keep workers on reduced hours rather than lay them off, which kept unemployment low.", "A policy to keep cyclical unemployment down."),
        rw("Retraining after coal closures", "Several governments have funded retraining and regional investment for areas that lost coal mining, with mixed success.", "Structural policies and their slow results."),
        rw("Tunisia and frictional unemployment", "A past paper asks about two ways the Tunisian government tried to reduce frictional unemployment.", "Policies matched to the type of unemployment."),
        rw("Minimum wage debates", "Many countries have raised minimum wages in recent years. Research finds that effects on employment are small for modest rises but can be larger when it is set very high.", "Evaluation: effect depends on the level.")),
    exam=ex, tips=tp)
write("em5", body, js, "Policies to Reduce Unemployment", "ig-unemployment-policies")
