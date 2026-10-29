const MONO = "font-family:ui-monospace,Menlo,Consolas,monospace;";
const pick = (a) => a[Math.floor(Math.random() * a.length)];
const rbits = (n) => Array.from({ length: n }, () => (Math.random() < 0.5 ? "0" : "1")).join("");
const ones = (s) => (s.match(/1/g) || []).length;
const hex2 = (n) => n.toString(16).toUpperCase().padStart(2, "0");
const withPar = (d7) => (ones(d7) % 2) + d7;                      // even parity bit on the left
const colPar = (bs) => [...Array(8)].map((_, c) => bs.reduce((a, b) => a + +b[c], 0) % 2).join("");
const sumMod = (bs) => bs.reduce((a, b) => a + parseInt(b, 2), 0) % 256;

/* ---------- the error x check grid ---------- */
const MT = ["Parity bit", "Parity block", "Checksum", "CRC", "Echo check", "Check digit"];
const VL = { y: "Detects", s: "May detect", n: "Misses", x: "Not its job" };
const MX = [
  { e: "One bit flipped in transit", v: "yyyyyx", why: "Every transmission check notices the change. The parity block also finds <b>where</b> it is (the wrong row and wrong column cross), so it can fix the bit. The echo check sees that the copy differs but cannot say which journey went wrong. A check digit is for typing mistakes, so it plays no part." },
  { e: "Two bits in a byte swap (a 1 becomes 0 and a 0 becomes 1)", v: "nysnyx", why: "The byte still has the same number of 1-bits, so a <b>parity bit</b> and a <b>CRC</b> (which counts 1-bits) both look correct and the error is missed. The parity block catches it because two columns now have the wrong parity. A checksum usually changes because the byte's value changed. An echo check sees the copy differs." },
  { e: "A byte is lost from inside a block", v: "nssssx", why: "Each remaining byte still has correct parity, so a <b>parity bit</b> misses it. The others compare something about the whole block, so they usually notice, unless the missing byte was all 0s and changed nothing they measure." },
  { e: "An extra byte is gained", v: "ssssyx", why: "A new byte with correct parity passes a <b>parity bit</b> check. The block-level checks usually notice the changed totals, but a lucky extra byte can slip through. The echo check sees a longer copy." },
  { e: "A whole packet never arrives", v: "nnnnnx", why: "All these checks examine data that <b>has arrived</b>. If nothing arrives there is nothing to recount or compare. The sender finds out because no acknowledgement comes back before the <b>timeout</b>, then re-sends (that is ARQ)." },
  { e: "A digit is mistyped when entering a code", v: "nnnnny", why: "The wrong digit is typed in <b>before</b> sending, so it travels perfectly and every transmission check agrees it arrived as sent. Only a <b>check digit</b> tests whether the number itself is valid." },
  { e: "Two digits are typed in the wrong order", v: "nnnnns", why: "Transmission checks pass it, as above. A check digit uses weightings so that position matters, so most swaps are caught, but not every combination." },
  { e: "A digit is left out when typing", v: "nnnnns", why: "The shorter number is sent and received perfectly. The check digit recalculation almost always fails because the digits are now in different positions with different weightings." },
];
(() => {
  const t = $("#mx");
  t.innerHTML = `<thead><tr><th>Error</th>${MT.map((m) => `<th>${m}</th>`).join("")}</tr></thead><tbody>` +
    MX.map((r, i) => `<tr data-i="${i}"><th scope="row"><button class="rowb" type="button" aria-label="Explain: ${r.e}">${r.e}</button></th>${[...r.v].map((c) => `<td><span class="v ${c}">${VL[c]}</span></td>`).join("")}</tr>`).join("") + "</tbody>";
  const show = (i) => {
    $$("tr", t).forEach((tr) => tr.classList.toggle("sel", +tr.dataset.i === i));
    $("#mxv").innerHTML = `<b>${MX[i].e}.</b> ${MX[i].why}`;
  };
  $$("tbody tr", t).forEach((tr) => ($("button", tr).onclick = () => show(+tr.dataset.i)));
  show(0);
})();

/* ---------- 1. parity block locates and corrects ---------- */
const A_DATA = ["00010111", "01001011", "10110010", "00001010"], A_PAR = colPar(A_DATA);
const A_ROW = 1, A_COL = 3;
const CW = 34, CG = 4, AX = 110, AY = 46, RH = 42;
function gridFrame(k) {
  let s = "";
  for (let c = 0; c < 8; c++) s += SV.text(AX + c * (CW + CG) + CW / 2, AY - 12, "col " + (c + 1), "sm", { "text-anchor": "middle" });
  const rows = [...A_DATA, A_PAR];
  rows.forEach((row, r) => {
    const y = AY + r * RH + (r === 4 ? 12 : 0);
    s += SV.text(24, y + 23, r === 4 ? "Parity byte" : "Byte " + (r + 1), "sm", { "text-anchor": "start" });
    [...row].forEach((b, c) => {
      const flipped = r === A_ROW && c === A_COL && k >= 1 && k < 5;
      const val = flipped ? (b === "1" ? "0" : "1") : b;
      let cls = r === 4 ? "cell cell-warn" : "cell";
      if (flipped && k === 1) cls = "cell cell-no";
      if (k === 4 && r === A_ROW && c === A_COL) cls = "cell cell-no";
      if (k === 5 && r === A_ROW && c === A_COL) cls = "cell cell-ok";
      s += SV.rect(AX + c * (CW + CG), y, CW, 34, cls, { rx: 6 }) + SV.text(AX + c * (CW + CG) + CW / 2, y + 23, val, "lbl bd", { "text-anchor": "middle", style: MONO + "font-size:18px" });
    });
    if (r < 4 && k >= 2 && k < 5) {
      const bad = r === A_ROW;
      s += SV.text(AX + 8 * (CW + CG) + 14, y + 23, bad ? "odd ✗" : "even ✓", "lbl bd " + (bad ? "t2" : "t3"), { "text-anchor": "start" });
    }
  });
  if (k >= 3 && k < 5) {
    for (let c = 0; c < 8; c++) {
      const bad = c === A_COL;
      s += SV.text(AX + c * (CW + CG) + CW / 2, AY + 4 * RH + 12 + 56, bad ? "✗" : "✓", "lbl bd " + (bad ? "t2" : "t3"), { "text-anchor": "middle" });
    }
    s += SV.text(24, AY + 4 * RH + 12 + 56, "Column check", "sm", { "text-anchor": "start" });
  }
  return s;
}
const aFrames = [
  { cap: "A block of four bytes is sent. Each has a parity bit (left-most) and the <b>parity byte</b> holds the column checks. The block is correct.", ps: [0], py: [0] },
  { cap: "Interference flips <b>one bit</b> in byte 2, column 4. Neither computer knows yet.", ps: [1], py: [1] },
  { cap: "The receiver checks each <b>row</b>. Byte 2 now has an odd number of 1-bits, so that row is wrong. The others are fine.", ps: [2], py: [2] },
  { cap: "The receiver checks each <b>column</b> against the parity byte. Only column 4 is wrong.", ps: [3], py: [3] },
  { cap: "The bad bit is where the wrong row and wrong column <b>cross</b>: byte 2, column 4.", ps: [4], py: [4] },
  { cap: "The receiver flips that bit back. The error is <b>corrected</b> with no re-send. This only works for <b>one</b> bad bit.", ps: [5], py: [5] },
];
Lib.stepper($("#stA"), {
  w: 700, h: 340, label: "A parity block finds a bad bit where the wrong row and column cross, then corrects it", base: { k: 0 }, tween: 1, dwell: 3800,
  draw: (s) => gridFrame(Math.round(s.k)), steps: aFrames.map((f, k) => ({ cap: f.cap, s: { k } })),
});

/* ---------- 2. negative acknowledgement against timeout ---------- */
const SX = 110, RX = 560, Y0 = 62, DY = 38;
const ROWS = [
  { d: "r", t: "Packet 1", n: "check passes", nc: "t3" },
  { d: "l", t: "ACK (positive acknowledgement)", c: "c3" },
  { d: "r", t: "Packet 2 (a bit is flipped)", c: "c2", tc: "t2", n: "check fails", nc: "t2" },
  { d: "l", t: "NAK (negative acknowledgement)", c: "c2" },
  { d: "r", t: "Packet 2 again", n: "check passes", nc: "t3" },
  { d: "l", t: "ACK (positive acknowledgement)", c: "c3" },
  { d: "lost", t: "Packet 3" },
  { d: "wait", t: "Timeout: no acknowledgement arrives" },
  { d: "r", t: "Packet 3 again", n: "check passes", nc: "t3" },
  { d: "l", t: "ACK (positive acknowledgement)", c: "c3" },
];
function seqFrame(k) {
  let s = SV.text(SX, 22, "Sender", "lbl bd", { "text-anchor": "middle" }) + SV.text(RX, 22, "Receiver", "lbl bd", { "text-anchor": "middle" });
  s += SV.line(SX, 34, SX, Y0 + ROWS.length * DY, "ax") + SV.line(RX, 34, RX, Y0 + ROWS.length * DY, "ax");
  ROWS.forEach((r, i) => {
    if (i >= k) return;
    const y = Y0 + i * DY, cc = r.c || "c1", tc = r.tc || "";
    if (r.d === "r") {
      s += SV.line(SX, y, RX - 8, y, cc) + SV.arrowHead(RX, y, "r", cc === "c2" ? "dot2" : cc === "c3" ? "dot3" : "dot1");
      s += SV.text((SX + RX) / 2, y - 8, r.t, "lbl bd " + tc, { "text-anchor": "middle" });
      if (r.n) s += SV.text(RX + 14, y + 4, r.n, "sm bd " + r.nc, { "text-anchor": "start" });
    } else if (r.d === "l") {
      s += SV.line(RX, y, SX + 8, y, cc) + SV.arrowHead(SX, y, "l", cc === "c2" ? "dot2" : "dot3");
      s += SV.text((SX + RX) / 2, y - 8, r.t, "lbl bd " + (cc === "c2" ? "t2" : "t3"), { "text-anchor": "middle" });
    } else if (r.d === "lost") {
      s += SV.line(SX, y, 330, y, "c4") + SV.text((SX + 330) / 2, y - 8, r.t, "lbl bd t4", { "text-anchor": "middle" });
      s += SV.text(346, y + 5, "✗ lost on the way", "lbl bd t2", { "text-anchor": "start" });
    } else {
      s += SV.text((SX + RX) / 2, y + 4, r.t, "lbl bd t4", { "text-anchor": "middle" });
    }
  });
  return s;
}
const bCaps = [
  "The sender is ready to send three packets.",
  "<b>Packet 1</b> arrives and its check passes.",
  "The receiver sends a <b>positive acknowledgement</b>. The sender moves on.",
  "<b>Packet 2</b> is sent, but interference flips a bit on the way.",
  "The receiver's check <b>fails</b>, so it sends a <b>negative acknowledgement</b>. The error was <b>detected</b>.",
  "The sender re-sends packet 2 because of the NAK. This time the check passes.",
  "A positive acknowledgement is sent.",
  "<b>Packet 3</b> is sent but never arrives. There is nothing to check, so the receiver says nothing.",
  "The sender waits for the <b>timeout</b>. No acknowledgement of either kind arrives, so it knows something went wrong.",
  "After the timeout the sender <b>re-sends automatically</b>. The packet arrives and passes its check.",
  "A positive acknowledgement is sent. All three packets are delivered.",
];
Lib.stepper($("#stB"), {
  w: 760, h: 470, label: "Sender and receiver exchanging packets, with one corrupted packet fixed by a negative acknowledgement and one lost packet fixed by a timeout", base: { k: 0 }, tween: 1, dwell: 3600,
  draw: (s) => seqFrame(Math.round(s.k)),
  steps: bCaps.map((cap, k) => ({ cap, s: { k } })),
});

/* ---------- Lab 2: one block, four checks ---------- */
(() => {
  const SENT = ["0110100", "1100001", "0101001", "1011011"].map(withPar);
  let base = SENT.slice(), rec = base.slice(), added = -1, lost = -1, sentPar, sentSum, sentOnes;
  const refresh = () => { sentPar = colPar(base); sentSum = sumMod(base); sentOnes = ones(base.join("")); };
  refresh();
  const chip = (damaged, found) => (!damaged ? `<span class="v y">Pass</span>` : found ? `<span class="v y">Detected</span>` : `<span class="v n">MISSED</span>`);
  function draw() {
    const same = rec.length === base.length;
    $("#l2b").innerHTML = rec.map((b, i) => {
      const odd = ones(b) % 2 === 1;
      return `<div class="r"><small>Byte ${i + 1}</small>${[...b].map((v, c) => `<button class="bitb ${i === added ? "ex" : same && base[i][c] !== v ? "fl" : v === "1" ? "on" : ""}" data-i="${i}" data-c="${c}" aria-label="Byte ${i + 1} bit ${c + 1}">${v}</button>`).join("")}<em class="${odd ? "bad" : ""}">${odd ? "odd ✗" : "even ✓"}</em></div>`;
    }).join("") +
      `<div class="r"><small>Parity byte</small>${[...sentPar].map((v) => `<button class="bitb sp" disabled>${v}</button>`).join("")}</div>` +
      `<div class="r"><small>Column check</small>${[...Array(8)].map((_, c) => { const bad = rec.reduce((a, b) => a + +b[c], 0) % 2 !== +sentPar[c]; return `<button class="bitb sp ${bad ? "fl" : ""}" disabled>${bad ? "✗" : "✓"}</button>`; }).join("")}</div>`;
    $$("#l2b button[data-i]").forEach((b) => (b.onclick = () => { const i = +b.dataset.i, c = +b.dataset.c; rec[i] = rec[i].slice(0, c) + (rec[i][c] === "1" ? "0" : "1") + rec[i].slice(c + 1); draw(); }));
    const damaged = rec.join("|") !== base.join("|");
    const badRows = rec.map((b, i) => (ones(b) % 2 ? i : -1)).filter((i) => i >= 0);
    const badCols = [...Array(8)].map((_, c) => (rec.reduce((a, b) => a + +b[c], 0) % 2 !== +sentPar[c] ? c : -1)).filter((c) => c >= 0);
    const rSum = sumMod(rec), rOnes = ones(rec.join(""));
    const pBit = badRows.length > 0, pBlk = badRows.length > 0 || badCols.length > 0, ck = rSum !== sentSum, crc = rOnes !== sentOnes, echo = damaged;
    const found = [pBit, pBlk, ck, crc, echo];
    const located = same && badRows.length === 1 && badCols.length === 1;
    $("#l2cs").textContent = hex2(sentSum); $("#l2cr").textContent = hex2(rSum); $("#l2ps").textContent = hex2(sentOnes); $("#l2pr").textContent = hex2(rOnes);
    const rows = [
      ["Parity bit (each byte)", pBit, badRows.length ? `Odd parity in byte ${badRows.map((i) => i + 1).join(", ")}` : "Every byte has even parity"],
      ["Parity block (rows and columns)", pBlk, badRows.length || badCols.length ? `Wrong rows: ${badRows.length ? badRows.map((i) => i + 1).join(", ") : "none"} · wrong columns: ${badCols.length ? badCols.map((c) => c + 1).join(", ") : "none"}${located ? `. <b>Located: byte ${badRows[0] + 1}, column ${badCols[0] + 1}</b>` : ""}` : "All rows and columns agree"],
      ["Checksum", ck, `Received ${hex2(rSum)}, sent ${hex2(sentSum)}`],
      ["CRC (count of 1-bits)", crc, `Received ${hex2(rOnes)}, sent ${hex2(sentOnes)}`],
      ["Echo check", echo, echo ? "The copy sent back differs from the original" : "The copy sent back is identical"],
    ];
    $("#l2t").innerHTML = `<tr><th>Check</th><th>Result</th><th>Detail</th></tr>` + rows.map((r, i) => `<tr><td><b>${r[0]}</b></td><td>${chip(damaged, found[i])}</td><td style="font-family:var(--sans)">${r[2]}</td></tr>`).join("");
    const n = found.filter(Boolean).length;
    $("#l2v").innerHTML = !damaged ? "The block arrived exactly as sent, so every check passes."
      : n === 0 ? "<b>The block is damaged and no check noticed.</b> The receiver accepts wrong data. This is why different checks have different weaknesses."
      : `<b>${n} of 5 checks detected the damage.</b> ` + (located ? "The parity block found exactly one wrong row and one wrong column, so it can <b>correct the bit</b> without a re-send. " : "") + (n < 5 ? `${5 - n} missed it. ` : "") + "Where any check fails the receiver sends a negative acknowledgement and the block is re-sent." + (lost >= 0 ? ` (Byte ${lost + 1} was lost.)` : "");
  }
  const flipOne = () => { const i = Math.floor(Math.random() * rec.length), c = Math.floor(Math.random() * 8); rec[i] = rec[i].slice(0, c) + (rec[i][c] === "1" ? "0" : "1") + rec[i].slice(c + 1); };
  $("#l2a").onclick = () => { added = -1; lost = -1; flipOne(); draw(); };
  $("#l2c").onclick = () => {
    const ok = rec.map((b, i) => i).filter((i) => rec[i].includes("0") && rec[i].includes("1")); if (!ok.length) return;
    added = -1; lost = -1; const i = pick(ok), b = [...rec[i]], o = b.map((v, k) => (v === "1" ? k : -1)).filter((k) => k >= 0), z = b.map((v, k) => (v === "0" ? k : -1)).filter((k) => k >= 0);
    b[pick(o)] = "0"; b[pick(z)] = "1"; rec[i] = b.join(""); draw();
  };
  $("#l2d").onclick = () => { if (rec.length < 2) return; added = -1; lost = Math.floor(Math.random() * rec.length); rec.splice(lost, 1); draw(); };
  $("#l2e").onclick = () => { lost = -1; added = Math.floor(Math.random() * (rec.length + 1)); rec.splice(added, 0, withPar(rbits(7))); draw(); };
  $("#l2n").onclick = () => { base = Array.from({ length: 4 }, () => withPar(rbits(7))); refresh(); rec = base.slice(); added = -1; lost = -1; draw(); };
  $("#l2r").onclick = () => { rec = base.slice(); added = -1; lost = -1; draw(); };
  draw();
})();

/* ---------- Lab 3: cost of each check ---------- */
(() => {
  const defs = [
    ["Parity bit", (n) => n, (n) => n / 8],
    ["Parity block", (n) => n + 8, (n) => (n + 8) / (8 * n) * 100],
    ["Checksum", () => 8, (n) => 100 / n],
    ["CRC", () => 8, (n) => 100 / n],
    ["Echo check", (n) => 8 * n, () => 100],
  ];
  const draw = (n) => {
    $("#l3o").innerHTML = defs.map(([name, bits, pct]) => { const p = pct(n); return `<div class="o"><b>${name}</b><div class="bar"><i style="width:${Math.min(100, p)}%"></i></div><span>+${bits(n)} bits (${p.toFixed(p < 10 ? 1 : 0)}%)</span></div>`; }).join("");
    $("#l3v").innerHTML = `A block of <b>${n} bytes</b> (${8 * n} bits). Checksums and CRCs cost one byte, so their share shrinks as the block grows. A parity bit always costs 12.5%. A parity block costs a little more but can <b>locate</b> an error. An echo check always doubles the traffic.`;
  };
  Lib.slider($("#l3s"), { id: "l3n", label: "Block size in bytes: ", min: 4, max: 256, step: 4, value: 16, onInput: draw });
})();

/* ---------- Lab 4: code ---------- */
Lib.codePanel($("#l4"), {
  pseudo: [
    "FUNCTION ParityOK(Byte : STRING) RETURNS BOOLEAN",
    "   Ones ← 0",
    "   FOR EACH Bit IN Byte",
    "      IF Bit = '1' THEN",
    "         Ones ← Ones + 1",
    "      ENDIF",
    "   NEXT Bit",
    "   RETURN Ones MOD 2 = 0",
    "ENDFUNCTION",
    "",
    "Faulty ← 0",
    "FOR EACH Byte IN Block",
    "   IF NOT ParityOK(Byte) THEN",
    "      Faulty ← Faulty + 1",
    "   ENDIF",
    "NEXT Byte",
    "IF Faulty = 0 THEN",
    "   SEND PositiveAcknowledgement",
    "ELSE",
    "   SEND NegativeAcknowledgement",
    "ENDIF",
  ],
  py: [
    "def parity_ok(byte):",
    "    return byte.count('1') % 2 == 0",
    "",
    "block = ['01101111', '11100100', '01011011', '10111011']",
    "faulty = sum(1 for b in block if not parity_ok(b))",
    "",
    "# a parity bit says a byte is wrong, not which bit",
    "print('ACK' if faulty == 0 else 'NAK')   # NAK: byte 3 has five 1-bits",
  ],
});

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Drag each situation to the type of error it is.", buckets: [{ label: "Corrupted data" }, { label: "Lost or gained data" }, { label: "Data entry error" }], items: [
  { text: "Interference turns a 1 into a 0", b: 0 }, { text: "Bits sent in parallel arrive out of step", b: 0 }, { text: "Radio interference alters bits in a call", b: 0 },
  { text: "A packet is dropped and never arrives", b: 1 }, { text: "An extra packet arrives that was never sent", b: 1 },
  { text: "5307 is typed as 5037", b: 2 }, { text: "13 is entered instead of 30", b: 2 }, { text: "A digit is left out of a barcode number", b: 2 },
], done: "Corrupted changes bits, lost or gained changes how much arrives, and data entry errors are human." });

Lib.classify($("#cl2"), { prompt: "What does each one do? Drag it to the right group.", buckets: [{ label: "Detects only" }, { label: "Can locate the bad bit" }, { label: "Recovers by re-sending" }], items: [
  { text: "Parity bit", b: 0 }, { text: "Checksum", b: 0 }, { text: "CRC", b: 0 }, { text: "Echo check", b: 0 }, { text: "Check digit", b: 0 },
  { text: "Parity block", b: 1 }, { text: "Wrong row and wrong column cross", b: 1 },
  { text: "Negative acknowledgement", b: 2 }, { text: "Timeout", b: 2 }, { text: "Automatic repeat request (ARQ)", b: 2 },
], done: "Detection finds a problem. Only the parity block pinpoints it, and re-sending is the usual recovery." });

Lib.match($("#m1"), { prompt: "Match each method to its main weakness.", pairs: [
  ["Parity bit", "Misses an even number of flipped bits in a byte"], ["Parity block", "More data must be sent with every block"], ["Checksum", "Says the block is wrong but not where"],
  ["CRC", "A 1 and a 0 swapping places leaves the count unchanged"], ["Echo check", "Cannot tell whether the error happened going or coming back"], ["Check digit", "Only checks data entry, not transmission"],
] });

Lib.order($("#o1"), { prompt: "Put these in order for a packet that is lost on its way.", items: [
  "The sender sends the packet and starts waiting", "The packet is lost and never reaches the receiver", "The timeout runs out with no acknowledgement", "The sender re-sends the packet automatically", "The packet arrives and the receiver sends a positive acknowledgement",
], done: "Send, lost, timeout, re-send, acknowledgement." });

Lib.calc($("#c1"), { qs: [
  { q: "Even parity. Received bytes: 01100110, 10110101, 11100001, 00011100. How many bytes contain an error?", a: 2, sol: "01100110 has four 1s (ok). 10110101 has five (error). 11100001 has four (ok). 00011100 has three (error). Two bytes.", hint: "Count the 1-bits in each byte." },
  { q: "Odd parity. The 7 data bits are 0110100. What is the parity bit?", a: 0, sol: "0110100 has three 1-bits, which is already odd, so the parity bit is 0.", hint: "Odd parity needs an odd number of 1-bits in total." },
  { q: "A block of 8 data bytes uses a parity bit in every byte and one parity byte. How many extra bits are added?", a: 16, sol: "8 parity bits (one per byte) + 8 bits in the parity byte = 16.", hint: "Count the parity bits, then the parity byte." },
  { q: "An echo check is used for a 200-byte message. How many bytes travel in total over both journeys?", a: 400, sol: "200 bytes out and 200 bytes back = 400.", hint: "The copy is as big as the original." },
  { q: "The sent checksum for bytes 12, 200, 45, 30 is 31 (the total 287, remainder after dividing by 256). The receiver gets 12, 200, 54, 30. What checksum does it calculate?", a: 40, sol: "12 + 200 + 54 + 30 = 296. 296 − 256 = 40. 40 is not 31, so the block is re-sent.", hint: "Add the received values, then subtract 256." },
  { q: "A CRC trailer says 0F. The receiver counts 14 1-bits in the payload. Enter 1 if the CRC matches and 0 if it does not.", a: 0, sol: "0F is 15 in decimal. The receiver counted 14, so they do not match and the packet is re-sent.", hint: "Convert 0F to decimal first." },
] });

(() => {
  const el = $("#drill");
  el.innerHTML = `<div class="qline" aria-live="polite"></div>
    <div class="row"><select data-s class="sel" aria-label="Answer"><option value="">Choose…</option><option value="y">Detects</option><option value="s">May detect</option><option value="n">Misses</option><option value="x">Not its job</option></select><button class="b pri" data-a="c">Check</button><button class="b" data-a="n">New question</button><span class="fb" aria-live="polite"></span></div><p class="note" data-st></p><p class="note" data-w></p>`;
  const ql = $(".qline", el), sl = $("[data-s]", el), fb = $(".fb", el), st = $("[data-st]", el), wk = $("[data-w]", el);
  let cur, streak = 0, best = 0, solved = false;
  function gen() {
    const prev = cur; do { cur = { r: Math.floor(Math.random() * MX.length), m: Math.floor(Math.random() * MT.length) }; } while (prev && prev.r === cur.r && prev.m === cur.m);
    solved = false; ql.innerHTML = `Error: <b>${MX[cur.r].e}</b><br>Check: <b>${MT[cur.m]}</b>. What happens?`; sl.value = ""; fb.textContent = ""; fb.className = "fb"; wk.innerHTML = "";
  }
  $("[data-a=c]", el).onclick = () => {
    if (!sl.value) return;
    const good = sl.value === MX[cur.r].v[cur.m]; if (!solved) { streak = good ? streak + 1 : 0; best = Math.max(best, streak); } if (good) solved = true;
    fb.textContent = good ? "✓ Correct" : "✗ Not quite"; fb.className = "fb " + (good ? "ok" : "no"); st.textContent = `Streak ${streak} · best ${best}`;
    if (good) wk.innerHTML = MX[cur.r].why;
  };
  $("[data-a=n]", el).onclick = gen; gen();
})();

Lib.quiz($("#qz1"), { qs: [
  { q: "Which error can a check digit detect but a CRC cannot?", opts: ["A bit changed by interference", "A mistyped digit entered before sending", "A bit lost in transit", "Gained data"], a: 1, why: "The mistyped number travels perfectly, so transmission checks pass it. A check digit tests the number itself." },
  { q: "A packet never arrives. Which part of ARQ deals with this?", opts: ["Parity byte", "Negative acknowledgement", "Timeout", "Echo check"], a: 2, why: "No packet means no check and no acknowledgement. The sender's timeout runs out and it re-sends." },
  { q: "Which method can find and correct a single bad bit without a re-send?", opts: ["Checksum", "Parity block", "Echo check", "Parity bit"], a: 1, why: "The wrong row and wrong column cross at the bad bit, so it can be flipped back." },
  { q: "What is the main disadvantage of an echo check compared with ARQ?", opts: ["It cannot use hex", "All the data is sent back, doubling the traffic", "It only works on text", "It needs a check digit"], a: 1, why: "ARQ only sends a short acknowledgement." },
  { q: "Two bits in one byte are flipped, a 1 becoming 0 and a 0 becoming 1. Which check misses it?", opts: ["Parity bit", "Parity block", "Echo check", "All of them"], a: 0, why: "The byte has the same number of 1-bits, so its parity is unchanged. The parity block spots the two wrong columns." },
  { q: "Which statement about transmission checks is true?", opts: ["They find mistakes made when typing", "They compare the data received with the data sent", "They stop errors from happening", "They never need a re-send"], a: 1, why: "They test how the data travelled, not whether it was right to begin with." },
  { q: "A receiver finds that a packet's CRC does not match. What does it do?", opts: ["Sends a positive acknowledgement", "Sends a negative acknowledgement", "Waits for the timeout", "Adds a check digit"], a: 1, why: "A negative acknowledgement tells the sender to re-send the packet." },
  { q: "Skew is a problem in which type of transmission?", opts: ["Serial", "Parallel", "Simplex", "Half-duplex only"], a: 1, why: "In parallel transmission the bits travel on separate wires and can arrive at slightly different times." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Corrupted data", "Data in which one or more bits have changed value during transmission, for example because of interference."],
  ["Lost data", "Bits or whole packets that never reach the receiver."], ["Gained data", "Extra data that arrives but was not part of the message sent."],
  ["Skew", "Bits sent in parallel arriving at slightly different times, which can corrupt the data."], ["Data entry error", "A mistake made when a person types or a scanner reads a code, before the data is sent."],
  ["Transposition", "Two digits entered in the wrong order, such as 5037 for 5307."], ["Phonetic error", "A mistake caused by words that sound alike, such as thirteen and thirty."],
  ["Parity block", "A parity check on rows and columns of a block of bytes, which can locate and correct one bad bit."], ["Checksum", "A value calculated from a block of data and sent after it, to be recalculated and compared by the receiver."],
  ["Echo check", "The receiver sends a copy of the data back and the sender compares it with the original."], ["Check digit", "The final digit of a code, calculated from the others, used to detect data entry errors."],
  ["Automatic repeat request (ARQ)", "A method that uses acknowledgements and a timeout to re-send data that was not received correctly."], ["Timeout", "The time a sender waits for an acknowledgement before re-sending."],
] });
