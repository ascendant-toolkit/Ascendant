const MONO = "font-family:ui-monospace,Menlo,Consolas,monospace;";
const pick = (a) => a[Math.floor(Math.random() * a.length)];
const rbits = (n) => Array.from({ length: n }, () => (Math.random() < 0.5 ? "0" : "1")).join("");
const flipAt = (s, i) => s.slice(0, i) + (s[i] === "1" ? "0" : "1") + s.slice(i + 1);
const ones = (s) => (s.match(/1/g) || []).length;
const hex = (n) => n.toString(16).toUpperCase();
const norm = (h) => h.replace(/^0+(?=.)/, "").toUpperCase();
const bytesOf = (s) => s.match(/.{8}/g);
const spaced = (s) => bytesOf(s).join(" ");

/* ---------- 1. sender builds the trailer ---------- */
const PAY = "11110110011110111011110111111111", BYTES = bytesOf(PAY), TOT = ones(PAY), TH = hex(TOT);
const CW = 34, CG = 4, X0 = 120, Y0 = 34, RH = 44;
function cellRow(bits, x0, y, cls) {
  let s = "";
  [...bits].forEach((b, i) => {
    s += SV.rect(x0 + i * (CW + CG), y, CW, 34, "cell" + (cls && cls[i] ? " cell-" + cls[i] : ""), { rx: 6 }) + SV.text(x0 + i * (CW + CG) + CW / 2, y + 23, b, "lbl bd", { "text-anchor": "middle", style: MONO + "font-size:18px" });
  });
  return s;
}
function buildFrame(k) {
  let s = SV.text(24, Y0 - 12, "Payload", "sm bd", { "text-anchor": "start" });
  BYTES.forEach((b, i) => {
    const y = Y0 + i * RH, cur = k >= 1 && k <= 4 && i === k - 1, cls = {};
    if (cur) [...b].forEach((c, q) => { if (c === "1") cls[q] = "cur"; });
    s += SV.text(24, y + 23, "Byte " + (i + 1), "sm", { "text-anchor": "start" }) + cellRow(b, X0, y, cls);
    if (k > i + 1 && k >= 1) s += SV.text(X0 + 8 * (CW + CG) + 16, y + 24, ones(b) + " ones", "lbl bd t1", { "text-anchor": "start" });
    else if (cur) s += SV.text(X0 + 8 * (CW + CG) + 16, y + 24, "counting… " + ones(b), "lbl bd t1", { "text-anchor": "start" });
  });
  const yt = Y0 + 4 * RH + 8;
  if (k >= 5) s += SV.text(X0, yt + 16, "Total 1-bits: 6 + 6 + 6 + 8 = " + TOT, "lbl bd t1", { "text-anchor": "start" });
  if (k >= 6) s += SV.text(X0, yt + 42, TOT + " = 1 × 16 + 10 (A), so the hex value is " + TH, "lbl bd t4", { "text-anchor": "start" });
  if (k >= 7) {
    const y = yt + 66;
    s += SV.rect(X0, y, 70, 40, "cell", { rx: 6 }) + SV.text(X0 + 35, y + 25, "Header", "sm", { "text-anchor": "middle" });
    s += SV.rect(X0 + 74, y, 160, 40, "cell cell-cur", { rx: 6 }) + SV.text(X0 + 154, y + 25, "Payload (32 bits)", "lbl", { "text-anchor": "middle" });
    s += SV.rect(X0 + 238, y, 70, 40, "cell cell-warn", { rx: 6 }) + SV.text(X0 + 273, y + 26, TH, "lbl bd", { "text-anchor": "middle", style: MONO + "font-size:18px" });
    s += SV.text(X0 + 273, y + 58, "Trailer", "sm", { "text-anchor": "middle" });
  }
  return s;
}
const frames = [
  { cap: "The sending computer is about to send a packet. The <b>payload</b> is 4 bytes (32 bits). The trailer value has not been worked out yet.", ps: [0, 1], py: [0, 1] },
  ...BYTES.map((b, i) => ({ cap: `<b>Add up the 1-bits</b> in byte ${i + 1}: <span style="font-family:var(--mono)">${b}</span> has <b>${ones(b)}</b>.`, ps: [2, 3], py: [2, 3] })),
  { cap: `The total number of 1-bits in the payload is <b>${TOT}</b>.`, ps: [4], py: [3] },
  { cap: `Write the total as a <b>hex value</b>: ${TOT} ÷ 16 = 1 remainder 10, and 10 is A. So the hex value is <b>${TH}</b>.`, ps: [5], py: [4] },
  { cap: `The hex value <b>${TH}</b> is stored in the <b>trailer</b> and the packet is sent.`, ps: [5], py: [4] },
];
frames.forEach((f, k) => (f.svg = buildFrame(k)));
Lib.algo($("#stA"), {
  w: 700, h: 400, label: "Adding up the 1-bits in a payload and storing the total as hex", dwell: 3800, frames,
  pseudo: [
    "FUNCTION TrailerValue(Payload) RETURNS STRING",
    "   Total ← 0",
    "   FOR EACH Byte IN Payload",
    "      Total ← Total + (number of 1-bits in Byte)",
    "   NEXT Byte",
    "   RETURN Total as a hex value",
    "ENDFUNCTION",
  ],
  py: [
    "def trailer_value(payload):",
    "    total = 0",
    "    for byte in payload:",
    "        total += byte.count('1')",
    "    return format(total, 'X')",
    "",
    "payload = ['11110110', '01111011', '10111101', '11111111']",
    "print(trailer_value(payload))   # 1A",
  ],
});

/* ---------- 2. packet journey ---------- */
const BADPAY = flipAt(PAY, 29), BADN = ones(BADPAY), BADH = hex(BADN);
function pkt(x, y, pay, tr, pc, tc) {
  let s = SV.rect(x, y, 70, 44, "cell", { rx: 6 }) + SV.text(x + 35, y + 27, "Header", "sm", { "text-anchor": "middle" });
  s += SV.rect(x + 74, y, 340, 44, "cell" + (pc ? " cell-" + pc : ""), { rx: 6 }) + SV.text(x + 244, y + 28, spaced(pay), "lbl bd", { "text-anchor": "middle", style: MONO + "font-size:15px" });
  s += SV.rect(x + 418, y, 70, 44, "cell" + (tc ? " cell-" + tc : ""), { rx: 6 }) + SV.text(x + 453, y + 29, tr, "lbl bd", { "text-anchor": "middle", style: MONO + "font-size:18px" });
  s += SV.text(x + 244, y - 6, "Payload", "sm", { "text-anchor": "middle" }) + SV.text(x + 453, y - 6, "Trailer", "sm", { "text-anchor": "middle" });
  return s;
}
function journey(s) {
  const k = Math.round(s.k), X = 150;
  let o = SV.text(24, 76, "Sender", "lbl bd", { "text-anchor": "start" }) + SV.text(24, 206, "Receiver", "lbl bd", { "text-anchor": "start" });
  o += pkt(X, 48, PAY, k >= 1 ? TH : "?", "", k >= 1 ? "warn" : "");
  if (k === 1) o += SV.text(X, 118, TOT + " 1-bits → hex " + TH + " stored in the trailer", "lbl bd t4", { "text-anchor": "start" });
  if (k >= 2 && k <= 5) o += SV.arrowHead(X + 244, 140, "d", "dot1") + SV.line(X + 244, 112, X + 244, 134, "c1");
  if (k >= 2 && k <= 5) o += pkt(X, 178, k >= 3 ? BADPAY : PAY, TH, k >= 3 ? "no" : "", "warn");
  if (k === 3) o += SV.text(X, 246, "Interference changes a 1 to a 0 in the last byte.", "lbl bd t2", { "text-anchor": "start" });
  if (k === 4) o += SV.text(X, 246, `Receiver counts ${BADN} one-bits → hex ${BADH}. Trailer says ${TH}. ${BADH} ≠ ${TH}: ERROR.`, "lbl bd t2", { "text-anchor": "start" });
  if (k === 5) o += SV.text(X, 246, "Values do not match, so the receiver asks for the packet to be sent again.", "lbl bd t2", { "text-anchor": "start" });
  if (k >= 6) {
    o += pkt(X, 178, PAY, TH, "ok", "ok");
    o += SV.text(X, 246, `Re-sent packet: receiver counts ${TOT} → hex ${TH}. Trailer says ${TH}. They match: no error found.`, "lbl bd t3", { "text-anchor": "start" });
  }
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 270, label: "A packet is corrupted, the CRC check fails and the packet is re-sent", base: { k: 0 }, tween: 1, dwell: 4300, draw: journey, steps: [
  { cap: "The sending computer builds a packet. The trailer is still empty.", s: { k: 0 } },
  { cap: `It adds up the 1-bits in the payload (<b>${TOT}</b>) and stores the hex value <b>${TH}</b> in the trailer.`, s: { k: 1 } },
  { cap: "The packet is sent to the receiving computer.", s: { k: 2 } },
  { cap: "During transmission, <b>interference</b> changes one bit in the payload. Neither computer knows yet.", s: { k: 3 } },
  { cap: `The receiving computer <b>recalculates the number of 1-bits</b> in the payload it received: <b>${BADN}</b>, which is hex <b>${BADH}</b>. It <b>checks</b> this against the trailer value <b>${TH}</b>.`, s: { k: 4 } },
  { cap: "The values <b>do not match</b>, so there has been a transmission error. The packet needs to be <b>re-sent</b>.", s: { k: 5 } },
  { cap: "The packet is sent again and arrives intact. The two values <b>match</b>, so no transmission errors have occurred.", s: { k: 6 } },
] });

/* ---------- Labs 1 and 2 share one payload ---------- */
(() => {
  let P = PAY.split(""), fl = new Set();
  const byteBtns = (bits, flipped, onclick, aria) => bytesOf(bits).map((b, bi) => `<div class="byte"><div class="row8">${[...b].map((v, q) => { const i = bi * 8 + q; return `<button class="bitb ${flipped ? (flipped.has(i) ? "fl" : "") : v === "1" ? "on" : ""}" data-i="${i}" aria-label="${aria} ${i + 1}">${v}</button>`; }).join("")}</div><small>Byte ${bi + 1}: ${ones(b)} ones</small></div>`).join("");
  const pktHtml = (pay, tr) => `<div><small>Header</small><strong style="font-size:.95rem">…</strong></div><div><small>Payload</small><strong style="font-size:.95rem">${spaced(pay)}</strong></div><div class="tr"><small>Trailer</small><strong>${tr}</strong></div>`;
  function draw() {
    const pay = P.join(""), n = ones(pay), h = hex(n);
    $("#l1b").innerHTML = byteBtns(pay, null, null, "Payload bit");
    $$("#l1b button").forEach((b) => (b.onclick = () => { P[+b.dataset.i] = P[+b.dataset.i] === "1" ? "0" : "1"; fl.clear(); draw(); }));
    $("#l1n").textContent = n; $("#l1h").textContent = h; $("#l1p").innerHTML = pktHtml(pay, h);
    $("#l2s").innerHTML = pktHtml(pay, h);
    const rx = [...pay].map((b, i) => (fl.has(i) ? (b === "1" ? "0" : "1") : b)).join(""), rn = ones(rx), rh = hex(rn);
    $("#l2r").innerHTML = byteBtns(rx, fl, null, "Received bit");
    $$("#l2r button").forEach((b) => (b.onclick = () => { const i = +b.dataset.i; fl.has(i) ? fl.delete(i) : fl.add(i); draw(); }));
    $("#l2n").textContent = rn; $("#l2h").textContent = rh; $("#l2t").textContent = h;
    $("#l2v").innerHTML = rh === h ? (fl.size ? `<b>Corrupted, but NOT detected.</b> ${fl.size} bits changed, but the number of 1-bits is still ${rn}, so ${rh} matches the trailer. The receiver accepts a damaged packet.` : `${rh} matches the trailer value ${h}: <b>no transmission error found</b>.`) : `${rh} does not match the trailer value ${h}: <b>error detected</b>. The packet needs to be re-sent. The check cannot say which bit changed.`;
  }
  const rnd = (n) => { fl = new Set(); while (fl.size < n) fl.add(Math.floor(Math.random() * P.length)); draw(); };
  $("#l1r").onclick = () => { P = rbits(32).split(""); fl.clear(); draw(); };
  $("#l1z").onclick = () => { P = Array(32).fill("0"); fl.clear(); draw(); };
  $("#l2a").onclick = () => rnd(1); $("#l2b").onclick = () => rnd(2);
  $("#l2c").onclick = () => { const o = P.map((_, i) => i).filter((i) => P[i] === "1"), z = P.map((_, i) => i).filter((i) => P[i] === "0"); if (!o.length || !z.length) return; fl = new Set([pick(o), pick(z)]); draw(); };
  $("#l2e").onclick = () => { fl.clear(); draw(); };
  draw();
})();

/* ---------- Lab 3: decimal to hex ---------- */
(() => {
  const sl = Lib.slider($("#l3s"), { id: "l3n", label: "Total number of 1-bits", min: 0, max: 64, value: 26, onInput: (v) => { $("#l3w").textContent = `${Math.floor(v / 16)} × 16 + ${v % 16}${v % 16 > 9 ? " (" + hex(v % 16) + ")" : ""}`; $("#l3h").textContent = hex(v).padStart(2, "0"); } });
})();

/* ---------- Lab 4: code ---------- */
Lib.codePanel($("#l4"), {
  pseudo: [
    "// Sending computer",
    "Total ← 0",
    "FOR EACH Byte IN Payload",
    "   Total ← Total + (number of 1-bits in Byte)",
    "NEXT Byte",
    "Trailer ← Total as a hex value",
    "SEND Header, Payload, Trailer",
    "",
    "// Receiving computer",
    "Total ← 0",
    "FOR EACH Byte IN ReceivedPayload",
    "   Total ← Total + (number of 1-bits in Byte)",
    "NEXT Byte",
    "IF Total as a hex value = ReceivedTrailer THEN",
    "   OUTPUT \"No error found\"",
    "ELSE",
    "   OUTPUT \"Re-send the packet\"",
    "ENDIF",
  ],
  py: [
    "def hex_total(payload):",
    "    total = 0",
    "    for byte in payload:",
    "        total += byte.count('1')",
    "    return format(total, 'X')",
    "",
    "# sending computer",
    "payload = ['11110110', '01111011', '10111101', '11111111']",
    "trailer = hex_total(payload)                 # '1A'",
    "",
    "# receiving computer (one bit damaged in transit)",
    "received = ['11110110', '01111011', '10111101', '11111011']",
    "if hex_total(received) == trailer:",
    "    print('No error found')",
    "else:",
    "    print('Re-send the packet')             # 19 != 1A",
  ],
});

/* ---------- practise ---------- */
Lib.classify($("#cl1"), { prompt: "Drag each step to the computer that does it.", buckets: [{ label: "Sending computer" }, { label: "Receiving computer" }], items: [
  { text: "Adds up all the 1-bits in the payload", b: 0 }, { text: "Writes the total as a hex value", b: 0 }, { text: "Stores the hex value in the trailer", b: 0 },
  { text: "Recalculates the number of 1-bits in the payload", b: 1 }, { text: "Checks its value against the one in the trailer", b: 1 }, { text: "Asks for the packet to be re-sent if the values differ", b: 1 },
], done: "The sender works out and stores; the receiver recalculates and checks." });

Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Header", "The start of a packet: destination address, packet number"], ["Payload", "The data being carried by the packet"], ["Trailer", "The end of the packet, which holds the CRC value"],
  ["Hex", "Base 16, using the digits 0 to 9 and A to F"], ["CRC", "A check on a packet using the number of 1-bits in its payload"], ["Re-sent", "What happens to a packet when the two values do not match"],
], done: "Those are the six key terms." });

Lib.order($("#o1"), { prompt: "Put the steps of a CRC check in the right order.", items: [
  "The sending computer adds up all the 1-bits in the payload", "The total is written as a hex value", "The hex value is stored in the trailer and the packet is sent", "The packet arrives and the receiving computer recalculates the number of 1-bits in the payload", "The receiving computer checks its value against the one in the trailer", "If the values match there is no error; otherwise the packet is re-sent",
], done: "Count, convert, store, recount, compare, decide." });

Lib.calc($("#c1"), { qs: [
  { q: "How many 1-bits are in the byte 10110010?", a: 4, sol: "1 + 0 + 1 + 1 + 0 + 0 + 1 + 0 = 4.", hint: "Count only the 1s." },
  { q: "How many 1-bits are in the payload 11001100 00111111?", a: 10, sol: "11001100 has 4. 00111111 has 6. 4 + 6 = 10." },
  { q: "Write 10 as a hex value.", t: ["A", "0A"], ph: "hex", sol: "10 = 0 × 16 + 10, and 10 is A.", hint: "A = 10, B = 11, C = 12, D = 13, E = 14, F = 15." },
  { q: "Write 26 as a hex value.", t: ["1A"], ph: "hex", sol: "26 ÷ 16 = 1 remainder 10. 1 then A: 1A." },
  { q: "The payload is 11110000 00001111 10101010. What hex value is stored in the trailer?", t: ["C", "0C"], ph: "hex", sol: "4 + 4 + 4 = 12. 12 in hex is C.", hint: "Count each byte, add them, then convert." },
  { q: "The payload is 10110010 01101110 11010001. What hex value is stored in the trailer?", t: ["D", "0D"], ph: "hex", sol: "4 + 5 + 4 = 13. 13 in hex is D." },
  { q: "The payload is 11110000 10000011 00110011 00111111 11111110 11100011. What hex value is stored in the trailer?", t: ["1D"], ph: "hex", sol: "4 + 3 + 4 + 6 + 7 + 5 = 29. 29 = 1 × 16 + 13, and 13 is D, so 1D. The receiver recounts 29 and gets 1D again, so no error.", hint: "Count each of the six bytes, add, convert." },
  { q: "Convert the hex value 2C to decimal.", a: 44, sol: "2 × 16 + 12 = 32 + 12 = 44." },
  { q: "The trailer says 1A. The receiving computer counts 25 one-bits. Do the values match? Type YES or NO.", t: ["NO"], ph: "YES or NO", sol: "25 in hex is 19 (1 × 16 + 9). 19 is not 1A, so they do not match and the packet is re-sent.", hint: "Convert 25 to hex first." },
] });

(() => {
  const el = $("#drill");
  el.innerHTML = `<label>Practise: <select data-m class="sel"><option value="val">Find the trailer value</option><option value="chk">Accept or re-send?</option></select></label>
    <div class="qline" aria-live="polite"></div>
    <div class="row"><input class="txin" data-i type="text" autocomplete="off" autocapitalize="characters" maxlength="3" placeholder="hex" aria-label="Answer"><select class="sel" data-s aria-label="Answer" hidden><option value="">Choose…</option><option>Accept</option><option>Re-send</option></select><button class="b pri" data-a="c">Check</button><button class="b" data-a="n">New question</button><span class="fb" aria-live="polite"></span></div><p class="note" data-st></p><pre class="work" data-w hidden></pre>`;
  const ql = $(".qline", el), md = $("[data-m]", el), ip = $("[data-i]", el), sl = $("[data-s]", el), fb = $(".fb", el), st = $("[data-st]", el), wk = $("[data-w]", el);
  let ans = "", work = "", streak = 0, best = 0, solved = false;
  const count = (p) => bytesOf(p).map((b) => `${b} → ${ones(b)}`).join("\n") + `\ntotal = ${ones(p)} = hex ${hex(ones(p))}`;
  function gen() {
    solved = false; fb.textContent = ""; fb.className = "fb"; wk.hidden = true; ip.value = ""; sl.value = "";
    const p = rbits(24);
    if (md.value === "val") {
      ans = hex(ones(p)); ip.hidden = false; sl.hidden = true; ql.innerHTML = `Payload: ${spaced(p)}<br>Hex value in the trailer?`; work = count(p);
    } else {
      const r = Math.random(); let rx = p;
      if (r < 0.4) rx = p; else if (r < 0.8) rx = flipAt(p, Math.floor(Math.random() * 24)); else { const o = [...p].map((c, i) => (c === "1" ? i : -1)).filter((i) => i >= 0), z = [...p].map((c, i) => (c === "0" ? i : -1)).filter((i) => i >= 0); rx = flipAt(flipAt(p, pick(o)), pick(z)); }
      const th = hex(ones(p)), rh = hex(ones(rx)); ans = rh === th ? "Accept" : "Re-send"; ip.hidden = true; sl.hidden = false;
      ql.innerHTML = `Trailer value: ${th}<br>Payload received: ${spaced(rx)}<br>Accept or re-send?`; work = count(rx) + `\n${rh} ${rh === th ? "=" : "≠"} ${th}: ${ans === "Accept" ? "values match, accept" : "values differ, re-send"}`;
    }
  }
  $("[data-a=c]", el).onclick = () => {
    const given = md.value === "val" ? norm(ip.value.trim()) : sl.value, good = given === ans;
    if (!solved) { streak = good ? streak + 1 : 0; best = Math.max(best, streak); } if (good) solved = true;
    fb.textContent = good ? "✓ Correct" : "✗ Not quite"; fb.className = "fb " + (good ? "ok" : "no"); st.textContent = `Streak ${streak} · best ${best}`;
    wk.hidden = !good; wk.textContent = good ? work : "";
  };
  $("[data-a=n]", el).onclick = gen; md.onchange = () => { streak = 0; st.textContent = ""; gen(); }; ip.addEventListener("keydown", (e) => e.key === "Enter" && $("[data-a=c]", el).click()); gen();
})();

Lib.quiz($("#qz1"), { qs: [
  { q: "What does the sending computer store in the trailer?", opts: ["The payload again", "The total number of 1-bits in the payload, as a hex value", "The number of 0-bits in the header", "The packet number"], a: 1, why: "It adds up the 1-bits in the payload and stores the total as a hex value." },
  { q: "The payload has 30 one-bits. What is stored in the trailer?", opts: ["30", "1E", "F", "3E"], a: 1, why: "30 = 1 × 16 + 14, and 14 is E, so 1E." },
  { q: "What does the receiving computer do when the packet arrives?", opts: ["Recalculates the number of 1-bits in the payload", "Deletes the trailer", "Counts the 0-bits in the header", "Sends a copy of the payload back"], a: 0, why: "It recalculates the number of 1-bits in the payload and compares it with the trailer." },
  { q: "The two values match. What does this mean?", opts: ["The packet is definitely perfect", "No transmission errors have been found", "The packet must be re-sent", "The trailer was lost"], a: 1, why: "A match means no errors were found. It is not an absolute guarantee." },
  { q: "The values do not match. What happens?", opts: ["The receiver corrects the damaged bit", "The packet needs to be re-sent", "The trailer is ignored", "The payload is deleted for ever"], a: 1, why: "A mismatch means an error occurred, so the packet is re-sent." },
  { q: "Which part of the packet is the check value stored in?", opts: ["Header", "Payload", "Trailer", "Checksum bit"], a: 2, why: "The trailer, at the end of the packet." },
  { q: "Why might a corrupted packet still pass the check?", opts: ["The trailer is secret", "Changes in the payload left the number of 1-bits the same", "Hex cannot show errors", "The header was changed"], a: 1, why: "If one 1 becomes 0 and one 0 becomes 1, the count is unchanged and the values match." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Cyclic redundancy check (CRC)", "An error checking method used on data packets. The 1-bits in the payload are added up and stored as a hex value in the trailer, then recalculated and compared on arrival."],
  ["Packet", "A small chunk of data sent across a network, made of a header, a payload and a trailer."],
  ["Header", "The start of a packet. It holds information such as the destination address and the packet number."],
  ["Payload", "The actual data carried by the packet."],
  ["Trailer", "The end of a packet. In a CRC check it holds the hex value of the number of 1-bits in the payload."],
  ["Hex (hexadecimal)", "A number system in base 16, using 0 to 9 and A to F. It gives a compact way to write binary values."],
  ["Transmission error", "Data that has been corrupted, lost or gained on its way from sender to receiver."],
  ["Re-send", "What happens to a packet when the values do not match: the packet is sent again."],
  ["Acknowledgement", "A message sent back to say whether data arrived correctly (positive) or with errors (negative)."],
] });
