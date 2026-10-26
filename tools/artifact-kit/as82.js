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
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 110, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 55, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); let o = B(10, "user criteria", k >= 0) + B(140, "query processor", k >= 1) + B(270, "tables", k >= 2) + B(400, "results shown", k >= 4) + SV.path("M120,62 H140", "ax") + SV.path("M250,62 H270", "ax") + SV.path("M380,62 H400", "ax"); return o; };
  Lib.stepper($("#stA"), { w: 530, h: 110, label: "Query", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["The user enters criteria.", "The <b>query processor</b> reads them.", "It searches the tables for matching data.", "It organises the results.", "The results are displayed."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const rows = [["Ann", "Shop 1", "£500"], ["Bob", "Shop 2", "£700"], ["Cy", "Shop 1", "£300"]]; let o = SV.text(20, 20, k === 0 ? "Owner sees all rows" : "Manager of Shop 1 sees a view", "lbl bd", { style: "font-size:13px" }); rows.forEach((r, i) => { const show = k === 0 || r[1] === "Shop 1"; o += SV.rect(20, 30 + i * 30, 360, 24, show ? "f1" : "cell", { rx: 4, ...(show ? {} : op(0.3)) }) + (show ? SV.text(30, 47 + i * 30, r.join("   "), "lbl", { style: "font-size:12px" }) : ""); }); return o; };
  Lib.stepper($("#stB"), { w: 420, h: 130, label: "Views", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["The owner has full access to every row.", "A <b>view</b> and access rights show the Shop 1 manager only the rows they need."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 40, 120, 40, "cell", { rx: 6 }) + SV.text(80, 65, "User A", "lbl bd", { "text-anchor": "middle" }) + SV.rect(20, 100, 120, 40, "cell", { rx: 6 }) + SV.text(80, 125, "User B", "lbl bd", { "text-anchor": "middle" }) + SV.rect(260, 70, 160, 40, k >= 1 ? "f2" : "f1", { rx: 6 }) + SV.text(340, 95, k >= 1 ? "record locked" : "record", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.path("M140,60 L260,85", "ax"); if (k >= 2) o += SV.text(150, 128, "waits for the lock", "sm"); if (k >= 3) o += SV.path("M140,120 L260,100", "ax") + SV.text(340, 135, "A's update saved first", "sm", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stC"), { w: 460, h: 150, label: "Locking", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Two users want to edit the same record.", "User A opens it: the DBMS <b>locks</b> the record.", "User B has to wait.", "A saves, the lock is released, then B can edit: no update is lost."].map((c, i) => ({ cap: c, s: { i } })) });
})();
btnTable("aB", "aO", [
  ["Owner", "Full access: read, write, delete all tables", "Administrator"],
  ["Manager of one shop", "Read and write for own shop through a view", "Sees only their shops"],
  ["Till operator", "Add new sales only", "Cannot see other data"],
  ["Student visitor", "No access", "Not authorised"]
], ["User", "Allowed", "Why"]);
btnTable("tB", "tO", [
  ["Where are the field names and data types stored?", "Data dictionary", "Metadata"],
  ["Which tool shows the structure as an E-R diagram?", "Logical schema", "Independent of the DBMS"],
  ["Which tool finds the matching rows for a search?", "Query processor", "Criteria in, results out"],
  ["Which tool lets me build a data entry form?", "Developer interface", "Forms, reports, tables"]
], ["Question", "Tool", "Why"]);
btnTable("sB", "sO", [
  ["Only some staff can edit customer data", "Access rights", "Different permissions"],
  ["Managers see only their own shop's rows", "Views", "Part of the database"],
  ["Data stays unreadable if stolen", "Encryption", "Cipher text"],
  ["Data restored after a server failure", "Back-up and recovery", "Copies"],
  ["Two edits at once do not overwrite each other", "Record locking", "One at a time"]
], ["Need", "Method", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which DBMS tool does it describe?", buckets: [{"label": "Data dictionary"}, {"label": "Logical schema"}, {"label": "Query processor"}, {"label": "Developer interface"}], items: [{"text": "Stores field names and data types", "b": 0}, {"text": "A model of the database not specific to one DBMS", "b": 1}, {"text": "Finds the data that matches the user's criteria", "b": 2}, {"text": "Lets the user create forms and reports", "b": 3}, {"text": "Stores validation rules and keys", "b": 0}, {"text": "Uses an E-R diagram to show structure", "b": 1}], done: "Match the tool." });
Lib.classify($("#cl2"), { prompt: "Does it support security or integrity?", buckets: [{"label": "Security"}, {"label": "Integrity"}], items: [{"text": "Access rights", "b": 0}, {"text": "Referential integrity", "b": 1}, {"text": "Views", "b": 0}, {"text": "Validation rules", "b": 1}, {"text": "Encryption", "b": 0}, {"text": "Cascading updates and deletes", "b": 1}], done: "Access, views, encryption: security." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Data dictionary", "Metadata: data about the data"], ["Logical schema", "A model independent of any DBMS"], ["Query processor", "Searches for data meeting criteria"], ["Developer interface", "Tools to build tables, forms and reports"], ["View", "A user sees only part of the database"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the query steps in order.", items: ["The user enters criteria", "The query processor reads the criteria", "It searches the tables for matching data", "It organises the results", "The results are displayed to the user"], done: "Enter, read, search, organise, display." });
Lib.calc($("#c1"), { qs: [
  {"q": "A back-up is taken every day and kept for 14 days. How many back-ups are kept?", "a": 14, "unit": "", "tol": 0.01, "hint": "One a day.", "sol": "<b>14</b>."},
  {"q": "A table has 5 users; 2 have full access, 2 read-only and 1 none. How many can read it?", "a": 4, "unit": "", "tol": 0.01, "hint": "2 + 2.", "sol": "<b>4</b>."},
  {"q": "Two users update a record of 100 at the same time, each adding 10, with no locking. The final value is 110 instead of 120. How many units are lost?", "a": 10, "unit": "", "tol": 0.01, "hint": "120 − 110.", "sol": "<b>10</b>."},
  {"q": "A data dictionary holds 6 tables with 8 fields each. How many field entries?", "a": 48, "unit": "", "tol": 0.01, "hint": "6 × 8.", "sol": "<b>48</b>."},
  {"q": "How many security methods are in the Learn tab table?", "a": 6, "unit": "", "tol": 0.01, "hint": "Count rows.", "sol": "<b>6</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The data dictionary stores:", opts: ["Metadata", "Only passwords", "Query results", "Back-ups"], a: 0, why: "Metadata." },
  { q: "A view lets a user:", opts: ["See only part of the database", "Delete tables", "Change keys", "Compile SQL"], a: 0, why: "Part only." },
  { q: "The query processor:", opts: ["Finds data matching criteria", "Creates forms", "Encrypts data", "Draws E-R diagrams"], a: 0, why: "Criteria." },
  { q: "Record locking prevents:", opts: ["Lost updates", "Large tables", "Passwords", "Views"], a: 0, why: "Lost updates." },
  { q: "The logical schema is:", opts: ["Independent of any DBMS", "A table", "An SQL query", "A password"], a: 0, why: "Independent." },
  { q: "Access rights:", opts: ["Give users different permissions", "Store keys", "Make tables", "Search data"], a: 0, why: "Permissions." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Data dictionary", "Metadata: names, types, rules, keys."],
  ["Logical schema", "Model of the database, not DBMS-specific."],
  ["Query processor", "Criteria in, results out."],
  ["Developer interface", "Tables, forms, reports, SQL."],
  ["Access rights", "Different permissions per user."],
  ["View", "Part of the database for a user."],
  ["Record locking", "Stops lost updates."],
  ["Back-up", "Recover lost data."],
] });
