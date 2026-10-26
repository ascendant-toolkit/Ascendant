/* ===== Fibonacci: double recursion, trace table, call counts ===== */
const PS = ["FUNCTION Fib(Number : INTEGER) RETURNS INTEGER", "   IF Number <= 1 THEN", "      Result ← Number", "   ELSE", "      Result ← Fib(Number - 1) + Fib(Number - 2)", "   ENDIF", "   RETURN Result", "ENDFUNCTION"];
const PY = ["def fib(number):", "    if number <= 1:", "        result = number", "    else:", "        result = fib(number - 1) + fib(number - 2)", "    return result"];
const CODE = { ps: PS, py: PY };
const fibv = (n) => { let a = 0, b = 1; for (let i = 0; i < n; i++) [a, b] = [b, a + b]; return a; };
const callsOf = (n) => 2 * fibv(n + 1) - 1;

/* Stack + call tree animation for Fib(n) */
function fibTrace(n) {
  const T = Trace({ treeName: "Number", outTitle: "Values returned", maxDepth: n + 1 });
  const run = (k, parent, ra) => {
    const nd = T.call(`Fib(${k})`, k, parent, ra, `<b>Fib(${k}) is called.</b> A new frame is pushed with Number = ${k}.`, [0], [0]);
    if (k <= 1) {
      T.note(nd, `Number = ${k}: BASE CASE`, `Is Number &lt;= 1? <b>Yes</b>: the <b>base case</b>. Result ← Number = ${k}. No further call.`, [1, 2], [1, 2], "base");
      T.print(`Fib(${k}) returns ${k}`);
      T.ret(nd, String(k), `RETURN Result sends <b>${k}</b> back to the waiting call. The frame is popped.`, [6], [5]);
      return k;
    }
    T.note(nd, "general case: two calls", `Is Number &lt;= 1? No (${k}). General case: Result ← Fib(${k - 1}) + Fib(${k - 2}). The first call is made now; the addition has to <b>wait</b> for both answers.`, [1, 4], [1, 4]);
    T.setStatus(nd, `paused: waiting for Fib(${k - 1})`);
    const a = run(k - 1, nd, "line 5, first call");
    T.note(nd, `${a} + Fib(${k - 2}) …`, `Fib(${k - 1}) returned ${a}. Back in Fib(${k}), the <b>second</b> call, Fib(${k - 2}), is made next.`, [4], [4]);
    T.setStatus(nd, `paused: waiting for Fib(${k - 2})`);
    const b = run(k - 2, nd, "line 5, second call");
    T.note(nd, `${a} + ${b} = ${a + b}`, `Both calls have returned: Result ← ${a} + ${b} = <b>${a + b}</b>.`, [4], [4]);
    T.print(`Fib(${k}) returns ${a + b}`);
    T.ret(nd, String(a + b), `RETURN Result sends ${a + b} up. The frame is popped.`, [6], [5]);
    return a + b;
  };
  const res = run(n, null, "main");
  T.finish(`The stack is empty. Fib(${n}) = ${res}, using ${T.nodes.length} calls. The stack was never more than ${n} frames deep: only one branch is active at a time.`, [], []);
  return T;
}
showAlgo("#aStack", fibTrace(4), CODE, "Animated call stack and call tree for Fib(4)", 2800);
showAlgo("#aStack3", fibTrace(3), CODE, "Animated call stack and call tree for Fib(3)", 2800);

/* The paper's trace table for Fib(5) (leftmost path) */
(() => {
  const rows = [
    ["1", "Fib(5)", "5", "Fib(4) + Fib(3)", "", "down", "<b>Call 1: Fib(5).</b> Number is 5, so this is the general case. Result holds the sum it cannot finish: Fib(4) + Fib(3). Nothing is returned yet."],
    ["2", "Fib(4)", "4", "Fib(3) + Fib(2)", "", "down", "<b>Call 2: Fib(4).</b> The first call from Fib(5). Again the general case, so it waits for Fib(3) + Fib(2)."],
    ["3", "Fib(3)", "3", "Fib(2) + Fib(1)", "", "down", "<b>Call 3: Fib(3).</b> Another general case. The first call it makes is Fib(2)."],
    ["4", "Fib(2)", "2", "Fib(1) + Fib(0)", "", "down", "<b>Call 4: Fib(2).</b> The last general case on this path. Its first call is Fib(1)."],
    ["5", "Fib(1)", "1", "1", "1", "base", "<b>Call 5: Fib(1).</b> Number &lt;= 1: the <b>base case</b>. Result = Number = 1, returned straight away. <b>Unwinding starts.</b>"],
    ["6", "Fib(0)", "0", "0", "0", "base", "<b>Call 6: Fib(0).</b> The second call from Fib(2), also a base case: Result = 0, returned."],
    ["(4)", "Fib(2)", "2", "1 + 0", "1", "up", "<b>Call 4 resumes.</b> Both its calls have returned: 1 + 0 = <b>1</b>."],
    ["(3)", "Fib(3)", "3", "1 + 1", "2", "up", "<b>Call 3 resumes.</b> Fib(2) returned 1, and the second call, Fib(1), is a base case returning 1: 1 + 1 = <b>2</b>."],
    ["(2)", "Fib(4)", "4", "2 + 1", "3", "up", "<b>Call 2 resumes.</b> Fib(3) returned 2, and its second call Fib(2) returns 1: 2 + 1 = <b>3</b>."],
    ["(1)", "Fib(5)", "5", "3 + 2", "5", "up", "<b>Call 1 resumes.</b> Fib(4) returned 3, and its second call Fib(3) returns 2: 3 + 2 = <b>5</b>. Fib(5) = 5."],
  ];
  const COLS = [["Call number", 0, 90], ["Function call", 90, 130], ["Number", 220, 80], ["Result", 300, 270], ["Return value", 570, 150]];
  const RHt = 30, top = 40;
  const tbl = (n) => {
    let g = "";
    COLS.forEach(([t, x]) => { g += SV.text(x + 8, 26, t, "sm bd", { style: "font-size:11px;text-transform:uppercase;letter-spacing:.03em" }); });
    g += SV.line(0, 34, 720, 34, "ax");
    rows.forEach((r, i) => {
      const y = top + i * RHt;
      if (i >= n) { g += SV.rect(0, y, 720, RHt, "cell", { style: "opacity:.35;stroke-width:1" }); return; }
      const cls = i === n - 1 ? "cell cell-cur" : r[5] === "base" ? "cell cell-warn" : r[5] === "up" ? "cell cell-ok" : "cell";
      g += SV.rect(1, y + 1, 718, RHt - 2, cls, { style: "stroke-width:" + (i === n - 1 ? 2.5 : 1.2) });
      r.slice(0, 5).forEach((c, k) => { const [, x, w] = COLS[k], mid = k === 0 || k === 2 || k === 4; g += SV.text(mid ? x + w / 2 : x + 8, y + 20, esc(c), "lbl" + (k === 4 ? " bd" : ""), { "text-anchor": mid ? "middle" : "start", style: "font-family:var(--mono);font-size:12px" }); });
    });
    COLS.slice(1).forEach(([, x]) => { g += SV.line(x, 34, x, top + rows.length * RHt, "gr"); });
    return g;
  };
  const frames = [{ cap: "A <b>trace table</b> has one row per call. Rows 1 to 6 go <b>down</b> (the calls), then the bracketed rows go <b>up</b> (the same calls finishing). Press Next to fill in call 1.", ps: [0], py: [0], svg: tbl(0) }];
  const lines = { down: [[1, 4], [1, 4]], base: [[1, 2, 6], [1, 2, 5]], up: [[4, 6], [4, 5]] };
  rows.forEach((r, i) => frames.push({ cap: r[6], ps: lines[r[5]][0], py: lines[r[5]][1], svg: tbl(i + 1) }));
  Lib.algo($("#aTab"), { w: 720, h: top + rows.length * RHt + 10, label: "Trace table being filled in for Fib(5)", pseudo: PS, py: PY, dwell: 3400, frames });
})();

Lib.codePanel($("#codeF"), { pseudo: PS, py: PY });

/* ===== Explore lab ===== */
(() => {
  let S, hi = 0;
  const sel = $("#fbHi");
  const tree = (n, h) => {
    const nodes = [];
    const mk = (k, parent) => { const nd = { k, parent, kids: [] }; nodes.push(nd); parent && parent.kids.push(nd); if (k > 1) { mk(k - 1, nd); mk(k - 2, nd); } return nd; };
    mk(n, null); layout(nodes);
    const W = 720, lv = nodes.depth, lvs = nodes.leaves, sp = lvs > 1 ? Math.min(52, (W - 40) / (lvs - 1)) : 0, r = lvs > 14 ? 12 : 15, dy = Math.min(50, 230 / Math.max(1, lv - 1)), ox = W / 2 - ((lvs - 1) * sp) / 2, oy = 28, H = oy + (lv - 1) * dy + 34;
    const px = (nd) => ox + nd.lx * sp, py = (nd) => oy + nd.d * dy;
    let g = "";
    nodes.forEach((nd) => { if (nd.parent) g += SV.line(px(nd.parent), py(nd.parent), px(nd), py(nd), "edge"); });
    nodes.forEach((nd) => {
      const on = nd.k === h;
      g += SV.circle(px(nd), py(nd), r, "nd", on ? { style: "fill:var(--warn-soft);stroke:var(--warn);stroke-width:3" } : {}) + SV.text(px(nd), py(nd) + 4.5, nd.k, "lbl bd", { "text-anchor": "middle", style: "font-size:" + (r < 14 ? 11 : 12.5) + "px" });
    });
    return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Call tree for Fib(${n}); calls to Fib(${h}) highlighted">${g}</svg>`;
  };
  const counts = (n) => { const c = Array(n + 1).fill(0); const go = (k) => { c[k]++; if (k > 1) { go(k - 1); go(k - 2); } }; go(n); return c; };
  const fill = (n) => { sel.innerHTML = Array.from({ length: n + 1 }, (_, k) => `<option value="${k}">Fib(${k})</option>`).join(""); hi = Math.min(hi, n); sel.value = hi; };
  const draw = () => {
    if (!S) return;
    const n = S.get();
    if (+sel.options.length !== n + 1) fill(n);
    hi = +sel.value;
    const c = n <= 20 ? counts(n) : null, total = callsOf(n), loop = Math.max(n - 1, 1);
    $("#fbRO").innerHTML = `<div><small>Fib(${n}) =</small><strong>${fibv(n).toLocaleString()}</strong></div><div><small>Total calls</small><strong>${total.toLocaleString()}</strong></div><div><small>Deepest stack</small><strong>${n + 1 > 1 ? Math.max(n, 1) : 1}</strong></div><div><small>Loop passes</small><strong>${loop}</strong></div><div><small>Calls to Fib(${hi})</small><strong>${c ? c[hi] : "–"}</strong></div>`;
    $("#fbTree").innerHTML = n <= 7 ? `<div class="card">${tree(n, hi)}</div>` : `<p class="note">The tree for Fib(${n}) has ${total.toLocaleString()} boxes, too many to draw. The counts below show the same pattern.</p>`;
    if (c) {
      const mx = Math.max(...c);
      $("#fbBars").innerHTML = `<h3>Calls made to each value</h3>` + c.map((v, k) => k).reverse().map((k) => `<div style="display:flex;gap:10px;align-items:center;margin:3px 0"><span style="font:600 .85rem var(--mono);width:64px">Fib(${k})</span><div style="flex:1;background:var(--soft);border-radius:4px"><div style="width:${Math.max(1.5, (c[k] / mx) * 100)}%;height:14px;border-radius:4px;background:${k === hi ? "var(--warn)" : "var(--accent)"}"></div></div><b style="font:700 .85rem var(--mono);width:70px;text-align:right">${c[k].toLocaleString()}</b></div>`).join("");
    } else $("#fbBars").innerHTML = "";
  };
  S = Lib.slider($("#fbS"), { id: "fbN", label: "Number: ", min: 0, max: 20, value: 0, onInput: draw });
  sel.addEventListener("change", draw);
  draw();
})();

/* ===== Activities ===== */
Lib.order($("#o1"), { prompt: "Fib(3) is called. Put the events in the order they happen.", items: ["Fib(3) is called and its frame is pushed", "Fib(2) is called (first call from Fib(3)) and its frame is pushed", "Fib(1) is called: base case, returns 1", "Fib(0) is called: base case, returns 0", "Fib(2) works out 1 + 0 = 1 and returns it", "Fib(1) is called (second call from Fib(3)): base case, returns 1", "Fib(3) works out 1 + 1 = 2 and returns it"], done: "The first call goes all the way down and back before the second call starts." });

Lib.classify($("#cl1"), { prompt: "Drag each piece of the function to the part of recursion it plays.", buckets: [{ label: "Base case" }, { label: "General case (calls itself)" }, { label: "Moves towards the base case" }, { label: "Runs during unwinding" }], items: [
  { text: "IF Number <= 1", b: 0 }, { text: "Result ← Number", b: 0 }, { text: "Fib(Number - 1)", b: 1 }, { text: "Fib(Number - 2)", b: 1 }, { text: "Number - 1 and Number - 2", b: 2 }, { text: "adding the two returned values", b: 3 }], done: "Two smaller calls are added together once both have returned." });

Lib.classify($("#cl2"), { prompt: "Which version is each statement true of?", buckets: [{ label: "Recursive Fib" }, { label: "Iterative Fib" }], items: [
  { text: "Uses stack frames for each call", b: 0 }, { text: "Repeats the same calculations many times", b: 0 }, { text: "Needs about n passes of a loop", b: 1 }, { text: "Can run out of stack space for very large Number", b: 0 }, { text: "Keeps the previous two values in variables", b: 1 }, { text: "Matches the mathematical definition most closely", b: 0 }], done: "Recursion is shorter to write for Fib; the loop is faster and safer." });

Lib.match($("#m1"), { prompt: "Match each term to what it means for Fib.", pairs: [
  ["Base case", "Number is 0 or 1: the answer is known without another call"], ["General case", "Number is 2 or more: two calls are made and added"], ["Double recursion", "a function that calls itself twice, so the calls form a tree"], ["Winding", "the calls being made, down to the base cases"], ["Unwinding", "the calls returning, with each sum worked out"], ["Stack frame", "one call’s copy of Number and its return address"]], done: "Those six ideas cover everything Fib can ask." });

/* ===== Practise ===== */
Lib.calc($("#c1"), { qs: [
  { q: "What does Fib(1) return?", a: 1, tol: 0, hint: "Number is 1, which is a base case.", sol: "Number <= 1, so Result = Number = 1." },
  { q: "What does Fib(0) return?", a: 0, tol: 0, hint: "Also a base case.", sol: "Number <= 1, so Result = Number = 0." },
  { q: "What does Fib(2) return?", a: 1, tol: 0, hint: "Fib(1) + Fib(0).", sol: "1 + 0 = 1." },
  { q: "What does Fib(3) return?", a: 2, tol: 0, hint: "Fib(2) + Fib(1).", sol: "1 + 1 = 2." },
  { q: "What does Fib(6) return?", a: 8, tol: 0, hint: "Keep adding the two before: 0, 1, 1, 2, 3, 5, …", sol: "Fib(4) = 3 and Fib(5) = 5, so 3 + 5 = 8." },
  { q: "How many calls to Fib are made in total by Fib(4), counting the first call?", a: 9, tol: 0, hint: "Fib(4) → Fib(3) + Fib(2); count every box in the tree.", sol: "Fib(4) 1, Fib(3) 5 calls, Fib(2) 3 calls: 1 + 5 + 3 = 9." },
  { q: "How many times is Fib(1) called by Fib(5)?", a: 5, tol: 0, hint: "Draw the tree for Fib(5) and count the Fib(1) boxes. Fib(1) is Fib(5)’s own value, so you can check this against the answer.", sol: "Each call to Fib(1) adds 1 to the total, and Fib(5) = 5, so Fib(1) is called 5 times." },
  { q: "What is the maximum number of frames on the stack at one time during Fib(5)?", a: 5, tol: 0, hint: "Follow the left branch down: Fib(5), Fib(4), Fib(3), Fib(2), then Fib(1).", sol: "Fib(5), Fib(4), Fib(3), Fib(2) and Fib(1) are all on the stack together: the stack holds one branch only. That is 5 frames, equal to Number." }] });

Lib.quiz($("#qz1"), { qs: [
  { q: "What is the base case of Fib?", opts: ["Number = 0 only", "Number <= 1, which returns Number", "Number = 2, which returns 1", "Number < 0"], a: 1, why: "Both Fib(0) = 0 and Fib(1) = 1 are known, and both are handled by returning Number." },
  { q: "Fib(Number - 1) + Fib(Number - 2) is an example of…", opts: ["tail recursion only", "double (binary) recursion", "iteration", "indirect recursion"], a: 1, why: "The function calls itself twice in one line, so the calls form a tree." },
  { q: "In Fib(5), which call is made first after Fib(5) itself?", opts: ["Fib(4)", "Fib(3)", "Fib(0)", "Fib(1)"], a: 0, why: "Fib(Number - 1) comes first in the expression, so Fib(4) is called, and it is completely finished before Fib(3) is started." },
  { q: "A trace table for Fib(5) has a row for call 4, Fib(2), with Result “Fib(1) + Fib(0)”. What is in its Return value column on that row?", opts: ["1", "0", "blank, because it has not returned yet", "1 + 0"], a: 2, why: "On the winding row the call is still waiting. The Return value is filled on the later (4) row, once both calls have returned." },
  { q: "The base case is changed to IF Number = 1 only. What happens when Fib(2) is called?", opts: ["It returns 1", "It calls Fib(1) and Fib(0), and Fib(0) keeps calling Fib(−1), Fib(−2)… until the stack overflows", "It returns 0", "It returns 2"], a: 1, why: "Fib(0) is no longer a base case, so it calls Fib(−1) and Fib(−2), and the numbers keep falling." },
  { q: "Why is recursive Fib slower than the loop for Number = 30?", opts: ["Recursion is always slower", "The same values are calculated again and again", "Python is slow at addition", "The loop uses a stack"], a: 1, why: "About 2.7 million calls are made for Fib(30) because nothing is remembered between calls." },
  { q: "How many frames are on the stack at the deepest point of Fib(6)?", opts: ["6", "7", "13", "25"], a: 0, why: "The deepest chain is Fib(6), Fib(5), Fib(4), Fib(3), Fib(2), Fib(1): six frames. Only one branch is on the stack at a time." }] });

Lib.cards($("#fc1"), { cards: [
  ["Fibonacci sequence", "0, 1, 1, 2, 3, 5, 8, … where each number is the sum of the previous two."],
  ["Base case", "The input for which the answer is known without a further call. For Fib: Number = 0 or 1."],
  ["General case", "The branch where the function calls itself with a simpler value: Fib(Number - 1) + Fib(Number - 2)."],
  ["Double recursion", "A function that calls itself twice. The calls form a tree, not a chain."],
  ["Call tree", "A diagram with a box for every call; the children of a box are the calls it makes."],
  ["Winding", "The phase where calls are made until the base case is reached."],
  ["Unwinding", "The phase where calls return and their frames are popped, in reverse order."],
  ["Stack frame", "The block pushed on the call stack for each call: parameters, local variables and the return address."],
  ["Return address", "Where the program carries on once a call finishes."],
  ["Trace table", "A table that records the calls, parameter values, results and returned values step by step."],
  ["Stack overflow", "An error when the call stack runs out of memory, for example because the base case is never reached."],
  ["Memoisation", "Storing answers already worked out so they are not recalculated (beyond the 9618 syllabus)."]] });
