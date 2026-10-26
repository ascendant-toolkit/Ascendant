"""A Level CS syllabus 14.2.2: packet switching and routers. Run: python3 tools/artifact-kit/mk_ac1422.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Packet switching</b> splits a message into small <b>packets</b>, each with a <b>header</b> holding the source and destination IP addresses and a sequence number, and sends every packet <b>independently</b>, so different packets may take <b>different routes</b> and arrive <b>out of order</b>. A <b>router</b> at each step reads the destination IP address in the header, looks it up in its <b>routing table</b>, and sends the packet on its <b>next hop</b>. At the destination the packets are <b>reassembled</b> in the right order using the sequence numbers, and missing or damaged packets are <b>re-sent</b>. Because the bandwidth is shared and packets can be re-routed, packet switching suits data networks such as the internet, though reassembly takes time. You need to be able to describe it, state benefits and drawbacks, describe a router, and compare it with circuit switching.</p></div>

  <h2>1 · The packet</h2>
  <div class="tw"><table class="t mono">
    <tr><th colspan="4">Header</th><th>Payload</th></tr>
    <tr><td>source IP</td><td>destination IP</td><td>sequence number</td><td>hop count</td><td>a small piece of the message</td></tr>
  </table></div>
  <ul>
    <li>The message is divided into <b>equal-sized packets</b>.</li>
    <li>The <b>header</b> holds key information: the <b>source and destination IP addresses</b>, the <b>packet (sequence) number</b> and a <b>hop count</b>. The <b>payload</b> is the data.</li>
  </ul>

  <h2>2 · How packet switching passes a message across a network</h2>
  <ol>
    <li>The message is <b>divided</b> into packets.</li>
    <li>Each packet is given a <b>header</b> with the source and destination IP addresses and a sequence number.</li>
    <li>Each packet is sent <b>independently</b>, and may travel by a <b>different route</b>. Routers choose the <b>optimum route</b> at the time, depending on congestion and availability, and re-route if a route is unavailable.</li>
    <li>The packets <b>may arrive out of order</b>.</li>
    <li>At the destination the packets are <b>reassembled</b> into the original message, in the correct order, using the sequence numbers.</li>
    <li>If a packet is <b>missing or damaged</b> a <b>re-send request</b> is made and it is sent again; if a packet's hop count runs out it is discarded and a re-send can be requested.</li>
  </ol>
  <div class="tip"><b class="h">Complete message received</b>Two ways packet switching makes sure a complete message arrives: packets are <b>checked on arrival</b> and a re-send is requested for any that are damaged or missing; and packets are routed <b>individually</b>, so if a route is blocked a packet is sent another way.</div>

  <h2>3 · The router</h2>
  <p>A <b>router</b> connects networks and passes packets on towards their destination. When a packet arrives:</p>
  <ol>
    <li>It <b>reads the destination IP address</b> from the packet header.</li>
    <li>It looks in its <b>routing table</b>, which holds information such as the available <b>hops</b>, the <b>netmask</b>, the <b>gateway</b> to use, adjacent routers and the status of routes.</li>
    <li>It decides the <b>next hop</b> (the best route) and <b>sends the packet</b> on.</li>
    <li>It reduces the <b>hop count</b> by 1 each time. When it reaches 0 the packet is discarded.</li>
  </ol>
  <div class="tw"><table class="t mono">
    <tr><th>Destination network</th><th>Next hop</th></tr>
    <tr><td>10.0.0.0 / 8</td><td>Router B</td></tr>
    <tr><td>172.16.0.0 / 16</td><td>Router C</td></tr>
    <tr><td>192.168.1.0 / 24</td><td>deliver locally</td></tr>
    <tr><td>everything else (default)</td><td>Router D</td></tr>
  </table></div>

  <h2>4 · Benefits and drawbacks</h2>
  <div class="tw"><table class="t">
    <tr><th>Benefits</th><th>Drawbacks</th></tr>
    <tr><td>Packets can be <b>re-routed</b> around faulty or busy lines, so they are more likely to arrive</td><td><b>Delay</b>: packets must be reordered and reassembled at the destination</td></tr>
    <tr><td>A lost or damaged packet can be <b>re-sent</b> on its own</td><td>Delay from packets that must be re-sent, and from sharing bandwidth with other traffic</td></tr>
    <tr><td><b>Bandwidth is shared</b>: no line is tied up; many users use the same path</td><td>Needs a <b>complex algorithm</b> / protocols to work</td></tr>
    <tr><td>More secure: packets travel by different routes, so a message is harder to intercept</td><td>Needs a lot of memory (RAM) to handle large amounts of data. Not suitable for real-time use</td></tr>
  </table></div>

  <h2>5 · Packet switching against circuit switching</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Circuit switching</th><th>Packet switching</th></tr>
    <tr><td>Path</td><td>A dedicated circuit set up first</td><td>No dedicated path: each packet finds its own way</td></tr>
    <tr><td>Data</td><td>A continuous stream; the message stays intact</td><td>Split into packets</td></tr>
    <tr><td>Route</td><td>All the data follows the same route</td><td>Packets can take different routes</td></tr>
    <tr><td>Order</td><td>Arrives in the order sent</td><td>May arrive out of order; reassembled</td></tr>
    <tr><td>Bandwidth</td><td>The whole bandwidth is used and cannot be shared</td><td>Bandwidth is shared; variable</td></tr>
    <tr><td>Start</td><td>Set-up delay before sending</td><td>Sending can begin straight away</td></tr>
    <tr><td>If something is lost</td><td>The whole transmission may need to be resent</td><td>Individual packets can be resent</td></tr>
    <tr><td>Used for</td><td>Voice calls, real-time communication</td><td>Internet data: email, web pages, large files</td></tr>
  </table></div>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Not saying each packet is sent <b>independently</b> and may take a <b>different route</b>.</li>
    <li>Forgetting the header and what is in it: the IP addresses and sequence number.</li>
    <li>Describing a router as "something that connects computers". Say it reads the destination IP address, uses a routing table and sends the packet on its next hop.</li>
    <li>For benefits and drawbacks, giving "it is faster" or "it is slower" without a reason.</li>
    <li>In a comparison, describing each method separately without saying what is different.</li>
    <li>Describing checking for completeness and re-sending when the question says to leave it out.</li>
  </ul>
'''

watch = '''
  <h2>1 · A message split into packets and sent by different routes</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stA"></div>
  <h2>2 · What a router does with a packet</h2>
  <div id="stB"></div>
  <h2>3 · A missing packet is re-sent</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Send a message by packet switching</h2>
  <p>The message is split into packets and each takes one of three routes with different delays. Watch the order of arrival and the reassembly.</p>
  <div class="card"><div id="pS"></div><div class="btnrow"><label><input type="checkbox" id="pL"> lose packet 3 on its way</label></div><div class="btnrow"><button class="b pri" id="pG">Send the message</button></div><div id="pO"></div><div class="verdict" id="pV"></div></div>

  <h2>Lab 2 · Be the router</h2>
  <p>A packet arrives with a destination IP address. Look it up in the routing table.</p>
  <div class="card"><div id="rB" class="btnrow"></div><div id="rO"></div></div>

  <h2>Lab 3 · Circuit or packet?</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · Circuit switching or packet switching?</h2><div id="cl1" class="card"></div>
  <h2>2 · Benefit or drawback of packet switching?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps of packet switching in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Packets and hops</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Loading a web page", "The page is sent as many packets. They may reach your device by different routes and out of order, and your computer puts them back in order. If one is lost, only that packet is sent again.", "packets sent independently, reassembled at the destination, re-sent if missing.") +
rw("A router in your home", "Your home router reads the destination address of every packet from your devices and passes it to your internet provider's router, which passes it on, hop by hop.", "a router reads the destination IP address and uses a routing table to choose the next hop.") +
rw("A cable cut under the sea", "Internet traffic is re-routed along other cables, and users may only notice a slight slowdown, because there is no fixed circuit.", "packets can be re-routed around a failed route.") +
rw("Sending a large photo by email", "The photo is split into many packets that share the lines with everyone else's traffic. It arrives complete even though the packets travelled separately.", "bandwidth is shared; packets are reassembled.") +
rw("A video call that stutters", "Packets arriving late or out of order cause delays and glitches, which is why live calls are harder on a packet-switched network than a dedicated circuit.", "a drawback: delay while packets are reordered or re-sent.")
)

where = [
  ("M/J 2021", "31, 32, 33", "6", "4", "Two benefits and two drawbacks of packet switching"),
  ("O/N 2021", "31, 32", "6(a), 6(b)", "5 + 3", "Explain how packet switching transfers messages; the function of a router"),
  ("M/J 2022", "31, 33", "3", "8", "Describe circuit and packet switching with an advantage and a disadvantage of each"),
  ("M/J 2023", "32", "7", "2 + 4", "Two uses of packet switching; four differences from circuit switching"),
  ("O/N 2024", "32", "1", "3 + 4", "Describe packet switching; two benefits and two drawbacks"),
  ("M/J 2025", "31", "3(b)", "4", "Describe packet switching as a method of transmitting messages"),
  ("M/J 2025", "33", "4(b)", "4", "The function of a router in packet switching"),
  ("O/N 2025", "31", "3(c)", "4", "Two ways packet switching ensures a complete message is received"),
  ("O/N 2025", "32", "4", "2 + 2", "A benefit of each method; two differences"),
  ("O/N 2025", "33", "3", "4", "Describe how packet switching passes messages across a network")]

past = '''  <p class="note">Packet switching, and the router, appear in Paper 3 in almost every series from May/June 2021 to Oct/Nov 2025, often as a describe question plus benefits and drawbacks. Circuit switching on its own is on the previous page. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Describing packet switching</h3>
''' + peq(SRC("w25", "33", "Q3"), "4 marks", "Describe",
  "Describe how packet switching is used to pass messages across a network. Do not include checking for completeness and resending packets in your answer.",
  "Divide, header, independent routes, optimum route, reassemble.",
  "<p>Any four: " + mks(["The message is divided into small chunks called packets", "Each packet is given a header with important data, including the source and destination IP addresses", "Each packet is sent independently / can be sent through different routes", "Packets are sent through the optimum route, and can be re-routed if a route is unavailable", "Packets are reassembled at the destination into the whole message"]) + "</p>", "Describing the re-sending of lost packets. The question excludes it.") + peq(SRC("s25", "31", "Q3(b)"), "4 marks", "Describe",
  "Describe packet switching as a method of transmitting messages across the internet.",
  "Packets, headers, independent routes, order, missing packets.",
  "<p>Any four: " + mks(["Data are broken into equal-sized packets", "Packets have headers containing information such as the IP addresses of the sender and receiver", "Each packet is sent independently to the destination: packets do not necessarily follow the same route", "Each packet is sent by the most optimum path available", "Packets do not necessarily arrive in the order sent; they are reconstructed at the destination in the correct order", "Missing or damaged packets are re-sent"]) + "</p>", None) + peq(SRC("w24", "32", "Q1"), "3 + 4 marks", "Describe / State",
  "(a) Describe how packet switching is used to transmit messages across a network. (b) State two benefits and two drawbacks of packet switching as a method of transmitting messages across a network.",
  "(a) the process in order. (b) two of each, with a reason.",
  "<p><b>(a)</b> Any three: " + mks(["The data to be transmitted is divided into equal-sized packets", "A packet header is attached to each, containing the source and destination IP addresses and a packet number", "Packets are transmitted independently and may travel by different routes, determined using a routing table", "The packets usually arrive out of order and are reassembled in the correct order at the destination", "If packets are missing or corrupted, a re-transmission request is sent"]) + "</p><p><b>(b)</b> Benefits (max 2): " + mks(["Packets are more likely to arrive because they can be re-routed, and a lost packet can be re-transmitted", "Bandwidth can be shared: packets from different messages share the same path", "Considered secure because packets generally travel by different routes", "A high data transmission rate is possible"], "a") + " Drawbacks (max 2): " + mks(["Time delay because packets need to be re-ordered or re-sent, or the bandwidth is shared", "Requires a complex algorithm to function", "Needs lots of RAM to handle large amounts of data"], "a") + "</p>", None) + peq(SRC("w21", "31, 32", "Q6(a)"), "5 marks", "Explain",
  "Explain how packet switching is used to transfer messages across the internet.",
  "The message divided, header and payload, independent dispatch, routes, reassembly, re-send.",
  "<p>Any five: " + mks(["A large message is divided into smaller chunks of the same size called packets", "A packet has a header and a payload", "The header contains the source IP address, the destination IP address (and a sequence number)", "Each packet is dispatched independently and may travel along different routes", "The packets may arrive out of order", "and are reassembled into the original message at the destination", "If packets are missing or corrupted a re-transmission request is sent"]) + "</p>", None) + peq(SRC("w25", "31", "Q3(c)"), "4 marks", "Describe",
  "Describe two ways in which packet switching ensures a complete message is received when passing messages across a network.",
  "Two ways, each with a description worth two marks.",
  "<p>Two ways, 2 marks each: " + mks(["Packets are checked at the receiving end / on arrival", "if packets arrive damaged or do not arrive at all, a re-send request is sent"]) + " " + mks(["Packets are sent individually, by different routes", "if a route is blocked, the packet is sent through a different route so it arrives"], "a") + " (or: if the packet's hop count is exceeded the packet is retired, which can generate a re-send request)</p>", None) + '''
  <h3>The router</h3>
''' + peq(SRC("w21", "31, 32", "Q6(b)"), "3 marks", "Outline",
  "Outline the function of a router in packet switching.",
  "Header, destination address, routing table, next hop.",
  "<p>Any three: " + mks(["The router examines the packet's header and reads the destination IP address", "A router has access to a routing table", "containing information such as the available hops, netmask or gateway used, and the status of routes", "The router decides the next hop / best route and sends the packet on its next hop"]) + "</p>", None) + peq(SRC("s25", "33", "Q4(b)"), "4 marks", "Describe",
  "Describe the function of a router in packet switching.",
  "The same idea, plus the hop counter.",
  "<p>Any four: " + mks(["The router reads the IP address of the destination from the packet header", "It uses a routing table to find information", "about e.g. the available hops, netmask, gateway used, adjacent routers or the status of the routers along the route", "The router determines the next hop / optimum route, and sends the packet on its next hop", "The router manages the hop counter: the hop count is reduced by 1 every time the packet passes a router"]) + "</p>", "Saying the router 'sends the message'. It forwards each packet separately.") + '''
  <h3>Benefits, drawbacks and comparing methods</h3>
''' + peq(SRC("s21", "31, 32, 33", "Q6"), "4 marks", "Give",
  "Give two benefits and two drawbacks of packet switching.",
  "Two benefits and two drawbacks.",
  "<p>Benefits (max 2): " + mks(["Accuracy: delivery of the message is accurate", "Completeness: missing packets are detected and a re-send is requested", "Resilience: if the network changes, data can be sent another way", "The path is also available to other users: the bandwidth is not all used / simultaneous use by many users", "Better security: packets are sent by different routes"], "a") + " Drawbacks (max 2): " + mks(["Time delays to correct errors, or from errors in packets", "Requires complex protocols for delivery", "Unsuitable for real-time transmission applications"]) + "</p>", None) + peq(SRC("s22", "31, 33", "Q3"), "8 marks", "Describe",
  "Data can be sent over networks using either circuit switching or packet switching. Describe both methods of data transmission. Include a different advantage and disadvantage for each method.",
  "Four marks for each method: two description points, an advantage, a disadvantage.",
  "<p>Circuit switching (max 4): " + mks(["a dedicated circuit", "the circuit is established before transmission starts and released after", "data is transferred using the whole bandwidth", "all data is transferred over the same route", "Advantage: data / frames arrive in order and do not need to be reassembled", "Disadvantage: nobody else can use the circuit even if it is idle / less secure as only one route is used"]) + "</p><p>Packet switching (max 4): " + mks(["data is split into packets", "each packet is given its own route", "the routing for a packet depends on the congestion", "packets may not arrive in the order sent", "Advantage: packets can be rerouted if there are problems / more secure as harder to intercept", "Disadvantage: time taken to reassemble packets at the destination"], "a") + "</p>", "Giving the same advantage or disadvantage for both methods. The question asks for a different one for each.") + peq(SRC("s23", "32", "Q7"), "2 + 4 marks", "State / Give",
  "(a) State two examples of where it would be appropriate to use packet switching. (b) Give four differences between circuit switching and packet switching.",
  "(a) uses and why. (b) four pairs, each a comparison.",
  "<p><b>(a)</b> Any two: " + mks(["On data networks such as the internet to send large data files that do not need live streaming", "When it is necessary to overcome failed or faulty lines by re-routing", "When communication needs to be more secure", "For high volume data transmission / when all the bandwidth is not needed", "Specific examples such as email, text messages, documents, VoIP"]) + "</p><p><b>(b)</b> Any four: " + mks(["Circuit switching uses a dedicated channel; packet switching forms data into packets to send over a digital network", "A dedicated path is established before transfer in circuit switching; not in packet switching", "Data is split into packets in packet switching; in circuit switching the message stays intact", "All the data follows the same path in circuit switching; packets can take different routes", "Circuit switching delivers in order; packets may arrive out of order and are reassembled", "Circuit switching uses the whole bandwidth; packet switching shares it", "Circuit switching ends with an error if there is a fault; packet switching allows packets to be re-sent"], "a") + "</p>", None) + peq(SRC("w25", "32", "Q4"), "2 + 2 marks", "Identify",
  "(a) Identify one benefit of circuit switching and one benefit of packet switching. (b) Identify two differences between circuit switching and packet switching.",
  "One of each in (a); two comparisons in (b).",
  "<p><b>(a)</b> " + mks(["Circuit switching: once connected the circuit is available until the end; a steady rate; no delay to reorder; data less likely to be lost; suits real-time"]) + " " + mks(["Packet switching: bandwidth can be shared; faulty or busy lines can be avoided by re-routing; individual packets can be resent; good security because packets take different routes; a high data rate"], "a") + "</p><p><b>(b)</b> Any two: " + mks(["Circuit switching needs a dedicated line connected before the transfer; in packet switching data transfer can start straight away", "Circuit switching uses the whole bandwidth; packet switching shares it", "In circuit switching all the data follows the same route; packets can follow different routes", "In circuit switching data arrives in order; in packet switching it has to be reordered", "Data is a continuous stream in circuit switching but segmented in packet switching", "Lost data in circuit switching requires the whole transmission to be resent; individual packets can be resent in packet switching"]) + "</p>", None)

review = req("3 marks", "Describe", "A 1200-byte message is sent by packet switching in packets of 400 bytes. Describe what is added to each packet and what happens at the destination.", "Header, order, reassembly.",
  "<p>" + mks(["The message is split into 3 packets; each has a header with the source and destination IP addresses and a sequence number.", "The packets may arrive by different routes and out of order.", "At the destination they are put in order using the sequence numbers and reassembled into the message."]) + "</p>", None) + req("2 marks", "Explain", "Explain why packet switching is more resilient than circuit switching when a cable is cut.", "Alternative routes.",
  "<p>" + mks(["Each packet is routed independently, so routers can send packets by another route around the fault.", "In circuit switching all the data follows one route, so the transmission ends."]) + "</p>", None) + req("3 marks", "Describe", "A packet arrives at a router with destination IP address 172.16.4.9. Describe what the router does.", "Table, next hop, hop count.",
  "<p>" + mks(["It reads the destination IP address from the packet header.", "It looks the address up in its routing table to find the next hop.", "It reduces the hop count by 1 and sends the packet on to the next router."]) + "</p>", None) + req("2 marks", "State", "State two drawbacks of packet switching for a live video call.", "Delay and order.",
  "<p>" + mks(["Packets may arrive late or out of order and have to be reordered, causing delay.", "Lost packets have to be re-sent, which causes more delay."]) + "</p>", None) + req("2 marks", "Explain", "Explain why a packet has a hop count.", "What if it goes round in circles?",
  "<p>" + mks(["The hop count is reduced each time the packet passes a router.", "When it reaches zero the packet is discarded, so a packet cannot travel round the network forever."]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on packet switching, routers and comparing the two switching methods (Paper 3), 2021 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Packets, header, independent.", "Divided into packets; a header with IP addresses and a sequence number; each sent independently."),
  ("Different routes, any order.", "Packets may arrive out of order, so they are reassembled."),
  ("Router: header, table, next hop.", "Reads the destination IP, checks the routing table, sends it on its next hop, reduces the hop count."),
  ("Benefits with reasons.", "Re-routing, resending single packets, shared bandwidth, security by different routes."),
  ("Drawbacks with reasons.", "Delay reordering or resending, complex protocols, not for real time."),
  ("For comparisons, put both in each point.", "'Circuit switching ..., whereas packet switching ...'."),
], [
  ("what a packet is", "A small chunk of a message with a header holding the source and destination IP addresses and a sequence number."),
  ("what a router does", "It reads the destination IP address, uses its routing table to find the next hop and sends the packet on."),
  ("how a message is completed", "Packets are reassembled in order at the destination and any missing or damaged packets are re-sent."),
  ("a difference from circuit switching", "Circuit switching uses a dedicated route for all the data, whereas packets in packet switching can take different routes."),
], [("Describe", "Say how it works, in several points."), ("Outline", "Give the main steps."), ("State / Give", "Name the benefits or drawbacks."), ("Identify", "Name the difference or benefit.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const lanes = [40, 110, 180];
    o += SV.rect(20, 80, 90, 60, "f2", { rx: 8 }) + SV.text(65, 115, "Sender", "lbl bd", { "text-anchor": "middle" }) + SV.rect(650, 80, 90, 60, "f2", { rx: 8 }) + SV.text(695, 115, "Receiver", "lbl bd", { "text-anchor": "middle" });
    lanes.forEach((y, i) => (o += SV.line(110, 110, 380, y, "ax") + SV.line(380, y, 650, 110, "ax") + SV.rect(340, y - 16, 80, 32, "f3", { rx: 6 }) + SV.text(380, y + 5, "Router " + "ABC"[i], "lbl", { "text-anchor": "middle", style: "font-size:12px" })));
    const lane = [0, 1, 2, 0, 1, 2], pk = ["HE", "LL", "O ", "WO", "RL", "D!"];
    pk.forEach((d, i) => {
      if (k === 0) return;
      let x, y;
      if (k === 1) { x = 130; y = 50 + i * 22; }
      else if (k === 2) { x = 330 + (i > 2 ? 0 : 0) + (i % 3) * 0; y = lanes[lane[i]] + (i > 2 ? 22 : -22); x = 360 + (i > 2 ? 60 : 0); }
      else { x = 560 + (i % 3) * 32; y = 100 + (i > 2 ? 24 : 0) - 6; }
      if (k <= 3) o += SV.rect(x - 22, y - 10, 44, 20, "cell-warn", { rx: 3 }) + SV.text(x, y + 4, (i + 1) + ":" + d, "lbl bd", { "text-anchor": "middle", style: "font-size:11px;font-family:var(--mono)" });
    });
    if (k === 0) o += SV.text(115, 170, "HELLO WORLD!", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" });
    if (k === 3) o += SV.text(380, 232, "arrival order: 2, 1, 3, 5, 4, 6 (out of order)", "lbl bd t2", { "text-anchor": "middle", style: "font-size:14px" });
    if (k === 4) o += SV.text(380, 232, "reassembled by sequence number: 1 2 3 4 5 6 = HELLO WORLD!", "lbl bd t3", { "text-anchor": "middle", style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 245, label: "A message split into packets", base: { i: 0 }, draw, tween: 400, dwell: 3200, steps: [
    { cap: "The message \"HELLO WORLD!\" is to be sent. It is <b>divided</b> into equal-sized packets.", s: { i: 0 } },
    { cap: "Each packet gets a <b>header</b> (source and destination IP addresses, sequence number) and is sent <b>independently</b>.", s: { i: 1 } },
    { cap: "The packets take <b>different routes</b> through different routers, chosen by the routers at the time.", s: { i: 2 } },
    { cap: "They <b>arrive out of order</b>, because the routes differ in length and congestion.", s: { i: 3 } },
    { cap: "The receiver uses the <b>sequence numbers</b> to put them in order and <b>reassemble</b> the message.", s: { i: 4 } }] });
})();

(function () {
  const rows = ["1 Read the destination IP address in the packet header", "2 Look it up in the routing table", "3 Decide the next hop (the best route)", "4 Reduce the hop count by 1", "5 Send the packet on its next hop"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.rect(30, 20, 120, 44, "f2", { rx: 6 }) + SV.text(90, 48, "packet in", "lbl bd", { "text-anchor": "middle" }) + SV.rect(610, 20, 120, 44, "f2", { rx: 6 }) + SV.text(670, 48, "packet out", "lbl bd", { "text-anchor": "middle" });
    rows.forEach((r, i) => (o += SV.rect(180, 20 + i * 38, 400, 32, k === i + 1 ? "cell-warn" : k > i + 1 ? "cell-ok" : "cell", { rx: 6 }) + SV.text(194, 41 + i * 38, r, "lbl", { style: "font-size:13px" })));
    if (k >= 2) o += SV.text(30, 200, "routing table entry used:", "sm") + SV.text(30, 218, "172.16.0.0/16 → Router C", "lbl", { style: "font-family:var(--mono);font-size:12px" });
    if (k >= 4) o += SV.text(610, 130, "hop count 8 → 7", "lbl bd", { style: "font-family:var(--mono);font-size:13px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 235, label: "The function of a router", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "A packet arrives at a router.", s: { i: 0 } },
    { cap: "The router <b>reads the destination IP address</b> from the packet header.", s: { i: 1 } },
    { cap: "It looks the address up in its <b>routing table</b> (hops, netmask, gateway, status of routes).", s: { i: 2 } },
    { cap: "It decides the <b>next hop</b>: the best route at that moment.", s: { i: 3 } },
    { cap: "It <b>reduces the hop count by 1</b>. If it reaches 0 the packet is discarded.", s: { i: 4 } },
    { cap: "It sends the packet to the next router. Each router repeats this, hop by hop.", s: { i: 5 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 28, "Packets received:", "lbl bd");
    for (let i = 1; i <= 5; i++) { const lost = i === 3 && k < 3; o += SV.rect(30 + (i - 1) * 90, 44, 80, 40, lost ? "cell-no" : "f3", { rx: 6 }) + SV.text(70 + (i - 1) * 90, 70, lost ? "?" : "P" + i, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }); }
    if (k >= 1) o += SV.text(30, 120, "The receiver checks the sequence numbers: packet 3 is missing", "lbl bd t2", { style: "font-size:14px" });
    if (k >= 2) o += SV.text(30, 150, "It sends a re-send request for packet 3", "lbl", { style: "font-size:14px" });
    if (k >= 3) o += SV.text(30, 180, "Packet 3 arrives (by any route): the message is complete", "lbl bd t3", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 205, label: "Re-sending a missing packet", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "Five packets were sent. They are checked on arrival.", s: { i: 0 } },
    { cap: "Packet 3 did not arrive, or arrived damaged. The receiver notices a gap in the sequence numbers.", s: { i: 1 } },
    { cap: "It sends a <b>re-send request</b>. Only that packet needs to be sent again.", s: { i: 2 } },
    { cap: "The missing packet arrives and the message is reassembled complete.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  const run = () => {
    const msg = "HELLO WORLD!", size = 2, pk = []; for (let i = 0; i < msg.length; i += size) pk.push(msg.slice(i, i + size));
    const delays = [5, 2, 7, 3, 6, 1], route = ["A", "B", "C", "A", "B", "C"], lose = $("#pL").checked;
    const arr = pk.map((d, i) => ({ n: i + 1, d, t: delays[i % 6], r: route[i % 6] })).filter((p) => !(lose && p.n === 3)).sort((a, b) => a.t - b.t);
    let h = '<div class="tw"><table class="t mono"><tr><th>Arrival</th><th>Packet</th><th>Data</th><th>Route</th></tr>' + arr.map((p, i) => `<tr><td>${i + 1}</td><td>${p.n}</td><td>"${p.d}"</td><td>${p.r}</td></tr>`).join("") + "</table></div>";
    const ordered = arr.slice().sort((a, b) => a.n - b.n);
    h += '<div class="tw"><table class="t mono"><tr><th>Reassembled by sequence number</th></tr><tr><td>' + ordered.map((p) => p.d).join("") + (lose ? " …(packet 3 missing)" : "") + "</td></tr></table></div>";
    $("#pO").innerHTML = h;
    $("#pV").textContent = lose ? "Packet 3 is missing, so the receiver sends a re-send request. Only packet 3 is sent again, then the message is complete: HELLO WORLD!" : "The packets took three routes and arrived out of order, but the sequence numbers let the receiver reassemble HELLO WORLD!";
  };
  $("#pG").onclick = run; $("#pL").onchange = run; run();
})();

/* Lab 2 */
(function () {
  const addrs = [["172.16.4.9", "Router C"], ["10.2.3.4", "Router B"], ["192.168.1.20", "deliver locally"], ["8.8.8.8", "Router D (default route)"]]; let cur = 0, hop = 8;
  const table = [["10.0.0.0 / 8", "Router B"], ["172.16.0.0 / 16", "Router C"], ["192.168.1.0 / 24", "deliver locally"], ["default", "Router D (default route)"]];
  const paint = () => {
    $$("#rB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const a = addrs[cur], hit = table.findIndex((t) => t[1] === a[1]);
    $("#rO").innerHTML = '<p>Destination IP address in the header: <b class="mono">' + a[0] + '</b>, hop count ' + hop + '</p><div class="tw"><table class="t mono"><tr><th>Network</th><th>Next hop</th></tr>' + table.map((t, i) => `<tr style="${i === hit ? "background:var(--warn-soft);font-weight:700" : ""}"><td>${t[0]}</td><td>${t[1]}</td></tr>`).join("") + "</table></div><div class=\"verdict\">The router reads " + a[0] + ", finds the matching entry, reduces the hop count to " + (hop - 1) + " and sends the packet to: " + a[1] + ".</div>";
  };
  $("#rB").innerHTML = addrs.map((a) => `<button class="b">${a[0]}</button>`).join("");
  $$("#rB button").forEach((b, i) => (b.onclick = () => { cur = i; paint(); })); paint();
})();

btnTable("eB", "eO", [
  ["Path", "A dedicated circuit set up first", "No dedicated path; each packet finds its own", "Set up before or sent straight away"],
  ["Data", "A continuous stream, message intact", "Split into packets with headers", "Segmented or not"],
  ["Route", "All the data follows the same route", "Packets can follow different routes", "Same or different routes"],
  ["Order", "Arrives in order sent", "May arrive out of order: reassembled", "Reordering delay"],
  ["Bandwidth", "Whole bandwidth, not shared", "Shared with other traffic", "Wasted or shared"],
  ["Faults", "The transmission ends if the route fails", "Re-routed; individual packets re-sent", "Resilience"]
], ["Feature", "Circuit switching", "Packet switching", "Point to make"]);
''' + CLASSIFY("cl1", "Circuit switching or packet switching?", ["Circuit switching", "Packet switching"],
  [("A dedicated path is set up before sending", 0), ("Data is split into packets with headers", 1), ("All data follows the same route", 0), ("Packets may arrive out of order", 1), ("Bandwidth is shared between users", 1), ("The whole bandwidth is reserved", 0), ("A router reads the destination IP address", 1), ("Individual lost packets can be re-sent", 1)],
  "Dedicated and continuous: circuit. Packets, headers, routers: packet.") + CLASSIFY("cl2", "Benefit or drawback of packet switching?", ["Benefit", "Drawback"],
  [("Packets can be re-routed around a fault", 0), ("Packets have to be reassembled at the destination", 1), ("Bandwidth can be shared", 0), ("Needs a complex algorithm and lots of RAM", 1), ("A lost packet can be re-sent on its own", 0), ("Not suitable for real-time transmission", 1)],
  "Benefits: re-routing, sharing, resending one packet. Drawbacks: delay, complexity.") + ORDER(
  "Put the steps of packet switching in order.",
  ["The message is divided into packets", "Each packet is given a header with the IP addresses and a sequence number", "Each packet is sent independently by routers, possibly on different routes", "The packets arrive at the destination, possibly out of order", "The packets are reassembled in order and missing ones are re-sent"],
  "Divide, header, send independently, arrive, reassemble.") + MATCH([
  ["Packet", "A small chunk of a message with a header"], ["Header", "Holds the IP addresses and sequence number"], ["Router", "Reads the destination IP address and chooses the next hop"], ["Routing table", "Information the router uses to choose the next hop"], ["Hop count", "Reduced by 1 at each router so a packet cannot circulate forever"]]) + CALC([
  {"q": "A 6000-byte message is sent in packets of 500 bytes. How many packets?", "a": 12, "unit": "", "tol": 0.01, "hint": "6000 ÷ 500.", "sol": "<b>12</b>."},
  {"q": "A packet starts with a hop count of 10 and passes through 4 routers. What is the hop count after?", "a": 6, "unit": "", "tol": 0.01, "hint": "10 − 4.", "sol": "<b>6</b>."},
  {"q": "12 packets are sent and packets 5 and 9 are lost. How many arrive?", "a": 10, "unit": "", "tol": 0.01, "hint": "12 − 2.", "sol": "<b>10</b>."},
  {"q": "How many packets have to be re-sent in the example above?", "a": 2, "unit": "", "tol": 0.01, "hint": "Only the lost ones.", "sol": "<b>2</b>."},
  {"q": "A packet has a hop count of 3 and needs 5 hops to reach its destination. Does it arrive? Enter 1 for yes, 0 for no.", "a": 0, "unit": "", "tol": 0.01, "hint": "The count reaches 0 after 3 hops: the packet is discarded.", "sol": "<b>0</b>: it is discarded."}]) + MCQ([
  ("What does a router read to decide where to send a packet?", ["The payload", "The destination IP address in the header", "The MAC address of the sender", "The file name"], 1, "The header's destination IP address."),
  ("Which is a benefit of packet switching?", ["The data always arrives in order", "Packets can be re-routed around a fault", "A dedicated circuit is reserved", "No reassembly is needed"], 1, "Resilience."),
  ("Which is a drawback of packet switching?", ["The bandwidth cannot be shared", "Packets must be reordered and reassembled", "A circuit must be set up", "There is no alternative route"], 1, "Delay."),
  ("What is used to reassemble the packets?", ["The hop count", "The sequence number", "The MAC address", "The payload"], 1, "Sequence numbers."),
  ("Packets of one message...", ["must take the same route", "may take different routes", "are never re-sent", "always arrive in order"], 1, "Each is sent independently."),
  ("What happens to a packet whose hop count reaches 0?", ["It is delivered", "It is discarded", "It is copied", "It is encrypted"], 1, "It is discarded.")], "qz1") + CARDS([
  ("Packet switching", "Message split into packets sent independently, reassembled at the destination."), ("Header", "Source and destination IP addresses, sequence number."), ("Router", "Reads the destination IP, uses the routing table, sends the packet on its next hop."), ("Hop count", "Reduced at each router; at 0 the packet is discarded."),
  ("Benefits", "Re-routing, resending one packet, shared bandwidth, security."), ("Drawbacks", "Delay reordering, complex, RAM, not real time."), ("Versus circuit", "No dedicated path, packets, different routes, shared bandwidth."), ("Complete message", "Check on arrival, request re-send, re-route.")])

build("ac1422", "ac-14-2-2-packet-switching-routers", "Packet Switching and Routers", EYA("14.2.2"),
  "How a message is divided into packets and routed independently, what a router does, benefits and drawbacks, and packet against circuit switching; animations, a packet network simulator and the real 9618 questions from 2021 to 2025.",
  dict(sub=CBK("Chapter 14 · Communication and internet technologies, section 14.2 Circuit switching, packet switching"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
