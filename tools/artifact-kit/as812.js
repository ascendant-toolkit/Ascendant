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
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, t, on) => SV.rect(x, y, 130, 30, on ? "f3" : "cell", { rx: 5 }) + SV.text(x + 65, y + 19, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); let o = B(20, 20, "CUSTOMER", true) + B(280, 20, "PURCHASE", true) + B(280, 110, "PURCHASE_ITEM", true) + B(20, 110, "PLANT", true);
    if (k >= 1) o += SV.path("M150,35 H280", "ax") + SV.text(215, 28, "1 ——< M", "sm", { "text-anchor": "middle" }); if (k >= 2) o += SV.path("M345,50 V110", "ax") + SV.text(380, 85, "1 —< M", "sm"); if (k >= 3) o += SV.path("M150,125 H280", "ax") + SV.text(215, 118, "1 ——< M", "sm", { "text-anchor": "middle" });
    o += SV.text(20, 175, ["", "CustomerID: PK in CUSTOMER, FK in PURCHASE", "PurchaseID: PK in PURCHASE, FK in PURCHASE_ITEM", "PlantName: PK in PLANT, FK in PURCHASE_ITEM"][k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stA"), { w: 440, h: 190, label: "E-R", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Four tables, no relationships drawn yet.", "CustomerID is a foreign key in PURCHASE: <b>CUSTOMER 1:M PURCHASE</b>.", "PurchaseID is a foreign key in PURCHASE_ITEM: <b>PURCHASE 1:M PURCHASE_ITEM</b>.", "PlantName is a foreign key in PURCHASE_ITEM: <b>PLANT 1:M PURCHASE_ITEM</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, k === 0 ? "StudentName   Subject (list)   SubjectCode (list)" : "StudentID  FirstName  LastName  |  StudentID  SubjectCode", "lbl bd", { style: "font-size:13px" });
    const rows = k === 0 ? ["Yuwei Chen   English, Maths, CS   EN, MA, CS", "Claudia Raj   Maths, Physics, Art   MA, PY, AR"] : ["S1  Yuwei  Chen   |   S1  EN", "S1  Yuwei  Chen   |   S1  MA", "S2  Claudia  Raj   |   S2  MA"]; rows.forEach((r, i) => o += SV.rect(20, 32 + i * 28, 480, 24, k === 0 ? "f2" : "f1", { rx: 4 }) + SV.text(30, 49 + i * 28, r, "lbl", { style: "font-size:12px" })); o += SV.text(20, 135, k === 0 ? "repeating groups and a name that holds two items" : "atomic fields; repeating group moved to its own table: 1NF", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 540, h: 150, label: "1NF", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["The table has <b>repeating groups</b> (lists of subjects) and a name that is not atomic.", "<b>1NF</b>: split the name, give a key and move the subjects into a table with one row each."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; const T = (x, y, n, rows, on) => { let r = SV.rect(x, y, 230, 22 + rows.length * 20, on ? "f1" : "cell", { rx: 5 }) + SV.text(x + 8, y + 15, n, "lbl bd", { style: "font-size:12px" }); rows.forEach((t, i) => r += SV.text(x + 8, y + 35 + i * 20, t, "lbl", { style: "font-size:11px" })); return r; };
    if (k === 0) o += T(20, 20, "STUDENT_SUBJECT", ["StudentID, SubjectCode, Subject", "(Subject depends on SubjectCode only)"], true); if (k === 1) o += T(20, 20, "STUDENT_SUBJECT", ["StudentID, SubjectCode"], true) + T(280, 20, "SUBJECT", ["SubjectCode, Subject"], true); if (k >= 2) o += T(20, 20, "STUDENT", ["StudentID, ..., TutorGroup"], true) + T(280, 20, "TUTOR_GROUP", ["TutorGroup, TutorName"], true);
    o += SV.text(20, 120, ["partial dependency: Subject depends on part of the key", "2NF: Subject moved into its own table", "3NF: TutorName depends on TutorGroup, so it moves to its own table"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 540, h: 140, label: "2NF and 3NF", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Subject depends only on SubjectCode, part of the composite key: a <b>partial dependency</b>.", "<b>2NF</b>: move it to a SUBJECT table.", "<b>3NF</b>: TutorName depends on TutorGroup, a <b>non-key dependency</b>: move it to its own table."].map((c, i) => ({ cap: c, s: { i } })) });
})();

btnTable("nB", "nO", [
  ["A cell holds 'English, Maths, Physics'", "1NF broken", "A repeating group; data is not atomic"],
  ["Subject name depends only on SubjectCode in a table keyed (StudentID, SubjectCode)", "2NF broken", "A partial dependency"],
  ["TutorName depends on TutorGroup, which is not the key", "3NF broken", "A non-key (transitive) dependency"],
  ["Every field depends on the primary key and nothing else", "In 3NF", "All three rules satisfied"]
], ["Problem", "Result", "Why"]);
btnTable("fB", "fO", [
  ["CustomerID in SHOP_ORDER (PK in CUSTOMER)", "CUSTOMER 1:M SHOP_ORDER", "FK table is the many side"],
  ["ShipID in CONTAINER (PK in SHIP)", "SHIP 1:M CONTAINER", "One ship, many containers"],
  ["OrderNo and ItemNumber in ORDER_ITEM", "Linking table: SHOP_ORDER 1:M ORDER_ITEM, ITEM 1:M ORDER_ITEM", "Two FKs"],
  ["StaffID in COMPLAINT (PK in STAFF)", "STAFF 1:M COMPLAINT", "One staff member, many complaints"]
], ["Foreign key", "Relationship", "Why"]);
$("#eG").innerHTML = "<svg viewBox=\"0 0 470 215\" style=\"width:470px;max-width:100%;display:block\" role=\"img\" aria-label=\"demo\"><line class=\"w\" x1=\"95.0\" y1=\"44.0\" x2=\"95.0\" y2=\"90.0\"/><line class=\"w\" x1=\"88.0\" y1=\"56.0\" x2=\"102.0\" y2=\"56.0\"/><line class=\"w\" x1=\"95.0\" y1=\"76.0\" x2=\"87.0\" y2=\"90.0\"/><line class=\"w\" x1=\"95.0\" y1=\"76.0\" x2=\"95.0\" y2=\"90.0\"/><line class=\"w\" x1=\"95.0\" y1=\"76.0\" x2=\"103.0\" y2=\"90.0\"/><line class=\"w\" x1=\"123.7\" y1=\"124.0\" x2=\"201.3\" y2=\"170.0\"/><line class=\"w\" x1=\"116.7\" y1=\"136.0\" x2=\"130.7\" y2=\"136.0\"/><line class=\"w\" x1=\"201.3\" y1=\"156.0\" x2=\"193.3\" y2=\"170.0\"/><line class=\"w\" x1=\"201.3\" y1=\"156.0\" x2=\"201.3\" y2=\"170.0\"/><line class=\"w\" x1=\"201.3\" y1=\"156.0\" x2=\"209.3\" y2=\"170.0\"/><line class=\"w\" x1=\"336.3\" y1=\"124.0\" x2=\"258.7\" y2=\"170.0\"/><line class=\"w\" x1=\"329.3\" y1=\"136.0\" x2=\"343.3\" y2=\"136.0\"/><line class=\"w\" x1=\"258.7\" y1=\"156.0\" x2=\"250.7\" y2=\"170.0\"/><line class=\"w\" x1=\"258.7\" y1=\"156.0\" x2=\"258.7\" y2=\"170.0\"/><line class=\"w\" x1=\"258.7\" y1=\"156.0\" x2=\"266.7\" y2=\"170.0\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"20\" y=\"10\" width=\"150\" height=\"34\" rx=\"4\"/><text class=\"lbl bd\" x=\"95.0\" y=\"31.0\" text-anchor=\"middle\" style=\"font-size:11px\">CUSTOMER</text><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"20\" y=\"90\" width=\"150\" height=\"34\" rx=\"4\"/><text class=\"lbl bd\" x=\"95.0\" y=\"111.0\" text-anchor=\"middle\" style=\"font-size:11px\">SHOP_ORDER</text><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"155\" y=\"170\" width=\"150\" height=\"34\" rx=\"4\"/><text class=\"lbl bd\" x=\"230.0\" y=\"191.0\" text-anchor=\"middle\" style=\"font-size:11px\">ORDER_ITEM</text><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"290\" y=\"90\" width=\"150\" height=\"34\" rx=\"4\"/><text class=\"lbl bd\" x=\"365.0\" y=\"111.0\" text-anchor=\"middle\" style=\"font-size:11px\">ITEM</text></svg>" + '<p class="note">The shop database: CUSTOMER 1:M SHOP_ORDER, SHOP_ORDER 1:M ORDER_ITEM, ITEM 1:M ORDER_ITEM (ORDER_ITEM is the linking table that makes orders and items many-to-many).</p>';
Lib.classify($("#cl1"), { prompt: "Which normal form does this problem break?", buckets: [{"label": "1NF"}, {"label": "2NF"}, {"label": "3NF"}], items: [{"text": "A field holds a list of subjects", "b": 0}, {"text": "An attribute depends on only part of a composite key", "b": 1}, {"text": "An attribute depends on another non-key attribute", "b": 2}, {"text": "The same group of fields repeats on every row", "b": 0}, {"text": "Partial dependency", "b": 1}, {"text": "Transitive (non-key) dependency", "b": 2}], done: "1NF: repeats. 2NF: part of the key. 3NF: non-key." });
Lib.classify($("#cl2"), { prompt: "In an E-R diagram, is the table on the one side or the many side?", buckets: [{"label": "One side"}, {"label": "Many side"}], items: [{"text": "CUSTOMER, where CustomerID is the primary key", "b": 0}, {"text": "SHOP_ORDER, which holds the foreign key CustomerID", "b": 1}, {"text": "SHIP, where ShipID is the primary key", "b": 0}, {"text": "CONTAINER, which holds the foreign key ShipID", "b": 1}, {"text": "PLANT in PLANT to PURCHASE_ITEM", "b": 0}, {"text": "PURCHASE_ITEM in PURCHASE to PURCHASE_ITEM", "b": 1}], done: "The foreign key table is the many side." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["1NF", "No repeating groups; fields are atomic"], ["2NF", "No partial dependencies on a composite key"], ["3NF", "No non-key (transitive) dependencies"], ["Linking table", "Breaks up a many-to-many relationship"], ["Atomic", "A field holds one value only"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the normalisation steps in order.", items: ["Identify the primary key and make every field atomic", "Move repeating groups into their own table", "Remove partial dependencies (2NF)", "Remove non-key dependencies (3NF)", "Check every table has a primary key and foreign keys link them"], done: "1NF, repeats, 2NF, 3NF, keys." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many tables are there in the 3NF example in the Learn tab (STUDENT, STUDENT_SUBJECT, SUBJECT, TUTOR_GROUP)?", "a": 4, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>4</b>."},
  {"q": "A linking table joins two tables. How many one-to-many relationships does it make?", "a": 2, "unit": "", "tol": 0.01, "hint": "One to each.", "sol": "<b>2</b>."},
  {"q": "In PLANTSALES there are 4 tables and 3 relationships. How many foreign keys are needed (one per relationship)?", "a": 3, "unit": "", "tol": 0.01, "hint": "One per line.", "sol": "<b>3</b>."},
  {"q": "A table has a composite key (A, B) and attribute C depends only on A. Which normal form does it break? Answer 2 for 2NF.", "a": 2, "unit": "", "tol": 0.01, "hint": "Partial dependency.", "sol": "<b>2</b> (2NF)."},
  {"q": "A student with 3 subjects is stored in 1 row with 3 subject columns (repeating group). In 1NF the subjects are moved to a table with one row per subject: how many rows for 3 subjects?", "a": 3, "unit": "", "tol": 0.01, "hint": "One per subject.", "sol": "<b>3</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The crow's foot is drawn at:", opts: ["The many end", "The one end", "Neither", "Both"], a: 0, why: "Many end." },
  { q: "3NF removes:", opts: ["Non-key dependencies", "Primary keys", "Foreign keys", "All tables"], a: 0, why: "Non-key dependencies." },
  { q: "A repeating group breaks:", opts: ["1NF", "2NF", "3NF", "None"], a: 0, why: "1NF." },
  { q: "2NF needs no:", opts: ["Partial dependencies", "Primary keys", "Records", "Tables"], a: 0, why: "Partial." },
  { q: "A many-to-many relationship is broken up with:", opts: ["A linking table", "A larger field", "An index", "A view"], a: 0, why: "Linking table." },
  { q: "An atomic field:", opts: ["Holds one value", "Is a key", "Is empty", "Is a table"], a: 0, why: "One value." },
] });
Lib.cards($("#fc1"), { cards: [
  ["E-R diagram", "Boxes for tables; lines for relationships."],
  ["Crow's foot", "The many end of a relationship."],
  ["1NF", "No repeating groups; atomic."],
  ["2NF", "No partial dependencies."],
  ["3NF", "No non-key dependencies."],
  ["Linking table", "Two foreign keys; two 1:M."],
  ["Partial dependency", "Depends on part of a composite key."],
  ["Transitive dependency", "Depends on a non-key attribute."],
] });
