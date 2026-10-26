"""A Level CS syllabus 18.1.2: Dijkstra's and A* algorithms. Run: python3 tools/artifact-kit/mk_ac1812.py"""
from ak18 import *

graph_check()
GP = GRAPHS


def dans(key, order):
    st, d, pv = dijkstra(GP[key])
    return "<p><b>Answers:</b> " + ", ".join(f"{n} = {d[n]}" for n in order) + "</p>"


def dq(key, order):
    return gsx(GP[key], cap="graph") + '<div class="tw"><table class="t mono"><tr>' + "".join(f"<th>{n}</th>" for n in order) + "</tr><tr>" + "<td></td>" * len(order) + "</tr></table></div>"


DM = mks(["Initialisation: the start node set to 0", "and the rest of the nodes set to ∞", "Evidence of values at nodes being updated", "Evidence of 'visited' nodes", "A correct calculation of at least one route", "More than one route calculated for at least one node"])
S = GP["s21"]
_, ds, ps = dijkstra(S)

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Dijkstra's algorithm</b> finds the <b>shortest path from a start node to every other node</b> in a weighted graph: it sets the start to 0 and all other nodes to ∞, repeatedly visits the unvisited node with the smallest distance, and updates its neighbours if the route through it is shorter. The <b>A* algorithm</b> finds the <b>best path between two nodes</b>, start and goal, and is faster because it uses a <b>heuristic</b> (an estimate of the distance still to go) to try the most promising nodes first, instead of exploring all routes. A* chooses the node with the lowest <b>f = g + h</b>, where <b>g</b> is the cost so far and <b>h</b> is the heuristic. Dijkstra's algorithm always finds the shortest path; A* may not if its heuristic is inaccurate. You will not be asked to write these algorithms, but you must be able to <b>work them through on a graph</b>.</p></div>

  <h2>1 · Purpose</h2>
  <p>Both algorithms perform a <b>search on a graph</b> to find a path between points. They are used in satnavs, route planners, game character movement and robot navigation, to find the optimal, shortest or most cost-effective route based on distance, cost or time.</p>

  <h2>2 · Dijkstra's algorithm</h2>
  <ol>
    <li><b>Initialise</b>: give the start node distance 0 and every other node ∞.</li>
    <li>Choose the <b>unvisited node with the smallest distance</b> and mark it <b>visited</b> (its distance is now final).</li>
    <li>For each unvisited neighbour, work out <b>distance of this node + weight of the edge</b>. If it is less than the neighbour's current value, replace it (and note the route).</li>
    <li>Repeat from step 2 until every node is visited (or the destination is visited).</li>
    <li>Read the final distances, and follow the recorded routes back to get each path.</li>
  </ol>
  <h3>Worked example (M/J 2021)</h3>
  <p>Shortest distance from Base to each town.</p>
  ''' + gsx(S, cap="Dijkstra worked example") + dist_table(S) + '''
  <p>Each row shows the distances after one more node has been visited (bold = visited, so final). For Town 5 the route Base, Town 3, Town 5 costs 2 + 1 = 3, which beats Base, Town 2, Town 5 (5 + 3 = 8), so Town 5 = 3. The answers: Town 1 = 3, Town 2 = 5, Town 3 = 2, Town 4 = 9, Town 5 = 3, Town 6 = 8.</p>
  <p>What the mark scheme looks for in your working (up to three marks) and in the answers (two marks: all correct, or four or five correct):</p>
  <ul>
    <li>Start node set to 0, all the rest to ∞.</li>
    <li>Values at nodes updated as you go.</li>
    <li>Visited nodes shown.</li>
    <li>A route calculated, and more than one route calculated for at least one node.</li>
  </ul>

  <h2>3 · The A* algorithm</h2>
  <p>A* is used to find a path from a <b>start node to a goal node</b>. Every node has a <b>heuristic h</b>: an estimate of the cost from that node to the goal (for a map, the straight-line distance). For each node A* keeps:</p>
  <ul>
    <li><b>g</b>: the cost of the route from the start to the node found so far;</li>
    <li><b>h</b>: the heuristic, the estimated cost from the node to the goal;</li>
    <li><b>f = g + h</b>: the estimated total cost of a route through this node.</li>
  </ul>
  <ol>
    <li>Put the start node in the table with g = 0 and its h.</li>
    <li>Choose the node with the <b>lowest f</b> that has not been expanded.</li>
    <li>For each neighbour, work out g (the current node's g plus the edge weight), look up h, and write the row: start node, destination node, g, h and f.  Only note a neighbour again if this route to it is <b>cheaper</b> than one already found.</li>
    <li>Stop when the goal is the node with the lowest f. The final path is found by following back through the nodes you came from.</li>
  </ol>
  <h3>Worked example (O/N 2021)</h3>
  <p>Find a path from Home to School. The number beside each node is its heuristic.</p>
  ''' + gsx(GP["w21"], h=True, cap="A* worked example") + astar_table(GP["w21"]) + '''
  <p>A* expanded Home, A, E and F, but never needed C or D: it found the path Home, A, E, F, School (cost 11) without exploring the whole graph.</p>

  <h2>4 · Dijkstra and A* compared</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Dijkstra's algorithm</th><th>A* algorithm</th></tr>
    <tr><td><b>Finds</b></td><td>The shortest path from the start to <b>every</b> node</td><td>A path from the start to <b>one</b> goal node</td></tr>
    <tr><td><b>Uses</b></td><td>Only the distance travelled so far</td><td>A <b>heuristic</b> as well: f = g + h, giving priority to nodes that seem better</td></tr>
    <tr><td><b>Explores</b></td><td>All possible routes (simply checks each vertex)</td><td>Does not need to pass through all nodes or paths</td></tr>
    <tr><td><b>Always shortest?</b></td><td>Yes</td><td>May not be, if the heuristic is inaccurate</td></tr>
    <tr><td><b>Speed</b></td><td>Slower on a big graph</td><td>Faster when the heuristic is good</td></tr>
  </table></div>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Not showing the working: ∞ for unvisited nodes, updated values, and which nodes are visited.</li>
    <li>Choosing the node with the smallest edge weight instead of the smallest total distance from the start.</li>
    <li>In A*, choosing the lowest g or lowest h instead of the lowest <b>f = g + h</b>.</li>
    <li>Saying that A* "always finds the shortest path". It depends on the heuristic.</li>
    <li>Giving only one route to each node. Show a second route where there is one, to show you compared them.</li>
  </ul>
'''

watch = '''
  <h2>1 · Dijkstra's algorithm, one node at a time</h2>
  <p>Press Play. The number under each node is its current distance from the Base; green nodes are visited and final.</p>
  <div id="stA"></div>
  <h2>2 · The A* algorithm</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Dijkstra's algorithm</h2>
  <p>Choose a graph from a past paper and move the slider to see each node being visited.</p>
  <div class="card"><div id="dB" class="btnrow"></div><div id="dS"></div><div id="dG"></div><div id="dT"></div></div>

  <h2>Lab 2 · A* with and without a heuristic</h2>
  <p>Choose a graph. With the heuristic off, every h is 0 and A* behaves like Dijkstra's algorithm: count the rows.</p>
  <div class="card"><div id="aB" class="btnrow"></div><div id="aH" class="btnrow"></div><div id="aG"></div><div id="aT"></div></div>
'''

practise = '''
  <h2>1 · Dijkstra's or A*?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which does the A* table column mean?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Put the steps of Dijkstra's algorithm in order</h2><div id="o1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Finding the quickest way home", "A route planner models the roads as a graph and runs a shortest-path search. A* is popular because the straight-line distance to your destination gives a good heuristic.", "A* uses a heuristic to search less.") +
rw("Characters in a game", "A character that has to walk from one side of a level to a door uses A* on a grid or map of locations, so it takes a sensible route round walls.", "path-finding for one start and one goal.") +
rw("Internet routing", "Routing protocols use shortest-path algorithms like Dijkstra's to decide the cheapest route across a network of routers.", "Dijkstra's finds the shortest path to every node.") +
rw("A robot vacuum", "It builds a map of your rooms as a graph and plans the route to cover them and get back to its charger.", "weights can be distance or energy.") +
rw("Emergency vehicles", "A planner can weight edges by travel time that includes traffic, so the quickest route changes through the day.", "weights are costs such as time.")
)

where = [
  ("M/J 2021", "31, 32, 33", "5(a)", "5", "Dijkstra's algorithm on a seven-node graph"),
  ("O/N 2021", "31, 32", "9(b)", "5", "A* on a graph of Home, School and six nodes"),
  ("M/J 2023", "31, 33", "2(b)", "2", "The purpose of the A* and Dijkstra's algorithms"),
  ("M/J 2023", "32", "10(b)", "5", "A* from Begin to End"),
  ("O/N 2023", "32", "8", "5", "Dijkstra's algorithm from Start"),
  ("M/J 2025", "33", "10(a), (b)", "1 + 2", "The purpose of A* and Dijkstra's; the difference between them"),
  ("O/N 2025", "31", "7(a)", "1", "Identify an AI algorithm to find the shortest distance between two points"),
  ("O/N 2025", "33", "8", "5", "Dijkstra's algorithm from Start"),
  ("M/J 2026", "31", "9(b)", "5", "Dijkstra's algorithm from Begin"),
  ("M/J 2026", "32", "9(b)", "3 + 5", "How A* differs from Dijkstra's; Dijkstra's algorithm from Home"),
  ("M/J 2026", "33", "9(b)", "5", "A* from W to E")]

past = '''  <p class="note">Graph searches have been set in Paper 3 in most series: a Dijkstra's calculation (about 5 marks, nodes and weights given) or an A* table, together with a purpose or difference question. The graphs are redrawn here; the paper's tables give the first rows of the A* working. In the answers the working table is generated by working the algorithm through, so rows may be in a slightly different order from the mark scheme, which accepts correct calculations in any order. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Purpose and difference</h3>
''' + peq(SRC("s23", "31/33", "Q2(b)"), "2 marks", "Describe",
  "Describe the purpose of both the A* algorithm and Dijkstra's algorithm.",
  "Optimal route between nodes, using distance, cost or time.",
  "<p>" + mks(["To find the optimal, shortest or most cost-effective route", "between two nodes in a graph", "based on distance, cost or time"]) + " (two of these three points)</p>", None) + peq(SRC("w25", "31", "Q7(a)"), "1 mark", "Identify",
  "Identify one Artificial Intelligence (AI) algorithm to find the shortest distance between two points on a graph.",
  "Either of the two.",
  "<p>" + mks(["A* algorithm, or Dijkstra's algorithm"]) + "</p>", None) + peq(SRC("s25", "33", "Q10(a)(b)"), "1 + 2 marks", "State / Outline",
  "(a) State the purpose of the A* and Dijkstra's algorithms. (b) Outline the difference between the A* and Dijkstra's algorithms.",
  "(b) A* uses a heuristic; Dijkstra's explores all routes.",
  "<p><b>(a)</b> " + mks(["To find the path between two points on a graph"]) + "</p><p><b>(b)</b> Any two: " + mks(["A* tries to find a better path by using a heuristic function; it finds the adjacent route with the shortest path and continues until the destination is reached", "Dijkstra's just explores all possible routes", "The heuristic function in A* gives priority to nodes that are supposed to be better than others", "Dijkstra's algorithm cannot work with negative weights, whereas the mark scheme also accepts that A* can"]) + "</p>", None) + peq(SRC("s26", "32", "Q9(b)(i)"), "3 marks", "Outline",
  "The A* and Dijkstra's algorithms are used to perform searches on a graph. Outline how the A* algorithm is different from Dijkstra's algorithm.",
  "Heuristics; not all nodes; Dijkstra's always shortest.",
  "<p>Any three: " + mks(["The A* algorithm tries to find the shortest path using heuristics (intelligent guesses)", "The A* algorithm does not necessarily pass through all nodes or paths", "Dijkstra's algorithm finds the shortest path to all nodes: it simply checks each vertex looking for the shortest path", "Dijkstra's algorithm always finds the shortest path", "The A* algorithm may not find the shortest path if the heuristics are inaccurate"]) + "</p>", "Writing that A* is 'faster' without the reason. The reason is the heuristic.") + '''
  <h3>Dijkstra's algorithm</h3>
''' + peq(SRC("s21", "31/32/33", "Q5(a)"), "5 marks", "Calculate",
  "Calculate the shortest distance between the base and each of the other towns in the diagram using Dijkstra's algorithm. Show your working and write your answers in the table provided." + dq("s21", ["Town 1", "Town 2", "Town 3", "Town 4", "Town 5", "Town 6"]),
  "Base = 0, others ∞. Visit Base, then Town 3 (2), then Town 1 (3) ...",
  "<p>Working, up to three: " + DM + " Answers, up to two: all six correct, or four or five correct.</p>" + dist_table(GP["s21"]) + dans("s21", ["Town 1", "Town 2", "Town 3", "Town 4", "Town 5", "Town 6"]), "Taking Town 5 as 8 (Base, Town 2, Town 5). The route via Town 3 is only 2 + 1 = 3. Always compare routes.") + peq(SRC("w23", "32", "Q8"), "5 marks", "Calculate",
  "Calculate the shortest distance between the Start and each of the destinations in the diagram using Dijkstra's algorithm. Show your working and write your answers in the table provided." + dq("w23", list("ABCDEF")),
  "Start is 0; the next node to visit is A (8) then F (10).",
  "<p>Working and answers as in the mark scheme (working up to three marks, answers two): </p>" + dist_table(GP["w23"]) + dans("w23", list("ABCDEF")), None) + peq(SRC("w25", "33", "Q8"), "5 marks", "Calculate",
  "Calculate the shortest distance between the Start node and each of the nodes in the graph using Dijkstra's algorithm. Show your working on the graph or in the working space." + dq("w25", list("TVWXYZ")),
  "Y looks close to Start (22) but T, V, X, Y is shorter.",
  "<p>" + DM + "</p>" + dist_table(GP["w25"]) + dans("w25", list("TVWXYZ")), "Using the direct edge Start to Y (22). The route Start, T, V, X, Y costs 6 + 4 + 9 + 3 = 22 as well; X is 18 via W (6 + 4 + 3 + 5), so Y = 21.") + peq(SRC("s26", "31", "Q9(b)"), "5 marks", "Calculate",
  "Calculate the best path between the Begin node and each of the nodes in the diagram using Dijkstra's algorithm. Show your working and write your answers in the table provided." + dq("s26_31", list("PQRSTU")),
  "Begin to R is 6, then P via R is 2 more.",
  "<p>" + DM + "</p>" + dist_table(GP["s26_31"]) + dans("s26_31", list("PQRSTU")), "Taking P as 9 (the direct edge). Begin, R, P costs 6 + 2 = 8.") + peq(SRC("s26", "32", "Q9(b)(ii)"), "5 marks", "Calculate",
  "Calculate the best path between the Home node and each of the nodes in the diagram using Dijkstra's algorithm. Show your working and write your answers in the table provided." + dq("s26_32", list("ABCDEF")),
  "Home to F directly is 16, but via A it is 6 + 8 = 14.",
  "<p>" + DM + "</p>" + dist_table(GP["s26_32"]) + dans("s26_32", list("ABCDEF")), None) + '''
  <h3>A* algorithm</h3>
''' + peq(SRC("w21", "31/32", "Q9(b)"), "5 marks", "Calculate",
  "Find a path between the Home and School nodes using the A* algorithm. Show your working in the table provided. The first two rows in the table have been completed (Home: g 0, h 14, f 14; A: g 1, h 10, f 11). The number by each node is its heuristic." + gsx(GP["w21"], h=True, cap="O/N 2021 Q9"),
  "Always expand the node with the lowest f.",
  "<p>One mark for each correct calculation (max 4): " + mks(["Node B and node C (from Home)", "Node B and node E (from A)", "Node F and node School (from E)", "Node School (from F)"]) + " One mark for the correct path (max 1).</p>" + astar_table(GP["w21"]), "Expanding B because it has the lowest g, not the lowest f. A* uses f = g + h.") + peq(SRC("s23", "32", "Q10(b)"), "5 marks", "Calculate",
  "Calculate the path that takes the shortest time to travel from the Begin node to the End node, using the A* algorithm. Show your working in the table provided. The first two rows have already been completed (Begin: g 0, h 12, f 12; A: g 5, h 8, f 13)." + gsx(GP["s23"], h=True, cap="M/J 2023 Q10"),
  "Lowest f after Begin is C.",
  "<p>One mark per correct calculation (max 4): " + mks(["B, C and D (from Begin)", "G (from C)", "F and End (from G)", "End (from F)"]) + " One mark for the path: Begin, C, G, F, End.</p>" + astar_table(GP["s23"]), None) + peq(SRC("s26", "33", "Q9(b)"), "5 marks", "Calculate",
  "Calculate the best path between the W and E nodes using the A* algorithm. Show your working in the table provided. The first two rows are done (W: g 0, h 18, f 18; N1: g 6, h 15, f 21)." + gsx(GP["s26_33"], h=True, cap="M/J 2026 Q9"),
  "N2 has the lowest f first (4 + 14 = 18).",
  "<p>One mark per correct calculation (max 4): " + mks(["W to N2 and W to N3", "W, N2 to N5", "W, N2, N5 to N4 and to N6", "W, N2, N5, N6 to E"]) + " One mark for the correct path: W, N2, N5, N6, E.</p>" + astar_table(GP["s26_33"]) + "<p>The table here also lists the improved route to N3 (6 via N2 against 7 direct); the mark scheme does not require it.</p>", None)

review = req("3 marks", "Calculate", "A graph has nodes S, A, B, T. Edges: S–A 2, S–B 6, A–B 3, A–T 7, B–T 2. Use Dijkstra's algorithm from S. State the shortest distance to each node.", "Visit S, A, then B.", "<p>" + mks(["A = 2 (S–A)", "B = 5 (S, A, B) not 6", "T = 7 (S, A, B, T) not 9 (S, A, T)"]) + "</p>", None) + req("2 marks", "Explain", "In A*, a node has g = 8 and h = 5. State its f and explain what f is used for.", "f = g + h.", "<p>" + mks(["f = 8 + 5 = 13", "A* expands the unexpanded node with the lowest f, the estimated total cost of a route through it"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a good heuristic makes A* faster than Dijkstra's algorithm.", "Which nodes are explored?", "<p>" + mks(["The heuristic estimates the distance still to go, so nodes that look better are tried first", "A* does not have to explore every route, so fewer nodes are examined"]) + "</p>", None) + req("2 marks", "Describe", "Give one situation where A* is better than Dijkstra's algorithm and one where Dijkstra's is needed.", "One goal or all nodes?", "<p>" + mks(["A*: finding a route between one start and one destination, for example a satnav", "Dijkstra's: finding the shortest distances from one node to all others, or when no good heuristic is available"]) + "</p>", None) + req("2 marks", "State", "State the values a node holds at the start of Dijkstra's algorithm.", "Start and others.", "<p>" + mks(["The start node has distance 0", "Every other node has distance ∞"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on Dijkstra's and the A* algorithms (Paper 3), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Dijkstra: start 0, others ∞.", "Write it down; it earns the working marks."),
  ("Visit the smallest distance.", "Then update neighbours: distance + weight, if smaller."),
  ("Show two routes.", "Compare them for at least one node."),
  ("A*: lowest f = g + h.", "Not the lowest g or h."),
  ("Dijkstra: all nodes, always shortest.", "A*: one goal, heuristic, may not be shortest."),
  ("Check the path.", "Add the weights of your final path."),
], [
  ("Dijkstra's algorithm", "Finds the shortest path from a start node to every node."),
  ("A* algorithm", "Finds a path to one goal using a heuristic."),
  ("a heuristic", "An estimate of the cost still to go."),
  ("f = g + h", "Cost so far plus estimated cost to the goal."),
], [("Calculate", "Work the algorithm, showing the working."), ("Outline", "Main points only."), ("State", "Short answer."), ("Identify", "Name it.")]) + FC

GJ = {k: {"start": v["start"], "goal": v.get("goal"), "h": v.get("h"), "nodes": {n: list(p) for n, p in v["nodes"].items()}, "edges": [list(e) for e in v["edges"]]} for k, v in GP.items()}
js = AKJS + AK20JS + AK18JS + "const GG = " + json.dumps(GJ) + ";\n" + r'''
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
''' + CLASSIFY("cl1", "Dijkstra's algorithm or the A* algorithm?", ["Dijkstra's", "A*"],
  [("Finds the shortest path to every node", 0), ("Uses a heuristic", 1), ("Always finds the shortest path", 0), ("May not find the shortest path if the heuristic is poor", 1), ("Chooses the node with the lowest f = g + h", 1), ("Explores all possible routes", 0)],
  "A* uses a heuristic and one goal; Dijkstra's explores everything.") + CLASSIFY("cl2", "What does it stand for in the A* table?", ["g", "h", "f"],
  [("The cost of the route from the start so far", 0), ("The estimated cost still to go", 1), ("g + h", 2), ("Used to choose the next node to expand", 2), ("Often the straight-line distance to the goal", 1), ("Adds the edge weights along the path", 0)],
  "g travelled, h estimated, f the total.") + MATCH([
  ["Dijkstra's algorithm", "Shortest path from a start node to all nodes"], ["A* algorithm", "Path to one goal using a heuristic"], ["Heuristic", "An estimate of the cost to the goal"], ["Visited node", "A node whose distance is final"], ["∞", "The starting value of every node except the start"]]) + ORDER(
  "Put the steps of Dijkstra's algorithm in order.",
  ["Set the start node to 0 and all others to ∞", "Visit the unvisited node with the smallest distance", "Update each neighbour if the route through this node is shorter", "Repeat until all nodes are visited", "Read off the shortest distances"],
  "Initialise, visit, update, repeat, read.") + CALC([
  {"q": "In A*, a node has g = 7 and h = 6. What is f?", "a": 13, "unit": "", "tol": 0.01, "hint": "g + h.", "sol": "<b>13</b>."},
  {"q": "Dijkstra: node X = 5. An edge from X to Y has weight 4 and Y is currently ∞. What does Y become?", "a": 9, "unit": "", "tol": 0.01, "hint": "5 + 4.", "sol": "<b>9</b>."},
  {"q": "Y is currently 9 and a new route gives 5 + 3 = 8. What does Y become?", "a": 8, "unit": "", "tol": 0.01, "hint": "The smaller value.", "sol": "<b>8</b>."},
  {"q": "M/J 2021 graph: the shortest distance from Base to Town 6.", "a": 8, "unit": "", "tol": 0.01, "hint": "Base, Town 3, Town 5, Town 6 = 2 + 1 + 5.", "sol": "<b>8</b>."},
  {"q": "O/N 2021 A* graph: the cost of the path Home, A, E, F, School.", "a": 11, "unit": "", "tol": 0.01, "hint": "1 + 6 + 1 + 3.", "sol": "<b>11</b>."}]) + MCQ([
  ("Which algorithm uses a heuristic?", ["Dijkstra's", "A*", "Bubble sort", "Binary search"], 1, "A*."),
  ("In Dijkstra's algorithm, unvisited nodes start at:", ["0", "1", "∞", "−1"], 2, "Infinity."),
  ("A* chooses the node with the lowest:", ["g", "h", "f = g + h", "weight"], 2, "f."),
  ("Which always finds the shortest path?", ["A*", "Dijkstra's", "Neither", "Both always, whatever h"], 1, "Dijkstra's."),
  ("What is h in A*?", ["Cost so far", "Estimated cost to the goal", "Number of edges", "The start node"], 1, "The heuristic."),
  ("Both algorithms are used to search a:", ["Graph", "Sorted list", "Stack", "Queue"], 0, "A graph.")], "qz1") + CARDS([
  ("Dijkstra's", "Shortest path from the start to all nodes; start 0, others ∞."), ("A*", "Path to one goal; f = g + h; heuristic."), ("Heuristic", "Estimate of the cost still to go."), ("f = g + h", "Cost so far plus estimate to the goal."),
  ("Visited", "Distance final."), ("Update", "New distance if smaller: distance + weight."), ("Difference", "A* uses a heuristic; Dijkstra's explores all routes."), ("Working marks", "0 and ∞, updates, visited, routes compared.")])

build("ac1812", "ac-18-1-2-dijkstra-a-star", "Dijkstra's and A* Algorithms", EYA("18.1.2"),
  "Dijkstra's shortest-path algorithm and the A* algorithm worked through on the graphs from the past papers, and how they differ; animations, search labs and the real Paper 3 questions from 2021 to 2026.",
  dict(sub=CBK("Chapter 18 · Artificial Intelligence, section 18.1 Artificial Intelligence"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
