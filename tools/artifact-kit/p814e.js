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

const FN_PS = ["Word ← \"Computer\"", "OUTPUT LENGTH(Word)", "OUTPUT UCASE(Word)", "OUTPUT SUBSTRING(Word, 4, 3)", "OUTPUT Word & \"s\""], FN_PY = ["word = \"Computer\"", "print(len(word))", "print(word.upper())", "print(word[3:6])", "print(word + \"s\")"];
const CT_PS = ["Word ← \"elephant\"", "Count ← 0", "FOR Index ← 1 TO LENGTH(Word)", "    Letter ← SUBSTRING(Word, Index, 1)", "    IF Letter = \"e\"", "      THEN", "        Count ← Count + 1", "    ENDIF", "NEXT Index", "OUTPUT Count"], CT_PY = ["word = \"elephant\"", "count = 0", "for index in range(1, len(word) + 1):", "    letter = word[index - 1]", "    if letter == \"e\":", "        count = count + 1", "print(count)"];
const RV_PS = ["Word ← \"STAR\"", "Reverse ← \"\"", "FOR Index ← 1 TO LENGTH(Word)", "    Reverse ← SUBSTRING(Word, Index, 1) & Reverse", "NEXT Index", "OUTPUT Reverse"], RV_PY = ["word = \"STAR\"", "reverse = \"\"", "for index in range(1, len(word) + 1):", "    reverse = word[index - 1] + reverse", "print(reverse)"];
tr($("#aF"), { label: "String functions", title: "String functions", pseudo: FN_PS, py: FN_PY, dwell: 2400, frames: [{"cap": "<b>Word ← \"Computer\"</b>. A string is a row of characters. In pseudocode the first character is <b>position 1</b>.", "ps": [0], "py": [0], "vars": [["Word", "Computer"]], "hl": ["Word"], "out": [], "cells": ["C", "o", "m", "p", "u", "t", "e", "r"]}, {"cap": "<b>LENGTH(Word)</b> counts every character: <b>8</b>.", "ps": [1], "py": [1], "vars": [["Word", "Computer"]], "hl": [], "out": ["8"], "cells": ["C", "o", "m", "p", "u", "t", "e", "r"], "cc": {"0": "cur", "1": "cur", "2": "cur", "3": "cur", "4": "cur", "5": "cur", "6": "cur", "7": "cur"}}, {"cap": "<b>UCASE(Word)</b> gives the whole string in capitals. Word itself is not changed.", "ps": [2], "py": [2], "vars": [["Word", "Computer"]], "hl": [], "out": ["8", "COMPUTER"], "cells": ["C", "o", "m", "p", "u", "t", "e", "r"], "cc": {"0": "cur", "1": "cur", "2": "cur", "3": "cur", "4": "cur", "5": "cur", "6": "cur", "7": "cur"}}, {"cap": "<b>SUBSTRING(Word, 4, 3)</b>: start at position <b>4</b> and take <b>3</b> characters: p, u, t.", "ps": [3], "py": [3], "vars": [["Word", "Computer"]], "hl": [], "out": ["8", "COMPUTER", "put"], "cells": ["C", "o", "m", "p", "u", "t", "e", "r"], "cc": {"3": "cur", "4": "cur", "5": "cur"}}, {"cap": "<b>&amp;</b> joins two strings together (<span class=\"kw\">concatenation</span>): \"Computer\" & \"s\".", "ps": [4], "py": [4], "vars": [["Word", "Computer"]], "hl": [], "out": ["8", "COMPUTER", "put", "Computers"], "cells": ["C", "o", "m", "p", "u", "t", "e", "r", "s"], "cc": {"8": "ok"}}] });
tr($("#aC"), { label: "Counting a letter", title: "Count the letter e", pseudo: CT_PS, py: CT_PY, dwell: 1300, frames: [{"cap": "<b>Count ← 0</b>. The loop will look at each letter from position 1 to LENGTH(Word) = 8.", "ps": [0, 1], "py": [0, 1], "vars": [["Index", null], ["Letter", null], ["Count", 0]], "hl": ["Count"], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"]}, {"cap": "Index 1. <b>Letter ← SUBSTRING(Word, 1, 1)</b> takes one character: \"e\".", "ps": [2, 3], "py": [2, 3], "vars": [["Index", 1], ["Letter", "e"], ["Count", 0]], "hl": ["Index", "Letter"], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "cur"}}, {"cap": "Is \"e\" = \"e\"?", "ps": [4], "py": [4], "vars": [["Index", 1], ["Letter", "e"], ["Count", 0]], "hl": [], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "cur"}, "cond": ["\"e\" = \"e\"", true]}, {"cap": "TRUE, so <b>Count ← Count + 1</b> = <b>1</b>.", "ps": [6], "py": [5], "vars": [["Index", 1], ["Letter", "e"], ["Count", 1]], "hl": ["Count"], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok"}, "cond": ["\"e\" = \"e\"", true]}, {"cap": "Index 2. <b>Letter ← SUBSTRING(Word, 2, 1)</b> takes one character: \"l\".", "ps": [2, 3], "py": [2, 3], "vars": [["Index", 2], ["Letter", "l"], ["Count", 1]], "hl": ["Index", "Letter"], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "1": "cur"}}, {"cap": "Is \"l\" = \"e\"?", "ps": [4], "py": [4], "vars": [["Index", 2], ["Letter", "l"], ["Count", 1]], "hl": [], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "1": "cur"}, "cond": ["\"l\" = \"e\"", false]}, {"cap": "Index 3. <b>Letter ← SUBSTRING(Word, 3, 1)</b> takes one character: \"e\".", "ps": [2, 3], "py": [2, 3], "vars": [["Index", 3], ["Letter", "e"], ["Count", 1]], "hl": ["Index", "Letter"], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "cur"}}, {"cap": "Is \"e\" = \"e\"?", "ps": [4], "py": [4], "vars": [["Index", 3], ["Letter", "e"], ["Count", 1]], "hl": [], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "cur"}, "cond": ["\"e\" = \"e\"", true]}, {"cap": "TRUE, so <b>Count ← Count + 1</b> = <b>2</b>.", "ps": [6], "py": [5], "vars": [["Index", 3], ["Letter", "e"], ["Count", 2]], "hl": ["Count"], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "ok"}, "cond": ["\"e\" = \"e\"", true]}, {"cap": "Index 4. <b>Letter ← SUBSTRING(Word, 4, 1)</b> takes one character: \"p\".", "ps": [2, 3], "py": [2, 3], "vars": [["Index", 4], ["Letter", "p"], ["Count", 2]], "hl": ["Index", "Letter"], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "ok", "3": "cur"}}, {"cap": "Is \"p\" = \"e\"?", "ps": [4], "py": [4], "vars": [["Index", 4], ["Letter", "p"], ["Count", 2]], "hl": [], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "ok", "3": "cur"}, "cond": ["\"p\" = \"e\"", false]}, {"cap": "Index 5. <b>Letter ← SUBSTRING(Word, 5, 1)</b> takes one character: \"h\".", "ps": [2, 3], "py": [2, 3], "vars": [["Index", 5], ["Letter", "h"], ["Count", 2]], "hl": ["Index", "Letter"], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "ok", "4": "cur"}}, {"cap": "Is \"h\" = \"e\"?", "ps": [4], "py": [4], "vars": [["Index", 5], ["Letter", "h"], ["Count", 2]], "hl": [], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "ok", "4": "cur"}, "cond": ["\"h\" = \"e\"", false]}, {"cap": "Index 6. <b>Letter ← SUBSTRING(Word, 6, 1)</b> takes one character: \"a\".", "ps": [2, 3], "py": [2, 3], "vars": [["Index", 6], ["Letter", "a"], ["Count", 2]], "hl": ["Index", "Letter"], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "ok", "5": "cur"}}, {"cap": "Is \"a\" = \"e\"?", "ps": [4], "py": [4], "vars": [["Index", 6], ["Letter", "a"], ["Count", 2]], "hl": [], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "ok", "5": "cur"}, "cond": ["\"a\" = \"e\"", false]}, {"cap": "Index 7. <b>Letter ← SUBSTRING(Word, 7, 1)</b> takes one character: \"n\".", "ps": [2, 3], "py": [2, 3], "vars": [["Index", 7], ["Letter", "n"], ["Count", 2]], "hl": ["Index", "Letter"], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "ok", "6": "cur"}}, {"cap": "Is \"n\" = \"e\"?", "ps": [4], "py": [4], "vars": [["Index", 7], ["Letter", "n"], ["Count", 2]], "hl": [], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "ok", "6": "cur"}, "cond": ["\"n\" = \"e\"", false]}, {"cap": "Index 8. <b>Letter ← SUBSTRING(Word, 8, 1)</b> takes one character: \"t\".", "ps": [2, 3], "py": [2, 3], "vars": [["Index", 8], ["Letter", "t"], ["Count", 2]], "hl": ["Index", "Letter"], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "ok", "7": "cur"}}, {"cap": "Is \"t\" = \"e\"?", "ps": [4], "py": [4], "vars": [["Index", 8], ["Letter", "t"], ["Count", 2]], "hl": [], "out": [], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "ok", "7": "cur"}, "cond": ["\"t\" = \"e\"", false]}, {"cap": "The loop ends. <b>OUTPUT Count</b>: the letter \"e\" appears <b>2</b> times.", "ps": [9], "py": [6], "vars": [["Index", 8], ["Letter", "t"], ["Count", 2]], "hl": ["Count"], "out": ["2"], "cells": ["e", "l", "e", "p", "h", "a", "n", "t"], "cc": {"0": "ok", "2": "ok"}}] });
tr($("#aR"), { label: "Reversing a string", title: "Reverse a string", pseudo: RV_PS, py: RV_PY, dwell: 2000, frames: [{"cap": "<b>Reverse ← \"\"</b>: an empty string to build the answer in.", "ps": [0, 1], "py": [0, 1], "vars": [["Index", null], ["Reverse", ""]], "hl": ["Reverse"], "out": [], "cells": ["S", "T", "A", "R"]}, {"cap": "Index 1: take \"S\" and join it on the <b>front</b> of Reverse. Reverse is now <b>\"S\"</b>.", "ps": [2, 3], "py": [2, 3], "vars": [["Index", 1], ["Reverse", "S"]], "hl": ["Index", "Reverse"], "out": [], "cells": ["S", "T", "A", "R"], "cc": {"0": "cur"}}, {"cap": "Index 2: take \"T\" and join it on the <b>front</b> of Reverse. Reverse is now <b>\"TS\"</b>.", "ps": [2, 3], "py": [2, 3], "vars": [["Index", 2], ["Reverse", "TS"]], "hl": ["Index", "Reverse"], "out": [], "cells": ["S", "T", "A", "R"], "cc": {"1": "cur"}}, {"cap": "Index 3: take \"A\" and join it on the <b>front</b> of Reverse. Reverse is now <b>\"ATS\"</b>.", "ps": [2, 3], "py": [2, 3], "vars": [["Index", 3], ["Reverse", "ATS"]], "hl": ["Index", "Reverse"], "out": [], "cells": ["S", "T", "A", "R"], "cc": {"2": "cur"}}, {"cap": "Index 4: take \"R\" and join it on the <b>front</b> of Reverse. Reverse is now <b>\"RATS\"</b>.", "ps": [2, 3], "py": [2, 3], "vars": [["Index", 4], ["Reverse", "RATS"]], "hl": ["Index", "Reverse"], "out": [], "cells": ["S", "T", "A", "R"], "cc": {"3": "cur"}}, {"cap": "<b>OUTPUT Reverse</b>: RATS. Each new letter was added in front of the last one.", "ps": [5], "py": [4], "vars": [["Index", 4], ["Reverse", "RATS"]], "hl": ["Reverse"], "out": ["RATS"], "cells": ["S", "T", "A", "R"]}] });
Lib.codePanel($("#cdStr"), { pseudo: FN_PS, py: FN_PY });
Lib.codePanel($("#cdLoop"), { pseudo: CT_PS, py: CT_PY });
Lib.codePanel($("#cdBuild"), { pseudo: RV_PS, py: RV_PY });


const cellsHtml = (s, hi) => [...s].map((c, i) => `<span class="${hi(i) ? "m1" : ""}" title="position ${i + 1}">${esc(c === " " ? "␣" : c)}<small style="display:block;font:600 .6rem var(--sans);color:var(--muted);text-align:center">${i + 1}</small></span>`).join("");
/* ---------- Lab 1 ---------- */
(() => {
  let a, b; const inp = $("#ti");
  const upd = () => {
    if (!a || !b) return; const s = inp.value, n = s.length;
    if (!n) { $("#tcells").innerHTML = ""; $("#tt").innerHTML = ""; return; }
    const st = Math.min(a.get(), n), ln = b.get(), sub = s.substr(st - 1, ln);
    $("#tcells").innerHTML = cellsHtml(s, (i) => i >= st - 1 && i < st - 1 + ln);
    $("#tt").innerHTML = `<tr><th>Pseudocode</th><th>Result</th><th>Python</th></tr><tr><td>LENGTH(Text)</td><td>${n}</td><td>len(text)</td></tr><tr><td>UCASE(Text)</td><td>"${esc(s.toUpperCase())}"</td><td>text.upper()</td></tr><tr><td>LCASE(Text)</td><td>"${esc(s.toLowerCase())}"</td><td>text.lower()</td></tr><tr><td>SUBSTRING(Text, ${st}, ${ln})</td><td>"${esc(sub)}"</td><td>text[${st - 1}:${st - 1 + ln}]</td></tr>`;
  };
  a = Lib.slider($("#s1"), { id: "ts", label: "Start position ", min: 1, max: 20, value: 3, onInput: upd });
  b = Lib.slider($("#s2"), { id: "tl", label: "How many characters ", min: 1, max: 10, value: 4, onInput: upd });
  inp.addEventListener("input", upd); upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  const f = $("#un1"), s = $("#un2");
  const upd = () => {
    const F = f.value, S = s.value;
    Lib.codePanel($("#ucode"), { pseudo: ["Username ← LCASE(SUBSTRING(First, 1, 1) & Surname)", "Initials ← UCASE(SUBSTRING(First, 1, 1) & SUBSTRING(Surname, 1, 1))", 'Greeting ← "Hello " & First & " " & Surname'], py: ["username = (first[0] + surname).lower()", "initials = (first[0] + surname[0]).upper()", 'greeting = "Hello " + first + " " + surname'] });
    if (!F || !S) { $("#ut").innerHTML = "<tr><td>Type a first name and a surname.</td></tr>"; return; }
    $("#ut").innerHTML = `<tr><th>Variable</th><th>Value</th></tr><tr><td>Username</td><td>"${esc((F[0] + S).toLowerCase())}"</td></tr><tr><td>Initials</td><td>"${esc((F[0] + S[0]).toUpperCase())}"</td></tr><tr><td>Greeting</td><td>"${esc("Hello " + F + " " + S)}"</td></tr><tr><td>LENGTH(Surname)</td><td>${S.length}</td></tr>`;
  };
  f.addEventListener("input", upd); s.addEventListener("input", upd); upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  const w = $("#lw"), l = $("#ll");
  const upd = () => { const W = w.value, L = l.value; if (!W) { $("#lcells").innerHTML = ""; $("#lv").textContent = "Type a word."; return; }
    let c = 0; [...W].forEach((x) => { if (x === L) c++; });
    $("#lcells").innerHTML = cellsHtml(W, (i) => L && W[i] === L);
    $("#lv").innerHTML = L ? `The loop checks ${W.length} positions. <b>${L}</b> matches ${c} time${c === 1 ? "" : "s"}, so <b>Count = ${c}</b>.${/[A-Z]/.test(W + L) ? " Capital and lower-case letters are different characters." : ""}` : "Type one letter to count."; };
  w.addEventListener("input", upd); l.addEventListener("input", upd); upd();
})();

/* ---------- Practise ---------- */
Lib.match($("#m1"), { prompt: "Match each expression to what it gives.", pairs: [
  ['LENGTH("Hello")', "5"], ['UCASE("hi")', '"HI"'], ['SUBSTRING("Computer", 1, 3)', '"Com"'], ['"Good" & "Day"', '"GoodDay"'], ['LCASE("ABC")', '"abc"'], ['SUBSTRING("Computer", 8, 1)', '"r"']],
  done: "Positions start at 1, and & joins." });
Lib.order($("#o1"), { prompt: "Put the lines of the reverse program in order.", items: ['Word ← "STAR"', 'Reverse ← ""', "FOR Index ← 1 TO LENGTH(Word)", "Reverse ← SUBSTRING(Word, Index, 1) & Reverse", "NEXT Index", "OUTPUT Reverse"], done: "Set up, empty string, loop, join on the front, end loop, output." });
Lib.calc($("#c1"), { qs: [
  { q: "What is LENGTH(\"Good morning\")?", a: 12, sol: "Good (4) + space (1) + morning (7) = 12." },
  { q: "What is SUBSTRING(\"Computer\", 4, 3)? Type the letters.", t: ["PUT"], ph: "letters", sol: "Start at position 4 (p) and take 3: put." },
  { q: "SUBSTRING(Word, 1, 1) with Word = \"Python\" gives which letter?", t: ["P"], ph: "letter", sol: "Position 1 is the first letter." },
  { q: "FOR Index ← 1 TO LENGTH(\"banana\"). How many times does the loop run?", a: 6, sol: "LENGTH(\"banana\") is 6." },
  { q: "The loop counts how many times \"a\" appears in \"banana\". What is Count at the end?", a: 3, sol: "b-a-n-a-n-a: three a's." },
  { q: "In Python, which index is the same as pseudocode position 5?", a: 4, sol: "Python starts at 0, so position 5 is index 4." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does LENGTH(\"hi there\") return?", opts: ["8", "7", "2", "9"], a: 0, why: "The space counts as a character." },
  { q: "In pseudocode, the first character of a string is at position...", opts: ["1", "0", "-1", "LENGTH"], a: 0, why: "Cambridge pseudocode starts at 1. Python starts at 0." },
  { q: "Which symbol joins two strings in pseudocode?", opts: ["&", "+", "*", "/"], a: 0, why: "& is concatenation." },
  { q: "SUBSTRING(\"Computer\", 2, 3) is...", opts: ["\"omp\"", "\"Com\"", "\"mpu\"", "\"ompu\""], a: 0, why: "Start at 2 (o), take 3: omp." },
  { q: "Are \"a\" and \"A\" equal in a comparison?", opts: ["No, they are different characters", "Yes", "Only in Python", "Only in a FOR loop"], a: 0, why: "Use UCASE or LCASE first to ignore case." }] });
Lib.cards($("#fc1"), { cards: [
  ["String", "A sequence of characters, for example \"Hello\"."],
  ["Character", "A single letter, digit, space or symbol."],
  ["LENGTH", "A function that gives the number of characters in a string."],
  ["SUBSTRING", "A function that takes part of a string: SUBSTRING(String, start, how many)."],
  ["UCASE / LCASE", "Functions that give the string in upper case or in lower case."],
  ["Concatenation", "Joining strings together, using & in pseudocode."],
  ["Position", "The place of a character in a string. It starts at 1 in pseudocode."],
  ["Empty string", "A string with no characters, written \"\"."]] });

