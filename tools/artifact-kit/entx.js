const MONO = "font-family:ui-monospace,Menlo,Consolas,monospace;";
const pick = (a) => a[Math.floor(Math.random() * a.length)];
const rint = (n) => Math.floor(Math.random() * n);
const ones = (s) => (s.match(/1/g) || []).length;
const hex2 = (n) => n.toString(16).toUpperCase().padStart(2, "0");
const WT = (i) => (i % 2 ? 3 : 1);                                   // weightings 1, 3, 1, 3 ...
const wtotal = (s) => [...s].reduce((a, c, i) => a + +c * WT(i), 0);
const cdOf = (d4) => (10 - (wtotal(d4) % 10)) % 10;                 // four data digits, check digit sits at weight 1
const valid = (s) => /^\d+$/.test(s) && wtotal(s) % 10 === 0;
const bcd = (s) => [...s].map((d) => (+d).toString(2).padStart(4, "0")).join("");
const unbcd = (b) => (b.match(/.{1,4}/g) || []).map((n) => { const v = parseInt(n, 2); return v > 9 ? "?" : v; }).join("");
const sumStr = (s) => [...s].map((c, i) => `${c}×${WT(i)}`).join(" + ") + " = " + wtotal(s);
const mono = (h) => `<span class="mono">${h}</span>`;
const diff = (a, b) => (a.length !== b.length ? mono(`<b>${b}</b>`) : mono([...b].map((c, i) => (c !== a[i] ? `<b>${c}</b>` : c)).join("")));
const grp = (b) => (b.match(/.{1,4}/g) || []).join(" ");
const diffBits = (a, b) => mono([...b].map((c, i) => (c !== a[i] ? `<b>${c}</b>` : c)).join("").replace(/((?:<b>.<\/b>|[01]){4})(?=.)/g, "$1 "));

/* ---------- 1. Watch: a check digit catches a typing mistake ---------- */
const FORM = "53075", WRONG = "50375";
const AXs = 170, CWs = 40, CGs = 6, xs = (i) => AXs + i * (CWs + CGs);
function aDraw(k) {
  let s = "";
  const typed = k === 5 ? FORM : WRONG;
  const row = (y, label, digs, cf) => {
    s += SV.text(20, y + 25, label, "sm", { "text-anchor": "start" });
    [...digs].forEach((c, i) => { s += SV.rect(xs(i), y, CWs, 36, cf(i), { rx: 6 }) + SV.text(xs(i) + CWs / 2, y + 25, c, "lbl bd", { "text-anchor": "middle", style: MONO + "font-size:18px" }); });
  };
  row(24, "Correct code", FORM, () => "cell");
  if (k >= 1) row(84, "Typed in", typed, (i) => (k === 5 ? "cell cell-ok" : typed[i] !== FORM[i] ? "cell cell-no" : "cell"));
  if (k >= 2) {
    s += SV.text(20, 152, "Weighting", "sm", { "text-anchor": "start" }) + SV.text(20, 188, "Digit × weight", "sm", { "text-anchor": "start" });
    [...typed].forEach((c, i) => {
      s += SV.text(xs(i) + CWs / 2, 152, WT(i), "lbl bd t1", { "text-anchor": "middle", style: MONO });
      s += SV.text(xs(i) + CWs / 2, 188, +c * WT(i), "lbl bd", { "text-anchor": "middle", style: MONO });
    });
  }
  if (k >= 3) s += SV.text(xs(5) + 12, 188, "Total = " + wtotal(typed), "lbl bd", { "text-anchor": "start" });
  if (k === 4) s += SV.text(350, 236, wtotal(typed) + " is not a multiple of 10 ✗  Code rejected. Nothing is sent.", "lbl bd t2", { "text-anchor": "middle" });
  if (k === 5) s += SV.text(350, 236, wtotal(typed) + " is a multiple of 10 ✓  Code accepted.", "lbl bd t3", { "text-anchor": "middle" });
  return s;
}
const aCaps = [
  "A customer's code is <b>53075</b>: the data 5307 plus the check digit 5.",
  "The clerk transposes two digits and types <b>50375</b>.",
  "The system multiplies each digit by its weighting: 1, 3, 1, 3, 1 (the check digit counts too).",
  "It adds the products: 5 + 0 + 3 + 21 + 5 = <b>34</b>.",
  "34 is not a multiple of 10, so the code is <b>invalid</b>. It is rejected at once. Nothing has been sent, and the clerk types it again.",
  "The clerk enters <b>53075</b>. Total 5 + 9 + 0 + 21 + 5 = 40, a multiple of 10, so the code is accepted.",
];
Lib.stepper($("#stA"), {
  w: 700, h: 260, label: "A check digit rejecting a mistyped code", base: { k: 0 }, tween: 1, dwell: 3600,
  draw: (s) => aDraw(Math.round(s.k)), steps: aCaps.map((cap, k) => ({ cap, s: { k } })),
});

/* ---------- 2. Watch: a CRC catches a flipped bit ---------- */
const BS = "01101011", BR = "01111011", BX = 150, BW = 34, BG = 4, bx = (i) => BX + i * (BW + BG), TX = BX + 8 * (BW + BG) + 10;
function bDraw(k) {
  let s = SV.text(BX, 28, "Payload", "sm", { "text-anchor": "start" }) + SV.text(TX, 28, "Trailer (hex count)", "sm", { "text-anchor": "start" });
  const bitsRow = (y, label, bits, flag) => {
    s += SV.text(20, y + 25, label, "sm", { "text-anchor": "start" });
    [...bits].forEach((c, i) => { s += SV.rect(bx(i), y, BW, 36, flag === i ? "cell cell-no" : "cell", { rx: 6 }) + SV.text(bx(i) + BW / 2, y + 25, c, "lbl bd", { "text-anchor": "middle", style: MONO + "font-size:17px" }); });
    s += SV.rect(TX, y, 54, 36, "cell cell-warn", { rx: 6 }) + SV.text(TX + 27, y + 25, "05", "lbl bd", { "text-anchor": "middle", style: MONO + "font-size:17px" });
  };
  bitsRow(40, "Sent packet", BS, -1);
  if (k >= 1) bitsRow(110, "Received", k < 4 ? BR : BS, k < 4 ? 3 : -1);
  if (k >= 2 && k < 4) s += SV.text(20, 186, "Receiver counts 6 one-bits, which is 06 in hex", "lbl bd", { "text-anchor": "start" });
  if (k >= 4) s += SV.text(20, 186, "Receiver counts 5 one-bits, which is 05 in hex", "lbl bd", { "text-anchor": "start" });
  if (k === 3) s += SV.text(20, 222, "06 ≠ 05 ✗  Negative acknowledgement sent", "lbl bd t2", { "text-anchor": "start" });
  if (k === 4) s += SV.text(20, 222, "05 = 05 ✓  The counts match", "lbl bd t3", { "text-anchor": "start" });
  if (k === 5) s += SV.text(20, 222, "Packet accepted. Positive acknowledgement sent.", "lbl bd t3", { "text-anchor": "start" });
  return s;
}
const bCaps = [
  "The sender builds a packet. The payload has <b>five</b> 1-bits, so the trailer holds <b>05</b> (hex).",
  "On the way, interference flips one bit (the fourth) from 0 to 1.",
  "The receiver counts the 1-bits in the payload it received. There are now <b>six</b>, which is 06 in hex.",
  "06 does not match the trailer 05. The packet was <b>damaged in transit</b>, so the receiver sends a negative acknowledgement.",
  "The sender re-sends the packet. This time the receiver counts five 1-bits: 05 matches the trailer.",
  "The packet is accepted and a positive acknowledgement is sent.",
];
Lib.stepper($("#stB"), {
  w: 700, h: 250, label: "A CRC mismatch revealing a bit flipped in transit", base: { k: 0 }, tween: 1, dwell: 3600,
  draw: (s) => bDraw(Math.round(s.k)), steps: bCaps.map((cap, k) => ({ cap, s: { k } })),
});

/* ---------- 3. Watch: the transmission check passes a typing mistake ---------- */
const PX = (i) => 20 + i * 140, PY = 96, PW = 118, PH = 70;
const cPay = bcd(WRONG), cCrc = hex2(ones(cPay));
const cFrames = [
  { v: ["–", "–", "–", "–", "–"], c: ["cell", "cell", "cell", "cell", "cell"], f: [], cap: "The ID should be <b>53075</b>. Follow it from keyboard to stored record." },
  { v: ["50375", "–", "–", "–", "–"], c: ["cell cell-no", "cell", "cell", "cell", "cell"], f: [], cap: "The clerk mistypes it as <b>50375</b>. This is a data entry error." },
  { v: ["50375", "none used", "–", "–", "–"], c: ["cell cell-no", "cell cell-warn", "cell", "cell", "cell"], f: [], cap: "This system has no check digit, so nothing tests whether 50375 is a valid ID." },
  { v: ["50375", "none used", "trailer " + cCrc, "–", "–"], c: ["cell cell-no", "cell cell-warn", "cell", "cell", "cell"], f: [], cap: "The packet is sent. Its CRC is worked out from the digits <b>as typed</b>, so the wrong digits are counted too." },
  { v: ["50375", "none used", "trailer " + cCrc, cCrc + " = " + cCrc + " ✓", "–"], c: ["cell cell-no", "cell cell-warn", "cell", "cell cell-ok", "cell"], f: [], cap: "It arrives perfectly. The recount matches the trailer, so the transmission check <b>passes</b>." },
  { v: ["50375", "none used", "trailer " + cCrc, cCrc + " = " + cCrc + " ✓", "50375 ✗"], c: ["cell cell-no", "cell cell-warn", "cell", "cell cell-ok", "cell cell-no"], f: [], cap: "The wrong ID is stored. Every transmission check passed, yet the data is wrong." },
  { v: ["50375", "✗ rejected", "–", "–", "–"], c: ["cell cell-no", "cell cell-ok", "cell", "cell", "cell"], f: [2, 3, 4], cap: "Add a <b>check digit</b> and 50375 totals 34, so it is rejected at the first stage, before anything is sent." },
];
function cDraw(k) {
  const F = cFrames[k], titles = ["Typed", "Entry check", "Sent", "CRC check", "Stored"];
  let s = SV.text(149, 62, "Data entry", "lbl bd t4", { "text-anchor": "middle" }) + SV.text(429, 62, "Data transmission", "lbl bd t1", { "text-anchor": "middle" });
  s += SV.line(20, 72, 278, 72, "c4") + SV.line(300, 72, 558, 72, "c1");
  titles.forEach((t, i) => {
    const fade = F.f.includes(i) ? { style: "opacity:.3" } : {}, cx = PX(i) + PW / 2;
    s += SV.rect(PX(i), PY, PW, PH, F.c[i], Object.assign({ rx: 10 }, fade));
    s += SV.text(cx, PY + 26, t, "sm bd", Object.assign({ "text-anchor": "middle" }, fade));
    s += SV.text(cx, PY + 52, F.v[i], "lbl bd", Object.assign({ "text-anchor": "middle", style: MONO + (F.f.includes(i) ? "opacity:.3" : "") }));
    if (i < 4) s += SV.line(PX(i) + PW + 2, PY + PH / 2, PX(i + 1) - 10, PY + PH / 2, "ax") + SV.arrowHead(PX(i + 1) - 2, PY + PH / 2, "r", "dot1");
  });
  return s;
}
Lib.stepper($("#stC"), {
  w: 700, h: 200, label: "A mistyped ID passing every transmission check, then being stopped by a check digit", base: { k: 0 }, tween: 1, dwell: 3800,
  draw: (s) => cDraw(Math.round(s.k)), steps: cFrames.map((f, k) => ({ cap: f.cap, s: { k } })),
});

/* ---------- Lab 1: follow a code from keyboard to receiver ---------- */
(() => {
  let data, code, sd;
  const reroll = () => { sd = { p: rint(12), k: rint(9), b: rint(20), b2: rint(20), d: rint(10) }; };
  const fresh = () => { data = String(rint(10000)).padStart(4, "0"); code = data + cdOf(data); reroll(); };
  fresh();
  function typedOf(m) {
    const a = [...code];
    if (m === "wrong") { const p = sd.p % 5; a[p] = String((+a[p] + 1 + sd.k) % 10); return a.join(""); }
    if (m === "swap") { for (let j = 0; j < 4; j++) { const p = (sd.p + j) % 4; if (a[p] !== a[p + 1]) { [a[p], a[p + 1]] = [a[p + 1], a[p]]; return a.join(""); } } return code; }
    if (m === "omit") { a.splice(sd.p % 5, 1); return a.join(""); }
    if (m === "extra") { a.splice(sd.p % 6, 0, String(sd.d)); return a.join(""); }
    return code;
  }
  function damage(pl, m) {
    const a = [...pl];
    if (m === "flip") { const i = sd.b % a.length; a[i] = a[i] === "1" ? "0" : "1"; return a.join(""); }
    if (m === "swapb") {
      const n = a.length, oi = [...Array(n).keys()].map((j) => (sd.b + j) % n).find((i) => a[i] === "1"), zi = [...Array(n).keys()].map((j) => (sd.b2 + j) % n).find((i) => a[i] === "0");
      if (oi === undefined || zi === undefined) return pl; a[oi] = "0"; a[zi] = "1"; return a.join("");
    }
    return pl;
  }
  function draw() {
    const em = $("#l1e").value, tm = $("#l1t").value, chk = $("#l1c").checked, crcOn = $("#l1x").checked;
    const typed = typedOf(em), entryBad = typed !== code;
    const rows = [["Intended code", mono(code) + ` <span class="note">(data ${data}, check digit ${code[4]})</span>`], ["Typed in", entryBad ? diff(code, typed) : mono(typed) + " <span class=\"note\">(no mistake)</span>"]];
    let verdict, good = true;
    const ok1 = valid(typed);
    rows.push(["Entry check", !chk ? "Not used" : `${sumStr(typed)}. ${ok1 ? `<span class="v y">Multiple of 10: accepted</span>` : `<span class="v n">Not a multiple of 10: rejected</span>`}`]);
    if (chk && !ok1) {
      rows.push(["Sent?", "No. The code is rejected at the keyboard and the user types it again."]);
      verdict = entryBad ? `<b>Caught at data entry.</b> The check digit found the mistake before anything was sent. The fix is to <b>re-enter</b> the code.` : "";
    } else {
      const pl = bcd(typed), tr = hex2(ones(pl)), rx = tm === "lose" ? null : damage(pl, tm), changed = rx !== null && rx !== pl;
      rows.push(["Packet sent", `payload ${mono(grp(pl))} trailer ${mono(tr)} <span class="note">(${ones(pl)} one-bits)</span>`]);
      rows.push(["Received", rx === null ? `<span class="v n">Packet never arrives</span>` : changed ? `payload ${diffBits(pl, rx)}` : "payload identical"]);
      let delivered;
      if (rx === null) {
        rows.push(["Transmission check", crcOn ? "No packet to check, so no reply comes. The sender's <b>timeout</b> runs out and it re-sends automatically." : "Not used. Nobody knows the packet is missing."]);
        delivered = crcOn ? typed : null;
      } else if (!changed) {
        rows.push(["Transmission check", crcOn ? `Recount ${ones(rx)} = ${tr} ✓ <span class="v y">Match</span>` : "Not used"]); delivered = typed;
      } else {
        const rtr = ones(rx), hit = rtr !== ones(pl);
        rows.push(["Transmission check", !crcOn ? "Not used" : hit ? `Recount ${hex2(rtr)} ≠ ${tr} <span class="v n">Mismatch</span> Negative acknowledgement, packet re-sent.` : `Recount ${hex2(rtr)} = ${tr} <span class="v s">Match: the damage is MISSED</span> The count of 1-bits did not change.`]);
        delivered = crcOn && hit ? typed : unbcd(rx);
      }
      rows.push(["Delivered", delivered === null ? "Nothing" : diff(code, delivered)]);
      good = delivered === code;
      const rec = [];
      if (entryBad) rec.push("a typing mistake");
      if (tm !== "none") rec.push("damage in transit");
      if (delivered === null) verdict = "<b>Data lost.</b> With no transmission check the packet vanished and nothing triggered a re-send.";
      else if (good) verdict = rec.length ? "<b>Correct data delivered.</b> " + (tm !== "none" && crcOn ? (tm === "lose" ? "The timeout recovered the lost packet. " : "The CRC found the damage and the packet was re-sent. ") : "") + (em !== "none" && !entryBad ? "The chosen typing mistake did not change this code." : "") : "<b>Everything arrived correctly.</b> Add a typing mistake or some damage in transit.";
      else if (entryBad && delivered === typed) verdict = `<b>Wrong data accepted.</b> ${chk ? "The mistake slipped past the check digit (they catch most typing errors, not all)." : "Without a check digit nothing tested the typed code."} The transmission checks passed it, because it arrived exactly as it was sent.`;
      else verdict = `<b>Damaged data accepted.</b> ${crcOn ? "The CRC counts 1-bits, so a 1 and a 0 swapping places leaves the count unchanged." : "Without a transmission check the damage went unnoticed."}`;
    }
    $("#l1o").innerHTML = rows.map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td></tr>`).join("");
    $("#l1v").innerHTML = verdict;
  }
  ["#l1e", "#l1t", "#l1c", "#l1x"].forEach((id) => ($(id).onchange = draw));
  $("#l1r").onclick = () => { reroll(); draw(); };
  $("#l1n").onclick = () => { fresh(); draw(); };
  $("#l1e").value = "swap"; $("#l1t").value = "none";
  draw();
})();

/* ---------- Lab 2: two checks on the same number ---------- */
(() => {
  const inp = $("#l2i");
  function draw() {
    const d = inp.value.replace(/\D/g, "").slice(0, 4);
    if (d.length < 4) { $("#l2a").innerHTML = $("#l2b").innerHTML = ""; $("#l2as").textContent = $("#l2bs").textContent = "Enter four digits."; return; }
    const t = wtotal(d), r = t % 10, cd = cdOf(d);
    $("#l2a").innerHTML = `<tr><th>Digit</th>${[...d].map((c) => `<td>${c}</td>`).join("")}</tr><tr><th>Weight</th>${[...d].map((_, i) => `<td>${WT(i)}</td>`).join("")}</tr><tr><th>Product</th>${[...d].map((c, i) => `<td>${+c * WT(i)}</td>`).join("")}</tr>`;
    $("#l2as").innerHTML = `Total ${t}. ${t} ÷ 10 leaves ${r}. ${r === 0 ? "Remainder 0, so the check digit is 0." : `10 − ${r} = <b>${cd}</b>.`} Code to type: <b>${d}${cd}</b>`;
    const pl = bcd(d), n = ones(pl);
    $("#l2b").innerHTML = `<tr><th>Digit</th>${[...d].map((c) => `<td>${c}</td>`).join("")}</tr><tr><th>Bits</th>${[...d].map((c) => `<td style="font-family:var(--mono)">${(+c).toString(2).padStart(4, "0")}</td>`).join("")}</tr><tr><th>1-bits</th>${[...d].map((c) => `<td>${ones((+c).toString(2))}</td>`).join("")}</tr>`;
    $("#l2bs").innerHTML = `Total 1-bits ${n}, so the trailer holds <b>${hex2(n)}</b> (hex). The receiver recounts and compares.`;
  }
  inp.oninput = draw; draw();
})();

/* ---------- Lab 3: beat the check digit ---------- */
(() => {
  let code, tries = 0, missed = 0, caught = 0;
  const mk = (data) => { code = data + cdOf(data); tries = missed = caught = 0; draw(); };
  const rnd = () => mk(String(rint(10000)).padStart(4, "0"));
  function draw(res) {
    $("#l3c").innerHTML = "Valid code: " + code;
    $("#l3d").innerHTML = [0, 1, 2, 3].map((i) => `<button class="b" data-i="${i}">Swap ${code[i]} and ${code[i + 1]}</button>`).join("");
    $$("#l3d button").forEach((b) => (b.onclick = () => {
      const i = +b.dataset.i, a = [...code]; [a[i], a[i + 1]] = [a[i + 1], a[i]]; const t = a.join("");
      tries++;
      if (t === code) { $("#l3v").innerHTML = `Those digits are the same, so swapping them changes nothing. Pick another pair.`; tries--; return; }
      const ok = valid(t); ok ? missed++ : caught++;
      $("#l3v").innerHTML = `<b>${t}</b>: total ${wtotal(t)}. ` + (ok ? `<span class="v n">A multiple of 10: the swap is MISSED</span> The two digits differ by 5, so the total did not change.` : `<span class="v y">Not a multiple of 10: caught</span>`);
      $("#l3s").textContent = `Swaps tried ${tries} · caught ${caught} · missed ${missed}`;
    }));
  }
  $("#l3n").onclick = rnd;
  $("#l3d").insertAdjacentHTML("afterend", `<div class="row"><button class="b" id="l3w">Give me a code with a weak spot</button></div>`);
  $("#l3w").onclick = () => {
    const a = String(rint(10000)).padStart(4, "0").split(""), p = rint(3), x = rint(10); a[p] = String(x); a[p + 1] = String((x + 5) % 10); mk(a.join(""));
    $("#l3v").innerHTML = `Look for the pair that differs by 5: ${a[p]} and ${a[p + 1]}.`; $("#l3s").textContent = "";
  };
  rnd();
  $("#l3v").innerHTML = "Pick a pair to swap. Neighbouring digits are only missed when they differ by exactly 5.";
})();

/* ---------- Lab 4: where did the error start? ---------- */
(() => {
  const ST = [
    { w: "A person types a code", z: "Data entry", e: "Incorrect digit, transposition, omitted digit, extra digit, phonetic error", c: "Check digit", f: "The code is rejected and the user types it again", n: "A CRC would pass it later, because the wrong code travels perfectly." },
    { w: "A scanner reads a barcode", z: "Data entry", e: "A misread or missing digit", c: "Check digit", f: "The till beeps and the item is scanned again", n: "Nothing has been transmitted yet." },
    { w: "A packet travels across a network (serial)", z: "Data transmission", e: "Corrupted data, gained data", c: "Parity bit or block, checksum, CRC, echo check", f: "Negative acknowledgement, then the data is re-sent (a parity block can fix one bit itself)", n: "A check digit does not compare received data with sent data." },
    { w: "Bits travel side by side (parallel)", z: "Data transmission", e: "Skew: bits arrive at different times so some are read wrongly", c: "Parity bit or block, checksum, CRC", f: "The data is re-sent", n: "Serial transmission avoids skew." },
    { w: "A packet goes missing", z: "Data transmission", e: "Lost data", c: "ARQ: no acknowledgement arrives before the timeout", f: "The sender re-sends automatically", n: "A CRC cannot help, because there is nothing to check." },
  ];
  const draw = (n) => {
    const s = ST[n - 1];
    $("#l4v").innerHTML = `<b>Stage ${n} of 5: ${s.w}.</b><br><span class="v ${s.z === "Data entry" ? "s" : "y"}">${s.z}</span><br>Possible errors: ${s.e}.<br>Check: <b>${s.c}</b>.<br>Fix: ${s.f}.<br><span class="note">${s.n}</span>`;
  };
  Lib.slider($("#l4s"), { id: "l4n", label: "Stage of the journey: ", min: 1, max: 5, step: 1, value: 1, onInput: draw });
  draw(1);
})();

/* ---------- Lab 5: code ---------- */
Lib.codePanel($("#l5"), {
  pseudo: [
    "FUNCTION CheckDigitOK(Code : STRING) RETURNS BOOLEAN",
    "   Total ← 0",
    "   FOR Position ← 1 TO LENGTH(Code)",
    "      Digit ← STRING_TO_NUM(MID(Code, Position, 1))",
    "      IF Position MOD 2 = 1 THEN",
    "         Total ← Total + Digit",
    "      ELSE",
    "         Total ← Total + Digit * 3",
    "      ENDIF",
    "   NEXT Position",
    "   RETURN Total MOD 10 = 0",
    "ENDFUNCTION",
    "",
    "REPEAT",
    "   OUTPUT \"Enter the code\"",
    "   INPUT Code",
    "UNTIL CheckDigitOK(Code)",
  ],
  py: [
    "def check_digit_ok(code):",
    "    total = 0",
    "    for pos, ch in enumerate(code, start=1):",
    "        total += int(ch) * (1 if pos % 2 == 1 else 3)",
    "    return total % 10 == 0   # the check digit is part of the sum",
    "",
    "code = input('Enter the code: ')",
    "while not check_digit_ok(code):",
    "    code = input('Invalid code, enter it again: ')",
    "print('Accepted')   # 53075 passes; 50375 totals 34 and is rejected",
  ],
});

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Drag each situation to the stage where the error happens.", buckets: [{ label: "Data entry error" }, { label: "Data transmission error" }], items: [
  { text: "5307 is typed as 5037", b: 0 }, { text: "A barcode scanner misreads a digit", b: 0 }, { text: "A digit is left out of a typed ID", b: 0 }, { text: "13 is typed instead of 30", b: 0 }, { text: "An extra digit is typed in a code", b: 0 },
  { text: "Interference turns a 1 into a 0", b: 1 }, { text: "A packet is dropped and never arrives", b: 1 }, { text: "An extra packet arrives that was never sent", b: 1 }, { text: "Bits sent in parallel arrive out of step", b: 1 }, { text: "A returned copy differs from the original", b: 1 },
], done: "If a person caused it before sending, it is data entry. If it happened on the way, it is transmission." });

Lib.classify($("#cl2"), { prompt: "Sort the checks and fixes into the right group.", buckets: [{ label: "Data entry" }, { label: "Transmission: detects" }, { label: "Transmission: recovers" }], items: [
  { text: "Check digit", b: 0 }, { text: "Re-enter or re-scan the code", b: 0 },
  { text: "Parity bit", b: 1 }, { text: "Parity block", b: 1 }, { text: "Checksum", b: 1 }, { text: "CRC", b: 1 }, { text: "Echo check", b: 1 },
  { text: "Negative acknowledgement", b: 2 }, { text: "Timeout", b: 2 }, { text: "Automatic repeat request (ARQ)", b: 2 },
], done: "Only the check digit belongs to data entry. Everything else guards the journey." });

Lib.match($("#m1"), { prompt: "Match each situation to the check that deals with it.", pairs: [
  ["A mistyped digit in an ID", "Check digit"], ["A bit changed by interference in one byte", "Parity bit"], ["One bad bit that must be fixed without a re-send", "Parity block"],
  ["A packet never arrives", "Timeout (ARQ)"], ["A copy of the data is sent back to the sender", "Echo check"], ["1-bits counted and stored in the trailer", "CRC"],
] });

Lib.order($("#o1"), { prompt: "Put these in order for a booking reference that is typed and then sent.", items: [
  "The customer types the booking reference", "The check digit is recalculated and the reference passes", "The booking is split into packets, each with a CRC in its trailer",
  "The packets travel across the network", "The receiver recounts the 1-bits and the CRCs match", "The receiver sends a positive acknowledgement",
], done: "Type, entry check, build packets, travel, transmission check, acknowledgement." });

Lib.calc($("#c1"), { qs: [
  { q: "Weightings 1, 3, 1, 3. Find the check digit for 7392.", a: 9, sol: "7×1 + 3×3 + 9×1 + 2×3 = 7 + 9 + 9 + 6 = 31. 31 leaves 1, so 10 − 1 = 9.", hint: "Multiply, add, then find what makes the next multiple of 10." },
  { q: "Weightings 1, 3, 1, 3, 1. Find the total for the code 62815.", a: 28, sol: "6×1 + 2×3 + 8×1 + 1×3 + 5×1 = 6 + 6 + 8 + 3 + 5 = 28. Not a multiple of 10, so the code is invalid.", hint: "The check digit is included in the total." },
  { q: "Weightings 1, 3, 1, 3. Find the check digit for 9150.", a: 3, sol: "9 + 3 + 5 + 0 = 17. 17 leaves 7. 10 − 7 = 3.", hint: "Find the total first." },
  { q: "A payload is 10110110. How many 1-bits will the CRC count?", a: 5, sol: "1, 0, 1, 1, 0, 1, 1, 0 has five 1s.", hint: "Count only the 1s." },
  { q: "A packet's trailer says 0A. The receiver counts 11 one-bits. Enter 1 if the CRC matches and 0 if it does not.", a: 0, sol: "0A is 10 in decimal. The receiver counted 11, so they do not match and the packet is requested again.", hint: "Convert 0A to decimal first." },
  { q: "Weightings 1, 3, 1, 3, 1. The code 48271 is typed. What is the total?", a: 52, sol: "4 + 24 + 2 + 21 + 1 = 52. Not a multiple of 10, so it is rejected.", hint: "Apply the weights to all five digits." },
] });

(() => {
  const OPT = { e: "Data entry: check digit", t: "Transmission: parity, checksum, CRC or echo check", l: "Transmission: timeout and re-send" };
  const SC = [
    ["Staff type 4172 as 4712", "e", "A person made the slip before the data was sent, so a check digit is the check."],
    ["A scanner misreads one digit of a barcode", "e", "Scanning is data entry. The check digit makes the till beep for a re-scan."],
    ["A digit is left out when a membership number is typed", "e", "An omitted digit is a data entry error."],
    ["15 is typed instead of 50 because the words sound alike", "e", "A phonetic error is a data entry error."],
    ["Interference changes a bit in a packet's payload", "t", "The data was right when sent and changed on the way. Parity, checksum, CRC or echo check compare received with sent."],
    ["Bits sent in parallel arrive at different times", "t", "Skew is a transmission error. The data is re-sent."],
    ["The copy that an echo check returns differs from the original", "t", "The sender compares the copy with the original, which is a transmission check."],
    ["An extra packet arrives that was never sent", "t", "Gained data is a transmission error."],
    ["A packet is dropped and never arrives", "l", "There is nothing to check. No acknowledgement arrives, so the timeout re-sends."],
    ["No acknowledgement comes back, so the sender keeps waiting", "l", "The timeout runs out and the sender re-sends automatically."],
  ];
  const el = $("#drill");
  el.innerHTML = `<div class="qline" aria-live="polite"></div>
    <div class="row"><select data-s class="sel" aria-label="Answer"><option value="">Choose…</option>${Object.entries(OPT).map(([k, v]) => `<option value="${k}">${v}</option>`).join("")}</select><button class="b pri" data-a="c">Check</button><button class="b" data-a="n">New question</button><span class="fb" aria-live="polite"></span></div><p class="note" data-st></p><p class="note" data-w></p>`;
  const ql = $(".qline", el), sl = $("[data-s]", el), fb = $(".fb", el), st = $("[data-st]", el), wk = $("[data-w]", el);
  let cur, streak = 0, best = 0, solved = false;
  function gen() {
    const prev = cur; do { cur = pick(SC); } while (cur === prev);
    solved = false; ql.innerHTML = `Situation: <b>${cur[0]}</b>. Which stage and check?`; sl.value = ""; fb.textContent = ""; fb.className = "fb"; wk.innerHTML = "";
  }
  $("[data-a=c]", el).onclick = () => {
    if (!sl.value) return;
    const good = sl.value === cur[1]; if (!solved) { streak = good ? streak + 1 : 0; best = Math.max(best, streak); } if (good) solved = true;
    fb.textContent = good ? "✓ Correct" : "✗ Not quite"; fb.className = "fb " + (good ? "ok" : "no"); st.textContent = `Streak ${streak} · best ${best}`;
    if (good) wk.innerHTML = cur[2];
  };
  $("[data-a=n]", el).onclick = gen; gen();
})();

Lib.quiz($("#qz1"), { qs: [
  { q: "Which check is used when a person types a code?", opts: ["Parity bit", "Check digit", "Checksum", "Echo check"], a: 1, why: "A check digit is the data entry check. The others guard data in transit." },
  { q: "A code is mistyped, then sent over a network with a checksum. What happens?", opts: ["The checksum finds the mistake", "The checksum passes it, because the data arrives as sent", "The data is lost", "The receiver corrects the digit"], a: 1, why: "The checksum compares received with sent. The wrong code travels perfectly." },
  { q: "Which is a data entry error?", opts: ["Skew", "Lost packet", "Transposed digits", "Gained data"], a: 2, why: "Transposition happens when a person types two digits in the wrong order." },
  { q: "Which is a data transmission error?", opts: ["Phonetic error", "Omitted digit", "Corrupted data", "Extra digit typed"], a: 2, why: "Corrupted data is bits changing on the way." },
  { q: "Does a check digit need extra data to be sent with the message?", opts: ["Yes, a copy of the code", "Yes, a trailer", "No, the digit is already part of the code", "Yes, a parity byte"], a: 2, why: "The check digit is the last digit of the code. Transmission checks add data." },
  { q: "A packet is lost. Which part of the system notices?", opts: ["The check digit", "The sender's timeout", "The parity bit", "The keyboard"], a: 1, why: "No packet means no check, so the sender's timeout is what triggers a re-send." },
  { q: "What is the usual fix when a check digit test fails?", opts: ["Send the data again", "Re-enter or re-scan the code", "Flip a bit", "Wait for a timeout"], a: 1, why: "Data entry errors are fixed by typing or scanning the code again." },
  { q: "Which statement is true?", opts: ["A check digit catches every error", "A transmission check shows data was typed correctly", "A check digit catches most typing errors but not all", "A CRC finds typing mistakes"], a: 2, why: "Two neighbouring digits that differ by 5 can swap without changing the total." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Data entry error", "A mistake made when a person types, or a scanner reads, a code, before the data is sent."],
  ["Data transmission error", "A change to the data while it travels, such as corrupted, lost or gained data, or skew."],
  ["Check digit", "The final digit of a code, calculated from the other digits, used to detect data entry errors."],
  ["Weighting", "The number each digit is multiplied by in a check digit calculation, for example 1 and 3 in turn."],
  ["Transposition", "Two digits entered in the wrong order, such as 5037 for 5307."],
  ["Phonetic error", "A mistake caused by words that sound alike, such as thirteen and thirty."],
  ["Corrupted data", "Data in which one or more bits have changed value during transmission."],
  ["Skew", "Bits sent in parallel arriving at slightly different times, which can corrupt the data."],
  ["Parity check", "Checking that each byte has an agreed even or odd number of 1-bits."],
  ["Checksum", "A value calculated from a block of data and sent with it, to be recalculated and compared by the receiver."],
  ["CRC", "A cyclic redundancy check: the count of 1-bits in a packet's payload is stored in the trailer and recounted by the receiver."],
  ["Echo check", "The receiver sends a copy of the data back and the sender compares it with the original."],
  ["Automatic repeat request (ARQ)", "A method that uses acknowledgements and a timeout to re-send data that was not received correctly."],
  ["Timeout", "The time a sender waits for an acknowledgement before re-sending."],
] });
