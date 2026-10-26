/* ===== Binary tree traversal: stored in arrays, null pointer = 0, indexes from 1 ===== */
const TREES = [
  { name: "Tree A", data: [50, 30, 70, 20, 40, 60], L: [2, 4, 6, 0, 0, 0], R: [3, 5, 0, 0, 0, 0] },
  { name: "Tree B", data: [40, 20, 60, 10, 30, 50, 55], L: [2, 4, 6, 0, 0, 0, 0], R: [3, 5, 0, 0, 0, 7, 0] },
  { name: "Tree C", data: [10, 20, 30, 40, 50], L: [0, 0, 0, 0, 0], R: [2, 3, 4, 5, 0] },
];
const dat = (t, p) => t.data[p - 1], lft = (t, p) => t.L[p - 1], rgt = (t, p) => t.R[p - 1];

/* visit sequence (indexes) for a traversal order */
function visits(t, order) {
  const out = [];
  const go = (p) => { if (!p) return; if (order === "pre") out.push(p); go(lft(t, p)); if (order === "in") out.push(p); go(rgt(t, p)); if (order === "post") out.push(p); };
  go(1); return out;
}
const levelsOf = (t, p = 1) => (p ? 1 + Math.max(levelsOf(t, lft(t, p)), levelsOf(t, rgt(t, p))) : 0);

/* draw the data tree; `seen` maps node index -> visit number, `cur` is the node being visited */
function treeSvg(t, seen = {}, cur = 0, showIdx = false) {
  const n = t.data.length, W = 720, pos = {}; let rank = 0;
  const walk = (p, d) => { if (!p) return; walk(lft(t, p), d + 1); pos[p] = { x: rank++, d }; walk(rgt(t, p), d + 1); };
  walk(1, 0);
  const lv = levelsOf(t), sp = n > 1 ? Math.min(84, (W - 80) / (n - 1)) : 0, dy = 66, ox = W / 2 - ((n - 1) * sp) / 2, oy = 34, H = oy + (lv - 1) * dy + 40;
  const X = (p) => ox + pos[p].x * sp, Y = (p) => oy + pos[p].d * dy;
  let g = "";
  for (let p = 1; p <= n; p++) { [lft(t, p), rgt(t, p)].forEach((c) => { if (c) g += SV.line(X(p), Y(p), X(c), Y(c), "edge"); }); }
  for (let p = 1; p <= n; p++) {
    const on = p === cur, done = seen[p] && !on;
    g += SV.circle(X(p), Y(p), 20, "nd" + (on ? " nd-cur" : done ? " nd-ok" : "")) + SV.text(X(p), Y(p) + 5, dat(t, p), "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (showIdx) g += SV.text(X(p) - 24, Y(p) - 16, "#" + p, "sm", { "text-anchor": "end", style: "font-family:var(--mono)" });
    if (seen[p]) g += SV.circle(X(p) + 18, Y(p) - 16, 10, "dot1") + SV.text(X(p) + 18, Y(p) - 12, seen[p], "sm bd", { "text-anchor": "middle", style: "fill:#fff;font-size:11px" });
  }
  return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${t.name}: binary tree">${g}</svg>`;
}

/* ---------- Learn: the stored tree ---------- */
(() => {
  const t = TREES[0], row = (lab, a) => `<tr><th>${lab}</th>${a.map((v) => `<td>${v}</td>`).join("")}</tr>`;
  $("#treeStatic").innerHTML = `<div class="card">${treeSvg(t, {}, 0, true)}<div class="tw"><table class="t mono"><tr><th>Index</th>${t.data.map((_, i) => `<th>${i + 1}</th>`).join("")}</tr>${row("Data", t.data)}${row("LeftPointer", t.L)}${row("RightPointer", t.R)}</table></div></div>`;
})();

/* ---------- code for each traversal ---------- */
const ORDERS = { in: ["L", "O", "R"], pre: ["O", "L", "R"], post: ["L", "R", "O"] };
const PROC = { in: "InOrder", pre: "PreOrder", post: "PostOrder" }, PYN = { in: "in_order", pre: "pre_order", post: "post_order" };
function codeFor(o) {
  const nm = PROC[o], pn = PYN[o];
  const PSL = { L: `      CALL ${nm}(LeftPointer[Node])`, R: `      CALL ${nm}(RightPointer[Node])`, O: "      OUTPUT Data[Node]" };
  const PYL = { L: `        ${pn}(left[node])`, R: `        ${pn}(right[node])`, O: "        print(data[node])" };
  return { ps: [`PROCEDURE ${nm}(Node : INTEGER)`, "   IF Node <> 0 THEN", ...ORDERS[o].map((k) => PSL[k]), "   ENDIF", "ENDPROCEDURE"], py: [`def ${pn}(node):`, "    if node != 0:", ...ORDERS[o].map((k) => PYL[k])] };
}
Lib.codePanel($("#codeT"), { pseudo: codeFor("in").ps, py: codeFor("in").py });

const FIND = {
  ps: ["FUNCTION Find(Node, Item : INTEGER) RETURNS INTEGER", "   IF Node = 0 THEN", "      RETURN 0", "   ELSEIF Data[Node] = Item THEN", "      RETURN Node", "   ELSEIF Item < Data[Node] THEN", "      RETURN Find(LeftPointer[Node], Item)", "   ELSE", "      RETURN Find(RightPointer[Node], Item)", "   ENDIF", "ENDFUNCTION"],
  py: ["def find(node, item):", "    if node == 0:", "        return 0", "    elif data[node] == item:", "        return node", "    elif item < data[node]:", "        return find(left[node], item)", "    else:", "        return find(right[node], item)"],
};
Lib.codePanel($("#codeFind"), { pseudo: FIND.ps, py: FIND.py });

/* ---------- Watch: traversal traces on Tree A ---------- */
function travTrace(t, o) {
  const nm = PROC[o], ord = ORDERS[o], T = Trace({ treeName: "Node", outTitle: "Output so far", maxDepth: levelsOf(t) + 1 });
  const lineOf = (k) => 2 + ord.indexOf(k);
  const side = { L: "left", R: "right" };
  const run = (p, parent, ra) => {
    const sh = p ? dat(t, p) : "∅";
    const nd = T.call(`${nm}(${p})`, sh, parent, ra, `<b>${nm}(${p}) is called.</b> ${p ? `Node = ${p}, the node holding ${dat(t, p)}.` : "Node = 0: a null pointer, there is no child here."} A new frame is pushed.`, [0], [0]);
    if (!p) {
      T.note(nd, "Node = 0: BASE CASE", `Is Node &lt;&gt; 0? <b>No.</b> This is the empty tree: the <b>base case</b>. Nothing is output and no further call is made.`, [1], [1], "base");
      T.ret(nd, null, `The procedure ends. The frame is popped and control returns to the caller.`, [6], []);
      return;
    }
    T.note(nd, `Node = ${p} (${dat(t, p)})`, `Is Node &lt;&gt; 0? <b>Yes</b> (${p}), so the node is real. The lines inside the IF run in this order: ${ord.map((k) => ({ L: "left call", R: "right call", O: "output" }[k])).join(", ")}.`, [1], [1]);
    ord.forEach((k) => {
      if (k === "O") { T.print(dat(t, p)); T.note(nd, `outputs ${dat(t, p)}`, `<b>OUTPUT Data[${p}]</b>: the value <b>${dat(t, p)}</b> is written to the output.`, [lineOf("O")], [lineOf("O")]); return; }
      const c = k === "L" ? lft(t, p) : rgt(t, p);
      T.setStatus(nd, `paused: ${side[k]} subtree`);
      run(c, nd, `line ${lineOf(k) + 1}`);
      T.note(nd, `${side[k]} subtree done`, `The ${side[k]} subtree of ${dat(t, p)} is finished. Back in ${nm}(${p}), the next line runs.`, [lineOf(k)], [lineOf(k)]);
    });
    T.ret(nd, null, `Both subtrees and the output are done. ${nm}(${p}) ends, its frame is popped and control goes back to its caller.`, [6], []);
  };
  run(1, null, "main");
  T.finish(`The stack is empty. Output: <b>${T.out.join(", ")}</b>. ${T.nodes.length} calls were made: 6 nodes plus 7 null pointers.`, [], []);
  return T;
}
["in", "pre", "post"].forEach((o) => { const c = codeFor(o); showAlgo({ in: "#aIn", pre: "#aPre", post: "#aPost" }[o], travTrace(TREES[0], o), { ps: c.ps, py: c.py }, `Animated call stack and call tree for ${PROC[o]} on Tree A`, 2200); });

/* search trace */
(() => {
  const t = TREES[0], item = 60, T = Trace({ treeName: "Node", outTitle: "Values returned", maxDepth: 5 });
  const run = (p, parent, ra) => {
    const nd = T.call(`Find(${p}, ${item})`, p ? dat(t, p) : "∅", parent, ra, `<b>Find(${p}, ${item}) is called.</b> ${p ? `Node ${p} holds ${dat(t, p)}.` : "Node = 0."}`, [0], [0]);
    if (!p) { T.note(nd, "base case: not found", "Node = 0: the item is not in this tree.", [1, 2], [1, 2], "base"); T.ret(nd, "0", "Returns 0 (not found).", [2], [2]); return 0; }
    if (dat(t, p) === item) { T.note(nd, "found!", `Node &lt;&gt; 0, and Data[${p}] = ${item}: <b>found</b>. This is a base case.`, [3, 4], [3, 4], "base"); T.ret(nd, String(p), `Returns the index <b>${p}</b>.`, [4], [4]); return p; }
    const left = item < dat(t, p);
    T.note(nd, left ? "go left" : "go right", `Data[${p}] = ${dat(t, p)}. ${item} is ${left ? "less" : "greater"} than ${dat(t, p)}, so only the <b>${left ? "left" : "right"}</b> subtree could hold it. The other side is ignored.`, left ? [5] : [7], left ? [5] : [7]);
    T.setStatus(nd, "paused: waiting for the result");
    const r = run(left ? lft(t, p) : rgt(t, p), nd, left ? "line 7" : "line 9");
    T.note(nd, `result ${r}`, `The call below returned ${r}. This frame passes it straight up.`, left ? [6] : [8], left ? [6] : [8]);
    T.ret(nd, String(r), `RETURN ${r}: the frame is popped.`, left ? [6] : [8], left ? [6] : [8]);
    return r;
  };
  const r = run(1, null, "main");
  T.finish(`The stack is empty. Find(1, ${item}) returned ${r}: the item is at index ${r}. Only ${T.nodes.length} of the 6 nodes were looked at.`, [], []);
  showAlgo("#aFind", T, FIND, "Animated call stack and call tree for Find(1, 60)", 2400);
})();

/* ===== Explore lab: step through the visits ===== */
(() => {
  const selT = $("#trT"), selO = $("#trO"); let S;
  const setup = () => {
    const t = TREES[+selT.value], seq = visits(t, selO.value);
    S = Lib.slider($("#trS"), { id: "trN", label: "Values output so far: ", min: 0, max: seq.length, value: 0, onInput: () => S && draw() });
    draw();
  };
  const draw = () => {
    const t = TREES[+selT.value], o = selO.value, seq = visits(t, o), k = S.get(), seen = {};
    seq.slice(0, k).forEach((p, i) => (seen[p] = i + 1));
    const cur = k ? seq[k - 1] : 0, n = t.data.length;
    $("#trSvg").innerHTML = `<div class="card">${treeSvg(t, seen, cur, false)}</div>`;
    $("#trRO").innerHTML = `<div><small>Nodes</small><strong>${n}</strong></div><div><small>Total calls</small><strong>${2 * n + 1}</strong></div><div><small>Deepest stack</small><strong>${levelsOf(t) + 1}</strong></div><div><small>Next to output</small><strong>${k < n ? dat(t, seq[k]) : "none"}</strong></div>`;
    $("#trOut").textContent = "Output: " + (k ? seq.slice(0, k).map((p) => dat(t, p)).join(", ") : "(nothing yet)");
  };
  selT.addEventListener("change", setup); selO.addEventListener("change", setup);
  setup();
})();

/* ===== Activities ===== */
Lib.order($("#o1"), { prompt: "InOrder(1) is called on Tree A. Put the first events in the order they happen.", items: ["InOrder(1) is called for the root, 50", "InOrder(2) is called for 50’s left child, 30", "InOrder(4) is called for 30’s left child, 20", "InOrder(0) is called for 20’s left child: Node = 0, base case, nothing happens", "20 is output", "InOrder(0) is called for 20’s right child and ends at once", "InOrder(4) ends, and InOrder(2) outputs 30"], done: "The left subtree is followed all the way down before any value is output." });

Lib.classify($("#cl1"), { prompt: "Drag each statement to the traversal it describes.", buckets: [{ label: "In-order" }, { label: "Pre-order" }, { label: "Post-order" }], items: [
  { text: "Outputs the values of a binary search tree in ascending order", b: 0 }, { text: "The OUTPUT line sits between the two recursive calls", b: 0 }, { text: "The root is always output first", b: 1 }, { text: "Useful for making a copy of a tree", b: 1 }, { text: "The root is always output last", b: 2 }, { text: "Useful for deleting a tree: children before parents", b: 2 }, { text: "The OUTPUT line sits before both recursive calls", b: 1 }, { text: "Used to evaluate an expression tree (operands before operator)", b: 2 }], done: "The position of one OUTPUT line makes all the difference." });

Lib.classify($("#cl2"), { prompt: "Which traversal of Tree A gives each output?", buckets: [{ label: "In-order" }, { label: "Pre-order" }, { label: "Post-order" }], items: [
  { text: "20, 30, 40, 50, 60, 70", b: 0 }, { text: "50, 30, 20, 40, 70, 60", b: 1 }, { text: "20, 40, 30, 60, 70, 50", b: 2 }, { text: "starts at 50 and the next value is 30", b: 1 }, { text: "ends at 50", b: 2 }, { text: "ascending order", b: 0 }], done: "Check the first and last values: they usually give it away." });

Lib.match($("#m1"), { prompt: "Match each term to what it means for a tree traversal.", pairs: [
  ["Base case", "the pointer is 0: an empty subtree, so nothing happens"], ["Subtree", "a child node with everything below it, itself a binary tree"], ["Root", "the one node that is not a child of any other"], ["Leaf", "a node with no children: both pointers are 0"], ["Traversal", "visiting every node of the tree exactly once"], ["Stack frame", "one call’s copy of Node and its return address"]], done: "Those six ideas are the vocabulary of the topic." });

/* ===== Practise ===== */
Lib.calc($("#c1"), { qs: [
  { q: "What is the first value output by an in-order traversal of Tree A?", a: 20, tol: 0, hint: "Keep going left from the root: 50, 30, 20. Then 20 has no left child.", sol: "The left-most node is 20, and nothing is output before it." },
  { q: "What is the fourth value output by an in-order traversal of Tree A?", a: 50, tol: 0, hint: "In-order is ascending: 20, 30, 40, …", sol: "20, 30, 40, 50: the fourth value is the root, 50." },
  { q: "What is the fourth value output by a pre-order traversal of Tree A?", a: 40, tol: 0, hint: "Node first: 50, then the whole left subtree (30 and its children), then the right.", sol: "50, 30, 20, 40, 70, 60: the fourth is 40." },
  { q: "What is the last value output by a post-order traversal of Tree A?", a: 50, tol: 0, hint: "Post-order ends with the root.", sol: "The root is output after both subtrees: 50." },
  { q: "How many calls to the traversal procedure are made in total on Tree A, counting calls with Node = 0?", a: 13, tol: 0, hint: "One call per node, plus one for every missing child.", sol: "6 nodes have 12 child pointers, 5 of them used, so 7 are null: 6 + 7 = 13 calls (or 2n + 1)." },
  { q: "How many of those calls have Node = 0?", a: 7, tol: 0, hint: "Count the zeros in LeftPointer and in RightPointer.", sol: "LeftPointer has 3 zeros and RightPointer has 4 zeros that belong to the six nodes, 7 in all (3 + 4)." },
  { q: "What is the greatest number of frames on the stack at one time during any traversal of Tree A (count the calls with Node = 0)?", a: 4, tol: 0, hint: "Follow the longest path: 50, 30, 20, then the null call below 20.", sol: "InOrder(1), InOrder(2), InOrder(4) and InOrder(0): 4 frames, equal to the number of levels (3) plus one." }] });

Lib.quiz($("#qz1"), { qs: [
  { q: "What is the base case of a recursive tree traversal?", opts: ["The root has been reached", "The pointer is null (0): the subtree is empty", "The node is a leaf", "The output is finished"], a: 1, why: "The empty tree is where nothing is left to visit. A leaf is not a base case: its two calls to empty trees are." },
  { q: "Which traversal outputs the values of a binary search tree in ascending order?", opts: ["Pre-order", "Post-order", "In-order", "None of them"], a: 2, why: "Left (smaller) values first, then the node, then right (larger) values." },
  { q: "In which traversal is the root output last?", opts: ["In-order", "Pre-order", "Post-order", "All of them"], a: 2, why: "Post-order outputs both subtrees before the node." },
  { q: "In the in-order procedure, the OUTPUT line is moved above both recursive calls. Which traversal is it now?", opts: ["In-order", "Pre-order", "Post-order", "It is no longer a traversal"], a: 1, why: "Node first, then left, then right is pre-order." },
  { q: "A tree has 9 nodes. How many calls does a traversal make, including those with a null pointer?", opts: ["9", "10", "18", "19"], a: 3, why: "2n + 1 = 19: nine real nodes plus ten null pointers." },
  { q: "Why is the stack for a traversal only as deep as the tree’s height, not the number of nodes?", opts: ["The stack is compressed", "Only one branch is active at a time: a subtree’s frames are popped before the next subtree starts", "Null pointers use no frames", "Recursion does not use a stack for trees"], a: 1, why: "Once the left subtree is finished all its frames have been popped, so the right subtree reuses the same space." },
  { q: "Which tree makes a recursive search slowest?", opts: ["A balanced tree", "A tree with values inserted in ascending order, forming a chain", "A tree with a single node", "A full tree"], a: 1, why: "A chain has height equal to the number of nodes, so the search may follow every node." }] });

Lib.cards($("#fc1"), { cards: [
  ["Binary tree", "A structure where each node has at most two children, a left child and a right child."],
  ["Subtree", "A node together with everything below it. Each subtree is itself a binary tree."],
  ["Root", "The top node, the only one that is not a child of another node."],
  ["Leaf", "A node with no children."],
  ["Null pointer", "A pointer value (such as 0) meaning ‘no child’. It is the base case of a traversal."],
  ["Traversal", "Visiting every node of a tree exactly once, in a defined order."],
  ["In-order", "Left subtree, node, right subtree. Ascending order for a binary search tree."],
  ["Pre-order", "Node, left subtree, right subtree. The root comes first."],
  ["Post-order", "Left subtree, right subtree, node. The root comes last."],
  ["Binary search tree", "A binary tree where every value in a node’s left subtree is smaller and every value in its right subtree is larger."],
  ["Height", "The number of levels in the tree. The recursion stack is about this deep."],
  ["Stack frame", "The block pushed on the call stack for each call: parameters, local variables and the return address."]] });
