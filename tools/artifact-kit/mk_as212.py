"""AS CS syllabus 2.1.2: cloud computing and transmission media (wired and wireless). Run: python3 tools/artifact-kit/mk_as212.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Cloud computing</b> means accessing services, software or files on a <b>remote server</b> over the internet instead of on your own computer. A <b>public cloud</b> is run by a third party and open to anyone with the right credentials, while a <b>private cloud</b> is a dedicated system available only to one organisation. The benefits are access from anywhere, no hardware to buy, easy sharing and built-in backup; the drawbacks are the need for an internet connection and reliance on someone else for security and backup. Data is carried by <b>transmission media</b>: <b>copper cable</b> (electrical signals), <b>fibre-optic cable</b> (pulses of light), and <b>wireless</b> media such as <b>radio waves</b> (Wi-Fi), <b>microwaves</b> and <b>satellites</b>. Wired links are usually faster, more reliable and more secure; wireless links are more mobile and cheaper to set up.</p></div>

  <h2>1 · Cloud computing</h2>
  <p>Cloud computing is <b>accessing a service, files or software on a remote server</b> rather than on a local computer. The user needs only a device and an internet connection.</p>
  <div class="tw"><table class="t">
    <tr><th></th><th>Public cloud</th><th>Private cloud</th></tr>
    <tr><td><b>Meaning</b></td><td>Computing services offered by a third-party provider over the public internet, open to anyone with the right equipment and credentials</td><td>A dedicated, bespoke system, offered over the internet or an internal network, available only to selected users or one organisation</td></tr>
    <tr><td><b>Control</b></td><td>Provider controls security and backup</td><td>Organisation has greater control over security, privacy and backup</td></tr>
    <tr><td><b>Cost</b></td><td>Shared infrastructure, cheaper</td><td>Dedicated, more expensive</td></tr>
    <tr><td><b>Example</b></td><td>Online file storage, web email, online courses</td><td>A company's own storage for its employees' work</td></tr>
  </table></div>
  <h3>Benefits and drawbacks</h3>
  <ul>
    <li><b>Benefits</b>: data can be accessed from <b>any computer with an internet connection</b>; <b>no need to buy</b> or maintain specific hardware or software; cloud services usually include <b>backup and recovery</b>; documents are <b>easy to share</b> and several people can work on one; storage can be <b>increased</b> quickly; free storage may be offered.</li>
    <li><b>Drawbacks</b>: it <b>cannot be accessed without an internet connection</b>; you <b>depend on a third party</b> for security and backup, so you have less control; uploading and downloading large files can take a long time; downtime at the provider stops access; limited free storage may mean paying more in the long term; compatibility problems if you want to move your data.</li>
  </ul>
  <p>Compared with a server on the company's own LAN, a public cloud brings a possible <b>loss of control</b>, <b>reliance on an external agency</b> and <b>recurring costs</b>, while a LAN server has a one-off cost and keeps working without the internet.</p>

  <h2>2 · Transmission media</h2>
  <div class="tw"><table class="t">
    <tr><th>Medium</th><th>How it carries data</th><th>Characteristics</th></tr>
    <tr><td><b>Copper cable</b> (twisted pair, coaxial)</td><td>Electrical signals</td><td>Cheap and easy to install; signal weakens over distance (repeaters needed); prone to interference; lower bandwidth than fibre; can be tapped</td></tr>
    <tr><td><b>Fibre-optic cable</b></td><td>Pulses of light through glass or plastic strands</td><td>Very high bandwidth and speed; little interference; works over much longer distances before a repeater; hard to hack into; more expensive and more fragile</td></tr>
    <tr><td><b>Radio waves</b> (including Wi-Fi)</td><td>Radio signals in all directions from an antenna</td><td>No cables, devices can move; shared channel and interference; walls reduce range; less secure unless encrypted</td></tr>
    <tr><td><b>Microwaves</b></td><td>High-frequency electromagnetic waves between dishes or towers (cell phone network)</td><td>High bandwidth over long distances; needs line of sight between towers; affected by weather and obstructions</td></tr>
    <tr><td><b>Satellite</b></td><td>Microwave signals to and from a satellite in orbit</td><td>Covers remote and large areas; long delay (latency) because the signal travels far; expensive; affected by weather</td></tr>
  </table></div>
  <h3>The cell phone network</h3>
  <p>The land is split into <b>cells</b>, designed for maximum line of sight. Each cell has a <b>tower with an antenna</b> that receives and transmits data. Data is sent wirelessly between the phone and the tower using low-power radio signals, and many devices can talk to the same tower at the same time.</p>

  <h2>3 · Wired and wireless networks compared</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Wired</th><th>Wireless</th></tr>
    <tr><td><b>Speed</b></td><td>Faster connection, higher bandwidth, less latency</td><td>Usually slower</td></tr>
    <tr><td><b>Reliability</b></td><td>More stable, less affected by distance, walls and interference</td><td>Signal degrades, interference possible</td></tr>
    <tr><td><b>Security</b></td><td>More secure: needs a physical connection</td><td>Can be less secure: anyone in range could try to connect</td></tr>
    <tr><td><b>Mobility</b></td><td>Fixed to the socket</td><td>Free movement; no cable; easy to add devices</td></tr>
    <tr><td><b>Setup</b></td><td>Cabling and expertise needed</td><td>Less cabling; cheaper initial setup</td></tr>
  </table></div>
  <p>To justify a choice, tie it to the situation: a gamer who downloads large files and wants low delay suits wired; a person who moves between rooms with a phone suits wireless.</p>

  <h2>4 · Common ways to lose marks</h2>
  <ul>
    <li>Describing a public cloud as "free". It is offered by a third party to anyone; some storage may be free.</li>
    <li>Writing "cloud is more secure" or "less secure" with no reason. Say who controls security and backup.</li>
    <li>Fibre against copper: write what each carries (light against electrical signals) and then a difference such as bandwidth, distance or interference.</li>
    <li>Saying wireless is "worse". Give the specific drawback: slower, interference, signal degrades, less secure.</li>
    <li>Forgetting the internet requirement as the main drawback of cloud computing.</li>
  </ul>
'''

watch = '''
  <h2>1 · Storing files in the cloud</h2>
  <p>Press Play. Files are on a remote server, not on your device.</p>
  <div id="stA"></div>
  <h2>2 · A signal travelling down fibre and copper</h2>
  <div id="stB"></div>
  <h2>3 · The cell phone network</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Is the internet working?</h2>
  <p>Switch the internet on and off and see what you can reach with cloud storage and with a LAN server.</p>
  <div class="card"><div class="btnrow" id="iB"></div><div id="iO"></div></div>
  <h2>Lab 2 · Choosing a transmission medium</h2>
  <p>Choose the distance and the need. The tool suggests suitable media.</p>
  <div class="card"><div id="dS"></div><div id="dB" class="btnrow"></div><div id="dO"></div></div>
  <h2>Lab 3 · Wired or wireless?</h2>
  <div class="card"><div id="wB" class="btnrow"></div><div id="wO"></div></div>
'''

_pr, _prjs = PR(["Public or private cloud?", "Benefit or drawback of cloud computing?", "Match the medium to its description", "Put the cell network steps in order", "Working out", "Multiple choice"],
  ("Is it a public cloud or a private cloud?", ["Public cloud", "Private cloud"], [("Run by a third-party provider and open to anyone with credentials", 0), ("Only available to one organisation's staff", 1), ("Gives the company greater control over backup", 1), ("Infrastructure is shared with other customers", 0), ("A dedicated, bespoke system", 1), ("Online storage anyone can sign up to", 0)], "Public is open and shared; private is dedicated."),
  ("Is it a benefit or a drawback of cloud computing?", ["Benefit", "Drawback"], [("Access from any computer with internet", 0), ("Cannot be used without an internet connection", 1), ("No need to buy extra hardware", 0), ("Reliance on a third party for backup", 1), ("Easy to share documents", 0), ("Uploading a large file can take a long time", 1)], "Benefits: access, no hardware, sharing. Drawbacks: internet, third party."),
  [["Copper cable", "Carries data as electrical signals"], ["Fibre-optic cable", "Carries data as pulses of light"], ["Microwaves", "Line-of-sight signals between towers or dishes"], ["Satellite", "Covers remote areas but has a long delay"], ["Radio waves", "Used for Wi-Fi: no cables, devices can move"]],
  ("Put the steps of cell phone data transfer in order.", ["The phone sends low-power radio signals to the nearest tower", "The tower's antenna receives the data", "The data passes on through the network to its destination", "The reply comes back to the tower", "The tower transmits it to the phone"], "Phone, tower, network, tower, phone."),
  [{"q": "A file is 400 MB and the upload speed is 20 MB per minute. How many minutes does it take?", "a": 20, "unit": "min", "tol": 0.1, "hint": "400 ÷ 20.", "sol": "<b>20</b> minutes."}, {"q": "How many types of cloud (public, private) must you be able to define?", "a": 2, "unit": "", "tol": 0.01, "hint": "Public and private.", "sol": "<b>2</b>."}, {"q": "A company pays $5 per user per month for cloud storage for 40 users. What is the cost per year ($)?", "a": 2400, "unit": "$", "tol": 0.5, "hint": "5 × 40 × 12.", "sol": "<b>$2400</b>."}, {"q": "A fibre cable carries data at 10 times the rate of a copper cable at 100 Mbps. What is the fibre rate in Mbps?", "a": 1000, "unit": "Mbps", "tol": 0.5, "hint": "100 × 10.", "sol": "<b>1000</b> Mbps."}, {"q": "How many transmission media does the syllabus list (copper, fibre-optic, radio waves, microwaves, satellite)?", "a": 5, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>5</b>."}],
  [("Fibre-optic cable carries data as:", ["Electrical signals", "Pulses of light", "Sound", "Heat"], 1, "Light pulses."), ("A drawback of cloud storage is:", ["Needs an internet connection", "Access from anywhere", "Easy sharing", "No hardware to buy"], 0, "Needs the internet."), ("A private cloud is:", ["Open to everyone", "Dedicated to one organisation", "Free for all", "A wireless network"], 1, "Dedicated."), ("Which is most affected by interference?", ["Fibre-optic", "Copper cable", "Neither", "Both equally"], 1, "Copper."), ("A satellite link has a long:", ["Cable", "Delay (latency)", "Battery", "Keyboard"], 1, "Delay."), ("Compared with wired, wireless is usually:", ["More mobile", "Always faster", "Always more secure", "Cheaper per bit always"], 0, "More mobile.")],
  [("Cloud computing", "Accessing services or files on a remote server."), ("Public cloud", "Third party; open to anyone with credentials."), ("Private cloud", "Dedicated to one organisation."), ("Copper", "Electrical signals; interference; repeaters."), ("Fibre", "Light; fast; long distance; secure; costly."), ("Radio", "Wi-Fi; mobile; interference."), ("Microwave", "Line of sight; towers."), ("Satellite", "Remote areas; delay; expensive.")])

real = RWNOTE + (
rw("Google Drive and OneDrive", "Your files are on a provider's servers. You can open them on any device with an internet connection, but not when you are offline unless you saved a copy.", "public cloud storage.") +
rw("A bank's own data centre", "A bank may run a private cloud so that only its staff can use the system and it controls the security.", "a private cloud is dedicated to one organisation.") +
rw("Fibre broadband", "Light pulses in glass strands give very fast, stable internet with little interference.", "fibre has a high bandwidth.") +
rw("Wi-Fi in a cafe", "You can move around with a laptop but the speed drops with distance and walls, and a public hotspot can be less secure.", "radio waves: mobility against interference.") +
rw("Satellite internet in a remote village", "No cable reaches the village, so a dish links to a satellite. It works anywhere but there is a noticeable delay.", "satellites cover remote areas but have a long delay.")
)

where = [
  ("M/J 2021", "11, 13", "4(c)(ii)", "3", "Whether to connect to the router by wired or wireless for films and games, with justification"),
  ("M/J 2022", "12", "9(b)", "3", "Three differences between fibre-optic and copper cables"),
  ("M/J 2022", "13", "8", "1 + 2 + 3", "Define cloud computing; public and private cloud; two benefits and a drawback"),
  ("O/N 2023", "11", "2(c)", "2", "Two drawbacks of students storing files on the public cloud"),
  ("O/N 2023", "13", "3(a)(i), (ii)", "2 + 4", "Why a company uses a public cloud; two disadvantages compared with a LAN server"),
  ("M/J 2024", "13", "5(a)", "1 + 3", "Define a private cloud; benefits over a public cloud"),
  ("O/N 2024", "13", "9(b)", "4", "Identify and describe two other transmission media for a WAN"),
  ("M/J 2025", "12", "6(b)", "4", "How data is transmitted using the cell phone network"),
  ("O/N 2025", "12", "8(a)", "2 + 2", "Two benefits and two drawbacks of cloud computing"),
  ("O/N 2025", "13", "4(a), (b)", "3 + 1", "Advantages and a drawback of a wireless network compared with wired")]

past = '''  <p class="note">Cloud computing and transmission media are examined in Paper 1 in most series. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s22", "13", "Q8"), "1 + 2 + 3 marks", "Define / State / Give",
  "A company uses cloud computing. (a) Define cloud computing. (b) State what is meant by a public cloud and a private cloud. (c) Give two benefits and one drawback of using cloud computing.",
  "Remote server; public open to anyone; private only for selected users.",
  "<p><b>(a)</b> " + mks(["Accessing a service, files or software on a remote server"]) + "</p><p><b>(b)</b> " + mks(["Public: computing services offered by a third-party provider over the public internet, available to anyone with the appropriate equipment or credentials", "Private: computing services offered over the internet or a private internal network, only available to select users, a dedicated system accessible only to the organisation"], "a") + "</p><p><b>(c)</b> Two benefits: " + mks(["Can be accessed anywhere with internet access", "No need to install security, or security might be better", "No need to perform backups", "No need to buy specific software or hardware", "Easy to share documents", "Multiple people can work on the same document"]) + " One drawback: " + mks(["Cannot access it without internet access", "Reliant on someone else for backup or security", "Cannot access it if the server goes down"], "n") + "</p>", "Defining it as 'storing data on the internet'. It is accessing services or files on a remote server.") + peq(SRC("w23", "13", "Q3(a)"), "2 + 4 marks", "Explain / Describe",
  "A company sells online Computer Science courses to students in different countries. The courses are stored on a public cloud. (i) Explain why the company uses a public cloud to store these courses. (ii) Describe two disadvantages of storing data on a public cloud compared to storing data on a server in a LAN.",
  "(i) available to anyone, on the internet, shared cost. (ii) control, reliance on third party, internet needed, recurring costs.",
  "<p><b>(i)</b> Any two: " + mks(["Courses must be available to anyone who wishes to follow them", "Courses must be available on the internet", "The company is willing to share infrastructure with other companies", "which is more economic for the company"]) + "</p><p><b>(ii)</b> Two disadvantages, a mark for each plus a mark for its expansion: " + mks(["Possible loss of control", "because the data is stored on someone else's infrastructure; reliance on an external agency for backups and security"]) + " " + mks(["Requires a reliable internet connection", "to access the remote data, more likely with a LAN"], "a") + " (or increased recurring costs, as the provider's charges must be paid and a LAN costs once)</p>", None) + peq(SRC("s24", "13", "Q5(a)"), "1 + 3 marks", "Define / Describe",
  "A multimedia design company has private cloud storage for its employees to store their work. (i) Define the term private cloud. (ii) Describe the benefits to the company of using private cloud storage instead of public cloud storage.",
  "Dedicated; control over security and backup.",
  "<p><b>(i)</b> " + mks(["Dedicated or bespoke services and storage on a remote server only available to the company"]) + "</p><p><b>(ii)</b> Any three: " + mks(["Not reliant on a third party", "which gives greater control over security and privacy", "and greater control over backup", "Storage can be tailored or scaled to the company's requirements, for example the amount of storage or facilitating sharing of files"], "a") + "</p>", None) + peq(SRC("w25", "12", "Q8(a)"), "2 + 2 marks", "Give",
  "A restaurant accesses software and stores data using cloud computing. (i) Give two benefits of storing data using cloud computing. (ii) Give two drawbacks of using cloud computing.",
  "Access anywhere, no devices, backup, sharing; internet needed, third-party, slow transfers.",
  "<p><b>(i)</b> Any two: " + mks(["Cloud storage can be free of charge for a limited amount", "No need for personal storage devices", "The data can be accessed from any computer with an internet connection", "Cloud services usually include backup and recovery", "Easier to share data or collaborate", "Storage capacity can be increased quickly and easily"]) + "</p><p><b>(ii)</b> Any two: " + mks(["It can only be accessed with an internet connection", "There may be no backups, or reliance on a third party for backups", "Uploading or downloading data could take a long time", "Problems at the cloud company such as downtime", "Compatibility issues if the data is moved", "Limited storage without paying extra, more expensive in the long term", "Possible security issues"], "a") + "</p>", None) + peq(SRC("w23", "11", "Q2(c)"), "2 marks", "Identify",
  "The students can save their school files on a public cloud. Identify two drawbacks of the students storing their files on the public cloud.",
  "Internet, space, third-party control.",
  "<p>Any two: " + mks(["The students cannot access their files without a reliable internet connection", "The amount of space for no payment may be limited, so students will have to purchase more space if needed", "The students do not have control over backup or security of their work; they depend on a third party"]) + "</p>", None) + peq(SRC("s22", "12", "Q9(b)"), "3 marks", "Describe",
  "Describe three differences between fibre-optic cables and copper cables.",
  "What it carries, speed, interference, distance, security, damage.",
  "<p>Any three: " + mks(["Fibre-optic data is transmitted using light; copper cable uses electrical signals", "Fibre has higher bandwidth, or higher transmission rates, than copper", "Fibre has a smaller risk of interference (noise) than copper", "Fibre can be used over longer distances before repeaters are needed", "Fibre is much more difficult to hack into than copper", "Fibre is more prone to damage than copper"]) + "</p>", "Writing 'fibre is faster' alone. Pair each point with what the copper cable does.") + peq(SRC("w24", "13", "Q9(b)"), "4 marks", "Identify / Describe",
  "Copper cable can be used to transmit data in a network. Complete the table by identifying and describing two other transmission media that can be used to transfer data in the WAN (name and description for each).",
  "Name each medium and say how it carries data.",
  "<p>A mark for a correct medium and a mark for its matching description, twice: " + mks(["Fibre optic", "Transmits data as pulses of light"]) + " " + mks(["Radio waves or microwaves", "Transmit electromagnetic waves on different frequencies"], "a") + " (satellite is also a valid medium)</p>", None) + peq(SRC("s25", "12", "Q6(b)"), "4 marks", "Explain",
  "The smartphones use the cell phone network to connect to the WAN. Explain how data is transmitted using the cell phone network.",
  "Cells, towers with antennae, radio signals, many devices.",
  "<p>Any four: " + mks(["The land is split into cells designed for maximum line of sight", "Each cell has a tower with an antenna which receives and transmits data", "Data is transmitted between the tower and the phone", "Data transmission is wireless using low-power radio signals or frequencies", "Multiple devices can communicate simultaneously with the same tower"]) + "</p>", None) + peq(SRC("w25", "13", "Q4(a)(b)"), "3 + 1 marks", "Give",
  "A network engineer is setting up a LAN in an office. The network uses both wired and wireless connectivity. (a) Give three advantages of a wireless network compared to a wired network. (b) Give one drawback of using a wireless network.",
  "Mobility, no cabling, adding devices, different devices.",
  "<p><b>(a)</b> Any three: " + mks(["Devices can be more mobile as no physical connection is required", "No cabling is needed, so it is easier to set up", "It is easier to add additional devices", "Multiple different device types can be connected"]) + "</p><p><b>(b)</b> One: " + mks(["Can be less secure", "Transmission speed can be slow", "Interference is possible", "The signal degrades quickly without repeaters or boosters"], "a") + "</p>", None) + peq(SRC("s21", "11/13", "Q4(c)(ii)"), "3 marks", "Justify",
  "Melinda mainly uses the internet to watch films and play computer games. Tick one box to identify whether Melinda should connect to the router using a wired or wireless network and justify your choice.",
  "No mark for the choice: the marks are for the justification. Games and films need speed and reliability.",
  "<p>Wired, up to three: " + mks(["Faster connection, higher bandwidth", "needed as she is downloading or streaming large files", "less time waiting, less latency, fewer delays", "More reliable and stable, and less susceptible to distance, walls or interference", "More secure"]) + " (Wireless can be justified with: freedom of movement between rooms; no physical connection; easily expanded; less cabling and so cheaper setup.)</p>", "Ticking a box and giving no justification. There is no mark for the choice itself.")

review = req("3 marks", "Explain", "A small firm backs up its accounts to a public cloud. Explain one benefit and one risk.", "Think of backup and control.", "<p>" + mks(["Benefit: the data is stored off-site and can be recovered if the office computers fail", "Risk: the firm depends on the provider for security and backup", "and cannot reach the data without an internet connection"]) + "</p>", None) + req("2 marks", "State", "State two reasons why a company might choose a private cloud rather than a public cloud.", "Control.", "<p>" + mks(["Greater control over security and privacy", "Greater control over backup, and storage can be tailored to the company"]) + "</p>", None) + req("3 marks", "Explain", "Explain why fibre-optic cable is used for the main links between cities.", "Bandwidth and distance.", "<p>" + mks(["It has a high bandwidth so it carries a lot of data", "It can be used over long distances before repeaters are needed", "It has a low risk of interference and is hard to hack into"]) + "</p>", None) + req("2 marks", "Describe", "Describe one situation where a satellite link is suitable and one disadvantage.", "Remote areas; delay.", "<p>" + mks(["Suitable where cables cannot easily reach, for example a remote village or a ship", "Disadvantage: a long delay (latency) as the signal travels to the satellite and back, and it is expensive"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between radio waves and microwaves as transmission media.", "Coverage and path.", "<p>" + mks(["Radio waves spread in all directions and are used for Wi-Fi to nearby devices", "Microwaves are higher-frequency waves sent between dishes or towers on a line-of-sight path over long distances"]) + "</p>", None)

tips = tips_html([
  ("Define cloud: remote server.", "Accessing services or files on a remote server."),
  ("Public v private.", "Public: third party, anyone. Private: dedicated, one organisation."),
  ("Drawback number one: the internet.", "Then reliance on a third party for security and backup."),
  ("Fibre: light. Copper: electricity.", "Then bandwidth, distance, interference, security."),
  ("Wireless: mobile but weaker.", "Name the specific drawback."),
  ("Justify.", "Marks come from linking the choice to the user's needs."),
], [("cloud computing", "Accessing services or files on a remote server."), ("a private cloud", "A dedicated cloud only available to one organisation."), ("bandwidth", "How much data a link can carry."), ("latency", "The delay before data arrives.")],
  [("Define", "Give the exact meaning."), ("Give / Identify", "State the points."), ("Describe", "Say what it is or does."), ("Justify", "Reason for the choice.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 40, 120, 60, "cell", { rx: 8 }) + SV.text(80, 66, "Your device", "lbl bd", { "text-anchor": "middle" }) + SV.text(80, 86, k >= 3 ? "(no files kept)" : "", "sm", { "text-anchor": "middle" });
    o += SV.rect(420, 20, 140, 120, k >= 1 ? "f1" : "cell", { rx: 12 }) + SV.text(490, 48, "Cloud server", "lbl bd", { "text-anchor": "middle" }) + SV.text(490, 68, "(remote)", "sm", { "text-anchor": "middle" });
    if (k >= 1) o += SV.path("M140,60 H420", "ax", { style: "stroke-dasharray:6 5" }) + SV.text(280, 52, "internet", "sm", { "text-anchor": "middle" }); if (k >= 2) o += SV.rect(445, 82, 90, 28, "cell-ok", { rx: 4 }) + SV.text(490, 101, "file.docx", "lbl", { "text-anchor": "middle", style: "font-size:12px" });
    if (k >= 3) o += SV.rect(20, 140, 120, 36, "cell", { rx: 8 }) + SV.text(80, 163, "Another device", "lbl", { "text-anchor": "middle", style: "font-size:12px" }) + SV.path("M140,158 L420,120", "ax", { style: "stroke-dasharray:6 5" }); return o; };
  Lib.stepper($("#stA"), { w: 600, h: 190, label: "Cloud storage", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "A device and a remote <b>cloud server</b> run by a provider.", s: { i: 0 } }, { cap: "The device connects to the server over the <b>internet</b>.", s: { i: 1 } }, { cap: "The file is stored on the <b>remote server</b>.", s: { i: 2 } }, { cap: "Any other device with an internet connection can reach the same file. Without the internet, nobody can.", s: { i: 3 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "copper: electrical signal", "lbl bd") + SV.path("M20,50 H560", "ax", { style: "stroke:#b87333;stroke-width:6" }); const x1 = 20 + k * 110; o += SV.circle(Math.min(560, x1), 50, 8 - Math.min(6, k), "dot4");
    o += SV.text(20, 22 + 80, "fibre: pulses of light", "lbl bd") + SV.path("M20,130 H560", "ax", { style: "stroke:var(--accent);stroke-width:6;opacity:.5" }); o += SV.circle(Math.min(560, 20 + k * 110), 130, 8, "dot1");
    if (k >= 4) o += SV.text(20, 76, "signal weakens and picks up noise: repeaters needed over distance", "sm") + SV.text(20, 156, "light arrives strong: far less interference, much longer distance", "sm"); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 175, label: "Copper and fibre", base: { i: 0 }, draw, tween: 100, dwell: 1600, steps: [{ cap: "The same data is sent down copper (electrical signals) and fibre (light).", s: { i: 0 } }, { cap: "The copper signal is already weakening; the light pulse is not.", s: { i: 1 } }, { cap: "Further on, the copper signal is weaker and can pick up interference.", s: { i: 2 } }, { cap: "Over distance the electrical signal needs a repeater.", s: { i: 3 } }, { cap: "<b>Fibre</b>: higher bandwidth, longer distance, less interference, harder to tap. <b>Copper</b>: cheaper and easier to install.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; [[110, 40], [300, 40], [490, 40], [205, 110], [395, 110]].forEach(([x, y], i) => (o += SV.rect(x - 38, y - 18, 76, 36, "cell", { rx: 8, ...op(0.8) }) + SV.text(x, y + 4, "cell " + (i + 1), "lbl", { "text-anchor": "middle", style: "font-size:12px" })));
    o += SV.rect(262, 80, 76, 40, "f3", { rx: 8 }) + SV.text(300, 104, "tower", "lbl bd", { "text-anchor": "middle" }); if (k >= 1) o += SV.rect(520, 140, 70, 30, "cell-warn", { rx: 6 }) + SV.text(555, 160, "phone", "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); if (k >= 2) o += SV.path("M520,150 L338,106", "ax", { style: "stroke-dasharray:5 4;stroke:var(--accent);stroke-width:3" }) + SV.text(440, 118, "radio", "sm", { "text-anchor": "middle" }); if (k >= 3) o += SV.rect(30, 140, 70, 30, "cell-warn", { rx: 6 }) + SV.text(65, 160, "phone 2", "lbl", { "text-anchor": "middle", style: "font-size:11px" }) + SV.path("M100,150 L262,108", "ax", { style: "stroke-dasharray:5 4;stroke:var(--accent);stroke-width:3" }); return o; };
  Lib.stepper($("#stC"), { w: 620, h: 190, label: "Cell phone network", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "The land is split into <b>cells</b>. Each has a tower with an antenna.", s: { i: 0 } }, { cap: "A phone is in range of one cell's tower.", s: { i: 1 } }, { cap: "It transmits data to the tower using <b>low-power radio signals</b>.", s: { i: 2 } }, { cap: "<b>Many devices</b> can communicate with the same tower at the same time.", s: { i: 3 } }] });
})();

(function () {
  let on = true; const b = $("#iB");
  const paint = () => { const rows = [["Open a file stored in the public cloud", on], ["Share a document with a colleague online", on], ["Open a file on the LAN server", true], ["Print on the office printer", true]]; $("#iO").innerHTML = '<div class="tw"><table class="t"><tr><th>Task</th><th>Possible?</th></tr>' + rows.map(([t, ok]) => `<tr><td>${t}</td><td style="font-weight:700;color:${ok ? "var(--good)" : "var(--bad)"}">${ok ? "yes" : "no: no internet"}</td></tr>`).join("") + `</table></div><div class="verdict">${on ? "The internet is on: cloud and LAN both work." : "The internet is off: cloud files cannot be reached. The LAN server still works because it does not use the internet."}</div>`; b.querySelectorAll("button").forEach((x) => (x.className = (x.dataset.k === "on") === on ? "on" : "")); };
  [["on", "Internet on"], ["off", "Internet off"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { on = k === "on"; paint(); }; b.appendChild(x); }); paint();
})();
(function () {
  let dist = 50, need = "speed"; const b = $("#dB");
  const paint = () => { const L = [["Copper cable", dist <= 100 && need !== "remote", "cheap and easy to install; fine over short distances"], ["Fibre-optic cable", need !== "mobile" && need !== "remote", "high bandwidth, long distance, little interference"], ["Radio waves (Wi-Fi)", dist <= 100 && need !== "speed", "no cables; devices can move"], ["Microwaves", dist > 100 && need !== "mobile", "line of sight between towers; long distances"], ["Satellite", need === "remote" || dist > 1000, "reaches remote areas; long delay"]];
    $("#dO").innerHTML = '<div class="tw"><table class="t"><tr><th>Medium</th><th>Suitable?</th><th>Why</th></tr>' + L.map(([m, ok, w]) => `<tr><td>${m}</td><td style="font-weight:700;color:${ok ? "var(--good)" : "var(--muted)"}">${ok ? "suitable" : "less suitable"}</td><td>${w}</td></tr>`).join("") + `</table></div><div class="verdict">Distance ${dist} m, need: <b>${need}</b>.</div>`; b.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === need ? "on" : "")); };
  [["speed", "Fast and reliable"], ["mobile", "Devices must move"], ["remote", "Remote area"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { need = k; paint(); }; b.appendChild(x); });
  Lib.slider($("#dS"), { id: "ds", label: "Distance (m) ", min: 10, max: 5000, value: 50, fmt: (x) => x, onInput: (v) => { dist = v; paint(); } }); paint();
})();
btnTable("wB", "wO", [
  ["Downloading large files and playing online games", "Wired", "Faster, lower latency, more stable"],
  ["Moving between rooms with a tablet", "Wireless", "Freedom of movement, no cable"],
  ["Transferring confidential data", "Wired", "More secure: a physical connection is needed"],
  ["A temporary stall at an event", "Wireless", "Quick, cheap setup with no cabling"],
  ["A server room", "Wired", "Reliable and fast connections between servers"],
  ["Adding many guest devices", "Wireless", "Easy to add devices without more cables"]
], ["Situation", "Choice", "Reason"]);
''' + _prjs

finish("as-2-1-2-cloud-computing-transmission-media", "as212", "Cloud Computing and Transmission Media",
  "Public and private cloud computing, their benefits and drawbacks, copper, fibre, radio, microwave and satellite media, the cell phone network and wired against wireless; animations, labs and the real Paper 1 questions from 2021 to 2025.",
  "2.1.2", "2 · Communication", "section 2.1 Networks including the internet", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on cloud computing and transmission media (Paper 1), 2021 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
