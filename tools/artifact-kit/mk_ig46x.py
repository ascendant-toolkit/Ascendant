"""Builds the 4.6 extension review: changes in the patterns and levels of employment (coursebook 30.2 and 30.3).
Cambridge removed this from the 0455 syllabus for 2027-29, so the page is labelled as extension.
Run: python3 tools/artifact-kit/mk_ig46x.py"""
from igsy import *
HEAD = Old("mon").j_((2, 25)) + Old("fisc").j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
TITLE = "Extension: Changing Patterns and Levels of Employment"

DRAW = '''
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
'''

js = HEAD + COMMON + DRAW + '''
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
''' + calc_js([
    ("The working-age population is 40 million and the labour force is 26 million. What is the participation rate (%)?", 65, "26 ÷ 40 × 100 = <b>65%</b>.", None, None),
    ("The working-age population is 90 million and the participation rate is 70%. How large is the labour force (millions)?", 63, "90 × 0.70 = <b>63 million</b>.", None, None),
    ("The labour force grows by 3 million and the number employed grows by 1 million. By how many million does unemployment change?", 2, "3 − 1 = <b>2 million more</b> unemployed.", None, None),
    ("Of 25 million employed people, 4 million work for the government. What percentage work in the private sector?", 84, "(25 − 4) ÷ 25 × 100 = <b>84%</b>.", None, None),
]) + mcq_js("qz1", [
    ("As an economy develops, employment usually moves:", ["From tertiary to primary", "From primary to secondary and then tertiary", "From secondary to primary", "Only into the public sector"], 1, "Services tend to take a growing share."),
    ("When could employment and unemployment both rise?", ["When the labour force grows faster than the number of jobs", "When the labour force shrinks", "Never", "When every new job goes to an unemployed person and nobody joins the labour force"], 0, "Some of the extra jobseekers find no work."),
    ("Which person is economically inactive?", ["A jobseeker", "A part-time worker", "A full-time student not looking for work", "A self-employed farmer"], 2, "They are outside the labour force."),
    ("Which is a likely feature of informal employment?", ["Strong union protection", "A company pension", "Little job protection", "Regular formal training"], 2, "Informal work is largely outside legal protection."),
    ("A shift towards privatisation is likely to:", ["Raise the share of workers in the private sector", "Raise the share in the public sector", "Remove all unemployment", "Shrink the working-age population"], 0, "Jobs move from state to private employers."),
]) + "\n" + cards_js([("Industrial structure", "How output and employment are divided between the primary, secondary and tertiary sectors."), ("Public sector", "Organisations owned or run by the government."), ("Private sector", "Businesses owned and run by private individuals and firms."), ("Self-employed", "People who work for themselves."), ("Informal economy", "Largely unrecorded work with little legal protection."), ("Formal economy", "Recorded work covered by laws, taxes and employment rights."), ("High quality employment", "Skilled, secure work with training, progression and good conditions."), ("Low quality employment", "Unskilled work with little training and poor conditions."), ("Flexible labour force", "A labour force that adjusts quickly and smoothly to changes in market conditions."), ("Participation rate", "The labour force as a percentage of the working-age population."), ("Economically active", "Those in the labour force, employed or unemployed."), ("Economically inactive", "Those of working age outside the labour force.")])

NOTE = '<div class="warn"><b class="h">Extension: not in the 2027–29 syllabus</b>Cambridge removed changing patterns and levels of employment from the 0455 syllabus for 2027, 2028 and 2029. Your coursebook still covers it (Chapter 30). Read it for background and stronger examples. It is not a set topic in those exams.</div>'
learn = f'''
  {NOTE}
  <div class="card big"><h3>The big idea</h3>
  <p>The <span class="kw">pattern of employment</span> (who works, where, for whom and on what terms) tends to change as an economy develops. The <span class="kw">level of employment</span> is how many people have jobs. Employment and unemployment do not always move in opposite directions, because the labour force can change too.</p></div>

  <h2>How patterns of employment change</h2>
  <div class="tw"><table class="t">
    <tr><th>Change</th><th>What tends to happen</th><th>Possible reason or effect</th></tr>
    <tr><td><b>Industrial structure</b></td><td>Workers move from primary to secondary, then to tertiary</td><td>Rising incomes and productivity shift demand and jobs. Some industries expand while others contract, so workers may need to be occupationally and geographically mobile</td></tr>
    <tr><td><b>Women in work</b></td><td>The number and proportion of women employed has risen in most countries</td><td>Changing social attitudes and less discrimination may open up jobs and raise women's pay</td></tr>
    <tr><td><b>Public and private sector</b></td><td>In many countries the private sector's share has grown</td><td>A move towards a market economy, including privatisation</td></tr>
    <tr><td><b>Full-time and part-time</b></td><td>Most work full-time; some work part-time</td><td>Part-time may be a choice (family care, other interests) or forced because full-time jobs cannot be found</td></tr>
    <tr><td><b>Employees and self-employed</b></td><td>Self-employment is rising in some countries and already high in others</td><td>In some lower-income countries many self-employed people work in the informal economy</td></tr>
    <tr><td><b>Flexibility</b></td><td>Firms look for workers who can adjust quickly</td><td>Numbers, hours, location, tasks or pay may change (see 4.6.1)</td></tr>
  </table></div>

  <h2>Formal and informal economies</h2>
  <div class="grid2">
    <div class="card"><h3>Formal</h3><ul><li>More likely to have social security, employment protection and legal rights.</li><li>Unions may bargain for better conditions.</li><li>A growing formal economy tends to raise job quality and productivity.</li></ul></div>
    <div class="card"><h3>Informal</h3><ul><li>Includes some self-employed, migrant and casual workers.</li><li>Minimum wage laws and pensions may not reach them.</li><li>Training, productivity and pay tend to be lower.</li></ul></div>
  </div>

  <h2>High and low quality employment</h2>
  <div class="grid2">
    <div class="card"><h3>High quality</h3><p>Skilled and interesting work with training, chances to progress, good conditions and relatively secure jobs. Its share tends to rise as an economy develops.</p></div>
    <div class="card"><h3>Low quality</h3><p>Unskilled work with little or no training and poor conditions.</p></div>
  </div>

  <h2>Changes in the level of employment</h2>
  <div class="tw"><table class="t">
    <tr><th>What happens</th><th>How it is possible</th></tr>
    <tr><td><b>Employment up, unemployment down</b></td><td>Unemployed people fill at least some of the new jobs, and the labour force does not grow by more</td></tr>
    <tr><td><b>Both up</b></td><td>The labour force grows faster than the number of jobs</td></tr>
    <tr><td><b>Unemployment down, no rise in employment</b></td><td>Unemployed people retire, enter full-time education, emigrate or stop looking</td></tr>
  </table></div>

  <h2>Why the labour force changes size</h2>
  <p>The labour force may grow if the <b>working-age population</b> rises, the <b>participation rate</b> rises, or both. The working-age population may rise because of a higher birth rate (after a long delay), a lower death rate or net immigration.</p>
  <p><b>Participation rate = labour force ÷ working-age population × 100.</b> Those in the labour force are <b>economically active</b>. Those of working age outside it, such as early retirees, students, homemakers and the long-term sick, are <b>economically inactive</b>.</p>
  <div class="tw"><table class="t">
    <tr><th>Influence on participation</th><th>Likely effect</th></tr>
    <tr><td>Wages</td><td>Higher wages may draw more people into work and keep some working past the usual retirement age</td></tr>
    <tr><td>Attitudes to women working</td><td>Greater acceptance may raise participation</td></tr>
    <tr><td>Care for children and the elderly</td><td>More nursery and care places may free carers to work</td></tr>
    <tr><td>Attitudes and provision for disabled workers</td><td>Acceptance and access, such as wheelchair ramps, may widen the labour force</td></tr>
    <tr><td>School leavers entering higher education</td><td>Participation may fall, but the quality of the labour force may rise</td></tr>
  </table></div>
'''
explore = '''
  <h2>Lab 1 · Jobs and the labour force</h2>
  <p>Change the number employed and the size of the labour force. Try to make both employment and unemployment rise, then make unemployment fall without any new jobs.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Employed</small><strong id="ea1"></strong></div><div><small>Unemployed</small><strong id="ea2"></strong></div><div><small>Labour force</small><strong id="ea3"></strong></div><div><small>Unemployment rate</small><strong id="ea4"></strong></div></div><div class="verdict" id="eav"></div></div></div></div>

  <h2>Lab 2 · Size of the labour force</h2>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>Labour force</small><strong id="pa1"></strong></div><div><small>Economically inactive</small><strong id="pa2"></strong></div></div><div class="verdict" id="pav"></div></div></div></div>

  <h2>Lab 3 · What changes the labour force?</h2>
  <div class="card"><div class="row" id="faBtns"></div><div id="faOut"></div></div>
'''

def pts(q, points):
    """one block per marked point"""
    body = "".join(f'<div class="pt"><b class="ph">Point {i} · {m} marks</b>{mk(t)}</div>' for i, (m, t) in enumerate(points, 1))
    return q.replace('<div class="ans">@</div>', f'<div class="ans pts">{body}</div>')

ex = "<p>These are our own practice questions on extension content.</p>\n  " + KEYL + "\n" + exam(
    Q(1, "Define", 2, "What is meant by the labour force participation rate?", "Two ideas: the labour force, and the working-age population.",
      "[K|It is the proportion of the working-age population] [K|that is in the labour force, either employed or unemployed.]", warn="Dividing by the total population."),
    Q(2, "Calculate", 2, "A country has a working-age population of 60 million, with 36 million employed and 3 million unemployed. Calculate the participation rate.", "Find the labour force first and show the working.",
      "[A|Labour force = 36 + 3 = 39 million.] [A|Participation rate = 39 ÷ 60 × 100 = 65%.]", warn="Leaving out the unemployed."),
    pts(Q(3, "Explain", 4, "Explain two reasons why the proportion of women in employment may rise.", "Two reasons, each with a developed link.", "@"), [
        (2, "[K|Social attitudes to women working may change.] [N|If paid work is more widely accepted, more women are likely to look for jobs and be hired.]"),
        (2, "[K|More childcare places may become available.] [N|Parents who looked after children at home could then take paid work.]")]),
    Q(4, "Explain", 4, "Explain how unemployment could fall even though no new jobs are created.", "Think about the ways people leave the labour force.",
      "[K|Unemployment counts only people in the labour force who are without work.] [N|If some unemployed people retire or start full-time education, they leave the labour force and are no longer counted.] [N|Others may emigrate or give up looking.] [A|For example, if 2 million jobseekers enrol on full-time courses, unemployment could fall by 2 million with employment unchanged.]", warn="Assuming every fall in unemployment means more jobs."),
    Q(5, "Analyse", 6, "Analyse how economic development may change the pattern of employment.", "Build chains: sectors, job quality, formal work.",
      "[K|Development tends to move workers from the primary sector to the secondary and then the tertiary sector.] [N|Machinery may raise productivity in farming, so fewer workers are needed to grow food.] [N|Higher incomes are likely to raise demand for manufactured goods and then for services, so firms in these sectors hire more.] [N|Better education may help workers move into skilled jobs, raising the share of high quality employment.] [N|More firms may also operate in the formal economy, giving more workers legal protection.] [A|A farm worker's child might train and work in banking or tourism.]", warn="Listing changes without explaining why they happen.", key=False),
    Q(6, "Discuss", 8, "Discuss whether or not a rise in self-employment benefits an economy.", "Both sides, then a judgement that depends on something.",
      "[K|Self-employed people work for themselves.] [N|A rise could benefit the economy if people start successful businesses, adding output and competition and perhaps later employing others.] [N|Their rewards depend on their own effort, which may raise productivity.] [N|On the other hand, many may work in the informal economy with low pay, little training and no protection.] [N|Tax revenue could be lower if earnings go unrecorded, and some may be self-employed only because they cannot find a job.] [E|Overall, the benefit is likely to depend on why people become self-employed. A rise in skilled, registered businesses may help growth, whereas a rise in casual survival work may signal a shortage of jobs.]", warn="One-sided answers, or ending without a judgement."),
    intro=False)
ex = ex.replace("<h2>Exam-style questions</h2>\n", "").replace("<p>These are", "<h2>Exam-style questions</h2>\n  <p>These are", 1)

tp = tips([
    ("Know it is extension.", "Not a set topic for 2027–29, but the examples can support answers on development, unemployment and supply-side policy."),
    ("Employment is not the mirror image of unemployment.", "Check what happened to the labour force."),
    ("Numbers or rates?", "Say whether data show people or percentages."),
    ("Divide by the right group.", "Participation: working-age population. Unemployment rate: labour force."),
    ("Say why the pattern changed.", "Attitudes, incomes, technology, competition or government policy."),
], cmds("Define", "Calculate", "Explain", "Analyse", "Discuss"))

body = page("IGCSE Economics · 0455 · 4.6 Extension", TITLE, "How who works, where and on what terms changes, and why employment and unemployment can move together. Coursebook Chapter 30; not in the 2027–29 syllabus.",
    learn=learn, watch=watch(("Moving between sectors", "stS"), ("Employment and unemployment", "stE"), ("Flexible employment", "stF")), explore=explore,
    practise=practise(("Which pattern?", "cl1", "card"), ("Formal or informal?", "cl2", "card"), ("Participation up or down?", "cl3", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Vietnam and the Netherlands", "The coursebook reports that in 2017 about 48% of Vietnam's workers were in the primary sector, while about 82% of workers in the Netherlands were in services.", "Contrasting employment structures at different stages of development."),
        rw("Australia's shift to private employers", "The coursebook reports that the public sector's share of Australian workers fell from 21% in 2000 to 15% in 2016.", "A change in the public and private pattern of employment."),
        rw("Participation compared", "The coursebook gives 2016 participation rates of 71% in New Zealand, 62.6% in the USA (down from 67.3% in 2000) and 52% in Pakistan.", "Differences may reflect attitudes, care provision and years in education.")),
    exam=ex, tips=tp)
(D / "em6.css").write_text(".pts{padding:2px 14px}.pt{padding:9px 0;border-top:1px dashed var(--line)}.pt:first-child{border-top:0}.ph{display:block;font:700 .7rem var(--sans);text-transform:uppercase;letter-spacing:.05em;color:var(--accent);margin-bottom:3px}\n")
write("em6", body, js, TITLE, "ig-employment-patterns-extension")
