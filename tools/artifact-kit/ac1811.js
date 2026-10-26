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
const GS = {"nodes": {"Base": [240, 36], "Town 1": [70, 100], "Town 2": [400, 90], "Town 3": [230, 130], "Town 6": [480, 170], "Town 4": [90, 240], "Town 5": [330, 230]}, "edges": [["Base", "Town 1", 4], ["Base", "Town 3", 2], ["Base", "Town 2", 5], ["Town 1", "Town 3", 1], ["Town 1", "Town 4", 7], ["Town 2", "Town 6", 8], ["Town 2", "Town 5", 3], ["Town 3", "Town 5", 1], ["Town 4", "Town 5", 6], ["Town 5", "Town 6", 5]], "start": "Base"}, GA = {"nodes": {"A": [60, 60], "B": [240, 40], "C": [150, 160], "D": [330, 150]}, "edges": [["A", "B", 4], ["A", "C", 2], ["B", "C", 1], ["B", "D", 5], ["C", "D", 8]], "start": "A"};

(function () {
  const steps = [{ n: 0, e: 0, w: false, cap: "A graph starts with <b>nodes</b>, one for each entity: here four places." }, { n: 4, e: 0, w: false, cap: "The four <b>nodes</b> A, B, C and D." }, { n: 4, e: 5, w: false, cap: "<b>Edges</b> connect nodes that are related, here by a road." }, { n: 4, e: 5, w: true, cap: "Each edge has a <b>weight</b>: the distance. Now the graph can be searched for the cheapest path." }];
  const draw = (s) => { const st = steps[Math.round(s.i)], g = GA, names = Object.keys(g.nodes); let o = "";
    g.edges.slice(0, st.e).forEach(([u, v, w]) => { o += SV.line(g.nodes[u][0], g.nodes[u][1], g.nodes[v][0], g.nodes[v][1], "ax", { style: "stroke:var(--muted);stroke-width:2" }); });
    g.edges.slice(0, st.e).forEach(([u, v, w]) => { const mx = (g.nodes[u][0] + g.nodes[v][0]) / 2, my = (g.nodes[u][1] + g.nodes[v][1]) / 2; if (st.w) o += SV.rect(mx - 12, my - 11, 24, 22, "cell", { rx: 4 }) + SV.text(mx, my + 5, String(w), "lbl bd", { "text-anchor": "middle" }); });
    names.slice(0, st.n).forEach((n) => (o += SV.circle(g.nodes[n][0], g.nodes[n][1], 22, "nd", {}) + SV.text(g.nodes[n][0], g.nodes[n][1] + 5, n, "lbl bd", { "text-anchor": "middle" }))); return o; };
  Lib.stepper($("#stA"), { w: 420, h: 210, label: "Building a graph", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: steps.map((x, i) => ({ cap: x.cap, s: { i } })) });
})();
(function () {
  const g = GA; const P = [["A", "B", "D"], ["A", "C", "B", "D"]];
  const draw = (s) => { const k = Math.round(s.i), p = P[k > 1 ? 1 : 0]; const hs = new Set(); p.forEach((n, i) => { if (i) { hs.add(p[i - 1] + n); hs.add(n + p[i - 1]); } }); let o = "";
    g.edges.forEach(([u, v, w]) => { o += SV.line(g.nodes[u][0], g.nodes[u][1], g.nodes[v][0], g.nodes[v][1], "ax", { style: "stroke:" + (k > 0 && hs.has(u + v) ? "var(--good)" : "var(--muted)") + ";stroke-width:" + (k > 0 && hs.has(u + v) ? 4 : 2) }); });
    g.edges.forEach(([u, v, w]) => { const mx = (g.nodes[u][0] + g.nodes[v][0]) / 2, my = (g.nodes[u][1] + g.nodes[v][1]) / 2; o += SV.rect(mx - 12, my - 11, 24, 22, "cell", { rx: 4 }) + SV.text(mx, my + 5, String(w), "lbl bd", { "text-anchor": "middle" }); });
    Object.keys(g.nodes).forEach((n) => (o += SV.circle(g.nodes[n][0], g.nodes[n][1], 22, p.includes(n) && k > 0 ? "nd-ok" : "nd", {}) + SV.text(g.nodes[n][0], g.nodes[n][1] + 5, n, "lbl bd", { "text-anchor": "middle" })));
    o += SV.text(20, 200, k === 1 ? "A, B, D: 2 edges, cost 4 + 5 = 9" : k === 2 ? "A, C, B, D: 3 edges, cost 2 + 1 + 5 = 8: cheaper" : "", "lbl bd t3", { style: "font-size:14px" }); return o; };
  Lib.stepper($("#stB"), { w: 420, h: 220, label: "Cheapest path", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: [{ cap: "Find the best path from A to D.", s: { i: 0 } }, { cap: "The path with the <b>fewest edges</b> is A, B, D. Its total weight is 9.", s: { i: 1 } }, { cap: "The path A, C, B, D has more edges but a total weight of only 8. The <b>cheapest</b> path is not the one with fewest edges.", s: { i: 2 } }] });
})();

(function () {
  const names = Object.keys(GS.nodes), F = $("#gF"), T = $("#gT"); names.forEach((n) => { F.add(new Option(n, n)); T.add(new Option(n, n)); }); F.value = "Base"; T.value = "Town 6";
  const a = adjOf(GS);
  const paint = () => { const f = F.value, t = T.value, all = []; const dfs = (u, path, cost) => { if (u === t) { all.push([path.slice(), cost]); return; } a[u].forEach(([v, w]) => { if (!path.includes(v)) { path.push(v); dfs(v, path, cost + w); path.pop(); } }); }; dfs(f, [f], 0); all.sort((x, y) => x[1] - y[1]);
    const best = all.length ? all[0][0] : []; const gs = graphSvgJs(GS, { hl: best }); $("#gG").innerHTML = `<svg viewBox="0 0 ${gs.W} ${gs.H}" style="width:${Math.round(gs.W * 1.1)}px;max-width:100%;display:block">${gs.inner}</svg>`;
    $("#gP").innerHTML = f === t ? "<p>Choose two different towns.</p>" : `<div class="tw"><table class="t mono"><tr><th>Path</th><th>Edges</th><th>Cost</th></tr>${all.slice(0, 12).map((x, i) => `<tr${i === 0 ? ' style="background:var(--good-soft);font-weight:700"' : ""}><td>${x[0].join(" → ")}</td><td>${x[0].length - 1}</td><td>${x[1]}</td></tr>`).join("")}</table></div><div class="verdict">${all.length} simple paths from ${f} to ${t}. The cheapest costs <b>${all[0] ? all[0][1] : "-"}</b> (shaded).</div>`; };
  F.onchange = T.onchange = paint; paint();
})();
(function () {
  const a = adjOf(GS), b = $("#nB");
  const show = (n) => { $("#nV").innerHTML = `<b>${n}</b> has <b>${a[n].length}</b> neighbours: ` + a[n].map(([v, w]) => `${v} (weight ${w})`).join(", ") + "."; b.querySelectorAll("button").forEach((x) => (x.className = x.textContent === n ? "on" : "")); };
  Object.keys(GS.nodes).forEach((n) => { const x = document.createElement("button"); x.textContent = n; x.onclick = () => show(n); b.appendChild(x); }); show("Base");
})();
Lib.classify($("#cl1"), { prompt: "Is it a node or an edge?", buckets: [{"label": "Node"}, {"label": "Edge"}], items: [{"text": "A town", "b": 0}, {"text": "A road between two towns", "b": 1}, {"text": "A person in a social network", "b": 0}, {"text": "A friendship", "b": 1}, {"text": "A router", "b": 0}, {"text": "A cable between routers", "b": 1}], done: "Nodes are the things; edges are the connections." });
Lib.classify($("#cl2"), { prompt: "In a road map graph, what is it?", buckets: [{"label": "Node"}, {"label": "Edge"}, {"label": "Weight"}], items: [{"text": "A junction", "b": 0}, {"text": "A road", "b": 1}, {"text": "The length of a road in km", "b": 2}, {"text": "A town", "b": 0}, {"text": "The journey time of a road", "b": 2}, {"text": "A motorway link", "b": 1}], done: "Junctions are nodes, roads edges, distances or times weights." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Vertex", "Another name for a node"], ["Edge", "A connection between two nodes"], ["Weight", "A distance, cost or time on an edge"], ["Path", "The nodes connected by edges between two nodes"], ["Cycle", "A path that returns to the same node"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of using a graph to plan a route in order.", items: ["Represent the places as nodes", "Connect them with edges", "Add the distances as weights", "Run a search algorithm such as Dijkstra's", "Read off the path with the lowest total weight"], done: "Nodes, edges, weights, algorithm, result." });
Lib.calc($("#c1"), { qs: [
  {"q": "In the A, B, C, D graph, what is the cost of the path A, C, D?", "a": 10, "unit": "", "tol": 0.01, "hint": "2 + 8.", "sol": "<b>10</b>."},
  {"q": "How many edges does the graph A, B, C, D have?", "a": 5, "unit": "", "tol": 0.01, "hint": "Count the lines.", "sol": "<b>5</b>."},
  {"q": "How many neighbours does node C have?", "a": 3, "unit": "", "tol": 0.01, "hint": "A, B and D.", "sol": "<b>3</b>."},
  {"q": "What is the cost of the cheapest path from A to D?", "a": 8, "unit": "", "tol": 0.01, "hint": "A, C, B, D.", "sol": "<b>8</b>."},
  {"q": "A complete graph with 4 nodes has an edge between every pair. How many edges?", "a": 6, "unit": "", "tol": 0.01, "hint": "4 × 3 ÷ 2.", "sol": "<b>6</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A graph in AI is made of:", opts: ["Bars", "Nodes and edges", "Rows only", "Pixels"], a: 1, why: "Nodes and edges." },
  { q: "A weight on an edge could be:", opts: ["A distance", "A colour", "A font", "A name"], a: 0, why: "A distance, cost or time." },
  { q: "A cycle is:", opts: ["A path that returns to the same node", "A node with no edges", "A weight", "A table"], a: 0, why: "It returns to the start." },
  { q: "Which algorithm can search a graph for a shortest path?", opts: ["Dijkstra's", "Bubble sort", "Binary search", "Hashing"], a: 0, why: "Dijkstra's." },
  { q: "A directed graph has:", opts: ["Edges with a direction", "No nodes", "Only weights", "No edges"], a: 0, why: "Arrows." },
  { q: "Neural networks can be represented as:", opts: ["Graphs", "Tables only", "Text", "Images only"], a: 0, why: "Neurons are nodes." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Graph", "Nodes joined by edges; records relationships."],
  ["Weight", "Distance, cost or time on an edge."],
  ["Path", "Nodes connected by edges between two nodes."],
  ["Cycle", "A path returning to its start."],
  ["Directed", "Edges can only be followed one way."],
  ["Why in AI", "AI problems become path-finding in a graph."],
  ["Algorithms", "Dijkstra's and A*."],
  ["Storage", "Adjacency matrix or adjacency list."],
] });
