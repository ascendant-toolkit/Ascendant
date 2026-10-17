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

function chainDraw(nodes, k) {
  const H = 40, G = 16; let o = "";
  nodes.forEach((t, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const y = 8 + i * (H + G);
    o += SV.rect(30, y, 700, H, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.55 * v) }) + SV.text(380, y + 25, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
    if (i > 0) o += SV.poly([[373, y - 10], [387, y - 10], [380, y - 2]], "dot4", op(v));
  });
  return o;
}
function chainStep(el, label, nodes, caps) {
  Lib.stepper($(el), { w: 760, h: 16 + nodes.length * 56, label, base: { k: 0 }, draw: (s) => chainDraw(nodes, s.k), tween: 700, dwell: 5200, steps: nodes.map((n, i) => ({ cap: caps[i], s: { k: i + 1 } })) });
}
function chooser(p, items, tmpl, lab = "Strength of the case") {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, lab + ": " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}

function pick(id, items, render) {
  const B = $("#" + id + "B"), O = $("#" + id + "O");
  B.innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t.label}</button>`).join("");
  const show = (i) => { $$("button", B).forEach((b, k) => b.classList.toggle("pri", k === i)); O.innerHTML = render(items[i]); };
  $$("button", B).forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}
const scoreBar = (m, max) => `<div style="background:var(--soft);border-radius:7px;height:14px;margin:6px 0 2px"><div class="bar ${m === max ? "b3" : m === 0 ? "b2" : "b4"}" style="width:${Math.max(2, (m / max) * 100)}%"></div></div><small>${m} of ${max} marks</small>`;

$("#pic1").innerHTML = (() => {
  const B = [["Read", "3 min", "Names, numbers, instructions", 20, "f1", 100], ["Plan", "2 min", "One checklist line per bullet", 130, "f3", 120], ["Write", "20 min", "Requirement by requirement, with comments", 260, "f2", 330], ["Check", "5 min", "Tick every bullet", 600, "f1", 140]];
  let o = ""; B.forEach(([n, t, d, x, c, w]) => { o += SV.rect(x, 12, w, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + w / 2, 40, n, "lbl bd", { "text-anchor": "middle", style: "font-size:15px" }) + SV.text(x + w / 2, 62, t, "sm", { "text-anchor": "middle" }) + SV.text(x + w / 2, 84, d.length > Math.floor(w / 6.2) ? d.slice(0, Math.floor(w / 6.2)) + "…" : d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 114" role="img" aria-label="Plan for the 30 minutes of the scenario question">${o}</svg>`;
})();
chainStep("#stA", "Planning the scenario", ["Read to the end: note RiderName[], RiderTime[], BadgeName[], 60 riders, 900 seconds", "Write one checklist line per bullet: twice and match; sort both; top three; store names; count", "Choose the technique for each line: loop, nested loops, selection, counter and second array", "Write in the order of the list, a comment above each part, a message on every input and output"], [
  "<b>Read:</b> the names and numbers you will use.", "<b>Checklist:</b> this is the mark scheme in your own words.", "<b>Techniques:</b> the mark scheme lists these beside each requirement.", "<b>Write:</b> the order of the list is the order of the program."]);
chainStep("#stC", "One requirement turned into marks", ["Requirement: store the names of riders who earn a badge in BadgeName[]", "Technique: a loop with selection and a counter that has its own index in the second array", "Code: IF RiderTime[Index] < 900 THEN BadgeCount ← BadgeCount + 1, BadgeName[BadgeCount] ← RiderName[Index]", "Marks: an appropriate technique and data stored in the structure (AO2); a comment and sensible names (AO3)"], [
  "<b>Requirement:</b> taken straight from a bullet.", "<b>Technique:</b> iteration, selection, counting.", "<b>Code:</b> the counter is separate from Index.", "<b>Marks:</b> AO2 for technique and data, AO3 for clarity and a requirement met."]);

/* ---- parallel arrays sort animation ---- */
const PF = [
  { n: ["Ana", "Ben", "Cal"], t: [95, 80, 88], hl: [], note: "Each rider's name and time sit at the same index." },
  { n: ["Ana", "Ben", "Cal"], t: [80, 95, 88], hl: [0, 1], bad: true, note: "Only the times were swapped. Ana now has 80 and Ben has 95: the pairing is broken." },
  { n: ["Ben", "Ana", "Cal"], t: [80, 95, 88], hl: [0, 1], note: "Swap the names too. Ben 80, Ana 95: the pairs are kept." },
  { n: ["Ben", "Cal", "Ana"], t: [80, 88, 95], hl: [1, 2], note: "Compare 95 and 88: swap both arrays again." },
  { n: ["Ben", "Cal", "Ana"], t: [80, 88, 95], hl: [], done: true, note: "Sorted. Index 1 holds the fastest rider, so RiderName[1] and RiderTime[1] give First." }
];
function pfDraw(s) {
  const f = PF[Math.max(0, Math.min(PF.length - 1, Math.round(s.i)))]; let o = SV.text(40, 40, "RiderName[]", "sm bd") + SV.text(40, 130, "RiderTime[]", "sm bd");
  [0, 1, 2].forEach((i) => {
    const x = 60 + i * 150, hl = f.hl.includes(i), c = hl ? (f.bad ? "f3" : "f1") : "f2";
    o += SV.rect(x, 52, 120, 44, c, { rx: 8, ...op(0.55) }) + SV.text(x + 60, 80, f.n[i], "lbl bd", { "text-anchor": "middle", style: "font-size:18px" });
    o += SV.rect(x, 142, 120, 44, c, { rx: 8, ...op(0.55) }) + SV.text(x + 60, 170, f.t[i], "lbl bd", { "text-anchor": "middle", style: "font-size:18px;font-family:var(--mono)" });
    o += SV.text(x + 60, 112, "index " + (i + 1), "sm", { "text-anchor": "middle" });
  });
  return o;
}
Lib.stepper($("#stB"), { w: 560, h: 210, label: "Sorting two parallel arrays together", base: { i: 0 }, draw: pfDraw, tween: 300, dwell: 4800, steps: PF.map((f, i) => ({ cap: "<b>" + (i === 1 ? "Wrong" : i === 4 ? "Done" : i === 0 ? "Start" : "Right") + ":</b> " + f.note, s: { i } })) });

/* ---- scenario decomposer ---- */
pick("sc", [
  { label: "Running club (Oct/Nov 2024, 21)", s: "1D arrays MemberName[], MemberTime[], MemberCertificate[], Position[]; variables such as ClubSize, TempTime, TempName, Swap, Count", r: [["R1", "Input and verify each member's time", "input, iteration"], ["R2", "Sort both arrays into ascending order of time and output the top three", "nested iteration, sorting, selection, output"], ["R3", "Store the names of members who get a certificate and output the number", "iteration, selection, counting, output"]], m: "One member only, not 200; the arrays not used or no index; a sort with one loop; the min/max method used once not three times; names not stored in the array given" },
  { label: "House rooms (Oct/Nov 2024, 22)", s: "1D array Rooms[], 2D array Dimensions[], variable Number", r: [["R1", "Input and store the number of rooms (validated), the names and the dimensions", "input with prompts, nested iteration, 1D and 2D arrays, validation"], ["R2", "Calculate and store the areas, total and average (rounded); find the smallest and largest", "calculation, totalling, rounding, maximum and minimum, iteration"], ["R3", "Output the results including the contents of the arrays", "iteration, output"]], m: "Declaring arrays and variables without need; maximum, minimum and totals not initialised" },
  { label: "Theatre seats (Oct/Nov 2023, 21)", s: "2D array Evening[1:10, 1:20]; variables Counter, SeatCounter, NumSeats, Row, Column", r: [["R1", "Find the number of seats available for each performance and output it", "searching, nested iteration, output"], ["R2", "Input and validate the number of seats", "input, iteration, selection"], ["R3", "Check whether seats are available and book them", "selection, assignment, output with appropriate messages"]], m: "No nested loop and not using the 2D array; output states only the seats booked, not whether seats were available" }
], (it) => `<p><small>Data structures named</small><br>${it.s}</p><div class="tw"><table class="t"><tr><th></th><th>Requirement</th><th>Technique the mark scheme lists</th></tr>${it.r.map((r) => `<tr><td><b>${r[0]}</b></td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join("")}</table></div><div class="verdict"><b>What the reports say was missed:</b> ${it.m}.</div>`);

/* ---- band estimator ---- */
const A2L = [["io", "Uses input and output"], ["loop", "Uses a loop to handle every item"], ["sel", "Uses selection to decide"], ["ct", "Uses counting or totalling"], ["ns", "Sorts or searches with nested iteration (if the scenario needs it)"], ["ver", "Verifies or validates input in a loop (if the scenario needs it)"], ["arr", "Uses the arrays or variables the scenario names"], ["all", "Stores all the data the scenario asks for"], ["cov", "Meets every requirement with an appropriate technique"]];
$("#a2").innerHTML = A2L.map(([k, t]) => `<label style="display:block;margin:5px 0"><input type="checkbox" data-k="${k}"> ${t}</label>`).join("");
$("#a3").innerHTML = `<label style="display:block;margin:5px 0">Comments <select id="cm"><option value="0">none</option><option value="1">some</option><option value="2">every part</option></select></label>
<label style="display:block;margin:5px 0">Identifiers <select id="id"><option value="0">few meaningful</option><option value="1">some</option><option value="2">most</option><option value="3">all, including data structures</option></select></label>
<label style="display:block;margin:5px 0">Requirements met <select id="rq"><option value="0">none</option><option value="1">at least one</option><option value="2">most</option><option value="3">all</option></select></label>
<label style="display:block;margin:5px 0"><input type="checkbox" id="lg"> In a logical order</label><label style="display:block;margin:5px 0"><input type="checkbox" id="ac"> Accurate: it works</label>`;
function band() {
  const t = {}; $$("#a2 input").forEach((c) => (t[c.dataset.k] = c.checked));
  const tech = ["loop", "sel", "ct", "ns", "ver"].filter((k) => t[k]).length, any = Object.values(t).some(Boolean);
  const a2 = !any ? [0, "0"] : t.all && t.cov && t.arr ? [8, "7 to 9"] : tech >= 2 && t.arr ? [5, "4 to 6"] : [2, "1 to 3"];
  const cm = +$("#cm").value, idv = +$("#id").value, rq = +$("#rq").value, lg = $("#lg").checked, ac = $("#ac").checked;
  const a3 = cm === 2 && idv === 3 && rq === 3 && lg && ac ? [6, "5 to 6"] : cm >= 1 && idv >= 2 && rq >= 2 ? [4, "3 to 4"] : (rq >= 1 || cm >= 1 || idv >= 1) ? [1, "1 to 2"] : [0, "0"];
  $("#b2").textContent = a2[1]; $("#b3").textContent = a3[1]; $("#bt").textContent = (a2[0] + a3[0]) + " approx.";
  const nextA = a2[1] === "7 to 9" ? "AO2 is in the top band." : a2[1] === "4 to 6" ? "To reach AO2 7 to 9, cover every requirement and store all the data in the structures the scenario names." : a2[1] === "1 to 3" ? "To reach AO2 4 to 6, apply at least two techniques to the scenario and use the arrays it names." : "Write something: any input, selection, loop or output earns credit.";
  const nextB = a3[1] === "5 to 6" ? "AO3 is in the top band." : a3[1] === "3 to 4" ? "To reach AO3 5 to 6, comment every part, use meaningful names throughout, put it in a logical order and make it work." : a3[1] === "1 to 2" ? "To reach AO3 3 to 4, add comments, name most things well and meet most of the requirements." : "Attempt at least one requirement.";
  $("#bv").textContent = nextA + " " + nextB;
}
$$("#a2 input, #a3 input, #a3 select").forEach((e) => e.addEventListener("input", band)); band();

function pl() {
  if (!$("#rd") || !$("#ck")) return;
  const rd = +$("#rd").value, ck = +$("#ck").value, wr = 30 - rd - ck;
  $("#r1").textContent = wr + " min"; $("#r2").textContent = Lib.fmtN(wr / 3, 1) + " min";
  $("#rv").textContent = `${rd} minutes reading and planning and ${ck} minutes checking leave ${wr} minutes to write, about ${Lib.fmtN(wr / 3, 1)} minutes for each of three requirements. ` + (wr / 3 < 6 ? "That is tight: the writing will have to be fast." : wr / 3 > 8 ? "Plenty of time: do not skip the check." : "A workable balance.");
  const W = 380, X = (v) => 20 + (v / 30) * W;
  $("#labA").innerHTML = SV.rect(X(0), 70, X(rd) - X(0), 50, "f1", op(0.5)) + SV.rect(X(rd), 70, X(rd + wr) - X(rd), 50, "f2", op(0.5)) + SV.rect(X(rd + wr), 70, X(30) - X(rd + wr), 50, "f3", op(0.5)) + SV.text(X(rd / 2), 100, rd, "sm", { "text-anchor": "middle" }) + SV.text(X(rd + wr / 2), 100, "Write: " + wr, "sm", { "text-anchor": "middle" }) + SV.text(X(rd + wr + ck / 2), 100, ck, "sm", { "text-anchor": "middle" }) + SV.text(210, 150, "30 minutes", "sm", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "rd", label: "Minutes reading and planning ", min: 2, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: pl });
Lib.slider($("#g2"), { id: "ck", label: "Minutes checking ", min: 2, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: pl });
pl();
Lib.classify($("#cl1"), { prompt: "Which AO2 band does each feature describe?", buckets: [{"label": "Band 1 to 3"}, {"label": "Band 4 to 6"}, {"label": "Band 7 to 9"}], items: [{"text": "Uses input, selection and output only", "b": 0}, {"text": "Stores a value in a variable but not in the arrays given", "b": 0}, {"text": "More than one technique applied to the scenario", "b": 1}, {"text": "Uses some of the given structures and stores some of the data", "b": 1}, {"text": "Every requirement is met by an appropriate technique", "b": 2}, {"text": "The structures chosen store all the data the scenario requires", "b": 2}], done: "Low: some technique. Middle: several techniques, some data stored. Top: every requirement and all the data." });
Lib.classify($("#cl2"), { prompt: "Which AO3 band does each feature describe?", buckets: [{"label": "Band 1 to 2"}, {"label": "Band 3 to 4"}, {"label": "Band 5 to 6"}], items: [{"text": "No relevant comments", "b": 0}, {"text": "Attempts at least one requirement", "b": 0}, {"text": "Some relevant comments", "b": 1}, {"text": "The majority of identifiers are appropriately named", "b": 1}, {"text": "Meets most of the requirements", "b": 1}, {"text": "Fully commented", "b": 2}, {"text": "Meaningful names throughout, including all data structures", "b": 2}, {"text": "In a logical order and accurate", "b": 2}, {"text": "Meets all the requirements", "b": 2}], done: "Comments, names, accuracy and requirements all move up together." });
Lib.order($("#o1"), { prompt: "Put the 30-minute plan in order.", items: ["Read the scenario to the end", "Write a checklist line for each requirement", "Write the program one requirement at a time, with comments", "Check each requirement against the code"], done: "Read, checklist, write, check." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["You do not need to declare any arrays", "Use them without declaring them"], ["All inputs and outputs must contain suitable messages", "Put a prompt before each input and a message with each output"], ["Add comments to explain how your code works", "Comment each part of the solution"], ["Names are stored in the array MemberName[]", "Use that array, with that name"], ["Use pseudocode or program code", "Pseudocode, Python, Visual Basic or Java"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "The scenario question is 15 marks with AO2 worth 9. What percentage of its marks is AO2?", "a": 60, "unit": "%", "tol": 0.5, "hint": "9 ÷ 15.", "sol": "<b>60%</b>."},
  {"q": "You spend 3 minutes reading, 2 minutes planning and 5 minutes checking in a 30-minute question. How many minutes are left for writing?", "a": 20, "unit": "min", "tol": 0.1, "hint": "30 − 10.", "sol": "<b>20 minutes</b>."},
  {"q": "A bubble sort on 60 riders needs at most how many passes?", "a": 59, "unit": "", "tol": 0.01, "hint": "n − 1.", "sol": "<b>59</b>."},
  {"q": "Five rooms have areas totalling 126.5 m². What is the average area, rounded to 2 decimal places?", "a": 25.3, "unit": "m²", "tol": 0.005, "hint": "126.5 ÷ 5.", "sol": "<b>25.30</b>."},
  {"q": "With 21 minutes for writing three requirements, how many minutes does each get?", "a": 7, "unit": "min", "tol": 0.05, "hint": "21 ÷ 3.", "sol": "<b>7 minutes</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does the syllabus suggest for the time on the 15-mark scenario question?", opts: ["10 minutes", "20 minutes", "30 minutes", "45 minutes"], a: 2, why: "About 30 minutes." },
  { q: "The scenario says 'you do not need to declare any arrays or variables'. What should you do?", opts: ["Declare them anyway", "Use them without declaring them, and initialise only what needs a starting value", "Not use them", "Ask the invigilator"], a: 1, why: "The reports say the time is better spent on the requirements." },
  { q: "Two arrays hold names and times for the same riders. When sorting by time, what must each swap do?", opts: ["Move the times only", "Move the names and the times together", "Move the names only", "Delete one array"], a: 1, why: "Otherwise the pairs are broken." },
  { q: "Which gets AO3 credit?", opts: ["Using a long program", "Comments and meaningful identifiers", "Using three languages", "A very short program"], a: 1, why: "AO3 rewards comments, names, logic and accuracy." },
  { q: "How should a second array of selected items be indexed?", opts: ["With the same Index as the first array", "With its own counter", "With a random number", "Not at all"], a: 1, why: "Its own counter avoids gaps." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Scenario question", "15 marks, about 30 minutes."],
  ["Marking", "AO2 out of 9, AO3 out of 6."],
  ["Plan", "Read, checklist, write, check."],
  ["Use the names", "Arrays and variables as described."],
  ["Do not declare", "If the question says it is not needed."],
  ["Initialise", "Totals, largest, smallest."],
  ["Comments", "Every part."],
  ["Messages", "Every input and output."],
] });
