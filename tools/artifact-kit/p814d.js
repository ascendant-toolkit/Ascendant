const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)", WARN = "var(--warn)";
const fv = (v) => (v === null || v === undefined ? "?" : v === true ? "TRUE" : v === false ? "FALSE" : typeof v === "string" ? '"' + v + '"' : v);
/* One animation frame: variable boxes, optional character cells or input queue, a condition result, and the output so far. */
function trSvg(f, o) {
  const W = 640; let s = SV.text(14, 24, f.title || o.title || "", "lbl bd", { "text-anchor": "start" });
  if (f.right) s += SV.text(W - 14, 24, f.right, "lbl bd t4", { "text-anchor": "end" });
  const vs = f.vars || [], n = vs.length;
  if (n) {
    const gap = 10, w = Math.min(150, Math.floor((W - 28 - (n - 1) * gap) / n)), tot = n * w + (n - 1) * gap, x0 = (W - tot) / 2;
    vs.forEach(([k, v], i) => {
      const x = x0 + i * (w + gap), hi = (f.hl || []).includes(k), t = String(fv(v));
      s += SV.rect(x, 38, w, 58, "", { rx: 10, style: `fill:var(--surface);stroke:${hi ? ACC : MUT};stroke-width:${hi ? 4 : 2}` });
      s += SV.text(x + w / 2, 56, k, "sm", { "text-anchor": "middle" });
      s += SV.text(x + w / 2, 84, t, "lbl bd", { "text-anchor": "middle", style: `font-size:${t.length > 9 ? 13 : t.length > 6 ? 16 : 20}px;font-family:var(--mono)` });
    });
  }
  if (f.cells) {
    const a = f.cells, m = a.length, g = 5, w = Math.min(44, Math.floor((W - 28 - (m - 1) * g) / m)), tot = m * w + (m - 1) * g, x0 = (W - tot) / 2;
    s += Lib.cells(a, { x0, y: 112, w, h: 38, gap: g, cls: f.cc || {}, idx: false });
    a.forEach((_, i) => (s += SV.text(x0 + i * (w + g) + w / 2, 166, i + 1, "sm", { "text-anchor": "middle" })));
  } else if (f.inp) {
    const t = f.inp.length ? "Waiting to be typed in:   " + f.inp.map(fv).join("    ") : "Nothing left to input";
    s += SV.rect(14, 114, W - 28, 36, "", { rx: 10, style: "fill:var(--soft);stroke:var(--line);stroke-width:2" });
    s += SV.text(W / 2, 138, t, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:15px" });
  }
  if (f.cond) s += SV.text(W / 2, 196, `${f.cond[0]}   is   ${f.cond[1] ? "TRUE" : "FALSE"}`, "lbl bd " + (f.cond[1] ? "t3" : "t2"), { "text-anchor": "middle", style: "font-family:var(--mono)" });
  else if (f.note) s += SV.text(W / 2, 196, f.note, "lbl bd " + (f.nc || ""), { "text-anchor": "middle" });
  let ot = (f.out || []).join("   "); if (ot.length > 62) ot = "…" + ot.slice(-61);
  s += SV.rect(14, 212, W - 28, 44, "", { rx: 10, style: "fill:var(--soft);stroke:var(--line);stroke-width:2" });
  s += SV.text(26, 229, "Output", "sm", { "text-anchor": "start" });
  s += SV.text(26, 249, ot, "lbl bd", { "text-anchor": "start", style: "font-family:var(--mono);font-size:15px" });
  return s;
}
function tr(el, o) {
  Lib.algo(el, { w: 640, h: 270, label: o.label, pseudo: o.pseudo, py: o.py, dwell: o.dwell || 2000, frames: o.frames.map((f) => ({ cap: f.cap, ps: f.ps, py: f.py, svg: trSvg(f, o) })) });
}
const nums = (v, k = 20) => v.trim().split(/[\s,]+/).filter(Boolean).map(Number).filter((x) => !isNaN(x)).slice(0, k);

const TOT_PS = ["Total ← 0", "FOR Count ← 1 TO 5", "    INPUT Number", "    Total ← Total + Number", "NEXT Count", "OUTPUT Total"], TOT_PY = ["total = 0", "for count in range(1, 6):", "    number = int(input())", "    total = total + number", "print(total)"];
const CNT_PS = ["Count ← 0", "FOR Index ← 1 TO 5", "    INPUT Mark", "    IF Mark >= 50", "      THEN", "        Count ← Count + 1", "    ENDIF", "NEXT Index", "OUTPUT Count"], CNT_PY = ["count = 0", "for index in range(1, 6):", "    mark = int(input())", "    if mark >= 50:", "        count = count + 1", "print(count)"];
const SEN_PS = ["Total ← 0", "Count ← 0", "INPUT Number", "WHILE Number <> -1 DO", "    Total ← Total + Number", "    Count ← Count + 1", "    INPUT Number", "ENDWHILE", "Average ← Total / Count", "OUTPUT Average"], SEN_PY = ["total = 0", "count = 0", "number = int(input())", "while number != -1:", "    total = total + number", "    count = count + 1", "    number = int(input())", "average = total / count", "print(average)"];
tr($("#aT"), { label: "Totalling", title: "Running total", pseudo: TOT_PS, py: TOT_PY, dwell: 1900, frames: [{"cap": "<b>Total ← 0</b> before the loop. A running total must <b>start at 0</b>.", "ps": [0], "py": [0], "vars": [["Count", null], ["Number", null], ["Total", 0]], "hl": ["Total"], "out": [], "inp": [12, 7, 20, 5, 16]}, {"cap": "Loop 1. <b>INPUT Number</b>: 12.", "ps": [1, 2], "py": [1, 2], "vars": [["Count", 1], ["Number", 12], ["Total", 0]], "hl": ["Count", "Number"], "out": [], "inp": [7, 20, 5, 16]}, {"cap": "<b>Total ← Total + 12</b> = <b>12</b>. The new total replaces the old one.", "ps": [3], "py": [3], "vars": [["Count", 1], ["Number", 12], ["Total", 12]], "hl": ["Total"], "out": [], "inp": [7, 20, 5, 16]}, {"cap": "Loop 2. <b>INPUT Number</b>: 7.", "ps": [1, 2], "py": [1, 2], "vars": [["Count", 2], ["Number", 7], ["Total", 12]], "hl": ["Count", "Number"], "out": [], "inp": [20, 5, 16]}, {"cap": "<b>Total ← Total + 7</b> = <b>19</b>. The new total replaces the old one.", "ps": [3], "py": [3], "vars": [["Count", 2], ["Number", 7], ["Total", 19]], "hl": ["Total"], "out": [], "inp": [20, 5, 16]}, {"cap": "Loop 3. <b>INPUT Number</b>: 20.", "ps": [1, 2], "py": [1, 2], "vars": [["Count", 3], ["Number", 20], ["Total", 19]], "hl": ["Count", "Number"], "out": [], "inp": [5, 16]}, {"cap": "<b>Total ← Total + 20</b> = <b>39</b>. The new total replaces the old one.", "ps": [3], "py": [3], "vars": [["Count", 3], ["Number", 20], ["Total", 39]], "hl": ["Total"], "out": [], "inp": [5, 16]}, {"cap": "Loop 4. <b>INPUT Number</b>: 5.", "ps": [1, 2], "py": [1, 2], "vars": [["Count", 4], ["Number", 5], ["Total", 39]], "hl": ["Count", "Number"], "out": [], "inp": [16]}, {"cap": "<b>Total ← Total + 5</b> = <b>44</b>. The new total replaces the old one.", "ps": [3], "py": [3], "vars": [["Count", 4], ["Number", 5], ["Total", 44]], "hl": ["Total"], "out": [], "inp": [16]}, {"cap": "Loop 5. <b>INPUT Number</b>: 16.", "ps": [1, 2], "py": [1, 2], "vars": [["Count", 5], ["Number", 16], ["Total", 44]], "hl": ["Count", "Number"], "out": [], "inp": []}, {"cap": "<b>Total ← Total + 16</b> = <b>60</b>. The new total replaces the old one.", "ps": [3], "py": [3], "vars": [["Count", 5], ["Number", 16], ["Total", 60]], "hl": ["Total"], "out": [], "inp": []}, {"cap": "The loop has finished. <b>OUTPUT Total</b> shows <b>60</b>, once, after the loop.", "ps": [5], "py": [4], "vars": [["Count", 5], ["Number", 16], ["Total", 60]], "hl": ["Total"], "out": ["60"], "inp": []}] });
tr($("#aC"), { label: "Counting", title: "Counting marks >= 50", pseudo: CNT_PS, py: CNT_PY, dwell: 1900, frames: [{"cap": "<b>Count ← 0</b> before the loop. A count <b>starts at 0</b>.", "ps": [0], "py": [0], "vars": [["Index", null], ["Mark", null], ["Count", 0]], "hl": ["Count"], "out": [], "inp": [62, 45, 78, 50, 31]}, {"cap": "Loop 1. <b>INPUT Mark</b>: 62.", "ps": [1, 2], "py": [1, 2], "vars": [["Index", 1], ["Mark", 62], ["Count", 0]], "hl": ["Index", "Mark"], "out": [], "inp": [45, 78, 50, 31]}, {"cap": "Is 62 >= 50?", "ps": [3], "py": [3], "vars": [["Index", 1], ["Mark", 62], ["Count", 0]], "hl": [], "out": [], "cond": ["62 >= 50", true], "inp": [45, 78, 50, 31]}, {"cap": "TRUE, so <b>Count ← Count + 1</b> = <b>1</b>. Counting adds <b>1</b>, not the mark.", "ps": [5], "py": [4], "vars": [["Index", 1], ["Mark", 62], ["Count", 1]], "hl": ["Count"], "out": [], "cond": ["62 >= 50", true], "inp": [45, 78, 50, 31]}, {"cap": "Loop 2. <b>INPUT Mark</b>: 45.", "ps": [1, 2], "py": [1, 2], "vars": [["Index", 2], ["Mark", 45], ["Count", 1]], "hl": ["Index", "Mark"], "out": [], "inp": [78, 50, 31]}, {"cap": "Is 45 >= 50?", "ps": [3], "py": [3], "vars": [["Index", 2], ["Mark", 45], ["Count", 1]], "hl": [], "out": [], "cond": ["45 >= 50", false], "inp": [78, 50, 31]}, {"cap": "Loop 3. <b>INPUT Mark</b>: 78.", "ps": [1, 2], "py": [1, 2], "vars": [["Index", 3], ["Mark", 78], ["Count", 1]], "hl": ["Index", "Mark"], "out": [], "inp": [50, 31]}, {"cap": "Is 78 >= 50?", "ps": [3], "py": [3], "vars": [["Index", 3], ["Mark", 78], ["Count", 1]], "hl": [], "out": [], "cond": ["78 >= 50", true], "inp": [50, 31]}, {"cap": "TRUE, so <b>Count ← Count + 1</b> = <b>2</b>. Counting adds <b>1</b>, not the mark.", "ps": [5], "py": [4], "vars": [["Index", 3], ["Mark", 78], ["Count", 2]], "hl": ["Count"], "out": [], "cond": ["78 >= 50", true], "inp": [50, 31]}, {"cap": "Loop 4. <b>INPUT Mark</b>: 50.", "ps": [1, 2], "py": [1, 2], "vars": [["Index", 4], ["Mark", 50], ["Count", 2]], "hl": ["Index", "Mark"], "out": [], "inp": [31]}, {"cap": "Is 50 >= 50?", "ps": [3], "py": [3], "vars": [["Index", 4], ["Mark", 50], ["Count", 2]], "hl": [], "out": [], "cond": ["50 >= 50", true], "inp": [31]}, {"cap": "TRUE, so <b>Count ← Count + 1</b> = <b>3</b>. Counting adds <b>1</b>, not the mark.", "ps": [5], "py": [4], "vars": [["Index", 4], ["Mark", 50], ["Count", 3]], "hl": ["Count"], "out": [], "cond": ["50 >= 50", true], "inp": [31]}, {"cap": "Loop 5. <b>INPUT Mark</b>: 31.", "ps": [1, 2], "py": [1, 2], "vars": [["Index", 5], ["Mark", 31], ["Count", 3]], "hl": ["Index", "Mark"], "out": [], "inp": []}, {"cap": "Is 31 >= 50?", "ps": [3], "py": [3], "vars": [["Index", 5], ["Mark", 31], ["Count", 3]], "hl": [], "out": [], "cond": ["31 >= 50", false], "inp": []}, {"cap": "After the loop, <b>OUTPUT Count</b>: <b>3</b> marks were 50 or more.", "ps": [8], "py": [5], "vars": [["Index", 5], ["Mark", 31], ["Count", 3]], "hl": ["Count"], "out": ["3"], "inp": []}] });
tr($("#aS"), { label: "Sentinel loop and average", title: "Sentinel -1", pseudo: SEN_PS, py: SEN_PY, dwell: 2100, frames: [{"cap": "Set <b>Total</b> and <b>Count</b> to 0. The user will stop the program by typing <b>-1</b> (a <span class=\"kw\">sentinel</span>).", "ps": [0, 1], "py": [0, 1], "vars": [["Number", null], ["Total", 0], ["Count", 0], ["Average", null]], "hl": ["Total", "Count"], "out": [], "inp": [8, 5, 11, -1]}, {"cap": "<b>INPUT Number</b> before the loop: 8.", "ps": [2], "py": [2], "vars": [["Number", 8], ["Total", 0], ["Count", 0], ["Average", null]], "hl": ["Number"], "out": [], "inp": [5, 11, -1]}, {"cap": "Is 8 <> -1? Yes, so the loop runs.", "ps": [3], "py": [3], "vars": [["Number", 8], ["Total", 0], ["Count", 0], ["Average", null]], "hl": [], "out": [], "cond": ["8 <> -1", true], "inp": [5, 11, -1]}, {"cap": "<b>Total ← Total + 8</b> = 8. <b>Count ← Count + 1</b> = 1.", "ps": [4, 5], "py": [4, 5], "vars": [["Number", 8], ["Total", 8], ["Count", 1], ["Average", null]], "hl": ["Total", "Count"], "out": [], "inp": [5, 11, -1]}, {"cap": "<b>INPUT Number</b> again, at the <b>end</b> of the loop body: 5.", "ps": [6], "py": [6], "vars": [["Number", 5], ["Total", 8], ["Count", 1], ["Average", null]], "hl": ["Number"], "out": [], "inp": [11, -1]}, {"cap": "Is 5 <> -1? Yes, so the loop runs.", "ps": [3], "py": [3], "vars": [["Number", 5], ["Total", 8], ["Count", 1], ["Average", null]], "hl": [], "out": [], "cond": ["5 <> -1", true], "inp": [11, -1]}, {"cap": "<b>Total ← Total + 5</b> = 13. <b>Count ← Count + 1</b> = 2.", "ps": [4, 5], "py": [4, 5], "vars": [["Number", 5], ["Total", 13], ["Count", 2], ["Average", null]], "hl": ["Total", "Count"], "out": [], "inp": [11, -1]}, {"cap": "<b>INPUT Number</b> again, at the <b>end</b> of the loop body: 11.", "ps": [6], "py": [6], "vars": [["Number", 11], ["Total", 13], ["Count", 2], ["Average", null]], "hl": ["Number"], "out": [], "inp": [-1]}, {"cap": "Is 11 <> -1? Yes, so the loop runs.", "ps": [3], "py": [3], "vars": [["Number", 11], ["Total", 13], ["Count", 2], ["Average", null]], "hl": [], "out": [], "cond": ["11 <> -1", true], "inp": [-1]}, {"cap": "<b>Total ← Total + 11</b> = 24. <b>Count ← Count + 1</b> = 3.", "ps": [4, 5], "py": [4, 5], "vars": [["Number", 11], ["Total", 24], ["Count", 3], ["Average", null]], "hl": ["Total", "Count"], "out": [], "inp": [-1]}, {"cap": "<b>INPUT Number</b> again, at the <b>end</b> of the loop body: -1.", "ps": [6], "py": [6], "vars": [["Number", -1], ["Total", 24], ["Count", 3], ["Average", null]], "hl": ["Number"], "out": [], "inp": []}, {"cap": "Is -1 <> -1? No, so the loop ends. The -1 is <b>not</b> added to the total.", "ps": [3, 7], "py": [3], "vars": [["Number", -1], ["Total", 24], ["Count", 3], ["Average", null]], "hl": [], "out": [], "cond": ["-1 <> -1", false], "inp": []}, {"cap": "<b>Average ← Total / Count</b> = 24 / 3 = <b>8</b>.", "ps": [8], "py": [7], "vars": [["Number", -1], ["Total", 24], ["Count", 3], ["Average", 8]], "hl": ["Average"], "out": []}, {"cap": "<b>OUTPUT Average</b>: 8.", "ps": [9], "py": [8], "vars": [["Number", -1], ["Total", 24], ["Count", 3], ["Average", 8]], "hl": ["Average"], "out": ["8"]}] });
Lib.codePanel($("#cdTot"), { pseudo: TOT_PS, py: TOT_PY });
Lib.codePanel($("#cdCnt"), { pseudo: CNT_PS, py: CNT_PY });
Lib.codePanel($("#cdSen"), { pseudo: SEN_PS, py: SEN_PY });


/* ---------- Lab 1 ---------- */
(() => {
  let sl; const inp = $("#pi");
  const upd = () => {
    if (!sl) return; const D = nums(inp.value, 20), lim = sl.get();
    if (!D.length) { ["pt", "pc", "po", "pa"].forEach((i) => ($("#" + i).textContent = "–")); $("#pv").textContent = "Enter some prices."; return; }
    const t = D.reduce((a, b) => a + b, 0), c = D.filter((x) => x > lim).length;
    $("#pt").textContent = fmtN(t, 2); $("#pc").textContent = D.length; $("#po").textContent = c; $("#pa").textContent = fmtN(t / D.length, 2);
    $("#pv").innerHTML = `<b>Total</b> adds each price: ${fmtN(t, 2)}. <b>Count</b> adds 1 per item: ${D.length}. <b>Count over $${lim}</b> adds 1 only when Price > ${lim}: ${c}. Average = ${fmtN(t, 2)} / ${D.length} = ${fmtN(t / D.length, 2)}.`;
  };
  sl = Lib.slider($("#s1"), { id: "pl", label: "Expensive means over $", min: 0, max: 20, value: 10, onInput: upd });
  inp.addEventListener("input", upd); upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  const D = [4, 6, 5];
  function upd() {
    const a = $("#b1").value, b = $("#b2").value, c = $("#b3").value;
    const ps = [a === "ten" ? "Total ← 10" : a === "none" ? "(Total is never set)" : "Total ← 0", "Count ← 0", "FOR Index ← 1 TO 3"];
    if (a === "inloop") ps.push("    Total ← 0");
    ps.push("    INPUT Number", "    Total ← Total + Number", b === "ok" ? "    Count ← Count + 1" : "    Count ← Count + Number");
    if (c === "in") ps.push("    OUTPUT Total, Count");
    ps.push("NEXT Index"); if (c === "after") ps.push("OUTPUT Total, Count");
    const py = [a === "ten" ? "total = 10" : a === "none" ? "# total is never set" : "total = 0", "count = 0", "for index in range(3):"];
    if (a === "inloop") py.push("    total = 0");
    py.push("    number = int(input())", "    total = total + number", b === "ok" ? "    count = count + 1" : "    count = count + number");
    if (c === "in") py.push("    print(total, count)");
    if (c === "after") py.push("print(total, count)");
    Lib.codePanel($("#bcode"), { pseudo: ps, py });
    let t = a === "ten" ? 10 : a === "none" ? undefined : 0, n = 0, outs = [], err = false;
    for (const x of D) { if (a === "inloop") t = 0; if (t === undefined) { err = true; break; } t += x; n += b === "ok" ? 1 : x; if (c === "in") outs.push(`${t} ${n}`); }
    if (!err && c === "after") outs.push(`${t} ${n}`);
    $("#bout").innerHTML = err ? `<span class="kpri">Error: Total has no value when Total + Number is worked out.</span>` : outs.join("<br>");
    const good = a === "ok" && b === "ok" && c === "after";
    $("#bv").innerHTML = good ? `<span class="kpub">Correct.</span> Total 15 (4 + 6 + 5) and Count 3 (three numbers).` :
      [a === "ten" ? "Total started at 10, so every total is 10 too high." : "", a === "inloop" ? "Total is reset to 0 on every repeat, so only the last number survives." : "", a === "none" ? "A variable must be given a start value." : "", b === "val" ? "Count adds the <b>value</b> instead of 1, so it is totalling, not counting." : "", c === "in" ? "OUTPUT inside the loop shows a running total on every repeat." : ""].filter(Boolean).join(" ");
  }
  ["b1", "b2", "b3"].forEach((i) => ($("#" + i).onchange = upd)); upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  let sl; const inp = $("#mi");
  const upd = () => {
    if (!sl) return; const D = nums(inp.value, 20), pm = sl.get();
    if (!D.length) { ["mp", "mf", "mt"].forEach((i) => ($("#" + i).textContent = "–")); $("#mv").textContent = "Enter some marks."; return; }
    const p = D.filter((x) => x >= pm).length;
    $("#mp").textContent = p; $("#mf").textContent = D.length - p; $("#mt").textContent = D.length;
    $("#mv").innerHTML = `Marks of ${pm} or more add 1 to <b>Pass</b>. All the others add 1 to <b>Fail</b>. ${p} + ${D.length - p} = ${D.length}.`;
  };
  sl = Lib.slider($("#s2"), { id: "pm", label: "Pass mark ", min: 0, max: 100, value: 50, onInput: upd });
  inp.addEventListener("input", upd); upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Sort each statement.", buckets: [{ label: "Totalling" }, { label: "Counting" }, { label: "Initialising" }], items: [
  { text: "Total ← Total + Price", b: 0 }, { text: "Sum ← Sum + Number", b: 0 },
  { text: "Count ← Count + 1", b: 1 }, { text: "Pass ← Pass + 1", b: 1 },
  { text: "Total ← 0", b: 2 }, { text: "Count ← 0", b: 2 }, { text: "Fail ← 0", b: 2 }],
  done: "Initialise to 0, add the value to total, add 1 to count." });
Lib.order($("#o1"), { prompt: "Put the steps of the average algorithm in order.", items: [
  "Total ← 0 and Count ← 0", "INPUT Number", "WHILE Number <> -1", "Add Number to Total and 1 to Count, then INPUT the next Number", "ENDWHILE, then Average ← Total / Count"], done: "Initialise, first input, test, body, after the loop." });
Lib.calc($("#c1"), { qs: [
  { q: "The numbers 4, 9, 2 and 7 are totalled. What is the final Total?", a: 22, sol: "4 + 9 + 2 + 7 = 22." },
  { q: "How many of 12, 7, 20, 5 and 16 are greater than 10?", a: 3, sol: "12, 20 and 16: 3." },
  { q: "What is the average of 8, 5 and 11?", a: 8, sol: "24 / 3 = 8." },
  { q: "A loop runs 8 times and contains Count ← Count + 1 with no IF. What is Count at the end (starting from 0)?", a: 8, sol: "1 is added on each of the 8 repeats." },
  { q: "Total was wrongly started at 10. The inputs 3 and 4 are added. What is Total at the end?", a: 17, sol: "10 + 3 + 4 = 17. It should be 7." },
  { q: "Numbers are input until -1. The user types 5, 9, 4, -1. What is Count at the end?", a: 3, sol: "Only 5, 9 and 4 are counted. The sentinel -1 is not." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What should a running total start at?", opts: ["0", "1", "The first number", "-1"], a: 0, why: "Start at 0 so the first value is added to nothing." },
  { q: "What does Count ← Count + 1 do?", opts: ["Adds 1 to the count", "Adds the input to the count", "Resets Count", "Outputs Count"], a: 0, why: "Counting adds 1 each time." },
  { q: "Where should OUTPUT Total normally go?", opts: ["After the loop", "Inside the loop", "Before the loop", "It does not matter"], a: 0, why: "After the loop the total is complete." },
  { q: "A sentinel value is...", opts: ["A special value that ends the input", "The largest number", "The first number", "A loop counter"], a: 0, why: "For example -1 signals that there is no more data." },
  { q: "Average is worked out as...", opts: ["Total / Count", "Total * Count", "Total + Count", "Count / Total"], a: 0, why: "The total divided by how many values there were." }] });
Lib.cards($("#fc1"), { cards: [
  ["Totalling", "Keeping a running total by adding each value to it, starting at 0."],
  ["Counting", "Adding 1 to a variable each time something happens, starting at 0."],
  ["Running total", "A total that is updated each time round a loop."],
  ["Initialise", "Give a variable its starting value before the loop."],
  ["Sentinel", "A special value, such as -1, typed to show there is no more data."],
  ["Average", "The total divided by the number of values (Total / Count)."],
  ["Counter", "A variable used to count, for example Count or Pass."]] });

