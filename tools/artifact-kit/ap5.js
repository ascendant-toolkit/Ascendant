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

/* ---------- topic data ---------- */
const TOP = [["7", "Firms, costs and market structures", 47, "f1"], ["8", "Government, equity and labour", 17, "f2"], ["9", "The macroeconomy and money", 24, "f3"], ["10", "Macro policy", 9, "f2"], ["11", "International and development", 25, "f1"]];
const SUB = [["7.1", "Utility", 5], ["7.2", "Indifference curves and budget lines", 4], ["7.3", "Efficiency and market failure", 6], ["7.4", "Private and social costs and benefits, externalities", 7], ["7.5", "Costs, revenue and profit; short and long run", 10], ["7.6", "Different market structures", 5], ["7.7", "Growth and survival of firms", 5], ["7.8", "Differing objectives and policies of firms", 5], ["8.1", "Government policies for efficiency and market failure", 2], ["8.2", "Equity and redistribution of income and wealth", 5], ["8.3", "Labour market forces and intervention", 10], ["9.1", "The circular flow of income", 3], ["9.2", "Economic growth and sustainability", 6], ["9.3", "Employment and unemployment", 7], ["9.4", "Money and banking", 8], ["10.1", "Government macroeconomic policy objectives", 1], ["10.2", "Links between macroeconomic problems", 5], ["10.3", "Effectiveness of policy options", 3], ["11.1", "Policies to correct balance of payments disequilibrium", 3], ["11.2", "Exchange rates", 5], ["11.3", "Economic development", 4], ["11.4", "Countries at different levels of development", 3], ["11.5", "Relationships between countries at different levels", 7], ["11.6", "Globalisation", 3]];

/* ---------- bullets chart ---------- */
$("#pic1").innerHTML = (() => { let o = SV.line(70, 190, 730, 190) + SV.line(70, 190, 70, 20) + SV.text(76, 16, "Numbered syllabus bullets (122 in total)", "sm"); TOP.forEach(([n, l, v, c], i) => { const x = 110 + i * 125, h = v * 3.2; o += SV.rect(x, 190 - h, 70, h, c, op(0.75)) + SV.text(x + 35, 210, "Topic " + n, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 35, 190 - h - 8, v, "lbl bd", { "text-anchor": "middle" }); }); return `<svg viewBox="0 0 760 225" role="img" aria-label="Syllabus bullets by topic: topic 7 has 47, topic 8 has 17, topic 9 has 24, topic 10 has 9 and topic 11 has 25">${o}</svg>`; })();

/* ---------- three phases stepper ---------- */
const PX = (w) => 70 + w * 6.6;
function phDraw(s) {
  let o = SV.line(70, 150, 730, 150) + SV.text(70, 28, "Start", "sm") + SV.text(730, 28, "Exam", "sm", { "text-anchor": "end" });
  const blk = (a, b, c, l, sub, k) => (k > 0 ? SV.rect(PX(a), 60, PX(b) - PX(a), 76, c, op(0.65 * k)) + SV.text((PX(a) + PX(b)) / 2, 92, l, "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text((PX(a) + PX(b)) / 2, 112, sub, "sm", { "text-anchor": "middle", ...op(k) }) : "");
  o += blk(0, 40, "f1", "1 · Rebuild", "about 40%", s.a) + blk(40, 80, "f3", "2 · Practise", "about 40%", s.b) + blk(80, 100, "f2", "3 · Perform", "20%", s.c);
  if (s.d > 0) o += tag(400, 200, "Spaced reviews of earlier topics run through all three phases.", "t4", s.d, "middle") + SV.line(PX(0), 176, PX(100), 176, "c4 dash", op(s.d));
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 230, label: "Three revision phases: rebuild, practise, perform", base: { a: 0, b: 0, c: 0, d: 0 }, draw: phDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Phase 1 · Rebuild.</b> Cover each topic: read the lesson, close the book, write what you remember, draw each diagram and make flashcards for what you missed.", s: { a: 1 } },
  { cap: "<b>Phase 2 · Practise.</b> Answer past questions by topic, untimed first, then timed. Mark them with the mark scheme and keep an error log.", s: { a: 1, b: 1 } },
  { cap: "<b>Phase 3 · Perform.</b> Full timed papers under exam conditions, then fix the weaknesses they expose. Rehearse the exam-day routine.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Throughout.</b> Review earlier topics at growing gaps so you do not forget phase 1 by the time you reach phase 3.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Planner ---------- */
function labPlan() {
  if (!$("#wk") || !$("#hr") || !$("#rc") || TOP.some((t, i) => !$("#cf" + i))) return;
  const wk = +$("#wk").value, hr = +$("#hr").value, rc = +$("#rc").value / 100, total = wk * hr, recap = total * rc, pool = total - recap;
  const conf = TOP.map((t, i) => +$("#cf" + i).value), w = TOP.map((t, i) => t[2] * (6 - conf[i])), sw = w.reduce((a, b) => a + b, 0), hrs = w.map((x) => pool * x / sw);
  $("#r1").textContent = Lib.fmtN(total, 0) + " h"; $("#r2").textContent = Lib.fmtN(pool, 0) + " h"; $("#r3").textContent = Lib.fmtN(total * 0.4, 0) + " / " + Lib.fmtN(total * 0.4, 0) + " / " + Lib.fmtN(total * 0.2, 0);
  const top = hrs.indexOf(Math.max(...hrs));
  $("#rv").textContent = `${wk} weeks at ${hr} hours is ${Lib.fmtN(total, 0)} hours. Setting aside ${Lib.fmtN(recap, 0)} hours for an AS recap leaves ${Lib.fmtN(pool, 0)} hours for topics 7 to 11. Topic ${TOP[top][0]} gets the most (${Lib.fmtN(hrs[top], 0)} hours) because of its size and your confidence rating. As a guide, that is about ${Lib.fmtN(pool / wk, 1)} hours of A Level topic study each week, with the first 40% of the time for rebuilding, the next 40% for practice and the last 20% for timed papers. Move the confidence sliders as your practice results change.`;
  const Y = (v) => 300 - v * (240 / Math.max(10, ...hrs)); let o = SV.line(40, 300, 410, 300) + SV.line(40, 300, 40, 24) + SV.text(46, 16, "Hours", "sm");
  TOP.forEach(([n, l, v, c], i) => { const x = 55 + i * 70, yy = Y(hrs[i]); o += SV.rect(x, yy, 52, 300 - yy, c, op(0.75)) + SV.text(x + 26, 320, "Topic " + n, "sm", { "text-anchor": "middle" }) + tag(x + 26, yy - 6, Lib.fmtN(hrs[i], 0), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "wk", label: "Weeks until the exam ", min: 4, max: 24, step: 1, value: 12, fmt: (v) => v, onInput: labPlan });
Lib.slider($("#g2"), { id: "hr", label: "Study hours a week for economics ", min: 3, max: 16, step: 1, value: 6, fmt: (v) => v, onInput: labPlan });
Lib.slider($("#g3"), { id: "rc", label: "Share of time for the AS recap, % ", min: 5, max: 35, step: 5, value: 15, fmt: (v) => v + "%", onInput: labPlan });
[["g4", 0], ["g5", 1], ["g6", 2], ["g7", 3], ["g8", 4]].forEach(([g, i]) => Lib.slider($("#" + g), { id: "cf" + i, label: "Confidence, topic " + TOP[i][0] + ": " + TOP[i][1] + " ", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labPlan }));
labPlan();

/* ---------- Topic tracker ---------- */
function saveGet() { try { return JSON.parse(localStorage.getItem("econ-revision-tracker") || "{}"); } catch (e) { return {}; } }
function saveSet(o) { try { localStorage.setItem("econ-revision-tracker", JSON.stringify(o)); } catch (e) {} }
(function () {
  const st = saveGet(), box = $("#trk"); if (!box) return;
  const row = (s, i) => { const slug = "s" + s[0].replace(".", "-"); return `<tr><td><b>${s[0]}</b></td><td><a href="../../a-econ/a-level/${slug}/">${s[1]}</a></td><td style="text-align:center">${s[2]}</td><td><select class="rag" data-id="${s[0]}" aria-label="Rating for ${s[0]}"><option value="">–</option><option value="R">R</option><option value="A">A</option><option value="G">G</option></select></td></tr>`; };
  box.innerHTML = `<div class="tw"><table class="t"><tr><th>Topic</th><th>Title (lesson page)</th><th>Bullets</th><th>Rating</th></tr>${SUB.map(row).join("")}</table></div>`;
  const upd = () => { let g = 0, a = 0, gb = 0, tb = 0; SUB.forEach((s) => { tb += s[2]; const v = st[s[0]]; if (v === "G") { g++; gb += s[2]; } else if (v === "A") a++; }); $("#k1").textContent = g; $("#k2").textContent = a; $("#k3").textContent = 24 - g - a; $("#kv").textContent = g + a === 0 ? "Rate the topics to see where to focus." : `${Lib.fmtN(gb / tb * 100, 0)}% of the syllabus bullets are in topics you rate green. Start with the red or unrated ones that have the most bullets: ` + (SUB.filter((s) => st[s[0]] !== "G" && st[s[0]] !== "A").sort((x, y) => y[2] - x[2]).slice(0, 3).map((s) => s[0]).join(", ") || "none, well done") + "."; };
  $$(".rag", box).forEach((sel) => { sel.value = st[sel.dataset.id] || ""; sel.onchange = () => { st[sel.dataset.id] = sel.value; saveSet(st); upd(); }; });
  upd();
})();

/* ---------- Forgetting curve ---------- */
function labF() {
  if (!$("#nr") || !$("#mm")) return;
  const nr = +$("#nr").value, m = +$("#mm").value / 10, days = [1, 3, 7, 14, 28].slice(0, nr);
  const ret = (t, rev) => { let S = 1.5, last = 0; rev.forEach((d) => { if (d <= t) { S *= m; last = d; } }); return Math.exp(-(t - last) / S); };
  $("#t1").textContent = Lib.fmtN(ret(30, []) * 100, 0) + "%"; $("#t2").textContent = Lib.fmtN(ret(30, days) * 100, 0) + "%"; $("#t3").textContent = days.length ? days.join(", ") : "none";
  $("#tv").textContent = nr === 0 ? "With no reviews you keep very little after a month. Cramming the night before gives a short boost that fades quickly." : `With reviews on day ${days.join(", ")} the memory lasts much longer each time. By day 30 you retain about ${Lib.fmtN(ret(30, days) * 100, 0)}%, against ${Lib.fmtN(ret(30, []) * 100, 0)}% with no review. This is a simplified model, but real experiments show the same pattern: spaced practice beats massed practice.`;
  const X = (t) => 40 + t * 8, Y = (v) => 270 - v * 240; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 292, "Days", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Memory strength", "sm");
  const p0 = [], p1 = []; for (let t = 0; t <= 45; t += 0.5) { p0.push([X(t), Y(ret(t, []))]); p1.push([X(t), Y(ret(t, days))]); }
  o += SV.path(Lib.ptsPath(p0), "c2 dash", op(0.6)) + SV.path(Lib.ptsPath(p1), "c1"); days.forEach((d) => (o += SV.line(X(d), 270, X(d), 30, "c4 dash", op(0.45)) + SV.text(X(d), 286, "R", "sm", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g9"), { id: "nr", label: "Number of reviews (days 1, 3, 7, 14, 28) ", min: 0, max: 5, step: 1, value: 4, fmt: (v) => v, onInput: labF });
Lib.slider($("#g10"), { id: "mm", label: "How much each review strengthens memory × 10 ", min: 15, max: 35, step: 1, value: 23, fmt: (v) => "×" + (v / 10).toFixed(1), onInput: labF });
labF();

/* ---------- Last week checklist ---------- */
const CK = [["T−7", "Sit a full timed Paper 4 and mark it with the mark scheme"], ["T−6", "Fix the errors from that paper; update the error log"], ["T−5", "Sit a full timed Paper 3 (75 minutes) and mark it"], ["T−5", "Redraw every diagram on your list from memory"], ["T−4", "Recall session on your amber and red topics only"], ["T−3", "Re-do wrong questions; write three 5-minute essay plans"], ["T−3", "Make a one-page sheet of formulas and key definitions"], ["T−2", "Light recall of all topics; no new papers"], ["T−1", "Read the formula and diagram sheet once; pack your bag; sleep early"], ["Exam", "Read the whole paper first; plan your time; answer every question"]];
(function () {
  const box = $("#chk"); if (!box) return; let st = {}; try { st = JSON.parse(localStorage.getItem("econ-revision-check") || "{}"); } catch (e) {}
  box.innerHTML = `<div class="tw"><table class="t"><tr><th>When</th><th>Do this</th><th>Done</th></tr>${CK.map((c, i) => `<tr><td><b>${c[0]}</b></td><td>${c[1]}</td><td style="text-align:center"><input type="checkbox" data-i="${i}" aria-label="Done: ${c[1]}"></td></tr>`).join("")}</table></div>`;
  $$("input[type=checkbox]", box).forEach((cb) => { cb.checked = !!st[cb.dataset.i]; cb.onchange = () => { st[cb.dataset.i] = cb.checked; try { localStorage.setItem("econ-revision-check", JSON.stringify(st)); } catch (e) {} }; });
})();

/* ---------- Paper 4 plan ---------- */
const QX = (m) => 70 + m * 5.5;
function p4Draw(s) {
  let o = SV.line(70, 150, 730, 150) + SV.text(70, 28, "0", "sm") + SV.text(730, 28, "120 min", "sm", { "text-anchor": "end" });
  [0, 30, 60, 90, 120].forEach((m) => (o += SV.line(QX(m), 144, QX(m), 156) + SV.text(QX(m), 176, m, "sm", { "text-anchor": "middle" })));
  const blk = (a, b, c, l, sub, k) => (k > 0 ? SV.rect(QX(a), 60, QX(b) - QX(a), 76, c, op(0.65 * k)) + SV.text((QX(a) + QX(b)) / 2, 92, l, "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text((QX(a) + QX(b)) / 2, 112, sub, "sm", { "text-anchor": "middle", ...op(k) }) : "");
  o += blk(0, 6, "f2", "Read", "6", s.a) + blk(6, 42, "f1", "Section A", "20 marks, 36 min", s.b) + blk(42, 78, "f3", "Section B", "20 marks, 36 min", s.c) + blk(78, 114, "f3", "Section C", "20 marks, 36 min", s.d) + blk(114, 120, "f2", "Check", "6", s.e);
  return o;
}
Lib.stepper($("#stX"), { w: 760, h: 215, label: "A 120 minute plan for Paper 4: read, Sections A, B and C, check", base: { a: 0, b: 0, c: 0, d: 0, e: 0 }, draw: p4Draw, tween: 700, dwell: 5600, steps: [
  { cap: "<b>Read, 6 minutes.</b> Read the whole paper. Choose your essays. Underline command words and marks.", s: { a: 1 } },
  { cap: "<b>Section A, 36 minutes.</b> The 20-mark data response, parts in order, with the biggest part last.", s: { a: 1, b: 1 } },
  { cap: "<b>Section B, 36 minutes.</b> A micro essay: plan 5 minutes, write about 30.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Section C, 36 minutes.</b> A macro essay with the same plan.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>Check, 6 minutes.</b> Diagrams labelled, every part answered, conclusions written.", s: { a: 1, b: 1, c: 1, d: 1, e: 1 } },
] });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is it active or passive revision?", buckets: [{"label": "Active"}, {"label": "Passive"}], items: [{"text": "Closing the book and writing everything you remember about the money market", "b": 0}, {"text": "Re-reading your notes three times", "b": 1}, {"text": "Answering past questions and marking them with the mark scheme", "b": 0}, {"text": "Highlighting a textbook chapter in four colours", "b": 1}, {"text": "Drawing a diagram from memory and labelling it", "b": 0}, {"text": "Copying out the lesson page word for word", "b": 1}, {"text": "Explaining the multiplier aloud to a friend", "b": 0}, {"text": "Watching a video without taking notes or pausing", "b": 1}], done: "Active methods make you produce answers. Passive methods only expose you to information." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Retrieval practice", "Testing yourself to recall information from memory"], ["Spaced review", "Revisiting topics at growing gaps"], ["Interleaving", "Mixing different topics in one practice session"], ["Error log", "A record of lost marks, the type of mistake and the fix"], ["Timed paper", "A past paper done under exam conditions"], ["Phase 3", "Full timed papers and fixing weaknesses"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the revision cycle in order.", items: ["Learn the topic from the lesson page", "Close the book and recall it", "Answer past questions on it", "Mark the answers and log the errors", "Review it again after a few days, then a week"], done: "Learn, recall, practise, review, repeat with growing gaps." });
Lib.calc($("#c1"), { qs: [
  {"q": "You have 12 weeks and study 6 hours a week. How many hours is that in total?", "a": 72, "unit": "h", "tol": 0.5, "hint": "12 × 6.", "sol": "<b>72 hours</b>."},
  {"q": "15% of those 72 hours go on an AS recap. How many hours are left for topics 7 to 11 (1 decimal place)?", "a": 61.2, "unit": "h", "tol": 0.1, "hint": "72 × 0.85.", "sol": "<b>61.2 hours</b>."},
  {"q": "Topic 7 has 47 of the 122 syllabus bullets. What percentage is that (1 decimal place)?", "a": 38.5, "unit": "%", "tol": 0.1, "hint": "47 ÷ 122.", "sol": "<b>38.5%</b>."},
  {"q": "Paper 4 lasts 120 minutes with 60 marks. How many minutes per mark (1 decimal place)?", "a": 2, "unit": "min", "tol": 0.05, "hint": "120 ÷ 60.", "sol": "<b>2.0 minutes per mark</b>, including reading and checking."},
  {"q": "Paper 3 has 30 questions in 75 minutes. How many minutes is that per question (1 decimal place)?", "a": 2.5, "unit": "min", "tol": 0.05, "hint": "75 ÷ 30.", "sol": "<b>2.5 minutes</b>, or about 100 seconds on a first pass."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is the best use of a past paper?", opts: ["Do it timed, mark it with the mark scheme and log your errors", "Read the questions and look at the answers", "Do it once in the last hour", "Skip the questions you are unsure about"], a: 0, why: "Timed practice, honest marking and an error log turn each paper into learning." },
  { q: "Why space your reviews out?", opts: ["It helps you remember for longer", "It saves time in total", "It stops you needing to practise questions", "It is easier"], a: 0, why: "Each review at a growing gap makes the memory last longer." },
  { q: "Which topic should get the most time, other things equal?", opts: ["The largest topic that you rate weak", "The smallest topic that you rate strong", "The topic you like most", "The topic you did last"], a: 0, why: "Size of syllabus and your weakness together set priorities." },
  { q: "What should you do in the last 24 hours?", opts: ["Light recall, check your sheet, sleep", "Start three new papers", "Study all night", "Learn new topics"], a: 0, why: "Rest and a calm routine help performance." },
  { q: "An error log is most useful when you:", opts: ["Review it weekly for repeated mistakes", "Never read it again", "Only note correct answers", "Use it to avoid hard questions"], a: 0, why: "Repeated mistakes show your priorities." },
  { q: "In Paper 4, how long should each 20-mark section take?", opts: ["About 36 minutes", "About 10 minutes", "About 60 minutes", "About 90 minutes"], a: 0, why: "Each section is worth a third of the marks; keep to time." },
  { q: "Which of these is passive?", opts: ["Highlighting your notes", "Drawing a diagram from memory", "Answering a past question", "Teaching a friend"], a: 0, why: "Highlighting does not make you retrieve anything." },
  { q: "What do you do first when the exam starts?", opts: ["Read the whole paper and plan your time", "Answer question 1 immediately", "Start the longest essay", "Draw diagrams"], a: 0, why: "Reading first lets you choose essays and set times." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Three phases", "Rebuild, practise, perform."],
  ["Time split", "About 40%, 40%, 20%."],
  ["Spaced review", "After 1 day, 3 days, 1 week, 2 weeks, 1 month."],
  ["Active revision", "Recall, past questions, diagrams, teaching."],
  ["Error log", "Question, mistake type, fix."],
  ["Paper 3", "75 minutes: 50 first pass, 16 second, 9 check."],
  ["Paper 4", "120 minutes: 6 read, 36 per section, 6 check."],
  ["Last 24 hours", "Light recall and sleep."],
] });
