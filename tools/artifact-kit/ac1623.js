const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

const bin = (n, w = 8) => n.toString(2).padStart(w, "0");
const hx = (n, w = 2) => n.toString(16).toUpperCase().padStart(w, "0");
const grp4 = (s) => s.replace(/(.{4})(?=.)/g, "$1 ");
const clamp01 = (v) => Math.max(0, Math.min(1, v));
/* row of boxes: items [{t, c, v}] t text, c fill class, v opacity */
function boxRow(items, x0, y, w = 64, h = 52, gap = 10, o = {}) {
  let s = "";
  items.forEach((it, i) => {
    const x = x0 + i * (w + gap), v = it.v === undefined ? 1 : it.v;
    if (v <= 0) return;
    s += SV.rect(x, y, w, h, it.c || "f3", { rx: 8, ...op(v * (it.c ? 0.55 : 0.18)) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) });
    s += SV.text(x + w / 2, y + h / 2 + 8, it.t, "lbl bd", { "text-anchor": "middle", style: "font-size:" + (o.fs || 22) + "px;font-family:var(--mono)", ...op(v) });
    if (it.top !== undefined) s += SV.text(x + w / 2, y - 8, it.top, "sm", { "text-anchor": "middle", ...op(v) });
    if (it.bot !== undefined) s += SV.text(x + w / 2, y + h + 18, it.bot, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return s;
}

/* memory cell: address on the left, value in the box */
function memCell(x, y, addr, val, cls = "f3", v = 1, w = 150, h = 40) {
  return SV.rect(x, y, w, h, cls, { rx: 6, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 6, fill: "none", ...op(v) }) +
    SV.text(x + 10, y + h / 2 + 6, String(addr), "sm", { style: "font-family:var(--mono)", ...op(v) }) +
    SV.text(x + w - 12, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono);font-size:17px", ...op(v) });
}
function regBox(x, y, name, val, cls = "f2", v = 1, w = 120, h = 46) {
  return SV.rect(x, y, w, h, cls, { rx: 8, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) }) +
    SV.text(x + 10, y - 7, name, "sm", op(v)) + SV.text(x + w / 2, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:19px", ...op(v) });
}
/* a list of code lines; hl is the highlighted index (or -1) */
function codeList(x, y, lines, hl, v = 1, lh = 30, w = 230) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 4, i === hl ? "cell-warn" : "cell", { rx: 4, ...op(v) }) + SV.text(x + 10, y + i * lh + 18, l, "lbl", { style: "font-family:var(--mono);font-size:14px;white-space:pre", ...op(v) })).join("");
}

const PREC = { "+": 1, "-": 1, "*": 2, "/": 2 };
const toks = (s) => (s.replace(/–/g, "-").match(/\d+(?:\.\d+)?|[A-Za-z]\w*|[()+\-*\/]/g) || []);
function toRpn(s) { const out = [], st = []; for (const t of toks(s)) { if (PREC[t]) { while (st.length && PREC[st[st.length - 1]] && PREC[st[st.length - 1]] >= PREC[t]) out.push(st.pop()); st.push(t); } else if (t === "(") st.push(t); else if (t === ")") { while (st[st.length - 1] !== "(") out.push(st.pop()); st.pop(); } else out.push(t); } return out.concat(st.reverse()); }
function toInfix(r) { const st = []; for (let t of r) { t = t.replace("–", "-"); if (PREC[t]) { const b = st.pop(), a = st.pop(); let ea = a[0], eb = b[0]; if (a[1] < PREC[t]) ea = "(" + ea + ")"; if (b[1] < PREC[t] || (b[1] === PREC[t] && (t === "-" || t === "/"))) eb = "(" + eb + ")"; st.push([ea + " " + t + " " + eb, PREC[t]]); } else st.push([t, 9]); } return st[0][0].replace(/-/g, "–"); }
function runRpn(r, env) { const st = [], trace = []; for (let t of r) { t = t.replace("–", "-"); if (PREC[t]) { const b = st.pop(), a = st.pop(); if (a === undefined || b === undefined) return { error: "The stack has too few values for the operator " + t, trace }; st.push(t === "+" ? a + b : t === "-" ? a - b : t === "*" ? a * b : a / b); } else { const v = env && t in env ? env[t] : Number(t); if (Number.isNaN(v)) return { error: "No value for " + t, trace }; st.push(v); } trace.push(st.slice()); } return { result: st[st.length - 1], left: st.length, trace }; }

function stackSvg(stack, x, yb, w, label) { let o = ""; stack.forEach((v, i) => (o += SV.rect(x, yb - (i + 1) * 36, w, 32, i === stack.length - 1 ? "cell-warn" : "cell", { rx: 4 }) + SV.text(x + w / 2, yb - (i + 1) * 36 + 22, String(v), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:" + (String(v).length > 12 ? 12 : 15) + "px" }))); return o + (label ? SV.text(x + w / 2, yb + 18, label, "sm", { "text-anchor": "middle" }) : ""); }
(function () {
  const r = "c a - b d + * b c + /".split(" "), env = { a: 4, b: 12, c: 24, d: 6 }, tr = runRpn(r, env).trace;
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "RPN (a = 4, b = 12, c = 24, d = 6)", "sm");
    r.forEach((t, i) => (o += SV.rect(20 + i * 52, 30, 46, 36, i === k - 1 ? "cell-warn" : i < k - 1 ? "cell-ok" : "cell", { rx: 6 }) + SV.text(43 + i * 52, 54, t.replace("-", "–"), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:16px" })));
    o += SV.text(20, 108, "stack", "lbl bd"); const st = k ? tr[k - 1] : []; o += stackSvg(st, 20, 220, 120, "") + SV.rect(20, 224, 120, 4, "ax", { fill: "var(--ink)" });
    if (k) { const t = r[k - 1]; let msg = "push " + (env[t] !== undefined ? t + " = " + env[t] : t); if (PREC[t.replace("–", "-")]) { const p = tr[k - 2], b = p[p.length - 1], a = p[p.length - 2]; msg = "pop " + b + " and " + a + ": " + a + " " + t.replace("-", "–") + " " + b + " = " + st[st.length - 1]; } o += SV.text(180, 190, msg, "lbl bd t3", { style: "font-size:14px" }); } return o; };
  Lib.stepper($("#stA"), { w: 620, h: 240, label: "Evaluating RPN", base: { i: 0 }, draw, tween: 100, dwell: 1900, steps: [{ cap: "The stack is empty. Read the expression from the left, one item at a time.", s: { i: 0 } }].concat(r.map((t, i) => ({ cap: PREC[t] ? `Operator <b>${t.replace("-", "–")}</b>: pop the last two values, apply it, push the result.` : `<b>${t}</b> is a value: push ${env[t]} on the stack.`, s: { i: i + 1 } }))) });
})();
(function () {
  const N = [{ t: "*", x: 300, y: 36 }, { t: "/", x: 200, y: 100 }, { t: "18", x: 400, y: 100 }, { t: "+", x: 120, y: 168 }, { t: "–", x: 280, y: 168 }, { t: "6", x: 80, y: 236 }, { t: "12", x: 160, y: 236 }, { t: "16", x: 240, y: 236 }, { t: "10", x: 320, y: 236 }];
  const E = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 5], [3, 6], [4, 7], [4, 8]]; const order = [5, 6, 3, 7, 8, 4, 1, 2, 0];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; E.forEach(([a, b]) => (o += SV.line(N[a].x, N[a].y, N[b].x, N[b].y, "edge")));
    N.forEach((n, i) => { const at = order.indexOf(i); o += SV.circle(n.x, n.y, 22, at < k ? (at === k - 1 ? "nd-cur" : "nd-ok") : "nd") + SV.text(n.x, n.y + 5, n.t, "lbl bd", { "text-anchor": "middle" }); });
    o += SV.text(20, 286, "RPN: " + order.slice(0, k).map((i) => N[i].t).join(" "), "lbl bd t3", { style: "font-family:var(--mono);font-size:15px" }); return o; };
  Lib.stepper($("#stB"), { w: 520, h: 300, label: "Expression tree", base: { i: 0 }, draw, tween: 100, dwell: 1900, steps: [{ cap: "The expression tree of ((6 + 12) / (16 – 10)) * 18: the operator that is done <b>last</b> is at the top. Read it with a post-order traversal: left, right, operator.", s: { i: 0 } }].concat([5, 6, 3, 7, 8, 4, 1, 2, 0].map((x, i) => ({ cap: ["6 is a leaf: output 6.", "12 is the next leaf: output 12.", "Both children of + are done, so output the operator <b>+</b>.", "16 on the right branch of /.", "10.", "Now the operator <b>–</b>.", "Both sides of / are done: output <b>/</b>.", "18, the right child of the top node.", "Finally the root: <b>*</b>. The RPN is <b>6 12 + 16 10 – / 18 *</b>."][i], s: { i: i + 1 } }))) });
})();
(function () {
  const r = "b a c - + d b + * c /".split(" "); const st = []; const frames = [[]]; r.forEach((t) => { const tt = t.replace("–", "-"); if (PREC[tt]) { const b = st.pop(), a = st.pop(); let ea = a[0], eb = b[0]; if (a[1] < PREC[tt]) ea = "(" + ea + ")"; if (b[1] < PREC[tt] || (b[1] === PREC[tt] && "-/".includes(tt))) eb = "(" + eb + ")"; st.push([ea + " " + t.replace("-", "–") + " " + eb, PREC[tt]]); } else st.push([t, 9]); frames.push(st.map((x) => x[0])); });
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "RPN: " + r.map((t) => t.replace("-", "–")).join(" "), "sm", { style: "font-family:var(--mono)" }); r.forEach((t, i) => (o += SV.rect(20 + i * 44, 30, 40, 32, i === k - 1 ? "cell-warn" : i < k - 1 ? "cell-ok" : "cell", { rx: 5 }) + SV.text(40 + i * 44, 51, t.replace("-", "–"), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" })));
    o += stackSvg(frames[k], 20, 240, 360, "stack of expressions"); return o; };
  Lib.stepper($("#stC"), { w: 530, h: 262, label: "RPN to infix", base: { i: 0 }, draw, tween: 100, dwell: 1900, steps: r.map((t, i) => ({ cap: PREC[t.replace("–", "-")] ? `Operator <b>${t.replace("-", "–")}</b>: pop two expressions, join them as <i>left ${t.replace("-", "–")} right</i> (adding brackets if needed) and push the result.` : `<b>${t}</b>: push it as an expression.`, s: { i: i + 1 } })).concat([{ cap: "One expression is left: <b>" + frames[r.length][0] + "</b>. That is the infix form.", s: { i: r.length } }]).slice(0, r.length + 1) });
})();

(function () {
  const inp = $("#eI"); const vars = { a: 4, b: 12, c: 24, d: 6 };
  const paint = () => { const r = inp.value.trim().split(/\s+/).filter(Boolean); const res = runRpn(r, vars); let h = "";
    if (res.trace && res.trace.length) { const depth = Math.max(...res.trace.map((s) => s.length)); h = '<div class="tw"><table class="t mono stk"><tr>' + r.slice(0, res.trace.length).map((t) => "<th>" + t.replace("-", "–") + "</th>").join("") + "</tr>"; for (let row = depth; row >= 1; row--) h += "<tr>" + res.trace.map((s) => "<td>" + (s.length >= row ? Math.round(s[row - 1] * 1000) / 1000 : "") + "</td>").join("") + "</tr>"; h += "</table></div>"; }
    $("#eV").innerHTML = '<p class="sm">Values: a = 4, b = 12, c = 24, d = 6.</p>'; $("#eO").innerHTML = h + `<div class="verdict">${res.error ? '<b style="color:var(--bad)">' + res.error + "</b>" : res.left !== 1 ? "The expression leaves " + res.left + " values on the stack, so it is not a complete RPN expression." : "Result: <b>" + Math.round(res.result * 1000) / 1000 + "</b>."}</div>`; };
  inp.oninput = paint; paint();
})();
(function () {
  const inp = $("#iI"); const paint = () => { try { const r = toRpn(inp.value); const v = runRpn(r, { a: 4, b: 12, c: 24, d: 6 }); $("#iO").innerHTML = "RPN: <b class='bx'>" + r.join(" ").replace(/-/g, "–") + "</b>" + (v.result !== undefined && !Number.isNaN(v.result) ? ". Value: <b>" + Math.round(v.result * 1000) / 1000 + "</b> (letters use a = 4, b = 12, c = 24, d = 6)." : ""); } catch (e) { $("#iO").textContent = "Check the brackets in the expression."; } };
  inp.oninput = paint; paint();
})();
(function () {
  const inp = $("#rI"); const paint = () => { const r = inp.value.trim().split(/\s+/).filter(Boolean); try { const res = runRpn(r, { a: 1, b: 1, c: 1, d: 1 }); if (res.error || res.left !== 1) throw 0; $("#rO").innerHTML = "Infix: <b class='bx'>" + toInfix(r) + "</b>"; } catch (e) { $("#rO").textContent = "That is not a complete RPN expression."; } };
  inp.oninput = paint; paint();
})();
Lib.classify($("#cl1"), { prompt: "Is the expression infix or RPN?", buckets: [{"label": "Infix"}, {"label": "RPN"}], items: [{"text": "3 + 4 * 2", "b": 0}, {"text": "3 4 2 * +", "b": 1}, {"text": "(a – b) * c", "b": 0}, {"text": "a b – c *", "b": 1}, {"text": "5 2 – 5 4 + * 9 /", "b": 1}, {"text": "(5 – 2) * (5 + 4) / 9", "b": 0}], done: "Operators between operands: infix. After operands: RPN." });
Lib.classify($("#cl2"), { prompt: "Is it a property of RPN?", buckets: [{"label": "Yes"}, {"label": "No"}], items: [{"text": "Evaluated left to right with a stack", "b": 0}, {"text": "Needs brackets", "b": 1}, {"text": "Needs rules of precedence", "b": 1}, {"text": "Unambiguous", "b": 0}, {"text": "The operator comes after its operands", "b": 0}, {"text": "The operator is between the operands", "b": 1}], done: "RPN: unambiguous, no brackets, no precedence." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["3 + 4 * 2", "3 4 2 * +"], ["(3 + 4) * 2", "3 4 + 2 *"], ["a * b + c", "a b * c +"], ["a * (b + c)", "a b c + *"], ["a – b – c", "a b – c –"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of evaluating RPN in order.", items: ["Read the next item from the left", "Push it on the stack if it is a value", "If it is an operator, pop the last two values", "Apply the operator and push the result", "When the expression ends, the value on the stack is the answer"], done: "Read, push, pop two, apply and push, finish." });
Lib.calc($("#c1"), { qs: [
  {"q": "Evaluate 6 2 / 4 * .", "a": 12, "unit": "", "tol": 0.01, "hint": "6 ÷ 2 = 3, then × 4.", "sol": "<b>12</b>."},
  {"q": "Evaluate 9 3 - 4 + 2 *.", "a": 20, "unit": "", "tol": 0.01, "hint": "6, 10, 20.", "sol": "<b>20</b>."},
  {"q": "Evaluate 15 3 5 + / .", "a": 1.875, "unit": "", "tol": 0.001, "hint": "3 + 5 = 8, then 15 ÷ 8.", "sol": "<b>1.875</b>."},
  {"q": "How many values are on the stack after reading a b c in a b c + *?", "a": 3, "unit": "", "tol": 0.01, "hint": "Three pushes.", "sol": "<b>3</b>."},
  {"q": "What is the deepest the stack gets when evaluating 6 12 + 16 10 - / 18 * ?", "a": 3, "unit": "", "tol": 0.01, "hint": "After 6 12 + 16 10 there are 3 values.", "sol": "<b>3</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is 4 5 + 2 * ?", opts: ["14", "18", "13", "40"], a: 1, why: "(4 + 5) × 2 = 18." },
  { q: "Which data structure evaluates RPN?", opts: ["Queue", "Stack", "Array only", "Linked list"], a: 1, why: "A stack." },
  { q: "In RPN the operator comes:", opts: ["Before the operands", "Between the operands", "After the operands", "At random"], a: 2, why: "After." },
  { q: "5 2 - with the stack: the left operand is:", opts: ["The first popped", "The second popped", "Always 0", "The operator"], a: 1, why: "The second popped, 5." },
  { q: "RPN needs:", opts: ["Brackets", "Precedence rules", "Neither", "Both"], a: 2, why: "Neither." },
  { q: "The infix of a b + c * is:", opts: ["a + b * c", "(a + b) * c", "a + (b * c)", "a * b + c"], a: 1, why: "(a + b) * c." },
] });
Lib.cards($("#fc1"), { cards: [
  ["RPN", "Operators after operands: 3 4 +."],
  ["Why RPN", "Unambiguous, left to right, no brackets, no precedence."],
  ["Evaluate", "Push values; operator pops two, applies, pushes."],
  ["Operand order", "Second popped is the left operand."],
  ["Infix to RPN", "Operand operand operator for each operation, in order."],
  ["RPN to infix", "Stack of expressions; add brackets where needed."],
  ["Tree", "Post-order traversal gives RPN."],
  ["Stack table", "Show the stack after every item."],
] });
