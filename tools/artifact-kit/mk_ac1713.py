"""A Level CS syllabus 17.1.3: SSL and TLS. Run: python3 tools/artifact-kit/mk_ac1713.py"""
from ak16 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Secure Sockets Layer (SSL)</b> and its successor <b>Transport Layer Security (TLS)</b> are protocols that give <b>security over the internet</b>: they <b>encrypt</b> the data, let the two parties <b>identify and authenticate</b> each other, and keep the communication <b>confidential</b> and unaltered. They are used in <b>client-server</b> communication, for example between a browser and a web server (HTTPS). A connection starts with a <b>handshake</b>: the client asks for the server's <b>digital certificate</b>, checks it and obtains the server's <b>public key</b>, the encryption algorithms are agreed, and <b>symmetric session keys</b> are generated. After that, the <b>record protocol</b> uses those keys to encrypt and send the data safely.</p></div>

  <h2>1 · Purpose of SSL/TLS</h2>
  <ul>
    <li>To provide <b>communications security over the internet</b> or a network: security and privacy.</li>
    <li>To provide <b>encryption</b> of the data sent.</li>
    <li>To let the two parties <b>identify and authenticate</b> each other (client and server).</li>
    <li>To let them communicate with <b>confidentiality and integrity</b>: nobody can read it and nobody can change it unnoticed.</li>
  </ul>
  <p>SSL is the older name. TLS is the modern version, and people often write SSL/TLS for both.</p>

  <h2>2 · How a secure session starts (client-server)</h2>
  <ol>
    <li>An SSL/TLS connection is <b>initiated by an application</b>, which becomes the <b>client</b>. The application that receives the connection is the <b>server</b>.</li>
    <li>Every new session begins with a <b>handshake</b>, as defined by the SSL/TLS protocols.</li>
    <li>The client <b>requests the digital certificate</b> from the server (the server sends it).</li>
    <li>The client <b>verifies the server's certificate</b> with the certificate authority that issued it, and obtains the server's <b>public key</b> from it.</li>
    <li>The <b>encryption algorithms are agreed</b>, and a <b>symmetric session key</b> is generated, with the help of the public key so that it can be shared safely.</li>
    <li>A <b>secure session</b> is established. Data is now encrypted with the fast symmetric session key.</li>
  </ol>
  <p>Notice that both kinds of cryptography are used: the <b>asymmetric</b> keys and the certificate set up trust and share the key, then <b>symmetric</b> encryption carries the data quickly.</p>

  <h2>3 · The two protocols that make up TLS</h2>
  <div class="tw"><table class="t">
    <tr><th>Protocol</th><th>Purpose</th></tr>
    <tr><td><b>Handshake protocol</b></td><td>Establishes a secure and reliable connection between the two devices: the client and server authenticate each other and agree the encryption algorithms and keys.</td></tr>
    <tr><td><b>Record protocol</b></td><td>Provides a secure and reliable way to send and receive data over the network: it encrypts and authenticates the data exchanged between client and server, protecting its integrity and authenticity, and deals with the format of the data transmission.</td></tr>
  </table></div>

  <h2>4 · When to use SSL/TLS</h2>
  <ul>
    <li>When sending <b>authentication data</b>: passwords and session cookies.</li>
    <li>When transmitting data that must be <b>protected from modification</b> on its way to or from a server, for example a user's input or results from the server.</li>
    <li>When transmitting data classified as <b>non-public</b>: card details, personal data, private messages, online banking and shopping.</li>
  </ul>
  <p>It is not needed for public information that anyone can read and nobody gains by changing, such as a public timetable page (although many sites use it anyway).</p>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Writing that SSL/TLS "stops hackers". Name the functions: encryption, authentication, confidentiality and integrity.</li>
    <li>Leaving out the digital certificate and the public key in the handshake.</li>
    <li>Saying the session uses the asymmetric keys for all the data. The agreed keys for the session are symmetric.</li>
    <li>Describing the two protocols without names: handshake protocol and record protocol, each with its own purpose.</li>
    <li>Giving examples that are too vague, such as "the internet". Say what is sent: passwords, payment details, personal data.</li>
  </ul>
'''

watch = '''
  <h2>1 · The handshake</h2>
  <p>Press Play. The client starts the conversation and checks the server before any data is sent.</p>
  <div id="stA"></div>
  <h2>2 · After the handshake: the record protocol</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · What can an eavesdropper see?</h2>
  <p>Type a message that a browser sends. Choose without or with SSL/TLS.</p>
  <div class="card"><div class="btnrow" id="vB"></div><input id="vI" type="text" value="password=Tiger99" style="width:100%;font:inherit;padding:8px"><div id="vO"></div></div>

  <h2>Lab 2 · Should SSL/TLS be used?</h2>
  <div class="card"><div id="sB" class="btnrow"></div><div id="sO"></div></div>
'''

practise = '''
  <h2>1 · Handshake or record protocol?</h2><div id="cl1" class="card"></div>
  <h2>2 · Is SSL/TLS appropriate?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Put the handshake steps in order</h2><div id="o1" class="card"></div>
  <h2>5 · Counting</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The padlock and https://", "When a web address starts with https the browser and the site have used TLS. The padlock means the site's certificate was checked and the data is encrypted.", "SSL/TLS is used between browser (client) and web server.") +
rw("Online banking and shopping", "Card numbers and passwords are sent over a TLS connection so that a person on the same Wi-Fi cannot read or change them.", "non-public data needs protecting.") +
rw("Logging in", "The password is sent inside the encrypted session. A session cookie that proves you are logged in is protected in the same way.", "authentication data such as passwords and session cookies.") +
rw("Secure email", "Mail servers use TLS between each other and your mail app, so messages are not readable on the way.", "TLS is used by many protocols, not just the web.") +
rw("A warning page about a certificate", "If the server's certificate cannot be verified, the browser warns you because it cannot be sure it is talking to the real site.", "the client verifies the server's certificate.")
)

where = [
  ("O/N 2021", "31, 32", "8", "2 + 4", "Purpose of SSL/TLS; how SSL/TLS is used when client-server communication is initiated"),
  ("M/J 2025", "31", "9", "2 + 2", "Two functions of SSL/TLS; two situations where it is appropriate"),
  ("M/J 2025", "32", "10", "4", "The two main protocols that form TLS and the purpose of each"),
  ("M/J 2025", "33", "7", "4", "How SSL/TLS is used when client-server communication is initiated")]

past = '''  <p class="note">SSL/TLS is asked in Paper 3 in Oct/Nov 2021 and in all three papers of May/June 2025, each with a different angle. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("w21", "31/32", "Q8"), "2 + 4 marks", "Describe / Explain",
  "(a) Describe the purpose of the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols. (b) Explain how SSL/TLS protocols are used when a client-server communication is initiated.",
  "(b) handshake, certificate, verify, public key, algorithms, session keys.",
  "<p><b>(a)</b> Any two: " + mks(["The SSL and TLS protocols provide communications security over the internet or a network", "they provide encryption", "They enable two parties to identify and authenticate each other", "and communicate with confidentiality and integrity"]) + "</p><p><b>(b)</b> Any four: " + mks(["An SSL/TLS connection is initiated by an application, which becomes the client", "The application which receives the connection becomes the server", "Every new session begins with a handshake (as defined by the protocols)", "The client requests the digital certificate from the server, or the server sends it", "The client verifies the server's digital certificate and obtains the server's public key", "The encryption algorithms are agreed", "The symmetric session keys are generated or defined"]) + "</p>", "Describing the data being encrypted without the handshake. The question is about how the session is set up.") + peq(SRC("s25", "31", "Q9"), "2 + 2 marks", "State / Give",
  "Secure Socket Layer (SSL) and Transport Layer Security (TLS) are two protocols. (a) State two functions of SSL/TLS. (b) Give two examples of situations where the use of SSL/TLS would be appropriate.",
  "(b) passwords, protected or non-public data.",
  "<p><b>(a)</b> Any two: " + mks(["Ensure security or privacy when using the internet", "Data encryption", "Identification or authentication of client and server"]) + "</p><p><b>(b)</b> Any two: " + mks(["When transmitting authentication data, for example passwords or session cookies", "When transmitting data that must be protected from modification on its way to or from a server, for example a user's input or results from the server", "When transmitting data classified as non-public"], "a") + "</p>", None) + peq(SRC("s25", "32", "Q10"), "4 marks", "Identify / State",
  "Identify the two main protocols that form Transport Layer Security (TLS) and state the purpose of each.",
  "Each: a name (1) and a purpose (1).",
  "<p>" + mks(["Handshake protocol", "To establish a secure and reliable connection between two devices, systems or networks; or it permits the web server and client to authenticate each other and use encryption algorithms"]) + "<br>" + mks(["Record protocol", "Provides a secure and reliable way to send and receive data over a network; encrypts and authenticates the data exchanged between a client and a server, ensuring its integrity and authenticity during transmission; deals with the format of data transmission"], "a") + "</p>", "Naming 'SSL' and 'TLS' as the two protocols. The two protocols inside TLS are the handshake and record protocols.") + peq(SRC("s25", "33", "Q7"), "4 marks", "Explain",
  "Secure Socket Layer (SSL) and Transport Layer Security (TLS) are two protocols. Explain how SSL/TLS is used when client-server communication is initiated.",
  "Handshake first, then certificate, verify, public key, algorithms, session established.",
  "<p>Any four: " + mks(["An SSL/TLS connection is initiated by an application or client", "Every new session begins with a handshake as defined by the SSL/TLS protocols", "The client requests the digital certificate from the server, or the server sends it to the client", "The client verifies the server's digital certificate", "and obtains the server's public key", "The encryption algorithms are agreed, or the symmetric session keys are generated or defined", "A secure session is established between client and server"]) + "</p>", None)

review = req("2 marks", "State", "State two things the client does with the server's digital certificate during the handshake.", "Verify and use.", "<p>" + mks(["It verifies the certificate", "It obtains the server's public key from it"]) + "</p>", None) + req("3 marks", "Explain", "Explain why the session keys used after the handshake are symmetric.", "Think about speed.", "<p>" + mks(["Symmetric encryption is simple and fast", "Asymmetric encryption is slower and more complex, so it is used to set up and share the key", "The data is then encrypted quickly with the shared session key"]) + "</p>", None) + req("2 marks", "Give", "Give two situations where a user would want SSL/TLS to be used.", "Authentication or non-public data.", "<p>" + mks(["Logging in (sending a password)", "Entering card details to pay online"]) + "</p>", None) + req("2 marks", "Describe", "Describe what the record protocol does after the handshake.", "Secure data.", "<p>" + mks(["It encrypts the data sent between client and server", "and authenticates it so its integrity and authenticity are protected"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between SSL and TLS.", "Old and new.", "<p>" + mks(["SSL is the earlier protocol", "TLS is its successor and is the one used today (both give security over a network)"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on SSL and TLS (Paper 3), 2021 and 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Functions: encrypt, authenticate, confidential, integrity.", "Learn all four."),
  ("Handshake first.", "Client, certificate, verify, public key, algorithms, session keys."),
  ("Client and server.", "The application that starts the connection is the client."),
  ("Two protocols.", "Handshake protocol and record protocol."),
  ("Symmetric session keys.", "Fast encryption for the data after the handshake."),
  ("Examples: passwords, cookies, non-public data.", "Be specific."),
], [
  ("SSL/TLS", "Protocols that give secure, authenticated, encrypted communication."),
  ("the handshake", "The start of a session, where the certificate is checked and keys agreed."),
  ("a session key", "A symmetric key generated for one secure session."),
  ("the record protocol", "Encrypts and authenticates the data sent after the handshake."),
], [("State", "Short answer."), ("Describe", "Several points."), ("Explain", "Give the steps in order with reasons."), ("Identify", "Name them.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const M = [["Client", "ClientHello: I want a secure connection"], ["Server", "Sends its digital certificate"], ["Client", "Verifies the certificate; gets the server's public key"], ["Client + Server", "Agree the encryption algorithms"], ["Client + Server", "Generate shared symmetric session keys"], ["Both", "Secure session established"]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 14, 150, 40, "cell", { rx: 8 }) + SV.text(95, 40, "Client", "lbl bd", { "text-anchor": "middle" }) + SV.rect(450, 14, 150, 40, "cell", { rx: 8 }) + SV.text(525, 40, "Server", "lbl bd", { "text-anchor": "middle" }) + SV.path("M95,54 V320", "ax", { style: "stroke-dasharray:4 5;opacity:.5" }) + SV.path("M525,54 V320", "ax", { style: "stroke-dasharray:4 5;opacity:.5" });
    M.slice(0, k).forEach(([who, t], i) => { const y = 84 + i * 48, cur = i === k - 1; const toServer = i === 0, toClient = i === 1; o += (toServer ? SV.path("M95," + y + " H450", "ax", {}) + SV.arrowHead(450, y, "r", "arr") : toClient ? SV.path("M525," + y + " H100", "ax", {}) + SV.arrowHead(95, y, "l", "arr") : "") + SV.text(310, y - 8, t, "lbl" + (cur ? " bd" : ""), { "text-anchor": "middle", style: "font-size:12.5px" }); });
    return o; };
  Lib.stepper($("#stA"), { w: 620, h: 340, label: "TLS handshake", base: { i: 0 }, draw, tween: 120, dwell: 2800, steps: [{ cap: "Before any data is sent, the client and server carry out a <b>handshake</b>.", s: { i: 0 } }, { cap: "The client (the application that starts the connection) asks for a secure session.", s: { i: 1 } }, { cap: "The server sends its <b>digital certificate</b>.", s: { i: 2 } }, { cap: "The client <b>verifies the certificate</b> and takes the server's <b>public key</b> from it.", s: { i: 3 } }, { cap: "The two sides <b>agree the encryption algorithms</b>.", s: { i: 4 } }, { cap: "<b>Symmetric session keys</b> are generated, with the public key making it safe to share them.", s: { i: 5 } }, { cap: "A <b>secure session</b> is established.", s: { i: 6 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 30, 130, 50, "cell", { rx: 8 }) + SV.text(85, 60, "Client", "lbl bd", { "text-anchor": "middle" }) + SV.rect(470, 30, 130, 50, "cell", { rx: 8 }) + SV.text(535, 60, "Server", "lbl bd", { "text-anchor": "middle" });
    o += SV.rect(150, 40, 320, 30, "f3", { rx: 15, ...op(0.35) }) + SV.text(310, 28, "secure tunnel (session key)", "sm", { "text-anchor": "middle" });
    if (k >= 1) o += SV.text(85, 110, "card=4242...", "lbl", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:12px" });
    if (k >= 2) o += SV.rect(250, 44, 120, 22, "f2", { rx: 4 }) + SV.text(310, 60, "x7#Qa9!kP2", "lbl", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:12px" });
    if (k >= 3) o += SV.text(535, 110, "card=4242...", "lbl", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:12px" }) + SV.text(310, 140, "an eavesdropper sees only x7#Qa9!kP2", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 620, h: 160, label: "Record protocol", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: [{ cap: "The handshake is complete. The client wants to send a card number.", s: { i: 0 } }, { cap: "The <b>record protocol</b> takes the data...", s: { i: 1 } }, { cap: "...encrypts and authenticates it with the session key, so it is protected as it travels.", s: { i: 2 } }, { cap: "The server decrypts it. Anyone who intercepts the data sees only cipher text, and any change would be noticed.", s: { i: 3 } }] });
})();

(function () {
  let tls = false; const inp = $("#vI"), b = $("#vB");
  const enc = (s) => { let h = 7; return [...s].map((c, i) => { h = (h * 31 + c.charCodeAt(0) + i * 17) % 4093; return h.toString(16).padStart(3, "0"); }).join(""); };
  const paint = () => { $("#vO").innerHTML = `<div class="tw"><table class="t mono"><tr><th>What the eavesdropper sees</th></tr><tr><td style="word-break:break-all">${tls ? enc(inp.value) : inp.value.replace(/</g, "&lt;")}</td></tr></table></div><div class="verdict">${tls ? "With SSL/TLS the data is <b>encrypted</b>: it is meaningless without the session key, and the server was authenticated first." : "Without SSL/TLS the data is sent as <b>plain text</b>: anyone on the route can read it, or change it."}</div>`; b.querySelectorAll("button").forEach((x) => (x.className = (x.dataset.k === "t") === tls ? "on" : "")); };
  [["p", "Without SSL/TLS"], ["t", "With SSL/TLS"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { tls = k === "t"; paint(); }; b.appendChild(x); });
  inp.oninput = paint; paint();
})();
btnTable("sB", "sO", [
  ["Sending a password to log in", "Yes", "Authentication data must be protected"],
  ["Entering card details to pay", "Yes", "Non-public data that must not be read or changed"],
  ["Sending a session cookie", "Yes", "It proves who you are; stealing it would let someone pretend to be you"],
  ["Reading a public news headline page", "Not essential", "Public data; nothing secret is sent (but TLS is still common)"],
  ["Sending results from a server to a user's input", "Yes", "Must be protected from modification on the way"],
  ["Filling in a private medical form", "Yes", "Non-public personal data"]
], ["Situation", "Use SSL/TLS?", "Reason"]);
''' + CLASSIFY("cl1", "Which protocol of TLS?", ["Handshake protocol", "Record protocol"],
  [("Client and server authenticate each other", 0), ("Encrypts the data sent after the session starts", 1), ("Agrees the encryption algorithms", 0), ("Protects the integrity of the data in transit", 1), ("Establishes a secure connection between two devices", 0), ("Deals with the format of data transmission", 1)],
  "Handshake sets up; record protects the data.") + CLASSIFY("cl2", "Is SSL/TLS appropriate?", ["Yes", "Not needed"],
  [("Sending a password", 0), ("Reading a public page with nothing to protect", 1), ("Online payment", 0), ("Sending a session cookie", 0), ("Posting non-public health data", 0), ("Looking at a public weather map", 1)],
  "Use it for authentication data and non-public or must-not-be-changed data.") + MATCH([
  ["Handshake", "The start of a session: certificate checked, keys agreed"], ["Digital certificate", "Sent by the server to prove its identity and give its public key"], ["Session key", "A symmetric key used for one secure session"], ["Record protocol", "Encrypts and authenticates the data in the session"], ["Client", "The application that starts the connection"]]) + ORDER(
  "Put the handshake steps in order.",
  ["The client starts the connection", "The server sends its digital certificate", "The client verifies the certificate and obtains the public key", "The encryption algorithms are agreed and session keys generated", "A secure session is established"],
  "Start, certificate, verify, agree, secure.") + CALC([
  {"q": "How many main protocols make up TLS?", "a": 2, "unit": "", "tol": 0.01, "hint": "Handshake and record.", "sol": "<b>2</b>."},
  {"q": "How many functions of SSL/TLS were listed in the purpose (encryption, authentication, confidentiality, integrity)?", "a": 4, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>4</b>."},
  {"q": "A page uses https. Does the data travel as plain text? Enter 0 for no, 1 for yes.", "a": 0, "unit": "", "tol": 0.01, "hint": "It is encrypted.", "sol": "<b>0</b>."},
  {"q": "How many keys does the server hold in the handshake that the client needs from its certificate (the public key)?", "a": 1, "unit": "", "tol": 0.01, "hint": "The public key.", "sol": "<b>1</b>."},
  {"q": "The session keys are symmetric. How many keys does each side use for the session?", "a": 1, "unit": "", "tol": 0.01, "hint": "One shared key.", "sol": "<b>1</b>."}]) + MCQ([
  ("SSL/TLS provides:", ["Only speed", "Encryption and authentication", "Only storage", "Printing"], 1, "Encryption and authentication."),
  ("The client:", ["Starts the connection", "Is always the server", "Issues certificates", "Has no keys"], 0, "It initiates it."),
  ("The handshake includes:", ["The server sending its certificate", "Deleting the data", "A virus scan", "Compression only"], 0, "Certificate."),
  ("The session keys are:", ["Asymmetric", "Symmetric", "Quantum", "None"], 1, "Symmetric."),
  ("Which would use SSL/TLS?", ["Sending a password", "Reading public information only", "Nothing", "Turning off the screen"], 0, "Passwords."),
  ("The record protocol:", ["Sets the session up", "Encrypts and authenticates the data", "Issues certificates", "Compresses files"], 1, "Protects the data.")], "qz1") + CARDS([
  ("SSL/TLS", "Secure, authenticated, encrypted client-server communication."), ("Handshake", "Certificate, verify, algorithms, session keys."), ("Record protocol", "Encrypts and authenticates the session data."), ("Session key", "Symmetric key for one session."),
  ("Client", "Starts the connection."), ("Server", "Receives it; sends its certificate."), ("Use when", "Passwords, cookies, non-public data."), ("Provides", "Encryption, authentication, confidentiality, integrity.")])

build("ac1713", "ac-17-1-3-ssl-tls", "SSL and TLS", EYA("17.1.3"),
  "The purpose of SSL and TLS, the handshake between client and server, the handshake and record protocols, and when to use them; animations, labs and the real Paper 3 questions from 2021 and 2025.",
  dict(sub=CBK("Chapter 17 · Security, section 17.1 Encryption, encryption protocols and digital certificates"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
