"""A Level CS syllabus 18.1.1: graphs in artificial intelligence. Run: python3 tools/artifact-kit/mk_ac1811.py"""
from ak18 import *

graph_check()
G = GRAPHS["s21"]
G1 = {"start": "A", "nodes": {"A": (60, 60), "B": (240, 40), "C": (150, 160), "D": (330, 150)}, "edges": [("A", "B", 4), ("A", "C", 2), ("B", "C", 1), ("B", "D", 5), ("C", "D", 8)]}

# adjacency matrix of the small graph
names1 = list(G1["nodes"])
mat = {n: {m: 0 for m in names1} for n in names1}
for u, v, w in G1["edges"]:
    mat[u][v] = mat[v][u] = w
matrix = '<div class="tw"><table class="t mono"><tr><th></th>' + "".join(f"<th>{n}</th>" for n in names1) + "</tr>" + "".join(f"<tr><th>{n}</th>" + "".join(f"<td>{mat[n][m] or '–'}</td>" for m in names1) + "</tr>" for n in names1) + "</table></div>"
alist = "<pre class=\"plain\">" + "\n".join(f"{n}: " + ", ".join(f"{m}({w})" for m, w in adj(G1)[n]) for n in names1) + "</pre>"

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>graph</b> is a data structure (an abstract data type) made of <b>vertices</b> (also called nodes) that represent things, joined by <b>edges</b> that represent the relationships or connections between them. In artificial intelligence a graph is used to <b>record relationships between entities</b>, for example places on a map and the distances between them, so that an algorithm can search it for the <b>best path</b>. Edges (and sometimes nodes) can carry a <b>weight</b> such as a distance, cost or time. A <b>path</b> is a list of nodes connected by edges from one node to another; a <b>cycle</b> is a path that returns to the node it started from. Many AI problems can be defined as finding a path in a graph, and neural networks can themselves be drawn as graphs.</p></div>

  <h2>1 · Structure of a graph</h2>
  ''' + gsx(G1, cap="a small weighted graph") + '''
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th><th>In the graph above</th></tr>
    <tr><td><b>Vertex / node</b></td><td>An entity: a place, a person, a state</td><td>A, B, C, D</td></tr>
    <tr><td><b>Edge</b></td><td>A connection between two nodes (an arc)</td><td>A–B, A–C, B–C, B–D, C–D</td></tr>
    <tr><td><b>Weight</b></td><td>A value on an edge: distance, cost, time</td><td>The numbers 4, 2, 1, 5, 8</td></tr>
    <tr><td><b>Path</b></td><td>The list of nodes connected by edges between two given nodes</td><td>A, C, B, D (cost 2 + 1 + 5 = 8)</td></tr>
    <tr><td><b>Cycle</b></td><td>A list of nodes that returns to the same node</td><td>A, B, C, A</td></tr>
    <tr><td><b>Neighbours</b></td><td>Nodes joined to a node by an edge</td><td>The neighbours of C are A, B and D</td></tr>
  </table></div>
  <p>The graph above is <b>undirected</b>: an edge can be used in either direction. A <b>directed</b> graph has arrows, so an edge can only be followed one way, as in a one-way street. A graph with weights is a <b>weighted</b> graph; the shortest path between two nodes is the path whose weights add up to the least. Which path has the fewest edges is not always the cheapest: from A to D, A–B–D has 2 edges and costs 9, but A–C–B–D has 3 edges and costs 8.</p>

  <h2>2 · Storing a graph</h2>
  <p>A graph can be stored in a program as an <b>adjacency matrix</b> (a table with a row and a column for every node, holding the weight where there is an edge) or an <b>adjacency list</b> (each node with a list of its neighbours and weights). You will not be asked to write code for a graph.</p>
  ''' + matrix + alist + '''

  <h2>3 · Why graphs are used in AI</h2>
  <ul>
    <li>They <b>record relationships</b> between entities in a way algorithms can use: places and the distances between them, people in a social network, web pages and links.</li>
    <li>Many AI problems can be defined as <b>finding a path in a graph</b>: the best route for a delivery van or a satnav, the shortest route a game character takes, or the sequence of moves that reaches a goal.</li>
    <li>Graphs can be analysed by a range of algorithms, for example <b>Dijkstra's algorithm</b> and the <b>A* algorithm</b> (next page), which are used in machine learning and path-finding.</li>
    <li><b>Artificial neural networks</b> can be represented as graphs: neurons are nodes and the weighted connections are edges.</li>
  </ul>
  <p>To justify using a graph for a situation, say what the nodes are, what the edges and weights are, and what question the graph will answer. For example, for a delivery company: nodes are towns, edges are roads, weights are distances, and the graph is searched for the shortest route.</p>

  <h2>4 · Common ways to lose marks</h2>
  <ul>
    <li>Describing a graph as a chart or a bar graph. In AI a graph is a set of nodes and edges.</li>
    <li>Mixing up nodes and edges: nodes are the entities, edges are the connections.</li>
    <li>Not saying what the weights mean when a question gives a situation.</li>
    <li>Writing that a graph "finds" the route. The graph stores the data; an algorithm such as Dijkstra's finds the route.</li>
    <li>Choosing the path with the fewest nodes instead of the lowest total weight.</li>
  </ul>
'''

watch = '''
  <h2>1 · Building a graph</h2>
  <p>Press Play. Nodes are entities, edges connect them, weights add meaning.</p>
  <div id="stA"></div>
  <h2>2 · Fewest edges is not the cheapest path</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Paths between two towns</h2>
  <p>The graph is the one from the M/J 2021 question. Choose two towns and see every simple path between them, with its cost.</p>
  <div class="card"><div class="btnrow"><select id="gF" style="font:inherit;padding:6px"></select> to <select id="gT" style="font:inherit;padding:6px"></select></div><div id="gG"></div><div id="gP"></div></div>

  <h2>Lab 2 · Neighbours and degree</h2>
  <p>Click a town to see its neighbours.</p>
  <div class="card"><div id="nB" class="btnrow"></div><div class="verdict" id="nV"></div></div>
'''

practise = '''
  <h2>1 · Node or edge?</h2><div id="cl1" class="card"></div>
  <h2>2 · What is each part in this situation?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Put the steps of using a graph in AI in order</h2><div id="o1" class="card"></div>
  <h2>5 · Counting</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A satnav", "Junctions are nodes, roads are edges and the distances or journey times are weights. The satnav searches the graph for the cheapest route.", "a graph stores places and distances for a path search.") +
rw("Social networks", "People are nodes and friendships are edges. The graph lets a site suggest people you might know, a friend of a friend.", "graphs record relationships between entities.") +
rw("A video game map", "Characters move across a graph of locations. The game uses it to find a route round obstacles.", "path-finding in games.") +
rw("Rail and flight networks", "Stations or airports are nodes and services are edges weighted by time or cost, so a planner can find the quickest or cheapest journey.", "weighted edges.") +
rw("The internet", "Routers are nodes and links are edges. Routing protocols use graph algorithms to decide where to send packets.", "networks are graphs.")
)

where = [
  ("M/J 2021", "31, 32, 33", "5(b)", "3", "Explain the use of graphs to aid AI (Dijkstra's calculation in 5(a) is on the next page)"),
  ("M/J 2025", "31", "10(a)", "2", "The purpose of a graph in an AI system"),
  ("M/J 2025", "32", "6(a)", "2", "The structure of a graph in an AI system")]

past = '''  <p class="note">The theory of graphs has been asked in Paper 3 in May/June 2021 and May/June 2025; most graph questions use a graph and ask for Dijkstra's or A* (next page). The graphs of those questions are redrawn there. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "31/32/33", "Q5(b)"), "3 marks", "Explain",
  "Explain the use of graphs to aid Artificial Intelligence (AI).",
  "Relationships between nodes; AI problems as finding a path; algorithms such as A* and Dijkstra's.",
  "<p>Any three: " + mks(["Artificial neural networks can be represented using graphs", "Graphs provide structures for relationships between nodes", "AI problems can be defined or solved as finding a path in a graph", "Graphs may be analysed by a range of algorithms", "for example the A* or Dijkstra's algorithm", "used in machine learning"]) + "</p>", "Writing about graphs as charts. The question is about nodes, edges and path-finding.") + peq(SRC("s25", "31", "Q10(a)"), "2 marks", "Describe",
  "Describe the purpose of a graph when used in an Artificial Intelligence (AI) system.",
  "Record relationships, with nodes and edges, for example distances on a map to find the shortest route.",
  "<p>Any two: " + mks(["A graph is used in AI to record relationships between entities", "using vertices (nodes) and edges", "for example to represent places on a map and the distances between them, in order to find the shortest route"]) + "</p>", None) + peq(SRC("s25", "32", "Q6(a)"), "2 marks", "Describe",
  "Describe the structure of a graph as used in an Artificial Intelligence (AI) system.",
  "Nodes, edges, weights, path, cycle.",
  "<p>Any two: " + mks(["A graph uses vertices (nodes) to identify or represent entities such as destinations or people", "Edges are used to connect nodes and can represent possible paths between them; a path is the list of nodes connected by edges between two given nodes", "Nodes or edges can be labelled or weighted, and this weighting can be used in the context of the application", "A cycle is a list of nodes that returns to the same node"]) + "</p>", "Describing the picture only. Say what nodes and edges represent and that edges can be weighted.")

review = req("3 marks", "Explain", "A delivery company wants to find the quickest route between its depot and 20 towns. Explain how a graph could be used.", "Nodes, edges, weights, algorithm.", "<p>" + mks(["Each town and the depot is a node and each road between them is an edge", "The weight on each edge is the journey time", "An algorithm such as Dijkstra's searches the graph for the path with the lowest total weight"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between a path and a cycle in a graph.", "Where does it end?", "<p>" + mks(["A path is a list of nodes connected by edges between two given nodes", "A cycle is a list of nodes that returns to the node it started from"]) + "</p>", None) + req("2 marks", "State", "In the graph of this page, state the cost of the path A, B, D and the cost of A, C, B, D.", "Add the weights.", "<p>" + mks(["A, B, D costs 4 + 5 = 9", "A, C, B, D costs 2 + 1 + 5 = 8"]) + "</p>", None) + req("2 marks", "State", "State what a directed graph shows that an undirected graph does not.", "One-way streets.", "<p>" + mks(["Edges have a direction", "An edge can only be followed in the direction of its arrow"]) + "</p>", None) + req("2 marks", "Describe", "Describe how a social network could be represented as a graph.", "Who are the nodes?", "<p>" + mks(["Each person is a node", "A friendship is an edge between two people"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on the purpose and structure of graphs in AI (Paper 3), 2021 and 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Nodes and edges.", "Nodes are the entities; edges are the connections."),
  ("Weights mean something.", "Distance, cost or time: say which."),
  ("Path v cycle.", "A path joins two nodes; a cycle returns to its start."),
  ("A graph stores; an algorithm searches.", "Dijkstra's and A* find the best path."),
  ("Fewest edges is not cheapest.", "Add up the weights."),
  ("Justify with a situation.", "Say what the nodes, edges and weights are."),
], [
  ("a graph", "Nodes joined by edges, used to represent relationships."),
  ("a weight", "A value on an edge such as a distance."),
  ("a path", "A list of nodes connected by edges between two nodes."),
  ("a cycle", "A list of nodes that returns to the same node."),
], [("Describe", "Say what it is and what it contains."), ("Explain", "Give uses and reasons."), ("State", "Short answer."), ("Distinguish", "Say how they differ.")]) + FC

js = AKJS + AK20JS + AK18JS + "const GS = " + json.dumps({"nodes": {n: list(p) for n, p in G["nodes"].items()}, "edges": [list(e) for e in G["edges"]], "start": "Base"}) + ", GA = " + json.dumps({"nodes": {n: list(p) for n, p in G1["nodes"].items()}, "edges": [list(e) for e in G1["edges"]], "start": "A"}) + ";\n" + r'''
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
''' + CLASSIFY("cl1", "Is it a node or an edge?", ["Node", "Edge"],
  [("A town", 0), ("A road between two towns", 1), ("A person in a social network", 0), ("A friendship", 1), ("A router", 0), ("A cable between routers", 1)],
  "Nodes are the things; edges are the connections.") + CLASSIFY("cl2", "In a road map graph, what is it?", ["Node", "Edge", "Weight"],
  [("A junction", 0), ("A road", 1), ("The length of a road in km", 2), ("A town", 0), ("The journey time of a road", 2), ("A motorway link", 1)],
  "Junctions are nodes, roads edges, distances or times weights.") + MATCH([
  ["Vertex", "Another name for a node"], ["Edge", "A connection between two nodes"], ["Weight", "A distance, cost or time on an edge"], ["Path", "The nodes connected by edges between two nodes"], ["Cycle", "A path that returns to the same node"]]) + ORDER(
  "Put the steps of using a graph to plan a route in order.",
  ["Represent the places as nodes", "Connect them with edges", "Add the distances as weights", "Run a search algorithm such as Dijkstra's", "Read off the path with the lowest total weight"],
  "Nodes, edges, weights, algorithm, result.") + CALC([
  {"q": "In the A, B, C, D graph, what is the cost of the path A, C, D?", "a": 10, "unit": "", "tol": 0.01, "hint": "2 + 8.", "sol": "<b>10</b>."},
  {"q": "How many edges does the graph A, B, C, D have?", "a": 5, "unit": "", "tol": 0.01, "hint": "Count the lines.", "sol": "<b>5</b>."},
  {"q": "How many neighbours does node C have?", "a": 3, "unit": "", "tol": 0.01, "hint": "A, B and D.", "sol": "<b>3</b>."},
  {"q": "What is the cost of the cheapest path from A to D?", "a": 8, "unit": "", "tol": 0.01, "hint": "A, C, B, D.", "sol": "<b>8</b>."},
  {"q": "A complete graph with 4 nodes has an edge between every pair. How many edges?", "a": 6, "unit": "", "tol": 0.01, "hint": "4 × 3 ÷ 2.", "sol": "<b>6</b>."}]) + MCQ([
  ("A graph in AI is made of:", ["Bars", "Nodes and edges", "Rows only", "Pixels"], 1, "Nodes and edges."),
  ("A weight on an edge could be:", ["A distance", "A colour", "A font", "A name"], 0, "A distance, cost or time."),
  ("A cycle is:", ["A path that returns to the same node", "A node with no edges", "A weight", "A table"], 0, "It returns to the start."),
  ("Which algorithm can search a graph for a shortest path?", ["Dijkstra's", "Bubble sort", "Binary search", "Hashing"], 0, "Dijkstra's."),
  ("A directed graph has:", ["Edges with a direction", "No nodes", "Only weights", "No edges"], 0, "Arrows."),
  ("Neural networks can be represented as:", ["Graphs", "Tables only", "Text", "Images only"], 0, "Neurons are nodes.")], "qz1") + CARDS([
  ("Graph", "Nodes joined by edges; records relationships."), ("Weight", "Distance, cost or time on an edge."), ("Path", "Nodes connected by edges between two nodes."), ("Cycle", "A path returning to its start."),
  ("Directed", "Edges can only be followed one way."), ("Why in AI", "AI problems become path-finding in a graph."), ("Algorithms", "Dijkstra's and A*."), ("Storage", "Adjacency matrix or adjacency list.")])

build("ac1811", "ac-18-1-1-graphs-in-ai", "Graphs in Artificial Intelligence", EYA("18.1.1"),
  "The purpose and structure of a graph: nodes, edges, weights, paths and cycles, and why graphs aid AI; animations, a path explorer and the real Paper 3 questions from 2021 and 2025.",
  dict(sub=CBK("Chapter 18 · Artificial Intelligence, section 18.1 Artificial Intelligence"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
