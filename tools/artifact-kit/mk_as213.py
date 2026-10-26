"""AS CS syllabus 2.1.3: LAN hardware, routers, Ethernet and CSMA/CD. Run: python3 tools/artifact-kit/mk_as213.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A LAN is built from a few kinds of hardware: a <b>network interface card (NIC)</b> or <b>wireless NIC (WNIC)</b> in each device, <b>cables</b>, a <b>switch</b> that forwards data only to its destination, a <b>server</b>, a <b>wireless access point (WAP)</b> for wireless devices, a <b>bridge</b> to join two LANs and a <b>repeater</b> to restore a weakening signal. A <b>router</b> joins networks together: it receives packets, reads the destination IP address, uses its routing table to choose the best route and forwards the packet. <b>Ethernet</b> is the protocol used for wired LANs, and it uses <b>CSMA/CD</b> to cope with <b>collisions</b>: a device listens, sends only when the line is idle, and if a collision happens it stops, sends a jamming signal and retries after a random wait. A router and a switch do different jobs: a switch connects devices inside a LAN by MAC address; a router connects different networks by IP address.</p></div>

  <h2>1 · LAN hardware</h2>
  <div class="tw"><table class="t">
    <tr><th>Device</th><th>Purpose</th></tr>
    <tr><td><b>Network interface card (NIC)</b></td><td>Lets a device connect to a wired network. It has a <b>MAC address</b> that identifies the device on the network.</td></tr>
    <tr><td><b>Wireless NIC (WNIC)</b></td><td>Lets a device connect to a wireless network: it provides the interface and acts as an antenna, receiving radio waves and converting them to digital data (and the reverse), and checking that incoming transmissions have the right address.</td></tr>
    <tr><td><b>Switch</b></td><td>Connects devices in a LAN. It stores the <b>MAC addresses</b> of the devices connected to it, receives packets and <b>forwards them only to the intended recipient</b>. (A hub, in contrast, sends data to every device.)</td></tr>
    <tr><td><b>Server</b></td><td>A computer that provides services to the other computers: files, printing, logins, security.</td></tr>
    <tr><td><b>Wireless access point (WAP)</b></td><td>Lets wireless devices connect to a wired network using radio signals (Wi-Fi). It provides radio communication between a central device and the nodes.</td></tr>
    <tr><td><b>Cables</b></td><td>Copper or fibre-optic links between devices (see 2.1.2).</td></tr>
    <tr><td><b>Bridge</b></td><td>Connects two LANs or segments that use the <b>same protocol</b> and transmits data between them.</td></tr>
    <tr><td><b>Repeater</b></td><td>Restores a digital signal so it can be transmitted over greater distances.</td></tr>
  </table></div>

  <h2>2 · The router</h2>
  <p>A <b>router</b> connects a LAN to other networks such as the internet. Its functions:</p>
  <ul>
    <li><b>Receives packets</b> from devices on the LAN or from the internet.</li>
    <li><b>Analyses the destination IP address</b> of each packet.</li>
    <li>Looks the address up in its <b>routing table</b> and <b>forwards the packet</b> towards its destination, finding the most efficient route; it maintains and updates the routing table.</li>
    <li>Allocates <b>private IP addresses</b> to devices on the LAN, and may share one public address between them (NAT).</li>
    <li>Implements a <b>firewall</b>, and may change the format of a packet for the next network.</li>
    <li>A home router usually also contains a switch and a WAP, and stores a table of the MAC and IP addresses of the devices attached to it.</li>
  </ul>
  <p>A router does <b>not</b> direct each packet to all devices (that is a hub) and does not look up the IP address of a URL (that is a DNS server).</p>

  <h2>3 · Ethernet and CSMA/CD</h2>
  <p><b>Ethernet</b> is a protocol (suite) for data transmission over standard wired network connections. Data is sent in <b>frames</b>; each frame has a source and destination (MAC or IP) address and error-checking data, so damaged frames can be resent. When devices share one transmission medium, two may transmit at the same moment and the signals <b>collide</b>. Ethernet manages this with <b>CSMA/CD</b>, Carrier Sense Multiple Access with Collision Detection:</p>
  <ol>
    <li><b>Carrier sense</b>: a device that wants to transmit <b>listens to the channel</b>.</li>
    <li>It sends data <b>only when the line is idle</b>, no other data being transmitted.</li>
    <li><b>Multiple access</b> means more than one computer is connected to the same medium, so two can start at once.</li>
    <li><b>Collision detection</b>: if a collision is detected, the devices <b>stop (abort) transmission</b> and send a <b>jamming signal</b>.</li>
    <li>Each device waits a <b>random time</b> before it tries to resend. If further collisions occur, the random wait time is <b>increased</b>.</li>
  </ol>
  <p>Drawbacks of CSMA/CD: waiting times can grow without limit and constant jamming could stop anything being sent; certain nodes cannot be prioritised; it is only suitable for short-distance networks and does not scale well, as more nodes mean much longer waits.</p>

  <h2>4 · Common ways to lose marks</h2>
  <ul>
    <li>Confusing a hub and a switch. A switch sends a packet only to the intended device.</li>
    <li>Describing CSMA/CD without the random wait. The order is listen, send if idle, detect collision, jam, wait a random time, resend.</li>
    <li>Saying a router "connects computers". Say it connects networks and routes packets using IP addresses and a routing table.</li>
    <li>Giving the NIC's purpose as "to connect to the internet". It provides the interface to the network and identifies the device with a MAC address.</li>
    <li>Mixing up a bridge (joins two LANs with the same protocol) and a repeater (restores the signal).</li>
  </ul>
'''

watch = '''
  <h2>1 · CSMA/CD: a collision and the retry</h2>
  <p>Press Play.</p>
  <div id="stA"></div>
  <h2>2 · A router forwards a packet</h2>
  <div id="stB"></div>
  <h2>3 · A switch forwards only to the receiver</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Collisions and random waits</h2>
  <p>Two devices try to send. After each collision each waits a random number of time slots. Press Send until a frame gets through.</p>
  <div class="card"><div class="btnrow" id="cB"></div><div id="cT"></div><div class="verdict" id="cV"></div></div>
  <h2>Lab 2 · Which device?</h2>
  <div class="card"><div id="dB" class="btnrow"></div><div id="dO"></div></div>
  <h2>Lab 3 · Hub or switch?</h2>
  <p>Choose the sender and the receiver. See which devices get the frame.</p>
  <div class="card"><div class="btnrow" id="hB"></div><div class="btnrow" id="hS"></div><div id="hG"></div><div class="verdict" id="hV"></div></div>
'''

_pr, _prjs = PR(["Which device?", "Router or switch?", "Match the device to its purpose", "Put the CSMA/CD steps in order", "Working out", "Multiple choice"],
  ("Which device does the description match?", ["NIC / WNIC", "Switch", "Bridge", "Repeater"], [("Provides a MAC address to identify the device on the network", 0), ("Forwards packets only to the intended recipient", 1), ("Restores the signal for greater distances", 3), ("Joins two LANs that use the same protocol", 2), ("Acts as an antenna for a laptop", 0), ("Stores the MAC addresses of connected devices", 1)], "NIC identifies, switch forwards, bridge joins, repeater restores."),
  ("Is it done by a router or by a switch?", ["Router", "Switch"], [("Joins the LAN to the internet", 0), ("Connects devices inside a LAN by MAC address", 1), ("Reads the destination IP address and uses a routing table", 0), ("Allocates private IP addresses", 0), ("Forwards a frame only to the receiving device on the LAN", 1), ("Finds the most efficient route to the destination", 0)], "Router: between networks, IP. Switch: inside a LAN, MAC."),
  [["Router", "Forwards packets between networks using IP addresses"], ["Switch", "Sends packets only to the intended device"], ["WAP", "Lets wireless devices join a wired network"], ["CSMA/CD", "Listen, send when idle, detect collisions"], ["Jamming signal", "Sent when a collision is detected"]],
  ("Put the CSMA/CD steps in order.", ["The device listens to the channel", "It sends data when the line is idle", "A collision is detected", "A jamming signal is sent and transmission aborted", "Each device waits a random time and resends"], "Listen, send, collision, jam, random wait."),
  [{"q": "Two devices collide. Device A waits 3 slots and device B waits 5 slots. How many slots after the collision does A resend?", "a": 3, "unit": "", "tol": 0.01, "hint": "A's own wait.", "sol": "<b>3</b>."}, {"q": "In the same case, how many slots later than A does B resend?", "a": 2, "unit": "", "tol": 0.01, "hint": "5 − 3.", "sol": "<b>2</b>."}, {"q": "A hub sends a frame to every connected device. A 6-port hub with one sender: how many devices receive it?", "a": 5, "unit": "", "tol": 0.01, "hint": "All the others.", "sol": "<b>5</b>."}, {"q": "A switch with one sender and one intended receiver: how many devices receive the frame?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the receiver.", "sol": "<b>1</b>."}, {"q": "How many items make up the Ethernet frame description in the Learn tab (source, destination, error-check)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Source address, destination address, error checking.", "sol": "<b>3</b>."}],
  [("A switch forwards packets:", ["To all devices", "Only to the intended recipient", "To the internet", "Nowhere"], 1, "Only to the recipient."), ("A router uses:", ["A routing table", "A keyboard", "A monitor", "A pen"], 0, "A routing table."), ("When a collision is detected, devices:", ["Send faster", "Abort and wait a random time", "Switch off", "Change topology"], 1, "Abort and wait."), ("A repeater:", ["Restores the signal", "Allocates IP addresses", "Stores files", "Prints"], 0, "Restores the signal."), ("A bridge joins:", ["Two LANs with the same protocol", "A PC and a printer", "Two monitors", "A network and a battery"], 0, "Two LANs, same protocol."), ("The NIC's MAC address:", ["Identifies the device on the network", "Is the internet speed", "Is the monitor size", "Is a password"], 0, "Identifies the device.")],
  [("NIC", "Interface to the network; has a MAC address."), ("Switch", "Forwards only to the recipient; stores MAC addresses."), ("Router", "Connects networks; routing table; IP addresses."), ("WAP", "Wireless devices to a wired network."), ("Bridge", "Joins two LANs, same protocol."), ("Repeater", "Restores the signal."), ("Ethernet", "Wired LAN protocol using frames and CSMA/CD."), ("CSMA/CD", "Listen, send if idle, detect, jam, random wait.")])

real = RWNOTE + (
rw("The box from your internet provider", "It is a router, a switch and a wireless access point in one: it connects your home network to the internet, connects wired devices and gives Wi-Fi to the rest.", "a router connects networks; the WAP gives Wi-Fi.") +
rw("The network socket in a classroom", "Behind it, cables run to a switch in a cabinet. The switch sends each packet only to the computer it is meant for.", "a switch forwards to the intended device.") +
rw("A Wi-Fi extender", "It repeats the signal so it reaches rooms that are too far from the router. That is a repeater.", "a repeater restores the signal over greater distance.") +
rw("Talking on a walkie-talkie", "If two people talk at once you hear nothing. Both stop, and each waits a random moment before trying again. That is how Ethernet handles collisions.", "CSMA/CD: random wait after a collision.") +
rw("The MAC address on a laptop's sticker", "Every network card has its own MAC address, so the switch knows which device is which.", "the NIC identifies the device on the network.")
)

where = [
  ("M/J 2021", "11, 13", "4(c)(i)", "2", "Tick the tasks performed by a router"),
  ("O/N 2021", "11, 13", "8(b), (c)", "2 + 4", "Two devices to connect 30 computers; the functions of a wireless NIC"),
  ("O/N 2021", "12", "3(b)(ii)", "3", "Three functions of a home router"),
  ("M/J 2022", "12", "9(a), (c)", "4 + 4", "Complete a table of network devices; describe CSMA/CD"),
  ("M/J 2023", "12", "1(d)", "3", "What is meant by Ethernet"),
  ("O/N 2023", "11", "2(a), (b)", "3 + 3", "The function of a router; the purpose of a switch, a WAP and a bridge"),
  ("O/N 2023", "12", "7(c)", "3", "Three tasks performed to deal with collisions using CSMA/CD"),
  ("M/J 2024", "13", "5(b), (c)", "2 + 2 + 2", "How packets travel in a star; how a collision is managed; two drawbacks of CSMA/CD"),
  ("M/J 2025", "12", "6(e)", "3", "The role of a switch in a network"),
  ("O/N 2025", "12", "5(d)", "3", "How collisions are detected and managed on an Ethernet bus network")]

past = '''  <p class="note">LAN hardware, the router and CSMA/CD are among the most repeated Paper 1 topics. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "11/13", "Q4(c)(i)"), "2 marks", "Tick",
  "Melinda connects her laptop to the internet through her router. Tick one box in each row to identify whether the task is performed by the router or not: (1) receives packets from devices; (2) finds the IP address of a Uniform Resource Locator (URL); (3) directs each packet to all devices attached to it; (4) stores the IP and/or MAC address of all devices attached to it.",
  "One mark for the first two ticks and one mark for the last two.",
  "<p>" + mks(["(1) Performed by the router; (2) not performed by the router (a DNS server does this)"]) + " " + mks(["(3) not performed by the router (a hub does this); (4) performed by the router"], "a") + "</p>", "Ticking (3) as the router's job. A router sends each packet towards its destination, not to all devices.") + peq(SRC("w21", "11/13", "Q8(b)(c)"), "2 + 4 marks", "Identify / Describe",
  "One classroom has 30 computers, each with a network interface card (NIC). (b) Identify two possible devices that can be used to physically connect the 30 computers to the rest of the network. (c) The school has several laptops, each with a Wireless Network Interface Card (WNIC). Describe the functions of a Wireless Network Interface Card.",
  "(b) Router, switch or hub. (c) Interface to the wireless network, antenna, analogue to digital, checks addresses.",
  "<p><b>(b)</b> Any two: " + mks(["Router", "Switch", "Hub"]) + "</p><p><b>(c)</b> Any four: " + mks(["Provides the interface to the wireless network, as an antenna", "Receives analogue radio waves and converts them to digital or binary", "Checks incoming transmissions for the correct MAC or IP address", "and ignores transmissions not intended for it", "Encrypts or encodes the data, and decrypts or decodes it", "Takes digital input, converts it to analogue waves and sends them via the antenna"], "a") + "</p>", None) + peq(SRC("w21", "12", "Q3(b)(ii)"), "3 marks", "Identify",
  "The home router has a wireless access point (WAP) to allow the devices to connect wirelessly. Identify three functions of the router in Andy's network.",
  "Receive, forward, find the destination, allocate addresses, routing table.",
  "<p>Any three: " + mks(["To receive packets from devices or the internet", "To forward or route packets to the destination", "To find the destination of the packet", "To assign or allocate private IP addresses to devices on the LAN", "To store, update or maintain a routing table", "To find the most efficient path to the destination", "To maintain a table of MAC and IP addresses"]) + "</p>", None) + peq(SRC("w23", "11", "Q2(a)(b)"), "3 + 3 marks", "Describe",
  "(a) The school LAN connects to the internet using a router. Describe the function of a router in a network. (b) Complete the table by writing the purpose of each of these other hardware devices used to support the LAN: switch; Wireless Access Point (WAP); bridge.",
  "(b) one purpose for each of three devices.",
  "<p><b>(a)</b> Any three: " + mks(["Receives packets from the internet or external network", "Implements a firewall", "Analyses the destination IP address of each packet", "Forwards the packet towards its destination, using the routing table", "Maintains and updates the routing table", "Allocates private IP addresses", "Finds the most efficient route to the destination", "Changes the packet format for the next network (NAT lets many devices share one public address)"]) + "</p><p><b>(b)</b> " + mks(["Switch: to connect individual devices to each other, receive transmissions and forward them to their destination"]) + " " + mks(["WAP: to allow wireless-enabled devices to connect to a wired network using radio signals"], "a") + " " + mks(["Bridge: to connect two LANs or segments with the same protocol and transmit data between them"], "n") + "</p>", None) + peq(SRC("s22", "12", "Q9(a)(c)"), "4 + 4 marks", "Complete / Describe",
  "(a) Complete the table of four network devices and descriptions: a device that receives and sends data between two networks operating on the same protocol; Wireless Network Interface Card (WNIC); a device that restores the digital signal so it can be transmitted over greater distances; Wireless Access Point (WAP). (c) Ethernet uses Carrier Sense Multiple Access/Collision Detection (CSMA/CD). Describe CSMA/CD.",
  "(a) Router, ?, repeater, ?",
  "<p><b>(a)</b> " + mks(["Router: receives and sends data between two networks operating on the same protocol", "WNIC: hardware that allows a device to connect to a wireless network, or provides a MAC address to identify the device on the wireless network", "Repeater: restores the digital signal so it can be transmitted over greater distances", "WAP: hardware that provides radio communication from the central device to the nodes on the network and vice versa"]) + "</p><p><b>(c)</b> Any four: " + mks(["A workstation wishing to transmit listens to the communication channel", "Data is only sent when the channel is free", "Because more than one computer is connected to the same medium, two workstations can start transmitting at the same time, causing a collision", "If a collision happens, the workstations send a jamming signal or abort transmission", "and each waits a random amount of time before attempting to resend"], "a") + "</p>", "In (a), writing 'bridge' for the first device. A bridge joins LANs with the same protocol; the description 'two networks' is a router.") + peq(SRC("s23", "12", "Q1(d)"), "3 marks", "Describe",
  "Computers can be connected using Ethernet. Describe what is meant by Ethernet.",
  "A protocol; wired; CSMA/CD; frames with addresses and error checking.",
  "<p>Any three: " + mks(["A protocol (suite)", "for data transmission over standard or universal wired network connections", "Uses Carrier Sense Multiple Access / Collision Detection (CSMA/CD)", "Data is transmitted in frames", "each frame has a source and destination (IP or MAC) address", "and error-checking data (so damaged frames can be resent)"]) + "</p>", None) + peq(SRC("w23", "12", "Q7(c)"), "3 marks", "State",
  "State three tasks performed by devices to deal with collisions when using the Carrier Sense Multiple Access / Collision Detection (CSMA/CD) protocol in a network.",
  "Monitor, wait for quiet, jam, random wait, increase it.",
  "<p>Any three: " + mks(["To monitor the communications channel", "To send data only when no data is being transmitted (the line is quiet or idle)", "To detect a collision and then stop transmission, or transmit a jamming signal", "To calculate a random wait or back-off time", "then retransmit the data after that random wait time", "Increase the random time if there are multiple collisions"]) + "</p>", None) + peq(SRC("s24", "13", "Q5(b)(c)"), "2 + 2 + 2 marks", "Explain / Describe / Identify",
  "(b) Explain how packets are transmitted between two devices in a star topology. (c)(i) A collision is detected on part of the network that uses Ethernet. Describe how the collision is managed using CSMA/CD. (ii) Identify two drawbacks of using CSMA/CD.",
  "(b) to the switch, address checked, forwarded directly.",
  "<p><b>(b)</b> " + mks(["The sending computer transmits packets directly to the switch or central device", "The switch checks the destination address of the packet and forwards it directly to that device"]) + "</p><p><b>(c)(i)</b> Any two: " + mks(["A jamming signal is transmitted by the sending device", "Transmission is aborted", "The sending device waits a random time before trying to send again", "If further collisions occur the wait time is increased"], "a") + "</p><p><b>(ii)</b> Any two: " + mks(["The random time is increased each time, so waiting could be infinite", "The jamming signal may be constant, so nothing ever sends", "Certain nodes cannot be prioritised", "High power consumption", "Only suitable for a short-distance network", "Not scalable: more nodes mean exponentially longer waits"], "n") + "</p>", None) + peq(SRC("s25", "12", "Q6(e)"), "3 marks", "Describe",
  "Describe the role of a switch in a network.",
  "Stores MAC addresses, receives packets, forwards to the intended recipient.",
  "<p>Any three: " + mks(["To store the MAC addresses of devices connected to it", "To receive packets from devices", "To forward packets directly to the intended recipient", "To provide a central point of connection for the network", "To enable connected devices to communicate"]) + "</p>", None) + peq(SRC("w25", "12", "Q5(d)"), "3 marks", "Describe",
  "Another type of network is a bus network. Ethernet is used to transmit and receive data between the devices on the bus network. Describe how collisions are detected and managed on this network.",
  "CSMA/CD with its steps.",
  "<p>Any three: " + mks(["The use of CSMA/CD", "The workstations listen to the communication channel", "and send data only when no data is being transmitted (the line is idle)", "If a collision is detected, transmission is aborted", "and a jamming signal is sent", "The workstation calculates a random wait time before trying to retransmit", "The random time is increased if there are multiple collisions"]) + "</p>", None)

review = req("3 marks", "Explain", "Explain the difference between a hub and a switch.", "Where does the data go?", "<p>" + mks(["A hub sends data to every connected device", "A switch stores MAC addresses and forwards the data only to the intended recipient", "So a switch reduces collisions and wasted traffic"]) + "</p>", None) + req("2 marks", "State", "State two tasks performed by a router.", "IP addresses and routes.", "<p>" + mks(["Analyses the destination IP address of each packet", "Forwards it towards its destination using a routing table"]) + "</p>", None) + req("3 marks", "Describe", "Describe what a device does when it wants to transmit on an Ethernet bus.", "Listen first.", "<p>" + mks(["It listens to the channel", "It sends only when the line is idle", "If a collision is detected it aborts, sends a jamming signal and waits a random time before trying again"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between a repeater and a bridge.", "Signal or networks.", "<p>" + mks(["A repeater restores the signal so it can travel further", "A bridge connects two LANs or segments that use the same protocol"]) + "</p>", None) + req("2 marks", "Explain", "Explain why the wait time after a collision is random.", "What if both waited the same?", "<p>" + mks(["If both devices waited the same time they would collide again", "Random waits make it likely one device sends first"]) + "</p>", None)

tips = tips_html([
  ("Switch: only to the recipient.", "Hub: to everyone."),
  ("Router: IP addresses and routing table.", "It connects networks."),
  ("CSMA/CD order.", "Listen, send if idle, collision, jam, random wait, resend."),
  ("NIC: MAC address.", "WNIC: also an antenna."),
  ("Bridge v repeater.", "Bridge joins LANs; repeater restores the signal."),
  ("Ethernet: frames.", "With addresses and error-checking data."),
], [("a switch", "Forwards packets only to the intended recipient."), ("a router", "Connects networks and forwards packets using IP addresses."), ("a collision", "Two devices transmitting at the same time on one medium."), ("a MAC address", "The address that identifies a network card.")],
  [("Identify / State", "Give the points."), ("Describe", "Say what it does, in steps."), ("Explain", "Give reasons."), ("Complete", "Fill the table.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.path("M30,100 H570", "ax", { style: "stroke-width:5" }); [[100, "A"], [300, "B"], [500, "C"]].forEach(([x, n]) => { o += SV.rect(x - 28, 30, 56, 36, k >= 1 && (n === "A" || n === "C") ? "cell-warn" : "cell", { rx: 6 }) + SV.text(x, 53, n, "lbl bd", { "text-anchor": "middle" }) + SV.path("M" + x + ",66 V100", "ax"); });
    if (k === 0) o += SV.text(30, 150, "A and C both want to send to B. Both listen to the line.", "lbl bd", { style: "font-size:13px" }); if (k === 1) o += SV.text(30, 150, "The line is idle: both start sending at the same moment.", "lbl bd", { style: "font-size:13px" });
    if (k >= 2) o += SV.circle(300, 100, 14, "dot2") + SV.text(300, 135, "collision!", "lbl bd t2", { "text-anchor": "middle" }); if (k === 3) o += SV.text(30, 165, "Both stop (abort) and send a jamming signal.", "lbl bd", { style: "font-size:13px" }); if (k >= 4) o += SV.text(30, 165, "A waits 2 slots, C waits 5 slots (random).", "lbl bd t3", { style: "font-size:13px" }); if (k >= 5) o += SV.circle(200, 100, 8, "dot3") + SV.text(30, 190, "A resends first and the frame gets through. C then sees the line busy and waits.", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 600, h: 205, label: "CSMA/CD", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "<b>Carrier sense</b>: both A and C listen to the shared line before sending.", s: { i: 0 } }, { cap: "The line is idle, so both begin to send at the same time.", s: { i: 1 } }, { cap: "The signals <b>collide</b>.", s: { i: 2 } }, { cap: "<b>Collision detected</b>: both devices stop and send a jamming signal.", s: { i: 3 } }, { cap: "Each waits a <b>random time</b> before trying again. Random times make another collision unlikely.", s: { i: 4 } }, { cap: "The device with the shorter wait sends first and succeeds. If there were more collisions the random wait would be increased.", s: { i: 5 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 50, 120, 60, "cell", { rx: 8 }) + SV.text(80, 85, "LAN device", "lbl bd", { "text-anchor": "middle" }) + SV.rect(240, 40, 120, 80, "f3", { rx: 10 }) + SV.text(300, 70, "Router", "lbl bd", { "text-anchor": "middle" }) + SV.text(300, 92, "routing table", "sm", { "text-anchor": "middle" }) + SV.rect(460, 50, 120, 60, "cell", { rx: 8 }) + SV.text(520, 85, "Internet", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.path("M140,80 H240", "ax", { style: "stroke:var(--accent);stroke-width:3" }) + SV.text(190, 70, "packet", "sm", { "text-anchor": "middle" }); if (k >= 2) o += SV.text(300, 150, "destination IP 93.184.x.x read", "lbl bd", { "text-anchor": "middle", style: "font-size:12.5px" }); if (k >= 3) o += SV.text(300, 170, "looked up in the routing table: best route found", "lbl bd t3", { "text-anchor": "middle", style: "font-size:12.5px" }); if (k >= 4) o += SV.path("M360,80 H460", "ax", { style: "stroke:var(--good);stroke-width:3" }) + SV.text(410, 70, "forwarded", "sm", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 185, label: "Router", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "A device on the LAN wants to reach something on the internet.", s: { i: 0 } }, { cap: "The router <b>receives the packet</b> from the device.", s: { i: 1 } }, { cap: "It <b>analyses the destination IP address</b>.", s: { i: 2 } }, { cap: "It looks the address up in its <b>routing table</b> and chooses the most efficient route.", s: { i: 3 } }, { cap: "It <b>forwards</b> the packet towards its destination.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(250, 70, 100, 50, "f3", { rx: 10 }) + SV.text(300, 100, "Switch", "lbl bd", { "text-anchor": "middle" });
    [[80, 40, "A"], [80, 150, "B"], [520, 40, "C"], [520, 150, "D"]].forEach(([x, y, n]) => { const to = k >= 3 && n === "D", from = k >= 1 && n === "A"; o += SV.path("M" + x + "," + y + " L300,95", "ax", { style: "stroke:" + (to || from ? "var(--good)" : "var(--muted)") + ";stroke-width:" + (to || from ? 4 : 2) }); o += SV.rect(x - 26, y - 16, 52, 32, to ? "cell-ok" : from ? "cell-warn" : "cell", { rx: 6 }) + SV.text(x, y + 5, n, "lbl bd", { "text-anchor": "middle" }); });
    if (k >= 2) o += SV.text(300, 150, "MAC table: D is on port 4", "lbl bd", { "text-anchor": "middle", style: "font-size:12.5px" }); if (k >= 3) o += SV.text(300, 175, "B and C do not receive the frame", "lbl bd t3", { "text-anchor": "middle", style: "font-size:12.5px" }); return o; };
  Lib.stepper($("#stC"), { w: 600, h: 190, label: "Switch", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "A wants to send a frame to D. All devices connect to the switch.", s: { i: 0 } }, { cap: "A sends the frame to the switch.", s: { i: 1 } }, { cap: "The switch checks the <b>destination MAC address</b> against its table.", s: { i: 2 } }, { cap: "It forwards the frame <b>only to D</b>. A hub would have sent it to everyone.", s: { i: 3 } }] });
})();

(function () {
  let st = { a: 0, b: 0 }, tries = 0, log = []; const b = $("#cB"); const rnd = () => Math.floor(Math.random() * 4);
  const paint = () => { $("#cT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Attempt</th><th>A waits</th><th>C waits</th><th>Result</th></tr>' + log.map((r, i) => `<tr><td>${i + 1}</td><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join("") + "</table></div>"; $("#cV").innerHTML = log.length ? (log[log.length - 1][2].startsWith("sent") ? "A frame got through after <b>" + log.length + "</b> attempt" + (log.length > 1 ? "s" : "") + ". The random waits are what avoided a repeat collision." : "Collision again: the wait range grows after each collision.") : "Both devices send at once and collide. Press Retry to give each a random wait."; };
  const step = () => { const range = Math.min(8, 2 + log.length * 2), a = Math.floor(Math.random() * range), c = Math.floor(Math.random() * range); log.push([a + " slots", c + " slots", a === c ? "collision again" : "sent by " + (a < c ? "A" : "C") + " first"]); if (log.length > 8) log.shift(); paint(); };
  [["Retry", step], ["Start again", () => { log = []; paint(); }]].forEach(([t, f]) => { const x = document.createElement("button"); x.textContent = t; x.onclick = f; b.appendChild(x); }); paint();
})();
btnTable("dB", "dO", [
  ["Gives a laptop a wireless connection", "WNIC", "Interface and antenna to the wireless network"],
  ["Connects the LAN to the internet", "Router", "Routes packets between networks by IP address"],
  ["Connects 30 classroom computers", "Switch", "Forwards frames only to the intended computer"],
  ["Lets phones join the wired LAN by Wi-Fi", "WAP", "Radio communication to the wired network"],
  ["Joins two LANs that use the same protocol", "Bridge", "Transmits data between the networks"],
  ["Strengthens a signal on a long cable", "Repeater", "Restores the digital signal"]
], ["Task", "Device", "Purpose"]);
(function () {
  let mode = "switch", from = "A", to = "D"; const b = $("#hB"), s = $("#hS"), g = $("#hG"); const nodes = { A: [60, 40], B: [60, 150], C: [540, 40], D: [540, 150] };
  const paint = () => { let o = '<svg viewBox="0 0 600 190" style="width:600px;max-width:100%;display:block">' + SV.rect(250, 70, 100, 50, "f3", { rx: 10 }) + SV.text(300, 100, mode === "switch" ? "Switch" : "Hub", "lbl bd", { "text-anchor": "middle" }); const got = from === to ? [] : mode === "hub" ? Object.keys(nodes).filter((n) => n !== from) : [to];
    Object.entries(nodes).forEach(([n, [x, y]]) => { const rx = got.includes(n); o += SV.path("M" + x + "," + y + " L300,95", "ax", { style: "stroke:" + (rx || n === from ? "var(--good)" : "var(--muted)") + ";stroke-width:" + (rx || n === from ? 4 : 2) }) + SV.rect(x - 26, y - 16, 52, 32, n === from ? "cell-warn" : rx ? "cell-ok" : "cell", { rx: 6 }) + SV.text(x, y + 5, n, "lbl bd", { "text-anchor": "middle" }); });
    g.innerHTML = o + "</svg>"; $("#hV").innerHTML = from === to ? "Choose different devices." : `${mode === "hub" ? "A hub" : "A switch"} sends the frame from ${from} to <b>${got.join(", ")}</b>. ` + (mode === "hub" ? "Every device receives it, so more traffic and more collisions." : "Only the intended device receives it.");
    b.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === mode ? "on" : "")); s.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === from + to ? "on" : "")); };
  [["switch", "Switch"], ["hub", "Hub"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { mode = k; paint(); }; b.appendChild(x); });
  [["A", "D"], ["B", "C"], ["C", "A"]].forEach(([f, t]) => { const x = document.createElement("button"); x.textContent = f + " to " + t; x.dataset.k = f + t; x.onclick = () => { from = f; to = t; paint(); }; s.appendChild(x); }); paint();
})();
''' + _prjs

finish("as-2-1-3-lan-hardware-router-ethernet", "as213", "LAN Hardware, Routers and Ethernet",
  "NICs, switches, WAPs, bridges, repeaters, the router and its functions, and Ethernet with CSMA/CD collision handling; animations, labs and the real Paper 1 questions from 2021 to 2025.",
  "2.1.3", "2 · Communication", "section 2.1 Networks including the internet", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on LAN hardware, routers and CSMA/CD (Paper 1), 2021 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
