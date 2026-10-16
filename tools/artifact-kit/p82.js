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
const FPS = ["DECLARE Marks : ARRAY[1:5] OF INTEGER", "FOR Index ← 1 TO 5", "    INPUT Marks[Index]", "NEXT Index", "FOR Index ← 1 TO 5", "    OUTPUT Marks[Index]", "NEXT Index"];
const FPY = ["marks = [0] * 5", "for index in range(5):", "    marks[index] = int(input())", "for index in range(5):", "    print(marks[index])"];
const TPS = ["FOR Row ← 1 TO 3", "    RowTotal ← 0", "    FOR Column ← 1 TO 4", "        RowTotal ← RowTotal + Amount[Row, Column]", "    NEXT Column", "    OUTPUT \"Row \", Row, \" total \", RowTotal", "NEXT Row"];
const TPY = ["for row in range(3):", "    row_total = 0", "    for column in range(4):", "        row_total = row_total + amount[row][column]", "    print(\"Row\", row + 1, \"total\", row_total)"];

/* ---------- 1. array view ---------- */
function av(arrv, o) {
  const n = arrv.length, W = 640, gap = 6, w = Math.min(64, Math.floor((W - 40 - (n - 1) * gap) / n)), x0 = (W - (n * w + (n - 1) * gap)) / 2;
  let s = SV.text(14, 26, o.title || "", "lbl bd", { "text-anchor": "start" });
  s += Lib.cells(arrv.map((v) => (v === null ? "" : v)), { x0, y: 70, w, h: 46, gap, cls: o.cls, ptr: o.ptr, idx: false });
  arrv.forEach((_, i) => (s += SV.text(x0 + i * (w + gap) + w / 2, 70 + 46 + 17, i + 1, "sm", { "text-anchor": "middle" })));
  if (o.vars) s += SV.text(W / 2, 214, o.vars, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" });
  if (o.note) s += SV.text(W / 2, 242, o.note, "lbl bd " + (o.nc || ""), { "text-anchor": "middle" });
  return s;
}
const INV = [62, 45, 78, 50, 91];
function fillFrames() {
  const F = [], D = [null, null, null, null, null], f = (cap, ps, py, o) => F.push({ cap, ps, py, svg: av([...D], { title: "Marks[1:5]", ...o }) });
  f("The array <b>Marks</b> is declared with 5 elements, indexed 1 to 5. They are empty.", [0], [0], {});
  for (let i = 0; i < 5; i++) { f(`<b>Index = ${i + 1}</b>. INPUT Marks[${i + 1}]: the user types <b>${INV[i]}</b>.`, [1, 2], [1, 2], { cls: { [i]: "cur" }, ptr: { [i]: "Index" }, vars: "Index = " + (i + 1) }); D[i] = INV[i]; f(`Marks[${i + 1}] now holds <b>${INV[i]}</b>.`, [2], [2], { cls: { [i]: "ok" }, ptr: { [i]: "Index" }, vars: "Index = " + (i + 1) }); }
  for (let i = 0; i < 5; i++) f(`Second loop, <b>Index = ${i + 1}</b>. OUTPUT Marks[${i + 1}] shows <b>${INV[i]}</b>.`, [4, 5], [3, 4], { cls: { [i]: "cur" }, ptr: { [i]: "Index" }, vars: "Index = " + (i + 1), note: "Output: " + INV.slice(0, i + 1).join("  "), nc: "t3" });
  return F;
}
Lib.algo($("#aF"), { w: 640, h: 260, label: "Filling and reading a 1D array", pseudo: FPS, py: FPY, dwell: 1500, frames: fillFrames() });

/* ---------- 2. 2D traversal ---------- */
const AM = [[4, 7, 2, 9], [5, 1, 8, 3], [6, 2, 4, 7]];
function gv2(o) {
  const cw = 64, ch = 44, x0 = 90, y0 = 50; let s = SV.text(14, 26, "Amount[1:3, 1:4]", "lbl bd", { "text-anchor": "start" });
  for (let c = 0; c < 4; c++) s += SV.text(x0 + c * cw + cw / 2, y0 - 8, "Col " + (c + 1), "sm", { "text-anchor": "middle" });
  for (let r = 0; r < 3; r++) { s += SV.text(x0 - 10, y0 + r * ch + ch / 2 + 5, "Row " + (r + 1), "sm", { "text-anchor": "end" });
    for (let c = 0; c < 4; c++) { const cl = o.cls[r + "," + c] || ""; s += SV.rect(x0 + c * cw, y0 + r * ch, cw - 4, ch - 4, "cell" + (cl ? " cell-" + cl : ""), { rx: 6 }) + SV.text(x0 + c * cw + cw / 2 - 2, y0 + r * ch + ch / 2 + 6, AM[r][c], "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px" }); }
    s += SV.text(x0 + 4 * cw + 30, y0 + r * ch + ch / 2 + 6, o.rt[r] === undefined ? "" : o.rt[r], "lbl bd t3", { "text-anchor": "middle", style: "font-family:var(--mono)" }); }
  s += SV.text(x0 + 4 * cw + 30, y0 - 8, "RowTotal", "sm", { "text-anchor": "middle" });
  if (o.vars) s += SV.text(320, 215, o.vars, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" }); if (o.note) s += SV.text(320, 243, o.note, "lbl bd t3", { "text-anchor": "middle" });
  return s;
}
function t2Frames() {
  const F = [], rt = [], done = {}, f = (cap, ps, py, o) => F.push({ cap, ps, py, svg: gv2({ cls: { ...done }, rt: [...rt], ...o }) });
  f("A 2D array of amounts: <b>3 rows</b>, <b>4 columns</b>. The outer loop goes through the rows; the inner loop through the columns.", [0], [0], {});
  for (let r = 0; r < 3; r++) { let tot = 0; f(`<b>Row ← ${r + 1}</b>. <b>RowTotal ← 0</b>.`, [0, 1], [0, 1], { vars: `Row = ${r + 1}   RowTotal = 0` });
    for (let c = 0; c < 4; c++) { const o = tot; tot += AM[r][c]; done[r + "," + c] = "cur"; f(`<b>Column ← ${c + 1}</b>. RowTotal ← ${o} + Amount[${r + 1},${c + 1}] = ${o} + ${AM[r][c]} = <b>${tot}</b>.`, [2, 3], [2, 3], { vars: `Row = ${r + 1}  Column = ${c + 1}  RowTotal = ${tot}` }); done[r + "," + c] = "ok"; }
    rt[r] = tot; f(`The inner loop ends. <b>OUTPUT</b> "Row ${r + 1} total ${tot}".`, [4, 5], [4], { vars: `Row = ${r + 1}   RowTotal = ${tot}` }); }
  f("The outer loop ends. Every cell has been visited once: 3 × 4 = <b>12</b> times through the inner body.", [6], [], { note: "12 cells visited" });
  return F;
}
Lib.algo($("#aT"), { w: 640, h: 260, label: "Nested loops on a 2D array", pseudo: TPS, py: TPY, dwell: 1300, frames: t2Frames() });

/* ---------- Learn code ---------- */
Lib.codePanel($("#cdDecl"), { pseudo: ["DECLARE Marks : ARRAY[1:5] OF INTEGER", "Marks[3] ← 78", "OUTPUT Marks[3]", "Index ← 2", "OUTPUT Marks[Index]"], py: ["marks = [0] * 5", "marks[2] = 78        # the 3rd element", "print(marks[2])", "index = 1", "print(marks[index])"] });
Lib.codePanel($("#cdFill"), { pseudo: FPS, py: FPY });
Lib.codePanel($("#cdTot"), { pseudo: ["Total ← 0", "FOR Index ← 1 TO 5", "    Total ← Total + Marks[Index]", "NEXT Index", "OUTPUT Total"], py: ["total = 0", "for index in range(5):", "    total = total + marks[index]", "print(total)"] });
Lib.codePanel($("#cdD2"), { pseudo: ["DECLARE Amount : ARRAY[1:3, 1:4] OF INTEGER", "Amount[2,3] ← 8", "OUTPUT Amount[2,3]"], py: ["amount = [[0] * 4 for _ in range(3)]", "amount[1][2] = 8      # row 2, column 3", "print(amount[1][2])"] });
Lib.codePanel($("#cdNest"), { pseudo: TPS, py: TPY });

/* ---------- Lab 1 ---------- */
(() => {
  let sl; const inp = $("#ae");
  function upd() {
    if (!sl) return; const A = inp.value.trim().split(/[\s,]+/).filter(Boolean).slice(0, 10), base = +$("[name=ab]:checked").value, n = A.length, i = sl.get(), a = i - base, ok = a >= 0 && a < n;
    let s = ""; const w = Math.min(56, 600 / Math.max(n, 1)), x0 = (640 - (n * (w + 6) - 6)) / 2;
    A.forEach((v, k) => { const on = k === a; s += SV.rect(x0 + k * (w + 6), 24, w, 46, "", { rx: 8, style: `fill:${on ? "var(--accent-soft)" : "var(--soft)"};stroke:${on ? "var(--accent)" : "var(--line)"};stroke-width:${on ? 4 : 2}` }) + SV.text(x0 + k * (w + 6) + w / 2, 54, esc(v), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:16px" }) + SV.text(x0 + k * (w + 6) + w / 2, 90, k + base, "sm", { "text-anchor": "middle" }); });
    $("#as").innerHTML = s;
    $("#av").innerHTML = ok ? `<span class="okf">Valid</span> <b>Marks[${i}]</b> = <b>${esc(A[a])}</b>. The array has ${n} elements, indexed ${base} to ${n - 1 + base}.` : `<span class="flag">Index out of range</span> Marks[${i}] does not exist: the valid indexes are ${base} to ${n - 1 + base}.`;
  }
  sl = Lib.slider($("#a1"), { id: "ai", label: "Index", min: 0, max: 11, value: 3, onInput: upd }); inp.addEventListener("input", upd); $$("[name=ab]").forEach((r) => r.addEventListener("change", upd)); upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  const G = [[4, 7, 2, 9], [5, 1, 8, 3], [6, 2, 4, 7]]; let sr, sc; const t = $("#gt");
  function draw() {
    const rt = G.map((r) => r.reduce((a, b) => a + b, 0)), ct = [0, 1, 2, 3].map((c) => G.reduce((a, r) => a + r[c], 0)), gt = rt.reduce((a, b) => a + b, 0);
    t.innerHTML = `<tr><th></th>${[1, 2, 3, 4].map((c) => `<th>Col ${c}</th>`).join("")}<th>Row total</th></tr>` + G.map((r, i) => `<tr><th>Row ${i + 1}</th>${r.map((v, j) => `<td><input class="ipin" style="width:60px;padding:4px 6px" type="text" inputmode="numeric" data-r="${i}" data-c="${j}" value="${v}" aria-label="Row ${i + 1} column ${j + 1}"></td>`).join("")}<td><b>${rt[i]}</b></td></tr>`).join("") + `<tr><th>Col total</th>${ct.map((v) => `<td><b>${v}</b></td>`).join("")}<td><b>${gt}</b></td></tr>`;
    $$("input", t).forEach((i) => i.addEventListener("change", () => { G[+i.dataset.r][+i.dataset.c] = parseFloat(i.value) || 0; draw(); upd(); }));
  }
  function upd() { if (!sr || !sc) return; const r = sr.get(), c = sc.get(); $("#gv").innerHTML = `<b>Amount[${r},${c}]</b> = <b>${G[r - 1][c - 1]}</b> (row ${r}, column ${c}). Row totals use an inner loop over the columns; column totals swap the loops.`; }
  sr = Lib.slider($("#g1"), { id: "gr", label: "Row", min: 1, max: 3, value: 2, onInput: upd }); sc = Lib.slider($("#g2"), { id: "gc", label: "Column", min: 1, max: 4, value: 3, onInput: upd }); draw(); upd();
})();

/* ---------- Lab 3 ---------- */
chooser($("#sn"), $("#sv"), ["Total of all elements", "Largest element", "Count of marks of 50 or more", "Output in reverse order", "Set every element to zero"], [
  ['<span class="ln2">Total ← 0<br>FOR Index ← 1 TO 5<br>&nbsp;&nbsp;&nbsp;Total ← Total + Marks[Index]<br>NEXT Index</span>', "Total of all elements"],
  ['<span class="ln2">Max ← Marks[1]<br>FOR Index ← 2 TO 5<br>&nbsp;&nbsp;&nbsp;IF Marks[Index] &gt; Max THEN Max ← Marks[Index]<br>NEXT Index</span>', "Largest element"],
  ['<span class="ln2">Count ← 0<br>FOR Index ← 1 TO 5<br>&nbsp;&nbsp;&nbsp;IF Marks[Index] &gt;= 50 THEN Count ← Count + 1<br>NEXT Index</span>', "Count of marks of 50 or more"],
  ['<span class="ln2">FOR Index ← 5 TO 1 STEP -1<br>&nbsp;&nbsp;&nbsp;OUTPUT Marks[Index]<br>NEXT Index</span>', "Output in reverse order"],
  ['<span class="ln2">FOR Index ← 1 TO 5<br>&nbsp;&nbsp;&nbsp;Marks[Index] ← 0<br>NEXT Index</span>', "Set every element to zero"],
]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Does each need a 1D array or a 2D array?", buckets: [{ label: "1D array" }, { label: "2D array" }], items: [
  { text: "A list of 30 student names", b: 0 },
  { text: "The marks of one class in a test", b: 0 },
  { text: "Prices of 10 products", b: 0 },
  { text: "Marks[Index]", b: 0 },
  { text: "A noughts and crosses board", b: 1 },
  { text: "Seats in a cinema in rows and columns", b: 1 },
  { text: "Sales per product for each month", b: 1 },
  { text: "Amount[Row, Column]", b: 1 },
], done: "One index or two." });

Lib.order($("#o1"), { prompt: "Put the lines in order to input 10 numbers into an array and output the largest.", items: [
  "DECLARE Numbers : ARRAY[1:10] OF INTEGER",
  "FOR Index ← 1 TO 10",
  "    INPUT Numbers[Index]",
  "NEXT Index",
  "Max ← Numbers[1]",
  "FOR Index ← 2 TO 10",
  "    IF Numbers[Index] > Max THEN Max ← Numbers[Index]",
  "NEXT Index",
  "OUTPUT Max"
], done: "Declare, fill, start Max, search, output." });

Lib.order($("#o2"), { prompt: "Put these lines in order to total every cell of the 2D array Amount[1:3, 1:4].", items: [
  "Total ← 0",
  "FOR Row ← 1 TO 3",
  "    FOR Column ← 1 TO 4",
  "        Total ← Total + Amount[Row, Column]",
  "    NEXT Column",
  "NEXT Row",
  "OUTPUT Total"
], done: "Zero the total, outer loop, inner loop, add, close both loops, output." });

Lib.match($("#m1"), { prompt: "Names[1:4] holds \"Ali\", \"Bea\", \"Cy\", \"Dee\" (first index 1). Match each expression to its value.", pairs: [
  ["Names[1]", "\"Ali\""],
  ["Names[3]", "\"Cy\""],
  ["Names[4]", "\"Dee\""],
  ["Names[Index] when Index = 2", "\"Bea\""],
  ["Names[Index + 1] when Index = 2", "\"Cy\""],
  ["LENGTH(Names[3])", "2"]
] });

Lib.calc($("#c1"), { qs: [
  { q: "What is Marks[3]?", a: 78, sol: "The third element is 78." },
  { q: "What is Marks[1] + Marks[5]?", a: 153, sol: "62 + 91 = 153." },
  { q: "What is the total of all five marks?", a: 326, sol: "62 + 45 + 78 + 50 + 91 = 326." },
  { q: "How many marks are 50 or more?", a: 4, sol: "62, 78, 50 and 91." },
  { q: "What is the first loop index if the array is indexed from 0?", a: 0, sol: "0." },
  { q: "What is Amount[2,3]?", a: 8, sol: "Row 2, column 3 is 8." },
  { q: "How many elements are in a 2D array with 3 rows and 4 columns?", a: 12, sol: "3 × 4 = 12." },
  { q: "What is the total of row 3 of Amount (6, 2, 4, 7)?", a: 19, sol: "6 + 2 + 4 + 7 = 19." },
  { q: "How many times does the inner loop body run for FOR Row ← 1 TO 3 containing FOR Column ← 1 TO 4?", a: 12, sol: "3 × 4 = 12." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "What does an array store?", opts: ["Many values of the same data type", "Only one value", "Values of different types", "Only text"], a: 0, why: "Elements of the same data type, under one name." },
  { q: "What is an index?", opts: ["The position of an element", "The array's data type", "A loop", "The array's name"], a: 0, why: "It identifies the element's position." },
  { q: "Which declares an array of 30 strings?", opts: ["DECLARE Names : ARRAY[1:30] OF STRING", "DECLARE Names : STRING", "Names ← 30", "ARRAY Names"], a: 0, why: "The range and data type are stated." },
  { q: "How many indexes does a 2D array element need?", opts: ["Two", "One", "Three", "None"], a: 0, why: "A row and a column." },
  { q: "Which loops read every cell of a 2D array?", opts: ["Nested loops", "Only one FOR loop", "A CASE statement", "A procedure"], a: 0, why: "Rows in the outer loop, columns in the inner." },
  { q: "What error occurs if you use Marks[6] in an array indexed 1 to 5?", opts: ["Index out of range", "Syntax error", "None", "Overflow"], a: 0, why: "The element does not exist." },
  { q: "What is Marks[Index]?", opts: ["The element at the position stored in Index", "The number Index", "The array size", "A constant"], a: 0, why: "A variable can be used as the index." },
  { q: "In Python, the first element of a list has index…", opts: ["0", "1", "−1", "10"], a: 0, why: "Python indexes start at 0." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Array", "A fixed-length structure that holds several values of the same data type under one name."],
  ["Element", "A single value in an array."],
  ["Index", "The position number used to access an element."],
  ["1D array", "An array with one index: a list."],
  ["2D array", "An array with two indexes: a table of rows and columns."],
  ["Lower bound", "The first index of an array (often 0 or 1)."],
  ["Upper bound", "The last index of an array."],
  ["Nested iteration", "A loop inside a loop, used to visit every cell of a 2D array."],
  ["DECLARE", "Pseudocode keyword used to declare a variable or array and its data type."],
  ["Index out of range", "An error caused by using an index outside the bounds of the array."]
] });
