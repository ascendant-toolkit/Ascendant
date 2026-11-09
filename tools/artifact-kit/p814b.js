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

const G_PS = ["INPUT Mark", "IF Mark >= 70", "  THEN", "    OUTPUT \"Grade A\"", "  ELSE", "    IF Mark >= 50", "      THEN", "        OUTPUT \"Grade B\"", "      ELSE", "        OUTPUT \"Grade C\"", "    ENDIF", "ENDIF"], G_PY = ["mark = int(input())", "if mark >= 70:", "    print(\"Grade A\")", "elif mark >= 50:", "    print(\"Grade B\")", "else:", "    print(\"Grade C\")"];
const IE_PS = ["DECLARE Mark : INTEGER", "INPUT Mark", "IF Mark >= 50", "  THEN", '    OUTPUT "Pass"', "  ELSE", '    OUTPUT "Fail"', "ENDIF"];
const IE_PY = ["mark = int(input())", "if mark >= 50:", '    print("Pass")', "else:", '    print("Fail")'];
const C_PS = ["INPUT Choice", "CASE OF Choice", '  1 : OUTPUT "Play"', '  2 : OUTPUT "Options"', '  3 : OUTPUT "Quit"', '  OTHERWISE OUTPUT "Invalid choice"', "ENDCASE"];
const C_PY = ["choice = int(input())", "if choice == 1:", '    print("Play")', "elif choice == 2:", '    print("Options")', "elif choice == 3:", '    print("Quit")', "else:", '    print("Invalid choice")'];
tr($("#aI"), { label: "IF THEN ELSE", title: "Pass or fail", pseudo: IE_PS, py: IE_PY, dwell: 2200, frames: [{"cap": "The program starts. Mark has no value yet.", "ps": [0], "py": [], "vars": [["Mark", null]], "hl": [], "out": [], "inp": [62]}, {"cap": "<b>INPUT Mark</b>: the user types 62.", "ps": [1], "py": [0], "vars": [["Mark", 62]], "hl": ["Mark"], "out": [], "inp": []}, {"cap": "The <b>condition</b> is tested. Is 62 >= 50? It is.", "ps": [2], "py": [1], "vars": [["Mark", 62]], "hl": [], "out": [], "cond": ["Mark >= 50", true]}, {"cap": "The condition is TRUE, so the <b>THEN</b> branch runs. The ELSE branch is skipped.", "ps": [3], "py": [2], "vars": [["Mark", 62]], "hl": [], "out": [], "cond": ["Mark >= 50", true]}, {"cap": "<b>OUTPUT \"Pass\"</b>. The program then jumps to after ENDIF.", "ps": [4], "py": [2], "vars": [["Mark", 62]], "hl": [], "out": ["Pass"], "cond": ["Mark >= 50", true]}, {"cap": "<b>ENDIF</b>: the selection is over. Only <b>one</b> of the two branches ever runs.", "ps": [7], "py": [], "vars": [["Mark", 62]], "hl": [], "out": ["Pass"], "note": "THEN branch ran, ELSE did not", "nc": "t3"}] });
tr($("#aN"), { label: "Nested IF", title: "Grade", pseudo: G_PS, py: G_PY, dwell: 2200, frames: [{"cap": "Three possible outcomes need <b>more than one test</b>. Mark is going to be 58.", "ps": [0], "py": [], "vars": [["Mark", null]], "hl": [], "out": [], "inp": [58]}, {"cap": "<b>INPUT Mark</b>: 58.", "ps": [0], "py": [0], "vars": [["Mark", 58]], "hl": ["Mark"], "out": [], "inp": []}, {"cap": "First test: is 58 >= 70? No.", "ps": [1], "py": [1], "vars": [["Mark", 58]], "hl": [], "out": [], "cond": ["Mark >= 70", false]}, {"cap": "FALSE, so jump to <b>ELSE</b>. Another test is inside it.", "ps": [4, 5], "py": [3], "vars": [["Mark", 58]], "hl": [], "out": [], "cond": ["Mark >= 70", false]}, {"cap": "Second test: is 58 >= 50? Yes.", "ps": [5], "py": [3], "vars": [["Mark", 58]], "hl": [], "out": [], "cond": ["Mark >= 50", true]}, {"cap": "TRUE, so this THEN runs.", "ps": [6, 7], "py": [4], "vars": [["Mark", 58]], "hl": [], "out": [], "cond": ["Mark >= 50", true]}, {"cap": "<b>OUTPUT \"Grade B\"</b>. The last ELSE is skipped.", "ps": [7], "py": [4], "vars": [["Mark", 58]], "hl": [], "out": ["Grade B"], "cond": ["Mark >= 50", true]}, {"cap": "Both ENDIFs close the selection. Tests run <b>top to bottom</b> and the first TRUE one wins.", "ps": [10, 11], "py": [], "vars": [["Mark", 58]], "hl": [], "out": ["Grade B"], "note": "Grade B", "nc": "t3"}] });
tr($("#aC"), { label: "CASE OF", title: "Menu", pseudo: C_PS, py: C_PY, dwell: 2200, frames: [{"cap": "A menu: 1 Play, 2 Options, 3 Quit. The user will choose 2.", "ps": [0], "py": [], "vars": [["Choice", null]], "hl": [], "out": [], "inp": [2]}, {"cap": "<b>INPUT Choice</b>: 2.", "ps": [0], "py": [0], "vars": [["Choice", 2]], "hl": ["Choice"], "out": [], "inp": []}, {"cap": "<b>CASE OF Choice</b> compares Choice with each value in turn. Is it 1? No.", "ps": [1, 2], "py": [1], "vars": [["Choice", 2]], "hl": [], "out": [], "cond": ["Choice = 1", false]}, {"cap": "Is it 2? Yes.", "ps": [3], "py": [3], "vars": [["Choice", 2]], "hl": [], "out": [], "cond": ["Choice = 2", true]}, {"cap": "A match, so this line runs: <b>OUTPUT \"Options\"</b>. The remaining cases are skipped.", "ps": [3], "py": [4], "vars": [["Choice", 2]], "hl": [], "out": ["Options"], "cond": ["Choice = 2", true]}, {"cap": "<b>ENDCASE</b>. OTHERWISE would only have run if <b>no value</b> had matched.", "ps": [6], "py": [], "vars": [["Choice", 2]], "hl": [], "out": ["Options"], "note": "Matched case 2", "nc": "t3"}] });
Lib.codePanel($("#cdIf"), { pseudo: ["INPUT Battery", "IF Battery < 20", "  THEN", '    OUTPUT "Low battery"', "ENDIF"], py: ["battery = int(input())", "if battery < 20:", '    print("Low battery")'] });
Lib.codePanel($("#cdIfElse"), { pseudo: IE_PS.slice(1), py: IE_PY });
Lib.codePanel($("#cdNest"), { pseudo: G_PS, py: G_PY });
Lib.codePanel($("#cdCase"), { pseudo: C_PS, py: C_PY });


/* ---------- Lab 1 ---------- */
(() => {
  const cp = Lib.codePanel($("#lcode"), { pseudo: G_PS, py: G_PY });
  Lib.slider($("#s1"), { id: "sm", label: "Mark ", min: 0, max: 100, value: 58, onInput: (m) => {
    const a = m >= 70, b = m >= 50;
    if (a) { cp.hl([1, 2, 3], [1, 2]); $("#lv").innerHTML = `${m} >= 70 is TRUE, so <b>Grade A</b>. Nothing else is tested.`; }
    else if (b) { cp.hl([1, 4, 5, 6, 7], [1, 3, 4]); $("#lv").innerHTML = `${m} >= 70 is FALSE. ${m} >= 50 is TRUE, so <b>Grade B</b>.`; }
    else { cp.hl([1, 4, 5, 8, 9], [1, 3, 5, 6]); $("#lv").innerHTML = `${m} >= 70 is FALSE and ${m} >= 50 is FALSE, so the last ELSE runs: <b>Grade C</b>.`; } } });
})();

/* ---------- Lab 2 ---------- */
(() => {
  const OK = [G_PS.slice(0), G_PY], BADPS = ["INPUT Mark", "IF Mark >= 50", "  THEN", '    OUTPUT "Grade B"', "  ELSE", "    IF Mark >= 70", "      THEN", '        OUTPUT "Grade A"', "    ENDIF", "ENDIF"];
  const BADPY = ["mark = int(input())", "if mark >= 50:", '    print("Grade B")', "elif mark >= 70:", '    print("Grade A")'];
  let sl;
  const upd = () => {
    if (!sl) return; const m = sl.get(), bad = $("#ord").value === "bad", cp = Lib.codePanel($("#ocode"), bad ? { pseudo: BADPS, py: BADPY } : { pseudo: G_PS, py: G_PY });
    if (!bad) { const g = m >= 70 ? "A" : m >= 50 ? "B" : "C"; cp.hl(m >= 70 ? [1, 3] : m >= 50 ? [1, 5, 7] : [1, 5, 9], m >= 70 ? [1, 2] : m >= 50 ? [3, 4] : [5, 6]); $("#ov").innerHTML = `Mark ${m}: <b>Grade ${g}</b>. ${m >= 70 ? "Correct." : ""}`; }
    else { cp.hl(m >= 50 ? [1, 3] : [1, 4, 5], m >= 50 ? [1, 2] : [1, 3]); $("#ov").innerHTML = m >= 70 ? `Mark ${m}: <span class="kpri">Grade B</span>. The first test (${m} >= 50) is TRUE, so the test for 70 is never reached.` : m >= 50 ? `Mark ${m}: <b>Grade B</b>. Correct here, but only by luck.` : `Mark ${m}: <b>nothing is output</b>. The 70 test is only reached for marks below 50, and none of those pass it.`; }
  };
  sl = Lib.slider($("#s2"), { id: "so", label: "Mark ", min: 0, max: 100, value: 85, onInput: upd });
  $("#ord").onchange = upd; upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  const sel = $("#ch"); sel.innerHTML = [1, 2, 3, 4, 9].map((v) => `<option>${v}</option>`).join("");
  const cp = Lib.codePanel($("#ccode"), { pseudo: C_PS, py: C_PY });
  const out = { 1: ["Play", [2], [2]], 2: ["Options", [3], [4]], 3: ["Quit", [4], [6]] };
  const upd = () => { const c = +sel.value, o = out[c];
    if (o) { cp.hl([0, 1].concat(o[1]), [0, 1].concat(o[2])); $("#cv").innerHTML = `Choice ${c} matches a case: <b>${o[0]}</b>.`; }
    else { cp.hl([0, 1, 5], [0, 7, 8]); $("#cv").innerHTML = `${c} matches no case, so OTHERWISE runs: <b>Invalid choice</b>.`; } };
  sel.onchange = upd; upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which structure fits each situation best?", buckets: [{ label: "IF ... THEN" }, { label: "IF ... ELSE" }, { label: "Nested IF" }, { label: "CASE OF" }], items: [
  { text: "Output a warning only if the battery is below 20", b: 0 }, { text: "Add a bonus point only if the key was found", b: 0 },
  { text: "Output Adult or Child", b: 1 }, { text: "Output Open or Closed", b: 1 },
  { text: "Output Grade A, B, C or D from a mark", b: 2 }, { text: "Choose a postage price from four weight bands", b: 2 },
  { text: "Turn a menu number 1 to 4 into an option name", b: 3 }, { text: "Turn day number 1 to 7 into the day name", b: 3 }],
  done: "One test: IF. Two routes: IF ELSE. Ranges with 3+ outcomes: nested IF. One variable against fixed values: CASE." });
Lib.order($("#o1"), { prompt: "Put this program in order.", items: ["INPUT Age", "IF Age >= 18", "THEN OUTPUT \"Adult\"", "ELSE OUTPUT \"Child\"", "ENDIF"], done: "Input, test, THEN branch, ELSE branch, ENDIF." });
Lib.calc($("#c1"), { qs: [
  { q: "IF Mark >= 50 THEN OUTPUT \"Pass\" ELSE OUTPUT \"Fail\" ENDIF. Mark is 50. What is output?", t: ["PASS", '"PASS"'], ph: "word", sol: "50 >= 50 is TRUE, so Pass." },
  { q: "The same code, with Mark 49. What is output?", t: ["FAIL", '"FAIL"'], ph: "word", sol: "49 >= 50 is FALSE, so Fail." },
  { q: "Grade code: &gt;= 70 gives A, otherwise &gt;= 50 gives B, otherwise C. Mark is 70. Which letter is output?", t: ["A", '"A"', "GRADEA"], ph: "letter", sol: "70 >= 70 is TRUE, so A." },
  { q: "The same code with Mark 69. Which letter is output?", t: ["B", '"B"', "GRADEB"], ph: "letter", sol: "69 >= 70 is FALSE. 69 >= 50 is TRUE: B." },
  { q: "A CASE OF has cases 1, 2 and 3 and OTHERWISE. Choice is 7. Which part runs?", t: ["OTHERWISE"], ph: "word", sol: "7 matches no case, so OTHERWISE runs." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a condition?", opts: ["Something that is TRUE or FALSE", "A loop", "A variable name", "A type of output"], a: 0, why: "Selection runs different lines depending on whether it is TRUE or FALSE." },
  { q: "How many branches of an IF ... ELSE run each time?", opts: ["Exactly one", "Both", "None", "It depends on the program length"], a: 0, why: "Either the THEN part or the ELSE part, never both." },
  { q: "In a nested IF, which test should come first?", opts: ["The most specific (hardest) one", "The easiest one", "It does not matter", "The ELSE"], a: 0, why: "The first TRUE test wins, so a wide test first can hide the others." },
  { q: "Which keyword ends an IF statement in pseudocode?", opts: ["ENDIF", "NEXT", "ENDCASE", "UNTIL"], a: 0, why: "IF ... ENDIF." },
  { q: "In Python, how is the end of an IF block shown?", opts: ["By indentation", "By ENDIF", "By a semicolon", "By NEXT"], a: 0, why: "Python uses indentation and a colon." }] });
Lib.cards($("#fc1"), { cards: [
  ["Selection", "Choosing which lines of a program to run, based on a condition."],
  ["Condition", "A test that is either TRUE or FALSE, such as Mark >= 50."],
  ["IF ... THEN ... ENDIF", "Runs lines only when the condition is TRUE."],
  ["ELSE", "The lines run when the IF condition is FALSE."],
  ["Nested IF", "An IF inside another IF, used for three or more outcomes."],
  ["CASE OF", "Compares one variable with several fixed values and runs the matching line."],
  ["OTHERWISE", "The part of a CASE OF that runs when no value matches."],
  ["Comparison operator", "A symbol such as =, <>, <, >, <= or >= that compares two values."]] });

