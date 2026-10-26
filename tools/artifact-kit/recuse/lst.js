/* ===== Lists and strings: first item, then the rest. Indexes start at 0. ===== */
const KINDS = {
  sum: {
    name: "Total", ps: ["FUNCTION Total(Numbers, Index, Last : INTEGER) RETURNS INTEGER", "   IF Index > Last THEN", "      RETURN 0", "   ELSE", "      RETURN Numbers[Index] + Total(Numbers, Index + 1, Last)", "   ENDIF", "ENDFUNCTION"],
    py: ["def total(numbers, index):", "    if index >= len(numbers):", "        return 0", "    else:", "        return numbers[index] + total(numbers, index + 1)"],
    hl: { base: [[1, 2], [1, 2]], add: [[1, 4], [1, 4]], hit: [[1, 4], [1, 4]], miss: [[1, 4], [1, 4]], upadd: [[4], [4]], uphit: [[4], [4]], upmiss: [[4], [4]], upbase: [[2], [2]] },
  },
  cnt: {
    name: "CountItem", ps: ["FUNCTION CountItem(Numbers, Index, Last, Target : INTEGER) RETURNS INTEGER", "   IF Index > Last THEN", "      RETURN 0", "   ELSEIF Numbers[Index] = Target THEN", "      RETURN 1 + CountItem(Numbers, Index + 1, Last, Target)", "   ELSE", "      RETURN CountItem(Numbers, Index + 1, Last, Target)", "   ENDIF", "ENDFUNCTION"],
    py: ["def count_item(numbers, index, target):", "    if index >= len(numbers):", "        return 0", "    elif numbers[index] == target:", "        return 1 + count_item(numbers, index + 1, target)", "    else:", "        return count_item(numbers, index + 1, target)"],
    hl: { base: [[1, 2], [1, 2]], hit: [[1, 3, 4], [1, 3, 4]], miss: [[3, 5, 6], [3, 5, 6]], upbase: [[2], [2]], uphit: [[4], [4]], upmiss: [[6], [6]] },
  },
  vow: {
    name: "CountVowels", ps: ["FUNCTION CountVowels(Value : STRING, Index : INTEGER) RETURNS INTEGER", "   IF Index >= LENGTH(Value) THEN", "      RETURN 0", "   ELSEIF IsVowel(MID(Value, Index, 1)) THEN", "      RETURN 1 + CountVowels(Value, Index + 1)", "   ELSE", "      RETURN CountVowels(Value, Index + 1)", "   ENDIF", "ENDFUNCTION"],
    py: ["def count_vowels(value, index):", "    if index >= len(value):", "        return 0", "    elif value[index] in \"aeiou\":", "        return 1 + count_vowels(value, index + 1)", "    else:", "        return count_vowels(value, index + 1)"],
    hl: { base: [[1, 2], [1, 2]], hit: [[1, 3, 4], [1, 3, 4]], miss: [[3, 5, 6], [3, 5, 6]], upbase: [[2], [2]], uphit: [[4], [4]], upmiss: [[6], [6]] },
  },
};
Lib.codePanel($("#codeSum"), { pseudo: KINDS.sum.ps, py: KINDS.sum.py });
Lib.codePanel($("#codeCnt"), { pseudo: KINDS.cnt.ps, py: KINDS.cnt.py });
Lib.codePanel($("#codeVow"), { pseudo: KINDS.vow.ps, py: KINDS.vow.py });

const PRESETS = [
  { k: "sum", label: "Total of 4, 7, 2, 9", items: [4, 7, 2, 9] },
  { k: "sum", label: "Total of 6, 1, 8, 5", items: [6, 1, 8, 5] },
  { k: "sum", label: "Total of 3, 3, 3, 3, 3, 3", items: [3, 3, 3, 3, 3, 3] },
  { k: "cnt", label: "Count the 0s in 0, 5, 1, 2, 5, 9, 9, 6, 5, 0 (O/N 2025)", items: [0, 5, 1, 2, 5, 9, 9, 6, 5, 0], target: 0 },
  { k: "cnt", label: "Count the 5s in 0, 5, 1, 2, 5, 9, 9, 6, 5, 0", items: [0, 5, 1, 2, 5, 9, 9, 6, 5, 0], target: 5 },
  { k: "cnt", label: "Count the 7s in 0, 5, 1, 2, 5, 9, 9, 6, 5, 0", items: [0, 5, 1, 2, 5, 9, 9, 6, 5, 0], target: 7 },
  ...["imagine", "recursion", "queue", "rhythm"].map((w) => ({ k: "vow", label: `Vowels in “${w}”` + (w === "imagine" ? " (O/N 2023)" : ""), items: [...w] })),
];

/* simulate one preset: per-call item, kind and returned value */
function sim(p) {
  const n = p.items.length, vowel = (c) => "aeiou".includes(c), calls = [], val = Array(n + 1).fill(0);
  for (let j = n - 1; j >= 0; j--) { const it = p.items[j], m = p.k === "sum" ? true : p.k === "cnt" ? it === p.target : vowel(it); val[j] = p.k === "sum" ? it + val[j + 1] : (m ? 1 : 0) + val[j + 1]; }
  for (let j = 0; j <= n; j++) { if (j === n) { calls.push({ kind: "base", val: 0 }); break; } const it = p.items[j]; calls.push({ item: it, kind: p.k === "sum" ? "add" : (p.k === "cnt" ? it === p.target : vowel(it)) ? "hit" : "miss", val: val[j] }); }
  return { n, calls, val };
}
const callLabel = (p, j, n) => p.k === "sum" ? `Total(Numbers, ${j}, ${n - 1})` : p.k === "cnt" ? `CountItem(Numbers, ${j}, ${n - 1}, ${p.target})` : `CountVowels("${p.items.join("")}", ${j})`;
const waitExpr = (p, c, j) => { const rest = `${KINDS[p.k].name}(…, ${j + 1})`; return c.kind === "base" ? "0" : c.kind === "add" ? `${c.item} + ${rest}` : c.kind === "hit" ? `1 + ${rest}` : rest; };
const doneExpr = (p, c, s, j) => (c.kind === "base" ? "0" : c.kind === "add" ? `${c.item} + ${s.val[j + 1]}` : c.kind === "hit" ? `1 + ${s.val[j + 1]}` : `${s.val[j + 1]}`);

function listSvg(p, s, st) {
  const W = 720, n = s.n, cw = Math.min(58, (W - 40) / n), x0 = (W - n * cw) / 2, y = 40, ch = 38;
  let g = "";
  for (let j = 0; j < n; j++) {
    const unw = st.unwinding, cur = j === st.cur;
    const faded = st.cur >= 0 && (unw ? j > st.cur : j < st.cur);
    const cls = cur ? (unw ? "cell cell-ok" : "cell cell-cur") : "cell";
    g += SV.rect(x0 + j * cw + 1, y, cw - 2, ch, cls, { rx: 6, style: faded ? "opacity:.3" : "" });
    g += SV.text(x0 + (j + 0.5) * cw, y + 25, p.items[j], "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:15px" + (faded ? ";opacity:.35" : "") });
    g += SV.text(x0 + (j + 0.5) * cw, y - 8, j, "sm", { "text-anchor": "middle", style: "font-family:var(--mono)" });
  }
  g += SV.text(24, 116, "CALLS, IN THE ORDER THEY WERE MADE", "sm bd", { "text-anchor": "start", style: "letter-spacing:.08em" });
  for (let j = 0; j < Math.min(st.k, n + 1); j++) {
    const c = s.calls[j], yy = 124 + j * 24, ret = j >= st.k - st.r, cur = j === st.cur;
    g += SV.rect(1, yy, 718, 22, cur ? "cell cell-cur" : ret ? "cell cell-ok" : c.kind === "base" ? "cell cell-warn" : "cell", { rx: 5, style: "stroke-width:" + (cur ? 2.2 : 1) });
    g += SV.text(10, yy + 16, `${j + 1}  ${callLabel(p, j, n)}`, "lbl", { "text-anchor": "start", style: "font-family:var(--mono);font-size:12px" });
    g += SV.text(430, yy + 16, "= " + (ret ? doneExpr(p, c, s, j) : waitExpr(p, c, j)), "lbl", { "text-anchor": "start", style: "font-family:var(--mono);font-size:12px" });
    if (ret) g += SV.text(710, yy + 16, "→ " + c.val, "lbl bd t3", { "text-anchor": "end", style: "font-family:var(--mono);font-size:13px" });
  }
  return g;
}

function listFrames(p) {
  const s = sim(p), n = s.n, K = KINDS[p.k], fr = [], nm = K.name;
  const hl = (key) => K.hl[key];
  const item = (c) => (p.k === "vow" ? `“${c.item}”` : c.item);
  fr.push({ cap: `${p.label}. The function handles the item at Index, then calls itself for the rest. Press Next to make the first call.`, ps: [0], py: [0], svg: listSvg(p, s, { k: 0, r: 0, cur: -1 }) });
  s.calls.forEach((c, j) => {
    const h = hl(c.kind), where = `<b>Call ${j + 1}: ${callLabel(p, j, n)}.</b>`;
    let cap;
    if (c.kind === "base") cap = `${where} Index ${j} is past the last item: the <b>base case</b>. It returns 0, with no further call.`;
    else if (p.k === "sum") cap = `${where} Index ${j} is not past the end, so the general case runs: item ${item(c)} is added to the total of the rest. That needs another call, so the + <b>waits</b>.`;
    else if (c.kind === "hit") cap = `${where} ${item(c)} ${p.k === "cnt" ? `equals ${p.target}` : "is a vowel"}: a match, so this call will return <b>1 +</b> the count for the rest. It has to wait for that call.`;
    else cap = `${where} ${item(c)} ${p.k === "cnt" ? `is not ${p.target}` : "is not a vowel"}: no match, so this call will return the count for the rest <b>unchanged</b>. It waits for that call.`;
    fr.push({ cap, ps: h[0], py: h[1], svg: listSvg(p, s, { k: j + 1, r: 0, cur: j }) });
  });
  for (let j = n; j >= 0; j--) {
    const c = s.calls[j], h = hl("up" + c.kind), r = n - j + 1;
    const cap = c.kind === "base" ? `<b>Call ${j + 1} returns 0.</b> The frame is popped and <b>unwinding starts</b>.` : p.k === "sum" ? `<b>Call ${j + 1} resumes.</b> The call below returned ${s.val[j + 1]}, so ${c.item} + ${s.val[j + 1]} = <b>${c.val}</b>, which it returns.` : c.kind === "hit" ? `<b>Call ${j + 1} resumes.</b> It was a match, so 1 + ${s.val[j + 1]} = <b>${c.val}</b>.` : `<b>Call ${j + 1} resumes.</b> No match, so it passes ${s.val[j + 1]} up <b>unchanged</b>.`;
    fr.push({ cap: cap + (j === 0 ? ` The answer is <b>${c.val}</b>.` : ""), ps: h[0], py: h[1], svg: listSvg(p, s, { k: n + 1, r, cur: j, unwinding: true }) });
  }
  return { frames: fr, sim: s };
}
const listAlgo = (sel, p, label) => { const { frames, sim: s } = listFrames(p); Lib.algo($(sel), { w: 720, h: 124 + (s.n + 1) * 24 + 8, label, pseudo: KINDS[p.k].ps, py: KINDS[p.k].py, dwell: 2800, frames }); return s; };

listAlgo("#aSum", PRESETS[0], "Total of 4, 7, 2, 9, call by call");
listAlgo("#aVow", PRESETS.find((p) => p.items.join("") === "imagine"), "Counting vowels in imagine, call by call");

/* the same Total call as a stack and call tree */
(() => {
  const p = PRESETS[0], s = sim(p), n = s.n, T = Trace({ treeName: "Index", outTitle: "Values returned", maxDepth: n + 1 });
  const run = (j, parent) => {
    const nd = T.call(callLabel(p, j, n).replace("Numbers, ", ""), j, parent, j ? "line 5" : "main", `<b>${callLabel(p, j, n)} is called.</b> A new frame is pushed with Index = ${j}.`, [0], [0]);
    if (j === n) { T.note(nd, "Index > Last: BASE CASE", `Is Index &gt; Last? ${j} &gt; ${n - 1}: <b>Yes</b>. Base case: RETURN 0.`, [1, 2], [1, 2], "base"); T.print("Index " + j + " returns 0"); T.ret(nd, "0", "RETURN 0 sends <b>0</b> back. The frame is popped and unwinding begins.", [2], [2]); return 0; }
    T.note(nd, `adds ${p.items[j]}: must wait`, `Is Index &gt; Last? No. General case: Numbers[${j}] = ${p.items[j]}, plus <b>Total of the rest</b>. The addition cannot happen until that call returns.`, [1, 4], [1, 4]);
    T.setStatus(nd, "paused: waiting for the rest");
    const v = run(j + 1, nd), t = p.items[j] + v;
    T.note(nd, `${p.items[j]} + ${v} = ${t}`, `The call below returned ${v}. This frame resumes: ${p.items[j]} + ${v} = <b>${t}</b>.`, [4], [4]);
    T.print(`Index ${j} returns ${t}`);
    T.ret(nd, String(t), `RETURN ${t}. The frame is popped.`, [4], [4]);
    return t;
  };
  const r = run(0, null);
  T.finish(`The stack is empty. The total is <b>${r}</b>. There were ${n + 1} calls: one per item plus the base case, and all ${n + 1} frames were on the stack at the deepest point.`, [], []);
  showAlgo("#aStack", T, { ps: KINDS.sum.ps, py: KINDS.sum.py }, "Animated call stack and call tree for Total of 4, 7, 2, 9", 2600);
})();

/* ===== Explore ===== */
(() => {
  const sel = $("#lsT");
  sel.innerHTML = PRESETS.map((p, i) => `<option value="${i}">${p.label}</option>`).join("");
  const go = () => {
    const p = PRESETS[+sel.value], s = listAlgo("#lsAlgo", p, p.label + ", call by call");
    $("#lsRO").innerHTML = `<div><small>Answer</small><strong>${s.val[0]}</strong></div><div><small>Calls made</small><strong>${s.n + 1}</strong></div><div><small>Deepest stack (frames)</small><strong>${s.n + 1}</strong></div><div><small>Loop passes needed</small><strong>${s.n}</strong></div>`;
  };
  sel.addEventListener("change", go); go();
})();

/* ===== Activities ===== */
Lib.order($("#o1"), { prompt: "Total(Numbers, 0, 2) is called with Numbers = 3, 5, 2. Put the events in the order they happen.", items: ["Total(Numbers, 0, 2) is called: it must add 3 to the total of the rest", "Total(Numbers, 1, 2) is called: it must add 5 to the total of the rest", "Total(Numbers, 2, 2) is called: it must add 2 to the total of the rest", "Total(Numbers, 3, 2) is called: Index is past Last, base case, returns 0", "Total(Numbers, 2, 2) works out 2 + 0 = 2 and returns it", "Total(Numbers, 1, 2) works out 5 + 2 = 7 and returns it", "Total(Numbers, 0, 2) works out 3 + 7 = 10 and returns it"], done: "All the calls go down to the end of the list first; the additions happen on the way back up." });

Lib.classify($("#cl1"), { prompt: "Drag each piece of CountItem to the part of recursion it plays.", buckets: [{ label: "Base case" }, { label: "General case (calls itself)" }, { label: "Moves towards the base case" }, { label: "Runs during unwinding" }], items: [
  { text: "IF Index > Last THEN RETURN 0", b: 0 }, { text: "CountItem(Numbers, Index + 1, Last, Target)", b: 1 }, { text: "Index + 1", b: 2 }, { text: "the 1 + added when there is a match", b: 3 }, { text: "RETURN 0", b: 0 }, { text: "ELSEIF Numbers[Index] = Target", b: 1 }], done: "One item is dealt with per call; the base case stops the chain at the end of the data." });

Lib.classify($("#cl2"), { prompt: "Is each piece part of the loop version or the recursive version?", buckets: [{ label: "Loop version" }, { label: "Recursive version" }], items: [
  { text: "Total ← 0 before the loop", b: 0 }, { text: "RETURN 0 when Index > Last", b: 1 }, { text: "FOR Index ← 0 TO Last", b: 0 }, { text: "Index + 1 passed to the next call", b: 1 }, { text: "Total ← Total + Numbers[Index]", b: 0 }, { text: "RETURN Numbers[Index] + Total(…)", b: 1 }, { text: "uses stack frames", b: 1 }, { text: "uses one variable that changes", b: 0 }], done: "Every part of the loop has a partner in the recursive version." });

Lib.match($("#m1"), { prompt: "Match each term to what it means for these functions.", pairs: [
  ["Base case", "no items left: the index is past the end, so return the starting value (0)"], ["General case", "handle the item at Index and call again with Index + 1"], ["Running total", "in the loop version a variable; in the recursive version the value passed back up the calls"], ["Index", "which item this call is dealing with: the parameter that moves towards the base case"], ["Winding", "calls going down the list, one item each"], ["Unwinding", "calls returning, with each sum or count worked out"]], done: "Those six ideas turn any loop over a list into a recursive function." });

/* ===== Practise ===== */
Lib.calc($("#c1"), { qs: [
  { q: "At what value of Index is the base case reached in Total(Numbers, 0, 3)?", a: 4, tol: 0, hint: "Base case: Index is greater than Last (3).", sol: "Index goes 0, 1, 2, 3 and then 4, which is greater than 3." },
  { q: "How many calls to Total are made in total, counting the first and the base case?", a: 5, tol: 0, hint: "One per item, plus the base case.", sol: "4 items + 1 = 5 calls." },
  { q: "What does the base-case call return?", a: 0, tol: 0, hint: "Nothing left to add.", sol: "It returns 0." },
  { q: "What does Total(Numbers, 3, 3) return? (Numbers = 6, 1, 8, 5)", a: 5, tol: 0, hint: "Numbers[3] plus the base case.", sol: "5 + 0 = 5." },
  { q: "What does Total(Numbers, 2, 3) return?", a: 13, tol: 0, hint: "Numbers[2] plus the answer you just found.", sol: "8 + 5 = 13." },
  { q: "What does Total(Numbers, 1, 3) return?", a: 14, tol: 0, hint: "Numbers[1] plus the previous answer.", sol: "1 + 13 = 14." },
  { q: "What does the original call Total(Numbers, 0, 3) return?", a: 20, tol: 0, hint: "Numbers[0] plus the previous answer.", sol: "6 + 14 = 20." },
  { q: "What is the greatest number of frames on the stack at one time?", a: 5, tol: 0, hint: "Every call waits for the one below it.", sol: "All 5 calls are waiting at the deepest point." }] });

Lib.quiz($("#qz1"), { qs: [
  { q: "What should the base case of a recursive total return?", opts: ["1", "0", "the last item", "−1"], a: 1, why: "Zero is the starting value for adding. With nothing left to add, the total of the rest is 0." },
  { q: "What should the base case of a recursive product (multiplying all the items) return?", opts: ["0", "1", "the first item", "−1"], a: 1, why: "1 is the starting value for multiplying. Returning 0 would make every product 0." },
  { q: "In CountItem, what does a call return when Numbers[Index] is not equal to Target?", opts: ["0", "1", "the count for the rest, unchanged", "Index"], a: 2, why: "No match means nothing is added, so the result of the call for the rest is passed straight up." },
  { q: "The recursive call is written as Total(Numbers, Index, Last) without + 1. What happens?", opts: ["The total is wrong", "It never reaches the base case and the stack overflows", "It returns 0", "It works but slowly"], a: 1, why: "Index never changes, so the call is identical each time and there is no end." },
  { q: "A string of 12 characters is passed to CountVowels. How many calls are made?", opts: ["11", "12", "13", "24"], a: 2, why: "12 characters plus the base-case call at Index 12." },
  { q: "In a loop version, the line Total ← 0 before the loop becomes what in the recursive version?", opts: ["The parameter list", "The base case return value", "The recursive call", "Nothing: it is dropped"], a: 1, why: "The starting value is what you get when there is nothing to process, which is the base case." },
  { q: "Why might a loop be preferred to recursion for totalling a list of one million values?", opts: ["Recursion cannot add", "A million frames on the stack could cause a stack overflow", "Loops are shorter to write", "Recursion gives a different answer"], a: 1, why: "Each item adds a stack frame. The loop needs no stack." }] });

Lib.cards($("#fc1"), { cards: [
  ["First and rest", "Handle the item at Index, then let a recursive call handle everything after it."],
  ["Base case", "No items left (Index past the last item, or an empty string). Returns the starting value: 0 for a sum or a count."],
  ["General case", "The branch that uses the current item and calls the function for the rest."],
  ["Index parameter", "Which item the call is dealing with. It becomes Index + 1 in the recursive call."],
  ["Running total", "A value built up one item at a time. In recursion it is built as the calls return."],
  ["Counting pattern", "A match returns 1 + the call for the rest; a non-match returns the call for the rest unchanged."],
  ["MID(Value, Start, Length)", "Returns Length characters of Value from position Start (the first position is 0 in 9618 string questions)."],
  ["Winding", "Calls going down the list to the base case."],
  ["Unwinding", "Calls returning, in reverse order, with results combined."],
  ["Loop to recursion", "Counter → parameter. Starting total → base case. Loop body → general case."],
  ["Stack depth", "For n items, n + 1 frames at the deepest point."]] });
