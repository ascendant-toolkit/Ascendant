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
/* ---------- 1. choosing types ---------- */
const DT = [["PhoneNumber", "0912 345 678", "Text", "Starts with 0; no calculations"], ["Price", "4.50", "Real", "Has a fractional part"], ["Quantity", "12", "Integer", "A whole number"], ["DateOfBirth", "14/05/2009", "Date/time", "A date"], ["Sex", "F", "Character", "A single character"], ["InStock", "TRUE", "Boolean", "Only two values"]];
function dtChart(s) {
  const k = Math.round(s.k); let o = ["Field", "Example value", "Data type", "Why"].map((h, i) => SV.text([20, 190, 340, 500][i], 26, h, "lbl bd t1", { "text-anchor": "start" })).join("") + SV.line(20, 36, 740, 36, "", { style: "stroke:var(--muted);stroke-width:2" });
  DT.forEach((r, i) => { const y = 62 + i * 42, on = i === k - 1, vis = i < k; if (!vis) return; o += SV.rect(14, y - 22, 730, 36, "", { rx: 8, style: `fill:${on ? "var(--accent-soft)" : "var(--surface)"};stroke:${on ? "var(--accent)" : "var(--line)"};stroke-width:${on ? 3 : 1}` }) + SV.text(20, y, r[0], "lbl bd", { "text-anchor": "start", style: "font-family:var(--mono);font-size:13px" }) + SV.text(190, y, r[1], "lbl", { "text-anchor": "start", style: "font-family:var(--mono);font-size:13px" }) + SV.text(340, y, r[2], "lbl bd t3", { "text-anchor": "start" }) + SV.text(500, y, r[3], "sm", { "text-anchor": "start" }); });
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 300, label: "Choosing data types", base: { k: 1 }, tween: 1, dwell: 3200, draw: dtChart, steps: [
  { cap: "<b>PhoneNumber</b> is <b>text</b>: it can start with 0, and you never do arithmetic with it.", s: { k: 1 } },
  { cap: "<b>Price</b> has a fractional part, so it is <b>real</b>.", s: { k: 2 } },
  { cap: "<b>Quantity</b> is a whole number: <b>integer</b>.", s: { k: 3 } },
  { cap: "<b>DateOfBirth</b> is <b>date/time</b>, so dates can be sorted and compared.", s: { k: 4 } },
  { cap: "A single letter such as <b>F</b> is <b>character</b>.", s: { k: 5 } },
  { cap: "<b>InStock</b> can only be TRUE or FALSE: <b>Boolean</b>.", s: { k: 6 } },
] });

/* ---------- 2. primary key ---------- */
const PK = [["1001", "Sam Lee", "10", "15/03/2010"], ["1002", "Ana Cho", "10", "15/03/2010"], ["1003", "Sam Lee", "9", "02/11/2011"], ["1004", "Bo Kim", "10", "21/07/2010"]];
function pkChart(s) {
  const k = Math.round(s.k), cw = 150, x0 = 90, hd = ["StudentID", "Name", "Year", "DateOfBirth"]; let o = "";
  hd.forEach((h, c) => { const on = (k === 1 && c === 1) || (k === 2 && c === 2) || (k === 3 && c === 3) || (k === 4 && c === 0); o += SV.rect(x0 + c * cw, 15, cw - 6, 38, "", { rx: 6, style: `fill:${on ? (k === 4 ? "var(--good-soft)" : "var(--bad-soft)") : "var(--soft)"};stroke:${on ? (k === 4 ? "var(--good)" : "var(--bad)") : "var(--line)"};stroke-width:${on ? 3 : 1.5}` }) + SV.text(x0 + c * cw + cw / 2 - 3, 40, h + (k === 4 && c === 0 ? " ★" : ""), "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); });
  PK.forEach((r, i) => r.forEach((v, c) => { const dup = (k === 1 && c === 1 && (i === 0 || i === 2)) || (k === 2 && c === 2 && i !== 2) || (k === 3 && c === 3 && (i === 0 || i === 1)), good = k === 4 && c === 0; o += SV.rect(x0 + c * cw, 60 + i * 42, cw - 6, 36, "", { rx: 6, style: `fill:${dup ? "var(--bad-soft)" : good ? "var(--good-soft)" : "var(--surface)"};stroke:${dup ? "var(--bad)" : good ? "var(--good)" : "var(--line)"};stroke-width:${dup || good ? 3 : 1.5}` }) + SV.text(x0 + c * cw + cw / 2 - 3, 84 + i * 42, v, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:14px" }); }));
  o += note(380, 262, ["Which field could identify one record only?", "Name: two students are called Sam Lee, so it repeats", "Year: most students share a year, so it repeats", "DateOfBirth: two students share a birthday, so it repeats", "StudentID: every value is different, so it is unique"][k], k === 4 ? "t3" : k ? "t2" : "t1");
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 280, label: "Finding a good primary key", base: { k: 0 }, tween: 1, dwell: 3500, draw: pkChart, steps: [
  { cap: "A <b>primary key</b> must be <b>unique</b> for every record. Which of these fields could work?", s: { k: 0 } },
  { cap: "<b>Name</b>: two students are called Sam Lee. A repeated value means it is <b>not suitable</b>.", s: { k: 1 } },
  { cap: "<b>Year</b>: three students are in Year 10. <b>Not suitable</b>.", s: { k: 2 } },
  { cap: "<b>DateOfBirth</b>: two students were born on the same day. <b>Not suitable</b>.", s: { k: 3 } },
  { cap: "<b>StudentID</b>: every value is different and none is empty. It is a <b>suitable primary key</b>.", s: { k: 4 } },
] });

/* ---------- Lab 1 ---------- */
chooser($("#sn"), $("#sv"), ["Text", "Character", "Boolean", "Integer", "Real", "Date/time"], [
  ["Telephone number", "Text"], ["Number of siblings", "Integer"], ["Height in metres", "Real"], ["Date of birth", "Date/time"], ["Is the member a student? (yes or no)", "Boolean"], ["Initial of the middle name", "Character"], ["Postcode", "Text"], ["Price of a book", "Real"], ["Appointment time", "Date/time"], ["Number of books in stock", "Integer"],
]);

/* ---------- Lab 2 ---------- */
(() => {
  const H = ["StudentID", "Name", "Year", "Form", "DateOfBirth", "Email"], D = [
    ["1001", "Sam Lee", "10", "10B", "15/03/2010", "sam@sch.org"], ["1002", "Ana Cho", "10", "10A", "15/03/2010", "ana@sch.org"], ["1003", "Sam Lee", "9", "9A", "02/11/2011", ""], ["1004", "Bo Kim", "10", "10B", "21/07/2010", "bo@sch.org"],
    ["1005", "Cy Diaz", "11", "11C", "09/01/2009", "cy@sch.org"], ["1006", "Dee Kay", "9", "9A", "30/05/2011", ""], ["1007", "Eli Moss", "10", "10A", "11/12/2010", "eli@sch.org"], ["1008", "Fay Ito", "11", "11C", "04/04/2009", "fay@sch.org"]];
  const t = $("#pk"), sel = $("#pf"), v = $("#pv"); sel.innerHTML = H.map((h, i) => `<option value="${i}">${h}</option>`).join("");
  function upd() { const c = +sel.value, vals = D.map((r) => r[c]), blank = vals.filter((x) => x === "").length, dups = vals.filter((x, i) => x !== "" && vals.indexOf(x) !== i).length;
    t.innerHTML = `<tr>${H.map((h, i) => `<th style="${i === c ? "background:var(--accent-soft)" : ""}">${h}</th>`).join("")}</tr>` + D.map((r) => `<tr>${r.map((x, i) => `<td style="${i === c ? "background:var(--accent-soft)" : ""}">${x || "<i>empty</i>"}</td>`).join("")}</tr>`).join("");
    v.innerHTML = dups || blank ? `<span class="flag">Not suitable</span> ${H[c]} ${dups ? `has <b>${dups} repeated value${dups > 1 ? "s" : ""}</b>` : ""}${dups && blank ? " and " : ""}${blank ? `has <b>${blank} empty value${blank > 1 ? "s" : ""}</b>` : ""}. A primary key must be <b>unique</b> and <b>never empty</b>.` : `<span class="okf">Suitable</span> Every value in ${H[c]} is different and none is empty, so it can identify exactly one record.`; }
  sel.onchange = upd; upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  const inp = $("#tv"), t = $("#tt");
  function upd() {
    const s = inp.value, fit = [["Text / alphanumeric", s.length >= 0], ["Character", s.length === 1], ["Boolean", /^(true|false|yes|no)$/i.test(s.trim())], ["Integer", /^-?\d+$/.test(s.trim())], ["Real", /^-?\d+\.\d+$/.test(s.trim()) || /^-?\d+$/.test(s.trim())], ["Date/time", /^\d{1,2}\/\d{1,2}\/\d{4}$/.test(s.trim()) || /^\d{1,2}:\d{2}$/.test(s.trim())]];
    t.innerHTML = `<tr><th>Data type</th><th>Could hold "${esc(s)}"?</th></tr>` + fit.map((f) => `<tr><td>${f[0]}</td><td>${f[1] ? '<span class="okf">Yes</span>' : '<span class="flag">No</span>'}</td></tr>`).join("") + `<tr><td colspan="2" class="note">Many values fit several types. Choose the type that matches what the data <b>means</b> (a telephone number could be digits, but it is text).</td></tr>`;
  }
  inp.addEventListener("input", upd); upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Choose the data type for each field.", buckets: [{ label: "Text" }, { label: "Character" }, { label: "Boolean" }, { label: "Integer" }, { label: "Real" }, { label: "Date/time" }], items: [
  { text: "Surname", b: 0 },
  { text: "Telephone number", b: 0 },
  { text: "Grade (a single letter)", b: 1 },
  { text: "Initial", b: 1 },
  { text: "IsMember", b: 2 },
  { text: "HasPaid", b: 2 },
  { text: "Number of siblings", b: 3 },
  { text: "Quantity in stock", b: 3 },
  { text: "Height in metres", b: 4 },
  { text: "Price", b: 4 },
  { text: "Date of birth", b: 5 },
  { text: "Appointment time", b: 5 },
], done: "Match the field to its type." });

Lib.classify($("#cl2"), { prompt: "Is each field a suitable primary key for a table of students?", buckets: [{ label: "Suitable" }, { label: "Unsuitable" }], items: [
  { text: "StudentID (a unique number)", b: 0 },
  { text: "Passport number", b: 0 },
  { text: "Email address (unique, never empty)", b: 0 },
  { text: "Surname", b: 1 },
  { text: "FirstName", b: 1 },
  { text: "Year", b: 1 },
  { text: "DateOfBirth", b: 1 },
  { text: "Form", b: 1 },
], done: "Unique and never empty." });

Lib.match($("#m1"), { prompt: "Match each field to its most suitable data type.", pairs: [
  ["Telephone number", "Text"],
  ["Number of books", "Integer"],
  ["Weight in kg", "Real"],
  ["Date of birth", "Date/time"],
  ["Overdue (yes or no)", "Boolean"],
  ["Grade (A, B or C)", "Character"]
] });

Lib.calc($("#c1"), { qs: [
  { q: "A table has a StudentID that is unique for each of 250 students. How many different StudentID values are in the table?", a: 250, sol: "One per student: 250." },
  { q: "A field called Mark holds whole numbers from 0 to 100. How many different values are allowed?", a: 101, sol: "0 to 100 inclusive is 101 values." },
  { q: "How many data types are in the IGCSE list? (text, character, Boolean, integer, real, date/time)", a: 6, sol: "Six." },
  { q: "In 2 records out of 8, a field has the same value as another record. Could it be a primary key? (1 = yes, 0 = no)", a: 0, sol: "Repeated values mean it is not unique, so no." },
  { q: "A primary key has 4 digits (1000 to 9999). How many records can the table hold before the keys run out?", a: 9000, sol: "9999 − 1000 + 1 = 9000." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "Which data type suits a telephone number?", opts: ["Text", "Integer", "Real", "Boolean"], a: 0, why: "No arithmetic, and it may start with 0." },
  { q: "Which data type suits a price?", opts: ["Real", "Boolean", "Character", "Date/time"], a: 0, why: "Prices have decimals." },
  { q: "Which suits a yes/no field?", opts: ["Boolean", "Text", "Real", "Integer"], a: 0, why: "Boolean has two values." },
  { q: "What is a primary key?", opts: ["A field whose value is unique for every record", "The first field", "A password", "The largest field"], a: 0, why: "It uniquely identifies a record." },
  { q: "Which is the best primary key?", opts: ["StudentID", "Surname", "Year", "Form"], a: 0, why: "It is different for every student." },
  { q: "Which type suits a single letter such as M or F?", opts: ["Character", "Integer", "Date/time", "Real"], a: 0, why: "Character stores one character." },
  { q: "Why can a Name not be a primary key?", opts: ["Two records may have the same name", "Names are too short", "Names are numbers", "Names are always empty"], a: 0, why: "Keys must be unique." },
  { q: "Which type suits a date of birth?", opts: ["Date/time", "Text", "Boolean", "Character"], a: 0, why: "Date/time can be sorted and compared." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Data type", "The kind of data a field can hold."],
  ["Text / alphanumeric", "Letters, digits and symbols in any mix."],
  ["Character", "A single character."],
  ["Boolean", "TRUE or FALSE."],
  ["Integer", "A whole number."],
  ["Real", "A number with a fractional part."],
  ["Date/time", "A date, a time, or both."],
  ["Primary key", "A field whose value is unique for every record."],
  ["Unique", "No two records have the same value in that field."]
] });
