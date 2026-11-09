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

const FOR_PS = ["FOR Count ← 1 TO 4", "    OUTPUT Count * 3", "NEXT Count"], FOR_PY = ["for count in range(1, 5):", "    print(count * 3)"];
const WH_PS = ["Number ← 3", "WHILE Number > 0 DO", "    OUTPUT Number", "    Number ← Number - 1", "ENDWHILE", "OUTPUT \"Go!\""], WH_PY = ["number = 3", "while number > 0:", "    print(number)", "    number = number - 1", "print(\"Go!\")"];
const RP_PS = ["REPEAT", "    INPUT Password", "    IF Password <> \"open\"", "      THEN", "        OUTPUT \"Wrong\"", "    ENDIF", "UNTIL Password = \"open\"", "OUTPUT \"Welcome\""], RP_PY = ["while True:", "    password = input()", "    if password != \"open\":", "        print(\"Wrong\")", "    else:", "        break", "print(\"Welcome\")"];
tr($("#aF"), { label: "FOR loop", title: "FOR loop", pseudo: FOR_PS, py: FOR_PY, dwell: 1800, frames: [{"cap": "<b>FOR Count ← 1 TO 4</b> will run the loop body 4 times. It sets Count to 1 first.", "ps": [0], "py": [0], "vars": [["Count", null]], "hl": [], "out": []}, {"cap": "Count is <b>1</b>. Body: OUTPUT 1 * 3.", "ps": [1], "py": [1], "vars": [["Count", 1]], "hl": ["Count"], "out": []}, {"cap": "Output <b>3</b>. <b>NEXT Count</b> adds 1 to Count and goes back to the top.", "ps": [2], "py": [1], "vars": [["Count", 1]], "hl": ["Count"], "out": ["3"]}, {"cap": "Count is <b>2</b>. Body: OUTPUT 2 * 3.", "ps": [1], "py": [1], "vars": [["Count", 2]], "hl": ["Count"], "out": ["3"]}, {"cap": "Output <b>6</b>. <b>NEXT Count</b> adds 1 to Count and goes back to the top.", "ps": [2], "py": [1], "vars": [["Count", 2]], "hl": ["Count"], "out": ["3", "6"]}, {"cap": "Count is <b>3</b>. Body: OUTPUT 3 * 3.", "ps": [1], "py": [1], "vars": [["Count", 3]], "hl": ["Count"], "out": ["3", "6"]}, {"cap": "Output <b>9</b>. <b>NEXT Count</b> adds 1 to Count and goes back to the top.", "ps": [2], "py": [1], "vars": [["Count", 3]], "hl": ["Count"], "out": ["3", "6", "9"]}, {"cap": "Count is <b>4</b>. Body: OUTPUT 4 * 3.", "ps": [1], "py": [1], "vars": [["Count", 4]], "hl": ["Count"], "out": ["3", "6", "9"]}, {"cap": "Output <b>12</b>. Count has reached 4, the last value, so the loop ends.", "ps": [2], "py": [1], "vars": [["Count", 4]], "hl": ["Count"], "out": ["3", "6", "9", "12"], "note": "4 repeats, then stop", "nc": "t3"}] });
tr($("#aW"), { label: "WHILE loop", title: "WHILE loop", pseudo: WH_PS, py: WH_PY, dwell: 1800, frames: [{"cap": "<b>Number ← 3</b>.", "ps": [0], "py": [0], "vars": [["Number", 3]], "hl": ["Number"], "out": []}, {"cap": "The condition is tested <b>before</b> each repeat. Is Number > 0?", "ps": [1], "py": [1], "vars": [["Number", 3]], "hl": [], "out": [], "cond": ["3 > 0", true]}, {"cap": "TRUE, so the body runs. <b>OUTPUT 3</b>.", "ps": [2], "py": [2], "vars": [["Number", 3]], "hl": [], "out": ["3"], "cond": ["3 > 0", true]}, {"cap": "<b>Number ← Number - 1</b>. It is now 2. Back to the test.", "ps": [3], "py": [3], "vars": [["Number", 2]], "hl": ["Number"], "out": ["3"]}, {"cap": "The condition is tested <b>before</b> each repeat. Is Number > 0?", "ps": [1], "py": [1], "vars": [["Number", 2]], "hl": [], "out": ["3"], "cond": ["2 > 0", true]}, {"cap": "TRUE, so the body runs. <b>OUTPUT 2</b>.", "ps": [2], "py": [2], "vars": [["Number", 2]], "hl": [], "out": ["3", "2"], "cond": ["2 > 0", true]}, {"cap": "<b>Number ← Number - 1</b>. It is now 1. Back to the test.", "ps": [3], "py": [3], "vars": [["Number", 1]], "hl": ["Number"], "out": ["3", "2"]}, {"cap": "The condition is tested <b>before</b> each repeat. Is Number > 0?", "ps": [1], "py": [1], "vars": [["Number", 1]], "hl": [], "out": ["3", "2"], "cond": ["1 > 0", true]}, {"cap": "TRUE, so the body runs. <b>OUTPUT 1</b>.", "ps": [2], "py": [2], "vars": [["Number", 1]], "hl": [], "out": ["3", "2", "1"], "cond": ["1 > 0", true]}, {"cap": "<b>Number ← Number - 1</b>. It is now 0. Back to the test.", "ps": [3], "py": [3], "vars": [["Number", 0]], "hl": ["Number"], "out": ["3", "2", "1"]}, {"cap": "The condition is tested <b>before</b> each repeat. Is Number > 0?", "ps": [1], "py": [1], "vars": [["Number", 0]], "hl": [], "out": ["3", "2", "1"], "cond": ["0 > 0", false]}, {"cap": "FALSE, so the loop is skipped and the program carries on after ENDWHILE.", "ps": [4], "py": [], "vars": [["Number", 0]], "hl": [], "out": ["3", "2", "1"], "cond": ["0 > 0", false]}, {"cap": "<b>OUTPUT \"Go!\"</b>.", "ps": [5], "py": [4], "vars": [["Number", 0]], "hl": [], "out": ["3", "2", "1", "Go!"]}] });
tr($("#aR"), { label: "REPEAT loop", title: "REPEAT ... UNTIL loop", pseudo: RP_PS, py: RP_PY, dwell: 2000, frames: [{"cap": "REPEAT runs the body <b>first</b>, then tests the condition at the end.", "ps": [0], "py": [0], "vars": [["Password", null]], "hl": [], "out": [], "inp": ["abc", "123", "open"]}, {"cap": "<b>INPUT Password</b>: the user types \"abc\".", "ps": [1], "py": [1], "vars": [["Password", "abc"]], "hl": ["Password"], "out": [], "inp": ["123", "open"]}, {"cap": "\"abc\" is not \"open\", so OUTPUT \"Wrong\".", "ps": [2, 3, 4], "py": [2, 3], "vars": [["Password", "abc"]], "hl": ["Password"], "out": ["Wrong"], "inp": ["123", "open"]}, {"cap": "<b>UNTIL Password = \"open\"</b>? Not yet, so go back to REPEAT.", "ps": [6], "py": [0], "vars": [["Password", "abc"]], "hl": [], "out": ["Wrong"], "cond": ["\"abc\" = \"open\"", false], "inp": ["123", "open"]}, {"cap": "<b>INPUT Password</b>: the user types \"123\".", "ps": [1], "py": [1], "vars": [["Password", "123"]], "hl": ["Password"], "out": ["Wrong"], "inp": ["open"]}, {"cap": "\"123\" is not \"open\", so OUTPUT \"Wrong\".", "ps": [2, 3, 4], "py": [2, 3], "vars": [["Password", "123"]], "hl": ["Password"], "out": ["Wrong", "Wrong"], "inp": ["open"]}, {"cap": "<b>UNTIL Password = \"open\"</b>? Not yet, so go back to REPEAT.", "ps": [6], "py": [0], "vars": [["Password", "123"]], "hl": [], "out": ["Wrong", "Wrong"], "cond": ["\"123\" = \"open\"", false], "inp": ["open"]}, {"cap": "<b>INPUT Password</b>: the user types \"open\".", "ps": [1], "py": [1], "vars": [["Password", "open"]], "hl": ["Password"], "out": ["Wrong", "Wrong"], "inp": []}, {"cap": "<b>UNTIL Password = \"open\"</b>? It is, so stop repeating.", "ps": [6], "py": [4, 5], "vars": [["Password", "open"]], "hl": [], "out": ["Wrong", "Wrong"], "cond": ["\"open\" = \"open\"", true], "inp": []}, {"cap": "The loop has ended. <b>OUTPUT \"Welcome\"</b>. The body ran 3 times; it always runs <b>at least once</b>.", "ps": [7], "py": [6], "vars": [["Password", "open"]], "hl": [], "out": ["Wrong", "Wrong", "Welcome"], "note": "3 repeats", "nc": "t3"}] });
Lib.codePanel($("#cdFor"), { pseudo: FOR_PS, py: FOR_PY });
Lib.codePanel($("#cdStep"), { pseudo: ["FOR Count ← 0 TO 10 STEP 2", "    OUTPUT Count", "NEXT Count"], py: ["for count in range(0, 11, 2):", "    print(count)"] });
Lib.codePanel($("#cdWhile"), { pseudo: WH_PS, py: WH_PY });
Lib.codePanel($("#cdRep"), { pseudo: RP_PS, py: RP_PY });


/* ---------- Lab 1 ---------- */
(() => {
  let a, b, c;
  const upd = () => {
    if (!a || !b || !c) return; const s = a.get(), e = b.get(), st = c.get(), v = [];
    for (let i = s; i <= e && v.length < 60; i += st) v.push(i);
    Lib.codePanel($("#fcode"), { pseudo: [`FOR Count ← ${s} TO ${e}${st > 1 ? " STEP " + st : ""}`, "    OUTPUT Count", "NEXT Count"], py: [`for count in range(${s}, ${e + 1}${st > 1 ? ", " + st : ""}):`, "    print(count)"] });
    $("#fn").textContent = v.length; $("#fv").textContent = v.length ? v.join(", ") : "none";
    $("#fvd").innerHTML = v.length ? `The loop runs <b>${v.length}</b> time${v.length > 1 ? "s" : ""}. Count starts at ${s}${v.length > 1 ? ` and the last value is ${v[v.length - 1]}` : ""}.` : `The start (${s}) is already past the end (${e}), so the body <b>never runs</b>.`;
  };
  a = Lib.slider($("#s1"), { id: "fs", label: "Start ", min: 0, max: 10, value: 1, onInput: upd });
  b = Lib.slider($("#s2"), { id: "fe", label: "End ", min: 0, max: 20, value: 8, onInput: upd });
  c = Lib.slider($("#s3"), { id: "ft", label: "Step ", min: 1, max: 5, value: 1, onInput: upd });
  upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  Lib.slider($("#s4"), { id: "ws", label: "Starting value of Number ", min: 0, max: 6, value: 5, onInput: (n0) => {
    let w = [], r = [], n = n0; while (n < 3) { w.push(n); n++; }
    n = n0; do { r.push(n); n++; } while (!(n >= 3) && r.length < 20);
    $("#wn").textContent = w.length; $("#rn").textContent = r.length;
    $("#wo").textContent = w.join(" ") || "(nothing)"; $("#ro").textContent = r.join(" ");
    $("#wv").innerHTML = n0 >= 3 ? `Start ${n0} already meets the stopping condition. <b>WHILE never runs its body</b> (0 times). <b>REPEAT runs it once</b> before it tests.` : `Start ${n0}: both loops run ${w.length} time${w.length === 1 ? "" : "s"}. Try a start of 3 or more.`; } });
})();

/* ---------- Lab 3 ---------- */
(() => {
  let a, b;
  const upd = () => { if (!a || !b) return; const r = a.get(), c = b.get();
    $("#nout").innerHTML = Array.from({ length: r }, () => "★".repeat(c)).join("<br>");
    $("#nv").innerHTML = `The outer loop runs <b>${r}</b> times. Each time the inner loop runs <b>${c}</b> times, so the inner body runs <b>${r} × ${c} = ${r * c}</b> times in total.`; };
  a = Lib.slider($("#s5"), { id: "nr", label: "Rows (outer loop) ", min: 1, max: 6, value: 3, onInput: upd });
  b = Lib.slider($("#s6"), { id: "nc", label: "Stars per row (inner loop) ", min: 1, max: 10, value: 5, onInput: upd });
  upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which loop fits best?", buckets: [{ label: "FOR" }, { label: "WHILE" }, { label: "REPEAT ... UNTIL" }], items: [
  { text: "Output the 12 times table", b: 0 }, { text: "Read 30 test marks", b: 0 },
  { text: "Keep going while the player has lives left (they may have none)", b: 1 }, { text: "Count down while a number is above zero", b: 1 },
  { text: "Ask for a PIN again until it is valid", b: 2 }, { text: "Show a menu at least once, until the user chooses Quit", b: 2 }],
  done: "Known count: FOR. Might run zero times: WHILE. Must run at least once: REPEAT." });
Lib.order($("#o1"), { prompt: "Put this loop in order.", items: ["REPEAT", "INPUT Password", "UNTIL Password = \"open\"", "OUTPUT \"Welcome\""], done: "REPEAT, body, UNTIL test, then output after the loop." });
Lib.calc($("#c1"), { qs: [
  { q: "How many times does FOR Count ← 1 TO 10 run its body?", a: 10, sol: "10 − 1 + 1 = 10." },
  { q: "How many times does FOR Count ← 3 TO 9 run its body?", a: 7, sol: "3, 4, 5, 6, 7, 8, 9 is 7 values." },
  { q: "How many times does FOR Count ← 0 TO 10 STEP 2 run its body?", a: 6, sol: "0, 2, 4, 6, 8, 10 is 6 values." },
  { q: "Number ← 5. WHILE Number > 5 DO ... ENDWHILE. How many times does the body run?", a: 0, sol: "5 > 5 is FALSE at the start, so 0 times." },
  { q: "Number ← 5. REPEAT ... UNTIL Number >= 5. How many times does the body run?", a: 1, sol: "The body runs once before the test, and then 5 >= 5 is TRUE." },
  { q: "An outer loop runs 4 times and an inner loop runs 3 times each. How many times does the inner body run?", a: 12, sol: "4 × 3 = 12." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which loop is count-controlled?", opts: ["FOR", "WHILE", "REPEAT", "IF"], a: 0, why: "A FOR loop runs a set number of times." },
  { q: "Where does a WHILE loop test its condition?", opts: ["At the start", "At the end", "In the middle", "It never tests"], a: 0, why: "WHILE tests before each repeat." },
  { q: "A REPEAT ... UNTIL loop stops when the condition is...", opts: ["TRUE", "FALSE", "zero", "negative"], a: 0, why: "UNTIL means stop once it is TRUE." },
  { q: "What causes an infinite loop?", opts: ["The condition never becomes the stopping value", "Using a FOR loop", "A short program", "Using INPUT"], a: 0, why: "Nothing inside changes the condition." },
  { q: "In Python, range(1, 6) gives...", opts: ["1 2 3 4 5", "1 2 3 4 5 6", "0 1 2 3 4 5", "2 3 4 5 6"], a: 0, why: "range stops before the end value." }] });
Lib.cards($("#fc1"), { cards: [
  ["Iteration", "Repeating a set of instructions."],
  ["Loop", "The block of code that is repeated."],
  ["FOR loop", "A count-controlled loop that repeats a set number of times."],
  ["WHILE loop", "A condition-controlled loop that tests first and repeats while the condition is TRUE."],
  ["REPEAT ... UNTIL", "A condition-controlled loop that tests last and stops when the condition is TRUE."],
  ["Loop counter", "A variable, such as Count, that changes each time round a FOR loop."],
  ["Infinite loop", "A loop that never ends because its condition never changes."],
  ["Nested loop", "A loop inside another loop."]] });

