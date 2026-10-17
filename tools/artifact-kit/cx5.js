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

function chainDraw(nodes, k) {
  const H = 40, G = 16; let o = "";
  nodes.forEach((t, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const y = 8 + i * (H + G);
    o += SV.rect(30, y, 700, H, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.55 * v) }) + SV.text(380, y + 25, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
    if (i > 0) o += SV.poly([[373, y - 10], [387, y - 10], [380, y - 2]], "dot4", op(v));
  });
  return o;
}
function chainStep(el, label, nodes, caps) {
  Lib.stepper($(el), { w: 760, h: 16 + nodes.length * 56, label, base: { k: 0 }, draw: (s) => chainDraw(nodes, s.k), tween: 700, dwell: 5200, steps: nodes.map((n, i) => ({ cap: caps[i], s: { k: i + 1 } })) });
}
function chooser(p, items, tmpl, lab = "Strength of the case") {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, lab + ": " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}

function pick(id, items, render) {
  const B = $("#" + id + "B"), O = $("#" + id + "O");
  B.innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t.label}</button>`).join("");
  const show = (i) => { $$("button", B).forEach((b, k) => b.classList.toggle("pri", k === i)); O.innerHTML = render(items[i]); };
  $$("button", B).forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}
const scoreBar = (m, max) => `<div style="background:var(--soft);border-radius:7px;height:14px;margin:6px 0 2px"><div class="bar ${m === max ? "b3" : m === 0 ? "b2" : "b4"}" style="width:${Math.max(2, (m / max) * 100)}%"></div></div><small>${m} of ${max} marks</small>`;

function ttHtml(names, out, f, hl = {}) {
  const n = names.length, rows = [];
  for (let i = 0; i < 1 << n; i++) { const v = names.map((_, k) => (i >> (n - 1 - k)) & 1); rows.push(v.concat(f(...v) ? 1 : 0)); }
  return `<div class="tw"><table class="t mx"><tr>${names.concat(out).map((h) => `<th>${h}</th>`).join("")}</tr>${rows.map((r, i) => `<tr>${r.map((c, k) => `<td class="${k === n ? (c ? "on" : "z") : ""}">${c}</td>`).join("")}</tr>`).join("")}</table></div>`;
}
function ttRows(names, f) {
  const n = names.length, rows = [];
  for (let i = 0; i < 1 << n; i++) { const v = names.map((_, k) => (i >> (n - 1 - k)) & 1); rows.push(f(...v) ? 1 : 0); }
  return rows;
}

/* ---- gate symbols and circuits ---- */
const GW = 56, GH = 44;
function gateSvg(t, x, y, v = 1) {
  const m = y + GH / 2, st = `fill:var(--soft);stroke:var(--ink);stroke-width:2;opacity:${v}`, ns = `fill:none;stroke:var(--ink);stroke-width:2;opacity:${v}`;
  let d, out = x + GW, extra = "";
  if (t === "AND" || t === "NAND") d = `M${x},${y} L${x + GW / 2},${y} A${GW / 2},${GH / 2} 0 0 1 ${x + GW / 2},${y + GH} L${x},${y + GH} Z`;
  else if (t === "NOT") d = `M${x},${y} L${x + GW - 9},${m} L${x},${y + GH} Z`;
  else d = `M${x},${y} Q${x + GW * 0.5},${y} ${x + GW},${m} Q${x + GW * 0.5},${y + GH} ${x},${y + GH} Q${x + GW * 0.3},${m} ${x},${y} Z`;
  if (t === "XOR") extra += `<path d="M${x - 8},${y} Q${x + GW * 0.3 - 8},${m} ${x - 8},${y + GH}" style="${ns}"/>`;
  if (t === "NAND" || t === "NOR" || t === "NOT") { const cx = t === "NOT" ? x + GW - 4 : x + GW + 5; extra += `<circle cx="${cx}" cy="${m}" r="5" style="fill:var(--surface);stroke:var(--ink);stroke-width:2;opacity:${v}"/>`; out = cx + 5; }
  return { t, svg: `<path d="${d}" style="${st}"/>${extra}` + SV.text(x + GW / 2, y + GH + 15, t, "sm", { "text-anchor": "middle", ...op(v) }), out: [out, m], in1: [x, t === "NOT" ? m : y + GH * 0.27], in2: [x, y + GH * 0.73] };
}
const wire = (pts, v = 1) => `<polyline points="${pts.map((p) => p.join(",")).join(" ")}" style="fill:none;stroke:var(--ink);stroke-width:2;opacity:${v}"/>`;
const dot = (x, y, v = 1) => `<circle cx="${x}" cy="${y}" r="3.5" style="fill:var(--ink);opacity:${v}"/>`;
function circuit(id) {
  const g = (t, x, y) => gateSvg(t, x, y);
  if (id === 1) {
    const n = g("NOT", 110, 18), o = g("OR", 235, 50), x = g("XOR", 235, 130), a = g("NAND", 370, 90);
    return { w: 540, h: 215, ins: [["P", 40], ["Q", 100], ["R", 170]], out: "X", parts: [n, o, x, a], dots: [[190, 100]], wires: [
      { p: [[50, 40], n.in1], need: [0] }, { p: [n.out, [205, n.out[1]], [205, o.in1[1]], o.in1], need: [0, 1] },
      { p: [[50, 100], [190, 100]], any: [1, 2] }, { p: [[190, 100], [210, 100], [210, o.in2[1]], o.in2], need: [1] }, { p: [[190, 100], [190, x.in1[1]], x.in1], need: [2] },
      { p: [[50, 170], [215, 170], [215, x.in2[1]], x.in2], need: [2] }, { p: [o.out, [335, o.out[1]], [335, a.in1[1]], a.in1], need: [1, 3] }, { p: [x.out, [350, x.out[1]], [350, a.in2[1]], a.in2], need: [2, 3] }, { p: [a.out, [500, a.out[1]]], need: [3] }],
      f: (p, q, r) => 1 - (((1 - p) | q) & (q ^ r)), names: ["P", "Q", "R"], expr: "X = (NOT P OR Q) NAND (Q XOR R)", src: "Oct/Nov 2024, paper 22, Q9" };
  }
  if (id === 2) {
    const n = g("NOT", 110, 18), x = g("XOR", 110, 125), o = g("OR", 260, 70);
    return { w: 480, h: 215, ins: [["X", 40], ["Y", 110], ["Z", 170]], out: "W", parts: [n, x, o], dots: [], wires: [
      { p: [[50, 40], n.in1], need: [0] }, { p: [n.out, [225, n.out[1]], [225, o.in1[1]], o.in1], need: [0, 2] }, { p: [[50, 110], [90, 110], [90, x.in1[1]], x.in1], need: [1] },
      { p: [[50, 170], [100, 170], [100, x.in2[1]], x.in2], need: [1] }, { p: [x.out, [235, x.out[1]], [235, o.in2[1]], o.in2], need: [1, 2] }, { p: [o.out, [430, o.out[1]]], need: [2] }],
      f: (x, y, z) => (1 - x) | (y ^ z), names: ["X", "Y", "Z"], expr: "W = NOT X OR (Y XOR Z)", src: "Oct/Nov 2024, paper 21, Q7" };
  }
  const n1 = g("NOT", 100, 18), a = g("AND", 230, 50), n2 = g("NOT", 100, 148), o = g("OR", 370, 100);
  return { w: 520, h: 215, ins: [["A", 40], ["B", 100], ["C", 170]], out: "X", parts: [n1, a, n2, o], dots: [], wires: [
    { p: [[50, 40], n1.in1], need: [0] }, { p: [n1.out, [195, n1.out[1]], [195, a.in1[1]], a.in1], need: [0, 1] }, { p: [[50, 100], [210, 100], [210, a.in2[1]], a.in2], need: [1] },
    { p: [[50, 170], n2.in1], need: [2] }, { p: [a.out, [335, a.out[1]], [335, o.in1[1]], o.in1], need: [1, 3] }, { p: [n2.out, [350, n2.out[1]], [350, o.in2[1]], o.in2], need: [2, 3] }, { p: [o.out, [480, o.out[1]]], need: [3] }],
    f: (a_, b, c) => ((1 - a_) & b) | (1 - c), names: ["A", "B", "C"], expr: "X = (NOT A AND B) OR NOT C", src: "Oct/Nov 2023, paper 21, Q7" };
}
function circuitSvg(c, k) {
  const vis = (i) => i < k; let o = "";
  c.ins.forEach(([n, y]) => (o += SV.text(24, y + 5, n, "lbl bd", { "text-anchor": "middle" })));
  c.parts.forEach((p, i) => { if (vis(i)) o += p.svg; });
  c.wires.forEach((w) => { const ok = w.need ? w.need.every(vis) : w.any.some(vis); if (ok) o += wire(w.p); });
  c.dots.forEach(([x, y]) => { if (vis(1) && vis(2)) o += dot(x, y); });
  if (k >= c.parts.length) o += SV.text(c.wires[c.wires.length - 1].p[1][0] + 12, c.wires[c.wires.length - 1].p[1][1] + 5, c.out, "lbl bd");
  return o;
}
const C1 = circuit(1);
Lib.stepper($("#stA"), { w: C1.w, h: C1.h, label: "Building a circuit for X = (NOT P OR Q) NAND (Q XOR R)", base: { k: 0 }, draw: (s) => circuitSvg(C1, Math.round(s.k)), tween: 200, dwell: 4500, steps: [
  { cap: "<b>Innermost bracket first.</b> NOT P is the first gate: one input, with a small circle on the output.", s: { k: 1 } },
  { cap: "<b>OR gate.</b> Its inputs are the output of the NOT gate and Q. This completes (NOT P OR Q).", s: { k: 2 } },
  { cap: "<b>XOR gate.</b> Its inputs are Q and R. Q has two uses, so its line branches, shown with a dot.", s: { k: 3 } },
  { cap: "<b>NAND gate.</b> It joins the OR output and the XOR output, and gives X. The circle on the output is the NOT of AND.", s: { k: 4 } }
] });

/* ---- truth table stepper ---- */
const TT = { heads: ["P", "Q", "R", "NOT P", "NOT P OR Q", "Q XOR R", "X"], f: [null, null, null, (p) => 1 - p, (p, q) => (1 - p) | q, (p, q, r) => q ^ r, (p, q, r) => 1 - (((1 - p) | q) & (q ^ r))] };
function ttDrawSvg(k) {
  const W = [50, 50, 50, 90, 140, 110, 70], rows = [];
  for (let i = 0; i < 8; i++) rows.push([(i >> 2) & 1, (i >> 1) & 1, i & 1]);
  let o = "", x = 40;
  TT.heads.forEach((h, c) => {
    const v = Math.max(0, Math.min(1, k - c)); if (v > 0) {
      o += SV.rect(x, 12, W[c] - 4, 28, c === 6 ? "f1" : c > 2 ? "f2" : "f3", { rx: 5, ...op(0.5 * v) }) + SV.text(x + (W[c] - 4) / 2, 31, h, "lbl bd", { "text-anchor": "middle", style: "font-size:12.5px", ...op(v) });
      rows.forEach((r, i) => { const val = c < 3 ? r[c] : TT.f[c](...r); o += SV.text(x + (W[c] - 4) / 2, 64 + i * 26, val, "lbl bd", { "text-anchor": "middle", style: "font-size:15px;font-family:var(--mono)" + (c === 6 ? ";fill:var(--accent)" : ""), ...op(v) }); });
    }
    x += W[c];
  });
  return o;
}
Lib.stepper($("#stB"), { w: 640, h: 280, label: "Completing a truth table column by column", base: { k: 0 }, draw: (s) => ttDrawSvg(s.k), tween: 500, dwell: 4500, steps: [
  { cap: "<b>Inputs.</b> Three inputs give eight rows, counted in binary from 000 to 111.", s: { k: 3 } },
  { cap: "<b>NOT P.</b> The first working column: the opposite of P in every row.", s: { k: 4 } },
  { cap: "<b>NOT P OR Q.</b> 1 when NOT P is 1 or Q is 1.", s: { k: 5 } },
  { cap: "<b>Q XOR R.</b> 1 when Q and R are different.", s: { k: 6 } },
  { cap: "<b>X.</b> NAND of the two brackets: 0 only when both brackets are 1. Eight outputs: four marks if all are right.", s: { k: 7 } }
] });

chainStep("#stC", "Reading SELECT Name, Quantity FROM InstrumentStock WHERE SupplierCode = \"BRS\" AND InStock ORDER BY Quantity", ["FROM: use the table InstrumentStock", "WHERE: both conditions must be true, so Trumpet and Tuba are kept and Trombone is dropped because it is out of stock", "ORDER BY: put them in order of Quantity, lowest first: Tuba, then Trumpet", "SELECT: show only Name and Quantity, in that order: Tuba 2, then Trumpet 5"], [
  "<b>FROM:</b> find the table.", "<b>WHERE:</b> both conditions must be true for AND. Trombone fails InStock.", "<b>ORDER BY:</b> ascending is the default.", "<b>SELECT:</b> write only these fields, with no punctuation."]);

/* ---- circuits lab ---- */
pick("ci", [1, 2, 3].map((n) => ({ label: "Circuit " + n, c: circuit(n) })), (it) => {
  const c = it.c;
  return `<div class="grid2"><div><svg viewBox="0 0 ${c.w} ${c.h}" role="img" aria-label="${c.expr}" style="max-width:100%">${circuitSvg(c, c.parts.length)}</svg></div><div>${ttHtml(c.names, c.out, c.f)}</div></div><p><code>${c.expr}</code> <small>(${c.src})</small></p>`;
});

function tm() {
  const n = +$("#tc").value, m = n === 8 ? 4 : n >= 6 ? 3 : n >= 4 ? 2 : n >= 2 ? 1 : 0;
  $("#r1").textContent = n + " of 8"; $("#r2").textContent = m;
  $("#rv").textContent = n === 8 ? "All eight right: full marks." : n >= 6 ? "Six or seven right: 3 marks. Check the NAND or NOR last step for the row that is wrong." : n >= 4 ? "Four or five right: 2 marks." : n >= 2 ? "Two or three right: 1 mark. Re-do the working columns." : "Fewer than two right: no mark.";
  let o = ""; for (let i = 0; i < 8; i++) o += SV.rect(30 + i * 46, 100, 38, 38, i < n ? "f3" : "f2", { rx: 6, ...op(0.6) }) + SV.text(49 + i * 46, 125, i < n ? "✓" : "✗", "lbl bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o + SV.text(210, 80, "Marks: " + m + " out of 4", "lbl bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "tc", label: "Correct outputs ", min: 0, max: 8, step: 1, value: 6, fmt: (v) => v, onInput: tm });
tm();

/* ---- SQL lab ---- */
const IS = [["IN01", "Violin", "Yes", "MUS", 120.00, 14], ["IN02", "Viola", "Yes", "MUS", 135.50, 6], ["IN03", "Cello", "No", "ORC", 310.00, 0], ["IN04", "Flute", "Yes", "WND", 95.00, 22], ["IN05", "Oboe", "No", "WND", 480.00, 0],
  ["IN06", "Clarinet", "Yes", "WND", 150.00, 9], ["IN07", "Trumpet", "Yes", "BRS", 210.00, 5], ["IN08", "Trombone", "No", "BRS", 275.00, 0], ["IN09", "Tuba", "Yes", "BRS", 640.00, 2], ["IN10", "Piccolo", "Yes", "WND", 88.50, 11]];
const COLS = ["ItemNo", "Name", "InStock", "SupplierCode", "Price", "Quantity"];
const SQ = [
  { label: "WHERE text", sql: ["SELECT ItemNo, Name", "FROM InstrumentStock", 'WHERE SupplierCode = "WND";'], cols: [0, 1], where: (r) => r[3] === "WND" },
  { label: "WHERE NOT (Boolean)", sql: ["SELECT Name", "FROM InstrumentStock", "WHERE NOT InStock;"], cols: [1], where: (r) => r[2] === "No" },
  { label: "ORDER BY", sql: ["SELECT ItemNo, Name, Price", "FROM InstrumentStock", "WHERE Price > 200", "ORDER BY Price;"], cols: [0, 1, 4], where: (r) => r[4] > 200, order: [4, 1] },
  { label: "AND", sql: ["SELECT Name", "FROM InstrumentStock", 'WHERE SupplierCode = "BRS" AND InStock;'], cols: [1], where: (r) => r[3] === "BRS" && r[2] === "Yes" },
  { label: "OR with DESC", sql: ["SELECT Name, Quantity", "FROM InstrumentStock", 'WHERE SupplierCode = "MUS" OR Quantity > 10', "ORDER BY Quantity DESC;"], cols: [1, 5], where: (r) => r[3] === "MUS" || r[5] > 10, order: [5, -1] },
  { label: "SUM", sql: ["SELECT SUM(Quantity)", "FROM InstrumentStock", 'WHERE SupplierCode = "WND";'], agg: "sum", where: (r) => r[3] === "WND" },
  { label: "COUNT", sql: ["SELECT COUNT(ItemNo)", "FROM InstrumentStock", "WHERE Price < 150;"], agg: "count", where: (r) => r[4] < 150 }
];
pick("sq", SQ, (q) => {
  const hit = IS.filter(q.where); let rows = hit.slice();
  if (q.order) rows.sort((a, b) => (q.order[1] === -1 ? b[q.order[0]] - a[q.order[0]] : q.order[1] === 1 ? (a[q.order[0]] < b[q.order[0]] ? -1 : 1) : a[q.order[0]] - b[q.order[0]]));
  const fmt = (r, c) => (c === 4 ? r[c].toFixed(2) : r[c]);
  const outLines = q.agg ? [q.agg === "sum" ? hit.reduce((s, r) => s + r[5], 0) : hit.length] : rows.map((r) => q.cols.map((c) => fmt(r, c)).join(" "));
  const tb = `<div class="tw"><table class="t mx"><tr>${COLS.map((c) => `<th>${c}</th>`).join("")}</tr>${IS.map((r) => `<tr>${r.map((v, i) => `<td class="${q.where(r) ? "on" : "z"}">${i === 4 ? v.toFixed(2) : v}</td>`).join("")}</tr>`).join("")}</table></div>`;
  return `<div class="formula" style="white-space:pre">${q.sql.join("\n")}</div>${tb}<p><b>Output</b> (no punctuation, ${q.order ? "in the ORDER BY order" : "in table order"}):</p><div class="formula" style="white-space:pre">${outLines.join("\n") || "(no records)"}</div><p>${hit.length} record${hit.length === 1 ? "" : "s"} match the WHERE condition. ${q.agg ? "SUM adds the values; COUNT counts the records." : "Only the SELECT fields are written, in the order SELECT lists them."}</p>`;
});
Lib.classify($("#cl1"), { prompt: "Which gate is it?", buckets: [{"label": "NOT"}, {"label": "AND"}, {"label": "OR"}, {"label": "NAND"}, {"label": "NOR"}, {"label": "XOR"}], items: [{"text": "Reverses a single input", "b": 0}, {"text": "Gives 1 only when both inputs are 1", "b": 1}, {"text": "Gives 1 when at least one input is 1", "b": 2}, {"text": "Gives 0 only when both inputs are 1", "b": 3}, {"text": "Gives 1 only when both inputs are 0", "b": 4}, {"text": "Gives 1 when the two inputs are different", "b": 5}, {"text": "Output is 1 for inputs 11, and 0 for inputs 00", "b": 1}, {"text": "Output is 0 for inputs 11 and 1 for inputs 01", "b": 3}, {"text": "Output is 1 for inputs 01 and 0 for inputs 11", "b": 5}], done: "NAND and NOR are the NOT of AND and OR. XOR needs the inputs to differ." });
Lib.classify($("#cl2"), { prompt: "Which data type suits each field?", buckets: [{"label": "Text or alphanumeric"}, {"label": "Character"}, {"label": "Boolean"}, {"label": "Integer"}, {"label": "Real"}, {"label": "Date/time"}], items: [{"text": "A book code such as LB204", "b": 0}, {"text": "A single grade letter", "b": 1}, {"text": "Hardback: yes or no", "b": 2}, {"text": "Number of copies in stock", "b": 3}, {"text": "A price such as 8.50", "b": 4}, {"text": "The date a song was recorded", "b": 5}, {"text": "A weight such as 20.5 kg", "b": 4}, {"text": "A person's name", "b": 0}, {"text": "InStock", "b": 2}], done: "Choose by what is stored: whole numbers are integers, numbers with a fractional part are real, yes or no is Boolean." });
Lib.order($("#o1"), { prompt: "Put the reading of an SQL statement in the order the computer does it.", items: ["FROM: find the table", "WHERE: keep the rows that match", "ORDER BY: sort the rows if asked", "SELECT: show only the fields listed, in that order"], done: "FROM, WHERE, ORDER BY, SELECT." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["SELECT", "Lists the fields to display"], ["FROM", "Names the table"], ["WHERE", "Gives the search condition"], ["ORDER BY", "Sorts the rows"], ["COUNT", "Counts the records"], ["SUM", "Adds the values of a field"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A truth table has 3 inputs. How many rows does it have?", "a": 8, "unit": "", "tol": 0.01, "hint": "2 × 2 × 2.", "sol": "<b>8</b>."},
  {"q": "A four-mark truth table has 8 outputs and 6 are correct. How many marks?", "a": 3, "unit": "", "tol": 0.01, "hint": "6 or 7 correct gives 3.", "sol": "<b>3</b> marks."},
  {"q": "A table has 7 fields and 12 records. How many data items are stored (not counting the headings)?", "a": 84, "unit": "", "tol": 0.01, "hint": "7 × 12.", "sol": "<b>84</b>."},
  {"q": "Five rock songs last 3, 4, 2, 5 and 6 minutes. What does SELECT SUM(Minutes) … WHERE Genre = 'rock' give?", "a": 20, "unit": "min", "tol": 0.01, "hint": "3 + 4 + 2 + 5 + 6.", "sol": "<b>20</b>."},
  {"q": "What is the output of a NAND gate when both inputs are 1? (Give 0 or 1.)", "a": 0, "unit": "", "tol": 0.01, "hint": "AND gives 1, NAND is NOT AND.", "sol": "<b>0</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "How should the NOT of X be written in an expression?", opts: ["X NOT", "NOT X", "X'", "-X"], a: 1, why: "NOT comes first." },
  { q: "Which mistake would turn the final column into the exact opposite of the right answer?", opts: ["Rows in the wrong order", "Missing the final NOT in a NAND or NOR", "Writing the inputs in capitals", "Counting the heading as a row"], a: 1, why: "NAND and NOR end with a negation, so missing it reverses every output." },
  { q: "In SQL, which line decides which records are shown?", opts: ["SELECT", "FROM", "WHERE", "ORDER BY"], a: 2, why: "WHERE gives the search condition." },
  { q: "A table has fields ItemNo, Type and Price. Why is Type not a good primary key?", opts: ["It is text", "Its values repeat, so it is not unique", "It is too short", "It is a Boolean"], a: 1, why: "A primary key must be a unique identifier." },
  { q: "What should the output of an SQL statement not contain?", opts: ["The data", "Extra punctuation", "The right columns", "The right order"], a: 1, why: "The report says punctuation should not be in the output." },
] });
Lib.cards($("#fc1"), { cards: [
  ["NOT", "Reverses one input."],
  ["AND, OR", "Both 1; at least one 1."],
  ["NAND, NOR", "NOT of AND, NOT of OR."],
  ["XOR", "1 when inputs differ."],
  ["Truth table", "Binary rows, a column per gate."],
  ["Primary key", "A unique identifier."],
  ["SQL order", "FROM, WHERE, ORDER BY, SELECT."],
  ["SQL output", "Selected fields, matching rows, no punctuation."],
] });
