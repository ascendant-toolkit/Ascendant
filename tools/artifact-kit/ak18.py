"""Shared pieces for the A Level Computer Science (9618) chapter 18 pages (Artificial Intelligence): the graphs from the past papers,
Dijkstra's and A* algorithms (Python and a JS twin cross-checked with node) and a graph drawer."""
import json
from ak16 import *

INF = float("inf")

# ---- the graphs of the past papers: nodes {name: (x, y)}, edges [(a, b, weight)], optional heuristic h
GRAPHS = {
    "s21": dict(start="Base", nodes={"Base": (240, 36), "Town 1": (70, 100), "Town 2": (400, 90), "Town 3": (230, 130), "Town 6": (480, 170), "Town 4": (90, 240), "Town 5": (330, 230)},
                edges=[("Base", "Town 1", 4), ("Base", "Town 3", 2), ("Base", "Town 2", 5), ("Town 1", "Town 3", 1), ("Town 1", "Town 4", 7), ("Town 2", "Town 6", 8), ("Town 2", "Town 5", 3), ("Town 3", "Town 5", 1), ("Town 4", "Town 5", 6), ("Town 5", "Town 6", 5)]),
    "w23": dict(start="Start", nodes={"A": (70, 50), "B": (240, 50), "C": (420, 60), "D": (150, 140), "E": (300, 170), "Start": (60, 240), "F": (430, 240)},
                edges=[("Start", "A", 8), ("Start", "F", 10), ("A", "B", 4), ("B", "C", 8), ("B", "D", 2), ("D", "E", 2), ("C", "E", 3), ("C", "F", 9), ("E", "F", 7)]),
    "w25": dict(start="Start", nodes={"V": (260, 36), "T": (90, 100), "X": (430, 90), "W": (170, 150), "Y": (330, 210), "Start": (60, 250), "Z": (450, 250)},
                edges=[("Start", "T", 6), ("Start", "Y", 22), ("T", "V", 4), ("V", "W", 3), ("V", "X", 9), ("W", "X", 5), ("X", "Y", 3), ("X", "Z", 10), ("Y", "Z", 8)]),
    "s26_31": dict(start="Begin", nodes={"Q": (90, 40), "S": (470, 40), "R": (300, 90), "P": (130, 140), "T": (500, 180), "U": (370, 240), "Begin": (70, 240)},
                   edges=[("Begin", "P", 9), ("Begin", "R", 6), ("Begin", "U", 21), ("P", "Q", 5), ("P", "R", 2), ("Q", "S", 5), ("R", "S", 8), ("S", "U", 6), ("S", "T", 3), ("T", "U", 4)]),
    "s26_32": dict(start="Home", nodes={"C": (250, 36), "B": (90, 90), "D": (450, 100), "A": (200, 160), "Home": (60, 240), "F": (340, 240), "E": (470, 250)},
                   edges=[("Home", "A", 6), ("Home", "F", 16), ("A", "B", 8), ("A", "C", 3), ("A", "F", 8), ("B", "C", 4), ("C", "D", 12), ("D", "F", 6), ("D", "E", 7), ("F", "E", 3)]),
    "w21": dict(start="Home", goal="School", h={"Home": 14, "A": 10, "B": 7, "C": 9, "D": 6, "E": 3, "F": 3, "School": 0},
                nodes={"Home": (250, 36), "A": (90, 70), "C": (410, 70), "B": (250, 120), "D": (410, 170), "F": (170, 180), "E": (70, 220), "School": (400, 250)},
                edges=[("Home", "A", 1), ("Home", "B", 5), ("Home", "C", 4), ("A", "B", 3), ("A", "E", 6), ("B", "D", 2), ("B", "School", 7), ("C", "D", 6), ("D", "School", 2), ("E", "F", 1), ("E", "School", 5), ("F", "School", 3)]),
    "s23": dict(start="Begin", goal="End", h={"Begin": 12, "A": 8, "B": 7, "C": 7, "D": 11, "E": 8, "F": 1, "G": 5, "End": 0},
                nodes={"Begin": (260, 36), "A": (110, 80), "D": (440, 80), "C": (370, 120), "B": (230, 120), "E": (60, 170), "End": (250, 190), "G": (430, 190), "F": (140, 240)},
                edges=[("Begin", "A", 5), ("Begin", "B", 6), ("Begin", "C", 5), ("Begin", "D", 4), ("A", "E", 6), ("A", "End", 8), ("B", "End", 7), ("C", "G", 2), ("D", "G", 6), ("E", "F", 7), ("F", "End", 1), ("F", "G", 4), ("G", "End", 7)]),
    "s26_33": dict(start="W", goal="E", h={"W": 18, "N1": 15, "N2": 14, "N3": 13, "N4": 9, "N5": 7, "N6": 3, "E": 0},
                   nodes={"N6": (300, 40), "N1": (140, 70), "E": (480, 100), "N5": (390, 100), "W": (50, 160), "N2": (260, 175), "N4": (430, 190), "N3": (150, 245)},
                   edges=[("W", "N1", 6), ("W", "N2", 4), ("W", "N3", 7), ("N1", "N2", 3), ("N1", "N6", 12), ("N2", "N3", 2), ("N2", "N5", 7), ("N3", "N4", 4), ("N6", "N5", 4), ("N6", "E", 3), ("N5", "E", 11), ("N5", "N4", 2), ("N4", "E", 12)]),
}


def adj(g):
    a = {n: [] for n in g["nodes"]}
    for u, v, w in g["edges"]:
        a[u].append((v, w))
        a[v].append((u, w))
    return a


def dijkstra(g, start=None):
    """Returns (steps, dist, prev). steps = [(visited node, {node: tentative distance after settling it})]."""
    a = adj(g)
    start = start or g["start"]
    dist = {n: INF for n in a}
    dist[start] = 0
    prev, seen, steps = {}, set(), []
    steps.append((None, dict(dist)))
    while len(seen) < len(a):
        u = min((n for n in a if n not in seen), key=lambda n: (dist[n], list(a).index(n)))
        if dist[u] == INF:
            break
        seen.add(u)
        for v, w in a[u]:
            if v not in seen and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
        steps.append((u, dict(dist)))
    return steps, dist, prev


def path_to(prev, goal, start):
    p = [goal]
    while p[-1] != start:
        p.append(prev[p[-1]])
    return p[::-1]


def astar(g):
    """A* in the exam's table style. Rows: (from node, to node, g, h, f). Ties go to the lower h, then the most recent."""
    a, h, start, goal = adj(g), g["h"], g["start"], g["goal"]
    best = {start: 0}
    prev = {}
    rows = [(start, start, 0, h[start], h[start])]
    open_ = {start: 0}
    closed = set()
    order = {start: 0}
    tick = 1
    while open_:
        u = min(open_, key=lambda n: (open_[n] + h[n], h[n], -order[n]))
        if u == goal:
            break
        gu = open_.pop(u)
        closed.add(u)
        for v, w in a[u]:
            ng = gu + w
            if v in closed or (v in best and ng >= best[v]):
                continue
            best[v] = ng
            prev[v] = u
            open_[v] = ng
            order[v] = tick
            tick += 1
            rows.append((u, v, ng, h[v], ng + h[v]))
    return rows, path_to(prev, goal, start), best[goal]


# ---- checked against the mark schemes
_, D1, _ = dijkstra(GRAPHS["s21"])
assert [D1[f"Town {i}"] for i in range(1, 7)] == [3, 5, 2, 9, 3, 8]
r_, p_, c_ = astar(GRAPHS["w21"])
assert p_ == ["Home", "A", "E", "F", "School"] and c_ == 11
assert [(x[0], x[1]) for x in r_][:9] == [("Home", "Home"), ("Home", "A"), ("Home", "B"), ("Home", "C"), ("A", "B"), ("A", "E"), ("E", "F"), ("E", "School"), ("F", "School")]
r_, p_, c_ = astar(GRAPHS["s23"])
assert p_ == ["Begin", "C", "G", "F", "End"] and c_ == 12
r_, p_, c_ = astar(GRAPHS["s26_33"])
assert p_ == ["W", "N2", "N5", "N6", "E"] and c_ == 18


def dist_table(g, start=None):
    """Dijkstra working: one row per node settled, a column per node showing the tentative distance (visited nodes in bold)."""
    steps, dist, prev = dijkstra(g, start)
    names = [n for n in g["nodes"]]
    h = '<div class="tw"><table class="t mono"><tr><th>Visit</th>' + "".join(f"<th>{n}</th>" for n in names) + "</tr>"
    visited = set()
    for u, d in steps:
        if u:
            visited.add(u)
        h += f"<tr><td>{u or 'start'}</td>" + "".join((f"<td><b>{d[n]}</b></td>" if n in visited else f"<td>{'∞' if d[n] == INF else d[n]}</td>") for n in names) + "</tr>"
    return h + "</table></div>"


def astar_table(g):
    rows, path, cost = astar(g)
    h = '<div class="tw"><table class="t mono"><tr><th>Start node</th><th>Destination</th><th>g (cost so far)</th><th>h (heuristic)</th><th>f = g + h</th></tr>'
    for r in rows:
        h += "<tr>" + "".join(f"<td>{x}</td>" for x in r) + "</tr>"
    return h + f"</table></div><p>Final path: <b>{' → '.join(path)}</b> (cost {cost}).</p>"


def graph_svg(g, hl=None, h=False, cap="", dist=None):
    """Static graph drawing. hl = list of nodes on a highlighted path; h=True shows heuristic values next to nodes."""
    nodes = g["nodes"]
    xs = [p[0] for p in nodes.values()]
    ys = [p[1] for p in nodes.values()]
    W, H = max(xs) + 60, max(ys) + 50
    hlp = set(zip(hl, hl[1:])) | set(zip(hl[1:], hl)) if hl else set()
    o = f'<svg viewBox="0 0 {W} {H}" style="width:{W * 1.1:.0f}px;max-width:100%;display:block" role="img" aria-label="{cap or "graph"}">'
    for u, v, w in g["edges"]:
        (x1, y1), (x2, y2) = nodes[u], nodes[v]
        on = (u, v) in hlp
        o += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ax" style="stroke:{"var(--good)" if on else "var(--muted)"};stroke-width:{3.4 if on else 1.8}"/>'
    for u, v, w in g["edges"]:
        (x1, y1), (x2, y2) = nodes[u], nodes[v]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        o += f'<rect x="{mx - 11}" y="{my - 10}" width="22" height="20" rx="4" style="fill:var(--surface)"/><text class="lbl bd" x="{mx}" y="{my + 5}" text-anchor="middle" style="font-size:13px">{w}</text>'
    for n, (x, y) in nodes.items():
        on = hl and n in hl
        w = max(46, 8.6 * len(n) + 20)
        ht = 42 if (h and "h" in g) else 34
        o += f'<rect x="{x - w / 2}" y="{y - ht / 2}" width="{w}" height="{ht}" rx="{ht / 2}" class="ax" style="fill:{"var(--good-soft)" if on else "var(--surface)"}"/>'
        if h and "h" in g:
            o += f'<text class="lbl bd" x="{x}" y="{y - 2}" text-anchor="middle" style="font-size:12.5px">{n}</text><text class="sm" x="{x}" y="{y + 12}" text-anchor="middle" style="fill:var(--accent);font-size:11px">h={g["h"][n]}</text>'
        else:
            o += f'<text class="lbl bd" x="{x}" y="{y + 5}" text-anchor="middle" style="font-size:12.5px">{n}</text>'
        if dist is not None and n in dist:
            o += f'<text class="sm" x="{x}" y="{y + 36}" text-anchor="middle" style="fill:var(--accent);font-size:12px">{dist[n]}</text>'
    return o + "</svg>"


def gsx(g, **kw):
    return f'<div class="synd">{graph_svg(g, **kw)}</div>'


AK18JS = r'''
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
'''


def graph_check():
    """Run the JS Dijkstra and A* under node on every graph and compare with Python."""
    import subprocess, tempfile, os
    gs = {k: {"start": v["start"], "goal": v.get("goal"), "h": v.get("h"), "nodes": {n: list(p) for n, p in v["nodes"].items()}, "edges": [list(e) for e in v["edges"]]} for k, v in GRAPHS.items()}
    js = AK18JS + "\nconst G=" + json.dumps(gs) + ";const out={};for(const k in G){const d=dijkstra(G[k]);out[k]={d:Object.fromEntries(Object.entries(d.dist).map(([n,v])=>[n,v===Infinity?null:v]))};if(G[k].h){const r=astar(G[k]);out[k].a=[r.rows,r.path,r.cost]}}console.log(JSON.stringify(out))"
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(js)
    out = json.loads(subprocess.run(["node", f.name], capture_output=True, text=True).stdout)
    os.unlink(f.name)
    for k, v in GRAPHS.items():
        _, dist, _ = dijkstra(v)
        assert {n: (None if x == INF else x) for n, x in dist.items()} == out[k]["d"], k
        if "h" in v:
            r, p, c = astar(v)
            assert [list(x) for x in r] == out[k]["a"][0] and p == out[k]["a"][1] and c == out[k]["a"][2], k
