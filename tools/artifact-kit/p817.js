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

const CH_PS = ["INPUT Cents", "Coins50 ← DIV(Cents, 50)", "Left ← MOD(Cents, 50)", "Coins10 ← DIV(Left, 10)", "Left ← MOD(Left, 10)", "OUTPUT Coins50, Coins10, Left"], CH_PY = ["cents = int(input())", "coins50 = cents // 50", "left = cents % 50", "coins10 = left // 10", "left = left % 10", "print(coins50, coins10, left)"], AV_PS = ["INPUT Total", "INPUT Number", "Average ← Total / Number", "Rounded ← ROUND(Average, 2)", "OUTPUT Rounded"], AV_PY = ["total = float(input())", "number = int(input())", "average = total / number", "rounded = round(average, 2)", "print(rounded)"], DI_PS = ["Sixes ← 0", "FOR Throw ← 1 TO 4", "    Dice ← ROUND(RANDOM() * 5, 0) + 1", "    OUTPUT Dice", "    IF Dice = 6", "      THEN", "        Sixes ← Sixes + 1", "    ENDIF", "NEXT Throw", "OUTPUT \"Sixes: \", Sixes"], DI_PY = ["import random", "sixes = 0", "for throw in range(1, 5):", "    dice = random.randint(1, 6)", "    print(dice)", "    if dice == 6:", "        sixes = sixes + 1", "print(\"Sixes:\", sixes)"];
tr($("#aC"), { label: "DIV and MOD", title: "Giving change", pseudo: CH_PS, py: CH_PY, frames: [{"cap": "A machine gives change using as few coins as possible. The change is 185 cents.", "ps": [0], "py": [], "vars": [["Cents", null], ["Coins50", null], ["Coins10", null], ["Left", null]], "hl": [], "out": [], "inp": [185]}, {"cap": "<b>INPUT Cents</b>: 185.", "ps": [0], "py": [0], "vars": [["Cents", 185], ["Coins50", null], ["Coins10", null], ["Left", null]], "hl": ["Cents"], "out": [], "inp": []}, {"cap": "<b>DIV(185, 50)</b> = 3. Three 50c coins fit (150).", "ps": [1], "py": [1], "vars": [["Cents", 185], ["Coins50", 3], ["Coins10", null], ["Left", null]], "hl": ["Coins50"], "out": [], "note": "DIV(185, 50) = 3", "nc": "t4"}, {"cap": "<b>MOD(185, 50)</b> = 35. This is what is <b>left over</b>.", "ps": [2], "py": [2], "vars": [["Cents", 185], ["Coins50", 3], ["Coins10", null], ["Left", 35]], "hl": ["Left"], "out": [], "note": "MOD(185, 50) = 35", "nc": "t4"}, {"cap": "<b>DIV(35, 10)</b> = 3 ten-cent coins.", "ps": [3], "py": [3], "vars": [["Cents", 185], ["Coins50", 3], ["Coins10", 3], ["Left", 35]], "hl": ["Coins10"], "out": [], "note": "DIV(35, 10) = 3", "nc": "t4"}, {"cap": "<b>MOD(35, 10)</b> = 5 cents remain.", "ps": [4], "py": [4], "vars": [["Cents", 185], ["Coins50", 3], ["Coins10", 3], ["Left", 5]], "hl": ["Left"], "out": [], "note": "MOD(35, 10) = 5", "nc": "t4"}, {"cap": "<b>OUTPUT</b>: 3 fifties, 3 tens and 5 cents. 150 + 30 + 5 = 185.", "ps": [5], "py": [5], "vars": [["Cents", 185], ["Coins50", 3], ["Coins10", 3], ["Left", 5]], "hl": [], "out": ["3 3 5"]}] });
tr($("#aA"), { label: "ROUND", title: "Rounding an average", pseudo: AV_PS, py: AV_PY, frames: [{"cap": "Work out an average and show it neatly. The user types 200, then 7.", "ps": [0], "py": [], "vars": [["Total", null], ["Number", null], ["Average", null], ["Rounded", null]], "hl": [], "out": [], "inp": [200, 7]}, {"cap": "<b>INPUT Total</b>: 200.", "ps": [0], "py": [0], "vars": [["Total", 200], ["Number", null], ["Average", null], ["Rounded", null]], "hl": ["Total"], "out": [], "inp": [7]}, {"cap": "<b>INPUT Number</b>: 7.", "ps": [1], "py": [1], "vars": [["Total", 200], ["Number", 7], ["Average", null], ["Rounded", null]], "hl": ["Number"], "out": [], "inp": []}, {"cap": "<b>200 / 7</b> gives a long decimal.", "ps": [2], "py": [2], "vars": [["Total", 200], ["Number", 7], ["Average", 28.57143], ["Rounded", null]], "hl": ["Average"], "out": []}, {"cap": "<b>ROUND(Average, 2)</b> keeps <b>2 decimal places</b>. The third decimal is 1, so it rounds down to 28.57.", "ps": [3], "py": [3], "vars": [["Total", 200], ["Number", 7], ["Average", 28.57143], ["Rounded", 28.57]], "hl": ["Rounded"], "out": []}, {"cap": "<b>OUTPUT Rounded</b>. Average itself has not changed.", "ps": [4], "py": [4], "vars": [["Total", 200], ["Number", 7], ["Average", 28.57143], ["Rounded", 28.57]], "hl": [], "out": ["28.57"]}] });
tr($("#aD"), { label: "RANDOM", title: "Throwing a dice", pseudo: DI_PS, py: DI_PY, frames: [{"cap": "<b>Sixes ← 0</b>. A dice is thrown 4 times. The random values here are examples: a real run gives different ones.", "ps": [0], "py": [1], "vars": [["Throw", null], ["Dice", null], ["Sixes", 0]], "hl": ["Sixes"], "out": []}, {"cap": "<b>RANDOM()</b> gives 0.62. 0.62 × 5 = 3.10, ROUND to 0 places = 3, then + 1 = <b>4</b>.", "ps": [1, 2], "py": [2, 3], "vars": [["Throw", 1], ["Dice", 4], ["Sixes", 0]], "hl": ["Throw", "Dice"], "out": [], "note": "ROUND(0.62 * 5, 0) + 1 = 4", "nc": "t4"}, {"cap": "OUTPUT 4. Is Dice = 6?", "ps": [3, 4], "py": [4, 5], "vars": [["Throw", 1], ["Dice", 4], ["Sixes", 0]], "hl": [], "out": ["4"], "cond": ["4 = 6", false]}, {"cap": "<b>RANDOM()</b> gives 0.97. 0.97 × 5 = 4.85, ROUND to 0 places = 5, then + 1 = <b>6</b>.", "ps": [1, 2], "py": [2, 3], "vars": [["Throw", 2], ["Dice", 6], ["Sixes", 0]], "hl": ["Throw", "Dice"], "out": ["4"], "note": "ROUND(0.97 * 5, 0) + 1 = 6", "nc": "t4"}, {"cap": "OUTPUT 6. Is Dice = 6?", "ps": [3, 4], "py": [4, 5], "vars": [["Throw", 2], ["Dice", 6], ["Sixes", 0]], "hl": [], "out": ["4", "6"], "cond": ["6 = 6", true]}, {"cap": "TRUE, so <b>Sixes ← 1</b>.", "ps": [6], "py": [6], "vars": [["Throw", 2], ["Dice", 6], ["Sixes", 1]], "hl": ["Sixes"], "out": ["4", "6"]}, {"cap": "<b>RANDOM()</b> gives 0.08. 0.08 × 5 = 0.40, ROUND to 0 places = 0, then + 1 = <b>1</b>.", "ps": [1, 2], "py": [2, 3], "vars": [["Throw", 3], ["Dice", 1], ["Sixes", 1]], "hl": ["Throw", "Dice"], "out": ["4", "6"], "note": "ROUND(0.08 * 5, 0) + 1 = 1", "nc": "t4"}, {"cap": "OUTPUT 1. Is Dice = 6?", "ps": [3, 4], "py": [4, 5], "vars": [["Throw", 3], ["Dice", 1], ["Sixes", 1]], "hl": [], "out": ["4", "6", "1"], "cond": ["1 = 6", false]}, {"cap": "<b>RANDOM()</b> gives 0.93. 0.93 × 5 = 4.65, ROUND to 0 places = 5, then + 1 = <b>6</b>.", "ps": [1, 2], "py": [2, 3], "vars": [["Throw", 4], ["Dice", 6], ["Sixes", 1]], "hl": ["Throw", "Dice"], "out": ["4", "6", "1"], "note": "ROUND(0.93 * 5, 0) + 1 = 6", "nc": "t4"}, {"cap": "OUTPUT 6. Is Dice = 6?", "ps": [3, 4], "py": [4, 5], "vars": [["Throw", 4], ["Dice", 6], ["Sixes", 1]], "hl": [], "out": ["4", "6", "1", "6"], "cond": ["6 = 6", true]}, {"cap": "TRUE, so <b>Sixes ← 2</b>.", "ps": [6], "py": [6], "vars": [["Throw", 4], ["Dice", 6], ["Sixes", 2]], "hl": ["Sixes"], "out": ["4", "6", "1", "6"]}, {"cap": "After the loop, output the count: <b>2</b>.", "ps": [9], "py": [7], "vars": [["Throw", 4], ["Dice", 6], ["Sixes", 2]], "hl": [], "out": ["4", "6", "1", "6", "Sixes: 2"]}] });
Lib.codePanel($("#cdR"), { pseudo: ["OUTPUT ROUND(3.14159, 2)    // 3.14", "OUTPUT ROUND(3.14159, 3)    // 3.142", "OUTPUT ROUND(9.7, 0)        // 10"], py: ["print(round(3.14159, 2))    # 3.14", "print(round(3.14159, 3))    # 3.142", "print(round(9.7))           # 10"] });
Lib.codePanel($("#cdD"), { pseudo: ["Dice ← ROUND(RANDOM() * 5, 0) + 1", "OUTPUT Dice"], py: ["import random", "dice = random.randint(1, 6)", "print(dice)"] });


/* ---------- Lab 1 ---------- */
(() => {
  let a, b;
  const upd = () => { if (!a || !b) return; const n = a.get(), s = b.get(), q = Math.floor(n / s), m = n % s;
    $("#ld").textContent = q; $("#lm").textContent = m;
    const box = (k, full) => `<span style="display:inline-block;border:2px ${full ? "solid var(--good)" : "dashed var(--warn)"};border-radius:8px;padding:2px 6px;margin:0 6px 6px 0;letter-spacing:2px">${"●".repeat(k)}</span>`;
    $("#boxes").innerHTML = Array(q).fill(box(s, true)).join("") + (m ? box(m, false) : "");
    $("#lv").innerHTML = `${n} items in boxes of ${s}: <b>DIV(${n}, ${s}) = ${q}</b> full boxes and <b>MOD(${n}, ${s}) = ${m}</b> left over. Check: ${q} × ${s} + ${m} = ${n}.`; };
  a = Lib.slider($("#s1"), { id: "dn", label: "Items ", min: 0, max: 60, value: 29, onInput: upd });
  b = Lib.slider($("#s2"), { id: "ds", label: "Items per box ", min: 2, max: 12, value: 4, onInput: upd });
  upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  let a, b;
  const upd = () => { if (!a || !b) return; const v = a.get(), p = b.get(), k = 10 ** (4 - p), out = (Math.floor(v / k + 0.5) / 10 ** p).toFixed(p), val = (v / 10000).toFixed(4), digit = p < 4 ? Math.floor(v / (k / 10)) % 10 : null;
    $("#rv0").textContent = val; $("#rv1").textContent = out;
    $("#rv2").innerHTML = `<b>ROUND(${val}, ${p})</b> = ${out}. ` + (digit === null ? "There are no digits to remove." : `The first digit removed is ${digit}, so it rounds <b>${digit >= 5 ? "up" : "down"}</b>.`); };
  a = Lib.slider($("#s3"), { id: "rn", label: "Value ", min: 0, max: 200000, value: 74682, fmt: (v) => (v / 10000).toFixed(4), onInput: upd });
  b = Lib.slider($("#s4"), { id: "rp", label: "Decimal places ", min: 0, max: 4, value: 2, onInput: upd });
  upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  let a, b;
  const range = () => { const lo = a.get(), hi = lo + b.get(); return [lo, hi]; };
  const upd = () => { if (!a || !b) return; const [lo, hi] = range();
    Lib.codePanel($("#xcode"), { pseudo: [`Number ← ROUND(RANDOM() * ${hi - lo}, 0) + ${lo}`], py: ["import random", `number = random.randint(${lo}, ${hi})`] });
    $("#xv").innerHTML = `Range: <b>${lo} to ${hi}</b>.`; $("#bars").innerHTML = ""; };
  const one = () => { const [lo, hi] = range(); return Math.round(Math.random() * (hi - lo)) + lo; };
  a = Lib.slider($("#s5"), { id: "xl", label: "Lowest value ", min: 0, max: 20, value: 1, onInput: upd });
  b = Lib.slider($("#s6"), { id: "xs", label: "Size of range (highest − lowest) ", min: 1, max: 10, value: 5, onInput: upd });
  $("#roll1").onclick = () => { $("#xv").innerHTML = `Number = <b>${one()}</b>`; $("#bars").innerHTML = ""; };
  $("#roll600").onclick = () => { const [lo, hi] = range(), n = {}; for (let i = 0; i < 600; i++) { const x = one(); n[x] = (n[x] || 0) + 1; } const top = Math.max(...Object.values(n));
    $("#bars").innerHTML = Array.from({ length: hi - lo + 1 }, (_, i) => { const c = n[lo + i] || 0; return `<div style="display:flex;align-items:center;gap:8px;margin:3px 0;font-family:var(--mono);font-size:.85rem"><span style="width:2.5em;text-align:right">${lo + i}</span><span style="height:14px;border-radius:4px;background:var(--accent);width:${(c / top) * 70}%"></span><span>${c}</span></div>`; }).join("");
    $("#xv").innerHTML = `600 rolls, all between <b>${lo}</b> and <b>${hi}</b>. The two end values appear about half as often.`; };
  upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which routine does each job need?", buckets: [{ label: "DIV" }, { label: "MOD" }, { label: "ROUND" }, { label: "RANDOM" }], items: [
  { text: "How many whole weeks in a number of days", b: 0 }, { text: "Number of full teams of 5", b: 0 },
  { text: "Test whether a number is odd", b: 1 }, { text: "Get the last digit of a number", b: 1 },
  { text: "Show a price with 2 decimal places", b: 2 }, { text: "Give a measurement to the nearest whole number", b: 2 },
  { text: "Shuffle which question appears next", b: 3 }, { text: "Simulate tossing a coin", b: 3 }],
  done: "DIV: whole times. MOD: remainder. ROUND: decimal places. RANDOM: unpredictable." });
Lib.match($("#m1"), { prompt: "Drag each result to its call.", pairs: [["DIV(38, 5)", "7"], ["MOD(38, 5)", "3"], ["ROUND(38.456, 1)", "38.5"], ["ROUND(38.456, 0)", "38"], ["MOD(40, 5)", "0"]] });
Lib.calc($("#c1"), { qs: [
  { q: "DIV(100, 7)", a: 14, sol: "7 × 14 = 98, so 14 whole times." },
  { q: "MOD(100, 7)", a: 2, sol: "100 − 98 = 2." },
  { q: "MOD(3, 10)", a: 3, sol: "10 goes into 3 zero times, so 3 is left." },
  { q: "ROUND(46.2951, 2)", a: 46.3, tol: 0.001, sol: "The third decimal is 5, so 46.29 rounds up to 46.30." },
  { q: "DIV(MOD(257, 100), 10)", a: 5, sol: "MOD(257, 100) = 57, then DIV(57, 10) = 5." },
  { q: "Largest value of ROUND(RANDOM() * 8, 0) + 2", a: 10, sol: "RANDOM() up to 1: 8 + 2 = 10." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does RANDOM() return?", opts: ["A number between 0 and 1", "A whole number between 1 and 10", "The remainder of a division", "A number rounded to 2 places"], a: 0, why: "Stretch and round it to get other ranges." },
  { q: "What is the 2 in ROUND(X, 2)?", opts: ["The number of decimal places", "The number to divide by", "The number of digits in total", "The number of times to round"], a: 0, why: "ROUND(value, places)." },
  { q: "Which expression is TRUE when N is a multiple of 3?", opts: ["MOD(N, 3) = 0", "DIV(N, 3) = 0", "MOD(3, N) = 0", "ROUND(N, 3) = 0"], a: 0, why: "No remainder means it divides exactly." },
  { q: "Why use a library routine?", opts: ["It is already written and tested", "It makes variables global", "It removes the need to call it", "It stops all run-time errors"], a: 0, why: "Saves time and reduces errors." },
  { q: "Which gives a whole number from 5 to 15?", opts: ["ROUND(RANDOM() * 10, 0) + 5", "ROUND(RANDOM() * 15, 0) + 5", "ROUND(RANDOM() * 5, 0) + 15", "RANDOM() * 10 + 5"], a: 0, why: "Range size 10, starting at 5." }] });
Lib.cards($("#fc1"), { cards: [
  ["Library routine", "A pre-written, tested procedure or function you can call."],
  ["DIV", "Returns the whole number part of a division."],
  ["MOD", "Returns the remainder of a division."],
  ["ROUND", "Rounds a value to a given number of decimal places."],
  ["RANDOM", "Returns a random number between 0 and 1."]] });

