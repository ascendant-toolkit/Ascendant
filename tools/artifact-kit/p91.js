const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)", WARN = "var(--warn)";
const note = (x, y, t, cls = "", anchor = "middle") => SV.text(x, y, t, "lbl bd " + cls, { "text-anchor": anchor });
const sm = (x, y, t, anchor = "middle") => SV.text(x, y, t, "sm", { "text-anchor": anchor });
const panel = (x, y, w, h, title, col, o = 1) => SV.rect(x, y, w, h, "", { rx: 12, style: `fill:var(--surface);stroke:${col};stroke-width:3`, opacity: o }) + (title ? SV.text(x + w / 2, y + 22, title, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) : "");
const arr = (x1, y1, x2, y2, col, dash) => SV.line(x1, y1, x2, y2, "", { style: `stroke:${col};stroke-width:3;${dash ? "stroke-dasharray:7 6" : ""}` });
const chip = (x, y, w, t, col) => SV.rect(x, y, w, 26, "", { rx: 13, style: `fill:${col}` }) + SV.text(x + w / 2, y + 18, t, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:12px" });
const range = (a, b) => { const r = []; for (let i = a; i <= b; i++) r.push(i); return r; };
/* select-one-per-row chooser. items: [text, correctOption] */
function chooser(el, v, opts, items, ph) {
  el.innerHTML = items.map((s) => `<div class="r" data-a="${esc(s[1])}"><span class="q">${s[0]}</span><select class="sel" aria-label="${esc(s[0].replace(/<[^>]+>/g, ""))}"><option value="">${ph || "Choose…"}</option>${opts.map((x) => `<option>${esc(x)}</option>`).join("")}</select></div>`).join("");
  v.textContent = "Choose an answer for each row.";
  $$(".r", el).forEach((r) => $("select", r).addEventListener("change", (e) => { r.classList.remove("ok", "no"); if (e.target.value) r.classList.add(e.target.value === r.dataset.a ? "ok" : "no"); v.textContent = `${$$(".r.ok", el).length} of ${$$(".r", el).length} correct. Red means a different answer fits better.`; }));
}
/* ---------- 1. anatomy ---------- */
const TB = [["StudentID", "Name", "Year", "Form"], ["1001", "Ana Lee", "10", "10B"], ["1002", "Ben Cho", "9", "9A"], ["1003", "Cy Diaz", "10", "10A"], ["1004", "Dee Kay", "11", "11C"]];
function anChart(s) {
  const k = Math.round(s.k), cw = 140, rh = 46, x0 = 100, y0 = 20; let o = "";
  for (let r = 0; r < 5; r++) for (let c = 0; c < 4; c++) { const hd = r === 0, on = (k === 0) || (k === 1 && hd) || (k === 2 && c === 2) || (k === 3 && r === 3) || (k === 4 && r === 3 && c === 1);
    o += SV.rect(x0 + c * cw, y0 + r * rh, cw - 4, rh - 4, "", { rx: 6, style: `fill:${on ? (k === 2 ? "var(--accent-soft)" : k === 3 ? "var(--good-soft)" : k === 4 ? "var(--warn-soft)" : k === 1 ? "var(--accent-soft)" : "var(--soft)") : hd ? "var(--soft)" : "var(--surface)"};stroke:${on ? "var(--accent)" : "var(--line)"};stroke-width:${on ? 3 : 1.5}` }) + SV.text(x0 + c * cw + cw / 2 - 2, y0 + r * rh + 28, TB[r][c], "lbl bd", { "text-anchor": "middle", style: `font-family:var(--mono);font-size:${hd ? 13 : 15}px` }); }
  o += note(380, 270, ["The whole TABLE: rows and columns of data", "The FIELD NAMES: the heading of each column", "A FIELD: a column, one type of data about every student", "A RECORD: a row, everything about one student", "A DATA ITEM: one value, where a record and a field meet"][k], "t1");
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 285, label: "The parts of a database table", base: { k: 0 }, tween: 1, dwell: 3500, draw: anChart, steps: [
  { cap: "A <b>table</b> holds all the data in <b>rows and columns</b>. This single table stores students.", s: { k: 0 } },
  { cap: "The top row gives the <b>field names</b>: StudentID, Name, Year and Form.", s: { k: 1 } },
  { cap: "A <b>field</b> is a column. The <b>Year</b> field holds one type of data (the year group) for every student.", s: { k: 2 } },
  { cap: "A <b>record</b> is a row: all the data about <b>one</b> student (1003, Cy Diaz, 10, 10A).", s: { k: 3 } },
  { cap: "A single value, such as <b>Cy Diaz</b>, is one <b>data item</b>: one record, one field.", s: { k: 4 } },
] });

/* ---------- 2. design ---------- */
const FD = [["StudentID", "Integer", "Range 1000 to 9999"], ["Name", "Text", "Presence; length"], ["Year", "Integer", "Range 7 to 13"], ["PaidTrip", "Boolean", "TRUE or FALSE"]];
function dsChart(s) {
  const k = Math.round(s.k); let o = SV.text(20, 28, "Requirement: store each student's ID, name, year group", "lbl", { "text-anchor": "start" }) + SV.text(20, 50, "and whether they have paid for the trip.", "lbl", { "text-anchor": "start" });
  const heads = ["Field name", "Data type", "Validation"];
  heads.forEach((h, i) => (o += SV.text(20, 108 + i * 50, h, "lbl bd t1", { "text-anchor": "start" })));
  FD.forEach((f, i) => { if (k < i + 1) return; const x = 150 + i * 150; o += SV.rect(x, 80, 140, 160, "", { rx: 10, style: `fill:var(--surface);stroke:${k === i + 1 ? "var(--accent)" : "var(--line)"};stroke-width:${k === i + 1 ? 4 : 2}` }) + SV.text(x + 70, 108, f[0], "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:13px" }) + SV.text(x + 70, 158, f[1], "lbl", { "text-anchor": "middle" }) + SV.text(x + 70, 208, f[2], "sm", { "text-anchor": "middle" }); });
  if (k >= 5) o += SV.text(150 + 70, 74, "★ primary key", "lbl bd t4", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 255, label: "Designing a table from requirements", base: { k: 0 }, tween: 1, dwell: 3600, draw: dsChart, steps: [
  { cap: "The school describes what it needs to store. Each item becomes a <b>field</b>, with a name, a <b>data type</b> and any <b>validation</b>.", s: { k: 0 } },
  { cap: "<b>StudentID</b>: a whole number (Integer), checked with a range check.", s: { k: 1 } },
  { cap: "<b>Name</b>: Text, with a presence check (must not be empty) and a length check.", s: { k: 2 } },
  { cap: "<b>Year</b>: an Integer with a range check from 7 to 13.", s: { k: 3 } },
  { cap: "<b>PaidTrip</b>: a yes/no value, so the type is <b>Boolean</b>.", s: { k: 4 } },
  { cap: "Finally, a <b>primary key</b> is chosen: StudentID is different for every student, so it is unique.", s: { k: 5 } },
] });

/* ---------- Lab 1 ---------- */
(() => {
  const ITEMS = [["PetID", 1], ["PetName", 1], ["Species", 1], ["DateOfBirth", 1], ["Vaccinated", 1], ["OwnerName", 1], ["OwnerPhone", 1], ["WaitingRoomColour", 0], ["NumberOfWindows", 0], ["VetsFavouriteFood", 0]];
  const el = $("#fp"), v = $("#fpv");
  const fill = () => { el.innerHTML = ITEMS.map((it, i) => `<label data-i="${i}"><input type="checkbox"> ${it[0]}</label>`).join(""); v.textContent = ""; };
  $("#fpc").onclick = () => { let ok = 0; $$("label", el).forEach((l) => { const good = ITEMS[+l.dataset.i][1] === +$("input", l).checked; l.classList.toggle("ok", good); l.classList.toggle("no", !good); if (good) ok++; }); v.innerHTML = ok === ITEMS.length ? "All correct. Each needed piece of data is its own field, and details that have nothing to do with the pets are left out." : `${ok} of ${ITEMS.length} correct. Green is right. Red: you ticked a field the table does not need, or missed one it does.`; };
  $("#fpr").onclick = fill; fill();
})();

/* ---------- Lab 2 ---------- */
(() => {
  const R = [
    ["StudentID", "Integer 1000 to 9999 (range check)", "1005", (v) => (/^\d+$/.test(v) ? (+v >= 1000 && +v <= 9999 ? [1, "an integer in range"] : [0, "outside 1000 to 9999"]) : [0, "not a whole number (type check)"])],
    ["Name", "Not empty, up to 20 characters (presence, length)", "Eli Moss", (v) => (!v.trim() ? [0, "empty (presence check)"] : v.length > 20 ? [0, "longer than 20 characters (length check)"] : [1, "present and short enough"])],
    ["Year", "Integer 7 to 13 (range check)", "10", (v) => (/^\d+$/.test(v) ? (+v >= 7 && +v <= 13 ? [1, "an integer in range"] : [0, "outside 7 to 13"]) : [0, "not a whole number (type check)"])],
    ["Form", "Two digits then a letter, such as 10B (format check)", "10B", (v) => (/^\d{1,2}[A-Z]$/.test(v) ? [1, "matches the pattern"] : [0, "does not match digits then a letter"])],
    ["Email", "Contains @ and a . after it (format check)", "eli@school.org", (v) => (/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v) ? [1, "matches the pattern"] : [0, "not in the form name@domain.ext"])],
  ];
  const t = $("#vr"), vv = $("#vv");
  t.innerHTML = `<tr><th>Field</th><th>Rule</th><th>Value</th><th>Result</th></tr>` + R.map((r, i) => `<tr><td><b>${r[0]}</b></td><td>${r[1]}</td><td><input class="ipin" style="width:150px;padding:4px 8px" type="text" data-i="${i}" value="${r[2]}" aria-label="${r[0]}" spellcheck="false"></td><td data-o="${i}"></td></tr>`).join("");
  function upd() { let bad = 0; R.forEach((r, i) => { const v = $(`[data-i="${i}"]`, t).value.trim(), x = r[3](v); if (!x[0]) bad++; $(`[data-o="${i}"]`, t).innerHTML = x[0] ? `<span class="okf">Accepted</span> ${x[1]}` : `<span class="flag">Rejected</span> ${x[1]}`; }); vv.innerHTML = bad ? `${bad} field${bad > 1 ? "s" : ""} failed validation, so the record <b>would not be stored</b> until corrected.` : "Every field passes, so the record is <b>stored</b>. Remember: valid data can still be wrong."; }
  $$("input", t).forEach((i) => i.addEventListener("input", upd)); upd();
})();

/* ---------- Lab 3 ---------- */
chooser($("#sn"), $("#sv"), ["Table", "Record", "Field", "Field name", "Data item"], [
  ["A row holding everything about one student", "Record"], ["The column headed Year", "Field"], ["The word \"Year\" at the top of a column", "Field name"], ["All the student data, in rows and columns", "Table"], ["The single value \"Ana Lee\"", "Data item"], ["The data about one book in a library database", "Record"],
]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is each item a field or a record?", buckets: [{ label: "Field" }, { label: "Record" }], items: [
  { text: "Surname", b: 0 },
  { text: "DateOfBirth", b: 0 },
  { text: "A column in the table", b: 0 },
  { text: "Year", b: 0 },
  { text: "Ana Lee, 10, 10B, 15/03/2010", b: 1 },
  { text: "A row in the table", b: 1 },
  { text: "Everything about one pet", b: 1 },
  { text: "Record number 3", b: 1 },
], done: "A column against a row." });

Lib.classify($("#cl2"), { prompt: "Which validation check does each rule describe?", buckets: [{ label: "Range check" }, { label: "Length check" }, { label: "Presence check" }, { label: "Format check" }, { label: "Type check" }], items: [
  { text: "Year must be from 7 to 13", b: 0 },
  { text: "Price must be at least 0", b: 0 },
  { text: "Password must have 8 to 12 characters", b: 1 },
  { text: "Phone number must have exactly 10 digits", b: 1 },
  { text: "The surname must not be left empty", b: 2 },
  { text: "A required field must contain something", b: 2 },
  { text: "A form code must be two digits then a letter", b: 3 },
  { text: "A date must be DD/MM/YYYY", b: 3 },
  { text: "Age must be a whole number", b: 4 },
], done: "Match the rule to the check." });

Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Table", "All the data in rows and columns"],
  ["Record", "A row: all the data about one item"],
  ["Field", "A column: one type of data"],
  ["Field name", "The heading of a column"],
  ["Data item", "A single value in the table"],
  ["Validation", "Checks that data is reasonable"]
] });

Lib.order($("#o1"), { prompt: "Put the steps of defining a single-table database in order.", items: [
  "Decide what each record is about",
  "List the fields needed",
  "Choose a field name and a data type for each field",
  "Choose the validation for each field",
  "Choose a primary key"
], done: "Record, fields, names and types, validation, key." });

Lib.calc($("#c1"), { qs: [
  { q: "A table has 30 records and 6 fields. How many data items does it hold?", a: 180, sol: "30 × 6 = 180." },
  { q: "A table has 30 records. 5 are added and 2 are deleted. How many records are there?", a: 33, sol: "30 + 5 − 2 = 33." },
  { q: "A StudentID must be from 1000 to 9999. How many different IDs are possible?", a: 9000, sol: "9999 − 1000 + 1 = 9000." },
  { q: "A table has 8 fields. How many field names does it have?", a: 8, sol: "One field name per field." },
  { q: "Records are sorted by Year. 12 students are in Year 10 and 9 in Year 11. How many records are in Years 10 and 11?", a: 21, sol: "12 + 9 = 21." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "What is a record?", opts: ["A row: all the data about one item", "A column", "A single value", "A database"], a: 0, why: "A record is a row." },
  { q: "What is a field?", opts: ["A column: one type of data", "A row", "A table", "A file"], a: 0, why: "A field is a column." },
  { q: "Which is a single-table database?", opts: ["All the data in one table", "Many linked tables", "A text file only", "A spreadsheet only"], a: 0, why: "IGCSE uses one table." },
  { q: "Why split a name into FirstName and Surname?", opts: ["To sort or search by each part", "To save a field", "To make it longer", "To avoid validation"], a: 0, why: "Separate fields can be sorted and searched separately." },
  { q: "Which does validation check?", opts: ["The data is reasonable", "The data is always correct", "The table size", "The record order"], a: 0, why: "Reasonable, not correct." },
  { q: "What does a range check on Year do?", opts: ["Checks it is between 7 and 13", "Checks it is text", "Checks it is not empty", "Checks its format"], a: 0, why: "A range check enforces limits." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Database", "An organised collection of data that can be searched, sorted and updated."],
  ["Table", "All the data of a database, arranged in rows and columns."],
  ["Record", "A row in a table: all the data about one item."],
  ["Field", "A column in a table: one type of data about each item."],
  ["Field name", "The heading of a column."],
  ["Data item", "A single value where a record and a field meet."],
  ["Validation", "An automatic check that data is reasonable."],
  ["Single-table database", "A database that stores all its data in one table."]
] });
