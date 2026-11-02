const MONO = "font-family:ui-monospace,Menlo,Consolas,monospace;";
const rint = (n) => Math.floor(Math.random() * n);
const dv = (c) => (c === "X" || c === "x" ? 10 : +c);
const w13 = (i) => (i % 2 ? 3 : 1);
const tot13 = (s) => [...s].reduce((a, c, i) => a + dv(c) * w13(i), 0);
const cd13 = (d) => (10 - (tot13(d) % 10)) % 10;
const tot11 = (s) => [...s].reduce((a, c, i) => a + dv(c) * (s.length - i), 0);   // weights count down to 1 at the check digit
const cd11 = (d) => { const t = [...d].reduce((a, c, i) => a + +c * (d.length + 1 - i), 0); return (11 - (t % 11)) % 11; };
const sym = (n) => (n === 10 ? "X" : String(n));
const ok13 = (s) => /^\d{13}$/.test(s) && tot13(s) % 10 === 0;
const ok11 = (s) => /^\d+X?$/i.test(s) && s.length > 1 && tot11(s) % 11 === 0;
const rdig = (n) => Array.from({ length: n }, () => rint(10)).join("");

/* ---------- Watch: step-through of the working ---------- */
const CX = 150, CW = 34, CG = 4, cx = (i) => CX + i * (CW + CG);
function calcDraw(digs, wts, k, mod, cdv) {
  let s = SV.text(20, 48, "Digit", "sm", { "text-anchor": "start" });
  [...digs].forEach((c, i) => { s += SV.rect(cx(i), 24, CW, 36, "cell", { rx: 6 }) + SV.text(cx(i) + CW / 2, 49, c, "lbl bd", { "text-anchor": "middle", style: MONO + "font-size:17px" }); });
  const n = digs.length, prods = [...digs].map((c, i) => dv(c) * wts[i]), total = prods.reduce((a, b) => a + b, 0);
  if (k >= 1) { s += SV.text(20, 96, "Weight", "sm", { "text-anchor": "start" }); wts.forEach((w, i) => (s += SV.text(cx(i) + CW / 2, 96, w, "lbl bd t1", { "text-anchor": "middle", style: MONO }))); }
  if (k >= 2) { s += SV.text(20, 132, "Product", "sm", { "text-anchor": "start" }); prods.forEach((p, i) => (s += SV.text(cx(i) + CW / 2, 132, p, "lbl bd", { "text-anchor": "middle", style: MONO }))); }
  if (k >= 3) s += SV.text(20, 176, "Total = " + total, "lbl bd", { "text-anchor": "start" });
  if (k >= 4) s += SV.text(20, 206, `${total} ÷ ${mod} leaves ${total % mod}`, "lbl bd", { "text-anchor": "start" });
  if (k >= 5) {
    s += SV.rect(cx(n), 24, CW, 36, "cell cell-ok", { rx: 6 }) + SV.text(cx(n) + CW / 2, 49, cdv, "lbl bd", { "text-anchor": "middle", style: MONO + "font-size:17px" });
    s += SV.text(20, 236, `Check digit = ${mod} − ${total % mod} = ${cdv}`, "lbl bd t3", { "text-anchor": "start" });
  }
  return s;
}
const D13 = "978030640615", W13 = [...D13].map((_, i) => w13(i)), C13 = cd13(D13);
Lib.stepper($("#stA"), {
  w: 700, h: 260, label: "Working out an ISBN-13 check digit", base: { k: 0 }, tween: 1, dwell: 3400,
  draw: (s) => calcDraw(D13, W13, Math.round(s.k), 10, C13),
  steps: [
    "The first 12 digits of the ISBN-13: <b>978030640615</b>.",
    "Give the digits weightings of <b>1 and 3</b> in turn, starting with 1.",
    "Multiply each digit by its weighting.",
    "Add the products: the total is <b>93</b>.",
    "Divide by 10. The remainder is 3.",
    "Check digit = 10 − 3 = <b>7</b>. The full ISBN-13 is 9780306406157.",
  ].map((cap, k) => ({ cap, s: { k } })),
});

const D11 = "030640615", W11 = [...D11].map((_, i) => 10 - i), C11 = cd11(D11);
function bDraw(k) {
  if (k <= 5) return calcDraw(D11, W11, k, 11, sym(C11));
  const full = D11 + C11, wts = [...full].map((_, i) => 10 - i), prods = [...full].map((c, i) => dv(c) * wts[i]), t = prods.reduce((a, b) => a + b, 0);
  let s = SV.text(20, 48, "Digit", "sm", { "text-anchor": "start" }) + SV.text(20, 96, "Weight", "sm", { "text-anchor": "start" }) + SV.text(20, 132, "Product", "sm", { "text-anchor": "start" });
  [...full].forEach((c, i) => {
    s += SV.rect(cx(i), 24, CW, 36, i === 9 ? "cell cell-ok" : "cell", { rx: 6 }) + SV.text(cx(i) + CW / 2, 49, c, "lbl bd", { "text-anchor": "middle", style: MONO + "font-size:17px" });
    s += SV.text(cx(i) + CW / 2, 96, wts[i], "lbl bd t1", { "text-anchor": "middle", style: MONO }) + SV.text(cx(i) + CW / 2, 132, prods[i], "lbl bd", { "text-anchor": "middle", style: MONO });
  });
  return s + SV.text(20, 176, "Total = " + t, "lbl bd", { "text-anchor": "start" }) + SV.text(20, 206, `${t} ÷ 11 = ${t / 11} remainder ${t % 11}`, "lbl bd", { "text-anchor": "start" }) + SV.text(20, 236, "Remainder 0, so the code is valid ✓", "lbl bd t3", { "text-anchor": "start" });
}
Lib.stepper($("#stB"), {
  w: 700, h: 260, label: "Working out and then testing a modulo-11 check digit", base: { k: 0 }, tween: 1, dwell: 3400,
  draw: (s) => bDraw(Math.round(s.k)),
  steps: [
    "The first 9 digits of an ISBN-10: <b>030640615</b>.",
    "Give weightings counting down from <b>10 to 2</b>.",
    "Multiply each digit by its weighting.",
    "Add the products: the total is <b>130</b>.",
    "Divide by 11. 11 × 11 = 121, so the remainder is 9.",
    "Check digit = 11 − 9 = <b>2</b>. The full ISBN-10 is 0306406152.",
    "<b>Testing</b>: the check digit joins the sum with weighting 1. The total is 132 = 12 × 11, so the code is valid.",
  ].map((cap, k) => ({ cap, s: { k } })),
});

/* ---------- Lab 1: ISBN-13 ---------- */
(() => {
  const el = $("#l1i");
  const draw = () => {
    const d = el.value.replace(/\D/g, "").slice(0, 12);
    if (d.length < 12) { $("#l1t").innerHTML = ""; $("#l1v").textContent = `Enter 12 digits (${d.length} so far).`; return; }
    const t = tot13(d), r = t % 10, cd = cd13(d);
    $("#l1t").innerHTML = `<tr><th>Digit</th>${[...d].map((c) => `<td>${c}</td>`).join("")}</tr><tr><th>Weight</th>${[...d].map((_, i) => `<td>${w13(i)}</td>`).join("")}</tr><tr><th>Product</th>${[...d].map((c, i) => `<td>${+c * w13(i)}</td>`).join("")}</tr>`;
    $("#l1v").innerHTML = `Total ${t}. ${t} ÷ 10 leaves ${r}. ${r === 0 ? "Remainder 0, so the check digit is 0." : `10 − ${r} = <b>${cd}</b>.`} Full ISBN-13: <b>${d}${cd}</b>`;
  };
  el.oninput = draw; draw();
})();

/* ---------- Lab 2: modulo-11 ---------- */
(() => {
  const el = $("#l2i");
  const draw = () => {
    const d = el.value.replace(/\D/g, "").slice(0, 12);
    if (d.length < 2) { $("#l2t").innerHTML = ""; $("#l2v").textContent = "Enter at least 2 digits."; return; }
    const ws = [...d].map((_, i) => d.length + 1 - i), t = [...d].reduce((a, c, i) => a + +c * ws[i], 0), r = t % 11, cd = cd11(d);
    $("#l2t").innerHTML = `<tr><th>Digit</th>${[...d].map((c) => `<td>${c}</td>`).join("")}</tr><tr><th>Weight</th>${ws.map((w) => `<td>${w}</td>`).join("")}</tr><tr><th>Product</th>${[...d].map((c, i) => `<td>${+c * ws[i]}</td>`).join("")}</tr>`;
    $("#l2v").innerHTML = `Total ${t}. ${t} ÷ 11 leaves ${r}. ${r === 0 ? "Remainder 0, so the check digit is 0." : `11 − ${r} = ${11 - r}${11 - r === 10 ? ", written as <b>X</b>" : ""}.`} Full code: <b>${d}${sym(cd)}</b>`;
  };
  el.oninput = draw; draw();
})();

/* ---------- Lab 3: is it valid? ---------- */
(() => {
  const el = $("#l3i"), m = $("#l3m");
  const draw = () => {
    const s = el.value.replace(/[^0-9Xx]/g, "").toUpperCase();
    if (m.value === "13") {
      if (!/^\d{13}$/.test(s)) { $("#l3t").innerHTML = ""; $("#l3v").textContent = `An ISBN-13 has 13 digits (${s.length} so far).`; return; }
      $("#l3t").innerHTML = `<tr><th>Digit</th>${[...s].map((c) => `<td>${c}</td>`).join("")}</tr><tr><th>Weight</th>${[...s].map((_, i) => `<td>${w13(i)}</td>`).join("")}</tr><tr><th>Product</th>${[...s].map((c, i) => `<td>${+c * w13(i)}</td>`).join("")}</tr>`;
      const t = tot13(s);
      $("#l3v").innerHTML = `Total ${t}. ${t % 10 === 0 ? `<span class="v y">A multiple of 10: valid</span>` : `<span class="v n">Remainder ${t % 10} when divided by 10: invalid</span>`}`;
    } else {
      if (!/^\d+X?$/.test(s) || s.length < 2) { $("#l3t").innerHTML = ""; $("#l3v").textContent = "Enter digits (X is allowed only as the last character)."; return; }
      const ws = [...s].map((_, i) => s.length - i);
      $("#l3t").innerHTML = `<tr><th>Digit</th>${[...s].map((c) => `<td>${c}</td>`).join("")}</tr><tr><th>Weight</th>${ws.map((w) => `<td>${w}</td>`).join("")}</tr><tr><th>Product</th>${[...s].map((c, i) => `<td>${dv(c) * ws[i]}</td>`).join("")}</tr>`;
      const t = tot11(s);
      $("#l3v").innerHTML = `Total ${t}. ${t % 11 === 0 ? `<span class="v y">A multiple of 11: valid</span>` : `<span class="v n">Remainder ${t % 11} when divided by 11: invalid</span>`}`;
    }
  };
  el.oninput = m.onchange = draw;
  const set = (v, mm) => { el.value = v; m.value = mm; draw(); };
  $("#l3a").onclick = () => set("9780306406157", "13");
  $("#l3b").onclick = () => set("080442957X", "11");
  $("#l3c").onclick = () => set("9780306406158", "13");
  draw();
})();

/* ---------- Lab 4: which method catches more swaps? ---------- */
(() => {
  let d = rdig(12), dist = 1;
  function rate(code, valid) {
    let tries = 0, caught = 0;
    for (let i = 0; i + dist < code.length; i++) {
      const j = i + dist; if (code[i] === code[j] || code[i] === "X" || code[j] === "X") continue;
      const a = [...code]; [a[i], a[j]] = [a[j], a[i]]; tries++; if (!valid(a.join(""))) caught++;
    }
    return { tries, caught, pct: tries ? (100 * caught) / tries : 100 };
  }
  function draw(n) {
    if (n) dist = n;
    const c13 = d + cd13(d), c11 = d + sym(cd11(d));
    $("#l4o").innerHTML = [["ISBN-13 (modulo-10)", c13, rate(c13, ok13)], ["Modulo-11", c11, rate(c11, ok11)]].map(([nm, c, r]) => `<div class="o"><b>${nm}</b><div class="bar"><i style="width:${r.pct}%"></i></div><span>${r.caught} of ${r.tries} caught</span></div><div class="note" style="margin:-4px 0 4px">Code ${c}</div>`).join("");
    $("#l4v").innerHTML = `Swapping two digits <b>${dist}</b> place${dist > 1 ? "s" : ""} apart. ` + (dist % 2 === 0 ? "Digits an even distance apart share a weighting in ISBN-13, so swapping them never changes the total: <b>ISBN-13 misses every one</b>. " : "In ISBN-13 a swap is only missed when the two digits differ by 5. ") + "Modulo-11 gives every position its own weighting, so it catches them all.";
  }
  Lib.slider($("#l4s"), { id: "l4d", label: "Distance between the swapped digits: ", min: 1, max: 6, step: 1, value: 1, onInput: draw });
  $("#l4n").onclick = () => { d = rdig(12); draw(); };
  draw();
})();

Lib.codePanel($("#l5"), {
  pseudo: [
    "FUNCTION Valid13(Code : STRING) RETURNS BOOLEAN",
    "   Total ← 0",
    "   FOR Position ← 1 TO 13",
    "      Digit ← STRING_TO_NUM(MID(Code, Position, 1))",
    "      IF Position MOD 2 = 1 THEN Total ← Total + Digit",
    "      ELSE Total ← Total + Digit * 3",
    "   NEXT Position",
    "   RETURN Total MOD 10 = 0",
    "ENDFUNCTION",
    "",
    "FUNCTION Valid11(Code : STRING) RETURNS BOOLEAN",
    "   Total ← 0",
    "   FOR Position ← 1 TO LENGTH(Code)",
    "      Ch ← MID(Code, Position, 1)",
    "      IF Ch = \"X\" THEN Digit ← 10 ELSE Digit ← STRING_TO_NUM(Ch)",
    "      Total ← Total + Digit * (LENGTH(Code) - Position + 1)",
    "   NEXT Position",
    "   RETURN Total MOD 11 = 0",
    "ENDFUNCTION",
  ],
  py: [
    "def valid13(code):",
    "    total = sum(int(c) * (1 if i % 2 == 0 else 3) for i, c in enumerate(code))",
    "    return total % 10 == 0",
    "",
    "def valid11(code):",
    "    n = len(code)",
    "    total = sum((10 if c == 'X' else int(c)) * (n - i) for i, c in enumerate(code))",
    "    return total % 11 == 0",
    "",
    "print(valid13('9780306406157'))   # True",
    "print(valid11('0306406152'))      # True",
    "print(valid11('080442957X'))      # True: the X stands for 10",
  ],
});

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Drag each feature to the method it describes.", buckets: [{ label: "ISBN-13 (modulo-10)" }, { label: "Modulo-11" }], items: [
  { text: "Weightings alternate 1, 3", b: 0 }, { text: "Divide the total by 10", b: 0 }, { text: "Check digit is always 0 to 9", b: 0 }, { text: "Misses swaps of digits that differ by 5", b: 0 }, { text: "Used on supermarket barcodes", b: 0 },
  { text: "Weightings count down", b: 1 }, { text: "Divide the total by 11", b: 1 }, { text: "Check digit can be X", b: 1 }, { text: "Catches every swap of two digits", b: 1 }, { text: "Used on older 10-digit ISBNs", b: 1 },
], done: "Same steps, different weightings and divisor." });

Lib.match($("#m1"), { prompt: "Match each term to what it means.", pairs: [
  ["Weighting", "The number a digit is multiplied by"], ["Total", "The sum of every digit × weighting"], ["Remainder", "What is left after dividing the total"],
  ["Check digit", "Divisor minus the remainder"], ["X", "A check digit of 10 in modulo-11"], ["Testing a code", "Include the check digit with weighting 1"],
] });

Lib.order($("#o1"), { prompt: "Put the steps for making a modulo-11 check digit in order.", items: [
  "Give each digit a weighting, counting down to 2", "Multiply each digit by its weighting", "Add the products to get the total", "Divide the total by 11 and find the remainder", "Subtract the remainder from 11 (write X for 10)",
], done: "Weight, multiply, add, divide, subtract." });

Lib.calc($("#c1"), { qs: [
  { q: "ISBN-13 first 12 digits 978013110362. What is the total of the digits × 1 and 3 in turn?", a: 73, sol: "9 + 21 + 8 + 0 + 1 + 9 + 1 + 3 + 0 + 9 + 6 + 6 = 73.", hint: "Odd positions ×1, even positions ×3." },
  { q: "The total is 73. What is the ISBN-13 check digit?", a: 7, sol: "73 ÷ 10 leaves 3. 10 − 3 = 7." },
  { q: "Modulo-11, digits 48215, weights 6, 5, 4, 3, 2. What is the total?", a: 85, sol: "24 + 40 + 8 + 3 + 10 = 85." },
  { q: "The total is 85. What is the modulo-11 check digit?", a: 3, sol: "85 ÷ 11 = 7 remainder 8. 11 − 8 = 3." },
  { q: "A modulo-11 total is 125. What is the check digit?", a: 7, sol: "125 ÷ 11 = 11 remainder 4. 11 − 4 = 7." },
  { q: "A modulo-11 total is 132 for a complete code. Enter 1 if the code is valid and 0 if not.", a: 1, sol: "132 = 12 × 11, so the remainder is 0 and the code is valid." },
  { q: "A modulo-11 total is 71. What is the remainder?", a: 5, sol: "11 × 6 = 66. 71 − 66 = 5, so the code is invalid." },
] });

(() => {
  const el = $("#drill");
  el.innerHTML = `<div class="qline" aria-live="polite"></div>
    <div class="row"><input class="inp" data-i maxlength="2" aria-label="Check digit" style="width:4em"><button class="b pri" data-a="c">Check</button><button class="b" data-a="n">New question</button><span class="fb" aria-live="polite"></span></div><p class="note" data-st></p><p class="note" data-w></p>`;
  const ql = $(".qline", el), inp = $("[data-i]", el), fb = $(".fb", el), st = $("[data-st]", el), wk = $("[data-w]", el);
  let cur, streak = 0, best = 0, solved = false;
  function gen() {
    cur = rdig(4); solved = false; ql.innerHTML = `Modulo-11 with weightings 5, 4, 3, 2. Find the check digit (use X for 10) for <b style="font-family:var(--mono)">${cur}</b>`; inp.value = ""; fb.textContent = ""; fb.className = "fb"; wk.innerHTML = "";
  }
  $("[data-a=c]", el).onclick = () => {
    if (!inp.value) return;
    const t = [...cur].reduce((a, c, i) => a + +c * (5 - i), 0), ans = sym(cd11(cur)), v = inp.value.trim().toUpperCase(), good = v === ans || (ans === "X" && v === "10");
    if (!solved) { streak = good ? streak + 1 : 0; best = Math.max(best, streak); } if (good) solved = true;
    fb.textContent = good ? "✓ Correct" : "✗ Not quite"; fb.className = "fb " + (good ? "ok" : "no"); st.textContent = `Streak ${streak} · best ${best}`;
    if (good) wk.innerHTML = `Total ${t}; ${t} ÷ 11 leaves ${t % 11}; ${t % 11 === 0 ? "check digit 0" : `11 − ${t % 11} = ${11 - (t % 11)}`}.`;
  };
  $("[data-a=n]", el).onclick = gen; gen();
})();

Lib.quiz($("#qz1"), { qs: [
  { q: "Which weightings does ISBN-13 use?", opts: ["10 down to 2", "1 and 3 in turn", "All 1", "2 and 5 in turn"], a: 1, why: "Alternating 1 and 3, starting with 1." },
  { q: "What do you divide by in the modulo-11 method?", opts: ["10", "11", "13", "9"], a: 1, why: "Modulo-11 divides by 11." },
  { q: "A modulo-11 total is 77. What is the check digit?", opts: ["0", "11", "X", "7"], a: 0, why: "77 = 7 × 11, remainder 0, so the check digit is 0 (not 11)." },
  { q: "Why can an ISBN-10 end in X?", opts: ["The code is invalid", "The check digit can be 10", "It is a spare letter", "It means the book is old"], a: 1, why: "X stands for 10, which would otherwise take two characters." },
  { q: "To test a code, the check digit is…", opts: ["Left out of the total", "Included with its weighting", "Doubled", "Subtracted"], a: 1, why: "It is part of the sum. A valid code gives a multiple of 10 (or 11)." },
  { q: "Which method catches every swap of two digits?", opts: ["ISBN-13", "Modulo-11", "Both", "Neither"], a: 1, why: "Every position has a different weighting, and 11 is prime." },
  { q: "Which swap can slip past ISBN-13?", opts: ["3 and 4 side by side", "2 and 7 side by side", "1 and 9 side by side", "6 and 8 side by side"], a: 1, why: "2 and 7 differ by 5, so the total changes by 10 and is still a multiple of 10." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Check digit", "The final digit of a code, calculated from the others, used to detect data entry errors."],
  ["Weighting", "The number a digit is multiplied by when a check digit is calculated."],
  ["Modulo-10 / ISBN-13", "Weightings of 1 and 3 in turn; the total of all digits must be a multiple of 10."],
  ["Modulo-11", "Weightings counting down; the total of all digits must be a multiple of 11."],
  ["Remainder", "What is left after dividing the total by 10 or 11."],
  ["X", "The symbol for a modulo-11 check digit of 10."],
  ["ISBN", "International Standard Book Number: 13 digits now, 10 digits on older books."],
  ["Transposition", "Two digits entered in the wrong order."],
] });
