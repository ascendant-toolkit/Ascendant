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
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += SV.rect(20, 20, 330, 190, "f1", { rx: 10, ...op(0.18) }) + SV.text(185, 44, "DECLARE Day : STRING", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:15px" });
    o += SV.rect(410, 20, 330, 190, "f2", { rx: 10, ...op(0.18) }) + SV.text(575, 44, "DECLARE Day : SchoolDay", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:15px" });
    if (k >= 1) o += SV.text(40, 80, "Day ← \"Wensday\"", "lbl", { style: "font-family:var(--mono);font-size:15px" }) + SV.text(430, 80, "Day ← Wensday", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 2) o += SV.rect(40, 100, 290, 36, "cell-ok", { rx: 6 }) + SV.text(52, 124, "accepted: any text is allowed", "lbl bd t3") + SV.rect(430, 100, 290, 36, "cell-no", { rx: 6 }) + SV.text(442, 124, "rejected: not in the list", "lbl bd t2");
    if (k >= 3) o += SV.text(40, 170, "A misspelling spreads through the program", "sm") + SV.text(430, 170, "Only Monday ... Friday can be stored", "sm");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 225, label: "STRING against an enumerated type", base: { i: 0 }, draw, tween: 300, dwell: 3200, steps: [
    { cap: "A program stores the day a lesson is on. With a <b>STRING</b>, any text is allowed. With a user-defined type <code>SchoolDay</code> only five values are.", s: { i: 0 } },
    { cap: "The programmer mistypes the day as <b>Wensday</b>.", s: { i: 1 } },
    { cap: "The STRING variable accepts it. The enumerated type <b>rejects</b> it, because Wensday is not one of the listed values.", s: { i: 2 } },
    { cap: "A user-defined type matches the data exactly, so mistakes are caught when the program is compiled or run, not later.", s: { i: 3 } }] });
})();

(function () {
  const names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 28, "TYPE SchoolDay = (Monday, Tuesday, Wednesday, Thursday, Friday)", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    names.forEach((n, i) => { const x = 30 + i * 144; o += SV.rect(x, 50, 130, 50, k >= 1 ? "f3" : "cell", { rx: 8, ...op(k >= 1 || i < 5 ? 1 : 0) }) + SV.text(x + 65, 80, n, "lbl bd", { "text-anchor": "middle", style: "font-size:15px" }); if (k >= 1) o += SV.text(x + 65, 122, "position " + i, "sm", { "text-anchor": "middle" }); });
    if (k >= 2) o += SV.text(30, 160, "Wednesday < Friday   is TRUE   (2 < 4)", "lbl bd t3", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 3) o += SV.text(30, 190, "Saturday is not in the list: it cannot be stored in a SchoolDay", "lbl bd t2");
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 210, label: "An enumerated type as an ordered list", base: { i: 0 }, draw, tween: 300, dwell: 3200, steps: [
    { cap: "The declaration lists every possible value. The names are not strings, so there are no quotation marks.", s: { i: 0 } },
    { cap: "The list is <b>ordered</b>: each value has a position, starting at 0. This is how the values are stored.", s: { i: 1 } },
    { cap: "Because the list is ordered the values can be <b>compared</b>: Wednesday comes before Friday.", s: { i: 2 } },
    { cap: "The list is <b>complete and fixed</b>. A value that is not in it cannot be stored.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(40, 24, "memory", "sm");
    o += memCell(40, 36, "addr 5000", 40, "f3", 1, 240, 44) + SV.text(330, 64, "Score  (INTEGER)", "lbl", { style: "font-size:14px" });
    o += memCell(40, 96, "addr 5004", 7, "f3", 1, 240, 44) + SV.text(330, 124, "Lives  (INTEGER)", "lbl", { style: "font-size:14px" });
    o += memCell(40, 170, "P", k === 0 ? "?" : k === 1 ? "5000" : "5004", k === 0 ? "cell" : "f2", 1, 240, 44) + SV.text(330, 198, "P : TIntPointer", "lbl", { style: "font-size:14px" });
    if (k === 1) o += SV.path("M 285 190 C 345 190 345 70 285 60", "c1", { fill: "none", "stroke-width": 2.5 }) + SV.arrowHead(285, 60, "l", "dot1");
    if (k === 2) o += SV.path("M 285 190 C 345 190 345 130 285 120", "c1", { fill: "none", "stroke-width": 2.5 }) + SV.arrowHead(285, 120, "l", "dot1");
    if (k >= 1) o += SV.text(430, 70, k === 1 ? "P ← ^Score  stores the ADDRESS 5000" : "P ← ^Lives  stores the ADDRESS 5004", "lbl bd", { style: "font-family:var(--mono);font-size:14px" }) + SV.text(430, 100, "P^ is the value at that address: " + (k === 1 ? 40 : 7), "lbl", { style: "font-family:var(--mono);font-size:14px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 240, label: "A pointer holds an address", base: { i: 0 }, draw, tween: 300, dwell: 3400, steps: [
    { cap: "Two variables are stored at addresses in memory. The pointer variable <b>P</b> has not been given an address yet.", s: { i: 0 } },
    { cap: "<code>P ← ^Score</code> stores the <b>address</b> of Score (5000) in P. P does not hold 40; it refers to where 40 is stored.", s: { i: 1 } },
    { cap: "Pointing P at Lives instead: <code>P ← ^Lives</code> changes the address in P to 5004. <code>P^</code> is now 7.", s: { i: 2 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); const score = k >= 3 ? 42 : 40; let o = "";
    o += memCell(40, 36, "Score", score, k >= 3 ? "cell-warn" : "f3", 1, 240, 44) + memCell(40, 120, "P", "→ Score", "f2", 1, 240, 44);
    o += SV.path("M 280 142 C 340 142 340 58 285 58", "c1", { fill: "none", "stroke-width": 2.5 }) + SV.arrowHead(285, 58, "l", "dot1");
    o += SV.text(380, 70, "Score ← 40;  P ← ^Score", "lbl", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 1) o += SV.text(380, 104, "OUTPUT P^   →  40", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 2) o += SV.text(380, 138, "P^ ← P^ + 2", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 3) o += SV.text(380, 172, "OUTPUT Score   →  42", "lbl bd t3", { style: "font-family:var(--mono);font-size:14px" });
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 200, label: "Changing a value through a pointer", base: { i: 0 }, draw, tween: 300, dwell: 3000, steps: [
    { cap: "P holds the address of Score, which holds 40.", s: { i: 0 } },
    { cap: "<code>OUTPUT P^</code> follows the pointer and outputs the value at that address: 40.", s: { i: 1 } },
    { cap: "<code>P^ ← P^ + 2</code> follows the pointer and changes the value stored at that address.", s: { i: 2 } },
    { cap: "Score itself has changed, because P^ <i>is</i> Score's memory location. Output: 42.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  const types = { SchoolDay: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], Spectrum: ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"], Level: ["Beginner", "Intermediate", "Advanced"], Animals: ["Alpaca", "Chicken", "Donkey", "Duck", "Goat", "Pony", "Sheep"] };
  let t = "SchoolDay", a = 0, b = 2;
  const paint = () => {
    const L = types[t]; if (a >= L.length) a = 0; if (b >= L.length) b = L.length - 1;
    $$("#eB button").forEach((x) => x.classList.toggle("pri", x.textContent === t));
    $("#eV1").innerHTML = '<span style="align-self:center;margin-right:6px">First:</span>' + L.map((v, i) => `<button class="b${i === a ? " pri" : ""}" data-i="${i}">${v}</button>`).join("");
    $("#eV2").innerHTML = '<span style="align-self:center;margin-right:6px">Second:</span>' + L.map((v, i) => `<button class="b${i === b ? " pri" : ""}" data-i="${i}">${v}</button>`).join("");
    $$("#eV1 button").forEach((x) => (x.onclick = () => { a = +x.dataset.i; paint(); })); $$("#eV2 button").forEach((x) => (x.onclick = () => { b = +x.dataset.i; paint(); }));
    $("#e1").textContent = a; $("#e2").textContent = b; $("#e3").textContent = a < b ? "TRUE" : "FALSE";
    $("#eV").innerHTML = `<code>TYPE ${t} = (${L.join(", ")})</code>`;
  };
  $("#eB").innerHTML = Object.keys(types).map((k) => `<button class="b">${k}</button>`).join("");
  $$("#eB button").forEach((x) => (x.onclick = () => { t = x.textContent; paint(); }));
  $("#eA").onclick = () => { const v = $("#eT").value.trim(), L = types[t]; $("#eV").innerHTML = L.includes(v) ? `<b>${v}</b> is in the list, so it is stored (position ${L.indexOf(v)}).` : `<b>${v || "(nothing)"}</b> is not in the list for ${t}, so it is rejected. A variable of this type can only hold: ${L.join(", ")}.`; };
  paint();
})();

/* Lab 2 */
(function () {
  let st;
  const reset = () => { st = { score: 40, lives: 7, p: null, out: "" }; paint("Choose a statement to run."); };
  const paint = (msg) => {
    $("#pO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Score (5000)</th><th>Lives (5004)</th><th>P holds</th><th>P^ is</th><th>Output</th></tr><tr><td>' + st.score + "</td><td>" + st.lives + "</td><td>" + (st.p === null ? "?" : st.p) + "</td><td>" + (st.p === 5000 ? st.score : st.p === 5004 ? st.lives : "?") + "</td><td>" + st.out + "</td></tr></table></div>";
    $("#pV").textContent = msg;
  };
  $$("[data-s]").forEach((b) => (b.onclick = () => {
    const s = +b.dataset.s;
    if (s === 0) { st.p = 5000; paint("P ← ^Score stores the address 5000."); }
    else if (s === 1) { st.p = 5004; paint("P ← ^Lives stores the address 5004."); }
    else if (st.p === null) paint("P does not point anywhere yet: assign an address first.");
    else if (s === 2) { if (st.p === 5000) st.score++; else st.lives++; paint("P^ ← P^ + 1 changed the variable at address " + st.p + "."); }
    else { st.out = st.p === 5000 ? st.score : st.lives; paint("OUTPUT P^ follows the pointer and outputs " + st.out + "."); }
  }));
  $("#pR").onclick = reset; reset();
})();

(function () {
  const rows = [
    ["TYPE Day = (\"Mon\", \"Tue\", \"Wed\")", "Quotation marks make the values strings, not enumerated names", "TYPE Day = (Mon, Tue, Wed)"],
    ["TYPE Word = STRING", "This only renames STRING; it is not a pointer. A pointer needs ^", "TYPE Word = ^STRING"],
    ["TYPE Quarter1 = (January, February, March, April)", "Holds a fourth month the question did not include", "TYPE Quarter1 = (January, February, March)"],
    ["TYPE Fibonacci = (0, 1, 2, 3, 5, 8, 13, 21), 34", "Extra punctuation and a value that was not given", "TYPE Fibonacci = (0, 1, 2, 3, 5, 8, 13, 21)"],
    ["P ← Score  (P is a pointer)", "Stores the value of Score, not its address", "P ← ^Score"],
    ["OUTPUT P  (to show Score)", "Outputs the address held in P, not the value", "OUTPUT P^"]
  ];
  const paint = (i) => { $$("#mB button").forEach((b, k) => b.classList.toggle("pri", k === i)); const r = rows[i]; $("#mO").innerHTML = '<div class="tw"><table class="t"><tr><th>Mistake</th><th>What is wrong</th><th>Correct</th></tr><tr><td><code>' + r[0].replace(/&/g, "&amp;").replace(/</g, "&lt;") + "</code></td><td>" + r[1] + "</td><td><code>" + r[2] + "</code></td></tr></table></div>"; };
  $("#mB").innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">Mistake ${i + 1}</button>`).join("");
  $$("#mB button").forEach((b) => (b.onclick = () => paint(+b.dataset.i))); paint(0);
})();
Lib.classify($("#cl1"), { prompt: "What kind of type is each declaration?", buckets: [{"label": "Enumerated"}, {"label": "Pointer"}, {"label": "Composite (record)"}], items: [{"text": "TYPE Colour = (Red, Green, Blue)", "b": 0}, {"text": "TYPE TNamePtr = ^STRING", "b": 1}, {"text": "TYPE Pet ... DECLARE PetName : STRING ... ENDTYPE", "b": 2}, {"text": "TYPE Level = (Low, Medium, High)", "b": 0}, {"text": "TYPE TAgePtr = ^INTEGER", "b": 1}, {"text": "TYPE Book ... DECLARE Title : STRING ... DECLARE Pages : INTEGER ... ENDTYPE", "b": 2}], done: "Brackets with a list of names: enumerated. ^ in the type: pointer. TYPE ... ENDTYPE with DECLARE lines: record." });
Lib.classify($("#cl2"), { prompt: "Which statement describes an enumerated type, and which a pointer type?", buckets: [{"label": "Enumerated"}, {"label": "Pointer"}], items: [{"text": "An ordered list of all possible values", "b": 0}, {"text": "Stores a memory address", "b": 1}, {"text": "The values are unique and cannot be added to", "b": 0}, {"text": "Says what type of data is stored at the address", "b": 1}, {"text": "A variable holds one value from the list", "b": 0}, {"text": "P^ is the value at the address", "b": 1}], done: "Enumerated: a fixed ordered list. Pointer: an address plus the type it points to." });
Lib.order($("#o1"), { prompt: "Put the steps for using an enumerated type in order.", items: ["Write TYPE and a name for the new type", "Give the list of values in brackets, in order, with no quotation marks", "DECLARE a variable of the new type", "Assign one of the listed values to the variable", "Compare it with other values using the order of the list"], done: "Type, list, variable, assign, compare." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Non-composite type", "Defined without referencing another data type"], ["Enumerated type", "An ordered list of all the possible values"], ["Pointer type", "Stores the memory address of data of a stated type"], ["^", "Marks a pointer type in a declaration"], ["User-defined type", "A type created by the programmer"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "TYPE Day = (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday). Counting from 0, what is the position of Thursday?", "a": 3, "unit": "", "tol": 0.01, "hint": "Monday is 0.", "sol": "<b>3</b>."},
  {"q": "TYPE Spectrum has 7 values. How many different values can a variable of this type hold at one time?", "a": 1, "unit": "", "tol": 0.01, "hint": "A variable holds one value.", "sol": "<b>1</b>."},
  {"q": "How many values are in TYPE Fibonacci = (0, 1, 2, 3, 5, 8, 13, 21)?", "a": 8, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>8</b>."},
  {"q": "TYPE Level = (Beginner, Intermediate, Advanced). How many bits are enough to store a position (0, 1 or 2)?", "a": 2, "unit": "bits", "tol": 0.01, "hint": "2 bits give 4 values.", "sol": "<b>2</b> bits."},
  {"q": "Score holds 10 and P points to Score. What is Score after P^ ← P^ + 5?", "a": 15, "unit": "", "tol": 0.01, "hint": "P^ is Score.", "sol": "<b>15</b>."},
  {"q": "A set of 12 months is stored as an enumerated type. What is the position of December if January is 0?", "a": 11, "unit": "", "tol": 0.01, "hint": "12th value is position 11.", "sol": "<b>11</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is an enumerated type?", opts: ["A pointer to a list", "An ordered list of all the possible values", "A record", "A kind of loop"], a: 1, why: "It lists every allowed value, in order." },
  { q: "What does a pointer type store?", opts: ["A value", "A memory address", "A list", "A record"], a: 1, why: "An address, plus the type of data there." },
  { q: "Which is a correct enumerated declaration?", opts: ["TYPE Size = (\"S\", \"M\", \"L\")", "TYPE Size = (S, M, L)", "TYPE Size = ^(S, M, L)", "Size = [S, M, L]"], a: 1, why: "Names in brackets, no quotation marks." },
  { q: "Which is a correct pointer type to STRING?", opts: ["TYPE Word = STRING", "TYPE Word = ^STRING", "TYPE Word = (STRING)", "TYPE Word = STRING^"], a: 1, why: "^ comes before the type." },
  { q: "Which makes a type non-composite?", opts: ["It holds many fields", "It is defined without referencing another type", "It is a record", "It is an array"], a: 1, why: "That is the mark scheme's definition." },
  { q: "Why is a user-defined type used?", opts: ["To make the program slower", "To create a type the language does not have and match the data", "To avoid declaring variables", "To remove loops"], a: 1, why: "It tailors the type to the data." },
] });
Lib.cards($("#fc1"), { cards: [
  ["User-defined type", "A data type created by the programmer."],
  ["Non-composite", "Defined without referencing another data type."],
  ["Enumerated", "An ordered list of all possible values. TYPE T = (a, b, c)."],
  ["Pointer", "Stores a memory address and the type of data there. TYPE P = ^INTEGER."],
  ["P ← ^Score", "P holds the address of Score."],
  ["P^", "The value at the address in P."],
  ["Composite", "Record, set, class: built from other types."],
  ["Why", "A type the language lacks, matching the data, clearer, safer."],
] });
