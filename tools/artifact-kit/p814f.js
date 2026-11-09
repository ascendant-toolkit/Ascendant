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

const PR_PS = ["Result ← (4 + 2) * 3 ^ 2", "OUTPUT Result"], PR_PY = ["result = (4 + 2) * 3 ** 2", "print(result)"];
const DM_PS = ["INPUT Minutes", "Hours ← Minutes DIV 60", "Remainder ← Minutes MOD 60", "OUTPUT Hours, \" h \", Remainder, \" min\""], DM_PY = ["minutes = int(input())", "hours = minutes // 60", "remainder = minutes % 60", "print(hours, \"h\", remainder, \"min\")"];
const LG_PS = ["INPUT Age", "INPUT Height", "IF Age >= 8 AND Height >= 120", "  THEN", "    OUTPUT \"Allowed\"", "  ELSE", "    OUTPUT \"Not allowed\"", "ENDIF"], LG_PY = ["age = int(input())", "height = int(input())", "if age >= 8 and height >= 120:", "    print(\"Allowed\")", "else:", "    print(\"Not allowed\")"];
tr($("#aP"), { label: "Order of operations", title: "Order of operations", pseudo: PR_PS, py: PR_PY, dwell: 2300, frames: [{"cap": "Brackets, then powers, then * and /, then + and -. The expression is <b>(4 + 2) * 3 ^ 2</b>.", "ps": [0], "py": [0], "vars": [["Result", null]], "hl": [], "out": [], "note": "(4 + 2) * 3 ^ 2", "nc": "t4"}, {"cap": "<b>1. Brackets first:</b> 4 + 2 = 6.", "ps": [0], "py": [0], "vars": [["Result", null]], "hl": [], "out": [], "note": "6 * 3 ^ 2", "nc": "t4"}, {"cap": "<b>2. Power next:</b> 3 ^ 2 = 9. The power binds tighter than *.", "ps": [0], "py": [0], "vars": [["Result", null]], "hl": [], "out": [], "note": "6 * 9", "nc": "t4"}, {"cap": "<b>3. Multiply:</b> 6 * 9 = 54. It is stored in Result.", "ps": [0], "py": [0], "vars": [["Result", 54]], "hl": ["Result"], "out": [], "note": "54", "nc": "t3"}, {"cap": "<b>OUTPUT Result</b>: 54. Without the brackets the answer would have been 4 + 2 * 9 = 22.", "ps": [1], "py": [1], "vars": [["Result", 54]], "hl": ["Result"], "out": ["54"]}] });
tr($("#aD"), { label: "DIV and MOD", title: "Minutes to hours and minutes", pseudo: DM_PS, py: DM_PY, dwell: 2300, frames: [{"cap": "Convert minutes into hours and minutes. The user will type 135.", "ps": [0], "py": [], "vars": [["Minutes", null], ["Hours", null], ["Remainder", null]], "hl": [], "out": [], "inp": [135]}, {"cap": "<b>INPUT Minutes</b>: 135.", "ps": [0], "py": [0], "vars": [["Minutes", 135], ["Hours", null], ["Remainder", null]], "hl": ["Minutes"], "out": [], "inp": []}, {"cap": "<b>135 DIV 60</b> = 2. DIV gives the <b>whole number</b> of times 60 goes into 135 (2 × 60 = 120).", "ps": [1], "py": [1], "vars": [["Minutes", 135], ["Hours", 2], ["Remainder", null]], "hl": ["Hours"], "out": [], "note": "135 DIV 60 = 2", "nc": "t4"}, {"cap": "<b>135 MOD 60</b> = 15. MOD gives the <b>remainder</b>: 135 − 120 = 15.", "ps": [2], "py": [2], "vars": [["Minutes", 135], ["Hours", 2], ["Remainder", 15]], "hl": ["Remainder"], "out": [], "note": "135 MOD 60 = 15", "nc": "t4"}, {"cap": "<b>OUTPUT</b> joins the pieces: 2 h 15 min. DIV and MOD together split a quantity into units.", "ps": [3], "py": [3], "vars": [["Minutes", 135], ["Hours", 2], ["Remainder", 15]], "hl": [], "out": ["2 h 15 min"]}] });
tr($("#aL"), { label: "AND in a condition", title: "Ride check", pseudo: LG_PS, py: LG_PY, dwell: 2300, frames: [{"cap": "A ride needs age 8 or over <b>and</b> height 120 or over. The user types 10, then 115.", "ps": [0], "py": [], "vars": [["Age", null], ["Height", null]], "hl": [], "out": [], "inp": [10, 115]}, {"cap": "<b>INPUT Age</b>: 10.", "ps": [0], "py": [0], "vars": [["Age", 10], ["Height", null]], "hl": ["Age"], "out": [], "inp": [115]}, {"cap": "<b>INPUT Height</b>: 115.", "ps": [1], "py": [1], "vars": [["Age", 10], ["Height", 115]], "hl": ["Height"], "out": [], "inp": []}, {"cap": "Left side of AND: is 10 >= 8?", "ps": [2], "py": [2], "vars": [["Age", 10], ["Height", 115]], "hl": [], "out": [], "cond": ["10 >= 8", true]}, {"cap": "Right side of AND: is 115 >= 120?", "ps": [2], "py": [2], "vars": [["Age", 10], ["Height", 115]], "hl": [], "out": [], "cond": ["115 >= 120", false]}, {"cap": "<b>AND</b> needs <b>both</b> sides TRUE. TRUE AND FALSE is FALSE.", "ps": [2], "py": [2], "vars": [["Age", 10], ["Height", 115]], "hl": [], "out": [], "cond": ["TRUE AND FALSE", false]}, {"cap": "FALSE, so the ELSE branch runs. If it had been <b>OR</b>, TRUE OR FALSE would be TRUE and the rider would be allowed.", "ps": [5, 6], "py": [4, 5], "vars": [["Age", 10], ["Height", 115]], "hl": [], "out": ["Not allowed"], "cond": ["TRUE AND FALSE", false]}] });
Lib.codePanel($("#cdPr"), { pseudo: PR_PS, py: PR_PY });
Lib.codePanel($("#cdLg"), { pseudo: LG_PS, py: LG_PY });


/* ---------- Lab 1 ---------- */
(() => {
  let a, b;
  const upd = () => {
    if (!a || !b) return; const x = a.get(), y = b.get(), d = Math.floor(x / y), m = x % y;
    $("#at").innerHTML = `<tr><th>Pseudocode</th><th>Python</th><th>Result</th></tr><tr><td>A + B</td><td>a + b</td><td>${x + y}</td></tr><tr><td>A - B</td><td>a - b</td><td>${x - y}</td></tr><tr><td>A * B</td><td>a * b</td><td>${x * y}</td></tr><tr><td>A / B</td><td>a / b</td><td>${fmtN(x / y, 3)}</td></tr><tr><td>A ^ 2</td><td>a ** 2</td><td>${x * x}</td></tr><tr><td>A DIV B</td><td>a // b</td><td>${d}</td></tr><tr><td>A MOD B</td><td>a % b</td><td>${m}</td></tr>`;
    $("#av").innerHTML = `${x} ÷ ${y} is <b>${d} remainder ${m}</b>: ${x} DIV ${y} = ${d} and ${x} MOD ${y} = ${m}. Check: ${d} × ${y} + ${m} = ${d * y + m}.${m === 0 ? ` MOD is 0, so ${y} divides ${x} exactly.` : ""}`;
  };
  a = Lib.slider($("#s1"), { id: "oa", label: "A ", min: 0, max: 30, value: 17, onInput: upd });
  b = Lib.slider($("#s2"), { id: "ob", label: "B ", min: 1, max: 10, value: 5, onInput: upd });
  upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  let a, h; const sel = $("#lo");
  const upd = () => {
    if (!a || !h) return; const ag = a.get(), ht = h.get(), p = ag >= 8, q = ht >= 120, o = sel.value;
    const T = (v) => (v ? "TRUE" : "FALSE"), r = o === "AND" ? p && q : o === "OR" ? p || q : !p;
    $("#lt").innerHTML = `<tr><th>Part</th><th>Value</th></tr><tr><td>Age >= 8  (${ag} >= 8)</td><td>${T(p)}</td></tr>` + (o === "NOT" ? "" : `<tr><td>Height >= 120  (${ht} >= 120)</td><td>${T(q)}</td></tr>`) + `<tr><td><b>${o === "NOT" ? "NOT (Age >= 8)" : "Age >= 8 " + o + " Height >= 120"}</b></td><td><b>${T(r)}</b></td></tr>`;
    $("#lv").innerHTML = o === "AND" ? (r ? "Both tests are TRUE, so AND is TRUE." : `AND needs <b>both</b> TRUE. ${!p && !q ? "Neither is" : !p ? "Age is not" : "Height is not"} TRUE.`) : o === "OR" ? (r ? "At least one test is TRUE, so OR is TRUE." : "Neither test is TRUE, so OR is FALSE.") : `NOT reverses ${T(p)} to ${T(!p)}.`;
  };
  a = Lib.slider($("#s3"), { id: "la", label: "Age ", min: 0, max: 30, value: 10, onInput: upd });
  h = Lib.slider($("#s4"), { id: "lh", label: "Height (cm) ", min: 80, max: 200, value: 115, onInput: upd });
  sel.onchange = upd; upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  const E = [["12 - 2 * 3", "12 - 6", 6, "* happens before -."], ["(12 - 2) * 3", "10 * 3", 30, "The brackets make the subtraction happen first."], ["2 + 3 ^ 2", "2 + 9", 11, "^ happens before +."], ["(2 + 3) ^ 2", "5 ^ 2", 25, "Brackets first, then the power."], ["20 / 4 + 1", "5 + 1", 6, "/ happens before +."], ["20 / (4 + 1)", "20 / 5", 4, "Brackets first."]];
  const sel = $("#pe"); sel.innerHTML = E.map((e, i) => `<option value="${i}">${e[0]}</option>`).join("");
  const upd = () => { const e = E[+sel.value]; $("#pout").innerHTML = `${esc(e[0])} &nbsp;→&nbsp; ${esc(e[1])} &nbsp;→&nbsp; <b>${e[2]}</b>`; $("#pv").textContent = e[3]; };
  sel.onchange = upd; upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Sort each operator into its type.", buckets: [{ label: "Arithmetic" }, { label: "Comparison" }, { label: "Logical" }], items: [
  { text: "+", b: 0 }, { text: "*", b: 0 }, { text: "^", b: 0 }, { text: "DIV", b: 0 }, { text: "MOD", b: 0 },
  { text: "=", b: 1 }, { text: "<>", b: 1 }, { text: ">=", b: 1 }, { text: "<", b: 1 },
  { text: "AND", b: 2 }, { text: "OR", b: 2 }, { text: "NOT", b: 2 }],
  done: "Arithmetic calculates, comparison gives TRUE/FALSE, logical combines TRUE/FALSE." });
Lib.match($("#m1"), { prompt: "Match each operator to what it does.", pairs: [
  ["MOD", "Remainder after division"], ["DIV", "Whole number of times it divides"], ["^", "To the power of"], ["<>", "Not equal to"], ["AND", "TRUE only if both sides are TRUE"], ["OR", "TRUE if at least one side is TRUE"]],
  done: "MOD is the remainder, DIV is the whole number." });
Lib.calc($("#c1"), { qs: [
  { q: "What is 17 DIV 5?", a: 3, sol: "5 goes into 17 three times (15)." },
  { q: "What is 17 MOD 5?", a: 2, sol: "17 − 15 = 2." },
  { q: "What is 2 ^ 5?", a: 32, sol: "2 × 2 × 2 × 2 × 2 = 32." },
  { q: "What is 3 + 4 * 2?", a: 11, sol: "4 * 2 = 8 first, then 3 + 8 = 11." },
  { q: "What is (3 + 4) * 2?", a: 14, sol: "Brackets first: 7 * 2 = 14." },
  { q: "What is 100 DIV 60? (Whole hours in 100 minutes.)", a: 1, sol: "60 goes into 100 once." },
  { q: "What is NOT (5 > 3)? Type TRUE or FALSE.", t: ["FALSE"], ph: "TRUE or FALSE", sol: "5 > 3 is TRUE. NOT reverses it to FALSE." },
  { q: "Age is 15. Is Age >= 13 AND Age <= 19 TRUE or FALSE?", t: ["TRUE"], ph: "TRUE or FALSE", sol: "Both parts are TRUE, so AND is TRUE." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which expression is TRUE when X is even?", opts: ["X MOD 2 = 0", "X DIV 2 = 0", "X ^ 2 = 0", "X / 2 = 1"], a: 0, why: "An even number has no remainder when divided by 2." },
  { q: "What is 7 + 3 * 2?", opts: ["13", "20", "16", "12"], a: 0, why: "Multiply first: 6, then add 7." },
  { q: "TRUE AND FALSE is...", opts: ["FALSE", "TRUE", "0", "an error"], a: 0, why: "AND needs both sides TRUE." },
  { q: "TRUE OR FALSE is...", opts: ["TRUE", "FALSE", "0", "an error"], a: 0, why: "OR needs at least one TRUE." },
  { q: "Which operator gives the remainder of a division?", opts: ["MOD", "DIV", "^", "/"], a: 0, why: "MOD gives the remainder." }] });
Lib.cards($("#fc1"), { cards: [
  ["Operator", "A symbol or word that does something to values."],
  ["Arithmetic operator", "Calculates: + - * / ^ DIV MOD."],
  ["Comparison operator", "Compares two values and gives TRUE or FALSE: = <> < > <= >=."],
  ["Logical operator", "Combines TRUE/FALSE values: AND, OR, NOT."],
  ["DIV", "Division that gives only the whole number part (17 DIV 5 = 3)."],
  ["MOD", "Gives the remainder of a division (17 MOD 5 = 2)."],
  ["^", "The power operator: 2 ^ 3 = 8."],
  ["Boolean", "A data type with only two values: TRUE and FALSE."]] });

