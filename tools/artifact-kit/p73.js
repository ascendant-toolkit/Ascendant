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
const TOT_PS = ["Total ← 0", "Count ← 0", "Max ← Marks[1]", "FOR Index ← 1 TO 5", "    Total ← Total + Marks[Index]", "    IF Marks[Index] >= 50", "      THEN", "        Count ← Count + 1", "    ENDIF", "    IF Marks[Index] > Max", "      THEN", "        Max ← Marks[Index]", "    ENDIF", "NEXT Index", "Average ← Total / 5", "OUTPUT Total, Count, Max, Average"];
const TOT_PY = ["total = 0", "count = 0", "maximum = marks[0]", "for index in range(5):", "    total = total + marks[index]", "    if marks[index] >= 50:", "        count = count + 1", "    if marks[index] > maximum:", "        maximum = marks[index]", "average = total / 5", "print(total, count, maximum, average)"];
const LIN_PS = ["Found ← FALSE", "Index ← 1", "WHILE Index <= 8 AND Found = FALSE DO", "    IF Data[Index] = Target", "      THEN", "        Found ← TRUE", "      ELSE", "        Index ← Index + 1", "    ENDIF", "ENDWHILE", "IF Found = TRUE", "  THEN", "    OUTPUT \"Found at \", Index", "  ELSE", "    OUTPUT \"Not found\"", "ENDIF"];
const LIN_PY = ["found = False", "index = 0", "while index < 8 and not found:", "    if data[index] == target:", "        found = True", "    else:", "        index = index + 1", "if found:", "    print(\"Found at\", index + 1)", "else:", "    print(\"Not found\")"];
const BUB_PS = ["FOR Pass ← 1 TO N - 1", "    FOR Index ← 1 TO N - Pass", "        IF Data[Index] > Data[Index + 1]", "          THEN", "            Temp ← Data[Index]", "            Data[Index] ← Data[Index + 1]", "            Data[Index + 1] ← Temp", "        ENDIF", "    NEXT Index", "NEXT Pass"];
const BUB_PY = ["for pass_num in range(1, n):", "    for index in range(n - pass_num):", "        if data[index] > data[index + 1]:", "            temp = data[index]", "            data[index] = data[index + 1]", "            data[index + 1] = temp"];
/* ---------- shared view ---------- */
function vw(data, W, o) {
  const n = data.length, gap = 6, w = Math.min(56, Math.floor((W - 30 - (n - 1) * gap) / n)), tot = n * w + (n - 1) * gap, x0 = (W - tot) / 2, y = 70, h = 46;
  let s = SV.text(14, 26, o.title || "", "lbl bd", { "text-anchor": "start" });
  if (o.right) s += SV.text(W - 14, 26, o.right, "lbl bd t4", { "text-anchor": "end" });
  s += Lib.cells(data, { x0, y, w, h, gap, cls: o.cls, dim: o.dim, ptr: o.ptr, idx: false, lift: o.lift });
  data.forEach((_, i) => (s += SV.text(x0 + i * (w + gap) + w / 2, y + h + 17, i + 1, "sm", { "text-anchor": "middle" })));
  if (o.vars) s += SV.text(W / 2, 214, o.vars, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" });
  if (o.note) s += SV.text(W / 2, 244, o.note, "lbl bd " + (o.nc || ""), { "text-anchor": "middle" });
  return s;
}

/* ---------- 1. totalling, counting, max ---------- */
const MARKS = [62, 45, 78, 50, 91];
function totFrames() {
  const F = [], n = MARKS.length; let tot = 0, cnt = 0, mx = MARKS[0];
  const V = () => `Total = ${tot}   Count = ${cnt}   Max = ${mx}`;
  const f = (cap, ps, py, o) => F.push({ cap, ps, py, svg: vw(MARKS, 640, { title: "Marks", vars: V(), ...o }) });
  f("Set <b>Total</b> and <b>Count</b> to 0, and <b>Max</b> to the first mark (62), not 0.", [0, 1, 2], [0, 1, 2], { ptr: {} });
  const done = {};
  for (let i = 0; i < n; i++) {
    const m = MARKS[i];
    tot += m; done[i] = "cur";
    f(`Index = ${i + 1}. <b>Total</b> ← Total + ${m} = <b>${tot}</b>.`, [3, 4], [3, 4], { cls: { ...done }, ptr: { [i]: "Index" } });
    if (m >= 50) { cnt++; f(`${m} >= 50, so <b>Count</b> goes up by 1 to <b>${cnt}</b>.`, [5, 6, 7], [5, 6], { cls: { ...done }, ptr: { [i]: "Index" } }); }
    else f(`${m} is not >= 50, so Count stays at <b>${cnt}</b>.`, [5], [5], { cls: { ...done }, ptr: { [i]: "Index" } });
    if (m > mx) { mx = m; f(`${m} is bigger than the old Max, so <b>Max</b> ← ${m}.`, [9, 10, 11], [7, 8], { cls: { ...done }, ptr: { [i]: "Index" } }); }
    done[i] = "ok";
  }
  F.push({ cap: `The loop ends. <b>Average</b> ← ${tot} / 5 = <b>${tot / 5}</b>. Output: Total ${tot}, Count ${cnt}, Max ${mx}, Average ${tot / 5}.`, ps: [14, 15], py: [9, 10], svg: vw(MARKS, 640, { title: "Marks", vars: V(), cls: { 0: "ok", 1: "ok", 2: "ok", 3: "ok", 4: "ok" }, note: `Average = ${tot / 5}`, nc: "t3" }) });
  return F;
}
Lib.algo($("#aT"), { w: 640, h: 260, label: "Totalling, counting and maximum", pseudo: TOT_PS, py: TOT_PY, dwell: 2200, frames: totFrames() });

/* ---------- 2. linear search ---------- */
const LIST = [14, 7, 22, 9, 31, 18, 5, 26];
function linFrames(t) {
  const F = [], n = LIST.length; let c = 0; const seen = {};
  const f = (cap, ps, py, o) => F.push({ cap, ps, py, svg: vw(LIST, 640, { title: "Linear search for " + t, right: "Comparisons: " + c, ...o }) });
  f("Found ← FALSE, Index ← 1. Start at the <b>first</b> item.", [0, 1], [0, 1], { ptr: { 0: "Index" } });
  for (let i = 0; i < n; i++) {
    c++;
    f(`Is Data[${i + 1}] = ${t}? Data[${i + 1}] is <b>${LIST[i]}</b>.`, [2, 3], [2, 3], { cls: { ...seen, [i]: "cur" }, ptr: { [i]: "Index" } });
    if (LIST[i] === t) {
      f(`<b>${LIST[i]} = ${t}.</b> Found ← TRUE, so the loop stops.`, [5, 9], [4], { cls: { ...seen, [i]: "ok" }, ptr: { [i]: "Index" }, note: `Found after ${c} comparison${c > 1 ? "s" : ""}`, nc: "t3" });
      f(`Output: <b>Found at ${i + 1}</b>.`, [10, 11, 12], [7, 8], { cls: { ...seen, [i]: "ok" }, ptr: { [i]: "Index" }, note: `Found at ${i + 1}`, nc: "t3" });
      return F;
    }
    seen[i] = "no";
    if (i < n - 1) f("Not equal. <b>Index ← Index + 1</b>.", [6, 7], [5, 6], { cls: { ...seen }, ptr: { [i + 1]: "Index" } });
  }
  f("Index has passed the end of the list, so the loop ends. Found is still FALSE.", [2, 9], [2], { cls: { ...seen } });
  f(`Output <b>Not found</b>. All ${n} items were checked.`, [13, 14], [9, 10], { cls: { ...seen }, note: `Not found after ${c} comparisons`, nc: "t2" });
  return F;
}
Lib.algo($("#aL"), { w: 640, h: 260, label: "Linear search animation", pseudo: LIN_PS, py: LIN_PY, dwell: 1900, frames: linFrames(31) });

/* ---------- 3. bubble sort ---------- */
function bubFrames(src) {
  const D = [...src], n = D.length, F = []; let c = 0, sw = 0, fin = new Set();
  const f = (cap, ps, py, o) => F.push({ cap, ps, py, svg: vw(D, 640, { title: "Bubble sort", right: `Comparisons ${c} · Swaps ${sw}`, dim: [], ...o, cls: { ...Object.fromEntries([...fin].map((i) => [i, "sorted"])), ...(o.cls || {}) } }) });
  f("The list is unsorted. N = " + n + ". Pass 1 will compare neighbours from the left.", [0], [0], {});
  for (let p = 1; p <= n - 1; p++) {
    f(`<b>Pass ${p}.</b> Compare pairs from Data[1] up to Data[${n - p + 1}].`, [0, 1], [0, 1], {});
    for (let i = 0; i < n - p; i++) {
      c++;
      const bad = D[i] > D[i + 1];
      f(`Is Data[${i + 1}] > Data[${i + 2}]? ${D[i]} &gt; ${D[i + 1]} is <b>${bad ? "true" : "false"}</b>.`, [2], [2], { cls: { [i]: "cur", [i + 1]: "cur" } });
      if (bad) { [D[i], D[i + 1]] = [D[i + 1], D[i]]; sw++; f(`Swap them, using a temporary variable. Now ${D[i]} is before ${D[i + 1]}.`, [4, 5, 6], [3, 4, 5], { cls: { [i]: "warn", [i + 1]: "warn" } }); }
    }
    fin.add(n - p);
    f(`End of pass ${p}: <b>${D[n - p]}</b> is now in its final place at the end.`, [8, 9], [1], { cls: {} });
  }
  fin.add(0);
  f(`The list is sorted after ${n - 1} passes: <b>${D.join(", ")}</b>. ${c} comparisons, ${sw} swaps.`, [9], [0], { note: "Sorted", nc: "t3" });
  return F;
}
Lib.algo($("#aB"), { w: 640, h: 260, label: "Bubble sort animation", pseudo: BUB_PS, py: BUB_PY, dwell: 1500, frames: bubFrames([5, 3, 8, 1, 4]) });

/* ---------- Learn code ---------- */
Lib.codePanel($("#cdTot"), { pseudo: ["Total ← 0", "FOR Index ← 1 TO 5", "    Total ← Total + Marks[Index]", "NEXT Index", "OUTPUT Total"], py: ["total = 0", "for index in range(5):", "    total = total + marks[index]", "print(total)"] });
Lib.codePanel($("#cdCnt"), { pseudo: ["Count ← 0", "FOR Index ← 1 TO 5", "    IF Marks[Index] >= 50", "      THEN", "        Count ← Count + 1", "    ENDIF", "NEXT Index", "OUTPUT Count"], py: ["count = 0", "for index in range(5):", "    if marks[index] >= 50:", "        count = count + 1", "print(count)"] });
Lib.codePanel($("#cdMax"), { pseudo: ["Max ← Marks[1]", "Min ← Marks[1]", "FOR Index ← 2 TO 5", "    IF Marks[Index] > Max", "      THEN", "        Max ← Marks[Index]", "    ENDIF", "    IF Marks[Index] < Min", "      THEN", "        Min ← Marks[Index]", "    ENDIF", "NEXT Index", "Average ← Total / 5"], py: ["maximum = marks[0]", "minimum = marks[0]", "for index in range(1, 5):", "    if marks[index] > maximum:", "        maximum = marks[index]", "    if marks[index] < minimum:", "        minimum = marks[index]", "average = total / 5"] });
Lib.codePanel($("#cdLin"), { pseudo: LIN_PS, py: LIN_PY });
Lib.codePanel($("#cdBub"), { pseudo: BUB_PS, py: BUB_PY });

/* ---------- Lab 1 ---------- */
(() => {
  const sel = $("#tg"); sel.innerHTML = LIST.map((v) => `<option>${v}</option>`).join("") + "<option value='99'>99 (not in the list)</option>"; sel.value = "26";
  const go = () => Lib.algo($("#lA"), { w: 640, h: 260, label: "Linear search lab", pseudo: LIN_PS, py: LIN_PY, dwell: 1500, frames: linFrames(+sel.value) });
  sel.onchange = go; go();
})();

/* ---------- Lab 2 ---------- */
(() => {
  const inp = $("#bi");
  function upd() {
    const D = inp.value.trim().split(/[\s,]+/).filter(Boolean).map(Number).filter((x) => !isNaN(x)).slice(0, 8), n = D.length;
    if (n < 2) { $("#bt").innerHTML = ""; $("#bp").textContent = $("#bc").textContent = $("#bs").textContent = "–"; $("#bv").textContent = "Enter at least two numbers."; return; }
    let c = 0, sw = 0, rows = `<tr><th>Pass</th><th>List after the pass</th><th>Swaps</th></tr><tr><td>start</td><td>${D.join(" ")}</td><td></td></tr>`, fullPasses = 0, firstClean = 0;
    for (let p = 1; p <= n - 1; p++) { let s = 0; for (let i = 0; i < n - p; i++) { c++; if (D[i] > D[i + 1]) { [D[i], D[i + 1]] = [D[i + 1], D[i]]; s++; sw++; } } rows += `<tr><td>${p}</td><td>${D.join(" ")}</td><td>${s}</td></tr>`; if (!s && !firstClean) firstClean = p; fullPasses = p; }
    $("#bt").innerHTML = rows; $("#bp").textContent = fullPasses; $("#bc").textContent = c; $("#bs").textContent = sw;
    $("#bv").innerHTML = firstClean ? `Pass ${firstClean} made <b>no swaps</b>, so a bubble sort with a Swapped flag could have stopped there.` : `Every pass made at least one swap. The basic algorithm makes N − 1 = ${n - 1} passes for ${n} items.`;
  }
  inp.addEventListener("input", upd); upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  let sl; const inp = $("#si");
  function upd() {
    if (!sl) return;
    const D = inp.value.trim().split(/[\s,]+/).filter(Boolean).map(Number).filter((x) => !isNaN(x)).slice(0, 20), pm = sl.get();
    if (!D.length) { ["st", "sc", "sx", "sn", "sa"].forEach((i) => ($("#" + i).textContent = "–")); $("#sv").textContent = "Enter some marks."; return; }
    const t = D.reduce((a, b) => a + b, 0), c = D.filter((x) => x >= pm).length;
    $("#st").textContent = t; $("#sc").textContent = c; $("#sx").textContent = Math.max(...D); $("#sn").textContent = Math.min(...D); $("#sa").textContent = fmtN(t / D.length, 2);
    $("#sv").innerHTML = `${D.length} marks. <b>Total</b> ${t}, <b>Count</b> of marks ≥ ${pm}: ${c}, <b>Average</b> = ${t} / ${D.length} = ${fmtN(t / D.length, 2)}.`;
  }
  sl = Lib.slider($("#s1"), { id: "spm", label: "Pass mark", min: 0, max: 100, value: 50, onInput: upd });
  inp.addEventListener("input", upd); upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which standard method does each statement describe?", buckets: [{ label: "Totalling" }, { label: "Counting" }, { label: "Maximum / minimum" }, { label: "Linear search" }, { label: "Bubble sort" }], items: [
  { text: "Start at 0 and add each value to it", b: 0 },
  { text: "Total ← Total + Mark", b: 0 },
  { text: "Add 1 each time a condition is true", b: 1 },
  { text: "Count ← Count + 1", b: 1 },
  { text: "Start with the first item, replace it if a bigger one is found", b: 2 },
  { text: "IF Mark < Min THEN Min ← Mark", b: 2 },
  { text: "Check each item in order until the target is found", b: 3 },
  { text: "Worst case: every item is checked", b: 3 },
  { text: "Compare neighbours and swap if out of order", b: 4 },
  { text: "Needs a temporary variable for the swap", b: 4 },
], done: "Each has a start value and a repeated step." });

Lib.order($("#o1"), { prompt: "Put the steps of a linear search in order.", items: [
  "Set Found to FALSE and Index to 1",
  "Compare Data[Index] with the Target",
  "If they match, set Found to TRUE",
  "Otherwise add 1 to Index",
  "Repeat until Found is TRUE or the end of the list",
  "Output the position, or that it was not found"
], done: "Set up, compare, record, move on, repeat, output." });

Lib.order($("#o2"), { prompt: "Put the steps of one swap in a bubble sort in order.", items: [
  "Compare Data[Index] with Data[Index + 1]",
  "If the left one is bigger, store it in Temp",
  "Copy Data[Index + 1] into Data[Index]",
  "Copy Temp into Data[Index + 1]",
  "Move on to the next pair"
], done: "Compare, store, copy, copy back, next." });

Lib.calc($("#c1"), { qs: [
  { q: "The marks 62, 45, 78, 50 and 91 are totalled. What is the total?", a: 326, sol: "62 + 45 + 78 + 50 + 91 = 326." },
  { q: "How many of the marks 62, 45, 78, 50, 91 are 50 or more?", a: 4, sol: "62, 78, 50 and 91 are 50 or more: 4." },
  { q: "What is the average of 62, 45, 78, 50 and 91?", a: 65.2, sol: "326 ÷ 5 = 65.2.", hint: "Total divided by the number of items." },
  { q: "How many comparisons does one full pass of a bubble sort make on 6 items?", a: 5, sol: "N − 1 = 5 comparisons in the first pass." },
  { q: "What is the maximum number of passes a basic bubble sort makes on 6 items?", a: 5, sol: "N − 1 = 5 passes." },
  { q: "A linear search is made on a list of 8 items. What is the maximum number of comparisons?", a: 8, sol: "Worst case is every item: 8." },
  { q: "A bubble sort is used on 5 3 8 1 4. Write the list after the first pass.", t: ["35148"], ph: "5 numbers", sol: "5 and 3 swap: 3 5 8 1 4. 5 and 8 no swap. 8 and 1 swap: 3 5 1 8 4. 8 and 4 swap: 3 5 1 4 8.", hint: "Compare each neighbouring pair once, left to right." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "Which value should Total start at?", opts: ["0", "1", "The first item", "−1"], a: 0, why: "A running total starts at 0." },
  { q: "What should Max start as?", opts: ["0", "The first item in the list", "100", "The last item"], a: 1, why: "Max starts as the first item." },
  { q: "What is needed to swap two values?", opts: ["A temporary variable", "A second array", "A loop", "A constant"], a: 0, why: "Without Temp, one value is overwritten." },
  { q: "After the first pass of a bubble sort…", opts: ["The smallest item is first", "The largest item is at the end", "The list is sorted", "Nothing has moved"], a: 1, why: "The largest item bubbles to the end." },
  { q: "Does a linear search need a sorted list?", opts: ["Yes", "No", "Only for numbers", "Only for text"], a: 1, why: "A linear search works on any list." },
  { q: "What does Count ← Count + 1 do?", opts: ["Totals the values", "Adds 1 to the count", "Finds the maximum", "Resets Count"], a: 1, why: "It counts one more." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Totalling", "Keeping a running total by adding each value to it, starting at 0."],
  ["Counting", "Adding 1 to a count each time a condition is met, starting at 0."],
  ["Maximum", "The largest value; start with the first item and replace it when a larger one is found."],
  ["Minimum", "The smallest value; start with the first item and replace it when a smaller one is found."],
  ["Average", "The total divided by the number of items."],
  ["Linear search", "Checking each item in order until the target is found or the list ends."],
  ["Bubble sort", "A sort that repeatedly compares neighbouring items and swaps them if out of order."],
  ["Pass", "One trip through the list in a bubble sort."],
  ["Temporary variable", "A variable used to hold a value while two values are swapped."]
] });
