const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)";
const note = (x, y, t, cls = "", anchor = "middle") => SV.text(x, y, t, "lbl bd " + cls, { "text-anchor": anchor });
const sm = (x, y, t, anchor = "middle") => SV.text(x, y, t, "sm", { "text-anchor": anchor });
const panel = (x, y, w, h, title, col, o = 1) => SV.rect(x, y, w, h, "", { rx: 12, style: `fill:var(--surface);stroke:${col};stroke-width:3`, opacity: o }) + (title ? SV.text(x + w / 2, y + 22, title, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) : "");
const rg = (x, y, w, h, name, val, hi, col = ACC) => SV.rect(x, y, w, h, "", { rx: 8, style: `fill:${hi ? "var(--soft)" : "var(--surface)"};stroke:${hi ? col : MUT};stroke-width:${hi ? 4 : 2}` }) + sm(x + w / 2, y + 17, name) + SV.text(x + w / 2, y + h - 12, val, "lbl bd", { "text-anchor": "middle", style: `fill:${hi ? col : "var(--ink)"}` });
const arr = (x1, y1, x2, y2, col, dash) => SV.line(x1, y1, x2, y2, "", { style: `stroke:${col};stroke-width:4;${dash ? "stroke-dasharray:7 6" : ""}` }) + SV.arrowHead(x2, y2, x2 >= x1 ? "r" : "l", "").replace('class=""', `style="fill:${col}"`);
const chip = (x, y, w, t, col) => SV.rect(x, y, w, 26, "", { rx: 13, style: `fill:${col}` }) + SV.text(x + w / 2, y + 18, t, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:12px" });

/* ---------- 4. MAC, IP, router ---------- */
function netChart(s) {
  const k = Math.round(s.k);
  let o = panel(15, 40, 190, 150, "Laptop", ACC) + panel(285, 40, 190, 150, "Router", GOOD) + panel(555, 40, 190, 150, "Web server", MUT);
  o += sm(110, 90, "NIC MAC address:") + SV.text(110, 110, "3C:22:FB:1A:B4:07", "lbl bd", { "text-anchor": "middle", style: k === 0 ? `fill:${ACC}` : "" });
  o += sm(110, 140, k >= 1 ? "IP address:" : "IP address: none yet") + (k >= 1 ? SV.text(110, 160, "192.168.1.24", "lbl bd t3", { "text-anchor": "middle" }) : "");
  o += sm(380, 90, "connects the local") + sm(380, 108, "network to the internet") + sm(380, 140, "local IP: 192.168.1.1");
  o += sm(650, 90, "IP address:") + SV.text(650, 110, "203.0.113.50", "lbl bd", { "text-anchor": "middle" });
  if (k === 0) o += note(380, 225, "The MAC address was set by the manufacturer. It never changes.", "t1");
  if (k === 1) o += arr(285, 120, 205, 120, GOOD) + note(380, 225, "The router assigns the laptop an IP address (dynamic: may change next time).", "t3");
  if (k === 2) o += arr(205, 120, 285, 120, ACC) + chip(60, 205, 250, "to 203.0.113.50 · from 192.168.1.24", ACC) + note(480, 225, "The packet carries both IP addresses.", "t1", "start");
  if (k === 3) o += arr(475, 120, 555, 120, ACC) + note(380, 225, "The router reads the destination IP and forwards the packet to the internet.", "t1");
  if (k === 4) o += arr(555, 120, 475, 120, GOOD) + arr(285, 120, 205, 120, GOOD) + note(380, 225, "The reply is sent to 192.168.1.24; the router passes it to the laptop.", "t3");
  return o;
}
Lib.stepper($("#stD"), { w: 760, h: 250, label: "A laptop sends data via a router using its IP address", base: { k: 0 }, tween: 1, dwell: 4200, draw: netChart, steps: [
  { cap: "The laptop needs a <b>network interface card (NIC)</b> to connect. The NIC has a <b>MAC address</b>, fixed when it was made.", s: { k: 0 } },
  { cap: "The <b>router</b> assigns the laptop an <b>IP address</b>. Unlike the MAC address, it comes from the network and can change.", s: { k: 1 } },
  { cap: "The laptop sends a request to a web server. The packet includes the <b>destination IP address</b>.", s: { k: 2 } },
  { cap: "The <b>router</b> connects the local network to the internet and sends the packet on towards its destination.", s: { k: 3 } },
  { cap: "The server's reply is addressed to the laptop's IP address, and the router delivers it.", s: { k: 4 } },
] });

/* ---------- Lab 4: address checker ---------- */
(() => {
  const inp = $("#ia"), out = $("#io"), vd = $("#iv"), hex = /^[0-9a-f]+$/i;
  function upd() {
    const s = inp.value.trim();
    if (!s) { out.textContent = "…"; vd.textContent = "Type an address."; return; }
    if (/[.]/.test(s) && !/:/.test(s)) {
      const p = s.split(".");
      if (p.length !== 4) { out.textContent = s; vd.innerHTML = `<span class="flag">Not valid IPv4</span> An IPv4 address has <b>4</b> numbers separated by dots, and this has ${p.length}.`; return; }
      const bad = p.find((x) => !/^\d{1,3}$/.test(x) || +x > 255);
      if (bad !== undefined) { out.textContent = s; vd.innerHTML = `<span class="flag">Not valid IPv4</span> "${esc(bad)}" is not a number from 0 to 255. Each part is 8 bits, so it can only be 0 to 255.`; return; }
      out.innerHTML = p.map((x) => (+x).toString(2).padStart(8, "0")).join(" . ");
      vd.innerHTML = `<span class="okf">Valid IPv4</span> Four groups of denary 0 to 255; each is 8 bits, so the address is 32 bits. There are 2<sup>32</sup> (about 4.3 billion) possible IPv4 addresses.`; return;
    }
    const mp = s.split(/[:-]/);
    if (mp.length === 6 && mp.every((x) => /^[0-9a-f]{2}$/i.test(x))) {
      out.innerHTML = `<span style="color:${ACC}">${mp.slice(0, 3).join(":")}</span> : <span style="color:${GOOD}">${mp.slice(3).join(":")}</span>`;
      vd.innerHTML = `<span class="okf">Valid MAC address</span> Six pairs of hex digits (48 bits). Blue: the <b>manufacturer code</b>. Green: the <b>serial code</b> the manufacturer gave this NIC.`; return;
    }
    if (/:/.test(s)) {
      const g = s.split(":");
      if (g.length === 8 && g.every((x) => x.length >= 1 && x.length <= 4 && hex.test(x))) { out.textContent = g.map((x) => x.toUpperCase().padStart(4, "0")).join(" : "); vd.innerHTML = `<span class="okf">Valid IPv6</span> Eight groups of hex digits (128 bits). There are 2<sup>128</sup> (about 3.4 × 10<sup>38</sup>) possible addresses.`; return; }
      out.textContent = s; vd.innerHTML = `<span class="flag">Not valid</span> A <b>MAC address</b> has 6 pairs of hex digits (0 to 9, A to F). An <b>IPv6</b> address has 8 groups of up to 4 hex digits. This has ${g.length} groups, or a character that is not hexadecimal.`; return;
    }
    out.textContent = s; vd.innerHTML = `<span class="flag">Not recognised</span> IPv4 uses dots (like 192.168.1.24). IPv6 and MAC addresses use colons.`;
  }
  inp.addEventListener("input", upd);
  $$("[data-ex]").forEach((b) => (b.onclick = () => { inp.value = b.dataset.ex; upd(); }));
  upd();
})();


/* ---------- Lab 2: MAC builder ---------- */
(() => {
  const m = $("#mm"), s = $("#ms"), o = $("#mo"), v = $("#mv"), hx = /^[0-9a-f]{6}$/i;
  function upd() {
    const a = m.value.trim(), b = s.value.trim();
    const pr = (x) => x.toUpperCase().match(/.{1,2}/g).join(":");
    if (hx.test(a) && hx.test(b)) { o.innerHTML = `<span style="color:${ACC}">${pr(a)}</span>:<span style="color:${GOOD}">${pr(b)}</span>`; v.innerHTML = `<span class="okf">Valid</span> A MAC address is the manufacturer code (6 hex digits) followed by the serial code (6 hex digits). That makes 12 hex digits, or 48 bits.`; }
    else { o.textContent = "…"; v.innerHTML = `<span class="flag">Check the codes</span> Each code needs exactly <b>6 hexadecimal digits</b> (0 to 9 and A to F).`; }
  }
  [m, s].forEach((e) => e.addEventListener("input", upd)); upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl5"), { prompt: "Which address does each statement describe?", buckets: [{ label: "MAC address" }, { label: "IP address" }], items: [
  { text: "Set by the manufacturer", b: 0 }, { text: "Belongs to the network interface card", b: 0 }, { text: "Does not change", b: 0 }, { text: "Made of a manufacturer code and a serial code", b: 0 },
  { text: "Allocated by the network", b: 1 }, { text: "Can be static or dynamic", b: 1 }, { text: "May change when the device reconnects", b: 1 }, { text: "Can be IPv4 or IPv6", b: 1 },
], done: "MAC: the hardware. IP: the network." });

Lib.classify($("#cl6"), { prompt: "Is each description IPv4 or IPv6?", buckets: [{ label: "IPv4" }, { label: "IPv6" }], items: [
  { text: "32 bits", b: 0 }, { text: "Four groups of denary numbers", b: 0 }, { text: "Separated by dots", b: 0 }, { text: "About 4.3 billion addresses", b: 0 },
  { text: "128 bits", b: 1 }, { text: "Eight groups of hexadecimal digits", b: 1 }, { text: "Separated by colons", b: 1 }, { text: "About 3.4 × 10³⁸ addresses", b: 1 },
], done: "IPv6 was created because IPv4 addresses were running out." });

Lib.order($("#o2"), { prompt: "Put these steps in order for a laptop requesting a web page through a home router.", items: [
  "The router assigns the laptop an IP address", "The laptop sends a request with the server's IP address as the destination", "The router reads the destination IP address", "The router forwards the data towards the internet", "The reply comes back to the router, addressed to the laptop's IP address", "The router delivers the reply to the laptop",
], done: "Assign, send, read, forward, reply, deliver." });

Lib.calc($("#c1"), { qs: [
  { q: "How many bits are in an IPv4 address?", a: 32, sol: "Four groups of 8 bits: 4 × 8 = 32." },
  { q: "A MAC address has 6 pairs of hex digits. Each hex digit is 4 bits. How many bits is the MAC address?", a: 48, sol: "12 hex digits × 4 bits = 48 bits.", hint: "6 pairs is 12 hex digits." },
  { q: "Convert the IPv4 group 11000000 to denary.", a: 192, sol: "128 + 64 = 192." },
  { q: "Convert the hex pair 3C to denary.", a: 60, sol: "3 × 16 + 12 = 60." },
  { q: "How many different values can one group in an IPv4 address take (0 to 255)?", a: 256, sol: "8 bits: 2⁸ = 256 values (0 to 255)." },
  { q: "An IPv6 address has 8 groups of 4 hex digits. How many hex digits is that in total?", a: 32, sol: "8 × 4 = 32 hex digits (128 bits)." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "Who gives a NIC its MAC address?", opts: ["The router", "The internet provider", "The manufacturer", "The user"], a: 2, why: "It is set at the point of manufacture." },
  { q: "Which is an IPv6 address?", opts: ["192.168.0.1", "3C:22:FB:1A:B4:07", "2001:0DB8:85A3:0000:0000:8A2E:0370:7334", "255.255.255.0"], a: 2, why: "Eight groups of four hex digits separated by colons." },
  { q: "What does a router do?", opts: ["Stores web pages", "Sends data to its destination and connects a network to the internet", "Measures temperature", "Encrypts the keyboard"], a: 1, why: "A router forwards data to a specific destination and can connect networks." },
  { q: "What is a dynamic IP address?", opts: ["One that never changes", "One that may change each time the device connects", "One set by the manufacturer", "One with 128 bits"], a: 1, why: "Dynamic addresses are allocated by the network and may change." },
  { q: "What does a NIC allow a computer to do?", opts: ["Store files", "Connect to a network", "Print documents", "Encrypt data"], a: 1, why: "A network interface card connects the computer to a network." },
  { q: "Why was IPv6 introduced?", opts: ["It is faster", "There were not enough IPv4 addresses", "It is easier to type", "IPv4 stopped working"], a: 1, why: "IPv6 has far more possible addresses." }
] });

Lib.cards($("#fc1"), { cards: [
  ["NIC", "Network interface card: the hardware that connects a computer to a network."],
  ["MAC address", "A unique hardware address set by the manufacturer, written as hex: a manufacturer code and a serial code."],
  ["IP address", "An address allocated by the network to identify a device."],
  ["Static IP address", "An IP address that does not change."],
  ["Dynamic IP address", "An IP address that may be different each time the device connects."],
  ["IPv4", "32-bit address written as four denary groups (0 to 255) separated by dots."],
  ["IPv6", "128-bit address written as eight groups of four hex digits separated by colons."],
  ["Router", "Sends data to a specific destination, connects a local network to the internet and can assign IP addresses."]
] });
