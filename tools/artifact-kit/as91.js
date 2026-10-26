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

const bin = (n, w = 8) => n.toString(2).padStart(w, "0");
const hx = (n, w = 2) => n.toString(16).toUpperCase().padStart(w, "0");
const grp4 = (s) => s.replace(/(.{4})(?=.)/g, "$1 ");
const clamp01 = (v) => Math.max(0, Math.min(1, v));
/* row of boxes: items [{t, c, v}] t text, c fill class, v opacity */
function boxRow(items, x0, y, w = 64, h = 52, gap = 10, o = {}) {
  let s = "";
  items.forEach((it, i) => {
    const x = x0 + i * (w + gap), v = it.v === undefined ? 1 : it.v;
    if (v <= 0) return;
    s += SV.rect(x, y, w, h, it.c || "f3", { rx: 8, ...op(v * (it.c ? 0.55 : 0.18)) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) });
    s += SV.text(x + w / 2, y + h / 2 + 8, it.t, "lbl bd", { "text-anchor": "middle", style: "font-size:" + (o.fs || 22) + "px;font-family:var(--mono)", ...op(v) });
    if (it.top !== undefined) s += SV.text(x + w / 2, y - 8, it.top, "sm", { "text-anchor": "middle", ...op(v) });
    if (it.bot !== undefined) s += SV.text(x + w / 2, y + h + 18, it.bot, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return s;
}

/* memory cell: address on the left, value in the box */
function memCell(x, y, addr, val, cls = "f3", v = 1, w = 150, h = 40) {
  return SV.rect(x, y, w, h, cls, { rx: 6, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 6, fill: "none", ...op(v) }) +
    SV.text(x + 10, y + h / 2 + 6, String(addr), "sm", { style: "font-family:var(--mono)", ...op(v) }) +
    SV.text(x + w - 12, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono);font-size:17px", ...op(v) });
}
function regBox(x, y, name, val, cls = "f2", v = 1, w = 120, h = 46) {
  return SV.rect(x, y, w, h, cls, { rx: 8, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) }) +
    SV.text(x + 10, y - 7, name, "sm", op(v)) + SV.text(x + w / 2, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:19px", ...op(v) });
}
/* a list of code lines; hl is the highlighted index (or -1) */
function codeList(x, y, lines, hl, v = 1, lh = 30, w = 230) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 4, i === hl ? "cell-warn" : "cell", { rx: 4, ...op(v) }) + SV.text(x + 10, y + i * lh + 18, l, "lbl", { style: "font-family:var(--mono);font-size:14px;white-space:pre", ...op(v) })).join("");
}

(function () {
  const draw = (s) => { const k = Math.round(s.i); const items = ["car ID", "start date", "cost", "paint colour", "driver's music", "shoe size"]; let o = ""; items.forEach((t, i) => { const keep = i < 3; o += SV.rect(20 + (i % 3) * 170, 20 + Math.floor(i / 3) * 40, 150, 30, k >= 1 ? (keep ? "f1" : "cell") : "cell", { rx: 5, ...(k >= 1 && !keep ? op(0.3) : {}) }) + SV.text(95 + (i % 3) * 170, 40 + Math.floor(i / 3) * 40, t, "lbl", { "text-anchor": "middle", style: "font-size:12px" }); });
    o += SV.text(20, 125, ["a lot of information about each hire", "abstraction filters out what is not needed...", "...leaving the abstract model: easier to design and solve"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 520, h: 145, label: "Abstraction", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Lots of information could be recorded about a car hire.", "<b>Abstraction</b> filters out what the task does not need.", "The <b>abstract model</b> keeps car, date and cost."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const m = ["GetOverdueLoan()", "IdentifyStudent()", "GetStudentEmail()", "CreateEmail()", "SendEmail()"]; let o = SV.rect(150, 10, 220, 30, "f3", { rx: 6 }) + SV.text(260, 30, "Email students with overdue books", "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); m.forEach((t, i) => { if (k >= 1) o += SV.path(`M260,40 L${60 + i * 100},70`, "ax", { style: "opacity:.4" }) + SV.rect(5 + i * 100, 70, 96, 30, i < k ? "f1" : "cell", { rx: 5 }) + SV.text(53 + i * 100, 89, t, "lbl", { "text-anchor": "middle", style: "font-size:9.5px" }); });
    o += SV.text(20, 130, ["one big problem", "split into sub-problems", "each module named for what it does", "", ""][Math.min(k, 2)], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 520, h: 145, label: "Decomposition", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["One large problem.", "<b>Decomposition</b> splits it into sub-problems.", "Each one becomes a module...", "...with its own name and use.", "Each module can be coded and tested separately."].map((c, i) => ({ cap: c, s: { i: Math.min(i, 5) } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 170, 40, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 85, 65, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); let o = B(20, "SendEmail(student)", true) + B(300, "IsOverdue(loan)", k >= 1);
    o += SV.text(20, 110, ["a procedure does a task", "a function returns a value (TRUE or FALSE)", ""][Math.min(k, 2)], "lbl bd t3", { style: "font-size:13px" }); if (k >= 1) o += SV.text(300, 100, "returns TRUE", "sm"); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 130, label: "Procedure and function", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["A <b>procedure</b> carries out a task.", "A <b>function</b> returns a value."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const items = [["car ID", 1], ["customer ID", 1], ["start date", 1], ["return date", 1], ["cost", 1], ["car's colour", 0], ["customer's hobbies", 0], ["driver's music taste", 0]]; const sel = new Set(); const bar = $("#aB");
  const paint = () => { const ok = [...sel].filter((i) => items[i][1]).length, bad = [...sel].filter((i) => !items[i][1]).length; $("#aV").innerHTML = sel.size ? `You kept <b>${ok}</b> needed item(s)` + (bad ? ` and <b>${bad}</b> unnecessary one(s) that abstraction would filter out.` : ".") + (ok === 5 && !bad ? " That is the abstract model: only what the car hire task needs." : "") : "Click items to include them in the model."; };
  items.forEach(([t], i) => { const b = document.createElement("button"); b.textContent = t; b.onclick = () => { sel.has(i) ? sel.delete(i) : sel.add(i); b.className = sel.has(i) ? "on" : ""; paint(); }; bar.appendChild(b); }); paint();
})();
btnTable("dB", "dO", [
  ["Cinema booking", "SearchFilms(), SearchSeats(), CalculateCost(), BookSeats()", "Sub-problems of booking"],
  ["Charity donation app", "SelectCharity(), SpecifyAmount(), MakePayment(), ValidatePayment()", "Steps of a donation"],
  ["Loyalty card", "ScanCard(), GetPoints(), CalculatePoints(), UpdatePoints()", "Steps of a purchase"],
  ["Overdue book email", "GetOverdueLoan(), IdentifyStudent(), CreateEmail(), SendEmail()", "Steps to email a student"]
], ["Problem", "Modules", "Why"]);
btnTable("pB", "pO", [
  ["Display the discount on screen", "Procedure", "Does a task"],
  ["Calculate the cost of a booking and give it back", "Function", "Returns a value"],
  ["Check whether a seat is free (TRUE/FALSE)", "Function", "Returns a Boolean"],
  ["Send an email", "Procedure", "Does a task"]
], ["Module", "Type", "Why"]);
Lib.classify($("#cl1"), { prompt: "Abstraction or decomposition?", buckets: [{"label": "Abstraction"}, {"label": "Decomposition"}], items: [{"text": "Filtering out information that is not necessary", "b": 0}, {"text": "Breaking a problem into sub-problems", "b": 1}, {"text": "Leads to program modules", "b": 1}, {"text": "Keeps only the data needed for the task", "b": 0}, {"text": "Makes the problem easier to solve by removing detail", "b": 0}, {"text": "Assigns parts of a problem to different teams", "b": 1}], done: "Abstraction removes; decomposition splits." });
Lib.classify($("#cl2"), { prompt: "For a car hire system, is the item needed in the abstract model?", buckets: [{"label": "Needed"}, {"label": "Not needed"}], items: [{"text": "Start date of hire", "b": 0}, {"text": "The car's paint colour", "b": 1}, {"text": "Customer ID", "b": 0}, {"text": "The customer's favourite music", "b": 1}, {"text": "Cost of hire", "b": 0}, {"text": "The driver's shoe size", "b": 1}], done: "Keep only what the task needs." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Abstraction", "Filtering out unnecessary information"], ["Decomposition", "Breaking a problem into sub-problems"], ["Module", "A procedure or function that does one part of the job"], ["Function", "A module that returns a value"], ["Abstract model", "A simplified version holding only the needed data"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the decomposition steps in order.", items: ["State the whole problem", "Break it into sub-problems", "Give each sub-problem a module name and a use", "Code and test each module separately", "Combine the modules into the program"], done: "Problem, split, name, test, combine." });
Lib.calc($("#c1"), { qs: [
  {"q": "A program is split into 6 modules. Four programmers each take an equal share of 6 modules as evenly as possible; at most how many modules does one programmer have?", "a": 2, "unit": "", "tol": 0.01, "hint": "6 ÷ 4 rounded up.", "sol": "<b>2</b>."},
  {"q": "A car hire record keeps 5 data items instead of 25 because of abstraction. What percentage is kept?", "a": 20, "unit": "%", "tol": 0.1, "hint": "5 ÷ 25.", "sol": "<b>20</b>%."},
  {"q": "How many sub-modules did the library overdue-email example use (GetOverdueLoan, IdentifyStudent, GetStudentEmail, CreateEmail, SendEmail)?", "a": 5, "unit": "", "tol": 0.01, "hint": "Count.", "sol": "<b>5</b>."},
  {"q": "A decomposed program has 8 modules and each takes 3 hours to test. How many hours to test them all?", "a": 24, "unit": "h", "tol": 0.01, "hint": "8 × 3.", "sol": "<b>24</b>."},
  {"q": "Two of the 5 data items stored per hire are dates. How many items are not dates?", "a": 3, "unit": "", "tol": 0.01, "hint": "5 − 2.", "sol": "<b>3</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Abstraction:", opts: ["Removes unnecessary detail", "Adds more data", "Splits a problem", "Compiles code"], a: 0, why: "Removes." },
  { q: "Decomposition:", opts: ["Breaks a problem into sub-problems", "Removes data", "Draws a flowchart", "Encrypts"], a: 0, why: "Breaks down." },
  { q: "A function:", opts: ["Returns a value", "Never returns", "Is a data item", "Is a file"], a: 0, why: "Returns a value." },
  { q: "An advantage of abstraction:", opts: ["Easier to design and solve", "Slower program", "More memory", "More errors"], a: 0, why: "Easier." },
  { q: "Decomposition leads to:", opts: ["Program modules", "Larger files", "Fewer tests", "A single module"], a: 0, why: "Modules." },
  { q: "An abstract model keeps:", opts: ["Only what the task needs", "Everything", "Nothing", "Only dates"], a: 0, why: "Only what is needed." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Abstraction", "Filter out what is not necessary."],
  ["Decomposition", "Break into sub-problems."],
  ["Module", "A procedure or function."],
  ["Function", "Returns a value."],
  ["Procedure", "Does a task; no return value."],
  ["Abstract model", "Only the needed data."],
  ["Scenario-specific", "Name modules for the scenario."],
  ["Advantage", "Easier to design, test, share."],
] });
