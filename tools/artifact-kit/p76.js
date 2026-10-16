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
const ERR = ["Wrong loop limit", "Wrong starting value", "Wrong operator", "Loop never ends", "Output in the wrong place", "Wrong variable"];
/* ---------- algorithms with a trace log ---------- */
const ALG = {
  total: { name: "Total of 4 numbers", help: "Four numbers, for example 3 8 2 5", def: "3 8 2 5", cols: ["Total", "Count", "Number", "OUTPUT"],
    ps: ["Total ← 0", "FOR Count ← 1 TO 4", "    INPUT Number", "    Total ← Total + Number", "NEXT Count", "OUTPUT Total"], py: ["total = 0", "for count in range(1, 5):", "    number = int(input())", "    total = total + number", "print(total)"],
    run(inp) { const L = []; let T = 0; L.push({ ps: [0], py: [0], set: { Total: 0 }, cap: "<b>Total ← 0</b>" });
      for (let c = 1; c <= 4; c++) { const n = inp[c - 1] ?? 0; L.push({ ps: [1], py: [1], set: { Count: c }, cap: `<b>Count ← ${c}</b> (the FOR loop)` }); L.push({ ps: [2], py: [2], set: { Number: n }, cap: `INPUT Number: the user types <b>${n}</b>` }); const o = T; T += n; L.push({ ps: [3], py: [3], set: { Total: T }, cap: `<b>Total ← ${o} + ${n} = ${T}</b>` }); }
      L.push({ ps: [5], py: [4], out: T, cap: `<b>OUTPUT Total</b>: ${T}` }); return L; } },
  digit: { name: "Digit sum (WHILE, MOD, DIV)", help: "One whole number, for example 345", def: "345", cols: ["Number", "Sum", "Digit", "OUTPUT"],
    ps: ["INPUT Number", "Sum ← 0", "WHILE Number > 0 DO", "    Digit ← MOD(Number, 10)", "    Sum ← Sum + Digit", "    Number ← DIV(Number, 10)", "ENDWHILE", "OUTPUT Sum"], py: ["number = int(input())", "sum_digits = 0", "while number > 0:", "    digit = number % 10", "    sum_digits = sum_digits + digit", "    number = number // 10", "print(sum_digits)"],
    run(inp) { const L = []; let n = Math.max(0, Math.floor(inp[0] || 0)), S = 0; L.push({ ps: [0], py: [0], set: { Number: n }, cap: `INPUT Number: <b>${n}</b>` }); L.push({ ps: [1], py: [1], set: { Sum: 0 }, cap: "<b>Sum ← 0</b>" });
      let guard = 0; while (n > 0 && guard++ < 12) { L.push({ ps: [2], py: [2], set: {}, skip: true, cap: `Is Number > 0? ${n} &gt; 0 is true, so enter the loop` }); const d = n % 10; L.push({ ps: [3], py: [3], set: { Digit: d }, cap: `<b>Digit ← MOD(${n}, 10) = ${d}</b>` }); const o = S; S += d; L.push({ ps: [4], py: [4], set: { Sum: S }, cap: `<b>Sum ← ${o} + ${d} = ${S}</b>` }); const m = Math.floor(n / 10); L.push({ ps: [5], py: [5], set: { Number: m }, cap: `<b>Number ← DIV(${n}, 10) = ${m}</b>` }); n = m; }
      L.push({ ps: [2, 6], py: [2], set: {}, skip: true, cap: "Is Number > 0? <b>0 &gt; 0 is false</b>, so the loop ends" }); L.push({ ps: [7], py: [6], out: S, cap: `<b>OUTPUT Sum</b>: ${S}` }); return L; } },
  max3: { name: "Largest of three numbers", help: "Three numbers, for example 7 12 9", def: "7 12 9", cols: ["A", "B", "C", "Max", "OUTPUT"],
    ps: ["INPUT A", "INPUT B", "INPUT C", "Max ← A", "IF B > Max", "  THEN", "    Max ← B", "ENDIF", "IF C > Max", "  THEN", "    Max ← C", "ENDIF", "OUTPUT Max"], py: ["a = int(input())", "b = int(input())", "c = int(input())", "maximum = a", "if b > maximum:", "    maximum = b", "if c > maximum:", "    maximum = c", "print(maximum)"],
    run(inp) { const [a, b, c] = [inp[0] ?? 0, inp[1] ?? 0, inp[2] ?? 0], L = []; let M = a;
      L.push({ ps: [0], py: [0], set: { A: a }, cap: `INPUT A: <b>${a}</b>` }); L.push({ ps: [1], py: [1], set: { B: b }, cap: `INPUT B: <b>${b}</b>` }); L.push({ ps: [2], py: [2], set: { C: c }, cap: `INPUT C: <b>${c}</b>` }); L.push({ ps: [3], py: [3], set: { Max: M }, cap: `<b>Max ← A = ${M}</b>` });
      L.push({ ps: [4], py: [4], set: {}, skip: true, cap: `Is B > Max? ${b} &gt; ${M} is ${b > M}` }); if (b > M) { M = b; L.push({ ps: [6], py: [5], set: { Max: M }, cap: `<b>Max ← B = ${M}</b>` }); }
      L.push({ ps: [8], py: [6], set: {}, skip: true, cap: `Is C > Max? ${c} &gt; ${M} is ${c > M}` }); if (c > M) { M = c; L.push({ ps: [10], py: [7], set: { Max: M }, cap: `<b>Max ← C = ${M}</b>` }); }
      L.push({ ps: [12], py: [8], out: M, cap: `<b>OUTPUT Max</b>: ${M}` }); return L; } },
  sent: { name: "Total until 0 is entered", help: "Numbers ending with 0, for example 5 12 3 0", def: "5 12 3 0", cols: ["Total", "Number", "OUTPUT"],
    ps: ["Total ← 0", "INPUT Number", "WHILE Number <> 0 DO", "    Total ← Total + Number", "    INPUT Number", "ENDWHILE", "OUTPUT Total"], py: ["total = 0", "number = int(input())", "while number != 0:", "    total = total + number", "    number = int(input())", "print(total)"],
    run(inp) { const L = []; let i = 0, T = 0; const nx = () => (i < inp.length ? inp[i++] : 0); L.push({ ps: [0], py: [0], set: { Total: 0 }, cap: "<b>Total ← 0</b>" }); let n = nx(); L.push({ ps: [1], py: [1], set: { Number: n }, cap: `INPUT Number: <b>${n}</b>` }); let g = 0;
      while (n !== 0 && g++ < 10) { L.push({ ps: [2], py: [2], set: {}, skip: true, cap: `Is Number &lt;&gt; 0? ${n} is not 0, so enter the loop` }); const o = T; T += n; L.push({ ps: [3], py: [3], set: { Total: T }, cap: `<b>Total ← ${o} + ${n} = ${T}</b>` }); n = nx(); L.push({ ps: [4], py: [4], set: { Number: n }, cap: `INPUT Number: <b>${n}</b>` }); }
      L.push({ ps: [2, 5], py: [2], set: {}, skip: true, cap: "Is Number &lt;&gt; 0? <b>It is 0</b>, so the loop ends" }); L.push({ ps: [6], py: [5], out: T, cap: `<b>OUTPUT Total</b>: ${T}` }); return L; } },
  bug: { name: "Buggy: add 1 to 5 (expects 15)", help: "No input needed", def: "", cols: ["Total", "Count", "OUTPUT"],
    ps: ["Total ← 0", "FOR Count ← 1 TO 4", "    Total ← Total + Count", "NEXT Count", "OUTPUT Total"], py: ["total = 0", "for count in range(1, 5):", "    total = total + count", "print(total)"],
    run() { const L = []; let T = 0; L.push({ ps: [0], py: [0], set: { Total: 0 }, cap: "<b>Total ← 0</b>" }); for (let c = 1; c <= 4; c++) { L.push({ ps: [1], py: [1], set: { Count: c }, cap: `<b>Count ← ${c}</b>` }); const o = T; T += c; L.push({ ps: [2], py: [2], set: { Total: T }, cap: `<b>Total ← ${o} + ${c} = ${T}</b>` }); } L.push({ ps: [4], py: [3], out: T, cap: `<b>OUTPUT Total</b>: ${T}. But the answer should be 15!` }); return L; } },
};
function rowsOf(log, cols) { return log.filter((l) => !l.skip).map((l) => { const r = {}; Object.entries(l.set || {}).forEach(([k, v]) => (r[k] = v)); if (l.out !== undefined) r.OUTPUT = l.out; return r; }); }
function trSvg(cols, rows, W, H, hiLast) {
  const cw = (W - 70) / cols.length; let s = SV.rect(10, 8, W - 20, 30, "", { rx: 6, style: "fill:var(--soft)" });
  cols.forEach((c, i) => (s += SV.text(60 + cw * i + cw / 2, 29, c, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" })));
  rows.forEach((r, i) => { const y = 44 + i * 24; if (hiLast && i === rows.length - 1) s += SV.rect(10, y, W - 20, 24, "", { rx: 4, style: "fill:var(--warn-soft)" });
    s += SV.text(30, y + 17, i + 1, "sm", { "text-anchor": "middle" }); cols.forEach((c, j) => { if (r[c] !== undefined) s += SV.text(60 + cw * j + cw / 2, y + 17, r[c], "lbl bd", { "text-anchor": "middle", style: `font-family:var(--mono);${c === "OUTPUT" ? "fill:var(--good)" : ""}` }); }); });
  return s;
}
function trFrames(a, inp, extraLast) {
  const log = a.run(inp), F = [], H = 60 + 15 * 24;
  log.forEach((l, i) => { const upto = log.slice(0, i + 1), rows = rowsOf(upto, a.cols); F.push({ cap: l.cap + (i === log.length - 1 && extraLast ? " " + extraLast : ""), ps: l.ps, py: l.py, svg: trSvg(a.cols, rows, 640, H, !l.skip) + (l.skip ? SV.text(320, H - 8, "(a condition is checked, no variable changes)", "sm", { "text-anchor": "middle" }) : "") }); });
  return F;
}
Lib.algo($("#aT"), { w: 640, h: 420, label: "Building a trace table for a total", pseudo: ALG.total.ps, py: ALG.total.py, dwell: 1700, frames: trFrames(ALG.total, [3, 8, 2, 5]) });
Lib.algo($("#aD"), { w: 640, h: 420, label: "Trace table for a digit sum", pseudo: ALG.digit.ps, py: ALG.digit.py, dwell: 1700, frames: trFrames(ALG.digit, [345]) });
Lib.algo($("#aE"), { w: 640, h: 420, label: "Finding an error with a trace table", pseudo: ALG.bug.ps, py: ALG.bug.py, dwell: 1800, frames: trFrames(ALG.bug, [], "The loop stops at Count = 4, so 5 is never added. Fix: FOR Count ← 1 TO 5.") });

/* ---------- Learn code ---------- */
Lib.codePanel($("#cdTr1"), { pseudo: ALG.total.ps, py: ALG.total.py });
Lib.codePanel($("#cdWr"), { pseudo: ["Count ← 0", "Max ← 0", "FOR Index ← 1 TO 20", "    INPUT Mark", "    IF Mark >= 50", "      THEN", "        Count ← Count + 1", "    ENDIF", "    IF Mark > Max", "      THEN", "        Max ← Mark", "    ENDIF", "NEXT Index", "OUTPUT Count", "OUTPUT Max"], py: ["count = 0", "maximum = 0", "for index in range(20):", "    mark = int(input())", "    if mark >= 50:", "        count = count + 1", "    if mark > maximum:", "        maximum = mark", "print(count)", "print(maximum)"] });

/* ---------- Lab 1 ---------- */
(() => {
  const sel = $("#ta"), inp = $("#ti"), tt = $("#tt"), tv = $("#tv"); let log = [], n = 0;
  sel.innerHTML = Object.entries(ALG).map(([k, a]) => `<option value="${k}">${a.name}</option>`).join("");
  const cur = () => ALG[sel.value];
  function load() { const a = cur(); $("#th").textContent = a.help; inp.disabled = !a.def; log = a.run(inp.value.trim().split(/[\s,]+/).filter(Boolean).map(Number).filter((x) => !isNaN(x))); n = 0; draw(); }
  function draw() {
    const a = cur(), rows = rowsOf(log.slice(0, n), a.cols);
    tt.innerHTML = `<tr><th></th>${a.cols.map((c) => `<th>${c}</th>`).join("")}</tr>` + rows.map((r, i) => `<tr><td>${i + 1}</td>${a.cols.map((c) => `<td>${r[c] ?? ""}</td>`).join("")}</tr>`).join("");
    const l = log[n - 1]; Lib.codePanel($("#tc"), { pseudo: a.ps, py: a.py }).hl(l ? l.ps : [], l ? l.py : []);
    tv.innerHTML = n === 0 ? "Press Next row to start." : l.cap + (n === log.length ? "<br>The algorithm has finished." : "");
  }
  sel.onchange = () => { inp.value = cur().def; load(); };
  inp.addEventListener("input", load);
  $("#tn").onclick = () => { if (n < log.length) n++; while (n < log.length && log[n - 1].skip) n++; draw(); };
  $("#tall").onclick = () => { n = log.length; draw(); }; $("#tr").onclick = () => { n = 0; draw(); };
  inp.value = ALG.total.def; load();
})();

/* ---------- Lab 2 ---------- */
chooser($("#sn"), $("#sv"), ERR, [
  ['<span class="ln2">Total ← 1<br>FOR Count ← 1 TO 5<br>&nbsp;&nbsp;&nbsp;Total ← Total + Count<br>NEXT Count</span><br>Should total 1 to 5 (15), but outputs 16', "Wrong starting value"],
  ['<span class="ln2">Total ← 0<br>FOR Count ← 1 TO 10<br>&nbsp;&nbsp;&nbsp;Total ← Total + Count<br>NEXT Count</span><br>Should total the numbers 1 to 5', "Wrong loop limit"],
  ['<span class="ln2">IF Mark &gt; 50<br>&nbsp;&nbsp;&nbsp;THEN OUTPUT "Pass"</span><br>A mark of 50 should pass but does not', "Wrong operator"],
  ['<span class="ln2">Count ← 1<br>WHILE Count &lt;= 10 DO<br>&nbsp;&nbsp;&nbsp;OUTPUT Count<br>ENDWHILE</span><br>The program never stops', "Loop never ends"],
  ['<span class="ln2">FOR Index ← 1 TO 5<br>&nbsp;&nbsp;&nbsp;INPUT Mark<br>&nbsp;&nbsp;&nbsp;Total ← Total + Mark<br>&nbsp;&nbsp;&nbsp;OUTPUT Total<br>NEXT Index</span><br>Should output one total only', "Output in the wrong place"],
  ['<span class="ln2">FOR Index ← 1 TO 5<br>&nbsp;&nbsp;&nbsp;INPUT Mark<br>&nbsp;&nbsp;&nbsp;Total ← Total + Index<br>NEXT Index</span><br>Should total the marks input', "Wrong variable"],
]);

/* ---------- Practise ---------- */
Lib.order($("#o1"), { prompt: "Put the lines in order to input 5 numbers and output their average.", items: [
  "Total ← 0",
  "FOR Count ← 1 TO 5",
  "INPUT Number",
  "Total ← Total + Number",
  "NEXT Count",
  "Average ← Total / 5",
  "OUTPUT Average"
], done: "Initialise, loop, input, add, end loop, calculate, output." });

Lib.match($("#m1"), { prompt: "Match each error to its fix.", pairs: [
  ["Loop runs one time too few", "Change the upper limit of the loop"],
  ["Total starts at 1", "Set Total ← 0 before the loop"],
  ["Uses > when 50 should pass", "Change the operator to >="],
  ["WHILE loop never ends", "Add an update such as Index ← Index + 1 inside it"],
  ["OUTPUT inside the loop", "Move OUTPUT after the loop ends"],
  ["Max starts at 0", "Start Max as the first item"]
] });

Lib.order($("#o2"), { prompt: "Put the lines in order to input 20 marks and count those of 50 or more.", items: [
  "Count ← 0",
  "FOR Index ← 1 TO 20",
  "INPUT Mark",
  "IF Mark >= 50 THEN Count ← Count + 1",
  "NEXT Index",
  "OUTPUT Count"
], done: "Initialise, loop, input, test and count, end loop, output." });

Lib.calc($("#c1"), { qs: [
  { q: "Total ← 0. FOR Count ← 1 TO 4: Total ← Total + Count * 2. NEXT Count. What is Total at the end?", a: 20, sol: "2 + 4 + 6 + 8 = 20.", hint: "Trace each Count value." },
  { q: "Number ← 4567, Sum ← 0. WHILE Number > 0: Sum ← Sum + MOD(Number, 10), Number ← DIV(Number, 10). What is Sum?", a: 22, sol: "7 + 6 + 5 + 4 = 22." },
  { q: "Number ← 100. WHILE Number > 10: Number ← DIV(Number, 2). What is Number at the end?", a: 6, sol: "100 → 50 → 25 → 12 → 6. At 6 the condition 6 > 10 fails." },
  { q: "Count ← 1. WHILE Count < 10: Count ← Count + 3. How many times does the loop run?", a: 3, sol: "Count is 1, 4, 7 (the loop runs), then 10 (fails): 3 times." },
  { q: "What is MOD(23, 5)?", a: 3, sol: "23 = 4 × 5 + 3. The remainder is 3." },
  { q: "What is DIV(23, 5)?", a: 4, sol: "23 ÷ 5 = 4 remainder 3. DIV gives 4." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "What does a trace table record?", opts: ["The values of variables as the algorithm is dry-run", "The code size", "The speed of the program", "The names of programmers"], a: 0, why: "A trace table records variable values (and outputs) as you work through the algorithm." },
  { q: "A loop FOR Count ← 1 TO 5 runs how many times?", opts: ["4", "5", "6", "1"], a: 1, why: "Count takes the values 1, 2, 3, 4, 5." },
  { q: "Which is an error that makes a WHILE loop never end?", opts: ["Not updating the loop variable", "Using ←", "Using OUTPUT", "Using INPUT"], a: 0, why: "Without an update the condition never changes." },
  { q: "What should Total start at when adding numbers?", opts: ["0", "1", "The first item", "100"], a: 0, why: "A total starts at 0." },
  { q: "How do you find an error in an algorithm?", opts: ["Trace it with test data and compare with the expected output", "Guess", "Delete it", "Rewrite it in English"], a: 0, why: "A trace shows where the values go wrong." },
  { q: "Which is a precise pseudocode statement?", opts: ["Count ← Count + 1", "Add one to Count", "Count goes up", "Increase it"], a: 0, why: "Use ← and variables." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Trace table", "A table showing the value of each variable (and outputs) as an algorithm is dry-run."],
  ["Dry-run", "Working through an algorithm by hand to see what it does."],
  ["Off-by-one error", "A loop that runs one time too many or too few."],
  ["Starting value", "The initial value of a variable, such as Total ← 0."],
  ["Infinite loop", "A loop that never ends because its condition never becomes false."],
  ["INPUT", "Pseudocode keyword to read a value into a variable."],
  ["OUTPUT", "Pseudocode keyword to display a value."],
  ["←", "The assignment operator in pseudocode."],
  ["MOD", "Returns the remainder of an integer division."],
  ["DIV", "Returns the quotient of an integer division."]
] });
