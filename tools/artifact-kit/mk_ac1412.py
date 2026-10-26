"""A Level CS syllabus 14.1.2: application layer protocols (HTTP, FTP, SMTP, POP3, IMAP, BitTorrent). Run: python3 tools/artifact-kit/mk_ac1412.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>The Application layer of TCP/IP contains the protocols that programs use to exchange data, and you need to know six and what each is for. <b>HTTP(S)</b> transfers the hypertext documents that make up web pages, <b>FTP</b> sends and receives files between devices, <b>SMTP</b> sends email, and <b>POP3</b> and <b>IMAP</b> receive email. <b>BitTorrent</b> shares files peer-to-peer, with the pieces of a file coming from many users' computers instead of one server. SMTP is a <b>push</b> protocol (the sender pushes mail out), and POP3 and IMAP are <b>pull</b> protocols (the receiving client pulls mail from the server). The exam asks you to name a protocol and describe its use, or to match protocols to uses.</p></div>

  <h2>1 · The six protocols</h2>
  <div class="tw"><table class="t">
    <tr><th>Protocol</th><th>Purpose</th><th>Key points</th></tr>
    <tr><td><b>HTTP / HTTPS</b> (Hypertext Transfer Protocol; S = secure)</td><td>Sending and receiving <b>web pages</b> / hypertext documents (and images, video) between a web server and a browser</td><td>The browser sends a <b>request</b>, the server a <b>response</b>. HTTPS is encrypted (TLS)</td></tr>
    <tr><td><b>FTP</b> (File Transfer Protocol)</td><td>Sending and receiving <b>files</b> over a network, between devices: uploading to and downloading from a server</td><td>Used to move files such as a website's pages to a web server</td></tr>
    <tr><td><b>SMTP</b> (Simple Mail Transfer Protocol)</td><td><b>Sending</b> email: from a computer to a mail server, and between mail servers</td><td>A <b>push</b> protocol: it delivers mail towards the destination</td></tr>
    <tr><td><b>POP3</b> (Post Office Protocol 3)</td><td><b>Receiving</b> email: the email client retrieves (downloads) messages from the mail server</td><td>A <b>pull</b> protocol. By default the message is downloaded to one device and removed from the server</td></tr>
    <tr><td><b>IMAP</b> (Internet Message Access Protocol)</td><td><b>Receiving</b> email: lets users access and read email from <b>any device</b> without removing it from the mail server</td><td>A <b>pull</b> protocol. Keeps the server and the client <b>in sync</b>, so a copy stays on the server</td></tr>
    <tr><td><b>BitTorrent</b></td><td><b>Peer-to-peer file sharing</b> over a network or the internet</td><td>No central web server holds the file; users share pieces directly with each other</td></tr>
  </table></div>
  <div class="tip"><b class="h">Sending against receiving</b>Sending email: <b>SMTP</b>. Receiving email: <b>POP3</b> or <b>IMAP</b>. An exam answer for "name a protocol associated with sending and one with receiving" is SMTP and POP3 or IMAP.</div>

  <h2>2 · How an email travels</h2>
  <ol>
    <li>You write a message in your email client and press send. The client uses <b>SMTP</b> to push it to your outgoing mail server.</li>
    <li>Your mail server uses <b>SMTP</b> to pass it to the recipient's mail server (and on, via other servers, if needed).</li>
    <li>The recipient's mail server stores it in their mailbox.</li>
    <li>The recipient's client <b>pulls</b> it with <b>POP3</b> (download, normally removing it from the server) or <b>IMAP</b> (view it, leaving it on the server, with every device in sync).</li>
  </ol>
  <div class="tw"><table class="t">
    <tr><th></th><th>POP3</th><th>IMAP</th></tr>
    <tr><td>Where mail is kept</td><td>Downloaded to the device, normally deleted from the server</td><td>Stays on the server; the device shows a copy</td></tr>
    <tr><td>Several devices</td><td>Messages end up on whichever device downloaded them</td><td>All devices see the same mailbox, in sync</td></tr>
    <tr><td>Needs a connection to read old mail</td><td>No: it is stored locally</td><td>Yes, to fetch it from the server (clients can cache)</td></tr>
  </table></div>

  <h2>3 · HTTP in a little more detail</h2>
  <p>A browser asks for a page with an HTTP <b>request</b> and the server answers with a <b>response</b>.</p>
  <pre class="plain">Request:   GET /index.html HTTP/1.1
           Host: www.example.com

Response:  HTTP/1.1 200 OK            (the status: 200 means success, 404 means page not found)
           Content-Type: text/html
           <html> ... the web page ... </html></pre>

  <h2>4 · How BitTorrent shares a file</h2>
  <ol>
    <li>A user who has the whole file creates a small <b>torrent (descriptor) file</b> with <b>metadata</b> about it: its name, size and the address of a tracker. The whole file must be on at least one peer to begin with.</li>
    <li>The file is divided into <b>equal-sized pieces</b>.</li>
    <li>Other users get the torrent file and connect to a <b>tracker</b>, which acts like a server holding data about all the computers sharing the file (the <b>swarm</b>).</li>
    <li>Each peer <b>downloads pieces from other peers</b>, many at once, until it has the whole file.</li>
    <li>As soon as a peer has a piece it becomes a <b>source</b> of that piece for others. A peer that has the complete file and keeps sharing it is a <b>seed</b>.</li>
  </ol>
  <p>This puts the load on the whole swarm instead of one server, so it can share files between thousands of users. All users are of <b>equal status</b>: there is no central web server.</p>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Writing "email" as the purpose of POP3 and IMAP without saying <b>receiving</b> (retrieving) email, and without saying SMTP is for <b>sending</b>.</li>
    <li>Saying IMAP "sends" email. It receives; SMTP sends.</li>
    <li>Not giving the difference between POP3 and IMAP: IMAP keeps the message on the server so it can be read from any device.</li>
    <li>Describing BitTorrent as "a website for downloading". It is a peer-to-peer protocol with no central server holding the file.</li>
    <li>Giving only the name of a protocol: the mark needs the <b>use</b> too.</li>
    <li>Describing HTTP as only for "the internet". It transfers hypertext documents (web pages).</li>
  </ul>
'''

watch = '''
  <h2>1 · An email's journey</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stA"></div>
  <h2>2 · POP3 against IMAP</h2>
  <div id="stB"></div>
  <h2>3 · BitTorrent: sharing pieces</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Which protocol does the job?</h2>
  <p>Choose the protocol for each situation.</p>
  <div class="card"><div id="wB" class="btnrow"></div><div id="wO"></div></div>

  <h2>Lab 2 · Run a BitTorrent swarm</h2>
  <p>Six peers share a file of 8 pieces. Peer A is the seed and has every piece. Press Next round: each peer downloads one piece from a peer that has it.</p>
  <div class="card"><div id="tS"></div><div class="btnrow"><button class="b pri" id="tN">Next round</button><button class="b" id="tR">Reset</button></div><div class="verdict" id="tV"></div></div>

  <h2>Lab 3 · The protocols compared</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · Which protocol?</h2><div id="cl1" class="card"></div>
  <h2>2 · Push or pull?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the journey of an email in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the protocol to its use</h2><div id="m1" class="card"></div>
  <h2>5 · BitTorrent counts</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Viewing a website", "Every page you open in a browser arrives through HTTP or HTTPS: the browser asks, the web server replies with the page, the images and the style files.", "HTTP(S) transfers web pages / hypertext documents.") +
rw("Uploading a school website", "A teacher uploads a new set of web pages to the school's web server using FTP, because FTP is designed to send and receive files between devices.", "FTP: sending and receiving files over a network.") +
rw("Reading your email on a phone and a laptop", "IMAP keeps the mail on the server, so the same inbox, with the same read and unread messages, appears on both devices.", "IMAP: access from any device without removing the message from the server.") +
rw("Sending a message", "When you press send, your email program hands the message to the outgoing mail server with SMTP, and mail servers use SMTP to pass it on.", "SMTP sends email; it is a push protocol.") +
rw("Downloading a large game or Linux image", "Instead of one overloaded server, the file comes in pieces from hundreds of other users who already have it, using BitTorrent.", "BitTorrent: peer-to-peer file sharing; no central server.")
)

where = [
  ("O/N 2022", "32", "3(c)", "2", "Describe the purpose of the IMAP protocol"),
  ("M/J 2022", "32", "3(a)", "4", "Identify two Application layer protocols and describe each"),
  ("M/J 2024", "31, 33", "2(c)", "2", "Outline one protocol associated with the Application layer"),
  ("M/J 2024", "32", "2(b), 2(c)", "2 + 3", "Email protocols for sending and receiving; the meaning of 'BitTorrent provides peer-to-peer file sharing'"),
  ("O/N 2023", "31, 33", "2(a)", "4", "Match four protocols to their uses"),
  ("O/N 2024", "32", "5", "4 + 3", "Name and describe two protocols; the purpose and function of the Application layer"),
  ("O/N 2025", "31", "3(b)", "4", "Identify and describe two email protocols other than POP3"),
  ("O/N 2025", "32", "3", "2 + 4", "Purpose of HTTP and IMAP; how files are shared using BitTorrent"),
  ("O/N 2025", "33", "4", "6", "Identify and describe three Application layer protocols")]

past = '''  <p class="note">The Application layer protocols are examined in Paper 3 in most series from May/June 2022 to Oct/Nov 2025, usually as a name-and-describe question. The TCP/IP layers themselves are on the previous page. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Name and describe</h3>
''' + peq(SRC("s22", "32", "Q3(a)"), "4 marks", "Identify / Describe",
  "The TCP/IP protocol suite has four layers. The application layer provides user services. Identify two protocols used by this layer. Describe the use of each protocol.",
  "One mark for the protocol and one for its use, twice.",
  "<p>Two protocols, one mark for the name and one for the matching description: " + mks(["HTTP(S): for sending and receiving web pages / hypertext documents", "FTP: for sending and receiving files over a network / between devices", "SMTP: for sending / uploading emails (a push protocol)", "POP3: for receiving / downloading emails (a pull protocol)", "IMAP: for receiving emails (a pull protocol), keeping them on the server"]) + "</p>",
  "Naming a protocol without a use, or giving the expansion only.") + peq(SRC("w25", "33", "Q4"), "6 marks", "Identify / Describe",
  "Identify and describe three protocols that are used in the Application layer of the TCP/IP protocol suite.",
  "Three protocols with a mark each for the name and for its use.",
  "<p>Any three, each as name [1] and description [1]: " + mks(["HTTP/HTTPS: transfers hypermedia documents / web pages / data files between networked devices", "FTP: downloads, uploads and transfers files from one location to another on a network", "POP3: retrieves / receives emails from a mail server to a computer", "IMAP: lets users access and read their emails from any device without removing the message from the mail server", "SMTP: sends emails between mail servers, or from a computer to a mail server", "BitTorrent: peer-to-peer file sharing"]) + "</p>", None) + peq(SRC("w24", "32", "Q5(a)"), "4 marks", "Name / Describe",
  "Name and describe two protocols used by the Application Layer of the TCP/IP protocol suite.",
  "One mark for each correct name and one for each correct description, maximum 2 + 2.",
  "<p>" + mks(["HTTP/HTTPS: sending and receiving / transferring web pages and hypertext", "FTP: sending and receiving files over a network / between devices", "POP3: a pull protocol for receiving / downloading emails", "IMAP: a pull protocol for receiving / downloading emails", "SMTP: a push protocol for sending / uploading emails", "BitTorrent: peer-to-peer file sharing over a network"]) + " (any two protocols with their descriptions)</p>", None) + peq(SRC("w25", "31", "Q3(b)"), "4 marks", "Identify / Describe",
  "POP3 is an email communication protocol. Identify and describe two other communication protocols that are used when sending or receiving emails.",
  "SMTP and IMAP are the two others.",
  "<p>" + mks(["SMTP", "a protocol used to send emails between mail servers, or from a computer to a mail server", "IMAP", "allows users to access / read their emails from any device without removing the message from the mail server, i.e. it synchronises emails on any device"]) + "</p>", "Giving POP3, which the question already names.") + peq(SRC("s24", "31, 33", "Q2(c)"), "2 marks", "Outline",
  "Outline one protocol that is associated with the Application layer.",
  "One mark for the name and one for the use.",
  "<p>One of: " + mks(["HTTP(S): responsible for the correct transfer of the hypertext documents that make up web pages", "FTP: used when transferring files from a server to a client on a network", "POP3 or IMAP: handles the receiving of emails", "SMTP: handles the sending of emails", "BitTorrent: provides peer-to-peer file sharing"]) + "</p>", None) + '''
  <h3>Email protocols and the purpose of a single protocol</h3>
''' + peq(SRC("w22", "32", "Q3(c)"), "2 marks", "Describe",
  "Describe the purpose of the IMAP protocol.",
  "Receiving email, retrieved by a client from a server, kept in sync.",
  "<p>Any two: " + mks(["Used by email clients to retrieve email messages (a pull protocol)", "from a mail server, over a TCP/IP connection", "It keeps the server and client in sync by not deleting the original email: a copy of the email is downloaded"]) + "</p>", None) + peq(SRC("w25", "32", "Q3(a)"), "2 marks", "State",
  "HTTP and IMAP are examples of protocols used in the Application Layer of the TCP/IP protocol suite. State the purpose of the HTTP and IMAP protocols.",
  "One mark each.",
  "<p>" + mks(["HTTP: to send and receive / transfer web pages, hypertext, images and videos", "IMAP: allows users to access and read their emails from any device without removing the message from the mail server / synchronises emails on any device"]) + "</p>", None) + peq(SRC("s24", "32", "Q2(b)"), "2 marks", "State",
  "State the names of two different protocols associated with the sending and receiving of emails between computers.",
  "One for sending, one for receiving.",
  "<p>" + mks(["Sending: SMTP", "Receiving: POP3 or IMAP"]) + "</p>", None) + peq(SRC("w23", "31, 33", "Q2(a)"), "4 marks", "Match",
  "Draw one line from each protocol to its most appropriate use. Protocols: HTTP, BitTorrent, SMTP, IMAP. Uses: (A) to provide peer-to-peer file sharing; (B) when retrieving email messages from a mail server over a TCP/IP connection; (C) when transmitting hypertext documents; (D) to map MAC addresses onto IP addresses; (E) when sending email messages towards the intended destination.",
  "Five uses, four protocols: (D) is the distractor.",
  "<p>" + mks(["HTTP matches (C) transmitting hypertext documents", "BitTorrent matches (A) peer-to-peer file sharing", "SMTP matches (E) sending email messages towards the destination", "IMAP matches (B) retrieving email from a mail server"]) + "</p><p>(D) is not an Application layer protocol use: mapping MAC addresses onto IP addresses is done at the Link layer.</p>", "Matching SMTP to retrieving email. SMTP sends; IMAP and POP3 retrieve.") + '''
  <h3>BitTorrent and the Application layer</h3>
''' + peq(SRC("s24", "32", "Q2(c)"), "3 marks", "Explain",
  "Explain the meaning of the phrase: BitTorrent protocol provides peer-to-peer file sharing.",
  "Many users, directly, no central server, equal status.",
  "<p>Any three: " + mks(["BitTorrent allows the sharing of files between thousands of users connected together over the internet", "It allows more users to share files with each other than would be the case with a simple peer-to-peer network", "Users share files directly with each other: their computers act as peers", "No web server / central device is used: all users are of equal status"]) + "</p>", None) + peq(SRC("w25", "32", "Q3(b)"), "4 marks", "Describe",
  "Describe how files are shared using the BitTorrent protocol.",
  "Torrent file, pieces, tracker and swarm, peers become sources, seeds.",
  "<p>Any four: " + mks(["Files are shared over a peer-to-peer network", "A small torrent (descriptor) file with metadata about the file is created by a peer", "The whole file must initially be on at least one peer", "The file is broken into equal-sized pieces", "Other peers obtain the torrent file and connect to a tracker, which holds data about all the computers in the swarm", "Each peer downloads parts of the file from other peers until it has the whole file", "As each peer receives a piece it becomes a source for that piece", "A peer that has the complete file and shares it is a seed"]) + "</p>", "Describing a central server that holds the file. In BitTorrent the tracker only holds data about the peers; the pieces come from the peers.") + peq(SRC("w24", "32", "Q5(b)"), "3 marks", "Explain",
  "Explain the purpose and function of the Application Layer in the TCP/IP protocol suite.",
  "User interface, the programs that exchange data, protocols.",
  "<p>Any three: " + mks(["The Application layer provides access to all the programs that exchange data / interacts directly with the user", "used by, for example, web browsers and server software", "It communicates with, and enables data transfer to and from, the Transport layer / allows applications to access the services of the other TCP/IP layers", "It defines the protocols that any application uses to exchange data"]) + "</p>", None)

review = req("2 marks", "Distinguish", "Distinguish between the SMTP and POP3 protocols.", "Sending against receiving.",
  "<p>" + mks(["SMTP is used to send email, from a client to a mail server and between mail servers (push).", "POP3 is used to receive email: the client downloads it from the mail server (pull)."]) + "</p>", None) + req("3 marks", "Compare", "Compare the POP3 and IMAP protocols for a user who reads email on a phone and a laptop.", "Where the mail is kept.",
  "<p>" + mks(["POP3 downloads the message to one device and normally removes it from the server, so the other device does not have it.", "IMAP leaves the message on the server and keeps all devices in sync.", "So IMAP is better for reading the same mail on two devices."]) + "</p>", None) + req("2 marks", "State", "State two ways in which sharing a file with BitTorrent differs from downloading it from a web server.", "Where does the file come from?",
  "<p>" + mks(["BitTorrent downloads pieces from many peers at once; a web server sends the whole file from one place.", "BitTorrent has no central server holding the file, and every peer that has a piece shares it."]) + "</p>", None) + req("2 marks", "Identify", "A web designer needs to copy a folder of new pages to the company's web server. Name the most suitable protocol and say why.", "Moving files.",
  "<p>" + mks(["FTP", "It is used for sending and receiving files over a network between devices"]) + "</p>", None) + req("3 marks", "Describe", "Describe what happens when a browser requests a web page using HTTP.", "Request and response.",
  "<p>" + mks(["The browser sends an HTTP request to the web server for the page.", "The server finds the page and sends an HTTP response containing the hypertext document, with a status such as 200.", "The browser displays the page."]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on the Application layer protocols (Paper 3), 2022 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Name and use.", "Every protocol answer needs the name and what it is used for."),
  ("SMTP sends, POP3 and IMAP receive.", "Say 'sending' or 'receiving' explicitly."),
  ("IMAP: any device, server copy kept.", "That is the distinction from POP3."),
  ("HTTP: web pages. FTP: files.", "Hypertext documents against file transfer."),
  ("BitTorrent: peer-to-peer, no central server.", "Pieces, torrent file, tracker, swarm, seed."),
  ("Do not give the protocol the question names.", "If POP3 is given, choose others."),
], [
  ("what HTTP is used for", "Sending and receiving web pages / hypertext documents."),
  ("what FTP is used for", "Sending and receiving files over a network between devices."),
  ("what SMTP is used for", "Sending email from a client to a mail server and between mail servers."),
  ("what BitTorrent is used for", "Peer-to-peer file sharing: users share pieces of a file directly with each other."),
], [("Name / Identify", "Give the protocol name."), ("Describe", "Say what it is used for, in a short sentence."), ("Outline", "Name it and give its use."), ("Explain", "Give the meaning with reasons.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const stops = ["Sender's email client", "Sender's mail server", "Recipient's mail server", "Recipient's email client"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    stops.forEach((t, i) => (o += SV.rect(20 + i * 185, 60, 160, 60, k >= i ? "f3" : "cell", { rx: 8, ...op(k >= i ? 1 : 0.5) }) + SV.text(100 + i * 185, 96, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" })));
    const labs = ["SMTP", "SMTP", "POP3 or IMAP"]; labs.forEach((t, i) => { const on = k > i; o += arrow(180 + i * 185, 90, 205 + i * 185, 90, i === 2 ? "l" : "r", on ? "c2" : "c1", on ? 1 : 0.2) + SV.text(192 + i * 185, 50, t, "lbl bd" + (on ? " t3" : ""), { "text-anchor": "middle", style: "font-size:12px", ...op(on ? 1 : 0.35) }); });
    if (k >= 1) o += SV.text(30, 160, k === 1 ? "push: the client sends the message to its mail server" : k === 2 ? "push: servers pass the message towards its destination" : "pull: the recipient's client retrieves the message", "lbl bd", { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 190, label: "An email's journey", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "An email travels from the sender's email client to the recipient's email client through two mail servers.", s: { i: 0 } },
    { cap: "<b>SMTP</b> pushes the message from the sender's client to the sender's mail server.", s: { i: 1 } },
    { cap: "<b>SMTP</b> again carries it from server to server, towards its destination.", s: { i: 2 } },
    { cap: "The recipient's client <b>pulls</b> the message from the server with <b>POP3</b> or <b>IMAP</b>.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 22, "POP3", "lbl bd") + SV.text(400, 22, "IMAP", "lbl bd");
    const box = (x, t, on, cls) => SV.rect(x, 34, 150, 44, on ? cls : "cell", { rx: 6 }) + SV.text(x + 75, 61, t, "lbl", { "text-anchor": "middle", style: "font-size:13px" });
    o += box(30, "Mail server: 1 email", true, "f3") + box(400, "Mail server: 1 email", true, "f3");
    o += box(30, k >= 1 ? "Laptop: downloaded" : "Laptop", k >= 1, "cell-ok") + box(400, k >= 1 ? "Laptop: shows a copy" : "Laptop", k >= 1, "cell-ok");
    o += SV.rect(30, 130, 150, 44, k >= 2 ? "cell-no" : "cell", { rx: 6 }) + SV.text(105, 157, k >= 2 ? "Phone: nothing" : "Phone", "lbl", { "text-anchor": "middle", style: "font-size:13px" });
    o += SV.rect(400, 130, 150, 44, k >= 2 ? "cell-ok" : "cell", { rx: 6 }) + SV.text(475, 157, k >= 2 ? "Phone: shows a copy" : "Phone", "lbl", { "text-anchor": "middle", style: "font-size:13px" });
    if (k >= 1) { o += SV.rect(30 + 160, 34, 190, 44, k >= 1 ? "cell-no" : "cell", { rx: 6 }) + SV.text(285, 61, "removed from the server", "lbl", { "text-anchor": "middle", style: "font-size:12px" }); o += SV.text(560, 61, "stays on the server", "lbl bd t3", { style: "font-size:13px" }); }
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 200, label: "POP3 and IMAP", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "One email waits on the mail server. The user has a laptop and a phone.", s: { i: 0 } },
    { cap: "The laptop retrieves it. With <b>POP3</b> the message is downloaded and normally removed from the server; with <b>IMAP</b> the server keeps it and the laptop shows a copy.", s: { i: 1 } },
    { cap: "Later the user checks the phone. With POP3 the email is not there (it was downloaded to the laptop). With IMAP the phone shows the same email, <b>in sync</b>.", s: { i: 2 } }] });
})();

(function () {
  const peers = [[0, 1, 2, 3, 4, 5], [0, 1, 2], [3, 4, 5], [0, 3], []];
  const names = ["Seed A", "Peer B", "Peer C", "Peer D", "Peer E"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    names.forEach((n, i) => { const y = 20 + i * 38; let have = peers[i].slice(); if (k >= 2 && i === 4) have = [0, 3, 4]; if (k >= 3 && i === 4) have = [0, 1, 2, 3, 4, 5]; o += SV.text(30, y + 22, n, "lbl bd", { style: "font-size:13px" }); for (let p = 0; p < 6; p++) o += SV.rect(130 + p * 52, y, 46, 30, have.includes(p) ? "f3" : "cell", { rx: 4, ...op(have.includes(p) ? 1 : 0.45) }) + SV.text(153 + p * 52, y + 20, "P" + (p + 1), "lbl", { "text-anchor": "middle", style: "font-size:12px" }); });
    if (k >= 1) o += SV.text(480, 40, "tracker: lists the swarm", "lbl bd", { style: "font-size:13px" }) + SV.text(480, 62, "A, B, C, D, E", "sm");
    if (k >= 2) o += SV.text(480, 110, "E asks several peers at once:", "lbl bd", { style: "font-size:13px" }) + SV.text(480, 132, "P1 from A, P4 from C, P5 from C...", "sm");
    if (k >= 3) o += SV.text(480, 170, "E now has the whole file: a new seed", "lbl bd t3", { style: "font-size:13px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 215, label: "A BitTorrent swarm", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "The file is split into six equal <b>pieces</b>. Seed A has them all; B, C and D have some. New peer E has none.", s: { i: 0 } },
    { cap: "E gets the <b>torrent file</b> and contacts the <b>tracker</b>, which tells it who is in the <b>swarm</b>.", s: { i: 1 } },
    { cap: "E downloads <b>different pieces from different peers at the same time</b>. Each piece it receives, it can share.", s: { i: 2 } },
    { cap: "E now has every piece. If it stays connected and shares, it is a <b>seed</b>. No central server held the file.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  const P = ["HTTP/HTTPS", "FTP", "SMTP", "POP3", "IMAP", "BitTorrent"];
  const q = [["Your browser fetches a web page", 0], ["Sending an email from your client to a mail server", 2], ["Downloading emails to one device and removing them from the server", 3], ["Reading the same inbox, in sync, on a phone and a laptop", 4], ["Uploading a folder of files to a web server", 1], ["Downloading a large file in pieces from thousands of other users", 5]];
  let cur = 0, pick = null;
  const paint = () => {
    $$("#wB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const Q = q[cur]; $("#wO").innerHTML = `<p><b>${Q[0]}</b></p><div class="btnrow">` + P.map((p, i) => `<button class="b${pick === i ? " pri" : ""}" data-i="${i}">${p}</button>`).join("") + '</div><div class="verdict">' + (pick === null ? "Choose a protocol." : pick === Q[1] ? "Correct: " + P[Q[1]] + "." : "Not " + P[pick] + ". The best answer is " + P[Q[1]] + ".") + "</div>";
    $$("#wO button").forEach((b) => (b.onclick = () => { pick = +b.dataset.i; paint(); }));
  };
  $("#wB").innerHTML = q.map((x, i) => `<button class="b" data-i="${i}">Situation ${i + 1}</button>`).join("");
  $$("#wB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; pick = null; paint(); })); paint();
})();

/* Lab 2: swarm */
(function () {
  const N = 8, names = ["A (seed)", "B", "C", "D", "E", "F"]; let have, round, seed = 7;
  const rnd = () => { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; };
  const reset = () => { seed = 7; round = 0; have = names.map((_, i) => (i === 0 ? new Set([...Array(N).keys()]) : new Set())); paint("Press Next round."); };
  const paint = (msg) => {
    $("#tS").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Peer</th>' + Array.from({ length: N }, (_, i) => `<th>P${i + 1}</th>`).join("") + "<th>Done?</th></tr>" + names.map((n, i) => "<tr><td>" + n + "</td>" + Array.from({ length: N }, (_, p) => `<td style="${have[i].has(p) ? "background:var(--good-soft)" : ""}">${have[i].has(p) ? "✓" : ""}</td>`).join("") + "<td>" + (have[i].size === N ? "seed" : have[i].size + "/" + N) + "</td></tr>").join("") + "</table></div>";
    $("#tV").textContent = msg;
  };
  $("#tN").onclick = () => {
    round++; const snap = have.map((h) => new Set(h)); let moved = 0;
    names.forEach((_, i) => { if (snap[i].size === N) return; const need = [...Array(N).keys()].filter((p) => !snap[i].has(p)); const options = []; need.forEach((p) => names.forEach((_, j) => { if (j !== i && snap[j].has(p)) options.push(p); })); if (options.length) { have[i].add(options[Math.floor(rnd() * options.length)]); moved++; } });
    const done = have.every((h) => h.size === N);
    paint(done ? "Round " + round + ": every peer has the whole file and can seed it. No server held the file." : "Round " + round + ": " + moved + " pieces were downloaded from other peers. Every piece a peer receives it can pass on.");
  };
  $("#tR").onclick = reset; reset();
})();

btnTable("eB", "eO", [
  ["HTTP / HTTPS", "Web pages / hypertext documents", "Browser requests, server responds; HTTPS is secure", "Sending and receiving web pages"],
  ["FTP", "Files between devices", "Upload and download to a server", "Sending and receiving files"],
  ["SMTP", "Sending email", "Push: client to server, server to server", "Sending / uploading emails"],
  ["POP3", "Receiving email", "Pull: download from the server, normally removed", "Receiving / downloading emails"],
  ["IMAP", "Receiving email", "Pull: any device, server copy kept, in sync", "Access email from any device"],
  ["BitTorrent", "Peer-to-peer file sharing", "Torrent file, tracker, swarm, pieces, seeds", "Sharing files peer to peer"]
], ["Protocol", "Purpose", "Key points", "Exam wording"]);
''' + CLASSIFY("cl1", "Which protocol is described?", ["HTTP(S)", "FTP", "SMTP", "POP3 / IMAP", "BitTorrent"],
  [("Transfers web pages between a server and a browser", 0), ("Sends and receives files over a network", 1), ("Sends email towards its destination", 2), ("Retrieves email from a mail server", 3), ("Peer-to-peer file sharing", 4), ("Hypertext documents", 0), ("Reads email from any device without removing it from the server", 3), ("Uses a tracker, a swarm and pieces of a file", 4)],
  "Web pages: HTTP. Files: FTP. Sending mail: SMTP. Receiving mail: POP3/IMAP. Peer to peer: BitTorrent.") + CLASSIFY("cl2", "Is it a push or a pull protocol?", ["Push", "Pull"],
  [("SMTP", 0), ("POP3", 1), ("IMAP", 1), ("Sending an email to the mail server", 0), ("Retrieving emails from the mail server", 1), ("Delivering mail between mail servers", 0)],
  "SMTP pushes mail out. POP3 and IMAP pull mail in.") + ORDER(
  "Put the journey of an email in order.",
  ["The sender's email client pushes the message to its mail server with SMTP", "That mail server passes it to the recipient's mail server with SMTP", "The recipient's mail server stores it in their mailbox", "The recipient's client retrieves it with POP3 or IMAP"],
  "Client, server, server, mailbox, retrieve.") + MATCH([
  ["HTTP", "Transferring hypertext documents"], ["SMTP", "Sending email towards its destination"], ["IMAP", "Reading email on any device, in sync with the server"], ["BitTorrent", "Peer-to-peer file sharing"], ["FTP", "Sending and receiving files over a network"]]) + CALC([
  {"q": "A file is split into 20 equal pieces. A peer has 12. How many more does it need?", "a": 8, "unit": "", "tol": 0.01, "hint": "20 − 12.", "sol": "<b>8</b>."},
  {"q": "A 600 MB file is split into pieces of 2 MB. How many pieces?", "a": 300, "unit": "", "tol": 0.01, "hint": "600 ÷ 2.", "sol": "<b>300</b>."},
  {"q": "How many protocols are used when an email is sent from one client and read on another using IMAP (count each protocol name once: SMTP, IMAP)?", "a": 2, "unit": "", "tol": 0.01, "hint": "SMTP and IMAP.", "sol": "<b>2</b>."},
  {"q": "A user has 3 devices and uses IMAP. On how many devices can they read the same message?", "a": 3, "unit": "", "tol": 0.01, "hint": "All devices see the server's copy.", "sol": "<b>3</b>."},
  {"q": "A user has 3 devices and uses POP3 with default settings. On how many devices will the message be downloaded?", "a": 1, "unit": "", "tol": 0.01, "hint": "The first to download it; it is then removed.", "sol": "<b>1</b>."}]) + MCQ([
  ("Which protocol sends email?", ["POP3", "IMAP", "SMTP", "FTP"], 2, "SMTP."),
  ("Which protocol lets you read email on any device without removing it from the server?", ["IMAP", "SMTP", "HTTP", "FTP"], 0, "IMAP."),
  ("What does HTTP transfer?", ["Email", "Hypertext documents (web pages)", "Peer-to-peer files", "MAC addresses"], 1, "Web pages."),
  ("In BitTorrent there is...", ["a central server holding the file", "no central server holding the file: users share pieces", "only one source", "no tracker or swarm"], 1, "Peer to peer."),
  ("FTP is used for...", ["sending and receiving files", "reading email", "web browsing only", "routing"], 0, "File transfer."),
  ("A peer with the complete file that keeps sharing it is called...", ["a tracker", "a seed", "a router", "a swarm"], 1, "A seed.")], "qz1") + CARDS([
  ("HTTP(S)", "Web pages / hypertext documents."), ("FTP", "Sending and receiving files."), ("SMTP", "Sending email (push)."), ("POP3", "Receiving email (pull); downloaded."),
  ("IMAP", "Receiving email (pull); any device, in sync."), ("BitTorrent", "Peer-to-peer file sharing."), ("Tracker", "Holds data about the peers in the swarm."), ("Seed", "A peer with the whole file that shares it.")])

build("ac1412", "ac-14-1-2-application-layer-protocols", "Application Layer Protocols: HTTP, FTP, Email and BitTorrent", EYA("14.1.2"),
  "What HTTP, FTP, SMTP, POP3, IMAP and BitTorrent are used for, how email travels, and how BitTorrent shares a file in pieces; animations, a swarm simulation and the real 9618 questions from 2022 to 2025.",
  dict(sub=CBK("Chapter 14 · Communication and internet technologies, section 14.1 Protocols"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
