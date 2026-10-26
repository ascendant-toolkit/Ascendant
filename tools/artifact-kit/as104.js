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

(function () {
  const draw = (s) => { const k = Math.round(s.i); const seq = [[], ["A"], ["A", "B"], ["A", "B", "C"], ["A", "B"], ["A"]]; const st = seq[k]; let o = ""; for (let i = 0; i < 5; i++) { const v = st[i]; o += SV.rect(30, 12 + (4 - i) * 26, 90, 24, v ? "f3" : "cell", { rx: 4 }) + SV.text(36, 29 + (4 - i) * 26, i + 1, "sm") + SV.text(75, 29 + (4 - i) * 26, v || "", "lbl bd", { "text-anchor": "middle" }); } if (st.length) o += SV.text(135, 29 + (5 - st.length) * 26, "← top of stack", "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stA"), { w: 330, h: 150, label: "Stack", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["The stack is empty.", "PUSH A.", "PUSH B.", "PUSH C.", "POP removes C: the last in is the first out.", "POP removes B."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const S = [{ q: [], f: 0, e: -1 }, { q: [[0, "Ann"]], f: 0, e: 0 }, { q: [[0, "Ann"], [1, "Bo"]], f: 0, e: 1 }, { q: [[0, "Ann"], [1, "Bo"], [2, "Cy"]], f: 0, e: 2 }, { q: [[1, "Bo"], [2, "Cy"]], f: 1, e: 2 }, { q: [[1, "Bo"], [2, "Cy"], [3, "Di"]], f: 1, e: 3 }];
  const draw = (s) => { const k = Math.round(s.i); const st = S[k]; let o = ""; for (let i = 0; i < 4; i++) { const it = st.q.find((x) => x[0] === i); o += SV.rect(30, 12 + i * 26, 90, 24, it ? "f3" : "cell", { rx: 4 }) + SV.text(36, 29 + i * 26, i, "sm") + SV.text(75, 29 + i * 26, it ? it[1] : "", "lbl bd", { "text-anchor": "middle" }); } if (st.q.length) { o += SV.text(135, 29 + st.f * 26, "← front", "lbl bd t3", { style: "font-size:12px" }); o += SV.text(135, 45 + st.e * 26, "← end", "lbl bd t2", { style: "font-size:12px" }); } return o; };
  Lib.stepper($("#stB"), { w: 330, h: 125, label: "Queue", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["An empty queue.", "Add Ann.", "Add Bo.", "Add Cy.", "Remove: Ann leaves first (FIFO) and the front moves on.", "Add Di at the end."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const rows = [["D40", "→ D32"], ["D32", "→ D11"], ["D11", "→ D100"], ["D100", "→ Ø"]];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; const L = k < 2 ? ["D40", "D32", "D11", "D100"] : k < 3 ? ["D40", "D32", "D11", "D100"] : ["D40", "D32", "D6", "D11", "D100"]; if (k >= 3) {} L.forEach((d, i) => { o += SV.rect(20 + i * 80, 30, 60, 28, d === "D6" ? "f3" : "cell", { rx: 5 }) + SV.text(50 + i * 80, 49, d, "lbl bd", { "text-anchor": "middle" }) + (i < L.length - 1 ? SV.text(82 + i * 80, 48, "→", "lbl") : SV.text(82 + i * 80, 48, "Ø", "lbl")); }); o += SV.text(20, 16, "Ptr1 (start)", "sm"); o += SV.text(20, 90, "Free list: " + (k < 3 ? "F1 → F2 → F3 → F4 → Ø" : "F2 → F3 → F4 → Ø  (F1 now holds D6)"), "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stC"), { w: 480, h: 105, label: "Insert", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["Insert D6 between D32 and D11.", "Take the first free node (F1) and store D6 in it.", "Set its pointer to D11, then Ptr2 moves to F2.", "Set the pointer of D32 to D6: the list is in order, no data moved."].map((c, i) => ({ cap: c, s: { i: i === 0 ? 0 : i === 1 ? 1 : i === 2 ? 2 : 3 } })) });
})();

(function () {
  let st, nxt; const abc = "PQRSTUVWXYZ".split(""); const reset = () => { st = []; nxt = 0; paint("Empty stack. TopOfStack is not pointing at anything."); };
  const paint = (m) => { let h = '<div class="tw"><table class="t mono"><tr><th>location</th><th>value</th><th>pointer</th></tr>'; for (let a = 200; a <= 207; a++) { const idx = 207 - a; const v = st[idx]; h += `<tr><td>${a}</td><td>${v ? "'" + v + "'" : ""}</td><td>${idx === st.length - 1 && v ? "TopOfStack" : ""}</td></tr>`; } $("#skV").innerHTML = h + `</table></div><div class="verdict">${m}</div>`; };
  $("#sk_push").onclick = () => { if (st.length === 8) return paint("Stack full: PUSH refused (overflow)."); const c = abc[nxt++ % abc.length]; st.push(c); paint(`PUSH '${c}': stored at ${208 - st.length}. The stack grows towards 200.`); };
  $("#sk_pop").onclick = () => { if (!st.length) return paint("Stack empty: POP refused (underflow)."); const c = st.pop(); paint(`POP returns '${c}', the last value added. TopOfStack moves back up.`); }; $("#sk_reset").onclick = reset; reset();
})();
(function () {
  let q, f, e, n, c; const reset = () => { q = Array(8).fill(""); f = 0; e = -1; n = 0; c = 0; paint("Empty queue."); };
  const paint = (m) => { let h = '<div class="tw"><table class="t mono"><tr><th>loc</th><th>value</th><th>pointer</th></tr>'; for (let i = 0; i < 8; i++) { const live = n > 0 && ((f <= e) ? i >= f && i <= e : i >= f || i <= e); h += `<tr><td>${i}</td><td style="${live ? "" : "opacity:.4"}">${q[i]}</td><td>${n && i === f ? "front " : ""}${n && i === e ? "end" : ""}</td></tr>`; } $("#quV").innerHTML = h + `</table></div><div class="verdict">${m} Items: <b>${n}</b>.</div>`; };
  $("#qu_add").onclick = () => { if (n === 8) return paint("Queue full: add refused."); e = (e + 1) % 8; q[e] = "item" + (++c); n++; paint(`End pointer moves to ${e}${e === 0 && c > 1 ? " (wrapped round)" : ""} and stores ${q[e]}.`); };
  $("#qu_rem").onclick = () => { if (!n) return paint("Queue empty: remove refused."); const v = q[f]; f = (f + 1) % 8; n--; paint(`Removed ${v} from the front. Front moves to ${f}. The old value stays in the array but is no longer in the queue (faded).`); }; $("#qu_reset").onclick = reset; reset();
})();
(function () {
  let D, P, S, F, hist; const N = 8; const reset = () => { D = Array(N + 1).fill(""); P = Array(N + 1).fill(0); for (let i = 1; i < N; i++) P[i] = i + 1; P[N] = 0; S = 0; F = 1; hist = []; paint("All 8 nodes are on the free list; the start pointer is null (0)."); };
  const paint = (m) => { let h = `<p class="mono">Start_Pointer = ${S || "0 (null)"} &nbsp; Free_List_Pointer = ${F || "0 (null: list full)"}</p><div class="tw"><table class="t mono"><tr><th>index</th><th>Data</th><th>Pointer</th></tr>`; for (let i = 1; i <= N; i++) h += `<tr><td>${i}</td><td>${D[i]}</td><td>${P[i] || "0"}</td></tr>`; const chain = []; for (let p = S; p; p = P[p]) chain.push(D[p]); $("#llV").innerHTML = h + `</table></div><div class="verdict">List in order: <b>${chain.length ? chain.join(" → ") + " → Ø" : "empty"}</b>. ${m}</div>`; };
  const bar = $("#llB"); ["mango", "apple", "pear", "fig", "kiwi", "banana"].forEach((w) => { const b = document.createElement("button"); b.textContent = "Insert " + w; b.onclick = () => { if (!F) return paint("No free node left."); const nn = F; F = P[nn]; D[nn] = w; let prev = 0, p = S; while (p && D[p] < w) { prev = p; p = P[p]; } P[nn] = p; if (prev) P[prev] = nn; else S = nn; hist.push(w); paint(`Took node ${nn} from the free list, stored "${w}" and changed pointers only. No data moved.`); }; bar.appendChild(b); });
  $("#ll_del").onclick = () => { if (!hist.length) return paint("Nothing to delete."); const w = hist.pop(); let prev = 0, p = S; while (p && D[p] !== w) { prev = p; p = P[p]; } if (!p) return paint(""); if (prev) P[prev] = P[p]; else S = P[p]; D[p] = ""; P[p] = F; F = p; paint(`Deleted "${w}": the previous pointer skips node ${p}, which joins the free list.`); }; $("#ll_reset").onclick = reset; reset();
})();
Lib.classify($("#cl1"), { prompt: "Which ADT is described?", buckets: [{"label": "Stack"}, {"label": "Queue"}, {"label": "Linked list"}], items: [{"text": "Last in, first out", "b": 0}, {"text": "First in, first out", "b": 1}, {"text": "Each node has a pointer to the next node", "b": 2}, {"text": "Browser Back button history", "b": 0}, {"text": "Print jobs waiting for a printer", "b": 1}, {"text": "Items can be inserted by changing pointers only", "b": 2}], done: "LIFO stack; FIFO queue; pointers linked list." });
Lib.classify($("#cl2"), { prompt: "Which pointer or term?", buckets: [{"label": "Start pointer"}, {"label": "Null pointer"}, {"label": "Free list pointer"}], items: [{"text": "Points to the first node in the list", "b": 0}, {"text": "Marks the end of the list (Ø)", "b": 1}, {"text": "Points to the first unused node", "b": 2}, {"text": "The value 0 when array indices are 1 to 8", "b": 1}, {"text": "After initialisation it points to the first node", "b": 2}, {"text": "Is null when the list is empty", "b": 0}], done: "Start first; null end; free unused." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["PUSH", "Add to the top of a stack"], ["POP", "Remove from the top of a stack"], ["Front pointer", "Next item to be removed from a queue"], ["End pointer", "Last item added to a queue"], ["Node", "A data item with a pointer"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for adding to a circular queue in order.", items: ["Check the queue is not full", "Increment the end pointer", "If past the last location, set it to the first (wrap round)", "Store the item at the end pointer", "Increment the count of items"], done: "Check, move, wrap, store, count." });
Lib.calc($("#c1"), { qs: [
  {"q": "Stack at 200 to 207; TOS points to 203. Three POPs are done. Which location does TOS point to afterwards? (The stack grows downwards in memory, so a POP raises the address.)", "a": 206, "unit": "", "tol": 0.01, "hint": "203 + 3.", "sol": "<b>206</b>."},
  {"q": "A queue of 10 locations has the front pointer at 5 and the end pointer at 1 (wrapped). How many items?", "a": 7, "unit": "", "tol": 0.01, "hint": "5 to 9 is 5; 0 to 1 is 2.", "sol": "<b>7</b>."},
  {"q": "A stack array holds 60 values. After 25 pushes and 9 pops, how many values are on the stack?", "a": 16, "unit": "", "tol": 0.01, "hint": "25 − 9.", "sol": "<b>16</b>."},
  {"q": "A stack grows up from index 1. SP points to the next free place. After 12 pushes, what is SP?", "a": 13, "unit": "", "tol": 0.01, "hint": "1 + 12.", "sol": "<b>13</b>."},
  {"q": "A linked list has 8 nodes. After initialisation, how many nodes are on the free list?", "a": 8, "unit": "", "tol": 0.01, "hint": "All of them.", "sol": "<b>8</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The next item out of a stack is:", opts: ["The last one pushed", "The first one pushed", "A random one", "The largest"], a: 0, why: "LIFO." },
  { q: "A queue works on:", opts: ["FIFO", "LIFO", "Random order", "Alphabetical order"], a: 0, why: "FIFO." },
  { q: "In a circular queue, the end pointer after the last location goes to:", opts: ["The first location", "The front pointer", "Null", "Zero items"], a: 0, why: "Wraps." },
  { q: "In a linked list the last node holds:", opts: ["A null pointer", "The start pointer", "The free list", "No data"], a: 0, why: "Null." },
  { q: "A disadvantage of a linked list compared with an array is:", opts: ["It stores extra pointers", "Insertion needs data to move", "It cannot hold strings", "It is always full"], a: 0, why: "Pointers need memory." },
  { q: "Front and end pointers are equal. The queue holds:", opts: ["One item", "No items", "A full queue", "Two items"], a: 0, why: "One." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Stack", "LIFO. PUSH, POP, top of stack."],
  ["Queue", "FIFO. Front and end pointers."],
  ["Circular", "Wraps round to reuse locations."],
  ["Node", "Data and a pointer."],
  ["Start pointer", "First node."],
  ["Null pointer", "End of list (Ø)."],
  ["Free list", "The unused nodes."],
  ["Full / empty", "Check before add / remove."],
] });
