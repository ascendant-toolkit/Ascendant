"""A Level CS syllabus 14.1.1: why protocols are needed, the protocol stack and the TCP/IP layers. Run: python3 tools/artifact-kit/mk_ac1411.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>protocol</b> is a set of agreed rules for communication between computers: it sets the format of the data, the order of messages and what to do when something goes wrong, so that devices from different makers can talk to each other. The <b>TCP/IP protocol suite</b> is built as a <b>stack of four layers</b>, <b>Application, Transport, Internet and Link</b>, and each layer has its own job and only deals with the layer directly above and below it. When a message is sent it passes <b>down</b> the stack on the sending host, with each layer adding information to a <b>header</b>, across the network, and <b>up</b> the stack on the receiving host, where each layer removes its header. The Application layer is where the user and their programs interact, and the Link layer is the one that actually sends the data over the physical connection. The next page covers the protocols that live in the Application layer.</p></div>

  <h2>1 · Why a protocol is essential</h2>
  <ul>
    <li>A protocol is a <b>standard set of rules</b> for communication: how data is formatted, addressed, sent, acknowledged and checked.</li>
    <li>It lets devices from <b>different manufacturers and platforms</b> communicate, because they follow the same rules.</li>
    <li>It makes communication <b>independent of the software and hardware</b> in use.</li>
    <li>Without it, two devices using different rules <b>could not communicate properly</b>: the data would not be understood.</li>
  </ul>

  <h2>2 · The stack idea</h2>
  <p>A protocol suite can be viewed as a <b>stack of layers</b>. Splitting the job into layers means each layer can be designed, improved and replaced on its own.</p>
  <ul>
    <li>Each layer has its <b>own functionality</b>.</li>
    <li>A layer can only accept input from the <b>next higher</b> or the <b>next lower</b> layer: the <b>adjacent</b> layers. The <b>interface</b> between adjacent layers is the only interaction between layers.</li>
    <li>The interactions are carried out by <b>installed software</b>.</li>
    <li><b>User interaction</b> takes place at the top (Application) layer. <b>Direct access to the hardware</b> takes place at the bottom (Link) layer.</li>
    <li>Data is <b>added to the header</b> as packets and frames pass down through the layers, and removed as they pass up.</li>
  </ul>

  <h2>3 · The four layers of TCP/IP</h2>
  <div class="tw"><table class="t">
    <tr><th>Layer</th><th>Purpose and function</th><th>Examples</th></tr>
    <tr><td><b>Application</b> (top)</td><td>Provides services and an <b>interface to the user</b>: the programs that exchange data (web browser, email client, file transfer). Defines the protocols applications use to exchange data</td><td>HTTP(S), FTP, SMTP, POP3, IMAP, BitTorrent</td></tr>
    <tr><td><b>Transport</b></td><td>Delivery from the <b>source host to the destination host</b> (end to end). Breaks data into <b>packets / segments</b>, adds a <b>sequence number</b> to the header, controls the <b>flow</b>, detects errors and requests <b>re-sending</b> of lost packets, and reassembles at the destination. Uses a port number</td><td>TCP, UDP</td></tr>
    <tr><td><b>Internet</b></td><td>Identifies the intended <b>network and host</b>. Adds a header with the <b>source and destination IP addresses</b>, forms datagrams, and <b>routes</b> each packet independently by the best route</td><td>IP</td></tr>
    <tr><td><b>Link</b> (bottom)</td><td>Transports data within the local network segment, <b>formats datagrams into frames</b>, maps <b>IP addresses to MAC (physical) addresses</b>, ensures the correct network protocols are followed, and sends and receives frames over the physical medium. Prepares the next hop</td><td>Ethernet, Wi-Fi</td></tr>
  </table></div>
  <div class="tip"><b class="h">Order to learn</b>From the user down: <b>A</b>pplication, <b>T</b>ransport, <b>I</b>nternet, <b>L</b>ink: "All Tests Include Logic". The Link layer is also called the Network Access or Data Link layer in some books; the exam uses Link.</div>

  <h2>4 · A message through the stack</h2>
  <ol>
    <li><b>Application layer (sender):</b> the user's program, such as a browser, creates the message using a protocol like HTTP.</li>
    <li><b>Transport layer:</b> breaks the message into packets, numbers them and adds a header (sequence number, port).</li>
    <li><b>Internet layer:</b> adds the source and destination IP addresses.</li>
    <li><b>Link layer:</b> puts the packet in a frame with MAC addresses and sends it onto the network.</li>
    <li>Routers pass it on. At the <b>receiver</b> the frame goes <b>up</b> the stack: the Link layer receives it, the Internet layer checks the address, the Transport layer puts the packets in order and checks them, and the Application layer gives the message to the program.</li>
  </ol>
  <div class="code">''' + pc('''# data gains a header at each layer on the way down (encapsulation)
message  = "GET /index.html"                       # Application layer: HTTP request
segment  = {"seq": 1, "port": 80, "data": message}   # Transport layer: sequence number, port
packet   = {"src": "192.168.1.5", "dst": "93.184.216.34", "data": segment}   # Internet layer: IP addresses
frame    = {"mac_src": "AA:01", "mac_dst": "BB:02", "data": packet}          # Link layer: MAC addresses
# the receiver removes the headers in the opposite order, Link first, Application last''') + '''</div>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Putting the layers in the wrong order. The Application layer is the top, the Link layer the bottom.</li>
    <li>Describing the layers by the function of a different layer: <b>routing and IP addresses</b> are the <b>Internet</b> layer; <b>sequence numbers, error checking and re-sending</b> are the <b>Transport</b> layer.</li>
    <li>Saying a protocol is "a program". It is a set of rules.</li>
    <li>Writing that layers talk to every other layer. Only <b>adjacent</b> layers interact.</li>
    <li>Describing the layers' functions when the question says <i>not</i> to (for example "describe how the suite is applied when a message is sent"): describe the stack, the direction down then up, and the interface.</li>
  </ul>
'''

watch = '''
  <h2>1 · A message goes down the stack, across, and up</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stA"></div>
  <h2>2 · Headers are added at each layer</h2>
  <div id="stB"></div>
  <h2>3 · Only adjacent layers talk to each other</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Build the packet</h2>
  <p>Choose a layer to see what it adds on the way down. The data grows a header at each layer.</p>
  <div class="card"><div id="pB" class="btnrow"></div><div id="pO"></div><div class="verdict" id="pV"></div></div>

  <h2>Lab 2 · Which layer does the job?</h2>
  <p>Choose the layer for each job.</p>
  <div class="card"><div id="wB" class="btnrow"></div><div id="wO"></div></div>

  <h2>Lab 3 · The layers compared</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · Which layer?</h2><div id="cl1" class="card"></div>
  <h2>2 · Protocol facts or stack facts?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the layers in order, top to bottom</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Counting layers and packets</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Loading a web page", "Your browser (Application layer) asks for a page with HTTP. The Transport layer splits the reply into numbered packets, the Internet layer addresses each one, and the Link layer sends it over Wi-Fi to your router.", "each layer does its own job, and the message passes down then up the stack.") +
rw("Devices from different makers", "A phone, a laptop and a games console from different companies all browse the same website because they all follow the TCP/IP protocols.", "a protocol is a standard that makes communication independent of the hardware and software.") +
rw("Upgrading Wi-Fi", "Moving from Wi-Fi 5 to Wi-Fi 6 changes the Link layer. The web page, the browser and the IP addresses are unchanged, because the layers are separate.", "layers can be improved independently, and only adjacent layers interact.") +
rw("A lost packet", "If a packet in a video call is lost, the Transport layer notices that a sequence number is missing and asks for it to be sent again, without the video app having to do anything.", "the Transport layer handles sequencing, flow and error recovery.") +
rw("Finding the way", "A router reads the destination IP address, which was added by the Internet layer, to decide where to send each packet next.", "routing and IP addresses belong to the Internet layer.")
)

where = [
  ("O/N 2022", "32", "3(a), 3(b)", "2 + 2", "Why a protocol is used; complete the TCP/IP stack diagram"),
  ("M/J 2024", "32", "2(a)", "2", "Why protocols are essential"),
  ("O/N 2025", "31", "3(a)", "2", "Why protocols are essential for communication"),
  ("O/N 2022", "31, 33", "2", "5", "Functions of the Transport and Internet layers"),
  ("M/J 2024", "31, 33", "2(a), 2(b)", "2 + 2", "Order the four layers; the function of the Transport layer"),
  ("O/N 2024", "31, 33", "4", "4", "How the layers of the stack interact"),
  ("M/J 2025", "31", "3(a)", "5", "Purpose of the Application layer and the Transport layer"),
  ("M/J 2025", "32", "3", "1 + 4", "Identify two layers; how the suite is applied when a message is sent"),
  ("M/J 2025", "33", "4(a)", "5", "Purpose of the Internet layer and the Link layer"),
  ("O/N 2023", "31, 33", "2(b)", "2", "The purpose of the Link layer"),
  ("O/N 2023", "32", "4", "3", "Complete a paragraph about a protocol suite"),
  ("M/J 2026", "31", "4", "4", "Match each TCP/IP layer to its description"),
  ("M/J 2026", "32", "2", "4", "Complete a paragraph about TCP/IP"),
  ("M/J 2026", "33", "2", "4", "Complete a paragraph about a protocol suite and its stack")]

past = '''  <p class="note">The protocol stack is one of the most regularly examined topics in this chapter: there is a TCP/IP question in Paper 3 in nearly every series from May/June 2022 to May/June 2026. The application-layer protocols (HTTP, FTP, SMTP, POP3, IMAP, BitTorrent) are on the next page. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Why protocols; the stack</h3>
''' + peq(SRC("w22", "32", "Q3(a), (b)"), "2 + 2 marks", "Explain / Complete",
  "(a) Explain why a protocol is used in communication between computers. (b) The TCP/IP protocol implementation can be viewed as a stack. Complete the diagram for the TCP/IP protocol stack, in which two of the layers, Transport and Link, are already shown." + qcode('''  [ ........ ]
  [ Transport ]
  [ ........ ]
  [ Link ]'''),
  "(a) a standard, so different devices can communicate. (b) the missing layers are the top and the third.",
  "<p><b>(a)</b> Any two: " + mks(["Protocols set a standard for communication", "They enable communication / compatibility between devices from different manufacturers or platforms", "If two devices used different protocols they would not be able to communicate properly"]) + "</p><p><b>(b)</b> " + mks(["Application (top)", "Internet / Network (third)"], "a") + "</p>" + qcode('''  [ Application ]
  [ Transport ]
  [ Internet ]
  [ Link ]'''),
  "Writing 'Network' or 'Physical' as the bottom layer. The bottom layer of the exam stack is Link.") + peq(SRC("s24", "32", "Q2(a)"), "2 marks", "Outline",
  "Outline why protocols are essential for communication between computers.",
  "A standard set of rules, and what it allows.",
  "<p>" + mks(["Protocols provide a standard set of rules that enables successful data transfer between devices", "they allow communication between devices on different platforms / make communication independent of software and hardware"]) + "</p>", None) + peq(SRC("w25", "31", "Q3(a)"), "2 marks", "Explain",
  "Explain why protocols are essential for communication between computer systems.",
  "Standard rules, compatibility, and what happens without one.",
  "<p>" + mks(["Protocols set a standard for communication (a standard set of rules)", "They enable compatibility between devices from different manufacturers or platforms, which could not communicate if they used different protocols"]) + "</p>", None) + peq(SRC("s24", "31, 33", "Q2(a), (b)"), "2 + 2 marks", "Complete / Describe",
  "The TCP/IP protocol suite has four layers: Transport, Application, Link, Internet. (a) Complete the diagram to show the correct order for these layers. (b) Describe the function of the Transport layer.",
  "(a) Application at the top. (b) end-to-end delivery, packets, sequence numbers, error recovery.",
  "<p><b>(a)</b> " + mks(["all four in the correct positions (two marks; one mark for at least two correct)"]) + "</p>" + qcode('''Application
Transport
Internet
Link''') + "<p><b>(b)</b> Any two: " + mks(["The Transport layer is responsible for delivery of data from the source host to the destination host", "Data is broken into packets and passed to the Internet layer", "It adds the sequence number to the packet header", "It establishes end-to-end contact", "It ensures data arrives error free / retransmits packets if lost"], "a") + "</p>", None) + peq(SRC("w24", "31, 33", "Q4"), "4 marks", "Describe",
  "The TCP/IP protocol may be viewed as a stack that contains four layers: Application, Transport, Internet, Link. Describe how the layers of the TCP/IP protocol stack interact with each other.",
  "Adjacent layers only, an interface, headers, software, user at the top and hardware at the bottom.",
  "<p>Any four: " + mks(["Each layer can only accept input from the next higher layer or the next lower layer", "There is an interface between adjacent layers, which is the only interaction between layers", "Data is added to the headers as the frames / packets pass through the layers", "The interactions are carried out by installed software", "User interaction takes place at the highest (Application) layer, through its protocols", "Direct access to the hardware takes place at the lowest (Link) layer"]) + "</p>", None) + peq(SRC("s25", "32", "Q3"), "1 + 4 marks", "Identify / Describe",
  "(a) Identify two different layers of the TCP/IP protocol suite. (b) Describe how the TCP/IP protocol suite is applied when a message is sent through the internet from one host to another. Do not describe the function of individual layers.",
  "(b) about the stack and the direction of travel, not what each layer does.",
  "<p><b>(a)</b> " + mks(["Any two of Application, Transport, Internet, Link"]) + "</p><p><b>(b)</b> Any four: " + mks(["The suite can be viewed as layers within a stack", "Each layer can only accept input from the next higher or lower (adjacent) layer", "The user interfaces with the top (Application) layer to send or receive a message", "A sent message passes from the Application layer down to the Link layer", "A received message passes from the Link layer up to the Application layer", "The Link layer interfaces directly with the network and sends / receives the message"], "a") + "</p>", None) + '''
  <h3>The functions of the layers</h3>
''' + peq(SRC("w22", "31, 33", "Q2"), "5 marks", "Outline",
  "Outline the functions of the Transport and Internet layers of the TCP/IP protocol suite.",
  "Up to three for each layer.",
  "<p>Transport (max 3): " + mks(["breaks data into manageable packets (segmentation)", "sequences the packets / adds a packet header", "sends packets to the Internet layer / receives data from the Application layer", "controls the flow of packets", "handles packet loss or corruption: acknowledges receipt of complete, error-free packets"]) + " Internet (max 3): " + mks(["identifies the intended network and host", "transmits packets to the Link layer", "routes the packets independently by the optimum route", "addresses packets with source and destination IP addresses", "uses an IP address and port number to form a socket"], "a") + "</p>", "Giving a Transport function (sequencing, re-sending) for the Internet layer.") + peq(SRC("s25", "31", "Q3(a)"), "5 marks", "Describe",
  "The Application Layer and Transport Layer are two layers of the TCP/IP protocol suite. Describe the purpose of the Application Layer and the purpose of the Transport Layer.",
  "Up to three for each.",
  "<p>Application (max 3): " + mks(["To provide services / an interface with the user (access to applications such as login, file transfer, email)", "To provide mechanisms for securing communication, e.g. encryption / authentication", "To define the protocols used to exchange data", "Error detection and recovery for application-specific errors"]) + " Transport (max 3): " + mks(["To provide logical communication between applications on different hosts / deliver data to the correct application process", "To ensure error-free, end-to-end delivery of data in sequence, with error detection and automatic repeat request", "To break data into segments when sent and reassemble them at the destination", "To regulate network connections / provide flow control to prevent data loss"], "a") + "</p>", None) + peq(SRC("s25", "33", "Q4(a)"), "5 marks", "Describe",
  "The Internet layer and Link layer are two layers of the TCP/IP protocol suite. Describe the purpose of the Internet layer and the purpose of the Link layer.",
  "Internet: IP addresses and routing. Link: frames, MAC addresses, the next hop.",
  "<p>Internet (max 3): " + mks(["To identify the intended network and host", "To add a header containing source and destination IP addresses", "To prepare packets for delivery, formatting them into datagrams", "To route datagrams through the optimum route"]) + " Link (max 3): " + mks(["To prepare the next hop by managing the link between two directly connected devices", "To format datagrams into frames for transmission", "To identify network protocols in the packet header", "To deliver frames to and receive frames from the network, mapping IP addresses to MAC (physical) addresses", "To provide error checking and correction, including resend requests"], "a") + "</p>", None) + peq(SRC("w23", "31, 33", "Q2(b)"), "2 marks", "Outline",
  "Outline the purpose of the Link layer in the TCP/IP protocol suite.",
  "Frames, MAC addresses, the physical medium.",
  "<p>Any two: " + mks(["To ensure correct network protocols are followed", "To enable the upper layers to access the physical medium / enable connection with the Internet layer", "To be responsible for transporting data within the network / local segments", "To format the data into frames for transmission", "To map IP addresses to MAC (physical) addresses"]) + "</p>", None) + '''
  <h3>Matching and completing</h3>
''' + peq(SRC("s26", "31", "Q4"), "4 marks", "Match",
  "Draw one line to connect each TCP/IP layer to its most appropriate description. Layers: Application, Transport, Internet, Link. Descriptions: (A) ensures packets arrive in sequence without errors; (B) provides remote access to files on a host server to access and manage files stored in a remote location; (C) interconnects nodes or hosts in a network, encapsulates IP packets into frames and ensures correct protocols are followed; (D) identifies the intended network and host; (E) contains all the programs that exchange data and includes protocols: HTTP, FTP and POP3.",
  "Five descriptions, four layers: one is a distractor.",
  "<p>" + mks(["Application matches (E): the programs that exchange data, and the protocols HTTP, FTP and POP3", "Transport matches (A): packets in sequence without errors", "Internet matches (D): identifies the intended network and host", "Link matches (C): interconnects nodes, encapsulates IP packets into frames"]) + "</p><p>Description (B) is the odd one out: it describes what the FTP protocol offers, not a layer.</p>", "Matching Link to 'identifies the intended network and host'. That is the Internet layer.") + peq(SRC("s26", "32", "Q2"), "4 marks", "Complete",
  "Complete the paragraph using the most appropriate words from the list. Some words are not used. Words: application, controls, disconnects, four, interconnects, internet, link, lists, many, packets, seven, transport." + qcode('''The TCP/IP protocol suite consists of ........ layers which can be thought of as a stack. It is
designed to send ........ of data across the internet. It is also used as a communications
protocol to ensure accurate delivery of data over private networks. The lowest layer of the
stack is the ........ layer. This is the layer that ........ nodes in the network.'''),
  "Four layers; data sent in packets; the lowest layer is Link; it interconnects nodes.",
  "<p>" + mks(["four", "packets", "link", "interconnects"]) + "</p>", None) + peq(SRC("s26", "33", "Q2"), "4 marks", "Complete",
  "Complete the paragraph using words from the list. Words: adjacent, Application, BitTorrent, corresponding, Internet, layer, Link, lower, protocol, route, Transport, upper." + qcode('''The implementation of a ........ suite can be viewed as a stack. Each ........ of the stack has its
own specific functionality and can only communicate with ........ layers of the stack. User
interaction is associated with the highest level of the stack, which is the ........ layer.'''),
  "A stack of layers: each layer talks only to its adjacent layers.",
  "<p>" + mks(["protocol", "layer", "adjacent", "Application"]) + "</p>", None) + peq(SRC("w23", "32", "Q4"), "3 marks", "Complete",
  "Complete the paragraph about a protocol suite, using words from the list. Words include: BitTorrent, circuit switching, layered, link, peer-to-peer, queue, stack, star, TCP/IP." + qcode('''The protocols in a ........ determine the interconnectivity rules for a ........ network model such
as the ........ model.'''),
  "A stack of protocols; the model is layered.",
  "<p>" + mks(["stack", "layered", "TCP/IP"]) + "</p>", None)

review = req("2 marks", "State", "State two reasons why a layered protocol stack is used rather than one large protocol.", "Think about changing one part.",
  "<p>" + mks(["Each layer has its own function and can be designed, tested and improved on its own.", "A layer can be replaced (for example a new Link layer for Wi-Fi) without changing the other layers."]) + "</p>", None) + req("3 marks", "Describe", "A browser requests a web page. Describe what the Transport layer does to the reply before it is sent.", "Packets, numbers, the header.",
  "<p>" + mks(["It breaks the reply into packets (segments).", "It adds a header containing a sequence number (and port number) to each.", "It passes the packets to the Internet layer, and later checks they arrive complete and in order."]) + "</p>", None) + req("2 marks", "Identify", "Name the layer that (a) adds the source and destination IP addresses; (b) formats the data into frames for the physical network.", "Internet, then Link.",
  "<p>" + mks(["(a) Internet layer", "(b) Link layer"]) + "</p>", None) + req("3 marks", "Explain", "Explain what is meant by saying that a layer can only interact with the adjacent layers.", "Which layers can the Transport layer deal with?",
  "<p>" + mks(["A layer only takes input from the layer directly above it or directly below it.", "The Transport layer deals only with the Application and Internet layers.", "The interface between two adjacent layers is the only interaction between them."]) + "</p>", None) + req("3 marks", "Complete", "Describe how a message travels through the TCP/IP stack from a sender to a receiver. Do not describe the individual functions of the layers.", "Down, across, up.",
  "<p>" + mks(["The message is created at the Application layer and passes down through the layers to the Link layer, with data added to the header at each.", "The Link layer sends it over the network.", "At the receiver it passes up from the Link layer to the Application layer and the headers are removed."]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on why protocols are used, the protocol stack and the TCP/IP layers (Paper 3), 2022 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Learn the order.", "Application, Transport, Internet, Link: top to bottom."),
  ("Match the job to the layer.", "Sequence numbers, packets, re-sending: Transport. IP addresses, routing: Internet. Frames, MAC addresses, the cable or Wi-Fi: Link. User services: Application."),
  ("Say 'adjacent'.", "A layer interacts only with the layer above and the layer below."),
  ("Say 'down then up'.", "Sending goes top to bottom, receiving bottom to top."),
  ("Use the exam's wording for a protocol.", "A standard set of rules enabling communication between devices from different manufacturers."),
  ("Read what is excluded.", "If the question says not to describe the functions of the layers, describe how the stack is used instead."),
], [
  ("why protocols are essential", "They set a standard so that devices from different manufacturers can communicate."),
  ("how the layers interact", "Each layer only accepts input from the adjacent layers, through the interface between them."),
  ("what the Transport layer does", "It breaks data into numbered packets and ensures they arrive error free and in order."),
  ("what the Internet layer does", "It adds the source and destination IP addresses and routes each packet."),
], [("State / Identify", "Give the name or fact only."), ("Outline", "Give the main points briefly."), ("Describe", "Say what it does, in several points."), ("Explain", "Give the reason as well.")]) + FC

js = AKJS + AK20JS + r'''
const LAYERS = [["Application", "f1", "HTTP request / the message", "message"], ["Transport", "f2", "seq number, port", "segments"], ["Internet", "f3", "source and destination IP address", "packets"], ["Link", "f4", "MAC addresses, frame check", "frames"]];

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const stack = (x, title, hl) => { let t = SV.text(x + 90, 20, title, "lbl bd", { "text-anchor": "middle" }); LAYERS.forEach((l, i) => (t += SV.rect(x, 30 + i * 46, 180, 40, hl === i ? "cell-warn" : l[1], { rx: 6, ...op(hl === i ? 1 : 0.6) }) + SV.text(x + 90, 55 + i * 46, l[0], "lbl bd", { "text-anchor": "middle", style: "font-size:15px" }))); return t; };
    const hlS = k >= 1 && k <= 4 ? k - 1 : -1, hlR = k >= 6 && k <= 9 ? 9 - k : -1;
    o += stack(40, "Sender", hlS) + stack(540, "Receiver", hlR);
    o += SV.line(220, 175, 540, 175, "dash", op(k >= 5 && k <= 5 ? 1 : 0.3)) + SV.text(380, 168, k === 5 ? "frames cross the network" : "network and routers", "sm", { "text-anchor": "middle" });
    if (k >= 1 && k <= 4) o += SV.text(260, 55 + (k - 1) * 46, "◀ " + ["creates the message", "adds sequence number, port", "adds IP addresses", "makes frames, sends"][k - 1], "sm");
    if (k >= 6 && k <= 9) o += SV.text(330, 55 + (9 - k) * 46, ["receives the frames ▶", "checks the IP address ▶", "orders and checks packets ▶", "gives message to the program ▶"][k - 6], "sm");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 225, label: "A message through the TCP/IP stack", base: { i: 0 }, draw, tween: 250, dwell: 2600, steps: [
    { cap: "Two hosts, each with the same four-layer stack. A message is sent from the left to the right.", s: { i: 0 } },
    { cap: "<b>Application layer</b>: the user's program creates the message using a protocol such as HTTP.", s: { i: 1 } },
    { cap: "<b>Transport layer</b>: breaks it into packets and adds a header with a sequence number.", s: { i: 2 } },
    { cap: "<b>Internet layer</b>: adds the source and destination IP addresses.", s: { i: 3 } },
    { cap: "<b>Link layer</b>: formats the packets into frames with MAC addresses and sends them over the physical network.", s: { i: 4 } },
    { cap: "The frames travel across the network, passing through routers.", s: { i: 5 } },
    { cap: "At the receiver the <b>Link layer</b> receives the frames, the first step on the way <b>up</b>.", s: { i: 6 } },
    { cap: "The <b>Internet layer</b> checks the destination IP address and passes the packets up.", s: { i: 7 } },
    { cap: "The <b>Transport layer</b> puts the packets in order using the sequence numbers and checks for loss or errors.", s: { i: 8 } },
    { cap: "The <b>Application layer</b> gives the complete message to the program.", s: { i: 9 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 22, "On the way down: each layer wraps what it receives", "lbl bd");
    const widths = [220, 300, 380, 460];
    for (let i = 0; i <= 3; i++) { const lv = i, v = k >= lv ? 1 : 0; if (!v) continue; const w = widths[3 - lv] + 160, x = 30 + (3 - lv) * 0; o += SV.rect(30 + lv * 22, 34 + lv * 34, 700 - lv * 44, 160 - lv * 34 - 0, LAYERS[lv][1], { rx: 8, ...op(0.32) }) + SV.text(44 + lv * 22, 52 + lv * 34, [ "Application: message", "Transport header: seq, port", "Internet header: IP addresses", "Link header: MAC addresses" ][lv], "lbl bd", { style: "font-size:13px" }); }
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 215, label: "Encapsulation", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "The Application layer produces the <b>message</b> (the data).", s: { i: 0 } },
    { cap: "The Transport layer adds a <b>header</b> in front: the sequence number and port.", s: { i: 1 } },
    { cap: "The Internet layer adds its own header with the <b>source and destination IP addresses</b>.", s: { i: 2 } },
    { cap: "The Link layer adds the <b>MAC addresses</b> to make a frame. Each layer treats everything from the layer above as its data. The receiver removes the headers in the opposite order.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    LAYERS.forEach((l, i) => { o += SV.rect(240, 20 + i * 48, 280, 40, k === 1 && i === 1 ? "cell-warn" : l[1], { rx: 6, ...op(0.7) }) + SV.text(380, 46 + i * 48, l[0], "lbl bd", { "text-anchor": "middle" }); });
    if (k >= 1) { o += arrow(380, 68, 380, 108, "d", "c2", 0) ; }
    if (k === 1) o += SV.text(30, 208, "Transport talks only to Application (above) and Internet (below)", "lbl bd", { style: "font-size:14px" });
    if (k === 2) o += SV.text(30, 208, "Application never talks straight to Internet or Link", "lbl bd t2", { style: "font-size:14px" }) + SV.path("M 240 40 C 190 40 190 112 240 112", "c3", { fill: "none", "stroke-width": 2.5, "stroke-dasharray": "6 4" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 225, label: "Adjacent layers", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "The four layers form a stack. Each has its own functionality.", s: { i: 0 } },
    { cap: "A layer can only accept input from the <b>next higher</b> or <b>next lower</b> layer. The Transport layer exchanges data only with the Application and Internet layers, through the interface between them.", s: { i: 1 } },
    { cap: "The Application layer cannot skip a layer and talk straight to the Link layer. Each layer relies on the one below it.", s: { i: 2 } }] });
})();

/* Lab 1 */
(function () {
  let cur = 0;
  const rows = [["Application", "GET /index.html", "The message from the program", "HTTP"], ["Transport", "[seq 1, port 80] GET /index.html", "Packets numbered and ported", "TCP"], ["Internet", "[src 192.168.1.5, dst 93.184.216.34] [seq 1, port 80] GET ...", "IP addresses added", "IP"], ["Link", "[MAC AA:01 → BB:02] [IP addresses] [seq, port] GET ...", "A frame for the local network", "Ethernet / Wi-Fi"]];
  const paint = () => {
    $$("#pB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    $("#pO").innerHTML = rows.slice(0, cur + 1).map((r, i) => `<div class="tw"><table class="t mono"><tr><th>${r[0]} layer</th><td style="${i === cur ? "background:var(--warn-soft)" : ""}">${r[1]}</td></tr></table></div>`).join("");
    $("#pV").textContent = rows[cur][0] + " layer: " + rows[cur][2] + " (protocols: " + rows[cur][3] + ").";
  };
  $("#pB").innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  $$("#pB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); })); paint();
})();

/* Lab 2 */
(function () {
  const jobs = [["Adds the source and destination IP addresses to a packet", 2], ["Splits the data into numbered packets and re-sends lost ones", 1], ["Provides the interface a web browser uses to fetch a page", 0], ["Formats packets into frames and uses MAC addresses", 3], ["Chooses the best route for each packet", 2], ["Controls the flow of packets so the receiver is not overwhelmed", 1]];
  let cur = 0, pick = null;
  const paint = () => {
    $$("#wB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const j = jobs[cur]; $("#wO").innerHTML = `<p><b>${j[0]}</b></p><div class="btnrow">` + LAYERS.map((l, i) => `<button class="b${pick === i ? " pri" : ""}" data-i="${i}">${l[0]}</button>`).join("") + '</div><div class="verdict">' + (pick === null ? "Choose a layer." : pick === j[1] ? "Correct: the " + LAYERS[j[1]][0] + " layer." : "Not the " + LAYERS[pick][0] + " layer. It is the " + LAYERS[j[1]][0] + " layer.") + "</div>";
    $$("#wO button").forEach((b) => (b.onclick = () => { pick = +b.dataset.i; paint(); }));
  };
  $("#wB").innerHTML = jobs.map((j, i) => `<button class="b" data-i="${i}">Job ${i + 1}</button>`).join("");
  $$("#wB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; pick = null; paint(); })); paint();
})();

btnTable("eB", "eO", [
  ["Application", "Services and interface to the user; the programs that exchange data", "HTTP(S), FTP, SMTP, POP3, IMAP, BitTorrent", "The message", "Describing it as the 'physical' layer"],
  ["Transport", "End-to-end delivery: packets, sequence numbers, flow control, error recovery", "TCP, UDP", "Segments / packets", "Giving it IP addresses"],
  ["Internet", "Identifies the network and host; IP addresses; routes packets", "IP", "Packets / datagrams", "Giving it re-sending of lost packets"],
  ["Link", "Frames, MAC addresses, the next hop, the physical medium", "Ethernet, Wi-Fi", "Frames", "Calling it the 'Network' layer"]
], ["Layer", "Purpose and function", "Protocols", "Data unit", "Trap"]);
''' + CLASSIFY("cl1", "Which layer does each job belong to?", ["Application", "Transport", "Internet", "Link"],
  [("Provides an interface to the user's programs", 0), ("Adds a sequence number to each packet", 1), ("Adds the source and destination IP address", 2), ("Formats datagrams into frames", 3), ("Controls the flow of packets", 1), ("Routes each packet by the best route", 2), ("Maps IP addresses to MAC addresses", 3), ("Defines the protocols programs use to exchange data", 0)],
  "Application: user. Transport: packets and sequence. Internet: IP and routing. Link: frames and MAC.") + CLASSIFY("cl2", "Is the statement about a protocol or about the stack?", ["About a protocol", "About the stack"],
  [("A standard set of rules for communication", 0), ("Layers that can only talk to adjacent layers", 1), ("Allows devices from different manufacturers to communicate", 0), ("Headers are added on the way down", 1), ("Makes communication independent of hardware and software", 0), ("User interaction at the top, hardware access at the bottom", 1)],
  "A protocol is the rules. The stack is the layered way of implementing them.") + ORDER(
  "Put the layers in order, from the top (nearest the user) to the bottom.",
  ["Application", "Transport", "Internet", "Link"],
  "Application, Transport, Internet, Link.") + MATCH([
  ["Protocol", "A set of rules for communication between devices"], ["Stack", "Layers of protocols, each with its own function"], ["Header", "Information added to data by a layer"], ["Interface", "The only point of interaction between adjacent layers"], ["Packet", "A small chunk of a message sent independently"]]) + CALC([
  {"q": "How many layers are in the TCP/IP protocol suite as used in the exam?", "a": 4, "unit": "", "tol": 0.01, "hint": "Application, Transport, Internet, Link.", "sol": "<b>4</b>."},
  {"q": "A message goes down the stack. How many headers have been added by the time it leaves the Link layer (one for each layer below the Application layer)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Transport, Internet and Link.", "sol": "<b>3</b>."},
  {"q": "A message of 4000 bytes is split into packets of 500 bytes. How many packets?", "a": 8, "unit": "", "tol": 0.01, "hint": "4000 ÷ 500.", "sol": "<b>8</b>."},
  {"q": "How many layers can the Transport layer exchange data with directly?", "a": 2, "unit": "", "tol": 0.01, "hint": "The adjacent layers above and below.", "sol": "<b>2</b>."},
  {"q": "How many layers can the Application layer exchange data with directly?", "a": 1, "unit": "", "tol": 0.01, "hint": "It is the top: only the Transport layer below.", "sol": "<b>1</b>."}]) + MCQ([
  ("Which layer breaks data into packets and adds sequence numbers?", ["Application", "Transport", "Internet", "Link"], 1, "That is the Transport layer."),
  ("Which layer adds source and destination IP addresses?", ["Internet", "Link", "Application", "Transport"], 0, "Internet."),
  ("Which is the bottom layer of the TCP/IP stack?", ["Application", "Transport", "Internet", "Link"], 3, "Link."),
  ("Why are protocols used?", ["To make computers faster", "To provide a standard so different devices can communicate", "To store data", "To encrypt data"], 1, "A standard set of rules."),
  ("A layer can only interact with...", ["any other layer", "the adjacent layers", "the top layer", "the bottom layer"], 1, "Above and below."),
  ("Where does user interaction take place?", ["Link layer", "Internet layer", "Application layer", "Transport layer"], 2, "At the top of the stack.")], "qz1") + CARDS([
  ("Protocol", "A standard set of rules for communication."), ("Application", "User services; HTTP, FTP, SMTP, POP3, IMAP, BitTorrent."), ("Transport", "Packets, sequence numbers, flow control, error recovery."), ("Internet", "IP addresses and routing."),
  ("Link", "Frames, MAC addresses, the physical medium."), ("Adjacent", "A layer interacts only with the layer above and below."), ("Sending", "Down the stack; headers added."), ("Receiving", "Up the stack; headers removed.")])

build("ac1411", "ac-14-1-1-protocols-tcp-ip-stack", "Protocols and the TCP/IP Stack", EYA("14.1.1"),
  "Why protocols are essential, the layered protocol stack and the four TCP/IP layers with their functions, how a message passes down and up the stack; animations, labs and the real 9618 questions from 2022 to 2026.",
  dict(sub=CBK("Chapter 14 · Communication and internet technologies, section 14.1 Protocols"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
