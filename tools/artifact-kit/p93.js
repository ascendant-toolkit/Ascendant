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
const DATA = [[1, 'Pencil', 'Stationery', 0.5, 200], [2, 'Notebook', 'Stationery', 2.25, 80], [3, 'Backpack', 'Bags', 24.99, 15], [4, 'Calculator', 'Electronics', 9.99, 40], [5, 'Headphones', 'Electronics', 19.5, 25], [6, 'Ruler', 'Stationery', 1.2, 120], [7, 'Lunchbox', 'Bags', 7.8, 30], [8, 'USB Drive', 'Electronics', 6.99, 0]];
const COLS = ["ID", "Name", "Category", "Price", "Stock"], NUM = { ID: 1, Price: 1, Stock: 1 };
/* ---------- 1. query pipeline ---------- */
const Q1 = (r) => r[2] === "Electronics";
const ORD = DATA.map((r, i) => [i, r]).filter(([i, r]) => Q1(r)).sort((a, b) => b[1][3] - a[1][3]).map((x) => x[0]);
function qState(k) {
  const s = { k }; DATA.forEach((r, i) => { const keep = Q1(r), rank = ORD.indexOf(i); s["y" + i] = k >= 2 ? (keep ? rank * 40 : 400 + i * 10) : i * 40; s["o" + i] = k >= 1 ? (keep ? 1 : 0.15) : 1; if (k >= 2 && !keep) s["o" + i] = 0; });
  s.cc = k >= 3 ? 0.12 : 1; return s;
}
function qChart(s) {
  const cx = [20, 70, 220, 360, 460], cw = [48, 148, 138, 98, 98]; let o = "";
  COLS.forEach((c, i) => (o += SV.text(cx[i] + cw[i] / 2, 22, c, "lbl bd t1", { "text-anchor": "middle", style: `opacity:${[1, 3].includes(i) ? 1 : s.cc}` })));
  o += SV.line(20, 32, 580, 32, "", { style: "stroke:var(--muted);stroke-width:2" });
  DATA.forEach((r, i) => { const y = 42 + s["y" + i]; if (s["o" + i] <= 0.01) return; o += SV.rect(16, y, 568, 34, "", { rx: 6, style: `fill:${s.k >= 1 && Q1(r) ? "var(--good-soft)" : "var(--surface)"};stroke:var(--line);stroke-width:1.5`, opacity: s["o" + i] });
    r.forEach((v, c) => (o += SV.text(cx[c] + cw[c] / 2, y + 22, c === 3 ? v.toFixed(2) : v, "lbl", { "text-anchor": "middle", style: `font-family:var(--mono);font-size:13px;opacity:${s["o" + i] * ([1, 3].includes(c) ? 1 : s.cc) }` }))); });
  return o;
}
Lib.stepper($("#stA"), { w: 600, h: 380, label: "A query running step by step", base: qState(0), tween: 900, dwell: 3800, draw: qChart, steps: [
  { cap: "The query: <b>SELECT Name, Price FROM Products WHERE Category = 'Electronics' ORDER BY Price DESC;</b> Step 1, <b>FROM</b>: start with every record in the Products table.", s: qState(0) },
  { cap: "Step 2, <b>WHERE Category = 'Electronics'</b>: keep only the matching records (green). The others drop out.", s: qState(1) },
  { cap: "Step 3, <b>ORDER BY Price DESC</b>: sort what is left, the most expensive first.", s: qState(2) },
  { cap: "Step 4, <b>SELECT Name, Price</b>: show only those two fields. Output: Headphones 19.50, Calculator 9.99, USB Drive 6.99.", s: qState(3) },
] });

/* ---------- 2. COUNT and SUM ---------- */
function agChart(s) {
  const k = Math.round(s.k); let o = SV.text(20, 24, "SELECT SUM(Stock) FROM Products WHERE Category = 'Electronics';", "lbl bd", { "text-anchor": "start", style: "font-family:var(--mono);font-size:13px" });
  let run = 0; DATA.forEach((r, i) => { const y = 44 + i * 34, hit = r[2] === "Electronics", seen = hit && DATA.slice(0, i + 1).filter((x) => x[2] === "Electronics").length <= k - 1; if (seen) run += r[4];
    const on = hit && seen; o += SV.rect(16, y, 500, 30, "", { rx: 6, style: `fill:${on ? "var(--good-soft)" : "var(--surface)"};stroke:${on ? "var(--good)" : "var(--line)"};stroke-width:${on ? 3 : 1.5};opacity:${k >= 1 && !hit ? 0.3 : 1}` }) + SV.text(30, y + 20, r[1], "lbl", { "text-anchor": "start", style: "font-family:var(--mono);font-size:13px" }) + SV.text(250, y + 20, r[2], "lbl", { "text-anchor": "start", style: "font-family:var(--mono);font-size:13px" }) + SV.text(480, y + 20, "Stock " + r[4], "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono);font-size:13px" }); });
  o += SV.rect(540, 60, 200, 110, "", { rx: 12, style: "fill:var(--surface);stroke:var(--accent);stroke-width:3" }) + SV.text(640, 90, k >= 4 ? "SUM(Stock)" : "running total", "lbl bd t1", { "text-anchor": "middle" }) + SV.text(640, 145, String(run), "lbl bd", { "text-anchor": "middle", style: "font-size:40px;font-family:var(--mono)" });
  if (k === 4) o += SV.text(640, 200, "COUNT(*) would give 3", "lbl bd t4", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 330, label: "SUM of a field for matching records", base: { k: 0 }, tween: 1, dwell: 3400, draw: agChart, steps: [
  { cap: "<b>SUM(Stock)</b> adds up the Stock values, but only for the records that pass the <b>WHERE</b> condition.", s: { k: 0 } },
  { cap: "Calculator is Electronics: Stock <b>40</b> is added. Running total 40.", s: { k: 1 } },
  { cap: "Headphones is Electronics: <b>25</b> is added. Running total 65.", s: { k: 2 } },
  { cap: "USB Drive is Electronics: Stock <b>0</b> is added. The total stays 65.", s: { k: 3 } },
  { cap: "Result: <b>SUM(Stock) = 65</b>. COUNT(*) would count the <b>records</b>, giving 3.", s: { k: 4 } },
] });

/* ---------- Lab 1: query builder ---------- */
(() => {
  const OPS = ["=", "<>", "<", "<=", ">", ">="], qf = $("#qf"), q = (id) => $(id);
  qf.innerHTML = COLS.map((c) => `<label><input type="checkbox" data-c="${c}" ${["Name", "Price"].includes(c) ? "checked" : ""}> ${c}</label>`).join("");
  ["w1f", "w2f"].forEach((id) => (q("#" + id).innerHTML = `<option value="">(no condition)</option>` + COLS.map((c) => `<option>${c}</option>`).join(""))); ["w1o", "w2o"].forEach((id) => (q("#" + id).innerHTML = OPS.map((o) => `<option>${o}</option>`).join("")));
  q("#of").innerHTML = `<option value="">(no order)</option>` + COLS.map((c) => `<option>${c}</option>`).join("");
  q("#w1f").value = "Category"; q("#w1v").value = "Electronics";
  const test = (r, f, op, v) => { const i = COLS.indexOf(f), a = r[i], b = NUM[f] ? parseFloat(v) : v; if (NUM[f] && isNaN(b)) return false; return { "=": a === b, "<>": a !== b, "<": a < b, "<=": a <= b, ">": a > b, ">=": a >= b }[op]; };
  const lit = (f, v) => (NUM[f] ? v : `'${v}'`);
  function upd() {
    const agg = q("#qa").value, fields = $$("input", qf).filter((i) => i.checked).map((i) => i.dataset.c);
    qf.style.opacity = agg ? 0.4 : 1;
    const conds = [[q("#w1f").value, q("#w1o").value, q("#w1v").value], [q("#w2f").value, q("#w2o").value, q("#w2v").value]].filter((c) => c[0] && c[2] !== "");
    let rows = DATA.filter((r) => !conds.length || (conds.length === 1 ? test(r, ...conds[0]) : q("#wl").value === "AND" ? test(r, ...conds[0]) && test(r, ...conds[1]) : test(r, ...conds[0]) || test(r, ...conds[1])));
    const of = q("#of").value; if (of) { const i = COLS.indexOf(of), d = q("#od").value === "DESC" ? -1 : 1; rows = [...rows].sort((a, b) => (a[i] < b[i] ? -d : a[i] > b[i] ? d : 0)); }
    let sql = "SELECT " + (agg || (fields.length ? fields.join(", ") : "*")) + "\nFROM Products"; if (conds.length) sql += "\nWHERE " + conds.map((c) => `${c[0]} ${c[1]} ${lit(c[0], c[2])}`).join(` ${q("#wl").value} `); if (of && !agg) sql += `\nORDER BY ${of} ${q("#od").value}`; sql += ";";
    q("#qs").textContent = sql;
    const t = q("#qt");
    if (agg) { const v = agg === "COUNT(*)" ? rows.length : agg === "SUM(Price)" ? Math.round(rows.reduce((a, r) => a + r[3], 0) * 100) / 100 : rows.reduce((a, r) => a + r[4], 0); t.innerHTML = `<tr><th>${agg}</th></tr><tr><td>${v}</td></tr>`; q("#qv").innerHTML = `${agg} of the <b>${rows.length}</b> matching record${rows.length === 1 ? "" : "s"}.`; return; }
    const cs = fields.length ? fields : COLS, idx = cs.map((c) => COLS.indexOf(c));
    t.innerHTML = `<tr>${cs.map((c) => `<th>${c}</th>`).join("")}</tr>` + rows.map((r) => `<tr>${idx.map((i) => `<td>${COLS[i] === "Price" ? r[i].toFixed(2) : r[i]}</td>`).join("")}</tr>`).join("");
    q("#qv").innerHTML = rows.length ? `<b>${rows.length}</b> record${rows.length === 1 ? "" : "s"} match the WHERE clause. SELECT then shows ${fields.length ? "the fields you ticked" : "every field"}.` : "No records match, so nothing is shown.";
  }
  $$("select,input", q("#explore")).filter((e) => e.closest(".card") && e.closest(".card").querySelector("#qs")).forEach((e) => { e.addEventListener("input", upd); e.addEventListener("change", upd); }); upd();
})();

/* ---------- Lab 2 ---------- */
chooser($("#sn"), $("#sv"), ["Missing quotes", "Clauses in the wrong order", "Missing comma", "SUM on a text field", "No error"], [
  ["<span class=\"ln2\">SELECT Name<br>FROM Products<br>WHERE Category = Stationery;</span>", "Missing quotes"],
  ["<span class=\"ln2\">SELECT Name<br>FROM Products<br>ORDER BY Price DESC<br>WHERE Stock &gt; 0;</span>", "Clauses in the wrong order"],
  ["<span class=\"ln2\">SELECT Name Price<br>FROM Products;</span>", "Missing comma"],
  ["<span class=\"ln2\">SELECT SUM(Name)<br>FROM Products;</span>", "SUM on a text field"],
  ["<span class=\"ln2\">SELECT Name, Price<br>FROM Products<br>WHERE Price &gt; 5<br>ORDER BY Price ASC;</span>", "No error"],
]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which SQL keyword does each description fit?", buckets: [{ label: "SELECT" }, { label: "FROM" }, { label: "WHERE" }, { label: "ORDER BY" }], items: [
  { text: "Chooses the fields to show", b: 0 },
  { text: "Can use * for all fields", b: 0 },
  { text: "Names the table", b: 1 },
  { text: "Chooses which records are included", b: 2 },
  { text: "Contains a condition such as Price > 5", b: 2 },
  { text: "Sorts the results", b: 3 },
  { text: "ASC or DESC follows it", b: 3 },
], done: "Fields, table, records, sort." });

Lib.match($("#m1"), { prompt: "Match each SQL statement or part to its meaning.", pairs: [
  ["COUNT(*)", "Counts the number of matching records"],
  ["SUM(Stock)", "Adds up the Stock values of matching records"],
  ["ORDER BY Price DESC", "Sorts with the highest price first"],
  ["WHERE A AND B", "Both conditions must be true"],
  ["WHERE A OR B", "At least one condition must be true"],
  ["SELECT *", "Shows all fields"]
] });

Lib.order($("#o1"), { prompt: "Put the lines of this query in the correct order.", items: [
  "SELECT Name, Price",
  "FROM Products",
  "WHERE Stock > 20",
  "ORDER BY Price ASC;"
], done: "SELECT, FROM, WHERE, ORDER BY." });

Lib.order($("#o2"), { prompt: "Put the steps of working out a query's output in order.", items: [
  "Start with all records in the table (FROM)",
  "Keep only the records that meet the condition (WHERE)",
  "Sort the remaining records (ORDER BY)",
  "Show only the chosen fields (SELECT)"
], done: "FROM, WHERE, ORDER BY, SELECT." });

Lib.calc($("#c1"), { qs: [
  { q: "SELECT COUNT(*) FROM Products WHERE Price > 5; What is the output?", a: 5, sol: "Backpack, Calculator, Headphones, Lunchbox and USB Drive: 5." },
  { q: "SELECT SUM(Stock) FROM Products WHERE Category = 'Stationery'; What is the output?", a: 400, sol: "200 + 80 + 120 = 400." },
  { q: "SELECT Name FROM Products WHERE Stock < 20; How many records are output?", a: 2, sol: "Backpack (15) and USB Drive (0)." },
  { q: "SELECT Name FROM Products ORDER BY Stock DESC; Which name is output first?", t: ["PENCIL"], ph: "product name", sol: "Pencil has the largest stock, 200." },
  { q: "SELECT Name FROM Products WHERE Category = 'Bags' OR Price < 1; How many records are output?", a: 3, sol: "Backpack and Lunchbox (Bags) and Pencil (price 0.50)." },
  { q: "SELECT Name FROM Products WHERE Category = 'Electronics' AND Stock > 30; How many records are output?", a: 1, sol: "Only Calculator (stock 40)." },
  { q: "SELECT SUM(Price) FROM Products WHERE Category = 'Bags'; What is the output?", a: 32.79, sol: "24.99 + 7.80 = 32.79." },
  { q: "SELECT Name FROM Products ORDER BY Price ASC; Which name is output first?", t: ["PENCIL"], ph: "product name", sol: "Pencil has the lowest price, 0.50." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "Which keyword chooses the fields to display?", opts: ["SELECT", "FROM", "WHERE", "ORDER BY"], a: 0, why: "SELECT lists the fields." },
  { q: "Which keyword sorts the output?", opts: ["ORDER BY", "WHERE", "FROM", "COUNT"], a: 0, why: "ORDER BY, with ASC or DESC." },
  { q: "What does DESC mean?", opts: ["Largest (or Z to A) first", "Smallest first", "Delete", "Describe"], a: 0, why: "Descending order." },
  { q: "Which operator means \"not equal to\"?", opts: ["<>", "=", ">=", "!"], a: 0, why: "<> is not equal to." },
  { q: "How should text be written in a condition?", opts: ["In quotes: 'Bags'", "Without quotes", "In brackets", "In capitals only"], a: 0, why: "Text values are quoted." },
  { q: "What does COUNT(*) return?", opts: ["The number of matching records", "The total of a field", "The largest value", "The field names"], a: 0, why: "A count of records." },
  { q: "What does SUM(Price) return?", opts: ["The total of the Price values", "The number of records", "The average", "The first price"], a: 0, why: "SUM adds numeric values." },
  { q: "Which is the correct clause order?", opts: ["SELECT, FROM, WHERE, ORDER BY", "FROM, SELECT, ORDER BY, WHERE", "WHERE, FROM, SELECT", "ORDER BY, SELECT, FROM"], a: 0, why: "SELECT, FROM, WHERE, ORDER BY." }
] });

Lib.cards($("#fc1"), { cards: [
  ["SQL", "Structured query language, used to query a database."],
  ["Query", "A request for data from a database."],
  ["SELECT", "Chooses which fields to display."],
  ["FROM", "Names the table to use."],
  ["WHERE", "Chooses which records to include, using a condition."],
  ["ORDER BY", "Sorts the results."],
  ["ASC", "Ascending order: smallest or A to Z first."],
  ["DESC", "Descending order: largest or Z to A first."],
  ["AND", "Both conditions must be true."],
  ["OR", "At least one condition must be true."],
  ["COUNT", "Counts the number of matching records."],
  ["SUM", "Adds up the values of a numeric field in the matching records."]
] });
