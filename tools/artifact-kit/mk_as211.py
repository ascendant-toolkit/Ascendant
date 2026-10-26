"""AS CS syllabus 2.1.1: networks, LAN and WAN, client-server and peer-to-peer, thin and thick clients, topologies. Run: python3 tools/artifact-kit/mk_as211.py"""
import json
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>network</b> is a group of computers and devices connected so they can share data and resources. A <b>LAN</b> covers a small area (a building) on equipment the owner controls, and a <b>WAN</b> covers a large area (cities or countries) using external, shared infrastructure. In a <b>client-server</b> network one or more servers provide services and manage the network for clients, while in a <b>peer-to-peer</b> network every computer has equal status and shares its own resources. A <b>thin client</b> leaves almost all processing to the server; a <b>thick client</b> does most of its own processing and storage. The way devices are connected is the <b>topology</b>: bus, star, mesh or a hybrid of them, each with its own cost, speed and fault tolerance.</p></div>

  <h2>1 · LAN and WAN</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>LAN (local area network)</th><th>WAN (wide area network)</th></tr>
    <tr><td><b>Area</b></td><td>Small geographical area: a building or site</td><td>Large geographical area: between cities or countries</td></tr>
    <tr><td><b>Infrastructure</b></td><td>Privately owned, dedicated hardware; no leased lines needed</td><td>Often external or public infrastructure, non-dedicated hardware</td></tr>
    <tr><td><b>Connections</b></td><td>Wired or wireless; usually physical links</td><td>Often virtual, over leased or public links</td></tr>
    <tr><td><b>Speed</b></td><td>Higher data transfer rate</td><td>Lower data transfer rate</td></tr>
    <tr><td><b>Security</b></td><td>Easier to protect</td><td>Harder to protect</td></tr>
  </table></div>
  <p>Benefits of connecting computers in a LAN: <b>sharing</b> files and data, <b>sharing resources</b> such as printers and software, <b>communication</b> between devices, and <b>central management</b> of security and backups. The internet is the biggest WAN.</p>

  <h2>2 · Client-server and peer-to-peer</h2>
  <ul>
    <li><b>Client-server</b>: one or more <b>servers</b> store the files, run services and manage security and backup; the <b>clients</b> request services from them. The server performs the tasks asked of it and sends the results back.</li>
    <li><b>Peer-to-peer</b>: <b>all computers are of equal status</b>. Each shares its own files and resources and is responsible for its own security. There is no central server.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th></th><th>Client-server</th><th>Peer-to-peer</th></tr>
    <tr><td><b>Benefits</b></td><td>Central management of security, backup and software; easier to control access; reliable and scalable</td><td>Cheap and simple to set up; no dedicated server or administrator; no single point of failure</td></tr>
    <tr><td><b>Drawbacks</b></td><td>Expensive to buy and maintain a server; if the server fails the clients lose the service; a network manager is needed</td><td>No central security: only as secure as the weakest computer, each at risk from viruses on the others; no central backup; slower when others use your computer; files only available while that computer is on</td></tr>
    <tr><td><b>Suits</b></td><td>A school, company or bank with many users and sensitive data</td><td>A few friends or a small home network sharing files</td></tr>
  </table></div>
  <h3>Thin client and thick client</h3>
  <ul>
    <li><b>Thin client</b>: depends on the server for processing and storage. It only sends requests and displays the results. Cheap, easy to manage and secure, but useless if the server or network is down.</li>
    <li><b>Thick client</b>: does most of its own processing, with software and data installed locally. It works without the server for much of the time, but the clients cost more and each needs updating.</li>
  </ul>

  <h2>3 · Topologies</h2>
  <div class="grid2"><div class="card"><b>Bus</b><div class="synd" data-topo="bus"></div><p>All devices share one backbone cable. Data goes along it and each device looks at the address. Cheap and simple, but only one device can transmit at a time, so there are <b>collisions</b>; a break in the backbone stops everything.</p></div>
  <div class="card"><b>Star</b><div class="synd" data-topo="star"></div><p>Every device connects directly to a central <b>switch</b>. Packets go from the sender to the switch, which checks the destination address and forwards them <b>only to the intended receiver</b>. Fewer collisions, easy to add devices and find faults; if one cable fails only that device is lost, but if the switch fails everything is.</p></div>
  <div class="card"><b>Mesh</b><div class="synd" data-topo="mesh"></div><p>Each device is connected to at least one other, often several. There are <b>multiple routes</b>, so a failed link can be avoided and nodes act as relays. Very reliable and secure, but expensive: a full mesh of n devices needs n(n − 1) ÷ 2 links.</p></div>
  <div class="card"><b>Hybrid</b><div class="synd" data-topo="hybrid"></div><p>A combination of topologies, for example stars joined by a bus backbone. Used in larger networks where different areas have different needs.</p></div></div>
  <p>To justify a topology for a situation, give a reason tied to the situation: a classroom of 20 computers on a switch suits a <b>star</b> (a fault stays local, higher performance, easy to add computers); a few buildings that must stay connected if a cable is cut suit a <b>mesh</b>.</p>

  <h2>4 · Common ways to lose marks</h2>
  <ul>
    <li>Writing "it is bigger" for a WAN. Say the geographical area, the use of public or leased infrastructure and the lower data rate.</li>
    <li>Drawing a star topology with devices connected to each other. In a star every device connects only to the switch (or server).</li>
    <li>Describing a thick client as a computer with a bigger screen. It is about where the processing and storage are.</li>
    <li>Giving drawbacks of peer-to-peer as "slow" with no reason. Say no central security or backup, or that files are only available while that computer is on.</li>
    <li>Saying a mesh is "better" with nothing more. Say multiple routes, so a failed line is avoided.</li>
  </ul>
'''

watch = '''
  <h2>1 · Packets in a star network</h2>
  <p>Press Play. The packet goes via the switch only to the receiver.</p>
  <div id="stA"></div>
  <h2>2 · Packets on a bus, and a collision</h2>
  <div id="stB"></div>
  <h2>3 · A mesh finds another route</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · How many cables?</h2>
  <p>Choose the number of devices. See how many cables each topology needs.</p>
  <div class="card"><div id="nS"></div><div id="nT"></div></div>
  <h2>Lab 2 · What if a cable fails?</h2>
  <p>Choose a topology and click a cable to break it. Devices that can no longer reach the others are shown in red.</p>
  <div class="card"><div id="fB" class="btnrow"></div><div id="fG"></div><div class="verdict" id="fV"></div></div>
  <h2>Lab 3 · Which model?</h2>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>
'''

_pr, _prjs = PR(["LAN or WAN?", "Client-server or peer-to-peer?", "Match the term to its meaning", "Put the star-network steps in order", "Working out", "Multiple choice"],
  ("Is the description a LAN or a WAN?", ["LAN", "WAN"], [("Covers a small geographical area", 0), ("Uses leased or public infrastructure", 1), ("Normally privately owned", 0), ("The internet is the largest one", 1), ("Higher data transfer rate", 0), ("Covers several cities", 1)], "LAN: small, private, fast. WAN: large, shared, slower."),
  ("Which network model does it describe?", ["Client-server", "Peer-to-peer"], [("A central server manages security and backup", 0), ("All computers have equal status", 1), ("Needs a network manager and a server", 0), ("Each computer is responsible for its own security", 1), ("Suits a few friends sharing files", 1), ("Suits a company with sensitive data", 0)], "Server in charge, or all peers equal."),
  [["LAN", "A network covering a small area on private equipment"], ["Thin client", "Relies on the server for processing"], ["Thick client", "Does most of its own processing"], ["Star topology", "Every device connects to a central switch"], ["Mesh topology", "Multiple routes between devices"]],
  ("Put the steps in order for a packet in a star network.", ["The sending device sends the packet to the switch", "The switch reads the destination address", "The switch forwards the packet only to the receiver", "The receiving device accepts the packet"], "Send, read, forward, receive."),
  [{"q": "How many cables does a star network of 8 devices need (one to each device from the switch)?", "a": 8, "unit": "", "tol": 0.01, "hint": "One per device.", "sol": "<b>8</b>."}, {"q": "How many links does a full mesh of 5 devices need?", "a": 10, "unit": "", "tol": 0.01, "hint": "5 × 4 ÷ 2.", "sol": "<b>10</b>."}, {"q": "How many links does a full mesh of 6 devices need?", "a": 15, "unit": "", "tol": 0.01, "hint": "6 × 5 ÷ 2.", "sol": "<b>15</b>."}, {"q": "In a star network of 20 computers one computer's cable is cut. How many computers lose their connection?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only that one.", "sol": "<b>1</b>."}, {"q": "In a bus network the backbone cable is cut in the middle. Is the network still fully connected? Enter 0 for no, 1 for yes.", "a": 0, "unit": "", "tol": 0.01, "hint": "It splits in two.", "sol": "<b>0</b>."}],
  [("What is a WAN?", ["A network in one room", "A network covering a large geographical area", "A type of cable", "A printer"], 1, "A wide area network."), ("Which is a peer-to-peer feature?", ["A central server", "All computers have equal status", "Needs an administrator", "Thin clients"], 1, "Equal status."), ("In a star network packets are forwarded by the:", ["Switch", "Printer", "Monitor", "Keyboard"], 0, "The central switch."), ("A thin client:", ["Does most processing locally", "Relies on the server", "Has no screen", "Needs no network"], 1, "It relies on the server."), ("Which topology has multiple routes between devices?", ["Bus", "Star", "Mesh", "None"], 2, "Mesh."), ("A drawback of a bus network is:", ["Collisions on the shared cable", "Too many cables", "Needs a switch for every device", "No data can be sent"], 0, "Collisions.")],
  [("LAN", "Small area, private, fast."), ("WAN", "Large area, external infrastructure."), ("Client-server", "Server manages; clients request."), ("Peer-to-peer", "All equal; no central control."), ("Thin client", "Server does the processing."), ("Thick client", "Does its own processing."), ("Star", "All to one switch; fault stays local."), ("Mesh", "Many routes; very reliable; costly.")])

real = RWNOTE + (
rw("Your home Wi-Fi", "Your phone, laptop and TV connect to one router. That is a star: every device talks to the router, not to each other directly.", "star topology around a central device.") +
rw("A school computer room", "Every computer connects to a switch, and the switch connects to the server. If one cable fails, only one computer is lost.", "star, with the server managing logins and files.") +
rw("Chromebooks and web apps", "A Chromebook does little itself and relies on web services. That is close to a thin client.", "thin clients rely on the server.") +
rw("Sharing a file between friends' laptops", "Two laptops on the same Wi-Fi can share a folder directly. Each is both giving and receiving: a small peer-to-peer network.", "peers have equal status.") +
rw("The internet", "Millions of networks joined by many routes: if one link is cut, data finds another way. That is the idea of a mesh at a huge scale.", "multiple routes give reliability.")
)

where = [
  ("M/J 2021", "11, 13", "4(a), (b)", "2 + 4", "Key features of a peer-to-peer network; two drawbacks of using one"),
  ("O/N 2021", "11, 13", "8(a)", "3", "LAN or WAN for a school building, with justification"),
  ("O/N 2021", "12", "3(b)(i)", "2", "Identify and justify the topology of a home network"),
  ("M/J 2023", "12", "1(a), (b), (c), (e)", "2 + 2 + 2 + 2", "Benefits and characteristics of a LAN; draw a star; the thick-client model"),
  ("M/J 2023", "13", "2(a)-(d)", "2 + 4 + 2 + 4", "WAN against LAN; mesh topology; thin clients; wired and wireless connections"),
  ("O/N 2023", "11", "2(d)", "2", "One advantage of a star over a bus topology"),
  ("O/N 2023", "12", "7(b)(i)", "2", "Draw a star topology"),
  ("O/N 2024", "13", "9(a)", "2", "The characteristics of a WAN"),
  ("M/J 2025", "12", "6(a), (d)", "2 + 4", "How a WAN differs from a LAN; draw and label a star topology"),
  ("O/N 2025", "12", "5(a)-(c)", "2 + 2 + 3", "Characteristics of a LAN; complete a star diagram; how packets travel in a star")]

past = '''  <p class="note">Network types, models and topologies are asked in Paper 1 almost every series; star-topology drawings and 'how packets are transmitted' are the most repeated. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "11/13", "Q4(a)(b)"), "2 + 4 marks", "Describe",
  "Melinda and her friends set up a peer-to-peer network between their computers to share data. (a) Describe the key features of a peer-to-peer network. (b) Describe two drawbacks to Melinda and her friends of using a peer-to-peer network.",
  "(a) Equal status, shared resources, own security. (b) Two drawbacks, each with a reason.",
  "<p><b>(a)</b> Any two: " + mks(["All computers are of equal status", "Each computer provides access to resources and data (data is distributed)", "Computers can communicate and share resources", "Each computer is responsible for its own security"]) + "</p><p><b>(b)</b> Two drawbacks, a mark each plus up to one expansion each (max 2 per drawback): " + mks(["Reduced security: there is no central management of security", "so it is only as secure as the weakest computer, and each is at risk from viruses from the others"]) + " " + mks(["No central management of backup", "so if the data on one computer is not backed up it is lost to all of them"], "a") + " Other drawbacks accepted: no central management of files or software (inconsistent versions); computers respond slowly while others use them; computers must all be switched on to share files.</p>", "Giving a drawback such as 'it is slower' with no reason. Say why: other computers are using it, or files are not available when a computer is off.") + peq(SRC("w21", "11/13", "Q8(a)"), "3 marks", "State / Justify",
  "A school is setting up a network within one of its buildings. State whether the network will be a LAN (local area network) or a WAN (wide area network). Justify your choice.",
  "Identify it, then two reasons.",
  "<p>" + mks(["LAN", "Small geographical area", "No leasing of external infrastructure or transmission media; the internet is not used to transmit within the building"]) + "</p>", None) + peq(SRC("w21", "12", "Q3(b)(i)"), "2 marks", "Identify / Justify",
  "Andy has several devices that connect wirelessly to the router in his house. Identify the topology of Andy's home network. Justify your choice.",
  "Everything connects to one central device.",
  "<p>" + mks(["Star topology"]) + " " + mks(["Devices are connected directly to the router independently; all devices are only connected to the router"], "a") + "</p>", None) + peq(SRC("s23", "12", "Q1"), "2 + 2 + 2 + 2 marks", "Give / Draw / Describe",
  "A company has a LAN. (a) Give two benefits of connecting computers to a LAN. (b) Give two characteristics of a LAN. (c) One of the company's offices has one server and four computers connected in a star topology. Draw a diagram to show the layout of the office's star topology. (e) The network runs as a thick-client model. Describe what is meant by a thick-client model." + '<div class="circ"><svg viewBox="0 0 300 180" style="width:300px;max-width:100%"><text class="sm" x="10" y="20">(draw your diagram here)</text></svg></div>',
  "(c) Everything connects only to the central device.",
  "<p><b>(a)</b> Any two: " + mks(["Allows the sharing of files or data, or communication between devices", "Allows the sharing of resources such as hardware or software (applications)", "Allows central management, for example backup and security"]) + "</p><p><b>(b)</b> Any two: " + mks(["Covers a small geographical area", "The infrastructure is privately owned, not controlled by external organisations"], "a") + "</p><p><b>(c)</b> " + mks(["Each computer directly connected only to the server (the central device)", "All components correctly labelled"]) + '</p><div class="synd" data-topo="star"></div><p><b>(e)</b> ' + mks(["The server performs minimal or some processing for the client", "The clients do most of their own processing independently, or most of the resources are installed locally"], "n") + "</p>", "Joining the computers to each other as well. In a star each computer connects only to the central switch or server.") + peq(SRC("s23", "13", "Q2(a)-(d)"), "2 + 4 + 2 + 4 marks", "Identify / Describe / Explain",
  "A university has two sites connected as a WAN. (a) Identify two differences between a WAN and a LAN. (b) In one building five computers are connected in a mesh topology. (i) Describe what is meant by a mesh topology. (ii) Give two advantages of using a mesh topology instead of a bus topology. (c) The computers in one room are set up as thin clients in a client-server model. Describe the role of the different computers in this model. (d) Students can connect their devices to the university network using cables or a wireless connection. Explain the benefits to the students of allowing them to use both.",
  "(c) Server does the work; clients request and display.",
  "<p><b>(a)</b> Any two: " + mks(["A WAN covers a large geographical area and a LAN a small one", "LAN connections are usually physical, WAN connections are often virtual", "A LAN has a high data transfer rate and a WAN a low one", "A LAN is privately owned; a WAN may be private or public", "A LAN is usually more secure"]) + "</p><p><b>(b)(i)</b> Any two: " + mks(["All computers are connected to at least one other device", "There are multiple routes between devices", "The computers can act as relays, passing packets on towards the destination"], "a") + " <b>(ii)</b> Any two: " + mks(["If one line goes down there are more routes available", "Improved security as one main line is not used", "No or fewer collisions", "New nodes can be added without interruption"], "n") + "</p><p><b>(c)</b> " + mks(["The server performs all the processes required by the task and/or data storage", "The clients only send requests to the server and display the returned results"]) + "</p><p><b>(d)</b> Any four, for example: " + mks(["Some students might only have one sort of connection on their device", "Wired gives better performance, for example faster access to databases, and less interference", "Wired lets students transmit private or confidential work securely", "Wireless lets students use their devices in different rooms, sites or outside, more freely", "Wireless lets students bring multiple devices or change devices"]) + "</p>", "Describing a mesh as 'lots of cables' without saying why: each device is connected to at least one other and there are multiple routes.") + peq(SRC("w23", "11", "Q2(d)"), "2 marks", "Explain",
  "A new classroom is being set up with 20 computers and a switch. Explain one advantage of implementing a star topology instead of a bus topology in the new classroom.",
  "One advantage with its reason.",
  "<p>One advantage and one expansion: " + mks(["Star is more resilient to faults, because there is no single cable and so less disruption", "Higher performance, because there are fewer collisions as each device connects only to the switch", "Easier to add new nodes, because each connects directly to the switch", "Easier to fault-find compared with a bus topology"]) + "</p>", "Giving the advantage with no reason. The second mark is for the reason, for example 'because there is no single backbone cable'.") + peq(SRC("w25", "12", "Q5(a)-(c)"), "2 + 2 + 3 marks", "Describe / Complete",
  "A local area network (LAN) has five computers, one switch and one server. (a) Describe the characteristics of a LAN. (b) Complete the diagram to show how these devices are connected in a star topology. (c) Describe how packets are transmitted between two hosts using a star topology.",
  "(c) sender to switch, switch checks the address, forwards only to the receiver.",
  "<p><b>(a)</b> Any two: " + mks(["Covers a small geographical area", "Normally privately owned or dedicated infrastructure", "Can use wired or wireless communication"]) + "</p><p><b>(b)</b> " + mks(["All computers directly connected to the switch and no other connections", "The switch connected directly to the server"], "a") + '</p><div class="synd" data-topo="star"></div><p><b>(c)</b> ' + mks(["The sending device sends the packets to the switch", "The switch checks the destination address on each packet", "and sends them only to the intended receiver"], "n") + "</p>", None) + peq(SRC("s25", "12", "Q6(a)(d)"), "2 + 4 marks", "State / Draw",
  "A company has multiple sites in different cities. (a) State two ways that a WAN is different to a LAN. (d) The main office has four wired computers, one server, two printers, one central switch and a device providing a single point of access for the internet. The network is a star topology. Draw the topology for the main office network. Label all devices.",
  "Everything connects to the switch, including the server, printers and the internet router.",
  "<p><b>(a)</b> Any two: " + mks(["A WAN lets devices connect over a larger geographical area; a LAN a smaller one", "A WAN may use non-dedicated hardware; a LAN usually dedicated", "A WAN uses external transmission media; a LAN usually company-owned"]) + "</p><p><b>(d)</b> " + mks(["The server directly connected to the switch", "Four labelled computers all connected directly to the switch", "Two printers each directly connected to the switch (or server or a computer)", "A router or modem directly connected to the switch (or server) for internet access"], "a") + "</p>", None)

review = req("2 marks", "Explain", "Explain why a thin client cannot be used when the server is switched off.", "Where is the processing?", "<p>" + mks(["A thin client depends on the server for processing and storage", "It only sends requests and displays results, so without the server it can do nothing"]) + "</p>", None) + req("3 marks", "Explain", "A small business has six computers. Explain whether client-server or peer-to-peer is the better choice if they handle customers' bank details.", "Think about security and backup.", "<p>" + mks(["Client-server", "A server centrally manages security (access rights, antivirus) and backups", "Peer-to-peer would leave each computer responsible for its own security, so the weakest computer puts the data at risk"]) + "</p>", None) + req("2 marks", "Describe", "Describe one disadvantage of a bus topology.", "Shared cable.", "<p>" + mks(["All devices share one backbone cable, so only one can transmit at a time and collisions occur", "If the backbone breaks the whole network (or part of it) fails"]) + " (one of these with its explanation)</p>", None) + req("3 marks", "Explain", "A hospital has three buildings that must always stay connected. Explain why a mesh topology could suit it.", "Multiple routes.", "<p>" + mks(["Each building is connected to at least one other, with several routes", "If one link fails data can go another way", "So the network is reliable (but it costs more cable)"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between a LAN and a WAN.", "Area and ownership.", "<p>" + mks(["A LAN covers a small area, usually in one building, on privately owned equipment", "A WAN covers a large area, such as between cities, using external or leased links"]) + "</p>", None)

tips = tips_html([
  ("Star: everything to the switch.", "Never connect devices to each other."),
  ("LAN: small, private. WAN: large, shared.", "Give the area and who owns the infrastructure."),
  ("Peer-to-peer: equal status.", "No central security or backup."),
  ("Thin client: server does the work.", "Thick client does its own processing."),
  ("Mesh: multiple routes.", "Reliable but costly."),
  ("Justify with the situation.", "Link the topology or model to the people and data in the question."),
], [("a LAN", "A network covering a small area on privately owned equipment."), ("a topology", "The way devices are connected in a network."), ("a thin client", "A client that relies on the server for processing."), ("peer-to-peer", "A network where all computers have equal status.")],
  [("State / Identify", "Give the answer only."), ("Describe", "Say what it is or how it works."), ("Explain", "Give the reason as well."), ("Justify", "Give reasons for a choice.")]) + FC

js = AKJS + AK20JS + r'''
const TOPO = {
  star: { n: { SW: [150, 100, "switch"], A: [50, 40, "PC"], B: [250, 40, "PC"], C: [50, 160, "server"], D: [250, 160, "printer"], E: [150, 28, "PC"] }, e: [["SW", "A"], ["SW", "B"], ["SW", "C"], ["SW", "D"], ["SW", "E"]] },
  bus: { n: { A: [50, 45, "PC"], B: [120, 165, "PC"], C: [190, 45, "server"], D: [260, 165, "PC"], BA: [50, 105, ""], BB: [120, 105, ""], BC: [190, 105, ""], BD: [260, 105, ""], E1: [15, 105, ""], E2: [290, 105, ""] }, e: [["E1", "BA"], ["BA", "BB"], ["BB", "BC"], ["BC", "BD"], ["BD", "E2"], ["A", "BA"], ["B", "BB"], ["C", "BC"], ["D", "BD"]] },
  mesh: { n: { A: [150, 20, "PC"], B: [255, 80, "PC"], C: [215, 165, "PC"], D: [85, 165, "PC"], E: [45, 80, "PC"] }, e: [["A", "B"], ["A", "C"], ["A", "D"], ["A", "E"], ["B", "C"], ["B", "D"], ["B", "E"], ["C", "D"], ["C", "E"], ["D", "E"]] },
  hybrid: { n: { S1: [60, 100, "switch"], S2: [240, 100, "switch"], A: [20, 40, "PC"], B: [20, 160, "PC"], C: [280, 40, "PC"], D: [280, 160, "PC"], BB1: [105, 100, ""], BB2: [195, 100, ""] }, e: [["S1", "A"], ["S1", "B"], ["S2", "C"], ["S2", "D"], ["S1", "BB1"], ["BB1", "BB2"], ["BB2", "S2"]] }
};
function topoSvg(kind, o) { o = o || {}; const T = TOPO[kind]; let s = "";
  T.e.forEach(([a, b]) => { const x1 = T.n[a][0], y1 = T.n[a][1], x2 = T.n[b][0], y2 = T.n[b][1];
    const hot = o.hot && o.hot.some(([p, q]) => (p === a && q === b) || (p === b && q === a)), broken = o.broken && o.broken.some(([p, q]) => (p === a && q === b) || (p === b && q === a));
    s += SV.line(x1, y1, x2, y2, "ax", { style: "stroke:" + (broken ? "var(--bad)" : hot ? "var(--good)" : "var(--muted)") + ";stroke-width:" + (hot ? 4 : broken ? 3 : 2) + (broken ? ";stroke-dasharray:5 5" : "") }); });
  Object.entries(T.n).forEach(([k, [x, y, t]]) => { if (!t) return; const cur = o.cur === k, lost = o.lost && o.lost.includes(k); s += SV.rect(x - 24, y - 15, 48, 30, lost ? "cell-no" : cur ? "cell-warn" : "cell", { rx: 6 }) + SV.text(x, y + 4, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); }); return s; }
document.querySelectorAll("[data-topo]").forEach((el) => (el.innerHTML = '<svg viewBox="0 0 300 190" style="width:300px;max-width:100%;display:block">' + topoSvg(el.dataset.topo) + "</svg>"));
(function () {
  const path = [["A", "SW"], ["SW", "C"]]; const seq = [{ cap: "Computer A wants to send a packet to the server. Every device is connected only to the central switch.", hot: [], cur: "A" }, { cap: "A sends the packet to the <b>switch</b>.", hot: [["A", "SW"]], cur: "SW" }, { cap: "The switch reads the <b>destination address</b> on the packet.", hot: [], cur: "SW" }, { cap: "It forwards the packet <b>only</b> to the server. No other device receives it, so there are few collisions.", hot: [["SW", "C"]], cur: "C" }];
  Lib.stepper($("#stA"), { w: 300, h: 190, label: "Star", base: { i: 0 }, draw: (s) => { const q = seq[Math.round(s.i)]; return topoSvg("star", { hot: q.hot, cur: q.cur }); }, tween: 100, dwell: 2600, steps: seq.map((q, i) => ({ cap: q.cap, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = topoSvg("bus", {}); const pk = (x, c) => SV.circle(x, 105, 8, c);
    if (k === 1) o += pk(50, "dot1") ; if (k === 2) o += pk(120, "dot1") + SV.text(120, 90, "→ to server", "sm", { "text-anchor": "middle" }); if (k === 3) o += pk(190, "dot3"); if (k === 4) o += pk(80, "dot1") + pk(230, "dot2") + SV.text(150, 90, "collision!", "lbl bd t2", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stB"), { w: 300, h: 190, label: "Bus", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "All devices share one backbone cable.", s: { i: 0 } }, { cap: "A sends a packet onto the backbone.", s: { i: 1 } }, { cap: "It travels along the cable past every device. Each looks at the address.", s: { i: 2 } }, { cap: "The server sees its own address and accepts the packet.", s: { i: 3 } }, { cap: "If two devices send at the same time, the signals <b>collide</b> and both must try again.", s: { i: 4 } }] });
})();
(function () {
  const seq = [{ cap: "Computer A sends a packet to C. There are several routes.", hot: [["A", "C"]], br: [] }, { cap: "The direct link A to C is cut.", hot: [], br: [["A", "C"]] }, { cap: "The packet goes another way: A to B to C. Devices act as <b>relays</b>.", hot: [["A", "B"], ["B", "C"]], br: [["A", "C"]] }];
  Lib.stepper($("#stC"), { w: 300, h: 190, label: "Mesh", base: { i: 0 }, draw: (s) => { const q = seq[Math.round(s.i)]; return topoSvg("mesh", { hot: q.hot, broken: q.br }); }, tween: 100, dwell: 2800, steps: seq.map((q, i) => ({ cap: q.cap, s: { i } })) });
})();
(function () {
  let n = 8; const paint = () => { $("#nT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Topology</th><th>Cables / links needed</th></tr>' + `<tr><td>Bus</td><td>1 backbone + ${n} connections</td></tr><tr><td>Star</td><td>${n} (one from each device to the switch)</td></tr><tr><td>Full mesh</td><td><b>${(n * (n - 1)) / 2}</b> (n × (n − 1) ÷ 2)</td></tr></table></div><div class="verdict">With ${n} devices a full mesh needs <b>${(n * (n - 1)) / 2}</b> links against ${n} for a star. That is why a full mesh is expensive.</div>`; };
  Lib.slider($("#nS"), { id: "ns", label: "Devices ", min: 2, max: 20, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();
(function () {
  let kind = "star", broken = []; const b = $("#fB"), g = $("#fG"); const ALT = { star: TOPO.star, mesh: TOPO.mesh };
  const lostOf = () => { const T = TOPO[kind], names = Object.keys(T.n), hub = kind === "star" ? "SW" : "A"; const adj = {}; names.forEach((x) => (adj[x] = [])); T.e.forEach(([p, q]) => { if (!broken.some(([a, c]) => (a === p && c === q) || (a === q && c === p))) { adj[p].push(q); adj[q].push(p); } }); const seen = new Set([hub]), st = [hub]; while (st.length) { const u = st.pop(); adj[u].forEach((v) => { if (!seen.has(v)) { seen.add(v); st.push(v); } }); } return names.filter((x) => !seen.has(x) && T.n[x][2]); };
  const paint = () => { const T = TOPO[kind], lost = lostOf(); g.innerHTML = '<svg viewBox="0 0 300 190" style="width:300px;max-width:100%;display:block;cursor:pointer" id="fSvg">' + topoSvg(kind, { broken, lost }) + "</svg>";
    $("#fSvg").onclick = (e) => { const r = e.currentTarget.getBoundingClientRect(), x = ((e.clientX - r.left) / r.width) * 300, y = ((e.clientY - r.top) / r.height) * 190; let best = null, bd = 18; T.e.forEach(([p, q], i) => { const [x1, y1] = T.n[p], [x2, y2] = T.n[q]; const dx = x2 - x1, dy = y2 - y1, t = Math.max(0, Math.min(1, ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy || 1))), d = Math.hypot(x - (x1 + t * dx), y - (y1 + t * dy)); if (d < bd) { bd = d; best = [p, q]; } }); if (best) { const i = broken.findIndex(([a, c]) => (a === best[0] && c === best[1])); if (i >= 0) broken.splice(i, 1); else broken.push(best); paint(); } };
    $("#fV").innerHTML = broken.length ? (lost.length ? "Devices cut off: <b>" + lost.map((x) => T.n[x][2] + " " + x).join(", ") + "</b>." : "<b>Nobody is cut off:</b> there is another route.") + " Click a broken cable again to repair it." : "Click a cable to break it.";
    b.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === kind ? "on" : "")); };
  ["star", "mesh"].forEach((k) => { const x = document.createElement("button"); x.textContent = k === "star" ? "Star" : "Mesh"; x.dataset.k = k; x.onclick = () => { kind = k; broken = []; paint(); }; b.appendChild(x); }); paint();
})();
btnTable("mB", "mO", [
  ["A company with many users and sensitive data", "Client-server", "Central security, backup and access control"],
  ["Three friends sharing music files", "Peer-to-peer", "Cheap and simple; no server needed"],
  ["A call centre of identical desks", "Thin clients", "Easy to manage; the server does the processing"],
  ["A designer editing large video files", "Thick client", "Processes locally; does not wait for the server"],
  ["A classroom of 20 computers", "Star topology", "Faults stay local; easy to add computers"],
  ["Hospital sites that must stay linked", "Mesh topology", "Several routes if a link fails"]
], ["Situation", "Choice", "Reason"]);
''' + _prjs

finish("as-2-1-1-networks-models-topologies", "as211", "Networks, Network Models and Topologies",
  "LANs and WANs, client-server and peer-to-peer models, thin and thick clients, and bus, star, mesh and hybrid topologies; animations, a cable-failure lab and the real Paper 1 questions from 2021 to 2025.",
  "2.1.1", "2 · Communication", "section 2.1 Networks including the internet", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on network types, models and topologies (Paper 1), 2021 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
