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

const IPO_PS = ["DECLARE Price : REAL", "DECLARE Quantity : INTEGER", "DECLARE Total : REAL", "INPUT Price", "INPUT Quantity", "Total ← Price * Quantity", 'OUTPUT "Total cost: ", Total'];
const IPO_PY = ["price = float(input())", "quantity = int(input())", "total = price * quantity", 'print("Total cost:", total)'];
const SW_PS = ["A ← 5", "B ← 9", "Temp ← A", "A ← B", "B ← Temp", "OUTPUT A, B"];
const SW_PY = ["a = 5", "b = 9", "temp = a", "a = b", "b = temp", "print(a, b)"];
const WR_PS = ["A ← 5", "B ← 9", "A ← B", "B ← A", "OUTPUT A, B"];
const WR_PY = ["a = 5", "b = 9", "a = b", "b = a", "print(a, b)"];
tr($("#aT"), { label: "Input, process, output", title: "Ticket cost", pseudo: IPO_PS, py: IPO_PY, dwell: 2300, frames: [{"cap": "The program runs <b>one line at a time, from the top</b>. DECLARE creates the three variables. They have no value yet.", "ps": [0, 1, 2], "py": [], "vars": [["Price", null], ["Quantity", null], ["Total", null]], "hl": [], "out": [], "inp": [4.5, 3]}, {"cap": "<b>INPUT Price</b>: the user types 4.5 and it is stored in Price.", "ps": [3], "py": [0], "vars": [["Price", 4.5], ["Quantity", null], ["Total", null]], "hl": ["Price"], "out": [], "inp": [3]}, {"cap": "<b>INPUT Quantity</b>: the user types 3.", "ps": [4], "py": [1], "vars": [["Price", 4.5], ["Quantity", 3], ["Total", null]], "hl": ["Quantity"], "out": [], "inp": []}, {"cap": "<b>Process.</b> Total ← 4.5 * 3 = <b>13.5</b>. Both inputs already have values, so this line works.", "ps": [5], "py": [2], "vars": [["Price", 4.5], ["Quantity", 3], ["Total", 13.5]], "hl": ["Total"], "out": [], "inp": []}, {"cap": "<b>OUTPUT</b> shows the result. The last line has run, so the program ends.", "ps": [6], "py": [3], "vars": [["Price", 4.5], ["Quantity", 3], ["Total", 13.5]], "hl": ["Total"], "out": ["Total cost: 13.5"], "inp": []}] });
tr($("#aS"), { label: "Swapping with a temporary variable", title: "Swap A and B", pseudo: SW_PS, py: SW_PY, dwell: 2200, frames: [{"cap": "<b>A ← 5.</b>", "ps": [0], "py": [0], "vars": [["A", 5], ["B", null], ["Temp", null]], "hl": ["A"], "out": []}, {"cap": "<b>B ← 9.</b>", "ps": [1], "py": [1], "vars": [["A", 5], ["B", 9], ["Temp", null]], "hl": ["B"], "out": []}, {"cap": "<b>Temp ← A.</b> Save A's value (5) before it is overwritten.", "ps": [2], "py": [2], "vars": [["A", 5], ["B", 9], ["Temp", 5]], "hl": ["Temp"], "out": []}, {"cap": "<b>A ← B.</b> A is now 9. The old 5 is safe in Temp.", "ps": [3], "py": [3], "vars": [["A", 9], ["B", 9], ["Temp", 5]], "hl": ["A"], "out": []}, {"cap": "<b>B ← Temp.</b> B takes the saved 5. The values have been swapped.", "ps": [4], "py": [4], "vars": [["A", 9], ["B", 5], ["Temp", 5]], "hl": ["B"], "out": []}, {"cap": "<b>OUTPUT A, B</b> shows 9 5.", "ps": [5], "py": [5], "vars": [["A", 9], ["B", 5], ["Temp", 5]], "hl": [], "out": ["9 5"]}] });
tr($("#aW"), { label: "A swap without Temp", title: "Wrong: no Temp", pseudo: WR_PS, py: WR_PY, dwell: 2200, frames: [{"cap": "<b>A ← 5.</b>", "ps": [0], "py": [0], "vars": [["A", 5], ["B", null]], "hl": ["A"], "out": []}, {"cap": "<b>B ← 9.</b>", "ps": [1], "py": [1], "vars": [["A", 5], ["B", 9]], "hl": ["B"], "out": []}, {"cap": "<b>A ← B.</b> A becomes 9. The old 5 is overwritten and lost.", "ps": [2], "py": [2], "vars": [["A", 9], ["B", 9]], "hl": ["A"], "out": [], "note": "5 has gone", "nc": "t2"}, {"cap": "<b>B ← A.</b> A is already 9, so B stays 9.", "ps": [3], "py": [3], "vars": [["A", 9], ["B", 9]], "hl": ["B"], "out": [], "note": "Both are 9", "nc": "t2"}, {"cap": "<b>OUTPUT A, B</b> shows 9 9. The swap failed because there was no Temp.", "ps": [4], "py": [4], "vars": [["A", 9], ["B", 9]], "hl": [], "out": ["9 9"], "note": "Wrong", "nc": "t2"}] });
Lib.codePanel($("#cdIPO"), { pseudo: IPO_PS, py: IPO_PY });
Lib.codePanel($("#cdOrd"), { pseudo: ["INPUT Price", "INPUT Quantity", "Total ← Price * Quantity", 'OUTPUT "Total: ", Total'], py: ["price = float(input())", "quantity = int(input())", "total = price * quantity", 'print("Total:", total)'] });
Lib.codePanel($("#cdSwap"), { pseudo: ["Temp ← A", "A ← B", "B ← Temp"], py: ["temp = a", "a = b", "b = temp"] });


/* ---------- Lab 1: fix the order ---------- */
(() => {
  const S = [
    { ps: "Price ← 20", sets: "Price", uses: [], f: (e) => 20 },
    { ps: "Discount ← Price / 10", sets: "Discount", uses: ["Price"], f: (e) => e.Price / 10 },
    { ps: "Final ← Price - Discount", sets: "Final", uses: ["Price", "Discount"], f: (e) => e.Price - e.Discount },
    { ps: "OUTPUT Final", out: "Final", uses: ["Final"] }];
  let ord = [1, 3, 0, 2];
  const box = $("#ro"), v = $("#roV");
  function draw() {
    const env = {}; let err = -1, msg = "", outp = null;
    ord.forEach((si, pos) => {
      if (err >= 0) return; const s = S[si], miss = s.uses.find((u) => env[u] === undefined);
      if (miss) { err = pos; msg = `Line ${pos + 1} uses <b>${miss}</b>, but it has no value yet.`; return; }
      if (s.out) outp = env[s.out]; else env[s.sets] = s.f(env);
    });
    box.innerHTML = '<ol class="scn" style="list-style:none;padding:0">' + ord.map((si, pos) => `<li class="r ${err === pos ? "no" : err >= 0 && pos > err ? "" : err < 0 ? "ok" : "ok"}"><b>${pos + 1}</b><span class="q" style="font-family:var(--mono)">${esc(S[si].ps)}</span><button class="b" data-m="${pos}" data-d="-1" aria-label="Move up" ${pos === 0 ? "disabled" : ""}>↑</button><button class="b" data-m="${pos}" data-d="1" aria-label="Move down" ${pos === 3 ? "disabled" : ""}>↓</button></li>`).join("") + "</ol>";
    v.innerHTML = err >= 0 ? `<span class="kpri">Error.</span> ${msg} Move a line that gives it a value above this one.` : `<span class="kpub">It runs.</span> Output: <b>${outp}</b>. (The discount is 10% of 20, so the final price is 18.)`;
  }
  box.addEventListener("click", (e) => { const b = e.target.closest("button[data-m]"); if (!b) return; const p = +b.dataset.m, d = +b.dataset.d; [ord[p], ord[p + d]] = [ord[p + d], ord[p]]; draw(); });
  $("#roShuf").onclick = () => { do { ord = shuffle([0, 1, 2, 3]); } while (ord.join() === "0,1,2,3"); draw(); };
  $("#roFix").onclick = () => { ord = [0, 1, 2, 3]; draw(); };
  draw();
})();

/* ---------- Lab 2: input, process, output ---------- */
(() => {
  let a, b;
  const upd = () => { if (!a || !b) return; const h = a.get(), r = b.get();
    $("#ipI").innerHTML = `INPUT Hours → <b>${h}</b> &nbsp; INPUT Rate → <b>${r}</b>`;
    $("#ipP").innerHTML = `Pay ← Hours * Rate → ${h} * ${r} = <b>${h * r}</b>`;
    $("#ipO").innerHTML = `OUTPUT "Pay: $", Pay → <b>Pay: $${h * r}</b>`; };
  a = Lib.slider($("#s1"), { id: "sh", label: "Hours worked ", min: 0, max: 40, value: 25, onInput: upd });
  b = Lib.slider($("#s2"), { id: "sr", label: "Rate per hour ($) ", min: 5, max: 30, value: 12, onInput: upd });
  upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is each statement an input, a process or an output?", buckets: [{ label: "Input" }, { label: "Process" }, { label: "Output" }], items: [
  { text: "INPUT Age", b: 0 }, { text: "INPUT Name", b: 0 }, { text: "Read a number typed by the user", b: 0 },
  { text: "Area ← Length * Width", b: 1 }, { text: "Total ← Price * Quantity", b: 1 }, { text: "Temp ← A", b: 1 },
  { text: "OUTPUT Total", b: 2 }, { text: 'OUTPUT "Hello ", Name', b: 2 }, { text: "Show the answer on the screen", b: 2 }],
  done: "Input brings data in, process works it out, output shows it." });
Lib.order($("#o1"), { prompt: "Put these steps of an area program in order. Length is input first.", items: [
  "Declare the variables", "INPUT Length", "INPUT Width", "Area ← Length * Width", "OUTPUT Area"], done: "Declare, inputs, process, output." });
Lib.order($("#o2"), { prompt: "Put the lines of a swap of A and B in order.", items: ["Temp ← A", "A ← B", "B ← Temp"], done: "Save A, copy B into A, copy the saved value into B." });
Lib.calc($("#c1"), { qs: [
  { q: "Price ← 8, Quantity ← 5, Total ← Price * Quantity. What is Total?", a: 40, sol: "8 * 5 = 40." },
  { q: "A ← 6, B ← 4, A ← A + B, B ← A - B. What is B at the end?", a: 6, sol: "A becomes 10. Then B ← 10 - 4 = 6.", hint: "A changes on the third line, before B is worked out." },
  { q: "X ← 3, Y ← X * 2, X ← Y + 1. What is X at the end?", a: 7, sol: "Y = 6. X ← 6 + 1 = 7." },
  { q: "Hours ← 7, Rate ← 12, Pay ← Hours * Rate, Pay ← Pay + 10. What is Pay?", a: 94, sol: "7 * 12 = 84. Then 84 + 10 = 94." },
  { q: "A program has 7 lines, with no selection and no iteration. How many lines are run?", a: 7, sol: "Sequence runs every line once, in order: 7." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does sequence mean?", opts: ["Instructions run in the order written", "Some instructions are skipped", "Instructions repeat", "Instructions run at random"], a: 0, why: "Sequence is one instruction after another, in order." },
  { q: "What does Total ← 5 do?", opts: ["Stores 5 in Total", "Compares Total with 5", "Outputs 5", "Inputs 5"], a: 0, why: "The arrow is assignment." },
  { q: "Which line should come first?", opts: ["INPUT Price", "Total ← Price * 2", "OUTPUT Total", "They can be in any order"], a: 0, why: "Price needs a value before it is used." },
  { q: "Why is Temp used in a swap?", opts: ["To hold a value so it is not overwritten", "To make the program faster", "To store the output", "It is not needed"], a: 0, why: "A ← B would otherwise destroy A's old value." },
  { q: "In Python, what does input() always give you?", opts: ["Text", "An integer", "A decimal", "A Boolean"], a: 0, why: "Convert with int() or float() to use it as a number." }] });
Lib.cards($("#fc1"), { cards: [
  ["Sequence", "Instructions carried out one after another, in the order they are written."],
  ["Input", "Data entered into a program, for example INPUT Age."],
  ["Process", "A calculation or other action done on the data."],
  ["Output", "Data shown to the user, for example OUTPUT Total."],
  ["Assignment", "Storing a value in a variable using ←, for example Total ← 0."],
  ["Variable", "A named memory location whose value can change while the program runs."],
  ["DECLARE", "A pseudocode statement that names a variable and gives its data type."],
  ["Temporary variable", "A variable used to hold a value while two values are swapped."]] });

