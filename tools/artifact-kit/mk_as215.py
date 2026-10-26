"""AS CS syllabus 2.1.5: IP addresses, subnetting, URLs and DNS. Run: python3 tools/artifact-kit/mk_as215.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>Every device on a network has an <b>IP address</b> so that packets can be sent to it. <b>IPv4</b> addresses are <b>32 bits</b>, written as four groups of 8-bit numbers (0 to 255) separated by full stops; <b>IPv6</b> addresses are <b>128 bits</b>, written as eight groups of four hexadecimal digits separated by colons. An IP address is made of a <b>network ID</b> and a <b>host ID</b>, and <b>subnetting</b> splits a network into smaller parts. A <b>public</b> IP address is visible on the internet; a <b>private</b> one is used only inside a LAN and is not reachable directly from outside, which helps security; a <b>static</b> address never changes while a <b>dynamic</b> one may change each time the device joins the network. People use a <b>URL</b> such as https://www.example.com/page.html, and the <b>Domain Name Service (DNS)</b> turns the domain name into the IP address of the web server.</p></div>

  <h2>1 · IPv4 and IPv6</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>IPv4</th><th>IPv6</th></tr>
    <tr><td><b>Size</b></td><td>32 bits (4 bytes)</td><td>128 bits (16 bytes)</td></tr>
    <tr><td><b>Written as</b></td><td>Four groups of 8-bit numbers, each 0 to 255, separated by <b>full stops</b>: 192.168.3.2</td><td>Eight groups of four <b>hexadecimal</b> digits separated by <b>colons</b>: 2001:0db8:0000:0000:0000:ff00:0042:8329</td></tr>
    <tr><td><b>Shortening</b></td><td>None</td><td>Consecutive groups of zeros can be replaced by a double colon: 2001:db8::ff00:42:8329</td></tr>
    <tr><td><b>Number of addresses</b></td><td>About 4.3 billion: running out</td><td>Vastly more: created to replace IPv4</td></tr>
  </table></div>
  <p>256.0.0.A is not a valid IPv4 address: the maximum value of a group is 255 and A is not a number. It is not IPv6 either: it uses full stops and has too few groups.</p>
  <h3>How an IP address is linked to a device</h3>
  <p>An IP address is <b>assigned to a device</b> on a network (usually by the router using DHCP, or set by hand). It identifies where the device is on the network so that packets can be delivered. A device on several networks can have a different address on each.</p>

  <h2>2 · Subnetting</h2>
  <p>An IP address has two parts: a <b>network ID</b> (which network or subnetwork the device is on) and a <b>host ID</b> (which device within it). Every device in one subnetwork has the <b>same network ID</b> and a <b>different host ID</b>. <b>Subnetting</b> divides a network into logical segments:</p>
  <ul>
    <li>splits a larger network into smaller, more manageable parts;</li>
    <li>reduces <b>congestion</b> (and collisions), because traffic between devices on the same subnet stays within it;</li>
    <li>improves <b>security</b>: a compromised device does not expose the whole network and not every device can reach every segment;</li>
    <li>makes it easier to <b>isolate faults</b>, and to <b>expand</b> the network.</li>
  </ul>

  <h2>3 · Public and private, static and dynamic</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Description</th><th>Implications</th></tr>
    <tr><td><b>Public IP address</b></td><td>Assigned to a device (such as a router) so it is <b>visible on the internet</b>. Unique across the internet.</td><td>Can be reached directly from outside, so it is exposed to attack</td></tr>
    <tr><td><b>Private IP address</b></td><td>Used for <b>internal LAN</b> communication only, assigned by the router. Ranges such as 192.168.x.x, 10.x.x.x.</td><td>Not directly reachable from the internet, so more secure; many LANs reuse the same private addresses</td></tr>
    <tr><td><b>Static IP address</b></td><td>Fixed: <b>does not change</b> each time the device rejoins the network</td><td>Suits servers, printers and websites that must always be found at the same address</td></tr>
    <tr><td><b>Dynamic IP address</b></td><td>May be <b>refreshed or changed</b> each time the device rejoins</td><td>Efficient use of addresses; less predictable for attackers</td></tr>
  </table></div>
  <p>A <b>static private</b> IP address does not change and can only be seen or used within the LAN. A router has two addresses: a public one so it is visible to the internet, and a private one to identify it to computers inside the LAN.</p>

  <h2>4 · URLs and the Domain Name Service</h2>
  <p>A <b>Uniform Resource Locator (URL)</b> identifies a resource on the WWW. For https://www.example.com/shop/item.html: <b>https</b> is the protocol, <b>www.example.com</b> is the domain name of the web server, and <b>/shop/item.html</b> is the path to the page.</p>
  <p>Computers route packets by IP address, not by name, so the browser needs the server's IP address. The <b>DNS</b> is a distributed directory of domain names and their IP addresses. How the browser uses a URL to get a page:</p>
  <ol>
    <li>The browser checks its <b>cache</b> for the URL or domain.</li>
    <li>It splits the URL into its parts (protocol, domain, path).</li>
    <li>It finds the IP address of the domain name by <b>querying a DNS server</b>, which sends back the matching IP address.</li>
    <li>The browser makes a connection to the <b>web server</b> at that IP address and sends a <b>request</b> for the resource.</li>
    <li>The server sends the page and the browser <b>renders and displays</b> it. The IP address is stored in the cache for future use.</li>
  </ol>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Writing IPv6 with full stops, or IPv4 with colons. IPv4 uses full stops and decimal; IPv6 uses colons and hexadecimal.</li>
    <li>Saying a private IP address is "secret". It is used only within the LAN and cannot be reached directly from the internet.</li>
    <li>Writing that DNS "finds the website". It converts the domain name into the IP address.</li>
    <li>Giving subnetting benefits as "faster" alone. Say congestion is reduced, security improved, faults isolated.</li>
    <li>Saying a static address is one that is "not used". It is one that does not change.</li>
  </ul>
'''

watch = '''
  <h2>1 · An IPv4 address in binary</h2>
  <div id="stA"></div>
  <h2>2 · From URL to web page</h2>
  <p>Press Play.</p>
  <div id="stB"></div>
  <h2>3 · Public and private addresses</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Check an IP address</h2>
  <p>Type an IPv4 or IPv6 address.</p>
  <div class="card"><input id="iI" type="text" value="192.168.3.2" style="width:100%;font:inherit;padding:8px"><div id="iO"></div></div>
  <h2>Lab 2 · Network ID and host ID</h2>
  <p>The example address is 192.168.1.37. Choose how many of the 32 bits identify the network.</p>
  <div class="card"><div id="sS"></div><div id="sO"></div></div>
  <h2>Lab 3 · DNS lookup</h2>
  <div class="card"><div id="dB" class="btnrow"></div><div id="dO"></div></div>
'''

_pr, _prjs = PR(["IPv4 or IPv6?", "Public, private, static or dynamic?", "Match the term to its meaning", "Put the URL steps in order", "Working out", "Multiple choice"],
  ("Is it IPv4 or IPv6?", ["IPv4", "IPv6"], [("32 bits", 0), ("128 bits", 1), ("Four groups separated by full stops", 0), ("Eight groups of four hex digits with colons", 1), ("Consecutive groups of zeros can be written ::", 1), ("Each group is a number from 0 to 255", 0)], "IPv4: 32 bits, full stops. IPv6: 128 bits, colons."),
  ("Which type of IP address is described?", ["Public", "Private", "Static", "Dynamic"], [("Visible on the internet", 0), ("Used only inside a LAN", 1), ("Does not change when a device rejoins the network", 2), ("May change each time the device rejoins", 3), ("Assigned by the router within the LAN", 1), ("Lets a device be reached directly from the internet", 0)], "Public/private is about visibility; static/dynamic about changing."),
  [["IPv4", "A 32-bit address in four groups"], ["IPv6", "A 128-bit address in eight hex groups"], ["Network ID", "The part of an IP address that identifies the (sub)network"], ["Host ID", "The part that identifies the device within the network"], ["DNS", "Turns a domain name into an IP address"]],
  ("Put the steps of loading a web page from a URL in order.", ["The browser checks its cache", "It queries a DNS server for the IP address", "The DNS server returns the IP address", "The browser connects to the web server and requests the page", "The browser renders and displays the page"], "Cache, query DNS, IP returned, connect, display."),
  [{"q": "How many bits are in an IPv4 address?", "a": 32, "unit": "", "tol": 0.01, "hint": "4 groups of 8.", "sol": "<b>32</b>."}, {"q": "How many bits are in an IPv6 address?", "a": 128, "unit": "", "tol": 0.01, "hint": "8 groups of 16 bits.", "sol": "<b>128</b>."}, {"q": "Convert the IPv4 group 192 to binary: how many 1 bits does it contain?", "a": 2, "unit": "", "tol": 0.01, "hint": "192 = 11000000.", "sol": "<b>2</b>."}, {"q": "A subnet uses 24 bits for the network ID. How many bits are left for the host ID?", "a": 8, "unit": "", "tol": 0.01, "hint": "32 − 24.", "sol": "<b>8</b>."}, {"q": "With 8 host bits, how many host addresses are there (2 to the power 8, before reserving any)?", "a": 256, "unit": "", "tol": 0.01, "hint": "2^8.", "sol": "<b>256</b>."}],
  [("IPv6 groups are separated by:", ["Full stops", "Colons", "Commas", "Spaces"], 1, "Colons."), ("DNS converts:", ["A domain name to an IP address", "A file to a picture", "Analogue to digital", "A URL to binary"], 0, "Domain name to IP address."), ("A private IP address:", ["Is visible on the internet", "Is only used inside a LAN", "Is always static", "Has 64 bits"], 1, "Only inside a LAN."), ("Which is a valid IPv4 address?", ["256.1.1.1", "192.168.0.1", "192.168.0", "A.B.C.D"], 1, "Each group 0 to 255."), ("A static IP address:", ["Changes each time", "Does not change", "Is never used", "Is IPv6 only"], 1, "It does not change."), ("Subnetting helps by:", ["Reducing congestion", "Deleting devices", "Raising voltage", "Adding bits"], 0, "Reducing congestion.")],
  [("IPv4", "32 bits; 4 groups 0-255; full stops."), ("IPv6", "128 bits; 8 hex groups; colons; :: for zeros."), ("Network ID / host ID", "Network part and device part."), ("Subnetting", "Smaller networks: less congestion, more security."), ("Public IP", "Visible on the internet."), ("Private IP", "Inside the LAN only."), ("Static / dynamic", "Fixed / may change."), ("DNS", "Domain name to IP address.")])

real = RWNOTE + (
rw("Your home network", "Your router has one public address from your internet provider. Your phone and laptop have private addresses like 192.168.1.20, which only work inside your home.", "private addresses are used only within the LAN.") +
rw("A website that never moves", "A web server needs the same address every time, so it is given a static IP. Your phone gets a dynamic address that can change when you reconnect.", "static addresses suit servers.") +
rw("Typing a website name", "You type a name, not a number. A DNS server looks the name up, like finding a friend's number in a phone book.", "DNS gives the IP address for a domain name.") +
rw("School network segments", "A school splits its network into subnets, such as one for staff and one for students, so the traffic stays separate and a problem on one does not affect the other.", "subnetting reduces congestion and improves security.") +
rw("Running out of addresses", "IPv4 has about 4.3 billion addresses, which ran short as phones and gadgets joined the internet. IPv6 has far more.", "IPv6 uses 128 bits.")
)

where = [
  ("M/J 2023", "13", "2(e)", "3", "Identify and describe the two parts of an IP address in a subnetwork"),
  ("O/N 2023", "12", "7(a), (b)(iii), (d)", "2 + 4 + 4", "Why 192.168.3.2 is not IPv6; two reasons for subnetting; complete a table of IP address types"),
  ("M/J 2024", "13", "5(d)", "1", "What is meant by a static private IP address"),
  ("O/N 2024", "13", "9(d)", "2 + 2", "Purpose of public and private IP addresses; the purpose of subnetting"),
  ("M/J 2025", "12", "6(c)", "6", "Complete a description of IPv4, IPv6, dynamic and private IP addresses"),
  ("O/N 2025", "11", "7", "2 + 3 + 4", "Describe static and public addresses; classify 256.0.0.A; how a browser uses a URL"),
  ("M/J 2026", "11", "7(c)", "1 + 3", "A static private IP address; three benefits of subnetting")]

past = '''  <p class="note">IP addresses, subnetting and the URL are in Paper 1 almost every series now. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("w23", "12", "Q7(a)(d)"), "2 + 4 marks", "Explain / Complete",
  "A LAN contains a router, two laptops and a server. (a) The server has the IP address 192.168.3.2. Explain why this is not an IPv6 address. (d) Complete the table by writing the missing types of IP addresses and the missing descriptions: (1) ... an IP address assigned to a device to allow direct access on the internet; static IP address ...; (2) ... an IP address used for internal LAN communication only; dynamic IP address ...",
  "(a) groups, notation, bits. (d) public, static description, private, dynamic description.",
  "<p><b>(a)</b> Any two: " + mks(["It only has four groups of digits; IPv6 has eight groups", "It uses dotted notation instead of colons", "Because it is a 32-bit (4-byte) address; IPv6 is 128 bits (16 bytes)"]) + "</p><p><b>(d)</b> " + mks(["Public IP address", "Static: an IP address that is fixed and does not change each time a device rejoins a LAN or network"]) + " " + mks(["Private IP address", "Dynamic: an IP address that may be refreshed or changed each time a device rejoins a LAN or network"], "a") + "</p>", None) + peq(SRC("w23", "12", "Q7(b)(iii)"), "4 marks", "Describe",
  "Subnetting can be used to separate a network into logical segments. Describe two other reasons why subnetting is used in a network.",
  "Each reason with an expansion: security, management, growth, performance.",
  "<p>A mark per reason (max 2) and a mark per expansion (max 2): " + mks(["To improve the security of the LAN", "so that devices do not receive unintended data, or a compromised device does not expose the whole network"]) + " " + mks(["To make network management easier", "because faults can be isolated more efficiently"], "a") + " " + mks(["To make the network easier to expand", "by allowing a greater range of IP addresses"], "n") + " " + mks(["To improve network performance", "by reducing congestion, localising communications so data between devices on the same subnet stays within it"], "e") + "</p>", None) + peq(SRC("s23", "13", "Q2(e)"), "3 marks", "Identify / Describe",
  "One site has split the network into several subnetworks. An IP address in a subnetwork is divided into two parts. Identify and describe the two parts of an IP address in a subnetwork.",
  "Network ID and host ID, with a description of each.",
  "<p>" + mks(["An IP address is made up of a network ID and a host ID"]) + " " + mks(["Each device in a subnetwork has the same network ID; each subnetwork has a different network ID"], "a") + " " + mks(["Every device has a different host ID: the host ID uniquely identifies the device within the subnetwork"], "n") + "</p>", None) + peq(SRC("s25", "12", "Q6(c)"), "6 marks", "Complete",
  "Complete the following description of IP addresses by writing the missing words. IPv4 is displayed as four groups of 8-bit numbers separated by ... . Each IPv4 address is 32 bits. IPv6 is made of eight groups of 4 ... numbers separated by colons. Multiple consecutive groups of ... can be replaced with a double colon. Each IPv6 address is ... bits. A ... IP address can change each time the computer connects to a network. A ... IP address can only be accessed by other devices in the same LAN and is assigned by the router within the LAN.",
  "Full stops, hexadecimal, zeros, 128, dynamic, private.",
  "<p>" + mks(["full stops", "hexadecimal", "zeros", "128", "dynamic", "private"]) + "</p>", None) + peq(SRC("w25", "11", "Q7"), "2 + 2 + 4 marks", "Describe / Justify / Explain",
  "Web browsers use Internet Protocol (IP) addresses. (a) Describe the following types of IP address: static; public. (b) Circle whether the IP address 256.0.0.A is IPv4, IPv6 or an invalid IP address. Justify your choice. (c) A user types a Uniform Resource Locator (URL) into the address bar of a web browser to access a web page. Explain how the web browser uses the URL to access the web page.",
  "(b) invalid. (c) cache, split URL, DNS, IP, connect, request, render.",
  "<p><b>(a)</b> " + mks(["Static: an IP address that does not change each time a device connects to the network"]) + " " + mks(["Public: an IP address assigned to a device on a network to allow the device to be visible on the internet"], "a") + "</p><p><b>(b)</b> Invalid (no mark for the choice): " + mks(["It is not IPv4 because the maximum denary value should be 255 and this uses 256", "It is not IPv6 because it uses a full stop to separate sections, not a colon, or there are not enough groups"]) + "</p><p><b>(c)</b> Any four: " + mks(["The browser checks its cache for the URL", "The browser parses the URL and splits it into its component parts", "The browser finds the IP address for the domain name by querying a DNS server", "The browser receives the matching IP address from the DNS server", "The browser creates a connection with the web server with the matching IP address", "A request for the resource is sent to the web server", "The browser renders and displays the result", "The IP address is stored in the browser cache for future use"], "n") + "</p>", "Saying DNS 'finds the web page'. DNS gives the browser the IP address; the web server provides the page.") + peq(SRC("w24", "13", "Q9(d)"), "2 + 2 marks", "State / Describe",
  "The LAN has a router. The router has a public IP address and a private IP address. (i) State the purpose of a public IP address and a private IP address. (ii) The LAN uses subnetting. Describe the purpose of subnetting in a network.",
  "Visible to the internet; identified within the LAN; smaller networks.",
  "<p><b>(i)</b> " + mks(["Public: so the router is visible to the internet, the external network or the WAN"]) + " " + mks(["Private: so the router is identified to computers within the LAN"], "a") + "</p><p><b>(ii)</b> Any two: " + mks(["It allows the network to be divided into smaller networks", "which reduces traffic in some parts of the network, or reduces congestion", "because traffic only travels through the parts necessary", "which hides the complexity of the network and allows easier maintenance"], "n") + "</p>", None) + peq(SRC("s24", "13", "Q5(d)"), "1 mark", "State",
  "The devices in the office have static private IP addresses. State what is meant by a static private IP address.",
  "Both words must be covered.",
  "<p>" + mks(["Static: the IP address for that device does not change; private: it can only be accessed, seen or used within the LAN"]) + "</p>", "Defining only one word. The answer needs both 'does not change' and 'only used within the LAN'.") + peq(SRC("s26", "11", "Q7(c)"), "1 + 3 marks", "State / Give",
  "Each of the school's computers has a static private IP address. (i) State what is meant by a static private IP address. (ii) The school's network uses subnetting. Give three benefits of using subnetting in a network.",
  "Does not change and only visible inside the LAN; smaller parts, less congestion, security, fault isolation.",
  "<p><b>(i)</b> " + mks(["It does not change and it is only visible or accessible within the network (LAN)"]) + "</p><p><b>(ii)</b> Any three: " + mks(["Subnetting splits a larger network into smaller, more manageable parts", "The network has increased efficiency (just 'faster' is not enough)", "Congestion is reduced, or fewer collisions happen", "Security is improved", "It is more straightforward to isolate faults", "It is easier to scale a network with subnets"]) + "</p>", None)

review = req("2 marks", "Explain", "Explain why 192.168.1.300 cannot be an IPv4 address.", "The largest group value.", "<p>" + mks(["Each group in IPv4 is an 8-bit number, so the maximum value is 255", "300 is greater than 255"]) + "</p>", None) + req("3 marks", "Explain", "A router has a public and a private IP address. Explain why devices in the LAN use private addresses.", "Visibility.", "<p>" + mks(["Private addresses are used only inside the LAN and are assigned by the router", "They are not directly reachable from the internet, which improves security", "The router's one public address is used to talk to the internet"]) + "</p>", None) + req("2 marks", "State", "State two examples of devices that need a static IP address and say why.", "Always found at the same place.", "<p>" + mks(["A web server, or a network printer", "Other devices must always be able to find it at the same address"]) + "</p>", None) + req("3 marks", "Describe", "Describe the role of a DNS server when a user types www.example.com.", "Name to number.", "<p>" + mks(["The browser sends the domain name to a DNS server", "The DNS server looks up the matching IP address and returns it", "The browser uses that IP address to connect to the web server"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between a network ID and a host ID.", "Which part is which?", "<p>" + mks(["The network ID identifies the network or subnetwork; every device in it shares it", "The host ID identifies one device within that network"]) + "</p>", None)

tips = tips_html([
  ("IPv4: 32 bits, full stops, 0 to 255.", "IPv6: 128 bits, colons, hexadecimal."),
  ("Public: visible. Private: inside the LAN.", "Static: fixed. Dynamic: may change."),
  ("Network ID + host ID.", "Same network ID, different host ID in a subnet."),
  ("Subnet benefits.", "Less congestion, security, fault isolation, easier to grow."),
  ("DNS: name to IP address.", "The browser then contacts the web server."),
  ("URL: protocol, domain, path.", "https://www.example.com/page."),
], [("an IP address", "The address that identifies a device on a network."), ("subnetting", "Dividing a network into smaller logical networks."), ("DNS", "The Domain Name Service: converts domain names to IP addresses."), ("a URL", "The address of a resource on the web.")],
  [("State", "Short answer."), ("Describe", "What it is or does."), ("Explain", "Reasons or steps."), ("Complete", "Fill in the missing parts.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const ip = [192, 168, 3, 2];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "192 . 168 . 3 . 2  (IPv4, 32 bits)", "lbl bd", { style: "font-family:var(--mono);font-size:16px" }); ip.forEach((v, i) => { const bits = bin(v, 8); if (k >= i + 1) { o += SV.text(40 + i * 140, 62, "group " + (i + 1) + " = " + v, "sm"); [...bits].forEach((b, j) => (o += SV.rect(30 + i * 140 + j * 15, 70, 14, 28, b === "1" ? "cell-ok" : "cell", { rx: 2 }) + SV.text(37 + i * 140 + j * 15, 90, b, "lbl bd", { "text-anchor": "middle", style: "font-size:12px;font-family:var(--mono)" }))); } });
    if (k >= 5) o += SV.text(20, 140, "4 groups × 8 bits = 32 bits", "lbl bd t3"); return o; };
  Lib.stepper($("#stA"), { w: 600, h: 160, label: "IPv4 in binary", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: [{ cap: "An IPv4 address is four groups, each a number from 0 to 255.", s: { i: 0 } }, { cap: "192 in 8 bits.", s: { i: 1 } }, { cap: "168 in 8 bits.", s: { i: 2 } }, { cap: "3 in 8 bits.", s: { i: 3 } }, { cap: "2 in 8 bits.", s: { i: 4 } }, { cap: "Four groups of 8 bits make <b>32 bits</b>.", s: { i: 5 } }] });
})();
(function () {
  const L = ["User types https://www.example.com/shop", "Browser checks its cache", "Browser splits the URL: https / www.example.com / /shop", "Browser asks a DNS server for the IP address", "DNS server returns 93.184.216.34", "Browser connects to the web server at that address and requests the page", "Server sends the page; the browser renders it"];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; L.forEach((t, i) => { if (i <= k) o += SV.rect(20, 10 + i * 36, 560, 30, i === k ? "cell-warn" : "cell-ok", { rx: 6 }) + SV.text(34, 30 + i * 36, t, "lbl", { style: "font-size:13px" }); }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 270, label: "URL to page", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: L.map((t, i) => ({ cap: ["The user types a URL.", "The browser first looks in its <b>cache</b>.", "It <b>parses</b> the URL into protocol, domain name and path.", "It <b>queries a DNS server</b> for the IP address of the domain name.", "The DNS server <b>returns the IP address</b>.", "The browser <b>connects</b> to the web server at that address and <b>requests</b> the page.", "The page is <b>rendered and displayed</b>, and the address is cached for next time."][i], s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "LAN (private addresses)", "lbl bd") + SV.rect(20, 30, 230, 160, "cell", { rx: 10 }); [["Laptop", "192.168.1.20", 50], ["Phone", "192.168.1.21", 90], ["Server", "192.168.1.5 (static)", 130]].forEach(([n, a, y]) => (o += SV.text(34, y + 12, n + "  " + a, "lbl", { style: "font-size:12px;font-family:var(--mono)" })));
    o += SV.rect(300, 80, 110, 60, "f3", { rx: 8 }) + SV.text(355, 105, "Router", "lbl bd", { "text-anchor": "middle" }) + SV.text(355, 125, "private 192.168.1.1", "sm", { "text-anchor": "middle", style: "font-size:10px" }); o += SV.path("M250,110 H300", "ax", {}) ;
    if (k >= 1) o += SV.rect(460, 80, 130, 60, "f1", { rx: 8 }) + SV.text(525, 105, "Internet", "lbl bd", { "text-anchor": "middle" }) + SV.text(525, 125, "public 203.0.113.7", "sm", { "text-anchor": "middle", style: "font-size:10px" }) + SV.path("M410,110 H460", "ax", {}); if (k >= 2) o += SV.text(300, 180, "outside, only the router's PUBLIC address is visible", "lbl bd t3", { style: "font-size:12.5px" }); return o; };
  Lib.stepper($("#stC"), { w: 620, h: 200, label: "Public and private", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "Devices inside the LAN have <b>private</b> addresses, assigned by the router.", s: { i: 0 } }, { cap: "The router also has a <b>public</b> address so it is visible on the internet.", s: { i: 1 } }, { cap: "Outsiders can reach only the public address, not the private ones. The server has a <b>static</b> address, the phone a <b>dynamic</b> one.", s: { i: 2 } }] });
})();

(function () {
  const inp = $("#iI"), out = $("#iO");
  const paint = () => { const s = inp.value.trim(); let h = ""; const v4 = /^\d{1,3}(\.\d{1,3}){3}$/.test(s), g = s.split("."); if (v4 && g.every((x) => +x <= 255)) { const priv = +g[0] === 10 || (+g[0] === 172 && +g[1] >= 16 && +g[1] <= 31) || (+g[0] === 192 && +g[1] === 168); h = `<p><b>Valid IPv4</b> (32 bits). Binary: <span class="bx">${g.map((x) => bin(+x, 8)).join(".")}</span></p><p>This is a <b>${priv ? "private" : "public"}</b> address (${priv ? "only used inside a LAN" : "visible on the internet"}).</p>`; }
    else if (v4) h = "<p><b>Invalid IPv4</b>: a group is above 255. Each group is an 8-bit number, 0 to 255.</p>"; else if (/^([0-9a-fA-F]{1,4}:){2,7}[0-9a-fA-F]{0,4}(::[0-9a-fA-F:]*)?$/.test(s) || /::/.test(s) && /^[0-9a-fA-F:]+$/.test(s)) h = "<p><b>Looks like IPv6</b> (128 bits): eight groups of four hexadecimal digits separated by colons; groups of zeros can be shortened to ::.</p>"; else h = "<p><b>Invalid</b>: not four decimal groups separated by full stops (IPv4) and not hexadecimal groups separated by colons (IPv6).</p>"; out.innerHTML = h; };
  inp.oninput = paint; paint();
})();
(function () {
  let p = 24; const ip = [192, 168, 1, 37];
  const paint = () => { const bits = ip.map((x) => bin(x, 8)).join(""), net = bits.slice(0, p), host = bits.slice(p); const hostBits = 32 - p, hosts = Math.max(0, 2 ** hostBits - 2); const fmt = (b, c) => [...b].map((x, i) => `<span style="color:${c}">${x}</span>` + ((i + 1 + (c === "var(--accent)" ? 0 : p)) % 8 === 0 && (i + 1 + (c === "var(--accent)" ? 0 : p)) < 32 ? "." : "")).join("");
    $("#sO").innerHTML = `<div class="verdict mono"><b style="color:var(--accent)">network ID bits (${p})</b> | <b style="color:var(--bad)">host ID bits (${hostBits})</b></div><p class="bx">${fmt(net, "var(--accent)")}${fmt(host, "var(--bad)")}</p><div class="verdict">Network ID: first <b>${p}</b> bits. Host ID: remaining <b>${hostBits}</b> bits. About <b>${hosts}</b> devices can share this subnet (2<sup>${hostBits}</sup> − 2, as the all-zeros and all-ones host values are reserved). More network bits mean more, smaller subnets.</div>`; };
  Lib.slider($("#sS"), { id: "ss", label: "Network ID bits ", min: 8, max: 30, value: p, fmt: (x) => x, onInput: (v) => { p = v; paint(); } }); paint();
})();
(function () {
  const T = { "www.example.com": "93.184.216.34", "www.school.edu": "198.51.100.12", "mail.example.org": "203.0.113.25", "www.nowhere.invalid": null }; const b = $("#dB");
  const show = (d) => { const ip = T[d]; $("#dO").innerHTML = `<div class="tw"><table class="t mono"><tr><th>Step</th><th>What happens</th></tr><tr><td>1</td><td>Browser cache checked for ${d}: not found</td></tr><tr><td>2</td><td>DNS query: what is the IP address of ${d}?</td></tr><tr><td>3</td><td>${ip ? "DNS reply: <b>" + ip + "</b>" : "<b>No record found</b>: the page cannot be reached"}</td></tr><tr><td>4</td><td>${ip ? "Browser connects to " + ip + " and requests the page" : "Browser shows an error"}</td></tr></table></div>`; b.querySelectorAll("button").forEach((x) => (x.className = x.textContent === d ? "on" : "")); };
  Object.keys(T).forEach((d) => { const x = document.createElement("button"); x.textContent = d; x.onclick = () => show(d); b.appendChild(x); }); show("www.example.com");
})();
''' + _prjs

finish("as-2-1-5-ip-addresses-urls-dns", "as215", "IP Addresses, URLs and DNS",
  "IPv4 and IPv6, network and host IDs and subnetting, public and private and static and dynamic addresses, URLs and the Domain Name Service; animations, labs and the real Paper 1 questions from 2023 to 2026.",
  "2.1.5", "2 · Communication", "section 2.1 Networks including the internet", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on IP addresses, subnetting, URLs and DNS (Paper 1), 2023 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
