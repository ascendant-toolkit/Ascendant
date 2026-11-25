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

const BAD_PS = ["INPUT A", "INPUT B", "C ← A * B", "IF C > 100", "  THEN", "    C ← C * 0.9", "ENDIF", "OUTPUT C"], BAD_PY = ["a = float(input())", "b = int(input())", "c = a * b", "if c > 100:", "    c = c * 0.9", "print(c)"], GOOD_PS = ["CONSTANT DiscountLimit ← 100", "CONSTANT DiscountRate ← 0.1", "// Input one order", "INPUT TicketPrice", "INPUT Quantity", "TotalCost ← TicketPrice * Quantity", "// Large orders get a discount", "IF TotalCost > DiscountLimit", "  THEN", "    TotalCost ← TotalCost * (1 - DiscountRate)", "ENDIF", "OUTPUT TotalCost"], GOOD_PY = ["DISCOUNT_LIMIT = 100", "DISCOUNT_RATE = 0.1", "# Input one order", "ticket_price = float(input())", "quantity = int(input())", "total_cost = ticket_price * quantity", "# Large orders get a discount", "if total_cost > DISCOUNT_LIMIT:", "    total_cost = total_cost * (1 - DISCOUNT_RATE)", "print(total_cost)"], SUB_PS = ["// Returns the price after any discount", "FUNCTION ApplyDiscount(Cost : REAL) RETURNS REAL", "    IF Cost > 100", "      THEN", "        RETURN Cost * 0.9", "      ELSE", "        RETURN Cost", "    ENDIF", "ENDFUNCTION", "", "// Main program: two orders", "OUTPUT ApplyDiscount(80)", "OUTPUT ApplyDiscount(200)"], SUB_PY = ["# Returns the price after any discount", "def apply_discount(cost):", "    if cost > 100:", "        return cost * 0.9", "    else:", "        return cost", "", "# Main program: two orders", "print(apply_discount(80))", "print(apply_discount(200))"];
tr($("#aB"), { label: "Hard to maintain", pseudo: BAD_PS, py: BAD_PY, frames: [{"cap": "This program works. But what is it <b>for</b>? Watch it and try to guess. The user types 15, then 8.", "ps": [0], "py": [0], "vars": [["A", null], ["B", null], ["C", null]], "hl": [], "out": [], "inp": [15, 8]}, {"cap": "<b>INPUT A</b>. A price? An age? A length?", "ps": [0], "py": [0], "vars": [["A", 15], ["B", null], ["C", null]], "hl": ["A"], "out": [], "inp": [8]}, {"cap": "<b>INPUT B</b>. The name tells us nothing.", "ps": [1], "py": [1], "vars": [["A", 15], ["B", 8], ["C", null]], "hl": ["B"], "out": [], "inp": []}, {"cap": "<b>C ← A * B</b> = 120.", "ps": [2], "py": [2], "vars": [["A", 15], ["B", 8], ["C", 120]], "hl": ["C"], "out": []}, {"cap": "<b>Why 100?</b> There is no clue.", "ps": [3], "py": [3], "vars": [["A", 15], ["B", 8], ["C", 120]], "hl": [], "out": [], "cond": ["120 > 100", true]}, {"cap": "<b>C ← C * 0.9</b> = 108. What does 0.9 mean?", "ps": [5], "py": [4], "vars": [["A", 15], ["B", 8], ["C", 108]], "hl": ["C"], "out": []}, {"cap": "<b>OUTPUT C</b>: 108. Correct, but hard to understand and risky to change.", "ps": [7], "py": [5], "vars": [["A", 15], ["B", 8], ["C", 108]], "hl": [], "out": ["108"]}] });
tr($("#aG"), { label: "Maintainable", pseudo: GOOD_PS, py: GOOD_PY, frames: [{"cap": "The <b>same program</b>, written to be maintained. Constants at the top name the fixed values.", "ps": [0, 1], "py": [0, 1], "vars": [["TicketPrice", null], ["Quantity", null], ["TotalCost", null]], "hl": [], "out": [], "note": "Limit = 100, rate = 0.1", "nc": "t4", "inp": [15, 8]}, {"cap": "A <b>comment</b> says what this section does. <b>TicketPrice</b> is 15.", "ps": [2, 3], "py": [2, 3], "vars": [["TicketPrice", 15], ["Quantity", null], ["TotalCost", null]], "hl": ["TicketPrice"], "out": [], "inp": [8]}, {"cap": "<b>INPUT Quantity</b>: 8.", "ps": [4], "py": [4], "vars": [["TicketPrice", 15], ["Quantity", 8], ["TotalCost", null]], "hl": ["Quantity"], "out": [], "inp": []}, {"cap": "The calculation now reads like a sentence.", "ps": [5], "py": [5], "vars": [["TicketPrice", 15], ["Quantity", 8], ["TotalCost", 120]], "hl": ["TotalCost"], "out": []}, {"cap": "The comment and the name explain the test.", "ps": [6, 7], "py": [6, 7], "vars": [["TicketPrice", 15], ["Quantity", 8], ["TotalCost", 120]], "hl": [], "out": [], "cond": ["120 > DiscountLimit", true]}, {"cap": "Take off the discount: <b>108</b>.", "ps": [9], "py": [8], "vars": [["TicketPrice", 15], ["Quantity", 8], ["TotalCost", 108]], "hl": ["TotalCost"], "out": []}, {"cap": "Same output, <b>108</b>. Changing the rate now means editing <b>one line</b>.", "ps": [11], "py": [9], "vars": [["TicketPrice", 15], ["Quantity", 8], ["TotalCost", 108]], "hl": [], "out": ["108"]}] });
tr($("#aS"), { label: "Using a function", pseudo: SUB_PS, py: SUB_PY, frames: [{"cap": "The discount rule is written <b>once</b>, in a function with a meaningful name and a comment.", "ps": [0, 1, 8], "py": [0, 1], "vars": [], "hl": [], "out": [], "title": "Main program"}, {"cap": "<b>ApplyDiscount(80)</b> is called.", "ps": [11], "py": [8], "vars": [], "hl": [], "out": [], "title": "Main program"}, {"cap": "Inside the function, is 80 > 100?", "ps": [2], "py": [2], "vars": [["Cost", 80]], "hl": ["Cost"], "out": [], "title": "Inside ApplyDiscount", "cond": ["80 > 100", false]}, {"cap": "<b>RETURN</b> 80.", "ps": [6], "py": [5], "vars": [["Cost", 80]], "hl": [], "out": [], "title": "Inside ApplyDiscount", "note": "returns 80", "nc": "t3"}, {"cap": "The main program outputs <b>80</b>.", "ps": [11], "py": [8], "vars": [], "hl": [], "out": ["80"], "title": "Main program"}, {"cap": "<b>ApplyDiscount(200)</b> is called.", "ps": [12], "py": [9], "vars": [], "hl": [], "out": ["80"], "title": "Main program"}, {"cap": "Inside the function, is 200 > 100?", "ps": [2], "py": [2], "vars": [["Cost", 200]], "hl": ["Cost"], "out": ["80"], "title": "Inside ApplyDiscount", "cond": ["200 > 100", true]}, {"cap": "<b>RETURN</b> 180.", "ps": [4], "py": [3], "vars": [["Cost", 200]], "hl": [], "out": ["80"], "title": "Inside ApplyDiscount", "note": "returns 180", "nc": "t3"}, {"cap": "The main program outputs <b>180</b>.", "ps": [12], "py": [9], "vars": [], "hl": [], "out": ["80", "180"], "title": "Main program"}] });
Lib.codePanel($("#cdCm"), { pseudo: ["// Add up the five test marks", "Total ← 0", "FOR Test ← 1 TO 5", "    INPUT Mark", "    Total ← Total + Mark    // keep a running total", "NEXT Test"], py: ["# Add up the five test marks", "total = 0", "for test in range(1, 6):", "    mark = int(input())", "    total = total + mark    # keep a running total"] });
Lib.codePanel($("#cdSub"), { pseudo: SUB_PS, py: SUB_PY });
Lib.codePanel($("#cdGood"), { pseudo: GOOD_PS, py: GOOD_PY });


/* ---------- Lab 1 ---------- */
(() => {
  const upd = () => {
    const N = $("#iN").checked, K = $("#iK").checked, C = $("#iC").checked, F = $("#iF").checked, I = $("#iI").checked;
    const build = (py) => {
      const nm = (a, b, c) => (N ? (py ? c : b) : a);
      const price = nm("a", "TicketPrice", "ticket_price"), qty = nm("b", "Quantity", "quantity"), tot = nm("c", "TotalCost", "total_cost");
      const lim = K ? (py ? "DISCOUNT_LIMIT" : "DiscountLimit") : "100", fac = K ? `(1 - ${py ? "DISCOUNT_RATE" : "DiscountRate"})` : "0.9";
      const fn = nm("f", "ApplyDiscount", "apply_discount"), p = nm("x", "Cost", "cost");
      const sp = (n) => (I || py ? " ".repeat(n) : ""), cm = (t) => { if (C) L.push((py ? "# " : "// ") + t); };
      const L = [], ar = py ? "=" : "←";
      if (K) L.push(py ? "DISCOUNT_LIMIT = 100" : "CONSTANT DiscountLimit ← 100", py ? "DISCOUNT_RATE = 0.1" : "CONSTANT DiscountRate ← 0.1");
      if (F) {
        cm("Returns the cost after any discount");
        if (py) L.push(`def ${fn}(${p}):`, `    if ${p} > ${lim}:`, `        ${p} = ${p} * ${fac}`, `    return ${p}`);
        else L.push(`FUNCTION ${fn}(${p} : REAL) RETURNS REAL`, `${sp(4)}IF ${p} > ${lim}`, `${sp(6)}THEN`, `${sp(8)}${p} ← ${p} * ${fac}`, `${sp(4)}ENDIF`, `${sp(4)}RETURN ${p}`, "ENDFUNCTION");
      }
      cm("Input one order");
      L.push(py ? `${price} = float(input())` : `INPUT ${price}`, py ? `${qty} = int(input())` : `INPUT ${qty}`, `${tot} ${ar} ${price} * ${qty}`);
      cm("Large orders get a discount");
      if (F) L.push(`${tot} ${ar} ${fn}(${tot})`);
      else if (py) L.push(`if ${tot} > ${lim}:`, `    ${tot} = ${tot} * ${fac}`);
      else L.push(`IF ${tot} > ${lim}`, `${sp(2)}THEN`, `${sp(4)}${tot} ← ${tot} * ${fac}`, "ENDIF");
      L.push(py ? `print(${tot})` : `OUTPUT ${tot}`);
      return L;
    };
    Lib.codePanel($("#lcode"), { pseudo: build(false), py: build(true) });
    const n = $$(".imp").filter((x) => x.checked).length;
    $("#lv").innerHTML = `<b>${n} of 5</b> improvements. ` + (n === 5 ? "A new programmer could understand and change this." : "Which one would help a new reader most?") + (I ? "" : " Python always needs indentation, so its tab stays indented.");
  };
  $$(".imp").forEach((x) => (x.onchange = upd)); upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  let a, b;
  const upd = () => { if (!a || !b) return; const n = a.get(), m = Math.min(b.get(), n); $("#m1n").textContent = n;
    $("#mv").innerHTML = m ? `If <b>${m}</b> line${m > 1 ? "s are" : " is"} missed, the program uses <b>two different rates</b> and gives wrong results in places. A constant avoids this.` : `All ${n} lines must be found and edited correctly. With a constant there is only one.`; };
  a = Lib.slider($("#s1"), { id: "mu", label: "Places the value is used ", min: 1, max: 40, value: 12, onInput: upd });
  b = Lib.slider($("#s2"), { id: "mm", label: "Lines the programmer misses ", min: 0, max: 5, value: 1, onInput: upd });
  upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Sort the identifiers.", buckets: [{ label: "Meaningful" }, { label: "Poor or not allowed" }], items: [
  { text: "HighestScore", b: 0 }, { text: "CalculateTotal", b: 0 }, { text: "MaxPlayers", b: 0 }, { text: "StudentName", b: 0 },
  { text: "x1", b: 1 }, { text: "thing", b: 1 }, { text: "Total Cost", b: 1 }, { text: "OUTPUT", b: 1 }],
  done: "Good names describe the contents or the job, have no spaces and are not keywords." });
Lib.match($("#m1"), { prompt: "Drag each benefit to its feature.", pairs: [["Meaningful identifiers", "Shows what each item stores or does"], ["Comments", "Explains the purpose of a section to the reader"], ["Procedures and functions", "Lets parts be tested and reused separately"], ["Constants", "A fixed value is changed in one place"], ["Indentation", "Shows where structures start and end"]] });
Lib.order($("#o1"), { prompt: "Arrange the parts of a well-laid-out program.", items: ["// Program purpose", "CONSTANT TaxRate ← 0.1", "DECLARE Price : REAL", "FUNCTION AddTax(Cost : REAL) RETURNS REAL ... ENDFUNCTION", "INPUT Price", "OUTPUT AddTax(Price)"], done: "Purpose, constants, variables, routines, then the main program." });
Lib.classify($("#cl2"), { prompt: "Which comments would help a reader?", buckets: [{ label: "Useful" }, { label: "Not useful" }], items: [
  { text: "// Repeat until the PIN is valid", b: 0 }, { text: "// Discount applies to orders over 100", b: 0 }, { text: "// Returns the average of three marks", b: 0 },
  { text: "// This is a line of code", b: 1 }, { text: "// X", b: 1 }, { text: "// Add 1 to Count (above: Count ← Count + 1)", b: 1 }],
  done: "Useful comments explain purpose or reason, not what is already obvious." });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is the most meaningful identifier for the number of items sold?", opts: ["ItemsSold", "n", "Data1", "Items Sold"], a: 0, why: "Descriptive and without a space." },
  { q: "What does the computer do with a comment?", opts: ["Ignores it", "Outputs it", "Stores it in a variable", "Runs it twice"], a: 0, why: "Comments are for people." },
  { q: "Which makes a repeated job easiest to change?", opts: ["Putting it in a procedure or function", "Copying it wherever it is needed", "Removing the indentation", "Using shorter names"], a: 0, why: "One place to edit." },
  { q: "Why use a constant for a fixed rate?", opts: ["It is changed in one place", "It can change while the program runs", "It makes the rate a parameter", "It stops the program needing inputs"], a: 0, why: "Easier and safer to update." }] });
Lib.cards($("#fc1"), { cards: [
  ["Maintainable program", "A program that is easy to read, understand and change."],
  ["Identifier", "The name of a variable, constant, array, procedure or function."],
  ["Meaningful identifier", "A name that describes what the item stores or does."],
  ["Comment", "A note for the reader that the computer ignores."],
  ["Constant", "A named value that does not change while the program runs."],
  ["Indentation", "Moving lines to the right to show the structure."]] });

