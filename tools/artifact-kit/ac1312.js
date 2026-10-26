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

function classBox(x, y, w, title, rows, v = 1, cls = "f1", lh = 20) {
  const h = 30 + rows.length * lh + 8;
  let o = SV.rect(x, y, w, h, "cell", { rx: 6, ...op(v) }) + SV.rect(x, y, w, 28, cls, { rx: 6, ...op(v * 0.6) }) + SV.text(x + w / 2, y + 19, title, "lbl bd", { "text-anchor": "middle", style: "font-size:15px", ...op(v) });
  rows.forEach((r, i) => { o += SV.text(x + 8, y + 46 + i * lh, r, "sm", { style: "font-family:var(--mono);font-size:11.5px", ...op(v) }); });
  return o;
}

(function () {
  const vals = ["\"XA782\"", "\"Cambridge\"", "12/12/2022", "C350"];
  const draw = (s) => {
    const k = Math.round(s.i); const f = ["FlightNumber", "Destination", "DepartureDate", "AircraftType"], t = ["STRING", "STRING", "DATE", "Aircraft"];
    let o = classBox(20, 20, 280, "TYPE Flight", f.map((n, i) => n + " : " + t[i]), 1, "f1", 24);
    if (k >= 1) o += classBox(380, 20, 340, "Flight1 : Flight", f.map((n, i) => n + " = " + (k > i + 1 ? vals[i] : "?")), 1, "f2", 24) + SV.line(300, 70, 380, 70, "dash", op(0.6));
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 200, label: "A record type and a record variable", base: { i: 0 }, draw, tween: 300, dwell: 3000, steps: [
    { cap: "The <b>TYPE</b> statement describes a record: a name and a field for each item, each with its data type. It creates no data yet.", s: { i: 0 } },
    { cap: "<code>DECLARE Flight1 : Flight</code> creates a variable that can hold one record. Its fields are empty.", s: { i: 1 } },
    { cap: "<code>Flight1.FlightNumber ← \"XA782\"</code>: dot notation assigns one field.", s: { i: 2 } },
    { cap: "<code>Flight1.Destination ← \"Cambridge\"</code>.", s: { i: 3 } },
    { cap: "<code>Flight1.DepartureDate ← 12/12/2022</code> (a DATE, no quotation marks).", s: { i: 4 } },
    { cap: "<code>Flight1.AircraftType ← C350</code>: an enumerated value, so no quotation marks. The record is complete.", s: { i: 5 } }] });
})();

(function () {
  const rows = [["SB2789", "Dublin", "N03"], ["BA104", "Paris", "W01"], ["XA782", "Cambridge", "N01"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "Flights : ARRAY[1:3] OF Flight", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    o += SV.text(30, 56, "index", "sm") + SV.text(100, 56, "FlightNumber", "sm") + SV.text(260, 56, "Destination", "sm") + SV.text(420, 56, "Gate", "sm");
    rows.forEach((r, i) => { const y = 66 + i * 40; o += SV.rect(30, y, 640, 34, k === i + 1 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(44, y + 22, String(i + 1), "lbl", { style: "font-family:var(--mono)" }) + SV.text(100, y + 22, r[0], "lbl", { style: "font-family:var(--mono)" }) + SV.text(260, y + 22, r[1], "lbl", { style: "font-family:var(--mono)" }) + SV.text(420, y + 22, k === 4 && i === 1 ? "W04" : r[2], "lbl" + (k === 4 && i === 1 ? " bd t3" : ""), { style: "font-family:var(--mono)" }); });
    if (k === 1) o += SV.text(30, 206, "Flights[1].Destination  →  \"Dublin\"", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    if (k === 4) o += SV.text(30, 206, "Flights[2].Gate ← W04   changes one field of one record", "lbl bd t3", { style: "font-family:var(--mono);font-size:14px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 230, label: "An array of records", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "An <b>array of records</b> stores many flights: every element is a whole record.", s: { i: 0 } },
    { cap: "<code>Flights[1].Destination</code>: the array element first, then the field.", s: { i: 1 } },
    { cap: "<code>Flights[2]</code> is the record for BA104.", s: { i: 2 } },
    { cap: "A loop can visit each record in turn: <code>FOR i ← 1 TO 3</code>.", s: { i: 3 } },
    { cap: "A field can be changed on its own: <code>Flights[2].Gate ← W04</code>.", s: { i: 4 } }] });
})();

(function () {
  const A = [1, 2, 3], B = [3, 4];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.circle(260, 120, 90, "f1", op(0.3)) + SV.circle(420, 120, 90, "f2", op(0.3)) + SV.text(200, 36, "A = {1, 2, 3}", "lbl bd") + SV.text(380, 36, "B = {3, 4}", "lbl bd");
    const items = { 1: [210, 120], 2: [240, 165], 3: [340, 120], 4: [470, 120] }, hit = (n) => k === 0 ? false : k === 1 ? true : k === 2 ? n === 3 : n === 1 || n === 2;
    [1, 2, 3, 4].forEach((n) => { const p = items[n]; o += SV.circle(p[0], p[1], 20, hit(n) ? "dot3" : "dot1", op(hit(n) ? 1 : 0.25)) + SV.text(p[0], p[1] + 6, String(n), "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:17px" }); });
    const caps = ["", "A ∪ B = {1, 2, 3, 4}", "A ∩ B = {3}", "A − B = {1, 2}"];
    if (k >= 1) o += SV.text(560, 130, caps[k], "lbl bd t3", { style: "font-size:17px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 240, label: "Set operations", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "Two sets. The number 3 is in both. In a set the order does not matter and no value appears twice.", s: { i: 0 } },
    { cap: "<b>Union</b>: everything that is in A or in B (or both). 3 is listed once.", s: { i: 1 } },
    { cap: "<b>Intersection</b>: only the values that are in both sets.", s: { i: 2 } },
    { cap: "<b>Difference</b> A − B: the values in A that are not in B.", s: { i: 3 } }] });
})();

(function () {
  const rows = [["VideoID  (SB2789 style code)", "STRING", "letters and digits"], ["Title", "STRING", "text"], ["ReleaseYear", "INTEGER", "whole number"], ["PurchaseDate", "DATE", "a calendar date"], ["VideoFormat  (DVD, Blu-ray, 4K)", "Enumerated", "fixed list of values"], ["RunningTime  (minutes)", "INTEGER", "whole number"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "TYPE VideoLibrary", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    rows.forEach((r, i) => { const y = 38 + i * 34; o += SV.rect(30, y, 700, 30, k > i ? "f3" : "cell", { rx: 6, ...op(k > i ? 1 : 0.7) }) + SV.text(44, y + 20, r[0], "lbl", { style: "font-family:var(--mono);font-size:13px" }); if (k > i) o += SV.text(380, y + 20, r[1], "lbl bd", { style: "font-family:var(--mono);font-size:13px" }) + SV.text(500, y + 20, r[2], "sm"); });
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 258, label: "Choosing a data type for each field", base: { i: 0 }, draw, tween: 250, dwell: 2600, steps: [
    { cap: "Each field needs the most appropriate type. Read what the data looks like and how it will be used.", s: { i: 0 } },
    { cap: "An identity code mixes letters and digits: <b>STRING</b>.", s: { i: 1 } },
    { cap: "A title is text: <b>STRING</b>.", s: { i: 2 } },
    { cap: "A year is a whole number: <b>INTEGER</b>.", s: { i: 3 } },
    { cap: "A purchase date: <b>DATE</b>.", s: { i: 4 } },
    { cap: "The format has only a few possible values, DVD, Blu-ray, 4K and MP4: an <b>enumerated</b> type is efficient and safe.", s: { i: 5 } },
    { cap: "A running time in minutes: <b>INTEGER</b>.", s: { i: 6 } }] });
})();

/* Lab 1: set operations */
(function () {
  const N = [1, 2, 3, 4, 5, 6, 7, 8]; let A = [1, 2, 3], B = [3, 4, 5], op = 0;
  const ops = ["Union", "Intersection", "Difference A − B", "Difference B − A"];
  const paint = () => {
    const mk = (id, S, which) => { $("#" + id).innerHTML = '<span style="align-self:center;margin-right:6px"><b>' + which + "</b></span>" + N.map((n) => `<button class="b${S.includes(n) ? " pri" : ""}" data-n="${n}">${n}</button>`).join(""); $$("#" + id + " button").forEach((b) => (b.onclick = () => { const n = +b.dataset.n; const i = S.indexOf(n); if (i >= 0) S.splice(i, 1); else S.push(n); paint(); })); };
    mk("sA", A, "A"); mk("sB", B, "B");
    $("#sO").innerHTML = ops.map((o, i) => `<button class="b${i === op ? " pri" : ""}" data-i="${i}">${o}</button>`).join(""); $$("#sO button").forEach((b) => (b.onclick = () => { op = +b.dataset.i; paint(); }));
    const srt = (a) => a.slice().sort((x, y) => x - y), fmt = (a) => "{" + srt(a).join(", ") + "}";
    const res = op === 0 ? [...new Set([...A, ...B])] : op === 1 ? A.filter((n) => B.includes(n)) : op === 2 ? A.filter((n) => !B.includes(n)) : B.filter((n) => !A.includes(n));
    $("#s1").textContent = fmt(A); $("#s2").textContent = fmt(B); $("#s3").textContent = fmt(res);
    $("#sV").textContent = ["Union: every value that is in A or in B, each listed once.", "Intersection: only the values in both sets.", "A − B: values in A that are not in B.", "B − A: values in B that are not in A."][op];
  };
  paint();
})();

/* Lab 2 */
(function () {
  const sc = [
    ["Booking", [["BookingNumber (letters and digits)", "STRING"], ["DateOfDeparture", "DATE"], ["ClientTelephone", "STRING"], ["TaxiUsed (M100, M230, T101 ...)", "Enumerated"]]],
    ["ColourData", [["ColourCode (XYZ12345)", "STRING"], ["Wavelength (650)", "INTEGER"], ["Frequency (4.62)", "REAL"], ["PrimaryColour (Yes or No)", "BOOLEAN"]]],
    ["ClubMember", [["Code (984632)", "INTEGER"], ["JoinDate", "DATE"], ["Fees (12.50)", "REAL"], ["FeesPaid (yes or no)", "BOOLEAN"]]]
  ];
  const T = ["STRING", "INTEGER", "REAL", "BOOLEAN", "DATE", "CHAR", "Enumerated"]; let cur = 0, pick = [];
  const paint = () => {
    $$("#tB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    $("#tO").innerHTML = '<div class="tw"><table class="t"><tr><th>Field</th><th>Choose the type</th></tr>' + sc[cur][1].map((f, i) => `<tr><td><code>${f[0]}</code></td><td>${T.map((t) => `<button class="b${pick[i] === t ? " pri" : ""}" data-i="${i}" data-t="${t}">${t}</button>`).join(" ")}</td></tr>`).join("") + "</table></div>";
    $$("#tO button").forEach((b) => (b.onclick = () => { pick[+b.dataset.i] = b.dataset.t; paint(); }));
    const done = sc[cur][1].every((f, i) => pick[i]); const ok = sc[cur][1].filter((f, i) => pick[i] === f[1]).length;
    $("#tV").innerHTML = done ? (ok === sc[cur][1].length ? "All four are the most appropriate types." : `${ok} of ${sc[cur][1].length} correct. Check: text and codes are STRING, whole numbers INTEGER, fractions REAL, yes/no BOOLEAN, fixed lists are enumerated.`) : "Choose a type for every field.";
  };
  $("#tB").innerHTML = sc.map((s, i) => `<button class="b" data-i="${i}">${s[0]}</button>`).join("");
  $$("#tB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; pick = []; paint(); })); paint();
})();

(function () {
  const rows = [
    ["TYPE Pet\n   DECLARE PetName : STRING\n   DECLARE PetAge : INTEGER", "No ENDTYPE: the definition is never closed", "Add ENDTYPE"],
    ["TYPE Pet\n   PetName : STRING\nENDTYPE", "Each field needs the word DECLARE", "DECLARE PetName : STRING"],
    ["DECLARE Pet1 : Pet\nPetName ← \"Tibbles\"", "The field is not tied to the variable", "Pet1.PetName ← \"Tibbles\""],
    ["Pet1.PetAge ← \"8\"", "PetAge is an INTEGER, so no quotation marks", "Pet1.PetAge ← 8"],
    ["Flight1.AircraftType ← \"C350\"", "AircraftType is enumerated: no quotation marks", "Flight1.AircraftType ← C350"],
    ["DEFINE Operators ('+', '-') : SymbolSet\n(no TYPE statement before it)", "The set type was never declared", "TYPE SymbolSet = SET OF CHAR first"]
  ];
  const paint = (i) => { $$("#mB button").forEach((b, k) => b.classList.toggle("pri", k === i)); const r = rows[i]; $("#mO").innerHTML = '<div class="tw"><table class="t"><tr><th>Mistake</th><th>What is wrong</th><th>Correct</th></tr><tr><td><pre class="plain">' + r[0].replace(/&/g, "&amp;").replace(/</g, "&lt;") + "</pre></td><td>" + r[1] + "</td><td><code>" + r[2] + "</code></td></tr></table></div>"; };
  $("#mB").innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">Mistake ${i + 1}</button>`).join("");
  $$("#mB button").forEach((b) => (b.onclick = () => paint(+b.dataset.i))); paint(0);
})();
Lib.classify($("#cl1"), { prompt: "Which data type is best for each field?", buckets: [{"label": "STRING"}, {"label": "INTEGER"}, {"label": "REAL"}, {"label": "BOOLEAN"}, {"label": "DATE"}, {"label": "Enumerated"}], items: [{"text": "A telephone number such as 01223 658721", "b": 0}, {"text": "A running time in minutes", "b": 1}, {"text": "A price of 12.99", "b": 2}, {"text": "Fees paid: yes or no", "b": 3}, {"text": "Date of departure", "b": 4}, {"text": "Format: DVD, Blu-ray, 4K or MP4", "b": 5}, {"text": "An identity code SB2789", "b": 0}, {"text": "Year released", "b": 1}, {"text": "A frequency of 4.62", "b": 2}, {"text": "Number of members", "b": 1}], done: "Codes and phone numbers are STRING. Whole numbers: INTEGER. With a fraction: REAL. Two values: BOOLEAN. Calendar: DATE. A fixed list: enumerated." });
Lib.classify($("#cl2"), { prompt: "Is it a record, a set or a class?", buckets: [{"label": "Record"}, {"label": "Set"}, {"label": "Class / object"}], items: [{"text": "Fields of different types about one flight", "b": 0}, {"text": "Unordered unique values of one type, with union and intersection", "b": 1}, {"text": "Fields and the methods that act on them, with objects as instances", "b": 2}, {"text": "TYPE Pet ... ENDTYPE", "b": 0}, {"text": "TYPE Numbers = SET OF INTEGER", "b": 1}, {"text": "A Parrot inherits from Animal", "b": 2}], done: "Record: fields. Set: unique unordered, one type. Class: fields plus methods." });
Lib.order($("#o1"), { prompt: "Put the steps for creating and using a record in order.", items: ["Write the TYPE statement with a DECLARE for each field", "End it with ENDTYPE", "DECLARE a variable of the new type", "Assign each field with variable.field", "Use the fields in the program"], done: "Type, ENDTYPE, variable, assign, use." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Record", "A composite type with fields of different types"], ["Set", "Unordered, unique values of one type"], ["Union", "Everything in either set"], ["Intersection", "Only what is in both sets"], ["Class", "A composite type holding fields and methods"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A = {1, 2, 3, 4, 5} and B = {4, 5, 6}. How many values are in the union?", "a": 6, "unit": "", "tol": 0.01, "hint": "1, 2, 3, 4, 5, 6.", "sol": "<b>6</b>."},
  {"q": "A = {1, 2, 3, 4, 5} and B = {4, 5, 6}. How many values are in the intersection?", "a": 2, "unit": "", "tol": 0.01, "hint": "4 and 5.", "sol": "<b>2</b>."},
  {"q": "A = {1, 2, 3, 4, 5} and B = {4, 5, 6}. How many values are in A − B?", "a": 3, "unit": "", "tol": 0.01, "hint": "1, 2, 3.", "sol": "<b>3</b>."},
  {"q": "A record type has 6 fields. How many DECLARE statements are inside the TYPE ... ENDTYPE?", "a": 6, "unit": "", "tol": 0.01, "hint": "One for each field.", "sol": "<b>6</b>."},
  {"q": "An array holds 30 records and each record has 5 fields. How many individual field values are there?", "a": 150, "unit": "", "tol": 0.01, "hint": "30 × 5.", "sol": "<b>150</b>."},
  {"q": "A set is defined as {2, 4, 6, 8, 10, 12}. How many values does it hold?", "a": 6, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>6</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a record?", opts: ["An ordered list of one type", "A composite type with fields, which may have different types", "A pointer", "A loop"], a: 1, why: "Fields grouped under one identifier." },
  { q: "Which data type should hold a telephone number?", opts: ["INTEGER", "STRING", "REAL", "BOOLEAN"], a: 1, why: "It is not used in arithmetic and may start with 0." },
  { q: "Which statement is true of a set?", opts: ["It is ordered", "It can contain duplicates", "Its elements are unordered and unique and have one data type", "It holds fields of different types"], a: 2, why: "Those are the characteristics." },
  { q: "Which line assigns a value to a field of the record variable Pet1?", opts: ["PetName ← \"Tibbles\"", "Pet1.PetName ← \"Tibbles\"", "Pet.PetName ← \"Tibbles\"", "Pet1(PetName) ← \"Tibbles\""], a: 1, why: "variable.field." },
  { q: "Which set operation gives the values in both sets?", opts: ["Union", "Intersection", "Difference", "Membership"], a: 1, why: "Intersection." },
  { q: "A field has the fixed values DVD, Blu-ray and 4K. What is the best type?", opts: ["STRING", "INTEGER", "An enumerated type", "REAL"], a: 2, why: "A fixed list is an enumerated type." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Composite type", "Refers to other types; holds several values under one identifier."],
  ["Record", "Fields of different types. TYPE ... ENDTYPE with DECLARE."],
  ["Set", "Unordered, unique values of one type. TYPE S = SET OF ... DEFINE ..."],
  ["Class", "Fields and methods; objects are instances."],
  ["Dot notation", "Variable.Field ← value"],
  ["Union / intersection", "Either set / both sets."],
  ["Choosing types", "STRING text and codes, INTEGER whole, REAL fraction, BOOLEAN yes/no, DATE, enumerated list."],
  ["Array of records", "Flights[2].Gate"],
] });
