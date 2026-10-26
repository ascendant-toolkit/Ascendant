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
const EMP = [{"n": 123, "name": "Smith,Eric", "dept": "1B", "att": 97.4}, {"n": 124, "name": "Lopez,Ana", "dept": "2A", "att": 88.5}, {"n": -1, "name": "", "dept": "", "att": 0}, {"n": 126, "name": "Okoye,Ben", "dept": "1B", "att": 71.0}, {"n": 127, "name": "Zhang,Cleo", "dept": "3C", "att": 90.0}];
(function () {
  const draw = (s) => { const k = Math.round(s.i); const fl = [["EmployeeNumber", "123", "INTEGER"], ["Name", "\"Smith,Eric\"", "STRING"], ["Born", "13/02/2006", "DATE"], ["Attendance", "97.40", "REAL"]]; let o = SV.rect(20, 10, 440, 24, "f3", { rx: 4 }) + SV.text(28, 27, "TYPE Employee", "lbl bd", { style: "font-size:12px" }); fl.forEach((f, i) => { if (i < k + 1) o += SV.rect(20, 40 + i * 30, 440, 26, "cell", { rx: 4 }) + SV.text(28, 58 + i * 30, "DECLARE " + f[0] + " : " + f[2], "lbl", { style: "font-size:12px" }) + SV.text(300, 58 + i * 30, f[1], "lbl bd t3", { style: "font-size:12px" }); }); if (k >= 4) o += SV.text(20, 175, "ENDTYPE", "lbl bd"); return o; };
  Lib.stepper($("#stA"), { w: 480, h: 190, label: "Record", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["A record starts with TYPE and its name.", "Each field has its own data type: INTEGER.", "STRING.", "DATE.", "REAL, then ENDTYPE. Different types, one identifier."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 16, "Staff : ARRAY [1:500] OF Employee", "lbl bd", { style: "font-size:12px" }); EMP.forEach((e, i) => { o += SV.rect(20, 24 + i * 28, 440, 24, e.n === -1 && k >= 2 ? "f2" : (k === 1 && i === 2 ? "f3" : "cell"), { rx: 4 }) + SV.text(28, 41 + i * 28, `[${i + 1}] ` + (e.n === -1 ? "EmployeeNumber -1  (unused)" : e.n + "  " + e.name + "  " + e.att), "lbl", { style: "font-size:11.5px" }); }); o += SV.text(20, 175, ["each element is one Employee record", "Staff[3].Name uses an index, then dot notation", "unused: marked with an impossible value, EmployeeNumber -1"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 480, h: 195, label: "Array of records", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["An array of five records (the real array has 500).", "<b>Staff[3]</b> picks one record; <b>.Name</b> picks a field.", "An unused element is marked with an impossible value."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; EMP.forEach((e, i) => { const unused = e.n === -1, hit = !unused && e.att <= 90; o += SV.rect(20, 10 + i * 28, 300, 24, i === k ? "f3" : i < k ? (unused ? "cell" : hit ? "f1" : "f2") : "cell", { rx: 4 }) + SV.text(28, 27 + i * 28, `[${i + 1}] ` + (unused ? "unused" : e.name + " " + e.att), "lbl", { style: "font-size:12px" }) + (i <= k ? SV.text(330, 27 + i * 28, unused ? "skip" : hit ? "output" : "no", "lbl bd t3", { style: "font-size:12px" }) : ""); }); return o; };
  Lib.stepper($("#stC"), { w: 420, h: 160, label: "Loop", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["Index 1: attendance 97.4 is above 90: not output.", "Index 2: 88.5 is 90 or less: output.", "Index 3: unused: skip.", "Index 4: 71.0: output.", "Index 5: 90.0 is 90 or less: output."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  let lim = 90; const paint = () => { const hits = EMP.filter((e) => e.n !== -1 && e.att <= lim); let o = '<div class="tw"><table class="t mono"><tr><th>Index</th><th>EmployeeNumber</th><th>Name</th><th>Attendance</th><th>Output?</th></tr>'; EMP.forEach((e, i) => { o += `<tr><td>${i + 1}</td><td>${e.n}</td><td>${e.name || ""}</td><td>${e.n === -1 ? "" : e.att}</td><td>${e.n === -1 ? "skipped (unused)" : e.att <= lim ? "<b>yes</b>" : "no"}</td></tr>`; }); $("#eG").innerHTML = o + "</table></div>"; $("#eV").innerHTML = `Attendance <= <b>${lim}</b>: <b>${hits.length}</b> employee(s) output` + (hits.length ? " (" + hits.map((h) => h.n).join(", ") + ")" : "") + ". The unused record is skipped by the first IF."; };
  Lib.slider($("#eS"), { id: "e1", label: "Attendance limit ", min: 60, max: 100, step: 0.5, value: lim, fmt: (x) => x.toFixed(1), onInput: (v) => { lim = v; paint(); } }); paint();
})();
btnTable("tB", "tO", [
  ["RentalID \"AB1234\"", "STRING", "Letters and digits in quotes"],
  ["CarID 241 (an array index)", "INTEGER", "Whole number"],
  ["DisCode 'S'", "CHAR", "One letter in single quotes"],
  ["Start 13/06/2025", "DATE", "A date"],
  ["Completed FALSE", "BOOLEAN", "TRUE or FALSE"],
  ["Limit_1 13.5", "REAL", "Decimal"]
], ["Field", "Type", "Why"]);
btnTable("dB", "dO", [
  ["Name of the 3rd employee", "Staff[3].Name", "Index then dot"],
  ["Attendance of the record at Index", "Staff[Index].Attendance", "Variable index"],
  ["Weight of the batch item at ThisIndex", "Batch[ThisIndex].Weight", "Same pattern"],
  ["Whether the Index-th loan is on loan", "Loan[Index].OnLoan", "BOOLEAN field"]
], ["Need", "Pseudocode", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which data type suits the value?", buckets: [{"label": "INTEGER"}, {"label": "REAL"}, {"label": "CHAR"}, {"label": "STRING"}, {"label": "BOOLEAN"}, {"label": "DATE"}], items: [{"text": "123478 (a numeric value used as an array index)", "b": 0}, {"text": "13.5 (a value in the range 0 to 100)", "b": 1}, {"text": "'B' (a letter for the stage of production)", "b": 2}, {"text": "\"AB1234\" (a unique alpha-numeric ID)", "b": 3}, {"text": "FALSE (TRUE if the item has been rejected)", "b": 4}, {"text": "13/06/2025 (when the rental starts)", "b": 5}], done: "Match the example and comment." });
Lib.classify($("#cl2"), { prompt: "Is it a feature of a record or of an array?", buckets: [{"label": "Record"}, {"label": "Array"}], items: [{"text": "Holds fields of different data types", "b": 0}, {"text": "Holds many items of the same type", "b": 1}, {"text": "Accessed with dot notation", "b": 0}, {"text": "Accessed with an index", "b": 1}, {"text": "Declared with TYPE ... ENDTYPE", "b": 0}, {"text": "Declared with ARRAY [1:500] OF ...", "b": 1}], done: "Record: mixed types. Array: same type, index." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Record", "A composite type holding several fields under one identifier"], ["Field", "One item of data inside a record"], ["Dot notation", "Staff[3].Name"], ["Array of records", "Many records reached by an index"], ["Unused element", "Marked with an impossible value"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the declaration of an array of records in order.", items: ["TYPE and the record name", "DECLARE each field with its data type", "ENDTYPE", "DECLARE the array with its bounds", "OF the record type"], done: "Type, fields, ENDTYPE, array, OF type." });
Lib.calc($("#c1"), { qs: [
  {"q": "An array of 500 Employee records has 120 unused elements. How many are in use?", "a": 380, "unit": "", "tol": 0.01, "hint": "500 − 120.", "sol": "<b>380</b>."},
  {"q": "A record has 5 fields. How many fields are there in 500 records?", "a": 2500, "unit": "", "tol": 0.01, "hint": "5 × 500.", "sol": "<b>2500</b>."},
  {"q": "A loop FOR Index ← 1 TO 500 skips unused records. If 380 are in use, how many are tested?", "a": 380, "unit": "", "tol": 0.01, "hint": "Only used ones.", "sol": "<b>380</b> (the loop passes 500 times; 120 are skipped)."},
  {"q": "Attendance values 97.4, 88.5, 71.0 and 90.0 are in use. How many are 90.00 or less?", "a": 3, "unit": "", "tol": 0.01, "hint": "88.5, 71.0, 90.0.", "sol": "<b>3</b>."},
  {"q": "An array is declared ARRAY [0:1999]. How many elements?", "a": 2000, "unit": "", "tol": 0.01, "hint": "0 to 1999.", "sol": "<b>2000</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A record can store:", opts: ["Different data types", "Only integers", "Only text", "Only one value"], a: 0, why: "Different types." },
  { q: "A CHAR holds:", opts: ["One character", "Many characters", "A date", "TRUE or FALSE"], a: 0, why: "One." },
  { q: "Which is valid dot notation?", opts: ["Item[1].Stage", "Item.Stage[1]", "Item[Stage]", "Stage.Item"], a: 0, why: "Item[1].Stage." },
  { q: "Unused records are marked with:", opts: ["An impossible value", "A random value", "Nothing", "A copy of the last record"], a: 0, why: "Impossible value." },
  { q: "A percentage such as 97.40 is:", opts: ["REAL", "INTEGER", "CHAR", "BOOLEAN"], a: 0, why: "REAL." },
  { q: "TYPE must be ended with:", opts: ["ENDTYPE", "END", "NEXT", "ENDIF"], a: 0, why: "ENDTYPE." },
] });
Lib.cards($("#fc1"), { cards: [
  ["INTEGER / REAL", "Whole / decimal numbers."],
  ["CHAR / STRING", "One character / text."],
  ["BOOLEAN / DATE", "TRUE or FALSE / a date."],
  ["Record", "TYPE ... ENDTYPE; mixed types."],
  ["Array of records", "Index plus dot notation."],
  ["Dot notation", "Staff[Index].Name"],
  ["Unused element", "Standard impossible value."],
  ["Benefit", "Mixed types, loops, simpler code."],
] });
