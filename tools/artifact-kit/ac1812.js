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

const INF = Infinity;
function adjOf(g) { const a = {}; Object.keys(g.nodes).forEach((n) => (a[n] = [])); g.edges.forEach(([u, v, w]) => { a[u].push([v, w]); a[v].push([u, w]); }); return a; }
function dijkstra(g, start) { const a = adjOf(g), names = Object.keys(a), dist = {}, prev = {}, seen = new Set(), steps = []; names.forEach((n) => (dist[n] = INF)); start = start || g.start; dist[start] = 0; steps.push([null, Object.assign({}, dist)]);
  while (seen.size < names.length) { let u = null; names.forEach((n) => { if (!seen.has(n) && (u === null || dist[n] < dist[u])) u = n; }); if (dist[u] === INF) break; seen.add(u); a[u].forEach(([v, w]) => { if (!seen.has(v) && dist[u] + w < dist[v]) { dist[v] = dist[u] + w; prev[v] = u; } }); steps.push([u, Object.assign({}, dist)]); }
  return { steps, dist, prev }; }
function pathTo(prev, goal, start) { const p = [goal]; while (p[p.length - 1] !== start) p.push(prev[p[p.length - 1]]); return p.reverse(); }
function astar(g) { const a = adjOf(g), h = g.h, start = g.start, goal = g.goal, best = { [start]: 0 }, prev = {}, rows = [[start, start, 0, h[start], h[start]]], open = { [start]: 0 }, closed = new Set(), order = { [start]: 0 }; let tick = 1;
  while (Object.keys(open).length) { const u = Object.keys(open).sort((x, y) => (open[x] + h[x]) - (open[y] + h[y]) || h[x] - h[y] || order[y] - order[x])[0]; if (u === goal) break; const gu = open[u]; delete open[u]; closed.add(u);
    a[u].forEach(([v, w]) => { const ng = gu + w; if (closed.has(v) || (v in best && ng >= best[v])) return; best[v] = ng; prev[v] = u; open[v] = ng; order[v] = tick++; rows.push([u, v, ng, h[v], ng + h[v]]); }); }
  return { rows, path: pathTo(prev, goal, start), cost: best[goal] }; }
function graphSvgJs(g, o) { o = o || {}; const nodes = g.nodes, hl = o.hl || [], hs = new Set(); hl.forEach((n, i) => { if (i) { hs.add(hl[i - 1] + "|" + n); hs.add(n + "|" + hl[i - 1]); } });
  const xs = Object.values(nodes).map((p) => p[0]), ys = Object.values(nodes).map((p) => p[1]), W = Math.max(...xs) + 60, H = Math.max(...ys) + 50; let s = "";
  g.edges.forEach(([u, v]) => { const on = hs.has(u + "|" + v); s += `<line x1="${nodes[u][0]}" y1="${nodes[u][1]}" x2="${nodes[v][0]}" y2="${nodes[v][1]}" class="ax" style="stroke:${on ? "var(--good)" : "var(--muted)"};stroke-width:${on ? 3.4 : 1.8}"/>`; });
  g.edges.forEach(([u, v, w]) => { const mx = (nodes[u][0] + nodes[v][0]) / 2, my = (nodes[u][1] + nodes[v][1]) / 2; s += `<rect x="${mx - 11}" y="${my - 10}" width="22" height="20" rx="4" style="fill:var(--surface)"/><text class="lbl bd" x="${mx}" y="${my + 5}" text-anchor="middle" style="font-size:13px">${w}</text>`; });
  Object.entries(nodes).forEach(([n, [x, y]]) => { const cur = o.cur === n, on = hl.includes(n), done = o.done && o.done.has(n), w = Math.max(46, 8.6 * n.length + 20), showH = o.h && g.h, ht = showH ? 42 : 34;
    s += `<rect x="${x - w / 2}" y="${y - ht / 2}" width="${w}" height="${ht}" rx="${ht / 2}" class="ax" style="fill:${cur ? "var(--warn-soft)" : on || done ? "var(--good-soft)" : "var(--surface)"};${cur ? "stroke:var(--warn);stroke-width:3" : ""}"/>`;
    s += showH ? `<text class="lbl bd" x="${x}" y="${y - 2}" text-anchor="middle" style="font-size:12.5px">${n}</text><text class="sm" x="${x}" y="${y + 12}" text-anchor="middle" style="fill:var(--accent);font-size:11px">h=${g.h[n]}</text>` : `<text class="lbl bd" x="${x}" y="${y + 5}" text-anchor="middle" style="font-size:12.5px">${n}</text>`;
    if (o.dist && o.dist[n] !== undefined) s += `<text class="sm" x="${x}" y="${y + 36}" text-anchor="middle" style="fill:var(--accent);font-size:12px">${o.dist[n] === INF ? "∞" : o.dist[n]}</text>`; });
  return { W, H, inner: s }; }
const GG = {"s21": {"start": "Base", "goal": null, "h": null, "nodes": {"Base": [240, 36], "Town 1": [70, 100], "Town 2": [400, 90], "Town 3": [230, 130], "Town 6": [480, 170], "Town 4": [90, 240], "Town 5": [330, 230]}, "edges": [["Base", "Town 1", 4], ["Base", "Town 3", 2], ["Base", "Town 2", 5], ["Town 1", "Town 3", 1], ["Town 1", "Town 4", 7], ["Town 2", "Town 6", 8], ["Town 2", "Town 5", 3], ["Town 3", "Town 5", 1], ["Town 4", "Town 5", 6], ["Town 5", "Town 6", 5]]}, "w23": {"start": "Start", "goal": null, "h": null, "nodes": {"A": [70, 50], "B": [240, 50], "C": [420, 60], "D": [150, 140], "E": [300, 170], "Start": [60, 240], "F": [430, 240]}, "edges": [["Start", "A", 8], ["Start", "F", 10], ["A", "B", 4], ["B", "C", 8], ["B", "D", 2], ["D", "E", 2], ["C", "E", 3], ["C", "F", 9], ["E", "F", 7]]}, "w25": {"start": "Start", "goal": null, "h": null, "nodes": {"V": [260, 36], "T": [90, 100], "X": [430, 90], "W": [170, 150], "Y": [330, 210], "Start": [60, 250], "Z": [450, 250]}, "edges": [["Start", "T", 6], ["Start", "Y", 22], ["T", "V", 4], ["V", "W", 3], ["V", "X", 9], ["W", "X", 5], ["X", "Y", 3], ["X", "Z", 10], ["Y", "Z", 8]]}, "s26_31": {"start": "Begin", "goal": null, "h": null, "nodes": {"Q": [90, 40], "S": [470, 40], "R": [300, 90], "P": [130, 140], "T": [500, 180], "U": [370, 240], "Begin": [70, 240]}, "edges": [["Begin", "P", 9], ["Begin", "R", 6], ["Begin", "U", 21], ["P", "Q", 5], ["P", "R", 2], ["Q", "S", 5], ["R", "S", 8], ["S", "U", 6], ["S", "T", 3], ["T", "U", 4]]}, "s26_32": {"start": "Home", "goal": null, "h": null, "nodes": {"C": [250, 36], "B": [90, 90], "D": [450, 100], "A": [200, 160], "Home": [60, 240], "F": [340, 240], "E": [470, 250]}, "edges": [["Home", "A", 6], ["Home", "F", 16], ["A", "B", 8], ["A", "C", 3], ["A", "F", 8], ["B", "C", 4], ["C", "D", 12], ["D", "F", 6], ["D", "E", 7], ["F", "E", 3]]}, "w21": {"start": "Home", "goal": "School", "h": {"Home": 14, "A": 10, "B": 7, "C": 9, "D": 6, "E": 3, "F": 3, "School": 0}, "nodes": {"Home": [250, 36], "A": [90, 70], "C": [410, 70], "B": [250, 120], "D": [410, 170], "F": [170, 180], "E": [70, 220], "School": [400, 250]}, "edges": [["Home", "A", 1], ["Home", "B", 5], ["Home", "C", 4], ["A", "B", 3], ["A", "E", 6], ["B", "D", 2], ["B", "School", 7], ["C", "D", 6], ["D", "School", 2], ["E", "F", 1], ["E", "School", 5], ["F", "School", 3]]}, "s23": {"start": "Begin", "goal": "End", "h": {"Begin": 12, "A": 8, "B": 7, "C": 7, "D": 11, "E": 8, "F": 1, "G": 5, "End": 0}, "nodes": {"Begin": [260, 36], "A": [110, 80], "D": [440, 80], "C": [370, 120], "B": [230, 120], "E": [60, 170], "End": [250, 190], "G": [430, 190], "F": [140, 240]}, "edges": [["Begin", "A", 5], ["Begin", "B", 6], ["Begin", "C", 5], ["Begin", "D", 4], ["A", "E", 6], ["A", "End", 8], ["B", "End", 7], ["C", "G", 2], ["D", "G", 6], ["E", "F", 7], ["F", "End", 1], ["F", "G", 4], ["G", "End", 7]]}, "s26_33": {"start": "W", "goal": "E", "h": {"W": 18, "N1": 15, "N2": 14, "N3": 13, "N4": 9, "N5": 7, "N6": 3, "E": 0}, "nodes": {"N6": [300, 40], "N1": [140, 70], "E": [480, 100], "N5": [390, 100], "W": [50, 160], "N2": [260, 175], "N4": [430, 190], "N3": [150, 245]}, "edges": [["W", "N1", 6], ["W", "N2", 4], ["W", "N3", 7], ["N1", "N2", 3], ["N1", "N6", 12], ["N2", "N3", 2], ["N2", "N5", 7], ["N3", "N4", 4], ["N6", "N5", 4], ["N6", "E", 3], ["N5", "E", 11], ["N5", "N4", 2], ["N4", "E", 12]]}};

function gsvg(g, o) { const s = graphSvgJs(g, o); return { W: s.W, H: s.H, inner: s.inner }; }
(function () {
  const g = GG.s21, { steps, dist } = dijkstra(g), names = Object.keys(g.nodes);
  const draw = (s) => { const k = Math.round(s.i), [cur, d] = steps[k]; const done = new Set(steps.slice(1, k + 1).map((x) => x[0])); const o = gsvg(g, { cur, done, dist: d }); return o.inner; };
  const W = Math.max(...Object.values(g.nodes).map((p) => p[0])) + 60, H = Math.max(...Object.values(g.nodes).map((p) => p[1])) + 60;
  Lib.stepper($("#stA"), { w: W, h: H, label: "Dijkstra", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: steps.map(([u, d], i) => ({ cap: i === 0 ? "Initialise: Base = 0 and every other node = ∞ (not yet reached)." : `Visit <b>${u}</b> (distance ${d[u]}, the smallest unvisited). Update its neighbours: ` + (adjOf(g)[u].filter(([v]) => !steps.slice(1, i + 1).some((x) => x[0] === v)).map(([v, w]) => `${v}: ${d[u]} + ${w} = ${d[u] + w}${d[v] === d[u] + w ? " (new best)" : ""}`).join("; ") || "no unvisited neighbours") + ".", s: { i } })) });
})();
(function () {
  const g = GG.w21, { rows, path } = astar(g);
  const Wd = Math.max(...Object.values(g.nodes).map((p) => p[0])) + 60, Hd = Math.max(...Object.values(g.nodes).map((p) => p[1])) + 60;
  const draw = (s) => { const k = Math.round(s.i); const seen = new Set(rows.slice(0, k + 1).flatMap((r) => [r[0], r[1]])); const cur = k ? rows[k][1] : "Home"; const o = gsvg(g, { h: true, cur, done: seen, hl: k === rows.length - 1 ? path : [] }); return o.inner; };
  Lib.stepper($("#stB"), { w: Wd, h: Hd, label: "A*", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: rows.map((r, i) => ({ cap: i === 0 ? "Start: Home has g = 0, h = 14, so f = 14." : `From <b>${r[0]}</b> to <b>${r[1]}</b>: g = ${r[2]}, h = ${r[3]}, <b>f = ${r[4]}</b>.` + (i === rows.length - 1 ? " The goal has the lowest f: the path is " + path.join(" → ") + "." : ""), s: { i } })) });
})();

(function () {
  let key = "s21", step = 99; const b = $("#dB"); const keys = ["s21", "w23", "w25", "s26_31", "s26_32"];
  const paint = () => { const g = GG[key], { steps } = dijkstra(g), k = Math.min(step, steps.length - 1), [cur, d] = steps[k]; const done = new Set(steps.slice(1, k + 1).map((x) => x[0])); const o = gsvg(g, { cur, done, dist: d });
    $("#dG").innerHTML = `<svg viewBox="0 0 ${o.W} ${o.H}" style="width:${Math.round(o.W * 1.1)}px;max-width:100%;display:block">${o.inner}</svg>`; const names = Object.keys(g.nodes);
    $("#dT").innerHTML = `<div class="tw"><table class="t mono"><tr><th>Visit</th>${names.map((n) => `<th>${n}</th>`).join("")}</tr>` + steps.slice(0, k + 1).map(([u, dd], i) => { const vis = new Set(steps.slice(1, i + 1).map((x) => x[0])); return `<tr><td>${u || "start"}</td>${names.map((n) => `<td>${vis.has(n) ? "<b>" + dd[n] + "</b>" : dd[n] === INF ? "∞" : dd[n]}</td>`).join("")}</tr>`; }).join("") + "</table></div>";
    b.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === key ? "on" : "")); };
  const NM = { s21: "M/J 2021", w23: "O/N 2023", w25: "O/N 2025", s26_31: "M/J 2026 P31", s26_32: "M/J 2026 P32" };
  keys.forEach((k) => { const x = document.createElement("button"); x.textContent = NM[k]; x.dataset.k = k; x.onclick = () => { key = k; step = 99; paint(); }; b.appendChild(x); });
  Lib.slider($("#dS"), { id: "ds", label: "Nodes visited ", min: 0, max: 7, value: 7, fmt: (x) => x, onInput: (v) => { step = v; paint(); } }); paint();
})();
(function () {
  let key = "w21", useH = true; const b = $("#aB"), hb = $("#aH"); const keys = ["w21", "s23", "s26_33"], NM = { w21: "O/N 2021", s23: "M/J 2023", s26_33: "M/J 2026" };
  const paint = () => { const g = JSON.parse(JSON.stringify(GG[key])); if (!useH) Object.keys(g.h).forEach((n) => (g.h[n] = 0)); const { rows, path, cost } = astar(g); const o = gsvg(g, { h: true, hl: path });
    $("#aG").innerHTML = `<svg viewBox="0 0 ${o.W} ${o.H}" style="width:${Math.round(o.W * 1.1)}px;max-width:100%;display:block">${o.inner}</svg>`;
    $("#aT").innerHTML = `<div class="tw"><table class="t mono"><tr><th>From</th><th>To</th><th>g</th><th>h</th><th>f</th></tr>${rows.map((r) => `<tr>${r.map((x) => `<td>${x}</td>`).join("")}</tr>`).join("")}</table></div><div class="verdict">${useH ? "With the heuristic" : "With h = 0 (like Dijkstra's)"}: <b>${rows.length}</b> rows. Path ${path.join(" → ")}, cost ${cost}.</div>`;
    b.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === key ? "on" : "")); hb.querySelectorAll("button").forEach((x) => (x.className = (x.dataset.k === "on") === useH ? "on" : "")); };
  keys.forEach((k) => { const x = document.createElement("button"); x.textContent = NM[k]; x.dataset.k = k; x.onclick = () => { key = k; paint(); }; b.appendChild(x); });
  [["on", "Heuristic on"], ["off", "Heuristic off (h = 0)"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { useH = k === "on"; paint(); }; hb.appendChild(x); }); paint();
})();
Lib.classify($("#cl1"), { prompt: "Dijkstra's algorithm or the A* algorithm?", buckets: [{"label": "Dijkstra's"}, {"label": "A*"}], items: [{"text": "Finds the shortest path to every node", "b": 0}, {"text": "Uses a heuristic", "b": 1}, {"text": "Always finds the shortest path", "b": 0}, {"text": "May not find the shortest path if the heuristic is poor", "b": 1}, {"text": "Chooses the node with the lowest f = g + h", "b": 1}, {"text": "Explores all possible routes", "b": 0}], done: "A* uses a heuristic and one goal; Dijkstra's explores everything." });
Lib.classify($("#cl2"), { prompt: "What does it stand for in the A* table?", buckets: [{"label": "g"}, {"label": "h"}, {"label": "f"}], items: [{"text": "The cost of the route from the start so far", "b": 0}, {"text": "The estimated cost still to go", "b": 1}, {"text": "g + h", "b": 2}, {"text": "Used to choose the next node to expand", "b": 2}, {"text": "Often the straight-line distance to the goal", "b": 1}, {"text": "Adds the edge weights along the path", "b": 0}], done: "g travelled, h estimated, f the total." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Dijkstra's algorithm", "Shortest path from a start node to all nodes"], ["A* algorithm", "Path to one goal using a heuristic"], ["Heuristic", "An estimate of the cost to the goal"], ["Visited node", "A node whose distance is final"], ["∞", "The starting value of every node except the start"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of Dijkstra's algorithm in order.", items: ["Set the start node to 0 and all others to ∞", "Visit the unvisited node with the smallest distance", "Update each neighbour if the route through this node is shorter", "Repeat until all nodes are visited", "Read off the shortest distances"], done: "Initialise, visit, update, repeat, read." });
Lib.calc($("#c1"), { qs: [
  {"q": "In A*, a node has g = 7 and h = 6. What is f?", "a": 13, "unit": "", "tol": 0.01, "hint": "g + h.", "sol": "<b>13</b>."},
  {"q": "Dijkstra: node X = 5. An edge from X to Y has weight 4 and Y is currently ∞. What does Y become?", "a": 9, "unit": "", "tol": 0.01, "hint": "5 + 4.", "sol": "<b>9</b>."},
  {"q": "Y is currently 9 and a new route gives 5 + 3 = 8. What does Y become?", "a": 8, "unit": "", "tol": 0.01, "hint": "The smaller value.", "sol": "<b>8</b>."},
  {"q": "M/J 2021 graph: the shortest distance from Base to Town 6.", "a": 8, "unit": "", "tol": 0.01, "hint": "Base, Town 3, Town 5, Town 6 = 2 + 1 + 5.", "sol": "<b>8</b>."},
  {"q": "O/N 2021 A* graph: the cost of the path Home, A, E, F, School.", "a": 11, "unit": "", "tol": 0.01, "hint": "1 + 6 + 1 + 3.", "sol": "<b>11</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which algorithm uses a heuristic?", opts: ["Dijkstra's", "A*", "Bubble sort", "Binary search"], a: 1, why: "A*." },
  { q: "In Dijkstra's algorithm, unvisited nodes start at:", opts: ["0", "1", "∞", "−1"], a: 2, why: "Infinity." },
  { q: "A* chooses the node with the lowest:", opts: ["g", "h", "f = g + h", "weight"], a: 2, why: "f." },
  { q: "Which always finds the shortest path?", opts: ["A*", "Dijkstra's", "Neither", "Both always, whatever h"], a: 1, why: "Dijkstra's." },
  { q: "What is h in A*?", opts: ["Cost so far", "Estimated cost to the goal", "Number of edges", "The start node"], a: 1, why: "The heuristic." },
  { q: "Both algorithms are used to search a:", opts: ["Graph", "Sorted list", "Stack", "Queue"], a: 0, why: "A graph." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Dijkstra's", "Shortest path from the start to all nodes; start 0, others ∞."],
  ["A*", "Path to one goal; f = g + h; heuristic."],
  ["Heuristic", "Estimate of the cost still to go."],
  ["f = g + h", "Cost so far plus estimate to the goal."],
  ["Visited", "Distance final."],
  ["Update", "New distance if smaller: distance + weight."],
  ["Difference", "A* uses a heuristic; Dijkstra's explores all routes."],
  ["Working marks", "0 and ∞, updates, visited, routes compared."],
] });
